# Roth.normOne_monomial — NO-mathlib-has-it

Existing `MvPolynomial.sum_monomial_eq` is precisely the singleton coefficient-sum identity at greater generality. Its parent `Finsupp.sum_single_index` removes all polynomial structure. The old interface is a direct specialization with an explicit proof that the coefficient-size function sends zero to zero. Four fresh native evidence sets establish the representation, original proof replay, broader forms, necessary premise and all three complete consumer proof bodies. No production changes or upstream PR are proposed.

## Phase 0 — Baseline

Baseline `lake build` succeeded, 2467 jobs, no reported warnings/errors. All 17 source/pin hashes freshly match the shared baseline manifest, independently checked in this package. Declaration79 of293 resolves at `Roth/CoeffNorm.lean:59–62`, public theorem, no sorry. Full declaring module read; its coefficient estimates serve determinants, Hasse derivatives and Roth's main lemma. [Baseline](../evidence/Roth.normOne_monomial/baseline-build.txt), [fresh inputs](../evidence/Roth.normOne_monomial/inputs.json), [module](../evidence/Roth.normOne_monomial/source-module.lean.txt), [canonical order](../evidence/Roth.normOne_monomial/canonical-order.json).

## Phase 1 — Content and proof

For any monomial with integer coefficient c and exponent vector e, the sum of the absolute real values of its coefficients is |c|. If c is zero, its support is empty and both sides are zero. Otherwise its only coefficient is c at e. The published proof pads the support to the singleton {e}, then simplifies the singleton sum and monomial coefficient formula.

Full native Lean type, with readable cast notation:

```lean
∀ {σ : Type u_1} (e : σ →₀ ℕ) (c : ℤ),
  Roth.normOne (MvPolynomial.monomial e c) = |(c : ℝ)|
```

The variable type σ has arbitrary universe and can be infinite or empty. e is any finite exponent vector; c is any integer. No further hypotheses. `normOne` is the only project definition in the statement; `normOne_eq_sum_of_support_subset` is an original-proof dependency, eliminated in the direct replacement. [Full native type/print/replay](../evidence/Roth.normOne_monomial/native-specific-success.json).

## Phase 2 — Preliminary checks

**SMALL**: helper singleton identity, neither new structure nor named theorem nor listed main result. Exhaustive literature protocol still runs. One-line definition test and its three exemptions: n/a, kind is theorem. Infrastructure is assessed separately below.

## Phase 3 — Exhaustive literature protocol

Exact requests, response hashes/UTF8 bytes, title/URL locators and concise original summaries are archived; no full article/search bodies. Returned URL queries are removed from archived locators. Searches ran against the real channels, not inferred from earlier declarations.

| Channel | Actual query/access | Result and limit |
|---|---|---|
| General web, specific | polynomial coefficient l1 norm monomial absolute value coefficient | Coefficient-vector ℓ¹ norm framework; singleton identity follows immediately. |
| General web, general | finitely supported function sum single support zero preserving function | Rice Semmes notes and IsarMathLib finite support models. |
| General web, alias | polynomial length sum absolute values coefficients monomial norm | Length is an alias; distinguish height/sup norm and value norms. |
| ChatGPT math MCP | unavailable tool | n/a: ask_chatgpt_math unavailable; no replacement channel invented. |
| Local clean.tex | actual monomial/norm/padding search; lines437–497 read | §3 Lemma3 proof introduces coefficient ℓ¹ sum and monomial expansion; singleton law is elementary input, not separately named result. |
| nLab | site:ncatlab.org/nlab free module finitely supported function basis sum | Module/basis background on formal finite sums. Direct basis-page open failed400 unsupported application/xhtml+xml; no claim of full retrieval. |
| nCatLab | site:ncatlab.org/ncatlab finitely supported functions monoid algebra | Returned nLab background; no relevant nCatLab-specific singleton law. No categorical generalization required. |
| Stacks | site:stacks.math.columbia.edu polynomial monomial coefficients basis | Broad polynomial background results. Direct00SK open is syntomic morphisms, a false-positive hit; no coefficient-norm theorem credited. |
| MathOverflow | site:mathoverflow.net polynomial l1 norm coefficients monomial | Question465899 explicitly uses integer polynomial coefficient-vector ℓ¹ size in monomial basis. Other L1-on-circle hits concern different norms. |
| arXiv within five years | site:arxiv.org polynomial coefficient l1 norm monomials after:2021-10-27 before:2026-10-28 | Typical Bohnenblust–Hille Ratios, submitted24Sep2026, discusses coefficient ℓp norms and arbitrary monomial supports. No exact named singleton theorem located. |

[General requests](../evidence/Roth.normOne_monomial/web-0.json), [nLab/nCatLab](../evidence/Roth.normOne_monomial/web-1.json), [Stacks/MO](../evidence/Roth.normOne_monomial/web-2.json), [arXiv](../evidence/Roth.normOne_monomial/web-3.json), [primary opens/failure](../evidence/Roth.normOne_monomial/web-4.json), [local excerpt](../evidence/Roth.normOne_monomial/local-literature.txt), [source hash](../evidence/Roth.normOne_monomial/local-literature-source.json).

Primary mathematical reference: Stephen Semmes, *Some basic topics in analysis related to shift operators*, [§2 pp5–6 and §8 pp16–18](https://math.rice.edu/~semmes/shft.pdf), models arbitrary finite-support coefficient functions and their delta basis. The [recent paper's abstract](https://arxiv.org/abs/2609.31779) confirms the conventional coefficient-norm framework. These sources motivate abstraction; the exact algebraic zero-preserving-size formulation is an abstraction verified against pinned mathlib, not attributed verbatim to literature. The literature supports the usual coefficient ℓ¹ interpretation; no contradictory convention for this explicitly defined norm arose. No naming claim depends on an absence search.

## Phase 4a — Parameters and hypotheses

| Parameter | Fixed parent interface | Expanded representation |
|---|---|---|
| σ : Type* | Already arbitrary universe, cardinality and emptiness | Replace exponent-index set by arbitrary ι in Finsupp. |
| e : σ →₀ ℕ | Needed to specify monomial; no degree/nonzero restriction | Any index i : ι suffices for single. |
| c : ℤ | Needed coefficient; all signs and zero included | `[Zero R]` in Finsupp, `[CommSemiring R]` for MvPolynomial. |
| ℝ output / absolute integer cast | Fixed by normOne's definition | Arbitrary `[AddCommMonoid A]`, size : ι→R→A, only size i0=0. |
| Implicit algebra instances | Canonical integer/real instances; none explicit to drop | No order, norm, multiplication or additive coefficient laws needed for generic Finsupp identity. |

## Phase 4b — Verified generality

**MAXIMALLY GENERAL** at the fixed `normOne` interface: there are no hypotheses to drop. Expanded representation is **STRICTLY NARROWER THAN STANDARD** relative to the conventional arbitrary-coefficient norm framework, and especially to the verified algebraic indexed-size law. These are restatements across representations, not successful edits to a nonexistent explicit typeclass parameter. No production edit is claimed.

The actual broader native statements are:

```lean
{ι R A : Type*} [Zero R] [AddCommMonoid A]
(i : ι) (r : R) (size : ι → R → A) (hzero : size i 0 = 0) :
  (Finsupp.single i r).sum size = size i r
```

and its `MvPolynomial` counterpart over `CommSemiring R`. Only zero preservation at the single selected index is required; global zero preservation is unnecessarily strong. A `[SeminormedCommRing R]` coefficient-norm specialization also compiles; that sufficient hierarchy is not claimed minimal. Cost CHEAP, never used to downgrade a contribution. [Raw generalized statements and guard](../evidence/Roth.normOne_monomial/native-raw-executed.lean.txt), [raw success](../evidence/Roth.normOne_monomial/native-raw-success.json), [norm specialization](../evidence/Roth.normOne_monomial/native-specific-executed.lean.txt), [generality record](../evidence/Roth.normOne_monomial/generality.json).

## Phase 4c — Nine modern-idiom checks

| # | Check | Finding / concrete consequence |
|---|---|---|
|1|Typeclasses instead of bundled predicates|No bundled hypotheses. Broader version uses existing Zero/AddCommMonoid classes.|
|2|Filters instead of metric sequences|No limits or topology.|
|3|Universal property instead of construction|No object is constructed. Free-module universal property would add unnecessary structure.|
|4|Bundled substructure instead of subset|No closure predicates or subset structure.|
|5|Weaker algebra hierarchy|Yes: CommSemiring for monomial representation, only Zero for coefficient Finsupp; broad existing API composes without integer arithmetic.|
|6|Higher categories|No categorical statement.|
|7|Concrete index generalization|Yes: exponent vectors may be arbitrary Finsupp indices; coefficient ℤ and size ℝ also widen as above.|
|8|Concrete-via-abstract diagnostic|Yes. Original proof body after padding rewrite has zero normOne identifiers and zero monomial identifiers; just simp. Within rewrite the only monomial-specific fact is support_monomial_subset. Generic single-index law captures all content; compiled, not guessed.|
|9|False-generalization guard|Original coefficient-abs size is recovered exactly; monomial coefficient Finsupp bridge is definitional and compiled. Dropping size i0=0 is false at coefficient0: constant size1 yields empty sum0 versus1 (`zeroNecessary`). Sup/height, Hamming count, Mahler measure and value-integral L1 are different whole-polynomial sizes and rejected as normOne replacements.|

Modern idiom available: yes, already existing indexed singleton-sum API. It avoids global norm instances and serves arbitrary finite coefficient families. No missing modernized theorem is suggested.

## Phase 4.5 — Infrastructure risk

n/a — theorem introduces no definitions, instances or definitional equalities. All six risk axes (instance diamonds, overlapping instances, coercion diamonds, defeq dependence, elaboration brittleness, universe constraints) are n/a for this theorem. The replacement requires explicit size binders because inference through normOne can fail; two rejected preparations document this, not infrastructure introduced by a theorem. No global polynomial Norm instance proposed.

## Phase 4.6 — Five proof-strategy checks

| # | Strategy check | Finding |
|---|---|---|
|1|Topology ε–δ vs filters|n/a finite algebraic identity.|
|2|Elements vs substructure inclusions|No substructure; direct Finsupp operation is the right abstraction.|
|3|Sequences vs nets|n/a no convergence.|
|4|Construction vs universal property|n/a no construction.|
|5|Missing helpers mathlib should have|No. sum_monomial_eq and sum_single_index already give the whole identity.|

REFACTOR-RECOMMENDED: use existing law directly, avoiding padding support and singleton coefficient simplification. CHEAP; no missing API.

## Phase 5 — Actual five-method formal search

All five methods ran on current, literature-standard and abstract forms. [Complete raw formal receipts](../evidence/Roth.normOne_monomial/formal-search.json) preserve exact queries and full responses. External indexes can differ from pinned revision; every decisive hit is checked in pinned native Lean.

| Method | Current | Standard | Abstract |
|---|---|---|---|
|Lean-Finder|Monomial integer coefficient ℓ¹ query: Polynomial.sum_monomial_index and other norm hits|Coefficient l1 monomial norm query: some unrelated norm hits|Zero-preserving single query: Finsupp.sum_single_index, DFinsupp analogue|
|Loogle|MvPolynomial.monomial, Finsupp.sum → sum_monomial_eq|"monomial", "sum" → same and univariate sum_monomial_index|Finsupp.sum, Finsupp.single → sum_single_index|
|LeanSearch|Absolute coefficient-sum query: coefficient/monomial API, mostly partial hits|Coefficient l1 query: unrelated formal multilinear norm identities|Abstract indexed-zero query: sum_single_index exact hit|
|rg|normOne_monomial/norm_one.*monomial: no pinned same-spelling result|sum_monomial, supNorm/gaussNorm_monomial: exact univariate analogue plus distinct norms|prod_single_index (to_additive source), sum_monomial_eq: decisive pinned source|
|Local name|normOne_monomial → project target|sum_monomial → MvPolynomial.sum_monomial_eq and others|sum_single_index textual aliases in monoid algebras; local index unavailable|

[rg current](../evidence/Roth.normOne_monomial/rg-current.json), [rg standard](../evidence/Roth.normOne_monomial/rg-literature.json), [rg abstract](../evidence/Roth.normOne_monomial/rg-abstract.json), [full-name untruncated](../evidence/Roth.normOne_monomial/rg-full-name.json). Local-index unavailability is not absence evidence. Generated additive Finsupp name does not occur as a theorem line in that source; `prod_single_index` has to_additive. Native #check confirms its actual signature.

Pinned existing law, `Mathlib/Algebra/MvPolynomial/Basic.lean:275–278`:

```lean
{R : Type u} {σ : Type v} [CommSemiring R]
{A : Type w} [AddCommMonoid A] {u : σ →₀ ℕ} {r : R}
{b : (σ →₀ ℕ) → R → A} (w : b u 0 = 0) :
  (MvPolynomial.monomial u r).coeff.sum b = b u r
```

Underlying `Finsupp.sum_single_index` is in `Mathlib/Algebra/BigOperators/Finsupp/Basic.lean` via `prod_single_index` lines68ff and requires only Zero R/AddCommMonoid A. [Pinned MvPolynomial source](../evidence/Roth.normOne_monomial/mathlib-mvpolynomial-basic.lean.txt), [Finsupp source](../evidence/Roth.normOne_monomial/mathlib-finsupp-basic.lean.txt), [native exact signatures](../evidence/Roth.normOne_monomial/native-raw-success.json). `Polynomial.sum_monomial_index` is analogous univariate API; `supNorm_monomial` and `gaussNorm_monomial` are semantically distinct measures overall.

## Phase 5.5 — Statement shape

Normal form: singleton coefficient sum reduces to size e c on RHS. Equivalent forms include explicit support sum, Finsupp.sum and MvPolynomial.coeff.sum. Existing sum_monomial_eq gives canonical abstraction; old normOne form is definitionally its absolute-cast specialization, verified directly. RHS normalization respected.

Syntactic generality: attempted existing MvPolynomial law, underlying Finsupp law, arbitrary indexed size and coefficient-norm form. All accepted. Prefer existing explicit indexed-size instantiation at use sites: inference through project normOne requires the size annotation. No opaque parent helper required.

Superfluous arguments: σ needed for polynomial type, e for the selected monomial, c for its coefficient and output. No explicit typeclasses/hypotheses to drop. Finite-variable, nonzero c and nonnegative c constraints are absent already. Broader zero premise is essential for uniform zero coefficient case, as native guard shows. Overall SHIP-AS-STATED locally; RESTATE-BEFORE-SHIP upstream would target a theorem already present, so no addition.

## Phase 6.0 — Full caller and inline audit

Source-level whole-word search finds three named consumers, three applications, all in declaring file; external-to-file references0. The declaration itself is the fourth textual hit. This is explicit source inventory, not opaque kernel/simp dependency closure. [Caller receipt](../evidence/Roth.normOne_monomial/rg-callers.json), [caller plans](../evidence/Roth.normOne_monomial/callers.json), [inline audit](../evidence/Roth.normOne_monomial/rg-inline.json).

| Caller | Source application | Refactor |
|---|---|---|
|Roth.normOne_mul_le96–102|simp [normOne_monomial, abs_mul] at102|Direct singleton-size law inside inner multiplication sum.|
|Roth.normOne_prod_le105–108|specialization at e0,c1 at108|Use same existing law for normOne1≤1, then finite-product inequality.|
|Roth.normOne_hasseDeriv_le148–157|rw [normOne_monomial,…] at155|Use direct singleton law, preserve cast/binomial bound.|

No separate complete monomial-size identity was rederived inline elsewhere. normOne_zero is related zero-polynomial API, not a duplicate complete monomial theorem. Three consumers establish utility but do not override an exact existing hit. No external repository searched or downstream absence asserted.

All **three entire proof bodies** freshly compile with monomial uses replaced by `NormMonomialAssessment.direct`, a newly checked direct application of existing Finsupp.sum_single_index; the fresh product also uses fresh multiplication. No use of own target in these snippets. This named assessment theorem is test scaffolding, not a proposed production wrapper. [Complete consumer source](../evidence/Roth.normOne_monomial/native-consumers-executed.lean.txt), [fresh receipt](../evidence/Roth.normOne_monomial/native-consumers-success.json), [direct Finsupp premise](../evidence/Roth.normOne_monomial/native-target-executed.lean.txt).

## Phase 6 — Composition and circularity controls

The exact old-interface replacement term is:

```lean
MvPolynomial.sum_monomial_eq (u := e) (r := c)
  (b := fun _ (z : ℤ) ↦ |(z : ℝ)|)
  (show |((0 : ℤ) : ℝ)| = 0 from
    (congrArg abs Int.cast_zero).trans abs_zero)
```

This is one existing singleton-sum-law application, with its explicit zero-size normalization obligation. Int.cast_zero and abs_zero are the two scalar facts; congrArg/trans transport that premise. No closing `simp [defs]` is used in the accepted replacement. Thus the Phase6b trivial-simp BORDERLINE heuristic does not control the verdict. Direct Finsupp route also compiles with explicit index/coefficient/size. Not a NO-composable decision based merely on counted tactics: exact more-general law exists and specializes definitionally through coeff and normOne. The original replay's terminal simp is retained only as replay evidence.

[Exact MvPolynomial replacement](../evidence/Roth.normOne_monomial/native-specific-executed.lean.txt) and [native success](../evidence/Roth.normOne_monomial/native-specific-success.json). The mathlib-only isolated raw13imports snippet imports no Roth, uses #check_failure Roth.normOne_monomial and independently defines the coefficient sum. It verifies both generic laws, current specialization and zeroNecessary. This excludes project simp circularity. No new axioms, sorry, unsafe, native_decide or raised limits. Only standard propext/Classical.choice/Quot.sound occur; complete receipts partial=false, success=true, no errors/warnings/timeouts.

Historical declaration78's native-consumers monomialValue replay is an explicit prerequisite context only, never relabeled fresh79 execution. Fresh79 native-specific supplies the original-shaped replay independently. Two earlier root target preparations failed inference/binder annotations; separately archived rejected evidence and not accepted proof success. [Verification inventory](../evidence/Roth.normOne_monomial/verification.json).

## Phase 7 — Actionable verdict

**NO-mathlib-has-it**, independently established. Existing building blocks: `MvPolynomial.sum_monomial_eq`, `Finsupp.sum_single_index`, `Int.cast_zero`, `abs_zero`; representation is definitional. There is no Mode B parent re-aim override needed: parent normOne is NO-composable, while this exact singleton law is independently already present. Padding parent's NO-mathlib-has-it is consistent but not the basis of this verdict.

Follow-up local refactor can remove this wrapper and apply the existing law directly at the three listed references, using explicit size annotations. Alternatively retain it in `Roth/CoeffNorm.lean` as project convenience until that separately authorized cleanup. This assessment changes no source. No upstream file/PR title/reviewer grouping is required for a NO verdict; no missing API or future human question remains. The prior accepted YES declarations do not form a contribution group with this already-existing theorem.

## Phase 8 — Completion and portability

All mandatory phases complete; theorem-only n/a justified. [Assessment](../evidence/Roth.normOne_monomial/assessment.json), [overview entry with full type](../evidence/Roth.normOne_monomial/overview-entry.json), [portable validator](../evidence/Roth.normOne_monomial/validate.py), [copy manifest](../evidence/Roth.normOne_monomial/copy-manifest.json). Validator checks current copy-manifest hashes, actual native success diagnostics/standard axioms, all source/pin hashes, protocol breadth and local links in scratch or integrated layout. Integration-only root-acceptance.json is excluded from the worker artifact-list guard; the current manifest remains authoritative. Root independent acceptance is pending.
