# Roth.boxFamily_finite — completed single-declaration assessment

Verdict: **BORDERLINE-needs-human**. Canonical245, `Roth/MainLemma.lean:301–305`.
All required assessment work is complete; the three future upstream questions are design decisions,
not user blockers. Production Lean sources, pins, Git and overview/progress were not modified.

## Phase 0 — baseline and identity

Fresh hashes of all17 production source/pin inputs equal the shared manifest; the accepted baseline
was clean2467jobs. This declaration is not a file-end checkpoint; no new whole-project build was due.
The entire MainLemma module (including its main lemma and actual pigeonhole caller) was read and
replayed in a fresh namespace, renaming only the target outside the canonical array.
The exact tracked canonical293 array passes the independent pre-execution gate and the native
requested/unique/present/value checks, all293. No partial response is accepted.
Evidence: [inputs.json](../evidence/Roth.boxFamily_finite/inputs.json), [input-manifest.json](../evidence/Roth.boxFamily_finite/input-manifest.json), [baseline-build.txt](../evidence/Roth.boxFamily_finite/baseline-build.txt),
[source-MainLemma.lean.txt](../evidence/Roth.boxFamily_finite/source-MainLemma.lean.txt), [original-executed.lean.txt](../evidence/Roth.boxFamily_finite/original-executed.lean.txt), [original-receipt.json](../evidence/Roth.boxFamily_finite/original-receipt.json),
[preparation-checks.json](../evidence/Roth.boxFamily_finite/preparation-checks.json).

## Phase 1 — statement and mathematical argument

Fix a variable type σ, a natural coordinate-degree bound r, and a natural coefficient bound B.
If only finitely many coordinates have nonzero r, only finitely many monomials can occur.
Each such monomial has one of the finitely many integer coefficients 0,…,B, so the entire
polynomial family is finite. The proof identifies it with an image of the finite coefficient-array
product. The representation equality, including the off-box zero coefficients, is substantive;
the final image-finiteness step is generic set theory.

Full native type (`Lean.getConstInfo`, `pp.funBinderTypes`):

```lean
∀ {σ : Type u_1} (r : σ → ℕ) [Finite ↑(Function.support r)] (B : ℕ), (Roth.boxFamily r B).Finite
```

σ is universe polymorphic; r and B are semantic bounds; `[Finite (Function.support r)]` is
the sole finiteness assumption. The conclusion is `Set.Finite`, not an enumeration.
Source body dependency: `Roth.boxFamily_eq_image_finsupp_aux`; source type dependency:
`Roth.boxFamily`. Kernel body additionally mentions `Roth.boxFamily` in its type transports
and the private name `_private.Roth.MainLemma.0.Roth.boxFamily_eq_image_finsupp_aux`.
These scopes differ. Exact type and body evidence: [native-type.json](../evidence/Roth.boxFamily_finite/native-type.json),
[dependencies-executed.lean.txt](../evidence/Roth.boxFamily_finite/dependencies-executed.lean.txt), [dependencies-receipt.json](../evidence/Roth.boxFamily_finite/dependencies-receipt.json).
The initial `pp.all` output elides9641characters and is **not a full kernel-body dump**.
A later compact printer emits the complete proof term without elision in the accepted dependencies
receipt. The full written source is separately archived.

## Phase 2 — preliminary checks

SMALL: an auxiliary finiteness theorem, not a named main result or a new structure.
The four proof lines do not determine contribution value. The one-line-definition test is
n/a because this declaration is a theorem. No exemption is being used to avoid the search.

## Phase 3 — exhaustive literature

| Channel | Exact query/access and result | Mathematical relevance |
|---|---|---|
| General specific | Integer multivariate polynomials, bounded degree and bounded coefficients, finite set, Roth auxiliary polynomial; [web-general.json](../evidence/Roth.boxFamily_finite/web-general.json) | Local paper supplies exact box count. General web context is related height finiteness. |
| General abstract | Finite support functions, finite coefficient choices, finite Cartesian products; same receipt | Finite product/image is the right elementary abstraction, without an ambient finite variable type. |
| General alias | Northcott finiteness, bounded height and degree; same receipt | Related bounded-complexity terminology, not a claim this theorem is Northcott. |
| Optional ChatGPT math | Unavailable tool; justified skip | No external answer is invented. |
| Local clean.tex | Lemma9 proof, displayed coefficient box, eq43; [local-excerpt.tex.txt](../evidence/Roth.boxFamily_finite/local-excerpt.tex.txt), [local-literature.json](../evidence/Roth.boxFamily_finite/local-literature.json) | Exact original family has finite m and count (B₁+1)^∏(rⱼ+1). Lean already supports infinite ambient σ with finite r support. |
| nLab | `site:ncatlab.org/nlab finite set finite product finite support functions`; [web-channels.json](../evidence/Roth.boxFamily_finite/web-channels.json) | Finite-set closure and pointed support context. Direct page fetch later failed unsupported XHTML; search result access is distinguished. |
| nCatLab distinct | `site:ncatlab.org/ncatlab finite products finite sets polynomials`; same receipt | Only out-of-namespace /nlab material returned; no exact in-namespace hit. This elementary theorem needs no categorical reformulation. |
| Stacks | Two actual mathematical queries, preserved in [web-channels.json](../evidence/Roth.boxFamily_finite/web-channels.json) and [web-recent.json](../evidence/Roth.boxFamily_finite/web-recent.json) | Broad graded-module chapters, no target law. Exploratory tag00E0 proved irrelevant and is labelled as such. |
| MathOverflow | Integer multivariate coefficient bounds and counting polynomials of bounded height; same two receipts | Pigeonhole coefficient boxes are familiar; discussion is not an exact infinite-variable theorem. |
| Recent arXiv | `site:arxiv.org multivariate polynomials bounded coefficients counting after:2021-10-29 before:2026-10-30`; [web-recent.json](../evidence/Roth.boxFamily_finite/web-recent.json) | arXiv2509.17563 submitted2025-09-22, revised2026-07-07, studies finite-field bounded-degree polynomial spaces, a related generality rather than this law. |

Primary crosschecks and access failures: [web-primary.json](../evidence/Roth.boxFamily_finite/web-primary.json). Each web artifact contains exact
requests, response SHA256/byte count/status, clean selected titles/URLs/locators and original concise
summaries only; no article or search-result bodies are stored. No malformedsite query was used.
Returned query URLs not needed as evidence were omitted. The local source hash is in
[literature-source.json](../evidence/Roth.boxFamily_finite/literature-source.json).

The common content is finite coefficient choices on a fixed finite monomial set. The manuscript's
integer coordinate box is one instance. Finite-field and height literature uses other coefficient
notions, so interval bounds must not be blindly transplanted to arbitrary rings or fields.
Ingram's June2020 slides, slide18, explicitly use bounded integer degree/coefficient finiteness
in a height-finiteness explanation; the recent finite-field paper supplies a different application.
No exact theorem-specific generality is inferred solely from absent search results.

## Phase 4a — all parameters and hypotheses

| Parameter/condition | Current form | Verified analysis |
|---|---|---|
| σ/universe | Arbitrary `Type u_1` | Already permits infinite σ and empty σ; no Fintype strengthening. |
| r | `σ → ℕ` with finite support | Bundling as Finsupp is a representation change. Native `finite_generic` uses `Finsupp.ofSupportFinite` and finite Iic, with its coercion defeq to r. |
| Support hypothesis | `[Finite ↑(Function.support r)]` | Required for general nonzero coefficient boxes: r=1 on ℕ and B=1 contains injectively all X i and is infinite. No iff or maximality criterion is claimed. |
| B | Any natural including0 | No positivity hypothesis to weaken. B=0 gives singleton zero independently of r support. The weaker disjunction B=0∨finite-support compiles. |
| Coefficient type | ℤ | Fresh theorem works over arbitrary `CommSemiring R` with explicitly finite coefficient sets. Merely replacing ℤ by ℚ and keeping intervals would not preserve finiteness. |
| Coefficient choices | Uniform integer interval | Fresh generic finite-support theorem permits coefficient sets varying by monomial; their finiteness is needed only on the selected monomial set. No zero-in-every-set premise is required for finiteness, since incompatible choices may make the family empty. |
| Monomial shape | Coordinate box | Fresh theorem permits an arbitrary finite monomial set, independent of coordinate or total-degree form. |
| Decidability | None in signature | Classical finite enumeration is local; no new public decidability assumption. |

Evidence: [isolated-executed.lean.txt](../evidence/Roth.boxFamily_finite/isolated-executed.lean.txt), [isolated-receipt.json](../evidence/Roth.boxFamily_finite/isolated-receipt.json),
[project-executed.lean.txt](../evidence/Roth.boxFamily_finite/project-executed.lean.txt), [project-receipt.json](../evidence/Roth.boxFamily_finite/project-receipt.json).

## Phase 4b — verified generality verdict

STRICTLY NARROWER in a semantic restatement: arbitrary finite monomial support and finite coefficient
sets were actually proved. This is a new proof, **not existing mathlib**. Within the fixed boxFamily
interface the support hypothesis cannot simply be dropped; the exceptional B=0 branch is separately
verified. The source signature is retained by the original recovery and a compiled proof equality
(the equality certifies type agreement by proof irrelevance, not identical proof syntax).

The proposed reusable semantic type, compiled under the stable18 mathlib-only imports, is:

```lean
{σ R : Type*} → [CommSemiring R] →
  (s : Set (σ →₀ ℕ)) → s.Finite →
  (t : (σ →₀ ℕ) → Set R) → (∀ d ∈ s, (t d).Finite) →
  {P : MvPolynomial σ R | (↑P.support : Set (σ →₀ ℕ)) ⊆ s ∧
    ∀ d, P.coeff d ∈ t d}.Finite
```

The project-context convenience wrapper for coordinate bounds asks finite t d for **all** d;
this is stronger than the primary theorem needs and is not called the weakest formulation.
The compiled generic recovery changes the underlying family/coefficient interface, so it does not
by itself settle YES-generalise-first. The upstream decision is between a semantic corollary and
using the existing enumerated image. Cost does not choose the verdict.

## Phase 4c — modern idiom, nine rows

| # | Question | Answer / concrete consequence |
|---|---|---|
| 1 | Typeclass preambles | Already uses Finite support; local Fintype construction only for enumeration. No custom finiteness predicate. |
| 2 | Filters/topology | No: finite combinatorics, no limit or metric premise. |
| 3 | Universal property | No: a coefficient injection and finite product suffice; no new universal-property class is justified. |
| 4 | Bundled substructure | No: bounded coefficient boxes are not generally closed under addition, so submodule/subring would change the object. |
| 5 | Algebraic hierarchy | Yes: arbitrary CommSemiring with finite coefficient sets is compiled; supports finite coefficient rings and non-interval choices. |
| 6 | Higher categories | No: no categorical hypothesis or additional usable consequence. |
| 7 | Concrete indices | σ already arbitrary. Monomials can be an arbitrary finite set; integer coefficient intervals become finite sets rather than an unjustified generic order. |
| 8 | Concrete-via-abstract | Yes: after the image rewrite, boxFamily occurs zero times in the remaining proof line. Abstract finite-image law already exists. The bridge to that form remains project-only, while the fresh semantic proof uses Set.Finite.pi' and of_injOn. |
| 9 | False-generalisation guard | Pass for finite coefficient sets with verified original specialization. Reject replacing infinite σ by Fintype as a generalization, dropping support unconditionally, or treating arbitrary ordered-field intervals as finite. |

Modern idiom available as a reusable semantic view, but its finiteness law is newly proved here;
no new typeclass or redundant enumerator is proposed. It concretely enables Set.Finite.pi',
Set.Finite.of_injOn, image/subset operations, and support shapes beyond coordinate boxes.

## Phase 4.5 — infrastructure risk

The declaration is a theorem, so the canonical six definition-risk rows are all justified n/a:

| Risk | Verdict / reason |
|---|---|
| Typeclass diamond | n/a: introduces no instance or structure. |
| Reducibility leak | n/a: introduces a proof, not a data definition or reducibility setting. |
| Noncanonical unfolding | n/a: introduces no definitional equality for data. |
| Instance priority | n/a: registers no instance. |
| Universe restriction | n/a: introduces no data universe choice; the theorem retains arbitrary σ. |
| Coercion | n/a: registers no coercion. |

It introduces no data definition, instance, coercion or simp attribute. The scratch generic family
is a probe, not an accepted production definition or instance proposal.

## Phase 4.6 — proof strategy, five rows

| # | Question | Verdict / consequence |
|---|---|---|
| 1 | ε–δ versus filters | n/a: no topology. |
| 2 | Element algebra versus substructures | No refactor into substructures: interval boxes are not closed; support/coeff injection is the meaningful abstraction. |
| 3 | Sequences versus nets | n/a: no analytic limit. |
| 4 | Construction versus universal property | n/a: a finite enumeration is exactly the required object. |
| 5 | Helper mathlib should have | Candidate semantic finite-support/finite-coefficient bridge, tested as a new theorem; Finset.finsupp and Set.Finite.image already cover its enumerated form. |

Current strategy is MATHLIB-IDIOMATIC once the representation is fixed. A semantic API change may
replace the private bridge with the fresh generic theorem, but shortness after a project helper is
not evidence of a strict existing-mathlib composition. No proof-strategy cost drives the verdict.

## Phase 5 — all15 actual formal-search cells

| Form | Method | Exact query/pattern | Result and receipt |
|---|---|---|---|
| current | leanfinder | `Integer multivariate polynomials with finitely supported coordinate degree bounds and coefficients between zero and B form a finite set` | Finsupp.finite_of_degree_le needs Finite σ; unrelated Chevalley bounds do not solve coefficient finiteness. [receipt](../evidence/Roth.boxFamily_finite/search-current-leanfinder.json) |
| current | loogle | `MvPolynomial.degreeOf, Set.Finite` | Empty results for degreeOf plus Set.Finite; not an absence proof. [receipt](../evidence/Roth.boxFamily_finite/search-current-loogle.json) |
| current | leansearch | `The set of integer multivariate polynomials with bounded coordinate degrees and bounded coefficients is finite` | External univariate card_eq_of_natDegree_le_of_coeff_le; pin spells related API Polynomial.ncard_boxPoly. [receipt](../evidence/Roth.boxFamily_finite/search-current-leansearch.json) |
| current | rg | `boxFamily_finite∣finite.*(coeff∣degree)∣card_eq_of_natDegree_le∣degreeOf_le_iff` | No target duplicate; degree/coefficient candidates inspected. [receipt](../evidence/Roth.boxFamily_finite/search-current-rg.json) |
| current | local_search | `boxFamily_finite` | Only project Roth.boxFamily_finite; index:error reported honestly. [receipt](../evidence/Roth.boxFamily_finite/search-current-local_search.json) |
| standard | leanfinder | `Finite set of finitely supported functions whose support lies in a finite set and values in finite sets` | Finset.finsupp / Finsupp.pi are genuine generic enumerators; search prose about Finset zero is checked against pin. [receipt](../evidence/Roth.boxFamily_finite/search-standard-leanfinder.json) |
| standard | loogle | `Finsupp.support, Set.Finite` | ofSupportFinite support identity; no semantic polynomial finite-family law. [receipt](../evidence/Roth.boxFamily_finite/search-standard-loogle.json) |
| standard | leansearch | `Finitely supported functions with support in a fixed finite set and finite coefficient choices form a finite set` | Finset.finsupp and onFinset; Finsupp.fintype requires finite ambient types. [receipt](../evidence/Roth.boxFamily_finite/search-standard-leansearch.json) |
| standard | rg | `finsupp∣finite.*support∣mem_finsupp_iff∣onFinset∣finite.*pi` | mem_finsupp_iff and locally finite Finsupp intervals supply the actual image construction. [receipt](../evidence/Roth.boxFamily_finite/search-standard-rg.json) |
| standard | local_search | `finsupp` | Finset.finsupp candidate; index:error; scratch evidence hits excluded from existing mathlib. [receipt](../evidence/Roth.boxFamily_finite/search-standard-local_search.json) |
| abstract | leanfinder | `The image of a finite set under any function is finite` | Set.Finite.image exact positive generic image law. [receipt](../evidence/Roth.boxFamily_finite/search-abstract-leanfinder.json) |
| abstract | loogle | `Set.Finite, Set.image` | Set.Finite.image / of_finite_image / finite_image_iff; all require a bridge to the target set. [receipt](../evidence/Roth.boxFamily_finite/search-abstract-loogle.json) |
| abstract | leansearch | `A finite image of a finite set is finite` | Finite.Set.finite_image instance; same image representation obligation. [receipt](../evidence/Roth.boxFamily_finite/search-abstract-leansearch.json) |
| abstract | rg | `theorem.*image∣finite_toSet∣Finite.*image∣finite_image_iff∣of_injOn` | Finite.image and Finite.of_injOn read in pinned source. [receipt](../evidence/Roth.boxFamily_finite/search-abstract-rg.json) |
| abstract | local_search | `Set.Finite.image` | Set.Finite.image and image2; index:error, positive source/native verification required. [receipt](../evidence/Roth.boxFamily_finite/search-abstract-local_search.json) |

The external search revision differs from the pin: `Polynomial.card_eq_of_natDegree_le_of_coeff_le`
is returned externally, while the pinned file has `Polynomial.boxPoly`, `Polynomial.ncard_boxPoly`
and `Polynomial.finite_mahlerMeasure_le`. Those are univariate and do not supply the required
arbitrary-variable coefficient/support bridge. Finsupp.finite_of_degree_le requires finite σ and
bounds exponent degree, not polynomial coefficient choices.
All source-based candidates were read in the archived pinned modules:
[mathlib-inputs.json](../evidence/Roth.boxFamily_finite/mathlib-inputs.json). Native positive signatures and stable-prefix availability:
[availability-executed.lean.txt](../evidence/Roth.boxFamily_finite/availability-executed.lean.txt), [availability-receipt.json](../evidence/Roth.boxFamily_finite/availability-receipt.json).
`Finset.finsupp` and Finsupp locally finite intervals are not imported by stable18; they are available
in the actual project document and their image law is compiled there, with no added imports.
A source-wide untruncated target/coefficient search is [full-name-search.json](../evidence/Roth.boxFamily_finite/full-name-search.json).
The local index reports `index:error`; scratch/evidence names it returns never count as mathlib.
Positive candidates are verified against the pin; failed/empty searches do not establish absence.

## Phase 5.5 — statement shape, three checks

1. **Normal form:** Set.Finite is the right output for subsequent `.fintype` use. The finite
   coefficient image and semantic support predicate are not definitionally identical; the private
   bridge proves equality. The native generic recovery verifies the semantic correspondence.
2. **Syntactic generality:** arbitrary finite monomial support avoids committing to coordinate
   degree syntax. Finsupp-bundled r can avoid a separate support instance; original function r is
   retained at the tested caller. The disjunctive B=0 statement is compiled as an optional logical
   weakening, not asserted to be an iff or the preferred main interface.
3. **Superfluous arguments:** σ, r and B describe the family; no argument is redundant. No
   positivity/Nonempty/Fintype σ condition is needed. Removing finite support wholesale is refuted
   by the actual infinite family. Classical decidability is local, not an additional hypothesis.

Statement-shape verdict: RESTATE-BEFORE-SHIP if choosing a semantic upstream theorem; the current
local statement is suitable for its one caller and all boundary cases pass.

## Phase 6.0 — full callers, inline derivations and kernel scopes

| Explicit caller | Source use | Cross-file? | Actual experiment |
|---|---|---|---|
| `Roth.exists_ne_modByMonic_eq`, MainLemma:359–379 | One body occurrence at367; local Fintype for pigeonhole domain | No | Full original statement and body replayed, replacing only the finiteness call by its bridge/image proof; clean success and signature agreement. |

Fresh `rg --no-ignore` and `git grep` agree exactly on the declaration head and the one use:
[source-search.json](../evidence/Roth.boxFamily_finite/source-search.json), [tracked-source-search.json](../evidence/Roth.boxFamily_finite/tracked-source-search.json). Full source caller body/signature
and hash are [callers.json](../evidence/Roth.boxFamily_finite/callers.json); full inventory is [source-inventory.json](../evidence/Roth.boxFamily_finite/source-inventory.json). The canonical
kernel audit independently yields one direct value consumer, zero direct type consumers:
[canonical-consumers.json](../evidence/Roth.boxFamily_finite/canonical-consumers.json). These are distinct from lexical declaration occurrences.
The broader inline audit [inline-audit.json](../evidence/Roth.boxFamily_finite/inline-audit.json) finds the target finiteness proof and
representation/counting code, but no second hidden direct derivation of the same boxFamily
finiteness statement. Other finite-set constructions prove different claims.

No simp attribute is present. Kernel direct-use independence of the inline caller is tested in
[composition-receipt.json](../evidence/Roth.boxFamily_finite/composition-receipt.json): target constant absent, private representation helper present.
The inline still uses `Roth.ncard_boxFamily`, which may share the private bridge. No independence
from all transitive project dependencies is claimed. Likewise, source caller counts are not a
transitive dependency census and the scoped kernel inventory does not pretend otherwise.

## Phase 6 — composition experiments and pairwise duplication audit

The abstract enumerated family has the existing two-call proof:

```lean
(s.finsupp t).finite_toSet.image AddMonoidAlgebra.ofCoeff
```

It was compiled in [composition-executed.lean.txt](../evidence/Roth.boxFamily_finite/composition-executed.lean.txt). Recovering the original boxFamily needs
`Roth.boxFamily_eq_image_finsupp_aux`, not an existing mathlib constant. The exact native caller
inline is in [project-executed.lean.txt](../evidence/Roth.boxFamily_finite/project-executed.lean.txt); this is locally actionable, but it retains that
private helper and is not counted as a pure mathlib-only ≤3-call replacement.
The original target fails the explicit finite-image call and `simp only [Roth.boxFamily]` closure
probes; a fresh generic theorem then closes it. These bounded negative probes are not a universal
proof of library absence. Outcome: **NOT-COMPOSABLE by the strict existing-mathlib criterion**
without the representation bridge. The newly proved semantic bridge is not silently relabelled
as an existing building block. No new imported project definitions are used in the isolated proof.

The parent boxFamily assessment is BORDERLINE, independently checked against the actual image
representation rather than inherited as a verdict. The explicit parent re-aim gate only forces
NO-mathlib-has-it when the parent was replaced by an existing more-general definition with its
analogous existing law. Here the generic image law exists and compiles, but the semantic bridge
is still new/project-only, so that gate does not force NO. This is an interface decision.

| Decl A | Decl B | Same statement? | Same proof? | Verdict |
|---|---|---|---|---|
| boxFamily_finite | boxFamily_eq_image_finsupp_aux | No: finite versus representation equality | Shares representation | Keep distinction; the equality carries normalization content. |
| boxFamily_finite | ncard_boxFamily | No: finite versus exact count | Shared private representation | Coordinate the API; do not use ncard count alone as automatic finiteness (infinite sets have ncard0). |
| boxFamily_finite | box/card_le_card_box | No: polynomial family versus finite exponent box | Both finite-coordinate combinatorics | Distinct coefficient layer; no duplicate statement. |
| boxFamily_finite | finite_mahlerMeasure_le | No: coordinate degrees and nonnegative coefficients versus univariate degree/Mahler measure | Different encodings | Related bounded complexity, no direct specialization verified. |
| boxFamily_finite | Set.Finite.image | Abstract law after bridge | Exact last step only | Reuse image law; retain honest bridge obligation. |

## Phase 7 — verdict and concrete actions

**BORDERLINE-needs-human.** The finiteness theorem is correct, used, and already general in its
variable index. There is a compiled, meaningful broader semantic theorem. The relevant existing
API already enumerates finite coefficient choices, and its image law is immediate, while the
semantic polynomial/degree bridge is substantive new content. Whether to expose a semantic
polynomial finiteness lemma upstream or use the enumerated interface is a mathematical API
boundary. Neither the four-line source spelling nor the parent's later use nor implementation
cost settles that choice. This is not an unsupported absence-based YES or an automatic NO.

Future upstream questions (assessment complete; no response required to finish this report):

1. Should mathlib expose a semantic finite-support/finite-coefficient polynomial finiteness theorem, or should users retain an explicit Finset.finsupp image?
2. If a semantic theorem is wanted, should its primary statement use an arbitrary finite monomial set and coefficient sets, with coordinate-degree boxes as corollaries?
3. Should the integer coordinate-box definition and its finiteness corollary stay local to Roth while only the reusable coefficient-support bridge is proposed upstream?

Alternative local destination: retain `Roth/MainLemma.lean` near the private coefficient-box
representation. If local cleanup is chosen, the sole caller can inline the verified bridge/image
proof, preserving its exact statement; no other caller needs changing. If proposing upstream,
use the arbitrary finite-monomial/finite-coefficient statement above and assess its home near
MvPolynomial support APIs with the Finset/Finsupp import layering made explicit. No upstream
PR title, reviewer, or grouping with accepted YES declarations is claimed for this BORDERLINE
assessment; those YES-only requirements are n/a. No production edit or PR was made.

## Phase 8 — verification, limits and frozen handoff

All accepted executions have complete clean diagnostics and only propext/Classical.choice/Quot.sound.
Exact executed sources, unchanged full raw native requests/results and elapsed_ms are linked by
[verification.json](../evidence/Roth.boxFamily_finite/verification.json). Three rejected isolated attempts, one rejected project elaboration,
one rejected project warning-only attempt and one rejected dependency-audit typo are retained;
none is accepted proof evidence. Initial cold original elaboration was partial and is retained
as warming only. No sorry/new axiom/unsafe/native_decide or resource-limit increase is accepted.
The final proof sets are original, availability, isolated, project, composition and dependencies.

The portable read-only validator checks current manifest hashes/bytes, fresh17 inputs, exact293
source/runtime array, accepted diagnostics/axioms, formal15 searches, caller/source consistency,
report links and secret guard, and supports scratch plus integrated layouts:
[validate.py](../evidence/Roth.boxFamily_finite/validate.py). Current supporting artifact inventory is [copy-manifest.json](../evidence/Roth.boxFamily_finite/copy-manifest.json).
Root acceptance remains pending and is independent of the worker's checks.
