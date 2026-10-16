# Phase 4 — Roth.coeff_kronecker

Scope: only this declaration in `Roth/GenWronskian.lean` and this report. Public signature,
definitions, docstring and source reference protected. Original declaration 14 lines,
final 13 lines, saved 1. No new helper, import, option, axiom, rename or dependency.
The proof now uses the absent-index obligation of `Finset.sum_eq_single` instead of a
separate support-membership case split. Its exponent bound is consequently inlined.

## References

Read both installed SKILL.md files, the complete worker contract, the initial file audit,
and golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md,
cleanup-gates.md, style-rules.md and naming-conventions.md. Explicit preservation and
scope instructions override generic API/docstring refactoring suggestions.

## Full 24-item audit

1. LINT: no target warning; five pre-existing outside warnings retained for owner handling.
2. HAVE SCAN: original `hlt`, no `by`, used twice: initially keep. Unified sum argument
   reduces this to one use; inline its degree bound. Final no `have`.
3. SET_OPTION: none.
4. SIMP SQUEEZE: original nonterminal `simp_rw` has explicit rewrite list; retain.
   New `simp` calls close their goals and remain unsqueezed.
5. NAMING: coefficient/substitution name describes result; no forbidden pattern or abbreviation.
6. LINE PACKING: all signature lines measured below; no repacking necessary.
7. BY PLACEMENT: `by` ends final signature line.
8. FORMAT: 2-space proof indent, no internal blank lines, one tactic per line. Ordinary
   lambda arrows normalized by rewriting affected proof; `conv_lhs =>` is tactic syntax.
9. COMMENTS: no inline comments; existing full docstring and source quotation unchanged.
10. DOCSTRING: public coefficient preservation, bounds and source already documented; preserved.
11. VISIBILITY: public API preserved; current local use does not authorize API removal.
12. STRUCTURE: final body 11 lines, branches at most 3; no conjunction in signature.
13. MATHLIB: five-method evidence below; generic sum/coeff APIs reused directly.
14. JUNK DEF: n/a, theorem.
15. EXISTS LEMMA: n/a, equality theorem.
16. SHOW vs CHANGE: none.
17. PUSH_NEG: none.
18. GENERALISE: every parameter considered below. No current need for API change.
19. INEQUALITY: all signature inequalities already `<`; scan below.
20. NORMAL-FORM: coefficient equality is canonical; no redundant equivalence graph.
21. SYNTAX-GEN: OK, implicit polynomial/exponent with explicit bounds supports application.
22. IMPORT-FANOUT: n/a, no new import.
23. CASTS: 0 dropped / 0 cross-type / 0 load-bearing in diff.
24. INSTANCE-NAME: n/a, no instance declaration.

Issues found: ordinary lambda syntax and duplicated support cases. Both fixed by unified
sum proof; no target lint or public warning proposal. Refactoring needed: none.

## Mathlib search-status

[A] Lean-Finder normal bounded call: “Kronecker substitution preserves polynomial coefficients
bounded exponents”; hits `Polynomial.coeff_contract`, `coeff_expand_mul`, `coeff_expand_mul'`.
These concern univariate expansion and do not replace the bounded multivariate theorem.
[B] Loogle `Polynomial.coeff, Finset.sum`: `Polynomial.finsetSum_coeff`, `sum_def`,
`sum_eq_of_subset`, `mul_eq_sum_sum`.
[C] LeanSearch “coefficient of polynomial after Kronecker substitution bounded individual
 degrees”: `MvPolynomial.aeval_natDegree_le`, PowerSeries substitution coefficient formulas,
`MvPolynomial.degreeOf_coeff_finSuccEquiv`; no replacement established.
[D] Source `rg`: coefficient/eval₂/aeval and `sum_eq_single`; direct hits include
`MvPolynomial/Coeff.lean` and `Basic.lean`; exact full-name `coeff_kronecker|kroneckerExp`
search across mathlib returns no textual match (untruncated).
[E] local-search `coeff` returns polynomial coefficient APIs and the project target;
index unavailable, so this is positive-name evidence only, never absence evidence.
Auxiliary variants: `sum_eq_single`, `sum_ite_eq`, `sum_ite_eq'`, `sum_ite_mem_eq`,
`coeff_expand_mul'`, `coeff_contract`, `sum_eq_of_subset`.
Common-equivalents table: no applicable discrete/finiteness/topological bucket.
Conclusion: partial generic matches, retain bounded local theorem and build directly on
`Polynomial.finsetSum_coeff` and `Finset.sum_eq_single`; no unconditional absence claim.
Compiled independent exact?/apply? probes recorded under verification.

## Generalisation status

| Parameter | Class | Use / candidates considered | Result |
|---|---|---|---|
| `{K : Type*}` | type variable | polynomial coefficient type, already universe polymorphic; drop would leave type unbound | retain |
| `[Field K]` | typeclass | `kronecker` has Field-based protected API; DivisionRing/CommRing/CommSemiring would require generalizing its definition first | no local API-compatible candidate |
| `{σ : Type*}` | type variable | exponent domain and polynomial variables; already universe polymorphic | retain |
| `[Fintype σ]` | typeclass | chosen equivalence/enumeration in kronecker and kroneckerExp; drop/Finite requires definition restatement | retain |
| `{k : ℕ}` | value | substitution base and all bounds, drop unbinds signature; abstract order does not support base encoding | retain |
| `hk : 1 < k` | proposition | injectivity of positional encoding; drop or `1 ≤ k` does not supply injectivity argument | retain |
| `{P : MvPolynomial σ K}` | value | both sides and hP depend on P; drop unbinds signature | retain |
| `hP : ∀ j, degreeOf j P < k` | proposition | each supported exponent bounded; drop/≤ does not establish strict bound; support-local statement changes public API | retain |
| `{d : σ →₀ ℕ}` | value | queried coefficient and hd depend on d; drop unbinds signature | retain |
| `hd : ∀ j, d j < k` | proposition | injectivity at queried exponent; drop/≤ fails same injection premise; no point-local subset suffices | retain |

Optional weakening work is closed under the preserved API, per worker authorization;
none applied or claimed verified as a stronger public theorem. Inversion check:
Kronecker-specific monomial rewrite and exponent-injectivity remain substantive; generic
support sum is already supplied by mathlib. No missing abstract helper required.
Big-change candidates: none pursued; no current need.

## Literature search

Query: “Kronecker substitution coefficients multivariate polynomial generalization”.
Top three search hits captured:
1. [Computing Characteristic Polynomials of Matrices](https://www.cecm.sfu.ca/~mmonagan/papers/MarshCASC2016.pdf)
2. [Kronecker Substitution](https://www.cecm.sfu.ca/~monaganm/papers/MarshCASC2016.pdf)
3. [Kronecker substitution overview](https://en.wikipedia.org/wiki/Kronecker_substitution)
Additional primary source: [Lecerf seminar appendix](https://algo.inria.fr/seminars/sem00-01/lecerf.html)
explicitly describes reading a multivariate coefficient at its positional univariate exponent.
Primary literature permits broader coefficient rings; implementing that here would first
change protected substitution definitions. No current need; no speculative API change.
Math ChatGPT MCP unavailable among tools; no external message sent.

## Line packing

`#check @coeff_kronecker` rendered at `format.width 100` in `/private/tmp/d08-proof.lean`:
```
@coeff_kronecker : ∀ {K : Type u_3} [inst : Field K] {σ : Type u_4} [inst_1 : Fintype σ] {k : ℕ},
  1 < k →
    ∀ {P : MvPolynomial σ K},
      (∀ (j : σ), degreeOf j P < k) →
        ∀ {d : σ →₀ ℕ}, (∀ (j : σ), d j < k) → ((kronecker k) P).coeff (kroneckerExp k d) = P.coeff d
```

| Signature line | Codepoints | Next atomic binder | Arithmetic | Action |
|---|---:|---|---|---|
| 80 | 96 | `{d : σ →₀ ℕ}` (12) | 96 + 1 + 12 = 109 > 100 | ok |
| 81 | 97 | no next signature line | n/a, proof follows | ok |

## Inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| – | complete signature and hypotheses | no ≥ or > in Lean code | none | none |

## Golfing rule pass — all 42

1.1 n/a: no by-exact wrapper.
1.2 n/a: no by-rfl wrapper.
1.3 n/a: no matching rewrite/exact pair after unifying sum obligations.
1.4 n/a: no simp/exact pair.
1.5 n/a: no trailing rfl.
1.6 n/a: no constructor.
1.7 n/a: no apply/exact pair.
1.8 n/a: no contradiction proof.
1.9 n/a: lambdas use their bound variables substantively.
1.10 applied: hlt becomes single-use after sum unification, then inlined.
1.11 n/a: no apply/intro pair.
1.12 n/a: no show.
1.13 n/a: no projection have.
1.14 n/a: no consecutive rw; simp_rw intervenes.
1.15 n/a: no terminal simp only.
1.16 n/a: simp_rw has explicit rules; new bare simp calls are terminal.
1.17 applied: Eq.symm function removed in favor of h.symm.
1.18 n/a: no needless outer application parentheses; necessary `hed (...)` preserved.
1.19 n/a: no push_neg.
1.20 n/a: no existential helper.
2.1 whole-proof grind attempted; see independent probe.
2.2 n/a: no existing grind.
2.3 applied: absent-index case closes with simp using coefficient-support API.
2.4 n/a: no function-property goal.
2.5 n/a: target is coefficient equality, no positivity subgoal.
2.6 n/a: no monotonicity subgoal; trans_lt composes exact needed bounds.
2.7 n/a: no arithmetic subgoal requiring a tactic.
2.8 whole-proof aesop attempted; see independent probe.
2.9 n/a: no numeric/cast computation.
2.10 n/a: generic polynomial equality not finite computation.
2.11 n/a: no denominator identity.
2.12 n/a: no ring/ring_nf ending.
2.13 n/a: support and nonsupport are not symmetric; unified generic API removes split.
2.14 n/a: no calc.
2.15 n/a: three sum obligations have different mathematical proofs.
3.1 n/a: no erw.
3.2 n/a: no continuity/measurability.
3.3 n/a: no omega.
3.4 n/a: no rcases.
3.5 n/a: no current automation registration need; public simp attributes protected.
3.6 n/a: no simp_all only.
3.7 n/a: no option override.

## Step back

A direct coefficient sum is appropriate: expand into monomials, use positional injectivity
to eliminate every other summand. `sum_eq_single` handles both support possibilities and
avoids duplicated injection reasoning. Term mode does not improve its dependent side
conditions. Whole-proof automation and exact?/apply? tested independently; no new helper.

## Verification and gates

- `/Users/ramin/.elan/bin/lake build Roth.GenWronskian`: exit 0, target built in 33s.
- Complete diagnostics `/private/tmp/d08-lsp.json`: success=true, partial=false,
  timed_out=false, failed_dependencies=[], zero errors, five complete warnings: missing
  copyright metadata; unused Fintype section parameter and Fintype-in-type on dependent
  zero theorem; DecidableEq-in-type on det_sum_rows; Fintype-in-type on existence theorem.
- Exact original signature compared byte-for-byte against the original baseline: equal.
- `/private/tmp/d08-original-api.lean`, lake env lean exit 0: original public type
  instantiated directly with current `coeff_kronecker`; axioms only
  `[propext, Classical.choice, Quot.sound]`. First pre-build missing-olean race was retried.
- `/private/tmp/d08-proof.lean`, lake env lean exit 0: independently reconstructed proof
  with no use of the target theorem; same three standard axioms, no sorryAx.
- Native multi_attempt stalled and was canceled; bounded direct multi_attempt timed out.
  Independent prefix-only automation probes are recorded separately below.
- Source SHA256 after module/LSP verification:
  `10694e44ecbeeafffa6e844498c585d636dbc8456c53ba2b6f2ac5b41a76ce66`.
  Owner revoked source ownership at this freeze; subsequent work is report/scratch only.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | module build exit 0 |
| definition_protected | pass | no definition edit |
| theorem_statement_protected | pass | original signature byte-identical |
| structure_gate | pass | 11 body lines, no conjunction, branches ≤3 |
| naming_gate | pass | descriptive name, no forbidden pattern |
| line_packing_gate | pass | complete 96/97-codepoint table above |
| inequality_orientation_gate | pass | zero ≥/> in signature |

Overall: pass. No renames queued, no helpers, no inline comments present, existing docstring
fully preserved. Audit issues found 2, fixed 2; refactoring deferred 0.

## Required phase checklist

- [x] Step 1 — reference docs read.
- [x] Step 2 — full 24-item audit printed.
- [x] Step 2.5 — five-method search status printed.
- [x] Step 2.6 — every-parameter generalisation status printed.
- [x] Step 2.7 — complete per-line width table printed.
- [x] Step 2.8 — inequality scan table printed.
- [x] Step 3 — all 42 golfing rules have statuses.
- [x] Step 4 — step-back reflection done.
- [x] Step 5a — complete LSP diagnostics clean of errors.
- [x] Step 5b — all diff gates pass.
- [x] Step 6a — rename queue n/a; no rename needed.


Automation probe detail: `apply?` suggests the generic
`Finsupp.apply_eq_of_mem_graph`, leaving its graph-membership premise; this is no
replacement theorem. Its suggestion interacts with `fail_if_success` and was isolated
from the final independent check. No source modification followed. The other whole-proof
probes use `fail_if_success solve | ...` so simplifier progress is not confused with
closing the goal.

Final independent prefix-only check `/private/tmp/d08-independent.lean`:
`lake env lean` exit 0 (session45952), target theorem absent from the input prefix.
Whole-proof `grind`, `simp [kronecker]`, `aesop` and `exact?` do not close the goal,
checked by `fail_if_success solve | ...`; the reconstructed final proof succeeds.
Axioms: `[propext, Classical.choice, Quot.sound]`, no sorryAx. Only its earlier copied
unrelated theorem emits the known unused-Fintype warning. All verification complete.
