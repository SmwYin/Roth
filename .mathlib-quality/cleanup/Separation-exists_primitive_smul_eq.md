# exists_primitive_smul_eq — initial audit (before source edits)

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md, plus style, naming, profiling, and the Phase 4 worker contract.

Baseline: branch ramin-cleanup, HEAD 2622b32, target original declaration 25/30; prior actual profile /private/tmp/roth-d24-final-profile.log(.json). Source target lines 400–438; 36 body lines (computed below). Scope: target and necessary new private proof helpers only.

Mathematics: clear denominators; divide the integral coefficient family by its nonzero gcd; reconstruct the primitive polynomial; rescale the original rational polynomial. The scalar equation and gcd condition must hold for the SAME polynomial witness, so replacing this correlated existential conjunction by independent existential results is mathematically inapplicable.

| Audit | Initial finding / action |
|---|---|
|1 LINT|Native complete diagnostics requested, pending; no suppressed warnings.|
|2 HAVE|hne proves support nonempty; hg0 proves gcd nonzero; hUcoeff computes reconstructed coefficients; hU0coeff gives coefficient factorization; h1 transports map coefficients; hsupp proves support equality. All carry proof content except h1, which is consumed through normalization.|
|3 SET_OPTION|None in target.|
|4 SIMP|hUcoeff and hsupp terminal simp remain unsqueezed; coefficient-map normalization uses nonterminal simp only.|
|5 NAMING|exists_primitive_smul_eq describes scalar normalization to primitive coefficients, snake_case, no forbidden abbreviations/numeric schemes. No rename warranted.|
|6 WIDTH|Signature width arithmetic follows below.|
|7 BY|Already on signature end.|
|8 FORMAT|Replace mathematical lambda => with ↦; no tactic packing; no haveI/letI.|
|9 COMMENTS|No inline comments in target; preserve source docstring verbatim.|
|10 DOCSTRING|Existing statement and source note preserved by explicit contract.|
|11 VISIBILITY|Public contract retained; any extracted stage private with _aux.|
|12 STRUCTURE|36 body lines: first try Mathlib/golf, otherwise extract integral primitive normalization stage, each body <=30. Correlated existential conjunction retained for reason above.|
|13 MATHLIB|Actual five searches run: Finder finds univariate integerNormalization/primPart; Loogle finds Finset.extract_gcd/gcd_div_eq_one; LeanSearch finds univariate IsPrimitive; rg confirms existing extract_gcd building block; local search finds extract_gcd but index unavailable. No whole multivariate replacement established. Need compiled exact? route.|
|14 JUNK DEF|n/a theorem.|
|15 EXISTS|n/a public substantial construction, not trivial private witness.|
|16 SHOW|None.|
|17 PUSH_NEG|None.|
|18 GENERALISE|Effective σ : Type*, G : MvPolynomial σ ℚ, hG : G ≠ 0. σ universe already arbitrary and G essential data. hG used to prove nonempty support; drop-test and zero counterexample to be compiled. No inherited τ instances appear in target. Generic fraction-field/GCD-domain variant is a substantive different API, not applied. Inversion check does not fire: Rat casts/denominators and integer gcd are essential.|
|19 INEQUALITY|No order inequalities anywhere in target signature/body, only ≠. No reversed order notation or names.|
|20 NORMAL FORM|Finite support gcd=1 is existing Finset API; Mathlib primPart/IsPrimitive located are univariate, no unsupported replacement.|
|21 SYNTAX GEN|Same-witness existential useful to caller exists_int_factors. No restatement needed.|
|22 IMPORT FANOUT|No imports planned.|
|23 CASTS|Integer→rational denominator and natural→rational scalar genuine cross-type; retain load-bearing coefficient ascriptions.|
|24 INSTANCE NAME|n/a no instance declaration.|

Literature search: actual web query “primitive polynomial rational coefficients clearing denominators gcd integer polynomial Gauss lemma”. Primary Stanford notes https://crypto.stanford.edu/pbc/notes/numberfield/gausslemma.html describe rational rescaling to integer polynomials with gcd 1. This supports the normalization stages; a general fraction-field variant needs a separate API proposal and is not necessary here.

Initial issues: 36-line proof needs mathematical decomposition if golf cannot reduce below 30; lambda style. No public API proposals. Native goal/automation and diagnostics in flight before source edits.

|Signature line|Width|Next group|Combined|Decision|
|---|---:|---|---:|---|
|400|82|`∃ (g : ℚ) (U : MvPolynomial σ ℤ), g ≠ 0`|122|overflow; break|
|401|81|`U.support.gcd (fun d => U.coeff d) = 1`|120|overflow; break|
|402|45|``|—|end|

## Applied proof cleanup

Actual measured original target: lines 400–438, 39 declaration lines, 36 proof-body lines (dispatch's “~38” was approximate). Final: lines 400–432, 33 declaration lines, 30 proof-body lines. Whole module 570→564 lines. Git diff: 12 insertions/18 deletions, net −6. No helper introduced; no additional independent helper worker required.

Used `support_nonempty` to express nonzeroness directly; the contradiction is terminal `simpa` on the mapped scalar equation. Coefficient reconstruction simp handles the universal binder directly. Coefficient factorization uses two terminal simplified membership cases. Support equality uses its coefficient characterization in one terminal simp. No tactic packing or source narrative deletion. Original mathematical lambda syntax updated to ↦, with definitionally identical public type.

All six original `have`s retained for distinct mathematical roles. h1 is normalized and rewritten before use, so direct inlining would obscure the coefficient comparison. All nonterminal simp remains `simp only`; all new simp/simpa is terminal. No casts added: existing natural/integer→rational casts retained, no redundant same-type casts introduced.

## Golfing rules — all 42

|Rule|Result|
|---|---|
|1.1|n/a: no `by exact` wrapper.|
|1.2|n/a: no `by rfl`.|
|1.3|Already terminal `rwa` in scalar coefficient equality.|
|1.4|Applied: support nonempty contradiction terminal simpa.|
|1.5|n/a: no trailing rfl.|
|1.6|Already existential tuple construction.|
|1.7|n/a: no apply/exact chain.|
|1.8|n/a: no by_contra/push_neg.|
|1.9|Coefficient lambdas carry projection/application data; no eta-redex. Mathematical lambdas changed to ↦.|
|1.10|h1 retained: rewritten/cast-normalized before use; remaining haves carry proof content.|
|1.11|n/a: no apply/intro chain.|
|1.12|n/a: no show.|
|1.13|Already destructures extract_gcd and denominator existence with obtain.|
|1.14|No consecutive independent rw calls to merge; h1 cast normalization separates rewrites.|
|1.15|No terminal simp only; nonterminal coefficient normalization intentionally squeezed.|
|1.16|No nonterminal bare simp.|
|1.17|Already uses support_nonempty.mpr and `.symm`; no useful dot conversion remains.|
|1.18|n/a: no trailing tactic argument parentheses suitable for <|.|
|1.19|n/a: no push_neg.|
|1.20|n/a: public substantial correlated existential; no trivial private existential.|
|2.1|Actual native whole-proof grind failed to construct witnesses; coefficient-equation grind also failed.|
|2.2|n/a: no retained grind, so no precursor deletion.|
|2.3|Applied: terminal simpa for in-support coefficient factorization and support contradiction.|
|2.4|n/a: no analytic function property.|
|2.5|Nonzero gcd/scalar comes from input hG and coefficient extraction, not structural positivity; exact_mod_cast preserves known nonzero facts.|
|2.6|n/a: no monotonicity/order comparison.|
|2.7|n/a: no linear integer arithmetic goals.|
|2.8|Actual native whole aesop failed to construct witnesses; no retained search automation.|
|2.9|Existing exact_mod_cast is the direct cast bridge; no numeric computation to normalize.|
|2.10|n/a: arbitrary-variable polynomial existence cannot be decided by finite computation.|
|2.11|Actual native field_simp; ring at coefficient equality failed: remaining product equation needs h1. Kept direct rwa.|
|2.12|Actual native linear_combination h1 at coefficient equality failed with denominator terms. No terminal ring/ring_nf in retained proof.|
|2.13|n/a: membership and nonmembership branches are asymmetric mathematics.|
|2.14|n/a: no calc block.|
|2.15|Two final goals are polynomial coefficient equality and gcd identity, different arguments; common automation inappropriate.|
|3.1|n/a: no erw.|
|3.2|n/a: no continuity/measurability.|
|3.3|n/a: no omega.|
|3.4|Original rintro rfl eliminated by terminal support contradiction.|
|3.5|No global automation attribute: existential construction is not a simp normal form.|
|3.6|n/a: no simp_all only.|
|3.7|n/a: no maxHeartbeats or limit change.|

Native live goal inspection at original line414 verified gcd nonzero reduces to negating all coefficients zero. Initial multi_attempt at original line405 targeted the outer have command rather than its inner proof, so those failed position experiments are NOT evidence against support_nonempty; isolated full proofs validated the actual replacements. A later mistaken line429 probe targeted support equality; discarded. Correct line427 coefficient probes above were performed afterwards. No source edits resulted from those probes.

## Generalisation and contract

|Effective binder|Probe / finding|Disposition|
|---|---|---|
|σ : Type*|Actual #check output in independent log confirms full universe polymorphism, with no Fintype/DecidableEq assumptions. Removing the type binder leaves dependent G ill-formed; this is data, not an unused assumption.|Retain arbitrary Type*.|
|G : MvPolynomial σ ℚ|Necessary polynomial data occurs in scalar identity and hG. Removing the binder while keeping its dependent statement is ill-formed; no claim of compiled negative drop-test.|Retain implicit parameter.|
|hG : G ≠ 0|Zero specialization negation proved in independent scratch file: mapped U=0 forces U=0, whose support gcd is 0, contradicting gcd=1. This is a kernel-checked reason the hypothesis cannot simply be dropped.|Retain.|

No inherited τ/Fintype/DecidableEq binders occur (actual compiled #check). Generic GCD-domain/fraction-field normalization is mathematically plausible, but would introduce a substantive API; no such change applied or required. The proof continues to use rational denominator arithmetic, integer casts, and integer coefficient gcd, so inversion does not produce an immediate abstract replacement.

No global claim of Mathlib absence: five actual searches locate the existing finite-family API and univariate APIs; whole live `exact?` search was attempted without establishing a new multivariate replacement. Since no helper/API is added, no absence claim is used to justify a new declaration.

## Final width and inequality artifacts

|Line|Width|Next syntactic group|Arithmetic|Action|
|---|---:|---|---|---|
|400|82|`∃ (g : ℚ) (U : MvPolynomial σ ℤ), g ≠ 0 ∧ map (Int.castRingHom ℚ) U = g • G ∧`|82 + 1 + 77 = 160 > 100|ok|
|401|81|`U.support.gcd (fun d ↦ U.coeff d) = 1 := by`|81 + 1 + 43 = 125 > 100|ok|
|402|49|``|end|ok|

|Inequality occurrence|Orientation|Action|
|---|---|---|
|None in signature or body (≠ is disequality)|No ≥ or > order notation; no _ge_/_gt_ name|No rewrite needed|

## Step-back / simplify

The original argument is already the correct normalization: denominator clearing followed by finite-family gcd extraction. The simplifications remove support boilerplate while keeping these mathematical stages visible. Public statement/docstring unchanged mathematically. Same-witness conjunction cannot be split into independent existential properties: an integral scalar multiple and a primitive polynomial obtained independently need not be the same polynomial or share the scalar equation. No >10-line branch remains; body30 satisfies the assigned preferred bound. No further decomposition is needed after real golf.

## Verification gates and completion steps

|Gate|Status / evidence|
|---|---|
|lake_build_file|PASS: `/Users/ramin/.elan/bin/lake build Roth.Separation`, exit0, 1876 jobs; /private/tmp/roth-d25-build.log.|
|definition_protected|PASS: no def/abbrev changes.|
|theorem_statement_protected|PASS: original type accepted by actual target in isolated example; only lambda notation changed.|
|structure_gate|PASS: 30 body lines, not named module headline, no >10-line branch. Same-witness conjunction exception justified above.|
|naming_gate|PASS: mathematical snake_case, no forbidden fragments.|
|line_packing_gate|PASS: full signature table above, maximum body width92.|
|inequality_orientation_gate|PASS: empty order-inequality occurrence table above.|
|complete native LSP|PASS: complete unfiltered response partial=false, success=true, timed_out=false, no failed dependencies: 0 errors / 6 inherited warnings / 0 info / 0 target warnings; raw /private/tmp/roth-d25-lsp-final.json.|
|independent original proof|PASS: /private/tmp/roth-d25-independent.lean uses exact ORIGINAL proof under fresh originalIndependent name; no self/the-target reference in that proof. Exit0 /private/tmp/roth-d25-independent.log.|
|original exact type|PASS: separate isolated example with original public result type applies actual target. Compiled #check confirms original effective binders.|
|actual built axioms|PASS: actual Roth.exists_primitive_smul_eq and direct caller Roth.exists_int_factors use [propext, Classical.choice, Quot.sound]; independent original same. /private/tmp/roth-d25-independent.log.|
|direct callers|Repo-wide `rg` finds only exists_int_factors in same module; actual module build/full LSP covers it, actual axiom check above. No external direct caller.|
|diff hygiene|PASS: git diff --check exit0; 12+/18−, no Git mutation by worker.|

All eleven completion phases, with worker/coordinator boundaries:

1. Doctor: inherited clean baseline and actual d24 profile; initial native full module diagnostics complete.
2. Prepare: contract, source and skills/references read; target before snapshot /private/tmp/roth-d25-before.lean.
3. Audit: all24 items written before any source edit.
4. File fixes: none authorized/needed for this target; user-preserved header untouched.
5. Declaration cleanup: five searches, effective-binder review, all42 golf statuses, live goal/tactic testing and compiled isolated golf.
6. Nonrename refactoring: no new helper needed once body30 achieved; no public type/definition changes.
7. Rename: no forbidden name, nothing queued.
8. Final gates: actual module build, complete native LSP, original exact type plus independent proof, actual axioms and direct caller verification as above.
9. Simplify: step-back review above; no further useful simplification warranting churn.
10. Buzz: exclusive actual repository profile, results appended after process completion below.
11. Report: this dedicated report; source freeze and ownership revocation appended after ALL requests drain. Parent handles cumulative original30/public20/allactual, sequential full and separate LeanEval builds, Git commit/push.

No pending public proposal and no source edits outside the owned declaration. No sorry/axioms/native_decide/limits/profiling scaffold introduced.

## Actual repository profile and freeze

Exclusive command `/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Separation.lean` exited0. Raw /private/tmp/roth-d25-final-profile.log; anchored parsed /private/tmp/roth-d25-final-profile.log.json, parser /private/tmp/roth-separation-profile-table.py. No concurrent Lean/MCP/compiler/profile jobs were active during this final sweep.

|Actual declaration|Baseline command+proof ms|Final command ms|Final outer async proof ms|Final conservative total ms|Anchors command/proof|
|---|---:|---:|---:|---:|---|
|Roth.exists_primitive_smul_eq|20.913+548.436 = 569.349|26.260|637.051|663.311|1/1|
|Roth.exists_int_factors (direct caller)|61.423+556.971 = 618.394|84.313|625.115|709.428|1/1|

Both final actual costs below750ms; no borderline repeat or >=1000ms diagnosis triggered. Timings did not improve in this sweep, and no performance improvement is claimed; the proof is structurally shorter and stays below the required budget. No new helpers exist.

ALL native tool requests, scratch compiler requests, module build, and profile requests have completed/drained. No Git/shared-log mutations performed. Source frozen at SHA256 `3e4987354099a50db25afe7b1cd0c65b72ce37bd406fc4f62493b87ad624eafb` for Roth/Separation.lean. I revoke ALL source ownership and am report-only from this point. No pending proposal/input; parent may perform cumulative audits and exact commit/push before original declaration26.

## Owner cumulative publication gates

Source FROZEN SHA256 `3e4987354099a50db25afe7b1cd0c65b72ce37bd406fc4f62493b87ad624eafb`; leaf ownership revoked and requests drained before owner gates. Owner probe `17212` exit0,40.75s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL26 actual retained standardaxiom checks. `/private/tmp/roth-separation-d25-compatibility.{lean,log,json}`. Owner build session `22435` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,117.51s/28.24s; source hash stable. `/private/tmp/roth-separation-d25-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.
