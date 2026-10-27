# Roth.geom_sum_le_one_add_pow — declaration 96/293

**Verdict: YES-but-generalise-first (MODERN-IDIOM).** Add the finite geometric-sum bound over a partially ordered semiring, without multiplicative commutativity or characteristic-zero assumptions. The exact real statement is useful but unnecessarily concrete. The stronger proof and its complete private caller replay both verify with standard axioms. This assessment changes no production source or pin.

## Phase 0 — baseline and provenance

The shared baseline build completed successfully (2467 jobs). A fresh comparison matches all 17 source/pin SHA256 values; [input check](../evidence/Roth.geom_sum_le_one_add_pow/input-hash-check.json), [inputs](../evidence/Roth.geom_sum_le_one_add_pow/inputs.json), and [baseline](../evidence/Roth.geom_sum_le_one_add_pow/baseline-build.txt) preserve that evidence. The canonical tracked entry is index 96, public theorem, `Roth/CoeffNorm.lean:205`; [canonical metadata](../evidence/Roth.geom_sum_le_one_add_pow/canonical-order.json).

The entire declaring module, including its sole explicit caller and the subsequent `abs_eval_le` proof, was read and archived: [module](../evidence/Roth.geom_sum_le_one_add_pow/source-module.lean.txt). Root's native check prints the target's type, complete term and axioms: [original snippet](../evidence/Roth.geom_sum_le_one_add_pow/native-original-executed.lean.txt), [complete native receipt](../evidence/Roth.geom_sum_le_one_add_pow/native-original-receipt.json). No placeholders occur in the target.

## Phase 1 — comprehension

For a nonnegative real number t and natural number r, the sum of the first r+1 powers, including the constant term, is bounded by (1+t)^r. Expand the right side using the binomial theorem: the coefficient of every t^s, for 0≤s≤r, is a positive natural number and hence at least one. Nonnegativity of each power makes the termwise comparison valid.

Full native type:

```lean
∀ {t : ℝ}, 0 ≤ t → ∀ (r : ℕ),
  ∑ s ∈ Finset.range (r + 1), t ^ s ≤ (1 + t) ^ r
```

`t` is the base; `ht : 0 ≤ t` permits comparison after multiplication by `t^s`; `r` is the natural truncation degree. There are no project definitions, polynomial parameters, hidden finite-type hypotheses, or project-lemma dependencies in the theorem. The proof uses `add_pow`, `Finset.sum_le_sum`, `pow_nonneg`, `le_mul_of_one_le_right`, and `Nat.choose_pos` with range membership and natural casting.

## Phase 2 — preliminary checks

SMALL: an elementary coefficient comparison helper, not a new structure or a named main theorem. The definition-only one-line test and its three exemptions are n/a: this is a theorem. The present proof has six substantive tactic lines; brevity does not establish composition in the sense of Phase 6.

## Phase 3 — exhaustive literature

Exact requests, returned response hashes and byte counts are preserved without article/search-result bodies. The channels below were actually queried; supplementary primary-source checks are separate.

| Channel | Exact request / evidence | Result and locator |
|---|---|---|
| General web, specific | `geometric sum 1 x x^n less than (1+x)^n binomial coefficients` | Finite binomial expansion and coefficient comparison; [general receipt](../evidence/Roth.geom_sum_le_one_add_pow/web-general.json). |
| General web, abstract | `binomial theorem commuting elements semiring nonnegative inequality sum powers` | Primary formal sources explicitly allow commuting elements of semirings: [Metamath srgbinom](https://metamath.tirix.org/mpeuni/srgbinom) and [Agda semiring binomial module](https://agda.github.io/agda-stdlib/v2.0/Algebra.Properties.Semiring.Binomial.html). Search access succeeded; subsequent direct opens returned cache misses. |
| General web, aliases | `finite geometric series bound binomial theorem coefficients at least one` | Binomial theorem and geometric-series terminology; the inequality is a finite binomial comparison, not an infinite convergence theorem. Same general receipt. |
| ChatGPT mathematics | n/a: `ask_chatgpt_math` unavailable | No surrogate second-opinion claim. |
| Local references | Actual `rg` of `clean.tex` | Exact inequality and explanation in §6, Lemma 9 proof, lines 1545–1547 and Lean implementation note lines 1566–1568; [excerpt](../evidence/Roth.geom_sum_le_one_add_pow/local-literature-excerpt.txt), [source hash](../evidence/Roth.geom_sum_le_one_add_pow/local-literature-source.json). |
| nLab | `site:ncatlab.org/nlab binomial theorem semiring` | [Binomial theorem](https://ncatlab.org/nlab/show/binomial%2Btheorem), Statement and Combinatorial interpretation, includes the finite polynomial identity; [receipt](../evidence/Roth.geom_sum_le_one_add_pow/web-nlab-ncat.json). Its complex infinite-series version requires additional hypotheses and is not the proposed generalization. |
| nCatLab | `site:ncatlab.org/ncatlab binomial theorem geometric sum` | Returned nLab material, including binomial types and rig terminology. No categorical reformulation is needed for this ordered finite inequality. Actual request is in the same receipt; no assertion of exhaustive categorical absence. |
| Stacks | `site:stacks.math.columbia.edu binomial theorem` | Divided powers uses the binomial identity in algebra; [07GK](https://stacks.math.columbia.edu/tag/07GK), Lemma 23.2.2 proof. Direct page access succeeded in [primary retry receipt](../evidence/Roth.geom_sum_le_one_add_pow/web-primary-retry.json); this is contextual, not an exact ordered-inequality reference. |
| MathOverflow | `site:mathoverflow.net geometric sum binomial inequality (1+x)^n` | [Question 290050](https://mathoverflow.net/questions/290050/lower-upper-bounds-for-sum-limits-i-0k-binom-ni-xi), weighted partial binomial sums. Related but not an exact theorem; [receipt](../evidence/Roth.geom_sum_le_one_add_pow/web-stacks-mo.json). |
| Recent arXiv | `site:arxiv.org 2022 2023 2024 2025 2026 geometric sum binomial inequality`, then `site:arxiv.org binomial geometric sum inequality after:2021-10-27 before:2026-10-28` | Returned related binomial estimates, e.g. [Kovač 2206.01591](https://arxiv.org/abs/2206.01591), 2022-06-03, and [Hackl–Wagner 2403.09408](https://arxiv.org/abs/2403.09408), 2024-03-14. Their abstracts concern different inequalities; they do not establish this exact lemma or a stronger exponent type. [Initial](../evidence/Roth.geom_sum_le_one_add_pow/web-arxiv.json), [dated receipt](../evidence/Roth.geom_sum_le_one_add_pow/web-arxiv-dated.json). |
| Supplementary primary documentation | Direct opens of Metamath, Agda, official mathlib docs, Stacks | Metamath and Agda direct opens failed with cache miss, including Metamath retry; [initial failures](../evidence/Roth.geom_sum_le_one_add_pow/web-primary.json). Official [mathlib binomial documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Choose/Sum.html), `Commute.add_pow`, succeeded and agrees with pinned source; primary retry receipt above. |

Concept: finite geometric-sum bound by a binomial power. The exact real form is explicitly in the project's source paper. The algebraic binomial theorem is standard for commuting semiring elements; the ordered-semiring inequality is the order-compatible consequence verified here, rather than a claim that every source states that exact typeclass signature. Historically broader infinite binomial series and categorical binomial types are different extensions; neither justifies dropping the natural exponent or the positivity hypothesis.

## Phase 4a — parameters and generality

| Current datum | General form / essential use | Finding |
|---|---|---|
| Real base type | `R` with `[Semiring R] [PartialOrder R] [IsOrderedRing R]` | Verified strict widening; division, subtraction, completeness, totality and Archimedeanness are unused. |
| Multiplicative commutativity available in ℝ | Only `t` and `1` need commute | `Commute.one_right t` supplies it without `[CommSemiring R]`. |
| Characteristic zero available in ℝ | Need only monotonic natural casts | `Nat.mono_cast` transfers `1 ≤ r.choose s`; no injective cast or `[CharZero R]` needed. |
| `{t}` | Arbitrary semiring element | Keep implicit for inference from `ht`. |
| `ht : 0 ≤ t` | Nonnegative base | Essential to a uniform statement over all r; verified counterexample t=−1, r=2 gives 1≤0. |
| `(r : ℕ)` | Natural finite degree | Retain; range indexing and binomial coefficients use natural numbers; real exponents would change the object. |
| `range (r+1)` | Includes exponent r and constant term | Retain, including r=0. No nonzero-degree or t<1 hypothesis is needed. |

## Phase 4b — verified widening

STRICTLY NARROWER than the verified abstract form. Proposed upstream signature:

```lean
theorem geom_sum_le_one_add_pow [Semiring R] [PartialOrder R] [IsOrderedRing R]
    {t : R} (ht : 0 ≤ t) (r : ℕ) :
    ∑ s ∈ Finset.range (r + 1), t ^ s ≤ (1 + t) ^ r := by
  rw [add_comm (1 : R) t, (Commute.one_right t).add_pow]
  refine Finset.sum_le_sum fun m hm ↦ ?_
  rw [one_pow, mul_one]
  refine le_mul_of_one_le_right (pow_nonneg ht m) ?_
  simpa only [Nat.cast_one] using
    (Nat.mono_cast (α := R) (Nat.choose_pos (Finset.mem_range_succ_iff.1 hm)))
```

This is the strongest structure weakening actually verified in this assessment, not a claim of absolute minimal classes. It preserves the same sum, powers and inequality, requires one statement-level type abstraction plus the natural-cast adjustment, and specializes back to the real statement by `generic ht r`. The exact isolated [executed source](../evidence/Roth.geom_sum_le_one_add_pow/native-raw-executed.lean.txt) uses the stable 17 mathlib imports, guards absence of the project target with `#check_failure`, and checks the binomial/comparison/cast signatures; [successful raw receipt](../evidence/Roth.geom_sum_le_one_add_pow/native-raw-receipt.json). No Roth import or target theorem is used.

Two rejected attempts are retained separately: [initial source](../evidence/Roth.geom_sum_le_one_add_pow/rejected-raw-executed.lean.txt), [receipt](../evidence/Roth.geom_sum_le_one_add_pow/rejected-raw-receipt.json), failed `exact_mod_cast`, recovering `sorryAx`; this invalidates the attempt, not the semiring theorem. The correction uses monotonicity rather than unjustified cast order reflection. [Second source](../evidence/Roth.geom_sum_le_one_add_pow/rejected-raw-clean-executed.lean.txt), [receipt](../evidence/Roth.geom_sum_le_one_add_pow/rejected-raw-clean-receipt.json), had a correct proof but a leading-space command whitespace warning; the final source removes it. No rejected proof supports the verdict.

## Phase 4c — all nine modern-idiom checks

| # | Diagnostic | Answer and downstream consequence |
|---|---|---|
| 1 | Typeclasses instead of informal hypotheses | Yes: semiring/order classes express exactly the common algebra; instance inference permits ℕ, ℚ, ℝ, nonnegative scalar types and suitable noncommutative ordered semirings. |
| 2 | Filters/nets | No: no convergence or topology occurs. |
| 3 | Universal property | No object is constructed. |
| 4 | Bundled substructure | No closed subset predicate is involved. |
| 5 | Weaken field-specific hierarchy | Yes: semiring/partial order suffices; no inverses or cancellation are used. |
| 6 | Higher categories | No categorical statement or downstream need. |
| 7 | Concrete index | Keep ℕ as finite natural exponent; abstract the value type, not the index. |
| 8 | Concrete-via-abstract adversarial check | Yes: the proof's ℝ identifier occurs in one annotation on the first rewrite and never afterward. All subsequent steps are abstract finite-sum, positivity and natural-coefficient facts. Verified raw proof confirms the diagnostic; the old real theorem becomes a one-call specialization of a *new* theorem, not of existing mathlib. |
| 9 | False-generalization guard | Passed for semiring abstraction: same operations and inequality; `t` commutes with one. Rejected hypothetical dropping `ht`, with a checked counterexample, and real/infinite exponent variants, which change the finite object. |

MODERN-IDIOM is available and verified. It enables the ordered-semiring multiplication and finite-product APIs directly without embedding into ℝ; the complete existing product caller was replayed successfully. This is a cheap mechanical algebra abstraction, with a meaningful noncommutative and non-characteristic-zero interface.

## Phase 4.5 — infrastructure risk

n/a: theorem. Typeclass diamond, reducibility leak, noncanonical unfolding, instance priority collision, universe-polymorphism and coercion ambiguity do not arise from a new definition or instance here. The six rows are recorded as justified n/a in [generality evidence](../evidence/Roth.geom_sum_le_one_add_pow/generality.json).

## Phase 4.6 — five proof-strategy checks

| # | Strategy question | Finding |
|---|---|---|
| 1 | Topology / filters | No topology. |
| 2 | Algebra / substructures | No ideal or submodule inclusion; termwise order comparison is the natural proof. |
| 3 | Analysis / sequences | No analytic limiting process. |
| 4 | Categories / universal properties | No construction needing characterization. |
| 5 | Missing helpers mathlib should have | The missing reusable layer is this finite geometric/binomial bound itself; binomial expansion, coefficient positivity and cast monotonicity already exist. No separate speculative helper is needed. |

MATHLIB-IDIOMATIC strategy after the verified type abstraction: expand the binomial power and compare summands. No strategy change based on cost or proof-line counting.

## Phase 5 — actual five-method mathlib search

All external formal requests and complete responses are in [formal-search.json](../evidence/Roth.geom_sum_le_one_add_pow/formal-search.json), with twelve individual raw receipts. External indices may have different revisions; every positive building block used in the proof is checked against the pin.

| Method | Current form | Literature-standard form | Abstract form |
|---|---|---|---|
| Lean-Finder | Nonnegative real geometric sum ≤ binomial power | Finite geometric sum/binomial bound in ordered semirings | `Commute.add_pow` noncommutative ordered-semiring bound |
| Loogle | `"geom", _ ≤ (1 + _) ^ _` | `Finset.sum, Nat.choose, _ ≤ _ ^ _` | `Commute, (_ + _) ^ _ = _` |
| LeanSearch | Real finite sum natural-language request | Ordered-semiring sum and positive binomial coefficients | Binomial theorem for commuting elements of a noncommutative semiring |
| rg pinned source | `geom_sum_le`, range-power bound variants | Geometric bounds and Bernoulli forms | `Commute`, `add_pow`, ordered power APIs |
| Local name search | `geom_sum` | `sum_le_pow` | `add_pow` |

Loogle's current and standard queries returned no hits. Finder/LeanSearch suggested Bernoulli inequalities (`one_add_mul_le_pow`, its variants), `pow_add_pow_le'`, and `geom_sum_Ico_le_of_lt_one`; they bound different expressions or need t<1, so are not replacements. The `Nat.geom_sum_le` hit bounds a sum of natural quotients, not our polynomial. Some external results use older names; that is not treated as pinned presence. Local searches returned source matches but explicitly reported `index: unavailable`, so no absence inference is made from an empty result.

The abstract queries positively identified `Commute.add_pow` and `add_pow`, located at `Mathlib/Data/Nat/Choose/Sum.lean:34,76`, plus its antidiagonal variant at line 68. These are expansion identities, not the desired inequality. Pinned-source [abstract search](../evidence/Roth.geom_sum_le_one_add_pow/rg-abstract.json), [current](../evidence/Roth.geom_sum_le_one_add_pow/rg-current.json), [literature](../evidence/Roth.geom_sum_le_one_add_pow/rg-literature.json), and [untruncated full-name search](../evidence/Roth.geom_sum_le_one_add_pow/rg-full-name.json) preserve actual command output. [Mathlib source hashes](../evidence/Roth.geom_sum_le_one_add_pow/mathlib-inputs.json) cover the inspected binomial, casting, ordered-ring and geometric APIs.

Search conclusion: found existing building blocks and near misses; no exact existing replacement was identified. This is not a universal absence proof. No failed or timed-out `exact?` is offered as absence evidence; no optional negative proof search was executed. The positive raw proof describes precisely the missing comparison layer.

## Phase 5.5 — statement shape

Normal form OK after type abstraction: finite `range (r+1)` sum on the left, `(1+t)^r` on the right, matching `Commute.add_pow` and the existing caller. An equivalent `Finset.Icc 0 r` formulation would require an index bridge; a sum over `Fin (r+1)` is also possible, but offers no application advantage here. Neither alternative is claimed natively verified. Syntactic choice: retain implicit t, explicit r, `ht` first, matching `(abs_nonneg (x j)) (r j)` at the caller. A nonnegative subtype would make `ht` implicit but force coercions at the existing real caller; it is a specialization of the proposed generic interface.

Superfluous arguments: none of t, r, ht can simply disappear from the same formula uniformly for all natural r; the concrete real structure can be weakened as verified. No ambient σ leaked into the full type. Overall RESTATE-BEFORE-SHIP: the semiring value type is the only proposed statement change.

## Phase 6.0 — callers and inline audit

There is **one explicit source use**, in the same module: `Roth/CoeffNorm.lean:218`, inside private `sum_box_prod_pow_le_aux`, comparing each coordinate's geometric sum before applying `Finset.prod_le_prod₀` and multiplication by nonnegative B. Therefore the command's external-to-declaring-file count is 0 and total source caller count is 1. The helper is subsequently called by `abs_eval_le` at line 239; this is an indirect use of the target, not a second direct call.

[Callers rg](../evidence/Roth.geom_sum_le_one_add_pow/rg-callers.json), [inline search](../evidence/Roth.geom_sum_le_one_add_pow/rg-inline.json) show the actual source matches. The source audit found no separate inline rederivation of this geometric-binomial bound outside its own proof; this is limited to the explicit searches, not a theorem about all semantic equivalents.

The runtime kernel audit checked the exact ordered canonical 293-name array generated directly from tracked JSON, preserving private names. It found 293 unique names, all present and all with values, and exactly one direct proof consumer:

```text
_private.Roth.CoeffNorm.0.Roth.sum_box_prod_pow_le_aux
```

[Executed caller and audit source](../evidence/Roth.geom_sum_le_one_add_pow/native-consumers-executed.lean.txt), [complete receipt](../evidence/Roth.geom_sum_le_one_add_pow/native-consumers-receipt.json), [canonical snapshot](../evidence/Roth.geom_sum_le_one_add_pow/canonical-snapshot.json). This is a direct proof-value dependency audit, not transitive closure. The array was not modified by replacing a global target string.

## Phase 6 — actual composition experiments

Attempt 1, existing binomial APIs: the successful mathlib-only proof expands `(1+t)^r`, compares every summand, establishes nonnegativity of powers, obtains positivity of each binomial coefficient from the range bound, and transports its lower bound using a monotone natural cast. It requires rewriting and more than three existing calls (`Commute.add_pow`, `Finset.sum_le_sum`, `pow_nonneg`, `le_mul_of_one_le_right`, `Nat.choose_pos`, `Finset.mem_range_succ_iff`, `Nat.mono_cast`, plus normalization). This is a proof, not a ≤3-call composition and not a closing simp composition. No new helper is counted as existing mathlib.

Attempt 2, exact old-form recovery: the final raw source verifies `generic ht r` over ℝ. This is a one-call corollary of the *newly proved* generic theorem, so it does not support a NO verdict.

Attempt 3, full caller transplant: root executed the complete private box-bound proof with the new generic bound. The target theorem is not called by that replay. `box_consumer` verifies with standard axioms; its existing product/multiplication normalization is unchanged. This establishes a concrete downstream use of the proposed abstract API rather than asserting that an analogous statement should elaborate.

No ≤3-existing-call replacement was established; the verified binomial comparison uses the listed facts. For the Phase 6 classification, the demonstrated route is NOT-COMPOSABLE in the prescribed short-composition sense. The positive comparison proof supplies the specific missing API. Single project use is a weak audience signal, but cannot override a verified general reusable inequality or manufacture a shorter existing composition.

## Phase 7 — actionable verdict

**YES-but-generalise-first, reason MODERN-IDIOM.** The exact paper inequality is elementary and reusable wherever geometric finite sums arise. Mathlib has the semiring binomial identity and the ordered comparison ingredients but the inspected geometric API instead treats geometric-series formulas, sign classification, and bounds for t<1. The proposed lemma fills the explicit gap between binomial expansion and an unweighted finite geometric bound without a ratio restriction. The algebraic abstraction is compiled and does not require cancellation, total order, commutative multiplication, or faithful natural casting.

Proposed upstream location: `Mathlib/Algebra/Order/Ring/GeomSum.lean`. Proposed PR title: `feat(Algebra/Order/Ring/GeomSum): bound finite geometric sums by binomial powers`. Add the appropriate binomial import if needed; confirm the dependency remains acyclic. Proposed public name: `geom_sum_le_one_add_pow` (confirm orientation/naming in review). Proof shown in Phase 4b is complete, with no placeholders.

Grouping: keep this small ordered-semiring addition separate from the already accepted Hasse-derivative and coefficient-norm developments. Related accepted YES declarations include `Roth.abs_coeff_hasseDeriv_le` and `Roth.normOne_hasseDeriv_le`, but they concern polynomial coefficient estimates and should consume elementary order APIs rather than force an unrelated combined PR. [Progress-derived grouping evidence](../evidence/Roth.geom_sum_le_one_add_pow/accepted-yes-grouping.json) records all accepted YES entries at completed count 95; no useful-looking name was presumed YES.

Before opening:

- [ ] `/generalise Roth.geom_sum_le_one_add_pow`: confirm the verified semiring signature, in particular preserve `ht` and use `Nat.mono_cast` rather than requiring `CharZero`.
- [ ] `/cleanup Roth/CoeffNorm.lean Roth.geom_sum_le_one_add_pow`: full declaration audit and diff gates; then clean the upstream candidate at its proposed file.
- [ ] Seek a relevant reviewer: Moritz Firsching recently changed binomial-bound organization (`9cb3970b1f`, 2026-09-14); Yaël Dillies recently documented ordered-semiring hierarchy changes (`64f7dc5fc8`, 2026-06-17). [Fresh relevant-file git log](../evidence/Roth.geom_sum_le_one_add_pow/reviewer-log.json). These are reviewer candidates based on actual activity, not a claim of ownership or availability.
- [ ] After the upstream API is available, replace the call at `Roth/CoeffNorm.lean:218` with its general mathlib name (same ht/r argument flow) and remove the project specialization, using the verified full private caller replay as the migration template. Until then the natural local destination is the present coefficient-bound module; the theorem is not dead code.

No production edit or upstream PR is made by this read-only assessment. The verified weakening is CHEAP; cost is not the verdict criterion.

## Phase 8 — verification and handoff

All requested phases are complete, with theorem-only n/a justified above. [Verification index](../evidence/Roth.geom_sum_le_one_add_pow/verification.json) links three accepted native sets and two rejected sets; accepted proofs use only `propext`, `Classical.choice`, `Quot.sound`. Original and caller runs explicitly report `partial=false`; isolated raw runs report completed success, no timeout, no diagnostics of error/warning severity. Root's full historical disk receipts are preserved unchanged, while executed-source archives retain original execution paths in receipts. No new axioms, sorry, unsafe/native decision, or raised limits are accepted.

[Assessment](../evidence/Roth.geom_sum_le_one_add_pow/assessment.json), [overview entry](../evidence/Roth.geom_sum_le_one_add_pow/overview-entry.json), [current artifact manifest](../evidence/Roth.geom_sum_le_one_add_pow/copy-manifest.json), [portable validator](../evidence/Roth.geom_sum_le_one_add_pow/validate.py). The validator resolves these `../evidence/<declaration>/...` links in scratch and integrated layouts and checks the current manifest, exact canonical order, input hashes and native success evidence. Root acceptance remains pending until independent review; unresolved verification items: none.
