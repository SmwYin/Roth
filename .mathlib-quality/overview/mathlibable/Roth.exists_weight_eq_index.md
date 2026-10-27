# Roth.exists_weight_eq_index — full mathlibable assessment

**NO-mathlib-has-it**, independently re-aimed at the already existing `AddMonoidAlgebra.infDegree`. Its attained-minimum law is `Finset.exists_mem_eq_inf`, applied definitionally to coefficient support. The old real-sInf spelling additionally needs the verified parent representation bridge and Taylor coefficient conversion. Those steps are genuine normalization, and are not advertised as a one-call proof of the old spelling.

## Phase 0 — Baseline and scope

Canonical declaration 136, theorem at `Roth/Index.lean:76`. The entire declaring module and MainLemma caller module were read: [Index](../evidence/Roth.exists_weight_eq_index/Index-source.lean.txt), [MainLemma](../evidence/Roth.exists_weight_eq_index/MainLemma-source.lean.txt). The full baseline build completed successfully with 2467 jobs and exit 0, no reported warnings/errors. [Receipt](../evidence/Roth.exists_weight_eq_index/baseline-build.txt). Its reuse is supported by a fresh [17-source/pin hash check](../evidence/Roth.exists_weight_eq_index/inputs.json), all matching the shared manifest. No production source, pin, Git or progress edit was made by this assessment.

The fresh [original native receipt](../evidence/Roth.exists_weight_eq_index/exists-weight-eq-index-original-audit-receipt.json) is complete, successful, nonpartial, and uses only standard axioms. The [exact original print commands](../evidence/Roth.exists_weight_eq_index/exists-weight-eq-index-original-executed.lean.txt) print the complete short body without a printer elision marker. The [fresh canonical audit source](../evidence/Roth.exists_weight_eq_index/exists-weight-eq-index-audit-executed.lean.txt) checks exactly the tracked 293 names in their proper order, including private names; requested/unique/present/values are all 293. Target info is scoped from native line 1619; audit from 1622. Earlier persistent-document messages are not substituted for fresh target evidence.

## Phase 1 — Mathematical content and full native type

For a nonzero polynomial P, its index at α relative to r is attained by a multi-index d: the evaluated Hasse derivative at d is nonzero and the weight of d equals the index. Translation preserves nonzeroness, so its finite coefficient support is nonempty; every finite nonempty image in a linear order has a minimum. This also works when some r entries are zero under Lean's division convention.

```lean
Roth.exists_weight_eq_index.{u_1} {σ : Type u_1} [Fintype σ]
    {P : MvPolynomial σ ℝ} (hP : P ≠ 0) (α : σ → ℝ) (r : σ → ℕ) :
    ∃ d, (MvPolynomial.eval α) ((MvPolynomial.hasseDeriv d) P) ≠ 0 ∧
      Roth.weight r d = Roth.index P α r
```

σ is the universe-polymorphic variable type, Fintype supplies the current global weight sum, P the real polynomial, α its center, and r the natural denominator data. The sole propositional assumption is hP. The chosen d is a finitely supported natural exponent vector. No positivity, degree bound, nonempty σ, characteristic or domain premise is added. The source applies `Set.Nonempty.csInf_mem` to the finite weight image of Taylor support, then converts support membership with its private `mem_support_taylor_iff`. Direct project dependencies are index, weight, taylor and its nonzero theorem, hasseDeriv, coeff_taylor and that private membership lemma.

## Phase 2 — Preliminary checks

**SMALL**: an elementary attained-minimum helper, with no new structure and not a named main result. Literature search remains exhaustive. One-line-definition test: **n/a**, theorem rather than a data declaration. The source body has four substantive lines, excluding signature.

## Phase 3 — Exhaustive literature

[Metadata 0](../evidence/Roth.exists_weight_eq_index/web0-metadata.json), [1](../evidence/Roth.exists_weight_eq_index/web1-metadata.json), [2](../evidence/Roth.exists_weight_eq_index/web2-metadata.json), [3](../evidence/Roth.exists_weight_eq_index/web3-metadata.json), [primary opens 4](../evidence/Roth.exists_weight_eq_index/web4-metadata.json), [locators/open 5](../evidence/Roth.exists_weight_eq_index/web5-metadata.json) preserve exact requests, response byte counts/SHA256 and returned title/URL locators, without article or search-result bodies. No credential-bearing URL was retained.

| Channel | Actual query/action | Finding and limitation |
|---|---|---|
| General specific | Roth polynomial index attained minimum weighted derivatives | Roth-index presentations; local primary manuscript below gives the exact assertion. |
| General standard | Hasse derivative weighted order nonzero coefficient minimum polynomial | Hasse derivatives as translation coefficients, finite-field multiplicity, and characteristic-independent nonvanishing detection. |
| General abstract | finite nonempty subset linear order infimum attained minimum support degree | Generic finite minimum/infimum; distinguishes linear order from a general lattice. |
| ChatGPT math | n/a: ask_chatgpt_math unavailable | No simulated consultation; remaining channels all performed. |
| Local references | rg index/minimum/attained in clean.tex | §4 lines 530–556 explicitly states an attained minimum. [Exact excerpt](../evidence/Roth.exists_weight_eq_index/clean-excerpt.tex.txt), [search receipt](../evidence/Roth.exists_weight_eq_index/local-literature-search.json). |
| nLab | site:ncatlab.org/nlab Hasse Schmidt derivative order vanishing | Derivation, valuation and related pages. Supplementary meet search identifies finite infimum language. Direct meet page open failed 400, unsupported application/xhtml+xml. |
| nCatLab | site:ncatlab.org/ncatlab polynomial valuation minimum support; site:ncatlab.org/ncatlab finite linear order minimum | Both target the distinct namespace. Returned results are /nlab pages/files; no exact in-namespace hit. This is not absence evidence. |
| Stacks | site:stacks.math.columbia.edu order vanishing polynomial multiplicity Taylor | Algebraic curves/order material; direct Tag 00PD concerns discrete valuations and one-dimensional regular local rings, adjacent rather than this support minimum. |
| MathOverflow | site:mathoverflow.net weighted multiplicity polynomial Hasse derivative minimum; site:mathoverflow.net weighted order vanishing polynomial minimum | Question 288637 concerns minimum degree with prescribed orders on a point set, a different optimization. Direct open yields only the site shell; mathematical content was available in search snippets. |
| Recent arXiv | site:arxiv.org after:2021-10-27 Hasse derivatives weighted multiplicity polynomial; site:arxiv.org after:2021-10-27 Hasse derivative multiplicity polynomial weighted order | 2610.00259, submitted 24 September 2026, concerns derivative/multiplicity loci in characteristic p. Relevant to formulation, not a new attained finite-support minimum. Returned 2103.07239 is outside five years and is not counted as recent. |

The standard concept is **weighted order of vanishing**, **index**, or **minimum support degree**. The local primary manuscript explains that Taylor gives a nonzero derivative and only finitely many can be nonzero, hence the minimum is attained. It uses positive real denominators and infinity for the zero polynomial. The project uses natural denominators, permits zeros, and uses zero for the empty-support index; the present P≠0 premise excludes that empty case. Thus attainment does not require positivity, integer denominator-clearing, additivity of the degree map, or a field.

[Goresky–Klapper, *Algebraic Shift Register Sequences*](https://www.math.ias.edu/~goresky/pdf/algebraic0.pdf), §15.4.1, PDF page 303, distinguishes Hasse derivatives from ordinary derivatives in positive characteristic. This supports retaining Hasse coefficients when generalizing the coefficient ring; it is not a source for reciprocal weighted minima. [Stacks Tag 00PD](https://stacks.math.columbia.edu/tag/00PD) provides the nearby discrete-valuation setting, which has extra multiplicative structure absent from an arbitrary degree-map minimum. [Xie, 2610.00259](https://arxiv.org/abs/2610.00259) studies characteristic-sensitive derivative and multiplicity loci; it is adjacent recent literature, not the library replacement.

## Phase 4a–4b — Generality

| Parameter/hypothesis | Current form | Checked wider form / necessity |
|---|---|---|
| σ and universe | Type u with Fintype | Abstract A : Type u requires no finiteness of ambient variables; finite support suffices. |
| Coefficients | ℝ | Abstract monoid-algebra law compiles over arbitrary Semiring R, independently universe v. |
| α | σ→ℝ | Used only to produce a translated polynomial; disappears after that polynomial is supplied. |
| r / degree map | σ→ℕ reciprocal weight | Arbitrary map D : A→T in abstractLaw; projectedLaw allows arbitrary real degrees, including negative/nonadditive maps. |
| Target order | ℝ with default zero | LinearOrder T and OrderTop T in abstractLaw, universe w independent. A general semilattice is insufficient for attainment by a member: two incomparable elements can have a strict smaller meet. |
| P / hP | nonzero MvPolynomial | Nonempty coefficient support of arbitrary AddMonoidAlgebra element. This is the exact finite-attainment premise. P≠0 cannot simply be removed: P=0 makes every evaluated derivative zero, even though the chosen index default is 0. |
| Nontriviality/domain | no explicit extra premise | No Nontrivial, NoZeroDivisors or field assumption is needed by the abstract support theorem. |
| Positivity, additivity, injectivity | absent | Remain absent; finite linear-order minimization requires none. |

The fixed parent interfaces require Fintype and real coefficients in the unchanged statement. No mechanically droppable hypothesis is claimed for that spelling. In the expanded support representation it is **STRICTLY NARROWER THAN STANDARD**: the wider law has actually compiled. [Isolated exact source](../evidence/Roth.exists_weight_eq_index/exists-weight-eq-index-mathlib-clean-executed.lean.txt), [raw complete success](../evidence/Roth.exists_weight_eq_index/exists-weight-eq-index-mathlib-clean-receipt.json). The generic conclusion is

```lean
∃ d, d ∈ P.coeff.support ∧ AddMonoidAlgebra.infDegree D P = D d
-- Existing proof, hP : P.coeff.support.Nonempty:
Finset.exists_mem_eq_inf _ hP D
```

This is a verified specialization of existing API, not a proposed new theorem or YES-generalise-first gap. The fully abstract form already covers arbitrary variable type and arbitrary coefficient semiring. The projected real version is separately compiled; no claim that old index and infDegree are definitionally equal is made. The isolated file has no Roth import and guards `#check_failure Roth.exists_weight_eq_index`. Its seven-import prefix exactly reuses the parent's preflighted prefix; it uses `Mathlib.Basic.Real.Basic`, with no deprecated forwarding import.

## Phase 4c — All nine modern-idiom checks

| # | Question | Answer and downstream consequence |
|---|---|---|
| 1 | Typeclass preambles | Already LinearOrder/OrderTop/Semiring in the abstract law; no bespoke minimum-attainment class. Existing Finset API specializes automatically. |
| 2 | Filters/topology | No: this is finite support, with no limits or neighborhoods. |
| 3 | Universal property | No new universal object is constructed. Translation already has aeval substitution; existence here is the ordinary finite minimum theorem. |
| 4 | Bundled substructures | No closure predicate. Finset coefficient support is the appropriate finite input and directly composes with inf. |
| 5 | Field→semiring/module | Yes: the accepted abstract law is over Semiring; coefficient-only minimization avoids any real-specific algebra. Hasse/Taylor translation remains separately justified. |
| 6 | Higher categories | No categorical structure or higher coherence is involved. |
| 7 | Concrete index/order | Yes: arbitrary D into a linearly ordered type with top. This reuses support-degree APIs for real, integer and other ordered degree targets. Top records the zero-support case honestly before projection. |
| 8 | Concrete-via-abstract diagnostic | Fires: source proof body contains index zero times, hasseDeriv zero times and taylor only in two support-image lines. Apart from support conversion it is entirely Set.Nonempty.csInf_mem; abstractLaw is existing Finset attainment. |
| 9 | False-generalization guard | Verified parent bridge preserves the original nonzero cases, arbitrary r including zeros, and the actual old value. Reject dropping hP, replacing LinearOrder by arbitrary semilattice, replacing formal polynomials by polynomial functions over finite fields, ordinary derivatives in characteristic p, or applying arbitrary-real finite-support attainment to infinite supports without a well-order/attainment hypothesis. |

Modern idiom available: **yes, already in mathlib**. The useful change is finite support + infDegree, with its generic attained minimum. It eliminates a redundant order API tied to reciprocal denominators. No valuation structure is invented: arbitrary D is not necessarily additive and its infDegree need not be multiplicative.

## Phase 4.5 — Definition infrastructure

All six rows are **n/a — theorem**: typeclass diamond, reducibility leak, noncanonical unfolding, instance priority, universe-polymorphism infrastructure and coercion ambiguity. The declaration introduces only a proof of Prop, no data, instance or coercion. Parent-definition infrastructure is separate from this theorem's assessment.

## Phase 4.6 — Proof strategy

| Question | Assessment |
|---|---|
| ε–δ versus filters | n/a: no topology. |
| Elements versus algebraic inclusions | Witness selection is the intended conclusion; existing Finset attainment is the natural abstract form. No ideal/submodule inclusion is concealed. |
| Sequences versus nets | n/a: no analytic limit. |
| Construction versus universal property | Finite minimum selection is appropriate; no universal-property alternative improves it. |
| Missing helpers mathlib should have | No missing attained-minimum law. Parent real-sInf/infDegree bridge is normalization, and coeff_taylor is separately assessed project API. |

Strategy: **REFACTOR-RECOMMENDED** when migrating the parent to infDegree: use Finset.exists_mem_eq_inf, project its equality and convert the coefficient premise. The existing csInf_mem proof is already idiomatic for its present sInf parent. This recommendation follows API structure; no cost-based verdict is used.

## Phase 5 — Five actual mathlib methods × three forms

[Full formal requests and raw receipts](../evidence/Roth.exists_weight_eq_index/formal-search.json) record Finder, Loogle, LeanSearch and local name search on current, standard weighted-order and abstract support-infimum forms: 12 planned requests plus two current-form retries. Two Loogle requests failed because its remote index does not recognize the project HasseDeriv/old MvPolynomial.coeff identifiers. The suggested quoted-name retry returned cleanly with no hits. The failures remain archived and are not absence evidence. [Current rg](../evidence/Roth.exists_weight_eq_index/rg-current.json), [standard rg](../evidence/Roth.exists_weight_eq_index/rg-literature.json), [abstract rg](../evidence/Roth.exists_weight_eq_index/rg-abstract.json) are the fifth method on pinned sources.

| Method | Current point-index form | Literature weighted-order form | Abstract support-minimum form |
|---|---|---|---|
| Finder | Adjacent weighted homogeneous/support bounds | exists_coeff_ne_zero_and_weightedOrder | infDegree, exists_supDegree_mem_support |
| Loogle | Two identifier errors, quoted hasseDeriv retry clean empty | weightedOrder family, no exact old index | **Finset.exists_mem_eq_inf**, complete matching signature |
| LeanSearch | weightedOrder, weighted homogeneous components | exists_coeff_ne_zero_and_weightedOrder / and_order | infDegree; Finset/Set csInf_mem |
| rg | Target and explicit applications | Pinned weightedOrder attainment at Order:161 | Generated Finset law at Fold:775; infDegree definition Degree:624 |
| local | Production target plus scratch replays | Exact weightedOrder attainment | Empty index-unavailable response; not evidence of absence |

External snapshots can differ from this pin. Every method/form has a successful actual request after the documented Loogle retries; local index unavailable remains a limitation. Positive candidates are pinned by the fresh isolated native check:

- `Finset.exists_mem_eq_inf`: generated by `@[to_dual]` from `exists_mem_eq_sup` at `Mathlib/Data/Finset/Lattice/Fold.lean:775`. Signature: `[LinearOrder T] [OrderTop T] (s : Finset A) (h : s.Nonempty) (D : A→T) : ∃ i ∈ s, s.inf D = D i`.
- `Finset.exists_mem_eq_inf'`: generated dual at Fold:764; nonempty minimum without needing a top on the unlifted order.
- `AddMonoidAlgebra.infDegree`: `Mathlib/Algebra/MonoidAlgebra/Degree.lean:624`, reducible coefficient-support infimum.
- `Finsupp.mem_support_iff`: coefficient nonvanishing/support conversion; `WithTop.untopD_coe` projects a finite value.
- `MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder`, `Mathlib/RingTheory/MvPowerSeries/Order.lean:161`, is the standard natural-weight analogue. It asks finite weighted order; clearing positive integral denominators is unnecessary for the chosen finite-support route and would exclude allowed zero-r cases.

Conclusion: **found in mathlib as Finset.exists_mem_eq_inf, more general form on the parent's existing infDegree representation**, independently verified. Search failures or empty results are not used to prove absence.

## Phase 5.5 — All three statement-shape checks

Normal forms: (i) nonvanishing evaluated Hasse derivative with weight equal to real sInf index; (ii) translated coefficient support member attaining WithTop-valued infDegree; (iii) member attaining a nonempty Finset.inf/inf'. The latter is the existing generic normal form. Parent normalization puts projected infDegree on the RHS; this existential theorem is not an iff normal-form rewrite. No pairwise web of new equivalence lemmas is proposed.

Syntactic generality attempts: abstractLaw uses support membership and infDegree=D d; projectedLaw uses nonzero coefficient and D d=projected infDegree, exactly the old orientation; originalReplacement returns the original Hasse form. All three actually compile. The membership form makes the generic law one existing Finset call; nonvanishing + reversed equality is convenient for all four current consumers. No old-form one-call claim is made.

Superfluous-argument audit: hP is necessary (zero polynomial counterexample); σ, P, α and r all describe the chosen index. Fintype and ℝ are fixed by current parent interfaces; their removal is verified in the abstract representation, not by an unchanged-parent drop. No positive-r, field/domain or nonempty-variable condition should be introduced. Normal form **REFACTOR** to infDegree; syntactic generality **RESTATE** to existing generic attainment; fixed-interface superfluous hypotheses **NONE**. Overall **RESTATE-BEFORE-SHIP** for a hypothetical upstream addition, which would then duplicate existing API.

## Phase 6.0 — Complete caller and inline audit

[Caller inventory and full fragments](../evidence/Roth.exists_weight_eq_index/callers.json), [canonical-inventory rg and git-grep cross-check](../evidence/Roth.exists_weight_eq_index/complete-caller-search.json), [fresh direct consumers](../evidence/Roth.exists_weight_eq_index/direct-consumers.json). There are four explicit callers/four applications, three inside Index, one external-to-file in MainLemma. Internal use count excluding the declaring file **K=1**, one distinct external module. Kernel direct-value consumers are the same four; this is not a claim about opaque/transitive kernel/simp closure. The target is not marked simp and is useful local API, not dead code.

| Caller | Exact reference | Actionable continuation after finite-minimum selection |
|---|---|---|
| Roth.index_eq_zero_iff | Index:101 | Obtain d/hd/hdw from the replacement; retain index=0 rewriting, weight_eq_zero_iff and hasseDeriv_zero_apply. |
| Roth.index_sub_weight_le_index_hasseDeriv | Index:112 | Select an attaining coefficient for hasseDeriv k P using hk; retain derivative-composition nonvanishing and weight_add/subtraction inequality. |
| Roth.index_le_card | Index:226 | Select attaining Taylor exponent; retain coefficient-support conversion, monomial_le_degreeOf and Taylor degree bound, then weight_le_card. |
| Roth.exists_hasseDeriv_eval_ne_zero | MainLemma:457 | Apply the replacement existential's .imp; retain hw ▸ hc to put the selected weight below c and swap conjunction order. |

[Inline audit](../evidence/Roth.exists_weight_eq_index/rg-inline.json) identifies the original csInf_mem proof and Index:147's independently selected MvPowerSeries weightedOrder coefficient in index_eq_weightedOrder_div. The latter is a genuine analogous inline attainment in a different representation, used to prove the power-series bridge; it does not introduce another explicit reference to this target. This supports examining existing generic attainment rather than creating a new minimum API. Multiple useful callers support retaining a local manuscript spelling, but do not establish an upstream gap.

## Phase 6 — Actual composition and representation bridge

The accepted isolated [mathlib source](../evidence/Roth.exists_weight_eq_index/exists-weight-eq-index-mathlib-clean-executed.lean.txt), [raw receipt](../evidence/Roth.exists_weight_eq_index/exists-weight-eq-index-mathlib-clean-receipt.json), proves the analogous infDegree attained-minimum law in exactly **one existing call**:

```lean
Finset.exists_mem_eq_inf _ hP D
```

infDegree is reducible to coefficient-support inf, so no additional algebra proof is needed. projectedLaw then obtains its witness, applies Finsupp.mem_support_iff and projects equality through untopD 0. Its explicit change unfolds infDegree before rw; the initial failure without that delta step is [retained as rejected](../evidence/Roth.exists_weight_eq_index/exists-weight-eq-index-mathlib-initial-receipt.json). Projection/equality normalization is not passed off as the original one-call law.

The accepted parent [mathlib-only bridge source](../evidence/Roth.exists_weight_eq_index/index-expanded-mathlib-executed.lean.txt), [raw complete receipt](../evidence/Roth.exists_weight_eq_index/index-expanded-mathlib-receipt.json), were independently inspected. finsetBridge splits empty/nonempty support, using Finset.coe_inf' and Finset.inf'_eq_csInf_image, with the empty case handled by zero-default projection. denominatorBridge expands reciprocal weights via Finsupp.weight and translation via aeval. These are newly proved normalization bridges, not preexisting mathlib replacement calls. The parent [actual target bridge](../evidence/Roth.exists_weight_eq_index/index-consumers-executed.lean.txt), [native receipt](../evidence/Roth.exists_weight_eq_index/index-consumers-receipt.json), and [fully expanded bridge](../evidence/Roth.exists_weight_eq_index/index-expanded-bridge-executed.lean.txt), [receipt](../evidence/Roth.exists_weight_eq_index/index-expanded-bridge-receipt.json), establish the representation in the actual Roth context, for all P/all r including zero cases.

The fresh [originalReplacement source](../evidence/Roth.exists_weight_eq_index/exists-weight-eq-index-target-executed.lean.txt), [native success](../evidence/Roth.exists_weight_eq_index/exists-weight-eq-index-target-receipt.json), obtains nonempty Taylor support using hP, applies Finset.exists_mem_eq_inf with lifted weight, rewrites membership through coeff_taylor, then rewrites targetBridge and projects the attained equality. It never invokes Roth.exists_weight_eq_index or any downstream index lemma. This old-form proof uses actual rewriting and more than three total normalization/building-block steps; **NOT-COMPOSABLE as a bare ≤3-call old-spelling expression**. Its project Taylor coefficient conversion and finite-minimum bridge are identified explicitly.

The fresh [whole Index and MainLemma consumer experiment](../evidence/Roth.exists_weight_eq_index/exists-weight-eq-index-callers-executed.lean.txt), [complete native receipt](../evidence/Roth.exists_weight_eq_index/exists-weight-eq-index-callers-receipt.json), replays Index with the target replaced by the fresh proof, thus checking all three Index consumer bodies. It also replays the complete MainLemma caller with the fourth use replaced. The original target name occurs nowhere in this accepted replay. All four consumers and the replacement print standard axioms. This verifies the actual caller shapes while leaving production unchanged.

Composition conclusion: **COMPOSABLE/one existing call on the re-aimed representation**; genuine normalization is needed for the old spelling. A closing simp [defs] alone would trigger Phase 6b's BORDERLINE caution. That is not the deciding experiment: Mode B's explicit re-aim rule says an existing analogous law on existing parent D′ yields NO-mathlib-has-it once the law and bridge are independently verified. Both have been verified here.

## Phase 7 — Verdict and actionable plan

**NO-mathlib-has-it** via the explicit parent re-aim rule, not blanket inheritance. The decisive existing law is `Finset.exists_mem_eq_inf` at Fold:775, one line for arbitrary nonempty coefficient-support infDegree as displayed above. Literature confirms the weighted-index spelling is a finite attained minimum; fresh native checks show that the abstract law already exists and specializes correctly after the actual bridge. No cost-based downgrade, failed-search absence claim or normalization-only automatic BORDERLINE is used.

For a refactor, implement the local index using projected infDegree or retain one documented local parent bridge. At all four listed applications, select a witness using Finset.exists_mem_eq_inf on nonempty Taylor support, convert its membership using coeff_taylor, and project/orient its infDegree equality. Then retain each row's subsequent rewriting/arithmetic. Delete exists_weight_eq_index after replacing those four applications if eliminating wrappers. The complete four-consumer replay proves type compatibility of the old-form replacement; direct generic selection supplies the corresponding parent-migration plan. Do not duplicate the finite-sInf bridge at four sites.

Alternative destination: retain this as **project-local convenience API in Roth/Index.lean** to match the manuscript and support its four consumers. Archive or a separate satellite is unnecessary for this elementary specialized spelling. No upstream PR is proposed for the theorem. Separately assessed Hasse/Taylor infrastructure is unaffected by this decision; later index laws still need their own re-aim checks.

## Phase 8 — Handoff

All mandatory phases complete; verification unresolved=[]; root acceptance pending. [Assessment](../evidence/Roth.exists_weight_eq_index/assessment.json), [verification](../evidence/Roth.exists_weight_eq_index/verification.json), [overview entry](../evidence/Roth.exists_weight_eq_index/overview-entry.json), [current manifest](../evidence/Roth.exists_weight_eq_index/copy-manifest.json), [portable read-only validator](../evidence/Roth.exists_weight_eq_index/validate.py). The validator supports scratch/integrated layouts and checks current artifact hashes/bytes, all 17 fresh source/pin hashes, exact canonical order and 293 counters, complete accepted native diagnostics/standard axioms, four callers and cross-searches, all formal methods/literature channels, local links and credential guard. Historical worker manifests do not replace current artifact validation.
