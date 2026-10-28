from pathlib import Path
import json
D=Path(__file__).parent;N='Roth.three_small_factors';P='../evidence/'+N+'/'
def link(n,label=None):return '['+(label or n)+']('+P+n+')'
typ=json.loads((D/'native-type.json').read_text())['type']
s='''# Roth.three_small_factors — canonical241

Verdict: **BORDERLINE-needs-human**. Completed read-only assessment; root acceptance pending.
The exact Roth numerical package is useful locally. A generic floor-power absorption lemma is
verified, but its public API boundary is a mathematical organization question. This verdict
is independent of earlier floor/log assessments and does not rest on implementation cost.

## Phase0 — baseline and integrity

The declaration resolves at `Roth/MainLemma.lean:180`; it is a public theorem, with no sorry.
The module proves Roth's main lemma using polynomial boxes, pigeonhole counting, Hasse
derivatives and height estimates. All17 source/pin hashes freshly match the tracked shared
manifest, so the successful2467-job baseline applies. The later accepted full build at228
is supplementary; no extra full-file-end build is prescribed at241.

'''+link('inputs.json')+'; '+link('input-manifest.json')+'; '+link('baseline-build.txt')+'''.
Production files, pins and Git were unchanged. Only the authorized scratch document and this
package were written. The persistent nine imports and isolated18-import prefix were preserved.
The exact canonical293 array was generated from tracked order, checked before native execution,
and checked again before freeze. Runtime: requested293, unique293, present293, values293.

'''+link('preparation-checks.json')+'; '+link('canonical-snapshot.json')+'; '+link('canonical-consumers.json')+'''.

## Phase1 — mathematical content

Let δ be nonnegative, m,q₁,r₁ natural with r₁ positive, A nonnegative, and α real. Put
X=q₁^(δr₁) and B₁=⌊X⌋₊. If
2m+1+2m log(1+A)+2m log(1+|α|)≤δ² log q₁,
then each of 2^(mr₁), (1+A)^(mr₁), and (1+|α|)^(mr₁) is strictly below B₁^δ.
There is no positive-dimension premise: m=0 is intentional.

Full kernel type, obtained from Lean.getConstInfo with pp.funBinderTypes=true:

```lean
'''+typ+'''
```

The proof first obtains 1≤δ²log q₁ and log2<1. Natural q₁ then supplies enough separation
to prove X>2 using `two_lt_rpow_aux`. The floor satisfies √X<B₁ and
½δr₁log q₁<log B₁. The budget forces δ>0, so multiplication by δ preserves the strict
floor gap. A common key combines 2m log t≤δ²log q₁ with that gap and
`Real.lt_rpow_of_log_lt`; `Real.log_pow` normalizes the natural exponent. Finally the budget
is allocated to t=2,1+A,1+|α|. Nonnegative logarithms prevent either of the latter two terms
from subsidizing the others.

Project body dependencies are exactly `mainCoeffBound`, private `two_lt_rpow_aux`,
`sqrt_lt_floor`, and `mul_log_div_two_lt_log_mainCoeffBound` at source-declaration level.
The original full module was replayed under a fresh namespace, renaming only the target
outside the separately generated canonical array. Its full original type is definitionally
equal to the replay type. Original and replay use only propext, Classical.choice, Quot.sound.
The kernel printer explicitly elided78949characters of the large arithmetic body; this is
not a complete kernel-body dump. The full exact written source and raw printer receipt are
preserved, together with full type, axioms and all293 kernel-value checks.

'''+link('target-excerpt.lean.txt')+'; '+link('source-MainLemma.lean.txt')+'; '+link('native-type.json')+'; '+link('original-executed.lean.txt')+'; '+link('original-receipt.json')+'''.

## Phase2 — preliminary checks

**SMALL**: an arithmetic helper, not a named theorem, new structure or listed main result.
One-line-definition check: **n/a**, theorem. The long arithmetic proof is assessed on its
mathematics, not on its line count or a short alternate spelling. Literature search remains
exhaustive.

## Phase3 — exhaustive literature search

All named channels were actually queried; the optional mathematical ChatGPT tool is unavailable.
Every web receipt stores the exact request, returned-text SHA256/byte count/status, clean
returned titles/URLs/locators and an original concise summary. Full response/article bodies
are not archived. Returned URL query parameters were removed and incomplete URLs omitted.
A search result's displayed freshness is not treated as a paper's publication date.

| Channel | Actual query or source | Result and interpretation | Receipt |
|---|---|---|---|
| General specific | Roth theorem auxiliary polynomial three small factors coefficient bound floor logarithm | Soundararajan/Petrow notes and other auxiliary-polynomial expositions; no separate named triple identified | WEB1 |
| General broad | power of floor x logarithmic lower bound square root floor exponential inequalities | Rounding and elementary logarithmic inequalities; DLMF §4.5.1 relevant | WEB2 |
| General aliases | Roth lemma 9 auxiliary polynomial height estimates logarithmic parameter choice | Auxiliary polynomial and height terminology; constants depend on exposition | WEB3 |
| ChatGPT mathematics | Standard/general/historical formulation | justified n/a: ask_chatgpt_math unavailable | n/a |
| Local references | clean.tex §6, eqs32,37, three-small-factors and following Lean note | Exact local source for all3 factors; original uses stricter assumptions, current Lean admits weak budget and m0 | LOCAL |
| nLab | site:ncatlab.org/nlab logarithm exponential order inequality | Logarithm/order background; no canonical floor-budget theorem established | NLAB |
| nCatLab distinct namespace | site:ncatlab.org/ncatlab logarithm exponential inequality | Returned mostly /nlab and other out-of-namespace material; no relevant categorical law established | NCAT |
| Stacks | site:stacks.math.columbia.edu logarithm height polynomial bound | Heights/background do not select this numerical triple; no AG abstraction needed | STACKS |
| MathOverflow | site:mathoverflow.net Roth theorem auxiliary polynomial height bounds | Checked discussions, no verified exact replacement from a snippet | MO |
| Recent arXiv | site:arxiv.org Roth theorem auxiliary polynomial height logarithm after:2021-10-28 before:2026-10-29 | Explicit five-year interval; noisy/unrelated results, not evidence of a new canonical full triple | ARXIV |
| Primary follow-up | DLMF §4.5; Soundararajan/Petrow PDF; Milojevic PDF | Opened primary texts; DLMF4.5.1 logarithm inequality, notes §§15–16 Proposition5, Milojevic January2022 §5 Lemma5.1 | PRIMARY |

Concept: absorption of fixed height factors by a large coefficient scale, using logarithms
and a rounding lower bound. No literature consensus makes this exact three-factor conjunction
an independently named general theorem. The local source explicitly packages the triple for
Roth's proof; other expositions choose different coefficient constants. This supports a
separate decision about generic floor-power API versus keeping the numerical package local.
It does not prove library absence. Primary background:
[DLMF4.5.1](https://dlmf.nist.gov/4.5.E1),
[Soundararajan/Petrow notes](https://math.stanford.edu/~ksound/TransNotes.pdf),
[Milojevic's exposition](https://aleksa-milojevic.github.io/expository/roth.pdf).

## Phase4a–b — every parameter and assumption

| Parameter/hypothesis | Use and weakening analysis | Verified evidence/decision |
|---|---|---|
| ℝ, its log/rpow | Real logarithms, real powers, square roots and natural floor | Arbitrary ordered field has no such default API. Algebraic transport can be abstracted only after supplying analytic hypotheses; no unsupported typeclass weakening claimed |
| δ≥0 | Budget rules out δ0; hence δ>0 and multiplication of floor-log gap is strict | Dropping sign is false: δ=-3,q2,m1,r1,A0,α0 has3≤9log2, but floor(2^-3)=0 and2<0 fails; full budget+failed conclusion compiled |
| m:ℕ | Natural power and dimension count | m0 retained; compiled zeroVariables even permits arbitrary real A |
| q₁:ℕ | Natural q with positive log implies q≥2; this lower base spacing enters twoPower | Generic floorPower instead takes arbitrary real X≥2; realPower reconstructs real q≥0 and arbitrary exponent transport. These are separate verified representations, not automatic weakening of all budget hypotheses |
| r₁>0 | Ensures X sufficiently large; positive multiplication where used | Dropping it fails with m0,δ1,r0,q=ceil(exp1): budget holds but1<1 fails; compiled noRPositiveGuard |
| A≥0 | Supplies log(1+A)≥0, protecting first and third factors as well as its own | Mechanically weakened to hlogA:0≤log(1+A), all3 conclusions compiled. A=-2 admitted explicitly; no claim that this is the maximal valid domain |
| α arbitrary real | Absolute value gives1+|α|≥1 and nonnegative log | Already no sign restriction; abstract positive base can replace expression in a different generic lemma |
| Non-strict budget≤ | Allocates log cost to each factor | Strict conclusions compile at equality. Concrete equality witness m0,q2,r1,A0,α0,δ=√(1/log2) is nonvacuous |
| Numerical2m+1 and factors2 |2m controls log2<1; positive residual1 rules out δ0 even at m0 | Compiled noSlackGuard: deleting residual1 allows allzero budget with δ0,m0 but1<1 fails. No optimality claim for positive m or coefficient2 |
| Three conclusions | All3 receive one shared strict floor-log gap | All3 genuinely used across actual callers; retain conjunction locally |

The A weakening is mathematical, not just unused-variable deletion: it also admits negative
bases because Lean's real log is log of absolute value off zero and totalized at zero, while
the left powers are natural. For A=-2 the base is−1; the proof still establishes the **first**
and **third** strict conclusions. This does not make negative A a meaningful nonnegative
coefficient height in callers. Merely assuming1+A>0 is insufficient: take m1,q2,r1,δ0,α0,
A=exp(-2)-1. Then the base is positive, the budget is−1≤0, and first factor2<1 is false.
The complete exact counterexample is compiled as noASignGuard.

Verified generic candidate, independent of project definitions:

```lean
theorem floorPower {X t δ : ℝ} {s : ℕ} (hX : 2 ≤ X) (hδ : 0 < δ)
    (h : (s : ℝ) * Real.log t ≤ δ * Real.log X / 2) :
    t ^ s < (⌊X⌋₊ : ℝ) ^ δ
```

This is a **new proof written for this assessment**. It uses a reconstructed strict
rootFloor/logFloor inequality and log monotonicity; it is not an existing mathlib replacement.
The exact triple's hA is strictly stronger than the verified logarithmic-domain premise.
The choice of a public upstream interface remains open, so the verified weakening alone does
not force YES-but-generalise-first for the audience-specific conjunction.

'''+link('isolated-executed.lean.txt')+'; '+link('isolated-receipt.json')+'''.

## Phase4c — all9 modern-idiom rows

| # | Question | Result and concrete consequence |
|---|---|---|
|1| Typeclasses/instances | No. Scalar size conditions should remain explicit; no custom structural Prop/class |
|2| Filters/nets | No. Finite explicit estimates rather than convergence; replacing budget with eventual asymptotics loses concrete bound |
|3| Universal property | No object being constructed |
|4| Bundled substructures | No closed subset or algebraic substructure |
|5| Weaker hierarchy | No immediate ℝ→field weakening supports log/rpow/floor; generic algebraic transport is distinct |
|6| Higher category | No categorical content |
|7| Concrete index | s:ℕ in floorPower abstracts m*r; arbitrary natural exponent usable without reconstructing a variable dimension |
|8| Concrete-via-abstract diagnostic | In original key mainCoeffBound appears in2 proof lines before log_pow and no later arithmetic line; other bases disappear into log t. Verified floorPower takes arbitrary X,t,s,δ; downstream any floor-defined scale can absorb powers without q natural, m, A or α |
|9| False-generalization guard | Removing A sign altogether rejected by first-factor counterexample. hlogA widening preserves all3 scalar statements but changes height interpretation outside nonnegative A. floorPower preserves the domination mechanism; it is not definitionally the exact triple, nor an existing library theorem |

A real organizational improvement exists as a possible **new generic floor-power estimate**:
it composes with natural floor bounds and `Real.log_pow`/`Real.lt_rpow_of_log_lt` for arbitrary
real scale X and arbitrary natural exponent s. The fixed bases2,1+A,1+|α| express Roth's
specific height costs; simply renaming them would not provide a more reusable semantic law.
The actual reusable parameters are X,δ,s and a logarithmic budget. Public packaging is the
question, not whether categorical notation looks more modern.

## Phase4.5 — infrastructure risk

All six risk rows are justified n/a because the target is a theorem: typeclass diamonds,
reducibility leakage, noncanonical unfolding, instance priorities, universe-polymorphism of
data and coercion ambiguity. It introduces no instance, data representation or coercion.
No new custom typeclass was proposed. Overall theorem infrastructure risk n/a.

## Phase4.6 — proof strategy, all5 rows

| # | Strategy question | Assessment |
|---|---|---|
|1| ε–δ versus filters | n/a, explicit scalar bound |
|2| Elements versus substructures | n/a, no inclusion law |
|3| Sequences versus nets | n/a, no limiting argument |
|4| Construction versus universal property | n/a, inequality proof |
|5| Missing helper API | Potential floorPower/logFloor helper. Deriving it takes a genuine strict floor inequality and logarithmic normalization; existing transport alone does not allocate the triple's budget |

Current strategy is mathematically idiomatic: one key estimate used at3 bases, with numerical
slack exposed. If generic API is accepted, refactor by proving floorPower once and retaining
local budget allocation. This is cleaner factoring, with moderate proof refactoring; cost
is not the verdict reason. No replacement by asymptotics preserves the explicit bound.

## Phase5 — all15 actual formal-search cells

External indexes need not match this pin. Positive candidates were checked against pinned
source and native signatures; search no-hits are not proofs of absence. Local index reports
**error** in all3 cells while source results still return; no empty local result is used as
an absence claim. Formal raw requests/results and timings remain intact.

| Form | Finder | Loogle | LeanSearch | rg | local |
|---|---|---|---|---|---|
| Current triple and floor budget | Behrend/additive Roth near-misses; different theorem | log/rpow/floor pattern no hit | Nat base-log arithmetic, different types | full current/floor/log search | target source hit; index error |
| Literature-standard floor-power absorption | Behrend and log_natCast_le_rpow_div partial neighbors | log/floor sum bounds, not target | Nat.log/clog inequalities, not real log | sqrt/floor/log combinations | floor names; index error |
| Abstract power/log transport | Real.lt_pow_of_log_lt and zpow variants | **Real.lt_rpow_of_log_lt** | **Real.pow_lt_iff_lt_log** and le variants | exact transport/log normalizers | Real.lt_rpow_of_log_lt source hit; index error |

'''+link('formal-search-matrix.json')+'; '+link('full-name-search.json')+'; '+link('mathlib-inputs.json')+'''.
The matrix identifies all15 receipts individually. Pinned `Pow/Real.lean` supplies
`Real.lt_rpow_of_log_lt : 0<y → log x<z log y → x<y^z`, and
`Real.pow_lt_iff_lt_log` handles natural powers with both positive bases. `Real.log_pow`
needs no positivity premise and `Real.log_rpow` needs positive base. `Log/Basic.lean` has
log nonnegativity and strict log upper bounds; `Floor/Semiring.lean` has `Nat.floor_le`
and `Nat.lt_floor_add_one`. None of the verified hits is the full three-factor budget law.
No blanket semantic absence is claimed. No broad numerical exact? search was repeated:
previous default-heartbeat exhaustion is inconclusive, and resource limits were not raised.
Instead the independent generic route and concrete candidate applications were compiled.

## Phase5.5 — statement shape

**Normal form:** alternatives are natural-power inequalities, their logarithmic inequalities,
and a generic floorPower premise. The canonical mathlib transport is log-to-rpow; exact
Roth package already uses ordinary natural powers and real rpow. This is not an equivalence
network needing O(n²) bridges. No RHS-normal-form violation.

**Syntactic generality:** attempted and compiled (i) hlogA instead of hA, (ii) one common
floorPower estimate instead of named triple, (iii) zero-variable specialization with arbitrary
A, (iv) equality-budget specialization. The conjunction is convenient because callers project
different components. A public generic estimate should name scale/exponent/log budget instead
of hardcoding Roth's coefficient definition. Keep exact local statement stable pending design.

**Superfluous argument audit:** δ sign and r positivity have full counterexamples after
removal; m is an exponent parameter with permitted zero; q determines scale; α has no sign
premise; A nonnegative can be weakened to log-domain nonnegativity but cannot simply be
removed; h32 supplies actual magnitude and its≤boundary is already sufficient. No typeclasses
or universes beyond concrete natural/real types. No unverified parameter deletion proposed.
Overall: exact local form acceptable; **RESTATE-BEFORE-SHIP** for a future generic upstream
candidate, rather than adding this coefficient-specific name verbatim.

## Phase6.0 — callers, inline audit and scope

| Actual caller | Location | Components consumed |
|---|---|---|
| private exists_mem_RSet_le_index_of_log_bound_aux | MainLemma:631 | second factor; α specialized to0 |
| private exists_auxiliary_polynomial_of_log_bound_aux | MainLemma:656 | first and third for derivative/evaluation bound |
| private roth_product_bound_aux | Main:502 | first for product of degree factors |

3 body occurrences,2 modules; counting only external-to-declaring-file uses gives1 in1file.
The source and tracked Git searches agree. No separate equivalent inline derivation was found
in scoped production sources. That is a source lexical observation, not global dead-code proof.
No statement/type occurrences or simp attribute are present. The independent canonical293
kernel audit finds exactly these3 direct proof-value consumers and no direct type consumers.
Transitive callers include main_lemma and roth; they are not extra lexical occurrences.

All actual caller bodies and their entire original modules were replayed in one new namespace.
The target declaration was removed and its original argument-taking proof was inserted locally
at each actual site as factorBounds; all other caller signatures remain unchanged. Runtime
compared the3 actual private caller types with the originals and checked their direct proof
values do not retain Roth.three_small_factors. The separate2 endpoint axiom checks are
main_lemma and roth; these are not5 signature comparisons. The original and scratch private
names were resolved with their correct modules using env.mainModule for scratch. This is a
verified inlining experiment, not a claim that inlining is stylistically preferable or that
a new proof has become existing mathlib API.

'''+link('callers.json')+'; '+link('source-search.json')+'; '+link('tracked-source-search.json')+'; '+link('inline-search.json')+'; '+link('source-Main.lean.txt')+'; '+link('inline-executed.lean.txt')+'; '+link('inline-receipt.json')+'''.

## Phase6 — composition experiments

| Attempt | Actual result | Interpretation |
|---|---|---|
| Real.lt_rpow_of_log_lt applied directly to half-log floor premise | fail_if_success confirms type/premise mismatch | It needs the log of the actual floor and a strict bound; original budget is not that premise |
| Real.pow_lt_iff_lt_log on same premise | fail_if_success confirms mismatch | Natural-power transport is not a floor lower bound or three-budget allocation |
| existingTransport from supplied strict log bound | Compiles using Real.lt_rpow_of_log_lt plus Real.log_pow equality transport | Existing abstract terminal step is at most2calls; it does not prove its input |
| floorPower | Compiles using reconstructed rootFloor/logFloor and a strict multiplication argument | New generic proof; not a≤3-existing-call witness |
| Full original triple isolated | Compiles without any Roth import/definition | Genuine arithmetic reconstruction, not a mathlib lookup hit |
| Actual3 callers inlined | Compiles; original signatures retained | Shows local refactoring feasibility, not mathematical triviality |

Conclusion: **NOT-COMPOSABLE** as a demonstrated≤3-existing-mathlib-call derivation of the
original theorem. None is a closing simp composition. This is an evidence statement, not an
unproved universal nonexistence claim. New rootFloor/logFloor/twoPower/logDomain/floorPower
proofs cannot be counted as pre-existing mathlib building blocks.

## Overview cross-checks: moral duplication and missing API

| Decl A | Decl B | Same statement? | Same proof? | Action |
|---|---|---|---|---|
| three_small_factors | sqrt_lt_floor | No; bounds3powers vs one floor | Uses it as strict floor prerequisite | Keep roles distinct |
| three_small_factors | mul_log_div_two_lt_log_mainCoeffBound | No; log lower bound vs allocated3factor estimates | Strict log lower bound is input to shared key | Do not inherit parent verdict |
| three_small_factors.key | floorPower candidate | Same domination mechanism after supplied half-log budget | Shared logarithmic transport, different interface and new proof | Consider generic API, retain local budget allocation |
| three_small_factors | Real.lt_rpow_of_log_lt | No; full arithmetic budget vs one supplied strict log premise | Terminal transport only | Existing API cannot stand in for missing premise |

Missing API candidate is the generic floor-power absorption boundary. The exact triple is
used, valid and not junk. Its3callers use all3factors, so deleting an allegedly unused
component would be wrong. The natural local destination is `Roth/MainLemma.lean`; making
it private later is a visibility decision requiring a matching Main caller refactor.

## Phase7 — verdict and concrete future upstream questions

**BORDERLINE-needs-human**, with all assessment work complete. The mathematical content is
stronger than the source paper at the weak-budget boundary and m0, and the independent proofs
verify those refinements. Existing mathlib handles logarithm/exponent transport; a primary
floor gap and the budget allocation remain actual proofs. Thus neither NO-mathlib-has-it nor
NO-composable has a supported replacement witness. Conversely, the exact triple's fixed
height factors and coefficient definition remain specific to Roth's bookkeeping, and no
literature channel makes that packaging a standard public theorem.

The independent floorPower candidate has a clearer reuse boundary. Its potential value is
that any floor-defined scale can absorb a natural power from a half-log budget. The remaining
judgment concerns which layer should be public, and the semantics of broad log-domain bases;
it is not a question of assessment completeness or proof cost.

1. Should upstream expose floorPower from a non-strict half-log budget, or keep
   Real.lt_rpow_of_log_lt plus a primary floor/log estimate as the public boundary?
2. Should this exact three-factor conjunction and numerical budget remain a private Roth
   proof helper, considering only the generic floor-power inequality for upstream?
3. For a public generic interface, should hypotheses retain nonnegative height bases or
   explicitly support the broader log-nonnegative domain including negative natural-power bases?

Future action: decide those API questions before proposing an upstream patch. Keep production
unchanged now. If local inlining is chosen, replace the two MainLemma uses and Main's product
bound with the verified local argument; if generic API is chosen, prove/clean the generic law
first and reapply the triple's numerical allocations. No YES-specific PR home/reviewer/grouping
is asserted because no YES verdict was selected.

## Phase8 — verification and handoff

Three accepted native batches: original fullmodule replay with canonical audit; isolated
mathlib-only proofs; full2module caller replay. All successful, complete/nonpartial where
that field exists, no warnings/errors, no sorry/new axiom/unsafe/native_decide/resource raises,
standard axioms only. Raw run_code diagnostics have no partial field, which is not an error.
Exact complete requests/results, elapsed_ms and sources are preserved. Three rejected isolated
attempts are separately retained; recovered sorryAx belongs only to rejected receipts.
Preparation width failures were corrected before execution, never treated as native success.

'''+link('verification.json')+'; '+link('assessment.json')+'; '+link('overview-entry.json')+'; '+link('validate.py')+'; '+link('validation-result.json')+'; '+link('secret-guard.json')+'; '+link('copy-manifest.json')+'''.
The portable read-only validator checks current artifact hashes/bytes, links, fresh input
hashes, exact293 order/uniqueness and runtime presence/value counts, required metadata,
all phases,15formal cells, web channel metadata, exact executed sources and clean native
receipts/axioms. It is actually run both in scratch and in a simulated integrated layout
with the report outside the evidence directory. Historical worker manifests never replace
current manifest validation. Root review/acceptance is independent and pending.
'''
for key,name in [('WEB1','web-general1.json'),('WEB2','web-general2.json'),('WEB3','web-general3.json'),('LOCAL','literature-local-excerpt.txt'),('NLAB','web-nlab.json'),('NCAT','web-ncatlab.json'),('STACKS','web-stacks.json'),('MO','web-mathoverflow.json'),('ARXIV','web-arxiv.json'),('PRIMARY','web-primary.json')]:s=s.replace('| '+key+' |','| '+link(name)+' |')
(D/'report.md').write_text(s)
print('Report written:',len(s.splitlines()),'lines')
