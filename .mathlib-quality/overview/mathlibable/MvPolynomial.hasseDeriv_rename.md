# MvPolynomial.hasseDeriv_rename

Verdict: **YES-add-as-is**. This supplies the all-multiorder counterpart of pinned `MvPolynomial.pderiv_rename`: transporting variables injectively and transporting the derivative multi-index commute with Hasse differentiation. It supports embedding a polynomial into a larger separated-variable ring. The actual raw construction needs monomial evaluation, binomial-factor transport, truncated-subtraction transport and additive induction; no verified ≤3-call existing-mathlib replacement was found. This decision is fresh and does not inherit the parent's verdict.

## Phase 0 — baseline and scope

All 17 current source/pin hashes match the successful shared `lake build` baseline (exit0,2467 jobs). See [source-check.json](../evidence/MvPolynomial.hasseDeriv_rename/source-check.json), [baseline-build.txt](../evidence/MvPolynomial.hasseDeriv_rename/baseline-build.txt), and [worker-source-manifest.json](../evidence/MvPolynomial.hasseDeriv_rename/worker-source-manifest.json). The complete declaring module and the sole explicit caller declaration, including its context, were read. No production Lean, pin, Git, overview or progress file was changed. This is source-level explicit-reference coverage, not a kernel/simp dependency closure.

## Phase 1 — statement and mathematics

Public theorem at `Roth/HasseDeriv.lean:143`:

```lean
theorem hasseDeriv_rename {σ R : Type*} [CommSemiring R]
    {τ : Type*} {f : σ → τ} (hf : Function.Injective f) (d : σ →₀ ℕ)
    (P : MvPolynomial σ R) :
    hasseDeriv (d.mapDomain f) (rename f P) = rename f (hasseDeriv d P)
```

An injective relabeling of polynomial variables preserves each divided partial derivative if its finite multi-index is relabeled along the same map. The coefficient semiring is arbitrary and both variable types may be infinite. On a monomial `a X^k`, injectivity preserves the factor `∏j choose(k j,d j)` and identifies `(k-d).mapDomain f` with `k.mapDomain f-d.mapDomain f`. Both operators preserve addition, so monomial equality extends to all polynomials. These two injectivity-dependent normalizations are substantive premises; extensionality alone does not prove them.

The full elaborated type, independent universes and standard axioms are retained in the accepted native target receipt linked by [verification.json](../evidence/MvPolynomial.hasseDeriv_rename/verification.json). The forced replay uses `simp only` with an explicit monomial rule and pinned transport lemmas, so cannot close by accidentally using its own theorem. Project dependencies are the parent `hasseDeriv`, its monomial rule and `hasseCoeff`. Their previously assessed status does not make them existing pinned mathlib declarations.

## Phase 2 — preliminary checks

SMALL: compatibility API, with no new foundational structure and no role as a main Roth theorem. The one-line-definition test is N/A for a theorem. This is not a glue lemma or a qualified-name prefilter hit. Proof shortness alone supplies no verdict.

## Phase 3 — exhaustive literature

[web-requests.json](../evidence/MvPolynomial.hasseDeriv_rename/web-requests.json) retains exact requests, response representation hashes/bytes/status and original summaries; [web-sources.json](../evidence/MvPolynomial.hasseDeriv_rename/web-sources.json) retains titles, URLs and locators. Full result/article bodies are deliberately absent. Access failures and irrelevant search noise are recorded without turning them into absence evidence.

| Channel | Actual query/access | Finding |
|---|---|---|
| Specific web | multivariate Hasse derivatives injective variable renaming substitution | Primary [Joints of Varieties](https://link.springer.com/article/10.1007/s00039-022-00597-5), §4.3,equation(4.1), explains Taylor coefficient extraction and coordinate transforms in arbitrary characteristic. |
| General web | Hasse Schmidt derivation polynomial coordinate change divided partial derivatives | Narváez-Macarro's arbitrary-commutative-algebra, multivariate substitution-map framework. |
| Alias web | Hasse derivatives Taylor coefficients variable embedding characteristic arbitrary semiring | Binomial coefficient and Taylor formulations agree; finite-field algorithm literature also uses coefficient extraction. |
| Mathematical ChatGPT MCP | Standard form, generality and historical evolution | N/A: `ask_chatgpt_math` unavailable; other channels completed. |
| Local references | Actual rg on `clean.tex` for Hasse,Delta,rename,embedded | §1 monomial operator and §4 embedded-polynomial index argument motivate this compatibility. Excerpts retained. |
| nLab | Hasse Schmidt derivative several indeterminates | [Hasse-Schmidt derivative](https://ncatlab.org/nlab/show/Hasse-Schmidt%2Bderivative), indexed several-indeterminate definition over commutative rigs. Direct fetch failed400 XHTML. |
| nCatLab | Hasse Schmidt derivation functor; direct page | No exact categorical theorem identified; direct ncatlab page inaccessible. Nearby functor/derivation results do not establish the target law. |
| Stacks | Hasse Schmidt derivations polynomial; derivations polynomial | Broad derivation hits, then actual [05G3](https://stacks.math.columbia.edu/tag/05G3), §10.14 polynomial presentations. Context only, no exact rename law. |
| MathOverflow | Hasse Schmidt coordinate substitution; Hasse derivations | [440759](https://mathoverflow.net/questions/440759/what-is-the-relationship-between-higher-order-derivations-in-the-sense-of-hasse),2023, distinguishes HS operators, differential operators and jets; [71423](https://mathoverflow.net/questions/71423/replacement-for-derivations-in-characteristic-p) discusses positive characteristic. No exact replacement. |
| Recent arXiv | Hasse-Schmidt derivations2022–2026 substitution maps, then exact phrase2023/2025 | [2305.04537](https://arxiv.org/abs/2305.04537),2023 high-order derivation modules; [2509.00887](https://arxiv.org/abs/2509.00887),2025 lifting/deformations. Actual current abstracts accessed only. |

Standard concept: equivariance/naturality of coordinate Hasse derivatives under injective variable relabeling. Taylor coefficient extraction gives the rename identity algebraically; the exact arbitrary-type Lean statement is an inference from the formulas, not a verbatim theorem in every source. Classical finite-variable field descriptions, arbitrary commutative algebra HS families and semiring binomial formulas differ in ambient structure, while agreeing on this coordinate operator. Historical divided ordinary derivatives are useful in characteristic zero; arbitrary characteristic requires the binomial formulation. The older [1810.08075](https://arxiv.org/abs/1810.08075), abstract revised2020, explicitly studies multivariate HS substitution maps and characteristic-zero reconstruction; it is contextual history, not the recent-arXiv channel. Recent abstract work does not identify the canonical polynomial coordinate family with every HS family.

## Phase 4a–b — generality

| Parameter/axis | Audit and verified control |
|---|---|
| σ,τ | Independent arbitrary types; no Fintype, DecidableEq, inhabitedness, nonemptiness or finiteness hypotheses. |
| R | CommSemiring, already permits positive characteristic, zero divisors and trivial semirings; no inverses or cancellation. |
| Semiring weakening | Actual `#check_failure` probes test the fixed `hasseDeriv` and `rename` interfaces; both require CommSemiring. This is an interface constraint, not a claim that the combinatorial formula intrinsically requires commutativity. A different additive-monoid-algebra representation is separate parent-level work. |
| f | Arbitrary injective function, not a bijection or an equivalence; unused target variables are allowed. Embedding surface verified separately and equivalent. |
| hf | Cannot drop outright: fold Fin2 to Unit, take d=single0 1 and P=X1 over ℕ. Native witnesses give LHS=1,RHS=0. Distinct source variables collide and cannot retain the same individual derivative. |
| Support localization | `Set.InjOn f (↑P.vars ∪ ↑d.support)` is a mathematically plausible weaker condition. No proof of this exact new statement is accepted here; it is not a verified mechanical weakening and does not license generalise-first. Finsupp `mapDomain_injOn` is relevant lower-level evidence, not the missing Hasse theorem. |
| d,P | All finite multi-indices and polynomials, including zero order, zero polynomial and indices exceeding degree. |
| Hidden assumptions | Classical choice is local proof machinery, not an extra DecidableEq binder; all explicit parameters participate in the conclusion. |
| Arbitrary substitution | Rejected as a literal widening: general substitutions require a chain rule/sum over multi-indices. They cannot preserve this single transported-coordinate identity. |

Generality verdict: **MAXIMALLY GENERAL within the current canonical injective-rename interface**; no proposed weakening actually compiled. The precise local-injectivity variant remains a possible companion theorem, with no unsupported maximality claim over every imaginable representation. Fixed-interface Semiring failure, actual collisions and the distinction between coordinate relabeling and general substitution prevent false generalisations.

## Phase 4c — modern idiom, all nine diagnostics

| # | Diagnostic | Finding and downstream consequence |
|---|---|---|
| 1 | Typeclass preambles | Already arbitrary CommSemiring instances; injectivity is a function property, with an equivalent bundled embedding probe. |
| 2 | Filters/nets | N/A finite algebra, no topology. |
| 3 | Universal property | Linear maps from polynomials are determined by monomials; generic monomial naturality criterion is verified, with its entire intertwining premise explicit. It does not provide the Hasse binomial/truncation normalization. |
| 4 | Bundled substructures | No set-with-closure predicate; no subobject to replace. |
| 5 | Field→module/semiring | Already CommSemiring and R-linear maps. Noncommutative/additive coefficient representations change the fixed parent interface. |
| 6 | Higher categories | Naturality squares can be written, but no higher-category machinery or demonstrated downstream benefit justifies replacing the rewrite theorem. |
| 7 | Concrete index | ℕ exponents encode polynomial monomials and binomial extraction. An arbitrary monoid has no chosen binomial/truncated-subtraction operator. |
| 8 | Concrete-via-abstract | Fires at the additive-induction layer: identifiers disappear after specifying the action on monomials. The accepted generic `natural_monomial` takes arbitrary linear D/E and their monomial intertwining premise. It can reuse additive extension for other operators, but that premise retains the Hasse-specific substance. Existing mapDomain/prod/subtraction lemmas handle the actual monomial normalization. |
| 9 | False-generalisation guard | Generic D/E must retain their monomial compatibility premise; arbitrary linear operators are not automatically natural. General substitutions change meaning. Embedding and square variants preserve exactly the original content. |

Modern-idiom verdict: the generic monomial criterion is useful as a diagnostic; no verified material reorganisation requires replacing the coordinate compatibility API. In particular, abstracting an induction while assuming its entire monomial conclusion is not evidence that the Hasse law becomes an existing-call corollary. Optional square/embedding surfaces do not improve the actual caller's rewrite.

## Phase 4.5 — infrastructure risk

Theorem N/A for each of the six required risks: typeclass diamonds, reducibility leaks, noncanonical definitional unfolding, instance-priority collisions, universe-polymorphism construction risks, and coercion ambiguity. No definition/class/instance is introduced. Universes and coercions in the statement are checked by actual elaboration; rewrite orientation is handled below.

## Phase 4.6 — proof strategy, all five rows

| # | Diagnostic | Result |
|---|---|---|
| 1 | ε–δ versus filters | N/A algebraic identity. |
| 2 | Elements versus ideal/submodule inclusion | No inclusion or closure statement; monomial induction matches linear equality. |
| 3 | Sequences versus nets | N/A. |
| 4 | Construction versus universal property | No object construction. Equality of linear composites is verified but requires the same pointwise normalization. |
| 5 | Missing helper API | Generic monomial intertwining criterion verified; existing `prod_mapDomain_index_inj`, `mapDomain_apply_of_injective`, `mapDomain_tsub` supply lower-level transport. No missing generic transport lemma is needed for the current proof. |

Proof-strategy verdict: **MATHLIB-IDIOMATIC**. Additive monomial induction is appropriate and mirrors pinned first-order `pderiv_rename`. Coefficient transport is another approach but would have to handle target indices outside the image; no shorter verified existing replacement emerged.

## Phase 5 — five actual mathlib methods at three forms

| Method | Current form | Literature form | Abstract form |
|---|---|---|---|
| Finder | Multivariate Hasse derivatives injective rename | HS divided partial derivatives substitution/Taylor | Finsupp mapDomain weighted operators |
| Loogle | `MvPolynomial.rename, MvPolynomial.pderiv` | `Polynomial.hasseDeriv` | `Finsupp.mapDomain, HSub.hSub` |
| LeanSearch | Same natural-language current query | Same literature query | Same abstract query |
| Source rg | Qualified target and hasseDeriv_rename heads | HS/higher derivative/rename vocabulary | prod_mapDomain_index_inj, mapDomain_apply_of_injective, mapDomain_tsub, lsum/mapDomain |
| Local symbol search | hasseDeriv_rename | pderiv_rename | mapDomain_tsub |

Twelve exact formal-search receipts and eight exact rg receipts are retained. Local reports `index:unavailable`; fallback results include the project target and cannot prove mathlib absence. External indexes may differ from the pin. See [grep-receipts.json](../evidence/MvPolynomial.hasseDeriv_rename/grep-receipts.json) and the method-form JSON files listed by [copy-manifest.json](../evidence/MvPolynomial.hasseDeriv_rename/copy-manifest.json).

Pinned positives checked by native Lean: `MvPolynomial.pderiv_rename` at `Mathlib/Algebra/MvPolynomial/PDeriv.lean:143`; `MvPolynomial.rename_monomial` and `MvPolynomial.coeff_rename_mapDomain` at `Mathlib/Algebra/MvPolynomial/Rename.lean`; `Finsupp.prod_mapDomain_index_inj` and `Finsupp.mapDomain_apply_of_injective` at `Mathlib/Data/Finsupp/Basic.lean`; `Finsupp.mapDomain_tsub` at `Mathlib/Data/Finsupp/Order.lean:295`; `Finsupp.lsum_single` in the linear Finsupp API. First-order ordinary derivatives cannot recover arbitrary divided derivatives in positive characteristic by factorial division. The univariate Hasse API cannot directly transport arbitrary independent variables. The Finsupp lemmas preserve binomial factors and subtraction individually; none is the all-order polynomial compatibility theorem.

Mathlib-only probes use `#check_failure` for both the target and the parent in the stable three-import environment. These controls establish missing names in that actual environment, not a global absence theorem. No failed search or local-index failure is used as proof of absence. Prior expensive exact-search failures were not repeated without reason and no limits were raised.

## Phase 5.5 — statement shape, all three checks

1. Normal form: move `rename` out of the derivative, preserving a source-space derivative and using the transported multi-index on the larger ring. This matches Separation165. The linear composite square compiles but is less direct for `rw` inside a product.
2. Syntactic generality: the verified `σ ↪ τ` version bundles exactly the function/injectivity data; it adds no generality. Keeping `f` implicit and hf explicit matches pinned `pderiv_rename`. No mandatory restatement.
3. Superfluous binders: all parameters matter; no inherited Fintype/DecidableEq assumptions appear. Counterexamples and fixed-parent elaboration controls audit the nontrivial hypotheses.

Statement-shape verdict: current form is appropriate; equivalent square/embedding companions are optional.

## Phase 6.0 — explicit source callers and inline audit

The theorem is not `[simp]`. Internal use count:0. Explicit external invocation count:1, in one caller. Broader grep audited `hasseDeriv.*rename|rename.*hasseDeriv|prod_mapDomain_index_inj|mapDomain_tsub`; mentions of the longer caller name are not extra invocations of this theorem.

| Source caller | Actual use | Concrete hypothetical inline/refactor plan |
|---|---|---|
| `Roth.hasseDeriv_rename_mul_aeval`, `Roth/Separation.lean:146`, invocation165 | Final `rw` in a separated-variable factorisation; f=Option.some, hf=Option.some_injective, P=U, order=d. | Introduce a local equality proven by the same forced monomial induction with these parameters, and replace the last target rewrite by this equality. Product/univariate context stays as written. The accepted arbitrary outer `observe` experiment checks exactly the Option.some interface under an arbitrary observation. |

The caller uses derivative composition, degree-zero factors and the univariate bridge before this final renaming step. The broader theorem has uses at Separation365, but that is an indirect consumer, not another explicit target invocation. [caller-Separation-146.lean](../evidence/MvPolynomial.hasseDeriv_rename/caller-Separation-146.lean) retains the full caller. No deletion or production caller refactor is proposed for this YES assessment. Scoped interface probes do not claim a full replay of the caller body; the shared hash-matched build verifies the unchanged full module.

## Phase 6 — actual composition experiments

1. **Pinned first-order analogue:** `MvPolynomial.pderiv_rename` verifies the right pattern but has only one ordinary derivative. No typed ≤3-call transport to all finite multiorders is available; factorial inversion is invalid in positive characteristic.
2. **Forced original replay:** induction on P, then explicit monomial rewriting and three injectivity-dependent Finsupp transports. Project monomial rules contain operator-specific content and are not existing pinned building blocks.
3. **Abstract monomial criterion:** arbitrary linear maps D/E commute with rename provided their monomial actions intertwine. This is newly proved by induction, and its hypothesis is precisely the normalisation needed in the concrete Hasse case. It does not magically prove that premise.
4. **Raw definition, mathlib only:** copy the exact `Finsupp.lsum`/`coeffLinearEquiv` operator with its binomial factor; prove its monomial action by the typed existing `Finsupp.lsum_single` term; prove rename naturality by additive monomial induction, transporting factor and exponent separately. No Roth import, project coefficient formula or imported target appears. This is substantive proof rather than a closing `simp [defs...]` composition.

Conclusion: **NOT-COMPOSABLE from verified existing pinned mathlib calls**. Neither an existing ≤3-call term nor a raw closing-simp replacement was verified. Phase6b's trivial-simp BORDERLINE criterion therefore does not apply merely because the monomial branch has a closing simplification. Additive induction plus its binomial and truncated-subtraction normalisations are the proof content. This is evidence from actual concrete construction, not a verdict forced by project helper naming.

## Phase 7 — decision and actionable upstream plan

**YES-add-as-is.** Concrete missing API: all-multiorder injective-variable-renaming compatibility for the polynomial Hasse family, extending pinned `pderiv_rename` without factorial inverses. It makes Hasse derivatives usable after inclusion into larger polynomial rings and combines with the existing rename, monomial, degree, evaluation and separated-variable APIs. Its sole explicit local caller demonstrates embedding into Option variables, while the statement serves arbitrary injections independently of Roth's theorem.

The actual raw construction requires the expected substantive proof: evaluate monomials, preserve binomial factors, preserve natural truncated subtraction, then extend additively. Abstracting the linear extension retains the monomial premise. The current coordinate form agrees with literature Taylor extraction and the pinned partial-derivative rename interface. No verified mechanical weakening or material modern-idiom replacement requires generalise-first, and no existing-call deletion term was obtained. Single local use does not turn a standard missing all-order algebra API into project-specific bookkeeping.

**Proposed upstream file:** `Mathlib/Algebra/MvPolynomial/HasseDeriv.lean`.

**Proposed PR title:** `feat(Algebra/MvPolynomial/HasseDeriv): add injective renaming compatibility`.

**Grouping:** include with the already accepted YES parent `MvPolynomial.hasseDeriv`, coefficient API `MvPolynomial.coeff_hasseDeriv`, and coefficient-change companion `MvPolynomial.hasseDeriv_map`. The parent and its monomial law must be upstream before submitting this independently. Do not infer verdicts for unassessed neighbours or automatically upstream a separately assessed scalar alias.

**Pre-PR checklist:**

1. Run `/generalise MvPolynomial.hasseDeriv_rename`; retain arbitrary variable types and CommSemiring. If pursuing support-local injectivity, prove the actual new statement and recheck the semantic guard before claiming a weakening.
2. Run `/cleanup Roth/HasseDeriv.lean MvPolynomial.hasseDeriv_rename`; preserve the substantive monomial transport and exclude circular simplification.
3. Recheck then-current mathlib for new Hasse API, align rename orientation/attributes with `pderiv_rename`, and consider optional linear-square/embedding companions only when consumers need them.
4. Reviewer candidates from actual pinned file history: Yaël Dillies (`631b214f7c`, MvPolynomial coefficient refactor,#41427) or Moritz Firsching (`334438dace`, Hasse coefficient-change API,#42428). [reviewer-commits.json](../evidence/MvPolynomial.hasseDeriv_rename/reviewer-commits.json) is the retained actual read-only history receipt shared with the immediately preceding assessment on the identical mathlib pin. These are evidence-based candidates, not claims of reviewer agreement or invented future history.

Alternative destination while preparing the coherent upstream module: retain `Roth/HasseDeriv.lean`. The result is ordinary general algebra appropriate for mathlib rather than Archive. Next action: root independently reviews and publishes this completed assessment, then continues immediately in overview order. No user permission question is needed for this read-only work.

## Phase 8 — evidence package

[assessment.json](../evidence/MvPolynomial.hasseDeriv_rename/assessment.json), [verification.json](../evidence/MvPolynomial.hasseDeriv_rename/verification.json), [copy-manifest.json](../evidence/MvPolynomial.hasseDeriv_rename/copy-manifest.json), and [validate.py](../evidence/MvPolynomial.hasseDeriv_rename/validate.py) describe the handoff. Native accepted sources and complete raw receipts are separate from rejected attempts. No axioms beyond propext,Classical.choice,Quot.sound, no sorry/admit/unsafe/native_decide and no raised limits are accepted. The read-only validator supports scratch and integrated layouts, validates current copy-manifest hashes/bytes rather than historical worker copies, and checks links, exact sources, receipt completion and baseline/source hashes. Root acceptance remains pending independent review.
