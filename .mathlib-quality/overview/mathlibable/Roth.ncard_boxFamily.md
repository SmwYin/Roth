# `Roth.ncard_boxFamily` — canonical246

**BORDERLINE-needs-human.** The formula is correct and useful, including arbitrary variable types
with finitely supported degree bounds. Existing mathlib counts the enumerated coefficient arrays;
the semantic polynomial bridge is new/project proof. A verified closing simp composition follows
the Phase6b BORDERLINE rule, not an automatic NO. This is a completed assessment with no
verification blocker; the three questions below concern future upstream API design.

## Phase 0 — baseline and scope

Public theorem, `Roth/MainLemma.lean:311–318`, seven proof lines, no sorry. The whole module and its
sole complete caller were read. The module proves Roth's main lemma by bounded coefficient
counting, pigeonhole, and Hasse derivative selection. The tracked frontier is246: all245 earlier
entries are accepted and246 is absent from completed declarations. All17 source/pin hashes freshly
match the successful2467-job baseline. No production/pin/Git/overview/progress file was changed.

[Inputs](../evidence/Roth.ncard_boxFamily/inputs.json),
[baseline](../evidence/Roth.ncard_boxFamily/baseline-build.txt),
[frontier snapshot](../evidence/Roth.ncard_boxFamily/accepted-verdict-snapshot.json),
[canonical order](../evidence/Roth.ncard_boxFamily/canonical-snapshot.json).
Full original-module replay and exact canonical293 requested/unique/present/kernel-values audit
passed. File-end Theta228 build is previously accepted; no new file-end build is due until266.
Nine persistent imports remain exact. Isolated prefix started with shared18; missing genuine
Finsupp interval API required adding only `Mathlib.Data.Finsupp.Interval`, whose pinned header
imports `Mathlib.Data.Finset.Finsupp`. Final active19 is stable; shared18 file unchanged.
Root independently accepted the exact added-import scope after execution, not as prior root
authorization: [chronology/scope note](../evidence/Roth.ncard_boxFamily/root-prefix-scope-note.json).

## Phase 1 — mathematical content and exact native type

The admissible exponent vectors form a finite rectangular box, with
`N = ∏ᶠ j, (r j + 1)` monomials. Every such monomial independently receives an integer coefficient
from0 throughB, giving `(B+1)^N` distinct polynomials. The exponent box count and coefficient
assignment count are separate layers; the zero polynomial is included.

```lean
∀ {σ : Type u_1} (r : σ → ℕ) [Finite ↑(Function.support r)] (B : ℕ),
  (Roth.boxFamily r B).ncard = (B + 1) ^ ∏ᶠ (j : σ), (r j + 1)
```

σ is an arbitrary variable type; r supplies each natural degree bound, B the natural coefficient
bound. The only structural premise is finiteness of the support of r; no positivity, Nonempty σ,
Finite σ or Fintype σ premise is needed. Native `Lean.getConstInfo`, with `pp.funBinderTypes`,
captures the type without splitting an internal let at `:=`.
The proof identifies the family with an injective `ofCoeff` image of `Finset.finsupp`, counts
choices using `Finset.card_finsupp`, counts exponent vectors using `Finsupp.card_Iic` and
`Nat.card_Iic`, and transports the finite support product to `finprod`.

Canonical project dependencies, including both scopes: **type:** `Roth.boxFamily`;
**body:** `Roth.boxFamily` and `Roth.boxFamily_eq_image_finsupp_aux`.
The latter's exact kernel name is
`_private.Roth.MainLemma.0.Roth.boxFamily_eq_image_finsupp_aux`.
[Native type/dependencies](../evidence/Roth.ncard_boxFamily/native-type.json),
[original source](../evidence/Roth.ncard_boxFamily/original-executed.lean.txt),
[original receipt](../evidence/Roth.ncard_boxFamily/original-receipt.json),
[compact kernel body receipt](../evidence/Roth.ncard_boxFamily/project-receipt.json).
The `pp.all` printer elided80823 characters: it is **not a full kernel-body dump**. The compact
body is complete and unelided; exact complete executed Lean source is separately preserved.

## Phase 2 — preliminary checks

**BIG**, because the module explicitly lists `ncard_boxFamily` under Main results (pigeonhole
step). Its arithmetic spelling alone would not justify SMALL. Exhaustive search runs regardless.
Definition-only one-line check: **n/a, theorem**. It defines neither data nor an instance;
definition exemptions do not classify this seven-line proof.

## Phase 3 — exhaustive literature

Exact requests, returned-response hashes/bytes/status and concise original summaries are archived;
no full web/article/search bodies are retained.

| Channel | Executed query / locator | Finding / limitation |
|---|---|---|
| General specific | integer multivariate polynomials coordinate degree bounds coefficients 0 B number (B+1) | Coefficient-array count; exact local Roth formula below. |
| General standard | count functions finite coordinate choices product cardinalities finite support | Finite product / function count. |
| General aliases | auxiliary polynomial Roth Siegel lemma counting monomials coefficient box | Roth/Siegel coefficient boxes, distinct from symmetric height boxes. |
| ChatGPT math | Optional ask_chatgpt_math | Justified n/a: unavailable; no response invented. |
| Local reference | clean.tex §6 Lemma9 proof, lines1405–1421, eq43 | Exact `(B₁+1)^r`, `r=∏(r_j+1)`. |
| nLab | site:ncatlab.org/nlab cardinality cartesian product finite sets | Cardinal arithmetic/cartesian product conceptual support; direct page fetch fails unsupported XHTML. |
| nCatLab distinct | site:ncatlab.org/ncatlab finite sets cardinality product | Actual distinct namespace query returned out-of-namespace nLab items, no exact hit; not absence evidence. |
| Stacks | site:stacks.math.columbia.edu polynomial monomials basis; corrective query with polynomial ring / monomials / basis | §15.31 (062D) uses monomial basis; adjacent algebra, not this count. An unrelated tag00E8 lookup was excluded. |
| MathOverflow | site:mathoverflow.net polynomials bounded coefficients counting | Small-coefficient reconstruction question404760 is related, not this law or an exact generalization. |
| Recent arXiv | site:arxiv.org auxiliary polynomials bounded coefficients counting monomials after:2021-10-29 before:2026-10-30 | 2409.08625 (submitted2024-09-13) counts bounded-height univariate polynomials with root restrictions; adjacent, not replacement. Other returned topics irrelevant. |

[General queries](../evidence/Roth.ncard_boxFamily/web-general.json),
[named channels](../evidence/Roth.ncard_boxFamily/web-channels.json),
[recent arXiv](../evidence/Roth.ncard_boxFamily/web-recent.json),
[primary opens and access limitations](../evidence/Roth.ncard_boxFamily/web-primary.json),
[corrective lookup and precise Mayr locator](../evidence/Roth.ncard_boxFamily/web-correction.json),
[local excerpt](../evidence/Roth.ncard_boxFamily/local-excerpt.tex.txt),
[local source hash](../evidence/Roth.ncard_boxFamily/literature-source.json).

Standard concept: independent finite coefficient choices on finitely many monomials.
[Mayr, Discrete Mathematics, slide64, PDF pages71–72](https://homepages.inf.ed.ac.uk/rmayr/Ch2.pdf)
gives the finite-function cardinality law. The local paper specializes it to rectangular exponents.
The broader form allows arbitrary finite monomial sets and coordinate-dependent finite choices.
[Dubickas–Sha,2024](https://arxiv.org/abs/2409.08625) is recent counting context only. No historical
reformulation was independently established; primary evidence is the finite-choice law and local
formula. No exact universal name for this Roth-specific interface was established.

## Phase 4a — every parameter and semantic generality

| Parameter / premise | Current form | Assessment / verified alternative |
|---|---|---|
| σ | arbitrary `Type u_1` | Already arbitrary; restricting to Fintype σ loses the infinite-variable finite-support case. |
| r | `σ → ℕ` | Coordinate degree bounds are natural; `r : σ →₀ ℕ` bundles finite support without changing the object. |
| Finite support | `Finite (Function.support r)` | Essential for the general count. A fresh infinite `X i` family refutes wholesale removal. |
| B | arbitrary natural bound, including0 | No positivity needed. Fixed `[0,B]` parent representation means replacing B by a field scalar is not a mechanical weakening. |
| Coefficients | integers in `[0,B]` | New verified general semantic family over `CommSemiring R`, coordinate-dependent finite coefficient choices. |
| RHS / cardinal | natural power, finprod | Count stays natural. `finprod` of infinitely many nonunit factors is totalized1, not an infinite cardinal. |

## Phase 4b — verified generality verdict and edge cases

Within the supplied parent `boxFamily` interface, σ, r and B identify the counted family. The uniform
finite-support formulation covers every natural B; removing support wholesale is refuted, while
the B=0 exception is separately verified. No full support/B iff criterion or mechanical Int
typeclass weakening is claimed.
A meaningful broader semantic statement was proved independently, rather than merely posited:

```lean
open scoped Classical in
theorem ncard_family {σ R : Type*} [CommSemiring R] (r : σ →₀ ℕ)
    (t : (σ →₀ ℕ) → Finset R) (ht : ∀ d ∉ Finset.Iic r, 0 ∈ t d) :
    {P : MvPolynomial σ R | (∀ j, degreeOf j P ≤ r j) ∧ ∀ d, P.coeff d ∈ t d}.ncard =
      ∏ d ∈ Finset.Iic r, (t d).card
```

This is the expanded signature of the accepted scratch `Box246Generic.ncard_family`.
Only off-box choices must contain0. Inside-box choices may exclude0 or be empty; the product
still counts correctly. Dropping off-box compatibility can make the semantic family empty while
the displayed product is positive. Constant choices give `t.card ^ ∏ j ∈ r.support, (r j+1)`.
The representation proof is **new assessment code**, not a previously existing mathlib theorem.

[Mathlib-only source](../evidence/Roth.ncard_boxFamily/isolated-executed.lean.txt),
[clean raw native receipt](../evidence/Roth.ncard_boxFamily/isolated-receipt.json).
Original r/function/finite-support/finprod form is recovered in `Box246Project.ncard_original`;
its entire supplied signature agrees by `rfl` (proof irrelevance after identical propositions).
This is parent-interface redesign plus a proved bridge, not one mechanical assumption edit;
it therefore does not force YES-but-generalise-first.

Actual clean native edge tests in [project source](../evidence/Roth.ncard_boxFamily/project-executed.lean.txt)
and [receipt](../evidence/Roth.ncard_boxFamily/project-receipt.json):

| Case | Verified result |
|---|---|
| B=0, arbitrary r without support premise | Family is `{0}`, ncard1, formula still holds. This exceptional case does not extend the full theorem to arbitrary support. |
| r=0, arbitrary σ | Only constant coefficients vary; ncard=B+1. |
| σ=Empty | One constant monomial remains; ncard=B+1, not1. |
| σ=ℕ, r=`Finsupp.single 0 2` | Infinite ambient variables, three admissible monomials; ncard=(B+1)^3. |
| σ=ℕ, r≡1, B=1 | Injective family `X i` is infinite, so Set.ncard=0; finprod of constant2 is1, RHS=2. The equality is formally refuted. |

## Phase 4c — modern idiom, all nine rows

| # | Question | Applies / concrete consequence |
|---|---|---|
| 1 | Typeclasses instead of hypotheses | Already uses `Finite (Function.support r)`; no new family typeclass needed. |
| 2 | Filters instead of sequences | No: finite combinatorics has no topology. |
| 3 | Universal property instead of construction | No new universal-property class: explicit finite coefficient choices are exactly the counting data. |
| 4 | Bundled substructure | No submodule: `[0,B]` coefficients are not closed under addition. Finsupp-bundled r usefully packages finite support and interval API. |
| 5 | Algebra hierarchy | Yes: semantic counting works over arbitrary CommSemiring R; multiplication/ordering on coefficients is not used in finite choices. Unlocks finite-field/semiring choices. |
| 6 | Higher categories | No: cardinality identity has no relevant categorical structure requiring higher generalization. |
| 7 | Concrete index generalization | σ already arbitrary; exponent naturals encode monomial degrees. Natural arithmetic constants express cardinalities, not redundant scalar choices. |
| 8 | Concrete-via-abstract diagnostic | Yes: `boxFamily` disappears after the initial image rewrite (0 subsequent body occurrences); counting works on abstract coefficient arrays. Arbitrary semantic choices were actually proved and original recovered. |
| 9 | False-generalization guard | Reject Fintype σ restriction and arbitrary-support finprod interpretation. Retain off-box0 compatibility; do not confuse monomial count with polynomial count. The verified generic semantic family preserves the original on specialization. |

Modern idiom available: finite coefficient-choice family with explicit Finsupp support. It composes
with `Finset.finsupp`, `Finset.card_finsupp`, finite intervals and injective image cardinality;
coordinate-dependent choices handle more than uniform integer intervals. No new bundled
substructure/instance is proposed. Whether to publish a semantic count or keep an enumerated
interface is the actual upstream decision, not a cost judgment.

## Phase 4.5 — six infrastructure risk rows

| Risk | Verdict / justification |
|---|---|
| Typeclass diamond | n/a: theorem introduces no instance paths or new carrier. |
| Reducibility leak | n/a: proof declaration, no data reducibility attribute. |
| Non-canonical unfolding | n/a: introduces no new data definitional equality; rewrites are explicit. |
| Instance priority collision | n/a: registers no instance or priority. |
| Universe-polymorphism issues | n/a: proof retains arbitrary σ universe; no new data universe choice. |
| Coercion ambiguity | n/a: registers no CoeFun/CoeSort/other coercion. |

Overall n/a, theorem. Scratch family definitions are probes, not production infrastructure proposals.

## Phase 4.6 — proof strategy, all five rows

| # | Question | Applies / verdict |
|---|---|---|
| 1 | Topology ε–δ versus filters | n/a: finite count. |
| 2 | Element algebra versus substructures | No substructure proof: boxes are not additive submodules; coefficient representation/injectivity is the useful abstraction. |
| 3 | Analysis sequences versus nets | n/a: no limits. |
| 4 | Category construction versus universal property | n/a: enumeration, not a categorical universal object. |
| 5 | Missing helper mathlib should have | Potential semantic degree/coefficient-family representation/count API; new generic proof verifies the gap's shape. Existing `card_finsupp` already counts enumerated arrays. |

MATHLIB-IDIOMATIC once the representation is fixed. Semantic API packaging could simplify multiple
box lemmas, but shortness after a project helper is not a pure existing-mathlib composition.

## Phase 5 — all15 actual formal search cells

| Form | Method | Exact query / pattern | Result / raw receipt |
|---|---|---|---|
| current | leanfinder | `number of integer multivariate polynomials with individual degree bounds and coefficients between zero and B` | Polynomial.card_eq_of_natDegree_le_of_coeff_le, ChevalleyThm.MvPolynomialC.numBound, ChevalleyThm.numBound. [receipt](../evidence/Roth.ncard_boxFamily/search-current-leanfinder.json) |
| current | loogle | `MvPolynomial.degreeOf, Set.ncard` | No hit. [receipt](../evidence/Roth.ncard_boxFamily/search-current-loogle.json) |
| current | leansearch | `cardinality of multivariate polynomials with degree bound in each variable and bounded natural integer coefficients` | Polynomial.card_eq_of_natDegree_le_of_coeff_le, MvPolynomial.cardinalMk_le_max, MvPolynomial.cardinalMk_le_max_lift. [receipt](../evidence/Roth.ncard_boxFamily/search-current-leansearch.json) |
| current | rg | `ncard_boxFamily∣card.*(degree∣coeff)∣card_eq_of_natDegree_le∣degreeOf_le_iff` | Pinned source hits; see receipt. [receipt](../evidence/Roth.ncard_boxFamily/search-current-rg.json) |
| current | local_search | `ncard_boxFamily` | Roth.ncard_boxFamily; index:error. [receipt](../evidence/Roth.ncard_boxFamily/search-current-local_search.json) |
| standard | leanfinder | `cardinality finite support functions with finite coordinate value choices product of cardinalities` | Finset.card_finsupp, Finset.card_dfinsupp, Finsupp.card_pi. [receipt](../evidence/Roth.ncard_boxFamily/search-standard-leanfinder.json) |
| standard | loogle | `Finset.card, Finset.finsupp` | Finset.card_finsupp. [receipt](../evidence/Roth.ncard_boxFamily/search-standard-loogle.json) |
| standard | leansearch | `cardinality of finitely supported functions restricted to a finite set and finite coefficient sets` | Cardinal.mk_finsupp_lift_of_fintype, DFinsupp.card_pi, Fintype.card_finsupp. [receipt](../evidence/Roth.ncard_boxFamily/search-standard-leansearch.json) |
| standard | rg | `card_finsupp∣card_Iic∣mem_finsupp_iff` | Pinned source hits; see receipt. [receipt](../evidence/Roth.ncard_boxFamily/search-standard-rg.json) |
| standard | local_search | `card_finsupp` | Finset.card_finsupp, Fintype.card_finsupp, Multiset.card_finsuppSum; index:error. [receipt](../evidence/Roth.ncard_boxFamily/search-standard-local_search.json) |
| abstract | leanfinder | `cardinality injective image finite set equals cardinality and finite dependent function product cardinality` | Finset.card_image₂, Finset.card_image₂_iff, Finset.card_image₂_singleton_right. [receipt](../evidence/Roth.ncard_boxFamily/search-abstract-leanfinder.json) |
| abstract | loogle | `Set.ncard, Function.Injective` | Set.ncard_range_of_injective, Set.ncard_image_of_injective, Set.ncard_preimage_of_injective_subset_range. [receipt](../evidence/Roth.ncard_boxFamily/search-abstract-loogle.json) |
| abstract | leansearch | `number of functions choosing an element of a finite set at every coordinate equals a product` | Finset.card_pi, Nat.card_fun, Fintype.card_filter_piFinset_eq_of_mem. [receipt](../evidence/Roth.ncard_boxFamily/search-abstract-leansearch.json) |
| abstract | rg | `ncard_image_of_injective∣card_pi∣card_fun∣finprod_eq_prod_of_mulSupport_subset` | Pinned source hits; see receipt. [receipt](../evidence/Roth.ncard_boxFamily/search-abstract-rg.json) |
| abstract | local_search | `ncard_image_of_injective` | Set.ncard_image_of_injective; index:error. [receipt](../evidence/Roth.ncard_boxFamily/search-abstract-local_search.json) |

Each cell links the exact current request and full raw returned result. Local search reports
`index:error`; positive hits were source/native checked, while empty/failure results are not
absence proofs. External Finder/LeanSearch returns
`Polynomial.card_eq_of_natDegree_le_of_coeff_le`; the pinned file instead declares
`Polynomial.boxPoly` and `Polynomial.ncard_boxPoly` at MahlerMeasure:55–69. This univariate degree
and real-interval count is not the arbitrary-variable monomial-box formula. The external spelling
is explicitly unavailable in the tested pinned context; it must not be invented as an API hit.
All relevant pinned files, exact signatures/proofs and hashes are archived in
[mathlib inputs](../evidence/Roth.ncard_boxFamily/mathlib-inputs.json).
Full-name [source search](../evidence/Roth.ncard_boxFamily/full-name-search.json) has no target hit.
The positive core candidates are natively checked and used in the accepted isolated proof:
`Finset.card_finsupp`, `Finsupp.card_Iic`, `Nat.card_Iic`, `Int.card_Icc`,
`Set.ncard_image_of_injective`, `AddMonoidAlgebra.ofCoeff_injective` and
`finprod_eq_prod_of_mulSupport_subset`. Abstract `Nat.card_fun` / `Finset.card_pi` and finite-type
Finsupp cardinalities explain the choice count but do not discharge the semantic bridge.

## Phase 5.5 — statement shape, all three checks

1. **Normal form:** semantic Set.ncard versus Finset cardinal/image versus finite-function
   cardinalities. The RHS arithmetic is the right normal form for caller rewriting; the bridge
   is a proved equality, not definitional. Do not replace ncard by an infinite cardinal silently.
2. **Syntactic generality:** compiled Finsupp r / varying coefficient choices and the constant
   specialization; original function r with support instance is easier at the existing caller and
   was preserved. `finprod_eq_prod_of_fintype` recovers finite-type notation, without restricting σ.
3. **Superfluous arguments:** σ, r, B identify the counted family; support is essential in the
   uniform theorem. No positivity or Nonempty/Fintype σ is needed. B=0 admits its separately
   proved exception. Decidability remains local/Classical, not an extra public premise.

Local form SHIP-AS-STATED; a semantic upstream proposal is RESTATE-BEFORE-SHIP with the generic
choice interface above, whose exact scope has compiled.

## Phase 6.0 — callers and inline audit

| Caller | Occurrence | Experiment |
|---|---|---|
| `Roth.exists_ne_modByMonic_eq`, MainLemma:359–379 | One body use in the simp list at373; same file | Full original signature/body replay with that single use replaced by the complete count proof; clean native success and signature equality. |

Fresh [rg --no-ignore](../evidence/Roth.ncard_boxFamily/source-search.json) and
[git grep](../evidence/Roth.ncard_boxFamily/tracked-source-search.json) agree on source occurrences.
[Full callers and hashes](../evidence/Roth.ncard_boxFamily/callers.json),
[source inventory](../evidence/Roth.ncard_boxFamily/source-inventory.json),
[inline audit](../evidence/Roth.ncard_boxFamily/inline-audit.json).
Executable source callers=1, same-file=1, external-to-file=0. The canonical kernel audit independently
finds one direct value consumer and zero direct type consumers:
[canonical consumers](../evidence/Roth.ncard_boxFamily/canonical-consumers.json).
Docstring mentions and the declaration head are lexical occurrences, not executable callers.
No independent inline rederivation of this same semantic count occurs elsewhere: `card_box` counts
monomials; other cardinality manipulations count remainder functions, different mathematical sets.

The caller equips only the family subtype with Fintype using `boxFamily_finite`, then maps each
polynomial to its J×Fin(natDegree f) array of bounded integer remainder coefficients. Its strict
inequality remains exactly
`(2*C+1)^(f.natDegree*J.card) < (B+1)^∏ᶠ j,(r j+1)` after `exact_mod_cast hcount`.
The inlined equality still rewrites the domain cardinality to that RHS, so
`Fintype.exists_ne_map_eq_of_card_lt` retains its original premise and output.
No Fintype σ restriction or changed mathematical hypothesis was introduced.

The native inlined caller has no **direct** `Roth.ncard_boxFamily` body dependency; it retains the
private representation helper and `boxFamily_finite`, which also shares that helper. No independence
from transitive project/simp closure is claimed. The target has no simp attribute; its use in this
simp list is explicit. Source, kernel-type, kernel-body and transitive scopes remain distinct.

## Phase 6 — composition and pairwise duplication audit

Actual existing-mathlib abstract image count closes by:

```lean
simp only [Set.ncard_image_of_injective _ AddMonoidAlgebra.ofCoeff_injective,
  Set.ncard_coe_finset, Finset.card_finsupp]
```

[Composition source](../evidence/Roth.ncard_boxFamily/composition-executed.lean.txt),
[clean receipt](../evidence/Roth.ncard_boxFamily/composition-receipt.json).
`Box246Composition.simp_original` also closes by a simp composition, **after** supplying the private
project representation and a newly proved exponent-cardinality/finprod equality. Those are real
obligations, not existing mathlib constants hidden in call counts. Original proof uses at least
image cardinality, finite-set coercion, coefficient product count, integer interval count, constant
product, Finsupp interval count, natural interval count, finprod transport and the private bridge.
Bounded direct `card_finsupp`, direct image law and `simp only [boxFamily]` closure probes fail,
then the full proof succeeds in the accepted project execution. These are concrete probes,
not universal absence claims. **NOT-COMPOSABLE by the strict existing ≤3-call criterion**.
The new generic semantic proof is not counted as an existing mathlib replacement.
The closing simp experiments trigger the explicit Phase6b taste boundary, hence BORDERLINE.

Parent `boxFamily` is already accepted BORDERLINE, not NO-mathlib-has-it, so ModeB's forced
re-aim NO gate does not apply. Its actual representation was independently read and tested;
no verdict was inherited from parent usefulness or proof length.

| Decl A | Decl B | Same statement? | Same proof? | Verdict |
|---|---|---|---|---|
| ncard_boxFamily | boxFamily_finite | No: exact count versus finiteness | Shared semantic representation | Keep count and finiteness distinct; ncard of infinite sets is0. |
| ncard_boxFamily | Roth.card_box | No: polynomials versus exponent vectors | Shared rectangular product counting | Count coefficients as second layer; no duplication. |
| ncard_boxFamily | Finset.card_finsupp | Only after representation, exponent count and interval arithmetic | Existing central finite-choice step | Reuse; do not call the full old form an existing theorem. |
| ncard_boxFamily | Polynomial.ncard_boxPoly | No: arbitrary-variable coordinate bounds versus univariate natDegree | Both finite coefficient choices, different bridge | Related API; no direct specialization proved for original form. |
| ncard_boxFamily | Set.ncard_image_of_injective | No: abstract transport law | Exact transport step | Use after the actual bridge. |

## Phase 7 — verdict and concrete actions

**BORDERLINE-needs-human.** Literature establishes the exact finite-choice formula, and the current
statement is sound at all boundaries. Formal search identifies genuine reusable counting primitives;
it does not establish an existing theorem about this semantic polynomial family. Generic semantic
counting is verified, but involves parent-interface redesign and a new representation proof.
Closing simp composition makes the choice of public semantic API a taste decision under Phase6b.
Neither implementation cost, short source spelling, nor parent usefulness decides this verdict.

Future upstream questions (completed assessment; these are not user blockers):

1. Should mathlib expose a semantic bounded-degree polynomial cardinality theorem, rather than
   leave users with the existing Finset.finsupp image count?
2. If yes, should the primary theorem allow coordinate-dependent finite coefficient sets over a
   commutative semiring, with zero permitted only outside the exponent box?
3. Should the integer coordinate-box finprod corollary remain project-local while the reusable
   semantic coefficient-family bridge is proposed upstream?

Concrete current action: retain the theorem near `boxFamily` in `Roth/MainLemma.lean`.
If local cleanup chooses inlining, replace the sole caller's simp-list entry with the full verified
count proof exactly as in project-executed, retaining the private representation; there are no
other explicit callers to update. If upstream interface design is selected, use the compiled generic
semantic statement and make Finsupp.Interval/Finset.Finsupp import layering explicit near
MvPolynomial degree/coefficient APIs. No unconditional deletion is justified by the experiments.
YES-only exact home/title/reviewer/recent commits/grouping requirements are justified n/a for this
BORDERLINE assessment; no unsupported upstream PR or accepted-YES grouping is proposed.

## Phase 8 — verification and handoff

Four complete clean native execution sets: original fullmodule/exact293 audit, isolated mathlib-only
generic proof, project original recovery/edge cases/full caller inline/dependencies, and composition.
All accepted sources have zero error/warning/sorry diagnostics, only propext/Classical.choice/Quot.sound,
no new axiom/unsafe/native_decide/resource raise. One cold original response is warming-only;
three isolated, one project and two composition rejected attempts remain separately archived,
including their recovered sorryAx diagnostics. None is accepted evidence. No extra experiments
were run after required scope completed.

[Verification ledger](../evidence/Roth.ncard_boxFamily/verification.json),
[preparation receipts/provenance](../evidence/Roth.ncard_boxFamily/preparation-checks.json),
[instruction input hashes](../evidence/Roth.ncard_boxFamily/instruction-inputs.json),
[current copy manifest](../evidence/Roth.ncard_boxFamily/copy-manifest.json),
[portable validator](../evidence/Roth.ncard_boxFamily/validate.py),
[actual scratch and simulated integrated validator results](../evidence/Roth.ncard_boxFamily/final-validation.json).
The read-only validator checks current manifest hashes/bytes, exact293 source/runtime evidence,
fresh17 production inputs, full clean accepted receipts/standard axioms, formal15, caller/signature
preservation, source links and secret guard. Root acceptance remains pending and independent.
