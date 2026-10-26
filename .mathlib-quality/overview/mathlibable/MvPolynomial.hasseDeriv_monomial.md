# Full /mathlibable assessment — `MvPolynomial.hasseDeriv_monomial`

**Category: NO-composable-from-mathlib. All assessment gates complete; independent root acceptance pending.** Scope is exactly the public simp theorem at `Roth/HasseDeriv.lean:66`, assessed independently. The parent definition's completed YES verdict is context, not an inherited verdict: `by simp [hasseDeriv]` is outside the command's narrow glue-inheritance forms.

Date: 2026-10-26. Branch: `ramin-cleanup`. Mathlib pin: `5ed2965256430c3649e86755f9576b54eca72435`; Lean v4.34.0. Production source/pin manifest starts at `99f19fda4b3cbee38fc0d31af76075834f5cc265`. No production source/Git mutation by this worker. Links below use the intended tracked report/evidence layout.

## Phase 0 — Doctor

The shared `lake build` passed, exit 0, 2467 jobs. Reuse is valid after independently verifying **17/17** current source/pin SHA-256 hashes. [Baseline](../evidence/MvPolynomial.hasseDeriv_monomial/evidence/baseline-build.txt), [input manifest](../evidence/MvPolynomial.hasseDeriv_monomial/evidence/input-manifest.json), [hash verification](../evidence/MvPolynomial.hasseDeriv_monomial/evidence/baseline-hash-verification.json), [portable reproduction script](../evidence/MvPolynomial.hasseDeriv_monomial/evidence/audit-sources.py).

Unique target: public theorem, `@[simp]`, `Roth/HasseDeriv.lean:66–68`. [Actual declaration](../evidence/MvPolynomial.hasseDeriv_monomial/evidence/target-source.lean), [declaration/context inventory](../evidence/MvPolynomial.hasseDeriv_monomial/evidence/target.json), [full source context including attribute](../evidence/MvPolynomial.hasseDeriv_monomial/evidence/source-context.txt). The module constructs multivariate Hasse derivatives and their coefficient, composition and compatibility API. Target has no `sorry`; scratch probes introduce no axioms, unsafe/native trust, limit raises or production edits. The [target native receipt](../evidence/MvPolynomial.hasseDeriv_monomial/evidence/target-lsp.json) reports `partial=false`, `success=true`, no errors or failed dependencies; the exact [executed source](../evidence/MvPolynomial.hasseDeriv_monomial/probes/TargetChecks.lean) preserves the request context. `#print axioms` returned exactly `propext`, `Classical.choice`, `Quot.sound`. The independent `simp [hasseDeriv]` proof ran with the imported target's simp attribute disabled, preventing circular verification. The nsmul RHS alternative also passed. The Semiring-only operator check produced the expected explicit missing `CommSemiring S` message under `#check_failure`; that diagnostic is info, not an admitted proof or failed compile. An inherited scratch module-docstring warning is retained; no linter suppression was applied. The separate source-hover request was canceled while loading; it is not claimed as a successful check. Actual elaborated theorem type from native `#check`:

```lean
@MvPolynomial.hasseDeriv_monomial :
  ∀ {σ : Type u_1} {R : Type u_2} [CommSemiring R] (d k : σ →₀ ℕ) (a : R),
    hasseDeriv d (monomial k a) = monomial (k - d) (↑(hasseCoeff d k) * a)
```

The two universes are independent. The final target exact-term composition receipt is checked below.

## Phase 1 — Mathematical statement

For arbitrary variables σ, a commutative coefficient semiring R, and finitely supported natural multiindices d and k, the Hasse derivative of the monomial aXᵏ is the monomial with exponent k−d and coefficient a multiplied by the coordinatewise binomial product ∏ⱼ binom(kⱼ,dⱼ). Natural subtraction is truncated; when some dⱼ exceeds kⱼ the product is zero, so no incorrect surviving monomial results. The formula includes the zero coefficient, zero derivative order, empty variable type and positive characteristic.

| Parameter/hypothesis | Role |
|---|---|
| `{σ : Type u}` | Arbitrary variables, no finiteness or decidable equality assumed |
| `{R : Type v}` | Arbitrary coefficient carrier, independent universe |
| `[CommSemiring R]` | Existing `MvPolynomial` and its R-linear maps, coefficient multiplication and natural casts |
| `d : σ →₀ ℕ` | Differentiation multiplicities |
| `k : σ →₀ ℕ` | Monomial exponents |
| `a : R` | Arbitrary coefficient, including zero |

Conclusion in Lean:

```lean
hasseDeriv d (monomial k a) = monomial (k - d) ((hasseCoeff d k : R) * a)
```

## Phase 2 — Preliminary checks

**SMALL:** the evaluation law of the previously defined operator, not itself a new structure or one of the module's separately highlighted main theorems. The Hasse name does not make each computational helper a distinct named theorem from literature. Literature width remains exhaustive.

**One-line check: n/a — theorem.** The actual command explicitly exempts theorem/lemma kinds from the definition-only check. Its proof has one substantive tactic line. Supplementary exemption audit: no new instance diamond; no sealed definition introduced here; there is concrete semantic/API value in the `@[simp]` law and its four actual callers. That value will be weighed explicitly against the generic evaluation composition, rather than mistaking brevity for dead code.

## Phase 3 — Exhaustive literature protocol

Exact requests, returned titles/URLs, failed fetch status and batch boundaries are retained in [literature requests](../evidence/MvPolynomial.hasseDeriv_monomial/evidence/literature-requests.json) and [follow-ups](../evidence/MvPolynomial.hasseDeriv_monomial/evidence/literature-followups.json). These contain no copied webpage text. Batch results do not prove that each individual query had a hit.

| Channel | Actual query/read | Outcome and original analysis |
|---|---|---|
| Web, specific | `multivariate Hasse derivative monomial formula binomial coefficients` | Batch returned primary polynomial formula, directly relevant to the target |
| Web, general | `Hasse Schmidt derivation commutative semiring polynomial monomials` | Batch returned commutative-ring primary sources and rig context; abstract higher derivations are broader families, not a replacement for this coordinate law |
| Web, aliases | `hyperderivative divided derivative multi index Taylor coefficient polynomial` | Batch returned Taylor coefficient formulation; no factorial division needed |
| ChatGPT MCP | Capability discovery for `ask_chatgpt_math` | n/a: absent; no consultation claimed. [Availability receipt](../evidence/MvPolynomial.hasseDeriv_monomial/evidence/tool-availability.json) |
| Local references | [`clean.tex:119–155` excerpt](../evidence/MvPolynomial.hasseDeriv_monomial/evidence/local-reference-excerpt.tex); `rg Hasse\|Delta\|semiring` | Explicit monomial definition with zero case and semiring scope, matching the target |
| nLab | `site:ncatlab.org/nlab Hasse Schmidt derivative` | Indexed rig-valued several-variable monomial definition inspected |
| nCatLab | `site:ncatlab.org/ncatlab Hasse Schmidt derivation` | Related categorical context returned; no equivalent categorical theorem replacing this coordinate evaluation |
| Stacks | `site:stacks.math.columbia.edu Hasse Schmidt differential operators` | Batch mixed results; no individual absence inference |
| MathOverflow | `site:mathoverflow.net Hasse derivative monomial` | Batch contextual results; no theorem used as mathematical authority |
| Recent arXiv | `site:arxiv.org Hasse derivatives multivariate 2024 2025 2026` | Broad noisy batch; unrelated results rejected |
| Recent arXiv | `site:arxiv.org/abs/2205.00342 Hasse derivative` | Direct 2022 primary paper independently opened below |
| Recent arXiv | `site:arxiv.org "Hasse derivatives" "2023"` | Batched follow-up; no individual positive claim |
| Stacks | `site:stacks.math.columbia.edu "Hasse" "Schmidt"` | Batched follow-up, related divided-power context inspected directly |
| nCatLab | `site:ncatlab.org/ncatlab "Hasse-Schmidt"` | Indexed derivative and graded-bimonoid context inspected |
| Recent arXiv isolated | `site:arxiv.org "Hasse derivative" "2023"` | Empty for this exact query, not an absence conclusion |
| nLab direct | Hasse–Schmidt derivative page | Direct fetch failed: unsupported XHTML; indexed content available; limitation preserved |
| Stacks direct | [23.2, tag 07GK](https://stacks.math.columbia.edu/tag/07GK) | Divided powers on an ideal, a different object from the polynomial endomorphism. Supplies context, no direct restatement |
| MO direct | [Question 510672](https://mathoverflow.net/questions/510672/hasse-derivative-and-laurent-denis-lemma) | Positive-characteristic application discussion, not a proof of the target or its generality |
| Recent arXiv direct | [2205.00342](https://arxiv.org/abs/2205.00342), then actual HTML link | Submitted 2022-04-30, inside the five-year interval 2021-10-26–2026-10-26. [Primary full text](https://arxiv.org/html/2205.00342v1), §3.2 Definition 3.4 and Proposition 3.5 read |

**Literature summary.** The concept is the multivariate Hasse/hyperderivative monomial law. Bhargava–Ghosh–Guo–Kumar–Umans, §3.2, defines the derivative by the Taylor coefficient of f(x+z) over a commutative ring and gives the binomial monomial expansion. The local source explicitly permits commutative semirings; the source algebra uses only additions, multiplications and natural coefficients. Our arbitrary finitely supported variable representation also covers finite-variable presentations. The semiring generality does not rely solely on secondary nLab material.

Sources agree on the coordinate formula. They vary in coefficient structure (field, ring, rig), finite versus arbitrary variable presentation, and whether the entire higher-derivation family is bundled. No source requires inverses of factorials for this law. General Hasse–Schmidt derivations on arbitrary algebras are different data and need not act on coordinates by this fixed formula; replacing the target by that abstraction would change its mathematical content.

## Phase 4a–b — Generality

| Parameter/hypothesis | Current versus standard | Verified weaker opportunity? | Reason |
|---|---|---|---|
| σ | Arbitrary, literature commonly finite variables | No | Already handles infinite/empty variable sets |
| R | Arbitrary, literature field/ring/rig | No | No characteristic, domain or inverse assumptions |
| `[CommSemiring R]` | Semiring form of coordinate polynomial algebra | No | Existing target and `MvPolynomial σ R` require it; Semiring-only floor probe fails explicitly: missing CommSemiring S |
| d | Any finite-support natural order | No | Arbitrary size, no positivity/degree condition |
| k | Any finite-support natural exponents | No | No d≤k assumption; binomial zero handles vanishing |
| a | Any coefficient | No | No nonzero condition |

**MAXIMALLY GENERAL for this existing polynomial/operator representation.** No verified weakening opportunities. Extending to noncommutative coefficients would require a different foundational object/API, not dropping an unused theorem hypothesis. Natural exponents encode polynomial monomials; Laurent/Hahn exponents are different domains.

## Phase 4c — Modern mathlib idiom, all nine questions

| # | Question | Answer / proposed reformulation | Concrete downstream consequence |
|---|---|---|---|
| 1 | Preambles to typeclasses? | No: CommSemiring already a typeclass | Existing polynomial/module API already usable |
| 2 | Sequences to filters? | No: finite algebraic equality | No topology involved |
| 3 | Construction to universal property? | No new construction in this theorem; its proof uses the universal linear extension | Existing `Finsupp.lsum_single` supplies abstract evaluation |
| 4 | Sets to bundled substructures? | No sets with closure predicates | Operator already bundled as LinearMap |
| 5 | Field/vector assumptions to modules/semirings? | Already CommSemiring; no field assumptions | Positive characteristic, ℕ, trivial semiring already covered |
| 6 | Higher category formulation? | No coordinate-preserving improvement found after categorical brief search | Graded bimonoids relate to the family, not a mechanical rewrite of this monomial law |
| 7 | Natural index to arbitrary monoid? | Rejected as a replacement: binomial coefficients and natural polynomial exponents are essential | Laurent variants would require different exponent/choose API |
| 8 | Concrete via abstract proof diagnostic? | **Yes diagnostic fires:** proof body is exactly `simp [hasseDeriv]`; one occurrence of the named operator, zero after unfolding. Abstract evaluation is `Finsupp.lsum_single R b k a` | Already-existing abstract theorem evaluates any family of component linear maps; no new abstract helper is needed |
| 9 | False generalisation guard? | General arbitrary b is a sound abstract evaluation theorem, already in mathlib; it must retain its b parameter. Calling arbitrary b a Hasse derivative would change meaning and is rejected | Keeps the Hasse semantic law distinct from the generic representation calculation |

**Modern-idiom verdict:** existing abstract idiom identified, not a novel modernisation proposal. The explicit Q8 test directs Phase 6 toward the existing linear-extension API. No unsupported YES-but-generalise-first claim follows from replacing the name by an arbitrary map.

## Phase 4.5 — Diamond/defeq risk

**n/a — declaration kind is theorem.** It adds a proposition proof and a simp rule, not data, a new reducibility path, class or instance. The command explicitly skips the six infrastructure-risk rows for this kind. Simp orientation is assessed in Phase 5.5.

## Phase 4.6 — Proof strategy

| # | Idiom question | Applies? / alternative | Cost |
|---|---|---|---|
| 1 | ε–δ to filters | No topology | n/a |
| 2 | Element algebra to bundled inclusions | No inclusion argument; this is generator evaluation | n/a |
| 3 | Sequences to nets | No analysis | n/a |
| 4 | Explicit construction to universal property | Proof already evaluates a universal linear extension | No strategy change |
| 5 | Missing helpers mathlib should have | No: `Finsupp.lsum_single` is the existing generic helper | No helper PR |

**MATHLIB-IDIOMATIC.** A single `simp [hasseDeriv]` is a reasonable local proof. Directly naming `Finsupp.lsum_single` may expose the underlying dependency more clearly, but it does not create new mathematics.

## Phase 5 — All five mathlib search methods

[Exact requests/raw tool outputs](../evidence/MvPolynomial.hasseDeriv_monomial/evidence/search-methods.json), [untruncated source searches](../evidence/MvPolynomial.hasseDeriv_monomial/evidence/grep-receipts.json), [whole-mathlib qualified/bare-name searches](../evidence/MvPolynomial.hasseDeriv_monomial/evidence/full-name-grep.json), [reproduction searches](../evidence/MvPolynomial.hasseDeriv_monomial/evidence/reproduction-grep-receipts.json), [pinned candidate source hashes](../evidence/MvPolynomial.hasseDeriv_monomial/evidence/candidate-source-hashes.json).

| Method | Actual query | Outcome |
|---|---|---|
| A Lean-Finder | Multivariate Hasse derivative of a monomial equals product of binomial coefficients times monomial with exponents subtracted | Polynomial analogue; pderiv, derivation and Laurent partial matches |
| B Loogle | `"hasseDeriv", "monomial"` | `Polynomial.hasseDeriv_monomial` |
| C LeanSearch | Hasse derivative multivariate polynomial monomial binomial coefficient | Same univariate analogue, first partial derivative and broader context |
| D Source grep | `hasseDeriv_monomial\|Hasse\|hasseDeriv\|hyperderiv` in mathlib MvPolynomial; candidate-specific grep | No text hit for the target in MvPolynomial subtree; positive generic and univariate candidates recorded |
| E Name pattern | `hasseDeriv_monomial` | Production target, copied evidence excerpt, univariate analogue, private downstream multiplication helper. Local symbol index reports **unavailable**; textual fallback is not an exhaustive symbol index |
| A abstract repeat | Finitely supported sum linear map applied to single supported coefficient evaluates its indexed component | `Finsupp.lsum_single`, `lsum_comp_lsingle`, related DFinsupp/linearCombination API |
| B abstract repeat | `Finsupp.lsum _ _ (Finsupp.single _ _) = _` | Empty for this type query |
| C abstract repeat | linear extension of a family of linear maps on finitely supported functions evaluated at a single | `Finsupp.lsum_comp_lsingle`, `Finsupp.lhom_ext`, DFinsupp context |
| E abstract repeat | `lsum_single` | Actual source candidate paths returned; index still unavailable |

Both user/literature coordinate formula and the Phase 4c abstract linear-extension form were searched. The literature form agrees with the user form at this representation.

| Candidate | Pinned source | Applicability |
|---|---|---|
| `Polynomial.hasseDeriv_monomial` | `Mathlib/Algebra/Polynomial/HasseDeriv.lean:104` | Exactly the univariate law for k,n:ℕ; no direct specialization yields arbitrary σ and d. Not the target under another namespace |
| `MvPolynomial.pderiv_monomial` | `Mathlib/Algebra/MvPolynomial/PDeriv.lean:69` | Order-one single-coordinate derivative, not arbitrary multidegree; factorial inversion invalid in general |
| `MvPolynomial.mkDerivation_monomial` | `Mathlib/Algebra/MvPolynomial/Derivation.lean:130` | Ordinary Leibniz derivation; higher Hasse components are not individually ordinary derivations |
| `Finsupp.lsum_single` | `Mathlib/LinearAlgebra/Finsupp/LSum.lean:123` | Generic linear extension evaluated at single: exactly the abstract content after project definition transport |
| `AddMonoidAlgebra.coeffLinearEquiv` | `Mathlib/Algebra/MonoidAlgebra/Module.lean:75` | Transports monomial storage to Finsupp coefficients |
| `MvPolynomial.monomial` | `Mathlib/Algebra/MvPolynomial/Basic.lean:93` | Defined through `AddMonoidAlgebra.lsingle`; source explains transport |

**Search conclusion:** positive generic building blocks and partial analogues found. No universal absence claim is made from empty search/index results. The successful mathlib-only probe distinguishes absence of the exact qualified name from the existence of the general mathematical route.

## Phase 5.5 — Statement shape

Equivalent forms considered: (1) current monomial with coefficient `(hasseCoeff d k : R) * a`; (2) natural scalar coefficient `hasseCoeff d k • a`; (3) piecewise zero when d≰k; (4) a scalar multiple of the monomial with coefficient a. The existing univariate `Polynomial.hasseDeriv_monomial` uses the same cast-times-coefficient RHS as (1). This is the appropriate proposed simp normal form: remove the derivative from a generator on the LHS, preserve monomial structure on the RHS. No quadratic family of orthogonal equivalences is needed.

**Syntactic generality attempted:** nsmul alternative successfully compiled in the target native batch. The current explicit d,k,a form supports direct `rw`, matches the existing univariate interface and handles zero coefficients without preconditions. The piecewise form adds case-splitting obligations; it is worse for these actual callers. Keep current form if retaining this local API.

| Argument/typeclass | Essentially used? | Reason |
|---|---|---|
| σ | Yes | Domain of exponents and monomials |
| R | Yes | Coefficients and scalar structure |
| CommSemiring | Yes for current statement | Existing MvPolynomial/operator type needs it; floor probe explicitly reports missing CommSemiring S |
| d | Yes | Operator order, coefficient choice and exponent shift |
| k | Yes | Input monomial exponent and output coefficient/exponent |
| a | Yes | Arbitrary coefficient on both sides |

Normal form **OK**; syntactic generality **OK**; superfluous arguments **NONE**; overall **SHIP-AS-STATED** as a local semantic interface. This statement-shape finding does not itself settle the independent upstream verdict.

## Phase 6.0 — Actual call sites

[Every written caller line with qualification and occurrence counts](../evidence/MvPolynomial.hasseDeriv_monomial/evidence/call-sites.json). Production Lean modules only; nested comments/docstrings, declaration head, substring names, copied evidence and scratch excluded. All five lines resolve to MvPolynomial in the enclosing namespace; none is the qualified Polynomial analogue.

**Internal use count outside the declaring file: 3 explicit occurrences / 2 code lines / 1 distinct caller declaration / 1 file.** Same file: 4 occurrences / 3 lines / 3 caller declarations. Whole project: **7 occurrences / 5 lines / 4 callers**. No downstream-library use established. These are written references, not opaque elaborator/simp dependency closure counts.

| Source | Qualified caller | Exact source line |
|---|---|---|
| `Roth/HasseDeriv.lean:94` | `MvPolynomial.coeff_hasseDeriv` | `rw [hasseDeriv_monomial, coeff_monomial, coeff_monomial]` |
| `Roth/HasseDeriv.lean:127` | `MvPolynomial.hasseDeriv_C` | `rw [C_apply, hasseDeriv_monomial, (hasseCoeff_eq_zero_iff d 0).2 (by simpa using hd)]` |
| `Roth/HasseDeriv.lean:233` | `MvPolynomial.hasseDeriv_monomial_mul` (private) | `rw [monomial_mul_monomial, hasseDeriv_monomial, hasseDeriv_monomial,` |
| `Roth/Taylor.lean:111` | `MvPolynomial.coeff_taylor_monomial_single_add_aux` (private) | `rw [mem_support_iff, ih e, hasseDeriv_monomial] at he` |
| `Roth/Taylor.lean:116` | Same private caller | `← monomial_single_add, hasseDeriv_monomial, hasseDeriv_monomial, eval_monomial,` |

Inline-derivation grep: `simp.*hasseDeriv|lsum_single|prod.*choose|choose.*prod` throughout Roth. The target is the explicit monomial evaluation interface; `hasseDeriv_apply` unfolds the operator to a full support sum, a different statement, and other product matches are scalar combinatorics. No second independent inline proof of exactly the monomial law found by this written-source search. It is useful API, not junk.

## Phase 6 — Composition attempts

1. Existing `Polynomial.hasseDeriv_monomial` cannot directly instantiate arbitrary multiindices. `MvPolynomial.pderiv_monomial` covers a single first-order coordinate only. Repeated partial differentiation plus factorial inversion does not work over arbitrary semirings/positive characteristic. These routes are partial, not compositions for the target.
2. Abstract linear-extension route: `Finsupp.lsum_single R b k a` evaluates b's extension at the single coefficient. Monomial/coeff transport is supplied by existing MvPolynomial/AddMonoidAlgebra storage. Actual project instance b is `(fun k => (monomial (k-d)).comp (LinearMap.lsmul R R (hasseCoeff d k : R)))`. No binomial identity is proved: the entire binomial factor is passed untouched to the component map.

[Mathlib-only exact source](../evidence/MvPolynomial.hasseDeriv_monomial/probes/MathlibOnly.lean) checks generic evaluation and repeats the target formula for an explicitly **new local witness**. It does not pass that new witness off as an existing mathlib operator. The [actual combined mathlib-only executed source](../evidence/MvPolynomial.hasseDeriv_monomial/probes/MathlibOnlyExecuted.lean) and [raw native receipt](../evidence/MvPolynomial.hasseDeriv_monomial/evidence/mathlib-only-lsp.json) report `partial=false`, `success=true`, zero errors and zero failed dependencies. The final appended local-witness proof is **only a direct `Finsupp.lsum_single` term**, without tactics; it passed. The two earlier `simpa` examples produced unnecessarySimpa warnings, retained honestly. The combined document's earlier sanity/example and previous definition probes are preserved with the exact source; their success does not expand the scope of this target verdict. The unknown target-name diagnostic is an expected info message from `#check_failure`, not a universal mathematical absence claim.

The initial batching attempt duplicated the global universe command, causing a scratch elaboration error; root removed that duplicate declaration and reran to the successful result. [Initial exact source](../evidence/MvPolynomial.hasseDeriv_monomial/probes/MathlibOnlyInitial.lean), [initial raw receipt](../evidence/MvPolynomial.hasseDeriv_monomial/evidence/mathlib-only-initial-lsp.json). No production edit or mathematical weakening was involved. Target-environment independent checks have imported target simp disabled. The [final exact target source](../evidence/MvPolynomial.hasseDeriv_monomial/probes/ExactTargetChecks.lean) and [raw native receipt](../evidence/MvPolynomial.hasseDeriv_monomial/evidence/exact-target-lsp.json) confirm the original target itself is closed by **the direct theorem term below**, with no `change`, `simp`, `using`, or intervening proof. Imported target simp remains disabled. Final native result: `partial=false`, `success=true`, `timed_out=false`, zero errors and failed dependencies. Two warnings in the combined document belong to the preserved earlier scratch header/`simpa` experiment; the final direct term adds no warning. The final warm response took 499 ms; that is not a claim about initial import/load time.

```lean
example (d k : σ →₀ ℕ) (a : R) :
    hasseDeriv d (monomial k a) = monomial (k - d) ((hasseCoeff d k : R) * a) :=
  Finsupp.lsum_single R (fun k : σ →₀ ℕ =>
    (monomial (k - d)).comp (LinearMap.lsmul R R (hasseCoeff d k : R))) k a
```

**Conclusion: COMPOSABLE.** Exactly one existing mathematical evaluation theorem is applied to the component maps from the defining recipe; storage transport and component-map application reduce definitionally. This is stronger than the command's ambiguous “trivial simp composition” case: there is an accepted direct proof term with no tactic reasoning. The positive route, rather than a search absence claim, supports the verdict.

## Phase 7 — Verdict and actionable plan

**Category: NO-composable-from-mathlib.** This is an independent full assessment, not parent inheritance.

Evidence: Phase 3 confirms the characteristic-free standard monomial law; Phase 4 finds no verified narrowing and identifies the already-existing abstract theorem; Phase 4.5 is legitimately n/a for a theorem; Phase 4.6 accepts the strategy; all five Phase 5 methods were actually attempted; Phase 5.5 accepts the statement shape; Phase 6 positively verifies the direct generic evaluation term in both isolated mathlib-only and target environments.

**Why not a standalone addition.** `Finsupp.lsum_single` already evaluates arbitrary linear extensions on single coefficients. The target's component map is explicitly the shifted monomial map composed with coefficient multiplication; it consumes the binomial coefficient as uninterpreted input, requiring no new binomial, derivative, or coefficient theorem. The exact accepted term above supplies the whole original statement using the generic API with definitional transport. The univariate and first-partial-derivative candidates are not the replacements; claiming that they already supply arbitrary multiindex Hasse derivatives would be false. The NO-composable bucket records this construction/evaluation route, without asserting that mathlib already contains the coordinate operator under another name.

**Local/package API qualification.** The theorem is useful: it has four actual caller declarations and gives a stable `@[simp]` normal form independent of coefficient-storage implementation. The command's definition-only one-line warning is n/a here, and these real consumers rule out calling it junk. Nevertheless, useful semantic naming alone does not defeat the verified one-call composition for the single-declaration standalone-addition decision. Retaining the name in this project is sensible during this read-only overview. If a future upstream multivariate Hasse derivative package is designed around the already-assessed `MvPolynomial.hasseDeriv` YES definition, its reviewer may deliberately retain this canonical generator simp law as package API, mirroring the existing univariate interface. That package-level design decision is separate from this positive standalone composability result; it supplies no inherited verdict to further unassessed laws. No cost argument is used.

**Building blocks:** `Finsupp.lsum_single`, `Mathlib/LinearAlgebra/Finsupp/LSum.lean:123`; storage transport `AddMonoidAlgebra.coeffLinearEquiv`, `Mathlib/Algebra/MonoidAlgebra/Module.lean:75`; component maps use `MvPolynomial.monomial` and `LinearMap.lsmul`. The exact composition sketch is the three-line direct theorem application immediately above.

**Belongs elsewhere:** keep as project-local API in `Roth/HasseDeriv.lean` while the parent package is downstream. This is basic algebraic infrastructure, not an isolated historical theorem for Archive/ or an unrelated satellite library.

**Mechanical future refactor plan, if standalone wrapper removal is authorized:**

1. At `HasseDeriv.lean:94`, replace the rewrite occurrence by the displayed generic term specialized to the induction monomial k,a and order d. At line 127, after `C_apply`, use the same term with k=0. At line 233, after `monomial_mul_monomial`, specialize it to k=a+b, coefficient c*c′ and to k=b, coefficient c′, both with the original order d. These are all four same-file written occurrences.
2. At `Taylor.lean:111`, specialize it to order e, exponent k and coefficient a after rewriting `ih e`; rewrite the hypothesis he using this equality. At line 116, specialize the same generic law to the monomial exponent exposed by each of the two derivative expressions in that rewrite chain (`k` with order `d.erase i`, and `Finsupp.single i n + k` with order d, both coefficient a). Alternatively inline the fully polymorphic equality proved by `fun d k a => Finsupp.lsum_single R (...) k a` as each rw entry, letting rw infer those exponents. Both occurrences in that line must be replaced. These are all three external written occurrences, in the single private Taylor caller.
3. Replace the exact theorem reference in the parent definition docstring at line 53 with the explicit formula, then remove the public theorem at 66–68. Preserve any local simp behavior needed by an implicit consumer by explicitly unfolding `hasseDeriv` in the relevant monomial proof; the written-reference count does not prove there are no additional simp consumers. Rebuild both affected modules and the project before removing the wrapper in production.

The general d,k,a typing is compiler verified by the final direct exact example. This assessment has **not** executed an all-callers source refactor or asserted its build result. Root's read-only assessment scope does not authorize this worker to edit production. The actionable plan names every current explicit caller and distinguishes direct references from implicit simp dependencies.

**Next action:** retain the local semantic helper during this read-only overview; record NO-composable as a standalone mathlib addition. In a future authorized cleanup, inline the accepted generic evaluation at the seven explicit uses on five lines, update the parent docstring, remove the wrapper only after checking implicit simp consumers, and rebuild. Discuss retaining this `@[simp]` law as part of the parent operator package with its reviewer instead of opening a standalone theorem PR.

## Phase 8 — Completion and evidence gate

All required artifacts are complete: baseline/type/axioms; mathematical prose; size and the explicitly inapplicable theorem one-line check; exhaustive literature channels with optional unavailable ChatGPT and failed nLab fetch recorded; generality and actual floor diagnostic; all nine modern-idiom questions with Q8 body diagnostic/Q9 semantic guard; justified theorem n/a for Phase 4.5; all five proof-strategy rows; all five actual mathlib search methods plus the abstract-form repeat; all three statement-shape checks and the successful nsmul alternative; complete qualified caller lines/counts; exact positive composition in both environments; actionable NO rationale and alternative destination.

Native final checks report no errors, no `sorry`, only the standard axioms and no failed dependencies. The initial scratch universe batching failure and retained style warnings are explicit. Search/index limitations are not used as mathematical absence proofs. No production source or Git mutation was performed by this worker. The [completion metadata](../evidence/MvPolynomial.hasseDeriv_monomial/assessment.json), [overview entry](../evidence/MvPolynomial.hasseDeriv_monomial/overview-entry.json), [link verification](../evidence/MvPolynomial.hasseDeriv_monomial/evidence/report-links.json), and [hashed copy manifest](../evidence/MvPolynomial.hasseDeriv_monomial/copy-manifest.json) support completed-only integration. Root's independent acceptance, tracked integration, commit and push are separate and are not claimed here.
