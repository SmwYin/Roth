# Phase 4: `MvPolynomial.degreeOf_hasseDeriv_le`

Date: 2026-10-15. Baseline supplied by orchestrator: `a44e380`; target at
`Roth/HasseDeriv.lean:207–211`. Scope: this declaration and this report only.
Source finalized; module build and final LSP passed. No Git mutations performed.

## References and scope

Read the complete Phase-4 worker prompt in
`/Users/ramin/.local/share/roth-mathlib-quality/commands/cleanup.md`, installed
`lean4/SKILL.md` and `mathlib-quality/SKILL.md`, and all of `golfing-rules.md`,
`proof-patterns.md`, `mathlib-search.md`, `generalisation-patterns.md`,
`cleanup-gates.md`, and `naming-conventions.md`. Read the applicable formatting,
documentation, inequality, syntax, visibility, normal-form, cast and generality
sections of `style-rules.md`. Read the entire target file and the source's
monomial definition in `.mathlib-quality/references/clean.tex:122–155`.
Classic import dialect; no `module` keyword. User statement/definition preservation
takes precedence over skill suggestions to change API. Existing public docstring
and source citation preserved verbatim.

## Complete 24-slot audit

| # | Item | Result/action |
|---|---|---|
| 1 | LINT | Initial and final LSP: no errors or warnings on target lines. Only preexisting file-header copyright warning at line 1. |
| 2 | HAVE SCAN | n/a: no `have` in the original or retained proof. |
| 3 | SET_OPTION | n/a: no declaration options; no options added to source. |
| 4 | SIMP SQUEEZE | The sole `by simp` closes the local exponent comparison; terminal and left unsqueezed. |
| 5 | NAMING | `degreeOf_hasseDeriv_le` describes the degree bound and uses the exact `degreeOf`/`hasseDeriv` API components. No forbidden abbreviation, numbered pattern, or single-letter public name. No rename warranted. |
| 6 | LINE PACKING | Both signature lines measured below; 76 + 1 + 48 = 125, so conclusion cannot join the first line. |
| 7 | BY PLACEMENT | `by` ends the conclusion line. |
| 8 | FORMAT | Two-space tactic indentation, no blank internal lines, one tactic per line, no `haveI`/`letI`. Changed ordinary lambda `=>` to `↦`. |
| 9 | COMMENTS | No inline proof comments; all existing doc/source prose preserved. |
| 10 | DOCSTRING | Public one-sentence mathematical description plus source reference already present. |
| 11 | VISIBILITY | Public API used in `Roth/CoeffNorm.lean:293` and `Roth/MainLemma.lean:615,678,691`; retained. |
| 12 | STRUCTURE | Three proof lines; no conjunction and no branches. No extraction needed. |
| 13 | MATHLIB | Five-method block below; retain the local Hasse API theorem and use existing support-degree lemmas directly. |
| 14 | JUNK DEF | n/a: theorem, not a definition. |
| 15 | EXISTS LEMMA | n/a: public inequality, not an existential helper. |
| 16 | SHOW/CHANGE | n/a: neither occurs. |
| 17 | PUSH_NEG | n/a: no negation tactic. |
| 18 | GENERALISE | Per-parameter table and literature below. No assumption weakening applies to the present API. Separately compiled stronger degree bound sent to orchestrator for user decision. |
| 19 | INEQUALITY | Canonical `≤`; scan table below, no `≥`/`>` in signature. |
| 20 | NORMAL-FORM | Already the canonical `degreeOf` natural-number inequality; zero-polynomial degree uses existing API convention. |
| 21 | SYNTAX-GEN | Explicit `j`, `d`, `P` are directly usable at existing call sites; no application-driven restatement needed. |
| 22 | IMPORT-FANOUT | n/a: no imports added or changed. |
| 23 | CASTS | 0 dropped / 0 kept cross-type / 0 kept load-bearing in diff. No explicit coercions/ascriptions added. |
| 24 | INSTANCE-NAME | n/a: theorem introduces no instance. |

Issues fixed: ordinary lambda arrow; replace prefix `le_trans` with dot notation
on the substantive support bound. No definition, statement, version, import,
visibility, attribute, or documentation change.

## Mathlib search-status

| Method | Query and evidence | Outcome |
|---|---|---|
| A Lean-Finder | `multivariate Hasse derivative degree in a variable does not increase`, 3 results | `Polynomial.natDegree_hasseDeriv_le`, `Polynomial.natDegree_hasseDeriv`, `Polynomial.hasseDeriv_eq_zero_of_lt_natDegree`; all univariate. |
| B Loogle | `MvPolynomial.degreeOf, _ ≤ _`, 8 results | Existing degree bounds, including `MvPolynomial.le_degreeOf_of_mem_support`; no exact local-Hasse theorem returned. |
| C LeanSearch | `Hasse derivative degree bound multivariate polynomial` | Service returned HTTP 500. Attempted once; unavailable result is not an absence claim. |
| D Source search | Untruncated full-name search for `degreeOf_hasseDeriv_le` throughout installed Mathlib; inspected `MvPolynomial/Degrees.lean` and `Polynomial/HasseDeriv.lean` | Full-name search had no hits; inspected `degreeOf_le_iff`, `monomial_le_degreeOf`, `le_degreeOf_of_mem_support`, `notMem_support_of_degreeOf_lt`, and univariate Hasse bounds. |
| E Name pattern | Native `lean_local_search` for `monomial_le_degreeOf` | Located `MvPolynomial.monomial_le_degreeOf` in `Degrees.lean`; index unavailable, source hit confirmed by source read and elaboration. |

Auxiliary variants: `_le_iff`, `le_degreeOf_of_mem_support`,
`notMem_support_of_degreeOf_lt`, `natDegree_hasseDeriv_le`, and
`hasseDeriv_eq_zero_of_lt_natDegree`. No common-equivalents table bucket matches.

Conclusion: partial match in Mathlib's support/degree API, already used directly.
The univariate Hasse theorem has different polynomial/operator types. Keep this
multivariate theorem. This is not merely a wrapper around an existing Mathlib
Hasse result: it connects the project-specific coefficient identity to Mathlib's
support-degree characterization. No ugly-proof API-extraction signal remains.
No claim of exhaustive semantic absence: generic `exact?` and `apply?` probes
were attempted before defining the target and reached their scratch heartbeat
budget rather than producing a theorem. Full-name grep alone is not treated as
proof of absence.

## Generalisation status

| # | Parameter | Class | Used as | Mechanical candidates and verification | Result |
|---|---|---|---|---|---|
| 1 | `{σ : Type*}` | type-variable | variable type for `j`, `d`, `P` | Already universe-polymorphic; dropping removes the type referenced by all three binders. No point-localisation or strictness hypothesis. | Keep; no meaningful weakening of an unrestricted type parameter. |
| 2 | `{R : Type*}` | type-variable | coefficient type and class carrier | Already universe-polymorphic; dropping leaves coefficient/class types unbound. | Keep. |
| 3 | `[CommSemiring R]` | typeclass | required by `hasseDeriv` and `degreeOf` | Isolated `lean_run_code` tried `[Semiring R]` and no class. Both failed to synthesize `CommSemiring R` at `hasseDeriv`. Other parent weakenings cannot supply the already-failed required class. | Keep; changing underlying operator is outside statement-preserving cleanup. |
| 4 | `(j : σ)` | structure-value | variable whose degree is bounded | Dropping would unbind `j` in both sides; no restrictive predicate or specialized type to weaken. | Keep explicit argument. |
| 5 | `(d : σ →₀ ℕ)` | structure-value | arbitrary Hasse multi-index | Dropping unbinds operator argument; replacing `ℕ` would change polynomial exponent/operator meaning. | Keep; already arbitrary finite support, no finite-variable requirement. |
| 6 | `(P : MvPolynomial σ R)` | structure-value | arbitrary polynomial | Dropping unbinds both sides; no nonzero/degree/characteristic condition to remove. | Keep. |

Structural binder drops above are dependency checks, not falsely reported as
compiled weakening experiments. The only typeclass weakening and drop candidates
were actually elaborated and failed. No `Fintype`, decidability, nontriviality,
domain, characteristic, strictness, global analytic, or bundled proposition
hypothesis exists to weaken. No signature edits were made.

Inversion check: `hasseDeriv` is used through its coefficient formula; the rest is
support arithmetic. The generic pointwise support bound is already represented
by Mathlib's `degreeOf_le_iff`. Introducing another wrapper for that fact offers
no new reusable abstraction. The separate sharper conclusion below is substantive.

## Literature search

Query 1: `multivariate Hasse derivative degree bound generalization arbitrary
commutative ring`. First three results captured: [On zeros of a polynomial in a
finite grid](https://arxiv.org/abs/1508.06020) (related zero-counting result),
[Fast Multivariate Multipoint Evaluation Over All Finite Fields, author PDF](https://zeyuguo.bitbucket.io/papers/MME.pdf),
and [the published article](https://doi.org/10.1145/3652025).
Read the author PDF §3.2, Definition 3.4 and Proposition 3.5: arbitrary commutative
ring coefficients and the monomial coefficient formula. Inference from that
formula: differentiation lowers each surviving exponent by the corresponding
multi-index component. It supports the degree comparison without a field or
characteristic-zero assumption.

Query 2: `"Hasse derivative" degree generalization site:en.wikipedia.org OR
site:ncatlab.org OR site:stacks.math.columbia.edu`. Top three hits:
[Hasse derivative](https://en.wikipedia.org/wiki/Hasse_derivative),
[Hasse-Schmidt derivative](https://ncatlab.org/nlab/show/Hasse-Schmidt%2Bderivative),
and [Derivation](https://en.wikipedia.org/wiki/Derivation_%28differential_algebra%29).
These were canonical-form discovery results; the primary paper and compiled Lean
probe supply the mathematical evidence. The local source explicitly states the
commutative-semiring generality at `clean.tex:134–135`.
ChatGPT math MCP: skipped as permitted by task instructions.

### Concrete additional API proposal, awaiting user decision

An optional separate theorem `degreeOf_hasseDeriv_le_sub` can prove
`degreeOf j (hasseDeriv d P) ≤ degreeOf j P - d j` over the same `CommSemiring R`.
This is stronger, not an assumption weakening. It was **actually compiled** by
isolated `lean_run_code`: `success: true`, `timed_out: false`, no diagnostics:

```lean
example (j : σ) (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    degreeOf j (hasseDeriv d P) ≤ degreeOf j P - d j := by
  refine degreeOf_le_iff.2 fun m hm ↦ ?_
  rw [mem_support_iff, coeff_hasseDeriv] at hm
  have h := monomial_le_degreeOf j (mem_support_iff.2 (right_ne_zero_of_mul hm))
  simp only [Finsupp.add_apply] at h
  lia
```

Recommended form is an additional theorem, preserving the current theorem and
four downstream callers. Replacing the present conclusion would require caller
changes. User approval is required because this adds substantive mathematical
API beyond the authorized proof/style cleanup. Evidence and recommendation sent
to the parent immediately; it is awaiting a decision, not automatically deferred.
No additional source declaration has been added.

## Measured signature packing

Reference from `#check @MvPolynomial.degreeOf_hasseDeriv_le` with
`format.width := 100`:

```text
@MvPolynomial.degreeOf_hasseDeriv_le : ∀ {σ : Type u_1} {R : Type u_2} [inst : CommSemiring R] (j : σ) (d : σ →₀ ℕ)
  (P : MvPolynomial σ R), MvPolynomial.degreeOf j ((MvPolynomial.hasseDeriv d) P) ≤ MvPolynomial.degreeOf j P
```

Widths below measured in Python codepoints, not bytes. The next signature unit
is the entire conclusion (as prescribed for conclusion packing).

| Sig line | Chars | Next signature unit | Arithmetic | Action |
|---|---:|---|---|---|
| 207 | 76 | `degreeOf j (hasseDeriv d P) ≤ degreeOf j P := by` (48) | 76 + 1 + 48 = 125 > 100 | ok |
| 208 | 52 | none; proof begins | n/a | ok |

No signature edit, so the final table equals the initial measurement. Proof's
longest line changed from 97 to 95 codepoints.

## Inequality scan

| # | Location | Original | Rewrite | Rename? |
|---|---|---|---|---|
| 1 | statement L208 | `degreeOf j (hasseDeriv d P) ≤ degreeOf j P` | none: canonical smaller-left form | none |
| 2 | all hypotheses/signature | n/a: no `≥` or `>` | none | no `_ge_` or `_gt_` name |

## All 42 golfing rules

| Rule | Status |
|---|---|
| 1.1 | n/a: no `by exact` wrapper. |
| 1.2 | n/a: no `by rfl`. |
| 1.3 | n/a: rewrite is at `hm`, followed by constructing a new support bound, not an `rwa` closure. |
| 1.4 | n/a: no sequential `simp` and `exact`. |
| 1.5 | n/a: no trailing `rfl`. |
| 1.6 | n/a: no constructor. |
| 1.7 | n/a: no apply/exact sequence. |
| 1.8 | n/a: no contradiction proof. |
| 1.9 | n/a: lambda binds support exponent and membership used nontrivially; not eta-reducible. Arrow changed to `↦`. |
| 1.10 | n/a: no single-use `have` in retained proof. |
| 1.11 | already uses `refine ... fun`; no separate `apply`/`intro`. |
| 1.12 | n/a: no `show`. |
| 1.13 | n/a: no `have` destructuring. |
| 1.14 | n/a: only one `rw`. |
| 1.15 | n/a: no terminal `simp only`; sole simp already unsqueezed. |
| 1.16 | n/a: no nonterminal bare simp. |
| 1.17 | APPLIED: `le_trans (by simp) bound` becomes `bound.trans' (by simp)`. |
| 1.18 | Considered `<| by simp`; same width, no trailing nesting benefit over one small simp argument, retain parenthesized argument. |
| 1.19 | n/a: no `push_neg`. |
| 1.20 | n/a: no existential helper. |
| 2.1 | Tried whole-proof `grind`: isolated prefix probe failed. Also `grind [monomial_le_degreeOf]` at final step failed. |
| 2.2 | n/a: no retained `grind`. |
| 2.3 | n/a: no simplification/closure sequence to consolidate; whole-proof `simp` made no progress. |
| 2.4 | n/a: no continuity, differentiability, measurability or other analytic function property. |
| 2.5 | n/a: goal is a comparison of two arbitrary natural degrees, not structural positivity. |
| 2.6 | Tried `gcongr` at final degree bound: no progress. |
| 2.7 | Tried support-bound `have`, `simp only [Finsupp.add_apply] at h`, `lia`: succeeds, but three lines replace one and add an unnecessary local. Retained composed term. |
| 2.8 | Tried whole-proof `aesop`: no progress. |
| 2.9 | n/a: no concrete numeric computation or cross-type cast goal. |
| 2.10 | n/a: arbitrary polynomial and index, not finite decidable computation. |
| 2.11 | n/a: no denominators or field identity. |
| 2.12 | n/a: no ring/ring_nf conclusion. |
| 2.13 | n/a: no symmetric branches. |
| 2.14 | n/a: no calc; existing transitivity made dot-style. |
| 2.15 | n/a: only one generated goal. |
| 3.1 | n/a: no erw. |
| 3.2 | n/a: no legacy analytic tactics. |
| 3.3 | Already considered lia in 2.7; no omega retained or introduced. |
| 3.4 | n/a: no rcases or substitution. |
| 3.5 | Considered, not added: inequality theorem already applied explicitly; no demonstrated automation need or canonical simp reduction. |
| 3.6 | n/a: no simp_all only. |
| 3.7 | n/a: no source maxHeartbeats or other resource option. |

Additional actual alternatives: `Nat.le_of_add_le_left` failed as an unknown
constant; `Nat.le_add_right (m j) (d j)` followed by `.trans` succeeded, but
exceeded line width. The shorter `Nat.le_add_right ..` variant also succeeded
with a long-line warning (106 codepoints). The retained dot-style proof is 95.
Term-mode would have to retain the local coefficient rewrite in a nested tactic
block; no size or clarity gain. Monomial induction would add branches and invoke
sum/add degree bounds, unlike the direct coefficient proof.

Whole-proof live `lean_multi_attempt` batches initially timed out at the 65-second
client bound. Retried as isolated `lean_run_code` with the pre-target source
prefix, so the target theorem was **not available** for circular `exact?` lookup.
Scratch-only 2000-heartbeat bounds gave concrete `grind`, `simp`, `aesop` failures
and deterministic `exact?`/`apply?` timeouts. These resource bounds never entered
the project file. No unsuccessful or timed-out experiment is reported as success.

## Gates and evidence

Direct proof/LSP adapter used:
`/Users/ramin/.local/share/uv/tools/lean-lsp-mcp/bin/python /private/tmp/roth_mcp_probe.py`.
It supplies the project-aware server environment. Some completed runs printed
an event-loop cleanup warning after delivering complete results; their Lean
result objects are recorded separately from that shutdown noise.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | PASS | `lake build Roth.HasseDeriv`, exit 0; 1430 jobs, target compile 14s; existing copyright warning only. |
| LSP | PASS | Final `lean_diagnostic_messages`, `success: true`, `partial: false`, `timed_out: false`; only line-1 copyright warning. |
| isolated proof | PASS | `lean_run_code` recompiled the final three-line proof as an `example`; success true, no errors. |
| exact public type | PASS | Same isolated run elaborated the full original universally quantified signature with `:= @degreeOf_hasseDeriv_le`. |
| standard axioms | PASS | `#print axioms MvPolynomial.degreeOf_hasseDeriv_le`: `[propext, Classical.choice, Quot.sound]`, no `sorryAx`. |
| definition_protected | PASS | Captured `git diff --no-color -- Roth/HasseDeriv.lean` changes only two proof lines; no def/abbrev. |
| theorem_statement_protected | PASS | Both signature lines byte-identical; isolated original-type check passes. |
| structure_gate | PASS | Three proof lines, no ∧ or branches. |
| naming_gate | PASS | Descriptive API components, no forbidden pattern or abbreviation. |
| line_packing_gate | PASS | Complete two-row measured signature table; both rows ok. |
| inequality_orientation_gate | PASS | Complete scan; zero ≥/> in signature/hypotheses. |
| comments/docs | PASS | Public docstring and source preserved verbatim; no inline comments existed. |

Overall existing-theorem cleanup: **PASS**. Parent owns project-wide build,
separate `lake build Roth.LeanEval`, shared logs, Git and publication.

## Result and required checklist

Before: 5 declaration lines / 3 proof lines. After: 5 / 3. Saved: 0 lines;
two concrete style improvements. Audit issues found 2, fixed 2. Applied golfing
rule 1.17 plus lambda-arrow normalization. Renames queued: none. Comments:
none inline; existing public/source docstring preserved. Refactoring needed:
the compiled optional stronger theorem is awaiting user decision via root;
it is not a blocker to the completed original proof/style cleanup.

- [x] Step 1: references read.
- [x] Step 2: all 24 audit slots reported.
- [x] Step 2.5: five-method search status, including service failure and bounded generic probes.
- [x] Step 2.6: per-parameter generalisation and public literature search.
- [x] Step 2.7: measured per-signature-line packing table.
- [x] Step 2.8: inequality scan table.
- [x] Step 3: all 42 rules have explicit status/reason.
- [x] Step 4: whole-proof automation, generic search and alternative strategies assessed with actual trials.
- [x] Step 5a: final complete LSP result has no target errors/warnings.
- [x] Step 5b: module build, isolation, type, axioms and diff gates recorded.
- [x] Step 6a: no rename needed, so no shared queue write.

## Dependent checkpoint validation

The file owner ran `lake build` (2586 jobs) and `lake build Roth.LeanEval`
(2585 jobs), sequentially; both exited 0. Logs:
`/private/tmp/roth-degreeOf_hasseDeriv_le-build.log` and
`/private/tmp/roth-degreeOf_hasseDeriv_le-leaneval.log`.
