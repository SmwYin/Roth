# `Roth.index_C_mul` cleanup

Fresh single-declaration audit, 2026-10-17, starting checkpoint `534ce66` on
`ramin-cleanup`. Only source change: the approved `omit [DecidableEq σ] in`, before
the unchanged docstring. The theorem's explicit signature and proof remain byte-identical
to `/private/tmp/roth-index-original.lean` (baseline `e557886`) and the worker snapshot
`/private/tmp/roth-index-cmul-before.lean`. This changes the actual public type by removing
one instance argument; it is not merely a textual cleanup. No other binder, definition,
documentation, import, attribute, or caller changed. Target declaration remains three lines;
its docstring plus declaration grows from four to five lines including `omit`. File 264→265.

Source authority released and revoked at SHA256
`580afc142903ea2171cb7e4411d681524fd1fbdaedef33611af5d7c50fef24c1`.
All Lean requests/compiler sessions finished before release. Subsequent work is report-only.
Whole-project build, separate LeanEval, original whole-file recovery, final independent
simplify/profile resweeps, Git and publication belong to the owner; this report claims only
the leaf gates. Owner confirms no external callers for this target.

## Audit: all 24 items

| # | Item | Concrete disposition |
|---|---|---|
| 1 | Lint | Original target had unused-section and unused-decidability warnings. Approved omission removes both. Final complete native diagnostics have no target warning/error. |
| 2 | Have scan | Zero `have` bindings in the one-rewrite proof. |
| 3 | Set option | No target limit, trace, or linter override. None added. |
| 4 | Simp squeeze | Production proof has no simp. Tested simp alternative closes but initially reports two unused arguments; reduced alternative compiles. Retained explicit rewrite. |
| 5 | Naming | `index_C_mul` describes index under constant-polynomial multiplication; `C` is the actual polynomial constructor. No forbidden abbreviation, scheme number, numeric auxiliary suffix, or inequality reversal. No rename needed. |
| 6 | Line packing | All two signature lines measured below, including conclusion; both pass. |
| 7 | By placement | `:= by` ends conclusion line 201. |
| 8 | Format | One tactic, two-space proof indentation, no blank proof lines, no semicolon chains, no `haveI`/`letI`. |
| 9 | Comments | No inline proof comments before/after. Every file docstring and header preserved byte-for-byte by snapshot comparison. |
| 10 | Docstring | Existing public source/formula docstring retained exactly, as required. No new documentation proposal applied. |
| 11 | Visibility | Public API theorem about the project index; retained public as instructed. Classic import dialect, not module syntax. |
| 12 | Structure | One proof-body line; no conjunction or branches. No helper/extraction/decomposition warranted. |
| 13 | Mathlib | Five actual methods below; support invariance is provided by mathlib and already used directly. No verified whole-target replacement. |
| 14 | Junk definition | n/a: theorem, not a definition. |
| 15 | Exists lemma | n/a: neither private nor existential. |
| 16 | Show/change | Neither occurs. |
| 17 | Push neg | No `push_neg` or negation-pushing block. |
| 18 | Generalise | Every binder/drop test below. Only approved decidability removal applied. |
| 19 | Inequality | Explicit zero-occurrence table below; no reversed inequalities or names. |
| 20 | Normal form | Eliminates constant multiplication from the index on the left to the simpler index on the right. Support equality is canonical underlying API. No competing equivalent-form lemma added. |
| 21 | Syntax generality | Explicit `hc : c ≠ 0` directly feeds support invariance; P/point/weights remain directly applicable. No argument-order or bundled-hypothesis change justified. |
| 22 | Import fanout | n/a: zero new production imports. |
| 23 | Casts | Diff contains no cast/ascription: 0 dropped, 0 kept cross-type, 0 kept load-bearing. Existing explicit binder types retained. |
| 24 | Instance names | n/a: no instance declaration introduced or named. |

## Mathlib search: five actual methods

| Method | Actual query | Result/evidence |
|---|---|---|
| A LeanFinder | `support of nonzero scalar multiple multivariate polynomial` | Actual bounded MCP attempt returned DNS failure, not absence; `/private/tmp/roth-index-cmul-finder.json`. |
| B Loogle | `MvPolynomial.support (_ • _) = _` | Actual bounded MCP attempt returned DNS failure; `/private/tmp/roth-index-cmul-loogle.json`. |
| C LeanSearch | `support nonzero scalar multiple multivariate polynomial` | Actual bounded MCP attempt returned DNS failure; `/private/tmp/roth-index-cmul-search.json`. |
| D Source search | `index_C_mul|support_smul_eq|support_C_mul|taylor_C` in mathlib MvPolynomial/project source | Positive `Mathlib/Algebra/MvPolynomial/Basic.lean:700`: `MvPolynomial.support_smul_eq`; its implementation delegates to `Finsupp.support_smul_eq`. Project Taylor supplies `taylor_C`. Also tried obsolete `Mathlib/Data/MvPolynomial` path, which does not exist; the valid Algebra path supplied the hit. No absence claim. |
| E Native name pattern | `lean_local_search("support_smul_eq")` | Positive Finsupp and MvPolynomial hits. Index unavailable, but these positive source hits were verified by built `#check`; no negative inference from index state. |

Auxiliary variants checked: support under scalar action versus `C` multiplication,
`Finsupp.support_smul_eq`, `MvPolynomial.support_smul_eq`, `support_C_mul`, and
Taylor constant preservation. Common-equivalents table: no discrete/finiteness/bornology
bucket matches. Six replacement rules considered: no new wrapper/predicate introduced;
existing support API used directly; no equivalent of the project-specific index theorem
verified; no deletion authorized. Existing docs are user-preserved, so no module-doc update.

Native whole-proof `exact?` and `apply?` both reached the default 200000-heartbeat limit;
neither established absence. `grind` failed, `aesop` left the goal. These were actual
live-file `lean_multi_attempt` calls at line 202, all returned before release. The multi-attempt
batch exceeded the preferred 45-second wall window; no limit was raised and no retry loop
was used. The conclusion is a verified partial match already used, with remote search
unavailable, not an exhaustive mathematical absence claim.

## Generalisation: every binder

All isolated mechanical probes import the built module, set `autoImplicit false`, and
retain the same goal/rewrite except the indicated binder substitution. Sources and logs:
`/private/tmp/roth-index-cmul-<probe>.lean[.log]`; complete exit-status map
`/private/tmp/roth-index-cmul-probes.json`. Expected failing probes are negative experiments,
not production gates. Final positive probe and production build both exit 0.

| Binder | Classification/use | Mechanical probe and actual result | Decision |
|---|---|---|---|
| `{σ : Type*}` | Universe-polymorphic type; indexes P, α, r | `drop_sigma`: unknown σ, exit 1. Already `Type*`; no remaining fixed-universe restriction. | Retain. |
| `[Fintype σ]` | Finiteness data used by the literal `weight`/index type | `drop_fintype`: missing Fintype, exit 1; parent weakening `[Finite σ]` (`finite_parent`) also missing Fintype, exit 1. | Retain actual construction contract; installing a chosen Fintype would restate the construction. |
| `[DecidableEq σ]` | Decidability, unused | `drop_decidable`: original rewrite without instance, exit 0; native target diagnostics clean; built signature confirms absence. | Approved omission applied. |
| `{c : ℝ}` | Scalar value appearing in C c and hc | `drop_c`: unknown c, exit 1. No hypothesis/parent class to weaken; concrete coefficient-field change would require a new index definition. | Retain. |
| `(hc : c ≠ 0)` | Proposition needed by scalar support invariance | `drop_hc`: unknown hc at support invocation, exit 1; `weak_hc` replacing with `0 ≤ c`: type mismatch (needs c ≠ 0), exit 1. | Retain. Tests show current argument fails under weakening, without claiming a complete necessity theorem. Already pointwise scalar condition; no global function property to localize. |
| `(P : MvPolynomial σ ℝ)` | Polynomial value in both sides | `drop_P`: unknown P, exit 1. No order/parent property attached to this data binder. | Retain. |
| `(α : σ → ℝ)` | Evaluation point used by Taylor translation | `drop_alpha`: unknown α, exit 1. Data, no global regularity hypothesis to point-localize. | Retain. |
| `(r : σ → ℕ)` | Weights appearing in both sides | `drop_r`: unknown r, exit 1. No positivity hypothesis here; zero weights already allowed by this definition. | Retain. |

Inversion check: after unfolding index, the theorem reduces to support invariance under
nonzero scalar multiplication, already available as mathlib's general
`MvPolynomial.support_smul_eq` (itself an application of Finsupp API). No missing abstract
helper to add. Strict→weak only applies to hc, tested above; the remaining binders are data,
universes, decidability or finite enumeration. No bundled conjunction to unbundle.

## Public literature and displayed search leads

Searches performed 2026-10-17. The first call combined Q1 and Q2 and returned a merged
ranking; each was then rerun individually to obtain an attributable first-three list.
Rankings are recorded as displayed, including irrelevant leads; none is treated as a
verified source merely because it appeared in search.

| Query/run | Rank 1 | Rank 2 | Rank 3 |
|---|---|---|---|
| Initial combined Q1+Q2, shared displayed ranking | [Min Ru, Roth's Theorem](https://www.math.uh.edu/~minru/fields/roth.pdf) | [AMS, Chapter 4 Rational](https://www.ams.org/bookstore/pspdf/mbk-48-prev.pdf) | [Scribd mirror of Vojta](https://www.scribd.com/document/847436004/Applications-of-Arithmetic-Algebraic-Geometry-to-Diophantine-Approximations-Vojta) |
| Q1 repeated: `Roth polynomial index nonzero scalar multiplication invariant generalization` | [Invariant varieties for polynomial dynamical systems, Annals](https://annals.math.princeton.edu/wp-content/uploads/annals-v179-n1-p02-p.pdf) | [Scanlon author-hosted version](https://math.berkeley.edu/~scanlon/papers/polynomial_dynamics_v2012.pdf) | [Scribd, Heights in Diophantine Geometry](https://www.scribd.com/document/480772625/Heights-in-Diophantine-Geometry-E-Bombieri-W-Gubler-Cambridge-2006-WW-pdf) |
| Q2 repeated: `Roth theorem index polynomial weighted order nonzero constant multiplication` | [Min Ru, Roth's Theorem](https://www.math.uh.edu/~minru/fields/roth.pdf) | [Vojta, Applications of Arithmetic Algebraic Geometry](https://math.berkeley.edu/~vojta/ftp/cime.pdf) | [AMS, Chapter 4 Rational](https://www.ams.org/bookstore/pspdf/mbk-48-prev.pdf) |

Opened primary author-hosted Min Ru notes, p. 3: index is the least normalized derivative
weight with nonzero derivative, compatible with nonzero constant multiplication. Opened
primary author-hosted Vojta notes, §3, Definition 3.1, p. 169: positive real weights and
power series are allowed; multiplication by a power series unit preserves index. This
suggests broader unit/power-series and positive-real-weight formulations, requiring a
different construction/public API. They are literature context, not an applied or compiled
implementation proposal. The present scalar invariance is its elementary special case.
Project `clean.tex:630–641` explicitly requires a separate nonzero-scalar identity and
states the exact formula. No content changed in that reference.

ChatGPT mathematical MCP: unavailable in the enabled tool catalog; no fabricated consultation.
No further public change proposed for application at this checkpoint.

## Signature packing and inequality artifacts

Actual built `#check @Roth.index_C_mul`, compiled with `set_option format.width 100`:

```lean
@index_C_mul : ∀ {σ : Type u_1} [inst : Fintype σ] {c : ℝ},
  c ≠ 0 → ∀ (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ), index (C c * P) α r = index P α r
```

| Signature line | Codepoints | Next signature token/block | Arithmetic | Action |
|---|---:|---|---|---|
| 200 | 89 | conclusion `index (C c * P) α r = index P α r := by` (39) | 89 + 1 + 39 = 129 > 100 | ok |
| 201 | 43 | None; proof body next | n/a, final signature line | ok |

Colon already ends line 200. Conclusion is included in the packing test; no hypothetical
byte-based width used. No signature repack required.

| # | Location | Original inequality | Rewrite | Rename |
|---|---|---|---|---|
| — | All signature hypotheses/conclusion | No `≥` or `>` occurrence | n/a | No `_ge_`/`_gt_` name |

## All 42 golfing rules

| Rule | Status/reason |
|---|---|
| 1.1 | n/a: no by-exact wrapper. |
| 1.2 | n/a: no by-rfl. |
| 1.3 | n/a: no rw followed by exact. |
| 1.4 | n/a: no simp followed by exact/assumption. |
| 1.5 | n/a: no trailing rfl. |
| 1.6 | n/a: no constructor. |
| 1.7 | n/a: no apply/exact chain. |
| 1.8 | n/a: no contradiction block. |
| 1.9 | n/a: no lambda in target proof. |
| 1.10 | n/a: no have. |
| 1.11 | n/a: no apply/intro chain. |
| 1.12 | n/a: no show. |
| 1.13 | n/a: no have/projection chain. |
| 1.14 | Already a single merged rw. |
| 1.15 | n/a: no terminal simp-only. |
| 1.16 | n/a: no nonterminal simp. |
| 1.17 | n/a: no eligible namespace application; support lemma is unqualified under open namespace. |
| 1.18 | n/a: no trailing argument parentheses to remove. |
| 1.19 | n/a: no push_neg. |
| 1.20 | n/a: no existential helper. |
| 2.1 | Actual `grind` attempt failed with false goal from negated equality. |
| 2.2 | n/a: no production grind or preceding chain. |
| 2.3 | Simp alternative tested live; two unused args initially. Reduced `simp [index, ← smul_eq_C_mul, support_smul_eq hc]` compiles in isolated built context. Retain explicit same-length rewrite for clarity and scope. |
| 2.4 | n/a: no continuity/differentiability/measurability goal. |
| 2.5 | n/a: target is index equality, not structural positivity. |
| 2.6 | n/a: no inequality or monotonicity proof. |
| 2.7 | n/a: no Nat/Int arithmetic goal. |
| 2.8 | Actual aesop attempt failed after exhaustive search. |
| 2.9 | n/a: no numerical or cast-normalization goal. |
| 2.10 | n/a: symbolic real/polynomial equality, no finite computable proposition. |
| 2.11 | n/a: support invariance rather than denominator algebra. |
| 2.12 | n/a: no ring/ring_nf ending or polynomial identity in scalar variables. |
| 2.13 | n/a: no symmetric cases. |
| 2.14 | n/a: no calc. |
| 2.15 | n/a: no multiple goals requiring repeated closer. |
| 3.1 | n/a: rw already used, no erw. |
| 3.2 | n/a: no legacy continuity/measurability. |
| 3.3 | n/a: no omega/linear arithmetic. |
| 3.4 | n/a: no rcases or substitution. |
| 3.5 | Considered: no new automation attribute needed for this cleanup; no existing attribute altered. |
| 3.6 | n/a: no simp_all. |
| 3.7 | n/a: no heartbeat override to remove; zero added. |

Step-back review: the existing whole proof is one tactic and exposes the exact mathematical
reason (unchanged support). `exact?`/`apply?` were bounded by default heartbeats and failed.
The independently proved coefficient route is longer and serves verification only. No term
wrapper or helper would improve production clarity. No gratuitous proof change made.

## Actual verification and gates

| Gate | Result and exact evidence |
|---|---|
| Module build | `/Users/ramin/.elan/bin/lake build Roth.Index` exited 0; actual build log `/private/tmp/roth-index-cmul-build.log`, Index built in 18s. Existing dependency/header warnings are preserved. |
| Complete native diagnostics | `/private/tmp/roth-index-cmul-diagnostics.json`: success=true, partial=false, timed_out=false, failed_dependencies=[]; unfiltered full-file request. Zero target warnings/errors. |
| Independent ORIGINAL type/proof | `/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-index-cmul-independent.lean` exited 0; log same stem `.log`. Imports Box/Taylor/real completeness support, never Index. Literal original sInf/image/support definition; fresh coefficientwise support proof, no target, private helper, or same-file theorem shortcut. Original DecidableEq binder intentionally retained and warned unused. |
| Exact original public recovery | `/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-index-cmul-built.lean` exited 0; final example has original σ/Fintype/DecidableEq/c/hc/P/α/r type and is proved by actual built target. Snapshot extraction independently asserts original target signature/body text identical. |
| Actual type and axioms | Same built file prints actual #check shown above (no DecidableEq). `#print axioms Roth.index_C_mul` and independent `CmulIndependent.original`: exactly propext, Classical.choice, Quot.sound. No sorryAx in successful final artifacts. |
| Definition protected | Snapshot equality allows only the one approved omit insertion; zero definition/abbreviation edits. |
| Theorem protected | Explicit source signature/body unchanged. Actual type changes only approved instance omission, established by built output and original recovery, not inferred solely from text. |
| Structure/naming/packing/inequality | Pass; concrete artifacts above. |
| No-comment-loss/new identifiers | All docstrings equal under snapshot extraction; no inline target comments existed. Diff introduces only omit command using existing DecidableEq/σ identifiers. No new referenced lemma identifiers. |
| No limits/scaffolding | Only source insertion is omit; no profiler options, temporary wrapper, limits, suppression, sorry, or axiom added. |
| External callers/full project | Owner responsibility and separate gate; owner reports no target external callers. Leaf does not claim full-project success. |

Full native warnings retained, without filtering or suppression: line 1 copyright; line
205 scaling unused section DecidableEq; line 204 scaling unused DecidableEq in type;
line 217 rename unused section DecidableEq; line 214 rename unused σ/τ DecidableEq in type;
line 228 card unused section DecidableEq and unused hr; line 225 card unused DecidableEq
in type; line 238 unique unused section DecidableEq; line 235 unique unused DecidableEq
in type. These ten warnings are outside this target and await their owners/header policy.

Failed preliminary independent scratch lacked the real InfSet import, producing errors and
an invalid sorryAx print; it is not accepted evidence. Added explicit real completeness
imports/unfolded local definition, then removed unused simp args and recompiled successfully.
Final independent log above is the accepted artifact. No production edit was needed.

## Simplify and buzz

Scoped simplify review: PASS-THROUGH. Sole approved omission removes exactly the unused
instance; one-rewrite proof has no duplicated skeleton, single-use have, or new helper to
clean. No built-in `/simplify` callable tool is exposed here; the owner's independent final
simplify sweep remains a file-level obligation, not falsely claimed as a tool invocation.

Buzz: FAST-BOARD for this declaration, budget 1000ms, target total **102.65ms**, proof
69.33ms, command 25.20ms; dominant tactic 65.303ms at the explicit rw. Actual command:

```text
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Index.lean > /private/tmp/roth-index-cmul-profile-trace.log 2>&1
```

Exited 0. Then `python3 /private/tmp/roth-index-profile-parse.py cmul` exited 0 and asserted
all 19 current declarations anchored; output table
`/private/tmp/roth-index-cmul-profile-table.json`. An initial parser attempt happened while
the process was still writing and failed its coverage assertion; discarded. Accepted parse
was rerun after the compiler exit was confirmed. Aggregate profiler categories are not used
as target timing.

Actual native `lean_profile_proof` attempt, 20-second tool budget, failed extracting scoped
omit/same-file context (`cannot omit referenced section variable`, followed by incomplete
extraction). Artifact `/private/tmp/roth-index-cmul-native-profile.json`; complete actual CLI
trace is the fallback authority. No stale native timing claimed.

Measured reduced simp alternative using actual CLI profiler:
`/private/tmp/roth-index-cmul-alternative.lean` / `.log`, exit 0, command node 67.173ms.
This separate built-import context differs from production's same-file context, so no
robust speedup is asserted or used to justify changing a clear one-line proof. Native
multi-attempt also reports the initial unnecessary simp arguments; production rw unchanged.
No performance fix, heartbeat raise, deferred slow target, or profiling scaffolding added.
Target is far below the 750ms borderline resweep threshold. File-final resweep remains owner work.

## Eleven checked worker steps and disposition

- [x] Step 1: full mandatory golf/proof/search/generalisation/gates references read, cleanup workflow and relevant style/naming/review/profiling/buzz contracts consulted.
- [x] Step 2: all 24 audit items recorded.
- [x] Step 2.5: five actual search methods, failures and positive verification recorded.
- [x] Step 2.6: every binder, catalogue applicability, actual probes, literature and inversion recorded.
- [x] Step 2.7: every signature line measured in codepoints with actual compiled width-100 output.
- [x] Step 2.8: explicit inequality table.
- [x] Step 3: all 42 numbered golf rules accounted for.
- [x] Step 4: whole-proof alternatives/reflection completed.
- [x] Step 5a: complete native diagnostics successful and target-clean.
- [x] Step 5b: actual module build, independent original proof, original type recovery, standard axioms, actual signature, scoped diff/content/profile gates pass.
- [x] Step 6a: no rename needed or applied; shared queue (one existing entry) untouched.

Issues found: one unused instance (two warnings); fixed by the single approved omission.
Renames queued: none. Comments preserved: all; zero inline proof comments. New identifiers:
none. Refactoring/decomposition needed: none at this checkpoint. Larger literature
formulations require separate development and are not applied. All source authority is now
with the owner; no Lean request, build, or source edit followed release.


## Owner checkpoint d17

Frozen SHA256 `580afc142903ea2171cb7e4411d681524fd1fbdaedef33611af5d7c50fef24c1`. Fresh whole ORIGINAL nonself reproof, all18 original public
type/value recoveries and all19 actual retained standard-axiom checks: compiler
session21635 exit0, `/private/tmp/roth-index-d17-compatibility.log`.
Approved no-DecEq types are additionally checked by Expr.find?; actual signatures printed.
Sequential owner full then separate LeanEval88853 both exit0(163.72s/39.89s),
Index+Theta hashes stable; `/private/tmp/roth-index-d17-{full,leaneval}.log`.
Worker COMPLETE unfiltered native Index diagnostics success=true partial=false timed_out=false, no faileddependencies, 0target diagnostics/10other warnings; /private/tmp/roth-index-cmul-diagnostics.json. Owner rg finds no project callers; no external caller query needed.
All original block docs byte-identical, source widths≤100, diff checked before staging.
Exact-path publication precedes the next edit.
