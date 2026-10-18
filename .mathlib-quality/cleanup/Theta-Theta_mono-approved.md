# Approved revisit 13 — `Roth.Θ_mono`

Scope: fresh dedicated audit of original13, only approved removal of `DecidableEq σ`.
Source baseline owner checkpoint `85d940cc22e24a4eeb33e568d8b08c3456727698`, SHA256
`962dca983519c78afaa1b9c90d9addb33652a95f9f768fc417fd973a9975ed11`.
Read-only preparation preceded explicit RELEASE. No Git mutation or shared-log/rename-queue write.
The user explicitly retains `hB`, `hr`, `Fintype σ`, all other parameters, proof and documentation.
Those choices remain honored; this revisit does not reopen the historical F proposal.

Applied exactly one line, before the existing docstring:

```lean
omit [DecidableEq σ] in
```

All other source bytes are unchanged, including both existing `Θ_lt` callers. No helper,
classical tactic, proof change, rename, attribute, import or hypothesis suppression was added.
Body remains 3 lines; source delta +1 line. Evidence directory: `/private/tmp/roth-mono-api/`.

## Baseline and preparation

Read the leaf instructions, lean4 and mathlib-quality skills, full cleanup workflow, and full
`golfing-rules.md`, `proof-patterns.md`, `mathlib-search.md`, `generalisation-patterns.md`,
`cleanup-gates.md`; relevant style/naming, profiling and review normal-form/syntax references.
Read current Theta and both earlier target/contract reports. Header metadata remains untouched.
The file uses the classic import/namespace dialect.

Owner supplied preceding frozen sequential full build 102.795s THEN separate `Roth.LeanEval`
31.734s, both exit0, all17 project/pin hashes unchanged. These are inherited baseline evidence,
not leaf final project-build claims. Complete unfiltered baseline LSP reused from
`/private/tmp/roth-forall-api/final-lsp.json` with identical source hash: success=true,
partial=false,timed_out=false,failed_dependencies=[],0errors21warnings. Optional cache/linter
commands were not rerun: cached imports and authoritative complete diagnostics already exist.

Fresh native `lean_goal` on the actual target confirmed the subset obligation and effective
Fintype/DecEq section instances (`goal.json`). Search requests and this live request completed
before baseline profiling. No duplicate parent compilers or unbounded multi_attempt request.
The known native multi_attempt limitation is recorded once from dispatch; bounded independent
anonymous prefix examples supply fresh actual tactic probes instead.

## Full substantive audit (24)

| # | Item | Concrete result/action |
|---|---|---|
| 1 | Lint | Remove only approved redundant DecEq instance; retained hr warning is intentional. |
| 2 | Have scan | No `have` in the three-line target proof. |
| 3 | Set options | No target option/limit; no production option added. Scratch automation uses lower2000-heartbeat budgets. |
| 4 | Simp squeeze | No target simp; bounded exploratory simp fails below. |
| 5 | Naming | `Θ_mono` identifies monotonicity of the defined mathematical quantity, snake suffix, no forbidden numerical/abbreviation/ge/gt pattern. No rename. |
| 6 | Packing | Every signature line measured below:100/28 codepoints; unchanged. |
| 7 | By placement | `:= by` ends conclusion line; unchanged. |
| 8 | Format | Two-space tactics, no blank body line, anonymous witness constructor and ↦ already present. |
| 9 | Comments | No inline proof comments; two-line source docstring byte-preserved. |
| 10 | Docstring | Public result has mathematical meaning and source attribution; protected. |
| 11 | Visibility | Public main result documented in module; retained as explicitly requested. |
| 12 | Structure | Headline body3≤15; no conjunction conclusion or branch>10; no extraction needed. |
| 13 | Mathlib | Fresh five-method search confirms generic csSup_le_csSup already used directly; domain coefficient-family inclusion remains local mathematical content. |
| 14 | Junk definition | n/a: theorem, no data wrapper. |
| 15 | Exists lemma | n/a: public inequality, not a private witness helper. |
| 16 | Show/change | Neither occurs. |
| 17 | Push-neg | Absent. |
| 18 | Generalisation | Every effective parameter audited/probed below; exactly selected class omission applied. Explicit preservation choices honored. |
| 19 | Inequality | Four occurrences all ≤/<; complete table below. |
| 20 | Normal form | Supremum inequality in a conditionally complete lattice is canonical; no alternate equivalence API. |
| 21 | Syntactic generality | Existing two pointwise callers match this statement; no concrete benefit from another bundled Monotone companion within retained public scope. |
| 22 | Import fanout | No new import. |
| 23 | Casts | No cast/ascription in diff:0 dropped,0 kept. |
| 24 | Instance names | No instance declarations/names added; retained anonymous Fintype class verified by actual AST. |

## Fresh five-method Mathlib searches

Raw native results, including full source-search output: `search.json` (all five calls returned).

| Method | Actual query | Outcome |
|---|---|---|
| A LeanFinder | Supremum of a nonempty subset is bounded by supremum of a bounded above set | csSup_le_csSup, primed variant, csSup_le; positive hits. |
| B Loogle | `sSup ?s ≤ sSup ?t` | sSup_le_sSup, cofinal/complete-order variants, DirectedOn.csSup_le_csSup. |
| C LeanSearch | supremum monotone under subset inclusion conditionally complete lattice | csSup_le_csSup, ciSup_mono, primed and complete variants. |
| D Source | Untruncated csSup_le_csSup/sSup_le_sSup/sSup_le in standard conditionally complete/real files | Exact csSup_le_csSup at Basic.lean:209; primed at548. No absence inferred from other empty matches. |
| E Native local search | csSup_le_csSup | Exact/primed/DirectedOn hits; index unavailable, so positive source hits only, no index-based absence claim. |

Auxiliary forms examined: `_of_subset`, primed `csSup_le_csSup'`, complete-order `sSup_le_sSup`,
`DirectedOn.csSup_le_csSup`, `ciSup_mono`, `csSup_le`. Primed/bottom and complete-order variants
require structure ℝ lacks. The current generic lemma is the right match. Common-equivalents
lookup: `BddAbove` already expresses the boundedness concept; no custom predicate/instance.
No newly discovered wrapper or generic helper is introduced. Public project wrappers are
explicitly retained. No claim that search failure proves global Mathlib absence.

Fresh anonymous examples use the exact source prefix ending BEFORE Θ_mono, with no imported
target or named failed trial available. `trials.lean`/`trials.log` expected exit1: grind fails,
simp leaves the supremum goal, aesop makes no progress, gcongr makes no progress, exact? and
apply? both reach the deliberately conservative2000-heartbeat bound. These are actual bounded
unsuccessful probes, not absence proofs or positive verification. The selected direct proof
is separately checked in exit0 runs. No contaminated/self-citing search was accepted.

## Every effective parameter: compiled dependency/weakening probes

`negative.lean`/`negative.log` is a named expected-failure batch, exit1. `positive.lean`/
`positive.log` is separate exit0 evidence including the independent original and selected
proof. Failures show dependencies of this expression/proof, not mathematical necessity.
Protected hB/hr are tested only to document the audit; no new removal is recommended.

| Parameter | Role | Actual probe/result | Decision |
|---|---|---|---|
| `{σ : Type*}` | Polymorphic polynomial variables | clear σ fails dependent Fintype; already universe polymorphic; Sort would not fit MvPolynomial domain. | Retain. |
| `[Fintype σ]` | Θ/index finite-variable meaning | Removing instance and weakening to Finite both fail Fintype synthesis in actual Θ type. | Retain exactly. |
| `[DecidableEq σ]` | Unused original section instance | SelectedMono13 exact proof compiles with only Fintype; actual final AST rejects DecEq anywhere. | Approved omission only. |
| `{B : ℝ}` | Lower coefficient bound | clear B fails dependent hB; remains in conclusion; abstract field changes definitions/codomain. | Retain implicit. |
| `{B' : ℝ}` | Upper coefficient bound | clear B' fails dependent hBB'; remains in conclusion. | Retain implicit. |
| `(hB : 1 ≤ B)` | Nonempty source family | Clearing causes unknown hB at original nonemptiness application; weakening to0≤B fails expected1≤B. Broader alternative already explicitly declined. | Retain exact name/type/mode/order. |
| `(hBB' : B ≤ B')` | Transports coefficient bounds | clear hBB' fails transitivity argument; already weak ≤, strict/equality would strengthen. | Retain exact. |
| `(q : σ → ℕ)` | Rational denominators | clear q fails target dependency; no q positivity premise to weaken; changing codomain changes construction. | Retain explicit. |
| `{r : σ → ℕ}` | Shared degree/weight values | clear r fails dependent hr; still in conclusion and coefficient family. | Retain implicit. |
| `(hr : ∀ j, 0 < r j)` | Protected public positive weights | Fresh hr_cleared and hr_weak proofs both compile exit0 with standard axioms; unused by present proof. | Explicit user choice: retain exact. |

No algebra/analysis typeclass parent weakening applies to the remaining concrete value binders.
No global continuity, differentiability, openness or injectivity premise is present to localise.
All ordinary names/order/BinderInfo and the complete old telescope are checked after build;
generated anonymous instance names alone are exempt from equality as instructed.

### Public literature and inversion check

Fresh WebSearch queries: “supremum nonempty bounded set inclusion monotone supremum theorem”
and “Formalizing Roth nondecreasing”. Search results included the monotonicity theorem,
completeness lecture notes and discussion pages; only primary formal documentation/local source
supports the conclusions here. The local primary `.mathlib-quality/references/clean.tex:650–669`
defines the polynomial family and states that increasing B enlarges allowed polynomials.
Fresh official [Mathlib conditionally complete lattice documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Order/ConditionallyCompleteLattice/Basic.html#csSup_le_csSup)
confirms the nonempty-subset/bounded-superset canonical form used directly. An attempted UPenn
primary completeness-notes open returned403; no claim relies on its unavailable text.
Raw browser outcome: `literature.json`. No callable ChatGPT math MCP exposed in tool metadata.
This literature check makes no new public widening proposal and does not reopen declined F.

Inversion check fires for Θ after the first generic supremum step: the remaining proof is
coefficient-family inclusion, retaining a polynomial and rational-point witness while composing
each coefficient bound with hBB'. The abstract supremum fact is already csSup_le_csSup;
another abstract helper would duplicate Mathlib. This is already the direct decomposition.

## Measured signature packing and inequalities

Actual `#check @Roth.Θ_mono` at `format.width100` is captured in `verified.log`.
The added scoped omit command is not part of the theorem telescope and has23 codepoints.

| Signature line | Codepoints | Next complete block | Arithmetic | Result |
|---|---:|---|---|---|
| 129 | 100 | `Θ B q r ≤ Θ B' q r := by` (24) | 100+1+24=125>100 | Correct break, unchanged. |
| 130 | 28 | None: proof next | n/a | Correct final signature line. |

| Occurrence | Location | Form | Action |
|---|---|---|---|
| 1 | hB | `1 ≤ B` | Already oriented. |
| 2 | hBB' | `B ≤ B'` | Already oriented. |
| 3 | hr | `0 < r j` | Already oriented. |
| 4 | Conclusion | `Θ B q r ≤ Θ B' q r` | Already oriented. |

Zero ≥/> in signature/hypotheses; no ge/gt rename.

## All42 golfing rules, freshly assessed

| Rule | Concrete status/reason |
|---|---|
| 1.1 by-exact | n/a: no wrapper. |
| 1.2 by-rfl | n/a: no such proof. |
| 1.3 rw/exact | n/a: no rw. |
| 1.4 simp/exact | n/a: no simp. |
| 1.5 trailing rfl | n/a: no trailing tactic rfl. |
| 1.6 constructors | Existing direct anonymous polynomial/witness constructors retained. |
| 1.7 apply/exact | n/a: direct refine with one subset obligation. |
| 1.8 contradiction | n/a: no contradiction. |
| 1.9 eta | Coefficient lambda composes a bound with hBB', not eta-reducible. |
| 1.10 have | n/a: none. |
| 1.11 refine/fun | Already direct refine/rintro dependent witness pattern; no apply/intro chain. |
| 1.12 show | n/a: absent. |
| 1.13 projections | Existing named hR0/hRd/hRc pattern already avoids projections. |
| 1.14 rw merge | n/a: absent. |
| 1.15 terminal simp | n/a: absent. |
| 1.16 nonterminal simp | n/a: absent. |
| 1.17 dot | Already uses `(hRc d).trans hBB'`. |
| 1.18 parentheses | Existing dependent constructor/lemma applications have no gratuitous outer parentheses. |
| 1.19 push-neg | n/a: absent. |
| 1.20 existential wrapper | n/a: no private existential helper. |
| 2.1 grind | Actual clean-prefix grind [Θ,indexSet] fails. |
| 2.2 before grind | n/a: no retained grind. |
| 2.3 simpa | Actual simp [Θ,indexSet] leaves supremum inequality; no chain to consolidate. |
| 2.4 fun-prop | n/a: no function regularity statement. |
| 2.5 positivity | n/a: comparison of two suprema, not positivity goal. |
| 2.6 gcongr | Actual clean-prefix attempt makes no progress. |
| 2.7 lia/omega | n/a: no Nat/Int arithmetic goal. |
| 2.8 aesop | Actual clean-prefix attempt fails without progress. |
| 2.9 norm-num/cast | n/a: no concrete arithmetic or cast subgoal. |
| 2.10 decide | n/a: symbolic real-supremum inequality is not finite computation. |
| 2.11 field/ring | n/a: no denominator identity or polynomial equation. |
| 2.12 linear-combination | n/a: no ring-ending proof. |
| 2.13 wlog | n/a: no symmetric branches. |
| 2.14 calc | n/a: no calc chain. |
| 2.15 multiple goals | n/a: one witness term closes one subset obligation. |
| 3.1 erw | n/a: absent. |
| 3.2 legacy analysis | n/a: absent. |
| 3.3 omega | n/a: absent. |
| 3.4 rfl patterns | Existing rfl witness substitution is direct; no redundant follow-up simp. |
| 3.5 attributes | No new global automation attribute justified by selected instance removal. |
| 3.6 simp-all | n/a: no simp-all context. |
| 3.7 limits | No live limit present/added; conservative scratch budgets only. |

Step-back reflection: this three-line proof already expresses the argument directly. A term
lambda would lengthen the dependent witness pattern. Exact?/apply? were tried anonymously with
bounded clean-prefix search; neither supplied a competing proof. The selected task explicitly
preserves the proof, and no new substantive proof improvement warrants a separate recommendation.
No custom helper, alternative domain, bundled companion or rename is proposed.

## Independent original contract and actual built verification

`immutable-original.lean` extracts the original independent Index+Theta proof namespace through
Θ_mono from the immutable compatibility source. `immutable-check.json` additionally checks the
entire original Θ_mono declaration/proof byte-equal to Git baseline
`2b64544bf9f77a8ff957bf1bcaf693ac72217ff6`. It retains all original classes/hB/hr and executes
the original proof, with its original supporting independent definitions/proofs. It does not
invoke the current Θ_mono to establish its own claim.

`positive.lean` separately proves SelectedMono13.Θ_mono with the exact current proof and only
Fintype; initial exit0 wall28.534s. All independent original/selected/hr exploratory proofs
print only propext,Classical.choice,Quot.sound. These are positive proof checks, unlike expected
failure batches. Subsequent actual-built `verified.lean` combines that independent namespace
with the explicit old adapter and AST verifier in `verification-tail.lean`.

Explicit original-telescope lambda, kernel checked against independent original theorem:

```lean
fun {σ} [Fintype σ] [DecidableEq σ] {B B'} hB hBB' q {r} hr ↦
  @Roth.Θ_mono σ _ B B' hB hBB' q r hr
```

The verifier directly compares actual getConstInfo types modulo universe alpha-renaming,
universe arity, complete dependent telescope, all retained argument names/order/BinderInfo.
Original arity10 is recovered by oldAdapter; actual selected arity9 differs precisely by
the removed third DecEq binder. It rejects DecEq anywhere in the actual type AST and explicitly
checks retained Fintype/hB/hr names/positions. Each proof and actual built Roth.Θ_mono and caller
Roth.Θ_lt has its ACTUAL collected axioms checked against the standard3. No sorry/new axiom,
native_decide, weaker conclusion or artificial instance-name scaffolding.

Repository-wide Lean-source inventory finds exactly two actual uses in Θ_lt at896 and912,
both unchanged; module checking validates their actual proof contexts. No external actual use.
An additional no-DecEq arbitrary-type call compiles in the verifier. All original ordinary
argument positions remain, so no routine caller edit is needed.

## Simplify review

PASS-THROUGH: holistic review confirms direct generic supremum application plus coefficient
inclusion. No builtin `/simplify` callable skill/tool exists here; this report claims the manual
review performed, not an unavailable invocation. No duplicated skeleton/new helper, collateral
source edit or further recommendation. Phase5a non-rename changes:none beyond approved omit;
Phase5b rename queue:none, no write. File-level phases/header/import cleanup belong to owner.

## Final verification and performance

`/Users/ramin/.elan/bin/lake build Roth.Theta` exited0 in48.986s (`module.log`,
`module-run.json`). Only after the actual module build, `lake env lean
/private/tmp/roth-mono-api/verified.lean` exited0 in29.384s (`verified.log`,
`verified-run.json`), with all direct actual-type/AST/old-adapter/axiom checks PASS.
Expected failure probes are kept in separate logs: `negative` exit1 in28.923s;
anonymous `trials` exit1 in35.231s. Neither is used to certify positive claims.

Fresh complete UNFILTERED native `lean_diagnostic_messages` (absolute Theta path, timeout60,
no range/declaration/severity filter) returned success=true, partial=false,timed_out=false,
failed_dependencies=[],0errors19warnings (`final-lsp.json`). The warning multiset differs from
the identical-source baseline only by removal of TWO Θ_mono DecEq warnings: unused section
instance and unused decidability in type. No added warning; retained hr/header/other warnings
remain unsuppressed. Baseline snapshot is additionally byte-identical to preceding leaf's
`/private/tmp/roth-forall-api/final.lean`.

`diff-check.json` and `change.diff` mechanically assert only the selected omit insertion;
all other source bytes including comments, definitions, signatures, body and callers unchanged.
All mathematical names in the proof are pre-existing, source/search/compiler verified;
new-identifier inventory is empty. No private helper suffix lookup is needed: no helper was
introduced, removed or referenced anew.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | PASS | Actual module command exit0 in48.986s. |
| definition_protected | PASS | Exact insertion-only source equality; no def/abbrev change. |
| theorem_statement_protected | PASS, approved change | Only selected DecEq removed; actual AST and full original10 adapter check. |
| structure_gate | PASS | Headline body3≤15, no >10 branch or conjunction conclusion. |
| naming_gate | PASS | No forbidden pattern/abbreviation/ge/gt; no rename. |
| line_packing_gate | PASS | Complete measured100/28 table; no repack. |
| inequality_orientation_gate | PASS | Four oriented inequalities; zero ≥/>. |
| independent_original_and_actual_axioms | PASS | Immutable independent proof/full-old lambda; actual built proof/caller standard3. |
| live_LSP | PASS | Fresh complete unfiltered0errors19warnings; exactly two intended removals. |
| callers | PASS | Both actual callers unchanged and module checked; no external direct use. |
| owner_cumulative_full_then_LeanEval | PENDING OWNER | Frozen sequential full `lake build` THEN separate `Roth.LeanEval`; not run/claimed by leaf. |

### Buzz pass — FAST-BOARD

Both accepted profile runs are uncontended: no owner compiler; native searches/live goal
completed before baseline; all ordinary proof/module/verification/final-LSP requests completed
before the final run. Sequential command for each stage:

```text
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/roth-mono-api/before-prefix.lean
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/roth-mono-api/final-prefix.lean
```

Both exit0; command walls46.037s/42.777s, raw UTF8 `before-profile.log`/`final-profile.log`,
exact invocations/exits in corresponding `*-run.json`; anchors and arithmetic in
`profile-summary.json`. Each preserves exact imports/all preceding source/context, ends
immediately after the target, and appends only `end Roth`. PREFIX-ONLY evidence: not a claim
that the known late whole-file default-heartbeat index_le_lem6 profile has been resolved.
Owner's eventual whole-module sweep after downstream cleanup remains mandatory.

| Stage | Outer command | Async proof | Async kernel/addDecl | Async linter | Total |
|---|---:|---:|---:|---:|---:|
| Before | 4.035ms | 13.045ms | 3.351ms | 4.702ms | 25.133ms |
| Final | 3.888ms | 12.590ms | 2.421ms | 4.814ms | 23.713ms |

Raw outer anchors: before log123367 identifies the original Θ_mono docstring/theorem;
final log123898 identifies the scoped omit wrapping that exact theorem. Async proof anchors
name `Roth.Θ_mono` explicitly (before123893/final123909); associated kernel entries
before126048/final126075 typecheck declarations `[Roth.Θ_mono]`; linter entries
before126056/final126083. Only outer and associated top-level async components are summed;
nested tactic/kernel/header nodes are not double counted. There is no separate executable
theorem compiler entry. Totals below750ms remeasurement threshold and1000ms budget, so no
repeat/fix justified. No meaningful speed improvement claimed from this small timing change.
No raises/scaffolding:0 removed,0 added. No slow-target deferral.

### Required11-step checklist

- [✓] Step1: all five full references, both skills, workflow, relevant style/naming/profiling read.
- [✓] Step2: fresh complete24-item substantive audit.
- [✓] Step2.5: five ACTUAL searches with honest index/bounded-search limitations.
- [✓] Step2.6: every effective parameter's compiled probes, public literature/inversion; explicit retained choices honored.
- [✓] Step2.7: complete measured signature packing table.
- [✓] Step2.8: complete inequality table.
- [✓] Step3: all42 rules considered with concrete statuses/fresh applicable tactic attempts.
- [✓] Step4: step-back/simplify review; no unavailable handoff claimed.
- [✓] Step5a: complete unfiltered actual final LSP success; no timeout/partial/dependency failure.
- [✓] Step5b: actual module/independent-original/full-old adapter/actual AST/axioms/callers/diff/profile gates pass. Owner full/LeanEval pending explicitly.
- [✓] Step6a: no rename needed; no queue/shared-report mutation.

Refactoring/follow-up recommendations:none. Historical extra hB/hr widening remains declined;
no new decision requested. Other declarations/warnings are not counted as audited by this leaf.

Source frozen, edit authority revoked: SHA256
`a7fc4b6f10bab79a35f6cf20b34870fdcde77e44a79c7fd151c3e5ba10f0c8bd`.
All started native requests and compiler/terminal sessions completed; no orphan job remains.
Only production write: selected omit line in Roth/Theta.lean. Only report write:
`.mathlib-quality/cleanup/Theta-Theta_mono-approved.md`. No Git mutation.
Owner may run frozen full `lake build`, then separate `lake build Roth.LeanEval`, and publish.


## Owner cumulative publication gates

After leaf freeze/revocation and drained requests, owner ran `lake build` followed by separate
`lake build Roth.LeanEval`: both exited 0, in 68.560 s and 31.179 s.
Theta SHA256 `a7fc4b6f10bab79a35f6cf20b34870fdcde77e44a79c7fd151c3e5ba10f0c8bd` was identical before and after both commands.
Raw logs: `/private/tmp/roth-theta-r13-full.log` and `/private/tmp/roth-theta-r13-leaneval.log`; machine record
`/private/tmp/roth-theta-r13-builds.json`. These completed owner gates supersede the
leaf's earlier pending cumulative entries. Exact-path staging, commit and successful push publish
this approved revisit before the next source edit. This revisits original 13; original counts
remain Theta 15/35, overall 196/264, 9/14 files. No new original or helper is counted.
