# Fresh helper10 cleanup — local review complete, closure receipt authoritative

Scope: private `exists_mem_RSet_le_index_aux` only; no accepted helper or public contract edits. Original helper is the genuine first ungolfed R4 artifact, SHA256 `9160c6534623a56dd1a3ef921edbdf7d533b53be9a6704b0f1524fb511d2e300`. Fresh scratch: `/private/tmp/roth-mainlemma-helper10-fresh1`. No completion/count/publication claim.

## Phase 0 — baseline

Actual full `lake build` exited 0, followed by separate `lake build Roth.LeanEval`, exit 0; both sessions fully drained. Logs `baseline-full-build-v1.log`, `baseline-eval-build-v1.log`. This establishes the transition from accepted helper9 compiled source734 to new source746. Optional cache fetch unnecessary; existing cache supplied imports. Full native MainLemma, file_path only, errors0, failed_dependencies[], partialfalse, timedoutfalse, inherited copyright warning1. Source17 observed before and after, raw return immediately timestamped and saved with hash/bytes. Author identity remains unknown; no header metadata invented.

## Phase 1 — preparation

Read full installed mathlib-quality and lean4 SKILL files, full cleanup.md (1847 lines), cleanup-all.md (488), buzz.md (279), and full golfing-rules, proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates, style-rules, naming-conventions, profiling, mathlib-review-stages references. Full target source read by contiguous ranges after an initial combined output truncation; no full-read credit claimed for truncated dumps. Dialect classic. Module has 37 declarations; this lifecycle's only new target is helper10 (L597), not a re-audit of nine accepted helpers.

Mathematics: the finite bounded remainder map yields one common pair of distinct box polynomials for every derivative in J. Subtracting gives one nonzero polynomial, coefficient bound B rather than 2B, and unchanged coordinate degrees. Its selected derivatives vanish at the root of f. Coverage of every box derivative of weight strictly below γ gives index at least γ. No dimension, degree positivity, δ, denominator, logarithmic or positivity premises are introduced. Empty variable types and zero degree bounds are permitted.

## Phase 2 — audit punch-list (before edits)

A.1 Copyright missing/inherited warning: protected metadata; no invented authors.
A.2 Module doc and all paper quotations present/protected.
A.3 Existing imports ordered, no new import proposed.
A.4 No contentless section headers.
A.5 746 lines, below file threshold.
A.6 No limit raises or debug options.
A.7 No λ/$/push_neg in helper.
B.1 Full native warning at L1 only, unrelated inherited header.
C.1 Private helper name describes existence/RSet/index, snake_case with literal RSet identifier and `_aux`; no forbidden abbreviation or number.
C.2 Private helper has no docstring, as required.
C.3 Body 11 code lines; no >10-line case branch. Existential conjunction preserves a single common witness; splitting into unrelated witnesses would weaken the intended contract.
C.4 Signature underpacking at J/γ→hC and hJ→existential; measure/repack before final gates.
C.5 hP is reused for nonzero, membership, degree bounds; retain. hmap0 is used once and can inline with existing map_ne_zero_iff API; attempt.
C.6 Terminal `simpa only` at count and degree transfer: attempt unsqueezing, retain squeezed only on measured performance grounds if needed.

## Phase 3 — file-level fixes

None in lease: imports/docs/author metadata and protected comments preserved. No file-wide edits authorized or needed.

## Phase 4 — 24-item audit

1. LINT: no helper-local warnings; inherited header warning remains documented.
2. HAVE: hP used in membership/nonzero/degree, retain. hmap0 single-use term, inline via map_ne_zero_iff candidate.
3. SET_OPTION: none.
4. SIMP: two terminal simpa only calls; unsqueeze candidate required.
5. NAMING: descriptive private `_aux`, no rename needed or queued.
6. PACKING: initial defects recorded above; final per-line measured table pending.
7. BY: `:= by` correctly on conclusion line.
8. FORMAT: 2-space proof, 4-space signature; no empty proof lines, no haveI/letI.
9. COMMENTS: literal `-- `W* = W' - W''`` retained at difference construction. All nine protected standalone comments remain literal.
10. DOCSTRING: n/a private helper; none added.
11. VISIBILITY: private, sole production caller main_lemma.
12. STRUCTURE: 11 code lines, retain one witness under conjunction; no meaningful new helper warranted.
13. MATHLIB: fresh five searches saved separately. Finder and LeanSearch return Nullstellensatz/finite-field partition and univariate derivative results; none matches selected integer remainder → project RSet/index statement. Loogle query returns rename existence, unrelated. Local name query finds target itself; index warming is qualified, not absence evidence. Direct source search saved untruncated. Full-name absence and generic compile probes pending.
14. JUNK DEF: n/a lemma, no data definition.
15. EXISTS LEMMA: substantive pigeonhole/index construction, not trivial witness/rfl wrapper.
16. SHOW/CHANGE: none.
17. PUSH_NEG: none.
18. GENERALISE: detailed per-parameter drop/weakening and counterchecks pending.
19. INEQUALITY: no reversed ≥/> in helper signature; strict count and weight cutoffs preserved.
20. NORMAL FORM: project RSet and index canonical predicates, direct mathlib injectivity API preferred.
21. SYNTAX GENERALITY: finite arbitrary σ, arbitrary selected J and real cutoff; no main-specific packaging.
22. IMPORT FANOUT: n/a no new imports.
23. CASTS: integer C and real B/count coercions cross types; explicit product type guides elaboration, will test redundant ascriptions.
24. INSTANCE NAME: no instance declaration; Fintype binder unnamed.

Failures preserved: native multi_attempt replaces one tactic line rather than the entire multiline proof, leaving a continuation; all returned suggestions/recovery sorry warnings rejected. Raw `automation-initial-contaminated-raw-v1.json`. Isolated whole-declaration probes replace this evidence. First runner invocation put options after argparse REMAINDER label and failed before launching compiler; corrected invocation uses options before label, no proof credit for failed wrapper.

### Golfing rules — all 42 slots

| Rule | Status |
|---|---|
| 1.1 by exact wrapper | n/a: proof requires witness selection, no wrapper. |
| 1.2 by rfl | n/a: no reflexivity wrapper. |
| 1.3 rw+exact | n/a: none in target. |
| 1.4 simp+exact | Count conversion already terminal simpa. |
| 1.5 trailing rfl | n/a: absent. |
| 1.6 constructor packing | Existing existential tuple retained, one shared P. |
| 1.7 apply+exact | n/a: no such chain. |
| 1.8 by_contra! | n/a: no contradiction chain. |
| 1.9 eta | d/hd/hw coverage lambda uses each argument essentially. |
| 1.10 inline have | hP used 3 times retained; hmap0 inlined via map_ne_zero_iff in candidate. |
| 1.11 refine+fun | n/a: no apply/intro chain. |
| 1.12 redundant show | n/a: absent. |
| 1.13 obtain fields | hP's membership/nonzero/degree projections are direct repeated uses, not redundant extraction. |
| 1.14 merge rw | n/a: no rw chain. |
| 1.15 terminal simp unsqueeze | Count conversion unsqueezed successfully in candidate source-v2. Degree conversion unsqueeze FAILED: simp distributes map_sub, so degrees_map_of_injective no longer matches; retain exact intended rewrite set. Raw candidate-source-v1.log. |
| 1.16 nonterminal simp | n/a: no bare nonterminal simp. |
| 1.17 dot notation | `.2 hP.1` canonical iff application; no further opportunity. |
| 1.18 <| | n/a: existing application grouping needed to distinguish next argument. |
| 1.19 push Not | n/a: no push_neg. |
| 1.20 trivial existential | n/a: mathematical construction is nontrivial, not rfl witnesses. |
| 2.1 grind | Isolated full proof failed with open contradiction goal. |
| 2.2 remove before grind | n/a: no selected grind. |
| 2.3 simpa consolidation | Count conversion terminal; no extra closing tactic. |
| 2.4 fun_prop | n/a: no continuity/measurability/differentiability property. |
| 2.5 positivity | n/a: no positivity subgoal; nonzero polynomial needs injectivity. |
| 2.6 gcongr | n/a: index proof is derivative vanishing, not monotonic arithmetic. |
| 2.7 lia/omega | n/a: no Nat/Int arithmetic goal in helper body. |
| 2.8 aesop | Isolated full proof failed, unsolved existential. |
| 2.9 norm_num/norm_cast | n/a: no concrete numeral or standalone cast goal. |
| 2.10 decide | n/a: existential over infinite integer polynomial type not finite decidable computation. |
| 2.11 field_simp/ring | n/a: no denominator/ring identity. |
| 2.12 linear_combination | n/a: no ring/ring_nf ending or polynomial equality certificate. |
| 2.13 wlog | n/a: no symmetric branches. |
| 2.14 calc composition | n/a: no calc. |
| 2.15 <;> | n/a: no similar repeated proof goals. |
| 3.1 erw→rw | n/a: no erw. |
| 3.2 fun_prop | n/a: no legacy continuity tactic. |
| 3.3 omega→lia | n/a: neither present. |
| 3.4 rcases rfl | n/a: no rfl destructuring. |
| 3.5 automation attributes | No new global attributes: private existential constructor is neither simp normal form nor a generally applicable search rule. |
| 3.6 simp_all | Whole-proof simp made no progress; hypotheses encode a genuine existence/counting argument. |
| 3.7 limits | None to remove; none added. |

Whole-proof `exact?` failed; `apply?` exited 0 but supplied only partial suggestions and emitted declaration-uses-sorry. It is explicitly rejected, not a proof success. All isolated logs and terminal/source/environment/drain receipts retained. No absence conclusion is based on `apply?` exit code alone.

### Step-back reflection (first pass)

The mathematical strategy is already the short path: count → common pair → difference → vanishing → index. Integer coefficient intervals, rather than symmetric absolute-value intervals, explain why the difference bound is B. Splitting membership/index existential facts would obscure the common witness and produce unnecessary API. The nonzero transport now uses the same canonical injectivity criterion as adjacent accepted code. Arbitrary finite variable type/J/cutoff are already independent of the numerical main-lemma package. No duplicate proof skeleton warrants a new meaningful helper. A later whole-helper holistic reflection follows verified candidate selection; whole-file independent review remains owner work.

### Generalisation status — parameter inventory

| Parameter | Class / mathematical role | Drop / weakening candidates | Status |
|---|---|---|---|
| σ | type variable | Drop; universe lift | Drop probe prepared; already Type* (u_1), no imposed universe ceiling. |
| Fintype σ | typeclass | Drop; Finite σ | Both probes prepared; product, index and weight need the chosen finite instance in their types. Finite needs an explicit local choice and restatement, not a parameter deletion. |
| f | structure value | Drop | Degree/modulus/root references tie f to the integer remainder map; drop probe prepared. |
| α | structure value | Drop | Evaluation point and root hypothesis require α; drop probe prepared. |
| hf | proposition | Drop; weaken to nonzero | Direct drop probe and concrete f=0 negative prepared. Monicity makes coefficients below natDegree a complete remainder encoding. Nonzero alone does not supply that argument. |
| hfα | proposition | Drop; point-localise | Root condition already at exactly α, no global hypothesis; direct drop probe prepared. Without it, vanishing modulo f does not imply vanishing at α. |
| r | structure value | Drop; allow zero weights | Drop probe prepared; zero weights already allowed, no extra positivity retained. |
| B | structure value | Drop; allow zero | Drop probe prepared; zero already allowed, count then determines feasibility. |
| C | structure value | Drop; real/integer bound | Coefficient bound and tuple-cardinality C encode finite integer intervals. Replacing by real C would add floor conversion and restate count, not weaken the same arithmetic statement. |
| J | structure value | Drop; arbitrary selected family | Drop probe prepared; already arbitrary Finset, not exact prescribed filter or all derivatives. |
| γ | structure value | Drop; sign assumptions | Drop probe prepared; no sign assumptions to remove. |
| hC | proposition | Drop; localise W/J/i | Drop probe and concrete no-bound negative prepared. Already restricted to W in box, j in J, and i below natDegree; no unnecessary bound on higher coefficients. |
| hcount | proposition | Drop; strict→weak | Drop probe plus B=0 weak-boundary negative prepared. Strictness is essential for two distinct objects. |
| hJ | proposition | Drop; localise d | Drop probe and J-empty negative prepared. Already restricted to box and weight<γ; no check at equality needed. |

No typeclass parent relation below Fintype supplies the same chosen-instance product/index expression. No decidable equality premise appears. ℤ is essential to the finite interval cardinality and bounded difference; ℝ supplies the existing project weight/index interface. Replacing those concrete codomains would be new mathematics/API rather than dropping an unused operation. The inversion diagnostic has no fixed object to unfold away: all polynomial/box/derivative arguments are arbitrary inputs and remain mathematically used. Private declaration: literature search n/a per scope; local §6 source passage L1501–1521 was inspected verbatim. It confirms one common pair, difference coefficients bounded by B, and vanishing low-weight derivatives, which match the Lean stages exactly.

Candidate verification limitation: the first generic metadata command used hasValue without allowOpaque and therefore captured only 7 data/generated rows, not theorems. Corrected allowOpaque=true then hit cumulative default heartbeat200000 while checking multiple declarations. Neither is credited as a complete retained audit. The repair uses separate commands per actual inventoried declaration so each keeps the unchanged standard default budget.

### Retained declaration guards and exact contract comparison

`before-perdecl-v1` and `candidate-perdecl-v1` both completed exit0, fully drained, source17 immutable and frozen environment equal. Actual inventory is 65 local declarations, including private helpers, generated declarations, and data. Every actual opaque VALUE and full TYPE was checked closed, inferred TYPE equal, standard axioms only and unchanged default limits 200000/20000/512. Raw TYPE and universe representations are identical for all 65, preserving written binder names/order/BinderInfo. All 65 actual VALUE representations are identical except the target helper's VALUE. No generated-binder normalization was needed for this comparison. Independent proof is separately reconstructed via le_index_iff, explicit inside/outside-box cases and derivative vanishing, rather than calling target or its index-criterion wrapper; its value differs. A compiled comparator allows only BOTH-generated binder macro scopes to differ; all written names and dependent types remain exact.

Selected source: 742 lines, SHA256 `f0c8c658446a5bbccb4cbd5540332333d79dd8c3a483c5a8b660d25250d2aafc`. Exact source outside target unchanged; substituting the entry helper back recovers source746 SHA5fac8481 exactly. Main remains 101 proof lines and FAILS headline15; its independent original27 performance repair is not credited by this helper lifecycle. Main.lean stays protected689.

Sequencing erratum: the first suspicion named independent-perdecl-v1 as active at the source mutation. Actual terminal/source-pin receipts show it had already ended at1792700164.312852 with exit0, immutable5fac→5fac, fully drained. The active run was counterchecks-v3 (1792700166.622613→1792700192.690395), whose source pins changed5fac→f0c8 and whose proof also had an unsolved diag0 goal. It receives NO acceptance credit. Initial mistaken suspicion retained in `selection-source-mutation-qualified-v1.json`; exact correction in `selection-source-mutation-chronology-erratum-v1.json`. Fixed-source independent recovery and repaired counterchecks are separate fresh runs; no old receipt rewritten.

An intermediate observer attempted to parse a still-growing metadata JSON line and got an unterminated-string error. This was an observer error, not Lean proof success/failure; no partial raw row was accepted. Later completed65-row parse succeeded. Initial syntactic parameter-deletion probes are qualified because deleting binders may resolve/infer identifiers rather than remove the mathematical premise. Explicit post-signature clear-drop probes were prepared to verify the actual dependency without silently reinserting an implicit binder.

### Phase 5a — non-rename refactoring

No new declaration, wrapper, optional API, imported abstraction, or meaningful subhelper introduced. Existing map_ne_zero_iff replaces the hand-written injectivity transport. No other source edits or cross-file refactors.

### Phase 5b — rename pass

Local target queue empty; no rename applied/queued. Central queue untouched under sole-owner rule. The five global project rename proposals are explicitly excluded by standing instruction.

### Completed drop/counter/nonself checks

Post-signature clear-drop compile produced exactly14 failures, one for every parameter (including individually B and C and the named Fintype instance): σ/instance/f/α/r/B/C/J/γ cannot clear because later hypotheses or goal depend on them; clearing hf/hfα/hC/hcount/hJ causes explicit unknown-identifier errors at their proof uses. This checks actual context dependency and does not mistake implicit reinsertion for successful weakening. The separate Finite/nonzero-divisor/weak-count structural alternatives failed; earlier synthetic deletion probes remain qualified as described above. No premise was silently dropped.

Formal degenerate certificates `counterchecks-v4` compiled exit0, source17 immutable and drained. `no_conclusion B` proves that zero weights force index0 for every nonzero mapped polynomial, contradicting cutoff1. The certificate datasets satisfy all relevant retained premises for: dropping monicity (f0,r0,B1,C0,J{0}); dropping remainder bounds (fX,r0,B1,C0,J{0}); dropping J coverage (fX,r0,B1,C0,Jempty); weakening strict count to ≤ (fX,r0,B0,C0,J{0}, equality1=1). This supports retaining the actual mathematical assumptions, rather than merely observing their names in the body. No positivity on degrees, B, γ, or nonempty variables was added.

Fixed-source independent proof/actual VALUE/std3/defaults and compiled strict TYPE comparison passed in `fixed-independent-v1`. Recursive nonself closure `independent-closure-v1` completed exit0/drained under unchanged defaults, visiting13,601 actual constant dependency nodes; all referenced dependencies are recursively represented, target/scratch aliases and sorryAx absent. Both raw files and exact acceptance tuples are saved. The independent TYPE comparison admits only both-generated binder macro scopes, never written-name/order/type normalization; its actual VALUE differs from the selected target.

One overbroad reconstructed65-TYPE guard failed on a generated declaration with an unsupported metadata type node in the serializer (`ERROR_UNSUPPORTED_TYPE_NODE`). This does not replace the successful actual65 opaque VALUE→TYPE checks and exact raw65 TYPE comparison. The follow-up compiled guard reconstructs the exact old helper/public main types only; generated TYPEs retain the stronger raw equality evidence and direct inferred-value validation. The failed unit remains preserved.

### Final packing correction

After all fixed-series calls drained, the count hypothesis was packed to exactly100 characters; hJ and its existential/membership prefix pack to98. This correction changes whitespace only from the initial selected proof, with an exact whitespace inverse receipt. Final7 signature widths are93,95,66,55,100,98,63; per-line arithmetic table follows final validation. No further proof or API change is involved.

### Phase 6.5 — whole-helper simplify reflection (adapted machinery)

The Claude Code built-in Skill(simplify) is unavailable here. The owner-authorized adaptation is an actual holistic helper review, not a claim that a nonexistent tool was invoked. This fresh auditor is distinct from the helper's original author; the later whole-file reviewer remains separate.

Reuse: existing project pigeonhole/difference/vanishing/index lemmas already express each mathematical stage. The helper makes a substantive bridge between them, not a 1–3-call Mathlib wrapper. Its explicit product count matches the main caller; no numerical main-specific assumptions remain. No additional API or subhelper is justified.

Quality: the same difference polynomial witnesses both RSet membership and index. All hypotheses are point-local to the objects actually inspected, the low-weight cutoff is strict and the resulting index bound weak. Zero degree bounds and an empty variable type are retained. Signature packing was corrected using actual arithmetic; the difference comment remains literally attached to its construction. Exact old/current65 raw TYPE/universe comparisons protect binder names, order, instance arguments and every public contract.

Efficiency: hP remains shared because its fields are reused. Single-use nonzero transport now uses map_ne_zero_iff; no large term is duplicated by inlining it. Broad simp at the degree transport was rejected after its actual failure; the exact intended degree rewrites remain. Performance is measured in the next scoped before/after pass, not inferred from shorter text. No further change warranted by this reflection.

Outcome: ISSUES-FOUND-AND-FIXED (canonical map nonzero API, count simp and final packing). No unresolved mathematical preference, new meaningful helper, or optional API recommendation. Full-file duplication/global performance decisions remain outside this local certificate.

### Line packing — final selected signature (codepoints)

| Line | Width | Next complete syntactic chunk | Arithmetic | Action |
|---|---:|---:|---|---|
| 597 | 93 | 14 | 93 + 1 + 14 = 108 > 100 | ok |
| 598 | 95 | 7 | 95 + 1 + 7 = 103 > 100 | ok |
| 599 | 66 | 49 | 66 + 1 + 49 = 116 > 100 | ok |
| 600 | 55 | 96 | 55 + 1 + 96 = 152 > 100 | ok |
| 601 | 100 | 55 | 100 + 1 + 55 = 156 > 100 | ok |
| 602 | 98 | 57 | 98 + 1 + 57 = 156 > 100 | ok |
| 603 | 63 | none | proof follows | ok |

The last line includes `:= by`. Full types and binder metadata were already independently captured; the pretty-printer type reference is in the exact raw TYPE records.

### Inequality scan

| Location | Reversed ≥/> occurrences | Action |
|---|---:|---|
| Entire helper signature and hypotheses | 0 | No rewrite or rename; strict count and strict weight cutoff preserved. |

## Final selected source and Phase 6 verification

Final source is742 lines, SHA256 `4e83772d7785fc681b8d6656b7254e2c1fb9ca3c0559d6393bd24f9ab43473c7`. Earlier f0c8 selected source is historical; final change is whitespace-only packing, with its preserved exact inverse. Target body11→10 code lines; no branch introduced. Main101 and all text outside the helper remain byte-identical to entry746. Substitution of the genuine original helper exactly recovers entry SHA5fac8481. No meaningful new helper, API, import, type weakening, public statement, docstring, literal paper quotation, or narrative comment changed. Main689 and original27 report555 protected.

All461 imported actual project/helper/generated/DATA declarations across13 source modules passed actual opaque VALUE/TYPE closedness, inferred type, standard axioms, defaults200000/20000/512 and actual source origin guards (`imported-retained-batch1-v2` through5). No all-row credit from earlier TYPE-only/opaque-excluded/cumulative-budget attempts. Final65 local raw TYPE/universe records exactly equal original; every other actual VALUE unchanged. Exact original helper and public caller types are independently compiled (`imported-contract-v1`, `contract-guards-v2`). Independent nonself proof/13,601-node recursive closure is separate from target VALUE. No generalized name normalization.

| Verification | Actual evidence/result |
|---|---|
| 1. Direct selected proof | whole declaration exit0, closed actual VALUE inferred TYPE |
| 2. Original contract | exact raw65 TYPE/universes and compiled original helper/main TYPE guards |
| 3. Standard axioms | all retained461 actual VALUEs; no sorryAx/new axioms |
| 4. Default limits | actual200000/20000/512 guards; none raised |
| 5. Nonself proof | different VALUE, strict binder comparator, recursive13,601-node closure |
| 6. Generality |14 explicit clear-drop expected failures and four formal counterdatasets |
| 7. Retained metadata/origin |461 actual imported rows, five completed batches |
| 8. Caller/public protection | actual main VALUE unchanged, original TYPE compiled, full builds |
| 9. Static/API/comments | exact inverse, nine literal comments, actual mathlib API source plus compiled VALUE |
| 10. Build | final-full-build-v1: actual `/Users/ramin/.elan/bin/lake build` exit0,4.846s; then final-eval-build-v1: actual `lake build Roth.LeanEval` exit0,4.876s; both fully drained |
| 11. Native | fresh unfiltered file_path-only MainLemma/Main/LeanEval: errors0, faileddeps[], partialfalse, timedoutfalse; inherited warnings1/4/0 |

Every final native has exclusive source17 SHA/bytes pre→request→immediate actual return timestamp→full raw save→SHA/bytes/save observation→post receipts, with each prep/save/post tool command exit0 and no session. `final-native-acceptance-v1.json` validates exact chronology and unchanged pins. Main warnings are copyright plus inherited hδ/hQ/hc unused-variable messages; no warning introduced by this helper. No server-cache assumption replaces the actual requests.

The initial final textual scan erroneously included mathematical λ inside protected docstrings and failed. Version2 scans Lean code excluding comments, preserving source and the failed script/qualification. This is a harness failure, not an accepted gate result or a reason to edit protected quotations.

### Phase 4/6 diff gates — local lease

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file / lake_build | pass | actual final-full-build-v1 FULL exit0 includes MainLemma; separate final-eval-build-v1 exit0 |
| definition_protected | pass | no def/abbrev/import/API changes; all source outside target exact |
| theorem_statement_protected | pass | target raw TYPE/universes identical; all64 non-target local VALUEs exact, including main |
| structure_gate | pass | helper10 code lines, no branch; existential conjunction intentionally retains the common witness, not independent facts |
| naming_gate | pass | descriptive private name, no forbidden numeric scheme/abbreviation, no rename queue |
| line_packing_gate | pass | seven measured rows above, exact100-character count line, every action ok |
| inequality_orientation_gate | pass | zero reversed inequality tokens in helper signature/hypotheses |

Cumulative external breakage: full project plus separate Eval builds and complete Main/ML/Eval natives pass;461 actual imported retained values checked. No file-wide cleanup/count claim: the original27 main remains101 lines and fails its headline15 gate. The parent retains its independent performance/structure repair queue.

## Phase 6.6 — Buzz pass (adapted actual profiling)

Parent explicitly held all competing compiler/native/profile/raw-parsing/heavy-review/administrative work through all six captures plus postfreeze/drain. Four matched wall captures use identical actual absolute Lake/Lean CLI `env lean -j1 --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 FILE`, same frozen current parent environment and actual Lake printenv,420-second external timeout, no Lean limit raises. Canonical exact original helper+actual main full command scopes were bound against complete printed payload, whitespace/standalone-comments only. Disjoint column0 command/proof/kernel/compiler/linter roots included; Meta/nested/trailing scopes excluded. Fresh actual local kernel families (helper1, main4) matched65 metadata. Source scaffolds invert exactly to canonical source. Inputs/source17/cache104/root8/setup14/package12202/core12592/binaries4 freeze verified through final postobservation. All18 actual capture/printenv groups absent before any parsing. Raw traces/failures and versioned parsers preserved.

| Scope | Before A ms | After A ms | Before B ms | After B ms | Result |
|---|---:|---:|---:|---:|---|
| helper |105.458|190.002|102.862|190.210|pass actual<1000 |
| actual main101 |1621.425|1598.901|1739.555|1624.699|valid FAIL, original27 queue |

The shortened proof costs about86ms more in these samples. No speedup or causal/noise discount is claimed. Both selected samples are below750ms, so no unchanged third sample or cherry-pick. Numeric comparisons to R4/Q captures from different environment/scope are prohibited.

Two separate configurations add only `trace.profiler.useHeartbeats=true`; actual entry/exit defaults remain200000/20000/512. Raw root-counter sums divided by1000: helper1769.419→3837.020; actual main30208.374→30208.360. These are proof-work counters, never milliseconds or substitutes for wall timing. Installed count_heartbeats macro was prospectively rejected because it sets maxHeartbeats0. `profile-six-acceptance-v1.json` binds all six actual results and whole freeze.

## Phase 7 — local outcome and closure protocol

Issues found and fixed: signature packing, canonical nonzero-map API, count simp unsqueezing. Degree simp unsqueezing failed concretely and remains narrowly squeezed. Every recommended local change implemented; no undecidable preference, new subhelper, deferred local API, rename or decomposition remains. Whole-helper reflection completed above; later whole-file fresh reviewer and parent acceptance remain separate. No Git/central writes, publication,264 credit or global completion claim.

Closure is completed only by the actual exclusive `final-seal.json` in `/private/tmp/roth-mainlemma-helper10-fresh1`, after two fresh full streams and final process drain. That receipt supplies actual counts/hashes and ALL7END status; this report deliberately makes no advance seal claim. Full reference/generic8542-source universe, current17 source/report, cache/root/setup/package/core/binary availability, immutable predecessor closure and every692 logical stored/decoded archive original are bound. This is availability, not an invented exact loaded-runtime closure. Missing pre-reboot historical references and lost771-byte oldADMIN remain explicitly qualified; no old P8/R3 complete-rehash claim. Only four exact self receipts are excluded: manifest, second-rehash, final-drain, final-seal. Parent administration frozen; only small immutable owner snapshots enter closure. After seal all leases return to the owner for independent third review; no further mutation by this auditor.

Final closure recovery: the first two complete streams passed37,403 rows/8,916,568,939 bytes/24,844 binary rows. The subsequent `/bin/ps` call was blocked by sandbox EPERM before execution; its exact failure receipt is retained, with no drain credit. The authorized escalated read-only retry observed183 known groups absent and zero task/printenv rows. Since the failure receipt was new after the second stream, those successful streams and drain are preserved under `*-pre-ps-recovery-v1.json`, and a fresh full two-stream closure plus fresh post-second drain replaces the final boundary. No proof/source/profile rerun or mutation occurred. Prior self-receipts remain historical exact saved bytes, not a claim their old live self paths still hold those bytes. The final seal alone determines final closure counts/hashes.
