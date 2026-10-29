# `LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine` — canonical290

Verdict: **BORDERLINE-needs-human**, completed assessment subject to root acceptance. Keep the exact LeanEval specification in `Roth/LeanEval.lean`; decide the upstream semantic API separately. This is an API-design judgment, not a cost judgment or an inherited verdict from Roth's theorem.

## Phase0 — baseline

The shared clean build completed2467 jobs. All17 current production source/pin hashes match its manifest, freshly checked before preparation and at freeze. Root alone executed native checks. No production source, pin, nine-import disk prefix, shared eighteen-import prefix or Git state was changed by this worker. Final project/LeanEval builds belong to root's final293 gate, not this definition's file boundary.

Evidence: [baseline-build.txt](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/baseline-build.txt), [inputs.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/inputs.json), [fresh-final-inputs.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/fresh-final-inputs.json), [prefix-controls.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/prefix-controls.json), [prefix-authorization.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/prefix-authorization.json).

## Phase1 — exact meaning and dependency scopes

Full native type: `ℝ → Prop`. The full body, with explicit input `x : ℝ`, is:

```lean
∀ ε : ℝ, 0 < ε → ∃ C : ℝ, 0 < C ∧
  ∀ (p q : ℤ), 0 < q →
    C / (q : ℝ) ^ ((2 : ℝ) + ε) < |x - (p : ℝ) / (q : ℝ)|
```

For every positive epsilon, one positive constant works uniformly for every integer numerator and every positive integer denominator. Constants may depend on x and epsilon. Exact rational approximations are included; consequently every satisfying x is irrational. There is no algebraicity hypothesis in this definition. The property expresses irrationality exponent at most2 for irrational reals; it is weaker than badly approximable, which demands a constant at exponent2 itself. The broader phrase Diophantine number sometimes means a bound at some finite exponent; this fixed2, every-epsilon predicate is more specific and must not be conflated with that usage.

The entire66-line LeanEval module and588-line Main module were read. Original replay copies just this definition into a fresh namespace, with native definitional equality `rfl`. Complete kernel body printing has no printer elision; full type/value constant inventories and standard axioms are archived. The mathematical body uses no other canonical project declaration. Its generated numeral helper `IsDiophantine._proof_1` is recorded separately rather than treated as a public project dependency.

Evidence: [native-type.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/native-type.json), [original-executed.lean.txt](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/original-executed.lean.txt), [original01-receipt.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/original01-receipt.json), [source-LeanEval.lean.txt](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/source-LeanEval.lean.txt), [source-Main.lean.txt](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/source-Main.lean.txt), [project-dependencies.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/project-dependencies.json).

The exact ordered canonical293 names were derived from tracked declaration-order, including private names with their defining modules; the pre-execution audit and runtime all293-present/all293-values checks passed. Direct kernel type and body consumers are precisely `LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff` and `.thueSiegelRoth`. Source statement occurrences agree. This distinguishes lexical scope, direct kernel scope, generated numeral helper, and transitive/simp closure; no claim to enumerate every external future consumer is made.

## Phase2 — size and one-line definition test

BIG: this introduces a named mathematical predicate, despite only two physical body lines and one substantive quantified formula. Semantic one-line result: **ONE-LINER WITH-EXEMPTION**.

| Exemption | Applies | Evidence |
|---|---|---|
| Avoid defeq abuse | no | No sealed computation barrier; native rfl unfolds it. |
| Avoid typeclass diamonds | no | No typeclass or instance is introduced. |
| Semantic intent / stable API | yes | Both actual consumers use the named predicate; the final theorem preserves the independent LeanEval problem statement. |

The exemption justifies a stable local API anchor; it does not automatically establish that upstream should receive this fixed2 name.

## Phase3 — exhaustive literature

All named channels were attempted; unavailable optional ask_chatgpt_math is justified n/a. Searches ran three distinct general queries plus an explicit mathlib4/lean4 API web search. Exact requests, status, response SHA256 and byte counts are archived without third-party article/search-result bodies. Query URLs carrying credentials were not retained; truncated URLs were omitted without guessing. Two concise inspection queries were repeated for fingerprinted archival; web-batch6/7 identify the actual recorded repeat responses.

| Channel | Exact query | Finding |
|---|---|---|
| web-specific | `Diophantine real number irrationality exponent at most 2 uniform lower bound epsilon Roth theorem definition` | Uniform lower bound is exactly the benchmark property. |
| web-general | `Diophantine type irrationality measure parameter rational approximation lower bound badly approximable distinction` | Parameterized irrationality exponents are standard; badly approximable differs by epsilon=0. |
| web-alias | `Roth type Diophantine number exponent epsilon strict uniform constant definition` | Roth type and irrationality measure terminology found. |
| nlab | `site:ncatlab.org/nlab irrationality measure Diophantine approximation` | Related irrational-number/number-theory pages; no exact sharp cutoff entry. |
| ncatlab | `site:ncatlab.org/ncatlab Diophantine approximation irrationality` | Returned out-of-namespace nLab material; exact irrationality-exponent refinement empty, no exact channel hit. |
| stacks | `site:stacks.math.columbia.edu Diophantine approximation irrationality` | Exact Diophantine approximation refinement empty; no relevant algebraic-geometric API. |
| mathoverflow | `site:mathoverflow.net irrationality exponent Diophantine Roth lower bound constant` | 498924 and457381 discuss uniform bounds and necessary irrationality. |
| arxiv | `site:arxiv.org irrationality exponent Diophantine approximation after:2021-10-29 before:2026-10-30` | Aaronson/Nakada2409.19393 (2024, revised2025) treats arbitrary irrationality exponents; no change to Roth cutoff2. |
| Optional ChatGPT math | standard form, generality, historical evolution | n/a: configured tool unavailable. |
| Local references | clean.tex: irrationality/Roth/approximation | Sections6/7 formulate infinite integer pairs; source search archived. |

- [Thue–Siegel–Roth theorem challenge](https://www.math-challenge.org/en/projects/thue_siegel_roth/problems/thue_siegel_roth), Statement and informal solution, lines10/23: Exact all-epsilon positive-constant specification; benchmark API must remain compatible.
- [LiouvilleWith mathlib4 documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleWith.html), Definition, exists_pos, mono, frequently_lt_rpow_neg, irrational, add_rat_iff, mul_rat_iff: API-rich denominator-frequency predicate excludes exact equality; rational low-exponent behavior prevents unguarded replacement.
- [Extravagance, irrationality and Diophantine approximation](https://arxiv.org/abs/2409.19393), Abstract; submitted2024-09-28, v5 2025-09-04: Arbitrary irrationality exponents occur for invariant measures; motivates parameterized cutoff rather than only2.
- [Diophantine approximation and expansions of real numbers](https://www.kurims.kyoto-u.ac.jp/~kenkyubu/bessatsu/open/B46/pdf/B46_010.pdf), Theorem2.3 and section3.1: Roth finiteness and irrationality exponent distinguished; p-adic generalizations require changed arithmetic data.
- [Diophantine approximation with powers](https://mathoverflow.net/questions/498924/diophantine-approximation-with-powers), Question: Uniform positive constants at2+epsilon appear in application questions.
- [Irrational number in nLab](https://ncatlab.org/nlab/show/irrational%2Bnumber), Definition/strong irrationality: Related irrationality context, not an exact cutoff definition.

Literature summary: irrationality exponent/measure and Roth-type approximation are established names. The standard family allows a real exponent cutoff; fixed2 is singled out by Roth's theorem. Natural-positive and signed integer denominators are normalization choices. The reduced-rational-denominator proof uses2+epsilon>0 and is not claimed for arbitrary negative cutoff. Rational-denominator height is valid here; replacing denominator height by projective max(num,den) height would require additional x-dependent comparison, and is not claimed as a verified equivalence. Number-field, p-adic, simultaneous and weighted generalizations require different arithmetic data and are not automatic weakenings.

Evidence: [literature.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/literature.json), [literature-local.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/literature-local.json), [local-source-section6.tex.txt](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/local-source-section6.tex.txt), [local-source-section7.tex.txt](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/local-source-section7.tex.txt), [web-batch0.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/web-batch0.json), [web-batch1.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/web-batch1.json), [web-batch2.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/web-batch2.json), [web-batch3.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/web-batch3.json), [web-batch4.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/web-batch4.json), [web-batch5.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/web-batch5.json), [web-batch6.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/web-batch6.json), [web-batch7.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/web-batch7.json).

## Phase4a/b — generality

| Input/condition | Current | Assessment |
|---|---|---|
| x | real | Real rpow and rational approximation are essential to this specified predicate; no extraneous algebraicity assumption. |
| epsilon | every positive real | Replacing forall by exists changes the meaning to a much weaker non-Liouville condition; reject. |
| numerator | integer | Arbitrary integers are required; reduced rationals provide verified alternative presentation. |
| denominator | positive integer | Natural-positive and signed-nonzero absolute denominator presentations verified; q=0 must not be added. |
| lower constant | exists C>0 for each epsilon | Fixed C across all epsilon or epsilon=0 strengthens the property; allowing C=0 reduces the bound to irrationality and admits Liouville numbers; strict/nonstrict positive bounds are equivalent after halving. |
| cutoff2 | fixed real numeral | Parameter t gives `UniformBound t x`; full original formula recovered definitionally at t=2. |

There is no external hypothesis/typeclass to weaken mechanically. Parameterization is a genuine wider API design, natively established; it is not being called a dropped-hypothesis improvement. A new scalar cutoff affects which property callers express. The benchmark's name and exact namespace remain a stable compatibility surface.

## Phase4c — nine modern-idiom checks

| Question | Result | Concrete consequence / guard |
|---|---|---|
| Typeclasses | no | A real-number property is not an ambient structure; no instance should register arithmetic truth. |
| Filters | yes | LiouvilleWith uses frequently atTop; retain Irrational x in the equivalence. Enables existing mono/add_rat_iff/mul_rat_iff. |
| Universal property | no | No constructed object or universal mapping problem. |
| Bundled substructure | no | The satisfying set is not shown closed under addition/multiplication; no justified Subring bundle. |
| Hierarchy weakening | no | The predicate uses real rpow and real rational approximation, not just field axioms; generic valued-field replacement changes the problem. |
| Higher categories | no | No categorical data or coherence. |
| Concrete index | yes | Positive integer denominators may be natural; nonzero signed denominators require absolute value. Parameter t in the cutoff enables monotonicity. |
| Concrete-via-abstract | yes | Definition body uses numeral2 once, in 2+epsilon; replacing with t is mechanically well-formed. UniformBound.cutoff_mono supplies concrete consequence and t=2 recovers original. |
| False-generalization guard | reject unguarded proposal | Irrationality is essential: rational0 fails uniform bound but satisfies forall p LiouvilleWith p 0 -> p<=2. Also p<=1 LiouvilleWith holds for all reals. Badly approximable at exponent2 is stronger. |

The tested modern semantic statement is:

```lean
UniformBound t x ↔ Irrational x ∧
  ∀ {p : ℝ}, LiouvilleWith p x → p ≤ t
```

This uses the existing filter predicate but the equivalence proof is new. It reconstructs the integer-pair predicate using genuine mathlib operations, proves finite bounded-denominator sets, converts denominator frequency to pair infinitude, takes a positive minimum over finite exceptions, and absorbs constants across a strict exponent gap. Pair/exponent helper structure is adapted with credit from accepted canonical288 scratch `modern2-executed.lean.txt`; this is reused proof syntax for a new generic proof, not an existing mathlib Roth theorem or an inherited verdict.

Concrete verified consequences are `cutoff_mono` for s≤t and rational affine invariance (`add_rat_iff`, `mul_rat_iff` with nonzero multiplier). The complete fixed2 formula is recovered, while `rational_cutoff` proves the cutoff family at every rational, `¬UniformBound 2 0` refutes the unguarded equivalence, and `liouvilleWith_one`/`mono` explicitly test p≤1. No algebraicity was smuggled into the property.

Evidence: [modern3-executed.lean.txt](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/modern3-executed.lean.txt), [modern03-receipt.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/modern03-receipt.json), [mathlib-inputs.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/mathlib-inputs.json).

## Phase4.5 — six infrastructure risks

| Risk | Level | Evidence |
|---|---|---|
| Typeclass diamond | none | Plain Prop-valued def; registers no class or instance. |
| Reducibility leak | low | Ordinary semireducible def; rfl unfolds the quantifier formula, natively checked; no reducible attribute or computational reduction. |
| Non-canonical unfolding | low | Named benchmark predicate unfolds intentionally in proofs; no simp attribute forces unexpected orientation. |
| Instance priority collision | none | No instance or priority. |
| Universe polymorphism | none | The full type is Real -> Prop; fixed real semantics are intentional, no universe parameter to constrain. |
| Coercion ambiguity | low | Integer-to-real casts explicit; denominator representation bridges natively check natural/rational casts; no new coercion. |

Overall LOW, no HIGH rows. Native rfl and failed instance-synthesis probes accompany the structural analysis; universe and CoeFun/CoeeSort probes are inapplicable to the fixed Real -> Prop signature, which introduces neither classes nor coercions.

## Phase4.6 — five proof-strategy checks

| Question | Applies | Assessment |
|---|---|---|
| Topology neighborhoods | no | Definition, no topology proof; filter expression is compared natively. |
| Algebra elements | no | No ideal/submodule argument. |
| Analysis sequences | yes | Frequency of denominators is natural for exponent cutoffs; requires finite-small-denominator bridge to full uniform bound. |
| Category construction | no | No universal property. |
| Missing helpers | yes | General uniform-bound iff irrationality-plus-LiouvilleWith cutoff, finite exceptional approximation minimum and rational-affine transport are natural bridge API; present scratch proofs are new content. |

The definition itself has no proof strategy. For upstream supporting API, REFACTOR-RECOMMENDED: provide the generic filter/constant bridge once, allowing rational-affine consequences from existing LiouvilleWith invariance rather than duplicate numerator arithmetic. This is a concrete new bridge, not a claim that filters alone solve finite-exception bounds.

## Phase5 — all15 formal cells

All current / literature-standard / abstract forms were searched by Lean-Finder, Loogle, LeanSearch, full source rg and root-executed local search. The malformed free-x Loogle attempt is preserved separately; a corrected fully quantified query returned clean empty results. Local index states were error/error/warming; these do not support absence. Semantic search index revisions differ from this pin; positive candidate signatures were independently checked against pinned sources and native checks.

| Form | Finder | Loogle | LeanSearch | rg | local |
|---|---|---|---|---|---|
| current | [formal-current-leanfinder.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/formal-current-leanfinder.json) | [formal-current-loogle-retry.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/formal-current-loogle-retry.json) | [formal-current-leansearch.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/formal-current-leansearch.json) | [formal-current-rg.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/formal-current-rg.json) | [formal-current-local.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/formal-current-local.json) |
| standard | [formal-standard-leanfinder.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/formal-standard-leanfinder.json) | [formal-standard-loogle.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/formal-standard-loogle.json) | [formal-standard-leansearch.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/formal-standard-leansearch.json) | [formal-standard-rg.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/formal-standard-rg.json) | [formal-standard-local.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/formal-standard-local.json) |
| abstract | [formal-abstract-leanfinder.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/formal-abstract-leanfinder.json) | [formal-abstract-loogle.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/formal-abstract-loogle.json) | [formal-abstract-leansearch.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/formal-abstract-leansearch.json) | [formal-abstract-rg.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/formal-abstract-rg.json) | [formal-abstract-local.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/formal-abstract-local.json) |

Closest API is `LiouvilleWith`, especially `exists_pos`, `mono`, `frequently_lt_rpow_neg`, `irrational`, `add_rat_iff`, `mul_rat_iff`. `Liouville` only asks arbitrarily strong approximation; its negation is insufficient for cutoff2. `Dioph`/`DiophFn` concern integer-polynomial representability, an unrelated same-word collision. `ae_not_liouvilleWith` is a measure-almost-everywhere statement, not this pointwise definition or Roth's algebraic result. The generic exact? probe before introducing the new bridge does not close its equivalence. Full-name grep is untruncated. Search conclusion: partial API match, no verified exact existing definition; it is not proof of global absence.

Evidence: [formal-search-matrix.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/formal-search-matrix.json), [full-name-search.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/full-name-search.json), [mathlib-source-0.lean.txt](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/mathlib-source-0.lean.txt), [mathlib-source-1.lean.txt](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/mathlib-source-1.lean.txt), [mathlib-source-2.lean.txt](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/mathlib-source-2.lean.txt), [mathlib-source-3.lean.txt](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/mathlib-source-3.lean.txt).

## Phase5.5 — statement shape

| Check | Result | Evidence |
|---|---|---|
| Normal form | RESTATEMENT-CHOICE | Uniform positive bound, rational-denominator bound, and irrationality-plus-cutoff are compared. Existing LiouvilleWith is API-rich but not the full predicate; no existing exact canonical bound predicate found. |
| Syntactic generality | VERIFIED-ALTERNATIVES | Natural-positive denominators, signed nonzero absolute denominators, strict/nonstrict via halving and reduced rational-denominator forms tested natively. |
| Superfluous arguments | NONE | Only explicit input is x:Real; epsilon positivity and q positivity are quantified defining conditions, not discardable external hypotheses. No algebraicity assumption occurs. |

Native exact alternatives cover natural-positive denominators; signed q≠0 with absolute denominator, including negative q; strict versus nonstrict positive bounds using C/2; and reduced rational denominator height r.den. None is an unproved name analogy. Overall RESTATE-BEFORE-SHIP concerns upstream API choice; the benchmark-compatible statement stays intact.

Evidence: [shape2-executed.lean.txt](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/shape2-executed.lean.txt), [shape02-receipt.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/shape02-receipt.json).

## Phase6.0 — full actual callers and inline audit

| Caller | Source | Explicit occurrences | Current role | Refactor action |
|---|---|---|---|---|
| LeanEval...isDiophantine_iff | LeanEval:42–57 |1 statement| Uniform bound vs infinite-pair cutoff | Keep full signature; define bridge through generic t=2 only if upstream API chosen. |
| LeanEval...thueSiegelRoth | LeanEval:61–64 |1 statement| Benchmark endpoint | Keep namespace, x and both original assumptions; recover exact bound from any modern endpoint using the irrationality input. |

Both have direct kernel type and body dependencies; there are no additional production source consumers. A complete original LeanEval module replay, with namespace substitution only, verifies full original caller proof bodies including the private helper and preserves signatures modulo native rfl. Both replayed caller types/values are free of the original target. Inlining here is the mathematically identical expanded formula behind the fresh definition; it establishes compatibility, not a replacement theorem from existing mathlib.

Evidence: [source-search.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/source-search.json), [tracked-source-search.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/tracked-source-search.json), [inline-search.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/inline-search.json), [callers.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/callers.json), [callers-executed.lean.txt](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/callers-executed.lean.txt), [callers01-receipt.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/callers01-receipt.json).

## Phase6 — composition and moral duplication

The quantified arithmetic formula can be pasted at both caller statements without changing their proofs, but naming it records semantic intent and benchmark compatibility. Existing LiouvilleWith alone does not define the same property: omitting irrationality provably changes rational cases. Obtaining the exact uniform-bound equivalence requires new finite-exception and exponent-gap proofs, not≤3 existing mathlib calls. The affine consequence proofs compose only after this new bridge; they cannot be represented as existing-mathlib replacements for the definition. Composition conclusion: NOT-COMPOSABLE from verified existing semantic API in≤3 calls. Moral overlap with Roth.approxSet is a genuinely proved alternate presentation, not definitional identity. No junk/dead-code diagnosis follows from the short body; both real callers depend on the stable predicate.

## Phase7 — verdict and actionable future questions

BORDERLINE-needs-human. The predicate is mathematically standard in its benchmark context and its one-line semantic exemption is real. The verified family exposes reusable cutoff monotonicity and rational-affine invariance. Choosing whether mathlib should add a named lower-bound family, simply use an irrationality conjunct plus the existing exponent predicate, or add only their bridge is an upstream API decision. This crosses a foundational interface, so it is not asserted to be a single dropped-hypothesis edit. No verdict is inherited from the enclosing Roth theorem and no cost/time criterion is used.

1. Should upstream introduce a named parameterized predicate `UniformBound (t x : ℝ) : Prop`, or keep `Irrational x ∧ ∀ {p}, LiouvilleWith p x → p ≤ t` as its canonical expression?
2. If a named predicate is wanted, should it use natural-positive denominators, with integer/signed/rational formulations supplied only as equivalence lemmas?
3. Should the fixed2 `IsDiophantine` name remain solely in the LeanEval compatibility module while the generic bridge and invariance API live upstream?

These are concrete future upstream questions, not unresolved assessment work or a request to stop the project. Preserve `Roth/LeanEval.lean` as the local destination. A candidate home for the eventual bridge/family is `Mathlib/NumberTheory/Transcendental/Liouville/Diophantine.lean`, importing LiouvilleWith. Recent related-file commit evidence is retained for a future reviewer decision; no YES PR grouping is claimed. Evidence: [reviewer-commits.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/reviewer-commits.json).

## Phase8 — verification and handoff

Accepted exact sources and raw root-native requests/results, rejected attempts, elapsed times, standard axioms, exact293 audit, all17 hashes and portable manifest/layout/secret gates are indexed in [verification.json](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/verification.json). Failed modern01, modern02 and shape01 are retained separately and not counted as accepted proof evidence; their recovered sorryAx is rejected. Accepted receipts must contain no PANIC even in info diagnostics. Current-manifest validation applies in scratch and integrated layouts; historical worker manifests never replace it. Production sources/pins remain unchanged. Root acceptance is pending.
