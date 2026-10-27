# `MvPolynomial.eq_sum_box_hasseDeriv` — full assessment 73/293

**Verdict: YES-but-generalise-first.** Production sources and pins remain unchanged. This is a read-only assessment; scratch proofs and receipts provide its formal evidence.

## Phase 0 — baseline and scope

The declaration resolves at **Roth/Taylor.lean:197–213**, in the module implementing multivariate polynomial translation, Hasse coefficient identification, and finite Taylor expansion. It is a public theorem with no simp attribute. The reusable clean baseline is commit `99f19fda4b3cbee38fc0d31af76075834f5cc265`, `lake build` exit 0, 2467 jobs, no reported warnings or errors. All **17** current production source/version-pin hashes freshly match that baseline: [inputs](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/inputs.json), [check](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/input-hash-check.json), [build](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/baseline-build.txt). This declaration does not finish the Taylor file; its file-completion build is due after declaration 74. Source and metadata are archived: [Taylor](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/Taylor-module.lean.txt), [canonical entry](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/canonical-entry.json), [order](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/order-entry.json).

## Phase 1 — mathematical content and proof

Let P be a polynomial in finitely many variables over a commutative ring, with coordinatewise degree bounds r. At any point α, P is exactly the finite sum of its Hasse derivative values at α times the corresponding products of powers of X−α, with multi-indices running over the entire coordinate box bounded by r. This is an algebraic identity, with no convergence, characteristic-zero assumption, division by factorials, or nonzero-polynomial condition.

Full native type:

```lean
∀ {σ : Type u_1} {A : Type u_2} [CommRing A] [Fintype σ] [DecidableEq σ] (α : σ → A) (r : σ → ℕ) (P : MvPolynomial σ A), (∀ j, MvPolynomial.degreeOf j P ≤ r j) → P = ∑ d ∈ Roth.box r, MvPolynomial.C (MvPolynomial.eval α (MvPolynomial.hasseDeriv d P)) * ∏ j, (MvPolynomial.X j - MvPolynomial.C (α j)) ^ d j
```

Parameters are independent-universe variable and coefficient types σ and A; a commutative-ring structure on A; a finite enumeration and currently decidable equality on σ; arbitrary α : σ → A, bound r : σ → ℕ, and polynomial P. The sole mathematical hypothesis hP bounds every degreeOf j P by r j. No positivity is required of r, and the empty variable type and zero polynomial are allowed.

**How.** First identify the translated polynomial taylor α P coefficient by coefficient with the finite sum of monomials whose coefficients are eval α (hasseDeriv d P). For an index outside Roth.box r, use `Roth.mem_box` to find a coordinate with exponent above its degree bound; `hasseDeriv_eq_zero_of_degreeOf_lt` annihilates its Hasse derivative. Apply inverse translation using `taylor_neg_taylor`. Finally `taylor_monomial` and `Finsupp.prod_fintype` turn the translated monomials into the displayed products of X−α. The 15-line proof is not just universal-property bookkeeping: the off-box vanishing and coefficient/Hasse identification are substantial mathematical inputs.

Direct project dependencies: **MvPolynomial.taylor, coeff_taylor, hasseDeriv, hasseDeriv_eq_zero_of_degreeOf_lt, taylor_neg_taylor, taylor_monomial, Roth.box, Roth.mem_box**. Some are referenced by the intermediate typed expression or statement, not exclusively an explicit rewrite token. [Proof diagnostic](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/proof-body-diagnostic.json).

## Phase 2 — preliminary checks

**BIG**: full algebraic multivariate Taylor reconstruction is a named foundational theorem, not a helper normalization. The one-line-definition gate is **n/a: theorem**; a short proof does not trigger definition exemptions. The proof and all surrounding source declarations were read, including the direct evaluated caller. Having one direct caller does not make this substantive theorem a wrapper.

## Phase 3 — exhaustive literature protocol

Every search below was actually attempted. Exact requests, response SHA256/byte counts and credential-safe returned URL metadata are retained in [web 0](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/web-0.json), [web 1](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/web-1.json), [web 2](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/web-2.json), [direct access 3](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/web-3.json), and [supplementary 4](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/web-4.json). Those artifacts deliberately do not copy full article/search bodies. All returned URL queries/fragments were stripped defensively; exact search requests and response digests remain intact.

| Channel | Exact query/access | Finding and limitations |
|---|---|---|
| General web: specific | `multivariate polynomial Taylor formula Hasse derivatives arbitrary commutative ring` | Search-exposed primary research article [Fast Multivariate Multipoint Evaluation over All Finite Fields](https://doi.org/10.1145/3652025), §3.2 Definition 3.4 and Proposition 3.5: multivariate Hasse operators are translated coefficients over a commutative ring. The later direct DOI open failed403; do not read this as a successful full-page download. The recent arXiv abstract independently verifies bibliographic metadata. |
| General web: broader | `polynomial Taylor expansion Hasse derivative positive characteristic finite sum multi index` | Algebraic, factorial-free Taylor identity appears in finite-field polynomial-method literature. [Hilbert functions and the finite degree Zariski closure in finite field combinatorial geometry](https://doi.org/10.1016/j.jcta.2015.03.011), §6 equations (6.1)–(6.2), gives expansion about an arbitrary point and explains positive-characteristic Hasse formulation. |
| General web: aliases | `higher derivations Hasse Schmidt polynomial translation binomial expansion` | Hasse–Schmidt/higher-derivation language offers a broader algebraic framework. It does not eliminate this finite polynomial identity; no categorical replacement theorem was identified. |
| Optional ChatGPT math | n/a: `ask_chatgpt_math` unavailable and explicitly optional | No claimed second-opinion response; other channels were not reduced. |
| Local references | Actual rg for `Taylor|Hasse|expansion` in clean.tex; read §4 lines500–529 | Exact project theorem with real coefficients and coordinate box; proof by linearity and monomial binomial expansion. [Excerpt](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/clean-excerpts.tex.txt), [locator/hash](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/local-literature.json), [search](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/rg-local-literature.json). |
| nLab | `site:ncatlab.org Hasse Schmidt derivation Taylor polynomial`; direct [Hasse–Schmidt derivative](https://ncatlab.org/nlab/show/Hasse-Schmidt+derivative) | Search locates higher-derivation context. Direct page access failed with unsupported XHTML content type (400); no invented successful full-page read. |
| nCatLab / categorical | `site:ncatlab.org Taylor expansion polynomial ring`; supplementary `site:ncatlab.org/ncatlab "Taylor" "Hasse"` | No specific higher-categorical replacement found. The supplementary query also returned unrelated Hasse–Weil/Taylor-name matches, which are excluded as evidence for this polynomial law. Underlying polynomial universal property is relevant; categorification is not required. |
| Stacks | `site:stacks.math.columbia.edu Hasse derivation Taylor polynomial`; direct [Hasse bibliography](https://stacks.math.columbia.edu/bibliography/Has) | Search returned bibliography/divided-power context. Direct bibliography access failed403; this is not an independently read proof of the displayed multivariate formula. |
| MathOverflow | `site:mathoverflow.net Hasse derivative multivariate Taylor formula`; direct [formal multidimensional Taylor series over commutative rings](https://mathoverflow.net/questions/288218/formal-multidimensional-taylor-series-expansion-over-commutative-rings) | Discusses arbitrary-ring algebraic expansion and the role of factorial-free coefficients. Used as formulation/history context, not an authoritative replacement for native theorem validation. |
| Recent arXiv, five-year window | `site:arxiv.org Hasse derivatives Taylor expansion multivariate 2022 2023 2024 2025 2026`; supplementary `site:arxiv.org/abs "Fast Multivariate Multipoint Evaluation" "Hasse"`; direct abstracts | [2205.00342](https://arxiv.org/abs/2205.00342), submitted **30 April2022**, authors Bhargava–Ghosh–Guo–Kumar–Umans, is within the current2026-10-27 five-year window and is the preprint of the directly relevant JACM article. [2305.04537](https://arxiv.org/abs/2305.04537), Paul Barajas, submitted **8 May2023**, concerns higher derivations of Hasse–Schmidt algebras; adjacent framework only. The general arXiv query also returned irrelevant analytic/ML Taylor papers, not accepted as mathematical matches. |

**Synthesis.** The standard name is algebraic multivariate Taylor expansion in Hasse derivatives, equivalently coefficient extraction after a constant shift. The finite bound-box formula is valid over arbitrary commutative rings in all characteristics; the local real-coefficient statement is a specialization. Infinite-variable polynomials still have finite support, permitting a different support-indexed theorem, but the particular full-coordinate product and Roth.box formulation here require finite variables. Literature varies between full translated-support sums, total-degree truncations, and coordinatewise boxes; those are meaningful presentations, not literally the same Lean type.

## Phase 4a–4b — parameter and generality audit

| Parameter/hypothesis | Role; weakening assessment |
|---|---|
| σ : Type* | Arbitrary finite variable type, not fixed Fin n. Independent universes preserved. |
| A : Type*, CommRing A | Arbitrary commutative coefficient ring; no domain, field, characteristic, nontriviality or order assumptions. Subtraction X−Cα and inverse shift need additive inverses in this spelling. A semiring addition-form Taylor identity is related but changes the conclusion and is not a mechanical deletion of CommRing. |
| Fintype σ | Needed to form the current full product over j and Roth.box r. An arbitrary-σ finite-support reconstruction is a separately tested representation; it is not the same bound-box statement without this instance. |
| DecidableEq σ | The supplied equality-decision binder can be removed. Native proof uses `open Classical in` around the theorem so its statement can form Roth.box, and proof-local `classical`. This is not just a proof-local deletion: the original statement mentions instance-dependent box data. Original arbitrary instances are recovered propositionally using `Subsingleton.elim`, then `cases`, and the full original evaluated caller compiles. Bare definitional/simp transport attempts failed and are retained as rejected preparations. |
| α | Arbitrary center. No equal-coordinate or distinguished-center assumption. |
| r | Arbitrary natural coordinate bounds, including0. No positive denominators or strict positivity. |
| P | Arbitrary polynomial, including0; no support/nonzero conditions. |
| hP | Essential to restrict to this particular box. Without a bound the omitted coefficient can be nonzero, e.g. X with r=0 and α=0. Support-indexed reconstruction replaces this hypothesis with an actual support range; it does not prove this same formula for an arbitrary r. |

**STRICTLY NARROWER THAN STANDARD: 1 verified weakening.** Remove the explicit DecidableEq binder using scoped Classical for the statement and the same mathematical proof with local classical. This changes no center, bound, polynomial, degree assumption or mathematical conclusion. The instance bridge is **propositional, not definitional**; the successful original-instance recovery and both complete evaluated callers make it actionable. This is not an untested “looks unused” guess. Cost CHEAP: statement scoping and a short proof-irrelevance transport where callers retain arbitrary instances.

```lean
open Classical in
theorem withoutDecidableEq {σ A : Type*} [CommRing A] [Fintype σ]
    (α : σ → A) (r : σ → ℕ) (P : MvPolynomial σ A)
    (hP : ∀ j, degreeOf j P ≤ r j) :
    P = ∑ d ∈ Roth.box r,
      C (eval α (hasseDeriv d P)) * ∏ j, (X j - C (α j)) ^ d j
```

The excerpt shows only the proposed signature; the **full successful proof** is [native target](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/native-target-executed.lean.txt). No other weakening is claimed verified. [Structured audit](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/generality.json).

## Phase 4c — all nine modern-idiom checks

| # | Check | Answer; concrete downstream consequence |
|---|---|---|
| 1 | Typeclasses instead of bundled informal preambles | Already uses CommRing/Fintype. Eliminate the explicit equality-decision requirement only by the verified scoped-Classical theorem and instance transport, not by guessing. |
| 2 | Filters/nets instead of sequences/metrics | No: exact finite algebraic identity has no limiting operation. |
| 3 | Universal property | Yes as a **proof organization**: aeval/eval₂ packages substitution; generic reconstruction transports coefficients. It cannot supply the Hasse coefficient relation or degree support bound. Helps expose a reusable support-indexed reconstruction lemma. |
| 4 | Bundled substructure | Optional bounded-degree submodule packages the family of hP, but this one theorem should retain a readily supplied coordinatewise bound; no new submodule construction was claimed necessary or tested as an existing replacement. |
| 5 | Weaker algebra hierarchy | Arbitrary CommRing already removes the source’s real-field assumptions. Semiring has an addition-centered identity rather than this subtraction form. Explicit DecidableEq removal is verified separately; no unsupported field-to-module claim. |
| 6 | Higher category | No: no categorical coherence or derived structure in this finite polynomial identity. |
| 7 | Generalize concrete indices | σ already arbitrary. Natural exponents encode polynomial monomials and Hasse multi-indices; an arbitrary additive monoid does not retain this mathematics automatically. |
| 8 | Concrete-via-abstract diagnostic | The proof’s coefficient comparison is generic reconstruction **once** the nontrivial Hasse coefficient and off-box vanishing facts are supplied. The proof still uses taylor at inverse transport and taylor_monomial; the named polynomial is an arbitrary P, not one concrete special witness. Separate generic support reconstruction can help both this and other substitution identities, but does not subsume the principal theorem. [Diagnostic](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/proof-body-diagnostic.json). |
| 9 | False-generalization guard | Dropping Fintype while keeping an all-variable finite product/box is not well-formed; arbitrary monoid exponents or noncommutative substitutions change the object. A support-indexed formulation and arbitrary commutative algebra evaluation are honest new APIs, not an already existing more-general theorem. |

**Modern-idiom verdict:** keep the polynomial expansion as an explicit finite identity while using aeval/AlgHom for substitution. Prefer standard Finsupp interval/box infrastructure upstream to a new Roth-prefixed box. This is a representation normalization/pre-PR obligation; no unverified interval transport has been presented as native-proved or as a finished weakening.

## Phase 4.6 — proof-strategy audit

| # | Question | Answer and action |
|---|---|---|
| 1 | ε–δ versus filters | n/a, no topology. |
| 2 | Elements versus ideal/submodule inclusions | Coefficient extensionality is the correct equality principle for this finite identity. Turning the proof into ideal inclusions would not prove the exact coefficients. |
| 3 | Sequences versus nets | n/a, no convergence. |
| 4 | Explicit construction versus universal property | Current proof already exploits the translation AlgHom and inverse substitution. Generic aeval reconstruction may shorten the final transport, without removing the coefficient/support argument. |
| 5 | Missing helpers mathlib should have | **coeff_taylor**, already assessed YES; Hasse derivative degree-vanishing API, plus optionally coefficient-support reconstruction after translation. These are genuine algebraic Taylor infrastructure, not a reason to duplicate their proofs in every caller. |

**Strategy verdict: MATHLIB-IDIOMATIC**, with optional support-reconstruction factoring before upstream submission. The proof chooses coefficient comparison and invertible substitution rather than repeating multivariate binomial induction. The bridge `coeff_taylor` is explicitly project mathematics, not counted as an existing mathlib call. No new development ticket/PR was opened in this survey.

## Phase 4.5 — six infrastructure risks

**n/a — theorem**, introducing no definition, instance or coercion. Individually: typeclass diamond n/a; reducibility leak n/a; noncanonical data unfolding n/a; instance-priority collision n/a; universe-polymorphism data construction n/a; coercion ambiguity n/a. The scoped-Classical restatement’s instance choice in its proposition is a real statement-transport check, verified separately; it is not swept under this theorem-kind exemption.

## Phase 5 — five-method exhaustive mathlib search

All methods were attempted on current, literature-standard and abstract reconstruction forms. [Complete formal requests/responses](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/formal-search.json).

| Method | Actual forms | Results and limits |
|---|---|---|
| Lean-Finder | Multivariate finite-box Hasse expansion; commutative-ring Hasse Taylor formula; inverse-shift coefficient reconstruction | `Polynomial.sum_taylor_eq`, `Polynomial.taylor_coeff`, `Polynomial.taylorEquiv`, `algEquivAevalXAddC_symm_apply`, generic coefficient/Finsupp isomorphisms. No exact arbitrary-variable Hasse box theorem. External indexv4.28 differs from the pin. |
| Loogle | `"taylor", "sum"`; `Polynomial.sum_taylor_eq`; abstract `MvPolynomial.aeval, MvPolynomial.sum` then corrected `MvPolynomial.aeval, "sum"` | First two find univariate `Polynomial.sum_taylor_eq`. First abstract query was rejected because MvPolynomial.sum is not an identifier; retry finds `MvPolynomial.aeval_sum`/sumElim, not reconstruction with Hasse coefficients. The failed query is retained, not hidden. |
| LeanSearch | Same three conceptual requests as Finder | Univariate Taylor coefficient/expansion and inverse-shift equivalences. No exact multivariate statement identified. |
| Source rg | Full untruncated name grep, current Taylor/sum patterns, literature Hasse patterns, abstract eval₂/coefficient reconstruction | [Current](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/rg-current.json), [literature](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/rg-literature.json), [abstract](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/rg-abstract.json), [full name](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/rg-full-name.json). No same-name mathlib declaration. Positive sources archived and hashed. |
| lean_local_search | `eq_sum_box_hasseDeriv`, `sum_taylor`, `sum_monomial` | Finds own theorem and univariate/generic reconstruction candidates through source fallback, but **index: unavailable** for all three. This is not an indexed absence proof. |

The pinned `Polynomial.sum_taylor_eq` at Taylor208 states reconstruction from the translated polynomial’s coefficient sum over a **CommRing**. Some Finder informal descriptions say “semiring” despite their returned formal signature saying CommRing: formal pinned type wins. `Polynomial.taylor_coeff` at68 identifies its univariate Hasse coefficients. Neither is a one-line specialization to arbitrary finitely many independent variables; iterating a univariate API requires new transport/coordinate bookkeeping and does not already prove this theorem.

`MvPolynomial.eval₂_eq` at Eval72 gives an arbitrary-variable support-product evaluation sum; `eval₂_eq'` at76 changes that to a full product under Fintype. `aeval_def` at572 connects algebra evaluation. These are genuine existing building blocks for inverse-shift reconstruction, but give translated coefficients, not their Hasse identity or coordinate-box padding. No parent re-aim rule changes this conclusion: even if Roth.box is replaced by standard interval infrastructure, no existing multivariate Taylor/Hasse expansion on that representation was found. [Pinned inputs](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/mathlib-inputs.json).

## Phase 5.5 — all statement-shape checks

**Normal form.** Equivalent presentations: coefficient identity `coeff_taylor`, support-indexed expansion after inverse translation, bounded coordinate-box polynomial identity here, and evaluated identity74. There is no existing complete pinned multivariate Hasse Taylor normal form discovered. Recommend coefficient identity as the foundational normal form; derive polynomial reconstruction and then evaluation. The present equality is a reconstruction rewrite with P on the LHS, not a simp rule; univariate `sum_taylor_eq` orients sum=P instead. Orientation should follow use: current direct caller applies congrArg then rewrites an evaluation. No symmetric pair of new simp rules is proposed.

**Syntactic generality.** Keep α/r/P explicit and hP pointwise, since the actual caller supplies these directly. Removing explicit DecidableEq is beneficial only with native verification that the box instance is transported correctly. Standard interval bounds are a prospective upstream representation, not a verified native signature in this package. A support-indexed expansion removes the supplied bound and Fintype requirement but becomes a separate theorem, not grounds for dropping assumptions from the existing displayed box.

**Superfluous assumptions.** Audit all: CommRing used by negation/subtraction; Fintype used by full-coordinate product and box; DecidableEq addressable by scoped Classical and tested transport; α/r/P are mathematical values; hP needed for this box. No nonzero, characteristic, ordered-field or positivity assumptions to remove. Overall **RESTATE-BEFORE-SHIP**: 1 explicit typeclass binder to remove, with scoped-Classical proposition and verified original-instance recovery.

## Phase 6.0 — exact callers, inline audit, duplication

| Direct caller | Location | Pattern and validation |
|---|---|---|
| `MvPolynomial.eval_eq_sum_box` | Roth/Taylor.lean220 (declaration starts217) | `simpa using congrArg (eval x) (eq_sum_box_hasseDeriv α r P hP)`; full fresh replay with the verified candidate and required instance bridge. |

**1 direct named caller, zero outside the declaring file.** Module-doc references and the declaration itself are excluded. `Roth.abs_eval_lt_of_le_index` at Main390 invokes **eval_eq_sum_box** and is a transitive mathematical application, not an extra direct reference to this theorem. The direct caller is more than an arbitrary single-use helper signal: it exposes exactly the expansion used for the main quantitative argument. [Callers](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/callers.json), [source search](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/rg-callers.json), [inline audit](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/rg-inline.json). This is explicit-source auditing, not an exhaustive repository-wide opaque kernel/simp dependency closure.

| Decl A | Decl B | Same statement? | Same proof? | Action |
|---|---|---|---|---|
| eq_sum_box_hasseDeriv | coeff_taylor | No: finite reconstruction versus individual coefficient law | Main proof uses it and vanishing/inverse transport | Keep coefficient theorem foundational; derive reconstruction. |
| eq_sum_box_hasseDeriv | eval_eq_sum_box | No: formal polynomial versus evaluated identity | Evaluation is congrArg corollary | Retain distinction; avoid duplicate binomial proof. |
| eq_sum_box_hasseDeriv | Polynomial.sum_taylor_eq | Same mathematical motif, different variable/index representation | Both inverse-shift transport; multivariate degree-box/Hasse work additional | Multivariate API is a genuine extension, not a direct existing-law specialization. |
| eq_sum_box_hasseDeriv | generic eval₂_eq' | No: inverse Taylor/Hasse reconstruction versus arbitrary evaluation coefficient sum | Generic sum is a definitional building block | Reuse evaluation sum, add substantive bridge. |
| eq_sum_box_hasseDeriv | Main.abs_eval_lt_of_le_index | No: exact expansion versus strict weighted estimate | Estimate consumes evaluated expansion | Not a duplication; retain algebra/analysis separation. |

Junk assessment: **KEEP**, substantive standard theorem with an actual path to the main application. No independently rederived exact full expansion was found. Other box sums count cardinalities, bound norms, or express Wronskian linear combinations and do not duplicate this theorem.

## Phase 6 — actual composition and native verification

Three accepted native sets all report complete success, partial=false, no errors/warnings or failed dependencies. All printed axioms are among propext, Classical.choice, Quot.sound. No sorry/admit/new axiom/unsafe/native_decide or raised resource limit is used in accepted sources.

- [Target source](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/native-target-executed.lean.txt), [receipt](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/native-target-success.json): original full type, original proof replay, scoped-Classical theorem without explicit DecidableEq, clean axiom checks.
- [Extra source](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/native-extra-executed.lean.txt), [receipt](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/native-extra-success.json): arbitrary original DecidableEq recovery using proof-irrelevance equality; full original evaluation caller and full caller without that binder. This certifies mathematical equivalence despite instance-dependent box data.
- [Isolated raw source](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/native-raw-executed.lean.txt), [receipt](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/native-raw-success.json): no Roth imports, missing-target guard, pinned univariate sum_taylor_eq type/print/application, and arbitrary-variable shifted-support reconstruction from independently proved inverse substitution and eval₂_eq/Finsupp.prod. **No Fintype** needed in this support representation; no Hasse coefficient or box-cutoff identity silently assumed.

Six rejected preparation attempts are archived separately in [verification inventory](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/verification.json): one target attempt lacked statement-level equality decision; three extra preparations failed at instance transport, and a fourth reported only a long-line style warning before the final accepted source; one raw preparation used Finsupp.sum instead of Finsupp.prod normalization. Their errors/possible recovered placeholders are not accepted proofs. No limits were raised to make them pass.

Composition attempt1: specialize `Polynomial.sum_taylor_eq`. The native univariate example succeeds, but its index is ℕ in Polynomial A rather than σ→₀ℕ in MvPolynomial σ A. A direct term cannot prove the multivariate bounded Hasse formula.

Composition attempt2: existing `MvPolynomial.eval₂_eq`/`eval₂_eq'` and inverse substitution reconstruct a polynomial using coefficients of its translate. The isolated mathlib-only experiment tests this generic support form; its coefficients have **not** yet been identified with eval α(hasseDeriv d P), and extending the support sum to an arbitrary degree box requires vanishing and finite-sum reasoning. These missing mathematical facts are project theorems, not≤3 existing mathlib calls. A theorem holding only after supplying the original desired coefficient formula as a hypothesis is not an existing replacement.

Composition attempt3: the actual project proof uses `coeff_taylor`, off-box derivative vanishing, inverse Taylor and monomial transport. It is a valid proof and replay, but cannot classify itself as a mathlib-only composition. Generic extensionality, map_sum, coefficient sums and Finsupp.prod_fintype perform structural transport around these substantive inputs.

**Conclusion: NOT-COMPOSABLE from ≤3 existing mathlib mathematical calls.** No failed search is used as an absolute absence proof. Exact full-name search, successful positive candidates, and isolated composition probes collectively bound the conclusion to the pinned mathlib environment.

## Phase 7 — actionable verdict

**YES-but-generalise-first — remove the explicit DecidableEq requirement.** The standard algebraic multivariate Taylor formula is genuinely useful outside Roth: it translates a collection of Hasse-derivative values into an exact polynomial expression, enabling multiplicity, interpolation and zero-estimate applications in every characteristic. Pinned mathlib has the univariate reconstruction theorem and generic evaluation sums but lacks the multivariate Hasse coefficient plus bounded-box bridge. A real native generic support expansion was tested, making the missing bridge explicit rather than inferred from search silence. The original proof is substantive and cannot be replaced by a 1–3-call term from existing mathlib.

The verified explicit-binder removal avoids requiring computational equality data for a classical mathematical identity. It retains the same mathematical conclusion and all substantive parameters. This does **not** mean the instance-dependent old and new terms are definitionally equal: the accepted propositional recovery and both full caller proofs are required evidence. This is a concrete generalise-first plan, not a cost-driven downgrade or an incomplete phase. The Fintype and CommRing assumptions remain in the proposed same-statement theorem; the separately verified arbitrary-variable support sum has a different range/product and does not authorize claiming their deletion here.

Proposed location: **Mathlib/Algebra/MvPolynomial/Taylor.lean**, alongside the already accepted coefficient/Hasse infrastructure. Proposed PR title: **feat(Algebra/MvPolynomial): finite Taylor expansion in Hasse derivatives**. Group with actual accepted YES declarations **MvPolynomial.coeff_taylor** and **MvPolynomial.degreeOf_taylor_le**, using **MvPolynomial.hasseDeriv** and **MvPolynomial.coeff_hasseDeriv** as foundation. Their actual current verdicts were checked in progress: [group evidence](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/proposed-pr-group.json). Do not group by useful names without their prior verdicts. If a named taylor surface is declined, its aeval spelling supports the same mathematical coefficient/reconstruction laws; the prior parent packaging BORDERLINE verdict does not erase this substantive theorem.

Before any upstream PR:

- Run `/generalise MvPolynomial.eq_sum_box_hasseDeriv` on the successful no-explicit-DecidableEq restatement, preserving the proved old-instance recovery.
- Use standard Finsupp interval/finite-box infrastructure rather than exporting Roth.box. The representation migration is a separate verified pre-PR task; no guessed native transport is claimed finished here.
- Run `/cleanup Mathlib/Algebra/MvPolynomial/Taylor.lean MvPolynomial.eq_sum_box_hasseDeriv` and required whole dependent/import, simplification and performance gates. These future submission checks are not falsely marked as done by this survey.
- Choose reviewers from actual recent history: **Yaël Dillies** (coefficient refactor631b214f7c) and **Aaron Liu** (Eval cleanup274ed6d67d) are evidence-based suggestions, with no availability promise. [Git history](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/reviewer-history.json). No external PR, message or reviewer request was sent.

Assessment complete, unresolved=[]; no required user input. Keep production unchanged during the survey. The root must independently accept this finished evidence before integrating and pushing it.

## Phase 8 — completion and evidence discipline

Production Lean, project structure, pins and existing local changes are untouched by the worker. All required literature, generality, idiom, strategy, source-search, actual composition and native evidence is incorporated and complete; independent root acceptance remains pending. The portable validator checks current manifest hashes/bytes, exact source/receipt pairing, source/pin consistency, standard axioms and complete nonpartial native success. It supports scratch and integrated layouts, and validates the **current** copy-manifest; worker-copy-manifest, if root preserves it, is historical only.

[Assessment](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/assessment.json), [verification inventory](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/verification.json), [validator](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/validate.py), [overview entry](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/overview-entry.json), [artifact manifest](../evidence/MvPolynomial.eq_sum_box_hasseDeriv/copy-manifest.json). No incomplete assessment is eligible for publication. Root alone performs independent acceptance, updates the tracked progress/overview, and commits/pushes the completed declaration.
