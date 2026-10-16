# Phase 4: MvPolynomial.taylor_taylor

Owned declaration: Roth/Taylor.lean:140–142. Baseline file SHA256
`fbd691573b1e1fa3dd2c4f33449095583791028ee6cbd25a8d92df2175e9ab39`.
Only the proof and ordinary lambda spelling changed. All public API and documentation preserved.

## References

Read lean4/SKILL.md, mathlib-quality/SKILL.md, full worker contract,
golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, cleanup-gates.md, relevant style-rules.md and naming-conventions.md.

## Full audit

1. LINT: no declaration warnings. Existing file-header copyright warning preserved by user decision.
2. HAVE SCAN: no have statements.
3. SET_OPTION: none in declaration; no performance options added.
4. SIMP SQUEEZE: original terminal simp_all replaced with terminal unsqueezed simp.
5. NAMING: taylor_taylor describes composition, snake_case, no forbidden pattern or abbreviation.
6. LINE PACKING: measured table below; full conclusion cannot fit on keyword line.
7. BY PLACEMENT: by ends conclusion line.
8. FORMAT: two-space tactic indentation; ordinary lambda => changed to ↦.
9. COMMENTS: no proof comments; existing docstring preserved verbatim.
10. DOCSTRING: public statement has concise existing composition description.
11. VISIBILITY: public API retained as explicitly requested; no deletion of wrappers.
12. STRUCTURE: one-line body, no conjunction or long branch.
13. MATHLIB: five-method search below finds direct composition API.
14. JUNK DEF: n/a, theorem.
15. EXISTS LEMMA: n/a, equality rather than existential.
16. SHOW vs CHANGE: neither occurs.
17. PUSH_NEG: none.
18. GENERALISE: every parameter covered below; no safe weakening found.
19. INEQUALITY: zero reversed inequalities, table below.
20. NORMAL-FORM: nested translations become one translation by pointwise sum; canonical composition orientation.
21. SYNTAX-GEN: current applied equality supports rewriting at P directly. Bundled equality is available through generic comp_aeval; no public restatement needed.
22. IMPORT-FANOUT: n/a, no import changes.
23. CASTS: 0 dropped / 0 cross-type / 0 load-bearing; no explicit casts in diff.
24. INSTANCE-NAME: n/a, no instance declaration.

Issues found/fixed: induction can use direct composition API; ordinary lambda spelling. Both fixed.
Refactoring needed: none.

## Five-method mathlib search

A. Lean-Finder: `MvPolynomial composition aeval evaluation substitution` returned
   aeval_comp_bind₁, eval₂_cast_comp, aeval_comp_rename.
B. Loogle: initial `MvPolynomial.aeval, _ (_ _) = _` rejected placeholder function syntax;
   corrected `MvPolynomial.aeval, "comp"` returned comp_aeval and comp_aeval_apply.
C. LeanSearch: `multivariate polynomial algebra evaluation composition` returned
   comp_aeval_apply, comp_eval₂Hom, eval_eval₂, eval₂_comp_left.
D. Source rg: aeval_comp/aeval_aeval/comp_aeval in Algebra/MvPolynomial and
   RingTheory/MvPolynomial found Eval.lean:607/612. Full untruncated taylor_taylor search
   found Polynomial.taylor_taylor (univariate), not a duplicate MvPolynomial declaration.
E. lean_local_search `aeval_comp` returned source-backed aeval_comp_rename/expand etc.;
   index unavailable, so absence was not inferred. Source inspection and successful #check
   @MvPolynomial.comp_aeval_apply verified the selected declaration.

Auxiliary variants: comp_aeval, comp_aeval_apply, aeval_comp_bind₁, aeval_comp_rename,
eval₂_comp_left. Common-equivalents table: no applicable bucket.
Conclusion: generic partial match comp_aeval_apply supplies the proof. Retain the public
local API under explicit user instruction overriding wrapper-deletion guidance.

## Actual proof experiments

Native lean_multi_attempt at the live proof line 142:
- `simp [taylor, comp_aeval_apply, add_assoc]`: no goals, no diagnostics.
- `grind`: failed to prove equality.
- `aesop`: failed, made no progress.
- `exact?`: default heartbeat limit at whnf.
- `apply?`: default heartbeat limit at isDefEq.
No limits raised. Initial attempt accidentally targeted old line 158 and returned parser
errors for all snippets; those results were discarded and rerun at verified live line 142.
The original induction proof already compiled; direct simp removes induction entirely.

## Generalisation status

| Parameter | Class | Use | Candidates/test | Result |
|---|---|---|---|---|
| σ : Type* | type variable | polynomial variables and domain of α, β | drop with autoImplicit false | native run_code: unknown σ; already universe-polymorphic |
| R : Type* | type variable | coefficients and codomain | drop with autoImplicit false | unknown R; already universe-polymorphic |
| [CommSemiring R] | typeclass | required by taylor and MvPolynomial | drop; weaken to Semiring R | native run_code rejects both, failed synthesis CommSemiring R |
| α : σ → R | value | outer translation and sum | drop with autoImplicit false | unknown α; no point-local proposition or structure weakening applies |
| β : σ → R | value | inner translation and sum | drop with autoImplicit false | unknown β; no point-local proposition or structure weakening applies |
| P : MvPolynomial σ R | value | input on both sides | drop with autoImplicit false | unknown P; changing to a map equality is API restatement, not hypothesis weakening |

These intentionally rejected isolated elaboration probes did not alter live source.
Native run_code reported expected errors (its recovery terms are not accepted proofs).
No proposition, decidability, strict bound, or analysis hypothesis occurs.
Inversion check: the abstract content is substitution composition already supplied by
comp_aeval_apply; use that API rather than create a new abstract theorem.
Big-change candidates: none needed for this declaration.

## Literature search

Query `polynomial translation composition additive semiring generalization` top hits:
1. [Translation theory for semirings](https://repository.tcu.edu/entities/publication/0d9cae79-a3e7-4c52-b1e4-e4a578416175)
2. [Translations in semirings and semiring of translations](https://www.researchgate.net/publication/341934123_Translations_in_semirings_and_semiring_of_translations)
3. [YAP polynomial implementation](https://hackage-content.haskell.org/package/yap-examples-0.1/docs/src/Data.YAP.Polynomial.html)
The first two concern multiplicative translations of semirings, a different use of the word;
they do not justify weakening this theorem.

Refined query `site.wikipedia.org shift operator polynomial translation composition`:
[Shift operator](https://en.wikipedia.org/wiki/Shift_operator),
[Composition operator](https://en.wikipedia.org/wiki/Composition_operator),
[Pincherle derivative](https://en.wikipedia.org/wiki/Pincherle_derivative).
The usual translation operator is substitution x ↦ x+a. The composition law follows by
associativity; no characteristic, finiteness, or inverse assumptions are needed here.
Query `site.stacks.math.columbia.edu polynomial ring universal property` returned
[Conormal modules](https://stacks.math.columbia.edu/tag/04EA),
[Commutative Algebra](https://stacks.math.columbia.edu/download/algebra.pdf), and
[Lifting](https://stacks.math.columbia.edu/tag/07LW); no useful stricter generalisation found.
ChatGPT math MCP: n/a, no such tool exposed in ALL_TOOLS.
Literature-driven big changes: none.

## Signature width

Native #check at format.width 100:
```lean
@MvPolynomial.taylor_taylor : ∀ {σ : Type u_3} {R : Type u_4} [inst : CommSemiring R] (α β : σ → R)
  (P : MvPolynomial σ R),
  (MvPolynomial.taylor α) ((MvPolynomial.taylor β) P) = (MvPolynomial.taylor fun j ↦ α j + β j) P
```

| Signature line | Codepoints | Next complete signature token | Arithmetic | Action |
|---|---:|---|---|---|
| 140 | 60 | conclusion and := by, 58 codepoints without indentation | 60 + 1 + 58 = 119 > 100 | ok |
| 141 | 62 | no next signature line | n/a | ok |

## Inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| — | full signature | no ≥ or > comparison | n/a | no _ge_ or _gt_ in name |

## All 42 golfing rules

1.1 n/a: no by-exact wrapper.
1.2 n/a: no by-rfl.
1.3 n/a: no rw/exact pair.
1.4 n/a: no simp/exact pair.
1.5 n/a: no trailing rfl.
1.6 n/a: no constructor.
1.7 n/a: no apply/exact pair.
1.8 n/a: no contradiction block.
1.9 n/a: sum lambda cannot eta-reduce; ordinary lambda glyph corrected.
1.10 n/a: no have.
1.11 n/a: no apply/intro.
1.12 n/a: no show.
1.13 n/a: no projected conjunction.
1.14 n/a: no consecutive rewrites.
1.15 n/a: no terminal simp only.
1.16 n/a: no nonterminal simp.
1.17 n/a: selected simp theorem is a constant, no receiver expression.
1.18 n/a: no trailing term parentheses.
1.19 n/a: no push_neg.
1.20 n/a: not an existential helper.
2.1 tried grind; failed as recorded.
2.2 n/a: no existing grind prefix.
2.3 applied direct simp composition, eliminates the induction rather than consolidating a closing exact.
2.4 n/a: no analytic function property.
2.5 n/a: no positivity goal.
2.6 n/a: no inequality or monotonicity goal.
2.7 n/a: no Nat/Int arithmetic.
2.8 tried aesop; failed as recorded.
2.9 n/a: no numeric or cast goal.
2.10 n/a: arbitrary polynomial equality is not finite computation.
2.11 n/a: no denominators.
2.12 n/a: no ring-ending proof or algebraic hypotheses to combine.
2.13 n/a: no symmetric case branches.
2.14 n/a: no calc.
2.15 original <;> already closed induction cases; direct proof removes case splitting.
3.1 n/a: no erw.
3.2 n/a: no continuity/measurability.
3.3 n/a: no omega.
3.4 n/a: no rcases.
3.5 considered composition simp attribute; no automation attribute changes needed for this requested proof cleanup.
3.6 original simp_all already unsqueezed; direct proof uses simp.
3.7 n/a: no heartbeat options.

## Step-back reflection

A single simp invocation is both shorter in characters and closer to the mathematical
composition argument. The generic homomorphism composition theorem is the abstraction;
a new helper or term-mode extensionality chain would add plumbing. No have blocks or
redundant tactics remain. exact?/apply? attempts did not establish absence of alternatives.

## Gates

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | /Users/ramin/.elan/bin/lake build Roth.Taylor exited 0, 1439 jobs, target 17s |
| definition_protected | pass | diff has no definitions or abbreviations |
| theorem_statement_protected | pass | keyword/binders unchanged; only => to ↦ parser-equivalent lambda spelling |
| structure_gate | pass | one-line body, no conjunction, no branches |
| naming_gate | pass | descriptive composition name, no forbidden pattern |
| line_packing_gate | pass | both signature lines measured above |
| inequality_orientation_gate | pass | zero reversed comparisons |
| native complete LSP | pass | success=true, partial=false, timed_out=false, failed_dependencies=[]; only preserved header warning |

Original-type isolated proof gate: PASS. `/Users/ramin/.elan/bin/lake env lean
/private/tmp/taylor-decl11-isolated.lean` exited 0. The scratch file contains the exact
pre-target prefix (imports Roth.Box and Roth.HasseDeriv, never Roth.Taylor), followed by
the original theorem type, renamed isolated_taylor_taylor and using the new proof.
It therefore excludes the target theorem and every subsequent declaration.
`#print axioms isolated_taylor_taylor` reports only `[propext, Classical.choice, Quot.sound]`.
No sorry or native_decide was introduced. Final frozen file SHA256:
`c3b13e052d8ffa6af70404bf29d2853cce67a99b36cd0dc4a8584f5bfbf23020`.
Overall worker gates: pass.

## Result and phase checklist

Before 3 declaration lines; after 3; saved 0 lines. Removed induction and simplified proof.
Two issues found and fixed; no deferred refactoring. Renames queued: none.
Comments preserved: existing docstring 1/1, no inline comments present.

- [x] Step 1: references read.
- [x] Step 2: full 24-item audit.
- [x] Step 2.5: all five search methods.
- [x] Step 2.6: parameter/generalisation and public literature audit.
- [x] Step 2.7: per-line codepoint table.
- [x] Step 2.8: inequality scan table.
- [x] Step 3: all 42 rules.
- [x] Step 4: alternate strategy reflection and actual tests.
- [x] Step 5a: complete native diagnostics.
- [x] Step 5b: diff gates and module build.
- [x] Step 6a: no renames required.

Parent owns full project build, separate Roth.LeanEval verification, shared logs, and publication.
