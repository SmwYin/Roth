# MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero — full mathlibable assessment

Verdict: **YES-add-as-is**, with the canonical multivariate Hasse derivative API. Multiplication by a polynomial independent of all differentiated variables commutes with the Hasse operator. This is useful over arbitrary commutative semirings, including positive characteristic. No production Lean or pins are changed by this assessment.

## Phase 0 — baseline and resolution

The shared `lake build` succeeded, exit 0, 2467 jobs: [baseline-build.txt](../evidence/MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero/baseline-build.txt). All 17 source/pin hashes freshly match it: [baseline-fresh-check.json](../evidence/MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero/baseline-fresh-check.json). The declaration resolves at `Roth/HasseDeriv.lean:243`. The complete declaring module and `Roth/Separation.lean`, containing both explicit calls, were read, together with Taylor's related coefficient argument. [Source hashes](../evidence/MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero/source-hashes.json) and [required reference hashes](../evidence/MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero/reference-hashes.json) record exact inputs. Native proofs and axioms are listed in Phase 6.

## Phase 1 — comprehend

Let R be any commutative semiring, σ any variable type, and d a finitely supported natural multi-index. If a polynomial f has degree zero in every variable occurring in d, then Δ_d(fg)=fΔ_d(g) for every polynomial g. The factor f can contain arbitrarily many other variables and need not be a scalar, nonzero, or invertible. Empty support d=0 and zero factors are covered.

Type, up to universe names: `∀ {σ R : Type*} [CommSemiring R] {d : σ →₀ ℕ} {f g : MvPolynomial σ R}, (∀ j ∈ d.support, degreeOf j f = 0) → hasseDeriv d (f * g) = f * hasseDeriv d g`. The actual native `#check` retains the elaborated universe-polymorphic type. The proof expands f into its supported monomials, uses linearity and distributivity, then invokes the private monomial factor lemma. For each occurring exponent a, the degree premise forces a j=0 on d.support. For monomial g with exponent b, `(a+b)-d=a+(b-d)` and `hasseCoeff d (a+b)=hasseCoeff d b`; coefficient commutativity finishes. [Exact source](../evidence/MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero/target-source.lean.txt).

Project dependencies: `hasseDeriv`, `hasseDeriv_monomial`, `hasseCoeff`, and the private `hasseDeriv_monomial_mul`; the latter's SKIP-private assessment does not make its proof an existing mathlib replacement. Mathlib supplies `as_sum`, sums and linear-map additivity, `monomial_le_degreeOf`, monomial multiplication and pointwise finite-support arithmetic.

## Phase 2 — preliminary checks

SMALL: basic operator API, not a new structure or main theorem. The one-line-definition test and its exemption rows are n/a because this is a theorem. Its short public proof hides a substantive monomial compatibility argument; proof length alone does not establish composability. No prefilter applies.

## Phase 3 — exhaustive nine-channel literature

[Exact web request metadata, returned-response SHA256, bytes and statuses](../evidence/MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero/web-receipts.json); [source locators and original concise summaries](../evidence/MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero/web-sources.json). Full web bodies are deliberately not retained.

| Channel | Actual request/check | Finding and limitation |
|---|---|---|
| Web specific | `multivariate Hasse derivative product independent variables constant factor` | Polynomial Hasse product law and binomial monomial action. |
| Web general | `Hasse Schmidt derivation constants subalgebra product rule arbitrary characteristic` | General higher derivations satisfy the convolution product identity; a factor killed by every positive component in the relevant directions passes through. |
| Web aliases | `higher divided derivatives polynomial disjoint variables Leibniz rule` | Divided derivatives and multi-index Leibniz rule are standard aliases. No factorial division is needed in the algebraic definition. |
| ChatGPT MCP | Available-tool inventory | n/a: `ask_chatgpt_math` unavailable; no external mathematical second opinion claimed. |
| Local | `clean.tex` §1 lines115–153 and §2 lines350–435 | Defines canonical multi-index operators; separated determinant computation uses factorwise derivatives of products in disjoint variable blocks. [Receipt](../evidence/MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero/literature-local.json). |
| nLab | Site query and direct Hasse–Schmidt derivative open | Indexed several-indeterminates definition works over a commutative rig. Direct fetch rejected XHTML content type; no successful direct-page fetch claimed. |
| nCatLab | Dedicated `site:ncatlab.org/ncatlab Hasse Schmidt derivation` query and `/ncatlab/show/Hasse-Schmidt+derivation` open, plus related derivation page | Dedicated categorical namespace search checked separately from nLab. Direct dedicated-page fetch failed; no higher-categorical factor-independence replacement obtained. Related derivation page provides context only. |
| Stacks | Site search; tag09CH direct open | §10.133 defines differential operators via commutators and principal parts. This is broader relative linearity, not an existing canonical Hasse normalization theorem. |
| MathOverflow/MSE | Site MathOverflow queries, derivations-tag result, MSE4527839 direct open | Discovery channel; MSE's question uses ordinary first derivatives under Hasse terminology. Its answer explicitly flags the naming mismatch; excluded as proof of arbitrary-order identity. |
| Recent arXiv, last five years | 2022–2026 query; 2509.00887v2 and 2409.19093 direct opens | Miyamoto2025 §2 gives higher derivations in positive characteristic; Bravo–Tirado Hernández2024 studies integrability. Neither is asserted to print the exact degree-zero corollary. 2605.20664 is a recent adjacent generalization, not target proof evidence. |

Primary reference [Fernández-Lebrón–Narváez-Macarro, §1.1](https://personal.us.es/narvaez/HS-web.pdf) defines higher derivations over commutative unital rings, their convolution product law and corresponding power-series algebra homomorphism. The target follows for canonical directional Hasse operators because independence kills all nonzero differentiated components of f; this implication is the assessment's reasoning, not a claimed verbatim theorem. [Miyamoto2025, §2](https://arxiv.org/html/2509.00887v2) confirms continuing use of Hasse–Schmidt operators where factorial division fails. [Stacks09CH](https://stacks.math.columbia.edu/tag/09CH) supplies the relative differential-operator viewpoint. The rig-level canonical monomial formula appears in [nLab's indexed definition](https://ncatlab.org/nlab/show/Hasse-Schmidt+derivative).

Literature summary: this is the constant-factor rule for canonical higher divided partial derivatives, equivalently linearity over the polynomial algebra in the undifferentiated variables. General Hasse–Schmidt systems allow arbitrary algebras and maps, but then the premise must assert vanishing of all relevant positive components or a relative coefficient-algebra structure; plain R-linearity does not yield the target. The current degree premise expresses genuine variable independence over all characteristics. No disagreement in canonical mathematical content; finite printed variable sets extend naturally to arbitrary σ using finite supports.

## Phase 4a–b — parameter and generality audit

| Parameter or premise | Audit |
|---|---|
| σ : Type* | Arbitrary universe-polymorphic variable type; no finiteness, nonemptiness or DecidableEq premise. Classical proof implementation does not impose an API hypothesis. |
| R : Type* | Arbitrary coefficients, no fixed characteristic or nontriviality. |
| CommSemiring R | Parent `MvPolynomial σ R` and the R-linear operator require this interface. The independent raw proof retains it; literal Semiring-only MvPolynomial is rejected in native guard. A different monoid-algebra representation is a parent-definition development, not a local hypothesis drop. |
| d : σ→₀ℕ | Arbitrary finite-support derivative order, including zero. Replacing naturals by an arbitrary monoid would change canonical binomial differentiation. |
| f | Arbitrary factor, including zero, allowed to involve variables outside d.support. Cannot require scalar-only f without losing current callers. |
| g | Entirely unrestricted polynomial, including zero. |
| hf | Sufficient coordinate independence condition. Equivalent to `Disjoint d.support f.vars`; no strict weakening is claimed by that repackaging. The compiled support variant and symmetric factor variant are companions. |

MAXIMALLY GENERAL within the canonical fixed-parent interface; no verified hypothesis/typeclass drop or strictly weaker local premise established. A generalized Hasse–Schmidt product-law theorem with vanishing intermediate components is mathematically broader, but would first require a new parent abstraction and its canonical instance. It is not a mechanical weakening of this signature or an existing mathlib replacement.

The degree-zero premise cannot be dropped. It also cannot be replaced by `pderiv j f=0` in arbitrary characteristic: over ZMod2, f=X² has ordinary first partial derivative zero, but Δ₂(f·1)=1 while f·Δ₂1=0. The native counterexample is retained. Vanishing of Δ_d f alone is likewise not enough in general: over ℕ, f=g=X and d=2 give Δ₂ f=0 but Δ₂(fg)=1 whereas fΔ₂g=0. This additional native counterexample verifies the intermediate-cross-term guard. No invalid widening is proposed.

## Phase 4c — nine modern-idiom rows

| # | Question | Finding and downstream consequence |
|---|---|---|
| 1 | Typeclasses | Already hierarchy-parametric. A class asserting this one factor condition would obscure an easily supplied local hypothesis. |
| 2 | Filters/nets | n/a, finite algebraic identity. |
| 3 | Universal property | Relative polynomial algebra gives a conceptual proof, but needs a proved transport/normalization of the Hasse operator; not obtained just by freeness. |
| 4 | Bundled substructure | Could bundle independent polynomials as the subalgebra generated by X j outside d.support; the theorem then asserts linearity over that subalgebra. This packages repeated scalar actions, but no current caller needs a new linear-map instance. Keep the direct rewriting API. |
| 5 | Module/semiring hierarchy | Already commutative-semiring level, stronger generality than field-only literature. A scalar extension to the undifferentiated subalgebra requires actual compatibility, not automatic map_smul. |
| 6 | Higher categories | No concrete higher-categorical downstream use located. The categorical context in nLab is adjacent, not a replacement proof. |
| 7 | Index generality | σ already arbitrary. Natural polynomial exponents/binomial orders are intrinsic; group exponents create a Laurent theory. |
| 8 | Concrete-via-abstract diagnostic | Fires: 0 exact `hasseDeriv` identifiers in the public body, helper substring on 1 line. Generic finite-sum extension from monomial compatibility is the abstract remainder; compatibility itself remains Hasse-specific. |
| 9 | False-generalization guard | Reject ordinary derivative-zero, plain R-linearity and arbitrary higher-derivation-without-constants-premise replacements. Equivalent vars-disjoint and symmetric-side forms preserve the operator and premise. |

[Q8 diagnostic](../evidence/MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero/q8-diagnostic.json). Abstract restatement tested: if T is R-linear and `∀ a ∈ f.support, T (monomial a (f.coeff a)*g)=monomial a (f.coeff a)*T g`, then `T(f*g)=f*T g`. This identifies reusable finite-sum proof organization, with its full normalization premise retained. It does not remove or prove the Hasse-specific monomial law. The generic reduction uses existing finite-sum linearity; no new mandatory public abstraction with demonstrable downstream gain over those primitives is established. Modern-idiom verdict: no required mathematical restatement; optional subalgebra packaging and vars corollary are useful later companions.

## Phase 4.5 — six infrastructure risks

All six n/a for a theorem: no new instance/typeclass diamond; no data-definition reducibility leak; no definitional unfolding equation; no instance-priority collision; no new universe restriction (native polymorphic type checked); no coercion declaration. Parent definitions were assessed separately.

## Phase 4.6 — five proof-strategy rows

| # | Question | Finding |
|---|---|---|
| 1 | Topology ε–δ versus filters | n/a. |
| 2 | Elements versus subobjects | Subalgebra-relative linearity is a conceptual organization, but the current pointwise equality is precisely what callers rewrite. Monomial reduction proves its substantive compatibility transparently. |
| 3 | Sequences versus nets | n/a. |
| 4 | Constructed object versus universal property | No object is constructed. A freeness argument would still need the Hasse normalization bridge. |
| 5 | Missing helpers that should be in mathlib | Multivariate Hasse product compatibility is missing. General multivariate Leibniz API would derive this from vanishing positive derivatives; useful follow-up, not an existing primitive to cite. Private monomial compatibility may stay private in the upstream module. |

MATHLIB-IDIOMATIC: linearity, monomial multiplication and supportwise exponent arithmetic. An eventual complete multivariate Leibniz theorem could make this a corollary, but does not invalidate a directly proved standard factor API. No cost-based verdict routing.

## Phase 5 — five actual mathlib methods across three forms

| Method | Current form | Literature-standard form | Abstract form |
|---|---|---|---|
| Finder | Multivariate Hasse derivative f*g with degree-zero factor | Hasse–Schmidt constant-factor higher product law | Linear map commutes with polynomial factor in disjoint variables |
| LeanSearch | Same exact current query | Same higher-derivation query | Same relative-linearity query |
| Loogle | `MvPolynomial.degreeOf, _ = 0` | `Polynomial.hasseDeriv, _ * _` | `LinearMap.map_smul` |
| rg | `hasseDeriv.*mul` and degreeOf variants over pinned tree | Hasse–Schmidt/higher derivations, hasseDeriv_mul and pderiv_mul | map_mul_algebraMap, map_smul, linearMap_ext, vars/degree equivalence |
| local | `hasseDeriv_mul_of_degreeOf_eq_zero` | `hasseDeriv_mul` | `LinearMap.map_mul` |

[Finder/LeanSearch complete raw receipts](../evidence/MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero/search-raw.json), [Loogle](../evidence/MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero/loogle-raw.json), [local](../evidence/MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero/local-raw.json), [full qualified-name search](../evidence/MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero/full-name.json), [current rg](../evidence/MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero/rg-current.json), [literature rg](../evidence/MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero/rg-literature.json), [abstract rg](../evidence/MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero/rg-abstract.json). Local index reports unavailable; source fallback finds target and univariate analogue, not independent absence certification. External indexes can differ from the project pin.

Positive candidates: `Polynomial.hasseDeriv_mul` in `Mathlib/Algebra/Polynomial/HasseDeriv.lean:211` states the full univariate antidiagonal convolution. `MvPolynomial.pderiv_mul` in `Mathlib/Algebra/MvPolynomial/PDeriv.lean:110` is first-order Leibniz. `LinearMap.map_algebraMap_mul`/`map_mul_algebraMap` in `Mathlib/Algebra/Algebra/Basic.lean:256,260` handle coefficients from the chosen scalar ring. `LinearMap.map_smul` similarly handles R-scalars, not arbitrary polynomials with other variables. `MvPolynomial.linearMap_ext` reduces linear-map equality to monomials but supplies no compatibility. `mem_vars_iff_degreeOf_ne_zero` in Variables.lean:148 identifies the equivalent support premise. Native pinned checks retain exact signatures.

Conclusion: partial analogues and generic building blocks exist; no existing canonical arbitrary-multi-index factor-passing theorem or ≤3-existing-call derivation found. This conclusion combines pinned source inspection and actual normalization experiments; search failures are not proofs of absence.

## Phase 5.5 — all statement-shape checks

Normal form OK: `Δ_d(f*g)=f*Δ_d g` rewrites a compound differentiated product into a simpler expression. Equivalent presentations include commuting the operator with left multiplication, `Disjoint d.support f.vars`, and linearity over the undifferentiated coefficient subalgebra. No existing canonical multivariate theorem chooses another normal form. Symmetric right-factor variant follows by commutativity, with the same premise on the independent factor f now on the right: Δ_d(g*f)=Δ_d(g)*f.

Syntactic generality OK: the native vars-disjoint equivalence is tested. The two actual callers already produce degreeOf=0 by simp on renamings; forcing vars disjointness would add support membership bookkeeping. Keep hf and implicit d,f,g, with optional vars-disjoint and right-factor corollaries. Superfluous arguments NONE: all σ,R,CommSemiring,d,f,g,hf audited above; no Fintype or characteristic constraint. Overall SHIP-AS-STATED.

## Phase 6.0 — full explicit caller and inline audit

Internal use count 2; one external-to-declaring-file module and one enclosing theorem. [Caller receipt](../evidence/MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero/callers.json), [exact excerpt](../evidence/MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero/caller-separated.lean.txt).

| Caller | Instantiation and role | Action |
|---|---|---|
| `Roth/Separation.lean:157`, `Roth.hasseDeriv_rename_mul_aeval` | d=single none ν, f=rename some U. Differentiate the none-variable factor while retaining U; degree of rename some U at none is zero. | Retain theorem as direct rw rule; inline would expand U into monomials and duplicate its compatibility proof. |
| `Roth/Separation.lean:161`, same theorem | d=mapDomain some d, f=aeval X none (hasseDeriv ν V) after mul_comm. Pass the none-only factor through derivatives in some j; `hnone` excludes none from support. | Retain theorem; equivalent vars premise is possible but currently less direct than degree simplification. |

This is explicit source-reference enumeration, not opaque kernel/simp closure. The theorem is not tagged simp. [Inline audit receipt](../evidence/MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero/inline-audit.json): private monomial factor argument is its proof leaf; Hasse composition for disjoint derivative supports concerns Δ_dΔ_e rather than polynomial multiplication. Taylor's `coeff_aeval_X_mul` is a different coefficient-factor statement with a univariate factor, not a bypassed implementation of this operator identity. No extra exact inline copy located. No junk finding: the two calls assemble factorwise separated derivatives used by the determinant factorization.

## Phase 6 — actual composition experiments and verification

[Verification manifest](../evidence/MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero/verification.json) lists exact executed source archives, native requests/results, source checks and rejected attempts separately. Accepted native results are complete (`partial=false`), have no errors or warnings, and printed axioms are restricted to propext, Classical.choice and Quot.sound.

1. Exact public proof replay uses `f.as_sum`, finite-sum distributivity and map_sum, calling a separately replayed private monomial factor proof. It does not call the target itself.
2. Vars-disjoint equivalence and symmetric right factor are actually checked. ZMod2 X² counterexample rejects replacing independence by first partial-derivative vanishing.
3. Isolated mathlib-only replay defines the full raw operator, independently proves its monomial action and monomial-product compatibility by induction, and extends to general f by its support sum. No Roth import; `#check_failure` guards missing project targets. This is substantive new proof, not a ≤3-existing-call composition.
4. Generic R-linear finite-sum extension is checked with full monomial-compatibility premise. Scalar map_smul and map_mul_algebraMap supply only scalar constants; they do not discharge the premise for arbitrary undifferentiated polynomial factors.
5. Both Option-block factor/support rewrites are checked at arbitrary-semiring types: `none_block` retains `rename some U`, and `some_block` retains a none-only polynomial represented by `rename (fun _ : Unit ↦ none) Q`. The latter is the standard univariate embedding shape used after `aeval_X_eq_rename` in the caller. No full Separation module rebuild is claimed. Univariate product law and pderiv product law are pinned positive analogues but need a multivariate transport/development, with characteristic-sensitive distinctions retained.

Conclusion NOT-COMPOSABLE from ≤3 existing pinned mathlib calls. The project-private helper and newly proved raw/generic helper are not counted as existing mathlib. No closing `simp [definitions...]` composition established; if one were established, Phase6b would require BORDERLINE rather than automatic NO. Prior unrelated exact? timeout is not repeated or used as absence evidence.

## Phase 7 — actionable verdict and gate

**YES-add-as-is.** The concrete gap is multiplication compatibility of the canonical multivariate Hasse operator with a factor independent of its differentiated variables. Existing univariate Hasse Leibniz and first-order multivariate pderiv Leibniz do not express this arbitrary-multi-index, characteristic-free relative constant-factor rule. It composes with renaming and aeval to compute derivatives of separated products and hence determinant entries, as the two genuine calls demonstrate. It is a standard API consequence with substantive monomial arithmetic, not a new research theorem and not merely an R-scalar map_smul wrapper.

Keep the current degree-zero rewriting interface; optionally add the verified vars-disjoint and symmetric-side corollaries. Keep the monomial compatibility helper private unless broader use warrants exposing it. A future full multivariate Leibniz theorem is worthwhile API; do not describe it as already available. Broader higher-derivation bundles are a separate parent-interface design, and invalid first-derivative-zero widening is expressly rejected.

Proposed upstream path: `Mathlib/Algebra/MvPolynomial/HasseDeriv.lean`. PR title: `feat(Algebra/MvPolynomial): add multivariate Hasse derivatives and independent-factor rule`. Group with actually accepted YES declarations in progress.json: `MvPolynomial.hasseDeriv`, `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseDeriv_map`, `MvPolynomial.hasseDeriv_rename`, `MvPolynomial.hasseDeriv_hasseDeriv`, `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`, `MvPolynomial.pderiv_hasseDeriv`, `MvPolynomial.degreeOf_hasseDeriv_le`, `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`. Do not classify related NO/private declarations as accepted YES.

Before PR: run `/generalise MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero`; run `/cleanup Roth/HasseDeriv.lean MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero`; choose reviewers from actual recent relevant commits. [Commit evidence](../evidence/MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero/reviewer-commits.json): Moritz Firsching authored HasseDeriv map API commit334438d (2026-08-19); Aaron Liu authored variables universal property7c345ee (2026-09-03); Yaël Dillies authored MvPolynomial coefficient refactor631b214 (2026-09-02). These are reviewer candidates, not claims of willingness or maintainer appointment. Alternative local destination if upstream design is deferred: keep `Roth/HasseDeriv.lean` beside the parent operator, preserving both Separation calls; Archive is less suitable for reusable polynomial API.

Gate: all required literature/search/generality/modern-idiom/strategy/shape/caller/composition artifacts present. No cost-based downgrade, unsupported verified weakening or private-helper-as-existing claim. Root independently reviews before integration; no external publication or production refactor is performed by this package.

## Phase 8 — handoff

Retain the theorem and prepare the grouped canonical Hasse API contribution through the generalise/cleanup checklist. [Assessment metadata](../evidence/MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero/assessment.json), [overview entry](../evidence/MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero/overview-entry.json), [portable read-only validator](../evidence/MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero/validate.py), and [current copy manifest](../evidence/MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero/copy-manifest.json) complete the reviewable handoff. Historical worker manifests, if preserved after integration, do not replace current-manifest validation.
