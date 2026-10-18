# Fresh independent audit: `Roth.exists_rat_factors_det_hasseDeriv_aux`

Initial audit recorded before any source edit. Scope: private helper at 508–533 and necessary `exists_det_eq_mul` call only. Initial snapshot `/private/tmp/roth-separation-d30-first-freeze.lean`; source 560 lines, helper body 20 lines, public main body 11 lines. No source edits currently proposed. Read Lean/mathlib-quality skills, full golfing-rules, proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates, relevant style/naming/profiling references and cleanup Phase 4. No delegation or Git mutations.

## Initial 24-item audit

1. LINT: complete fresh native module diagnostics requested; no warning suppression permitted.
2. HAVE SCAN: `hdeg` transports the degree bound across the injective integer/rational map; used by separated representation. `hFmap` transports the determinant and identifies the Wronskian product; used by final witness tuple. Both carry substantive mathematical facts, neither is a trivial alias.
3. SET_OPTION: none in helper or caller.
4. SIMP SQUEEZE: the sole `simpa [...] using hn` closes hdeg and remains unsqueezed. No nonterminal bare simp.
5. NAMING: exists_rat_factors_det_hasseDeriv_aux describes rational factors of a Hasse derivative determinant; `_aux` is unnumbered, private and permitted; `hasseDeriv` matches referenced API. No forbidden abbreviation/pattern, no rename needed.
6. LINE PACKING: full codepoint table below, to be verified before completion.
7. BY PLACEMENT: `:= by` ends the last signature line.
8. FORMAT: 2-space proof indentation, no empty body lines, no haveI/letI; `let := Fintype.ofFinite τ` installs finite enumeration locally.
9. COMMENTS: helper has no existing inline comments; public source narrative untouched.
10. DOCSTRING: private helper is exempt; public caller documentation preserved.
11. VISIBILITY: used only by exists_det_eq_mul; private appropriate.
12. STRUCTURE: helper 20 body lines below 60; caller 11 below 15. Shared l,D,U,V existential witnesses are correlated: splitting the conjuncts into independent existentials loses the common determinant and bounds. Parent explicitly agrees to retain the shared statement. No branch exceeds ten lines.
13. MATHLIB: actual five-method queries below; substantive project-level separated representation plus generalized Wronskian construction; no equivalent identified.
14. JUNK DEF: n/a, lemma.
15. EXISTS LEMMA: not trivial; constructs Wronskians through representation, nonvanishing and map/determinant transport. Not a reflexivity witness wrapper.
16. SHOW vs CHANGE: no show.
17. PUSH_NEG: none.
18. GENERALISE: every effective binder listed below. Finite rather than Fintype already minimizes the enumeration assumption. No public generalisation authorized beyond existing approved DecidableEq omission; public Fintype retained.
19. INEQUALITY: hn: degreeOf none P ≤ n; output 1 ≤ l; l ≤ n + 1; (D μ).degree ≤ μ. All four oriented ≤; no ≥ or >.
20. NORMAL-FORM: standard existential witnesses, degreeOf, rename and aeval factorization; no alternate custom predicate.
21. SYNTAX-GEN: hP and the sole relevant distinguished-variable bound hn are direct application hypotheses; caller supplies hr none.
22. IMPORT-FANOUT: no import changes.
23. CASTS: `(ν : ℕ)` bridges Fin to Nat; typed X fixes ambient polynomial coefficient/variable type in aeval; Matrix indices specify square size. None dropped.
24. INSTANCE-NAME: anonymous local finite enumeration; no named instance declarations.

## Generalisation: all effective binders

| Binder | Use | Candidate / initial conclusion |
|---|---|---|
| `{τ : Type*}` | variable index type, throughout | already universe polymorphic; dropping makes index unbound; no smaller structure involved |
| `[Finite τ]` | Fintype.ofFinite | drop probe required; no weaker standard finite-enumeration parent |
| `{P : MvPolynomial (Option τ) ℤ}` | polynomial whose determinant factors | value essential in goal; concrete ℤ→ℚ abstraction is a larger restatement, no API change proposed |
| `(hP : P ≠ 0)` | nonzero separated representation | drop probe required; zero polynomial cannot have nonzero separated determinant factors |
| `{n : ℕ}` | upper bound on l and input degree | index value essential; abstract order type would break Fin/natural derivative orders |
| `(hn : degreeOf none P ≤ n)` | hdeg | drop probe required; already weak inequality and pointwise none rather than global degree bound |
| ambient `[Fintype τ]` | explicitly omitted | not an effective binder; no public Fintype removal |
| ambient `[DecidableEq τ]` | explicitly omitted | not an effective binder; classical locally supplies decidability |

Inversion check: integer/rational map appears in hdeg, nonzero proof and hFmap, so concrete coefficient relation is used throughout, not discarded after one unfolding. A general injective characteristic-zero coefficient map would need a new coefficient framework; not a mechanical weakening. Private literature exemption applies; no external literature search is required for this unpublished implementation helper.

## Five actual search methods

A. Lean-Finder query: nonzero multivariate polynomial Hasse derivative determinant factors as separated polynomials Wronskian. Returned Polynomial.wronskian, wronskianBilin, divRadical_dvd_wronskian_right: binary polynomial partial matches, no multivariable determinant factorization.
B. Loogle query `MvPolynomial.hasseDeriv, Matrix.det` returned unknown identifier; retry `"hasseDeriv", "det"` pending. Failure is unavailability for this query, not absence.
C. LeanSearch query: determinant of Hasse derivatives of nonzero multivariate polynomial product of separated nonzero rational polynomials. Returned det_mvPolynomialX_ne_zero, Polynomial.hasseDeriv, hasseDeriv_comp; none equivalent.
D. Unfiltered rg in Mathlib and project: `hasseDeriv.*det|det.*hasseDeriv|separated_representation|genWronskian`; found local det_hasseDeriv_separated and project construction. One nonexistent optional project path was reported explicitly; mathlib source search itself completed.
E. Native name search `det_hasseDeriv`: source hit Roth.det_hasseDeriv_separated, index unavailable; cannot conclude indexed absence. Auxiliary `_of_`, separated and Wronskian variants included in source/type verification follow-up.

Conclusion: build on existing project Wronskian and mathlib injectivity/map APIs; retain substantive helper. No global claim of mathlib absence. Generic exact?/apply? route to be tested.

## Initial golfing statuses (all 42 rules)

| Rule | Concrete status |
|---|---|
|1.1|No by-exact wrapper; by block has construction.|
|1.2|No by-rfl.|
|1.3|No rw then exact on same goal; hFmap rewrite continues with congruence.|
|1.4|hdeg already uses simpa using hn.|
|1.5|No simp followed by rfl.|
|1.6|Final witness uses anonymous tuple already.|
|1.7|No apply then exact.|
|1.8|No contradiction block.|
|1.9|Nonzero lambda composes injectivity, not eta-only.|
|1.10|hdeg and hFmap are multi-step facts, not trivial single-use aliases.|
|1.11|No apply-intro sequence.|
|1.12|No show.|
|1.13|Both existence results already destructured via obtain.|
|1.14|hFmap has one rw before congruence and one after ext; cannot merge across ext.|
|1.15|No terminal simp only; terminal simpa left unsqueezed.|
|1.16|No nonterminal bare simp.|
|1.17|h.trans and map_injective use appropriate API.|
|1.18|Parentheses in injectivity lambda are nested applications; changing to <| gives no clarity gain.|
|1.19|No push_neg.|
|1.20|20-line existence construction, not reflexivity-only.|
|2.1|Whole-proof grind native attempt pending.|
|2.2|No preceding grind steps to delete.|
|2.3|Degree transport already consolidated as simpa.|
|2.4|No analytic function-property goal.|
|2.5|Nonzero factors arise from Wronskian independence, not ordered positivity.|
|2.6|No monotonicity inequality proof; bound transported by equality.|
|2.7|No Nat/Int arithmetic subproof needing lia.|
|2.8|Whole-proof aesop native attempt pending.|
|2.9|No concrete computation/cast equality goal.|
|2.10|Parametric existential construction not closed finite computation.|
|2.11|No field-denominator identity.|
|2.12|No ring/ring_nf ending.|
|2.13|No symmetric branches.|
|2.14|No calc block.|
|2.15|No repeated sibling goals; one Matrix.ext entrywise rewrite.|
|3.1|No erw.|
|3.2|No continuity/measurability tactic.|
|3.3|No omega; no arithmetic tactic needed.|
|3.4|No rfl-pattern rcases.|
|3.5|Existential helper should not rewrite globally; no automation attribute.|
|3.6|No simp_all only.|
|3.7|No heartbeat/recursion option.|

Initial issues: complete the actual probes and gate evidence; no source edit proposed. No new helper introduced by this audit.

## Final signature packing

Widths are Unicode codepoints. The next units are whole binders/application expressions, not partial identifiers that would sever Lean expressions. Exact type reference rendered using `set_option format.width 100; #check @Roth.fresh_helper` in `/private/tmp/roth-separation-d30-fresh-width.log`; the independently proved type is the exact initial helper type. The actual private constant type is also printed in the fresh built-axiom log.

| Line | Width | Next signature unit (width) | Sum | Action |
|---|---:|---|---:|---|
|508|94|`(hP : P ≠ 0)` (12)|107|ok|
|509|78|`∃ D : Fin l → (τ →₀ ℕ),` (23)|102|ok|
|510|100|`U ≠ 0` (5)|106|ok|
|511|76|Hasse derivative application through `.det` (70)|147|ok|
|512|98|`Polynomial.aeval ... V := by` (61)|160|ok|
|513|71|no following signature line|n/a|ok|

## Final inequality scan

| Location | Expression | Orientation | Action |
|---|---|---|---|
|509 hypothesis hn|degreeOf none P ≤ n|≤|retain|
|509 conclusion|1 ≤ l|≤|retain|
|509 conclusion|l ≤ n + 1|≤|retain|
|510 conclusion|(D μ).degree ≤ μ|≤|retain|
|517 local hdeg|degreeOf none PQ ≤ n|≤|retain|

No reversed inequality syntax or `_ge_`/`_gt_` name. The local hdeg makes five total occurrences including the proof.

## Step-back and simplify review

Rational separation is the mathematically independent stage preceding integral rescaling. It combines a separated representation with two Wronskian nonvanishing results and coefficient-map transport. The public caller then handles only integrality and degree bounds. Inlining would again mix these distinct mathematical stages; splitting shared existential witnesses would lose their correlations. No new public API or additional private helper is warranted.

Whole-proof native `grind`, `aesop`, `simp` attempts all failed; raw complete results `/private/tmp/roth-separation-d30-fresh-probe1.json`. In particular grind explicitly leaves the existential construction unsolved; aesop fails at rule depth 30 and its scratch continuation also times out at default 200000 heartbeats. These are failed experiments, not diagnostics of the unchanged source. No limit was raised. Native goal context is `/private/tmp/roth-separation-d30-fresh-probe0.json`.

The built-in simplify entry point is not installed in this tool set. Its requested holistic reuse/quality/efficiency review was performed directly above; outcome PASS-THROUGH, no issues requiring edits, no files modified by simplify. This is not a claim that an unavailable skill was invoked.

## Performance / buzz

Actual unchanged repository-module profile accepted from dispatch: `/private/tmp/roth-separation-d30-profile.log`, parsed `/private/tmp/roth-separation-d30-profile.log.json`.

| Declaration | Outer command | Outer async proof | Conservative total |
|---|---:|---:|---:|
|exists_rat_factors_det_hasseDeriv_aux|118.975 ms|377.575 ms|496.550 ms|
|exists_det_eq_mul|173.686 ms|133.513 ms|307.199 ms|

Both below 750ms repeat threshold and 1000ms budget. File is byte-identical to first freeze, so this remains a valid actual-module baseline; no changed proof requiring a fresh run. No nested trace costs counted twice, no extracted-copy timing substituted. Outcome FAST-BOARD for this scope, 0 raises added/removed, no profiling scaffolding. No whole-project speed claim.

Theta ordinary build and complete unfiltered LSP 0 errors / 28 warnings are reused from dispatch's unchanged frozen leaf evidence: `/private/tmp/roth-separation-d30-theta-final-build.log`, `/private/tmp/roth-separation-d30-theta-lsp.json`. The direct caller is `Roth.index_le_lem6`, not `index_det_le`. The attempted Theta profile `/private/tmp/roth-separation-d30-theta-profile-1ms.log` failed in its unchanged linarith proof at default 200000 heartbeats and is NOT successful performance evidence. Parent explicitly assigns external Theta performance to the next Theta file audit; no Theta source edits or limits raised here.

## Verification evidence

Fresh `lake build Roth.Separation` exit 0: `/private/tmp/roth-separation-d30-fresh-build.log`.
Complete native unfiltered Separation diagnostics: `/private/tmp/roth-separation-d30-fresh-probe3.json`, partial=false, success=true, timed_out=false, 0 errors / 2 warnings / 0 infos. Header warning is user-preserved metadata; unusedFintypeInType warning on public caller retained by exact approval scope. No suppression.
Independent theorem with exact INITIAL helper type and proof reconstructed from public dependencies (no self/helper invocation): `/private/tmp/roth-separation-d30-fresh-independent.lean`, compiled exit 0, log same stem `.log`. Its axioms and width-100 type additionally checked in fresh-width.log.
Actual built axioms: `/private/tmp/roth-separation-d30-fresh-axioms.log` (exit 0). Private name resolved by exact suffix from environment, not guessed; helper, exists_det_eq_mul and direct index_le_lem6 each only `[propext, Classical.choice, Quot.sound]`. Auxiliary `index_det_le` also checked, same result.
Native searches saved as `/private/tmp/roth-separation-d30-fresh-finder.json`, `-search.json`, `-local.json`, `-loogle.json`; successful empty retry `"hasseDeriv", "det"` in `-probe2.json`. Full-name and auxiliary source search also performed; no common-equivalents bucket matches a polynomial determinant construction. No equivalent established, rather than an unsupported absence claim.

## Gates

| Gate | Result | Evidence |
|---|---|---|
|lake_build_file|pass|fresh actual module exit 0|
|definition_protected|pass|no source edit; exact frozen file equality|
|theorem_statement_protected|pass|no source edit; public Fintype retained|
|structure_gate|pass with correlated-existential justification|20-line helper / 11-line headline theorem; shared witnesses retained by parent agreement|
|naming_gate|pass|descriptive mathematical name, no forbidden pattern|
|line_packing_gate|pass|all six signature lines measured above|
|inequality_orientation_gate|pass|five occurrences table; all ≤|
|cumulative_no_unintended_breakage|pass for affected scope|unchanged Theta ordinary build/LSP plus fresh direct-caller axioms; parent owns cumulative project gates|

No pending public API proposal from this worker. No Git or shared log mutations. Source change: 0 lines, helper body 20→20, public body 11→11, module 560→560; 27 retained declarations as supplied by original30 audit. One dedicated report written.

## Final binder and generic-route results

All fresh scratch probes are listed in `/private/tmp/roth-separation-d30-fresh-probes.json`, with exact `.lean` source and unfiltered `.log` per stem. These are actual compiler results, not untested negative claims; scratch compiler checks supplement native live-file goals/diagnostics.

| Effective binder | Actual result | Decision |
|---|---|---|
|τ|Deleting explicit binder compiles only because autoImplicit recreates it; with autoImplicit=false, unknown τ at line 5|retain explicit universe-polymorphic index binder|
|Finite τ|drop exits 1, failed synthesis at Fintype.ofFinite line 11|retain weakest existing enumeration assumption|
|P|drop exits 1, ambiguous polynomial index type at line 8; autoImplicit=false confirms unknown P line 34|retain typed polynomial input|
|hP|drop exits 1, unknown hP line 18|retain nonzero input required by representation|
|n|Deleting explicit binder compiles only because autoImplicit recreates it; autoImplicit=false confirms unknown n line 62|retain natural bound parameter|
|hn|drop exits 1, unknown hn line 15|retain pointwise weak degree bound|

Structural no-autoImplicit combined probe: `/private/tmp/roth-separation-d30-fresh-structural-drops.lean` and `.log`, exit 1, with all unknown-index/value diagnostics preserved. These tests establish proof/binder dependence, not impossibility of a different mathematical generalization. No unused effective binder discovered. No order structure exists on MvPolynomial here that would make replacing hP by positivity a meaningful weakening; no global continuity/monotonicity hypothesis to point-localize. ℤ/ℚ abstraction is a nonmechanical reformulation, not applied.

Generic compiled `exact?` probe exits 1 and fails to close the exact helper type. `apply?` probe exits 0 but emits **declaration uses sorry** and many partial suggestions with remaining subgoals; this is a failed/incomplete search, NOT a verified proof or independent-proof success. Raw `/private/tmp/roth-separation-d30-fresh-exact.log` and `-apply.log`. The genuine independent proof and actual source contain no sorry or nonstandard axioms.

Final rule status updates: 2.1 grind failed; 2.8 aesop failed; simp also failed. No tactic replacement retained. Loogle retry succeeded with zero items. The earlier query error remains documented; local index unavailable remains unavailable rather than evidence of absence.

## Eleven-phase completion ledger (scoped worker)

1. Phase 0 doctor: dispatched unchanged baseline; fresh actual module build and complete native LSP pass with preserved warnings.
2. Phase 1 prepare: full 560-line source inspected, exact initial helper snapshot and caller context inspected; applicable skills/references read. I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md.
3. Phase 2 audit: initial 24-item audit, every-binder table and 42-rule table written before any possible edit; no source edit followed.
4. Phase 3 file-level fixes: no authorized/needed file-level change; header user-preserved.
5. Phase 4 deep cleanup: all five actual searches; native goal/tactic attempts; complete binder probes; independent exact initial type proof; no retained change.
6. Phase 5a refactoring: no added helper or API change; correlated witnesses retained with parent agreement.
7. Phase 5b renames: clean mathematical name, no proposed rename or queue mutation.
8. Phase 6 gates: fresh module/native/independent/actual axioms verified; source byte-identical; parent owns cumulative whole-project and LeanEval gates.
9. Phase 6.5 simplify: direct holistic pass-through review, built-in entry unavailable and not falsely claimed invoked.
10. Phase 6.6 buzz: accepted actual unchanged module profile, helper 496.550ms and caller 307.199ms, below repeat/budget thresholds; no Theta performance claim.
11. Phase 7 report: this dedicated report contains audit, searches, binder tests, widths, inequalities, rule statuses, gate evidence, performance and freeze; no shared log/Git mutation.

## Final freeze and ownership release

All my native MCP, compiler, build, axiom, scratch and profiling requests have completed; no pending requests or running sessions remain. No profile was launched in this independent audit because the source is exactly the accepted baseline. Source ownership over ALL of Roth/Separation.lean, including this helper and necessary caller edits, is revoked. I am report-only; no later source edit is authorized to this worker.

Frozen Separation SHA256: `2f1dd34c7e9556683e147c522310bb4e07f9a21a6145a2f58018f928fb4b67f1`, 560 lines, exact first-freeze equality. Frozen unchanged Theta SHA256: `7804edad88aa3e586df46b7722755ba89e67566c5434c58ae970d0dd2fbfa4fd`.
