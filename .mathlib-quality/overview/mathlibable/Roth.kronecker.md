# Roth.kronecker — NO-mathlib-has-it

Canonical declaration102, `Roth/GenWronskian.lean:53`. Full independent assessment; root acceptance pending. This is a positive specialization of existing `MvPolynomial.aeval`, not an absence inference or an inherited verdict.

## Phase 0 — baseline

The successful baseline `lake build` completed2467 jobs; all17 source/pin hashes freshly match the shared baseline. [Baseline](../evidence/Roth.kronecker/baseline-build.txt), [fresh inputs](../evidence/Roth.kronecker/inputs.json), [source hashes](../evidence/Roth.kronecker/source-inputs.json). The declaration is a public noncomputable definition with no placeholder. The entire declaring module and every explicit caller body were read. The module proves existence of a nonzero generalized Wronskian by reducing multivariate polynomials to univariate ones.

Full native type (universe names normalized only):
```lean
∀ {K : Type u} [Field K] {σ : Type v} [Fintype σ],
  ℕ → MvPolynomial σ K →ₐ[K] Polynomial K
```
Its exact body is `MvPolynomial.aeval fun j ↦ Polynomial.X ^ k ^ (Fintype.equivFin σ j : ℕ)`.
The actual original native print, definition and axiom record are archived in verification.json. No `CharZero`, `DecidableEq σ`, positive-base or degree hypotheses belong to this definition.

## Phase 1 — comprehension

For a chosen enumeration e of the finite variables, replace variable x_j by t raised to k raised to e(j), preserving the coefficients. The result is a coefficient-algebra homomorphism from multivariate to univariate polynomials. This construction exists for every natural k, including0 and1; injectivity only on bounded exponent sets is a later theorem with additional hypotheses.

K is the coefficient field, σ is the variable type, its `Fintype` supplies the chosen enumeration, and k is the encoding base. There are no proof hypotheses. A choice of enumeration is mathematically significant: permuting variable ranks generally changes the resulting polynomial. This is not a canonical enumeration-independent invariant.

## Phase 2 — size and one-line definition

BIG: a named classical mathematical substitution, though its implementation is one substantive line. Exhaustive literature remains mandatory.

| One-line exemption | Applies | Evidence |
|---|---|---|
| Avoid defeq abuse | no | Ordinary semireducible definition; no opacity/reducibility barrier contract; exact equality to aeval closes by rfl. |
| Avoid typeclass diamonds | no | A value of existing AlgHom, not a new type or instance. |
| Semantic intent/stable API | yes | `kronecker_monomial`, `coeff_kronecker`, `kronecker_eq_zero_iff`, and the Wronskian reduction use the shared named substitution. |

ONE-LINER WITH-EXEMPTION. This permits considering a name but does not force a new upstream wrapper. The positive existing universal construction and mechanically inlined complete caller proofs decide the verdict. Merely counting one body line would not decide it.

## Phase 3 — exhaustive literature

Every named channel was actually queried/read. Exact requests, returned response hash/bytes/status and sanitized URL locators are in [web0](../evidence/Roth.kronecker/web-0.json), [web1](../evidence/Roth.kronecker/web-1.json), [web2](../evidence/Roth.kronecker/web-2.json). Returned URL query strings were removed; no full returned articles/search bodies are retained.

| Channel | Actual query/read | Outcome |
|---|---|---|
| General web, specific | Kronecker substitution multivariate polynomial x_i t power base degree ring | Uniform-base bounded-exponent encoding; Berkeley thesis theorem6.5.1. |
| General web, general | Kronecker substitution arbitrary commutative ring polynomial encoding weights | Mixed-radix power substitutions; FLINT multivariate multiplication, Lemma4. |
| General web, aliases | Kronecker substitution polynomial multiplication exponent packing algorithm | Also integer coefficient bit packing; distinguish that from this multivariate-to-univariate map. |
| Optional ask_chatgpt_math | tool inventory | n/a: unavailable; no substituted model assertion. |
| Local references | clean.tex lines224–280; rg actual substitution/exponent terms | Lemma1 proof explicitly uses φ(t,t^k,…), degree restriction only for injectivity. [Excerpt](../evidence/Roth.kronecker/local-literature.txt). |
| nLab | site:ncatlab.org/nlab Kronecker substitution polynomial | Polynomial/free commutative algebra universal property; exact Kronecker name gives unrelated delta material too. |
| nCatLab | site:ncatlab.org/ncatlab polynomial algebra evaluation universal property | No distinct Kronecker-specific construction identified; categorical abstraction is general evaluation, not new higher structure. |
| Stacks | site:stacks.math.columbia.edu polynomial algebra universal property | General polynomial-algebra material only, no distinct specialized Kronecker API identified. |
| MathOverflow | site:mathoverflow.net Kronecker substitution multivariate polynomial | Mostly matrix/root-of-unity false positives; no contrary normal form. |
| Recent arXiv | site:arxiv.org Kronecker substitution after:2021-10-27 before:2026-10-28 | Wang–Su–Wang–Zhang2403.12716(2024) discusses iterative Kronecker reductions;2404.00332 discusses quotient-ring applications. |

[Direct access metadata](../evidence/Roth.kronecker/web-direct.json), [full primary paper metadata](../evidence/Roth.kronecker/web-full.json). nLab direct open failed400 unsupported XHTML; indexed text was available. Stacks tag00F0 direct follow-up was unrelated spectra material and excluded from support. The FLINT page discloses partially generated text and is treated as supplementary implementation documentation; the primary arXiv full paper §1 lines52–55 independently states the standard ordered power substitution and history.

Primary paper: [Wang et al.2024](https://arxiv.org/abs/2403.12716). Supplementary implementation documentation: [FLINT multivariate multiplication](https://fredrikj.net/fdoc/html/algorithms/multivariate/multiplication.html). Conceptual reference: [nLab polynomial](https://ncatlab.org/nlab/show/polynomial). These establish a standard family of chosen ordered power substitutions, with uniform and mixed radices. The universal evaluation construction is broader than these named instances. The current rational-source proof works over fields, whereas defining the map needs neither inverses nor characteristic assumptions. Claims of global injectivity or enumeration independence would change the mathematics and are rejected.

## Phase 4a–4b — parameters and verified generality

| Parameter | Current | Standard/general form | Actual check |
|---|---|---|---|
| K | Type u | arbitrary coefficient type | Already universe polymorphic. |
| Field K | field | CommSemiring R suffices for evaluation/powers | Native `general`/`weighted` compile over CommSemiring; R=ℕ probe. |
| σ | Type v | arbitrary variable type for chosen weights | Independent universe and infinite σ=ℕ probes. |
| Fintype σ | implicit chosen enumeration | explicit rank e:σ→ℕ or weights w:σ→ℕ require no finiteness | Compiled explicit e and w variants; specialization by rfl. Dropping Fintype while retaining equivFin is not claimed. |
| k | ℕ | retain natural base for uniform radix | Powers require this representation; arbitrary weights are broader evaluation, not an injective encoding without extra restrictions. |
| target Polynomial K | univariate polynomials | any commutative R-algebra for general evaluation | Existing native aeval signature supplies this, no new helper needed. |

STRICTLY NARROWER THAN STANDARD/general algebraic interface, mechanically verified. Proposed generalized presentation is `aeval (fun j ↦ Polynomial.X ^ w j)` over `[CommSemiring R]`, arbitrary σ and w. It is already in mathlib as `MvPolynomial.aeval`; therefore this is the explicit false-positive Class4 guard against YES-but-generalise-first. Scratch `general` and `weighted` are testing presentations, not preexisting mathlib constants and not proposed new wrappers. Cost CHEAP; cost is not a verdict factor.

## Phase 4c — all nine modern-idiom rows

| # | Question | Answer and consequence |
|---|---|---|
|1| Typeclasses instead of preambles | no new class; Field/Fintype are already instances, evaluation uses existing Algebra. |
|2| Filters/topology | no; finite algebraic power substitution has no limits. |
|3| Universal characterization | yes; existing free commutative algebra evaluation `aeval`, with generator images specified explicitly. |
|4| Bundled substructures | no; result already bundled AlgHom, no closure predicate to replace. |
|5| Hierarchy weakening | yes; CommSemiring coefficients compile, enabling ℕ and rings with zero divisors. |
|6| Higher categorical | no; no higher categorical content in this substitution. |
|7| Concrete indices | yes for variable ranks: explicit e/w removes artificial chosen finite enumeration; retain ℕ exponents for ordinary polynomials. |
|8| Concrete-via-abstract diagnostic | body has one occurrence each of X/equivFin in the image assignment, and otherwise only abstract aeval. No theorem proof/unfolding prefix exists to count. Abstract construction already exists; substitution is its specialization. |
|9| False-generalization guard | no semantic mismatch in exact specialization to the old weights. Arbitrary weights are not automatically a bounded-injective Kronecker code; no such false theorem proposed. Enumeration independence explicitly rejected. |

Modern idiom available: yes, already `MvPolynomial.aeval`. It composes with `aeval_X`, `aeval_monomial`, AlgHom map APIs and arbitrary coefficient algebras. This is a real existing abstraction, not an invented categorical restatement.

## Phase 4.5 — infrastructure risks, all six rows

| Risk | Level | Evidence |
|---|---|---|
| Typeclass diamond | NONE | Definition introduces no instance. Polynomial coefficient Algebra and CommSemiring synthesize along existing paths. |
| Reducibility leak | LOW | Ordinary noncomputable def, no reducible attribute; direct equality to RHS rfl verified. Noncomputability includes the chosen enumeration; aeval itself is also noncomputable in this setting. |
| Noncanonical unfolding | LOW | EquivFin is choice-dependent, but internally shared; no simplifier rule declares enumeration-independent output. Explicit weights avoid this hidden choice. |
| Instance priority collision | NONE | Not an instance; no priority to collide. |
| Universe polymorphism | LOW | Native ℚ/Fin2 and independently lifted coefficient and variable universes compile; no same-universe constraint. |
| Coercion ambiguity | NONE | Existing AlgHom CoeFun synthesizes; no new coercion, AlgHom and its function application have the expected types. |

Overall LOW; no HIGH rows. Native infrastructure source/receipt is linked by verification.json. None of these probes claims a `#synth` of the non-class value kronecker itself.

## Phase 4.6 — proof strategy, all five rows

| Question | Answer |
|---|---|
| Topological ε/δ versus filters | no topology. |
| Element versus submodule/ideal reasoning | no proof: map is already bundled algebra homomorphism. |
| Sequences versus nets | no convergence. |
| Explicit construction versus universal property | already uses universal evaluation aeval, not hand-built ring-hom obligations. |
| Missing helpers SHOULD exist | no helper needed for defining this map; bounded coefficient/injectivity/chain-rule theorems are separately assessed declarations. |

MATHLIB-IDIOMATIC construction. Locally retaining a semantic name may aid readability; it does not introduce a missing mathematical construction upstream.

## Phase 5 — five actual mathlib methods on three forms

[Complete formal requests/raw receipts](../evidence/Roth.kronecker/formal-search.json); actual command receipts: [current](../evidence/Roth.kronecker/rg-current.json), [standard](../evidence/Roth.kronecker/rg-standard.json), [abstract](../evidence/Roth.kronecker/rg-abstract.json).

| Method | Current form | Literature form | Abstract form |
|---|---|---|---|
| Finder | named Kronecker substitution query; unrelated finSuccEquiv/expand | aeval/powers query | arbitrary AlgHom signature; aeval positive hit |
| Loogle | quoted kronecker; matrix names unrelated | MvPolynomial, Polynomial | MvPolynomial.aeval, positive exact general signature |
| LeanSearch | Kronecker power substitution | aeval powers | general algebra evaluation, positive aeval hit |
| rg | full untruncated Kronecker hits | aeval/bind₁/expand in MvPolynomial | actual Eval.lean definition and algHom_ext |
| local | kronecker | aeval | eval₂Hom |

Local tool explicitly reports index unavailable; its results are limited fallback, not exhaustive absence. Remote revisions may differ; all decisive candidates were checked against the pinned local library and compiled. `Matrix.kronecker` is tensor-product matrix construction. `MvPolynomial.expand` sends each variable to the same power of itself and stays multivariate; `bind₁` also stays multivariate; neither is falsely cited as the exact target. `finSuccEquiv` is an equivalence to an iterated polynomial ring, not this many-to-one encoding.

Positive exact existing block: `MvPolynomial.aeval` in `Mathlib/Algebra/MvPolynomial/Eval.lean:569`:
```lean
{R : Type u} → {S : Type v} → {σ : Type w} →
  [CommSemiring R] → [CommSemiring S] → [Algebra R S] →
  (σ → S) → MvPolynomial σ R →ₐ[R] S
```
Instantiating S=Polynomial K and the displayed generator assignment gives the original **definitionally**, in one existing constructor call. `aeval_monomial` is checked as supporting API, not substituted for the definition. `eval₂Hom` is its lower-level RingHom counterpart. The isolated mathlib-only source guards `#check_failure Roth.kronecker`; no own/downstream theorem is used to manufacture the positive hit.

Conclusion: found in mathlib as `MvPolynomial.aeval`, strictly more general form with exact choice of generator images. No absence conclusion is needed.

## Phase 5.5 — three statement-shape checks

Normal form: existing bundled `MvPolynomial.aeval` with an explicit assignment; alternative `eval₂ (algebraMap …)`/`eval₂Hom` erases or lowers the convenient AlgHom structure. Native original-to-aeval equality has canonical RHS and closes rfl. Syntactic generality: explicit enumeration/weights are easier to supply for ordered variable types, and avoid hardwiring choice; actual general and weighted experiments compile. The convenient named local uniform-base map remains an optional downstream interface.

Superfluous audit: K/σ are essential types; Field can weaken to CommSemiring; Fintype is essential only to the current equivFin spelling, removable with supplied rank/weights; k is essential for uniform base. No CharZero or l argument exists in the elaborated type. Overall RESTATE-BEFORE-SHIP if one were proposing a new specialization; existing aeval already has the desired generality. This does not require changing production in a read-only assessment.

## Phase 6.0 — complete explicit callers and inline audit

Internal uses outside the declaring file:0; external-to-file callers/files:0. Inside it,9 distinct declarations have17 textual identifier occurrences on15 source lines (excluding definition/docstrings). This is useful local API, not dead code. [Callers/refactor plan](../evidence/Roth.kronecker/callers.json), [source rg](../evidence/Roth.kronecker/rg-callers.json), [inline audit](../evidence/Roth.kronecker/rg-inline.json).

| Caller | Lines | Required migration |
|---|---|---|
| kronecker_monomial |61,62| inline aeval assignment in conclusion; remove kronecker unfolding from simp. |
| coeff_kronecker |89| inline assignment; use replayed monomial statement. |
| kronecker_eq_zero_iff |107| inline assignment; use replayed coefficient statement. |
| linearIndependent_kronecker |119| inline assignment; use replayed zero criterion. |
| private kronHasse |146| inline assignment inside composed operator. |
| private derivative_kronHasse_aux |159| remove kronecker unfolding; existing chain rule evaluates explicit assignment. |
| private hasseDeriv_kronecker_mem |191,200,205| inline every occurrence; replay its induction with migrated operators. |
| exists_hasseDeriv_kronecker_eq_sum |216| inline assignment in the uniform expansion. |
| private wronskian_kronecker_eq_sum_aux |240–245| inline all four occurrences; existing AlgHom.map_det remains applicable. |

Inline RHS grep finds no second construction bypassing the definition. The derivative helper spells derivatives of the generator images, which is required chain-rule data, not a duplicate map. Exact293-name ordered unique canonical audit records9 expression consumers with different membership: derivative_kronHasse_aux has a source-only unfold entry but no target constant in its compiled term; exists_genWronskian_ne_zero has an elaborated target reference despite no literal source identifier. The exact separate list is retained in verification.json; source callers are not equated to kernel closure.

Actual full caller proof replay removes the target definition entirely and substitutes the direct existing aeval at every operator application in the whole declaring-module body, with new namespace and full original proofs. It includes the eventual existence theorem to check composition of migrated callers. Explicit `(Polynomial.X : Polynomial K)` annotations resolve coefficient inference after inlining. The first replay with unannotated X was rejected (metas/default typeclass budget); the corrected complete proof replay passed without raising limits. This is not theorem transport via a new equality theorem. Project Hasse/Wronskian ingredients still occur because this tests caller migration, not a claim all downstream mathematics is already in mathlib. Isolated direct construction separately proves the mathlib-only claim.

## Phase 6 — actual composition

COMPOSABLE in one call:
```lean
MvPolynomial.aeval
  (fun j ↦ Polynomial.X ^ k ^ (Fintype.equivFin σ j : ℕ))
```
Equality of this expression to the original is `rfl`; no normalization premise, `simp [defs]` proof, parent project lemma, or newly proved helper is counted as an existing building block. The full replay concerns caller compatibility; its multi-line proofs are not miscounted as this one-call composition.

## Phase 7 — verdict and concrete action

**NO-mathlib-has-it**, existing declaration `MvPolynomial.aeval`. Reason: exact positive definitional specialization of a general existing construction, confirmed in isolated mathlib and by the actual elaborator, plus complete inlined caller proof migration. Literature confirms semantic meaning and the one-line exemption is real; nevertheless a chosen-enumeration wrapper adds no missing construction over the existing universal evaluation API. This verdict is not based on cost, failed search, source body length, or genWronskian's independent YES verdict. No parent-NO re-aim shortcut applies.

Do not submit this exact definition alone to mathlib. At each of the9 callers listed above, direct aeval assignment is the verified replacement; remove target unfolding entries at the two simp sites. If retaining the name for the Roth proof's readability, its alternative destination is a local/private helper in `Roth/GenWronskian.lean`, with choice of enumeration documented. If a later contribution establishes a reusable bounded-exponent encoding API, assess that mathematics separately, preferably with explicit variable ranks/radices; this report makes no verdict claim for unassessed lemmas.

## Phase 8 — evidence handoff

All phases complete; no unresolved verification obligations. Native exact executed sources and raw receipts, fresh region starts and axiom assertions are enumerated by [verification](../evidence/Roth.kronecker/verification.json). The package [validator](../evidence/Roth.kronecker/validate.py) supports scratch/integrated layouts and checks the current manifest, exact canonical order, hashes, fresh native messages, no errors/warnings/nonstandard axioms, and credential guard. Two native attempts are retained as rejected evidence: initial inline-coefficient inference, and initial infrastructure/audit with missing ULift import and a duplicated canonical name. The final exact-order293 audit and independently lifted universe probes passed; rejected diagnostics are never accepted proof evidence. Root independently reviews before integration; production and Git are untouched by this worker.
