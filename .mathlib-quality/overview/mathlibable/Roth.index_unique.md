# Roth.index_unique — full mathlibable assessment

**Verdict: NO-mathlib-has-it, after the parent re-aim.** The normalized univariate law is `Polynomial.rootMultiplicity_eq_natTrailingDegree`. The original spelling requires an actual support/translation bridge; it is not a one-call replacement in the unchanged project. Independently checked proofs also show that its nonzero-polynomial hypothesis is removable.

## Phase 0 — Doctor

Canonical declaration 151 is the public theorem at `Roth/Index.lean:234`, the last declaration in that module. The whole declaring module and the complete sole caller proof were read: [Index](../evidence/Roth.index_unique/Roth-Index.lean.txt), [Theta](../evidence/Roth.index_unique/Roth-Theta.lean.txt), [canonical metadata](../evidence/Roth.index_unique/canonical-target.json). Index develops weighted Taylor-support minima, bounds, differentiation, sums, products, scalar and variable changes, and the one-variable multiplicity comparison.

The historical [baseline build](../evidence/Roth.index_unique/baseline-build.txt) succeeded, exit 0, 2467 jobs. All 17 current source/pin hashes were independently recomputed and agree with that baseline manifest: [inputs](../evidence/Roth.index_unique/inputs.json), [manifest](../evidence/Roth.index_unique/input-manifest.json). A fresh full build at completion is separately archived with this package. Production sources, pins, Git and progress records remain unchanged by the worker.

## Phase 1 — Comprehend

A polynomial in a unique variable can be viewed as a univariate polynomial. At any center α, its index is the multiplicity of α as a root, divided by the denominator assigned to the variable. The source assumes the polynomial is nonzero, but the formula remains valid at zero because both the project index and mathlib's natural rootMultiplicity use zero there. Natural denominator zero is also allowed: both sides then vanish.

Full native type:

```lean
@Roth.index_unique : ∀ {σ : Type u_1} [inst : Fintype σ] [inst_1 : Unique σ]
  {P : MvPolynomial σ ℝ}, P ≠ 0 → ∀ (α : σ → ℝ) (r : σ → ℕ),
  Roth.index P α r =
    ↑(Polynomial.rootMultiplicity (α default) ((MvPolynomial.uniqueAlgEquiv ℝ σ) P)) /
      ↑(r default)
```

σ is arbitrary-universe; Fintype supplies the sum in the project weight; Unique identifies a distinguished sole variable and supplies the univariate algebra equivalence; P is a real-coefficient multivariate polynomial; hP asserts nonvanishing; α is the center; r supplies natural denominators. The conclusion is equality in ℝ, with explicit natural-number casts on multiplicity and denominator.

Proof: put q equal to the univariate Taylor expansion. The project Hasse-derivative/equivalence compatibility and evaluation comparison identify each translated multivariate coefficient with q's coefficient at d(default). Nonvanishing of P ensures nonvanishing of q. Rewrite multiplicity as natTrailingDegree of q; the trailing coefficient realizes the minimum, and every nonzero coefficient has exponent at least natTrailingDegree. Divide the two inequalities by the nonnegative natural denominator. Project dependencies include index, weight, index_le_weight, le_index_iff and the project Hasse compatibility API; these are not existing mathlib replacement calls.

The fresh [full original printer and canonical source](../evidence/Roth.index_unique/index-unique-original-executed.lean.txt), [raw original/audit receipt](../evidence/Roth.index_unique/index-unique-original-audit-receipt.json), and [exact audit block](../evidence/Roth.index_unique/index-unique-audit-executed.lean.txt) contain the complete 5374-character kernel printer without MCP elision. The target uses only propext, Classical.choice and Quot.sound. The new target-specific runtime audit checks 293 requested names, 293 unique, 293 present and 293 value-bearing, in exact tracked order including private names. It finds one direct kernel-value consumer, the private Theta index_unique_le_log_div; this is distinct from transitive kernel or simp closure.

## Phase 2 — Preliminary checks

BIG: explicitly named among the module's main results and supplies the univariate step of Lemma 5. The one-line definition test and its three exemptions are n/a: the declaration is a theorem, not a definition. The original proof is a genuine coefficient-minimum argument, not literal rfl glue; no inherited-glue shortcut is used.

## Phase 3 — Exhaustive literature

Exact requests, response SHA256/bytes/status, sanitized locators and titles are archived, with original concise summaries and no article/search-result bodies: [general forms](../evidence/Roth.index_unique/web-general.json), [nLab/nCatLab/Stacks](../evidence/Roth.index_unique/web-labs-stacks.json), [MO/recent arXiv](../evidence/Roth.index_unique/web-mo-arxiv.json), [direct primary access](../evidence/Roth.index_unique/web-primary.json), [precise locators](../evidence/Roth.index_unique/web-locators.json), [synthesis](../evidence/Roth.index_unique/literature-summary.json).

| Channel | Actual query / primary locator | Finding and limit |
|---|---|---|
| General specific | `Roth theorem polynomial index one variable multiplicity divided weight Taylor expansion` | [Milojevic, An elementary approach to Roth's theorem](https://aleksa-milojevic.github.io/expository/roth.pdf), §3, Claim 3.1 and Taylor-support explanation. The title page gives January 2022; search publication freshness is not substituted for that date. |
| General most-general | `polynomial order vanishing multiplicity smallest nonzero Taylor coefficient Hasse derivative arbitrary characteristic` | [Tao, Algebraic combinatorial geometry](https://ems.press/content/serial-article-files/36979), §2, printed pp.9–10, Taylor formula and divisibility/Hasse criterion over fields. Direct PDF text inspected; supports arbitrary characteristic, with infinite order at zero. |
| General aliases | `Dyson lemma normalized index polynomial one variable root multiplicity` | Weighted-index accounts of Roth/Dyson, including Roth's1958 ICM account; useful historical context. The abstract root-multiplicity/lowest-Taylor-coefficient identity is the common mathematical core. No full ICM PDF inspection is claimed. |
| ChatGPT math | Standard form, generality, historical evolution | n/a: ask_chatgpt_math unavailable. Other channels all executed. |
| Local reference | `multiplicity|Taylor|ind\(|index|r_1|r_\{1\}` in clean.tex | [Exact search](../evidence/Roth.index_unique/local-literature-search.json), [§4–5 excerpt](../evidence/Roth.index_unique/clean-index-excerpt.tex.txt): §5 Lemma 5 proof explicitly sets t to root multiplicity and obtains index=t/r₁. §4 uses positive real denominators and zero index +∞. |
| nLab | `site:ncatlab.org/nlab order vanishing multiplicity polynomial Taylor` | [Taylor's theorem](https://ncatlab.org/nlab/show/Taylor%27s+theorem), smooth Taylor expansion: indexed excerpt inspected. Direct open failed400 unsupported application/xhtml+xml. Adjacent real analytic context, not a substitute for Hasse theory in finite characteristic. |
| nCatLab | `site:ncatlab.org/ncatlab multiplicity polynomial order vanishing` | Actual distinct namespace query returned off-path nLab pages/files, including category-theory notes. No exact nCatLab result accepted. No categorical restatement forced from this failed-to-find query. |
| Stacks | `site:stacks.math.columbia.edu polynomial multiplicity Taylor coefficient order vanishing`, then tag-focused query | [Definition 10.121.2, tag 02MD](https://stacks.math.columbia.edu/tag/02MD), lines 23–31, directly inspected: length-theoretic order of vanishing. Geometric adjacent formulation, not a denominator-weighted univariate API. |
| MathOverflow | `site:mathoverflow.net polynomial multiplicity Hasse derivative Taylor coefficient characteristic` | [Multiplicity in positive characteristic](https://mathoverflow.net/questions/338778/multiplicity-of-a-polynomial-in-positive-characteristic) and [algebraic Taylor expansion](https://mathoverflow.net/questions/82970/algebraic-taylor-expansion-for-polynomials-rational-functions-with-coefficie) discuss ordinary derivative failure and Hasse replacement. Context only; proofs rest on pinned sources and native checks. |
| Recent arXiv,2021-10-27–2026-10-27 | `site:arxiv.org/abs/ Hasse derivatives multiplicity polynomial after:2021-10-27 before:2026-10-28`, refined2024 query | [Chernyavsky–Lebedev–Trubnikov,2404.08550](https://arxiv.org/abs/2404.08550), submitted 2024-04-12, abstract directly inspected. Higher-resultant derivatives recover multiple roots; adjacent application, no exact index theorem or full-paper equivalence claimed. |

Synthesis: the standard content is the least nonzero Taylor coefficient characterization of univariate multiplicity, followed by a nonnegative scaling. Hasse derivatives provide the characteristic-independent version. The manuscript's infinite zero order differs from the project's zero-valued projection; that discrepancy must be preserved in any representation bridge. Classical positive real denominators are broader than the natural r interface, but negative scaling would select a maximum exponent rather than the least one.

## Phase 4a — Parameter and hypothesis inventory

| Parameter / hypothesis | Actual role | Checked weakening / limitation |
|---|---|---|
| σ : Type u | unique variable type | Already universe-polymorphic. Polynomial R eliminates the variable index entirely in the expanded representation. |
| Fintype σ | fixed index/weight interface | Unique.fintype supplies the Fintype instance automatically; the explicit ambient binder can be omitted. Fintype-choice independence is checked. This is interface reconstruction, not silently deleting a binder from an unchanged elaborated expression. |
| Unique σ | defines default and uniqueAlgEquiv | Required by this representation. Arbitrary multivariable collapse can cancel monomials, so a generic rename is not an equality of the same one-variable object. Native source typechecks the existing Unique-based API. |
| ℝ coefficients | fixed Roth.index interface | Univariate Taylor multiplicity already works over CommRing R. The isolated support minimum proof keeps ℝ as the ordered numerical codomain while allowing arbitrary CommRing coefficients. This is an expanded representation, not a mechanical edit to Roth.index. |
| P ≠ 0 | supports attainment in the given proof | Droppable: independently replayed nonzero proof plus direct zero branch. The old target is never called in that proof. |
| α | arbitrary center | No regularity or rationality needed. Remains in the Taylor translation and rootMultiplicity; cannot erase it without changing content. |
| r : σ→ℕ | nonnegative reciprocal scaling | No positivity premise occurs or is required. Zero-denominator case checked. Real nonnegative reciprocals would widen representation; arbitrary negative scaling is rejected by the native finite-support guard. |
| ℝ result | allows finite minimum and division | Zero convention deliberately maps empty support/infinite order to0. Replacing with unprojected infDegree at zero is false, checked natively. |

## Phase 4b — Generality verdict

STRICTLY NARROWER through one verified drop: hP. The all-polynomial conclusion is exactly the old conclusion with P arbitrary; [target source](../evidence/Roth.index_unique/index-unique-target-executed.lean.txt) and [complete receipt](../evidence/Roth.index_unique/index-unique-target-receipt.json) establish it cleanly. The proof independentNonzero copies the mathematical argument without calling index_unique; allPolynomials handles zero directly. The changed hypothesis therefore has positive evidence beyond syntactic non-use.

Expanded representation: `(P : Polynomial R) [CommRing R] (a : R) (r : ℕ)` with the Taylor-support minimum in ℝ. Coefficient-ring generality and the minimum normalization are independently checked in isolated mathlib-only evidence. Existing rootMultiplicity_eq_natTrailingDegree already states the essential generalized law. The existence of a droppable local premise does not make this a new upstream result.

## Phase 4c — All nine modern-idiom questions

| # | Diagnostic | Result / downstream consequence |
|---|---|---|
| 1 | Typeclasses | Already uses Unique and Fintype. Derive the latter locally; a new index class would contribute no inference or algebraic data. |
| 2 | Filters / nets | No topology or convergence. |
| 3 | Universal property | uniqueAlgEquiv and polynomial substitution already give the relevant free-algebra identifications. No new universal-property class needed. |
| 4 | Bundled substructures | No unbundled closure condition. Finite coefficient support and existing degree API are suitable. |
| 5 | Hierarchy weakening | Univariate CommRing coefficient version compiles; neither field, domain nor characteristic-zero is required. Avoiding ordinary factorial-normalized derivatives exposes positive-characteristic applications. |
| 6 | Higher category | Scalar equality, with no categorical morphism coherence data. |
| 7 | Concrete ordered codomain | Generic infDegree and trailingDegree retain infinity until explicit projection. Natural multiplicity suffices here; arbitrary negative weights fail to preserve least-exponent interpretation. |
| 8 | Concrete-via-abstract | Body contains no real-specific root theorem: ℝ appears zero times in the proof body; after setting q, the substantive argument uses its least nonzero coefficient and nonnegative scaling. The abstract minimum-support law is verified separately, and the root-multiplicity law already exists. Consequence: reuse the same order API for integer, finite-field and other CommRing polynomials. |
| 9 | False-generalization guard | Preserve projected zero and zero denominators. Native zero/top guard rejects unprojected infDegree=0; negative-scale guard on support{1,2} rejects arbitrary signed scaling. Hasse coefficients avoid the characteristic-p failure of ordinary derivatives. Unique cannot be replaced by a many-to-one variable collapse without an injectivity/no-cancellation argument. |

Modern idiom available: yes, rootMultiplicity/natTrailingDegree in Polynomial R and generic support infDegree, all existing mathematical objects. Their compatibility normalization is new evidence, not a newly discovered existing theorem. The move eliminates duplicated one-variable minimum reasoning and enables existing rootMultiplicity map, divisor-power and Taylor APIs in the only consumer.

## Phase 4.5 — Infrastructure risks

n/a — theorem kind. The six definition risks (typeclass diamonds, reducibility leak, noncanonical unfolding, instance priority, universe-polymorphism construction, coercion registration) do not apply to adding a proposition proof. No instance or coercion is introduced. Actual parameter/coercion/Fintype issues are addressed in4a and the native guard package.

## Phase 4.6 — All five proof-strategy questions

| # | Question | Assessment |
|---|---|---|
| 1 | ε–δ versus filters | n/a: finite algebra/order proof. |
| 2 | Elements versus subobjects | Coefficient inequalities are legitimate for the representation bridge; after bridge normalization, reuse the established root-multiplicity equality. No ideal bundle simplifies the denominator arithmetic. |
| 3 | Sequences versus nets | n/a: no limiting argument. |
| 4 | Construction versus universal property | Existing uniqueAlgEquiv already packages the single-generator algebra. |
| 5 | Missing helpful API | Taylor-support real minimum versus natTrailingDegree/r, and infDegree versus polynomial trailingDegree are useful normalization lemmas. The executed new minimumSupport proof is actual reasoning, not an existing-call theorem or an absence claim. |

Strategy verdict: REFACTOR-RECOMMENDED. Separate representation conversion from the existing univariate multiplicity law; use a local all-polynomial bridge while the project retains Roth.index. This is mathematical organization, not a cost downgrade. No proof-performance claim is made.

## Phase 5 — All five actual mathlib methods

[Complete formal requests and raw receipts](../evidence/Roth.index_unique/formal-search.json) cover 12 actual external/local calls, four methods on three forms. [Current source search](../evidence/Roth.index_unique/rg-current.json), [literature search](../evidence/Roth.index_unique/rg-literature.json), [abstract source search](../evidence/Roth.index_unique/rg-abstract.json) complete the fifth method on all forms.

| Method | Current spelling | Literature-standard law | Abstract support minimum |
|---|---|---|---|
| Finder | rootMultiplicity and irrelevant derivRootWeight; no direct project-index replacement | rootMultiplicity_eq_natTrailingDegree, shift law | natTrailingDegree_eq_support_min', trailingDegree |
| Loogle | uniqueAlgEquiv plus rootMultiplicity returned no items | rootMultiplicity_eq_natTrailingDegree and zero-center variant | infDegree, infDegree_withTop_some_comp, support-degree inequalities |
| LeanSearch | weightedOrder and adjacent derivRootWeight | exact rootMultiplicity_eq_natTrailingDegree | infDegree, trailingDegree |
| rg | No independent exact project spelling found | pinned RingDivision:133, Div:582 and Taylor expansion | pinned MonoidAlgebra Degree:624 and TrailingDegree:45–56 |
| local | rootMultiplicity family | natTrailingDegree family | infDegree and old scratch guard; scratch hit not a mathlib replacement |

All service receipts have isError=false; local search reports index unavailable, so missing local hits are not absence evidence. External versions can differ from the pin: positive candidate signatures and proofs are independently compiled against the local pin. No search failure proves absence.

**Positive hit:** `Polynomial.rootMultiplicity_eq_natTrailingDegree`, `Mathlib/Algebra/Polynomial/RingDivision.lean:133`:

```lean
{R : Type u} [CommRing R] {p : Polynomial R} {t : R} :
  p.rootMultiplicity t = (p.comp (Polynomial.X + Polynomial.C t)).natTrailingDegree
```

This is the re-aimed law, with no nonvanishing condition. Polynomial.taylor_apply converts composition to the Taylor spelling. The isolated exact existingReaim is `.symm` on that existing theorem. Polynomial.natTrailingDegree_le_of_ne_zero and coeff_natTrailingDegree_ne_zero prove the actual minimum normalization; generic infDegree alone does not magically supply this bridge.

## Phase 5.5 — All three statement-shape checks

Normal form: rootMultiplicity at a, natTrailingDegree of the Taylor translate, finite weighted support minimum, and generic infDegree are equivalent after specified projections. Existing univariate normal form is rootMultiplicity/natTrailingDegree; the project equality correctly puts rootMultiplicity/r on the RHS. Keep bridges to this form instead of pairwise equivalences among every alternative presentation.

Syntactic generality: allPolynomials removes the explicit hP argument; the full caller replay changes `rw [index_unique nonzeroProof, ...]` to `rw [allPolynomials, ...]`, with no new premise. Its existing hR is still needed by the later arithmetic estimate and is retained. Native uniqueProvidesFinite has no Fintype binder: Unique.fintype is inferred automatically at the index interface.

Superfluous-argument audit: hP removable; Fintype redundant as caller-supplied data but present in the fixed index type; Unique required for default/univariate equivalence; σ already arbitrary universe; P,α,r all mathematically substantive; no positivity, domain, characteristic-zero or DecidableEq parameter is silently introduced. Coefficient generality requires restating the parent representation. Overall RESTATE-BEFORE-SHIP for a local API cleanup: remove hP and derive finite data where desired. The existing upstream law already has the appropriate nonvanishing-free statement.

## Phase 6.0 — Complete callers and inline audit

[Canonical lexical enumeration](../evidence/Roth.index_unique/lexical-enumeration.json), [fresh no-ignore rg](../evidence/Roth.index_unique/caller-rg.json), [tracked git grep](../evidence/Roth.index_unique/caller-git-grep.json), [full caller inventory](../evidence/Roth.index_unique/callers.json), and [inline search](../evidence/Roth.index_unique/rg-inline.json) agree. There are three lexical occurrences: a module-doc mention, the declaration, and one proof application. Internal use count 1; external-to-declaring-file files 1; statement applications 0; proof applications 1.

| Caller | Actual use | Refactor |
|---|---|---|
| Roth/Theta.lean:242, private Roth.index_unique_le_log_div beginning223 | `rw [index_unique ((map_ne_zero_iff _ (map_injective _ Int.cast_injective)).2 hR), hmapeq, hmult]` | Use all-polynomial bridge with inferred arguments, then the unchanged map/multiplicity/log estimates. Complete original body replayed, with no DecidableEq σ binder. |

Inline-derivation grep: no independent copy of the same weighted-index/root-multiplicity equality found elsewhere. Theta's power-root-divisibility and multiplicity map formulas are different statements; Θ_unique_le uses this private consumer, not another direct application. Source and direct-kernel counts happen to agree at1; this does not identify the transitive closure or prove deadness.

## Phase 6 — Actual composition experiments

1. Unchanged project statement: rfl and a closing `simp only [index]` both fail in the accepted negative probe; independentNonzero proves it by the genuine coefficient argument. **NOT-COMPOSABLE** in≤3 existing mathlib calls with the original definitions. Project index/weight and Hasse bridges do not count as mathlib calls.
2. Independent weakening: allPolynomials splits P=0 and otherwise uses the independently proved body. This is new checked local proof, not a claimed existing replacement.
3. Mathlib-only normalization: minimumSupport identifies real sInf of n/r over polynomial support with natTrailingDegree/r, including P=0 and r=0. taylorMinimum then identifies it with rootMultiplicity/r using the actual existing theorem and taylor_apply. These proofs are archived as new normalization, not hidden inside a call count.
4. Re-aimed canonical statement: `(P.comp (X+C a)).natTrailingDegree = P.rootMultiplicity a` follows in one call, `Polynomial.rootMultiplicity_eq_natTrailingDegree.symm`. The generic infDegree/trailingDegree bridge verifies the connection to the parent index's already assessed abstraction. In particular realInfSupport computes the projected WithTop ℝ infDegree with weight n/r as natTrailingDegree/r for all P and r, and realRootInf performs the translated root comparison. These are actual new bridge proofs; their existence is not attributed to mathlib.
5. Full consumer replay and zero/Fintype/signed-weight/infinite-zero guards compile with standard axioms; no old index_unique use closes a replacement proof.

The parent index was assessed NO-mathlib-has-it because infDegree is more general. Under ModeB's explicit re-aim rule, this dependent law is NO-mathlib-has-it once its analogous canonical law and representations are independently checked. The old-form count remains honest; this is not NO-composable-from-mathlib and not automatic NO because a simp expansion happened to close.

## Phase 7 — Verdict and actionable destination

**NO-mathlib-has-it, re-aimed to Polynomial.rootMultiplicity_eq_natTrailingDegree.** The existing theorem already identifies multiplicity with the minimum Taylor exponent over any CommRing, including the zero polynomial. Its minimum is precisely the one-variable instance of the parent's support-infimum construction. Independent normalization and old-body replays supply the representation evidence; they are not passed off as pinned declarations.

The one-call canonical example, actually executed in isolated mathlib-only context, is:

```lean
example {R : Type u} [CommRing R] (P : Polynomial R) (a : R) :
    (P.comp (Polynomial.X + Polynomial.C a)).natTrailingDegree = P.rootMultiplicity a :=
  Polynomial.rootMultiplicity_eq_natTrailingDegree.symm
```

Existing building blocks are rootMultiplicity_eq_natTrailingDegree in RingDivision:133; taylor_apply in Polynomial/Taylor; natTrailingDegree support/coefficient laws in Polynomial/Degree/TrailingDegree; uniqueAlgEquiv in MvPolynomial/Equiv; finite infimum facts in ConditionallyCompleteLattice/Finset. The unmodified old formula is not a one-line application of the displayed theorem. Refactor plan for the sole explicit caller at Theta242: move its index expression through one documented local representation bridge, rewrite the resulting univariate natTrailingDegree by the existing theorem (or use the checked all-polynomial bridge while retaining the local index name), then keep hmapeq, hmult and all later log arithmetic. Drop the nonzero proof argument supplied solely to index_unique; retain hR for pow_rootMultiplicity_le. The complete native caller replay verifies these argument-flow details.

Alternative destination: retain the all-polynomial compatibility bridge in project-local Roth/Index.lean while the project uses its real-valued normalized index. It is useful local API, not junk, despite its single explicit consumer. A future generic support-minimum compatibility lemma can be considered separately in mathlib; it is not a reason to add a second project-index multiplicity theorem upstream. If migrating the parent index API fully, delete index_unique only after moving this consumer to the normalized representation and updating the module-doc mention. No production refactor is performed by this read-only assessment. No new upstream PR, reviewer, or YES grouping is proposed for an already existing canonical law.

## Phase 8 — Handoff

Accepted [full caller and guard source](../evidence/Roth.index_unique/index-unique-callers-guards-clean-executed.lean.txt) and [clean receipt](../evidence/Roth.index_unique/index-unique-callers-guards-clean-receipt.json) verify the complete consumer and five convention/generality exercises. The initial [guard attempt](../evidence/Roth.index_unique/index-unique-callers-guards-initial-executed.lean.txt) and [rejected receipt](../evidence/Roth.index_unique/index-unique-callers-guards-initial-receipt.json) retain the unavailable Fintype.ofUnique name and unused-section warnings; they are not accepted proof evidence. The corrected source infers Unique.fintype automatically. The [isolated mathlib source](../evidence/Roth.index_unique/index-unique-mathlib-executed.lean.txt) and [complete receipt](../evidence/Roth.index_unique/index-unique-mathlib-receipt.json) verify minimumSupport, taylorMinimum and exact existingReaim against the pin.

The [complete canonical normalization source](../evidence/Roth.index_unique/index-unique-infdegree-executed.lean.txt) and [clean receipt](../evidence/Roth.index_unique/index-unique-infdegree-receipt.json) separately verify trailingInf, rootInf, finsetBridge, realInfSupport and realRootInf. The [initial canonical attempt](../evidence/Roth.index_unique/index-unique-infdegree-initial-executed.lean.txt) and [rejected receipt](../evidence/Roth.index_unique/index-unique-infdegree-initial-receipt.json) retain three HDiv ℝ ℕ inference errors and recovered elaboration sorryAx artifacts. The clean source supplies explicit real denominator/codomain casts; none of the initial recovery artifacts count as accepted proof evidence.

The [collapse guard](../evidence/Roth.index_unique/index-unique-collapse-executed.lean.txt) and [clean native receipt](../evidence/Roth.index_unique/index-unique-collapse-receipt.json) additionally verify that X₀−X₁ is nonzero before both variables are renamed to the same Unit variable, where it becomes0. This confirms the cancellation obstruction behind the Unique restriction. The [fresh full lake build receipt](../evidence/Roth.index_unique/index-file-completion-2026-10-27.json) and [complete log](../evidence/Roth.index_unique/index-file-completion-2026-10-27.log) establish the final Index-module completion build: exit 0, 2467 jobs, 15.178 seconds, zero warnings/errors, with unchanged source/pin hashes.

All phases complete, verification unresolved=[], root acceptance pending. The package preserves original, canonical293, target-independent weakening, all explicit caller replay, isolated mathlib normalization, false-generalization guards, full-build evidence and raw receipts. [Assessment](../evidence/Roth.index_unique/assessment.json), [verification](../evidence/Roth.index_unique/verification.json), [overview entry](../evidence/Roth.index_unique/overview-entry.json), [current manifest](../evidence/Roth.index_unique/copy-manifest.json) and [portable validator](../evidence/Roth.index_unique/validate.py) are the review artifacts. The validator checks exact source/receipt pairs, complete native success, scoped new-region audit markers, standard axioms, all17 source/pin hashes, pinned candidate hashes, canonical name order, sole caller source/body, full-build status, manifest bytes/hashes, all phase/search coverage, links and the credential guard. The current manifest is authoritative; historical worker-copy-manifest cannot replace validation of current artifacts.
