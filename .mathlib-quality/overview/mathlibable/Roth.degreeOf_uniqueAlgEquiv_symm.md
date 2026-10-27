# Roth.degreeOf_uniqueAlgEquiv_symm

**BORDERLINE-needs-human.** The canonical general degree comparison already exists as
`MvPolynomial.degreeOf_eq_natDegree`; the precise singleton `uniqueAlgEquiv` rewrite law
was not located. Translating between these statements requires a separately proved
algebra-homomorphism identity and injective coefficient-map degree preservation. This is
not an existing one-call replacement. The unresolved choice is the upstream API surface,
not the correctness of the theorem or of the verified bridge.

## Phase 0 — Baseline

Canonical declaration **162/293**, public theorem, `Roth/Separation.lean:174`. The corrected
manifest agrees with the tracked order. `lake build` completed successfully with 2467 jobs;
all 17 current source/pin hashes freshly match the shared baseline. No production change
was made. [Inputs](../evidence/Roth.degreeOf_uniqueAlgEquiv_symm/inputs.json),
[build receipt](../evidence/Roth.degreeOf_uniqueAlgEquiv_symm/index-file-completion-2026-10-27.json),
[canonical metadata](../evidence/Roth.degreeOf_uniqueAlgEquiv_symm/canonical-target.json).

The declaring module separates one variable to construct the determinant factorization in
Lemma 2 of the source. It imports coefficient norm and generalized Wronskian machinery.
The full declaring module and the full explicit caller module `Roth.Theta` were read.

## Phase 1 — Mathematical content and full type

A univariate polynomial, regarded as a multivariate polynomial whose variable type has
exactly one element, has the same natural degree in that element as before. Its coefficients
and exponents are unchanged; only their indexing changes. Zero is allowed: both natural
valued degree functions assign it zero.

```lean
@Roth.degreeOf_uniqueAlgEquiv_symm : ∀ {R : Type u_1} [inst : CommSemiring R]
  {σ : Type u_2} [inst_1 : Unique σ] (f : Polynomial R),
  MvPolynomial.degreeOf default ((MvPolynomial.uniqueAlgEquiv R σ).symm f) = f.natDegree
```

`R` is a universe-polymorphic coefficient commutative semiring; `σ` is an independently
universe-polymorphic singleton variable type; `f` is arbitrary. There are no nonzero,
finite-dimensional, finite-variable, domain, field, characteristic, or decidable-equality
hypotheses. Native type, actual kernel proof body, and axiom checks are in the
[original receipt](../evidence/Roth.degreeOf_uniqueAlgEquiv_symm/unique-degree-original-audit-receipt.json).
The proof uses `MvPolynomial.coeff_uniqueAlgEquiv_symm` directly, not the preceding Roth
coefficient wrapper. It bounds exponents by `natDegree` in one direction and proves
vanishing of higher univariate coefficients in the other. Project dependencies: **none**.

## Phase 2 — Preliminary checks

SMALL: a helper degree-compatibility theorem, neither a new structure nor a named main
result. The full literature protocol still ran. The definition-only one-line/exemption
check is n/a because this is a theorem; its proof is substantive and not `rfl` glue.
The inherited-verdict shortcut does not apply. Declaration 161 is a theorem about
coefficients, not a rejected project representation definition whose laws inherit NO.

## Phase 3 — Exhaustive literature

Exact requests, hashes/byte counts of returned responses, locators, titles and concise
original summaries are retained; full web bodies are not archived.
[Eight initial queries](../evidence/Roth.degreeOf_uniqueAlgEquiv_symm/literature-individual.json),
[primary access and retry records](../evidence/Roth.degreeOf_uniqueAlgEquiv_symm/literature-primary-access.json),
[availability](../evidence/Roth.degreeOf_uniqueAlgEquiv_symm/literature-availability.json).

| Channel | Actual request / result | Interpretation |
|---|---|---|
| General web, specific | `polynomial one variable multivariate singleton degree equals univariate degree`; Magma handbook and polynomial descriptions | Degree in the chosen variable uses the same nonzero exponents. |
| General web, general | `polynomial ring iterated polynomial ring degree in one variable coefficients commutative semiring`; iterated-ring notes and monoid-ring descriptions | Grouping other variables into coefficients is the broader standard presentation. |
| General web, aliases | `degree preserving polynomial ring isomorphism relabeling variables natural degree zero polynomial` | Canonical monomial-preserving relabeling matters; arbitrary ring isomorphism is not enough. |
| ChatGPT math | n/a, `ask_chatgpt_math` unavailable in callable inventory | Optional channel unavailable; other channels unchanged. |
| Local references | Actual `rg` in `clean.tex`; Lemma 2, lines 348–435; degree bounds in §5, lines 649–657 | Disjoint-variable degree comparison and the degree constraints on the embedded univariate factor are the project use. |
| nLab | `site:ncatlab.org/nlab/ polynomial ring monoid algebra` | Abstract polynomial/free commutative algebra context. Direct `/show/polynomial+ring` gave 404; encoded-space retry inaccessible. |
| nCatLab | `site:ncatlab.org/ncatlab polynomial ring degree` | Distinct namespace actually queried; no exact singleton degree theorem identified. Out-of-namespace results do not prove absence. |
| Stacks | `site:stacks.math.columbia.edu polynomial ring degree variable` | Returned graded polynomial-ring results, not an exact theorem. Primary tag 053C gives polynomial algebras with assigned variable weights. Initial guessed tag 00CR was localization and is explicitly excluded as support. |
| MathOverflow | `site:mathoverflow.net polynomial ring degree variable isomorphism` | Arbitrary isomorphism questions are broader and do not imply this canonical map preserves degree. |
| Recent arXiv | Initial broad query returned older/unrelated material; explicit `after:2021-10-27 before:2026-10-28` retry on `"polynomial semirings"` found Ruiwen Dong, 2022, arXiv:2209.13347 | Primary abstract opened: polynomial semirings are relevant modern context, not an exact uniqueness-index degree law. |

The [local search](../evidence/Roth.degreeOf_uniqueAlgEquiv_symm/local-literature-search.json)
and [local excerpts](../evidence/Roth.degreeOf_uniqueAlgEquiv_symm/clean-excerpt.tex.txt) locate
actual source uses. The UCSD iterated-polynomial-ring lecture PDF failed with 502, and its
alternative host timed out; it is not treated as a successfully read primary proof.

Standard content: degree is the greatest exponent with a nonzero coefficient. Reindexing
one variable or regrouping the other variables into the coefficient ring preserves this
quantity. The zero polynomial has varying conventions in literature; this statement uses
natural degree zero, not the bottom-valued `Polynomial.degree` convention. No source suggests
field or domain assumptions for mere reindexing. Literature agreement is conceptual;
no external source is claimed to state this exact Lean representation law.

## Phase 4a — Parameter and hypothesis analysis

| Parameter | Role and necessity | Tested consequence |
|---|---|---|
| `{R : Type u}` | Arbitrary coefficient universe, no concrete scalar field | Native type retains independent universes. |
| `[CommSemiring R]` | Required by `MvPolynomial` and the fixed algebra-equivalence interface | The standalone `[Semiring S]` spelling of `uniqueAlgEquiv S Unit` is rejected by `#check_failure`; no weakening of that interface is claimed. |
| `{σ : Type v}` | Arbitrary singleton labels | No `Fintype`, `Finite`, or external `DecidableEq` survives elaboration. |
| `[Unique σ]` | Supplies the unique variable and default element | Bool is rejected for the equivalence; a two-variable false-generalization counterexample is proved. |
| `f : Polynomial R` | Arbitrary polynomial including zero and constants | Zero, `X^3`, and `2X²` over `ZMod 4` are checked independently. |

No extra proposition is present to drop. A choice of arbitrary `j : σ` instead of `default`
was mechanically checked in `arbitraryCoordinate`; this is equivalent syntactic generality,
not a strictly weaker assumption. No `Nontrivial R` or `f ≠ 0` is needed.

## Phase 4b — Comparison with standard generality

MAXIMALLY GENERAL within the existing singleton `uniqueAlgEquiv` interface. There is no
verified strict hypothesis weakening of that interface. The broader mathematical content
is degree in an arbitrary variable after converting the remaining variables into
coefficients; that is already the pinned `MvPolynomial.degreeOf_eq_natDegree`. The
[isolated source](../evidence/Roth.degreeOf_uniqueAlgEquiv_symm/unique-degree-isolated-executed.lean.txt)
proves the full representation bridge and then the original statement from this law.
That bridge is a new proof, not a preexisting mathlib call and not definitional equality.

## Phase 4c — Modern idiom, all nine diagnostics

| # | Diagnostic | Finding / restatement and downstream effect |
|---|---|---|
| 1 | Typeclasses rather than bundled preambles | No change: CommSemiring and Unique already use instances. |
| 2 | Filters/nets instead of sequences/metrics | No: finite polynomial coefficients and no topology. |
| 3 | Universal property instead of constructing an object | Yes for the representation bridge: equality of polynomial algebra homomorphisms is proved with `Polynomial.algHom_ext` and their values on X. This normalizes the canonical presentation. |
| 4 | Bundled substructures instead of closure predicates | No: no unbundled substructure. |
| 5 | Modules/(semi)rings instead of fields | Already CommSemiring, with actual zero-divisor example; no field/domain restriction to weaken. |
| 6 | Higher categorical statement | No categorical coherence datum or higher object is involved. |
| 7 | Generalize a concrete index | Exponents are the natural-number free-monoid indexing inherent in ordinary polynomials; arbitrary ordered monoid exponents change the object. |
| 8 | Concrete-via-abstract proof diagnostic | Yes, the named equivalence is used only through its coefficient identity in the original proof. Alternative: transport through `degreeOf_eq_natDegree` plus the new AlgHom bridge. General degree transport already exists, while the bridge's API placement is open. |
| 9 | False-generalization guard | Reject dropping singleton uniqueness or replacing the chosen canonical map by an arbitrary isomorphism. Verified `degreeOf false (X true : MvPolynomial Bool ℕ) ≠ Polynomial.X.natDegree` and missing Bool Unique guard. |

The modern route enables arbitrary selected-variable degree reasoning and coefficient
extension without redoing a support proof. Its primitive law already exists. The new
normalization helper is cheap to prove but this cost is not a verdict factor. No claim
of `YES-but-generalise-first` follows from this different representation.

## Phase 4.5 — Infrastructure risk

n/a: theorem, not a definition, instance, structure, or class. The six definition-risk
rows (typeclass diamond, reducibility leak, noncanonical unfolding, instance priority,
universe forcing, coercion ambiguity) introduce no new data or instance paths here.
The experimental bridge is also a theorem; it does not define another algebra instance.

## Phase 4.6 — Proof strategy, all five diagnostics

| # | Question | Applies? / outcome |
|---|---|---|
| 1 | ε–δ versus filters | No topology; n/a. |
| 2 | Element proof versus ideal/submodule inclusion | No ideal or submodule predicate to bundle. Coefficient-support inequalities are appropriate; the alternative AlgHom normalization is more structural. |
| 3 | Sequences versus nets/filter limits | No convergence; n/a. |
| 4 | Construct object versus universal property | Yes to using polynomial AlgHom extensionality in the presentation bridge; no new object is constructed. |
| 5 | Missing helper mathlib should have | A unique-equivalence/selected-variable conversion bridge or direct singleton degree rewrite would shorten the proof; whether either deserves a named upstream theorem is the substantive open choice. |

Current original support proof is MATHLIB-IDIOMATIC and sound. A structural alternative is
fully verified; adoption is an API design choice, not a correctness fix. The two strategies
are preserved rather than counting a newly proved helper as existing infrastructure.

## Phase 5 — Actual five-method search on all three forms

[Raw formal-search receipts](../evidence/Roth.degreeOf_uniqueAlgEquiv_symm/formal-search.json)
contain every exact query and full returned formal result. Each form has Finder, Loogle,
LeanSearch, local and source-rg evidence: 15 method/form cells.

| Form | Finder | Loogle | LeanSearch | Source rg | Local |
|---|---|---|---|---|---|
| Current singleton inverse-equivalence degree | Found nearby finSucc degree and irrelevant composition equivalences | `uniqueAlgEquiv, degreeOf`: no results | Returned degree/natDegree and `supDegree_eq_natDegree` | No unique-equivalence degree theorem located | Current project theorem and scratch replays; index unavailable |
| Standard degree invariance under singleton/iterated polynomial presentation | `degreeOf_eq_natDegree`, `natDegree_optionEquivLeft`, finSucc laws | `degreeOf, natDegree`: nearby laws | Maps preserving monomial degrees and injective coefficient maps | Equiv.lean:578, 815, 827 | `degreeOf_eq_natDegree` source hit; index unavailable |
| Abstract chosen-variable degree after option conversion | Same general option/degree laws | Both exact canonical general laws | `degreeOf_eq_natDegree`, option degree laws | Canonical law plus generic support supremum | `natDegree_optionEquivLeft` source hit; index unavailable |

An unavailable local index is not an absence proof. External indexes may have another
revision; pinned candidate signatures and actual successful proofs take precedence.
[Current source search](../evidence/Roth.degreeOf_uniqueAlgEquiv_symm/rg-current.json),
[standard](../evidence/Roth.degreeOf_uniqueAlgEquiv_symm/rg-literature.json),
[abstract](../evidence/Roth.degreeOf_uniqueAlgEquiv_symm/rg-modern.json),
[pinned native signatures](../evidence/Roth.degreeOf_uniqueAlgEquiv_symm/unique-degree-api-receipt.json).

Positive pinned building blocks, each read in source and checked natively:

- `MvPolynomial.degreeOf_eq_natDegree`, `Mathlib/Algebra/MvPolynomial/Equiv.lean:827`:
  arbitrary selected-variable degree equals natDegree after `optionSubtypeNe` renaming and
  `optionEquivLeft`; needs CommSemiring and DecidableEq, supplied classically in the bridge.
- `MvPolynomial.natDegree_optionEquivLeft`, same file:578: the transformed natDegree equals
  the original degree in `none`, including zero. `natDegree_finSuccEquiv` is a finite-label analogue.
- `MvPolynomial.coeff_uniqueAlgEquiv_symm`, same file:115: exact general coefficient law
  used in the original target proof, at every finitely supported exponent.
- `Polynomial.natDegree_map_eq_of_injective` and `MvPolynomial.C_injective`: preserve
  natDegree after the injective coefficient embedding occurring in the verified bridge.
- `MvPolynomial.degreeOf_eq_sup`, `Degrees.lean:223`, and
  `Polynomial.supDegree_eq_natDegree`, `Polynomial/Degree/Support.lean:38`: support-supremum
  formulations, also checked. They still require a representation/support bridge.

Search conclusion: **canonical analogous general law present; exact singleton target not
located; its full normalization bridge is newly proved in this assessment**. No claim
that formal-search failure proves global absence is needed for the verdict.

## Phase 5.5 — Statement shape

1. Normal form: the current `degreeOf = natDegree` equality has the useful univariate
   quantity on the RHS. The alternative existing canonical form uses arbitrary selected
   variable and a polynomial ring over the remaining variables. Full bridge checked.
2. Syntactic generality: `arbitraryCoordinate f j` eliminates a preliminary
   `Subsingleton.elim j default` rewrite for a singleton consumer. Either direction of
   `natDegree (uniqueAlgEquiv p) = degreeOf default p` is an equivalent candidate; the
   present direction matches both real callers. No extra converse theorem is required.
3. Superfluous arguments: R, CommSemiring R, σ, Unique σ, f all occur essentially in the
   fixed interface; independent universes retained; no hidden Fintype/DecidableEq/domain.

SHIP-AS-STATED is coherent if the direct rewrite theorem is accepted. If canonical
conversion bridges are preferred, organize around that representation instead; the
statement-shape choice is included in Phase 7.

## Phase 6.0 — All callers and inline audit

[Scoped no-ignore rg](../evidence/Roth.degreeOf_uniqueAlgEquiv_symm/caller-rg.json),
[tracked-source git grep](../evidence/Roth.degreeOf_uniqueAlgEquiv_symm/caller-git-grep.json),
[canonical source enumeration](../evidence/Roth.degreeOf_uniqueAlgEquiv_symm/lexical-enumeration.json),
[inline search](../evidence/Roth.degreeOf_uniqueAlgEquiv_symm/rg-inline.json).
There are three occurrences: declaration and **two explicit uses**, in two caller
declarations and two files. Excluding the declaring file, the command's count is K=1 in
one external-to-file module; counting the entire project gives K=2. These are real consumers.

| Caller | Exact role | Concrete checked refactor |
|---|---|---|
| `Roth.degreeOf_none_rename_mul_aeval`, Separation:226 | Terminal transitivity after injective variable renaming | Replace target call by new checked `canonicalRoute`, preserving generic CommRing/IsDomain hypotheses. |
| private `Roth.index_separated_mul_le_aux`, Theta:427 | Rewrite degree bound to show the embedded V lies in RSet | Replace target rewrite by new checked `canonicalRoute`; preserve full original Fintype assumption and all original `hr0`, coprimality, nonzero/degree/coefficient hypotheses. |

The exact ordered 293-name native kernel-value audit finds precisely the same two direct
consumers (including the actual private Lean name). This is separate from transitive
kernel/simp closure. No separate production inline rederivation of this exact degree law
was identified; neighboring coefficient or map-degree uses are not incorrectly counted.
The declaration is not dead code.

## Phase 6 — Actual composition experiments

The original proof is independently compiled in mathlib-only context as `oldForm` and
uses the coefficient law directly; it exceeds three existing calls. A structural proof
was also compiled:

```lean
rw [MvPolynomial.degreeOf_eq_natDegree, representationBridge]
exact Polynomial.natDegree_map_eq_of_injective (MvPolynomial.C_injective _ _) f
```

`representationBridge` is **new**, proved by `Polynomial.algHom_ext`, simplification of the
image of X using `uniqueAlgEquiv_symm_apply`, and `AlgHom.congr_fun`. Its content is:

```lean
optionEquivLeft R {b : σ // b ≠ default}
  (rename (Equiv.optionSubtypeNe (default : σ)).symm
    ((uniqueAlgEquiv R σ).symm f)) = f.map MvPolynomial.C
```

Thus the displayed two-line proof cannot justify NO-composable: it hides this new helper.
The native direct-generic and narrowly scoped negative composition diagnostics explicitly
check that a direct `degreeOf_eq_natDegree` term and the same term normalized only with
`uniqueAlgEquiv_symm_apply` do not directly have the requested type. These finite failed
attempts are not a proof of nonexistence of every possible short proof.
[Final composition source](../evidence/Roth.degreeOf_uniqueAlgEquiv_symm/unique-degree-composition-executed.lean.txt),
[clean receipt](../evidence/Roth.degreeOf_uniqueAlgEquiv_symm/unique-degree-composition-receipt.json).
An initial composition diagnostic failed because Lean omitted the section variable σ
from the theorem with conclusion `True`, leaving the tactic body with an unknown σ
and recovered `sorryAx`. The final theorem explicitly binds σ and Unique σ and has a
separate complete clean receipt. The
[rejected source](../evidence/Roth.degreeOf_uniqueAlgEquiv_symm/unique-degree-composition-rejected-executed.lean.txt)
and [rejected receipt](../evidence/Roth.degreeOf_uniqueAlgEquiv_symm/unique-degree-composition-rejected-receipt.json)
are retained solely as failed-attempt history.

Both complete caller declarations were compiled again in the real project context, with
fresh bridge/route helpers and every original assumption retained. The new caller region
contains no use of the assessed target. It still uses other project APIs legitimately;
this is caller-refactor feasibility evidence, not mathlib-only replacement evidence.
[Complete caller source](../evidence/Roth.degreeOf_uniqueAlgEquiv_symm/unique-degree-callers-executed.lean.txt),
[complete successful receipt](../evidence/Roth.degreeOf_uniqueAlgEquiv_symm/unique-degree-callers-receipt.json).

The isolated final execution has no Roth import and includes `#check_failure` for this
target. It verifies both routes, arbitrary singleton coordinate, zero, positive degree,
a coefficient zero-divisor example, Bool counterexample, and fixed-interface Semiring
rejection. [Source](../evidence/Roth.degreeOf_uniqueAlgEquiv_symm/unique-degree-isolated-executed.lean.txt),
[receipt](../evidence/Roth.degreeOf_uniqueAlgEquiv_symm/unique-degree-isolated-receipt.json).
The initial isolated attempt failed on nonexistent `MvPolynomial.CAlgHom`, missing explicit
parameters, and a simplifier argument; its source/receipt are retained as rejected evidence.
It does not establish any verification claim and its recovered `sorryAx` is never accepted.

Conclusion: **no verified existing-only ≤3-call composition**. A canonical general analogue
exists, with a genuine proved normalization bridge. This makes the question one of API
organization; it is neither automatic NO nor an automatically novel YES result.

## Phase 7 — Verdict and concrete next action

**BORDERLINE-needs-human**, all evidence complete, verification unresolved `[]`.
The exact native singleton degree law is mathematically general and has two actual uses.
The current general canonical law already covers the degree content after conversion.
Neither a cheap original proof nor an automatic parent-NO inheritance resolves whether
another rewrite law is useful upstream: there is no project representation parent here
that was rejected in favor of a more general mathlib definition.

Concrete future upstream API questions (no response required to complete this read-only
assessment):

1. Add `MvPolynomial.degreeOf_uniqueAlgEquiv_symm` to `Mathlib/Algebra/MvPolynomial/Equiv.lean`
   beside `coeff_uniqueAlgEquiv_symm` as the direct singleton rewrite API?
2. Prefer a named equivalence-normalization bridge between `uniqueAlgEquiv` and the
   `optionSubtypeNe`/`optionEquivLeft` presentation, deriving the degree law locally?
3. If adding the direct degree theorem, state it for arbitrary `j : σ` and retain the
   default-coordinate form as specialization, or use the current default form consistently
   with `uniqueAlgEquiv`?

Until resolved, retain the theorem in `Roth/Separation.lean` near the equivalent coefficient
API; no production deletion or caller rewrite is authorized by this assessment. Both
candidate caller refactors are concrete and checked. There is no proposed generalise-first
ticket and no accepted-YES grouping is needed for this BORDERLINE report. No cost-based
reason is used to pick the bucket.

## Phase 8 — Package and verification

[Verification manifest](../evidence/Roth.degreeOf_uniqueAlgEquiv_symm/verification.json),
[assessment](../evidence/Roth.degreeOf_uniqueAlgEquiv_symm/assessment.json),
[portable read-only validator](../evidence/Roth.degreeOf_uniqueAlgEquiv_symm/validate.py),
[current copy manifest](../evidence/Roth.degreeOf_uniqueAlgEquiv_symm/copy-manifest.json).
All accepted native diagnostics are complete and clean, with standard axioms only.
The canonical audit preserves exact ordered 293 names including private module names.
Source/pin hashes, manifest bytes/hashes, local links, all 15 search cells, all named
literature channels and credential guard are validated. Root acceptance remains pending
until independent review and publication; this worker changed scratch evidence only.
