# Roth.weight_single — full mathlibable assessment

Canonical declaration 35, `Roth/Box.lean:96`. **NO-mathlib-has-it**, by the command’s explicit dependent-lemma re-aim rule. Completed read-only assessment; root acceptance pending. Parent `Roth.weight` was assessed as NO-mathlib-has-it in favor of generic `Finsupp.weight`; that existing parent has the exactly analogous `Finsupp.weight_single`. The native reciprocal-weight bridge verifies the specialization. The current finite quotient spelling is not definitionally equal to the bundled form: its independent four-fact proof remains evidence, but does not override the re-aim rule. No claim of novelty follows from unsuccessful searches.

## Phase 0 — baseline and existence

The shared successful `lake build` completed 2467 jobs with exit code 0. All 17 production-source/pin hashes were freshly compared and match the baseline input manifest. This reuses that build, not a new full build. The exact target declaration resolves, its elaborated type and standard axioms were printed, and the independently replayed target, raw mathlib-only mirror and caller fragments all have terminal native success, `partial=false`, no failed dependencies and no errors or warnings. Production sources and pins remain untouched.

Evidence: [baseline](../evidence/Roth.weight_single/baseline-build.txt), [fresh 17-way hash check](../evidence/Roth.weight_single/baseline-hash-check.json), [input manifest](../evidence/Roth.weight_single/input-manifest.json), [native target receipt](../evidence/Roth.weight_single/native-target.json), [verification map](../evidence/Roth.weight_single/verification.json).

## Phase 1 — comprehend

The native elaborated type is

```lean
@Roth.weight_single : ∀ {σ : Type u} [Fintype σ] (r : σ → ℕ) (j : σ) (n : ℕ),
  Roth.weight r (Finsupp.single j n) = (n : ℝ) / (r j : ℝ)
```

For a multi-index concentrated at coordinate j with exponent n, every other summand vanishes, so its weight is n divided by r j. `r j=0` and `n=0` are allowed: Lean's real division is total, with division by zero equal to zero. There is no positivity assumption. The file's earlier `omit [DecidableEq σ]` applies: no explicit equality-decider is present in the elaborated theorem. `classical` is proof-local. The proof unfolds `Roth.weight` and uses `Finsupp.single_apply`, conditional division and finite singleton summation. The sole project definition dependency is `Roth.weight`; it invokes no other project theorem.

The entire declaring module, both complete caller modules and the generic weight module were read. Caller roles are detailed in Phase 6. [Full Box source](../evidence/Roth.weight_single/Box-source.lean.txt), [Lattice source](../evidence/Roth.weight_single/Lattice-source.lean.txt), [Theta source](../evidence/Roth.weight_single/Theta-source.lean.txt), [pinned Weight source](../evidence/Roth.weight_single/Weight-source.lean.txt), [source hashes](../evidence/Roth.weight_single/source-hashes.json).

## Phase 2 — preliminary checks

SMALL: elementary finite summation identity, not a named deep theorem or new construction. The one-line definition test is n/a because this is a theorem. Its substantive proof has two lines (`classical`, `simp ...`), but theorem proof length does not activate the definition-only exemptions. No prefilter or blanket parent-verdict inheritance was used; this is not a definitional `rfl` bridge. All phases ran in full. At final routing, the parent NO-mathlib-has-it assessment triggers the explicit re-aim check against its generic replacement; the analogous generic singleton theorem is verified upstream.

## Phase 3 — exhaustive literature protocol

Every named channel was actually searched. The protocol's informal nine-channel label includes three web forms and optional ChatGPT separately; no artificial synthesis channel was invented. Web artifacts retain requests, response hashes/byte lengths and sanitized locators only, plus original concise summaries here. Full remote bodies were not archived. An initial specific query produced irrelevant index-finance and machine-learning results; a recorded retry likewise found no direct standalone statement. This is search noise, not evidence that the identity is absent from literature.

| Channel | Exact query / locator | Result and relevance |
|---|---|---|
| General web, specific | `"Roth" "multi-index" "weight" single coordinate` | No direct theorem hit; numerical and statistical multi-index false positives. [request/metadata](../evidence/Roth.weight_single/web0-metadata.json) |
| General web, standard | `weighted degree monomial x_i power n equals n weight` | MIT algebraic geometry notes §1.7.8 define monomial weighted degree as the sum of exponent times assigned weight. Singleton formula follows immediately. [metadata](../evidence/Roth.weight_single/web1-metadata.json) |
| General web, abstract | `free module linear combination basis vector evaluation universal property` | Lecture-note primary sources for free modules; the abstract content is linear extension evaluated on a generator. [metadata](../evidence/Roth.weight_single/web2-metadata.json) |
| ChatGPT mathematical MCP | Standard form / generality / historical evolution | n/a: `ask_chatgpt_math` unavailable. No claim of an answer from another assistant. |
| Local source | `clean.tex:530–555,786–812` plus exhaustive weight/index grep | Positive real parameters in the index definition; the last-coordinate derivative term subtracts ν/r_p. The isolated singleton identity is bookkeeping rather than a separately named theorem. [local evidence](../evidence/Roth.weight_single/local-literature.json), [actual grep](../evidence/Roth.weight_single/source-search-3.json) |
| nLab | `site:ncatlab.org/nlab weighted degree monomial` | Degree/monomial pages returned as conceptual matches. [metadata](../evidence/Roth.weight_single/web3-metadata.json) |
| nCatLab | `site:ncatlab.org weighted monomial free module` | Free commutative monoid/module pages support abstraction, not a novel ratio identity. Direct free-module page opening failed with unsupported XHTML content type (400); not reported as a successful page read. [metadata](../evidence/Roth.weight_single/web4-metadata.json), [open receipt metadata](../evidence/Roth.weight_single/web8-metadata.json) |
| Stacks | `site:stacks.math.columbia.edu graded polynomial weighted degree` | Graded polynomial ring matches; direct tag 00CV was opened and is tensor products, not free-module singleton evaluation. It supplies only broader universal-property context; no exact hit claimed. [metadata](../evidence/Roth.weight_single/web5-metadata.json) |
| MathOverflow | `site:mathoverflow.net weighted degree polynomial monomial` | Weighted homogeneous polynomial discussion uses sum of exponents times variable degrees. No exact Roth ratio API or generality improvement established from discussion. [metadata](../evidence/Roth.weight_single/web6-metadata.json) |
| Recent arXiv, last five years | `site:arxiv.org weighted degree multi-index Roth theorem 2022 2023 2024 2025 2026` | Salami, submitted 13 October 2026, arXiv:2610.17589, abstract discusses weighted projective Roth and cautions against naive index rescaling. Adjacent topic, not evidence that this elementary identity fails or needs positivity. [metadata](../evidence/Roth.weight_single/web7-metadata.json), [opened abstract metadata](../evidence/Roth.weight_single/web8-metadata.json) |

Primary locators: [MIT notes §1.7.8](https://math.mit.edu/classes/18.721/ag-aug31-2021.pdf), [Stacks tag 00CV, contextual only](https://stacks.math.columbia.edu/tag/00CV), [Salami abstract](https://arxiv.org/abs/2610.17589). Only these primary sources and the local source establish the literature synthesis; forum and encyclopedia results are search leads. No historical change of this elementary basis identity was established. The conventional weighted-degree presentation uses positive integer weights; Roth's source permits positive real reciprocal weights. The underlying additive weighted sum needs neither order nor positivity, and basis evaluation makes sense for any semiring/module. Thus the literature-standard mathematical operation is weighted linear combination, while the quotient spelling is the project's chosen parameterization.

Credential handling: returned URL query strings were removed preventively before archival, including ordinary query parameters. No secret values were retained. Some early metadata serialization attempts failed before writing; successful replacement searches supply the final metadata. The hash is of the returned tool response serialized as JSON, encoded in UTF-8; no body is included in the package. All `site:` syntax used for final queries is valid.

## Phases 4a–4b — parameters and generality

| Parameter / hypothesis | Current form | Standard abstraction and actual verification |
|---|---|---|
| σ universe | `Type u` | Already universe polymorphic; no restriction to Fin n. |
| Finiteness | `[Fintype σ]` | Required to state the fixed parent univ sum. Support sums and bundled weight remove it; `support_division` and an infinite ℕ example compile. This changes the representation, rather than dropping a typeclass from the same parent expression. |
| Equality decision | None | Native exact target type and four-fact proof have no DecidableEq hypothesis. No candidate drop remains. |
| r | `σ → ℕ` | The source permits positive real parameters; compiled `finite_division` accepts arbitrary K-valued r for `[DivisionSemiring K]`, even zeros. This expands the parent definition, rather than weakening a hypothesis of the existing theorem. |
| j | arbitrary σ | Essential coordinate; no order, nonemptiness or enumerated position needed. |
| n | ℕ exponent | Standard module form accepts any semiring coefficient, compiled as `arbitrary_weight`. `finite_kernel` permits any coefficient type with zero. Exponent semantics remain natural in the project. |
| Codomain | ℝ | Fixed by parent; compiled division identity over DivisionSemiring and zero-preserving additive kernels isolates the weaker algebra. Order, completeness and Archimedean assumptions are unnecessary in the expanded statement. |
| Denominator positivity | Absent | Correctly absent; zero and nonzero denominator guards compile. Adding positivity would narrow the identity. |

**Verdict:** MAXIMALLY GENERAL relative to the fixed `Roth.weight` interface: no unused hypothesis can be dropped. Expanded representations are strictly broader and were actually compiled; they are not mislabelled as a one-edit `YES-but-generalise-first`. `[Fintype]` cannot simply disappear while leaving the current univ-sum parent unchanged. No attempted weakening failed and was silently discarded. The parent migration would affect the Box API and downstream files, and the abstract singleton theorem is already present upstream.

Compiled restatement:

```lean
theorem finite_kernel [Fintype σ] {A B : Type*} [Zero A] [AddCommMonoid B]
    (g : σ → A → B) (hg : ∀ i, g i 0 = 0) (j : σ) (a : A) :
    (∑ i, g i ((Finsupp.single j a) i)) = g j a :=
  (Finsupp.sum_fintype (Finsupp.single j a) g hg).symm.trans
    (Finsupp.sum_single_index (hg j))
```

This freshly proved helper is **not** an existing mathlib replacement. [Exact raw source](../evidence/Roth.weight_single/raw-executed.lean.txt), [terminal receipt](../evidence/Roth.weight_single/native-raw.json).

## Phase 4c — nine modern-idiom rows

| # | Diagnostic | Answer, concrete reformulation and consequence |
|---|---|---|
| 1 | Typeclass preambles | No missing bundled hypothesis: zero-preserving kernels can be explicit, module axioms already use instances upstream. |
| 2 | Sequences / filters / topology | No: finite algebraic equality has no convergence or neighborhoods. |
| 3 | Universal property | Yes: use `Finsupp.linearCombination` / `Finsupp.weight`, the linear extension from generators. Already upstream; basis evaluation is `Finsupp.weight_single`. |
| 4 | Bundled substructures | No substructure closure predicate occurs. Bundling the additive map is useful, covered by row 3 rather than inventing a subobject. |
| 5 | Hierarchy weakening | Yes in expanded statement: semiring/module for arbitrary weight, DivisionSemiring for direct division; compiled. Enables non-real module weights and no ambient Fintype. |
| 6 | Higher categories | No categorical theorem or coherence data occurs; categorification has no demonstrated caller benefit. |
| 7 | Concrete numeric indices | σ already arbitrary; natural coefficients can expand to semiring coefficients. This is verified and available via existing generic weight, not a missing theorem. |
| 8 | Concrete-via-abstract | Yes. Source proof mentions `weight` in one unfolding line and then only finite singleton evaluation; no analytic property of ℝ occurs. Abstract restatement is zero-preserving `finite_kernel` or bundled `Finsupp.weight_single`. The native bridge `via_bundled` confirms that reciprocal real weights specialize correctly. |
| 9 | False-generalization guard | Pass for displayed algebraic identities: substituting `(r i : ℝ)⁻¹` and natural exponents yields the same sum, including zero denominators. Reject treating arbitrary signed/module values as automatically satisfying Roth's nonnegativity and positive-weight index lemmas. Those properties require separate assumptions; no such migration is claimed here. |

Modern idiom available: **yes, already in mathlib**. Using bundled weight enables `map_add`, singleton evaluation and arbitrary ambient types. Actual downstream consequences are the two derivative/lattice decompositions, plus elimination of repeated finite-sum casts after a parent bridge. Mathematical improvement is reusing the free additive linear-combination API. This is an API design migration, not a new generalized singleton theorem. No production migration was performed.

## Phase 4.5 — six infrastructure risks

Theorem n/a: it introduces no new definition, class or instance. Explicit row audit: typeclass diamonds n/a (no instance); reducibility leak n/a (opaque proposition proof); noncanonical unfolding n/a for theorem (the parent remains unchanged); instance priority collision n/a (no priority); universe issues n/a as new infrastructure (already polymorphic theorem, natively checked); coercion ambiguity n/a (no coercion declaration). Overall NONE as infrastructure addition; any future parent refactor deserves its own assessment.

## Phase 4.6 — five proof-strategy rows

| # | Strategy check | Finding |
|---|---|---|
| 1 | ε–δ vs filters | n/a: no topology. |
| 2 | Elements vs subobject algebra | No ideal/submodule inclusions; finite scalar evaluation is appropriate. Bundled weight provides optional point-free organization. |
| 3 | Sequences vs nets | n/a: no limits. |
| 4 | Construction vs universal property | Existing free-module universal property explains generic weight; current theorem is only its coordinate calculation after a bridge. No new object is constructed. |
| 5 | Missing helper mathlib should have | Possible generic univ-sum zero-preserving-kernel convenience lemma (`finite_kernel`), but it itself uses two existing facts. No demonstrated mathematical gap in singleton evaluation. A bridge for the project's quotient parameterization is local API design. |

Current strategy MATHLIB-IDIOMATIC for the retained parent: a direct `simp` proof is natural. REFACTOR-RECOMMENDED only if the parent weight is migrated to bundled support-sum form. Shorter code alone does not resolve whether upstream should expose this ratio convenience wrapper. No cost-based verdict is used.

## Phase 5 — all five actual mathlib searches

Three forms were used: current finite cast/division sum; literature weighted-degree basis vector; abstract Finsupp weight and scalar multiplication. Each form ran Finder, LeanSearch, Loogle, local search and pinned `rg`. External index revisions may differ from the pinned checkout. Local index reported `unavailable`, even when source hits were returned; empty local results are not absence certificates.

| Form | Finder | LeanSearch | Loogle | Local | pinned rg |
|---|---|---|---|---|---|
| Current | `Finsupp.weight_single`, `Fintype.sum_single_smul` | `Finsupp.sum_nsmul`, `univ_sum_single_apply` | Initial `"sum"` too broad; retry `Finsupp.single, HDiv.hDiv` returns irrelevant basis repr quotient | Roth and Finsupp weight singleton hits; index unavailable | Source and caller search, direct quotient form is project-local |
| Literature | Weighted homogeneous monomial API | Weighted-degree and singleton search results archived | `Finsupp.single` gives low-level API, not ratio formula | `sum_single_index` source-name hits partial; unavailable index | Generic finite-support sum and singleton facts located |
| Abstract | `Finsupp.weight_single` exact | `Finsupp.weight_single` exact | `Finsupp.weight, Finsupp.single` exact | Pinned source match exists, unavailable index | Weight.lean:96–98 exact generic theorem |

Raw full formal-search receipts are [current Finder](../evidence/Roth.weight_single/search-current-finder.json), [current LeanSearch](../evidence/Roth.weight_single/search-current-leansearch.json), [current Loogle](../evidence/Roth.weight_single/search-current-loogle.json), [Loogle retry](../evidence/Roth.weight_single/search-current-loogle-retry.json), [current local](../evidence/Roth.weight_single/search-current-local.json), [literature Finder](../evidence/Roth.weight_single/search-literature-finder.json), [literature LeanSearch](../evidence/Roth.weight_single/search-literature-leansearch.json), [literature Loogle](../evidence/Roth.weight_single/search-literature-loogle.json), [literature local](../evidence/Roth.weight_single/search-literature-local.json), [abstract Finder](../evidence/Roth.weight_single/search-abstract-finder.json), [abstract LeanSearch](../evidence/Roth.weight_single/search-abstract-leansearch.json), [abstract Loogle](../evidence/Roth.weight_single/search-abstract-loogle.json), [abstract local](../evidence/Roth.weight_single/search-abstract-local.json), [pinned weight search](../evidence/Roth.weight_single/source-search-1.json), [pinned sum search](../evidence/Roth.weight_single/source-search-2.json).

Positive candidate signatures were independently checked by root and source read: `Finsupp.weight_single` in `Mathlib/Data/Finsupp/Weight.lean:96`, `weight_eq_sum` at line 100; `Finsupp.sum_fintype` and `sum_single_index` are generated additive counterparts in `Mathlib/Algebra/BigOperators/Finsupp/Basic.lean` (native signatures resolve even when literal source-name grep misses generated declarations). `Finsupp.weight_single_index` varies the weight FUNCTION, whereas our theorem varies the FINITE MULTI-INDEX: it is not a same-statement hit. `univ_sum_single_apply` lacks varying denominators. `Fintype.sum_single_smul` uses Pi.single and scalar form, so cast and reciprocal conversion remain.

Conclusion: generic structural theorem found; no exact same-parent ratio result or ≤3-fact normalization certificate established. A search failure would not itself establish absence.

## Phase 5.5 — statement shape

1. Normal form: singleton weight reduces on the left to scalar quotient on the right, appropriate rewrite direction. `Finsupp.weight` scalar-multiplication form is canonical for abstract weights; `n/r j` is natural for the project's denominator parameters. Native `via_bundled` checks equality of the representations, not definitional equality.
2. Syntactic generality: reversed equality compiled as `WeightSingleConsumerChecks.reversed`; useful for rewriting backwards but no stronger theorem. General zero-preserving kernel and division-valued forms compiled. A bundled hom equality is unnecessary for evaluation at a supplied singleton, and existing upstream API already offers it.
3. Superfluous arguments: r,j,n each affect the expression; no explicit hypotheses. DecidableEq already absent; Fintype is needed by the parent. Broadening coefficients/target requires parent replacement.

Verdict: KEEP current statement locally; RESTATE-BEFORE-SHIP if proposing any abstract result, because upstream already owns the broader form. No new independent ratio theorem is justified merely by the spelling.

## Phase 6.0 — all explicit callers and inline audit

Actual source grep yields exactly two references outside the declaration. There is no simp attribute. This is source-level usage, not the opaque kernel/simp dependency closure.

| Caller | Line | Role | Concrete future plan |
|---|---|---|---|
| private `Roth.card_filter_fiber_eq` | Lattice.lean:155 | After additivity and injective mapDomain, replace weight of `single (Fin.last n) i` by i/r(last n); reduces filtered-fiber threshold. | Keep current lemma; if deleting it locally, bind a local singleton equality with the four-fact proof below and replace the `weight_single` item in this `rw` list with that equality. If migrating parent, specialize `Finsupp.weight_single` to reciprocal weights after the separately checked bridge. `fin_split` compiles the exact Fin-last rewrite shape. |
| `Roth.sum_max_sub_le_index_det` | Theta.lean:391 | At h1, split Option.some derivative weight plus `single none ν`; obtain ν/r none for determinant index lower bound. | Keep current lemma; a local equality proved by the same four-fact term can replace the `rw ... at h1` item, with j=none and n=ν. Parent migration instead needs reciprocal-weight bridge before existing generic singleton evaluation. `option_split` compiles the exact Option-none shape. |

Internal explicit use count K=2, external caller files=2. Inline-derivation search `weight.*single|single.*weight` finds these same callers, the theorem and its proof only. The inspected complete caller modules contain other single-coordinate Finsupp calculations, but no additional standalone derivation of this quotient singleton-weight formula. No dead-code claim: the lemma serves two distinct mathematical steps. [Actual source grep](../evidence/Roth.weight_single/source-search-0.json), [native caller source](../evidence/Roth.weight_single/project-relevant-excerpt.lean.txt), [caller terminal receipt](../evidence/Roth.weight_single/native-project.json).

These are compiled caller fragments. Neither entire migrated Lattice nor Theta module was edited or rebuilt, and whole-file migration is not claimed.

## Phase 6 — actual composition experiments and honest count

Native same-parent direct proof:

```lean
  have hzero : ∀ i : σ, ((0 : ℕ) : ℝ) / (r i : ℝ) = 0 := fun i ↦
    (congrArg (fun x : ℝ ↦ x / (r i : ℝ)) (Nat.cast_zero (R := ℝ))).trans (zero_div _)
  exact (Finsupp.sum_fintype (Finsupp.single j n)
    (fun i m ↦ (m : ℝ) / r i) hzero).symm.trans
      (Finsupp.sum_single_index (hzero j))
```

This uses **four distinct domain facts**: `Nat.cast_zero`, `zero_div`, `Finsupp.sum_fintype`, `Finsupp.sum_single_index`. The universal hzero proof is built once and passed to `sum_fintype`, then its specialization at j is passed to `sum_single_index`. Counting occurrences of reused local certificates is different from counting distinct domain lemmas; neither hides the cast fact. Equality congruence/transitivity/symmetry are structural core operations, not new domain API. With those counted as calls too the term is longer still. This is a reproducible four-fact certificate, not evidence of an absolute lower bound against every imaginable three-call proof. It evaluates composition in the original representation only; the dependent-lemma re-aim rule routes the verdict using the existing generic parent API instead.

Other actual native experiments:

- `arbitrary_weight`: one existing `Finsupp.weight_single` call, arbitrary semiring/module and no finite ambient type. This is the abstract theorem already upstream, not the original representation.
- `finite_kernel`: two existing domain facts with zero-preservation supplied as hypothesis. This new helper is not an existing replacement and does not absorb the original zero-cast proof for free.
- `finite_division`: three distinct facts (`sum_fintype`, `sum_single_index`, `zero_div`), with zero_div used at both the universal kernel and selected index. Coefficients are K-valued, avoiding the original natural cast; this is a changed statement.
- `support_division`: two distinct facts (`sum_single_index`, `zero_div`), without Fintype, but the definition changes to support summation with K-valued coefficients.
- `via_bundled`: `simpa [original, Finsupp.weight_eq_sum, nsmul_eq_mul, div_eq_mul_inv] using Finsupp.weight_single ...`. This is a verified bridge, with at least the generic theorem plus three independent named normalization facts, not a ≤3-fact same-parent term. A single tactic invocation is not a call-count certificate.
- Source replay `simp [Roth.weight, Finsupp.single_apply, ite_div]` succeeds. Its closing simp alone does not supply a NO-composable certificate. Final NO-mathlib-has-it instead follows from the explicit re-aim rule and verified analogous upstream theorem.
- Zero denominator, nonzero denominator and a negated incorrect zero conclusion were checked on Unit. Infinite ambient ℕ is supported by the bundled form. No sorry, raised limits, unsafe or native_decide was used for these proofs.

[Raw exact executions](../evidence/Roth.weight_single/raw-executed.lean.txt), [target relevant excerpt](../evidence/Roth.weight_single/target-relevant-excerpt.lean.txt), [native receipts and hashes](../evidence/Roth.weight_single/verification.json). Composition conclusion: no certified ≤3 existing-call composition for the exact original parent statement. After the mandatory parent re-aim, singleton evaluation is one call to the already existing `Finsupp.weight_single`; the verified normalization bridge specializes it back to the quotient notation. This supports NO-mathlib-has-it under the re-aim rule, not NO-composable based on original proof length.

## Phases 7–8 — actionable verdict

**NO-mathlib-has-it.** The command’s explicit re-aim rule (mathlibable.md, Mode B, “Re-aim rule”, lines 1192–1207 in the installed version) says that when a parent is NO-mathlib-has-it because a more general definition D′ exists, a dependent lemma is re-aimed at D′; if D′ has the analogous lemma, record NO-mathlib-has-it citing that lemma. Parent `Roth.weight` already has that assessment. We independently verified the required hit: `Finsupp.weight_single`, `Mathlib/Data/Finsupp/Weight.lean:96–98`. This is a checked re-aim, not blind inheritance from a parent name or a verdict selected from source proof length.

Native verified follow-from in quotient notation (the exact raw source names its mirror `original`):

```lean
by simpa [original, Finsupp.weight_eq_sum, nsmul_eq_mul, div_eq_mul_inv] using
  Finsupp.weight_single (fun i ↦ (r i : ℝ)⁻¹) j n
```

With parent API migrated, the theorem itself becomes exactly `Finsupp.weight_single (fun i ↦ (r i : ℝ)⁻¹) j n`; `n • (r j : ℝ)⁻¹` is its canonical scalar RHS. The bridge above is a closing simp with normalization facts; it is not being misrepresented as a ≤3-call original-representation composition. The existing analogous theorem and explicit re-aim rule are what justify the verdict. The independent four-fact proof remains useful evidence of the old representation and a fallback local refactor, but creates no new mathematical gap.

Actionable refactor plan at all K=2 explicit caller sites:

1. Coordinate with the separately assessed parent migration: implement the weight operation through `Finsupp.weight (fun i ↦ (r i : ℝ)⁻¹)`, preserving a quotient-sum bridge where needed. This assessment does not claim the entire parent migration has been compiled or performed.
2. At `Roth/Lattice.lean:155`, after `weight_add` and the Fin.castSucc `weight_mapDomain` rewrite, replace the singleton rewrite with `Finsupp.weight_single` specialized to `Fin.last n` and i. Normalize natural smul and inverse product to `i / r (Fin.last n)` using `nsmul_eq_mul` and `div_eq_mul_inv`; the native `fin_split` fragment confirms the original caller’s type flow.
3. At `Roth/Theta.lean:391`, in h1 after Option.some `weight_mapDomain`, use the same generic theorem with j=none and n=ν, then the same scalar-to-quotient normalization. The native `option_split` fragment confirms the original caller’s type flow. Do not count the project-local add/mapDomain facts as mathlib building blocks.
4. Once the parent migration and both complete caller modules compile, delete the redundant `Roth.weight_single` theorem, or retain only a project-local compatibility wrapper during transition. The existing `Roth/Box.lean` weight API is the appropriate alternative local destination for such a wrapper; `Archive/` adds no value for an existing generic identity.

No production edits were made. The fragments establish local substitution shapes, not completion of the proposed multi-file refactor. No additional upstream PR for a duplicate singleton theorem is warranted. Generalization and cleanup PR grouping/reviewer requirements apply to YES verdicts and are n/a here. Root’s initial emphasis on original four-fact count was corrected during independent review by applying the explicit re-aim rule; the final report uses the rule while preserving all executed mathematical evidence.

Package validation checks all mandatory phases, exact accepted sources against native requests or root execution snapshots, terminal success, diagnostics/axioms, current manifest hashes and bytes, source/pin hashes and portable evidence links. Credential guard is run separately before freeze. [Portable validator](../evidence/Roth.weight_single/validate.py), [assessment record](../evidence/Roth.weight_single/assessment.json), [overview entry](../evidence/Roth.weight_single/overview-entry.json).
