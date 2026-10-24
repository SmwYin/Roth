# Original11 cleanup: `Roth.exists_approximants`

Scope: target and owner-leased deletion of its unused `hδ0` caller argument in `roth_of_isIntegral`. No Git/shared-progress/rename writes, no helpers, no unrelated edits. The genuine original target and entry were saved before Lean/proof changes and are exactly equal: 28 declaration lines / 23 body lines. Entry Main SHA256 `4248f0cd2d75850e16ac260b14a2ad8921e5bb8017cf1e64cff38f5d4f4328a9`.

## Baseline / preparation

Valid same-source prior full build59.459s, separate Eval58.838s, natives Main30.780/Eval28.800/root29.521 and complete LSP reused per owner receipt `/private/tmp/roth-main-owner/delta-choice-owner-accepted-v1.json`; no redundant baseline compilation. Full target/module context and installed workflows/references read. Cache fetch not needed. Header and two unrelated unused-binder warnings remain owner/file-final scope. No file-level change authorized or needed.

# Original11 initial audit
References: full cleanup/cleanup-all workflows and golfing-rules, proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates read; relevant style/naming/review/profiling/buzz read. No simplify invocation available; manual scoped holistic pass required.
1. LINT: entry unused hδ; bounded authorized drop and sole caller repair.
2. HAVE: hs0 no-by single use inline by definitional equality; hsS recursive equation keep; hmem by proof used five times keep; hlt initial by keep; hpos no-by single use inline; hj no-by single use inline; hqi by cast keep or strengthen to positivity; hlt successor no-by single use inline into log API; h1 no-by single use inline with lt_log_of_rpow_lt.
3. SET_OPTION: none.
4. SIMP: empty simp only before successor is redundant candidate; remove.
5. NAMING: exists_approximants snake_case descriptive, no forbidden forms.
6. PACKING: initial five signature widths measured separately; remove hδ then remeasure all lines.
7. BY: correctly on final signature line.
8. FORMAT: replace all lambda => with ↦; eta-reduce Nat.rec lambda and drop redundant Nat ascription.
9. COMMENTS: none in proof.
10. DOCSTRING: present, source and mathematical constraints; scope permits qualified application tip, consider after proof stable.
11. VISIBILITY: public documented construction used by headline theorem; retain.
12. STRUCTURE: 23 body lines; branches 5 and 8 lines; coherent shared existential witness with five linked conditions, no helper needed.
13. MATHLIB: semantic search Liouville hits differ in exponent/arbitrary reduced growth. Loogle gives Real.log_rpow; local source reveals Real.lt_log_of_rpow_lt replacing final arithmetic scaffolding. Existing construction builds on accepted exists_reduced_approx; no full direct replacement found yet.
14. JUNK DEF: n/a theorem.
15. EXISTS LEMMA: nontrivial choice and recursive growth, not trivial witness/rfl wrapper.
16. SHOW: none.
17. PUSH_NEG: none.
18. GENERALISE: α and κ values retained (conclusion and input set); hα,hκ,hinf used by reduced approximants, drop tests remove needed premise; hκ strict needed by accepted earlier theorem, weak κ=0 would require new number theoretic argument outside bounded scope; m needed in Fin indexing; NeZero m needed for q 0; δ needed for growth factor; hδ unused drop; L needed initial logarithm. No universes/typeclass hierarchy or point-local hypotheses. Inversion check: concrete rational denominators used throughout; no optional ambient abstraction.
19. INEQUALITY: no ≥/> code occurrences in signature (arrows → do not count).
20. NORMAL-FORM: canonical integer numerator/natural positive denominator with IsCoprime, Fin indexing, log growth; preserve.
21. SYNTAX-GEN: removing unused hδ improves application; preserve argument order otherwise.
22. IMPORT-FANOUT: no imports added.
23. CASTS: p.2 : ℕ and double parentheses redundant candidate; ℕ→ℝ and ℕ→ℤ casts genuine.
24. INSTANCE-NAME: no instance declaration.

## Final audit resolutions

1. LINT: actual complete Main LSP proves unused hδ warning gone; target/caller no errors.
2. HAVE: only hmem (by-proof, five uses) and initial hlt (two uses) remain. The owner-recommended hsS inlining actually passed complete LSP; recurrence reduces definitionally after rw [hij.symm].
4. SIMP: vacuous simp only removed, none remains.
6. Packing: table below; same five signature lines, reduced binder list.
8. Lambdas use ↦; Nat.rec eta-reduced; no empty proof lines or haveI/letI.
12. Final15 body lines; witness conjunction is coherent shared data, no artificial splitting; branches3 and5 lines.
13. Direct mathlib Real.lt_log_of_rpow_lt replaces hqi/hlt/h1/log_rpow/linarith scaffolding. Entire proof exact? failed; not a1–3-call wrapper.
18. hδ drop verified by actual compiled production proof and solecaller repair. hδ0 remains used elsewhere. Other binders required as detailed below.
23. Dropped redundant `(p.2 : ℕ)` ascription (already Nat); all retained Nat→Real/Nat→Int coercions are genuine cross-type bridges. Initial Real coercion fixes ceil comparison target; no redundant same-type ascription introduced.
24. No named instances added.

## Signature packing (codepoints)

| Line | Width | Next syntactic clause | Clause width | Sum | Action |
|---|---:|---|---:|---:|---|
| 252 | 76 | `(hinf : (approxSet α κ).Infinite)` | 33 | 110 | ok |
| 253 | 74 | `∃ (h : Fin m → ℤ) (q : Fin m → ℕ),` | 34 | 109 | ok |
| 254 | 74 | `(∀ j, IsCoprime (h j) (q j : ℤ))` | 32 | 107 | ok |
| 255 | 93 | `i.val + 1 = j.val →` | 19 | 113 | ok |
| 256 | 71 | `end` | — | — | ok |

The existential quantifier's two linked binders form one witness clause; splitting `∃` from its bound variables would obscure the signature. Width100 #check reference is recorded by the profile derivative.

## Inequality scan

| Occurrence | Result |
|---|---|
| Signature and hypotheses | No ≥ or > occurrences; only correctly oriented < inequalities. |

## Mathlib five-method search

| Method | Actual query / finding |
|---|---|
| A Lean-Finder | finite rational approximations, arbitrarily large denominators, rapidly increasing logarithms: Liouville.frequently_exists_num / LiouvilleWith / Liouville; different hypotheses and conclusions. |
| B Loogle | `Real.log (_ ^ _) = _`: Real.log_pow/log_zpow/log_rpow. |
| C LeanSearch | infinite natural denominators / unbounded sequence: Set.Infinite.not_bddAbove, Set.seq_of_forall_finite_exists; no direct reduced finite logarithmic-growth replacement. |
| D Source | Full target names absent from mathlib DiophantineApproximation; log API source at Pow/Real:854 gives Real.lt_log_of_rpow_lt and is used directly. |
| E Name pattern | exists_seq; source results returned, index unavailable (not evidence of absence). Source variants rpow_lt_iff_lt_log, lt_log_of_rpow_lt, pow/zpow variants checked. |

Compiled absence probe: whole-proof exact? could not close goal. Partial match applied: standard logarithm API; keep nontrivial finite reduced witness construction. Common-equivalents discrete/finite/bounded wrappers do not encode reduced rational approximation or growth.

## Generalisation per binder

| Binder | Class | Use / drop and weakening result |
|---|---|---|
| α:ℝ | structure value | approxSet and Irrational; dropping loses statement parameter. No optional ambient field abstraction. |
| hα:Irrational α | proposition | required argument of exists_reduced_approx; cannot remove from this proof. |
| κ:ℝ | structure value | approximation exponent in premise/conclusion. |
| hκ:0<κ | proposition | required strict hypothesis of exists_reduced_approx; weak form does not satisfy that API. Additional κ=0 theory outside bounded scope. |
| hinf | proposition | supplies reduced witnesses for every threshold. |
| m:ℕ | structure value | Fin m witness domain and q0. |
| NeZero m | typeclass | needed to elaborate Fin m zero; no parent class weakening. |
| δ:ℝ | structure value | growth factor2/δ throughout statement and recursion. |
| hδ:0<δ | proposition | unused; actual production proof compiles after drop, with complete clean target/caller LSP. |
| L:ℝ | structure value | initial exponential threshold and L<log(q0). |

Universe, decidability and point-localisation catalogue: no applicable binders. No new generality proposed. Inversion diagnostic: concrete rational denominator/log construction remains throughout; no concrete object merely unfolded once. Literature query `Roth theorem proof choose rational approximations denominators arbitrarily large rapidly increasing` returned original [Roth1955](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/EFB89E2873019B246F004FAA06E05A7F/S0025579300000644a.pdf/rational_approximations_to_algebraic_numbers.pdf), an [elementary exposition](https://aleksa-milojevic.github.io/expository/roth.pdf), and the [AMS preview](https://www.ams.org/bookstore/pspdf/mbk-48-prev.pdf). Local cited §7 supplies the exact construction; no source-driven additional change identified. Math ChatGPT MCP unavailable.

# All 42 golfing slots
- [1.1] n/a: no by-exact wrapper.
- [1.2] n/a: no by-rfl wrapper.
- [1.3] n/a: final rewrite/exact replaced by direct log API.
- [1.4] n/a: no simp/exact chain.
- [1.5] n/a: no trailing rfl.
- [1.6] already anonymous existential and conjunction constructor.
- [1.7] n/a: apply log theorem leaves genuine cast/ceil bound, not just exact hypothesis.
- [1.8] n/a: no contradiction.
- [1.9] applied: eta-reduced s Nat.rec lambda.
- [1.10] applied: hs0/hsS/hpos/hj/hlt-successor/h1 eliminated; hmem and initial hlt reused.
- [1.11] n/a: no apply followed by intro.
- [1.12] n/a: no show.
- [1.13] n/a: no projection-only temporary have.
- [1.14] n/a: one successor rw remains.
- [1.15] applied: removed vacuous simp only.
- [1.16] n/a: no remaining simp.
- [1.17] applied trans and trans_lt dot notation.
- [1.18] n/a: no avoidable trailing callback parentheses.
- [1.19] n/a: no push_neg.
- [1.20] n/a: nontrivial recursive existential with growth proof.
- [2.1] whole-proof grind actually failed, no witnesses constructed.
- [2.2] n/a: no retained grind.
- [2.3] n/a: direct log API replaces calculation, no simp consolidation.
- [2.4] n/a: no regularity properties.
- [2.5] positivity scaffolding eliminated using strict denominator bound and exp_pos.
- [2.6] n/a: no inequality congruence goal; successor bound is concrete ceil witness.
- [2.7] n/a: no residual Nat/Int arithmetic goal, max bound uses existing order API.
- [2.8] whole-proof aesop actually failed without progress.
- [2.9] exact_mod_cast retained for genuine Nat→Real order bounds.
- [2.10] n/a: infinite-set real existential not finite decidable computation.
- [2.11] n/a: no polynomial or denominator identity.
- [2.12] n/a: no ring/ring_nf ending.
- [2.13] n/a: zero/successor recursion is not symmetric cases.
- [2.14] n/a: no calc.
- [2.15] retained shared rintro zero/succ <;> constructor proof.
- [3.1] n/a: no erw.
- [3.2] n/a: no continuity/measurability.
- [3.3] n/a: no omega, arithmetic API handles bounds.
- [3.4] n/a: no rcases rfl.
- [3.5] n/a: constructive existential is unsuitable global simp/grind rule.
- [3.6] n/a: no simp_all.
- [3.7] n/a: no resource override.

Step back: whole-proof exact? actually failed; a distinct exponential-threshold independent construction is prepared for semantic checking. Choice plus concrete Nat.rec is the short mathematical route. No helper/API wrapper needed after direct mathlib logarithm API.

## Manual holistic review (simplify unavailable)

No actual simplify invocation claimed. Substantive review checked witness reuse, canonical rational data, both logarithm bounds, choice/recursion, cast routes, and caller. The existing shared witness is coherent; direct log API and definitional recurrence remove scaffolding without a helper. All8 proof lines saved improve clarity. Existing docstring/source context preserved.

## Refactoring and renames

Only bounded unused-assumption removal and leased single caller repair; no renames queued. Earlier accepted global renames and file-final eta candidate untouched. No import, trust, resource-limit, option or metadata changes.

## Semantic verification

`/private/tmp/roth-main-approximants/semantics-receipt.json` records actual current target, independently constructed exponential-threshold proof, and original-contract recovery. Actual fresh families are singleton roots, each with actual universe list `[]` (not a blanket family universe assumption). Complete old target TYPE10750B and caller TYPE2391B were read using indexed row offsets and cap2*TYPE_bytes+2000, decoded only the TYPE JSON string, and SHA256 checked; no old VALUE decoded/exported.

Strict recursive comparison covers Expr, Name, Level, BinderInfo, metadata, literal, projection, syntax/source fields without ExprBEq shortcut. Actual original=current sixth anonymous instance Name differs from each independent/recovery module salt. The two literal actual pairs are constrained to forall path6 and instImplicit, both actual Name.hasMacroScopes and equal eraseMacroScopes; after replacing that exact binder Name only, the entire remaining raw TYPE repr bytes and recursive structures agree. Raw independent/recovery TYPEs are explicitly unequal. Caller full old TYPE remains strictly equal. The independent theorem never calls the target/generated family or later Main results. Fresh local graph is acyclic,367 actual external origins strictly upstream; earlier accepted helper/DATA graph reused.

Actual opaque proof VALUEs checked in memory, inferred/closed/no admits, standard axioms only, bytes316494(target)/302590(independent)/2789(recovery), hashes in receipt. Actual caller VALUE likewise inferred/closed/standard. Full raw VALUE export/identity is not claimed. Actual defaults200000/20000/512 verified.

Failed probes disclosed: initial oldTYPE literal parser failed at unquoted `_@`, before any semantic rows. Narrow quote repair exposed the actual two hygienic-binder mismatches; failed log preserved as semantics-type-mismatch.stdout. Exact finite-pair supplement then passed; no generic normalization, inference loop, or limit change.

## Build closure and whitespace qualification

Production proof/API full build passed64.852s; separate `lake build Roth.LeanEval` passed31.899s. Measured signature packing then moved only `∀ i j : Fin m,` onto the preceding line (93chars), preserving every token and all other source bytes. Exact prepack snapshot, packing-only.diff, and SHA256/token-equality binding are saved. A second full build was already launched before the coordinator's reuse ruling and passed32.831s on the current packed source. The coordinator explicitly approved reuse of the separate Eval build under this exact whitespace-only qualification; no duplicate separate Eval build was run solely for formatting. Current fresh native Eval/root, complete diagnostics, semantics and profile still bind current source.

## Fresh verification / gate status

All invocations are recorded with actual exit0 and group-absence evidence in scoped `*-launch.json`/`*-terminal.json` logs. Production after final packing is Main601lines/33547B/SHA256 `8875868f966da50880091739b9a23369d133766180b27dd6972813090fd12228`; Eval unchanged SHA256 `610ec95658c5d43c931217bfb56b54d62f825473de17b3bdf6a1dde85dd900ca`.

| Gate | Result / evidence |
|---|---|
| lake_build_file and full lake_build | PASS current `lake build` exit0/32.831s; proof/API build64.852s also passed. |
| separate Eval build | PASS `lake build Roth.LeanEval` exit0/31.899s; reused solely under explicitly approved exact signature-whitespace qualification above. |
| unfiltered natives | PASS Main31.960s / Eval28.045s / root27.657s, each terminal0; full stdout/stderr captured. |
| complete fresh LSP | PASS Main0errors/3existing unrelated warnings1,386,387; Eval/root0diagnostics; all partial=false, no failed dependencies. |
| definition_protected | PASS no def/abbrev or computational data changes. |
| theorem_statement_protected | PASS authorized unused hδ removal only; original positive-δ contract recovered, full conclusion preserved. |
| cumulative_no_unintended_breakage | PASS sole caller exact argument deletion, full caller oldTYPE strict equal + actualVALUE checked; root/Eval validated. |
| structure_gate | PASS15body lines; branches3/5; one coherent shared witness, no helpers required. |
| naming_gate | PASS descriptive snake_case, no forbidden pattern/abbreviation. |
| line_packing_gate | PASS all5signature rows measured; final quantifier moved onto93char line; max target width93. |
| inequality_orientation_gate | PASS no≥/> in code signature/hypotheses; required scan present. |
| trust/resource/scaffolding | PASS actual opaque VALUE checks/std axioms/default200000/20000/512; no sorry/newaxiom/native_decide/limit raise/count_heartbeats/trace/scaffolding in production. |
| exact scoped source diff | PASS only target and owner-leased single caller argument; every other source byte unchanged, Eval unchanged. |
| comments/docs/metadata | PASS no proof comments originally; original docstring preserved, no metadata change. |

New identifier verification: `Real.lt_log_of_rpow_lt` found as actual declaration in pinned mathlib `Analysis/SpecialFunctions/Pow/Real.lean:854`, and accepted by complete LSP/full build/natives. All other added names already existed in the entry proof.

Actual #check @Roth.exists_approximants at format.width100 from the frozen profile derivative:

```lean
@exists_approximants : ∀ {α : ℝ},
  Irrational α →
    ∀ {κ : ℝ},
      0 < κ →
        (approxSet α κ).Infinite →
          ∀ (m : ℕ) [inst : NeZero m] {δ : ℝ} (L : ℝ),
            ∃ h q,
              (∀ (j : Fin m), (h j, q j) ∈ approxSet α κ) ∧
                (∀ (j : Fin m), IsCoprime (h j) ↑(q j)) ∧
                  (∀ (j : Fin m), 1 < q j) ∧
                    L < Real.log ↑(q 0) ∧ ∀ (i j : Fin m), ↑i + 1 = ↑j → 2 / δ * Real.log ↑(q i) < Real.log ↑(q j)
```

## Buzz / actual profile

Outcome FAST-BOARD,326.035ms<1000ms and<750ms repeat threshold; no repeat needed. Exact source prefix/unchanged imports+preceding commands+target followed by actual family TYPE/VALUE/default/std and width100 observation. This is scoped-prefix evidence; mandatory wholefile all-row capture remains the owner's later final-file phase, not claimed completed here.

| Disjoint outer root | ms |
|---|---:|
| command |20.294|
| async target proof |276.181|
| kernel parent |3.795|
| async lint |25.765|
| total |326.035|

Nested kernel3.739ms already included in3.795 parent; no nested doublecount, no compiler parent or lazy prior DATA roots in this target row. Actual generated family enumeration returned only `Roth.exists_approximants`; full canonical payload (doc/signature/body) binds exactly, root line/byte offsets in target-profile-acceptance.json. Actual opaque VALUE inferred/closed/standard, actual universe list observed. Full raw VALUE identity/export not claimed.

Production/profile root TYPE differs solely in the observed actual hygienic instance binder at sixth forall: production `inst.«_@».Roth.Main.3334748119._hygCtx._hyg.24`, prefix `inst.«_@»._stdin.3334748119._hygCtx._hyg.24`. Both actual Name.hasMacroScopes true, both erase to `inst`, instImplicit at path6. The capture verified full recursive TYPE equality and complete remaining repr bytes after replacing only this actual binder Name; postparse confirmed exactly1raw Name occurrence. Raw TYPE equality is false. Receipt production-profile-family-types.json preserves literal Name repr and full TYPE hashes.

Historical narrow indexed target row576.293ms comes from actual Main689 after MainLemma caller repairs, not genuine-originalMain684. Its entire canonical target matches the genuine original including docstring. Contexts remain explicitly separate: no speedup ratio, causal claim, or noise dismissal. Old317MB trace not reparsed.

Exact HOLD ACK preceded preparation. Narrow ps escalation used firsttry; only task-owned arguments/PID/start/executable persisted, full parent/Lake environment bytes compared only in memory with hash/length plus approved PATH/LEAN/toolchain allowlist. All launches/driver terminal0/absent and14known groups actually absent, defaults/env/freezePASS before RAWUNPARSED notice; explicit owner RELEASE received before parsing. No failed profile phase. Capture/source freeze remains exact.

## Phase checklist / result

- ✓ Step1 references and context read; genuine original/entry saved before Lean/golf and exactly compared.
- ✓ Step2 all24 audit items; all findings resolved or explicitly n/a with scope reason.
- ✓ Step2.5 actual five-method search and compiled exact? probe.
- ✓ Step2.6 per-binder mechanical/generalisation and public literature status.
- ✓ Step2.7 all5signature rows measured/repacked.
- ✓ Step2.8 inequality scan.
- ✓ Step3 all42rule slots, applicable bounded probes recorded.
- ✓ Step4 holistic alternative strategy review; distinct independent exponential-threshold proof.
- ✓ Step5a complete fresh diagnostics on all affected modules.
- ✓ Step5b actual builds/native/semantic/protection/structure/naming/packing/inequality gates.
- ✓ Step6a no renames; previous global rename choices untouched.
- ✓ P5a only authorized unused assumption/caller refactoring; P5b empty scoped rename queue.
- ✓ P6.5 substantive manual scoped holistic review, no unavailable simplify invocation claimed.
- ✓ P6.6 exact valid frozen profile326.035ms under budget; no deferral.
- ✓ P7 report complete. File-final eta candidate left untouched for independent final review.

Before28lines/23body → after20lines/15body; saved8lines. Main609→601. Issues fixed: unused binder+caller, single-use scaffolding, eta/lambda syntax, redundant Nat ascription, empty simp, signature packing. No new helper/rename/import/unrequested generality. Refactoring deferred: none in target scope.

END — actual FINAL. Owner minimal independent review passed (`/private/tmp/roth-main-owner/approximants-owner-review-v1.json`). All compiler/native/semantic/profile/parser drivers and LSP queries terminal; all14known recorded launch groups actually absent. ALL scoped source/report/compiler/native/semantic/LSP/profile leases released. No Git/shared-progress/next-target edits.
