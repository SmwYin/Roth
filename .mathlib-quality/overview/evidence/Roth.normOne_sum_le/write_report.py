from pathlib import Path
import json
D=Path(__file__).resolve().parent;N='Roth.normOne_sum_le';P='../evidence/'+N+'/'
def out(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
modern=[
['1','No','No ad hoc structure hypotheses to turn into instances. The generic existing theorem already uses additive and ordered typeclasses.'],
['2','No','Finite algebraic sum; no convergence or topology.'],
['3','No','An inequality constructs no universal object.'],
['4','No','No subset with closure predicates.'],
['5','Yes','Replace the polynomial carrier by any additive commutative monoid and real target by an ordered additive commutative monoid; existing Finset.le_sum_of_subadditive already does this.'],
['6','No','No categorical content requiring higher categories.'],
['7','Yes','Coefficient ℤ and target ℝ can be replaced in an expanded Finsupp coefficient-size representation; genericFinite verifies arbitrary M,N. Both finite-family and exponent indices are already arbitrary.'],
['8','Yes','Original proof is exactly one existing generic finite-sum call with normOne, project zero, project triangle as arguments. The entire concrete identifier appears on one body line; abstract properties suffice.'],
['9','Pass','False-generalization guard: weighted Finsupp preserves coefficient-size aggregation and specializes by abs∘Int.cast; Gauss maximum, supremum on unit circle, algebraic field norm and p<1 quasinorm do not preserve the same quantity.']]
strategy=[['1','No','No epsilon/delta topology.'],['2','No','Finite additive estimate, not an ideal or submodule inclusion.'],['3','No','No sequences or limits.'],['4','No','No universal construction.'],['5','Conditional','The generic finite induction exists; missing candidate is coefficient-size/Finsupp subadditivity bridge, separately assessed from finite induction. New proof is not counted as existing API.']]
infra=[[str(i),'n/a: theorem','No new definition, instance or computational representation introduced.'] for i in range(1,7)]
questions=['Should the finite coefficient-size bound remain a named local convenience in Roth/CoeffNorm.lean while the coefficient-size representation is settled?','If a general Finsupp coefficient-size subadditivity API is added upstream, should users invoke the existing Finset.le_sum_of_subadditive, or should that API also expose a finite-sum corollary for discoverability?']
out('generality.json',dict(fixed_interface='MAXIMALLY GENERAL: σ,ι arbitrary; no explicit hypotheses/typeclasses to drop while keeping Roth.normOne',expanded_forms=[dict(name='NormSumRaw.genericFinite',verified=True,status='native receipt required before freeze',meaning='κ-indexed size on finitely supported M-valued coefficients into ordered additive N; size zero vanishes and size subadditive')],modern_rows=modern,strategy_rows=strategy,infrastructure_rows=infra,future_questions=questions,cost_not_verdict_factor=True,parent_reaim='No Mode B override: normOne assessed NO-composable, not NO-mathlib-has-it.'))
lean_type='∀ {σ : Type u_1} {ι : Type u_2} (s : Finset ι) (f : ι → MvPolynomial σ ℤ), Roth.normOne (∑ i ∈ s, f i) ≤ ∑ i ∈ s, Roth.normOne (f i)'
out('overview-entry.json',dict(declaration=N,kind='theorem',type=lean_type,what='The coefficient ℓ1 size of a finite sum of integer multivariate polynomials is bounded by the sum of the coefficient sizes.',how='Finset.le_sum_of_subadditive applied to normOne using project normOne_zero and normOne_add_le.',hypotheses='Arbitrary variable type σ, family index ι, finite set s and polynomial family f; no Fintype, DecidableEq, degree or coefficient bound assumptions.',project_dependencies=['Roth.normOne','Roth.normOne_zero','Roth.normOne_add_le'],caller_summary='3 named direct consumers,4 source occurrences, all in CoeffNorm: normOne_mul_le99/101, normOne_det_le123, normOne_hasseDeriv_le152; full293 unique direct-proof audit.',mathlib_api_audit='Existing Finset.le_sum_of_subadditive supplies finite induction; norm_sum_le needs a seminormed additive group compatible with this coefficient size. Project triangle is not an existing mathlib building block.',moral_duplications='Abstract subadditive finite-sum bound and norm_sum_le; direct existing theorem specializes once the project zero/triangle witnesses are supplied.',generalization='Fixed normOne interface maximal; expanded generic Finsupp-weight finite bound verified over arbitrary additive commutative coefficient monoid and ordered additive target.',missing_api='Potential generic Finsupp sum subadditivity/coefficient-size bridge; existing finite induction itself has no gap.',junk='Not dead:4 occurrences in3 consumers. One-call local convenience whose upstream role follows coefficient-size API design.',action='BORDERLINE-needs-human: retain local finite wrapper for now; settle common coefficient-size API and discoverability question. No production change made.'))
s='''# Roth.normOne_sum_le — full mathlibable assessment

Canonical declaration **84/293**, `Roth/CoeffNorm.lean:90–92`. Verdict: **BORDERLINE-needs-human**. This read-only assessment is complete once the linked native receipts pass; upstream API questions below are design choices, not unresolved verification.

## Phase 0 — baseline and source

The shared `lake build` completed successfully (2467 jobs). All **17** current source/pin hashes were freshly matched against its input manifest; production sources and pins are unchanged. The declaration is a public theorem without sorry. The complete declaring module was read, including all consumer proofs: it develops integer multivariate coefficient ℓ1 estimates, products, determinants, Hasse derivatives, diagonal substitution and evaluation.

Evidence: [baseline](BASEbaseline-build.txt), [17 fresh inputs](BASEinputs.json), [hash check](BASEinput-hash-check.json), [whole module](BASEsource-module.lean.txt), [canonical location](BASEcanonical-order.json).

## Phase 1 — mathematical content and full native type

For any finite family of integer multivariate polynomials, the sum of absolute values of the coefficients of their sum is at most the sum of those coefficient sizes. Coefficient cancellation can decrease the left side. Iterating the binary triangle inequality over the finite family proves this; the empty family uses the zero-polynomial size.

```lean
∀ {σ : Type u_1} {ι : Type u_2} (s : Finset ι) (f : ι → MvPolynomial σ ℤ),
  Roth.normOne (∑ i ∈ s, f i) ≤ ∑ i ∈ s, Roth.normOne (f i)
```

`σ` indexes variables, `ι` indexes summands, `s` selects a finite subfamily and `f` is that polynomial family. There are no further hypotheses or typeclasses. The native print gives precisely `Finset.le_sum_of_subadditive Roth.normOne (Eq.le Roth.normOne_zero) Roth.normOne_add_le s f`.

Evidence: [exact original/replay source](BASEnative-original-executed.lean.txt), [complete native receipt](BASEnative-original-success.json).

## Phase 2 — preliminary checks

**SMALL**: a helper estimate, not a named theorem or main result and introduces no structure. Phase2b definition-only one-line/exemption test is **n/a: theorem**. Its one-line proof is still audited in Phase6; proof length alone does not settle upstream suitability.

## Phase 3 — exhaustive literature

The exact requests, response SHA256/UTF8 byte counts, titles/URLs and original short summaries are preserved below. Full web result/article bodies are not archived. Returned URL query strings are removed; original requests remain exact. Search access and direct page access are distinguished.

| Channel | Actual query / locator | Finding |
|---|---|---|
| General web: concrete | `polynomial coefficient l1 norm finite sum triangle inequality` | Coefficient ℓ1 norm; distinguish it from integrated polynomial L1 norm. [receipt](BASEweb-0.json) |
| General web: abstract | `subadditive function finite sum inequality ordered commutative monoid` | Existing abstract finite-subadditive theorem appears in historical mathlib documentation. [receipt](BASEweb-0.json) |
| General web: aliases | `Minkowski inequality l1 norm finite sums polynomials length` | Norm triangle / Minkowski terminology. NIST DLMF§1.7 states p>1; it alone does not prove the endpoint p=1. [receipt](BASEweb-0.json) |
| ChatGPT math | n/a: `ask_chatgpt_math` unavailable | Optional channel unavailable; other channels executed. |
| Local reference | `clean.tex` lines437–497, Lemma3 proof | Defines coefficient size, uses triangle and finite determinant sum. [excerpt](BASElocal-literature.txt), [source hash](BASElocal-literature-source.json), [actual search](BASErg-local-literature.json) |
| nLab | `site:ncatlab.org/nlab norm triangle inequality finite sum` | Indexed norm-on-abelian-group and p-norm pages; direct norm-page fetch unsupported XHTML. [search](BASEweb-1.json), [direct access](BASEweb-7.json) |
| nCatLab | `site:ncatlab.org/ncatlab subadditive norm finite sum` | Returned nLab material, no distinct categorical standard. Direct subadditive-function page inaccessible; not an absence proof. [search](BASEweb-2.json), [direct access](BASEweb-7.json) |
| Stacks | `site:stacks.math.columbia.edu norm triangle inequality finite sum` | Returned field norm/trace and derived-category triangles, different concepts; no coefficient ℓ1 standard from this channel. [receipt](BASEweb-3.json) |
| MathOverflow | `site:mathoverflow.net polynomial coefficient norm sum absolute values triangle` | Question465899 explicitly defines integer coefficient ℓ1 norm; uniform polynomial norms in other hits differ. [receipt](BASEweb-4.json) |
| Recent arXiv | Three actual requests restricting after2021-10-27 and before2026-10-28 | Initial noisy results; refined query found2026 Montel/Cauchy coefficient-length context, not a new finite triangle law. [initial](BASEweb-5.json), [refined](BASEweb-6.json) |
| Primary supplementary teaching source | Hunter, Chapter7 Definition7.11 and Example7.15, pp95–96; §7.6 | General norm axioms and ℓp, with p=1 directly verifiable. [access receipt](BASEweb-7.json) |

Sources: [Hunter Chapter7](https://www.math.ucdavis.edu/~hunter/m125a/intro_analysis_ch7.pdf), [nLab norm](https://ncatlab.org/nlab/show/norm), [DLMF1.7](https://dlmf.nist.gov/1.7), [MathOverflow465899](https://mathoverflow.net/questions/465899/what-is-the-smallest-mathbbzx-multiple-of-x-1n-in-the-coefficient-ve/465997), [Krishna2026 abstract](https://arxiv.org/abs/2606.19355). The recent abstract is relevant context only; no theorem about our exact finite sum is attributed to it.

Concept: finite triangle inequality for coefficient ℓ1 size, also polynomial length. The broader standard law applies to any seminorm, or simply any subadditive size nonpositive at zero. No polynomial multiplication, integer-specific degree theory or finite variable assumption is essential to finite induction. This is inferred from the shared mathematical pattern and is independently checked against the pinned abstract theorem.

## Phase 4a — every parameter and hypothesis

| Item | Current form | Generality audit |
|---|---|---|
| Variable index | arbitrary `σ : Type*` | Already arbitrary; neither finiteness nor decidable equality is assumed. |
| Family index | arbitrary `ι : Type*` | Already arbitrary and independent of σ. |
| Family selection | `s : Finset ι` | Finite sum, including empty; replacing it by an infinite family requires summability/topology and changes the statement. |
| Family | `f : ι → MvPolynomial σ ℤ` | Arbitrary polynomials, no bounds or support restrictions beyond inherent finite support. |
| Coefficients | `ℤ`, fixed by `normOne` | Changing coefficient carrier requires expanding the parent representation; not dropping a theorem parameter. |
| Size target | `ℝ`, fixed by `normOne` | Abstract ordered target possible in expanded representation, already supported by finite induction. |
| Hidden hypotheses | none | No removable theorem typeclasses or extra assumptions. |

## Phase 4b — verified generality

**MAXIMALLY GENERAL within the fixed `Roth.normOne` interface**. No theorem assumption can be weakened while retaining that definition. The fresh Roth-free experiment also proves a broader **expanded representation**, `NormSumRaw.genericFinite`:

```lean
{κ ι M N : Type*} [AddCommMonoid M] [AddCommMonoid N]
[Preorder N] [IsOrderedAddMonoid N]
(size : κ → M → N) (hzero : ∀ i, size i 0 = 0)
(hadd : ∀ i a b, size i (a + b) ≤ size i a + size i b)
(s : Finset ι) (f : ι → κ →₀ M) :
(∑ i ∈ s, f i).sum size ≤ ∑ i ∈ s, (f i).sum size
```

This checks coefficient carrier, target and index generality mechanically. It requires a newly proved Finsupp subadditivity helper, not an existing mathlib replacement. This hzero=0 formulation is sufficient, not asserted maximal among all possible weighted APIs: nonnegative-at-zero variants would require their own normalization proof. The original coefficient size is recovered by `size := fun _ (z : ℤ) ↦ |(z : ℝ)|`. Cost is not a verdict factor.

Evidence: [exact fresh Roth-free source](BASEnative-raw-executed.lean.txt), [complete native success](BASEnative-raw-success.json), [generality inventory](BASEgenerality.json).

## Phase 4c — all nine modern-idiom rows

MODERNROWS

Q8 diagnostic: all concrete names occur in the single original proof-body line passed to `Finset.le_sum_of_subadditive`; no polynomial property enters after the abstract zero/subadditivity premises are supplied. The abstract finite-sum law **already exists**. Moving size onto a common coefficient representation could improve reuse, but it would need its own upstream API decision. This theorem does not independently introduce that API.

## Phase 4.5 — infrastructure risk

All six rows—instance diamonds, definitional-equality alignment, reduction transparency, typeclass search, coercion/notation ambiguity and computational representation—are **n/a: theorem**. This declaration introduces no instances or data. The separately discussed parent representation should be reviewed if redesigned. [Six-row inventory](BASEgenerality.json).

## Phase 4.6 — all five proof-strategy rows

STRATEGYROWS

Strategy: **MATHLIB-IDIOMATIC** finite induction. A generic coefficient-size subadditivity bridge may be useful upstream, but finite induction should continue using existing mathlib. Proving support-union triangle again in each consumer would duplicate mathematics and does not support a NO-composable certificate.

## Phase 5 — all five actual formal-search methods

Each method was run against current, literature-standard and abstract forms; exact raw requests/results are in [formal inventory](BASEformal-search.json). Every individual call is also archived.

| Method | Current form | Standard form | Abstract form |
|---|---|---|---|
| Lean-Finder | coefficient l1 polynomial finite-sum query; related Mahler/Gauss hits | `norm of finite sum is at most sum of norms` → `norm_sum_le` | subadditive finite-sum description → `Finset.le_sum_of_subadditive` |
| Loogle | quoted `normOne_sum_le`: no hit | `norm_sum_le`: positive | initial unqualified query rejected; first retry rate-limited; qualified second retry succeeds |
| LeanSearch | coefficient norm query → `norm_sum_le` and relatives | finite norm query → standard norm API | abstract query → generic subadditive finite-sum API |
| rg | [current spelling](BASErg-current.json), [full-name audit](BASErg-full-name.json) | [norm/length files](BASErg-literature.json) | [Finsupp and finite-order files](BASErg-abstract.json) |
| Local search | project declaration found in source fallback | no returned standard hit | no returned abstract hit; all report `index: unavailable` |

Unavailable local index and external search failures do not prove absence. Finder/LeanSearch external signatures use PartialOrder while the pinned Loogle/native signature uses Preorder; the pinned source/native check controls. The additive declaration is generated by `@[to_additive le_sum_of_subadditive]` at `Mathlib/Algebra/Order/BigOperators/Group/Finset.lean:95`, and documented at103. [Pinned source](BASEmathlib-finset-order.lean.txt), [hashes](BASEmathlib-inputs.json).

Positive candidates checked natively: `Finset.le_sum_of_subadditive`, `norm_sum_le`, `Finsupp.sum_of_support_subset`, `Finset.sum_le_sum`, `abs_add_le`. `norm_sum_le` is in `Mathlib/Analysis/Normed/Group/Basic.lean:809`. The pinned [Lp Finsupp module](BASEmathlib-lp-finsupp.lean.txt) supplies metrics on `WithLp p (ι →₀ X)`; it does not itself supply the compatible seminormed-additive-group instance and bridge needed to apply norm_sum_le directly to the old coefficient-size spelling. No metric-only hit is silently promoted into an exact norm theorem.

## Phase 5.5 — statement shape

Normal form: **OK locally**. Equivalent mathematical forms are coefficient-support sums, generic Finsupp weighted sums and norm notation after a compatible norm representation. Prefer a common coefficient representation before proliferating pairwise bridges. This is an inequality, so an equivalence-RHS simp direction is inapplicable.

Syntactic generality: explicit `s,f` works at all four sites; making the index finite with an univ sum would add needless assumptions. Generic finite-weight restatement and inlining were actually tested. Superfluous argument audit: σ determines monomials; ι determines family; s selects summands; f determines each polynomial. All four are essential; no typeclasses to drop. **SHIP-AS-STATED locally**, settle representation before upstreaming.

## Phase 6.0 — all source callers and inline audit

| Explicit direct caller | Source occurrences | Refactor experiment |
|---|---|---|
| `Roth.normOne_mul_le` |99,101| Both occurrences replaced by full abstract finite-sum call using project zero/add witnesses. |
| `Roth.normOne_det_le` |123| Determinant expansion first inequality replaced by that call. |
| `Roth.normOne_hasseDeriv_le` |152| Hasse monomial expansion first inequality replaced by that call. |

**3 named consumers,4 occurrences;0 external-to-file callers.** All complete consumer proofs were read and re-elaborated after replacement, not just miniature goals. The actual [source grep](BASErg-callers.json) has five lines including the declaration. The [inline grep](BASErg-inline.json) finds no independent finite coefficient-size rederivation bypassing this helper.

The fresh direct proof-value audit examines the exact canonical **293** declarations, with runtime uniqueness guard, and reports293 requested/present/values and293 unique names. Its name array is generated in canonical order with private-name modules intact, and the validator compares the exact array source to current declaration-order.json. Direct consumers are exactly the three above. This is direct proof-value dependency, not transitive kernel or simp closure; downstream determinant consumers may depend indirectly. The replacement consumer proofs deliberately retain other project lemmas; they demonstrate local inlining, not mathlib-only replacement.

Evidence: [exact consumer/audit source](BASEnative-consumers-executed.lean.txt), [raw native receipt](BASEnative-consumers-success.json), [canonical array](BASEcanonical-audit-array.lean.txt), [callers inventory](BASEcallers.json).

## Phase 6 — composition experiments

1. Exact original: one existing `Finset.le_sum_of_subadditive` call **plus project** zero and triangle witnesses. This compiles; it is not a ≤3-call composition solely from mathlib. `Roth.normOne_add_le` is a substantive project theorem, not an existing building block.
2. Fresh Roth-free coefficient-size route: the guard confirms project target absent; a new generic Finsupp subadditivity proof aligns support unions using `Finsupp.sum_of_support_subset`, sums pointwise bounds, then specializes abs∘Int.cast. Finite induction is one existing mathlib call afterward. The newly proved generic/direct helpers are counted as new proofs, never as existing API.
3. All complete consumer inlinings compile and retain project triangle/zero. No source change is proposed by this read-only assessment.

Thus the **exact original form is NOT-COMPOSABLE under the strict ≤3 existing mathlib-call gate** on the evidence available; the higher-level finite-subadditive law is already in mathlib. No closing `simp [defs...]` is promoted to a composition certificate. There is **no Mode B parent re-aim override**: normOne was assessed NO-composable, not NO-mathlib-has-it; parent triangle was BORDERLINE, which is not a proof of this declaration's verdict. The independent checks above establish the distinction.

## Phase 7 — verdict and concrete next actions

**BORDERLINE-needs-human.** The finite-induction mathematics is fully covered by an existing general theorem. The exact project quantity still needs its coefficient-size triangle witness, whose suitable general upstream API is unsettled. Treating that new witness as already-existing mathlib would create a false NO certificate; proposing a new generic finite induction theorem would duplicate existing mathlib. The four consumer uses support retaining a discoverable local API while the shared representation is settled.

1. Should the finite coefficient-size bound remain a named local convenience in `Roth/CoeffNorm.lean` while the coefficient-size representation is settled?
2. If a general Finsupp coefficient-size subadditivity API is added upstream, should users invoke the existing `Finset.le_sum_of_subadditive`, or should that API also expose a finite-sum corollary for discoverability?

These are future API questions and require no user interruption for completing this overview. Recommended current destination: **project-local `Roth/CoeffNorm.lean`**. If the local wrapper is later removed, replace all4 occurrences in the3 named consumers by `Finset.le_sum_of_subadditive normOne normOne_zero.le normOne_add_le _ _`; all complete proof experiments already verify that plan. No standalone finite-induction PR is proposed. A broader coefficient-size PR should coordinate with the binary subadditivity/representation design; it must not re-add a generic finite induction theorem mathlib already has. No cost-based downgrade is used.

## Phase 8 — verification and handoff

Accepted sources and raw native results are enumerated in [verification](BASEverification.json); standard axiom basis only (`propext`, `Classical.choice`, `Quot.sound`), no errors/warnings/partial results. The portable [read-only validator](BASEvalidate.py) validates exact current manifest hashes,17 inputs, canonical293 unique/order coverage, all mandatory phases, all formal methods/forms, all literature channels, links and credential guard. The [current copy manifest](BASEcopy-manifest.json) is authoritative; a historical worker manifest never substitutes for current validation. Root acceptance remains pending independent review. Production Lean and pins remain unchanged.
'''
s=s.replace('BASE',P)
def table(rows):return '| # | Applies? | Finding |\n|---|---|---|\n'+'\n'.join('| '+' | '.join(r)+' |' for r in rows)
s=s.replace('MODERNROWS',table(modern)).replace('STRATEGYROWS',table(strategy))
(D/'report.md').write_text(s)
print('Draft full report and generality/overview JSON prepared; native gates still control completion.')
