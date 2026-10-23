# Cleanup — `Roth.exists_reduced_approx`

Final source proof: 23 lines (original 53), with the image and fiber blocks each 9 lines. One substantive normalization helper was separately audited by a fresh worker and accepted locally. Parent and helper await joint owner publication after closure. This report supersedes the partial handoff; historical snapshots and failed experiments remain in `/private/tmp/roth-main-reduced-approx`.

## Baseline and provenance

Same-source accepted baseline: complete Main LSP had zero errors and four existing warnings outside the target; the accepted full/Eval/native baseline was reused instead of rebuilding it for a label change. Genuine original Main SHA `f651e4dd4b511c9aec15608b6d4ea9a2a4140ac513d486cee4c4ed7c30fa1069` and worker entry Main SHA `6c0515414938241c00257dc0c0604d0d7900e69b0b56351644b1dc633a3bb95b` were saved before all Lean experiments. Their target sources are byte-identical. The original theorem declaration has 56 lines including its three signature lines; its proof body has 53 lines (correcting the initial off-by-one estimate).

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md, the full installed Lean4/mathlib-quality skills and cleanup/cleanup-all workflows, and relevant style/naming/review/profiling references.

## Full 24-item audit

1. **LINT:** no target warnings. Final complete Main diagnostics: zero errors, four existing warnings at 1/282/423/424 (header and unused hδ/hQ/hc outside the target).
2. **HAVE SCAN:** original hred, hxR, hxdiv, hden, inner h1, hdenR, hV, hfib, hε, second hxR, hqpos, hpow, second h1, h2, h3, hsub all examined. Original normalization block moved into the independently audited helper; coprimality is applied directly. Original hpow/h2/h3 and manual rpow inversion disappeared; hsub disappeared via mathlib finite-fiber assembly. Final hV/hfib have proof content; hm is a typed term used twice (membership and hcon); hbound is rewritten then used. No unused one-use term have remains.
3. **SET_OPTION:** none; no raised limits or profiling scaffolding in production.
4. **SIMP SQUEEZE:** the original empty simp-only normalizations disappeared from the parent. Final `simpa [← hρx, ρ] using hm.2` is terminal and intentionally unsqueezed. The separately audited helper owns its own simp/monotonicity decisions.
5. **NAMING:** `exists_reduced_approx` is descriptive snake_case, free of forbidden abbreviations and numerical schemes. No rename warranted or queued.
6. **LINE PACKING:** every signature line measured in codepoints; conclusion repacked onto the last hypothesis line up to the next complete atomic predicate. Table below.
7. **BY PLACEMENT:** by ends each preceding signature/have line.
8. **FORMAT:** two-space tactic indentation, four-space signature continuation, no empty proof lines, no semicolon tactic chains, mathematical lambda uses ↦. Removed unused hρ equation. No haveI/letI.
9. **COMMENTS:** preserved and re-anchored the exact inline signpost about reduction beside the helper use; preserved the cited source signpost and citation. Genuine original target has one inline -- signpost plus its documentation source paragraph; no comment was removed.
10. **DOCSTRING:** preserves the claim and source; adds the application context that coprimality supports successive approximant choices. No proof strategy moved into documentation.
11. **VISIBILITY:** retained the existing public approximation API and caller contract. The new proof-only normalization lemma is private and independently accepted; no unrelated visibility change.
12. **STRUCTURE:** original 53-line proof → 23 lines. hV and hfib each 9 body lines, no branch >10. Existential conclusion keeps membership, denominator bound, and coprimality for the same witness, so artificial fact-splitting would obscure the contract. One natural membership-only helper; no wrapper/tuple helper.
13. **MATHLIB:** direct use of `Set.Finite.of_finite_fibers`; rational normal form and coprimality remain library facts. Five-method results below.
14. **JUNK DEF:** n/a: theorem, no data definition.
15. **EXISTS LEMMA:** n/a: substantive approximation result, no trivial private witness wrapper.
16. **SHOW/CHANGE:** none in parent.
17. **PUSH_NEG:** none; by_contra! retained.
18. **GENERALISE:** every parameter examined and proposition drop-tests run; no verified parent weakening. Normalization needs only nonnegative κ, as reflected in the accepted helper. Details below.
19. **INEQUALITY:** no ≥ or > in Lean signature/hypotheses. No reversed-orientation name.
20. **NORMAL-FORM:** rational values are canonically represented by Rat.num/Rat.den; approxSet membership is the project interface. No competing equivalent normal-form theorem found.
21. **SYNTAX-GEN:** existential pair with explicit Q₀ directly supports caller choice; preserved binder order and implicitness. No restatement warranted.
22. **IMPORT-FANOUT:** n/a: no new import.
23. **CASTS:** parent retains three explicit cross-type casts: hq.2→ℤ in the conclusion, hq.1→ℚ in ρ, x→ℝ in the fiber threshold. All are substantive bridges; no redundant cast retained. Function type ℤ×ℕ→ℚ fixes ρ's codomain. Removed the old real-denominator/cast scaffolding from the parent.
24. **INSTANCE-NAME:** n/a: no instance declaration.

## Mathlib search status

| Method | Query / result |
|---|---|
| A Lean-Finder | Reduction to coprime numerator/denominator: Rat.den_div_eq_of_coprime, den_mk, and unrelated approximation bounds; no approxSet membership theorem. |
| B Loogle | `Rat.den (_ / _) ≤ _`: no hit. |
| C LeanSearch | Infinite set / finite fibers: Set.Finite.preimage' and generic finite-image API. |
| D source search | den_dvd, num_div_den, cast_def, infinite image, finite fibers: read and used Set.Finite.of_finite_fibers, plus existing rational API. |
| E local-name | Rat.den_: den_dvd, den_divInt, den_mkRat, den_pos and arithmetic variants; source hits valid, index unavailable, so no absence claim from an empty index. |

Auxiliary variants checked: den_div_eq_of_coprime, den_mk, mul_den_dvd, image/preimage', of_finite_fibers, num_div_den, cast_def. Common-equivalents bucket: finiteness. Conclusion: partial library matches; use them directly and keep the project theorem. Whole-target exact? failed; apply? offered only generic logical repackaging. No unsupported global absence claim.

## Generalisation status

| Parameter | Class | Mechanical candidates / actual result |
|---|---|---|
| {α : ℝ} | value | Occurs in statement and Irrational; dropping leaves it unbound. Abstract-field replacement would change approxSet/Real.rpow and is outside this concrete task. |
| hα : Irrational α | proposition | Live drop-test failed at hα.ne_rat in the positive-distance argument; reverted. No global/pointwise catalogue weakening applies to this predicate. |
| {κ : ℝ} | value | Occurs in the set and exponent; dropping leaves it unbound. No class/universe parameter to weaken. |
| hκ : 0 < κ | proposition | Live drop and 0≤κ trials failed at actual uses, particularly strict decay in eventually_div_rpow_lt; reverted. The weak trial also had an incidental hκ.le error in the then-original normalization block. These failures establish no verified mechanical weakening, not impossibility of a different proof at κ=0. |
| hinf | proposition | Live drop-test failed at final hinf contradiction (and expected caller arity errors); reverted. |
| Q₀ : ℕ | value | Occurs as arbitrary denominator cutoff; removing binder leaves conclusion unbound. Changing argument order/implicitness would disrupt direct caller choice. |

All changed-header tests were reverted before source closure. No algebraic typeclass, global continuity/measurability/monotonicity, decidability, or universe hypothesis exists to weaken. Inversion check: approximation structure and rational denominators drive the argument throughout; the concrete object is not merely unfolded and forgotten. No warranted ambient expansion or companion theorem.

Literature query: `rational approximation reduced fractions infinitely many denominators irrational generalization`. Top three hits were Koukoulopoulos's [arXiv survey](https://arxiv.org/abs/2109.11003), its [EMS chapter](https://ems.press/content/book-chapter-files/33183), and [author PDF](https://dms.umontreal.ca/~koukoulo/documents/publications/DS-expository.pdf). They use reduced rational approximations and general error sequences Δ_q. Moving this theorem to arbitrary error functions requires new monotonicity/decay assumptions and a different interface, so it is not a mechanical weakening warranted here. Math MCP unavailable. Local clean.tex1578–1587 gives exactly reduction, positive fixed-rational distance, finite fibers, and unbounded reduced denominators. Big-change recommendations: none.

## Line packing

| Signature line | Codepoints | Next whole hypothesis/atomic conclusion | Arithmetic | Action |
|---|---:|---|---|---|
| 158 | 78 | `(hinf : (approxSet α κ).Infinite)` (33) | 78+1+33=112>100 | ok |
| 159 | 82 | `IsCoprime hq.1 (hq.2 : ℤ) := by` (31) | 82+1+31=114>100 | ok |
| 160 | 35 | no next signature line | n/a | ok |

The final focused capture supplies actual `#check @Roth.exists_reduced_approx` at format.width100; its output is recorded with the timing evidence. Maximum parent source line width84. No byte-width substitutions.

## Inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 1 | full signature and hypotheses | zero ≥/> | n/a | no _ge_/_gt_ |

## Golfing rule pass

| Rule | Actual status |
|---|---|
|1.1 by-exact|n/a: no wrapper.|
|1.2 by-rfl|n/a: no parent wrapper.|
|1.3 rw+exact|n/a: final rw changes a hypothesis subsequently used in a different contradiction, not the goal.|
|1.4 simp+exact|applied strategy: final cast block collapsed to terminal simpa using hm.2.|
|1.5 trailing rfl|eliminated original cast-proof blocks; no parent trailing rfl.|
|1.6 anonymous constructor|already uses witness/And tuples.|
|1.7 apply+exact|n/a: none.|
|1.8 by_contra!|already present; retained.|
|1.9 eta-reduce|n/a: ρ uses two projections and a quotient, not eta expansion.|
|1.10 inline have|removed hε/hxR/happ/hpow/h1/h2/h3/hsub blocks via composition, accepted helper, decay API, and finite-fiber API; hm has two uses, hbound is rewritten and used.|
|1.11 refine+fun|already used subset rintro and le_of_not_gt fun.|
|1.12 redundant show|n/a: none.|
|1.13 have projections|removed bundled hred and hcop; intrinsic Rat.reduced applied directly.|
|1.14 merge rw|new reciprocal normalization uses one combined rw list.|
|1.15 terminal simp only|n/a: none in final parent.|
|1.16 nonterminal simp|n/a: none in final parent.|
|1.17 dot notation|retained finite-image .subset and uses hκ.le; existing mathlib finite-fiber assembly directly.|
|1.18 application pipe|Applied final `not_lt_of_gt hbound <\| by simpa`.|
|1.19 push Not|n/a: no push_neg.|
|1.20 trivial exists|n/a: no trivial existential helper.|
|2.1 grind|whole-proof test failed at the missing mathematical construction.|
|2.2 delete before grind|n/a: no grind remains.|
|2.3 simpa|applied final rational-value cast simplification, replacing the explicit equality/cast/rewrite block.|
|2.4 fun_prop|n/a: no function-property goal.|
|2.5 positivity|old rpow positivity/threshold scaffolding removed; needed strict distance follows irrationality, not positivity automation.|
|2.6 gcongr|normalization inequality isolated and independently audited; accepted helper's final gcongr reused, no re-audit. Parent inequality uses exact reciprocal algebra.|
|2.7 lia/omega|n/a: no arithmetic automation block remains; denominator bound is le_of_not_gt with real contradiction.|
|2.8 aesop|whole-proof trial failed; direct finite-fiber argument replaces custom logical assembly.|
|2.9 norm_num/norm_cast|exact_mod_cast worked in direct candidate; final simpa handles the bridge more directly; no concrete numeric computation.|
|2.10 decide|n/a: unbounded existential/irrationality is not finite computation.|
|2.11 field_simp;ring|n/a: no algebraic equality closure; reciprocal inequality handled by div_lt_iff₀.|
|2.12 linear_combination|n/a: no ring/ring_nf closure.|
|2.13 wlog|n/a: no symmetric duplicate cases.|
|2.14 calc to term|old two-stage approximation inequality moved to the independently audited normalization helper; no final parent calc.|
|2.15 <;>|n/a: image witness membership, boundedness and equality are distinct obligations.|
|3.1 erw→rw|n/a: no erw.|
|3.2 fun_prop|n/a: no continuity/measurability.|
|3.3 omega→lia|n/a: no omega.|
|3.4 rfl substitution|image witness rintro already substitutes with rfl.|
|3.5 attributes|no new global simp/grind attribute warranted for this project theorem.|
|3.6 simp_all|n/a: no simp_all only.|
|3.7 resource limits|none present/added.|

## Step back

The proof now states its mathematical division clearly: reduced values form a finite image under a hypothetical denominator bound, and each fiber is finite by strict decay. Mathlib assembles finite fibers directly. Whole-proof automation and exact?/apply? did not supply this construction. Term-mode compression of the remaining witness/image steps would hide shared membership evidence; the natural short blocks are retained. No alternative helper or ambient expansion is required.

## Failed and retained experiments

`whole-attempts.json` records grind/aesop/exact?/apply? on the original target. Live drop/weakening failures are preserved. `fiber-wrong-position-attempt.json` records an unsuccessful LSP replacement positioned inside the old fiber block, so its intro failure is not mathematical evidence. The subsequent full-source replacement compiled and is retained. Semantic scratch v1/v2 failed because the old caller TYPE's generated names needed correct quoting; no production theorem failed, no admits were introduced. Their logs are retained, and only a successful corrected check can close semantics.

## Verification and gates

Final FULL `lake build`: exit0,59.282s; subsequent separate `lake build Roth.LeanEval`: exit0,32.261s. Direct native Main/Eval/root: exit0,26.940/25.476/27.484s. Captured launch/terminal/stream hashes in scratch. Main complete unfiltered LSP0errors4existingwarnings. Genuine-original independent target compiled exit0,26.071s. Final source Main SHA `8f25b12a5dc43b92b8020d100a5a4b2978a7377994adfdb8c22f5bab2e18e958`; accepted helper source and all preceding/following source are unchanged since helper acceptance.



### Completed semantic and dependent-file gates

Corrected target-specific checker `Semantics.lean` passed exit0 in93.106s. It compares genuine old/current/independent full TYPE recursively, including Name components, Levels, BinderInfo and metadata, without an ExprBEq shortcut. It checks actual opaque VALUEs in memory for inference, closedness, no admits, and only propext/Classical.choice/Quot.sound. It enumerates actual fresh generated families and actual universes (target `[Roth.exists_reduced_approx]`; independent `[independentReducedApprox]`, both root universes empty as in the old metadata). No VALUE identity between different proofs/modules is claimed. Only sizes/hashes, types and small receipts were persisted.

The independent fixture replays exactly the genuine original target proof except its declaration name; its actual constant closure cannot use the current target, circular wrappers, or later Main declarations. Accepted unchanged preceding leaves are reused: approxSet, approxSet_den_le_finite, eventually_div_rpow_lt, and the freshly accepted private normalization helper. Actual external origins have strictly earlier module indices; the fresh local graph is acyclic. Previously accepted upstream graph evidence is reused rather than replayed across the entire project.

The direct caller `Roth.exists_approximants` has strict full TYPE equal to its genuine old indexed row. Its current actual opaque VALUE is inferred, closed, admit-free, and standard-axiom in memory. Only TYPE and metadata were decoded from the indexed old rows; no large old caller VALUE was decoded, exported, or copied. Complete Eval/root LSP also passed with no errors or warnings. Main's four existing unrelated warnings remain documented above.

### Focused performance gate

Final exact-source-prefix derivative compiled with `lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0`, separate stdout/stderr. Full canonical doc/signature/body binds to the production target; prefix bytes, exact imports and preceding commands bind to final Main. The appended observation enumerates actual family/TYPE/universes and checks actual VALUE/defaults/std/closedness/inference, then prints #check at format.width100. Actual profile TYPE serialization equals the production TYPE already checked strictly against original/independent TYPE.

| Disjoint target root | ms |
|---|---:|
| Outer Elab.command |12.354|
| Async proof |179.935|
| Async kernel parent |6.224|
| Async linter parent |14.921|
| **Total** |**213.434**|

The nested kernel check6.127ms is already in its6.224ms parent and is not added again. No compiler or lazy earlier DATA root belongs to this target. Total<1000ms and<750ms, so no repeat was required or performed.

The historical whole-source original row is separately retained as a valid **FAIL1034.003ms**. Its complete canonical source equals the genuine original target; indexed narrow reads verified its full raw printed command and four actual root lines. This is a different source-prefix/context measurement; no timing ratio or causal before/after claim is made, and no noise waiver is used.

Before any profile preparation the owner explicitly ACKed HOLD. The capture's first ps observer attempt used the approved narrow escalation, with only task-owned args/PIDs/start/exe and safe environment fields persisted; full environment equality was checked in memory. Tool identity/current binaries, defaults200000/20000/512, environment bytes, and all41frozen inputs matched before/after. All five launches and driver terminated, all process groups were absent, raw data remained unparsed, and owner explicitly RELEASED before raw parsing. Phase receipts preserve this order. The accepted helper's independent final202.439ms evidence is reused because its exact source prefix remained unchanged; no helper reprofile/re-audit.

Actual width100 reference:

```lean
@Roth.exists_reduced_approx : ∀ {α : ℝ},
  Irrational α →
    ∀ {κ : ℝ},
      0 < κ → (Roth.approxSet α κ).Infinite → ∀ (Q₀ : ℕ), ∃ hq ∈ Roth.approxSet α κ, Q₀ < hq.2 ∧ IsCoprime hq.1 ↑hq.2
```

### New identifiers

| Identifier newly used in parent | Verification |
|---|---|
|Set.Finite.of_finite_fibers|Read Mathlib/Data/Set/Finite/Lattice.lean234; full build/native/semantics pass|
|approxSet_num_den_mem_aux|Fresh independent helper audit/owner local acceptance; exact helper source unchanged|
|eventually_div_rpow_lt|Previously accepted preceding theorem; source and current TYPE bound; full build and profile pass|
|not_lt_of_gt|Mathlib/Order/Defs/PartialOrder.lean106 alias; full build/native pass|
|Real.rpow_zero/div_one/div_right_comm/div_lt_iff₀/one_mul|Existing library facts; compiled parent, strict semantics and profile observations pass|

### Gate status — exists_reduced_approx

| Gate | Result | Evidence |
|---|---|---|
|lake_build_file|pass|FULL build0/59.282s includes Main; separate Eval0/32.261s; launch/terminal receipts|
|lake_build|pass|Actual complete project build0,2467 jobs|
|definition_protected|pass|No def/abbrev mutation|
|theorem_statement_protected|pass|Parent strict original TYPE exact; signature only repacked; helper addition explicitly authorized by STRUCTURE audit and fresh helper lifecycle|
|structure_gate|pass|23-line parent, hV9/hfib9, no branch>10, coherent same existential witness|
|naming_gate|pass|Descriptive snake_case; no forbidden pattern; no rename queue edit|
|line_packing_gate|pass|All three signature lines measured above; no repack row|
|inequality_orientation_gate|pass|Zero ≥/> in Lean signature and hypotheses|
|cumulative_no_unintended_breakage|pass|Direct caller full TYPE/actualVALUE checked; FULL/separateEval/nativeMainEvalroot/completeunfilteredLSP pass|
|performance|pass|213.434ms, complete canonical/family/disjoint roots/default/env/freeze evidence|

Overall: **pass** for this original declaration and its audited helper; publication belongs to owner.

### Simplify and file-final boundary

Actual Skill(simplify) is unavailable in this environment; no invocation is claimed. Mandatory fresh independent whole-file holistic review remains the owner's later file-final lifecycle. This declaration's full audit, structure, build, semantic, and focused performance gates are complete. The independent helper lifecycle has already completed and owner minimally reviewed this parent closure with no source recommendations. Fresh full-source all-row timing remains mandatory at file-final, distinct from this focused parent gate.

### Result

Before56 declaration lines/53 body lines; after26 declaration lines/23 body lines; saved30 parent lines. Accepted helper adds8 declaration lines/6 body lines. Whole Main worker-entry658→638 lines (net−20, including helper and documentation). Renames queued:none. Comments preserved:1/1 inline signpost plus citation/source signpost; no deletion or relocation from docstring. Refactoring needed:none for parent. No limits/axioms/admits/weaker conclusions/native_decide/count_heartbeats introduced. No other target or caller source was edited.

Phase checklist:
- [✓] Step1 references/workflows read
- [✓] Step2 full24-item audit
- [✓] Step2.5 five-method mathlib search
- [✓] Step2.6 every parameter/generalisation/literature/inversion check
- [✓] Step2.7 all signature width rows and actual width100 reference
- [✓] Step2.8 inequality scan
- [✓] Step3 all42 rules have actual status or concrete n/a reason
- [✓] Step4 strategy reflection and whole-proof automation/search attempts
- [✓] Step5a complete unfiltered final diagnostics
- [✓] Step5b all diff/build/structure/naming/packing/inequality gates
- [✓] Step6a no rename warranted; shared queue untouched
- [✓] Original/current/independent and direct-caller strict contracts/actual values
- [✓] Focused profile actual capture/default/env/freeze/drain/release/parse

All exact paths, source/diff bindings, accepted old TYPE metadata, failed trials, completed tool receipts and profile evidence are in `/private/tmp/roth-main-reduced-approx`. Source/report leases return to owner at END for joint helper+parent publication.
