# Cleanup audit: `Roth.exists_monic_aeval_eq_zero`

Result: PASS for this dedicated original-declaration-6 audit. The theorem now requires only integrality, with the identical monic/root/degree-at-least-two conclusion. The chosen witness is `f * X²`. The sole project caller removes its `hα` argument; its statement is unchanged. No helper/import/rename/ambient expansion was added. Source: `Roth/Main.lean`, final L136–141; authorized caller repair final L503.

Measured code: 11 → 6 lines, proof body 9 → 4 lines; documentation plus code 17 → 12 lines. Main: 663 → 658 lines. Early scratch notes and the dispatch line range were off by one; these are actual final measurements. No previous Main declaration audit was reopened. This report does not claim whole-file completion.

## Baseline and scope
The same-source accepted baseline FULL build (60.783572 s), separate Eval build (31.990705 s), complete Main/Eval/root native checks, and complete Main LSP diagnostics are reused from `/private/tmp/roth-main-reduction`; owner acceptance is `/private/tmp/roth-main-owner/reduction-owner-accepted-v1.json`. No redundant entry-source build was run. Original and entry targets were saved before any Lean experiment and are byte-identical: SHA256 `ac56c0a713331dfb2b7eac0f1fd41f2a1cfd169d0ffee0f7c242667e8616c90c` (including final newline). Genuine original Main SHA256 `f651e4dd4b511c9aec15608b6d4ea9a2a4140ac513d486cee4c4ed7c30fa1069`; entry Main SHA256 `84c2a9dc00bab32468251e3a83bc4be7944bd2b3e933553d64e7170e362e8dd2`.

The full installed mathlib-quality/lean4 skills, cleanup/cleanup-all workflows, mandatory golfing/proof/search/generalisation/gate references, applicable style/naming sections, and review-stages documentation were read. Owner binding scope and standing authorization supersede generic template escalation/rename/visibility exceptions. `Skill(simplify)` is unavailable in this host; it was not invoked or falsely credited. Fresh independent holistic whole-file review remains the owner's later file-final task.

## Full 24-item audit
1. **LINT:** no target warnings. Final complete LSP has 0 errors and four existing warnings outside target: header L1; unused `hδ` L302, `hQ` L443, `hc` L444. No suppression added.
2. **HAVE SCAN:** original and final target contain zero `have` statements; no inline candidates omitted.
3. **SET_OPTION:** no per-declaration or introduced limit/debug options; defaults verified 200000/20000/512.
4. **SIMP SQUEEZE:** original has no simp. Final sole `simp [hf.ne_zero]` is terminal. A terminal simp-only root variant compiled; direct rw is shorter and avoids terminal squeeze. Broad simp failed due algebra-map normalization; preserve explicit root rw.
5. **NAMING:** `exists_monic_aeval_eq_zero` describes the witness/evaluation conclusion, uses snake_case with mathlib `aeval`, no forbidden abbreviations or numbered/single-letter patterns. No `_ge_`/`_gt_`. No rename needed or queued; shared queue untouched.
6. **LINE PACKING:** final measured table below; all signature lines covered, no repack rows.
7. **BY PLACEMENT:** `by` ends final signature line; no standalone by.
8. **FORMAT:** two-space proof indentation, four-space signature continuation, no empty proof lines, no semicolon chains, haveI/letI, or trailing whitespace. The old nested `push_cast; linarith` disappears with its branch.
9. **COMMENTS:** no inline proof comments existed; zero removed. Source quotation retained exactly. Docstring now accurately describes the stronger result and warns users that the witness may be reducible/nonminimal; no proof-strategy prose was introduced.
10. **DOCSTRING:** retained public documentation/source context, refined with the positive application tip about witness degree and reducibility; source quotation unchanged.
11. **VISIBILITY:** classic file. Preserve public contract under owner's explicit scope; mathematical witness result is available to public downstream users and consumed by public `roth_of_isIntegral`. No optional visibility/API restriction.
12. **STRUCTURE:** final body four lines; two one-line branches. The ∃-bound conjunction bundles properties of the same witness and is consumed together at the caller; splitting into independently chosen witnesses would change the useful contract. No long branch, repeated skeleton, helper, or decomposition needed.
13. **MATHLIB:** five methods and compiled whole-goal discovery below; use existing integrality, monicity, aeval, and natDegree API. No exact equivalent found by these probes; no unsupported global absence assertion or speculative helper extraction.
14. **JUNK DEF:** n/a: theorem, no def/abbrev added/changed.
15. **EXISTS LEMMA:** not a private rfl-only witness; retain the substantive monic/root/degree construction.
16. **SHOW vs CHANGE:** no tactic `show`; original typed omega proof disappears. No change/show introduced.
17. **PUSH_NEG:** none; original by_contra! disappears with the degree-case argument.
18. **GENERALISE:** constructively drop irrationality under standing authorization and narrow caller lease. Retain integrality, bound α and concrete ℝ/ℤ scope; full per-parameter classification below. No optional ambient generalisation.
19. **INEQUALITY:** final signature has canonical `2 ≤ f.natDegree`, no ≥/>. Occurrence table below.
20. **NORMAL-FORM:** monic + aeval-zero + natural-degree bound uses the standard integral witness representation. No parallel equivalence/normal form added.
21. **SYNTAX-GEN:** stronger single-hypothesis statement simplifies its caller; property order, implicit α and existential bundling preserved.
22. **IMPORT-FANOUT:** n/a: imports unchanged.
23. **CASTS:** 0 dropped / 0 introduced cross-type casts / 0 introduced load-bearing ascriptions. `Polynomial.X`'s coefficient ring is inferred from `f`; no redundant cast added.
24. **INSTANCE-NAME:** n/a: no instance declaration or local instance plumbing.

Issues found/fixed: four concrete items—unnecessary irrationality, degree-case proof, documentation alignment, and required caller argument adjustment. Final width measurement passes without extra signature churn. Refactoring deferred: none for this declaration.

## Mathlib search-status
| Method | Actual query / result |
|---|---|
| A Lean-Finder | `integral element root monic polynomial arbitrarily large degree`; results included AdjoinRoot.isIntegral_root', IsAdjoinRootMonic.isIntegral_root and IsIntegral.of_aeval_monic, not the required degree-bounded witness. |
| B Loogle | `IsIntegral, Polynomial.Monic`; results minpoly.monic, IsIntegral.of_aeval_monic and related minpoly/AdjoinRoot results, no exact strengthened conclusion. |
| C LeanSearch | `An integral element is a root of a monic polynomial of degree at least two`; integrality definitions and rational-root criterion, no exact match. |
| D source | Untruncated `rg` for exists/monic/degree/aeval names and natDegree_mul_X, monic_X_pow, monic degree multiplication; verified Degree/Operations.lean natDegree_mul_X_pow and Monic.lean Monic.natDegree_mul, plus monic_X_pow. No exact full-name equivalent located. |
| E local name pattern | `natDegree_mul_X` located natDegree_mul_X and natDegree_mul_X_pow; index unavailable, so only positive source results credited (no index-based absence claim). |

Auxiliary variants: monic_X_pow; Monic.mul/pow/natDegree_mul/ne_zero; natDegree_mul_X_pow; degree-zero monic polynomial; minpoly.monic/aeval; IsIntegral.of_aeval_monic. Common-equivalents table: no bucket match. Actual original whole-goal `exact?` failed; `apply?` offered only partial logical/Finsupp existential restatements. Whole grind/simp/aesop failed. These are bounded compiled discovery results, not a proof of library-wide absence. Keep the local construction on the verified existing API. Search receipts: `search0.json`–`search3.json`; source search output and LSP tactic results in worker transcript.

## Generalisation status
| Parameter | Class / use | Mechanical catalogue candidates | Verified result |
|---|---|---|---|
| `{α : ℝ}` | structure value; root argument in conclusion | Drop-test: conclusion still binds α, so deleting its binder leaves unbound/reimplicitized α rather than a mathematical weakening. No explicit universe/typeclass/strict/point-global/bundled hypothesis. Ambient ℝ→abstract algebra would be an optional restatement, outside binding scope. | Keep α and its implicitness; no unsupported ambient expansion. |
| `(hα : Irrational α)` | proposition; originally excludes degree 1 | Drop-test with new padding construction, rather than merely erasing a used hypothesis. No applicable strict→weak/point-local/typeclass-parent/universe form. | Probe v2 compiled, final whole-file LSP/build/native clean; dropped. Old exact full contract recovered by checked theorem application. |
| `(hint : IsIntegral ℤ α)` | proposition; supplies monic vanishing polynomial | Drop-test; no strict/point-global/universe/typeclass-parent weakening. Replacing integrality by a monic root witness is its definition, not a weaker mathematical condition. | Actual `clear hint; grind` fails. Retain: the conclusion itself gives an integrality witness; dropping integrality would assert all real numbers integral over ℤ. |

Inversion check: α is a bound element, not a named concrete object unfolded away; witness f remains central throughout the proof. No concrete-named-object abstraction diagnostic fires. The irrationality drop is a public API strengthening explicitly authorized by the standing user instruction and owner caller lease, not hidden golf drift. No other big-change candidate implemented/deferred.

### Literature search status
Web query: `integral element monic polynomial arbitrarily large degree generalization Stacks project`. Top three returned hits were arXiv 1412.4548 (fewnomials, irrelevant to this elementary witness), Stacks Commutative Algebra, and an Algebraic Number Theory text (criterion for integrality). The canonical definition is [Stacks, Definition 10.36.1](https://stacks.math.columbia.edu/tag/00GI): an integral element satisfies some monic polynomial. The inference that multiplication by X² preserves a root and forces a sufficiently large degree is our elementary construction, independently compiled, not a quotation of a literature theorem. ChatGPT math MCP: unavailable in this session; no invocation claimed. No optional literature-driven ambient expansion/helper was added.

## Line packing
Actual width-100 #check reference from the frozen profile derivative:
```lean
@Roth.exists_monic_aeval_eq_zero : ∀ {α : ℝ},
  IsIntegral ℤ α → ∃ f, f.Monic ∧ (Polynomial.aeval α) f = 0 ∧ 2 ≤ f.natDegree
```
Widths count codepoints, not UTF-8 bytes. The complete return expression is the next syntactic signature block.

| Sig line | Chars | Next token/block | Arithmetic | Action |
|---|---:|---|---|---|
| 136 | 68 | full `∃ f : Polynomial ℤ, ... := by` (78 chars without indentation) | 68 + 1 + 78 = 147 > 100 | ok |
| 137 | 82 | no next signature line; proof body next | n/a | ok |

## Inequality scan
| Occurrence | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| n/a | complete signature/hypotheses | no ≥ or > | none; `2 ≤ f.natDegree` already canonical | none |

### Golfing rule pass (42/42)
| Rule | Status |
|---|---|
| 1.1 by exact wrapper | n/a: no outer `by exact` wrapper. |
| 1.2 by rfl | n/a: no reflexive proof. |
| 1.3 rw + exact | n/a after strategy change: root branch is closed by one rw; original `rwa` was already compressed. |
| 1.4 simp + exact | n/a: no simp-followed-by-exact chain; degree closes by simp. |
| 1.5 trailing rfl | n/a: no trailing rfl. |
| 1.6 constructors | already anonymous; retain one anonymous existential/conjunction constructor with two proof holes. |
| 1.7 apply + exact | n/a: no such chain. |
| 1.8 by_contra + push_neg | original already by_contra!; entire contradiction argument eliminated by padding. |
| 1.9 eta reduction | n/a: no lambdas in target. |
| 1.10 inline have | n/a: no have declarations. |
| 1.11 apply + intro | n/a: no universal introduction goal. |
| 1.12 redundant show | n/a: no show. |
| 1.13 have projections | original/final already obtain existential witnesses. |
| 1.14 consecutive rw | root equation closes in one rw list; no mergeable sequential rw. |
| 1.15 terminal simp only | n/a: none retained; tested terminal simp-only root also works but rw is shorter and avoids fragile unsqueezing. |
| 1.16 nonterminal simp | n/a: sole final simp is terminal. |
| 1.17 dot notation | applied: hf.mul and hf.ne_zero; direct Polynomial.monic_X_pow constructor remains qualified. |
| 1.18 <\| | n/a: no parenthesized trailing tactic/lambda argument. |
| 1.19 push Not | n/a: no push_neg. |
| 1.20 trivial private existential | n/a: public monic root/degree theorem, not private rfl witness. |
| 2.1 whole grind | tested on actual original goal; failed. No automatic polynomial padding witness discovered. |
| 2.2 delete before grind | n/a: no grind retained. |
| 2.3 simpa | tested probe v1 degree simpa compiled but linter recommended simp; replaced with simp. |
| 2.4 fun_prop | n/a: no analytic function-property goal. |
| 2.5 positivity | n/a: no structural zero-positivity goal in final target; required lower bound is 2, discharged directly by simp. |
| 2.6 gcongr | n/a: no calc/monotonicity chain; natDegree padding rewrite plus simp closes directly. |
| 2.7 lia/omega | original omega-based small-degree case removed; independent proof uses lia after natDegree_pow, verifying arithmetic route. |
| 2.8 aesop | tested whole original goal; failed without witness construction. |
| 2.9 norm_num/norm_cast | n/a: no concrete standalone numerical or cast goal; exponent 2 handled by simp. |
| 2.10 decide | n/a: existential polynomial search is not finite decidable computation. |
| 2.11 field_simp/ring | n/a: no denominators or ring-identity goal. |
| 2.12 linear_combination | n/a: no ring/ring_nf exit or ring-equation hypotheses. |
| 2.13 wlog | n/a: degree-zero/degree-one cases were not symmetric and are eliminated. |
| 2.14 calc composition | n/a: no calc block. |
| 2.15 <;> | tested common simp closure; failed root goal due algebraMap-vs-cast normalization; separate rw/simp retained. |
| 3.1 erw/rw | no erw; final root branch uses rw. |
| 3.2 continuity/measurability | n/a: neither present. |
| 3.3 omega/lia | removed original omega entirely; independent arithmetic uses lia, no omega added. |
| 3.4 rcases rfl | n/a: no substitution-pattern rcases. |
| 3.5 automation attributes | n/a: existential construction has no canonical rewrite normal form; no blanket automation attributes added. |
| 3.6 simp_all | n/a: no simp_all only or context-wide simplification needed. |
| 3.7 resource option | n/a: no resource limit option present or introduced. |

### Step back and think
Whole-goal grind/simp/aesop/exact? did not close the goal. apply? offered only partial logical restatements, not a mathematical root/degree theorem. Term-mode packing would obscure the two independent obligations and save no substantive proof step. Multiplying any integral witness by X² removes the unjustified reliance on minimality while preserving precisely all three promised witness properties. This strategy is four tactic lines rather than the original nine and needs neither irrationality nor any new helper/import. The separately compiled square-witness proof establishes the stronger statement without using the target or any Roth declaration.

## Evidence, independent proof, and strict semantics
All evidence is under `/private/tmp/roth-main-monic-root`. `Main-entry.lean`, `original-target.lean`, and `final-target.lean` retain the exact source boundaries. `Main-worker.diff` and `source-bindings.json` verify the entire file outside the target is identical except the single authorized caller argument removal. Existing source citation text is exact. No Git/shared progress/shared queue write was made.

The accepted genuine-original full TYPE/opaque VALUE records are reused from `/private/tmp/roth-mainlemma-helper18-fresh1/after-imported-pairs-v1.log` and its row index. `genuine-original-reuse.json` binds the actual original family (root plus `_proof_1_1`), original source target, exact row offsets/hashes/lengths, universes/defaults/standard axioms. No unchanged prior DATA or preceding declaration was re-proved/exported. Evidence hygiene erratum: the first indexed extraction briefly wrote the old target/caller JSON including VALUE fields to scratch; both were immediately replaced by TYPE/metadata-only JSON. No such duplicated full old VALUE remains. No old caller re-elaboration was performed.

`IndependentMonic.lean` proves the same stronger statement with f²: a degree-zero monic polynomial equals 1 and cannot vanish, hence f has positive degree, so its square has degree at least two. It imports only the two mathlib imports, no Roth module. It was saved before Lean, compiled to a cached scratch module and then imported by the small checker. This is a fresh proof with a different witness/degree argument, no target application or later Roth closure.

`Semantics.lean` uses a strict recursive Expr comparator covering every Expr constructor, complete Name/Level/BinderInfo, metadata DataValue/Syntax/SourceInfo; it has no blanket Expr-BEq shortcut. It checks actual full TYPE equality of production and independent roots, and exact old full TYPE equality for `oldContractRecovery`, whose body applies the stronger theorem to hint. It also strictly checks `roth_of_isIntegral` against its accepted actual full TYPE, and infers/checks its fresh actual full opaque VALUE in memory (closed, no sorry/open metavariables, standard axioms). It neither clones/reproves the large caller nor prints/persists its VALUE. The caller's remaining source, statement, and every other proof step are unchanged. The old source caller contracts plus fresh full build/natives are reused as replay evidence; this is not the caller's later substantive audit.

Actual fresh target family: `Roth.exists_monic_aeval_eq_zero`; independent actual family: `independentMonic`, `independentMonic._proof_1_1`. Actual universes are recorded per declaration; empty-universe checks apply only to these known monomorphic roots/caller/recovery, not blanket helper assumptions. All fresh actual opaque proof values are inferred against their actual full type and checked closed/standard (`propext`, `Classical.choice`, `Quot.sound` subset), local graph acyclic, no self/target/circular/later Main use. All external dependencies have actual module index strictly before Main; this target needs no accepted preceding Main declarations at all. 369 dependency-origin observations are retained. Production VALUE representations are observed in memory, with hash/length retained; no claim of persisted full production VALUE or identity between distinct proofs/modules is made. Full actual prefix VALUE is emitted separately by the focused profile derivative. Default limits 200000/20000/512 verified; no limit raise or new axiom/sorry/native_decide/count_heartbeats.

### Actual tests and failures
| Run | Result |
|---|---|
| Initial padding probe v1 | Failed: broad simp normalized algebraMap to Int.castRingHom before hf0 could rewrite; degree simpa produced unnecessarySimpa warning. |
| Padding probe v2 | PASS, 25.585 s, explicit root rw and terminal degree simp; clean output. |
| Initial independent build | Failed before elaboration: scratch output was outside default root; no false proof failure credited. |
| Independent build v2 with explicit scratch root | PASS, 26.033 s. |
| Fresh semantics | PASS, 82.948 s; driver terminal 0. |
| Whole original goal LSP attempts | grind/simp/aesop/exact? failed; apply? partial logical candidates only. |
| First multiline LSP drop/common-closure snippets | Parser/indentation failures, discarded; corrected semicolon test establishes actual hint-drop failure and common-simp root failure. |
| Correct root simp-only variant | PASS, but explicit rw is shorter and preserved. |
| Full lake build | PASS, 61.798 s, `final-full-build-{launch,terminal}.json`, exit 0. |
| Subsequent separate lake build Roth.LeanEval | PASS, 33.389 s, `final-eval-build-{launch,terminal}.json`, exit 0. |
| Fresh unfiltered native Main / Eval / root | PASS, 39.498 / 40.179 / 26.246 s; all output retained and driver terminal 0. |
| Final actual-source LSP | complete, 0 errors, 4 existing warnings elsewhere; `final-Main-lsp.json`. |

The FULL→Eval builds used identical final Lean code but preceded the owner's two-line docstring wording refinement. That exact doc-only delta was applied only after build/independent jobs drained. Per owner instruction, no redundant full build was run just for wording. Fresh native checks, final actual-source LSP, semantic evidence, and the frozen profile bind the final source after that refinement.

### Introduced identifier verification
| Identifier / application | Evidence |
|---|---|
| Polynomial.monic_X_pow | source Degree/Defs.lean; compiled probe/production |
| Polynomial.Monic.mul | source monic API; compiled hf.mul application |
| Polynomial.Monic.ne_zero | source monic API; compiled terminal simp |
| map_mul, zero_mul | compiled root rw, final native/semantic proof inspection |
| Polynomial.natDegree_mul_X_pow | positive local/source search; used implicitly by final simp; compiled probe |

## Diff gates
| Gate | Result | Concrete basis |
|---|---|---|
| lake_build_file | PASS | actual full build then separate Eval, plus unfiltered native Main/Eval/root; receipts above |
| lake_build | PASS | `/Users/ramin/.elan/bin/lake build`, exit 0; doc-only qualification above |
| definition_protected | PASS | no def/abbrev/import/instance line changed |
| theorem_statement_protected | PASS with authorized strengthening | declared audit item 18 removes hα; same conclusion, exact full old contract recovered; caller TYPE exact |
| structure_gate | PASS | body 4 lines, branches 1 line; ∃-bound witness properties remain bundled; no extraction needed |
| naming_gate | PASS | descriptive snake_case, no forbidden pattern/abbreviation; no rename necessary |
| line_packing_gate | PASS | both signature lines measured; all rows ok |
| inequality_orientation_gate | PASS | full signature scan: zero ≥/>; no _ge_/_gt_ rename |
| cumulative_no_unintended_breakage | PASS | exhaustive actual caller search: only roth_of_isIntegral, repaired under narrow lease; fresh caller VALUE/type + full/root/Eval validation |
| comment preservation | PASS | no inline comments removed; historical citation exact; documentation alignment authorized |
| scope gate | PASS | only target + leased caller argument + this report; no helper/ambient/general queue/Git writes |

Overall: PASS for this declaration. Existing file warnings outside scope remain; no warning suppression or false warning-free file claim.

## Focused buzz pass
Outcome: FAST-BOARD, focused exact-prefix derivative. This is not the mandatory later fresh full-source all-row profile.

The owner ACKed the entire preparation/capture/environment/maps/freeze/drain interval. First attempt failed before any owned launches because sandbox denied `/bin/ps`; driver exit 1, zero timing credit. Owner explicitly RELEASED that failed phase. A new full-phase HOLD was ACKed before retry; approved narrow escalation ran the unchanged safe observer. Five actual retry launches all exited 0, groups absent, defaults before/after correct, full parent/Lake environment bytes compared only in memory. Retained environment evidence is hash/length plus the approved nonsecret PATH/LEAN/toolchain allowlist; process observations retain only task-owned PID/start/executable/arguments. Owner explicitly RELEASED after actual COMPLETE and before any raw parse. No unrelated command arguments/full environment persisted.

Actual command: `lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/roth-main-monic-root/final-profile/FinalPrefix.lean`. Exact final imports/preceding commands/target bytes plus namespace close and actual-family/full TYPE/VALUE/default/width-100 observations are bound by `prefix-binding.json`. Canonical whole emitted doc/signature/body payload matches production target; full TYPE/universes match production observations. Module-context proof VALUE identity is not demanded or claimed.

| Disjoint root | ms |
|---|---:|
| outer command | 21.972 |
| async proof elaboration | 80.980 |
| kernel parent | 7.764 |
| async lint | 6.025 |
| compiler / lazy prior DATA roots | 0 / 0 |
| total | 116.741 |

Nested kernel 7.719 ms is already included in its parent and not added again. Actual fresh target family is root only; all roots succeeded; canonical/family/kernel/compiler associations verified. Total <1000 ms and <750 ms, so no unchanged repeat capture. Historical genuine-original indexed same-target row: 310.152 ms, separately scoped to original Main context; not an entry-source baseline, no controlled speedup ratio/causal claim. Its source canonical matches original target exactly. `target-profile-acceptance.json` retains roots/offsets/hashes and binding; no broad historical raw-profile scan/copy performed. Limit raises removed/added: 0/0. Deferrals: none for this target.

## Result and handoff
Before: 11 code lines; after: 6; saved: 5. Rules materially applied: strategy/hypothesis strengthening; 1.17 dot notation; 2.3 degree simpa→simp; 3.3 removes omega by eliminating cases. Renames queued: none. Comments preserved: no inline proof comments originally; source quotation exact. Refactoring needed: none for target; later whole-file independent simplify review and mandatory full-source profile remain owner/file-final work, not credited as completed here.

Phase checklist:
- [✓] Step 1: required skills/workflows/references read.
- [✓] Step 2: all 24 audit items recorded.
- [✓] Step 2.5: five-method mathlib search and actual exact?/apply? probe.
- [✓] Step 2.6: every parameter classified, constructive hα drop and hint-drop result recorded; literature status.
- [✓] Step 2.7: complete codepoint width table + actual width-100 check.
- [✓] Step 2.8: complete inequality occurrence scan.
- [✓] Step 3: all 42 golfing slots have concrete status.
- [✓] Step 4: strategy reflection and independent square-witness proof.
- [✓] Step 5a: complete final-source LSP, zero errors; existing warnings disclosed.
- [✓] Step 5b: actual source/build/native/semantic/profile gates pass with doc-only build qualification.
- [✓] Step 6a: no necessary rename, shared queue untouched.
- [✓] Step 6b: report, scoped diff, final drain and lease release.

Final drain: all 15 recorded launch groups absent, all launch/terminal records present; native/semantic/capture drivers and all LSP queries terminal, no pending calls. Compiler/native/LSP/profile leases released. Owner review/exact-path commit/push required before any next target edit; worker makes no next-target edit or Git write.

Final Main SHA256: `6c0515414938241c00257dc0c0604d0d7900e69b0b56351644b1dc633a3bb95b`.
