# Dedicated original16 audit: `Roth.isPrimitive_linear`

Scope: only this private declaration in `Roth/Theta.lean`, plus verification of its sole public caller `exists_eq_pow_mul_of_rootMultiplicity`. Immutable original: `2b64544bf9f77a8ff957bf1bcaf693ac72217ff6`. Starting checkpoint: `f9be46d32024200bf5cff25fbacf26d7b2625773`; starting Theta SHA256 `a7fc4b6f10bab79a35f6cf20b34870fdcde77e44a79c7fd151c3e5ba10f0c8bd`.

The proof says that every common divisor of the coefficients of `qX-h` divides both `h` and `q`, and is therefore a unit. Removed the definitional rewrite of `IsPrimitive` and inlined the two once-used coefficient facts. Body: 9 → 5 lines; no new helper, imports, attributes, names, visibility, definitions, statements, or documentation changes. All original inline comments/docstrings remain untouched (none in the audited proof).

Artifacts are under `/private/tmp/roth-primitive-linear/`. Required references were read in full: both SKILL.md files, cleanup workflow, golfing-rules, proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates, style-rules, naming-conventions, profiling. Preparation obeyed the read-only embargo; compilers/searches/edits began only after explicit RELEASE.

## Baseline and full audit

Owner supplied clean sequential full build (68.560s) then separate LeanEval (31.179s), both exit0 at the starting checkpoint. Reused the matching-hash complete baseline LSP `/private/tmp/roth-mono-api/final-lsp.json`: success=true, partial=false, timed_out=false, failed dependencies empty; zero errors, 19 existing warnings. Cache retrieval unnecessary. No target-specific lint finding.

| # | Audit item | Concrete finding/action |
|---|---|---|
| 1 | Lint | No warning in audited range; existing module warnings outside scope. |
| 2 | Have scan | `h1 := hc 1` used once in final coprimality application; `h0 := hc 0` likewise; both inlined with coefficient normalization at the use site. |
| 3 | Options | No declaration options; no limits raised. |
| 4 | Simp | Original nonterminal `simp only` normalized two hypotheses. Final constant-coefficient `simpa` is unsqueezed. Linear-coefficient plain `simpa` and `simpa [Polynomial.coeff_C]` failed due to integer-cast simplification; the verified explicit coefficient normalizations remain necessary. |
| 5 | Naming | `isPrimitive_linear` describes a primitive linear polynomial using mathlib's `IsPrimitive` terminology; no forbidden abbreviation, number scheme, `_ge_`/`_gt_`, or numbered aux. No rename. |
| 6 | Packing | Two signature lines measured below; neither can absorb the next expression. |
| 7 | By placement | `by` remains at the end of the conclusion line. |
| 8 | Format | Two-space tactic indent; no blank proof lines, sequential `rw`, semicolon chains, haveI/letI, or trailing whitespace introduced. |
| 9 | Comments | None in proof; all file narratives protected and unchanged. |
| 10 | Docstring | Private declaration has none; caller's original docstring unchanged. |
| 11 | Visibility | Already private; remains private. Classic import dialect. |
| 12 | Structure | Five-line proof, no conjunction conclusion, branches, or independent block needing extraction. |
| 13 | Mathlib | Five actual methods and clean nonself `exact?`/`apply?` probes below; no direct replacement found. Builds on existing coefficient divisibility and coprimality APIs. |
| 14 | Junk definition | n/a: theorem, no data definition. |
| 15 | Existential helper | n/a: no existential conclusion or witness wrapper. |
| 16 | Show/change | None. Direct introduction unfolds the definitional predicate. |
| 17 | Push negation | None. |
| 18 | Generalisation | Every effective binder inspected and compiled probes below. Private scope exempts literature; arbitrary CommRing and IsRelPrime alternatives assessed. No private API widening recommended solely because possible. |
| 19 | Inequality | No inequality in signature or body; table below. |
| 20 | Normal form | Standard `Polynomial.IsPrimitive` conclusion and `IsCoprime` hypothesis; no custom predicate. |
| 21 | Syntactic generality | Existing implicit h/q and explicit hcop serve sole caller directly; no rebundling improves it. |
| 22 | Import fanout | n/a: no import added. |
| 23 | Casts | Retained `q : ℕ` to ℤ is a genuine cross-type coefficient cast; no redundant cast introduced/dropped. |
| 24 | Instance naming | n/a: no instance declaration or local instance. |

## Five-method mathlib search

Actual raw results: `search-finder.json`, `search-loogle.json`, `search-leansearch.json`, `search-local.json`.

| Method | Actual query / search | Result |
|---|---|---|
| A Lean-Finder | polynomial a X plus b primitive if coefficients coprime | `irreducible_C_mul_X_add_C`, `irreducible_of_degree_eq_one_of_isRelPrime_coeff`, `IsPrimitive`, `Monic.isPrimitive`, `isPrimitive_primPart`. Irreducibility route needs nonzero leading coefficient, absent here (q=0 is valid when h is a unit). No exact primitive-linear lemma returned. |
| B Loogle | `Polynomial.IsPrimitive, Polynomial.C, Polynomial.X` | Empty items, no tool error; this alone is not an absence claim. |
| C LeanSearch | a linear polynomial is primitive if its two coefficients are coprime | Same irreducibility routes, primitive divisor/content characterizations. |
| D Source rg | untruncated primitive linear/C_mul_X/X_mul/sub_C/add/sub patterns in Polynomial; full `isPrimitive_linear` and primitive/coprime patterns across mathlib | No exact matching declaration; read Content.lean definition and primitive API and Coprime/Basic.lean `isUnit_of_dvd'`/`isRelPrime`. |
| E Local name | `isPrimitive`, limit60 | Primitive polynomial APIs plus local target and unrelated roots/characters. Index reported unavailable; positive textual results useful, empty index cannot establish absence. Local target was excluded from proof-search environment. |

Auxiliary variants checked: linear, C_mul_X, X_mul, sub_C, add/sub, `.Monic.isPrimitive`, `Irreducible.isPrimitive`, `_iff_isUnit_of_C_dvd`, `_iff_content_eq_one`, `_of_dvd`, coprime/relative-prime. Common-equivalents table has no matching bucket. Clean anonymous automation examples live in exact source prefix ending BEFORE the target, not an import of Theta: `search-probes.lean`/`.log`. `grind`, `aesop`, `simp` fail; `exact?` fails; `apply?` returns only partial Monic/Irreducible/content/divisor obligations and leaves holes. Expected-failure exit1 is not verification. No failed named declaration or current target can contaminate those suggestions. Native multi_attempt was not repeated because the prescribed bounded fallback follows documented earlier session stalls. Conclusion: partial API match, retain focused proof using existing APIs; no claim that search proves global absence. No new public API extraction is warranted by this short coefficient argument.

## Effective parameter probes and inversion

| Effective parameter | Use | Compiled drop/weakening probe | Result |
|---|---|---|---|
| `{h : ℤ}` | Constant coefficient and coprimality | Removing binder with autoImplicit=false; arbitrary `{h : R}` with CommRing R | Negative file rejects unknown h; generic candidate compiles. Data cannot be omitted from this dependent statement. |
| `{q : ℕ}` | Linear coefficient and coprimality | Removing binder with autoImplicit=false; replace natural q with arbitrary `{q : R}` | Negative file rejects unknown q; generic CommRing candidate compiles, covering q:ℤ as specialization. No scope-driven reason to widen this private helper. |
| `(hcop : IsCoprime h (q : ℤ))` | Unit common-divisor conclusion | Drop; replace IsCoprime by IsRelPrime in arbitrary CommRing | Drop leaves IsUnit c unsolved; relative-prime alternative compiles. This is an equivalent formulation over ℤ; keep sole caller's existing convenient hypothesis. |

`negative.lean`/`.log` is expected-failure exit1 and includes only dependency/drop failures, not verification. `general.lean`/`.log` and `relative.lean`/`.log` are independent positive candidates, each exit0 with standard axioms. The effective original telescope has only these three binders: σ/Fintype/DecidableEq section variables do not occur in it; actual-constant verification checks this, rather than assuming it from visible source. Universe polymorphism not relevant to the fixed integer statement; the assessed generic candidate is universe-polymorphic.

Literature: n/a, private declaration under the explicit workflow exemption. Inversion: polynomial qX-h is concrete, but the argument is coefficient-generic after opening IsPrimitive. The compiled arbitrary CommRing/relative-prime candidate establishes that abstraction is possible; no second helper or public API is introduced for this single use. No positivity or strict inequality assumptions exist to weaken.

## Measured signature packing and inequality orientation

Original and final signature identical, at final L162–163. Reference is the actual built constant type printed by verification (three effective binders).

| Signature line | Codepoints | Next full expression | Arithmetic | Action |
|---|---:|---|---|---|
| 162 | 79 | `(Polynomial.C (q : ℤ) * Polynomial.X - Polynomial.C h).IsPrimitive := by` (72) | 79+1+72=152>100 | ok |
| 163 | 76 | none, proof next | n/a | ok |

| Occurrence | Location | Original | Rewrite / rename |
|---|---|---|---|
| none | Entire signature and proof | No ≥ or > | n/a; no orientation rename |

## All 42 golfing rules

| Rule | Status |
|---|---|
| 1.1 by exact | n/a: no sole wrapper. |
| 1.2 by rfl | n/a: no rfl proof. |
| 1.3 rw+exact→rwa | n/a: rewrite changes divisor hypothesis, not goal for subsequent exact. |
| 1.4 simp+exact→simpa | Applied by normalizing coefficients inside the final application. |
| 1.5 trailing rfl | n/a: none. |
| 1.6 anonymous constructor | n/a: no conjunction constructor. |
| 1.7 apply+exact | n/a: already exact application. |
| 1.8 by_contra! | n/a: no contradiction. |
| 1.9 eta reduction | n/a: no lambda. |
| 1.10 inline have | Applied to both h0 and h1. |
| 1.11 refine+fun | n/a: no apply/intro pair. |
| 1.12 redundant show | n/a: none; redundant IsPrimitive iff rewrite removed instead. |
| 1.13 obtain projections | n/a: no projected pair. |
| 1.14 merge rewrites | n/a: only one rewrite remains. |
| 1.15 terminal simp unsqueeze | Tried, succeeds for coefficient0 but fails for coefficient1; explicit normalization retained there. |
| 1.16 nonterminal simp squeeze | Original explicit list already squeezed; final simpa uses explicit needed normalization. |
| 1.17 dot notation | Retained `hcop.isUnit_of_dvd'`. |
| 1.18 <\| | n/a: ordinary two coefficient proof arguments, no outer trailing function parenthesis. |
| 1.19 push Not | n/a: no negation tactic. |
| 1.20 existential inline | n/a: not existential. |
| 2.1 grind whole proof | Actual clean prefix probe fails. |
| 2.2 delete before grind | n/a: no grind in selected proof. |
| 2.3 simpa consolidation | Applied directly to coefficient applications. |
| 2.4 fun_prop | n/a: no analytic function-property goal. |
| 2.5 positivity | n/a: no sign/nonzero structural goal. |
| 2.6 gcongr | n/a: no inequality/monotonicity. |
| 2.7 lia/omega | n/a: algebraic divisibility, no linear arithmetic. |
| 2.8 aesop | Actual clean prefix probe exhausts without proof. |
| 2.9 norm_num/cast | n/a: symbolic polynomial/common-divisor statement, not numerical evaluation. |
| 2.10 decide | n/a: no finite computation, unbounded symbolic integers. |
| 2.11 field_simp/ring | n/a: no denominators or equality goal. |
| 2.12 linear_combination | n/a: no ring/ring_nf ending or equality hypotheses. |
| 2.13 wlog | n/a: no symmetric branches. |
| 2.14 collapse calc | n/a: no calc. |
| 2.15 <;> | n/a: coefficient0 and coefficient1 require distinct normalizations. |
| 3.1 erw→rw | n/a: no erw. |
| 3.2 legacy function tactics | n/a: none. |
| 3.3 omega→lia | n/a: neither. |
| 3.4 rcases rfl | n/a: no cases. |
| 3.5 attributes | No global attribute addition justified for this private single-use fact. |
| 3.6 simp_all | n/a: no simp_all only, direct applications shorter and controlled. |
| 3.7 remove limits | n/a: no limits present/added. |

Step back: searched exact/apply, tried whole-proof grind/aesop/simp, checked general abstract strategy, and compared term composition. Direct introduction plus coefficient divisibility is clearer and smaller than the original two temporary facts; no additional helper or public statement churn improves the caller. Holistic simplify pass: PASS-THROUGH after these changes; no duplicate skeleton or further worthwhile composition found. Built-in Skill dispatch is unavailable in this host; its review was performed in-thread, not claimed as an invoked external tool.

## Verification and performance

`/Users/ramin/.elan/bin/lake build Roth.Theta` (session82194) exited0, ending “Build completed successfully (2423 jobs).” The actual built private constant was programmatically located as `_private.Roth.Theta.0.Roth.isPrimitive_linear`. `verified.lean` imports the rebuilt Theta, independently replays the immutable original helper, power helper and complete original public caller proof in `PrimitiveLinearOriginal`, compares actual types by definitional equality and full binder names/order/BinderInfo, and traverses the actual constants’ axiom sets. Corrected compiler session51005 exited0. Both independent originals and both actual built constants use exactly `[propext, Classical.choice, Quot.sound]`. The actual private telescope has h/q implicit and hcop explicit, with no σ or section instances. The caller retains its full old R/hR/h/q/hq/hcop contract, including `hR : R ≠ 0`; no future hR removal was applied.

Fresh native `lean_diagnostic_messages` on the COMPLETE unfiltered live Theta returned success=true, partial=false, timed_out=false, failed_dependencies=[]; zero errors and 19 existing warnings, none at the private target. Raw response `final-lsp.json` is complete. No new warning and no sorry/axiom/limit/profiling scaffolding was introduced. New-identifier verification: the diff only reuses original coefficient lemmas and `hcop.isUnit_of_dvd'`; there is no newly introduced library identifier to verify.

All ordinary search/build/compiler/LSP requests completed and were drained before the final profile began. Prefix source is exact through the target, followed only by the two closing ends. This is prefix-only timing: no claim that whole Theta’s profiled compilation passes (known later index_le_lem6 default-heartbeat failure); the owner’s final whole-module performance sweep remains separate.

Final source SHA256, frozen before final profiling: `8527a06d9d0b2b9626ca96d23f57bceefbac4c47b96ecfe80551a3be8a1d6aa8`. After source freeze only this report and scratch verification artifacts were written. Exact-prefix baseline/final raw UTF8 logs and timing totals are recorded below. Owner full project and separate LeanEval final gates remain pending and are not claimed here.

Initial exploration corrections: bare `simpa` (including `[Polynomial.coeff_C]`) on the linear coefficient failed because default integer-cast simplification obscured the coefficient-of-C expression; the explicit verified coefficient rewrite list fixes it. The first verifier-only metaprogram used reserved local token `matches` and failed parsing; corrected to `foundConstants`. The failed diagnostic is retained separately as `verifier-initial-failure.txt`; only the corrected final exit0 certifies the actual declarations. No production source change arose from either correction.

### Buzz pass: FAST-BOARD

Both real commands exited0, run separately with no outstanding ordinary compiler/LSP requests and no owner compiler overlap:

```
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/roth-primitive-linear/baseline-prefix.lean
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/roth-primitive-linear/final-prefix.lean
```

Raw logs: `baseline-profile.log` and `final-profile.log`; exact declaration source anchor L162, `private lemma isPrimitive_linear`; temporary compiled name `_private._stdin.0.Roth.isPrimitive_linear` (actual module constant independently verified above). The inner macro-expanded `private theorem` command is nested within the outer `private lemma` command and is not added twice. AddDecl async totals include their nested kernel/compiler work; nested Kernel rows are not added again.

| Target component | Baseline ms | Final ms |
|---|---:|---:|
| Outer private lemma command | 24.403 | 23.685 |
| Associated asynchronous proof | 58.763 | 126.813 |
| Associated helper/main AddDecl kernel/compiler totals | 0.146+0.179+7.232 | 0.163+9.233 |
| Associated target linter | 5.492 | 4.794 |
| Total including linter | **96.215** | **164.688** |

No speedup is claimed: the final proof is smaller and clearer but measured 68.473ms slower under verbose profiling. Both totals are below 750ms, so no borderline repeat is required; both comfortably meet the 1000ms budget. No raised heartbeat/recursion limits or profiling source scaffolding; zero performance deferrals. Whole-file profiling remains the owner's cumulative responsibility.

### Final diff gates

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | PASS | Actual `lake build Roth.Theta`, session82194, exit0; module-build.log. |
| complete live LSP | PASS | Native complete unfiltered final-lsp.json, success=true/partial=false/timed_out=false/no failed deps; 0 errors, 19 existing warnings. |
| definition_protected | PASS | No definition or abbrev change. |
| theorem_statement_protected | PASS | Actual private original type and binders equal; sole public caller full original type and binders equal. Source signature byte-identical. |
| standard axioms | PASS | Corrected verified.lean, session51005, exit0; actual and independent original private/public constants checked. |
| structure | PASS | 5 proof lines; no conjunction or long branch. |
| naming | PASS | Mathematical name; no forbidden pattern; no rename. |
| line packing | PASS | Full two-line measured table above. |
| inequality orientation | PASS | Full scan above, no reversed inequality. |
| unintended caller change | PASS | Entire source before target and after target identical to starting snapshot; caller independently proved and actual contract checked. |
| simplify | PASS-THROUGH | In-thread holistic review completed; no further worthwhile refactoring. |
| buzz | FAST-BOARD | Real exact-prefix target totals96.215→164.688ms; both exit0, budget1000ms. |
| owner full build / LeanEval | PENDING OWNER | Not performed or claimed by this leaf; owner runs them sequentially after handoff. |

`git diff --check -- Roth/Theta.lean` exited0. Frozen SHA256 rechecked unchanged: `8527a06d9d0b2b9626ca96d23f57bceefbac4c47b96ecfe80551a3be8a1d6aa8`.

Phase5a: no non-rename refactoring beyond the approved local proof simplification. Phase5b: no rename proposed or queued; no shared queue/log/Git writes. No new helper requiring later audit. No remaining recommendation or undecidable question. Comments-preserved: none in target; all file comments unchanged. Declaration reduction: 9→5 proof-body lines (-4); total source delta -4 lines.

### Eleven-step checklist

- [x] Step1: full required references read.
- [x] Step2: all24 substantive audit items reported.
- [x] Step2.5: five actual mathlib searches and clean compiled nonself search probes recorded.
- [x] Step2.6: all three effective binders classified; compiled drop/generic/relative alternatives recorded; private literature exemption and inversion check explicit.
- [x] Step2.7: every signature line measured in codepoints.
- [x] Step2.8: full inequality occurrence scan table.
- [x] Step3: all42 golfing rules have concrete status.
- [x] Step4: whole-proof automation, exact/apply, composition and alternative strategy reconsidered.
- [x] Step5a: fresh complete unfiltered native final diagnostics clean of errors.
- [x] Step5b: actual module, diff, independent-original/actual-constant/caller/axiom, simplify and real profile gates recorded.
- [x] Step6a: rename action n/a; none needed, no shared-sidecar write authorized or made.

Source edits permanently revoked at the recorded freeze. All compiler/native requests and profiling sessions completed; no tools left running. Only this dedicated report was finalized after the timing run. Owner final full project and separate LeanEval gates remain explicitly pending.


## Owner cumulative publication gates

After leaf source revocation and drained requests, owner ran full `lake build` (62.585 s),
then separate `lake build Roth.LeanEval` (23.065 s); both exit0. All 17 project/source/pin
hashes remained identical through both commands. Theta SHA256 `8527a06d9d0b2b9626ca96d23f57bceefbac4c47b96ecfe80551a3be8a1d6aa8`.
Raw logs: `/private/tmp/roth-theta-d16-full.log`, `/private/tmp/roth-theta-d16-leaneval.log`; machine record
`/private/tmp/roth-theta-d16-builds.json`. These completed gates supersede pending owner
entries above. Exact-path staging, commit and successful push publish this checkpoint before
the next original declaration edit. After publication: Theta 16/35, overall 197/264 original
declarations, 9/14 completed files. No new production helper.
