# MvPolynomial.degreeOf_hasseDeriv_le — full mathlibable assessment

Verdict: **YES-add-as-is**, as the nonincrease corollary in a multivariate Hasse derivative API. Add a sharper primary companion with bound `degreeOf j P - d j`; it has been proved under exactly the same assumptions. This is a strict conclusion improvement, not a dropped hypothesis. The assessment does not change production Lean or pins.

## Phase 0 — baseline and resolution

The shared successful `lake build` completed 2467 jobs with exit 0; [baseline-build.txt](../evidence/MvPolynomial.degreeOf_hasseDeriv_le/baseline-build.txt). All 17 source/pin SHA256 values freshly match the baseline [baseline-fresh-check.json](../evidence/MvPolynomial.degreeOf_hasseDeriv_le/baseline-fresh-check.json), so no rebuild is inferred from stale Git status. Canonical declaration location is `Roth/HasseDeriv.lean:210` (211 is the continuation line). The module develops multivariate Hasse derivatives over commutative semirings. Target has no sorry; native full type and axioms, independent replay, sharp companion, generic witnesses and counterexamples all completed without errors or warnings. Exact programs and receipts: [disk-executed.lean.txt](../evidence/MvPolynomial.degreeOf_hasseDeriv_le/disk-executed.lean.txt), [disk-success.json](../evidence/MvPolynomial.degreeOf_hasseDeriv_le/disk-success.json), [raw-executed.lean.txt](../evidence/MvPolynomial.degreeOf_hasseDeriv_le/raw-executed.lean.txt), [raw-success.json](../evidence/MvPolynomial.degreeOf_hasseDeriv_le/raw-success.json). All printed dependencies use only `propext`, `Classical.choice`, `Quot.sound`.

## Phase 1 — comprehend

For any commutative semiring R, arbitrary variable type σ, variable j, derivative multi-index d and polynomial P, applying the Hasse derivative of order d cannot increase the exponent degree in j. Degree is natural valued, including degree zero for the zero polynomial. Every nonzero output coefficient at m comes from the input coefficient at m+d, so m(j)≤(m+d)(j)≤deg_j(P).

Full elaborated type, with implicit universes, is `∀ {σ : Type u} {R : Type v} [CommSemiring R] (j : σ) (d : σ →₀ ℕ) (P : MvPolynomial σ R), degreeOf j (hasseDeriv d P) ≤ degreeOf j P`. Native receipts give the actual universe names. There are no extra assumptions about finite variables, characteristic, coefficient nontriviality, cancellation or nonzero input/output. Dependencies specific to this project are `hasseDeriv` and `coeff_hasseDeriv`; the degree characterization, nonzero-product implication and exponent arithmetic are pinned mathlib.

## Phase 2 — preliminary checks

SMALL: an elementary support/degree API lemma; not a new structure, a person-named theorem or listed module main result. One-line-definition test and all three exemptions are n/a: theorem, with a three-step proof, not a definition. No prefilter or glue inheritance applies.

## Phase 3 — exhaustive nine-channel literature protocol

Exact requests, returned-response hashes/bytes/status and original summaries are retained in [web-receipts.json](../evidence/MvPolynomial.degreeOf_hasseDeriv_le/web-receipts.json); full web bodies are deliberately not copied. [web-sources.json](../evidence/MvPolynomial.degreeOf_hasseDeriv_le/web-sources.json) records source locators and access limitations.

| Channel | Actual attempt | Finding |
|---|---|---|
| General web, specific | `multivariate Hasse derivatives degree in each variable bound degree minus multiindex` | Standard monomial exponent lowering; primary Joints of Varieties and ECCC2023 found. |
| General web, general | `Hasse derivatives polynomial ring arbitrary characteristic Taylor expansion degree bound` | Taylor coefficient extraction works in arbitrary characteristic; degree may drop further. |
| General web, aliases | `Hasse Schmidt higher divided derivatives multidegree order polynomial` | Higher/Hasse–Schmidt terminology; divided powers and polynomial differential operators are adjacent general structures. |
| ChatGPT MCP | Availability inventory | n/a: `ask_chatgpt_math` unavailable; no substitute opinion claimed. |
| Local | `clean.tex` §1 lines123–150; §2 Lemma2 lines348–435; §6 degree uses | Explicit binomial monomial formula and coefficient-shift interface; Lemma2 uses weak degree bounds for determinant entries. |
| nLab | Indexed `Hasse-Schmidt derivative`, definition for several indeterminates | Commutative rig, monomial extraction, zero if derivative monomial does not divide input. Direct XHTML fetch unsupported400; indexed text available. |
| nCatLab | Site queries for Hasse derivative and categorical Hasse–Schmidt; dedicated URL open | Dedicated `/ncatlab/show/...` inaccessible. Related nLab graded bimonoid description suggests graded organization; no categorical coordinate-degree theorem identified. |
| Stacks | Site queries `Hasse derivation`, `Hasse Schmidt higher derivations`, exact `Hasse-Schmidt` | No relevant coordinate-degree theorem located; unrelated contributors hits rejected. No absence claim. |
| MathOverflow | `Hasse derivatives degree multivariate`; replacement for derivations in characteristic p | Laurent Denis question highlights characteristic-p overclaims; replacement-derivation discussion points to Hasse/jet theory. These are discovery/context only, not primary mathematical proof sources. |
| Recent arXiv, last five years | Recency query and explicit 2024/2025 queries, then open2305.04537 | Paul Barajas, submitted2023-05-08, higher derivations of Hasse-Schmidt algebra, abstract only: adjacent abstraction, no coordinate-degree theorem. Older results returned by search were not misclassified as recent. Two guessed unrelated arXiv IDs were rejected. |

Primary published comparison: [Tidor–Yu–Zhao, Joints of Varieties (2022)](https://link.springer.com/article/10.1007/s00039-022-00597-5), §4.3 Definition4.2, formula and zero condition, lines587–607. [Harsha–Kumar–Saptharishi–Sudan, ECCC TR2023-182](https://eccc.weizmann.ac.il/report/2023/182/download/), Definition2.3, PDF page13, defines multivariate Hasse derivatives by Taylor coefficient extraction. The sharper coordinate inequality is our mathematical inference from the monomial formula, subsequently compiled; those papers are not claimed to state that exact Lean inequality. The nLab rig formulation confirms no field/division requirement. [Barajas2305.04537](https://arxiv.org/abs/2305.04537), abstract and submission date, is the recent-arXiv check.

Literature summary: canonical Hasse partial derivatives lower each surviving monomial exponent by d. Thus the natural-valued bound `deg_j Δ_d P ≤ deg_j P - d_j` is valid and stronger than the target. The target is its useful weak corollary. Arbitrary characteristic requires inequalities; equality can fail when binomial coefficients vanish. The local source uses exactly the weak bound. Literature frequently uses finite tuples/fields; Lean's arbitrary σ and commutative-semiring form already encompasses those settings.

## Phase 4a–b — all parameters and genuine strengthening

| Argument | Role and actual audit | Weakening outcome |
|---|---|---|
| σ : Type* | Arbitrary variable index, no finiteness/DecidableEq assumption | Already unrestricted polynomial variable type. |
| R : Type* | Arbitrary coefficients | Already unrestricted within pinned MvPolynomial interface. |
| CommSemiring R | Needed to form this canonical MvPolynomial and its R-linear Hasse operator | Literal `[Semiring S]` target fails under `#check_failure MvPolynomial σ S`; this is an interface floor, not a claim that abstract coefficient support needs commutative multiplication. |
| j : σ | Degree coordinate | Essential; bound valid independently for every j. |
| d : σ→₀ℕ | Arbitrary finite-support derivative order | No positivity, box membership or order restriction to drop. ℕ encodes polynomial exponents; arbitrary groups would change the object. |
| P | Arbitrary polynomial | Neither P≠0 nor Δ_dP≠0 required; zero case verified. |

Parameter generality: MAXIMALLY GENERAL for the fixed pinned parent interface; zero successful argument/typeclass weakenings. This does **not** mean the conclusion is maximally strong. The following stronger conclusion is actually verified with the same parameters:

```lean
degreeOf j (hasseDeriv d P) ≤ degreeOf j P - d j
```

Its proof uses `degreeOf_le_iff`, the coefficient shift, `monomial_le_degreeOf` and `Nat.le_sub_of_add_le`. The `Unit`/ℕ monomial X³ with d=1 has exact degrees 2 and3, proving strict improvement. The candidate untruncated additive bound `deg_j Δ_dP + d_j ≤ deg_j P` without nonzero output is false: P=0,d_j=1 gives1≤0, formally refuted. Hence do not replace natural subtraction blindly with addition. No raised limits, axioms, unsafe computation or placeholders were used. Cross-coefficient support abstraction is discussed below; it does not weaken the parent definitions.

## Phase 4c — all nine modern-idiom rows

| # | Question | Finding and downstream consequence |
|---|---|---|
| 1 | Typeclasses | Already CommSemiring; no bundled preamble to replace. |
| 2 | Filters/nets | No topology or limits. |
| 3 | Universal property | No object construction; a support bound, not a universal mapping property. |
| 4 | Bundled substructures | Box-degree filtered submodules could organize families, but existing `degreeOf_le_iff` already supplies support membership; no new bundled formulation needed for the five consumers. |
| 5 | Hierarchy weakening | Semiring literal probe fails at parent type; abstract support proof may allow different coefficient semirings and does not change the canonical object. |
| 6 | Higher categories | nCatLab/graded-bimonoid adjacency gives no concrete improved degree API here. |
| 7 | General indices | σ arbitrary already; replacing natural exponents by general groups changes polynomials to another object and loses this degree. |
| 8 | Concrete via abstract | Diagnostic fires: zero exact `hasseDeriv` identifiers in body, one substring line `coeff_hasseDeriv`, zero Hasse references after that rewrite. Generic cross-coefficient shift criterion verified, with actual map and support-truncation consumers. |
| 9 | False-generalization guard | Cross-coefficient criterion preserves the support implication and specializes to actual Δ; no false widening accepted. Arbitrary operator with no support premise, Laurent exponents, unconditional degree equality, and untruncated additive inequality are rejected. |

Exact Q8 counts and body: [q8-diagnostic.json](../evidence/MvPolynomial.degreeOf_hasseDeriv_le/q8-diagnostic.json). Verified generic signature:

```lean
∀ {R S} [CommSemiring R] [CommSemiring S] (j : σ) (d : σ →₀ ℕ)
  (P : MvPolynomial σ R) (Q : MvPolynomial σ S),
  (∀ m, Q.coeff m ≠ 0 → P.coeff (m + d) ≠ 0) →
  degreeOf j Q ≤ degreeOf j P - d j
```

This is a real abstraction: native proofs instantiate d=0 for coefficient maps and support truncation. It is **new helper proof evidence**, never an existing mathlib replacement. The diagnostic alone does not mandate a new public theorem: pinned `degreeOf_eq_sup`/`degreeOf_le_iff` already characterize all such support bounds, and `degrees_map_le` at Degrees178 handles the map case from `support_map_subset`. Support truncation likewise follows from finite support sup monotonicity. The generic helper packages that existing proof organization with shifted arithmetic; no downstream proof blocked by the existing support characterization was identified. Therefore modern idiom available as a diagnostic helper, but no material public-API replacement established; no MODERN-IDIOM generalise-first claim. Canonical Hasse nonincrease remains discoverable and avoids repeatedly unfolding coefficient shifts.

## Phase 4.5 — six infrastructure risks

All six rows are n/a because this declaration is a theorem: typeclass diamonds (no instance), reducibility leak (no data definition), noncanonical unfolding (no added definitional equation), instance-priority collision (no instance), universe obstruction (native polymorphic type already elaborates), coercion ambiguity (no coercion declaration). Parent operator design is assessed separately, not silently inherited as proof of this theorem.

## Phase 4.6 — all five proof-strategy rows

| # | Strategy question | Outcome |
|---|---|---|
| 1 | ε–δ versus filters | n/a, finite algebra. |
| 2 | Elements versus subobject inclusions | Support argument is the canonical `degreeOf_le_iff` interface; introducing a submodule adds no needed step. |
| 3 | Sequences versus nets | n/a, no convergence. |
| 4 | Construction versus universal property | n/a, no construction. |
| 5 | Missing helper API | The project-specific `coeff_hasseDeriv` is the substantive multivariate missing API anchor. Generic support criterion already available; a sharp Hasse degree companion is valuable. |

Strategy MATHLIB-IDIOMATIC. Native independently replayed the exact coefficient proof and sharp proof, then proved an isolated raw operator coefficient identity by polynomial induction before its sharp degree bound. Thus degree proof is not circular through the target or downstream simp lemmas. No negative `exact?` absence certification is claimed: the raw bundle's successful `exact?` example is only a tool control, not the degree goal.

## Phase 5 — all five actual mathlib methods, all three forms

| Method | Current form | Literature/sharp form | Abstract support form |
|---|---|---|---|
| Lean-Finder | degreeOf Hasse nonincrease | multivariate degree minus multiindex | coefficient-shift support bound |
| LeanSearch | same current query | same sharp query | same abstract query |
| Loogle | `MvPolynomial.degreeOf, "hasseDeriv"` empty | `Polynomial.hasseDeriv, Polynomial.natDegree, _ ≤ _ - _` gives univariate candidate; `MvPolynomial.degreeOf, _ ≤ _ - _` empty | `MvPolynomial.degreeOf, MvPolynomial.support, _ ≤ _` gives degree support API |
| rg | complete mathlib degreeOf/hasseDeriv and degreeOf/pderiv search empty | pinned uni Hasse degree lemmas | degreeOf characterization, support sup and map degree API |
| local names | degreeOf_hasseDeriv returns only project target | natDegree_hasseDeriv returns uni bounds | degreeOf_le returns characterization |

All six Finder/Search queries succeeded with complete receipts [search-raw.json](../evidence/MvPolynomial.degreeOf_hasseDeriv_le/search-raw.json). Loogle three-form originals [loogle-raw.json](../evidence/MvPolynomial.degreeOf_hasseDeriv_le/loogle-raw.json), stronger multivariate retry [loogle-stronger.json](../evidence/MvPolynomial.degreeOf_hasseDeriv_le/loogle-stronger.json); first stronger attempt hit 3/30s rate limit and was retried successfully, not treated as empty. Local index reports unavailable while returning source matches: [local-raw.json](../evidence/MvPolynomial.degreeOf_hasseDeriv_le/local-raw.json); this is not absence evidence. Full-name untruncated search [full-name.json](../evidence/MvPolynomial.degreeOf_hasseDeriv_le/full-name.json), current [rg-current.json](../evidence/MvPolynomial.degreeOf_hasseDeriv_le/rg-current.json), standard [rg-literature.json](../evidence/MvPolynomial.degreeOf_hasseDeriv_le/rg-literature.json), abstract [rg-abstract.json](../evidence/MvPolynomial.degreeOf_hasseDeriv_le/rg-abstract.json).

Positive pinned candidate `Polynomial.natDegree_hasseDeriv_le` at `Mathlib/Algebra/Polynomial/HasseDeriv.lean:179` has full type `∀ {R} [Semiring R] (p : Polynomial R) (n : ℕ), (Polynomial.hasseDeriv n p).natDegree ≤ p.natDegree - n`; native #check verifies it. It handles one variable, not arbitrary σ; transporting a multivariate operator to iterated univariates needs compatibility machinery, not specialization of that theorem. `MvPolynomial.degreeOf_le_iff` at Degrees235 and `monomial_le_degreeOf` at268 are actual pinned checks and support building blocks. Finder informal descriptions sometimes conflate coordinate and total degree; pinned types control the assessment. Conclusion: partial univariate analogue and generic support infrastructure found; no existing target replacement established. Search indexes may differ from pin; no universal absence theorem is claimed.

## Phase 5.5 — all statement-shape checks

Normal form: coordinate natural degree inequality, coherent with `degreeOf_le_iff`. Alternative forms are a support bound, a degree-box preservation implication, and the sharper subtraction inequality. Keep the target nonincrease theorem as the weak, directly composable corollary; add the sharp primary theorem in the same API, matching the univariate convention. The target is already a canonical useful consequence, not an orthogonal equivalence; RHS convention n/a to inequality and small-left orientation respected.

Syntactic-generality attempt: native `caller_bound` proves `degreeOf j P≤r → degreeOf j (Δ_dP)≤r` from the sharp bound with `Nat.sub_le`. This covers all five source invocations without changing how hP is supplied. Explicit j,d,P are convenient for dot-notation transitivity. Do not replace the current signature by an arbitrary ambient bound r that users can already provide via `.trans`.

Superfluous-argument audit: σ,R,CommSemiring,j,d,P are each required as explained in Phase4a; no dead hypothesis or extra typeclass. SHIP-AS-STATED for the weak corollary, with a recommended sharp companion (not a claim that the weak bound is strongest). Naming of the sharp companion should be chosen against mathlib's current conventions during cleanup; it is not a reason to stop assessment.

## Phase 6.0 — all explicit callers and inline audit

Five invocations, two external-to-file caller files, no same-file invocation. Scope is source-level references, not kernel closure. [callers.json](../evidence/MvPolynomial.degreeOf_hasseDeriv_le/callers.json), [caller-coeffnorm.lean.txt](../evidence/MvPolynomial.degreeOf_hasseDeriv_le/caller-coeffnorm.lean.txt), [caller-mainlemma.lean.txt](../evidence/MvPolynomial.degreeOf_hasseDeriv_le/caller-mainlemma.lean.txt).

| Caller | Exact pattern | Action if sharp companion added |
|---|---|---|
| Roth/CoeffNorm.lean:253, `degreeOf_det_hasseDeriv_le` | `(degreeOf_hasseDeriv_le _ _ _).trans (hP j)` | Retain weak corollary; alternatively insert sharp bound followed by `Nat.sub_le` before hP. |
| Roth/MainLemma.lean:465, `abs_eval_iterated_hasseDeriv_lt_aux` | `(degreeOf_hasseDeriv_le j k P).trans (hP j)` | Same, k derivative of P. |
| Roth/MainLemma.lean:467, same declaration | `(degreeOf_hasseDeriv_le j i _).trans (hdQ j)` | Same, i derivative of Δ_kP; input degree premise is hdQ. |
| Roth/MainLemma.lean:491, `exists_hasseDeriv_index_eval_bound_aux` | `(degreeOf_hasseDeriv_le j k P).trans (hd j)` | Same, establishes selected Q stays in original degree box. |
| Roth/MainLemma.lean:504, `abs_coeff_diag_hasseDeriv_modByMonic_le_aux` | `(degreeOf_hasseDeriv_le k j P).trans (hd k)` | Same with k degree coordinate and j derivative multi-index. |

Native `caller_bound` verifies the exact general transitivity pattern to arbitrary r; full CoeffNorm/MainLemma bodies were read, but not rebuilt under any production change because no change was made. Inline audit [inline-audit.json](../evidence/MvPolynomial.degreeOf_hasseDeriv_le/inline-audit.json) inspected all `degreeOf_le_iff`, `monomial_le_degreeOf`, `coeff_hasseDeriv`, and degree/Hasse combinations. `degreeOf_taylor_le` at Taylor172 is translation, `degreeOf_coeffNone_le` at Separation116 coefficient extraction, Separation177 univariate transport, and MainLemma294 box-family support conversion: related degree-support proofs, not rederivations of the target. CoeffNorm coefficient/norm bounds use coefficient shifts for different norm conclusions. No equivalent Hasse degree nonincrease inline rederivation found. Five uses establish reusable API; no junk/dead-code finding.

## Phase 6 — actual composition experiments

1. Existing univariate `Polynomial.natDegree_hasseDeriv_le`: pinned type verified; insufficient for arbitrary σ without a multivariate-to-iterated-univariate compatibility development. Not ≤3 existing calls.
2. Generic support characterization: exact target replay uses coefficient rewrite, extraction of nonzero input coefficient and exponent comparison. Crucial `coeff_hasseDeriv` is project API, not an existing mathlib building block. Isolated raw program defines the actual operator, proves its coefficient identity by monomial/addition induction, then proves the degree estimate. This substantive bridge is not a composition of existing mathlib facts alone.
3. Newly proved `support_shift_cross` specializes to the sharp Hasse result after supplying the coefficient-shift premise. This helper was just proved in scratch; cannot manufacture a NO verdict by counting it as existing library content. Generic arithmetic closes the final step, not the Hasse-specific premise.

Conclusion NOT-COMPOSABLE from ≤3 pinned existing mathlib calls. No closing `simp [defs...]` composition has been certified. Prior unrelated exact-search exhaustion is not repeated or converted into absence evidence.

## Phase 7 — verdict and actionable upstream plan

**YES-add-as-is**, useful weak corollary within the multivariate Hasse API. The concrete gap is a degree-box preservation interface for canonical multivariate Hasse derivatives in arbitrary characteristic. All five consumers repeatedly require this interface to feed existing determinant degree, evaluation and coefficient-bound APIs. The multivariate parent operator and coefficient-shift bridge are not in the pinned API; the univariate sharp theorem does not supply that bridge. This is positive API evidence, not merely a failed-search argument.

The literal sharp bound has been proved and is strictly better; ship it as the primary companion, then derive the weak corollary. Retaining this target makes degree-box preservation a single discoverable lemma as used at five sites, parallel to mathlib's weak derivative degree bounds. No claim that the current conclusion is maximally strong is made. No assumption-drop generalise-first claim is justified, and the Q8 abstraction overlaps support-sup infrastructure already present. The verdict does not depend on implementation cost.

Proposed file: `Mathlib/Algebra/MvPolynomial/HasseDeriv.lean`. PR title: `feat(Algebra/MvPolynomial/HasseDeriv): add coordinate degree bounds for Hasse derivatives`. Group with already assessed YES `MvPolynomial.hasseDeriv`, `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseDeriv_map`, `MvPolynomial.hasseDeriv_rename`, `MvPolynomial.hasseDeriv_hasseDeriv`, and the independently assessed `MvPolynomial.pderiv_hasseDeriv`; avoid a standalone one-lemma PR lacking the parent operator. Add sharp primary companion `degreeOf j (Δ_dP) ≤ degreeOf j P - d j`, keep current nonincrease name for callers, and decide whether the generic support helper is local proof organization or a separately justified Degrees addition. Reviewer candidates from actual recent relevant file commits: Yaël Dillies (MvPolynomial coeff-deletion refactor631b214f,2026-09-02), Moritz Firsching (univariate Hasse map334438da,2026-08-19); [reviewer-commits.json](../evidence/MvPolynomial.degreeOf_hasseDeriv_le/reviewer-commits.json). They are candidates, not assigned reviewers.

- [ ] `/generalise MvPolynomial.degreeOf_hasseDeriv_le`: preserve the demonstrated semiring/interface distinction and include the compiled sharp bound; do not reopen guessed assumption drops as facts.
- [ ] `/cleanup Roth/HasseDeriv.lean MvPolynomial.degreeOf_hasseDeriv_le`: full style/import/proof checks before upstreaming, select sharp companion name and derive weak corollary through it.
- [ ] Pick reviewer from recent relevant commits; prepare the coherent parent/API PR above.

Project alternative destination if not upstreamed: retain in `Roth/HasseDeriv.lean`, a genuine common API used by two modules. No deletion/refactor of five consumers is warranted by current pinned evidence.

## Phase 8 — completion and limits

All phases complete with theorem n/a infrastructure explanation. Read-only assessment; no production edit, pin change, PR or message to an external person. Native accepted programs have no placeholders or raised limits. Search services and unavailable local index do not prove absence; ask_chatgpt unavailable, nCatLab dedicated URL inaccessible, direct nLab XHTML failed, recent arXiv abstract only. Caller experiment scope is the shared transitivity fragment, not whole downstream rebuild. These limits do not leave a missing verification obligation for the completed read-only assessment. `unresolved=[]`; root independent acceptance pending.
