# Roth.one_mem_RSet — canonical184

**BORDERLINE-needs-human. Retain locally in Roth/Theta.lean.** This is the elementary unit witness for the complete bounded polynomial family, not an independently established upstream family API. The actual independent proof closes by `simp` after unfolding that family. Under Phase6b this is SIMP-COMPOSABLE, which does not by itself establish the strict one-to-three-existing-call gate. No existing exact full-family theorem was verified, and none is claimed absent from all of mathlib. Assessment is complete; future API-design questions below are not unresolved verification work.

## Phase 0 — baseline

The reusable build completed all2467 jobs without errors or warnings. All17 production-source and pin hashes were freshly compared and match the shared baseline. The declaration resolves at Roth/Theta.lean:73 and is a theorem, with no sorry. The declaring module defines extremal polynomial indices and proves Lemmas5–7 of the source. The entire985-line module and the entire sole actual caller were read. [Build](../evidence/Roth.one_mem_RSet/baseline-build.txt), [fresh hashes](../evidence/Roth.one_mem_RSet/source-hashes.json), [module](../evidence/Roth.one_mem_RSet/source-Theta.lean.txt).

## Phase 1 — statement and proof

For any type of variables and any vector of natural degree bounds, the constant integer polynomial1 belongs to the family of nonzero polynomials satisfying every coordinate degree bound and every coefficient absolute-value bound, provided the real coefficient bound is at least1. Its coordinate degrees are0; its constant coefficient is1 and its other coefficients are0. This provides an admissible polynomial for nonemptiness of the index supremum family.

Full native type:

```lean
∀ {σ : Type u_1} {B : ℝ}, 1 ≤ B → ∀ (r : σ → ℕ), 1 ∈ Roth.RSet B r
```

There is no Fintype or DecidableEq instance parameter. `σ` is universe-polymorphic, `B` is the real coefficient bound, `hB` is its lower bound and `r` is any natural degree vector. The proof uses local classical decidability for coefficient case analysis, not a public assumption. Its full kernel body was printed without elision. Standard axioms are propext, Classical.choice and Quot.sound. [Original type/body/audit](../evidence/Roth.one_mem_RSet/one-mem184-original-receipt.json), [native type](../evidence/Roth.one_mem_RSet/native-type.json).

## Phase 2 — preliminary checks

SMALL: this is a witness/helper, neither a main result nor a named theorem. One-line-definition test: n/a, declaration kind theorem. No definition exemption is invoked, and proof length alone does not decide its verdict.

## Phase 3 — exhaustive literature

All actual exact requests, returned-response SHA256/bytes/status, returned titles/URLs and original concise summaries are retained; full web bodies are not archived. The table reports every named protocol channel, without inventing a ninth channel to resolve the command's counting mismatch.

| Channel | Actual query or source | Outcome |
|---|---|---|
| General web, specific | constant polynomial1 height maximum absolute coefficients degree zero Roth theorem bounded polynomials | Roth expositions use coefficient maxima plus coordinate bounds; elementary unit witness is consistent. |
| General web, general | multivariate polynomial height naive height constant polynomial one coefficient norm | Naive height is coefficient maximum; several other height conventions also returned. |
| General web, alias | polynomial Gauss norm unit one bounded degree coefficient box | Gauss-norm sources are related; univariate root/Cauchy bounds are not the complete family. |
| ChatGPT math MCP | standard form/generality/history | n/a: ask_chatgpt_math unavailable; other channels still executed. |
| Local source | clean.tex642–670, §5 | Defines all three conditions and explicitly admits constant1. |
| nLab | site:ncatlab.org/nlab polynomial norm Gauss | Norm/polynomial background; direct polynomial open failed400 unsupported XHTML. |
| nCatLab, distinct namespace | site:ncatlab.org/ncatlab polynomial norm | Results were mostly /nlab; no exact in-namespace hit, not proof of absence. |
| Stacks | site:stacks.math.columbia.edu polynomial ring constants degree | Broad book/exercises/chow PDFs; no exact full-family unit result identified. |
| MathOverflow | site:mathoverflow.net polynomial height maximum coefficients constant | Height/factor discussions distinguish coefficient height from other bounds. |
| Recent arXiv | site:arxiv.org polynomial height constant polynomial bounded coefficients after:2021-10-27 before:2026-10-28 | Actual date-filtered search; irrelevant applied-polynomial results also returned. Jelinek2023 verified separately. |

[General searches](../evidence/Roth.one_mem_RSet/web-0.json), [nLab/nCatLab](../evidence/Roth.one_mem_RSet/web-1.json), [Stacks/MO](../evidence/Roth.one_mem_RSet/web-2.json), [arXiv](../evidence/Roth.one_mem_RSet/web-3.json), [primary access receipts](../evidence/Roth.one_mem_RSet/web-primary.json), [local evidence](../evidence/Roth.one_mem_RSet/local-literature.json), [exact local excerpt](../evidence/Roth.one_mem_RSet/clean-section5-excerpt.tex.txt).

The standard concept is the constant unit in a bounded degree and naive-height family. The local source says exactly “the constant polynomial $1$ with every $h_i=1$ is allowed”. Independent [Milojevic notes](https://aleksa-milojevic.github.io/expository/roth.pdf) (January2022, coefficient-height definition) and [Min Ru notes](https://www.math.uh.edu/~minru/fields/roth.pdf) (p3, definition before Index Theorem) use coefficient maxima separately from degree bounds. [Jelinek2023](https://arxiv.org/abs/2308.15146) concerns averages at fixed naive height; it supports continued use of the concept, not this exact lemma. No separate historically named unit-membership theorem emerged. Normed coefficients are a meaningful expanded representation; projective/logarithmic heights have different normalizations and cannot silently replace the current coefficient maximum.

## Phase 4a — all parameters and hypotheses

| Parameter | Current form | Standard/comparison | Weakening conclusion |
|---|---|---|---|
| σ | arbitrary Type u | source uses finitely many variables | Already stronger generality for this witness; no Fintype to remove. |
| decidability | absent publicly | coefficient lookup needs temporary equality decisions | Local classical proof compiles; no new public class. |
| B | arbitrary real | source assumes B≥1 | Fixed parent RSet interface; changing codomain needs a new family representation. |
| hB | 1≤B | constant coefficient has absolute value1 | Necessary and sufficient: isolated `iff_bound` compiles for full arithmetic predicate. |
| r | arbitrary σ→ℕ | source assumes positive finite degree vector | Zero bounds already allowed; degrees of1 are0, no positivity needed. |
| ℤ coefficients | fixed by RSet | coefficient max over normalized absolute values/norms | Expanded normed-field and normed-ring predicates compile; changing RSet itself is not a one-edit weakening of this theorem. |

## Phase 4b — generality verdict

MAXIMALLY GENERAL within the fixed RSet interface: no removable instance or hypothesis was found. In particular `1≤B` cannot weaken to `0≤B` because of the constant coefficient, even for an empty variable type. Isolated arithmetic `iff_bound` verifies this necessity mechanically. Expanded normed-field and normed commutative-ring forms are independent proof experiments, not newly discovered existing mathlib theorems and not a YES-but-generalise-first ticket against the current fixed parent. [Isolated proofs](../evidence/Roth.one_mem_RSet/one-mem184-isolated-executed.lean.txt), [raw success](../evidence/Roth.one_mem_RSet/one-mem184-isolated-receipt.json).

## Phase 4c — modern idiom, all nine rows

| # | Diagnostic | Answer and consequence |
|---|---|---|
| 1 | Preambles to classes | No: σ is already arbitrary and hB is ordinary bound data, not an algebraic structure. |
| 2 | Sequences to filters | No topology or limiting argument. |
| 3 | Construction to universal property | No: witness membership is not a universal-property construction. |
| 4 | Closure predicate to substructure | No: nonzero bounded-height family lacks additive and multiplicative closure; bundling as submodule/subring would change content. |
| 5 | Scalar hierarchy | Yes in expanded representation: normed ring with normalized norm of1; independently compiled. Fixed integer RSet remains unchanged. |
| 6 | Higher category | No categorical statement or transport coherence involved. |
| 7 | Concrete index to ordered monoid | Variable type is already arbitrary; ℕ coordinate exponents are intrinsic to polynomials. Real coefficient bounds belong to parent representation. |
| 8 | Concrete via abstract | Fires: RSet occurs once in the two substantive proof lines, as an unfolding argument; remaining proof uses coefficient delta, degree0, nonzero1 and order bounds. Generic expanded normed predicates compile. |
| 9 | False-generalization guard | Removing nonzero, replacing coordinate bounds by total degree, bundling as a subring, allowing arbitrary norms without norm1=1 or substituting projective/log height would change the object. Those proposals are rejected. |

Modern idiom available: normalized coefficient-norm and degree-bound API could package this witness with a future generic family. This could reuse `MvPolynomial.degreeOf_one` and `coeff_one`, but no existing exact family was independently verified. Its design should be resolved alongside the already BORDERLINE parent RSet assessment, rather than upstreaming a Roth-specific spelling independently.

## Phase 4.5 — infrastructure risks

n/a for all six infrastructure rows: theorem introduces no typeclass instance, reducible construction or coercion. Specifically typeclass diamond, reducibility leak, noncanonical unfolding, priority collision, universe-polymorphism risk and coercion ambiguity are n/a at this theorem declaration; its existing parent definition is assessed separately. The actual theorem type confirms arbitrary universe and absence of finiteness/decidability parameters.

## Phase 4.6 — proof strategy, all five rows

| # | Strategy diagnostic | Outcome |
|---|---|---|
| 1 | ε–δ versus filters | No topology. |
| 2 | Elements versus ideal/submodule inclusions | No closure structure exists for nonzero bounded family; direct witness checks are appropriate. |
| 3 | Sequences versus nets | No limits. |
| 4 | Construction versus universal property | No categorical construction. |
| 5 | Helpers mathlib should have | Existing unit-degree and delta-coefficient facts suffice for the proof; possible new family API is a design question, not a necessary helper gap. |

MATHLIB-IDIOMATIC: local classical simplification is the direct mathematical proof. No cost-based verdict downgrade and no invented helper theorem are used.

## Phase 5 — all15 formal search cells

Every Finder, Loogle, LeanSearch and local-name request has its complete raw result in [formal-search.json](../evidence/Roth.one_mem_RSet/formal-search.json). Pinned source searches preserve exact CLI arguments and untruncated stdout in [current](../evidence/Roth.one_mem_RSet/rg-current.json), [standard](../evidence/Roth.one_mem_RSet/rg-standard.json) and [abstract](../evidence/Roth.one_mem_RSet/rg-abstract.json). External indices need not match this pin; positive primitive signatures were checked natively.

| Form | Finder | Loogle | LeanSearch | rg pinned source | local search |
|---|---|---|---|---|---|
| Current full unit membership | Poly.coe_one/C_1/cauchyBound_one, no exact full family | degreeOf_one plus variable-degree results | univariate degree_one/coeff_one, partial | full target/family/bounded patterns, recorded | target only; index unavailable |
| Standard unit degree/height | degrees_one/degreeOf_one and cauchyBound_one | MvPolynomial.coeff_one | C_1/Height.mulHeight_one/isPrimitive_one, partial or different meaning | supNorm_one/gaussNorm_one/height_one/degreeOf_one/degrees_one | degreeOf_one hit; index unavailable |
| Abstract normalized coefficient norm | spectralValue and root coefficient bounds, not same predicate | AddMonoidAlgebra.coeff_one_zero and coefficient delta variants | single_apply/one_def, useful primitives | coeff_one/norm_one/norm_zero/one_ne_zero | coefficient names including MvPolynomial; index unavailable |

Native pinned positives: `MvPolynomial.degreeOf_one` works over CommSemiring, `MvPolynomial.coeff_one` is an if-zero coefficient formula over CommSemiring with local decidability, `AddMonoidAlgebra.coeff_one_zero` is a generic constant coefficient fact, plus `one_ne_zero`, `Nat.zero_le`, `abs_one`, `abs_zero`. [Pinned signatures](../evidence/Roth.one_mem_RSet/one-mem184-isolated-receipt.json). Relevant complete pinned source files are hashed in [mathlib-inputs](../evidence/Roth.one_mem_RSet/mathlib-inputs.json).

`Polynomial.supNorm_C`/`gaussNorm_C` concern univariate coefficient norms; `Polynomial.cauchyBound_one` concerns a root bound. `Height.mulHeight_one` concerns a different height abstraction. None is claimed an exact full arbitrary-variable, nonzero, all-degree/all-coefficient family membership theorem. Local index unavailability and finite search results do not prove global absence. No blind exact? absence claim is made: the actual generic-route check is the independently compiled full conjunction normalization, not a negative search theorem.

## Phase 5.5 — statement shape

Normal forms: `1∈RSet B r`, the expanded three-conjunct predicate, and the equivalent bound `1≤B`. Current membership is the right client-facing shape for `indexSet_nonempty`; expanded predicates are evidence, not a proposed new project API. Native `iff_bound` puts `1≤B` on the RHS and verifies both directions. Mathlib's primitive normal forms degreeOf1=0 and coefficient delta are already used. No competing two-form equivalence mesh is proposed.

Syntactic generality: proof could expose an iff instead of a sufficient-condition lemma, but sole actual caller has hB and needs membership, so the present application is direct. All variables and degree bounds are explicit where useful. Superfluous parameters: no Fintype, DecidableEq, positive-degree or nonempty-variable assumptions occur; hB is necessary as above. Normed-field/ring variants widen the representation, not the existing parent interface.

## Phase 6.0 — callers and inline audit

Exact production lexical enumeration uses `rg --no-ignore` restricted to Roth/ and Roth.lean and is independently cross-checked against tracked `git grep`. There are two occurrences: the declaration and one use at Theta:81 in `Roth.indexSet_nonempty`. The full caller constructs index-family nonemptiness using polynomial1, numerator1, generic coprime1 and reflexivity. Canonical ordered293 audit independently reports one direct kernel-value consumer `Roth.indexSet_nonempty` and zero direct kernel-type consumers; these are not claimed to be opaque kernel/simp dependency closure. [Lexical receipts](../evidence/Roth.one_mem_RSet/callers.json), [tracked cross-check](../evidence/Roth.one_mem_RSet/git-callers.json), [structured caller](../evidence/Roth.one_mem_RSet/callers-structured.json), [inline audit](../evidence/Roth.one_mem_RSet/inline-audit.json).

No other production inline rederivation of the unit witness was identified. The theorem is live local API, not dead code. If deleted in a future refactor, its only explicit caller can use the same local simp proof as its membership witness; the actual caller reconstruction was independently checked with `OneMem184.expanded` in place of the target. This new proof is not an existing mathlib building block. [Project exact source](../evidence/Roth.one_mem_RSet/one-mem184-project-executed.lean.txt), [project receipt](../evidence/Roth.one_mem_RSet/one-mem184-project-receipt.json).

## Phase 6 — composition experiment and strict gate

The actual old-form proof checked independently is:

```lean
by
  classical
  simp [Roth.RSet, MvPolynomial.coeff_one, apply_ite, ite_apply,
    hB, zero_le_one.trans hB]
```

An isolated mathlib-only probe guarded by `#check_failure Roth.one_mem_RSet` proves the complete expanded arithmetic predicate with the same coefficient normalization; it imports no Roth module. It checks nonzero1, every degree bound and every coefficient bound. A normed-field expansion and a mechanically weaker normed-ring expansion also succeed. The normed-ring variant uses [NormedCommRing K] [NormOneClass K] [Nontrivial K]. It specializes back to the exact integer arithmetic conjunction using pinned Int.norm_eq_abs; this is a checked representation bridge, not merely similar notation. [Ring success](../evidence/Roth.one_mem_RSet/one-mem184-normed-ring-receipt.json), [integer specialization](../evidence/Roth.one_mem_RSet/one-mem184-specialization-receipt.json). These are genuine composition experiments, not just restatement sketches.

Classification: **SIMP-COMPOSABLE**, not a demonstrated ≤3 existing-call term. The formula requires conjunction construction, nonzero1, degreeOf_one plus natural nonnegativity, coefficient delta case analysis, cast/absolute-value normalization, and propagation of0≤1≤B. Merely counting the three conjuncts, counting `simp` as one existing theorem, or counting project RSet as an existing mathlib building block would fail the strict gate. A new generic witness helper would be new code, not an existing-call replacement. The evidence therefore supports BORDERLINE under Phase6b without asserting a universal lower bound on proof call count or mathematical novelty.

## Phase 7 — verdict and action

**BORDERLINE-needs-human.** Retain `Roth.one_mem_RSet` in Roth/Theta.lean. Parent RSet was accepted BORDERLINE for a possible generic degree/height family API, not NO-mathlib-has-it; therefore the ModeB parent re-aim rule does not force a NO verdict. This theorem is not definitional rfl glue, so the full assessment was independently executed. There is no exact verified upstream full-family analogue and no strict ≤3-existing-call replacement. The fact that a short simp proof closes is recorded honestly rather than converted automatically into NO.

Future upstream design questions (not questions that block this read-only assessment):

1. Should a generic bounded coordinate-degree and normalized coefficient-norm family be added, with unit membership among its basic laws?
2. Should that family expose unit membership as an iff with1≤B, or only the sufficient-condition form used by nonemptiness clients?
3. Should the family stay a raw set intersection of the three conditions, or have a dedicated API name given that excluding zero prevents subring/submodule packaging?

No standalone Roth-specific upstream PR is recommended pending those choices. Any future family API should be assessed against the parent's degree/height proposal and the existing monoid-algebra coefficient and polynomial-degree machinery. All production remains unchanged.

## Phase 8 — verification and delivery

All phases PASS, theorem-only exceptions justified, unresolved[]. Full canonical order, all293 unique names and all293 values verified; one value consumer and zero type consumers. All accepted native responses are successful, complete and warning/error/sorry-free with standard axioms. The portable read-only validator checks current manifest hashes/bytes, links, fresh17 inputs, exact canonical order, search cells, caller data, native source/receipts and the secret guard. The historical worker manifest is never substituted for the current copy manifest. [Assessment](../evidence/Roth.one_mem_RSet/assessment.json), [verification](../evidence/Roth.one_mem_RSet/verification.json), [overview entry](../evidence/Roth.one_mem_RSet/overview-entry.json), [validator](../evidence/Roth.one_mem_RSet/validate.py).
