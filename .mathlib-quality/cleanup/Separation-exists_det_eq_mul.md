# Roth.exists_det_eq_mul — original declaration 30

Initial audit, written BEFORE source edits. Scope: exists_det_eq_mul and necessary new private proof helpers only. Approved amendment: omit ONLY DecidableEq τ before the preserved original docstring; RETAIN Fintype τ. Definitions, existing helpers and documentation protected. Read lean4 and mathlib-quality skills, full golfing-rules/proof-patterns/mathlib-search/generalisation-patterns/cleanup-gates, and relevant cleanup Phase 4, naming, style and profiling references.

## Initial 24-item audit
1. LINT: complete native unfiltered LSP: 0 errors, 3 warnings: protected header, unused DecidableEq and Fintype on target. Apply only authorized DecidableEq removal, preserve Fintype warning.
2. HAVE SCAN: hPQ0 (proof-content lambda), hdeg (by proof), hW (no by, one use: inline), hFmap (by proof), two h1 bounds (one use each: inline through simpa where useful). PQ and F are set binders, necessary repeated expressions; not have aliases.
3. SET_OPTION: none.
4. SIMP SQUEEZE: hdeg terminal simpa, no nonterminal bare simp. Preserve terminal unsqueezed simplification.
5. NAMING: exists_det_eq_mul explicitly describes existential determinant factorization; snake_case with established hasseDeriv API component where used. No forbidden abbreviations/numbers; no rename needed.
6. LINE PACKING: initial per-line table below; will repack semantic binders/logical groups without splitting correlated outputs.
7. BY PLACEMENT: all by at prior line end.
8. FORMAT: two-space indentation; no empty body lines. Ordinary lambdas currently =>; change owned body lambdas to ↦. Matrix.of lambda => in preserved statement may become ↦ as syntax-only style.
9. COMMENTS: no inline proof comments; original Lemma 2 source doc preserved verbatim.
10. DOCSTRING: existing detailed public source citation preserved by explicit contract.
11. VISIBILITY: public headline consumed by Roth.index_le_lem6 in Theta; retain public.
12. STRUCTURE: current body 27 physical lines (>15 headline budget); extract substantive rational separated-determinant construction. The conjunction is under shared dependent existential witnesses l,D,U,V: independently splitting existential conclusions loses correlation, so direct recombination applies. No case branches >10.
13. MATHLIB: five actual methods executed; logs initial-0/1/2/3/6. Finder/LeanSearch returned unrelated partial foundational matches; Loogle hasseDeriv query unavailable identifier in remote snapshot, successful wronskian name query finds two-polynomial API rather than finite generalized determinant. Source and local pattern locate Roth decomposition/nonvanishing/degree API. No claim of proved absence.
14. JUNK DEF: n/a theorem, no definition added.
15. EXISTS LEMMA: target is public substantive existence, not trivial witness bundle.
16. SHOW/CHANGE: no show.
17. PUSH_NEG: none.
18. GENERALISE: every effective binder considered below. Only DecidableEq removal approved; Fintype stays even if independent proof does not need it.
19. INEQUALITY: all ≤ in correct orientation; no ≥/> code tokens. Table below.
20. NORMAL FORM: existential natural size, derivative multi-indices, integer polynomial factorization and degreeOf/natDegree bounds already canonical; determinant equality oriented constructed determinant to factors.
21. SYNTAX-GEN: closed correlated outputs directly destructured by Theta caller, preserving ordering supports application.
22. IMPORT FANOUT: no new imports needed.
23. CASTS: (ν : ℕ) cross-type Fin→Nat necessary; Matrix Fin l annotations pin determinant size; coefficient type ascriptions fix aeval target. No redundant ↑.
24. INSTANCE NAME: n/a theorem, no instance declarations.

## Generalisation initial status (all effective binders)
| Binder | Role/use | Candidate/probe | Initial result |
|---|---|---|---|
| τ : Type* | variable index, all constructions | universe already polymorphic; drop makes conclusion ill-formed | retain |
| Fintype τ | original public instance | independent drop-body probe planned; exact user requires retaining | retain irrespective result |
| DecidableEq τ | original unused decidability | independent omission probe + native file LSP | approved remove after verification |
| P : MvPolynomial (Option τ) ℤ | determinant input and integer descent | drop makes conclusion ill-formed; abstract coefficient requires different descent theorem | retain ℤ |
| hP : P ≠ 0 | rational nonzero, independent factors | drop probe planned; cannot construct separated nonzero representation | retain |
| r : Option τ → ℕ | bound values across output | drop makes statement ill-formed; coefficient/ring abstraction changes API | retain |
| hr : ∀ j, degreeOf j P ≤ r j | none size + all degree estimates | drop and local-only bound probes planned; full-variable conclusion requires all j | retain |
Pointwise/strict→weak catalogue: hr already weak bound, no strict hypothesis; hP cannot be weakened to nonnegativity for unordered polynomials. No bundled input assumptions. Inversion check: P and r remain in determinant construction and degree bounds throughout, so no concrete-object disappearance. New private helper remains restricted to meaningful rational descent construction; it is not a fixed-witness conjunction wrapper.

## Literature search
Actual WebSearch queries: Roth lemma 2 determinant differential operators separation polynomial Takloo Bighash Yin generalization; Roth lemma polynomial differential operators determinant U V separation lemma characteristic zero; Roth generalized Wronskian lemma.
Relevant primary hits: https://turing.cs.hbg.psu.edu/~rawalker/LinDep-post.pdf ; https://modnet.imj-prg.fr/preprints/papers/archive/680.pdf ; https://www.ams.org/bookstore/pspdf/mbk-48-prev.pdf . These discuss generalized Wronskians and characteristic-zero/rational-function extensions; no evidence supporting changing the integral-output public contract. Source remains local clean.tex Lemma 2. Math ChatGPT MCP unavailable in listed tools. No public generalization proposed beyond exact approved omission.

## Initial signature line packing
| Line | Codepoints | Next semantic signature unit | Sum | Action |
|---|---:|---|---:|---|
| 507 | 89 | `(hr : ∀ j, degreeOf j P ≤ r j) :` | 122 | logical-group break |
| 508 | 36 | `∃ l, 1 ≤ l ∧ l ≤ r none + 1 ∧ ∃ D : Fin l → (τ →₀ ℕ), (∀ μ, (D μ).degree ≤ μ) ∧` | 116 | logical-group break |
| 509 | 83 | `∃ (U : MvPolynomial τ ℤ) (V : Polynomial ℤ), U ≠ 0 ∧ V ≠ 0 ∧` | 144 | logical-group break |
| 510 | 66 | `(∀ j, degreeOf j U ≤ l * r (some j)) ∧ V.natDegree ≤ l * r none ∧` | 132 | logical-group break |
| 511 | 73 | `(Matrix.of fun μ ν : Fin l =>` | 103 | logical-group break |
| 512 | 37 | `hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) P).det =` | 110 | logical-group break |
| 513 | 84 | `rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) ℤ) V := by` | 162 | logical-group break |
| 514 | 87 | `` | n/a | final |

## Inequality scan
| Location | Occurrences | Action |
|---|---|---|
| hr | degreeOf j P ≤ r j | correct |
| existential size | 1 ≤ l; l ≤ r none + 1 | correct |
| derivative bound | (D μ).degree ≤ μ | correct |
| degree bounds | degreeOf j U ≤ l * r (some j); V.natDegree ≤ l * r none | correct |
| ≥ or > code | 0 | no rewrite/rename |

Initial action: decompose rational construction, preserve dependent witness conjunction and degree control, inline hW, apply approved omit, then independently recover exact original type. New helper requires a fresh independent leaf audit after freeze before parent publication.

## Final audit updates / step-back review
The argument now reads: construct a rational separated determinant using independent coefficient families and their nonzero Wronskians; descend its factors to integers; recover each factor's degree from the determinant degree estimate. The helper proves substantive existence with correlated witnesses, rather than bundling facts for an already-fixed witness. Integer descent remains in the headline, making the mathematical boundary explicit. No changes to existing factor helpers. No public widening beyond the approved DecidableEq omission. No definition, import, documentation or source narrative changed.

Final HAVE SCAN: headline has zero `have`; helper has hdeg (by proof of mapped degree bound, used once, content retained) and hFmap (by determinant transport proof, used once, content retained). Original hW, hPQ0 and both degree aliases eliminated. PQ and F still factor repeated expressions. hPQdef is used in the degree transfer; its redundant rewrite after inlining hPQ0 was removed.

Generalisation verified: new private helper uses `[Finite τ]`, supplying a local plain `let := Fintype.ofFinite τ`; thus no new unused-instance warning. Main retains `[Fintype τ]` as expressly required. Complete native LSP confirms DecidableEq omission. Standalone original and new signatures use the old non-self constructive proof, independent of both new helper and target. Drop Fintype fails at the generalized Wronskian instance; drop hP fails at rational nonzero proof; drop hr fails degree transfer/bounds; replacing hr with only its none bound fails the all-variable determinant estimate. These are dependency probes of the present proof, not mathematical nonexistence theorems. τ/P/r drop tests are structurally ill-formed because their variables occur in the conclusion; no compiler-verified negative is claimed for those data binders. Private helper probes drop Finite, hP and hn individually. Universe polymorphism is already maximal; global→pointwise and strict→weak do not apply beyond the tested none-only alternative to hr. ℤ→abstract coefficient descent would change the public contract and is not proposed.

Literature conclusion: Wronskian generalizations to characteristic-zero differential/rational-function settings do not justify silently replacing integer factor outputs. The existing integer formulation follows local Lemma 2, with the finite-variable representation aligned to generalized Wronskians. Private helper literature exemption: private proof decomposition; no public mathematical contract added.

## All 42 golfing rules
| Rule | Concrete status |
|---|---|
| 1.1 | n/a: no `by exact` wrapper. |
| 1.2 | n/a: no `by rfl`. |
| 1.3 | Existing `rwa` degree-alias proofs replaced by goal rewrites + direct bound, eliminating the aliases. |
| 1.4 | Tried terminal `simpa` degree consolidation; both bare and `only` variants fail matching determinant before factorization. Reverted to direct goal rewrite. |
| 1.5 | n/a: no simp followed by rfl. |
| 1.6 | Applied: correlated outputs assembled with one anonymous constructor; no constructor/exact branch chain. |
| 1.7 | Applied where relevant: directly exact determinant degree theorem after rewriting, no apply/exact pair. |
| 1.8 | n/a: no contradiction/push-neg chain. |
| 1.9 | n/a: all retained lambdas either index the derivative expression or perform genuine extensional proof; none eta-reducible. |
| 1.10 | Applied: hW, hPQ0 and two bound aliases eliminated. |
| 1.11 | Already appropriate: `refine Matrix.ext fun μ ν ↦ ?_`; no apply/intro chain. |
| 1.12 | n/a: no redundant show. |
| 1.13 | Already appropriate: obtain destructures separated representation, generalized Wronskian, rational factors and integral factors directly. |
| 1.14 | Already appropriate: determinant transport has one rw chain, final coefficient transport another; degree branches one rw each. |
| 1.15 | Retained unsqueezed terminal simpa for mapped degree. Failed simpa-only attempt was reverted. |
| 1.16 | n/a: no nonterminal bare simp. |
| 1.17 | Dot notation used for mapDomain/trans; no shortened direct theorem equivalent of degree bound. |
| 1.18 | n/a: no trailing by/fun argument parenthesis to remove safely. |
| 1.19 | n/a: no push_neg. |
| 1.20 | n/a: substantive rational construction, not reflexive fixed witness existence. |
| 2.1 | Actual native whole-proof `grind` failed at existential factor construction; log golf-whole.json. |
| 2.2 | n/a: final proof has no grind or preceding grind scaffolding. |
| 2.3 | Actual simpa degree consolidation failed (both variants); direct rewrite and exact retained. |
| 2.4 | n/a: no continuity/differentiability/measurability goal. |
| 2.5 | n/a: nonvanishing depends on independent Wronskians/injective integer cast, not ordered positivity; no ordered scalar subgoal. |
| 2.6 | n/a: the degree estimates are API identifications followed by the exact determinant theorem, not monotonicity congruence. |
| 2.7 | n/a: arithmetic size/order inequalities supplied directly by substantive existence lemmas; no Nat/Int arithmetic proof left. |
| 2.8 | Actual native whole/assembly aesop attempts fail and hit normal rule/depth bounds; no limits raised. |
| 2.9 | n/a: coefficient cast transport uses ring-hom naturality and degree-map injection, not concrete numeric cast arithmetic. |
| 2.10 | n/a: arbitrary polynomial existence is not a finite closed decidable proposition. |
| 2.11 | n/a: no denominators or field algebra identity. |
| 2.12 | n/a: no ring/ring_nf proof with hypotheses. |
| 2.13 | n/a: no symmetric case split. |
| 2.14 | n/a: no two-step calc. |
| 2.15 | n/a: degreeOf some and natDegree none are distinct APIs; shared blanket automation fails to identify factors. |
| 3.1 | n/a: no erw. |
| 3.2 | n/a: no legacy continuity/measurability. |
| 3.3 | n/a: no omega/lia. |
| 3.4 | n/a: no rcases with rfl. |
| 3.5 | No attribute added: a noncanonical multi-witness existence theorem is unsuitable as a global simp/grind rule. |
| 3.6 | Whole/assembly simp_all actually fails at existence; no simp_all-only in final source. |
| 3.7 | n/a: no limit override exists or added. |

Native attempts: `/private/tmp/roth-separation-d30-golf-main.json` and `...-golf-whole.json`. The multi-attempt engine substitutes a tactic in context and reports downstream effects as well; failures are explicitly not clean-module evidence. Final complete module diagnostics remain the acceptance gate.

## Final signature width tables
Every row below uses codepoints. The next token is a complete semantic binder, quantified proposition, matrix lambda prefix, derivative operand, or product operand (not an arbitrarily split word). No row permits moving that unit without overflow.

### exists_rat_factors_det_hasseDeriv_aux

| Line | Chars | Next semantic unit | Arithmetic | Action |
|---|---:|---|---|---|
| 508 | 94 | `(hP : P ≠ 0)` (12) | 94 + 1 + 12 = 107 | ok |
| 509 | 78 | `∃ D : Fin l → (τ →₀ ℕ),` (23) | 78 + 1 + 23 = 102 | ok |
| 510 | 100 | `U ≠ 0 ∧` (7) | 100 + 1 + 7 = 108 | ok |
| 511 | 76 | `hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) P).det =` (72) | 76 + 1 + 72 = 149 | ok |
| 512 | 98 | `Polynomial.aeval (X none : MvPolynomial (Option τ) ℚ) V := by` (61) | 98 + 1 + 61 = 160 | ok |
| 513 | 71 | `` (0) | n/a — final signature line | ok |

Reference: actual `#check` rendered with `format.width := 100` in `/private/tmp/roth-separation-d30-axioms.log` (public headline), and independent helper declaration/probe for helper.

### exists_det_eq_mul

| Line | Chars | Next semantic unit | Arithmetic | Action |
|---|---:|---|---|---|
| 541 | 89 | `(hr : ∀ j, degreeOf j P ≤ r j)` (30) | 89 + 1 + 30 = 120 | ok |
| 542 | 90 | `(∀ μ, (D μ).degree ≤ μ) ∧` (25) | 90 + 1 + 25 = 116 | ok |
| 543 | 92 | `(∀ j, degreeOf j U ≤ l * r (some j)) ∧` (38) | 92 + 1 + 38 = 131 | ok |
| 544 | 73 | `(Matrix.of fun μ ν : Fin l ↦` (28) | 73 + 1 + 28 = 102 | ok |
| 545 | 36 | `hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) P).det =` (72) | 36 + 1 + 72 = 109 | ok |
| 546 | 100 | `Polynomial.aeval (X none : MvPolynomial (Option τ) ℤ) V := by` (61) | 100 + 1 + 61 = 162 | ok |
| 547 | 71 | `` (0) | n/a — final signature line | ok |

Reference: actual `#check` rendered with `format.width := 100` in `/private/tmp/roth-separation-d30-axioms.log` (public headline), and independent helper declaration/probe for helper.

## Final inequality scan
| Declaration | Location/occurrences | Result |
|---|---|---|
| headline | hr; 1 ≤ l; l ≤ r none + 1; derivative bound; U bound; V bound (6) | all smaller side left |
| rational helper | hn; 1 ≤ l; l ≤ n + 1; derivative bound (4) | all smaller side left |
| both | ≥ or > (excluding ↦ and →) | zero; no rewrite/rename |

Final casts: 0 dropped / 5 kept as cross-type Fin→Nat / 8 kept as load-bearing matrix-size and aeval target annotations, across the owned new helper plus target. No ↑ casts added; no custom instance declaration, haveI/letI, warning suppression, axiom, sorry, native_decide or profiler scaffolding added.

## Changes/counts
- exists_det_eq_mul: 35 → 18 declaration lines (17 saved); 27 → 11 physical body lines (16 saved).
- exists_rat_factors_det_hasseDeriv_aux: 26 declaration lines; 20 physical body lines.
- Source line count: 548 → 560; net +12. One new private declaration; target retained.
- Exact original docstring is byte-identical; original public statement differs only in approved instance omission and lambda/whitespace syntax. Public nonzero hypotheses, r argument, bounds, integral coefficient types, output witness order and equality are preserved.

## Verification artifacts and gates
- Native complete unfiltered Separation diagnostics: `/private/tmp/roth-separation-d30-final-lsp.json`, `partial=false`, `timed_out=false`, success, 0 errors / 2 warnings / 0 infos. Remaining warnings are the explicitly preserved header and user-required public Fintype argument.
- Native complete unfiltered Theta diagnostics: `/private/tmp/roth-separation-d30-theta-lsp.json`, `partial=false`, `timed_out=false`, success, 0 errors / 28 warnings / 0 infos. The actual direct external `Roth.index_le_lem6` caller and the additionally requested `Roth.index_det_le` theorem remain built and unchanged. No explicit argument adjustment was needed.
- Actual final module gate: `/Users/ramin/.elan/bin/lake build Roth.Separation Roth.Theta`, exit 0; `/private/tmp/roth-separation-d30-final-modules-build.log` ends `Build completed successfully (2423 jobs).` Earlier single-module Separation success is in `...-final-build.log`; Theta build in `...-theta-final-build.log`.
- Independent exact ORIGINAL proof: `/private/tmp/roth-separation-d30-original.lean`, full original statement with explicit `{τ : Type*} [Fintype τ] [DecidableEq τ]` in original order and original bound/witness contract. Its proof never mentions target or new helper. Final standalone compile exit 0, `/private/tmp/roth-separation-d30-original-final.log`; standard axioms and complete old #check output included. The old type was checked against `/private/tmp/roth-separation-original.lean`.
- Independent approved NEW proof: `/private/tmp/roth-separation-d30-new.lean`, explicit `[Fintype τ]` retained and no DecidableEq; old constructive proof independent of target and helper. Successful first log `...-new.log`; final repeat in `...-new-final.log`.
- Actual compiled axioms: `/private/tmp/roth-separation-d30-axioms.lean`, with actual public target and actual external `Roth.index_det_le` plus environment exact-suffix lookup of the private rational helper. Each has exactly `[propext, Classical.choice, Quot.sound]`; `/private/tmp/roth-separation-d30-axioms.log`, final repeat `...-axioms-final.log`. No guessed numeric private-name component was used for the query.
- Binder probes: `...-dropFintype.log`, `...-dropHP.log`, `...-dropHR.log`, `...-onlyNone.log`, plus `...-helper.log`, `...-helperDropFinite.log`, `...-helperDropHP.log`, `...-helperDropHN.log`. Successful helper independent reconstruction exits 0; all specified negative probes exit 1 at expected dependencies. Compiler-produced `sorryAx` in invalid scratch declarations is not accepted evidence; no such declaration is added to repository source. Initial negative probe attempts raced a rebuilding olean and were rerun after an actual build; only the successful-import reruns above count as binder evidence.

| Gate | Status | Evidence |
|---|---|---|
| definition_protected | pass | no existing definition touched |
| theorem_statement_protected | pass | only exact user-approved omission; proposition preserved |
| naming_gate | pass | descriptive existential determinant name; private hasseDeriv API name and `_aux` suffix |
| line_packing_gate | pass | every final signature line measured above; 100 maximum |
| inequality_orientation_gate | pass | complete per-occurrence table above; no reversed code inequality |
| structure_gate | pass | headline 11 physical lines; helper 20; longest degree branch 3; correlated outputs recombined directly |
| lake_build_file | pass | actual Separation and Theta build exit 0 |
| cumulative_no_unintended_external_breakage | pass for direct caller | actual Theta build and complete unfiltered native LSP; parent owns final whole-project gate |
| axioms | pass | actual retained/new/caller constants standard-only |

## Eleven completion steps
1. References read: full required golf/proof/search/generalisation/gates and relevant style/naming/profile material; explicit scoped contract takes precedence over generic public-API edits.
2. Full initial audit: all 24 items written before source edit; final updates recorded.
3. Five-method search: all methods actually executed; warming symbol index and unavailable remote hasseDeriv identifier recorded without absence claims.
4. Every-binder generalisation: effective public binders and new private helper covered; compiled dependency/drop probes and semantic reasons distinguished.
5. Width table: every final signature line measured, every identified repack applied and table corrected.
6. Inequality scan: per-occurrence results for both declarations; no reversed inequality.
7. All 42 golf rules: concrete statuses, actual whole/assembly automation probes and failed simpa consolidation recorded.
8. Step-back reflection: substantive rational construction separated from integer descent; no fixed-witness conjunction helper, no duplicate mathlib wrapper or existing helper edits.
9. Complete native LSP: raw full module and direct-caller results saved, not partial/time-limited successes.
10. Diff gates/build/proofs/axioms: actual module build, independent old/new proofs, exact actual private lookup, and direct caller checks run; parent retains cumulative whole-original/all-retained/full-project/LeanEval/commit/push gates.
11. Rename/output handling: no rename needed; only dedicated report written; no Git/shared-log mutation or subagent delegation. Isolated profiling and final freeze appended below.

## Isolated actual-module profiling
All native Lean/MCP/compiler/build/probe requests completed before starting the sweep. Exact command: `/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Separation.lean`. Exit 0; raw log `/private/tmp/roth-separation-d30-profile.log`, anchored parse `/private/tmp/roth-separation-d30-profile.log.json`. Parser takes the maximum enclosing command anchor plus the outer asynchronous proof anchor and never sums nested trace nodes.

| Actual declaration | Outer command ms | Outer async proof ms | Conservative total ms |
|---|---:|---:|---:|
| exists_det_eq_mul | 173.686 | 133.513 | 307.199 |
| exists_rat_factors_det_hasseDeriv_aux | 118.975 | 377.575 | 496.550 |

Both are below 750 ms, so neither requires a borderline repeat. Accepted prior actual-module old-target baseline: `/private/tmp/roth-separation-d29-owner-profile1.log(.json)` gives 120.919 + 397.858 = 518.777 ms; repeat `...profile2.log(.json)` gives 108.477 + 429.718 = 538.195 ms. The headline now elaborates less work, while construction work lives in the new helper; this is a decomposition comparison, not a claim of whole-module or project performance improvement.

### External Theta profile: actionable limitation, not a performance pass
The actual direct source call is `Roth.index_le_lem6` at Theta.lean:530. The additionally dispatched `Roth.index_det_le` is a separate theorem at line 406. Both were included in the actual Theta build/LSP and subsequent axiom checks.

The threshold-zero actual-module Theta sweep stalled at 135 MB / 1,341,552 trace lines. Its own session was terminated cleanly with Ctrl-C (exit 130), all requests drained, and that incomplete log (`/private/tmp/roth-separation-d30-theta-profile.log`) is EXCLUDED from accepted complete samples.

Owner explicitly authorized a bounded reduced-trace rerun. Lean 4.34 source `/Users/ramin/.elan/toolchains/leanprover--lean4---v4.34.0/src/lean/Lean/Util/Trace.lean:182–185` declares the option as `Nat` in milliseconds, so `-Dtrace.profiler.threshold=1` is exactly 1 ms. The actual command remained `/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=1 Roth/Theta.lean`, with a 120-second process-group timeout wrapper. It completed within the bound, exit 1, because profiling the unchanged direct caller reached the default 200000 heartbeat limit at Theta.lean:604 and :617, specifically the linarith simplex algorithm. No limit was raised and no Theta proof was changed.

Raw complete failed-run output: `/private/tmp/roth-separation-d30-theta-profile-1ms.log`; run status: `...-theta-profile-1ms-status.json`; actual anchored parse: `...-theta-profile-1ms.log.json`.

| Actual external declaration | Outer command ms | Outer async proof ms | Sum ms | Interpretation |
|---|---:|---:|---:|---|
| index_det_le | 79.149 | 1976.026 | 2055.175 | unchanged external theorem; over budget |
| index_le_lem6 | 42.342 | 9973.583 | 10015.925 | failed instrumented elaboration; diagnostic timing only |

These are actual source anchors but NOT an accepted successful Theta performance sample. The ordinary actual Theta build and complete unfiltered native LSP passed. External performance remains explicit follow-up for the next dedicated Theta cleanup, as instructed by the owner after the measurement; no authorization to broaden this worker's source scope was granted. Consequently this report claims successful target/helper profiling only and DOES NOT claim whole-module or whole-project performance success. The over-budget/failing external evidence is preserved rather than hidden by limits, extraction into a namespace copy, or an aggregate timing claim.

## Final completion and freeze
Final actual axiom compile exited 0: `/private/tmp/roth-separation-d30-axioms-final.log` now includes all four actual constants: the public target, `Roth.index_det_le`, the real direct caller `Roth.index_le_lem6`, and the exact-suffix-located private helper. Every one uses only `propext`, `Classical.choice`, `Quot.sound`. The same output includes the actual private helper's type rendered at `format.width := 100`, confirming its `[Finite τ]` hypothesis and rational determinant conclusion. Independent exact original and new proofs both finally exit 0 in their `*-final.log` artifacts.

Actual focused source diff arithmetic (against d30-before, no Git mutation): +45 / -33, net +12; source 548 → 560 lines. Existing source before the new helper is byte-identical, and the original Lemma 2 docstring is byte-identical to both pre-worker and original snapshots. One new private declaration only: `Roth.exists_rat_factors_det_hasseDeriv_aux`, actual environment constant `_private.Roth.Separation.0.Roth.exists_rat_factors_det_hasseDeriv_aux` at source line 508. Its independent fresh declaration audit is REQUIRED from another leaf after this freeze and BEFORE publication; this worker does not self-certify that independent gate. No other new helper, public alias or definition was introduced.

All my native Lean/MCP, compiler, module build, standalone probe and profile requests have completed or been terminated and drained. The accepted target/helper sample completed exit 0; the terminated and failed external Theta samples are explicitly excluded as successful performance gates. External Theta performance follow-up remains pending under the owner's explicit scope decision; no source widening is pending.

**Source freeze SHA256** (`Roth/Separation.lean`): `2f1dd34c7e9556683e147c522310bb4e07f9a21a6145a2f58018f928fb4b67f1`.

I revoke ALL source ownership and become report-only. No source edit will follow this freeze. Parent owns fresh helper audit, cumulative original/public/all-retained checks, final whole-project build followed by separate LeanEval build, exact-path commit and verified push. This is a completed declaration-worker handoff with the explicit external performance follow-up; it is not a claim that the parent publication workflow or whole-project performance gate has finished.

## Required fresh helper audit resolution
[Distinct fresh full audit](Separation-exists_rat_factors_det_hasseDeriv_aux.md) retained the20-line private rationalconstruction helper unchanged. Freshmodulebuild, completeLSP0errors/2preservedwarnings, independentexactINITIALnonselfproof and actualhelper/main/directindex_le_lem6 standardaxioms allpass. Allrequestsdrained and sourceownershiprevoked. FrozenSHA remains2f1dd34c7e9556683e147c522310bb4e07f9a21a6145a2f58018f928fb4b67f1; accepted prior isolatedactualmodule profile is therefore unchanged-source evidence. Ownerall27anchorparse max705.265ms, allbelow750/1000. Filefinalphasesremain afteroriginal30checkpointpublication; externalTheta instrumentedprofilelimitation above remains explicit nextfileperformancework.

## Owner cumulative publication gates

Source FROZEN SHA256 `2f1dd34c7e9556683e147c522310bb4e07f9a21a6145a2f58018f928fb4b67f1`; leaf ownership revoked and requests drained before owner gates. Owner probe `26845` exit0,48.43s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL27 actual retained standardaxiom checks. `/private/tmp/roth-separation-d30-compatibility.{lean,log,json}`. Owner build session `71967` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,93.75s/32.91s; source hash stable. `/private/tmp/roth-separation-d30-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.
