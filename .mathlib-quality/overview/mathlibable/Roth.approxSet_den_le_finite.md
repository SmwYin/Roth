# Roth.approxSet_den_le_finite — canonical269

**Verdict: BORDERLINE-needs-human.** The bounded-denominator arithmetic fact is useful and is not an independently verified existing mathlib theorem or a composition of at most three existing calls. Its appropriate upstream API grain remains a concrete design choice: arbitrary approximation functions or generic finite integer tubes. This is a completed assessment with three future upstream questions, `unresolved=[]`, and root acceptance pending. It does not pause the overview for user input. Production sources, pins and Git were not changed.

## Phase0 — baseline and scope

The shared baseline `lake build` completed successfully with2467jobs. All17 source/pin hashes were freshly compared against the tracked shared manifest and compared again at completion. The declaration resolves at Roth/Main.lean:73–96, is a theorem, and has no proof hole. Main proves Roth's theorem by reducing to algebraic integers, choosing rapidly growing approximants and comparing upper and lower bounds for an auxiliary polynomial. Entire Main and LeanEval modules and every direct caller were read. The prior accepted full-file boundary build at canonical228 is reusable; the next required boundary is289, so no file-end build was due at269.

Original-proof re-elaboration follows the new minimal-replay addendum: **the exact target declaration only**, renamed `Bounded269Original.replay`, with no necessary private helper. Existing public project ingredients remain imported. Namespace/name substitutions are documented in the preparation script. Native equality by `Subsingleton.elim` checks agreement of original and replay theorem types; it does not assert proof-construction identity. Original loaded kernel type, value and axioms were queried independently.

Evidence: [inputs](../evidence/Roth.approxSet_den_le_finite/inputs.json), [baseline](../evidence/Roth.approxSet_den_le_finite/baseline-build.txt), [Main](../evidence/Roth.approxSet_den_le_finite/source-Main.lean.txt), [LeanEval](../evidence/Roth.approxSet_den_le_finite/source-LeanEval.lean.txt), [preparation](../evidence/Roth.approxSet_den_le_finite/preparation-checks.json), [exact original execution](../evidence/Roth.approxSet_den_le_finite/original-executed.lean.txt), [raw native receipt](../evidence/Roth.approxSet_den_le_finite/original-receipt.json).

## Phase1 — mathematical content and full type

For arbitrary real numbers α and κ, there are only finitely many pairs of an integer h and a positive natural denominator q with q≤Q and |α−h/q|<1/q^κ. No irrationality, algebraicity, positive exponent, or coprimality assumption is involved. This is finiteness of each bounded slice; it does not say that all approximants are finite.

Full native elaborated type, obtained through `Lean.getConstInfo` and a tagged `pp.funBinderTypes` message:

```lean
∀ (α κ : ℝ) (Q₀ : ℕ),
  {hq : ℤ × ℕ | hq ∈ Roth.approxSet α κ ∧ hq.2 ≤ Q₀}.Finite
```

α is the center, κ controls the allowed error at each positive q, and Q₀ bounds the supplied denominator. The proof sums the finitely many nonnegative error radii for1≤q≤Q₀. The triangle inequality bounds |h/q| by |α| plus this sum; multiplication by q≤Q₀ bounds |h|. `Int.le_ceil` converts that bound into containment in a finite integer/natural rectangle, using `Finset.single_le_sum`, `Finset.finite_toSet`, and `Set.Finite.subset`.

The source body has no explicit project identifier. Kernel membership reduction uses `Roth.approxSet`, and the kernel also has two generated local simp-proof helpers. Complete project value closure is target, approxSet, and those two helpers; no other canonical project dependency occurs. The target has no declared simp attribute. Source-token, elaborated kernel, generated-helper and transitive scopes are distinguished in [dependencies](../evidence/Roth.approxSet_den_le_finite/dependencies.json) and the [compact scope receipt](../evidence/Roth.approxSet_den_le_finite/scope-receipt.json).

The full written proof is archived. The `pp.all` kernel printer and the long constant list contain explicit MCP elision markers: this is **not a complete kernel body dump**. Full tagged type, standard axioms, unchanged written source and exact293kernel-value audit are available independently. See [native-type metadata](../evidence/Roth.approxSet_den_le_finite/native-type.json).

## Phase2 — preliminary classification

**SMALL:** an elementary finiteness helper, neither a new mathematical structure nor a named theorem or the project's main result. Literature width remains exhaustive. The one-line-definition test and its three exemptions are n/a because this declaration is a theorem. The proof contains substantive numerator-bound reasoning; its short arithmetic appearance is not evidence of an existing mathlib replacement.

## Phase3 — exhaustive literature

Each web receipt preserves exact requests, response SHA256/byte count/status and selected clean titles/URLs/locators with original concise summaries. Full returned articles and search-result bodies were not persisted. The general search used three distinct actual queries. The recent search used `after:2021-10-29 before:2026-10-30`; publication dates were checked for the two recent papers cited below. Search success is not proof of absence.

| Channel | Actual query or checked source | Outcome and significance |
|---|---|---|
| General specific | `rational approximation bounded denominators finitely many numerators real number` | Standard rational-approximation context; lecture notes and bounded-denominator discussions. |
| General abstract | `finite lattice points bounded intervals finite fibers approximation function psi` | Finite interval/lattice mechanism is relevant; no exact named arbitrary-tube theorem identified. |
| General aliases | `Diophantine approximation arbitrary approximating function bounded denominator finiteness` | Arbitrary approximating functions are established vocabulary, beyond power laws. |
| Optional ChatGPT math | `ask_chatgpt_math` capability inventory | Justified n/a: unavailable; other channels not reduced. |
| Local reference | clean.tex1175–1187 and1577–1587 | Direct elementary bounded-denominator argument in reduction; later reduced-solution finite-fiber discussion. |
| nLab | `site:ncatlab.org/nlab discrete subset compact finite lattice` | Compact discrete finiteness perspective, finite-set closure. |
| nCatLab distinct | `site:ncatlab.org/ncatlab finite fibers finite set integers bounded`; retry `site:ncatlab.org/ncatlab "finite" "fiber"` | Results were out-of-namespace nLab pages. Direct nCatLab finite-set page access failed. No exact nCatLab hit claimed. |
| Stacks | `site:stacks.math.columbia.edu finite fibres finite set`; retry with quoted terms; open02NH | Quasi-finite scheme morphisms are different mathematics; no arithmetic generalization extracted. |
| MathOverflow | `site:mathoverflow.net Diophantine approximation bounded denominators finite` | Lower-bound discussion concerns asymptotic Diophantine estimates, not this finite slice. |
| Recent arXiv | `site:arxiv.org Diophantine approximation approximating function psi after:2021-10-29 before:2026-10-30` | 2024 multiplicative Duffin–Schaeffer and2022 homogeneous-function work use arbitrary ψ; no elementary slice theorem located as the main result. |

The local reference explicitly gives the bounded-q implication used here. [Pottmeyer's lecture notes](https://www.esaga.uni-due.de/f/lukas.pottmeyer/DioApp.pdf), §1.1 pp1–2, give integer numerator/positive denominator conventions and distinguish reduced rationals. [Frühwirth–Hauke2024](https://arxiv.org/abs/2403.11257), abstract, demonstrates the standard approximating-function axis, including nonmonotone functions. [Kleinbock–Skenderi2022](https://arxiv.org/abs/2205.01361) uses an approximating-function framework in a different setting. Neither paper is presented as a source for a direct existing mathlib theorem. [Stacks02NH](https://stacks.math.columbia.edu/tag/02NH) concerns quasi-finite schemes, and supplies no replacement for the integer arithmetic.

Concept identified: finite bounded-denominator slices, proved through finite integer intervals or a finite family of finite vertical fibers. The power law is unnecessary for this local finiteness mechanism: arbitrary finite real radii at each denominator suffice. This last extrapolation is supported by fresh Lean proofs, not merely inferred from the literature. There is no universal named literature standard for the exact proposed generic tube API.

Evidence: [general](../evidence/Roth.approxSet_den_le_finite/web-general.json), [named channels](../evidence/Roth.approxSet_den_le_finite/web-channels.json), [recent](../evidence/Roth.approxSet_den_le_finite/web-recent.json), [primary access](../evidence/Roth.approxSet_den_le_finite/web-primary.json), [local searches](../evidence/Roth.approxSet_den_le_finite/local-literature.json), [relevant local excerpt](../evidence/Roth.approxSet_den_le_finite/local-excerpt.tex.txt).

## Phase4a–b — generality and verified experiments

| Parameter/condition | Actual strength and checked generality |
|---|---|
| α:ℝ | Already arbitrary, including rational, zero, large and negative centers. No irrationality or nonzero condition can be dropped because none is assumed. |
| κ:ℝ | Already arbitrary, including negative exponents. Its only role is selecting a radius at each positive denominator. Replacing it by an arbitrary real function ψ freshly compiles. |
| Q₀:ℕ | Zero is allowed and gives the empty slice; any finite denominator set is the abstract finite-base version. |
| Supplied denominator0<q | Essential for this quotient-form API. Removing it admits every integer numerator at q=0 when α=0 and radius1; fresh infinite-set counterexample compiled. |
| Strict error inequality | Finiteness also holds with closed endpoints, verified in the independent tube theorem. The approximation definition's strictness need not be changed globally. |
| Numeratorℤ | Finite integer intervals are essential. Allowing arbitrary rational or real numerators would make a positive-width interval fiber infinite. |
| Ambientℝ | Arbitrary-radius numerator tubes additionally compile over `[Ring K] [LinearOrder K] [IsStrictOrderedRing K] [FloorRing K]`. No general real-exponent operation is asserted there. |
| No smoothness/growth conditions | No continuity, positivity, decay, or monotonicity of ψ is required; ψ is real-valued so each chosen radius is finite. Signed radii cause no problem. |

The current power-law spelling is narrower than the verified arbitrary-ψ slice fact. The literal theorem cannot be improved by removing an existing hypothesis: there are none beyond its parameters and the set predicate. Generalizing the semantic family is a restatement, and the upstream choice between a named approximation family and a raw generic lattice theorem still needs API judgment. The independent Ring/FloorRing theorem is a proven auxiliary formulation; it does not claim that a real power with arbitrary real exponent makes sense in that ring.

Verified arbitrary-radius slice:

```lean
theorem bounded_den_finite (α : ℝ) (ψ : ℕ → ℝ) (Q₀ : ℕ) :
    {hq : ℤ × ℕ | (0 < hq.2 ∧ |α - (hq.1 : ℝ) / hq.2| < ψ hq.2) ∧
      hq.2 ≤ Q₀}.Finite
```

Verified generic finite integer tubes:

```lean
theorem finite_radius {K ι : Type*} [Ring K] [LinearOrder K]
    [IsStrictOrderedRing K] [FloorRing K] (s : Set ι) (hs : s.Finite) (c r : ι → K) :
    {p : ℤ × ι | p.2 ∈ s ∧ |(p.1 : K) - c p.2| ≤ r p.2}.Finite
```

The arbitrary-ψ proof is **credited accepted267 scratch mathematics**, freshly compiled here and used to recover the exact original type and full callers. It is not an existing mathlib building block and does not transfer267's verdict. The finite-radius proof and ordered Ring/FloorRing weakening are fresh269scratch mathematics. A first generic `linarith` spelling failed over noncommutative Ring; the successful proof uses additive order equivalences and no stronger commutative hypothesis.

Boundary checks compiled: Q=0 empty for every α and ψ; negative exponent−3 at center−1000000; rational center3/7; closed endpoints over finite denominator sets; negative-radius emptiness. The set of all exact zero-center pairs `(0,n+1)` is infinite for every κ, so bounded-slice finiteness cannot be promoted to finiteness of all supplied-pair approximants. A separate q=0 counterexample verifies the positive-denominator guard.

Evidence: [isolated proof and endpoints](../evidence/Roth.approxSet_den_le_finite/isolated-executed.lean.txt), [clean isolated receipt](../evidence/Roth.approxSet_den_le_finite/isolated-receipt.json), [generic ordered-ring proof](../evidence/Roth.approxSet_den_le_finite/supplement-executed.lean.txt), [generic receipt](../evidence/Roth.approxSet_den_le_finite/supplement-receipt.json), [absence probe and q=0 test](../evidence/Roth.approxSet_den_le_finite/supplement2-executed.lean.txt), [receipt](../evidence/Roth.approxSet_den_le_finite/supplement2-receipt.json), [explicit credit](../evidence/Roth.approxSet_den_le_finite/prior-proof-credit.json).

## Phase4c — all nine modern-idiom checks

| Row | Check | Answer and concrete consequence |
|---|---|---|
|1|Typeclasses instead of preambles|No new approximation typeclass needed. Existing FloorRing/order instances suffice for generic integer bounds.|
|2|Sequences to filters|Yes for the consequence that infinite approximants have unbounded denominators; finite slices are the input to `Infinite.sdiff`. The target itself is a finite-set assertion, not a limit. No new filter proof is claimed here.|
|3|Universal-property construction|No; there is no object determined by a universal property.|
|4|Bundled substructure|No; approximating pairs are not an additive or multiplicative substructure. Retain a set so `Finite.image`, `subset` and `Infinite.sdiff` compose.|
|5|Hierarchy weakening|Yes for integer tubes: ordered Ring+FloorRing proved. This avoids requiring real topology or arbitrary real exponent infrastructure for the finite arithmetic core.|
|6|Higher categories|No; finite arithmetic fibers have no categorical content improved by this route.|
|7|Concrete index|Yes; arbitrary finite index set s in the verified tube formulation replaces natural denominator intervals. Existing `Finite.biUnion` then assembles fibers.|
|8|Concrete-via-abstract|Yes. The proof body never names approxSet; κ appears only in radius formulas. Replacing the power radius by ψ compiles and the exact power-law case is a one-line specialization. This enables nonmonotone radii and constants without repeating numerator bounds.|
|9|False-generalization guard|Pass for signed finite radii, arbitrary center/index and closed endpoints as independently checked. Rejected extrapolations: arbitrary dense numerator types, omitted positive quotient denominator, finiteness of all approximants, and real powers in an arbitrary ring. Reduced rationals identify different supplied pairs, so quotienting is not silently substituted.|

Modern idiom is available, but does not select one uniquely appropriate upstream theorem. The concrete consequence of the ψ restatement is exact use at all existing callers without exponent-specific numerator bounding. The generic tube formulation separates finite interval transport from approximation theory. This ambiguity is about API granularity, not proof cost. See [diagnostic](../evidence/Roth.approxSet_den_le_finite/concrete-diagnostic.json).

## Phase4.5 — infrastructure risk

N/a for all six risks: theorem kind introduces no typeclass diamond, reducibility leak, noncanonical data unfolding, instance-priority collision, universe-polymorphic data construction, or coercion ambiguity. Proposed generic statements are likewise theorems using existing instances. No new instance was introduced.

## Phase4.6 — proof strategy

| Row | Check | Assessment |
|---|---|---|
|1|Topology ε–δ versus filters|No ε–δ argument occurs; finite intervals are the direct mechanism.|
|2|Algebra elements versus substructures|No ideal/module closure fact; integer interval membership is the content.|
|3|Sequences versus nets|No sequence construction in the target. Unbounded-denominator consequences naturally use existing finite-set/filter API.|
|4|Category universal properties|Not applicable to this finite arithmetic estimate.|
|5|Missing helpers|A finite integer-cast tube lemma or arbitrary-ψ slice theorem would remove the global finite-sum bound from later applications. Both candidate shapes are freshly verified; existing finite-fiber infrastructure already supplies the outer assembly.|

**REFACTOR-RECOMMENDED:** for an upstream contribution, separate finite integer intervals from the specific power law. The existing sum/rectangle proof is correct; a finite-base/fiber argument avoids manufacturing one global sum and ceiling. The change is mathematically cleaner where varying centers/radii occur. Cost does not determine the verdict.

## Phase5 — all15formal cells and positive candidates

| Form | Lean-Finder | Loogle | LeanSearch | Source rg | Local name search |
|---|---|---|---|---|---|
|Current bounded-denominator approximation|LiouvilleWith and reduced-rational approximation results; no exact hit|`Set.Finite, Real.rpow`: empty|Dirichlet existence and rational-center exponent2 finiteness; different hypotheses|Current names and near matches checked|`finite_rat` returns rational-center theorem; index:error recorded|
|Literature finite integer intervals|LocallyFiniteOrder and lattice intersection results|`Set.Finite, Int.ceil`: empty|Integer interval API|ceil/floor, finite_Icc and interval proofs checked|`finite_int` returns unrelated names; index:error recorded|
|Abstract finite base/fibers|`Set.Finite.of_finite_fibers`, preimage and dependent-image results|Exact finite-fiber signature found|Same criterion and finite preimages|Finite unions/fibers source inspected|`of_finite_fibers` source hit; index:error recorded|

All exact queries and full raw tool receipts are in the [15cell matrix](../evidence/Roth.approxSet_den_le_finite/formal-search-matrix.json). External indices may differ from the pin. Local symbol indexing returned error, so its source-text hits are usable while empty results would not establish absence. Three initial rg calls had a nonexistent module path; exact rejected-path receipts were retained and all three cells rerun on the real Finset/Defs path. The full qualified-name source search is untruncated and empty; it is not used alone as an absence proof.

Pinned candidates checked with native signatures:

* `Set.Finite.of_finite_fibers`, Data/Set/Finite/Lattice:234, needs a finite image **and already finite fibers**. It does not prove the numerator bounds. Its complete existing proof assembles a finite biUnion and subset.
* `Set.Finite.biUnion`, `Set.finite_Icc`, and finite products supply the finite family of integer intervals; `Int.ceil_le` and `Int.le_floor` transport real/ring bounds to integer membership.
* `Rat.finite_rat_abs_sub_lt_one_div_den_sq`, NumberTheory/DiophantineApproximation/Basic:253, has a rational center, rational reduced inputs and exponent2. Its full proof uses a finite dependent union of bounded numerator intervals after a different denominator bound. It is not the current supplied-pair result and does not handle arbitrary α, κ or ψ.
* Broad lattice compactness results returned by semantic search require bounded-set/discreteness premises. Establishing those premises here is the arithmetic proof, and no direct specialization was found.

The generic finite-radius theorem's `exact?` closure probe runs **before** defining that theorem, with no project imports and standard resources. It did not close the goal; the explicit proof then compiled. This is bounded nonclosure evidence, not a universal proof of nonexistence. No resource limits were raised and no broad search was repeated after heartbeat exhaustion.

Evidence: [full name search](../evidence/Roth.approxSet_den_le_finite/full-name-search.json), [pinned mathlib snapshots and hashes](../evidence/Roth.approxSet_den_le_finite/mathlib-inputs.json), isolated native signature/positive-proof receipts above.

## Phase5.5 — statement shape

Normal forms considered: finite bounded slice of approxSet; raw arbitrary-ψ slice; finite set of integer pairs in varying closed tubes; finite image plus finite fibers. `Set.Finite` is the correct consumer-facing conclusion because all current callers remove or map a finite set. An explicit Finset could supply counts later, but would add decidability/choice packaging the callers do not need. This theorem has no iff orientation, so an RHS simp normal-form rule is n/a.

Syntactic generality was tested by exact old-form recovery from the raw ψ comprehension, and by all full caller replacements retaining signatures. Generic finite tubes have the clearest arbitrary-base statement; the approximation-slice theorem has the least call-site friction. The generic ring tube theorem uses closed endpoints and no radius-positivity hypothesis. These are verified alternatives, not a chosen foundational approximation redesign.

Argument audit: α determines the center, κ the radius profile, Q₀ the finite base. There is no dead argument or unused typeclass in the current theorem. κ can be replaced by a semantic function parameter, rather than dropped with an unchanged conclusion. Positive denominator belongs to approxSet and is essential to quotient-form finiteness. Irrationality and exponent positivity from callers must not be imported into this theorem.

Overall: **RESTATE-BEFORE-SHIP** if an upstream lemma is selected; keep local current statement until that API choice. The restatement is arbitrary-ψ slices or generic integer tubes, not a theorem falsely claiming that all approximants are finite.

## Phase6.0 — full actual callers, inline and duplication audit

Fresh scoped `rg --no-ignore` and tracked `git grep` agree on four call sites, in three declarations and two files. No other lexical caller was found. The exact canonical293audit independently found those same three direct kernel-value consumers, zero direct type consumers,293unique names in tracked order,293present constants and293kernel values. Private module names are generated from tracked order and independently checked by the pre-execution audit script.

| Caller | Exact source use | Role |
|---|---|---|
|Roth.reduction, Main:118–134|line124 once|Discard the bounded-denominator slice before scaling numerators and absorbing the exponent gap.|
|Roth.exists_reduced_approx, Main:164–189|lines170 and182|Bound reduced rational image under contradiction, then bound each rational-value fiber.|
|LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff, LeanEval:42–56|line49 once|Choose an approximant outside the bounded slice to contradict a uniform lower bound.|

All complete caller bodies were tested twice. Literal route adds a local `bound` containing the complete original target proof and changes all four calls to it. Generic route adds a local specialization of the newly proved arbitrary-ψ theorem. Caller signatures and every other proof step are retained, except namespace qualification of IsDiophantine and whitespace reflow. Two necessary private helper bodies, `approxSet_num_den_mem_aux` and `exists_pos_div_rpow_lt_aux`, were copied completely into each namespace. Six native original/copy theorem-type equalities and six standard-axiom checks passed.

Project/scratch value dependency traversal, including generated and private constants, verifies that none of these six caller proofs reaches the original bounded-denominator theorem or its generated helpers. Mathlib internals are not claimed to be exhaustively enumerated by that traversal. No truncated caller prefix or assumed desired conclusion was used.

| Decl A | Decl B | Same statement? | Same proof? | Action |
|---|---|---|---|---|
|approxSet_den_le_finite|finite rational-value fibers inside exists_reduced_approx|No; latter fixes a rational value and needs irrationality+positive exponent|Shares finite-slice endpoint; latter first bounds q by decay|Keep distinct; latter legitimately calls this theorem.|
|approxSet_den_le_finite|Rat.finite_rat_abs_sub_lt_one_div_den_sq|No; arbitrary supplied pairs versus reduced rationals/rational center/exponent2|Both finish with finite integer intervals|Reuse interval machinery, not an invalid direct theorem substitution.|
|approxSet_den_le_finite|credited267 arbitrary-ψ bounded_den_finite|Original is a verified specialization|Same finite rectangle mechanism after replacing radius with its absolute value|Candidate generic helper, explicitly new scratch mathematics.|
|approxSet_den_le_finite|new269 finite_radius|Related finite integer tubes, not literal same quotient statement|Finite varying intervals rather than uniform sum rectangle|Alternative upstream API grain; no false claim of existing mathlib equivalence.|

Inline-derivation search found no source bypassing duplicate of the exact result. Finiteness of rational-value fibers in exists_reduced_approx is not an overlooked duplicate. The theorem is not junk: all four uses express a reusable mathematical step.

Evidence: [lexical](../evidence/Roth.approxSet_den_le_finite/source-search.json), [tracked crosscheck](../evidence/Roth.approxSet_den_le_finite/tracked-source-search.json), [caller metadata/excerpts](../evidence/Roth.approxSet_den_le_finite/callers.json), [canonical audit](../evidence/Roth.approxSet_den_le_finite/canonical-consumers.json), [full actual replacements](../evidence/Roth.approxSet_den_le_finite/inline-executed.lean.txt), [raw receipt](../evidence/Roth.approxSet_den_le_finite/inline-receipt.json), [inline scope](../evidence/Roth.approxSet_den_le_finite/inline-audit.json).

## Phase6 — actual composition attempts

**NOT-COMPOSABLE under the strict≤3existing-call criterion.** The existing finite-fiber theorem needs the arithmetic image/fiber premises. A direct application without those premises was tested and fails. The original rectangle route additionally proves numerator inequalities and integer-bound transport. The independent tube route needs the absolute-value/order equivalences and explicit membership transport. These are real proofs, not projections or compositions of three pre-existing results.

The one-line recovery from `bounded_den_finite α (fun q ↦ 1 / (q:ℝ)^κ) Q₀` succeeds, but that theorem is newly proved267scratch mathematics, freshly replayed at269. Counting it as existing mathlib would give an invalid NO verdict. No closing `simp [defs]` experiment is being disguised as a NO-composable argument. See [composition evidence](../evidence/Roth.approxSet_den_le_finite/composition.json).

## Phase7 — verdict and concrete future upstream questions

**BORDERLINE-needs-human**, independently assessed. All phases and proof gates are complete. There is verified mathematical generality and genuine local reuse, while no direct existing theorem or eligible≤3call composition was established. The unresolved *upstream design* choice is whether to expose a small arithmetic slice API tied to an approximation family, or keep the underlying finite-tube result as general integer interval infrastructure. This is a question of API audience and granularity, not a cost-based downgrade and not an inherited parent verdict.

1. Should an upstream approximation family be parameterized by an arbitrary error function ψ and export this bounded-denominator finiteness lemma as its primary finite-slice theorem?
2. Should the new finite integer-tube theorem over ordered Ring+FloorRing and arbitrary finite bases be exposed as reusable interval infrastructure, with power-law approximation finiteness kept as a local corollary?
3. If neither new API has an additional intended consumer beyond this Roth development, should the present elementary slice helper remain project-local until an approximation-family PR establishes that audience?

Next action: retain Roth/Main's current helper; use the verified candidate statements and exact caller replacements when choosing the future API. If the ψ family is selected, group its finite-slice theorem with the approximation-family and frequent-witness bridges; accepted267itself is BORDERLINE, so it is not listed as an accepted YES contribution. No unrelated accepted YES theorem is proposed for grouping. No user decision is required to complete this read-only assessment.

## Phase8 — verification, limitations and handoff

Six accepted exact native sources: original focused replay+audit; isolated arbitraryψ+boundaries; six full callers; generic ordered-ring tube theorem; default-resource nonclosure probe+q=0 guard; compact project closure source. All accepted receipts show clean success, no warnings/errors, no recovered proof holes, and only `propext`, `Classical.choice`, `Quot.sound`. Disk requests are explicitly nonpartial; run_code receipts use their documented diagnostics/success format. Shared18 and disk9 imports stayed unchanged, with no extra import request or resource raises.

Three rejected native sources and receipts remain separately archived: first isolated pair-constructor syntax/deprecation warnings, second isolated tactic-layout failure, first generic ordered-ring `linarith` failure. They include recovered `sorryAx` in failed declarations and are excluded from accepted verification. Two inline preparation-width failures and the corrected source-path searches are documented; no stale source was executed after failed preparation. The original raw receipt write initially hit a stdin encoding issue; the exact in-memory result was saved with apply_patch, with no lost receipt.

The portable read-only validator checks the **current** copy manifest, fresh17source/pin hashes, full source snapshots, exact ordered/private canonical293array and runtime293presence/value results, accepted exact sources/raw native results/axioms, complete caller reconstruction,15formal cells, named literature requests, relevant local excerpts, stable imports, required overview fields, links and secret scan. Both scratch and simulated integrated layouts must pass before freeze. Root owns independent acceptance, integration and publication.

Evidence: [assessment](../evidence/Roth.approxSet_den_le_finite/assessment.json), [verification](../evidence/Roth.approxSet_den_le_finite/verification.json), [validator](../evidence/Roth.approxSet_den_le_finite/validate.py), [fresh final hashes](../evidence/Roth.approxSet_den_le_finite/fresh-final-inputs.json), [final validation](../evidence/Roth.approxSet_den_le_finite/final-validation.json), [freeze](../evidence/Roth.approxSet_den_le_finite/freeze-record.json).
