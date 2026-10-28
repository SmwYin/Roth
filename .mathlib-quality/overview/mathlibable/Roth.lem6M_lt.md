# Roth.lem6M_lt — canonical217

**BORDERLINE-needs-human.** Retain this coefficient-envelope absorption estimate in `Roth/Theta.lean`. A real-base extension and a larger determinant-size range compile, but the remaining upstream question is whether this particular numerical envelope should be public API in a future Roth small-index development. This is an independently completed assessment, not inheritance from parent182. Production sources and pins are unchanged; no implementation is proposed by this review.

## Phase 0 — baseline and native integrity

The public theorem resolves at `Roth/Theta.lean:649–672`. All17 current production/pin hashes match the successful2467-job baseline: [inputs](../evidence/Roth.lem6M_lt/inputs.json), [baseline](../evidence/Roth.lem6M_lt/baseline-build.txt). The entire985-line source module and the complete actual caller proof were read; [module](../evidence/Roth.lem6M_lt/source-module.lean.txt) preserves the source.

The [original exact execution](../evidence/Roth.lem6M_lt/original-executed.lean.txt) reproduces the entire module under a fresh namespace, renaming only the target to `replay` and updating its caller. [Native receipt](../evidence/Roth.lem6M_lt/original-receipt.json) is successful, partial=false, no warnings/errors, and checks every public replay declaration's axioms. The ordered canonical293 audit confirms293 unique names,293 present constants and293 values, including private modules; its sole direct value consumer is `_private.Roth.Theta.0.Roth.theta_phi_lt_aux`. This is a direct kernel-value audit, not a transitive or simp dependency closure.

The full native type is:
```lean
∀ {p : ℕ}, 0 < p → ∀ {δ : ℝ}, 0 < δ → ∀ {r₁ q₁ : ℕ},
  ↑p * (2 * ↑p + 1) / δ ≤ Real.log ↑q₁ → ∀ {l : ℕ}, 1 ≤ l → l ≤ r₁ →
  Roth.lem6M p r₁ (↑q₁ ^ (δ * ↑r₁)) l < ↑q₁ ^ (δ * (1 + 1 / ↑p) * (↑l * ↑r₁))
```
The byte-exact printer statement is in [native type](../evidence/Roth.lem6M_lt/native-type.json). Only `propext`, `Classical.choice`, `Quot.sound` occur. The large `#print` kernel body has an explicit MCP output-elision marker; this is not claimed as an unabridged kernel-body dump. Written replay source and the complete native type/axiom/value evidence remain available.

## Phase 1 — mathematical content

Let p be a positive natural number, δ a positive real number, and l,r positive natural sizes with l≤r. If a natural denominator q satisfies log q≥p(2p+1)/δ, then the determinant coefficient envelope
`M=(r+1)^(p*l) l! (q^(δ*r))^l 2^(p*l*r)` is strictly below `q^(δ*(1+1/p)*l*r)`.
This absorbs the combinatorial overhead into the extra exponent δ/p. It feeds the induction proving the small-index bound; it is not itself a theorem about roots, coprimality, or polynomial indices.

Parameters: p counts variables and occurs in natural exponents and the reciprocal exponent increment; r bounds partial degrees; l is determinant size and factorial index; δ is an exponent budget; q is the denominator base. Hypotheses are hp, hδ0, hq₁, hl, hl′. No ambient Fintype/DecidableEq/universe parameters survive elaboration. Direct project ingredients are exactly `Roth.lem6M`, `Roth.factorial_coefficient_le_two_pow_aux`, `Roth.two_pow_lt_rpow_aux`.

## Phase 2 — preliminary checks

SMALL: numerical helper, neither new structure nor the named main Lemma7. The proof has22 source lines. The one-line definition test is n/a because this is a theorem. Public, non-aux name and substantive arithmetic mean no B1 prefilter applies. Private215/216 are project proof ingredients, not existing mathlib replacements.

## Phase 3 — exhaustive literature

[Web requests](../evidence/Roth.lem6M_lt/web-general.json) preserve three distinct actual queries. Every named channel was attempted; records contain exact requests, response digest/bytes/status, clean full URL locators and original summaries only. No search/article bodies are archived.

| Channel | Query / locator | Finding |
|---|---|---|
| General web, specific | `Roth theorem lemma 7 "M" "delta" logarithm coefficient factorial bound` | Roth method and lecture-note results; some unrelated additive Roth hits. |
| General web, general | `Roth theorem auxiliary polynomial coefficient height exponential absorption bound logarithm` | Height control and large-denominator arguments in Roth expositions. |
| General web, aliases | `Roth small index lemma generalized Wronskian height estimate Dyson lemma` | Wronskian proof and alternative Dyson small-index approaches. |
| ChatGPT math | n/a | `ask_chatgpt_math` unavailable; no other channel reduced. |
| Local reference | clean.tex935–985 | Exact expression and absorption chain in proof of Lemma7; [excerpt](../evidence/Roth.lem6M_lt/clean-excerpt.tex.txt). |
| nLab | `site:ncatlab.org/nlab Roth theorem polynomial height logarithm` | Polynomial/free algebra and logarithm/height pages; no exact estimate. [Record](../evidence/Roth.lem6M_lt/nlab.json). |
| nCatLab | `site:ncatlab.org/ncatlab Roth polynomial coefficient height exponential` | Results were outside requested namespace, mainly nLab; no exact in-namespace hit. [Record](../evidence/Roth.lem6M_lt/ncatlab.json). |
| Stacks | `site:stacks.math.columbia.edu polynomial coefficients height factorial bound` | Hilbert polynomials/divided powers and algebraic multiplicities, different invariants. [Record](../evidence/Roth.lem6M_lt/stacks.json). |
| MathOverflow | `site:mathoverflow.net Roth theorem small index lemma height polynomial` | Dyson question431381 and quantitative Roth questions, surrounding method rather than this estimate. [Record](../evidence/Roth.lem6M_lt/mathoverflow.json). |
| Recent arXiv | `site:arxiv.org Roth Diophantine small index polynomial height after:2021-10-28 before:2026-10-29` | Hindes2209.09182 and other broader/unrelated results; no exact formula identified. [Record](../evidence/Roth.lem6M_lt/arxiv.json). |

Opened primary sources in [primary](../evidence/Roth.lem6M_lt/primary.json) and [locators](../evidence/Roth.lem6M_lt/primary-locators.json). [Roth1955](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/EFB89E2873019B246F004FAA06E05A7F/S0025579300000644a.pdf/rational_approximations_to_algebraic_numbers.pdf), pp12–13, Lemma7 proof between (21) and (24), has this absorption step. Its OCR corrupts formulas, so exact exponents are supported by clean.tex973–983, not silently reconstructed from OCR. [Milojevic's exposition](https://aleksa-milojevic.github.io/expository/roth.pdf), Lemma5.1, gives a different quantitative small-index condition; this supports the surrounding mathematics, not uniqueness of these constants. [Hindes](https://arxiv.org/abs/2209.09182) concerns positive-characteristic differences and does not supply an exact replacement.

Concept: finite exponential absorption of a factorial coefficient envelope. The source uses positive integer denominators and stronger surrounding degree/growth conditions. This theorem already isolates the arithmetic and allows equality in the logarithm threshold. No unique most-general named literature theorem was established; the real-base extension below is verified analytically, not mislabelled as an independently standard published formulation. Search failures are not proofs of nonexistence.

## Phase 4a–b — generality, checked extensions and limits

| Parameter/hypothesis | Role and current form | Checked assessment |
|---|---|---|
| p:ℕ; hp:0<p | Natural exponent/count and division by p | Kept; no assertion that proof use proves optimality. Zero-p formula guard fails strictly at r=l=1. |
| δ:ℝ; hδ0:0<δ | Positive exponent budget, divides log threshold | Kept. Zero-δ formula guard fails at p=r=l=1. No optimality claim. |
| r:ℕ | Degree/count exponent | With original l≥1,l≤r, r>0 follows. Extended size range needs an explicit r>0. |
| q:ℕ | Positive denominator in application | Arithmetic extends to real q≥0; log threshold then derives q>1. Full extended proof compiles. |
| hq₁ | Quantitative log threshold | Already nonstrict although original paper uses strict. Kept; no necessity or best-constant claim. |
| l:ℕ; hl:1≤l | Factorial/determinant size, strict multiplication | Kept; zero-size strict conclusion reduces to 1<1. |
| hl′:l≤r | Convenient source range | Extended to l≤2^r with r>0. The natural prefactor helper already accepts this bound. |
| section classes | None in full type | No hidden classes to remove. |

The [broader entire-module execution](../evidence/Roth.lem6M_lt/broader-executed.lean.txt) and [receipt](../evidence/Roth.lem6M_lt/broader-receipt.json) prove:
```lean
theorem realEnvelope {p : ℕ} (hp : 0 < p) {δ : ℝ} (hδ0 : 0 < δ)
    {r₁ : ℕ} {q₁ : ℝ} (hq₁nonneg : 0 ≤ q₁)
    (hq₁ : (p : ℝ) * (2 * p + 1) / δ ≤ Real.log q₁) {l : ℕ}
    (hl : 1 ≤ l) (hl' : l ≤ 2 ^ r₁) (hr₁ : 0 < r₁) :
    lem6M p r₁ (q₁ ^ (δ * r₁)) l < q₁ ^ (δ * (1 + 1 / p) * (l * r₁))
```
Its original-signature wrapper uses q≥0 by natural casting and r>0 by hl/hl′. All original downstream signatures, including the actual private caller and Θ_lt, remain unchanged in this replay. Thus both axes are actual verified extensions, not guessed parameter weakening. The [independent mathlib-only version](../evidence/Roth.lem6M_lt/isolated-executed.lean.txt) also compiles with the exact18imports and `#check_failure` guards against importing either project target or parent; [receipt](../evidence/Roth.lem6M_lt/isolated-receipt.json). Its `formula` and helper lemmas are NEW scratch code, not pre-existing library API.

STRICTLY NARROWER than the verified analytic extension; not claimed maximally general or uniquely literature-standard. Changing q alone is mechanical; widening l requires adding the positive-degree guard. Natural factorial/exponent indices are not arbitrary additive-group indices. Generalizing the ambient real analytic scalar would require an exponential/logarithm structure beyond a bare ordered field and has no demonstrated benefit here.

[Endpoint proofs](../evidence/Roth.lem6M_lt/inline-guards-executed.lean.txt) establish formula failure at l=0, at r=0,l=1, at p=0,r=l=1, and at δ=0,p=r=l=1. They are formula guards, not packaged counterexamples asserting that every other original hypothesis is simultaneously satisfied. In particular l≤r rules out r=0,l=1 in the original theorem; l≤2^r does not. `Real.log (-q)=Real.log q` explains why the logarithm threshold alone cannot derive positivity for unrestricted real q; no full negative-base counterexample is claimed. [Clean receipt](../evidence/Roth.lem6M_lt/inline-guards-receipt.json).

## Phase 4c — all nine modern idioms

| # | Question | Answer and concrete consequence |
|---|---|---|
| 1 | Typeclasses replace preambles? | No: numerical inequalities are value hypotheses; no new structure merits an instance. |
| 2 | Sequences/metrics to filters? | No limiting statement. A finite quantitative threshold is needed by caller. |
| 3 | Universal property? | No: this is an inequality, not an object construction. |
| 4 | Bundled substructure? | No closure predicate or lattice of subobjects. |
| 5 | Field-specific hierarchy? | Real log/rpow are substantive. Bare semiring-valued syntax does not preserve the analytic bound. |
| 6 | Higher categories? | No categorical content. |
| 7 | Concrete indices? | q can be a nonnegative real, actually checked, removing integrality from this arithmetic step. p,r,l remain combinatorial exponent/factorial indices. |
| 8 | Concrete-via-abstract? | Diagnostic fires for lem6M: two calc/body lines before unfolding, zero mentions after `rw [lem6M]`. The arithmetic splits into prefactor≤2^N, strict absorption2^N<q^e, and positive multiplication/exponent addition. A compiled `abstractAbsorb` transports any two supplied bounds, but the substantive prefactor and strict estimate are still new/project proofs. |
| 9 | False-generalization guard | q≥0 plus threshold preserves positive real powers; natural q specializes exactly. l-range extension adds r>0. Arbitrary signed q from log alone and arbitrary monoid factorial indices are rejected as unsupported. A filter eventual bound would lose the caller's explicit threshold. |

A useful organizational extension is possible, but no new broad analytic principle beyond existing positive multiplication and rpow laws is established. `abstractAbsorb` compiles in [composition](../evidence/Roth.lem6M_lt/composition-executed.lean.txt), with its [receipt](../evidence/Roth.lem6M_lt/composition-receipt.json). It enables scalar-bound transport but does not replace the numeric estimates. This is insufficient on its own to settle an upstream YES audience.

## Phase 4.5 — infrastructure

n/a for all six definition/instance risks: theorem introduces no new carrier, definitional alias, instance path or priority, universe-polymorphic construction, or coercion. Consequently typeclass diamond, reducibility leak, noncanonical definition unfolding, priority collision, universe restriction and coercion ambiguity assessments are n/a, rather than fabricated synthesis probes.

## Phase 4.6 — proof strategy

| # | Strategy question | Assessment |
|---|---|---|
| 1 | ε-δ versus filters | n/a: fixed finite inequality. |
| 2 | Elements versus subobjects | n/a: scalar arithmetic, no ideal/module inclusion. |
| 3 | Sequences versus nets | n/a: explicit threshold needed, not a limit. |
| 4 | Construction versus universal property | n/a: no categorical construction. |
| 5 | Missing helpers mathlib should have | Factorial-envelope and logarithmic-absorption helpers isolate the mathematics. Both are project/new proofs; public status depends on the broader coefficient-height API, not search absence. |

MATHLIB-IDIOMATIC strategy: bound the natural combinatorial prefactor, compare powers using log2<1 and exponential monotonicity, then combine exponents with rpow laws. An eventual-asymptotics result loses the explicit finite constant and is not a shorter proof of this statement. No cost-based downgrade or mandatory missing public helper is asserted.

## Phase 5 — fifteen actual method/form cells

Each cell has an individual raw receipt `search-<form>-<method>.json`, including full requests and failures/index status. Representative links: [current Finder](../evidence/Roth.lem6M_lt/search-current-leanfinder.json), [standard LeanSearch](../evidence/Roth.lem6M_lt/search-standard-leansearch.json), [abstract Loogle](../evidence/Roth.lem6M_lt/search-abstract-loogle.json), [current rg](../evidence/Roth.lem6M_lt/search-current-rg.json), [local](../evidence/Roth.lem6M_lt/search-standard-local_search.json).

| Method | Current formula | Literature absorption | Abstract bound transport |
|---|---|---|---|
| Finder | Exact envelope query: unrelated additive Roth | Polynomial approximation/Chevalley/Lindemann facts | Bertrand/Behrend estimates, not general bridge |
| Loogle | factorial,rpow,strict bound: empty | log,rpow,strict bound: empty | Exact `Real.rpow_add` hit |
| LeanSearch | Additive Roth and choose/factorial bounds | `Real.pow_div_factorial_le_exp`, eventual factorial growth, little-o exponential | `Real.rpow_add` and NNReal/ENNReal variants |
| rg | Full-name/form grep: no project envelope hit in mathlib | Factorial bounds and exp comparison candidates | log/rpow/exp candidate declarations |
| local | Project target itself | `Nat.factorial_le_pow` plus project helpers | `Real.rpow_mul_natCast` and NNReal variants |

Local index says **warming**, so it contributes positive source hits but no absence evidence. External indexes may use a different mathlib revision. Pinned positive signatures are compiled in the independent source: `Nat.factorial_le_pow`, `Nat.lt_two_pow_self`, `Real.rpow_add`, `Real.rpow_mul_natCast`, `Real.log_pos_iff`, `Real.exp_lt_exp`, `Real.pow_div_factorial_le_exp`. Pinned source search receipts retain full paths/lines. The last exp theorem bounds x^n/n!, whereas this theorem has n! in the numerator and varying natural parameters. Asymptotic little-o and eventual-factorial bounds lack this uniform finite threshold. No existing exact or more-general replacement was established; this does not prove global absence.

Parent re-aim: n/a. Parent182 lem6M was BORDERLINE with no existing D′ replacement, and this is a substantive law rather than rfl glue. Its earlier verdict was read for context but not inherited.

## Phase 5.5 — statement shape

Normal form: the source packages an envelope comparison rather than an equivalence; no RHS-normal-form issue. Equivalent choices include the expanded product and the logarithmic inequality for its positive factors. The named bound is easiest at the actual caller; expanded real-base formula is the cleaner independent arithmetic candidate. A different log form is not silently claimed canonical.

Syntactic alternatives actually compiled: named original natural-q statement, real-q wider-size statement, expanded independent formula, and generic bound transport with explicit upper bounds. The original application supplies l≤r naturally; using a wider theorem requires the verified wrapper, not pretend definitional equality of assumptions.

Every argument appears in the statement or proof. hp/hδ0/hq₁ drive strict absorption and base positivity, hl supplies l>0, hl′ supplies both the prefactor range and degree positivity. q's natural type is unnecessary analytically; original ambient classes are already absent. These are sufficient roles, not necessity/maximality proofs. For a future standalone arithmetic contribution: RESTATE-BEFORE-SHIP with real q and a documented size/degree interface. Locally SHIP-AS-STATED remains justified by actual denominator usage.

## Phase 6 — complete callers, inline audit and composition

[rg ignoring ignore rules](../evidence/Roth.lem6M_lt/source-search.json) and [tracked search](../evidence/Roth.lem6M_lt/tracked-source-search.json) agree: declaration649 and one explicit use871, both in Theta. Zero external-to-file callers; one in-file caller. [Structured caller](../evidence/Roth.lem6M_lt/callers.json) preserves the whole proof and source hash.

| Caller | Actual usage and potential refactor |
|---|---|
| `Roth.theta_phi_lt_aux`,840–889, call871 | Bounds its local M by a q0 power with ε=δ(1+1/p), obtains l≤r0 from the degree-ratio hypothesis, and supplies this bound to the one-variable and induction estimates. To inline locally, introduce the original full absorption proof as a local `absorbed` lemma immediately before hM, then use the identical application and final simp normalization. This entire caller plus all downstream declarations compiles in inline-guards execution. |

[Inline audit](../evidence/Roth.lem6M_lt/inline-audit.json) finds only the target and its two genuine helper inequalities; no separate full-form rederivation. Kernel direct value count is independently one, agreeing with lexical count here, without equating the concepts.

Composition experiments:

1. `fail_if_success exact?` on the independent full envelope statement succeeds as a negative closure probe before the new `realEnvelope` is declared. It does not find a complete existing theorem; this is finite search evidence only.
2. Direct candidate `Real.pow_div_factorial_le_exp q hq l` is rejected by a guarded term attempt; `simp only [formula]` also does not close. Accepted proof then constructs the new natural-prefactor and logarithmic estimates explicitly.
3. `abstractAbsorb` proves `A*(q^a)^l<q^(b+a*l)` from A≤C and C<q^b via rpow normalization and positive multiplication. Those inputs encode the substantive content; supplying them from this theorem's original assumptions still needs the two new/project helpers and arithmetic. Not an existing ≤3-call replacement.
4. Actual caller proof inlining is successful but still contains the full nontrivial estimate. One consumer is a scope signal, not proof of composability.

NOT-COMPOSABLE under the strict ≤3-existing-call rule. A new scratch/helper theorem does not count as a mathlib building block. There is no closing trivial simp composition to promote to automatic NO.

## Phase 7 — actionable verdict

BORDERLINE-needs-human, independently assessed. The specific unresolved judgment is **API audience and organization**: Roth's proof uses this deliberately generous envelope only once; literature confirms the step but uses alternative quantitative small-index formulations elsewhere. Verified generalization makes it more analytically reusable, yet does not establish that mathlib should name this isolated constant and its bound publicly. The concrete potential gap is an explicit determinant coefficient-height API with factorial overhead and large-denominator absorption; the available arithmetic primitives do not package that substantive bound. Lack of a named search hit is not the rationale by itself.

Retain `Roth.lem6M_lt` at `Roth/Theta.lean` as a proof-organizing local result. Do not delete it based on the private215/216 helpers or generic multiplication/rpow laws. If future upstream scope is chosen, use the already compiled real-q/wider-size statement or retain the source-facing wrapper with a documented reason; assess whether the prefactor and strict logarithmic helper deserve public names in that package. No production refactor is authorized by this review.

Future upstream API questions, not user blockers:

1. Should an eventual Roth small-index API expose this named coefficient envelope and its absorption bound publicly, or keep the estimate local to the induction proof?
2. Should its primary arithmetic interface use real q≥0, with natural-denominator users specializing through the checked wrapper?
3. Should the size hypothesis be the analytic range l≤2^r with explicit r>0, or the source-facing l≤r with degree positivity derived?
4. Should the factorial-envelope and strict logarithmic helpers be public parts of a general determinant-height API, rather than exporting this one numerical corollary alone?

All mandatory phases are complete and unresolved[]; these are future design choices. No YES PR home/title/grouping/reviewer recommendation is claimed. This verdict is not based on generalization cost or inherited parent policy.

## Phase 8 — evidence and limitations

[Verification](../evidence/Roth.lem6M_lt/verification.json), [phase ledger](../evidence/Roth.lem6M_lt/assessment.json), [portable read-only validator](../evidence/Roth.lem6M_lt/validate.py) and [current manifest](../evidence/Roth.lem6M_lt/copy-manifest.json) cover five accepted clean native executions, fresh source/pin hashes, ordered293 audit,15 formal-search cells, every literature channel and exact original caller replay. Rejected initial header-warning source/receipt and a redundant stale-source query after failed width preparation are explicitly excluded; the latter is not broadening evidence. The unsupported git-regex attempt and its corrected `-w` search are both retained. No sorry/new axiom/unsafe/native_decide/resource-limit raises are accepted. Root independently reviews before integration.
