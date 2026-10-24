# Main original 16 — `Roth.roth`

The source is retained unchanged after a fresh dedicated audit. The five declaration lines contain a three-line proof: assume an exponent above two; reduce to an irrational algebraic integer; contradict the already proved integral case. No helper, extraction, import, rename, API weakening or optional generalization improves this outline.

## Immutable baseline and scope

Saved genuine project-original Main684 and actual entry Main583 plus their exact target bytes BEFORE any Lean query or golf in `/private/tmp/roth-main-roth/{GENUINE,ENTRY}-{Main,target}.lean`. Genuine Main SHA `f651e4dd4b511c9aec15608b6d4ea9a2a4140ac513d486cee4c4ed7c30fa1069`; entry/current SHA `fb8f0346210a5307f4f76fc3cc31f02ee1fb0bd5d0deb3bcddadccbb1a3cf462`. Genuine and entry target including docstring are byte-identical, SHA `36d899943dce9317d59d4fc3843cc6f5fb91cdbbe55c9c343c41c09586b8ca8f`. This is target identity, not full-source identity. Only this report is written; accepted earlier helpers/proofs/reports/callers, Git, global rename queue and shared progress are untouched.

Installed mathlib-quality and lean4 skills; full installed cleanup/cleanup-all commands, golfing-rules, proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates, style-rules, naming-conventions, mathlib-review-stages, profiling and buzz command read. Whole actual Main read; classic dialect. Simplify is unavailable in this environment: the manual holistic review below is performed without claiming an invocation.

Baseline and final correctness evidence reuse is explicitly owner-authorized for the EXACT SAME source: `/private/tmp/roth-main-integral-roth` actual final `lake build` exit0 40.390s, subsequent separate `lake build Roth.LeanEval` exit0 25.760s; complete native Main/Eval/root exit0 24.222/18.776/25.179s; fresh complete unfiltered Main/Eval/root diagnostics, partial=false, no errors, Main pre-existing header warning only. Eval SHA `610ec95658c5d43c931217bfb56b54d62f825473de17b3bdf6a1dde85dd900ca`. No owner-label rebuild or repeated unchanged native/LSP check is claimed. Cache fetch unnecessary. Whole-file copyright/header warning and unused eta helper are reserved to independent file final review.

## Full 24-item audit

| Item | Finding and action |
|---|---|
| 1 LINT | No target warning/error in accepted same-source complete native/LSP; retain existing line1 header warning qualification. |
| 2 HAVE SCAN | Zero `have` occurrences; nothing to inline. The `obtain` decomposes actual existential data once. |
| 3 SET_OPTION | None; defaults200000/20000/512 retained. |
| 4 SIMP SQUEEZE | No simp call. `by_contra!` already expresses logical normalization directly. |
| 5 NAMING | `Roth.roth` is the named main theorem in its subject namespace; snake_case, no prohibited abbreviation/scheme/numeric/helper pattern. No rename. |
| 6 LINE PACKING | Both signature lines measured below; no available next binder fits. |
| 7 BY PLACEMENT | `:= by` ends the conclusion line. |
| 8 FORMAT | Two-space proof/four-space continuation, one tactic per line, no semicolons, empty lines or trailing spaces inside declaration. |
| 9 COMMENTS | No inline proof comments present; none removed. All source-citation prose preserved. |
| 10 DOCSTRING | Identifies the named main result, distinguishes general algebraic case from preceding integral case and following rational formulation, records exact §6 source. No proof strategy. Existing source quotation is preserved for provenance; no gratuitous documentation churn. |
| 11 VISIBILITY | Public headline theorem with downstream rational/Eval use; retain public. |
| 12 STRUCTURE | Three proof lines≤15; no conjunction in conclusion or long branch. Extra helper would fragment the outline. |
| 13 MATHLIB | Five methods and variants below. Main content is not a thin chain of mathlib facts: the earlier project integral theorem carries Roth's argument. No new API gap or wrapper. |
| 14 JUNK DEF | n/a: theorem, no def. |
| 15 EXISTS LEMMA | n/a: public inequality theorem, not a trivial private witness lemma. |
| 16 SHOW/CHANGE | None. |
| 17 PUSH_NEG | None; existing `by_contra!` is already canonical. |
| 18 GENERALISE | All five binders assessed below; no supported small-safe weakening. |
| 19 INEQUALITY | Signature conclusion `κ ≤ 2`; zero reversed code inequalities; scan below. |
| 20 NORMAL-FORM | `Set.Infinite` on approximation pairs is the project's primary canonical formulation; rational-denominator companion follows separately. No unstable simp equivalence introduced. |
| 21 SYNTAX-GEN | Implicit real/exponent, explicit usable hypotheses; existing caller can pass facts directly. No easier equivalent form justifies API restatement. |
| 22 IMPORT-FANOUT | n/a: no new imports. |
| 23 CASTS | Zero explicit casts/coercions in target code, zero dropped/kept; no diff casts. |
| 24 INSTANCE-NAME | n/a: no instance declaration or local instance. |

## Line packing

Width100 `#check @Roth.roth` observation is in independent.stdout and will also be in final exact prefix profile.

| Signature line | Codepoints | Next complete signature token | Arithmetic | Action |
|---|---:|---|---|---|
|567|73|`(hinf : (approxSet α κ).Infinite)` (33)|73+1+33=107>100|ok|
|568|51|none; proof body follows|n/a|ok|

Conclusion is already on the last hypothesis line. Proof line lengths are below100.

## Inequality scan

| Location | Occurrence | Action |
|---|---|---|
|568 conclusion|`κ ≤ 2`|canonical; retain|
|entire signature/hypotheses|zero `≥`/`>`|no rewrite or rename|

`.not_gt` in the proof is an existing mathlib elimination lemma, not a newly declared reversed-name result. Prose `q > 0` remains natural source wording.

## Five-method search and six replacement rules

| Method | Actual query | Outcome |
|---|---|---|
| A Lean-Finder | Roth theorem irrational algebraic real number infinitely many rational approximations exponent at most two | Dirichlet infinite square-bound and Liouville definition; partial/topic matches, not Roth. |
| B Loogle | `Irrational, IsAlgebraic` | Empty result, successful response. |
| C LeanSearch | Roth theorem irrational algebraic real approximation exponent | Dirichlet improvement, Liouville root lower bound and almost-everywhere non-Liouville; no replacement of this contract. |
| D local source | Untruncated `roth|thue.siegel|approx.*algebraic` in NumberTheory; examined DiophantineApproximation.Basic and Liouville.Basic declarations | Additive Roth is unrelated; LiouvilleWith mentions Roth as a mathematical reference. Dirichlet gives exponent2 approximations and Liouville a degree-dependent bound. |
| E name pattern | `roth`, local search, limit20 | Existing project main/integral/rational results and unrelated additive Roth names; index unavailable is explicitly qualified, not absence evidence. |

Auxiliary variants: `_of_isIntegral`, `_rat`, `infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational`, `exists_pos_real_of_irrational_root`, `_of_irrational`, finite/infinite alternatives. Common-equivalents table: no discrete/compact/separation/bornology bucket applies. These searches establish usable partial building blocks, not an exhaustive mathematical absence theorem. No new library theorem is invented and no compile-checked generic-absence claim is made. Existing project reduction and integral result are used directly; no mathlib duplicate wrapper/custom predicate is added, no deletion justified, no new import/documentation API change needed. Existing `Irrational`, `IsAlgebraic` and `Set.Infinite` are standard predicates.

## Every-binder generalisation and literature

| Binder | Class | Actual role | Candidates and assessment | Result |
|---|---|---|---|---|
| `{α : ℝ}` | structure value | Object of algebraicity/irrationality/approximation predicates | Drop fails to state dependent hypotheses; arbitrary ordered field changes real absolute-value/rpow/rational-height content and accepted reduction API. No optional ambient extension. | retain |
| `hα : Irrational α` | proposition | Essential input to reduction and integral theorem | Drop is mathematically false: α=0, h=0, arbitrary positive q give infinitely many exact pairs for κ=3. No typeclass parent or point-local weakening. | retain |
| `halg : IsAlgebraic ℚ α` | proposition | Essential input to denominator clearing/reduction | Drop fails for sufficiently well approximable transcendental/Liouville numbers. Integral assumption would strengthen rather than weaken. Changing base to ℤ is equivalent presentation, already bridgeable by standard API. | retain |
| `{κ : ℝ}` | structure value | Approximation exponent and conclusion | Drop leaves exponent unbound; arbitrary real exponents include the sharp threshold; restricting positivity or integrality is a specialization. | retain |
| `hinf : (approxSet α κ).Infinite` | proposition | Supplies infinitely many approximations to reduction | Drop makes κ=3 contradict the conclusion for any algebraic irrational. Nonempty/arbitrarily one approximation is weaker but insufficient; finite sets of positive denominators can occur. `Infinite` is already canonical. | retain |

Mechanical drop candidates are rejected on concrete mathematical dependency/content grounds, not reported as successful compiler edits. There are no class/decidability/universe binders, strict numeric hypotheses to relax, bundled conjunctions to project, or global analytic hypotheses to localize. Inversion check: no concrete named witness unfolded into abstract mathematics; α and κ remain the actual variables of accepted reduction/integral results.

Actual literature web query: “Roth theorem irrational algebraic real numbers generalization Schmidt subspace theorem”. Top relevant hits include [Bugeaud, Quantitative versions of the Subspace Theorem and applications](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.749.pdf), [The subspace theorem](https://algant.eu/documents/theses/zerbini.pdf), and [Waldschmidt, Some Remarks](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/SomeRemarksDiophantineEquationsDiophantineApproximationVI.pdf). Standard form is finite rational approximations at exponent2+ε; Ridout/Schmidt extend valuation/dimensional content and require a different theorem, not a removable local assumption. Local authoritative clean.tex1139–1146 matches this theorem exactly. Math ChatGPT MCP unavailable; no invocation claimed. No actionable small-safe or in-scope big-change candidate supported.

## All 42 golfing rules

| Rule | Status |
|---|---|
|1.1 by exact|n/a: three real proof steps, no trivial wrapper|
|1.2 by rfl|n/a: no rfl|
|1.3 rw+exact|n/a: no rw|
|1.4 simp+exact|n/a: no simp|
|1.5 simp+rfl|n/a: neither|
|1.6 constructor pair|n/a: inequality conclusion|
|1.7 apply+exact|n/a: no such adjacent pattern|
|1.8 by_contra!|already applied in entry; retain|
|1.9 eta lambdas|n/a: no lambdas|
|1.10 single-use have|n/a: zero have|
|1.11 apply+intro|n/a: no such pattern|
|1.12 redundant show|n/a: zero show|
|1.13 obtain|already destructures actual reduction existential directly|
|1.14 consecutive rw|n/a: none|
|1.15 terminal simp only|n/a: none|
|1.16 nonterminal simp|n/a: none|
|1.17 dot notation|already `.not_gt` on the bound|
|1.18 trailing parens|n/a: parentheses necessary to call `.not_gt` on result|
|1.19 push_neg|n/a: no deprecated tactic|
|1.20 trivial existential helper|n/a: no new helper; accepted reduction is substantive|
|2.1 grind whole|No forced replacement: three-line mathematical outline already≤15, accepted quantitative reduction not a default logical grind fact. No new broad experiment claimed.|
|2.2 pre-grind deletion|n/a: no grind|
|2.3 simpa|n/a: no simplification chain|
|2.4 fun_prop|n/a: no function-property goal|
|2.5 positivity|n/a: conclusion κ≤2 requires number theory, not structural nonnegativity|
|2.6 gcongr|n/a: no congruence or monotonicity calculation|
|2.7 lia/omega|n/a: real exponent bound is not Nat/Int arithmetic|
|2.8 aesop|No forced replacement or broad replay: dependency-sensitive existential reduction and integral theorem already explicit; no shorter zero-risk logical pattern.|
|2.9 norm_num/norm_cast|n/a: no numeric/cast computation|
|2.10 decide|n/a: general real algebraicity/infinitude not finite decidable computation|
|2.11 field_simp;ring|n/a: no field identity|
|2.12 linear_combination|n/a: no ring/ring_nf terminal identity|
|2.13 wlog|n/a: no symmetric branches|
|2.14 calc term|n/a: no calc|
|2.15 <;>|n/a: no repeated goals|
|3.1 erw→rw|n/a: no erw|
|3.2 fun_prop migration|n/a: no legacy analysis automation|
|3.3 omega→lia|n/a: no omega|
|3.4 rfl substitution|n/a: no rcases-with-rfl|
|3.5 attributes|No simp/grind attribute: headline quantified arithmetic theorem has no simplifier normal form; global automation change unjustified.|
|3.6 simp_all|n/a: none|
|3.7 resource raises|none to remove; zero added|

## Manual holistic review before final gates

The proof has one logical contradiction boundary, one existential elimination, one order-theoretic contradiction. The actual mathematical abstraction already lies in accepted `reduction` and `roth_of_isIntegral`; another helper, inline reproof or global automation would obscure this boundary. Distinct scratch proof uses `le_of_not_gt`, explicit `intro`, `rcases`, and `not_lt_of_ge`; this is a verification witness, not a source rewrite. It has no clarity/performance reason to replace the existing three-line outline. No duplicated local proof skeleton, unnecessary instance, cast, hidden assumption, missing canonical API, stale comment or documentation action found. Scope remains original16 only.

## Final gates and performance

All scoped gates pass with the explicitly authorized exact-source build/native/LSP reuse. `same-source-gate-reuse.json` binds current Main/Eval hashes, terminal receipts, prior actual target TYPE/opaque/universe row and unchanged caller evidence. No new full build/native/editor execution is claimed.

| Gate | Result and evidence |
|---|---|
| FULL + separate Eval | PASS reused actual full exit0 40.390s then separate Eval exit0 25.760s; exact Main/Eval source hashes unchanged |
| Complete native/LSP | PASS reused complete serial Main/Eval/root evidence; no target errors; pre-existing header warning qualified |
| Source/definition/signature protection | PASS actual full Main byte-equal to entry; empty source diff; no new identifier or cast |
| Structure/naming/packing/inequality | PASS three proof lines≤15; clean named main result; complete measured signature table; no reversed signature inequality |
| Actual family and universes | PASS independent compile exit0 29.738s, BEFORE per-row guards enumerated production `Roth.roth` and distinct `Roth.independentRoth`; each actually has only its opaque root and observed universes[] |
| Strict semantic TYPE | PASS semantics exit0 28.818s; complete actual old/current/independent Expr + raw repr exact; recursive Name/Level/BinderInfo/metadata/literal/projection comparison, no ExprBEq shortcut, no hygiene exception |
| Actual opaque VALUE | PASS both actual VALUES inferred in memory, closed/no free/meta/loose variables or admissions, defaults200000/20000/512, standard propext/Classical.choice/Quot.sound only. Production46,259bytes, independent41,067bytes; hash/length receipts, no full VALUE dumps or identity claim |
| Independent dependency gate | PASS fresh actual local graph acyclic/self-free; rejects actual target/generated/caller/later/circular dependencies; permits only exact accepted earlier reduction/integral/approxSet leaves and actual strictly upstream ModuleIdxs. Earlier helper/caller VALUES not reinferred |
| Current prefix TYPE | PASS final-profile-TYPE exit0 21.081s, full strict recursive/raw actual prefix TYPE + actual universe list identical to current target |
| Caller preservation | PASS prior actual full caller TYPE/metadata and valid proof evidence reused under unchanged API/source, plus same-source FULL/Eval/native coverage; no unrelated caller reproof |

Exact current prefix profile is uniquely bound to the full canonical doc/signature/proof command and actual observed family. All four disjoint roots are counted: outer command16.094ms, async proof9.268ms, kernel parent0.939ms, async lint4.620ms; total30.921ms. Nested kernel0.918ms is not counted twice. Actual kernel family is precisely `[Roth.roth]`; compiler roots and lazy prior DATA roots are empty for this command. Under1000ms and below750ms, so no repeat is required. FAST-BOARD; zero resource raises, scaffold/source edits, deferrals or optional repairs.

The owner ACK was received BEFORE any profile preparation; owner writes/heavy work idled. Safe task-only observer was first run escalated; full parent/Lake environment equality was checked in memory, with only hashes/lengths and approved PATH/LEAN/toolchain fields persisted. Frozen source/import/tool/default/map inputs remained exact. All five profile launches exited0, actual capture driverPID33190 and child PIDs/groups33192/33217/33243/33300/33330 were absent at RAW UNPARSED notice. Explicit OWNER RELEASE preceded parsing. Actual session57414 and parser session45691 are terminal0. Receipts reside in `/private/tmp/roth-main-roth/final-profile`.

Historical accepted all17 row has a full identical canonical target command and four actual disjoint roots totaling45.243ms. Narrow indexed seeks matched the complete printed command and every root/kernel parent against the historical raw file; no broad317MB reparse or baseline recapture. Historical raw SHA is reused from the accepted index with exact file length verified, not freshly rehashed. This is Main689 after MainLemma repairs, separate from project-originalMain684 and the fresh current prefix context. No speedup ratio, cause/noise dismissal or cross-context timing identity is claimed. Detailed binding is in historical-raw-binding.json.

Phase5a: no supported refactoring. Phase5b: no target rename; global queue untouched. Simplify unavailable: substantive manual pass-through above, no invocation claimed, no findings or fixes. Buzz FAST-BOARD30.921ms, no heartbeat wrapper or limit raise. New identifier table empty because source diff is empty. Inline proof comments0→0, none removed. No failed Lean candidate or incomplete guard row in this worker. The earlier reused evidence retains its documented historical scratch/Eval overlap FAIL qualification; it is not relabeled a fresh serial pass.

| Required scoped phase | Status |
|---|---|
| Save genuine/entry before Lean; read skills/commands/references/full source | complete |
| Full24-item/42-rule/per-binder/HAVE/search/packing/inequality/docs/casts | complete |
| Step-back mathematical reflection and manual holistic review | complete, unchanged proof justified |
| Source/API/caller/build/native/LSP gates | pass with authorized same-source reuse and historical qualification |
| Fresh actual complete inventory/TYPE/opaque VALUE/default/no-self checks | pass |
| Exact final current prefix profile + current TYPE + repeat rule | pass, no repeat required |
| Report and actual final drain/END/ALL lease release | complete in FINAL.json |

Result: declaration5→5 lines, proof3→3, zero source delta; report only. Main583lines/35,289bytes unchanged. No project progress credit or publication is claimed by this worker. Owner review and exact-path publication remain owner-controlled before original17.
