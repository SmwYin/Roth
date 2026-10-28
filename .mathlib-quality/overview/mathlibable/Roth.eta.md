# Roth.eta — canonical231

Verdict: **BORDERLINE-needs-human**. Completed read-only assessment; root acceptance pending. The two final questions concern future upstream API design, not unfinished verification or a current user blocker. No production Lean, pins, Git, overview or progress edited.

## Phase 0 — Baseline and resolution

`Roth/MainLemma.lean:66`, public noncomputable definition, resolves natively. All 17 production source/pin hashes freshly match the shared clean 2467-job build. Canonical228 Theta endpoint build was already root accepted;231 is not an endpoint, next266. No new full build is required. Whole MainLemma and Main read; exact source archives retained. MainLemma constructs Roth's auxiliary polynomial by pigeonhole, high index and a low-order nonvanishing Hasse derivative.

Evidence: [inputs.json](../evidence/Roth.eta/inputs.json); [baseline-build.txt](../evidence/Roth.eta/baseline-build.txt); [target-metadata.json](../evidence/Roth.eta/target-metadata.json); [original-receipt.json](../evidence/Roth.eta/original-receipt.json); [native-type.json](../evidence/Roth.eta/native-type.json).

## Phase 1 — Comprehension

Eta is the chosen small-index error η(δ,m)=10^m δ^((1/2)^m). For nonnegative δ this is ten to dimension times an m-fold principal square root; the root bridge below was actually proved. This error bounds the rational-point index in Lemma 7, and subtracting it from the large algebraic-point index γ leaves the gap used in Lemma 9. It differs from λ, the square-root-in-dimension loss in a counting threshold, and γ=(m−λ)/2, the large-index cutoff.

Full native Lean type, extracted by Lean.getConstInfo with pp.funBinderTypes:

```lean
Roth.eta : ℝ → ℕ → ℝ
-- binders: (δ : ℝ) → (m : ℕ) → ℝ
noncomputable def eta (δ : ℝ) (m : ℕ) : ℝ := 10 ^ m * δ ^ ((1 / 2 : ℝ) ^ m)
```

Parameters: δ arbitrary real approximation parameter; m natural dimension. Hypotheses: none. Conclusion: a real number, not a proposition. Source-level project dependencies: []. Full pp.all kernel body and axioms are in [native-type.json](../evidence/Roth.eta/native-type.json); no printer-elision marker. Incidental generated numeral-instance proofs `Roth.eta._proof_1` and `Roth.gam._proof_1` appear in the kernel printer; these do not turn the arithmetic definition into a mathematical use of the public gamma function.

Important totalization: m=0 gives eta δ 0 = δ, and eta 0 m = 0 for all m. For δ<0 the power uses exp(log δ·e)cos(eπ), e=(1/2)^m, not an unrestricted iterated principal-root convention. [project-receipt.json](../evidence/Roth.eta/project-receipt.json) proves these laws and the negative-base formula. In particular eta(−1,0)=−1 rules out replacing the full real interface by a nonnegative-real interface without a domain restriction.

## Phase 2 — Preliminary checks

SMALL: this is a numerical parameter definition, not a new structure or the main theorem. Literature width remains exhaustive.

One substantive body line: ONE-LINER WITH-EXEMPTION.

| Exemption | Applies | Evidence |
|---|---|---|
| Avoid defeq abuse | no | Full caller inlining preserves every original signature; no required sealing barrier identified. |
| Avoid typeclass diamonds | no | Returns existing ℝ; introduces no instance, class, coercion or alternate structure. |
| Semantic intent / API stability | yes | exists_delta_bound, exists_delta and main_lemma use eta to carry one error bound through parameter choice and the gap γ−η; eight caller declarations. |

An API exemption is not sufficient for a YES verdict. Its public versus local status remains the final design question.

## Phase 3 — Exhaustive literature

All named channels were actually queried; optional ask_chatgpt_math unavailable, justified n/a. Exact requests, response SHA256/UTF8 bytes, returned status and clean titles/URLs are archived; only original concise summaries are retained, no article/search-result bodies. The successful metadata transport follows an initial rejected serialization command that wrote no artifact.

| Channel | Exact query or locator | Finding and limit | Evidence |
|---|---|---|---|
| General specific | Roth main lemma eta "10" "delta" auxiliary polynomial index | Exact parameter family surfaced alongside unrelated eta-functions. | [web-general.json](../evidence/Roth.eta/web-general.json) |
| General wider | Roth lemma 7 index bound iterated square root delta power dimension | Classical index bounds have dyadic exponents; constants/parameterization vary. | [web-general.json](../evidence/Roth.eta/web-general.json) |
| General aliases | Roth theorem Dyson lemma quantitative index small parameter eta | Dyson alternatives and number-field formulations; no universal name for fixed 10 eta. | [web-general.json](../evidence/Roth.eta/web-general.json) |
| ChatGPT math | n/a | ask_chatgpt_math unavailable; no other channel reduced. | This row |
| Local clean.tex | §5 Lemma 7; §6 eq(36), eq(38), Lemma 9 | Exact eta is defined in eq(36), following earlier displayed small-index estimate. | [local-literature.json](../evidence/Roth.eta/local-literature.json); [local-excerpt.tex.txt](../evidence/Roth.eta/local-excerpt.tex.txt) |
| nLab | site:ncatlab.org/nlab Roth theorem Diophantine approximation iterated square root | Principal real square root and Vojta/number-theory context; no exact eta definition. | [nlab.json](../evidence/Roth.eta/nlab.json) |
| Distinct nCatLab | site:ncatlab.org/ncatlab Roth theorem index auxiliary polynomial | Search returned /nlab analytic-index pages outside requested namespace; no categorical eta counterpart established. | [ncatlab.json](../evidence/Roth.eta/ncatlab.json) |
| Stacks | site:stacks.math.columbia.edu Roth theorem index estimates | Trace/index/algebra documents returned; not a fixed Roth numerical-envelope API. | [stacks.json](../evidence/Roth.eta/stacks.json) |
| MathOverflow | site:mathoverflow.net Roth lemma small index eta | Q431381 asks how Dyson volume estimates imply small index. Context, not proof of this formula or canonicality. | [mathoverflow.json](../evidence/Roth.eta/mathoverflow.json) |
| Recent arXiv | site:arxiv.org Roth theorem Diophantine approximation index after:2021-10-28 before:2026-10-29 | Goel–Lunia–Ray2502.00731 is relevant; characteristic-p paper is a semantic guard; additive/physics hits rejected. | [arxiv.json](../evidence/Roth.eta/arxiv.json) |
| Primary followup | Goel–Lunia–Ray v2 Lemma3.9; Gao §3.4 Lemma3.4.1 p52, §3.5 | These choose small free parameters / different constants; they do not define the exact universal fixed 10 eta. | [primary.json](../evidence/Roth.eta/primary.json); [primary-locators.json](../evidence/Roth.eta/primary-locators.json) |
| Mathlib web API | mathlib4 real rpow iterated sqrt Roth eta parameter | Official real-power docs agree with pinned negative-base convention; CFC operator powers are a different domain. | [web-api.json](../evidence/Roth.eta/web-api.json) |

Primary sources: [Goel–Lunia–Ray, Diophantine approximation and the subspace theorem](https://arxiv.org/html/2502.00731v2), Lemma3.9 (v2 dated21 July2026); [Gao, An Introduction to Diophantine Geometry](https://ziyangjeremygao.github.io/LectureNotes/DiophantineGeometry.pdf), §3.4, printed p52 and §3.5. The local source exactly identifies eq(36). Gao's index estimate is a different constant/exponent normalization, not an equality to eta. The arXiv paper's free eta is also not this defined eta. These are independently checked mathematical distinctions, not inherited verdicts.

Summary: standard concept is a small-index error bound obtained by dimension induction, with dyadic exponents. Exact numerical constants are proof choices. Current form matches local §6 perfectly; no uniquely most-general standard named numerical object emerged. This supports a semantic API question, not a search-based global absence claim.

## Phase 4a — Generality

| Parameter / choice | Current | Wider candidate | Verified result / semantic limit |
|---|---|---|---|
| δ | ℝ, no hypotheses | NNReal domain | typedBridge compiles, but is restriction/representation; negativeGuard refutes unrestricted replacement. |
| m | ℕ including0 | Real dimension | Not a dimension in polynomial induction anymore; no natural-index assumption to drop. |
| Target ℝ | Real.rpow | Generic Pow carrier / CFC | Arbitrary Pow does not express analytic roots; CFC concerns positive operators. False semantic widening rejected. |
| Fixed10 | constant factor10^m | C^m | New generic formula compiles; changing C does not retain the proven Θ estimate automatically. |
| Fixedhalf | (1/2)^m | b^m | New formula compiles; for continuity require nonnegative exponent (proved with b≥0), for zero law b>0. No arbitrary-b claim. |
| Signs/nonzero/instances | none | remove hypotheses | There are none to remove. No unused binder. |

Compiled new representation:

```lean
noncomputable def formula (C b δ : ℝ) (m : ℕ) : ℝ := C ^ m * δ ^ (b ^ m)
```

[isolated-receipt.json](../evidence/Roth.eta/isolated-receipt.json) establishes formula10half equals the direct arithmetic expression, root interpretation for δ≥0, zero/dimension 0/positive laws and NNReal bridge. These are **new scratch definitions/proofs**, not existing mathlib counterparts. [project-receipt.json](../evidence/Roth.eta/project-receipt.json) gives the rfl bridge to actual eta and continuity from existing real-power API.

## Phase 4b — Generality verdict

MAXIMALLY GENERAL relative to the literal numerical object: zero hypothesis/typeclass weakening opportunities. Constants and codomain can be parameterized as representation experiments, but literature does not identify the new arbitrary-C,b function as the standard semantic error bound. No YES-but-generalise-first claim is made. A future arbitrary admissible error bound in the main-lemma API is a larger semantic design choice; the defining arithmetic alone does not prove that theorem for arbitrary error.

## Phase 4c — Modern idiom

| # | Question | Applies / consequence |
|---|---|---|
| 1 | Typeclasses instead of preambles | no; no bundled mathematical hypotheses or structures to replace. |
| 2 | Filters instead of metric/sequence form | no at definition; continuity proof already uses standard Continuous / ContinuousAt and composes in parameter selection. |
| 3 | Universal property instead of construction | no; this is a selected scalar formula, no universal characterization. |
| 4 | Bundled substructure | no; NNReal representation is possible on nonnegative δ but is no substructure construction. |
| 5 | Weaken field/module hierarchy | no established semantic weakening; arbitrary Pow is only a formal spelling with no analytic law. |
| 6 | Higher category | no; numerical bound has no categorical content. |
| 7 | Generalize concrete index | no semantic replacement; m counts variables and supports natural induction. Real m would change that role. |
| 8 | Concrete-via-abstract diagnostic | Explicitly checked: eta body contains zero eta references, no unfolding-proof tail; it is directly arithmetic. New C,b profile compiles, but no concrete-result proof becomes an existing generic theorem. Theta induction actually uses10 andhalf numerically in lem7_numeric. |
| 9 | False-generalization guard | Reject unconditional NNReal/iterated-root replacement on all δ and arbitrary-C,b substitution in Θ theorem. Verified bridges state domain/parameter restrictions. |

Modern idiom available: no demonstrated new abstraction with independent library consequences. Useful local companion API is continuity and zero evaluation. Typed representation can simplify nonnegativity goals but does not create an existing library eta or automatically justify an upstream definition.

## Phase 4.5 — Infrastructure risks

| Risk | Verdict | Evidence |
|---|---|---|
| Typeclass diamond | none | Ordinary real-valued function; no class/instance created; real power/natural power inferred by explicit exponent types. |
| Reducibility leak | low | rfl bridge succeeds for semireducible def; body is small arithmetic, no reducible attribute. |
| Noncanonical unfolding | low | Ordinary multiplication/power; zero arguments simplify after explicit unfold. No simp attribute on eta; semantic name controls exposure. |
| Instance priority collision | none | Not an instance; no priority or alternate structure registered. |
| Universe issue | none | Native universe parameter list[]; fixed ℝ/ℕ, no hidden polymorphic carrier. |
| Coercion ambiguity | none | Fixed real output; failed fully typed CoeFunℝ probe confirms it is a scalar, not a competing bundled map. NNReal bridge explicitly coerces. |

Overall LOW; no HIGH row. Actual rfl/universe/typed-coercion probes in [project-receipt.json](../evidence/Roth.eta/project-receipt.json)/[isolated-receipt.json](../evidence/Roth.eta/isolated-receipt.json). Class synthesis of eta itself would be ill-typed, so not misreported as a diamond test.

## Phase 4.6 — Proof strategy

| # | Question | Answer / alternative |
|---|---|---|
| 1 | Topology ε–δ versus filters | no proof in def; surrounding continuity uses existing topology API. etaContinuous compiles and could shorten the two continuity arguments locally. |
| 2 | Element algebra versus subobjects | no; scalar expression is not an ideal/submodule inclusion. |
| 3 | Sequences versus nets | no; scalar power construction, no limiting sequence. |
| 4 | Construction versus universal property | no; no categorical object. |
| 5 | Missing helpers mathlib should have | no arithmetic gap established. New rootIter_eq is induction using rpow_mul/sqrt_eq_rpow, not an existing-call replacement; a generic iteration lemma would need its own assessment. |

MATHLIB-IDIOMATIC construction. Existing Continuous/rpow APIs already handle analytic companions; no cost-based verdict or compulsory refactor.

## Phase 5 — All 15 mathlib search cells

Three genuinely distinct forms, five actual methods each. External index results may not match the pinned revision. Local index reported error, though source matches were returned; this cannot establish absence. Full raw formal-tool responses retained. Every positive building block used in accepted proofs was checked under the pin. Empty search is not proof of global absence.

| Form | Finder | Loogle | LeanSearch | rg | local |
|---|---|---|---|---|---|
| Current fixed 10 dyadic eta | [search-current-leanfinder.json](../evidence/Roth.eta/search-current-leanfinder.json) | [search-current-loogle.json](../evidence/Roth.eta/search-current-loogle.json) | [search-current-leansearch.json](../evidence/Roth.eta/search-current-leansearch.json) | [search-current-rg.json](../evidence/Roth.eta/search-current-rg.json) | [search-current-local_search.json](../evidence/Roth.eta/search-current-local_search.json) |
| Literature small-index / iterated-root | [search-standard-leanfinder.json](../evidence/Roth.eta/search-standard-leanfinder.json) | [search-standard-loogle.json](../evidence/Roth.eta/search-standard-loogle.json) | [search-standard-leansearch.json](../evidence/Roth.eta/search-standard-leansearch.json) | [search-standard-rg.json](../evidence/Roth.eta/search-standard-rg.json) | [search-standard-local_search.json](../evidence/Roth.eta/search-standard-local_search.json) |
| Abstract scaled power / continuity | [search-abstract-leanfinder.json](../evidence/Roth.eta/search-abstract-leanfinder.json) | [search-abstract-loogle.json](../evidence/Roth.eta/search-abstract-loogle.json) | [search-abstract-leansearch.json](../evidence/Roth.eta/search-abstract-leansearch.json) | [search-abstract-rg.json](../evidence/Roth.eta/search-abstract-rg.json) | [search-abstract-local_search.json](../evidence/Roth.eta/search-abstract-local_search.json) |

Current and standard Finder gave additive Roth-number results: rejected because they concern arithmetic-progression-free subsets, not Diophantine index. Standard LeanSearch finds Real.sqrt_eq_rpow and rpow_div_two_eq_sqrt. Abstract finds real-power continuity. Loogle returned no items on the actual patterns; local names confirm source paths but index error means incomplete symbol-index contribution. Pinned candidate source archives and hashes: [mathlib-inputs.json](../evidence/Roth.eta/mathlib-inputs.json).

Existing building blocks: Real.rpow in Mathlib/Analysis/SpecialFunctions/Pow/Real.lean:36; Real.rpow_mul:415; Real.sqrt_eq_rpow:986; NNReal.coe_rpow in Pow/NNReal.lean:47; Real.continuousAt_rpow_const in Pow/Continuity.lean:218 and continuous_rpow_const:226. Exact signatures checked in native receipts. Existing natural power/multiplication/division provide the formula's other operations. No named semantic eta replacement is established. The newly defined generic formula/typed/rootIter functions must not be cited as existing mathlib declarations.

The exact18 isolated prefix does not expose continuity constants: accepted #check_failure verifies that import fact. Initial lexical import traversal overapproximated the graph and was explicitly rejected after native evidence. Prefix stayed unchanged; actual-context continuity is verified separately. [import-preflight.json](../evidence/Roth.eta/import-preflight.json); [isolated-rejected-receipt.json](../evidence/Roth.eta/isolated-rejected-receipt.json) preserves initial failed experiment with recovered sorryAx and is **not accepted evidence**. No accepted proof has sorryAx, raised resources, unsafe or native_decide.

## Phase 5.5 — Statement shape

Normal form: current rpow expression is the normal form for the chosen constants. Alternative nonnegative iterated roots need a new induction bridge; NNReal needs a domain restriction; a direct inverse power spelling is arithmetic notation only. Put the existing real-power expression on the RHS of bridge equalities. No new O(n²) bridge API proposed.

Syntactic generality attempted: original δ,m order; new C,b,δ,m profile; restricted NNReal scalar; m-fold root. Keep current δ,m order for project consumers, avoiding repeated coercions and extra constant arguments. No material application benefit established from changing m to a real.

Superfluous arguments: δ used as base and m in both exponents; neither can be dropped. No hypotheses/instances exist to delete. SHIP-AS-STATED for local semantics, subject to future public API boundary; not an automatic upstream YES.

## Phase 6.0 — Full caller and duplication audit

Eight lexical declaration callers;18 executable token occurrences (11 signature,7 written body); five in MainLemma, three in Main; one external-to-declaring-file module. Source enumeration with rg--no-ignore exactly agrees with git grep on tracked production Lean. [callers.json](../evidence/Roth.eta/callers.json) has full signatures/bodies, source SHA and per-site inlining action. [source-search.json](../evidence/Roth.eta/source-search.json); [tracked-source-search.json](../evidence/Roth.eta/tracked-source-search.json); [source-inventory.json](../evidence/Roth.eta/source-inventory.json) prevent ignore-rule omissions.

| Caller | File:line | Signature/body tokens | Actual use / mechanical inline plan |
|---|---|---|---|
| `Roth.exists_delta` | Roth/Main.lean:227 | 2/2 | Continuity/zero evaluation and gap denominator; replace eta δm by direct formula and remove eta from simp list. |
| `Roth.exists_roth_parameters_aux` | Roth/Main.lean:410 | 2/0 | Carries both eta constraint and gamma−eta bound; direct replacement in statement. |
| `Roth.one_lt_roth_eval_bound_aux` | Roth/Main.lean:453 | 1/0 | Taylor upper bound at gap; direct statement replacement. |
| `Roth.exists_delta_bound` | Roth/MainLemma.lean:77 | 1/2 | Continuity and at-zero simplification; direct formula plus remove eta from simp. |
| `Roth.eta_lt_gam_iff` | Roth/MainLemma.lean:100 | 2/0 | Both sides retain identical scalar eta; direct replacement, grind proof unchanged. |
| `Roth.theta_lt_eta_of_sq_log_bound_aux` | Roth/MainLemma.lean:671 | 1/1 | Consumes Θ_lt via simpa[eta]; expand RHS and remove eta from simp. |
| `Roth.exists_auxiliary_polynomial_with_index_gap_aux` | Roth/MainLemma.lean:692 | 1/0 | Gap statement; direct replacement. |
| `Roth.main_lemma` | Roth/MainLemma.lean:735 | 1/2 | Gap statement and internal cutoff c; replace all three occurrences. |

Canonical direct kernel types:8; direct values:8, with different member sets. eta_lt_gam_iff is a type consumer only; roth_of_isIntegral is a value consumer without an explicit eta token (elaborated arithmetic carries the index gap). This is not transitive/simp closure. No claim that lexical target removal makes imported downstream proofs target-free.

Actual full MainLemma/Main caller proofs were replayed after deleting eta's scratch definition and expanding every explicit eta application, not just replaced by calls to original theorems. All eight original signatures retained by rfl/Lean.Meta.isDefEq; roth_of_isIntegral also replays. Earlier imports remain original. Source/receipt: [inline-executed.lean.txt](../evidence/Roth.eta/inline-executed.lean.txt); [inline-receipt.json](../evidence/Roth.eta/inline-receipt.json).

| A | B | Same object/statement? | Same proof? | Action |
|---|---|---|---|---|
| eta δm | Roth.lem7_numeric RHS (Theta.lean), Θ_lt RHS | Exact same scalar10^m δ^((1/2)^m), up to natural successor/subtraction index | eta has no proof; lem7_numeric is substantive inequality | Future common definition must be before Theta, not import MainLemma back into Theta. |
| eta δm | lam δnm | no; nonlinear small-δ dyadic error versus affine-δ square-root dimension loss | no | Keep roles distinct. |
| eta δm | gam δnm | no; small-index upper error versus high-index lower cutoff | no | Gapγ−η meaningful; no unification. |
| eta δm | New C,b profile / NNReal typed | specialization / restricted representation | New scratch bridge, not old library proof | Do not call a typed representation an existing mathlib counterpart. |

Inline audit also inspected Roth.lem7_Φ_bound, Roth.lem7_numeric, theta_prefix_lt_aux, theta_lt_base_aux, theta_phi_lt_aux, theta_lt_succ_aux, theta_lt_of_large_delta_aux and Θ_lt; their full source is archived in [source-Theta.lean.txt](../evidence/Roth.eta/source-Theta.lean.txt). These use raw formula because Theta precedes MainLemma. No current production edit, movement or import cycle was made. They are uses of the same bound, not independent proofs of eta's definition.

## Phase 6 — Composition experiments

1. Direct arithmetic construction succeeds in one written line:

```lean
fun (δ : ℝ) (m : ℕ) ↦ (10 : ℝ) ^ m * Real.rpow δ ((1 / 2 : ℝ) ^ m)
```

It is a construction using natural powers, real power, division and multiplication; the new name is about meaning. No exact existing named eta definition or strict≤3-existing-semantic-call replacement was verified. Full proof inlining does succeed. Hence **NOT-COMPOSABLE** in the narrow named-theorem-replacement sense, while explicitly recording that arithmetic construction/inlining is trivial. This is not evidence of a new arithmetic theorem.

2. Existing Real.sqrt_eq_rpow plus Real.rpow_mul support the nonnegative m-fold-root representation; the induction rootIter_eq is a new proof. Not an existing≤3 call replacement. NNReal.coe_rpow gives typedBridge by simp normalization. Under Phase6b this is a trivial simp composition to record as BORDERLINE, not automatic NO. Both typed/rootIter definitions are new scratch objects, not mathlib counterparts.

3. Actual-context etaContinuous uses Real.continuous_rpow_const with positive dyadic exponent and const_mul; atZero uses zero_rpow. They establish convenient local API, not a need to upstream the exact numerical choice. No unconstrained arbitrary-b continuity or negative-base root equivalence is claimed.

Accepted sources and full raw results: [verification.json](../evidence/Roth.eta/verification.json). Four complete native sets, all standard axioms only. Original partial cold-load and rejected isolated attempt are separately retained and excluded from accepted verification. No resource increases. Exact canonical array is generated from tracked declaration-order; source preflight and runtime agree on293 requested,293 unique,293 present,293 values with correct private modules/order.

## Phase 7 — Verdict and concrete action

**BORDERLINE-needs-human.** Eta is a useful semantic parameter already shared by an earlier endpoint inequality and later parameter/gap statements, not dead code. Local clean.tex eq(36) exactly names it, but primary alternative expositions organize small-index bounds with different constants/free parameters. Existing mathlib arithmetic and analytic API construct the number and its basic laws; neither a novel structure nor a uniquely standard generic numerical-envelope API has been demonstrated. The one-line semantic exemption and eight callers prevent automatic dismissal, while the trivial construction and representational bridges prevent a claim of novel library mathematics. This verdict is based on API meaning and audience, never implementation cost or previous parameter verdicts.

Two future upstream questions:

1. For an upstream Roth development, should this exact dyadic error be a public documented parameter shared with the small-index theorem, or remain local numerical notation?
2. If shared, should the definition move to a dependency before Theta, or should a generic scaled power profile be introduced with fixed 10,half chosen only in the application?

Current authorized action: retain eta during the read-only overview. Local continuity/zero companion lemmas can be considered in an explicitly authorized cleanup. If future design chooses local notation, use the caller-specific inline plans above; every written proof and original signature has already been tested. If shared public API is chosen, put it before Theta and assess with the substantive small-index theorem. No claim of an accepted YES grouping/home/PR title: those fields are not applicable to this BORDERLINE verdict, and no useful neighbouring name was treated as a previous YES.

## Phase 8 — Completion and portable evidence

All mandatory phases PASS; optional ask_chatgpt_math justified n/a. Completed=true, unresolved[]. Root acceptance pending. Four accepted exact executed sources archived as .lean.txt with original requests, full raw receipts, durations and source hashes; exact18/nineimport prefixes preserved. Current copy-manifest is authoritative, not historical worker-copy-manifest. Portable validator checks current evidence hashes/bytes, mandatory overview keys, source/pin freshness, all 15 formal cells, web metadata/URL hygiene, full native success and standard axioms, exact canonical 293 order/private names, caller/full-source hashes, relative links, rejected separation and secret guard. Integration-only root-acceptance/root-review files are excluded from worker coverage.

Validation artifacts: [assessment.json](../evidence/Roth.eta/assessment.json), [verification.json](../evidence/Roth.eta/verification.json), [overview-entry.json](../evidence/Roth.eta/overview-entry.json), [copy-manifest.json](../evidence/Roth.eta/copy-manifest.json), [validate.py](../evidence/Roth.eta/validate.py).
