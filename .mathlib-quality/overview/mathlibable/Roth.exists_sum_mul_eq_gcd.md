# `Roth.exists_sum_mul_eq_gcd` — NO-mathlib-has-it

Canonical declaration 170, `Roth/Separation.lean:374`. Full read-only `/overview` and `/mathlibable` assessment. Production sources and pins remain unchanged. Root acceptance is pending.

## Phase 0 — Doctor

All 17 fresh source/pin hashes agree with the successful shared baseline. [Fresh inputs](../evidence/Roth.exists_sum_mul_eq_gcd/inputs.json), [baseline](../evidence/Roth.exists_sum_mul_eq_gcd/baseline-build.txt), [input manifest](../evidence/Roth.exists_sum_mul_eq_gcd/input-manifest.json). The declaration resolves as a theorem without sorry. The whole declaring module concerns separating multivariate polynomial factors and proving Lemma 2 of the source; its integrality section uses this arithmetic step to descend rational coefficients to integers. The [complete declaring module](../evidence/Roth.exists_sum_mul_eq_gcd/source-module.lean.txt) and sole caller were read.

## Phase 1 — Comprehend

For any finite family of integers, its normalized greatest common divisor is an integer linear combination of those integers. The coefficient function is defined on the entire ambient index type; only its values on the given finite set matter. Empty sets and all-zero families are included: their gcd is zero. No nonemptiness, nonzero or coprimality premise is present.

Full native type (all binders, including the witness):

```lean
∀ {ι : Type u_2} (s : Finset ι) (u : ι → ℤ),
  ∃ (z : ι → ℤ), ∑ i ∈ s, z i * u i = s.gcd u
```

`ι` is any universe-polymorphic index type, `s` selects the finite family, and `u` supplies the integers. The surrounding `τ`, `Fintype τ`, and `DecidableEq τ` parameters are absent from the elaborated type. There are no explicit hypotheses beyond the data. The proof specializes `Finset.gcd_eq_sum_mul` and reverses equality and multiplication order. It depends on no project lemma. [Native type](../evidence/Roth.exists_sum_mul_eq_gcd/native-type.json), [complete native kernel/type/canonical receipt](../evidence/Roth.exists_sum_mul_eq_gcd/bezout-original-audit-receipt.json). The target kernel print is complete, without output elision.

## Phase 2 — Preliminary checks

BIG by the command's named-theorem criterion: the docstring explicitly identifies Bézout's identity, although the implementation is a one-step specialization. Literature width remains exhaustive. Phase 2b is n/a: theorem, not a definition; its one-line proof does not invoke the definition exemption test. This is a full assessment, not a prefilter or inherited verdict.

## Phase 3 — Exhaustive literature

The exact requests, response SHA256/byte counts, status, titles, URLs and original summaries are preserved in [literature accounting](../evidence/Roth.exists_sum_mul_eq_gcd/literature-individual.json). No article/search-response bodies are archived. All returned URL query strings were removed from archived locators, including credential-bearing signed URLs; the unchanged response hashes remain recorded.

| Channel | Actual query or locator | Finding |
|---|---|---|
| General web, current | `finite family integers Bezout identity greatest common divisor linear combination` | Primary number-theory teaching sources identify the gcd linear-combination identity. |
| General web, general | `Bezout ring finitely generated ideal principal gcd linear combination` | Standard ring abstraction: finitely generated ideals are principal. |
| General web, aliases | `extended Euclidean algorithm Bezout lemma several integers identity` | Bézout lemma and extended Euclidean algorithm describe the same arithmetic content. |
| ChatGPT mathematical MCP | Tool availability inventory | n/a: `ask_chatgpt_math` unavailable. Historical evolution checked independently in the primary textbook's historical remark 2.4.7. |
| Local references | `rg -n 'B.zout|gcd|primitiv|coprime' .mathlib-quality/references/clean.tex` | §2 lines420–436 discusses primitive integral rescaling and the finite Bézout relation when coefficient gcd is one. |
| nLab | `site:ncatlab.org/nlab Bezout domain finitely generated ideal` | Bézout ring/domain pages give the principality formulation. Direct XHTML fetch failed; search access succeeded. Some returned examples are garbled; only the definitions are used. |
| nCatLab | `site:ncatlab.org/ncatlab Bezout identity ideals` | Returned `/nlab` pages, no separate `/ncatlab` hit. No higher-categorical result claimed. |
| Stacks | `site:stacks.math.columbia.edu Bezout ring finitely generated ideal principal` | Tag0ASR, Definition15.126.5(1) explicitly defines Bézout domains by principality of finitely generated ideals. |
| MathOverflow | `site:mathoverflow.net Bezout domain gcd finitely generated ideal` | Discussions distinguish GCD from Bézout domains; supplementary motivation, not primary proof evidence. |
| arXiv, five years | `site:arxiv.org/abs/ Bezout domains finitely generated ideals after:2021-10-27 before:2026-10-28` | Contemporary ideal theory hits, including 2610.00076 and 2305.18796; also irrelevant results. No stronger replacement identity inferred. |

[Local search](../evidence/Roth.exists_sum_mul_eq_gcd/local-literature-search.json), [local excerpt](../evidence/Roth.exists_sum_mul_eq_gcd/clean-excerpt.tex.txt), [availability](../evidence/Roth.exists_sum_mul_eq_gcd/literature-availability.json).

Primary sources: [NTIC §2.4](https://math.gordon.edu/ntic/ntic/section-bezout-id.html), Definition2.4.1 and lines876–887, explicitly discusses both coefficient orders; [Stacks0ASR](https://stacks.math.columbia.edu/tag/0ASR), Definition15.126.5(1). Direct access metadata: [integer textbook](../evidence/Roth.exists_sum_mul_eq_gcd/primary-integer.json), [exact locator/historical remark](../evidence/Roth.exists_sum_mul_eq_gcd/primary-locator.json), [Stacks](../evidence/Roth.exists_sum_mul_eq_gcd/primary-stacks.json), [failed nLab fetch](../evidence/Roth.exists_sum_mul_eq_gcd/primary-nlab.json), [recent primary arXiv context](../evidence/Roth.exists_sum_mul_eq_gcd/primary-arxiv.json).

Literature summary: the concept is finite Bézout identity. Integer versions arise algorithmically, while the standard ring formulation uses a Bézout property and a gcd representative determined up to association. The finite linear-combination formulation and ideal generation agree. Indices can be arbitrary with finite support; coefficients must remain in a ring supporting the Bézout relation. The current declaration agrees mathematically but fixes the coefficient ring to integers. No substantive disagreement among the primary definitions was found; contemporary papers add ideal theory, not a new formulation of this identity.

## Phase 4a — Parameters and generality

| Parameter or feature | Current | Standard / candidate | Assessment |
|---|---|---|---|
| `ι : Type*` | Arbitrary universe | Arbitrary index | Already general; no finiteness or decidable equality class needed. |
| `s : Finset ι` | Finite selected family | Finite generated ideal or finite support | Essential finite-family representation. Infinite families require a finite-support witness and an ideal formulation. |
| `u : ι → ℤ` | Integer values | `u : ι → R` with `CommRing R`, `IsBezout R`, `NormalizedGCDMonoid R` | Verified strictly broader existing theorem. |
| Witness `z : ι → ℤ` | Full coefficient function | Ring-valued function; alternatively finitely supported combination | Full function avoids extension obligations at the actual caller. |
| Gcd normalization | Integer normalized gcd | Explicit normalized gcd structure | Needed to specify an element rather than only its associate class. |
| Equality/product orientation | `∑ zᵢuᵢ = gcd` | `gcd = ∑ uᵢzᵢ` | Equivalent by symmetry and commutativity, with no definition expansion. |
| Nonemptiness/nonzero | None | None | Edge cases actually compiled. |
| Parent interface | No project definition | Existing `Finset.gcd` | No parent migration or inherited decision required. |

## Phase 4b — Verified generality verdict

STRICTLY NARROWER THAN STANDARD, with one verified coefficient-ring expansion:

```lean
{R ι : Type*} [CommRing R] [IsBezout R] [NormalizedGCDMonoid R]
(s : Finset ι) (u : ι → R) :
  ∃ z : ι → R, ∑ i ∈ s, z i * u i = s.gcd u
```

The unchanged one-line specialization proof compiles under these binders as `Bezout170.general` in the [mathlib-only exact execution](../evidence/Roth.exists_sum_mul_eq_gcd/bezout-isolated-executed.lean.txt), [clean native receipt](../evidence/Roth.exists_sum_mul_eq_gcd/bezout-isolated-receipt.json). This is a concrete-to-abstract expansion, not an unused-hypothesis removal; the source contains no instance hypotheses to drop. Mechanical cost is cheap and is not a verdict factor. The general form is already in mathlib, so this does not create a YES-generalise ticket. No unsupported claim of maximal generality beyond this verified interface is made.

## Phase 4c — All nine modern-idiom checks

| # | Question | Answer / proposed form | Concrete downstream consequence |
|---|---|---|---|
| 1 | Typeclass preambles | Yes for the expanded ring form: existing `IsBezout R` and normalized gcd classes. | Reuses ring instances and the finite gcd API rather than integer arithmetic. |
| 2 | Filters/topology | No; finite algebraic equality has no convergence. | None. |
| 3 | Universal property | Yes as an alternative view: ideal generation characterizes allowable combinations. | Existing `Ideal.mem_span_range_iff_exists_fun` gives membership ↔ coefficient function. |
| 4 | Bundled substructures | Yes: `Ideal.span (Set.range u)` bundles the span. | Ideal inclusion, sums and principality API; already present. |
| 5 | Hierarchy weakening | Yes: integers to commutative Bézout ring with normalized gcd. | Finite Bézout law specializes without Euclidean/PID assumptions. |
| 6 | Higher categories | No categorical structure in this scalar identity. | None. |
| 7 | Concrete index | No: `ι` is already arbitrary; ℤ is coefficient ring, not index. | No artificial index generalization. |
| 8 | Concrete-via-abstract diagnostic | Yes: grep of the single proof line finds zero occurrences of `ℤ` or `Int`; it only calls generic `Finset.gcd_eq_sum_mul`. | Actual general-ring proof compiles; other Bézout rings reuse it. |
| 9 | False-generalization guard | Verified ring expansion preserves the same identity. Dropping Bézout merely because a gcd exists is unjustified; replacing integer coefficients by naturals is false. | Actual `naturalCoefficientsFail` proves there are no naturals `a,b` with `2a+3b=1`. Semiring ideal membership is separately true, not a gcd theorem without the span premise. |

Modern idiom available, already supplied by mathlib. The [guard execution](../evidence/Roth.exists_sum_mul_eq_gcd/bezout-guards-executed.lean.txt) and [receipt](../evidence/Roth.exists_sum_mul_eq_gcd/bezout-guards-receipt.json) verify the ideal membership alternative under `Semiring`/`Fintype`, the natural-coefficient obstruction, and empty/all-zero integer families. The ideal alternative changes the representation/premise; it is not advertised as a definitionally equal replacement or a new helper.

## Phase 4.5 — Infrastructure risks

n/a: this is a theorem, introducing no data, reducibility choice, typeclass instance or coercion. All six definition-only rows are n/a: typeclass diamond, reducibility leak, noncanonical unfolding, instance-priority collision, universe-polymorphism construction risk, coercion ambiguity. Its index universe is checked in the full native type; no definition or instance proposal is being smuggled into this exemption.

## Phase 4.6 — Five proof-strategy checks

| # | Question | Assessment |
|---|---|---|
| 1 | Topological ε–δ vs filters | n/a, no topology. |
| 2 | Elements vs ideal/submodule inclusion | Ideal membership is the conceptual explanation, but the existing finite Bézout theorem directly supplies the required coefficient witnesses. Reproving via ideal induction would duplicate established API. |
| 3 | Sequences vs nets | n/a, no limits. |
| 4 | Construction vs universal property | The witness is extracted from existing Bézout law; ideal-span iff already captures the alternative characterization. |
| 5 | Missing helpers that should exist | None for this declaration: both finite gcd representation and span membership already exist. |

MATHLIB-IDIOMATIC proof strategy: call the existing theorem. Local wrapper removal is recommended because the statement duplicates that API; there is no missing mathematical helper to upstream first.

## Phase 5 — All five actual methods on three forms

The 15 exact requests and complete raw formal-search responses are indexed by [formal search matrix](../evidence/Roth.exists_sum_mul_eq_gcd/formal-search.json). The current, literature-standard ring, and abstract ideal forms were all searched; no search failure is treated as absence.

| Method | Current integer form | Standard ring form | Abstract ideal form |
|---|---|---|---|
| Finder | Integer and binary Bézout identities | Binary Bézout and finite gcd extraction candidates | `Ideal.mem_span_range_iff_exists_fun`, `Finsupp.mem_ideal_span_range_iff_exists_finsupp` |
| Loogle | `Finset.gcd, Exists` hits exact finite law | `Finset.gcd, _ = ∑ _ ∈ _, _ * _` hits exact finite law | `Ideal.span, Exists` hits span pair/singleton/insert facts |
| LeanSearch | Integer/binary Bézout candidates | Existing ring Bézout law and `IsBezout` | Exact finite ideal membership iff and submodule variants |
| rg | Exact finite gcd theorem in pinned source | Existing ring finite/binary laws and class context | Exact ideal/finsupp membership names in pinned source |
| local name patterns | Exact `Finset.gcd_eq_sum_mul` | Broader gcd_eq names | Ideal/submodule mem_span names |

The local tool marks its index unavailable while returning lexical candidates; this is recorded, not interpreted as exhaustive absence. External search indices may use another revision. Pinned source plus actual native signature/proof checks settle presence independently.

Conclusion: **found in mathlib as `Finset.gcd_eq_sum_mul`; more general form** in `Mathlib/RingTheory/PrincipalIdealDomain.lean:233`. Its precise existing signature is:

```lean
{R : Type*} {α : Type*} [CommRing R] [IsBezout R] [NormalizedGCDMonoid R]
(s : Finset α) (f : α → R) : ∃ g : α → R, s.gcd f = ∑ a ∈ s, f a * g a
```

[Complete pinned source](../evidence/Roth.exists_sum_mul_eq_gcd/PrincipalIdealDomain.lean.txt), [actual signature and independent proof receipt](../evidence/Roth.exists_sum_mul_eq_gcd/bezout-isolated-receipt.json). `Ideal.mem_span_range_iff_exists_fun` lives in `Mathlib/RingTheory/Ideal/Operations.lean`; its actual `Semiring`/`Fintype` signature is checked too. Neither candidate is an invented project helper.

## Phase 5.5 — All three statement-shape checks

Normal form: existing gcd-left/family-first `Finset.gcd_eq_sum_mul` is canonical. The alternative is the current sum-left/coefficient-first expression or ideal-span membership. Equality symmetry and commutativity bridge the first two; no new O(n²) equivalence lemma is useful. RHS normal-form convention does not force a new equality orientation lemma.

Syntactic generality: both original orientation and generic ring variant were compiled. The sole full caller was also compiled using the existing orientation directly, so it need not normalize an entire existential statement. Choose existing API at the call site. The abstract ideal iff was separately compiled, but the caller already holds a gcd-one premise and benefits from direct Bézout coefficients.

Superfluous arguments: `ι` indexes both data and witness; `s` selects the summation/gcd; `u` supplies the family. All are essential data. There are no extra typeclasses, nonzero assumptions or unused parent parameters in the native type. No argument to drop.

Overall: RESTATE-BEFORE-SHIP locally by using the existing canonical theorem; no upstream declaration is proposed. Normal form REFACTOR, syntactic generality RESTATE to existing API, superfluous arguments NONE.

## Phase 6.0 — Complete callers and inline audit

Exact lexical enumeration uses every canonical source file and fresh content hashes. [Enumeration](../evidence/Roth.exists_sum_mul_eq_gcd/lexical-enumeration.json), [ignore-proof rg](../evidence/Roth.exists_sum_mul_eq_gcd/caller-rg.json), [tracked-source git grep](../evidence/Roth.exists_sum_mul_eq_gcd/caller-git-grep.json). There are two source occurrences: declaration line374 and use line446. No docstring occurrence. Explicit use count = 1; internal uses excluding declaring file = 0; external-to-file callers = 0.

| Caller | Usage | Mechanical refactor |
|---|---|---|
| `Roth.exists_int_eq_of_gcd_eq_one`, `Roth/Separation.lean:446` | `obtain ⟨z, hz⟩ := exists_sum_mul_eq_gcd s u` | Use `Finset.gcd_eq_sum_mul s u`; retain gcd-left equality and generator-first product, then adapt the calc as in the exact compiled `Bezout170.caller`. |

[Inline re-derivation audit](../evidence/Roth.exists_sum_mul_eq_gcd/rg-inline.json) finds only the wrapper's own call to `Finset.gcd_eq_sum_mul` and the wrapper/use; no second inline derivation elsewhere. The exact293 canonical audit independently counts all293 unique names and all293 kernel values, with sole direct kernel-value consumer `Roth.exists_int_eq_of_gcd_eq_one`. [Audit source](../evidence/Roth.exists_sum_mul_eq_gcd/bezout-audit-executed.lean.txt), [consumer record](../evidence/Roth.exists_sum_mul_eq_gcd/canonical-consumers.json). Direct value consumers are distinct from transitive proof/simp dependency closure; the assessment does not infer dead code from lexical counts.

## Phase 6 — Actual composition/replacement experiments

An additional [exact explicit composition](../evidence/Roth.exists_sum_mul_eq_gcd/bezout-direct-composition-executed.lean.txt) and [clean receipt](../evidence/Roth.exists_sum_mul_eq_gcd/bezout-direct-composition-receipt.json) avoid even closing simp: obtain the existing coefficient function `z,hz`, then return `⟨z, (Finset.sum_congr rfl (fun i _ ↦ mul_comm (z i) (u i))).trans hz.symm⟩`. This uses exactly three named existing calls (`Finset.gcd_eq_sum_mul`, `Finset.sum_congr`, `mul_comm`), plus core equality/existential operations; no definition expansion or custom bridge theorem.

The original full statement succeeds independently with this one-line specialization of the existing result:

```lean
by simpa only [eq_comm, mul_comm] using Finset.gcd_eq_sum_mul s u
```

The same proof succeeds for the verified generic ring form. This is one existing mathematical theorem plus equality/product orientation normalization, with no definition expansion or custom reasoning. **COMPOSABLE**, and more specifically an existing-theorem hit. Phase6b's borderline heuristic for discovering a theorem by `simp [defs...]` composition is acknowledged: a successful arbitrary simp proof would not by itself justify NO-composable. Here the named existing theorem has the same finite family, witness and gcd conclusion, read in pinned source and independently checked at both coefficient rings. `simp only` uses just symmetry/commutativity, and the full sole-caller proof also calls the theorem directly in its own canonical orientation. Consequently the NO-has-it verdict rests on existing Bézout law presence, not on cost or a broad simp closure.

The [accepted mathlib-only source](../evidence/Roth.exists_sum_mul_eq_gcd/bezout-isolated-executed.lean.txt) contains the original, generic, and full only-caller proofs under exactly11 mathlib imports and `#check_failure Roth.exists_sum_mul_eq_gcd`. No project import or wrapper participates. Full caller key changes:

```lean
obtain ⟨z, hz⟩ := Finset.gcd_eq_sum_mul s u
rw [hu] at hz
-- In the calc, use sum u_i*z_i, and `simp [← hz]`.
-- After push_cast use `mul_comm (u i : ℚ)`, then mul_assoc and hw i hi.
```

The preserved [rejected first source](../evidence/Roth.exists_sum_mul_eq_gcd/bezout-isolated-rejected-executed.lean.txt) and [receipt](../evidence/Roth.exists_sum_mul_eq_gcd/bezout-isolated-rejected-receipt.json) had declaration-whitespace warnings and a cast-level multiplication rewrite error. They are not verification evidence. The corrected exact execution is clean, complete, uses only standard axioms, and includes no sorry, new axioms, unsafe, native_decide, or raised limits.

## Phase 7 — Actionable verdict

**NO-mathlib-has-it.** Existing `Finset.gcd_eq_sum_mul`, `Mathlib/RingTheory/PrincipalIdealDomain.lean:233`, already proves finite Bézout over any commutative Bézout ring with normalized gcd. Integer specialization differs only in symmetry and factor order, as the primary textbook also treats as interchangeable. The native original/general probes and complete sole-caller refactor substantiate the hit. No generalization or missing API remains to contribute for this declaration.

Delete `Roth.exists_sum_mul_eq_gcd`; at its one call site, `Roth/Separation.lean:446`, call `Finset.gcd_eq_sum_mul s u` and use the exact compiled `Bezout170.caller` arithmetic adaptation. The only mathematical building block is `Finset.gcd_eq_sum_mul`; `eq_comm` and `mul_comm` orient the equivalent displayed statement. Retain the existing theorem's import through the established context or add its owning module explicitly if import cleanup changes that context. Production changes are outside this read-only assessment and have not been made.

Alternative destination if the pedagogical spelling is retained: a local explanatory comment/example in `Roth/Separation.lean`'s integrality section, because its purpose is to narrate the source's primitive-coefficient argument. It is used, not mathematically junk; the redundant public wrapper is what should disappear. No upstream PR, reviewer or YES grouping is applicable to this NO verdict.

## Phase 8 — Evidence and validation

All required phases pass; theorem-only definition checks are justified n/a. No verification question remains. [Assessment](../evidence/Roth.exists_sum_mul_eq_gcd/assessment.json), [verification sources and raw receipts](../evidence/Roth.exists_sum_mul_eq_gcd/verification.json), [overview entry](../evidence/Roth.exists_sum_mul_eq_gcd/overview-entry.json), [portable read-only validator](../evidence/Roth.exists_sum_mul_eq_gcd/validate.py). Validation checks current manifest hashes/bytes, all17 fresh inputs, exact293 array order/private names, clean complete native executions, standard axioms,15 actual search cells, every named literature channel, complete callers and portable links. Root independently accepts before publication.
