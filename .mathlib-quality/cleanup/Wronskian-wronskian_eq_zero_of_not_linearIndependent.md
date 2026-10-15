# Declaration cleanup: `Roth.wronskian_eq_zero_of_not_linearIndependent`

Worker baseline: `d36d1f5`, `Roth/Wronskian.lean:63–70` (8 declaration lines, 6 proof-body lines; counting the `:= by` line gives 7). Scope: this declaration only. Existing docstring and public API preserved.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md. Also read the Lean skill, naming conventions, applicable style sections, and the authoritative Phase 4 worker contract.

## Full audit

1. **LINT:** No warning in lines 63–70. Full-file LSP completes with the existing header warning and unrelated unused `hφ`/`hd` warnings at 134/135.
2. **HAVE SCAN:** No `have` binding. The `obtain` exposes the nonzero dependence coefficient and the linear relation, both used.
3. **SET_OPTION:** No options or resource-limit changes.
4. **SIMP SQUEEZE:** Two terminal `simpa` calls at 67 and 69–70, already unsqueezed. Removing the final scalar-conversion lemma fails; `simp_all` alone does not apply the Hasse derivative to the relation.
5. **NAMING:** Descriptive conclusion-of-hypothesis theorem name: Wronskian equals zero given lack of linear independence. `linearIndependent` follows the established predicate's spelling. No forbidden abbreviation, numeric scheme, single-letter public identifier, `_ge_`, or `_gt_`; no rename.
6. **LINE PACKING:** Initial first line was underpacked (69 + 1 + 29 = 99). Moved the entire hypothesis onto it; the colon starts the next line because even the colon would yield 101. Full tables below.
7. **BY PLACEMENT:** `by` remains at the end of the conclusion line.
8. **FORMAT:** Two-space proof indentation, four-space signature continuation, no blank lines inside, no semicolon chains or consecutive rewrites. Replaced the two lambda `=>` arrows with `↦`.
9. **COMMENTS:** No proof comments to re-anchor; no comments removed. Existing three-line docstring preserved verbatim under the explicit declaration contract, including its source quotation.
10. **DOCSTRING:** Existing documentation states the easy direction over any field, distinguishing it from the later characteristic-zero converse; source reference preserved.
11. **VISIBILITY:** Public mathematical API for the characteristic-independent direction, used by `wronskian_eq_zero_iff`. Preserved under the user's current-API decision; no conversion to private.
12. **STRUCTURE:** Six body lines, two branches of one and three lines, no conjunction in the public statement. No extraction needed.
13. **MATHLIB:** Five-method block below. Existing determinant/kernel criterion and finite dependence relation are reused directly. The polynomial-Hasse relation is the additional content; this is not just a duplicate of the binary `Polynomial.wronskian` API.
14. **JUNK DEF:** n/a: theorem, no data definition.
15. **EXISTS LEMMA:** n/a: public zero-equality theorem, no trivial existential helper.
16. **SHOW vs CHANGE:** n/a: neither tactic appears.
17. **PUSH_NEG:** n/a: no negation-pushing tactic.
18. **GENERALISE:** Every parameter considered below. Weaker field parents fail against the existing definition's field contract; no approved definition change.
19. **INEQUALITY:** No order relations in statement/hypotheses; table below. No inequality-oriented rename needed.
20. **NORMAL-FORM:** Already the natural rewrite normal form `wronskian φ = 0`, with the standard `¬ LinearIndependent K φ` hypothesis.
21. **SYNTAX-GEN:** OK: callers can apply directly to their negated linear-independence hypothesis. An existential coefficient formulation would make the public call less convenient.
22. **IMPORT-FANOUT:** n/a: no imports changed or added.
23. **CASTS:** One redundant explicit target ascription dropped: `(μ : ℕ)` becomes `μ`; the genuine `Fin l → ℕ` coercion is inferred from `hasseDeriv`. No new cross-type casts or load-bearing type ascriptions introduced. `C (g ν)` remains a necessary coefficient-to-polynomial ring homomorphism, not a removable annotation.
24. **INSTANCE-NAME:** n/a: no instance declaration or local instance.

Issues fixed: two lambda arrows, one redundant type annotation, one signature packing boundary. Refactoring needed: none.

## Mathlib search status

| Method | Query/evidence | Result |
|---|---|---|
| A Lean-Finder | `Wronskian determinant vanishes linearly dependent family polynomials` (3 results) | `Polynomial.wronskianBilin_apply`, `Polynomial.isAlt_wronskianBilin`, `Polynomial.wronskian_self_eq_zero`: binary Wronskians, not this arbitrary finite Hasse matrix |
| B Loogle | `Matrix.det, LinearIndependent` (5 results) | `Matrix.det_eq_zero_of_not_linearIndependent_rows`, `_cols`, their nonzero-determinant converses, and Gram determinant result; partial matches |
| C LeanSearch | Inherited service health: HTTP 500 in this cleanup session | Unavailable, not an absence result; not repeatedly retried |
| D Source | Untruncated `rg` for full target name, `exists_mulVec_eq_zero_iff`, `det_eq_zero_of_not_linearIndependent`, `not_linearIndependent_iff`, plus Wronskian API source | Existing kernel criterion in `Matrix/ToLinearEquiv.lean`, determinant dependence in `Matrix/Determinant/Basic.lean`, coefficient relation in `LinearIndependent/Defs.lean`; binary polynomial Wronskian API in `RingTheory/Polynomial/Wronskian.lean` |
| E Native local name search | `wronskian` | Valid source hits for Roth and Polynomial APIs; symbol index reported `warming`, so no inference from missing indexed entries |

Auxiliary variants: rows/cols, nonzero determinant converses, Wronskian bilinear/alternating/zero-left/zero-right/self variants. Common-equivalents table: no discrete/finite/topological bucket applies. Initial source query named an incorrect Algebra path; corrected to the actual RingTheory path before inspecting the API.

Compiled checks verified `@Matrix.exists_mulVec_eq_zero_iff` and `@Fintype.not_linearIndependent_iff`. Live `exact?` before this declaration's body could not close it; `apply?` found only incomplete generic zero-characterizations. Conclusion: **partial matches reused**, retaining the concrete Hasse-derivative linear relation. No claim of exhaustive library absence and no replacement/public-API deletion proposed.

## Generalisation status

| Parameter | Class | Role | Mechanical candidates/drop test | Evidence/result |
|---|---|---|---|---|
| `{K : Type*}` | Type/universe | Coefficient type | Already universe-polymorphic; dropping leaves types of `φ`/linear independence unbound | No further universe weakening |
| `[Field K]` | Typeclass | Existing Wronskian definition, polynomial domain determinant criterion | `[CommRing K]`, `[DivisionRing K]`; dropping also removes required algebraic structures | Actual isolated elaboration errors at `Roth.wronskian φ`: expected the Field-based polynomial type; no live change |
| `{l : ℕ}` | Structure value/index size | `Fin l` and square matrix size | Dropping leaves `Fin l` unbound; arbitrary finite index would restate the definition/API | Retain; no caller need for a new indexing API |
| `{φ : Fin l → K[X]}` | Structure value/family | Object of both premise and conclusion | Dropping leaves `φ` unbound; abstract linear-map-family version requires a different matrix definition | Retain |
| `(h : ¬ LinearIndependent K φ)` | Proposition | Supplies nontrivial coefficient relation | Scratch drop followed by `exact?` and `simp` did not close (guarded failure probes); no pointwise or strict-to-weak variant in catalogue | Essential mathematical premise; retain |

The scratch block intentionally containing failing weakenings and a final `sorry` was only a negative experiment, never a verification gate or source edit. A separate entirely closed isolated proof succeeded, with standard axioms and exact theorem-type compatibility.

Inversion check: the determinant/kernel argument is abstract, but its closing step uses polynomial Hasse linearity and `smul_eq_C_mul`. An abstract family-of-linear-maps determinant theorem could cover this and the analogous multivariate proof in `GenWronskian.lean`; this would add public API and change organization, with no simplification necessary for the six-line proof. Closed as optional scope expansion under the user's current-API preference, not an unresolved required task.

### Public literature search

Web query: `Wronskian linearly dependent polynomials arbitrary characteristic Hasse derivatives generalization`.

Three leading research hits captured: Bostan–Dumas *Wronskians and Linear Independence* (also [author-hosted PDF](https://mathexp.eu/dumas/publications/Bostan_Dumas_2010_WLI.pdf)); *Algebraic independence over finite fields: Higher derivation based* ([search result](https://citeseerx.ist.psu.edu/document?doi=2cc8db4c436d9e5f06085d50e5b3df38c5efe642&repid=rep1&type=pdf)); *Deterministic Truncation of Linear Matroids* ([search result](https://citeseerx.ist.psu.edu/document?doi=06960c60d7740b1372e83869587a2062c1664a80&repid=rep1&type=pdf)). Opened the primary author-hosted Bostan–Dumas paper. Page 1 states the easy implication for dependent families; page 2 discusses characteristic restrictions on the converse and formal-series/rational-function variants. That supports keeping this direction free of a characteristic-zero assumption. It does not justify adding an analytic or rational-function interface here. ChatGPT math MCP: n/a, no such callable service exposed. No literature-driven change needed.

## Signature widths and inequality scan

Compiled reference at `format.width := 100`:

```lean
@Roth.wronskian_eq_zero_of_not_linearIndependent : ∀ {K : Type u_1} [inst : Field K] {l : ℕ} {φ : Fin l → K[X]},
  ¬LinearIndependent K φ → Roth.wronskian φ = 0
```

Initial table (codepoints):

| Signature line | Width | Next syntactic token | Arithmetic | Action |
|---|---:|---|---|---|
| 63 | 69 | `(h : ¬ LinearIndependent K φ)` (29) | 69 + 1 + 29 = 99 ≤ 100 | repack |
| 64 | 57 | none; proof next | n/a | ok |

Final table, measured from final source:

| Signature line | Width | Next syntactic token | Arithmetic | Action |
|---|---:|---|---|---|
| 63 | 99 | `:` (1; entire conclusion also cannot fit) | 99 + 1 + 1 = 101 > 100 | ok |
| 64 | 27 | none; proof next | n/a | ok |

| Occurrence | Location | Original | Rewrite | Name action |
|---|---|---|---|---|
| none | Full signature and all hypotheses | No `≥` or `>` | n/a | No `_ge_`/`_gt_` |

## Every golfing rule

| Rule | Status |
|---|---|
| 1.1 by exact | n/a: no wrapper |
| 1.2 by rfl | n/a: no wrapper |
| 1.3 rw + exact | n/a: no rewrite chain |
| 1.4 simp + exact | Already consolidated into terminal `simpa using` |
| 1.5 trailing rfl | n/a: none |
| 1.6 constructor/exact | Already uses anonymous existential/conjunction constructor in `refine` |
| 1.7 apply + exact | n/a: no such pair |
| 1.8 by_contra + push_neg | n/a: neither present |
| 1.9 eta reduction | Lambdas wrap `C (g ν)` and `hν₀ ?_`; neither is a direct eta redex. Composition notation gives no clarity benefit; normalized arrows |
| 1.10 single-use have | n/a: no have |
| 1.11 apply + intro | Already `refine` with lambda |
| 1.12 redundant show | n/a: none |
| 1.13 have projections | Already `obtain` destructures the coefficient relation |
| 1.14 merge rw | n/a: no rw |
| 1.15 terminal simp only | Already unsqueezed terminal simpa |
| 1.16 nonterminal simp | n/a: no nonterminal simp |
| 1.17 dot notation | `.1 h` already used for iff forward implication; remaining `congrArg`/`congrFun` calls are direct |
| 1.18 trailing parentheses | Remaining parentheses delimit required function argument `(hasseDeriv μ)` or `(g ν)`; no ending parenthesized proof |
| 1.19 push_neg | n/a: none |
| 1.20 trivial existential helper | n/a: no helper |
| 2.1 grind whole proof | Actual live attempt fails with negated Wronskian equality and `False` goal |
| 2.2 delete before grind | n/a: no successful grind proof |
| 2.3 simpa consolidation | Already consolidated; retained final two-line call; removed inferable Nat annotation after full proof check |
| 2.4 fun_prop | n/a: no analytic function property |
| 2.5 positivity | n/a: no ordered positivity goal; arbitrary field |
| 2.6 gcongr | n/a: no monotonicity inequality |
| 2.7 lia/omega | n/a: no Nat/Int arithmetic proposition |
| 2.8 aesop | Actual live whole-proof attempt made no progress |
| 2.9 norm_num/norm_cast | Actual final-goal `norm_cast` leaves matrix-vector equality; no concrete numbers to normalize |
| 2.10 decide | n/a: arbitrary field polynomial equality is not finite closed computation |
| 2.11 field_simp/ring | n/a: no denominator identity |
| 2.12 linear_combination | n/a: no ring/ring_nf ending; relation must first be transported through a linear map |
| 2.13 wlog | n/a: no symmetric cases |
| 2.14 calc term mode | n/a: no calc |
| 2.15 close several with <;> | Goals are heterogeneous: nonzero constant coefficient versus Hasse-transformed relation. Final `simp_all` experiment leaves transformed relation; keep distinct short branches |
| 3.1 erw | n/a: no erw |
| 3.2 continuity/measurability | n/a: none |
| 3.3 omega → lia | n/a: no arithmetic tactic |
| 3.4 rcases rfl | n/a: no equality substitution |
| 3.5 automation attributes | No new attribute: theorem requires a substantial negated independence premise, and no caller automation need identified |
| 3.6 simp_all | Tried unsqueezed `simp_all` on final goal; insufficient without mapping hg |
| 3.7 resource options | n/a: no options |

## Experiments and reflection

Actual live whole-proof attempts: `rfl` failed (not definitional); `simp` made no progress; `grind` failed; `aesop` made no progress; `exact?` could not close; `apply?` offered only incomplete generic zero-characterizations (not accepted as success). Final branch tests: removing the `Nat` ascription closes the mathematical goal; dropping `← smul_eq_C_mul` fails with scalar-multiplication versus `C`-multiplication mismatch; `simp_all` and `norm_cast` leave goals.

The line-based final-branch probe retained the original continuation and therefore produced an extra `unexpected token using` diagnostic. It was not treated as a complete-file pass. A separate `lean_run_code` with the entire rewritten proof returned `success: true`, no errors, and only `[propext, Classical.choice, Quot.sound]`; `example : @cleanedProof = @Roth.wronskian_eq_zero_of_not_linearIndependent := rfl` passed. That independently confirms exact signature compatibility and proof closure.

Step-back conclusion: retaining the direct nonzero kernel-vector argument is clearer than recasting dependence through column independence and restriction of scalars. The two terminal `simpa` steps represent the actual coefficient injection and linear-map application; no redundant mathematical stage or useful helper extraction remains.

## Gate status

Final source is eight declaration lines (unchanged), six body lines. Codepoint widths: 99, 27, 66, 82, 30, 10, 81, 38. No source outside the declaration changed, verified against worker HEAD by exact string comparison after masking the target. Signature is byte-identical after removing whitespace. All comments unchanged.

| Gate | Result | Evidence |
|---|---|---|
| definition_protected | pass | No definition or abbreviation touched |
| theorem_statement_protected | pass | Whitespace-normalized complete signature comparison true; compiled proof-type equality |
| structure_gate | pass | Six body lines; no conjunction; branch sizes one/three |
| naming_gate | pass | Descriptive mathematical name, no forbidden pattern |
| line_packing_gate | pass | Complete initial/final tables above; final 99-character first line |
| inequality_orientation_gate | pass | No forbidden orientation in code; full scan above |
| isolated_proof/type/axioms | pass | Separate successful `lean_run_code`, no sorry, standard axioms only |
| LSP diagnostics | pass | Full file, `partial: false`, `success: true`, no failed dependencies; only three inherited out-of-target warnings |
| diff scope and hygiene | pass | Outside-target equality true; no sorry/admit/axiom/native_decide/options; git diff whitespace check clean |
| lake_build_file | pass | `/Users/ramin/.elan/bin/lake build Roth.Wronskian`, final packed source, session 16574 exited 0; 1826 jobs, module 18 s; only inherited warnings |
| cumulative dependents | parent-owned | Full project and LeanEval checkpoint run by file owner before publication |

Renames queued: none. Refactoring needed: none. Definition/API changes: none. Comments preserved: all three docstring lines; no inline proof comments present. Before 8 lines, after 8 lines, saved 0 (clarity/style only). No new source names or imports.

Phase checklist:
- [x] Step 1 — reference docs read.
- [x] Step 2 — all 24 audit items recorded.
- [x] Step 2.5 — all five search methods accounted for.
- [x] Step 2.6 — parameter/generalisation and public literature checks recorded.
- [x] Step 2.7 — complete signature width tables recorded and repack applied.
- [x] Step 2.8 — inequality table recorded.
- [x] Step 3 — all 42 rules recorded.
- [x] Step 4 — actual experiments and reflection completed.
- [x] Step 5a — complete live diagnostics passed.
- [x] Step 5b — protection/content gates recorded; final module build result below.
- [x] Step 6a — no renames necessary.

Overall Phase 4 gates: **pass**. Source and report released to the file owner. The first pre-packing module build (session 62061) also passed, but the final gate is the separate post-packing build above.
