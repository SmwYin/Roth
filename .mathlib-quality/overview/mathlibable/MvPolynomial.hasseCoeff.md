# Full /mathlibable assessment — `MvPolynomial.hasseCoeff`

**Category: NO-composable-from-mathlib (standalone declaration).** The value is exactly `Finsupp.prod d (fun j n ↦ Nat.choose (k j) n)`: two existing mathlib operations, with no proof or extra algebraic structure. A semantic name is useful to the project's Hasse derivative API, but this declaration alone contributes no missing operation. This assessment does not decide the inclusion of `hasseDeriv` or any coefficient identity, and does not delete or change any production source.

Assessment date: 2026-10-26. Input: branch `ramin-cleanup`, commit `99f19fda4b3cbee38fc0d31af76075834f5cc265`. Pinned mathlib: `5ed2965256430c3649e86755f9576b54eca72435` (v4.34.0). Scope: one declaration at `Roth/HasseDeriv.lean:50`.

Evidence links below target the intended tracked layout: this report in `.mathlib-quality/overview/mathlibable/`, all supporting files in `.mathlib-quality/overview/evidence/MvPolynomial.hasseCoeff/`. The complete supporting directory can be copied intact; no temporary path is needed to reproduce a check. Historical compiler receipts retain the exact original command and working directory. Re-run `python3 <evidence-directory>/run-probes.py` from the project root.

## Phase 0 — Doctor

- `lake build`: **PASS**, exit 0, 2467 jobs. Reused the shared baseline build, not a new build; its input matches this declaration's unchanged source hash and pins. See [build receipt](../evidence/MvPolynomial.hasseCoeff/baseline-build.txt), [baseline manifest](../evidence/MvPolynomial.hasseCoeff/input-manifest.json), and [current hashes](../evidence/MvPolynomial.hasseCoeff/source-manifest.json) and [17/17 baseline hash comparison](../evidence/MvPolynomial.hasseCoeff/baseline-hash-verification.json).
- Declaration resolves: **PASS**, one definition at `Roth/HasseDeriv.lean:50`.
- Kind: `def`; no `sorry`; no new axioms. `#print axioms` gives only `propext`, `Classical.choice`, `Quot.sound`.
- Module: constructs multivariate Hasse derivatives and proves their coefficient, composition, partial derivative and univariate compatibility laws.
- Actual elaborated type, obtained from the compiler rather than inferred from the section variables:

```lean
@MvPolynomial.hasseCoeff.{u} :
  {σ : Type u} → (σ →₀ ℕ) → (σ →₀ ℕ) → ℕ
```

In particular, **neither `R` nor `[CommSemiring R]` is an argument**. [TargetProbes.lean](../evidence/MvPolynomial.hasseCoeff/TargetProbes.lean), [raw compiler log](../evidence/MvPolynomial.hasseCoeff/TargetProbes.log), [receipt](../evidence/MvPolynomial.hasseCoeff/TargetProbes.receipt.json): exit 0, 136.62 seconds. No redundant project build was run.

## Phase 1 — Comprehend

For natural multiindices `d` and `k`, this defines the multi-index binomial coefficient
`B(d,k) = ∏_{j ∈ supp(d)} binom(k_j,d_j)`. It counts independent choices of `d_j` occurrences from `k_j` occurrences in each coordinate. Coordinates outside `supp(d)` have lower index zero and hence factor one, so the product is well-defined for any variable type; it is zero when some `d_j > k_j`. The lower index is the first Lean argument, reversing the usual displayed top/bottom order of `binom(k,d)`.

| Lean parameter | Mathematical role |
|---|---|
| `{σ : Type u}` | Arbitrary variable/index type, universe-polymorphic; no finiteness or decidable equality assumption |
| `d : σ →₀ ℕ` | Lower multiindex / differentiation multiplicities; its finite support indexes the product |
| `k : σ →₀ ℕ` | Upper multiindex / monomial exponents; only its coordinate values are inspected |

Hypotheses: none. Conclusion: a natural number. Conclusion (Lean): n/a, definition; result type `ℕ`.

## Phase 2 — Preliminary checks

**Size: SMALL.** It is a scalar combinatorial helper, not a new mathematical structure or a named theorem. Listing it among the module's main definitions does not make it a main-result theorem. The exhaustive literature protocol still applies.

**Body: one substantive line; ONE-LINER WITH-EXEMPTION.**

| Exemption | Applies? | Evidence |
|---|---|---|
| Avoid defeq abuse | No | Both orientations of equality with the body compile by `rfl`; downstream `simp [hasseCoeff]` explicitly unfolds it. No evidence of a deliberately sealed unfolding barrier. |
| Avoid diamonds | No | It returns the existing type `ℕ`, introduces no type or instance, and consumes only the existing `Zero ℕ`/`CommMonoid ℕ` structures in `Finsupp.prod`. |
| Semantic intent / API stability | Yes | The docstring and name identify the scalar in `hasseDeriv`, `coeff_hasseDeriv`, `hasseDeriv_hasseDeriv`; `MvPolynomial.hasseCoeff_single_add_eq` and `Roth.abs_coeff_hasseDeriv_le` consume it outside the declaring file.  |

The semantic exemption establishes legitimate local API value. It does not turn a two-operation construction into independent mathematical content under this command's composition criterion.

## Phase 3 — Exhaustive literature protocol

All requested channels were checked or have the specific unavailable/inapplicable reason below. Exact queries, source titles, URLs, access outcomes and original summaries are retained in [literature.json](../evidence/MvPolynomial.hasseCoeff/literature.json); the root's three initial web query receipts are [root-web-presearch.json](../evidence/MvPolynomial.hasseCoeff/root-web-presearch.json). The relevant primary thesis, arXiv survey, recent arXiv paper, Stacks section and ETH notes were opened during this assessment. Failed fetches and irrelevant navigation results are not treated as affirmative evidence.

| Channel | Actual query / inspection | Hit / outcome | Standard form / significance |
|---|---|---|---|
| Web, specific | `multi-index binomial coefficient product binomial Hasse derivatives arbitrary commutative ring` | Yes | Coordinate product for Hasse derivatives; independently checked against the sources below. |
| Web, general | `Hasse Schmidt multivariate divided derivatives arbitrary set variables binomial coefficients` | Yes | Hasse–Schmidt derivations over commutative algebras; finite multidegrees. |
| Web, alias | `multi binomial coefficient finitely supported multiindices coefficient Taylor expansion` | Yes | Multi-index binomial coefficient; distinguish from multinomial coefficient. |
| Web, additional explicit name | `multi-index binomial coefficient definition` | Yes | Sweering, Definition 19, product of coordinate choices. |
| ChatGPT MCP | Capability discovery for `ask_chatgpt_math` | **n/a: ask_chatgpt_math unavailable** | No independent ChatGPT consultation is claimed; absence of this optional tool does not reduce other channels. |
| Local references | Read `.mathlib-quality/references/clean.tex:119–152` | Yes | §1 gives the exact product on monomials, arbitrary commutative semirings, and finitely supported Lean multiindices. [Local excerpt](../evidence/MvPolynomial.hasseCoeff/local-reference-excerpt.tex). |
| nLab | `site:ncatlab.org Hasse Schmidt multivariate binomial coefficient`; exact Hasse–Schmidt derivative entry | Yes | Multivariable definition over commutative rigs uses a product only over differentiated variables. Direct page fetch rejected XHTML; substantive indexed page text was available. |
| nCatLab | `site:ncatlab.org/ncatlab Hasse Schmidt` | No relevant separate categorical formulation; **n/a for categorical generalisation** | This target is a scalar counting function, not a category, functor or universal-property construction. The brief search supplies no reason to categorify it. |
| Stacks | `site:stacks.math.columbia.edu Hasse Schmidt derivation divided powers`; opened tag 07GK | Related, not identical | Divided-power ideal axioms have binomial constants; they do not replace the two-multiindex scalar operation. |
| MathOverflow | `site:mathoverflow.net multi index binomial coefficient Hasse derivative`; opened question 389146 | Yes, contextual | Combinatorial multiindices and factorial quotient under coordinatewise order; ordered derivative lists are a different representation. |
| Recent arXiv, last five years | `site:arxiv.org Hasse derivatives multivariate 2021 2022 2023 2024 2025`, plus 2024 and 2022 variants; opened arXiv:2402.18717 | Related current use | Ghosh's 2024 paper, current revision 2026-10-19, uses univariate Hasse–Schmidt derivatives. It does not supply a different standard scalar coefficient. The older 2018/2020 survey is recorded separately as historical/general context, not as recent evidence. |

The primary finite-vector formula is in [Sweering's thesis](https://repository.tudelft.nl/file/File_aefc411b-e29f-4374-a3ab-3d85fbd0f9fc?preview=1), §2-9, Definition 19, (2-48), printed p.14. The [nLab definition](https://ncatlab.org/nlab/show/Hasse-Schmidt%2Bderivative) confirms the support-of-lower-index product in the Hasse setting. [Narváez Macarro's survey](https://arxiv.org/abs/1810.08075) supports characteristic-free commutative-algebra Hasse–Schmidt theory; characteristic zero is relevant to recovering classical derivatives, not to this natural-number coefficient. The [Stacks divided-power section](https://stacks.math.columbia.edu/tag/07GK) and [recent Ghosh paper](https://arxiv.org/abs/2402.18717) were checked for related formulations.

**Literature summary.** The concept is the multi-index binomial coefficient. Sources agree on the coordinate product; some state it only when `d ≤ k`, while the project's `Nat.choose` gives a total function that is zero otherwise. Sources usually use a finite number of variables; finitely supported lower multiindices give the same product over arbitrary variable types. There is no characteristic, coefficient-ring or topology assumption on the scalar count. The named multi-index coefficient is standard; the spelling `hasseCoeff` is project-specific. General Hasse–Schmidt systems or divided-power structures are related larger objects, not stronger restatements of this number.

## Phase 4 — Generality

| Parameter / constraint | Current form | Literature-standard comparison | Weakening / result |
|---|---|---|---|
| Index type | Arbitrary `Type u` | Literature generally uses finitely many coordinates | Already encompasses those cases; no `Fintype` or `DecidableEq` to drop. |
| Lower multiplicities | Finitely supported naturals | Nonnegative multiindices, finite coordinate product | Finite support is the mathematical termination condition for this product. Removing it would need a different product convention. |
| Upper multiplicities | Finitely supported naturals | Finite nonnegative vectors in the usual statement | Finiteness of the upper support is not used in the construction. A verified extension accepts an arbitrary `σ → ℕ`; every current call supplies a monomial multiindex. |
| Codomain | `ℕ` | Natural combinatorial coefficient | Already the natural codomain; coefficient casts belong at consumers. |
| Ring / field / order hypotheses | None in the elaborated type | No ring is needed for the scalar count | Nothing to weaken. Do not mistakenly propose dropping the surrounding section's `[CommSemiring R]`. |

**Generality verdict: MAXIMALLY GENERAL relative to the literature-standard two-multiindex scalar.** Zero literature-required hypothesis weakenings were found. One optional representation extension is mechanically verified: the upper index need not have finite support. This is recorded without claiming the literature requires an infinitely supported upper exponent or that it defines a new monomial. The existing form handles all finite monomial exponent cases and arbitrary variable types. The extension's exact compiled definition and specialization are:

```lean
def upperFunctionCoeff (d : σ →₀ ℕ) (k : σ → ℕ) : ℕ :=
  Finsupp.prod d (fun j n ↦ Nat.choose (k j) n)
example (d k : σ →₀ ℕ) :
    upperFunctionCoeff d k = MvPolynomial.hasseCoeff d k := rfl
```

Cost of that extension: CHEAP; no production change is proposed or made. This does not lead to YES-but-generalise-first because the more permissive construction is also the same two mathlib operations. [Compiled probe](../evidence/MvPolynomial.hasseCoeff/TargetProbes.lean).

### Phase 4c — Modern mathlib idiom

| # | Question | Applies? / conclusion | Reformulation and concrete downstream |
|---|---|---|---|
| 1 | Bundled hypotheses → typeclasses? | No; no hypotheses or structures are supplied. | No new instance would help. |
| 2 | Sequences/metrics → filters/topology? | No; finite natural-number product. | n/a |
| 3 | Construction → universal property? | No; computes a scalar rather than constructing a structured object. | Formal coefficient extraction characterizes the surrounding derivative, not this scalar by itself. |
| 4 | Closure predicates → bundled substructure? | No predicates or substructures occur. | n/a |
| 5 | Field/vector-space assumptions → hierarchy weakening? | No coefficient algebra is present in the actual type. | Natural-number cast API already handles later semiring coefficients. |
| 6 | 1-category → higher category? | No categorical content. | n/a |
| 7 | Concrete natural index → additive abstraction? | No; `Nat.choose` uses natural multiplicities and counting. | Replacing `ℕ` by a generic monoid would change the combinatorial object. |
| 8 | Concrete witness hides abstract proof? | No: body diagnostic finds no concrete witness and no initial unfolding `rw`; the whole body is the generic product of `Nat.choose`. | The optional upper-function extension is above; it is not abstraction of a special concrete witness. |
| 9 | False-generalisation guard | No false generalisation in the optional extension, because it agrees by `rfl` for every original input. | **Reject** treating arbitrary functions as monomial exponents, or replacing this by `Finsupp.multinomial`/a higher category. Those change the intended object. |

**Modern-idiom verdict: no modern mathematical reorganisation needed.** `Finsupp.prod` is already the appropriate support-product idiom; an optional upper-function domain is not a missing abstraction needed by any current caller. No theorem about abstract Hasse–Schmidt systems is smuggled in as a purported weakening of this number.

### Phase 4.5 — Diamond / defeq risk

These are actual checks against the elaborated type, definition and [compiled risk probes](../evidence/MvPolynomial.hasseCoeff/TargetProbes.lean), not six copies of a generic reassurance.

| Risk | Verdict | Checked evidence |
|---|---|---|
| Typeclass diamond | NONE | Definition returns `ℕ` and introduces no instance. `#synth CommMonoid ℕ` selects `Nat.instCommMonoid`; `#synth Zero ℕ` selects the existing inherited zero. Product result uses that existing structure; an ordinary `mul_one` example compiles. There is no new target class/type on which two paths could compete. |
| Reducibility leak | LOW | Ordinary `def`, no `@[reducible]`, `abbrev` or new coercion. Both equalities with the body compile by `rfl`, as expected for a semireducible definition. Product computation is exposed when explicitly unfolded; no global transparency change. |
| Noncanonical unfolding | LOW | Callers explicitly unfold it via `simp [hasseCoeff]`; support orientation is fixed by `d`. `rfl` handles eta-expanded `fun j n ↦ Nat.choose (k j) n`. No simp attribute on the definition installs an extra global rewrite. |
| Instance priority collision | NONE | Not an `instance` and has no priority registration. The probes synthesize pre-existing Nat structures, not an instance produced by this definition. |
| Universe polymorphism | NONE | Actual type is polymorphic in `σ : Type u`. Calls compile for `ℕ : Type 0`, `ULift.{1} ℕ : Type 1`, and generic `σ : Type u`; result stays `ℕ`. |
| Coercion ambiguity | NONE | It is a number, not a `CoeFun`/`CoeSort` carrier. `#synth CoeFun (σ →₀ ℕ) ...` selects existing `DFunLike.toCoeFun` for its input. Calls with outputs in `ℕ` and cast to `ℤ` both compile; no new coercion path is registered. |

**Overall risk: LOW.** No HIGH rows or mitigations required. These risk findings make it technically safe as a local definition; they are not evidence of upstream mathematical necessity.

### Phase 4.6 — Proof strategy

| Check | Applies? | Alternative / cost |
|---|---|---|
| Topological neighbourhood argument → filters | No | No topology. |
| Elementwise algebra → substructure inclusion | No | A scalar finite-product definition; no inclusion argument. |
| Sequence analysis → nets | No | No analysis. |
| Object construction → categorical universal property | No | No structured object. |
| Missing helper that mathlib should supply | No for this declaration | `Finsupp.prod` and `Nat.choose` already compute it. The surrounding derivative's nontrivial laws need their own assessments. |

**Current strategy: MATHLIB-IDIOMATIC.** There is no proof body to shorten; defining the product is the direct construction. No cost-based argument is used in the verdict.

## Phase 5 — Five-method mathlib search

The full search reference and verdict/generalisation/review-stage references were consulted. Source checks use the pinned local revision; online search indices are corroborative and may refer to another snapshot. Lean-Finder used its exposed v4.28.0 default, older than the pinned v4.34.0 library. Local name search explicitly reported `index: unavailable`, so its empty/nonempty results are source fallback information, not a certified complete elaborated index.

| Method | Actual query | Outcome / source verification |
|---|---|---|
| A Lean-Finder | `product of binomial coefficients for two finitely supported natural multiindices Hasse derivative coefficient`; `multi-index binomial coefficient Finsupp choose` | Univariate `Polynomial.hasseDeriv`, its coefficient/monomial/composition laws; `Finsupp.multinomial`, `Ring.choose`. No result returned is an exact two-multiindex coefficient. [Current](../evidence/MvPolynomial.hasseCoeff/finder-current.json), [general](../evidence/MvPolynomial.hasseCoeff/finder-general.json). |
| B Loogle | `Finsupp.prod, Nat.choose`; `Finsupp.prod` | Combined query returned no items; generic query returned `Finsupp.prod`, `prod_fintype`, support and product lemmas. The actual pinned definitions were read and `#check`ed. [Combined](../evidence/MvPolynomial.hasseCoeff/loogle.json), [generic](../evidence/MvPolynomial.hasseCoeff/loogle-general.json). |
| C LeanSearch | `multiindex binomial coefficient product of natural choose on finitely supported functions`; `product over support of a finitely supported function of binomial choose from an arbitrary function` | Multinomial family in the first search; `Finsupp.prod`, `prod_fintype` and more-general finite-support products in the second. [First](../evidence/MvPolynomial.hasseCoeff/search.json), [broader upper-index form](../evidence/MvPolynomial.hasseCoeff/search-general.json). |
| D Source grep | Full untruncated `\bhasseCoeff\b`; broader `prod.*choose|choose.*prod|hasseCoeff|multi.?binom|binom.*multi|Hasse` over all pinned Mathlib sources | Full-name grep exit 1 (no textual hits); broad grep preserved in [mathlib-rg.txt](../evidence/MvPolynomial.hasseCoeff/mathlib-rg.txt). Existing product and scalar choice definitions provide the construction. [Exact grep receipts](../evidence/MvPolynomial.hasseCoeff/grep-receipts.json). |
| E Local names | `hasseCoeff`, `choose`, `Finsupp.prod` | Actual calls made; target and project API found, generic product family found, index unavailable. No absence conclusion is drawn from the unavailable index. [Target](../evidence/MvPolynomial.hasseCoeff/local.json), [choose](../evidence/MvPolynomial.hasseCoeff/local-choose.json), [prod](../evidence/MvPolynomial.hasseCoeff/local-prod.json). |

**Conclusion: found building blocks `Finsupp.prod` and `Nat.choose`; composition yields the full construction.** This is a positive composition finding, **not** a claim that exhaustive generic absence has been proved. The optional upper-function extension was searched too and is covered by the same product primitive. There is no unverified proposed modern form requiring another search.

Pinned declarations:

- `Finsupp.prod`: `Mathlib/Algebra/BigOperators/Finsupp/Basic.lean:48`; product over finite support. [Source excerpt](../evidence/MvPolynomial.hasseCoeff/mathlib-prod-excerpt.lean).
- `Nat.choose`: `Mathlib/Data/Nat/Choose/Basic.lean:50`; the usual total natural binomial coefficient. [Source excerpt](../evidence/MvPolynomial.hasseCoeff/mathlib-choose-excerpt.lean).
- `Finsupp.prod_fintype`: same product file, line 63, explains equivalence with the finite all-coordinate form; verified in `TargetProbes.lean`.
- `Finsupp.multinomial`: `Mathlib/Data/Nat/Choose/Multinomial.lean:202`; one multiindex, total factorial divided by product of coordinate factorials. This is a different operation. Neither its type nor its formula replaces the two-multiindex coefficient.
- `Polynomial.hasseDeriv`: `Mathlib/Algebra/Polynomial/HasseDeriv.lean:59`; univariate linear operator rather than this scalar. Do not substitute it without an actual multivariate construction.

The generic-route check is successful construction, not a negative `exact?` inference: the mathlib-only probe proves the eta-expanded expression agrees with the direct product both by `rfl` and `exact?`, without importing the project declaration. [MathlibComposition.lean](../evidence/MvPolynomial.hasseCoeff/MathlibComposition.lean), [raw log](../evidence/MvPolynomial.hasseCoeff/MathlibComposition.log), [receipt](../evidence/MvPolynomial.hasseCoeff/MathlibComposition.receipt.json): exit 0, 27.84 seconds. No `sorry` or extra axiom succeeds in place of a proof.

## Phase 5.5 — Statement shape

**Normal form.** Equivalent forms are (1) `d.prod (fun j ↦ (k j).choose)`, (2) `∏ j ∈ d.support, (k j).choose (d j)`, and (3), with `[Fintype σ]`, `∏ j, (k j).choose (d j)`. Mathlib's generic canonical support product is `Finsupp.prod`, as its defining source and `prod_fintype` show. The current body already uses it. The finite-variable bridge compiles, so no unverified equivalence is assumed. There is no proposition-level iff to orient; an equation exposing an alias should put this canonical product on the RHS.

**Syntactic generality attempted.** Explicit eta expansion `fun j n ↦ Nat.choose (k j) n`, the all-coordinate finite product, and arbitrary upper function `σ → ℕ` were actually compiled. For current derivative callers, two Finsupp arguments and lower-first order match differentiation order followed by the monomial exponent. Inline the exact eta-expanded product if removing the wrapper. An API named `Finsupp.choose k d` would be a naming/design proposal, not a verified existing replacement. It is not necessary for the composition.

| Argument / typeclass | Essentially needed? | Audit |
|---|---|---|
| `σ` | Yes | Gives the coordinate domain; already arbitrary and universe-polymorphic. |
| `d` | Yes | Supplies the chosen multiplicities and finite product support. |
| `k` | Yes as a function | Supplies upper binomial arguments; its Finsupp representation is convenient for monomials but not essential for computing the count. Optional extension verified above. |
| `[CommSemiring R]`, `R` | Not present | No dead section assumptions survive elaboration. |

**Normal form: OK. Syntactic generality: OK for the existing monomial API. Superfluous arguments: NONE to drop. Overall: SHIP-AS-STATED as a local helper.** This shape verdict concerns the valid local formulation; it does not override the standalone NO-composable inclusion verdict. The optional upper-support extension does not require changing current call sites.

## Phase 6 — Call sites and composition

**Internal use count, excluding the declaring file: 3 code-bearing lines, 2 distinct caller declarations, 2 files.** They contain 5 occurrences: CoeffNorm has one, the Taylor helper's statement has two, and its unfolding line has two. This avoids treating repeated unfolding as five independent consumers. Within `HasseDeriv.lean`: 21 code-bearing lines, 24 occurrences, 16 distinct callers. Whole project: 24 code-bearing lines / 29 occurrences. Docstrings, the defining declaration and identifiers merely containing the substring (e.g. `hasseCoeff_eq_zero_iff`) are excluded. No uses outside this repository were established.

Each code-bearing caller line is listed below; [call-sites.json](../evidence/MvPolynomial.hasseCoeff/call-sites.json) retains the caller declaration, exact excerpt and occurrence count. It was collected from actual source with nested comments stripped, not from the earlier structural parser's body boundaries.

| Caller file:line | Caller declaration | Actual code excerpt |
|---|---|---|
| `Roth/CoeffNorm.lean:139` | `abs_coeff_hasseDeriv_le` | `· have hc : (hasseCoeff d (e + d) : ℝ) ≤ 2 ^ (∑ j, r j) := by` |
| `Roth/HasseDeriv.lean:59` | `hasseDeriv` | `(monomial (k - d)).comp (LinearMap.lsmul R R (hasseCoeff d k : R))) ∘ₗ` |
| `Roth/HasseDeriv.lean:67` | `hasseDeriv_monomial` | `hasseDeriv d (monomial k a) = monomial (k - d) ((hasseCoeff d k : R) * a) := by` |
| `Roth/HasseDeriv.lean:74` | `hasseDeriv_apply` | `hasseDeriv d P = ∑ k ∈ P.support, monomial (k - d) ((hasseCoeff d k : R) * P.coeff k) := by` |
| `Roth/HasseDeriv.lean:80` | `hasseCoeff_eq_zero_iff` | `theorem hasseCoeff_eq_zero_iff (d k : σ →₀ ℕ) : hasseCoeff d k = 0 ↔ ¬d ≤ k := by` |
| `Roth/HasseDeriv.lean:81` | `hasseCoeff_eq_zero_iff` | `simp [hasseCoeff, Finsupp.prod, Finset.prod_eq_zero_iff, Nat.choose_eq_zero_iff, Finsupp.le_iff,` |
| `Roth/HasseDeriv.lean:90` | `coeff_hasseDeriv` | `(hasseDeriv d P).coeff e = (hasseCoeff d (e + d) : R) * P.coeff (e + d) := by` |
| `Roth/HasseDeriv.lean:106` | `hasseCoeff_eq_prod` | `theorem hasseCoeff_eq_prod [Fintype σ] (d k : σ →₀ ℕ) : hasseCoeff d k = ∏ j, (k j).choose (d j) :=` |
| `Roth/HasseDeriv.lean:114` | `hasseDeriv_zero_apply` | `simp [coeff_hasseDeriv, hasseCoeff]` |
| `Roth/HasseDeriv.lean:149` | `hasseDeriv_rename` | `simp [rename_monomial, hasseCoeff, Finsupp.prod_mapDomain_index_inj hf,` |
| `Roth/HasseDeriv.lean:154` | `hasseCoeff_mul_hasseCoeff` | `hasseCoeff d (f + d) * hasseCoeff e (f + d + e) =` |
| `Roth/HasseDeriv.lean:155` | `hasseCoeff_mul_hasseCoeff` | `hasseCoeff d (d + e) * hasseCoeff (d + e) (f + (d + e)) := by` |
| `Roth/HasseDeriv.lean:157` | `hasseCoeff_mul_hasseCoeff` | `simp only [hasseCoeff]` |
| `Roth/HasseDeriv.lean:176` | `hasseDeriv_hasseDeriv` | `hasseDeriv d (hasseDeriv e P) = (hasseCoeff d (d + e) : R) • hasseDeriv (d + e) P := by` |
| `Roth/HasseDeriv.lean:187` | `hasseDeriv_hasseDeriv_of_disjoint` | `rw [hasseDeriv_hasseDeriv, show hasseCoeff d (d + e) = 1 from` |
| `Roth/HasseDeriv.lean:192` | `hasseCoeff_mul_succ` | `hasseCoeff d (e + Finsupp.single j 1 + d) * (e j + 1) =` |
| `Roth/HasseDeriv.lean:193` | `hasseCoeff_mul_succ` | `(d j + 1) * hasseCoeff (d + Finsupp.single j 1) (e + Finsupp.single j 1 + d) := by` |
| `Roth/HasseDeriv.lean:194` | `hasseCoeff_mul_succ` | `simpa [hasseCoeff, add_comm, add_left_comm, add_assoc, mul_comm] using` |
| `Roth/HasseDeriv.lean:234` | `hasseDeriv_monomial_mul` | `show hasseCoeff d (a + b) = hasseCoeff d b from` |
| `Roth/HasseDeriv.lean:259` | `hasseDeriv_single_aeval_X` | `simp [-map_natCast, X_pow_eq_monomial, C_mul_monomial, hasseCoeff, Finsupp.single_tsub,` |
| `Roth/HasseDeriv.lean:271` | `uniqueAlgEquiv_hasseDeriv` | `simp [hasseCoeff, Finsupp.single_add]` |
| `Roth/HasseDeriv.lean:277` | `hasseCoeff_le_two_pow` | `hasseCoeff d k ≤ 2 ^ (∑ j, r j) := by` |
| `Roth/Taylor.lean:83` | `hasseCoeff_single_add_eq` | `hasseCoeff d (Finsupp.single i n + k') = n.choose (d i) * hasseCoeff (d.erase i) k' := by` |
| `Roth/Taylor.lean:85` | `hasseCoeff_single_add_eq` | `rw [hasseCoeff, ← Finsupp.mul_prod_erase' d i _ (by simp), hasseCoeff]` |

**Inline-derivation grep.** Whole-project code search `prod.*choose|choose.*prod` finds the definition and its finite-product bridge in `HasseDeriv.lean`; no second independent definition of the same support product was found. Other matches in that file are scalar identities used in proofs. The binomial determinant in `Wronskian.lean` and one-coordinate choice in Taylor are different objects, not bypassed reimplementations. [Grep receipt](../evidence/MvPolynomial.hasseCoeff/grep-receipts.json). The code indeed depends on this named helper; a dead-code claim would be false.

**Attempt 1 — direct existing operations (succeeds):**

```lean
fun (d k : σ →₀ ℕ) ↦ Finsupp.prod d (fun j n ↦ Nat.choose (k j) n)
```

Calls: `Finsupp.prod` and `Nat.choose`; input evaluation uses the existing Finsupp coercion. The comparison with the actual project definition compiles by `rfl`. Independently, the same construction compiles using only Mathlib imports; no project target is in its environment. This is a definition, so producing its value is the relevant composition test, rather than fabricating a Prop theorem of the same name.

**Attempt 2 — finite all-coordinate product (succeeds with extra `[Fintype σ]`):** `d.prod_fintype _ (fun _ ↦ Nat.choose_zero_right _)` bridges to `∏ j, ...`. This is useful for finite-variable estimates but is a worse replacement for an arbitrary variable type; it is not the recommended refactor.

**Conclusion: COMPOSABLE.** Attempt 1 works for every original input, with exactly two existing mathematical operations and no intervening reasoning, rewrite automation or new helper theorem. There is no failed search being disguised as proof of absence.

## Phase 7 — Verdict and actionable plan

**Category: NO-composable-from-mathlib.**

Evidence: Phase 3 identifies a standard multi-index binomial count; Phase 4 finds the project representation adequate for that standard and compiles an optional upper-function extension; Phase 4c finds no new mathematical abstraction, Phase 4.5 gives LOW infrastructure risk, Phase 4.6 accepts the construction strategy, Phase 5 positively identifies and checks both building blocks, Phase 5.5 finds no statement defect, and Phase 6 compiles the complete two-operation construction.

**Why not add this standalone definition.** Mathlib already supplies the finite-support product in arbitrary universes and the total natural binomial coefficient. The wrapper chooses the lower multiindex's support and partially applies `Nat.choose`; no additional structure, characteristic assumption, algebraic construction or theorem is needed. The standard name and the project's real consumers justify retaining it locally, but the full formula remains a direct composition. `Finsupp.multinomial` is not a replacement, and the absence of a returned exact name is not the basis of the verdict.

The semantic one-line exemption was explicitly considered. The surrounding Hasse API may eventually justify a named coefficient as part of a coherent upstream design; that is a package design decision for a later assessment of `hasseDeriv` and its substantive laws. This single-declaration verdict gives no verdict inheritance to those non-glue theorems, and does not require deleting a useful local alias before that package is designed. It recommends against a separate PR adding only `MvPolynomial.hasseCoeff`. No cost argument is used.

**Mathlib building blocks:** `Finsupp.prod` at `Mathlib/Algebra/BigOperators/Finsupp/Basic.lean:48`, `Nat.choose` at `Mathlib/Data/Nat/Choose/Basic.lean:50`.

**Composition sketch (one line):**

```lean
fun (d k : σ →₀ ℕ) ↦ d.prod (fun j n ↦ Nat.choose (k j) n)
```

**Belongs elsewhere:** the project-local `Roth/HasseDeriv.lean` is an appropriate destination for the semantic helper while the multivariate derivative API remains downstream. It is general combinatorial infrastructure, not an isolated historical theorem suited to `Archive/`.

**Mechanical future refactor plan, if removing the alias:**

1. At the external callers `Roth/CoeffNorm.lean:139` and `Roth/Taylor.lean:83`, replace every `hasseCoeff d k` by `d.prod (fun j n ↦ Nat.choose (k j) n)`, retaining surrounding casts and parentheses. At `Taylor.lean:85`, remove the two `hasseCoeff` unfolding entries from `rw`; `Finsupp.mul_prod_erase'` then addresses the product directly. These are the 3 external code lines / 2 caller declarations listed above.
2. Apply the same expression substitution to all 21 same-file code lines in the table, including theorem statements. Remove bare `hasseCoeff` entries from `simp only`, `simp` and `rw` lists because there is no alias left to unfold. Keep `Finsupp.prod` when explicitly expanding to `Finset.prod` is needed. Do not delete the scalar identities merely because the parent wrapper is composable; they require their own re-aimed assessments.
3. Remove only the definition at line 50 after all usages are updated, then compile the affected modules/project. The current assessment validates the defining substitution and generic typing, **not** an executed all-callers refactor. No such source edits are authorized by this read-only assessment and none were made.

**Next action:** retain this useful local helper during the read-only overview; mark it NO-composable as an independent mathlib addition. In a future authorized source cleanup, inline the displayed product at the 3 external lines and 21 same-file lines, remove obsolete unfolding entries, then remove the alias and rebuild. If proposing a multivariate Hasse derivative package upstream, discuss the coefficient name/location with the package reviewer rather than opening a standalone coefficient-definition PR.

## Phase 8 — Completion and evidence gate

All required per-declaration artifacts are present: doctor/type/axioms; mathematical prose; size and all one-line exemptions; all literature channels with explicit unavailability/inapplicability reasons; parameter-by-parameter generality; compiled optional extension; all nine modern-idiom questions including Q8 body diagnostic/Q9 semantic guard; all six risk rows with actual synthesis/defeq/coercion/universe probes; all five proof-strategy rows; actual calls for all five mathlib search methods; all three statement-shape audits; complete source caller table and inline re-derivation check; positive mathlib-only composition proof; actionable NO rationale and alternative destination.

Both compiler checks passed with standard axioms and no `sorry`. The baseline build was reused only after checking source/pin hashes. The local symbol index's unavailable status and the optional ChatGPT tool's absence are explicit limitations; neither is reported as an absence proof. The conclusion depends on a successful positive composition, not comprehensive negative search. Production Lean sources stayed unchanged. `assessment.json` records completion and per-phase gates. Independent review is a separate root-level acceptance gate and has not been falsely claimed here.
