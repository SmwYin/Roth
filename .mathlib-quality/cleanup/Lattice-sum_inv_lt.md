# `Roth.sum_inv_lt` declaration cleanup

Scope: only `sum_inv_lt` in `Roth/Lattice.lean` and this report. Public type,
documentation, mathematical content, versions, and file header are protected.
Baseline: complete LSP `partial=false`, `success=true`; only warning is line 1 copyright.
All required references read, including the complete five search/golf/generalisation/gates
references, Phase 4 prompt, and relevant style/naming sections. No helpers planned.

## Mathematical content

The paired reciprocal sum is bounded above by `(r+1) lam/(lam²-1)`. Since
`sqrt(1-1/m) < 1-lam⁻²` and both denominators are positive, reversing reciprocals
gives the desired strict bound. The square-root quotient identity normalizes its RHS.
The argument is a specialized quantitative bound, not a wrapper around one mathlib result.

## Full audit (before edits; lines 62–85)

1. LINT: no warnings in target range; complete module has only preexisting header warning.
2. HAVE SCAN: `hm'` has `by`, keep cast proof; `hsq1` is a no-`by` lemma application,
   used once in `hlam2`, INLINE; `hlam2` has `by`, keep positivity threshold proof;
   `hpos1` has a proof-bearing argument but no outer `by`, used once, retain explicit
   typed sqrt positivity fact (its argument contains actual rewrite/arithmetic proof);
   `hsqrt` has `by`, keep square-root identity; `hlam'` has `by`, keep rational identity;
   nested anonymous `have : lam ≠ 0` has `by`, keep field denominator evidence.
3. SET_OPTION: none; no limit increases or suppressions.
4. SIMP SQUEEZE: no `simp` calls; `field_simp` is denominator normalization, not `simp`.
5. NAMING: `sum_inv_lt` explicitly describes a strict reciprocal-sum bound, snake_case,
   no forbidden abbreviation, scheme number, single-letter public name, or ge/gt naming.
   No rename is needed or queued.
6. LINE PACKING: all three signature rows measured below; no type changes.
7. BY PLACEMENT: all `by` keywords are on the preceding declaration/tactic line.
8. FORMAT: two-space proof indent, no empty lines; split semicolon in `hpos1`.
9. COMMENTS: none inside target proof. Preserve all surrounding comments.
10. DOCSTRING: present, includes exact source; protected by task instructions, unchanged.
11. VISIBILITY: public result intentionally protected by task; no visibility change.
12. STRUCTURE: 21 body lines before edits, below 30/60; no conjunction or case branch.
    Target is not named in a module `Main results` list. No extraction justified.
13. MATHLIB: five-method status below; use existing `Real.sqrt_div'` directly.
14. JUNK DEF: n/a, theorem not definition.
15. EXISTS LEMMA: n/a, conclusion is a strict inequality, not existential.
16. SHOW vs CHANGE: no `show` or `change` in target.
17. PUSH_NEG: none.
18. GENERALISE: every binder probed below; preserve public API and close optional API work.
19. INEQUALITY: every Lean inequality already `<` or `≤`; table below.
20. NORMAL-FORM: inverse notation matches paired-sum API; sqrt quotient normalized only
    inside proof by `Real.sqrt_div'`. No competing equivalence API created.
21. SYNTAX-GEN: current form directly feeds `card_filter_weight_le`; abstract endpoints
    or a weaker threshold would require additional caller conversions without benefit.
22. IMPORT-FANOUT: n/a, no new imports.
23. CASTS: public casts fixed; proof casts bridge Nat to Real or fix ordered numeric types.
    Remove avoidable `(by linarith : (0 : ℝ) ≤ m)` in favor of `Nat.cast_nonneg m`.
24. INSTANCE-NAME: n/a, no instance declarations.

Issues to fix: inline `hsq1`; split chained tactics; use direct cast-nonneg theorem.
Refactoring needed: none. Earlier declined sqrt threshold generalization remains closed.

## Mathlib search status

| Method | Actual query | Outcome |
|---|---|---|
| A Lean-Finder | Upper bound on finite sum of reciprocals `lam-1+2j/r` by reciprocal lam times sqrt m/(m-1) | ADE reciprocal restriction, geometric-power reciprocal sums, Euler–Mascheroni bound; no exact match |
| B Loogle | `Real.sqrt (_ / _) = _` | `Real.sqrt_div`, `Real.sqrt_div'` |
| C LeanSearch | sum of reciprocals arithmetic progression upper bound square root | `harmonic_le_one_add_log`, inverse-square sum bounds, floor-power bounds |
| D source rg | full names `sum_inv_lt`, `sum_inv_le` across entire mathlib source; `sqrt_div`, `lt_sqrt_of_sq_lt` in sqrt/ordered-sum sources | sqrt quotient and comparison API; untruncated full-name search has no matches (exit 1) |
| E local name | `sqrt_div` | Real/NNReal quotient variants; actual positive matches, index warming does not establish absence |

Auxiliary variants: sqrt_div, sqrt_div', sqrt_div_self, sqrt_div_self', lt_sqrt_of_sq_lt.
Common-equivalents table: no discrete/finiteness/boundedness bucket applies.
Conclusion: partial mathlib match; retain specialized bound and use sqrt API directly.
No claim of global absence. `exact?` failed on live original goal; `apply?` supplied only
generic comparison/conversion introductions, no completed bound. `grind`, `simp`, `aesop`
also fail on the full live goal. No new declaration is introduced.

## Literature search status (public declaration)

Actual web queries: `"Roth" "lattice" "harmonic" sum inequality generalization`;
`"sum of reciprocals" "arithmetic progression" "convex" upper bound`;
`"Takloo-Bighash" "Yin" "Formalizing Roth"`;
`"Hermite" "Hadamard" convex inequality upper bound endpoints generalization`.
The broad first searches yielded unrelated arithmetic-progression results, not usable
generalizations. The last yielded the following primary mathematical papers:

- [Steinerberger, Hermite–Hadamard in higher dimensions](https://arxiv.org/abs/1808.07794):
  a general convex endpoint/integral average bound, with higher dimensional extensions.
- [Generalizations of Hermite–Hadamard Type Integral Inequalities](https://www.mdpi.com/2075-1680/10/3/136):
  integral convex-function bounds rather than the discrete specialized threshold here.
- [A generalization of Hadamard's inequality](https://www.sciencedirect.com/science/article/pii/S0893965907001371):
  general convex integral mean bounds.

Read local source `.mathlib-quality/references/clean.tex` lines 1100–1120: it states the
same r≥1, m≥2, λ>2√m bound and derives it by pairing plus reciprocal comparison.
Inference: convex endpoint arguments motivate an abstract finite-grid estimate, but do
not establish a useful replacement for this downstream induction's exact shape.
Math ChatGPT MCP: unavailable (no matching tool in exposed ALL_TOOLS).
Literature-driven API changes: none; optional abstractions without caller benefit closed.

## Line packing and inequality scan

Signature is byte-identical; codepoint widths include indentation. Expressions are kept
intact at the relation boundary (not split token-by-token inside the sum or product).

| Signature line | Chars | Next complete expression token | Arithmetic | Action |
|---|---:|---|---|---|
| 62 | 94 | `∑ j ∈ range ... <` (52 chars without indent) | 94+1+52=147>100 | ok |
| 63 | 56 | `lam⁻¹ * ... * (r+1)` (47 chars, excluding `:= by`) | 56+1+47=104>100 | ok |
| 64 | 59 | proof follows | n/a | ok |

| Occurrence | Location | Orientation | Rewrite/rename |
|---|---|---|---|
| 1 | hr | `1 ≤ r` | none |
| 2 | hm | `2 ≤ m` | none |
| 3 | hlam | `2 * √(m:ℝ) < lam` | none |
| 4 | conclusion | reciprocal sum `<` product | none |
| 5 | body hm', hsq1, hlam2, hpos1, sqrt denominator | all `≤`/`<` | none |
| n/a | entire Lean signature | zero `≥`/`>` | no `_ge_`/`_gt_` name |

## Generalisation status: every binder

All substitutions were actually compiled in isolated copies of the original module prefix,
using `lake env lean /private/tmp/lattice_sum_<variant>.lean`; diagnostics retained in
adjacent `.lean.log` files. This avoids editing the protected live public API for probes.

| Binder | Class / use | Mechanical probes and outcome |
|---|---|---|
| `{r : ℕ}` | value, sum range and divisor | remove explicit binder: compiles because autoImplicit reinserts r with its inferred Nat type; not a generalization, retain explicit binder. Abstract indexing requires changed content/rational grid; no caller benefit |
| `{m : ℕ}` | value, sqrt comparison | remove explicit binder: fails because inference chooses real m and `sqrt_one_sub_inv_lt` requires Nat; Nat type is load-bearing. No universe/typeclass weakening for a fixed Nat value |
| `hr : 1 ≤ r` | proposition, passed to sum_inv_le | drop: unknown hr at application; weaken `0 ≤ r`: fails expected `1 ≤ r`. Retain |
| `hm : 2 ≤ m` | proposition, cast and sqrt bound | drop: unknown hm; weaken `1 ≤ m`: cast and sqrt_one_sub_inv_lt reject it. Retain; no point/global variants apply |
| `{lam : ℝ}` | value, real sqrt/division | remove explicit binder: autoImplicit reinserts real lam; no generality gained. Arbitrary ordered field cannot express this Real.sqrt directly; restatement closed without caller benefit |
| `hlam : 2 * √(m:ℝ) < lam` | proposition, strict sqrt comparison | drop: threshold derivation fails and unknown hlam; strict→weak `≤`: sqrt_one_sub_inv_lt requires `<`. No live API alteration |

Inversion check: the sum is handled by sum_inv_le, then a concrete real sqrt/rational
comparison. This suggests abstract composition of a sum bound and positive denominator
comparison, but both components already have APIs and an additional wrapper has no current
caller benefit. No new abstract theorem proposed. The previously rejected sqrt-generalization
is not reopened. No typeclass, universe, global continuity, or bundled hypothesis is present.

## All 42 golfing rules

| Rule | Result |
|---|---|
| 1.1 by exact | n/a: none |
| 1.2 by rfl | n/a: none |
| 1.3 rw+exact→rwa | n/a: no closing exact immediately after a single compatible rewrite; bound step needs gcongr |
| 1.4 simp+exact→simpa | n/a: no simp |
| 1.5 trailing rfl | n/a: none |
| 1.6 anonymous constructor | n/a: no constructors |
| 1.7 apply+exact | n/a: no apply |
| 1.8 by_contra! | n/a: no contradiction block |
| 1.9 eta-reduce | n/a: no lambdas |
| 1.10 single-use have | applied: inline hsq1; retained proof-bearing sqrt/rational haves; final hpos1 has outer by |
| 1.11 refine+fun | n/a: no apply/intro |
| 1.12 redundant show | n/a: none |
| 1.13 obtain projections | n/a: no projected conjunction/existential have |
| 1.14 merge rw | n/a: no sequential rewrites without intervening work |
| 1.15 terminal simp | n/a: no simp only |
| 1.16 nonterminal simp | n/a: no bare simp |
| 1.17 dot notation | existing Real API calls appropriate; no useful conversion |
| 1.18 trailing parentheses | n/a: all remaining parentheses delimit necessary tactic arguments / explicit identities |
| 1.19 push Not | n/a: no push_neg |
| 1.20 trivial exists helper | n/a: no such helper |
| 2.1 grind whole proof | actually tried live; fails on reciprocal/sqrt comparison |
| 2.2 delete before grind | tried grind on positivity subgoal in isolation; fails; no grind retained |
| 2.3 simpa consolidation | n/a: no simp+closing chain |
| 2.4 fun_prop | n/a: no function-property goals |
| 2.5 positivity | actual live radicand probe fails at `0 < 1-1/m`; keep rewrite/arithmetic positivity proof; final gcongr discharges structural positivity |
| 2.6 gcongr | actual independent candidate compiles, applied to strict product/division comparison |
| 2.7 lia/omega | n/a: no Nat/Int arithmetic tactic goals; inequalities needing automation are Real |
| 2.8 aesop | actual whole-goal attempt fails, no progress |
| 2.9 norm_num/norm_cast | actual isolated `example {m : ℕ} (hm : 2 ≤ m) : (2 : ℝ) ≤ m := by norm_cast` compiles cleanly; retain equally short exact_mod_cast hm for explicit evidence. Initial live probe targeted outer goal and was discarded |
| 2.10 decide/kernel | n/a: variable real analytic inequality, not a closed decidable computation |
| 2.11 field_simp+ring | actual live rational-identity probe: field_simp closes; appended ring emits unreachable/unused warnings, so retain field_simp alone |
| 2.12 linear_combination | no ring-ending proof requiring hypotheses; extra sqrt-identity probe fails because square root is not polynomial |
| 2.13 wlog | n/a: no symmetric case branches |
| 2.14 collapse calc | n/a: three heterogeneous steps (weak bound, strict bound, normalization), not two composable direct terms |
| 2.15 <;> | n/a: no similar branch goals remaining |
| 3.1 erw→rw | n/a: no erw |
| 3.2 continuity | n/a: no legacy continuity or measurability |
| 3.3 omega→lia | n/a: no omega |
| 3.4 rcases rfl | n/a: no rcases |
| 3.5 automation attributes | none: specialized quantitative upper bound does not define a useful simp normal form |
| 3.6 simp_all | actual live radicand simp_all attempt does not finish reciprocal comparison; none retained |
| 3.7 limits | none to remove; none added |

## Arithmetic and inequality evidence

| Block | Domain | Chosen proof and bounded alternatives |
|---|---|---|
| hm' | Nat→Real | exact_mod_cast hm directly transfers order; isolated norm_cast closes the same local fact, same proof length; retain explicit evidence |
| hlam2 | Real | linarith with inline lt_sqrt_of_sq_lt, isolated example compiled successfully |
| hpos1 | Real reciprocal/sqrt | rw sqrt_pos/sub_pos/div_lt_one, then linarith; positivity, grind, simp_all all failed on radicand goal |
| hsqrt | Real sqrt quotient | direct sqrt_div' with Nat.cast_nonneg, congr 1, field_simp; full replacement independently compiled. ring and linear_combination fail on sqrt identity |
| hlam' | Real rational identity | explicit nonzero fact + field_simp; ring alone fails, additional ring after field_simp is unused |
| strict calc step | Real order | gcongr followed by sqrt_one_sub_inv_lt; independent original-type candidate compiled |
| final equality | Real rational identity | rewrite typed hsqrt, field_simp; no polynomial follow-up needed |

Step-back reflection: full-goal grind/simp/aesop fail; exact? finds no complete direct
term. apply? only gives generic conversion/comparison shells. The existing structure
clearly separates the paired sum estimate, positive reciprocal comparison, and square-root
normalization. No additional helper or changed strategy improves current callers.

## Final checks and gates

Reference, actual `set_option format.width 100 in #check @Roth.sum_inv_lt`:

```lean
@Roth.sum_inv_lt : ∀ {r m : ℕ},
  1 ≤ r →
    2 ≤ m →
      ∀ {lam : ℝ},
        2 * √↑m < lam → ∑ j ∈ Finset.range (r + 1), (lam - 1 + 2 * ↑j / ↑r)⁻¹ < lam⁻¹ * (√(↑m - 1))⁻¹ * √↑m * (↑r + 1)
```

The pretty-printer may exceed width for its final unbreakable formatted expression;
source signature remains the measured three-line form above, maximum 94 codepoints.
The initial exploratory `pp.width` option was invalid; the actual successful check uses
`format.width`, and no option was written to source.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | `/Users/ramin/.elan/bin/lake build Roth.Lattice`, final build exit 0, 26s, 2214 jobs |
| definition_protected | pass | no def/abbrev changed or added |
| theorem_statement_protected | pass | literal original signature comparison succeeded |
| structure_gate | pass | body 20 lines (21 before), no conjunction or case branch; no helper added |
| naming_gate | pass | descriptive snake_case, zero forbidden patterns |
| line_packing_gate | pass | every signature line measured above; unchanged |
| inequality_orientation_gate | pass | occurrence table above, zero reversed code inequalities |
| documentation/scope | pass | exact file prefix/suffix equality proves docs and every byte outside target unchanged |
| complete LSP | pass | partial=false, timed_out=false, success=true; only preexisting header warning, zero target diagnostics |
| actual theorem trust | pass | lean_verify Roth.sum_inv_lt: standard, propext/Classical.choice/Quot.sound, no source warnings or nonstandard axioms |
| independent proof | pass | `/private/tmp/lattice_sum_gcongr.lean` compiled exit 0; module prefix excludes original target, fresh name, original exact type, copied final proof does not reference sum_inv_lt |
| independent trust | pass | compiled #print axioms of fresh theorem: standard three only |

Full project and separate LeanEval gates belong to the file owner after source freeze.
No git or shared progress changes performed.

Result: declaration 24→23 lines, body 21→20. Four changes: hsq1 inline, clearer
proof-bearing hpos1, direct cast-nonneg API, gcongr comparison. No helper, rename, API,
documentation, version, or header changes. Final target SHA256:
`7ab9ac33bf8b5440c2b63b6617538a415bdf9497d14f999192c9695d4961eb3d`.
Final file SHA256: `ee64506a923d08cf5a57871b5f670a67f6f4509e924c56feac07e27909366d42`.

## Required eleven-item phase checklist

- [x] Step 1: required reference documents read.
- [x] Step 2: all 24 audit items recorded.
- [x] Step 2.5: five actual search methods and partial-match status recorded.
- [x] Step 2.6: every parameter/drop/weakening and public literature recorded.
- [x] Step 2.7: per-line codepoint packing table and actual width-100 #check.
- [x] Step 2.8: occurrence inequality scan table.
- [x] Step 3: all 42 golf rules given a concrete status.
- [x] Step 4: whole-proof/reflection alternatives considered and probed.
- [x] Step 5a: complete LSP green, zero target diagnostics.
- [x] Step 5b: all declaration diff gates passed, actual module build exit 0.
- [x] Step 6a: no renames needed; no queue mutation.

Owner checkpoint: explicit source-ownership revocation at above frozen hash before sequential full/separate LeanEval session36147; both exit0 (108.79s/34.18s), hash stable. Logs `/private/tmp/roth-lattice-d04-{full,leaneval}.log`.
