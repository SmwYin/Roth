# Full mathlibable assessment — `Roth.linearIndependent_update_sub_smul`

Canonical 49; source `Roth/Wronskian.lean:170–176`; branch `ramin-cleanup`.
**Verdict: NO-mathlib-has-it.** Mathlib already proves the elementary shear law as
`linearIndependent_add_smul_iff`, for arbitrary indexed modules over rings, with arbitrary
coefficient functions vanishing at the source. The single polynomial update is its specialisation.
This verdict is independently established; no inheritance from canonical 48 applies.

## Phase 0 — Doctor

Reused successful `lake build` (2467 jobs, exit 0) only after freshly matching all 17 production
source/pin hashes against the shared baseline manifest. [Baseline](../evidence/Roth.linearIndependent_update_sub_smul/baseline-build.txt),
[fresh inputs](../evidence/Roth.linearIndependent_update_sub_smul/inputs.json). The theorem resolves, contains no sorry, and native
replay/type/axioms succeed with partial=false. The declaring module was read in full: it develops
finite polynomial Hasse Wronskians and proves nonvanishing from linear independence by decreasing
the sum of degrees. Both actual callers were read in full, then rebuilt.
[Complete native target receipt](../evidence/Roth.linearIndependent_update_sub_smul/target-success.json),
[exact executed source](../evidence/Roth.linearIndependent_update_sub_smul/target-executed.lean.txt),
[whole module](../evidence/Roth.linearIndependent_update_sub_smul/Wronskian.lean.txt).

## Phase 1 — Comprehend

Subtracting a scalar multiple of one member of a linearly independent polynomial family from a
different member preserves linear independence. The source vector remains unchanged; adding the
same scalar multiple back reverses the operation. The current proof instead uses preservation of
the span and the equality between the family cardinality and the dimension of its span.

Full native elaborated type (universe name immaterial):

```lean
@Roth.linearIndependent_update_sub_smul :
  ∀ {K : Type u_1} [inst : Field K] {l : ℕ} {φ : Fin l → K[X]} {ν ν' : Fin l},
    ν ≠ ν' → ∀ (c : K), LinearIndependent K φ →
      LinearIndependent K (Function.update φ ν' (φ ν' - C c * φ ν))
```

Parameters: coefficient field K; family length l; polynomial family φ; source ν and destination ν';
distinctness h; arbitrary scalar c; initial independence hφ. There is **no CharZero assumption**.
The theorem does not mention `Roth.wronskian` or `wronskianMatrix`.

Project dependencies: no project theorem/definition occurs in this proof. Mathlib dependencies:
`linearIndependent_iff_card_eq_finrank_span` (twice), `Set.finrank`,
`Polynomial.smul_eq_C_mul`, `Submodule.span_range_update_sub_smul`.

## Phase 2 — Preliminary checks

SMALL: elementary linear-algebra helper, not a main result, new structure, or named theorem.
The definition-only one-line/exemption test is n/a: this is a theorem. The substantive proof is
three tactic lines; short syntax alone does not establish strict composability.

## Phase 3 — Exhaustive literature

Exact requests, response SHA256/bytes, titles and URLs are archived in
[web evidence](../evidence/Roth.linearIndependent_update_sub_smul/web-evidence.json); no full web bodies are stored.
The following are original summaries, not quotations.

| Channel | Actual query/access | Outcome |
|---|---|---|
| General web: specific | linearly independent polynomials subtract constant multiple column operation preserves independence | Standard elementary column operations; polynomial context is incidental. |
| General web: general | elementary transvection module ring preserves linear independence | Module transvections and ring-level generalisations; primary research on automorphisms. |
| General web: aliases | shear transformation linear independence elementary column operation | Shear/transvection terminology; Daniel Hsu's 2022 Columbia lecture notes, §1.7 p.9, explain invertible shear operators and subtracting a multiple of a different row. |
| Optional ChatGPT math | unavailable: no ask_chatgpt_math tool exposed | n/a; no fabricated consultation. |
| Local source | clean.tex §2, lines 164–179; full rg receipt retained | Rational-polynomial independence and invertible column operations replacing a basis by one with distinct degrees. |
| nLab | site:ncatlab.org/nlab transvection linear independence module; direct transvection page | Search returned transvections over skewfields and module independence. Direct page failed with unsupported application/xhtml+xml (400); search excerpts usable, failure recorded. |
| nCatLab | site:ncatlab.org transvection elementary matrix; supplementary free-module/independence query | Same site's abstract formulation via injectivity of the free-module map; no separate higher-categorical shear law. |
| Stacks | site:stacks.math.columbia.edu elementary matrix transvection module; direct tags 00DV and 0ASL | Adjacent module/basis machinery, not a new exact shear theorem; Nakayama is not claimed as a hit. |
| MathOverflow | site:mathoverflow.net elementary transvection linear independence module; direct question 59884 | Discussion of generation by transvections over rings; relevant generality, not proof authority for this theorem. |
| Recent arXiv | site:arxiv.org transvection module 2022 2023 2024 2025 2026; retry with quoted transvection/module/2024; direct abs and HTML 2608.10038v1 | Broad query noisy. Rampuria–Amrutha–Chattopadhyay, submitted Aug 10 2026, discusses module transvection automorphism groups; inside five-year window. No new elementary independence formulation required. |

Primary mathematical locators:
[Hsu, Linear transformations and representations](https://www.cs.columbia.edu/~djhsu/CLA/notes/transformations.pdf)
§1.7, p.9;
[Normality of Relative Elementary Tranvection Groups](https://arxiv.org/abs/2608.10038)
abstract, submitted 2026-08-10;
[Stacks, modules over a PID](https://stacks.math.columbia.edu/tag/0ASL)
(adjacent context only).
[nLab transvection](https://ncatlab.org/nlab/show/transvection) and
[nLab module independence](https://ncatlab.org/nlab/show/linearly%2Bindependent%2Bsubset)
supply terminology, with direct-access limitation above.

Literature summary: the concept is invariance of independence under an elementary column shear,
also called transvection or change of generators. Classical presentations use finite-dimensional
vector spaces; module literature treats automorphisms over rings, and independence makes sense
for arbitrary families via finitely supported relations. Invertibility, not division,
polynomial differentiation, or characteristic zero, is the mechanism. A ring/module form is
mathematically coherent and verified below; literature on more elaborate transvection groups is
not being substituted for the elementary law.

## Phase 4a–b — Every parameter and generality

| Parameter/hypothesis | Current | Verified general target / necessity |
|---|---|---|
| K : Type* | universe-polymorphic field carrier | independent universe-polymorphic ring R and module M; no fixed concrete type. |
| Field K | field | Ring R suffices; generic native proof compiles, dropping division, commutativity and domain assumptions together. |
| l : ℕ | finite length | removed in favour of arbitrary index ι; no cardinality or Fintype needed. |
| φ : Fin l → K[X] | polynomials | v : ι → M for AddCommGroup M and Module R M; no polynomial property used after scalar normalisation. |
| ν, ν' | Fin indices | arbitrary i,j : ι; update form needs DecidableEq ι, or classical choice locally. Existing all-coefficient law needs neither DecidableEq nor finiteness. |
| h : ν ≠ ν' | distinct source/destination | essential for arbitrary c; same-index c=1 turns nonzero singleton into zero. Compiled guard. Exceptional c=0 does not justify dropping h uniformly. |
| c : K | any scalar | arbitrary c : R; not restricted to nonzero/unit. Existing law allows an entire coefficient function a with a i=0. |
| hφ | independence | essential: a zero singleton stays dependent; cannot conclude independent without initial independence. Existing law strengthens implication to iff. |
| C c * φ ν | constant polynomial multiplication | c • v i; bridge uses Polynomial.smul_eq_C_mul propositionally. Not asserted definitionally equal. |

**STRICTLY NARROWER THAN STANDARD**, verified via [generic native proof](../evidence/Roth.linearIndependent_update_sub_smul/generic-executed.lean.txt)
and [clean receipt](../evidence/Roth.linearIndependent_update_sub_smul/generic-success.json). CHEAP local bridge, but no new upstream
generalisation needed because the more general law is already in mathlib:

```lean
linearIndependent_add_smul_iff :
  ∀ {ι R M : Type*} [Ring R] [AddCommGroup M] [Module R M]
    {v : ι → M} {a : ι → R} {i : ι},
    a i = 0 →
      (LinearIndependent R (v + fun k ↦ a k • v i) ↔ LinearIndependent R v)
```

This target is an existing declaration, not a helper invented for this assessment.
For the old update use a = update (fun _ ↦ 0) j (-c). At i it is zero by i≠j.
The function equality is checked by extensionality and cases k=j; it is not mere rfl.

## Phase 4c — Nine modern-idiom checks

| # | Question | Answer / consequence |
|---|---|---|
| 1 | Typeclass preambles? | Already typeclasses; expand Field/polynomial specialisation to Ring/module, already supported by existing API. |
| 2 | Filters/nets instead of sequences? | No topology, limits, or metric structure. |
| 3 | Universal property rather than construction? | Independence as injectivity of Finsupp.linearCombination; existing generic law composes with addSingleEquiv. No new construction necessary. |
| 4 | Bundled substructure rather than closure predicate? | Current span proof already uses Submodule; generic law avoids dimension. No ad hoc closure predicate to replace. |
| 5 | Vector-space hierarchy weakening? | Yes: Ring/AddCommGroup/Module. Enables arbitrary modules and noncommutative coefficients, not only K[X]. Verified. |
| 6 | Higher category? | No; ordinary module relation suffices. No concrete downstream higher-category benefit. |
| 7 | Concrete index generalisation? | Yes: Fin l → arbitrary ι, including infinite families; existing law directly handles it. |
| 8 | Concrete-via-abstract diagnostic? | Yes: count polynomial-specific identifiers in proof after smul normalisation = 0; only generic span/dimension remains. Generic proof removes polynomial structure and finite rank entirely. |
| 9 | False-generalisation guard? | No false generalisation in Ring/module target; every old instance specialises and C-multiplication bridge compiled. Reject dropping source/destination distinctness uniformly; guard refutes it. Subtraction prevents naïve Semiring-without-negation signature. |

Modern idiom available: **yes, already in mathlib**. Actual downstream gain: Finsupp linear
combination and addSingleEquiv support arbitrary indices; no finite-dimensional proof or field
division is needed. This is the same elementary independence statement, not a different object
sharing a name. It is independent of the unresolved Wronskian representation design.

## Phase 4.5 — Infrastructure risk

All six rows n/a because the declaration is a theorem: typeclass diamonds, reducibility leaks,
non-canonical unfolding, instance priority collisions, universe-polymorphism construction risks,
and coercion ambiguity. No instance or definition is introduced. Overall risk n/a. The
representation bridge is propositional normalisation, and its proof cost is recorded separately.

## Phase 4.6 — Five proof-strategy checks

| # | Check | Finding |
|---|---|---|
| 1 | ε–δ vs filters | n/a: algebraic theorem. |
| 2 | Elements vs submodule inclusions | Current span equality is already idiomatic point-free algebra; dimension route nevertheless imposes finite-field assumptions unnecessarily. |
| 3 | Sequences vs nets | n/a: no analysis. |
| 4 | Construction vs universal property | Existing injective Finsupp coefficient-change equivalence is the direct mechanism; no bespoke basis construction needed. |
| 5 | Helpers that should exist | No missing mathematical helper needed: linearIndependent_add_smul_iff already exists. A convenient update spelling is optional presentation API, not absent mathematics. |

**REFACTOR-RECOMMENDED**, CHEAP: apply the existing shear iff; use explicit function normalisation
only for the old update spelling. Not claiming this full bridge is syntactically shorter than
the three-tactic dimension proof; it is more general and removes the dimension detour.

## Phase 5 — Five actual methods × three forms

[Raw formal search requests/responses](../evidence/Roth.linearIndependent_update_sub_smul/formal-search.json)
contain 12 calls; [source search receipts](../evidence/Roth.linearIndependent_update_sub_smul/source-search.json) provide the
three source-search forms and full caller/inline audit.

| Method | Current polynomial form | Standard column operation | Abstract Ring/module form |
|---|---|---|---|
| Lean-Finder | positive linearIndependent_add_smul_iff | positive same law, pair lemmas | positive same law |
| Loogle | LinearIndependent _, Function.update, Polynomial.C → empty | LinearIndependent _, Function.update → LinearIndependent.update | LinearIndependent (_ + fun _ => _ • _) → empty |
| LeanSearch | positive same law | positive same law and determinant analogue | positive same law |
| rg pinned source | linearIndependent.*update → update general lemma | span_range_update_sub_smul and finrank criterion | linearIndependent_add_smul_iff and addSingleEquiv positive |
| Local name patterns | linearIndependent_update finds project target | LinearIndependent.update positive | linearIndependent_add_smul_iff positive |

Local index reports **unavailable** on all three calls; file-scan hits establish textual presence
only. External indices may differ from the project pin. Native #check verifies the chosen hit
at the pin. Empty or unavailable searches establish no absence claim.

Pinned primary hit: `Mathlib/LinearAlgebra/LinearIndependent/Defs.lean:751–754`.
Its own proof composes injectivity of the finitely supported linear-combination map with
`Finsupp.linearCombination_comp_addSingleEquiv`. Alternative
`LinearIndependent.update` at `.../Lemmas.lean:544` over CommRing accepts a non-zero-divisor
coefficient witness; it is applicable in principle but unnecessary here. Pair lemmas cover only
two-vector special cases. [Pinned file hashes](../evidence/Roth.linearIndependent_update_sub_smul/mathlib-inputs.json).

Conclusion: **found in mathlib as linearIndependent_add_smul_iff; more general form**.

## Phase 5.5 — Three statement-shape checks

Normal forms: old Function.update/subtract/C-multiply; scalar update; coefficient-function shear;
finite span-finrank equality. The canonical mathematical law is the existing shear iff with
unchanged independence on the RHS; the one-way old update is a convenient downstream spelling.
RHS convention respected by the existing iff.

Syntactic generality attempted: generic scalar update, all-coefficient shear iff, and same-parent
polynomial specialisation. All relevant bridges compile. Use the existing iff directly when
changing the family representation; for current callers the verified update normalisation
preserves their exact types.

Superfluous-argument audit: Field strength, Fin length/finiteness, and polynomial target are
unnecessary mathematically; generic Ring/module proof verifies removal. Initial independence,
source/destination and arbitrary scalar data are real. Distinctness is necessary uniformly.
No CharZero assumption is present to drop; no nonzero c assumption should be introduced.
Universe generality already correct. **RESTATE-BEFORE-SHIP** (but do not ship a duplicate):
reuse the existing canonical API.

## Phase 6.0 — Actual callers and inline audit

Total explicit source uses = **2**, both in the declaring file, external-to-file uses = **0**,
external caller files = **0**. Skill's internal-use count excluding declaring file = **0**.
These counts describe source references, not kernel/simp dependency closure.

| Caller | Exact use | Refactor plan |
|---|---|---|
| Roth.sum_natDegree_update_lt, Roth/Wronskian.lean:190 | (linearIndependent_update_sub_smul h a hφ).ne_zero ν' | Establish independence via existing shear iff with coefficients update 0 ν' (-a), normalise the family, then .ne_zero ν'; retain Function.update evaluation normalisation. |
| Roth.wronskian_ne_zero_of_linearIndependent, Roth/Wronskian.lean:214 | linearIndependent_update_sub_smul hne _ h | Same specialisation with c=(φ ν').leadingCoeff/(φ ν).leadingCoeff supplies independence in induction. Replace the degree-decrease caller too, avoiding a hidden dependence through old helper. |

Complete caller proofs were rebuilt using fresh generic-derived specialisation and fresh
degree-decrease helper: [exact caller execution](../evidence/Roth.linearIndependent_update_sub_smul/callers-executed.lean.txt),
[clean receipt](../evidence/Roth.linearIndependent_update_sub_smul/callers-success.json). The first caller proves the updated
polynomial is nonzero before lowering degree; the second supplies the updated induction hypothesis.
The native checking document contains earlier unrelated replay sections, but these two rebuilt
callers do not use the original target or the original degree helper.

Inline-derivation rg over all production Roth modules found no duplicate derivation of this
independence law; related Wronskian column-invariance is a different predicate.
No outside-project downstream usage was claimed. The theorem has no simp attribute.

## Phase 6 — Actual composition experiments

1. Original proof replay: succeeds by the finite-span/finrank criterion. It uses the independence
criterion twice, Set.finrank unfolding, scalar-polynomial bridge and span-update law; this is
more than three named normalisation/call steps. Not sold as strict ≤3-call composition.
2. Existing generic law: its canonical statement is one mathematical theorem call,
`(linearIndependent_add_smul_iff hc).2 hv`. Generic update bridge succeeds but includes
coefficient condition proof, conversion, function extensionality and index case split.
3. Same-parent polynomial specialisation succeeds with `simpa only [smul_eq_C_mul]`;
this uses a newly proved bridge, **not** an existing mathlib replacement by itself.
4. Exact original-goal `exact?` experiment exhausted the default 200000 heartbeats at whnf.
This is an honestly rejected search attempt, not evidence of absence, not a wall-clock timeout,
and not accepted proof evidence. No limits were raised.
[Rejected source](../evidence/Roth.linearIndependent_update_sub_smul/composition-executed.lean.txt),
[raw rejected receipt](../evidence/Roth.linearIndependent_update_sub_smul/composition-rejected.json).
5. Native same-index guard: singleton ℚ-family 1 is independent, update at the same index by
subtracting itself is dependent. [Guard source](../evidence/Roth.linearIndependent_update_sub_smul/guards-executed.lean.txt),
[clean receipt](../evidence/Roth.linearIndependent_update_sub_smul/guards-success.json). Initial unused simp argument warning was
corrected and its [rejected receipt](../evidence/Roth.linearIndependent_update_sub_smul/guards-warnings-rejected.json) retained separately.

Strict old-spelling conclusion: **NOT-COMPOSABLE by tested ≤3-call routes**; no proof-minimality
claim. Canonical form: a direct existing more-general-law hit. In particular, neither a
simp-closing wrapper nor a new generic helper is being counted as a three-call mathlib term.

## Phase 7 — Verdict and gate

**NO-mathlib-has-it**, because the existing Ring/module coefficient-function shear law is the
mathematical result at strictly greater generality. This is a direct positive result, unrelated
to parent re-aim inheritance. Normalising old Function.update syntax does not create new
mathematics. The existing core inference follows in one line:

```lean
-- hc : a i = 0; hv : LinearIndependent R v
exact (linearIndependent_add_smul_iff hc).2 hv
```

The exact old-form bridge is the accepted generic source, not falsely claimed to be definitionally
equal or a one-call term. Both explicit callers have concrete, native-checked refactor plans
above. Delete the public specialised wrapper when performing that refactor; keep local
normalisation at the two sites, or use a private bridge in `Roth/Wronskian.lean` if retaining
current family syntax improves readability. This is the appropriate alternative local
destination, rather than a new mathlib polynomial theorem or Archive entry.

No new upstream file/PR/reviewer recommendation is applicable to this NO verdict. Already accepted
YES declarations were read in progress.json; none changes the direct existing hit or needs grouping
with this redundant theorem. Missing API: no mathematical gap. Optional generic update convenience
spelling is an upstream API taste question independent of the current duplicate; not a reason to
override the verified existing-law verdict. Cost is not used to decide the category.

Gate: full literature and 5×3 search completed; all parameters/9 modern idioms/5 strategies/
6 justified theorem-risk n/a/3 statement shapes checked; all two explicit callers rebuilt; exact
type and standard axioms checked; strict callcount and failed automation stated honestly.
Verification unresolved = []. Root acceptance remains pending.

## Phase 8 — Consolidated report and next action

This document is the explicit complete Phase-8 report, containing Phases 0–7 in order and the
bucket-specific next action: **delete the polynomial-specific public wrapper during the caller
refactor and reuse linearIndependent_add_smul_iff, with the verified representation bridge at
both callers**. This assessment changes no production Lean, Git state, pins, or overview records.
[Machine assessment](../evidence/Roth.linearIndependent_update_sub_smul/assessment.json),
[verification manifest](../evidence/Roth.linearIndependent_update_sub_smul/verification.json),
[portable validator](../evidence/Roth.linearIndependent_update_sub_smul/validate.py).

