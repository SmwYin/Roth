# Phase 4 — `Roth.wronskian_update_sub_smul`

Baseline `a860965`; declaration originally at 181–190, worker entry at 164–173.
Single-declaration scope. The existing public signature, visibility, documentation,
definitions, imports, and toolchain are preserved. Source ownership was released
immediately after final module/LSP verification; subsequent work is report-only.

## References and mathematical reading

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md in full. Also read the worker contract,
Lean/mathlib-quality skills, applicable style sections, and naming conventions.

Subtracting `c` times column `ν` from distinct column `ν'` preserves the determinant.
Hasse differentiation commutes with subtraction and constant scalar multiplication,
so the updated family's Wronskian matrix is precisely that column update. The final
proof maps this matrix equality through `Matrix.det` and composes it with mathlib's
column-operation theorem. Entrywise update formulas let one terminal simp discharge
the matrix equality without manual cases.

## Full audit (24 items)

1. **LINT:** No warning in the target. Final complete LSP has only existing copyright
   header warning and predecessor unused `hφ`/`hd` warnings at 127/128. Those are outside
   this worker's scope and remain with the file coordinator.
2. **HAVE SCAN:** Original L166 `have hM : ... := by ...`, used once at L173. It has
   substantive proof content, so rule 1.10 does not mandate inlining. The better
   composition proof retains its mathematical obligation as the `congrArg` hole and
   eliminates the named matrix equality and final rewrite chain. No `have` remains.
3. **SET_OPTION:** None in source before or after. Width settings occur only in scratch.
4. **SIMP SQUEEZE:** Original two `simp [...]` calls both terminal. Final single
   `simp [...]` is terminal and unsqueezed; no nonterminal simp needs squeezing.
5. **NAMING:** `wronskian_update_sub_smul` describes invariance under a family update
   subtracting a scalar multiple; snake_case, no forbidden abbreviation, numeric
   scheme, `_aux` number, single-letter public name, `_ge_`, or `_gt_`. No rename needed.
6. **LINE PACKING:** Both signature lines measured below; complete conclusion cannot
   fit after the binders. No signature change required.
7. **BY PLACEMENT:** `:= by` remains at the end of the conclusion line.
8. **FORMAT:** Two-space tactic indentation, no blank lines in declaration or trailing
   whitespace, one tactic per line, no `haveI`/`letI`. Removed old `fun k =>` along with
   its obsolete explicit matrix expression; no lambda remains in the proof.
9. **COMMENTS:** No inline proof comments existed; none removed. Existing four-line
   docstring and source citation are byte-identical.
10. **DOCSTRING:** Existing public docstring explains the column operation and source;
    preserved under the existing-documentation contract.
11. **VISIBILITY:** Existing exported column-operation invariant, named in module
    implementation notes and used by `wronskian_eq_zero_iff`. Public API retained;
    no visibility mutation authorized or needed.
12. **STRUCTURE:** Body 8→5 lines, declaration 10→7. No conjunction in statement and
    no branches after cleanup; below all extraction thresholds. No helper needed.
13. **MATHLIB:** Five-method status below. Partial generic match already supports this
    proof; used directly. The remaining matrix-conversion content concerns the
    project's `wronskianMatrix`, not a duplicate of the generic matrix theorem.
14. **JUNK DEF:** n/a: theorem, no definition introduced or edited.
15. **EXISTS LEMMA:** n/a: no existential helper or witness construction.
16. **SHOW vs CHANGE:** n/a: neither occurs.
17. **PUSH_NEG:** n/a: no negation-normalization tactic.
18. **GENERALISE:** All parameters inspected below. No API change applied. Typeclass
    weakening of this declaration alone fails against the field-bound definitions;
    distinctness is necessary, verified by a compiled one-column counterexample.
19. **INEQUALITY:** Required scan below; zero reversed order relations.
20. **NORMAL-FORM:** Equality reducing a column update to the original Wronskian is
    the natural rewrite direction. Constant multiplication is left unchanged in the
    public statement; proof locally converts it to scalar multiplication.
21. **SYNTAX-GEN:** OK: an explicit distinctness proof and scalar fit the current caller.
    Bundling a family equivalence would complicate this use and require a new API.
22. **IMPORT-FANOUT:** n/a: no imports added; all used lemmas available in existing context.
23. **CASTS:** 0 dropped / 0 cross-type casts / 0 load-bearing ascriptions introduced.
    `C c` is the mathematical constant-polynomial map, not a redundant type cast;
    parentheses in `(-C c)` group the scalar argument.
24. **INSTANCE-NAME:** n/a: theorem, no instance declarations or local instances.

Issues fixed: replace named matrix equality plus rewrite chain with congruence
composition; combine the entrywise update cases using conditional simplification.
Refactoring needed: none. No rename queue entry.

## Mathlib search status

| Method | Query and actual result |
|---|---|
| A Lean-Finder | `determinant unchanged adding scalar multiple of another column`: returned `Matrix.det_updateRow_add_smul_self`, `Matrix.det_updateCol_add_smul_self`, and `Matrix.det_updateCol_add_self`. |
| B Loogle | `Matrix.det, Matrix.updateCol`: returned the column-addition, scalar, sum, and zero-column determinant lemmas. |
| C LeanSearch | Unavailable: coordinator supplied the already-established HTTP 500 service failure. Not repeatedly retried; not evidence of mathematical absence. |
| D Source search | Untruncated `rg` for `det_updateCol.*(sub\|add_smul)`, `updateCol_apply`, full `wronskian_update_sub_smul`; found the determinant theorem at `Determinant/Basic.lean:478`, entrywise update at `RowCol.lean:233`, target and its existing caller. `Function.update_apply` found at `Logic/Function/Basic.lean:669`. |
| E Local name patterns | `det_updateCol` returned seven source-backed declarations including add/smul/sum and the needed theorem; semantic index reported `unavailable`, so no absence inference. All selected names additionally compiled with `#check`. |

Auxiliary variants considered: update-column addition, addition of scalar multiple,
scalar-column determinant, zero/repeated column, update-row counterpart, update-column
entrywise and self/non-self formulas. Common-equivalents table: no discrete/finite/
separation/bornology bucket applies.

Conclusion: **partial match** `Matrix.det_updateCol_add_smul_self`, used directly.
The project-specific Hasse matrix conversion remains necessary; the existing public
invariant remains under the user's API-preservation instruction. No new wrapper,
custom predicate, or unsupported claim of mathlib absence. Whole-goal `exact?` in an
isolated context without the target theorem failed; `apply?` offered only generic
polynomial extensionality and unrelated conditions, not a replacement theorem.

## Generalisation status

| Parameter | Class | Use / mechanical candidates | Verification and disposition |
|---|---|---|---|
| `{K : Type*}` | Type/universe | Coefficient type; already universe-polymorphic. Dropping changes well-formedness of all following types. | No universe restriction to weaken; retain. |
| `[Field K]` | Typeclass | Required by current `wronskian` and `wronskianMatrix` signatures. Consider drop, `CommRing`, `DivisionRing`; predicate `IsField` reformulation requires definition/API changes. | Actual isolated probes with current definitions under `[CommRing R]` and `[DivisionRing D]` both fail to synthesize `Field`. Dropping cannot provide it either. No source change. |
| `{l : ℕ}` | Structure value | Sizes `Fin l` and the matrices. Dropping leaves index types unbound; arbitrary finite index requires restating derivative-row order. | Retain natural size parameter; no current-call-site need for a new indexed construction. |
| `{φ : Fin l → K[X]}` | Structure value | Appears in both sides, updated entry and source column. Drop makes the statement ill-formed. | Retain; no extra property to weaken. |
| `{ν : Fin l}` | Structure value | Source column in update and distinctness. Drop leaves those terms unbound. | Retain. |
| `{ν' : Fin l}` | Structure value | Destination column and distinctness. Drop leaves those terms unbound. | Retain. |
| `(h : ν ≠ ν')` | Proposition | Needed by determinant column-operation theorem. Drop and point/strict-to-weak catalogues considered: this is already a local distinctness condition, not an ordered strict inequality. | Compiled counterexample when indices coincide: `l=1`, coefficient field `ℚ`, constant family `1`, `c=1`; updated Wronskian is unequal to original. Cannot drop. |
| `(c : K)` | Structure value | Scalar used in updated polynomial. Drop leaves update unbound. | Retain arbitrary scalar; no nonzero hypothesis required. |

Inversion check: the abstract determinant invariance is already the mathlib theorem,
which this proof uses; the remaining conversion still uses the specific Hasse-linear
matrix entries. Generalizing the coefficient ring would first require broadening the
two existing definitions, rather than weakening this theorem in isolation. No present
caller needs that change, so no new API proposal is being carried forward as a task.
No mathematical hypothesis was changed or silently removed.

### Literature search status

Web query: `determinant elementary column operation commutative ring invariance generalization`.
Top three returned hits recorded: Linnæus University thesis (diva2:2074772), Stephen New's
MATH 146 determinant notes, and Stanford PBC Vandermonde notes. The primary sources used
were [New, Chapter 4](https://www.math.uwaterloo.ca/~snew/MATH146/chap4.pdf), whose Theorem
4.26 treats elementary column operations over a commutative ring, and the
[Stanford Vandermonde notes](https://crypto.stanford.edu/pbc/notes/misc/vandermonde.html),
which explicitly work over a commutative ring and use column operations in determinant
computations. These support the generic ring-level determinant ingredient already in
mathlib; they do not require changing this project's public definition contract.
ChatGPT math MCP: n/a, no callable mathematical second-opinion tool exposed in this session.
Literature-driven required changes: none.

## Required line-packing artifact

Actual `#check` with `format.width := 100`:

```lean
@wronskian_update_sub_smul : ∀ {K : Type u_1} [inst : Field K] {l : ℕ} {φ : Fin l → K[X]} {ν ν' : Fin l},
  ν ≠ ν' → ∀ (c : K), wronskian (Function.update φ ν' (φ ν' - C c * φ ν)) = wronskian φ
```

Signature unchanged; widths are Unicode codepoints. Following the file's binder/
conclusion packing convention, the next unit is the complete conclusion, not a split
function application.

| Sig line | Chars | Next complete binder/conclusion | Arithmetic | Action |
|---|---:|---|---|---|
|164|90|`wronskian (Function.update φ ν' (φ ν' - C c * φ ν)) = wronskian φ := by` (71)|90+1+71=162>100|ok|
|165|75|none; conclusion and `:= by` included|n/a|ok|

## Required inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
|1|Full signature and all hypotheses|n/a: zero `≥` or `>` order relations|none|no `_ge_`/`_gt_` in name|

## Golfing-rule pass (all 42)

| Rule | Status |
|---|---|
|1.1 by exact|n/a: no such wrapper.|
|1.2 by rfl|n/a: no such wrapper.|
|1.3 rw + exact|n/a: no trailing exact; final rewrite chain replaced by composition.|
|1.4 simp + exact|n/a: original and final simp calls are terminal.|
|1.5 trailing rfl|n/a: none.|
|1.6 constructor|n/a: no conjunction/product proof.|
|1.7 apply + exact|n/a: none.|
|1.8 by_contra|n/a: none.|
|1.9 eta reduction|Original matrix-entry lambda is not an eta-redex; removed with intermediate matrix expression.|
|1.10 single-use have|Original hM contains a by proof, so mandatory no-by rule does not apply; optional fold into congrArg hole succeeds and is kept.|
|1.11 apply + intro|n/a: no such sequence.|
|1.12 redundant show|n/a: none.|
|1.13 have projections|n/a: hM was equality, not a product.|
|1.14 merge rw|n/a: no adjacent rw; old closing rewrite sequence eliminated.|
|1.15 terminal simp only|n/a: none was squeezed.|
|1.16 nonterminal simp|n/a: none.|
|1.17 dot notation|Applied `.trans` to compose congruence with determinant theorem; retain `h.symm`.|
|1.18 less parentheses|n/a: second argument to `.trans` spans a line and parentheses are standard; no dispensable wrapper introduced.|
|1.19 push_neg|n/a: none.|
|1.20 trivial exists helper|n/a: no existential helper.|
|2.1 grind|Actually tried on whole goal; failed. Isolated `fail_if_success grind` subsequently compiled.|
|2.2 delete before grind|n/a: final proof contains no grind.|
|2.3 simpa|Direct simpa from determinant theorem tested; failed because point-free Function.update remains on one side while the other is an entrywise conditional. Keep explicit matrix congruence and extensionality.|
|2.4 fun_prop|n/a: no analytic/function-property goal.|
|2.5 positivity|n/a: determinant equality, no ordered scalar positivity conclusion.|
|2.6 gcongr|n/a: no order/monotonicity goal.|
|2.7 lia / omega|n/a: no arithmetic goal; finite indices only label columns.|
|2.8 aesop|Actually tried whole goal; failed exhaustive search. Corrected isolated probe `fail_if_success solve \| aesop` confirms nonclosure.|
|2.9 norm_num / norm_cast|n/a: no numeric computation or cast goal.|
|2.10 decide|n/a: arbitrary polynomial family over arbitrary field, not a closed decidable computation.|
|2.11 field_simp; ring|n/a: no division or denominator identity.|
|2.12 linear_combination|n/a: no terminal ring/ring_nf or scalar equation to combine.|
|2.13 wlog|n/a: equality/non-equality update cases are not symmetric; both eliminated by conditional simplification.|
|2.14 collapse calc|No calc block; analogous equality composition via `.trans` applied.|
|2.15 multiple goals|Combined by_cases/<;> simp candidate actually compiled, then improved to case-free ext/simp. No <;> needed in final proof.|
|3.1 erw|n/a: none.|
|3.2 continuity/measurability|n/a: none.|
|3.3 omega to lia|n/a: neither is relevant or present.|
|3.4 rcases rfl|Original rcases substituted automatically; entire split removed.|
|3.5 automation registration|No attribute change: conditional column-operation rewrite not needed by current automation; retain existing API attributes.|
|3.6 simp_all|n/a: final simp already closes without a context-wide simplifier.|
|3.7 limits|n/a: no heartbeat/recursion limit settings.|

## Actual experiments and step-back review

- Native live `lean_goal` confirmed exact full goal at L166.
- Native multi-attempt tested grind, expanded simp, aesop, exact?, apply?. That tool's
  line replacement leaves the rest of the multiline `have` and produces extra parse
  diagnostics. Those were not counted as valid whole-proof verification.
- Repeated the affected whole-goal probes in a self-contained scratch module defining
  only the two Wronskian constructions, without importing the target theorem.
  `fail_if_success grind`, `fail_if_success solve | simp [...]`,
  `fail_if_success solve | aesop`, and `fail_if_success exact?` all compiled before the
  candidate proof. This validates nonclosure rather than mistaking tool parse noise
  for a mathematical failure. The initial plain aesop probe was corrected because
  aesop can return unfinished goals without raising failure.
- Combined by_cases/simp compiled; removed a reported unused `Matrix.updateCol_apply`
  argument from that interim candidate. It was not the final chosen proof.
- Congruence plus one terminal conditional simp compiled, with no warnings and only
  the three standard axioms. Here `Matrix.updateCol_apply` is necessary to expose
  the conditional without explicit cases, and final diagnostics report no unused args.
- Direct simpa tested once and rejected with concrete mismatch described in rule 2.3.
- Final exact five-line proof recompiled in isolation without probe tactics. Actual
  theorem subsequently checked with `#check` and `#print axioms` after module build.
- Weaker typeclass probes fail against the current definitions; the concrete h-drop
  counterexample compiles successfully in a separate final scratch run.

Reflection: one generic determinant lemma supplies the invariant, but bare automation
cannot discover the Hasse-matrix conversion. The final proof isolates exactly that
conversion without a named intermediate fact or branches. No additional helper,
strategy rewrite, or public statement change would improve the current use.

## Verification and diff gates

| Gate | Result | Evidence |
|---|---|---|
|lake_build_file|PASS|`/Users/ramin/.elan/bin/lake build Roth.Wronskian`, session26823 exit0,1826jobs; log `/private/tmp/roth-wronskian-decl10-module.log`.|
|Complete LSP diagnostics|PASS|`partial:false`, `success:true`, `timed_out:false`, no failed dependencies; only existing three warnings outside target.|
|Isolated proof|PASS|Native `lean_run_code` final exact proof: `success:true`, `timed_out:false`, no warning/error.|
|Axioms|PASS|Actual `Roth.wronskian_update_sub_smul` and isolated candidate: `propext`, `Classical.choice`, `Quot.sound`; no sorryAx.|
|definition_protected|PASS|No def/abbrev/import/toolchain modifications.|
|theorem_statement_protected|PASS|Signature byte-identical by extraction comparison.|
|structure_gate|PASS|5 body lines, no conjunction and no branches.|
|naming_gate|PASS|Descriptive operation-based name; no forbidden pattern.|
|line_packing_gate|PASS|Two measured signature rows, no unpacked binder or complete conclusion.|
|inequality_orientation_gate|PASS|Zero reversed relations.|
|Documentation|PASS|Existing docstring intact; zero inline comments before/after.|
|Diff hygiene|PASS|`git diff --check -- Roth/Wronskian.lean` exit0; target max90 codepoints, no sorry/admit/options/instances/scaffolding.|

Overall: **PASS**. Parent owns dependent full-project and separate LeanEval gates and
publication; this worker neither edits shared logs nor commits/pushes.

## Result and checklist

Before10 declaration lines /8 body lines. After7 declaration lines /5 body lines.
Saved3 lines. Two cleanup issues fixed, no deferred refactoring, no renames.
Rules applied: composition/optional proof-have folding, dot notation, replacement of
case split by terminal conditional simplification; related 1.10,1.17,2.14,2.15,3.4.
Comments preserved: existing docstring unchanged; no inline comments present.

- [x] Step1 reference docs read.
- [x] Step2 all24 audit items answered.
- [x] Step2.5 five-method search block and limitations recorded.
- [x] Step2.6 every parameter/generalisation/literature/inversion check recorded.
- [x] Step2.7 per-line signature width table.
- [x] Step2.8 per-occurrence inequality table.
- [x] Step3 all42 golfing rules have statuses.
- [x] Step4 strategy reflection and bounded actual experiments.
- [x] Step5a complete final LSP clean of errors.
- [x] Step5b all diff gates and module build pass.
- [x] Step6a no renames required.
