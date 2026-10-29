# Roth.exists_degrees — canonical278

**Verdict: YES-but-generalise-first.** The reusable contribution is finite positive-weight natural
rounding with independent error, lower threshold and growth margin. The exact Roth wrapper is a
corollary. This assessment proposes changes; production Lean files and pins remain unchanged.

## Phase0 — baseline and scope

Shared baseline: clean2467 jobs; all17 source/pin hashes freshly match the tracked shared manifest.
No file-end build is due at278 (next289). See [baseline-build.txt](../evidence/Roth.exists_degrees/baseline-build.txt), [inputs.json](../evidence/Roth.exists_degrees/inputs.json).
The declaration resolves at Roth/Main.lean282–317. Entire Main1–588 and LeanEval1–73 were read.
Original re-elaboration copies only the complete target in a fresh namespace; no private helpers
are needed. Loaded original full type, direct kernel constants, standard axioms, and all293 ordered
canonical declarations are independently audited. Printer output explicitly elides78277 characters;
this is **not** a full kernel-body dump. Complete written original proof is retained.

[original-executed.lean.txt](../evidence/Roth.exists_degrees/original-executed.lean.txt); [original-receipt.json](../evidence/Roth.exists_degrees/original-receipt.json); [native-type.json](../evidence/Roth.exists_degrees/native-type.json).

## Phase1 — mathematical content

Given positive logarithms growing by at least2/δ at each successor, choose positive integer degrees
rj>10/δ so that adjacent degrees satisfy rj/δ<ri. Their logarithmic products all lie in the
half-open interval from r0 log(q0) to (1+δ/10)r0 log(q0). The source chooses a common large integer
scale using Finset.sup', rounds each inverse logarithmic weight upward, and bounds the rounding
error by one. The final factor estimate uses hδ1; the existence assertion itself does not need it.

Full native original type:
```lean
∀ {m : ℕ} [inst : NeZero m] {δ : ℝ},
  0 < δ →
    δ ≤ 1 →
      ∀ {q : Fin m → ℕ},
        (∀ (j : Fin m), 1 < q j) →
          (∀ (i j : Fin m), ↑i + 1 = ↑j → 2 / δ * Real.log ↑(q i) ≤ Real.log ↑(q j)) →
            ∃ (r : Fin m → ℕ),
              (∀ (j : Fin m), 0 < r j) ∧
                (∀ (j : Fin m), 10 / δ < ↑(r j)) ∧
                  (∀ (i j : Fin m), ↑i + 1 = ↑j → ↑(r j) / δ < ↑(r i)) ∧
                    (∀ (j : Fin m), ↑(r 0) * Real.log ↑(q 0) ≤ ↑(r j) * Real.log ↑(q j)) ∧
                      ∀ (j : Fin m), ↑(r j) * Real.log ↑(q j) < (1 + δ / 10) * (↑(r 0) * Real.log ↑(q 0))
```
Written project dependencies: `[]`; direct kernel project dependencies: `[]`. Arithmetic and order
lemmas are mathlib. Source occurrences, direct type/body consumers, transitive source closure and
implicit simp/typeclass dependencies are distinct scopes. See [canonical-consumers.json](../evidence/Roth.exists_degrees/canonical-consumers.json).

## Phase2 — preliminary checks

SMALL: quantitative helper, no new structure or main named result. Definition-only one-line check:
n/a, theorem. Its short scale/rounding spelling does not establish a three-call composition.

## Phase3 — exhaustive literature

| Channel | Exact query | Title / locator | Finding |
|---|---|---|---|
| web-specific | Roth theorem degrees r_j log q_j ceiling r_1 log q_1 log q_j | Transcendental Number Theory, Soundararajan/Petrow; §15, p56, lines5060–5111 | Positive degree/log products are balanced, with integer rounding at large common scale. Exact constants differ; supports mathematical pattern, not this precise helper name. |
| web-general | finite positive real numbers natural multiples common large scale ceiling relative error | CS4220 Numerical Analysis, David Bindel; Notions of error | General query returned numerical relative-error material; it does not establish this finite balancing lemma as a standard named theorem. |
| web-alias | simultaneous rounding positive weights ceiling Archimedean approximation Roth proof degrees | Rounding probabilities: Unbiased multipliers, Pukelsheim; multiplier-rounding discussion | Rounding weight vectors with a prescribed sum is related terminology, but the sum constraint is absent here. Do not conflate it with our theorem. |
| nlab | site:ncatlab.org/nlab Archimedean ordered field approximation integers | Archimedean ordered field; definition/search result | Archimedean structure is the relevant abstraction. Direct fetch failed with unsupported application/xhtml+xml; no full page reading claimed. |
| ncatlab | site:ncatlab.org/ncatlab simultaneous rounding positive real numbers | No in-namespace exact result; actual site:ncatlab.org/ncatlab query | Returned /nlab and other host namespaces. No exact /ncatlab hit; no categorical reformulation supported. |
| stacks | site:stacks.math.columbia.edu Archimedean integer approximation positive real | The Trace Formula; search result, simultaneous powers in a sector | Search found simultaneous sector approximation, a different complex-number problem. No matching positive-weight degree rounding result; no algebraic geometry restatement proposed. |
| mathoverflow | site:mathoverflow.net Roth theorem proof degrees logarithms rounding | Estimate number of solutions in Roth’s theorem; quantitative bounds discussion | Discussion concerns solution counts and auxiliary polynomial techniques, not a finite ceiling-rounding API. |
| arxiv | site:arxiv.org Roth theorem Diophantine approximation auxiliary polynomial degrees after:2021-10-29 before:2026-10-30 | Diophantine approximation and the subspace theorem; Goel–Lunia–Ray, submitted2025-02-02, revised2026-07-21, abstract | Recent survey covers proofs of Roth and subspace theorems. Its abstract does not certify the exact rounding helper; dated search also returned characteristic-p and unrelated additive Roth results. |

Local source: clean.tex1608–1646, §7 eqs51–53. The author notes explicitly request one rounding
lemma. Optional ask_chatgpt_math is unavailable; all remaining named channels were actually queried.
The precise complete sources and own summaries are in [literature.json](../evidence/Roth.exists_degrees/literature.json). External response
hashes/bytes/status and exact requests are archived; full article/search bodies are not persisted.
Primary direct access succeeded for Soundararajan/Petrow p56 and the2025/2026 arXiv survey; nLab
returned unsupported XHTML. General rounding/sum-preserving apportionment and characteristic-p
analogues are distinct results. Neither a standard name nor the most general field statement is
attributed to the recent survey's abstract. The broader field form is our tested new proof.

## Phase4a–b — generality

| Parameter | Finding |
|---|---|
| m/NeZero | Needed to address base0; generic base b over Finite ι replaces it. |
| δ>0 | Retained in original quantitative extension; zero error impossible at base. |
| δ≤1 | Removed natively while retaining original outputs, via τ=min(δ/10,1/2). δ≤10 is a weaker consequence, no need stop there. |
| q naturals | Only log positivity used; arbitrary positive weights verified over floor ordered fields. |
| q>1 | Cannot weaken to q≥1; q=1 strict upper0<0 counterexample. |
| h50 | Weak growth inequality sufficient; strict ratio obtained from strict ceiling upper bound and c>1 margin. |
| 10,2,δ/10 | Generalize independently to positive B, c>1 and ε>0; not merely renamed arithmetic constants. |

The exact original upper bound δ≤1 is removable with **all** five quantitative outputs retained.
Take ε=δ/10, B=10/δ and c=2 in the generic theorem. Internally use τ=min(δ/10,1/2)>0;
choose a sufficiently large scale using max(B,1/τ). The strict upper error is at most1+τ≤3/2≤2,
so adjacency cancellation still gives rj/δ<ri. Since τ≤δ/10, the original strict upper product bound
survives. This also covers δ≤10; stopping at10 would leave a verified further weakening.
The complete exact old type is recovered by retaining its unused hδ1 binder.

Original δ>0, q>1/log positivity and successor conditions remain in that recovered interface.
Generic δ>0 was independently found unnecessary and removed, since its error and B are independent
positive parameters; that does not authorize removing original δ>0. Zero error and zero weight
contradict the strict upper bound at the base; c=1 with equal weights contradicts strict separation.
The q=1 counterexample blocks merely weakening q>1 to q≥1. See [edges-executed.lean.txt](../evidence/Roth.exists_degrees/edges-executed.lean.txt).

Proposed complete generic signature (tested section binders included):
```lean
variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K] [FloorRing K]
theorem exists_separated_nat_multiples {ι : Type*} [Finite ι] (b : ι) {ℓ : ι → K} (hℓ : ∀ j, 0 < ℓ j)
    {ε B δ c : K} (hε : 0 < ε) (hB : 0 < B) (hc : 1 < c)
    (R : ι → ι → Prop) (hg : ∀ i j, R i j → c / δ * ℓ i ≤ ℓ j) :
    ∃ r : ι → ℕ, (∀ j, 0 < r j) ∧ (∀ j, B < r j) ∧
      (∀ i j, R i j → (r j : K) / δ < r i) ∧
      (∀ j, (r b : K) * ℓ b ≤ r j * ℓ j) ∧
      ∀ j, (r j : K) * ℓ j < (1 + ε) * (r b * ℓ b)
```

[generic5-executed.lean.txt](../evidence/Roth.exists_degrees/generic5-executed.lean.txt); [recovery5-executed.lean.txt](../evidence/Roth.exists_degrees/recovery5-executed.lean.txt).
Verified strictly weaker hypotheses and broader applicability, with modern abstraction. Proof effort is moderate;
cost does not drive the verdict. Natural witnesses and every strict/weak endpoint are preserved.

## Phase4c — modern idioms

| Question | Applies | Restatement | Downstream consequence |
|---|---|---|---|
| Typeclasses | yes | Field, LinearOrder, IsStrictOrderedRing and FloorRing on K; Finite index | Rational and real weights share one proof; no explicit Archimedean assumption, inferred by FloorRing.archimedean. |
| Filters | no | Finite quantitative existence retained | tendsto_nat_ceil_mul_div_atTop is an asymptotic building block but loses the explicit finite package; filter proof would need finite-eventual intersection. |
| Universal property | no | Existential witnesses with inequalities | No universal construction characterized. |
| Bundled substructure | no | Positive weight hypotheses | No closure subset/algebraic substructure. |
| Algebraic hierarchy | yes | ℝ→ordered floor field | Only ordered-field arithmetic and ceiling bounds are used; no real completeness or logarithm after positivity. |
| Higher categories | no | None | Finite ordered arithmetic is unrelated. |
| Concrete index | yes | Fin m→Finite ι with base b and relation R | Avoids nonzero dimension/Fin successor bookkeeping in generic API. |
| Concrete via abstract | yes | Replace log(q j) by arbitrary positive ℓ j, δ/10 by ε and 2 by c>1 | Real.log appears only in initial positivity line; generic proof and exact full recovery verified natively. |
| False generalization | no false change | Retain natural witnesses, strict upper/ratio and weak lower products | All five original outputs recovered together. Lower threshold and error are independent semantic parameters, not cosmetic constant changes. |

The concrete-via-abstract diagnostic counted the proof: Real.log occurs only in the initial
positivity step after defining ℓ. All subsequent arguments use positive weights. The same generic
proof works for rational weights and arbitrary finite indices; finite height/degree allocations
can reuse it without natural denominator/logarithm presentation. These are mathematical changes,
not a cosmetic rescaling of10. The recovered full original and actual caller guard against changing
meaning. See [concrete-diagnostic.json](../evidence/Roth.exists_degrees/concrete-diagnostic.json).

## Phase4.5 — infrastructure risks

| Risk | Verdict | Reason |
|---|---|---|
| Typeclass diamond | n/a | Theorem introduces no definitional equality, instance, coercion or universe-polymorphic structure. |
| Reducibility leak | n/a | Theorem introduces no definitional equality, instance, coercion or universe-polymorphic structure. |
| Noncanonical unfolding | n/a | Theorem introduces no definitional equality, instance, coercion or universe-polymorphic structure. |
| Instance priority | n/a | Theorem introduces no definitional equality, instance, coercion or universe-polymorphic structure. |
| Universes | n/a | Theorem introduces no definitional equality, instance, coercion or universe-polymorphic structure. |
| Coercion ambiguity | n/a | Theorem introduces no definitional equality, instance, coercion or universe-polymorphic structure. |

## Phase4.6 — proof strategy

| Question | Applies | Alternative | Cost |
|---|---|---|---|
| Topology | no | No topology | n/a |
| Algebra point-free | no | Scalar order estimates, no subobjects | n/a |
| Analysis sequence/filter | no | Direct finite ceiling estimate best matches quantitative outputs | n/a |
| Category universal property | no | No categorical construction | n/a |
| Missing helper API | yes | Finite positive-weight balancing plus separated relation corollary | New API; Nat.ceil_lt_mul covers only a scalar rounding bound. |

REFACTOR-RECOMMENDED: extract finite balancing and a margin corollary, then recover logarithmic
weights. Existing Nat.ceil_lt_mul may shorten the one-coordinate upper estimate during cleanup.
A filter proof via tendsto_nat_ceil_mul_div_atTop is possible, but finite intersection, choosing an
integer scale, base equality and strict-margin arithmetic still need proof. No filter rewrite was
falsely claimed as a three-call replacement.

## Phase5 — all15 formal cells

| Form | Method | Receipt | Result |
|---|---|---|---|
| current | leanfinder | [formal-current-leanfinder.json](../evidence/Roth.exists_degrees/formal-current-leanfinder.json) | Actual executed query; elementary ceiling/asymptotic candidates inspected. None supplies the full finite quantitative package as an existing call. |
| current | loogle | [formal-current-loogle.json](../evidence/Roth.exists_degrees/formal-current-loogle.json) | Actual executed query; elementary ceiling/asymptotic candidates inspected. None supplies the full finite quantitative package as an existing call. |
| current | leansearch | [formal-current-leansearch.json](../evidence/Roth.exists_degrees/formal-current-leansearch.json) | Actual executed query; elementary ceiling/asymptotic candidates inspected. None supplies the full finite quantitative package as an existing call. |
| current | rg | [formal-current-rg.json](../evidence/Roth.exists_degrees/formal-current-rg.json) | Actual executed query; elementary ceiling/asymptotic candidates inspected. None supplies the full finite quantitative package as an existing call. |
| current | local | [formal-current-local.json](../evidence/Roth.exists_degrees/formal-current-local.json) | Local index unhealthy/warming; only returned candidates, no absence inference. |
| standard | leanfinder | [formal-standard-leanfinder.json](../evidence/Roth.exists_degrees/formal-standard-leanfinder.json) | Actual executed query; elementary ceiling/asymptotic candidates inspected. None supplies the full finite quantitative package as an existing call. |
| standard | loogle | [formal-standard-loogle.json](../evidence/Roth.exists_degrees/formal-standard-loogle.json) | Actual executed query; elementary ceiling/asymptotic candidates inspected. None supplies the full finite quantitative package as an existing call. |
| standard | leansearch | [formal-standard-leansearch.json](../evidence/Roth.exists_degrees/formal-standard-leansearch.json) | Actual executed query; elementary ceiling/asymptotic candidates inspected. None supplies the full finite quantitative package as an existing call. |
| standard | rg | [formal-standard-rg.json](../evidence/Roth.exists_degrees/formal-standard-rg.json) | Actual executed query; elementary ceiling/asymptotic candidates inspected. None supplies the full finite quantitative package as an existing call. |
| standard | local | [formal-standard-local.json](../evidence/Roth.exists_degrees/formal-standard-local.json) | Local index unhealthy/warming; only returned candidates, no absence inference. |
| abstract | leanfinder | [formal-abstract-field-leanfinder.json](../evidence/Roth.exists_degrees/formal-abstract-field-leanfinder.json) | Actual executed query; elementary ceiling/asymptotic candidates inspected. None supplies the full finite quantitative package as an existing call. |
| abstract | loogle | [formal-abstract-field-loogle.json](../evidence/Roth.exists_degrees/formal-abstract-field-loogle.json) | Actual executed query; elementary ceiling/asymptotic candidates inspected. None supplies the full finite quantitative package as an existing call. |
| abstract | leansearch | [formal-abstract-field-leansearch.json](../evidence/Roth.exists_degrees/formal-abstract-field-leansearch.json) | Actual executed query; elementary ceiling/asymptotic candidates inspected. None supplies the full finite quantitative package as an existing call. |
| abstract | rg | [formal-abstract-rg.json](../evidence/Roth.exists_degrees/formal-abstract-rg.json) | Actual executed query; elementary ceiling/asymptotic candidates inspected. None supplies the full finite quantitative package as an existing call. |
| abstract | local | [formal-abstract-local.json](../evidence/Roth.exists_degrees/formal-abstract-local.json) | Local index unhealthy/warming; only returned candidates, no absence inference. |

Current means the full logarithmic quantitative result; standard means finite relative-error
ceiling rounding; abstract means arbitrary finite positive weights over an ordered floor field.
Additional abstract-field remote searches and one local retry are archived. Local states were
error/error/warming, followed by error on retry: returned candidates only, **no absence inference**.
Remote indexes may differ from the pin. Pinned source and native candidate checks establish the
actual signatures: Nat.le_ceil, Nat.ceil_lt_add_one, Nat.ceil_natCast, exists_nat_gt,
Finset.le_sup', Nat.ceil_lt_mul/ceil_le_mul, and tendsto_nat_ceil_mul_div_atTop.
The latter two kinds address scalar bounds or asymptotic convergence, not this synchronized
finite package. Dirichlet approximations and additive Roth numbers are different problems.
The untruncated qualified-name grep and compiled exact?/simp negative closure probe supplement
search; they do not logically prove no conceivable composition exists.

## Phase5.5 — statement shape

| Check | Assessment |
|---|---|
| Normal form | Use natural witnesses with weak lower product and strict upper product. Equivalent ratio/interval forms require positive divisions; conjunction packaging matches caller. |
| Syntactic generality | Finite ι, base b, arbitrary relation R, weights ℓ, tolerance ε, lower threshold B and growth c; specializes directly without changing old signature. |
| Superfluous arguments | δ≤1 removable from target with all outputs. Generic δ>0 was unused and removed; original δ>0 retained for ε,B. Redundant Archimedean removed. Fintype weakened to Finite. Caller δ≤1 is retained: used by the actual antitonicity/degree>=3 proof; no blanket mathematical necessity claim. |

RESTATE-BEFORE-SHIP: generic natural witness/product normal form; base b, independent ε,B and margin
c. Original signature remains the application interface in the tested recovery. No new class or
custom positivity predicate is introduced. Generic Finite replaces unused-in-type Fintype, and
FloorRing.archimedean infers Archimedean rather than retaining a redundant instance.

## Phase6.0 — callers and inline audit

Exactly one explicit proof call: Roth.exists_roth_approximants_aux at Main440, whole declaration
429–450; zero external-to-file calls. Main33 is documentation, not a proof call. Its complete body
was tested twice: literal original target proof inlined into the actual obtain, then the target
call replaced by the all-positive-delta recovery. Native equality checks preserve the exact original
private caller signature. Its δ≤1 remains for antitonicity and degree≥3. The terminal source closure
is roth_of_isIntegral→roth→roth_rat/LeanEval.thueSiegelRoth; no terminal replay is claimed.
[callers5-executed.lean.txt](../evidence/Roth.exists_degrees/callers5-executed.lean.txt); [callers.json](../evidence/Roth.exists_degrees/callers.json).
Fresh rg --no-ignore and tracked git grep agree; inline-pattern search found the source rounding
proof and consumers of its outputs, no independent duplicate degree selector.

## Phase6 — composition and duplication

NOT-COMPOSABLE from at most three existing mathlib calls on the verified evidence. Nat.ceil_lt_mul
needs a supplied one-coordinate lower threshold. Finset.le_sup' and exists_nat_gt choose a common
scale, but proving positivity, base equality, both products and strict relation preservation still
requires nontrivial multiplication/order reasoning. The compiled generic probe rejects simp and
exact? before writing the actual new proof. New balanced/separated helpers are **not** existing
mathlib replacements. The old recovery's one generic call is a call to our new theorem.

| A | B | Same statement | Same proof | Action |
|---|---|---|---|---|
| Roth.exists_degrees | Roth.exists_approximants | False | False | Complementary denominator selection versus degree rounding; do not unify. |
| Roth.exists_degrees | Nat.ceil_lt_mul | False | Partial ceiling estimate only | Reuse scalar candidate in future cleanup; finite synchronization/separation is new proof. |
| Roth.exists_degrees | tendsto_nat_ceil_mul_div_atTop | False | Asymptotic version of one-coordinate rounding | A finite quantitative theorem still needs scale selection and arithmetic assembly. |

## Phase7 — actionable verdict

YES-but-generalise-first, for verified weakening plus modern idiom. The concrete missing API is
finite synchronized natural rounding at a prescribed multiplicative tolerance and degree floor,
with a strict relation-margin corollary. Existing scalar ceiling and limit APIs do not discharge
that complete package. The known Roth degree choice supplies a concrete application; arbitrary
positive rational/real weights, finite index sets and independent tolerances are additional uses.
Retain the project wrapper until a generic upstream theorem is available, then replace its single
actual call using the exact tested recovery. Do not delete its required caller δ≤1 argument.

Proposed home: `Mathlib/Algebra/Order/Floor/Finite.lean`, a **new leaf** importing finite-supremum and
ordered-floor APIs. Floor.Semifield has assert_not_exists Finset, so placing this finite result
there would violate current import layering. Proposed PR title: **feat(Algebra/Order/Floor): balance
natural multiples of finite positive weights**. Group the new balanced theorem and separated
corollary together. Fresh accepted progress confirms YES for Roth.eventually_div_rpow_lt,
Roth.exists_reduced_approx and Roth.main_lemma; those belong to separate analytic/Diophantine or
project-theorem PRs, not this foundational floor API. No earlier verdict is inherited.

Before PR: `/generalise Roth.exists_degrees`; `/cleanup` on the new leaf/balancing lemmas; minimize
imports and split the constructive scale estimate if useful. Reviewer candidates based on actual
recent relevant commits: Yaël Dillies (a78f66ab84/e06eff5f95) or Seewoo Lee (caabe1c7b0). This is a
routing suggestion, not reviewer approval. See [reviewer-commits.json](../evidence/Roth.exists_degrees/reviewer-commits.json).

## Phase8 — evidence and limits

Root exclusively executed all native/project-LSP requests. Stable18 mathlib-only and disk9 controls
are archived and unchanged; only candidate06 adds the freshly authorized Floor.Semifield import; its exact19prefix/hash authorization is archived. No inherited exception is used. All
sources are at most100 columns. Required accepted proofs use only propext, Classical.choice and
Quot.sound. Rejected generic attempts and every preparation-only version remain separately
accounted for, including recovered sorryAx in failed generic01/04 (never accepted proof evidence).
[verification.json](../evidence/Roth.exists_degrees/verification.json); [prefix-controls.json](../evidence/Roth.exists_degrees/prefix-controls.json); [formal-search-matrix.json](../evidence/Roth.exists_degrees/formal-search-matrix.json).

Required native gates and draft validation have passed. Final current-manifest, both-layout and
secret-scan receipts accompany this frozen package. Root acceptance remains a separate pending review.
