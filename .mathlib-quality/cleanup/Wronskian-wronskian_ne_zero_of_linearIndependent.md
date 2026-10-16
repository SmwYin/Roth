# Declaration audit: `Roth.wronskian_ne_zero_of_linearIndependent`

Dedicated Phase 4 worker, baseline `ab266cd`. Original inventory lines 251–261; worker-start lines 217–227. Final lines 217–226: 11 → 10 declaration lines, 9 → 8 proof-body lines. Only this declaration and this report were edited. Source ownership released after successful module build and complete LSP diagnostics; no subsequent source edits.

## Reference reading

Read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, cleanup-gates.md, applicable style-rules.md sections, naming-conventions.md, and the Lean skill. The complete worker contract was supplied at `/private/tmp/roth-wronskian-worker-contract.md`. Existing docstring preservation and public API preservation take precedence over speculative changes.

## Full audit

1. **LINT:** No warnings in target. Complete file diagnostics report only the existing header warning and earlier coefficient lemma's unused `hφ`/`hd`; those are outside ownership.
2. **HAVE SCAN:** Zero `have`/`let` declarations. `hN` is the induction equation, `ih` the induction hypothesis, and `hdeg`/`hne` are destructured witnesses, all used.
3. **SET_OPTION:** None.
4. **SIMP SQUEEZE:** No simp in retained proof. A terminal `simpa only [wronskian_update_sub_smul hne] using ...` alternative was tested successfully; it saves no lines and adds a simplification phase, so direct rewriting is retained.
5. **NAMING:** `wronskian_ne_zero_of_linearIndependent` describes the conclusion and sufficient hypothesis; references `LinearIndependent` with the usual lower-camel fragment. No numeric scheme, forbidden abbreviation, single-letter public name, `_ge_`, or `_gt_`. No rename.
6. **LINE PACKING:** Every signature line measured below. Packed the induction branch onto its preceding line (99 codepoints); signature already maximally packed.
7. **BY PLACEMENT:** `by` stays on final signature line.
8. **FORMAT:** Two-space proof indentation and branch indentation; no blank proof lines or semicolons. Changed mathematical lambda `=>` to `↦`; branch arrow remains `=>`. No `haveI`/`letI`.
9. **COMMENTS:** Existing three-line public docstring preserved byte-for-byte. Zero inline proof comments to move or remove.
10. **DOCSTRING:** Existing statement and primary-source attribution retained. It distinguishes this general independence criterion from the earlier distinct-degree sufficient criterion; no documentation gap requiring a change.
11. **VISIBILITY:** Public mathematical criterion used in `Roth/GenWronskian.lean:276` and `Roth/Separation.lean:598`, as well as the following equivalence. Public visibility justified.
12. **STRUCTURE:** Eight-line body, one one-line injective branch, five-line degree-descent continuation; no conjunction conclusion. No extraction needed; main-theorem 15-line threshold also satisfied.
13. **MATHLIB:** Five-method evidence below. Existing `Nat.strong_induction_on` and `Function.not_injective_iff` used directly; specialized degree descent relies on substantive project lemmas. No new wrapper or definition.
14. **JUNK DEF:** n/a: theorem, not a definition.
15. **EXISTS LEMMA:** n/a: nonvanishing theorem, not a trivial private existential helper.
16. **SHOW vs CHANGE:** Neither occurs.
17. **PUSH_NEG:** None.
18. **GENERALISE:** Complete binder table and actual isolated failed weakening probes below; no accepted change.
19. **INEQUALITY:** Per-occurrence scan below; no reversed order notation.
20. **NORMAL-FORM:** Already the conventional nonzero-Wronskian consequence of `LinearIndependent`; the following equivalence provides the zero/linear-dependence form. No extra equivalence or competing normal form.
21. **SYNTAX-GEN:** OK: implicit polynomial family inferred from bundled linear independence; directly usable at current call sites. No more convenient warranted restatement.
22. **IMPORT-FANOUT:** n/a: no imports changed or added.
23. **CASTS:** 0 dropped / 0 cross-type casts / 0 load-bearing explicit ascriptions in diff.
24. **INSTANCE-NAME:** n/a: theorem, no introduced instances.

Issues found: two routine formatting issues; both fixed. Refactoring needed: none.

## Line-packing artifact

Actual `#check` with `format.width := 100`:

```lean
@wronskian_ne_zero_of_linearIndependent : ∀ {K : Type u_1} [inst : Field K] {l : ℕ} [CharZero K] {φ : Fin l → K[X]},
  LinearIndependent K φ → wronskian φ ≠ 0
```

The pretty-printer's diagnostic string is a reference, not the source width measurement. Unicode codepoints were measured on the actual source.

| Signature line | Codepoints | Next complete syntactic token | Arithmetic | Action |
|---|---:|---|---|---|
| 217 | 78 | `(h : LinearIndependent K φ)` (27) | 78 + 1 + 27 = 106 > 100 | ok |
| 218 | 55 | none: proof body follows | n/a | ok |

Before/after signature strings are identical, including whitespace. Maximum final declaration line is 99 codepoints.

## Inequality occurrence artifact

| Location | Occurrence | Action |
|---|---|---|
| Signature conclusion | `wronskian φ ≠ 0` | Non-equality, not an oriented order relation; unchanged |
| Signature hypotheses and written proof types | Zero `<`, `≤`, `>`, `≥` occurrences | No order rewrite necessary |
| Inferred induction hypothesis | Strict smaller natural degree (`m < N`) | Library-generated, already smaller side first |
| Declaration name | No `_ge_`/`_gt_` | No rename |

Post-edit source scan: zero `≥`, zero order `>`; pattern branch `=>` is syntax, not an inequality.

## Five-method search status

| Method | Query / evidence | Result |
|---|---|---|
| A Lean-Finder | “Wronskian determinant of linearly independent polynomials nonzero characteristic zero” | Returned `Polynomial.natDegree_wronskian_lt_add`, `Polynomial.wronskianBilin_apply`, `Polynomial.wronskian_self_eq_zero`; these concern two polynomials, not the arbitrary finite determinant criterion. |
| B Loogle | `"wronskian"` | Returned `Polynomial.wronskian`, self-zero and negation identities; no replacement from these results. |
| C LeanSearch | Environment's previously established HTTP 500 failure | Unavailable; not counted as negative evidence and not repeatedly retried. |
| D source grep | Untruncated target-name and Wronskian theorem searches in mathlib Polynomial, LinearAlgebra, and `RingTheory/Polynomial/Wronskian.lean` | The two-polynomial theory and coprime criterion are distinct. Local helpers implement the finite determinant degree descent. |
| E local name search | `wronskian` | Found project finite-family API and mathlib two-polynomial API; index `warming`, so only positive returned results used. |

Actual `#check Nat.strong_induction_on` and `#check Function.not_injective_iff` verified the existing generic building blocks. Live `exact?` and `apply?` were attempted before the target declaration was available as an established fact; the very large suggestion output was truncated, so no exhaustive absence claim is made from it. No new declaration was invented on an absence claim. No names guessed or imported, no generated wrapper, no custom predicate/decidability instance; the file-level documentation distinguishes mathlib’s two-polynomial Wronskian from this finite-family construction.

## Generalisation status

| Binder | Kind | Mechanical candidates examined / tried | Verified result / disposition |
|---|---|---|---|
| `{K : Type*}` | Type variable | Drop; universe weakening | Dropping loses the coefficient type of `K[X]`/`LinearIndependent`; already universe polymorphic (`u_1` in actual #check). No meaningful weaker binder. |
| `[Field K]` | Typeclass | Drop; `DivisionRing K`; ring/semiring parent | Actual isolated `DivisionRing` substitution fails at `wronskian φ`: public definition is parameterized by `Field`; dropping or moving farther to ring/semiring also lacks that required structure. Determinant commutativity and division in degree cancellation are substantive. No class change. |
| `{l : ℕ}` | Data | Drop; abstract finite index / universe | Removing binder leaves `Fin l` without its size. Arbitrary finite indexing would change the definition/API, not mechanically weaken this theorem. Already arbitrary natural size. |
| `[CharZero K]` | Typeclass | Drop | Actual isolated drop fails to synthesize `CharZero K` for the nonvanishing criterion. Mathematically necessary without degree restrictions (e.g. 1 and X^p in characteristic p). |
| `{φ : Fin l → K[X]}` | Data | Drop; point-localize | Family is the object in both hypothesis and conclusion; cannot drop. Already arbitrary family; no quantified analytic property to localize. |
| `(h : LinearIndependent K φ)` | Proposition | Drop; unbundle / strict-to-weak | Actual drop probe fails with unknown `h`; direct proof needs its nonzero and update-independence consequences. Without it a family containing zero disproves conclusion. No strict inequality or bijectivity to weaken. |

No typeclass/proposition weakening succeeded. There are no structure-value, decidability, analytic, monotonicity, or order hypotheses omitted from the table. Inversion check: not applicable to a concrete-via-abstract simplification; the proof specifically uses polynomial degrees, leading coefficients, and the Wronskian's column-operation invariance throughout.

### Literature status

[A] Web query: “Wronskians linear independence polynomials characteristic zero generalization Bostan Dumas”. Top three primary results:

1. Bostan–Dumas, [Wronskians and linear independence](https://arxiv.org/abs/1301.6598).
2. [Author-hosted published PDF](https://mathexp.eu/dumas/publications/Bostan_Dumas_2010_WLI.pdf).
3. [Inria author-hosted version](https://specfun.inria.fr/bostan/publications/BoDu09.pdf).

The article extends the characteristic-zero criterion to formal power series and rational functions, and explains why unrestricted positive characteristic fails. Those extensions would require different objects and infrastructure, not a safe hypothesis deletion in the current polynomial API. No current caller needs such a change; no substantial change proposed or applied.

[B] ChatGPT math MCP: n/a, no callable math-chat service exposed in the tool inventory.

## Complete golfing-rule pass

| Rule | Status |
|---|---|
| 1.1 by exact | n/a: multi-step induction, no wrapper. |
| 1.2 by rfl | n/a: no reflexivity-only proof. |
| 1.3 rw + exact | Examined: final rewrite followed by induction application; `rwa` has no existing hypothesis to consume without manufacturing a `have`. Terminal simpa alternative tested instead, no line saving. |
| 1.4 simp + exact | n/a: no retained simp chain. |
| 1.5 trailing rfl | n/a: final `rfl` is a required equality argument to `ih`, not a redundant tactic. |
| 1.6 constructor | n/a: nonvanishing conclusion, no constructor chain. |
| 1.7 apply + exact | n/a: existing exact applications are direct. |
| 1.8 by_contra | n/a: no contradiction/push chain. |
| 1.9 eta reduction | Lambda applies `.natDegree` to `φ ν`, not eta-reducible without composition; converted arrow to `↦`. |
| 1.10 single-use have | n/a: zero have bindings. |
| 1.11 apply + intro | n/a: no such pair. |
| 1.12 redundant show | n/a: none. |
| 1.13 projections | Already obtains collision witnesses directly; no have/projection chain. |
| 1.14 merge rw | n/a: only one rw. |
| 1.15 terminal simp only | n/a in retained proof; candidate simpa-only was not adopted. |
| 1.16 nonterminal simp | n/a: none retained. |
| 1.17 dot notation | Existing `h.ne_zero`, `.1` access used; generic induction API already direct. |
| 1.18 `<\|` | n/a: parenthesized arguments are followed by more arguments or required within rewrite list. |
| 1.19 push_neg | n/a: none. |
| 1.20 existential wrapper | n/a: no private existential lemma. |
| 2.1 grind | Actual whole-proof attempt failed at `False` from `wronskian φ = 0`; no degree-descent construction. |
| 2.2 pre-grind deletion | n/a: no grind retained. |
| 2.3 simpa consolidation | Actual live terminal `simpa only [wronskian_update_sub_smul hne] using ih ...` closes the goal; following existing exact gets “No goals to be solved”. Same three-line layout, no advantage; retain direct rewrite. |
| 2.4 fun_prop | n/a: no analytic/function-property goal. |
| 2.5 positivity | Actual attempt fails “failed to prove nonzeroness”; algebraic structure alone is insufficient. |
| 2.6 gcongr | n/a: target is nonzero, with strict degree descent supplied by a named theorem rather than an inequality subgoal. |
| 2.7 lia/omega | n/a: no open arithmetic goal; degree descent is a specialized polynomial lemma. |
| 2.8 aesop | Included in real live whole-proof batch; output too large/truncated to independently certify a closing proof. No result adopted; explicit induction remains verified. |
| 2.9 norm_num/norm_cast | n/a: no numeric computation or casts. |
| 2.10 decide | n/a: symbolic unbounded polynomial family, not a closed finite decision problem. |
| 2.11 field_simp/ring | n/a: no rational identity goal; coefficient ratio is only an argument. |
| 2.12 linear_combination | n/a: proof has no ring/ring_nf tail. |
| 2.13 wlog | n/a: injective/noninjective cases are mathematically distinct, not symmetric duplicates. |
| 2.14 calc collapse | n/a: no calc. |
| 2.15 shared goals | n/a: branches require different arguments. |
| 3.1 erw | n/a: existing rw works. |
| 3.2 legacy function tactics | n/a: absent. |
| 3.3 omega to lia | n/a: no arithmetic tactic. |
| 3.4 rcases rfl | n/a: collision equality concerns degrees, not equality of indices; no substitution available. |
| 3.5 automation attribute | No attribute added: this criterion is consumed explicitly and by the following equivalence; no demonstrated automation need. |
| 3.6 simp_all | n/a: none in retained proof. |
| 3.7 heartbeat limits | n/a: no local limits present or introduced. |

## Experiments and reflection

The proof first handles distinct degrees using the established determinant coefficient theorem. Otherwise it subtracts a suitable constant multiple of one polynomial from another, preserving Wronskian and independence while decreasing total degree; natural strong induction concludes. This is already a concise mathematical outline and cannot be replaced by reflexive or elementary arithmetic automation. Packing the induction pattern removes one line without changing that structure.

The first native whole-proof batch eventually returned a very large diagnostic payload. It was checked via a termination request, which retrieved its already-completed result. A duplicate direct fallback had been started while the native call appeared stalled; it was canceled with Ctrl-C (exit 130) when the native result arrived. That canceled fallback is not verification evidence. No repeated equivalent automation search was pursued afterward. Native diagnostics, the distinct terminal-simpa experiment, and isolated code compilation were responsive.

## Verification and gates

- `/Users/ramin/.elan/bin/lake build Roth.Wronskian`: session 46535, exit 0, “Build completed successfully (1826 jobs)”; log `/private/tmp/roth-wronskian-decl14-module.log`.
- Native `lean_diagnostic_messages` on complete file: `success: true`, `partial: false`, `timed_out: false`, no errors and only the three known earlier warnings.
- Native isolated `lean_run_code` with the complete rewritten proof: `success: true`, `timed_out: false`. It reported an informational import-rebuild notice during concurrent module rebuild; the proof itself uses unchanged helper statements and compiled independently. Module build subsequently completed successfully.
- Fresh post-build `/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-wronskian-decl14-type.lean`: session 51834 exited 0, independently checked the explicit original theorem type and printed only `propext`, `Classical.choice`, `Quot.sound`. This fresh process resolves the native scratch server’s informational stale-import notice.
- Exact original/final signature string comparison passed. Existing docstring unchanged; diff restricted to induction line wrapping and lambda arrow.
- Final target scan: zero `sorry`, `admit`, `set_option`, `haveI`, `letI`, `push_neg`, reversed inequalities, or new imports.
- Full project and separate `Roth.LeanEval` dependent builds belong to the parent publication checkpoint, not claimed prematurely here.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Actual module command exited 0 / 1826 jobs |
| definition_protected | pass | No def/abbrev changes |
| theorem_statement_protected | pass | Original and final signature text identical |
| structure_gate | pass | Eight-line body; branches below ten; no conjunction |
| naming_gate | pass | Mathematical conclusion-of-hypothesis name; no forbidden form |
| line_packing_gate | pass | Both signature lines measured above, no repack row |
| inequality_orientation_gate | pass | Scan above, no reversed order symbols |

Overall: pass. Audit issues found 2, fixed 2; no refactoring or renames queued. Existing docstring preserved; inline comments none present.

## Phase checklist

- [x] Step 1: required references read.
- [x] Step 2: all 24 audit items reported.
- [x] Step 2.5: five-method search status and actual name checks.
- [x] Step 2.6: all binders considered, actual weakening probes, public literature status.
- [x] Step 2.7: every signature line measured in codepoints.
- [x] Step 2.8: per-occurrence inequality scan.
- [x] Step 3: all 42 golfing rules considered with concrete status.
- [x] Step 4: mathematical step-back and alternative strategy assessed.
- [x] Step 5a: complete live diagnostics passed.
- [x] Step 5b: all seven diff gates passed.
- [x] Step 6a: no renames required.
