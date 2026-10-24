# `isDiophantine_iff` — original2 complete joint checkpoint

Status: **PASS, target-local**, with the independently audited helper accepted locally by the
file owner. The same original author resumed and completed the joint original2 validation.
Owner acceptance/publication and the later fresh whole-file reviewer remain owner work.
Historical partial-handoff sections below are retained as provenance and superseded by the
final evidence at the end; they do not describe outstanding original2 work.

## Scope and baseline

Target: `LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff` in `Roth/LeanEval.lean`.
Exclusive source/report/compiler/native/LSP lease was assigned by the file owner.
Read fully: mathlib-quality and lean4 SKILL.md; cleanup.md and cleanup-all.md;
golfing-rules, proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates,
style-rules, naming-conventions, profiling, pr-feedback-examples.

Saved **before any Lean or golf**:

| Snapshot | Bytes | SHA-256 |
|---|---:|---|
| `/private/tmp/roth-eval-iff/original.lean` (genuine d2eb5e9, copied from original1 recovery) | 3018 | e95c44ae19345ef1514a59ca5e8b182247e9a32aaf4b7d39f0ce57ae5ed27f56 |
| `/private/tmp/roth-eval-iff/entry.lean` (actual worker entry) | 3190 | 7e528eb63d7b06616dcb0cd72c3383cc8e433c44d60aa91104a94da4944f2eb0 |
| `/private/tmp/roth-eval-iff/helper-first-ungolfed.lean` (genuine first helper, saved before helper Lean/golf) | 1338 | 6a0fa884b07d2f4b65ae25833e4824a9c6f86b87d034ea094632f4e2b5a715bf |

Genuine and entry proofs differ: the former passes positivity to
`Roth.eventually_div_rpow_lt`; the entry uses the accepted generalized API `(M := 1 / C)`.
They must not be assumed byte-identical. Initial unfiltered LSP diagnostics on entry: success,
partial=false, timed_out=false, items=[], failed_dependencies=[]. Parent's accepted baseline
build/native evidence is available; no replay is claimed here.

## Mathematical understanding and extraction

The forward direction takes an exponent halfway between 2 and κ. The Diophantine lower
bound at that exponent eventually exceeds `1/q^κ`, contradicting a sufficiently large
denominator in the infinite approximation set after removing its finite bounded-denominator part.
The reverse direction minimizes the positive weighted approximation error on the finite
exceptional approximation set enlarged by `(0,1)`. Irrationality makes this minimum positive;
outside that set the weighted error is at least 1. Half the smaller bound works uniformly.

The finite-exception argument is substantive mathematics (18 proof lines), not a wrapper.
It needs any real exponent κ and finiteness of the approximation set; it does not require
κ=2+ε or positivity of ε. It was extracted verbatim with this parameterization as
`private lemma exists_pos_div_rpow_lt_aux`, no docstring. The parent's public statement,
docstring, and caller are preserved. Helper-only new source was saved before any helper
Lean/golf. No helper golf has been attempted by its author. The fresh auditor owns its full
24-item/42-rule/gate/profiling audit.

## Bounded search and automation evidence so far

| Method | Actual query | Outcome |
|---|---|---|
| A Lean-Finder | finite rational approximations imply a uniform positive weighted-error bound | partial: `LiouvilleWith`, `Liouville`, `LiouvilleWith.exists_pos`; no direct bridge returned (index v4.28.0, must verify pinned source) |
| B Loogle | `Set.Finite, ∃ c : ℝ, 0 < c ∧ _` | empty result, isError=false |
| C LeanSearch | irrationality exponent finite rational approximations uniform lower bound | partial: `Rat.finite_rat_abs_sub_lt_one_div_den_sq`, `Irrational.eventually_forall_le_dist_cast_rat_of_den_le`, residual Liouville characterization |
| D source | `exists_min_image`, positive finite uniform-bound variants in finite sets/order bounds and DiophantineApproximation/Liouville files | `Set.exists_min_image` in Data/Set/Finite/Lemmas.lean:75; existing proof already uses it directly |
| E local names | `Diophantine`, `exists_pos` | local predicate/bridge and partial Liouville API; index=warming, therefore no absence conclusion from the local index |

Auxiliary searches inspected finite/minimum/bddBelow/exists-pos variants. Common-equivalents
table supplies finite-set minimum building blocks, not the weighted-error conversion. No
claim of universal absence is made. Full-name grep / generic compiled helper absence probe
remain for the independent helper auditor.

Actual entry `lean_multi_attempt` at line 20: `grind` failed, `simp [IsDiophantine]`
left the expanded equivalence, `aesop` left both directions, `exact?` failed. `apply?`
offered logical reshuffles with open subgoals; proof_status=null, therefore **not a proof**.
At line 28: `grind`, `exact?`, `aesop` also failed; aesop simplified the denominator-exclusion
hypothesis to Q<q but did not close the contradiction. No successful result has been
inferred from an empty goals array when diagnostics report failure.

Public literature query: “irrationality exponent uniform lower bound finite approximations
Roth theorem equivalence.” Top relevant primary references returned:
[The Irrationality Exponents of Computable Numbers](https://math.berkeley.edu/~slaman/papers/ie.pdf),
[Roth lecture notes](https://www1.cmc.edu/pages/faculty/lenny/classes/spring_2019/m195/GNT_lecture-notes.pdf),
[AMS chapter preview on approximation exponents](https://www.ams.org/bookstore/pspdf/mbk-48-prev.pdf).
Search snippets describe the usual finite-exception threshold formulation. This is evidence
for the canonical mathematical formulation, not evidence for dropping irrationality in the
uniform positive-bound equivalence. ChatGPT math MCP is not exposed in available tools.

## Outstanding original-author work

The complete original-target 24-item report, all 42 golfing-rule slots, per-binder drop and
weakening experiments, inversion check, final codepoint/inequality/cast tables, strict type
and actual opaque proof/default-semantics/dependency guards, ordered builds, native/LSP gates,
and held isolated profiler capture remain **pending** until the helper auditor returns.
The forward branch still exceeds ten lines at this checkpoint. Original2 is not complete.
The built-in simplify Skill tool is unavailable; the file owner will dispatch a fresh final
independent substantive reviewer after original3; no simplify invocation is claimed.

## Readiness and lease release — PARTIAL-END

`lake env lean Roth/LeanEval.lean` completed with exit 0, no output; terminal session 62789
was explicitly polled to completion. Subsequent unfiltered LSP diagnostics returned
partial=false, timed_out=false, success=true, items=[], failed_dependencies=[]. All author
tool calls have returned, with zero pending author compiler/native/LSP/profile jobs.
No profile driver or external background process was launched. Helper payload equals the
saved genuine first helper source exactly (asserted in memory).

Readiness source: 3399 bytes, SHA-256
`4d6a3d7eda1ea16c17a161c4e41c7dcb36d3e22077129c2753fb820f41d961ba`.
Frozen whole-file copy: `/private/tmp/roth-eval-iff/helper-ready-file.lean`.
Machine-readable receipt: `/private/tmp/roth-eval-iff/partial-handoff.json`.
Released to file owner: source, target report, compiler, native, LSP, and profile leases.
Original2 must resume through the **same original author** after fresh independent helper
acceptance, and must not be published as completed from this partial checkpoint.

## Same-author resumption and full target audit

The fresh helper auditor's full report and owner acceptance are frozen separately in
`LeanEval-exists_pos_div_rpow_lt_aux.md` and
`/private/tmp/roth-eval-owner/finite-helper-owner-accepted-v1.json`. Its only production
change is the explicit minimizing pair `hmin (p, q)`, replacing `_`. Its accepted actual
production proof and timing evidence are reused without reinference or re-profiling.
Resumed source snapshot: `/private/tmp/roth-eval-iff/resume-entry.lean` (3404 bytes,
SHA256 `b682d05b7faa24c0ac24d61d7fc36af71d79422c7ff9993c139a171a4e827c26`).

| Item | Actual finding/action for the original bridge |
|---|---|
| 1 LINT | Complete unfiltered diagnostics clean after final source rewrite. One intermediate untyped hgap simplification failed because its inferred expression used multiplication by inverse; reverted to typed substantive hgap. |
| 2 HAVE | Entry hQq: no by, one explicit use, inlined into hQ; entry hs: no by, one use, replaced by application and direct finite-set proof. hgap: by-proof, one use in hpq.2.trans, keep substantive scaling/simplification content. Other original reverse haves now belong to the independently audited helper. |
| 3 SET_OPTION | None in source; no limits raised or debug options added. |
| 4 SIMP | Two terminal simpa calls: scaling by C, and Nat/Int cast bridge. Both unsqueezed. No nonterminal bare simp. |
| 5 NAMING | isDiophantine prefix references IsDiophantine; `_iff` is the equivalence suffix. No forbidden abbreviation, scheme number, single-letter public name, or rename needed. |
| 6 LINE PACKING | Both unchanged signature lines measured below; full semantic RHS does not fit beside the declaration/binders. |
| 7 BY | Main and hgap `:= by` stay on preceding lines. |
| 8 FORMAT | Two-space proof indentation, no blank body lines, no haveI/letI, no sequential rewrite pair. |
| 9 COMMENTS | No original inline proof comments existed; zero removed. Original docstring preserved verbatim. |
| 10 DOCSTRING | Existing one-sentence equivalence/application documentation preserved exactly. |
| 11 VISIBILITY | Public bridge is the documented adapter API and used by thueSiegelRoth; retain public. Helper private and separately audited. |
| 12 STRUCTURE | Original 32 tactic lines → 13; proof boundary plus body14. Forward branch9, reverse3. Lambda constructor and le_of_not_gt remove setup without inventing helpers or hiding branches. No conjunction in the external target. |
| 13 MATHLIB | Actual five-method bounded search and exact?/apply? probes above; uses existing finite-set and asymptotic APIs directly. No 1–3-call wrapper duplicates mathlib. |
| 14 JUNK DEF | n/a: theorem, not definition; original predicate frozen. |
| 15 EXISTS LEMMA | n/a: target is an equivalence, accepted helper is substantive rather than witness/rfl. |
| 16 SHOW/CHANGE | n/a: neither tactic appears. |
| 17 PUSH_NEG | n/a: none. |
| 18 GENERALISE | Every external binder classified below, actual hx drop probe fails; no small safe weakening applied. |
| 19 INEQUALITY | Signature κ≤2 is smaller-left; no ≥/>. All internal typed inequalities also smaller-left. Imported not_gt and lt_of_not_ge are existing mathlib APIs, not declaration names to rename. |
| 20 NORMAL-FORM | This is the requested adapter from LeanEval's uniform constants to the project's infinite-approxSet exponent bound; neither original predicate nor exponent contract changed. |
| 21 SYNTAX-GEN | Iff permits .mp/.mpr and rewriting; the sole caller uses .mpr. No easier required application form found. |
| 22 IMPORT-FANOUT | n/a: import Roth.Main unchanged; no new import. Repository search found one same-file caller, no external file importing Roth.LeanEval. |
| 23 CASTS | No new explicit cast/ascription introduced by final golf; real/natural/integer crossings in typed hgap and hbound remain substantive. The real exponent annotation in the eventual bound fixes the inequality inferred by linarith. |
| 24 INSTANCE-NAME | n/a: no instance declaration. |

### Signature codepoint table

Actual `#check @isDiophantine_iff` at `format.width=100`:

```
∀ {x : ℝ}, Irrational x →
  (IsDiophantine x ↔ ∀ {κ : ℝ}, (Roth.approxSet x κ).Infinite → κ ≤ 2)
```

The tool qualifies the predicate/namespace in its actual output, retained in
`enumerate.stdout`; the display above shortens only those qualifications for reading.

| Sig line | Codepoints | Next complete semantic unit | Arithmetic | Action |
|---|---:|---|---|---|
| 39 | 55 | Full Iff conclusion through `:= by`, 72 without indent | 55+1+72=128 | ok |
| 40 | 76 | No next signature line | n/a | ok |

| Inequality occurrence | Location | Form | Action |
|---|---|---|---|
| 1 | conclusion RHS | κ ≤ 2 | retain smaller-left |
| ≥/> | signature and named hypotheses | zero | no rewrite/rename |

### Per-binder weakening, drop, and inversion

| Binder | Class/use | Candidates and actual outcome |
|---|---|---|
| `{x : ℝ}` | Concrete value in Irrational, IsDiophantine, approxSet | Removing x makes the same statement unbound. It is already arbitrary real; field abstraction changes fixed real rpow/approxSet definitions and public contract. No class-parent, universe, decidability, strict→weak, or regularity point-localization applies. |
| `(hx : Irrational x)` | Proposition, passed only to accepted finite-bound helper | Actual minimal-hypotheses drop experiment: unknown hx at reverse application, then original caller argument becomes invalid. No mechanical parent, inequality weakening, or regularity localization applies. Retain exact accepted API. |

The drop tool reports skipped_implicit=1; x was separately inspected above. The drop
failure establishes that this proof uses hx, not that no different proof could avoid it.
For rational x both sides should fail; removing irrationality would require a substantive
rational-case argument and change the accepted public API. The owner's explicit
no-optional-API-expansion instruction rules out that separate extension; it is not a
deferred mandatory small weakening. No typeclass or universe parameter is present.
Inversion check: approxSet occurs in finite bounded-denominator removal and finiteness
conversion; the rational-error structure is used in both estimates. No concrete object
is unfolded once and then forgotten. The helper already captures the coherent
arbitrary-exponent finite-exception content. No additional generalization is recommended.

### All 42 golfing-rule slots

| Rule | Actual status |
|---|---|
| 1.1 by exact | n/a: no declaration wrapper. |
| 1.2 by rfl | n/a: none. |
| 1.3 rw+exact | n/a: no rw in bridge. |
| 1.4 simp+exact | Already two terminal simpa using applications. |
| 1.5 trailing rfl | n/a: none. |
| 1.6 constructor | Applied lambda anonymous Iff constructor, replacing constructor plus intro setup. |
| 1.7 apply+exact | Reverse apply supplies expected finite-set goal; combining the wrapped typed negation would only nest the same term and gives no material clarity/speed win; retain targeted step under minimum-value filter. |
| 1.8 by_contra+push | Replaced contradiction setup with le_of_not_gt in the constructor lambda. |
| 1.9 eta | Remaining lambdas bind hypotheses used in constructed terms, not eta. |
| 1.10 inline have | Applied to hQq and hs, with typed substantive hgap retained. |
| 1.11 apply+intro | Constructor hypotheses directly bound by lambdas. |
| 1.12 show | n/a: none. |
| 1.13 projections | C and large-denominator witnesses already obtained/destructured. |
| 1.14 rw merge | n/a: no rw. |
| 1.15 terminal simp-only | n/a: none. |
| 1.16 nonterminal bare simp | n/a: none. |
| 1.17 dot notation | hinf.sdiff, hpq.2.trans, .not_gt and hC.ne' already used. |
| 1.18 <| | Existing grouped expressions necessary as nested arguments; reverse composition considered but retained explicit expected goal. |
| 1.19 push_neg | n/a: none. |
| 1.20 trivial exists helper | n/a: bridge not existential and accepted helper substantive. |
| 2.1 whole grind | Actual entry whole attempt fails; no evidence for one-tactic replacement. |
| 2.2 pre-grind deletion | n/a: no retained grind. |
| 2.3 simpa consolidation | Existing casts/scaling already terminal simpa. Untyped hgap experiment failed and was reverted. |
| 2.4 fun_prop | n/a: no function regularity goal. |
| 2.5 positivity | Positive exponent gap requires hκ; linarith proves linear relation. No standalone structural positivity chain in bridge to replace. |
| 2.6 gcongr | n/a: scaling is one direct mul_lt_mul_of_pos_left application. |
| 2.7 lia/omega | n/a: only real linear exponent arithmetic; exact_mod_cast handles cross-type positivity. |
| 2.8 aesop | Actual whole/forward/reverse bounded probes fail; reverse probe reports sorry/incomplete and is expressly rejected. |
| 2.9 norm_num/norm_cast | Existing exact_mod_cast proves denominator positivity; no numeral-evaluation chain. |
| 2.10 decide | n/a: not closed finite computation; no native_decide. |
| 2.11 field_simp/ring | n/a: no polynomial identity; scaling simplification uses inverse cancellation. |
| 2.12 linear_combination | n/a: no ring/ring_nf closing tactic with identities. |
| 2.13 wlog | n/a: two directions have asymmetric arguments. |
| 2.14 calc | Already trans composition, no calc. |
| 2.15 <;> | n/a: no multiple similar side goals; the two directions need different proofs. |
| 3.1 erw→rw | n/a: neither. |
| 3.2 continuity | n/a: no legacy regularity tactic. |
| 3.3 omega→lia | n/a: no omega. |
| 3.4 rcases rfl | n/a: no substitution case. |
| 3.5 automation attributes | n/a: endpoint Iff adapter is not a canonical simp rewrite to register; no attribute added. |
| 3.6 simp_all | Actual reverse probe makes no progress; no simp_all only in source. |
| 3.7 resource options | None present; no change. |

Step-back reflection: exact?/apply? supplied no complete proof; whole automation cannot
invent finite minima or the exponent-gap argument. The final proof expresses those two
mathematical roles directly, with no extra helper beyond the independently audited bound.
One reverse probe was accidentally placed on continuation line53 and returned unknown
tactic identifiers; corrected line52 probes remained unsuccessful. Such tool-generated
errors/sorry diagnostics are failed scratch attempts, never production admissions.

## Final actual semantics, types, families, and recovery

`lake build Roth.LeanEval` passed after the source edit (22s; ordinary inherited upstream
warnings only). The fresh import inventory then enumerated **all six actual constants before
any semantic guard** in `current-inventory.json` and `enumerate.stdout` (exit0,52.236s):

| Actual complete Eval family | Universe parameters |
|---|---|
| IsDiophantine | [] |
| IsDiophantine._proof_1 | [] |
| isDiophantine_iff | [] |
| isDiophantine_iff._simp_1_1 | [u_1] |
| thueSiegelRoth | [] |
| _private.Roth.LeanEval.0.LeanEval.NumberTheory.ThueSiegelRothProblem.exists_pos_div_rpow_lt_aux | [] |

The first five have the full `LeanEval.NumberTheory.ThueSiegelRothProblem.` prefix.
No generated suffix or universe was guessed. The old generated simplifier singleton
remains, with exact raw TYPE preserved; no generated declaration retired or appeared.

`LiveGuard.lean` uses the fully recursive strict Expr checker, including binder names,
BinderInfo, all levels, literals, source/syntax metadata, and raw repr TYPE strings.
No ExprBEq, defeq-only TYPE claim, broad name normalization, or hygiene exception was used.
The theorem signature is source-byte identical to genuine d2eb and actual entry; predicate,
caller source, and original docstring are also unchanged. Public target TYPE2087 bytes,
caller TYPE823 bytes, and generated TYPE2777 bytes are raw-byte identical to accepted
pre-change metadata. `Meta.isDefEq` is used only after independent actual VALUE inference
to check that inferred VALUE type agrees with its already-protected declaration TYPE.

| Actual opaque value checked with `value! true` | VALUE bytes | VALUE hash | Outcome |
|---|---:|---|---|
| isDiophantine_iff | 2585150 | 4034613749863572135 | default inference, closed, standard axioms, no self/current-caller reference, upstream dependencies PASS |
| thueSiegelRoth | 10510 | 13987190834422677417 | current caller default inference, closed, standard axioms, no self, upstream dependencies PASS |
| isDiophantine_iff._simp_1_1 | 3006 | 2119453233130545600 | default inference, closed, axioms[], upstream, no parent/self/caller reference PASS |

Each costly check has its own run_cmd with default maxHeartbeats200000,
synthInstance.maxHeartbeats20000, maxRecDepth512. All actual type/value expressions reject
mvars, levelmvars, free variables, loose bvars, and sorryAx; axioms are restricted to
propext/Classical.choice/Quot.sound. No lower helper proof was re-inferred.
The first semantic harness run exited1 in59.742s **after** valid target/caller rows;
only a scratch Name construction for private numeric component0 and quoted `«_@»` spelling
was wrong. Those valid rows remain in `semantic-valid-rows.json`; they were not replayed.
`RemainingGuard.lean` repaired those literal constructors with Name.num and raw `_@`,
and checked only outstanding cheap helper binding/generated proof (exit0,50.922s).
Strict TYPE comparisons have zero permitted hygienic renamings.

The original predicate and generated proof are reused from original1 with exact source,
raw TYPE, VALUE hash/length and actual dependency binding; accepted helper is reused from
the owner's receipt and actual production proof receipt with the same bindings. These are
hash/length/dependency receipts, **not a claim of full raw VALUE identity**. Actual in-file
dependency graph is acyclic: predicate→its proof; bridge→predicate/its proof/accepted helper;
caller→predicate/bridge; helper and simplifier singleton have no Eval dependencies.
`semantic-receipt.json` records the full graph. The bridge does not refer to itself, its
current caller, a circular alias, or its generated proof; accepted lower helper is allowed.

`Independent.lean` separately recovers the exact **accepted entry proof** under another
theorem name, importing Main alone. It includes no current bridge/helper/caller dependency.
It is not presented as a novel proof strategy or as the unrepaired genuine d2eb proof:
genuine d2eb's old eventual-bound API call differs from the accepted entry call. Recovery
exit0,38.502s; actual default closed opaque inference passes, TYPE raw2087 bytes and []
are exact to the original metadata. Recovered VALUE3095814 bytes/hash6996827800711983296,
standard axioms only. No large caller clone was made.

## Held performance capture

Owner HOLDACK preceded all phase preparation, environment observation, freezing and capture.
The owner remained fully idle through both terminal exits, task/driver group drain and the
raw-UNPARSED receipt; parsing began only after explicit RELEASE. Actual commands:

```
lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 baseline-prefix.lean
lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 final-prefix.lean
```

The real commands use absolute Lake and prefix paths in `profile-terminal.json`.
`baseline-prefix.lean` is the accepted ENTRY prefix, not genuine d2eb; final prefix is
the exact current production prefix through this target plus the namespace close. No
profiling scaffolding touches production. The accepted helper is elaborated incidentally
in the final prefix; its timing is not re-certified, summed into target cost, or used to
replace accepted helper evidence. All43 frozen inputs remain current and byte-bound.

Actual ENTRY PID/PGID45664, final45703, driver45643; each PID and PGID was explicitly
observed absent after terminal completion. Entry exit0 in107.143s, final exit0 in33.281s.
Raw streams kept separate and hashed; no raw output dump. Both actual full parent
environment byte strings compare equal in memory (2814 bytes/hashfb0e091f…);
both actual lake environment byte strings compare equal in memory
(6212 bytes/hash24ee4da7…). Only hashes/lengths and safe PATH/toolchain are persisted.

Full canonical target commands, including the entire docstring/signature/body, are bound
to source. The profiler pretty-printer removes exactly one space in
`¬ (2 + ε ≤ 2)`→`¬(2 + ε ≤ 2)`; the narrow literal pair and occurrence count1 are recorded.
The initial whitespace-collapse-only assertion caught this and failed, then the binding
was repaired with only that explicitly enumerated spacing pair. No mathematical term,
name, binder, or syntax token was normalized away. `timing.json` records canonical
hashes/lengths and source positions (ENTRY starts stdout2112; final40996).

| Disjoint target roots | Accepted ENTRY context ms | Final exact prefix ms |
|---|---:|---:|
| Outer source command | 7.842 | 4.028 |
| Detached proof elaboration | 2270.088 | 297.892 |
| Generated singleton kernel parent | 0.124 | 0.171 |
| Main target kernel parent | 258.795 | 9.653 |
| Lint parent | 32.489 | 8.835 |
| All target-range detached Meta.whnf roots, conservative charge | 1.844 (1588) | 0.930 (808) |
| Actual lazy DATA roots / compilation roots | 0 / 0 | 0 / 0 |
| **Total** | **2571.182** | **321.509** |

Kernel child costs are enclosed by their listed parents and not added again. Every actual
top-level root in the target range is accounted for. Meta.whnf roots are Meta, not DATA.
The accepted ENTRY is a separately valid historical context; no controlled before/after
ratio is claimed. Final321.509ms is below750ms and1000ms; no same-freeze repeat or third
capture was warranted or run. Buzz outcome: FAST-BOARD for final target; zero limit raises,
no deferral, no further speculative optimization. Later actual whole-file profiling belongs
to the owner's file-final review, not this per-declaration checkpoint.

## Final gates and phase checklist

After the timing pass, actual final commands ran serially in required order:

| Gate | Actual evidence/result |
|---|---|
| lake_build | `run.py final-build …/lake build`, exit0,4.646s |
| lake_build_file | separate `run.py final-eval-build …/lake build Roth.LeanEval`, exit0,2.954s |
| native complete current Eval | `run.py final-native …/lake env lean Roth/LeanEval.lean`, exit0,29.317s, both output streams empty |
| final complete unfiltered LSP | success=true, partial=false, timed_out=false, items=[], failed_dependencies=[] |
| definition_protected | Original predicate source/TYPE unchanged; no def/abbrev changed. |
| theorem_statement_protected | Genuine/entry/current target signature and docstring byte-identical; caller source/TYPE unchanged; actual helper source equals accepted helper. |
| structure_gate | Target13 body lines, forward9/reverse3, no external conjunction. |
| naming_gate | Descriptive predicate prefix and iff suffix; no forbidden name; no renames queued. |
| line_packing_gate | Two measured rows, complete semantic unit arithmetic55+1+72=128. |
| inequality_orientation_gate | Signature κ≤2; zero ≥/>. |
| cumulative callers | Sole same-file caller freshly type/VALUE-checked; complete file native/build/LSP pass. No external Eval importer/caller found. |
| unchanged dependent evidence | Main/root source unchanged; accepted broad native/LSP evidence reused with qualified source/import bindings rather than replayed. |
| hallucination/new identifier check | le_of_not_gt and accepted private helper are resolved in compiled current proof and default semantic guard; no unverified identifier. |

All target phases complete: full references,24-item audit, five-method search, per-binder
generalization/drop/inversion, codepoint and inequality tables,42 rule statuses, actual
bounded whole/chunk automation, step-back reflection, current strict types/opaque values,
independent entry recovery, actual-family DAG, held performance capture, ordered broad
gates, and final clean complete diagnostics. No rename or optional API work remains.
No built-in simplify tool was available or invoked; the owner's required fresh independent
whole-file reviewer after original3 supplies that separate substantive pass.

Final source:3343 bytes/63 lines, SHA256
`e4f3998fd64e5a3acc1ccd4bc6588537ebf0e43ceeb4642343dd2795be294d35`, maximum width99.
Original target32 tactic lines→13,19 fewer; accepted helper17 tactic lines is accounted
separately, so no whole-file reduction is falsely inferred from the target extraction.
`final-source-receipt.json` verifies current source, helper/predicate/caller/doc contracts,
all43 frozen timing inputs, six actual constants, and no admission/debug/limit scaffolding.

## FINAL-END and release

All nine resumed task launches and their actual driver PID/PGID groups have been checked
absent after terminal completion (`final-drain.json`). All author calls have returned;
zero compiler/native/LSP/profile jobs remain. The accepted helper report SHA256 remains
`25606210a93fc765e02283944e8a18079e9fdc89831f4a6ed2bea17748e3fb7c`.
`/private/tmp/roth-eval-iff/FINAL-END.json` records the final source and complete status.
All source, target-report, compiler, native, LSP and profile leases are released to the
file owner. This report is frozen. No Git or central-progress mutation was made by this worker.
