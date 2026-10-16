# Fresh audit: `MvPolynomial.eq_sum_box_hasseDeriv`

Target: `Roth/Taylor.lean:192–208`, original requested lines 210–227. Dedicated scope only.
Baseline supplied: branch `ramin-cleanup`, checkpoint `32473ad`, source SHA256
`0a6ab3437c5950f4d2e800b78f03e7a53b7ce97f6cc248c3bff71fcf00a46f22`.
Worker-start snapshot: `/private/tmp/decl19-before.lean`.
Frozen source SHA256: `eda896cd346e776d923237cdc4235045d1dd2e4fe32a8d039f561ca6068221a6`.
Parent explicitly revoked source ownership after this freeze; remaining work is report-only.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md. Also read both skill files, the full
worker contract, naming-conventions, relevant style-rules sections and review-stage guidance.
User/parent preservation instructions govern public signatures, definitions, documentation,
header warning, and public-wrapper retention.

## Full 24-item audit

1. **LINT:** native complete whole-file diagnostics: no errors, no target warnings; only the
   existing line-1 `Copyright too short!` warning. Preserved as instructed.
2. **HAVE SCAN:** L195 `have h1 : ... := by`: genuine proof content, used once at L205;
   keep. No other `have`. The `obtain` at L200 carries a nontrivial membership-negation proof.
3. **SET_OPTION:** none in target; none introduced.
4. **SIMP SQUEEZE:** L197 nonterminal `simp only` is appropriate; `simp? only` returned
   exactly `[coeff_taylor, coeff_sum, coeff_monomial, Finset.sum_ite_eq']`. L201 terminal
   `simpa [Roth.mem_box] using he` and L208 terminal `simp [sub_eq_add_neg]` remain unsqueezed.
5. **NAMING:** `eq_sum_box_hasseDeriv` describes the equality and uses the existing API
   identifier `hasseDeriv`; no forbidden abbreviation, numbered pattern, or single-letter name.
6. **LINE PACKING:** complete measured signature table below; all justified breaks.
7. **BY PLACEMENT:** every `by` ends its preceding line.
8. **FORMAT:** two-space tactic indentation, four-space signature continuation, no internal
   blank line, no `haveI`/`letI`; changed three ordinary lambda arrows to `↦`.
9. **COMMENTS:** no inline proof comments present; existing docstring preserved byte-for-byte.
10. **DOCSTRING:** existing two-line source-bearing public docstring retained; describes the
    polynomial form and degree-bound use, distinguishing evaluated form immediately below.
11. **VISIBILITY:** public headline result, explicitly listed in module main results; retained.
12. **STRUCTURE:** before 16 lines including `:= by`, after 15 (14 tactic-body lines).
    No conjunction, no branch over 10 lines. Consolidating h1's coefficient rewrites avoids
    unnecessary extraction; no new helper or follow-up helper audit needed.
13. **MATHLIB:** five-method evidence below; partial matches, not a direct box formula.
14. **JUNK DEF:** n/a: theorem, no definition changed.
15. **EXISTS LEMMA:** n/a: no private existential lemma; local obtain proves a needed witness.
16. **SHOW vs CHANGE:** n/a: no `show` or `change`.
17. **PUSH_NEG:** n/a: none.
18. **GENERALISE:** every parameter covered below; negative probes only, API unchanged.
19. **INEQUALITY:** zero reversed inequalities in signature; required table below.
20. **NORMAL-FORM:** already expansion equality with polynomial on left and finite sum on
    right; subtraction form matches the intended centered-monomial formula.
21. **SYNTAX-GEN:** OK: explicit coordinatewise bound supports direct application; no new
    bundled assumption or restatement demonstrably improves call sites.
22. **IMPORT-FANOUT:** n/a: no imports added.
23. **CASTS:** 0 dropped / 0 cross-type / 0 load-bearing in diff; diff has no casts/ascriptions.
24. **INSTANCE-NAME:** n/a: no instance declaration or local instance introduced.

Issues found: (1) headline body exceeded 15-line threshold; (2) three ASCII lambda arrows.
Both fixed. Refactoring needed: none.

## Mathlib search-status

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | `multivariate polynomial Taylor expansion Hasse derivatives` | `Polynomial.taylor_coeff`, `Polynomial.hasseDeriv_apply`, `Polynomial.hasseDeriv_comp`: univariate partial matches |
| B Loogle | `MvPolynomial.monomial, Finset.sum` | `MvPolynomial.as_sum`, `support_sum_monomial_coeff`, `monomial_sum_prod`, `monomial_sum_one` |
| C LeanSearch | `A multivariate polynomial equals sum of monomials with its coefficients over finite set containing support` | `MvPolynomial.as_sum`; univariate `Polynomial.sum_eq_of_subset`, `as_sum_support`, `sum_monomial_eq` |
| D source | `sum.*monomial`, `as_sum`, `support.*subset` in MvPolynomial Basic/CommRing/Degrees; `eq_sum_box_hasseDeriv`, `taylor.*sum`, `sum.*taylor` | Basic:963/967 support expansion; no exact target-name or multivariate Taylor-sum hit; full exact-name search across Mathlib also empty |
| E local name | `sum_monomial` | MvPolynomial/Polynomial/SkewPolynomial sum-monomial facts; index `unavailable`, so this result is not evidence of absence |

Auxiliary variants: support-sum, monomial-sum, sum-of-subset, Taylor coefficient, Hasse
composition. Common-equivalents lookup: no matching discrete/finite/topological bucket.
Source and compiled `#check` verify chosen partial matches; exact-name grep was untruncated.

Conclusion: **found partial match `MvPolynomial.as_sum`**. Retain the public target and use
mathlib coefficient/sum/monomial/Finsupp-product APIs directly. `as_sum` still requires a
support-to-box enlargement and coefficient identification, so does not replace this proof
in 1–3 calls. No global absence claim is made: whole-goal `exact?` and `apply?` hit the
ordinary 200000-heartbeat bound. Whole-goal `grind`, `simp`, `aesop` failed to close the goal.
These were attempted in native `lean_multi_attempt` at L195 before the target was available
in its own context; the failed attempts also reported continuation parse errors because
replacing the `have` header leaves its original nested lines. The primary tactic failures
were explicit, independent of those continuation errors.

Six strict rules: no new wrapper; all five searches performed; auxiliary variants checked;
no custom predicate introduced; no direct equivalent found requiring replacement (public
retention is explicitly required); module documentation unchanged under preservation rule.
No API-extraction signals such as manual coercion/class plumbing or wrapper round trips.

## Generalisation status

Mechanical candidate file: `/private/tmp/decl19-candidates.lean`, output
`/private/tmp/decl19-candidates.log`, actual `lake env lean` exit 1 as expected for negative
probes. Each candidate contains the pre-target prefix and a renamed copy, excluding the
public target; `autoImplicit false` prevents dropped parameters being silently reintroduced.
The first attempt to ask native diagnostics about a `/private/tmp` scratch file was rejected
as outside a Lean project; CLI compilation supplied the negative-probe evidence instead.
Native whole-file diagnostics separately validate the retained source completely.

| Parameter | Class / use | Candidates actually tested or excluded | Evidence / result |
|---|---|---|---|
| `{σ : Type*}` | type variable; domain of α/r, monomial index | drop ruled out structurally by dependent binders; already universe-polymorphic | no narrower universe to weaken; removing σ leaves dependent types unbound |
| `{A : Type*}` | type variable; coefficients | drop ruled out structurally by dependent binders; already universe-polymorphic | no concrete coefficient type to abstract; removing A leaves α/P unbound |
| `[CommRing A]` | typeclass; polynomial ring and subtraction | drop; `[Ring A]`; `[CommSemiring A]` | fresh sections after closing original CommRing: drop/Ring fail `CommSemiring A` synthesis at 351/309; semiring fails subtraction elaboration at 331; none retained |
| `[Fintype σ]` | typeclass; box and finite product | drop; Finite requires choosing a different signature/representation | drop fails `Fintype σ` synthesis at 212; no point-localization candidate for a finite product over all σ |
| `[DecidableEq σ]` | decidability; box's signature | drop | fails `DecidableEq σ` synthesis at 231 before proof; adding `classical` inside proof cannot repair declaration elaboration |
| `(α : σ → A)` | structure value; evaluation and center | drop | unknown α at 250; no continuity/pointwise catalogue entry applies |
| `(r : σ → ℕ)` | structure value; bound and box | drop | unknown r at 268; ℕ is the polynomial exponent type, replacing it changes the object |
| `(P : MvPolynomial σ A)` | structure value; polynomial | drop | unknown P at 287; type already arbitrary in σ/A |
| `(hP : ∀ j, degreeOf j P ≤ r j)` | proposition; vanishing outside box | drop | unknown hP at 201; bound needed for derivative vanishing; already weak ≤, all coordinates used, no strict→weak or point-local variant |

These are tests of mechanical weakening, not claims of mathematical impossibility. No
candidate compiled, hence no public-API proposal or source modification was made.
Inversion diagnostic: no concrete witness hiding an abstract argument; Taylor/monomial
structure persists through the proof. Box membership is used precisely to enforce the
coordinatewise exponent bound. Arbitrary finite supersets would be a different expansion
API, not a missing mechanical generalisation of the advertised box theorem.
Big-change candidates: none recommended.

## Public literature search

Web query: `Hasse derivatives multivariate Taylor expansion commutative ring generalization`.
Three relevant results captured/opened:

1. [Bhargava et al., Fast Multivariate Multipoint Evaluation Over All Finite Fields, §3.2](https://zeyuguo.bitbucket.io/papers/MME.pdf): defines multivariate Hasse derivatives by coefficients of translation over an arbitrary commutative ring (Definition 3.4); supports present coefficient generality.
2. [Narváez Macarro, Hasse–Schmidt derivations versus classical derivations](https://arxiv.org/abs/1810.08075): survey over arbitrary commutative algebras, suggesting broader Hasse–Schmidt frameworks but no weakening of this centered finite-box formula.
3. [Hasse derivative, canonical-form cross-check](https://en.wikipedia.org/wiki/Hasse_derivative): consulted as requested canonical encyclopedic reference; primary mathematical justification above.

Findings are paraphrased, no long quotations. No characteristic-zero, field, or domain
assumption is needed, and none is present. Centered subtraction requires additive inverses.
Math ChatGPT MCP: n/a, no callable math-chat tool in `ALL_TOOLS`.
Literature-driven big-change candidates: none recommended.

## Line packing (codepoints, final table)

`#check @audit_original_type` in isolated original-type file at `format.width 100`:

```lean
@audit_original_type : ∀ {σ : Type u_3} {A : Type u_4} [inst : CommRing A]
  [inst_1 : Fintype σ] [inst_2 : DecidableEq σ] (α : σ → A) (r : σ → ℕ)
  (P : MvPolynomial σ A), (∀ (j : σ), degreeOf j P ≤ r j) →
  P = ∑ d ∈ Roth.box r, C ((eval α) ((hasseDeriv d) P)) * ∏ j, (X j - C (α j)) ^ d j
```

Reference display is reflowed here for readability; source widths measured directly by
Python `len`, counting Unicode codepoints, not bytes. No signature edit was necessary.

| Sig line | Chars | Next complete syntactic unit | Arithmetic | Action |
|---|---:|---|---|---|
| 192 | 81 | `(P : MvPolynomial σ A)` (22) | 81 + 1 + 22 = 104 > 100 | ok |
| 193 | 59 | complete conclusion with `:= by` (84) | 59 + 1 + 84 = 144 > 100 | ok |
| 194 | 88 | no next signature line | n/a | ok |

## Inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| — | complete signature/hypotheses | n/a: no `≥` or `>` | none | no `_ge_`/`_gt_` in name |

The hP inequality is already `degreeOf j P ≤ r j`. Local witness uses `r j < e j`.

## All 42 golfing rules

| Rule | Status / actual evidence |
|---|---|
| 1.1 by-exact | n/a: no wrapper |
| 1.2 by-rfl | n/a: no by-rfl proof |
| 1.3 rw+exact | n/a: no adjacent exact |
| 1.4 simp+exact | n/a: existing terminal simpa already consolidated |
| 1.5 simp+rfl | n/a: no trailing rfl after simp |
| 1.6 constructors | n/a: no conjunction constructor |
| 1.7 apply+exact | n/a: no apply |
| 1.8 by_contra | n/a: no negation proof |
| 1.9 eta | n/a: negative-center lambda is not eta reducible; product proof's anonymous argument is required |
| 1.10 have inline | h1 has proof content, retained |
| 1.11 apply+intro | n/a: already refine + lambda at sum_congr |
| 1.12 redundant show | n/a: no show |
| 1.13 have projections | n/a: none |
| 1.14 merge rewrites | applied related consolidation: coefficient rw then simp only became one simp only at L197 |
| 1.15 terminal simp only | n/a: only simp only is nonterminal |
| 1.16 squeeze | native simp? only reproduces exact L197 list; terminal simp/simpa unsqueezed |
| 1.17 dot notation | existing `(hP j).trans_lt hj` and `.symm` already use it |
| 1.18 parens | n/a: remaining parentheses delimit necessary applications/ascriptions |
| 1.19 push Not | n/a: no push_neg |
| 1.20 existential helper | n/a: no private existential helper |
| 2.1 grind | actual native whole-goal and coefficient-goal attempts fail |
| 2.2 tactics before grind | n/a: retained proof has no grind |
| 2.3 simpa | existing terminal witness simpa is the direct negated-box equivalence; no following exact to consolidate |
| 2.4 fun_prop | n/a: no analytic function-property goal |
| 2.5 positivity | n/a: no positivity goal |
| 2.6 gcongr | n/a: no inequality congruence goal; trans_lt is one direct order application |
| 2.7 lia/omega | n/a: no free-standing arithmetic subgoal; witness is box-membership logic, bound is direct trans_lt |
| 2.8 aesop | native whole-goal and coefficient-goal attempts fail |
| 2.9 numeric/casts | n/a: no numeric computation/cast goal |
| 2.10 decide | n/a: polymorphic symbolic polynomial identity, not closed finite computation |
| 2.11 field_simp/ring | n/a: no denominators, no final ring chain |
| 2.12 linear_combination | n/a: no ring/ring_nf ending or linear-combination hypotheses |
| 2.13 wlog | n/a: membership true/false branches are mathematically different |
| 2.14 collapse calc | two steps remain; second contains sum congruence proof, term composition would obscure it without savings |
| 2.15 multiple goals | n/a: sum_congr has one unresolved summand goal |
| 3.1 erw | n/a: no erw |
| 3.2 legacy function tactics | n/a: none |
| 3.3 omega to lia | n/a: no arithmetic tactic |
| 3.4 rcases rfl | n/a: no equality substitution |
| 3.5 automation attributes | n/a: no new API fact and target is an expansive conditional rewrite, not a simplifier normal form |
| 3.6 simp_all | n/a: no simp_all only |
| 3.7 limits | n/a: no options or limit raises |

## Step-back reflection

The proof naturally has two stages: identify the coefficients of the translated polynomial
on the box, then translate back. Native whole-goal automation did not close it; exact/apply
search timed out at default limits. Support-based `as_sum` is an alternative but requires
extra support-enlargement work. Keeping h1 avoids nesting a substantial coefficient proof
inside a rewrite. Consolidating its initial simplification saves a line and keeps the
mathematical stages explicit. No helper extraction or statement change is warranted.

## Actual verification and diff gates

- `diff -u /private/tmp/decl19-before.lean Roth/Taylor.lean`: only target proof changed:
  one coefficient-simplification consolidation and three lambda arrows.
- Native `lean_diagnostic_messages({file_path:"Roth/Taylor.lean",timeout_s:40})`, repeated
  with timeout_s:30 after freeze: **whole file**, no start/end/declaration filter,
  `partial:false`, `success:true`, `timed_out:false`, no failed dependencies;
  only preserved line-1 header warning.
- `/Users/ramin/.elan/bin/lake build Roth.Taylor`: exit 0, Built Roth.Taylor (9.7s),
  `Build completed successfully (1439 jobs).` Existing Box/HasseDeriv/Taylor header warnings.
- `/Users/ramin/.elan/bin/lake env lean /private/tmp/decl19-isolated.lean`: exit 0.
  This file copies only the source prefix before target, then the ORIGINAL statement with
  renamed `audit_original_type` and final proof; it neither imports Roth.Taylor nor includes
  target/later declarations. `#print axioms` returns exactly
  `[propext, Classical.choice, Quot.sound]`.
- No sorry, axiom declaration, native_decide, diagnostic suppression, or limit raise added.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | actual module build exit 0 above |
| definition_protected | pass | no def/abbrev changed |
| theorem_statement_protected | pass | full original signature byte-identical |
| structure_gate | pass | 15 including := by, 14 tactic lines, branches ≤10, no ∧ |
| naming_gate | pass | descriptive name, no forbidden pattern |
| line_packing_gate | pass | all three measured rows above |
| inequality_orientation_gate | pass | zero reversed inequalities above |

Overall: pass. Parent owns full build and subsequent independent LeanEval; neither claimed
as worker-run evidence.

## Result and eleven checks

Before: 16 proof lines. After: 15. Saved: 1.
Audit issues: 2; fixed: 2; deferred: 0. Applied: 1.14-related simplification consolidation,
ordinary lambda Unicode formatting. Renames queued: none. Proof comments: none present.
Existing docstrings/module header preserved. Refactoring needed: none.

- [x] Step 1: references read.
- [x] Step 2: complete 24-item audit.
- [x] Step 2.5: five-method search-status evidence.
- [x] Step 2.6: per-parameter generalisation and public literature search.
- [x] Step 2.7: complete signature width table.
- [x] Step 2.8: inequality scan table.
- [x] Step 3: all 42 golfing rules have statuses.
- [x] Step 4: step-back reflection.
- [x] Step 5a: native complete whole-file diagnostics clean except preserved header warning.
- [x] Step 5b: actual build, isolated original-type proof/axioms, and all diff gates pass.
- [x] Step 6a: rename check complete; no rename required.
