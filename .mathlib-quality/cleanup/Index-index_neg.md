# `Roth.index_neg` cleanup

Scope: original snapshot e557886, declaration 205–207; worker baseline 42712af,
current declaration 194–196. Applied only the approved `omit [DecidableEq σ] in`
before the byte-preserved docstring. Proof/signature text and all definitions preserved.
Public type deliberately loses that instance; it is not claimed type-identical.
Declaration remains 3 lines, proof 1 line; file 263→264 lines. No renames queued or applied.

## Audit (24 items)

| # | Item | Concrete result |
|---|---|---|
| 1 | Lint | Two target unused-instance warnings resolved; final full native diagnostics below. |
| 2 | Have scan | Zero `have` bindings. |
| 3 | Options | No per-declaration options or limit overrides. |
| 4 | Simp | Single terminal `simp [index, support_neg]`; retain unsqueezed. |
| 5 | Naming | `index_neg` describes index under negation; snake_case, no forbidden abbreviations/numeric patterns, no rename. |
| 6 | Packing | Every signature line measured below; width100 built check recorded. |
| 7 | By | `by` ends the conclusion line. |
| 8 | Format | Four-space signature continuation, two-space tactic, one tactic, no interior blank lines/instance plumbing. |
| 9 | Comments | No proof comments; the entire existing docstring is byte-identical. |
| 10 | Docstring | Existing §5 sign-invariance source citation preserved by explicit scope instruction. |
| 11 | Visibility | Public API used in `Roth/Theta.lean:398`; retain public. |
| 12 | Structure | One tactic; no conjunction or branches; no extraction needed. |
| 13 | Mathlib | Five actual methods below; support fact already supplied by mathlib. |
| 14 | Junk def | n/a: theorem, no definition introduced. |
| 15 | Exists lemma | n/a: no existential conclusion or private wrapper. |
| 16 | Show/change | No `show` or `change`. |
| 17 | Push neg | No `push_neg`. |
| 18 | Generalise | Every binder/drop probe and public literature recorded below. |
| 19 | Inequality | Equality only; explicit scan table below. |
| 20 | Normal form | Removing negation on RHS is the canonical invariance equation. |
| 21 | Syntax generality | Direct equation rewrites the determinant sign use; no easier restatement needed. |
| 22 | Import fanout | n/a: no new imports. |
| 23 | Casts | 0 dropped/0 cross-type/0 load-bearing casts in diff. |
| 24 | Instance names | n/a: theorem, no instance declaration introduced. |

## Five-method search

Evidence prefix throughout: `/private/tmp/roth-index-neg-`.

| Method | Actual query | Result/artifact |
|---|---|---|
| A LeanFinder | support of negative multivariate polynomial equals original support | `finder.json`: bounded call, DNS failure; unavailable, not absence. |
| B Loogle | `MvPolynomial.support (-_)` | `loogle.json`: bounded call, DNS failure. |
| C LeanSearch | support of negation of multivariate polynomial | `search.json`: bounded call, DNS failure. |
| D Source | `support_neg`, `support_smul_eq`, full `index_neg` | Mathlib `Algebra/MvPolynomial/CommRing.lean:75` and `Basic.lean:700`; untruncated exact-name search `fullname-search.log` empty. |
| E Names | `support_neg` via actual local search | `local.json` returns `MvPolynomial.support_neg`; index unavailable but positive source hit verified by built `#check`. |

Auxiliary routes: `map_neg`, `support_neg`, `support_smul_eq`; no common-equivalents
bucket applies. Partial match: use mathlib support-negation API after unfolding this
project's index. No verified exact mathlib theorem for the project-specific index;
remote unavailability precludes an exhaustive absence claim. No new wrapper/helper.
`exact?`/`apply?` fallback results are recorded with alternative checks below.

## Generalisation

All drop files use `set_option autoImplicit false`. Original independent proof uses
literal original index definition in a fresh namespace, with `Roth.weight` qualified.
No import of `Roth.Index`, target theorem, support helper or same-file theorem.

| Binder | Class/use | Actual candidate and result |
|---|---|---|
| `{σ : Type*}` | Universe/type variable in polynomial and function domains | Drop tested (`drop-σ`); unknown `σ`, correctly no auto-insertion. Already universe-polymorphic; lowering to `Type` would specialize. |
| `[Fintype σ]` | Structure/data needed by unchanged `weight`/index definition | Drop and parent `[Finite σ]` tested (`drop_fintype`, `finite`): cannot synthesize `Fintype σ` at literal definition. Retain; Finite alone supplies no computational enumeration to unchanged API. |
| `[DecidableEq σ]` | Decidability; unused | Drop tested (`drop_sigma`) successfully; approved omit applied and actual built signature confirms removal. |
| `(P : MvPolynomial σ ℝ)` | Polynomial value on both sides | Drop tested (`drop-P`): unknown identifier `P`; retain. No parent/point-local/strict weakening for a value binder. |
| `(α : σ → ℝ)` | Translation point on both sides | Drop tested (`drop-α`): unknown identifier `α`; retain. No continuity/global hypothesis to localize. |
| `(r : σ → ℕ)` | Weight data on both sides | Drop tested (`drop-r`): unknown identifier `r`; retain. No positivity or strict hypothesis to weaken. |

No proposition hypotheses; strict→weak and point-localization have no applicable target.
No abstract-object inversion gain: after unfolding, exactly the generic `map_neg` and
support-negation facts already explain the result; no new abstract helper warranted.
Changing the coefficient type requires changing `index`, outside this target's scope.
No additional public API proposal applied.

## Literature

Actual web query: `polynomial index Roth theorem invariant multiplication nonzero scalar generalization`.
First three displayed leads, in order (one query, no repeated rankings):

| Rank | Displayed lead | Assessment |
|---|---|---|
| 1 | [Min Ru, Roth’s Theorem](https://www.math.uh.edu/~minru/fields/roth.pdf) | Opened author-hosted notes, p.3: weighted minimum of nonzero derivatives; relevant primary exposition. |
| 2 | [Medvedev–Scanlon, Invariant varieties for polynomial dynamical systems](https://annals.math.princeton.edu/wp-content/uploads/annals-v179-n1-p02-p.pdf) | Polynomial-scaling search noise; no conclusion drawn. |
| 3 | [Milojević, An elementary approach to Roth’s theorem](https://aleksa-milojevic.github.io/expository/roth.pdf) | Opened author-hosted exposition; Claim 3.1 and Taylor support viewpoint support the interpretation. |

Inference from the support definition: changing every coefficient's sign preserves
nonvanishing and hence the same minimum; no positivity/nonzero-P hypothesis is needed
for this identity, including this project's zero convention. Local primary manuscript
`clean.tex:825` explicitly states sign invariance; `:638` states nonzero-scalar invariance
already represented by neighboring `index_C_mul`. No literature-driven new API change.
Math ChatGPT MCP unavailable (no matching tool in inventory), honestly not queried.

## Packing and inequalities

Actual built `set_option format.width 100; #check @Roth.index_neg` (`recovery.log`):

```lean
@index_neg : ∀ {σ : Type u_2} [inst : Fintype σ] (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ),
  index (-P) α r = index P α r
```

| Signature line | Codepoints | Next complete syntactic item | Arithmetic/action |
|---|---:|---|---|
| 194 | 66 | conclusion `index (-P) α r = index P α r := by` (34) | 66 + 1 + 34 = 101 > 100; break justified, ok |
| 195 | 38 | no next signature line | n/a; proof next, ok |

| Occurrence | Location | Original | Rewrite/rename |
|---|---|---|---|
| 0 | All signature/hypotheses | No `≥`/`>`; equality only | n/a; no `_ge_`/`_gt_` name |

## All 42 golf rules

| Rule | Result |
|---|---|
| 1.1 | n/a: no `by exact` wrapper. |
| 1.2 | n/a: no `by rfl`. |
| 1.3 | n/a: no rw/exact sequence. |
| 1.4 | n/a: no simp/exact sequence. |
| 1.5 | n/a: no trailing rfl. |
| 1.6 | n/a: no constructor. |
| 1.7 | n/a: no apply/exact sequence. |
| 1.8 | n/a: no contradiction argument. |
| 1.9 | n/a: no lambda. |
| 1.10 | n/a: no have. |
| 1.11 | n/a: no apply/intro. |
| 1.12 | n/a: no show. |
| 1.13 | n/a: no projected have. |
| 1.14 | n/a: no consecutive rewrites. |
| 1.15 | n/a: terminal simp already unsqueezed. |
| 1.16 | n/a: no nonterminal simp. |
| 1.17 | n/a: no functional lemma application to convert to dots. |
| 1.18 | n/a: no trailing application parentheses. |
| 1.19 | n/a: no push_neg. |
| 1.20 | n/a: no existential helper. |
| 2.1 | Actual grind fallback tested; see alternatives evidence. |
| 2.2 | n/a: no preceding grind tactics. |
| 2.3 | n/a: one terminal simp, nothing to consolidate. |
| 2.4 | n/a: equality, no function property. |
| 2.5 | n/a: no positivity goal. |
| 2.6 | n/a: no inequality/monotonicity goal. |
| 2.7 | n/a: not Nat/Int linear arithmetic. |
| 2.8 | Actual aesop fallback tested; see alternatives evidence. |
| 2.9 | n/a: no numeric/cast goal. |
| 2.10 | n/a: symbolic real sInf equality, not finite computation. |
| 2.11 | n/a: no field-expression identity. |
| 2.12 | n/a: no ring-ending proof/hypotheses. |
| 2.13 | n/a: no symmetric branches. |
| 2.14 | n/a: no calc. |
| 2.15 | n/a: single goal and terminal tactic. |
| 3.1 | n/a: no erw. |
| 3.2 | n/a: no legacy function-property tactic. |
| 3.3 | n/a: no omega. |
| 3.4 | n/a: no rcases. |
| 3.5 | No attribute change: this task preserves the existing public API. |
| 3.6 | n/a: no simp_all only. |
| 3.7 | n/a: no heartbeat override. |

Step back: the proof already is one tactic using the relevant mathlib invariant.
`simp [index]` compiles in the independent replica; keeping the explicit support hint
preserves the requested proof and makes the reason visible. No marginal churn justified.

## Verification and honest failures

| Check | Actual invocation/evidence | Result |
|---|---|---|
| Module | `/Users/ramin/.elan/bin/lake build Roth.Index` → `build.log` | exit 0; Index 7.5 s; existing warnings, none on target. |
| Full native diagnostics | MCP helper `lean_diagnostic_messages {file_path: Roth/Index.lean, timeout_s:50}` → `after-lsp.json` | Complete unfiltered response: success=true, partial=false, timed_out=false, failed_dependencies=[]; 0 errors, 12 warnings, 0 target warnings. |
| Independent original theorem | `lake env lean /private/tmp/roth-index-neg-independent.lean` → `independent.log` | exit 0; fresh proof `unfold index; congr 1; rw [map_neg, support_neg]`, original explicit DecidableEq retained here. |
| Original type recovery | `lake env lean /private/tmp/roth-index-neg-recovery.lean` → `recovery.log` | exit 0; snapshot's literal original signature instantiated by actual built target; owner additionally owns whole-original Expr recovery gate. |
| Actual axioms | `#print axioms Roth.index_neg` in recovery; independent print in independent file | Both exactly `[propext, Classical.choice, Quot.sound]`; no sorry/custom axiom. |
| Actual public signature | Built `#check @Roth.index_neg` at `format.width 100` | Fintype retained; DecidableEq absent, as approved. |
| Every-binder probes | `roth-index-neg-run-probes.py` → `probes.json`, all subprocesses completed | DecidableEq drop exit0; data drops/Fintype-parent fail as classified, no changes adopted from failing probes. |
| Alternate minimal simp | `lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/roth-index-neg-alt.lean` → `alt.log` | exit0, command6.516ms/proof79.910ms in isolated replica; different context, not a target performance comparison. |
| Other tactics | `roth-index-neg-alternatives.py` → `alternatives.json` | `grind [index, support_neg]` exit0; aesop exit1/no progress; exact?/apply? exit1 at default200000-heartbeat isDefEq timeout. No limits raised. |
| Diff/comment check | Python unified diff versus `before.lean` and block-comment extraction | Exactly one omission line added; all block comments identical; 0/0 proof comments; no new declarations/lemma references. |

Failed tools are not counted as successes: first live multi-attempt accidentally targeted
blank line197 and returned parser errors; corrected line196 call hit its bounded65s
timeout. Both are retained (`attempts.json`, `attempts-correct.json`); fresh CLI
alternatives above supply usable evidence. Native profile extraction failed on scoped
omit/same-file context (`native-profile.json`); actual full-file CLI trace supplies timing.
MCP helper shutdown printed subprocess-loop cleanup warnings after returning successful
complete diagnostics; all requests/processes completed before release. Failed drop
scratch elaborations sometimes emit secondary automatic sorry-recovery warnings; they
are rejected candidates, never proofs or changes in project source.

Complete native warning inventory (unfiltered original JSON retained, not just this summary):

| Line | Warning |
|---|---|
| 1 | Existing header copyright too short; user-preserved metadata. |
| 199 | `index_C_mul` unused section DecidableEq σ. |
| 227 | `index_le_card` unused section DecidableEq σ. |
| 216 | `index_rename` unused section DecidableEq σ. |
| 204 | `index_mul_left_weights` unused section DecidableEq σ. |
| 198 | `index_C_mul` unused decidability in type. |
| 213 | `index_rename` unused decidability σ and τ in type. |
| 227:72 | `index_le_card.hr` unused. |
| 224 | `index_le_card` unused decidability in type. |
| 203 | `index_mul_left_weights` unused decidability in type. |
| 237 | `index_unique` unused section DecidableEq σ. |
| 234 | `index_unique` unused decidability in type. |

## Scoped simplify and buzz

Simplify: PASS-THROUGH. Reviewed sole diff for reuse, quality and efficiency: omission
removes unnecessary typeclass dependency; proof is already one explicit support rewrite
via terminal simp, no duplication/helper extraction. Built-in simplify invocation is
not available; this is the scoped direct review, not a claim of a separate tool run.
Independent whole-file simplify remains the owner's final gate.

Actual buzz command:
`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Index.lean`
→ `/private/tmp/roth-index-neg-profile-trace.log`, exit0, followed only after completion
by `python3 /private/tmp/roth-index-profile-parse.py neg`, exit0.
Parser asserted all19 current source declarations anchored; table in `profile-table.json`.

| Target | Command | Proof | Total | Dominant tactic | Budget |
|---|---:|---:|---:|---|---|
| index_neg:194 | 10.89ms | 236.14ms | 250.05ms | simp233.504ms | 1000ms, safely below750ms resweep trigger |

Outcome FAST-BOARD for the scoped target. No speed change claimed; no before benchmark
required for the approved instance-only edit. Native extraction failure disclosed above.
No limit raises, scaffolding, new instances or performance fix; deferrals none.
File-final independent profile/simplify and full project/caller gates belong to owner.

## Diff gates

| Gate | Result/evidence |
|---|---|
| lake_build_file | ✓ actual `lake build Roth.Index` exit0, `build.log`. |
| definition_protected | ✓ no def/abbrev changes. |
| theorem_statement_protected | ✓ only explicitly approved scoped instance omission changes public type; original-type recovery passes. |
| structure_gate | ✓ one proof line, no conjunction/branch. |
| naming_gate | ✓ descriptive snake_case, no forbidden pattern; no rename necessary. |
| line_packing_gate | ✓ both signature rows measured, 66+1+34=101 justifies break. |
| inequality_orientation_gate | ✓ zero reversed inequalities; scan table present. |
| new-identifier verification | ✓ no new identifiers referenced; added `DecidableEq σ` already existing section binder; map_neg/support_neg in independent scratch verified by compiled check. |
| comments preserved | ✓ all block comments identical; proof had none. |
| no-limit/no-scaffolding | ✓ sole source addition is omit; no profiler/options/sorry/axiom added. |

Overall scoped worker gates pass. No full-project or external-caller result asserted:
owner runs full build, separate LeanEval, independent original-file/type/Expr/axiom gates,
Theta caller diagnostics, and commits/pushes. Unrelated rename queue remains untouched.

## Eleven required steps

- [✓] Step1: Lean4/mathlib-quality skills; full cleanup workflow and relevant cleanup-all contract; golfing-rules, proof-patterns, search, generalisation, gates, style/naming, review stages, profiling/buzz references read.
- [✓] Step2: all24 audit rows concrete above.
- [✓] Step2.5: five actual searches, positive local verification and remote failures disclosed.
- [✓] Step2.6: every binder classified/probed; public literature/top3 leads recorded.
- [✓] Step2.7: every signature line codepoint arithmetic and actual built width100 check.
- [✓] Step2.8: explicit inequality scan table.
- [✓] Step3: all42 golf rules reported.
- [✓] Step4: one-tactic/reflection/alternative evidence; retain clear existing proof.
- [✓] Step5a: complete unfiltered final native diagnostics, zero target warnings/errors.
- [✓] Step5b: actual module/type/axiom/independent proof/profile and diff gates above.
- [✓] Step6a: naming gate passes; no rename added/applied, existing queue untouched.

Source authority released and owner acknowledged revocation after all Lean/compiler
processes completed. Frozen Index SHA256:
`4117b5c634957e30e7df55bdc5a43b0c98d1b5a12dec1343fdc662155f7975b1`.
After release: report writing only. Refactoring/decomposition flags: none.


## Owner checkpoint d16

Frozen SHA256 `4117b5c634957e30e7df55bdc5a43b0c98d1b5a12dec1343fdc662155f7975b1`. Fresh whole ORIGINAL nonself reproof, all18 original public
type/value recoveries and all19 actual retained standard-axiom checks: compiler
session49904 exit0, `/private/tmp/roth-index-d16-compatibility.log`.
Approved no-DecEq types are additionally checked by Expr.find?; actual signatures printed.
Sequential owner full then separate LeanEval13150 both exit0(101.62s/26.94s),
Index+Theta hashes stable; `/private/tmp/roth-index-d16-{full,leaneval}.log`.
Worker COMPLETE unfiltered Index LSP success=true partial=false timed_out=false, no faileddependencies, 0target diagnostics/12other warnings; /private/tmp/roth-index-neg-after-lsp.json. External Theta COMPLETE native LSP0errors/24warnings after bounded partial+complete retry:23previous plus newly exposed unused-section instance in sum_max_sub_le_index_det at371; original section instance retained, no warning suppression or Theta edit. Caller398 accepted; raw /private/tmp/roth-index-d16-theta-lsp.json.
All original block docs byte-identical, source widths≤100, diff checked before staging.
Exact-path publication precedes the next edit.
