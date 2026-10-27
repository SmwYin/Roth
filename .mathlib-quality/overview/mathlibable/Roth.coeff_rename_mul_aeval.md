# Roth.coeff_rename_mul_aeval

**BORDERLINE-needs-human.** The full scalar coefficient identity in iterated-polynomial coordinates is exactly three existing mathlib calls. The original `Option`/`rename`/`aeval` statement additionally needs a genuine coordinate transport proof. The remaining choice is whether mathlib should expose that adapter or its reusable transport API. All assessment and verification work is complete; no production edits were made.

## Phase 0 — Doctor

Declaration158 resolves at Roth/Separation.lean:123. Baseline `lake build` succeeded, and all17 production/pin hashes freshly match its manifest. The newer complete Index build also succeeded on exactly these inputs. Original native diagnostics are complete/nonpartial with no errors or warnings and only standard axioms. [Inputs](../evidence/Roth.coeff_rename_mul_aeval/inputs.json), [baseline](../evidence/Roth.coeff_rename_mul_aeval/baseline-build.txt), [full build](../evidence/Roth.coeff_rename_mul_aeval/index-file-completion-2026-10-27.json), [native receipt](../evidence/Roth.coeff_rename_mul_aeval/separated-product-coeff-original-audit-receipt.json).

The module separates the distinguished variable from the others to factor a Hasse-derivative determinant, then rescales rational factors to integral ones. Both the [entire declaring module](../evidence/Roth.coeff_rename_mul_aeval/Roth-Separation.lean.txt) and [Theta caller module](../evidence/Roth.coeff_rename_mul_aeval/Roth-Theta.lean.txt) were read.

## Phase 1 — Comprehend

Let U be a polynomial in an arbitrary family of variables xτ, and V a univariate polynomial in a different variable y, with coefficients in a commutative semiring. In U(xτ)V(y), the coefficient of xτᵃyᵇ is UₐVᵦ. The factors use disjoint variables, so there is a unique way to split the requested multi-index between them; no sum of cross terms remains.

Full native type:

```lean
@Roth.coeff_rename_mul_aeval : ∀ {τ : Type u_1} {R : Type u_2} [inst : CommSemiring R]
  (U : MvPolynomial τ R) (V : Polynomial R) (a : τ →₀ ℕ) (b : ℕ),
  ((MvPolynomial.rename some) U * (Polynomial.aeval (MvPolynomial.X none)) V).coeff
      (Finsupp.mapDomain some a + Finsupp.single none b) =
    U.coeff a * V.coeff b
```

τ and R are independently universe-polymorphic. U,V are arbitrary, including zero; a,b select the two coefficients. Only `CommSemiring R` survives elaboration: the section's `Fintype τ` and `DecidableEq τ` are omitted. There are no domain, nonzero, positivity, characteristic or finiteness premises.

Proof: `optionEquivLeft` identifies the multivariate ring with `(MvPolynomial τ R)[X]`. Under it, `rename some U` becomes the constant polynomial C U and evaluating V at X none becomes mapping its coefficients by `MvPolynomial.C`. Extract the coefficient at b, then a. The original proof uses project `coeff_coeffNone` and `coeffNone`; the independent replacement proves the exponent bridge directly and uses neither project helper. [Complete kernel/type source](../evidence/Roth.coeff_rename_mul_aeval/separated-product-coeff-original-executed.lean.txt), [independent isolated proof](../evidence/Roth.coeff_rename_mul_aeval/separated-product-coeff-isolated-executed.lean.txt).

## Phase 2 — Preliminary checks

SMALL: elementary separated-variable coefficient API, not a main theorem, named mathematical result, or new structure. The one-line definition test and its three exemptions are n/a: this is a theorem. Its proof length does not settle inclusion.

## Phase 3 — Exhaustive literature

All rows were actually searched. [Exact individual requests, response SHA256/bytes/status, titles, URLs and concise summaries](../evidence/Roth.coeff_rename_mul_aeval/literature-individual.json); [initial batched requests](../evidence/Roth.coeff_rename_mul_aeval/literature-search.json). Full web bodies are not archived. No credential-bearing returned URL required redaction.

| Channel | Exact query or locator | Finding |
|---|---|---|
| Web specific | `"polynomials in disjoint variables" coefficients product` | Research and surveys use variable-disjoint products; no independently named elementary law established |
| Web general | `"polynomial semiring" multiplication coefficient` | Coefficient convolution and scalar extraction over semirings; positive mathlib coefficient API hits |
| Web alias | `"Cauchy product" polynomial coefficients` | Cauchy product is convolution; separating variable blocks isolates one coefficient pair |
| Optional ChatGPT | `ask_chatgpt_math` unavailable | n/a; tool inventory inspected, other channels retained |
| Local references | clean.tex Lemma2 lines347–435 and Lemma6 lines734–749 | Exact project source law, applied to integrality and coefficient bounds |
| nLab | `site:ncatlab.org/nlab/show/polynomial polynomial ring` | Free commutative algebra and coefficient context |
| nCatLab | `site:ncatlab.org/ncatlab polynomial algebra coefficients` | Results were outside /ncatlab namespace, chiefly /nlab; no in-namespace exact hit |
| Stacks | `site:stacks.math.columbia.edu "polynomial ring"` | Polynomial presentations and commutative algebra chapters; no exact separated coefficient theorem established |
| MathOverflow | `site:mathoverflow.net "disjoint" "variables" polynomial coefficients` | Related variable-disjoint polynomial questions, no exact general law established |
| Recent arXiv | `site:arxiv.org/abs/ "polynomial" "disjoint variables" after:2021-10-27` | Saha 2406.05567, submitted June2024, uses polynomial rings with disjoint variables; within five years |

The local source explicitly uses that a coefficient of the product is the product of two coefficients to recover integrality from a primitive factor, then to bound the two factors' coefficients. [Lemma2 excerpt](../evidence/Roth.coeff_rename_mul_aeval/clean-separation-excerpt.tex.txt), [Lemma6 excerpt](../evidence/Roth.coeff_rename_mul_aeval/clean-theta-excerpt.tex.txt), [local query receipt](../evidence/Roth.coeff_rename_mul_aeval/local-literature-search.json).

Direct primary access was attempted for nLab, Stacks00F2, arXiv2406.05567 and mathlib docs. nLab failed because its XHTML content type is unsupported; its search excerpt was inspected. [Primary access metadata](../evidence/Roth.coeff_rename_mul_aeval/literature-primary-access.json) records this limitation. [Stacks00F2](https://stacks.math.columbia.edu/tag/00F2) supplies polynomial-presentation context, not this coefficient law. [Saha's abstract](https://arxiv.org/abs/2406.05567) confirms current disjoint-variable usage, not a new formulation of the elementary identity. [Mathlib coefficient documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Coeff.html) positively exposes coefficient-scaling APIs; pinned source and native checks settle the actual revision. No inaccessible full paper is claimed to have been read.

Synthesis: the standard content is separated-variable coefficient multiplication, equivalently the unique relevant term of coefficient convolution. Literature often states this over fields or rings; subtraction and inverses play no role. A commutative semiring already suffices. The abstract core is coefficient extraction under multiplication by a zero-index singleton in a monoid algebra. There is no mathematical disagreement between the proved forms, but the original coordinate adapter is additional API content.

## Phase 4a — Parameter and hypothesis audit

| Parameter/interface | Current form | Generality assessment |
|---|---|---|
| τ | Arbitrary Type u_1 | Already arbitrary, including empty/infinite families; no equality decision needed |
| R | Type u_2, CommSemiring | Existing `MvPolynomial` representation requires this interface; not a field/ring specialization |
| U,V | Arbitrary polynomials | No nonzero/domain restrictions; zeros allowed |
| a | τ →₀ ℕ | Natural exponents are intrinsic to ordinary polynomials |
| b | ℕ | Ordinary univariate exponent; arbitrary additive index would change representation |
| Option τ/some/none | Distinguished-variable partition | Encodes disjointness structurally; arbitrary colliding renamings do not preserve this law |
| mapDomain plus singleton | Expanded multi-index | `a.optionElim b` is equivalent through a verified, nondefinitional coordinate bridge |
| Hidden section assumptions | Fintype/DecidableEq | Absent from actual type, so nothing to drop |

## Phase 4b — Mechanically verified generality

MAXIMALLY GENERAL for the fixed polynomial interface. The isolated original-form theorem compiles with arbitrary τ and only `CommSemiring R`; it uses no project imports. No unsupported weakening to `Semiring R` for the same `MvPolynomial` type is proposed.

The underlying right-constant coefficient law is more abstract and already exists as `AddMonoidAlgebra.coeff_mul_single_zero`: arbitrary `Semiring S` and `AddZeroClass M` suffice. This exact weaker floor was separately compiled, not inferred from prose or the stronger initial `AddMonoid M` draft. [Weaker-floor source](../evidence/Roth.coeff_rename_mul_aeval/separated-product-coeff-scalar-floor-executed.lean.txt), [receipt](../evidence/Roth.coeff_rename_mul_aeval/separated-product-coeff-scalar-floor-receipt.json). This is a change of representation and an already existing law, not a mechanical single-hypothesis generalization of the original theorem. No YES-generalise verdict is inferred from it.

## Phase 4c — All modern-idiom diagnostics

| # | Diagnostic | Answer and consequence |
|---|---|---|
| 1 | Preambles to typeclasses | Already uses CommSemiring; no ad hoc algebraic hypotheses |
| 2 | Sequences/metrics to filters | n/a, finite algebraic identity |
| 3 | Construction to universal property | `optionEquivLeft` is existing algebra equivalence; hom extensionality proves its action on rename, no new universal-property class |
| 4 | Closure predicates to bundled substructures | No closure predicates present |
| 5 | Fields to modules/(semi)rings | Current law already CommSemiring; abstract coefficient core verified for Semiring |
| 6 | Higher-category restatement | No organizational improvement for this coefficient equality; tensor language is context only |
| 7 | Concrete index to additive structure | Yes for the underlying coefficient-times-singleton law: arbitrary AddZeroClass M, already mathlib; natural exponents remain essential for ordinary polynomials |
| 8 | Concrete-via-abstract | Diagnostic fires after transport: proof uses only constant/mapped coefficients and multiplication. It is exactly the full scalar three-call canonical proof below, with independent transport retained |
| 9 | False-generalization guard | Disjointness is essential: compiled collision_guard shows the coefficient of X in X·X is0 whereas the product of the two X coefficients is1 over ℕ |

Explicit Q8 body audit: there is no named concrete coefficient ring or finite dimension. After `map_mul`, rename and aeval disappear through the hom comparison and `aeval_X_left_eq_map`; the final scalar argument has no distinguished-variable geometry. The final original `mul_comm U, coeff_C_mul, mul_comm` can be replaced in canonical coordinates by existing `AddMonoidAlgebra.coeff_mul_single_zero`. This recovers the **full scalar** identity, not only its intermediate polynomial-valued b coefficient.

Modern idiom available: yes, iterated polynomial coefficient extraction and monoid-algebra right-scalar action. It composes with existing coeff/map APIs and avoids unnecessary commutations. The remaining adapter choice is meaningful for callers that already use Option-indexed Hasse exponents. Cost is not a verdict factor. [Guard and bridge receipt](../evidence/Roth.coeff_rename_mul_aeval/separated-product-coeff-isolated-receipt.json).

## Phase 4.5 — Infrastructure risk

n/a: theorem introduces no data, definition, instance or coercion. All six risk axes—typeclass diamonds, reducibility leaks, noncanonical unfolding, instance priorities, universe-forcing definitions and coercion ambiguity—are outside the scope of this declaration. Universe-polymorphic native proofs and complete original type are retained; the abstract restatement reuses existing classes rather than adding instances.

## Phase 4.6 — Proof strategy

| # | Diagnostic | Finding |
|---|---|---|
| 1 | ε–δ versus filters | n/a |
| 2 | Elements versus ideal/submodule inclusions | No inclusion statement; coefficient equality via algebra equivalence is idiomatic |
| 3 | Sequences versus nets | n/a |
| 4 | Explicit construction versus universal property | Uses existing equivalence and `algHom_ext` to identify constant embedding; no new object is constructed |
| 5 | Missing helper API | Potential reusable `optionEquivLeft` action on renamed/aeval product; canonical coefficient core itself has no gap |

REFACTOR-RECOMMENDED for a future upstream proposal: factor coordinate transport from the canonical coefficient laws, use the existing right-singleton scalar law, and choose one reusable adapter surface. This would remove repeated hom/index normalization across consumers. The design issue is not proof length or development cost.

## Phase 5 — All five actual mathlib methods

[Complete raw formal receipts](../evidence/Roth.coeff_rename_mul_aeval/formal-search.json) retain exact requests/results for all three forms. External searches can use a different mathlib revision. Local search reports index unavailable even when its source fallback returns entries; an empty result does not prove absence.

| Method | Current Option/aeval form | Literature separated coefficients | Abstract iterated/algebra form |
|---|---|---|---|
| Finder | coeff_rename_mapDomain, rename_polynomial_aeval_X partial matches | coeff_mul, coeff_prod degree formulas | coeff_C_mul, coeff_smul |
| Loogle | Initial unrecognized MvPolynomial.coeff; [successful quoted-coeff retry](../evidence/Roth.coeff_rename_mul_aeval/loogle-current-retry.json) empty | coeff_C_mul and coeff_mul_C | coeff_map and coeff_map_eq_comp |
| LeanSearch | rename coefficient correspondences | coeff_mul/convolution | coeff_C_mul, coeff_mul_C, coeff_mapAlgHom_apply |
| rg pinned source | [Current search](../evidence/Roth.coeff_rename_mul_aeval/rg-current.json): coordinate neighbors, no asserted exact hit | [Standard search](../evidence/Roth.coeff_rename_mul_aeval/rg-literature.json): scalar coefficient laws | [Abstract search](../evidence/Roth.coeff_rename_mul_aeval/rg-modern.json): map/exponent/monoid-algebra laws |
| Local name | Target and prior scratch replays, not replacements | coeff_C_mul entries | optionEquivLeft_coeff_coeff |

Pinned positive candidates were read and natively checked/used: `Polynomial.coeff_C_mul` (Algebra/Polynomial/Coeff.lean:155), `Polynomial.coeff_map` (Algebra/Polynomial/Eval/Coeff.lean), `AddMonoidAlgebra.coeff_mul_single_zero` (generated additive version of Algebra/MonoidAlgebra/Defs.lean:646–649), `MvPolynomial.optionEquivLeft_coeff_coeff` (Algebra/MvPolynomial/Equiv.lean:610), and the rename/aeval transport APIs. All pinned files are archived with [hashes](../evidence/Roth.coeff_rename_mul_aeval/mathlib-inputs.json).

Conclusion: positively found **the three building blocks for the whole canonical scalar law**, plus APIs to prove the original representation bridge. No exact original-form single theorem is asserted to have been found. Search failure is not used as proof of absence. No parent verdict is inherited; no downstream or imported scratch replay is counted as mathlib API.

## Phase 5.5 — Statement shape

Normal forms considered: original expanded mapDomain-plus-single multi-index, `a.optionElim b`, iterated polynomial double coefficient, and monoid-algebra coefficient-times-zero-singleton. Mathlib already has the canonical coefficient-scaling pieces. RHS scalar product is a suitable simplification normal form. Upstream should pick one transport adapter to avoid pairwise coordinate variants.

Syntactic generality: Option form is easiest at the existing Hasse exponent and coefficient-bound call sites; iterated form is easiest for algebraic coefficient extraction. Both complete forms were independently compiled. Neither can be substituted definitionally for the other. The original form needs no superfluous typeclass removal: τ,R,CommSemiring,U,V,a,b are all needed to express the identity, while Fintype/DecidableEq are already omitted. Overall RESTATE-BEFORE-SHIP if an upstream adapter is selected; preserving local signatures is verified below.

## Phase 6.0 — Every caller and inline audit

[Ignore-proof rg](../evidence/Roth.coeff_rename_mul_aeval/caller-rg.json), [tracked git grep](../evidence/Roth.coeff_rename_mul_aeval/caller-git-grep.json), and [canonical-source lexical inventory](../evidence/Roth.coeff_rename_mul_aeval/lexical-enumeration.json) agree: one declaration and three source uses in two caller declarations. Excluding the declaring file there are two uses in one file; within Separation there is one use. This is real reused API, not dead code.

| Source location | Caller and purpose | Concrete future refactor |
|---|---|---|
| Separation.lean:476 | private exists_int_polynomial_of_primitive_factor_aux; coefficient products are rational images of integers | Replace its `simp only` coefficient adapter with chosen upstream law, preserving integer-map normalization |
| Theta.lean:480 | index_det_le, bounds coefficients of U using nonzero V leading coefficient | Replace adapter in `rw [hF,…]`, retain casts/absolute-value and leading coefficient argument |
| Theta.lean:486 | same index_det_le, bounds coefficients of V using nonzero coefficient of U | Replace adapter in same rewrite, preserve existential coefficient selection and all hypotheses |

Both **full** original callers were replayed with all hypotheses and statements intact using a newly proved independent mathlib bridge `oldForm`. The private `index_separated_mul_le_aux` is accessed through its actual constant with a term elaborator; it is not the target theorem or a mathlib building block. The replacement `oldForm` does not use the target, parent `coeff_coeffNone`, `coeffNone`, or imported scratch replays. [Exact full caller source](../evidence/Roth.coeff_rename_mul_aeval/separated-product-coeff-callers-executed.lean.txt), [complete successful receipt](../evidence/Roth.coeff_rename_mul_aeval/separated-product-coeff-callers-receipt.json). This demonstrates feasibility, not that the newly proved bridge counts as an existing one-call replacement.

Inline audit found no independent re-derivation of this whole separated-product coefficient law. Nearby `coeff_X_none_pow_mul_rename`, expansion and derivative laws have related coordinate transport but different conclusions. [Inline search](../evidence/Roth.coeff_rename_mul_aeval/rg-inline.json).

The fresh exact ordered293 kernel-value audit retains private names and confirms293 requested/unique/present/value-bearing constants. Exactly two direct value consumers are the private integral-factor auxiliary and public `Roth.index_det_le`, matching the source caller declarations. [Audit source](../evidence/Roth.coeff_rename_mul_aeval/separated-product-coeff-audit-executed.lean.txt). These are direct kernel-value consumers, not an opaque kernel/simp dependency closure. The validator compares the complete canonical order, not only the count.

## Phase 6 — Actual composition experiments

The **entire scalar conclusion** in canonical coordinates was checked independently:

```lean
example (U : MvPolynomial τ R) (V : Polynomial R) (a : τ →₀ ℕ) (b : ℕ) :
    ((Polynomial.C U * V.map (MvPolynomial.C : R →+* MvPolynomial τ R)).coeff b).coeff a =
      U.coeff a * V.coeff b := by
  rw [Polynomial.coeff_C_mul, Polynomial.coeff_map]
  exact AddMonoidAlgebra.coeff_mul_single_zero U (V.coeff b) a
```

Exactly three existing theorem calls, with `MvPolynomial.C` definitionally the zero-index singleton in the last call. The intermediate polynomial-valued b coefficient alone is **not** counted as the theorem. [Exact full scalar source](../evidence/Roth.coeff_rename_mul_aeval/separated-product-coeff-scalar-executed.lean.txt), [receipt](../evidence/Roth.coeff_rename_mul_aeval/separated-product-coeff-scalar-receipt.json).

The old form was independently proved in the isolated source. Its additional transport includes: nontrivial hom extensionality identifying `optionEquivLeft ∘ rename some` with `CAlgHom`; `AlgHom.congr_fun`; a real `optionElim = mapDomain + single` proof using update, excluded-coordinate zero and embedding/mapDomain correspondence; conversion of aeval through an algebra hom; and evaluation at X as coefficient map. These do not reduce definitionally and are not part of the three-call scalar count. The original source also uses commutativity twice around coeff_C_mul, which the scalar proof avoids through the right-singleton law.

Thus canonical mathematical core COMPOSABLE; exact original API form is **not established as a strict ≤3-call composition**. A new bridge helper is new proof content and cannot be called one existing mathlib call. No closing `simp [defs...]` is being relabeled as automatic NO. This differs materially from a one-rewrite embedding representation change: callers currently need the full hom/aeval/index adapter.

False guard: over ℕ with the same single variable in both factors, `(X * X).coeff(single () 1) =0`, while `X.coeff(single () 1) * X.coeff(single () 1) =1`. The compiled inequality proves dropping separation is false. No extra coefficient-ring assumptions are invented to repair it.

## Phase 7 — Verdict

**BORDERLINE-needs-human.** The scalar coefficient content is already a strict three-call composition, but the actual separated-variable adapter is a coherent reusable API surface used three times in two callers. Its transport is a real proof, so neither a partial coefficient hit nor a fresh local helper justifies NO-mathlib-has-it/NO-composable for the full original form. Conversely, the existing canonical law prevents claiming new coefficient mathematics. The decision concerns upstream representation API, not expense, lack of proof verification, or inherited verdicts.

1. Should mathlib expose a coefficient theorem for separated products in Option variables, despite its three-call iterated-polynomial core?
2. Should upstream instead expose the `optionEquivLeft` rename/aeval transport law and have users derive scalar coefficients through existing coefficient APIs?

Potential upstream home is Mathlib/Algebra/MvPolynomial/Equiv.lean beside the existing Option coefficient equivalence, subject to import-layer review. If retained locally, the current theorem belongs in Roth/Separation.lean: the two caller modules use its existing exponent representation. No PR, reviewer selection, or YES-grouping is proposed before the API choice; no production change or user response is needed to complete this read-only assessment. A future selected adapter can replace all three uses as itemized above; both complete callers have already been verified under independent transport.

## Phase 8 — Evidence and validation

[Assessment metadata](../evidence/Roth.coeff_rename_mul_aeval/assessment.json), [verification index](../evidence/Roth.coeff_rename_mul_aeval/verification.json), [overview entry](../evidence/Roth.coeff_rename_mul_aeval/overview-entry.json), [portable read-only validator](../evidence/Roth.coeff_rename_mul_aeval/validate.py). All accepted native executions succeeded on the first actual run, with no recovered sorryAx, errors or warnings; standard axioms only. Preparations are separately labelled and not accepted as execution evidence. Raw disk receipts retain historical diagnostics; target checks are scoped to fresh native regions while errors/warnings/axioms are checked over the full receipt. Original kernel print is complete, with no elision marker. Production files, pins, Git and progress remained untouched. Root acceptance is pending independent review.
