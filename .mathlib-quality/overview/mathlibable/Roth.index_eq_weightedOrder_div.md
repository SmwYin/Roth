# Roth.index_eq_weightedOrder_div

**Verdict: YES-but-generalise-first.** Remove the unnecessary polynomial nonvanishing hypothesis, and propose the underlying polynomial-to-power-series weighted-order comparison against existing `AddMonoidAlgebra.infDegree`. This comparison is new API; the parent index and weight constructions already existing in more general forms does not supply their comparison automatically.

## Phase 0 — baseline and target

The shared successful `lake build` (2467 jobs, no errors/warnings) is reusable: all17 production/pin hashes freshly match [baseline inputs](../evidence/Roth.index_eq_weightedOrder_div/inputs.json), [manifest](../evidence/Roth.index_eq_weightedOrder_div/input-manifest.json), and [build receipt](../evidence/Roth.index_eq_weightedOrder_div/baseline-build.txt). No production or pin change is proposed by this assessment. Canonical143 is a public theorem, Roth/Index.lean:143. The entire declaring module and its sole explicit caller were read. Parent133/index and142/denominator reports were context, not inherited evidence.

[Fresh native original/audit receipt](../evidence/Roth.index_eq_weightedOrder_div/index-weighted-order-original-audit-receipt.json) gives the full elaborated type and standard axioms, complete kernel body without printer elision, and exact293 canonical names/unique/present/values. The direct kernel consumer is independently `Roth.index_mul`; kernel consumers and lexical references are separate notions.

## Phase 1 — statement and mathematics

For a nonzero polynomial P and positive integers rⱼ, let D=∏rⱼ and wⱼ=D/rⱼ. The index of P at α is the natural weighted order of the translated polynomial P(X+α), embedded into multivariate power series, divided by D. Both minima range over exactly the same nonzero coefficients, with reciprocal weights converted into natural weights. The proof takes a coefficient attaining the finite weighted order and establishes the two inequalities using the index lower-bound characterization.

Full native statement:
```lean
∀ {σ : Type u_1} [inst : Fintype σ] {P : MvPolynomial σ ℝ},
  P ≠ 0 → ∀ {r : σ → ℕ}, (∀ j : σ, 0 < r j) → ∀ α : σ → ℝ,
    Roth.index P α r =
      ((MvPowerSeries.weightedOrder (fun j ↦ (∏ i, r i) / r j)
        (MvPolynomial.taylor α P : MvPowerSeries σ ℝ)).toNat : ℝ) / (∏ i, r i)
```

Parameters σ/Fintype specify finitely many reciprocal denominators and their product; P, α and r specify the polynomial, center and weights. hP supplies a finite-order witness in the original proof, and hr supplies denominator clearing. The conclusion itself also holds for P=0 under the project's default-zero conventions. This extension does not preserve the manuscript's infinity-valued zero index unless the projection convention is explicitly retained.

## Phase 2 — preliminary classification

BIG: the module lists this theorem among its main results. One-line definition test and its three exemptions are n/a: this is a theorem. Its proof is a genuine pair of inequalities, not a definitional alias.

## Phase 3 — exhaustive literature

Exact requests, response SHA256/bytes/status, titles and locators are retained in web metadata; full web bodies are not archived. Initial locator extraction had a parser bug; its original request/digest records are preserved and corrected complete locators are in repeat records. [Summary](../evidence/Roth.index_eq_weightedOrder_div/literature-summary.json) distinguishes direct support from adjacent results and failed opens.

| Channel | Actual query/source | Finding |
|---|---|---|
| Specific web | Roth polynomial index weighted order common denominator Taylor expansion | Roth ICM1958 p206, AMS Chapter4 and Milojevic Claim3.1 identify weighted derivative minima; [requests/locators](../evidence/Roth.index_eq_weightedOrder_div/web-specific-repeat.json). |
| General web | weighted order polynomial minimum support monomial valuation rational weights | Monomial valuations and weights, alongside unrelated maximum-degree results; [receipt](../evidence/Roth.index_eq_weightedOrder_div/web-general-repeat.json). |
| Aliases web | weighted initial degree formal power series monomial valuation positive rational weights | Initial forms/weighted degree/formal series; distinguish minimum from maximum; [receipt](../evidence/Roth.index_eq_weightedOrder_div/web-alias-repeat.json). |
| ChatGPT math | Standard form/generality/history | n/a: ask_chatgpt_math unavailable. |
| Local | clean.tex index/weightedOrder/natural weights | §4 lines530–558 explicitly gives this common-denominator comparison and warns about infinite-toNat; [excerpt](../evidence/Roth.index_eq_weightedOrder_div/clean-excerpt.tex.txt), [search](../evidence/Roth.index_eq_weightedOrder_div/local-literature-search.json). |
| nLab | site:ncatlab.org/nlab valuation formal power series weighted order | Valuation page: infinity at zero and general ordered-group target; [receipt](../evidence/Roth.index_eq_weightedOrder_div/web-nlab-repeat.json). |
| nCatLab | site:ncatlab.org/ncatlab weighted order valuation polynomial | Only out-of-namespace nLab/Schreiber results; no exact in-namespace hit; [receipt](../evidence/Roth.index_eq_weightedOrder_div/web-ncatlab-repeat.json). |
| Stacks | site:stacks.math.columbia.edu order formal power series valuation | Opened tag00I8 Section10.50 on valuation rings; adjacent, not this comparison; [receipt](../evidence/Roth.index_eq_weightedOrder_div/web-stacks-repeat.json). |
| MathOverflow | site:mathoverflow.net weighted order polynomial monomial valuation | Q476147 monomial orders via weight vectors; adjacent, not exact polynomial coercion law; [receipt](../evidence/Roth.index_eq_weightedOrder_div/web-mathoverflow-repeat.json). |
| Recent arXiv | site:arxiv.org "monomial valuations" after:2021-10-27 | Bengus-Lasnier–Shkolnikov, *Fibers of phase tropicalizations*, Jan2026/revisedApr2026, abstract discusses monomial valuations and associated graded rings; [receipt](../evidence/Roth.index_eq_weightedOrder_div/web-arxiv-repeat.json). |

[Primary opens](../evidence/Roth.index_eq_weightedOrder_div/web-primary-open.json): ICM PDF exceeds fetch size, AMS returns403, nLab XHTML unsupported; these failures are not hidden. Stacks and the recent arXiv abstract opened successfully. Roth's [1958 address](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf) supplies the historical weighted derivative formulation via returned search excerpt. The [2026 paper](https://arxiv.org/abs/2601.18519) supports the contemporary valuation context, not the exact normalized formula. No mathematical claim rests on unrelated search results.

The standard mathematical core is a minimum of assigned monomial weights over coefficient support. Positive rational weights admit common-denominator scaling; arbitrary positive real weights do not uniformly reduce to natural weights. The usual infinity-at-zero convention differs from the project's real zero value. An all-P comparison is valid here precisely because both sides use the same explicit default-zero projection.

## Phase 4a — parameters and hypotheses

| Parameter/hypothesis | Audit |
|---|---|
| σ : Type* | Already universe polymorphic. Generic polynomial/series comparison works for arbitrary σ without Fintype; verified separately. |
| Fintype σ | Required by unchanged Roth.weight/global product syntax. Removed in expanded support-based comparison, not an unused fixed-interface assumption. |
| P : MvPolynomial σ ℝ | Replace coefficients by arbitrary CommSemiring R in generic comparison; verified. Changing the existing parent signature is a representation rewrite, not a mechanical typeclass drop. |
| hP : P≠0 | Mechanically removable from the exact conclusion: zero branch gives index0=0 and weightedOrder0=⊤ with toNat⊤=0. Independent original proof plus zero case compiled. |
| r : σ→ℕ | Integral denominators implement natural-weight reduction. Arbitrary real weights require finite-support minimum/infDegree instead. |
| hr : ∀j,0<rj | Cannot drop uniformly: mixed-zero Bool denominators leave a nonzero reciprocal coordinate but D=0 destroys the RHS. Positivity is stronger than the local support certificate needed by an expanded denominator bridge, but not simply disposable. |
| α : σ→ℝ | Changes translated support and index. Generic bridge takes any polynomial Q; choose Q=taylor α P. Removing α from the exact point-index formula changes its data. |
| ℝ-valued result | Supports division/order/sInf and default0. Generic order identity is naturally ℕ∞-valued and requires neither ℝ nor division. |

No NoZeroDivisors, Nontrivial, characteristic-zero or positive natural-weight assumptions are needed by the generic coefficient-support comparison. These stronger conditions arise in multiplication or denominator arithmetic, not in identifying the two support minima.

## Phase 4b — verified generality

STRICTLY NARROWER: one exact-interface named weakening, delete hP. [Executed original-proof/zero-case/caller source](../evidence/Roth.index_eq_weightedOrder_div/index-weighted-order-target-executed.lean.txt) and [native receipt](../evidence/Roth.index_eq_weightedOrder_div/index-weighted-order-target-receipt.json) prove `replacement` without hP and replay all three caller uses. Its nonzero branch is independently copied/rechecked from the mathematical proof and never calls the target comparison theorem.

Modern re-aimed upstream statement, already independently compiled mathlib-only:
```lean
theorem weightedOrder_coe {σ : Type u} {R : Type v} [CommSemiring R]
    (P : MvPolynomial σ R) (w : σ → ℕ) :
    (P : MvPowerSeries σ R).weightedOrder w =
      AddMonoidAlgebra.infDegree (fun d ↦ (Finsupp.weight w d : ℕ∞)) P
```
[Exact source](../evidence/Roth.index_eq_weightedOrder_div/index-weighted-order-mathlib-clean-executed.lean.txt), [raw native success](../evidence/Roth.index_eq_weightedOrder_div/index-weighted-order-mathlib-clean-receipt.json). This broader interface is explicitly separate from the mechanical hP deletion. It changes the representation being compared, preserves infinity internally, and specializes to the project theorem after finite projection/scaling and denominator clearing.

The independently proved `scaledInfDegree` compares the real default-zero projected infDegree with weightedOrder.toNat/D for all P, arbitrary σ, CommSemiring coefficients and real D≥0, including D=0. [Executed source](../evidence/Roth.index_eq_weightedOrder_div/index-weighted-order-scale-executed.lean.txt), [receipt](../evidence/Roth.index_eq_weightedOrder_div/index-weighted-order-scale-receipt.json). It includes its own finiteProjection normalization proof. These are new proofs, not existing library replacements. The [modern-to-original specialization](../evidence/Roth.index_eq_weightedOrder_div/index-weighted-order-modern-clean-executed.lean.txt) and [raw success](../evidence/Roth.index_eq_weightedOrder_div/index-weighted-order-modern-clean-receipt.json) then transport the actual Roth.index through its infDegree bridge, identify degree functions using the independently checked denominator bridge, and instantiate scaledInfDegree. This all-P link never calls the old target theorem; all seven positive candidate signatures are printed in that receipt. Cost: cheap exact hP drop; broader API packaging requires import/naming review. Cost does not decide the verdict.

## Phase 4c — all modern-idiom checks

| # | Question | Result and concrete consequence |
|---|---|---|
| 1 | Preambles/typeclasses | Already uses Fintype/CommSemiring appropriately; no new class for a comparison equality. |
| 2 | Sequences/filters | No topology or limits. |
| 3 | Construction/universal property | No new object to characterize; existing polynomial inclusion and infDegree suffice. |
| 4 | Subset/bundled substructure | Support is already a Finset; no closed-substructure predicate to bundle. |
| 5 | Field/module hierarchy | Yes: natural comparison needs only CommSemiring coefficients, enabling semiring and positive-characteristic polynomial embeddings. |
| 6 | Higher categories | No categorical content requiring a higher analogue. |
| 7 | Concrete numerical target | Separate natural ℕ∞ comparison from real scale/projection, retaining infinity until deliberate toNat; arbitrary ordered-target infDegree exists but cannot be called natural weightedOrder unchanged. |
| 8 | Concrete-via-abstract | Fires: after setting F=↑(taylor α P), the original proof uses generic weighted-order attainment/bounds and arithmetic weight identification. Taylor only identifies coefficient support. The generic bridge applies to every polynomial and interfaces with existing infDegree inequalities and weightedOrder_mul. |
| 9 | False-generalization guard | Passed: coefficient identity preserves exactly the same support minimum. Dropping hr uniformly, using negative D with minimum-preserving scaling, replacing minimum by weightedTotalDegree maximum, or calling arbitrary real weights natural weightedOrder are rejected. The zero extension is explicitly a projected-default statement, not infinity-preserving equality in ℝ. |

Modern idiom available: use `weightedOrder_coe` as canonical polynomial/series bridge and keep the reciprocal-denominator corollary local. This gives direct access from polynomial infDegree to weightedOrder multiplication and coefficient bounds, including arbitrary variable types and semiring coefficients; the old Roth-only theorem blocks those inputs. It also prevents every downstream project from reproving attainment and both minimum inequalities.

## Phase 4.5 — infrastructure risk

n/a for all six definition-risk rows (diamonds, reducibility, noncanonical unfolding, instance priority, universe constraints, coercion ambiguity): declaration kind is theorem and introduces no construction/instance/coercion. Proposed comparison is also a theorem; ordinary import-layering review remains in the upstream plan.

## Phase 4.6 — proof strategy

| Row | Audit |
|---|---|
| Topological εδ/filter | n/a, no topology. |
| Algebra element/substructure | Coefficient-support inequalities are appropriate; no ideal inclusion replaces this comparison. |
| Sequences/nets | n/a, no convergence. |
| Construction/universal property | Existing inclusion is used; no universal-property re-construction needed. |
| Missing helper API | Yes: canonical `weightedOrder_coe` tying polynomial infDegree to its series order. Proved with Finset.le_inf_iff, inf_le, weightedOrder_le, le_weightedOrder and coefficient membership. |

REFACTOR-RECOMMENDED: establish the natural comparison once, then finite real projection/scaling, and put Roth's denominator choice in the local specialization. This removes repeated minimum attainment logic from specialized proofs; no claimed missing helper is treated as already existing.

## Phase 5 — actual mathlib methods × three forms

All12 external/local API invocations have unchanged requests/raw receipts as `search-{current,literature,abstract}-{finder,loogle,leansearch,local}.json`. All3 pinned source searches and inline audit have exact argv and complete outputs. External indexes may differ from this pin; local index=unavailable is not absence evidence.

| Method | Current index/denominator | Standard weighted support minimum | Abstract infDegree/series comparison |
|---|---|---|---|
| Finder | Mostly unrelated polynomial estimates | weightedOrder, weightedTotalDegree, monomial/characterization | weightedOrder, weightedTotalDegree maximum; no exact comparison |
| Loogle | weightedOrder+infDegree returns empty | polynomial/weightedOrder partial results | infDegree+ℕ∞ empty |
| LeanSearch | weightedOrder/monomial/coeff bounds | weightedOrder/characterization | order/weightedOrder facts; no coe-infDegree bridge |
| rg pinned | Project spelling absent from mathlib | Existing definitions and bounds | No source cross-reference weightedOrder↔infDegree |
| Local | Project target found, not a library replacement | weightedOrder family | infDegree and withTop comparison; index unavailable |

Pinned candidate sources: [Order](../evidence/Roth.index_eq_weightedOrder_div/Order.lean.txt) weightedOrder definition140, finiteness148, attainment161, bounds171/197, characterization207; [Degree](../evidence/Roth.index_eq_weightedOrder_div/Degree.lean.txt) infDegree624 and withTop comparison632; [Basic](../evidence/Roth.index_eq_weightedOrder_div/Basic.lean.txt) coefficient-preserving polynomial coercion. Existing `weightedTotalDegree` is a maximum and cannot replace this minimum. `infDegree_withTop_some_comp` compares two finite-support target representations, not a polynomial and power series order. Fresh isolated default-limit `fail_if_success exact?` and `fail_if_success (solve | simp [weightedOrder, infDegree])` both pass before the independently proved bridge, showing neither direct discovery nor this definitional simp closes the goal. Sources/receipts are recorded in verification; no previously proved new bridge was available in those isolated contexts.

Conclusion: existing constituent definitions and characterization laws, but no existing analogous comparison hit. This is an actual API gap between two present canonical objects, not novelty inferred merely from a negative web search. The parent re-aim gate was applied independently: infDegree exists; its analogous series comparison must still be proved.

## Phase 5.5 — all statement-shape checks

1. Normal form: natural coefficient-preserving coe comparison with infDegree on RHS; isolate the real default projection and scaling. This gives one canonical bridge, avoiding pairwise lemmas between every reciprocal/series/support spelling.
2. Syntactic generality: take arbitrary polynomial P and assigned natural w, not Taylor expansion at a fixed real center. The project specialization chooses taylor α P and D=∏rⱼ. Exact hP-free point-index form remains convenient for its caller.
3. Superfluous arguments: hP removed by actual compilation. P/w/center/denominators change values; Fintype is a fixed original-parent interface requirement; expanded generic form needs neither Fintype nor α nor ℝ. hr is not silently erased. No unused DecidableEq instance added.

RESTATE-BEFORE-SHIP: submit the canonical generic comparison, retain local arithmetic specialization if useful.

## Phase 6.0 — complete callers and inline audit

[Canonical-inventory lexical enumeration](../evidence/Roth.index_eq_weightedOrder_div/lexical-enumeration.json), [rg --no-ignore and git grep](../evidence/Roth.index_eq_weightedOrder_div/complete-caller-search.json), [caller fragment/plan](../evidence/Roth.index_eq_weightedOrder_div/callers.json), [kernel consumer](../evidence/Roth.index_eq_weightedOrder_div/direct-consumers.json). One distinct caller, three proof-body applications, zero statement applications; documentation mention and declaration excluded.

| Caller/use | Verified plan |
|---|---|
| Roth.index_mul, Index164, P | Rewrite using hP-free replacement P hr α. |
| Roth.index_mul, Index164, Q | Rewrite using hP-free replacement Q hr α. |
| Roth.index_mul, Index165, P*Q | Rewrite using hP-free replacement (P*Q) hr α. Keep hP,hQ for finite ENat.toNat_add; dropping them from index_mul would be false in general under default-zero convention. |

The entire caller was actually rechecked. [Inline audit](../evidence/Roth.index_eq_weightedOrder_div/rg-inline.json) finds no independent duplicate derivation bypassing the theorem; index_mul repeats the same natural weights solely for finiteness/additivity. One user does not make this dead code or automatically make its actual comparison proof trivial.

## Phase 6 — composition and guards

Old-form result is NOT-COMPOSABLE in ≤3 existing calls: denominator clearing, finite weighted-order attainment, two index inequalities, coefficient transport and finite toNat monotonicity are genuine proof work. Parent Roth lemmas are not mathlib primitives. The re-aimed generic comparison uses four distinct order APIs plus coefficient/support normalization, so the displayed proof is not a ≤3-call term either. New `weightedOrder_coe`, `scaledMinimum` and `finiteProjection` are contributions/probes, never counted as preexisting building blocks. A closing simp-only composition would invoke Phase6b BORDERLINE. Fresh isolated [exact? probe](../evidence/Roth.index_eq_weightedOrder_div/index-weighted-order-exact-probe-executed.lean.txt), [exact? receipt](../evidence/Roth.index_eq_weightedOrder_div/index-weighted-order-exact-probe-receipt.json), [simp closure probe](../evidence/Roth.index_eq_weightedOrder_div/index-weighted-order-simp-probe-executed.lean.txt), and [simp receipt](../evidence/Roth.index_eq_weightedOrder_div/index-weighted-order-simp-probe-receipt.json) verify that neither tested route closes this goal; these limited failures are not universal absence proofs.

Zero audit: weightedOrder zero is⊤ (despite an erroneous introductory prose bullet in the library file), toNat⊤=0, real sInf∅=0, and the projected real infDegree also defaults to0. Thus hP-free comparison is correct, although the original proof uses hP to obtain an attaining coefficient. On nonzero P, the proof establishes finiteness before natural projection; ENat.toNat_le_toNat also receives its finite RHS witness. `index_mul` still needs both factors nonzero for toNat addition. Zero natural w are allowed in the generic bridge; order need not detect nonconstant monomials then, but is finite for any nonzero series.

The scaled generic theorem requires only D≥0, includes D=0 and all P, and does not itself justify reciprocal denominator clearing. Negative real scaling reverses min/max in general. The common-denominator product representation separately needs nonzero denominators globally, or a suitable support-local certificate. For mixed-zero r on Bool with r(true)=1, r(false)=0, P=X true and center0, index=1 while D=0 makes the normalized RHS0. The [actual guards](../evidence/Roth.index_eq_weightedOrder_div/index-weighted-order-guards-clean-executed.lean.txt) and [nonpartial native success](../evidence/Roth.index_eq_weightedOrder_div/index-weighted-order-guards-clean-receipt.json) verify both values. This is an actual counterexample to uniformly dropping hr; all-zero/one-variable-zero cases may still happen to agree, so pointwise necessity is not overstated. Empty σ has product1 and only exponent0; P=0 defaults0 consistently.

## Phase 7 — verdict and actionable upstream plan

**YES-but-generalise-first**, reasons MODERN-IDIOM plus verified hP deletion. The real mathematical contribution is the canonical comparison of two existing order constructions across the polynomial inclusion, not a second polynomial index definition. This is independently missing from the checked pinned APIs; the generic proof and scaled finite projection have actually compiled. Parent re-aim therefore yields a new comparison candidate, not inherited NO. The exact hP weakening is mechanical and verified; the broader coefficient/variable/representation change is separately scoped and verified, not falsely described as merely deleting a typeclass.

Propose `MvPowerSeries.weightedOrder_coe` with the precise generic signature in Phase4b. Initial location: **Mathlib/RingTheory/MvPowerSeries/Order.lean**, importing `Mathlib.Algebra.MonoidAlgebra.Degree` after import-fanout review; a dedicated **Mathlib/RingTheory/MvPowerSeries/Polynomial.lean** comparison leaf is an alternative if that layering is undesirable. Do not put the power-series-dependent theorem into foundational MvPolynomial.Eval. Proposed PR title: **feat(RingTheory/MvPowerSeries): compare polynomial weighted order with infDegree**. Include a small finite projection/scaling corollary only if the reviewer wants that interface; keep Roth's r/D/taylor specialization in Roth/Index.lean.

Grouping: the accepted prior YES `Roth.index_sub_weight_le_index_hasseDeriv` has a related coefficient-weight/order audience but a different Hasse derivative bound; coordinate design with it, without claiming it is a dependency or bundling unrelated analytic bounds. Accepted `MvPolynomial.coeff_taylor` and `MvPolynomial.taylor_eq_zero_iff` can support the separate polynomial translation API PR; their acceptance is confirmed from the progress snapshot, not inferred from their names. No earlier accepted YES generic coe-infDegree comparison was found.

Pre-PR checklist:

- Run `/generalise Roth.index_eq_weightedOrder_div` to remove hP from the local corollary and tension the upstream natural comparison against its allP/CommSemiring/arbitraryσ signature.
- Run `/cleanup Roth/Index.lean Roth.index_eq_weightedOrder_div`, and full cleanup on the new mathlib comparison declaration/imports.
- Choose a reviewer from [recent relevant commits](../evidence/Roth.index_eq_weightedOrder_div/recent-commits.json): Justus Springer edited weightedOrder documentation (b7d0290f4e); Violeta Hernández Palacios worked on ENat import refactoring (5658ee5a7c). Ask an appropriate area maintainer to confirm infDegree/series placement.

Alternative local destination: keep the exact denominator/point-index wrapper in Roth/Index.lean for its clear implementation role. No Archive/satellite move is indicated. No production rewrite or upstream PR is performed by this read-only assessment. No unresolved verification remains; root acceptance is pending.

## Phase 8 — evidence package

[Assessment](../evidence/Roth.index_eq_weightedOrder_div/assessment.json), [verification](../evidence/Roth.index_eq_weightedOrder_div/verification.json), [overview entry](../evidence/Roth.index_eq_weightedOrder_div/overview-entry.json), [current copy manifest](../evidence/Roth.index_eq_weightedOrder_div/copy-manifest.json), [portable validator](../evidence/Roth.index_eq_weightedOrder_div/validate.py). All required phases, all named literature channels and all5 mathlib methods on all3 forms are complete. Accepted native evidence is complete and has only standard axioms; unsuccessful preparation/execution is separated. The validator checks current manifests, exact293 names/order, original inputs, caller evidence, native diagnostics, portable links and credential safety.
