# `Roth.exists_int_factors` — YES-but-generalise-first

Canonical declaration176, `Roth/Separation.lean:485`. Full read-only assessment; production sources and pins unchanged. Root acceptance pending.

## Phase 0 — Doctor

All seventeen fresh source/pin hashes match the successful baseline (`lake build`, exit0,2467 jobs). [Fresh hashes](../evidence/Roth.exists_int_factors/baseline-hashes.json), [baseline](../evidence/Roth.exists_int_factors/baseline-build.txt), [manifest](../evidence/Roth.exists_int_factors/input-manifest.json). The entire declaring module and complete sole caller were read. [Whole module](../evidence/Roth.exists_int_factors/source-context.lean.txt). This public theorem has no prefilter and does not inherit either172 or173's verdict.

## Phase 1 — Comprehend

An integer polynomial in disjoint sets of variables which is a product of two nonzero rational factors admits integer factors with exactly the same individual degrees. The left factor uses the variables `τ`; the right factor is univariate in the distinguished `none` variable. Both integer factors must be nonzero, their product must equal the original integer polynomial, and every left partial degree and the right natural degree must agree with the supplied rational factors.

```lean
∀ {τ : Type u_1} {U' : MvPolynomial τ ℚ} {V' : Polynomial ℚ},
  U' ≠ 0 →
    V' ≠ 0 →
      ∀ {F : MvPolynomial (Option τ) ℤ},
        (map (Int.castRingHom ℚ)) F = (rename some) U' * (Polynomial.aeval (X none)) V' →
          ∃ (U : MvPolynomial τ ℤ) (V : Polynomial ℤ),
            U ≠ 0 ∧
              V ≠ 0 ∧
                F = (rename some) U * (Polynomial.aeval (X none)) V ∧
                  (∀ (j : τ), degreeOf j U = degreeOf j U') ∧ V.natDegree = V'.natDegree
```

[Full native type](../evidence/Roth.exists_int_factors/native-type.json), [original exact execution](../evidence/Roth.exists_int_factors/factors176-original-executed.lean.txt), [native receipt](../evidence/Roth.exists_int_factors/factors176-original-receipt.json). The kernel pretty-printer explicitly elides1652 characters; this is not a full kernel-body dump. The complete written source, full type/axioms and kernel-value audit remain available. Standard axioms are `propext`, `Classical.choice`, `Quot.sound`.

The proof chooses a primitive integral scalar multiple `U=g•U'`, rescales `V'` by `g⁻¹`, and uses the coefficient products of disjoint factors plus Bézout to show every rescaled coefficient belongs to ℤ. Injectivity of coefficient mapping descends factor equality; nonzero scalar multiplication and degree preservation under injective mapping establish all remaining conclusions. The exact ordered293-name audit checks293 unique/present/value constants and finds precisely one direct kernel-value consumer, `Roth.exists_det_eq_mul`. This count is not a transitive dependency/simp closure.

## Phase 2 — Preliminary

BIG by the command's criterion: explicitly listed under the declaring module's main results. It is an integral factor-descent API, independent of Wronskians. The one-line definition test is n/a for a theorem. Its single caller discards degree equalities, but the public mathematical statement contains them and they are included in the complete generalization experiment.

## Phase 3 — Exhaustive literature

Exact requests, response SHA256/bytes/status, sanitized locators and original concise summaries: [general](../evidence/Roth.exists_int_factors/literature-0.json), [named channels](../evidence/Roth.exists_int_factors/literature-1.json), [MO/arXiv](../evidence/Roth.exists_int_factors/literature-2.json), [primary access](../evidence/Roth.exists_int_factors/literature-3.json), [recent/Stacks retry](../evidence/Roth.exists_int_factors/literature-4.json). Full article/search bodies were not persisted; returned locator query strings are removed. Exact query requests are preserved.

| Channel | Actual request / locator | Result |
|---|---|---|
| General specific | `Gauss lemma separated variables rational factorization integer polynomials primitive content` | Classical primitive polynomial/content descent. |
| General abstract | `GCD domain fraction field primitive polynomial product integral coefficients Gauss lemma` | GCD domains are the natural standard scope beyond ℤ/ℚ. |
| General alternative | `rank one integer matrix rational outer product integer factorization primitive vector` | Coefficients form an outer product; rank-one decomposition alone does not give integral witnesses. |
| ChatGPT math | Tool inventory | n/a: `ask_chatgpt_math` unavailable. |
| Local references | clean.tex §2 lines420–431 | Explicit primitive rescaling, coefficient Bézout descent, integrality/nonzero; [search](../evidence/Roth.exists_int_factors/local-literature-search.json), [excerpt](../evidence/Roth.exists_int_factors/local-literature.txt). |
| nLab | `site:ncatlab.org/nlab Gauss lemma primitive polynomial`; content(ring theory) | Content/primitive terminology. Direct page HTTP400 unsupported XHTML; search returned locators. |
| nCatLab | `site:ncatlab.org/ncatlab primitive polynomial Gauss lemma`; retry `site:ncatlab.org/ncatlab "Gauss lemma"` | Returned nLab pages outside namespace, including unrelated geometry; no exact nCatLab result. No absence inference. |
| Stacks | `site:stacks.math.columbia.edu Gauss lemma polynomial fraction field`; retry with factor | 0H71 Lemma10.44.1 uses Gauss descent over a multivariate polynomial fraction field. 037B Lemma10.37.6 gives denominator cancellation for PID normality. Initial00H7 is going-down, rejected as exact theorem citation. |
| MathOverflow | `site:mathoverflow.net Gauss lemma multivariate polynomial rational integer factors` | Question73601 absorbs rational scalar factors into primitive integral factors;512096 distinguishes forms of primitivity. Supplementary discussion. |
| Recent arXiv, five years | `site:arxiv.org primitive polynomial content Gauss lemma after:2021-10-27 before:2026-10-28`, content/GCD retries | 2610.30208, submitted2026-10-21, proves content/primitivity results for special polynomial families; application context, not this theorem. Initial Gaussian/finite-field/Gauss-period hits rejected. |

Primary [Monson, Notes on Commutative Rings, p7 §5(b)](https://bmonson.ext.unb.ca/fields/comrg.pdf) explicitly rescales two fraction-field factors into the base UFD. [Stacks0H71](https://stacks.math.columbia.edu/tag/0H71) gives a related multivariate Gauss application. [Recent arXiv abstract](https://arxiv.org/abs/2610.30208) supplies dated content/primitivity context. Chicago lecture notes search identifies Lemma2.21.6, but direct URL404; no successful full-page access is claimed.

Synthesis: this is Gauss-type integral factor descent with separated-variable support and preserved degrees. Standard coefficients range from ℤ to UFDs and GCD domains. The project uses a Bézout shortcut for scalar integrality; gcd1 need not generate the unit ideal over a GCD domain. A reduced-fraction divisibility argument supplies the correct broader proof, without adding Bézout as an artificial hypothesis.

## Phase 4a — Parameters and hypotheses

| Parameter / premise | Audit |
|---|---|
| `τ : Type*` | Arbitrary universe/index type. Native type has no finiteness or decidable equality instance. Empty and infinite variable sets are allowed. |
| `ℤ`, `ℚ`, cast hom | Replace by a commutative GCD domain `R`, fraction field `K`, `algebraMap R K`, `[Algebra R K] [IsFractionRing R K]`. This is actual verified proof transfer, not definitional equality. |
| `U' : MvPolynomial τ ℚ` | Retain arbitrary left factor. No monic, irreducible or positive-degree restriction. Constant factors included. |
| `V' : Polynomial ℚ` | Retain arbitrary univariate right factor, no monic/primitive condition. |
| `hU`, `hV` | Essential for the unchanged nonzero-output conclusion: if a rational factor is0 then `F=0`; the product of two nonzero integral factors in a domain cannot be0. |
| `F` | Arbitrary integral polynomial; no primitive or nonzero hypothesis is required separately. Its nonzero follows from factorization and the two supplied nonzero factors. |
| `hF` | Exact separated-variable equality retained. An unrestricted rational factorization would need a different support-preservation theorem. |
| Conclusion | Full existential integral factors, two nonzero proofs, exact factorization, all `∀ j` partial-degree equalities and `natDegree` equality preserved. Not replaced by coefficient-integrality alone. |
| Generic hierarchy | `CommRing R`, `NormalizedGCDMonoid R`, fraction-field structure and field `K` support gcd extraction, reduced fractions and degree transfer. No claimed semiring/noncommutative weakening. No `IsBezout`, UFD, characteristic0 or finite-variable hypothesis in final GCD form. |

The [native zero-factor guards](../evidence/Roth.exists_int_factors/factors176-guards-executed.lean.txt) and [receipt](../evidence/Roth.exists_int_factors/factors176-guards-receipt.json) prove no nonzero integral separated factors can multiply to0, while each omitted input-nonzero hypothesis admits the explicit rational0×1 or1×0 factorization.

## Phase 4b — Verified generality

STRICTLY NARROWER THAN THE VERIFIED GCD-DOMAIN FORM. Generalization is a proof transfer of the existing target, using generalized primitive representatives and a reduced-fraction scalar lemma. A separately verified Bézout-domain proof was an intermediate successful route; it is not misrepresented as the final GCD proof. Existing `NumDen` APIs assume UFD and were rejected as a route to arbitrary GCD domains. Existing `IsLocalization.surj_of_gcd_domain` supplies the actual reduced relation.

```lean
variable {τ R K : Type*} [CommRing R] [IsDomain R] [NormalizedGCDMonoid R]
    [Field K] [Algebra R K] [IsFractionRing R K]
theorem exists_separated_factors {U' : MvPolynomial τ K} {V' : Polynomial K} (hU : U' ≠ 0) (hV : V' ≠ 0)
    {F : MvPolynomial (Option τ) R} (hF : map (algebraMap R K) F =
      rename some U' * Polynomial.aeval (X none : MvPolynomial (Option τ) K) V') :
    ∃ (U : MvPolynomial τ R) (V : Polynomial R), U ≠ 0 ∧ V ≠ 0 ∧
      F = rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) R) V ∧
      (∀ j, degreeOf j U = degreeOf j U') ∧ V.natDegree = V'.natDegree
```

[Full isolated GCD proof](../evidence/Roth.exists_int_factors/factors176-gcd-full-executed.lean.txt), [clean receipt](../evidence/Roth.exists_int_factors/factors176-gcd-full-receipt.json), [composition and exact specialization](../evidence/Roth.exists_int_factors/factors176-gcd-composition-specialization-executed.lean.txt), [specialization receipt](../evidence/Roth.exists_int_factors/factors176-gcd-composition-specialization-receipt.json). The isolated execution imports only fifteen mathlib modules, guards the project target with `#check_failure`, and locally reproves the coefficient bridge and generic primitive representative; neither helper is smuggled in through Roth.

The new scalar lemma obtains `v*b=a` with unit gcd(a,b), uses each integral product to prove `b∣uᵢ`, then `b∣gcd(u)=1`, and solves using the unit inverse. This avoids the false inference gcd1⇒unit ideal. The primitive representative theorem and degree arguments then preserve the full factorization statement. MODERATE proof adjustment; cost has no bearing on the verdict. [Pinned source](../evidence/Roth.exists_int_factors/Mathlib_Algebra_GCDMonoid_IntegrallyClosed.lean.txt).

## Phase 4c — Modern idioms

| # | Diagnostic | Result / downstream consequence |
|---|---|---|
| 1 | Typeclasses | Yes: existing GCD-domain/fraction-field structures replace concrete rings; works over other UFD/GCD coefficient rings. |
| 2 | Filters/nets | No topology or limiting operation. |
| 3 | Universal property | Existing localization algebra suffices; no new construction/class is needed. |
| 4 | Bundled substructures | `Polynomial.lifts` and `IsLocalization.IsInteger` are canonical image-membership interfaces for auxiliary descent. Main theorem should retain explicit factors/equality, which the caller needs. |
| 5 | Weaker hierarchy | Yes: replace ℤ/ℚ by general GCD domain/fraction field. No artificial Bézout/UFD restriction in final proof. |
| 6 | Higher categories | No categorical coherence or higher-categorical object. |
| 7 | Concrete index | `τ` already arbitrary; concrete integers/rationals are coefficients rather than an indexing restriction. |
| 8 | Concrete-via-abstract | Yes by full verified transfer. [Lexical diagnostic](../evidence/Roth.exists_int_factors/concrete-abstract-diagnostic.json) finds several Int.cast/injectivity lines, so the literal0/1-line shortcut does not fire. Those lines are coefficient-map/degree transport; denominators/Bézout occur in helpers. |
| 9 | False-generalization guard | Pass: full original witnesses/degrees recovered by ℤ/ℚ specialization. Reject claiming arbitrary-module gcd1 descent over GCD domains, replacing fraction fields by arbitrary field extensions, or treating univariate Gauss as an immediate MVP theorem. |

MODERN-IDIOM AVAILABLE: general coefficient algebra eliminates repeated concrete casts and composes with localization and gcd APIs. The benefit is explicit integral descent for polynomial rings over other coefficient domains; no category-theory relabeling is proposed.

## Phase 4.5 — Infrastructure risks

Theorem n/a for all six infrastructure rows: no new instance path (diamonds), no reducible definition (leaks), no unfolding alias, no instance priority, no forced universe restriction (generic theorem is universe-polymorphic), and no new coercion. Proof-local algebra structures use existing mathlib APIs.

## Phase 4.6 — Proof strategy

| # | Question | Answer / alternative |
|---|---|---|
| 1 | Topology | No topology. |
| 2 | Elements vs substructures | Auxiliary coefficient integrality may use `IsInteger`/`lifts`; reduced divisibility is appropriate over GCD domains. Main existential factors remain concrete for consumers. |
| 3 | Analysis sequences | No analysis. |
| 4 | Category universal property | Existing localization structure, no new universal construction. |
| 5 | Missing helpers | Generic primitive representative, finite primitive scalar descent and separated factor descent/degree preservation are concrete API gaps; upstream them as distinct lemmas. |

REFACTOR-RECOMMENDED: use generalized primitive representative plus GCD reduced-fraction scalar descent, then factor and degree transport. The original Bézout proof is idiomatic for integers but unnecessarily narrows the coefficient ring. Existing univariate Gauss theorem is valuable infrastructure, but transporting multivariate supports/primitivity to it is new mathematical glue.

## Phase 5 — Actual five-method search, all three forms

Every cell below corresponds to an actual tool/CLI request. External index declarations may differ from this pinned checkout. Local search reports index unavailable and returns fallback source hits including scratch probes; those are not mathlib declarations.

| Form | Finder | Loogle | LeanSearch | rg | Local |
|---|---|---|---|---|---|
| Current ℤ/ℚ separated | [receipt](../evidence/Roth.exists_int_factors/current-leanfinder.json) | [receipt](../evidence/Roth.exists_int_factors/current-loogle.json) | [receipt](../evidence/Roth.exists_int_factors/current-leansearch.json) | [receipt](../evidence/Roth.exists_int_factors/current-rg.json) | [receipt](../evidence/Roth.exists_int_factors/current-local_search.json) |
| Standard univariate Gauss | [receipt](../evidence/Roth.exists_int_factors/standard-leanfinder.json) | [receipt](../evidence/Roth.exists_int_factors/standard-loogle.json) | [receipt](../evidence/Roth.exists_int_factors/standard-leansearch.json) | [receipt](../evidence/Roth.exists_int_factors/standard-rg.json) | [receipt](../evidence/Roth.exists_int_factors/standard-local_search.json) |
| Abstract GCD scalar descent | [receipt](../evidence/Roth.exists_int_factors/abstract-leanfinder.json) | [receipt](../evidence/Roth.exists_int_factors/abstract-loogle.json) | [receipt](../evidence/Roth.exists_int_factors/abstract-leansearch.json) | [receipt](../evidence/Roth.exists_int_factors/abstract-rg.json) | [receipt](../evidence/Roth.exists_int_factors/abstract-local_search.json) |

Positive candidates, full pinned source archives/hashes in [mathlib inputs](../evidence/Roth.exists_int_factors/mathlib-inputs.json):

- `Polynomial.IsPrimitive.map_mul_mem_lifts_iff` and `.mul_map_mem_lifts_iff`, `Mathlib/RingTheory/Polynomial/GaussLemma.lean:254,238`: primitive univariate factor times a fraction-field polynomial is integral iff the other factor is. Loogle gave an exact positive hit; native exact-call example verifies it.
- `Polynomial.IsPrimitive.dvd_of_fraction_map_dvd_fraction_map`, same file:301: divisibility descent, not the full separated-factor existential/degree statement. External LeanSearch signatures varied; pinned native signatures govern.
- `MvPolynomial.isLocalization`, `Mathlib/RingTheory/MvPolynomial/Localization.lean`: coefficient localization and integer-multiple existence. Does not produce primitive factors or preserve separated supports automatically.
- `IsLocalization.surj_of_gcd_domain`, `Mathlib/Algebra/GCDMonoid/IntegrallyClosed.lean:25`: reduced scalar relation with unit gcd. This is existing infrastructure, not the new finite-family integrality conclusion.
- `IsFractionRing.isInteger_of_isUnit_den`, `Mathlib/RingTheory/Localization/NumDen.lean:103`: requires UFD via its section; not an arbitrary-GCD shortcut.
- Injective map and scalar-degree APIs (`degrees_map_of_injective`, `Polynomial.natDegree_map_eq_of_injective`, `degreeOf_C_mul`, `Polynomial.natDegree_C_mul`) prove the degree transport after new factors exist.

Conclusion: partial matches and infrastructure found; no verified existing declaration or ≤3-call proof of the full target. This is not an absolute absence claim based on search failure. The actual isolated Gauss proof and complete generic construction distinguish existing API from new proof work.

## Phase 5.5 — Statement shape

1. Normal form: explicit factor witnesses/equality serve the caller; auxiliary `IsInteger`/`Polynomial.lifts` express image membership canonically. `optionEquivLeft` gives an alternative iterated-polynomial form. Its conversion and primitive-coefficient bridge are not definitional or supplied by univariate Gauss alone. Equality orientation remains compatible with rewriting at the consumer.
2. Syntactic generality: actually attempted Bézout and GCD coefficient-ring transfers, preserving `Option τ`, all existential data and degree conclusions. Choose the verified GCD/fraction-field form. A two-arbitrary-variable-block or tensor/pure-rank-one formulation is a separate expanded-representation proposal, not a proven mechanical weakening here.
3. Superfluous arguments: original native statement contains only `τ,U',V',hU,hV,F,hF`; each object is used, both nonzero assumptions serve nonzero output, and `hF` controls integrality. Outer Fintype/DecidableEq were already omitted. The generic helpers omit genuinely unused domain/fraction assumptions where Lean's linter identifies them; do not carry them as hidden premises.

RESTATE-BEFORE-SHIP: use the GCD-domain form; retain full original statement as a concrete specialization if useful locally. Degree equalities may be exposed as a separate strengthened corollary, but must not be silently discarded in this assessment.

## Phase 6.0 — Caller and inline audit

| Explicit caller | Source | Behavior and refactor |
|---|---|---|
| `Roth.exists_det_eq_mul` | `Roth/Separation.lean:552` | Takes rational Wronskian factors from the private precursor, obtains integral nonzero factors/equality, and discards degree equalities. Replace this one invocation by the generic theorem specialized with `(R := ℤ) (K := ℚ)`; retain the entire determinant and degree-bound proof. Complete caller replay checks this exact refactor. |

Internal use count1 within the declaring module; external-to-file0. [Unignored search](../evidence/Roth.exists_int_factors/callers-rg.json), [tracked grep](../evidence/Roth.exists_int_factors/callers-git-grep.json), [canonical lexical enumeration](../evidence/Roth.exists_int_factors/lexical-enumeration.json), [inline audit](../evidence/Roth.exists_int_factors/inline-rg.json). The module docstring occurrence and declaration itself are not calls. No independent inline rederivation was found. The direct293 kernel-value audit independently confirms the sole consumer; neither search is claimed as opaque transitive dependency closure.

## Phase 6 — Actual composition experiments

The [bounded full-goal closure probes](../evidence/Roth.exists_int_factors/factors176-gcd-composition-specialization-executed.lean.txt) check `fail_if_success exact hF` and `fail_if_success simpa only using hF` immediately before the genuine full generic proof. They rule out only those two routes, not all possible mathlib proofs. The [complete GCD caller](../evidence/Roth.exists_int_factors/factors176-gcd-caller-executed.lean.txt) and [receipt](../evidence/Roth.exists_int_factors/factors176-gcd-caller-receipt.json) verify the sole downstream consumer.

1. Existing univariate Gauss exact-call experiment succeeds on its own `Polynomial.IsPrimitive`/`Polynomial.lifts` interface. It does not produce a multivariate primitive representative, encode disjoint factors, descend coefficient witnesses, or give all degree equalities. An encoding through `optionEquivLeft` still needs these substantive bridges.
2. Existing localization produces integer multiples; primitive extraction requires gcd division/support transport. Reusing the newly proved generic172 theorem is legitimate project refactoring but is not an existing mathlib call. The accepted complete generic proof additionally needs scalar-integrality descent, coefficient extraction, factor equality transport and separate degree calculations.
3. The complete sole caller replay uses the new generic target and checks all downstream determinant degree bounds. It is a specialization of a new theorem, not evidence for NO-composable-from-mathlib.

No verified ≤3-existing-call full-statement replacement was found. Phase6 classification is NOT-COMPOSABLE in the workflow's evidence-based sense; this is not a proof of universal absence. No closing `simp [definitions]` composition is presented as an automatic NO; normalization/proof transfer here is substantial. Failed native attempts are separately archived and excluded from accepted evidence; they do not prove API absence.

## Phase 7 — Actionable verdict

**YES-but-generalise-first**, reasons LITERATURE-WEAKENING and MODERN-IDIOM. The precise missing API is multivariate separated factor descent over a GCD domain/fraction field, preserving nonzero witnesses and all individual degrees. The verified generic proof demonstrates the gap rather than merely reporting unsuccessful searches. Existing univariate Gauss integrality/divisibility is not the same statement, and adjacent accepted172/173 do not imply this verdict.

Proposed upstream file: `Mathlib/RingTheory/MvPolynomial/GaussLemma.lean` (new file importing existing `MvPolynomial/Localization`, `Polynomial/GaussLemma` and the needed polynomial equivalences; avoid importing it into foundational `MvPolynomial/Eval`). PR title: **feat(MvPolynomial): descend separated fraction-field factors over GCD domains**. Group with already accepted YES `Roth.exists_primitive_smul_eq` (generic primitive representatives); the separately accepted `Roth.exists_int_eq_of_gcd_eq_one` module/Bézout abstraction can be a companion PR, while the GCD scalar variant belongs with factor descent. [Verified grouping records](../evidence/Roth.exists_int_factors/accepted-grouping.json).

Before a PR:

- Run `/generalise Roth.exists_int_factors` with the verified GCD form and choose upstream names for primitive scalar descent and separated factor descent.
- Run `/cleanup Roth/Separation.lean Roth.exists_int_factors`, preserving all conclusions and distinguishing local/private glue from upstream API.
- Run `/cleanup Mathlib/RingTheory/MvPolynomial/GaussLemma.lean MvPolynomial.exists_separated_factors` on the proposed upstream module and final theorem name.
- Place primitive representative/scalar-integrality helpers before the factor theorem; retain explicit degree corollaries or the full strengthened theorem.
- Replay the sole `exists_det_eq_mul` refactor and run required checks, then `/pre-submit`.

Reviewer selection from [focused recent relevant commits](../evidence/Roth.exists_int_factors/reviewers-focused.json): Justus Springer (e4c37418a1, primitive-polynomial `mem_lifts` Gauss API; f10bf357d0, integerNormalization simplification) and Junyan Xu (2f35248703, NormalizationMonoid weakening). [Broader path history](../evidence/Roth.exists_int_factors/reviewers.json) also records recent contributors. These are evidence-based candidates, not a claim of availability or assignment. No messages or PR were sent.

Alternative local destination during migration: `Roth/Separation.lean`; the concrete ℤ/ℚ wrapper supports Roth's determinant factorization. No junk/dead-code finding.

## Phase 8 — Verification and handoff

[Verification map](../evidence/Roth.exists_int_factors/verification.json), [assessment](../evidence/Roth.exists_int_factors/assessment.json), [portable validator](../evidence/Roth.exists_int_factors/validate.py), [manifest](../evidence/Roth.exists_int_factors/copy-manifest.json). Accepted exact native sources/receipts, rejected attempts, fresh17 hashes, exact canonical293 order, all search cells, literature metadata and full caller evidence are retained. Validation is read-only in scratch and integrated layouts. Unresolved technical checks: none. Root independently reviews before publication.
