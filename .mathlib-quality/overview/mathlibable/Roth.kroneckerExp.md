# Roth.kroneckerExp — full overview and mathlibable assessment

**Verdict: NO-mathlib-has-it.** Existing `Finsupp.weight` is the same weighted exponent map at greater generality. The chosen power weights are a specialization, independently of the earlier `Roth.kronecker` assessment. Semantic usefulness does not establish missing mathlib content.

## Phase 0 — baseline and scope

Resolved public noncomputable definition at `Roth/GenWronskian.lean:57`, canonical103. The complete272-line declaring module and every source caller were read. No production source or pin was edited. All17 inputs were freshly hashed and match the clean2467-job baseline, exit0; [inputs](../evidence/Roth.kroneckerExp/inputs.json), [baseline](../evidence/Roth.kroneckerExp/baseline-build.txt). Root also reports the full CoeffNorm100 build exit0,2467jobs,5.992seconds; baseline reuse here is justified by exact unchanged inputs, not inferred from that timing.

Full native type:

```lean
Roth.kroneckerExp.{u_1} : {σ : Type u_1} → [Fintype σ] → ℕ → (σ →₀ ℕ) → ℕ
```

Full definition:

```lean
fun {σ} [Fintype σ] k d ↦ ∑ j, d j * k ^ (Fintype.equivFin σ j : ℕ)
```

The surrounding `K`, `[Field K]`, and `l` do not occur in the elaborated type. Axioms are exactly standard subsets of `propext`, `Classical.choice`, `Quot.sound`; no `sorryAx`. The disk session explicitly imports `Mathlib.Data.Finsupp.Weight` before the candidate execution; that added assessment prerequisite is not a production import change. Native source/receipt and fresh-region verification are linked in [verification](../evidence/Roth.kroneckerExp/verification.json).

## Phase 1 — mathematical meaning

For a chosen enumeration of a finite variable set, associate to an exponent vector its base-k positional weighted sum. This is the exponent of the image of the monomial under the substitution sending the j-th variable to t raised to k raised to its enumeration rank. The definition itself requires neither k>1 nor any bound on digits; those belong to the separately assessed injectivity theorem.

Parameters: σ is an arbitrary universe-polymorphic index type; its `Fintype` instance supplies cardinality, finite summation, and chosen enumeration; k is the natural base, d a finitely supported vector of natural exponents. Output is a natural number, not a polynomial, a coefficient, or a claim of injectivity. Project declaration dependencies: none. Existing mathlib finite sums and `Fintype.equivFin` supply the body.

## Phase 2 — preliminary checks

SMALL: a positional exponent helper, not a new mathematical structure or a main result. Although its name refers to Kronecker substitution, this declaration asserts no named theorem. Body substantive line count1: ONE-LINER WITH-EXEMPTION.

| One-line exemption | Applies? | Evidence |
|---|---|---|
| Avoid defeq abuse | no | Ordinary semireducible definition; consumers explicitly unfold it; no sealing requirement or reduction barrier found. |
| Avoid typeclass diamonds | no | No class, structure, instance, or new coercion; natural arithmetic paths are existing ones. |
| Semantic intent/API stability | yes | Docstring names the exponent used by `kronecker_monomial`, `kroneckerExp_injOn`, and `coeff_kronecker`; a real local API. |

The exemption permits a useful local name, and does not justify duplicating an already existing general weighted map upstream.

## Phase 3 — exhaustive literature

Only exact requests, response SHA256/byte counts/status, locators, and original short summaries are archived; no article/search-result bodies. Search dates2026-10-27. No returned credential query was needed; secret guard applies to the entire package.

| Channel | Actual request | Finding |
|---|---|---|
| Web specific | Kronecker substitution exponent sum base k monomial encoding | Roche thesis Fact1.1 gives power substitutions and mixed-radix packing. |
| Web general | weighted degree monomial arbitrary weights linear combination exponents | MIT notes §1.8 define exponent-weight dot product. |
| Web aliases | Kronecker map polynomial exponent packing radix representation | Packing exponent map terminology and mixed-radix formulation; unrelated Kronecker sums rejected. |
| ChatGPT math MCP | n/a | `ask_chatgpt_math` is not available; no substitute answer fabricated. |
| Local references | actual rg in clean.tex | §2 lines231–269 contain exactly s₁+ks₂+⋯+k^(p−1)sₚ; bounded digits used for uniqueness, not definition. |
| nLab | site:ncatlab.org/nlab weighted degree monomial; direct free+commutative+monoid page | Indexed free commutative monoid explains formal natural linear combinations. Direct fetch400 unsupported XHTML, preserved honestly. |
| nCatLab | site:ncatlab.org/ncatlab free commutative monoid weight; supplementary quoted free commutative monoid | Returned neighboring nLab material, no independent exact nCatLab hit. Abstract universal-property context relevant; no higher-categorical novelty found. |
| Stacks | site:stacks.math.columbia.edu graded polynomial weighted degree; individual graded/polynomial/degree query | Tag053C permits arbitrary positive generator degrees; Exercise02E7 uses degrees2 and3. Related grading context, no power-radix-specific novelty. |
| MathOverflow | site:mathoverflow.net Kronecker substitution; individual quoted query | Irrelevant approximation/notation results, rejected. This is a limited search outcome, not proof of absence. |
| Recent arXiv | Kronecker substitution polynomial exponents and weighted degree monomial encoding, after:2021-10-27 before:2026-10-28 | 2403.12716 studies iterative substitutions; 2404.00332 quotient-ring uses. Other Kronecker/tensor/recurrence hits rejected. |

Evidence: [general queries](../evidence/Roth.kroneckerExp/web-0.json), [named channels](../evidence/Roth.kroneckerExp/web-1.json), [arXiv](../evidence/Roth.kroneckerExp/web-2.json), [direct fetches](../evidence/Roth.kroneckerExp/web-direct.json), [Stacks](../evidence/Roth.kroneckerExp/web-stacks.json), [MathOverflow](../evidence/Roth.kroneckerExp/web-mo.json), [local source](../evidence/Roth.kroneckerExp/local-literature.txt).

Standard concept: weighted degree of a monomial, specialized to positional encoding; general weighted sums make sense independently of coefficient rings, enumerations, or positivity. The particular power-weight encoding and its bounded injectivity should not be conflated. [MIT notes, §1.8](https://math.mit.edu/classes/18.721/ag-feb20.pdf), [Roche thesis, Fact1.1](https://cs.uwaterloo.ca/~droche/phd/ch1-intro.pdf), [arXiv2403.12716](https://arxiv.org/abs/2403.12716).

## Phase 4a–4b — generality

| Parameter | Current interface | Standard/general form | Verified result |
|---|---|---|---|
| σ | arbitrary type with Fintype | arbitrary type if weights explicit and support finite | Existing `Finsupp.weight` and compiled arbitrary-type probes require no Fintype. |
| Fintype σ | enumeration and finite sum | explicit w:σ→M | Cannot drop from this exact spelling: equivFin requires it. Replacement changes representation and explicitly supplies weights. |
| k:ℕ | positional base | arbitrary weight vector | k is an actual input, including0 and1; generic weight specializes to its powers. |
| d:σ→₀ℕ | natural exponent vector | generic finitely supported coefficients over semiring R | Native `Finsupp.weight`/linearCombination equality verifies the general map; original exponent meaning stays natural. |
| output ℕ | positional natural exponent | AddCommMonoid M with Module R M | Existing generic map already handles this; arbitrary additive target verified. |
| K, Field K, l | surrounding context only | absent | Native full type confirms absent; do not advertise dropping nonexistent hypotheses. |

Current fixed chosen-enumeration interface is maximally general without changing representation. Abstract weighted representation is strictly broader and already in mathlib; there is no YES-generalise-first ticket. Generality is established by actual elaborated candidate and compiled equalities, not hierarchy speculation. In particular, arbitrary weights do not inherit radix injectivity.

## Phase 4c — all modern-idiom checks

| # | Question | Result and concrete consequence |
|---|---|---|
| 1 | Typeclasses instead of bundled hypotheses | no: Fintype is already a class; no manual algebraic laws. |
| 2 | Filters/nets | no: finite algebraic encoding, no topology. |
| 3 | Universal property | yes: extend generator weights from a free commutative monoid; existing `Finsupp.weight`, built from `linearCombination`, supplies the bundled map. |
| 4 | Bundled substructure | no: no set-with-closure predicate occurs. The bundled additive-map improvement is addressed in row3; it enables `map_zero`, `map_add`, `weight_single`. |
| 5 | Field/vector-space weakening | no coefficient field in actual type. Existing generic R-semiring/M-module weight is useful but not a field weakening of this declaration. |
| 6 | Higher category | no: no categorical statement to upgrade. |
| 7 | Concrete indices/targets | yes: arbitrary weight targets in additive commutative monoids via ℕ-module structure are already implemented. Preserve ℕ for actual exponent encoding. |
| 8 | Concrete-via-abstract diagnostic | yes: definition body contains zero `kronecker` identifiers; its only special data are k powers and enumeration. It uses only finite sum and multiplication, exactly weight_eq_sum. Explicit native equality verifies the abstract diagnostic. |
| 9 | False-generalization guard | passes for specialization equality; fails if arbitrary weights are claimed injective or claimed the same chosen radix encoding without specialization. Those claims are rejected. |

Modern idiom available: existing `Finsupp.weight (fun j ↦ k ^ rank j)`. It exposes additive and singleton laws without reproving them. Cost is a local caller rewrite; the verdict depends on exact existing content, not that cost.

## Phase 4.6 — proof strategy

| Check | Applies? | Assessment |
|---|---|---|
| Topology ε–δ versus filters | no | No topology. |
| Algebra elementwise versus bundled | yes | Replace plain finite-sum function by existing additive weight hom; native `map_add` closes the general law. |
| Analysis sequences versus nets | no | No convergence. |
| Category construction versus universal property | no new category | Existing free-object linearCombination is the relevant abstraction; no new class needed. |
| Missing helper API | no | `weight`, `weight_eq_sum`, `linearCombination` already cover the definition and normalization. |

REFACTOR-RECOMMENDED locally: use weight directly where desired. No missing API for this definition; bounded injectivity, coefficient recovery, and derivative claims remain separate assessments.

## Phase 4.5 — six infrastructure risks

| Risk | Verdict | Evidence |
|---|---|---|
| Typeclass diamond | NONE | Target installs no instances. Native AddCommMonoid ℕ and Module ℕ ℕ synthesize existing structures; replacement uses their existing paths. |
| Reducibility leak | LOW | Semireducible plain def, no reducible attribute; explicit rfl body probe and generic linearCombination rfl equality verify controlled definitional equality. |
| Noncanonical unfolding | LOW | Fintype.equivFin is chosen noncomputably. Enumeration changes the encoding; equality to weight keeps exactly the same enumeration and uses weight_eq_sum, not an asserted rfl bridge. |
| Instance priority collision | NONE | No instance or priority declaration, so no new competing search path. |
| Universe polymorphism | NONE | Native ULift.{v}(Fin2) tests target and weight with lifted universe; signature retains arbitrary universe. |
| Coercion ambiguity | NONE | Original is a natural-valued function; replacement uses the single existing additive-hom CoeFun path, synthesized explicitly over lifted index type. No custom coercion added. |

Overall LOW; no HIGH rows. Actual native probes, signatures, fresh diagnostics, and axioms are in [verification](../evidence/Roth.kroneckerExp/verification.json).

## Phase 5 — five actual mathlib methods

Every method ran on current, literature-standard, and abstract forms. [Formal requests and complete raw receipts](../evidence/Roth.kroneckerExp/formal-search.json), [Loogle retry](../evidence/Roth.kroneckerExp/formal-search-retry.json).

| Method | Current | Standard | Abstract |
|---|---|---|---|
| Lean-Finder | Kronecker exponent search, monomial/weighted-homogeneous neighbors | weighted monomial degree points to Finsupp.weight | finite-coefficient module combination points to linearCombination |
| Loogle | quoted kronecker name gives unrelated symbols/no exact target | Finsupp.weight positive signature | dotted linearCombination query failed, retained; quoted-name retry positive exact Finsupp.linearCombination |
| LeanSearch | positional substitution exponent query | weighted sum returns weight and weight_apply | free-module linearCombination query positive |
| rg local pinned source | kroneckerExp/Kronecker | weight, weight_apply, weight_eq_sum | linearCombination definition and application |
| lean_local_search | kronecker | Finsupp.weight family | Finsupp.linearCombination family |

Local API reports index unavailable; returned file/name fallback is useful, but not an absence proof. External indices may use a different revision. Local complete files and native pinned specialization are authoritative. [rg-current](../evidence/Roth.kroneckerExp/rg-current.json), [rg-standard](../evidence/Roth.kroneckerExp/rg-standard.json), [rg-abstract](../evidence/Roth.kroneckerExp/rg-abstract.json).

Positive candidate in `Mathlib/Data/Finsupp/Weight.lean:82,100`:

```lean
Finsupp.weight : {σ M R : Type*} → [Semiring R] → (σ → M) →
  [AddCommMonoid M] → [Module R M] → (σ →₀ R) →+ M
Finsupp.weight_eq_sum (w : σ → M) [Fintype σ] (d : σ →₀ R) :
  Finsupp.weight w d = ∑ i, d i • w i
```

`weight` is definitionally `(Finsupp.linearCombination R w).toAddMonoidHom`; native signature/definition and general rfl check confirm that fact. Read [Weight complete source](../evidence/Roth.kroneckerExp/source-2.lean.txt), [LinearCombination complete source](../evidence/Roth.kroneckerExp/source-3.lean.txt). MvPolynomial weightedTotalDegree instead aggregates weights across polynomial support; it is not this exponent-vector map and was rejected as an exact replacement. Nat.ofDigits is an alternative positional-list view requiring an enumeration bridge, and not the preferred general weighted abstraction.

## Phase 5.5 — statement shape

Normal forms considered: explicit finite sum, `Finsupp.weight w d`, `Finsupp.linearCombination ℕ w d`, and `Nat.ofDigits` on an enumerated digit list. Canonical mathlib monomial-weight form is `Finsupp.weight`. Equality is oriented toward this existing form on the right; it is not claimed definitional from the original whole-Fintype sum.

Syntactic generality: prefer weight application for an exponent and its additive hom for function arguments such as InjOn. Native pointwise and function equalities both compile. Superfluous arguments: none in actual elaborated type. Fintype is essential to chosen enumeration; removing it requires explicit weights, not merely deleting a hypothesis. k and d are essential data; no hk/digit-bound hypothesis is present to drop. Overall RESTATE-BEFORE-SHIP as a specialization of the existing canonical weight rather than an upstream duplicate.

## Phase 6.0 — every caller and inline audit

[Exact source receipts](../evidence/Roth.kroneckerExp/rg-callers.json), [structured callers](../evidence/Roth.kroneckerExp/callers.json), [inline search](../evidence/Roth.kroneckerExp/rg-inline.json). Three distinct explicit source callers, six code occurrences on six lines after excluding definition and docstring; one docstring occurrence at59 is additionally retained in raw rg. Zero callers outside the declaring file. Already accepted `Roth.weight` is another specialization of the same generic Finsupp.weight API, into ℝ using reciprocal weights (including zero-denominator behavior); it is not equal to this ℕ-valued exponential-weight map. This shared generic pattern is an overview moral duplication, independently verified here rather than inheriting its verdict. No hidden downstream-library assumption is made. This is useful local API, not dead code.

| Caller | Migration |
|---|---|
| Roth.kronecker_monomial, lines61–62 | Exponent becomes `Finsupp.weight (fun j ↦ k ^ rank j) d`; change unfolded kroneckerExp in simp list to weight_eq_sum and smul_eq_mul. Remaining aeval/power proof unchanged. |
| Roth.kroneckerExp_injOn, lines70,73–74 | InjOn takes weight hom coerced to a function; local Nat.ofDigits-to-weight equality uses weight_eq_sum and smul_eq_mul. Original list digit uniqueness proof retained. |
| Roth.coeff_kronecker, line89 | Coefficient index becomes identical weight application; uses replayed monomial and injectivity lemmas, with its original coefficient proof unchanged. |

Inline audit: direct power weights also occur in the kronecker generator definition and derivative coefficients; these are generators/coefficients, not independently rederived exponent-vector maps. Nat.ofDigits local hsum is the expected representation bridge, not an independent external implementation. `Roth.weight` and rational/index-related Finsupp.weight uses are different weight choices; no duplicate positional map outside this module found.

The canonical runtime audit visits all293 declarations in exact tracked order, including actual private names, and checks requested293/unique293/present293/values293. The actual direct value consumers are `Roth.kronecker_monomial`, `Roth.kroneckerExp_injOn`, `Roth.coeff_kronecker`, and `Roth.kronecker_eq_zero_iff`: the fourth arises during elaboration although its source has no explicit token. Source callers are distinct from constants whose elaborated values retain direct references. Full source replay removes the target definition and migrates every term/unfolding use, including later generalized-Wronskian assembly. This validates executable caller migration, not merely statement sketches. [Prepared replay](../evidence/Roth.kroneckerExp/consumers-prepared.lean.txt), [canonical source](../evidence/Roth.kroneckerExp/canonical-audit-array.lean.txt), [native verification](../evidence/Roth.kroneckerExp/verification.json).

## Phase 6 — actual composition experiments

COMPOSABLE as exact specialization of an existing map. Native direct pointwise proof:

```lean
by simpa only [Roth.kroneckerExp, smul_eq_mul] using
  (Finsupp.weight_eq_sum (fun j ↦ k ^ (Fintype.equivFin σ j : ℕ)) d).symm
```

This is a single existing `weight_eq_sum` application with symmetry and representation normalization. It is not a discovery based solely on a closing `simp [defs...]` composition under Phase6b: the positive existing object itself is Finsupp.weight, and the named application states exactly its finite-sum formula. Native function equality adds funext; no new upstream theorem is necessary. General weight/linearCombination equality is rfl, and additivity is existing `map_add`. The Mathlib-only probe guards `#check_failure Roth.kroneckerExp` and independently verifies the finite-sum specialization; own/downstream project lemmas do not supply the replacement.

## Phase 7 — actionable verdict

NO-mathlib-has-it. Exact existing `Finsupp.weight`, derived from `Finsupp.linearCombination`, includes this map at greater generality and already has its finite-sum formula. The definition has no coefficient field, and the evidence does not depend on a parent kronecker verdict or re-aim shortcut.

Refactor plan: replace each of the three callers exactly as listed in Phase6.0; retain the bounded radix theorem under an appropriate weight specialization. The full module replay demonstrates all proof bodies through `exists_genWronskian_ne_zero`. Alternative local destination: keep a documented local/private semantic helper in `Roth/GenWronskian.lean` (implemented via weight if desired) while not proposing this specialization alone to mathlib. Existing building blocks: `Finsupp.weight`, `Finsupp.weight_eq_sum`, `Finsupp.linearCombination`; incidental normalization uses `smul_eq_mul`. No additional PR or public API is justified for the definition itself. No unresolved user design question remains for this read-only assessment; production edits are outside this package.

## Phase 8 — completion and evidence discipline

All required phases are present. Five accepted native execution sets are original, generic, consumers, raw, and audit-final. No native proof attempt failed. One preparation-only array duplication was caught by root before execution and preserved separately; the generator was repaired by using the exact tracked array once. An earlier successful audit had a coefficient metavariable in one infrastructure #check and is explicitly superseded by the final explicit-R:=ℕ probe. These are excluded from accepted verification. Standard axioms only, no sorry/admit/unsafe/native_decide or raised limits in accepted sources. Current portable manifest validates artifact hashes/bytes, all17 source/pin hashes, actual native success and fresh-region messages, exact ordered canonical293 array, source callers, report links, and secret guard. Root acceptance remains pending until independent review. [Assessment](../evidence/Roth.kroneckerExp/assessment.json), [overview entry](../evidence/Roth.kroneckerExp/overview-entry.json), [verification](../evidence/Roth.kroneckerExp/verification.json), [portable validator](../evidence/Roth.kroneckerExp/validate.py).
