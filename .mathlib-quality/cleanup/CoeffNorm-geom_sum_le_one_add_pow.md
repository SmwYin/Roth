# Phase 4: Roth.geom_sum_le_one_add_pow

Scope: only the theorem at `Roth/CoeffNorm.lean:200–206` and this report. Original and final
declaration: 7 lines, 5 tactic lines; saved 0 lines, reduced the final membership conversion.
No Git operations, shared-log writes, imports, public types, instances, definition values,
names, or docstrings changed. The original §6 source quotation is preserved byte-for-byte.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md, as well as both SKILL.md files, the full
worker contract, style-rules.md and naming-conventions.md.

Baseline supplied by file owner: full `lake build` and separate `lake build Roth.LeanEval`
session 89064 exited 0; complete baseline LSP had no errors. These were not repeated here.

## Mathematics and changes

Expand `(t + 1)^r`, compare summands using nonnegative `t^m`, and use positivity of
`r.choose m` when `m ≤ r`. Replaced the two-step conversion
`Nat.lt_succ_iff.1 (Finset.mem_range.1 hm)` with `Finset.mem_range_succ_iff.1 hm`.
Normalized the ordinary lambda arrow from `=>` to `↦`.

## Full audit

| # | Item | Concrete finding/action |
|---|---|---|
| 1 | LINT | No target warnings. Complete final LSP: no errors, six pre-existing outside warnings. |
| 2 | HAVE SCAN | No `have` in the target. |
| 3 | SET_OPTION | No per-declaration options. |
| 4 | SIMP SQUEEZE | No `simp` calls in final proof. |
| 5 | NAMING | Descriptive snake_case, mathlib-standard `geom_sum`; no forbidden abbreviation or numeric pattern. |
| 6 | LINE PACKING | Both signature lines measured below; neither can absorb the next complete signature expression. |
| 7 | BY PLACEMENT | `by` is at end of conclusion line. |
| 8 | FORMAT | Two-space tactics, no internal blank lines, one tactic per line; normalized lambda arrow. |
| 9 | COMMENTS | No inline proof comments; existing source quotation preserved. |
| 10 | DOCSTRING | Existing explanatory statement and §6 attribution preserved under explicit documentation protection. |
| 11 | VISIBILITY | Public API preserved; no deletion/privatization requested. |
| 12 | STRUCTURE | Five tactic lines, no conjunction, no branches; comfortably below extraction thresholds. |
| 13 | MATHLIB | Five methods and compiled exact-search probe below; retained direct binomial comparison. |
| 14 | JUNK DEF | n/a: theorem, no data definition. |
| 15 | EXISTS LEMMA | n/a: no existential statement or witness wrapper. |
| 16 | SHOW vs CHANGE | n/a: no `show`. |
| 17 | PUSH_NEG | n/a: no negation pushing. |
| 18 | GENERALISE | All three parameters assessed and actual drop probes executed below. |
| 19 | INEQUALITY | Two `≤` occurrences and no reversed comparisons in code; table below. |
| 20 | NORMAL-FORM | Finite range sum and binomial power already standard; field quotient form would add exceptional cases. |
| 21 | SYNTAX-GEN | OK: explicit degree and nonnegativity fit evaluation-bound call site; no beneficial public restatement needed. |
| 22 | IMPORT-FANOUT | n/a: no new imports. |
| 23 | CASTS | Diff introduces zero coercions/ascriptions: 0 dropped, 0 cross-type, 0 load-bearing. Existing `(1 : ℝ)` untouched. |
| 24 | INSTANCE-NAME | n/a: no instance declarations. |

Issues found: ordinary lambda arrow and avoidable two-lemma membership conversion; both fixed.
Refactoring needed: none. Optional abstract versions were closed under the explicit
public-type-preservation instruction; no concrete downstream need requires one here.

## Mathlib search-status

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | finite geometric sum bounded by `(1+x)^n` for nonnegative x | Bernoulli bounds `Real.mul_add_one_le_add_one_pow`, `one_add_mul_le_pow'`, and field geometric bounds; no exact match returned. |
| B Loogle | `"geom", _ ≤ _ ^ _` | `Real.harm_mean_le_geom_mean`, unrelated. |
| C LeanSearch | sum of powers from zero to n is at most `(1+x)^n` for nonnegative x | Exponential factorial sum, `geom_sum_lt`, `geom_sum_Ico_le_of_lt_one`, `Nat.geom_sum_le`, power superadditivity; no exact match. |
| D source rg | `geom_sum_le`, `sum.*choose`, `choose_pos`, `geom_sum.*pow`; full-name `geom_sum_le_one_add_pow`, `geom_sum.*one_add`, `geom_sum.*add_one` | Building blocks `Nat.choose_pos`, `Nat.sum_range_choose`, `add_pow`; no exact mathlib declaration found. Initial path `Algebra/GeomSum.lean` did not exist; corrected to Algebra/Order and Algebra/Ring in the subsequent untruncated query. |
| E local name | `geom_sum_le` | `Nat.geom_sum_le` and this Roth theorem; index unavailable, so empty-index absence was never asserted. |

Auxiliary variants: `_lt`, `_Ico_le_of_lt_one`, `_one_add`, `_add_one`, and coefficient
`choose_pos` / `mem_range_succ_iff`; source read confirms the latter membership lemma.
Common-equivalents table: no relevant topology/finiteness/bornology bucket.
Compiled/live absence probe: whole-target `exact?` could not close; `apply?` after expansion
suggested `Finset.sum_le_sum` with the expected coefficient subgoal and numerous unrelated
partial inequality routes. No broad absence theorem is claimed; no replacement was found.
Conclusion: partial matches only; retain the local bound built directly from existing
binomial and order API. No wrapper deletion authorized. No missing coercion/structure API
signals occur: these five lines express the coefficient comparison itself.
Strict rules: no new wrappers or custom predicates, all five methods attempted, auxiliary
variants searched, no exact equivalent found to delete, and mathlib usage documented here
without modifying protected module documentation.

## Public literature search

Actual query: `geometric sum inequality (1+x)^n binomial coefficients nonnegative generalization`.
The first three returned hits were:

1. [Binghamton Math 330 notes](https://people.math.binghamton.edu/mfochler/bu-mfx/bu-math-arv/math-330-arv/math-330-2020-08/html/lec-notes/bu-ln-330-m330-solns-2020-10-22.pdf), finite geometric series and binomial theorem teaching material.
2. [Iliman–de Wolff, simplex Newton polytope bounds](https://arxiv.org/abs/1402.6185), broader polynomial nonnegativity, not a replacement for this finite estimate.
3. [Generalization of Bernoulli's inequality discussion](https://math.stackexchange.com/questions/1460629/prove-the-generalization-of-bernoullis-inequality), related but a different lower polynomial bound.

Canonical supplementary result returned: [binomial theorem](https://en.wikipedia.org/wiki/Binomial_theorem), finite expansion for natural exponents. The inference relevant here is coefficientwise comparison for nonnegative t; extension to arbitrary real exponents does not preserve a finite range indexed by r. ChatGPT math MCP: n/a, no such tool was exposed in ALL_TOOLS. No literature-driven API change required.

## Mechanical generalisation

| # | Parameter | Class/use | Catalogue candidates and actual evidence | Result |
|---|---|---|---|---|
| 1 | `{t : ℝ}` | Structure value; powers, order, binomial expansion | Drop tested with `autoImplicit false`: unbound t in ht/conclusion. Abstract ordered-semiring restatement is a public-type change, closed under preservation; no typeclass parent, decidability, universe, point-local/global or strictness parameter exists here. | Keep original binder. |
| 2 | `(ht : 0 ≤ t)` | Proposition; used in `pow_nonneg ht m` | Drop tested: unbound ht at the nonnegativity proof. A compiled counterexample shows the unrestricted result false at t = -1, r = 2. Already weak inequality; point-localisation n/a, a single scalar fact. | Keep; essential. |
| 3 | `(r : ℕ)` | Structure value; range endpoint, exponent and binomial coefficient | Drop tested with `autoImplicit false`: unbound r in conclusion. Arbitrary ordered index would change range, power and choose meanings, so no content-preserving mechanical weakening. No universe/instance/strictness/global-hypothesis candidates. | Keep original binder. |

Probe paths: `/private/tmp/roth-geom-drop-probes.lean` (expected errors),
`/private/tmp/roth-geom-probes.lean` (positive exact-type, reproof, counterexample and axioms).
Inversion check: no distinguished concrete witness is unfolded; the theorem already
quantifies freely over the scalar and natural degree. An abstract scalar type would be
an optional public restatement, not a required fix. No unused inherited σ binder is
present in the elaborated target type.

## Packing and inequality artifacts

Actual width-100 output:

```lean
@Roth.geom_sum_le_one_add_pow : ∀ {t : ℝ}, 0 ≤ t → ∀ (r : ℕ), ∑ s ∈ Finset.range (r + 1), t ^ s ≤ (1 + t) ^ r
```

Lean's #check renderer prints that type as one info line even under format.width 100;
source declaration layout uses the complete conclusion as a mathematical expression.

| Signature line | Codepoints | Next complete expression | Arithmetic | Action |
|---|---:|---|---|---|
| 200 | 62 | `∑ s ∈ Finset.range (r + 1), t ^ s ≤ (1 + t) ^ r := by` (53) | 62 + 1 + 53 = 116 > 100 | ok |
| 201 | 57 | proof body follows | n/a | ok |

No signature edits needed; both lines unchanged. Actual body widths: 34, 40, 23, 52, 64.

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 1 | ht | `0 ≤ t` | already correctly oriented | none |
| 2 | conclusion | finite sum `≤ (1 + t) ^ r` | already correctly oriented | none |
| — | all signature code | no `≥` or `>` occurrences | n/a | none |

## Every golfing rule

| Rule | Status |
|---|---|
| 1.1 | n/a: no by-exact wrapper. |
| 1.2 | n/a: no by-rfl wrapper. |
| 1.3 | n/a: rewrites followed by inequality refinement, not exact matching term. |
| 1.4 | n/a: no simp/exact chain. |
| 1.5 | n/a: no trailing rfl. |
| 1.6 | n/a: no constructors. |
| 1.7 | n/a: no apply/exact chain. |
| 1.8 | n/a: no contradiction proof. |
| 1.9 | lambda cannot eta-reduce: both m and hm build a subproof; arrow normalized to ↦. |
| 1.10 | n/a: no have. |
| 1.11 | already refined with lambda, no separate intro. |
| 1.12 | n/a: no show. |
| 1.13 | n/a: no product projections. |
| 1.14 | existing adjacent commutation/expansion rewrites already merged; remaining rewrites occur after introducing summand. |
| 1.15 | n/a: no terminal simp only. |
| 1.16 | n/a: no nonterminal bare simp. |
| 1.17 | membership lemma direct `.1` projection retained; simplified compound conversion. |
| 1.18 | n/a: no unnecessary trailing parens around tactic/lambda argument. |
| 1.19 | n/a: no push_neg. |
| 1.20 | n/a: no existential helper. |
| 2.1 | whole proof grind tried: failed contradiction goal for finite sum bound. |
| 2.2 | n/a: no existing grind chain. |
| 2.3 | whole-target simp tried: made no progress; post-expansion simp leaves coefficient comparison. |
| 2.4 | n/a: no function-property goal. |
| 2.5 | actual coefficient positivity attempt failed: `not a positivity goal`; inline positivity for t^m succeeds but is longer than `pow_nonneg ht m`. |
| 2.6 | actual gcongr at coefficient multiplication failed to make progress. |
| 2.7 | lia at coefficient multiplication failed: power/binomial order facts are missing; direct range-membership API supersedes arithmetic conversion. |
| 2.8 | whole-target aesop tried: made no progress; post-expansion search also did not close comparison. |
| 2.9 | norm_cast then choose_pos succeeds, two tactics vs exact_mod_cast one; norm_num multiplication probe leaves goal. |
| 2.10 | n/a: universal symbolic real inequality is not finite decidable computation. |
| 2.11 | n/a: no denominators or field identity. |
| 2.12 | n/a: no ring-ending equality or linear combination of polynomial equations. |
| 2.13 | n/a: no symmetric branches. |
| 2.14 | n/a: no calc chain. |
| 2.15 | n/a: no repeated sibling goals. |
| 3.1 | n/a: no erw. |
| 3.2 | n/a: no continuity/measurability. |
| 3.3 | n/a: no omega; lia failed as recorded in 2.7. |
| 3.4 | n/a: no rcases. |
| 3.5 | no new attributes: global automation change has no concrete benefit here. |
| 3.6 | n/a: no simp_all only. |
| 3.7 | n/a: no heartbeat options. |

## Reflection and verification

Single-tactic grind/simp/aesop/exact? failed. apply? suggested the same sum comparison
after expansion. No `have` blocks remain to compose. Term-mode inline positivity was
tested; it closes the multiplication goal but produces a longer nested term and an
expected `No goals to be solved` from the subsequent original tactic in the live probe.
The retained proof exposes the binomial comparison in five straightforward steps.
Alternative induction would require a new recurrence estimate and be longer.

All source edits finished before SOURCE FROZEN; whole-file SHA256
`0aaf92ee5addd94f9c952317d166f8e29d4247d4f2412ac312bee11ca2d448e1`.
The file owner explicitly revoked source ownership at that hash. No subsequent source edits.

Actual final build: `/Users/ramin/.elan/bin/lake build Roth.CoeffNorm`, session 83702,
exit 0, built CoeffNorm in 19 seconds, 1658 jobs. Complete final native LSP diagnostics:
`partial=false`, `timed_out=false`, `success=true`, no errors, no failed dependencies.
Six outside warnings: header; DecidableEq in normOne_mul_le/normOne_prod_le/normOne_det_le/
abs_coeff_det_hasseDeriv_le; unused hC in normOne_det_le. Preserved as instructed.
Exact type and independent non-self reproof CLI session 52207 exited 0; both target and
independentGeom axioms were exactly `[propext, Classical.choice, Quot.sound]`.

| Gate | Result | Actual evidence |
|---|---|---|
| lake_build_file | ✓ pass | session 83702 exit 0, Roth.CoeffNorm built. |
| definition_protected | ✓ pass | Only two target proof lines changed; no definitions. |
| theorem_statement_protected | ✓ pass | Both original signature lines unchanged; exact original-type assignment compiled. |
| structure_gate | ✓ pass | Five tactic lines; no conjunction or long branch. |
| naming_gate | ✓ pass | No forbidden pattern or abbreviation. |
| line_packing_gate | ✓ pass | Complete measured two-row table above; no repack rows. |
| inequality_orientation_gate | ✓ pass | Complete scan above; zero reversed inequalities in code. |

Overall: pass. Renames queued: none. Comments preserved: no inline comments present;
all existing documentation preserved. Refactoring needed: none.

- [✓] Step 1 — reference docs read.
- [✓] Step 2 — all 24 audit items reported.
- [✓] Step 2.5 — all five mathlib search methods reported.
- [✓] Step 2.6 — all parameters mechanically assessed with actual probes.
- [✓] Step 2.7 — complete per-line width table and width-100 #check recorded.
- [✓] Step 2.8 — complete inequality occurrence table recorded.
- [✓] Step 3 — all 42 golfing rules have a status.
- [✓] Step 4 — step-back reflection and alternative strategy recorded.
- [✓] Step 5a — complete final LSP has no errors.
- [✓] Step 5b — actual build and all diff gates pass.
- [✓] Step 6a — no rename needed, no shared sidecar modified.
