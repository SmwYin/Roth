# Cleanup: `MvPolynomial.coeff_taylor_monomial_single_add_aux`

Target: `Roth/Taylor.lean`, originally lines 95–113 (19 lines), finally 95–112 (18 lines).
Source frozen at SHA256 `9a4189e83c942dbf021d9c6f831a4d4a17384e5b7ad8a88e1ded62dbba73cdd8`.
No other declaration, signature, import, docstring, toolchain, shared log or Git metadata changed.
Parent owns dependent builds and publication. This newly extracted helper does not increment the project declaration count.

## References and mathematics

Read the Lean4 and mathlib-quality SKILL.md files, worker contract, golfing-rules.md,
proof-patterns.md, mathlib-search.md, generalisation-patterns.md, cleanup-gates.md and
relevant style-rules.md sections. Naming reference not additionally required: no naming defect.

The induction step factors the monomial into a power of one variable and the remaining monomial.
The induction hypothesis and `k i = 0` show that the latter translate has no support in coordinate i.
The coefficient of the product then separates into the univariate binomial coefficient and the
remaining coefficient; the local combinatorial identities recombine the Hasse coefficient and
powers. This is substantive mathematical proof, not a wrapper of one existing theorem.

## Full audit

1. **LINT:** No target diagnostics. Complete file diagnostics have only the pre-existing L1:2 copyright warning; user chose to leave it unchanged, without suppression.
2. **HAVE SCAN:** Original L101 `hXC`, has a `by` proof, used once in the main rewrite; KEEP (proves evaluation identity). Original L104 `hsupp`, has a five-line `by` proof, used once by `coeff_aeval_X_mul`; KEEP (proves vanishing support). No other haves.
3. **SET_OPTION:** None; no limit increases or diagnostic options introduced.
4. **SIMP SQUEEZE:** Three terminal simp calls: hXC, contradiction in hsupp, final commutative product identity. No nonterminal bare simp or terminal simp-only. Changed hXC `simp [algebraMap_eq]` to `simp`, verified independently and jointly.
5. **NAMING:** Descriptive coefficient/Taylor/monomial/single-add name with private `_aux`; no forbidden abbreviation or numeric pattern, no rename needed.
6. **LINE PACKING:** Every signature line measured below. No repacking needed.
7. **BY PLACEMENT:** All `by` tokens finish their preceding line.
8. **FORMAT:** Two-space proof indentation, four-space signature continuation; no empty proof lines, semicolon chains, `haveI` or `letI`. Removed redundant `classical` after successful isolated compilation.
9. **COMMENTS:** None in target; no comments removed or moved.
10. **DOCSTRING:** n/a: private helper intentionally has no API docstring.
11. **VISIBILITY:** Already private and only used by the adjacent monomial induction.
12. **STRUCTURE:** Body 14 → 13 lines, no conjunction in statement, no case branch over 10 lines. hXC is three lines and hsupp is five lines including its header. No decomposition flag needed.
13. **MATHLIB:** Five-method search and checked source building blocks below. Keep substantive local argument using existing binomial API.
14. **JUNK DEF:** n/a: lemma, not a definition.
15. **EXISTS LEMMA:** n/a: equality conclusion, not a trivial existential witness.
16. **SHOW vs CHANGE:** None.
17. **PUSH_NEG:** None; `by_contra h` has no following push_neg to merge.
18. **GENERALISE:** All parameters reviewed below; exact statement preserved. No approved or discovered mechanically valid signature weakening applied.
19. **INEQUALITY:** Zero reversed inequality occurrences, table below.
20. **NORMAL-FORM:** Already in coefficient-equals-evaluated-Hasse-derivative normal form used by the induction. No equivalent-form conversion API needed.
21. **SYNTAX-GEN:** OK: explicit induction hypothesis supplies every coefficient needed for support and erase-index evaluation. No easier application shape identified.
22. **IMPORT-FANOUT:** n/a: no new import.
23. **CASTS:** Diff: 0 dropped / 0 cross-type / 0 load-bearing casts introduced. Existing hXC polynomial type ascription is untouched and fixes the polynomial ambient type; no explicit coercion in this proof diff.
24. **INSTANCE-NAME:** n/a: no instance declaration.

Issues fixed: redundant classical tactic; unnecessary explicit simp hint in hXC.
Refactoring needed: none.

## Mathlib search-status

| Method | Queries / evidence | Result |
|---|---|---|
| A Lean-Finder | `multivariate polynomial coefficient Taylor translation monomial binomial` | Univariate `Polynomial.taylor_monomial`, `taylor_apply`, `taylor_X_pow`, `sum_taylor_eq`; no direct replacement returned. |
| B Loogle | `MvPolynomial.coeff, MvPolynomial.aeval`; then `"coeff_X_add_C_pow"` | First query rejected by remote index as unknown identifier; second returns `Polynomial.coeff_X_add_C_pow`, already used. |
| C LeanSearch | Translation/monomial coefficient query class | Unavailable: parent established repeated HTTP 500 service failure; per task instruction not retried. |
| D source rg | `coeff.*aeval`, `taylor`, `coeff.*monomial.*add`, full target name, `coeff_X_add_C_pow`, `monomial_single_add` in relevant polynomial directories | Read `Polynomial/Coeff.lean:292` and `MvPolynomial/Basic.lean:255`; verified both with compiled `#check`. No full target-name duplicate found. |
| E local names | `coeff_taylor`, `coeff_X_add_C` | Project target/parent plus univariate results; positive source-backed hit for `Polynomial.coeff_X_add_C_pow`. Index unavailable/warming, so empty index results were not used as absence evidence. |

Auxiliary variants: `monomial_add_single`, `monomial_single_add`, `coeff_X_add_one_pow`,
`coeff_one_add_X_pow`, `taylor_X_pow`, coefficient/aeval combinations. Common-equivalents
lookup: no matching topological/finiteness/bornological bucket.

Conclusion: partial match `Polynomial.coeff_X_add_C_pow`; keep the local multivariate induction
step and use that existing lemma directly, as the proof already does. No categorical absence claim
is inferred from the unavailable search service. PRE-TARGET `exact?` did not close the goal;
`apply?` produced only a graph-membership obligation, not a complete proof.

## Generalisation status

All statement substitutions were isolated experiments; none were applied to production source.
The local API is already over `CommSemiring R` (not merely Semiring).

| Parameter | Class / use | Mechanical candidates examined or tried | Verified / result |
|---|---|---|---|
| `{σ : Type*}` | type variable; variables and Finsupp indices | Drop would leave dependent binders ill-scoped or reintroduce σ through auto-implicit; universe polymorphism already present. No point/strict variant. | Structural dependency retained. |
| `{R : Type*}` | type variable; coefficient type | Drop would leave α/a and the coefficient structure ill-scoped or auto-implicit; already universe polymorphic. | Retained. |
| `[CommSemiring R]` | typeclass; taylor algebra hom and commutative products | Drop, Semiring, NonUnitalCommSemiring probes using `omit [CommSemiring R] in`. | All rejected: cannot omit referenced section instance; Semiring also yields inconsistent synthesized instances. Existing taylor API requires CommSemiring. No success claimed for a wholesale API generalisation. |
| `(α : σ → R)` | structure value; translation/evaluation | Drop not possible while keeping the dependent statement; abstract function already arbitrary. Point-localisation catalogue concerns continuity etc., absent here. | Retained. |
| `(a : R)` | structure value; monomial scalar | Drop not possible while retaining stated monomials; no stronger property imposed. | Retained. |
| `{i : σ}` | structure value; single coordinate | Drop would leave single/support evaluations unbound; no finite restriction or concrete specialization. | Retained. |
| `(n : ℕ)` | structure value; exponent/choose | Drop would leave exponent unbound; abstracting ℕ changes polynomial multi-index/binomial mathematics and has no mechanical analogue. | Retained. |
| `{k : σ →₀ ℕ}` | structure value; residual monomial | Drop would leave monomial/hi/ih unbound; already arbitrary finite-support index. | Retained. |
| `(hi : k i = 0)` | proposition; support vanishing and product identities | Actual drop-test; equality-to-two-inequalities is equivalent repackaging, not a weakening; no strict→weak form. | CLI rejected dropped proof at references to hi and support/product goals. Retained. |
| `(ih : ∀ d, ...)` | proposition; coefficient identities for support e and d.erase i | Actual drop-test; point-localisation to one index cannot supply all support e; restriction to support plus erase would restate the private induction interface with extra obligations. | CLI rejected dropped proof at ih references and coefficient goal. Retained. |
| `(d : σ →₀ ℕ)` | structure value; requested coefficient | Drop leaves conclusion unbound; arbitrary index already. | Retained. |

A binder-drop that merely auto-reintroduces the same data variable is not a generalisation and was
not claimed as one. No mathematical necessity claim is made for hi/ih beyond the mechanical proof
experiment; the ultimate unconditional Taylor theorem is established later by induction.
Inversion check: n/a, no concrete named witness; proof is parametric and specifically uses translation,
Hasse derivatives, and single-coordinate monomials throughout.
Big-change candidates: none justified by a successful compiled proposal.
Literature search: n/a: private declaration, literature search not required (both WebSearch and math MCP).

## Signature widths and inequalities

`set_option format.width 100 in #check @coeff_taylor_monomial_single_add_aux` from the isolated final
pre-target file printed:

```lean
@coeff_taylor_monomial_single_add_aux : ∀ {σ : Type u_3} {R : Type u_4} [inst : CommSemiring R] (α : σ → R) (a : R)
  {i : σ} (n : ℕ) {k : σ →₀ ℕ},
  k i = 0 →
    (∀ (d : σ →₀ ℕ), ((taylor α) ((monomial k) a)).coeff d = (eval α) ((hasseDeriv d) ((monomial k) a))) →
      ∀ (d : σ →₀ ℕ),
        ((taylor α) ((monomial (Finsupp.single i n + k)) a)).coeff d =
          (eval α) ((hasseDeriv d) ((monomial (Finsupp.single i n + k)) a))
```

Widths are Unicode codepoints including indentation. Next token means complete binder or the
conclusion expression at the legal break, not individual lexical words inside that expression.

| Signature line | Chars | Next binder/expression chars | Arithmetic | Action |
|---|---:|---:|---|---|
| 95 | 99 | `(hi : k i = 0)`, 14 | 99 + 1 + 14 = 114 > 100 | ok |
| 96 | 18 | complete ih binder, 84 | 18 + 1 + 84 = 103 > 100 | ok |
| 97 | 88 | `(d : σ →₀ ℕ)`, 12 | 88 + 1 + 12 = 101 > 100 | ok |
| 98 | 77 | RHS through `:= by`, 65 | 77 + 1 + 65 = 143 > 100 | ok |
| 99 | 71 | no next signature line | n/a; proof next | ok |

| Occurrence | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| none | signature and local hypotheses | n/a: no `≥` or `>` inequalities | none | no `_ge_`/`_gt_` in name |

## Experiments

Native `lean_multi_attempt` at the hXC line attempted `grind`, `simp_all`, `aesop`, `exact?`, `apply?`.
Its replacement left continuation-line parser errors, so these were not used as sole evidence.
The following complete-declaration experiments were rerun with the live prefix ending BEFORE the
target, excluding both target and downstream Taylor results from the environment.
All CLI runs used `/Users/ramin/.elan/bin/lake env lean /private/tmp/newhelper01-*.lean` and default limits.

| Experiment | Outcome |
|---|---|
| original whole proof | exit 0; standard axioms only |
| whole `grind` | exit 1; failed equality/False goal |
| whole `simp_all` | exit 1; unresolved translated monomial coefficient |
| whole `aesop` | exit 1; exhaustive search failed |
| whole `exact?` | exit 1; no closing lemma |
| whole `apply?` | exit 0 but partial proof with sorry warning; REJECTED, not proof success |
| drop hi | exit 1; unknown hi and unresolved support/product goals |
| drop ih | exit 1; unknown ih and unresolved product coefficient |
| drop classical | exit 0; adopted |
| hXC bare simp | exit 0; adopted |
| hsupp `simp_all` | exit 1; support implication remains |
| drop/parent instance probes | exit 1; referenced CommSemiring instance cannot be omitted |
| combined final proof/type/axioms | exit 0, no sorry warning; exact final proof in pre-target context |

Temporary apply? elaboration warnings were not written into repository source or accepted as proofs.

## Every golfing rule

- [1.1] n/a: no `by exact` wrapper.
- [1.2] n/a: no `by rfl`.
- [1.3] n/a: no rw followed by exact; main rewrite needs final algebraic simp.
- [1.4] n/a: no simp followed by exact/assumption.
- [1.5] n/a: no trailing rfl.
- [1.6] n/a: no constructor chain.
- [1.7] n/a: no apply/exact chain.
- [1.8] n/a: by_contra has no push_neg step.
- [1.9] n/a: the hle lambda composes transport and inequality elimination, not eta form.
- [1.10] Both haves contain genuine by proofs; no single-use alias to inline.
- [1.11] n/a: no apply/intro sequence.
- [1.12] n/a: no show.
- [1.13] n/a: no conjunction-valued have/projections.
- [1.14] Main rw list already merged; hsupp rw is in a separate scope.
- [1.15] Terminal simps already unsqueezed; additionally removed redundant hXC explicit hint after compilation.
- [1.16] n/a: all simp calls terminal.
- [1.17] Existing `.2`/`.1` eliminations already direct; no eligible long namespace composition.
- [1.18] Existing `fun hle ↦ ...` is unparenthesized; remaining parentheses delimit required subterms.
- [1.19] n/a: no push_neg.
- [1.20] n/a: not an existential lemma.
- [2.1] Whole grind tried and failed, isolated evidence above.
- [2.2] n/a: no grind in accepted proof.
- [2.3] n/a: terminal simp closes its blocks, no following closing tactic to consolidate.
- [2.4] n/a: no continuity/differentiability/measurability goals.
- [2.5] n/a: no standalone positive/nonnegative goal; support proof is vanishing from a binomial coefficient.
- [2.6] n/a: no monotonicity inequality goal or calc.
- [2.7] n/a: no standalone Nat/Int arithmetic tactic block; le_zero_iff is a direct exact conversion in a proof term.
- [2.8] Whole aesop tried and failed; hsupp simp_all also failed.
- [2.9] n/a: no numeric evaluation or cast-normalization block.
- [2.10] n/a: symbolic coefficient identity over arbitrary semiring, no closed decidable computation.
- [2.11] n/a: no division or field structure.
- [2.12] n/a: no ring/ring_nf ending or ring hypotheses.
- [2.13] n/a: no symmetric case branches.
- [2.14] n/a: no calc.
- [2.15] n/a: no repeated parallel goals.
- [3.1] n/a: no erw.
- [3.2] n/a: no continuity/measurability tactic.
- [3.3] n/a: no omega.
- [3.4] n/a: no rcases/rfl substitution.
- [3.5] No new automation attribute: specialized induction helper carries a quantified ih; no useful canonical simp orientation.
- [3.6] n/a: no accepted simp_all-only block; trial simp_all did not close.
- [3.7] n/a: no maxHeartbeats option. Removed redundant classical independently.

Step-back reflection: no whole-proof tactic or direct lemma found. The two haves name distinct
mathematical stages, and the rewrite uses the existing single-coordinate and binomial API.
Inlining them would obscure the support argument without eliminating it. Keep the 13-line proof.

## Gates and final verification

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | `/Users/ramin/.elan/bin/lake build Roth.Taylor`, exit 0; final Taylor job 8.9 seconds |
| complete LSP | pass | Native lean_diagnostic_messages after final edit: success=true, partial=false, timed_out=false, failed_dependencies=[]; only accepted L1:2 header warning |
| isolated exact proof/type/axioms | pass | `/Users/ramin/.elan/bin/lake env lean /private/tmp/newhelper01-final.lean`, exit 0; prefix excludes target/downstream results; exact final declaration and #check/#print axioms |
| definition_protected | pass | Diff has no definition/abbreviation changes |
| theorem_statement_protected | pass | Full five-line signature byte-identical |
| structure_gate | pass | 13 body lines; no conjunction or long branch |
| naming_gate | pass | Mathematical private `_aux`, no forbidden pattern |
| line_packing_gate | pass | Complete five-row codepoint table above |
| inequality_orientation_gate | pass | No reversed inequality in signature/local hypotheses |

Final isolated axiom output: `[propext, Classical.choice, Quot.sound]` only.
The only diff is removal of `classical` and hXC `simp [algebraMap_eq]` → `simp`.
Full-project and separate LeanEval verification belong to the parent after source freeze.

Result: Before 19 lines / After 18 / Saved 1; body 14 → 13.
Audit issues found 2, fixed 2; refactoring deferred 0.
Rules applied: terminal simp simplification (1.15 spirit), redundant classical removal.
Gates: pass. Renames queued: none. Comments preserved: none present. Refactoring needed: none.

## Required phase checklist

- [x] Step 1 — mandatory references read.
- [x] Step 2 — all 24 audit items reported.
- [x] Step 2.5 — five-method search-status block.
- [x] Step 2.6 — per-parameter generalisation status and private-literature exemption.
- [x] Step 2.7 — every signature line measured.
- [x] Step 2.8 — inequality scan table.
- [x] Step 3 — all 42 golfing rules have status/reason.
- [x] Step 4 — step-back reflection and actual automation tests.
- [x] Step 5a — complete LSP success; only accepted pre-existing header warning.
- [x] Step 5b — diff gates, module build, exact isolated proof/type/axioms.
- [x] Step 6a — rename queue n/a: no warranted rename.
