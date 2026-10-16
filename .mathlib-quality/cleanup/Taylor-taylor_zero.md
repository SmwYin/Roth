# Declaration audit: `MvPolynomial.taylor_zero`

Worker scope: only this declaration, live lines 146–147 of `Roth/Taylor.lean`.
Baseline source SHA: c3b13e052d8ffa6af70404bf29d2853cce67a99b36cd0dc4a8584f5bfbf23020.
Frozen source SHA: a2f43a6a92cc7e8cee595b4fdb1047638cc7f8a9d1d031e050f72a95f086a6af.
No source changes after freeze. Parent owns project build and separate Lean evaluation.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md. Also read both SKILL.md files,
style-rules.md, naming-conventions.md, mathlib-review-stages.md and the complete
`/private/tmp/roth-taylor-worker-contract.md` (including separately recovering clipped output).

## Mathematics and change

Translation by zero evaluates every variable at itself. Mathlib already proves that this
algebra evaluation fixes every polynomial. Replace polynomial induction with
`simp [taylor, aeval_X_left_apply]`. Replace the mathematical lambda arrow `=>` with `↦`.
The public name, original elaborated type, explicit argument, simp attribute and docstring
remain intact. No imports or other declarations changed.

```diff
-theorem taylor_zero (P : MvPolynomial σ R) : taylor (fun _ => (0 : R)) P = P := by
-  induction P using MvPolynomial.induction_on <;> simp_all
+theorem taylor_zero (P : MvPolynomial σ R) : taylor (fun _ ↦ (0 : R)) P = P := by
+  simp [taylor, aeval_X_left_apply]
```

## Full 24-item audit

1. **LINT:** no diagnostics in lines 146–147. Complete native diagnostics retain only the
   existing file-header warning at line 1, explicitly preserved by user instruction.
2. **HAVE SCAN:** no `have` declarations in either proof; no use-count candidates.
3. **SET_OPTION:** none in target; no limits added or raised.
4. **SIMP SQUEEZE:** original terminal `simp_all` closes induction branches. Final single
   `simp [taylor, aeval_X_left_apply]` is terminal; leave unsqueezed. No nonterminal simp.
5. **NAMING:** `taylor_zero` describes the operation at zero, snake_case, no prohibited
   abbreviations, numeric scheme prefixes, numeric auxiliary suffixes or single-letter name.
   No rename needed; no queue writes.
6. **LINE PACKING:** one signature line, measured 82 before and 81 after (Unicode codepoints).
   Full conclusion and `:= by` already share it; table below.
7. **BY PLACEMENT:** `by` ends the signature line.
8. **FORMAT:** proof has two-space indent and one tactic; no empty lines, chained rewrites,
   `haveI`, `letI`, trailing spaces or over-width lines. Mathematical arrow corrected.
9. **COMMENTS:** no inline proof comments; no comments removed. Existing docstring untouched.
10. **DOCSTRING:** existing sentence explains translation identity; appropriate depth for
    this elementary identity; preserved verbatim under the documentation contract.
11. **VISIBILITY:** retained public algebra API and simp theorem per explicit user direction.
    Generic wrapper/private advice does not override this direction.
12. **STRUCTURE:** one proof line before and after; no conjunction or long branch. Induction
    removed entirely; no extraction needed.
13. **MATHLIB:** all five searches actually run; identity-evaluation API found and compiled.
    Details below. No global decidability instance or coset workaround.
14. **JUNK DEF:** n/a: theorem, not definition.
15. **EXISTS LEMMA:** n/a: equality theorem, not existential helper.
16. **SHOW vs CHANGE:** n/a: neither present.
17. **PUSH_NEG:** n/a: no negation-pushing tactic.
18. **GENERALISE:** all four elaborated parameters considered below; semiring and drop-class
    probes rejected by elaboration. Universes already independent; no hypotheses to localize.
19. **INEQUALITY:** zero inequalities in signature, including inherited parameters; table below.
20. **NORMAL-FORM:** translation identity is oriented toward the unchanged polynomial on RHS;
    this is a terminating simp normal form. No competing equivalence form introduced.
21. **SYNTAX-GEN:** OK: explicit polynomial argument is useful for rewriting. A bundled
    endomorphism identity is derivable by extensionality; changing this API brings no necessary
    benefit and is not authorized.
22. **IMPORT-FANOUT:** n/a: no new imports.
23. **CASTS:** no casts or ascriptions introduced by the proof change: 0 dropped / 0 cross-type /
    0 new load-bearing ascriptions. The pre-existing `(0 : R)` is preserved as part of the
    original statement under the user signature-preservation instruction; it is not claimed
    necessary to inference. Binder `P : MvPolynomial σ R` specifies the theorem's input type.
24. **INSTANCE-NAME:** n/a: theorem defines no instance.

Issues found: indirect induction; mathematical lambda arrow. Both fixed.
Refactoring needed: none. Public wrapper preservation is explicit authorization, not a deferred
proposal to delete the theorem.

## Mathlib search-status

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | `multivariate polynomial evaluation at variables identity` | `MvPolynomial.eval₂_eta`, `aeval_X_left_apply`, `aeval_X_left` |
| B Loogle | `MvPolynomial.aeval, _ = _` | `aevalTower_id`, `aevalTower_ofId`, `Algebra.adjoin_range_eq_range_aeval`; nearby general evaluation API |
| C LeanSearch | `Evaluating multivariate polynomial at its variables equals itself` | `eval₂_eta`, `aeval_X_left_apply`, `aeval_ite_mem_eq_self` |
| D source grep | `aeval_X_left\|aeval_X\|eval₂_C_X`, then exact declarations | `Eval.lean:601` and `:604`, plus `eval₂_eta:222`, `aeval:569` |
| E local name pattern | `aeval_X` | source hits include both identity lemmas; index reported `unavailable`, so not used as evidence of absence |

Auxiliary variants searched: `_left`, `_left_apply`, `eval₂_eta`, evaluation-tower identity.
Common-equivalents table: no discrete/finite/separation/bornology bucket applies.
Conclusion: partial match through unfolding `taylor`; use existing identity evaluation directly
inside the preserved public theorem. No claim of library absence is made.
Six rules: exhaustive search performed; auxiliary variants examined; no custom predicates;
mathlib API used; public-wrapper deletion rules 1/5 superseded by explicit API preservation;
rule 6 satisfied by recording the exact dependency here without altering protected module prose.
`#check @aeval_X_left_apply` compiled in the prefix experiment.

## Generalisation status

| # | Parameter | Class | Used as | Mechanical candidates | Verified / result |
|---|---|---|---|---|---|
| 1 | `{σ : Type*}` | type-variable | variable index of `P`, `taylor`, `X` | drop would leave index unbound; universe relaxation already present | structurally indispensable index; no narrower universe constraint |
| 2 | `{R : Type*}` | type-variable | coefficient type and zero | drop would leave coefficient type unbound; universe relaxation already present | structurally indispensable coefficient type; independently universe-polymorphic |
| 3 | `[CommSemiring R]` | typeclass | elaboration of `MvPolynomial`, `taylor`, `aeval` | weaken to `Semiring R`; drop entirely | compiled exact-prefix probes both fail synthesis of `CommSemiring R`; dropping also fails `OfNat R 0` |
| 4 | `(P : MvPolynomial σ R)` | structure-value | polynomial on both sides | drop leaves both occurrences of `P` unbound; implicit conversion changes call signature | no assumption to weaken; preserve explicit input |

No propositional, decidability, topology, strict-order or bundled hypotheses. Thus point-localize,
strict→weak and unbundling catalogues are inapplicable. The class is already subtraction-free;
ring/field weakening catalogue starts above its present strength.

Actual class probes: `/private/tmp/taylor12-weaken.lean`, compiled with
`/Users/ramin/.elan/bin/lake env lean /private/tmp/taylor12-weaken.lean`, exit 1. This file
uses the exact pre-target source prefix, closes its section, and opens fresh sections with
respectively `[Semiring R]` and no algebra instance. Errors at 148 and 153 demand
`CommSemiring R`; no failed probe was installed in the live source.

Inversion check: the named operation `taylor` unfolds once, then the theorem is the generic
identity-evaluation law already in mathlib. No new abstract helper is needed. Big-change
candidates: none; a noncommutative substitution construction would change the underlying API.
No successful weakening held back.

## Literature search status

A. WebSearch query `polynomial substitution identity zero translation universal property
commutative semiring generalization` returned these first three hits:

1. [Keith Conrad, Universal Identities](https://kconrad.math.uconn.edu/blurbs/linmultialg/univid.pdf).
2. [Linear independence over tropical semirings and beyond](https://www.researchgate.net/publication/23671028_Linear_independence_over_tropical_semirings_and_beyond).
3. [Universal Identities mirror](https://citeseerx.ist.psu.edu/document?doi=178d561c5c712b2eb910263da9ca176461f6f13f&repid=rep1&type=pdf).

Targeted queries `site.stacks.math.columbia.edu polynomial ring universal property` and
`site.ncatlab.org polynomial semiring universal property` produced, among the first displayed
hits, [nLab universal construction](https://ncatlab.org/nlab/show/universal+construction),
[Stacks 04EA](https://stacks.math.columbia.edu/tag/04EA), and
[nLab polynomial](https://ncatlab.org/nlab/show/polynomial). The polynomial entry characterizes
polynomial algebras as free commutative algebras on the variable set. Inference: the identity
map on generators extends to the identity endomorphism, exactly the abstraction used here.
The existing semiring theorem requires no field, characteristic or finite-variable assumption.
No literature-driven signature change is indicated. Search snippets do not establish a
maximality theorem for all possible noncommutative constructions.

B. ChatGPT mathematical MCP: n/a; discovery of `ALL_TOOLS` found no math ChatGPT endpoint.

## Line packing

Compiled reference, `set_option format.width 100 in #check @test_taylor_zero` in the exact prefix:

```lean
@test_taylor_zero : ∀ {σ : Type u_3} {R : Type u_4} [inst : CommSemiring R] (P : MvPolynomial σ R),
  (taylor fun x => 0) P = P
```

| Signature line | Before chars | After chars | Next signature token | Arithmetic | Action |
|---|---:|---:|---|---|---|
| 146 | 82 | 81 | none; proof body follows | n/a: complete signature fits 81 ≤ 100 | ok |

The codepoint measurement was computed from the live source using Python `len`; no byte counts.
No repacking row needed. The proof body cannot join: 81 + 1 + 33 = 115 > 100
(`simp [taylor, aeval_X_left_apply]` is 33 characters).

## Inequality scan

| Occurrence | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| none | entire signature and inherited parameters | no `≥`, `>`, `≤`, `<` relation | n/a | no `_ge_` or `_gt_` name |

Final signature has zero reversed inequalities. Original ASCII lambda arrow was syntax, not an
inequality; it was replaced with `↦` independently.

## Golfing-rule pass (42 rules)

| Rule | Status |
|---|---|
| 1.1 by exact | n/a: no exact wrapper |
| 1.2 by rfl | n/a: no reflexivity proof |
| 1.3 rw + exact | n/a: no rewrites followed by exact |
| 1.4 simp + exact | n/a: no closing exact chain |
| 1.5 trailing rfl | n/a: none |
| 1.6 constructor | n/a: equality, no constructor proof |
| 1.7 apply + exact | n/a: none |
| 1.8 by_contra | n/a: no contradiction argument |
| 1.9 eta-reduction | n/a: constant-zero lambda is not eta-reducible; arrow standardized |
| 1.10 single-use have | n/a: no haves |
| 1.11 apply + intro | n/a: none |
| 1.12 redundant show | n/a: none |
| 1.13 have projections | n/a: none |
| 1.14 merge rw | n/a: none |
| 1.15 unsqueeze terminal simp only | n/a: no squeezed terminal simp |
| 1.16 squeeze nonterminal simp | n/a: final simp is terminal |
| 1.17 dot notation | n/a: no receiver-based lemma application |
| 1.18 `<\|` | n/a: no parenthesized term-proof application |
| 1.19 push Not | n/a: no push_neg |
| 1.20 existential helper | n/a: no existential helper |
| 2.1 grind | tried native `grind [taylor, aeval_X_left_apply]`; failed to close negated identity |
| 2.2 pre-grind deletion | n/a: no retained grind |
| 2.3 simpa consolidation | identity simplification replaces induction; no simp/exact chain requiring simpa |
| 2.4 fun_prop | n/a: algebraic equality, no function regularity property |
| 2.5 positivity | n/a: no order/positivity goal |
| 2.6 gcongr | n/a: no monotone inequality |
| 2.7 lia/omega | n/a: arbitrary polynomial equality, no integer arithmetic goal |
| 2.8 aesop | tried natively, failed with no progress |
| 2.9 norm_num/norm_cast | n/a: symbolic substitution, no numeric calculation or cast goal |
| 2.10 decide | n/a: arbitrary coefficient semiring has no computational equality decision |
| 2.11 field_simp/ring | n/a: no denominator, no field instance; evaluation rather than ring normalization |
| 2.12 linear_combination | n/a: no ring-ending proof or algebraic hypotheses |
| 2.13 wlog | n/a: no symmetric branches |
| 2.14 collapse calc | n/a: no calc |
| 2.15 `<;>` | removed need for branching altogether; no remaining multiple goals |
| 3.1 erw | n/a: none |
| 3.2 continuity/measurability | n/a: neither tactic nor regularity goal |
| 3.3 omega to lia | n/a: no omega |
| 3.4 rcases rfl | n/a: no rcases |
| 3.5 automation attributes | existing `[simp]` retained; identity is appropriate normal form |
| 3.6 simp_all | original already unsqueezed; superseded by direct identity simp |
| 3.7 limits | n/a: no limits present or added |

## Step back and think / experiments

The original induction is mathematically unnecessary: evaluate at `X` directly. The one-tactic
proof is better than extracting a helper or composing a longer explicit term.

* Prefix-only `simp [taylor]` failed, leaving `(aeval fun j => X j) P = P`.
* Prefix-only `simp [taylor, aeval_X_left_apply]` passed with the exact original type.
* Native multi-attempt at live proof line 147 tested the final simp, grind, aesop, exact?, apply?.
  Simp had no diagnostics; grind and aesop failed; exact? and apply? hit the default 200000
  heartbeat limit. No limit was raised. An earlier attempt mistakenly addressed declaration
  line 146 and returned syntax errors; it was discarded and rerun at proof line 147.
* No haves, redundant intermediate goals or candidate composed terms remain.

## Verification and gates

Actual module invocation `/Users/ramin/.elan/bin/lake build Roth.Taylor` exited 0;
`Built Roth.Taylor (10s)`, `Build completed successfully (1439 jobs)`.
Warnings are the existing header warnings in Box, HasseDeriv and Taylor.

Native `lean_diagnostic_messages` on `Roth/Taylor.lean` after the edit returned
`success=true`, `partial=false`, `timed_out=false`, no failed dependencies. The sole item
was the preserved line-1 header warning. No errors, sorries or target warnings.

Isolation: `/private/tmp/taylor12-isolated.lean` contains the exact file prefix ending before
the target docstring, then `test_taylor_zero` with the original type and candidate proof,
then `#check`/axiom commands and closing sections. It imports only the original Box and
HasseDeriv dependencies, never Roth.Taylor, and contains no `taylor_zero` declaration.
`/Users/ramin/.elan/bin/lake env lean /private/tmp/taylor12-isolated.lean` exited 0.
`#print axioms test_taylor_zero`: `[propext, Classical.choice, Quot.sound]`.
The temporary failed experiment before repair reported `sorryAx`; this is not the accepted
artifact, whose successful rerun above has only the three standard axioms.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | actual module build exit 0 |
| definition_protected | pass | no definition edits |
| theorem_statement_protected | pass | exact original-type isolated proof; only equivalent lambda notation changed |
| structure_gate | pass | one proof line; no conjunction or branches |
| naming_gate | pass | descriptive snake_case, no forbidden pattern |
| line_packing_gate | pass | full one-row signature table, 81 chars |
| inequality_orientation_gate | pass | full zero-occurrence table |
| LSP complete | pass | success true, partial false |
| isolated proof / standard axioms | pass | prefix CLI exit 0, three standard axioms |

Overall: pass. Freeze SHA stated above; full project and separate LeanEval are parent-owned.

## Result and complete phase checklist

Before: 2 declaration lines. After: 2. Saved: 0 lines; induction replaced by direct evaluation.
Audit issues found: 2; fixed: 2. Refactoring deferred: 0. Renames queued: none.
Comments preserved: docstring intact, no proof comments present. Rules applied: direct
identity simplification (2.3 strategy), removal of branching (2.15), mathematical arrow style.

- [x] Step 1 — references read.
- [x] Step 2 — all 24 audit items printed.
- [x] Step 2.5 — all five search methods and six-rule review printed.
- [x] Step 2.6 — every parameter, class probes, inversion and literature covered.
- [x] Step 2.7 — measured per-line width table printed.
- [x] Step 2.8 — inequality scan table printed.
- [x] Step 3 — every one of 42 golfing rules assigned a concrete status.
- [x] Step 4 — strategy reflection and actual tactic experiments recorded.
- [x] Step 5a — native complete diagnostics verified.
- [x] Step 5b — diff gates, module build, isolation and axioms recorded.
- [x] Step 6a — no renames required; shared queue untouched.
