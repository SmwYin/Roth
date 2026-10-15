# Phase 4 — `MvPolynomial.uniqueAlgEquiv_hasseDeriv`

Dedicated declaration worker, 2026-10-15. Scope: this declaration and this report.
Baseline snapshot: `/private/tmp/HasseDeriv-decl24-before.lean`. Initial declaration
lines 263–269; final lines 263–268. No Git operations or shared-log edits.

## References and mathematics

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md. Also read the complete Phase-4
worker prompt, installed lean4 and mathlib-quality skills, naming-conventions.md,
relevant style-rules sections, and the normal-form, syntactic-generality, and
documentation sections of mathlib-review-stages.md. Read the file and source §1
at `.mathlib-quality/references/clean.tex:118–152`.

The equivalence between polynomials with a unique variable and univariate
polynomials commutes with Hasse differentiation. On the coefficient of degree m,
both sides give `choose (m + n) n * coeff P (single default (m + n))`.
The coefficient proof avoids converting P to an inverse-equivalence image and
proving an auxiliary equality with polynomial evaluation.

## Full audit — all 24 items

1. **LINT:** no warning on the declaration. Full-file diagnostics have only the
   previously known copyright-header warning at line 1.
2. **HAVE SCAN:** original L267 `hX` is used twice at L269, once forwards and once
   backwards. Its lambda contains a `by` proof, so mandatory alias inlining does
   not apply. The successful coefficient proof removes the helper entirely.
3. **SET_OPTION:** none present or added.
4. **SIMP SQUEEZE:** original proof had no simp. New terminal `simp [hasseCoeff,
   Finsupp.single_add]` closes the coefficient identity; leave unsqueezed.
5. **NAMING:** `uniqueAlgEquiv_hasseDeriv` states which equivalence commutes with
   which operator, retaining their actual API names as snake-case components.
   No numeric scheme, forbidden abbreviation, single-letter name, `_ge_`, or
   `_gt_` occurs. No rename warranted.
6. **LINE PACKING:** all three signature lines measured below; signature unchanged.
7. **BY PLACEMENT:** `:= by` ends the final signature line.
8. **FORMAT:** two-space proof indent, one tactic per line, no blank body lines;
   removing hX removes its `fun g =>` and `rw ...; rfl` style issues. No `haveI`
   or `letI` introduced. Final maximum line width is 96 codepoints.
9. **COMMENTS:** no inline proof comments were present; source citation preserved.
10. **DOCSTRING:** existing public documentation identifies the equivalence and
    contrasts the result with the preceding evaluation theorem; unchanged.
11. **VISIBILITY:** main result named in module documentation and consumed by
    `Roth/Index.lean:256`; keep public.
12. **STRUCTURE:** body 4→3 lines, below the main-result limit of 15. No conjunction
    or long case branch; no decomposition needed.
13. **MATHLIB:** partial matches provide both coefficient APIs; direct use removes
    the auxiliary conversion proof. Detailed search-status below.
14. **JUNK DEF:** n/a: this is a theorem.
15. **EXISTS LEMMA:** n/a: no existential conclusion or witness helper.
16. **SHOW vs CHANGE:** n/a: neither occurs.
17. **PUSH_NEG:** n/a: none occurs.
18. **GENERALISE:** all six parameters inspected and drop-tested; see table.
19. **INEQUALITY:** no ≥ or > in the signature or hypotheses; table below.
20. **NORMAL-FORM:** already a compatibility equation reducing a transported
    multivariate operator to the univariate operator on the RHS.
21. **SYNTAX-GEN:** OK: existing pointwise equality supports the actual `rw`
    consumer. Bundled map equality would require extra coercion manipulation.
22. **IMPORT-FANOUT:** n/a: no import changes.
23. **CASTS:** 0 added, 0 dropped cross-type casts, 0 added load-bearing ascriptions.
    Removed hX's local `Polynomial R` binder annotation with that entire helper.
    Existing statement annotations are preserved.
24. **INSTANCE-NAME:** n/a: no instance declaration.

Issues fixed: local conversion helper eliminated, lambda arrow issue eliminated,
semicolon tactic chain eliminated. Refactoring needed: none. No warranted
substantial API or mathematical change was found.

## Mathlib search-status

| Method | Query and evidence | Result |
|---|---|---|
| A Lean-Finder | `MvPolynomial uniqueAlgEquiv Hasse derivative corresponds univariate polynomial derivative` | `Polynomial.hasseDeriv_one`, `_one'`, bivariate derivative compatibility; partial matches only |
| B Loogle | `MvPolynomial.uniqueAlgEquiv` | Found `coeff_uniqueAlgEquiv`, `_symm_apply`, `_symm_monomial`, and evaluation compatibility |
| C LeanSearch | n/a: parent reported persistent HTTP 500 during this cleanup | Known failed service deliberately not retried; bounded alternative searches used |
| D source grep | Full target name and both `uniqueAlgEquiv.*hasseDeriv` orders across Mathlib; Equiv/HasseDeriv source | No target match; existing coefficient identities found and read |
| E local name search | `uniqueAlgEquiv` | Local target plus mathlib equivalence/coefficient APIs; index warming, positive source hits used only |

Auxiliary variants checked: `_apply`, `_symm_apply`, `_monomial`, `_symm_monomial`,
`coeff_`, `eval₂_`, `hasseDeriv_coeff`. Common-equivalents table: no matching bucket.
Live `exact?` at the initial goal failed; `apply?` offered partial equivalence and
coefficient-extensionality reductions, not a complete proof. Both new coefficient
API names were separately `#check`ed in the successful isolated snippet.

Conclusion: found partial matches `MvPolynomial.coeff_uniqueAlgEquiv` and
`Polynomial.hasseDeriv_coeff`; keep the local theorem and use those directly.
This theorem relates the project-defined multivariate derivative to mathlib's
univariate derivative; no standalone mathlib theorem provides that compatibility.
No new declaration was introduced on a search-only absence claim. The old hX
API-extraction signal is resolved by eliminating the conversion step entirely.

## Generalisation status

| Parameter | Class | Used as | Mechanical candidates / verification | Result |
|---|---|---|---|---|
| `{σ : Type*}` | type variable | variable type and multi-index domain | Already universe polymorphic; isolated drop with autoImplicit false gives unknown σ | Keep |
| `{R : Type*}` | type variable | coefficients of both polynomial types | Already separate universe; isolated drop gives unknown R | Keep |
| `[CommSemiring R]` | typeclass | MvPolynomial, derivative and algebra equivalence | Isolated drop and weakening to `[Semiring R]` both fail CommSemiring synthesis | Keep; weaker parents cannot express unchanged statement |
| `[Unique σ]` | typeclass | unique-variable equivalence and default index | Isolated drop fails Unique synthesis; `[Subsingleton σ] [Inhabited σ]` also fails automatic Unique synthesis | Keep; latter is an equivalent rebundling, not a mathematical weakening |
| `(n : ℕ)` | structure value | Hasse order and single multi-index | Isolated drop gives unknown n; no point/global or strict/weak hypothesis; natural order is intrinsic | Keep |
| `(P : MvPolynomial σ R)` | structure value | arbitrary input polynomial | Isolated drop gives unknown P; already arbitrary | Keep |

Drop/weakening tests ran in isolated `lean_run_code` sections without changing the
live public statement. Their expected errors were inspected explicitly. No
propositional, decidability, finite-type, ordered, characteristic-zero, or field
assumption exists to remove. No safe weakening passed.

Inversion check: the coefficient proof still relies specifically on
`coeff_uniqueAlgEquiv` and the Hasse coefficient formulas after its first rewrite.
An abstract map satisfying that coefficient formula would merely package the
same equivalence, with no demonstrated additional application. An arbitrary
substitution requires a chain rule and changes the mathematical statement.
No warranted big-change candidate.

### Literature search

Web query: “Hasse derivatives multivariate polynomial single variable arbitrary
commutative ring generalization”. Top three returned hits: *Fast Multivariate
Multipoint Evaluation over All Finite Fields* ([publisher](https://doi.org/10.1145/3652025)),
the [authors' PDF](https://mrinalkr.bitbucket.io/papers/MME2.pdf), and
*Polynomial Identity Testing of Read-Once* (Citeseer result). PDF fetch timed out;
the first paper's [arXiv full text, §3.2](https://arxiv.org/html/2205.00342v1#S3.SS2)
was accessed successfully. Definition 3.4 defines multivariate Hasse derivatives
by coefficient extraction over commutative rings and then gives the univariate
specialization. Inference: identifying the sole variable preserves these
coefficients, precisely the theorem here. The current semiring formulation
already removes the additive-inverse assumption used in that source.

Also read the abstract of Narváez-Macarro's
[Hasse–Schmidt derivations versus classical derivations](https://arxiv.org/abs/1810.08075),
which treats multivariate Hasse–Schmidt derivations over arbitrary commutative
algebras and substitution maps. It suggests a broader chain-rule setting, not an
unused assumption in this one-variable equivalence theorem. nLab was searched;
the page fetch rejected XHTML, so it is not relied on as inspected evidence.
Local source §1 explicitly allows commutative semirings. ChatGPT math MCP:
skipped as instructed. Literature-driven substantial changes: none.

## Measured line packing

Compiled `#check @uniqueAlgEquiv_hasseDeriv` with `format.width := 100`:

```text
@uniqueAlgEquiv_hasseDeriv : ∀ {σ : Type u_3} {R : Type u_4} [inst : CommSemiring R] [inst_1 : Unique σ] (n : ℕ)
  (P : MvPolynomial σ R),
  (uniqueAlgEquiv R σ) ((hasseDeriv (Finsupp.single default n)) P) = (Polynomial.hasseDeriv n) ((uniqueAlgEquiv R σ) P)
```

All widths measured by Python `len` (Unicode codepoints). Next unit denotes a
complete mathematical application, preserving natural expression boundaries.

| Signature line | Chars | Next unit | Arithmetic | Action |
|---|---:|---|---|---|
| 263 | 77 | complete left-hand application and `=` (77) | 77 + 1 + 77 = 155 > 100 | ok |
| 264 | 81 | `Polynomial.hasseDeriv n` (23) | 81 + 1 + 23 = 105 > 100 | ok |
| 265 | 58 | no next signature line | n/a | ok |

Before/after signature bytes are identical; this table covers both versions.

## Inequality scan

| Occurrence | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| none | full signature and every parameter | no ≥ or > | n/a | no `_ge_` or `_gt_` |

## Golfing rule pass — all 42 rules

| Rule | Status |
|---|---|
| 1.1 by exact | n/a: no wrapper |
| 1.2 by rfl | n/a: old rfl follows rw, not a standalone wrapper |
| 1.3 rw + exact | n/a: no trailing exact |
| 1.4 simp + exact | n/a: no such sequence |
| 1.5 trailing rfl after simp | n/a: old rfl follows rw |
| 1.6 constructor | n/a: no conjunction/constructor proof |
| 1.7 apply + exact | n/a: none |
| 1.8 by_contra | n/a: none |
| 1.9 eta reduction | n/a: old lambda has proof content; removed with hX instead |
| 1.10 single-use have | Optional strengthening applied: twice-used proof helper removed by coefficient strategy |
| 1.11 apply + intro | n/a: none |
| 1.12 redundant show | n/a: none |
| 1.13 have projections | n/a: no projected conjunction |
| 1.14 merge rewrites | Final coefficient rewrites combined in one rw; no adjacent rw remains |
| 1.15 terminal simp only | n/a: final simp already unsqueezed |
| 1.16 nonterminal simp | n/a: final simp closes the goal |
| 1.17 dot notation | n/a: rewrites use named coefficient theorems; no beneficial dot conversion |
| 1.18 trailing parentheses | n/a: no proof-term argument block |
| 1.19 push_neg | n/a: none |
| 1.20 existential helper | n/a: none |
| 2.1 grind whole proof | Tried live; failed to prove compatibility |
| 2.2 delete before grind | n/a: final proof has no grind |
| 2.3 simpa consolidation | No trailing exact/assumption pattern; tested complete coefficient simp alternative successfully |
| 2.4 fun_prop | n/a: no analytic function-property goal |
| 2.5 positivity | n/a: no positivity or nonzero goal |
| 2.6 gcongr | n/a: no monotonicity or inequality goal |
| 2.7 lia / omega | n/a: no residual Nat/Int arithmetic proposition |
| 2.8 aesop | Tried live; failed after exhaustive search |
| 2.9 norm_num / norm_cast | n/a: symbolic polynomial equality, no numeric or cast subgoal |
| 2.10 decide | n/a: arbitrary polynomials and arbitrary coefficient semiring |
| 2.11 field_simp; ring | n/a: no denominator or ring-expression goal |
| 2.12 linear_combination | n/a: no ring-ending proof or arithmetic hypotheses |
| 2.13 wlog | n/a: no symmetric branches |
| 2.14 calc collapse | n/a: no calc |
| 2.15 close multiple goals | n/a: only one coefficient goal after ext |
| 3.1 erw → rw | n/a: no erw |
| 3.2 legacy function tactics | n/a: none |
| 3.3 omega → lia | n/a: no arithmetic tactic |
| 3.4 rcases rfl | Original obtain rfl auto-substitutes correctly; entire step removed |
| 3.5 automation registration | Considered; no attribute change needed for explicit rewrite use, preserving public normal forms |
| 3.6 simp_all | n/a: no simp_all only and no hypotheses needing global simplification |
| 3.7 heartbeat option | n/a: no limit changes |

## Actual alternatives and reflection

Live initial-goal attempts: `grind`, `simp`, `aesop`, `exact?` failed. `apply?`
returned partial equivalence-inverse and coefficient-extensionality suggestions.
An initial `ext m; simp [coeff_uniqueAlgEquiv, ...]` left an evaluation-coefficient
goal because the default simp rule unfolds `uniqueAlgEquiv` too early.
Disabling `uniqueAlgEquiv_apply` in that terminal simp successfully closed the
coefficient goal, but the explicit coefficient `rw` version avoids needing a
negative simp rule and is equally short after line wrapping. It was selected.

Live multi-attempt replacement can leave old trailing lines behind, producing
`No goals to be solved` or parser errors once a successful replacement has closed
the goal. These were not treated as complete validation. The final proof was
compiled independently under the fresh name `MvPolynomial.decl24_checked`, with
an explicit exact-type assignment against the original signature. The proof does
not use the theorem being cleaned. The first formatting-only probe accidentally
used unknown option `pp.width`; the corrected `format.width` probe succeeded.

The coefficient approach removes the hX conversion layer, uses the existing
computational interfaces directly, and supplies no new helper API. One-tactic
automation failed; term mode would add a coefficient-congruence lambda without
simplifying the mathematics. The final three-line proof is the selected result.

## Verification and gates

Isolated `lean_run_code`: `success: true`, `timed_out: false`; exact original type
checked and axioms printed as `[propext, Classical.choice, Quot.sound]`.
Full-file `lean_diagnostic_messages`: `partial: false`, `success: true`,
`timed_out: false`, no failed dependencies, only known line-1 copyright warning.
Actual `lake build Roth.HasseDeriv`, command session 93479: exit 0, 1430 jobs,
module compilation 14 seconds, only the same existing warning.

Snapshot comparison verifies `signature_equal: True`, `other_source_equal: True`,
declaration lines 7→6, body lines 4→3, max width 96, no sorry/admit/axiom/options
in the target. No definitions, imports, docstrings or other declarations changed.
No passing check was rerun absent a change or failure.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | `lake build Roth.HasseDeriv`, exit 0, 14s |
| definition_protected | pass | Only target proof differs from snapshot |
| theorem_statement_protected | pass | Signature and documentation byte-identical |
| structure_gate | pass | Three-line main proof; no conjunction or long branch |
| naming_gate | pass | Descriptive compatibility name; no forbidden patterns |
| line_packing_gate | pass | All three signature lines measured above |
| inequality_orientation_gate | pass | Zero forbidden inequalities in all parameters and conclusion |

Overall: pass. Full project and LeanEval builds belong to the parent checkpoint.

## Result and checklist

Before: 7 declaration lines / 4 proof lines. After: 6 declaration lines / 3 proof
lines. Saved: 1 line and the complete auxiliary conversion. Three audit issues
fixed; no deferred refactoring. Rules applied: 1.10 (optional helper elimination),
1.14 (combined coefficient rewrites); proof-strategy replacement. Renames queued:
none. Comments preserved: no inline comments existed; public documentation and
source citation preserved. Refactoring needed: none.

- [x] Step 1 — required references read
- [x] Step 2 — all 24 audit slots reported
- [x] Step 2.5 — five-method search-status including known service limitation
- [x] Step 2.6 — all parameters audited and public literature searched
- [x] Step 2.7 — measured signature table
- [x] Step 2.8 — inequality scan table
- [x] Step 3 — all 42 golfing statuses
- [x] Step 4 — actual alternatives and reflection
- [x] Step 5a — complete full-file LSP, only baseline header warning
- [x] Step 5b — diff gates and actual module build
- [x] Step 6a — no rename warranted; no shared sidecar mutation

## Dependent checkpoint validation

The file owner ran `lake build` (2586 jobs) and `lake build Roth.LeanEval`
(2585 jobs), sequentially; both exited 0. Logs:
`/private/tmp/roth-uniqueAlgEquiv_hasseDeriv-build.log` and
`/private/tmp/roth-uniqueAlgEquiv_hasseDeriv-leaneval.log`.
