# Cleanup: `MvPolynomial.coeff_taylor_monomial_aux`

Private helper added during Taylor decomposition; this audit does not increment the original
264-declaration count. Scope: `Roth/Taylor.lean`, original L114–124, final L114–123.
Only the helper body changed. All statements, definitions, documentation and other declarations
were preserved. Source frozen at whole-file SHA256
`61807d7fe836eb95dbcea48055b0c9a5f5747d3c98b8d15f0d82fe33aee3f81d`.

## References and proof

Read both Lean4 and mathlib-quality skills, the complete supplied Phase-4 worker contract,
golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md,
cleanup-gates.md, relevant style-rules.md sections, and mathlib-review-stages.md.
Naming has no flagged pattern requiring additional naming investigation.

The proof inducts on the finite support of the monomial exponent. The zero exponent is a
constant polynomial: derivative order zero simplifies, and positive derivative order uses
the existing `hasseDeriv_C`. The support extension case uses the independently audited
`coeff_taylor_monomial_single_add_aux`. Induction generalizes the coefficient index `d`.

## Full audit

1. **LINT:** No target diagnostics. Complete final file diagnostics contain only the known
   L1:2 missing-copyright warning, explicitly left unchanged by the user.
2. **HAVE SCAN:** No `have` declarations in the target, before or after.
3. **SET_OPTION:** No source options or resource-limit changes.
4. **SIMP SQUEEZE:** Original two terminal `simp` calls were unsqueezed already. Final
   `simp` and `simp [← C_apply, hasseDeriv_C hd, hd.symm]` both close their branches;
   no nonterminal bare simp remains.
5. **NAMING:** Descriptive snake_case, private `_aux`, no numeric suffix, forbidden
   abbreviation, scheme number, `_ge_`, or `_gt_`; no rename needed.
6. **LINE PACKING:** Both signature lines measured below; unchanged and within 100 codepoints.
7. **BY PLACEMENT:** `:= by` ends the conclusion line.
8. **FORMAT:** Two-space tactic indentation; no internal blank lines, chained distinct
   tactics, `haveI`, or `letI`. Existing single-add exact fits in 91 codepoints.
9. **COMMENTS:** None in this helper; surrounding documentation unchanged.
10. **DOCSTRING:** Private auxiliary, no docstring required or added.
11. **VISIBILITY:** Already private, only used by the following main theorem.
12. **STRUCTURE:** Body 9→8 lines; longest branch 3 tactic lines. No conjunction or large
    branch; no extraction necessary.
13. **MATHLIB:** Five-method search recorded below. The univariate Taylor coefficient result
    is a partial mathematical match; the local multivariate proof still needs support induction.
    Existing project constant-derivative API replaces manual coefficient reasoning.
14. **JUNK DEF:** n/a: lemma, no definition introduced.
15. **EXISTS LEMMA:** n/a: equality, not a witness wrapper.
16. **SHOW vs CHANGE:** n/a: neither appears.
17. **PUSH_NEG:** n/a: none appears.
18. **GENERALISE:** Per-parameter analysis and actual failed drop/weaken probes below.
19. **INEQUALITY:** No reversed inequalities; scan table below.
20. **NORMAL-FORM:** Coefficient translated on the left, evaluated Hasse derivative on the
    right, matching the project's canonical Taylor coefficient formulation.
21. **SYNTAX-GEN:** OK: explicit translation, coefficient index, exponent and scalar match
    the immediate monomial-induction caller. No easier equivalent interface identified.
22. **IMPORT-FANOUT:** n/a: no source imports changed.
23. **CASTS:** 0 dropped / 0 kept cross-type / 0 kept load-bearing in the diff.
24. **INSTANCE-NAME:** n/a: no instance declarations.

Issue fixed: unnecessary manual constant-case coefficient expansion. No deferred refactoring.

## Mathlib search status

| Method | Query and result |
|---|---|
| A — Lean-Finder | `multivariate polynomial coefficient translation Hasse derivative monomial`: returned univariate `Polynomial.hasseDeriv_coeff`, `hasseDeriv_monomial`, `hasseDeriv_apply`; no direct multivariate replacement. |
| B — Loogle | `MvPolynomial.coeff, MvPolynomial.eval` failed with unknown-identifier query error; bounded fallback `"coeff", "eval"` returned univariate coefficient-zero/evaluation lemmas. This query failure is not absence evidence. |
| C — LeanSearch | `coefficient of translated multivariate monomial equals evaluation of Hasse derivative`: service recovered and returned `Polynomial.taylor_coeff`, `MvPolynomial.mkDerivation_monomial`, and `Polynomial.hasseDeriv`. No HTTP 500 in this worker's call. |
| D — source | Full untruncated mathlib search for `coeff_taylor_monomial_aux`, `coeff_taylor`, `taylor_monomial`; hits were univariate Taylor lemmas. Searched MvPolynomial directories and project HasseDeriv for constant and zero variants. |
| E — local names | `hasseDeriv_C` returned project `MvPolynomial.hasseDeriv_C` and univariate/series variants. Index was `warming`; results establish these names, not absence of other names. |

Auxiliary variants: constant derivative, coefficient zero, monomial derivative, Taylor monomial,
support induction. Common-equivalents table: no matching discrete/finite/topological bucket.
Verified `@hasseDeriv_C` and `@Finsupp.induction` using Lean. `Polynomial.taylor_coeff`
is not imported in the current prefix (an explicit `#check` failed); a separate snippet
importing `Mathlib.Algebra.Polynomial.Taylor` verified its semiring/univariate type.
No source import was added because it does not replace this multivariate statement.

Compiled pre-target `exact?` failed to close the goal. `apply?` returned only
`Finsupp.apply_eq_of_mem_graph` with graph-membership remaining and a generated-sorry warning;
this is rejected as an incomplete proof despite the tool's overall success flag.
Conclusion: partial univariate match, not an exhaustive global absence claim. Keep the local
multivariate induction and reuse the project constant-derivative API. No custom predicates,
wrapper definition, casting round-trips, or missing-API extraction signal remains.

## Generalisation status

| Parameter | Class | Use | Mechanical candidates / verification | Result |
|---|---|---|---|---|
| `{σ : Type*}` | type variable | Variable index domain of α, d, k | Universe polymorphism already present; removing the domain makes the dependent parameter types ill-formed. No point/strict catalogue entry applies to a type. | Retain arbitrary universe. |
| `{R : Type*}` | type variable | Coefficient domain | Universe polymorphism already present; deleting the domain destroys α/a/CommSemiring types. No narrower structure-value hypothesis to weaken. | Retain arbitrary universe. |
| `[CommSemiring R]` | typeclass | Required by taylor, eval, hasseDeriv and the prior helper | Actual separate pre-target probes outside the inherited section: drop, then `Semiring R`. Both fail synthesizing `CommSemiring R` in the statement. Further parent weakening cannot supply this missing class. | Retain. |
| `(α : σ → R)` | structure value | Translation and evaluation | Actual drop with scratch-only autoImplicit=false fails unknown identifier α. No point-localization: arbitrary translation coordinates are part of the result. | Retain. |
| `(d : σ →₀ ℕ)` | structure value | Coefficient / derivative order | Actual drop fails unknown identifier d. Generalizing ℕ-valued polynomial exponents changes the mathematical object, not a mechanical weakening. | Retain. |
| `(k : σ →₀ ℕ)` | structure value | Monomial exponent, induction variable | Actual drop fails unknown identifier k. Same exponent-domain restriction. | Retain. |
| `(a : R)` | structure value | Scalar monomial coefficient | Actual drop fails unknown identifier a. Its type already follows arbitrary R. | Retain. |

No proposition hypotheses, strict inequalities, decidability parameters, bundled maps, or
pointwise/global analysis assumptions occur. `classical` is a proof tactic, not a hypothesis:
removing it from the simplified candidate leaves `(C a).coeff d = 0` unsolved; retained.
All mutation probes were isolated `lean_run_code` snippets, not edits to the live signature.
Thus these are compiler-diagnostic experiments, not claims of live-file LSP mutation checks.
No generalisation applied. Big-change candidates: none. Inversion check: not applicable;
the statement already concerns arbitrary types and arbitrary input data, and the proof uses
the specific monomial/translation structure throughout its two branches.

Literature search: n/a: private decl, literature search not required. Neither web nor
math-consultation literature calls were needed for this private helper.

## Line packing

Lean `#check @coeff_taylor_monomial_aux` under scratch-only `format.width := 100`:

```lean
@coeff_taylor_monomial_aux : ∀ {σ : Type u_3} {R : Type u_4} [inst : CommSemiring R] (α : σ → R) (d k : σ →₀ ℕ) (a : R),
  ((taylor α) ((monomial k) a)).coeff d = (eval α) ((hasseDeriv d) ((monomial k) a))
```

The tool keeps the initial forall telescope together despite the width preference; source
signature widths below are independently measured Unicode codepoint counts.

| Sig line | Chars | Next syntactic unit | Arithmetic | Action |
|---|---:|---|---|---|
| 114 | 76 | `(taylor α (monomial k a)).coeff d` (33) | 76 + 1 + 33 = 110 > 100 | ok |
| 115 | 82 | No next signature line | n/a, proof body next | ok |

## Inequality scan

| Occurrence | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| none | Signature and all hypotheses | No `≥` or `>` inequality | None needed | No `_ge_` / `_gt_` name |

## Golfing rule pass

| Rule | Status |
|---|---|
| 1.1 by exact wrapper | n/a: no wrapper. |
| 1.2 by rfl | n/a: none. |
| 1.3 rw + exact | n/a: no such sequence. |
| 1.4 simp + exact | n/a: simp already terminal. |
| 1.5 trailing rfl | n/a: none. |
| 1.6 constructor | n/a: equality, no constructor sequence. |
| 1.7 apply + exact | n/a: helper already applied by exact. |
| 1.8 by_contra + push_neg | n/a: neither occurs. |
| 1.9 eta reduction | n/a: removed manual lambda with the zero-case simplification; no residual lambda. |
| 1.10 single-use have | n/a: no have. |
| 1.11 apply + intro | n/a: none. |
| 1.12 redundant show | n/a: none. |
| 1.13 have + projections | n/a: none. |
| 1.14 consecutive rw | n/a: original one rw deleted; no sequence. |
| 1.15 terminal simp only | n/a: both original and final simps are unsqueezed. |
| 1.16 nonterminal simp | n/a: both final simps terminate. |
| 1.17 dot notation | Existing `.1 hi` and `hd.symm` appropriate; no shorter new receiver form. |
| 1.18 trailing parentheses | n/a: parenthesized notMem_support proof is an interior argument, not trailing. |
| 1.19 push Not | n/a: no push_neg. |
| 1.20 existential wrapper | n/a: no existential. |
| 2.1 grind whole proof | Actually tried isolated pre-target; failed. Also failed on live zero branch. |
| 2.2 delete before grind | n/a: no retained grind. |
| 2.3 simpa consolidation | Existing constant API gives terminal simp directly; no following exact to consolidate. |
| 2.4 fun_prop | n/a: no function-property proposition. |
| 2.5 positivity | n/a: no positivity/nonzero goal. |
| 2.6 gcongr | n/a: no monotonicity inequality. |
| 2.7 lia / omega | n/a: no Nat/Int arithmetic goal; equality of arbitrary semiring coefficients. |
| 2.8 aesop | Actually tried isolated whole proof and live zero branch; failed. |
| 2.9 norm_num / norm_cast | n/a: symbolic arbitrary-semiring coefficients, no numeric or cast subgoal. |
| 2.10 decide / decide +kernel | n/a: arbitrary functions, coefficient ring and exponents, not finite computation. |
| 2.11 field_simp; ring | n/a: no division, only CommSemiring structure. |
| 2.12 linear_combination | n/a: no ring/ring_nf ending or ring identity with hypotheses. |
| 2.13 wlog | n/a: zero and single_add are distinct inductive constructors, not symmetric cases. |
| 2.14 calc collapse | n/a: no calc. |
| 2.15 common goal closing | Zero/nonzero branches need different simp inputs; explicit branches remain clearer. |
| 3.1 erw → rw | n/a: no erw. |
| 3.2 legacy property tactics | n/a: no continuity/measurability. |
| 3.3 omega → lia | n/a: no omega and no arithmetic goal. |
| 3.4 rfl substitution | Existing `obtain rfl` substitutes directly, followed by plain simp. |
| 3.5 automation attributes | n/a: private one-use proof helper; no global attribute justified. |
| 3.6 simp_all only | n/a: none. |
| 3.7 maxHeartbeats | n/a: no limits. |

## Experiments and reflection

Native live goal inspection at original L119 exposed the constant-monomial goal, and
`lean_multi_attempt` tested `simp [← C_apply]`, `simp [← C_apply, hasseDeriv_C]`,
`aesop`, and `grind`. None closed that goal directly. Subsequent isolated pre-target
experiments supply `hd` to the constant-derivative lemma after splitting `d = 0`.
The first simplified candidate without `classical` failed, while restoring `classical`
compiled cleanly. Whole-proof simp/grind/aesop/exact? all failed; apply? was incomplete.

The accepted candidate contains neither the target theorem nor the following main theorem
in its preceding environment: the live source prefix stops immediately before the target.
Its full statement and proof compile, and `#print axioms` reports exactly `propext`,
`Classical.choice`, `Quot.sound`. No `sorryAx`. Failed scratch probes are not accepted proofs.

Step-back result: support induction is the mathematical assembly still required. A term-mode
recursor would add explicit motives/lambdas without reducing the mathematical argument.
No have blocks or redundant rewriting remain. The single-add helper is already reused
directly. The useful improvement is replacing five lines of constant-case work by four,
using existing derivative API instead of unfolding its binomial formula.

## Verification gates

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | `/Users/ramin/.elan/bin/lake build Roth.Taylor`, exit 0; Taylor built in 13s, 1439 jobs. |
| definition_protected | pass | No def/abbrev edits. |
| theorem_statement_protected | pass | Both signature lines byte-identical to worker baseline. |
| structure_gate | pass | Eight body lines, no conjunction, no branch over ten lines. |
| naming_gate | pass | Descriptive private `_aux`, no forbidden pattern. |
| line_packing_gate | pass | Complete two-line codepoint table above. |
| inequality_orientation_gate | pass | No reversed inequalities or orientation-name changes. |
| complete LSP | pass | partial=false, success=true, timed_out=false, failed_dependencies=[]; only known header warning. |
| isolated proof/type/axioms | pass | Pre-target candidate success=true; full type checked; standard axioms only. |

Worker diff: delete the zero-case `rw` line; replace `simp [hasseCoeff]` by `simp`; replace
the manually proved `hasseCoeff` vanishing simp argument by the constant-derivative API.
No other source edits. Full-project dependent build and separate LeanEval are parent gates;
this report does not claim those results. No leaf full-project build was run.

## Result and checklist

Before: 11 declaration lines / 9 body lines. After: 10 declaration lines / 8 body lines.
Saved: 1 line, with clearer API reuse. Issues found: 1; fixed: 1; deferred: 0.
Rules applied: existing-API replacement, terminal simp cleanup; 3.4 retained.
Gates: pass. Renames queued: none. Comments preserved: none present in target.
Refactoring needed: none. Source ownership ended on the recorded freeze SHA; report-only after freeze.

- [x] Step 1 — reference docs read.
- [x] Step 2 — full 24-item audit recorded.
- [x] Step 2.5 — five-method search status recorded.
- [x] Step 2.6 — per-parameter generalisation status recorded.
- [x] Step 2.7 — complete signature width table recorded.
- [x] Step 2.8 — inequality scan table recorded.
- [x] Step 3 — all 42 golfing rules have concrete statuses.
- [x] Step 4 — step-back reflection and actual automation experiments completed.
- [x] Step 5a — complete live LSP clean apart from accepted header warning.
- [x] Step 5b — diff-gate status recorded, actual module build exit 0.
- [x] Step 6a — no renames required; no shared rename sidecar edited.
