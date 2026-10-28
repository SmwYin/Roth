from pathlib import Path
import json
D=Path(__file__).resolve().parent
rd=lambda n:json.loads((D/n).read_text())
link=lambda f:'[evidence](../evidence/Roth.mainCoeffBound/'+f+')'
s='''# Roth.mainCoeffBound — canonical 232

**Verdict: NO-composable-from-mathlib.** The exact natural cutoff is a construction from
`Nat.floor`, `Real.rpow`, and multiplication. It has a useful local semantic name, but does
not supply new rounding machinery or a new mathematical operation for mathlib. This verdict
is independently established here, not inherited from the neighboring scalar parameters.

## Phase 0 — Baseline and scope

PASS. `Roth/MainLemma.lean:69`, public noncomputable definition. Fresh hashes of all17
production source/pin inputs match the shared manifest and its successful2467-job baseline.
The prior accepted file-end228 build remains applicable; this is not a file endpoint
(next266). Production files, pins, Git and progress are unchanged. Full MainLemma and Main,
all eight actual caller proofs, and the earlier generic floor helpers were read.

'''+link('inputs.json')+' '+link('baseline-build.txt')+' '+link('target-metadata.json')+'''

## Phase 1 — Mathematical content and kernel type

For a real δ and natural denominator q₁ and degree r₁, choose
B₁ = ⌊(q₁:ℝ)^(δ(r₁:ℝ))⌋₊ as a natural number. The intended main-lemma regime makes this
large, but the definition is total and carries no positivity premises. The construction is
real exponentiation followed by natural floor; it has no project body dependencies.

Full elaborated type: `ℝ → ℕ → ℕ → ℕ`.
Binder form: `(δ : ℝ) → (q₁ r₁ : ℕ) → ℕ`. Universe parameters: `[]`.
The full kernel body/type printer and tagged `Lean.getConstInfo` type are archived without
printer elision. Standard axioms only: propext, Classical.choice, Quot.sound.

'''+link('native-type.json')+' '+link('original-executed.lean.txt')+' '+link('original-receipt.json')+'''

## Phase 2 — Size and one-line definition

SMALL: a numerical cutoff in the auxiliary construction, not a new structure or the main
existence theorem. One substantive body line: ONE-LINER WITH-EXEMPTION.

| Exemption | Applies? | Evidence |
|---|---|---|
| Avoid defeq abuse | No | rfl bridge and full inlining compile without a sealed boundary. |
| Avoid typeclass diamonds | No | A function into ℕ creates no instance or new carrier. |
| Semantic intent / API stability | Yes locally | three_small_factors and main_lemma share the chosen integer cutoff; Main uses its same derivative scale. |

Semantic usefulness is not a proof of new upstream content. The independent strict3
construction below settles the contribution question while allowing local notation.

## Phase 3 — Exhaustive literature

Every named channel was actually attempted. Optional ask_chatgpt_math is unavailable; it is
the only skipped optional channel. Search receipts store exact requests, UTF8 returned-response
SHA256/bytes/status, clean titles/URLs and original summaries; no article or result bodies.

| Channel | Actual query / locator | Result |
|---|---|---|
| General web, specific | Roth theorem auxiliary polynomial coefficient bound "floor" q delta | Related polynomial height sources; no distinct named operation. |
| General web, general | greatest integer floor function nonnegative integer coefficient interval counting | Greatest-integer/floor characterization; applies here to nonnegative real powers. |
| General web, alias | Roth Lemma 9 "B_1" coefficient bound | Princeton seminar notes Lemma18.3.1 and coefficient arrays. |
| Local clean.tex | §6 eq(roth:eq37), lines1356–1360; following floor paragraph and Lean note | Exact B₁ choice. Both strict √X lower bound and non-strict B₁≤X explicitly required. |
| nLab | site:ncatlab.org/nlab floor function Galois connection | Floor as greatest integer and right adjoint to inclusion. |
| nCatLab distinct | site:ncatlab.org/ncatlab floor natural integer adjoint | Returned /nlab pages outside requested namespace; no exact /ncatlab hit. |
| Stacks | site:stacks.math.columbia.edu floor integer polynomial coefficient bound | Different algebraic/polynomial material; no exact cutoff API. |
| MathOverflow | site:mathoverflow.net Roth auxiliary polynomial coefficient bound floor | Related quantitative Roth and coefficient questions; no exact named parameter. |
| Recent arXiv | site:arxiv.org Roth theorem auxiliary polynomial height floor after:2021-10-28 before:2026-10-29 | Additive Roth homonyms and unrelated polynomial papers. |
| Recent arXiv refined | site:arxiv.org "Roth" "Diophantine" auxiliary polynomial after:2021-10-28 before:2026-10-29 | Diophantine applications, including2209.09182; no exact cutoff counterpart. |
| Supplementary primary | Princeton Diophantine seminar PDF pp158–159, Lemma18.3.1, eq18.12 | Integer coefficients in [0,B₁], family count (B₁+1)^r. Does not independently certify exact floor formula. |
| Supplementary API web | official mathlib floor/rpow documentation query | Existing FloorSemiring/Nat.floor organization, verified at the pin. |

'''
for f in ['web-general.json','literature-source.json','local-literature.json','local-excerpt.tex.txt','nlab.json','ncatlab.json','stacks.json','mathoverflow.json','arxiv.json','primary.json','primary-floor.json','web-api.json']:s+=link(f)+' '
s+='''

Concept: natural floor of a nonnegative real power, serving as a proof-specific coefficient
cutoff. Local eq37 is precise. General sources agree on floor semantics; they do not establish
an independent named B₁ operation across mathematical areas. Classical integer floor and
Nat.floor agree on these nonnegative inputs. nLab's adjoint account uses integer inclusion;
mathlib's `Nat.le_floor_iff` has the necessary nonnegative-domain condition. No global
absence inference is drawn from failed or unrelated searches.

Primary locators: [Princeton seminar notes](https://web.math.princeton.edu/mathlab/jr02/diophantine.pdf),
[nLab floors](https://ncatlab.org/nlab/show/floor),
[official floor API](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Floor/Defs.html).
These support the floor/counting roles, not a claim of new upstream nomenclature.

## Phase 4a — Generality comparison

| Parameter / condition | Current | Comparison and verified result |
|---|---|---|
| δ | arbitrary ℝ | No δ≥0 premise to drop. Negative δ matters: q>1 and r>0 gives B₁=0. |
| q₁ | ℕ | Natural denominator in the parent interface. floorPower(q,e) with real q compiles; endpoint law requires q≥0. This expands the representation, not a needed hypothesis weakening. |
| r₁ | ℕ | Natural degree; δr₁ is already a real exponent. A separate real exponent e is verified, with exact specialization. |
| output | ℕ | Needed by boxFamily and coefficient interval counts. Raw real power is not a type-preserving replacement. |
| sign / nonzero assumptions | None | Total Real.rpow and natural floor conventions already cover endpoints. |
| floor infrastructure | concrete ℝ | Generic floor order characterization compiles for arbitrary `[Semiring K] [PartialOrder K] [FloorSemiring K]`; already Nat.le_floor_iff. |

## Phase 4b — Generality verdict

MAXIMALLY GENERAL for the fixed chosen-denominator/degree interface: no mechanical hypothesis
drop exists. `floorPower (q e : ℝ) : ℕ := ⌊q^e⌋₊` is an expanded representation, not a new
existing mathlib definition or a verified novel standard weakening. The generic floor order
law is existing infrastructure. No generalise-first conclusion is justified.

Boundary tests compile in mathlib-only context: δ=0 or r=0 gives1 for every q, including q=0;
q=1 gives1; q=0 gives1 iff δr=0 and0 otherwise (even for negative exponent); for q>1,r>0,δ<0,
the cutoff is0. δ=1 gives q^r. Integer powers exhibit equality in B₁≤X, ruling out a strict
upper bound. The raw real power is nonnegative for every allowed natural base.

'''+link('isolated-executed.lean.txt')+' '+link('isolated-receipt.json')+'''

## Phase 4c — Modern idiom, all nine questions

| # | Question | Assessment and downstream consequence |
|---|---|---|
| 1 | Typeclass preambles | No new preamble to convert; existing FloorSemiring supplies rounding. |
| 2 | Sequences → filters | No sequence or limit in this definition. Floor has jumps; no global continuity claim. |
| 3 | Construction → universal property | Floor already has gc_floor/Nat.le_floor_iff characterization, verified generically; no new class needed. |
| 4 | Set → bundled substructure | Output is a natural, not a subset with closure data. |
| 5 | Algebra hierarchy weakening | Real.rpow needs its real semantics; floor alone already abstracts over FloorSemiring. |
| 6 | Higher categories | No categorical construction to improve; adjunction perspective is already order API. |
| 7 | Concrete index | q,r are denominator/degree naturals. Real q,e representation compiles; counting still needs a natural cutoff. |
| 8 | Concrete-via-abstract body diagnostic | Body contains no separate named mathematical witness after excluding its declaration name; it is exactly floor(power(cast q,δ*cast r)). Abstract x↦⌊x⌋₊ is existing Nat.floor. This is construction evidence, not a hidden new theorem. |
| 9 | False-generalization guard | Reject replacing natural floor with raw real power, ceil, or globally continuous profile. Integer coefficient transport needs a proved bridge and nonnegative X; the exact floor endpoint matters. |

Modern idiom available as existing infrastructure, with no new modernization contribution:
Nat.floor and its order law are already canonical. The orientation is cast ⊣ floor on the nonnegative domain; the original abstract LeanSearch query incorrectly said lower adjoint. A corrected supplementary semantic query is archived separately, preserving the historical request. For an integer z and X≥0 the exact bridge
`|z| ≤ (⌊X⌋₊:ℤ) ↔ |(z:ℝ)| ≤ X` compiles. It permits rewriting coefficient inequalities,
but does not make real X an argument to natural boxFamily or justify dropping floor from counts.
This bridge is a new scratch verification proof using Int.natCast_floor_eq_floor/Int.le_floor,
not an existing named theorem asserted to be in mathlib.

## Phase 4.5 — Infrastructure risk

| Risk | Rating | Evidence |
|---|---|---|
| Typeclass diamond | None | The declaration is data in ℕ, registers no instance. FloorRing ℝ and its derived FloorSemiring synthesize canonically. |
| Reducibility leak | Low | Ordinary noncomputable def, no reducible attribute. rfl unfolds it; no recursive computation exposed. |
| Noncanonical unfolding | Low | Full actual caller replay works with explicit floor; endpoint casts remain explicit. |
| Instance priorities | None | No instance declaration or priority introduced. |
| Universe issues | None | Native levelParams=[]; values are fixed ℝ/ℕ. Generic FloorSemiring scratch law is universe-polymorphic. |
| Coercion ambiguity | Low | NatCast ℝ synthesizes as Real.instNatCast; no CoeFun/CoeSort introduced. Direct Coe ℕ ℝ synthesis was a rejected probe, corrected to NatCast. |

Overall LOW. No HIGH rows or special infrastructure exemption. Accepted sources have no warnings.

## Phase 4.6 — Proof strategy

| # | Strategy question | Assessment |
|---|---|---|
| 1 | ε-δ versus filters | n/a: numeric definition, no topology proof. |
| 2 | Elements versus substructures | n/a: no algebraic inclusion proof. |
| 3 | Sequences versus nets | n/a: no convergence argument. |
| 4 | Explicit object versus universal property | Existing floor characterization already available; defining it again is unnecessary. |
| 5 | Missing helpers mathlib should have | None needed to construct B₁. sqrt_lt_floor is a separate project theorem and has no inherited verdict here. |

MATHLIB-IDIOMATIC construction. The project sqrtBound check uses Roth.sqrt_lt_floor and is
explicitly project companion evidence. The isolated sqrtLower is a new reproduction from floor,
sqrt and order tools; neither is counted among the strict3 definition-building operations.

## Phase 5 — All fifteen formal search cells

External indexes are not the pinned checkout. Local searches returned index=error, so their
empty/partial responses do not prove absence. All positive building blocks were checked
natively at the pin; exhaustive rg receipts are untruncated.

| Form | Lean-Finder | Loogle | LeanSearch | rg | local search |
|---|---|---|---|---|---|
| Current floor power | Roth-number arithmetic-progression homonyms (rejected) | Exact floor(power product) pattern: no hit | Nat.floor and natural-power floor bounds | mainCoeffBound/floor-rpow: no exact name | target local name only, index error |
| Standard floor | Nat.floor_le, floor_eq_iff, Int floor bridge | Loose pattern returned floor-power asymptotic bounds, not target | Nat.floor_eq_iff | Floor.Semiring endpoints | floor_le variants, index error |
| Abstract order | FloorSemiring.gc_floor, Nat.le_floor_iff | Nat.le_floor, floor_mono, partial matches | Nat.floor, FloorSemiring.floor/gc_floor | Floor.Defs generic law | le_floor variants, index error |

'''
for form in ['current','standard','abstract']:
 for m in ['leanfinder','loogle','leansearch','rg','local_search']:s+=link('search-'+form+'-'+m+'.json')+' '
s+='''

Conclusion: existing building blocks `Nat.floor`, `Real.rpow`, multiplication give the exact
construction. Nat.floor alone is not asserted as an identical three-argument mathlib object,
so the verdict is composable, not exact has-it. `mul_pow_le_nat_floor_pow` deals with natural
exponent asymptotics; arithmetic-progression Roth numbers and Nat.floorRoot are different.
No new theorem is being proposed on an absence claim, so no broad exact? search is necessary.

Pinned locations: Floor/Defs.lean:117 (Nat.floor), :138 (le_floor_iff),
Floor/Semiring.lean:47 (floor_le), :63 (lt_floor_add_one), :112 (floor_pos),
Pow/Real.lean:35 (rpow), :129 (zero_rpow), :666 (negative-exponent bound).
'''+link('mathlib-inputs.json')+' '+link('search-abstract-leansearch-corrected.json')+' '+link('root-primary-crosscheck.json')+'''

## Phase 5.5 — Statement shape

| Check | Finding |
|---|---|
| Canonical normal form | ⌊(q:ℝ)^(δ*r)⌋₊; integer floor cast is equivalent only with nonnegative input. This nonnegativity holds here. rfl bridge puts explicit mathlib normal form on RHS. |
| Syntactic generality | Tested explicit Nat.floor(Real.rpow q (δ*r)), real-base floorPower(q,e), and integral coefficient interval equivalence. Keep explicit natural floor at counting sites and current casts in real inequalities. |
| Superfluous arguments | δ,q,r all occur essentially in the formula; no typeclass/hypothesis to drop. Zero/special values do not make a parameter globally unused. |

SHIP-AS-STATED as local notation; upstream standalone name unnecessary. Do not restate natural
counting parameters as real numbers. No orthogonal equivalence web or typeclass widening needed.

## Phase 6.0 — Full actual caller audit

Eight distinct lexical callers,21 executable occurrences: six declarations in MainLemma and
two in Main (four external-to-file occurrences in one file). Documentation and the target
are excluded. Signatures and proof bodies are counted separately below. Fresh scoped rg and
tracked git grep cross-check production enumeration despite ignore rules.

| Caller | Occurrences (signature/body) | Role and exact refactor |
|---|---|---|
'''
for c in rd('callers.json')['callers']:
 n=c['name'].removeprefix('Roth.');roles={'mul_log_div_two_lt_log_mainCoeffBound':'Log lower bound; expand floor in conclusion and remove target from simp list.','three_small_factors':'Three factor bounds; replace all type/local real casts by casts of explicit floor.','exists_mem_RSet_le_index_of_log_bound_aux':'Natural B fed to counting helper; preserve Nat floor in RSet and B argument.','exists_auxiliary_polynomial_of_log_bound_aux':'Local natural B and derivative scale; preserve local let B as floor.','exists_auxiliary_polynomial_with_index_gap_aux':'Derivative bound in statement; replace its Nat floor cast.','main_lemma':'Public derivative conclusion; keep same natural floor under real cast.','one_lt_roth_eval_bound_aux':'Taylor/evaluation contradiction bound; inline floor under real cast.','roth_product_bound_aux':'Positivity, upper endpoint and product loss; preserve floor in all three statements.'}
 s+='| `'+c['file']+':'+str(c['line'])+' '+n+'` | '+str(c['occurrences'])+' ('+str(c['signature_occurrences'])+'/'+str(c['body_occurrences'])+') | '+roles[n]+' |\n'
s+='''

'''+link('callers.json')+' '+link('source-search.json')+' '+link('tracked-source-search.json')+'''

Inline-derivation audit: `Cn := ⌊(B:ℝ)^c⌋₊` in the generic rpow-bound helper,
`pigeonhole_count` and its floor_rpow_count_lt_aux use related floor-power expressions. They
are different coefficient/remainder cutoffs, not independent reproofs of the exact δ,q,r name.
The earlier sqrt_lt_floor handles generic X already; no separate B₁ floor engine is missing.

Pairwise duplication check:

| Pair | Same statement? | Same proof? | Result |
|---|---|---|---|
| mainCoeffBound / local Cn | Same floor-power pattern at different parameters | Both direct floor constructions | Share existing Nat.floor; no new generic wrapper required. |
| mainCoeffBound / sqrt_lt_floor | No: data choice versus generic inequality | No | Apply earlier generic estimate; do not inherit a verdict for it. |
| mainCoeffBound / pigeonhole_count | No: natural cutoff versus strict count inequality | No | Keep counting theorem separately assessable. |
| mainCoeffBound / eta,lam,gam | No: natural floor versus real numerical profiles | No | Independent assessment; no continuity or verdict transfer. |

'''+link('inline-audit.json')+'''

The exact canonical293 array is derived from tracked order with private module names intact;
pre-execution source gate and runtime all293 unique/present/values pass. Direct kernel types
contain B₁ in8 declarations; direct kernel values in9, with extra `roth_of_isIntegral`. This
is neither transitive kernel closure nor the simp dependency closure. Full original MainLemma
replay preserves body/source semantics. Full two-module actual written proofs then inline B₁,
replaying all8 actual caller signatures checked by `Lean.Meta.isDefEq`; the final integral
Roth theorem also replays. Existing imported project theorems remain accessible; no claim that
the whole transitive environment is target-free. This is stronger than a synthetic consumer,
without pretending to remove every original import.

'''+link('inline-executed.lean.txt')+' '+link('inline-receipt.json')+'''

## Phase 6 — Composition experiments

1. Strict direct construction, PASS:

```lean
Nat.floor (Real.rpow (q : ℝ) (δ * (r : ℝ)))
```

Three existing mathematical operations: natural floor, real exponentiation, multiplication.
The two standard casts are explicitly retained. This count is not a claim of three kernel
constants including all dictionary/coercion applications. The project equality is `rfl` and
mathlib-only construction elaborates with `#check_failure Roth.mainCoeffBound`.

2. Generic floor order characterization, PASS: `Nat.le_floor_iff hx` works on arbitrary
FloorSemiring. Existing one-call theorem, not a new result about the chosen parameter.
3. Both real endpoints, PASS: `⟨Nat.floor_le (Real.rpow_nonneg hq e), Nat.lt_floor_add_one _⟩`.
4. Integral coefficient bridge, PASS, new scratch proof using three rewrites. It is not
needed to justify direct construction and not mislabeled as an existing named law.
5. sqrt lower bound, PASS, new scratch proof reproducing the earlier project floor estimate;
not a ≤3-call theorem composition and not evidence to downgrade that theorem.
6. Full actual caller proof inlining, PASS with all8 original signatures and both modules.

COMPOSABLE for the definition itself. No closing simp/ring/aesop argument is used to claim
strict composability of the defining expression. Separate boundary lemmas naturally use simp;
their proofs are not the criterion for this definition's verdict.

'''+link('project-executed.lean.txt')+' '+link('project-receipt.json')+'''

## Phase 7 — Verdict and actionable destination

**NO-composable-from-mathlib.** Floor/rpow/mul already construct exactly the desired value.
The semantic-name exemption is genuine in this project, but the mathematical role is the
specific B₁ choice in Roth's proof; the general rounding object is already Nat.floor. The
complete proof replays show the name is mechanically removable while preserving its natural
interface and all caller signatures. This is not a cost-based judgment or an inference that
the parent main lemma is unimportant.

For an upstream cleanup, delete the standalone wrapper and perform each of the eight exact
replacements in the caller table; retain the floor and all natural/integer/real casts. In
mul_log_div_two_lt_log_mainCoeffBound remove only mainCoeffBound from the simp list. Keep the
local `let B` where it clarifies counting. The two-module inlining script supplies the concrete
reviewable refactor template. Rename the surviving log theorem only in a future actual cleanup
if its name should cease referring to the removed wrapper.

Alternative destination: leave a documented project-local definition or scoped notation at
Roth/MainLemma.lean:69 as useful numerical notation for eq37. The overview makes no production
edit. There is no proposed new mathlib file/PR/reviewer because this is a NO verdict; earlier
accepted YES contributions need no grouping with this redundant construction.

## Phase 8 — Verification and limitations

All phases PASS, unresolved=[], completed=true; root acceptance pending. Four accepted native
receipts (original, isolated, inline, project) are full successes, no warnings/errors/sorryAx,
no raised resource limits or unsafe/native_decide/new axioms. The original cold partial response
is separately labeled warming. Five rejected native attempts remain exact: orphan docstring,
three failed natural-exponent proof spellings, and incorrect direct Coe-class synthesis. None
supports the verdict; the corrected accepted sources do. Initial metadata serialization failures
wrote no article bodies; final metadata uses exact response hashes.

The portable read-only validator checks the current copy manifest, source/pin and mathlib hashes,
exact canonical array order/private names/runtime counts, all15 search cells, caller slices,
original-signature markers, standard axioms and accepted diagnostics. It supports scratch or
integrated evidence layout. Secret guard and validator must pass before frozen release.

'''+link('verification.json')+' '+link('assessment.json')+' '+link('validate.py')+' '+link('copy-manifest.json')+'\n'
s='\n'.join(l.rstrip() for l in s.splitlines())+'\n'
(D/'report.md').write_text(s)
print('Report written',len(s),'characters')
