# Roth.wronskian_ne_zero_of_linearIndependent

**Verdict: BORDERLINE-needs-human.** The hard direction of the polynomial Wronskian criterion is substantial missing mathematics for mathlib. Upstreaming it needs a decision about the n-ary Wronskian interface and the coefficient-ring theorem. This is not a composition or a verdict inherited from a parent definition.

## Phase 0 — Doctor

The reusable baseline is a successful `lake build` (2467 jobs); all 17 source/pin SHA256 values were freshly checked against the shared input manifest. [Baseline](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/baseline-build.txt); [fresh hash check](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/input-hash-check.json); [manifest](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/input-manifest.json).
The declaration resolves at `Roth/Wronskian.lean:205`, is a theorem without sorry, and the original proof was replayed successfully with only `propext, Classical.choice, Quot.sound`. [Exact executed source](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/native-target-executed.lean.txt); [complete native receipt](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/native-target-success.json).
The whole declaring module and both external caller modules were read. [Wronskian](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/Wronskian-module.lean.txt), [GenWronskian](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/GenWronskian-module.lean.txt), [Separation](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/Separation-module.lean.txt).

## Phase 1 — Comprehend

For any finite family of univariate polynomials over a characteristic-zero field, linear independence over the coefficient field implies that the determinant of their successive Hasse derivatives is a nonzero polynomial. Rows have orders 0 through l−1. This states polynomial nonvanishing, not nonvanishing at every evaluation point.

Full native type:

```lean
∀ {K : Type u_2} [inst : Field K] {l : ℕ} [CharZero K] {φ : Fin l → K[X]},
  LinearIndependent K φ → Roth.wronskian φ ≠ 0
```

K is the coefficient field, l the family length (including zero), φ the polynomial family, and h its independence over K. The conclusion uses the determinant of `Polynomial.hasseDeriv μ (φ ν)`. Strong induction on the sum of natural degrees reduces repeated degrees by cancellation of a leading coefficient. A constant column shear preserves the determinant and linear independence, and strictly lowers that sum. Distinct degrees then give a nonzero top coefficient via the binomial/Vandermonde determinant.

Project dependencies are `wronskian`, `wronskian_ne_zero_of_natDegree_injective`, `wronskian_update_sub_smul`, `sum_natDegree_update_lt`, and `linearIndependent_update_sub_smul`. The last has an existing general shear replacement; that fact alone does not supply this theorem. Neither the downstream iff nor the generalized Wronskian theorem is used to prove the criterion.

## Phase 2 — Preliminary checks

**BIG.** This is the hard implication of the named Wronskian criterion, whose combined iff is a main result of the module, and it is essential to the multivariate and separation arguments. It is not mere determinant bookkeeping. Phase 2b one-line-definition test: n/a, theorem.

## Phase 3 — Exhaustive literature

Every named channel was actually attempted. Exact requests and response SHA256/byte counts are retained; full returned article/search bodies are not archived. The protocol's informal “nine channels” does not replace any named row.

| Channel | Exact request artifact | Finding / limitation |
|---|---|---|
| General web, current form | [request](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/web-general-current.json) | “Wronskian linearly independent polynomials characteristic zero Hasse derivatives theorem”; Bostan–Dumas and Hasse/ordinary comparison sources |
| General web, standard / named form | [request](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/web-general-standard.json) | “Bostan Dumas Wronskians and linear independence formal power series polynomials 2010”; primary paper identified |
| General web, abstract form | [request](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/web-general-abstract.json) | “Wronskian criterion differential field constants positive characteristic Hasse derivatives”; differential-field criterion |
| General web, domain refinement | [request](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/web-domain.json) | Integral-domain/fraction-field search; domain extension requires descent, not an unsupported drop of Field |
| Optional mathematical ChatGPT | n/a | `ask_chatgpt_math` unavailable in tool inventory; no simulated second opinion |
| Local reference | [source receipt](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/local-reference.json) | `clean.tex` §2 lines157–195: rational-coefficient Hasse Wronskian iff and degree-elimination proof |
| nLab | [search](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/web-nlab.json), [open](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/web-primary-nlab.json) | Wronskian entry found; direct open failed with unsupported application/xhtml+xml (400); search excerpt inspected |
| nCatLab | [request](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/web-ncatlab.json) | Separate site-wide differential-field search; Wronskian entry and differential-equation material, no stronger categorical interface located |
| Stacks Project | [request](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/web-stacks.json) | Results concern independence of characters, not a Wronskian theorem; no direct match identified |
| MathOverflow | [request](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/web-mathoverflow.json) | Positive-characteristic/Hasse query returns differential-operator and geometric discussions; not treated as the proof authority |
| Recent arXiv, window2021-10-27–2026-10-27 | [initial](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/web-arxiv.json), [Hasse-refined](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/web-primary-recent.json), [date-refined](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/web-recent-refined.json) | 2022 generalized polylogarithm and 2023 derivative-family applications; exact Hasse refinement empty. Recent applications do not replace the standard polynomial theorem. |

Primary sources actually inspected:

* [Bostan–Dumas, Wronskians and linear independence](https://mathexp.eu/dumas/publications/Bostan_Dumas_2010_WLI.pdf), Theorem2 pp1–2, Lemma2–3 p3, proof p4: power series/rational functions in characteristic zero; invertible constant change of basis and Vandermonde nonvanishing. Their ordinary derivatives differ from Hasse rows by invertible factorial factors here. [Access metadata](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/web-primary-bostan.json).
* [Churchill–Kovacic, Introduction to Differential Galois Theory](https://ksda.ccny.cuny.edu/PostedPapers/intro.pdf), Proposition2.1.1 p17, Proposition3.12.2/Corollary3.12.3 pp71–73: differential-field independence is over its field of constants. The discussion after Corollary3.12.3 distinguishes fraction-field constants from fractions of ring constants. [Access metadata](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/web-primary-differential.json).

Standard concept: the Wronskian criterion / Wronskian test for linear independence. The polynomial characteristic-zero field formulation agrees with the literature; local rational coefficients are already generalized. Power-series/rational-function and abstract differential-field forms are broader representations, not mechanical edits of a theorem about K[X]. Historical sources use ordinary derivatives; the local normalized Hasse convention is equivalent in characteristic zero. General arbitrary smooth functions and arbitrary positive-characteristic base-field independence are false extensions.

## Phase 4a–4b — Generality

| Parameter / assumption | Used? | Weakening assessment |
|---|---|---|
| K : Type* | yes | Already universe polymorphic |
| Field K | yes in current proof/interface | Leading-coefficient division and inherited parents need a field. DivisionRing alone cannot support this commutative determinant interface. An expanded domain theorem via fraction fields is a real alternative; it is a new descent proof, not a successful same-parent drop-test. |
| l : ℕ | yes | Includes l=0 and l=1, no positivity hypothesis to remove. Ordered consecutive Hasse rows depend on Fin l; arbitrary finite column labels require an enumeration/reindexing design. |
| CharZero K | yes | Needed for distinct degree casts / factorial nonvanishing; independence of 1 and X^p does not force nonzero first-consecutive-row Wronskian in characteristic p. |
| φ : Fin l → K[X] | yes | Already an arbitrary family; rational functions/power series/differential fields need different ambient structures and constants bookkeeping. |
| h : LinearIndependent K φ | yes | Removing it permits the zero family; independence supplies nonzero entries and prevents cancellation producing zero. |

Generality verdict: current form is standard **within its Field-bound parent interface**, but a characteristic-zero integral-domain version is mathematically meaningful. Proposed expanded representation:

```lean
{R : Type*} [CommRing R] [IsDomain R] [CharZero R] {l : ℕ}
{φ : Fin l → R[X]} (hφ : LinearIndependent R φ) :
  (Matrix.of fun μ ν : Fin l ↦ Polynomial.hasseDeriv (μ : ℕ) (φ ν)).det ≠ 0
```

The domain proposal preserves both the polynomial object and the scalar ring in the independence statement. **The complete expanded theorem was compiled successfully**, using extension to the fraction field, then commutation of polynomial map with Hasse derivatives and determinant. Its Field criterion is an explicit replay of the original induction, not the target theorem or downstream iff. [Exact executed source](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/native-domain-executed.lean.txt); [clean complete native receipt](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/native-domain-success.json). It does not pretend that `Roth.wronskian` currently elaborates under CommRing. This adds a new descent proof and needs a parent interface decision, so the reference's Class5 prevents treating it as a one-edit YES-generalise weakening. A general differential-field theorem must use constants of the derivation; replacing these with arbitrary base scalars is rejected.

## Phase 4c — Modern idiom, all nine rows

| # | Question | Result and concrete consequences |
|---|---|---|
| 1 | Typeclasses instead of preambles | Already Field and CharZero classes; no extra predicate class needed |
| 2 | Filters/nets instead of sequences | n/a: finite algebraic criterion, no limits |
| 3 | Universal property instead of construction | No new object constructed by this theorem; fraction-field universal property helps its proposed domain proof |
| 4 | Bundled substructures | A degree-filtered submodule/basis-echelon API could package elimination, but no existing direct criterion was found; avoid inventing a new closure predicate |
| 5 | Field hierarchy weakening | Yes, domain-expanded criterion composes with `LinearIndependent.iff_fractionRing`, polynomial map, and `hasseDeriv_map`; useful for integral polynomial families without first restating them over a field |
| 6 | Higher-category formulation | No relevant categorical content |
| 7 | Concrete index generalization | Fin rows encode consecutive derivative orders; arbitrary finite columns require chosen enumeration. An arbitrary additive-group index would change the object. |
| 8 | Concrete-via-abstract diagnostic | Proof-body audit: no concrete named coefficient field/witness is present. Wronskian appears through its specific shear and distinct-degree laws, not through an accidental one-off witness. A generic “invariant under degree-lowering shears” induction schema would still assume the missing Wronskian facts and is not a replacement. |
| 9 | False-generalization guard | Domain polynomial determinant preserves the object. Arbitrary linear operators do not satisfy this criterion; arbitrary smooth functions fail it; dropping CharZero while keeping base-field independence fails it. Higher Hasse orders may work in characteristic p for particular families, so do not claim all Hasse Wronskians vanish there. |

Modern-idiom verdict: a domain-level polynomial API has a concrete mathematical benefit; the abstract differential-field extension is also substantial but changes ambient representation and needs a separate constants API. These are interface/proof choices, not a license to invent a verified mechanical weakening.

## Phase 4.5 — Infrastructure risks

n/a: theorem. Typeclass diamond, reducibility leak, noncanonical unfolding, instance priority collision, universe-instance issues, and coercion ambiguity introduce no new infrastructure here. The existing parent-definition interface questions are tracked separately; this theorem does not inherit their verdict.

## Phase 4.6 — Proof-strategy optimality

| Row | Applicability / conclusion |
|---|---|
| Topology: epsilon/delta versus filters | n/a |
| Algebra: elements versus bundled submodule statements | Degree-elimination proof is appropriate; an echelon-basis lemma for a finite-dimensional polynomial subspace could expose the key structure. It would be new API, not a ≤3-call replacement. |
| Analysis: sequences versus nets | n/a |
| Category theory: construction versus universal property | n/a for the current proof; fraction-field transport is appropriate for the domain proposal |
| Missing helper API | N-ary Wronskian itself is explicitly TODO upstream; echelonization / distinct-degree basis may be reusable, while finite-family sum-decrease bookkeeping need not be public Wronskian API. |

Proof-strategy verdict: current strong induction is mathematically sound and matches the source elimination argument. Prefer a reusable polynomial echelon lemma if designed; do not replace the proof by downstream iff/generalized criterion, which would be circular.

## Phase 5 — All five actual mathlib searches

Each API was called on current Hasse determinant, standard ordinary-polynomial criterion, and abstract differential-field/constants forms; domain-expanded probes were added as a fourth form.

| Method | Current | Standard | Abstract | Domain |
|---|---|---|---|---|
| Finder | [raw](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/formal-finder-current.json) | [raw](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/formal-finder-standard.json) | [raw](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/formal-finder-abstract.json) | [raw](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/formal-finder-domain.json) |
| Loogle | [raw](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/formal-loogle-current.json) | [raw](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/formal-loogle-standard.json) | [raw](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/formal-loogle-abstract.json) | [raw](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/formal-loogle-domain.json) |
| LeanSearch | [raw](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/formal-leansearch-current.json) | [raw](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/formal-leansearch-standard.json) | [raw](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/formal-leansearch-abstract.json) | [raw](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/formal-leansearch-domain.json) |
| Source rg | [raw](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/rg-current.json) | [raw](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/rg-standard.json) | [raw](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/rg-abstract.json) | `iff_fractionRing` included in abstract source search |
| Local name index | [raw](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/formal-local-current.json) | [raw](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/formal-local-standard.json) | [raw](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/formal-local-abstract.json) | [raw](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/formal-local-domain.json) |

Local results include project/evidence declarations and may mark the index unavailable. They establish neither pinned mathlib completeness nor absence. External indices can differ from the project's pin; pinned candidate signatures and actual experiments are required.

Candidate adjudication: `Polynomial.wronskian` is binary, not n-ary; `IsCoprime.wronskian_eq_zero_iff` additionally assumes coprimeness and concerns vanishing derivatives of two polynomials. `Matrix.linearIndependent_cols_of_det_ne_zero` goes in the other direction and uses scalars in the matrix coefficient ring. A generic determinant criterion over the fraction field of K[X] would still require proving independence of the jet columns over that field; h only gives independence of the original polynomials over K. Gram/discriminant determinants are different matrices. `LinearIndependent.iff_fractionRing` transports scalars and helps the new domain proof; it does not prove field Wronskian nonvanishing.

The pinned `Mathlib/RingTheory/Polynomial/Wronskian.lean` explicitly has TODO “Define Wronskian for n-tuple of polynomials, not necessarily two.” [Pinned source](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/Wronskian-mathlib.lean.txt). This is a specific missing-API anchor, beyond unsuccessful searches.

## Phase 5.5 — Statement shape

Normal forms considered: (1) LI implies W≠0, (2) W≠0 iff LI, (3) W=0 iff not LI. The implication is a useful primary lemma and all actual callers supply independence. The full iff belongs with the completed easy direction, not as a circular replacement. Binary `Polynomial.wronskian` cannot be reused without a naming/interface decision.

Syntactic generality: keep φ implicit and h explicit; this supports `apply` in GenWronskian and direct tuple insertion in Separation. The expanded determinant/domain formulation permits weakening without asserting unsupported instances for the current parent. No arbitrary l>0 hypothesis or separate nonzero hypotheses should be added. Every parameter was audited in Phase4a; h is sufficient without requiring pairwise distinct input degrees.

Shape verdict: **RESTATE-BEFORE-SHIP** if adopting the domain interface; original implication shape is otherwise appropriate. Full iff is a companion, not an independently available mathlib building block.

## Phase 6.0 — All explicit source callers and inline audit

[Exact whole-source search](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/callers.json); [inline-derivation search](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/inline.json).

Internal use count excluding declaring module: **2**, in **2** files. Including same-module use: **3** explicit source calls.

| Location | Actual use | Upstream migration |
|---|---|---|
| Roth/Wronskian.lean:221, `wronskian_eq_zero_iff` | `imp_not_comm.mp wronskian_ne_zero_of_linearIndependent` | Use the adopted upstream implication, keeping easy direction; do not prove implication through this iff |
| Roth/GenWronskian.lean:262, `exists_genWronskian_ne_zero` | `apply wronskian_ne_zero_of_linearIndependent` after contradiction, then LI of Kronecker-substituted family | Apply upstream criterion to the same univariate family; namespace/interface bridge only after chosen API |
| Roth/Separation.lean:534, private `exists_rat_factors_det_hasseDeriv_aux` | tuple entry `wronskian_ne_zero_of_linearIndependent hφ` for a rational separated factor | Supply upstream theorem specialized to ℚ; adjust determinant spelling if parent replaced |

No independent inline re-derivation of the full hard implication was identified. The distinct-degree theorem is a proper subcase, and the generalized criterion is a downstream consumer. These counts describe explicit source references, not kernel/simp dependency closure. The two external applications plus same-module iff establish useful API, even without the heuristic threshold of three external calls.

Native migration checks succeeded: the expanded domain theorem recovers the exact original Field statement by the definitional equality of its raw determinant with the current parent; the same-file iff was completely rebuilt using that recovered statement and the easy direction. The generalized-Wronskian consumer was checked as its typed contradiction fragment with χ denoting the already-constructed Kronecker family. The separation consumer was checked as its final existential construction with the already-produced nonzero generalized factor and factorization equality as parameters. [Exact executed source](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/native-callers-executed.lean.txt); [accepted complete receipt](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/native-callers-success.json). These are a full same-file iff rebuild and typed external application fragments, **not** complete migrated GenWronskian/Separation module builds. The unchanged production modules retain the verified baseline.

## Phase 6 — Actual composition analysis

Attempt1: generic matrix determinant/independence. Its needed jet-column independence over K(X) is the hard missing content. Independence over K of φ does not supply it by definitional equality.
Attempt2: binary coprime Wronskian theorem. It cannot handle arbitrary l and its coprimeness hypothesis is absent.
Attempt3: distinct-degree Wronskian nonvanishing plus an independence-preserving shear. Arbitrary independent input can have repeated degrees, so it requires well-founded iteration; the current proof performs precisely that new mathematics. Project helpers are not counted as existing mathlib calls.

Conclusion: **NOT-COMPOSABLE** from ≤3 existing mathlib calls. No closing `simp [defs]` composition was found. The isolated raw determinant `exact?` experiment failed to close, without timing out; this is limited evidence about that attempt, not a proof of absence. [Exact failed composition source](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/native-composition-executed.lean.txt); [rejected receipt](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/native-composition-rejected.json). Fraction-field descent presupposes a newly proved field criterion, so it is not an existing-mathlib replacement.

The positive candidates' exact pinned signatures were checked in a mathlib-only isolated experiment with `#check_failure Roth.wronskian_ne_zero_of_linearIndependent`. The guessed `Polynomial.wronskian_eq_zero_iff` is unavailable under that spelling in the tested import context; this check alone does not establish global absence. The pinned binary module was separately read and source-searched. The same experiment **proved both** that `![1,X²]` is linearly independent over ZMod2 and that its consecutive Hasse Wronskian determinant is zero. It uses no new axioms or limit increases. [Exact source](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/native-guards-executed.lean.txt); [accepted receipt](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/native-guards-success.json). Initial domain preparation errors are retained separately as rejected evidence and are not verification success. [Rejected domain preparation](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/native-domain-rejected.json).

## Phase 7 — Verdict and gate

**BORDERLINE-needs-human.** The specific upstream gap is the n-ary polynomial Wronskian TODO and its independence criterion. A complete polynomial criterion should be contributed once the determinant representation and coefficient-ring scope are chosen. The judgement concerns the public mathematical interface: the current two parents require Field, while a ring-defined Hasse determinant supports a domain theorem. The applicable routing instruction is [False-positive Class5, exact installed excerpt](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/class5-routing-reference.md), with [original path/hash and excerpt lines](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/class5-reference-metadata.json): a foundational-definition change is not a single mechanical weakening. This is not a cost-based downgrade and not blanket inheritance from the two BORDERLINE parents.

The named fields, source theorem, independent induction replay, full searches, scalar mismatch in the generic determinant route, and caller inventory support retaining the theorem locally. The proposed domain extension is evidence for a better upstream interface, not a claim that changing one typeclass in the original proof suffices.

Concrete upstream API questions:

1. Should the n-ary polynomial Wronskian be defined over CommRing using Hasse derivatives, with this criterion over IsDomain+CharZero, rather than keeping the current Field-bound parent?
2. Should the public n-ary object get a distinct name from binary `Polynomial.wronskian`, with an explicit Fin2 bridge?
3. Should the first PR expose a distinct-degree basis/echelon lemma for polynomial subspaces, or retain degree-sum induction internally?

Action: retain `Roth/Wronskian.lean` as local destination until this API decision; target `Mathlib/RingTheory/Polynomial/Wronskian.lean` for eventual upstream work. Do not delete the three caller applications. A future PR can group the already accepted YES `Roth.det_choose_eq`, `Roth.coeff_wronskian_of_natDegree_injective`, and `Roth.wronskian_ne_zero_of_natDegree_injective` (their exact verdicts were read from progress.json); the parent definitions require their own design resolution. Proposed title: “feat(Polynomial): add n-ary Hasse Wronskian criterion”. Before opening: `/generalise Roth.wronskian_ne_zero_of_linearIndependent`; `/cleanup Roth/Wronskian.lean Roth.wronskian_ne_zero_of_linearIndependent`; choose a reviewer from relevant recent commits. Moritz Firsching's pinned Hasse-map addition and Yaël Dillies' algebra API work are concrete starting points, not claimed reviewer acceptance. [Commit receipt](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/reviewers.json).

Phase7 gate: no invented mathlib theorem, no unsupported ≤3-call proof, no unverified same-parent weakening, no circular criterion, no cost factor, all callers recorded. Remaining questions concern future upstream choices, so assessment verification can finish with unresolved=[].

## Phase 8 — Consolidated report and next action

All required phases, searches, parameter checks, modern-idiom rows, proof-strategy rows, source callers, exact native sources, and validator are represented in this report and linked evidence. Optional mathematical ChatGPT is unavailable; nLab direct access failed as documented. The theorem remains useful project-local mathematics while the numbered upstream API questions are resolved. No production source, pin, or project Git state was changed by this assessment.

[Verification index](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/verification.json), [current copy manifest](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/copy-manifest.json), [portable read-only validator](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/validate.py), and [targeted credential guard receipt](../evidence/Roth.wronskian_ne_zero_of_linearIndependent/credential-guard.json) provide the final handoff. Accepted native evidence consists of the exact target replay, complete expanded domain proof, isolated characteristic-two guards/pinned signatures, and original-statement recovery plus caller checks. The rejected composition attempt and initial domain preparation remain explicitly rejected; neither contributes proof success. All accepted runs completed without partial results, errors, warnings, nonstandard axioms, or raised resource limits. Run the validator with the project root as its argument in scratch or integrated layout; it always validates the current manifest, never a historical worker manifest.

