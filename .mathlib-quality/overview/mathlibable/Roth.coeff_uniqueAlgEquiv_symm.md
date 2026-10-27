# Roth.coeff_uniqueAlgEquiv_symm: NO-mathlib-has-it

## Phase 0 — Baseline and resolution

The reusable baseline `lake build` succeeded; all 17 production source/pin SHA256 values were freshly checked and match the shared manifest. See [baseline](../evidence/Roth.coeff_uniqueAlgEquiv_symm/baseline-build.txt), [fresh inputs](../evidence/Roth.coeff_uniqueAlgEquiv_symm/inputs.json) and [build receipt](../evidence/Roth.coeff_uniqueAlgEquiv_symm/index-file-completion-2026-10-27.json). Canonical declaration161 is the public theorem at **Roth/Separation.lean:169–171**; initial assignment line174 is the next degree theorem. Both canonical inventories agree. [Canonical target](../evidence/Roth.coeff_uniqueAlgEquiv_symm/canonical-target.json), [corrected metadata](../evidence/Roth.coeff_uniqueAlgEquiv_symm/corrected-target.json).

The entire declaring module was read. It separates one variable, constructs determinant factors, and controls degrees and integral coefficients. The theorem is complete, with standard axioms only. Namespace-aware prefilter does not skip `Roth.coeff_uniqueAlgEquiv_symm`: the same bare spelling in namespace `MvPolynomial` is an independently assessed candidate, not the same qualified declaration.

## Phase 1 — Mathematical content and exact type

For a commutative semiring R and a one-element variable type σ, the canonical equivalence between R[X] and multivariate polynomials in σ preserves the coefficient of Xⁿ. A singleton multi-index with value n represents precisely that monomial. The proof uses the existing arbitrary-multi-index coefficient law followed by evaluation of a finitely supported singleton at its own index.

```lean
Roth.coeff_uniqueAlgEquiv_symm : ∀ {R : Type u_1} [inst : CommSemiring R] {σ : Type u_2} [inst_1 : Unique σ]
  (f : Polynomial R) (n : ℕ), ((MvPolynomial.uniqueAlgEquiv R σ).symm f).coeff (Finsupp.single default n) = f.coeff n
```

R is the coefficient type; σ is the variable type; `Unique σ` supplies a unique distinguished variable; f and n are arbitrary. Ambient τ/Fintype/DecidableEq parameters are absent in the actual type. There is no nonzero, characteristic, field, domain or finiteness hypothesis. [Native type](../evidence/Roth.coeff_uniqueAlgEquiv_symm/native-type.json), [complete native original/type/body/axiom receipt](../evidence/Roth.coeff_uniqueAlgEquiv_symm/unique-coeff-original-audit-receipt.json). No project declarations occur in the proof.

## Phase 2 — Preliminary checks

SMALL: a coefficient compatibility helper, not a main theorem, named result or new structure. One-line definition test is **n/a: theorem**, so no definition exemptions are invoked. The two-line source proof is not used as a verdict shortcut.

## Phase 3 — Exhaustive literature

| # | Channel | Exact query | Finding |
|---|---|---|---|
| 1 | Web specific | `univariate polynomial singleton variable multivariate polynomial coefficients canonical isomorphism` | Primary formalization and computational-algebra material identifies univariate polynomials with multivariate polynomials on a singleton; coefficients are finite monomial coordinates. |
| 2 | Web general | `polynomial algebra free commutative algebra one generator monomial coefficients semiring` | Free commutative algebra on a singleton is the polynomial algebra on one generator; no field-specific assumption is intrinsic. |
| 3 | Web aliases / monoid algebra | `polynomial ring monoid algebra natural numbers coefficient basis identification` | Monoid-algebra descriptions index polynomial coefficients by natural powers; exponent reindexing preserves coordinates. |
| 4 | nLab | `site:ncatlab.org/nlab/ polynomial ring free commutative algebra` | nLab polynomial entry states free algebra on one generator and free commutative algebra on a set; this supports the abstract formulation. |
| 5 | nCatLab | `site:ncatlab.org/ncatlab polynomial ring free algebra coefficient` | Explicit nCatLab namespace query attempted; returned material must not be mistaken for an exact nCatLab theorem. |
| 6 | Stacks | `site:stacks.math.columbia.edu polynomial ring coefficients monomials` | Stacks polynomial algebra material supplies arbitrary-ring multivariable setting; no independently named singleton coefficient law identified. |
| 7 | MathOverflow | `site:mathoverflow.net polynomial ring one variable free algebra monomials` | MathOverflow discusses free algebra and free module on powers of x; supporting conceptual source rather than pinned Lean evidence. |
| 8 | recent arXiv | `site:arxiv.org/abs/ polynomial semiring monoid algebra coefficients 2021 2022 2023 2024 2025 2026` | Recent arXiv 2302.02321 (2023), 2604.11569 and 2607.02874 (2026) concern polynomial semirings and evaluation; evaluation quotients differ from formal polynomial coefficient transport. |
| 9 | Local clean.tex | `V\(x_p\)`, `roth:lem6`, `R_1`, coefficients | §5 Lemma6 proof, lines734–766, uses the univariate factor as a one-variable admissible polynomial; this explains the coefficient-transport need. |
| 10 | ChatGPT mathematics MCP | Standard form, generality and historical evolution | n/a: ask_chatgpt_math is unavailable in exposed tools; no second-opinion result invented. |

The standard concept is coefficient transport under the canonical polynomial-algebra identification for a singleton variable set. [Crighton's p-adic Fields, §2.14, page63](https://www.isa-afp.org/browser_info/current/AFP/Padic_Field/outline.pdf) gives a primary formalization with a coefficientwise singleton embedding; its variable multiplicity is exactly the exponent coordinate here. This source uses commutative rings, whereas the pinned mathlib API already works over commutative semirings. [nLab polynomial](https://ncatlab.org/nlab/show/polynomial) search results describe the free algebra on one generator; direct fetch failed unsupported XHTML, so only the search finding is claimed. The explicit nCatLab query returned /nlab material, with no exact /ncatlab hit; this is a limitation, not proof of absence.

[Stacks §15.21, Lemma15.21.6](https://stacks.math.columbia.edu/tag/052Y) uses multi-index coefficient expansions over arbitrary rings; it supplies context, not this coefficient theorem. An initial guessed Stacks tag00E8 was unrelated and is excluded from mathematical support. MathOverflow supplies free-algebra/free-module conceptual background, with no named exact law. [Ajran et al., 2023](https://arxiv.org/abs/2302.02321) studies evaluation polynomial semirings and lies within 2021-10-27–2026-10-27; evaluated quotients are a different object from formal coefficient transport. No modern paper supplies a reason to change this law to a field-specific statement. Historical evolution is from ring descriptions to free-algebra and semiring formulations; no chronological priority claim is made.

All exact requests, response byte counts/SHA256 values, returned titles/locators and original concise summaries are preserved, without article/search bodies: [eight queries](../evidence/Roth.coeff_uniqueAlgEquiv_symm/literature-individual.json), [primary access](../evidence/Roth.coeff_uniqueAlgEquiv_symm/literature-primary-access.json), [precise primary locators](../evidence/Roth.coeff_uniqueAlgEquiv_symm/literature-primary-locators.json), [availability](../evidence/Roth.coeff_uniqueAlgEquiv_symm/literature-availability.json), [local search](../evidence/Roth.coeff_uniqueAlgEquiv_symm/local-literature-search.json), [local excerpt](../evidence/Roth.coeff_uniqueAlgEquiv_symm/clean-excerpt.tex.txt).

## Phase 4a — Parameters and generality

| Parameter | Need / standard form | Verified assessment |
|---|---|---|
| R : Type* | Coefficients in a semiring/ring | Arbitrary independent universe; no concrete coefficient restriction. |
| CommSemiring R | Fixed algebra-equivalence interface | General Semiring fails to instantiate this exact interface, verified by #check_failure; no mathematical impossibility for alternative ring-equivalence APIs claimed. |
| σ : Type* | A singleton variable set | Arbitrary universe; no finite enumeration required. |
| Unique σ | Exactly one variable, including its chosen inhabitant | Essential for the stated equivalence; split Subsingleton+Inhabited would repackage equivalent information. Bool counterexample rules out merely dropping uniqueness. |
| f : Polynomial R | Any finite formal polynomial | Zero included; no extra assumptions to remove. |
| n : ℕ | Power of the unique formal variable | Arbitrary n; exponent can be any d : σ →₀ ℕ using the already-existing general law. Integers would describe Laurent polynomials and change the object. |

## Phase 4b — Verified generality verdict

Within the **fixed parent interface**, coefficient and variable hypotheses are maximally general. The exponent spelling is strictly narrower than the verified standard arbitrary-d form, already provided by `MvPolynomial.coeff_uniqueAlgEquiv_symm R f d`. The accepted isolated probe proves `generalForm`, `arbitraryCoordinate`, and the full bridge `d = Finsupp.single default (d default)`. These are not conjectured weakenings or new upstream helpers. No generalise-first verdict is warranted when the expanded form is already in mathlib. [Exact accepted source](../evidence/Roth.coeff_uniqueAlgEquiv_symm/unique-coeff-isolated-executed.lean.txt), [accepted receipt](../evidence/Roth.coeff_uniqueAlgEquiv_symm/unique-coeff-isolated-receipt.json).

## Phase 4c — All nine modern idiom checks

| # | Question | Answer and concrete downstream consequence |
|---|---|---|
| 1 | Typeclasses | Already uses CommSemiring/Unique; no ad hoc preambles. |
| 2 | Filters / nets | No topology; coefficient identity is finite algebra. |
| 3 | Universal property | Parent is already bundled AlgEquiv; replacing this computation by an abstract universal-property class would lose the specified generator coordinates. |
| 4 | Bundled substructures | No closure-predicate set; no lattice/substructure improvement. |
| 5 | Hierarchy weakening | Already semiring-level; Semiring-only fixed-interface probe fails. |
| 6 | Higher categories | No categorical coherence or higher morphism content to extend. |
| 7 | General exponent index | Arbitrary finitely supported d form is verified and existing; enables direct rewrites for unknown d as in Theta:429, without singleton-normalization first. |
| 8 | Concrete-via-abstract diagnostic | Proof body contains uniqueAlgEquiv in one line only (as the existing lemma name), then singleton evaluation; the proof uses only generic coefficient transport. The diagnostic fires toward arbitrary d, but that abstract law is already present. No named special polynomial is hidden. |
| 9 | False-generalisation guard | Arbitrary d and coordinate j preserve the same object under Unique. Dropping uniqueness is rejected: Bool lacks Unique, and coefficient of X_true at singleton false1 is0 while coefficient of univariate X at1 is1. Passing to evaluated polynomial functions or integer exponents changes the object. |

Modern idiom available **and already implemented**: use the existing arbitrary-d coefficient law. It is concretely better for Theta's arbitrary-exponent bound; there is no missing modern upstream statement.

## Phase 4.5 — Infrastructure risks

All six rows are n/a because this is a theorem, with no new instance, structure, coercion or reducibility path: typeclass diamond; reducibility leak; noncanonical unfolding; instance priority collision; universe definition risk; coercion ambiguity. No new definitional equality is introduced. Existing parent-interface constraints were examined in Phase4a. Overall risk n/a.

## Phase 4.6 — Proof strategy

| # | Strategy check | Answer |
|---|---|---|
| 1 | ε–δ versus filters | No topology. |
| 2 | Elements versus substructures | Coefficients are the intended coordinate computation; ideal/submodule inclusion would obscure equality. |
| 3 | Sequences versus nets | No analysis or limiting operation. |
| 4 | Object construction versus universal property | No construction; computes a bundled equivalence already defined. |
| 5 | Missing helpers that should exist | None: the general coefficient theorem, unique-single representation and singleton evaluation are all pinned existing mathlib declarations. |

Current strategy MATHLIB-IDIOMATIC; local duplicate deletion is recommended. The pure equality-transitivity term below independently checks composition without simp-search dependence.

## Phase 5 — All five mathlib methods on three forms

| Form | Finder | Loogle | LeanSearch | rg | local name search |
|---|---|---|---|---|---|
| Current singleton coefficient | Monomial equivalence near hits | coeff_uniqueAlgEquiv | broad map/coefficient near hits | exact coeff_uniqueAlgEquiv_symm | exact spelling plus prior scratch hits; source distinguished |
| Literature singleton-algebra transport | singleton equivalence near hits | repaired query yields coefficient family | singleton parent equivalence | both coefficient directions and monomial laws | coeff_uniqueAlgEquiv family |
| Abstract arbitrary-d coordinate | monomial equivalence near hits | exact general coeff_uniqueAlgEquiv_symm | coefficient/Equiv near hits | unique_single and coefficient family | uniqueAlgEquiv family |

These are 15 mandatory cells, with two additional honest retries. The original standard Loogle query used `MvPolynomial.coeff`, which the external index rejected; first retry used `MvPolynomial.uniqueAlgEquiv, "coeff"` but was rate-limited; a later retry of that exact repaired query returned both coefficient laws. Deprecated pUnit hits and external-index aliases were not blindly accepted. Local searches can contain scratch namespace results; those are not mathlib replacements. [All actual formal requests/responses](../evidence/Roth.coeff_uniqueAlgEquiv_symm/formal-search.json), [current rg](../evidence/Roth.coeff_uniqueAlgEquiv_symm/rg-current.json), [standard rg](../evidence/Roth.coeff_uniqueAlgEquiv_symm/rg-literature.json), [abstract rg](../evidence/Roth.coeff_uniqueAlgEquiv_symm/rg-modern.json).

Pinned positive candidate at **Mathlib/Algebra/MvPolynomial/Equiv.lean:115**:

```lean
 theorem MvPolynomial.coeff_uniqueAlgEquiv_symm [Unique σ]
     (P : Polynomial R) (d : σ →₀ ℕ) :
     ((MvPolynomial.uniqueAlgEquiv R σ).symm P).coeff d = P.coeff (d default)
```

The section parameters include `(R) [CommSemiring R]`. Pinned #check signatures and the existing general theorem as a term compiled in an isolated mathlib-only environment, guarded by `#check_failure Roth.coeff_uniqueAlgEquiv_symm`. [Pinned complete source](../evidence/Roth.coeff_uniqueAlgEquiv_symm/Mathlib-Algebra-MvPolynomial-Equiv.lean.txt). No absence assertion rests on failed search.

## Phase 5.5 — Statement shape

Normal form: coefficient of inverse equivalence on the left, ordinary coefficient on the right. The reverse direction `MvPolynomial.coeff_uniqueAlgEquiv` is the corresponding forward bridge; arbitrary-d and singleton-d are equivalent via `Finsupp.unique_single`, not definitionally the same spelling. RHS normalization is respected.

Syntactic alternatives actually tried: singleton default n; arbitrary d; singleton j n for an arbitrary unique coordinate. The arbitrary-d existing statement is easiest for downstream d already in scope. Parent typeclasses R/CommSemiring/σ/Unique are used; f and n are the mathematical operands. No Fintype/DecidableEq/ambient τ are present to drop. All superfluous-argument checks pass. Overall local form is coherent, but RESTATE to the existing arbitrary-d theorem when applying it to arbitrary coefficients; no new public theorem needs shipping.

## Phase 6.0 — Complete caller and inline audit

Internal explicit uses **K=0**, external-to-declaring-file callers **0**; actual caller table is empty. Every canonical production source was freshly enumerated, with no-ignore rg and tracked git grep cross-check. An initial git grep ERE word-boundary spelling returned no matches on this platform; the preserved successful `git grep -w` retry agrees with the full lexical enumeration. Five lexical occurrences: own declaration:169, own mathlib proof:171, direct mathlib uses in degree theorem:179/182, and Theta:429. The fully qualified `MvPolynomial.*` occurrences are **not callers of the Roth wrapper**. [Enumeration](../evidence/Roth.coeff_uniqueAlgEquiv_symm/lexical-enumeration.json), [rg](../evidence/Roth.coeff_uniqueAlgEquiv_symm/caller-rg.json), [git grep](../evidence/Roth.coeff_uniqueAlgEquiv_symm/caller-git-grep.json).

Fresh canonical ordered audit: requested293, unique293, present293, values293, **zero direct kernel-value consumers** of the Roth declaration. This covers the canonical project's direct value references; it does not claim arbitrary external, opaque-kernel or simp dependency closure. [Exact canonical audit source](../evidence/Roth.coeff_uniqueAlgEquiv_symm/unique-coeff-audit-executed.lean.txt).

Inline/bypass site: `Roth/Theta.lean:429–430` rewrites coefficients at arbitrary d using the more general existing mathlib theorem and applies `hVc _`. The exact coefficient-bound subproof was independently replayed with no Roth coefficient law. [Context source](../evidence/Roth.coeff_uniqueAlgEquiv_symm/unique-coeff-context-executed.lean.txt), [receipt](../evidence/Roth.coeff_uniqueAlgEquiv_symm/unique-coeff-context-receipt.json). This verifies the coefficient branch, **not** the full Theta theorem and not a full actual caller (there are none). Nearby degree proofs similarly use the mathlib spelling; no target-specific singleton re-derivation elsewhere was found. Zero explicit usage alone is not the basis for declaring dead API.

## Phase 6 — Actual composition and bridge

The complete old form compiled without importing Roth:

```lean
(MvPolynomial.coeff_uniqueAlgEquiv_symm R f _).trans (congrArg f.coeff Finsupp.single_eq_same)
```

Two existing mathematical building blocks, plus equality congruence/transitivity; no normalization premise is omitted. The general-form theorem is exactly one existing call. The full arbitrary-exponent representation bridge was independently checked, and an arbitrary unique coordinate specialization compiled. This is not a `simp [defs...]` composition being promoted automatically to NO: the primary evidence is the **named existing exact general analogue**, and the old-form pure term confirms its specialization. No project parent lemmas are counted as mathlib building blocks.

One initial isolated attempt reversed `Finsupp.unique_single`; it failed and recovered sorryAx. It is explicitly rejected evidence, separately archived. Root corrected the orientation and removed an unused f argument before the successful run. Only the final clean source/receipt count. [Verification index](../evidence/Roth.coeff_uniqueAlgEquiv_symm/verification.json).

## Phase 7 — Actionable verdict

**NO-mathlib-has-it.** Mathlib already provides coefficient transport for every finitely supported exponent, which strictly covers the singleton spelling and matches the modern representation. `MvPolynomial.coeff_uniqueAlgEquiv_symm` at `Mathlib/Algebra/MvPolynomial/Equiv.lean:115`, together with `Finsupp.single_eq_same`, yields the exact local theorem by the compiled one-line term above. This verdict is independently verified, not inherited from proof length, parent assessment, bare-name collision or zero callers.

Recommend delete `Roth.coeff_uniqueAlgEquiv_symm` from `Roth/Separation.lean:169–171`. There are **zero explicit callers to rewrite**; preserve the fully qualified mathlib uses at Separation:179/182 and Theta:429. Future singleton-exponent consumers can use the displayed term or rewrite with the two cited mathlib facts; arbitrary-d consumers should use the existing general theorem directly. If compatibility requires a transitional named wrapper, its alternative destination is **project-local Roth/Separation.lean**, with deprecation toward the mathlib API. Archive/satellite placement and a new upstream PR add no mathematical content. No production edit is made by this assessment.

## Phase 8 — Verification and handoff

Full phases complete, unresolved requirements empty, root acceptance pending. Accepted native receipts are complete, clean, have no recovered sorryAx and use only standard axioms. Rejected attempts are separated. All293 canonical names including private terms preserve exact tracked order; all17 source/pin hashes freshly match; web bodies are not archived. [Assessment](../evidence/Roth.coeff_uniqueAlgEquiv_symm/assessment.json), [overview entry](../evidence/Roth.coeff_uniqueAlgEquiv_symm/overview-entry.json), [portable validator](../evidence/Roth.coeff_uniqueAlgEquiv_symm/validate.py), [current manifest](../evidence/Roth.coeff_uniqueAlgEquiv_symm/copy-manifest.json). Production Lean, pins, Git and overview/progress files were unchanged by this worker.
