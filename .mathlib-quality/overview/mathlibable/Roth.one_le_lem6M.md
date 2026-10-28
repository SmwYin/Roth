# Full mathlibable assessment — `Roth.one_le_lem6M`

Canonical200 of293; `Roth/Theta.lean:279`. **BORDERLINE-needs-human**. Completed read-only assessment; verification unresolved[]; root acceptance pending. This is a useful local certificate for an explicit coefficient envelope. Its arithmetic is existing mathlib, but the actual old-form proof is not a verified ≤3-existing-call term. The remaining judgment is whether this envelope should be named upstream alongside Roth's index infrastructure.

## Phase 0 — baseline and integrity

Reused successful `lake build` (2467 jobs, exit0, no warnings/errors), with all17 source/pin SHA256 values freshly matched: [baseline](../evidence/Roth.one_le_lem6M/baseline-build.txt), [fresh hashes](../evidence/Roth.one_le_lem6M/source-hashes.json), [input manifest](../evidence/Roth.one_le_lem6M/input-manifest.json). No production source, pin, Git or overview record changed.

The target resolves as a theorem with standard axioms `propext`, `Classical.choice`, `Quot.sound`. A fresh target-specific native audit loaded every canonical293 declaration and all293 values, exact order and uniqueness, finding one direct kernel-value consumer and zero direct kernel-type consumers. The source was derived by splitting outside the canonical array, never replacing names inside it. Pre-execution `check_audit_source.py` passed for all disk sources; [fresh gate receipts](../evidence/Roth.one_le_lem6M/canonical-gates.json) repeat the gate independently. See [original source](../evidence/Roth.one_le_lem6M/onelem6m200-original-executed.lean.txt), [complete raw receipt](../evidence/Roth.one_le_lem6M/onelem6m200-original-receipt.json), [canonical snapshot](../evidence/Roth.one_le_lem6M/canonical-snapshot.json).

## Phase 1 — comprehend statement and complete context

Full native type (no elided binders):

```lean
∀ (p r₁ : ℕ) {B : ℝ}, 1 ≤ B → ∀ (l : ℕ), 1 ≤ Roth.lem6M p r₁ B l
```

The quantity is `((r₁:ℝ)+1)^(p*l) * l.factorial * B^l * 2^(p*l*r₁)`. The proof lower-bounds its four factors by one, then assembles them with three multiplication inequalities. The first factor uses natural-cast nonnegativity, the second factorial positivity transported through natural casts, the third hB, the fourth the numeral inequality1≤2. All exponents are natural; zero values require no case split.

The complete985-line declaring module was read and archived as [source](../evidence/Roth.one_le_lem6M/source-Theta.lean.txt). It develops degree/coefficient-bounded polynomial families, their supremal indices, the one-variable bound, the induction bound and the final Lemma7 estimate. The target's single explicit caller `theta_phi_lt_aux` uses it to certify the intermediate bound `M≥1`, which feeds the one-variable and prefix estimates. The declaration has no σ/τ/Fintype/DecidableEq binder despite its surrounding sections. Its only project dependency is the definition `Roth.lem6M`. [Native type](../evidence/Roth.one_le_lem6M/native-type.json).

## Phase 2 — size and one-line gate

SMALL: an eight-line elementary order proof. This does not narrow the literature protocol. Definition-only one-line test is **n/a — theorem**, with no definitional-equality/diamond exemption needed. It is not `rfl`, a direct alias, or a one-call theorem. A single tactic invocation would not make its generated arithmetic a single existing theorem call. The parent constant's zero theorem-call construction count is unrelated to this theorem's actual call count.

## Phase 3 — exhaustive literature

Every named channel was actually attempted; optional ChatGPT mathematical MCP is unavailable. Web records retain exact requests, response SHA256/bytes/status, titles/URLs/locators and concise original summaries, without article or result bodies: [general queries](../evidence/Roth.one_le_lem6M/web-0.json), [nLab/nCatLab/Stacks](../evidence/Roth.one_le_lem6M/web-1.json), [MO/recent arXiv](../evidence/Roth.one_le_lem6M/web-2.json), [targeted retry/direct access](../evidence/Roth.one_le_lem6M/web-3.json), [primary attempts](../evidence/Roth.one_le_lem6M/web-4.json).

| Channel | Actual query / locator | Finding and limitation |
|---|---|---|
| General web specific | `Roth theorem auxiliary constant "(r" "factorial" "Lemma 6"` | Coefficient-bound context; no separately named unit lower-bound theorem located. |
| General web abstract | `ordered monoid product elements greater than one natural powers inequality` | Order-compatible multiplication explains generic closure. |
| General web aliases/context | `Roth lemma 6 coefficient bound M l factorial B 2` | Roth1958 exposition and textbook coefficient-bound passages surfaced. Third-party book mirrors are discovery locators, not relied on as primary theorem sources. |
| ChatGPT mathematical MCP | Standard form, generality, historical evolution | n/a: `ask_chatgpt_math` unavailable; no invented response. |
| Local reference | `clean.tex`, §5 Lemma `roth:lem6`, Eq`roth:eq16`,704–759 | Exact formula M; coefficients bounded through determinant/degree estimates. The unit lower bound is a routine consequence, rather than a separate named statement. [Hash/locator](../evidence/Roth.one_le_lem6M/local-literature.json), [excerpt](../evidence/Roth.one_le_lem6M/clean-lemma6-excerpt.tex.txt). |
| nLab | `site:ncatlab.org/nlab ordered monoid multiplication monotone` | Ordered-group page remark describes ordered monoids; general structure, not Roth endpoint. Direct ordered-monoid URL inaccessible; direct ordered-group open rejected XHTML. Search response still supplied the structural passage. |
| nCatLab distinct namespace | `site:ncatlab.org/ncatlab ordered monoid positive product`; retry exact `"ordered monoid"` | Results returned nLab/out-of-namespace material. No exact nCatLab endpoint identified; this is not a proof of absence. |
| Stacks | `site:stacks.math.columbia.edu ordered ring positive product factorial` | No exact relevant endpoint located. Direct tag09DW access succeeded but is Galois theory and irrelevant; explicitly excluded as support. |
| MathOverflow | `site:mathoverflow.net Roth theorem auxiliary polynomial coefficient bounds factorial` | Coefficient-factor bounds and Diophantine Roth discussions, with additive-combinatorial collisions. No exact elementary endpoint found. |
| Recent arXiv | `site:arxiv.org Roth theorem formalization auxiliary polynomial after:2021-10-27 before:2026-10-28`; exact `"Formalizing Roth"` retry | Explicit last-five-year window. Mostly additive-combinatorial Roth results and an unrelated history paper; no exact endpoint located. |
| Supplementary primary attempts | Roth ICM1958; official mathlib docs | Original proceedings PDF fetch blocked at74MB; official mathlib order-arithmetic docs accessible. Pinned local source/native checks determine exact API. |

Primary locators: [Roth1958 ICM proceedings](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf), [nLab ordered group](https://ncatlab.org/nlab/show/ordered%2Bgroup), [official mathlib arithmetic](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/GroupWithZero/Basic.html). Access failures are recorded, not silently treated as successful full-text reads.

Concept: a product lower bound in an ordered multiplicative structure, specialized to a proof-specific coefficient envelope. Most general abstract standard form: if every factor is at least the unit, so is a finite product; natural powers preserve that lower bound. Literature varies in whether multiplication is globally monotone or only on nonnegative elements. The old-form M formula is an analytic bookkeeping choice, not an independent general order law. No historical evidence suggests a new higher-level replacement for this elementary inequality.

## Phase 4a — all parameters and hypotheses

| Parameter | Current role | Generality assessment |
|---|---|---|
| p:ℕ | exponent multiplicity | Zero already allowed; arbitrary natural p is broader than source p≥2. No positivity assumption to drop. |
| r₁:ℕ | base r₁+1 and exponent | Zero already allowed. Abstracting this to a nonnegative scalar base/exponent changes factorial/exponent representation; arbitrary real exponents would require separate rpow API, not the same object. |
| B:ℝ | coefficient-height base | Expanded formula compiles over `Semiring K`, `PartialOrder K`, `IsOrderedRing K`; real parent interface is fixed. |
| hB:1≤B | lower bound on B^l | Can weaken to1≤B^l for a fixed l, verified. Cannot uniformly remove: p=r₁=0,l1,B0 makes product0. |
| l:ℕ | factorial and powers | Zero already allowed; native zeroExponent proves value1 for every B. Factorial requires a natural parameter. |
| implicit instances/universes | none | Full native target type has no ambient finite-variable or decidable-equality instances. |

## Phase 4b — verified generality verdict

At the fixed named real parent interface, no unused typeclass or parameter can be deleted. There is one verified hypothesis weakening (`powerPremise`:1≤B^l) and a verified expanded scalar generalization (`genericWeak`, weakening the initially checked `genericScalar`):

```lean
{K : Type*} [Semiring K] [PartialOrder K] [IsOrderedRing K]
(p r : ℕ) {B : K} (hB : 1 ≤ B) (l : ℕ) :
1 ≤ ((r : K) + 1) ^ (p * l) * l.factorial * B ^ l * 2 ^ (p * l * r)
```

The initial stronger variant and hypothesis weakening compile cleanly in the [isolated source](../evidence/Roth.one_le_lem6M/onelem6m200-isolated-executed.lean.txt) and [receipt](../evidence/Roth.one_le_lem6M/onelem6m200-isolated-receipt.json), with no Roth imports. The further weak-order variant compiles in [weak source](../evidence/Roth.one_le_lem6M/onelem6m200-weak-executed.lean.txt) / [receipt](../evidence/Roth.one_le_lem6M/onelem6m200-weak-receipt.json), using Nat.mono_cast rather than characteristic-zero order reflection, with no strictness, linearity, CharZero or commutativity assumption. This is an expanded representation, not a mechanical weakening of the existing real-valued `lem6M` constant. No generalise-first claim is inferred from it. Existing abstract product/power laws already express the reusable order content. The more local exponent premise may be less convenient at the actual caller, which already has B≥1 from a real-power bound. This is an API judgment, not a cost downgrade.

## Phase 4c — modern idiom, all nine rows

| # | Question | Answer / concrete consequence |
|---|---|---|
| 1 | Preambles to typeclasses | No extra preambles. Scalar variant uses existing algebra/order classes; no new class needed. |
| 2 | Sequences/metrics to filters | No: finite scalar inequality with no convergence. |
| 3 | Construction to universal property | No: proving a bound, not constructing an initial/universal object. |
| 4 | Sets to bundled substructures | No set closure in target; an upper cone/submonoid could package factors but already available product laws suffice. |
| 5 | Field-specific to semiring/module | Yes for expanded formula: genericWeak needs no division/subtraction/commutativity/linearity/strictness. Enables same bound over natural/rational/ordered-semiring scalars. Parent M remains real. |
| 6 | Higher-category formulation | No: no categorical structure or downstream categorical consumer. |
| 7 | Concrete indices to ordered structures | Natural p,r₁,l occur as exponents/factorial, not just an arbitrary ordered index. Finite factor families generalize via existing List/Finset products. |
| 8 | Concrete-via-abstract | **Fires:** after `rw [lem6M]`, zero occurrences of lem6M. The body uses factor≥1 facts only. `List.one_le_prod` already supplies abstract closure; actual four factors and their proofs are instantiated in listReal. |
| 9 | False-generalization guard | Scalar formula preserves original upon K=ℝ. Replacing M by an arbitrary product with its factor hypotheses *supplied* is only an abstraction schema: it must not be advertised as the whole original result without those factor proofs. Globally monotone multiplication cannot be assumed on all ℝ because negative multipliers reverse order; zero-aware `PosMulMono` handles the needed nonnegative factors. |

Modern idiom available: yes, and already in mathlib. Genuine improvement is reuse of ordered product/power API, not a new generalized envelope theorem. Concrete downstream: `List.one_le_prod`, `Finset.one_le_prod₀`, `one_le_pow₀` support variable numbers of factors, zero exponents and nonnegative ordered multiplication. No new category-theoretic or abstract API proposal follows.

## Phase 4.5 — infrastructure

n/a — declaration kind is theorem. It introduces no data definition, instance, coercion or reducibility setting. All six infrastructure concerns (diamond, reducibility leak, noncanonical unfolding, instance priority, universe-polymorphism path, coercion ambiguity) are n/a for this theorem; assessment of parent `lem6M` is separate.

## Phase 4.6 — proof strategy, all five rows

| # | Diagnostic | Answer |
|---|---|---|
| 1 | ε-δ versus filters | n/a: no topology. |
| 2 | Element arguments versus substructures | No ideal/submodule argument; finite scalar product laws are direct. |
| 3 | Sequences versus nets | n/a: no limits. |
| 4 | Construction versus universal property | n/a: no categorical construction. |
| 5 | Missing helpers mathlib should have | No missing elementary law: all multiplication, power, factorial/cast bounds verified. A fresh helper for these four fixed factors would merely name the same local arithmetic. |

Strategy verdict: **MATHLIB-IDIOMATIC**. The direct existing ordered arithmetic is appropriate. A list-product presentation verifies the abstraction but adds finite-list normalization and still proves all four factor obligations. No proof-length gain or new missing generic theorem was demonstrated. A shorter tactic proof would require honest generated-call accounting.

## Phase 5 — all five actual mathlib methods on three forms

Exact requests/raw receipts: search-0 through search-11; source rg receipts for each form. The search cells are available through [first search](../evidence/Roth.one_le_lem6M/search-0.json), [search manifest](../evidence/Roth.one_le_lem6M/verification.json) and the package manifest. All twelve formal calls returned; local index reported warming rather than a reliable global absence index. External services may index revisions different from this pin.

| Method | Current formula | Literature-standard powers/product | Abstract order form |
|---|---|---|---|
| Finder | Roth formula query returned unrelated additive-combinatorial Roth bounds | Finite product query located List/Finset/Fintype/finprod lower bounds | Ordered-monoid query located one_le_pow₀ and related laws |
| Loogle | `1 ≤ (_ : ℝ)^_ * _ * _^_ * _^_`: no items | `1 ≤ ?a → 1 ≤ ?a^?n`: one_le_pow₀ | `1 ≤ ?a → 1 ≤ ?b → 1 ≤ ?a*?b`: one_le_mul and zero-aware law |
| LeanSearch | Formula query: additive-combinatorial collisions | Finite product lower-bound laws | one_le_pow₀ and one_le_mul_of_one_le_of_one_le |
| rg pinned source | No Roth-named endpoint; elementary factorial/cast patterns | Power and factorial laws | List/Finset product and multiplication laws |
| local | Current project target only | Power API, unrelated polynomial denominator/height results | List/Finset product bounds; index warming caveat |

Pinned positive signatures and proofs checked in the isolated run: `one_le_mul_of_one_le_of_one_le`, `one_le_pow₀`, `List.one_le_prod`, `Finset.one_le_prod₀`, `Nat.factorial_pos`, `Nat.cast_le`. [Pinned source hashes/archives](../evidence/Roth.one_le_lem6M/mathlib-inputs.json); [current rg](../evidence/Roth.one_le_lem6M/rg-current.json), [standard rg](../evidence/Roth.one_le_lem6M/rg-standard.json), [abstract rg](../evidence/Roth.one_le_lem6M/rg-abstract.json).

Conclusion: found all elementary building blocks and the more general abstract product law. No exact full old-form named theorem identified. This is a scoped search conclusion, not a proof of global absence. The abstract list theorem does not automatically certify that the concrete formula is a one-call specialization: its premise still requires four actual inequalities.

## Phase 5.5 — statement shape

Normal forms: `1≤lem6M...`, expanded left-associated multiplication, or a finite-list product. Existing mathlib uses `1≤x^n` and `1≤∏...` as generic bounds. The target uses the named local M normal form, appropriate for downstream Θ hypotheses. RHS convention is respected by `1≤M`; no orthogonal equivalence lemma is proposed.

Syntactic generality attempts: expanded generic scalar formula, actual list representation, exponent-local premise. All compile. Fixed statement easiest for sole caller because M is already let-bound and1≤B supplied by `Real.one_le_rpow`. Superfluous audit: p/r₁/l each enters expression; B enters B^l; hB is essential uniformly; no implicit finite-variable instances. Zero-exponent degeneracy does not make hB superfluous for all l.

Statement-shape verdict: normal form OK, syntactic generality OK, superfluous arguments NONE, **SHIP-AS-STATED locally**. This is not an upstream YES recommendation.

## Phase 6.0 — complete callers and inline audit

[git grep](../evidence/Roth.one_le_lem6M/callers.json) and [rg --no-ignore](../evidence/Roth.one_le_lem6M/inventory-callers.json) agree, cross-checked with all293 canonical declarations by fresh [lexical enumeration](../evidence/Roth.one_le_lem6M/lexical-enumeration.json). One explicit body occurrence, one distinct caller, zero external-to-declaring-file callers. The command's excluding-declaring-file count is0; same-file body uses are separately1.

| Caller | Use / actionable inlining option |
|---|---|
| `Roth.theta_phi_lt_aux`, declaration840, call866 | `have hM1 : 1 ≤ M := one_le_lem6M _ _ (Real.one_le_rpow ... ) l`. Replace this invocation by a local proof unfolding lem6M; establish r₁+1≥1, factorial≥1, B^l≥1 from the existing real-power bound, 2^...≥1; combine with existing multiplication laws. Complete unchanged caller proof with independently reproved bound was executed successfully. |

The canonical audit independently finds `_private.Roth.Theta.0.Roth.theta_phi_lt_aux` as the sole direct value consumer and no direct type consumer. These are direct constant references, not a transitive/simp dependency closure. [Inline search](../evidence/Roth.one_le_lem6M/inline-search.json) found no independent full-form duplicate; related generic M≥1 hypotheses downstream are consumers, not derivations. [Detailed comparison/call accounting](../evidence/Roth.one_le_lem6M/inline-audit.json).

## Phase 6 — actual composition experiments

1. `directReal` proves the exact expanded formula with mathlib only: three `one_le_mul_of_one_le_of_one_le` calls, three `one_le_pow₀` calls, factorial positivity, casts, additive and numeral bounds. This is a real elementary proof, **more than three calls**.
2. `listReal` instantiates `List.one_le_prod` with all actual factors. It separately supplies the r₁+1 power, cast factorial, B power and2 power inequalities; it explicitly normalizes List.prod and associativity. No factor hypothesis is assumed without proof. `abstractProduct` alone is a one-call existing-law specialization, and is clearly distinguished from the complete formula proof.
3. `powerPremise` verifies weaker1≤B^l; `genericScalar` verifies an expanded ordered-semiring form and `genericWeak` removes its linearity/strictness through Nat.mono_cast; `zeroExponent` and `baseAssumptionNecessary` are certified guards. No custom axiom, admitted proof, raised limits or project theorem is used in accepted isolated evidence.
4. [Complete caller source](../evidence/Roth.one_le_lem6M/onelem6m200-fullcaller-executed.lean.txt) / [receipt](../evidence/Roth.one_le_lem6M/onelem6m200-fullcaller-receipt.json) replay the entire original private caller after replacing its target call with independently reproved `OneLem6M200Project.bound`. Private upstream helpers are referenced by explicit term elaborators returning their actual constants, introducing no axioms.
5. [Full-module source](../evidence/Roth.one_le_lem6M/onelem6m200-fullmodule-executed.lean.txt) / [receipt](../evidence/Roth.one_le_lem6M/onelem6m200-fullmodule-receipt.json) replay every declaration of Theta in a fresh namespace, through final Θ_lt, cleanly. This is stronger than checking a detached two-line use and preserves the full module body.

Conclusion: **No ≤3-existing-mathlib-call proof of the full actual formula was verified**. No exhaustive impossibility of a shorter proof is claimed. No closing simp/tactic or a newly created helper is counted as one existing block. More-than-three elementary calls alone does not imply mathlib should expose this named certificate.

## Phase 7 — verdict and concrete future API questions

**BORDERLINE-needs-human**, independently assessed; parent182's BORDERLINE was context, not inherited. The arithmetic has no missing generic theorem and no separately named literature endpoint. The theorem has one real consumer. Its usefulness upstream depends on whether the exact proof-specific envelope itself becomes part of an upstream Roth API. No difficulty/cost-based downgrade is used; no unsupported NO/YES claim is forced by counting tactics.

Retain at `Roth/Theta.lean` beside lem6M. If local inlining is chosen later, the sole caller866 has a verified refactor plan above and a complete successful replay. Do not submit a new fixed-four-factor order theorem or invent another generalized wrapper around List.one_le_prod. Future upstream choices:

1. If the Lemma6 envelope is accepted as a public Roth constant, should its `1≤M` certificate be exported beside it?
2. If the envelope stays a local let, should this sole lower-bound use be inlined with the verified arithmetic proof?
3. Should a future coefficient-bound API expose individual factor lower bounds through generic product laws, leaving this particular uniform-degree envelope entirely downstream?

These are reviewable future design questions; the read-only assessment is complete and does not require pausing for user answers. No upstream PR home/title/reviewer/grouping is proposed for a non-YES verdict. Source/pin changes are outside this assessment.

## Phase 8 — evidence and handoff

All mandatory phases PASS; infrastructure is justified theorem n/a; unresolved[]. Five accepted native receipts: exact original/canonical audit, mathlib-only isolated batch, weak-order scalar batch, complete caller replay, complete module replay. All successful, nonpartial where the API exposes partial, no warnings/errors, standard axioms only. Raw run_code has no partial field; its complete success/diagnostics format is checked directly.

Rejected isolated attempts are preserved separately with exact requests and elapsed time in [preparation log](../evidence/Roth.one_le_lem6M/preparation-log.json): an omitted empty-list implication and an incorrect binder were corrected; two weak-order numeral elaboration failures were corrected by explicit typing and one_add_one_eq_two; one width-preparation failure caused an accidental stale rerun, explicitly excluded. Recovered sorryAx appears only in rejected receipts and never in accepted proof evidence. No claim of successful preparation is made for that stale rerun.

[Verification](../evidence/Roth.one_le_lem6M/verification.json), [assessment](../evidence/Roth.one_le_lem6M/assessment.json), [portable validator](../evidence/Roth.one_le_lem6M/validate.py), [current copy manifest](../evidence/Roth.one_le_lem6M/copy-manifest.json). Validator checks current manifest hashes/bytes, full exact canonical order/runtime values, accepted diagnostics/axioms, all17 baseline hashes, every mandatory phase/search cell/literature channel, complete callers and links. Root independently reviews and publishes.
