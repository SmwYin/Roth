# Roth.weight_le_degree_div — full mathlibable assessment

Verdict: **BORDERLINE-needs-human**. Canonical declaration 38, public theorem at `Roth/Box.lean:118`.
The mathematics is standard finite weighted-sum comparison. The existing `Finsupp.weight`
representation is more general than Roth's ambient finite sum, but this assessment found no
existing analogous upper-bound or weight-monotonicity law to invoke under the parent re-aim rule.
The original form requires genuine normalization and pointwise order reasoning, exceeding the
three-call composition gate. A general monotonicity law would be new API, not an existing replacement.
The unresolved choice is upstream API design, not Lean verification; all requested probes passed.

## Baseline and comprehension (Phases 0–2)

The reusable build completed successfully, 2467 jobs. All 17 production-source and pin hashes
were freshly compared and match the shared baseline. No production edits were made. The whole
declaring module was read: it defines boxes of multi-indices and reciprocal real weights.
Evidence: [baseline](../evidence/Roth.weight_le_degree_div/baseline-build.txt),
[fresh hashes](../evidence/Roth.weight_le_degree_div/input-check.json),
[module](../evidence/Roth.weight_le_degree_div/Box-source.lean.txt),
[canonical metadata](../evidence/Roth.weight_le_degree_div/canonical-metadata.json).

For a finite family of natural denominators all at least a positive natural number m, the
sum of d(j)/r(j) is at most the total degree of d divided by m. Each nonnegative numerator
can only increase when its denominator is decreased to m, and summation preserves this order.
Here d is a finitely supported natural multi-index; its degree is the sum of its entries.
The comparison takes place in the reals, so the conclusion uses real division, not Nat division.

Full elaborated type, independently obtained from native Lean:

```lean
∀ {σ : Type u} [Fintype σ] {r : σ → ℕ} {m : ℕ},
  0 < m → (∀ j : σ, m ≤ r j) → ∀ d : σ →₀ ℕ,
    Roth.weight r d ≤ (Finsupp.degree d : ℝ) / (m : ℝ)
```

`DecidableEq σ` has already been omitted in the source; it is not a hidden requirement.
Project dependency: `Roth.weight` only. Native target and recreated proof use only standard
axioms `propext`, `Classical.choice`, `Quot.sound`; there are no sorries.
Classification **SMALL**: elementary helper rather than a main theorem or new structure.
One-line-definition test: **n/a, theorem**; the short proof is not a definition prefilter.

## Exhaustive literature (Phase 3)

Exact requests, returned-response SHA256/byte counts and locator metadata are retained;
article/search bodies are not archived. Returned URL query strings are stripped from all
locators, including harmless ones, to avoid retaining credentials. Search misses are not
evidence of absence. All named channels were attempted; the protocol's informal nine-channel
label does not suppress its separately required three general-web forms.

| Channel | Exact query or local action | Finding |
|---|---|---|
| Web, current | `"Roth" "index" "total degree" "weight"` | Textbook material on index and nonnegative multi-indices; broad noisy results. |
| Web, general | `"weighted degree" "total degree" "maximum weight"` | ECCC 2026/032 uses dot-product weighted degree; no specific upper-bound theorem identified. |
| Web, abstract/alias | `"weighted sum" "nonnegative" "upper bound" "linear functional"` | General positivity/linear-functional context, no distinctive named theorem. |
| ChatGPT math | Tool availability inspected | n/a: ask_chatgpt_math unavailable. |
| Local reference | `clean.tex`, lines 790–809, with broader weight search | Exact source comparison: sum of first-variable derivative weights bounded by w/r_(p−1), for w their sum and ordered positive denominators. |
| nLab | `site:ncatlab.org/nlab "weighted degree"` | Empty results; no weighted-degree standardization established here. |
| nCatLab | `site:ncatlab.org "ordered module" "positive"` | Positive cone page gives ordered-module context; direct open failed unsupported XHTML. No categorical reformulation required. |
| Stacks | `site:stacks.math.columbia.edu "weighted degree"` | Empty results. This numerical comparison needs no scheme-specific formulation. |
| MathOverflow | `site:mathoverflow.net "Roth" "index" polynomial` | Roth/approximation discussions, no target finite-sum law. |
| arXiv, recent | `site:arxiv.org "Roth" "index" "polynomial" after:2021-10-26` | Empty results. |
| arXiv, broadened | `site:arxiv.org "weighted degree" "polynomial" after:2021-10-26 before:2026-10-27` | arXiv:2412.06384, submitted 9 December 2024, weighted-homogeneous singularities; contextual usage, no target comparison. |
| Supplementary primary/expository | `"Roth theorem" "index" filetype:pdf university`, then open publisher/author sources | AMS preview search result describes normalized index; direct fetch 403. Milojevic author PDF (January 2022) accessible, situates classical Roth index terminology. |

Evidence: [web current](../evidence/Roth.weight_le_degree_div/web0-metadata.json),
[general](../evidence/Roth.weight_le_degree_div/web1-metadata.json),
[abstract](../evidence/Roth.weight_le_degree_div/web2-metadata.json),
[nLab](../evidence/Roth.weight_le_degree_div/web3-metadata.json),
[nCatLab](../evidence/Roth.weight_le_degree_div/web4-metadata.json),
[Stacks](../evidence/Roth.weight_le_degree_div/web5-metadata.json),
[MathOverflow](../evidence/Roth.weight_le_degree_div/web6-metadata.json),
[recent arXiv](../evidence/Roth.weight_le_degree_div/web7-metadata.json),
[broadened queries](../evidence/Roth.weight_le_degree_div/web8-metadata.json),
[publisher/author access](../evidence/Roth.weight_le_degree_div/web9-metadata.json),
[arXiv/nLab access](../evidence/Roth.weight_le_degree_div/web10-metadata.json),
[local locators](../evidence/Roth.weight_le_degree_div/caller-literature-excerpts.json).

The local mathematical source is the direct support for the exact estimate. The general form
is positivity of a finite linear combination: if a_j≥0 and w_j≤c on its support, then
Σ a_j w_j≤c Σ a_j. Reciprocal weights with m>0 and m≤r_j give c=1/m.
This abstraction is a mathematical inference, not a claim that the fetched papers state an
arbitrary ordered-field theorem. Standard sources use positive denominators, whereas Lean's
totalized division also permits ignoring zero denominators, a strictly weaker formal premise.
Relevant primary locators: [Milojevic](https://aleksa-milojevic.github.io/expository/roth.pdf),
[Eyral–Oka](https://arxiv.org/abs/2412.06384),
[AMS preview](https://www.ams.org/bookstore/pspdf/mbk-48-prev.pdf).

## Generality and modern idiom (Phases 4a–4c)

| Parameter / premise | Necessity and mechanical result |
|---|---|
| arbitrary universe/type σ | Already arbitrary; no order, inhabitance, or nonemptiness required. |
| Fintype σ | Required to state the fixed Roth ambient-sum interface. Eliminated in the compiled Finsupp.weight representation over the finite support of d. |
| r : σ→ℕ | Natural denominators are a project choice. Native `support_bound` allows arbitrary values in any Field K with LinearOrder and IsStrictOrderedRing, assuming positive m≤r_j on support. |
| m : ℕ | Can become an arbitrary positive element of K in the expanded representation. |
| hm : 0<m | Essential in this general statement. Unit, m=0,r=1,d=single()1 gives false 1≤0 while hr is true. Negative m is also invalid over ℝ: r=1,m=−1,d=1 gives false 1≤−1. |
| hr : ∀j,m≤r_j | Strictly stronger than needed for fixed d. Compiled support-local version uses only ∀j∈d.support,m≤r_j. Bool witness: d supported at true, r(true)=1,r(false)=0,m=1. |
| zero denominators | Compiled still weaker premise ∀j∈d.support,r_j≠0→m≤r_j; zero denominators contribute zero. Unit d=1,r=0,m=1 witnesses strictness versus unconditional support-local hr. |
| d : σ→₀ℕ | Natural exponents ensure nonnegative numerators. Generalization to arbitrary signed coefficients without a sign premise is false: multiplying reciprocal inequality by a negative coefficient reverses it. |
| ℝ codomain | No completeness or Archimedean property used; ordered-field proof compiled. A bare unordered Field cannot state/prove the inequality; order and sign compatibility must remain. |
| conclusion | Exact original upper bound retained throughout. No larger bound or weaker conclusion used to claim generality. |

Generality verdict: **STRICTLY NARROWER** than the standard positive finite linear-combination comparison in its checked support/scalar forms. Three independent dimensions improve: localization of hr, ambient support representation, and ordered scalar generality. The totalized-zero variant is an additional Lean-specific weakening, rather than a claim about classical source conventions. A mechanically verified proposed expanded signature is:

```lean
{σ K : Type*} → [Semifield K] → [LinearOrder K] → [IsStrictOrderedRing K] →
  (r : σ → K) → {m : K} → 0 < m → (d : σ →₀ ℕ) →
  (∀ j ∈ d.support, m ≤ r j) →
  Finsupp.weight (fun j ↦ (r j)⁻¹) d ≤ (d.degree : K) / m
```

The weakened support hypotheses depend on the fixed d, so d must precede them in the binder list.
The support bound and totalized-zero bound are successful mechanical weakenings, not a guess
based on dead-variable inspection. They do not make a new helper an existing mathlib replacement.

All nine modern-idiom rows:

| # | Diagnostic | Result |
|---|---|---|
| 1 | Preambles/bundled hypotheses to typeclasses | No custom algebraic structure premise; existing Fintype and ordered scalar structure already use typeclasses. Numerical support bounds remain ordinary hypotheses. |
| 2 | Metric/sequences to filters | No topology or convergence. |
| 3 | Construction to universal property | No object construction. Existing free-module linearCombination gives the structural context. |
| 4 | Closure predicates to substructures | No subring/submodule predicate to replace. |
| 5 | Concrete field to typeclass hierarchy | Yes: ordered Field proof checked; ring/module comparison is the conceptual umbrella, reciprocal syntax needs division. |
| 6 | Higher categories | No categorical content or justified higher-categorical move. |
| 7 | Concrete index/scalar generalization | σ already arbitrary; ambient Fintype removed in expanded support representation. ℝ replaced by ordered Field. |
| 8 | Concrete-via-abstract adversarial test | Fires: after `rw [weight,...]`, zero subsequent proof lines mention weight. Remaining proof is finite-sum monotonicity and denominator antitonicity. Proposed abstract API is weight monotonicity/constant upper bound, not a second Roth-only theorem. |
| 9 | False-generalization guard | Support-based Finsupp reciprocal weight is the same weighted sum, with unchanged bound. Signed coefficients without nonnegativity or unordered scalars would change/falsify content and are rejected. |

Modern idiom available: yes. A support-local reciprocal Finsupp.weight upper bound, ideally
derived from an arbitrary generator-weight comparison, works over arbitrary index types.
This composes with linearCombination and degree API. A further successful native hierarchy probe replaces Field by **Semifield**, with the same LinearOrder and IsStrictOrderedRing assumptions: additive inverses are unused. This is the broadest mechanically checked scalar form; the original Field receipt is retained unchanged. Local restatement is CHEAP; migration
of the parent weight interface is a separate project decision. Cost is not a verdict factor.

## Proof strategy and infrastructure (Phases 4.6, 4.5)

| Proof-strategy question | Assessment |
|---|---|
| Topology: ε–δ versus filters | n/a, finite algebraic inequality. |
| Algebra: elements versus substructures | No ideal/submodule inclusion; scalar pointwise comparison is natural. Bundled weight may organize repeated uses. |
| Analysis: sequences versus nets | n/a, no limit. |
| Category theory: construction versus universal property | n/a, no categorical construction. |
| Missing helper that should exist | Candidate weight monotonicity/constant upper bound, if useful broadly; none actually found. Generic finite-sum primitives already suffice for the proof. |

Current strategy: **MATHLIB-IDIOMATIC** for the fixed spelling. `gcongr` expresses exactly the
monotonicity argument. API organization could improve under Finsupp.weight without making
the original mathematical strategy poor. Dedicated helper design remains an upstream choice.

Infrastructure risk: n/a because this is a theorem, with all six rows considered:
typeclass diamond (no new instance), reducibility leak (no new data definition), noncanonical
unfolding (proof theorem adds no simp unfolding rule), priority collision (no priority-bearing
instance), universe issue (arbitrary Type u captured natively), coercion ambiguity (ordinary Nat
casts to ordered Field, no custom coercion). Overall risk NONE for this declaration.

## Five-method mathlib audit (Phase 5)

All five methods ran on current, literature-standard, and abstract formulations. External
indices may use a different mathlib revision; candidate signatures were checked against
pinned source/native Lean where used. Local symbol index reported **unavailable**, not a
consulted empty index. That limitation is not absence evidence.

| Method | Current / literature / abstract searches | Finding |
|---|---|---|
| Lean-Finder | quotient sum versus degree; weighted degree versus max weight; monotone linearCombination | Lower bounds, weightedTotalDegree, degree_eq_weight_one, unrelated degree-bound machinery. No existing analogous upper law identified. |
| Loogle | `Finsupp.weight, LE.le`; `Finsupp.weight, Monotone`; `Finsupp.linearCombination, LE.le` | Lower bounds and weightedTotalDegree comparisons; monotone query empty; linearCombination results concern Gröbner/span membership, not this comparison. |
| LeanSearch | denominator lower-bound sum; weight monotonicity/degree bound; nonnegative linear-combination monotonicity | Generic sum order API, weight_apply, degree_apply, linearCombination definitions; no matching law. |
| rg source | Complete untruncated full-name and broader weight/degree/linearCombination/order searches | Actual Weight.lean read in full; Finsupp.Order.sum_le_sum discovered; no weight_mono or weight_le_degree match. |
| local name search | `weight`; `weight_mono`; `linearCombination` | Source hits available but generated-symbol index unavailable. No claim that all possible synthesized generic routes are absent. |

Raw formal-search receipts: [Finder current](../evidence/Roth.weight_le_degree_div/finder-current.json),
[literature](../evidence/Roth.weight_le_degree_div/finder-literature.json),
[abstract](../evidence/Roth.weight_le_degree_div/finder-abstract.json),
[Loogle current](../evidence/Roth.weight_le_degree_div/loogle-current.json),
[literature](../evidence/Roth.weight_le_degree_div/loogle-literature.json),
[abstract](../evidence/Roth.weight_le_degree_div/loogle-abstract.json),
[LeanSearch current](../evidence/Roth.weight_le_degree_div/leansearch-current.json),
[literature](../evidence/Roth.weight_le_degree_div/leansearch-literature.json),
[abstract](../evidence/Roth.weight_le_degree_div/leansearch-abstract.json),
[local current](../evidence/Roth.weight_le_degree_div/local-current.json),
[literature](../evidence/Roth.weight_le_degree_div/local-literature.json),
[abstract](../evidence/Roth.weight_le_degree_div/local-abstract.json),
[exact CLI searches](../evidence/Roth.weight_le_degree_div/source-search.json).

Positive APIs inspected: `Finsupp.weight_apply`, `Finsupp.weight_eq_sum`,
`Finsupp.degree_eq_sum`, `Finsupp.degree_eq_weight_one`, `Finsupp.degree_mono`,
`Finsupp.sum_le_sum`, `Finset.sum_le_sum`, `Finset.sum_div`,
`div_le_div_of_nonneg_left`. The lower bounds `Finsupp.le_weight` and
`Finsupp.le_weight_of_ne_zero` do not supply an upper bound. `degree_mono` compares
coefficient vectors, not reciprocal generator families, and applies in a canonically ordered
codomain; it cannot simply be applied to real reciprocal weights. `degree_eq_weight_one`
identifies degree with constant-one weight but supplies no order law between weight families.
The actual native proof is the positive generic-route experiment. A failed exact? would not
prove absence and was not added, especially given prior search timeouts. This BORDERLINE
verdict makes no exhaustive semantic-absence claim.

Parent re-aim gate explicitly checked: `Roth.weight` is already assessed NO-mathlib-has-it
via reciprocal Finsupp.weight. Unlike the scaling/additivity laws, no analogous bundled
upper-bound law was found here. Merely inventing weight_mono, or applying sum_le_sum after
new normalization/pointwise reasoning, does not establish an existing analogue.

## Statement shape and consumers (Phases 5.5, 6.0)

Normal forms compared: Roth finite quotient sum; reciprocal `Finsupp.weight`; finite-support
dot product. Existing Finsupp.weight is the canonical structural object, not a parallel Roth
weight API. This is an inequality, so the RHS convention for iff/equality normalization does
not impose another rewrite direction. Proposed upstream normal form is an upper comparison
of weights with support-local generator assumptions; original spelling remains appropriate
as a local convenience while its parent exists.

Syntactic generality: tried global hr, support-local hr, conditional nonzero-denominator hr,
and arbitrary ordered-Field/Finsupp representation, all with the same bound. Prefer a simple
generator comparison upstream; the conditional denominator version is the mechanically
weakest checked Roth premise but less close to literature's positive denominators.
Superfluous-argument audit: no DecidableEq binder; Fintype essential only to original interface;
hm essential; global hr stronger than necessary; ℝ stronger than necessary in the expanded
representation. Overall **RESTATE-BEFORE-SHIP** for any new upstream result.

Explicit source references: **zero callers**, zero external-to-file caller files; only the
declaration itself matches. It has no simp tag. This does not establish kernel/simp dependency
closure or prove the public theorem dead. There are therefore no explicit callers to refactor.

Inline audit found `Roth.weight_le_delta_aux`, `Roth/Theta.lean:494–508`, a related bound using
real δ, the ratio hypothesis r_none≤δ*r_some, and d.degree≤r_none. It rederives the same
pointwise/sum technique but is not the exact target statement: a natural m cannot generally
equal r_none/δ. It suggests that a real-scalar general upper-bound API could be useful.
No refactor is claimed verified for that different theorem; it is not counted as a caller.
If the original helper is retained, its alternative local destination is its present Box
bookkeeping module; if unused public helpers are pruned, remove only after downstream API review.

## Composition and verification (Phase 6)

Native same-statement proof (project dependency only in the definition being unfolded):

```lean
rw [Roth.weight, Finsupp.degree_eq_sum, Nat.cast_sum, Finset.sum_div]
exact Finset.sum_le_sum fun j _ ↦
  div_le_div_of_nonneg_left (Nat.cast_nonneg _)
    (by exact_mod_cast hm) (by exact_mod_cast hr j)
```

Honest count: three nondefinitional normalization facts, plus sum monotonicity and denominator
antitonicity, with cast/sign facts as additional supporting steps. This is not a ≤3-call
composition merely because it occupies three lines. No project lemma is counted as a mathlib
building block. The source `rw; gcongr` proof is also new order reasoning, not a direct existing
upper-bound call. Finsupp.weight normalization likewise requires finite-support/cast/product
rewrites before pointwise inverse antitonicity. Conclusion: no qualifying direct ≤3-call
replacement established; the small proof leaves a genuine API-packaging question.

Accepted isolated mathlib-only proof includes `#check_failure Roth.weight_le_degree_div` and
imports no Roth module. It verifies the finite original-form inequality, arbitrary ambient
index set/ordered Field support bound, strict support-local witness, m=0 counterexample,
and negative-m guard. Native project proof verifies the unchanged Roth conclusion and both
localizations, including the strict conditional-zero witness. Target replay separately checks
the declaration signature and axioms. Accepted receipts are terminal success, not warming or
partial responses. Failed initial normalization/zero-branch attempts are retained separately
and never used as proof evidence.

Evidence: [verification map](../evidence/Roth.weight_le_degree_div/verification.json),
[isolated exact source](../evidence/Roth.weight_le_degree_div/raw-executed.lean.txt),
[isolated receipt](../evidence/Roth.weight_le_degree_div/native-raw.json),
[project exact source](../evidence/Roth.weight_le_degree_div/project-executed.lean.txt),
[project receipt](../evidence/Roth.weight_le_degree_div/native-project.json),
[target receipt](../evidence/Roth.weight_le_degree_div/native-target.json),
[broader Semifield source](../evidence/Roth.weight_le_degree_div/semifield-executed.lean.txt),
[Semifield receipt](../evidence/Roth.weight_le_degree_div/native-semifield.json).

## Action (Phases 7–8)

**BORDERLINE-needs-human**, completed read-only assessment, verification unresolved `[]`.
Keep the theorem local pending a decision about a broader Finsupp order API. Do not submit
the Roth-only natural-denominator spelling as-is and do not label it existing without an
actual analogous theorem. No upstream PR, production edit, or caller rewrite was performed.

Concrete future upstream design questions, requiring no interruption of the current overview:

1. Should Finsupp.weight expose a support-local monotonicity theorem in its generator family?
2. Should the constant-weight/degree upper bound be a named corollary of that API?
3. Should reciprocal estimates be left to division order lemmas, with Roth-specific denominator premises kept downstream?

YES PR file/title/grouping/reviewer requirements are n/a for this verdict. The Phase-7
BORDERLINE questions, complete search limitations and native verification are provided instead.
Portable validation: [validator](../evidence/Roth.weight_le_degree_div/validate.py),
[current manifest](../evidence/Roth.weight_le_degree_div/copy-manifest.json).
