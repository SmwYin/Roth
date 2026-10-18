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
Θ_le_card's overlapping C.hr removal remain approved. This selected scope does not itself authorize another hypothesis, definition,
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
- Approved revisit 6, one_mem_RSet: Only the approved Fintype σ and DecidableEq σ removals applied with independent original adapter,
  actual axioms/metadata/caller, complete LSP, profile and frozen full/LeanEval gates.
- Approved revisit 7, indexSet_nonempty: Only the approved DecidableEq σ removal applied with independent original adapter,
  actual axioms/metadata/caller, complete LSP, profile and frozen full/LeanEval gates.
- Next: approved revisit of original 8, indexSet_bddAbove (DecidableEq σ and hr only, plus necessary caller proof fixes). Counts remain unchanged on approved revisits.

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
