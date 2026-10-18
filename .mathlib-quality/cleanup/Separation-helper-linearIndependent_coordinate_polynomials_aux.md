# Independent helper audit: linearIndependent_coordinate_polynomials_aux

Initial audit recorded before source edits. Snapshot: /private/tmp/roth-separation-d21-source-freeze.lean; exact helper snapshot: /private/tmp/roth-d21-linearIndependent_coordinate_polynomials_aux.lean.txt. Scope is only this private helper and strictly necessary private caller substitutions. No public edits authorized. Public instance menu handling belongs to parent. During this audit user approved menu 12; application is deferred until this private-helper batch completes.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md.

| Audit | Initial finding/action |
|---|---|
|1 LINT|Complete native initial LSP collected; no warnings in helper; inherited warnings outside scope.|
|2 HAVE SCAN|hcoeff: coefficient extraction; h1: congrArg hg, single-use but keeps coefficient normalization readable; hf: extensionality on spanning generators. Test simplification and direct automation.|
|3 SET_OPTION|None in target; none to add.|
|4 SIMP SQUEEZE|h1 nonterminal simp only correctly squeezed; two terminal simpa only lists to test unsqueezed.|
|5 NAMING|Describes linear independence of coordinate polynomials; private _aux; no forbidden abbreviation/pattern.|
|6 LINE PACKING|Measure all five signature lines before deciding packing.|
|7 BY PLACEMENT|by ends signature line.|
|8 FORMAT|Two-space tactic indentation, no blank proof lines or semicolon chains; no haveI/letI.|
|9 COMMENTS|No target inline comments to preserve.|
|10 DOCSTRING|Private helper has no docstring, as required.|
|11 VISIBILITY|Private helper used once by exists_separated_representation; correct.|
|12 STRUCTURE|23 proof-body lines, no conjunction or >10-line case branches; helper has actual multi-step content.|
|13 MATHLIB|All five methods actually called; candidates are building blocks, not replacements; exact?/apply? heartbeat out, not evidence of absence.|
|14 JUNK DEF|n/a: lemma, no definition.|
|15 EXISTS LEMMA|n/a: conclusion LinearIndependent, not trivial existential.|
|16 SHOW/CHANGE|Neither occurs.|
|17 PUSH_NEG|None.|
|18 GENERALISE|Already R/M-parametric; probe Ring and CommSemiring and every effective binder; no ambient τ/K instances occur in goal.|
|19 INEQUALITY|No relation inequalities; table required below.|
|20 NORMAL-FORM|LinearIndependent is canonical; monomial coefficients in C_mul_X_pow form.|
|21 SYNTAX-GEN|Spanning-family basis packages membership naturally; existing caller supplies v,b directly.|
|22 IMPORT-FANOUT|No new imports needed.|
|23 CASTS|Fin→Nat power coercion required; Polynomial R type annotation directs congrArg.|
|24 INSTANCE-NAME|No instance declarations.|

Issues: attempt terminal simplification; measure signature packing; probe safe private assumptions. No helper additions planned. Literature search exempt because this is a private implementation helper with no public mathematical claim.

## Search status (actual calls)

A Lean-Finder query `linear independence coordinate polynomials of spanning vectors in a basis` returned Basis.mk_coord_apply/ne/eq, Basis.linearIndependent, and ofVectorSpaceIndex.linearIndependent. These describe basis coordinates/independence, not the transposed polynomial family.
B Loogle query `LinearIndependent _ (fun _ => ∑ _, Polynomial.C _ * Polynomial.X ^ _)` returned no items successfully.
C LeanSearch query `coordinate polynomials spanning family basis linearly independent` returned Polynomial.Sequence.linearIndependent, Basis.mk.congr_simp, MvPolynomial.linearIndependent_X, Polynomial.coe_basisMonomials, and basisOfPiSpaceOfLinearIndependent.congr_simp. The sequence result requires distinct degrees/domain and does not apply to this arbitrary coordinate family.
D Actual untruncated source `rg` over mathlib for `linearIndependent.*(coeff|transpose)|linearIndependent_coordinate_polynomials_aux` found only a matrix transpose rewrite and a minpoly coefficient use; a targeted source search inspected Fintype.linearIndependent_iff and its semiring variant. No direct replacement located.
E Native local search `linearIndependent` returned source declarations including Fintype.linearIndependent_iff and Basis.linearIndependent; index unavailable, so absence is NOT asserted. Source search is the fallback.

Live whole-proof automation probes: grind failed; aesop made no progress; exact? and apply? each exhausted the default 200000 heartbeats (not raised). Raw: /private/tmp/roth-d21-helper1-attempts.json. These results establish no automatic replacement found, not mathematical absence. No new helper created.

## Generalisation and every effective binder

| Binder | Actual drop/weakening evidence | Decision |
|---|---|---|
|R : Type*|drop gives Unknown identifier R, autoImplicit false|required coefficient ring type|
|M : Type*|drop gives Unknown identifier M|required module type|
|CommRing R|drop fails Semiring R inference; Ring fails HSMul on dual linear maps; CommSemiring fails ring linearIndependent rewrite|retain; failed unchanged-proof probes do not disprove a redesigned semiring theorem|
|AddCommMonoid M|drop fails AddCommMonoid M inference|retain minimal additive structure used by Module/Basis|
|Module R M|drop fails Module R M inference|retain|
|n : Nat|drop gives Unknown identifier n|required finite polynomial exponent range|
|l : Nat|drop gives Unknown identifier l|required basis index|
|v|drop gives Unknown identifier v|required spanning generators|
|b|drop gives Unknown identifier b.repr|required coordinate basis|

Raw compiled drop suite: /private/tmp/roth-d21-helper1-drops.lean and .log, exit1 as expected; no negative test is claimed successful. Ring/semiring logs: /private/tmp/roth-d21-helper1-ring.log and /private/tmp/roth-d21-helper1-semiring.log (both exit1). K, Field K, τ, Fintype τ, DecidableEq τ are absent from actual effective goal returned by native lean_goal at line224; private omit already removes ambient index instances. No public binder changed.

Pointwise/global and strict/weak: n/a, no continuity/global predicates or strict hypotheses. Concrete→abstract: R/M already abstract, Type* universe polymorphic. Inversion check: no concrete named object in contract; v and b remain used throughout. General finite exponent embeddings would be a redesigned statement with explicit injectivity, no practical benefit for the sole Fin caller; not proposed.

## Signature packing (Unicode codepoints)

The next unit is a complete syntactic binder or expression group, rather than an identifier fragment.

| Line | Current | Next unit width | Arithmetic | Action |
|---|---:|---:|---|---|
|218 declaration + R/M + CommRing|85|16 `[AddCommMonoid M]`|85+1+16=102|ok|
|219 remaining instances,n/l,v|66|63 complete b binder including colon|66+1+63=130|ok|
|220 b binder and colon|67|47 conclusion prefix through sum binder|67+1+47=115|ok|
|221 conclusion sum|51|93 full C_mul_X_pow summand through := by|51+1+93=145|ok|
|222 final summand and := by|99|n/a end of signature|99≤100|ok|

## Inequality scan

| Region | Occurrences | Action |
|---|---:|---|
|signature and hypotheses|0 inequalities (`≥`, `>`, `<`, `≤`)|none|
|proof|0 order relation inequalities; `→` is function syntax|none|
|name|0 `_ge_`/`_gt_`|no rename|

## All 42 golf rules

| Rule | Concrete outcome |
|---|---|
|1.1|n/a, no by exact wrapper|
|1.2|n/a, no by rfl|
|1.3|n/a, rw followed by refine rather than exact|
|1.4|Terminal simpa already present; shortening trial rejected on measured performance|
|1.5|n/a, no trailing rfl after simp|
|1.6|n/a, no constructor proof|
|1.7|n/a, no apply/exact chain|
|1.8|n/a, no contradiction/push_neg|
|1.9|lambdas use their arguments in polynomial coefficients/extensionality; no eta wrapper|
|1.10|h1 single-use retained: bare inlining would duplicate multiline coefficient normalization; hcoeff/hf retain named mathematical stages|
|1.11|n/a, no apply followed by intro|
|1.12|n/a, no show|
|1.13|already obtain for range witness; no have projections|
|1.14|no consecutive rw commands; sum-congruence separates existing rewrites|
|1.15|Tried on both terminal simpa only calls; compiled golf2 but rejected after 846.313ms profile vs 282.147ms explicit baseline|
|1.16|only nonterminal simp is already simp only with four coefficient lemmas|
|1.17|dot notation used for Fin.ext, b.repr, etc.; LinearMap.ext_on explicit namespace clarifies theorem|
|1.18|n/a, no trailing tactic/function parentheses removable|
|1.19|n/a, no push_neg|
|1.20|n/a, not an existential witness helper|
|2.1|actual whole-proof grind fails; raw attempts log|
|2.2|n/a, no retained grind tail to absorb previous steps|
|2.3|Terminal simplifier shortening tried then rejected for speed; hcoeff all-at-once simp trial failed conditional Fin equality normalization|
|2.4|n/a, no analytic function property|
|2.5|n/a, no positivity/nonzero goal|
|2.6|n/a, no order inequality|
|2.7|n/a, no Nat/Int arithmetic goal; casts are coefficient indices|
|2.8|actual whole-proof aesop fails without progress|
|2.9|n/a, no concrete numerical/cast equality goal|
|2.10|n/a, arbitrary module/ring family has no closed decidable computation|
|2.11|n/a, no denominators|
|2.12|n/a, no ring/ring_nf conclusion or polynomial identity stage|
|2.13|n/a, no symmetric branches|
|2.14|n/a, no calc|
|2.15|n/a, no parallel similar subgoals; Finset.sum_congr produces one branch|
|3.1|n/a, no erw|
|3.2|n/a, no continuity/measurability|
|3.3|n/a, no omega|
|3.4|obtain rfl substitutes x directly; no redundant later simp of its equality|
|3.5|no global automation attribute: implementation helper is private and used once|
|3.6|n/a, no simp_all only|
|3.7|no maxHeartbeats or other limit setting in source|

## Step-back review

The dual-functional argument isolates substantive algebra and is not a 1–3-call wrapper. Basis independence alone does not prove independence of the coordinate polynomials. Coefficient extraction, vanishing on spanning generators, and evaluation on basis vectors are the necessary three stages. A coefficient simp trial failed because Nat equality tests inside nested sums do not automatically reduce to Fin equality; keeping the explicit sum_eq_single avoids brittle rewriting. The terminal cleanup compiled and saved four lines, but the actual isolated module measured 55.474ms outer command + 790.839ms outer async proof = 846.313ms, versus supplied explicit baseline 282.147ms. The shorter proof is rejected; terminal explicit lists are a justified performance exception under profiling.md. No timing claim is made for the entire project. No additional helper or public abstraction is needed. Existing mathematical statements/docs/comments preserved.

## Actual module performance

Both isolated actual repository-module commands exited 0, with no concurrent Lean request and no limit changes:

`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Separation.lean`

| Version | Outer command | Outer async proof | Conservative total | Decision |
|---|---:|---:|---:|---|
|Supplied original baseline|52.298ms|229.849ms|282.147ms|valid initial source baseline|
|Rejected four-line terminal shortening|55.474ms|790.839ms|846.313ms|rejected; >=750ms triggered next actual sweep|
|Final restored explicit proof|69.106ms|308.618ms|377.724ms|pass, <750ms and <1000ms|

Raw rejected log: /private/tmp/roth-d21-helper1-profile.log (anchors 256837,257008). Raw final repeat: /private/tmp/roth-d21-helper1-profile-final.log (anchors 257273,257450). Nested timings are not added. Actual public caller in final repeat: outer command 48.215ms at410958 + outer async640.097ms at420515 =688.312ms. No substitutions or caller source changes. This comparison supports retaining explicit terminal simp-only lists, not a whole-project performance claim.

Final source restored byte-for-byte to supplied d21 freeze; no retained source change. Declaration remains28 lines /23 proof-body lines. Four-line trial saved4 lines temporarily, then restored4; net0. Module remains587lines/26 retained declarations; Git numstat95 added/59 deleted is cumulative pre-existing d21 refactor, not this helper audit's delta.

Casts:0 dropped /1 Fin→Nat exponent coercion retained as cross-type /1 Polynomial R annotation retained to direct congrArg. No comments present in helper; public docs/header untouched. No new helper added, no rename queued, no public API proposal from this helper.

## Final verification and gates

Actual final `/Users/ramin/.elan/bin/lake build Roth.Separation` exited0,1876 jobs; raw /private/tmp/roth-d21-helper1-build-final.log. Initial trial build also exited0 at /private/tmp/roth-d21-helper1-build.log.

Independent exact ORIGINAL helper statement compiled under fresh name independentAudit, without using the audited helper or its public caller. The independent proof uses `simpa [Polynomial.finsetSum_coeff, Polynomial.coeff_C_mul_X_pow, Fin.val_inj, a, mul_ite] using h1` for coefficient extraction, unlike the retained explicit sum_eq_single argument. It proves the original CommRing/AddCommMonoid/Module contract, not a convenient specialization. Code /private/tmp/roth-d21-helper1-independent.lean; actual compile exit0, log /private/tmp/roth-d21-helper1-independent.log. The broad alternative is useful independent verification, not a retained unprofiled source golf.

The same compiled check enumerates imported environment names by exact suffix and checks actual built helper and actual built Roth.exists_separated_representation. All three (independentAudit, actual helper, actual caller) use only propext, Classical.choice, Quot.sound. No sorryAx/native/custom axiom. Actual helper type is printed at format.width100 in that log; it has only R,M,CommRing,AddCommMonoid,Module,n,l,v,b, with independent type universes, and no ambient τ/K instances.

Complete final unfiltered native lean_diagnostic_messages: success true, partial false, timed_out false, failed_dependencies empty;0errors/31warnings/0info/0hints. Full raw /private/tmp/roth-d21-helper1-lsp-final.json. No helper-local diagnostics. This matches initial complete0errors/31warnings at /private/tmp/roth-d21-helper1-lsp-initial.json. Existing header/public instance warnings retained within scope boundaries, never suppressed.

| Gate | Result | Evidence |
|---|---|---|
|lake_build_file|pass|actual final module build exit0|
|definition_protected|pass|no retained source diff against d21 freeze|
|theorem_statement_protected|pass|exact helper signature and public contracts unchanged|
|structure_gate|pass|23 body lines; no conjunction or >10-line case branch|
|naming_gate|pass|descriptive private _aux, no forbidden pattern/abbreviation|
|line_packing_gate|pass|five measured signature rows, all ok, max99codepoints|
|inequality_orientation_gate|pass|explicit zero-occurrence table|
|actual_axioms|pass|independent proof, actual helper/caller standard3 only|
|performance|pass|final actual helper377.724ms; caller688.312ms; rejected trial measured and repeated|

Overall pass. Before28lines, after28lines, saved0. No renames queued; no newly introduced helper; no pending private/public proposal from this helper; no changes to shared logs/Git. Public menu12 approval/application remains parent's work after this batch.

## Eleven completion steps

- [x] Step1 reference documents read (skills, cleanup Phase4, all golfing/proof/search/generalisation/gates; relevant naming/style/profiling).
- [x] Step2 all24 initial audit items recorded before source edits.
- [x] Step2.5 five actual search methods and honest index/automation limitations.
- [x] Step2.6 every effective binder drop probe and Ring/CommSemiring weakening probes; private literature exemption.
- [x] Step2.7 every signature line measured with explicit arithmetic.
- [x] Step2.8 every inequality region and name scanned.
- [x] Step3 all42 golf rules with concrete outcomes, rejected trial included.
- [x] Step4 step-back review, independent proof, and measured terminal-simp exception.
- [x] Step5a complete unfiltered final native LSP, zero errors.
- [x] Step5b actual module build, diff gates, built axioms, and isolated actual profiles.
- [x] Step6a no rename warranted; no queue mutation.

## Freeze

Full source SHA256 d4b98fed52d6f22e3a3c34e2509abf03a5f30ac2342161ab819afe6b8d70c32f; byte-for-byte full d21 snapshot equality and exact helper .txt equality checked. Source587lines,26 retained declarations. All source ownership is revoked, including the helper and any caller substitution scope. All Lean/MCP/compiler/build/profile requests started by this worker are drained/completed. Worker is report-only and makes no subsequent source edit. This fresh helper audit does not increment the original-declaration count.
