# Phase 4 — `Roth.wronskian`

Baseline: `046dfdf`. Target `Roth/Wronskian.lean:58`, one declaration line. No source edits.
I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md, plus relevant style and naming rules.
Lean4 and mathlib-quality skills apply. Existing docstring and public API are preserved.

## Full audit

1. **LINT:** no warning at line 58. Complete file diagnostics have only existing header
   warning at line 1 and unused `hφ`/`hd` at lines 134/135, outside this target.
2. **HAVE SCAN:** zero `have` expressions; body is `(wronskianMatrix φ).det`.
3. **SET_OPTION:** none in target; no resource limits or linter suppression.
4. **SIMP SQUEEZE:** n/a: no tactic proof or simp call.
5. **NAMING:** `wronskian` names the mathematical determinant and returns data, hence
   correct lowerCamelCase. No forbidden abbreviation, scheme number, numeric auxiliary
   suffix, single-letter public name, `_ge_`, or `_gt_`; no rename required.
6. **LINE PACKING:** one line, 80 codepoints including body; signature through `:=` 56.
   Required measured table below; no break can be repacked.
7. **BY PLACEMENT:** n/a: direct term definition, no `by`.
8. **FORMAT:** flush-left declaration; proper spaces; no blank body line, tactic chain,
   `haveI`, or `letI`. Dot notation already used.
9. **COMMENTS:** no inline comments; existing one-line docstring remains byte-identical.
10. **DOCSTRING:** documents the determinant/Hasse derivative convention and source §2;
    sufficient for this definition, preserved under existing-docstring protection.
11. **VISIBILITY:** public mathematical API; used in `GenWronskian.lean:278,284` and
    `Separation.lean:371,376,379,603`, as well as several local theorem statements.
12. **STRUCTURE:** one expression, no conjunction, cases, or branches; no extraction.
13. **MATHLIB:** partial match is binary `Polynomial.wronskian`; target names the
    arbitrary finite-family Hasse determinant using mathlib `Matrix.det`. Search below.
14. **JUNK DEF:** keep: nontrivial named mathematical object with surrounding API and
    downstream users in two other files; not a single-use convenience wrapper.
15. **EXISTS LEMMA:** n/a: data definition, no existential helper.
16. **SHOW vs CHANGE:** n/a: neither present.
17. **PUSH_NEG:** none.
18. **GENERALISE:** mechanical candidates and actual scratch outcomes below. Public
    signature remains unchanged; no currently justified coordinated refactor.
19. **INEQUALITY:** zero order relations in signature/body; table below.
20. **NORMAL-FORM:** canonical determinant of the Hasse-derivative matrix; replacing it
    with ordinary derivatives would alter factorial normalization, so preserve it.
21. **SYNTAX-GEN:** OK: explicit family argument and inferred field/length support
    current callers directly. No more convenient bundled hypothesis is present.
22. **IMPORT-FANOUT:** n/a: no new imports or file dependencies.
23. **CASTS:** 0 dropped / 0 cross-type / 0 load-bearing coercions in the empty diff.
24. **INSTANCE-NAME:** n/a: this is a definition, not an instance.

Issues to fix: none. Refactoring needed: none. No deferred rename/decomposition.

## Line packing

Actual `#check @Roth.wronskian` with `format.width := 100`:

```lean
@Roth.wronskian : {K : Type u_1} → [inst : Field K] → {l : ℕ} → (Fin l → K[X]) → K[X]
```

| Signature line | Chars through `:=` | Full line chars | Next signature token | Arithmetic | Action |
|---|---:|---:|---|---|---|
| 58 | 56 | 80 | none; body on same line | n/a, no next signature line | ok |

Python `len` measured Unicode codepoints from the current source; no edit/re-emission needed.

## Inequality scan

| Occurrence | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| none | complete line 58 | no `≥` or `>` (indeed no order relations) | n/a | none |

## Mathlib search status

- **A Lean-Finder:** `Wronskian determinant finite family polynomial Hasse derivatives`
  returned `Polynomial.wronskian`, `wronskianBilin`, and `wronskianBilin_apply`.
- **B Loogle:** `"wronskian"` returned the binary definition, self-zero, and negation
  theorems. Their signatures have two polynomial arguments, not a `Fin l` family.
- **C LeanSearch:** inherited HTTP 500 service failure in this serialized cleanup;
  unavailable, not evidence of absence; not repeatedly retried.
- **D source:** full untruncated `rg` on the pinned
  `Mathlib/RingTheory/Polynomial/Wronskian.lean` verified binary definition and API.
  Initial guessed Algebra path did not exist; corrected to the actual RingTheory path.
  Determinant Basic:60 and HasseDeriv:59 supply the existing constituent definitions.
- **E local name patterns:** `wronskian` returned both local and mathlib definitions,
  binary bilinear/add/neg/zero variants and local finite-family results. Index reported
  unavailable; positive source hits are valid, empty-index absence is not asserted.

Auxiliary variants inspected: `wronskianBilin`, `wronskianBilin_apply`, `_self_eq_zero`,
`_neg_eq`, `_add_left`, `_add_right`, `_zero_left`. Common-equivalents lookup: no bucket.
Actual compiled `#check @Polynomial.wronskian` confirms
`{R : Type u_1} → [CommRing R] → R[X] → R[X] → R[X]`.
Actual `#check @Matrix.det` confirms its CommRing/Fintype/DecidableEq API.
Conclusion: partial match; keep the named finite-family definition already built directly
on `Matrix.det`. No universal absence claim, no new wrapper theorem, no bridge API.
`exact?` and `apply?` on the defining equality both compile and suggest
`coeff_inj.mp rfl`; the direct defining term is clearer and shorter than introducing
that redundant theorem proof. Definitional equality itself separately passes by `rfl`.

## Generalisation status

| Binder | Kind | Mechanical candidates checked | Verified? | Result |
|---|---|---|---|---|
| `{K : Type*}` | type variable | drop; universe widening | dependency inspection; original #check compiled | K occurs in family and result; already universe-polymorphic |
| `[Field K]` | typeclass | drop; DivisionRing; CommRing; CommSemiring | yes, isolated Lean code | dropping lacks Semiring; DivisionRing/CommRing with unchanged body fail because wronskianMatrix needs Field; expanded CommSemiring lacks CommRing for determinant |
| `{l : ℕ}` | value/index | drop; abstract finite index | dependency inspection | Fin l determines square matrix and derivative order; removing l does not preserve this signature; arbitrary indexing needs an order/row-order assignment and API restatement |
| `(φ : Fin l → K[X])` | function/data | drop; point-localize | dependency inspection | φ is the input to the determinant; no propositional global/pointwise premise to weaken |
| none | proposition/structure-value/decidability hypotheses | drop, unbundle, strict→weak | n/a | none explicitly supplied; Fin supplies finite decidable indexing |

Scratch positive experiment:

```lean
noncomputable def broad {K : Type*} [CommRing K] {l : ℕ}
    (φ : Fin l → K[X]) : K[X] :=
  (Matrix.of fun μ ν : Fin l ↦ hasseDeriv μ (φ ν)).det
example {K : Type*} [Field K] {l : ℕ} (φ : Fin l → K[X]) :
    broad φ = Roth.wronskian φ := rfl
```

This compiles. A coordinated generalisation of wronskianMatrix and wronskian could
support CommRing, but no current caller needs it. Under the authorized API-preserving
scope, this optional exploration is closed without a pending task or applied change.
`CommRing + IsField` is a rebundling requiring API restatement with no caller benefit;
no application. Inversion check: n/a to abstract proof extraction, since this is the
named data construction itself, not a theorem hiding a generic proof after unfolding.

## Literature search status

**A WebSearch:** query `Wronskian Hasse derivatives determinant polynomials generalization`.
Top three returned entries: [On one generalization of Wronskian](https://journals.vu.lt/LMR/en/article/view/25246),
its [alternate journal host](https://www.journals.vu.lt/LMR/en/article/view/25246), and
[On Generalized Wronskians](https://www.impan.pl/~pragacz/gatto2.pdf).
Additional directly relevant primary result:
[Subspace designs, preliminaries](https://www.math.toronto.edu/swastik/subspace-designs.pdf)
discusses switching ordinary and Hasse derivatives by factorial factors when those
factors are nonzero. This supports retaining the explicit Hasse normalization.
Generalized Wronskians allow other derivative selections; that is a different API,
not a required correction to the present consecutive-order determinant.
**B ChatGPT math MCP:** n/a: no such tool exposed in this session.
Literature-driven mandatory changes: none; optional broadening disposition above.

## Golfing rule pass (all 42)

| Rule | Status and concrete reason |
|---|---|
| 1.1 by exact | n/a: direct term already |
| 1.2 by rfl | n/a: no proof wrapper |
| 1.3 rw+exact | n/a: no tactics |
| 1.4 simp+exact | n/a: no tactics |
| 1.5 trailing rfl | n/a: no tactics |
| 1.6 constructor pair | n/a: determinant value, no conjunction |
| 1.7 apply+exact | n/a: direct term already |
| 1.8 by_contra | n/a: no contradiction proof |
| 1.9 eta-reduce | n/a: no lambda in target |
| 1.10 inline have | n/a: no have |
| 1.11 apply+intro | n/a: no tactics |
| 1.12 show | n/a: no show |
| 1.13 have projections | n/a: none |
| 1.14 merge rw | n/a: no rw |
| 1.15 terminal simp only | n/a: no simp |
| 1.16 nonterminal simp | n/a: no simp |
| 1.17 dot notation | already `(wronskianMatrix φ).det` |
| 1.18 less parentheses | n/a: parentheses enclose receiver for dot notation |
| 1.19 push Not | n/a: no push_neg |
| 1.20 exists helper | n/a: data definition |
| 2.1 grind | n/a: data construction, not a proof goal; tactic synthesis could choose a different polynomial |
| 2.2 delete before grind | n/a: no grind |
| 2.3 simpa consolidation | n/a: no simp chain |
| 2.4 fun_prop | n/a: no analytic property goal |
| 2.5 positivity | n/a: no positivity goal |
| 2.6 gcongr | n/a: no inequality goal |
| 2.7 lia/omega | n/a: no arithmetic proposition |
| 2.8 aesop | n/a: data definition, not a logic proof |
| 2.9 norm_num/norm_cast | n/a: no numeric or cast goal |
| 2.10 decide | n/a: no decidable proposition |
| 2.11 field_simp/ring | n/a: no denominator equality |
| 2.12 linear_combination | n/a: no equality proof or hypotheses |
| 2.13 wlog | n/a: no branches |
| 2.14 calc | n/a: no calc |
| 2.15 multiple goals | n/a: no proof goals |
| 3.1 erw→rw | n/a: no erw |
| 3.2 continuity | n/a: no legacy analysis tactic |
| 3.3 omega→lia | n/a: no omega |
| 3.4 rcases rfl | n/a: no rcases |
| 3.5 attributes | n/a: definition already has its dedicated theorem API; no automation theorem added |
| 3.6 simp_all | n/a: no simp_all |
| 3.7 resource options | n/a: no options |

## Reflection and verification

Term mode already supplies the shortest clear mathematical construction. There are no
intermediate facts, redundant steps, or proof branches to compress. Replacing the body
with automation is inappropriate for a data definition. Actual `exact?`/`apply?`
experiments target its defining equality, not unconstrained polynomial synthesis.

- `lake build Roth.Wronskian` session 3061 exited 0; 1826 jobs, inherited warnings only.
- Native complete `lean_diagnostic_messages` returned `success:true`, `partial:false`,
  `timed_out:false`, no failed dependencies, zero errors, the three known file warnings.
- Native `lean_run_code` with imported compiled target returned `success:true` for
  type checks, defining rfl, exact?/apply?, and the CommRing scratch comparison.
- `#print axioms Roth.wronskian`: only `propext`, `Classical.choice`, `Quot.sound`.
- `git diff -- Roth/Wronskian.lean` empty against worker start; source never mutated.
- Negative weakening scratch checks intentionally fail as documented and are not source edits.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | actual command above, exit 0 |
| definition_protected | pass | definition/signature/body byte-identical |
| theorem_statement_protected | pass | no theorem edits |
| structure_gate | pass | one-line term, no conjunction or branches |
| naming_gate | pass | mathematical lowerCamelCase, no forbidden patterns |
| line_packing_gate | pass | measured single-line table, 80 total codepoints |
| inequality_orientation_gate | pass | complete scan table, zero reversed relations |
| type/definition preservation | pass | unchanged source plus compiled rfl |
| axiom gate | pass | only three standard axioms |

Overall: pass. Before 1 line; after 1 line; saved 0. Audit issues 0; fixed 0;
refactoring deferred 0. Rules applied: none needed. Renames queued: none.
Comments preserved: 1 of 1 docstring, no inline comments. Refactoring needed: none.
Full project and separate LeanEval checkpoint builds belong to the parent.

## Phase checklist

- [x] Step 1 reference docs read.
- [x] Step 2 all 24 audit items answered.
- [x] Step 2.5 five-method search status, including truthful service limitation.
- [x] Step 2.6 mechanical generalisation, experiments, inversion and public literature.
- [x] Step 2.7 every signature line measured.
- [x] Step 2.8 inequality table complete.
- [x] Step 3 every one of 42 rules has a status and reason.
- [x] Step 4 reflection and applicable experiments completed.
- [x] Step 5a complete LSP success, no target warning.
- [x] Step 5b actual module build and all diff gates pass.
- [x] Step 6a no rename needed; shared sidecar untouched.
