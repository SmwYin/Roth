# `Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul` — canonical253

Verdict: **BORDERLINE-needs-human**. Assessment completed; production and pins unchanged. The ordered arithmetic is valid and admits a verified positive-scale abstraction. Evidence does not establish that this particular budget-transfer family warrants a named mathlib API. The unused strict specialization also no longer matches the weak boundary needed by the related theta proof. These are API questions, not unfinished proof work or a cost-based downgrade.

## Phase0 — baseline and scope

The shared build succeeded with2467jobs; fresh hashes of all17 source/pin files match its manifest. No new file-end build is scheduled at253 (next266). The target resolves at `Roth/MainLemma.lean:433`, has no sorry, and belongs to the module constructing Roth's auxiliary polynomial. The whole762-line declaring module was read. Full original module replay compiles with identical target signature and standard axioms. [`inputs.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/inputs.json), [`baseline-build.txt`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/baseline-build.txt), [`source-MainLemma.lean.txt`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/source-MainLemma.lean.txt), [`original-executed.lean.txt`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/original-executed.lean.txt), [`original-receipt.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/original-receipt.json).

## Phase1 — exact mathematics

In a linearly ordered semifield satisfying the displayed compatibility assumptions, suppose the positive scale `2m+1` is at most `δ²L`, while `δm<1`. Then `m(2m+1)/δ<L`. Neither δ nor m is assumed positive. The scale/budget force δ nonzero. Multiply the desired inequality by its positive square, normalize the left side to `(δm)(2m+1)`, use strict contraction below1, and then use the budget.

Full native type, obtained from `Lean.getConstInfo.type` under `pp.funBinderTypes=true`:

```lean
∀ {K : Type u_1} [inst : Semifield K] [inst_1 : LinearOrder K] [IsStrictOrderedRing K]
  [ExistsAddOfLE K] {δ m L : K}, 0 < 2 * m + 1 → δ * m < 1 → 2 * m + 1 ≤ δ ^ 2 * L → m * (2 * m + 1) / δ < L
```

`K` is universe polymorphic; `δ,m,L` are arbitrary scalars. The native type contains no project definition. The body contains no canonical project dependency. The kernel printer elided4115characters in `#print`; this is **not** a full kernel-body dump. Complete written source, full native type/axioms, and exact canonical kernel-value audit remain archived. [`native-type.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/native-type.json), [`dependencies.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/dependencies.json).

## Phase2 — size and one-line check

SMALL: this is an arithmetic helper, not a new structure or the project's main theorem. The definition-only one-line test and its defeq/diamond/API exemptions are n/a: the declaration is a theorem. Small size does not narrow literature search or determine the verdict.

## Phase3 — exhaustive literature

The local primary source `clean.tex`, §6, Lemma `lem:lem7-satisfied`, lines1330–1335 explicitly derives the Lemma7 threshold from equations29 and32. It has positive δ and natural positive m. The Lean theorem already abstracts away real logarithms and strengthens the budget boundary to weak ≤. The arbitrary positive scale is a proof-grounded abstraction, **not** a literature-named theorem discovered by search. [`local-excerpt.tex.txt`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/local-excerpt.tex.txt), [`literature-local.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/literature-local.json), [`literature-local-input.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/literature-local-input.json).

| Executed channel | Finding / limit | Receipt |
|---|---|---|
| General1: Roth Lemma7 δ log q threshold | Located Roth numerical parameter literature and Princeton seminar notes; delta-function false positives excluded | [`web-general1.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/web-general1.json) |
| General2: auxiliary-polynomial logarithmic budget | Located number-theory notes; additive-combinatorics Roth results concern another theorem | [`web-general2.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/web-general2.json) |
| General3: ordered-field positive-square clearing | Found general sign/order accounts, not a named quadratic-budget implication | [`web-general3.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/web-general3.json) |
| Local references | Exact project source anchor above, fresh hash retained | [`literature-local.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/literature-local.json) |
| nLab | Ordered field / inequality pages, no exact named helper | [`web-nlab.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/web-nlab.json) |
| distinct nCatLab namespace | Actual `site:ncatlab.org/ncatlab` query returned /nlab material instead; no in-namespace match established | [`web-ncatlab.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/web-ncatlab.json) |
| Stacks | Ordered-field related algebra, no exact implication established | [`web-stacks.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/web-stacks.json) |
| MathOverflow | Roth proof/effectivity discussion, no exact helper identified | [`web-mathoverflow.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/web-mathoverflow.json) |
| arXiv recent five-year window | Actual after:2021-10-29 before:2026-10-30 query; returned unrelated formalization/additive-Roth papers | [`web-arxiv.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/web-arxiv.json) |
| Optional ask_chatgpt_math | Justified n/a: unavailable | [`literature-protocol.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/literature-protocol.json) |

Supplementary primary source: [Diophantine Analysis and Approximations](https://web.math.princeton.edu/mathlab/jr02/diophantine.pdf), equations17.6,17.9 at PDF page150 and Lemma18.2.3 at page157, contain the positive small-δ context and logarithmic threshold. PDF `find` for “immediate” matched unrelated passages and is not used as an exact quotation. [`web-primary.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/web-primary.json), [`web-primary-detail.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/web-primary-detail.json). No search miss is treated as proof of absence. Receipts retain exact requests, response hash/bytes/status, clean returned locators and original concise summaries only; no article/search-result bodies are archived.

## Phase4a–4b — parameters and verified generality

| Parameter/hypothesis | Mathematical role; weakening assessment |
|---|---|
| `K : Type*` | Arbitrary universe already; no concrete real/log dependence |
| `Semifield K` | Commutative multiplication/division and cancellation; a semiring alone lacks the displayed division conclusion |
| `LinearOrder K` | Supports the sign-independent square argument and strict order comparisons; no partial-order weakening verified |
| `IsStrictOrderedRing K` | Supplies positive multiplication/order compatibility; not dropped merely because instance projections obscure uses |
| `ExistsAddOfLE K` | Used by pinned `sq_pos_of_ne_zero`; controls demonstrate not synthesizable from the other listed assumptions. No class weakening claimed |
| `δ` | Nonzero follows from positive scale and budget; δ>0 is unnecessary and would narrow the statement |
| `m` | No naturalness/nonnegativity assumption; negative and zero rational examples compiled |
| `L` | Arbitrary budget scalar; no explicit sign premise needs adding |
| `hm : 0<2m+1` | Replace exact arithmetic expression by arbitrary positive `a`; scale positivity matters: zero/negative-scale counterexamples compiled |
| `hδm : δm<1` | Replacing < by ≤ only gives weak conclusion when budget also weak; equality counterexample compiled |
| `h32 : 2m+1≤δ²L` | Equality allowed in original; strict conclusion comes from strict contraction. Dropping budget has a compiled counterexample |

Verified wider restatement (same class assumptions):

```lean
theorem generic {δ m a L : K} (ha : 0 < a) (hδm : δ * m < 1)
    (hbudget : a ≤ δ ^ 2 * L) : m * a / δ < L
```

Original specialization is `generic hm hδm h32`; native `isDefEq` confirms its full type is exactly the original. Also compiled: weak δm≤1 / weak conclusion; weak δm≤1 plus strict budget / strict conclusion; δ nonzero with fewer class hypotheses. These are **new scratch proofs**, not existing mathlib replacements. Generality is strictly wider at the modern arithmetic scale interface; literature itself does not name that interface. [`isolated-executed.lean.txt`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/isolated-executed.lean.txt), [`isolated-receipt.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/isolated-receipt.json), [`controls-executed.lean.txt`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/controls-executed.lean.txt), [`controls-receipt.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/controls-receipt.json).

## Phase4c — all nine modern-idiom rows

| # | Question | Assessment and downstream consequence |
|---|---|---|
|1|Typeclasses/instances|Already uses algebra/order classes; no new predicate/instance needed|
|2|Filters/nets|No limiting process or topology|
|3|Universal property|No object is constructed|
|4|Bundled substructure|No closure predicate or subtype API|
|5|Weaken field-specific hierarchy|Already semifield, no subtraction needed; no stronger weakening verified|
|6|Higher categories|No category-theoretic content|
|7|Concrete index to abstract order|Already arbitrary K; m is not restricted to ℕ|
|8|Concrete-via-abstract|Yes: `2m+1` appears only as a positive scale throughout the proof; independently replacing it by positive a compiles and original becomes one call|
|9|False-generalization guard|The abstraction preserves the same multiplication/cancellation implication and exactly specializes. It does not add δ>0; negative-δ guard compiled. Weak version has weak conclusion, preserving boundary meaning|

Concrete diagnostic and actual downstream comparison: [`concrete-diagnostic.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/concrete-diagnostic.json), [`comparison-executed.lean.txt`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/comparison-executed.lean.txt), [`comparison-receipt.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/comparison-receipt.json). The new weak generic law shortens a full related theta module and retains its main theorem's original signature. This is a concrete API benefit, not a claim that a scratch theorem is already in mathlib or that the original has a caller.

## Phase4.5 — infrastructure risk6

All six infrastructure rows are justified n/a for this theorem: typeclass diamond, reducibility leak, noncanonical unfolding, instance priority collision, universe-polymorphism infrastructure, coercion ambiguity. The theorem introduces no definition, instance, coercion, or definitional equality. The scratch generic result is also a theorem, with universe-polymorphic K. No risk exemption is used to bypass a definition audit.

## Phase4.6 — proof strategy5

| # | Check | Result |
|---|---|---|
|1|ε-δ versus filters|No topology|
|2|Element algebra versus subobject inclusions|Scalar inequality is the mathematical content; no ideal/submodule reformulation helps|
|3|Sequences versus nets|No asymptotic analysis|
|4|Construction versus universal property|No construction|
|5|Missing helper mathlib should have|Possible positive-scale budget-transfer family; not established sufficiently canonical for unconditional YES|

The positive-square strategy is MATHLIB-IDIOMATIC and handles δ<0 uniformly. A local refactor could unify strict and weak transfer by a generic scale, but no shortness/cost argument decides upstream inclusion.

## Phase5 — fifteen formal search cells

Current form searches the exact arithmetic implication; standard form searches positive-scale quadratic-budget transfer; abstract form searches positive-square cancellation and contraction. All five methods executed on each form:

| Form | Finder | Loogle | LeanSearch | pinned rg | local search |
|---|---|---|---|---|---|
|current|[`search-current-leanfinder.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/search-current-leanfinder.json)|[`search-current-loogle.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/search-current-loogle.json)|[`search-current-leansearch.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/search-current-leansearch.json)|[`search-current-rg.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/search-current-rg.json)|[`search-current-local_search.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/search-current-local_search.json)|
|standard|[`search-standard-leanfinder.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/search-standard-leanfinder.json)|[`search-standard-loogle.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/search-standard-loogle.json)|[`search-standard-leansearch.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/search-standard-leansearch.json)|[`search-standard-rg.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/search-standard-rg.json)|[`search-standard-local_search.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/search-standard-local_search.json)|
|abstract|[`search-abstract-leanfinder.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/search-abstract-leanfinder.json)|[`search-abstract-loogle.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/search-abstract-loogle.json)|[`search-abstract-leansearch.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/search-abstract-leansearch.json)|[`search-abstract-rg.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/search-abstract-rg.json)|[`search-abstract-local_search.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/search-abstract-local_search.json)|

No exact full implication identified. Finder/LeanSearch returned many unrelated items; Loogle identified genuine building blocks `mul_lt_of_lt_one_left` and `mul_lt_mul_iff_of_pos_right`. Local search returned `index:error`, so an empty/partial list does not establish absence. External indices can differ from the pin. Full-name pinned grep is untruncated and returns no hit; a mathlib-only original-signature probe confirms `exact?` does not close it and then proves the statement normally. [`formal-search-matrix.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/formal-search-matrix.json), [`full-name-search.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/full-name-search.json), [`controls-receipt.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/controls-receipt.json).

Pinned signatures compiled: `mul_lt_of_lt_one_left` needs positive multiplier and factor<1; `mul_lt_mul_iff_of_pos_right` reflects inequality after positive multiplication; `sq_pos_of_ne_zero` needs the ordered-semiring and `ExistsAddOfLE` assumptions. Pinned sources archived and hashed in [`mathlib-inputs.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/mathlib-inputs.json). These are existing building blocks; `Budget253.generic`/`weak` are new proofs.

## Phase5.5 — statement shape3

1. Normal form: compare divided inequality with the cleared square inequality `(δ*m)*a < L*δ²`; the latter is an intermediate normalization, not an independent equivalence API. No existing canonical named budget-transfer form found. Ordinary scalar inequality syntax is appropriate; no RHS-equivalence convention applies.
2. Syntactic generality: positive `a` is preferable to hard-coded `2m+1` upstream. Weak and strict-budget variants were actually tested. An implication with supplied sign and budget hypotheses is easier than bundling them in a custom predicate.
3. Superfluous arguments: no unused scalar or class drop verified for the full target. δ≠0 is derived, so adding it or δ>0 is redundant/narrowing. Literal constants2,1 are representation-specific and can be replaced together by positive a. The unrelated δ-nonzero sublemma omits two unused section classes; its initial warning receipt is retained as rejected evidence and clean correction compiled.

Overall RESTATE-BEFORE-SHIP if accepted upstream: generic positive scale, with a deliberate weak/strict API choice.

## Phase6.0 — full callers, inline and scope audit

Fresh `rg --no-ignore` and `git grep` scoped to tracked production inventory each find only the declaration. Callers table: **none**; internal uses excluding declaring file0, external-to-file files0, actual proof uses0. Full actual caller inlining is justified n/a, not silently replaced with a toy. Exact293 canonical names were generated directly from tracked order (including private modules), independently checked before native execution, and audited at runtime: requested293, unique293, present293, values293, zero direct type/value consumers. [`source-search.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/source-search.json), [`tracked-source-search.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/tracked-source-search.json), [`canonical-consumers.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/canonical-consumers.json), [`callers.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/callers.json), [`scope-audit.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/scope-audit.json).

The nearby private `theta_lt_eta_of_sq_log_bound_aux` repeats the same square-clearing strategy with δm≤1 and conclusion `m(2m+1)/δ≤log q₁`. This is **not the same strict statement**, and cannot call the strict theorem on its equality boundary. Full module comparison substitutes the new weak scratch lemma into exactly that hq derivation and compiles all remaining bodies. `Roth.main_lemma` and comparison `main_lemma` signatures are definitionally identical. This supports local unification if the API is retained, without inventing an original caller. [`inline-search.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/inline-search.json), [`inline-audit.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/inline-audit.json), [`comparison-receipt.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/comparison-receipt.json).

The no-consumer claim is lexical and direct-kernel scope only. It does not establish external, global simp, or transitive deadness. The target has no simp attribute.

## Phase6 — actual composition attempts

**NOT-COMPOSABLE** under the ≤3 existing-call criterion established here:

- Direct `mul_lt_of_lt_one_left hm hδm` proves the cleared contraction inequality, not the divided target; compiled negative application probe rejects it.
- Direct `mul_lt_mul_iff_of_pos_right hm` does not normalize the needed δ-square factor or discharge δ nonzero; compiled negative application probe rejects it.
- The complete isolated proof needs derived nonzeroness, square positivity, positive-square order reflection, field normalization, contraction, and transitivity with the commuted budget. This is a new ordered implication proof, not a ≤3-call composition; `field_simp` does not itself prove the order implication.
- Original recovery is one call to the **new scratch generic lemma**, which is not a mathlib building block. It does not support a NO-composable verdict.

A search miss or failed `exact?` is not an absolute theorem of API absence; the conclusion is bounded to the tested routes and pin. No general search retries or resource raises were used.

## Phase7 — verdict and concrete future questions

**BORDERLINE-needs-human**. The arithmetic is reusable in principle and generic a improves its shape. Yet the primary literature presents this as routine Roth parameter arithmetic; current audited use is zero, and the one nearby application requires a weak partner. Evidence supports a taste/API decision, not unconditional upstream interest and not an existing-mathlib replacement. No verdict is inherited from a parent, and no implementation cost determines it.

1. Should mathlib expose a named positive-scale quadratic-budget transfer lemma in Mathlib/Algebra/Order/Field/Basic.lean, beyond its existing multiplication and cancellation API?
2. If it does, should the weak budget-transfer law and the two strict variants form one small API?
3. Locally, should the unused strict specialization be removed, or retained as a documented arithmetic fact alongside a weak generic helper used by the theta proof?


These questions are follow-up design choices; the assessment is complete with `unresolved: []`. No user approval is required to finish this read-only package. A provisional upstream home, if maintainers want the family, is `Mathlib/Algebra/Order/Field/Basic.lean`; no PR/reviewer/grouping claim is made for a BORDERLINE result.

Locally, flag the strict specialization as an unused API/removal candidate, not a proven globally dead declaration. If a stable public arithmetic lemma is wanted, generalize it and introduce the weak partner used by theta. No production change was made.

## Phase8 — verification and portable package

Accepted sources: full original module replay/audit, stable18 mathlib-only generic/boundary checks, mathlib-only compiled absence/application controls, and full related nonconsumer comparison. All accepted diagnostics are complete, no errors/warnings, standard axioms only. The initial isolated attempt compiled with an unused-section-variable warning and is retained separately as rejected, never counted clean. Full original bodies and all original execution requests/raw receipts/timings are retained. [`verification.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/verification.json), [`assessment.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/assessment.json), [`validate.py`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/validate.py), [`copy-manifest.json`](../evidence/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul/copy-manifest.json).

Portable validation checks the **current** copy manifest, all artifact hashes/bytes, fresh17/pinned sources, exact canonical293 order and runtime counts, clean native receipts and exact request/source equality, all15formal cells, all literature channels, required overview keys, links and secret guard. Historical worker manifest never substitutes for current integrity. Root acceptance remains pending.
