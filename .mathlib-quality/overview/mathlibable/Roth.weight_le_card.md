# Roth.weight_le_card — full mathlibable assessment

**Verdict: BORDERLINE-needs-human.** The original natural-coefficient, real-valued interface needs natural-cast order certificates as well as the finite-sum bound. A generic field-valued finite-sum version uses three existing facts. The support-cardinality version of `Finsupp.weight` is a plausible upstream API question, rather than an established missing theorem. No dedicated analogous upper-cardinality law for the re-aimed parent was located. This assessment is complete; the questions below concern future API design and do not block this read-only survey.

## 0. Baseline and identity

Canonical declaration 36 is public theorem `Roth.weight_le_card`, actual head `Roth/Box.lean:103`, body through line 107. Canonical metadata and source were independently checked: [metadata](../evidence/Roth.weight_le_card/canonical-metadata.json), [whole declaring module](../evidence/Roth.weight_le_card/Box-source.lean.txt). It is neither private nor glue, and the namespace-aware mathlib search did not find the qualified declaration.

The successful 2467-job baseline is reused only after freshly hashing all 17 source/pin files: [baseline](../evidence/Roth.weight_le_card/baseline-build.txt), [input manifest](../evidence/Roth.weight_le_card/input-manifest.json), [fresh check](../evidence/Roth.weight_le_card/input-check.json). Source and reference hashes are in [source hashes](../evidence/Roth.weight_le_card/source-hashes.json). Root's terminal native checks, with no errors/warnings and standard axioms, verify the actual declaration and independent proofs: [verification](../evidence/Roth.weight_le_card/verification.json).

## 1. Comprehension

Elaborated type, including every retained parameter:

```lean
@Roth.weight_le_card : ∀ {σ : Type u} [Fintype σ] {r : σ → ℕ} {d : σ →₀ ℕ},
  (∀ j, d j ≤ r j) → Roth.weight r d ≤ (Fintype.card σ : ℝ)
```

`DecidableEq σ` from the module preamble is omitted; it is not an implicit theorem parameter. `weight r d` is the real sum of the normalized coordinates. Each numerator is bounded by its denominator, so every ratio is at most one, including denominator zero under Lean's totalized division. Summing gives the number of coordinates. No strict positivity of `r` is required. The only project dependency in the statement/proof is `Roth.weight`; the proof uses generic sum and division inequalities. The hypotheses do not mention a polynomial, a point, Taylor coefficients, or nonvanishing. Those enter at the sole caller.

## 2. Preliminary checks

BIG under the command’s presentation-based rule: `Roth.weight_le_card` is explicitly listed in the declaring module’s `## Main results` at `Roth/Box.lean:32`. Its mathematics is elementary finite-sum arithmetic; that observation does not override the protocol’s BIG criterion. The classification is narrative evidence only. One-line-definition test is **n/a: theorem**, not a `def`/`abbrev`/instance. The fact that the source fits into a short proof is not a replacement certificate. Its API signal is one explicit caller, no simp attribute, and no duplicated inline derivation found by the audited source searches.

## 3. Exhaustive literature search

Every named channel was attempted. Three distinct general-web requests, the local reference, nLab, nCatLab, Stacks, MathOverflow and recent arXiv are recorded separately; the protocol's informal channel count is not repaired by inventing a synthesis channel. ChatGPT mathematical second-opinion capability is unavailable in this session.

| Channel | Exact request/evidence | Finding |
|---|---|---|
| General web, current form | [web0](../evidence/Roth.weight_le_card/web0-metadata.json) | Roth index literature uses normalized derivative multi-indices and coordinate degree bounds. |
| General web, standard form | [web1](../evidence/Roth.weight_le_card/web1-metadata.json) | Broad bounded-summand query also returned irrelevant sumset results; no claim of theorem absence follows. |
| General web, abstract form | [web2](../evidence/Roth.weight_le_card/web2-metadata.json) | Finite support and weighted sums are the relevant abstract vocabulary. |
| Local clean.tex | [excerpts](../evidence/Roth.weight_le_card/caller-literature-excerpts.json) | §5, lines 666–667 explicitly uses a nonzero derivative with coordinate bounds and weight at most the number of variables. §4 defines the sum. |
| nLab | [web3](../evidence/Roth.weight_le_card/web3-metadata.json) | Polynomial degree page located. Direct fetch failed: unsupported XHTML content type, HTTP 400. |
| nCatLab | [web4](../evidence/Roth.weight_le_card/web4-metadata.json) | Finite support/distribution/mean material; no matching normalized-coordinate upper bound established. Same host as nLab, independently queried. |
| Stacks Project | [web5](../evidence/Roth.weight_le_card/web5-metadata.json) | Polynomial algebra/degree hits. Opened tag 00NO is about associated graded rings of regular local rings, not this bound. |
| MathOverflow | [web6](../evidence/Roth.weight_le_card/web6-metadata.json) | Diophantine approximation and Roth context, no sharper matching API formulation established. |
| arXiv, last five years | [web7](../evidence/Roth.weight_le_card/web7-metadata.json) | Explicit 2022–2026 query; recent polynomial Roth/corners results concern additive combinatorics, not this normalized index inequality. |
| ask_chatgpt_math | Unavailable | No tool exposed; no invented response. |

Representative primary-source access is documented in [open0](../evidence/Roth.weight_le_card/web-open0-metadata.json) and [open1](../evidence/Roth.weight_le_card/web-open1-metadata.json). Soundararajan's *Transcendental Number Theory* notes, recorded by Petrow (2011), provide the Roth auxiliary-polynomial context: [notes](https://math.stanford.edu/~ksound/TransNotes.pdf). The recent arXiv distinction was checked against Chen–Guo's July 2023 [polynomial corners paper](https://arxiv.org/abs/2307.00271). These contextual sources do not establish novelty for an elementary sum bound.

Literature-standard mathematical content: a finite sum of quantities individually bounded by one is bounded by its number of terms. The project spelling is a normalized natural multi-index instance. Primary local source supports the intended application directly; the more abstract formulation is grounded independently in mathlib's finite-sum API. Only requests, response hashes/byte sizes, locators and concise original summaries are archived; full returned web bodies are not persisted. Returned URL query parameters are omitted, and redactions are documented.

## 4a–4b. Generality and verified changes

| Parameter or hypothesis | Current role | Checked generality result |
|---|---|---|
| `σ : Type*` | Arbitrary universe | Already universe-polymorphic; no restriction to a numeric index. |
| `[Fintype σ]` | Needed by `Roth.weight` and ambient cardinality | Fixed-parent constraint. The `Finsupp.weight` support version removes ambient finiteness entirely. |
| `r : σ → ℕ` | Natural denominators | Nonnegative cast automatic, zero allowed. Arbitrary field denominators require explicit nonnegativity on the summation set. |
| `d : σ →₀ ℕ` | Natural coefficients | Finite ordinary functions into an ordered field also work. This is a representation extension, not dropping a theorem typeclass. |
| `hd : ∀ j, d j ≤ r j` | Ratio bound | Support-local restriction is equivalent over ℕ: outside support, `d j=0≤r j`. Root compiled both directions. It is **not** a strict hypothesis weakening. |
| RHS ambient cardinality | Counts all variables | Stronger conclusion `weight r d ≤ d.support.card` compiled; a Bool/singleton witness verifies strictly smaller support is possible. |
| Zero denominators | Ratio contributes zero | The actual weaker condition can ignore bounds at zero denominators; see native extra checks described in verification. |
| `[DecidableEq σ]` | None in elaborated type | Already omitted. Classical support manipulations need no additional public assumption. |

The exact accepted sources are [raw](../evidence/Roth.weight_le_card/raw-executed.lean.txt) and [project](../evidence/Roth.weight_le_card/project-executed.lean.txt). The raw support statement is:

```lean
theorem support_bound (r : σ → ℕ) (d : σ →₀ ℕ)
    (hd : ∀ j ∈ d.support, d j ≤ r j) :
    Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹) d ≤ d.support.card
```

The field statement uses `[Field K] [LinearOrder K] [IsStrictOrderedRing K]`, a finite set `s`, field-valued functions `d r`, and `hd`/`hr` only on `s`. Division and its sign conditions remain essential: the native example `(-2)/(-1)=2` rejects removal of denominator nonnegativity even when `-2≤-1`. Dropping coordinate bounds altogether is false (`Unit`, `r=1`, `d=2`); `r=0,d=17` confirms totalized division must be preserved. No positivity of every parameter should be silently added to an upstream restatement.

Verdict: the original bound hypothesis has a verified one-edit strict weakening to nonzero-denominator coordinates. Independently, changing the foundational parent representation is a multi-declaration design choice. These generalizations are real; they do not establish a missing upstream API or force a YES verdict for an elementary convenience law. No cost-based downgrade is used.

## 4c. All nine modern-idiom checks

| # | Question | Answer and concrete consequence |
|---|---|---|
| 1 | Replace preambles with typeclasses? | No additional class needed; finiteness is already a class, inequalities properly value hypotheses. |
| 2 | Filters/nets instead of sequences? | No topology or convergence. |
| 3 | Universal-property formulation? | No object constructed; an inequality does not need a universal-property class. |
| 4 | Bundled substructures instead of closure predicates? | No closure predicate. `Finsupp` is already bundled finite support. |
| 5 | Weaken field/space hierarchy? | Yes, abstract finite-sum bound needs only ordered additive structure; ratios add ordered division. Accepted field version makes the real-specific proof reusable over ℚ. |
| 6 | Higher-categorical restatement? | No categorical structure. |
| 7 | Generalize concrete index? | `σ` already arbitrary; the concrete scalars can be replaced as in the field proof. |
| 8 | Concrete-via-abstract diagnostic? | Yes. Proof body contains zero occurrences of `Roth.weight` or real-specific analytic facts; unfolding exposes only sum/division/order. `Finset.sum_le_card_nsmul` is the existing abstract theorem. The `Finsupp.weight` bridge removes ambient `Fintype` and enables infinite variable types with finite support. |
| 9 | False-generalization guard? | No semantic mismatch for the accepted field/support statements: the bridge preserves exactly the original sum. Reject negative-denominator widening and unrestricted coefficients with no term bound. Support localization is not falsely advertised as strict weakening. |

Modern-idiom verdict: use existing generic sum infrastructure and consider a support-bound convenience API against `Finsupp.weight`; no new algebraic bundle is needed. The bridge is propositional, established by `weight_eq_sum`, `nsmul_eq_mul`, and division-to-inverse normalization, **not definitional equality**.

## 4.5. Infrastructure risks

All six rows are **n/a: theorem**, which adds no data, instance, or coercion: typeclass diamond; reducibility leak; noncanonical unfolding; instance-priority collision; universe-polymorphism construction risk; coercion ambiguity. The parent `Roth.weight` has its own assessment; this theorem does not create another implementation of it.

## 4.6. Proof strategy

| Check | Result |
|---|---|
| Topology: ε–δ versus filters | n/a: finite algebraic sum. |
| Algebra: elements versus substructures | No gain from ideal/submodule language; termwise bounds are the exact primitive. |
| Analysis: sequences versus nets | n/a: no limits. |
| Category theory: construction versus universal property | n/a: no object construction. |
| Missing helper API | No missing helper needed for this proof; `sum_le_card_nsmul` already packages the summation step. A `Finsupp.weight` support-cardinality convenience theorem is a design candidate, not proven absence. |

Strategy verdict: **KEEP** the termwise bound strategy; use the existing cardinality-sum theorem if inlining. No sophisticated proof method is missing.

## 5. All five actual mathlib methods, three forms

The complete raw requests and tool responses are preserved: [current](../evidence/Roth.weight_le_card/search-current.json), [literature](../evidence/Roth.weight_le_card/search-literature.json), [abstract](../evidence/Roth.weight_le_card/search-abstract.json), [source searches](../evidence/Roth.weight_le_card/source-search.json). Finder, LeanSearch, Loogle and local name search were actually invoked on each form; rg source inspection supplies the fifth method for each.

| Method | Current form | Literature-standard form | Abstract/re-aimed form |
|---|---|---|---|
| Lean-Finder | Pigeonhole/sum bounds, no exact hit | Bounded fiber sums | `Finsupp.le_weight` and variants are lower bounds, wrong direction. |
| Loogle | Initial query errored; [retry](../evidence/Roth.weight_le_card/search-current-loogle-retry.json) checks ratio bound | Exact `Finset.sum_le_card_nsmul` signature hit | Initial pattern errored; [retry](../evidence/Roth.weight_le_card/search-abstract-loogle-retry.json) checks weight API. |
| LeanSearch | `Finset.sum_le_card_nsmul` | Multiset analog and unrelated weighted homogeneous API | Lower bounds and `weightedOrder_le`, no matching upper support-cardinality result. |
| rg | Full qualified and bare target search, no duplicate | Generic sum bound source and generated additive name | Read full `Data/Finsupp/Weight.lean`, inspected `Order.lean`; no dedicated upper-cardinality weight law found. |
| Local search | Empty, index unavailable | Empty, index unavailable | Source results include weight/weight_eq_sum/weight_single; index unavailable. |

Local index unavailability is recorded honestly and is not absence evidence. External service snapshots can differ from the pinned revision; the positive candidates and accepted proofs were checked natively against the project's pinned mathlib.

Pinned building blocks: `Finset.sum_le_card_nsmul`, generated by `@[to_additive]` from `prod_le_pow_card` at `Mathlib/Algebra/Order/BigOperators/Group/Finset.lean:285`; `div_le_one_of_le₀`; `Nat.cast_le`; `Nat.cast_nonneg`; `nsmul_one`. `Finsupp.weight_eq_sum` is at `Mathlib/Data/Finsupp/Weight.lean:100`, `weight_apply` at line 85. Native receipts supply exact signatures and axioms.

Parent re-aim gate: parent `Roth.weight` is already assessed NO-mathlib-has-it via `Finsupp.weight`. We independently verified the reciprocal-weight representation bridge and searched for the analogous **upper** law. Existing `le_weight` is not that law and cannot trigger automatic NO. The generic Finset theorem gives the expanded finite-sum inequality but a representation bridge and coefficient/sign certificates remain. No claimed exact absence is inferred from search failure, and no new helper is counted as an existing library replacement.

## 5.5. Statement-shape checks

Normal form: inequality orientation is conventional and supports transitivity at the caller. No iff-side normalization issue. Syntactic-generality attempt: support-local bound and support cardinality were compiled, plus field-valued finite-set representation; the former hypothesis is equivalent and the conclusion genuinely stronger. Superfluous-argument audit: `σ`, `Fintype`, `r`, `d`, `hd` all matter in the current parent interface; no `DecidableEq` remains. Zero-denominator coordinates permit the actual weaker hypothesis `∀ j, r j ≠ 0 → d j ≤ r j`, verified separately with a strictness witness. Overall **RESTATE-BEFORE-SHIP** if upstreaming: target `Finsupp.weight` or generic Finset infrastructure, not the project-specific parent.

## 6.0. Every explicit caller and inline audit

| Caller | Location | Usage and action |
|---|---|---|
| `Roth.index_le_card` | `Roth/Index.lean:227` | Obtain an attained nonzero Taylor coefficient, establish `d j≤r j` by monomial degree and translated degree bounds, then substitute `hdw : weight r d=index P α r`. If deleting the local theorem, inline the accepted termwise finite-sum argument at this exact substitution. |

K=1 source-level explicit call. `Box.lean:32` is documentation, line 103 is the declaration; neither is a caller. Internal declaring-file use count is zero. Full modules were read, not just snippets. No matching independent inline derivation was located by the archived source queries. This is source-level evidence, not an assertion about kernel dependency or simp closure. The target has no simp attribute.

Root compiled `WeightLeCardExtra.attained_index`, matching the actual `hdw ▸ ...` use, an original-parent support-bound proof, and `WeightLeCardWeaker.attained_weaker`, adapting global bounds to the strict weakening via `fun j _ ↦ hd j`. The fragment verifies the replacement/substitution shape with arbitrary attained value and coordinate bound. It deliberately does not claim to rebuild a migrated production `Roth.Index` or prove its unrelated Taylor-degree premises anew.

## 6. Composition experiments and honest counts

The accepted mathlib-only `original_composition` is:

```lean
(Finset.sum_le_card_nsmul Finset.univ (fun j ↦ (d j : ℝ) / r j) 1
  (fun j _ ↦ div_le_one_of_le₀ (by exact_mod_cast hd j)
    (Nat.cast_nonneg _))).trans_eq (nsmul_one _)
```

This is **at least five distinct arithmetic facts**, not three: the sum bound, ratio bound, natural-cast order transport used by `exact_mod_cast`, nonnegativity of natural casts, and nsmul-one normalization. There may be additional elaboration/normalization infrastructure; the report claims no minimality theorem. `.trans_eq` is structural composition, not a substitute for counting the hidden cast certificate. The source proof similarly needs cast and constant-sum normalization.

For the generic field statement with inequalities already in the field, the exact term uses three facts: `sum_le_card_nsmul`, `div_le_one_of_le₀`, `nsmul_one`. That experiment is valid but does not erase the original natural-cast premises. The reciprocal-weight representation bridge closes by simp using four named normalization facts; it is explicitly a normalization proof, not a direct pre-existing theorem about this bound. Phase 6b therefore does not certify original-form NO-composable on the strength of a short simp script. Result: **BORDERLINE normalization/API granularity**, with a verified generic route, rather than unsupported exact presence or fabricated absence.

## 7. Actionable verdict

**BORDERLINE-needs-human.** The implementation is mathematically elementary, has one real consumer, and is provably covered by existing finite-sum infrastructure after supplying cast/sign certificates. The old spelling exceeds the literal three-fact certificate; re-aim did not find a dedicated analogous `Finsupp.weight` upper law. The remaining issue is whether a support-local upper-bound convenience API is worth adding, not proof correctness or cost.

1. Should mathlib add a `Finsupp.weight` upper bound by support cardinality under pointwise bounds on `d j • w j`, or keep such proofs in the Finset sum API?
2. If a Finsupp theorem is wanted, should its reusable conclusion be `weight w d ≤ d.support.card • b` for ordered additive targets and arbitrary bound `b`?
3. Should this project's sole caller inline the arithmetic proof while the parent representation migration is considered?

Future upstream design anchor: `Mathlib/Data/Finsupp/Weight.lean`, alongside the existing lower-bound API, with ordered sums from `Mathlib/Algebra/Order/BigOperators/Group/Finset.lean`. No unconditional YES, PR grouping, or reviewer selection is proposed because that would pre-judge these API questions. Alternative destination is the current project-local `Roth/Box.lean`: normalized degree bookkeeping is directly tied to Roth's index construction. If deletion is chosen, update the sole caller `Roth.index_le_card:227` using the verified substitution and arithmetic term above, and remove the corresponding module-doc bullet. No production edits were made.

## 8. Completion and verification

All required phases passed or have explicit theorem-only n/a. Accepted raw proof has `#check_failure Roth.weight_le_card`, imports only mathlib, and uses no project theorem, sorry, unsafe code, native_decide or limit raises. Project checks are noncircular: replay uses generic facts, and the consumer uses that independently replayed proof. Rejected import/class and support-normalization attempts are retained separately; accepted receipts show terminal success, with no partial elaboration or unproved axiom. Exact source equality, baseline/source hashes, current copy-manifest hashes/bytes, report links, and credential safety are checked by [validator](../evidence/Roth.weight_le_card/validate.py). Root acceptance remains pending independent review.
