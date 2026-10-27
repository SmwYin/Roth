# Roth.aeval_X_eq_rename — full mathlibable assessment

Verdict: **NO-mathlib-has-it**. Mathlib already states the same identity as equality of bundled algebra homomorphisms in `Polynomial.toMvPolynomial_eq_rename_comp`, at `Mathlib/Algebra/MvPolynomial/Equiv.lean:891`. Applying that equality to a polynomial gives this exact statement. The conclusion follows from the positive pinned hit, not the length of the project proof or any inherited verdict.

## Phase 0 — Doctor

The public theorem resolves at `Roth/Separation.lean:137`. This module separates one distinguished polynomial variable, proves separated representations and factors determinants of Hasse derivatives. All 17 production source and pin hashes freshly match the baseline manifest. The clean baseline build and the later successful full Index build remain applicable; no source, pin, Git, overview or progress mutation was made by this assessment. Original native diagnostics are successful and complete, with no errors, warnings or recovered sorry. The target has only standard axioms `propext`, `Classical.choice`, `Quot.sound`.

Evidence: [fresh inputs](../evidence/Roth.aeval_X_eq_rename/inputs.json), [baseline](../evidence/Roth.aeval_X_eq_rename/baseline-build.txt), [later build](../evidence/Roth.aeval_X_eq_rename/index-file-completion-2026-10-27.json), [original native receipt](../evidence/Roth.aeval_X_eq_rename/aeval-rename-original-audit-receipt.json).

## Phase 1 — Comprehend

For a commutative semiring R, an arbitrary variable set σ and a selected i in σ, evaluating a univariate polynomial f at the formal variable Xᵢ gives the same multivariate polynomial as first regarding f as a polynomial with one Unit-indexed variable and then renaming that variable to i. This is an identity of formal polynomial expressions; it does not assert equality of arbitrary polynomial functions. Coefficients are preserved and the exponent of the single input indeterminate becomes the exponent at i.

Full native elaborated type:

```lean
Roth.aeval_X_eq_rename : ∀ {R : Type u_1} [inst : CommSemiring R] {σ : Type u_2}
  (i : σ) (f : Polynomial R),
  (Polynomial.aeval (MvPolynomial.X i)) f =
    (MvPolynomial.rename fun x ↦ i) ((MvPolynomial.uniqueAlgEquiv R Unit).symm f)
```

R and σ occupy independent universes. The only typeclass is `CommSemiring R`. There is no τ, Fintype, DecidableEq, domain, characteristic or nonzero hypothesis. The ambient section's τ instances do not occur in the native type. `i` selects the coordinate, `f` is arbitrary, `Unit` supplies the one-generator presentation. There are no project dependencies in the target's proof. Its entire kernel proof is the application of `AlgHom.congr_fun` to the existing Mathlib equality; the printer output is complete without an elision marker.

Evidence: [native type](../evidence/Roth.aeval_X_eq_rename/native-type.json), [whole declaring module](../evidence/Roth.aeval_X_eq_rename/Roth-Separation.lean.txt), [pinned Mathlib module](../evidence/Roth.aeval_X_eq_rename/Mathlib-Algebra-MvPolynomial-Equiv.lean.txt).

## Phase 2 — Preliminary checks

SMALL: a representation-compatibility helper, not a named theorem, new structure or module main result. The definition-only one-line prefilter is n/a because this is a theorem. No definition barrier, instance diamond exemption or cost argument determines the verdict. All exhaustive phases still ran.

## Phase 3 — Exhaustive literature

All named channels were executed. The optional `ask_chatgpt_math` tool is unavailable; this is the sole unavailable channel. Each search request, response SHA256, response byte count, returned title/locator and honest access status is retained without archiving article/search bodies. Returned locator query strings were removed as a credential precaution.

| Channel | Actual query | Outcome and interpretation |
|---|---|---|
| General web, specific | `univariate polynomial embedding multivariate polynomial renaming variable` | Found polynomial renaming and embedding documentation. Pinned source, rather than mirror documentation, establishes the Lean API. |
| General web, general | `polynomial algebra universal property free commutative semiring algebra substitution` | Found Bergman's textbook treating polynomial algebras as free commutative algebras and substitution through their universal mapping property. |
| General web, aliases | `polynomial ring in one variable singleton indeterminates natural isomorphism` | Found polynomial ring lecture notes; singleton-generator presentation is the natural interpretation, with no separate named identity required. |
| ChatGPT mathematics | unavailable | No configured `ask_chatgpt_math`; no substitute model opinion fabricated. |
| Local clean.tex | `embedded\|collecting\|one-variable\|roth:lem4-2` | §4 Lemma4-2 lines614–624 identifies embedded Q's index with its one-variable index; §2 line374 collects terms in a distinguished variable. This contextualizes the representation bridge, not its semiring generality. |
| nLab | `site:ncatlab.org/nlab/ polynomial ring free commutative algebra` | Found polynomial/free algebra discussion. Direct open of polynomial page failed with unsupported `application/xhtml+xml`; search results provide context only. |
| nCatLab | `site:ncatlab.org/ncatlab polynomial algebra substitution` | Actual distinct namespace query returned nLab pages and no exact nCatLab law; no namespace match claimed. |
| Stacks | `site:stacks.math.columbia.edu polynomial ring universal property` | Returned generator-map use in04EB and divided-power results. Refined quoted query preserved. Direct04EB proof line27 sends polynomial generators to chosen elements, an indirect use of substitution; its theorem is not the identity being assessed. The exploratory00E5 page is about spectra of quotients and was rejected as irrelevant. |
| MathOverflow | `site:mathoverflow.net polynomial ring universal property variables` | Discussions of universal polynomial-ring properties, including question73664. These are context, not authority for a pinned Lean signature. |
| recent arXiv | `site:arxiv.org/abs/ polynomial semiring free commutative algebra 2022 2023 2024 2025 2026` | Broad query returned older and unrelated results, so targeted2024 semiring and2023 free-commutative searches followed. Manjunath2410.15426 (2024-10-20) treats one-variable equations over polyhedral semirings; Wang et al2403.12716 (2024-03-19) treats Kronecker substitution. Neither supplies a new version of this coordinate-renaming law. Both lie within the five-year window. |

The standard concept is substitution through the universal property of a polynomial/free commutative algebra, and its compatibility with generator renaming. The general standard form compares algebra maps agreeing on generators. Coefficient rings in elementary sources may be fields or commutative rings; the present theorem already works over commutative semirings. No historical change of mathematical content is evidenced: the bundled Lean form organizes the classical substitution property. There is no literature basis for imposing finite variable sets or integral domains.

Primary locator: [Bergman, An Invitation to General Algebra and Universal Constructions](https://math.berkeley.edu/~gbergman/245/3.4.pdf), §4.12 printed p85, PDF p91, lines3961–3964. It explains free commutative polynomial algebras and substitution. [Stacks04EB](https://stacks.math.columbia.edu/tag/04EB), proof line27, is contextual only. Recent primary sources: [Manjunath2024](https://arxiv.org/abs/2410.15426) and [Wang et al2024](https://arxiv.org/abs/2403.12716).

Evidence: [all eight search-channel requests](../evidence/Roth.aeval_X_eq_rename/literature-individual.json), [primary access and targeted retries](../evidence/Roth.aeval_X_eq_rename/literature-primary-access.json), [availability and limitations](../evidence/Roth.aeval_X_eq_rename/literature-availability.json), [local search](../evidence/Roth.aeval_X_eq_rename/local-literature-search.json), [source excerpt](../evidence/Roth.aeval_X_eq_rename/clean-excerpt.tex.txt).

## Phase 4a — Generality status

| Parameter/interface | Current form | Standard/abstract target | Actual conclusion |
|---|---|---|---|
| R | arbitrary universe-polymorphic type | coefficient commutative semiring | Already arbitrary; no special coefficient field. |
| CommSemiring R | commutative semiring | same for the fixed `MvPolynomial`/R-algebra interface | Used by both the maps and their types; dropping to plain Semiring does not preserve this interface. No unverified weakening claimed. |
| σ | arbitrary independent universe | arbitrary generator set | No finiteness, ordering or decidable equality needed; native oldForm confirms this. |
| i : σ | selected generator | selected generator | Cannot remove while keeping a specified-coordinate embedding; σ may otherwise be empty. |
| f : Polynomial R | arbitrary polynomial | equality of algebra maps, hence all f simultaneously | Bundled form eliminates explicit f from the law and is already Mathlib's existing statement. |
| Unit | fixed singleton generator set | arbitrary `[Unique ι]` representation | Actual Unique-index extension compiles by homomorphism extensionality; this is representation expansion with a new proof, not a missing assumption on the original theorem or an existing-call replacement. |
| Coefficients unchanged | R-algebra self coefficients | coefficient-changing evaluation into another algebra | A separate substitution/mapping interface; not obtained merely by dropping a hypothesis. Existing `aeval_comp_toMvPolynomial` is relevant API. No speculative generalise-first claim. |
| Ambient τ/Fintype/DecidableEq | absent in elaborated theorem | absent | No hidden assumptions to drop. |

## Phase 4b — Generality verdict

MAXIMALLY GENERAL for the fixed R-coefficient and Unit presentation interface: zero verified typeclass weakenings. A useful expanded singleton representation was actually proved:

```lean
{ι : Type*} [Unique ι] → ∀ (i : σ) (f : Polynomial R),
  Polynomial.aeval (X i : MvPolynomial σ R) f =
    rename (fun _ : ι ↦ i) ((uniqueAlgEquiv R ι).symm f)
```

This changes the representation parameter, and its proof uses `Polynomial.algHom_ext` and generator normalization. It is not counted as an existing theorem or a ≤3 existing-call composition. The original target is nevertheless already the pointwise instance of an exact existing bundled identity. No cost-based verdict adjustment is made.

Evidence: [accepted isolated execution](../evidence/Roth.aeval_X_eq_rename/aeval-rename-isolated-executed.lean.txt), [successful native receipt](../evidence/Roth.aeval_X_eq_rename/aeval-rename-isolated-receipt.json).

## Phase 4c — Modern idiom, all nine rows

| # | Diagnostic | Applies and consequence |
|---|---|---|
|1| Typeclass preambles | Already uses `CommSemiring` and the canonical inferred R-algebra structures. No new predicate/instance proposed. |
|2| Filters/topology | No: exact polynomial algebra identity, with no convergence. |
|3| Universal property | Yes organizationally: equality of algebra homomorphisms compares substitutions at the generator. Existing `Polynomial.toMvPolynomial_eq_rename_comp` already supplies this form and `Polynomial.algHom_ext` explains its proof. Enables composition with `AlgHom.comp` and applying to any f. |
|4| Bundled substructure | No sets with closure predicates occur. Bundled algebra maps, rather than substructures, are the relevant existing API. |
|5| Hierarchy weakening | No field/ring assumption to weaken: commutative semiring already suffices. No invented noncommutative claim. |
|6| Higher category | No: no concrete downstream need for higher categorical coherence in the five consumers. |
|7| Concrete index | Unit is the singleton representation, not an additive index. Actual arbitrary `[Unique ι]` extension succeeds; σ was arbitrary already. |
|8| Concrete-via-abstract | Diagnostic fires as representation organization: the one-line body has zero literal `Unit` occurrences and applies a bundled map equality to f; i and f each occur once. Thus bundling removes the concrete argument f and the existing Mathlib hit supplies the abstract content. The actual Unique experiment separates representation expansion from assumption removal. |
|9| False-generalization guard | Replacing Xᵢ by an arbitrary polynomial while leaving rename-to-i unchanged is false. Actual `falseGeneralization` chooses R=ℕ, σ=Unit, f=X and proposed evaluation point0; coefficient at exponent1 distinguishes0 from X. This guard compiled with standard axioms. Valid bundled/Unique forms preserve the chosen generator. |

Modern idiom available: **yes, already present**. This yields no modernization contribution: the library form is at least as organized as the project statement. Concrete downstream benefits are `AlgHom.comp` equalities and one application for all rewrite instances. The proposed abstract form does not depend on unavailable API.

## Phase 4.5 — Infrastructure risk

n/a — theorem, not def/class/instance. Typeclass diamonds, reducibility leaks, noncanonical unfolding, instance priorities, universe constraints in a new data construction and competing coercions are all outside scope: no new definition or instance is proposed. Existing universe-polymorphic maps and canonical coercions are checked natively.

## Phase 4.6 — Proof strategy, all five rows

| # | Question | Assessment |
|---|---|---|
|1| Topology ε–δ versus filters | n/a: no topology. |
|2| Algebra elements versus pointfree | The pointwise statement follows by applying an existing pointfree equality; this is the appropriate use of `AlgHom.congr_fun`, with no coefficient calculation. |
|3| Analysis sequences versus nets | n/a: no analysis. |
|4| Explicit construction versus universal property | Existing Mathlib proof uses the polynomial algebra homomorphism extensionality theorem. Reuse this identity rather than reconstructing maps. |
|5| Missing helper API | None needed for the exact target or all five callers; the arbitrary-Unique experiment is a new representation variant and does not establish a required gap. |

MATHLIB-IDIOMATIC. The project proof already uses the right mathematical strategy; the action is API deduplication. No proposed proof helper or expensive-development objection determines the verdict.

## Phase 5 — All five Mathlib methods on all three forms

All15 cells executed: Finder, Loogle, LeanSearch, source rg and local name search, each on current pointwise, standard singleton/free-polynomial and abstract bundled-composition forms. Exact requests and complete raw tool results are preserved.

| Method | Current | Literature-standard | Modern abstract |
|---|---|---|---|
| Finder | exact `Polynomial.toMvPolynomial_eq_rename_comp` hit | same exact hit | same exact hit plus composition API |
| Loogle | `Polynomial.toMvPolynomial, MvPolynomial.rename` hits exact law | `MvPolynomial.uniqueAlgEquiv, MvPolynomial.rename` hits exact law | `Polynomial.toMvPolynomial, AlgHom.comp` hits exact law, aeval composition and renaming composition |
| LeanSearch | exact bundled law | exact bundled law | exact law and `Polynomial.algHom_ext` |
| rg | exact pinned lemma at Equiv891 and rename law | singleton equivalence and embedding definitions | bundled composition laws and polynomial hom extensionality |
| local | `toMvPolynomial` finds exact lemma | `uniqueAlgEquiv` finds singleton equivalence | `rename_comp` finds bundled renaming composition |

Local responses honestly report `index: unavailable`; their returned lexical matches are still positive source locators, never evidence of absence. Finder/LeanSearch external signatures sometimes use `pUnitAlgEquiv`; this is an index-revision mismatch, not this pin's spelling. Pinned source, Loogle and actual native type confirm `uniqueAlgEquiv R Unit`. The qualified project target is missing in the isolated environment (`#check_failure`), preventing circular target use.

Concluded: **found in Mathlib as `Polynomial.toMvPolynomial_eq_rename_comp`; bundled form contains the exact law for every f**. It states equality of the same two R-algebra maps, one named `toMvPolynomial` (definitionally `Polynomial.aeval (X i)`), with the same Unit representation. This is not only a partial naturality match.

Evidence: [current four formal methods](../evidence/Roth.aeval_X_eq_rename/formal-search-current.json), [other eight formal calls](../evidence/Roth.aeval_X_eq_rename/formal-search-other.json), [current rg](../evidence/Roth.aeval_X_eq_rename/rg-current.json), [standard rg](../evidence/Roth.aeval_X_eq_rename/rg-literature.json), [abstract rg](../evidence/Roth.aeval_X_eq_rename/rg-modern.json), [native pinned signatures and complete theorem print](../evidence/Roth.aeval_X_eq_rename/aeval-rename-isolated-receipt.json).

## Phase 5.5 — Statement shape

Normal-form alternatives: pointwise equality at f; function equality of the two coerced maps; bundled equality of R-algebra homomorphisms. Mathlib's bundled equality is canonical and preserves the same orientation (evaluation/embedding on left, renaming composition on right). The project pointwise equation is a usable specialization, but adding a separate global name duplicates that law.

Syntactic-generality attempt: `bundled` directly uses the existing map equality, and `oldForm` applies it at any f. Both actually compile. All five full callers also compile using that pointwise specialization, preserving their rewrite orientation. A local `have` binding of the existing specialization is a mechanical way to retain a simp/rewrite name after deleting the public wrapper.

Superfluous-argument audit: R determines coefficients; CommSemiring R supplies the fixed polynomial and R-algebra interfaces; σ and i determine the target variable; f is the universally quantified input. No unused elaborated argument or instance exists. τ/Fintype/DecidableEq are absent, not pending removals. Unit can be expanded to another Unique representation, as explicitly verified.

Verdict: normal form OK as pointwise instance; syntactic generality favors using the existing bundled law; superfluous arguments NONE. SHIP-AS-STATED is vacuous for a NO verdict; do not ship an additional theorem. Refactor locally to existing API.

## Phase 6.0 — Complete caller and inline audit

Fresh lexical enumeration of every production source in the canonical inventory, `rg --no-ignore` scoped to Roth/ and Roth.lean, and tracked `git grep` agree on six occurrences: one declaration and **five explicit uses**, one use per caller. Three are same-file and two external in Theta. Internal-use count excluding declaring file is2; total downstream uses5; external files1. No dot-notation or qualified occurrence is missed. The fresh exact canonical293 ordered kernel-value audit finds exactly the same five direct consumers. Source references, direct kernel consumers and transitive/simp dependency closure are distinct quantities; no claim of a full opaque dependency closure is made.

| Caller and location | Use | Concrete refactor plan |
|---|---|---|
| `Roth.hasseDeriv_rename_mul_aeval`, Separation162 | `simp [aeval_X_eq_rename, degreeOf, …]` | Replace the simp argument by local specialization `oldForm`, proved solely from `AlgHom.congr_fun (Polynomial.toMvPolynomial_eq_rename_comp i) f`, or bind an equivalent local `have` and use it. Full body verified. |
| `Roth.degreeOf_rename_mul_aeval`, Separation207 | `simp [aeval_X_eq_rename, degreeOf, …]` | Same local specialization in the final simp step; all degree and injectivity arguments preserved. Full body verified over the original CommRing/IsDomain interface. |
| `Roth.degreeOf_none_rename_mul_aeval`, Separation224 | `rw […, zero_add, aeval_X_eq_rename]` | Supply the specialization at i=none and f=V in this rewrite; the subsequent existing degree proof is unchanged. Full body verified. |
| private `Roth.index_separated_mul_le_aux`, Theta437 | `rw [aeval_X_eq_rename, map_mul, …]` | Supply specialization at i=none with R=ℤ and polynomial V before coefficient mapping and index renaming; full body verified with only Fintype τ, matching original elaboration. |
| private `Roth.mapped_det_ne_zero_aux`, Theta528 | `rw [aeval_X_eq_rename, map_eq_zero_iff …]` | Supply the same ℤ/none/V specialization before injectivity rewrites; full body verified without Fintype or DecidableEq assumptions. |

Inline-derivation grep: no independent rederivation of this exact identity found. There are other `uniqueAlgEquiv.symm` representations and the target's own original Mathlib call; they are recorded but are not bypass proofs. Five consumers establish usefulness, not upstream novelty against an exact existing theorem.

Evidence: [lexical inventory](../evidence/Roth.aeval_X_eq_rename/lexical-enumeration.json), [rg](../evidence/Roth.aeval_X_eq_rename/caller-rg.json), [git grep](../evidence/Roth.aeval_X_eq_rename/caller-git-grep.json), [inline search](../evidence/Roth.aeval_X_eq_rename/rg-inline.json), [full Theta module](../evidence/Roth.aeval_X_eq_rename/Roth-Theta.lean.txt), [fresh293 audit source](../evidence/Roth.aeval_X_eq_rename/aeval-rename-audit-executed.lean.txt), [original/audit receipt](../evidence/Roth.aeval_X_eq_rename/aeval-rename-original-audit-receipt.json).

## Phase 6 — Actual composition experiments

Attempt1 succeeds in the isolated Mathlib-only native environment:

```lean
example {R σ : Type*} [CommSemiring R] (i : σ) (f : Polynomial R) :
    Polynomial.aeval (MvPolynomial.X i : MvPolynomial σ R) f =
      MvPolynomial.rename (fun _ : Unit ↦ i) ((MvPolynomial.uniqueAlgEquiv R Unit).symm f) :=
  AlgHom.congr_fun (Polynomial.toMvPolynomial_eq_rename_comp i) f
```

Honest old-form count: one existing mathematical theorem, plus the generic equality-application operation `AlgHom.congr_fun` (two named calls total). The bundled identity itself is one existing call. `Polynomial.toMvPolynomial` unfolds definitionally to aeval at Xᵢ; no newly proved normalization bridge is required. `AlgHom.comp` and the inverse-equivalence coercion evaluate definitionally at f. There is no closing `simp [defs…]` composition hidden here.

Attempt2 confirms organization: `bundled` is exactly `Polynomial.toMvPolynomial_eq_rename_comp i`. The arbitrary-Unique experiment uses a genuine extensionality proof and is excluded from the existing-call count. The concrete false-generalization guard rejects arbitrary replacement of Xᵢ.

Actual-context experiment: all five **complete caller bodies** were replayed in a fresh namespace. Each uses a scratch `oldForm` with exactly the Mathlib-only proof above. The original target is not referenced in the replay region, and no own/downstream simp theorem supplies the replacement proof. Existing project lemmas remain legitimate context for their other mathematical steps, not counted as Mathlib building blocks. Root split semiring/domain/finite-Theta/mapped sections to match original elaborated interfaces; the preparation-only file is not the authoritative execution. Native execution succeeds completely, with no errors/warnings, all six replay declarations using only standard axioms. No rejected native attempt occurred.

Conclusion: COMPOSABLE, and more specifically an **exact bundled Mathlib hit**. The proper verdict is NO-mathlib-has-it, not a generic composition-based absence claim.

Evidence: [isolated exact execution](../evidence/Roth.aeval_X_eq_rename/aeval-rename-isolated-executed.lean.txt), [isolated receipt](../evidence/Roth.aeval_X_eq_rename/aeval-rename-isolated-receipt.json), [all five full callers exact executed source](../evidence/Roth.aeval_X_eq_rename/aeval-rename-callers-executed.lean.txt), [all callers native receipt](../evidence/Roth.aeval_X_eq_rename/aeval-rename-callers-receipt.json), [verification map](../evidence/Roth.aeval_X_eq_rename/verification.json).

## Phase 7 — Actionable verdict and gate

**NO-mathlib-has-it**. Exact existing declaration: `Polynomial.toMvPolynomial_eq_rename_comp` in `Mathlib/Algebra/MvPolynomial/Equiv.lean:891`. It gives the identity of the same two algebra homomorphisms; pointwise evaluation gives this exact Unit-form theorem by the one-line term above. Both the hit and actual representation compatibility were independently verified. This conclusion does not rely on failed searches, inherited judgments, proof cost or the arbitrary-Unique extension.

Existing building blocks are `Polynomial.toMvPolynomial_eq_rename_comp` (Equiv891), `Polynomial.toMvPolynomial` (Equiv880), `MvPolynomial.uniqueAlgEquiv` (Equiv's one-variable section), `MvPolynomial.rename`, and `AlgHom.congr_fun` for equality application. Only the first and last are named proof calls. Alternative local destination: a local `have`/rewrite specialization at each of the five listed callers, or a private project-local compatibility helper in Separation if repeat spelling warrants one. There is no reason to move a duplicate to Archive or a satellite mathematical library.

Next action: delete the public `Roth.aeval_X_eq_rename` and apply the five caller refactors above, using the existing bundled identity and generic congruence. Full replay demonstrates the proposed local proof source for every caller; the assessment itself deliberately makes no production changes. No YES PR title/home/grouping/reviewer checklist is applicable to a NO verdict. No unresolved design question or verification remains. Root independent review remains pending.

## Phase 8 — Package and integrity

Completed all mandatory phases with actual native success. Exact executed Lean sources use `.lean.txt` evidence suffixes; unchanged original execution paths remain in raw receipts. Native messages are scoped to target-specific fresh regions while full-file errors/warnings and axiom checks remain enforced. The canonical audit has293 requested entries,293 unique names,293 present constants and293 values, with exact order including private names compared against tracked declaration-order.json. Canonical direct target dependencies are empty; direct callers are the five listed constants.

[Portable validator](../evidence/Roth.aeval_X_eq_rename/validate.py) checks fresh source/pin hashes, current copy manifest hashes/bytes, required overview keys, phase completion, exact canonical order, native completion, standard axioms, lexical/rg/git agreement, all search rows and literature channels, source links, executed replacement/caller regions and credential guard. [Assessment metadata](../evidence/Roth.aeval_X_eq_rename/assessment.json) keeps `root_acceptance=pending`; no publication is implied.
