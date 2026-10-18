# Cleanup: `Roth.pow_rootMultiplicity_le` (original 19)

Scope: dedicated single-declaration audit, with the necessary one-line caller adaptation in
`Roth.Θ_unique_le`. Released checkpoint `ab9c01a9913d5309b27f35db846cfda82cf8977d`, source
SHA256 `718711f6e77fd4aaee62970a7447b67cfdac545c42fc1dc2a22158efa1741a5f`.
Immutable original: `2b64544bf9f77a8ff957bf1bcaf693ac72217ff6`.
Artifacts below live in `/private/tmp/roth-rootmult-bound/` unless a full path is given.

## Result and authorization

The hypothesis `hB` now asks only `|(R.leadingCoeff : ℝ)| ≤ B`, rather than a uniform bound
on every coefficient. This weakens the hypothesis and strengthens the theorem: the proof compares leading coefficients,
and the old hypothesis supplies the new one at `R.natDegree`. The public name, all other binder
domains, all names/order/BinderInfo, coefficient domains and conclusion are retained. The owner's
explicit direction under the user's standing authorization approved exactly this localization,
after the complete old-contract adapter and candidate caller compiled. No other API change.

The sole caller passes `hcoef R1.natDegree`; its complete immutable original contract, including
`[DecidableEq σ]`, is preserved. Target proof: **13 → 12 lines**. Inline the single-use `hQ0`,
normalize the existing `hB` directly instead of introducing a redundant coefficient-bound alias.
Original documentation/source quote preserved, with one sentence explaining the weaker premise.
No new production helpers, definitions, attributes, imports, axioms or limits.

## Preparation and baseline

Read `/private/tmp/roth_theta_leaf_instructions.md`, both complete Lean/mathlib-quality skills,
complete cleanup command, full golfing-rules/proof-patterns/mathlib-search/generalisation-patterns/
cleanup-gates/profiling references, and relevant style/naming sections. Read current Theta and
immutable original target/caller. Preparation before RELEASE performed no writes or Lean requests.

Baseline doctor: owner full project build exit 0 (58.997s), then separate `Roth.LeanEval` exit 0
(23.527s), all 17 hashes unchanged at release. Matching complete unfiltered baseline LSP reused
from `/private/tmp/roth-rootmult-factor/final-lsp.json`: success=true, partial=false,
timed_out=false, failed_dependencies=[], zero errors, 18 existing warnings. Target has no
warnings; caller's old DecidableEq warnings belong to the next original declaration's audit.

A fresh uncontended baseline exact-prefix profile was also run, rather than relying solely on
the inherited measurement. `baseline-prefix.lean` preserves the exact released preceding source
and ends after this target. Prefix-only evidence never certifies the whole module.

## Full 24-item audit

| # | Item | Finding/action |
|---|---|---|
| 1 | Lint | No target warnings; preserve caller's full old type including its pending DecEq. |
| 2 | Have scan | Old hQ0: no by, one use → inline. hlc: by proof, one use → retain. h1: by proof, one use → retain. Old h2: coefficient-bound alias, rewritten at four sites → eliminate by normalizing localized hB itself. Final only hlc and h1 remain. |
| 3 | Options | No target options or raised limits. |
| 4 | Simp | No target simp calls. Existing rw/push_cast uses explicit focused normalization. |
| 5 | Naming | pow_rootMultiplicity_le describes the bound and follows the existing rootMultiplicity API atom; no forbidden numeric or abbreviated pattern. No rename. |
| 6 | Packing | Every signature line measured below; all breaks justified. |
| 7 | By | At end of signature/typed-have lines. |
| 8 | Format | Two-space proof indent, no blank proof lines/semicolons/haveI/letI. |
| 9 | Comments | Zero original inline proof comments; no narrative removed. Original source quote preserved. |
| 10 | Docstring | Preserve original sufficient-condition sentence/quote; append leading-coefficient clarification authorized by owner. |
| 11 | Visibility | Public mathematical bound retained as selected public API; no visibility churn. Classic-file dialect. |
| 12 | Structure | Twelve proof lines, no conjunction result, no case branch; no extraction needed. |
| 13 | Mathlib | All five actual methods plus clean compiled automation probes below; partial rational-root matches only. |
| 14 | Junk def | n/a: theorem, no definition introduced. |
| 15 | Exists | n/a: numerical inequality, not a trivial witness wrapper. Existing factorization theorem already separately audited. |
| 16 | Show/change | None in target or added diff. |
| 17 | Push-neg | None. |
| 18 | Generality | Every effective binder drop compiled; localize uniform hB to leading coefficient, old contract recovered. See table. |
| 19 | Inequalities | Smaller side left in all code; scan below. |
| 20 | Normal form | Natural multiplicity, natural denominator, real absolute leading-coefficient estimate; no simp normal-form change. |
| 21 | Syntax generality | Localized hB avoids proving unrelated coefficient estimates; original uniform callers specialize at natDegree. |
| 22 | Imports | No new imports, so no added downstream fanout. |
| 23 | Casts | New hypothesis genuinely casts ℤ→ℝ. Existing h1 cast likewise necessary. hQ0 inline adds no casts; no redundant cast added. |
| 24 | Instances | n/a: theorem declares no instances and includes no effective section instances. |

## Signature packing and inequality scan

Widths count Unicode codepoints, including indentation. Width-100 `#check @...` is in the
successful final actual-constant log. First next binder has width 28; the last conclusion block
has width 89 including `:= by` and excluding its indentation.

| Signature line | Before width | Final width | Addition test | Action |
|---|---:|---:|---|---|
| theorem and R/hR/h/q/hq | 92 | 92 | 92 + 1 + 28 = 121 > 100 | ok |
| hcop/B/hB and colon | 82 | 76 | 76 + 1 + 89 = 166 > 100 | ok |
| conclusion and := by | 93 | 93 | no next signature token | ok |

| Location | Inequality | Orientation/action |
|---|---|---|
| hq | 0 < q | correct |
| old hB | ∀ n, abs coefficient ≤ B | correct; localized, not reversed |
| final hB | abs leadingCoeff ≤ B | correct |
| conclusion | q^multiplicity ≤ B | correct |
| reverse ≥/> in code | zero | no rewrite/rename needed |

## Five actual mathlib searches and replacement decision

Raw full native responses: `search.json` (each tool returned isError=false).

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | integer polynomial rational root denominator power multiplicity bounded by leading coefficient | den_dvd_of_is_root, one_le_pow_mul_abs_eval_div, rootMultiplicity and denominator-clearing building blocks. |
| B Loogle | Polynomial.rootMultiplicity, _ ≤ _ | rootMultiplicity comparisons, le_rootMultiplicity_iff, map/multiplication/roots results; no coefficient-height bound. |
| C LeanSearch | If an integer polynomial has rational root h/q with multiplicity t then q^t divides its leading coefficient | den_dvd_of_is_root, num_dvd_of_is_root, pow_rootMultiplicity_dvd, le_rootMultiplicity_iff. |
| D full source rg | pow_rootMultiplicity_le; rootMultiplicity.*(leadingCoeff\|coeff); leadingCoeff.*rootMultiplicity | No exact textual match. Also inspected full RationalRoot.lean relevant theorem/proofs and existing polynomial/Gauss factorization API. |
| E native local name | rootMultiplicity (limit 30) | Thirty real source-name matches including zero/C/powers/map/scaleRoots variants; index=unavailable, so this is not an indexed absence certificate. |

Auxiliary variants covered: multiplicity zero/powers/linear factors, multiplicity map/scaleRoots,
leadingCoeff_mul/pow/linear, rational-root denominator/numerator divisibility and Gauss primitive
factorization. No common-equivalents bucket applies. `den_dvd_of_is_root` handles the single
root divisibility assertion, not the multiplicity power plus real coefficient bound. Replacing
this theorem by that lemma would require a new substantial argument, not direct specialization.
Keep the mathematical bound built from the separately audited factorization and standard leading
coefficient/absolute-value lemmas. No new wrapper/helper is introduced. No claim of exhaustive
mathematical absence from bounded searches or an unavailable index.

Clean compiler automation is against an exact prefix ending BEFORE the audited target, with
anonymous examples, so neither target nor failed named trials can be suggested. In
`automation-clean.log`, rfl/simp/ring/linarith/nlinarith/omega/grind/aesop fail; exact? does not
close; apply? only finds unrelated partial order/power reductions and reaches the local 20k
heartbeat bound. `final-automation.log` repeats simp/lia/exact?/apply?/grind/aesop on the final
localized statement, likewise no complete proof. Local 20k bounds only REDUCE exploration
budgets; production limits unchanged. No repeated stalled full-Theta multi_attempt request:
prior consecutive-leaf stalls are documented in the dispatched instructions, and isolated ordinary
Lean compilation is the prescribed fallback. Failed search batches are not axiom evidence.

Two initial scratch issues were corrected before using definitive results: placing set_option
before imports in the first binder batch, and placing set_option after an unattached target
docstring in the first automation batch. Corrected `negative-binders.log`/`final-binders.log`
and `automation-clean.log` contain the actual definitive trials. No scratch error is silently
counted as successful verification.

## Effective binder probes and inversion check

`final-binders.lean`/`.log` compile each exact final binder deletion separately in one named
negative batch under autoImplicit=false, with the rest of the current proof unchanged. Every row
fails with the corresponding unknown identifier; these test proof dependence, not impossibility
of a different mathematical proof. Values in the conclusion cannot simply disappear.

| Binder | Role/use | Compiled candidate | Result/action |
|---|---|---|---|
| {R : Polynomial ℤ} | polynomial, leading coefficient, map, conclusion | drop | fails: dependent statement/proof needs R; retain. |
| hR : R ≠ 0 | nonzero factor Q/leading coefficient | drop | fails hR transport; retain. Zero polynomial would invalidate positive q^0 bound at B=0. |
| {h : ℤ} | rational root and coprimality | drop | fails h; retain arbitrary h, no point-localization applicable. |
| {q : ℕ} | denominator, linear factor, conclusion | drop | fails q; retain natural denominator. |
| hq : 0 < q | factorization and linear leading coefficient | drop; 0≤q; q≠0 | drop fails hq; weak nonnegative form fails factorization's strict requirement. q≠0 equivalent adapter compiles in positive-generality.log; no additional mathematical generality, retain hq. |
| hcop : IsCoprime h ↑q | primitive integral factorization | drop | fails hcop; retain reduced-fraction condition, no typeclass weakening applies. |
| {B : ℝ} | real upper bound | drop; ordered-field alternative | drop fails B. Original uniform-bound proof transfers to arbitrary Type* Field+LinearOrder+IsStrictOrderedRing (positive-generality.log exit0); this adds an abstract field and three classes without a current caller need, outside the chosen localization, not recommended API churn. |
| hB | coefficient upper bound | drop; specialize to leading coefficient | drop fails hB. weak-leading.log exit0 proves exact weaker premise; preapply.log verifies old adapter and caller before mutation; applied. |

No hidden σ/Fintype/DecEq binder occurs in the actual target type; final metadata verification
checks this. The theorem is already arbitrary in its polynomial/root/denominator. It has no named
concrete witness to unfold away, so the named-object inversion diagnostic is inapplicable. The
real missed localization was the global coefficient hypothesis; it is now point-localized to
the one coefficient used. No independent long branch or repeated coercion round-trip signals a
missing helper API.

Public literature search performed: “rational root theorem multiplicity denominator leading
coefficient Gauss lemma generalization”. Top returned sources included the rational-root theorem,
Notre Dame course notes, and Gauss's lemma. Opened and checked Emory's primary course exposition
[The Remainder, Factor, and Rational Roots Theorems](https://math.oxford.emory.edu/site/math108/rationalRoots/):
it derives denominator divisibility of the leading coefficient for a reduced rational root.
The multiplicity version is the factorization extension used here (inference from Gauss's lemma).
The project's clean.tex lines 678–700 explicitly compare leading coefficients, supporting the
implemented localization. Math second-opinion MCP is unavailable in the exposed tools; no
claim that it was consulted. No other literature-driven API change is recommended.

## All 42 golfing rules

| Rule | Status |
|---|---|
| 1.1 by exact | n/a: multi-step mathematical proof. |
| 1.2 by rfl | n/a: no reflexive proof wrapper. |
| 1.3 rw+exact→rwa | n/a: final inequality composition does not rewrite to the same goal. |
| 1.4 simp+exact→simpa | n/a: no such pair. |
| 1.5 trailing rfl | n/a: none. |
| 1.6 constructor→tuple | n/a: no constructor result. |
| 1.7 apply+exact | n/a: no such pair. |
| 1.8 by_contra! | n/a: direct proof. |
| 1.9 eta | n/a: no target lambda. |
| 1.10 inline have | applied hQ0; remove now-redundant h2 alias by rewriting hB directly. |
| 1.11 apply+intro | n/a: no function introduction. |
| 1.12 redundant show | n/a: none. |
| 1.13 have projections→obtain | existing factorization uses obtain already. |
| 1.14 merge rw | no consecutive rw without intervening cast normalization; preserve one cast bridge. |
| 1.15 terminal simp | n/a: no simp. |
| 1.16 nonterminal simp | n/a: no simp. |
| 1.17 dot notation | existing trans composition retained. |
| 1.18 <\| | no new trailing-paren proof wrapper; nested inequality/nonzero expressions are short and properly grouped. |
| 1.19 push Not | n/a: no negation normalization. |
| 1.20 trivial exists | n/a: inequality, not a witness theorem. |
| 2.1 grind whole | compiled old/final examples fail; explicit factorization necessary. |
| 2.2 delete before grind | n/a: selected proof has no grind. |
| 2.3 simpa consolidation | compiled simp on whole theorem makes no progress; no simp+closing pair. |
| 2.4 fun_prop | n/a: no analytic regularity. |
| 2.5 positivity | existing nonnegative-power subgoal closed by positivity; retain. |
| 2.6 gcongr | selected proof is integer nonzero leading coefficient plus factorization; no monotonicity calc chain. |
| 2.7 lia/omega | whole arithmetic trials fail; root multiplicity/factorization information is missing to arithmetic alone. |
| 2.8 aesop | old/final examples fail exhaustive search. |
| 2.9 norm_num/norm_cast | exact_mod_cast retained on actual ℤ→ℝ lower bound; no concrete numerical computation. |
| 2.10 decide | n/a: arbitrary polynomial/real inequality, not closed finite computation. No native_decide. |
| 2.11 field_simp;ring | n/a: no denominator identity to prove. |
| 2.12 linear_combination | n/a: no ring/ring_nf termination; theorem concerns absolute values and an integer nonzero lower bound. |
| 2.13 wlog | n/a: no symmetric cases. |
| 2.14 two-step calc | existing composed .trans is already direct. |
| 2.15 <;> | n/a: no repeated subgoals. |
| 3.1 erw→rw | n/a: only rw. |
| 3.2 continuity→fun_prop | n/a: none. |
| 3.3 omega→lia | target has no omega; final whole lia trial fails. |
| 3.4 rcases rfl | n/a: factorization witness not an equality substitution case. |
| 3.5 automation attributes | no new global attributes: this substantial bound has explicit hypotheses and no canonical simp rewrite. |
| 3.6 simp_all | n/a: no simp_all. |
| 3.7 remove limits | none present/introduced. |

## Step back, simplify, and correctness evidence

The proof factors off the primitive rational-root linear polynomial over ℤ, compares leading
coefficients, uses the nonzero integer cofactor's absolute leading coefficient ≥1, and casts the
single inequality to ℝ. This is the mathematical structure; compression by generic automation
lost the factorization information. No independent helper is warranted for a 12-line proof.

Simplify pass: the built-in /simplify tool is unavailable in this environment; performed its
scoped holistic review directly. Outcome ISSUES-FOUND-AND-FIXED: localize hB and remove the
redundant hQ0/bound aliases. No duplication or additional helper extraction remains.
Phase 3 file-wide fixes, 5a unrelated refactoring and 5b rename pass are out of this single-leaf
ownership. Renames queued: none; shared logs/queues/Git never mutated.

Preapply evidence: `preapply.lean` and `preapply.log`, exit 0. Recompiles independent original
Index+Theta through Θ_unique_le, the concrete candidate target/caller, the full original uniform
coefficient adapter, and proof-irrelevance equalities at the complete old target and caller types.
Both candidate adapter and candidate caller have only [propext, Classical.choice, Quot.sound].

Verification scaffolding corrections: the first strict caller-name comparison correctly found synthetic
instance-name differences from the isolated original namespace. The final comparison exempts only
anonymous instImplicit generated names, as required by the leaf instructions; explicit user names,
class types/order/BinderInfo remain protected. A subsequent ambiguous short `.instImplicit` name
was qualified as `Lean.BinderInfo.instImplicit`. Only the final exit-0 verifier is evidence.

New-identifier check: no mathematical identifier absent from the released proof is introduced.
`R1.natDegree` at the caller is the existing Polynomial API; it is elaborated by preapply and module
build, not an unverified guessed lemma.

Final gates, timings, hashes, and exact actual-constant evidence are recorded below after the
sequential requests complete. Owner's final whole project build and separate LeanEval are pending
for this leaf; preceding checkpoint's builds do not certify the edited source.

## Final actual-constant and diagnostic gates

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | `/Users/ramin/.elan/bin/lake build Roth.Theta`, exit 0, all 2423 jobs; `module-build.log`. |
| full live LSP | pass | Native lean_diagnostic_messages, complete unfiltered Theta file, success=true, partial=false, timed_out=false, failed_dependencies=[], zero errors/18 existing warnings; `final-lsp.json`. No target warnings. |
| definition protection | pass | No def/abbrev/import change in released-source diff (`change.diff`). |
| theorem statement protection | pass, authorized localization | Only selected hB domain weakened; expectedNew.type checked exactly against actual built type, all other domains and conclusion literal AST equality, full old uniform-hB adapter.type checked against immutable original.type. |
| original independent proof | pass | `actual-original.lean` recompiles immutable original Index+Theta through Θ_unique_le; `immutable-source-check.json` confirms target/caller original blocks byte-identical to 2b64544. AST checks reject using the current target to prove its own original. |
| caller contract | pass | Actual built Θ_unique_le type definitionally equals independent immutable complete original type; same named binders/order/BinderInfo. Only generated anonymous instImplicit names exempted; exact class domains/retained order checked. Original DecEq retained. |
| actual standard axioms | pass | Final `actual-original.log`, exit 0: original/current target, oldUniformAdapter, expectedNew, original/current caller each use exactly [propext, Classical.choice, Quot.sound]. Failed scratch runs never used for this gate. |
| structure | pass | 12 proof lines; no conjunction conclusion/long case branch/new production helper. |
| naming | pass | No forbidden pattern; no rename needed. |
| line packing | pass | Complete measured three-line table above. |
| inequality orientation | pass | Complete occurrence table above, zero reversed inequalities in code. |
| comments/docs | pass | All original source text/quote preserved, authorized clarification added; zero inline narrative lost. |
| limits/scaffolding | pass | No production sorry/axiom/native_decide/raised limit/profile scaffolding introduced. |
| caller coverage | pass | Full untruncated repository rg finds only declaration and Θ_unique_le call; module and final complete LSP check the adaptation. |
| full project / separate LeanEval | owner pending | This worker does not run the owner's frozen sequential final gates. |

Successful preapply adapter/candidate file: `/private/tmp/roth-rootmult-bound/preapply.lean`.
Definitive post-build actual constants/adapters: `/private/tmp/roth-rootmult-bound/actual-original.lean`.
Definitive exit-0 log: `/private/tmp/roth-rootmult-bound/actual-original.log`.

| Added identifier/expression | Verification | Result |
|---|---|---|
| No new mathematical lemma names | Released-source focused diff | pass |
| Caller specialization `hcoef R1.natDegree` | preapply exit0 + actual module build + actual-original exit0 | pass |

Overall worker correctness gates: pass. Owner publication/build gates remain pending.

## Required phase checklist

- [✓] Step 1 — all required reference documents read.
- [✓] Step 2 — substantive full 24-item audit recorded.
- [✓] Step 2.5 — all five actual mathlib search methods recorded with honest limitations.
- [✓] Step 2.6 — each effective parameter drop compiled; applicable weakening/localization probes compiled; public literature and inversion checks recorded.
- [✓] Step 2.7 — measured full signature line-packing table recorded.
- [✓] Step 2.8 — per-occurrence inequality scan recorded.
- [✓] Step 3 — all 42 golfing rules have explicit findings.
- [✓] Step 4 — mathematical strategy and holistic simplify review completed.
- [✓] Step 5a — fresh complete unfiltered final live LSP passes; no target diagnostics.
- [✓] Step 5b — module/protection/structure/naming/packing/inequality/caller/original-type/axiom gates pass; only owner's subsequent project gates remain pending.
- [✓] Step 6a — no rename needed; shared sidecars untouched.

## Buzz pass: exact-prefix performance

Outcome: FAST-BOARD (both affected declarations remain below the 1000ms budget). This is not a
speedup claim. Both baseline and final caller measurements ≥750ms were repeated uncontended.
All commands exited 0 and used the real Lean 4.34 options:

`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 FILE`

`baseline-prefix.lean` ends after the target. `baseline-caller-prefix.lean` and `final-prefix.lean`
end after Θ_unique_le, preserving the exact respective preceding source/imports/section context.
Final profiles ran only after all module, exploration, compatibility and native LSP requests had
completed, with no concurrent compiler/LSP request. Repeated baseline/final profiles were likewise
sequential and uncontended. These are prefix-only timings; owner's final whole-module profile
sweep remains required after the later declarations are cleaned.

The total sums the outer command and associated top-level async proof, kernel/addDecl and linter
roots. Nested tactic/kernel/linter nodes are not double-counted. No compiler root is emitted for
these Prop-valued theorems.

| Raw UTF-8 log | Declaration | Outer ms | Proof ms | Kernel async ms | Linter ms | Total ms | Anchor lines (outer/proof/kernel/linter) |
|---|---|---:|---:|---:|---:|---:|---|
| baseline-profile.log | pow_rootMultiplicity_le | 34.293 | 219.790 | 7.262 | 12.350 | 273.695 | 259009/261512/288857/288859 |
| baseline-caller-profile.log | pow_rootMultiplicity_le | 30.445 | 240.131 | 7.930 | 12.733 | 291.239 | 259211/261715/289149/289151 |
| baseline-caller-profile.log | Θ_unique_le | 36.559 | 672.828 | 26.698 | 20.949 | 757.034 | 289211/290667/451422/451424 |
| baseline-caller-profile-repeat.log | pow_rootMultiplicity_le | 28.127 | 247.694 | 7.054 | 12.818 | 295.693 | 259318/261822/289165/289167 |
| baseline-caller-profile-repeat.log | Θ_unique_le | 35.655 | 683.631 | 29.011 | 23.116 | 771.413 | 289227/290676/450830/450832 |
| final-profile.log | pow_rootMultiplicity_le | 30.430 | 300.331 | 9.285 | 12.496 | 352.542 | 259335/261642/304795/304797 |
| final-profile.log | Θ_unique_le | 29.535 | 738.667 | 26.926 | 25.675 | 820.803 | 304857/306310/467204/467206 |
| final-profile-repeat.log | pow_rootMultiplicity_le | 23.367 | 322.156 | 8.983 | 11.568 | 366.074 | 259321/261627/304861/304863 |
| final-profile-repeat.log | Θ_unique_le | 29.598 | 725.683 | 31.489 | 42.239 | 829.009 | 304923/306376/467241/467243 |

Machine-readable totals/anchors: `timings.json`; parser: `parse_profiles.py`.
Accepted repeated final: target **366.074ms**, routine caller **829.009ms**.
No over-budget declaration in this leaf; no speed-driven rewrite/helper/limit raise is needed.
maxHeartbeats raises removed: 0; added: 0. Deferred over-budget items: none. No profile scaffolding
in production. No new production helper requires a fresh follow-up audit.

## Freeze and handoff

Source frozen; worker revokes further source edits. All compiler/native/profile requests drained.
Only the dedicated report and scratch evidence were written in addition to the scoped source edits.
No Git/shared queue/shared log mutation. Owner must still perform the frozen full project build,
then separate Roth.LeanEval, publish/push, and eventual cumulative whole-module profile sweep.

Final source SHA256: `f72be18abfb0dc5a92007ff55716548b9dd3dae4da799406e1902a49856521a7`.
Total source line delta: 974 → 974 (0); target proof 13 → 12 (−1), documentation +1.


## Owner cumulative publication gates

After leaf source revocation and drained requests, owner ran full `lake build` (77.364 s),
then separate `lake build Roth.LeanEval` (24.504 s); both exit0. All 17 project/source/pin
hashes remained identical through both commands. Theta SHA256 `f72be18abfb0dc5a92007ff55716548b9dd3dae4da799406e1902a49856521a7`.
Raw logs: `/private/tmp/roth-theta-d19-full.log`, `/private/tmp/roth-theta-d19-leaneval.log`; machine record
`/private/tmp/roth-theta-d19-builds.json`. These completed gates supersede pending owner
entries above. Exact-path staging, commit and successful push publish this checkpoint before
the next original declaration edit. After publication: Theta 19/35, overall 200/264 original
declarations, 9/14 completed files. No new production helper.
