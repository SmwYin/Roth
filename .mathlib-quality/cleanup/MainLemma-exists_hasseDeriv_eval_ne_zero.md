# Result: `Roth.exists_hasseDeriv_eval_ne_zero` — original25 FULL Mode B

Generalized the variable domain from `Fin m` to arbitrary universe-polymorphic `σ` with `[Fintype σ]`, retaining real coefficients and natural weights from the actual Index API. The proof maps the existing attained-index witness directly with `Exists.imp`. No caller edit, new import, declaration rename or meaningful helper was required. The original `Fin m` contract is recovered exactly by specialization. This is the original25 declaration result; whole-file review and global performance acceptance remain the owner's later work.

Before: 2 proof lines. After: 1 proof line. Saved: 1 proof line. File: 692→694 lines (net +2, due to useful public doc guidance). Audit issues found: 3 (finite-domain specialization, unpacked signature break, optional direct witness mapping); fixed: 3. A concrete new unused-lambda-binder warning in v1 was repaired with `_` in v2. Refactoring deferred for this declaration: none. New meaningful helpers: 0; no helper lifecycle bypass. Existing five independently audited helpers and seven signposts are protected byte for byte by exact target/doc inverse.

Rules applied: 1.13, 1.17, 2.14 (direct term reflection). Gates: PASS for original25 within the granted declaration scope; no whole-file/global performance PASS claim. Renames-queued: none. Comments-preserved: exact entire original Source quotation, including line breaks and closing punctuation; no inline target proof comments existed, none removed. Refactoring needed: none for original25.

## Provenance and scope

Entry SHA256 `cb59bb4129cbf7e353b272f05615b0cfd2193c67177b82100590c3fa84afd056`; final SHA256 `2a8aa8abb74ff479e0dae3b2885a89e8a2bc8471e2a6a8950f284d94460074ac`. `source-audit25.json` verifies replacing only the final target/doc with the entry block restores all 692 entry lines byte for byte. All other 16 source/config pins are unchanged, including Main SHA256 `5f384557dccacaec469699cc7d32bd5666c9d525267e00433b7ae401fee98d09`. Source/proof/doc from original24, its explicit-K hΘ bridge, all prior callers, helpers and signposts remain unchanged. No Git, central ledger/queue/learnings edit or child agent was used.

Full installed lean4/mathlib-quality skills, cleanup/cleanup-all/buzz commands, all mandatory references and all 854+112+46 owner instruction lines were read, with every initial truncation recovered. `reference-inputs25.json` preserves 39 hashed inputs and exact copies, including the local source text `clean.tex:1526–1537` and actual pinned `Exists.imp` definition. `before25-source/`, phase sources, `launched-inputs/<SHA>/`, exact CLI receipts and separate raw stdout/stderr preserve every actual launched variant, including failed attempts. Failed or v1 runs are historical, never relabeled as v2 evidence.

## Complete 24-item final audit

1. LINT: full actual unfiltered native ML final v2 succeeds, nonpartial, nontimeout, no failed dependencies or errors; only existing header warning at line1, outside target. Main has existing header/unused hδ/hQ/hc warnings; Eval none.
2. HAVE SCAN: none. Final term maps the attained-index witness and uses both returned facts.
3. SET_OPTION: no target resource or diagnostic overrides; actual imported limits200000/20000/512.
4. SIMP SQUEEZE: none in target.
5. NAMING: exists describes existential conclusion, hasseDeriv references the actual operation, eval names evaluation, ne_zero gives nonvanishing. No forbidden abbreviation, numbering, single-letter declaration, _gt_ or _ge_. No rename recommended.
6. LINE PACKING: separate packing25-before.json measures every signature line. Original second break68+1+17=86 needed repacking. Final generalized signature is packed; all three actual rows and next indivisible units are below.
7. BY PLACEMENT: Direct term proof; no by wrapper remains.
8. FORMAT: two-space term indentation, no internal blank line, one tactic per line, no haveI/letI or sequential rw.
9. COMMENTS: no inline target proof comments. Preserve exact existing Source quotation, including all newlines and closing punctuation; all caller signposts and prior audited context remain unchanged.
10. DOCSTRING: present. Retain exact Source paragraph. Added application guidance, arbitrary finite variable type and zero weight allowance; no tactic narration.
11. VISIBILITY: retain public mathematical API used by main_lemma and useful for selecting a nonvanishing derivative below a cutoff.
12. STRUCTURE: one-line ordinary proof is below30; no branches. Existential witness has a conjunction tying its weight and evaluation together; splitting it would lose the common witness and does not produce independent conclusions. No meaningful helper warranted.
13. MATHLIB: all five actual searches and compiled generic routes completed below. Existing project exists_weight_eq_index is the exact attained-minimum building block; current target adds a strict-cutoff extraction. No claim of mathematical absence from text searches.
14. JUNK DEF: n/a, theorem.
15. EXISTS LEMMA: public cutoff API, not a private trivial witness lemma; no literal witness is constructed independently of the input polynomial.
16. SHOW vs CHANGE: none.
17. PUSH_NEG: none.
18. GENERALISE: implemented Fin m→universe-polymorphic σ with Fintype; compiled drop/weakening attempts and full remaining-premise counters below audit hP, strict hc and every outer/inner binder. Coefficient/weight domains follow actual Index API, no independent redesign. Full remaining-premise counters compiled; proof-body failure alone is not treated as necessity.
19. INEQUALITY: signature contains two occurrences of <, each with smaller quantity on left, and no ≥/>. No orientation rename.
20. NORMAL-FORM: standard existential multi-index, weight bound and nonzero evaluation; arbitrary finite variable type aligns with adjacent Index API.
21. SYNTAX-GEN: keep explicit hP, α, r, hc order so existing callers remain inferable. An optional iff/converse adds no evidenced downstream use and is not recommended.
22. IMPORT-FANOUT: no imports added; exact all-context inverse restores entry bytes.
23. CASTS: target contains no explicit numeric coercion or term ascription to remove. MvPolynomial σ ℝ and function codomains are necessary type declarations.
24. INSTANCE-NAME: target declares no named instance. No global classical equality instance is introduced.


## Step 2.5 — all five actual search methods

1. Lean-Finder actual nonzero/Hasse/index cutoff query returned `MvPolynomial.nonTorsionWeight_of`, `MvPolynomial.IsWeightedHomogeneous`, `MvPowerSeries.weightedHomogeneousComponent_of_weightedOrder`: related domains/statements, not this cutoff result.
2. Loogle actual `sInf ?s < ?c` query returned `csInf_lt_iff`, `exists_lt_of_csInf_lt` and complete-order results: generic building blocks needing translation of the custom index.
3. LeanSearch actual finite-minimum cutoff query returned `Finset.inf'_lt_iff` and minimum facts: partial matches requiring support/index translation.
4. Actual complete local source searches, including auxiliary `_zero`, `_iff`, `_of` and generic csInf routes, are saved untruncated in `search25-source.json` with commands/raw stdout/stderr. Relevant Index/Hasse sources were read.
5. Native local name search returned `Roth.exists_weight_eq_index` but reported `index:error`; this is an index failure, never mathematical absence. Full source fallback and actual generic-route candidates supply bounded evidence.

Auxiliary variants assessed: `exists_weight_eq_index`, `index_le_weight`, `le_index_iff`, `csInf_lt_iff`, `exists_lt_of_csInf_lt`, `hasseDeriv_zero_apply`, `eq_zero_of_hasseDeriv_eq_zero`, `weightedHomogeneousComponent_of_weightedOrder`. No common-equivalents bucket directly matches. The existing project attained-index theorem is the useful reusable building block; retaining the one-line public strict-cutoff extractor is justified. No missing-API helper signal or downstream use for an extra iff/converse companion was found. The admitted partial successes of `apply?`/other search are rejected by actual opaque VALUE/std3 guards.

## Step 2.6a–e — every outer and inner binder

| Binder | Final audit and actual evidence |
|---|---|
| old `m : ℕ` / `Fin m` | Generalized to `σ : Type*`; old contract recovered exactly by specialization in full TYPE AST/isDefEq checks and `old_fin_use`. |
| `σ : Type*` | Arbitrary universe parameter retained; actual levels, all written BinderInfo/names/order and inner binders checked. |
| `[Fintype σ]` | Actual no-instance and `[Finite σ]` candidates failed elaboration of existing Index API; Fintype required for this API formulation, no claim that the mathematics intrinsically needs this representation. No DecidableEq added. |
| `P : MvPolynomial σ ℝ` | Value and dependent domain retained; coefficients fixed by actual index API, no independent Index redesign. |
| `hP : P ≠ 0` | Drop attempt rejected; full zero-polynomial certificate has remaining `index 0 < 1` but no nonvanishing derivative. Cannot infer hP from hc. |
| `α : σ → ℝ` | Arbitrary point retained; no global hypothesis to localize. Full arrow binder/codomain checked. |
| `r : σ → ℕ` | Arbitrary natural weights already include zero; no positivity premise invented. Empty/zero-weight use compiled. |
| `{c : ℝ}` | Arbitrary real cutoff; nonpositive cutoff impossibility certificate compiled. |
| `hc : index P α r < c` | Drop and ≤ weakening rejected with full remaining-premise countercertificates (negative c, or P=1 and c=index). Strict inequality remains. |
| inner existential `k : σ →₀ ℕ` | Domain generalized with σ, finite support and same common witness for both conjuncts preserved. Splitting conjunction loses the shared witness and is not an independent-results decomposition. |
| inner function/dependent binders | Every inner TYPE binder, universe and BinderInfo compared literally; all DATA originating-spine checks preserve actual opaque values. |

2.6b: actual `candidate25-general` and `candidate25-term` exit0 with actual closed TYPE/VALUE/std3/default guards; finite/no-Fintype/drop-hP/weak-hc/aesop/apply-search/exact-search/grind exit1 preserved. A body failure alone is not necessity evidence; the eight final property declarations provide full certificates and applications. 2.6c: domain widening was explicitly recommended before editing and authorized by the standing user instruction to implement recommended changes. 2.6d: three separate actual public literature queries follow. 2.6e: only the compiled generalization and direct mapping term remain applied; coefficient/weight redesign and redundant API were not warranted.

### Three actual public literature queries — ordered top three each

The exact query strings and full actual results are in `literature25-query1/2/3.json`. Titles/links below describe retrieved search results, not claims that every linked work was fully read. Primary fetch failures (74 MB Roth PDF, ACM 403) are preserved in `literature25-primary-read.json`. The actual optional math-chat capability search was empty (`math-chat25-capability.json`). Local primary exposition `clean.tex:1526–1537` was read and its full bytes saved/hashed. It explicitly selects a derivative below the index cutoff; no claim that literature misses prove absence.

| Query | Top 1 | Top 2 | Top 3 |
|---|---|---|---|
| weighted index polynomial nonvanishing Hasse derivative generalization | [Mathlib.Data.Polynomial.HasseDeriv](https://math.iisc.ac.in/~gadgil/proofs-and-programs-2023/doc/Mathlib/Data/Polynomial/HasseDeriv.html) | [Hasse derivative](https://en.wikipedia.org/wiki/Hasse_derivative) | [Mathlib.Algebra.Polynomial.HasseDeriv](https://firsching.ch/FormalBook/docs/Mathlib/Algebra/Polynomial/HasseDeriv.html) |
| multivariate Hasse derivatives Taylor expansion arbitrary commutative ring | [Formal multidimensional Taylor series](https://mathoverflow.net/questions/288218/formal-multidimensional-taylor-series-expansion-over-commutative-rings) | [same question, actual second indexed result](https://mathoverflow.net/questions/288218/formal-multidimensional-taylor-series-expansion-over-commutative-rings?r=31) | [Points on lines in F3](https://math.mit.edu/documents/spur/2013NieWang.pdf) |
| Roth polynomial index weighted order vanishing derivative Lemma 9 | Baker/Wüstholz, Logarithmic Forms and Diophantine Geometry (nzdr.ru PDF; exact long URL in query3 raw) | [Chapter 4, Rational](https://www.ams.org/bookstore/pspdf/mbk-48-prev.pdf) | [K. F. Roth, ICM 1958](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf) |

### Step 2.7 — all signature lines, codepoints

| Signature row | Current | Next indivisible unit | Next width | Current+1+next | Action |
|---|---:|---|---:|---:|---|
| theorem/binders | 98 | `(α : σ → ℝ)` | 11 | 110 | ok |
| point/weights/cutoff/existential | 74 | entire predicate `weight r k < c ∧ eval α (hasseDeriv k P) ≠ 0 :=` | 47 | 122 | ok |
| predicate including indent and `:=` | 51 | final signature row | — | — | ok |

### Step 2.8 — inequality orientation

| Occurrence | Action |
|---|---|
| `index P α r < c` | smaller quantity left; retain |
| `weight r k < c` | smaller quantity left; retain |
| `≥` or `>` | zero target occurrences; no name rewrite |

## All42 golfing rules

| Rule | Actual assessment/action |
|---|---|
|1.1 by exact wrapper|n/a: original proof has obtain and exact, no wrapper. Direct term form independently compiled.|
|1.2 by rfl|n/a: no reflexivity proof.|
|1.3 rw+exact|n/a: no rw.|
|1.4 simp+exact|n/a: no simp.|
|1.5 trailing rfl|n/a: no rfl.|
|1.6 constructor chain|n/a: already anonymous witness/conjunction.|
|1.7 apply+exact|n/a: no apply.|
|1.8 by_contra/push_neg|n/a: no contradiction.|
|1.9 eta reduction|n/a: no eta lambda in original; selected anonymous lambda destructures returned conjunction.|
|1.10 single-use have|n/a: no have.|
|1.11 apply+intro|n/a: neither occurs.|
|1.12 redundant show|n/a: no show.|
|1.13 obtain|original already destructures existential; selected term maps it directly with Exists.imp.|
|1.14 merge rw|n/a: no rw.|
|1.15 terminal simp only|n/a: none.|
|1.16 nonterminal simp|n/a: none.|
|1.17 dot notation|term candidate compiled with `(exists_weight_eq_index hP α r).imp`.|
|1.18 trailing parens|n/a: only grouping fixes the receiver of `.imp`.|
|1.19 push Not|n/a: no push_neg.|
|1.20 private trivial existential|n/a: public input-dependent cutoff API.|
|2.1 grind whole proof|actual hinted whole-proof attempt rejected unusable theorem pattern and actual VALUE guard; no admitted result accepted.|
|2.2 before grind|n/a: original has no grind.|
|2.3 simpa consolidation|n/a: no simp/closing chain.|
|2.4 fun_prop|n/a: existential algebraic goal has no function regularity property.|
|2.5 positivity|n/a: joint existential conclusion is not a standalone positivity goal; its nonvanishing depends on polynomial input.|
|2.6 gcongr|n/a: no monotonicity argument.|
|2.7 lia/omega|n/a: no Nat/Int arithmetic proof goal.|
|2.8 aesop|actual whole-proof attempt failed unsolved goal/rule-depth; no limit raise.|
|2.9 norm_num/norm_cast|n/a: no numeric/cast calculation.|
|2.10 decide|n/a: unbounded multi-index existential is not finite decidable computation.|
|2.11 field_simp/ring|n/a: no field identity to prove.|
|2.12 linear_combination|n/a: no ring/ring_nf endpoint.|
|2.13 wlog|n/a: no symmetric cases.|
|2.14 calc term|n/a: no calc; actual direct term alternative compiled.|
|2.15 parallel goals|n/a: original closes one witness construction, no repeated branches.|
|3.1 erw→rw|n/a: no erw.|
|3.2 legacy regularity|n/a: no continuity/measurability tactics.|
|3.3 omega→lia|n/a: no omega.|
|3.4 rfl substitution|n/a: no rcases rfl.|
|3.5 automation attributes|n/a: existential cutoff selection is not a canonical simplification or function-property rule.|
|3.6 simp_all|n/a: none.|
|3.7 limits|none present; all actual candidate guards assert200000/20000/512 and no internal reset.|

Step4 reflection: the mathematical operation is mapping the attained-index witness to the strict-cutoff witness. The direct Exists.imp term expresses that operation in one line and compiled without new API, helper, axiom or resource override. Whole automation alternatives failed and are preserved. Manual simplify review selects this direct term and the domain generalization; an independent entire-file simplify reviewer remains the owner's mandatory later task. No independent review is claimed here.


## Fresh final semantic, contract, property and consumer gates

`final25-v2-independent` reconstructs the ENTIRE genuine original, entry and selected namespace bodies in fresh namespaces, with byte-exact recovery and original25 plus whole actual direct-caller main_lemma mathematical proofs. Genuine original input SHA256 `a3d09825fb878c5d512cfdd3feca517465e0a8215807b1261b988f664915f3a8`; final fixture SHA256 `e2c0387d6c2e51ab400698c91ec1cf04728e718513427d33097778ea141d5891`. All 28 exact contracts, 70 closed TYPE/actual opaque VALUE/inferredTYPE/std3 checks, four prevalidated literal pairs, DATA values and all written outer/inner binder/universe AST comparisons pass. Actual defaults are 200000/20000/512; no internal reset or option raise. DATA normalization is restricted to named DATA and originating-spine beta with independently prevalidated literal TYPE/VALUE/binder pairs; no arbitrary proof unfolding/NameMap/proofirrelevance.

The six full nonself TYPE+actual opaque VALUE transitive closure counts are original target11494/main30373, entry target11494/main30464, selected target11495/main30465. Actual full private Lean.Name roots and descendants are denied with `root.isPrefixOf`; no current target/helper/DATA proof leaks into original proofs. The audited unchanged H5 clone also passes its16966 nonself closure. All proofs use only propext/Classical.choice/Quot.sound.

Fresh dynamic inventory: 32 written declarations +29 generated =61 actual retained declarations, crossmatched exactly between independent replay and fresh retained elaboration. Thirty-six actual deny roots include the four support roots. `final25-v2-retained` validates each actual declaration in a separate ordinary command at default limits, full TYPE+opaque VALUE/inferredTYPE/std3; every generated kind/name/levels/full TYPE/VALUE AST and source absence printed. The generated `Roth.exists_hasseDeriv_eval_ne_zero.match_1_1` is an actual compiler definition, not a new meaningful source helper or added cleanup-count item. No hard-coded generated suffix cap or expected count substitutes for fresh discovery.

`final25-v2-properties` passes eight actual closed TYPE/VALUE/std3/default-guarded declarations: hP necessity with all remaining premises; strict cutoff necessity at c=index with nonzero P; nonpositive cutoff; empty variable type/zero weights; dropped hc negative cutoff counter; generic σ application; empty API application; exact oldFin application. `final25-v2-consumer-inventory` scans actual environment TYPE+opaque VALUE, validating entire current target/caller values before printing hashes/constants/full TYPE; the sole direct consumer is `Roth.main_lemma`. Complete source/reference/LSP evidence agrees; its source did not need repair.

| New identifier | Actual verification | Result |
|---|---|---|
| `Exists.imp` / `.imp` | Pinned core Init/PropLemmas.lean:257, saved exact source; successful actual candidate, full builds and closed selected opaque VALUE | pass |
| `Fintype`/universe-polymorphic domain | Actual existing Index API, full selected TYPE/binder/universe check and builds | pass |

## Actual builds and unfiltered native diagnostics

Baseline actual `--deps`, affected/full/separateEval builds and ML/Main/Eval native all passed before editing; baseline17pins and104 project companions were saved. Final commands run in order with explicit frozen parent and actual raw Lake environment before/after, all17pins immutable, launched bytes exact, each process group drained:

| Final actual command/run | Exit | Wall seconds |
|---|---:|---:|
| `/Users/ramin/.elan/bin/lake build Roth.MainLemma Roth.Main` (final25-v2-affected) | 0 | 89.329 |
| `/Users/ramin/.elan/bin/lake build` (final25-v2-full) | 0 | 40.875 |
| `/Users/ramin/.elan/bin/lake build Roth.LeanEval` (final25-v2-Eval-build) | 0 | 42.092 |
| `/Users/ramin/.elan/bin/lake env lean -j1 /private/tmp/roth-mainlemma-exists-deriv-ne-zero/final25-independent.lean` (final25-v2-independent) | 0 | 241.712 |
| `/Users/ramin/.elan/bin/lake env lean -j1 /private/tmp/roth-mainlemma-exists-deriv-ne-zero/all-retained25-v2.lean` (final25-v2-retained) | 0 | 69.143 |
| `/Users/ramin/.elan/bin/lake env lean -j1 /private/tmp/roth-mainlemma-exists-deriv-ne-zero/properties25-final.lean` (final25-v2-properties) | 0 | 35.703 |
| `/Users/ramin/.elan/bin/lake env lean -j1 /private/tmp/roth-mainlemma-exists-deriv-ne-zero/inventory25-final.lean` (final25-v2-consumer-inventory) | 0 | 114.738 |

Final native `mcp__lean_lsp__lean_diagnostic_messages` used complete file_path +timeout_s120 only; no severity/declaration/range filter. Each full raw response and contemporaneous start, tool-return, response-save observations precede postpins; actual file bytes saved bySHA. All three return success=true, partial=false, timed_out=false, failed_dependencies=[], zero errors. MainLemma has only pre-existing unknown copyright header warning at1; Main has that warning plus pre-existing unused hδ333/hQ474/hc475; Eval has no warnings. No invented copyright metadata or linter suppression. V1's new unused d warning was fixed in final source and its v1 evidence remains historical.

## Actual matched scoped performance and environment closure

Only standalone trace.profiler options are added to exact entire canonical target and entire actual direct consumer, including all docs/types/bodies/order/Classical wrapper. Stripping only those option lines exactly recovers canonical bytes. Actual CLI for all four captures: `/Users/ramin/.elan/bin/lake env lean -j1 --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 FILE`. Full printed command payloads match canonical tokens with layout/standalone-line-comment omission only; no formatting exception was used. Column-zero disjoint Elab.command/async roots include actual proof/kernel/lint/compiler once; every internal Meta root (including0) is excluded. Exact fresh generated Name/kernel/compiler siblings and source absence are crossmatched, no forced old root count. Final target has6 roots; main9. The before pair remains the actual original25 entry pair; no after-v1 capture was launched and no third unchanged sample was cherry-picked.

| Group | BEFORE 1 | BEFORE repeat | AFTER 1 | AFTER repeat | Result |
|---|---:|---:|---:|---:|---|
| target | 19.220 ms | 19.031 ms | 32.566 ms | 29.031 ms | PASS below1000 in both final captures |
| actual direct consumer main_lemma | 5023.870 ms | 4885.906 ms | 5175.935 ms | 5047.346 ms | existing foreign failure retained for original27/global work |

Whole consumer mean4954.888→5111.6405ms, +156.7525ms (+3.1636%). Actual exact changed obtain-call samples9.317/9.647→9.390/9.402ms (mean9.482→9.396, -0.086ms); preceding hsX900.833→937.593 (+36.760ms), hΘ139.518→143.171 (+3.653ms). `profile25-v2-call-diagnosis.json` binds complete actual printed tactic payloads/lines/top direct costs. Inclusive child times are diagnostic only, never added to disjoint totals. These data do not establish causality or justify dismissing the whole-caller increase as noise. The target remains far below its own limit; no unrelated main_lemma repair is introduced during original25. Existing global delta/public19/main failures remain unresolved, no global or whole-file performance PASS claimed.

Frozen observed parent SHA256 `3d16685726f44ba55b7ebdbac4c29181048c0216b6e16fa03281279a77e50c89`; every final run's actual raw Lake before/after SHA256 `f224321b28ac30fabd6271c2f5678c71ed115f96cfadd1b603a198b6520e8d77`. All four actual Lean/Lake/Elan proxy binaries, resolved paths/PATH, configs and package/core catalogs are hashed independently. End availability union24793 artifacts/3929058144B versus before3929053440B; project-cache intersection11, strict external24782/3918200888B exactly unchanged. Pinned core compiled superset12592/2125623224B;104 project cache companions frozen again after all profiles. This is setup/package availability plus core superset, not an exact runtime-loaded closure. `closure25-v2-comparison.json` verifies strict external and binaries unchanged, only target source pin changed, final cache hashes stable.

## Failure history and review limits

All failed candidates, raw streams, initial unlaunched argv error, initial admitted automation rejection, manually stopped full-repr inventory (actual exit-15, drained), tooling/PATH/serialization and permission-error history remain preserved. No approval rejection or active abandoned compiler is hidden. Historical inherited-environment v1 correctness was followed by an explicit observed-frozen replay; neither is accepted as final v2 credit. Final v2 semantic/build/property/consumer runs all freshly use frozen-general wrapper. V1 source425972.../native unused d warning is preserved in explicit v1 copies; final source differs only by lambda d→_. The old profile parser honestly rejected actual `Lean.compileDecls`; v5 includes the disjoint compiler root and binds its exact fresh generated name rather than deleting it. The initial diagnostic h32prime lookup failed because that inherited prospect is absent from canonical source; corrected diagnosis uses actual written hsX/hΘ and preserves this failure. No unchanged third profile capture or cherry-picked substitute.

Manual simplify/step-back reflection completed above; no built-in simplify tool is exposed. A NEW fresh independent whole-file simplify reviewer after original27 remains mandatory owner work, as do final global all-row performance, cumulative contracts/Main checks and publication. This declaration report does not claim the file or project cleanup complete.

## Gate status — original25 declaration scope

| Gate | Result | Actual evidence |
|---|---|---|
| lake_build_file | PASS | actual final v2 `lake build Roth.MainLemma Roth.Main`, exit0 |
| definition_protected | PASS | no def/abbrev change; exact target/doc inverse restores entire entry |
| theorem_statement_protected | PASS, authorized GENERALISE | declared finite-domain widening; exact oldFin contract recovery and full literal TYPE checks |
| structure_gate | PASS | ordinary target1≤30 proof lines, no branch>10; common-witness conjunction is not independent results |
| naming_gate | PASS | meaningful exists/hasseDeriv/eval/ne_zero, no forbidden scheme or _gt_/_ge_ |
| line_packing_gate | PASS | all three rows measured98/74/51, next indivisible totals110/122 |
| cumulative_no_unintended_breakage | PASS | full build then separateEval, sole current actual consumer plus full original/entry/selected whole-caller reconstruction, unfiltered ML/Main/Eval native |

Overall: PASS for original25 declaration scope. Additional inequality_orientation_gate PASS (two `<`, no `≥`/`>`); full `lake_build` PASS; docstring_only_changes n/a (FULL Mode B). Caller/global performance failure remains explicit separate owner work, not a hidden gate waiver.

## Required 6b phase checklist

- [✓] Step1 — all complete reference/instruction reads, hashes and copies.
- [✓] Step2 — all24 audit items above.
- [✓] Step2.5 — all five actual search methods and honest error fallback.
- [✓] Step2.6 — outer/inner a–e audit, compiled candidates/counters, three actual queries/top3.
- [✓] Step2.7 — every signature row/next indivisible table.
- [✓] Step2.8 — every inequality occurrence/orientation table.
- [✓] Step3 — all42 golfing rules individually assessed above.
- [✓] Step4 — manual simplify/step-back reflection, later fresh whole-file review disclosed.
- [✓] Step5a — final actual complete unfiltered native diagnostics, no new warning/error.
- [✓] Step5b — seven gate rows +Overall and inequality orientation above.
- [✓] Step6a — no rename warranted, no central sidecar mutation.

## Artifact integrity and seven-lease END

`manifest25.json` is the full scratch/report/source/config/reference/executable/actual compiled-input manifest, including every failed/v1/raw artifact with bytes/SHA256/streamed strict UTF8 status; only explained actual compiled/executable inputs may use binary exceptions, never binary logs/text. It explicitly excludes only itself, `manifest25-second-rehash.json` and `seal25.json` to resolve self-reference. An independent full streamed second rehash must match every path/hash/byte/UTF8 and exact coverage. The subsequent self-excluded seal freshly checks every actual owned run group absent and every native request completed AFTER the rehashes. Pre-seal actual receipts enumerate 39 wrapped runs and 15 completed native calls (`preseal25-counts.json`); all historical failures remain included. The resulting seal freshly rechecks these dynamic counts and records exact report/manifest/second-rehash hashes after all rehashes.

This report's END is effective only when `manifest25.py verify` has returned successfully and `seal25.json` records the final fresh absence/completion observations. At that point all SEVEN leases END/RELEASE: target source, doc, evidenced narrow callers, report/artifacts, compiler, native, profile. No child, compiler, native or profile remains active; no subsequent leaf mutation is authorized. Parent independently reviews and performs its own post-END gates/publication before original26. No Git publication by leaf.
