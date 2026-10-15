# Phase 4: `Roth.wronskianMatrix`

Dedicated worker: original/current lines 54–55, two declaration lines. Ownership: this declaration and this report only. Source is frozen after these checks for parent dependent builds and publication.

Read `lean4/SKILL.md`, `mathlib-quality/SKILL.md`, the authoritative worker contract, and the golfing-rules, proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates, relevant style-rules and naming-conventions references. I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md.

## Full audit

| # | Item | Finding/action |
|---|---|---|
| 1 | LINT | No warning in lines 54–55. Full-file original warnings remain at 1 (header, intentionally preserved by user), 134 and 135 (unused names outside this declaration). |
| 2 | HAVE SCAN | None: the body is a matrix-valued term. |
| 3 | SET_OPTION | None. |
| 4 | SIMP SQUEEZE | None: no tactic proof or simp call. |
| 5 | NAMING | `wronskianMatrix` describes a mathematical matrix, returns data and uses lowerCamelCase; no forbidden abbreviation, numbered scheme, `_ge_` or `_gt_`; no rename needed. |
| 6 | LINE PACKING | The single signature line is 85 codepoints; complete table below. |
| 7 | BY PLACEMENT | n/a: term definition, no `by`. |
| 8 | FORMAT | Retain two-space body indent and term mode; normalize the sole lambda arrow to `↦`. No `haveI`, `letI`, blank interior lines or sequential tactics. |
| 9 | COMMENTS | No inline comments; the existing one-sentence public docstring is preserved byte-for-byte. |
| 10 | DOCSTRING | Existing docstring identifies the entries and source; preserved. |
| 11 | VISIBILITY | Public mathematical definition used by `Roth.wronskian` and matrix proofs, including `Roth/GenWronskian.lean:280`; retain public visibility. |
| 12 | STRUCTURE | One-line term body, no conjunction, branching or extraction needed. |
| 13 | MATHLIB | Five-method evidence below: binary Wronskian is a partial match; retain the finite-family matrix built directly from mathlib Hasse derivatives. |
| 14 | JUNK DEF | Not junk: named mathematical object with repeated local uses in determinant, coefficient and column-operation proofs and an external GenWronskian user. |
| 15 | EXISTS LEMMA | n/a: definition, not a single-use existential helper. |
| 16 | SHOW vs CHANGE | Neither occurs. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | Scratch Semiring weakening succeeds, dropping all algebraic structure fails; preserve current Field signature per user. Details below. |
| 19 | INEQUALITY | No inequalities in signature or body; complete table below. |
| 20 | NORMAL-FORM | Already standard `Matrix.of` of Hasse derivatives with row derivative order and column polynomial index. |
| 21 | SYNTAX-GEN | Current family argument and square matrix output are directly usable by determinant and column-operation APIs. No restatement needed. |
| 22 | IMPORT-FANOUT | n/a: no new imports. |
| 23 | CASTS | One redundant explicit ascription dropped: `(μ : ℕ)` → `μ`; Lean inserts the same genuine Fin-to-Nat coercion from `hasseDeriv`'s expected argument type. 0 explicit cross-type casts retained, 0 load-bearing ascriptions retained in diff. |
| 24 | INSTANCE-NAME | n/a: not an instance. |

Issues found: two syntax issues (lambda arrow, redundant explicit coercion), both fixed. Refactoring needed: none. No signature, docstring, visibility, import, version or mathematical definition changed.

## Line packing

Definition reference: `#check @Roth.wronskianMatrix` with `format.width := 100` reports

```lean
@Roth.wronskianMatrix : {K : Type u_1} → [inst : Field K] → {l : ℕ} →
  (Fin l → K[X]) → Matrix (Fin l) (Fin l) K[X]
```

| Sig line | Chars before/after | Next signature token | Arithmetic | Action |
|---|---:|---|---|---|
| 54 | 85 / 85 | None: `:=` terminates signature, body follows | n/a, no following signature line | ok |

There is only one signature line. Body line 55 is 40 codepoints after cleanup. No repacking is required.

## Inequality scan

| # | Location | Original | Rewrite | Lemma rename? |
|---|---|---|---|---|
| — | Signature and body | n/a: zero `≥` or `>` inequality occurrences | None | None: no `_ge_`/`_gt_` name |

## Mathlib search status

- **A Lean-Finder:** query `Wronskian matrix of Hasse derivatives of finitely many polynomials`; three hits: `Polynomial.wronskian`, `Polynomial.wronskianBilin`, `Polynomial.wronskianBilin_apply`. All concern two polynomials, not this finite-family matrix.
- **B Loogle:** query `Polynomial.hasseDeriv`; hits `Polynomial.hasseDeriv`, `_one`, `_zero`. The first works over `Semiring`, checked by actual `#check`.
- **C LeanSearch:** unavailable: inherited session probe reports HTTP 500. Not retried indefinitely; this is service failure, not evidence of absence.
- **D Source:** untruncated `rg -n 'wronskianMatrix|def wronskian|def hasseDeriv' Roth .lake/packages/mathlib/Mathlib` finds the local matrix, its local/external uses, mathlib's two-polynomial Wronskian and the polynomial/Laurent-series Hasse derivatives.
- **E Local name search:** `wronskian`, limit 20, returns local matrix/theorem API and binary mathlib Wronskian API. Index unavailable; source matches establish presence only and do not establish absence.

Auxiliary variants inspected: `wronskianBilin`, `wronskianBilin_apply`, `hasseDeriv_zero`, `hasseDeriv_one`. Common-equivalents table: no matching discrete/finite/separation/bornology pattern. Six replacement rules: no redundant theorem wrapper, no duplicate definition identified, auxiliary variants searched, no custom predicate replacing a class, no proven equivalent requiring deletion, no new mathlib dependency needing documentation. Existing module documentation already distinguishes the binary mathlib Wronskian.

Conclusion: partial match, retain the named finite-family matrix and use `Polynomial.hasseDeriv` directly as before. No absence claim is made and no new declaration is introduced. `exact?`/`apply?` are inapplicable as replacement-proof searches: the target constructs specific data, and merely finding an inhabitant of a matrix type would not establish equality to these entries.

## Generalisation status

| Parameter/hypothesis | Kind | Mechanical candidates considered/tried | Verified? | Result |
|---|---|---|---|---|
| `K : Type*` | Type variable | Drop would leave the polynomial coefficient type unbound; universe weakening already present | Existing signature checked | Retain universe-polymorphic type |
| `[Field K]` | Typeclass | Drop entirely; parents DivisionRing, Ring, CommRing, CommSemiring; weakest applicable `Semiring` | Actual standalone compiler experiments | Dropping class fails synthesizing `Semiring R`; Semiring version compiles and specializes to original by `rfl`. Stronger intermediate parents add nothing beyond successful weakest candidate. Current Field API retained by user scope. |
| `{l : ℕ}` | Index value | Drop would leave `Fin l` unbound; arbitrary finite index would require a derivative-order enumeration/restatement | Signature dependency inspection | Retain dimension parameter; no arbitrary-index API proposal needed |
| `φ : Fin l → K[X]` | Structure-valued family | Drop would remove the polynomials whose derivatives form entries | Body dependency inspection | Essential input; retain |
| — | Propositions | No propositional hypotheses, inequalities, injectivity, regularity, point-localisation or strict-to-weak candidates | n/a | No such weakening applicable |
| — | Decidability | No explicit decidability parameters | n/a | No drop candidate |

Inversion check: n/a, this is the construction itself, not a theorem whose proof forgets a concrete object. There is no abstract-proof tail to extract.

Scratch Semiring version:

```lean
noncomputable def matrixSemiring {R : Type*} [Semiring R] {l : ℕ}
    (φ : Fin l → R[X]) : Matrix (Fin l) (Fin l) R[X] :=
  Matrix.of fun μ ν ↦ hasseDeriv μ (φ ν)
```

It compiled, as did `Roth.wronskianMatrix φ = matrixSemiring φ := rfl` under Field. It was never installed in the project. Optional widening is closed, not pending: the user chose current APIs and no existing caller needs it. No big-change proposal remains.

### Literature status

A. Web search query: `Wronskian Hasse derivatives matrix generalization polynomials arbitrary characteristic`.
Top three returned hits captured: [Parameterized Algorithms for… thesis](https://www.imsc.res.in/xmlui/bitstream/handle/123456789/408/HBNI%20Th122.pdf?isAllowed=y&sequence=1), [Deterministic Truncation of Linear Matroids](https://citeseerx.ist.psu.edu/document?doi=06960c60d7740b1372e83869587a2062c1664a80&repid=rep1&type=pdf), [second indexed copy of that paper](https://citeseerx.ist.psu.edu/document?doi=82c9ca70cacd5f84d66b0734956553818ec6d59b&repid=rep1&type=pdf).
A directly relevant primary author-hosted result, [Explicit Subspace Designs](https://www.math.toronto.edu/swastik/subspace-designs.pdf), describes Hasse derivatives over fields and the factorial scaling between Hasse and usual Wronskians, with characteristic constraints for the independence criterion. This distinguishes the construction from later nonvanishing theorems. No such theorem hypotheses are changed here. The semiring construction evidence comes from the compiled mathlib API, not an inference that characteristic-sensitive nonvanishing theorems generalize.

B. ChatGPT math MCP: n/a, no tool with that capability exposed in the discovered tool catalogue.
Literature-driven API changes: none warranted for current callers.

## All 42 golfing rules

| Rule | Status |
|---|---|
| 1.1 by exact wrapper | n/a: no proof wrapper |
| 1.2 by rfl | n/a: data term, no proof |
| 1.3 rw + exact | n/a: no tactics |
| 1.4 simp + exact | n/a: no tactics |
| 1.5 trailing rfl | n/a: no tactics |
| 1.6 anonymous constructor | n/a: no conjunction or structure proof |
| 1.7 apply + exact | n/a: no tactics |
| 1.8 by_contra! | n/a: no negation proof |
| 1.9 eta-reduce lambdas | Inspected: both μ and ν are used inside Hasse derivative application; no simple eta-redex of `fun x ↦ f x` remains. Normalize arrow only. |
| 1.10 inline have | n/a: no have |
| 1.11 apply + intro | n/a: no tactics |
| 1.12 redundant show | n/a: no show |
| 1.13 obtain | n/a: no pair-producing have |
| 1.14 merge rw | n/a: no rw |
| 1.15 unsqueeze terminal simp | n/a: no simp |
| 1.16 squeeze nonterminal simp | n/a: no simp |
| 1.17 dot notation | n/a: Matrix.of and hasseDeriv are constructors/operators; no receiver lemma |
| 1.18 remove trailing parens | n/a: `(φ ν)` is the required function argument grouping; no removable trailing tactic/lambda parentheses |
| 1.19 push Not | n/a: no push_neg |
| 1.20 inline existential helper | n/a: not an existential lemma |
| 2.1 grind | n/a: specific data construction, not a propositional tactic proof |
| 2.2 pre-grind tactics | n/a: no grind |
| 2.3 simpa | n/a: no simp/closing tactic chain |
| 2.4 fun_prop | n/a: no analytic regularity goal |
| 2.5 positivity | n/a: no positivity goal |
| 2.6 gcongr | n/a: no inequality goal |
| 2.7 lia/omega | n/a: no arithmetic proof goal |
| 2.8 aesop | n/a: specific matrix data construction |
| 2.9 norm_num/norm_cast | n/a: no numeric/cast equality proof; redundant term ascription removed and rfl-checked |
| 2.10 decide | n/a: not a decidable proposition |
| 2.11 field_simp/ring | n/a: no rational identity |
| 2.12 linear_combination | n/a: no ring proof or equation hypotheses |
| 2.13 wlog | n/a: no case branches |
| 2.14 calc term mode | n/a: already a single term |
| 2.15 multigoal closure | n/a: no goals created |
| 3.1 erw | n/a: no rewrite tactic |
| 3.2 legacy continuity | n/a: no regularity tactic |
| 3.3 omega to lia | n/a: no arithmetic tactic |
| 3.4 rcases with rfl | n/a: no case split |
| 3.5 automation registration | n/a: definition, no proved rewrite theorem needing an attribute |
| 3.6 simp_all | n/a: no simp_all |
| 3.7 heartbeat options | n/a: no options in declaration |

## Experiments and step-back reflection

1. Native isolated `cleanedMatrix` with `↦` and inferred coercion compiles; equality to original is `rfl`.
2. The Semiring scratch construction and specialization equality compile; drop-all-classes experiment fails with missing `Semiring R`, as expected.
3. An initial equality probe omitted the lambda binder type on the RHS, letting Lean infer the row index as Nat; it failed Matrix Nat/Fin mismatch. Corrected the probe by annotating `μ ν : Fin l`. This was scratch-only; the definition's expected matrix type supplies this information directly.
4. An initial data-valued type-compatibility `example` needed a `noncomputable section`; corrected the scratch probe. No source issue.
5. Source edit keeps the original signature line verbatim. Complete native LSP succeeds after edit. Module build succeeds.
6. Isolated final probe checks the exact original function type, original body equality by `rfl`, and axioms. Because native scratch output included an out-of-date-import informational notice after module rebuild, an independent `lake env lean` probe against the rebuilt module also runs below.

The construction is already one direct term using mathlib's matrix and Hasse derivative API. Replacing it with proof automation would obscure specified data. No different proof strategy, helper extraction, eta reduction or local binding removes further useful structure. Existing mathematical API is worth retaining.

## Gate status

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | `/Users/ramin/.elan/bin/lake build Roth.Wronskian`, session 36366, exit 0, 1826 jobs; module reports 20 s |
| complete LSP | pass | `lean_diagnostic_messages` on full file, `success:true`, `partial:false`, no errors or failed dependencies; only 3 original warnings |
| definition_protected | pass | Declaration/signature line unchanged; only body syntax normalization, kernel-confirmed equality to original by rfl |
| theorem_statement_protected | pass | No theorem declaration or statement changed |
| structure_gate | pass | One-line term body, no conjunction or branches |
| naming_gate | pass | Descriptive lowerCamelCase data name; no forbidden pattern |
| line_packing_gate | pass | All signature lines covered by table, 85 chars, no continuation signature line |
| inequality_orientation_gate | pass | Table emitted, zero reversed inequalities, no rename |
| type compatibility | pass | Original polymorphic function type accepted in standalone probe |
| axiom check | pass | `propext`, `Classical.choice`, `Quot.sound` only |
| comments/docstrings | pass | Existing docstring unchanged; no inline proof comments existed |

Final direct compiler probe status is appended after its process exits. Parent owns full project and LeanEval builds before publication.

## Result/checklist

Before: 2 lines. After: 2 lines. Saved: 0 lines. Two routine syntax improvements. Rules applied: lambda-format rule and redundant-cast audit; 1.9 inspected without eta reduction. No renames queued. No refactoring needed. Comments preserved: existing docstring unchanged, no inline comments.

- [x] Step 1: references read.
- [x] Step 2: all 24 audit items recorded.
- [x] Step 2.5: all five search methods have evidence/status.
- [x] Step 2.6: generalisation, hypothesis dependency/drop analysis and literature status recorded.
- [x] Step 2.7: complete per-signature-line width table.
- [x] Step 2.8: inequality scan table.
- [x] Step 3: all 42 golfing rules individually recorded.
- [x] Step 4: alternative/whole-term reflection and actual scratch experiments.
- [x] Step 5a: complete successful live LSP diagnostics.
- [x] Step 5b: all diff gates and actual module build pass.
- [x] Step 6a: naming gate passes; no rename queue mutation needed.

Final direct verification: `/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-wronskian-matrix-verify.lean`, session 82212, exited 0. It checked the exact original type and original body equality by `rfl`, and printed only the three standard axioms above. No warnings or stale-import notice from the direct compiler. Overall: PASS. Source ownership released to the parent for dependent builds/publication.
