# `aeval_X_none_ne_zero` — original declaration 15

Initial audit recorded before source edits. Baseline HEAD `9d78cdf`; 559 lines, 24 retained declarations. Private helper at lines 131–135, exact uses at 199 and 212. Source-wide project rescan and mathlib search confirmed these two necessary callers. Parent owns Git, public proposals and cumulative gates.

## Initial substantive audit (24 items)

| Item | Finding/action |
|---|---|
| 1 Lint | Complete native baseline: 0 errors, 31 existing warnings; none on helper. |
| 2 Have scan | No `have`. |
| 3 Options | None. |
| 4 Simp squeeze | No simp. |
| 5 Naming | Descriptive snake case, no banned pattern; private wrapper deletion supersedes `_aux` rename. |
| 6 Packing | Original signature table below; deletion eliminates it. |
| 7 By | At signature end. |
| 8 Format | Two-space proof indentation, no blank proof lines. |
| 9 Comments | No helper comments; preserve all caller narratives/docs. |
| 10 Docstring | None, appropriate for private helper. |
| 11 Visibility | Private, only two local uses. |
| 12 Structure | Two proof lines, no conjunction/branches. |
| 13 Mathlib | Found direct `Polynomial.toMvPolynomial_injective`; delete helper, specialize via `map_ne_zero_iff` at two callers. Native independent example compiled. |
| 14 Junk def | Not a definition. |
| 15 Exists | No existential. |
| 16 Show/change | No show. |
| 17 Push neg | None. |
| 18 Generalise | Every effective binder probed below; mathlib already has arbitrary-variable generality. |
| 19 Inequality | No `≥` or `>` in statement/hypotheses. |
| 20 Normal form | Canonical zero-preserving injective hom consequence. |
| 21 Syntax generality | Use mathlib hom/injectivity directly at caller. |
| 22 Imports | No added import. |
| 23 Casts | Existing `X none` type annotation supplies polynomial coefficient/variable types; caller replacement introduces no coercions/ascriptions. |
| 24 Instance name | Not an instance. |

| Signature line | Codepoints | Next complete signature unit | Arithmetic/action |
|---|---:|---|---|
| 132 | 68 | conclusion (`Polynomial.aeval … ≠ 0 := by`, 65) | 68 + 1 + 65 = 134 > 100; break required |
| 133 | 69 | proof follows | final signature line |

| Inequality occurrence | Location | Result |
|---|---|---|
| None | Entire target signature and hypotheses | No orientation change |

Five actual native search methods: Lean Finder returned `Polynomial.toMvPolynomial_injective`; Loogle query `Polynomial.toMvPolynomial, _ ≠ 0` returned empty; LeanSearch returned `Polynomial.toMvPolynomial`/`MvPolynomial.aeval_toMvPolynomial`; source grep found injectivity and `_inj` at Equiv.lean 897/903; local name search returned these same symbols (index warming, positive source-backed hits). Raw complete native results including baseline diagnostics: `/private/tmp/roth-separation-d15-search.json`. Auxiliary variants `_inj`, `_injective`, `map_ne_zero_iff` checked in native snippet; generic `ZeroHomClass` route compiles. Common-equivalents lookup: no matching geometric bucket; ordinary injective zero hom is the canonical abstraction. Literature: explicit private-declaration exemption; no public theorem statement is changed.

Action: authorized removal of this private wrapper and exactly two necessary proof-term substitutions; no new helper, public API or documentation changes.


## Generalisation: every effective binder

| Binder | Probe | Result |
|---|---|---|
| `τ : Type*` | Arbitrary `σ : Type*` and `i : σ` replacing `Option τ`/`none` | Compiled native independent example; mathlib already supplies this abstraction. Universe polymorphism already present. Dropping the index type with autoImplicit false gives unknown τ (native drop-names probe). |
| `R : Type*` | Universe-polymorphic throughout; coefficient type follows `V` and codomain | Actual drop with autoImplicit false rejects unbound R; no monomorphic universe restriction to remove. |
| `[CommSemiring R]` | Parent `[Semiring R]`; drop entirely | Actual native rejected probes: missing `CommSemiring R` for aeval; missing `Semiring R` for `Polynomial R`. Raw `/private/tmp/roth-separation-d15-binder-negative.json`. |
| `{V : Polynomial R}` | Implicit type inferred from hV and target; retain arbitrary V | A dropped explicit binder can be silently auto-implicit in Lean; that is not evidence of removal. Independent example quantifies V with no extra restrictions. Actual drop with autoImplicit false rejects unknown V. |
| `(hV : V ≠ 0)` | Drop hypothesis | Compiler-verified refutation of `∀ V, aeval (X none) V ≠ 0` by specialization to zero, in independent probe. Thus indispensable. No ordered structure exists for a strict-to-weak replacement. |
| `[Fintype τ]` | Omitted in exact independent original statement | Compiled without this instance. Already omitted by helper; public caller menu remains pending. |
| `[DecidableEq τ]` | Omitted in exact independent original statement | Compiled without this instance. Already omitted by helper; public caller menu remains pending. |

Inversion check: the concrete `none` specialization is exactly the arbitrary-index mathlib injectivity theorem; delete the private specialization. No new abstraction/helper required. Native isolated exact ORIGINAL statement/non-self proof and zero counterprobe are saved as `/private/tmp/roth-separation-d15-independent.lean` and `.json`; only standard axioms.

## All 42 golfing rules

| Rule | Concrete result |
|---|---|
| 1.1 | No by-exact wrapper; replacement at caller is a direct term. |
| 1.2 | No by-rfl. |
| 1.3 | Original already uses rwa; replaced by existing injectivity API. |
| 1.4 | No simp plus exact. |
| 1.5 | No trailing rfl. |
| 1.6 | No constructor. |
| 1.7 | No apply/exact pair. |
| 1.8 | No by_contra/push_neg. |
| 1.9 | Original injectivity lambda is not eta-reducible; removed with wrapper. |
| 1.10 | No have. |
| 1.11 | No apply/intro. |
| 1.12 | No show. |
| 1.13 | No have projections. |
| 1.14 | Original one rwa; no consecutive rewrites. |
| 1.15 | No terminal simp only. |
| 1.16 | No nonterminal simp. |
| 1.17 | Caller `.2 hV` uses projection directly. |
| 1.18 | Parentheses necessary around argument passed to degreeOf_mul_eq. |
| 1.19 | No push_neg. |
| 1.20 | Not existential. |
| 2.1 | Native grind attempted and failed to prove nonzeroness. |
| 2.2 | No existing grind prefix. |
| 2.3 | No simp/concluding tactic chain. |
| 2.4 | No function regularity predicate. |
| 2.5 | Native positivity attempted, failed to prove nonzeroness. |
| 2.6 | No ordered inequality/monotonicity goal. |
| 2.7 | No integer/natural arithmetic proposition. |
| 2.8 | Native aesop attempted, failed at nonzero contradiction. |
| 2.9 | No concrete arithmetic/casts. |
| 2.10 | Arbitrary semiring polynomial nonzero is not finite computation. |
| 2.11 | No division. |
| 2.12 | No ring/ring_nf endpoint. |
| 2.13 | No symmetric branches. |
| 2.14 | No calc. |
| 2.15 | No multiple goals. |
| 3.1 | No erw. |
| 3.2 | No continuity/measurability. |
| 3.3 | No omega. |
| 3.4 | No rcases/rfl substitution. |
| 3.5 | Removed duplicate private specialization; no automation attribute needed. |
| 3.6 | No simp_all. |
| 3.7 | No heartbeat or recursion options. |

Step back: native simp and exact? did not close; apply? produced partial suggestions. Native multi-attempt replaces only one tactic line here, leaving the original continuation line and causing additional parser errors; those are probe artifacts, not accepted candidates. The direct mathlib term was therefore independently checked in a complete isolated snippet and then in the actual two caller contexts. No claim that a malformed multi-attempt was a passing proof. Existing `Polynomial.toMvPolynomial` is definitionally `Polynomial.aeval (X i)`; explicit aeval argument is required in caller terms to avoid folded-pattern failure of rw. This is the shortest clear existing-API route and removes duplicated reasoning.

Raw explicit type/value binder drop tests: `/private/tmp/roth-separation-d15-binder-drop-names.json` (expected rejected probes, autoImplicit false).


## Verification and final gates

Applied change: delete private helper (six lines including `omit` and blank separator); replace exactly two caller proof arguments (one line becomes two at each site). No new helper. Source 559 → 555 lines, 24 → 23 retained declarations; Git diff `+4/-8`, net −4. `git diff --check` passes. All 20 public documentation blocks remain, and public statements/definitions/imports remain unchanged.

The first candidate using `_` for the zero hom compiled in isolation but failed both actual `rw` caller contexts because it inferred folded `Polynomial.toMvPolynomial`. This failure was repaired by explicitly passing `Polynomial.aeval (X none)`; `/private/tmp/roth-separation-d15-final-lsp.json`, initial module/profile logs preserve rejected evidence. Accepted source is verified by:

- Actual `/Users/ramin/.elan/bin/lake build Roth.Separation`, exit 0, 1876 jobs: `/private/tmp/roth-separation-d15-module-build-fixed.log`.
- Complete unfiltered native module LSP: `partial=false`, `timed_out=false`, success true, 0 errors / 31 pre-existing warnings: `/private/tmp/roth-separation-d15-final-lsp-fixed.json`.
- Independent exact ORIGINAL type/non-self proof, no helper invocation: `/private/tmp/roth-separation-d15-independent.lean`, native `.json`; actual built-import rerun `/private/tmp/roth-separation-d15-independent-built.log`.
- Actual built caller constants, checked by fresh command-line import (avoids stale LSP imports): `/private/tmp/roth-separation-d15-built-axioms.lean` and `.log`. Both `Roth.degreeOf_rename_mul_aeval` and `Roth.degreeOf_none_rename_mul_aeval` depend only on `propext`, `Classical.choice`, `Quot.sound`. Removed helper has no final constant to check.

| Gate | Result/evidence |
|---|---|
| lake_build_file | PASS, actual module build exit 0 |
| definition_protected | PASS, no definition/abbrev change |
| theorem_statement_protected | PASS, authorized private-wrapper deletion; both public caller statements byte-identical |
| structure_gate | PASS, target deleted; exact caller argument substitutions only |
| naming_gate | PASS, no new name; no retained offending target |
| line_packing_gate | PASS, complete original target table above; target absent finally, new proof argument lines ≤100 |
| inequality_orientation_gate | PASS, target none; no caller signature edits |
| comments/docs | PASS, no documentation or narrative edits |
| cumulative external checks | Parent owns sequential full project, separate LeanEval and cumulative original/public/all-actual probes after freeze |

Overall declaration gates: PASS. No rename queued. No new helper requires another audit. Public instance menu and public `aeval_X_eq_rename` deletion remain pending without application.

## Actual module profiling

Command: `/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Separation.lean`.
Baseline actual module log `/private/tmp/roth-separation-d14-final-profile.log`; accepted final actual module log `/private/tmp/roth-separation-d15-final-profile-fixed.log`, parsed with `/private/tmp/roth-separation-profile-table.py`. Conservative outer command + outer async proof only; one command and one proof anchor each, no nested double-counting.

| Declaration | Baseline outer command + async (ms) | Final outer command + async (ms) |
|---|---|---|
| Removed target | 14.736 + 113.710 = 128.446 | Removed; no final declaration cost |
| `degreeOf_rename_mul_aeval` | 28.381 + 71.092 = 99.473 | 16.682 + 106.199 = 122.881 |
| `degreeOf_none_rename_mul_aeval` | 22.465 + 91.375 = 113.840 | 27.223 + 171.228 = 198.451 |

Both affected final declarations are <750 ms, therefore no repeat threshold and no 1000 ms remediation triggered. Caller costs increased in this run; removal is justified by existing API reuse, not a claim of whole-project speedup. No profiler scaffolding/options were added to source.

Holistic simplify review: duplicate private specialization removed; preserving the two public caller formulas and their narratives is the appropriate boundary. Further public generalisation/removal is not applied. Buzz review: above actual anchors within budget; no limits raised.

## Eleven completion steps

- [x] Step 1: relevant skills, cleanup Phase 4/gates, golfing/proof patterns, search/generalisation/style/naming/profiling references read.
- [x] Step 2: all 24 audit items recorded before source edits.
- [x] Step 2.5: all five actual search methods and generic routes checked.
- [x] Step 2.6: every effective binder tested or dependency accounted for; explicit private literature exemption.
- [x] Step 2.7: measured per-line signature width table.
- [x] Step 2.8: per-occurrence inequality scan table.
- [x] Step 3: all 42 golf rule statuses.
- [x] Step 4: alternate strategies and native direct/API proof checked.
- [x] Step 5a: complete native unfiltered LSP 0 errors/31 warnings.
- [x] Step 5b: actual module/independent proof/actual caller axioms and diff gates.
- [x] Step 6a: no rename to queue; parent retains all shared logs/Git ownership.

## Freeze

Accepted final actual profile command exited 0. Actual independent built-import rerun exited 0; fresh actual built caller axioms command exited 0. ALL native Lean/MCP/compiler/profile requests are complete and drained, including rejected initial requests. No running request remains.

Final `Roth/Separation.lean` SHA256: `7089df105ebdca3d3358741fa4a574aa44a6f07c870d24838028eb550cac6960`.

ALL source ownership is revoked. This worker is now report-only and will make no further source edit. Parent owns cumulative compatibility, sequential full project and LeanEval, exact-path commit and push. Pending public proposals remain untouched.

## Owner cumulative publication gates

Source FROZEN SHA256 `7089df105ebdca3d3358741fa4a574aa44a6f07c870d24838028eb550cac6960`; leaf ownership revoked and requests drained before owner gates. Owner probe `89268` exit0,58.49s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL23 actual retained standardaxiom checks. `/private/tmp/roth-separation-d15-compatibility.{lean,log,json}`. Owner build session `10803` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,147.67s/37.60s; source hash stable. `/private/tmp/roth-separation-d15-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.
