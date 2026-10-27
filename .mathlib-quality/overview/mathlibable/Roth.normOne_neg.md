# Roth.normOne_neg — full mathlibable assessment

**Declaration 83/293; NO-composable-from-mathlib.** The coefficient length is unchanged by negating every coefficient. The exact existing Finsupp negation reindexing law, integer cast negation and absolute-value negation give the result. This is an independent assessment, not an inherited parent verdict. Production sources remain unchanged.

## Phase 0 — doctor and exact source

The shared baseline completed `lake build` successfully (2467 jobs, no warnings/errors). All 17 source/pin hashes freshly match its manifest. The full declaring module was read, including the determinant consumer, and the separate `index_neg` inline-search candidate was inspected. Source lines 86–87 contain the theorem. Native `#check`, `#print` and original replay succeed with only standard axioms. [Baseline](../evidence/Roth.normOne_neg/baseline-build.txt), [fresh inputs](../evidence/Roth.normOne_neg/inputs.json), [hash gate](../evidence/Roth.normOne_neg/input-hash-check.json), [entire module](../evidence/Roth.normOne_neg/source-module.lean.txt), [canonical metadata](../evidence/Roth.normOne_neg/canonical-entry.json), [native original](../evidence/Roth.normOne_neg/native-original-success.json).

## Phase 1 — comprehend

For any integer polynomial in any variable type, the sum of the absolute values of its coefficients equals the corresponding sum for its negative. Negation preserves the nonzero exponent support, and each absolute coefficient is unchanged. The statement concerns the coefficient vector, rather than values of the polynomial on a domain.

Full native type:

```lean
∀ {σ : Type u_1} (P : MvPolynomial σ ℤ), Roth.normOne (-P) = Roth.normOne P
```

`σ` is arbitrary, without finite/decidable/nonempty instances. `P` is the only explicit argument. There are no theorem hypotheses, degree bounds or sign premises. The parent fixes integer coefficients and real output. The sole project dependency in statement and original proof is `Roth.normOne`. The printed proof uses support equality, finite-sum congruence, `Int.cast_neg`, `abs_neg` and structural equality normalization. [Executed original](../evidence/Roth.normOne_neg/native-original-executed.lean.txt).

## Phase 2 — size and one-line check

**SMALL**: elementary coefficient-norm law, no new structure, named theorem or main project result. Phase 2b definition-only one-line test is **n/a: theorem**. The short `simp [normOne]` proof is not, by itself, sufficient for a NO verdict: Phase 6b classifies unstructured closing simp compositions as borderline. All literature channels and explicit composition experiments below were still performed.

## Phase 3 — exhaustive literature

Every named channel was actually queried. Web artifacts preserve exact requests, response SHA256/bytes/status, returned titles/URLs/locators and original concise summaries; no full web bodies are archived. Returned URL query parameters were stripped from archived locators before persistence.

| Channel | Exact query or local action | Result and interpretation |
|---|---|---|
| General web, specific | `polynomial coefficient l1 norm invariant negation` | Coefficient l1 applications; an unaudited Lean companion names negation invariance, supplementary only. [Receipt 0](../evidence/Roth.normOne_neg/web-0.json). |
| General web, general | `normed vector space norm of negative vector absolute homogeneity` | MIT functional-analysis Chapter 1 defines absolute homogeneity; setting scalar to −1 recovers negation invariance. [Receipt 1](../evidence/Roth.normOne_neg/web-1.json). |
| General web, alias | `coefficient length polynomial sum absolute coefficients norm` | University of Debrecen manuscript defines multivariate integer polynomial length as sum of absolute coefficients, distinct from height. [Receipt 2](../evidence/Roth.normOne_neg/web-2.json). |
| ChatGPT math MCP | Standard form, generality, history | n/a: `ask_chatgpt_math` unavailable in enabled tools. No fabricated response or historical evolution claim. |
| Local reference | `clean.tex` lines 437–497, with fresh search/hash | §3 uses coefficient l1 and states signs have absolute value 1 (line 475), precisely the determinant application. [Excerpt](../evidence/Roth.normOne_neg/local-literature.txt), [hash](../evidence/Roth.normOne_neg/local-literature-source.json), [search](../evidence/Roth.normOne_neg/rg-local-literature.json). |
| nLab | `site:ncatlab.org/nlab normed vector space norm negation` | Norm definition on an abelian group includes integer homogeneity, hence −1 invariance. [Receipt 3](../evidence/Roth.normOne_neg/web-3.json). |
| nCatLab | `site:ncatlab.org/ncatlab normed abelian group` | Search returns nLab norm, no distinct categorical extension established. No access failure is invented. [Receipt 4](../evidence/Roth.normOne_neg/web-4.json). |
| Stacks | `site:stacks.math.columbia.edu normed vector space norm` | Tag 0BIF discusses determinant norms of field extensions, a different object. No useful coefficient l1 law; not an algebraic-geometry generalization. [Receipt 5](../evidence/Roth.normOne_neg/web-5.json). |
| MathOverflow | `site:mathoverflow.net polynomial coefficient norm l1` | Question 465899 explicitly uses the sum of absolute coefficients for integer polynomials. Discussion of extremal multiples does not alter sign invariance. [Receipt 6](../evidence/Roth.normOne_neg/web-6.json). |
| Recent arXiv | `site:arxiv.org polynomial coefficient l1 norm after:2021-10-27 before:2026-10-28` | Results include approximation/Fourier norm papers and tensor l1; none establishes a different standard sign-invariance formulation. Search publication/revision labels are not assumed to be original dates. [Receipt 7](../evidence/Roth.normOne_neg/web-7.json). |

Literature synthesis: coefficient l1 is standard, also called polynomial length. Negation invariance is the norm symmetry law, a special case of absolute homogeneity. The elementary proof needs only an invariant coordinate size and finite support; vector-space structure is unnecessary. Integral L1 on a circle, maximum coefficient height, Bombieri norm, Mahler measure and field-extension norm are distinct quantities. These searches establish standard terminology and general forms, not a novel history of the law.

## Phase 4a — parameters and generality

| Component | Current interface | Verified expanded representation |
|---|---|---|
| `σ : Type*` | Already arbitrary, no typeclasses | Replace exponent index by arbitrary Finsupp index `ι`. |
| `P` | Essential polynomial argument | Any `f : ι →₀ G`. |
| Coefficients | Integer ring fixed by parent | `[SubtractionMonoid G]` suffices for the existing negation reindexing law; ring operations and coefficient order are unused. |
| Values | Real absolute values of integer casts | Arbitrary `[AddCommMonoid M]` output and indexed `size : ι → G → M`. |
| Coordinate hypotheses | Cast absolute value is zero-preserving and sign-invariant | `∀ i, size i 0 = 0` and `∀ i x, size i (-x) = size i x` suffice. |
| Additional assumptions | None to remove | No positivity, order, triangle inequality, multiplication, scalar field, completeness or finite variable set is required. |

## Phase 4b — generality verdict

**MAXIMALLY GENERAL at the fixed parent interface**: no theorem premise can be dropped and the variable type is unrestricted. Expanded Finsupp form is actually verified in both target and isolated environments:

```lean
theorem generic {ι G M : Type*} [SubtractionMonoid G] [AddCommMonoid M]
    (size : ι → G → M) (hzero : ∀ i, size i 0 = 0)
    (hneg : ∀ i x, size i (-x) = size i x) (f : ι →₀ G) :
    (-f).sum size = f.sum size := by
  simpa only [hneg] using (Finsupp.sum_neg_index (g := f) (h := size) hzero)
```

This helper is newly written assessment code and is not counted as an existing mathlib replacement. Its assumptions are sufficient, not claimed minimal: for genuine additive groups support-neg equality can avoid zero-preservation of the size. No unexecuted hypothetical weakening is claimed verified. Changing the parent representation would be a broader refactor, not dropping a class on this theorem. [Verified target/general form](../evidence/Roth.normOne_neg/native-target-consumers-executed.lean.txt), [native receipt](../evidence/Roth.normOne_neg/native-target-consumers-success.json), [isolated source](../evidence/Roth.normOne_neg/native-raw-executed.lean.txt).

## Phase 4c — nine modern-idiom rows

| # | Question | Answer and consequence |
|---|---|---|
| 1 | Preambles to typeclasses | No explicit predicates to bundle; expanded form uses standard additive classes. |
| 2 | Sequences/metrics to filters | No convergence, so no filter reformulation. |
| 3 | Construction to universal property | No object construction or needed universal-property class. |
| 4 | Closure predicates to substructures | No closure predicate/subobject lattice. |
| 5 | Hierarchy weakening | Yes after representation expansion: SubtractionMonoid coefficients and additive output suffice. |
| 6 | Higher-categorical form | No categorical content or supported extension. |
| 7 | Concrete indices/structures | `σ` is already arbitrary; abstract coordinate Finsupp and additive size remove the fixed integer/real arithmetic. |
| 8 | Concrete-via-abstract diagnostic | Fires: after unfolding `normOne`, no parent-specific content remains; the printed proof uses support-neg equality and invariant coordinate values. The tested generic form shares the same sign invariance across arbitrary indexed sizes. |
| 9 | False-generalization guard | Pass: specialization recovers the same finite coefficient l1 sum. Replacing by a sup norm, circle integral, field norm or arbitrary polynomial-function norm changes the object and is rejected. |

The generic negation reindexing API already exists; it organizes coordinatewise sign invariance without polynomial-only API. This is a real sharing of proofs across coefficient types, not a reason to add a new unneeded wrapper. Modern-idiom verdict: use existing Finsupp reindexing plus coordinate normalization.

## Phase 4.5 — infrastructure risks

n/a: theorem introduces no new definition, class, instance or coercion. All six risks—typeclass diamonds, reducibility leaks, noncanonical unfolding, priority collisions, universe infrastructure and coercion ambiguity—are theorem-n/a. No L1 instance or competing norm structure is installed.

## Phase 4.6 — five proof-strategy rows

| # | Question | Result |
|---|---|---|
| 1 | ε–δ versus filters | No topology argument. |
| 2 | Elements versus subobject inclusions | Coordinate invariance is intrinsic; no inclusion reformulation. |
| 3 | Sequences versus nets | No limits. |
| 4 | Construction versus universal property | No construction. |
| 5 | Missing helpers | Existing `Finsupp.sum_neg_index` handles the nontrivial finite-support bookkeeping. No new helper is needed for the checked replacement. |

Strategy **MATHLIB-IDIOMATIC** locally: original simplification is direct and short. Explicit named reindexing is preferable as replacement evidence because it identifies the actual existing abstract law. No cost-based verdict downgrade is used.

## Phase 5 — all five actual mathlib methods on three forms

| Method | Current coefficient form | Standard norm form | Abstract finite-support form |
|---|---|---|---|
| Lean-Finder | Symmetric-polynomial negation and nearby results, not the target law | `norm_neg` | Exact `Finsupp.sum_neg_index`. |
| Loogle | Malformed quoted query retained; first retry rate-limited; successful second retry yields `MvPolynomial.coeff_neg` | Exact `norm_neg` | Exact `Finsupp.sum_neg_index` signature. |
| LeanSearch | `IsAbsoluteValue.abv_neg` and sign facts | Lp norm-neg family | DFinsupp negated-index law and nearby Finsupp results. |
| `rg` pinned sources | No `normOne_neg` spelling in mathlib | Generic norm-neg and polynomial norm family | `prod_neg_index` has `@[to_additive]`, generating `sum_neg_index` that is absent as a literal theorem spelling. |
| Local search | Project `Roth.normOne_neg` | Norm-neg family | Empty `sum_neg_index` result; index marked unavailable, never absence evidence. |

[All raw formal receipts](../evidence/Roth.normOne_neg/formal-search.json), [current rg](../evidence/Roth.normOne_neg/rg-current.json), [standard rg](../evidence/Roth.normOne_neg/rg-literature.json), [abstract rg](../evidence/Roth.normOne_neg/rg-abstract.json), [untruncated full-name rg](../evidence/Roth.normOne_neg/rg-full-name.json). External indexes may differ from the pinned revision. All candidate claims used for the verdict have native pinned checks, rather than relying on external search alone.

Pinned key API:

```lean
Finsupp.sum_neg_index
  {α M G : Type*} [SubtractionMonoid G] [AddCommMonoid M]
  {g : α →₀ G} {h : α → G → M} (h0 : ∀ a, h a 0 = 0) :
  (-g).sum h = g.sum (fun a b => h a (-b))
```

Source: `Mathlib/Algebra/BigOperators/Finsupp/Basic.lean:265–268`, generated from the multiplicative theorem. `Int.cast_neg` is in `Mathlib/Data/Int/Cast/Basic.lean`; `abs_neg` is in `Mathlib/Algebra/Order/Group/Unbundled/Abs.lean`. `norm_neg` requires a matching bundled seminormed group and is not automatically a theorem about the project coefficient sum. The existing polynomial norm concerns a different norm. [Finsupp source](../evidence/Roth.normOne_neg/mathlib-finsupp-basic.lean.txt), [polynomial norm source](../evidence/Roth.normOne_neg/mathlib-norm.lean.txt), [pinned source hashes](../evidence/Roth.normOne_neg/mathlib-inputs.json), [native exact signatures](../evidence/Roth.normOne_neg/native-target-consumers-success.json).

## Phase 5.5 — three statement-shape checks

Normal form: `normOne (-P) = normOne P` is correctly oriented for eliminating negation; no inequality normalization issue. Syntactic generality: original replay, direct Finsupp expression and indexed invariant-size statement all compile. Finsupp form exposes the reusable existing law; original is convenient inside determinant sign simplification. Superfluous argument audit: `σ` and `P` occur essentially, no unused theorem hypothesis/class. **SHIP-AS-STATED locally** as an existing interface, but do not upstream the redundant specialization; any local deletion uses the concrete caller plan below.

## Phase 6.0 — every explicit caller and inline audit

One explicit source occurrence beyond the declaration, one named caller, zero external-to-module callers:

| Caller | Exact use | Refactor plan |
|---|---|---|
| `Roth.normOne_det_le`, `Roth/CoeffNorm.lean:119–128` | Line127 `simpa [h, normOne_neg]` removes the sign of the product in the determinant expansion | Before the permutation-sign cases, introduce a local quantified negation identity using the explicit Finsupp composition below; replace the simp-list item by that local fact. Keep `normOne_prod_le` and entry bounds unchanged. The complete determinant proof is freshly replayed using the checked replacement identity. |

Inline search finds `Roth.index_neg` using support-neg for an entirely different index statistic, not another coefficient-length derivation. No independent inline coefficient-length symmetry proof was found. This theorem is not dead code. [Caller search](../evidence/Roth.normOne_neg/rg-callers.json), [inline search](../evidence/Roth.normOne_neg/rg-inline.json), [caller scope](../evidence/Roth.normOne_neg/callers.json).

Fresh canonical direct-proof audit: requested293, present293, values293, sole direct consumer `Roth.normOne_det_le`, including all canonical private and LeanEval entries. This is written-value constant occurrence, not a transitive, opaque/generated-helper dependency closure or a claim about external users/future simp behavior. The native complete determinant replay succeeds with standard axioms. [Fresh consumer/audit source](../evidence/Roth.normOne_neg/native-target-consumers-executed.lean.txt), [full receipt](../evidence/Roth.normOne_neg/native-target-consumers-success.json).

## Phase 6 — actual composition experiments

The original proof is closing `simp [normOne]`; standing alone it would receive Phase6b's borderline treatment. The separately tested direct replacement explicitly specializes an existing abstract identity:

```lean
  change (-P.coeff).sum (fun _ (z : ℤ) ↦ |(z : ℝ)|) = P.coeff.sum (fun _ (z : ℤ) ↦ |(z : ℝ)|)
  simpa only [Int.cast_neg, abs_neg] using
    (Finsupp.sum_neg_index (g := P.coeff) (h := fun _ (z : ℤ) ↦ |(z : ℝ)|) (by simp))
```

The three core mathematical facts are `Finsupp.sum_neg_index`, `Int.cast_neg`, `abs_neg`. The zero-preservation parameter additionally normalizes `Int.cast_zero` and `abs_zero`; these are explicitly acknowledged structural/parameter normalization, not hidden as absent calls. The `change` succeeds definitionally through coefficient Finsupp representation and its negation. After the existing reindexing theorem, only pointwise cast and sign normalization remains: no new finite-support lemma, support argument, inequality or representation bridge is proved. This is a named-law specialization with parameter normalization, rather than the unstructured `simp [defs]` argument alone. Verdict COMPOSABLE under the three-core-fact criterion.

The new generic assessment helper is not part of that existing-call count. Native isolated proof imports only the stable 13 mathlib modules, asserts `#check_failure Roth.normOne_neg`, and proves both direct and general forms without importing Roth. Thus no target/downstream simp circularity is used. [Raw source](../evidence/Roth.normOne_neg/native-raw-executed.lean.txt), [raw receipt](../evidence/Roth.normOne_neg/native-raw-success.json). Parent `Roth.normOne` was NO-composable via Finsupp aggregation, not NO-has-it through a replacement parent. No Mode B parent re-aim override or inherited verdict is used. Unlike the preceding triangle inequality, the exact generic negation reindexing operation already exists.

## Phase 7 — verdict and actionable local plan

**NO-composable-from-mathlib.** Standard coefficient l1 symmetry has no new mathematical content here: existing Finsupp negation reindexing reduces it to integer-cast negation and absolute-value symmetry. Full original, generic, isolated and complete consumer experiments succeed. This verdict rests on the explicit named existing law and its normalization, not on theorem length, a failed absence search or an inherited parent result.

Building blocks and paths are enumerated in Phase5; parameter normalization also uses `Int.cast_zero` and `abs_zero`. To implement the recommended local cleanup, delete `Roth.normOne_neg`, introduce the displayed composition as a proof-local `hneg : ∀ P : MvPolynomial σ ℤ, normOne (-P) = normOne P` within `Roth.normOne_det_le`, then replace the single `normOne_neg` simp-list item by `hneg`. The checked complete consumer substitutes the same verified identity; no coefficient or determinant inequality changes. A subsequent production cleanup should inline/localize the identity rather than export a new wrapper. Record the Finsupp API in the module's mathlib-usage documentation if that cleanup is undertaken.

Alternative destination if API stability warrants retaining the spelling: the present downstream `Roth/CoeffNorm.lean`, as a project-specific coefficient-length convenience, not mathlib/Archive. This assessment is read-only and does not perform deletion. No upstream PR, new helper, reviewer selection or YES grouping is proposed because the result is redundant as a contribution.

## Phase 8 — verification and portable handoff

Three fresh complete native receipts cover original target replay, target/general form plus entire determinant and293 audit, and isolated mathlib-only replacement. Accepted runs have success=true, partial=false where applicable, no timeout, errors, warnings, failed dependencies or nonstandard axioms; no rejected native attempts exist. Search failures are separately retained. Requested fragments are preparation artifacts, not mislabeled execution.

All phases PASS or justified theorem-n/a; unresolved=[]; root acceptance pending independent review. Production and pins unchanged. Package includes [assessment](../evidence/Roth.normOne_neg/assessment.json), [verification](../evidence/Roth.normOne_neg/verification.json), [overview entry](../evidence/Roth.normOne_neg/overview-entry.json), [generality](../evidence/Roth.normOne_neg/generality.json), [current manifest](../evidence/Roth.normOne_neg/copy-manifest.json), [portable validator](../evidence/Roth.normOne_neg/validate.py). Validator supports scratch/integrated layouts and always checks the current manifest, while historical worker manifests and integration-added root acceptance are exempt from inventory. It checks every source/pin/archive hash and byte count, complete native success/standard axioms, all formal and literature channels, every local report link and credential scan. No optional follow-up experiments remain required.
