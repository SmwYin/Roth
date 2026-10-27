# `Roth.exists_primitive_smul_eq` — YES-but-generalise-first

Canonical declaration172, `Roth/Separation.lean:406`. Full read-only overview/mathlibable assessment; production sources and pins unchanged. Root acceptance pending.

## Phase 0 — Doctor

The seventeen freshly computed source/pin hashes match the shared successful baseline (`lake build`, exit0,2467 jobs). [Fresh hashes](../evidence/Roth.exists_primitive_smul_eq/baseline-hashes.json), [baseline receipt](../evidence/Roth.exists_primitive_smul_eq/baseline-build.txt), [input manifest](../evidence/Roth.exists_primitive_smul_eq/input-manifest.json). The entire declaring module and all explicit callers were read: separation decomposes a multivariate polynomial over a field, factors its Hasse determinant, and descends rational separated factors to integral factors. [Full module](../evidence/Roth.exists_primitive_smul_eq/source-context.lean.txt). No prefilter, verdict inheritance, or project-code mutation was used.

## Phase 1 — Comprehend

Every nonzero rational polynomial in an arbitrary type of variables has a nonzero rational scalar multiple which is an integer polynomial with coefficient gcd exactly1. Finite monomial support suffices; neither finitely many variables nor decidable equality is an explicit hypothesis.

```lean
∀ {σ : Type u_2} {G : MvPolynomial σ ℚ},
  G ≠ 0 →
    ∃ (g : ℚ) (U : MvPolynomial σ ℤ),
      g ≠ 0 ∧ (map (Int.castRingHom ℚ)) U = g • G ∧ (U.support.gcd fun (d : σ →₀ ℕ) ↦ U.coeff d) = 1
```

[Full native type](../evidence/Roth.exists_primitive_smul_eq/native-type.json), [original native evidence](../evidence/Roth.exists_primitive_smul_eq/primitive-original-audit-receipt.json), [exact executed original source](../evidence/Roth.exists_primitive_smul_eq/primitive-original-executed.lean.txt). The proof first clears denominators with the preceding project theorem, then uses `Finset.extract_gcd`, reconstructs the divided coefficient family as a polynomial, proves coefficient identities including outside support, and transfers gcd1 along equality of supports. The scalar is the clearing integer divided by the nonzero coefficient gcd. Neither denominator clearing nor `extract_gcd` alone supplies the entire conclusion.

Native kernel-value audit checks the exact canonical array of293 declarations (including private names, original order),293 unique names,293 present constants,293 values, and the sole direct kernel-value consumer `Roth.exists_int_factors`. The target uses only standard axioms `propext`, `Classical.choice`, `Quot.sound`. Its `#print` body contains an explicit MCP printer elision (3073 characters omitted;6087 returned); this is not a complete pretty-printed kernel body. Exact source, full native type, axioms, and canonical kernel-value inspection are retained completely.

## Phase 2 — Preliminary

SMALL: a classical primitive-normalization helper, neither the project's main theorem nor a new structure. Its proof has genuine normalization and support bookkeeping; size does not determine the verdict. The definition-only one-line test (2b) is n/a because this is a theorem. One explicit use is an API signal, not grounds for deleting the theorem without a valid composition.

## Phase 3 — Exhaustive literature

Exact requests, returned response SHA256/bytes/status, locators and concise original summaries are retained in [web1](../evidence/Roth.exists_primitive_smul_eq/web-1-metadata.json), [web2](../evidence/Roth.exists_primitive_smul_eq/web-2-metadata.json), [web3](../evidence/Roth.exists_primitive_smul_eq/web-3-metadata.json), [primary access](../evidence/Roth.exists_primitive_smul_eq/web-4-metadata.json), and [targeted retries](../evidence/Roth.exists_primitive_smul_eq/web-5-metadata.json). Full article/search-result bodies are not archived. Returned locator query strings are stripped; request text and response digests are retained. No access failure is interpreted as nonexistence.

| Channel | Actual query / locator | Finding |
|---|---|---|
| General specific | `nonzero rational multivariate polynomial rational multiple primitive integer polynomial coefficients gcd` | Classical finite-coefficient primitive normalization. |
| General broader | `polynomial fraction field GCD domain primitive part scalar multiple` | Content and primitive part over GCD domains/UFDs. |
| General aliases/history | `Gauss lemma primitive polynomial content clearing denominators history` | Related Gauss-lemma formulations; multiplicativity, irreducibility descent, primitive scalar normalization are distinct. |
| ChatGPT math | Tool inventory | n/a: `ask_chatgpt_math` unavailable; all remaining channels executed. |
| Local references | `rg -n -i 'primitive\|coprime\|clearing.denominator\|gcd\|content' .mathlib-quality/references/clean.tex` | §2 lines420–422 explicitly chooses nonzero rational scalar, clears denominators, divides coefficient gcd; lines430ff explain Bézout use. [Search](../evidence/Roth.exists_primitive_smul_eq/local-literature-search.json), [excerpt](../evidence/Roth.exists_primitive_smul_eq/local-literature.txt). |
| nLab | `site:ncatlab.org/nlab primitive polynomial content Gauss lemma` | Content(ring theory), Definition0.1 defines coefficient gcd over a UFD. Ruitenburg notes Lemma2.0 cover GCD domains. Direct content-page open failed HTTP400 unsupported application/xhtml+xml; search result accessible. |
| nCatLab | `site:ncatlab.org/ncatlab primitive polynomial content localization`; retry quoted primitive polynomial | Only out-of-namespace nLab documents; no exact nCatLab hit. The query was actually executed, rather than replaced by nLab. |
| Stacks | `site:stacks.math.columbia.edu primitive polynomial content Gauss lemma`; retry primitive polynomial fraction | Results concern primitive elements/completions, not this content normalization. Direct tag00F6 was inspected and rejected as unrelated (quasi-compact opens). No stronger statement attributed to it. |
| MathOverflow | `site:mathoverflow.net primitive polynomial fraction field GCD domain` | Question512096 distinguishes GCD-primitive and unit-ideal formulations; question31494 relates primitive-polynomial localization. Supplementary mathematical discussion. |
| Recent arXiv five years | `site:arxiv.org "primitive polynomial" "content" after:2021-10-27 before:2026-10-28` | arXiv2610.30208, submitted2026-10-21, computes content and primitivity of polynomial families; an application, not a replacement for the general algebraic normalization. |

Primary source: [Keith Conrad, *The Gauss norm and Gauss’s lemma*](https://kconrad.math.uconn.edu/blurbs/ringtheory/gaussnormlemma.pdf), page3 Lemma10 supplies rational-to-integral-primitive scalar normalization (nonzero context); page1 describes three related Gauss-lemma forms. [nLab content](https://ncatlab.org/nlab/show/content%2B%28ring%2Btheory%29), Definition0.1, supplies terminology; [Ruitenburg, Constructing roots](https://ncatlab.org/nlab/files/Ruitenburg-Roots.pdf), Lemma2.0, uses GCD-domain contents. [Recent arXiv abstract](https://arxiv.org/abs/2610.30208) supplies dated application context. [MathOverflow512096](https://mathoverflow.net/questions/512096/the-equivalence-of-different-forms-of-gauss-s-lemma) is supplementary and highlights a genuine primitivity distinction.

Literature synthesis: clear a finite coefficient family in the fraction field of a GCD domain, then divide its common gcd. Polynomial multiplication is irrelevant to the normalization itself, so the same mechanism could serve finitely supported coefficient families. However gcd1 is weaker than coordinates generating the unit ideal over a general GCD domain: `2,X` in `ℤ[X]` illustrates the distinction. Over `ℤ`, Bézout identifies the two, and this is why the downstream integer-integrality argument works. No generality claim silently substitutes unimodularity or assumes a Bézout domain.

## Phase 4a — All parameters

| Feature | Actual interface | Audit / broader form |
|---|---|---|
| `σ : Type*` | Arbitrary universe, no instances | Already unrestricted, including empty and infinite variable types. |
| `G : MvPolynomial σ ℚ` | Finite monomial support | Fraction-field polynomial over a GCD domain is an expanded representation. |
| `hG : G ≠ 0` | Essential | Zero cannot map to a gcd1 polynomial; accepted zero-impossibility test checks this. |
| `g : ℚ`, `g ≠ 0` | Nonzero scalar, no prescribed sign | Preserve both existential scalar and nonzeroness; cannot simply return a denominator without gcd division. |
| `U : MvPolynomial σ ℤ` | Integral polynomial | Replace `ℤ` by a normalized GCD domain only with an actual fraction-field map. |
| Map equality | `map (Int.castRingHom ℚ) U = g • G` | Scalar/algebra-map normalization is a real bridge; not an assumed definitional equality. |
| Gcd | `U.support.gcd U.coeff = 1` in `ℤ` | Literal normalized gcd; neither pairwise coprimality nor unit-ideal primitivity in general. |
| Ambient variables | Outer `τ`, `Fintype τ`, `DecidableEq τ` absent from full type | Nothing to drop. All output data and conjunctions are used by the sole caller. |

## Phase 4b — Generality

There are no removable instance assumptions in the fixed integer/rational statement. Removing `hG` is false, as the zero-impossibility proof verifies. Removing nonzero scalar and primitivity produces the vacuous scalar0/integer0 witness, verified separately. Abstract GCD-domain coefficient extraction is a genuine broader subclaim, not by itself the full original conclusion. The full fraction-field restatement is separately checked in native evidence, retaining nonzero scalar, mapped polynomial equality and coefficient gcd1:

```lean
variable {σ R K : Type*} [CommRing R] [IsDomain R] [NormalizedGCDMonoid R]
    [Field K] [Algebra R K] [IsFractionRing R K]
theorem primitive {G : MvPolynomial σ K} (hG : G ≠ 0) :
    ∃ (g : K) (U : MvPolynomial σ R), g ≠ 0 ∧ map (algebraMap R K) U = g • G ∧
      U.support.gcd U.coeff = 1
```

Expanded-parameter audit: `CommRing R` is the existing `MvPolynomial.isLocalization` interface floor used by this proof, so a semiring weakening would require different denominator infrastructure, not deleting unused subtraction. `IsDomain R` is used for nonzero-divisor/support computations; the standard GCD-domain interface is retained (the equivalent `Nontrivial`/`NoZeroDivisors` split is not a mathematical expansion). `NormalizedGCDMonoid R` supplies normalized coefficient gcd/extraction. `Field K` supplies nonzero scalar division; `Algebra R K` identifies the coefficient map/scalar action; `IsFractionRing R K` supplies clearing and injectivity; the native `IsFractionRing.injective` signature itself does not require `IsDomain R`. Arbitrary unrelated field extensions do not satisfy the claimed result. No verified weakening of any of these full-target premises is claimed. The generic integral extraction subclaim has fewer operations but is not advertised as the full fraction-field normalization theorem.

This expanded representation is strictly broader than the concrete statement, but is not an unused-hypothesis deletion: both coefficient rings, cast map, scalar numerator and denominator-clearing interface change. The actual proof must use localization injectivity, support nonemptiness, gcd extraction and polynomial reconstruction. It does not establish arbitrary-ring primitive representatives without GCD hypotheses. The full native proof verifies the expanded signature: no foundational parent definition or downstream representation must be migrated. This is the concrete modern-idiom target for `/generalise`, rather than an untested hierarchy suggestion.

## Phase 4c — Nine modern-idiom rows

| # | Question | Answer and target | Concrete consequence |
|---|---|---|---|
| 1 | Typeclass preambles | Yes for expanded representation: `Algebra R K`, `IsFractionRing R K`, normalized GCD domain. | Other fraction fields reuse the same normalization law. |
| 2 | Filters/topology | No, purely finite algebra. | None. |
| 3 | Universal property | Yes for clearing stage: existing polynomial localization instance plus `exists_integer_multiple`. | Avoid coefficient-denominator reconstruction; gcd extraction remains. |
| 4 | Bundled substructures | Existing `Submonoid` for denominators; gcd1 is a predicate, not a new substructure needing a lattice. | Localization API records permissible denominators. No invented structure. |
| 5 | Hierarchy | Yes, ℤ/ℚ can become a GCD domain/fraction field; extracting gcd alone is broader still. | Useful for polynomial rings over other UFD/GCD coefficient rings. |
| 6 | Higher categories | No higher categorical datum or required abstraction. | None. |
| 7 | Concrete indices | `σ` already arbitrary; monomial indices `σ →₀ ℕ` are inherent polynomial exponents. | A future coefficient-Finsupp theorem would change representation, not alter polynomial exponents. |
| 8 | Concrete-via-abstract diagnostic | After the initial project denominator-clearing call, the proof uses finite support, gcd extraction, and field cancellation. Integer cast rewrites remain; it is not a literal arbitrary-ring proof already. Actual full generic probe checks the expanded interface. | Could factor a reusable primitive coefficient normalization law, instead of one result per coefficient field. |
| 9 | False-generalization guard | Require fraction-field relation and normalized gcd, preserve nonzero/map/gcd1. Reject unit-ideal/unimodular replacement over GCD domains, arbitrary fields unrelated to R, zero input, and infinite series. | Avoid invalid broader statements; `2,X` in ℤ[X] shows gcd1 need not imply unit-ideal coordinates. |

Modern verdict: generalise the theorem to the fully checked normalized-GCD-domain/fraction-field interface. This gives a useful public law immediately, without requiring a new content definition. A later Finsupp/content/primitive-part API can reuse it; that optional design does not block this contribution. Current mathlib's localization law alone omits primitivity. Polynomial algebra instances are scoped locally to avoid the documented global instance diamond.

## Phase 4.5 — Infrastructure risks

All six definition/class/instance risks are n/a: typeclass diamonds, reducibility leak, noncanonical unfolding, instance priority, universe-instance issues, and coercion ambiguity. This declaration is a theorem and introduces no computational definition or instance. Local scratch algebra instances do not alter production typeclass search.

## Phase 4.6 — Five proof-strategy rows

| # | Strategy | Finding |
|---|---|---|
| 1 | ε–δ versus filters | n/a: no topology. |
| 2 | Elements versus ideal/submodule inclusions | Partial: finite coefficient gcd can be abstracted, but an ideal-span-top predicate is not equivalent over arbitrary GCD domains. Keep gcd semantics. |
| 3 | Sequences versus nets | n/a: finite support. |
| 4 | Construction versus universal property | Localization supplies the clearing numerator; primitive-part reconstruction is still new normalization. |
| 5 | Missing helpers | MvPolynomial content/primitive-part normalization or an equivalent finite-support gcd-normalization bridge would remove reconstruction and support transport. `Finset.extract_gcd` already handles the underlying finite function. |

Proof-strategy verdict: use established localization for denominators and isolate genuine primitive coefficient normalization. The proof already uses mathlib's generic gcd extraction. More abstract formulation has concrete users in integer-factor descent and other fraction-field polynomial normalization, not aesthetic categorical motivation.

## Phase 5 — All fifteen actual search cells

[Complete formal receipts](../evidence/Roth.exists_primitive_smul_eq/formal-search-receipts.json) preserve twelve actual tool calls (four tools ×three forms). [Exact rg and caller searches](../evidence/Roth.exists_primitive_smul_eq/source-search-receipts.json) supply the fifth method for every form, without output truncation. External search indices may differ from the pin; pinned source and native checks control candidate claims. Local index reports `unavailable`, though source matches are returned: empty results are not proof of absence. Scratch replay constants returned by local search are excluded as mathlib replacements. A supplementary correctly spelled `primPart` local query returns the six univariate primitive-part declarations via source search, with index still unavailable: [receipt](../evidence/Roth.exists_primitive_smul_eq/supplementary-local-search.json).

| Form | Finder | Loogle | LeanSearch | rg pinned source | Local-name |
|---|---|---|---|---|---|
| Current rational MvPolynomial scalar/gcd1 | Univariate normalization/primPart hits | Exact combined map/smul/gcd query empty | Univariate content and GaussLemma hits | Exact full-name and MvPolynomial content/primPart search no target | `exists_primitive`: target and scratch copies plus unrelated primitive elements |
| Standard fraction field/content | `Polynomial.primPart`, content_primPart | `Polynomial.IsPrimitive` and API | Univariate content/GaussLemma | Content.lean and GaussLemma.lean actual bodies read | `primitivePart` empty, unavailable index |
| Abstract finite-support gcd primitive vector | `Finset.extract_gcd` | extract_gcd and division variants | Projectivization representative and unrelated Finsupp module API | MvPolynomial/Finsupp scans plus GCD-Finset bodies | `extract_gcd` confirms finite-function theorem via source |

Pinned candidates: `Finset.extract_gcd` in `Mathlib/Algebra/GCDMonoid/Finset.lean` extracts a function on a nonempty finset with gcd1; it does not return an integral polynomial or field scalar. `MvPolynomial.isLocalization` in `Mathlib/RingTheory/MvPolynomial/Localization.lean` and `IsLocalization.exists_integer_multiple` in `Mathlib/RingTheory/Localization/Integer.lean` supply a denominator multiple in the ring image; they do not primitive-normalize. `Polynomial.primPart`, `eq_C_content_mul_primPart`, `isPrimitive_primPart`, `content_primPart` in `Mathlib/RingTheory/Polynomial/Content.lean` concern univariate polynomials. `Polynomial.isUnit_or_eq_zero_of_isUnit_integerNormalization_primPart` in GaussLemma.lean is a univariate unit criterion with an additional unit hypothesis. `IsFractionRing.exists_reduced_fraction` concerns one fraction, not a whole coefficient vector; `Projectivization.exists_smul_eq_mk_rep` supplies a field representative, not integral gcd1 coordinates. No direct/specialization hit was established. Archived complete pinned source files and hashes appear in [mathlib inputs](../evidence/Roth.exists_primitive_smul_eq/mathlib-inputs.json). Failed bounded candidate tests supplement this positive accounting; they do not prove global absence.

## Phase 5.5 — Three statement-shape checks

Normal form: `map ... U = g • G` agrees with the source caller and ordinary coefficient map/smul API. The scalar can be bundled as a unit, but that is a presentation choice and does not remove the gcd argument. Syntactic generality: no finite-variable or decidable-equality assumptions occur; the full checked R/K version changes representation rather than merely renaming binders. Superfluous arguments: `σ,G,hG` all necessary; both witnesses and all three conclusions are used downstream. Shape verdict: keep the existing `support.gcd coeff = 1` conclusion in the proposed theorem; content/Finsupp predicates are optional later API work. Do not weaken gcd1 to pairwise coprimality or replace it with unrelated polynomial gcd data.

## Phase 6.0 — Complete caller and inline audit

| Explicit production caller | Occurrence | Role and refactor consequence |
|---|---|---|
| `Roth.exists_int_factors` | `Roth/Separation.lean:491` | Obtains scalar, integer factor, nonzero scalar, mapped equality and gcd1. Equality rescales the complementary rational factor; gcd1/Bézout descends its coefficients; nonzero scalar and mapped identity preserve nonzeroness and degrees. |

Internal use count1, declaration occurrence1. Fresh lexical enumeration covers the complete canonical source inventory and is cross-checked with tracked `git grep` and scoped `rg --no-ignore`. [Enumeration](../evidence/Roth.exists_primitive_smul_eq/lexical-enumeration.json). Native direct kernel-value consumers also count1 (`Roth.exists_int_factors`); this is a separate quantity, not the complete kernel/simp dependency closure. Scoped searches for coefficient gcd/extract_gcd found the target's reconstruction and the adjacent primitive-factor descent, with no second inline derivation of the full rational normalization theorem. The source caller uses all conclusions, so dropping any is not an equivalent refactor.

## Phase 6 — Actual composition experiments

The exact target is re-proved mathlib-only under a missing-project-target guard, retaining the original gcd reconstruction and replacing denominator clearing with an independently normalized localization bridge. This is a full proof, not a short existing-call composition. The full generic R/K version, generic integral extraction subclaim, zero-impossibility/vacuity guards, and targeted one-call failure tests are checked separately. The sole full actual-context `exists_int_factors` caller is replayed through the strongest full generic theorem via a direct one-call concrete specialization; helper replays and root-import context are disclosed in [the exact full caller source](../evidence/Roth.exists_primitive_smul_eq/primitive-fullcaller-executed.lean.txt) and [clean native receipt](../evidence/Roth.exists_primitive_smul_eq/primitive-fullcaller-receipt.json). The actual-context scratch source was compacted to eight imports plus current172 proofs; no historical proof source was overwritten in archived evidence. Six positive univariate candidate signatures are checked there. The initial module-docstring linter warning attempt is separately rejected and archived; the accepted header correction does not change proofs. No private project helper is counted as a mathlib building block.

Composition verdict: No verified ≤three-existing-call full-statement replacement found. Existing localization + finite gcd extraction leave coefficient reconstruction, mapped scalar cancellation, nonzero-gcd reasoning and support-gcd transport. Univariate content API does not automatically transfer to arbitrary multivariate monomials. A new generic helper proof cannot be counted as an existing mathlib replacement. A future closing simp normalization would require Phase6b judgment rather than automatic NO. Accepted/rejected exact executed sources and raw native receipts are indexed by [verification](../evidence/Roth.exists_primitive_smul_eq/verification.json).

## Phase 7 — Actionable verdict

YES-but-generalise-first, reason MODERN-IDIOM. The verified full normalized-GCD-domain/fraction-field theorem preserves the complete scalar/map/gcd1 conclusion and genuinely expands the coefficient interface, without replacing a parent definition or changing polynomial representation. The missing API is the primitive integral representative of a nonzero multivariate fraction-field polynomial: existing localization supplies integrality and `Finset.extract_gcd` supplies a finite coefficient function, but neither returns the mapped polynomial and primitive scalar relation. The intervening coefficient reconstruction and support transport are a real proof, not a ≤three-call wrapper. Generic content/primPart definitions may be valuable later but are not a prerequisite. This verdict does not depend on proof cost, the preceding theorem's verdict, or search failure. The broader proof and its concrete specialization, rather than an unsupported assumption-drop claim, justify generalise-first.

Proposed declaration: `MvPolynomial.exists_primitive_smul_eq` with the exact full signature in Phase4b. Proposed upstream file: new `Mathlib/RingTheory/MvPolynomial/Content.lean`, importing `Mathlib.Algebra.GCDMonoid.Finset`, `Mathlib.RingTheory.MvPolynomial.Localization`, and `Mathlib.RingTheory.Localization.FractionRing` (precise minimal imports to be checked during cleanup). This initial theorem can expose `support.gcd coeff = 1`; no new computational content/primitive-part definition is required. Proposed PR title: **feat(MvPolynomial): primitive representatives over fraction fields**.

Grouping: tracked progress was read before selecting already accepted YES declarations. `Roth.exists_separated_representation` (YES-but-generalise-first) and `Roth.hasseDeriv_rename_mul_aeval` (YES-but-generalise-first) belong to the broader separation development and can share a coordinated upstream series. Keep this normalization PR mathematically focused; it does not require bundling unrelated Hasse/Taylor/Wronskian work. The predecessor `Roth.exists_nat_smul_eq_map` is BORDERLINE and is not represented as accepted YES. Reviewer candidates: Junyan Xu (2f35248703, normalized-monoid assumption refactor) is the strongest subject fit; Kim Morrison (6d1799a50b, relevant backward-defeq cleanup) is a secondary candidate. These are recent relevant-file history candidates, not a claim of maintainer assignment or availability. [Actual Git log receipt](../evidence/Roth.exists_primitive_smul_eq/primitive-reviewer-commits.json), [selection](../evidence/Roth.exists_primitive_smul_eq/reviewers.json). No outbound message was sent.

Next actions: run `/generalise Roth.exists_primitive_smul_eq` against the already checked full R/K signature; run `/cleanup Roth/Separation.lean Roth.exists_primitive_smul_eq`; prepare the new upstream module with mathlib namespace/name/docs, verify minimal imports and generic theorem, test the literal ℤ/ℚ specialization and the full `exists_int_factors` consumer, and run `/pre-submit` before any PR. `gcd1` must retain normalized-GCD semantics: do not silently replace it by a unit-ideal/unimodular predicate over non-Bézout domains. Preserve arbitrary `σ` and `G ≠ 0`.

Alternative local destination until accepted: `Roth/Separation.lean`, because its sole caller uses every conclusion. At `Roth.exists_int_factors:491`, replace the project call with the new generic theorem specialized to `R := ℤ`, `K := ℚ`; the verified specialization confirms the cast-map interface. Do not delete the current theorem on the false premise that a generic denominator-clearing theorem already handles primitivity. This assessment itself changes no production code and opens no PR.

## Phase 8 — Verification handoff

All required phases complete, with theorem-only n/a rows justified. Portable read-only validator checks phase keys, required overview schema, complete current manifest hashes/bytes, native success and standard axioms, exact canonical293 order/uniqueness, fresh source/pin hashes, caller inventory, formal-search15 cells, literature coverage, evidence links and secret guard. [Assessment](../evidence/Roth.exists_primitive_smul_eq/assessment.json), [verification index](../evidence/Roth.exists_primitive_smul_eq/verification.json), [portable validator](../evidence/Roth.exists_primitive_smul_eq/validate.py), [manifest](../evidence/Roth.exists_primitive_smul_eq/copy-manifest.json). Verification unresolved list is empty after accepted native executions; optional future content/Finsupp API design does not imply incomplete evidence. Root independently reviews before publication.
