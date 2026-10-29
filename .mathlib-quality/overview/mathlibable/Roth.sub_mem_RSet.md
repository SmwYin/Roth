# `Roth.sub_mem_RSet` — canonical250

**Assessment verdict: BORDERLINE-needs-human.** The elementary interval-diameter estimate is existing mathlib API. The complete nonzero/coordinate-degree/coefficient family-membership result is a new assembly of those facts, with a project-specific source and destination family. Keep the lemma local while deciding whether a generic coefficient-family API warrants upstreaming. This is a completed assessment; the future upstream design questions are not blockers to the overview.

## Phase0 — baseline and source integrity

The target is the public theorem at `Roth/MainLemma.lean:388`. All17 production-source/pin hashes were freshly compared with the shared successful2467-job baseline. Production Lean and pins were unchanged. The accepted file-end full build at canonical228 is reused; the assignment requires no new file-end build at250. The entire MainLemma module and its sole caller's continuation were read. The original full-module scratch replay renames only the target inside a fresh namespace; all293 canonical audit names come directly from tracked declaration order, including the correct private-module names. Preparation and freeze-time canonical checks must pass before acceptance.

Evidence: [fresh17](../evidence/Roth.sub_mem_RSet/inputs.json), [baseline](../evidence/Roth.sub_mem_RSet/baseline-build.txt), [full source](../evidence/Roth.sub_mem_RSet/source-MainLemma.lean.txt), [original exact replay](../evidence/Roth.sub_mem_RSet/original-executed.lean.txt), [complete native result](../evidence/Roth.sub_mem_RSet/original-final-receipt.json), [canonical consumers](../evidence/Roth.sub_mem_RSet/canonical-consumers.json).

The first original-source native request warmed the persistent document and returned partial=true/success=false; it is not accepted verification. The follow-up returned success=true, partial=false, no errors/warnings, only standard axioms, and requested=unique=present=values=293. The native target body printer returned the complete body without elision. One rejected isolated boundary-test batch had an unsolved constant-degree simplification and an unused simp argument; it is preserved separately, including its recovered sorryAx, and is not accepted evidence. The corrected batch uses `degreeOf_C` explicitly and passes without errors, warnings, or sorryAx. Source-level dependencies, direct kernel constants, canonical consumers, and uncomputed transitive/simp closure are distinguished below.

## Phase1 — comprehension

Take two distinct integer multivariate polynomials whose degree in coordinate `j` is at most `r j`, and whose coefficients all lie in `[0,B]`. Their difference is nonzero, has the same coordinate-degree bounds, and every coefficient has absolute value at most **B**. The last conclusion uses the diameter of the original coefficient interval; replacing it by the triangle-inequality bound2B loses the content needed by this construction.

Full native type, obtained through `Lean.getConstInfo` with `pp.funBinderTypes=true`:

```lean
∀ {σ : Type u_1} {r : σ → ℕ} {B : ℕ} {W' W'' : MvPolynomial σ ℤ},
  W' ∈ Roth.boxFamily r B → W'' ∈ Roth.boxFamily r B → W' ≠ W'' →
    W' - W'' ∈ Roth.RSet (↑B) r
```

Here σ is an arbitrary universe-polymorphic variable type, r consists of natural coordinate bounds, B is a natural coefficient bound, and W′/W″ are integer polynomials. There are no Fintype, finite-support, positivity-of-degree, positivity-of-B, root, derivative, or divisibility assumptions. The proof combines `sub_ne_zero`, `MvPolynomial.degreeOf_sub_le` followed by `max_le`, and the generated mathlib theorem `abs_sub_le_of_nonneg_of_le`, after `MvPolynomial.coeff_sub` and integer-to-real cast transport. The source body names no other project theorem: `boxFamily` and `RSet` occur in the statement and are unfolded by elaboration.

Evidence: [native type](../evidence/Roth.sub_mem_RSet/native-type.json), [target source](../evidence/Roth.sub_mem_RSet/target-excerpt.lean.txt), [dependency scopes](../evidence/Roth.sub_mem_RSet/dependencies.json).

## Phase2 — preliminary checks

**SMALL:** an elementary helper in the auxiliary-polynomial construction, not a named main result or a new structure. The definition-only one-line test is **n/a: theorem**, even though its arithmetic core is short. Neither proof length nor its parent's utility determines the verdict.

## Phase3 — exhaustive literature

The exact requests, response UTF-8 hashes/byte counts/status/timings, clean titles/URLs/locators, and original concise summaries are archived. Full article/search-result bodies are not retained. Search snippets establish context, not unverified theorem equivalence. Long rows that were article text rather than clean titles were omitted explicitly.

| Channel | Actual query or locator | Outcome and role |
|---|---|---|
| General specific | `Roth theorem auxiliary polynomial difference nonnegative coefficients bounded B pigeonhole` | Bounded integer coefficient boxes and subtraction occur in auxiliary-polynomial proofs; [receipt](../evidence/Roth.sub_mem_RSet/web-general1.json). |
| General broader | `polynomials coefficients in interval diameter difference height bound Siegel lemma` | Small-height polynomial and Siegel-lemma context; [receipt](../evidence/Roth.sub_mem_RSet/web-general2.json). |
| General aliases | `box principle difference integer polynomials height bounded coefficients auxiliary polynomial` | Box principle and height terminology; no separate canonical combined membership law established; [receipt](../evidence/Roth.sub_mem_RSet/web-general3.json). |
| ChatGPT mathematics | Optional `ask_chatgpt_math` unavailable | Justified n/a; other channels were not reduced. |
| Local references | `clean.tex`, §6, Lemma9 proof, coefficient box through W*=W′−W″ | Exact mathematical role: distinctness gives nonzero and interval diameter gives B; [input/excerpt](../evidence/Roth.sub_mem_RSet/literature-local-excerpt.txt). |
| nLab | `site:ncatlab.org/nlab interval diameter ordered abelian group` | Ordered-group and interval context; no exact combined polynomial theorem; [receipt](../evidence/Roth.sub_mem_RSet/web-nlab.json). |
| distinct nCatLab | `site:ncatlab.org/ncatlab bounded diameter additive group interval` | Actual separate namespace query; returned nLab/out-of-namespace material is not counted as a positive nCatLab theorem; [receipt](../evidence/Roth.sub_mem_RSet/web-ncatlab.json). |
| Stacks | `site:stacks.math.columbia.edu polynomial coefficient height bounded difference` | Height exercises and polynomial context, not this combined statement; [receipt](../evidence/Roth.sub_mem_RSet/web-stacks.json). |
| MathOverflow | `site:mathoverflow.net Siegel lemma polynomial coefficients pigeonhole height` | Versions of Siegel's lemma and height estimates; no packaged family-membership result established; [receipt](../evidence/Roth.sub_mem_RSet/web-mathoverflow.json). |
| recent arXiv | `site:arxiv.org Roth auxiliary polynomial coefficient height pigeonhole after:2021-10-29 before:2026-10-30` | Mostly proof-complexity and additive-combinatorial Roth results; distinguish those from irrationality Roth; [receipt](../evidence/Roth.sub_mem_RSet/web-arxiv.json). |
| recent arXiv refined | `site:arxiv.org "Siegel" "lemma" "height" after:2021-10-29 before:2026-10-30` | Empty returned results; not a mathematical absence claim; [receipt](../evidence/Roth.sub_mem_RSet/web-arxiv-refined.json). |
| supplementary primary exposition | Milojevic, January2022, Lemma4.3, pp6–7, returned lines935–966 | Subtracting two vectors in a symmetric box gives twice the radius. This supports the diameter principle while explaining why our nonnegative interval gives B; [access](../evidence/Roth.sub_mem_RSet/web-primary.json), [specific locator](../evidence/Roth.sub_mem_RSet/web-primary-detail.json). |

Concept: **coefficient-box subtraction / interval diameter**, used in the pigeonhole proof of Siegel-type auxiliary-polynomial existence. The literature has scalar interval diameter and finite-dimensional coefficient-vector formulations. The current theorem already goes beyond the finite-variable presentation by allowing arbitrary σ and arbitrary r. The literature does not establish a separately named universal nonzero-degree-height tuple as a standard independent theorem. Its broader coefficient-level content is already provided by mathlib's ordered-group theorem. This supports a local packaging/design judgment, not a novelty-by-search-failure claim.

Primary context: [An elementary approach to Roth's theorem](https://aleksa-milojevic.github.io/expository/roth.pdf), Lemma4.3. No external mathematical source is treated as proof that an existing Lean declaration matches the whole tuple.

## Phase4a–4b — generality and boundary checks

| Parameter / premise | Mathematical role and tested interpretation |
|---|---|
| σ : Type* | Already arbitrary, including Empty and infinite types. No finiteness or support-of-r assumption can be dropped because none is present. |
| r : σ→ℕ | Arbitrary coordinate bounds, including all-zero bounds. Constants give nontrivial examples with all r=0 and infinitely many variables; positivity would be an unnecessary restriction. |
| B : ℕ | Integrality/nonnegativity encodes the project's counting interface. The scalar diameter law works for arbitrary ordered-group bounds; changing this parameter alone does not generalize the fixed-ℤ `boxFamily` and real-valued `RSet` interfaces. |
| W′, W″ : MvPolynomial σ ℤ | The proof uses a commutative ring for polynomial subtraction/degree API and ordered additive structure for interval diameter; not integer arithmetic itself. A fresh generic theorem over a linearly ordered commutative ring compiles independently; this is new proof, not existing mathlib replacement API. |
| h′.1 and h″.1 | Both degree bounds feed `max_le`. Dropping a bound permits `X` against zero with r=0. |
| h′.2 and h″.2 lower bounds | Both are needed for the sharper B. Without nonnegativity, coefficients1 and−1 both have upper bound1 but their difference has magnitude2. |
| h′.2 and h″.2 upper bounds | Nonnegative coefficients alone are unbounded:2 and0 violate bound1. Each operand's upper bound is relevant. |
| hne | Exactly equivalent to the difference being nonzero; equality forces the zero difference. Removing it would change membership in the nonzero destination family. |
| B=0 | Every source polynomial is zero by coefficient extensionality; no distinct source pair exists. The theorem is vacuous there, and does not need B>0. |
| empty σ / zero support | Constants survive. For B>0, C B and0 are distinct and attain coefficient magnitude B, even with zero coordinate bounds. No false sharpness claim at B=0. |

Verified expanded restatement:

```lean
theorem interval_sub {σ R : Type*} [CommRing R] [LinearOrder R] [IsOrderedAddMonoid R]
    {r : σ → ℕ} {lb ub : R} {p q : MvPolynomial σ R}
    (hp : (∀ j, degreeOf j p ≤ r j) ∧ ∀ d, lb ≤ p.coeff d ∧ p.coeff d ≤ ub)
    (hq : (∀ j, degreeOf j q ≤ r j) ∧ ∀ d, lb ≤ q.coeff d ∧ q.coeff d ≤ ub)
    (hne : p ≠ q) : p - q ≠ 0 ∧ (∀ j, degreeOf j (p - q) ≤ r j) ∧
      ∀ d, |(p - q).coeff d| ≤ ub - lb
```

The independent proof, integer specialization, scalar counterexamples, B0 result, empty-variable sharp constant, all-zero degree example, and original project-signature recovery are archived as [mathlib-only proofs](../evidence/Roth.sub_mem_RSet/isolated-executed.lean.txt) and [project recovery](../evidence/Roth.sub_mem_RSet/recovery-executed.lean.txt). This preserves B, not2B. The generic all-coefficients interval may be empty when its lower endpoint excludes zero; no unwarranted nonemptiness is claimed.

A further verified `sized_set_sub` parameterizes coefficient sets S(d), size : R→ℝ, and supplied pairwise diameter bounds B(d). It uses no order on R, so valuations or seminorms can supply size. This is a genuine semantic coefficient-range parameter with user-supplied diameter evidence. It does not assert every seminorm ball of radius B has diameter B: symmetric balls typically have diameter2B. No normed-ring specialization is claimed compiled merely from naming that application.

**Generality verdict:** the written statement is maximally general within its fixed project families; a strictly broader representation has been proved. It is not a mechanical hypothesis drop: changing the foundational coefficient family/target representation is the substantive API decision. Therefore the verified broader theorem does not automatically force YES-but-generalise-first. Cost is not the reason for this routing.

## Phase4c — all nine modern-idiom checks

| # | Question | Answer and downstream consequence |
|---|---|---|
| 1 | Typeclasses replace preambles? | No new instance for membership/distinctness; these are data-dependent propositions. Generic coefficient algebra/order uses existing classes. |
| 2 | Sequences/metrics become filters? | No; pointwise finite-support algebra, with no limits. |
| 3 | Construction becomes universal property? | No; subtraction already is the canonical ring operation. |
| 4 | Predicate becomes bundled substructure? | No: `[0,B]` coefficient boxes are not closed under subtraction or addition, and nonzero RSet excludes zero. A Submodule would change the object. |
| 5 | Weaken hierarchy? | Yes in an expanded statement: no field/domain or finite-type structure is needed; generic ordered commutative rings suffice. `degreeOf_sub_le` is already generic. |
| 6 | Higher categorical restatement? | No categorical data or coherence issue. |
| 7 | Concrete numeric index generalized? | σ already arbitrary and r already semantic. B is a bound, not a hardcoded numeral. Coefficient interval endpoints can be semantic parameters with diameter ub−lb. |
| 8 | Concrete-via-abstract diagnostic? | Fires: source body contains boxFamily=0, RSet=0, ℤ=0 explicit occurrences; `Int.cast_abs` is a representation bridge. The proof works only with degree and coefficient-range properties. `interval_sub` and `sized_set_sub` demonstrate the abstraction; the project theorem is recovered with its original signature. |
| 9 | False-generalization guard? | The interval and supplied-diameter restatements preserve the sharp bound and nonzero condition under specialization. Rejected alternatives: bare coefficient norm≤B implies only2B; dropping distinctness includes zero; a Submodule changes the bounded nonzero family. |

Modern idiom available in an expanded representation: yes. It enables nonintegral ordered coefficients and arbitrary coefficient sets with diameter certificates, and composes with `abs_sub_le_of_le_of_le`, `coeff_sub`, `degreeOf_sub_le`. Whether the full conjunction should itself be upstream API remains the design issue. A new generic helper proved here is never described as already in mathlib.

## Phase4.5 — six infrastructure risks

| Risk | Status and reason |
|---|---|
| Typeclass diamond | n/a: theorem; adds no instance path. |
| Reducibility leak | n/a: theorem; no data reduction equation. |
| Non-canonical unfolding | n/a: theorem; introduces no definitional normal form. |
| Instance priority collision | n/a: theorem; registers no instance. |
| Universe-polymorphism issues | n/a: theorem infrastructure risk; the existing universe-polymorphic type is separately retained and signature-checked. |
| Coercion ambiguity | n/a: theorem; registers no coercion. |

Overall n/a. These labels do not assess the parent definitions' infrastructure risk.

## Phase4.6 — all five proof-strategy checks

| # | Question | Result |
|---|---|---|
| 1 | ε–δ versus filters | No topology. |
| 2 | Elements versus substructure inclusions | Coefficientwise argument is appropriate: bounded coefficient families lack additive closure. A set image/subtraction inclusion can describe the result but does not eliminate arithmetic. |
| 3 | Sequences versus nets | No convergence. |
| 4 | Construction versus universal property | Canonical subtraction, no universal-property replacement needed. |
| 5 | Missing helper that should exist | Scalar interval diameter already exists, including generated additive names. A combined bounded-polynomial-family subtraction helper is a possible API proposal; existing evidence does not establish demand outside this construction. |

**MATHLIB-IDIOMATIC** for the current local statement. Generic coefficient-family organization is optional future API design, not a tactic/performance or proof-cost argument.

## Phase5 — all15 formal-search cells and pinned candidates

| Form | Finder | Loogle | LeanSearch | rg | local name/index |
|---|---|---|---|---|---|
| current nonzero integer box difference | [receipt](../evidence/Roth.sub_mem_RSet/search-current-leanfinder.json) | [receipt](../evidence/Roth.sub_mem_RSet/search-current-loogle.json) | [receipt](../evidence/Roth.sub_mem_RSet/search-current-leansearch.json) | [receipt](../evidence/Roth.sub_mem_RSet/search-current-rg.json) | [receipt](../evidence/Roth.sub_mem_RSet/search-current-local_search.json) |
| standard ordered interval diameter | [receipt](../evidence/Roth.sub_mem_RSet/search-standard-leanfinder.json) | [receipt](../evidence/Roth.sub_mem_RSet/search-standard-loogle.json) | [receipt](../evidence/Roth.sub_mem_RSet/search-standard-leansearch.json) | [receipt](../evidence/Roth.sub_mem_RSet/search-standard-rg.json) | [receipt](../evidence/Roth.sub_mem_RSet/search-standard-local_search.json) |
| abstract coefficientwise difference/support | [receipt](../evidence/Roth.sub_mem_RSet/search-abstract-leanfinder.json) | [initial](../evidence/Roth.sub_mem_RSet/search-abstract-loogle.json), [corrected retry](../evidence/Roth.sub_mem_RSet/search-abstract-loogle-retry.json) | [receipt](../evidence/Roth.sub_mem_RSet/search-abstract-leansearch.json) | [receipt](../evidence/Roth.sub_mem_RSet/search-abstract-rg.json) | [receipt](../evidence/Roth.sub_mem_RSet/search-abstract-local_search.json) |

All15 cells were actually invoked. Abstract Loogle initially rejected the unquoted coefficient name; the quoted-name retry returned `MvPolynomial.coeff_sub`. The local tool returned index=error in all three cells, including positive source-backed name hits. An empty local result proves no absence. External search snapshots can differ from the project pin. An untruncated [exact-name source search](../evidence/Roth.sub_mem_RSet/full-name-search.json) has no hit; no semantic absence conclusion follows from that alone.

Pinned positive building blocks, signatures checked in the accepted isolated source:

- `MvPolynomial.degreeOf_sub_le`, `Mathlib/Algebra/MvPolynomial/CommRing.lean:132`: degree of p−q at j ≤ max of the two degrees.
- `MvPolynomial.coeff_sub`, same file:72: coefficient of the difference equals coefficient difference.
- `sub_ne_zero`: difference nonzero iff operands differ, under additive-group assumptions.
- `abs_sub_le_of_nonneg_of_le`: generated by `@[to_additive]` from `mabs_div_le_of_one_le_of_le`, `Mathlib/Algebra/Order/Group/Abs.lean:125`.
- `abs_sub_le_of_le_of_le`: generated from `mabs_div_le_of_le_of_le`, same file:196; applies over linearly ordered additive commutative groups and gives ub−lb.
- `max_le`, order transitivity and `Int.cast_abs`/cast transport finish the family tuple.

The generated additive theorems are exactly why lexical failure alone is unreliable. Sources and hashes: [mathlib inputs](../evidence/Roth.sub_mem_RSet/mathlib-inputs.json). Search conclusion: existing scalar/generic polynomial building blocks verified; no search hit verified for the full family-membership tuple. This is weaker and more accurate than asserting universal API absence.

## Phase5.5 — statement shape

**Normal form:** compare project family membership, an explicit nonzero-degree-absolute-coefficient tuple, a coefficient-interval statement, and a set-difference inclusion. `RSet` is the project normal form; the generic coefficient statement uses ordinary polynomial operations. No orthogonal iff maze is introduced. RHS convention is n/a for this implication.

**Syntactic generality:** the tuple/interval form and arbitrary coefficient-set diameter form were actually proved. The original membership form remains easiest for the sole caller: it immediately projects hP.1, hP.2.1 and the height bound. The full caller was separately inlined, retaining its original signature. There is no claim that replacing parent definitions is a definitional bridge with no proof work.

**Superfluous-argument audit:** σ, r, B and the two polynomial parameters each determine the output; both degree hypotheses and both coefficient intervals are used; distinctness is essential for nonzero. No Fintype/DecidableEq/finite-support assumption is hidden in the target's native type. B>0 is deliberately absent and B0 is vacuous. Overall **SHIP-AS-STATED locally; RESTATE-BEFORE-SHIP if an upstream coefficient-family API is chosen**.

## Phase6.0 — complete callers and inline audit

Fresh `rg --no-ignore` scoped to production and `git grep` agree: one actual proof use, within the declaring module; zero external-to-file uses, so the command's internal-use-count excluding declaring file is0. The canonical293 runtime scan independently gives one direct kernel-value consumer and no direct type consumers. These are separate scopes, despite agreeing here.

| Actual caller | Usage and every required retained conclusion |
|---|---|
| private `Roth.exists_mem_RSet_le_index_aux`, `Roth/MainLemma.lean:550`, call at560 | After obtaining a distinct pair with equal selected remainders, `have hP := sub_mem_RSet hW' hW'' hne`. It returns W′−W″ with hP membership, uses hP.1 to prove the mapped polynomial nonzero, and hP.2.1 to transfer coordinate degree bounds before applying the Hasse vanishing/index criterion. |

Its continuation feeds the rpow-bound helper, then the logarithmic-bound helper, the auxiliary-polynomial construction, and `main_lemma`. Those are transitive users, not additional direct callers. The theorem has no simp attribute. No claim is made about full transitive kernel or implicit simp closure. The fresh inline-derivation search found no independent rederivation of this same complete tuple elsewhere.

The [full actual module with the target removed and its proof inlined at the sole caller](../evidence/Roth.sub_mem_RSet/inline-executed.lean.txt) compiles with unchanged caller signature. Kernel-value inspection confirms the new caller does not retain a reference to `Roth.sub_mem_RSet`. The inlined continuation through `main_lemma` is preserved, not replaced with a schematic caller example. [Caller receipt](../evidence/Roth.sub_mem_RSet/inline-receipt.json), [lexical caller record](../evidence/Roth.sub_mem_RSet/callers.json), [fresh source search](../evidence/Roth.sub_mem_RSet/source-search.json), [tracked cross-check](../evidence/Roth.sub_mem_RSet/tracked-source-search.json).

## Phase6 — actual composition experiments

1. The scalar height estimate alone is one existing call after coefficient normalization: `abs_sub_le_of_nonneg_of_le`. It does not establish nonzero or coordinate degree bounds.
2. `degreeOf_sub_le` plus `max_le` and transitivity proves only the degree component. `sub_ne_zero` proves only nonzero. Combining those with `coeff_sub`, interval diameter and cast transport constructs the tuple. This is the actual full proof, not one existing call or a ≤3-call replacement; conjunction projections/constructors are not counted as mathematical calls, but the polynomial/order/cast steps still exceed the threshold.
3. The accepted isolated experiment checks that a restricted `simp only [coeff_sub, sub_ne_zero]` does not close the full statement, then proves it with the identified building blocks. This is a bounded negative route, not a universal no-proof certificate or a claim based on a failed broad search.
4. A newly written `interval_sub` recovers the integer tuple and the original project theorem with signature equality. It is new generic proof content; calling it does not make it an existing-mathlib composition.
5. Inlining the original proof in the full actual caller succeeds and preserves its signature. That proves a concrete local refactoring is possible, not that the original is a ≤3-call wrapper.

**NOT-COMPOSABLE** under the command's strict existing-mathlib ≤3-call criterion. No closing `simp [defs]` proof is claimed. This rules out an automatic NO-composable verdict, while one caller and the lack of an independently established standard combined theorem leave the upstream packaging question open.

## Phase7 — verdict and actionable disposition

**BORDERLINE-needs-human**, independently assessed; neither boxFamily233 nor RSet179's verdict is inherited. The exact scalar diameter result already exists in mathlib and is genuinely more general than integer arithmetic. Nevertheless, it is not an analogous full nonzero/degree/height law for an existing replacement of both project families, so the re-aim gate does not establish NO-mathlib-has-it for this complete theorem. The original theorem contains useful project packaging, and a verified representation-independent proof exists. What remains unsettled is whether that full conjunction is the right reusable upstream surface.

Future upstream questions, each answerable concretely:

1. Should a bounded coefficient-family API expose subtraction with a supplied diameter certificate, or should polynomial users combine `coeff_sub` with the existing scalar diameter theorem at their own call sites?
2. If an interval-coefficient polynomial API is adopted, should the nonzero conclusion be a separate corollary of `sub_ne_zero`, keeping the primary API a subtraction inclusion with degree and coefficient bounds?
3. Does a second intended mathlib consumer need the complete degree-plus-coefficient tuple, supporting a home near `Mathlib/Algebra/MvPolynomial/CommRing.lean`, or should this combined lemma remain in the Roth auxiliary-polynomial module?

These questions concern a future upstream proposal. No user response is required to finish this read-only assessment. Current recommendation: **retain `Roth.sub_mem_RSet` in `Roth/MainLemma.lean` as a local construction helper**. If local API minimization is chosen, the verified inline source gives the exact refactor at its sole private caller: replace `have hP := sub_mem_RSet ...` with the explicit nonzero/degree/interval-diameter tuple and remove this theorem; no downstream signature needs changing. Do not substitute a 2B bound.

## Overview synthesis and moral duplication

| Pair | Same statement? | Same proof? | Decision |
|---|---|---|---|
| sub_mem_RSet / abs_sub_le_of_nonneg_of_le | No; only coefficient arithmetic overlaps | Scalar leaf is exactly existing API | Reuse scalar theorem; no claim it packages full membership. |
| sub_mem_RSet / degreeOf_sub_le | No; degree component only | Same degree leaf | Existing generic building block, not duplicate of full theorem. |
| sub_mem_RSet / sub_ne_zero | No; nonzero component only | Same nonzero leaf | Distinctness is essential, no duplicated new algebra. |
| sub_mem_RSet / new interval_sub | Original is a specialization after project-family and cast bridge | Generic proof has same three components | New scratch helper; potential future API, not existing-mathlib evidence. |
| sub_mem_RSet / norm_coeff_modByMonic_le | No; remainder-elimination norm growth versus one interval-difference step | Different mathematical arguments | Do not unify merely because both bound coefficients. |

Mathlib API audit: use existing generated scalar interval results and canonical polynomial subtraction API. Generalization: arbitrary ordered coefficients/endpoints or supplied coefficient-set diameter preserves the sharp B and makes integrality a specialization. Missing API: possible combined coefficient-family subtraction inclusion, subject to the three questions. Junk: not dead; one actual proof consumer and transitive use by the main theorem, with verified optional inlining. Parent-family redesign is a separate task, not performed here. Production files and import prefixes remain unchanged.

## Phase8 — verification and handoff

The portable [validator](../evidence/Roth.sub_mem_RSet/validate.py) validates the **current** copy manifest, both scratch and simulated-integrated layouts, all17 hashes, exact293 source order and runtime presence/value counts, all15 formal cells, every literature channel, clean accepted native results and standard axioms, full caller signature retention, links, secret guard and required overview-entry keys. Historical worker manifests do not replace current validation. Root acceptance is pending independent review.

Evidence controls: [verification](../evidence/Roth.sub_mem_RSet/verification.json), [preparation checks](../evidence/Roth.sub_mem_RSet/preparation-checks.json), [assessment](../evidence/Roth.sub_mem_RSet/assessment.json), [final validator results](../evidence/Roth.sub_mem_RSet/final-validation.json).
