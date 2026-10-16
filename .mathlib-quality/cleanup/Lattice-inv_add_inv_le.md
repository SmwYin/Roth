# Phase 4 — `inv_add_inv_le`

Dedicated single-declaration worker; 2026-10-16. Scope: `Roth/Lattice.lean:34–39`
and this report only. Source unchanged (6 declaration lines, 4 proof lines → same).
Baseline supplied by owner: full project + LeanEval pass; complete module LSP has only
the existing header warning. No Git mutation, shared-progress edits, or version edits.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md. Also read both skill entrypoints,
the complete Phase-4 worker prompt, and relevant style/naming sections.

## Mathematics and full audit

The paired reciprocals have positive denominators. Their common numerator is `2 * lam`;
the denominator product exceeds `lam ^ 2 - 1` by `x * (2 - x) ≥ 0`.
Cross-multiplication and polynomial arithmetic prove the estimate.

| # | Audit | Concrete result |
|---|---|---|
| 1 | LINT | No target warning/error. Complete file diagnostics: existing header warning only. |
| 2 | HAVE SCAN | `ha` at L36, `hb` at L37 each contain `by linarith`; each used twice, in nonzero proofs and `mul_pos`; retain both. |
| 3 | SET_OPTION | None. No limits introduced. |
| 4 | SIMP SQUEEZE | No simp calls. |
| 5 | NAMING | Descriptive snake_case reciprocal-sum bound; no forbidden abbreviation/numeric/structural name. Standard mathematical property, no `_aux` rename required. |
| 6 | LINE PACKING | Both signature lines measured below; no repack. |
| 7 | BY PLACEMENT | `by` at end of statement and local-have lines. |
| 8 | FORMAT | Two-space proof indent, no blank proof lines, one tactic per line; no haveI/letI. |
| 9 | COMMENTS | None present; none removed. |
| 10 | DOCSTRING | Private helper, no docstring required; none added. |
| 11 | VISIBILITY | Already private, single in-file caller `sum_inv_le`; retain. |
| 12 | STRUCTURE | Four proof lines, no conjunction or branches; no decomposition required. |
| 13 | MATHLIB | Five actual methods below. Partial building blocks verified; exact? fails; retain custom polynomial estimate. |
| 14 | JUNK DEF | n/a: lemma, not a definition. |
| 15 | EXISTS LEMMA | n/a: inequality, no existential witness. |
| 16 | SHOW vs CHANGE | n/a: neither appears. |
| 17 | PUSH_NEG | n/a: no negation tactic. |
| 18 | GENERALISE | Every parameter audited below. Compiled bound weakenings closed without application by owner instruction; no current caller benefit. |
| 19 | INEQUALITY | Zero ≥/> occurrences, table below. |
| 20 | NORMAL-FORM | Already reciprocal arithmetic followed by ≤ bound, consistent with caller. No alternate canonical object. |
| 21 | SYNTAX-GEN | Current separate lower/upper x bounds are supplied directly by caller. Bundling into Icc gives no application improvement. |
| 22 | IMPORT-FANOUT | n/a: no new imports. |
| 23 | CASTS | 0 dropped / 0 cross-type / 0 load-bearing casts in diff; source unchanged. Binder ℝ is the required type specification. |
| 24 | INSTANCE-NAME | n/a: no instance declaration. |

Issues to fix: none after the exhaustive pass. Refactoring needed: none.

## Mathlib search-status

| Method | Actual query | Actual outcome |
|---|---|---|
| A Lean-Finder | `For 0 ≤ x ≤ 2 and 2 < λ, bound 1/(λ-1+x)+1/(λ+1-x) by 2*λ/(λ^2-1)` | Success; 5 hits, including `sub_one_div_inv_le_two`, Hurwitz kernel bounds, ADE reciprocal sum, Akra–Bazzi smoothing, rpow integrand; none directly proves target. |
| B Loogle | `_⁻¹ + _⁻¹ ≤ _` | Success; empty items. |
| C LeanSearch | `upper bound sum reciprocal positive numbers with fixed sum and lower bound` | Success; harmonic/log, FloorPow, mean inequalities, Holder and Summable hits, no direct target. |
| D source rg | `inv_add_inv_le|inv_add_inv|div_le_div_iff₀` in Algebra/Order/Field and Algebra/Field/Basic | Actual hits: Basic.lean L49 `inv_add_inv'`, L74 `Commute.inv_add_inv`, L164 `inv_add_inv`. No source exact-name match in that search. |
| E local names | `inv_add_inv` (20 results), then `inv_add_inv_le` | Actual positive hits include `inv_add_inv`, `inv_add_inv'`, `Commute.inv_add_inv`, Holder reciprocal lemmas and local target. Index was **warming**, so empty/partial coverage proves no absence. |

Auxiliary variants checked: `inv_add_inv'`, `Commute.inv_add_inv`, Holder reciprocal-sum
equalities, `div_le_div_iff₀`. Common-equivalents table: no matching discrete/finite/
separation/bornology bucket. Native run_code successfully #checked `@inv_add_inv` and
`@div_le_div_iff₀`. Native live multi_attempt `exact?` failed; `apply?` returned only
partial order/real conversion routes, no completed target proof. This is positive
evidence for the existing building-block proof, **not an absolute absence claim**.
No DNS failure or warming index is treated as absence. No thin 1–3-call wrapper:
the final nlinarith discharges the substantive polynomial bound.
No wrapper API, new predicate, module-docstring edit, or speculative public extraction.

## Generalisation status

All candidates below were actually elaborated with native run_code; failed experimental
declarations were never inserted into the source. Successful candidates preserve the
conclusion. The owner explicitly closed optional generalisations without current caller
benefit, so successful explicit-bound changes are retained only as evidence.

| Parameter | Class/use | Candidates/probes | Result |
|---|---|---|---|
| `lam : ℝ` | structure value; appears in every denominator and RHS | Drop not meaningful: conclusion depends on lam; would create an unbound variable. No pointwise/universe/decidability candidate applies to a scalar value. Abstract-field restatement closed as optional with no caller benefit. | Retain exact real binder. |
| `x : ℝ` | structure value; both paired denominator terms | Drop not meaningful: conclusion depends on x. No point-localisation, universe or typeclass-parent candidate applies to a concrete scalar binder. Optional abstract restatement closed. | Retain exact real binder. |
| `hlam : 2 < lam` | proposition; positivity of both factors and lam²−1 | Drop: fails both `linarith` positivity goals and denominator nlinarith. Replace by `1 ≤ lam`: same failures. `2 ≤ lam`: compiles. `1 < lam`: compiles with unchanged proof. | Retain exact signature: caller supplies `2 < lam` directly; weakening changes explicit premise type and needs adjacent caller adaptation, with no current benefit. Owner explicitly approved no-op. |
| `hx0 : 0 ≤ x` | proposition; first-factor positivity and x(2−x) | Drop: first linarith fails and final hx0 reference unbound. Already weak inequality; strict→weak unavailable. | Retain; compiled counterexample lam=3,x=−1 refutes dropping it. |
| `hx2 : x ≤ 2` | proposition; second-factor positivity and x(2−x) | Drop: second linarith fails and final hx2 reference unbound. Already weak inequality; strict→weak unavailable. | Retain; compiled counterexample lam=3,x=3 refutes dropping it. |

Compiled numeric counterexample lam=1,x=1 refutes the `1 ≤ lam` weakening itself,
not merely the chosen proof. No global function property is available to point-localise;
no implicit universe, decidability, bundled structure, or class hypothesis to weaken.
Inversion check: no named concrete object to unfold; only scalar field/order arithmetic.
Literature search: **n/a: private decl, literature search not required**.
Big-change candidates: none pending. Optional generic API exploration is closed.

## Line packing

Native successful run_code used `set_option format.width 100` and `#check @probe`,
where probe was an independently declared exact original type with original proof:

```text
@probe : ∀ {lam x : ℝ}, 2 < lam → 0 ≤ x → x ≤ 2 → (lam - 1 + x)⁻¹ + (lam - 1 + (2 - x))⁻¹ ≤ 2 * lam / (lam ^ 2 - 1)
```

| Signature line | Codepoints | Next token | Arithmetic | Action |
|---|---:|---|---|---|
| 34 | 87 | `(lam - 1 + x)⁻¹` (15) | 87 + 1 + 15 = 103 > 100 | ok |
| 35 | 75 | No next signature line; proof follows | n/a | ok |

Measured with Python len on source strings (codepoints). Both source lines ≤100.
The full conclusion also cannot join line34 (87 + 1 + 71 = 159).

## Inequality scan

| # | Location | Original | Rewrite | Lemma rename? |
|---|---|---|---|---|
| 1 | Entire signature L34–35 | No ≥/> | n/a | n/a — no ≥/> in signature |

## Every golfing rule

| Rule | Status |
|---|---|
| 1.1 | n/a: no by exact wrapper. |
| 1.2 | n/a: no by rfl. |
| 1.3 | n/a: rw followed by nlinarith, not exact. |
| 1.4 | n/a: no simp/exact sequence. |
| 1.5 | n/a: no simp/rfl. |
| 1.6 | n/a: no constructor. |
| 1.7 | n/a: no apply/exact sequence. |
| 1.8 | n/a: no contradiction proof. |
| 1.9 | n/a: no lambda. |
| 1.10 | Both haves have proof content and two uses each; retain. |
| 1.11 | n/a: no apply/intro. |
| 1.12 | n/a: no show. |
| 1.13 | n/a: no conjunction projection. |
| 1.14 | Already one combined rw list. |
| 1.15 | n/a: no terminal simp only. |
| 1.16 | n/a: no nonterminal simp. |
| 1.17 | Already uses ha.ne', hb.ne', sub_nonneg.2. |
| 1.18 | n/a: the by nlinarith argument is inside a rewrite lemma application; trailing `<|` would not improve enclosing list syntax. |
| 1.19 | n/a: no push_neg. |
| 1.20 | n/a: not existential. |
| 2.1 | Actual whole-goal grind fails, including denominator-zero branch. |
| 2.2 | n/a: no grind retained, so no preceding tactics to delete. |
| 2.3 | n/a: no simp sequence to consolidate. |
| 2.4 | n/a: no function property. |
| 2.5 | Actual whole-goal positivity says not a positivity goal; local affine differences require bound arithmetic already handled directly by linarith. |
| 2.6 | Actual whole-goal gcongr makes no progress. |
| 2.7 | n/a: real rational inequality, no Nat/Int arithmetic. |
| 2.8 | Actual whole-goal aesop makes no progress. |
| 2.9 | n/a: symbolic estimate; no cast or numeric computation to replace. Numeric counterexamples separately verified by norm_num. |
| 2.10 | n/a: real symbolic inequality, no finite decidable computation. |
| 2.11 | Actual field_simp/nlinarith alternative leaves rational inequality and fails; not a field identity for ring. |
| 2.12 | n/a: no ring/ring_nf terminal equality; nlinarith uses inequalities. |
| 2.13 | n/a: no symmetric case branches. |
| 2.14 | n/a: no calc. |
| 2.15 | n/a: no multiple similar goals. |
| 3.1 | n/a: no erw. |
| 3.2 | n/a: no legacy analysis tactic. |
| 3.3 | n/a: no omega or integer arithmetic. |
| 3.4 | n/a: no rcases. |
| 3.5 | Private one-caller estimate; no global automation registration justified. |
| 3.6 | n/a: no simp_all. |
| 3.7 | n/a: no heartbeat/recursion limit. |

Step back: the four lines expose positivity, cross-multiplication, and the sole polynomial
estimate directly. Tried grind, aesop, exact?, apply?, positivity, gcongr and field_simp.
No completed one-tactic replacement or shorter useful term proof emerged; retain clear proof.

## Verification and gates

`/Users/ramin/.elan/bin/lake build Roth.Lattice` actual exec session19043 exited0;
log `/private/tmp/roth-lattice-inv_add_inv_le-module.log` ends
`Build completed successfully (2214 jobs).` No fullproject or LeanEval build run by worker.

Complete native `lean_diagnostic_messages` returned success=true, partial=false,
timed_out=false, failed_dependencies=[]; only pre-existing line1 header warning
(`Copyright too short!`). Header retained under explicit user instruction; no suppression.

Independent `probe` at the **exact original type**, using the original four-line proof
and no self-reference, compiled with standard axioms `[propext, Classical.choice, Quot.sound]`.
Numeric counterexample scratch lines had long-line warnings; scratch only, no source warning.
Actual built private target was separately found in imported Roth.Lattice environment as
`_private.Roth.Lattice.0.Roth.inv_add_inv_le`; `Lean.collectAxioms` on that loaded constant
returned `[propext, Classical.choice, Quot.sound]`. Native lean_verify also returned
trust=standard, non_standard_axioms=[], source warnings=[]. Initial literal-name #checks
failed because the numeric private name component was not expressible by that quoted
syntax; the subsequent environment lookup inspected the actual imported constant successfully.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Actual module command/session19043 exit0 above. |
| definition_protected | pass | No source edit; every definition byte-identical. |
| theorem_statement_protected | pass | Exact target signature byte-identical. |
| structure_gate | pass | Four-line body; no branches/conjunction. |
| naming_gate | pass | Mathematical name; no forbidden pattern/abbreviation. |
| line_packing_gate | pass | Both lines measured; 103>100 boundary; no repack. |
| inequality_orientation_gate | pass | Zero ≥/> in signature. |
| new_identifiers | pass | No source diff introduces any identifier. |
| original_exact_type | pass | Independent compiled proof, standard axioms. |
| actual_built_target_axioms | pass | Imported environment constant, standard axioms. |

Overall: pass. Source SHA256:
`9d5a4630daf715a8a7c8248c41046c74276421ccc603c004d020e129d049c53c`.

Before: 6 lines. After: 6 lines. Saved: 0. Audit issues found: 0 requiring edits.
Rules applied: none; justified no-op after full pass. Renames queued: none.
Comments-preserved: none present. Refactoring needed: none. No pending user question.

## Phase checklist

- [✓] Step 1 — references read.
- [✓] Step 2 — full24 audit printed.
- [✓] Step 2.5 — five-method search block printed with actual outcomes.
- [✓] Step 2.6 — every parameter audited, concrete probes recorded.
- [✓] Step 2.7 — every signature line measured with width100 #check reference.
- [✓] Step 2.8 — inequality scan table printed.
- [✓] Step 3 — all42 rules have status.
- [✓] Step 4 — step-back reflection and actual alternatives recorded.
- [✓] Step 5a — complete LSP clean except explicitly retained pre-existing header.
- [✓] Step 5b — module/diff/protection/axiom gates passed.
- [✓] Step 6a — no renames required; shared queue untouched.

Source ownership is now explicitly revoked/frozen at the above hash; worker will make no
further source mutation. Owner may run sequential whole-project and LeanEval gates.

Owner checkpoint: source ownership explicitly revoked before sequential full/separate LeanEval session74194; both exit0 (6.14s/2.86s), frozen hash stable. Logs `/private/tmp/roth-lattice-d02-{full,leaneval}.log`.
