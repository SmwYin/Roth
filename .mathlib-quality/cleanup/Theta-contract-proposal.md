# Theta contract candidates and approved scope

## Continuing cleanup authorization

The user's later instruction is: “From now on implement all changes that you recommend.
Only ask me if you can't decide.” This supersedes automatic per-change approval requests for
new well-supported recommendations. Concrete compiler/original-contract/axiom evidence and all
sequential checkpoint gates still apply. Earlier explicit preservation choices remain preferences:
do not automatically reopen declined hq/D/E/F additions, retained wrappers or optional domains,
or introduce unnecessary broad API churn. The current selected revisits proceed unchanged.

## Explicit user decision (2026-10-18)

The user approved exactly A and B below, plus the first five C rows:

- Remove all 15 DecidableEq binders from the 14 listed public theorems.
- Remove Fintype only from one_mem_RSet.
- Remove hr from indexSet_bddAbove and Θ_le_card.
- Remove hR from exists_eq_pow_mul_of_rootMultiplicity and sum_max_sub_le_index_det.
- Remove hl′, hδ and the consequently unused implicit δ from index_det_le.

The user chose preservation for the remaining options: RETAIN hq in index_le_lem6 and
Θ_option_le; RETAIN Θ_nonneg's hB/hr, Θ_le_card's hB, and Θ_mono's hB/hr. Thus D/E/F's
additional bound/weight widening is declined; their overlapping A instance removals and
Θ_le_card's overlapping C.hr removal remain approved. This selected scope does not itself
authorize another hypothesis, definition,
domain, conclusion, binder order, naming or project structure change; the later standing
authorization above governs any new well-supported recommendation.

Application proceeds through dedicated sequential declaration checkpoints/revisits. Original 15
Θ_equiv applies its approved A row in the first publication below; earlier completed targets
then receive fresh revisits in source/dependency order, without inflating original counts.
Future approved targets apply their rows in their dedicated original audits. This decision is
more restricted than the historical whole-candidate compiler probe, which also explored hq
removals. No unselected row may be inferred from that probe's successful compile.

### Published application ledger

- Original 15, Θ_equiv: both approved A.DecEq instance removals applied, independently original
  ten-binder recovered through an explicit adapter to the actual eight-binder theorem. Module,
  complete LSP, actual axioms, caller, final profile and owner full/separate LeanEval gates pass.
- Approved revisit 6, one_mem_RSet: Only the approved Fintype σ and DecidableEq σ removals. Independent original adapter,
  actual axioms/metadata/caller, complete LSP, profile and frozen full/LeanEval gates pass.
- Approved revisit 7, indexSet_nonempty: Only the approved DecidableEq σ removal. Independent original adapter,
  actual axioms/metadata/caller, complete LSP, profile and frozen full/LeanEval gates pass.
- Approved revisit 8, indexSet_bddAbove: Only the approved DecidableEq σ and hr removals, with two required helper-call argument deletions. Independent original adapter,
  actual axioms/metadata/caller, complete LSP, profile and frozen full/LeanEval gates pass.
- Approved revisit 9, index_le_Θ: Only the approved DecidableEq σ removal; hr remains public. Independent original adapter,
  actual axioms/metadata/caller, complete LSP, profile and frozen full/LeanEval gates pass.
- Approved revisit 10, Θ_nonneg: Only the approved DecidableEq σ removal; hB, hr and Fintype remain.
  Independent original adapter, actual axioms/metadata/caller, complete LSP, profile and frozen
  full/LeanEval gates pass.
- Approved revisit 11, Θ_le_card: Removed only the approved DecidableEq σ and hr; retained hB and Fintype σ.
  Independent original adapter, actual axioms/metadata/caller, complete LSP, profile and frozen
  full/LeanEval gates pass.
- Approved revisit 12, Θ_le_of_forall_index_le: Removed only the approved DecidableEq σ; retained every other parameter and hypothesis.
  Independent original adapter, actual axioms/metadata/caller, complete LSP, profile and frozen
  full/LeanEval gates pass.
- Approved revisit 13, Θ_mono: Removed only the approved DecidableEq σ; retained hB/hr, Fintype σ and every other argument.
  Independent original adapter, actual axioms/metadata/caller, complete LSP, profile and frozen
  full/LeanEval gates pass.
- Original 18, exists_eq_pow_mul_of_rootMultiplicity: approved C.hR removal applied; sole caller obsolete argument removed while its own hR/full original contract remain.
  Immutable original proof and full-old adapter, exact retained metadata/selected-drop AST, actual
  standard axioms, complete LSP, target/caller profiles and frozen full/LeanEval gates pass.
- Original 19, pow_rootMultiplicity_le: recommended hB localization to the absolute leading coefficient implemented under the user’s standing authorization after concrete compiled candidate/old-adapter/caller evidence.
  Exact new premise and all other retained domains/metadata, independent originals, actual standard
  axioms, complete LSP, repeated target/caller profiles and frozen full/LeanEval gates pass.
- Original20, Θ_unique_le: approved A.DecidableEq σ removed; every other public parameter including hB/hr/Fintype retained.
  Headline29→3; ONE new private index/log helper has a separate fresh full audit, body23,
  initial-contract adapter and final original-public adapter/actual axioms/LSP/profiles/full/LeanEval.
- Original26, min_le_sum_max: recommended unconditional bound implemented under standing authority; removed exactly hrp/hθ, preserving domain/conclusion and the entire original sole caller contract. Three new private helpers each received a separate fresh audit; exact original adapters/actual standard axioms, full LSP, all-four real prefix profiles and frozen full/separate LeanEval gates pass. See section H.
- Original27, sum_max_sub_le_index_det: approved A.DecidableEqτ and C.hR removals applied, all other arguments including hD/hδ retained. Sole caller obsolete argument/local proof removed; its entire original contract remains. Independent full original target and caller proofs/telescope/value/BinderInfo/standard axioms, full LSP0errors14warnings, real profile746.452ms and frozen full110.300s then separate LeanEval32.749s pass. No new helper or extra API change; generic finite-family/column-bound alternatives assessed and not recommended.
- Original28, index_det_le: approved A/C removals and supported redundant hB removal implemented under standing authorization, exact old drop set DecidableEqτ/δ/hB/hl′/hδ. Entire sole caller contract retained. Both new helpers freshly audited; coefficient wrapper deleted via existing constant-degree specialization, separated helper26 retained. Exact old target+entire caller/value/BinderInfo/actual standard axioms, full LSP0/11, real helper655.221ms/public742.222ms, frozen full91.138s then separate LeanEval30.612s pass. See section I.
- Supported revisit 29, index_le_lem6 arithmetic boundary: K weakens hδ0/hδ1 to nonstrict bounds and hrp to3≤(rnone:ℝ); removes only index_le_lem6.hr0/hB. Domains, exact conclusion, hq and protected globalΘ hB/hr hypotheses remain..
  Independent original adapter, actual axioms/metadata/caller, complete LSP, profile and frozen
  full/LeanEval gates pass.
- Performance revisit 26, mul_sq_div_three_le_sum_max_of_pos_aux: Only the assigned private proof changes; exact FIRST six-binder contract and all source outside it remain byte-identical.
  Independent original adapter, actual axioms/metadata/caller, complete LSP, profile and frozen
  full/LeanEval gates pass.
- Performance revisit 29, index_le_lem6: Only the assigned public proof changes; exact signature and all surrounding source remain byte-identical.
  Independent original adapter, actual axioms/metadata/caller, complete LSP, profile and frozen
  full/LeanEval gates pass.
- Performance revisit 28, index_det_le: Only the assigned public proof changes; exact signature and all surrounding source remain byte-identical.
  Independent original adapter, actual axioms/metadata/caller, complete LSP, profile and frozen
  full/LeanEval gates pass.
- Performance revisit 28, index_separated_mul_le_aux: Only the assigned private proof changes; exact signature and all surrounding source/caller bytes remain unchanged.
  Independent original adapter, actual axioms/metadata/caller, complete LSP, profile and frozen
  full/LeanEval gates pass.
- Next: fresh dedicated index_numeric_bound_aux performance revisit, then sum_max, lem7_Φ_bound and lem7_numeric plus the mandatory second theta_prefix_lt_aux repair, followed by independent filewide review/final gates. Counts remain unchanged on validated revisits.

The evidence and proposal descriptions below were prepared before this decision. Their historic
unapplied status is superseded only by the exact selected scope above and subsequent checkpoint
publication evidence. Dedicated original-declaration audits remain mandatory; none is counted
from the exploratory whole-file compiler probe.

A full independent copy of current Theta was compiled in namespace ThetaContractCandidate,
using Roth's existing Index/Separation APIs and original mathematical proofs. Only the menu
below, corresponding routine internal call arguments, and scoped classical proof instances
changed. Candidate file `/private/tmp/roth-theta-contract-candidate.lean`; actual command
`lake env lean /private/tmp/roth-theta-contract-candidate.lean` exited0. Successful log:
`/private/tmp/roth-theta-contract-candidate-fixed.log`. The earlier first draft failed solely
because omit was placed between a docstring and theorem; its failed log is not pass evidence.
No profiling/performance claim follows from this ordinary compiler result.

## A. Remove unused decidable-equality instance binders

| Public theorem | Proposed instance removal |
|---|---|
| one_mem_RSet | DecidableEq σ |
| indexSet_nonempty | DecidableEq σ |
| indexSet_bddAbove | DecidableEq σ |
| index_le_Θ | DecidableEq σ |
| Θ_nonneg | DecidableEq σ |
| Θ_le_card | DecidableEq σ |
| Θ_le_of_forall_index_le | DecidableEq σ |
| Θ_mono | DecidableEq σ |
| Θ_equiv | DecidableEq σ and DecidableEq τ |
| Θ_unique_le | DecidableEq σ |
| sum_max_sub_le_index_det | DecidableEq τ |
| index_det_le | DecidableEq τ |
| index_le_lem6 | DecidableEq τ |
| Θ_option_le | DecidableEq τ |

Fourteen public theorems,fifteen instance binders. Where necessary,classical decidability is
selected inside proofs. No definition/signature of RSet,indexSet,Θ,lem6M or lem6Φ is changed.
Fintype remains everywhere except the single B row below. The private renaming helper's
corresponding decidability removals in the exploratory copy are routine internal changes;
its own dedicated audit must still check them separately before live application.

## B. Remove unused Fintype from one_mem_RSet

The constant polynomial1 meets all coordinate degree/coefficient bounds without requiring
finitely many variables. The same proof compiles with arbitrary σ and classical decidability.
No other public Fintype removal is proposed here.

## C. Remove explicit unused hypotheses

| Public theorem | Proposed removal | Resulting mathematical statement |
|---|---|---|
| indexSet_bddAbove | hr : ∀j,0<r j | Its defining indices are bounded above for arbitrary natural weights. |
| Θ_le_card | hr : ∀j,0<r j | The supremum bound by card σ holds for arbitrary natural weights,still1≤B. |
| exists_eq_pow_mul_of_rootMultiplicity | hR : R≠0 | The integer factorization also holds for the zero polynomial. |
| sum_max_sub_le_index_det | hR : R≠0 | The retained nonzero determinant hypothesis supplies the nonvanishing needed by the proof. |
| index_det_le | hl' : l≤r none+1; hδ : 0<δ; consequently the unused implicit δ parameter | This factorized-determinant upper bound does not require those restrictions;1≤l,positive weights and every factor/degree/coefficient hypothesis remain. |
| index_le_lem6 | hq : ∀j,0<q j | The polynomial bound's proof works without this separate denominator positivity assumption. |
| Θ_option_le | hq : ∀j,0<q j | The supremum bound's proof works without this separate denominator positivity assumption. |

The r parameters remain implicit where originally implicit. No argument reordering,no conclusion
change,no weaker result,new axiom,sorry,resource-limit raise or live edit was used. These are
strictly scoped options; approving one row/group does not authorize unrelated widenings.
The coefficient domain remains integers,with real indices/bounds and natural weights/denominators.
The q-positivity rows deserve an explicit choice because the paper states positive denominators;
the compiled extension is valid under the existing division-by-zero/index conventions.

Removing the first two C restrictions exposes further unused hr parameters in index_le_Θ and
Θ_mono in the candidate. Those remain deliberately intact and are not included in this menu;
any further removal needs its own concrete scoped audit/decision. Likewise no general Ring,
non-finite index theory,new companion API,renaming or module restructuring is proposed here.

Historical preview status was unapplied. The exact selected scope is now approved above; each
selected amendment will be independently verified and published at its declaration checkpoint.
This preview does not replace those gates or authorize the two declined hq removals.


## Stronger original-contract, actual-axiom and caller verification

Completed independently after the ordinary candidate compile,without any live API edit.
Actual command `lake env lean --root=/private/tmp -o
/private/tmp/ThetaContractCandidateChecked.olean /private/tmp/ThetaContractCandidateChecked.lean`
exited0. `/private/tmp/roth-theta-contract-verified-v4.log` records29/29PASS lines.
The source is the complete independent candidate plus actual imported Roth.Theta and a verifier.
The earlier v1/v2 scratch meta/import errors and v3 missing --root export failure are NOT pass
samples; only v4 is accepted. No source/proof limit was raised or standard axiom bypassed.

For EVERY one of the29 original public declarations,the verifier constructs an explicit lambda
adapter taking the full actual original telescope,passes exactly the retained matching arguments
to the candidate,and kernel-checks an equality with the actual old constant. This checks exact
old-type recovery;the five defining values also recover by definitional equality. It then checks
all29 ACTUAL candidate axiom sets are subsets of propext,Classical.choice,Quot.sound. AST checks
reject DecidableEq anywhere in each14 group-A type (both occurrences in Θ_equiv),Fintype anywhere
in one_mem_RSet,and every removed C-row binder name in its actual candidate telescope.
The kernel-checked adapter declarations are in namespace ThetaOriginalContractAdapters.

An additional compiler importing the generated .olean exited0 and rendered ALL29 explicit
adapters with format.width100 and pp.proofs=true. Full inspect source
`/private/tmp/ThetaContractCandidateInspect.lean`;reviewable actual lambda terms in
`/private/tmp/roth-theta-contract-adapters-explicit.log` (earlier rendering hid proof expressions
with ellipses and is not the explicit-term artifact). Example:

```lean
@Roth.one_mem_RSet =
  fun {σ} [Fintype σ] [DecidableEq σ] {B} hB r ↦
    ThetaContractCandidate.one_mem_RSet hB r
```

Precise external caller inventory: repository-wide Lean-source searches for all15 changed public
names find exactly one direct use outside Theta: Roth/MainLemma.lean:672,
`index_le_Θ hr0 hWX hh`. Its hr and every explicit argument are retained;only implicit decidability
changes. The exact call shape is separately compiled at the end of the verifier,with actual
Roth.RSet/index/Θ in the hypotheses/conclusion and the candidate theorem as proof. No caller fix
is needed for this menu. MainLemma:670 calls Θ_lt with hq0;Θ_lt's entire original public contract,
including hq0,recovers in the29-adapter check. Roth/Main.lean,Roth/LeanEval.lean and Roth.lean have
no direct changed-API use. No MainLemma/Main source edit or denominator-contract removal is
proposed. Their full project validation will run after any approved live amendment.

Historical status at verification was UNAPPLIED; the subsequent exact decision is recorded above. Candidate verification
does not count toward the35 dedicated original Theta audits or authorize any further hr removal.

## D. Fresh original10 proposal: nonnegativity for all bounds and weights (extra widening declined)

The fresh dedicated Θ_nonneg audit found a canonical Real.sSup_nonneg proof. This gives the
strictly stronger public candidate below, keeping B/r implicit and q explicit:

```lean
theorem Θ_nonneg {σ : Type*} [Fintype σ] {B : ℝ} (q : σ → ℕ) {r : σ → ℕ} :
    0 ≤ Θ B q r := by
  apply Real.sSup_nonneg
  rintro _ ⟨R, _, h, _, rfl⟩
  exact index_nonneg _ _ _
```

This newly proposes dropping hB:1≤B and hr:∀j,0<r j, in addition to groupA's already-proposed
DecidableEqσ removal for this one theorem. No other groupA/B/C row is extended or inferred.
Fintypeσ, coefficient/denominator/weight domains and every definition remain unchanged.
The statement includes empty defining sets, whose real supremum is zero under the existing
formal definition; every member is a nonnegative index. Paper's nonempty positive-parameter
setting remains a special case. The user declined the extra hB/hr removal; those hypotheses
remain. Only the overlapping A.DecEq removal is approved.
The live proof can use the canonical argument with all original public binders retained.

Definitive actual-import evidence: `/private/tmp/roth-theta-nonneg-original.lean`, exit0,
raw `/private/tmp/roth-theta-nonneg-original.log`. It imports the ACTUAL Roth.Theta and proves
Stronger10.candidate against its actual definitions. An explicit lambda taking the full old
σ/Fintype/DecEq/B/hB/q/r/hr telescope kernel-equals actual Roth.Θ_nonneg by rfl; direct
getConstInfo.type comparison modulo universe alpha-renaming plus binderInfo/order checks PASS.
The independent copied baseline original proof also passes exact-type/kernel equality checks.
Candidate AST has precisely σ/Fintype/B/q/r, no hB/hr/DecEq; actual candidate/adapter/original
and both caller trials use only propext,Classical.choice,Quot.sound. Earlier prefix-only
candidate probe is separately useful but is not this actual-import compatibility evidence.

Exact caller inventory: four actual uses, all inside Theta, in index_le_lem6 (two) and Θ_lt
(two); no external use (module-doc mention is not a call). Both are add_nonneg pairs proving
0≤lem6Φ. Minimal prospective replacement after dropping hB/hr:
`add_nonneg (Θ_nonneg (B := M) _) (Θ_nonneg (B := M) _)`; fully inferred variant also compiles
against the actual lem6Φ definition. No caller edit or public amendment is applied from this
preview, and this exploration is not counted as an additional original declaration audit.

## E. Fresh original11 proposal: cardinal bound for all B/weights (extra hB removal declined)

The fresh Θ_le_card audit compiled the stronger candidate:

```lean
theorem Θ_le_card {σ : Type*} [Fintype σ] {B : ℝ} (q : σ → ℕ) {r : σ → ℕ} :
    Θ B q r ≤ Fintype.card σ
```

This NEWLY proposes dropping hB:1≤B, alongside this target's existing menuA DecidableEqσ
and menuC hr:∀j,0<r j removals. No other old menu row or new assumption is bundled implicitly.
It uses Real.sSup_le with the already-proved bound on each mapped-polynomial index and the
nonnegativity of cardσ. The empty defining-set case also satisfies the same bound by the
existing real-supremum convention. All definitions/domains/Fintype and remaining binder
order/implicitness are unchanged. The user declined the extra hB removal, so hB remains.
Only the overlapping A.DecEq and C.hr removals are approved.

Definitive ACTUAL-import source `/private/tmp/roth-theta-card-original.lean:138`, successful
raw `/private/tmp/roth-theta-card-original.log`. Independent baseline original proof, actual
built theorem and candidate/explicit full-old-args lambda adapter all compile. The adapter
kernel-equals actual Roth.Θ_le_card by rfl; direct old actual type/binderInfo/order checks PASS.
AST has exactly σ/Fintype/B/q/r and no hB/hr/DecEq. Original/actual/candidate/adapter and
named/inferred/old-shape inference trials all have only the standard three axioms.
Repository-wide source inventory has NO actual caller, internal or external: only declaration
and module-doc mention. Thus no downstream call fix is necessary; the named/inferred trials
are compatibility examples, not claims that such calls already occur in the project.
No source API edit/helper or additional original-declaration count follows from this preview.

## F. Fresh original13 proposal: monotonicity for all B/weights (extra widening declined)

The fresh Θ_mono audit compiled the stronger candidate against actual imported definitions:

```lean
theorem Θ_mono {σ : Type*} [Fintype σ] {B B' : ℝ} (hBB' : B ≤ B')
    (q : σ → ℕ) {r : σ → ℕ} : Θ B q r ≤ Θ B' q r
```

This NEWLY proposes dropping hB:1≤B and hr:∀j,0<r j, alongside this target's existing menuA
DecidableEqσ removal. The earlier menus do not implicitly authorize either new row. All other
parameters, definitions, domains, Fintype and retained binder order/implicitness stay intact.
The candidate supplies the cardinal upper bound for the larger indexSet directly, proves its
supremum nonnegative, and uses Real.sSup_le. Thus it also covers empty defining sets and zero
weights. The user declined the extra hB/hr removal, so both remain. Only the overlapping
A.DecEq removal is approved; the broader candidate stays unapplied.

Definitive ACTUAL-import source `/private/tmp/roth-theta-mono/positive.lean:19`, exit0 raw
`/private/tmp/roth-theta-mono/positive.log`. Independent baseline original proof, styled proof,
and explicit full-old-args lambda adapter have the actual old theorem type modulo universe
alpha-renaming, with BinderInfo checked separately. The lambda adapter kernel-equals actual
Roth.Θ_mono by rfl. Candidate AST has exactly seven binders σ/Fintype/B/B'/hBB'/q/r, with no
hB/hr/DecEq. Original/actual/candidate/adapter and the caller reproof all use only the standard
three axioms. No performance claim is made for this optional API candidate.

Exact caller inventory: two actual uses, both in Θ_lt; no external use (module-doc mention
excluded). The complete independent original Θ_lt proof compiles against actual imported
definitions after replacing exactly those two calls by `strong hMlt.le _`. Its actual public
caller type is checked directly and its actual axiom set is standard. Thus the prospective
minimal production fixes are `Θ_mono hMlt.le _` in both places; no caller or public API edit
has been applied from this preview, and no additional original declaration is counted.


## G. Original19: leading-coefficient localization (implemented under standing authorization)

`pow_rootMultiplicity_le` now assumes only `hB : |(R.leadingCoeff : ℝ)| ≤ B`,
rather than the uniform coefficient premise. Every other parameter/domain, argument mode/order/name
and the conclusion remain. This strengthens the theorem by using precisely the coefficient
compared in the proof and the paper. The sole `Θ_unique_le` caller supplies
`hcoef R1.natDegree`; its full immutable original public contract remains unchanged.
The original uniform-bound theorem is recovered by the explicit adapter specializing the old
`hB` at `R.natDegree`, definitionally the leading coefficient. This change is separate from
the earlier declined D/E/F changes to the Θ bounds, which remain declined and unapplied.

Preapply candidate, original-contract adapter and candidate caller compiled exit0 before mutation:
`/private/tmp/roth-rootmult-bound/preapply.lean` and `preapply.log`. Definitive post-build
`actual-original.lean`/`.log` independently replay immutable originals and check the exact new
premise, every other retained domain/name/order/BinderInfo, full-old adapter, original caller
contract and actual standard axiom sets. Source edits were frozen before final sequential gates.
Complete final LSP: 0 errors,18 warnings. Repeated accepted target/caller profiles:366.074/829.009ms,
under1000ms with the required ≥750 caller repeat passed. Frozen full build77.364s then separate
LeanEval24.504s both exit0 on all17identical project/pin hashes.
[Detailed original19 audit](Theta-pow_rootMultiplicity_le.md). Original counts after publication:
Theta19/35,overall200/264,9/14files; no new helper. The uncompiled cumulative final29 verifier
now explicitly handles this exact hB specialization alongside the selected A/B/C removals;
it is FINAL-STATE scaffolding, not a current all29 verification claim.

## H. Original26: unconditional positive-part sum bound (implemented under standing authorization)

The independently compiled candidate removes both `min_le_sum_max.hrp` and `.hθ`:

```lean
theorem min_le_sum_max {θ : ℝ} {rp : ℕ} (l : ℕ) :
    min (l * θ / 2) (rp * θ ^ 2 / 3) ≤
      ∑ ν ∈ Finset.range l, max 0 (θ - ν / rp)
```

Zero `rp` and nonpositive `θ` give a nonpositive minimum. For positive inputs, the
finite arithmetic-sum estimate handles both sides of the cutoff without the old `>10`
condition. The public name, real/natural domains and exact conclusion stay unchanged.
The owner implemented this supported recommendation under the user's standing instruction
to implement recommended changes. It is separate from the explicitly retained Θ/hq assumptions.

Before application, `/private/tmp/roth-theta-min-sum/candidate-compatibility.lean` and its
exit-0 log independently replay the immutable original proof and its two old arithmetic
predecessors, prove the unconditional candidate, and check the complete original-telescope
adapter by kernel `rfl`. Original and candidate actual axioms are standard only. The
sole-caller fix in `index_le_lem6` deletes the two proof arguments and supplies the now-needed
inference parameters: `min_le_sum_max (θ := θ) (rp := r none) l`. Its independent full original
contract/axiom checks remain required.

The two previously audited public floor lemmas remain public. All original prose is preserved,
with the additional explanation of the stronger scope. Three new private proof helpers each
received a separate fresh dedicated audit: linear15, positivecore22, quadraticwrapper7 body
lines; the public proof is7 lines. The wrapper audits additionally remove private radius
positivity and admit the weak cutoff. Their exact first-contract adapters and independent
proofs pass. No new helper or routine caller change adds an original declaration.

On final Theta SHA256 `e6360c9acdc9d7be22356ba3a26006e24cc1b0b667b5992395759228e1087530`,
module and complete unfiltered LSP pass (0errors17warnings); independent immutable original
min plus ENTIRE index_le_lem6 proofs, exact original telescopes/BinderInfo and actual
standard axiom sets pass. Final uncontended real exact-prefix profiles: public165.806ms,
linear460.921ms, positivecore543.552ms, quadraticwrapper304.757ms, all<750ms. Frozen full
project build92.510s then separate LeanEval33.553s both exit0, all17 source/pin hashes stable.
[Original26 and helper audit links](Theta-min_le_sum_max.md). After successful publication:
Theta26/35, overall207/264;9/14files. The final29 generator requires exact named drops
`[hrp, hθ]`; it remains UNCOMPILED final-state scaffolding, not current cumulative evidence.
Whole-Theta profiling and remaining originals/final phases remain outstanding.


## I. Original28: redundant coefficient-bound premise (implemented and validated)

Alongside the selected A/C removals, `index_det_le.hB : 1 ≤ B` is removed under the
standing instruction to implement supported recommended changes. The target only used it
to establish nonnegativity of B. Its retained uniform coefficient bound already proves
that directly at the zero monomial:

```lean
have hB0 : (0 : ℝ) ≤ B :=
  (abs_nonneg ((R.coeff 0 : ℤ) : ℝ)).trans (hR.2.2 0)
```

The coefficient estimate derives the same fact from its retained uniform coefficient premise,
so it needs no separate nonnegativity argument. Its fresh helper audit found the existing
`abs_coeff_det_hasseDeriv_le` at constant degree bound sufficient and deleted the single-use
private coefficient wrapper. No nonzero witness or added assumption is needed for this deduction. This recommendation is separate from the user's
explicitly retained hB arguments on Θ_nonneg, Θ_le_card and Θ_mono; those remain intact.
The target's exact removed binders, in the original effective order, are DecidableEqτ,
δ, hB, hl′, hδ. Every other public binder/domain/mode/name/order and conclusion remains.
The sole caller deletes hB/hl′/hδ0 at its hupper application, while keeping its entire own
original telescope, including its own hB, δ/hδ0, hq and DecidableEqτ.

Before live application, the exact candidate containing both extracted helpers compiled
with the complete independent original namespace, full-old target/caller adapters,
all retained type/name/order/BinderInfo/universe/conclusion checks and original opaque
proof-value checks. Both original target and ENTIRE original index_le_lem6 proof are
replayed independently. Candidate/original/recovery axiom sets are standard only.
Clean final preapply log: `/private/tmp/roth-theta-index-det/candidate-compatibility-final.log`;
earlier clean candidate evidence is in candidate-compatibility.log. Failed scratch trials
are not certification. The exact first live full snapshot SHA256 is
`42d60acc1b1b3d587ffe568e246cb9ba637ee0a6449a6a2b29d6f02249354ba4`.

Both initially extracted private helpers received separate fresh dedicated audits. The coefficient
helper was deleted after replacing it with the existing constant-degree specialization; its
independent first proof, exact contract and actual deleted-constant/trace absence pass. The
retained separated-product helper has26 proof lines; its independent first proof and actual
full private telescope/value/BinderInfo/standard axioms pass. Public proof24 physical lines
includes all3 Step comments and satisfies its ordinary≤30 cap. No third helper was introduced.

On final Theta SHA256 `c6e59b0ff252c0cdfc0e00070bb7c0c5bea3a53e0786889767f4b1594f5e6ee3`,
module, complete unfiltered native LSP0errors11warnings, exact independent original public28
and ENTIRE original caller proofs/adapters/type/value/standard axioms all pass. Fresh real global
prefix profile: retained helper655.221ms/public742.222ms, both<750ms. Frozen full project
build91.138s then separate LeanEval30.612s both exit0 with all17 source/pin hashes stable.
[Original28 final batch evidence](Theta-index_det_le.md). After successful publication:
Theta28/35, overall209/264;9/14files. The UNCOMPILED final29 generator records the exact hB
drop but remains final-state scaffolding, not current cumulative evidence. Whole-Theta profiling
and remaining originals/final phases remain outstanding.


## J. Original29: weak ratio boundary (implemented; validated publication)

The selected proof needs only `∀ j, (r none : ℝ) ≤ δ * r (some j)` in
`index_le_lem6`, rather than the original strict inequality. The weight estimate multiplies
this nonstrict bound by nonnegative multi-index coefficients; every later conclusion is a
nonstrict bound. This admits the equality boundary with the exact same conclusion and
unchanged domains. The owner recommends this supported weakening under the user's standing
instruction to implement recommended changes. The explicit retained hq and earlier Θ-bound
hB/hr preferences remain untouched; no other public argument is changed by this proposal.

Before live application, the full weak-ratio candidate compiled independently in
`/private/tmp/roth-theta-lem6/weak-ratio.lean`, exit0 (26.464s). The exact preapply verifier
`ratio-preapply-compatibility.lean` and clean exit0 log (40.574s) replay the immutable original
proof namespaces, check the exact entire old29 adapter (approved DecidableEq removal and
strict hratio forwarded via `le_of_lt`), preserve the full original Θ_option_le type AND
independent full caller proof with its strict assumption, and check opaque proof values and
actual candidate standard axiom sets. The minimal actual caller fix is to pass
`fun j ↦ (hratio j).le`; the caller's own public ratio remains strict.

The exact weak-ratio API and the strict caller `.le` fix are applied. On final source SHA256
`47369dc4b524f54d2981a0c23e67786b442f061e86c1ec2f6141d6c46fb62c69`, all three new private
helpers have separate fresh complete audits; public proof22lines, numeric16, weight12, mapped14.
Final module, independent entire original29+original30 proofs/adapters/type/value/standard axioms
and complete unfiltered native LSP0errors10warnings pass. Both real exact-prefix sweeps pass
(public895.050/854.163, numeric939.576/873.525, weight408.013/361.605, mapped707.126/651.477ms).
A shorter mapped simp variant with an overbudget sweep was rejected and its raw history retained;
the explicit14-line transport certificate is final. Frozen full project build92.063s then
separate LeanEval29.415s both exit0 with all17 project/source/pin hashes unchanged.
[Original29 final batch evidence](Theta-index_le_lem6.md). After successful publication:
Theta29/35,overall210/264,9/14files. At this first checkpoint K was a distinct queued dedicated revisit; its subsequent
validated application is recorded below. The UNCOMPILED future final29 generator includes the exact current
strict-to-weak ratio localization; original30 DecidableEq removal remains pending and the
generator is not cumulative verification evidence. Whole-module profiling/final phases remain.



## K. Original29 arithmetic boundary (implemented; dedicated revisit validated)

Under the standing instruction to implement recommended changes, the fresh dedicated
original29 revisit extends the exact same conclusion to `hδ0 : 0 ≤ δ`, `hδ1 : δ ≤ 1`,
`hrp : 3 ≤ (r none : ℝ)`. It also removes only this theorem's derivable `hr0` and `hB`: the
ratio and positive distinguished weight force all weights positive, and a nonzero integer
coefficient plus its uniform bound imply1≤B. The existing weak coordinate ratio, hq, domains,
shared witness and conclusion remain. The protected globalΘ hB/hr preferences are unchanged.

The initial three-boundary candidate and exact full original29 adapter plus ENTIREoriginal30
new-candidate caller proof compiled in
`/private/tmp/roth-numeric-helper/public-candidate-compatibility.lean/log` (50.921s).
The fresh revisit then compiled the complete additional hr0/hB-drop candidate BEFORE live
application in `/private/tmp/roth-public29-K/candidate-compatibility.lean/log`, with full old29
and old30 immutable proofs/adapters/names/BinderInfo/universes/conclusions/opaque values and
actual standard axiom sets. The entire NEW30 caller proof explicitly depends on the new29
constant. The minimal actual caller forwarding preserves its ENTIRE original public telescope,
forwards strictδ bounds by.le, derives3≤rp from its old reciprocal premise, and removes only
obsolete hr0/hB application arguments. Its newly exposed unused hr0 is reserved for original30's
own fresh audit, alongside its previously selected DecidableEq removal.

Final source SHA256
`59fc1479999b47953aff7aee6bf8be17a325e9523ca94375d8b48b273618e427`,946lines/public29proof29,
no new helper; all three existing private helpers and other source are byte-identical.
[Dedicated fresh revisit](Theta-index_le_lem6-boundary-revisit.md) records all24/42/fiveactual
search/everybinder/literature/inversion/packing/inequality/11checks. Fresh module34.272s,
full actual compatibility50.088s and complete unfiltered nativeLSP0errors11warnings pass.
Owner separately compared BOTH full immutable originalIndex and originalTheta proof blocks;
all exact original contracts, actual proof values, standard axiom sets and caller dependencies
pass. Real exact-prefix first/repeat ms: public996.125/936.382,numeric918.885/829.176,
weight455.974/355.065,mapped722.709/634.434; every target passes both1000ms runs.
Frozen owner full build92.105s THEN separateLeanEval29.557s both exit0; all17 project/source/pin
hashes unchanged. No source or limit mask; no whole-module profile claim.

After successful publication, counts remain210/264,Theta29/35,9/14files. This is the ninth
validated revisit (eight prior approved-scope revisits, this supported standing-authority
revisit), with no original-count increase. Next original30 Θ_option_le. The UNCOMPILED future
all29 generator must encode exact weakδ/rp3 forwarding and index29 hr0/hB drops; no cumulative
final-state verification is claimed until original30's own audit and cumulative gates.


## L. Θ_option_le boundary alignment (original30; validated publication)

The fresh original30 audit removes the selected `[DecidableEq τ]` binder and its now-derived
`hr0` premise, and aligns the unchanged bound with index_le_lem6: `0 ≤ δ`, `δ ≤ 1`,
`3 ≤ (r none : ℝ)`, and weak coordinate ratios. It retains `hq` by explicit user preference
and `hB` as the existing supremum-wrapper input. No domain, conclusion, definition, import or
private helper changes. The public headline proof is five lines (immutable initial6; immediate
pre-audit8 after K forwarding). These supported recommendations follow the standing instruction
to implement recommended changes; no additional user approval was inferred or requested.

Before live application, `/private/tmp/roth-public30-option/candidate-compatibility.lean/log`
compiled the exact new theorem and complete original30 adapter, preserving every retained name,
type, BinderInfo and positional universe. The ENTIRE original Θ_lt proof and its entire adapted
new proof/type/value/standard axioms were checked, including explicit new30 dependency. The
minimal actual caller forwards old strictδ/ratio premises by.le and derives3≤rp from the old
reciprocal bound; its own entire public telescope remains unchanged. Protected hq omission was
positively tested but deliberately not applied. [Fresh audit](Theta-Theta_option_le.md).

Final source SHA256
`c488d3189154ae0da29fd6d798c3b1d016e44fa588ab4ab32a5ea7c93c3837fd`,948lines. Module, actual
complete compatibility and complete unfiltered native LSP0errors8warnings pass. REAL exact
prefix-through30 first/repeat ms: Θ_option158.615/144.368,index29 901.577/925.763,
numeric903.545/922.672,mapped693.423/723.578,weight401.279/399.404; all five pass both1000ms
sweeps. Earlier broader-prefix baseline overages remain diagnostic history; no whole-module
performance pass is claimed.

All selected A/B/C applications are now applied, including all15 DecidableEq removals across
14 public declarations and the single selected Fintype removal. Owner compiled cumulative
recovery of ALL29 original public contracts and ALL5 definition values, with exact named
drops/forwarding and both immutable entire original proof blocks. The final enhanced verifier
passes29 entire old adapters,87 explicit opaque body-type checks and87 actual standard axiom
checks (exit0,48.324s). Source/log/record are archived as
`/private/tmp/ThetaApprovedOriginalFinalProbe-d30-values.lean` and
`/private/tmp/roth-theta-d30-values-cumulative29.{log,json}`. These completed current cumulative
gates supersede earlier sections' UNCOMPILED/pending-original30 generator status.

Frozen full build113.288s THEN separateLeanEval37.676s both exit0; all17 project/source/pin
hashes remain identical, including after the cumulative verifier. After successful publication:
overall211/264,Theta30/35,9/14files. No new helper or count from revisits. Next original31
private one_lt_of_log_pos, then32–35 and mandatory final file phases. Earlier public-wrapper,
hq, globalΘ hB/hr, domain and header preservation choices remain in force.


## M. lem6M_lt positive-p/closed-log bound (original32)

Under the standing instruction to implement well-supported recommendations, original32 now
requires `0 < p` instead of `2 ≤ p`, omits `0 < r₁` derived from `1 ≤ l ≤ r₁`, and accepts the
closed logarithmic lower bound. Its conclusion remains strict because `log 2 < 1` supplies
strict slack. Natural domains and all other public inputs remain, and the complete `Θ_lt`
public telescope is unchanged. Only its obsolete positive-r₁ application argument is removed.
The public docstring accurately records the strengthened range while retaining the source quote.

Before application, the concrete entire candidate, exact immutable original32 adapter and ENTIRE
original/current Θ_lt independent proof/type/value/standard axioms compiled. Original32 proof
53→21 lines with two substantive private estimates, each subsequently assigned a separate fresh
full audit. Final private coefficient bound accepts `l ≤ 2 ^ r₁` (proof9lines); the analytic
estimate accepts `0 ≤ q` and internally derives positivity (proof21lines). Exact independent
INITIAL helper contracts and all actual built values/standard axioms pass. No extra helper,
public definition, conclusion, import, header or protected-hypothesis change.

Final source `edd28b8b48e01767e9d4434e08c0190f8a8848a873497bd647fa25e8ecdbc35f`,949lines.
Module and complete unfiltered native LSP pass (0errors8samewarnings). Actual uncontended final
prefix profiles: public32675.914ms, coefficient290.063ms, exponential597.526ms, all below750.
Owner cumulative final-state recovery passed47.118s: ALL29 original public adapters, ALL5
original definition values,87opaque body-type checks and87actual standard-axiom sets. Both full
immutable original proof blocks remain byte-identical72cf/355a. Exact successful source/log/record:
`/private/tmp/ThetaApprovedOriginalFinalProbe-d32-values-corrected.lean` and
`/private/tmp/roth-theta-d32-values-corrected-cumulative29.{log,json}`. The first stale generated
probe failure and its correction are recorded in the original32 audit, with raw evidence retained.

[Original32 audit](Theta-lem6M_lt.md), [fresh coefficient audit](Theta-factorial_coefficient_le_two_pow_aux.md),
[fresh exponential audit](Theta-two_pow_lt_rpow_aux.md). Earlier numeric/index29 failed repeat
1068.193/1115.157ms and actual whole Θ_lt profiler stalls remain mandatory file-final repair;
no whole-file performance pass is claimed. Owner frozen full/separate LeanEval publication gates
are recorded with this original32 checkpoint; helpers/revisits add no original counts.


Original32 frozen owner full91.810s THEN separateLeanEval31.678s pass; all17 source/pin hashes
stable. Successful publication yieldsTheta32/35,overall213/264,ninefiles. Exact source/audit commit
is recorded in central cleanup-progress; no original inflation from the two fresh helper audits.


## N. lem7_Φ_bound closed upper endpoint (original33)

Under standing implementation authority, `δ < 1` becomes `δ ≤ 1`, with the strict conclusion
preserved. All other public binders, domains and conclusion remain. The sole current Θ_lt
application forwards its old strict bound by.le; that caller's entire effective public type and
independently re-elaborated proof/value/standard axioms are checked. The paper's strict range
remains accurately quoted; the extra endpoint is this compiled proof's strengthening.

The dedicated full original33 audit proved the concrete candidate and exact immutable old33
adapter before application, then checked the actual built ROOT adapter, independent old/current
proof values, standard axioms, complete unfiltered native diagnostics0errors8samewarnings, and
ENTIRE original/current Θ_lt proof/type/value/dependency. No helper/import/header/definition
change. Dead locals and one-use facts were removed, direct product bounds replaced one broad
nonlinear step, and terminal arithmetic is restricted to the supplied scaled bounds. Proof22→20.

Actual baseline1489.059ms improved to876.021ms; required same-source repeat757.251ms also passes,
with all raw traces retained and no third cherry-picked run. These are scoped prefix measurements;
previous numeric/index29 failed repeats and whole Θ_lt stalled profiles remain mandatory final
repair. SourceSHAfc354913a6695d434020810dd37299614daa2bd7ca345b0e8bac489492679337,947lines.

Owner regenerated cumulative recovery passes all29 original-public adapters, all5 definition
values,87opaque body-type checks and87actual standard-axiom sets in51.807s; both entire original
proof blocks remain unchanged. Exact archived input `/private/tmp/ThetaApprovedOriginalFinalProbe-d33-values.lean`,
SHA6d7fc49401e480f2e681a733ccabf9c5dae1d1f3f764410205738fcc57ffed10.
[Detailed original33 audit](Theta-lem7_Phi_bound.md). Frozen owner build/publication gates are
recorded with this checkpoint; no new helper or revisit count.


Original33 frozen owner full105.519s THEN separateLeanEval38.323s pass, all17 source/pin hashes
stable. Successful publication yieldsTheta33/35,overall214/264,ninefiles; exact source/audit hash
is recorded in central progress. Original34/35 and every file-final phase remain.


## O. lem7_numeric closed bounds and arbitrary Φ (original34)

Under standing implementation authority, δ<1 becomes δ≤1, the strict Φ upper bound becomes
closed, and Φ nonnegativity is removed. The strict conclusion, domains and retained binder
metadata remain. The only Θ_lt change forwards its strict bounds by.le and removes its now
unneeded local Φ-nonnegativity proof. No new helper. The numerical target proof25→29lines
meets its ordinary30-line cap; all subproofs≤5. Source attribution is preserved and the
docstring accurately records the additional endpoints/negativeΦ range. Keeping the Nat/Real
domains and public name is a technical recommendation, not an explicit user veto.

Concrete preapply and final actual certificates recover the exact immutable old34 telescope
(including old Φ nonnegativity), ENTIRE old/current/independent Θ_lt proof/type/opaque value,
actual standard axioms and dependency. Complete native LSP has0errors8unchangedwarnings.
Owner final cumulative d34-values passes all29 original-public adapters/all5 definition values/
87opaque body-type checks/87actual standard-axiom sets in50.626s; both complete original
proof blocks remain byte-identical72cf/355a. Exact archived input
`/private/tmp/ThetaApprovedOriginalFinalProbe-d34-values.lean`,
SHAdf89dc269811de74901c772a70a4ccf9fb0b0a9c2d1ebd2bb4c66063c14ad5b1.

Actual baseline1429.265ms improves to757.682ms; mandatory same-source repeat865.831ms also
passes. Both final full raw traces are strict UTF8; the baseline earlier-prefix invalid bytes
remain untouched with exact offsets and valid target slice provenance. No third timing sweep,
raised limits or whole-file performance claim. The earlier numeric/index29 required-repeat
failures1068.193/1115.157ms and actual wholeΘ_lt trace stalls remain mandatory final repairs.
[Full original34 audit](Theta-lem7_numeric.md). Frozen owner full/separate LeanEval gates are
recorded with this checkpoint. Successful publication givesTheta34/35,overall215/264,ninefiles.


### Original35 recommended application under standing authorization

The user’s standing instruction is “From now on implement all changes that you recommend. Only ask me if you can't decide.” The supported Θ_lt cleanup applies after concrete independent proofs, exact full original adapters and whole original/current MainLemma caller recovery: remove derived hr0/hq0 and the unnecessary δ upper bound; replace10/δ<rLast with3≤rLast; weaken adjacent strict division ratios to closed multiplicative bounds and the strict logarithm lower bound to≤. The conclusion, domains, retained binder names/order and public definitions remain unchanged. MainLemma keeps its entire26-binder public contract and changes only the necessary Θ_lt proof call. All11 introduced helper obligations and the extra prefix performance revisit are complete. Explicit prior hq preservation in index_le_lem6/Θ_option_le, selected global hB/hr choices and header/wrapper/domain preferences remain. Original35 is a scoped checkpoint; the eight older performance revisits and file-final phases remain outstanding.
