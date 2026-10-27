# Roth.index_le_card — full mathlibable assessment

**Verdict: BORDERLINE-needs-human.** The coordinate-degree cardinality estimate is standard, and its nonvanishing hypothesis is mechanically removable under the project's real-valued zero convention. Canonical `infDegree` already supplies the witness upper-bound law, but the full Taylor/coordinate-degree/cardinality estimate was not located as an existing library theorem. The remaining choice is which degree-bound API merits an upstream named specialization; all verification is complete and no user response is required for this read-only assessment.

## Phase 0 — Doctor

Public declaration150, `Roth/Index.lean:224`, theorem. [Canonical entry](../evidence/Roth.index_le_card/canonical-target.json). [Baseline build](../evidence/Roth.index_le_card/baseline-build.txt): exit0,2467jobs, no reported errors/warnings. All17 source/pin hashes freshly match the shared baseline manifest: [inputs](../evidence/Roth.index_le_card/inputs.json). Production files remain unchanged. The whole [Index module](../evidence/Roth.index_le_card/Roth-Index.lean.txt) and complete relevant caller declarations in [Theta](../evidence/Roth.index_le_card/Roth-Theta.lean.txt) were read. Index develops weighted orders at a point; Theta bounds suprema of such indices.

## Phase 1 — Comprehend

For a nonzero polynomial P in m variables, with degree in variable j at most rj, its weighted order of vanishing at every point is at most m. Translate P to the chosen point and choose a nonzero Taylor coefficient. Its exponent in each coordinate is at most the corresponding degree, hence each normalized exponent is at most1; their sum bounds the minimum.

Full native elaborated type:

```lean
Roth.index_le_card.{u_1} : ∀ {σ : Type u_1} [inst : Fintype σ]
  {P : MvPolynomial σ ℝ}, P ≠ 0 → ∀ {r : σ → ℕ},
  (∀ (j : σ), MvPolynomial.degreeOf j P ≤ r j) →
  ∀ (α : σ → ℝ), Roth.index P α r ≤ ↑(Fintype.card σ)
```

σ is the variable type; Fintype supplies both the rational-weight sum and cardinality. P has real coefficients; α is an arbitrary real point; r is any natural denominator vector. hP provides a nonzero coefficient; hd bounds all coordinate degrees. There is no positivity hypothesis on r: real division at zero is0. The theorem actually holds at P=0 too because this project's index0=0. The manuscript's +∞ convention does not permit that weakening.

The original proof obtains an attaining witness from `exists_weight_eq_index`, converts nonzero derivative evaluation to Taylor support using a private helper, applies `monomial_le_degreeOf`, then project-defined `MvPolynomial.degreeOf_taylor_le` and `Roth.weight_le_card`. Namespace alone does not make these last two mathlib lemmas. [Original exact source](../evidence/Roth.index_le_card/index-card-original-executed.lean.txt), [native full printer and audit](../evidence/Roth.index_le_card/index-card-original-audit-receipt.json). The entire kernel body was printed with no elision. Standard axioms only: propext, Classical.choice, Quot.sound. Fresh canonical audit checks293 requested/unique/present/value-bearing names and finds two direct consumers. This is distinct from lexical source enumeration.

## Phase 2 — Preliminary checks

SMALL: a degree estimate supporting Theta bounds, not a main named result or a new structure. One-line-definition test is n/a: theorem. Short proof length is not an exclusion criterion.

## Phase 3 — Exhaustive literature

Each named channel was actually checked, including three distinct general-web forms. Stored web artifacts contain exact requests, response SHA256/bytes/status, sanitized titles/URLs, and original concise summaries only: [general](../evidence/Roth.index_le_card/web-general.json), [labs/Stacks](../evidence/Roth.index_le_card/web-labs-stacks.json), [MO/recent arXiv](../evidence/Roth.index_le_card/web-mo-arxiv.json), [primary access/refinement](../evidence/Roth.index_le_card/web-primary.json).

| Channel | Actual request / locator | Finding |
|---|---|---|
| General specific | `Roth theorem polynomial index bounded number variables degrees r` | Min Ru's [Roth notes](https://www.math.uh.edu/~minru/fields/roth.pdf), p2, define normalized derivative minimum; coordinate degrees bound the possible exponent box. PDF inspected directly. |
| General abstract | `weighted order vanishing polynomial coordinate degree upper bound` | Taylor support and degree restrictions are the relevant standard abstraction; no single universal name for this cardinality corollary emerged. |
| General aliases | `Dyson lemma index polynomial sum i_j r_j` | Dyson/Roth index terminology; unrelated Dyson constant-term conjecture hits excluded. |
| ChatGPT math MCP | Standard form/generality/history | n/a: ask_chatgpt_math unavailable. |
| Local clean.tex | `ind\(|Index|index|Taylor|weight at most|at most.*m` | §4 defines index with positive REAL weights and zero+∞. §5 explicitly explains Θ≤m by a nonzero Taylor derivative with ij≤rj. [Search](../evidence/Roth.index_le_card/local-literature-search.json), [excerpt](../evidence/Roth.index_le_card/clean-index-excerpt.tex.txt). |
| nLab | `site:ncatlab.org/nlab weighted polynomial degree order vanishing` | Valuation/order context is adjacent. Direct valuation page failed400 unsupported XHTML; not claimed read. |
| nCatLab | `site:ncatlab.org/ncatlab weighted polynomial degree` | Explicit distinct namespace checked; no exact categorical cardinality law located. Off-namespace hits do not count as a nCatLab publication. |
| Stacks | `site:stacks.math.columbia.edu order vanishing polynomial degree` | [02MB](https://stacks.math.columbia.edu/tag/02MB), Definition10.121.2, directly inspected: order via local-ring lengths. Adjacent geometric order, not this normalized multivariate estimate. |
| MathOverflow | `site:mathoverflow.net Roth theorem index polynomial` | Diophantine/Roth discussions and high-order vanishing context; no exact replacement. Additive-combinatorial Roth hits excluded. |
| Recent arXiv | Initial2022–2026 Roth/weighted query, refined `site:arxiv.org/abs/ "monomial valuations" "Taylor" after:2021-10-27` | [Dutta–Ghosh2609.03451](https://arxiv.org/abs/2609.03451), submitted2026-09-03, abstract relates monomial valuations and Taylor expansions. Adjacent, not a proof of the cardinality estimate. Medical Roth-name and additive-combinatorics results rejected. Window2021-10-27–2026-10-27. |

Synthesis: weighted Taylor order is standard. More generally, an order is bounded by the weight of any nonzero coefficient; a coordinate box bounds every coefficient weight by the sum of its normalized widths. Natural denominators and real coefficients are specializations. Dropping nonvanishing is specific to projecting the empty-support value to0, not a literature assertion with +∞.

## Phase 4a — Parameter and hypothesis audit

| Parameter | Role | Generality / actual evidence |
|---|---|---|
| σ : Type u | arbitrary variable universe | Already universe-polymorphic. Finite cardinal conclusion presumes finite σ. |
| Fintype σ | sum and m | Fixed parent interface requires it. A generic finite-support witness law needs no finite variable type; exact isolated infDegreeWitness verifies this. |
| ℝ coefficients | Taylor support and degree | Expanded realSupport is entirely independent of coefficients; infDegreeWitness works for any Semiring coefficient. A polynomial Taylor version needs CommSemiring. These are expanded representations, not a silently weakened Roth.index signature. |
| P | polynomial input | hP removable in this interface, independently verified by original argument plus P=0 case; no invocation of index_le_card. |
| hP : P≠0 | original attaining witness | Dropped in noNonzero. Essential again if retaining +∞ at zero, as explicit guard verifies. |
| r : σ→ℕ | denominators | May contain zeros; no hr needed. Literature permits positive real widths; no such signature change claimed compiled here. |
| hd : ∀j,degreeOf j P≤rj | entire degree box | Weakened to existence of ONE nonzero Taylor coefficient within the box in oneWitness; further to a single weighted coefficient bound by arbitrary c in weightedWitness. These actual probes compile. Removing all degree/weight control is false: one-variable X² at0 with r=1 has index2>card1. |
| α : σ→ℝ | arbitrary center | No nonvanishing/positivity/rationality condition. Translation changes coefficients while not increasing coordinate degrees. |
| ℝ target | real default0 | Canonical WithTop infDegree retains∞. Real default0 empty-support upper bounds require a nonnegative proposed bound; card satisfies this. Generic negative-c claim without a witness is false and tested. |

## Phase 4b — Verified generality

STRICTLY NARROWER in its hP hypothesis. Verified current-parent restatement:

```lean
{σ : Type*} → [Fintype σ] → {P : MvPolynomial σ ℝ} → {r : σ → ℕ} →
(∀ j, MvPolynomial.degreeOf j P ≤ r j) →
∀ α, Roth.index P α r ≤ Fintype.card σ
```

[Exact noncircular weakening and witness forms](../evidence/Roth.index_le_card/index-card-target-executed.lean.txt), [clean native receipt](../evidence/Roth.index_le_card/index-card-target-receipt.json). Nonzero branch reproduces the original support argument independently, and zero branch unfolds the parent. `oneWitness` proves the stronger support-witness statement; `weightedWitness` proves arbitrary upper bound from one nonzero coefficient. This is real mechanical evidence, not an unused-syntax guess. It does not alone force YES: the canonical witness law already exists, and the upstream value of packaging coordinate-degree/cardinality specialization remains an API question. No verdict is based on arithmetic proof cost.

## Phase 4c — Nine modern-idiom rows

| # | Question | Answer / downstream effect |
|---|---|---|
| 1 | Preambles to typeclasses | No new class: existing Fintype/order/semiring structures suffice. hP and hd are data-specific propositions. |
| 2 | Sequences to filters | No topology or convergence. |
| 3 | Construction to universal property | No new construction. Translation uses the existing free polynomial algebra interface. |
| 4 | Sets to bundled substructures | A degree restriction could be a polynomial submodule, but this inequality consumes a coordinate box directly; no closure predicate to replace. |
| 5 | Field-specific to semiring | Expanded support estimate ignores coefficients; infDegreeWitness is verified over Semiring. Current index fixes ℝ. |
| 6 | Higher categories | No categorical structure in a scalar upper bound. |
| 7 | Concrete numeric index to ordered structure | Canonical infDegree permits SemilatticeInf+OrderTop and arbitrary grading; verified generic witness law has no σ/Fintype or real coefficients. Coordinate-card estimate still needs numeric sum structure. |
| 8 | Concrete-via-abstract diagnostic | Fires: after obtaining d the original final expression only uses hdw, support/degree and weight_le_card. No special property of P beyond degree-controlled Taylor support remains; α appears only through degreeOf_taylor_le. Generic realSupport accepts any finite exponent support. |
| 9 | False-generalization guard | Keep ∞ at empty support unless deliberately projecting it. Dropping hP in unprojected infDegree is false. Do not discard degree bounds: X² counterexample. A mere infDegreeWitness is weaker than the full polynomial/cardinality theorem and is not passed off as its exact replacement. |

Modern form: support-minimum upper bounds via infDegree plus separate degree-envelope estimate. This organizes the actual dependencies and reuses the canonical parent. Larger coefficient/weight expansions are distinguished from the single mechanically verified hP deletion.

## Phase 4.5 — Infrastructure risks

n/a: theorem introduces no definitional equality, instance, priority, universe constraint, or coercion. All six rows assessed: typeclass diamond, reducibility leak, noncanonical unfolding, instance-priority collision, universe polymorphism, coercion ambiguity. None applies to adding a proposition proof; the chosen parent representation is an API concern, not a new instance risk.

## Phase 4.6 — Five proof-strategy rows

| # | Question | Assessment |
|---|---|---|
| 1 | ε–δ to filters | n/a, finite polynomial estimate. |
| 2 | Element algebra to substructure inclusion | Witness selection is appropriate for an upper bound on a minimum. Restrict-degree submodule inclusion would add detours. |
| 3 | Sequences to nets | n/a, no analysis limit. |
| 4 | Construction to universal property | n/a, no categorical construction. |
| 5 | Missing helpers mathlib SHOULD have | Candidate reusable package: Taylor translation preserving coordinate-degree restrictions, then support-box weighted minimum bound. Generic infDegreeWitness already exists as Finset.inf_le. Whether cardinality deserves a named theorem is the remaining question. |

Strategy: REFACTOR-RECOMMENDED for future upstream API: use one support witness rather than an attaining-minimum witness, and keep coordinate-envelope arithmetic separate. The original mathematics is sound. No difficulty/cost argument changes the verdict.

## Phase 5 — Five actual mathlib methods

[Complete raw formal search requests and receipts](../evidence/Roth.index_le_card/formal-search.json) run all four services on each of current, literature-standard and abstract forms. [Current rg](../evidence/Roth.index_le_card/rg-current.json), [literature rg](../evidence/Roth.index_le_card/rg-literature.json), [abstract rg](../evidence/Roth.index_le_card/rg-abstract.json) complete the fifth method.

| Method | Current form | Literature / abstract forms |
|---|---|---|
| Finder | Index bounded by variable count | Weighted order/coordinate degree and finite-support infimum queries; degree bounds and le_weightedTotalDegree partial matches. |
| Loogle | `MvPolynomial.degreeOf, _ ≤ _` | `AddMonoidAlgebra.infDegree, _ ≤ _`; `Finset.inf_le` gives exact generic witness law. |
| LeanSearch | Polynomial index upper-card bound | Weighted-order and finite-support-weight upper bound; `monomial_le_degreeOf`, `Finset.inf'_le` and weight/degree lemmas. |
| rg | index_le_card and Taylor-degree patterns | weightedOrder, weightedTotalDegree and infDegree/support patterns in pinned source. |
| local | index_le_card | weightedOrder; inf_le. Source hits returned but index unavailable; empty results never certify absence. |

Pinned candidates actually checked in isolated native Lean: `MvPolynomial.monomial_le_degreeOf`, `Finset.sum_le_sum`, `div_le_one_of_le₀`, `Finset.inf_le`, `csInf_le`. Exact generic proof `infDegreeWitness := Finset.inf_le hd` verifies existing analogous witness law on the canonical parent. [Mathlib-only source](../evidence/Roth.index_le_card/index-card-mathlib-executed.lean.txt), [clean receipt](../evidence/Roth.index_le_card/index-card-mathlib-receipt.json). `#check_failure Roth.index_le_card` verifies isolation. External indexes can differ from this pin. A partial weightedTotalDegree hit does not supply Taylor control or the order/cardinality conclusion.

## Phase 5.5 — Three statement-shape checks

1. Normal form: project real sInf, canonical infDegree in WithTop, and MvPowerSeries weightedOrder divided by product weights are possible representations. The canonical finite-support minimum is infDegree. Its top value must not be identified with real0 definitionally; no such false bridge is claimed.
2. Syntactic generality: degreeOf-based bound is easy for both callers, whose RSet membership already supplies it. Witness-based bound is mathematically weaker but forces callers to manufacture a support witness. Keep the degree-bound wrapper locally while choosing upstream API; hP can be dropped immediately in any future local cleanup.
3. Superfluous assumptions: hP removable; no DecidableEq required; Fintype required by current weight/card interface; α and hd carry genuine point/degree data; real coefficients fixed by parent. Full caller replay specifically removes an accidental scratch DecidableEq parameter to match the original omit signature.

Overall RESTATE-BEFORE-SHIP: remove hP under current real default0 convention, or retain it with canonical∞. Both options require explicit zero semantics.

## Phase 6.0 — Complete call-site and inline audit

[rg --no-ignore and git grep](../evidence/Roth.index_le_card/complete-caller-search.json), [canonical-source lexical enumeration](../evidence/Roth.index_le_card/lexical-enumeration.json), [caller plans](../evidence/Roth.index_le_card/callers.json). Exactly two proof applications, no statement applications: indexSet_bddAbove at Theta91 and Θ_le_card at Theta117. Both occur in complete arguments bounding mapped integer-polynomial indices from mapped degree bounds. Fresh canonical direct kernel consumers are exactly those two public declarations; no claim about transitive/simp closure follows.

| Caller | Full replay | Prospective change |
|---|---|---|
| indexSet_bddAbove | bddAboveReplay | Replace target by noNonzero; discard map-injective nonzero proof; retain map degree proof. |
| Θ_le_card | cardReplay | Same substitution inside Real.sSup_le; maintain nonnegative cardinal upper bound. |

[Both exact full caller proofs](../evidence/Roth.index_le_card/index-card-callers-clean-executed.lean.txt), [clean receipt](../evidence/Roth.index_le_card/index-card-callers-clean-receipt.json). Initial scratch attempt unnecessarily inherited DecidableEq and produced linter warnings; archived separately as rejected, not accepted proof evidence. [Inline audit](../evidence/Roth.index_le_card/rg-inline.json) locates the same degree/weight pattern in the target and these cardinality callers; no second independent inline proof of the full target was found. Zero explicit references would not establish dead simp API; here the actual two uses already establish local usefulness.

## Phase 6 — Actual composition and guards

Mathlib-only realSupport proves, for ANY finite exponent set inside the coordinate box, its real weighted-support minimum is at most card. It splits empty/nonempty support, selects a witness, uses csInf_le plus finite-image boundedness, then sum_le_sum/div_le_one_of_le₀ and finite-sum normalization. This is a new helper proof, not an existing replacement theorem; counting its name as one mathlib call would be dishonest. Its proof is preserved exactly in the native source cited above.

The normalized witness upper-bound is literally existing Finset.inf_le (one call) and an arbitrary further bound uses trans. This only settles the witness component; original hd must still travel through polynomial Taylor degree control and coordinate quotients. Project `exists_weight_eq_index`, `degreeOf_taylor_le` and `weight_le_card` do not count as mathlib building blocks. No ≤3-existing-call proof of the full original statement was verified. The proof does not establish that no such proof exists. A closing `simp [defs]` would in any case need the Phase6b BORDERLINE treatment, not automatic NO.

[Guard source](../evidence/Roth.index_le_card/index-card-guards-clean-executed.lean.txt), [native receipt](../evidence/Roth.index_le_card/index-card-guards-clean-receipt.json): zero P, zero r, exact one-variable degree counterexample, infinity-at-zero counterexample, and negative upper bound for empty real support. The zeroWeights guard uses the already independently proved `IndexScale148.zeroScale` boundary (with `Nat.zero_mul` normalization); that earlier proof remains in the full executed disk source. It does not call index_le_card. These preserve the distinction between a genuine hP deletion and a false infinity-valued generalization.

## Phase 7 — Actionable verdict

BORDERLINE-needs-human is an upstream API/audience choice, not an unresolved proof and not a cost downgrade. The parent definition was assessed NO-mathlib-has-it because infDegree is more general. Its analogous witness law is independently verified here, so that COMPONENT is NO-mathlib-has-it under re-aim. The FULL degree/cardinality conclusion was not found under that parent and must not inherit NO merely because one component exists. Conversely, verified hP deletion alone does not justify a new public library theorem packaging a specialized degree estimate.

Concrete future upstream questions:

1. Should the normalized coordinate-box upper bound be a public polynomial degree theorem, or stay as a Roth-local corollary of support-witness bounds?
2. Should an upstream theorem retain WithTop∞ at zero and require P≠0, with the real default0 version only a local projection?
3. Should this be grouped with a reusable Taylor degree-preservation theorem and the coordinate weight/cardinality API proposed for weight_le_card, or should callers use the generic finite-support envelope directly?

Local destination: retain Roth/Index.lean while the parent/Taylor API is settled. A future cleanup can remove hP and replace both callers by the verified noNonzero shape. This assessment authorizes no production edit. Potential upstream home, if question1 is yes: a Taylor/translation degree file under Mathlib/Algebra/MvPolynomial/ together with the Taylor API; foundational Degree.lean alone cannot import project translation machinery. This is a conditional design location, not a submitted PR or an accepted YES grouping.

## Phase 8 — Evidence and completion

All mandatory phases are complete; verification unresolved[] is empty. [Verification index](../evidence/Roth.index_le_card/verification.json), [assessment](../evidence/Roth.index_le_card/assessment.json), [overview](../evidence/Roth.index_le_card/overview-entry.json), [portable validator](../evidence/Roth.index_le_card/validate.py), [manifest](../evidence/Roth.index_le_card/copy-manifest.json). The validator checks fresh17 input hashes, current manifest hashes/bytes, exact canonical293 array/order, clean accepted native success, standard axioms, both full caller replays, all search channels and portable links. Raw native full diagnostics remain intact; new-region markers scope target-specific claims. Rejected scratch attempts are explicitly segregated. Root acceptance remains pending until independent review.
