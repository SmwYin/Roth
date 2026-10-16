# Phase 4 — derivative_kronHasse_aux (fresh extracted-helper audit)

Scope: only private helper in `Roth/GenWronskian.lean`, initially L145–153; final L145–152.
This is an additional helper audit, not another original-declaration completion. No tally increment.
Source frozen at SHA256 `3e6cfc0362faa15037b2a786465a581c24c8a1c282a3ef322c974e0553e44a2c`.
Parent revoked source ownership after module and complete LSP gates; remaining work is report-only.
Both skills, complete worker contract, initial GenWronskian audit, golfing-rules,
proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates, style-rules,
naming-conventions and mathlib-review-stages consulted.

## Full audit (24 items)

1. LINT: no warning in helper. Complete LSP reports five outside warnings, listed below.
2. HAVE SCAN: none; no hidden single-use intermediate facts.
3. SET_OPTION: none; no option introduced or raised.
4. SIMP SQUEEZE: initial nonterminal `simp only` already squeezed; replaced with terminal
   `simp` using associativity/commutativity, eliminating explicit sum congruence and ring.
5. NAMING: private `derivative_kronHasse_aux` names derivative of the existing kronHasse
   subject; `_aux` has no numeric suffix; no forbidden abbreviation/pattern. No rename.
6. LINE PACKING: all four signature lines measured below. No repack remains.
7. BY PLACEMENT: `:= by` remains at end of final signature line.
8. FORMAT: two-space proof indentation, no empty proof lines, one tactic per line,
   ordinary mathematical lambdas use ↦. Removed unnecessary exponent parentheses.
9. COMMENTS: no helper comments present; all surrounding docs/comments preserved.
10. DOCSTRING: n/a: private auxiliary, no docstring required or added.
11. VISIBILITY: private helper retained with `_aux`.
12. STRUCTURE: nine declaration lines become eight; four proof lines after `:= by`, no
    conjunction/case split/long branch. Retain meaningful operator identity supporting the
    caller's span-generator branch rather than re-inlining it and regressing structure.
13. MATHLIB: five actual searches and generic tactic probes below; no exact replacement
    established. Uses project chain rule and project multivariate Hasse formula.
14. JUNK DEF: n/a: theorem, not data definition.
15. EXISTS LEMMA: n/a: function equality, not existential witness packaging.
16. SHOW vs CHANGE: n/a: neither occurs.
17. PUSH_NEG: n/a: no negation-normalisation tactic.
18. GENERALISE: every actual parameter covered below; no safe local weakening.
19. INEQUALITY: zero ≥ or > occurrences in helper statement/hypotheses; table below.
20. NORMAL-FORM: function equality with a sum of scalar multiples is the caller's canonical
    module form; underlying pointwise chain rule is existing `derivative_aeval`.
21. SYNTAX-GEN: OK: `rw [derivative_kronHasse_aux]` rewrites exactly the function-valued
    generator needed by span induction. Pointwise restatement would add work to caller.
22. IMPORT-FANOUT: n/a: no new imports.
23. CASTS: zero casts changed in diff. Existing Fin→ℕ and ℕ→K coercions are genuine;
    inner `: ℕ` preserves natural addition before casting. Retained two cross-type
    conversions and one load-bearing natural-expression ascription. Parenthesized exponent
    removed; operator associativity still parses `X ^ (k ^ e)`.
24. INSTANCE-NAME: n/a: no instance declaration or local instance introduced.

Issues found: terminal simplification can remove explicit congruence/ring scaffolding;
redundant exponent parentheses. Both fixed. Refactoring needed: none.

## Mathlib search status (actual five methods)

| Method | Query/action | Result |
|---|---|---|
| A Lean-Finder | derivative multivariate polynomial evaluation Hasse derivative chain rule | Successful response: `Polynomial.derivative_eval₂_C`, `Polynomial.hasseDeriv_comp`, `Polynomial.hasseDeriv_mul`; univariate, not this identity |
| B Loogle | `Polynomial.derivative, MvPolynomial.aeval` | Complete response, zero items |
| C LeanSearch | derivative aeval multivariate Hasse derivative | Successful response: analytic `Polynomial.hasDerivWithinAt_aeval`, `Polynomial.hasDerivAt_aeval`, univariate `Polynomial.hasseDeriv` |
| D source grep | untruncated `derivative_aeval`, `derivative_kronHasse_aux`, `pderiv_hasseDeriv`, derivative/eval variants in relevant MvPolynomial/Polynomial and project source | Only project multivariate chain/Hasse declarations; univariate candidates checked in Derivative.lean:592 and HasseDeriv.lean:154 |
| E local name | `derivative_aeval` | Returned `Roth.derivative_aeval`; index unavailable, so no absence inference |

Search services were called normally and responded on this run. Native `lean_multi_attempt`
stalled and was canceled; bounded direct MCP fallback timed out after 65 seconds. Scratch
source clone excluding the target independently tested `grind`, `aesop`, `exact?` using
`fail_if_success (solve | ...)`; all failed to close, and the final simp proof compiled
(exit 0). Separate `apply?` attempt reported no relevant lemmas/running out of time at the
existing limit; no limit raised. Logs `/private/tmp/roth-helper-kronHasse-cascade.log` and
`/private/tmp/roth-helper-kronHasse-attempt.json`.

Six strict rules: no exact Mathlib duplicate found; no absence asserted from searches;
auxiliary/univariate variants checked; existing typeclasses used; no equivalent to delete;
no new direct Mathlib dependency requiring module-documentation edits. This extracted
project-specific operator identity combines existing project lemmas with function
extensionality, scalar evaluation and associativity; it is not a redundant wrapper around
one to three Mathlib calls. Common-equivalents table has no matching discrete/finiteness/
separation/bornology construction.

## Generalisation status

| Parameter | Class | Mechanical candidates | Evidence/result |
|---|---|---|---|
| `{K : Type*}` | type carrier | drop, universe widening | Carrier occurs in both polynomial types and coefficient conversion; already independent universe-polymorphic `Type*`; removing carrier requires another carrier, not weaker hypotheses |
| `[Field K]` | typeclass | drop; DivisionRing; CommRing; CommSemiring | Exact current statement invokes `Roth.kronecker` through private kronHasse, whose declared argument is `[Field K]`. Dropping/weaker parents cannot construct that argument; DivisionRing also lacks the commutative polynomial algebra. This is an API dependency, not evidence the mathematics requires division. Generalising upstream definitions is outside this helper-only scope |
| `{σ : Type*}` | type carrier | drop, universe widening | σ is the domain of d, Hasse variables, and sum index; already independent `Type*`; dropping changes the objects rather than a proposition hypothesis |
| `[Fintype σ]` | representation/data class | drop; Finite; point-localise | `Fintype.equivFin σ` explicitly occurs in exact statement and selects exponent enumeration; finite summation also uses Fintype. Finite alone cannot supply the same chosen equivalence without introducing a chosen Fintype value and restating the expression. No pointwise predicate/strict inequality to localise/weaken |
| `(k : ℕ)` | structure value | drop; abstract natural-number structure | k determines substitution `X ^ k ^ e`; cannot drop varying substitution. ℕ powers and finite enumeration are representation-essential; no order-only hypothesis here |
| `(d : σ →₀ ℕ)` | structure value | drop; abstract exponent structure | d determines Hasse operator and successor shift `d + single j 1`; no redundant predicate to weaken and abstracting it changes derivative data |

`l` from the surrounding section is absent from the elaborated helper type. No explicit
DecidableEq hypothesis; `classical` discharges internal finite-function decisions. No
proposition hypotheses, bundled conjunctions, strict inequalities or analytic/global
predicates exist, so strict→weak, unbundling and point-localisation catalogues are n/a.
Inversion check: the arbitrary substitution chain rule is already `derivative_aeval`;
this identity specializes it and applies `pderiv_hasseDeriv` to the concrete Hasse operator.
The meaningful specialization serves the caller's module form; no new generalized wrapper.
Literature search: n/a: private declaration, literature search not required. Big changes: none
proposed/applied; no public definitions or statements changed.

## Line packing

Reference: isolated `#check @initial_type_reproof` with `format.width 100` checks the exact
initial helper type, with all existing parameters and explicit coefficient conversion.
Widths are Unicode codepoints, including indentation. Next token means the next complete
syntactic expression/application, not a fragment of its identifier.

| Signature line | Chars | Next expression width | Arithmetic | Action |
|---|---:|---:|---|---|
| 145 | 61 | 58, full `(fun P ↦ Polynomial.derivative ...)` | 61 + 1 + 58 = 120 > 100 | ok |
| 146 | 64 | 77, sum binder and derivative factor through `*` | 64 + 1 + 77 = 142 > 100 | ok |
| 147 | 83 | 33, `Polynomial.C ((d j + 1 : ℕ) : K))` | 83 + 1 + 33 = 117 > 100 | ok |
| 148 | 86 | none; proof next | n/a | ok |

Initial third signature line was 85 codepoints; redundant parentheses removal gives 83.
Other lines unchanged. All four final lines ≤100; final conclusion and `:= by` packed.

## Inequality scan

| Region | Occurrences of ≥ / > | Action |
|---|---:|---|
| Entire helper signature and every hypothesis | 0 / 0 | none |
| Helper name `_ge_` / `_gt_` | 0 / 0 | no rename |

## Every golfing rule (42)

| Rule | Status |
|---|---|
| 1.1 by exact | n/a: no wrapper |
| 1.2 by rfl | n/a: no reflexivity proof |
| 1.3 rw + exact | n/a: no rewrite chain |
| 1.4 simp + exact | applied: terminal simp replaces simp plus closing sum-congruence expression |
| 1.5 trailing rfl | n/a: none |
| 1.6 constructor triples | n/a: equality, no constructor |
| 1.7 apply + exact | n/a: none |
| 1.8 contradiction | n/a: no negative proposition |
| 1.9 eta reduction | n/a: lambda genuinely composes derivative with kronHasse |
| 1.10 single-use have | n/a: none |
| 1.11 apply + intro | n/a: none |
| 1.12 redundant show | n/a: none |
| 1.13 have projections | n/a: none |
| 1.14 merge rewrites | n/a: no rw |
| 1.15 terminal simp only | applied in consolidated terminal simp |
| 1.16 nonterminal bare simp | n/a: old nonterminal simp already only; final simp terminal |
| 1.17 dot notation | n/a: no named proof argument to dot |
| 1.18 <\| | n/a: no trailing proof-expression parentheses |
| 1.19 push Not | n/a: no push_neg |
| 1.20 trivial exists | n/a: not existential |
| 2.1 grind | tried on whole goal in source clone; did not close |
| 2.2 delete before grind | n/a: final proof contains no grind |
| 2.3 simpa consolidation | applied terminal simp consolidation; no external witness for simpa needed |
| 2.4 fun_prop | n/a: formal polynomial derivative, no analytic predicate |
| 2.5 positivity | n/a: no sign/nonzero goal |
| 2.6 gcongr | n/a: no inequality/monotonicity |
| 2.7 lia/omega | n/a: no Nat/Int arithmetic proposition |
| 2.8 aesop | tried on whole goal, failed to close |
| 2.9 norm_num/norm_cast | n/a: no concrete number equation or cast-equality subgoal |
| 2.10 decide | n/a: universal symbolic function equality, not finite computation |
| 2.11 field_simp; ring | n/a: no denominator; initial ring replaced with simp associativity |
| 2.12 linear_combination | n/a: no equality hypotheses in initial ring context |
| 2.13 wlog | n/a: no symmetric branches |
| 2.14 calc term | n/a: no calc |
| 2.15 <;> | n/a: no parallel goals |
| 3.1 erw | n/a: none |
| 3.2 fun_prop migration | n/a: no continuity/measurability tactics |
| 3.3 omega→lia | n/a: no arithmetic tactic |
| 3.4 rfl substitution | n/a: no rcases |
| 3.5 automation attributes | n/a: one private operator identity; caller directly rewrites |
| 3.6 simp_all | n/a: no local equality hypotheses or simp_all |
| 3.7 options | n/a: no maxHeartbeats/maxRecDepth override |

Step-back reflection: whole-goal automation cannot see through the specific generator;
function extensionality followed by terminal simplification states the mathematical route
clearly and eliminates ring normalization. No extra helper or API duplication introduced.

## Gates and verification

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | `/Users/ramin/.elan/bin/lake build Roth.GenWronskian`, session17564 exit0; `/private/tmp/roth-helper-kronHasse-build.log` |
| definition_protected | pass | no definition changes; isolated diff only target signature syntax/proof |
| theorem_statement_protected | pass | exact original type independently reproved; only redundant exponent parentheses removed |
| structure_gate | pass | four proof lines; no conjunction or branch |
| naming_gate | pass | descriptive private name, allowed `_aux`, no forbidden pattern |
| line_packing_gate | pass | four-row arithmetic table, no repack |
| inequality_orientation_gate | pass | zero reversed inequalities/name fragments |
| LSP | pass | complete success=true, partial=false, timed_out=false; failed_dependencies=[]; `/private/tmp/roth-helper-kronHasse-lsp.json` |

Full warning disclosure (outside helper): L1 missing authoritative header; L36 unused
Fintype section variable for dependent-zero theorem; L32 same theorem unused Fintype in
type; L221 det_sum_rows unused DecidableEq; L239 existence theorem unused Fintype. None
suppressed or edited. No helper warning, no error, no sorry or nonstandard axiom.

Independent artifacts: `/private/tmp/roth-helper-kronHasse-independent.lean` and `.log`
(import actual built module, resolve private generator through environment lookup,
reprove exact INITIAL helper type without invoking helper; inspect actual built axioms).
Proof-search source clone `/private/tmp/roth-helper-kronHasse-cascade.lean` excludes target
and therefore cannot prove absence by invoking the helper under audit.

Result: before 9 lines, after 8, saved 1. Two audit issues fixed. Rules applied 1.4,
1.15,2.3. No rename/refactoring/decomposition queue. Comments: none present in helper;
all existing surrounding comments/docs preserved. Original tally unchanged.

## Required phase checklist

- [x] Step 1 — reference docs read
- [x] Step 2 — all 24 audit items reported
- [x] Step 2.5 — five actual search statuses and six replacement rules reported
- [x] Step 2.6 — every parameter generalisation/dependency analysis; private literature exemption
- [x] Step 2.7 — every signature line measured at width 100
- [x] Step 2.8 — inequality scan table
- [x] Step 3 — all 42 golfing rules have concrete status/reason
- [x] Step 4 — step-back reflection
- [x] Step 5a — complete clean helper LSP, all five outside warnings disclosed
- [x] Step 5b — module and all diff gates pass
- [x] Step 6a — no rename needed, no sidecar mutation

### Final independent verification result

Fresh compiler invocation `/Users/ramin/.elan/bin/lake env lean
/private/tmp/roth-helper-kronHasse-independent.lean` session86502 exited 0. Earlier scratch
lookup/unfolding attempts failed and were corrected before this final gate; no failed
scratch result is counted as verification. Initial type is taken from the pre-edit helper,
including original exponent parentheses and nested natural coefficient cast. The proof
unfolds the imported private generator by definitional `change`, applies the independent
chain/Hasse lemmas, and never invokes the helper being audited.

Width-100 reference output:

```text
@initial_type_reproof : ∀ {K : Type u_3} [inst : Field K] {σ : Type u_4} [inst_1 : Fintype σ] (k : ℕ) (d : σ →₀ ℕ),
  (fun P => Polynomial.derivative (Roth.kronHasse✝ k d P)) =
    ∑ j,
      (Polynomial.derivative (Polynomial.X ^ k ^ ↑((Fintype.equivFin σ) j)) * Polynomial.C ↑(d j + 1)) •
        Roth.kronHasse✝ k (d + Finsupp.single j 1)
'Roth.initial_type_reproof' depends on axioms: [propext, Classical.choice, Quot.sound]
actual built name: _private.Roth.GenWronskian.0.Roth.derivative_kronHasse_aux
actual built axioms: [propext, Classical.choice, Quot.sound]
```

Helper-only captured change:

```diff
-      ∑ j, (Polynomial.derivative (Polynomial.X ^ (k ^ (Fintype.equivFin σ j : ℕ))) *
+      ∑ j, (Polynomial.derivative (Polynomial.X ^ k ^ (Fintype.equivFin σ j : ℕ)) *
-  simp only [kronHasse, kronecker, derivative_aeval, pderiv_hasseDeriv, map_smul,
-    Finset.sum_apply, Pi.smul_apply, smul_eq_mul, Polynomial.smul_eq_C_mul]
-  exact Finset.sum_congr rfl fun j _ ↦ by ring
+  simp [kronHasse, kronecker, derivative_aeval, pderiv_hasseDeriv, map_smul,
+    Polynomial.smul_eq_C_mul, mul_assoc, mul_comm, mul_left_comm]
```
