# Original 13: `Roth.Θ_mono`

Scope: only `Roth/Theta.lean:121`, plus this report. Fresh dedicated leaf; original12 owner checkpoint `4f15ff1ee078bdc4a63491b77bdb09500d8743d5`. Source checkpoint SHA256 `7f8ddcf44c78dd1b8f505206609b350b66cc70e17aaca919d70c704bcc0584e7`. Read-only preparation preceded explicit owner RELEASE. No Git mutations, shared-log writes, new live helpers, or public API changes.

Applied: destructure the three `RSet` properties in the membership pattern instead of nested projections; lambda `=>` becomes `↦`; pack `hr` onto the first signature line. Body remains three tactic lines (3 → 3, total source line delta 0). Every original binder, universe, binder mode, name, visibility, definition and narrative remains. No routine callers edited. The two actual applications remain in `Θ_lt` at lines 891 and 907.

## Baseline and references

The previous complete unfiltered native diagnostic artifact `/private/tmp/roth-theta-forall-final-lsp.json` has identical source hash: success=true, partial=false, timed_out=false, 0 errors, 33 warnings. It is reused as baseline per dispatch. Target warning: redundant `DecidableEq σ` in the public type. It remains protected by the pending menu A. Header metadata and unrelated warnings are outside scope. Owner reports preceding full build 89.886s, then separate `Roth.LeanEval` 28.529s, both exit0; these are inherited baseline evidence, not this leaf's final build claims.

Read the full leaf instructions; both skills; cleanup workflow; all five required references `golfing-rules`, `proof-patterns`, `mathlib-search`, `generalisation-patterns`, `cleanup-gates`; relevant style/naming sections and profiling reference. Native goal at line124 confirms the actual subset goal and effective section instances. Native `lean_run_code` type/axiom exploration succeeded (`native-types.json`). All local evidence is in `/private/tmp/roth-theta-mono/` unless given another absolute path.

## Complete substantive audit (24)

| # | Item | Finding/action |
|---|---|---|
| 1 | Lint | Existing public unused-DecEq warning preserved pending A; no suppression. |
| 2 | Have scan | No `have` in original or selected live proof. |
| 3 | Set options | None in live declaration; no limit changes. Scratch failed automation uses conservative 10000-heartbeat budgets. |
| 4 | Simp squeeze | No simp in live proof. |
| 5 | Naming | `Θ_mono` describes monotonicity of the named mathematical quantity; no forbidden number pattern/abbreviation or ge/gt suffix. No rename. |
| 6 | Packing | Measured tables below; `hr` packed, first signature line exactly100 codepoints. |
| 7 | By placement | `:= by` at end of conclusion line. |
| 8 | Format | Two-space proof indentation, no blank lines or chained tactics; `↦` fixed. |
| 9 | Comments | Original two-line docstring unchanged; no inline proof comments existed, none removed. |
| 10 | Docstring | Public statement/source description present and protected. |
| 11 | Visibility | Public main result listed in module documentation; public preserved. |
| 12 | Structure | Headline body3 lines, no conjunction in conclusion or >10-line branch. No helper/decomposition needed. |
| 13 | Mathlib | Five actual methods below; generic subset/supremum theorem already used directly. Project-specific coefficient-family inclusion remains substantive local content. |
| 14 | Junk def | n/a: theorem, not data definition. |
| 15 | Exists lemma | n/a: public inequality, no private existential wrapper. |
| 16 | Show/change | None. |
| 17 | Push-neg | None. |
| 18 | Generalise | Every effective binder checked below; stronger actual-definition candidate compiled and remains unapplied. |
| 19 | Inequality | All four occurrences correctly oriented, table below. |
| 20 | Normal form | Order relation on suprema is canonical; use generic csSup machinery directly. |
| 21 | Syntax generality | A global `Monotone (fun B ↦ Θ B q r)` is an equivalent bundled candidate after stronger monotonicity; no new public companion justified or applied. |
| 22 | Import fanout | No new import. |
| 23 | Casts | Diff has no casts/ascriptions: 0 dropped, 0 kept. |
| 24 | Instance name | No instance declaration introduced or changed. |

## Five actual mathlib searches

Raw native search results: `/private/tmp/roth-theta-mono-search.json`.

| Method | Actual query | Result |
|---|---|---|
| A LeanFinder | “The supremum of a subset is at most the supremum of a bounded above set” | `csSup_le_csSup`, primed bottom-order variant, `sSup_le_sSup`, `iSup_le_iSup_of_subset`. |
| B Loogle | `sSup ?s ≤ sSup ?t` | Generic complete/conditionally complete variants, including `csSup_le_csSup`. |
| C LeanSearch | “real supremum monotone under inclusion nonnegative bounded set” | `Real.sSup_def`, `Real.sSup_nonneg`, generic upper-bound monotonicity. |
| D Source search | Full `csSup_le_csSup`, `sSup_le`, `sSup_nonneg` in standard order/real files | Exact generic implementation and real-empty-set conventions verified. Untruncated full-name search found the declarations. |
| E Native local name search | `csSup_le_csSup` | Exact theorem and variants present; index status warming, positive hits valid, no absence inferred. |

Auxiliary variants: primed `csSup_le_csSup'` needs an order bottom (not ℝ); complete-order `sSup_le_sSup` also unsuitable directly for ℝ; `Real.sSup_le` and `Real.sSup_nonneg` support the stronger proposal. Common-equivalents lookup: boundedness corresponds to `BddAbove`; no custom boundedness predicate introduced. No generic theorem packages this project's `RSet` coefficient inclusion automatically. The nonself prefix automation probe uses copied actual definitions before `Θ_mono`, with anonymous examples so `exact?` cannot cite the theorem being audited or a failed named trial. `exact?` fails; `apply?` gives partial suggestions and hits the conservative10000-heartbeat bound. This is bounded unsuccessful search, not a proof of global absence. The initial imported named-trial attempt was corrected because it could cite earlier failed declarations; its suggestions are not used as evidence.

## Generalisation: every effective binder

Negative compiled dependency/drop trials are labelled in `negative.lean`, log `negative.log` (expected exit1). Positive weakening trials are separate in `positive.lean` with standard-axiom checks. A failed drop of the original *proof* is not asserted to prove mathematical necessity.

| Binder | Role/use | Compiled trial and outcome | Live decision |
|---|---|---|---|
| `{σ : Type*}` | Universe-polymorphic polynomial variable type | `clear σ` fails: Fintype depends on σ; already universe polymorphic. Sort-valued abstraction would not preserve MvPolynomial's Type domain. | Preserve. |
| `[Fintype σ]` | Index/Θ finite-sum meaning, uniform cardinal bound | Removing it fails Fintype synthesis in Θ's actual type; `[Finite σ]` alone likewise fails. Explicitly choosing another Fintype would restate instance-dependent data. | Preserve. |
| `[DecidableEq σ]` | Original public helper applications require classical decidability | Strong actual-import candidate and `drop_decEq` compile without it; candidate AST verifies absence. | Menu A pending, preserve. |
| `{B : ℝ}` | Source coefficient bound | `clear B` fails dependent hB; value remains in conclusion/strong candidate. Abstract field would change index codomain and definitions. | Preserve. |
| `{B' : ℝ}` | Target coefficient bound | `clear B'` fails dependent hBB'; value remains in conclusion/strong candidate. | Preserve. |
| `(hB : 1 ≤ B)` | Supplies old nonemptiness helper | Original proof after clearing fails unknown hB; `drop_hB` and weakening `0 ≤ B` compile via stronger proof. No sign assumption is necessary for strong candidate. | Preserve pending new decision. |
| `(hBB' : B ≤ B')` | Transports every coefficient bound | Clearing in old proof fails; no weaker order hypothesis from catalogue applies (already weak). Equality/strict order would strengthen. | Preserve. |
| `(q : σ → ℕ)` | Evaluation denominators in conclusion | `clear q` fails target dependency; no positivity/nonzero assumption to weaken. | Preserve. |
| `{r : σ → ℕ}` | Shared weight/degree parameter | `clear r` fails dependency; persists in strong conclusion. | Preserve implicit. |
| `(hr : ∀ j, 0 < r j)` | Passed to old boundedness helper | Original proof after clearing fails unknown hr; strong `drop_hr` and `∀ j, 0 ≤ r j` candidates compile. Global positivity is unnecessary for the new proof; no point localisation needed. | Preserve pending new decision. |

### Stronger candidate (report only)

Candidate `strong` imports the actual built `Roth.Theta`, so it uses actual `RSet`, `indexSet`, `Θ` and `index` definitions, not a shadow construction. It has exactly seven effective binders: implicit σ, instance Fintype, implicit B/B', explicit hBB', explicit q, implicit r. It removes hB/hr/DecEq, retaining every other mode. It proves arbitrary-r boundedness inline from `index_le_card`, real supremum nonnegativity from `index_nonneg`, and monotonicity using `Real.sSup_le` and `le_csSup`. It does not claim the current live `indexSet_bddAbove` or `Θ_nonneg` APIs have already widened.

Concrete compiled F proof (scratch namespace, actual imported definitions):

```lean
omit [DecidableEq σ] in
theorem strong {B B' : ℝ} (hBB' : B ≤ B') (q : σ → ℕ) {r : σ → ℕ} : Θ B q r ≤ Θ B' q r := by
  have hb : BddAbove (indexSet B' q r) := by
    refine ⟨Fintype.card σ, ?_⟩
    rintro _ ⟨R, ⟨hR0, hRd, -⟩, h, -, rfl⟩
    exact index_le_card ((map_ne_zero_iff _ (map_injective _ Int.cast_injective)).2 hR0)
      (by simpa [degreeOf, degrees_map_of_injective R (f := Int.castRingHom ℝ)
            Int.cast_injective] using hRd) _
  have hn : 0 ≤ Θ B' q r := by
    apply Real.sSup_nonneg
    rintro _ ⟨R, _, h, _, rfl⟩
    exact index_nonneg _ _ _
  refine Real.sSup_le ?_ hn
  rintro _ ⟨R, ⟨hR0, hRd, hRc⟩, h, hh, rfl⟩
  exact le_csSup hb ⟨R, ⟨hR0, hRd, fun d ↦ (hRc d).trans hBB'⟩, h, hh, rfl⟩

```

Explicit full-old-type lambda adapter accepts every original binder in order, ignoring hB/hr/DecEq only inside the adapter. Kernel `rfl` equality with actual `@Roth.Θ_mono` is checked; direct `getConstInfo.type`, universe arity and all `BinderInfo` are independently checked for original proof, styled proof, and adapter. Candidate telescope AST rejects any residual hB/hr/DecEq. Exact full `Θ_lt` caller proof is copied independently, with only its two Θ_mono applications replaced by `strong hMlt.le _`; a scratch-only copy of the original private logarithm helper makes that complete caller accessible. No live companion/helper/caller edit is applied. Acceptance requires parent/root's fresh decision; menus A–E grant no permission for this broader hB/hr change.

### Public literature and inversion

Local primary source `.mathlib-quality/references/clean.tex:650–669` defines the family and states: “Θ_m is nondecreasing in B, since increasing B enlarges the set of allowed polynomials” (mathematical notation rendered here). Search queries: supremum monotonicity/subset/bounded/empty set; “Formalizing Roth” nondecreasing theta; canonical completeness formulation. Primary [UPenn analysis notes](https://www2.math.upenn.edu/~gressman/analysis/01-completeness.html) require nonempty bounded subsets for the usual real supremum. [Mathlib's real supremum API](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Archimedean/Real/Basic.html) uses zero for the empty case, permitting the additional nonnegative-target argument. Other top search hits included ETH lecture notes and MathWorld; no independent Roth-paper widening was found. ChatGPT math MCP unavailable (no callable matching tool). Search does not establish absence in literature.

Inversion check fires: after the supremum step the proof is exactly coefficient-bound inclusion and generic order theory. That abstract supremum implication already exists as `csSup_le_csSup`; adding an abstract helper would duplicate mathlib. The stronger real variant uses established `Real.sSup_le` and nonnegative target. Broad coefficient-ring/real-codomain replacement is outside this declaration's definitions and not proposed as a mechanically verified theorem.

## Measured signature packing and inequality orientation

`#check @Roth.Θ_mono` at `format.width 100` is recorded in `native-types.json`; selected proof remains the exact old type.

| Stage/line | Codepoints | Next complete token/block | Arithmetic | Action |
|---|---:|---|---|---|
| Before121 | 78 | `(hr : ∀ j, 0 < r j)` =19 | 78+1+19=98≤100 | Repack applied. |
| Before122 | 50 | none | n/a | Final signature line. |
| Final121 | 100 | conclusion through `:= by` =24 | 100+1+24=125>100 | Correct break. |
| Final122 | 28 | none | n/a | Correct final line. |

| Occurrence | Location | Form | Result |
|---|---|---|---|
| 1 | hB | `1 ≤ B` | Already oriented. |
| 2 | hBB' | `B ≤ B'` | Already oriented. |
| 3 | hr | `0 < r j` | Already oriented. |
| 4 | conclusion | `Θ B q r ≤ Θ B' q r` | Already oriented. |

No `≥`/`>` in signature or hypotheses; no ge/gt rename.

## All 42 golfing rules

| Rule | Status/reason |
|---|---|
| 1.1 by-exact | n/a: no wrapper. |
| 1.2 by-rfl | n/a: no such proof. |
| 1.3 rw/exact | n/a: no rw. |
| 1.4 simp/exact | n/a: no simp. |
| 1.5 trailing rfl | n/a: no trailing tactic rfl. |
| 1.6 constructors | Already uses anonymous constructors. |
| 1.7 apply/exact | n/a: direct refine/constructor. |
| 1.8 contradiction | n/a: no contradiction. |
| 1.9 eta | Coefficient lambda changes value by transitivity, cannot eta-reduce; ↦ style fixed. |
| 1.10 have inline | n/a: no have. |
| 1.11 refine/fun | Existing refine then dependent witness elimination is direct; no apply/intro chain. |
| 1.12 show | n/a: absent. |
| 1.13 projections | Applied: unpack hR into hR0/hRd/hRc in existing pattern. |
| 1.14 rw merge | n/a: absent. |
| 1.15 terminal simp | n/a: absent. |
| 1.16 nonterminal simp | n/a: absent. |
| 1.17 dot notation | Already `.trans hBB'`. |
| 1.18 parens | No gratuitous outer argument parentheses. |
| 1.19 push-neg | n/a: absent. |
| 1.20 existential wrapper | n/a: public inequality, no such helper. |
| 2.1 grind | Actual nonself isolated attempt failed. |
| 2.2 before grind | n/a: no grind retained. |
| 2.3 simpa | Actual `simp [Θ]` leaves supremum inequality; no simp consolidation opportunity. |
| 2.4 fun-prop | n/a: no continuity/differentiability/measurability goal. |
| 2.5 positivity | n/a: goal is comparison of two suprema, not positivity. |
| 2.6 gcongr | Actual attempt made no progress. |
| 2.7 lia/omega | n/a: no Nat/Int arithmetic goal in target proof. |
| 2.8 aesop | Actual attempt failed without progress. |
| 2.9 norm-num/cast | n/a: no concrete arithmetic/cast subgoal. |
| 2.10 decide | n/a: abstract real-supremum inequality is not finite computation. |
| 2.11 field/ring | n/a: no algebraic identity. |
| 2.12 linear-combination | n/a: no ring ending or polynomial relation. |
| 2.13 wlog | n/a: no symmetric branches. |
| 2.14 calc | n/a: no calc. |
| 2.15 multiple goals | n/a: one subset obligation closed by one witness term. |
| 3.1 erw | n/a: absent. |
| 3.2 legacy analysis | n/a: absent. |
| 3.3 omega | n/a: absent. |
| 3.4 rfl patterns | Existing rfl substitutes index value directly; preserved. |
| 3.5 attributes | No globally justified automation attribute for this domain-specific theorem; none added. |
| 3.6 simp-all | n/a: no simplification context. |
| 3.7 limits | None in live source; none added. |

Step-back reflection: the generic supremum lemma is already optimal for the protected signature. Named coefficient bounds avoid opaque nested projections without adding lines/helpers. Automation cannot discover the required polynomial witness in the bounded nonself trials. A term lambda could replace rintro but would lengthen the dependent witness pattern. The stronger proof needs two auxiliary semantic facts, so it is a separately reviewable API proposal, not silent golf.

## Verification, simplify, buzz and freeze

`/Users/ramin/.elan/bin/lake build Roth.Theta` exit0, 62.294s,2423 jobs (`module-build.log`, `module-build.json`). After that build, `lake env lean actual-built.lean` exit0: independent original and selected proofs have actual final constant's exact type/universe/BinderInfo, adapter preserves every binder, all four proofs plus actual built `Roth.Θ_mono` use only `[propext, Classical.choice, Quot.sound]` (`actual-built.log`). No proof invokes Θ_mono to discharge its own original statement. The kernel adapter-equality check separately refers to the actual constant, as intended.

Fresh complete UNFILTERED native `lean_diagnostic_messages(file_path=/Users/ramin/LEAN/Roth/Roth/Theta.lean, timeout_s=60)` succeeded: partial=false,timed_out=false,failed_dependencies=[],0errors33warnings. Raw `final-lsp.json`; machine `diagnostic-check.json` confirms exact warning multiset equality with baseline (only output order changes). Protected DecEq warning remains; no new or suppressed warning.

`diff-check.json` asserts precisely the intended target-only patch: all bytes outside target unchanged, no comments removed, no new library identifiers, source line delta0. `target.diff` is the exact leaf diff. All referenced library identifiers were pre-existing and search/compiler verified; there is no newly introduced name to hallucination-check.

Simplify pass: PASS-THROUGH after holistic review in this leaf. No callable built-in `/simplify` tool/skill is exposed, so no unavailable handoff is claimed. The direct generic supremum theorem and named witness properties suffice; another helper would duplicate mathlib or add a fresh audit obligation. No new issue or follow-up beyond the separately compiled F proposal.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Actual module command exit0 above. |
| definition_protected | pass | No definition change, exact diff assertion. |
| theorem_statement_protected | pass | Packing only; direct actual type/universe/BinderInfo equality compiled after build. |
| structure_gate | pass | Headline body3 lines, no >10-line branch or conjunction conclusion. |
| naming_gate | pass | No forbidden name pattern; no rename required. |
| line_packing_gate | pass | Every signature line measured, final widths100/28. |
| inequality_orientation_gate | pass | Four oriented occurrences, zero ≥/>. |
| independent_original_and_axioms | pass | Original proof nonself; actual built constant, selected proof, strong candidate and adapter use only standard3. |
| live_LSP | pass | Fresh complete unfiltered native0errors33warnings. |
| callers | pass | Actual two Θ_lt callers unchanged and module-checked; separate full copied caller proof with F substitutions exit0 and exact actual caller type. |
| owner_cumulative_full_and_LeanEval | pending owner | Frozen whole-project build THEN separate Roth.LeanEval required; not run/claimed by leaf. |

Per-leaf gates pass; owner cumulative gates remain explicit. Corrected exploratory failures are not certification: imported named automation trials could cite failed declarations and were replaced with anonymous nonself-prefix examples; the scratch reserved variable `at` was renamed `actualType`, and inaccessible private logarithm helper was copied into scratch. Definitive `positive.log` and `actual-built.log` both come from final exit0 runs.

### Buzz pass — FAST-BOARD

All ordinary compiler/native/LSP requests drained before two sequential profiled compiles. Commands were `/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/roth-theta-mono/before-prefix.lean`, then the identical flags on `final-prefix.lean`. Both exit0; total command walls50.097s/48.775s. Raw UTF8 logs `before-profile.log`/`final-profile.log`, exact invocation/result JSONs `before-profile-run.json`/`final-profile-run.json`, measured component/anchor table `profile-summary.json`.

| Stage | Outer command | Async proof | Async kernel/addDecl | Async linter | Total |
|---|---:|---:|---:|---:|---:|
| Before | 3.548ms | 12.990ms | 2.330ms | 4.615ms | 23.483ms |
| Final | 3.628ms | 12.425ms | 2.972ms | 4.581ms | 23.606ms |

Raw anchors explicitly identify original source docstring/theorem Θ_mono, its proof and associated kernel declaration. Only top-level outer/async nodes are summed; nested tactic/kernel nodes are not double-counted. Both totals are far below750ms remeasurement threshold and1000ms budget. No performance improvement claimed; no additional run justified. No executable theorem-compilation entry exists beyond these associated nodes. Limit raises removed0/added0, no scaffolding in live source, no deferred slow target.

These are PREFIX-ONLY profiles: each preserves exact imports/all preceding source/context, ends immediately after target, and appends only `end Roth`. The known late whole-file `index_le_lem6` default-heartbeat issue is not bypassed with raised limits. Prefix success is not an allfile performance claim. Owner must run its eventual whole-module profiling sweep after downstream cleanup.

### Required 11-step worker checklist

- [✓] Step1: all required references read.
- [✓] Step2: full24-item audit supplied.
- [✓] Step2.5: five actual searches and bounded failure status supplied.
- [✓] Step2.6: every effective binder's classification/compiled trials, public literature and inversion supplied.
- [✓] Step2.7: measured complete packing table supplied.
- [✓] Step2.8: complete inequality scan supplied.
- [✓] Step3: all42 golfing rules supplied.
- [✓] Step4: holistic reflection/simplify review supplied.
- [✓] Step5a: fresh complete native final diagnostics succeeded.
- [✓] Step5b: exact diff, module, type, axioms, caller and performance gates supplied; owner cumulative builds pending as stated.
- [✓] Step6a: no rename required, no shared queue write permitted or performed.

Refactoring needed for owner/root decision: F, remove hB/hr/DecEq from Θ_mono using compiled `strong` while adapting exactly its two Θ_lt calls. This overlaps A's DecEq removal and goes further than A; it is not authorised by A–E and remains entirely unapplied. No speculative companion/new live helper requested. Existing A–E all remain unapplied.

Source frozen: SHA256 `8d6d5dda0246f2b78ed60a6a06017c5ad8de774aec4693dfb710ef8a94288045`. Source edit authority revoked on handoff. Every started compiler/process/native request completed; no orphan request or profiling job remains. No Git mutation. Report `.mathlib-quality/cleanup/Theta-Theta_mono.md`. Owner may now run its sequential frozen full build and separate LeanEval gate, then publish the checkpoint.


## Owner cumulative publication gates

After leaf freeze/revocation and all leaf requests drained, owner ran sequential `lake build`
then separate `lake build Roth.LeanEval`: both exit0, 58.864s and21.222s. Source SHA256 remained
`8d6d5dda0246f2b78ed60a6a06017c5ad8de774aec4693dfb710ef8a94288045` before/after BOTH commands.
Raw `/private/tmp/roth-theta-d13-full.log` and `/private/tmp/roth-theta-d13-leaneval.log`;
machine `/private/tmp/roth-theta-d13-builds.json`. The leaf's earlier owner-pending entries
are superseded by these completed owner gates. Exact-path staging, commit and successful push
publish this original13 checkpoint before the next original source edit. No public amendment
is applied; menus A–F remain pending. Published counts: Theta13/35, overall194/264,9/14files.
