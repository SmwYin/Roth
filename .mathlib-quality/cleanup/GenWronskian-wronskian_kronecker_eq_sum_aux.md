# Phase 4 — wronskian_kronecker_eq_sum_aux (fresh helper audit)

Additional extracted-helper audit only: no original-declaration tally credit. Initial helper
L230–244, 15 declaration lines / 9 proof lines. Final candidate: 8 declaration lines / 3 proof
lines, saving 7 declaration lines. Own source edits were restricted to the private helper
and the owner's explicitly authorized sole caller adaptation. No Git operations, shared-log
changes, full build, LeanEval build, new helper, new import, definition change or public API
change. Source ownership was revoked after initial module/LSP checks; final packing is owned
by the parent. Final certification status is recorded below.

Read the complete installed lean4 and mathlib-quality skills, complete worker contract,
golfing-rules, proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates,
naming-conventions, mathlib-review-stages and relevant style-rules sections. Native LSP
tools were discovered through ALL_TOOLS metadata and used before shell verification.

## Full audit (24 items)

1. LINT: no helper warning. Five inherited warnings outside its range are listed below.
2. HAVE SCAN: initial `hM : ... := by` at L237 has proof content and one use in the rewrite;
   keeping it would satisfy the rule. Instead the whole matrix equality is absorbed by
   terminal `simpa`. No no-by single-use have occurs, and none remains in the final body.
3. SET_OPTION: none in the helper; no resource option or suppression added.
4. SIMP SQUEEZE: initial proof has no simp. Final simpa is terminal, deliberately unsqueezed.
5. NAMING: snake_case with mathematical subject and equality-to-sum conclusion; private
   `_aux` is unnumbered. No forbidden abbreviation/pattern or single-letter public name.
6. LINE PACKING: every initial/final signature line measured below. One missed packing
   opportunity was reported after freeze; parent accepted its correction. Final five-line
   candidate signature has no remaining repack row.
7. BY PLACEMENT: `:= by` stays at the end of the last signature line.
8. FORMAT: two-space proof indentation, no empty declaration lines, one tactic per line,
   ↦ lambdas; no haveI/letI, redundant parentheses or consecutive rw calls remain.
9. COMMENTS: none inside this helper; all surrounding docs/comments preserved verbatim.
10. DOCSTRING: n/a: private helper has no docstring and needs none.
11. VISIBILITY: private + `_aux`, used only by the headline result in this file.
12. STRUCTURE: 9 proof lines become 3; no conjunction, case split or branch. The helper
    retains the meaningful derivative/substitution determinant expansion so the public
    headline stays at 13 proof lines. Deleting the helper would regress that structure.
13. MATHLIB: five actual methods below found determinant transport API, now used directly.
    No exact replacement for the project-specific Wronskian/substitution identity established.
14. JUNK DEF: n/a: proposition lemma, not a data definition.
15. EXISTS LEMMA: n/a: equality theorem, not trivial witness packaging.
16. SHOW vs CHANGE: n/a: neither tactic occurs.
17. PUSH_NEG: n/a: no negation tactic.
18. GENERALISE: point-localized hc from every polynomial to the supplied family. Owner
    approved after both formulations compiled. All parameters/catalogue checks below.
19. INEQUALITY: no ≥ or > in signature/hypotheses, and no _ge_/_gt_ name. Scan below.
20. NORMAL-FORM: RHS is the determinant's standard finite row-choice expansion, with the
    coefficient product outside the substituted generalized determinant. No competing
    equivalence form or simp normal form introduced.
21. SYNTAX-GEN: OK: localized hypothesis is easier to establish when only this family is
    known. Uniform existing caller specializes with `fun μ ν ↦ hc μ (φ ν)`.
22. IMPORT-FANOUT: n/a: no imports added.
23. CASTS: 0 dropped / 0 explicit cross-type casts kept / 0 explicit load-bearing casts
    kept in the diff. Fin→ℕ coercion in hasseDeriv is genuine and remains implicit.
24. INSTANCE-NAME: n/a: no instance declaration or new local instance.

Issues fixed: explicit matrix-equality/sum-congruence/ring-hom coercion scaffolding;
overly uniform hc; one signature packing opportunity. No rename queued. No additional
helper extracted. Public statements, docstrings and definition values are protected.

## Mathlib search status — all five actual methods

| Method | Query | Actual result |
|---|---|---|
| A Lean-Finder | determinant of matrix rows that are sums of scalar multiples expands over row choices | Returned Matrix.sum_cramer, Matrix.det_updateRow_sum, determinant row-addition variants; these concern one replaced row or row operations |
| B Loogle | `RingHom, Matrix.det` | Returned RingHom.map_det and polynomial determinant variants |
| C LeanSearch | A ring homomorphism commutes with the determinant of a matrix | Returned AlgHom.map_det, RingHom.map_det, RingEquiv.map_det |
| D source grep | full helper name; map_det; aeval/det variants in matrix determinant and MvPolynomial sources | Full helper name absent from Mathlib text; Basic.lean:318–332 supplies RingHom/AlgHom/RingEquiv/AlgEquiv transport |
| E local name | map_det; Matrix.map | Returned AlgHom.map_det, RingHom.map_det and Matrix.map definitions; index warming, so empty/name absence was never inferred |

Auxiliary variants checked: algebra/ring hom and equivalence map_det, determinant row update
and sum_cramer, Matrix.map and map_apply. The common-equivalents lookup has no matching
discrete/finiteness/separation/bornology construction. Successful remote results were used;
no outage was interpreted as absence.

Six strict rules checked: use actual Mathlib determinant transport directly; search all
five methods and generic routes; inspect auxiliary variants; use existing typeclasses;
no exact duplicate established to delete; no new dependency/docstring change needed.
This extracted identity composes the project row-expansion theorem with derivative
substitution and determinant transport. It is retained as the mathematically meaningful
expansion used by the headline proof, per the owner's explicit scope/structure decision.
No claim that grep proves absence. Live exact? failed, apply? suggested only polynomial
extensionality/other partial routes. The independent initial-type proof below explicitly
uses det_sum_rows and AlgHom.map_det and does not reference this helper.

## Generalisation status — every parameter

| Parameter | Class | Mechanical candidates / evidence | Result |
|---|---|---|---|
| `{K : Type*}` | carrier | Drop cannot preserve the coefficient/polynomial types; already independent universe-polymorphic Type* | Keep |
| `[Field K]` | typeclass | Drop/CommSemiring cannot supply Field argument of genWronskian; actual CommRing probe failed at genWronskian; DivisionRing probe failed synthesizing CommSemiring K and commutative polynomial instances | Keep; upstream definitions would need restatement to weaken |
| `{σ : Type*}` | carrier | Occurs in MvPolynomial and multi-index types; dropping changes the objects; universe already independent Type* | Keep |
| `[Fintype σ]` | representation/data | Actual drop probe failed synthesizing Fintype σ at kronecker occurrences; Finite alone supplies no chosen enumeration used by kronecker | Keep; changing chosen enumeration is a different statement |
| `{l : ℕ}` | index data | Determines every Fin l and determinant size; no predicate/drop candidate. General finite indexing would also need row-order values for hasseDeriv | Keep |
| `(k : ℕ)` | data | Determines kronecker substitution; dropping/replacing by abstract order loses natural-power substitution data | Keep |
| `(φ : Fin l → MvPolynomial σ K)` | family data | Supplies every derivative argument and both Wronskians; removing binder merely makes same required data implicit | Keep |
| `(s : Fin l → Finset (σ →₀ ℕ))` | finite-support data | Determines hc sum and piFinset RHS. No redundant proposition/drop or smaller local predicate | Keep |
| `(c : Fin l → (σ →₀ ℕ) → Polynomial K)` | coefficient data | Determines hc coefficients and RHS product; cannot remove while preserving expression | Keep |
| `hc` | proposition | Drop test leaves mismatch between Hasse-derivative matrix and arbitrary row sum; actual clear-hc probe reports that matrix mismatch. Point-local replacement ∀ μ ν proved independently and accepted by owner | Applied point-localization |

No DecidableEq parameter is inherited; `classical` provides internal decisions. No strict
inequality, positivity assumption, analytic/global predicate or bundled conjunction exists,
so those weakening catalogue entries do not apply. Proposition strict→weak and unbundling
are n/a for an equality identity. No carrier or data binder can be deleted without changing
the expressed objects; these are not unused logical assumptions.

Inversion check: after unfolding, concrete kronecker-specific algebra is absent; generic
core content already lives in det_sum_rows and AlgHom.map_det. An arbitrary algebra-hom
transport theorem would specialize those same APIs. No additional generic wrapper is
introduced; the private identity expresses the specific expansion needed by the public
argument. Literature search: n/a: private declaration, literature search not required.
Big-change candidates: none left for this helper; hc localization and its caller adjustment
were explicitly approved before writing. Upstream Field/finite-index restatements are
outside this private-helper audit and not asserted necessary mathematical assumptions.

## Signature packing and inequality scan

Reference: `#check @initial_type_reproof` with `format.width 100`, compiled against the
exact initial uniform-hc type. Exact output appears in certification evidence below.
Widths include indentation and count Unicode codepoints, not UTF-8 bytes. Next token is
the complete next mathematical expression/binder, not a fragment of an identifier.

Initial six-line signature widths were 83, 71, 68, 56, 69, 61. Localized six-line
intermediate widths were 83, 71, 70, 60, 69, 61. The fourth intermediate line could accept
the entire 37-character Wronskian LHS: 60 + 1 + 37 = 98, then ` =` reaches exactly 100.
This was corrected by the owner after I reported it under revoked source ownership.

| Final sig line | Chars | Next complete expression width | Arithmetic | Action |
|---|---:|---|---|---|
| 230 | 83 | `(s : Fin l → Finset (σ →₀ ℕ))`, 29 | 83 + 1 + 29 = 113 > 100 | ok |
| 231 | 71 | hc binder through equality `=`, 66 | 71 + 1 + 66 = 138 > 100 | ok |
| 232 | 70 | hc sum expression through closing binder, 52 | 70 + 1 + 52 = 123 > 100 | ok |
| 233 | 100 | `∑ f ∈ Fintype.piFinset s,`, 25 | 100 + 1 + 25 = 126 > 100 | ok |
| 234 | 85 | none, proof next | n/a | ok |

| Region | ≥ occurrences | > occurrences | Action |
|---|---:|---:|---|
| Entire signature and every hypothesis | 0 | 0 | no rewrite |
| Name _ge_ / _gt_ | 0 | 0 | no rename |

## Golfing rule pass — every rule (42)

| Rule | Status |
|---|---|
| 1.1 by exact | n/a: no such wrapper |
| 1.2 by rfl | n/a: no pure rfl proof |
| 1.3 rw + exact | replaced entire rewrite proof with simpa using |
| 1.4 simp + exact | applied simpa consolidation using determinant expansion |
| 1.5 trailing rfl | applied: explicit terminal rfl removed with map/unfold simplification |
| 1.6 anonymous constructor | n/a: no constructor goal |
| 1.7 apply + exact | n/a: no chain |
| 1.8 by_contra! | n/a: no contradiction |
| 1.9 eta reduction | n/a: all final lambda binders select genuinely different row/multi-index/column arguments |
| 1.10 single-use have | hM has by proof and was permitted to remain; whole proof consolidation removes it |
| 1.11 refine + fun | n/a: no apply/intro chain |
| 1.12 redundant show | n/a: no show |
| 1.13 obtain | n/a: no projections/destructuring |
| 1.14 merge rw | n/a: initial rw calls separated by sum congruence; final no rw |
| 1.15 terminal simp only | n/a: final terminal simpa unsqueezed |
| 1.16 nonterminal simp | n/a: none |
| 1.17 dot notation | generic AlgHom.map_det is passed as a simplifier lemma, not direct application |
| 1.18 <\| | n/a: using application has no dispensable final parentheses |
| 1.19 push Not | n/a: no push_neg |
| 1.20 trivial exists helper | n/a: equality expansion, no witness |
| 2.1 grind | actual live attempt failed on entire identity |
| 2.2 preceding grind | n/a: no retained grind |
| 2.3 simpa | applied: full determinant rewrite transported in terminal simpa |
| 2.4 fun_prop | n/a: no topological/analytic property |
| 2.5 positivity | n/a: equality, no positivity/nonzero subgoal |
| 2.6 gcongr | n/a: no inequality/monotonicity |
| 2.7 lia/omega | n/a: no Nat/Int arithmetic proposition |
| 2.8 aesop | actual live attempt failed, no progress |
| 2.9 norm_num/norm_cast | n/a: no concrete numeric/cast identity |
| 2.10 decide +kernel | n/a: arbitrary-field identity with universal hypothesis, not finite computation |
| 2.11 field_simp; ring | n/a: no denominators or rational identity |
| 2.12 linear_combination | n/a: no ring/ring_nf conclusion; finite determinant transport required |
| 2.13 wlog | n/a: no symmetric branches |
| 2.14 calc term | n/a: no calc |
| 2.15 <;> | n/a: final proof has one goal, no similar branches |
| 3.1 erw→rw | n/a: no erw |
| 3.2 fun_prop | n/a: no continuity/measurability |
| 3.3 omega→lia | n/a: no arithmetic tactic |
| 3.4 rcases rfl | n/a: no rcases |
| 3.5 automation registration | no attribute: RHS introduces s/c-dependent expansion and private local hypothesis; not a canonical global simp rule |
| 3.6 simp_all | n/a: no simp_all only |
| 3.7 resource options | n/a: no maxHeartbeats/maxRecDepth option |

Step back: tried whole-proof grind/simp/aesop/exact?/apply?; none established a complete
independent proof. apply? produced partial polynomial extensionality routes. A scratch
`fail_if_success (solve | apply?)` probe unexpectedly considered such partial suggestions
successful and introduced sorryAx; that scratch was rejected, never source verification.
The independent clean reproof below omits all search tactics and has exactly standard axioms.
Terminal simp initially failed to identify mapped matrices; adding Matrix.map normalizes
them and succeeds. AlgHom.map_det removes the old RingHom coercion round-trip. The final
strategy is determinant multilinearity plus algebra-hom naturality; no new abstraction needed.

## Verification and gates

Initial source SHA256: cbd1564dda27d17e67feacd0712e035fdfd0feeeefe920d6f7603cee970bade8.
Intermediate source SHA256: df3cbe90e0748ef20cd204d41d0c95decbd10ad0de9198403d0d9f2547a2a6d3.
Packed candidate SHA256: 175ce6a3ece377484ccf54ad54479d3f79e425080364fbbcbe635484a9d482c9.
Packed complete source snapshot: `/private/tmp/wronskian-helper-packed-full.lean`.

At the intermediate hash, `/Users/ramin/.elan/bin/lake build Roth.GenWronskian` exited 0,
module built in 19s, 1838 jobs. Complete native lean_diagnostic_messages returned
success=true, partial=false, timed_out=false, errors=0, failed_dependencies=[]. Five inherited
file warnings: copyright header; unused Fintype section variable in
genWronskian_eq_zero_of_not_linearIndependent; unused Fintype-in-type for that theorem;
unused DecidableEq-in-type for det_sum_rows; unused Fintype-in-type for the headline.
No helper warning. No suppressions or resource changes.

Final packed-source module/LSP gates: owner revalidated source SHA256
175ce6a3ece377484ccf54ad54479d3f79e425080364fbbcbe635484a9d482c9.
`/Users/ramin/.elan/bin/lake build Roth.GenWronskian` exited 0 (module 19s, 1838 jobs),
log `/private/tmp/roth-helper-wronskian-packed-module.log`. Complete native LSP returned
success=true, partial=false, timed_out=false, errors=0, failed_dependencies=[], same five
inherited warnings and no helper warning; artifact
`/private/tmp/roth-helper-wronskian-packed-lsp.json`. Both artifacts were read directly
and the final source hash checked. No subsequent source writes by this worker.
The owner's full-project/separate LeanEval/cumulative checks are recorded in its file report.

`/Users/ramin/.elan/bin/lake env lean /private/tmp/wronskian-helper-certification.lean`
exited 0. Its initial-type theorem is copied from the initial helper's uniform-hc signature
and independently proved using det_sum_rows plus terminal simpa. No target/helper reference
occurs in that proof. It checks `#check` at format.width 100 and `#print axioms`.
An initial scratch ppExpr call used the wrong elaboration monad; repaired isolated command
uses Command.liftTermElabM. The successful command discovers the actual built private Name
object from the environment and passes that object directly to Lean.collectAxioms.

```text
@initial_type_reproof : ∀ {K : Type u_3} [inst : Field K] {σ : Type u_4} [inst_1 : Fintype σ] {l : ℕ} (k : ℕ)
  (φ : Fin l → MvPolynomial σ K) (s : Fin l → Finset (σ →₀ ℕ)) (c : Fin l → (σ →₀ ℕ) → Polynomial K),
  (∀ (μ : Fin l) (P : MvPolynomial σ K),
      (Polynomial.hasseDeriv ↑μ) ((kronecker k) P) = ∑ d ∈ s μ, c μ d * (kronecker k) ((hasseDeriv d) P)) →
    (wronskian fun ν ↦ (kronecker k) (φ ν)) =
      ∑ f ∈ Fintype.piFinset s, (∏ μ, c μ (f μ)) * (kronecker k) (genWronskian f φ)
'Roth.initial_type_reproof' depends on axioms: [propext, Classical.choice, Quot.sound]
BUILT _private.Roth.GenWronskian.0.Roth.wronskian_kronecker_eq_sum_aux:
  [propext, Classical.choice, Quot.sound]
```

The actual helper type was intentionally weakened privately. The original type is recovered
by specializing its uniform hc as `fun μ ν ↦ hc μ (φ ν)`, exactly as in the sole caller.
It is not claimed that the helper's old and new types are identical. All public signatures
and docs and all definition values remain byte-identical.

| Gate | Status | Evidence |
|---|---|---|
| lake_build_file | pass | final packed hash module exited 0; log above |
| definition_protected | pass | no def/abbrev edit |
| theorem_statement_protected | pass with authorized private weakening | only hc point-localized; public headline signature unchanged |
| structure_gate | pass | 3 proof lines, no conjunction/branch; headline remains 13 |
| naming_gate | pass | descriptive unnumbered _aux; no rename |
| line_packing_gate | pass on candidate | all five final lines and arithmetic above |
| inequality_orientation_gate | pass | zero reversed inequalities |
| comments/docs protected | pass | no comment/doc edit |
| axioms/original type | pass | independent original reproof and actual built helper std3 |

## Required phase checklist (11)

- [x] Step 1 — mandatory references read.
- [x] Step 2 — all 24 audit items reported.
- [x] Step 2.5 — all five actual mathlib-search methods, strict rules and generic probes.
- [x] Step 2.6 — every parameter, point-localization and inversion analysis.
- [x] Step 2.7 — full final signature width/arithmetic table.
- [x] Step 2.8 — inequality scan table.
- [x] Step 3 — all 42 golfing-rule statuses.
- [x] Step 4 — step-back alternatives evaluated.
- [x] Step 5a — final packed-hash complete LSP, artifact read and verified.
- [x] Step 5b — final packed-hash module gate, artifact read and verified.
- [x] Step 6a — no rename required; no shared sidecar write.

Refactoring needed: none after the accepted packing correction. Helper audit complete:
15→8 declaration lines, 9→3 proof lines, all worker gates pass, all eleven checks complete.
No increment to original declaration counts. No routine work pending for this helper audit.
