# Roth.four_lt_rpow — canonical 238

**Verdict: BORDERLINE-needs-human.** The numerical implication is substantive. Existing
`Real.lt_rpow_of_log_lt` transports an already-established logarithmic inequality; it does
not derive that inequality from `3 ≤ δ² log q`. A real-base/real-degree extension and sharper
threshold compile, but the choice between a general inequality API and a Roth-specific
numerical corollary remains an upstream design question. This assessment is complete;
the future design questions below do not block the overview.

## Phase 0 — Baseline and scope

Resolved public theorem at `Roth/MainLemma.lean:122`. All 17 production-source/pin hashes
freshly match the tracked shared manifest; the reusable baseline build passed 2467 jobs.
The accepted file-end build through Theta228 remains applicable; this is not a file-end
checkpoint. No production sources, pins or Git state were changed. Both entire declaring
and caller modules were read and archived.

Evidence: [fresh inputs](../evidence/Roth.four_lt_rpow/inputs.json),
[baseline](../evidence/Roth.four_lt_rpow/baseline-build.txt),
[MainLemma](../evidence/Roth.four_lt_rpow/source-MainLemma.lean.txt),
[Main](../evidence/Roth.four_lt_rpow/source-Main.lean.txt).

## Phase 1 — Mathematical content and exact type

For a nonnegative real δ, a natural base q and a positive natural degree r, the lower bound
δ² log q ≥ 3 implies q^(δr) > 4. Positivity of log q follows from the premise, so q ≥ 2.
The proof bounds log 2 by 3/4 using a quadratic lower bound for exp, then squares a hypothetical
reverse inequality to prove log 4 < δ log q. Multiplying by r ≥ 1 and applying the log/rpow
comparison finishes the argument. This is an auxiliary estimate for a positive natural floor
coefficient bound in the main lemma and the final Roth argument.

The full native type from `Lean.getConstInfo` with `pp.funBinderTypes` is:

```lean
∀ {δ : ℝ}, 0 ≤ δ → ∀ {q₁ r₁ : ℕ}, 0 < r₁ →
  3 ≤ δ ^ 2 * Real.log ↑q₁ → 4 < ↑q₁ ^ (δ * ↑r₁)
```

Parameters: δ is the small real parameter; q₁ is a natural denominator; r₁ is a positive
natural degree. There are no typeclass parameters and no project declarations in the proof.
All three hypotheses matter in the senses detailed below. The full original module replay
renames only this theorem outside the canonical array and proves its signature unchanged.

[Original exact source](../evidence/Roth.four_lt_rpow/original-executed.lean.txt),
[complete raw receipt](../evidence/Roth.four_lt_rpow/original-receipt.json),
[native type](../evidence/Roth.four_lt_rpow/native-type.json).
The large body printer explicitly elides 96561 characters. This is not a full body dump;
the complete executed source, full kernel type, axioms and canonical value audit are retained.

## Phase 2 — Preliminary checks

SMALL: an elementary numerical helper, not a named theorem, structure, or module-listed main
result. Exhaustive literature width is unchanged. Definition-only one-line test: **n/a —
theorem**. Its roughly 25-line proof is not classified as a one-line definition, and neither
its final API call nor usefulness of `main_lemma` determines its verdict.

## Phase 3 — Exhaustive literature channels

Every named channel was actually queried. Exact requests, returned-response SHA256/byte
counts/status, clean titles/URLs and original summaries are archived; full web/search bodies
are omitted. No search failure or irrelevant return is treated as proof of absence.

| Channel | Actual query or source | Finding and limitation |
|---|---|---|
| General, specific | `Roth theorem auxiliary polynomial coefficient bound q delta log q greater than four` | Roth auxiliary-polynomial context; no canonical named numerical theorem established. |
| General, broader | `logarithm power inequality squared exponent log base lower bound` | Elementary logarithmic inequalities, including NIST DLMF. |
| General, aliases | `exponential logarithmic inequalities comparison powers positive base` | Comparison of positive powers by logarithms is standard; constants3/4 are not a standard named package. |
| ask_chatgpt_math | n/a | Tool unavailable; optional channel skipped explicitly. |
| Local source | `clean.tex`, §6, lines1320–1384 | Equations29/32, coefficient bound37 and X>4. Source uses stronger parent constraints; this Lean helper deliberately isolates a weaker sufficient premise. |
| nLab | `site:ncatlab.org/nlab logarithm exponential ordered real numbers` | Logarithm/exponential concepts returned; direct logarithm open failed400, unsupported XHTML. |
| nCatLab, distinct | `site:ncatlab.org/ncatlab logarithm exponential inequality` | Returned mostly /nlab and other namespaces; no exact /ncatlab result claimed. |
| Stacks | `site:stacks.math.columbia.edu logarithm exponential inequalities real powers` | No exact numerical analytic helper established. Algebraic geometry context does not supply a replacement. |
| MathOverflow | `site:mathoverflow.net logarithmic inequalities real powers Roth theorem` | No exact helper established; homonymous Roth contexts require care. |
| Recent arXiv | `site:arxiv.org Roth theorem auxiliary polynomial logarithmic inequalities after:2021-10-28 before:2026-10-29` | Mostly tangential results; additive-combinatorial Roth is distinct from Diophantine approximation. |
| Recent arXiv, retries | Explicit `/abs/` Roth auxiliary/formalization and Diophantine/irrational-algebraic queries, same date window | Hindes2209.09182 is genuinely Diophantine but characteristic p; it does not supply this real numerical estimate. Other returned prime-approximation papers and author-name homonyms are not evidence for the target. |
| Primary follow-up | Actual open of NIST DLMF §4.5, formulas4.5.1/4.5.4/4.5.8/4.5.13 | Positive-real log/exp inequalities support the method, not the exact δ²logq premise or a Lean replacement. Root independently crosschecked the same page. |

[Literature metadata](../evidence/Roth.four_lt_rpow/web-general.json),
[nLab](../evidence/Roth.four_lt_rpow/web-nlab.json),
[nCatLab](../evidence/Roth.four_lt_rpow/web-ncatlab.json),
[Stacks](../evidence/Roth.four_lt_rpow/web-stacks.json),
[MathOverflow](../evidence/Roth.four_lt_rpow/web-mathoverflow.json),
[recent arXiv](../evidence/Roth.four_lt_rpow/web-arxiv.json),
[targeted retries and primary open](../evidence/Roth.four_lt_rpow/web-primary.json),
[Diophantine retries](../evidence/Roth.four_lt_rpow/web-diophantine.json),
[local excerpt](../evidence/Roth.four_lt_rpow/literature-local-excerpt.txt),
[root primary crosscheck](../evidence/Roth.four_lt_rpow/root-primary-crosscheck.json).

Literature synthesis: this is a logarithmic lower bound for a real power, using monotonicity,
a lower bound away from1 for the base, and comparison of squares. The literature supports
positive-real analytic forms rather than a special natural-denominator theorem. It does not
identify a unique upstream theorem packaging these hypotheses. No historical evolution claim
is inferred from the unavailable second-opinion tool.

## Phases 4a–4b — Generality and verified weakening

| Parameter/hypothesis | Assessment, with compiled evidence |
|---|---|
| δ : ℝ | Real logarithm/rpow need their real analytic setting. The arithmetic square-transfer subargument extends to an ordered commutative semiring, verified also over ℚ; this does not generalize Real.log itself to arbitrary semirings. |
| 0 ≤ δ | Cannot drop: δ=-3,q=2,r=1 satisfies the numerical premise and fails the conclusion. δ=0 makes the premise impossible, so strict positivity follows under the complete hypotheses; replacing nonnegative by positive would strengthen, not weaken. |
| q : ℕ | Integrality is used to turn q>1 into q≥2. Replaced by real q≥2 in a compiled extension. Mere real q>1 is false: q=exp(1/4),δ=4,r=1 has δ²logq=4 and q^(δr)=exp1<4. |
| r : ℕ, 0<r | Only r≥1 is used; real r≥1 compiles, including r=3/2. Zero degree fails. Mere positivity of a real degree fails for δ=3,q=2,r=1/3. This does not prove r≥1 is the optimal separate bound. |
| 3 ≤ δ²logq | Sharpened to `4*log2 < δ²logq` for q≥2,r≥1. The strict threshold is sharp uniformly over that base/degree range: q=2,δ=2,r=1 has equality and power4. The original weak3 endpoint remains valid; δ=√(3/log2),q=2,r=1 realizes it. |
| Fixed constants4 and3 | They are sufficient numerical constants, not a new semantic object. A compiled arbitrary-target/threshold transfer isolates square comparison; it is a new proof, not an existing mathlib theorem. |

Current form is **STRICTLY NARROWER** than verified sufficient analytic forms. No maximality
is claimed for the real-base or real-degree hypotheses. The precise power/log criterion is
already `Real.lt_rpow_iff_log_lt`; supplying it as a new hypothesis merely assumes the key
step and does not establish that the original theorem is a trivial specialization.

Verified useful candidate:

```lean
∀ {d q r : ℝ}, 0 ≤ d → 2 ≤ q → 1 ≤ r →
  4 * Real.log 2 < d ^ 2 * Real.log q → 4 < q ^ (d * r)
```

Verified semantic-parameter candidate:

```lean
∀ {a c d q r : ℝ}, 0 ≤ d → 1 < q → 1 ≤ r →
  c ≤ d ^ 2 * Real.log q → (Real.log a) ^ 2 < c * Real.log q → a < q ^ (d * r)
```

Verified algebraic subargument:

```lean
∀ {K : Type*} [CommSemiring K] [LinearOrder K] [IsStrictOrderedRing K]
  {a c d L : K}, 0 ≤ d → 0 < L → c ≤ d ^ 2 * L → a ^ 2 < c * L → a < d * L
```

These are scratch proofs. Real-base and degree changes are mechanically proved sufficient;
no production API is changed. Generic numerical parameters enable targets other than4 and
thresholds other than3, but their exact API value needs comparison with existing square-order
lemmas. The initial semiring `nlinarith` attempt failed; explicit square monotonicity and a
ring normalization compiled. A tactic failure was not interpreted as a structural obstruction.

[Isolated exact source](../evidence/Roth.four_lt_rpow/isolated-executed.lean.txt),
[isolated clean receipt](../evidence/Roth.four_lt_rpow/isolated-receipt.json),
[boundary and semiring proofs](../evidence/Roth.four_lt_rpow/boundary-executed.lean.txt),
[boundary clean receipt](../evidence/Roth.four_lt_rpow/boundary-receipt.json).

## Phase 4c — All nine modern-idiom checks

| # | Question | Answer and downstream consequence |
|---|---|---|
| 1 | Typeclass preambles | No new class is warranted for pointwise numerical inequalities. Existing ordered structures suffice for the algebraic subargument. |
| 2 | Filters/topology | No sequence or convergence occurs; filter restatement supplies no benefit. |
| 3 | Universal property | No object is constructed. |
| 4 | Bundled substructure | No closure predicate or subobject. NNReal bundling δ would hide an existing explicit sign premise and would still need positive logarithm analysis. |
| 5 | Hierarchy weakening | Yes for square transfer: ordered CommSemiring verified. Full Real.log/rpow statement stays analytic over ℝ. |
| 6 | Higher categories | No categorical content. |
| 7 | Concrete indices | Yes: real r≥1 instead of positive natural r; q≥2 explicitly replaces the integrality-derived gap. Enables existing real-exponent monotonicity API. |
| 8 | Concrete-via-abstract | Numeric4 occurs only in the log4 comparison/numeral rewrite, and3 in positivity/threshold arguments. There is no named witness disappearing after unfolding. Their semantic roles can be parameterized by a,c, with the strict square-gap premise retained. Generic squareTransfer/powerTransfer compile; they are own new proofs. |
| 9 | False-generalisation guard | Real q>1 alone is rejected by the explicit exp(1/4) counterexample. Real r>0 alone is rejected by1/3. Dropping δ's sign is rejected. Replacing Real.log with a symbol over arbitrary rings is not proposed. |

Modern idiom available: **yes**, real parameter interfaces and an abstract square-transfer
kernel. Benefit: exposes base-gap and degree requirements to Real power/log API and separates
ordered algebra from analysis. It does not establish that another bundled or categorical
infrastructure should be added.

## Phase 4.5 — Infrastructure risks

All six rows are **n/a — theorem**: typeclass diamonds, reducibility leaks, noncanonical
unfolding, instance-priority collisions, universe-polymorphism issues and coercion ambiguity.
No definition, instance or coercion is introduced by this theorem. Proposed scratch theorem
variants likewise add no instance paths; no infrastructure probe is required for this kind.

## Phase 4.6 — All five proof-strategy checks

| # | Check | Assessment |
|---|---|---|
| 1 | ε–δ versus filters | n/a: pointwise inequality, no neighborhoods. |
| 2 | Elements versus subobjects | n/a: arithmetic comparison, no ideal/submodule. |
| 3 | Sequences versus nets | n/a: no limit. |
| 4 | Construction versus universal property | n/a: no object construction. |
| 5 | Missing helper API | Candidate: square-gap-to-product comparison, or real-base rpow numerical threshold. Existing square-order primitives plus normalization already do the algebra; reusable packaging is the open taste question. |

Strategy: **REFACTOR-RECOMMENDED** for any upstream version. Separate square comparison from
logarithmic estimates, then use existing `Real.lt_rpow_of_log_lt` for the final transport.
The existing proof's reasoning is sound. No cost argument changes the verdict.

## Phase 5 — All fifteen formal-search cells

Each of current, literature-standard and abstract forms was submitted to Finder, Loogle,
LeanSearch, source rg and local-name search. The [15-cell matrix](../evidence/Roth.four_lt_rpow/formal-search-matrix.json)
links every exact request/full raw result. All cells were executed; returned limitations are
preserved rather than converted to absence claims.

| Form | Finder | Loogle | LeanSearch | Pinned rg | Local index |
|---|---|---|---|---|---|
| Current δ²logq≥3 → power>4 | Behrend additive-Roth estimates, not this theorem | No exact result | Integer logarithm/zpow estimates, not this premise | No exact specialized spelling | Source hit Roth.four_lt_rpow; index error |
| Standard positive-base log/power comparison | Real.le_pow_of_log_le and zpow variants | Real.lt_rpow_of_log_lt, Real.lt_rpow_iff_log_lt | Power/log transport; some external names differ from pin | Existing transport and log/exp estimates | Real.lt_rpow_of_log_lt source hit; index error |
| Abstract square comparison | Nonnegative square-order and AM–GM primitives | Partial square-product facts, not full target | sq_lt_sq₀ and mul_self comparison | Existing square/multiplication monotonicity | Square-order source hits; index error |

Local index errors do not prove absence. External indexes can differ from the pin: the
accepted isolated source checks the actual pinned signatures before use. The full-name scan
is untruncated. A broad exact? probe occurred only in the rejected timeout request; it is
neither an accepted no-hit probe nor proof of absence, and was not repeated. Timing caveat:
external formal-search setup timings were evaluated before await; their zero values do not
measure network duration. Native elapsed timings correctly surround awaited requests.

Positive building blocks verified in the pin include:
`Real.lt_rpow_of_log_lt`, `Real.lt_rpow_iff_log_lt`, `Real.log_le_log`,
`Real.log_lt_iff_lt_exp`, `Real.quadratic_le_exp_of_nonneg`,
`Real.le_log_one_add_of_nonneg`, `Real.lt_log_one_add_of_pos`,
`sq_lt_sq₀`, `mul_self_le_mul_self`, `pow_le_pow_left₀` and
`Real.rpow_le_rpow_of_exponent_le`.
The relevant homes are `Mathlib/Analysis/SpecialFunctions/Pow/Real.lean`,
`Mathlib/Analysis/SpecialFunctions/Log/Basic.lean`, and the ordered-ring/monoid square API.
[Pinned source hashes](../evidence/Roth.four_lt_rpow/mathlib-inputs.json),
[full-name scan](../evidence/Roth.four_lt_rpow/full-name-search.json),
[timing disclosure](../evidence/Roth.four_lt_rpow/search-timing-note.json).

Conclusion: partial matches and building blocks, not a verified exact existing numerical
implication. No mathematical absence theorem is asserted.

## Phase 5.5 — Three statement-shape checks

1. **Normal form:** Real.rpow is already appropriate. `4 < q^(δr)` and
   `log4 < δr*logq` are equivalent under q>0 by the existing iff theorem. Keep the power
   conclusion for floor consumers; use the log form internally. No new O(n²) equivalence API.
2. **Syntactic generality:** tested real-base/degree and strict-threshold variants plus
   arbitrary a,c transfer. Existing callers supply the original weak3 premise conveniently;
   a sharper logarithmic constant should be hidden behind a general numerical lemma only
   if upstream accepts that abstraction. No mere reassociation is counted as generalization.
3. **Superfluous arguments:** δ sign cannot be dropped; r positivity cannot be dropped in
   the natural form; numerical hypothesis cannot be dropped (δ=0 gives power1). q's natural
   type carries the crucial discrete gap; no hidden typeclass is present. δ positivity and
   q≥2 are derived, not additional premises needed by the original signature.

Overall: **RESTATE-BEFORE-SHIP** for upstream consideration; no original premise is simply
unused. Preserve original project signatures while deciding the upstream interface.

## Phase 6.0 — All callers and inline audit

| Caller | Source use | Role |
|---|---|---|
| Private exists_mem_RSet_le_index_of_log_bound_aux | MainLemma:641, `(four_lt_rpow hδ0 hr₁ hq).le` | Proves Nat.floor_pos for B. |
| Private roth_product_bound_aux | Main:495, `(four_lt_rpow hδ0 hr0 h32').le` | Supplies X≥2 to sqrt_lt_floor and positive B. |

Two source proof calls overall; internal count excluding the declaring file is1, across one
other file. Fresh `rg --no-ignore`, tracked `git grep`, and the canonical293 kernel-value
scan agree. There are exactly two direct kernel proof consumers and zero direct type
consumers. No `[simp]` attribute is attached. Source lexical/type/kernel/simp/transitive
scopes remain distinct. Downstream final Roth theorems depend transitively through these
helpers; direct counts are not a transitive-closure count.

Inline-derivation search found no separate rederivation of this exact4-bound. Adjacent
private `two_lt_rpow_aux` is a moral duplication of the square-comparison method with a
weaker bound aimed at2; it is not an existing mathlib replacement. The generic arbitrary-target
transfer is a concrete route to sharing the method, with numeric hypotheses still proved.

The full original bodies of both modules were replayed with this target declaration/docstring
removed and its complete arithmetic proof put inside each actual caller as a local
`numericalBound`. For scratch inspection, private lemmas in the cloned modules were made
public; production visibility was unchanged. Both caller signatures and main_lemma,
roth_of_isIntegral, roth and roth_rat were kernel-compared with the originals: six identical
signatures, standard axioms, no direct target reference in the six replayed values.
This establishes inlining feasibility, not an existing-only three-call proof.

[Caller inventory](../evidence/Roth.four_lt_rpow/callers.json),
[source search](../evidence/Roth.four_lt_rpow/source-search.json),
[tracked search](../evidence/Roth.four_lt_rpow/tracked-source-search.json),
[inline derivation search](../evidence/Roth.four_lt_rpow/inline-search.json),
[canonical consumers](../evidence/Roth.four_lt_rpow/canonical-consumers.json),
[full caller-inline source](../evidence/Roth.four_lt_rpow/inline-executed.lean.txt),
[clean inline receipt](../evidence/Roth.four_lt_rpow/inline-receipt.json).

## Phase 6 — Composition experiments

* Existing final transport compiles in one call when supplied `log a < z*log q`.
  The original δ²logq premise has a different type; a guarded direct application fails even
  with base positivity already proved. That is evidence of the missing numerical bridge,
  not global absence of any short proof.
* The isolated original form is reconstructed from new squareTransfer/powerTransfer,
  realBase and sharper proofs. These new lemmas cannot be counted as existing mathlib calls.
* The algebraic semiring route uses square monotonicity, multiplication monotonicity,
  transitivity and ring normalization. The full theorem additionally proves base separation,
  the strict log2 numerical estimate, logarithm-square comparison, degree enlargement and
  final log/rpow transport. Those are genuine arithmetic reasoning steps, not a certified
  composition of at most three existing calls.
* Full caller inlining succeeds by duplicating the original proof. It does not shorten that
  proof to three existing calls. No closing `simp [defs...]` composition was found or claimed.

Conclusion: **NOT-COMPOSABLE in the certified existing-only ≤3-call sense**; no such witness
was established. The exact? timeout is inconclusive. Novelty or upstream desirability does
not follow merely from a failed search/probe.

## Phase 7 — Verdict and concrete future upstream questions

**BORDERLINE-needs-human.** This is a complete assessment with no verification blocker.
The original estimate is more than final rpow transport and is used at two genuine caller
sites. Verified real-base/degree and sharp-threshold forms expose broader mathematics.
Nevertheless4 and3 encode a local sufficient margin; the reusable part may belong to the
existing elementary square-comparison API, while an arbitrary a,c packaging introduces a
squared-log premise that consumers may prefer to prove directly. Neither search silence,
parent theorem importance, nor refactoring cost decides which API mathlib should export.

1. Should the uniform real-base `q≥2,r≥1,4log2<δ²logq` estimate be exported in
   `Mathlib/Analysis/SpecialFunctions/Pow/Real.lean`, or should this sufficient margin stay
   local to Roth/MainLemma?
2. Is a general square-gap-to-product lemma over ordered commutative semirings a useful
   addition near the square-order API, or should users combine square monotonicity and
   multiplication monotonicity directly after normalization?
3. If the numerical analytic lemma is accepted, should its primary interface retain an
   arbitrary target/threshold with squared-log gap, or use a base-lower-bound parameter so
   callers can supply an explicit uniform margin without proving that gap each time?

Recommended local action: retain the proven helper while resolving that future upstream
interface; consider sharing its square-comparison argument with private two_lt_rpow_aux.
No deletion is justified by a verified existing replacement. If a future choice is to inline,
both exact caller locations and a complete signature-preserving experiment are archived.
No YES PR title/reviewer/grouping is proposed because this assessment does not select YES;
no prior accepted declaration's verdict is inherited.

## Phase 8 — Verification and handoff

The portable validator checks all phase/entry keys, current artifact manifest hashes/bytes,
17 source/pin hashes, exact293 canonical source order/private modules and runtime presence/
values/uniqueness, native complete success, required tagged messages and standard axioms,
source/request identity, all15 search cells, web metadata and relative report links. It
supports both scratch and integrated layouts and validates the current manifest, not a
historical worker manifest. Rejected timeout/compiler attempts are retained separately,
including recovered sorryAx diagnostics, and are never accepted proof evidence.

[Verification](../evidence/Roth.four_lt_rpow/verification.json),
[portable validator](../evidence/Roth.four_lt_rpow/validate.py),
[current manifest](../evidence/Roth.four_lt_rpow/copy-manifest.json),
[secret guard](../evidence/Roth.four_lt_rpow/secret-guard.json).
