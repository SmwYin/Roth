# Roth.Θ_option_le — BORDERLINE-needs-human

Canonical214, Roth/Theta.lean:593. This is a completed read-only assessment. Production Lean and versions are unchanged. The named recursive Lemma6 endpoint combines a substantive arithmetic rank witness with existing supremum/finite-maximum transport. Retain it locally while deciding the audience/interface of any upstream contribution; future design questions do not block this review.

## Phase 0 — Baseline and native resolution

The successful shared baseline completed2467 jobs. All17 production-source/version-pin hashes were freshly recomputed and match it. Lean4.34.0 and mathlib5ed2965256430c3649e86755f9576b54eca72435 are retained. The entire985-line declaring module and sole actual caller were read. It defines the bounded-integer-polynomial index supremum and proves Lemmas5–7 feeding Roth's theorem. The target has no sorry. [Baseline](../evidence/Roth.Θ_option_le/baseline-build.txt), [fresh hashes](../evidence/Roth.Θ_option_le/inputs.json), [full source](../evidence/Roth.Θ_option_le/source-module.lean.txt), [target metadata](../evidence/Roth.Θ_option_le/target-metadata.json).

The original native execution replays the complete module in a fresh namespace, changing only the namespace/target name, and checks axioms of every public replay declaration. The original type and kernel proof are printed without a printer-elision marker. The first response was an incomplete warmup, explicitly excluded; the following response was complete, nonpartial and clean. [Original source](../evidence/Roth.Θ_option_le/original-executed.lean.txt), [receipt](../evidence/Roth.Θ_option_le/original-receipt.json), [excluded warmup](../evidence/Roth.Θ_option_le/original-warming-receipt.json).

Full native statement:

~~~lean
∀ {τ : Type u_2} [inst : Fintype τ] {δ : ℝ},
  0 ≤ δ →
    δ ≤ 1 →
      ∀ {r : Option τ → ℕ},
        3 ≤ ↑(r none) →
          (∀ (j : τ), ↑(r none) ≤ δ * ↑(r (some j))) →
            ∀ {r₁ : ℕ},
              (∀ (j : Option τ), r j ≤ r₁) →
                ∀ {q : Option τ → ℕ},
                  (∀ (j : Option τ), 0 < q j) →
                    ∀ {B : ℝ},
                      1 ≤ B →
                        Roth.Θ B q r ≤
                          2 *
                            (Finset.Icc 1 (r none + 1)).sup' ⋯ fun l ↦
                              Roth.lem6Φ q r (Roth.lem6M (Fintype.card τ + 1) r₁ B l) l +
                                  √(Roth.lem6Φ q r (Roth.lem6M (Fintype.card τ + 1) r₁ B l) l) +
                                √δ
~~~

The finite-supremum nonempty proof prints as ⋯, hiding proof-irrelevant evidence rather than a mathematical hypothesis. All accepted axioms lie in propext, Classical.choice and Quot.sound.

## Phase 1 — Mathematical content

Natural degree/weight bounds are attached to a distinguished variable and a finite complementary family. Suppose the distinguished weight is at least3, each complementary weight is sufficiently large through0≤δ≤1, all weights have uniform ceiling r₁, denominators are positive, and coefficient bound B≥1. Then the supremum of indices of admissible integer polynomials at coprime rational tuples is at most twice the maximum of Φ(l)+√Φ(l)+√δ over1≤l≤r_none+1. The quantity Φ is the sum of the distinguished one-variable and complementary-variable suprema at enlarged height M(l), producing dimension reduction.

The written proof uses Θ_le_of_forall_index_le to reduce the supremum claim to each polynomial/numerator tuple, index_le_lem6 to supply the arithmetic rank witness, Finset.le_sup' to dominate that rank by the finite maximum, and mul_le_mul_of_nonneg_left to multiply by2. The determinant/height mathematics lives in the project theorem index_le_lem6; it is not supplied by the order lemmas.

## Phase 2 — Preliminary checks

BIG: the module docstring lists this named Lemma6 as a main result. The one-line-definition test is n/a for theorem kind. Its four proof steps do not establish redundancy from existing mathlib because the rank witness is project mathematics. Literature width remains exhaustive.

## Phase 3 — Exhaustive literature

Exact requests, returned-response SHA256/bytes, clean complete locators, access status and original summaries are saved; no full article/search bodies are archived. Returned locator query strings are omitted to avoid signed credentials.

| Channel | Actual query/form | Result |
|---|---|---|
| Specific web | Roth theorem lemma6 index polynomial Theta supremum2 Phi square root delta | Weighted-index/Wronskian primary locators; exact constants in local manuscript |
| General web1 | Roth lemma index polynomial Wronskian height recursive bound | AMS chapter describes small-index/coefficient-height mechanism |
| General web2 | supremum pointwise existential finite maximum bound ordered set | Elementary order transport, not arithmetic witness |
| General web3 | Thue Siegel Roth polynomial index lemma induction coefficients bounded height | Diophantine index-lemma setting |
| Aliases | Roth lemma Dyson lemma index polynomials auxiliary polynomial recursive estimate | Related Dyson/product methods, different hypotheses/endpoints |
| ChatGPT math MCP | n/a, optional ask_chatgpt_math unavailable | All other named channels completed |
| Local clean.tex | §5, Lemma roth:lem6; eqs13–16 and subsequent induction | Exact finite maximum, M and Φ |
| nLab | site:ncatlab.org/nlab supremum order finite maximum valuation polynomial | Valuation/order/join context; usual zero valuation is infinity |
| nCatLab | site:ncatlab.org/ncatlab supremum order polynomial index Roth | Distinct namespace queried; returned chiefly /nlab material, no exact /ncatlab endpoint |
| Stacks | site:stacks.math.columbia.edu order vanishing polynomial valuation supremum | Section02MB length-based orders, not integer-height recursion |
| MathOverflow | site:mathoverflow.net Roth lemma polynomial index Wronskian Dyson | Quantitative Roth/Dyson pointers; not used as primary proof authority |
| Recent arXiv | Roth lemma polynomial index height Dyson, after2021-10-28 before2026-10-29 | Mostly unrelated hits; two narrower Roth+Wronskian and Roth+Diophantine+index queries returned empty |

[Specific](../evidence/Roth.Θ_option_le/web-specific.json), [general](../evidence/Roth.Θ_option_le/web-general.json), [aliases](../evidence/Roth.Θ_option_le/web-aliases.json), [nLab](../evidence/Roth.Θ_option_le/nlab.json), [nCatLab](../evidence/Roth.Θ_option_le/ncatlab.json), [Stacks](../evidence/Roth.Θ_option_le/stacks.json), [MathOverflow](../evidence/Roth.Θ_option_le/mathoverflow.json), [arXiv](../evidence/Roth.Θ_option_le/arxiv.json), [narrow retry](../evidence/Roth.Θ_option_le/arxiv-retry.json), [local excerpt](../evidence/Roth.Θ_option_le/local-literature.txt).

Primary [Min Ru Roth notes](https://www.math.uh.edu/~minru/fields/roth.pdf), pp2–4, define weighted index and coefficient height and state a small-index Roth lemma. [Stacks02MB](https://stacks.math.columbia.edu/tag/02MB) defines length-based vanishing orders. These contextual sources are not claimed to state the exact recursive constants. Princeton's PDF timed out400; AMS's PDF returned403; nLab valuation direct open failed400 unsupported XHTML; an attempted Stanford locator was inaccessible. [Primary statuses](../evidence/Roth.Θ_option_le/primary.json), [additional statuses](../evidence/Roth.Θ_option_le/primary-extra.json).

Synthesis: the standard context is Roth's bounded-height weighted-index lemma and recursive dimension reduction. Modern Dyson/product arguments are related alternatives, not identical formulas. The most general elementary outer law bounds a conditional supremum from pointwise finite witnesses. It assumes rather than proves the arithmetic witness. Search results establish neither nonexistence nor historical/maximal generality.

## Phases 4a and 5.5c — Every parameter and assumption

| Parameter/constraint | Role | Audit |
|---|---|---|
| τ:Type u | Complementary variables | Already universe-polymorphic; arbitrary index type in isolated outer theorem |
| Fintype τ | Existing index/Θ interface, finite dimension in M | Retained here; no finiteness on the polynomial-family index in abstract transport |
| DecidableEq τ | Absent from native type | Already omitted |
| δ:ℝ | Weight-ratio error/square-root term | Existing real Θ and sqrt interfaces retained |
| hδ0:0≤δ | Pointwise derivative-weight/positivity argument | Retained, no necessity claim; nonempty τ permits a separate ratio inference, but empty τ requires care |
| hδ1:δ≤1 | Pointwise numerical estimate | Retained, no global sharpness claim |
| r:Option τ→ℕ | Degree bounds/inverse weights | Naturals retained; abstract outer law independent of degrees |
| hrp:3≤r_none | Original numerical threshold | Jointly weakened to1 by a complete replay carrying213's new half-quadratic finite-sum proof |
| hratio | Distinguished/complementary ratio | Retained in all verified arithmetic variants |
| r₁,hr₁ | Uniform ceiling determines M | Retained; no minimality claim |
| q:Option τ→ℕ | Denominators in every Θ term | Arbitrary natural q in broader form, including0 with total division/existing coprimality |
| hq:∀j,0<qj | Passed to unused pointwise premise | Removed jointly with other improvements; actual caller/final Θ_lt statements preserved |
| B:ℝ,hB:1≤B | Height/nonempty family | hB removed by Real.sSup_le and nonnegative RHS; B<1 family empty and Θ=0 freshly proved |
| Integer coefficients/real output | Integer discreteness, real supremum/sqrt | Arithmetic representation retained; abstract order generality does not generalize factor heights to arbitrary rings |
| Nonzero, degree, height, coprimality predicates | Full admissible family | All retained in pointwise witness, none silently dropped |

## Phase 4b — Verified broadening

STRICTLY NARROWER than a verified sufficient interface: remove hq and hB and replace3≤(r none:ℝ) by1≤(r none:ℝ), retaining exactly the same conclusion and other premises.

The no-B proof unfolds outer Θ to sSup(indexSet...), applies existing Real.sSup_le, proves the pointwise witness bound, and proves0≤RHS from Θ_nonneg and sqrt nonnegativity at rank1. Icc1(r_none+1) is nonempty for every natural r_none; this fact is separate from the positive-weight condition required by the pointwise method. A separate guard derives B<1 emptiness from a nonzero integer coefficient of absolute value≥1, then Θ=0 from Real.sSup_empty. No invalid unconditional real-supremum monotonicity is used.

[No-B/no-q whole module](../evidence/Roth.Θ_option_le/broader-executed.lean.txt), [receipt](../evidence/Roth.Θ_option_le/broader-receipt.json), [joint positive-weight whole module](../evidence/Roth.Θ_option_le/lowdegree-executed.lean.txt), [receipt](../evidence/Roth.Θ_option_le/lowdegree-receipt.json), [small-B guards](../evidence/Roth.Θ_option_le/guards-executed.lean.txt), [receipt](../evidence/Roth.Θ_option_le/guards-receipt.json).

The lower-weight proof carries the complete new finite-sum and numerical proofs from accepted213, broadens both pointwise and recursive endpoints, and checks all later code with original caller/Θ_lt conclusions. These new/project proofs are not existing mathlib calls. This proves a broadening, not impossibility at zero weight, necessity of retained premises, arbitrary-ring arithmetic generality or maximality. Cost does not determine the verdict.

## Phase 4c — All nine modern-idiom rows

| # | Question | Result/downstream consequence |
|---|---|---|
|1| Typeclasses instead of premises? | No: numerical inequalities are local facts, not global structures |
|2| Filters instead of sequence/metric language? | No topology/convergence |
|3| Universal-property object? | Existing conditional-completeness interface suffices; no new object |
|4| Bundled substructure? | Nonzero bounded-height polynomials are not a submodule/subring |
|5| Weaker scalar hierarchy? | Outer transport works for any ConditionallyCompleteLinearOrder with nonempty source; real sqrt/integer arithmetic remains separate |
|6| Higher categories? | No concrete downstream gain |
|7| Generalized concrete indices? | Arbitrary finite set/function for outer law, rather than just natural Icc ranks; compiled independently |
|8| Concrete-via-abstract body diagnostic? | Zero bare Θ occurrences after opening helper; body uses supplied witness/order facts. Isolated arbitrary-set proof verifies this abstraction without hiding the arithmetic witness |
|9| False-generalization guard? | Nonempty source or nonnegative real bound needed. Compiled empty-source/-1 counterexample rejects removing both; weightedOrder zero=∞ distinguishes real index0=0 conventions |

No new generic wrapper contribution is needed: existing order lemmas already provide the abstract law. The useful local consequence is dropping B≥1; it does not fabricate a general arithmetic theorem.

## Phase 4.5 — Infrastructure

n/a for theorem kind. All six dimensions checked: no new instance diamond, reducible data, unfolding definition, priority path, data-universe restriction or coercion instance. A rejected inline helper escaped a universe; the corrected local helper is Type-specialized for the actual Fin caller. The public original remains universe-polymorphic.

## Phase 4.6 — Five proof-strategy rows

| # | Strategy | Result |
|---|---|---|
|1| ε–δ vs filters | No topology |
|2| Elements vs ideals/submodules | Height-bounded nonzero family is not a substructure; sets/suprema appropriate |
|3| Sequences vs nets | No limits |
|4| Concrete object vs universal property | No categorical construction |
|5| Missing reusable helper | No missing order primitive: Real.sSup_le, csSup_le and Finset.le_sup'_of_le suffice given the arithmetic witness. Determinant/order/factor-height/numerical candidates remain separate |

REFACTOR-RECOMMENDED locally to the verified broader interface, preserving the named dimension-reduction endpoint. Consider upstream arithmetic ingredients separately; no cost-based verdict.

## Phase 5 — Fifteen actual searches and parent re-aims

| Form | Lean-Finder | Loogle | LeanSearch | Source rg | Local pattern |
|---|---|---|---|---|---|
| Current recursive endpoint | Arithmetic/additive-combinatorial name collisions, no whole hit | Exact quoted target no hit | Mostly unrelated iSup/other hits | Full names no mathlib declaration | Actual project target; warming index |
| Standard index/height recursion | Degree/height/Chevalley ingredients | Finset.sup' order laws | Degree/max ingredients | Finite/real supremum laws | Sup' variants; warming index |
| Abstract pointwise finite witness→supremum bound | le_sup'_of_le,le_sup'_iff | Mixed query failed; simpler Finset retry hit | Real.sSup_le,sSup_le,finite sup | csSup_le,default-zero laws | Conditional supremum laws; warming index |

Exact request/raw formal-service response or untruncated command/stdout/exit is saved for every cell. [Current Finder](../evidence/Roth.Θ_option_le/search-current-leanfinder.json), [standard Loogle](../evidence/Roth.Θ_option_le/search-standard-loogle.json), [abstract failed query](../evidence/Roth.Θ_option_le/search-abstract-loogle.json), [retry](../evidence/Roth.Θ_option_le/search-abstract-loogle-retry.json), [abstract rg](../evidence/Roth.Θ_option_le/search-abstract-rg.json). The validator checks all remaining matrix files. External revisions differ from the pin, so positive ingredients are native-verified. Warming local indexes do not prove absence.

Parent re-aim explicitly applied: accepted Θ181 is SupSet.sSup; accepted index133 points toward AddMonoidAlgebra.infDegree. Existing Real.sSup_le/finite sup laws supply the analogous outer transport, verified independently. Five fresh infDegree/weightedOrder searches check the whole recursive height/rank law; native weightedOrder_mul is only a product ingredient. Neither parent supplies the full arithmetic witness, enlarged integer height or recursive two-family Φ endpoint. The whole target is therefore not NO merely because its last outer layer is generic order theory. [Parent Finder](../evidence/Roth.Θ_option_le/reaim-leanfinder.json), [Loogle](../evidence/Roth.Θ_option_le/reaim-loogle.json), [LeanSearch](../evidence/Roth.Θ_option_le/reaim-leansearch.json), [rg](../evidence/Roth.Θ_option_le/reaim-rg.json), [local](../evidence/Roth.Θ_option_le/reaim-local_search.json), [accepted Θ parent](../evidence/Roth.Θ_option_le/Theta-parent181-report.md.txt).

The isolated environment imports mathlib only and checks target absence. It proves conditional-order transport by csSup_le/le_sup'_of_le, real nonnegative-bound transport by Real.sSup_le/le_sup'_of_le, and the existing Finset.le_sup'_iff witness equivalence. It also verifies empty real supremum/zero infinite-valued order guards. [Isolated source](../evidence/Roth.Θ_option_le/isolated-executed.lean.txt), [receipt](../evidence/Roth.Θ_option_le/isolated-receipt.json), [pinned-source hashes](../evidence/Roth.Θ_option_le/mathlib-inputs.json). Search failure is not represented as a nonexistence proof.

## Phase 5.5 — Three statement-shape checks

1. Normal form: sSup plus Finset.sup' is canonical conditional-order API; existential rank and maximum have a verified existing witness equivalence. infDegree/weightedOrder bridges do not identify every arithmetic convention definitionally.
2. Syntactic generality: verified no-hq/no-hB/positive-weight interface, with arbitrary finite sets/functions at the outer level. Keep the maximum form because the actual caller immediately uses Finset.sup'_lt_iff.
3. Superfluous arguments: hq and hB dropped, hrp weakened. Remaining finite/ratio/degree/numerical conditions retained for current parent/substantive arguments; no necessity asserted.

RESTATE-BEFORE-SHIP if the endpoint is proposed upstream; no production rewrite here.

## Phase 6.0 — Complete caller inventory

Scoped rg --no-ignore and tracked git grep find one application, private theta_lt_succ_aux at Theta920. Documentation/header occurrences are not extra applications. No external-to-file source applications occur. Exact canonical293 order/uniqueness/presence/value audit finds sole direct kernel-value consumer _private.Roth.Theta.0.Roth.theta_lt_succ_aux. This is not a transitive/simp/generated/type-consumer closure claim. [Source search](../evidence/Roth.Θ_option_le/source-search.json), [tracked search](../evidence/Roth.Θ_option_le/tracked-source-search.json), [full caller](../evidence/Roth.Θ_option_le/callers.json), [kernel consumers](../evidence/Roth.Θ_option_le/canonical-consumers.json).

The caller transports Fin(n+2) to Option(Fin(n+1)), applies this theorem, unfolds Φ/reindexing, then uses Finset.sup'_lt_iff and theta_phi_lt_aux. A complete fresh caller copy replaces the application with a local proof of the entire original endpoint; that local proof does not use the target. Reopening the replay namespace exposes the original private helpers; the Type-specialized local helper suffices for the actual Fin instance. [Complete inline source](../evidence/Roth.Θ_option_le/inline-executed.lean.txt), [receipt](../evidence/Roth.Θ_option_le/inline-receipt.json).

## Phase 6 — Composition and verification

A strict≤3-existing-mathlib-call proof of the whole endpoint is not verified. The generic outer transport uses two existing calls once the witness is assumed. This target obtains its witness from index_le_lem6, whose determinant, integer factor-height and numerical arguments are substantive project content. Those project/new helpers are not counted as existing library lemmas. Full inlining compiles but does not establish a mathlib duplicate.

Six clean accepted executions: original complete module/canonical audit; arbitrary-B/no-q whole module; joint positive-weight whole module; complete actual caller inline; small-B guards; isolated order/edge cases. Two rejected drafts are separate: the binding-removal draft missed _hq/hB and left caller arguments unsatisfied; a caller appended in a new namespace missed private helpers and had an escaping-universe diagnostic. Recovered sorryAx is excluded from accepted evidence. An unchanged diagnostic query accidentally repeated the first rejected draft after a failed preparation assertion; it adds no accepted evidence. A width-guard rejection happened before native execution. [Ledger](../evidence/Roth.Θ_option_le/verification.json), [portable validator](../evidence/Roth.Θ_option_le/validate.py), [phases](../evidence/Roth.Θ_option_le/phase-evidence.json).

Accepted sources exactly match executed requests/texts, width≤100, no sorry/admit/new axiom/unsafe/native_decide/resource-limit raises. Accepted diagnostics are successful, complete, warning/error-free and standard-axiom-only. The worker made no production, version, Git, overview or progress changes.

## Phase 7 — Verdict and concrete action

BORDERLINE-needs-human: complete assessment. This is a useful named Roth dimension-reduction endpoint with a live caller. Existing order theory covers its short outer layer but not its substantive arithmetic witness. The unresolved upstream issue is the audience/interface for this specialized recursive Θ family, not verification, proof cost, search absence or the ability to form a maximum.

Retain Roth.Θ_option_le in Roth/Theta.lean. Future local edits may apply the three jointly verified interface improvements and the demonstrated sole-caller adjustment. Independently consider reusable determinant, integer factor-height, finite-sum and numerical-witness stages before proposing this recursive endpoint. No upstream-ready PR or inherited YES verdict is claimed.

Future design questions, not review blockers:

1. Full recursive Θ endpoint upstream, or a Roth/Diophantine downstream library?
2. Which determinant/factor-height/numerical ingredients should precede a recursive Θ API?
3. Option's distinguished coordinate, or arbitrary finite family with chosen coordinate and an explicitly verified reindexing bridge?

## Phase 8 — Completion

All required phases, detailed report, verification, literature/search receipts and supporting artifacts are complete; unresolved verification items are empty. Root independently reviews/accepts before integration/commit/push. The current manifest tracks each required report/evidence hash and byte count; future upstream choices are not incomplete assessment work.
