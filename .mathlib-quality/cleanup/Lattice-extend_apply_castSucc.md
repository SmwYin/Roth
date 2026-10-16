# Cleanup: `Roth.extend_apply_castSucc`

Scope: only the private declaration in `Roth/Lattice.lean`, originally lines 86–89.
The exact type, visibility, callers, imports, comments and documentation are preserved.
This report is the dedicated Phase-4 worker artifact; project-wide gates and Phase-5
coordination belong to the file owner.

## Baseline and references

Owner-supplied baseline: d04 full build and separate Lean evaluation passed, exit 0,
108.79s / 34.18s; `/private/tmp/roth-lattice-d04-{full,leaneval}.log`.
Native LSP diagnostics completed (`partial: false`, `success: true`), with only the
known line-1 copyright-header warning, preserved by explicit user preference.
No target-range warnings. Classic import dialect. Optional cache/linter not rerun.

Read both skill files and the complete cleanup Phase-4 prompt; read golfing-rules,
proof-patterns, mathlib-search, generalisation-patterns and cleanup-gates in full.
Consulted relevant style sections on indentation, whitespace, signatures, terminal
simp, proof comments, visibility and inequalities, and naming sections on capitalization,
mathematical names, suffixes and forbidden abbreviations.

## Full 24-item audit (before source mutation)

| Item | Finding and action |
|---|---|
| 1 LINT | No target warnings; preserve known file-header warning per user. |
| 2 HAVE SCAN | No `have` declarations. |
| 3 SET_OPTION | No target options or limit overrides. |
| 4 SIMP SQUEEZE | Terminal `simp [hints]`; leave unsqueezed. Remove independently verified redundant singleton hint. |
| 5 NAMING | Describes extension evaluation at the `Fin.castSucc` API; no forbidden abbreviations, numbered schemes, or single-letter name. No rename. |
| 6 LINE PACKING | Both signature lines measured below, width-100 `#check` obtained. |
| 7 BY PLACEMENT | `by` ends conclusion line. |
| 8 FORMAT | Two-space tactic indent, no blank lines inside, one terminal tactic. |
| 9 COMMENTS | None in target; none removed. |
| 10 DOCSTRING | Private helper has none, appropriate. |
| 11 VISIBILITY | Private, four local uses in `card_filter_box_last`; keep. |
| 12 STRUCTURE | Two proof lines become one; equality, no conjunction or branches. |
| 13 MATHLIB | Five actual searches below; no exact combined-expression theorem located. |
| 14 JUNK DEF | n/a: lemma, not data definition. |
| 15 EXISTS LEMMA | n/a: equality, not existential. |
| 16 SHOW/CHANGE | No `show` or `change`. |
| 17 PUSH_NEG | No negation-pushing tactics. |
| 18 GENERALISE | All four binder drop-tests run; results below. |
| 19 INEQUALITY | No inequalities in signature; table below. |
| 20 NORMAL-FORM | Evaluation equality with original value on RHS is canonical. |
| 21 SYNTAX-GEN | Current pointwise equality directly supports four rewrites; no restatement benefit. |
| 22 IMPORT-FANOUT | No new imports. |
| 23 CASTS | 0 dropped / 0 cross-type / 0 load-bearing; `castSucc` is an actual index embedding. |
| 24 INSTANCE-NAME | n/a: not an instance. |

Issues: redundant explicit singleton-zero hint, verified removable. No signature change.

## Mathematics and searches

Embedding `d` into the first `m` coordinates leaves `d j` at `j.castSucc`.
The added singleton lives at the distinct last coordinate and contributes zero there.

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | `Finsupp mapDomain Fin.castSucc plus single Fin.last evaluated at castSucc` | `Fin.snoc_castSucc`, `Fin.snoc_last`, `Finsupp.cons`; different construction, no direct replacement. |
| B Loogle | `Finsupp.mapDomain, Fin.castSucc` | Empty results, no tool error. |
| C LeanSearch | `Finsupp mapDomain injective apply add single zero outside support Fin castSucc last` | `mapDomain_apply`, `mapDomain_injective`, `mem_range_mapDomain_iff`; building blocks. Search index uses a newer signature for `mapDomain_apply`; installed source and compilation are authoritative. |
| D Source rg | `extend_apply_castSucc`, `mapDomain_apply_of_injective`, `mapDomain_apply`, `castSucc_ne_last`, `castSucc_lt_last` in Mathlib Data/Finsupp and Data/Fin | Installed `mapDomain_apply_of_injective` is simp-tagged; `Fin.castSucc_lt_last` and singleton simplification discharge last-coordinate contribution. |
| E Local names | `mapDomain_apply` | Installed five variants found, including `mapDomain_apply_of_injective`; index unavailable, so positive source hits only, no absence claim. |

Auxiliary variants inspected: `mapDomain_apply'`, `mapDomain_of_not_mem_image_support`,
`castSucc_ne_last`, `snoc_castSucc`, `snoc_last`. Common-equivalents table: no matching
discrete, finite, separated, or bornological pattern. No custom predicates or instances.
Conclusion: partial Mathlib match; keep the reused local computational equation and
use Mathlib simplification directly. No exact equivalent found; no global absence claim.
The helper names a repeated composite expression at four rewrite sites. Deleting it
would repeat the embedding-injectivity hint at each site; no new wrapper is introduced.

`lean_multi_attempt` tried `simp`, single-hint simp, the newer-index `mapDomain_apply`
form, `grind`, `aesop`, `exact?`, `apply?`. Bare simp/aesop leave the mapDomain equation;
grind fails; exact? finds no closing lemma; apply? gives only partial graph/arithmetic
routes. Multi-attempt's line substitution leaves the original continuation line and
therefore emits a parse error for every candidate; a separate `lean_run_code` exact-type
proof with the single hint compiled successfully, avoiding that tool limitation.

## Generalisation (mechanical probes)

Native `lean_run_code`, `autoImplicit false`, four separate examples with one binder
deleted each: expected unknown-identifier errors confirm all binders are required by
the statement. These intentionally failing scratch probes did not touch project source.

| Parameter | Class and use | Candidates actually tested | Result |
|---|---|---|---|
| `{m : ℕ}` | structure value: dimension of both Fin types and last index | delete binder | Fails: unknown `m`; retain. No strict/pointwise/typeclass weakening applies to a dimension value. |
| `d : Fin m →₀ ℕ` | structure value: embedded function and RHS value | delete binder | Fails: unknown `d.mapDomain`/`d`; retain. No hypothesis to point-localise or weaken. |
| `i : ℕ` | structure value: added singleton coefficient | delete binder | Fails: unknown `i`; retain. No proposition or typeclass parent to weaken. |
| `j : Fin m` | structure value: evaluation index | delete binder | Fails: unknown `j.castSucc`/`j`; retain. No hypothesis to point-localise or weaken. |

No explicit typeclasses, propositions, decidability assumptions or universe binders.
The coefficient monoid could abstract from ℕ, but this would restate the fixed private
API with no current-caller benefit, contrary to the delegated scope; no expansion made.
Inversion check: the explicit extension construction remains throughout the one-step
proof; no unfolding followed by object-independent argument. Literature search: n/a,
private declaration, literature search not required.

## Line packing

Actual `set_option format.width 100; #check @independent` on an independently proved
copy of the original exact type:

```lean
@independent : ∀ {m : ℕ} (d : Fin m →₀ ℕ) (i : ℕ) (j : Fin m),
  (Finsupp.mapDomain Fin.castSucc d + Finsupp.single (Fin.last m) i) j.castSucc = d j
```

| Signature line | Chars | Next syntactic unit | Arithmetic | Action |
|---|---:|---|---|---|
| 86 | 82 | conclusion `(d.mapDomain … = d j := by)` (81 chars without indent) | 82 + 1 + 81 = 164 > 100 | ok |
| 87 | 85 | no next signature line | n/a | ok |

The conclusion expression stays together at its natural boundary; all binders are
already packed on line 86. No signature formatting change.

## Inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| — | whole signature | n/a: no `≥` / `>` inequalities | none | none |

The `→₀` Finsupp notation is not an inequality.

## All 42 golfing rules

| Rule | Status |
|---|---|
| 1.1 | n/a: no `by exact`. |
| 1.2 | n/a: not a reflexivity proof. |
| 1.3 | n/a: no rewrite/exact chain. |
| 1.4 | n/a: terminal simp already closes. |
| 1.5 | n/a: no trailing rfl. |
| 1.6 | n/a: no constructor. |
| 1.7 | n/a: no apply/exact chain. |
| 1.8 | n/a: no contradiction proof. |
| 1.9 | n/a: no lambda. |
| 1.10 | n/a: no have. |
| 1.11 | n/a: no apply/intro. |
| 1.12 | n/a: no show. |
| 1.13 | n/a: no projected have. |
| 1.14 | n/a: no rewrites. |
| 1.15 | Terminal simp already unsqueezed; preserve. |
| 1.16 | n/a: no nonterminal simp. |
| 1.17 | `.ne` singleton hint becomes redundant; delete entire hint. |
| 1.18 | n/a: parentheses in retained simp argument are needed for application. |
| 1.19 | n/a: no push_neg. |
| 1.20 | n/a: not existential. |
| 2.1 | Actual grind attempt failed; retain simp. |
| 2.2 | n/a: no grind in original. |
| 2.3 | Remove redundant hint from single terminal simp; standalone exact-type proof passes. |
| 2.4 | n/a: no analytic function-property goal. |
| 2.5 | n/a: equality of arbitrary function values, not positivity. |
| 2.6 | n/a: not inequality/monotonicity. |
| 2.7 | n/a: arbitrary Finsupp evaluation requires mapDomain API, not linear arithmetic. |
| 2.8 | Actual aesop attempt leaves mapDomain equation. |
| 2.9 | n/a: no concrete numeric or cross-type cast computation. |
| 2.10 | n/a: symbolic unbounded input, no finite closed computation. |
| 2.11 | n/a: no fields/denominators. |
| 2.12 | n/a: no ring terminal or algebraic equation hypotheses. |
| 2.13 | n/a: no symmetric cases. |
| 2.14 | n/a: no calc. |
| 2.15 | n/a: one goal. |
| 3.1 | n/a: no erw. |
| 3.2 | n/a: no legacy function-property tactics. |
| 3.3 | n/a: no omega. |
| 3.4 | n/a: no rcases. |
| 3.5 | No global attribute needed for a private four-site computational helper. |
| 3.6 | n/a: no simp_all only. |
| 3.7 | n/a: no limits to remove. |

## Step back

The original already has one tactic; bare simp lacks the injectivity proof while
the singleton contribution simplifies automatically. The single retained Mathlib hint
is a direct mathematical explanation, shorter than term-mode unfolding. Exact?/apply?
found no direct shortcut. No helpers, API expansion or caller edits are needed.

## Verification

Independent original-exact-type proof: native `lean_run_code` compiled successfully;
axioms `[propext, Classical.choice, Quot.sound]`. Does not invoke the target helper.
Baseline target profiling: 34.1ms total; hotspot original simp line 31.5ms, below 1000ms.

Focused source edit removed only
`Finsupp.single_eq_of_ne (Fin.castSucc_lt_last j).ne` from the simp hint list.
No names introduced. Remaining hint names already existed in the target and were
verified in local/source search and the independently compiled proof.

Actual `/Users/ramin/.elan/bin/lake build Roth.Lattice`, exec session 13844,
completed exit 0, log `/private/tmp/roth-castSucc-build.log`:
`Built Roth.Lattice (31s)` and `Build completed successfully (2214 jobs).`
Only known header warnings in Roth.Box and Roth.Lattice were emitted.

Post-edit native LSP diagnostics were complete: `success: true`, `partial: false`,
`timed_out: false`, `failed_dependencies: []`, no errors or target-range warnings.
The sole known header warning remains under the explicit preservation instruction.

Actual built private target check, after that module build:
`/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-castSucc-built.lean`, session
31949, exit 0; log `/private/tmp/roth-castSucc-built.log`:

```text
Built target: _private.Roth.Lattice.0.Roth.extend_apply_castSucc
Axioms: [propext, Classical.choice, Quot.sound]
```

This inspects the imported constant, using the actual `Name` from the environment.
An initial native scratch attempt used the reserved identifier `matches` and failed;
the corrected fresh CLI probe above passed and also avoided the native stale-import
notice. Neither scratch attempt changed project source or its trust basis.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Actual module command, session 13844, exit 0 above. |
| definition_protected | pass | No def/abbrev edit. |
| theorem_statement_protected | pass | Original fragment and current target signature compared byte-for-byte. |
| structure_gate | pass | One proof line, no branches or conjunction. |
| naming_gate | pass | Descriptive computational name, no forbidden pattern/abbreviation. |
| line_packing_gate | pass | Both signature lines measured in codepoints, 164 > 100 boundary. |
| inequality_orientation_gate | pass | No reversed inequalities; scan table present. |
| independent exact type | pass | Fresh non-self-referential proof compiles; standard axioms. |
| built target trust | pass | Imported private constant inspected; standard axioms. |
| cumulative caller check | pass locally | Four local rewrite sites included in successful module build. Owner runs full project and separate Lean evaluation. |

Overall worker gates: pass. Full-project and separate Lean evaluation final gates
are explicitly owner-owned and were not duplicated by this worker.

## Simplify assessment

Outcome: PASS-THROUGH for the final single-hint proof. No duplicated proof structure
inside this target; the named equation serves four local rewrite sites. No further
quality or efficiency issue. The built-in `/simplify` capability is not available in
this runtime, so this is an explicit in-thread assessment, not a claimed tool handoff.
No additional files modified by this assessment.

## Buzz pass

Outcome: FAST-BOARD (nothing over 1000ms), native `lean_profile_proof` on this target.

| Declaration | Before | After | Over budget? |
|---|---:|---:|---|
| `extend_apply_castSucc` | 34.1ms | 54.3ms | no |

The after measurement ran during module build; both are far below budget. This is
a clarity/maintenance reduction, not a claimed speedup. No slow declaration to
trace-diagnose, no performance fix needed. Limit raises removed 0, added 0.
No profiling scaffolding in project source; no deferrals or large changes.

## Result and phase checklist

Before: 4 declaration lines, 2 proof lines. After: 3 declaration lines, 1 proof line.
Saved: 1 line. Audit issue found: 1; fixed: 1. Applied: simp-hint reduction (2.3),
maintained terminal-simp convention (1.15), eliminated redundant dot-notation hint
(1.17). Renames queued: none. Comments preserved: none present, none removed.
Refactoring needed: none. No public API, documentation, import or version changes.

- [✓] Step 1 — required references read.
- [✓] Step 2 — all 24 audit items recorded before source edit.
- [✓] Step 2.5 — all five search methods actually called, results recorded.
- [✓] Step 2.6 — every parameter classified and mechanically drop-tested.
- [✓] Step 2.7 — every signature line measured, width-100 check recorded.
- [✓] Step 2.8 — inequality scan table recorded.
- [✓] Step 3 — all 42 golfing rules have concrete statuses.
- [✓] Step 4 — mathematical/whole-proof reflection completed.
- [✓] Step 5a — complete native diagnostics, no errors or target warnings.
- [✓] Step 5b — gate table includes actual module build and trust checks.
- [✓] Step 6a — no rename needed, no queue mutation.

Source frozen and handed back to owner. Target SHA256:
`a0ad50ba68ceab7478367d390b9ce57f6e8c8c7a6ea7d94db994a4f380a976b5`.
File SHA256 at handoff:
`7e42ef79b31d4fe9dcd627cc064dc656732639564afbf968f10a91ae38d56aa0`.

Owner checkpoint: explicit source edit revocation at above freeze before sequential full/separate LeanEval session5569; both exit0 (104.10s/35.13s), hash stable. Logs `/private/tmp/roth-lattice-d05-{full,leaneval}.log`.
