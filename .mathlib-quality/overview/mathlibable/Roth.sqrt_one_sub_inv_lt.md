# Roth.sqrt_one_sub_inv_lt — full mathlibable assessment

**Verdict: BORDERLINE-needs-human.** The inverse-square threshold is a project-specific scalar consequence of Bernoulli's square-root inequality. It has a verified broader real-parameter form, but the existing Bernoulli theorem does not give the original result by a literal ≤3-call composition: positivity, reciprocal comparison, squaring and arithmetic normalization remain real proof work. The upstream design question is whether this additional threshold API is useful alongside the existing tangent bound. Cost is not a verdict factor.

Phase 0 — baseline and scope. Declaration 120/293 is the public theorem at `Roth/Lattice.lean:29`. The entire 220-line module and its sole explicit caller `sum_inv_lt` were read. The module proves the lattice count estimate through a reciprocal-sum estimate and induction on box dimension. The target has no project-defined constants in its statement or proof. All 17 production-source/pin hashes freshly match the shared clean-build manifest; baseline `lake build` completed 2467 jobs with no errors or warnings. [Fresh input hashes](../evidence/Roth.sqrt_one_sub_inv_lt/source-inputs.json), [baseline](../evidence/Roth.sqrt_one_sub_inv_lt/baseline-build.txt), [complete module](../evidence/Roth.sqrt_one_sub_inv_lt/declaring-module.lean.txt).

Phase 1 — meaning. For a natural dimension m≥2 and a real λ larger than 2√m, the square root of 1−1/m is strictly smaller than 1−λ⁻². The dimension bound ensures positivity of the relevant quantities, while the λ bound makes its inverse square sufficiently small. The proof bounds λ⁻² by 1/(4m), converts the square-root comparison to a squared comparison, and closes the resulting polynomial inequality.

Full elaborated type:
```lean
Roth.sqrt_one_sub_inv_lt {m : ℕ} (hm : 2 ≤ m) {lam : ℝ}
  (hlam : 2 * √↑m < lam) : √(1 - 1 / ↑m) < 1 - lam⁻¹ ^ 2
```
The native `#check`, original kernel-value audit and standard-axiom check succeeded. The `#print` body is explicitly elided by the MCP output-size limit (94563 characters omitted); the complete short source proof is preserved separately. This is not claimed to be a complete pretty-printed kernel-body dump. [Original native receipt](../evidence/Roth.sqrt_one_sub_inv_lt/sqrt-one-sub-inv-original-receipt.json), [exact executed source](../evidence/Roth.sqrt_one_sub_inv_lt/sqrt-one-sub-inv-original-executed.lean.txt).

Phase 2 — **SMALL**: elementary helper for the harmonic-sum estimate, neither a named main theorem nor new structure. One-line definition test: n/a, declaration is a theorem; its multiline proof is not a definition wrapper.

Phase 3 — exhaustive literature protocol. Exact executed requests, response SHA256/bytes/status and returned locators are archived without article bodies. The date window for recent literature is 2021-10-27 through 2026-10-27. [Web receipts 1](../evidence/Roth.sqrt_one_sub_inv_lt/web1-metadata.json), [2](../evidence/Roth.sqrt_one_sub_inv_lt/web2-metadata.json), [3](../evidence/Roth.sqrt_one_sub_inv_lt/web3-metadata.json), [local primary source](../evidence/Roth.sqrt_one_sub_inv_lt/local-literature.txt).

| Channel | Exact query or locator | Finding |
|---|---|---|
| General web, specific | `"sqrt" "1 - 1" "Roth" lattice count` | No relevant exact scalar theorem located; unrelated Roth/lattice hits do not establish absence. |
| General web, standard | `Bernoulli inequality fractional exponent square root concavity tangent` | Fractional-exponent Bernoulli inequality; the square-root case is the relevant standard theorem. |
| General web, alias | `square root arithmetic geometric mean inequality tangent bound` | AM–GM gives √t≤(1+t)/2 for nonnegative t. Primary teaching source: Bjorn Poonen, *Inequalities*, §1, p.1. |
| Optional ask_chatgpt_math | Standard form, generality, historical evolution | n/a: tool unavailable; no second-opinion response invented. |
| Local references | `clean.tex`, §6, lines 1094–1129 | Exact displayed inequality at 1115; at 1116–17 the source justifies it by squaring positive quantities. It is a step of Lemma 8, not a separately named theorem. |
| nLab | `site:ncatlab.org/nlab/show convex function`; `site:ncatlab.org/nlab/show concave function`; direct convex-function page | Indexed convex/concave definition available; direct open failed with unsupported XHTML content-type. No exact threshold API found. |
| nCatLab | `site:ncatlab.org/ncatlab concave function square root Bernoulli inequality` (targeted follow-up to broad host query) | Search returned nLab convex-function, real-square-root and other host pages; no `/ncatlab`-page hit for the threshold inequality. This is not absence evidence. No separate categorical restatement improves this scalar bound. [Exact request and metadata](../evidence/Roth.sqrt_one_sub_inv_lt/ncatlab-targeted-metadata.json). |
| Stacks | `site:stacks.math.columbia.edu square root inequality concavity` | Hits concern algebraic square roots/fundamental theorem of algebra, not the ordered real inequality. n/a for algebraic-geometric generalisation. |
| MathOverflow | `site:mathoverflow.net Bernoulli inequality square root concavity` | Nearby elementary-inequality/Karamata and constructive-square-root discussion; no exact λ,m threshold theorem. |
| Recent arXiv | Broad 2022–2026 query, then `site:arxiv.org/abs/ "Bernoulli inequality" "2023"` and same with `2024` | 2302.05522 (Bergman-space analogues, 2023) and 2411.16966 (quasiregular distortion, 2024) are genuine recent but different generalisations. 1702.00265 is historical supplementary material, outside the window. |

Primary locators: [Poonen, Inequalities, §1](https://math.berkeley.edu/~stankova/MathCircle/Joyce/inequalities.pdf), [nLab convex function](https://ncatlab.org/nlab/show/convex%2Bfunction), [2023 Bergman-space paper](https://arxiv.org/abs/2302.05522), [2024 distortion paper](https://arxiv.org/abs/2411.16966). The standard useful form is the Bernoulli/tangent estimate √(1+x)≤1+x/2 for x≥−1; concavity and AM–GM explain it. The source's inverse-square specialization is narrower and has no separate established name in the searched literature. Literature searches do not prove absence.

Phase 4a–b — parameter and hypothesis audit. **STRICTLY NARROWER THAN STANDARD** in the sense of the verified real-parameter extension below; this is a sufficient extension, not a claim of optimal hypotheses.

| Parameter / hypothesis | Actual role | Verified or rejected change |
|---|---|---|
| `m : ℕ` | Only its real cast is used in the scalar argument; no induction or discrete arithmetic | Replaced by `m : ℝ`. |
| `2 ≤ m` | Provides a positive reciprocal and a positive right side | Weakened to real `1 ≤ m`, including m=1. Dropping every bound is false at m=0, λ=1. |
| `lam : ℝ` | Ordered field operations and the chosen real square-root API | Retained; arbitrary fields have no automatically supplied principal real square root. |
| `2 * √m < lam` | Gives an inverse-square upper bound | Weakened to `2 * √m ≤ lam` while retaining the strict conclusion. Removing it entirely is false at m=2, λ=1. |
| Implicit typeclasses/universes | Concrete ℝ/ℕ statement | No independent hidden project interfaces or unused structure arguments. |

Verified sufficient restatement:
```lean
theorem realWeak {m lam : ℝ} (hm : 1 ≤ m) (hlam : 2 * √m ≤ lam) :
    √(1 - 1 / m) < 1 - lam⁻¹ ^ 2
```
The algebra uses λ⁻²≤1/(4m), so even equality in the λ premise leaves strict slack in the squared comparison. The stronger tentative condition λ²≥2m is not claimed verified or optimal here. The original source's requirement m≥2 is needed by adjacent positivity arguments in `sum_inv_lt`, but that parent context does not force the scalar helper to have the same restriction. Native accepted proofs and guards are catalogued in [verification](../evidence/Roth.sqrt_one_sub_inv_lt/verification.json).

Phase 4c — all modern-idiom rows:

| # | Question | Result and downstream consequence |
|---|---|---|
| 1 | Typeclasses instead of bundled hypotheses | No: scalar inequalities, not algebraic structures needing new instances. |
| 2 | Filters/nets instead of sequences/metrics | No sequences, convergence or topology in the target. |
| 3 | Universal property instead of construction | No object is constructed. |
| 4 | Bundled substructure instead of closure predicates | No substructure or closure predicates. |
| 5 | Weaker scalar hierarchy | The polynomial comparison itself works in an ordered field, but `Real.sqrt` selects ℝ. An abstract square-comparison guard verifies the elementary order content; it is not an upstream replacement theorem about sqrt. |
| 6 | Higher categories | No categorical content; convex-space terminology does not improve this scalar application. |
| 7 | Concrete index | Yes: natural m becomes real m≥1, admitting real parameters without casts. This directly composes with `Real.sqrt_lt'` and reciprocal comparison. |
| 8 | Concrete-via-abstract diagnostic | The proof has 5 occurrences of m over 4 body lines, and 2 `Real.sqrt` occurrences over 2 lines ([exact diagnostic](../evidence/Roth.sqrt_one_sub_inv_lt/concrete-diagnostic.json)); it never unfolds a project-defined named object. After introducing the real lower bound, no natural-number property is used. Real m extension verifies this specific abstraction. Replacing sqrt by arbitrary functions is rejected absent explicit square/nonnegativity laws. |
| 9 | False-generalisation guard | Real m preserves the same scalar quantity and specializes back by casting. Arbitrary ordered fields with an uninterpreted `sqrt` do not preserve the object. Verified numerical counterexamples prevent dropping all domain/threshold assumptions. |

Modern idiom available: modest scalar-domain improvement, not a new categorical organisation. It enables the actual caller through casting and weakening, but does not show broad independent demand for a new inverse-square threshold API.

Phase 4.5 — n/a: theorem. All six infrastructure categories are inapplicable: no typeclass diamond, reducibility leak, non-canonical unfolding, instance-priority collision, universe-polymorphism constraint or coercion ambiguity is introduced. No instance priority or infrastructure API migration is proposed; the optional statement-level real-parameter refactor is assessed separately above.

Phase 4.6 — proof strategy:

| # | Strategy question | Finding |
|---|---|---|
| 1 | ε–δ versus filters | No topology. |
| 2 | Elements versus subobjects | No subobjects. |
| 3 | Sequences versus nets | No limiting argument. |
| 4 | Construction versus universal property | No construction. |
| 5 | Missing helpers mathlib should have | `Real.sqrt_one_add_le` already supplies the standard tangent estimate; no missing generic helper was demonstrated. The additional inverse-square threshold remains a possible convenience API question. |

Current strategy: MATHLIB-IDIOMATIC for a short scalar inequality. An alternative Bernoulli proof is actually tested, with normalization and arithmetic included; it exposes the literature connection but still needs substantive proof glue and is not automatically a shorter replacement.

Phase 5 — five actual mathlib search methods × three forms. [Raw complete formal receipts](../evidence/Roth.sqrt_one_sub_inv_lt/formal-search.json), [exact source commands and results](../evidence/Roth.sqrt_one_sub_inv_lt/source-search-raw.json).

| Method | Current inverse-square form | Standard Bernoulli form | Abstract concavity form |
|---|---|---|---|
| Lean-Finder | Partial: `sqrt_one_add_le` and unrelated scalar estimates | Exact `Real.sqrt_one_add_le`; general real-rpow Bernoulli | `Real.strictConcaveOn_sqrt`, NNReal analogue |
| Loogle | Exact pattern empty | Exact `Real.sqrt_one_add_le` | Exact `Real.strictConcaveOn_sqrt` |
| LeanSearch | `sqrt_lt'`, `sqrt_lt`, tangent building blocks | Exact tangent theorem | Strict concavity and `ConcaveOn.slope_le_of_hasDerivAt` |
| rg pinned source | No declaration with target full name; reciprocal/sqrt blocks inspected | `Mathlib/Analysis/Real/Sqrt.lean:440`; rpow theorem `Analysis/Convex/SpecificFunctions/Basic.lean:168` | `Analysis/Convex/SpecificFunctions/Pow.lean:90`; derivative slope API |
| Local name search | Only project target | Pinned-source tangent hit | Pinned-source concavity hits |

All local searches report `index: unavailable`; source hits remain useful, empty indexed absence is not asserted. Finder/LeanSearch advertise an older `Mathlib.Data.Real.Sqrt` module path; the pin's actual path is `Mathlib.Analysis.Real.Sqrt`. Pinned native signatures, guarded isolated proofs and failed direct automation probes are preserved. The standard tangent is present, but is not identical to the original λ,m threshold claim.

Phase 5.5 — statement shape. Normal form: direct ordered inequality is appropriate; `lam⁻¹ ^ 2`, `1 / lam ^ 2` and `(lam ^ 2)⁻¹` are equivalent field forms, not new mathematical concepts. `Real.sqrt_lt'` is the canonical route to polynomial comparison, while `sqrt_one_add_le` is the standard reusable tangent form. No orthogonal iff lemma should be added. Syntactic generality: real m≥1 plus nonstrict threshold avoids Nat casts and unnecessary strictness; the sole caller can supply it without changing its own stronger hypotheses. Superfluous-argument audit: neither m nor λ is removable; their **bounds are stronger than necessary**, not unused in the original proof. Overall **RESTATE-BEFORE-SHIP** if a threshold lemma is selected for upstreaming.

Phase 6.0 — all callers and inline audit:

| Caller | Usage | Concrete consequence |
|---|---|---|
| `Roth/Lattice.lean:87`, `Roth.sum_inv_lt` | `exact sqrt_one_sub_inv_lt hm hlam` under `gcongr` | Replace only this step by the verified real-parameter helper, with real cast m≥1 and `hlam.le`; the complete caller is replayed natively. [Exact caller replay](../evidence/Roth.sqrt_one_sub_inv_lt/sqrt-one-sub-inv-consumer-executed.lean.txt), [receipt](../evidence/Roth.sqrt_one_sub_inv_lt/sqrt-one-sub-inv-consumer-receipt.json). |

One same-file explicit use; zero external-to-file explicit references. Native scan of all 293 canonical kernel values identifies exactly `Roth.sum_inv_lt` as a direct consumer. This is a direct dependency audit, not a transitive/simp closure claim. Source search found no separate inline rederivation; adjacent `hpos1` proves positivity and `hsqrt` rewrites the ratio, so neither duplicates the target. [Canonical native audit](../evidence/Roth.sqrt_one_sub_inv_lt/sqrt-one-sub-inv-audit-receipt.json).

Phase 6 — actual composition experiments. **NOT-COMPOSABLE** under the strict ≤3-existing-call rule demonstrated by the attempted routes, without claiming global mathematical absence.

1. Original proof: establishes cast bound, squared λ bound, reciprocal-power estimate, positive right side, sqrt-to-square equivalence and polynomial comparison. This uses at least `Real.sqrt_nonneg`, `Real.sq_sqrt`, `Nat.cast_nonneg`, reciprocal comparison, `Real.sqrt_lt'`, and `sq_nonneg`, with `rw` and `nlinarith`. This is an actual proof, not three chained existing calls.
2. Bernoulli route: `Real.sqrt_one_add_le (x := -(1/m))` supplies √(1−1/m)≤1−1/(2m). It still needs the λ-square estimate, reciprocal comparison, tangent-domain premise, negation/division normalization and strict arithmetic comparison. The executed proof preserves all those obligations, including explicit `one_div_pos` required by the arithmetic closing step. [Accepted independent proofs](../evidence/Roth.sqrt_one_sub_inv_lt/sqrt-one-sub-inv-raw-clean-executed.lean.txt), [clean native receipt](../evidence/Roth.sqrt_one_sub_inv_lt/sqrt-one-sub-inv-raw-clean-receipt.json). The one-call standard tangent specialization alone does not prove the inverse-square theorem.
3. Direct `exact?` probes on current and widened shapes fail cleanly, with no timeout or heartbeat exhaustion. Fresh absence guards confirm that neither the project target nor the new test helpers are imported. The standard-form positive control suggests `exact Real.sqrt_one_add_le hx`. [Exact executed search](../evidence/Roth.sqrt_one_sub_inv_lt/sqrt-one-sub-inv-direct-search-executed.lean.txt), [native search receipt](../evidence/Roth.sqrt_one_sub_inv_lt/sqrt-one-sub-inv-direct-search-receipt.json). Failure is a negative experiment, not proof of absence. No new project helper is counted as an existing mathlib call.

Phase 7 — actionable verdict. Keep this helper project-local in `Roth/Lattice.lean` while resolving upstream scope; it is live and useful in the reciprocal-sum argument, not junk. Its generalization is mathematically valid and not dismissed for cost. `Mathlib/Analysis/Real/Sqrt.lean` would be the natural home **if** an additional real inverse-square threshold API is accepted, but this assessment does not propose duplicating the already present generic Bernoulli tangent theorem.

1. Should mathlib expose an inverse-square threshold inequality in addition to `Real.sqrt_one_add_le`, given the current single lattice-count use?
2. If yes, should the API use the verified real-m≥1/nonstrict-λ form, or a more symmetric square-parameter comparison with explicitly optimized hypotheses?
3. Should the project retain the named specialized helper for readability, or use a private real-parameter helper at `sum_inv_lt`?

These are upstream API questions, not unresolved verification work. No production edits or user confirmation are required to complete this read-only assessment. A later affirmative API choice should run `/generalise Roth.sqrt_one_sub_inv_lt` and `/cleanup Roth/Lattice.lean Roth.sqrt_one_sub_inv_lt`; no cost-based downgrade or unverified optimality claim is made.

Phase 8 — evidence package. Accepted and rejected native runs are distinguished; standard axioms only, exact canonical 293-name order and source hashes are validated. [Machine assessment](../evidence/Roth.sqrt_one_sub_inv_lt/assessment.json), [verification](../evidence/Roth.sqrt_one_sub_inv_lt/verification.json), [portable validator](../evidence/Roth.sqrt_one_sub_inv_lt/validate.py), [artifact manifest](../evidence/Roth.sqrt_one_sub_inv_lt/copy-manifest.json).
