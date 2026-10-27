# `Roth.sum_natDegree_update_lt` — full mathlibable assessment

Verdict: **BORDERLINE-needs-human**. The leading-term cancellation is standard, and mathlib already has both the degree-cancellation law and the finite-sum comparison machinery. The current statement bundles those with global linear independence and a particular `Fin l` family. Verified local hypotheses and arbitrary finite indexing suffice. The unresolved design choice is whether upstream should expose a normalized two-polynomial cancellation corollary, a finite-update wrapper, or only the existing `cancelLeads` API. This is a completed read-only assessment; these are future API decisions, not incomplete verification.

## Phase 0 — Doctor

The baseline `lake build` succeeded (2467 jobs), as recorded in [baseline-build.txt](../evidence/Roth.sum_natDegree_update_lt/baseline-build.txt). All 17 source/pin SHA256 values were freshly matched against the shared manifest; [inputs.json](../evidence/Roth.sum_natDegree_update_lt/inputs.json) captures current hashes and byte counts. Branch: `ramin-cleanup`. Target resolves at `Roth/Wronskian.lean:182`; it is a public theorem, with no sorry. The entire [declaring module](../evidence/Roth.sum_natDegree_update_lt/Wronskian.lean.txt) and its sole actual caller were read. The module proves a finite polynomial Wronskian criterion by cancelling equal leading degrees and then computing a Vandermonde coefficient.

## Phase 1 — Comprehend

For a linearly independent finite family of polynomials over a field, take two distinct members with equal natural degree. Subtract from the second the first multiplied by the ratio of their leading coefficients. The new family has strictly smaller sum of natural degrees. Linear independence guarantees that both polynomials and their difference are nonzero; equal leading terms cancel, and all other family entries stay fixed.

Full native type (universe names are immaterial):

```lean
∀ {K : Type u} [Field K] {l : ℕ} {φ : Fin l → K[X]},
  LinearIndependent K φ → ∀ {ν ν' : Fin l}, ν ≠ ν' →
    (φ ν).natDegree = (φ ν').natDegree →
      ∑ ρ, (Function.update φ ν'
        (φ ν' - C ((φ ν').leadingCoeff / (φ ν).leadingCoeff) * φ ν) ρ).natDegree <
        ∑ ρ, (φ ρ).natDegree
```

Parameters: universe-polymorphic coefficient field `K`; natural family size `l`; family `φ`; indices `ν,ν'`. Hypotheses: field structure, global linear independence, distinct indices, equal natural degrees. The conclusion is a strict inequality in `ℕ`. Project dependency in the source proof: `Roth.linearIndependent_update_sub_smul`, only to establish the updated difference is nonzero. This is not an extra parent-interface constraint on the target: the target contains no Wronskian definition and can be restated independently. The proof uses `degree_C_mul`, `degree_eq_natDegree`, `degree_sub_lt_left`, `natDegree_lt_natDegree`, and `Finset.sum_lt_sum` with explicit leading-coefficient normalization and pointwise update reasoning.

## Phase 2 — Preliminary checks

**SMALL**: an induction-measure helper, not a named main theorem or new structure. It is mentioned in implementation notes, not the main-results list. One-line definition check: **n/a, theorem**. There is no definition to remove for defeq, diamond, or stable-name reasons; proof length is not a verdict factor.

## Phase 3 — Exhaustive literature

Exact requests, returned response SHA256/bytes/status, and returned URL locators are in the `web-*.json` files, consolidated in [web-evidence.json](../evidence/Roth.sum_natDegree_update_lt/web-evidence.json). Only metadata and original concise summaries are retained, not article/search-result bodies. Returned URL query strings were omitted proactively; no credential values were retained. Every required named channel was attempted; the protocol's informal nine-channel label does not justify inventing a synthesis channel.

| Channel | Exact query or request | Outcome and relevance |
|---|---|---|
| General web, specific | `Wronskian linearly independent polynomials equal degrees eliminate leading coefficients` | Standard Wronskian reduction literature, including Bostan–Dumas and Hermoso–Alcázar. |
| General web, general | `polynomial basis distinct degrees Gaussian elimination leading coefficients` | Gaussian elimination on coefficient vectors; the finite-family presentation is bookkeeping. |
| General web, alias | `polynomial leading term cancellation degree reduction field` | Leading-term cancellation and polynomial reduction; equality of leading degrees gives a constant quotient. |
| Optional mathematical second opinion | `ask_chatgpt_math` | n/a: unavailable in this session; no query falsely claimed. |
| Local references | `rg -n 'Wronsk\|leading\|basis' .mathlib-quality/references/clean.tex` | §Wronskians, lines 174–178: eliminate equal leading degrees; degree-filtration quotients have dimension at most one. [Excerpt](../evidence/Roth.sum_natDegree_update_lt/clean-excerpt.tex.txt). |
| nLab | `site:ncatlab.org/nlab Wronskian polynomial linear independence`; open `https://ncatlab.org/nlab/show/Wronskian` | Search attempted; direct access failed with unsupported XHTML content type. No inaccessible content used as evidence. |
| nCatLab | `site:ncatlab.org Wronskian degree cancellation` | No dedicated finite-update result located; this is algebraic elimination, not a categorical construction. |
| Stacks | `site:stacks.math.columbia.edu polynomial degree leading coefficient division` | Polynomial algebra background, no direct family-sum law located. Exploratory tag `0009` was irrelevant (set theory), explicitly excluded. |
| MathOverflow | `site:mathoverflow.net Wronskian polynomial linearly independent degree` | Broader Wronskian/independence discussions; no sharper local hypothesis needed than cancellation. |
| arXiv, recent five years | `site:arxiv.org Wronskian polynomial linear independence 2022 2023 2024 2025 2026` | Broad noisy results; followed by precise title query below, not treated as absence. |
| arXiv follow-up | `"Nonzero Constant Wronskians" polynomials Laurent arxiv`; `site:arxiv.org Wronskian polynomials "2024" "2025" degree` | Hermoso–Alcázar, arXiv:2410.18867v1 (24 October 2024), Proposition 1, proof equations (3), directly performs the same leading-coefficient quotient subtraction. |
| Primary sources | Open arXiv HTML 2410.18867v1 and 1301.6598v1 | First source §2, Proposition 1, lines 74–88; second source Lemma 2, lines 80–96, explains Gaussian column elimination for distinct orders of power series. The power-series order increases rather than polynomial degree decreasing. |

Primary locators: [Hermoso–Alcázar, Proposition 1](https://arxiv.org/html/2410.18867v1#S2), [Bostan–Dumas, Lemma 2](https://arxiv.org/html/1301.6598v1). An exploratory guessed arXiv identifier `2410.22528` returned an optics paper and was excluded; exact request retained honestly. Recent means the actual 2024 submission date, not a search-engine crawl/publication-age approximation.

Concept: leading-term cancellation / Gaussian elimination respecting the polynomial degree filtration. Sources agree on this operation; they differ on whether they package it as a basis-with-distinct-degrees theorem, a two-polynomial step, or a valuation/order argument for power series. The most general standard cancellation mechanism is subtraction of equal leading terms. Global independence is needed to retain a basis, not to prove degree descent for arbitrary positive-degree inputs. Characteristic zero is needed later for the Wronskian criterion, and is absent here correctly. The source's sum-of-natural-degrees conclusion is a termination measure, rather than a separately named mathematical theorem.

## Phase 4a–4b — Parameters and verified generality

| Parameter/hypothesis | Role, weakening attempt and evidence |
|---|---|
| `K : Type*` | Already universe polymorphic; no restriction to rationals or reals. |
| `[Field K]` | Division is used in the displayed expression, so a bare semiring/ring is not a literal drop. Cross-multiplied cancellation over a commutative ring is already in `Polynomial.cancelLeads`. The mechanical `Field` → `DivisionRing` replacement compiled for all four local/family variants, without adding hypotheses. This is a genuine further weakening; the `CommRing` `cancelLeads` theorem does not directly subsume noncommutative division rings. |
| `l : ℕ`, `Fin l` | Replaced by arbitrary `ι` with `[Fintype ι] [DecidableEq ι]`; compiled. This removes an artificial numeric-index restriction; finite summation is essential. |
| `φ` | Arbitrary family already; all entries besides the two selected members are irrelevant to cancellation. |
| global `LinearIndependent K φ` | Compiled replacement: nonzero selected `p,q`, equal degrees, nonzero normalized difference. Stronger useful compiled alternative: equal degrees and **positive common natural degree alone**. The latter allows dependent families and a zero result. |
| `ν ≠ ν'` | Dropped in compiled local/family restatements. It is useful only to derive nonzero difference from independence in the original proof. In the positive-degree form even the same member may cancel to zero and strictly reduce its degree. |
| equal degree `hdeg` | Retained for the same constant-quotient operation. General polynomial division allows shifted degrees, represented by `cancelLeads`; that is a different formula requiring its bridge. |
| implicit nonzero control | Never drop blindly: natural degree of zero is zero. Constant inputs can cancel to zero without a strict decrease. `degree : WithBot ℕ` has a clean strict law including zero, but summing it changes the induction measure and is not a free drop-in replacement. |

Verdict: **STRICTLY NARROWER THAN STANDARD**, with native-verified local-hypothesis and finite-index replacements. The strongest compiled positive-degree restatement is:

```lean
theorem family {K ι : Type*} [DivisionRing K] [Fintype ι] [DecidableEq ι]
    {φ : ι → K[X]} {i j : ι}
    (hd : (φ i).natDegree = (φ j).natDegree) (hpos : 0 < (φ j).natDegree) :
    ∑ k, (Function.update φ j
      (φ j - C ((φ j).leadingCoeff / (φ i).leadingCoeff) * φ i) k).natDegree <
      ∑ k, (φ k).natDegree
```

The local nonzero-difference version is also useful, because its premise is immediately available from independence. These are **new proven helpers**, not pre-existing mathlib hits. Both imply the same family measure descent; the caller must supply local nonzero/positivity evidence, so a signature change is not silently substituted into production. Restatement cost is moderate and has no role in the verdict.

## Phase 4c — Modern idiom, all nine rows

| # | Question | Answer, reformulation and downstream consequence |
|---|---|---|
| 1 | Typeclasses instead of bundled hypotheses? | No additional class. `Field`/finite-index instances already use the hierarchy; local polynomial hypotheses should stay ordinary premises. |
| 2 | Sequences/metrics to filters? | No topology or convergence. |
| 3 | Construction to universal property? | No constructed universal object; cancellation is an explicit algebraic operation. |
| 4 | Closure predicates to bundled substructures? | No. A span/filtration theorem would describe existence of a distinct-degree basis, a separate larger theorem. |
| 5 | Field-specific result to modules/rings? | Yes for cross-multiplied cancellation: existing `cancelLeads` works over `CommRing`, and its commuting-leading-coefficient variant over `Ring`. The literal quotient expression still requires division. This lets polynomial reduction work over integral coefficient rings without invented division. |
| 6 | Higher-categorical version? | No categorical input or universal construction. |
| 7 | Concrete index to abstract index? | Yes: compiled arbitrary finite `ι`. Enables directly indexed bases and finite sets without transport through `Fin (card ι)`. Natural-degree values remain natural because the actual caller uses strong induction. |
| 8 | Concrete-via-abstract diagnostic? | The coefficient-cancellation block is genuinely polynomial-specific. After the local `hlt` inequality, only generic finite sums and `Function.update` remain (five source proof lines); this identifies the split into local polynomial descent and ordered finite-update comparison. The `Fin l` operations supply no essential arithmetic. This is not an assertion that the entire polynomial theorem follows by generic extensionality. |
| 9 | False-generalisation guard? | No semantic mismatch for the compiled division-ring/finite-index/local-premise proposals. Replacing degree by power-series order reverses the inequality and changes the well-founded argument; rejected as a literal generalization. Replacing the field by a ring without replacing division is also rejected. Constant cancellation is explicitly guarded. |

Modern-idiom verdict: **restate around local polynomial cancellation plus generic finite sums**. Concrete consequences are removing global independence from reduction applications, allowing dependent positive-degree families, and using arbitrary finite bases. There is no reason to build a category or new degree structure.

## Phase 4.5 — Infrastructure risk

**n/a: theorem**, not a definition/class/instance. All six definition risks are inapplicable: no typeclass diamond, reducibility body, new unfolding normal form, instance priority, universe-bearing construction, or coercion is introduced. Existing polynomial/function instances are used, not replaced.

## Phase 4.6 — Proof strategy

| # | Diagnostic | Result |
|---|---|---|
| 1 | Topology ε–δ vs filters | n/a: finite algebra. |
| 2 | Elements vs submodule inclusions | Direct coefficients are appropriate for local cancellation; global independence is excessive for the measure step. A filtration/basis existence theorem would be a separate reusable result. |
| 3 | Sequences vs nets | n/a: no analytic limits. |
| 4 | Construction vs universal property | n/a: no universal object. |
| 5 | Missing helper API | Candidate gap is a normalized equal-degree quotient-cancellation corollary and/or its relation to `cancelLeads`; the full finite-family wrapper's value is less clear. Generic `sum_lt_sum` already exists. |

Verdict **REFACTOR-RECOMMENDED**: separate the polynomial inequality from the pointwise update/sum argument, and reuse existing cancellation normal forms where appropriate. This is cleaner independently of cost; no new axiom or limit raise is justified.

## Phase 5 — Five actual formal-search methods, three forms

Raw full tool receipts are in [formal-search.json](../evidence/Roth.sum_natDegree_update_lt/formal-search.json); exact untruncated CLI commands/results in [source-search.json](../evidence/Roth.sum_natDegree_update_lt/source-search.json). Each external method ran independently on (A) the current finite-family form, (B) standard leading-term cancellation, and (C) abstract finite update/sum. External index results are candidates, not proof of compatibility with the pinned revision.

| Method | A current form | B literature form | C abstract form |
|---|---|---|---|
| Lean-Finder | Full normalized update/sum description | Equal leading coefficients and degree subtraction | Strict finite-sum update comparison; `Finset.sum_lt_sum` hit |
| Loogle | `Polynomial.natDegree, Function.update` | `Polynomial.degree (?p - ?q) < Polynomial.degree ?p` | `Finset.sum, Function.update`; sum-update API hits |
| LeanSearch | Independent equal-degree family cancellation | Equal degrees and equal leading coefficients | A finite sum strictly decreases if one summand is smaller |
| `rg` | Full target name and polynomial/update patterns throughout pinned mathlib | `cancelLeads`, `degree_sub_lt_left` | `sum_update`, `theorem sum_lt_sum` |
| `lean_local_search` | `sum_natDegree_update_lt` | `degree_sub_lt_left` | `sum_update` |

Local index reports `unavailable`; it still returned source hits, including an overview-evidence pollution hit for `sum_update_add`, which is excluded. This limitation is not evidence of absence. Finder/LeanSearch report historical `Polynomial.degree_sub_lt` in `Degree.Definitions`; pinned mathlib uses `degree_sub_lt_left` at `Degree/Defs.lean:543`, with deprecated alias at line 560. Actual pinned source/signatures and compiled experiments control the assessment.

Positive existing API:

* `Polynomial.degree_sub_lt_left`, `Mathlib/Algebra/Polynomial/Degree/Defs.lean:543`: over `Ring`, equal degrees, nonzero left polynomial and equal leading coefficients imply strict `degree` descent.
* `Polynomial.natDegree_lt_natDegree`: converts degree descent when the lower polynomial is nonzero.
* `Polynomial.cancelLeads` and `natDegree_cancelLeads_lt_of_natDegree_le_natDegree`, `Mathlib/Algebra/Polynomial/CancelLeads.lean:41,81`: cross-multiplied leading-term cancellation over `CommRing`, positive upper natural degree, weak degree comparison. Commuting-leading-coefficient variant at line 51 works over `Ring`.
* `Finset.sum_lt_sum`, `Mathlib/Algebra/Order/BigOperators/Group/Finset.lean`: pointwise weak plus one strict inequality.
* `Finset.sum_update_of_mem`, `Mathlib/Algebra/BigOperators/Group/Finset/Piecewise.lean`: update equals replacement summand plus erased sum.

Conclusion: **partial matching general cancellation law and generic summation building blocks**, with normalized representation bridges tested separately. No claim that a failed search proves absence, or that the new local helper is an existing mathlib declaration.

## Phase 5.5 — Statement shape

Normal-form alternatives: (i) `degree` descent after equal leading coefficients; (ii) `cancelLeads` natural-degree descent; (iii) normalized quotient subtraction; (iv) summed family update. Mathlib already has (i) and (ii). The source chooses (iv) for its induction measure. An equivalence normal form on a RHS is inapplicable: the conclusion is an inequality, not an equivalence between definitions.

Syntactic experiments: arbitrary finite index/local nonzero difference and arbitrary finite index/positive degree both compile. The second has fewer premises; the first aligns naturally with the existing independence caller. There is no upstream need to assume independence of unrelated family entries. Superfluous-argument audit is the complete Phase 4 table: field quotient is used, `Fin l` is replaceable, global independence and index distinctness are replaceable by local conditions, degree equality remains, and the zero/constant boundary cannot be ignored. Shape verdict: **RESTATE-BEFORE-SHIP**, with a local cancellation core preferred over a family-specific wrapper.

## Phase 6.0 — All explicit callers and inline audit

| Caller | Exact use | Refactor implication |
|---|---|---|
| `Roth/Wronskian.lean:213`, `wronskian_ne_zero_of_linearIndependent` | `ih _ (hN ▸ sum_natDegree_update_lt h hne hdeg)` | Supply a local cancellation inequality, then generic finite-sum decrease, retaining `hN` transport for the strong-induction bound. Independence is still needed separately for the recursive family's independence. |

Actual executable references: **one**, same-file; external-to-file references: **zero**; internal count excluding the declaring file per command convention: **zero**. The module docstring has one explanatory reference at line 39, not a second call. `source-search.json` records qualified/bare and inline patterns. No independent inline duplicate found. Source callers are not an opaque kernel/simp dependency closure; the theorem is not tagged simp. The actual call makes this live code, so zero external-file references does not imply junk.

## Phase 6 — Actual composition experiments

Attempt 1: the source's direct `degree_sub_lt_left` → `natDegree_lt_natDegree` → `Finset.sum_lt_sum` route. Merely listing three names hides construction of equal scaled degrees, leading-coefficient division cancellation, nonzero difference, and unchanged-entry inequalities. The compiled original replay confirms a proof, not a three-call existing-API composition. Its project independence-update helper is not a mathlib building block.

Attempt 2 (compiled successfully, including `DivisionRing`): compile local polynomial cancellation and arbitrary finite-family transport. These succeed under weaker premises, but each is a newly proved helper; they cannot count as existing mathlib for a NO verdict.

Attempt 3 (compiled successfully over a field): compare the normalized operation to `cancelLeads`. The representation change uses leading-coefficient normalization and degree equality rather than definitional equality. The bridge is `q - C (q.leadingCoeff / p.leadingCoeff) * p = C p.leadingCoeff⁻¹ * p.cancelLeads q`, proved by an explicit `simp only` algebra chain with `p ≠ 0` and equal natural degrees. Applying `natDegree_C_mul_le` and the existing `cancelLeads` bound yields positive-degree local descent. The `simp only` closes precisely this polynomial equality bridge; it does not close the positive-degree inequality or the original finite-family statement. Consequently the bridge alone does not trigger Phase 6b's mandatory borderline case for the original theorem, and is not a definitional equality or ≤3-call proof of it. Its exact executed bridge and native outcome are archived with [verification.json](../evidence/Roth.sum_natDegree_update_lt/verification.json). Even a successful normalized bridge does not erase the caller's nonzero/positivity derivation and the family-sum layer.

Attempt 4: `exact?` on the whole original family goal failed to close, without timeout. Its separate [rejected receipt](../evidence/Roth.sum_natDegree_update_lt/composition-rejected.json) establishes only that this search attempt failed. Compiled guards verify constant cancellation does not strictly lower natural degree, and unequal-degree inputs can retain their degree after this constant subtraction. The [caller replay](../evidence/Roth.sum_natDegree_update_lt/caller-executed.lean.txt) recovers the original exact statement noncircularly from the local inequality, derives positive degree, applies the generalized family bound, then rebuilds the complete strong-induction caller without using the original target in that rebuilt proof. The persistent document also contains older accepted replays; their references are historical context, not dependencies of `DegreeUpdateRecover.recovered` or `.caller_rebuilt`.

Conclusion: **NOT-COMPOSABLE as a demonstrated ≤3 existing-call term for the full original statement**. This does not assert mathematical novelty: the central cancellation law is already formalized. No `simp [defs]` experiment closes the original goal here: only the normalized polynomial equality bridge closes by explicit simplification. The BORDERLINE verdict therefore rests independently on the competing API boundaries and existing-law overlap, not an automatic Phase 6b classification of the full theorem. No cost-based downgrade is used.

## Phase 7 — Verdict and next action

**BORDERLINE-needs-human.** The standard mathematics and reusable cancellation API exist; the exact package is one project's induction-measure helper. Verified weakenings make `YES-add-as-is` inappropriate. There is also no verified ≤3-call existing-mathlib proof of the entire statement supporting `NO-composable`, and `degree_sub_lt_left` alone is not the entire finite-family law. No verdict is inherited from the separately assessed independence-update theorem. The explicit parent-definition re-aim rule is inapplicable: this theorem's statement does not mention that parent definition, and the former dependency is just a proof lemma.

Future upstream API questions (no user interruption required for this assessment):

1. Should `CancelLeads.lean` expose a normalized equal-degree quotient-cancellation corollary, or should clients normalize through `cancelLeads` directly?
2. If such a corollary is wanted, should its natural-degree premise be positive common degree, with a nonzero-difference variant for linear-independence clients?
3. Is a generic finite-update strict-sum lemma useful in its own right, leaving the polynomial-family wrapper downstream?

Alternative local destination: keep the measure helper in `Roth/Wronskian.lean`, preferably private/local to the strong-induction proof or split into local cancellation and sum transport. It is useful there and is not junk. At the sole caller line 213, a future refactor should derive selected-member nonzeroness and nonzero updated difference from independence (using existing generic shear/independence API), apply the local inequality, and lift it with `Finset.sum_lt_sum`; preserve the recursive independence argument. No production edit or PR is made by this assessment. The noncommutative division-ring variant is a further design consideration: cross-multiplied cancellation requires commuting leading coefficients in the existing ring theorem, while right-quotient cancellation does not. If upstream accepts a normalized cancellation API, rerun `/generalise Roth.sum_natDegree_update_lt` and `/cleanup Roth/Wronskian.lean sum_natDegree_update_lt` with that specific target.

## Phase 8 — Consolidated report and verification handoff

This report consolidates all required phases. [assessment.json](../evidence/Roth.sum_natDegree_update_lt/assessment.json) records phase status and the completed verdict; [verification.json](../evidence/Roth.sum_natDegree_update_lt/verification.json) names exact accepted sources and complete raw native receipts. Only standard axioms are permitted; no sorry, new axiom, unsafe/native proof shortcut, limit raise, timeout, or partial response is accepted. Rejected attempts remain separate. [validate.py](../evidence/Roth.sum_natDegree_update_lt/validate.py) validates both scratch and integrated layout, current manifest hashes/bytes, source/pin freshness, native success/axioms, and report links, then runs the shared credential-safe URL guard. Root acceptance remains pending independent review. Next action: retain the local helper while resolving the three concrete upstream API questions in a future contribution design; continue the project overview.
