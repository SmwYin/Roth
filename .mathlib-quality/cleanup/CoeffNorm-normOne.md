# Phase 4 audit: `Roth.normOne`

Single-declaration worker; `Roth/CoeffNorm.lean:42`, one source line (docstring at 41).
Before: 1 line. After: 1 line. Saved: 0. Source edits: none. Docstring, public API,
definition value, and implicit universe parameter preserved exactly. No Git operations.
The file owner's import reorder is outside this worker's changes.

## Step 1 — references

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md in full. Also read both complete
`mathlib-quality/SKILL.md` and `lean4/SKILL.md`, the complete 853-line worker contract,
the applicable style and naming rules, the normal-form/syntactic-generality/documentation
sections of mathlib-review-stages.md, the complete target file, and clean.tex:439–465.
Paths: `/Users/ramin/.codex/skills/mathlib-quality/references/` and
`/Users/ramin/.codex/skills/lean4/SKILL.md`.

Source frozen without edits at whole-file SHA256
`1290a45f7dbbe5f2a37df1dfd7cb9718884fad6f1d6ae903c0afcf7dbbee9c5b`.
Ownership subsequently revoked by the file owner; only this report was written afterward.

## Step 2 — full audit

| Item | Concrete result |
|---|---|
| 1 LINT | None at the declaration. Complete LSP has zero errors; the known header, four other DecidableEq warnings and other declaration's `hC` warning remain outside this worker's ownership. |
| 2 HAVE SCAN | n/a: the complete body is one sum term and contains zero `have` expressions. |
| 3 SET_OPTION | n/a: no per-declaration options. |
| 4 SIMP SQUEEZE | n/a: no simp calls. |
| 5 NAMING | `normOne` returns real data and follows lowerCamelCase; it describes the coefficient ℓ¹ norm. No forbidden abbreviation, numerical scheme, single-letter name, `_ge_`, or `_gt_`. No rename needed. |
| 6 LINE PACKING | Full source line is 96 codepoints; signature through `:=` is 55. Complete one-row table below. |
| 7 BY PLACEMENT | n/a: term definition has no `by`. |
| 8 FORMAT | Flush-left one-line term, spaces around operators, no blank internal lines, no tactics/semicolons/`haveI`/`letI`. |
| 9 COMMENTS | No inline comments; existing one-line docstring preserved exactly. |
| 10 DOCSTRING | Existing single sentence identifies ℓ¹ coefficient norm and source §3; preserved under task/API instruction. |
| 11 VISIBILITY | Public main definition listed in module docstring and foundation of substantial norm API; retain public. |
| 12 STRUCTURE | One term line, no conjunction or branches; no extraction needed. |
| 13 MATHLIB | Five searches and compiled generic coefficient-sum comparison below; generic sum machinery is already used directly. |
| 14 JUNK DEF | Keep: domain-specific coefficient norm with nonnegativity, zero, monomial, addition, negation, sum, multiplication, product, determinant, Hasse derivative, and coefficient estimates. It names a central mathematical object used repeatedly, rather than a single-use convenience expression. |
| 15 EXISTS LEMMA | n/a: definition of real data, not an existential lemma. |
| 16 SHOW vs CHANGE | n/a: no `show` or tactic proof. |
| 17 PUSH_NEG | n/a: no negation tactics. |
| 18 GENERALISE | Both actual parameters probed below. Already arbitrary universe and variable type; no hypotheses/instances to weaken. A generic coefficient functional compiles, but would change the public contract and is only an optional future API direction. |
| 19 INEQUALITY | Zero inequalities in signature/body; table below. |
| 20 NORMAL-FORM | Finite support sum of absolute real coefficient values is the coefficient ℓ¹ norm in clean.tex. Generic Finsupp.sum gives the same value (compiled proof below). No competing normal form is needed. |
| 21 SYNTAX-GEN | OK: implicit arbitrary variable type and one explicit polynomial argument permit direct use at all existing sites. Bundling into a new norm structure would be an API redesign, not an application improvement required here. |
| 22 IMPORT-FANOUT | n/a: this worker introduced no imports. |
| 23 CASTS | Diff: 0 dropped / 0 introduced cross-type / 0 introduced load-bearing casts, because source diff is empty. Existing ℤ→ℝ coercion implements the intended real-valued norm. Existing inner ℤ annotation was left unchanged under definition-value preservation; no claim it is essential. |
| 24 INSTANCE-NAME | n/a: this declaration is a `def`, with no instance declarations. |

Issues to fix: none. Refactoring needed: none required. Optional future generic API is
described below, without a requested source change.

## Step 2.5 — Mathlib search-status

| Method | Actual query and result |
|---|---|
| A Lean-Finder | `l1 norm of multivariate polynomial sum absolute values coefficients` (3 results): `Polynomial.gaussNorm`, `Polynomial.mahlerMeasure_le_sum_norm_coeff`, `Polynomial.sum`. Gauss norm is a weighted supremum, not this sum; the others are univariate generic machinery/estimates. |
| B Loogle | `MvPolynomial _ ℤ → ℝ` (3 requested): empty successful result. This is search evidence, not a proof of absence. |
| C LeanSearch | `sum of norms of coefficients of a multivariate polynomial`: `Polynomial.mahlerMeasure_le_sum_norm_coeff`, `FormalMultilinearSeries.norm_apply_eq_norm_coef`, `MvPolynomial.eval_eq`. None supplies this named multivariate norm. |
| D rg source | Untruncated `normOne\|l1Norm\|norm.*coeff\|coeff.*norm` in normed, polynomial analysis, and MvPolynomial source; untruncated full-name patterns over Mathlib for `MvPolynomial.norm`, `MvPolynomial.l1Norm`, and `Finsupp.norm`. Found univariate supNorm/Gauss/Mahler APIs and unrelated NormOneClass instances. Direct Basic.lean inspection found `MvPolynomial.sum_def` at 519. |
| E local name | `normOne` returned this project API plus unrelated `NormOneClass`; `MvPolynomial.norm` returned fuzzy unrelated NewtonIdentities results. Both local index responses were `warming`, so neither is used to establish absence. |

Auxiliary variants considered: `sum_def`, `sum_norm`, `l1Norm`, coefficient sum,
`supNorm`, `gaussNorm`, and Mahler coefficient estimates. Common-equivalents lookup:
no discrete/finite/separation/bornology bucket matches.

Conclusion: found a partial match in generic coefficient summation (`MvPolynomial.sum_def`);
keep the local mathematical norm, whose body already uses finite summation directly.
No assertion of exhaustive global absence is made from the warming index or empty query.
No missing-API extraction signal occurs in the one-term definition. Definitions returning
ℝ cannot meaningfully use `exact? : ℝ` to detect the intended value (it could return zero),
so the generic route was instead checked by a compiled equality:

```lean
import Roth.CoeffNorm
example {σ : Type*} (P : MvPolynomial σ ℤ) :
    Roth.normOne P = (AddMonoidAlgebra.coeff P).sum (fun _ z ↦ |(z : ℝ)|) :=
  (MvPolynomial.sum_def (p := P) (b := fun _ z ↦ |(z : ℝ)|)).symm
```

Native `lean_run_code`: success true, timed_out false, zero diagnostics. Earlier scratch
`P.sum` failed because AddMonoidAlgebra has no such field; bare `sum_def.symm` failed
implicit argument inference. The explicit `p` and `b` above repair both scratch issues.
No scratch code was installed in the source.

## Step 2.6 — generalisation status

| # | Parameter | Class | Used as | Mechanical candidates tried | Verified? | Result |
|---|---|---|---|---|---|---|
| 1 | `{σ : Type*}` (implicit section parameter) | type-variable/universe | variable type of polynomial and exponent | drop σ binder under `autoImplicit false`; arbitrary higher universe `ULift.{1} ℕ` | yes, native isolated elaboration | Drop fails `Unknown identifier σ` at line 3 column 52. Higher-universe polynomial compiles. Already universe polymorphic; no restriction to weaken. |
| 2 | `(P : MvPolynomial σ ℤ)` | structure-value | determines support and every coefficient | remove P binder under `autoImplicit false`; abstract coefficient ring/function proposal | yes, native isolated elaboration | Drop fails `Unknown identifier P.support` and `P.coeff` at line 4. Generic coefficient functional compiles below; specialization is definitionally equal. Public signature preserved. |

No typeclass, decidability, propositional, strict-order, global function-property, or
bundled-hypothesis parameters exist: parent-class, strict→weak, point-localisation and
unbundling catalogue entries therefore have no candidate on this signature. No unused
argument was found. Inversion check: n/a for proof abstraction, because this is a data
definition rather than a concrete theorem proved by abstract reasoning.

Both final drop probes used `import Roth.CoeffNorm`, so the only failures were the
deliberately removed identifiers. Initial overly small-import scratch probes also lacked
ℝ; those were superseded and are not the claimed final evidence.

Compiled optional restatement experiment, not applied:

```lean
noncomputable def coefficientSumProbe {σ R : Type*} [CommSemiring R]
    (f : R → ℝ) (P : MvPolynomial σ R) : ℝ := ∑ d ∈ P.support, f (P.coeff d)
example {σ : Type*} (P : MvPolynomial σ ℤ) :
    coefficientSumProbe (fun z : ℤ ↦ |(z : ℝ)|) P = Roth.normOne P := rfl
```

This supplies generic coefficient summation, not a proof of norm laws under arbitrary `f`.
It is not recommended as a replacement for the existing specialized norm API. An initial
`[Norm R]` experiment lacked that class in the imports; the final functional experiment
above compiles with no additional imports. Big-change candidates requiring action: none.

### Literature search status

A. Web query: `polynomial l1 norm sum absolute coefficients generalization normed ring`.
Top three returned hits: [Rings implementation](https://github.com/PoslavskySV/rings/blob/develop/rings/src/main/java/cc/redberry/rings/poly/univar/UnivariatePolynomial.java),
[CRM PDF](https://citeseerx.ist.psu.edu/document?doi=183a21b05542f27456bedebb4bee879fc2fbe574&repid=rep1&type=pdf),
and [Richard Pink, The Strong Nullstellensatz for Certain Normed Algebras](https://arxiv.org/abs/1603.01439).
Opened the first and third primary sources. Pink's abstract treats the coefficient ℓ¹
norm for complex polynomials in finitely many variables; hence the integer coefficient
case is mathematically a specialization. This supports a possible broader normed-ring
API, but does not imply the current integer-focused Roth development needs that redesign.
The CRM hit is only recorded as a query hit, not relied on for a technical claim.
Local clean.tex:446–452 defines the coefficient sum for this proof; the Lean value matches it.
B. ChatGPT math MCP: n/a — no such tool exists in the available tool inventory.
Literature-driven mandatory refactoring candidates: none; no hypotheses are redundant.

## Step 2.7 — line packing

Exact native output with `set_option format.width 100` and `#check @Roth.normOne`:

```text
@Roth.normOne : {σ : Type u_1} → MvPolynomial σ ℤ → ℝ
```

| Sig line | Chars | Next signature token | current + 1 + next ≤ 100? | Action |
|---|---:|---|---|---|
| 42 through `:=` | 55 | none: same-line term body follows | n/a: no next signature line | ok |

The entire source line, including body, is 96 Unicode codepoints (measured with Python
`len` on the exact source line); there is no wrap or dangling conclusion to repack.

## Step 2.8 — inequality scan

| # | Location | Original | Rewrite | Lemma rename? |
|---|---|---|---|---|
| 1 | complete signature and hypotheses | n/a: no `≥` or `>` | none | n/a: name contains neither `_ge_` nor `_gt_` |

## Step 3 — all 42 golfing rules

Each n/a below is based on the complete one-term data definition. Automation is for
proving propositions and is not substituted for a prescribed mathematical data value.

| Rule | Status |
|---|---|
| 1.1 by exact wrapper | n/a: no tactic wrapper. |
| 1.2 by rfl | n/a: no reflexivity proof. |
| 1.3 rw + exact | n/a: no rewrites or exact tactics. |
| 1.4 simp + exact | n/a: no simp or exact. |
| 1.5 trailing rfl | n/a: no proof tactics. |
| 1.6 anonymous constructor | n/a: value is a scalar sum, not a structure proof. |
| 1.7 apply + exact | n/a: no apply or exact. |
| 1.8 by_contra! | n/a: no contradiction reasoning. |
| 1.9 eta-reduce | n/a: source contains no explicit lambda abstraction. |
| 1.10 inline have | n/a: no local `have`. |
| 1.11 refine + fun | n/a: no apply/intro. |
| 1.12 redundant show | n/a: no `show`. |
| 1.13 obtain | n/a: no conjunction projections or have. |
| 1.14 merge rw | n/a: no rewrites. |
| 1.15 unsqueeze terminal simp | n/a: no simp. |
| 1.16 squeeze nonterminal simp | n/a: no simp. |
| 1.17 dot notation | n/a: existing `P.support` and `P.coeff` already use dot syntax. |
| 1.18 use <\| | n/a: no trailing function-call parentheses to eliminate. |
| 1.19 push Not | n/a: no negation tactics. |
| 1.20 existential inline | n/a: not an existential lemma. |
| 2.1 grind | n/a: no multi-line tactic proof or proposition goal. |
| 2.2 delete before grind | n/a: no grind. |
| 2.3 simpa consolidation | n/a: no simp/closing tactic chain. |
| 2.4 fun_prop | n/a: no continuity/measurability goal. |
| 2.5 positivity | n/a: defines data; no positivity proof goal. |
| 2.6 gcongr | n/a: no inequality goal. |
| 2.7 lia / omega | n/a: no arithmetic proposition. |
| 2.8 aesop | n/a: no logic or membership goal. |
| 2.9 norm_num / norm_cast | n/a: no numeric/cast proof goal. |
| 2.10 decide +kernel | n/a: arbitrary polynomial value, not finite decidable proposition. |
| 2.11 field_simp; ring | n/a: no denominator identity. |
| 2.12 linear_combination | n/a: no ring proof or hypotheses. |
| 2.13 wlog | n/a: no cases. |
| 2.14 collapse calc | n/a: no calc. |
| 2.15 <;> | n/a: no subgoals. |
| 3.1 erw → rw | n/a: no erw. |
| 3.2 fun_prop | n/a: no legacy continuity tactics. |
| 3.3 omega → lia | n/a: no omega. |
| 3.4 rcases rfl | n/a: no rcases. |
| 3.5 automation attributes | n/a: this is a norm value definition, not a proposition to register. |
| 3.6 simp_all | n/a: no simp_all. |
| 3.7 remove limits | n/a: no maxHeartbeats/maxRecDepth option. |

Rules applied: none. This is already the intended one-line term; preserving it avoids
unnecessary definitional/API churn.

## Step 4 — reflection

There is no tactic proof to compress: the sum is the mathematical definition. Replacing
it with an unconstrained automated construction of a real number would not preserve the
value. The generic Finsupp coefficient sum is equivalent, as the compiled comparison
shows, but obscures the immediate support-sum formula without shortening this one line.
No have blocks, redundant proof steps, alternate proof strategy, helper extraction or
automation registration improve this declaration. Existing API justifies keeping the name.

## Step 5a — diagnostics and independent checks

Final native `lean_diagnostic_messages` on the whole file: `success: true`,
`partial: false`, `timed_out: false`, `failed_dependencies: []`; zero errors.
Exactly the six known outside-scope warnings remain; no warning refers to normOne itself.

Final isolated native `lean_run_code` succeeded (true, timed_out false), checking:

```lean
import Roth.CoeffNorm
noncomputable section
set_option format.width 100
#check @Roth.normOne
#print axioms Roth.normOne
example : {σ : Type*} → MvPolynomial σ ℤ → ℝ := @Roth.normOne
example {σ : Type*} (P : MvPolynomial σ ℤ) :
    Roth.normOne P = ∑ d ∈ P.support, |((P.coeff d : ℤ) : ℝ)| := rfl
example (P : MvPolynomial (ULift.{1} ℕ) ℤ) : 0 ≤ Roth.normOne P := Roth.normOne_nonneg P
```

Axioms output: `[propext, Classical.choice, Quot.sound]` only. The `rfl` example
independently verifies exact original value; the function assignment verifies the original
type including polymorphic σ. This is data, not a proof declaration, so value equality is
the corresponding original-proof preservation check. Initial stale-import probe failed
before module rebuild; initial assignment outside `noncomputable section` failed codegen.
Both were repaired in the final successful isolation above; neither failure touched source.

## Step 5b — gate status

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | ✓ pass | `/Users/ramin/.elan/bin/lake build Roth.CoeffNorm`, PTY session 89974, exit 0: `Build completed successfully (1658 jobs).` Target compilation reported 21s. |
| definition_protected | ✓ pass | Empty worker source diff; original definition unchanged byte-for-byte. |
| theorem_statement_protected | ✓ pass | No theorem source touched. |
| structure_gate | ✓ pass | One body line, no conjunction/branches. |
| naming_gate | ✓ pass | Descriptive lowerCamelCase data name, no forbidden pattern. |
| line_packing_gate | ✓ pass | Complete one-row table; 55-char signature, 96-char full line. |
| inequality_orientation_gate | ✓ pass | Complete zero-occurrence table; zero reverse inequalities. |
| original type/value and axioms | ✓ pass | Independent compiled assignment and rfl equality; only three standard axioms. |

Overall: pass. Full project build belongs to file owner; this worker did not run it.

## Step 6 — result and checklist

Before: 1 line. After: 1 line. Saved: 0. Audit issues found: 0. Fixed: 0.
Refactoring deferred: 0 required. Renames queued: none; no shared sidecar modified.
Comments preserved: docstring 1 of 1, inline comments none. Pending: none for this declaration.

- [✓] Step 1 — reference documents read.
- [✓] Step 2 — full 24-item audit printed.
- [✓] Step 2.5 — all five search methods and generic comparison printed.
- [✓] Step 2.6 — every parameter/drop probe, universes, literature and optional abstraction recorded.
- [✓] Step 2.7 — complete measured line-packing table and width-100 #check printed.
- [✓] Step 2.8 — complete inequality scan table printed.
- [✓] Step 3 — all 42 golfing rules have concrete status.
- [✓] Step 4 — mathematical and proof-strategy reflection done.
- [✓] Step 5a — complete final LSP clean of errors, independent original-value/type check passed.
- [✓] Step 5b — all seven required diff gates printed and passed, actual module build exit 0.
- [✓] Step 6a — no rename required; no shared sidecar mutation.
