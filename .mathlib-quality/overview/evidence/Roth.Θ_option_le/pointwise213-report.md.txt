# Full mathlibable assessment: `Roth.index_le_lem6`

Canonical declaration **213/293**, `Roth/Theta.lean:556–587`; assessment date2026-10-28.
Verdict: **BORDERLINE-needs-human**. The assessment is complete. The remaining questions concern
future upstream API scope, not missing verification or a request blocking this repository review.
Production sources and pins are unchanged. Keep this useful theorem in `Roth/Theta.lean`.

## Phase0: baseline and scope

The clean2467-job build in [baseline-build.txt](../evidence/Roth.index_le_lem6/baseline-build.txt)
is reused only after a fresh match of all17 sources/pins against
[input-manifest.json](../evidence/Roth.index_le_lem6/input-manifest.json), recorded in
[inputs.json](../evidence/Roth.index_le_lem6/inputs.json). The target resolves at the exact
[source excerpt](../evidence/Roth.index_le_lem6/target-excerpt.lean.txt).
The entire985-line declaring module and its sole explicit caller were read. The module defines
the extremal index Θ and proves Lemmas5–7 supporting Roth's theorem. No `sorry`, new axiom,
unsafe proof, resource-limit increase, production edit or version change was used.

## Phase1: mathematical statement and proof

For a nonzero integer polynomial R with coordinate degrees at most r and coefficients bounded
by B, consider its weighted vanishing index at a coprime rational tuple h/q. If the distinguished
weight r_p is at least3, lies below δ times every complementary weight, and 0≤δ≤1, some integer
1≤l≤r_p+1 satisfies

`index(R,h/q,r) ≤ 2 (Φ_l + √Φ_l + √δ)`.

Here `M_l=(r₁+1)^((card τ+1)l) l! B^l 2^((card τ+1)lr₁)` and Φ_l adds the one-variable and
complementary-variable extremal indices at coefficient bound M_l and degree/index weights lr.
The ceiling r₁ bounds all coordinates. This is the individual-polynomial step before taking the
supremum/max in `Θ_option_le`; it is not itself the final Roth theorem or the full Dyson lemma.

`exists_det_eq_mul` supplies a nonzero mixed-Hasse determinant F with separated factors and
1≤l≤r_p+1. `mapped_det_ne_zero_aux` preserves its nonzeroness over ℝ. The row derivative degree
bounds and `weight_le_delta_aux` feed `sum_max_sub_le_index_det`, giving
`Σ_{ν<l}max(0,θ−ν/r_p)−lδ ≤ index F`. `index_det_le` gives `index F≤lΦ_l`. Combining these with
`min_le_sum_max` yields `min(lθ/2,r_pθ²/3)≤l(Φ_l+δ)`. `Θ_nonneg` supplies Φ_l≥0, and
`index_numeric_bound_aux` turns this inequality into the asserted square-root estimate.
These project theorems and new generalization helpers are **not existing mathlib calls**.

### Full original elaborated type

```lean
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
                    ∀ {B : ℝ} {R : MvPolynomial (Option τ) ℤ},
                      R ∈ Roth.RSet B r →
                        ∀ {h : Option τ → ℤ},
                          (∀ (j : Option τ), IsCoprime (h j) ↑(q j)) →
                            ∃ l,
                              1 ≤ l ∧
                                l ≤ r none + 1 ∧
                                  Roth.index ((map (Int.castRingHom ℝ)) R) (fun j ↦ ↑(h j) / ↑(q j)) r ≤
                                    2 *
                                      (Roth.lem6Φ q r (Roth.lem6M (Fintype.card τ + 1) r₁ B l) l +
                                          √(Roth.lem6Φ q r (Roth.lem6M (Fintype.card τ + 1) r₁ B l) l) +
                                        √δ)
```

The [native receipt](../evidence/Roth.index_le_lem6/original-receipt.json) records the exact type,
standard axioms and canonical293-value audit. The kernel pretty-printer explicitly elided
**3237 characters** from the original proof body; this is not claimed to be a full kernel-body
printout. The complete written source and full successfully compiled replay remain archived.

## Phase2: preliminary checks

**BIG**: this is the individual-polynomial content of source Lemma6, a substantial named step
in the Roth index argument. The exhaustive search is unchanged by this classification.
Theorem, not a definition: one-line-definition test and its exemptions are **n/a**.
The written proof has25 substantive/proof lines in the inventory and combines substantive
algebraic, height and numerical ingredients; it is not a one-line existing-library wrapper.

## Phase3: exhaustive literature

Every query below was actually sent. Exact requests, response digests/byte counts and clean
source locators are archived; full returned articles/search bodies are not copied into Git.

| Channel | Exact query or request | Finding and limitation |
|---|---|---|
| Specific web | `Roth theorem polynomial index lemma 6 Phi square root determinant Takloo Bighash Yin` | Princeton lecture17 and Stanford lecture17 describe index/Wronskian methods; exact normalization comes from local source. |
| General web1 | `Roth lemma index polynomial bounded coefficients rational points determinant proof` | Rational-point index/height formulation found; not an exact Lean replacement. |
| General web2 | `Dyson lemma Roth index polynomial differential determinant height` | Related Dyson/Roth strategies; no claim the two full statements coincide. |
| General web3 | `Thue Siegel Roth lemma recursive index bound separated variables Wronskian` | Separated-Wronskian proof context found. |
| Aliases web | `Roth auxiliary polynomial index lemma 6 Bombieri Siegel lemma generalized Wronskian` | Standard aliases and related auxiliary-polynomial constructions. |
| Optional ChatGPT | Standard form, generality and historical evolution | **n/a: ask_chatgpt_math unavailable**, as permitted by user; other channels retained. |
| Local | `rg` on `clean.tex`, Lemma `roth:lem6`, eqs13–17 and lower-bound passage | Exact recursive formula, degree/height separation and integer factor-height argument. |
| nLab | `site:ncatlab.org/nlab Roth Diophantine approximation polynomial index` | Returned operator-algebra index, not this arithmetic index. |
| nCatLab | `site:ncatlab.org/ncatlab Roth polynomial index weighted vanishing` | Actual distinct namespace requested; returned nLab/operator-index results outside namespace do not count as an exact hit. |
| Stacks | `site:stacks.math.columbia.edu multiplicity order vanishing determinant polynomial` | Trace/intersection multiplicity context; direct tag02MB gives local vanishing-order additivity, not the arithmetic height bound. |
| MathOverflow | `site:mathoverflow.net Roth lemma Dyson lemma polynomial index` | Question431381 asks how Dyson's lemma gives the small-index step; context, not an equivalent theorem proof used here. |
| recent arXiv | `site:arxiv.org Roth polynomial index Wronskian Diophantine approximation after:2021-10-28 before:2026-10-29` | Includes Hindes2209.09182, submitted2022-09-19; its characteristic-p dynamical setting needs different techniques. No exact recursive endpoint hit established. |

Evidence: [specific](../evidence/Roth.index_le_lem6/web-specific.json),
[general](../evidence/Roth.index_le_lem6/web-general.json),
[aliases](../evidence/Roth.index_le_lem6/web-aliases.json),
[local excerpt](../evidence/Roth.index_le_lem6/local-literature.txt),
[nLab](../evidence/Roth.index_le_lem6/nlab.json),
[nCatLab](../evidence/Roth.index_le_lem6/ncatlab.json),
[Stacks](../evidence/Roth.index_le_lem6/stacks.json),
[MathOverflow](../evidence/Roth.index_le_lem6/mathoverflow.json),
[arXiv](../evidence/Roth.index_le_lem6/arxiv.json),
[primary opens](../evidence/Roth.index_le_lem6/primary.json),
[primary followup](../evidence/Roth.index_le_lem6/primary-extra.json).

Primary sources: [Soundararajan/Petrow course notes](https://math.stanford.edu/~ksound/TransNotes.pdf),
section17, printed pp62–64 (Wronskian construction and comparison of indices);
[Stacks02MB](https://stacks.math.columbia.edu/tag/02MB), section10.121;
[Hindes2209.09182](https://arxiv.org/abs/2209.09182), abstract and submission date.
The Princeton PDF direct open timed out400; nLab direct open failed400. A Stanford literal
`17 Roth` find found nothing, then `Wronskians` located the relevant passage. Access failures
are not mathematical negative results. Local `clean.tex` is the exact reference for this Phi/M
formula; the external notes use a different parameter packaging and prove a small-index lemma.

Literature synthesis: this is Roth's rational-point small-index mechanism. The local paper
requires p≥2, strictly positive δ<1, strongly decreasing positive weights and positive q.
The Lean statement already permits arbitrary finite τ (including empty), weak ratios, δ endpoints,
and r_p≥3 without the paper's r_p>10/δ condition. There is no literature-supported assertion that
this particular recursive Φ envelope is the unique most general upstream interface.

## Phase4a–b: all parameters and hypotheses

| Parameter/hypothesis | Mathematical role | Assessment |
|---|---|---|
| `τ : Type*`, `[Fintype τ]` | Complementary variables, sums, cardinal and Θ | Arbitrary finite family; no `[Nonempty τ]` needed. Fintype retained for current cardinal/supremum interface. |
| Ambient DecidableEq | Finite manipulations | Already omitted by source; scratch classical choice is local, not a new public instance premise. |
| `δ : ℝ`, `hδ0 : 0≤δ` | Derivative row-weight bound and positivity of all r | Retained in full endpoint; real numerical core itself works with δ≤1 and no δ≥0. No claim full endpoint extends to negative δ. |
| `hδ1 : δ≤1` | `δ≤√δ` in numerical linear branch | Retained; a mere occurrence in one proof is not a proof of necessity. |
| `r : Option τ→ℕ` | Degree and reciprocal-index parameters | Natural degree bounds and real reciprocal weights are coupled by this interface; not arbitrary real weights. |
| `hrp : 3≤r none` | Positive weight and numerical `3l≤4r_p` | **Verified weakening to1≤r none**, using a new `/2` positive-part lemma and modified numerical argument. Natural r means this is precisely positivity. No optimality or zero-case impossibility claim. |
| `hratio` | Gives row derivatives weight≤δ | Retained for this degree-based determinant witness. Prior207's per-row-weight alternative is an ingredient, not automatically a combined endpoint generalization. |
| `r₁`, `hr₁` | Uniform ceiling for determinant coefficient envelope | Retained; sharper coordinatewise envelope would change M and needs a distinct interface, not a silent weakening. |
| `q : Option τ→ℕ`, `_hq : ∀j,0<q j` | Rational-point paper setting | **Verified deletion of `_hq`** with unchanged proof; arbitrary natural q including0 now allowed in scratch. Real division by0 is0, not a genuine rational denominator; semantic distinction recorded. |
| `B : ℝ` | Input coefficient bound | No separate B≥1 premise. Nonzero integer R and its coefficient bound already force B≥1; it need not be added. |
| `R`, `hR.1` | Integer polynomial/nonzero determinant witness | Nonzeroness retained for `exists_det_eq_mul`; no full zero-input extension claimed. |
| `hR.2.1` | Coordinate degree bounds | Feeds witness factor degrees and coefficient envelope; retained. |
| `hR.2.2` | Coefficient bounds | Feeds determinant height envelope; retained. |
| `h : Option τ→ℤ`, `hh` | Coprime numerator/denominator representatives | Coprimality feeds membership in the defining Θ families; dropping it at fixed q is not justified by fraction reduction, which changes q. |
| Coefficient ringℤ / real target | Discrete nonzero coefficient size≥1, real squares/square roots/suprema | Do not naively replaceℤ byℚ or arbitrary commutative rings. `100·(1/100)=1` with factor100>1 refutes naive factor-height transfer, not the entire arbitrary-rational-coefficient endpoint. |
| Existential l, `1≤l≤r_p+1` | Nonzero separated determinant rank | Preserved. Numerical abstraction allows l as real only for the numerical inequality; full determinant rank remains natural. |

Current form is **strictly narrower than the verified meaningful extension**, not claimed
maximally general. Proposed full scratch restatement changes only `_hq` removal and `hrp` to
`1≤(r none:ℝ)`; its exact complete elaborated type is in
[lowdegree receipt](../evidence/Roth.index_le_lem6/lowdegree-receipt.json).
The complete source is [lowdegree execution](../evidence/Roth.index_le_lem6/lowdegree-executed.lean.txt).
The no-q-only interface is independently compiled in
[noq execution](../evidence/Roth.index_le_lem6/noq-executed.lean.txt) and
[receipt](../evidence/Roth.index_le_lem6/noq-receipt.json).

The stronger finite inequality is
`min(lθ/2,r_pθ²/2)≤Σ_{ν<l}max(0,θ−ν/r_p)`.
It is freshly compiled over any linearly ordered field with `IsStrictOrderedRing`; its bounded
natural cutoff uses `Nat.findGreatest`, not a floor instance. It was first verified in accepted206
and is copied exactly with namespace changes into this complete execution. It is **new proof
content**, not a pinned existing-mathlib theorem. For the present natural r_p≥1, `/2` is stronger
than `/3`; no such constant-comparison claim is made for negative scales. The revised numerical
core uses `2l≤4r_p`, which follows from l≤r_p+1 and r_p≥1, preserving the original endpoint2.
The real scalar numerical core requires r_p≥1 as a sufficient condition; this is separate from
the full theorem's natural-degree/index interface.

The r_p=0 case remains outside the compiled extension. Degree_noneR=0 suggests a direct
complementary-variable/rename route, so failure of the current positive-weight method does not
establish that0 is impossible. No zero-threshold counterexample, necessity or maximality is claimed.
The broadened whole-module replay preserves the **original** statements of actual `Θ_option_le`
and later `Θ_lt`: it merely removes the now-unused q argument at the former's call and explicitly
converts3≤r_p to1≤r_p. It does not claim either downstream public API was itself generalized.

## Phase4c: nine modern-idiom checks

| # | Question | Answer and downstream consequence |
|---|---|---|
|1|Typeclasses instead of hypotheses|No artificial instance for a coefficient envelope/ratio; explicit inequalities avoid global instance ambiguity. Existing Fintype is appropriate.|
|2|Filters/topology|No limiting argument: finite determinant and arithmetic estimates.|
|3|Universal property|No new universal object. Existing rename/evaluation homomorphisms express the variable split.|
|4|Bundled substructure|RSet includes nonzero and bounded heights, not closure under addition/multiplication; it is not a Submodule.|
|5|Hierarchy weakening|Lower-order/determinant ingredients admit more general coefficient/order interfaces, but integer factor heights use discreteness. Full arbitrary-ring endpoint is not established.|
|6|Higher categories|No categorical content or downstream benefit from a categorification.|
|7|Concrete index|Natural degrees/rank stay natural; newly re-proved numerical core separates real θ,δ,r_p,l from polynomial data. Full index re-aim needs explicit reciprocal weights and zero handling.|
|8|Concrete-via-abstract diagnostic|After determinant bounds, final step uses only Φ≥0 and a min inequality. `abstractWitness` compiles for arbitrary nonnegative function Φ on natural l; enables reuse with other height envelopes. It is not a claim that determinant existence/height control disappear.|
|9|False-generalization guard|Do not replace real index0=0 with conventional order0=∞, or integer height by rational size. Numerical guards show why positive l and Φ≥0 cannot simply be erased from the original `/3` arithmetic schema; these are scalar-core counterexamples, not counterexamples satisfying the full project theorem premises.|

Modern idiom available: **yes, separate arithmetic-witness core from determinant construction**.
This separates a reusable numerical implication from the concrete integer height machinery, and
keeps generic order/multiplicativity API distinct from Diophantine approximation. It does not by
itself settle whether this final arithmetic endpoint belongs upstream or in a Roth leaf module.
The proof-body diagnostic records R in the witness/lower/upper stage; only the final arithmetic
stage becomes object-independent. No assertion that the entire proof is a generic numerical fact.

## Phase4.5: infrastructure risk

Theorem, not a definition/instance: each of diamonds, reducibility leaks, noncanonical unfolding,
instance-priority collisions, universe-data design and coercion-instance ambiguity is **n/a**.
No new instance or reducible data alias is proposed by this assessment. Scratch namespaces and
proof declarations do not alter the production instance graph.

## Phase4.6: five proof-strategy checks

| Check | Assessment |
|---|---|
|Topology/filter proof|n/a finite algebra, no neighborhoods.|
|Elementwise vs substructure algebra|Coefficient-height information is essential and not captured by ideal membership; do not lose size data through point-free notation.|
|Analysis sequences/nets|n/a no convergence or infinite series.|
|Category/universal property|Existing rename/evaluation homomorphisms suffice.|
|Missing helper API|Factor-height transfer, generic determinant order and the `/2` finite-sum bound are meaningful prerequisites; their own reports/verifications remain distinct from this endpoint.|

**REFACTOR-RECOMMENDED for future upstream**: expose the numerical witness implication, use the
verified `/2` finite bound, and package the algebraic witness/height dependencies deliberately.
This improves applicability at small positive weights and with alternative Φ envelopes. Cost is
not the verdict reason; mathematical audience and API placement are the open design issues.

## Phase5: actual five-method searches, including parent re-aim

All15 form/method cells ran, plus5 parent re-aim cells. Raw formal-search receipts are archived
as `search-{current,standard,abstract}-{leanfinder,loogle,leansearch,rg,local_search}.json` and
`reaim-*.json`. Exact queries/commands and complete responses are retained; pinned source rg
searches are untruncated files. External index revisions may differ from the project pin.

| Form | Finder | Loogle | LeanSearch | Pinned rg | Local |
|---|---|---|---|---|---|
|Current `index_le_lem6`|Roth AP-number false friends|Project name unknown; quoted retry gives no hit|AP-Roth results, not Diophantine index|Full target/Φ spelling search|Finds own project/evidence; index warming|
|Literature polynomial-index/height|Chevalley complexity and polynomial approximation, not endpoint|MvPolynomial index-name matches, unrelated monomial index|weighted-order support lemmas|Roth/Dyson/index-height searches|Many index homonyms; warming|
|Abstract determinant weighted order/height|Complexity/number-field height, not endpoint|weightedOrder and basic laws|Matrix.det_le plus weightedOrder coefficient laws|weightedOrder, infDegree, sqrt/min ingredients|Pinned weightedOrder names found; warming|
|Parent `index`→`infDegree`|No exact arithmetic endpoint|infDegree and product lower bound|generic infimum/support bounds|Exact infDegree/weighted-order search|infDegree found but index status error|

The quoted current Loogle retry is retained separately; an initial query error is not reported as
a clean negative. Local warming/error likewise never proves absence. Finder's `rothNumberNat`
hits concern three-term progression-free subsets, a different Roth theorem.

Pinned positive ingredient `MvPowerSeries.weightedOrder_mul` at
`Mathlib/RingTheory/MvPowerSeries/NoZeroDivisors.lean:146` is actually applied in the isolated
execution. `AddMonoidAlgebra.le_infDegree_mul` at
`Mathlib/Algebra/MonoidAlgebra/Degree.lean:637` and support-infimum infrastructure express order
estimates, not existence of this determinant rank, integer heights, coprime representatives or
recursive real Θ. Consequently the parent re-aim rule does **not** find the analogous whole law;
this is not a glue lemma about the parent definition. No unsupported NO-has-it inheritance.
`Matrix.det_le` controls determinant absolute value, not the weighted vanishing index of the
polynomial determinant and its recursive coefficient-family supremum.

The mathlib-only accepted numerical proof contains explicit failing bounded `simp` and
`positivity` closure probes, followed by the complete proof. Those failures only show these
specific automation routes did not close that arithmetic goal, not universal absence.
No broad resource-exhausting exact?/search was repeated or resource limit raised.

## Phase5.5: three statement-shape checks

1. **Normal form**: support-infimum/weighted-order formulations are canonical ingredients;
   the reciprocal real-weight and zero conventions require bridges. No existing normalized
   whole arithmetic endpoint was established.
2. **Syntactic generality**: the verified no-q and r_p≥1 statements and independent
   `abstractWitness` interface are easier to apply. The existing `Option τ` variable split already
   permits any finite distinguished variable via an equivalence; no fixed Fin ordering required.
3. **Superfluous arguments**: `_hq` is unused and verified removable; DecidableEq is already
   absent; the stronger finite bound lowers hrp. All remaining premises have roles above,
   without a claim that proof use establishes logical necessity.

## Phase6.0: complete caller and inline audit

Exact canonical enumeration plus `rg --no-ignore` and tracked `git grep` find **one explicit caller
and one application**, `Roth.Θ_option_le` at593, call at601. The original293-value kernel audit
finds **one direct value consumer**, the same caller. This is not a generated/simp/transitive
closure claim or a claim of zero type consumers. Read the complete
[caller record](../evidence/Roth.index_le_lem6/callers.json),
[source search](../evidence/Roth.index_le_lem6/source-search.json),
[tracked search](../evidence/Roth.index_le_lem6/tracked-source-search.json), and
[inline search](../evidence/Roth.index_le_lem6/inline-audit.json).

| Caller | Purpose | Verified experiment | Future application plan |
|---|---|---|---|
|`Roth.Θ_option_le`|Apply the per-polynomial witness, bound Φ_l by finite sup', then bound Θ|Whole original replay, no-q whole replay, stronger-weight whole replay and complete caller inlining all clean|For broadened target remove only hq argument and derive 1 ≤ r_p from 3 ≤ r_p; preserve original caller statement unless separately choosing its API.|

Inlining the whole25-line mathematical argument into the caller compiles, but destroys useful
proof decomposition. This is evidence of caller compatibility, **not** a recommendation to
remove the theorem as junk. The actual caller also uses `Θ_le_of_forall_index_le`, `Finset.le_sup'`
and nonnegative scalar multiplication; it is not itself identical to the individual-polynomial step.

## Phase6: composition and independent verification

**NOT-COMPOSABLE as a verified≤3 existing-mathlib-call term.** The argument needs the genuine
project determinant-existence theorem, lower/upper bounds, min-sum estimate and numerical step.
Neither project helper names nor the new finite/numerical abstraction count as existing mathlib.
The isolated arithmetic core is a full min/square-root proof, not a≤3-call library composition.
No closing `simp [defs…]` endpoint is claimed, and no search failure proves mathematical absence.

Accepted exact executions:

| Source | Verification and purpose |
|---|---|
|[original](../evidence/Roth.index_le_lem6/original-executed.lean.txt)|Whole original Θ namespace replay, target renamed, unchanged bodies; full original type/axioms, all public replay axioms, exact293 runtime present/value audit.|
|[noq](../evidence/Roth.index_le_lem6/noq-executed.lean.txt)|Whole module without target's q-positivity premise; actual caller statement preserved, single argument removed.|
|[lowdegree](../evidence/Roth.index_le_lem6/lowdegree-executed.lean.txt)|Whole module with new `/2` finite-sum proof, revised numerical core and r_p≥1 target; caller and final Θ_lt retain their statements.|
|[inline](../evidence/Roth.index_le_lem6/inline-executed.lean.txt)|Complete actual caller with the target's mathematical proof inlined; no circular invocation of original target.|
|[isolated](../evidence/Roth.index_le_lem6/isolated-executed.lean.txt)|Independent mathlib-only original/improved numerical cores, abstract witness, zero-division and rational-height guards, positive-l/Φ guards, weightedOrder_mul.|
|[isolated final](../evidence/Roth.index_le_lem6/isolated-final-executed.lean.txt)|Same independent core with explicit bounded closure probes and additional guard axiom check.|

Each clean native response is full/nonpartial, error/warning-free, no recovered sorryAx, and only
`propext`, `Classical.choice`, `Quot.sound`. The isolated source has exactly18 stable mathlib imports,
no Roth import and a `#check_failure Roth.index_le_lem6` guard. Native requests, elapsed times and
raw responses are exact in matching `*-receipt.json`, indexed by
[verification.json](../evidence/Roth.index_le_lem6/verification.json).
The first disk request was still elaborating/partial; its warming receipt is retained and **not**
accepted as verification. A preparation width guard caught one extended call before writing or
executing it; the wrapped subsequent source is the one verified. There are no failed proof runs
being passed off as accepted evidence.

## Phase7: verdict and concrete future choices

**BORDERLINE-needs-human**: the full endpoint packages Roth-specific determinant, discrete height
and extremal-family machinery. Literature confirms its mathematical role and scratch verification
exhibits useful broader statements. Neither establishes that this exact endpoint is an independent
mathlib API rather than a downstream Roth theorem leaf. This is a scope/design choice, not a
cost-based downgrade or incomplete proof assessment. Useful generic ingredients already assessed
YES are not inherited contribution verdicts for this whole endpoint.

1. Should the recursive Θ-index estimate enter a dedicated Diophantine-approximation leaf
   after its prerequisites, or remain in the downstream Roth development?
2. Should the independent numerical witness implication and `/2` finite-sum estimate be the
   primary reusable APIs, with this endpoint a corollary?
3. Should a future endpoint cover r_p=0 by a separate direct complementary-variable branch,
   or document positive natural weights as its intended interface?

Recommended action: retain local theorem and proof-stage separation; use the verified no-q,
positive-natural-weight formulation if later planning a source edit. Do not silently generalize
later positive-denominator APIs or treat signed/zero divisor conventions as interchangeable.
No human answer is needed to finish this read-only assessment. Root independently reviews,
accepts and publishes the completed evidence before updating progress.
