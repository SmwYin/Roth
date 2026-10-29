# Roth.exists_nat_mul_isIntegral — canonical268

**Verdict: NO-mathlib-has-it.** The substantive positive natural multiplier result already exists as `IsAlgebraic.exists_nsmul_eq`, with a witness in an arbitrary integral closure of ℤ. Specializing that closure to `integralClosure ℤ ℝ`, extracting its subtype property, and converting natural scalar multiplication to multiplication gives exactly this theorem. The pinned canonical denominator API supplies another direct witness. This conclusion was checked independently; it is not inherited from generic integral-multiple infrastructure or another assessment. Assessment complete; root acceptance pending. Production, pins, Git, overview and progress unchanged.

## Phase0 — baseline and source

`Roth/Main.lean:62–66`, public theorem, four proof lines, no `sorry`. Read the full declaring module and the complete actual caller `Roth.reduction`, including the surrounding reduction and final Roth proof. The module proves Roth's theorem by reducing to integral algebraic numbers and deriving a contradiction using its main lemma. The shared build completed successfully,2467jobs, exit0. All17source/pin hashes freshly match the tracked manifest, including the current final check. The accepted Theta228 file-end build remains reusable; no new file-end build is due until289.

Evidence: [fresh inputs](../evidence/Roth.exists_nat_mul_isIntegral/inputs.json), [baseline](../evidence/Roth.exists_nat_mul_isIntegral/baseline-build.txt), [source](../evidence/Roth.exists_nat_mul_isIntegral/source-Main.lean.txt), [metadata](../evidence/Roth.exists_nat_mul_isIntegral/target-metadata.json), [instructions](../evidence/Roth.exists_nat_mul_isIntegral/instructions-read.json).

## Phase1 — meaning, full type, and proof

A real algebraic number α has a positive natural number M such that Mα satisfies a monic polynomial over ℤ. There is no irrationality or nonzeroness assumption on α:0and every rational number are included. Positivity ensures a useful nonzero scaling in the subsequent irrationality and approximation argument.

Fresh kernel type, read with `Lean.getConstInfo` and `pp.funBinderTypes`:

```lean
∀ {α : ℝ}, IsAlgebraic ℚ α → ∃ (M : ℕ), 0 < M ∧ IsIntegral ℤ (↑M * α)
```

`IsFractionRing.isAlgebraic_iff ℤ ℚ ℝ` first changes the coefficient ring of an annihilating polynomial. `IsAlgebraic.exists_integral_multiple` then applies integral normalization to obtain an integer y≠0 with yα integral. These are distinct operations: merely clearing coefficients does not make the polynomial monic or its root integral. Taking `y.natAbs` gives a positive natural witness. Integer multiplication by `y.sign` preserves integrality and converts yα into |y|α.

The exact complete Main module was replayed in a fresh namespace, changing only this target's spelling outside the canonical array. Original and replay have the same type and standard axioms. The original `pp.all` body print elided42592characters; **this is not a complete kernel body dump**. The complete written source/body, fresh full type, standard axioms, complete293kernel-value audit, and corrected opaque body-constant extraction remain available. An initial `ci.value?` without `allowOpaque` returned `none`; the later opaque query and compact audit correct that, rather than interpreting it as an empty proof.

Source/body/type scopes: no other canonical project declaration occurs in the target's type or proof. Its compiled proof refers to two generated helpers named `Roth.exists_nat_mul_isIntegral._simp_1_1` and `_simp_1_2`. These are explicitly recorded; they are not additional public declarations or cross-declaration mathematical dependencies. The target has no source `[simp]` attribute. Full dependency closure rooted at those generated helpers returns only those two Roth-prefixed helpers; imported mathlib cannot depend back on Roth.

Evidence: [original exact execution](../evidence/Roth.exists_nat_mul_isIntegral/original-executed.lean.txt), [original raw receipt](../evidence/Roth.exists_nat_mul_isIntegral/original-receipt.json), [native type disclosure](../evidence/Roth.exists_nat_mul_isIntegral/native-type.json), [compact kernel scopes](../evidence/Roth.exists_nat_mul_isIntegral/scope-receipt.json), [dependencies](../evidence/Roth.exists_nat_mul_isIntegral/dependencies.json).

## Phase2 — preliminary classification

SMALL: an algebraic reduction helper, not a named main theorem or new structure. Exhaustive search still applies. The one-line **definition** check and its three exemptions are n/a: this is a theorem. Its four proof lines do not by themselves determine upstream value.

## Phase3 — exhaustive literature

All named channels were attempted. The following requests are exact in the linked metadata; responses are represented by SHA256, byte count, status and clean locators, with original concise summaries. Full web articles and search bodies are not archived. The general response uses documented ASCII-escaped JSON serialization for its hash because the returned text contains UTF16 surrogate pairs; the other metadata hashes use the returned UTF8 string.

| Channel | Actual query / local lookup | Outcome |
|---|---|---|
| General specific | `algebraic number positive integer multiple algebraic integer leading coefficient` | Standard positive integer multiple formulation; computational algebra documentation confirms denominator witness. |
| General abstract | `commutative ring algebraic element fraction field nonzero multiple integral integral closure` | Integral closure and field-of-fractions formulation; no real-order restriction. |
| General alias | `denominator ideal algebraic number natural denominator algebraic integer` | Denominator ideal and positive generator terminology. |
| Optional ChatGPT math | Standard form/generality/history channel | n/a: `ask_chatgpt_math` unavailable. No substitute invented. |
| Local paper | `clean.tex`, lines1154–1165, surrounding reduction1148–1189 | Exact positive M lemma; polynomial leading-coefficient normalization. |
| nLab | `site:ncatlab.org/nlab algebraic integer integral closure` | Integral closure and algebraic integer definitions, arbitrary base-ring context. Direct page fetch later failed400unsupported XHTML; search result evidence retained. |
| nCatLab, distinct namespace | `site:ncatlab.org/ncatlab algebraic element integral closure denominator` | Returned /nlab material; no in-namespace exact hit. Not a categorical reformulation claim. |
| Stacks | `site:stacks.math.columbia.edu algebraic field extension multiple integral clearing denominators`, plus refinements | Broad finite/integral extension results and off-target ramification material; no exact positiveNat hit. Two additional refinements returned empty. |
| MathOverflow | `site:mathoverflow.net algebraic number denominator positive integer integral`, then `site:mathoverflow.net "denominator" "algebraic number"` | Denominator as positive generator; powers and height applications. |
| Recent arXiv | `site:arxiv.org algebraic number denominators integral after:2021-10-29 before:2026-10-30` | Singhal–Lin, *Primes in denominators of algebraic numbers*, submitted24Nov2022/revised15Dec2022; direct abstract opened. |
| Supplementary formal API web | `mathlib4 Algebra natDenominator isIntegral_natDenominator_smul` | Current official docs expose normalized denominator API; pinned native/source verification is separate. |

An exact arXiv path supplied as a **search** query returned unrelated results; a subsequent direct open of the actual returned abs URL supplied reliable metadata. Off-target results are not treated as supporting the theorem.

The literature agrees on positive integer denominators for algebraic numbers and scalar denominators over general domains. The stronger canonical view is the positive generator of the denominator ideal; the mere existence statement does not need a number field or finite extension. The recent arXiv paper studies denominator ideals and prime supports, not a replacement definition of integrality. The real-valued target is a valid specialization, with mathematical content extending beyond ℝ.

Primary locators: [Wolfram denominator documentation](https://reference.wolfram.com/language/ref/AlgebraicNumberDenominator.html), [KANT EltDen](https://page.math.tu-berlin.de/~kant/doc/html/html/html/EltDen.html), [nLab integral closure](https://ncatlab.org/nlab/show/integral%2Bclosure), [recent arXiv abstract](https://arxiv.org/abs/2211.13822). Own summaries only; no quotations required.

Evidence: [general](../evidence/Roth.exists_nat_mul_isIntegral/web-general.json), [named channels](../evidence/Roth.exists_nat_mul_isIntegral/web-channels.json), [recent/API](../evidence/Roth.exists_nat_mul_isIntegral/web-recent.json), [primary access limitations](../evidence/Roth.exists_nat_mul_isIntegral/web-primary.json), [corrective direct open](../evidence/Roth.exists_nat_mul_isIntegral/web-supplement.json), [local excerpt](../evidence/Roth.exists_nat_mul_isIntegral/local-excerpt.tex.txt), [optional channel](../evidence/Roth.exists_nat_mul_isIntegral/optional-math-opinion.json).

## Phases4a–4b — generality, with actual proofs

| Parameter/hypothesis | Current | Verified general form / limit |
|---|---|---|
| Ambient α | ℝ | Any `Ring A` for algebraicity over ℤ; no order, topology, completeness, field or domain assumption on A. The manual sign proof compiled. |
| Algebraicity | `IsAlgebraic ℚ α` | `IsAlgebraic ℤ x` in the abstract ring version. For a rational algebra, equivalence to existence of a positiveNat integral multiple compiled; hypothesis cannot simply be dropped. |
| Rational base | ℚ | Any fraction field K of any commutative domain R, compatible commutative K-algebra A, yields a nonzero **R** scalar. No GCD, UFD or principal-ideal assumption required. |
| Integral base | ℤ | Arbitrary commutative R supports the existing nonzero-R-multiple theorem even for `Ring A`. This changes the scalar witness from Nat to R and is not the same positiveNat assertion. |
| Witness | M:ℕ,0<M | Natural nonzero and positive are equivalent. Existing `exists_nsmul_eq` already has nonzeroNat; natural scalar multiplication and cast-times are propositionally transported by `nsmul_eq_mul`, not asserted defeq. |
| α nonzero / irrational | Absent | Correctly absent: zero and arbitrary rational endpoints compiled. |
| Positivity weakened to0≤M | Not adopted | Allows M=0for every x, destroying the meaningful nonzero scaling; compiled vacuity guard. |
| Universes / structure constraints | Concrete | Generic `Type u`, `Type v`, `Type w` compiled. `Ring A` is required to use this integrality/algebra API; no semiring claim. |

Verified strongest positive-natural proposal (a **new scratch generic proof**, not claimed as an existing named theorem):

```lean
theorem nat_noncomm {A : Type u} [Ring A] {x : A} (h : IsAlgebraic ℤ x) :
    ∃ M : ℕ, 0 < M ∧ IsIntegral ℤ ((M : A) * x) := by
  obtain ⟨y, hy, hint⟩ := h.exists_integral_multiple
  refine ⟨y.natAbs, Int.natAbs_pos.2 hy, ?_⟩
  simpa [zsmul_eq_mul, ← mul_assoc, ← Int.cast_mul, Int.sign_mul_self] using hint.zsmul y.sign
```

Its **actual compiled original specialization** is:

```lean
nat_noncomm ((IsFractionRing.isAlgebraic_iff ℤ ℚ ℝ).2 hα)
```

The commutative rational-algebra version and its converse also compiled. Separately, the already existing broader base-ring result was specialized with the exact compiled signature:

```lean
{R : Type u} {K : Type v} {A : Type w} [CommRing R] [IsDomain R]
[Field K] [CommRing A] [Algebra R K] [IsFractionRing R K]
[Algebra R A] [Algebra K A] [IsScalarTower R K A] {x : A}
(h : IsAlgebraic K x) : ∃ r : R, r ≠ 0 ∧ IsIntegral R (r • x)
```

The current statement is STRICTLY NARROWER than verified standard ambient generality. The negative upstream verdict comes from existing stronger commutative integral-closure/denominator APIs, not a claim that the newly proved noncommutative scratch helper already exists. The Denominator module requires `CommRing A`; it does **not** itself supply `nat_noncomm`.

Evidence: [isolated exact proofs and signatures](../evidence/Roth.exists_nat_mul_isIntegral/isolated-executed.lean.txt), [full clean raw receipt](../evidence/Roth.exists_nat_mul_isIntegral/isolated-receipt.json), [necessary-hypothesis counterexample](../evidence/Roth.exists_nat_mul_isIntegral/supplement-executed.lean.txt), [supplement receipt](../evidence/Roth.exists_nat_mul_isIntegral/supplement-receipt.json).

## Phase4c — modern idiom, nine required rows

| # | Question | Finding and downstream consequence |
|---|---|---|
|1| Typeclasses instead of bundled hypotheses | Ambient ring/algebra structures generalized; pointwise `IsAlgebraic` stays a premise. An entire algebra need not be algebraic. |
|2| Filters/topology | No: finite polynomial algebra, no limit or metric premise. |
|3| Universal property | Yes: `IsFractionRing` handles fraction fields; `IsIntegralClosure` handles any integral-closure model through existing `exists_nsmul_eq`. Enables alternate number-field models. |
|4| Bundled substructure | Yes: witness s in `integralClosure ℤ A`, then `s.property`; reuses Subalgebra/algebraMap API instead of repeating sign work. |
|5| Algebraic hierarchy | Yes: generic `Ring A` sign proof; `CommRing A` canonical-denominator route; no field/order needed on A. |
|6| Higher categories | No: no relevant categorical statement or additional usable API. |
|7| Concrete indices/scalars | Nat is intentional nonzero integer scaling. Arbitrary base R supports nonzero R scalar, not arbitrary positiveNat. |
|8| Concrete-via-abstract | Yes: only the first existence line names ℝ/ℚ; subsequent proof is integer arithmetic and integrality preservation. Actual generic proof and exact specialization verified, rather than relying on identifier counting alone. |
|9| False-generalization guard | No accepted false generalization. Nat→R witness change is explicitly different; natural positivity remains tied to ℤ. Arbitrary R=ℚ[t], x=1/t illustrates why a natural multiplier need not clear an R-denominator. Dropping algebraicity fails for X:ℤ[X], formally proved; zero scalar is vacuous. |

Modern idiom available, already implemented by existing mathlib APIs: use the integral-closure existence law or canonical denominator and divisibility characterization. This composes with integral-closure maps and denominator divisibility/minimality. It is a concrete organizational improvement, not a new modernized theorem to upstream. Identifier diagnostics are [archived](../evidence/Roth.exists_nat_mul_isIntegral/concrete-diagnostic.json).

## Phase4.5 — infrastructure risk

All six rows are justified n/a for a theorem: typeclass diamond; reducibility leak; noncanonical unfolding; instance-priority collision; universe-polymorphism issues; coercion ambiguity. No definition, class or instance is introduced, and no existing instance path is modified. The generic scratch proofs are propositions only.

## Phase4.6 — proof strategy

| # | Required question | Result |
|---|---|---|
|1| ε–δ versus filters | n/a: no topology. |
|2| Elements versus substructures | Existing integral-closure witness avoids manual sign normalization. Full caller version compiled. |
|3| Sequences versus nets | n/a: no analysis. |
|4| Construction versus universal property | Existing `IsFractionRing` and `IsIntegralClosure` are the correct abstractions. |
|5| Helpers mathlib should have | None needed for this real result: exact nonzeroNat closure law and canonical denominator exist. Scratch noncommutative positiveNat wrapper is a separate potential convenience, not an established missing mathematical theorem. |

REFACTOR-RECOMMENDED for reuse: use the already available integral-closure or denominator route. The original strategy is sound and idiomatic as a local proof; no new polynomial-root normalization should be developed here. Cost does not determine the verdict.

## Phase5 — all15formal search cells

| Form | LeanFinder | Loogle | LeanSearch | rg | Local name index |
|---|---|---|---|---|---|
| Current positiveNat real | Integral multiple API | `IsIntegral, "nat"` exposed canonical Denominator API | Integral multiple and integral/nsmul APIs | `exists_nsmul_eq` | Target found in project; warming index |
| Standard natural integral-closure witness | Integral multiple/closure infrastructure | `IsAlgebraic, "exists"` found `exists_nsmul_eq` | Integral multiples | Closure/existence source hits | `IsAlgebraic.exists_nsmul_eq`; warming |
| Abstract base-ring scalar | `exists_integral_multiple`, iff | `IsAlgebraic, IsIntegral` | Same generic API | Generic theorem + fraction-field bridge | Generic theorem found; warming |

All exact requests and raw responses are in the [15-cell matrix](../evidence/Roth.exists_nat_mul_isIntegral/formal-search-matrix.json) and named `search-<form>-<method>.json` receipts. Local indexes were **warming**, not absence evidence. External indexes may differ from the pin; every positive candidate used in the conclusion was read in pinned source and kernel-checked. The [untruncated full-name rg](../evidence/Roth.exists_nat_mul_isIntegral/full-name-search.json) has no exact project-name duplicate in mathlib; the conclusion instead relies on a semantically stronger named result. No absence claim rests on rg or warming results. This is a positive API hit, so a broad `exact?` timeout is unnecessary.

Existing pinned locations:

- `Mathlib/RingTheory/Algebraic/Integral.lean:146`: `IsAlgebraic.exists_integral_multiple`, arbitrary commutative base/Ring algebra.
- Same file207–214: `IsAlgebraic.exists_nsmul_eq`, already **natural**, nonzero multiplier and integral-closure witness.
- `Mathlib/RingTheory/Localization/Integral.lean:106`: `IsFractionRing.isAlgebraic_iff`, coefficient-base transfer.
- `Mathlib/RingTheory/Algebraic/Denominator.lean`: `Algebra.natDenominator`, `Algebra.natDenominator_dvd_iff`, `Algebra.isIntegral_natDenominator_smul`, `IsAlgebraic.natDenominator_ne_zero`.

Full pinned source archives and hashes are indexed in [mathlib-inputs](../evidence/Roth.exists_nat_mul_isIntegral/mathlib-inputs.json). Isolated proofs use exact stable18 plus the root-authorized Denominator import19; shared18 and disk9 are unchanged. The guarded target is absent in the isolated environment.

## Phase5.5 — all three statement-shape checks

**Normal form:** `n • x` versus `(n:A)*x`, and `n≠0` versus `0<n`, are equivalent via named lemmas, not defeq claims. Existing integral-closure witness is the stronger reusable form; canonical denominator divisibility characterizes all acceptable n. The target is an existence statement, so RHS-of-iff convention is n/a; the compiled `nat_iff` and existing denominator divisibility iff give canonical comparison forms.

**Syntactic generality:** tested positiveNat nsmul, cast-times, nonzeroNat closure witness, rational-algebra iff, generic R scalar, and exact real recovery. At this particular reduction callsite positiveNat/cast-times is convenient, while existing `exists_nsmul_eq` has the stronger reusable API. No packaging is assumed to preserve proof terms by definitional equality.

**Superfluous arguments:** α is the object; algebraicity is essential (formal converse and X counterexample). There is no irrationality, α≠0, finite dimensionality, topology or hidden extra proposition to drop. ℝ's ambient structure can be weakened as proved above. Overall: RESTATE-BEFORE-SHIP if proposing a new generic convenience lemma, but the real form is already covered by existing API and should not ship anew.

## Phase6.0 — complete callers, inline audit, canonical kernel audit

| Caller | Actual use | Completed experiment |
|---|---|---|
| `Roth.reduction`, Main118–134, use121 | Obtains M,hM0,hMint; hM0 preserves irrationality and allows positive scaling of approximation inequalities | Complete original proof retained; only first obtain replaced. Both manual sign and existing integralClosure routes compiled with exactly the original signature. |

Total explicit source caller declarations1; occurrence1; external-to-declaring-file callers0. Following the command's exclusion convention, internal uses **outside** the declaring file0; this does not hide the same-file caller. Fresh `rg --no-ignore` and tracked `git grep` agree. Source references, kernel direct values, types, transitive dependencies, and simp scopes are distinguished. Exact tracked array order293, unique293, present293, values293; canonical direct value consumer is only `Roth.reduction`, direct type consumers0. No other inline rederivation was found. `Roth.exists_nat_smul_eq_map` clears coefficients of a rational multivariate polynomial; that does not prove integral normalization of its root and is not this theorem's duplicate.

The compact accepted scope audit asserts both caller proofs contain neither the target nor either generated target helper. The remaining original project references are exactly `Roth.approxSet`, `Roth.eventually_div_rpow_lt`, `Roth.approxSet_den_le_finite`. No claim that these full caller proofs are mathlib-only: their scalar-multiple replacement is mathlib-only, and the project remainder is intentionally preserved.

Evidence: [complete caller](../evidence/Roth.exists_nat_mul_isIntegral/caller-Roth.reduction.lean.txt), [callers](../evidence/Roth.exists_nat_mul_isIntegral/callers.json), [fresh source search](../evidence/Roth.exists_nat_mul_isIntegral/source-search.json), [tracked search](../evidence/Roth.exists_nat_mul_isIntegral/tracked-source-search.json), [inline exact source](../evidence/Roth.exists_nat_mul_isIntegral/inline-executed.lean.txt), [inline receipt](../evidence/Roth.exists_nat_mul_isIntegral/inline-receipt.json), [compact exact assertions](../evidence/Roth.exists_nat_mul_isIntegral/scope-executed.lean.txt), [compact receipt](../evidence/Roth.exists_nat_mul_isIntegral/scope-receipt.json), [canonical consumers](../evidence/Roth.exists_nat_mul_isIntegral/canonical-consumers.json).

## Phase6 — composition with honest accounting

The old sign route is a genuine short proof: fraction-field transfer, integral-multiple existence, positivity from natAbs, integrality under zsmul, and arithmetic normalization. It is not a ≤3-call term merely because it occupies four lines, and a closing `simpa` chain alone would trigger Phase6b's borderline heuristic.

The canonical-denominator replacement is a **single constructor term using existing API**, without a newly proved helper or automation:

```lean
⟨Algebra.natDenominator α,
  Nat.pos_of_ne_zero ((IsFractionRing.isAlgebraic_iff ℤ ℚ ℝ).2 hα).natDenominator_ne_zero,
  (nsmul_eq_mul _ α) ▸ Algebra.isIntegral_natDenominator_smul α⟩
```

This has three substantive algebra API applications **plus** `Nat.pos_of_ne_zero` and `nsmul_eq_mul`: five explicit theorem applications and one witness definition (excluding logical constructors/projections). It is not claimed ≤3under all-call counting; strict composition result NOT-COMPOSABLE. The upstream **NO-mathlib-has-it** result instead uses the stronger existing **existence theorem** `exists_nsmul_eq`, whose witness is already a nonzero natural multiple in an integral closure, together with actually verified representation transport. The extra arithmetic spelling is not missing mathematical content. `nat_noncomm`, the converse, and the unconditional-X guard are newly written scratch proofs; they are not counted as existing library building blocks.

Evidence: [composition accounting](../evidence/Roth.exists_nat_mul_isIntegral/composition.json), [isolated direct term and closure proof](../evidence/Roth.exists_nat_mul_isIntegral/isolated-executed.lean.txt).

## Phase7 — actionable verdict

**NO-mathlib-has-it.** Existing `IsAlgebraic.exists_nsmul_eq` provides a more general natural-scalar existence statement; normalized denominator API even selects a canonical witness and characterizes all integral scalar multiples. The exact real recovery was compiled through both APIs. This is independent positive evidence, not an absence inference, inherited judgment, or cost-based rejection. Generic integral-multiple existence alone would not have justified ignoring the positiveNat refinement.

On a future authorized cleanup, delete the real wrapper and replace the sole initial obtain in `Roth.reduction` with the following **already compiled full-caller block**, retaining all subsequent original lines:

```lean
  obtain ⟨M, s, hM, hs⟩ :=
    ((IsFractionRing.isAlgebraic_iff ℤ ℚ ℝ).2 halg).exists_nsmul_eq (integralClosure ℤ ℝ)
  have hM0 : 0 < M := Nat.pos_of_ne_zero hM
  have hMint : IsIntegral ℤ ((M : ℝ) * α) := by
    have hi : IsIntegral ℤ (M • α) := by
      rw [hs]
      exact s.property
    simpa only [nsmul_eq_mul] using hi
```

This route needs no additional production import. Alternatively, explicitly import `Mathlib.RingTheory.Algebraic.Denominator` and use the direct canonical term above, introducing M,hM0,hMint by `let`/`have`. The direct old theorem was checked mathlib-only, but no claim is made that this extra module was already imported by the persistent disk9caller environment. If retaining the source-paper correspondence is desirable, `Roth/Main.lean` remains an appropriate local pedagogical destination; there is no reason to move a real-only wrapper into Archive. No production refactor was performed in this assessment.

No future upstream questions are required for this NO verdict. The novel noncommutative scratch convenience statement can be considered separately on its own merits, without relabeling the real specialization as new.

## Phase8 — verification, limitations, and handoff

All accepted native sources finish successfully, nonpartial where the disk format exposes that field, no errors/warnings, no recovered `sorryAx`, only `propext`, `Classical.choice`, `Quot.sound`. Isolated `run_code` format has diagnostics/success/timed_out and does not supply a partial field. Standard limits retained; no sorry, new axiom, unsafe, native_decide or resource raise. Six accepted source/receipt pairs include the first clean isolated source and the strengthened final isolated source with an explicit RingA→real specialization. Ten actual native executions, nine distinct sources, four rejected executions of three sources. The second rejected source's **initial** receipt failed to save because of UTF8 stdin encoding; its exact source was then separately replayed, with the replay's own full raw receipt clearly labeled. The replay is not a recovered original response. Nine actual raw responses are archived; that one unaccepted initial raw response remains only in conversation. This limitation affects no accepted proof evidence.

Rejected sources/receipts are retained: two isolated elaboration failures (closure coercion and one nonexistent suggested name, then subtype-versus-mapped integrality), and an inline audit metaprogram precedence error. They are not accepted evidence. Printer elision is disclosed above; compact programmatic assertions supply unelided dependency conclusions. Every exact executed source is archived as `.lean.txt`; no evidence `.lean` modules are introduced.

[Verification ledger](../evidence/Roth.exists_nat_mul_isIntegral/verification.json), [capture limitation](../evidence/Roth.exists_nat_mul_isIntegral/receipt-capture-failure.json), [preparation checks](../evidence/Roth.exists_nat_mul_isIntegral/preparation-checks.json), [portable validator](../evidence/Roth.exists_nat_mul_isIntegral/validate.py), [final checks](../evidence/Roth.exists_nat_mul_isIntegral/final-validation.json), [freeze/release](../evidence/Roth.exists_nat_mul_isIntegral/freeze-record.json). The portable validator checks the **current** manifest, source/pin hashes, canonical293exact order and private modules, native requests/results and axioms, caller preservation, all15formal cells, literature metadata and report links in scratch and simulated integrated layouts. Root independently accepts and publishes.
