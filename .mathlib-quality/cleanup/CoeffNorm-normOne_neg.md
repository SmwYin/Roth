# Phase 4: Roth.normOne_neg

Scope: `Roth/CoeffNorm.lean`, lines 81–82. Fresh single-declaration audit; only this
proof and this report are owned. No Git commands or shared-log edits. Pinned
`leanprover/lean4:v4.34.0`; dependencies unchanged. Baseline full build and separate
LeanEval passed upstream (session 55968); independently obtained complete baseline LSP.

Before (2 declaration lines):
```lean
theorem normOne_neg (P : MvPolynomial σ ℤ) : normOne (-P) = normOne P := by
  simp [normOne, support_neg]
```

After (2 declaration lines; one redundant simp argument removed):
```lean
theorem normOne_neg (P : MvPolynomial σ ℤ) : normOne (-P) = normOne P := by
  simp [normOne]
```

SOURCE FROZEN: whole-file SHA256
`12422f3bbb5a494633eede6148bc384c1c3eff739be1aa3c00181dabea5d7423`.
All source edits finished before this freeze; ownership was explicitly revoked upstream.

## Step 1 — References

Read both `/Users/ramin/.codex/skills/mathlib-quality/SKILL.md` and
`/Users/ramin/.codex/skills/lean4/SKILL.md`, the full worker contract
`/private/tmp/roth-coeffnorm-worker-contract.md`, and the complete reference files
`golfing-rules.md`, `proof-patterns.md`, `mathlib-search.md`,
`generalisation-patterns.md`, `cleanup-gates.md`, `style-rules.md`, and
`naming-conventions.md`. Also consulted `mathlib-review-stages.md` for normal forms
and syntactic generality. References are under the mathlib-quality skill directory.
Large initial outputs were reread in smaller ranges where truncated.

## Step 2 — Full audit (24 items)

1. LINT: no diagnostic in lines 80–82; complete baseline and final LSP have zero errors.
   Six unrelated pre-existing warnings remain: header (1), unused DecidableEq in
   normOne_mul_le (89), normOne_prod_le (104), normOne_det_le (122),
   abs_coeff_det_hasseDeriv_le (294), and hC (125). Scope does not authorize those edits.
2. HAVE SCAN: none; the body contains one simp call, no local facts.
3. SET_OPTION: none in target; no limit changes or suppression introduced.
4. SIMP SQUEEZE: sole simp is terminal. Tested removing support_neg successfully;
   retain unsqueezed `simp [normOne]`. `simp?` confirms support_neg already participates.
5. NAMING: normOne is the defined subject; suffix neg describes the operation.
   No forbidden abbreviation or numeric/single-letter pattern. No rename necessary.
6. LINE PACKING: measured signature is 75 codepoints; complete one-line signature.
   Per-line table below, including width-100 #check evidence.
7. BY PLACEMENT: by remains at the end of the signature line.
8. FORMAT: two-space proof indent, one tactic, no internal blank, no semicolon,
   no haveI/letI or trailing whitespace.
9. COMMENTS: no inline proof comments; preserved the existing one-sentence docstring.
10. DOCSTRING: existing public docstring states negation invariance; unchanged under
    Lean Rule A and explicit dispatch instructions.
11. VISIBILITY: public reusable norm API, explicitly preserved; no private helper.
12. STRUCTURE: one proof-body line, no conjunction and no case branch; no extraction.
13. MATHLIB: all five methods below find reusable support/coefficient negation facts.
    Keep the existing project-defined norm API; broad migration is outside this scope.
14. JUNK DEF: n/a — theorem, no definition introduced or edited.
15. EXISTS LEMMA: n/a — equality theorem, not a private existential helper.
16. SHOW vs CHANGE: n/a — neither occurs.
17. PUSH_NEG: n/a — none occurs.
18. GENERALISE: all elaborated parameters σ and P audited and actually drop-tested;
    universe and concrete coefficient candidates tested below.
19. INEQUALITY: no ≥ or > in signature or hypotheses; occurrence table below.
20. NORMAL-FORM: already canonical negated-input-to-unnegated-output equality.
    No competing equivalent proposition or O(n²) equivalence family.
21. SYNTAX-GEN: OK; explicit polynomial is directly usable in rw. A bundled seminorm
    would be a cross-declaration representation change, not an inline improvement.
22. IMPORT-FANOUT: n/a — no import change.
23. CASTS: 0 dropped / 0 kept cross-type / 0 kept load-bearing in diff; none present.
24. INSTANCE-NAME: n/a — target is a theorem and adds no instance.

Issues found: one redundant simp argument. Fixed: one. Refactoring needed: none for
this declaration. The six file-wide warning decisions remain with the file owner.

## Step 2.5 — Mathlib search status

Native Lean MCP was discovered through ALL_TOOLS metadata and responded without stalls.
Fallback script/schema paths were inspected but were unnecessary.

| Method | Actual query/action | Result |
|---|---|---|
| A Lean-Finder | sum absolute values coefficients multivariate polynomial invariant negation | coeff_neg, degrees_neg, Polynomial.signVariations_neg |
| B Loogle | `MvPolynomial.support (-_)` | MvPolynomial.support_neg |
| C LeanSearch | support of negation of multivariate polynomial equals support | Polynomial.support_neg, MvPolynomial.support_neg, Finsupp.support_neg |
| D source grep | untruncated normOne_neg/support_neg/norm_neg in MvPolynomial and normed group source; inspected CommRing.lean | support_neg is already tagged simp at line 75; coeff_neg available |
| E local name search | support_neg (limit 10) | MvPolynomial, Finsupp and other support_neg results; index warming, so not used to establish absence |

Auxiliary variants considered and found: coeff_neg, Finsupp.support_neg, degrees_neg;
generic norm_neg was probed but is not imported in this module (unknown identifier).
Common-equivalents lookup: no discrete/finiteness/separation/boundedness match.
The standard norm route would require changing the custom norm representation.
Actual live `exact?` fails on the original goal; `apply?` supplies only Real.ext_cauchy
goals and a sorry warning in its temporary attempt, not a completed proof.
No sorry entered source. Conclusion: partial mathlib matches; existing proof uses their
registered simp API after unfolding normOne. No new wrapper or declaration added.
Rules 1/5 do not authorize deleting this existing public signature under the explicit
session contract. Rules 2/3 satisfied by searches and actual generic-route probes;
Rule 4 n/a (no custom hypothesis predicate); Rule 6 recorded here without changing docs.

## Step 2.6 — Generalisation status

Each candidate was tested in isolated native lean_run_code, preserving live public API.
No anonymous-instance/typeclass/proposition parameters are hidden: #check lists only σ,P.

| # | Parameter | Class / usage | Mechanical candidates tried | Verified? | Result |
|---|---|---|---|---|---|
| 1 | `{σ : Type*}` | type-variable; exponent index | drop with autoImplicit false; explicit `Type u` | yes | drop fails unknown σ; universe-u proof succeeds, already universe polymorphic |
| 2 | `(P : MvPolynomial σ ℤ)` | structure-value; both sides | drop with autoImplicit false; concrete ℤ→ℝ coefficient proposal | yes | drop fails unknown P; ℝ proposal fails expected MvPolynomial _ ℤ |

Parent-typeclass weakening: n/a, no typeclass hypothesis. Point-localise: n/a, no
global analytic/property hypothesis. Strict→weak: n/a, no ordered assumption.
Unbundle: n/a, no bundled hypothesis. Decidability: n/a, none required. Type* already
quantifies an arbitrary universe. P cannot be removed without changing the statement.

Inversion check: after unfolding normOne, the content is finite sums of an even weight.
Actual compiled abstract candidate succeeds:
```lean
example {ι : Type*} {G : Type*} [AddGroup G] (g : G → ℝ) (h : ∀ x, g (-x) = g x)
    (f : ι →₀ G) : (∑ x ∈ (-f).support, g ((-f) x)) = ∑ x ∈ f.support, g (f x) := by
  simp [h]
```
This uses existing Finsupp simp API and needs no new helper. No useful missing abstract
result surfaced. Big-change candidates: general norm/coefficient-space migration only;
not proposed as necessary work, since it changes the definition/public representation.
No public unused parameter was found or removed.

### Public literature search

Web query: `polynomial coefficient l1 norm negation norm generalization`.
Top three returned hits recorded and screened:

1. [ECCC TR26-127](https://eccc.weizmann.ac.il/report/2026/127/) — coefficient ℓ¹ bounds
   for approximating polynomials; not needed to establish this elementary invariance.
2. [LTlib ℓ¹ companion](https://allenhaozhu.github.io/LTFP-Lean/wiki/concepts/l1-norm/)
   — reports ℓ¹ negation invariance; secondary companion, not relied on as authority.
3. [Yin et al., PMLR 97](https://proceedings.mlr.press/v97/yin19b.html) — norm-constrained
   generalization bounds; not a useful assumption weakening for this theorem.

Finding: no literature-driven change to the preserved public theorem. The abstract
even-weight Finsupp observation above is independently compiler checked; it is not
inferred from unrelated search hits. ChatGPT math MCP: unavailable (no matching tool
in ALL_TOOLS); no external mathematical second opinion claimed. Local source clean.tex
was searched for coefficient/norm context; this result is an elementary auxiliary norm
identity rather than a separate numbered claim in the paper.

## Step 2.7 — Line packing

Successful `set_option format.width 100; #check @Roth.normOne_neg` output:
```lean
@Roth.normOne_neg : ∀ {σ : Type u_1} (P : MvPolynomial σ ℤ), Roth.normOne (-P) = Roth.normOne P
```

| Signature line | Codepoints | Next signature token | Current + 1 + next | Action |
|---|---:|---|---|---|
| 81 | 75 | none; body follows | n/a — complete signature on one line | ok |

Body line 82 is 16 codepoints. Packing both on one physical line would be 75+1+14=90,
but keeping a two-space one-tactic proof line preserves existing declaration style;
the signature packing gate does not demand moving the proof onto its signature line.

## Step 2.8 — Inequality scan

| # | Location | Original | Rewrite | Lemma rename? |
|---|---|---|---|---|
| 1 | signature and every hypothesis | n/a — zero ≥/> occurrences | none | no _ge_/_gt_ in name |

## Step 3 — Every golfing rule

- 1.1 by exact: n/a, no exact wrapper.
- 1.2 by rfl: tried rfl; fails definitional equality, no rfl wrapper to remove.
- 1.3 rw+exact: n/a, neither present.
- 1.4 simp+exact: n/a, simp already terminal.
- 1.5 trailing rfl: n/a, no trailing tactic.
- 1.6 constructor: n/a, equality not structure construction.
- 1.7 apply+exact: n/a, neither present.
- 1.8 by_contra: n/a, no contradiction block.
- 1.9 eta: n/a, no lambda in live body.
- 1.10 inline have: n/a, no have.
- 1.11 apply+intro: n/a, neither present.
- 1.12 show: n/a, absent.
- 1.13 projections: n/a, no have or projection.
- 1.14 merge rw: n/a, no rewrites.
- 1.15 terminal simp only: already unsqueezed; retain terminal simp and remove redundant support_neg.
- 1.16 nonterminal simp: n/a; simp? tested for evidence, no squeeze retained.
- 1.17 dot notation: n/a, no function application improved by it.
- 1.18 <|: n/a, no trailing argument parentheses.
- 1.19 push Not: n/a, no push_neg.
- 1.20 existential helper: n/a, neither private nor existential.
- 2.1 grind: actually tried; fails to refute ¬normOne(-P)=normOne P.
- 2.2 pre-grind tactics: n/a, no grind retained.
- 2.3 simpa consolidation: n/a, no post-simp closing step to consolidate.
- 2.4 fun_prop: n/a, no function property goal.
- 2.5 positivity: n/a, equality not positivity/nonzero goal.
- 2.6 gcongr: n/a, no monotonicity/inequality.
- 2.7 lia/omega: n/a, no natural/integer arithmetic goal.
- 2.8 aesop: actually tried; fails with unchanged goal.
- 2.9 norm_num/norm_cast: n/a, no computation or cast goal.
- 2.10 decide: n/a, arbitrary real equality and arbitrary polynomial not finite computation.
- 2.11 field_simp/ring: n/a, no denominator/ring-expression identity.
- 2.12 linear_combination: n/a, no ring-ending proof or algebraic hypotheses.
- 2.13 wlog: n/a, no symmetric branches.
- 2.14 calc composition: n/a, no calc.
- 2.15 <;>: n/a, one goal closed by simp.
- 3.1 erw→rw: n/a, neither present.
- 3.2 fun_prop migration: n/a, no continuity/measurability.
- 3.3 omega→lia: n/a, no arithmetic tactic.
- 3.4 rcases rfl: n/a, no cases or substitutions.
- 3.5 automation attributes: no change; touching public simp normal forms is outside scope.
- 3.6 simp_all: n/a, no simp_all only or useful local hypotheses.
- 3.7 heartbeat removal: n/a, no local override.

## Step 4 — Reflection and actual probe outcomes

Mathematically, negation preserves the exponent support and negates each coefficient;
absolute value removes the sign. One terminal simp after unfolding expresses this
directly. Actual live multi-attempt: rfl fails; bare simp makes no progress;
`simp [normOne]` and original `simp [normOne, support_neg]` both close with no diagnostics;
`simp? [normOne]` suggests support_neg, AddMonoidAlgebra.coeff_neg, Finsupp.coe_neg,
Pi.neg_apply, Int.cast_neg, abs_neg. Bare grind/aesop fail. exact? finds no closing term;
apply? leaves Cauchy-equality subgoals. Do not count its empty goals array as success:
its diagnostics explicitly include temporary sorry. The final proof is the shortest
tested meaningful one-tactic proof. No term-mode lemma avoids unfolding the local def.

One early scratch probe used nonexistent pp.width and an unimported norm_neg; those
errors were corrected by using format.width and the available support/coeff API.
They never affected the live file.

## Steps 5a/5b — Verification and gates

Final full native `lean_diagnostic_messages(Roth/CoeffNorm.lean, timeout_s=30)`:
success=true, partial=false, timed_out=false, failed_dependencies=[], zero errors,
the same six pre-existing outside warnings. No warning in target.

Actual `/Users/ramin/.elan/bin/lake build Roth.CoeffNorm`, session 62505: exit 0,
`Built Roth.CoeffNorm (19s)`; build completed successfully (1658 jobs).

Independent native code probe successfully typechecks the original full type and
reproves the original statement without using Roth.normOne_neg:
```lean
example : ∀ {σ : Type*} (P : MvPolynomial σ ℤ), Roth.normOne (-P) = Roth.normOne P :=
  @Roth.normOne_neg
theorem normOne_neg_independent {σ : Type*} (P : MvPolynomial σ ℤ) :
    Roth.normOne (-P) = Roth.normOne P := by
  unfold Roth.normOne
  rw [MvPolynomial.support_neg]
  exact Finset.sum_congr rfl fun d _ ↦ by simp
```
Both #print axioms results are exactly `[propext, Classical.choice, Quot.sound]`.
Native scratch imports reported cached-import info after rebuild; a fresh CLI probe
`lake env lean /private/tmp/coeffnorm-normOne_neg-final.lean` supplies final independent
artifact verification: session 75775 exited 0, printed the preserved full original type,
and printed `[propext, Classical.choice, Quot.sound]` for both the original theorem
and its independent reproof, with no stale-import message or compiler warning.

Actual snapshot comparison checked whole_file_exact_expected_edit=True: the entire
source equals the initial snapshot with exactly one replacement of the redundant
simp argument. Signature_unchanged=True; scoped forbidden-token scan empty;
reversed inequality count 0; body_lines=1; frozen SHA reproduced.

| Gate | Result | Actual evidence |
|---|---|---|
| lake_build_file | ✓ pass | module build session 62505 exit 0 |
| definition_protected | ✓ pass | exact whole-file snapshot replacement; no def/abbrev touched |
| theorem_statement_protected | ✓ pass | original signature and docs byte-identical; compiled full-type check |
| structure_gate | ✓ pass | one proof line, no conjunction/branches |
| naming_gate | ✓ pass | descriptive subject+neg suffix; no forbidden pattern |
| line_packing_gate | ✓ pass | all signature lines covered; sole line 75 codepoints |
| inequality_orientation_gate | ✓ pass | explicit occurrence scan and measured zero |

Overall: pass. No renamed declarations, no new axioms, no source sorry/admit, no
suppression, no definition-value/public-signature change. No full build run by this worker.

## Step 6 — Result

Before: 2 lines. After: 2 lines. Saved: 0 lines; removed one redundant argument.
Audit issues found: 1. Fixed: 1. Refactoring deferred: 0 for this declaration.
Rules applied: terminal-simp simplification under 1.15/Step 4.
Renames queued: none (no rename required, no shared sidecar edit).
Comments preserved: existing docstring byte-identical; no inline comments present.
Pending: file-owner decisions on the six pre-existing warnings, outside this scope.

- [✓] Step 1 — reference docs read.
- [✓] Step 2 — full 24-item audit printed.
- [✓] Step 2.5 — five-method mathlib search status printed.
- [✓] Step 2.6 — every-parameter generalisation and literature status printed.
- [✓] Step 2.7 — per-signature-line codepoint packing table printed.
- [✓] Step 2.8 — per-occurrence inequality scan table printed.
- [✓] Step 3 — all 42 golfing rules have individual status lines.
- [✓] Step 4 — reflection and actual candidate probes recorded.
- [✓] Step 5a — complete final LSP diagnostics, no errors or target warning.
- [✓] Step 5b — actual module build and diff gate table printed.
- [✓] Step 6a — no required rename; no sidecar mutation.
