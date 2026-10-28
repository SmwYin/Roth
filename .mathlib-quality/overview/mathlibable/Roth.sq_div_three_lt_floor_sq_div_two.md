# Roth.sq_div_three_lt_floor_sq_div_two — declaration 202

**BORDERLINE-needs-human.** The statement is an elementary, source-specific floor comparison with no explicit project callers. The original proof is sound. A weaker sufficient hypothesis `5 ≤ a` and a floor-free ordered-ring lemma compile, but neither is an existing mathlib replacement. The remaining decision is whether a numerical corollary with these particular constants warrants upstream API. No production changes are proposed as already performed.

## Phase 0 — Baseline

`lake build` succeeded (2467 jobs) in the shared baseline. All 17 production-source/pin hashes were freshly recomputed and match that baseline. Declaration resolves uniquely at `Roth/Theta.lean:300`, theorem, no sorry. Theta defines bounded polynomial families and their supremal index, proving the one-variable, recursive and final exponential bounds in the proof of Roth's theorem. The complete 985-line declaring module was read and archived, and its whole namespace body was replayed successfully under a fresh namespace in the actual project context.

Evidence: [baseline](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/baseline-build.txt), [fresh17](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/source-hashes.json), [complete source](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/source-Theta.lean.txt), [verification](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/verification.json).

## Phase 1 — Mathematical content and exact type

For a real number greater than ten, its square divided by three is strictly smaller than half the square of its natural floor. This is the second FACT in the paper's proof of Lemma6. The proof uses the strict rounding error bound `a < floor(a)+1`, nonnegativity of the natural floor, and polynomial arithmetic. No property of the polynomial-index construction occurs in the statement or proof.

The sole variable is an implicit `a : ℝ`; the sole explicit hypothesis is `ha : 10 < a`. All apparent surrounding finite-type parameters disappear from the elaborated type:

```lean
∀ {a : ℝ}, 10 < a → a ^ 2 / 3 < ↑⌊a⌋₊ ^ 2 / 2
```

Kernel axioms are exactly `propext`, `Classical.choice`, `Quot.sound`. The full type and canonical kernel-value audit are complete. The tool's pretty-printed proof body explicitly elides71913characters; this is disclosed, and the raw returned receipt is retained unchanged. It is not a complete pretty-printed kernel-body dump.

Evidence: [type metadata](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/native-type.json), [exact original executed source](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/floorcompare202-original-executed.lean.txt), [raw receipt](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/floorcompare202-original-receipt.json).

## Phase 2 — Preliminary checks

SMALL: this is a numerical helper, not a new structure, named theorem, or module main result. Exhaustive literature search still applies. The one-line definition-only test is n/a: this is a theorem, despite its one-tactic proof. No definition exemption is being used to justify inclusion.

## Phase 3 — Exhaustive literature protocol

Every actual request, response SHA256/byte count, returned URL locator, access limitation and concise original summary is archived; article and search-result bodies are not persisted. The search window is after2021-10-28 and before2026-10-29. Search-engine displayed crawl/publication estimates are not treated as authoritative event dates.

| Channel | Actual query/request | Result and relevance |
|---|---|---|
| General web: specific | `floor function square inequality x squared 3 floor x squared 2 x greater than 10` | Elementary floor material; no identified independently named theorem with these constants. |
| General web: general | `floor function inequalities x minus 1 less than floor x powers ordered field` | Primary Toronto floor handout; defining interval bound, not the numerical corollary. |
| General web: aliases | `integer part fractional part floor function quadratic estimates Roth theorem` | Integer-part/fractional-part formulations and related floor literature. |
| Optional mathematical assistant | n/a: `ask_chatgpt_math` unavailable | No substitute answer invented. |
| Local references | Read `clean.tex` §5, lines851–893 | Exact second FACT, lines879–889: α>10 and n=floor α≥10 imply the comparison. The source does not assert an optimal constant. |
| nLab | `site:ncatlab.org/nlab floor function integer part Galois connection` | Floors and ceilings: integer-part bounds and adjunction. Direct open failed400 unsupported `application/xhtml+xml`; returned search text was available. |
| Distinct nCatLab | `site:ncatlab.org/ncatlab floor function inequality integer part`; retry with quoted floor/inequality | Returned /nlab material, no exact /ncatlab hit. No evidence of a categorical quadratic-comparison API. |
| Stacks Project | `site:stacks.math.columbia.edu floor function integer part inequalities`; retry quoted floor | No identifiable exact result returned. No absence theorem inferred. |
| MathOverflow | `site:mathoverflow.net floor function inequality squares bound` | MO421435 (2022), a different multivariate quadratic floor inequality proved using convexity; not a replacement. Opened the actual question and answer. |
| Recent arXiv | `site:arxiv.org floor function inequalities quadratic after:2021-10-28 before:2026-10-29` | Related and irrelevant results, no exact replacement. Supplementary primary arXiv2312.02198 (submitted2Dec2023) studies characterizations of floor/ceiling, not this comparison. |

[General query receipts](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/web-0.json), [nLab/nCatLab/Stacks](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/web-1.json), [MO/recent arXiv/retries](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/web-2.json), [actual source access](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/web-3.json), [local locator/hash](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/local-literature.json), [local excerpt](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/clean-lemma6-excerpt.tex.txt).

The standard concept is the integer part with a rounding error in `[0,1)`. [Campesato's primary handout, page5](https://www.math.toronto.edu/campesat/ens/21W/l17-handout.pdf) states the defining interval. [nLab's floor entry](https://ncatlab.org/nlab/show/floor) relates floor to an order adjunction. [Hooshmand's2023 paper](https://arxiv.org/abs/2312.02198) concerns functional characterizations. The numerical constants2,3,10 are the local paper's specialization; the broader invariant is control of polynomial growth using a bounded rounding error. The abstract ring and cutoff5 refinements below are independently proved, not claimed to be literature-standard theorems discovered in those sources.

## Phase 4a — Parameter and hypothesis audit

| Parameter/hypothesis | Current form | Verified weakening / boundary |
|---|---|---|
| Scalar | `ℝ` | `Field K`, `LinearOrder K`, `IsStrictOrderedRing K`, `FloorSemiring K`: original proof compiles unchanged. Completeness, topology, logarithms and analytic structure are unused. |
| Size | `10 < a` | `5 ≤ a` suffices. `Nat.le_floor` gives `5 ≤ floor(a)` and the same polynomial comparison follows. In particular equality at5 is allowed. This is a verified sufficient threshold, with no claim of smallest real threshold or maximality. |
| Lower-bound necessity | A positive size restriction | The unrestricted theorem fails at0; replacing the bound by `4 ≤ a` (or `4 < a`) fails at99/20, whose natural floor is4. These are certified counterexamples to those specific weakenings. |
| Floor convention | Natural floor | `FloorSemiring` suffices; `FloorRing` is not required. The floor-free result removes rounding structure entirely, while preserving its numerical premise explicitly. Signed-floor conversion would be a representation bridge, not definitional equality. |
| Divisions and constants | squares divided by3 and2 | Equivalent division-free form is `2*a² < 3*n²`. With `0≤a`, `5≤n`, `a<n+1` this compiles over `CommRing K`, `LinearOrder K`, `IsStrictOrderedRing K`. The proof uses no integrality or lower bound `n≤a`. |
| Abstract nonnegativity | `0≤a` in floor-free schema | Essential to that schema: `a=-100,n=5` satisfies the other two premises but fails the conclusion. It is derived from `5≤a` in the original application. |

## Phase 4b — Verified generality verdict

The real-specific and cutoff10 restrictions are stronger than necessary. This is **verified narrower than the available abstract formulation**, without declaring a literature-standard optimized bound or a maximally weak hierarchy. Original-to-generic is a mechanical scalar replacement. The cutoff improvement and floor-free helper are new proofs. Both were checked with clean native diagnostics, not merely suggested from the class hierarchy.

```lean
theorem genericFive {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    [FloorSemiring K] {a : K} (ha : 5 ≤ a) :
    a ^ 2 / 3 < (⌊a⌋₊ : K) ^ 2 / 2

theorem floorFree {K : Type*} [CommRing K] [LinearOrder K] [IsStrictOrderedRing K]
    {a n : K} (ha : 0 ≤ a) (hn : 5 ≤ n) (hlt : a < n + 1) :
    2 * a ^ 2 < 3 * n ^ 2
```

These are statements of compiled new helpers in the [isolated exact source](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/floorcompare202-isolated-executed.lean.txt), with [successful raw receipt](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/floorcompare202-isolated-receipt.json). `realSpecialization` discharges `5≤a` from `10<a` and specializes the new helper. It does not count as an existing-mathlib replacement. Further ratio/threshold optimization remains outside any claimed maximality result. Cost is not used to select the verdict.

## Phase 4c — Modern-idiom check: all nine rows

| # | Question | Finding and downstream consequence |
|---|---|---|
| 1 | Typeclasses for structural hypotheses | Yes: the generic scalar statement uses existing ordered-field and FloorSemiring classes; applies also to rational/other floored ordered fields without rebuilding real analysis. No new instances. |
| 2 | Filters/nets instead of sequences | No: a single pointwise arithmetic inequality, no convergence premise. |
| 3 | Universal-property object | No new object is constructed. Floor already has a Galois-connection API; restating the comparison as an adjunction would hide the polynomial argument. |
| 4 | Bundled substructures | No closure predicate or substructure appears. |
| 5 | Weaker algebraic hierarchy | Yes: the exact signature generalizes to floored ordered fields; division-free polynomial content works for the stated ordered CommRing. This removes completeness and division infrastructure for arbitrary cutoffs. |
| 6 | Higher categories | No: no categorical theorem or categorical construction here. |
| 7 | Concrete indices/scalars | Yes for `ℝ` as above. The natural floor's ℕ codomain represents integral rounding, and is retained in its floor corollary. The floor-free helper takes arbitrary ring element `n`, a genuinely wider approximation interface. |
| 8 | Concrete-via-abstract diagnostic | Fires: the one-line body contains0 occurrences of `Real`/`ℝ`, no real-specific API, and1 line invoking `Nat.lt_floor_add_one`. It uses an abstract rounding-error inequality plus ordered polynomial arithmetic. `floorFree` verifies the extracted content; `genericFive` supplies all actual floor premises. |
| 9 | False-generalization guard | Pass: the generic floor theorem specializes to the same natural floor and original conclusion. Arbitrary `n` is explicitly a new approximation parameter, not a claim every ordered ring has a floor. The missing `0≤a` case is guarded by the negative counterexample. |

[Executed concrete-via-abstract body diagnostic](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/proof-body-audit.json).

Modern organization is available, with actual downstream consequences: use the existing `Nat.le_floor`/`Nat.lt_floor_add_one` interface on any floored ordered field, or a floor-free approximation in an ordered ring. This is mathematical reorganization, not evidence by itself that the specialized numeric theorem should be upstreamed.

## Phase 4.5 — Infrastructure risk

n/a: theorem, not a definition/class/instance. Six rows are recorded for completeness.

| Risk | Status and reason |
|---|---|
| Typeclass diamond | n/a: theorem introduces no class or instance path. |
| Reducibility leak | n/a: opaque proof constant introduces no data-level reducible body. |
| Noncanonical unfolding | n/a: no new definition or simp attribute. |
| Instance priority | n/a: no instance declaration or priority. |
| Universe restriction | n/a: the original scalar is fixed; compiled generic theorem quantifies `Type*` without new universe machinery. |
| Coercion ambiguity | n/a: existing natural casts/floor coercions; no new coercion. |

## Phase 4.6 — Proof strategy: all five rows

| # | Question | Assessment |
|---|---|---|
| 1 | ε–δ versus filters | No topology or neighborhood argument. |
| 2 | Elements versus ideal/submodule inclusion | Numerical polynomial inequalities; no substructure inclusion to expose. |
| 3 | Sequences versus nets | No limit. |
| 4 | Construction versus universal property | No constructed mathematical object. |
| 5 | Missing helper that should exist | Potential floor-free numeric-comparison helper, but no demonstrated recurring mathlib need for exactly2,3,5. The compiled helper is new proof, not a missing standard primitive inferred from a failed search. |

Current strategy is MATHLIB-IDIOMATIC for a local arithmetic fact: a standard floor bound followed by `nlinarith`. For upstream organization, prefer the more general statement if there is demand. The [alternative square-monotonicity route](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/floorcompare202-composition-executed.lean.txt) compiles but still needs substantive arithmetic; [receipt](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/floorcompare202-composition-receipt.json). No performance or cost argument is used to downgrade a suitable generalization.

## Phase 5 — Five methods on all three forms

| Form | Finder | Loogle | LeanSearch | Source rg | Local name search |
|---|---|---|---|---|---|
| Current real quadratic floor comparison | search0 | search1 | search2 | rg-current | search3 |
| Literature floor-error bounds | search4 | search5 | search6 | rg-standard | search7 |
| Abstract ordered-ring square comparison | search8 | search9 | search10 | rg-abstract | search11 |

All15cells were actually executed. Exact requests and complete raw responses are in [search0](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/search-0.json), [search1](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/search-1.json), [search2](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/search-2.json), [search3](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/search-3.json), [search4](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/search-4.json), [search5](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/search-5.json), [search6](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/search-6.json), [search7](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/search-7.json), [search8](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/search-8.json), [search9](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/search-9.json), [search10](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/search-10.json), [search11](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/search-11.json), [rg-current](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/rg-current.json), [rg-standard](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/rg-standard.json), [rg-abstract](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/rg-abstract.json).

Pinned positive APIs, with exact native signatures and actual proofs using them: `Nat.lt_floor_add_one`, `Nat.sub_one_lt_floor`, `Nat.le_floor`, `Nat.floor_eq_iff` in `Mathlib/Algebra/Order/Floor/{Defs,Semiring}.lean`; `sq_lt_sq₀` in `Mathlib/Algebra/Order/GroupWithZero/Basic.lean`; `sq_lt_sq'` in `Mathlib/Algebra/Order/Ring/Abs.lean`. Source archives and hashes are indexed in [mathlib inputs](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/mathlib-inputs.json). Native `Nat.lt_floor_add_one` has a weaker signature than some external-index displays: the exact pinned signature is authoritative.

Near hits were checked honestly: `Behrend.div_lt_floor` compares `x/exp(1)` with floor(x/2) and has a different threshold; `mul_pow_le_nat_floor_pow` and `sum_div_nat_floor_pow_sq_le_div_sq` concern discretized exponential sequences/sums. `Int.div_two_lt_floor` has coefficient1/2 and signed floor, not the needed sqrt(2/3) relative bound. These are not replacements. All four local-search receipts say `index: warming`; source matches are real, but no empty or partial index result proves absence. External indices can differ from this pin.

An additional [untruncated full-name search over all pinned mathlib](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/rg-full-name.json) returned no lexical match. That result alone is not an absence proof.

The compiled `closureGuards` tests `exact?`, `simp`, and `linarith` before introducing new helpers, and each fails to close the goal; `nlinarith` then proves it. No raised limits or forbidden proof mechanisms. This bounds the claim: no exact existing replacement or strict three-existing-call composition was established. It is not a global absence proof.

## Phase 5.5 — Three statement-shape checks

**Normal form:** equivalent positive-denominator forms include `a²/3 < floor(a)²/2` and `2*a² < 3*floor(a)²`; square-root ratio forms would introduce additional analytic structure. The paper's division form is readable locally; the division-free form is more general algebraically. This is an inequality rather than an equivalence lemma, so RHS simp-normal-form orientation is n/a.

**Syntactic generality:** compiled `floorFree` takes an arbitrary approximation `n` and premises `0≤a`, `5≤n`, `a<n+1`. `genericFive` restores the natural-floor API and discharges its nontrivial floor premise with `Nat.le_floor`. `viaSquareMonotonicity` separately verifies the division and square monotonicity normalization. Choice depends on whether the API serves rounded values or general approximations.

**Superfluous arguments:** no unused finite-type parameters survive elaboration. Real completeness is unnecessary; cutoff10 is sufficient but replaceable by5 inclusive. Some size restriction cannot be discarded (zero counterexample). In the floor-free form, nonnegativity cannot be discarded (negative counterexample). No claim that every algebra/order class in the generic forms is mathematically minimal.

Statement-shape verdict: RESTATE-BEFORE-SHIP if upstreaming is chosen; keep local paper-facing spelling only for documentary purposes. No automatic API addition follows from this diagnosis.

## Phase 6.0 — Every caller and inline audit

| Caller class | Count | Evidence |
|---|---|---|
| Source target occurrences | 1, declaration itself at300 | Fresh no-ignore rg, tracked git grep, and production inventory searches agree. |
| Explicit callers within declaring file | 0 | Fresh lexical enumeration over all293declarations. |
| Explicit external-to-file/project callers | 0 / 0files | No-ignore and tracked searches. |
| Canonical direct kernel-value consumers | 0 | All293ordered names loaded and inspected. |
| Canonical direct kernel-type consumers | 0 | Separate type-constant inspection. |
| simp attribute | none | Source declaration has no attribute; no claim of a hidden simp consumer. |

[No-ignore callers](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/callers.json), [tracked callers](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/tracked-callers.json), [inventory callers](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/inventory-callers.json), [lexical audit](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/lexical-enumeration.json), [canonical snapshot](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/canonical-snapshot.json), [pre-execution gates](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/canonical-gates.json).

[Inline search](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/inline-search.json) and [full-body overlap audit](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/inline-audit.json) distinguish neighboring mathematics from re-derivation of this same statement. `floor_sq_div_two_le_sum` is a triangular-sum lower bound. Private `mul_sq_div_three_le_sum_max_of_pos_aux` proves `(θr)²/3 ≤ sum(θr−ν)` using the exact Gauss identity and nonnegative remainders; it then rescales and compares with a max-sum. It does **not** prove the strict intermediate `(θr)²/3 < floor(θr)²/2`, and works without the cutoff10 that this intermediate would need. `min_le_sum_max` therefore bypasses this source FACT by a stronger direct strategy, not by re-deriving an identical strict floor-square theorem. `sqrt_lt_nat_floor_aux` in MainLemma proves a different power comparison; its full short body was read and replayed as `sqrtComparison` in the mathlib-only composition experiment.

The kernel consumer audit is direct constants in canonical values/types, not transitive/simp dependency closure or a census of external users. There are no actual target callers to refactor or replay; the full original declaring-module body was replayed successfully, rather than inventing a caller. [Exact full replay](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/floorcompare202-fullmodule-executed.lean.txt), [complete native receipt](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/floorcompare202-fullmodule-receipt.json).

## Phase 6 — Actual composition experiments

| Attempt | Executed outcome | Interpretation |
|---|---|---|
| `nlinarith [Nat.lt_floor_add_one a]` | Compiles under original and generic scalar signatures | One tactic generates a polynomial proof, not a chained existing theorem term. |
| `nlinarith [Nat.sub_one_lt_floor a]` | Compiles in `viaSubOne` | Equivalent rounding-error API, still a new arithmetic proof. |
| `sq_lt_sq₀` applied to the floor upper interval, then numerical comparison | Compiles in `viaSquareMonotonicity` | Existing square monotonicity proves only `a²<(floor(a)+1)²`; cutoff inequality is additional substantive arithmetic. |
| New `floorFree` then `genericFive` then original specialization | Compiles; all supplied premises discharged | Real generalization/composition experiment, but helpers are newly proved, not existing mathlib calls. |
| `exact?` / `simp` / `linarith` only | Negative guards pass before new helpers | Limited search/automation evidence; not proof of universal noncomposability. |

No ≤3 existing-call term was verified. Phase6b explicitly excludes substantive normalization/automation as a trivial composition. Existing floor and square lemmas are useful building blocks but do not alone justify NO-mathlib-has-it or NO-composable. Parent project helpers are never counted as mathlib building blocks, and new-helper proofs never circularly use the target. There were no rejected executed native drafts in this assessment.

## Phase 7 — Actionable verdict and questions

**BORDERLINE-needs-human.** The source-specific comparison is unused by this development and the final max-sum proof avoids the strict intermediate altogether. Literature supports a basic floor-error principle; no independent standard named role for these exact constants was established. Conversely, the short `nlinarith` proof is a real proof under the command's composition gate, so shortness does not certify a NO-composable verdict. Verified scalar/cutoff generalization gives a concrete potential upstream statement, but does not establish mathematical demand for it. This is a judgment about API usefulness/grain, not cost or unfinished verification.

1. Should mathlib expose the specific squared-floor coefficient comparison, or should it remain a project-local numerical fact derived from floor error bounds?
2. If upstream API is desired, should its primary statement be the floor-free ordered-ring approximation lemma, with the floored ordered-field version as corollary?
3. Should an upstream floor corollary adopt the verified inclusive sufficient cutoff5 while the paper-facing cutoff10 endpoint is removed or retained locally only as documentation?

Concrete future local action: consider removing this unused public endpoint from `Roth/Theta.lean` during a separately authorized refactor; there are0explicit callers and0canonical direct consumers to update. If documenting the paper's two FACTs is a deliberate goal, retain it locally with that reason rather than presenting it as necessary infrastructure. This is not a claim of external deadness. The private direct-sum argument must remain independent; it supplies the actual downstream bound.

A potential upstream floor corollary belongs near `Mathlib/Algebra/Order/Floor/Semifield.lean`, subject to hierarchy/import review; a floor-free inequality would need demonstrated broader demand before choosing an arithmetic home. This is a provisional design option, not a YES proposal or a staged PR. No accepted-YES grouping is inferred from any neighboring declaration.

## Phase 8 — Completion and trust boundary

All mandatory phases are complete, unresolved verification is empty, root acceptance remains pending. Four exact native runs succeeded with no warnings/errors/sorry, standard axioms only: original type/kernel audit, mathlib-only generalization/necessity/closure guards, mathlib-only alternative compositions, and whole Theta body replay. Original and full replay each passed the pre-execution exact-order293 guard and runtime293unique/present/value checks. The isolated files use the exact persistent18import prefix, while the disk document retains all9original imports. No production, pin, Git, overview or progress edits occurred. [Phase metadata](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/phase-evidence.json), [portable read-only validator](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/validate.py), [assessment](../evidence/Roth.sq_div_three_lt_floor_sq_div_two/assessment.json).
