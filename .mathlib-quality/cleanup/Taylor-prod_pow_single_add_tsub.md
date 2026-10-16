# `MvPolynomial.prod_pow_single_add_tsub` — declaration cleanup

Baseline: `258cfa4`, `Roth/Taylor.lean:86–96` (original file inventory: 101–111).
Final: lines 86–93. Declaration 11 → 8 lines; proof body 7 → 5 lines.
Only this private declaration was edited. No Git operations or shared report edits.

## Step 1 — references

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md in full, together with the supplied
worker contract, lean4 and mathlib-quality skills, quality principles, and the relevant
formatting, tactics, inequality, documentation, visibility, and normal-form sections
of style-rules.md. The dispatch's API/documentation preservation and header decision
override generic suggestions to broaden signatures or edit headers.

## Step 2 — full audit

1. **LINT:** no diagnostic in this declaration. Complete final LSP has only the
   user-preserved file copyright warning at line 1.
2. **HAVE SCAN:** original L91/final L90 `have h : ... := by` is used once in the
   final simplification. KEEP: genuine extensional coordinate proof (two lines), not
   a single-use term alias. No other `have`.
3. **SET_OPTION:** none; no limits or tracing added.
4. **SIMP SQUEEZE:** existing `simp [*, Finsupp.erase_ne]` closes both coordinate
   cases. New `simp [h, Finsupp.prod_add_index', pow_add, -Finsupp.single_tsub]`
   closes the entire product goal. Both terminal; neither needs squeezing.
5. **NAMING:** `prod_pow_single_add_tsub` describes a product of powers after
   singleton addition and truncated subtraction, uses snake_case, and contains no
   forbidden numeric pattern, abbreviation, or reversed inequality suffix. No rename.
6. **LINE PACKING:** moved `hi` onto the first line and packed `d` with the equation,
   including its first right-hand factor. Before/after tables below.
7. **BY PLACEMENT:** declaration and local equality both end their signature with `by`.
8. **FORMAT:** two-space proof indentation; four-space signature continuation, six
   spaces for continued equation; no blank lines inside; no haveI/letI. Ordinary
   lambdas changed to `↦`. Removed rw/congr/exact assembly in favor of terminal simp.
9. **COMMENTS:** none inside target, none removed. Adjacent documentation unchanged.
10. **DOCSTRING:** n/a: private helper, no docstring required or introduced.
11. **VISIBILITY:** remains private; one use in the coefficient Taylor proof.
12. **STRUCTURE:** 5-line body, no conjunction in statement, coordinate branches
    each closed by the shared simp. No extraction or decompose flag warranted.
13. **MATHLIB:** five-method status below; reuse `Finsupp.prod_add_index'` and
    `Finsupp.prod_single_index` through simplification. Keep substantive coordinate
    decomposition; no exact replacement was found.
14. **JUNK DEF:** n/a: lemma, no definition.
15. **EXISTS LEMMA:** n/a: equality, no existential witness.
16. **SHOW vs CHANGE:** n/a: neither present.
17. **PUSH_NEG:** none.
18. **GENERALISE:** every parameter assessed below. A CommMonoid version compiles
    in scratch; existing caller already needs CommSemiring, so there is no concrete
    benefit to changing the private contract in this cleanup. Live API preserved.
19. **INEQUALITY:** equality-only statement and local hypothesis, table below.
20. **NORMAL-FORM:** Finsupp natural truncated subtraction and multiplicative
    factorization are the appropriate existing forms. The local negative simp lemma
    prevents `single_tsub` expanding the singleton before `prod_single_index` evaluates it.
21. **SYNTAX-GEN:** OK: explicit α, hi, d match the existing rewrite use. No bundled
    predicate or less usable formulation needs restatement.
22. **IMPORT-FANOUT:** n/a: no imports added.
23. **CASTS:** 0 dropped / 0 cross-type / 0 load-bearing; no casts in the diff.
24. **INSTANCE-NAME:** n/a: no instance declaration.

Issues found: underpacked signature, ordinary lambda arrows, avoidable final
rw/congr/exact assembly. All three fixed. Refactoring needed: none.

## Mathlib search status

| Method | Actual query/evidence | Result |
|---|---|---|
| A Lean-Finder | `Finsupp product powers single add subtract erase` | `Finsupp.mul_prod_erase'`, `Finsupp.mul_prod_erase`, and unrelated AddMonoidAlgebra product lemma |
| B Loogle | `Finsupp.prod, Finsupp.single` | `Finsupp.prod_single_index` |
| C LeanSearch | n/a: parent-established HTTP 500 outage; dispatch explicitly prohibited repeated retry | unavailable, not evidence of absence |
| D source search | `prod_(add_index\|single_index)`, `single.*tsub`, `tsub.*single`, `erase.*sub`, `sub.*erase` in Finsupp source | `prod_add_index`, `prod_add_index'`, `prod_add_index_of_disjoint`, `prod_single_index`, `single_tsub`; initial nonexistent Algebra/Finsupp path corrected to Algebra/BigOperators/Finsupp/Basic.lean |
| E local name search | `Finsupp.prod_add` | source matches for three product-add variants; index unavailable, so no absence claim |

Auxiliary variants: general and primed product-add, disjoint product-add, product
single-index, erase splitting, and single_tsub. Common-equivalents lookup: no matching
concept bucket. Actual `#check` verified the types of `prod_add_index'`,
`prod_single_index`, and `single_tsub` in the original imports.

Conclusion: partial mathlib matches, used directly inside the proof. The helper
still contains a genuine coordinate decomposition with two cases; it is not an exact
copy or a wrapper consisting only of 1–3 direct mathlib calls. Whole-goal `exact?`
failed and `apply?` produced unrelated inverse/unit obligations. This is not a claim
that exhaustive mathematical absence has been proved.

## Generalisation status

| Parameter | Class | Use / mechanical candidates | Verified? | Result |
|---|---|---|---|---|
| `{σ : Type*}` | type-variable | domain of α, i, k', d; drop would leave the statement unbound; universe already arbitrary | structural check | retain |
| `{R : Type*}` | type-variable | codomain of α/product; drop leaves R unbound; universe already arbitrary | structural check | retain |
| `[CommSemiring R]` | typeclass | only multiplicative product/power needed; try CommMonoid, Monoid, drop | compiled candidate with CommMonoid; compiled Monoid rejection (`CommMonoid R` synthesis); drop likewise lacks product/power instances | CommMonoid mathematical weakening established, unapplied per preserved-contract policy and no caller benefit |
| `(α : σ → R)` | structure value | determines every product factor; drop leaves α unbound; no continuity/global predicate to localize | structural check | retain |
| `{i : σ}` | structure value | singleton/erase coordinate; drop leaves i unbound | structural check | retain |
| `{n : ℕ}` | structure value | singleton exponent and n − d i; drop leaves n unbound; changing Nat restates exponent/subtraction semantics | structural check | retain |
| `{k' : σ →₀ ℕ}` | structure value | finitely supported residual exponent; drop leaves k' unbound; arbitrary-function restatement loses finite product domain | structural check | retain |
| `(hi : k' i = 0)` | proposition | forces singleton-coordinate remainder zero; drop tested; ≤ 0 is equivalent over Nat, not weaker; no strict inequality/global hypothesis | compiled drop fails: `n + k' j - d j = n - d j + k' j` | retain |
| `(d : σ →₀ ℕ)` | structure value | subtracted exponent and erased component; drop leaves d unbound | structural check | retain |

No explicit decidability parameter: proof-local `classical` handles the coordinate
case split. Inversion check: no named concrete mathematical object; this is already
parametric in σ, R, α, i, n, k', d. Literature: n/a, private declaration. No
literature-driven proposal. CommMonoid scratch evidence was sent to the parent;
parent confirmed to preserve the live signature and distinguish optional abstraction
from concrete benefit. No unresolved approval or phase-5 task.

## Line packing

Original signature lines (codepoint counts):

| Line | Chars | Next syntactic unit | Arithmetic | Action |
|---|---:|---|---|---|
| 86 | 80 | `(hi : k' i = 0)` = 15 | 80 + 1 + 15 = 96 ≤ 100 | repack |
| 87 | 34 | left product expression = 57 | 34 + 1 + 57 = 92 ≤ 100 | repack |
| 88 | 63 | `α i ^ (n - d i)` = 15 | 63 + 1 + 15 = 79 ≤ 100 | repack |
| 89 | 72 | proof follows | n/a | ok |

Final signature lines:

| Line | Chars | Next syntactic unit | Arithmetic | Action |
|---|---:|---|---|---|
| 86 | 96 | `(d : σ →₀ ℕ)` = 12 | 96 + 1 + 12 = 109 > 100 | ok |
| 87 | 95 | `(k' - d.erase i).prod` = 21 | 95 + 1 + 21 = 117 > 100 | ok |
| 88 | 53 | proof follows | n/a | ok |

Actual width-100 `#check` reference:

```lean
@prod_pow_single_add_tsub : ∀ {σ : Type u_3} {R : Type u_4} [inst : CommSemiring R] (α : σ → R) {i : σ} {n : ℕ}
  {k' : σ →₀ ℕ},
  k' i = 0 →
    ∀ (d : σ →₀ ℕ),
      ((Finsupp.single i n + k' - d).prod fun j e => α j ^ e) =
        α i ^ (n - d i) * (k' - Finsupp.erase i d).prod fun j e => α j ^ e
```

## Inequality scan

| Occurrence | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| none | complete signature and local `h` type | no ≥ or >; all relations are equality | none | none |

## Golfing rule pass

| Rule | Status |
|---|---|
| 1.1 by exact wrapper | n/a: multi-step decomposition proof |
| 1.2 by rfl | n/a: no reflexivity wrapper |
| 1.3 rw + exact | replaced entire final assembly with terminal simp |
| 1.4 simp + exact | n/a: old simp already terminal in coordinate proof |
| 1.5 trailing rfl | n/a: none |
| 1.6 constructor chain | n/a: no constructor target |
| 1.7 apply + exact | n/a: no such pair |
| 1.8 by_contra + push_neg | n/a: no contradiction proof |
| 1.9 eta-reduce | removed explicit zero/add compatibility lambdas through simp; remaining power lambda is not an eta-redex |
| 1.10 single-use have | retain h: genuine by proof, no term alias |
| 1.11 apply + intro | n/a: none |
| 1.12 redundant show | n/a: none |
| 1.13 have projections | n/a: none |
| 1.14 consecutive rw | tried merging product-single rewrite; needed explicit h function to infer correctly; terminal simp is shorter |
| 1.15 terminal simp only | n/a: no squeezed terminal simp |
| 1.16 nonterminal simp | n/a: both final simp calls close their goals |
| 1.17 dot notation | existing prod/erase notation retained; no additional applicable shortening |
| 1.18 parenthesis removal | n/a: parenthesized product-function argument groups syntax; no terminal proof parentheses |
| 1.19 push_neg | n/a: absent |
| 1.20 trivial existential | n/a: equality helper |
| 2.1 grind | actual whole-goal attempt failed with opaque product equality |
| 2.2 delete before grind | n/a: no successful grind to retain |
| 2.3 simpa consolidation | replaced final assembly with direct terminal simp; no external result requiring simpa |
| 2.4 fun_prop | n/a: no analytic function property |
| 2.5 positivity | n/a: no sign/nonzero goal |
| 2.6 gcongr | n/a: no order target |
| 2.7 lia/omega | n/a: coordinate cases already close by simplification; no remaining linear arithmetic goal |
| 2.8 aesop | actual whole-goal attempt failed, made no progress |
| 2.9 norm_num/norm_cast | n/a: no concrete numeric or cast computation |
| 2.10 decide | n/a: arbitrary semiring/function equality, not finite computation |
| 2.11 field_simp; ring | n/a: no denominators or field structure |
| 2.12 linear_combination | n/a: no ring/ring_nf ending and no polynomial linear combination needed |
| 2.13 wlog | n/a: coordinate equality/inequality cases have different meanings, both already one shared simp |
| 2.14 calc collapse | n/a: no calc |
| 2.15 shared closing tactic | retained `<;> simp` for both coordinate cases |
| 3.1 erw | n/a: absent |
| 3.2 continuity/measurability | n/a: absent |
| 3.3 omega→lia | n/a: neither tactic used |
| 3.4 rfl substitution | retained obtain rfl branch with automatic substitution |
| 3.5 automation registration | no global attribute needed for private helper; existing mathlib simp API used locally |
| 3.6 simp_all only | n/a: no simp_all only |
| 3.7 limits | n/a: none present or added |

## Step 4 — experiments and reflection

Live multi-attempt probes tried `grind`, `simp [hi]`, `aesop`, `exact?`, `apply?`
at the main goal. None closed it: the first four report direct failures/no progress,
while apply? suggested unrelated unit/inverse obligations. The tool also reports
trailing old-source parse diagnostics when replacing a nested have line; those are
probe artifacts, not final-source results. No completion claim relies on them.

At the final assembly goal, a merged rw with an unconstrained `pow_zero _` did not
infer the product function; explicitly supplying `(h := fun j e ↦ α j ^ e)` works.
Plain simp with h/product-add/pow-add expands `single_tsub` too early and leaves a
product over a difference. Disabling precisely that rewrite closes the whole goal.
The selected proof compiled independently with only the original imports and
preceding declarations; it cannot use the target or later theorem circularly.
The extensional equality remains useful proof content; inlining it into a term
would hide its two-coordinate argument without shortening the mathematics.

## Verification and gates

- `/Users/ramin/.elan/bin/lake build Roth.Taylor`: final exit 0, 1439 jobs,
  Taylor built in 12s; `/private/tmp/roth-taylor-prod-module.log`.
- Complete `lean_diagnostic_messages`: success true, partial false, timed_out false,
  no failed dependencies; only preserved header warning, no target warnings/errors.
- Isolated selected proof and original-type application: `lake env lean
  /private/tmp/roth-taylor-prod-final.lean`, exit 0. Log
  `/private/tmp/roth-taylor-prod-final.log`. The subsequent live change only repacked
  identical signature tokens; final module and LSP were rerun after that formatting.
- `#print axioms`: exactly propext, Classical.choice, Quot.sound.
- CommMonoid candidate exit 0; Monoid candidate exit 1 (missing CommMonoid); hi-drop
  exit 1 (unsolved singleton coordinate). These failed scratch experiments were never
  introduced into the live file.
- Source diff compared against baseline: only owned declaration. No definitions,
  docstrings, imports, attributes, theorem contract, or other declarations changed.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | actual final module command exit 0 |
| definition_protected | pass | no def/abbrev edits |
| theorem_statement_protected | pass | same binders/instance/conclusion modulo whitespace and lambda spelling; original-type application compiles |
| structure_gate | pass | 5-line body; no conjunction; no >10-line branch |
| naming_gate | pass | mathematical snake_case name, no forbidden pattern |
| line_packing_gate | pass | all three final signature lines measured above, no repack row |
| inequality_orientation_gate | pass | no reversed inequality occurrences |

Overall: pass. Parent owns full project and separate LeanEval dependent gates.
Source frozen and ownership released after final module/LSP verification:
`58a982948ba48df089ea5e4a00e8050fb00566e381e9a942279484ac88e0818e`.

## Result and checklist

Before 11 lines; after 8; saved 3. Audit issues 3; fixed 3. Rules applied:
1.3/1.9/2.3 (terminal simplification and compatibility-lambda removal), retained
2.15/3.4; signature packing and ↦ style. Gates pass. Renames queued: none.
Comments preserved: none present. Refactoring needed: none.

- [x] Step 1 — mandatory references read.
- [x] Step 2 — all 24 audit items recorded.
- [x] Step 2.5 — five-method search with unavailable-service limitation.
- [x] Step 2.6 — every parameter, actual applicable weakening probes, private literature exemption.
- [x] Step 2.7 — before/after signature codepoint tables.
- [x] Step 2.8 — inequality scan table.
- [x] Step 3 — all 42 golfing rules have concrete status.
- [x] Step 4 — actual automation/direct-lemma experiments and reflection.
- [x] Step 5a — complete clean target LSP diagnostics.
- [x] Step 5b — actual module build and all diff gates.
- [x] Step 6a — no rename required.
