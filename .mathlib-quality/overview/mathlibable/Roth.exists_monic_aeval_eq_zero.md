# Roth.exists_monic_aeval_eq_zero — canonical272

**Verdict: BORDERLINE-needs-human.** The mathematical generalization is verified: any integral element over a nontrivial commutative ring has monic annihilators above every natural degree cutoff. There is also a semiring version from a supplied monic annihilator. Whether this elementary padding operation merits a named upstream existence lemma, or should stay a local construction, remains an API judgment. This is a completed read-only assessment with three concrete future upstream questions, not a user blocker or a cost-based verdict. No earlier verdict is inherited.

## Phase0 — Baseline and exact scope

The theorem resolves at `Roth/Main.lean:142–147`. The declaring module proves Roth's theorem by reduction to integral real numbers, choosing parameters and approximants, and comparing lower and upper polynomial evaluation bounds. The entire Main module and actual downstream LeanEval module were read. Fresh hashes of all17 sources/pins match the tracked shared manifest, permitting reuse of the clean2467-job baseline and accepted fileendTheta228 build. No literal fileend build is due at272; next boundary is289. Sources, pins, project imports and production declarations remain unchanged.

[Input hashes](../evidence/Roth.exists_monic_aeval_eq_zero/inputs.json), [baseline](../evidence/Roth.exists_monic_aeval_eq_zero/baseline-build.txt), [full Main](../evidence/Roth.exists_monic_aeval_eq_zero/source-Main.lean.txt), [full LeanEval](../evidence/Roth.exists_monic_aeval_eq_zero/source-LeanEval.lean.txt).

Root executed all native checks through its persistent session. This worker prepared exact sources/requests and inspected the complete returned receipts. The original-proof replay contains exactly this target, renamed `Monic272Original.replay` in a fresh namespace; no private helper is necessary. It does **not** replay unrelated Main declarations. Native proof equality through `Subsingleton.elim` verifies original/replay type agreement, not identity of proof constructions. Kernel type/value constants and standard axioms are inspected independently. The `pp.all` body printer elides109933 characters; it is not a full body dump. Full written target source is preserved. The exact293 ordered names were generated from tracked declaration order; root preflight and runtime confirm293 unique names,293 present and293 kernel values, with proper private module names.

[Exact original source](../evidence/Roth.exists_monic_aeval_eq_zero/original-executed.lean.txt), [raw original receipt](../evidence/Roth.exists_monic_aeval_eq_zero/original-receipt.json), [native type/constants](../evidence/Roth.exists_monic_aeval_eq_zero/native-type.json), [source reading scope](../evidence/Roth.exists_monic_aeval_eq_zero/source-reading.json).

## Phase1 — Mathematical statement

An integral real number is a zero of some monic polynomial with integer coefficients and degree at least two. The chosen polynomial need not be irreducible or minimal. In fact, take any monic annihilator furnished by integrality and multiply it by `X²`. This preserves the root and monicity and increases its degree by two.

Full native type:

```lean
∀ {α : ℝ}, IsIntegral ℤ α →
  ∃ (f : Polynomial ℤ), f.Monic ∧ (Polynomial.aeval α) f = 0 ∧ 2 ≤ f.natDegree
```

The only explicit parameter is the real element `α`; the only hypothesis is integrality over `ℤ`. In particular, there is **no irrationality premise**. Integral integers and rational zero are covered by executed examples. No assertion that a minimal polynomial has degree at least two is made; such a claim would fail for integer inputs. The integer coefficient ring's nontriviality, rather than the target real field's division/order/topology, underlies degree inflation. The original kernel body has no project declaration dependencies.

## Phase2 — Preliminary checks

SMALL: an elementary auxiliary existence result, neither a new structure nor a named main theorem. The proof occupies four substantive tactic lines. One-line-definition test: n/a, theorem. This classification did not reduce literature or formal-search breadth.

## Phase3 — Exhaustive literature

Every named channel was executed; optional mathematical-opinion tooling was unavailable. Exact requests, return hashes/bytes/status and clean titles/URLs are archived, without full web article/search-result bodies. Individual general queries were sent in one batch; all three were actual requests.

| Channel | Exact query or locator | Finding |
|---|---|---|
| General specific | `algebraic integer monic polynomial arbitrary large degree multiply X` | Annihilator/minimal-polynomial distinction; elementary multiples enlarge degree. |
| General ring | `integral element monic annihilating polynomial degree padding ring algebra` | Commutative-ring integrality and finite-module characterizations; real numbers are not essential. |
| General aliases | `annihilating polynomial multiples minimal polynomial monic root` | Standard terms are annihilating polynomial and minimal polynomial; they are distinct notions. |
| ChatGPT mathematical opinion | unavailable | Optional `ask_chatgpt_math` channel n/a; remaining channels unchanged. |
| Local `clean.tex` | lines1201–1205, fresh `monic|algebraic integer|degree|irrational` search | Roth argument selects monic integer f and invokes irrationality for degree≥2. This Lean lemma instead pads its witness and needs no irrationality. |
| nLab | `site:ncatlab.org/nlab integral element monic polynomial` | Integral closure entry found; direct fetch fails unsupported `application/xhtml+xml`, honestly retained. |
| nCatLab distinct namespace | `site:ncatlab.org/ncatlab integral element monic polynomial` | Actual distinct query; results return nLab/other namespaces, no exact nCatLab hit. |
| Stacks | `site:stacks.math.columbia.edu integral element monic polynomial` | [Definition10.36.1](https://stacks.math.columbia.edu/tag/00GH) formulates integrality for a ring map by a monic annihilator. |
| MathOverflow | `site:mathoverflow.net monic annihilating polynomial integral element degree` | [Bounds question](https://mathoverflow.net/questions/251738/bound-for-annihilating-polynomials/254051) concerns coefficient control, not this degree-padding law. |
| Recent arXiv | `site:arxiv.org integral elements monic annihilating polynomial after:2021-10-29 before:2026-10-30` | [Borodin–Liu–Zhang,2302.12637](https://arxiv.org/abs/2302.12637), submitted2023/revised2023, studies minimum-degree vanishing polynomials over general rings, a neighboring but different problem. |

Supplementary primary source [Stacks§9.9](https://stacks.math.columbia.edu/tag/09GL), Definition9.9.1 and following paragraph, distinguishes least-degree monic generators from their higher-degree multiples in field extensions. The degree-padding consequence for arbitrary semiring algebras is our verified deduction, not a claim that the source states that exact Lean formulation. Literature agrees on the general integrality concept, but does not settle whether this particular lower-degree existential warrants standalone API.

[Detailed channel summaries](../evidence/Roth.exists_monic_aeval_eq_zero/literature.json), [web0](../evidence/Roth.exists_monic_aeval_eq_zero/web-batch0.json), [web1](../evidence/Roth.exists_monic_aeval_eq_zero/web-batch1.json), [web2](../evidence/Roth.exists_monic_aeval_eq_zero/web-batch2.json), [open results metadata](../evidence/Roth.exists_monic_aeval_eq_zero/web-batch3.json), [local excerpts](../evidence/Roth.exists_monic_aeval_eq_zero/local-excerpts.json).

## Phase4a–b — Generality and actual proofs

| Parameter/property | Original | Verified general form and guard |
|---|---|---|
| Coefficients | `ℤ` | Any nontrivial commutative ring for `IsIntegral`; witness-level proof even uses `CommSemiring`. No domain or characteristic assumption. |
| Target | `ℝ` | Any `Ring A` for pinned `IsIntegral`; witness-level proof uses any `Semiring A` with `Algebra R A`, including noncommutative or trivial targets. |
| Integrality | `IsIntegral ℤ α` | Same property over arbitrary ring algebra. Pinned `IsIntegral` itself requires `CommRing R` and `Ring A`; do not advertise a nonexistent semiring `IsIntegral` API. |
| Degree threshold | fixed2 | Any `N : ℕ`, using `f * X^N`. Exact degree is `f.natDegree+N`, not necessarily N. |
| Nontriviality | inferred for integers | Coefficient `[Nontrivial R]` is essential for unrestricted positive cutoffs. Executed `PUnit[X]` guard proves no polynomial has degree≥1. |
| Irrationality/target nontriviality | no irrationality premise | Neither is needed; arbitrary integer inputs, rational zero, and trivial target are executed guards. |
| Integrality hypothesis | supplied witness | Needed for existence; removing it would require arbitrary real numbers to be integral. No unsupported drop claim. |

STRICTLY NARROWER than a natural general ring/algebra formulation. The following **new scratch theorem**, not an already existing mathlib lemma, compiled under unchanged18 mathlib imports, with `#check_failure Roth.exists_monic_aeval_eq_zero`:

```lean
theorem integral {R A : Type*} [CommRing R] [Nontrivial R] [Ring A] [Algebra R A]
    {a : A} (ha : IsIntegral R a) (N : ℕ) :
    ∃ g : Polynomial R, g.Monic ∧ Polynomial.aeval a g = 0 ∧ N ≤ g.natDegree
```

Its core is the independently proved semiring witness lemma:

```lean
theorem pad {R A : Type*} [CommSemiring R] [Nontrivial R] [Semiring A] [Algebra R A]
    {a : A} {f : Polynomial R} (hf : f.Monic) (hfa : Polynomial.aeval a f = 0) (N : ℕ) :
    ∃ g : Polynomial R, g.Monic ∧ Polynomial.aeval a g = 0 ∧ N ≤ g.natDegree
```

The original type is recovered with `integral hint 2`. Generalization is a mechanical abstract replacement of the same proof, not costly machinery or a reinterpretation. This does not establish absolute minimality of all possible raw homomorphism formulations: the claim is the verified algebra hierarchy shown above.

[Exact generic/guard source](../evidence/Roth.exists_monic_aeval_eq_zero/isolated3-executed.lean.txt), [clean raw result](../evidence/Roth.exists_monic_aeval_eq_zero/isolated3-receipt.json).

## Phase4c — All nine modern-idiom checks

| # | Question | Assessment and concrete consequence |
|---|---|---|
|1|Typeclass preambles|Yes: abstract coefficient/target structure is expressed by established algebra classes, enabling the same `aeval` and monic API for other rings. Integrality stays an element proposition.|
|2|Filters instead of sequences/metrics|No: finite polynomial construction, no topology or limits.|
|3|Universal property instead of construction|No new class needed: existing evaluation algebra hom supplies multiplicativity; an existential polynomial witness is precisely the request.|
|4|Bundled substructure instead of closure predicate|No new subset with closure conditions; `Polynomial R` and `aeval` are already bundled. An evaluation-kernel reformulation is optional and adds obligations.|
|5|Weaken field hierarchy|Yes: semiring witness padding, ring integral wrapper, no real/order/field structure. This serves `IsIntegral` on arbitrary algebras.|
|6|Higher categorical form|No categorical structure in this elementary existence law.|
|7|Concrete indices/constants|Yes: replace cutoff2 by arbitrary N. Polynomial exponents remain natural because they index ordinary polynomials; arbitrary ordered-group exponents would change the object.|
|8|Concrete-via-abstract diagnostic|Yes: body contains no `ℝ`, `ℤ` or `α` identifier. Generic source and original specialization actually compile.|
|9|False-generalization guard|Passed for displayed forms. Nontrivial coefficient guard is retained and tested. No minimal/irreducible/exact-cutoff conclusion is smuggled in; target nontriviality is not imposed.|

Modern idiom available; concrete benefits are reusable degree padding under `Polynomial.aeval` for integral elements in arbitrary algebra extensions and unifying any cutoff requirement. This is a real improvement in scope, but upstream packaging remains a distinct question. [Diagnostic](../evidence/Roth.exists_monic_aeval_eq_zero/concrete-diagnostic.json).

## Phase4.5 — Six infrastructure risks

Theorem-kind n/a for each: typeclass diamonds, reducibility leaks, noncanonical unfolding, instance priority collisions, universe forcing by definitions, and coercion ambiguity. No new definition, instance or coercion is introduced in production or proposed by the theorem statements. Existing algebra instances are parameters. Overall n/a, no infrastructure-risk-based verdict.

## Phase4.6 — All five proof-strategy checks

| # | Check | Result |
|---|---|---|
|1|Topology ε–δ versus filters|n/a: no topology.|
|2|Element versus ideal/submodule argument|Evaluation-kernel membership is another presentation requiring a bridge, with no call-site advantage here. The existing kernel API permits arbitrary semiring source/target; it does not force commutative targets. Multiplicative `aeval` supplies the root preservation directly.|
|3|Sequences versus nets|n/a: no convergence.|
|4|Explicit categorical object versus universal property|n/a: no categorical construction. Existing algebra hom evaluation already supplies the needed law.|
|5|Missing helper mathlib should have|Possible arbitrary-cutoff monic-annihilator existence wrapper; basic monic product/degree/evaluation machinery is already present. Its standalone usefulness is the verdict question.|

MATHLIB-IDIOMATIC strategy: monic multiplication and multiplicative evaluation are the direct proof; the opportunity is abstracting assumptions/cutoff, not replacing the argument.

## Phase5 — All15 formal search cells

Current form = integral real with monic integer annihilator and degree≥2. Literature form = integral element of ring algebra with arbitrary cutoff. Abstract form = semiring monic-annihilator padding. Every cell below links its complete raw request/receipt; local searches were executed by root. Remote indices may differ from the pin. Local states `error`, `error`, `warming` do not establish absence, even when source-fallback items are returned.

| Form | Lean-Finder | Loogle | LeanSearch | rg pinned source | local search |
|---|---|---|---|---|---|
|Current|[receipt](../evidence/Roth.exists_monic_aeval_eq_zero/search-current-leanfinder.json)|[receipt](../evidence/Roth.exists_monic_aeval_eq_zero/search-current-loogle.json)|[receipt](../evidence/Roth.exists_monic_aeval_eq_zero/search-current-leansearch.json)|[receipt](../evidence/Roth.exists_monic_aeval_eq_zero/search-current-rg.json)|[receipt](../evidence/Roth.exists_monic_aeval_eq_zero/search-current-local_search.json)|
|Literature|[receipt](../evidence/Roth.exists_monic_aeval_eq_zero/search-standard-leanfinder.json)|[receipt](../evidence/Roth.exists_monic_aeval_eq_zero/search-standard-loogle.json)|[receipt](../evidence/Roth.exists_monic_aeval_eq_zero/search-standard-leansearch.json)|[receipt](../evidence/Roth.exists_monic_aeval_eq_zero/search-standard-rg.json)|[receipt](../evidence/Roth.exists_monic_aeval_eq_zero/search-standard-local_search.json)|
|Abstract|[receipt](../evidence/Roth.exists_monic_aeval_eq_zero/search-abstract-leanfinder.json)|[receipt](../evidence/Roth.exists_monic_aeval_eq_zero/search-abstract-loogle.json)|[receipt](../evidence/Roth.exists_monic_aeval_eq_zero/search-abstract-leansearch.json)|[receipt](../evidence/Roth.exists_monic_aeval_eq_zero/search-abstract-rg.json)|[receipt](../evidence/Roth.exists_monic_aeval_eq_zero/search-abstract-local_search.json)|

Abstract Lean-Finder timed out initially; a successful retry found `Polynomial.natDegree_mul_X_pow`. The initial raw failure remains separate. Full-name pinned grep is complete and untruncated. Positive primitives checked natively: `Polynomial.Monic.mul`, `Polynomial.monic_X_pow`, `Polynomial.Monic.ne_zero`, `Polynomial.natDegree_mul_X_pow`, `Polynomial.aeval_def`. Their full pinned source files and hashes are archived. The degree lemma requires only `Semiring R` and `Nontrivial R`; no integral-domain degree assumption is needed when multiplying by `X^N`.

Nearby results rejected as full replacements: `one_lt_natDegree_of_irrational_root` requires irrationality; `minpoly.two_le_natDegree_iff` has the extra image-exclusion criterion; `IsIntegral.of_aeval_monic` deduces integrality in the opposite direction; ideal-coefficient monic annihilator existence theorems impose different coefficient constraints and do not give arbitrary lower-degree bounds. No exact existing full theorem was located. Search limitations and failed automation are not a global absence proof. [Matrix](../evidence/Roth.exists_monic_aeval_eq_zero/formal-search-matrix.json), [full-name search](../evidence/Roth.exists_monic_aeval_eq_zero/full-name-search.json), [pinned sources](../evidence/Roth.exists_monic_aeval_eq_zero/mathlib-inputs.json).

## Phase5.5 — Three statement-shape checks

1. **Normal form:** `IsIntegral R a` is already the canonical integrality predicate; `aeval a f = 0` is its natural algebra evaluation spelling. `eval₂ (algebraMap R A) a f = 0` is definitionally bridged by `aeval_def`; evaluation-kernel membership is another presentation with no call-site advantage here. No orthogonal equivalence lemma is proposed.
2. **Syntactic generality:** both supplied-monic-witness padding and `IsIntegral` arbitrary-cutoff forms were actually elaborated. The latter is easier for callers already holding integrality; the former captures the semiring weakening. Old form recovers in one application of our new scratch theorem.
3. **Arguments:** integrality supplies the annihilator; α specifies the evaluation. No explicit unused hypothesis exists. Concrete ℤ/ℝ and cutoff2 are unnecessarily fixed. Coefficient nontriviality is required for positive cutoffs; target nontriviality, commutativity, order and topology are not required by the core.

Overall RESTATE-BEFORE-SHIP for any generic upstream candidate; SHIP-AS-STATED remains valid as a local specialization. No production edits were performed.

## Phase6.0 — Actual callers and scope

| Caller | Actual written use | Verification |
|---|---|---|
|`private Roth.exists_roth_parameters_aux`, Main410, use Main415|`obtain ⟨f, hf, hfα, hdeg⟩ := exists_monic_aeval_eq_zero hint`|Complete original signature/body replay with witness extraction and padding inlined. Native equality with the original private constant verifies its exact proposition.|

Direct written calls:1; callers external to Main:0. This differs from the command's narrower “excluding declaring file” count, which is0. The original exact293 kernel audit independently finds one direct value consumer, `_private.Roth.Main.0.Roth.exists_roth_parameters_aux`, and no direct type consumer. The theorem is not in the simp set. Original project dependency closure is just the target itself: its proof uses no other project result.

The five canonical transitive consumers are the private parameter lemma, `Roth.roth_of_isIntegral`, `Roth.roth`, `Roth.roth_rat`, and `LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth`. This is a project-scoped graph over the canonical293 list, not an inventory of all generated Lean declarations or arbitrary external libraries. It does not turn `roth_of_isIntegral` into a direct written caller.

Full caller verification preserves the direct caller and all four downstream theorem signatures. It copies four unrelated original private helper bodies (approximants, evaluation comparison, product bound, logarithm bound), changing only private visibility inside a fresh scratch namespace; this makes their original proof bodies accessible. It re-elaborates complete `roth_of_isIntegral`, `roth`, `roth_rat`, and final LeanEval theorem bodies. The explicit noncircular traversal walks **four Main roots**, rejects the original target and original downstream Roth theorems, and expands only project/private/scratch constants. The terminal LeanEval theorem is appended after that loop; it explicitly calls the new scratch `roth` and original `isDiophantine_iff`, whose audited original closure does not reach this target. Do not mistake that structural/source check for inclusion in the four-root walk. No truncated caller prefix or supplied desired conclusion is accepted as a caller proof.

Fresh complete ignore-safe lexical search and full source inventory find no second complete inline degree-padding derivation. Existing monic/root uses in MainLemma consume a supplied polynomial and solve different estimates.

[Caller details](../evidence/Roth.exists_monic_aeval_eq_zero/callers.json), [original private caller](../evidence/Roth.exists_monic_aeval_eq_zero/caller-original.lean.txt), [complete executed caller source](../evidence/Roth.exists_monic_aeval_eq_zero/caller2-executed.lean.txt), [actual caller result](../evidence/Roth.exists_monic_aeval_eq_zero/caller2-receipt.json), [complete original scope source](../evidence/Roth.exists_monic_aeval_eq_zero/consumer-scope-executed.lean.txt), [scope receipt](../evidence/Roth.exists_monic_aeval_eq_zero/consumer-scope-receipt.json), [lexical calls](../evidence/Roth.exists_monic_aeval_eq_zero/caller-complete-search.json), [inline pattern search](../evidence/Roth.exists_monic_aeval_eq_zero/inline-complete-search.json).

## Phase6 — Existing-only composition

Before introducing any same-result scratch lemma, an isolated mathlib-only experiment confirmed `exact?` cannot close the full original goal and `simp [IsIntegral, RingHom.IsIntegralElem]` does not close it. The explicit padding proof then succeeds. This is an experiment under default limits, not an impossibility claim about all mathlib routes.

```lean
obtain ⟨f, hf, hf0⟩ := hint
refine ⟨f * Polynomial.X ^ 2, hf.mul (Polynomial.monic_X_pow 2), ?_, ?_⟩
· rw [map_mul, Polynomial.aeval_def, hf0, zero_mul]
· simp [hf.ne_zero]
```

At least seven distinct existing facts occur in the transparent derivation: monic multiplication, monic powers of X, multiplicativity of evaluation, the `aeval_def` bridge, zero multiplication, shifted degree, and monic nonzeroness. Core constructors and elementary natural inequalities are additional glue. It is not an established ≤3-existing-call term. Counting `Monic272Generic.integral` as an existing mathlib call would be false: that is our new scratch proof. Conversely, its elementary witness construction and final simp make a tiny standalone lemma's API value a fair judgment call, explicitly consistent with Phase6b's terminal-simp caveat. Conclusion: NOT-COMPOSABLE by the strict demonstrated criterion; easy direct construction with a packaging question, not a cost barrier.

[Exact experiment](../evidence/Roth.exists_monic_aeval_eq_zero/composition-executed.lean.txt), [clean result](../evidence/Roth.exists_monic_aeval_eq_zero/composition-receipt.json), [call accounting](../evidence/Roth.exists_monic_aeval_eq_zero/composition.json).

## Overview cross-check: API, moral duplication, missing API, junk

| Decl A | Decl B | Same statement? | Same proof? | Conclusion |
|---|---|---|---|---|
|This theorem|`IsIntegral` witness predicate|No: predicate omits lower-degree bound|Original starts by unpacking it, then adds padding|Canonical integrality API reused; not literal duplicate.|
|This theorem|`one_lt_natDegree_of_irrational_root`|No: latter fixes f and needs irrationality|No: irrational-root argument versus padding|No replacement without strengthening the original hypothesis.|
|This theorem|`minpoly.two_le_natDegree_iff`|No: minimality and image exclusion differ|No|Do not infer minimal degree≥2 for integral integer inputs.|
|This theorem|other project monic/root uses in MainLemma|No: polynomial supplied to analytic/Diophantine estimates|No complete second padding derivation found|No moral duplicate to merge.|

Existing `Polynomial`, `Monic`, `IsIntegral` and algebra-hom `aeval` are the API-rich choices already used. Possible missing API is a named arbitrary-cutoff monic-annihilator existence theorem; no new structure, coercion or class is needed. Not junk/dead code: one actual private caller and the Roth/LeanEval transitive chain use it. Its public specialized visibility could nevertheless be reduced or its proof inlined if generic upstream API is declined.

## Phase7 — Verdict and actionable alternatives

**BORDERLINE-needs-human.** Neither “mathlib already has it” nor a strict ≤3-call composition is established. The proposed arbitrary-N ring/semiring generality is concretely verified. However, mathematical truth and broader applicability alone do not settle whether a short monic-padding existential deserves a named public upstream theorem. The elementary proof, one local direct caller, and absence of a literature-standard named result motivate an API-grain decision, independent of implementation cost. Generalization work is already done, so this is not deferring a difficult proof.

Three concrete future upstream questions:

1. Should mathlib expose `IsIntegral.exists_monic_aeval_eq_zero_natDegree_ge` with arbitrary cutoff N, despite the elementary padding proof?
2. If adding it, should the semiring monic-witness padding lemma be public API, or should only the ring `IsIntegral` wrapper be public?
3. If the generic API is declined, should this real/integer specialization become private or be inlined into `exists_roth_parameters_aux`?

If accepted upstream in generic form, place the ring wrapper near `Mathlib/RingTheory/IntegralClosure/IsIntegral/Basic.lean`; assess import layering separately for the semiring witness lemma, which uses the polynomial monic and degree operations API. If declined, keep a private project helper in `Roth/Main.lean`, or inline the shown construction at the single direct Main415 call. The full caller replay verifies that option with unchanged downstream signatures. No other direct call-site replacement is needed. These are reviewable future actions; production stays unchanged in this assessment.

## Phase8 — Verification and handoff

Accepted primary native checks: original replay+kernel audit2792ms; final isolated generality/guards734ms; complete extended callers14104ms; original consumer scope2860ms; existing-only composition10703ms. All are successful, complete, default-limit checks with no errors/warnings or unproved declarations. Standard axioms only: `propext`, `Classical.choice`, `Quot.sound`. Run-code responses have documented diagnostics format and no `partial` field; disk responses explicitly have `partial=false`.

Historical attempts retained: isolated01 failed two guard-example elaborations (102073ms), isolated02 succeeded with one unnecessarySimpa warning (1537ms), and caller01 was a clean16067ms earlier version expanded by accepted caller02. The first two are not accepted proof batches. No raised limits, custom axioms, `sorry`, `unsafe`, or `native_decide` occur in accepted executed sources.

The recursive current manifest, portable read-only validator, actual scratch/integrated-layout receipts and secret scan govern final readiness. Root's independent acceptance remains pending. [Verification index](../evidence/Roth.exists_monic_aeval_eq_zero/verification.json), [assessment](../evidence/Roth.exists_monic_aeval_eq_zero/assessment.json), [validator](../evidence/Roth.exists_monic_aeval_eq_zero/validate.py), [current manifest](../evidence/Roth.exists_monic_aeval_eq_zero/copy-manifest.json).

Final package gates: actual [draft layout checks](../evidence/Roth.exists_monic_aeval_eq_zero/draft-validation.json) and [final layout checks](../evidence/Roth.exists_monic_aeval_eq_zero/final-validation.json) passed in scratch and recreated integrated layouts; temporary layout removed. [Credential/signed-URL scan](../evidence/Roth.exists_monic_aeval_eq_zero/secret-guard.json) passed. [Freeze record](../evidence/Roth.exists_monic_aeval_eq_zero/freeze-record.json) releases native requests; root acceptance remains pending.
