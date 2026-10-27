# MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt — full mathlibable assessment

Verdict: **YES-add-as-is**, within the canonical multivariate Hasse derivative API. A derivative vanishes if its order exceeds the polynomial's degree in even one coordinate. The stronger support-avoidance criterion is a useful companion, while the present degree condition is exactly the interface used by three project callers. This assessment changes no production Lean or pins.

## Phase 0 — baseline and resolution

The shared `lake build` completed successfully, exit 0, 2467 jobs: [baseline-build.txt](../evidence/MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt/baseline-build.txt). All 17 source/pin hashes freshly match that successful baseline: [baseline-fresh-check.json](../evidence/MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt/baseline-fresh-check.json). Canonical source is `Roth/HasseDeriv.lean:219`; the full declaring module and both caller modules were read. [Source hashes](../evidence/MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt/source-hashes.json) and [reference hashes](../evidence/MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt/reference-hashes.json) record exact inputs. Native verification is documented in Phase 6 and its complete accepted receipts.

## Phase 1 — comprehend

For arbitrary variables σ and commutative semiring R, let d be a finitely supported natural multi-index and P a multivariate polynomial. If `degreeOf j P < d j` for some coordinate j, then `hasseDeriv d P = 0`. No finiteness of σ, nonzero assumption, characteristic restriction, cancellation or field structure is required.

Full type, up to universe names: `∀ {σ : Type u} {R : Type v} [CommSemiring R] {j : σ} {d : σ →₀ ℕ} {P : MvPolynomial σ R}, degreeOf j P < d j → hasseDeriv d P = 0`. The native `#check` provides the actual elaborated type; `#print axioms` checks dependencies. The hypothesis excludes every exponent e+d from P's support, since `(e+d) j ≥ d j`; hence all derivative coefficients vanish by `coeff_hasseDeriv`. The exact three-line proof is archived in [target-source.lean.txt](../evidence/MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt/target-source.lean.txt). Project dependencies are `hasseDeriv` and its coefficient identity; degree/support exclusion and coefficient extensionality are mathlib.

## Phase 2 — preliminary checks

SMALL: basic annihilation API for a canonical operator, not a main result, new structure or person-named theorem. One-line-definition check and its three exemption rows are n/a: this is a theorem, not a definition. No prefilter applies; all literature and search phases were executed.

## Phase 3 — exhaustive nine-channel literature protocol

Exact web requests with returned-response SHA256, bytes, status and original short summaries: [web-receipts.json](../evidence/MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt/web-receipts.json). Source titles, locators and limitations: [web-sources.json](../evidence/MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt/web-sources.json). Full copyrighted web bodies are not retained.

| Channel | Actual attempt | Finding |
|---|---|---|
| General web, specific | `multivariate Hasse derivative vanishes degree variable order` | Canonical monomial lowering and coordinatewise vanishing; primary Joints of Varieties. |
| General web, general | `Hasse Schmidt derivative polynomial arbitrary commutative ring degree zero` | Algebraic higher derivatives over commutative rings, beyond fields. |
| General web, aliases | `higher divided derivatives Taylor coefficient monomial binomial vanishing` | Hasse–Schmidt/divided-derivative terminology and Taylor coefficients. |
| ChatGPT MCP | Tool availability inventory | n/a: `ask_chatgpt_math` unavailable; no mathematical second opinion claimed. |
| Local | `clean.tex` §1 lines123–150, §6 lines1500–1517 | Explicit formula over commutative semirings; outside-degree-box derivatives identically zero. [Receipt](../evidence/MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt/literature-local.json). |
| nLab | General and site query; direct `Hasse-Schmidt derivative` open | Indexed text gives commutative-rig multivariate extraction and zero when derivative monomial does not divide input; direct XHTML400. |
| nCatLab | Site query `site:ncatlab.org/ncatlab Hasse Schmidt`, dedicated URL open | Dedicated path inaccessible; no concrete categorical degree-vanishing replacement found. Related graded bimonoid description does not identify one. |
| Stacks | `site:stacks.math.columbia.edu Hasse Schmidt derivations` | No exact coordinate-degree theorem located. Not a proof of absence; abstract differential-operator theory alone does not imply coordinate bounds. |
| MathOverflow | `site:mathoverflow.net Hasse derivative degree vanishing` | Hasse derivative/Laurent Denis discussion supplies positive-characteristic caution; discovery only, not primary proof source. |
| Recent arXiv, five years | `site:arxiv.org Hasse derivatives multivariate 2022 2023 2024 2025 2026`, explicit open2305.04537 | Barajas, submitted2023-05-08, abstract inspected: higher derivations of Hasse–Schmidt algebra, adjacent abstraction; no exact coordinate criterion attributed. Older search hits were not classified recent. |

Primary published comparison: [Tidor–Yu–Zhao, Joints of Varieties (2022)](https://link.springer.com/article/10.1007/s00039-022-00597-5), §4.3 Definition4.2, formula and coordinatewise vanishing at lines590–597. It works over any field; the coordinate-degree criterion is an elementary consequence of its monomial zero clause and linearity, not claimed to be printed there verbatim. [nLab's Hasse–Schmidt derivative](https://ncatlab.org/nlab/show/Hasse-Schmidt+derivative), indexed several-indeterminates definition, gives the commutative-rig version. [Barajas2305.04537](https://arxiv.org/abs/2305.04537), abstract and date, is the recent-primary-source check. No long quotes retained.

Literature summary: canonical multivariate Hasse derivatives kill monomials not divisible by the derivative monomial. Consequently support avoiding the upper cone `{k | d ≤ k}` suffices. The target is the coordinate-degree corollary used to restrict Taylor sums to a box. Abstract Hasse–Schmidt derivations need not lower a chosen coordinate degree: arbitrary higher derivations are a larger, different family, so do not transfer this bound without the canonical coefficient/monomial law. Historical naming varies; the algebraic binomial definition avoids factorial division in positive characteristic.

## Phase 4a–b — every parameter and generality

| Parameter/hypothesis | Mathematical role | Weakening audit |
|---|---|---|
| σ : Type* | Arbitrary variables | Already unrestricted; no Fintype, finite, decidable equality or nonempty typeclass. A supplied j is a chosen coordinate. |
| R : Type* | Coefficients | No fixed field, characteristic or nontriviality. |
| CommSemiring R | Pinned MvPolynomial and R-linear parent interface | Semiring-only literal parent is rejected by compiled missing-instance guard. Abstract coefficient/support proof needs less; changing representation is a separate parent-interface project. |
| j : σ | Witness of an exceeded coordinate | Could be packaged existentially; this is syntactic equivalence, not stronger mathematics. Current implicit j is inferred from h at all callers. |
| d : σ→₀ℕ | Derivative order | Arbitrary; finite support is the polynomial multi-index type, not an extra premise. No d≠0 needed separately. |
| P | Polynomial | Zero allowed; h is a sufficient condition and not necessary. |
| h : degreeOf j P < d j | Excludes every possible surviving input exponent | Strictness essential for this unconditional criterion: P=X j, d=single j 1 has equality of degree and order but derivative1 over ℕ. Cannot replace `<` by `≤` or remove h. |

Parameter generality: MAXIMALLY GENERAL for the fixed parent interface; no successful argument/typeclass drop. More general sufficient criteria are available: `∀ k ∈ P.support, ¬ d ≤ k`, or `∀ e, P.coeff (e+d)=0`. These do not force one uniform coordinate j to exclude every monomial. The exact coefficient-product criterion characterizes zero even in positive characteristic and with zero divisors. They are companion APIs, not evidence that the useful coordinate criterion has an unnecessary parameter. Formally verified variants and counterexamples are in the native bundle; no mere proposed weakening is counted as compiled.

The converse is false: over ZMod2 the first Hasse derivative of X² vanishes even though degree2 is not below order1. Support avoidance is sufficient but not necessary for the same reason. Natural-valued degree of zero is0; the theorem need not cover every zero derivative to be correct. No division by factorials is introduced.

## Phase 4c — all nine modern-idiom questions

| # | Question | Outcome and downstream consequence |
|---|---|---|
| 1 | Typeclasses | Already uses CommSemiring; no bundled informal preamble to replace. |
| 2 | Filters/nets | No topology or convergence. |
| 3 | Universal property | No object constructed; vanishing follows from coefficients, not a universal mapping property. |
| 4 | Bundled substructure | Could state bounded-degree polynomials lie in `LinearMap.ker (hasseDeriv d)`; kernel wording adds lattice composition for families, but three current callers need pointwise equality. No mandatory new bundled replacement shown. |
| 5 | Hierarchy | Already semiring-level canonical interface; general rings/fields from literature specialize. Literal noncommutative Semiring parent guard fails. |
| 6 | Higher categories | No concrete categorical downstream gain located; graded bimonoid adjacency alone is insufficient. |
| 7 | General index | σ arbitrary; natural exponent/order indices are intrinsic to polynomial divisibility. Group exponents change to Laurent objects and this degree criterion. |
| 8 | Concrete via abstract | Diagnostic fires: zero exact `hasseDeriv` identifiers in body, one `coeff_hasseDeriv` substring line, no Hasse-specific occurrence after that rewrite. Generic coefficient-shift annihilation criterion with full normalization premise tested. |
| 9 | False-generalization guard | Coefficient-shift/support premise must stay. Arbitrary linear maps, arbitrary Hasse–Schmidt systems or ordinary iterated derivatives without characteristic qualifications do not supply the same object or necessity criterion. Strictness/converse counterexamples guard two tempting false claims. |

[Exact Q8 diagnostic](../evidence/MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt/q8-diagnostic.json). Abstract proposal: for P,Q and weight w, assume `∀ e, Q.coeff e = w e * P.coeff (e+d)` and `∀ e, P.coeff (e+d)=0`; conclude Q=0 by coefficient extensionality. More generally support avoids d's upper cone. This is real reusable proof organization for shifted weighted coefficient operators. It is new helper proof evidence, not existing mathlib replacement. Generic coefficient extensionality and support exclusion already express the argument; no new public abstraction with downstream capability beyond those APIs was established. Thus Q8 fires and was tested, but does not alone force YES-but-generalise-first. The canonical Hasse criterion remains the discoverable coordinate-degree API.

## Phase 4.5 — infrastructure risks

All six are n/a for theorem: no typeclass diamond (no instance), reducibility leak (no data definition), noncanonical unfolding (no definitional equation added), instance priority collision (no instance), new universe restriction (native polymorphic type checked), or coercion ambiguity (no coercion declaration). Parent definitions require their own assessment.

## Phase 4.6 — all five proof-strategy rows

| # | Strategy question | Finding |
|---|---|---|
| 1 | ε–δ versus filters | n/a, finite algebra. |
| 2 | Elements versus subobjects | Coefficient extensionality directly matches equality to zero; kernel inclusion is optional packaging, not a shorter mathematical argument for current callers. |
| 3 | Sequences versus nets | n/a, no convergence. |
| 4 | Constructions versus universal properties | n/a, no object construction. |
| 5 | Missing helper API | `coeff_hasseDeriv` is substantive missing multivariate bridge; support-zero companion is useful but not needed to avoid a bad proof strategy. |

MATHLIB-IDIOMATIC: extensionality, coefficient shift, support exclusion. Alternative monomial induction through raw parent definition also checked; it requires the actual binomial/support law. A sharp degree bound alone with natural subtraction does not establish vanishing: degree0 also holds for nonzero constants. Do not deduce this theorem merely from `degreeOf Δ ≤ degreeOf P - d`.

## Phase 5 — all five actual mathlib methods on three forms

| Method | Current coordinate form | Literature standard form | Abstract coefficient/support form |
|---|---|---|---|
| Finder | Multivariate Hasse zero above one degree | Hasse–Schmidt polynomial vanishing over commutative semiring | Shift coefficient map annihilates support avoiding upper cone |
| LeanSearch | Same current query | Same general query | Same abstract query |
| Loogle | `MvPolynomial.degreeOf, _ < _, _ = 0`: unrelated Nullstellensatz only | `Polynomial.hasseDeriv, _ = 0`: univariate candidate | `MvPolynomial.coeff, _ = 0` rejected unknown identifier; quoted `"coeff", _ = 0` retry succeeds, generic coefficient hits, no exact bridge |
| rg | Full multivariate hasseDeriv/degreeOf/zero names | Univariate hasseDeriv zero and natDegree | Support exclusion, extensionality, restrictSupport |
| local | `hasseDeriv_eq_zero` | Same source matches include univariate theorem | `notMem_support_of_degreeOf_lt`, `coeff_eq_zero` |

[Finder/Search raw receipts](../evidence/MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt/search-raw.json), [Loogle raw](../evidence/MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt/loogle-raw.json), [successful abstract retry](../evidence/MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt/loogle-retry.json), [local receipts](../evidence/MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt/local-raw.json). Local index is unavailable and source fallback includes archived evidence copies: those are not independent library hits or absence certification. External search revisions may differ from the pin.

[Full-name untruncated search](../evidence/MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt/full-name.json), [current rg](../evidence/MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt/rg-current.json), [literature rg](../evidence/MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt/rg-literature.json), [abstract rg](../evidence/MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt/rg-abstract.json). Positive pinned analogue `Polynomial.hasseDeriv_eq_zero_of_lt_natDegree` at `Mathlib/Algebra/Polynomial/HasseDeriv.lean:89`: `[Semiring R] (p : Polynomial R) (n : ℕ), p.natDegree < n → Polynomial.hasseDeriv n p = 0`. It covers one variable, not arbitrary multi-indices without a compatibility development. Pinned `MvPolynomial.notMem_support_of_degreeOf_lt`, `notMem_support_iff` and extensionality are the generic building blocks. Native checks verify positive candidates; no search failure is treated as proof of absence.

## Phase 5.5 — statement shape

Normal form OK: derivative equality to zero, consistent with the univariate canonical theorem and coefficient extensionality; zero sits on RHS. Equivalent presentations include `hasseDeriv d P = 0`, `P ∈ LinearMap.ker (hasseDeriv d)`, and vanishing of all output coefficients. Support avoidance and coefficient-product iff are stronger/same-conclusion interfaces, not orthogonal duplicates of an existing canonical multivariate theorem.

Syntactic generality OK: existential `∃ j, degreeOf j P < d j` can be unpacked by cases; `∃ j, r j < d j` with `∀ j, degreeOf j P ≤ r j` composes by transitivity. Verified existential and bounded-degree caller forms show no improvement from forcing all callers to construct an existential. Current implicit j,d,P infer directly from h. Superfluous arguments NONE: every type/instance/index/input/premise is audited in Phase4a. Parent CommSemiring is an interface constraint, not a claim that coefficient extensionality intrinsically uses commutative multiplication.

## Phase 6.0 — every explicit caller and inline audit

Three explicit invocations outside declaring module, two files; [callers.json](../evidence/MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt/callers.json). This counts source references, not opaque kernel/simp closure.

| Caller | Role | Refactor/inlining outcome |
|---|---|---|
| `Roth/Taylor.lean:173`, `degreeOf_taylor_le` | Excess exponent e j forces Δ_eP=0 and hence Taylor coefficient0 | Retain canonical theorem. Could inline coefficient ext + coeff_hasseDeriv + support exclusion, duplicating its proof. [Excerpt](../evidence/MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt/caller-taylor-degree.lean.txt). |
| `Roth/Taylor.lean:207`, `eq_sum_box_hasseDeriv` | Outside box r gives `degreeOf j P < e j`; evaluation is zero | Retain, with `(hP j).trans_lt hj`; exact shared bound/evaluation fragment checked. [Excerpt](../evidence/MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt/caller-taylor-box.lean.txt). |
| `Roth/MainLemma.lean:425`, `le_index_of_forall_eval_eq_zero` | Nonzero evaluated derivative must lie in coordinate box | Retain, with `(hd j).trans_lt hj`; same bound/evaluation fragment closes contradiction. [Excerpt](../evidence/MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt/caller-mainlemma.lean.txt). |

[Inline audit](../evidence/MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt/inline-audit.json): Hasse constant and monomial zero arguments are special cases of binomial-factor vanishing, not duplicate coordinate-degree theorems; coefficient/Taylor support proofs use the target or coefficient identity for different conclusions. Separation's univariate support exclusion is transport through `uniqueAlgEquiv`, not the arbitrary multi-index target. No additional inline equivalent was located. No junk finding: three uses support translation degree, finite Taylor expansion and index bounds.

## Phase 6 — actual composition experiments

The exact target is replayed independently of its own theorem. Generic Q8 zero criterion, support and coefficient-product variants, existential wrapper, strictness/converse witnesses and arbitrary coefficient-ring caller fragments are checked. An isolated mathlib-only program defines the raw operator and independently proves its coefficient law before the zero criterion; it guards absence of project targets with `#check_failure` and imports no Roth. The complete disk bundle additionally proves `HasseZeroShiftedInput.shifted_input_zero` and `weighted` from the literal shifted-input coefficient-zero premise. Complete native receipts and exact executed source archives are linked by [verification.json](../evidence/MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt/verification.json).

1. Existing univariate zero theorem: positive pinned check succeeds, but does not supply multivariate compatibility. No ≤3-existing-call reduction established.
2. Coefficient ext + mathlib support exclusion closes once the project coefficient law is supplied. That law is not an existing mathlib call. Raw proof supplies its substantive induction rather than silently importing a project theorem.
3. Newly proved abstract criterion/stronger support companion cannot be counted as existing building blocks. The normalization premise is explicitly present; `LinearMap.ext` alone does not establish it.

Conclusion NOT-COMPOSABLE from ≤3 pinned existing mathlib calls. No closing `simp [defs...]` existing-call composition has been certified; were one found, Phase6b would require BORDERLINE review rather than automatic NO. No failed exact-search or timeout is an absence proof.

Accepted exact source/receipt pairs: [disk-executed.lean.txt](../evidence/MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt/disk-executed.lean.txt), [disk-success.json](../evidence/MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt/disk-success.json); [raw-executed.lean.txt](../evidence/MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt/raw-executed.lean.txt), [raw-success.json](../evidence/MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt/raw-success.json). Rejected initial attempts are separately listed in verification.json and never accepted as proof evidence. The raw exact? example is a trivial tool control, not an absence probe for this target.

## Phase 7 — actionable verdict

**YES-add-as-is**: canonical coordinate annihilation in the multivariate Hasse API, parallel to the univariate theorem, used at three concrete consumers. It supplies the important transition from an out-of-box derivative order to equality zero; weak/sharp natural-degree estimates cannot replace that transition. Positive coefficient-support proof and independent raw operator bridge establish the missing API content, beyond unsuccessful searches. Stronger support and coefficient-product criteria can accompany it; no cost-based downgrade or unverified hypothesis-drop claim is used.

Proposed upstream file `Mathlib/Algebra/MvPolynomial/HasseDeriv.lean`; PR title `feat(Algebra/MvPolynomial/HasseDeriv): add coordinate vanishing criterion for Hasse derivatives`. Group with actually accepted YES declarations from progress: `MvPolynomial.hasseDeriv`, `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseDeriv_map`, `MvPolynomial.hasseDeriv_rename`, `MvPolynomial.hasseDeriv_hasseDeriv`, `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`, `MvPolynomial.pderiv_hasseDeriv`, and `MvPolynomial.degreeOf_hasseDeriv_le`. Do not infer YES for `hasseCoeff`, monomial/apply wrappers, constants or zero identities; their recorded verdicts differ.

Reviewer candidates from actual relevant recent commits: Yaël Dillies, coefficient refactor631b214f (2026-09-02); Moritz Firsching, univariate Hasse map334438da (2026-08-19). [Commit receipt](../evidence/MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt/reviewer-commits.json). These are suggestions, not assignments or messages.

- [ ] `/generalise MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`: preserve demonstrated strictness and parent-interface constraints; consider support-avoidance and exact coefficient iff as companions.
- [ ] `/cleanup Roth/HasseDeriv.lean MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`: full style/import/proof checks and alignment with univariate naming before the coherent parent/API PR.
- [ ] Choose reviewer based on relevant recent history and prepare parent operator plus coefficient, degree and zero APIs together.

Alternative local destination if not upstreamed: retain `Roth/HasseDeriv.lean`, shared by Taylor and MainLemma. No deletion/refactor is warranted by existing pinned API evidence.

## Phase 8 — completion and limitations

Read-only assessment, all required phases complete with theorem n/a infrastructure explanation; no production/pin changes. Both accepted native programs completed with zero errors/warnings, partial=false, timed_out=false, and only propext, Classical.choice and Quot.sound; exact sources/receipts retained. ask_chatgpt unavailable; local index unavailable; direct nLab XHTML400/nCatLab inaccessible; arXiv abstract only; rejected Loogle identifier retained separately from successful retry. Caller experiments include a full replay of `degreeOf_taylor_le`; Taylor207 and MainLemma425 are verified through scoped outside-box/evaluation fragments, not edited whole downstream modules. No universal absence claim. `unresolved=[]`; independent root acceptance pending.
