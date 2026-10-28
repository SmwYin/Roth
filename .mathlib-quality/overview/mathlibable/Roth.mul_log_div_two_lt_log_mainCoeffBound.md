# Roth.mul_log_div_two_lt_log_mainCoeffBound — canonical239

Verdict: **BORDERLINE-needs-human**. Assessment complete; no unresolved verification obligations. The three questions below concern a future upstream API choice, and do not block this read-only assessment. Production sources and pins are unchanged. Root acceptance is pending independent review.

## Phase0: baseline and scope

The shared clean build completed2467 jobs. All17 production-source/pin SHA256 values were freshly matched before execution. No file-end build is due for239 (the accepted prior checkpoint was228; next266). The declaration resolves at `Roth/MainLemma.lean:149`, is public, has no `sorry`, and introduces no new instance. The module proves Roth's main lemma through coefficient rounding, pigeonhole counting and derivative/index bounds. The whole original module, including its actual caller, was read and replayed. No production/Git writes were made.

Evidence: [baseline](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/baseline-build.txt), [fresh17](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/inputs.json), [shared input manifest](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/input-manifest.json), [whole original module](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/source-MainLemma.lean.txt), [preparation gates](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/preparation-checks.json).

## Phase1: statement and proof

Let δ be real and q₁,r₁ be natural numbers, and put X=q₁^(δr₁). If X≥2, then log(floor₊X)>δr₁ log(q₁)/2. The floor makes an integer coefficient bound; the strict lower estimate survives the endpoint X=2. There are no separate δ≥0, r₁>0 or q₁>0 assumptions: the power lower bound supplies what logarithmic normalization needs.

Full native type, extracted through `Lean.getConstInfo` and `pp.funBinderTypes=true`:

```lean
∀ {δ : ℝ} {q₁ r₁ : ℕ},
  2 ≤ ↑q₁ ^ (δ * ↑r₁) →
  δ * ↑r₁ * Real.log ↑q₁ / 2 < Real.log ↑(Roth.mainCoeffBound δ q₁ r₁)
```

The proof first invokes `Roth.sqrt_lt_floor hX`. Since √X>0, `Real.log_lt_log` transports its strict lower bound. `Real.log_sqrt` and `Real.log_rpow` then produce the displayed arithmetic spelling. Base positivity is obtained from `Real.one_lt_rpow_iff`, with natural-cast nonnegativity. Project dependencies are exactly `Roth.mainCoeffBound` (unfolded notation) and `Roth.sqrt_lt_floor` (substantive rounding bound).

The full target kernel body is printed without an explicit printer-elision marker. The whole-module replay changes the namespace and renames only this theorem to `replay`; its kernel type is definitionally equal to the original. Full original target and replay axioms are standard (`propext`, `Classical.choice`, `Quot.sound`). The canonical293 list is generated from tracked declaration order: exact source order/uniqueness passed before execution and was rechecked at freeze; runtime293 requested,293 unique,293 present,293 values.

Evidence: [full native type](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/native-type.json), [original exact execution](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/original-executed.lean.txt), [complete original receipt](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/original-receipt.json), [canonical consumers](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/canonical-consumers.json).

## Phase2: preliminary classification

**SMALL**: a numerical helper, neither a named theorem nor a principal module result. Exhaustive literature width is unchanged. Definition-only one-line/exemption test: n/a, theorem. Its short source is not itself a composition verdict: one premise comes from a project theorem, and sign/coercion/logarithm normalization must be checked independently.

## Phase3: exhaustive literature

Each web receipt records the exact request, status, SHA256/byte length of the actual returned tool response, clean source titles/URLs, and an original concise summary. Full article/search bodies are not archived. Returned credential/query parameters are omitted; incomplete URLs are omitted without reconstruction. These requests were executed afresh.

| Channel | Actual query / locator | Finding |
|---|---|---|
| General1 | `logarithm floor x half log x square root floor inequality` | Elementary floor/log sources and DLMF; no exact named bridge identified. [receipt](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/web-general1.json) |
| General2 | `Roth theorem auxiliary polynomial coefficient bound floor q delta log B` | Diophantine Roth auxiliary-polynomial context, including original ICM proceedings and expository constructions. [receipt](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/web-general2.json) |
| General3 | `floor function logarithm lower bound rounding positive real numbers` | General rounding context; floor(log X) must be distinguished from log(floor X). [receipt](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/web-general3.json) |
| Optional mathematical second opinion | `ask_chatgpt_math` unavailable | Justified n/a; other channels still executed. |
| Local source | `clean.tex:1352–1389`, §6, eq.(37) and paragraph preceding `three-small-factors` | Defines B₁=floor(q₁^(δr₁)); derives its half-log lower bound from the square-root lower bound for X>4. [excerpt](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/literature-local-excerpt.txt), [input hash](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/literature-local-input.json) |
| nLab | `site:ncatlab.org/nlab floor logarithm monotone` | Floor and monotone-function entries; direct floor-page access returned unsupported XHTML HTTP400. [query](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/web-nlab.json), [access receipt](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/web-primary.json) |
| Distinct nCatLab | `site:ncatlab.org/ncatlab floor logarithm inequality` | Actual namespace query executed; search returned nLab pages outside requested namespace, not a verified nCatLab theorem. [receipt](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/web-ncatlab.json) |
| Stacks | `site:stacks.math.columbia.edu logarithm floor inequality` | Algebraic-geometry hits do not supply this real rounding/logarithm estimate. [receipt](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/web-stacks.json) |
| MathOverflow | `site:mathoverflow.net logarithm floor inequality` | Floor-function and logarithmic discussions; no matching reusable bridge identified. [receipt](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/web-mathoverflow.json) |
| Recent arXiv | `site:arxiv.org Roth theorem auxiliary polynomial coefficient bound after:2021-10-28 before:2026-10-29` | Recent additive-combinatorial namesakes distinguished from Diophantine Roth. Müller–Taktikos2026 concerns ABC-conditional effective constants, not this floor/log law. [query](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/web-arxiv.json), [abstract access](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/web-primary.json) |

Primary external locators: [DLMF §4.5(i)](https://dlmf.nist.gov/4.5) records classical logarithmic inequalities; it does not establish this particular natural-floor estimate. [Müller–Taktikos abstract and submission history](https://arxiv.org/abs/2601.11376) provide recent Diophantine context, without claiming a matching theorem. Local `clean.tex` is the exact mathematical source for the current application.

Literature synthesis: the concept is an elementary lower bound for the logarithm of an integer coefficient cutoff, obtained from floor approximation and logarithm monotonicity. No independent named theorem or uniquely preferred public log-floor interface emerged. The source uses X>4; Lean proves a stronger theorem using the weaker hypothesis X≥2. The representation q₁^(δr₁) is incidental to the generic real-X logarithmic bound; coefficient integrality remains meaningful.

## Phase4a–b: generality and actual proofs

All displayed proofs and boundary claims below compile with the exact18-import mathlib-only prefix and `#check_failure Roth.mul_log_div_two_lt_log_mainCoeffBound`. They introduce no Roth dependencies. The first rejected boundary draft is preserved separately, including its error diagnostics and recovered `sorryAx`; it is not accepted evidence.

| Parameter / assumption | Current role | Verified analysis |
|---|---|---|
| δ:ℝ | Scales the exponent | No extra δ sign premise needed. Absorb δr₁ into a single arbitrary real z. |
| q₁:ℕ | Natural denominator, cast to ℝ | `realPower` allows a nonnegative real base q; hX forces q>0. A compiled q=1/2,z=−1 witness proves this is a substantive widening, not merely a numeral spelling change. |
| r₁:ℕ | Natural degree | Only its appearance in the real exponent matters here. Arbitrary z removes the degree representation without changing the floor estimate. |
| hX:2≤q₁^(δr₁) | Rounding threshold and positivity | Cannot simply drop: q₁=r₁=δ=1 makes the strict conclusion false. Under X≥1 the generic bound holds iff X≥2. |
| mainCoeffBound | A natural floor of a power | Replace the named coefficient representation by genuine `Nat.floor` for generic upstream discussion; original specialization compiles. Parent definition composition alone does not settle this theorem's verdict. |
| 1/2 | Comes from the square-root law | Not an arbitrary semantic parameter. With c and an explicit X^c<B premise, the conclusion is already `Real.lt_log_of_rpow_lt`; that does not establish a floor estimate for arbitrary c. No optimality claim for the coefficient1/2. |
| ℝ and natural floor | Real logarithm/square-root domain; natural cutoff | No unsupported weakening to an arbitrary ordered ring with a logarithm. A generic monotone-function transport is existing order API, not a replacement for the numerical floor bound. |

Compiled proposed generic interfaces:

```lean
theorem logFloor {X : ℝ} (hX : 2 ≤ X) :
    Real.log X / 2 < Real.log (⌊X⌋₊ : ℝ)
theorem realPower {q z : ℝ} (hq : 0 ≤ q) (hX : 2 ≤ q ^ z) :
    z * Real.log q / 2 < Real.log (⌊q ^ z⌋₊ : ℝ)
```

Generality verdict: **STRICTLY NARROWER** than the verified generic real-X interface; coefficient-specific parameters are removable representations. The proof refactoring is local and compiled. This finding makes a generic interface a candidate; it does not itself establish that a separate public logarithmic lemma is desirable.

Boundary semantics are fully checked:

* X=1: both logarithms vanish, so strictness fails.
* 1≤X<2: floor₊X=1 and log X≥0, so strictness fails.
* X=2: strictness holds.
* 0<X<1: floor₊X=0 and Lean's total log0=0; log X<0 makes the written inequality true. This is not the intended positive coefficient-bound semantics.
* For X>0, the full exact criterion is `(X < 1 ∨ 2 ≤ X)`. Under X≥1 (equivalently positive natural floor for positive X), it is exactly `2 ≤ X`. Thus the threshold is sharp on the positive-floor domain, not globally on all positive reals.

Evidence: [isolated exact source](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/isolated-executed.lean.txt), [clean isolated receipt](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/isolated-receipt.json), [rejected boundary source](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/rejected-isolated-executed.lean.txt), [rejected boundary receipt](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/rejected-isolated-receipt.json).

## Phase4c: all nine modern-idiom checks

| # | Diagnostic | Answer and concrete consequence |
|---|---|---|
| 1 | Typeclasses instead of object premises | No: the sole premise is a numerical lower bound, not reusable structure. |
| 2 | Filters/nets instead of sequences | No sequence or limit in this pointwise inequality. |
| 3 | Universal-property characterization | No constructed object beyond an existing floor operation. |
| 4 | Bundled substructure | No closure predicate or algebraic subobject to bundle. |
| 5 | Weaker algebraic hierarchy | No justified scalar weakening of real log/sqrt. Generic order transport already exists but does not supply rounding. |
| 6 | Higher category reformulation | No categorical content. |
| 7 | Concrete indices | Yes: natural q,r only represent a real power; compiled realPower permits nonintegral bases and negative exponents. This composes directly with real-power/logarithm API. |
| 8 | Concrete-via-abstract proof diagnostic | Yes: `mainCoeffBound` occurs once in the proof, as an unfolding simp argument; after that only the generic floor/root/log bound remains. Generic logFloor applies to any positive real cutoff independent of denominators/degrees. |
| 9 | False-generalization guard | Passed for real-X/realPower forms with signs retained. Reject dropping hX, treating log0 as a positive cutoff, using arbitrary logarithms without monotonicity, or claiming arbitrary exponent c from X≥2. |

Modern idiom available: **yes**, abstract the coefficient witness to X. This removes q,r,δ-specific sign reconstruction from the reusable rounding/logarithm fact. It lets any real cutoff feed `Real.log_lt_log`/real-power estimates; no categorical embellishment is proposed. The half-base negative-exponent witness verifies actual additional coverage. API packaging still requires the Phase7 judgment.

## Phase4.5: infrastructure risk

All six rows are justified n/a for a theorem: typeclass diamond, reducibility leak, noncanonical definitional unfolding, instance priority collision, universe-polymorphism issue, and coercion-instance ambiguity. The theorem introduces no definitions or instances. Its uses of Nat→Real coercion are mathematical typing obligations already checked in the isolated and original-signature experiments, rather than new infrastructure paths.

## Phase4.6: proof strategy

| # | Strategy diagnostic | Finding |
|---|---|---|
| 1 | ε–δ vs filters | n/a; no topology argument. |
| 2 | Elements vs subobjects | n/a; scalar inequality, no algebraic inclusion. |
| 3 | Sequences vs nets | n/a; no convergence. |
| 4 | Construction vs universal property | n/a; no such construction. |
| 5 | Helpers that mathlib should have | Candidate: a generic natural-floor square-root lower bound, and possibly its logarithmic corollary. Verified rootFloor/logFloor are new scratch proofs, not existing library declarations. |

Current mathematical strategy is **MATHLIB-IDIOMATIC**: prove the rounding estimate, transport through a strictly increasing log, normalize log/sqrt/rpow. A generic real-X interface would make the coefficient specialization cleaner. The conditional outer transport is already small existing API; the numerical floor input is the substantive step. No cost-based verdict is used.

## Phase5: all15 formal search cells

External indices can differ from the pin; actual candidates were read in pinned sources and checked natively. Local name-index receipts say `warming`, so an empty or partial local result is not semantic absence. Every exact request/result and measured elapsed time is archived.

| Form | Lean-Finder | Loogle | LeanSearch | rg pinned source | Local name index |
|---|---|---|---|---|---|
| Current coefficient-power form | Real.log_natCast_le_rpow_div and unrelated Roth/Behrend bounds | Chebyshev floor/count bounds, not target | Int.log and floor(logb)/Nat.log identities; different order of operations | Full lexical log/floor sweep | Project target found; warming |
| Generic log X/2<log floor₊X | Nat/real logarithm comparisons; no matching target | No result | Int.div_two_lt_floor and Real.log_sqrt; partial matches | Includes floor-of-log-base and root/floor APIs | Harmonic/log-floor name hit is not target; warming |
| Abstract root/rpow→log transport | Real.lt_log_of_rpow_lt and log monotonicity | Real.log_sqrt | Real.log_lt_log, strictMonoOn_log | Existing transport signatures found | Real.log_sqrt found; warming |

The15 exact cells are enumerated in [matrix](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/formal-search-matrix.json); each row links its raw method receipt. The [full-name search](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/full-name-search.json) is untruncated. Relevant complete pinned files and their hashes are listed in [mathlib inputs](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/mathlib-inputs.json).

Specific existing candidates:

* `Real.log_lt_log`, `Log/Basic.lean:155`: requires a positive lower input and a strict input inequality.
* `Real.log_sqrt`, `Log/Basic.lean:303`: identifies log√X with logX/2 for X≥0.
* `Real.log_rpow`, `Pow/Real.lean:494`: requires a positive base.
* `Real.lt_log_of_rpow_lt`, `Pow/Real.lean:854`: requires a strict power bound, not merely hX.
* `Nat.le_floor`, `Floor/Defs.lean:141`, and `Nat.lt_floor_add_one`, `Floor/Semiring.lean:63`: yield floor≥2 and X<floor+1. Converting those to X<floor² uses a new quadratic argument.
* `Int.div_two_lt_floor` concerns X/2<integer floor; it does not give √X<floor for all X≥2, nor the target half-log estimate.

Conclusion: existing **building blocks and conditional transport** found. No direct matching pinned theorem or ≤3-existing-call proof of the original goal was established. Actual candidate probes compile: attempted direct calls with hX fail as expected, then a newly proved logFloor closes the goal. No broad numerical `exact?` was run after the documented prior timeout, and no universal absence claim is made.

## Phase5.5: statement shape

| Check | Attempt / result |
|---|---|
| Normal form | Original coefficient/log expression, generic log-floor inequality, and log-of-sqrt form compared. Existing canonical Nat.floor and Real.log are retained. logFloor is the suggested generic primary spelling if this API is added. The theorem is not an equivalence; RHS convention is n/a, with the useful floor bound remaining on the right. |
| Syntactic generality | logFloor, realPower, existingAbstract and existingExponent all compile. logFloor minimizes representation/coercion overhead; realPower is useful when the exponent product is already present. Original spelling remains practical for this project's sole caller. |
| Superfluous arguments | δ,q₁,r₁ all occur essentially in the original expression but can be absorbed into X. hX cannot be removed. No explicit typeclass or universe argument exists to drop. No additional positivity hypotheses should be added. |

Overall **RESTATE-BEFORE-SHIP** for a generic upstream proposal; current project theorem can remain as-is. Do not replace it by an alleged existing generalization that merely assumes the missing floor bound.

## Phase6.0: full callers, scope and inlining

| Caller | Exact occurrence and purpose | Verified future local action |
|---|---|---|
| `Roth.three_small_factors`, MainLemma:205 | `mul_lt_mul_of_pos_left (mul_log_div_two_lt_log_mainCoeffBound hX) hδ` inside local `key` | Insert the accepted `logBound` argument immediately after hX, then use `mul_lt_mul_of_pos_left logBound hδ`. hpow/hq make log normalization explicit. |

One same-file body occurrence; zero external-to-declaring-file uses; zero direct type consumers. The exhaustive canonical value audit independently finds exactly `Roth.three_small_factors`. Full inventory-scoped `rg --no-ignore` and tracked `git grep` agree. Inline-derivation search found no separate bypassing derivation. The theorem has no simp attribute; this does not make claims about every transitive or global simp dependency.

The entire original MainLemma module was replayed with the target declaration removed and the original mathematical argument inserted into its sole caller. A literal copied `simpa` proof initially failed in that larger context; the rejected exact source/receipt are preserved. The accepted proof supplies explicit hpow/hq and `simpa only` normalization. It is not a claim of verbatim unchanged proof text. Both `three_small_factors` and `main_lemma` have kernel types definitionally equal to their original signatures. Both checked values have no direct target constant. All original public/private declarations remain available through unchanged imports; full callers were checked, not schematic examples.

Evidence: [callers](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/callers.json), [source search](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/source-search.json), [tracked cross-check](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/tracked-source-search.json), [inline-derivation search](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/inline-search.json), [accepted full inline source](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/inline-executed.lean.txt), [clean inline receipt](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/inline-receipt.json), [rejected literal inline source](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/rejected-inline-executed.lean.txt), [rejected receipt](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/rejected-inline-receipt.json).

## Phase6: actual composition experiments

1. Existing outer transport succeeds with an explicitly supplied root bound:

```lean
(Real.log_sqrt hX.le) ▸ Real.log_lt_log (Real.sqrt_pos.mpr hX) hroot
```

This is at most three existing analytical calls once `hroot : √X < B` is given. Existing `Real.lt_log_of_rpow_lt hX hpower` also succeeds for arbitrary c with a supplied X^c<B. These isolate what mathlib already provides.

2. Neither transport accepts the original hX:2≤X as its root/power premise. Actual `fail_if_success` candidate probes verify the mismatch without broad wildcard search. The rootFloor scratch proof uses floor≥2, X<floor+1, a quadratic comparison and sqrt equivalence. logFloor then performs the existing transport. These are new proofs, not existing calls. Original specialization via realPower compiles independently of Roth.

3. Full original-caller inlining succeeds with explicit sign normalization. It proves local removability, not ≤3-call composition from existing mathlib. The inlined proof still uses the project square-root-floor estimate. Likewise, a `simpa [mainCoeffBound,…]` using a project parent cannot establish a NO verdict under the command's composition rule.

Conclusion: **NOT-COMPOSABLE as demonstrated from ≤3 existing mathlib calls for the original statement**. Conditional outer transport is composable; rounding input is not supplied by those calls. No claim of exhaustive semantic impossibility is needed for the BORDERLINE design judgment.

Moral-duplication comparison:

| A | B | Same statement? | Same argument? | Action |
|---|---|---|---|---|
| Assigned theorem | Roth.sqrt_lt_floor | No; logarithmic corollary of one component | Shares rounding input; adds positive-log transport and real-power normalization | Consider a primary generic floor/root API; do not inherit parent's verdict. |
| Assigned theorem | Real.lt_log_of_rpow_lt | No; library result assumes a power comparison | Same final transport, missing numerical floor premise | Reuse transport; no direct replacement claimed. |
| Assigned theorem | logFloor scratch | Original is a specialization after log_rpow/unfolding | Yes after representation bridge | Prefer generic X for any upstream proposal. |

## Phase7: verdict and concrete action

**BORDERLINE-needs-human.** The current coefficient-specific statement is a valid, used project helper. A mathematically broader real-X floor/log bound has been proved with exact strictness, coercions and boundary semantics. The existing library already supplies the outer log transport, while the generic rounding input is a short new proof. The evidence does not justify calling the original theorem an existing mathlib result or a ≤3-existing-call composition. It also does not establish an independently standard logarithmic API beyond the underlying floor/root estimate. The decision is whether that logarithmic corollary deserves its own public interface or should remain a client application of the primary rounding API. This is an upstream granularity/design question, not a cost or verification limitation.

Future upstream questions (assessment complete; no user response required now):

1. Should the generic natural-floor half-log bound be public API, or should clients apply log monotonicity to a primary square-root/floor estimate?
2. If a log-floor lemma is added, should its interface be the simple sufficient condition2≤X or the sharp positive-floor-domain equivalence under1≤X?
3. Should a real-base/arbitrary-real-exponent corollary be public, or should log_rpow normalization remain downstream at coefficient-bound call sites?

Provisional home if a generic log-floor API is chosen: a real logarithm/floor leaf near `Mathlib/Analysis/SpecialFunctions/Log/Basic.lean`, with imports reviewed rather than pushing logarithms into the algebraic Floor layer. This is not an accepted YES proposal or PR grouping. No prior useful declaration is treated as an accepted YES merely by its name.

Immediate action: retain production unchanged. In a future refactor, either keep this local coefficient-specialized helper in `Roth/MainLemma.lean`, or remove it and inline the verified `logBound` argument at its one `three_small_factors` occurrence. If an upstream log-floor lemma is selected, replace the inner rounding/log step by that generic theorem and retain the log_rpow representation bridge locally. The exact accepted inline source is reviewable now.

## Phase8: verification and package

Three clean native batches: full original module/kernel audit; independent mathlib-only generalization/transport/boundaries; full original caller inline replay. All accepted diagnostics are successful, complete and warning/error-free with standard axioms only. Both rejected attempts remain explicitly separate. The exact18 isolated prefix and nine persistent imports are unchanged. No `sorry`, new axiom, `unsafe`, `native_decide`, resource-limit raise, or partial native result is accepted.

The portable validator checks current manifest hashes/bytes, required metadata/phase keys, native requests/exact executed sources/axioms, source/pin hashes, exact canonical293 order/private modules/runtime counts, all15 formal cells, literature receipts, report links, and the secret guard. It resolves a report alongside scratch evidence and the published report outside the integrated evidence directory. Historical worker manifests never replace current validation.

Evidence index: [assessment](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/assessment.json), [verification](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/verification.json), [overview entry](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/overview-entry.json), [portable validator](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/validate.py), [current copy manifest](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/copy-manifest.json), [validation results](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/validation-result.json), [secret guard](../evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/secret-guard.json).
