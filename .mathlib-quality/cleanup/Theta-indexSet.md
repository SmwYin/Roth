# Dedicated audit: `Roth.indexSet`

Scope: original declaration `Roth/Theta.lean` L56–58, baseline HEAD `08ab073cf398fea8f93cfdba17f6610b7eb61d05`. Only source change is ordinary lambda arrow `=>` → `↦` at L58. Public name, visibility, signature and elaborated value preserved. Three code lines before/after, delta zero. No helpers, caller edits, Git mutations or shared-sidecar writes.

Reference reading: both Lean/mathlib-quality skills; full cleanup workflow; full golfing-rules, proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates and profiling references under `/Users/ramin/.local/share/roth-mathlib-quality/skills/mathlib-quality/references`; relevant style sections on definitions, lambdas, documentation, API, inequalities, signatures, visibility and performance; naming conventions for data definitions. Large combined reads were truncated, so substantive omitted ranges were reread separately.

## Baseline and mathematical contract

Owner supplied published clean checkpoint and complete actual-source LSP `/private/tmp/roth-theta-d01-lsp.json`: success true, partial false, timed_out false, 0 errors / 28 warnings, none at target. Unchanged baseline full builds were not repeated. Header metadata protected. This audit does not claim that whole-file profiling succeeds: later `index_le_lem6` linarith failures under profiling remain known to owner.

Local source `.mathlib-quality/references/clean.tex` L643–667 defines Θ as the supremum of indices of nonzero integer polynomials satisfying partial-degree/coefficient bounds, at rational coordinates with coprime numerators and denominators. The comprehension supplies exactly that family. `RSet` packages the polynomial restrictions, `h : σ → ℤ` packages one shared numerator vector, and the final equality records its index. There is no proof-conjunction decomposition here: existential witnesses and their coprimality/index constraints must stay correlated. Definition accepts arbitrary B, q and r; positivity/nonemptiness conditions belong to later results.

## Full 24-item audit

| # | Item | Concrete result |
|---|---|---|
| 1 | LINT | No target warning in complete baseline; final live check recorded below. |
| 2 | HAVE SCAN | No `have`; term set definition. |
| 3 | SET_OPTION | None on declaration. |
| 4 | SIMP SQUEEZE | No simp calls. |
| 5 | NAMING | `indexSet` descriptive lowerCamelCase data name; no scheme numbers, forbidden abbreviations or single-letter public name. No rename. |
| 6 | LINE PACKING | One 45-codepoint signature line through `:=`; complete measured table below. |
| 7 | BY PLACEMENT | No `by`; `:=` at end of signature. |
| 8 | FORMAT | Two-space body, four-space continuation, no blank/trailing-space lines. Changed ordinary lambda to mapsto. |
| 9 | COMMENTS | No inline comments; protected existing three-line docstring retained byte-for-byte. |
| 10 | DOCSTRING | Public object explained, with rational-point/coprmality context and source citation. Preserved. |
| 11 | VISIBILITY | Retain public, a documented principal definition with Θ and several membership/boundedness/invariance consumers. No visibility change authorized. |
| 12 | STRUCTURE | Three-line definition, two-line body, no proof branch. Membership conjunction ties the same h to coprimality and its index; preserve shared existential. |
| 13 | MATHLIB | Five actual methods below found generic set-image tools and unrelated polynomial results; no direct replacement established. |
| 14 | JUNK DEF | Keep: source-specific mathematical family with nonempty/bddAbove/subset API and repeated consumers, not a disposable one-use abbreviation. |
| 15 | EXISTS LEMMA | n/a: data definition, not single-use private witness lemma. |
| 16 | SHOW vs CHANGE | Neither appears. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | Every parameter/ambient instance considered and concrete drop probes recorded below. No public contract change applied. |
| 19 | INEQUALITY | No inequalities in declaration code, only equality; measured scan below. |
| 20 | NORMAL-FORM | Existential comprehension directly expresses allowed index values; a Set.image form is equivalent but makes witness access less direct. No canonical rewrite obligation identified. |
| 21 | SYNTAX-GEN | Current nested existential supports direct `rintro ... ⟨R, hR, h, hh, rfl⟩`; changing to subtype image would burden callers. |
| 22 | IMPORT-FANOUT | No import change. |
| 23 | CASTS | 0 dropped / 2 explicit casts kept as cross-type: q : ℕ→ℤ for IsCoprime; h : ℤ→ℝ for coordinates. Implicit q : ℕ→ℝ also required. Diff introduces no cast. |
| 24 | INSTANCE-NAME | Not an instance; none introduced. |

Issues fixed: lambda notation. Refactoring needed: none recommended; no new helper audit needed.

## Signature packing and inequality tables

Definition reference: n/a for pretty-printer packing comparison; actual type is captured in imported verification log below.

| Signature line | Codepoints | Next signature token | Arithmetic | Action |
|---|---:|---|---|---|
| 56 | 45 | none, `:=` boundary reached | n/a | ok |

Body L57/L58 widths are 70/70 codepoints. Joining complete body predicate to signature would exceed 100. Body continuation preserves meaningful final index-equality unit, with no artificial signature break.

| Location | Reversed inequality occurrence | Action |
|---|---|---|
| L56 signature and L57–58 body | none; no ≥ or >, only final = | n/a, no rewrite or rename |

## Five actual mathlib searches

Native Lean MCP metadata/full schemas were inspected before calls. All four native searches completed without error; queries bounded to three results except local name lookup eight.

| Method | Actual query | Observed result |
|---|---|---|
| A Lean-Finder | `set of indices of integer multivariate polynomials at coprime rational points` | `xInTermsOfW_vars_subset`, `xInTermsOfW_vars_aux`, `ChevalleyThm.MvPolynomialC.numBound`: unrelated Witt/Chevalley results. |
| B Loogle | `Set.image` | `Set.image`, `Set.imageFactorization`, `Set.mapsTo_image`: generic construction only, not this restricted index family. |
| C LeanSearch | `set of indices of multivariate integer polynomials rational coprime points Roth theorem` | `Poly`, `MvPolynomial.irreducible_sumSMulX`, `addRothNumber`: no returned replacement. |
| D Source rg | `indexSet|def index|theorem.*index` in polynomial/DiophantineApproximation directories; full untruncated `indexSet|Roth.index` across Mathlib | No target-name/restricted-index family hit. |
| E local name pattern | `indexSet` | Positive project hits Roth.indexSet, indexSet_bddAbove, indexSet_nonempty, indexSet_comp_subset; index unavailable, so no absence inference. |

Auxiliary variants: image, imageFactorization/mapsTo_image, restricted polynomial indices, nonempty/bddAbove/subset family API, polynomial degree/Diophantine folders. Common-equivalents lookup does not match discrete/finite/compact/bornology buckets. Conclusion: no equivalent established; generic Set.image is a building block, not replacement for named mathematical content. No new lemma or global absence claim is made. The six replacement rules introduce neither wrappers nor custom typeclass predicates. Independent original-value certification below, not a self-invocation, verifies the unchanged definition.

## Generalisation and literature

| Parameter/context | Role | Mechanical candidate | Result |
|---|---|---|---|
| `{σ : Type*}` | Variable index type | Drop index type; universe widening | Already universe polymorphic; drop τ probe tests missing type. |
| `[Fintype σ]` | Supplies index weight sum | Drop; weaken to `[Finite σ]` | Concrete scratch probes below. |
| `[DecidableEq σ]` | Ambient decidability | Drop | Concrete scratch probe below; if omitted from elaborated definition, no public source change needed. |
| `(B : ℝ)` | Real coefficient bound in RSet | Drop | Concrete scratch probe below; dropping data parameter cannot preserve the bounded family. Abstract field change requires redesign of RSet/index and is not assumption weakening here. |
| `(q : σ → ℕ)` | Denominator vector, coprimality and coordinates | Drop | Concrete scratch probe below; arbitrary vector already allowed; ℤ/ℚ denominator restatement changes object/API. |
| `(r : σ → ℕ)` | Degree/weight vector | Drop | Concrete scratch probe below; degree and index explicitly depend on r. |

No propositional hypotheses, strict bounds, global function-property assumptions or bundled equivalences to weaken. Inversion check n/a: direct data construction, no theorem proof which forgets a concrete object after unfolding. Abstracting a set and a function would merely recreate generic image and lose the named source meaning, not strengthen a theorem.

Public literature searches actually run: `Roth theorem polynomial index Theta supremum bounded coefficients coprime rational points generalization` and `Roth lemma index multivariate polynomial weighted order vanishing generalization`. Top relevant hits of first query included Bombieri–Gubler (secondary hosted copy), [Roth ICM1958 proceedings](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf), [Proof of Roth’s Theorem](https://diposit.ub.edu/bitstreams/8cfc8916-c376-44d7-8822-14f9fed3aa15/download). Second-query relevant hits included polynomial order-of-vanishing discussion (secondary), quantitative Subspace Theorem paper listing, and [Roth’s Theorem lecture notes](https://www.math.uh.edu/~minru/fields/roth.pdf). Only primary Roth proceedings and local clean.tex used for mathematical inference: indices at rational points with coefficient-size control are the intended framework. No literature-supported contract change recommended. ChatGPT math MCP unavailable in tool metadata; recorded as unavailable, not mathematical absence evidence.

## All 42 golf rules

| Rule | Status/reason |
|---|---|
| 1.1 by exact | n/a, term data definition |
| 1.2 by rfl | n/a, no proof wrapper |
| 1.3 rw+exact | n/a, no tactic chain |
| 1.4 simp+exact | n/a, no simp |
| 1.5 trailing rfl | n/a, no simp/rfl |
| 1.6 constructor | n/a, membership predicate rather than proof |
| 1.7 apply+exact | n/a, no tactics |
| 1.8 by_contra | n/a, no contradiction proof |
| 1.9 eta | Coordinate lambda combines h, cast and division; cannot eta-reduce to h or q. Mapsto syntax fixed separately. |
| 1.10 have | n/a, none |
| 1.11 apply+intro | n/a, none |
| 1.12 show | n/a, none |
| 1.13 have projections | n/a, none |
| 1.14 merge rw | n/a, none |
| 1.15 terminal simp | n/a, none |
| 1.16 nonterminal simp | n/a, none |
| 1.17 dot notation | No applicable redundant qualified call; Int.castRingHom is the intended ring hom. |
| 1.18 trailing parentheses | Existing parentheses delimit ring hom and coordinate lambda; no tactic-argument parentheses to remove. |
| 1.19 push_neg | n/a, none |
| 1.20 ∃ helper | n/a, direct set definition; no helper |
| 2.1 grind | n/a, no proposition proof goal |
| 2.2 before grind | n/a, none |
| 2.3 simpa | n/a, none |
| 2.4 fun_prop | n/a, no function-property goal |
| 2.5 positivity | n/a, no positivity goal |
| 2.6 gcongr | n/a, no inequality goal |
| 2.7 lia/omega | n/a, no arithmetic proof |
| 2.8 aesop | n/a, data construction not proof |
| 2.9 norm_num/norm_cast | n/a, casts construct the point; no cast equality goal |
| 2.10 decide | n/a, unrestricted set of real index values |
| 2.11 field_simp/ring | n/a, no algebraic proof |
| 2.12 linear_combination | n/a, no ring proof |
| 2.13 wlog | n/a, no case branches |
| 2.14 calc | n/a, none |
| 2.15 <;> | n/a, no tactic goals |
| 3.1 erw | n/a, none |
| 3.2 continuity | n/a, none |
| 3.3 omega→lia | n/a, no arithmetic tactics |
| 3.4 rcases rfl | n/a, none |
| 3.5 automation attributes | n/a, no new lemma; do not unfold restricted family globally |
| 3.6 simp_all | n/a, none |
| 3.7 heartbeat option | n/a, none |

Step-back / simplify review: direct term comprehension is already compact, keeps witnesses shared and is easy to destruct downstream. No independent proof skeleton or branch to extract. Set.image presentation would add a subtype/product layer without simplifying clients. Built-in simplify tool unavailable; manual holistic equivalent performed, PASS-THROUGH beyond requested syntax cleanup. No new identifiers to verify: ↦ is syntax only.

## Validation, gates, profile, freeze

Module gate: `/Users/ramin/.elan/bin/lake build Roth.Theta` exited 0, `/private/tmp/ThetaIndexSetBuild.log` ends `Build completed successfully (2423 jobs)`. Full `lake build` and separate `lake build Roth.LeanEval` are explicitly owner final gates; this report does not label them passed without owner's actual runs.

Actual built declaration check: `/Users/ramin/.elan/bin/lake env lean /private/tmp/ThetaIndexSetVerify.lean` exited 0; raw UTF-8 `/private/tmp/ThetaIndexSetVerify.log`. This imports `Roth.Theta`, defines an independent `IndexSetAudit.original` copied from original baseline `2b64544bf9f77a8ff957bf1bcaf693ac72217ff6` (with references qualified, retaining original arrow), then proves `Roth.indexSet B q r = original B q r` by `rfl`. It does not use Roth.indexSet to define the original. `#check`, `#print` and `#print axioms` inspect the actual built constant, not a prefix-local lookalike. Actual signature: `{σ : Type u} → [Fintype σ] → ℝ → (σ → ℕ) → (σ → ℕ) → Set ℝ`. Actual axioms exactly `[propext, Classical.choice, Quot.sound]`. Surrounding DecidableEq is already absent; no public weakening needed.

Primary literature fetch note: opening the ICM proceedings PDF failed due to 74.7MB content size; only its search excerpt was available. Local clean.tex was read directly and remains decisive; no uninspected broad generalisation is claimed.

Every parameter probe actually compiled in a separate file importing Roth.Theta; raw logs `/private/tmp/ThetaIndexSet-{dropFintype,weakenFinite,dropDecidableEq,dropB,dropq,dropr,dropσ}.log` (corresponding `.lean` files retained). Exit statuses respectively 1,1,0,1,1,1,1. Drop Fintype and Finite replacement both fail to synthesize `Fintype σ` at the index application. Drop DecidableEq succeeds, agreeing with actual built signature. Drop B/q/r produces unknown identifier errors at their uses. Type-drop variant replacing σ with fresh τ fails to synthesize Fintype τ; already arbitrary type/universe is the maximal direct index domain here. No probe changes live source. These are genuine data/type dependencies, not unused propositional hypotheses. All public parameters remain untouched.

Complete unfiltered final native `lean_diagnostic_messages` on actual final `Roth/Theta.lean` completed with success true, partial false, timed_out false, failed_dependencies empty; 0 errors / 28 warnings and none at L56–58. Raw full response `/private/tmp/ThetaIndexSetFinalLsp.json` retained (console display truncated, stored response is full). All warnings remain owner scope: lines 1, 87, 135, 74, 79, 72, 72, 87, 84, 94, 102, 110, 109, 117, 127, 154, 135, 372, 188, 228, 372, 369, 414, 419, 407, 621, 524, 518; same baseline set. No warning suppression added.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Actual `lake build Roth.Theta` exit 0, raw log above. |
| definition_protected | pass | Signature/name/visibility byte-identical; only body syntax arrow changed; actual built original value equality compiled. |
| theorem_statement_protected | pass | No theorem touched. |
| structure_gate | pass | Two-line defining body, no branches; shared existential outputs preserved. |
| naming_gate | pass | Descriptive lowerCamelCase data name, no banned pattern. |
| line_packing_gate | pass | Every signature line measured; single line 45 codepoints. |
| inequality_orientation_gate | pass | Complete zero-occurrence table above. |
| live diagnostics | pass for target | Complete final unfiltered response, no errors / no target warnings. |
| original type/value and standard axioms | pass | Imported actual built constant compared against independent original, exit 0. |
| cumulative external breakage | owner final gate | Public value/type unchanged; no caller edits; source rg shows direct indexSet users all in Theta. Owner full/LeanEval builds still required. |
| full project and LeanEval | pending owner | Explicitly not run by this leaf. |

## Required 11-step checklist

- [✓] Step 1: reference documents read, with omitted substantive truncated ranges reread.
- [✓] Step 2: full 24-item audit printed in this dedicated report.
- [✓] Step 2.5: all five actual search methods and limitations recorded.
- [✓] Step 2.6: every parameter/instance with concrete compiled drop/weakening probes; public literature/inversion checks.
- [✓] Step 2.7: complete signature codepoint table.
- [✓] Step 2.8: complete inequality scan table.
- [✓] Step 3: all 42 golfing rules have concrete status/reason.
- [✓] Step 4: step-back holistic simplification review, no helper needed.
- [✓] Step 5a: actual final-source full live LSP complete; no target diagnostics.
- [✓] Step 5b: diff/content/module/type/value/axiom gates recorded, owner gates explicit.
- [✓] Step 6a: no rename needed or queued; shared sidecar untouched.

Comments-preserved: protected three-line docstring unchanged; no inline comments to move. Refactoring needed: none. Simplify suggestions: none. Source delta: 0 lines, one ordinary lambda symbol. No new identifier, helper, sorry, axiom, native_decide, limit raise or profiling scaffolding in source.

## Buzz pass and frozen handoff

Outcome: FAST-BOARD for indexSet. Owner explicitly confirmed exclusive uncontended compiler/LSP window. All seven parameter probes and imported-value compiler process completed; final live LSP request completed before profiling started. Actual command `/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/ThetaIndexSetPrefix.lean` exited 0. Raw UTF-8 `/private/tmp/ThetaIndexSetProfile.log` retained. Prefix preserves exact final source, all imports and context through indexSet, then closes Roth; this is explicitly prefix-only and does not certify later whole-Theta profiling.

Actual anchor and non-overlapping timings:

| Component | Seconds | Milliseconds |
|---|---:|---:|
| Outer Elab.command anchored by indexSet docstring/declaration (log L1607) | 0.024983 | 24.983 |
| Associated addDeclCore async, including kernel (L4993) | 0.005153 | 5.153 |
| Associated compileDecls async (L4995) | 0.000058 | 0.058 |
| Associated runLintersAsync (L4998) | 0.003721 | 3.721 |
| Total without nested double counting | 0.033915 | 33.915 |

Nested anchors: Elab.definition.header `Roth.indexSet` 0.382ms, value 23.155ms, kernel 5.121ms, compiler 0.040ms. These nested nodes are not added again. Budget 1000ms; no ≥750ms repeat threshold reached. No performance fix needed, no deferral, maxHeartbeats raises removed/added 0/0. Later whole-module sweep remains owner responsibility after slow-declaration cleanup.

Frozen source SHA256: `4966bfa4274976d8e46102aa89c8fead84392ecf1351f7b337ad8ecfac63ecd9`. Prefix SHA256 `51d6014362009b37be9d6418dcbfee53f456084d97c76ae071e1658cf4be1a9c`. Independent original verification file SHA256 `80a3c69d525277f7616dee91db68443b072c2b81a9059ce0994d0bdd50b7b63d`.

Final diff whitespace check passed. All worker requests, shell sessions and compilers finished; no orphan requests. Source-edit authority revoked at handoff: no further source edits by this leaf. Parent owns sequential final full project then separate LeanEval gates and publication before next original declaration.


## Owner frozen checkpoint gates

After fresh leaf report/source authority revoked and every leaf request drained,owner
sequential `lake build` exited0 in94.839s,then separate `lake build Roth.LeanEval` exited0
in31.755s. `/private/tmp/roth-theta-d02-builds.json` and full/leaneval logs; source SHA
`4966bfa4274976d8e46102aa89c8fead84392ecf1351f7b337ad8ecfac63ecd9` stable throughout.
Owner inspected actual imported original-value rfl/actual standardaxioms,complete unfiltered
LSP and actual trace profile raw evidence. No source edit after freeze; no new helper/API.
Checkpoint publication requires exact-path commit and successful authorized branch push.
