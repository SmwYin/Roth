# `rename_some_ne_zero` — original declaration 14

Initial audit recorded before source edits. Scope: private helper and its two exact callers,
`degreeOf_rename_mul_aeval` and `degreeOf_none_rename_mul_aeval` in `Roth/Separation.lean`.
Project-wide `rg` finds only these three occurrences. Baseline complete native LSP: no errors,
31 warnings; none on this private lemma. Parent supplied clean build baseline at `6a06466`.
No public proposal is applied. Private literature-search exemption applies: this is an
implementation-only instance of an existing library injectivity lemma.

## Initial 24-item audit

| Item | Concrete finding/action |
|---|---|
| 1 Lint | No target warnings; 31 existing module warnings. |
| 2 Have scan | No `have`. |
| 3 Set option | No options. |
| 4 Simp | No simp calls in target. |
| 5 Naming | Describes renaming by `some` preserving nonzero; no forbidden fragments. Remove redundant helper rather than rename. |
| 6 Packing | Two signature lines; measured table below. Removal eliminates underpacking. |
| 7 By | Term proof; no `by` issue. |
| 8 Format | Two-space term indentation, no empty proof lines or instance tactics. |
| 9 Comments | No target comments; caller documentation is preserved verbatim. |
| 10 Docstring | Private helper correctly has none. |
| 11 Visibility | Already private; library replacement removes it. |
| 12 Structure | One-line proof; no conjunction or branches. |
| 13 Mathlib | Found `rename_eq_zero_iff_of_injective`; test `.not.mpr hU` in both callers. |
| 14 Junk def | N/a: lemma. |
| 15 Exists | N/a: nonexistential statement. |
| 16 Show | No show. |
| 17 Push neg | None. |
| 18 Generalise | `Fintype` and `DecidableEq` already omitted. General injective-map form exists in mathlib. Probe all effective binders. |
| 19 Inequality | No ordered inequalities; `≠` is the nonzero premise/conclusion. |
| 20 Normal form | Canonical library zero iff, negated, covers this statement. |
| 21 Syntax generality | Direct library use removes a project-specific spelling. |
| 22 Import fanout | No added imports. |
| 23 Casts | No explicit casts added or removed. |
| 24 Instance name | N/a: not an instance. |

Plan: compile independent original-type proof and binder probes, remove private wrapper,
replace only its two proof calls, build module, collect complete native LSP, inspect actual
caller axioms, and profile actual module callers. No new helper will be introduced.

## Five-method mathlib search

| Method | Actual query and result | Raw evidence |
|---|---|---|
| A Lean-Finder | `MvPolynomial injective rename preserves nonzero`: hit `MvPolynomial.rename_injective`, killCompl and degree variants. | `/private/tmp/roth-separation-d14-leanfinder.json` |
| B Loogle | `MvPolynomial.rename, _ = 0 ↔ _ = 0`: exact hit `MvPolynomial.rename_eq_zero_iff_of_injective`. | `/private/tmp/roth-separation-d14-loogle.json` |
| C LeanSearch | Natural language injective renaming zero iff: rename, coefficient, support and polynomial map hits. | `/private/tmp/roth-separation-d14-leansearch.json` |
| D Source | `rename.*(eq_zero|ne_zero)` and `rename_injective` in `Mathlib/Algebra/MvPolynomial/Rename.lean`: exact lemma at 107, injectivity at 102, proof read. | Source and session output |
| E Name pattern | `lean_local_search rename_eq_zero_iff_of_injective`: source hit (index warming, so no absence inference). `#check` independently confirms compiled constant. | `/private/tmp/roth-separation-d14-local.json`, `...-probe.json` |

Auxiliary variants searched/read: `rename_injective`, `rename_eq_zero_iff_of_injective`,
`coeff_rename_ne_zero`, `killCompl_rename_app`, general `map_ne_zero_iff`.
Common-equivalents match: nonzero is negation of zero, so zero-iff's `.not.mpr` is the canonical
specialisation. Conclusion: existing more general library lemma; delete private local and
specialise it directly at two callers. All remote searches returned results; none unavailable.

## Generalisation and effective-binder probes

Exact original type uses `{τ R : Type*} [CommSemiring R] {U : MvPolynomial τ R} (hU : U ≠ 0)`.
`Fintype τ` and `DecidableEq τ` were explicitly omitted in the original and stay absent in
independent proof. Original-type and arbitrary injective `f : σ → τ` proofs are in
`/private/tmp/roth-separation-d14-independent.lean`. No proof refers to the removed constant.
Drop tests have `autoImplicit false`; each source and complete compiler log is preserved as
`/private/tmp/roth-separation-d14-drop-{τ,R,commSemiring,U,hU}.{lean,log}` and aggregated in
`/private/tmp/roth-separation-d14-binders.json`. The tests distinguish type dependency failures
from a false mathematical weakening; they are not claimed as semantic counterexamples.
Types τ/R and polynomial U are dependencies; the nonzero premise is essential (take U = 0).
Weakening CommSemiring to Semiring cannot construct the MvPolynomial algebra API. Point
localisation, strict-to-weak, ordered-ring, field, finite/compact, regularity and named-object
inversion checks do not apply: no such hypotheses or object exist. The useful map generality
already exists in mathlib, and no new declaration or public contract is needed.

## All 42 golf rules

Target was a single term proof, so most structural rules have no matching syntax. Native
live-file attempts were run with `by` terms after an initial term-position invocation rejected
bare tactic syntax; both raw results are preserved. Corrected `simpa` and `grind` close the
goal, `positivity` and `aesop` fail, and `exact?` finds no complete proof. The direct library
term is more explicit and avoids a new automation wrapper. These attempts only test the
private target, not wholesale caller golf outside this ownership.

| Rule | Concrete status |
|---|---|
| 1.1 Remove `by exact` wrapper | Already term mode; no by-exact wrapper. |
| 1.2 Remove `by rfl` | No by-rfl. |
| 1.3 `rw + exact` → `rwa` | No rw/exact chain. |
| 1.4 `simp + exact/assumption` → `simpa using` | Tested simpa using hU successfully; library term chosen for direct caller replacement. |
| 1.5 Remove trailing `rfl` after `simp` | No simp/rfl. |
| 1.6 `constructor + exact + exact` → anonymous constructor | No constructor. |
| 1.7 `apply f; exact h` → `exact f h` | No apply/exact. |
| 1.8 `by_contra + push_neg` → `by_contra!` | No contradiction proof. |
| 1.9 Eta-reduce lambdas | No eta lambda. |
| 1.10 Inline single-use `have` (no `by`) | No have. |
| 1.11 `apply + intro` → `refine + fun` | No apply/intro. |
| 1.12 Remove redundant `show` | No show. |
| 1.13 `have + .1/.2` → `obtain ⟨ ⟩` | No projected have. |
| 1.14 Merge consecutive `rw` | No consecutive rw in target; caller rw kept intact. |
| 1.15 Unsqueeze terminal `simp only` | No terminal simp only in target. |
| 1.16 Squeeze nonterminal bare `simp` | No nonterminal simp in target or added diff. |
| 1.17 Use dot notation | Library iff uses dot notation .not.mpr. |
| 1.18 Use `<|` to avoid trailing parens | Argument nesting in rw requires parentheses; no trailing function-argument parenthesis to remove. |
| 1.19 `push_neg` → `push Not` | No push_neg. |
| 1.20 Inline trivial single-use `∃`-lemmas | Not existential. |
| 2.1 Try `grind` on the whole proof | Native by grind with exact zero-iff succeeds; explicit library term selected. |
| 2.2 Try deleting tactics before `grind` | No tactics precede grind. |
| 2.3 Try `simpa` consolidation | Native simpa consolidation succeeds; explicit term selected. |
| 2.4 Try `fun_prop` | No regularity predicate; fun_prop inapplicable. |
| 2.5 Try `positivity` | Native positivity attempted and fails to prove nonzero. |
| 2.6 Try `gcongr` | No ordered inequality/monotonicity; gcongr inapplicable. |
| 2.7 Try `lia` / `omega` (prefer `lia`) | No Nat/Int arithmetic; lia/omega inapplicable. |
| 2.8 Try `aesop` | Native aesop attempted; fails at depth 30. No limits raised. |
| 2.9 Try `norm_num` / `norm_cast` | No numerals computation or casts; norm_num/norm_cast inapplicable. |
| 2.10 Try `decide` / `decide +kernel` | Not a closed finite decidable computation; generic coefficient semiring and polynomial. |
| 2.11 Try `field_simp; ring` | No denominators or ring identity. |
| 2.12 Try `linear_combination` | No ring ending or linear relation. |
| 2.13 Try `wlog` for symmetric cases | No symmetric case split. |
| 2.14 Try collapsing `calc` to term mode | No calc. |
| 2.15 Close multiple goals with `<;>` | One goal; no parallel branches. |
| 3.1 `erw` → `rw` | No erw. |
| 3.2 `continuity` / `measurability` → `fun_prop` | No legacy regularity tactics. |
| 3.3 `omega` → `lia` (preferred default; `grind` subsumes both) | No omega. |
| 3.4 `rcases ... with rfl` auto-substitutes | No rcases. |
| 3.5 Register lemmas for automation | Existing library lemma is simp; no helper remains to register. |
| 3.6 `simp_all` over `simp_all only` | No simp_all only. |
| 3.7 Remove `set_option maxHeartbeats` | No heartbeat option. |

## Step-back review

The mathematical content is injectivity preserving nonzero, already supplied for every
injective variable map. Removing the private wrapper simplifies the local API. Its two
specialisations are long enough to wrap once but remain within 100 columns, with no new
helper and no change to caller statements or documentation. The retained aeval helper and
the two public proposals are outside this change. No blanket simp attributes, imports,
instance edits, metadata changes, or proof limits are introduced.

## Width and inequality gates

`#check` at `format.width 100` is recorded in `...-probe.json` (library API) and
`...-independent-final.log` (original effective type). Original helper signature width table:

| Original signature line | Codepoints | Next signature token | Arithmetic/action |
|---|---:|---|---|
| 194 | 71 | `rename some U ≠ 0 :=` (20) | 71 + 1 + 20 = 92; would repack if retained; declaration removed |
| 195 | 24 | None | Terminal; removed |

No final target signature remains. Caller signature tables are included because their
proof calls changed; both signatures themselves are byte-identical to baseline.

| Final caller/signature line | Codepoints | Next token | Arithmetic/action |
|---|---:|---|---|
| degreeOf_rename_mul_aeval 193 | 98 | `degreeOf` (8) | 98 + 1 + 8 = 107 > 100; keep |
| 194 | 97 | `degreeOf` (8) | 97 + 1 + 8 = 106 > 100; keep |
| 195 | 24 | None | Terminal; keep |
| degreeOf_none_rename_mul_aeval 206 | 95 | `degreeOf` (8) | 95 + 1 + 8 = 104 > 100; keep |
| 207 | 93 | `V.natDegree` (11) | 93 + 1 + 11 = 105 > 100; keep |
| 208 | 23 | None | Terminal; keep |

| Inequality occurrence | Finding/action |
|---|---|
| Original premise `U ≠ 0` | Disequality, no orientation change |
| Original conclusion `rename some U ≠ 0` | Disequality, removed with wrapper |
| Caller hV/hU premises and case splits | Disequality/equality, no ordered inequality |
| All added proof lines | No `>`, `≥`, `<`, or `≤` |

## Verification and performance

- Actual `/Users/ramin/.elan/bin/lake build Roth.Separation` exited 0, 1876 jobs:
  `/private/tmp/roth-separation-d14-build.log`.
- Complete unfiltered native LSP baseline and final: **0 errors, 31 warnings**, no partial
  elaboration or timeout. Raw `/private/tmp/roth-separation-d14-{baseline-lsp,final-lsp}.json`.
- Independent exact ORIGINAL-type proof and arbitrary-injective-map generalisation both
  compile. Five actual negative binder probes exit 1 for the documented dependency/type
  errors or unclosed goal; all complete logs and exit codes in `...-binders.json`.
- Native `lean_verify` for both actual changed caller constants reports `trust: standard`,
  only `[propext, Classical.choice, Quot.sound]`, no source warnings. Raw
  `/private/tmp/roth-separation-d14-degreeOf_{rename_mul_aeval,none_rename_mul_aeval}-axioms.json`.
- Independent proof is rerun against the final built module, including `#print axioms` for
  the exact original-type proof and both actual public callers, in `...-independent-final.log`.
- Actual module profile command exits 0:
  `/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Separation.lean`.
  Complete `/private/tmp/roth-separation-d14-final-profile.log`, parsed `.log.json` by
  `/private/tmp/roth-separation-profile-table.py`. No source profiler scaffolding.

| Actual declaration | Baseline command + proof (ms) | Final command + proof (ms) | Final raw anchors |
|---|---|---|---|
| rename_some_ne_zero | 21.790 + 82.032 = 103.822 | Removed, no final cost | Absent |
| degreeOf_rename_mul_aeval | 49.778 + 95.879 = 145.657 | 28.381 + 71.092 = **99.473** | command 206566; proof 209798 |
| degreeOf_none_rename_mul_aeval | 34.571 + 139.383 = 173.954 | 22.465 + 91.375 = **113.840** | command 217178; proof 220522 |

Baseline actual module log is `/private/tmp/roth-separation-d13-removal-profile.log`.
Only outer command and outer async proof times are summed; nested nodes are not added.
Both affected retained declarations are below 750 ms, so no repeat sweep is required.
These timings do not establish a whole-project speedup. Other declarations' performance
is owned by their dedicated audits.

## Diff gates and eleven completion stages

| Gate | Status/evidence |
|---|---|
| module build | Pass, actual command exit 0 |
| definition protection | Pass, no definition or abbreviation changes |
| theorem statement protection | Pass, only authorised private wrapper removed; public types identical |
| structure | Pass, removed one-line helper, no new proof branches or helper |
| naming | Pass, redundant helper removed rather than renamed; no forbidden names introduced |
| line packing | Pass, removed target; retained caller table above |
| inequality orientation | Pass, per-occurrence table above |
| cumulative external compatibility | Parent owns final sequential full project, LeanEval and original-file compatibility checks after freeze |
| comments/docs | Pass, no documentation changed |
| whitespace | `git diff --check` exit 0 |

| Completion stage | Result |
|---|---|
| 0 Doctor | Parent clean pushed baseline `6a06466`; own complete baseline LSP |
| 1 Prepare | Original snapshot, callers, skills, contract and references read |
| 2 Audit | Initial full 24-item audit written before source edits |
| 3 File fixes | None needed within ownership; metadata preserved |
| 4 Deep golf | All 42 rules assessed; live term/automation probes saved |
| 5a Refactor | Private wrapper removed using existing canonical library API |
| 5b Rename | No rename queue needed; no new names |
| 6 Final gates | Module build, complete LSP, isolated proof, actual axioms and diff checks |
| 6.5 Simplify | Holistic step-back review above; direct library composition chosen |
| 6.6 Buzz | Actual retained caller profile anchors below budget |
| 7 Report | Dedicated report and complete raw logs; final freeze below |

Final arithmetic: source **562 → 559 lines**, **25 → 24 retained declarations**;
Git source diff **4 additions, 7 deletions**, net -3. Removal consumes five source lines;
two caller replacements add one line each. No public proposal is applied; pending instance
menu and public `aeval_X_eq_rename` removal remain exactly with the parent.

## Freeze

All native Lean/MCP, compiler, module-build and profile requests have completed and are
drained. Final independent rerun exits 0 and prints only the standard three axioms for
all three checked proofs. **ALL source ownership is revoked.** This worker is report-only
from this point onward and will make no further source edits.

Frozen `Roth/Separation.lean` SHA256:
`5ee248fa04d6ef74d0d6cccb17c898c52302215f62eb480dfa5944562ebe5ea1`.
Parent owns Git, shared/cumulative records, final project and LeanEval gates, commit and push.

## Owner cumulative publication gates

Source FROZEN SHA256 `5ee248fa04d6ef74d0d6cccb17c898c52302215f62eb480dfa5944562ebe5ea1`; leaf ownership revoked and requests drained before owner gates. Owner probe `59421` exit0,57.83s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL24 actual retained standardaxiom checks. `/private/tmp/roth-separation-d14-compatibility.{lean,log,json}`. Owner build session `84208` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,142.29s/41.59s; source hash stable. `/private/tmp/roth-separation-d14-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.
