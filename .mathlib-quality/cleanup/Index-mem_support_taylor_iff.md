# Phase 4 — `Roth.mem_support_taylor_iff`

Scope: private declaration at `Roth/Index.lean:55–57` (3 lines, plus existing omit wrapper
at line 54). Worker made **no source changes**. Owner retains publication, full-project
builds, final simplify, and final file-wide buzz responsibility. Source frozen at SHA256
`9ea21436746c9e155e485b0ae6ef6deb884e4391417044407c717cb2f6206f64`.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md in full, both skill files, the complete
cleanup command including its verbatim Phase-4 contract, and relevant declaration,
formatting, visibility, naming, documentation, and statement-style references.

## Full audit (24 items)

| # | Item | Concrete result |
|---|---|---|
| 1 | LINT | No diagnostics on lines 54–57. Complete file diagnostics report 27 existing warnings elsewhere, no errors. |
| 2 | HAVE SCAN | No `have` occurrences. |
| 3 | SET_OPTION | No declaration-local limit/debug options. |
| 4 | SIMP SQUEEZE | No simp calls in retained proof; one terminal `rw`. Tested terminal simp variant; no gain. |
| 5 | NAMING | Descriptive snake_case membership/Taylor/iff name; no forbidden abbreviations or patterns. Reused API helper rather than single-use step, so no `_aux` rename needed. No queue entry. |
| 6 | LINE PACKING | Both signature lines measured below; 86 + 1 + 60 = 147, conclusion does not fit. |
| 7 | BY PLACEMENT | `:= by` ends conclusion line. |
| 8 | FORMAT | Two-space proof indent; four-space signature continuation; no blank proof lines, repeated rewrites, or haveI/letI. |
| 9 | COMMENTS | None in declaration; none removed. |
| 10 | DOCSTRING | No docstring, appropriate for private lemma; existing file docs preserved. |
| 11 | VISIBILITY | Already private. Six uses in this file, none outside; classic dialect. |
| 12 | STRUCTURE | One proof-body line; no conjunction or branches; no extraction/decomposition needed. |
| 13 | MATHLIB | Five actual searches below. Generic support characterization exists in Mathlib; Taylor coefficient identity is project API. No exact same-type Mathlib result found; no absence claim. |
| 14 | JUNK DEF | n/a: lemma, not definition. |
| 15 | EXISTS LEMMA | n/a: conclusion is iff, not existence. |
| 16 | SHOW/CHANGE | Neither occurs. |
| 17 | PUSH_NEG | No occurrence. |
| 18 | GENERALISE | Every parameter/drop probe below; existing omission of Fintype and DecidableEq verified. CommSemiring coefficient-ring candidate compiled but report-only. |
| 19 | INEQUALITY | Scan table below: none. |
| 20 | NORMAL-FORM | Canonical support-membership iff nonzero Taylor coefficient rewritten to Hasse evaluation. No equivalence web introduced. |
| 21 | SYNTAX-GEN | Existing iff directly supports `.1` and `.2` at all six uses; no easier call-site restatement identified. |
| 22 | IMPORT-FANOUT | n/a: no import changes. |
| 23 | CASTS | 0 dropped, 0 cross-type, 0 load-bearing casts; no source diff. Binder types are parameter declarations. |
| 24 | INSTANCE-NAME | n/a: no instance declaration. |

Issues to fix: none within owned declaration.
Refactoring needed: none required. A generic coefficient-ring observation is recorded below;
owner confirmed keeping this private specialization. Wrapper removal would modify six
other declaration bodies, outside this worker's ownership, and would replace project
Taylor API reuse rather than an exact Mathlib duplicate.

## Mathlib search-status (actual calls)

| Method | Query | Result |
|---|---|---|
| A Lean-Finder | “A multivariate polynomial Taylor translate has a monomial in its support iff the corresponding Hasse derivative evaluates to nonzero” | Returned univariate `Polynomial.taylor_coeff`, `Polynomial.taylor_monomial`, unrelated `MvPolynomial.support_expand_subset`. |
| B Loogle | `MvPolynomial.support, MvPolynomial.eval, MvPolynomial.hasseDeriv` | Actual remote error: unknown identifier `MvPolynomial.hasseDeriv`; this is project API, not an absence result. |
| B Loogle retry | `MvPolynomial.support, (_ ∈ _ ↔ _ ≠ 0)` | Returned `MvPolynomial.mem_support_iff` and unrelated monomial-order fact. |
| C LeanSearch | “multivariate polynomial Taylor translation support nonzero Hasse derivative evaluation” | Univariate `Polynomial.taylor_coeff`, `Polynomial.taylor_eval`, `Polynomial.taylor_eval_sub`; no exact multivariate hit among returned results. |
| D Source rg | `mem_support_taylor`, `support_taylor`, `taylor_coeff`, `coeff_taylor`, `theorem mem_support_iff` | Mathlib `Algebra/MvPolynomial/Basic.lean:513` support characterization; univariate Taylor API; `Roth/Taylor.lean:128` project coefficient theorem. Full candidate-name search was untruncated. |
| E Name pattern | `mem_support_taylor` and `coeff_taylor` via native `lean_local_search` | Target private helper; project `MvPolynomial.coeff_taylor` and private monomial auxiliaries; Mathlib univariate coefficient variants. Index reported `warming`, so empty matches would not establish absence. |

Auxiliary variants inspected: support/coeff membership, Taylor coefficient-zero/one,
`taylor_eval`, `taylor_eval_sub`, monomial coefficient auxiliaries. Common-equivalents
table: no topology/finiteness/bornology bucket applies.

Conclusion: partial generic Mathlib support match plus project Taylor coefficient API;
keep current helper built on these. `exact?` did not close the live original goal;
`apply?` offered only partial logical scaffolding and a temporary sorry-bearing result,
which was never installed. Searches establish these positive matches, not global absence.
No new wrapper, predicate, or documentation was added.

## Generalisation status (every parameter)

All isolated negative drop tests used `set_option autoImplicit false` to prevent Lean
silently reinstating a removed binder. Native `lean_run_code` returned concrete errors.

| # | Parameter | Class/use | Actual candidates/probes | Result |
|---|---|---|---|---|
| 1 | `{σ : Type*}` | Type variable for polynomial/domain/multi-index | Drop: unknown σ in three binder types. `Sort*`: application type mismatch at MvPolynomial/Finsupp. Original universe-polymorphic Type* positive example compiled. | Retain; already universe polymorphic. |
| 2 | `{P : MvPolynomial σ ℝ}` | Structure value in translate and derivative | Drop: unknown P at translate/derivative applications. Generalize coefficients to R with CommSemiring: positive example compiled. | Retain original concrete specialization; abstract-ring restatement report-only. |
| 3 | `{α : σ → ℝ}` | Structure value in translate/evaluation | Drop: unknown α at both applications. Coordinated R-valued candidate compiled. Point-localise/strict→weak inapplicable: this is a value, no regularity/proposition hypothesis. | Retain. |
| 4 | `{d : σ →₀ ℕ}` | Structure value in support/derivative | Drop: unknown d in membership/derivative. No weaker value type supports the unchanged Hasse multi-index API; finite-support natural exponents are part of its definition. | Retain. |
| 5 | `[Fintype σ]` ambient | Already omitted before target | Positive original-type proof compiled with no Fintype binder. | Existing omission verified. |
| 6 | `[DecidableEq σ]` ambient | Already omitted before target | Same positive original-type proof, with no decidable-equality binder and no classical tactic. | Existing omission verified. |

There are no proposition hypotheses to drop, localize, weaken strictness, or unbundle.
No algebraic class parameter belongs to the actual declaration; ℝ is a concrete coefficient
type, not an explicit field assumption. Coordinated `[CommSemiring R]` replacement for
P and α compiles using exactly the current two rewrite lemmas, proving no order, field,
characteristic-zero, or completeness structure is needed. This changes abstract structure
and is therefore a report-only candidate, not an automatic edit. Owner confirmed retaining
current specialization. The inversion check identifies precisely this generic coefficient
identity; it does not justify additional project API or a changed index definition here.

Literature search: n/a: private declaration, exempt under cleanup Step 2.6d.

## Line packing (all signature lines; codepoints)

Actual width-100 `#check @target` was executed on the **built private constant** using
`mkIdent` and `Lean.Elab.Command.elabCommand` (numeric private-name component is not an
ordinary source identifier):

```lean
@Roth.mem_support_taylor_iff✝ : ∀ {σ : Type u_1} {P : MvPolynomial σ ℝ} {α : σ → ℝ} {d : σ →₀ ℕ},
  d ∈ ((MvPolynomial.taylor α) P).support ↔ (MvPolynomial.eval α) ((MvPolynomial.hasseDeriv d) P) ≠ 0
```

| Sig line | Codepoints | Next complete signature unit | Arithmetic | Action |
|---|---:|---|---|---|
| 55 | 86 | `d ∈ (taylor α P).support ↔ eval α (hasseDeriv d P) ≠ 0 := by` (60) | 86 + 1 + 60 = 147 > 100 | ok |
| 56 | 64 | None; next line is proof body | n/a | ok |

The entire declaration signature is 147 codepoints when joined with one space;
splitting the mathematical conclusion merely to fill a few characters provides no
improvement. All binders already share the first line; the whole conclusion shares
the second. No wide-hyp escape invoked. Existing omit wrapper is 35 codepoints.

## Inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 1 | signature and all parameters | n/a: no ≥ or > occurrences | none | none |

## Golfing rule pass (42 rules)

| Rule | Status and evidence |
|---|---|
| 1.1 | n/a: no by-exact wrapper. |
| 1.2 | n/a: no by-rfl wrapper; direct rfl tested and failed (not definitionally equal). |
| 1.3 | n/a: no rw followed by exact. |
| 1.4 | n/a: no simp/exact chain. |
| 1.5 | n/a: no trailing rfl. |
| 1.6 | n/a: no constructor branches. |
| 1.7 | n/a: no apply/exact chain. |
| 1.8 | n/a: no contradiction proof. |
| 1.9 | n/a: no lambdas. |
| 1.10 | n/a: no have. |
| 1.11 | n/a: no apply/intro. |
| 1.12 | n/a: no show. |
| 1.13 | n/a: no have/projection extraction. |
| 1.14 | Already one merged rw with both identities. |
| 1.15 | n/a: no simp only. |
| 1.16 | n/a: no nonterminal simp. |
| 1.17 | n/a: no application benefiting from dot notation. |
| 1.18 | n/a: no trailing argument parentheses. |
| 1.19 | n/a: no push_neg. |
| 1.20 | n/a: not an existence lemma. |
| 2.1 | Actual live grind failed; hinted grind succeeded but warned mem_support_iff already registered, and is heavier than rw. |
| 2.2 | n/a: no grind in retained proof. |
| 2.3 | Tested simpa with coeff_taylor using mem_support_iff; compiled with unnecessarySimpa warning. Bare simp failed; hinted terminal simp succeeded, no brevity/clarity improvement. |
| 2.4 | n/a: no analytic function-property goal. |
| 2.5 | n/a: outer goal is iff; nonzero RHS is not an unconditional positivity fact. |
| 2.6 | n/a: no order/monotonicity goal. |
| 2.7 | n/a: no linear Nat/Int arithmetic proposition. |
| 2.8 | Actual live aesop failed with unsolved coefficient/evaluation implications and rule-depth warning; no limit raised. |
| 2.9 | n/a: no numerical/cast computation. |
| 2.10 | n/a: symbolic real polynomial iff, not finite closed computation. |
| 2.11 | n/a: no denominator identity. |
| 2.12 | n/a: no ring/ring_nf ending or algebraic hypotheses. |
| 2.13 | n/a: no symmetric cases. |
| 2.14 | n/a: no calc. |
| 2.15 | n/a: only one goal. |
| 3.1 | Already rw, no erw. |
| 3.2 | n/a: no continuity/measurability. |
| 3.3 | n/a: no omega/lia. |
| 3.4 | n/a: no rcases substitution. |
| 3.5 | No new attribute: support fact already has grind registration; private specialized iff does not need global automation registration. |
| 3.6 | Tested simp_all [coeff_taylor], succeeds but unnecessary context-wide simplification compared with current rw. |
| 3.7 | n/a: no heartbeat override. |

## Step back / independent recovery

The proof is already one targeted tactic. Two explicit identities communicate exactly the
mathematical argument: support membership means nonzero coefficient, and the Taylor
coefficient is the Hasse derivative evaluated at α. A compiled term-mode alternative
`(coeff_taylor α d P) ▸ mem_support_iff` succeeds, but is longer and less immediately
recognizable than the current rewrite. An initial scratch `ne_congr` attempt failed
unknown identifier and was discarded; it never entered source. Bare exact?/apply? found
no complete replacement. No proof step is redundant.

Native `lean_run_code` independently compiled the exact original type, importing Roth.Index
but **without referring to this helper**:

```lean
example {σ : Type*} {P : MvPolynomial σ ℝ} {α : σ → ℝ} {d : σ →₀ ℕ} :
    d ∈ (taylor α P).support ↔ eval α (hasseDeriv d P) ≠ 0 := by
  rw [mem_support_iff, coeff_taylor]
```

It also compiled the coordinated CommSemiring R version. Both returned success=true,
timed_out=false and no error/warning diagnostics. This proves recovery at the original
type without circular use of the helper.

Actual built private constant `_private.Roth.Index.0.Roth.mem_support_taylor_iff` was
enumerated from the imported environment and checked via generated #check/#print commands.
The final successful call returned **[propext, Classical.choice, Quot.sound]** only.
Direct source spelling of the numeric component, and then string-like «0», failed;
using the actual environment Name with mkIdent corrected both scratch lookup attempts.

## Worker gates

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Actual `lake build Roth.Index > /private/tmp/Index-mem-support-build.log 2>&1`, session 47848, exit 0; “Build completed successfully (1501 jobs).” |
| definition_protected | pass | No source edit. |
| theorem_statement_protected | pass | No source edit; independent original-type proof compiled. |
| structure_gate | pass | One body line, no conjunction/branches. |
| naming_gate | pass | Descriptive legal name; no forbidden pattern, no rename. |
| line_packing_gate | pass | Complete measured table above. |
| inequality_orientation_gate | pass | Complete empty-occurrence scan above. |
| actual_private_axioms | pass | Built imported private Name; only three standard axioms. |
| complete_LSP | pass | Final native full-file call success=true, partial=false, timed_out=false, failed_dependencies=[], 0 errors and 0 messages on lines 54–57; 27 existing warnings elsewhere. |

Overall: pass at worker scope. Full-project build and separate LeanEval belong to owner;
this report makes no claim that the worker ran them.

## Result and phase checklist

Before 3 lines; after 3; saved 0. Audit defects fixed: 0 (none in owned target).
Rules retained: 1.14; all applicable alternatives tested above. Renames queued: none.
Comments preserved: none present; existing docs untouched. Required refactoring: none.

- [✓] Step 1 — complete mandatory references read.
- [✓] Step 2 — all 24 audit items answered.
- [✓] Step 2.5 — five actual search methods and remote query failure disclosed.
- [✓] Step 2.6 — every parameter/drop/structural candidate covered.
- [✓] Step 2.7 — every signature line measured with width-100 #check.
- [✓] Step 2.8 — inequality table emitted.
- [✓] Step 3 — all 42 golfing rules answered.
- [✓] Step 4 — global strategy and term-mode alternatives considered/tested.
- [✓] Step 5a — complete LSP, target clean; existing out-of-scope warnings disclosed.
- [✓] Step 5b — all worker gates above pass.
- [✓] Step 6a — no rename needed, no sidecar entry written.

Source edit authority released to owner at the frozen hash above. No source edits after
release. No Git, shared report, version, definition, public API, or unrelated declaration
edits performed. Dedicated report is the sole repository mutation by this worker.

## Buzz measurement and handoff

Outcome: **preliminary isolated proof is fast; final source-anchored owner sweep pending**.
No speed fix was needed or applied. The dedicated buzz tool/skill dispatcher is unavailable,
so the documented compiler/profiler procedure was followed directly after reading buzz.md
and profiling.md completely.

| Measurement | Actual evidence | Interpretation |
|---|---|---|
| Native `lean_profile_proof` at line 55 | Error: extracted standalone snippet unexpected end of input | Extraction failure; no timing or speed verdict inferred. |
| `lake env lean -Dprofiler=true -Dprofiler.threshold=0 Roth/Index.lean` | Session 56555 exited 0; `/private/tmp/Index-mem-support-profile.log` | File/global aggregate diagnostics, not a source-anchored per-declaration timing; not used as target timing. |
| First isolated CountHeartbeats scratch compile | Exit 1: missing `#` before `count_heartbeats` | Scratch syntax error corrected; no source impact. |
| `lake env lean --profile /private/tmp/IndexMemSupportProfile.lean` | Session 21034 exit 0; `/private/tmp/Index-mem-support-isolated-profile.log` | Identical original-type proof, independently reconstructed; **166 heartbeats**. |

The isolated compiler reports aggregate elaboration 0.868 ms, tactic execution 9.35 ms,
type checking 4.3 ms, plus 19.7 s import time. These are **aggregate profiler categories**,
not an actual anchored source declaration wall-clock trace; import time must not be
charged to the lemma. Heartbeats are the reliable target-specific evidence from this
probe. Owner's mandatory final full-source anchored `--profile` sweep supersedes this
preliminary observation and supplies the final FAST-BOARD verdict.

Limit raises removed 0, added 0. No profiling scaffolding entered project source.
No over-budget fix attempts or decomposition flags are warranted by this tiny proof.
All worker-launched compiler sessions (47848, 56555, 20536, 21034) terminated before
handoff; native snippet/diagnostic requests completed. Source hash rechecked unchanged.
