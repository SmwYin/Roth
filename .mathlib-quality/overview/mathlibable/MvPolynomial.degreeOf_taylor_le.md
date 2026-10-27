# Full mathlibable assessment: `MvPolynomial.degreeOf_taylor_le`

Canonical declaration **69/293**, `Roth/Taylor.lean:170–173`. Verdict **YES-add-as-is**: coordinate-degree control for multivariate constant translations, over arbitrary commutative semirings. The assessment changes no production Lean source.

## Phase 0: baseline and scope

Baseline `99f19fda4b3cbee38fc0d31af76075834f5cc265` built successfully, 2467 jobs, exit0, no warnings/errors. The fresh seventeen source/version-pin hashes match that baseline ([build](../evidence/MvPolynomial.degreeOf_taylor_le/baseline-build.txt), [inputs](../evidence/MvPolynomial.degreeOf_taylor_le/inputs.json), [check](../evidence/MvPolynomial.degreeOf_taylor_le/input-hash-check.json)). Target, independent proof, actual caller, stronger ring consequence, and raw mathlib routes were checked natively by root. Source and dependency versions remain unchanged; scratch evidence is distinct from production modules.

## Phase 1: comprehension

Replacing every variable by itself plus a constant cannot increase the highest exponent of any chosen variable. The result includes the zero polynomial, whose natural coordinate degree is zero, and requires neither a domain nor characteristic zero. Every translated monomial has exponents bounded coordinatewise by its original exponent; the implemented proof captures this through Taylor coefficients and Hasse-derivative vanishing.

Full native type, with independent universes:

```lean
∀ {σ : Type u_1} {R : Type u_2} [CommSemiring R]
  (α : σ → R) (j : σ) (P : MvPolynomial σ R),
  MvPolynomial.degreeOf j (MvPolynomial.taylor α P) ≤ MvPolynomial.degreeOf j P
```

The entire [Taylor module](../evidence/MvPolynomial.degreeOf_taylor_le/Taylor-module.lean.txt) and [Index caller module](../evidence/MvPolynomial.degreeOf_taylor_le/Index-module.lean.txt) were read. Exact native signature, printed proof, axioms and independent proof constants are in [target receipt](../evidence/MvPolynomial.degreeOf_taylor_le/native-target-success.json). Direct project dependencies are `taylor`, `coeff_taylor`, and `hasseDeriv_eq_zero_of_degreeOf_lt`. For a supported exponent e exceeding the old j-degree, the last lemma kills the Hasse derivative, the coefficient Taylor identity kills the translated coefficient, and support membership gives a contradiction. `degreeOf_le_iff` converts these pointwise exponent bounds into the degree inequality.

## Phase 2: preliminary checks

**SMALL**, a structural degree lemma, not one of the module's named main expansion theorems or a new data structure. Phase2b **n/a**, theorem rather than one-line definition. Its three-line proof is not a three-mathlib-call composition: the two essential Hasse/Taylor results belong to this project. Qualified-name [search](../evidence/MvPolynomial.degreeOf_taylor_le/rg-full-name.json) has no pinned mathlib declaration of this name; that fact alone does not establish mathematical absence. Parent `taylor` was BORDERLINE, but this theorem is not definitional glue and receives independent assessment.

## Phase 3: exhaustive literature search

Actual requests, response hashes/byte counts, stripped safe URLs and original summaries: [three general searches](../evidence/MvPolynomial.degreeOf_taylor_le/web0-metadata.json), [named channels](../evidence/MvPolynomial.degreeOf_taylor_le/web1-metadata.json), [follow-ups and primary access](../evidence/MvPolynomial.degreeOf_taylor_le/web2-metadata.json), [direct-source follow-up](../evidence/MvPolynomial.degreeOf_taylor_le/web3-metadata.json). Full returned search/article bodies are not archived; all returned URL queries/fragments are stripped.

| Channel | Actual query or check | Result and limitation |
|---|---|---|
| Web specific | `multivariate polynomial translation individual degree does not increase` | Shift-equivalence work and degree discussion. No stand-alone exact lemma established solely from search snippets. |
| Web general | `polynomial substitution coordinate shifts preserve multidegree commutative ring` | Polynomial substitution context. Some “multidegree” results concern module/ideal invariants, a different concept; excluded. |
| Web aliases | `shift equivalence polynomial individual degree invariant` | Shift-equivalence definitions, including Dvir–Oliveira–Shpilka's [2014 primary paper](https://arxiv.org/abs/1401.3714). This is context, not claimed to prove the target over semirings. |
| Optional ChatGPT math | `ask_chatgpt_math` | Unavailable and optional; skipped without reducing other searches. |
| Local reference | `clean.tex`, Taylor/degree/exponent search | Taylor expansion at lines501–533 has coordinate box bounds; translated coefficients identified at546–548; lines650–667 use the box to bound index by variable count. [Excerpt](../evidence/MvPolynomial.degreeOf_taylor_le/clean-excerpts.tex.txt), [source hash](../evidence/MvPolynomial.degreeOf_taylor_le/local-literature.json), [complete search](../evidence/MvPolynomial.degreeOf_taylor_le/rg-local-literature.json). |
| nLab | `site:ncatlab.org/nlab polynomial degree filtration translation` | [Degree of a polynomial](https://ncatlab.org/nlab/show/degree+of+a+polynomial) distinguishes partial degree/left shifts and characteristic-sensitive derivative criteria. Search-index text available; direct fetch failed unsupported XHTML. No characteristic-zero restriction transferred to Hasse derivatives. |
| nCatLab | `site:ncatlab.org/nlab symmetric algebra filtered affine translation` | [Filtered object](https://ncatlab.org/nlab/show/filtered+object) and symmetric-algebra/algebra-modality context. Direct filtered-object access failed unsupported XHTML. A filtered substitution map is an organizational alternative, not an existing proof of its required preservation property. |
| Stacks | `site:stacks.math.columbia.edu polynomial substitution degree translation`; follow-up polynomial-ring universal-property query | Initial groupoid-scheme hits are not target evidence; follow-up divided-power/universal-thickening hits also differ. Direct [05G3](https://stacks.math.columbia.edu/tag/05G3), remark after Definition10.14.1, gives polynomial-presentation substitution under base change, not coordinate-degree translation law. |
| MathOverflow | `site:mathoverflow.net polynomial translation individual degree`; follow-up `site:mathoverflow.net "polynomial" "translation" "degree"` | Direct [conjugate-polynomial discussion](https://mathoverflow.net/questions/53610/which-polynomials-arise-as-formulas-for-a-conjugate), answer opening, uses translation/dilation normalization. No exact multivariate degree lemma established; not used as proof verification. |
| Recent arXiv within five years | `site:arxiv.org shift equivalence polynomials 2022 degree` | [Chen–Du–Fang2204.06968](https://arxiv.org/abs/2204.06968) submitted14April2022; v1/search title *Shift Equivalence Testing of Polynomials and Symbolic Summation of Multivariate Rational Functions*, current v3 title *Symbolic Summation of Multivariate Rational Functions*, revised17March2025. Shift-equivalence context is explicit. [2610.27168](https://arxiv.org/abs/2610.27168), *Deterministic Shift Equivalence Testing for Sparse Polynomials*, submitted19October2026. Both within five years of27October2026. Neither is cited as a semiring-degree proof. |

Concept: **coordinate-degree control under constant polynomial shifts**, equivalently preservation of coordinate degree bounds. Literature applications often use finite variables over a field/ring; the binomial/support mechanism admits arbitrary variable types and commutative semirings. Ring translations have inverse shifts, yielding degree equality; that stronger conclusion under stronger assumptions does not invalidate the broader semiring upper bound. Literature supplies context and applications; the accepted native proof establishes the precise generality rather than importing field assumptions from algorithm papers.

## Phases 4a–4b: all parameters and generality

| Parameter | Comparison with standard form and verified outcome |
|---|---|
| σ : Type u_1 | Arbitrary including empty/infinite variable sets; individual polynomials have finite support. No Fintype/DecidableEq assumption to drop. |
| R : Type u_2 | Independent coefficient universe. No concrete ℝ restriction; positive characteristic, zero divisors and trivial semiring allowed. |
| CommSemiring R | Fixed parent translation and MvPolynomial interface. No subtraction/inverses used. Semiring-only parent formation is guarded natively; failure concerns this interface, not impossibility of a different construction. |
| α : σ → R | Arbitrary constant shift; no nonzero or genericity assumption. Arbitrary polynomial substitutions need additional degree constraints and can increase degree. |
| j : σ | Any chosen variable, no membership in P.vars required. |
| P | Any polynomial, including zero and constants; no degree positivity or nonvanishing assumption. |

**MAXIMALLY GENERAL within the fixed parent interface; no mechanical hypothesis weakening established.** Root verified a ring companion `degreeOf j (taylor α P) = degreeOf j P` by applying the independent upper-bound proof to α and −α and using the inverse-translation law. This is a stronger specialization under **CommRing**, not a removal of the semiring assumption, and is not grounds for YES-but-generalise-first. The univariate equality is already in mathlib over Semiring, but transporting arbitrary multivariate coordinate isolation and all other shifted variables requires a representation argument; no one-call replacement was established.

## Phase 4c: nine modern-idiom checks

| # | Check | Finding and downstream consequence |
|---|---|---|
| 1 | Typeclasses versus preambles | Already CommSemiring and bundled AlgHom; no replacement preamble. |
| 2 | Filters versus metric/sequences | No topology, n/a. |
| 3 | Universal property versus construction | Translation uses aevaluation; proof uses coefficients/support rather than inventing a substitution construction. |
| 4 | Bundled substructures | Degree-bounded polynomial submodules/filtrations could package preservation. Establishing preservation still requires this mathematical law; no current additional consumer needs a new bundle. |
| 5 | Modules/semirings versus fields | Already CommSemiring; no field/domain/characteristic requirement. Ring equality is verified separately, not a weakening. |
| 6 | Higher category | No concrete downstream benefit demonstrated. |
| 7 | Concrete index | σ arbitrary; exponent ℕ is the actual polynomial monoid, not an incidental restriction. Replacing it changes the object. |
| 8 | Concrete-via-abstract proof diagnostic | Yes: body mentions `taylor` only through `coeff_taylor` once, then uses coefficient vanishing and support degree bounds. [Diagnostic](../evidence/MvPolynomial.degreeOf_taylor_le/proof-body-diagnostic.json). Raw generic coefficient criterion is verified, but **assumes** the essential high-coefficient vanishing. It cannot replace the target until that premise is proved. No missing new generic criterion is established. |
| 9 | False-generalization guard | Arbitrary substitution, total degree, and formal derivatives are not silently substituted for constant shifts, individual degree, and Hasse derivatives. Generic evaluation can increase degree; ring equality is not asserted for all semirings on the basis of its inverse proof. |

No verified real modern restatement requires changing the shipped theorem. A filtration companion may organize future API, but the original inequality directly composes with `monomial_le_degreeOf` and degree-bound transitivity in the actual caller. No cost-based downgrade or unverified generalise-first claim.

## Phase 4.5: infrastructure risks

All six rows **n/a, theorem**: typeclass diamonds, reducibility leak, noncanonical unfolding, instance-priority collision, universe-polymorphism infrastructure, coercion ambiguity. The declaration creates no data definition or instance. Independent universes are present in its native type.

## Phase 4.6: five proof-strategy checks

| Check | Finding |
|---|---|
| ε/neighborhood versus filters | n/a, algebraic degree inequality. |
| Elements versus structural maps | Support-wise degree criterion is canonical for the numerical conclusion; generic AlgHom alone does not imply degree preservation. |
| Sequences versus nets | n/a, finite polynomial support. |
| Construction versus universal property | Existing aevaluation/degree API used; no unnecessary construction. |
| Missing helper | Hasse coefficient identity and degree vanishing are the real mathematical dependencies. They are already assessed YES project contributions, not current mathlib primitives. Generic substitution-degree control would be a separate new helper requiring proof. |

Strategy **MATHLIB-IDIOMATIC** with the proposed Hasse/Taylor API. A future direct monomial/support proof may reduce dependencies; no such alternative is needed to establish the current theorem or count as an existing replacement.

## Phase 5: five actual methods on three forms

[Raw formal-search receipts](../evidence/MvPolynomial.degreeOf_taylor_le/formal-search.json) preserve twelve actual requests/responses; three untruncated source searches supply methodD.

| Method | Current degree-of-translation form | Literature shift/individual degree | Abstract substitution-degree form |
|---|---|---|---|
| Finder | Total-degree rename and coordinate-degree equivalence near-matches | Coordinate isolation via degreeOf_eq_natDegree / finSuccEquiv | aeval_natDegree_le; univariate composition bounds |
| Loogle | `"degreeOf_taylor"`: empty | `"natDegree_taylor"`: positive univariate candidate | `MvPolynomial.degreeOf, MvPolynomial.aeval`: empty |
| LeanSearch | degreeOf and sum/product/constant multiplication bounds | Homogeneity/rename, univariate translation equivalence near-matches | aeval_natDegree_le, univariate sum/product bounds |
| rg | [current](../evidence/MvPolynomial.degreeOf_taylor_le/rg-current.json) | [literature](../evidence/MvPolynomial.degreeOf_taylor_le/rg-literature.json) | [abstract](../evidence/MvPolynomial.degreeOf_taylor_le/rg-abstract.json) |
| Local symbols | Project degreeOf_taylor_le resolves | Polynomial.natDegree_taylor resolves | degreeOf_eval empty |

Local index **unavailable**; empty local result does not establish absence. External indexes may differ from the pinned revision. Pinned source modules and native checks establish the actual positive facts:

* `MvPolynomial.degreeOf_le_iff`, [Degrees](../evidence/MvPolynomial.degreeOf_taylor_le/MvPolynomial-Degrees-module.lean.txt):235, characterizes degree by bounds on supported exponents. The raw coefficient criterion specializes this together with `mem_support_iff`; its vanishing hypothesis remains to be supplied.
* `degreeOf_add_le`:264, `degreeOf_sum_le`:303, `degreeOf_prod_le`:311, `degreeOf_pow_le`:319 control algebra operations. Applying them to a shifted monomial expansion requires the expansion and exponent-bound argument; they do not state the target.
* `Polynomial.natDegree_taylor`, [univariate Taylor](../evidence/MvPolynomial.degreeOf_taylor_le/Polynomial-Taylor-module.lean.txt):93, preserves univariate natural degree over Semiring. Exact specialization is natively checked. It is not `MvPolynomial.degreeOf` of simultaneous multivariate shifts.
* `MvPolynomial.aeval_natDegree_le`, [RingTheory polynomial Basic](../evidence/MvPolynomial.degreeOf_taylor_le/Polynomial-Basic-module.lean.txt):898, has univariate target and bounds it by **totalDegree × substitution bound**. A bound by total degree is insufficient for the chosen coordinate-degree conclusion.
* `degreeOf_eq_natDegree` is natively signature-checked as a coordinate-isolation bridge. Establishing its compatibility with simultaneous shifts would be additional mathematical work; no compatible existing shift transport is demonstrated.

Search conclusion: positive partial analogues and degree building blocks; no verified exact normalized multivariate target or short composition. This is not a global absence proof from search failure.

## Phase 5.5: three statement-shape checks

1. **Normal form:** the translated degree on the left and original bound on the right matches `degreeOf_*_le` conventions. Equivalent support/coefficient-vanishing criteria exist; the numerical inequality is immediately usable by the caller. Ring equality is a companion under stronger assumptions.
2. **Syntactic generality:** direct `aeval (fun i ↦ X i + C (α i)) P` spelling is definitionally the same target. Native generic coefficient criterion and ring equality explore alternative forms; neither requires replacing the current broad inequality.
3. **Superfluous arguments:** σ and R determine polynomial type, CommSemiring forms both polynomial and translation, α determines shift, j selects coordinate degree, P is the input. None unused. No hidden Fintype/DecidableEq/Nontrivial assumption.

Overall **SHIP-AS-STATED**; optional direct-aeval spelling changes naming surface, not mathematics.

## Phase 6.0: complete callers and inline audit

| Caller | Source and use | Verified transport |
|---|---|---|
| `Roth.index_le_card` | Index229, one explicit application; combines supported exponent ≤ translated degree ≤ original degree ≤ supplied bound | Full copied caller proof uses fresh `DegreeTaylorAssessment.replay`, with a separately copied public support bridge replacing the original private helper. All weight/index steps compile. |

**K=1 explicit production caller**, no same-file caller, no simp tag. [Exact search](../evidence/MvPolynomial.degreeOf_taylor_le/rg-callers.json), [inline audit](../evidence/MvPolynomial.degreeOf_taylor_le/rg-inline.json), [summary](../evidence/MvPolynomial.degreeOf_taylor_le/callers.json). Other uses of `degreeOf_le_iff` bound Hasse derivatives, unrelated substitutions or support boxes, rather than independently rederiving constant-shift control. Source references are not a complete opaque kernel-dependency closure. One caller is weaker API-usage evidence than three callers, but cannot make a genuine new degree lemma into a short composition from old mathlib.

## Phase 6: actual composition and evidence

Independent target replay uses:

```lean
refine degreeOf_le_iff.2 fun e he ↦ not_lt.1 fun h ↦ ?_
simp [mem_support_iff, coeff_taylor, hasseDeriv_eq_zero_of_degreeOf_lt h] at he
```

The two central facts are **new project mathematics**, not pinned mathlib blocks. The raw module imports no Roth and independently verifies an abstract coefficient criterion:

```lean
degreeOf_le_iff.mpr fun d hd ↦ not_lt.mp fun hlt ↦
  (mem_support_iff.mp hd) (h d hlt)
```

Here `h` states the essential coefficient vanishing above a threshold. Applying this to translation with that premise assumed does **not** prove the target; obtaining the premise is the Taylor/Hasse content. The raw univariate equality is a positive analogue. No ≤3-existing-call term for the complete old target is established. Closing `simp` in the project replay is not automatically NO or BORDERLINE: unlike purely definitional normalization, it calls the already assessed coefficient-Taylor and Hasse-vanishing contributions. The actual gap is **coordinate-degree control for multivariate constant substitution**, absent from the tested generic routes, not arbitrary algebra-map degree preservation.

Accepted [target source](../evidence/MvPolynomial.degreeOf_taylor_le/native-target-executed.lean.txt)/[receipt](../evidence/MvPolynomial.degreeOf_taylor_le/native-target-success.json), [raw source](../evidence/MvPolynomial.degreeOf_taylor_le/native-raw-executed.lean.txt)/[receipt](../evidence/MvPolynomial.degreeOf_taylor_le/native-raw-success.json), [extra source](../evidence/MvPolynomial.degreeOf_taylor_le/native-extra-executed.lean.txt)/[receipt](../evidence/MvPolynomial.degreeOf_taylor_le/native-extra-success.json). Complete success, partial false, no errors/warnings/unproved declarations; axioms only `propext`, `Classical.choice`, `Quot.sound`. No limit raises, unsafe proof, new axiom or sorry. Direct proof-constant audit excludes a circular target call in the independent replay. [Verification](../evidence/MvPolynomial.degreeOf_taylor_le/verification.json) separates rejected attempts from accepted evidence.

The isolated final-goal `exact?` attempt failed without a heartbeat exhaustion; it is a bounded diagnostic, not proof of absence or minimality ([attempt](../evidence/MvPolynomial.degreeOf_taylor_le/native-composition-attempt.lean.txt), [rejected receipt](../evidence/MvPolynomial.degreeOf_taylor_le/native-composition-rejected.json)). Initial extra preparation failed because aeval_natDegree_le was not imported and a support helper inherited an unused Fintype; initial raw preparation used unqualified coefficient identifiers. Corrected accepted sources compile. These preparation failures are separately archived and excluded from accepted proof evidence.

## Phases 7–8: verdict, gates and actionable next steps

**YES-add-as-is.** This standard degree law supports polynomial shift arguments beyond the Roth index application. It works at commutative-semiring and arbitrary-variable generality, fits the `degreeOf_*_le` API, and fills a concrete missing connection between constant substitution and individual degree. Univariate equality and total-degree evaluation bounds are insufficient replacements. The short proof correctly reuses proposed Hasse/Taylor mathematics; no ≤3-call composition from existing mathlib or mechanical weakening is established. This verdict is not inherited from parent `taylor`, not based on cost, and not inferred from an empty search alone.

Proposed destination **`Mathlib/Algebra/MvPolynomial/Taylor.lean`**, with coefficient-Taylor law. Proposed PR title **“feat(Algebra/MvPolynomial): bound coordinate degrees under translation”**. Group with actual accepted YES `MvPolynomial.coeff_taylor`, `degreeOf_hasseDeriv_le`, `hasseDeriv_eq_zero_of_degreeOf_lt`, and foundational `hasseDeriv`; [recorded accepted grouping](../evidence/MvPolynomial.degreeOf_taylor_le/accepted-yes-grouping.json) was read from progress, not guessed from names. The optional named translation parent can be decided separately: stating the identical law against `aeval(X+Cα)` preserves this contribution if that name is declined.

Pre-PR checklist: `/generalise MvPolynomial.degreeOf_taylor_le` to reconfirm the current interface floor and separately consider the verified ring equality; `/cleanup Roth/Taylor.lean degreeOf_taylor_le`; choose named taylor versus direct aevaluation; include imports, source attribution and coefficient/degree proof chain; test the index consumer and mathlib build. Check reviewers against recent relevant history: **Kenny Lau**, Taylor API commits41b93296c7/2b2788e7a1, and **Yaël Dillies**, MvPolynomial coefficient/degree refactor631b214f7c, are evidence-based candidates ([history](../evidence/MvPolynomial.degreeOf_taylor_le/reviewer-history.json)). No reviewer contacted and no upstream PR opened.

Alternative destination if upstream translation API is declined: retain this law in `Roth/Taylor.lean`; its generic degree content does not require Archive or a specialist satellite. Production stays unchanged under this assessment request. All required phases, rows, searches, actual caller validation and supporting artifacts are complete; unresolved verification list empty. Root independently reviews before publication. [Assessment](../evidence/MvPolynomial.degreeOf_taylor_le/assessment.json), [portable validator](../evidence/MvPolynomial.degreeOf_taylor_le/validate.py).
