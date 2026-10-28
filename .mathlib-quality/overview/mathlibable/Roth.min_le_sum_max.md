# Roth.min_le_sum_max — declaration 206

**BORDERLINE-needs-human.** The unconditional finite positive-part estimate is useful in the paper's argument, but the evidence establishes only one project consumer and no independent demand for this particular pair of constants. There is a verified, stronger natural-scale estimate and a more general ordered-field statement. Neither the new branch proofs nor their short assembly count as existing mathlib replacements. No production edits were made.

## Phase 0 — Baseline

The successful shared `lake build` completed 2467 jobs. All 17 production-source and pin hashes freshly match its input manifest; source files and pins remain unchanged. The target resolves at `Roth/Theta.lean:362`, is a public theorem, and has no `sorry`. Read the entire 985-line declaring module, the sole caller and surrounding determinant/index argument.

Evidence: [baseline](../evidence/Roth.min_le_sum_max/baseline-build.txt), [fresh hashes](../evidence/Roth.min_le_sum_max/source-hashes.json), [source](../evidence/Roth.min_le_sum_max/source-Theta.lean.txt), [native audit](../evidence/Roth.min_le_sum_max/minsum206-original-receipt.json).

## Phase 1 — Mathematical content and exact type

For every real θ and natural numbers r and l, the sum of the nonnegative parts of θ−ν/r, for 0≤ν<l, is at least the smaller of lθ/2 and rθ²/3. There are **no positivity or size hypotheses**: l=0, r=0 and negative θ are included. Division by zero has Lean's field meaning.

The full native elaborated type is:
```lean
∀ {θ : ℝ} {rp : ℕ} (l : ℕ),
  min (↑l * θ / 2) (↑rp * θ ^ 2 / 3) ≤
    ∑ ν ∈ Finset.range l, max 0 (θ - ↑ν / ↑rp)
```

θ is the scalar height; rp is the scale/denominator; l is the finite truncation length. The ambient Fintype/DecidableEq/variable-index parameters in the file do not occur in the kernel type.

For θ≤0, the linear expression is nonpositive and each summand is nonnegative. Otherwise split at l≤θr: the short branch uses the arithmetic-progression sum and gives lθ/2; the long branch cuts off at a natural approximation to θr and gives rθ²/3. The original body calls the two private project lemmas `mul_div_two_le_sum_max_aux` and `mul_sq_div_three_le_sum_max_aux`; the latter calls the positive-scale private branch. These are project dependencies, **not existing mathlib building blocks**.

## Phase 2 — Preliminary checks

SMALL: an elementary numerical helper in the proof of Lemma 6, not a main theorem or named structure. The one-line-definition test and all its exemptions are n/a: this is a theorem with a substantive case split. The short final assembly hides genuinely new branch estimates.

## Phase 3 — Exhaustive literature

All named channels were attempted. Search evidence retains exact requests, response digests/status, result titles/URLs/locators and original concise summaries; no full web bodies were persisted. Dates refer to this assessment on 2026-10-28.

| Channel | Actual query / locator | Finding |
|---|---|---|
| General web, specific | `"Roth" "sum" "max" "theta" "Lemma 6" inequality` | Mostly unrelated uses of Roth; no exact numeric bound. |
| General web, general | `finite sum positive parts decreasing arithmetic progression lower bound triangular sum` | Standard arithmetic-series identity, notably Canadian Mathematical Society §2.2. |
| General web, aliases | `truncated arithmetic progression positive part sum lower bound min quadratic linear` | Arithmetic progressions/triangular sums and unrelated counting results; no named standard minimum theorem. |
| Optional mathematical consultation | Standard form/generality/historical-evolution question | n/a: ask_chatgpt_math unavailable; no substitute answer invented. |
| Local reference | `clean.tex` §5, proof of Lemma 6, lines 841–927 | Exact source minimum after the two cases, with θrp>10 and positive weights. |
| nLab | `site:ncatlab.org/nlab positive part ordered field finite sum inequality` | Ordered field/ring foundations; no exact estimate. |
| nCatLab | `site:ncatlab.org/ncatlab positive part ordered ring inequality` | Query executed distinctly; returned /nlab and other host paths, no in-namespace exact hit. |
| Stacks | `site:stacks.math.columbia.edu arithmetic progression sum inequality` | Algebraic-geometry excerpts, no relevant numeric bound. |
| MathOverflow | `site:mathoverflow.net sum positive parts arithmetic progression lower bound` | Progression/counting questions, not this result. |
| Recent arXiv | `site:arxiv.org Roth theorem index polynomial arithmetic progression sum max after:2021-10-28 before:2026-10-29` | Nonlinear/additive-combinatorial Roth and unrelated analytic results; no exact Diophantine-index estimate. |

See [general requests](../evidence/Roth.min_le_sum_max/web-0.json), [nLab/nCatLab](../evidence/Roth.min_le_sum_max/web-1.json), [Stacks/MO](../evidence/Roth.min_le_sum_max/web-2.json), [recent arXiv](../evidence/Roth.min_le_sum_max/web-3.json), [local search](../evidence/Roth.min_le_sum_max/local-literature-search.json), [exact local excerpt](../evidence/Roth.min_le_sum_max/clean-lemma6-excerpt.tex.txt).

The local source supplies the exact paper-facing statement, while the [CMS arithmetic-sums source](https://cms.math.ca/wp-content/uploads/2023/02/atom14.pdf) supplies the underlying standard identity in §2.2.1. No external source located establishes the arbitrary-scale ordered-field version or a canonical modern name for these constants. The generic version below is a verified mathematical development of that elementary identity, not an attributed literature theorem. The two floor FACTs in the source lose information; the direct remainder proof improves the quadratic coefficient.

## Phase 4a — Every parameter and assumption

| Parameter / constraint | Audit and verified outcome |
|---|---|
| θ : ℝ | Real completeness and analysis unused; generalized to arbitrary ordered field K. All signs allowed. |
| rp : ℕ | Integrality not needed for either /3 or /2 estimates: arbitrary scale rp : K verified, including negative and zero scale. |
| l : ℕ | Natural finite length retained; l=0 included. Arbitrary group index would change the interval/counting object; no such claim. |
| No hypotheses | No hidden θ≥0, rp>0, l>0 or θrp>10 to weaken. These are internal branches or paper assumptions, never target premises. |
| Ordered-field operations | Field, LinearOrder, IsStrictOrderedRing verified. Subtraction, division, square and total order remain meaningful interface requirements. No minimal hierarchy claim. |
| FloorSemiring | First verified with it, then removed by finite `Nat.findGreatest` cutoff bounded by l; no Archimedean or floor instance required. |
| Constants | /2 quadratic estimate verified. It strengthens the **original natural-scale** /3 result; the coefficients are not ordered the same way for negative rp. |

## Phase 4b — Mechanically verified restatements

[Independent isolated proof](../evidence/Roth.min_le_sum_max/minsum206-isolated-executed.lean.txt) and [clean receipt](../evidence/Roth.min_le_sum_max/minsum206-isolated-receipt.json) prove the original /3 minimum over a Field/LinearOrder/IsStrictOrderedRing with FloorSemiring and arbitrary scalar scale. Its real-scale and natural-scale specializations compile.

The stronger final candidate, [finite cutoff proof](../evidence/Roth.min_le_sum_max/minsum206-finite-executed.lean.txt), has this signature:
```lean
theorem generic {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    {θ rp : K} (l : ℕ) :
    min (l * θ / 2) (rp * θ ^ 2 / 2) ≤
      ∑ ν ∈ Finset.range l, max 0 (θ - ν / rp)
```

In the positive long branch set n=findGreatest (fun k : ℕ ↦ (k:K)≤θr) l. The zero witness proves n≤θr; casting gives n<l; maximality at n+1 gives θr<n+1. After the Gauss identity, the remainder certificate is
`hsum/2 + a/2 + (a−n)(n+1−a)/2`,
with each non-identity term nonnegative. This proves the /2 quadratic bound without a floor structure. Original natural-rp /3 follows from min monotonicity and nonnegativity of rpθ², then the new /2 theorem. The scratch helper names containing “three” were mechanically retained in the /2 experiment; their exact statements and proofs use /2.

[Clean finite receipt](../evidence/Roth.min_le_sum_max/minsum206-finite-receipt.json); [initial floor-based /2 experiment](../evidence/Roth.min_le_sum_max/minsum206-stronger-executed.lean.txt). These are **new proofs**, including the bounded-cutoff bridge. Current form is verified narrower than the modern algebraic candidate, with an additionally weaker quadratic constant for natural scale. No sharp-constant or maximal-generality assertion is made. Cost is not a verdict factor.

## Phase 4c — Nine modern-idiom rows

| # | Question | Answer, reformulation and downstream effect |
|---|---|---|
| 1 | Typeclass preambles | Yes: ordered-field classes express the arithmetic setting; no custom structures/instances are introduced. |
| 2 | Filters/topology | No: finite arithmetic inequality, no limit or topology. |
| 3 | Universal properties | No object is constructed by a universal property; the cutoff is bounded finite search. |
| 4 | Bundled substructures | No closure predicate or substructure; no benefit from bundling θ/r. |
| 5 | Hierarchy weakening | Yes: ℝ→Field/LinearOrder/IsStrictOrderedRing, with FloorSemiring subsequently eliminated. Enables reuse over ℚ and non-Archimedean ordered fields without importing real analysis. |
| 6 | Higher categories | No categorical content or compositional benefit. |
| 7 | Concrete indices | Yes for scale rp:ℕ→K, preserving the same quotient and summands. Natural ν,l remain the finite counting index. |
| 8 | Concrete-via-abstract | Diagnostic fires: target body has zero `Real.` API occurrences and one ℝ annotation. It uses order/signs and branch bounds. Independently generalizing all branch proofs verifies the abstract content; original endpoint is a proved corollary. |
| 9 | False-generalization guard | Same field arithmetic and natural finite range retained. Dropping min is false: linear branch fails at θ=r=1,l=4; quadratic branch at θ=2,r=3,l=0. Strict inequality fails at l=0; dropping max fails at θ=r=1,l=4. Native counterexamples compile. |

See [body diagnostic](../evidence/Roth.min_le_sum_max/proof-body-audit.json). The strengthened /2 formula also permits arbitrary negative scale, but comparing /2 to /3 requires sign care: the **original endpoint bridge** explicitly uses Nat.cast_nonneg. These are meaningful wider applications, not a claim that the literature supplies a ready-made abstraction.

## Phase 4.5 — Infrastructure risks

n/a — theorem, no new definitional equality or instance path.

| Risk | Disposition |
|---|---|
| Typeclass diamond | n/a: proposition proof introduces no instance. |
| Reducibility leak | n/a: no computational definition exported. |
| Noncanonical unfolding | n/a: no new definitional interface. |
| Instance priority | n/a: no instance declaration. |
| Universe constraints | n/a for original real endpoint; generic proof is universe-polymorphic in K. |
| Coercion ambiguity | n/a: existing natural casts and field operations only. |

## Phase 4.6 — Five proof-strategy rows

| # | Question | Finding |
|---|---|---|
| 1 | ε–δ versus filters | n/a: no topology. |
| 2 | Elements versus subobjects | n/a: scalar inequality and finite sum, no ideal/submodule relation. |
| 3 | Sequences versus nets | n/a: finite range, no convergence. |
| 4 | Construction versus universal property | n/a: finite maximization, no categorical characterization. |
| 5 | Missing helper API | Potentially a positive-part arithmetic-progression estimate, preferably /2 and generic ordered-field form. All branch estimates in this evidence are new; desirability as public mathlib API remains unestablished. |

REFRACTOR-RECOMMENDED **if upstreamed**: use the floor-free bounded cutoff and strengthened natural-scale theorem. This gives exact arithmetic control without the paper's two lossy floor FACTs. An integral comparison is mathematically possible for reals but introduces integration and antitonicity plus an integral computation, and loses the generic field interface. No unsupported claim that that route is a three-call proof.

## Phase 5 — All fifteen actual mathlib search cells

Every cell has an exact request/raw response or complete CLI receipt. External search snapshots may differ from the pin; positive arithmetic/floor/min APIs were checked and used in clean Lean snippets. Local results say **index warming**, so they are not global absence certificates.

| Form | Finder | Loogle | LeanSearch | rg | local |
|---|---|---|---|---|---|
| Current minimum/positive-part sum | [0](../evidence/Roth.min_le_sum_max/search-0.json): theta-kernel/recurrence bounds, no replacement | [1](../evidence/Roth.min_le_sum_max/search-1.json): unqualified min error; [qualified retry12](../evidence/Roth.min_le_sum_max/search-12.json) returns lattice/sum results | [2](../evidence/Roth.min_le_sum_max/search-2.json): Schlömilch and unrelated estimates | [current](../evidence/Roth.min_le_sum_max/rg-current.json): Gauss identity | [3](../evidence/Roth.min_le_sum_max/search-3.json): own project theorem only |
| Standard truncated arithmetic progression | [4](../evidence/Roth.min_le_sum_max/search-4.json): condensed/Schlömilch sums | [5](../evidence/Roth.min_le_sum_max/search-5.json): unqualified max error; [qualified retry13](../evidence/Roth.min_le_sum_max/search-13.json) returns norm-difference bounds | [6](../evidence/Roth.min_le_sum_max/search-6.json): Schlömilch and sum-integral comparison | [standard](../evidence/Roth.min_le_sum_max/rg-standard.json): arithmetic-series infrastructure | [7](../evidence/Roth.min_le_sum_max/search-7.json): sum_range_id and sum_range_id_mul_two |
| Abstract ordered field/affine positive parts | [8](../evidence/Roth.min_le_sum_max/search-8.json): Young/square and weighted pigeonhole estimates | [9](../evidence/Roth.min_le_sum_max/search-9.json): min_le_iff | [10](../evidence/Roth.min_le_sum_max/search-10.json): affine/valuation/nonnegative sums | [abstract](../evidence/Roth.min_le_sum_max/rg-abstract.json): min and sum-integral infrastructure | [11](../evidence/Roth.min_le_sum_max/search-11.json): nonnegative subset sum monotonicity |

[Untruncated full-name rg](../evidence/Roth.min_le_sum_max/rg-full-name.json) returns no mathlib occurrence of min_le_sum_max. This concerns the spelling, not mathematical absence.

Pinned positive APIs include `Finset.sum_range_id_mul_two` (Intervals:171), `Finset.sum_le_sum_of_subset_of_nonneg`, `min_le_iff`, and, in the initial route, `Nat.floor_le`, `Nat.lt_floor_add_one`, `Nat.floor_lt`. The final route checks and uses `Nat.findGreatest_spec` and `Nat.findGreatest_is_greatest` (Data/Nat/Find:210,247). Exact source archives are hash-pinned in [mathlib inputs](../evidence/Roth.min_le_sum_max/mathlib-inputs.json). None already states the arithmetic estimate. The partial hits in SumIntegralComparisons and PSeries do not compute this clipped affine sum or its quadratic lower bound.

Conclusion: no verified existing theorem or ≤3-existing-call replacement established. Searches and failed automation do not prove global absence.

## Phase 5.5 — Three statement-shape checks

1. **Normal form:** min(A,B)≤S is equivalent to A≤S∨B≤S by min_le_iff. The min bound composes directly by transitivity with the caller's determinant-sum estimate; the disjunction would move case handling into the caller. max 0 x agrees with the usual positive-part notation after order normalization, but changing notation alone adds no mathematical content.
2. **Syntactic generality:** arbitrary scalar scale and /2 quadratic term are the verified preferred candidate. Natural range ν<l retains exact indexing; a Fin l sum is an equivalent indexing convenience. Keep ≤: strict fails at zero length.
3. **Superfluous hypotheses:** original has none; ambient Fintype/DecidableEq are absent in native type. Real completeness, naturalness of scale and the initially introduced FloorSemiring are removable as verified. No proof of minimal ordered-field hierarchy.

Overall: RESTATE-BEFORE-SHIP if a mathlib contribution is desired.

## Phase 6.0 — Complete callers and inline audit

Fresh lexical enumeration over the canonical source inventory, `rg --no-ignore` and tracked `git grep` agree: definition at362, **one explicit call at586**, in `Roth.index_le_lem6`; zero external-to-file callers. The canonical direct-expression audit independently finds **one value consumer**, `Roth.index_le_lem6`, and **zero type consumers**, among293 ordered unique present proof constants. This is not a transitive dependency/simp closure.

The target has no simp attribute. Neighboring private lemmas establish individual cases; `index_numeric_bound_aux` reasons from a supplied min bound, not a reproof of this sum inequality. No second independent full minimum theorem was found inline. [Caller receipts](../evidence/Roth.min_le_sum_max/callers.json), [tracked cross-check](../evidence/Roth.min_le_sum_max/tracked-callers.json), [lexical enumeration](../evidence/Roth.min_le_sum_max/lexical-enumeration.json), [inline audit](../evidence/Roth.min_le_sum_max/inline-audit.json).

The **entire Theta module** was replayed with the target proved via the final finite-cutoff /2 theorem and its natural /3 bridge. The complete actual `index_le_lem6` body and downstream `Θ_option_le`, `Θ_lt` compile. A separate entire `inlineConsumer` duplicates the actual caller, substituting the original target's case split at its use: this also compiles using the replay's private branch lemmas. It demonstrates a possible **project-local** inline refactor, not an existing mathlib composition.

## Phase 6 — Existing-call gate and actual experiments

[Fresh isolated composition source](../evidence/Roth.min_le_sum_max/minsum206-composition-executed.lean.txt) runs exact?, simp and positivity guards **before any new helper declarations**. Each fails to close the original goal, as expected. It also executes and rejects the two explicit three-call attempts:
```lean
(min_le_left _ _).trans (Finset.sum_nonneg ...)
(min_le_right _ _).trans (Finset.sum_nonneg ...)
```
Nonnegativity supplies 0≤S, not either generally positive branch bound. The snippet then proves the theorem with three freshly local branch proofs; these make the proof complete without counting them as library calls.

The guards in the separate generic isolated proof run **after** newly declared branch helpers; they are supplementary and are not claimed as the before-new-helpers test. A first rejected isolated draft accidentally let exact? find the previously introduced realScale alias, as well as containing annotation/tactic issues; it is explicitly excluded from accepted closure evidence.

The new theorem plus min monotonicity gives a short original-form corollary, but that calls **new** code. The original target's two project-helper calls likewise fail the existing-mathlib requirement. No strict ≤3-existing-call term was verified; no closing simp composition occurred. This is NOT-COMPOSABLE-ESTABLISHED by the attempted routes, with no exhaustive impossibility claim.

[Clean composition receipt](../evidence/Roth.min_le_sum_max/minsum206-composition-receipt.json), [full actual-context source](../evidence/Roth.min_le_sum_max/minsum206-fullmodule-executed.lean.txt), [full native receipt](../evidence/Roth.min_le_sum_max/minsum206-fullmodule-receipt.json).

## Phase 7 — Actionable verdict

**BORDERLINE-needs-human.** The project theorem is sound, its use is real, and its statement has verified improvements. The arithmetic estimate needs actual branch proofs; two short project-helper calls do not establish a mathlib NO verdict. Conversely, the exact source constants and one consumer do not establish a reusable public API demanded beyond this argument. The remaining decision is mathematical API grain and audience, not proof cost or incomplete verification.

Concrete future upstream design questions; no user response is required to complete this read-only assessment:

1. Should mathlib expose a general clipped arithmetic-progression bound, rather than leaving this numerical helper in `Roth/Theta.lean`?
2. If so, should the public endpoint be the verified arbitrary-scale ordered-field /2 minimum, with the natural-scale /3 paper statement only a downstream corollary?
3. Should one public finite positive-part estimate replace the three private branch helpers as the intended API grain, rather than exposing their case-specific interfaces?

If retained locally, keep the current named theorem because it communicates the determinant lower bound; it is not dead code. A later authorized generalization can replace its proof with the new finite-cutoff theorem and natural /3 bridge, updating the single call only if the public statement changes. If inlining is chosen, the verified inlineConsumer gives the complete caller refactor, but retains project numerical helpers and is not a reason to label NO-composable-from-mathlib. No production changes or speculative upstream file placement are required for this BORDERLINE assessment.

## Phase 8 — Verification and handoff

Fresh17 baseline inputs match; original type/print/standard axioms checked; canonical source arrays exactly match tracked order with293 unique names, including private module names; runtime all293 are present and have values. Direct consumers are1value/0type. Final finite proof, original specialization, arbitrary-real-scale proof, four false-strengthening guards, negative-scale example, complete caller and module replay all pass. Accepted evidence has no warnings/errors, timeout, recovered sorryAx, resource raises, unsafe code or new axioms.

Rejected executed drafts are separately archived: initial isolated draft (annotation/syntax/sum normalization and alias-contaminated guard); initial finite draft (Nat.cast_succ normalization). Their recovered sorryAx outputs are **not** accepted proof evidence. Successful earlier composition/fullmodule batches are preserved separately as historical accepted executions. The exact original kernel print is complete here; no printer-elision marker occurred.

[Verification map](../evidence/Roth.min_le_sum_max/verification.json), [phase metadata](../evidence/Roth.min_le_sum_max/phase-evidence.json), [portable validator](../evidence/Roth.min_le_sum_max/validate.py), [current manifest](../evidence/Roth.min_le_sum_max/copy-manifest.json). Root acceptance is pending independent review; all assessment phases complete, verification unresolved[].

