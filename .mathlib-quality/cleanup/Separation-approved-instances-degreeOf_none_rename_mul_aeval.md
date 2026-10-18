# Approved instance removal: `Roth.degreeOf_none_rename_mul_aeval`

Fresh audit on clean pushed HEAD dfd0961, source 582 lines. Own only this theorem and this report. Both Fintype τ and DecidableEq τ removals are approved. Preserve CommRing R / IsDomain R, Nat codomain, both wrappers and exact docs.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md, both skills and relevant style/naming/profiling references.

Initial audit written BEFORE source edits.

## Full initial 24-item audit

1. LINT: fresh native live goal confirms the original Fintype/DecidableEq/CommRing/IsDomain context; fresh complete native module baseline has 0 errors and 15 warnings. Fresh final unfiltered diagnostics required below.
2. HAVE SCAN: no `have` declarations in the target. One typed term-mode `show` proves the zero coordinate degree inside the rewrite list; single-use and directly local.
3. SET_OPTION: none; no limit or profiler scaffolding in source.
4. SIMP SQUEEZE: `simp [hV]` closes the zero branch. Inner `simp [degreeOf, degrees_rename_of_injective ...]` closes its typed subgoal; both terminal and appropriately unsqueezed.
5. NAMING: `degreeOf_none_rename_mul_aeval` describes the coordinate degree of a renamed/evaluated product; uses established mathlib identifier spelling, no forbidden abbreviation or numeric scheme. No rename needed.
6. LINE PACKING: all three signature lines measured below; source statement unchanged.
7. BY PLACEMENT: `:= by` ends the conclusion line; nested `show ... by` is term mode.
8. FORMAT: two-space proof indentation; one tactic per line; existing multiline rw list; no blank line inside body; no haveI/letI.
9. COMMENTS: no inline comments in target; all existing source documentation preserved.
10. DOCSTRING: existing public doc gives the disjoint-variable degree meaning and source §2 citation; preserve exact text.
11. VISIBILITY: public theorem used by exists_det_eq_mul; preserve public API.
12. STRUCTURE: short equality proof with one zero case and one nonzero case; no conjunction, extraction unnecessary.
13. MATHLIB: fresh native Finder/Loogle/LeanSearch/local-name and full source searches executed; product and rename APIs already used directly. Fresh exact? probe is scheduled; no absence claim from text-only search.
14. JUNK DEF: n/a, theorem.
15. EXISTS LEMMA: n/a, equality theorem, no existential helper.
16. SHOW vs CHANGE: the `show degreeOf none (rename some U) = 0 by ...` is a term argument within `rw`, required to state the auxiliary equality; not a tactic rewriting the main goal.
17. PUSH_NEG: none.
18. GENERALISE: every effective binder to be mechanically tested in isolated compiler probes with autoImplicit=false. Both index-instance removals are explicitly approved; coefficient widening is explicitly declined.
19. INEQUALITY: no ordered comparison in full signature, hypotheses or proof body; table below.
20. NORMAL-FORM: degreeOf/natDegree equality is the relevant mathlib coordinate-degree form; zero V is handled because natDegree zero is zero.
21. SYNTAX-GEN: U is inferred from hU, V explicit, matching the consumer. No useful restatement proposed.
22. IMPORT-FANOUT: no import change.
23. CASTS: the statement's `X none : MvPolynomial (Option τ) R` fixes the evaluation codomain; proof's `(none : Option τ)` fixes the constant rename map. No coercion added or dropped.
24. INSTANCE-NAME: n/a, theorem introduces no instance declaration.

## Signature-width table (Unicode codepoints)

| Line | Width | Next token | Arithmetic | Action |
|---|---:|---|---|---|
|206|95|degreeOf (8)|95 + 1 + 8 = 104|ok|
|207|93|V.natDegree (11)|93 + 1 + 11 = 105|ok|
|208|23|end of signature|23 ≤ 100; no next signature token|ok|

## Inequality scan

| Region | ≤ | < | ≥ | > | Action |
|---|---:|---:|---:|---:|---|
| Full effective signature and hypotheses | 0 | 0 | 0 | 0 | none: equality and hU ≠ 0 |
| Proof body | 0 | 0 | 0 | 0 | none: equality split and injectivity only |

Initial action: preserve current direct proof unless a complete, tested replacement improves clarity or cost. Approved edit planned: scoped omit before the existing docstring, with local classical if needed. No helper planned. Compiler probes, complete LSP, module build, independent ORIGINAL proof and actual axioms will be recorded before freeze.

## Five actual fresh mathlib searches

|Method|Query|Result / raw file|
|---|---|---|
|A Finder|degree in a variable of product of multivariate polynomials with disjoint variables|degreeOf_mul_eq, degreeOf_prod_eq and bounds; `/private/tmp/roth-separation-r08-finder.json`|
|B Loogle|MvPolynomial.degreeOf (_ * _)|success, empty for this pattern; `/private/tmp/roth-separation-r08-loogle.json`|
|C LeanSearch|degreeOf none rename some product aeval polynomial natDegree|natDegree and supDegree APIs; `/private/tmp/roth-separation-r08-search.json`|
|D source|full target name and degreeOf_rename/degreeOf_mul throughout MvPolynomial|generic APIs; untruncated `/private/tmp/roth-separation-r08-source-search.log`; Degrees.lean:419 and NoZeroDivisors.lean:43 source read|
|E name pattern|degreeOf_mul|eight source results, index unavailable; `/private/tmp/roth-separation-r08-local.json`; not index-certified absence|

Exact? live generic probe failed. Auxiliary mul_X, mul_X_pow, mul_C and prod variants do not express this complete identity. No absence theorem claimed. Common-equivalents table contains no matching custom-predicate replacement. Existing proof uses mathlib APIs directly; no new wrapper or predicate. Exact public wrapper names are explicitly preserved by user instruction.

## Fresh public literature search

Actual query: `multivariate polynomial degree product disjoint variables integral domain Choe Oxley Sokal Wagner Lemma 4.7`. First three hits: [Choe–Oxley–Sokal–Wagner primary PDF](https://www.math.lsu.edu/~oxley/ycjoasdw.pdf), [same paper mirror](https://citeseerx.ist.psu.edu/document?doi=355f7014c19df59cbab14ed2407625ce06d343a9&repid=rep1&type=pdf), [CGAL polynomial manual](https://doc.cgal.org/4.7/Polynomial/index.html). Primary PDF opened and Lemma 4.7 inspected: coordinate degrees add by nonvanishing of the product of leading coefficients in the polynomial ring on the other variables. This explains the domain hypothesis and disjoint-variable argument. Inference: finite enumeration of the index type is unnecessary because each polynomial has finite support; the exact arbitrary-τ Lean type is verified separately. The paper is not claimed to prove a semiring widening. ChatGPT math MCP unavailable in actual tool inventory; no second opinion claimed. Coefficient widening was declined and stays unapplied.

## All 42 golf rules

| Rule | Concrete status |
|---|---|
|1.1 by exact|n/a: no no-op tactic wrapper|
|1.2 by rfl|n/a: no reflexivity-only proof|
|1.3 rw + exact → rwa|reviewed: rw transforms product and missing-variable degrees, then exact composes injective renaming and unique-variable degree; putting both transport facts into rwa would obscure rather than simplify the same argument; retain|
|1.4 simp + exact|n/a: both simp calls close their own subgoal; no following exact in that subgoal|
|1.5 trailing rfl|n/a: absent|
|1.6 anonymous constructor|n/a: no constructor or conjunction|
|1.7 apply + exact|n/a: no apply|
|1.8 by_contra!|n/a: direct zero split, no contradiction chain|
|1.9 eta reduction|constant Unit lambda cannot eta-reduce; `(fun _ _ _ => rfl)` proves injectivity from subsingleton equality, no f x lambda|
|1.10 inline have|n/a: zero haves; single-use zero-degree equality already inline|
|1.11 refine fun|n/a: no apply/intro pair|
|1.12 remove show|typed term show is a rw argument specifying a new auxiliary equality; dropping it loses that equality's expected type, not a redundant tactic show|
|1.13 obtain projections|n/a: no repeated pair projections; `.2 hV` directly applies an iff|
|1.14 merge rw|already one combined rewrite list|
|1.15 terminal simp unsqueezed|already satisfied: both simp calls terminal|
|1.16 nonterminal simp squeeze|n/a: no nonterminal simp|
|1.17 dot notation|already `.not.mpr`, `.2`, `.trans`; no verbose composition to replace|
|1.18 <| syntax|n/a: nested parentheses delimit rewrite terms and the head of `.trans`, not a trailing application to by/fun|
|1.19 push Not|n/a: no push_neg|
|1.20 inline existential helper|n/a: none|
|2.1 whole grind|actual native live attempt failed to derive the polynomial degree identity|
|2.2 delete before grind|n/a: no retained grind|
|2.3 simpa consolidation|whole simp made no progress; existing degree transport is explicitly chained, no simp/exact redundancy|
|2.4 fun_prop|n/a: no continuity/differentiability/measurability property|
|2.5 positivity|n/a: goal is symbolic degree equality, not positivity|
|2.6 gcongr|n/a: no monotonicity inequality|
|2.7 lia/omega|n/a: no arithmetic relations imply the missing polynomial identity|
|2.8 aesop|actual native live attempt failed after exhaustive search; continuation errors are retained raw and are not successful replacement evidence|
|2.9 norm_num/norm_cast|n/a: arbitrary symbolic polynomials, no numeric calculation or cast target|
|2.10 decide/kernel|n/a: not a closed decidable finite computation|
|2.11 field_simp; ring|n/a: no division or ring-expression equality|
|2.12 linear_combination|n/a: no ending ring/ring_nf, equality is of degrees|
|2.13 wlog|n/a: zero and nonzero V cases are mathematically asymmetric|
|2.14 calc composition|already final `.trans` composes two equalities; no calc block|
|2.15 close uniform goals|n/a: branches need different facts; zero branch simp and nonzero degree formula|
|3.1 erw → rw|n/a: only rw present|
|3.2 legacy analysis tactics|n/a: none|
|3.3 omega → lia|n/a: no arithmetic automation|
|3.4 rcases rfl|n/a: no rcases|
|3.5 automation attributes|none added: specialized public rule, existing normal forms suffice; attribute change has no demonstrated consumer need|
|3.6 simp_all|actually tested at final transport goal: left the symbolic renamed-polynomial degree goal; no simp_all only to unsqueeze|
|3.7 remove heartbeat limits|n/a: no source limits|

Fresh native live entry attempts at line 209 (before edit) were grind, simp, aesop, exact?. Grind failed with an error despite an empty goals list; simp made no progress; aesop exhausted search; exact? could not close. Continuation-line errors are not success. Fresh native final-transport attempts after the edit are saved in `/private/tmp/roth-separation-r08-final-attempts.json`; exact? failed and simp/simp_all retained symbolic renamed-polynomial degree goals. The line-replacement API also left the original continuation, so its syntax error is not evidence against an isolated complete alternative. The original direct proof is retained.

## Step-back review

Zero V closes by simp. Nonzero V uses product-degree additivity, absence of none from the renamed U variables, and univariate degree transport. These are distinct mathematical steps, with no haves to inline. Final trans already composes the two transport facts. Induction on V introduces addition/leading-coefficient cases; a new wrapper repeats existing mathlib APIs. Whole automation failed in fresh live attempts. No shorter complete proof with a clarity/performance benefit was found. Minimal approved edit only; no helper added.

## Every effective binder: fresh mechanical probes

All probes set `autoImplicit false` and use the independently named theorem with the same direct mathlib proof, plus local classical. Scratch sources/logs are `/private/tmp/roth-separation-r08-NAME.{lean,log}`. The completed exit table will be recorded below; negative results concern these mechanical proof/signature tests, not mathematical impossibility.

|Binder|Use / candidates|Disposition|
|---|---|---|
|τ : Type*|index of U and Option τ; drop_tau; universes already polymorphic|cannot drop the type appearing in the statement|
|Fintype τ|no enumeration used; drop_fintype and drop_both|approved omission applied; no Finite assumption needed|
|DecidableEq τ|only proof decidability; drop_decidable and drop_both|approved omission applied with local classical|
|R : Type*|coefficient type; drop_R; already independent universe|cannot drop the type appearing in the statement|
|CommRing R|commutative coefficient operations; drop_commring, ring, commsemiring|coefficient widening explicitly declined; preserve CommRing|
|IsDomain R|nonzero-product degree formula; drop_domain, nozerodivisors|coefficient widening explicitly declined; preserve IsDomain|
|U : MvPolynomial τ R|left operand inferred from hU; drop_U|value/type required by the expression|
|hU : U ≠ 0|rename U nonzero; drop_hU; certified U=0,V=X counterexample|essential; no order structure gives a nonnegative substitute|
|V : Polynomial R|right operand and natDegree; drop_V|value/type required by the expression|

No global continuity/monotonicity premise, strict ordered inequality, bundled bijection, or concrete real/complex type occurs. Inversion check: no special named concrete witness unfolds away; this is already a parametric polynomial identity. Naturals are the canonical degree codomain and explicitly preserved. Both public wrapper names retained. No new helper, attribute, instance, import or pending public proposal.

## Native tooling and fallback

Native tool metadata and complete relevant schemas were discovered from ALL_TOOLS before native queries. Native searches, live tactic attempts and complete module diagnostics work. Two actual native run_code attempts to import the rebuilt Roth.Separation reported “Imports are out of date”; raw `/private/tmp/roth-separation-r08-native-check.json` and `...-native-check-retry.json`. Those attempts were bounded and drained; no success is claimed. Explicit isolated compiler contract/binder probes supply the honest fallback. No direct fallback MCP session was needed.

## Completed probe exits

|Probe|Exit|Meaning|
|---|---:|---|
|independent|0|same proof compiles|
|drop_tau|1|mechanical deletion/weakening does not compile|
|drop_R|1|mechanical deletion/weakening does not compile|
|drop_commring|1|mechanical deletion/weakening does not compile|
|ring|1|mechanical deletion/weakening does not compile|
|commsemiring|0|same proof compiles|
|drop_domain|1|mechanical deletion/weakening does not compile|
|nozerodivisors|0|same proof compiles|
|drop_U|1|mechanical deletion/weakening does not compile|
|drop_hU|1|mechanical deletion/weakening does not compile|
|drop_V|1|mechanical deletion/weakening does not compile|
|drop_fintype|0|same proof compiles|
|drop_decidable|0|same proof compiles|
|drop_both|0|same proof compiles|
|contract|1|first contract: all type assignments/axiom checks passed, but scratch hU counterexample needed explicit Polynomial ℤ ascription; repaired final contract recorded below|

All 15 batch requests completed; machine-readable `/private/tmp/roth-separation-r08-probe-results.json`. Successful coefficient probes are recorded only; the user declined their application. Drop_hU mechanically leaves an unknown hU, independently strengthened by the certified counterexample in the final contract.

## Final signature packing / inequality tables

|Line|Codepoints|Next token|Arithmetic|Action|
|---|---:|---|---|---|
|207|95|degreeOf|95+1+8=104>100|ok|
|208|93|V.natDegree|93+1+11=105>100|ok|
|209|23|end|23≤100; no next signature token|ok|

|Region|≤|<|≥|>|Action|
|---|---:|---:|---:|---:|---|
|Effective signature + hypotheses|0|0|0|0|none|
|Proof body|0|0|0|0|none; the two => lambda arrows are syntax|

The width reference is actual #check at `format.width 100` in the final contract log, with independently polymorphic τ and R and no index instances. Explicit original and new type assignments verify both interfaces. All theorem signature text and original docs remain byte-identical; only effective instance inclusion changes.

## Verification gates

Actual `/Users/ramin/.elan/bin/lake build Roth.Separation` exit 0, 1876 jobs; `/private/tmp/roth-separation-r08-build.log`. Complete unfiltered final native LSP after all live tactic trials: success=true, partial=false, timed_out=false, failed_dependencies=[], 0 errors / 12 warnings / 0 infos; raw `/private/tmp/roth-separation-r08-final-lsp.json`. The three target warnings were removed; remaining warnings belong to other declarations and preserved header metadata. No suppressions.

No external direct caller exists: untruncated `rg` over Roth finds this theorem and its application inside `Roth.exists_det_eq_mul` only. That same-file caller is covered by module build, full-file LSP and its actual built axiom check. No caller source edit.

|Gate|Result|Evidence|
|---|---|---|
|lake_build_file|pass|actual module build exit 0|
|definition_protected|pass|no def/abbrev/import/header/pin edits|
|theorem_statement_protected|pass, approved generalization|exact declaration text/doc unchanged; scoped omit removes exactly approved index instances|
|structure_gate|pass|declaration 13→14 lines; proof including := by 11→12; nonzero branch 8 lines; no conjunction/headline theorem|
|naming_gate|pass|coordinate degree/none/rename/product/evaluation name; no forbidden abbreviation/pattern|
|line_packing_gate|pass|all three measured signature rows, 95/93/23 codepoints|
|inequality_orientation_gate|pass|zero ordered comparisons; lambda arrows excluded|
|LSP|pass|complete native 0E/12W/0I|
|independence/axioms|pass|non-self new and original proofs, original/new types; actual target/caller axioms exactly propext, Classical.choice, Quot.sound|
|diff arithmetic|pass|git diff --check exit 0; 2 added/0 removed source lines; 582→584 lines; 25→25 retained declarations|

Actual source SHA256 remains `49790c37e35777ce2c4668975e173e5e7c7ae5af353ba151d800df0472892f74`. Performance and final freeze follow after the final isolated profile. No pending proposal is created; declined coefficient widening is only documented. All original docs and both wrapper names are preserved.

## Required Phase-4 checklist

- [✓] Step 1: both skills and required full golf/proof/search/generalization/gates references read; relevant style/naming/profiling and cleanup requirements read.
- [✓] Step 2: all 24 initial audit items written before source edits.
- [✓] Step 2.5: five actual native/source search methods, auxiliary variants and generic exact? probe.
- [✓] Step 2.6: every effective binder, fresh successful and failed compiler probes, public literature, approved and declined decisions.
- [✓] Step 2.7: measured per-signature-line tables before and after.
- [✓] Step 2.8: complete ordered-comparison scan; no comparisons.
- [✓] Step 3: all 42 golf rules have concrete status.
- [✓] Step 4: chunk review, whole automation, term composition and alternate strategy review.
- [✓] Step 5a: complete unfiltered native LSP, 0 errors / 12 warnings.
- [✓] Step 5b: actual module build, contract/independent/axiom checks, all focused diff gates.
- [✓] Step 6a: no rename, helper or shared sidecar needed.

## Eleven completion steps

1. Doctor: clean pushed HEAD dfd0961; baseline full project gates inherited from owner; fresh native full module LSP 0E/15W.
2. Prepare: required skills/reference reading, ORIGINAL contract, direct caller and baseline actual profile located.
3. Audit: complete initial 24-item artifact saved before the two-line source edit.
4. File-level fixes: only owned target; preserve all metadata/docs/imports/pins.
5. Golf: all 42 statuses, live entry/final attempts and step-back review; direct proof retained.
6. Refactor: approved removal of both index instances only, scoped omit + local classical; no helpers/renames/attributes/wrapper removals/coefficient widening.
7. Module gate: actual lake build Roth.Separation exit 0; whitespace/diff gates pass.
8. LSP: final native unfiltered response after all live attempts, 0E/12W/0I, no partial/timeout/failed deps.
9. Contracts/axioms: independently compiled new and original proofs, exact new type and original adapter, hU counterexample; actual built target and same-file caller use only the three standard axioms.
10. Simplify/buzz: complete replacements tested, no clarity benefit from extra restructuring; actual anchored isolated module profiling below, no limits/scaffolding.
11. Report/freeze: final completion after timing, request drain and hash confirmation below. Owner retains cumulative original/public/all-retained checks, sequential full build + separate LeanEval, exact-path commit and successful push before next edit.

## Exact ORIGINAL contract and final isolated timing setup

The final compiler invocation `/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-separation-r08-contract.lean` exited 0; raw `/private/tmp/roth-separation-r08-contract-final.log`. It includes the explicit complete ORIGINAL forall binder order `{τ} [Fintype τ] [DecidableEq τ] {R} [CommRing R] [IsDomain R] {U}`, recovered by a lambda adapter from the new theorem, as well as the arbitrary-τ type, separate non-self proofs under NEW and ORIGINAL assumptions, and certified hU counterexample. Both independent proofs and actual built target/caller use exactly `[propext, Classical.choice, Quot.sound]`. No self-use appears in either independent proof body. This focused contract is separate from the owner's cumulative whole-original probe. The first contract failure was a missing scratch-only Polynomial ℤ ascription in the counterexample; source was unaffected, and the complete repaired file passed.

First isolated repository profile exited 0: `/private/tmp/roth-separation-r08-profile.log`. Target conservative cost 194.041 ms = outer command 25.271 + outer async proof 168.770. The scoped omit command yields two command anchors; max outer command + outer proof conservatively avoids double-counting nested traces. The inherited baseline `/private/tmp/roth-separation-r07-profile.log(.json)` measured this target at 154.331 ms = 17.606 + 136.725. These are local noisy timings, not a whole-project speedup claim.

Raw first profile contains three malformed UTF-8 replacement positions in nested Lean trace output. Original bytes are preserved. The supplied parser failed strict decoding; a dedicated temporary parser `/private/tmp/roth-separation-r08-profile-table.py` differs only by reading with `errors='replace'`. All declaration name/outer timing anchors are preserved; its table is `/private/tmp/roth-separation-r08-profile.log.json`. The first table has two inherited borderline declarations, `eq_sum_aeval_basis_coeffNone_aux` 770.520 ms and `exists_separated_representation` 824.040 ms; final isolated sweep repeats both after the final explicit adapter compiler has drained. No source changes were made. Final sweep `/private/tmp/roth-separation-r08-profile-final.log` started only after all native MCP, binder batch, module build and final contract requests completed, with owner compiler/MCP idle.

## Final actual repository profile and freeze

Final isolated command `/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Separation.lean` exited 0 (session 27038), after all other requests drained and with owner compiler/MCP idle. Raw `/private/tmp/roth-separation-r08-profile-final.log`, table `...log.json`. Final raw output has zero malformed UTF-8 positions; both the replacement-tolerant temporary parser and the original supplied `/private/tmp/roth-separation-profile-table.py` successfully parse it identically. All 25 retained declaration command anchors and all 24 theorem async-proof anchors are present. `coeffNone` is a definition and correctly has no async theorem-proof anchor.

|Actual declaration|First sweep ms|Final sweep ms|Final command + proof ms|Anchor lines|
|---|---:|---:|---|---|
|degreeOf_none_rename_mul_aeval|194.041|166.317|23.747 + 142.570|outer command 225752; outer proof 225790|
|eq_sum_aeval_basis_coeffNone_aux|770.520|699.921|102.939 + 596.982|outer command 323422; outer proof 323659|
|exists_separated_representation|824.040|814.956|30.910 + 784.046|outer command 405078; outer proof 414604|
|exists_int_factors|679.320|754.519|83.388 + 671.131|both actual module tables|
|exists_det_eq_mul (only direct caller)|table preserved|488.675|95.480 + 393.195|outer command 965994; outer proof 987357|

Two actual isolated sweeps on identical source give repeated measurements, including the 750 ms borderline declarations. No declaration reaches 1000 ms in either r08 sweep; no performance fix or limit raise is needed. The target stays below both thresholds. Conservative command + outer async proof uses maxima of nested-command wrapper anchors and does not add nested tactic/Meta nodes. No claimed whole-project speedup.

Final arithmetic: source 582→584 lines, 25→25 retained declarations, target declaration 13→14 lines (proof 11→12 including := by), +2/−0 source diff. The extra scoped omit lies before the original docstring, and local classical is the only body addition. An exact byte comparison against HEAD reconstructed with those two insertions passed, proving all other bytes unchanged. `git diff --check` passed. Both public wrappers, CommRing/IsDomain assumptions, hU and Nat codomain remain intact. No helper, name, attribute, import, pin, source comment or shared report was changed.

ALL Lean/MCP/compiler/profile requests are drained: all native search/goal/tactic/run-code/diagnostics requests completed; binder batch session 50677, module build session 1279, repaired contract sessions 95742/46940, first profile 73125 and final profile 27038 all completed. No failed/partial request is represented as a passing gate. No further compiler job is pending. No public proposal remains for this target: approved index removal applied; declined coefficient widening and declined wrapper changes remain unapplied.

ALL source ownership is explicitly REVOKED. Source is FROZEN; report-only from this point. Final frozen source SHA256:

`49790c37e35777ce2c4668975e173e5e7c7ae5af353ba151d800df0472892f74`

Owner must complete cumulative ORIGINAL/public/all-actual checks, sequential full project and separate LeanEval builds, exact-path commit and successful push before the next declaration edit. This worker made no Git mutations.

## Owner cumulative publication gates

Source FROZEN SHA256 `49790c37e35777ce2c4668975e173e5e7c7ae5af353ba151d800df0472892f74`; leaf ownership revoked and requests drained before owner gates. Owner probe `60715` exit0,39.76s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL25 actual retained standardaxiom checks. `/private/tmp/roth-separation-r08-compatibility.{lean,log,json}`. Owner build session `5802` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,118.81s/28.04s; source hash stable. `/private/tmp/roth-separation-r08-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.
