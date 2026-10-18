# Dedicated single-declaration audit: `Roth.RSet`

Scope: `Roth/Theta.lean` L46–50 (docstring L46–48; declaration L49–50), baseline HEAD `2b64544bf9f77a8ff957bf1bcaf693ac72217ff6`. Sole leaf, no delegation. Source unchanged; no Git or shared-report changes. Before/after: 2 code lines / 2 code lines, delta 0. Existing docs and mathematical definition preserved.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md in full, both skills in full, the cleanup worker workflow, relevant style rules and naming conventions. The five reference documents under the installed skill and `/Users/ramin/.local/share/roth-mathlib-quality/skills/mathlib-quality/references` have identical SHA1s.

## Baseline and diagnostics

Owner baseline `lake build` passed, exact log `/private/tmp/roth-theta-baseline-full.log`; separate LeanEval gate passed per owner. Full unfiltered native LSP response on this unchanged source is `/private/tmp/roth-theta-baseline-lsp.json`: `success=true`, `partial=false`, `timed_out=false`, `failed_dependencies=[]`; 0 errors, 28 warnings. No warning in RSet's range. The owner retains all 28 warnings. Their locations: 1, 86, 134, 73, 78, 71, 71, 86, 83, 101, 93, 109, 108, 126, 134, 116, 153, 187, 227, 371, 371, 368, 413, 418, 406, 620, 523, 517. Header warning is outside this declaration and protected by user scope. Other warnings concern theorems, not this definition. My redundant native batched diagnostics/search wrapper stalled and was terminated; no success is claimed from it. Actual bounded direct searches below completed.

## Mathematical check

Local source `.mathlib-quality/references/clean.tex` L643–654 defines the polynomial set by integrality and nonzeroness, degree bounds in every variable, and absolute coefficient bounds. Lean represents integrality by `MvPolynomial σ ℤ`; its conjunction states exactly the remaining conditions. Arbitrary `σ` permits all finite variable enumerations without fixing `Fin m`; the definition itself does not require finiteness or decidable equality. It also makes sense without positivity restrictions on B or r, already broader than the source's setup. A conjunction inside a set comprehension is its defining membership condition, not a theorem with independently proved conjuncts. Splitting it into helper theorems would add API without simplifying construction.

## Full 24-item audit

| # | Item | Concrete outcome |
|---|---|---|
| 1 | LINT | No diagnostics L46–50 in complete unfiltered LSP response. |
| 2 | HAVE SCAN | n/a: no `have` or proof blocks. |
| 3 | SET_OPTION | None attached to declaration. |
| 4 | SIMP SQUEEZE | n/a: no simp calls. |
| 5 | NAMING | RSet is a descriptive source-symbol name without forbidden patterns, numeric schemes, abbreviations, or single-letter public name. Generic lowerCamelCase would suggest `rSet`; public API preservation takes precedence over that cosmetic rename, which is not queued. |
| 6 | LINE PACKING | Complete signature width table below: one 56-codepoint signature line, no next signature token. Body is 76 codepoints. |
| 7 | BY PLACEMENT | n/a: term definition with `:=` ending signature line. |
| 8 | FORMAT | Flush-left def, two-space body, no blank line/trailing whitespace/internal tactic sequence. |
| 9 | COMMENTS | No inline comments; docstring retained byte-identically. |
| 10 | DOCSTRING | Existing public doc describes mathematical object and cites three source conditions; preserved. |
| 11 | VISIBILITY | Public object documented in module API, used in `Roth/MainLemma.lean` and Theta's index API. Retain public. |
| 12 | STRUCTURE | Two-line data definition, no branches, no long proof. Membership conjunction is mathematical data and needs no theorem decomposition. |
| 13 | MATHLIB | Five actual searches below; partial degree-only matches have different objects and omit coefficient bound/nonzero conditions. Keep definition. |
| 14 | JUNK DEF | Not junk: multiple public uses and domain-specific source concept; no inlining. |
| 15 | EXISTS LEMMA | n/a: data definition, not existential lemma. |
| 16 | SHOW vs CHANGE | n/a: neither syntax appears. |
| 17 | PUSH_NEG | n/a: no tactics. |
| 18 | GENERALISE | Every elaborated parameter and surrounding instances considered below; already arbitrary universe/type, finite/decidable assumptions not captured. |
| 19 | INEQUALITY | Degree/coefficient bounds both use ≤; no ≥ or >. Table below. |
| 20 | NORMAL-FORM | Set comprehension is canonical for conjunction of nonzero/coordinate-degree/coefficient constraints. Not a submodule: excludes zero and has bounded coefficients. |
| 21 | SYNTAX-GEN | Current conjunction supports direct `.1`, `.2.1`, `.2.2` destructuring used downstream. Alternative norm/intersection presentation does not ease callers. |
| 22 | IMPORT-FANOUT | n/a: no import added. |
| 23 | CASTS | Diff contains no casts. Existing ℤ→ℝ cast is required by real bound B. Inner `: ℤ` ascription is redundant but deleting it alone fails minimum-value filter; value/API untouched. |
| 24 | INSTANCE-NAME | n/a: definition, no declared instances. |

Issues requiring source fixes: none. Refactoring needed: none. Optional naming observation is explicitly subordinate to public API preservation.

## Line packing

Definition signature reference: `@Roth.RSet : {σ : Type u_1} → ℝ → (σ → ℕ) → Set (MvPolynomial σ ℤ)`.

| Signature line | Codepoints | Next signature token | Arithmetic | Action |
|---|---:|---|---|---|
| 49 | 56 | none; `:=` boundary reached | n/a | ok |

L50 is a 76-codepoint body. Joining the entire body to L49 would require `56 + 1 + 74 = 131`, exceeding 100. No artificial signature break exists.

## Inequality scan

| Location | Occurrence | Orientation/action |
|---|---|---|
| Signature | no ≥ or > | n/a, no rewrite |
| Body L50 | `degreeOf j R ≤ r j` | smaller side left, keep |
| Body L50 | `|((R.coeff d : ℤ) : ℝ)| ≤ B` | smaller side left, keep |

## Mathlib search-status

All remote searches used bounded `/private/tmp/roth_mcp_probe.py` with the Lean LSP MCP Python environment and finished exit 0; native initial batch was not counted.

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | `set of nonzero integer multivariate polynomials bounded degree coefficients` | `MvPolynomial.degreesLE`, `restrictTotalDegree`, `restrictDegree`; degree-only objects, no exact replacement. |
| B Loogle | `MvPolynomial.degreeOf, Set` | `chevalley_mvPolynomial_mvPolynomial`; unrelated constructibility degree bound. |
| C LeanSearch | `multivariate integer polynomial bounded coefficients bounded individual degree` | `Polynomial.card_mahlerMeasure_le_prod`, `MvPolynomial.degrees_sum_le`, `Poly`; no equivalent returned. |
| D Source rg | full `RSet`, `degreesLE`, `restrictDegree` over mathlib polynomial directories and project; also `degreeOf.*≤` / `supported` | RSet only project; degree-only submodules found. Full-name rg untruncated. |
| E Name-pattern local search | `restrictDegree` | Verified actual source hit `MvPolynomial.restrictDegree`; symbol index unavailable, positive source hit only, not an absence claim. |

Auxiliary variants inspected: `mem_degreesLE`, `mem_restrictDegree`, `mem_restrictDegree_iff`, `supported`, support and degree-bound variants. `degreesLE` and `restrictDegree` contain zero and allow arbitrary coefficient size, so cannot replace RSet. Common-equivalents table: no discrete/compact/bornology equivalence supplies this polynomial set. Concluded: partial degree-only matches; keep the source-specific intersection of conditions. No exhaustive global absence claim or new theorem is made, so no invented exact?/apply? absence probe; the original value/type is independently compile-checked below. No wrapper, custom typeclass predicate, or missing-API proof signal arises.

## Generalisation status

| Parameter/context | Class/use | Candidates considered | Result |
|---|---|---|---|
| `{σ : Type*}` | type variable, arbitrary variables | universe widening / concrete→abstract | Already arbitrary universe/type; no finite enumeration baked in. |
| section `[Fintype σ]` | ambient class | drop / `Finite` | Not captured in elaborated definition at all; no source change needed. |
| section `[DecidableEq σ]` | ambient decidability | drop / classical | Not captured in elaborated definition at all; no source change needed. |
| `(B : ℝ)` | structure value, bounds coefficients | drop; abstract ordered codomain | Drop destroys the family parameter; abstract norm/codomain restates protected data. No proof hypothesis to weaken. |
| `(r : σ → ℕ)` | structure value, individual degree bounds | drop; alternate index/bound type | Drop destroys individual bounds; degreeOf naturally ℕ. Already arbitrary σ. |

No propositional hypotheses, strict bounds, global continuity/monotonicity assumptions, bundled equivalences or explicit typeclasses exist in the elaborated signature. Mechanical weakening table therefore introduces no valid small safe edit. Inversion check: n/a; defining a set directly, no concrete witness theorem/proof that forgets its object. Generic coefficient-ring/absolute-value replacements are different constructions with extra choices, not supported assumption weakening of this source-defined object.

Literature search: actual WebSearch `Roth theorem auxiliary polynomial bounded coefficients individual degrees generalization`; top relevant hits: [Proof of Roth’s Theorem](https://diposit.ub.edu/bitstreams/8cfc8916-c376-44d7-8822-14f9fed3aa15/download), [An elementary approach to Roth’s theorem](https://aleksa-milojevic.github.io/expository/roth.pdf), [Roth’s theorem overview](https://en.wikipedia.org/wiki/Roth%27s_theorem). Results retain the multivariate integer-polynomial, partial-degree and coefficient-size framework; no change is justified to this defined family. Local source is authoritative and was read directly. ChatGPT math MCP: n/a, no such tool in available metadata. Literature-driven big-change candidates: none recommended.

## Golfing rules: all 42 considered

| Rule | Status/reason |
|---|---|
| 1.1 by exact wrapper | n/a: no tactic wrapper |
| 1.2 by rfl | n/a: no proof |
| 1.3 rw + exact | n/a: no rewrites |
| 1.4 simp + exact | n/a: no simp |
| 1.5 trailing rfl | n/a: no simp/rfl |
| 1.6 constructor chain | n/a: set predicate, no construction proof |
| 1.7 apply + exact | n/a: no tactics |
| 1.8 contradiction | n/a: no proof |
| 1.9 eta lambda | n/a: set binder predicate depends on R, not eta form |
| 1.10 single-use have | n/a: none |
| 1.11 apply + intro | n/a: none |
| 1.12 redundant show | n/a: none |
| 1.13 have projections | n/a: none |
| 1.14 consecutive rw | n/a: none |
| 1.15 terminal simp only | n/a: none |
| 1.16 nonterminal simp | n/a: none |
| 1.17 dot notation | Already `R.coeff`; degreeOf is standard mathematical spelling, no gain |
| 1.18 trailing parentheses | n/a: no applicable higher-order call |
| 1.19 push_neg | n/a: none |
| 1.20 existential helper | n/a: no existential lemma |
| 2.1 grind whole proof | n/a: produces data set, no proof goal |
| 2.2 delete before grind | n/a: no grind |
| 2.3 simpa consolidation | n/a: no simp/proof |
| 2.4 fun_prop | n/a: no function-property proof |
| 2.5 positivity | n/a: inequalities define membership rather than goals |
| 2.6 gcongr | n/a: no inequality proof |
| 2.7 lia/omega | n/a: no arithmetic proof |
| 2.8 aesop | n/a: no proof goal |
| 2.9 norm_num/norm_cast | n/a: no cast proof |
| 2.10 decide/kernel | n/a: arbitrary polynomial set, no closed decidable proposition |
| 2.11 field_simp/ring | n/a: no equality proof |
| 2.12 linear_combination | n/a: no ring proof |
| 2.13 wlog | n/a: no cases |
| 2.14 calc collapse | n/a: no calc |
| 2.15 multiple goals | n/a: no goals |
| 3.1 erw→rw | n/a: none |
| 3.2 continuity/measurability | n/a: none |
| 3.3 omega→lia | n/a: none |
| 3.4 rcases rfl | n/a: none |
| 3.5 automation attributes | n/a: not introducing a theorem or unconditional rewrite |
| 3.6 simp_all | n/a: none |
| 3.7 heartbeat option | n/a: none |

Step-back reflection / manual simplify equivalent: term-mode set comprehension is already the direct mathematical construction; tactics would obscure it, and a general degree submodule would omit the nonzero/coefficient restrictions. No shared proof skeleton or helper is warranted. Built-in simplify callable unavailable; manual holistic check performed, outcome PASS-THROUGH.

## Validation and gates

Source-prefix scratch files preserve exact imports, namespace, ambient variables, docstring and RSet value through L50, then close namespace; no repository helper is added. `/private/tmp/ThetaRSetVerify.lean` contains `#check @Roth.RSet`, `#print Roth.RSet`, `#print axioms Roth.RSet`, plus equality of original full value by `rfl`. An initial scratch-only `pp.width` typo was corrected to `format.width`; no source edit resulted.

Module/full/LeanEval build gates are delegated explicitly to file owner final Phase 6; per-worker deferral is not a claim of a fresh worker module build. There are no source changes or new identifiers.

| Gate | Result | Evidence |
|---|---|---|
| definition_protected | pass | Source declaration/value byte-identical. |
| theorem_statement_protected | pass | No theorem edits. |
| structure_gate | pass | Two-line definition; no theorem conjunction or proof branch. |
| naming_gate | pass under public API rail | No forbidden pattern; cosmetic casing note documented, no unauthorized rename. |
| line_packing_gate | pass | One-line signature measured above. |
| inequality_orientation_gate | pass | No reversed inequality. |
| live full diagnostics | pass for declaration | Complete unfiltered owner LSP response; no RSet warning. |
| lake_build_file/full/LeanEval | owner final Phase 6 | Baseline owner builds passed; owner reruns final builds. |

## Required phase checklist

- [✓] Step 1: reference documents read in full.
- [✓] Step 2: all 24 audit items recorded.
- [✓] Step 2.5: all five actual search methods recorded.
- [✓] Step 2.6: every elaborated parameter and ambient instance reviewed; literature searched.
- [✓] Step 2.7: all signature-line codepoint widths recorded.
- [✓] Step 2.8: inequality scan table recorded.
- [✓] Step 3: every one of the 42 golfing rules has an explicit status.
- [✓] Step 4: independent step-back / holistic simplification review completed.
- [✓] Step 5a: complete unfiltered LSP clean for target declaration, file warnings retained.
- [✓] Step 5b: protection/content gates recorded, owner build deferral explicit.
- [✓] Step 6a: no rename needed/authorized; shared sidecar untouched.

Comments-preserved: no inline comments; existing public docstring retained. Rules applied: none; no unnecessary code churn. Renames-queued: none. Source-edit authority frozen on handoff; no further edits by this worker.

Independent validation completed: `/Users/ramin/.elan/bin/lake env lean /private/tmp/ThetaRSetVerify.lean` exited 0; `/private/tmp/ThetaRSetVerify.log` prints the original universe-polymorphic type/value and exactly `[propext, Classical.choice, Quot.sound]`. The `rfl` original-value equality compiled. No Fintype or DecidableEq parameter appears in the actual signature.

Buzz prefix checks: actual `/Users/ramin/.elan/bin/lake env lean --profile -Dprofiler=true -Dprofiler.threshold=0 /private/tmp/ThetaRSetPrefix.lean` exited 0, log `/private/tmp/ThetaRSetProfile.log`; RSet's set-builder command elaboration 16.1ms, kernel check 0.414ms. Separate `-Dprofiler=true -Dprofiler.threshold=0` compile exited 0, `/private/tmp/ThetaRSetAnchoredProfile.log`: corresponding elaboration 1.91ms. These runtime profiler logs emit command-order timings rather than source positions in this toolchain; an explicit trace-profiler probe is recorded below. All timings well below 1000ms. Full Theta profiling intentionally not run: owner reports later `index_le_lem6` linarith times out under profiling; this bounded source prefix validates RSet only. No performance limit was raised and no scaffolding entered the source.

Frozen source SHA256: `7804edad88aa3e586df46b7722755ba89e67566c5434c58ae970d0dd2fbfa4fd`; HEAD remains `2b64544bf9f77a8ff957bf1bcaf693ac72217ff6`. Prefix SHA256 `92ea135cbff1dd45fd898ed8c52e5d3dbcc71d3cba346d9054accd5ccb4036cd`; verification scratch SHA256 `a5cc90bc6546e1f7331c0b4908fe3b9c105af9eddf55e70d0af6252090bd6e8e`.

Explicit anchored buzz probe completed exit 0: `/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/ThetaRSetPrefix.lean`, log `/private/tmp/ThetaRSetTraceProfile.log`. Actual anchors: `[Elab.definition.header] [0.005528] Roth.RSet` (5.528ms), `[Elab.definition.value] [0.019761] Roth.RSet` (19.761ms), `[Kernel] [0.000508] typechecking declarations [Roth.RSet]` (0.508ms), `[Compiler] [0.000032] compiling: [Roth.RSet]` (0.032ms). Outcome FAST-BOARD for this declaration; no deferral, no fixes needed, maxHeartbeats raises added/removed 0. This is a real source-prefix run, not a full-module profiler success claim. All worker shell/probe sessions have completed; none orphaned.

The enclosing `[Elab.command] [0.029547]` node prints the exact RSet declaration and docstring: whole command 29.547ms, below 1000ms. This is the declaration timing anchor, including its elaboration/lint command context.


## Owner checkpoint after leaf release

Fresh leaf source/report edit authority revoked and every request drained. Owner applied only
Phase3 import ordering: alphabetized Mathlib group before alphabetized project group, with blank
separator. Six original imports retained; no declaration/body/docs changed. Final source SHA256
`d454ac8b873677f7ea6de6e38c8443eb3d53795c46bb760559666e2e309ee6e1`.

- Actual `lake build Roth.Theta` exit0, `/private/tmp/roth-theta-d01-module.log`.
- Complete unfiltered final-source native LSP: success=true,partial=false,timed_out=false,
  failed_dependencies=[],zero errors28warnings,`/private/tmp/roth-theta-d01-lsp.json`.
- Independent original definition in separate namespace equals actual built `@Roth.RSet` by rfl;
  actual `#print axioms Roth.RSet` standard-only,exact universe-polymorphic type preserved;
  `/private/tmp/roth-theta-d01-original.lean/.log`,compiler exit0. Ambient Fintype/DecEq absent.
- Fresh uncontended actual source-prefix profile through RSet,with final import order:
  `lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0
  /private/tmp/roth-theta-d01-prefix.lean`,exit0,raw UTF8 log
  `/private/tmp/roth-theta-d01-profile-final.log`. Explicit Elab.command RSet anchor35.280ms;
  associated kernel0.711ms,compiler0.036ms,total36.027ms,well below750ms/1000ms.
  Earlier owner `d01-profile.log` overlapped an original-contract compiler during startup;
  it is NOT accepted uncontended timing evidence. No false full-Theta profile pass is claimed.
- Owner frozen sequential full `lake build`:exit0 in88.463s,then separate
  `lake build Roth.LeanEval`:exit0 in37.522s;sourcehash stable in both.
  `/private/tmp/roth-theta-d01-builds.json` and corresponding full/leaneval logs.
  Exact-path commit and successful push are final checkpoint publication gates.
