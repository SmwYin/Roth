# `Roth.degreeOf_none_rename_mul_aeval` — original declaration 20

Fresh dedicated audit, inherited clean pushed HEAD `3bdcd23`; source 551 lines / 23 retained declarations. Public ORIGINAL effective type and documentation, especially `hU`, are protected. Four public options remain PENDING/unapplied: twelve-theorem index-instance removal; deletion of `aeval_X_eq_rename`; deletion of `coeff_uniqueAlgEquiv_symm`; grouped Domain coefficient weakening. No new helper is planned.

Initial audit recorded before any source edit (none made).

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md, together with both skills, cleanup Phase 4 and relevant style/naming/profiling references.

## Full initial 24-item audit

1. LINT: fresh native live goal confirms the original Fintype/DecidableEq/CommRing/IsDomain context; inherited complete module baseline has 0 errors and 31 warnings. Fresh final unfiltered diagnostics required below.
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
13. MATHLIB: native Finder/Loogle/LeanSearch/local-name and full source searches executed; product and rename APIs already used directly. Exact? failed to close the live entry goal; no absence claim from text-only search.
14. JUNK DEF: n/a, theorem.
15. EXISTS LEMMA: n/a, equality theorem, no existential helper.
16. SHOW vs CHANGE: the `show degreeOf none (rename some U) = 0 by ...` is a term argument within `rw`, required to state the auxiliary equality; not a tactic rewriting the main goal.
17. PUSH_NEG: none.
18. GENERALISE: every effective binder to be mechanically tested in isolated compiler probes with autoImplicit=false. Public changes stay pending per owner contract.
19. INEQUALITY: no ordered comparison in full signature, hypotheses or proof body; table below.
20. NORMAL-FORM: degreeOf/natDegree equality is the relevant mathlib coordinate-degree form; zero V is handled because natDegree zero is zero.
21. SYNTAX-GEN: U is inferred from hU, V explicit, matching the consumer. No useful restatement proposed.
22. IMPORT-FANOUT: no import change.
23. CASTS: the statement's `X none : MvPolynomial (Option τ) R` fixes the evaluation codomain; proof's `(none : Option τ)` fixes the constant rename map. No coercion added or dropped.
24. INSTANCE-NAME: n/a, theorem introduces no instance declaration.

## Signature-width table (Unicode codepoints)

| Line | Width | Next token | Arithmetic | Action |
|---|---:|---|---|---|
|197|95|degreeOf (8)|95 + 1 + 8 = 104|ok|
|198|93|V.natDegree (11)|93 + 1 + 11 = 105|ok|
|199|23|end of signature|23 ≤ 100; no next signature token|ok|

## Inequality scan

| Region | ≤ | < | ≥ | > | Action |
|---|---:|---:|---:|---:|---|
| Full effective signature and hypotheses | 0 | 0 | 0 | 0 | none: equality and hU ≠ 0 |
| Proof body | 0 | 0 | 0 | 0 | none: equality split and injectivity only |

Initial action: preserve current direct proof unless a complete, tested replacement improves clarity or cost. No source edit or new helper is justified yet. Compiler probes, complete LSP, module build, independent ORIGINAL proof and actual axioms will be recorded before freeze.

## Mathematical proof and all five actual search methods

For V=0, both sides are zero. For V nonzero, injective renaming and univariate evaluation preserve nonzeroness; degreeOf_mul_eq adds coordinate degrees. U contributes zero degree in none. Injective renaming of the one-variable polynomial identifies the other degree with V.natDegree. The original hU is essential: U=0 and V=X over ℤ give 0≠1, certified separately in the independent probe.

| Method | Actual query | Result and raw evidence |
|---|---|---|
|A Lean-Finder|`degree in a variable of product of multivariate polynomials with disjoint variables`|success: degreeOf_mul_eq, degreeOf_prod_eq, degreeOf_mul_le, degreeOf_mul_X_of_ne; `/private/tmp/roth-separation-d20-finder.json`|
|B Loogle|`MvPolynomial.degreeOf (_ * _)`|success, empty for this pattern only; `/private/tmp/roth-separation-d20-loogle.json`|
|C LeanSearch|`degreeOf none rename some product aeval polynomial natDegree`|success: natDegree_prod, supDegree_eq_natDegree and degree definitions; no direct replacement; `/private/tmp/roth-separation-d20-leansearch.json`|
|D Full source grep|untruncated full candidate name and `degreeOf_rename`, `degreeOf_mul`, degreeOf/aeval/toMvPolynomial patterns|generic degree/product/rename facts found; `/private/tmp/roth-separation-d20-source-search.log`; actual source of Degrees.lean:419 and NoZeroDivisors.lean:43 read|
|E Native name pattern|`degreeOf_mul`|source fallback returned eight multiplication variants; index=unavailable, explicitly not index-certified absence; `/private/tmp/roth-separation-d20-lean_local_search.json`|

Auxiliary variants inspected: degreeOf_prod_eq, degreeOf_mul_X_of_ne, degreeOf_mul_X_pow_of_ne, degreeOf_mul_C_le, degreeOf_rename_of_injective. Common-equivalents table has no custom predicate bucket matching this polynomial identity. Live generic route `exact?` failed; no direct mathlib equivalent found by these tests. No theorem of absence is asserted. The existing theorem combines nonzero-product, missing-variable, and univariate transport facts; retain the direct mathlib-based proof. No new wrapper or predicate is added. The docstring-preservation contract takes precedence over the general search guideline to rewrite module documentation.

## Actual public literature search

Query: `multivariate polynomial degree product disjoint variables integral domain generalization`. First three returned hits: [On zeros of a polynomial in a finite grid](https://arxiv.org/abs/1508.06020), [Androma degree formula](https://androma.org/theorems/13240), and Choe–Oxley–Sokal–Wagner, *Homogeneous Multivariate Polynomials with the Half-Plane Property*. Raw search `/private/tmp/roth-separation-d20-web.json`.

Primary source actually opened and relevant text inspected: [Choe–Oxley–Sokal–Wagner, Lemma 4.7 proof, printed page 23](https://www.math.lsu.edu/~oxley/ycjoasdw.pdf), PDF page 22. The proof uses nonvanishing of the product of leading coefficients in the other-variable polynomial ring to add the degrees in one chosen variable. This supports the coordinate-degree argument over domains. Inference from the formal mathlib API: subtraction and finite variable enumeration are unnecessary; compiler probes below verify precise weaker signatures. The paper is not claimed to state the semiring generalization. Existing local Roth source citation remains intact.

ChatGPT math MCP: unavailable; actual metadata search found no matching connector. No second opinion or outbound message is claimed.

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

Live attempts and all diagnostics are retained in `/private/tmp/roth-separation-d20-lean_multi_attempt.json`; goal/context `/private/tmp/roth-separation-d20-lean_goal.json`. `grind` had a failure diagnostic despite an empty goals array, so it is explicitly failed. No result was accepted from an empty goals array alone.

Additional native final-transport attempts (`exact?`, a simpa-only rename transport, `simp_all`) are preserved in `/private/tmp/roth-separation-d20-final-attempts.json`. Exact? did not close and simp_all left the transport goal. The line-replacement tool also left continuation line 209, producing syntax errors; the simpa candidate had a function-application error from that continuation. These are not successful complete proof replacements, and the simpa result is not claimed to disprove the tactic in an isolated whole-body trial. The existing two-line `.trans` term is retained by the minimum-value filter.

## Step-back review

Reviewed the proof in chunks: lines 200–204 handle V=0 and product nonzeroness; 205–207 prove the missing-variable summand vanishes; 208–209 transport univariate degree. Every retained step changes or closes a goal. No have chain or symmetric branch remains. Whole grind, simp, aesop and exact? were actual native attempts and did not supply a replacement. Term-mode composition would still need the same cases and transport identities. Induction on V adds leading-coefficient and addition cases. Reintroducing a private zero-degree/nonzero wrapper would duplicate deliberately removed helpers and trigger a fresh audit without improving the mathematics. No source change survives the clarity/performance minimum-value filter.

## Verification evidence already completed

Actual `/Users/ramin/.elan/bin/lake build Roth.Separation` exited 0 (1876 jobs), raw `/private/tmp/roth-separation-d20-build.log`. Complete unfiltered native module LSP: 0 errors, 31 warnings, 0 infos, partial=false, timed_out=false, success=true, failed_dependencies=[]; raw `/private/tmp/roth-separation-d20-final-lsp.json`. Target warnings are the preserved unused Fintype/DecidableEq reports (including unused-section warning); warning suppressions were not added.

Isolated `/private/tmp/roth-separation-d20-independent.lean` compiled exit 0, log `.log`: an explicit ORIGINAL effective type assigned to the actual theorem, separate non-self proof `AuditD20.independent_original`, and certified counterexample when hU is removed (U=0, V=X, R=ℤ). Actual built `Roth.degreeOf_none_rename_mul_aeval` and independent theorem each use exactly `[propext, Classical.choice, Quot.sound]`, no sorryAx/custom/native axioms. This target-only probe does not duplicate the owner's whole-original compatibility test.

Actual repository declaration profile reused with dispatch authorization because source/target remain unchanged: `/private/tmp/roth-separation-d18-direct-final-profile.log`. Outer command line 216610 is 17.385 ms, target text at 216612; outer async proof line 219922 is 182.839 ms. Conservative total 200.224 ms, one command and one proof anchor, reconfirmed by `/private/tmp/roth-separation-profile-table.py`; no nested times double-counted. Below both 750 ms repeat and 1000 ms budget. No whole-project speedup claimed; no new final profile required for an unchanged source.

The inequality scan counts ordered comparisons, excluding the `>` character in the two existing `=>` lambda arrows. Neither lambda arrow is an inequality occurrence.

## Generalisation status: every effective binder

Trials use actual isolated Lean compiler invocations with `autoImplicit=false`, retaining the original proof body and replacing only the listed binder (plus `classical` for removed decidability). Scratch sources/logs `/private/tmp/roth-separation-d20-NAME.{lean,log}` and machine-readable completed batch results `/private/tmp/roth-separation-d20-probe-results.json`. Negative results concern the tested mechanical proof, not abstract impossibility. No repository signature changed.

| Binder | Use and applicable weakening/drop probes | Result / disposition |
|---|---|---|
|τ : Type*|index type in U and Option τ; drop τ; universe weakening|drop_tau exit 1 unknown τ; already universe-polymorphic u_1, no forced equality to coefficient universe|
|Fintype τ|unused enumeration; drop; Finite is weaker than Fintype but stronger than no assumption|drop_fintype exit 0; public removal stays PENDING|
|DecidableEq τ|not needed by resulting statement; drop with classical|drop_decidable exit 0; public removal stays PENDING|
|R : Type*|coefficient type in both polynomial types; drop R; universe weakening|drop_R exit 1 unknown R; already independent u_2|
|CommRing R|commutative multiplication underlies MvPolynomial rename/aeval; drop, Ring, CommSemiring|drop_commring exit 1 missing Semiring; ring exit 1 missing CommSemiring; commsemiring exit 0. Dropping commutativity further to noncommutative Semiring/NonAssocRing cannot supply the same CommSemiring-dependent statement; no such restatement applied. Grouped coefficient weakening remains PENDING|
|IsDomain R|used by product-degree formula; drop, NoZeroDivisors|drop_domain exit 1 missing NoZeroDivisors; nozerodivisors exit 0. Nontriviality is not needed separately; grouped coefficient weakening remains PENDING|
|U : MvPolynomial τ R|left operand, inferred via hU; drop U|drop_U exit 1 unknown U; no structure parent keeps the same polynomial expression|
|hU : U ≠ 0|ensures rename some U nonzero; drop hU|drop_hU exit 1 unknown hU; certified U=0/V=X counterexample proves unrestricted version false. No order on polynomial/coefficients provides a nonnegative replacement|
|V : Polynomial R|right operand and RHS natDegree; drop V|drop_V exit 1 unknown V; dependent structure value, not a pointwise/global hypothesis|

No continuity/monotonicity/global-pointwise hypothesis, strict ordered inequality, bundled conjunction, or concrete real/complex type occurs. Inversion check: no named concrete mathematical object disappears after unfolding; this is already a parametric polynomial statement, and the Option renaming encodes the actual disjoint-variable content. No useful new abstract theorem is proposed.

Combined probes completed: `drop_both` (no Fintype/DecidableEq, classical proof) exit 0; `weakest` (also CommSemiring/NoZeroDivisors) exit 0. Complete batch `/private/tmp/roth-separation-d20-probe-results.json` records all 15 completed source/log pairs (including independent proof). These are compiler-verified proposals, not applied changes. No negative binder row is represented as compiler-verified without an actual failing invocation.

## Concrete pending public proposals

Existing twelve-theorem index-instance proposal remains pending: `.mathlib-quality/cleanup/Separation-instance-proposal.md`. Existing `aeval_X_eq_rename` and `coeff_uniqueAlgEquiv_symm` deletion options remain pending in `.mathlib-quality/cleanup/Separation-wrapper-proposal.md`.

The independently compiled full-module grouped Domain coefficient candidate is `/private/tmp/roth-separation-d19-domain-proposal.lean`, log `.log`, exit 0, inherited verified evidence from d19 and inspected here. Its sole production-like edit is `[CommRing R] [IsDomain R]` → `[CommSemiring R] [NoZeroDivisors R]` on the Domain section variables. Both d19 and this d20 then have weaker coefficient assumptions; their original Fintype/DecidableEq binders, hV/hU, docs, and proof bodies remain. Appended scratch #checks print both actual signatures and #print axioms returns only the three standard axioms. This option is independent from index-instance removal. It was communicated to the owner before any application; no application authorized or made.

No additional public proposal, new helper, definition, axiom, import, rename, attribute, or source edit was introduced by this worker.

## Diff gates

| Gate | Result | Concrete evidence |
|---|---|---|
|lake_build_file|pass|actual lake build Roth.Separation exit 0; `/private/tmp/roth-separation-d20-build.log`|
|definition_protected|pass|source diff empty, no def/abbrev/import/header/pin changes|
|theorem_statement_protected|pass|ORIGINAL source doc+signature byte-for-byte equal; explicit ORIGINAL effective public type compiles against actual theorem|
|structure_gate|pass|13 declaration lines, 11 proof lines including := by; zero branch one line, nonzero branch eight lines; no conjunction; not a module headline result|
|naming_gate|pass|mathematical coordinate-degree/rename/product/evaluation identifier; no forbidden abbreviation or numeric pattern|
|line_packing_gate|pass|all three signature lines measured: 95/93/23 codepoints with overflow arithmetic above|
|inequality_orientation_gate|pass|no ordered comparison in effective type/hypotheses/body; => syntax excluded|
|LSP|pass|fresh complete unfiltered native final after all native tactic tests: 0 errors, 31 warnings, 0 infos; no failed dependencies or pending ranges|
|independent proof and actual axioms|pass|explicit original type plus independent non-self proof compiled; actual target/independent axioms exactly three permitted standard axioms|
|profile target|pass|unchanged actual-module anchors, 200.224 ms, below repeat and budget thresholds|
|diff and arithmetic|pass|git diff --check exit 0, source numstat empty, source 551→551 lines / 23→23 retained; declaration 13→13 and proof 11→11; 0 source lines added/deleted|

Overall: pass for target retention. Public proposals remain pending/unapplied. Full-project, separate LeanEval, cumulative original30/public20/all-retained-axiom checks and publication are owner scope, after the freeze below.

## Required Phase-4 checklist

- [✓] Step 1 — required references read.
- [✓] Step 2 — all 24 concrete initial audit items recorded before source edits.
- [✓] Step 2.5 — five actual search methods and generic entry probe recorded.
- [✓] Step 2.6 — every effective binder tested; public literature and pending proposals recorded.
- [✓] Step 2.7 — every signature line has width arithmetic.
- [✓] Step 2.8 — ordered-comparison scan table covers signature, hypotheses and proof.
- [✓] Step 3 — all 42 golf rules have concrete statuses.
- [✓] Step 4 — chunk review, automation, transport and alternate strategy review recorded.
- [✓] Step 5a — complete native unfiltered final LSP, 0 errors / 31 inherited warnings.
- [✓] Step 5b — all target diff gates and actual module build pass.
- [✓] Step 6a — no rename; no sidecar mutation required.

## Eleven completion steps and freeze

1. Doctor: inherited clean pushed HEAD `3bdcd23`, unchanged actual target baseline; fresh native complete module diagnostics reconfirmed baseline warnings.
2. Prepare: both skills, cleanup Phase 4, full golf/proof-pattern references and relevant search/generalisation/gates/style/naming/profiling references read; source and ORIGINAL public contract located.
3. Initial audit: all 24 items written before source edits; none were needed.
4. File-level fixes: none within owned scope; original metadata, docs and all four public options preserved.
5. Golf: all 42 statuses, live entry and final-transport attempts, and chunk review completed; retained direct proof by the minimum-value filter.
6. Refactor: no wrapper, helper, rename, attribute or public type change applied; all compiled public proposals remain pending.
7. Module gate: actual lake build Roth.Separation exit 0; git diff --check exit 0; source diff empty.
8. LSP: complete unfiltered final native response after tactic tests, 0 errors / 31 warnings / 0 infos, no pending range, timeout or failed dependency; raw `/private/tmp/roth-separation-d20-final-lsp.json`.
9. Contract/independence/axioms: actual ORIGINAL effective public type assignment and independent non-self proof compile; actual built target and independent theorem use exactly the permitted standard axioms. All nine effective binders tested, with successful combined weakest candidate and hU counterexample certified. No owner's whole-original probe duplicated.
10. Simplify/buzz: no clearer complete replacement found; unchanged actual-module command+outer-proof cost 200.224 ms, no limit or profiler scaffold added. Existing grouped full-module coefficient candidate inspected and retained pending.
11. Report/freeze: only this dedicated report written in repository; source 551→551 lines, retained 23→23, target declaration 13→13 lines / proof 11→11 lines. ALL source ownership revoked; report-only. ALL Lean/MCP/compiler/profile requests drained, including native final-attempt/final-diagnostic requests and completed 15-probe compiler batch. Owner handles sequential full project, separate LeanEval, cumulative original30/public20/all-actual-axiom probes, exact-path commit and successful push before next declaration.

Frozen source SHA256: `1c58b8b35fe3c01d326d802b94c54dbc8ed0349e1ca388f87e9b34aa2a0278d4`.

## Owner cumulative publication gates

Source FROZEN SHA256 `1c58b8b35fe3c01d326d802b94c54dbc8ed0349e1ca388f87e9b34aa2a0278d4`; leaf ownership revoked and requests drained before owner gates. Owner probe `76196` exit0,34.50s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL23 actual retained standardaxiom checks. `/private/tmp/roth-separation-d20-compatibility.{lean,log,json}`. Owner build session `12121` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,5.58s/2.79s; source hash stable. `/private/tmp/roth-separation-d20-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.
