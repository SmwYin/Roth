# Roth.normOne_zero — full mathlibable assessment

Verdict: **NO-mathlib-has-it**. `Finsupp.sum_zero_index` already proves the more general statement: a support sum over the zero finitely supported function is zero for **any** indexed size function. No zero-preservation assumption is needed. The original polynomial norm expression specializes this existing law by definitional reduction; a fresh native term checks this directly. This is an independent finding, not blanket inheritance from `Roth.normOne` (whose accepted verdict was NO-composable).

## Phase 0 — baseline and identity

Declaration80/293, public `[simp]` theorem at `Roth/CoeffNorm.lean:66–67`. The entire declaring module was read: it develops coefficient length, Hasse derivative/determinant estimates, diagonal substitution and evaluation bounds for Roth's theorem. The complete explicit caller `normOne_sum_le` is in that module. The baseline build succeeded (2467 jobs, no reported warnings/errors); all17 production/pin hashes freshly match the shared baseline manifest. No production or pin changes are part of this assessment. Target native print and axioms resolve the actual theorem without placeholders.

Evidence: [baseline](../evidence/Roth.normOne_zero/baseline-build.txt), [fresh inputs](../evidence/Roth.normOne_zero/inputs.json), [hash gate](../evidence/Roth.normOne_zero/input-hash-check.json), [source module](../evidence/Roth.normOne_zero/source-module.lean.txt), [canonical order](../evidence/Roth.normOne_zero/canonical-order.json), [native target](../evidence/Roth.normOne_zero/native-target-success.json).

## Phase 1 — exact content

For any set of variables, the sum of the absolute values of the real casts of the integer coefficients of the zero multivariate polynomial is zero. Its support is empty, so this conclusion depends only on the identity of an empty additive aggregate. It does not use positivity, absolute value, polynomial multiplication or finite variable type.

Full native elaborated type:

```lean
∀ {σ : Type u_1}, Roth.normOne (0 : MvPolynomial σ ℤ) = 0
```

The only parameter is the arbitrary universe-polymorphic type `σ`. There are no explicit hypotheses, additional typeclasses, degree conditions, nonzero assumptions or finiteness assumptions. The parent definition fixes integer coefficients and real-valued coefficient absolute sum. The original proof is `by simp [normOne]`.

## Phase 2 — preliminary checks

**SMALL**: elementary zero law of a project convenience; no new structure, main named theorem or person/place theorem. Literature search remains exhaustive. One-line definition test: **n/a, theorem**. The theorem's one-line tactic proof does not trigger the definition-only exemptions. It is not a glue declaration eligible for literal-rfl inheritance: its recorded source proof uses `simp [normOne]`; the complete independent workflow was run.

## Phase 3 — exhaustive literature

Exact requests, response SHA256/byte counts and concise original summaries are retained; full article/search bodies are not archived. Returned credential-bearing URLs are not retained. `ask_chatgpt_math` is unavailable; that optional channel is recorded n/a, including the unavailable historical-formulation consultation. No missing channel is replaced with an invented channel.

| Channel | Actual query/access | Outcome |
|---|---|---|
| General web, specific | `"zero polynomial" "coefficient" "l1 norm"` | No separately named zero-law source needed; zero coefficients and norm terminology found. |
| General web, general | `"sum over empty set" "additive" monoid zero` | Empty aggregate identity context; a primary mathematical article explicitly uses the convention. |
| General web, alias | `polynomial length sum absolute coefficients zero length` | Primary Evertse–Gyory manuscript and Tubbs chapter identify length as coefficient absolute sum. |
| ChatGPT mathematical MCP | Standard form, generality and historical evolution | n/a: `ask_chatgpt_math` unavailable. |
| Local reference | `clean.tex`, actual `rg` for zero/norm/triangle inequality; lines437–497 read | Section3 proof of Lemma3 uses coefficient ℓ¹ norm for coefficient and determinant estimates. No separate zero lemma asserted. |
| nLab | `site:ncatlab.org/nlab "norm" "zero"`; direct norm page | Indexed empty-word/list and monoid material is adjacent. Direct norm page fails400 unsupported XHTML; no unaccessed page content inferred. |
| nCatLab | `site:ncatlab.org/ncatlab "monoid" "empty"` | Results are nLab pages/files; no distinct categorical coefficient-zero theorem. Finite support sum needs no categorical reformulation. |
| Stacks | `site:stacks.math.columbia.edu "empty sum"`; direct search URL | No exact result; direct search inaccessible. This elementary additive identity is not an algebraic geometry-specific API gap. |
| MathOverflow | `site:mathoverflow.net polynomial length sum absolute coefficients` | Small-coefficient interpolation discussion, adjacent only; not used as primary proof authority. |
| Recent arXiv | `site:arxiv.org polynomial "length" "coefficients" after:2021-10-27 before:2026-10-28` | Actual five-year search, adjacent2024 reduction-theory result, no exact named law. Supplemental2022 Houben–Streng primary PDF checked. |
| Supplemental primary access | Evertse–Gyory2021 manuscript; Houben–Streng2022 abstract/PDF; PDF finds | Concrete standard-form locators below. This is additional access, not an invented mandatory channel. |

Literature evidence: [web0](../evidence/Roth.normOne_zero/web-0.json), [web1](../evidence/Roth.normOne_zero/web-1.json), [web2](../evidence/Roth.normOne_zero/web-2.json), [web3](../evidence/Roth.normOne_zero/web-3.json), [web4](../evidence/Roth.normOne_zero/web-4.json), [web5](../evidence/Roth.normOne_zero/web-5.json), [local excerpt](../evidence/Roth.normOne_zero/local-literature.txt), [local hash](../evidence/Roth.normOne_zero/local-literature-source.json), [local search](../evidence/Roth.normOne_zero/rg-local-literature.json).

[Evertse–Gyory, Effective Results and Methods for Diophantine Equations over Finitely Generated Domains](https://math.unideb.hu/sites/default/files/upload_documents/version-210614_0.pdf), PDFpage86, printedp67, lines2945–2961, defines length for integer multivariate polynomials by coefficient absolute sum. [Houben–Streng, Generalized class polynomials](https://arxiv.org/pdf/2207.08915), §3, PDFpage4 lines252–253, uses coefficient absolute sum for complex univariate polynomials. These sources agree on the coefficient length concept, while coefficient domain and number of variables vary. The zero law follows from that definition; this last sentence is an inference, not a claim that either source names the theorem. Height/sup norm and Mahler measure are distinct notions, even though several share a zero value.

Most general useful standard abstraction: aggregate any indexed size over finite support; for the zero object, support is empty, so additive identity follows. No historical change in this elementary convention is evidenced by this search. No claim of novelty follows from the absence of a separately named theorem.

## Phase 4a — parameters and generality

| Component | Current interface | Weaker/expanded form | Check |
|---|---|---|---|
| Variable type | arbitrary `σ : Type*` | arbitrary support index `ι : Type*` | Already no finite/decidable index assumptions; expanded Finsupp theorem verified. |
| Polynomial coefficient | fixed `ℤ` within `normOne` | any `R` with `Zero R` for Finsupp; `CommSemiring R` for polynomial form | Expanded statements verified; changing parent interface is a representation refactor, not dropping a theorem hypothesis. |
| Output | fixed real numbers | any `AddCommMonoid S` | Verified generic theorem needs additive identity/finite sum only. |
| Size | real absolute value of integer cast | arbitrary `ι → R → S` | Verified with no `size i 0 = 0` assumption. |
| Object | zero multivariate polynomial | zero finitely supported function | Definitional coefficient representation supplies exact specialization. |
| Hypotheses | none | none to drop | No positivity, nonzero, finite variable or degree premise added. |

## Phase 4b — generality verdict

**MAXIMALLY GENERAL at the fixed parent interface**: `σ` is unrestricted and there are no hypotheses to weaken. Expanded representations are genuinely broader and freshly verified; their existing theorem is `Finsupp.sum_zero_index`, not a proposed new helper. The generic polynomial form keeps `CommSemiring R` only because that is the polynomial interface. The arbitrary Finsupp form removes multiplication/order/absolute value entirely. Cost: CHEAP, recorded only for sequencing and never as a verdict reason.

In contrast to support-padding and singleton laws, **zero-preservation of size is unnecessary**: zero support contains no entries. The raw test `sizeZeroUnnecessary` uses constant size1 into ℕ and still proves the support sum zero. This prevents accidentally carrying an unnecessary premise from related lemmas. [Fresh raw source](../evidence/Roth.normOne_zero/native-raw-executed.lean.txt), [receipt](../evidence/Roth.normOne_zero/native-raw-success.json).

## Phase 4c — nine modern-idiom rows

| # | Question | Answer and concrete consequence |
|---|---|---|
| 1 | Typeclass preambles? | No bundled hypotheses to convert. Generic sum already uses `Zero R`/`AddCommMonoid S`. |
| 2 | Filters/topology? | No: finite empty aggregate, no convergence. |
| 3 | Universal-property construction? | No object constructed by this theorem. No universal-property helper needed. |
| 4 | Bundled substructure? | No closure predicates or subobjects; no useful lattice restatement. |
| 5 | Hierarchy weakening? | Yes in expanded representation: remove ring, norm and order down to Zero coefficients/additive monoid output; existing Finsupp law supplies it. |
| 6 | Higher categories? | No categorical result; categorification adds no relevant downstream operation. |
| 7 | Concrete indices? | `σ` already arbitrary, but exponent index can be replaced by arbitrary `ι` once polynomial representation is expanded; applicable to all finite support aggregates. |
| 8 | Concrete-via-abstract diagnostic? | Yes: original body has one occurrence of `normOne`, solely in unfolding `simp [normOne]`; zero occurrences afterward. Empty support is the entire mechanism. Finsupp generic statement checked and exact project specialization checked. |
| 9 | False-generalization guard? | Arbitrary indexed size preserves this support-sum zero identity by exact specialization. Replacing the entire coefficient norm by sup norm/Mahler measure is a different object and is rejected as a replacement of parent `normOne`. Constant size1 test confirms support aggregation is distinct from a sum over a padded nonempty set. |

Modern idiom available: **yes, already in mathlib**. Concrete consequences: the same law works for arbitrary Finsupp coefficients/sizes without establishing a norm instance, a ring, absolute-value zero or ordered codomain; it is also the existing simplifier rule on Finsupp sums. It does not make this local spelling a new upstream contribution.

## Phase 4.5 — infrastructure risk

n/a: theorem introduces no definitions, classes, instances, coercions or reducibility infrastructure. Thus the six definition-risk rows (diamonds, reducibility leak, noncanonical unfolding, priority collision, universe infrastructure, coercion ambiguity) are not applicable. The `[simp]` attribute is an API use concern and is examined in Phase6; it is not a new instance path.

## Phase 4.6 — proof strategy

| # | Strategy question | Answer |
|---|---|---|
| 1 | ε–δ versus filters | No topology. |
| 2 | Element algebra versus subobject inclusions | No element chase; empty-support calculation already direct. |
| 3 | Sequences versus nets | No limits. |
| 4 | Construction versus universal property | No construction. |
| 5 | Helpers mathlib should have but lacks | None: `Finsupp.sum_zero_index` is precisely the generic law; `MvPolynomial.support_zero` plus `Finset.sum_empty` is another existing route. |

Strategy: **MATHLIB-IDIOMATIC** original `simp [normOne]`, with a more explicit existing-law term available for dependency/refactor audit. No missing helper or new proof strategy gap. Phase6b's trivial-simp-only caution is respected: the verdict rests on an exact checked existing theorem application, not merely on a tactic closing the goal.

## Phase 5 — five methods × three forms

All five actual methods ran on the current polynomial-norm form, literature length/zero-polynomial form and abstract Finsupp form. Raw formal responses preserve the exact calls and any failures. External indexes need not match the pinned revision; candidates are checked against pinned source/native signatures.

| Method | Current | Literature-standard | Abstract |
|---|---|---|---|
| Lean-Finder | coefficient-zero and norm-zero analogues | Gauss/content/Mahler zero analogues (different sizes) | exact `Finsupp.sum_zero_index` |
| Loogle | initial unquoted coeff identifier rejected; retry rate-limited; second quoted retry returns coefficient-zero family | exact `Polynomial.sum_zero_index` | exact `Finsupp.sum_zero_index` |
| LeanSearch | coefficient-zero and generic norm-zero analogues | `Polynomial.sum_zero_index` | exact Finsupp zero-sum family |
| `rg` pinned source | no project spelling in mathlib | polynomial zero-index, sup/Gauss analogues | generated additive law of `prod_zero_index`, Basic86–88 |
| `lean_local_search` | finds project target (not mathlib replacement) | sum-zero family | polynomial/skew counterparts; index marked unavailable, so not evidence of absence |

Receipts: [all formal calls](../evidence/Roth.normOne_zero/formal-search.json), [rg current](../evidence/Roth.normOne_zero/rg-current.json), [rg standard](../evidence/Roth.normOne_zero/rg-literature.json), [rg abstract](../evidence/Roth.normOne_zero/rg-abstract.json), [full-name audit](../evidence/Roth.normOne_zero/rg-full-name.json). The two failed Loogle attempts are retained, then a successful retry supplies the current-form result; failures are not treated as absence.

Pinned positive law: **`Finsupp.sum_zero_index`**, `Mathlib/Algebra/BigOperators/Finsupp/Basic.lean:86–88`, generated by `@[to_additive (attr := simp)]` from `prod_zero_index`. Its full native type is:

```lean
∀ {α : Type u_1} {M : Type u_8} {N : Type u_10}
  [Zero M] [AddCommMonoid N] {h : α → M → N},
  (0 : α →₀ M).sum h = 0
```

The source body is `rfl`. `Polynomial.sum_zero_index` is a univariate analogous API; `MvPolynomial.support_zero` and `Finset.sum_empty` provide a two-step alternative; generic `norm_zero` requires the correct norm structure and cannot simply be used for arbitrary parent `normOne`. The existing target does not require any such instance.

Source: [Finsupp](../evidence/Roth.normOne_zero/mathlib-finsupp-basic.lean.txt), [MvPolynomial](../evidence/Roth.normOne_zero/mathlib-mvpolynomial-basic.lean.txt), [Polynomial](../evidence/Roth.normOne_zero/mathlib-polynomial-basic.lean.txt), [norm comparison](../evidence/Roth.normOne_zero/mathlib-norm.lean.txt), [source hashes](../evidence/Roth.normOne_zero/mathlib-inputs.json).

Conclusion: **found in mathlib as Finsupp.sum_zero_index; more general form**.

## Phase 5.5 — statement shape

Normal forms: (1) `normOne (0 : MvPolynomial σ ℤ) = 0`; (2) zero coefficient Finsupp sum equals0; (3) finite sum over empty support equals0. Mathlib's support-sum normal form is existing Finsupp law, with0 on RHS. Local norm convenience also respects RHS simplifier convention.

Syntactic alternatives actually attempted: direct old-interface term; fresh expanded original `simp` proof; arbitrary indexed-size Finsupp theorem; arbitrary-size polynomial theorem. The direct term is easiest for the single explicit witness consumer; keeping the local theorem preserves the stable simp spelling until an authorized project refactor. Superfluous-argument audit: sole `σ` is required to specify polynomial type; no hypotheses/typeclass arguments to drop. Expanded form deliberately omits zero-preservation of size. Overall **SHIP-AS-STATED locally**; no orthogonal equivalence or malformed argument order. Upstream use existing normal form.

## Phase 6.0 — consumers and inline audit

One explicit use/one distinct named caller, zero external-to-file callers. Whole-word source inventory is not a kernel/simp dependency closure.

| Caller | Actual source usage | Refactor |
|---|---|---|
| `Roth.normOne_sum_le`, CoeffNorm90–92 | `Finset.le_sum_of_subadditive normOne normOne_zero.le normOne_add_le s f` | Replace zero witness by `(Finsupp.sum_zero_index (α := σ →₀ ℕ) (h := fun _ (z : ℤ) ↦ |(z : ℝ)|)).le`; retain sum and additivity arguments. Full consumer replay checked. |

Inline grep finds `simp [normOne]` in `normOne_neg` and `simpa [normOne]` in `normOne_le_card_mul`, but those prove negation invariance/cardinality bound, not a duplicate zero norm identity. Monomial/product identity proofs involve coefficient1; they are related elementary norm API, not zero-law duplicates. No separate complete zero law is rederived in production source.

The target is a useful simp API: the explicit caller alone precludes dead-code classification. Native direct proof-constant audit checks actual elaborated production proof terms for hidden uses of `Roth.normOne_zero`; its precise scope/results and replacement consumers are recorded in [callers](../evidence/Roth.normOne_zero/callers.json) and [consumer native receipt](../evidence/Roth.normOne_zero/native-consumers-success.json). The final audit inspected all293 canonical written declaration values, including private names and all4 LeanEval declarations; only `Roth.normOne_sum_le` directly contained the target-prefix constant. There were no additional implicit simp users in those293 values. The preliminary consumer receipt inspected289 values before LeanEval import and explicitly logged4 absent declarations; it is not presented as full coverage. A direct occurrence audit does not recursively inspect opaque/generated helper bodies or transitive dependency closure, does not quantify external users, and does not certify future simp behavior after deletion. The final [293-value audit source](../evidence/Roth.normOne_zero/native-full-audit-executed.lean.txt) and [receipt](../evidence/Roth.normOne_zero/native-full-audit-success.json) close the missing-module scope. Preserve the project-local simp theorem unless undertaking a separately authorized source refactor; do not infer safety of deletion solely from source grep.

Evidence: [source callers](../evidence/Roth.normOne_zero/rg-callers.json), [inline audit](../evidence/Roth.normOne_zero/rg-inline.json), [full fresh consumer snippet](../evidence/Roth.normOne_zero/native-consumers-executed.lean.txt).

## Phase 6 — actual composition

Exact old-interface term, fresh native checked:

```lean
example {σ : Type*} : Roth.normOne (0 : MvPolynomial σ ℤ) = 0 :=
  Finsupp.sum_zero_index (α := σ →₀ ℕ) (h := fun _ (z : ℤ) ↦ |(z : ℝ)|)
```

This is **one existing call**, no new helper, no project theorem premise, no absolute-value normalization proof. Representation conversion here is definitional and was checked by direct elaboration, rather than assumed. Isolated mathlib-only raw source guards target absence with `#check_failure Roth.normOne_zero`, replays original definition/proof, checks exact Finsupp application, expanded coefficient/output/index parameters and the no-zero-preservation test. No Roth imports occur. All accepted proof axioms are standard; no sorry/unsafe/native_decide/new axioms/raised resource limits.

Composition conclusion: **COMPOSABLE**, but more precisely the exact generic result already exists, so **NO-mathlib-has-it** rather than NO-composable. The original broad simp proof alone would be Phase6b borderline evidence; it is not the decisive argument. One failed native preparation with underconstrained coefficient metavariable is retained separately; its explicit-parameter correction compiled. Earlier declaration75 zero replay is historical context only and is not relabeled as a fresh80 verification.

## Phase 7 — verdict and actionable plan

**NO-mathlib-has-it**. Empty-support size aggregation already has its most general useful form in `Finsupp.sum_zero_index`. The independently compiled original-interface term proves the bridge, while generic raw experiments prevent an unnecessary zero-size premise. No Mode B parent re-aim override applies: parent75 is NO-composable, and this verdict comes from a fresh positive theorem hit, not inherited parent status. Size, proof length and implementation cost do not decide this verdict.

Alternative local destination: retain the useful `[simp]` convenience in `Roth/CoeffNorm.lean` with its parent API. No Archive/satellite library or new mathlib PR is indicated. For an authorized source refactor, replace the one explicit zero witness in `normOne_sum_le` by the displayed term; account for the actual implicit proof-constant audit, preserve a local simp bridge while parent spelling remains, and rebuild affected/downstream modules before deleting a public simp declaration. This read-only survey does not delete it or modify production.

Existing building blocks are fully located above. There is no new missing API. The parent's larger coefficient norm representation refactor remains separate; no new global polynomial norm instance or identity masquerading as a new norm is proposed. The verdict's action does not depend on unverified weakening, failed searches or the number of callers.

## Phase 8 — completion gates

All required phases PASS (definition-only checks and infrastructure n/a justified). Verification unresolved list is empty only after actual complete native receipts. [Verification manifest](../evidence/Roth.normOne_zero/verification.json) identifies exact executed sources, accepted/rejected receipts, standard axiom policy and audit scope. [Assessment](../evidence/Roth.normOne_zero/assessment.json), [overview entry](../evidence/Roth.normOne_zero/overview-entry.json), [portable validator](../evidence/Roth.normOne_zero/validate.py), [current copy manifest](../evidence/Roth.normOne_zero/copy-manifest.json) retain machine checks. Root independent acceptance is pending worker handoff; integration may add `root-acceptance.json`, explicitly exempted from worker file inventory while all current manifest hashes stay checked.
