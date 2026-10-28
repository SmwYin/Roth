# `Roth.boxFamily` — canonical 233

**Verdict: BORDERLINE-needs-human.** Keep the project definition while deciding whether upstream
should expose a general coefficient-family interface. Its one-line body is a useful semantic name
for seven consumers. Mathlib supplies the finite products and support machinery, but the actual
coordinate-degree/coefficient-family bridge requires a proof. The new generic proof below is
assessment work, not an existing mathlib replacement. This completed assessment leaves no
verification blocker; the three questions at the end concern future upstream API design.

## Phase 0 — baseline and scope

Resolved public `def` at `Roth/MainLemma.lean:275–276`; no sorry. The module proves Roth's main
lemma by a pigeonhole argument on bounded integer polynomials and then a Hasse derivative
selection. All 17 production-source/pin hashes freshly match the successful 2467-job baseline.
Production, pins, Git and overview/progress files were untouched. The original full MainLemma
module replay passes with standard axioms, together with an exact-order canonical audit of
293 requested, unique, present declarations and 293 kernel values. No file-end build was due at233.

Evidence: [fresh inputs](../evidence/Roth.boxFamily/inputs.json),
[baseline](../evidence/Roth.boxFamily/baseline-build.txt),
[complete original execution](../evidence/Roth.boxFamily/original-executed.lean.txt),
[complete native receipt](../evidence/Roth.boxFamily/original-receipt.json).

The persistent disk document retains its original nine imports. The first isolated run used the
shared exact18 prefix and showed that `Finset.finsupp` and finite Finsupp intervals were not
imported. Necessary233-only extra imports are `Mathlib.Data.Finset.Finsupp`,
`Mathlib.Data.Finsupp.Interval`, and `Mathlib.RingTheory.MvPolynomial.Basic`; their genuine pinned
headers were read. The accepted isolated prefix has21 imports, explicitly authorized by root;
the shared18 file remains unchanged. Cold loading took minutes, not evidence of mathematical
failure. The initial18 failure and all later rejected attempts are archived separately, including
recovered sorryAx and a style warning, and are never counted as accepted verification.
See [authorization](../evidence/Roth.boxFamily/root-prefix-scope-authorization.json),
[prefix hashes/provenance](../evidence/Roth.boxFamily/prefix-provenance.json), and
[verification ledger](../evidence/Roth.boxFamily/verification.json).

## Phase 1 — mathematical content and exact type

For an arbitrary variable type σ, coordinate bounds r : σ → ℕ, and a natural coefficient bound B,
this is the set of integer multivariate polynomials whose degree in each variable j is at most
r(j) and whose every coefficient belongs to the integer interval [0,B]. The zero polynomial is
included. Neither σ nor the support of r must be finite to define the family; those restrictions
concern subsequent finite enumeration. This distinguishes it from the nonzero, absolute-value
bounded `Roth.RSet`.

Full native type (universe u_1 is arbitrary):

```lean
{σ : Type u_1} → (σ → ℕ) → ℕ → Set (MvPolynomial σ ℤ)
```

Exact body:

```lean
{W | (∀ j, degreeOf j W ≤ r j) ∧ ∀ d, 0 ≤ W.coeff d ∧ W.coeff d ≤ B}
```

There are no section hypotheses or project declaration dependencies in the type/body. Construction
uses coordinate degree and coefficient comparisons, rather than selecting or normalizing a
polynomial. [Full kernel type/body](../evidence/Roth.boxFamily/native-type.json) is unelided;
the complete original source is archived separately from the pretty-printed kernel expression.

## Phase 2 — preliminary checks

SMALL: a coefficient-box family used in a proof, not a new algebraic structure or the named main
theorem. The body has one substantive line: ONE-LINER WITH-EXEMPTION.

| Exemption | Applies? | Concrete evidence |
|---|---|---|
| Avoid defeq abuse | No | All seven original caller types remain definitionally equal after literal inlining. |
| Avoid typeclass diamonds | No | This is a Set-valued definition, with no instance or new carrier. |
| Semantic intent / stable API | Yes | `boxFamily_finite`, `ncard_boxFamily`, `exists_ne_modByMonic_eq`, and `sub_mem_RSet` share the same named family. |

The exemption supports a local name, not an automatic upstream YES. Full inlining proves that a
definition can be removed without changing the mathematics; it does not establish an existing
mathlib API replacement.

## Phase 3 — exhaustive literature

Each request, returned-response SHA256/byte count/status, clean titles/URLs and own summary is
archived; article/search bodies are not retained. Search engines can return adjacent concepts
and papers outside a date filter; relevance is assessed from the actual item, not the filter alone.

| Channel | Exact query or local operation | Finding / limitation | Receipt |
|---|---|---|---|
| General specific | integer multivariate polynomials bounded partial degrees coefficients box counting auxiliary polynomial Roth lemma | Coefficient vectors, polynomial lattices; local paper gives this exact construction. | [three queries](../evidence/Roth.boxFamily/web-general.json) |
| General broad | finite monomial support polynomials coefficient sets Cartesian product cardinality | Independent choices of coefficients on a monomial support; broader than a rectangular box. | same receipt |
| General aliases | polynomials bounded height degree lattice box coefficient vectors | Bounded height often means a symmetric absolute bound, which differs from [0,B]. | same receipt |
| ChatGPT math | Optional channel | n/a: `ask_chatgpt_math` is unavailable; no second-opinion response invented. | this row |
| Local references | `rg` in `.mathlib-quality/references/clean.tex` | §6 Lemma9 proof, lines1405–1421: rectangular monomial expansion, integer coefficients0…B₁, count(B₁+1)^r. | [local excerpt](../evidence/Roth.boxFamily/local-excerpt.tex.txt), [source hash](../evidence/Roth.boxFamily/literature-source.json) |
| nLab | site:ncatlab.org/nlab polynomial ring finitely supported functions monomials | Polynomial/free-algebra descriptions support coefficient and finite-support organisation; no exact family primitive. | [receipt](../evidence/Roth.boxFamily/nlab.json) |
| nCatLab distinct namespace | site:ncatlab.org/ncatlab polynomial ring free commutative algebra finite support | Executed distinct namespace query; returned nLab pages, not a matching nCatLab page. This is an access/search limitation, not an absence theorem. | [receipt](../evidence/Roth.boxFamily/ncatlab.json) |
| Stacks Project | site:stacks.math.columbia.edu polynomial ring monomials basis arbitrary variables | Returned algebra and more-algebra material on polynomial rings; no bounded coefficient family identified. | [receipt](../evidence/Roth.boxFamily/stacks.json) |
| MathOverflow | site:mathoverflow.net integer polynomials bounded degree height counting coefficients | Heights/factor questions use coefficient bounds; no universal name for this one-sided family emerged. | [receipt](../evidence/Roth.boxFamily/mathoverflow.json) |
| Recent arXiv | site:arxiv.org multivariate polynomials bounded height counting coefficients after:2021-10-28 before:2026-10-29 | 2205.00342 describes polynomials by coefficient vectors with individual variable degree bounds; 2409.08625 counts bounded-height integer polynomials. Neither establishes this exact upstream API. | [receipt](../evidence/Roth.boxFamily/arxiv.json) |

The exact family is explicit in the local paper. A broader standard presentation fixes a set of
eligible monomials and allowed coefficients independently, treating polynomials as finite
coefficient vectors. [Bhargava et al., 2022](https://arxiv.org/abs/2205.00342) supplies a recent
example of coefficient-vector organisation; [nLab polynomial](https://ncatlab.org/nlab/show/polynomial)
supplies abstract context. Neither is claimed to name `boxFamily`. There is no evidence that this
Roth-specific name has an independent universal meaning. Historical reformulation was not
independently established by the optional unavailable channel.

## Phase 4a — generality with actual proofs

| Parameter / condition | Current form | Tested alternative and consequence |
|---|---|---|
| σ | Arbitrary `Type*`, no instances | Already includes infinite variable types and higher universes; Type and Unit checks compile. |
| r | Arbitrary σ → ℕ | Preserve for the Set definition. `σ →₀ ℕ` is useful for finite enumeration but would exclude legitimate infinite-support families. |
| Degree exponent | Natural coordinate degree | Natural exponents are intrinsic to ordinary polynomials. Replacing by arbitrary monoids defines another algebra unless a new interpretation is supplied. |
| Coefficients | ℤ | A generic family over `[CommSemiring R]` with monomial-specific allowed sets compiles; it specializes definitionally to the integer interval family. |
| B | Natural scalar cast to ℤ | The interval [0,B] is semantic input; allow arbitrary coefficient sets in a structural interface, retain the interval specialization for Roth's difference bound. |
| Finite support | No such hypothesis on the definition | Generic finite enumeration uses r : σ →₀ ℕ. The existing theorem's `[Finite (Function.support r)]` supplies exactly this bridge. |
| Nonzero / positive bounds | None | Zero belongs; B=0 gives {0} for every r, including infinite-support r. No positivity hypothesis should be added. |

Verified general interface, fully implemented in the isolated snippet:

```lean
def family {σ R : Type*} [CommSemiring R] (r : σ → ℕ)
    (t : (σ →₀ ℕ) → Set R) : Set (MvPolynomial σ R) :=
  {P | (∀ j, degreeOf j P ≤ r j) ∧ ∀ d, P.coeff d ∈ t d}
```

`family_eq_image` proves, for r : σ →₀ ℕ and finite coefficient choices t(d), that this set is
`ofCoeff '' ↑((Finset.Iic r).finsupp t)`. The proof uses `degreeOf_le_iff` and
`monomial_le_degreeOf` in both directions and handles coefficients outside the exponent box.
`family_finite` and `family_ncard` then use the existing finite-product APIs. The tested premise
`∀ d, 0 ∈ t d` is sufficient, not minimal: only monomials outside the box need0 membership to
meet the global coefficient predicate. It is automatic for the original intervals.

## Phase 4b — generality verdict

STRICTLY NARROWER as a representation of coefficient-constrained polynomials: the semiring and
allowed-set restatement is verified, not guessed. This does not by itself justify
YES-but-generalise-first: deciding whether to add that foundational family rather than transport
existing finite products is an upstream interface choice. No cost-based downgrade is used.
[Isolated full proofs and signatures](../evidence/Roth.boxFamily/isolated-executed.lean.txt),
[clean receipt](../evidence/Roth.boxFamily/isolated-receipt.json),
[actual original specialization](../evidence/Roth.boxFamily/project-executed.lean.txt),
[project receipt](../evidence/Roth.boxFamily/project-receipt.json).

Compiled guards establish that the family with σ=ℕ, r(j)=1 and B=1 is infinite (it contains the
injective family X_i), while the B=0 family is {0}. Finite support is therefore a meaningful
sufficient enumeration condition, not a definitional necessity or a necessary condition in
every degenerate case. An unconditional finite-Finset replacement would lose original content.

## Phase 4c — modern idiom, all nine rows

| # | Diagnostic | Result and actual downstream consequence |
|---|---|---|
| 1 | Typeclasses / instances | No new class needed. Generic coefficients use the existing CommSemiring hierarchy; admissible coefficient sets are data, not a typeclass. |
| 2 | Filters / topology | No: finite coefficient constraints, no limit assertion. |
| 3 | Universal properties | No additional universal-property class. Existing `coeffEquiv` already identifies polynomial coefficients. |
| 4 | Bundled substructures | Partly: support-only constraints use `restrictSupport`; the coefficient-bounded set is not a submodule. Compiled1+1 counterexample atB=1 rejects that false replacement. |
| 5 | Weaker algebraic hierarchy | Yes: generic allowed-set family over CommSemiring, without coefficient order, enables finite products for arbitrary finite alphabets. |
| 6 | Higher categories | No categorical statement to lift. |
| 7 | Concrete indices | σ is already abstract. Keep natural monomial exponents; abstract coefficient sets rather than reinterpreting ordinary polynomial degree. |
| 8 | Concrete-via-abstract | Fires for coefficient data: body has one0≤coefficient≤B line; no special arithmetic operation on ℤ is used in construction. Replacing interval membership by t(d) leaves the degree predicate intact. Generic specialization compiles. |
| 9 | False-generalization guard | Passed for generic coefficient choices. Rejected making the whole family a submodule, imposing finite support in the definition, and silently replacing the interval by a symmetric absolute bound. |

Modern idiom available: support plus coefficient-choice data, with a finite enumerator derived
through `Finset.finsupp`. This gives actual membership and product-count APIs. The named
polynomial-family layer is a proposed organisation, not an already existing primitive or an
automatically desirable addition.

## Phase 4.5 — six infrastructure risks

| Risk | Verdict | Evidence |
|---|---|---|
| Typeclass diamond | none | Set-valued def registers no instance; ordinary CommSemiring ℤ synthesis checked. |
| Reducibility leak | low | Ordinary def, no reducible attribute. Literal predicate and generic interval specialization are rfl; callers use projections from membership. |
| Noncanonical unfolding | low | The body unfolds to a conjunction of bounds; complete caller inlining succeeds. Name remains a useful semantic anchor. |
| Instance priority collision | none | No new instance or priority path. |
| Universe polymorphism | none | Native u_1 arbitrary; Unit and Type instantiations compile, generic R has independent universe. |
| Coercion ambiguity | none | Uses existing Set membership and polynomial coefficient projection; Membership synthesis verified. No custom CoeFun/CoeSort is declared. |

Overall LOW; no HIGH row. These observations do not license a new global classical instance.

## Phase 4.6 — proof strategy, all five rows

| Question | Applies? | Assessment |
|---|---|---|
| Topology ε–δ versus filters | no | No topology. |
| Element algebra versus bundled inclusions | partly | `restrictSupport` captures degree/support layer; coefficient intervals must remain a set restriction. |
| Sequences versus nets | no | No convergence. |
| Explicit construction versus universal property | no | Coefficient equivalence already exists; another class would duplicate it. |
| Missing helpers mathlib should have | possible | Generic degree-box/coefficient-product bridge is a concrete candidate; compiled here as new proof rather than assumed library API. |

Current definition strategy is MATHLIB-IDIOMATIC locally. For a reusable upstream package,
REFACTOR-RECOMMENDED: choose the general coefficient interface first and expose the finite
representation bridge. Finite counting after that bridge is existing API. This recommendation
does not reassess or inherit verdicts for the later public theorems.

## Phase 5 — all15 formal search cells

Exact requests/raw results and timings are in the linked cells. Finder's external snapshot is
v4.28.0 by default; pinned source and native checks, not external indexes, certify actual hits.
Local search returned useful source hits with `index:error`; its empty/generated-name coverage
is not trusted as proof of absence.

| Form | Lean-Finder | Loogle | LeanSearch | pinned rg | local name |
|---|---|---|---|---|---|
| Current degree/interval form | [receipt](../evidence/Roth.boxFamily/search-current-leanfinder.json) | [degreeOf](../evidence/Roth.boxFamily/search-current-loogle.json) | [receipt](../evidence/Roth.boxFamily/search-current-leansearch.json) | [receipt](../evidence/Roth.boxFamily/search-current-rg.json) | [boxFamily](../evidence/Roth.boxFamily/search-current-local_search.json) |
| Standard coefficient/support form | [receipt](../evidence/Roth.boxFamily/search-standard-leanfinder.json) | [finsupp](../evidence/Roth.boxFamily/search-standard-loogle.json) | [receipt](../evidence/Roth.boxFamily/search-standard-leansearch.json) | [receipt](../evidence/Roth.boxFamily/search-standard-rg.json) | [card_finsupp](../evidence/Roth.boxFamily/search-standard-local_search.json) |
| Abstract finite functions | [receipt](../evidence/Roth.boxFamily/search-abstract-leanfinder.json) | [support](../evidence/Roth.boxFamily/search-abstract-loogle.json) | [receipt](../evidence/Roth.boxFamily/search-abstract-leansearch.json) | [receipt](../evidence/Roth.boxFamily/search-abstract-rg.json) | [mem_finsupp_iff](../evidence/Roth.boxFamily/search-abstract-local_search.json) |

The separate overview4a web API search was also executed explicitly, using queries for
`mathlib4 bounded multivariate polynomial coefficient family Finset.finsupp restrictSupport`,
current mathlib4 documentation for `Finset.finsupp/card_finsupp`, and current mathlib4
`MvPolynomial.restrictSupport/mem_restrictSupport_iff`. Its exact requests and returned-response
digest/byte count, clean URLs, declaration locators and original summary are retained in the
[web API receipt](../evidence/Roth.boxFamily/web-api.json). The search returned current
[mathlib4 support documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/MvPolynomial/Basic.html)
for the support submodule and single uniform degree bound. For finite coefficient products it
returned a historical mathlib3 page marked synchronized with mathlib4; that is not represented
as a current mathlib4 documentation hit. Existing pinned-source/native checks remain authoritative
for `Finset.finsupp`. This additional channel confirms the candidate scope without identifying
an exact full family replacement. Root's independently opened primary-paper crosscheck is
archived in [primary crosscheck](../evidence/Roth.boxFamily/root-primary-crosscheck.json).

Pinned, full source candidates are hashed in [mathlib inputs](../evidence/Roth.boxFamily/mathlib-inputs.json).

| Candidate | Actual scope / disposition |
|---|---|
| `Finset.finsupp`, `mem_finsupp_iff`, `card_finsupp` — Data/Finset/Finsupp | Existing general finite coefficient products, exact signatures checked. They do not mention coordinate degree bounds or construct their bridge. |
| `Finsupp.card_Iic` — Data/Finsupp/Interval | Counts eligible exponent vectors for a finitely supported degree bound. It does not constrain polynomial coefficients. |
| `AddMonoidAlgebra.coeffEquiv`, `ofCoeff_injective` — Algebra/MonoidAlgebra/Defs | Exact coefficient representation/injectivity; alone supplies neither degree-box equivalence nor interval predicate. |
| `MvPolynomial.degreeOf_le_iff`, `monomial_le_degreeOf` — Algebra/MvPolynomial/Degrees | Existing pointwise degree/support laws used in the new bridge. |
| `MvPolynomial.restrictSupport`, `mem_restrictSupport_iff` — RingTheory/MvPolynomial/Basic:93,107 | Existing submodule of specified monomial support. Compiled equivalence for the degree layer; leaves all coefficient restrictions outstanding. |
| `MvPolynomial.restrictDegree` — same file:171 | A single uniform boundm, not the arbitrary coordinate functionr. Not an exact replacement. |
| `MvPolynomial.degreesLE` — Algebra/MvPolynomial/Degrees:616 | Multiset degree bounds form a submodule. Coefficient bounds still require separate set restriction. |
| `FirstOrder.Ring.mvPolynomialSupportLEEquiv` — RingTheory/MvPolynomial/FreeCommRing | Search found support-bounded polynomial families equivalent to coefficient functions. Full pinned source reviewed; useful alternative representation, not a bounded-interval family or direct replacement term. Not claimed as native imported hit. |

Conclusion: existing building blocks found; no exact full bounded-coefficient family replacement
identified. This is a search-and-probe conclusion, not a certified theorem that no possible
generic library term exists. The accepted degree/product bridge fails `rfl` and then has an
explicit new proof. No broad wildcard `exact?` search or resource-limit increase was used.

## Phase 5.5 — statement shape

Normal forms considered: (1) coordinate-degree and coefficient bounds; (2) membership in
`restrictSupport ℤ {d | ∀ j, d j ≤ r j}` plus coefficient interval membership;
(3) image of the finite coefficient product when r has finite support. The compiled support
bridge proves their degree-layer equivalence. For enumeration, existing `Finset.finsupp` is the
canonical finite-product representation; an equality to that image should orient that form to
the RHS. A general Set family must still cover infinite r.

Syntactic alternatives actually attempted: interval membership (definitionally equal), arbitrary
allowed coefficient sets (definitionally specializes), interval preimages/intersection (compiled
terminal simp), and finite image representation (compiled new proof). The current conjunction
is easiest for existing callers because h.1 supplies degree bounds and h.2 supplies both endpoint
inequalities. Preserve it locally unless a general upstream interface is selected.

Superfluous-argument audit: σ indexes variables; r supplies coordinate bounds; B supplies the
coefficient interval. Every argument changes the denoted family. No unused typeclasses or
hypotheses are present, and finiteness/positivity must not be silently added. Overall:
SHIP-AS-STATED locally; RESTATE-BEFORE-SHIP if an upstream generic coefficient-family package is
chosen. Its tested zero-membership premise is sufficient rather than claimed minimal.

## Phase 6.0 — every actual caller and inline audit

All executable occurrences lie in MainLemma; external-to-declaring-file count0. There are seven
distinct actual callers, with full original types/bodies/signatures/hashes in
[callers](../evidence/Roth.boxFamily/callers.json). Fresh ignore-independent rg and tracked Git
grep agree. The source inventory and full declaring module are retained. Counts of source
occurrences, declarations and kernel references are deliberately distinct.

| Caller (original line) | Pattern and retained hypotheses | Exact inlining / representation consequence |
|---|---|---|
| private `boxFamily_eq_image_finsupp_aux`280 | Family on LHS; finite support ofr; B arbitrary | Inline conjunction verbatim. Finite-product bridge remains a real proof using both membership directions. |
| `boxFamily_finite`301 | Family in statement; finite support ofr | Inline set; retain same image proof and hypothesis. |
| `ncard_boxFamily`311 | Family in statement; finite support ofr | Inline set; retain coefficient injectivity and cardinality calculation. |
| `exists_ne_modByMonic_eq`359 | Bounds quantified over family, two witnesses, finite subtype; finite support ofr, monicf, J,C and count | Inline in hypotheses, conclusion, Fintype and map domain. Pigeonhole proof survives with the same original signature. |
| `sub_mem_RSet`388 | Two family members, distinct; arbitraryr | Inline both hypotheses; h'.1/h''.1 degree estimates and h'.2/h''.2 interval differences remain unchanged. Nonzero follows from distinctness, not membership. |
| private `exists_mem_RSet_le_index_aux`550 | Family in hC; Fintypeσ, monic root and counting/index hypotheses | Inline bound domain; same subtraction/index proof and original signature. |
| private `exists_mem_RSet_le_index_of_rpow_bound_aux`581 | Family only inside local hC; Finm, positive degree/coefficient and rpow bounds | Inline local set with variable type inferred as Finm; coefficient and degree projections still discharge the actual proof. |

The complete MainLemma module was replayed with the definition removed and every actual use
replaced by its literal predicate. Native `isDefEq` confirms all seven original signatures; all
37 remaining declarations, including private proofs, have standard axioms only.
[Complete inline execution](../evidence/Roth.boxFamily/inline-executed.lean.txt),
[receipt](../evidence/Roth.boxFamily/inline-receipt.json).

The canonical kernel audit independently finds seven direct value consumers and six direct type
consumers: the rpow helper is a body-only consumer. This is not a transitive/simp dependency
closure. The definition has no simp attribute; a zero lexical count would not establish deadness
for a different simp API. [Exact consumers](../evidence/Roth.boxFamily/canonical-consumers.json).
Inline-derivation search found related degree/coefficient constraints in `RSet` and coefficient
norm estimates, but no separate re-derivation of the entire same one-sided family.

| Pair | Same statement? | Same construction? | Verdict |
|---|---|---|---|
| boxFamily / RSet | no: zero allowed and one-sided integer coefficients versus nonzero absolute real bound | shared coordinate degree layer only | Keep separate semantics; subtraction lemma is the intentional bridge. |
| boxFamily / Finset.finsupp image | equal only after finite-support specialization and proved degree bridge | polynomial layer versus generic finite choices | Reuse finite-product API; do not call the new bridge an existing theorem. |
| boxFamily / restrictSupport | no: support-only allows arbitrary coefficients | same degree layer, missing interval constraint | Combine with coefficient constraint if choosing that normal form. |

## Phase 6 — concrete composition experiments

1. Interval form `Box233Generic.family r (fun _ ↦ Set.Icc 0 (B : ℤ))` specializes by rfl.
   This is a newly defined generic family, not an existing mathlib call.
2. Degree predicate and intersection of coefficient interval preimages compiles by extensionality
   and terminal `simp only`. Under Phase6b this is a **trivial simp composition, BORDERLINE**;
   it does not force a NO verdict on a meaningful named family.
3. `ofCoeff '' ↑((Finset.Iic r).finsupp t)` is an existing-data expression; the full bridge to
   coordinate degree and global coefficients fails rfl and requires the archived new proof,
   including the off-box zero case. It is NOT a ≤3-existing-call replacement proof.
4. `restrictSupport` is a reusable existing representation of the degree layer. Its combination
   with interval constraints is an alternative design, not a complete existing family law.

The actual finite-support specialization uses the new generic bridge and existing
`Finset.coe_Icc`/`Finsupp.ofSupportFinite_coe` normalization. The source distinguishes this from
the original project-private bridge. Accepted mathematical proofs have no project dependencies
in the isolated run. Composition conclusion: no verified direct ≤3-existing-call term for the
full family interface; a verified trivial set/simp presentation exists, leaving semantic API
judgment under Phase6b. No cost or earlier arithmetic-definition verdict enters the decision.

## Phase 7 — rationale, action and future upstream questions

**BORDERLINE-needs-human.** The integer box is standard in the actual source and is genuinely
shared across counting, pigeonhole and subtraction. Its short definition does not eliminate the
mathematical content of the representation theorem, and `restrictSupport` cannot enforce finite
coefficient choices. Conversely, mathlib already has generic finite products and coefficient
equivalences, so adding another polynomial-specific family name without selecting its general
interface risks redundant API. A generic semiring/allowed-coefficient version and its bridge were
actually proved; upstream taste concerns what layer deserves a name, not whether those proofs
are possible or affordable.

Concrete action now: retain `Roth.boxFamily` in MainLemma as a project-local semantic definition.
Do not delete it as dead code or claim it is already `restrictSupport`. If later choosing to
inline, the seven rows above and complete verified replay provide the mechanical plan with
original signatures preserved. If choosing a new upstream family interface, use the compiled
generic signatures and keep arbitrary-variable/infinite-support Set semantics separate from
finite enumeration. A potential generic bridge home is `Mathlib/RingTheory/MvPolynomial/Basic.lean`
or a small new module importing degree and finite-Finsupp APIs; this is provisional import/API
design, not an exact approved PR proposal. No YES grouping or reviewer-selection obligation is
triggered, and no already-accepted declaration is assigned a verdict here by name alone.

Three concrete future upstream questions (none blocks the completed read-only assessment):

1. Should mathlib name a Set-valued polynomial family with arbitrary monomial-specific allowed
   coefficient sets, rather than expose only coefficient-equivalence transport lemmas?
2. Should its finite-degree-box representation theorem use `r : σ →₀ ℕ`, with function/finite-support
   versions as wrappers, or expose the original function-valued bounds directly?
3. Should the zero-membership side condition be restricted to off-box monomials and the
   integer `[0,B]` specialization remain entirely downstream?

## Phase 8 — verification and handoff

Four accepted executions: full original replay/audit, isolated generic proofs, full actual-caller
inline replay, and project specialization/composition/guards. Every accepted receipt is clean,
successful, nonpartial where that format has a partial field, with standard axioms only; raw
run_code uses diagnostics and has no partial field. All sources are exact immutable `.lean.txt`
archives including original whitespace. Failed/warming attempts are labelled separately. The
first inline draft used σ where only Finm was in scope and was rejected; the corrected inferred
variable-type replay passes, without changing production statements or raising limits.

[Verification ledger](../evidence/Roth.boxFamily/verification.json),
[portable read-only validator](../evidence/Roth.boxFamily/validate.py),
[current copy manifest](../evidence/Roth.boxFamily/copy-manifest.json).
The validator checks the current manifest, fresh17 hashes, exact293 source order and runtime
counts/consumers, exact21 isolated prefix and target absence, actual caller source hashes and
seven signature checks, all15 formal cells, every named literature channel, report links and
secret guard. Root acceptance remains pending until independent review/integration.
