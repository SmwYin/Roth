# Roth.sum_max_sub_le_index_det — full mathlibable assessment

**Verdict: BORDERLINE-needs-human.** The determinant transport layer is reusable and independently proved generically. The original Hasse/index formula is specialized to Roth's argument. The remaining decision is which upstream order/valuation interface should carry that layer and whether the Hasse corollary should remain downstream. This is a completed read-only assessment with no verification blockers; the three design questions below do not require a user response to finish this assessment.

## Phase 0 — Doctor

Canonical declaration207 is the public theorem at Roth/Theta.lean:376. The entire985-line [Theta module](../evidence/Roth.sum_max_sub_le_index_det/source-Theta.lean.txt), entire [Index parent](../evidence/Roth.sum_max_sub_le_index_det/source-Index.lean.txt), actual entry inequality, determinant expansion, product nonvanishing and sole caller were read. The module develops the supremum Θ and Lemmas5–7 used in Roth's theorem. The [baseline build](../evidence/Roth.sum_max_sub_le_index_det/baseline-build.txt) completed2467jobs with exit0 and no reported warnings/errors. Its reuse is supported by a fresh match of all17source/pin hashes: [manifest](../evidence/Roth.sum_max_sub_le_index_det/input-manifest.json), [fresh hashes](../evidence/Roth.sum_max_sub_le_index_det/source-hashes.json). No new project build or production edit is claimed.

The [original native source](../evidence/Roth.sum_max_sub_le_index_det/det207-original-executed.lean.txt) and [complete receipt](../evidence/Roth.sum_max_sub_le_index_det/det207-original-receipt.json) resolve the target, print its body/type and verify standard axioms. The exact293-name array, including private modules/order, passed the pre-execution checker and runtime presence/value checks. There is one direct kernel-value consumer and no direct type consumer. This is distinct from source enumeration and from transitive dependency or simp closure.

## Phase 1 — Comprehend

Let R be a real polynomial in variables τ plus a distinguished variable xₚ. Let the l×l matrix entry in rowμ,columnν be the Hasse derivative with τ-multi-index Dμ and distinguished-variable derivative orderν. When the determinant is nonzero, its weighted index at any point is at least the sum overν<l of max(0,index(R)−ν/rₚ), minus lδ, provided the τ-derivative weights are controlled byδ.

The proof first establishes the entry estimate for nonzero entries. The derivative-index inequality bounds the total loss by weight(Dμ)+ν/rₚ. Since index is nonnegative and weight(Dμ)≤δ, the loss can be moved outside the positive part. Expand the determinant over permutations. For each nonzero signed product, every entry is nonzero; multiplication by its sign preserves index. Positive r permits the existing project product law, so summing the entry estimates proves the common lower bound for each nonzero summand, and the project sum law transfers it to the nonzero determinant.

Full native type (preserved without field elision in [native-type.json](../evidence/Roth.sum_max_sub_le_index_det/native-type.json)):

```lean
∀ {τ : Type u_2} [inst : Fintype τ] {R : MvPolynomial (Option τ) ℝ} {l : ℕ} (D : Fin l → τ →₀ ℕ),
  (∀ (μ : Fin l), Finsupp.degree (D μ) ≤ ↑μ) →
    (Matrix.of fun (μ ν : Fin l) ↦ (hasseDeriv (Finsupp.mapDomain some (D μ) + Finsupp.single none ↑ν)) R).det ≠ 0 →
      ∀ (α : Option τ → ℝ) {r : Option τ → ℕ},
        (∀ (j : Option τ), 0 < r j) →
          ∀ {δ : ℝ},
            (∀ (d : τ →₀ ℕ), Finsupp.degree d ≤ l - 1 → Roth.weight (r ∘ some) d ≤ δ) →
              ∑ ν ∈ Finset.range l, max 0 (Roth.index R α r - ↑ν / ↑(r none)) - ↑l * δ ≤
                Roth.index
                  (Matrix.of fun (μ ν : Fin l) ↦
                      (hasseDeriv (Finsupp.mapDomain some (D μ) + Finsupp.single none ↑ν)) R).det
                  α r
```

Parameters: arbitrary-universe τ indexes nondistinguished variables; Fintype supplies the current weight/index interfaces; R and α specify the polynomial and point; l sizes the determinant; D specifies row derivatives; r gives natural denominators; δ bounds the row losses. Hypotheses are hD, hdet, hr and hδ. Neither l>0 nor an additional δ≥0 premise is assumed. The original hδ already implies0≤δ by taking d=0, including l=0.

## Phase 2 — Preliminary checks

SMALL: this is a technical lower estimate inside Lemma6, not a named main result or a new structure. One-line definition check is n/a because the declaration is a theorem. Its substantive proof has an entry-estimate stage and a determinant-transport stage; its length is not a verdict factor.

## Phase 3 — Exhaustive literature protocol

Exact requests, returned response SHA256/bytes, titles/URLs/locators and original concise summaries are retained, without full result/article bodies: [three general queries](../evidence/Roth.sum_max_sub_le_index_det/web-0.json), [nLab/nCatLab/Stacks](../evidence/Roth.sum_max_sub_le_index_det/web-1.json), [MO/recent arXiv](../evidence/Roth.sum_max_sub_le_index_det/web-2.json), [primary retrievals](../evidence/Roth.sum_max_sub_le_index_det/web-3.json). URL query parameters were removed from returned locator lists; exact requests remain. Search timestamps are not treated as publication dates.

| Channel | Actual query / primary locator | Finding |
|---|---|---|
| General web, specific | `Roth theorem index determinant derivatives sum max index lower bound` | UCL's Math249A transcription notes, p63, show the same positive-part determinant lower estimate in Roth's lemma. Indexed excerpt inspected; direct URL fetch returned404, honestly retained. [Primary locator](https://www.ucl.ac.uk/~ucahpet/TransNotes.pdf). |
| General web, general | `valuation determinant lower bound row column valuations tropical determinant` | Valuations and tropical determinants suggest the generic permutation-sum organization. This is mathematical synthesis, not a claim that a returned reference states our exact Lean schema. |
| General web, alias | `generalized Wronskian order of vanishing determinant Hasse derivatives` | [Towse, Generalized Wronskians and Weierstrass weights](https://msp.org/pjm/2000/193-2/pjm-v193-n2-p12-p.pdf), Proposition1, concerns derivatives of generalized Wronskians; adjacent determinant calculus rather than an exact weighted-index bound. |
| ChatGPT math MCP | Standard form, generality and historical evolution | n/a: ask_chatgpt_math unavailable. No answer fabricated. |
| Local clean.tex | [search](../evidence/Roth.sum_max_sub_le_index_det/local-literature-search.json), [source metadata](../evidence/Roth.sum_max_sub_le_index_det/local-literature.json), [§5 excerpt](../evidence/Roth.sum_max_sub_le_index_det/clean-lemma6-excerpt.tex.txt), lines789–840 | Gives the entry positive-part inequality, permutation products and exactly the displayed lower bound. This is the precise source for the target. |
| nLab | `site:ncatlab.org/nlab valuation determinant order vanishing` | [valuation](https://ncatlab.org/nlab/show/valuation), Definition, gives the additive valuation laws with zero value∞; [determinant](https://ncatlab.org/nlab/show/determinant) gives the permutation expansion. Adjacent structural context. |
| nCatLab | `site:ncatlab.org/ncatlab valuation determinant` | Actual namespace-specific query returned nLab/off-namespace material. No exact in-namespace formulation found; this is not an absence proof. |
| Stacks | `site:stacks.math.columbia.edu determinant valuation order vanishing` | [02MB](https://stacks.math.columbia.edu/tag/02MB), Definition10.121.2 and Lemma10.121.7, defines vanishing order by length and relates determinant order to lattice distance. Direct page inspected; it does not replace the multivariate Hasse/index estimate. |
| MathOverflow | `site:mathoverflow.net valuation determinant lower bound` | Results on determinant valuations/cancellations were adjacent, not the exact lower estimate. No mathematical proof or exact generality conclusion is borrowed from them. |
| Recent arXiv | `site:arxiv.org Wronskian order vanishing Hasse derivatives after:2021-10-28 before:2026-10-29` | [Kiselev2511.03848](https://arxiv.org/abs/2511.03848), abstract lines8–17, submitted2025-11-05, concerns Jacobi identities of multidimensional generalized Wronskians. It is inside the five-year window but does not supply the target bound. Other Hasse-invariant hits concern a different object and were rejected. |

The exact formula is classical bookkeeping in Roth's argument. Its matrix core is the elementary valuation principle: a lower bound shared by all permutation products bounds a determinant. The manuscript's ∞ at zero differs from this project's index0=0; that difference is substantive. No reference establishes that the real-valued supplied-law schema below is the unique or maximally general upstream API.

## Phase 4a — Parameter and hypothesis audit

| Parameter/hypothesis | Use and verified status |
|---|---|
| τ : Type u | Already arbitrary universe. Generic matrix layer has arbitrary finite index type n, independently of variable type. |
| Fintype τ | Used by current Roth.weight/index. Not removed from their unchanged interfaces. Finite-support degree is a possible expanded representation; no arbitrary-variable Hasse transport is claimed here. |
| ℝ coefficients and α | Fixed parent signatures. Abstract determinant layer works over any commutative domain A with v:A→ℝ satisfying the supplied laws, verified in isolation. This does not prove arbitrary-coefficient Hasse/index laws. |
| R,α | Genuine input/center of entry estimate. After hterm, the matrix proof no longer needs their special properties. |
| l : ℕ, Fin l | Consecutive ν is genuine to the Hasse column loss. The matrix transport itself uses arbitrary finite n. l=0 is already allowed and determinant1 is handled. |
| D | Actual row derivatives remain data. Generic matrix transport does not need Hasse form. |
| hD : degree(Dμ)≤μ | Used only to invoke globalhδ at Dμ. Jointly replace hD/globalhδ by per-row weights≤δ; the weakening compiles. Simply dropping hD while keeping only the old ball-bound is not claimed. |
| hδ : every degree≤l−1 d has weight≤δ | Stronger than required. New weak theorem asks only ∀μ,weight(Dμ)≤δ. The old result specializes by hδ(Dμ)((hDμ).trans(Nat.le_sub_one_of_lt μ.isLt)). |
| hdet≠0 | Needed for the real zero-default index. A compiled actual Hasse-shaped counterexample disproves deletion, below. |
| r : Optionτ→ℕ and hr>0 | Natural denominators are parent-interface constraints; positivity is required by the invoked project index_prod bridge. No necessity or maximality claim is made: handling zero weights via another support-degree representation is a separate proof. |
| δ : ℝ | Already arbitrary real in signature; nonnegativity follows from hδ. No new δ>0 requirement is justified. |

## Phase 4b — Compiled weakening and actual consumers

The [mathlib-only proof](../evidence/Roth.sum_max_sub_le_index_det/det207-isolated-executed.lean.txt) proves a new `Det207.lowerDet`: for any commutative domain A, real-valued v with supplied finite nonzero-sum lower-bound law, additive finite-product law and integer-unit invariance, if col(j)−row(i)≤v(Mij) for each nonzero entry and detM≠0, then Σcol−Σrow≤v(detM). It handles arbitrary finite n and row-specific losses. This is a newly proved schema, not an existing mathlib theorem or a bundled valuation instance. [Raw native success](../evidence/Roth.sum_max_sub_le_index_det/det207-isolated-receipt.json).

In the [complete native replay](../evidence/Roth.sum_max_sub_le_index_det/det207-fullmodule-executed.lean.txt), `Det207Project.indexDet` instantiates it using project le_index_sum/index_prod/index_C_mul. `Det207Project.weak` proves the original conclusion under only the per-row weight bound. The original signature is recovered by the explicit bridge above; all985lines of Theta are replayed in a separate namespace. The exact sole caller `index_le_lem6` compiles against that restored signature. A second complete `directWeakCaller` invokes the weakened theorem directly, deriving its row weights from the caller's hD/weight_le_delta_aux. The replay also checks Θ_lt's axioms. [Complete clean receipt](../evidence/Roth.sum_max_sub_le_index_det/det207-fullmodule-receipt.json).

The independently verified [ordered additive group variant](../evidence/Roth.sum_max_sub_le_index_det/det207-group-executed.lean.txt), [raw success](../evidence/Roth.sum_max_sub_le_index_det/det207-group-receipt.json), replaces ℝ by Γ with AddCommGroup, PartialOrder and IsOrderedAddMonoid. The same row/column proof works; no linear order, completeness or real division is used in this layer. IsDomain is a sufficient coefficient hypothesis here, not claimed necessary or minimal.

The abstract matrix guard uses all entries X in a2×2 matrix: each entry has index1, while its zero determinant has index0, so a lower bound2 fails. Separately, the **actual target guard** uses τ=Empty,R=X none,l=2,Dμ=0,α=0,r=1,δ=0. hD and the full originalhδ hold, both Hasse matrix rows agree, det=0, and the claimed lower bound is1 while index(det)=0. `actualNonzeroGuard` proves this negation. Thus the abstract guard is not being misrepresented as Hasse-shaped evidence. All guards have standard axioms and no warnings. An ∞-valued formulation could permit zero determinants, but that changes codomain/convention and is not an unconditional theorem about the current ℝ-valued index.

## Phase 4c — All nine modern-idiom checks

| # | Question | Assessment / concrete consequence |
|---|---|---|
| 1 | Typeclass abstraction | Existing ring/domain classes suffice for matrix algebra. Supplied laws establish a diagnostic schema; selecting an existing bundled valuation/degree interface is an upstream design question, not an excuse to invent an Index class. |
| 2 | Filters/nets | No convergence argument; none needed. |
| 3 | Universal properties | det's alternating universal property does not by itself express order inequalities. The permutation expansion directly exposes the needed products. |
| 4 | Bundled substructures | Filtration ideals could encode vanishing bounds, but no filtration-ideal refactor is claimed compiled. No ad hoc closed subset in current theorem. |
| 5 | Field-specific hierarchy | Matrix layer generalizes to commutative domain A. The compiled Hasse layer retains fixed real parents; arbitrary coefficients are not silently inferred. |
| 6 | Higher categories | No higher-categorical data or benefit here. |
| 7 | Concrete indices/ordered targets | Generic layer replaces Fin l by arbitrary finite n and constantδ by row losses. This supports other derivative matrices without repeating permutation transport. A separately compiled schema also uses Γ with [AddCommGroup Γ], [PartialOrder Γ], [IsOrderedAddMonoid Γ]; a top-valued bundled interface remains design work. |
| 8 | Concrete-via-abstract diagnostic | [Body audit](../evidence/Roth.sum_max_sub_le_index_det/proof-body-audit.json): after hterm, R/Hasse-specific reasoning disappears. The remaining E matrix uses only sum/product/sign index laws. Diagnostic fires, and the isolated lowerDet plus actual indexDet instantiation confirms the abstraction. The earlier entry bound still genuinely uses Hasse derivatives and weights. |
| 9 | False-generalization guard | Preserve zero convention/nonvanishing. The compiled Hasse counterexample rejects dropping hdet. A bundle with v(0)=∞ cannot be identified with index at0. Arbitrary real weights may be negative and would not preserve index_nonneg; no such strengthening is claimed. |

Modernization is available for the determinant layer. The downstream gain is a reusable matrix-order bound with row-specific losses; the remaining question is its library-facing interface. No cost or presumed proof difficulty drives the verdict.

## Phase 4.5 — Infrastructure risk

All six rows are theorem-kind n/a: no new definition, class, instance or coercion is proposed as accepted production code.

| Risk | Status / reason |
|---|---|
| Typeclass diamond | n/a: theorem registers no instance path. |
| Reducibility leak | n/a: theorem introduces no definitional implementation boundary. |
| Noncanonical unfolding | n/a: proof transport, no new reducible data. |
| Instance priority | n/a: no instance or priority. |
| Universe issues | n/a as definition risk; generic proof uses common universeu for matrix and finite laws. The first rejected attempt's independent-universe error is retained. |
| Coercion ambiguity | n/a: no CoeFun/CoeSort is introduced; ordinary casts are checked by native proofs. |

## Phase 4.6 — All five proof-strategy checks

| # | Strategy question | Assessment |
|---|---|---|
| 1 | ε–δ versus filters | No topology. |
| 2 | Elements versus bundled algebra | Finite entry inequalities/permutation sums are appropriate. An order/valuation determinant API isolates this from the Hasse application, as compiled. |
| 3 | Sequences versus nets | No limiting operation. |
| 4 | Construction versus universal property | No constructed object needing a different universal property. |
| 5 | Missing helpers mathlib should have | Generic determinant lower transport against an established order/valuation/infDegree interface is the concrete API candidate. New lowerDet proves the mathematical content but its supplied-law signature is not automatically the preferred upstream form. |

**REFACTOR-RECOMMENDED** for an upstream proposal: separate Hasse entry control from determinant transport, use established support-degree/valuation infrastructure and preserve the point-index specialization locally if needed. This is a mathematical API recommendation, not a performance or cost judgment.

## Phase 5 — All five search methods and parent re-aim

All15cells were actually executed on current, literature-standard and abstract weightedOrder forms. Four additional service queries plus pinned rg re-aim the result at the parent index's existing `AddMonoidAlgebra.infDegree` representation. Exact requests and complete raw responses are retained as search0–11 and reaim0–3; selected links: [Finder current](../evidence/Roth.sum_max_sub_le_index_det/search-0.json), [Loogle standard](../evidence/Roth.sum_max_sub_le_index_det/search-5.json), [LeanSearch abstract](../evidence/Roth.sum_max_sub_le_index_det/search-10.json), [local abstract](../evidence/Roth.sum_max_sub_le_index_det/search-11.json), [infDegree re-aim](../evidence/Roth.sum_max_sub_le_index_det/reaim-1.json).

| Method | Current Hasse determinant | Standard valuation determinant | Abstract weighted order / parent re-aim |
|---|---|---|---|
| Finder | Univariate Hasse degree/Chevalley bounds, not this law | Adjacent matrix/order results | weightedOrder primitives; re-aim returned determinant degree/absolute-value upper bounds |
| Loogle | determinant reindex hits, no target estimate | Matrix determinant inequalities | weightedOrder finite/top laws; infDegree add/mul inequalities |
| LeanSearch | weightedOrder/order-lowering primitives | valuation/order-related candidates, no exact target located | det_le, weightedOrder products; re-aim finds support finite-product inequality |
| rg | [current](../evidence/Roth.sum_max_sub_le_index_det/rg-current.json) | [standard](../evidence/Roth.sum_max_sub_le_index_det/rg-standard.json) | [abstract](../evidence/Roth.sum_max_sub_le_index_det/rg-abstract.json), [infDegree](../evidence/Roth.sum_max_sub_le_index_det/rg-reaim.json) |
| local | Finds project target | Name lookup, no exact candidate | Finds weightedOrder/infDegree families. Index reports warming/error, so missing hits do not establish absence. |

The independent [full-name search](../evidence/Roth.sum_max_sub_le_index_det/rg-full-name.json) found no mathlib target spelling. This and searches do not prove global absence. Remote indexes may differ from the pin. [Pinned sources/hashes](../evidence/Roth.sum_max_sub_le_index_det/mathlib-inputs.json) and [native positive signatures](../evidence/Roth.sum_max_sub_le_index_det/det207-positive-receipt.json) establish usable APIs: Matrix.det_apply′, Equiv.sum_comp, weightedOrder product/add/neg laws, infDegree add/mul and `AddMonoidAlgebra.le_inf_support_coeff_finsetProd`. A remote old spelling `le_inf_support_finset_prod` produced a deprecation warning; that source/receipt is retained separately, and the accepted source uses the current name.

`Matrix.det_le` in Matrix/AbsoluteValue is an upper bound with factorial and ordinary absolute value. It has the wrong direction and mathematical object; no identification with the additive order estimate is claimed. infDegree has useful sum/product laws, but no complete determinant-and-Hasse lower estimate was found. Parent index was assessed NO because infDegree supplies its construction; that does not imply an analogous determinant law is already present. The re-aim gate would force NO if such a law were verified. Here no hit/representation bridge gives the whole target in≤3existing calls, and the newly proved schema is not counted as existing mathlib.

## Phase 5.5 — Three statement-shape checks

Normal form: the source's scalar bound Σmax−lδ≤index(det) is convenient for the next arithmetic step. Equivalent rearrangement puts lδ on the right; the generic matrix normal form is Σcol−Σrow≤v(det). Existing infDegree/weightedOrder use top for zero, unlike the real projection. No existing complete canonical determinant law was located, and no pairwise equivalence API is invented.

Syntactic generality: the compiled per-row premise is easier to apply when one has only the chosen Dμ weights. Its original specialization uses a one-line degree-to-weight bridge; the full caller with original input data passes. Row-specific losses belong in matrix transport, while ν<l stays in the Hasse application.

Superfluous assumptions: hD/globalhδ can be jointly replaced by row weights, not merely erased. DecidableEqτ is already omitted in the original full native type; classical reasoning supplies local decisions. Fintypeτ/ℝ are fixed parent constraints. hr is used through index_prod, with no claim it is logically necessary in every expanded representation. hdet is essential under current zero convention, mechanically refuted without it. R,α,D,r,l andδ all supply real data or bounds. **RESTATE-BEFORE-SHIP** if an upstream theorem is proposed; retain the original locally pending design choice.

## Phase 6.0 — Every caller and inline audit

Fresh [ignore-independent search](../evidence/Roth.sum_max_sub_le_index_det/callers.json), [tracked production search](../evidence/Roth.sum_max_sub_le_index_det/tracked-callers.json), [canonical inventory search](../evidence/Roth.sum_max_sub_le_index_det/inventory-callers.json) and [comment-stripped lexical enumeration](../evidence/Roth.sum_max_sub_le_index_det/lexical-enumeration.json) agree: declaration line376 and one call line576, both in Theta. K=0 outside the declaring file; one internal caller is `Roth.index_le_lem6`.

| Caller | Use / concrete future refactor |
|---|---|
| Roth.index_le_lem6, Theta:576 | Uses hD and degree-ball weight bound from weight_le_delta_aux to obtain hlower; combines it with index_det_le and min_le_sum_max. Keep current call locally, or call weak with `(fun μ ↦ weight_le_delta_aux … (((hD μ).trans …).trans …))`; the entire directWeakCaller proof already compiles. |

[Inline search](../evidence/Roth.sum_max_sub_le_index_det/inline-search.json), [audit](../evidence/Roth.sum_max_sub_le_index_det/inline-audit.json), [full caller source](../evidence/Roth.sum_max_sub_le_index_det/inline-index_le_lem6.lean.txt) show no second full lower estimate rederived inline. Parent sum/product laws and the opposite determinant upper bound are related, not duplicate target proofs. The target is not simp-tagged and is live. Exact293kernel audit finds the same sole direct value consumer, no type consumer; this does not claim complete opaque/transitive/simp closure.

## Phase 6 — Composition experiments

With hsum/hprod/hunit supplied as explicit hypotheses, and before any new determinant helper is available, the isolated lowerDet proof executes three concrete existing-route probes: `fail_if_success solve | exact?`, `simp`, and `positivity`. All fail to close; native compilation then proves the result explicitly by Matrix.det_apply′, nonzero-entry extraction, sign invariance, product additivity, permutation reindexing and sum monotonicity. These are bounded experiments on the abstract supplied-law goal, not closure tests for the complete old Hasse/index statement and not a theorem of absence. No heartbeats/recursion limits were raised.

For the old Hasse formula, project index_sub_weight_le_index_hasseDeriv, le_index_sum, index_prod and index_C_mul are essential inputs in the actual proof and **are not existing mathlib building blocks**. Nor is the new lowerDet helper counted as an existing call. The original becomes short only after these project/new layers and its weight bridge are supplied. No verified strict≤3existing-mathlib-call term is available for the complete target, so neither NO-composable nor NO-mathlib-has-it is justified by these experiments. No `simp [defs…]` closure is being promoted to a strict-call NO verdict.

Accepted exact sources, complete native receipts and rejection reasons are indexed by [verification.json](../evidence/Roth.sum_max_sub_le_index_det/verification.json). Rejected attempts cover the initial universe mismatch, finite-sum/caller-context errors, unused-instance/simp warnings, deprecated name and actual-guard normalization; recovered sorryAx in those failures is never accepted evidence. Clean historical executions are retained separately and superseded by final clean sources.

## Phase 7 — Actionable verdict and design questions

**BORDERLINE-needs-human**, with all phases complete. A mechanically verified per-row weakening exists, and generic determinant transport is real reusable mathematics. Nevertheless, the appropriate upstream object remains a judgment about valuation/support-degree API and the location of this Roth-specific Hasse specialization. The evidence does not yet justify naming the supplied-law diagnostic schema as a stable library API, and does not show an existing replacement. This is not a cost-based downgrade or a verification deferral.

1. Should the generic determinant-order bound be stated against an existing bundled valuation, or directly against infDegree/support-degree inequalities with top?
2. Should a real zero-default corollary with nonzero determinant be exposed upstream, or should the library keep∞at zero and leave this projection downstream?
3. After generic determinant transport and Hasse entry-order laws exist, should the exact consecutive-column Roth formula remain local to Theta rather than become another public mathlib specialization?

Concrete current destination: retain Roth/Theta.lean. A future matrix API could live in a new `Mathlib/LinearAlgebra/Matrix/Valuation.lean` or, if support-degree specific, a separate determinant/monoid-algebra integration file; import layering is provisional. Existing Degree should not import the matrix stack solely for this application. No YES PR title/reviewer grouping is required for a BORDERLINE assessment. No future declaration is being assessed here.

## Phase 8 — Verification and handoff

Five accepted executions cover original target/audit, isolated generic proof with three probes, pinned positive signatures ordered additive group schema, and full-module/caller/weakening/guard replay. Every accepted receipt has success, complete nonpartial diagnostics where supported, no errors/warnings/sorry, and standard axioms only. Sources use the exact18-import isolated prefix and unchanged nine-import disk header. Arrays preserve all293names in exact canonical order. Source/pin/module hashes, report links, exact native sources/requests/receipts and every supporting artifact are checked by the portable validator and current copy manifest.

The package is read-only with respect to production/Git and awaits root's independent acceptance. [Assessment metadata](../evidence/Roth.sum_max_sub_le_index_det/assessment.json), [phase evidence](../evidence/Roth.sum_max_sub_le_index_det/phase-evidence.json), [portable validator](../evidence/Roth.sum_max_sub_le_index_det/validate.py) and [completion record](../evidence/Roth.sum_max_sub_le_index_det/completion.json) record that boundary.
