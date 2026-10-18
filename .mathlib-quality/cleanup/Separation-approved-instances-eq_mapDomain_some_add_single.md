# Approved instance revisit: `Roth.eq_mapDomain_some_add_single`

Fresh dedicated worker r01, starting HEAD c5877f4. Own only this theorem and this report; no Git mutations or subdelegation. Explicit user approval (dispatch and `Separation-instance-proposal.md`) covers removing BOTH `[Fintype τ]` and `[DecidableEq τ]`, with scoped omission before the preserved docstring. No other public change is authorized. Original snapshot `/private/tmp/roth-separation-original.lean`.

Read both skills and installed cleanup Phase 4, full golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, cleanup-gates.md, profiling.md, and relevant style/naming sections. Initial audit below was written BEFORE any source edit. Fresh native baseline `/private/tmp/roth-separation-r01-baseline.json`: success=true, partial=false, timed_out=false, 0 errors,31 warnings,0 sorry. Parent owns cumulative full/separate LeanEval builds and compatibility. Actual baseline target114.550ms (command22.471+async92.079) in `/private/tmp/roth-separation-d21-owner-profile.log{,.json}`.

## Initial audit: all 24 items (before source edit)

| # | Item | Concrete finding / planned action |
|---|---|---|
| 1 | LINT | Three target warnings: unused section instances, unused DecidableEq in type, unused Fintype in type. Apply precisely approved omissions; no suppression. |
| 2 | HAVE SCAN | No have blocks exist. |
| 3 | SET_OPTION | No per-theorem option or limit exists. |
| 4 | SIMP SQUEEZE | Shared simp is terminal for both Option cases, already unsqueezed; preserve. |
| 5 | NAMING | Describes equality splitting mapDomain some and single none, embedding actual API camelCase; no forbidden abbreviation, numeric scheme, ge/gt or single-letter name; no rename. |
| 6 | LINE PACKING | Two signature lines measured in table below; conclusion unit cannot fit on first. |
| 7 | BY PLACEMENT | by already ends conclusion line. |
| 8 | FORMAT | Two-space tactics; wrapped simp list; no empty proof line, trailing spaces, haveI or letI. |
| 9 | COMMENTS | No inline proof narrative exists; preserve original docstring exactly. |
| 10 | DOCSTRING | Concise multi-index restriction interpretation, already present and preserved. |
| 11 | VISIBILITY | Public reusable decomposition; preserve approved public API visibility and name. |
| 12 | STRUCTURE | Three proof lines, two short Option branches, no conjunction. No extraction/helper needed. |
| 13 | MATHLIB | Fresh five searches find partial Option reconstruction API; pointwise additive decomposition uses mapDomain lemmas. No exact replacement identified; do not assert absence. |
| 14 | JUNK DEF | n/a: theorem, not a definition. |
| 15 | EXISTS LEMMA | n/a: equality, not existential. |
| 16 | SHOW/CHANGE | Neither exists. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | Remove precisely approved two instances. Audit every effective binder below; arbitrary coefficient is a separate unapproved restatement. |
| 19 | INEQUALITY | No inequalities in whole signature/hypotheses; table below. |
| 20 | NORMAL-FORM | Splitting Finsupp into mapped restriction and distinguished singleton is useful additive form; optionEquiv offers related update form. |
| 21 | SYNTAX-GEN | Additive expression lets caller rewrite coefficient indices directly; retain expression, order, explicit d. |
| 22 | IMPORT-FANOUT | n/a: no imports needed. |
| 23 | CASTS | No explicit coercion/type ascription in planned diff; 0 dropped/0 cross-type/0 load-bearing. |
| 24 | INSTANCE-NAME | n/a: theorem, not instance declaration. |

Issues to fix: remove both approved unused instances; add local classical only if required. No new helper, rename, docstring change, definition change or unrelated source edit.

## Signature width and inequality tables

| Line (initial) | Codepoints | Next syntactic unit | Arithmetic | Action |
|---|---:|---|---|---|
| 50 | 58 | complete equality conclusion and := by (72) | 58+1+72=131>100 | ok |
| 51 | 76 | proof begins | n/a | ok |

Equality is one conclusion unit; do not split its head across lines merely to fill space. Scoped omission is a separate command, not a theorem binder line. Final measurements and width-100 #check follow in verification.

| Scope | ≥ / > occurrences | Rewrite | Rename |
|---|---|---|---|
| Complete theorem signature and all hypotheses | none | none | none |

## Fresh search and literature evidence

All native raw results `/private/tmp/roth-separation-r01-{finder,loogle,search,names,goal,baseline}.json`.

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | finitely supported function on Option split restriction some plus single none | optionEquiv, optionElim_some, optionElim, some; partial representations. |
| B Loogle | Finsupp.some, Finsupp.single | some_single_some, some_single_none. |
| C LeanSearch | finsupp option decomposition some mapDomain plus single none | sum_option_index, finsum_option, Fintype.sum_option, sum_option_index_smul. |
| D source | full target name, mapDomain.*some.*single, optionElim_some, optionElim_add, embDomain_some_none, embDomain_eq_mapDomain, some_embDomain_some | Partial reconstruction/embedding API. Raw full untruncated search `/private/tmp/roth-separation-r01-source-search.log`. |
| E name pattern | Finsupp.optionElim | Eleven source hits; index unavailable, hence no absence conclusion from empty index. |

Auxiliary variants checked: optionElim_some, optionElim_add, some_embDomain_some, embDomain_some_none, embDomain_some_some, embDomain_eq_mapDomain, some_single_some, some_single_none. Common-equivalents table: no topology/bornology/discrete/finiteness-of-intersection bucket. Conclusion: partial reconstruction match; preserve current pointwise library-based proof, within exact approved scope. No new wrapper. No claim of exhaustive absence.

Actual WebSearch query: `finitely supported functions Option decomposition direct sum arbitrary index additive monoid`. Top three hits: [IsarMathLib finite support](https://isarmathlib.org/FinSupp_ZF.html), [FLT mirror of mathlib direct-sum/Finsupp](https://imperialcollegelondon.github.io/FLT/docs/Mathlib/Algebra/DirectSum/Finsupp.html), [official mathlib direct-sum/Finsupp](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/DirectSum/Finsupp.html). These support the inference that finite support imposes no finiteness condition on the ambient index; local primary `Mathlib/Data/Finsupp/Option.lean` explicitly constructs optionEquiv for arbitrary α with Zero M. ChatGPT mathematical MCP unavailable in ALL_TOOLS; no external mathematical consultation tool exists. Literature-driven arbitrary AddCommMonoid coefficients remain a possible distinct public restatement, outside approved scope.

## Effective binder/generalisation audit

| Binder | Classification and use | Catalogue candidates / fresh evidence | Decision |
|---|---|---|---|
| `{τ : Type*}` | Universe-polymorphic domain type | Already Type*, no universe restriction; independent arbitrary Type u proof below. Removing τ leaves Option τ ill-scoped; syntactic dependency, not claimed failed compiler test. Sort is incompatible with Finsupp's Type domain. | Retain |
| `[Fintype τ]` | Automatically included, not mathematically used | Drop entirely is weaker than Finite replacement. Fresh no-instance native run_code succeeds without classical. No finiteness proof use. | Approved omission applied |
| `[DecidableEq τ]` | Automatically included, not in proposition | Drop entirely; fresh no-instance native run_code succeeds without classical, so even local classical is unnecessary. | Approved omission applied |
| `(d : Option τ →₀ ℕ)` | Structure value subject of equality | Cannot delete while retaining statement (free d); syntactic dependency, not tested negative compiler claim. Fresh arbitrary AddCommMonoid M proof succeeds, even without classical in final isolated verification. | Keep explicit d and ℕ; coefficient generalisation unapproved |
| `{R}`, `[CommSemiring R]` | Inactive section binders | Neither included in effective type (#check and equality test); no actual target hypothesis to weaken. | n/a |

No proposition hypothesis, bundled conjunction, global regularity property or strict inequality exists: unbundling, point-localising and strict-to-weak catalogue entries are inapplicable. Inversion check: no concrete witness unfolded; coefficient ℕ can be abstracted, but changing coefficient type is a separate public restatement. That pending idea is recorded rather than silently applied. No other pending action is required for this exact approved instance menu item.

Fresh native generic probe `/private/tmp/roth-separation-r01-generic.json`: success=true,timed_out=false,no diagnostics (uses local classical). Fresh independent no-classical probe `/private/tmp/roth-separation-r01-no-classical.json`: success=true,timed_out=false,no diagnostics; this establishes the minimal actual edit needs no proof adjustment. The actual scoped omission was then checked by complete module LSP, rather than only an extracted probe.

## All 42 golfing rules

Fresh live multi_attempt at original ext line52: rfl, simp, grind, aesop, exact? all report failure; apply? gives partial extensionality suggestions. Raw `/private/tmp/roth-separation-r01-attempt.json`. This replaces only a tactic span, so the final `No goals to be solved` from the leftover original next tactic in the apply? attempt is not evidence of a successful complete proof. We retain the independently compiled whole ext/cases/simp proof. No absence claim is inferred from exact?.

| Rule | Fresh concrete assessment |
|---|---|
| 1.1 by exact | n/a: no such wrapper. |
| 1.2 by rfl | n/a: ext/cases/simp argument, no by rfl. |
| 1.3 rw+exact | n/a: neither occurs. |
| 1.4 simp+exact | n/a: simp already closes branches. |
| 1.5 trailing rfl | n/a: no trailing tactic. |
| 1.6 constructor pairs | n/a: Finsupp equality, not conjunction. |
| 1.7 apply+exact | n/a: neither occurs. |
| 1.8 contradiction | n/a: no by_contra. |
| 1.9 eta | n/a: no lambda. |
| 1.10 inline have | n/a: no have. |
| 1.11 apply+intro | n/a: ext already introduces coordinate directly. |
| 1.12 redundant show | n/a: no show. |
| 1.13 have projections | n/a: no have/projection pair. |
| 1.14 merge rw | n/a: no rewrite calls. |
| 1.15 terminal simp only | Already terminal unsqueezed simp with pointwise API list. |
| 1.16 nonterminal simp | n/a: terminal on every branch. |
| 1.17 dot notation | No suitable receiver chain; explicit injection supplied to mapDomain lemma is clear. |
| 1.18 trailing parentheses | Parentheses group injection theorem passed as an argument inside simp list; <| cannot replace that comma-delimited grouping. |
| 1.19 push Not | n/a: no push_neg. |
| 1.20 existential | n/a: public equality, no existential wrapper. |
| 2.1 whole grind | Fresh live attempt fails on coordinate equality; retain pointwise proof. |
| 2.2 delete pre-grind | n/a: no retained grind. |
| 2.3 simpa | n/a: no later closing fact to consolidate. |
| 2.4 fun_prop | n/a: no regularity goal. |
| 2.5 positivity | n/a: no positivity goal. |
| 2.6 gcongr | n/a: no inequality. |
| 2.7 lia/omega | n/a: not arithmetic entailment, despite ℕ coefficient. |
| 2.8 aesop | Fresh live attempt fails, no progress. |
| 2.9 norm_num/cast | n/a: no numerical evaluation/coercion. |
| 2.10 decide/kernel | n/a: arbitrary Finsupp equality, no finite decision problem. |
| 2.11 field_simp/ring | n/a: no denominators or polynomial arithmetic proof. |
| 2.12 linear_combination | n/a: no ring-normalisation endpoint or algebraic hypotheses. |
| 2.13 wlog | none/some cases have distinct roles, not symmetric interchangeable cases. |
| 2.14 collapse calc | n/a: no calc chain. |
| 2.15 shared closure | Already cases <;> simp; preserve shared branch closure. |
| 3.1 erw→rw | n/a: no erw. |
| 3.2 fun_prop migration | n/a: no continuity/measurability tactics. |
| 3.3 omega→lia | n/a: no arithmetic tactic. |
| 3.4 rcases rfl | n/a: no rcases. |
| 3.5 attributes | No simp attribute: rewriting arbitrary d expands into two terms and repeats d; keep deliberate rewrites at caller. No new automation attribute requested. |
| 3.6 simp_all | n/a: no simp_all, no hypotheses to simplify. |
| 3.7 options | n/a: no limit options. |

## Step-back / simplify review

The natural proof checks none and some coordinates, using the map's off-range vanishing and injectivity. Native goal inspection confirms ext generates precisely the pointwise equality. Whole-proof rfl/simp/grind/aesop/exact? do not finish; apply? points toward ext. Alternative optionEquiv/optionElim representations require conversion from update/embDomain back to the additive expression needed by the caller, adding plumbing with no practical gain. No have, calc or duplicated large subterm can fold away. Three proof lines already satisfy structure bounds; no helper extraction or new identifier. Built-in simplify tool unavailable: performed this in-thread holistic pass and preserved proof byte-for-byte. The meaningful improvement is removing two unnecessary assumptions with the smallest edit.

## Fresh verification and diff gates

- Actual `lake build Roth.Separation`, session93323, exit0: `/private/tmp/roth-separation-r01-build.log`, final `Build completed successfully (1876 jobs)`.
- COMPLETE unfiltered native module LSP `/private/tmp/roth-separation-r01-lsp.json`: success=true,partial=false,timed_out=false,0 errors,28 warnings,0 sorry. Baseline31 warnings → final28; the three target warnings disappeared. Other declarations' warnings and preserved header metadata remain outside scope; no suppression.
- Actual imported built target and affected `Roth.eq_sum_X_none_pow_mul_coeffNone` have exactly `[propext, Classical.choice, Quot.sound]`. `/private/tmp/roth-separation-r01-verify.lean` and `.log`, session15138 exit0.
- Verification re-proves the ORIGINAL theorem with original effective instance arguments and the original snapshot's case-by-case proof, including a scratch-only private off-range bridge. This proof does not call the target. A proof-irrelevance equality compares that theorem against the explicit original-class-argument adapter `fun {τ} (_ : Fintype τ) (_ : DecidableEq τ) d ↦ @Roth.eq_mapDomain_some_add_single τ d`. The adapter recovers the complete original effective type.
- A separate independently proved arbitrary-τ statement is compared by `example : @Roth.eq_mapDomain_some_add_single = @independent := rfl`, checking the exact NEW type. An explicit ℕ-index application checks infinite ambient index use without Fintype. Width-100 `#check` prints original and actual new types. Generic arbitrary Type u/Type v AddCommMonoid coefficients also compile without classical. All independent proof axioms are standard.
- Raw automated diff check `/private/tmp/roth-separation-r01-diff-check.json` asserts the entire final source equals initial HEAD plus this one approved omit line. Original target docstring, signature text and body are byte-for-byte unchanged. Effective signature changes precisely by the approved omitted class arguments. No new repository helper or declaration, imports, definitions, options or attributes.

| Gate | Result | Concrete evidence |
|---|---|---|
| lake_build_file | pass | actual module session93323 exit0,1876 jobs |
| definition_protected | pass | sole added line is scoped omit; no definition diff |
| theorem_statement_protected | pass, approved generalisation | exact approved omission only; independent original adapter and exact new-type equality compile |
| structure_gate | pass | three unchanged proof lines; no conjunction or long branch |
| naming_gate | pass | descriptive equality, no forbidden abbreviation/pattern; no rename queued |
| line_packing_gate | pass | measured final lines51/52 below |
| inequality_orientation_gate | pass | complete zero-occurrence table above; no ge/gt name |
| caller/trust | pass in owned module | actual expansion caller compiles and standard axioms; cumulative whole-project checks parent-owned |
| no forbidden scaffolding | pass | one-line exact diff, no sorry/axiom/native_decide/limits/haveI/letI |

| Final signature line | Codepoints | Next unit | Arithmetic | Action |
|---|---:|---|---|---|
| 51 | 58 | equality conclusion with := by (72 unindented) | 58+1+72=131>100 | ok |
| 52 | 76 | proof body follows | n/a | ok |

Actual wc/diff arithmetic: source573→574lines (+1), git numstat1 addition/0 deletions. Theorem body stays3lines and theorem keyword-through-proof stays5lines; scoped omit adds one surrounding command line. No proof compression claimed. Initial/full source equality assertions ensure existing comments and narratives remain intact. Parent must still run sequential full `lake build`, separate `lake build Roth.LeanEval`, cumulative original/public compatibility, and exact-path commit/push before next source edit; these are not claimed completed by this worker.

## All eleven completion steps

- [x] Step1 references read.
- [x] Step2 full24-item audit written before source edits.
- [x] Step2.5 fresh five-method search plus auxiliary variants and honest index limitations.
- [x] Step2.6 every effective binder, catalogue, inversion check and actual public literature search.
- [x] Step2.7 every signature line measured, width-100 #check verified.
- [x] Step2.8 whole-signature/hypothesis inequality table.
- [x] Step3 all42 rules assessed, fresh live automation probes.
- [x] Step4 holistic step-back/simplify review and whole independent proofs.
- [x] Step5a complete unfiltered native LSP,0 errors/28 warnings/0 sorry.
- [x] Step5b actual module, exact approved diff, original/new contract and actual built axioms.
- [x] Step6a no rename required; no sidecar mutation.

Result: one approved scoped omission; two unnecessary assumptions removed, three warnings resolved,0 new helpers,0 proof edits,0 comments removed,1 docstring preserved. No golfing rule needed a new transformation; existing shared-branch rule2.15 retained. Optional future generalisation: replace ℕ coefficients by arbitrary AddCommMonoid M, compiled successfully but unapproved and outside this task. No pending proposal blocks the exact approved omission.

## Buzz: actual repository-module profile and freeze

Actual command `/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Separation.lean`, session10704 exit0. Complete raw `/private/tmp/roth-separation-r01-profile.log` and parsed `/private/tmp/roth-separation-r01-profile.log.json`. Ran with no other worker compiler/profiler/MCP request outstanding; parent confirmed no concurrent owner compiler. Target outer scoped-omit command21.552ms plus async proof94.276ms = conservative115.828ms. Nested direct theorem-command18.745ms and definition-value92.915ms are included in those outer nodes and NOT added again. The two command anchors reflect scoped omit wrapping its inner declaration. Baseline114.550ms; difference1.278ms is ordinary timing variation, no speedup claim. Target below750ms repeat threshold and1000ms budget; no repeat, fix or raised limit required. Actual expansion caller also below budget: command23.539ms+async74.836ms=98.375ms. No extracted-namespace timing used as actual repository evidence.

All native search/goal/attempt/run_code/diagnostic jobs and compiler/build/profile sessions have completed and been drained. ALL SOURCE OWNERSHIP EXPLICITLY REVOKED; worker is report-only from this point. Frozen `Roth/Separation.lean` SHA256 `b0d740f0e8638621a0fcbe68ac01235846bdde1ef27fb27b756d310b4af2dd0d`. No source edit after freeze. Parent owns subsequent cumulative compatibility/full+separate LeanEval/commit/push gates before next declaration. Final whitespace check passes.

## Owner cumulative publication gates

Source FROZEN SHA256 `b0d740f0e8638621a0fcbe68ac01235846bdde1ef27fb27b756d310b4af2dd0d`; leaf ownership revoked and requests drained before owner gates. Owner probe `63261` exit0,48.96s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL25 actual retained standardaxiom checks. `/private/tmp/roth-separation-r01-compatibility.{lean,log,json}`. Owner build session `8377` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,124.57s/29.09s; source hash stable. `/private/tmp/roth-separation-r01-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.
