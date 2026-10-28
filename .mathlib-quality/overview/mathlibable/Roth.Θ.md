# Roth.Θ — full mathlibable assessment

**Verdict: NO-mathlib-has-it.** The outer construction is exactly the existing `SupSet.sSup` applied to the index family. Re-aiming the parent family at `Set.image2` gives the same real supremum, and a freshly verified expanded map uses `AddMonoidAlgebra.infDegree`. The documented Greek name remains useful as a project-local semantic alias; no new generic supremum primitive should be added upstream.

## Phase 0 — Doctor

Canonical181 is the public noncomputable definition at `Roth/Theta.lean:68`. The entire985-line [Theta module](../evidence/Roth.Θ/source-Theta.lean.txt) and762-line [MainLemma module](../evidence/Roth.Θ/source-MainLemma.lean.txt) were read, together with the relevant [Index](../evidence/Roth.Θ/source-Index.lean.txt), [Box](../evidence/Roth.Θ/source-Box.lean.txt) and all exact source callers. The module develops index families and Lemmas5–7, subsequently used to produce the auxiliary polynomial in the main lemma.

The successful2467-job [baseline](../evidence/Roth.Θ/baseline-build.txt) is reused after fresh equality of all17 source/pin hashes: [fresh hashes](../evidence/Roth.Θ/source-hashes.json), [shared input manifest](../evidence/Roth.Θ/input-manifest.json). Native original type/body/axioms and exact ordered293-name kernel audit are in [original source](../evidence/Roth.Θ/theta181-original-executed.lean.txt), [receipt](../evidence/Roth.Θ/theta181-original-receipt.json), and [standalone audit source](../evidence/Roth.Θ/theta181-audit-executed.lean.txt). There is no sorry or printer elision. Production sources, pins and Git are unchanged.

## Phase 1 — Comprehend

For a finite variable type σ, Θ is the real supremum of the weighted indices of all nonzero integer polynomials with individual degrees bounded by r and every coefficient absolute value bounded by B, evaluated at all coordinatewise h/q with h coprime to q. Both the polynomial and numerator vector vary independently. The definition is total even outside the manuscript's positive parameter range; theorem hypotheses are supplied when interpreting the supremum as a least upper bound.

Full native type:

```lean
@Roth.Θ : {σ : Type u_1} → [Fintype σ] →
  ℝ → (σ → ℕ) → (σ → ℕ) → ℝ
```

The exact body is `fun B q r ↦ sSup (indexSet B q r)`. σ is universe-polymorphic. Fintype comes from indexSet/index/weight, and DecidableEq is absent. B, q and r are data, with no B≥1, q>0 or r>0 hypotheses captured. The coefficient bound, nonzero condition, coordinate degree bounds and reduced numerator predicate are all retained. Real `sSup ∅ = 0` and unbounded real suprema also evaluate to0; an extended-real supremum would change those totalization conventions. For this particular family boundedness is proved separately by indexSet_bddAbove.

## Phase 2 — Preliminary checks

BIG: Θ is the named central quantity of Lemmas5–7 and the bridge into the main lemma. Definition-only body count is1 substantive line: ONE-LINER.

| Exemption | Applies? | Evidence |
|---|---|---|
| Avoid defeq abuse | no | Exact literal and image2 supremum equations are rfl. There is no opaque unfolding barrier needed by source consumers. |
| Avoid typeclass diamonds | no | A real-valued definition installs no instance or alternate order operation. |
| Semantic intent / API stability | yes | lem6Φ, Θ_lt and main_lemma benefit from a compact name for the same arithmetic family supremum. There are19 explicit consumer declarations, including3 in MainLemma. |

ONE-LINER WITH-EXEMPTION. A stable local name is justified; it does not automatically justify a separate upstream primitive.

## Phase 3 — Exhaustive literature

Actual requests, returned-response digests/bytes, sanitized URLs/titles and original concise summaries are in [general queries](../evidence/Roth.Θ/web-0.json), [nLab/nCatLab/Stacks](../evidence/Roth.Θ/web-1.json), [MO/recent arXiv](../evidence/Roth.Θ/web-2.json), [direct primary access](../evidence/Roth.Θ/web-primary.json), [local query](../evidence/Roth.Θ/local-literature.json) and [local §5 excerpt](../evidence/Roth.Θ/clean-theta-excerpt.tex.txt). Full external bodies are not archived.

| Channel | Actual query / locator | Result |
|---|---|---|
| General web, specific | `Roth theorem Theta supremum index bounded polynomials denominators` | Exact Θ family appears in *An Invitation to Modern Number Theory*, §6.4.4; indexed excerpt read. Local manuscript supplies the authoritative exact input conjunction. |
| General web, general | `supremum weighted order vanishing polynomial Roth index` | [Princeton lecture17.1.1](https://web.math.princeton.edu/mathlab/jr02/diophantine.pdf) gives weighted polynomial index via first nonzero normalized derivative; direct PDF fetch timed out. Search excerpt inspected only. |
| General web, aliases | `Thue Siegel Roth auxiliary polynomial index maximum theta` | Roth's index theorem and auxiliary polynomial argument; no equivalence between an arbitrary maximum and a real supremum inferred. Additive-combinatorial Roth and theta-function hits rejected. |
| ChatGPT mathematical MCP | Standard form, generality and historical evolution | n/a: ask_chatgpt_math unavailable. No answer fabricated. |
| Local references | clean.tex §5 lines644–670 | Exact supremum over ℛ and coprime integer numerators. Source assumes m≥1, B≥1 and positive q,r, and proves nonempty/boundedness. Lean definition deliberately omits those premises. |
| nLab | `site:ncatlab.org/nlab supremum least upper bound` | [Join, Definition](https://ncatlab.org/nlab/show/join) describes least upper bounds and arbitrary joins. Indexed material read; direct open failed with unsupported XHTML. Supports the general order concept, not a named arithmetic Θ. |
| nCatLab | `site:ncatlab.org/ncatlab supremum order` | Returned off-namespace nLab material. No exact nCatLab hit or categorical Θ replacement found; not an absence proof. |
| Stacks | `site:stacks.math.columbia.edu order vanishing polynomial` | [Tag02MB, Definition10.121.2](https://stacks.math.columbia.edu/tag/02MB) directly read: local one-dimensional Noetherian order via lengths. Adjacent concept, not this weighted-index family supremum. |
| MathOverflow | `site:mathoverflow.net Roth theorem index polynomial supremum` | [Question431381](https://mathoverflow.net/questions/431381/dysons-lemma-implies-index-is-small-in-proving-roths-theorem) concerns small index in Roth's proof; other answers concern quantitative/effective Roth. Secondary context only. |
| Recent arXiv,2021-10-27–2026-10-27 | `site:arxiv.org Roth theorem polynomial index after:2021-10-27 before:2026-10-28` | Returned additive-combinatorial papers (rejected) and weighted-projective Roth work, not the exact Θ. Supplementary direct [Goel–Lunia–Ray2502.00731](https://arxiv.org/abs/2502.00731), submitted2025-02-02, revised2026-07-21, abstract describes a classical Roth/subspace exposition. No full-paper equivalence claimed. |

Standard form: supremum of weighted indices over degree/height constrained integer polynomials and reduced rational points with prescribed denominators. The underlying order operation is the general supremum of a set; positive source hypotheses ensure its usual meaning. Broader geometric heights, coefficient rings and weight conventions require separate arithmetic models. No single universal Θ family beyond that application is asserted. The general join literature explains why a supremum is structural rather than a new numerical primitive, while its empty/unbounded convention must be checked against Lean.

## Phase 4a — Every parameter and hypothesis

| Item | Role | Generality analysis |
|---|---|---|
| σ : Type u | common coordinate type | Already arbitrary finite type/universe, including empty type, while source assumes positive dimension. SupSet itself permits any target universe. |
| Fintype σ | current parent index uses global finite weight sum | Needed by unchanged indexSet signature. A separately verified expanded infDegree/Finsupp.weight expression defines the same finite specialization without Fintype; this is a representation change, not silently dropping a parent parameter. |
| B : ℝ | bounds every coefficient's absolute value | Any B allowed. B<0 yields empty indexSet and Θ=0, actually tested. Dropping B changes the arithmetic family. |
| q : σ→ℕ | fixed denominators, also cast to ℤ for coprimality | No positivity captured. Zero denominators retain total division and the original IsCoprime predicate; do not replace by unrestricted real centers. |
| r : σ→ℕ | degree cap and reciprocal weight | Zero coordinates allowed, including all0. Splitting bounds from weights would expand an interface, not eliminate an unused argument. |
| Integer coefficients/numerators | integrality and reduced-fraction constraint | Changing to a general coefficient field or projective height changes the family; no mechanical arithmetic generalization claimed. |
| Real output | conditional supremum, with empty/unbounded value0 | Generic outer specialization only requires SupSet. Order laws require conditional completeness/nonempty/boundedness as appropriate. Replacing ℝ by extended reals without a bridge changes totalized values. |

## Phase 4b — Generality verdict

MAXIMALLY GENERAL within fixed indexSet/index interfaces: there is no unused captured argument or positivity premise to remove. The outer operation independently generalizes to `{V : Type w} [SupSet V] (s : Set V) : V := SupSet.sSup s`, which already exists. Fresh expanded arbitrary_variables has arbitrary σ without Fintype and an exact compiled finite specialization. That normalization proves an alternate representation, not that downstream arithmetic bounds hold for arbitrary maps or infinite variables. No YES-but-generalise-first claim is made from an uncompiled weakening.

## Phase 4c — Nine modern-idiom questions

| # | Question | Answer / concrete downstream consequence |
|---|---|---|
| 1 | Preambles to typeclasses | No new class. Fintype is already inherited; SupSet/conditional completeness already supply the order operation/laws. |
| 2 | Sequences to filters | No sequence, convergence or topology in the definition. |
| 3 | Construction to universal property | IsLUB characterizes a supremum for nonempty bounded families; existing isLUB_csSup/Real.isLUB_sSup handle it. Replacing the total function by an IsLUB subtype would require hypotheses and change the interface. |
| 4 | Predicate to bundled substructure | Full RSet excludes0 and has bounded coefficients; it is not a submodule. The index family need not be a sublattice. No closure bundle applies. |
| 5 | Field-specific hierarchy weakening | Outer sSup needs only SupSet, already abstract in mathlib. The map/input sets carry arithmetic structure separately. |
| 6 | Higher categorical formulation | No categorical data/laws. General joins are poset colimits, but adding categorical machinery enables no needed consumer. |
| 7 | Concrete indices/order structure | Existing generic sSup works over arbitrary target universes. Finite support infDegree gives an infinite-variable representation while preserving finite specializations. |
| 8 | Concrete-via-abstract diagnostic | Body contains Θ0times and indexSet1time. After naming the set input, only sSup remains: exact SupSet.sSup specialization. le_csSup, csSup_le, csSup_le_csSup and Real.sSup_nonneg give actual member/upper/monotone/sign APIs. |
| 9 | False-generalization guard | Preserve full nonzero/degree/coefficient conjunction, coprime numerators, total q/r zeros, and untopD0. Reject complete-lattice sSup_image2 directly on ℝ: ℝ is conditionally complete and has no CompleteLattice instance. Reject max without attainment proof and extended-real values without projection. |

Modern idiom available, already in mathlib: use the existing supremum operation and its conditional-order laws. The exact specialized term is one outer constructor call. `sSup_image2` is a useful search hit for complete lattices but is explicitly rejected as an unconditional real replacement; `csSup_image` has boundedness and an empty-supremum lower-bound premise. Native generic member/upper proofs use the valid real API instead.

## Phase 4.5 — Six infrastructure risks

| Risk | Level | Actual evidence / interpretation |
|---|---|---|
| Typeclass diamond | none observed | Θ installs no class or instance. Native SupSet ℝ synthesis chooses the existing real order operator; Fintype is a parameter, not another instance path. |
| Reducibility leak | low | Ordinary semireducible noncomputable def with rfl RHS equality, no reducible attribute or new computational reduction rule. |
| Noncanonical unfolding | low | no_automatic_unfold first checks simp only cannot close the equation, then rfl succeeds. Explicit unfolding is intentional; representation changes need bridges. |
| Instance priority collision | none | No instance/priority/search rule registered. Existing SupSet synthesis does not depend on a new priority. |
| Universe polymorphism | none observed | Full Type u native signature and actual ULift universe1 probe elaborate. Expanded variable type is independently universe-polymorphic. |
| Coercion ambiguity | none observed | Real-valued output has ordinary equality/order and application. No CoeFun/CoeSort introduced; native negative function-coercion probe checks it does not masquerade as a function. Explicit casts fix numerator/denominator types in expanded maps. |

Overall LOW, no HIGH row. This is not an infrastructure objection to a local name; the upstream question is redundancy of the outer construction.

## Phase 4.6 — Five proof-strategy questions

| # | Check | Answer / alternative |
|---|---|---|
| 1 | ε–δ vs filters | No proof or topology. |
| 2 | Element algebra vs inclusions | Existing sSup and image2 pointwise-bound interfaces avoid rebuilding bounded existential reasoning; polynomial arithmetic remains substantive. |
| 3 | Sequences vs nets | No convergence. |
| 4 | Explicit categorical construction vs universal property | Existing conditional IsLUB API is enough; do not replace a total real quantity by a new universal-property class. |
| 5 | Missing helper API | Supremum member, upper-bound and monotonicity API already exist. The finite-support infDegree projection bridge is new normalization glue, not an existing mathlib point-index result. |

MATHLIB-IDIOMATIC for the local one-line definition. Upstream use should reuse SupSet.sSup, with map normalization separate. No cost/performance rationale enters the verdict.

## Phase 5 — Fifteen actual formal search cells

All requests and complete raw responses are retained; external indices may differ from the pin. Local index was unavailable, so empty/heuristic results are not absence proofs. Positive source/signature checks use this pin: [mathlib input inventory](../evidence/Roth.Θ/mathlib-inputs.json).

| Form | Finder | Loogle | LeanSearch | rg | Local |
|---|---|---|---|---|---|
| Current bounded polynomial index supremum | [receipt](../evidence/Roth.Θ/search-current-finder.json): unrelated Chevalley bounds | [receipt](../evidence/Roth.Θ/search-current-loogle.json): Real.sSup_empty/isLUB/unbounded | [receipt](../evidence/Roth.Θ/search-current-leansearch.json): iSup and adjacent arithmetic bounds | [receipt](../evidence/Roth.Θ/rg-current.json): no exact project name in pin | [receipt](../evidence/Roth.Θ/search-current-local.json): empty, index unavailable |
| Standard supremum over two constrained choices | [receipt](../evidence/Roth.Θ/search-standard-finder.json): sSup_image2 | [receipt](../evidence/Roth.Θ/search-standard-loogle.json): sSup_image2/GaloisConnection laws | [receipt](../evidence/Roth.Θ/search-standard-leansearch.json): complete-lattice sSup_image2 | [receipt](../evidence/Roth.Θ/rg-standard.json): complete/conditional supremum-image laws, real zero convention | [receipt](../evidence/Roth.Θ/search-standard-local.json): csSup_image family, index unavailable |
| Abstract set supremum constructor | [receipt](../evidence/Roth.Θ/search-abstract-finder.json): sSup_image2 plus unrelated setwise joins | [receipt](../evidence/Roth.Θ/search-abstract-loogle.json): exact SupSet.sSup | [receipt](../evidence/Roth.Θ/search-abstract-leansearch.json): csSup_le and conditional LUB laws | [receipt](../evidence/Roth.Θ/rg-abstract.json): exact SupSet class/field and conditional laws | [receipt](../evidence/Roth.Θ/search-abstract-local.json): Real.sSup definitions/laws among heuristic hits |

Concluded: found in mathlib as **SupSet.sSup**, more general outer operation. Pinned `Mathlib/Order/SetNotation.lean:44–46` defines the class/field and exports sSup; real implementation/zero conventions are in `Mathlib/Algebra/Order/Archimedean/Real/Basic.lean`. The family itself is re-aimed to existing Set.image2 with the full arithmetic map, and separately expanded to infDegree; none of RSet, indexSet or index is falsely counted as a mathlib declaration.

## Phase 5.5 — Statement shape

Normal forms compared: literal sSup(indexSet); sSup(image2 exactmap fullRSet coprimeNumerators); expanded sSup(image2 infDegree/aeval map); and indexed suprema. The first two agree definitionally; the expanded one needs finite minimum/support normalization. The canonical outer operation is sSup. Generic complete-lattice indexed supremum rewriting is not valid automatically for real totalized inputs. Equivalence statements place the selected existing form on the RHS.

Syntactic generality: retain the short local Greek name for long arithmetic formulas, or inline `sSup (indexSet B q r)` mechanically at callers. Moving the family into two subtype binders adds coercions; it does not remove the conditional-order premises. Actual source proof experiments and expanded finite specialization check the alternatives.

Superfluous arguments: NONE. σ/Fintype belong to the current parent signature; B,q,r all determine the family. DecidableEq and positivity are already absent. Expanded representation removes Fintype only after changing the parent map representation. SHIP-AS-STATED locally; RESTATE-BEFORE-SHIP for a generic upstream proposal, because SupSet.sSup already exists.

## Phase 6.0 — Complete callers and inline audit

Fresh [scoped rg](../evidence/Roth.Θ/callers.json), [tracked git grep](../evidence/Roth.Θ/git-callers.json), and comment-stripped exact-identifier [structured occurrences](../evidence/Roth.Θ/callers-structured.json) agree. There are **28 standalone code occurrences across19 consumer declarations**:25 in16 same-file callers and3 in3 MainLemma callers. The command's outside-declaring-file internal use count K is3, in1 file. Θ_substring helper names and documentation are excluded. Native canonical293 audit separately finds13 direct kernel-value consumers and17 direct type consumers; neither is lexical counts or full transitive/simp closure.

Every row below uses the mechanically exact replacement `Θ B q r ↦ sSup (indexSet B q r)`; parent arguments remain unchanged. If indexSet is simultaneously eliminated, substitute the full image2 term from Phase6 after that first step.

| Explicit caller | Exact lines / occurrences | Concrete refactor plan |
|---|---|---|
| index_le_Θ | Theta:101,1 | Replace upper endpoint; retain le_csSup/indexSet_bddAbove and exact membership witness. Full proof replay tested. |
| Θ_nonneg | Theta:107,1 | Replace endpoint; Real.sSup_nonneg and index_nonneg remain the proof. Full proof replay tested. |
| Θ_le_card | Theta:114,1 | Replace left endpoint; retain Real.sSup_le, nonzero map and coordinate-degree/cardinality bound. |
| Θ_le_of_forall_index_le | Theta:126,1 | Replace left endpoint; retain nonempty premise and csSup_le. Full proof replay tested. |
| Θ_mono | Theta:135,2 | Replace both endpoints; retain csSup_le_csSup, nonempty and family inclusion proof. |
| Θ_equiv | Theta:160,2 | Replace both endpoints; congrArg sSup and exact family transport remain valid. |
| Θ_unique_le | Theta:257,1 | Replace left endpoint; keep quantified individual-index logarithm proof and Θ_le_of_forall_index_le call until separately refactored. |
| lem6Φ | Theta:276,2 | Replace both terms in sum by corresponding sSup/indexSet; exact definition equation tested. |
| Θ_option_le | Theta:596,1 | Replace left endpoint; retain individual-index Lemma6 and finite maximum bound. |
| private theta_scaled_unique_le_aux | Theta:744,1 | Replace conclusion endpoint; Θ_mono/Θ_unique_le statements are definitionally compatible; logarithmic arithmetic unchanged. |
| private theta_prefix_lt_aux | Theta:787–788,2 | Replace induction hypothesis and conclusion supremum with their own B/q/r arguments; preserve scaled prefix arithmetic. |
| private theta_lt_base_aux | Theta:820–821,2 | Replace conclusion and local intermediate endpoint; retain unique-variable logarithm bound. |
| private theta_phi_lt_aux | Theta:851,854–855,3 | Replace induction hypothesis and both local Φ components; retain numerical Φ bound and scaled/prefix comparison. |
| private theta_lt_succ_aux | Theta:901–902,2 | Replace induction hypothesis/conclusion; Θ_equiv/Θ_option_le theorem applications still elaborate by transparency, unless independently rewritten. |
| private theta_lt_of_large_delta_aux | Theta:934,938,2 | Replace conclusion and calc first expression; keep Θ_le_card and numeric domination. |
| Θ_lt | Theta:966,1 | Replace conclusion; induction helper statements remain definitionally compatible. |
| private theta_lt_eta_of_sq_log_bound_aux | MainLemma:676,1 | Replace conclusion; retain Θ_lt application plus eta/log/ratio normalization. Entire source proof replay tested. |
| private exists_auxiliary_polynomial_with_index_gap_aux | MainLemma:699,1 | Replace supremum inside index gap; hγ and theta_lt_eta comparison remain the same real inequality. |
| main_lemma | MainLemma:750,1 | Replace supremum in local midpoint c; retain gap and index_le_Θ to compare the chosen polynomial's index. |

[Inline audit](../evidence/Roth.Θ/inline-audit.json) finds the actual sSup definition plus generic source bound proofs; no independent arithmetic Θ implementation was found. The live alias is not junk. A call to Θ_lt is not an extra explicit Θ term, even though its elaborated theorem type contains Θ.

## Phase 6 — Actual composition and re-aim experiments

The literal existing operation is one application:

```lean
sSup (indexSet B q r)
```

The parent-family re-aim gives the exact same real expression:

```lean
sSup (Set.image2
  (fun R h ↦ index (map (Int.castRingHom ℝ) R) (fun j ↦ (h j : ℝ) / q j) r)
  (RSet B r) {h : σ → ℤ | ∀ j, IsCoprime (h j) (q j : ℤ)})
```

The fully expanded map form, preserving the complete RSet input, is:

```lean
sSup (Set.image2 (fun R (h : σ → ℤ) ↦
  (AddMonoidAlgebra.infDegree
    (fun d : σ →₀ ℕ ↦
      (Finsupp.weight (R := ℕ) (fun j ↦ (r j : ℝ)⁻¹) d : WithTop ℝ))
    (aeval (fun j ↦ X j + C ((h j : ℝ) / q j))
      (map (Int.castRingHom ℝ) R))).untopD 0)
  {R : MvPolynomial σ ℤ | R ≠ 0 ∧ (∀ j, degreeOf j R ≤ r j) ∧
    ∀ d, |((R.coeff d : ℤ) : ℝ)| ≤ B}
  {h : σ → ℤ | ∀ j, IsCoprime (h j) (q j : ℤ)})
```

Fresh native literal/image2 equations are rfl. After replacing the inner index by the independently rechecked infDegree/Finsupp.weight/aeval map, congrArg sSup transports the exact all-input equality. The expanded expression is archived with full source and is not described as definitionally equal to the old index. It includes the entire RSet and coprime-numerator family and the explicit untopD0 projection. The finite-support empty/nonempty split, Finset.coe_inf', Finset.inf'_eq_csInf_image, Finsupp.weight_eq_sum and MvPolynomial.finsupp_support_eq_support are genuine normalization glue; they are not preexisting mathlib point-index calls.

[Accepted probes](../evidence/Roth.Θ/theta181-probes-executed.lean.txt), [generality](../evidence/Roth.Θ/theta181-generality-executed.lean.txt), [caller source replays](../evidence/Roth.Θ/theta181-callers-executed.lean.txt), and [isolated mathlib-only source](../evidence/Roth.Θ/theta181-isolated-executed.lean.txt) are linked to complete raw receipts in [verification](../evidence/Roth.Θ/verification.json). The isolated source guards Roth.Θ as absent and checks generic SupSet.sSup specialization, valid real image2 membership/upper-bound laws, real empty/unbounded conventions and absence of a CompleteLattice ℝ instance. Actual expanded no-Fintype construction and finite specialization compile; negative B yields Θ=0, and q/r zero inputs retain total conventions.

Composition conclusion: exact specialization of existing SupSet.sSup;1 outer existing call. With an ordinary image2 family, there are2 outer structural operations. The full arithmetic map construction has more operations and a genuine normalization proof, so it is not counted as a ≤3-call fully expanded proof. No closing `simp [defs]` is the basis of the verdict; Phase6b's trivial-simp caution is respected. Existing constructor identification is a positive hit. The ModeB re-aim gate is checked independently, not inherited from indexSet180 or index133; complete-lattice-only search hits are not used to smuggle in invalid real laws.

## Phase 7 — Verdict and actionable disposition

**NO-mathlib-has-it.** `SupSet.sSup` already is exactly the operation performed by Θ. The native equality `Θ B q r = SupSet.sSup (indexSet B q r)` is rfl for all inputs, with no extra hypotheses or changed conventions. Existing conditional-order API supplies member bounds, upper bounds, monotonicity and nonnegativity. The independently normalized parent re-aim yields the same sSup of a full image2 map, rather than a novel generic operation. The verdict does not assert that mathlib has a named Roth Θ family or that the inner arithmetic results are trivial.

Retain `Roth.Θ` in `Roth/Theta.lean` as the documented semantic alias. This is the natural alternative local destination: it names the quantity threaded through the proof and the literature. There is no upstream definition PR for a parallel supremum primitive. If local policy instead removes the alias, update all28 exact occurrences at the19 table rows to `sSup (indexSet B q r)` with the displayed arguments, then update docstrings; helper names need separate assessment rather than substring replacement. The tested source replays cover direct member/nonneg/upper laws, two-term lem6Φ and the external main-lemma eta comparison. Keep nonempty/boundedness proof obligations and all arithmetic inputs. Neither cost nor prior verdict inheritance drives this conclusion.

## Phase 8 — Completion and limitations

All required phases, all15 formal search cells and every named literature channel are complete. Future design work for a broader arithmetic height/index API is independent of this positive existing-constructor assessment. The first universe data example needed noncomputable, and the first MainLemma eta replay needed explicit `simpa [eta, Θ]`; both rejected receipts are archived separately from the clean final executions. That closing simp is caller normalization, not the basis of the constructor verdict. Verification unresolved is empty; external fetch/index limitations and rejected native attempts are recorded honestly. [Assessment](../evidence/Roth.Θ/assessment.json), [verification](../evidence/Roth.Θ/verification.json), [overview entry](../evidence/Roth.Θ/overview-entry.json), [copy manifest](../evidence/Roth.Θ/copy-manifest.json), [portable validator](../evidence/Roth.Θ/validate.py). Root acceptance remains pending until independent review. No production or pin changes are proposed in this read-only assessment.
