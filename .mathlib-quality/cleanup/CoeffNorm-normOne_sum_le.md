# Phase 4 — Roth.normOne_sum_le

Dedicated single-declaration audit, `Roth/CoeffNorm.lean:85–87`, on the parent-provided
`ramin-cleanup` / `2647a56` baseline. Only this report was written; source unchanged.
Baseline full build and separate LeanEval session 54826 exited 0 per parent handoff.
No additional full build was run by this worker.

SOURCE FROZEN: whole-file SHA256
`12422f3bbb5a494633eede6148bc384c1c3eff739be1aa3c00181dabea5d7423`.
Parent explicitly revoked source ownership at this hash. All subsequent work was verification
and reporting. `cmp` and `diff -u` against `/private/tmp/coeffnorm-sum-before.lean` show no diff.

## Step 1 — references

Read both full skills (`mathlib-quality/SKILL.md`, `lean4/SKILL.md`), the full 853-line
`/private/tmp/roth-coeffnorm-worker-contract.md`, and full reference files:
`golfing-rules.md`, `proof-patterns.md`, `mathlib-search.md`,
`generalisation-patterns.md`, `cleanup-gates.md`, `style-rules.md`,
`naming-conventions.md`, and `mathlib-review-stages.md`. Initial combined reads truncated;
subsequent range reads covered the omitted portions. No applicable repository AGENTS.md found.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md.

## Mathematical meaning

The coefficient ℓ¹ size of a finite sum of integer multivariate polynomials is bounded by the
sum of their coefficient ℓ¹ sizes. Binary subadditivity plus the zero value gives the result
for an arbitrary finite index set. The proof is precisely the generic mathlib finite-sum
subadditivity theorem specialized to `normOne`.

## Step 2 — full audit

| Item | Finding and action |
|---|---|
| 1 LINT | No target warning. Complete native diagnostics: no errors, six existing warnings outside target. |
| 2 HAVE SCAN | No `have` or local binding; nothing to inline. |
| 3 SET_OPTION | No declaration option or raised limit. |
| 4 SIMP SQUEEZE | No simp in retained proof; alternatives using `by simp` fail. |
| 5 NAMING | `normOne_sum_le` describes the named norm, sum, and inequality; no forbidden patterns or abbreviations. No rename. |
| 6 LINE PACKING | Signature widths 78,54; complete conclusion cannot share first line (129). Full table below. |
| 7 BY PLACEMENT | Term mode; no redundant `by`. |
| 8 FORMAT | Two-space term indentation; no empty body lines, semicolons, haveI/letI, trailing space. |
| 9 COMMENTS | No inline proof comments; existing docstring preserved verbatim. |
| 10 DOCSTRING | Existing one-sentence finite triangle inequality docstring preserved under Lean Rule A. |
| 11 VISIBILITY | Public reusable coefficient-norm API, used by subsequent multiplication and determinant estimates; visibility preserved. |
| 12 STRUCTURE | One proof-body line; no conjunction, branches, or extraction signal. |
| 13 MATHLIB | Exact abstract result `Finset.le_sum_of_subadditive` already used. Five-method evidence below. Public deletion is outside authorized signature-preserving scope. |
| 14 JUNK DEF | n/a: theorem, not definition. |
| 15 EXISTS LEMMA | n/a: not an existential lemma. |
| 16 SHOW vs CHANGE | n/a: neither occurs. |
| 17 PUSH_NEG | n/a: no negation tactic. |
| 18 GENERALISE | Every parameter analyzed below; no unused hypothesis or class; abstract generalization already exists in mathlib. |
| 19 INEQUALITY | Sole relation is `≤`; no reversed relation or `_ge_`/`_gt_` name. |
| 20 NORMAL-FORM | Standard finite-sum triangle inequality in smaller-to-larger order. No equivalence graph or restatement needed. |
| 21 SYNTAX-GEN | Explicit `s f` matches existing call sites; currying proposal compiles but changing signature is unnecessary. |
| 22 IMPORT-FANOUT | n/a: no imports added. |
| 23 CASTS | 0 dropped / 0 cross-type / 0 load-bearing casts in diff (empty). |
| 24 INSTANCE-NAME | n/a: theorem, no instance declaration. |

Issues to fix: none within authorized source scope. Refactoring needed: optional public wrapper
deletion and migration to `Finset.le_sum_of_subadditive` is a Phase 5 API decision, not applied.
There are no correctness, naming, packing, structure, or inequality deferrals.

## Step 2.5 — mathlib search-status

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | `subadditive function of a finite sum is at most the sum of its values` | `Finset.le_sum_of_subadditive`, nonempty variant, List nonempty variant. |
| B Loogle | `Finset, (?f (?a + ?b) ≤ ?f ?a + ?f ?b) → _` | Three irrelevant pointwise/interval results; no useful hit from this query. |
| C LeanSearch | `A subadditive map bounded by zero at zero is bounded on a finite sum by sum of values` | Exact generic result; Multiset and Finset `_on_pred` variants. |
| D source rg | `le_sum_of_subadditive|sum_le_of_subadditive|norm_sum_le` under Algebra/Order/BigOperators | Finset Group file L95–103 generated additive theorem; applications L366 and Ring/Finset L201; List/Multiset alternatives. |
| E local name | `le_sum_of_subadditive`, `le_sum_nonempty_of_subadditive` | Finset/List/Multiset and predicate variants found; index `warming`, so no absence inference. |

The guessed Analysis/Normed/Group/Finset path was absent; source search still found the
actual generic Group/Finset file, which was inspected directly. Native hover at L87:3 and
compiled `#check @Finset.le_sum_of_subadditive` verified the pinned version uses `Preorder`,
weaker than the remote search index's `PartialOrder`.

Auxiliary variants: nonempty sums, `_on_pred`, List, Multiset, absolute-value finite sums.
Common-equivalents lookup: no discrete/finiteness/separation/bornology bucket applies;
the direct subadditivity API is the relevant canonical abstraction.

Conclusion: found a more general mathlib theorem, already used directly in the proof.
Rule 1/5 wrapper deletion is a scoped public-API proposal only because the task explicitly
preserves all public signatures. No new wrapper created. Rule 2 presence established, so
no claim of absence or absence probe is required. Rule 3 variants checked. Rule 4 no custom
predicate to replace. Rule 6 dependency recorded here; existing module docstring is API and
outside ownership, so no unauthorized documentation edit.

## Step 2.6 — mechanical generalisation

| # | Parameter | Class | Used as | Mechanical candidate / reason | Verification | Result |
|---|---|---|---|---|---|---|
| 1 | `{σ : Type*}` | type variable | Polynomial exponent domain | Already arbitrary universe; dropping leaves polynomial domain unbound. No class parents or point/strict assumptions exist. | Width100 `#check` shows independent `u_1`. | Keep. |
| 2 | `{ι : Type*}` | type variable | Finite sum index type | Already arbitrary universe; dropping leaves `s`, `f` unbound. No decidability/finiteness class present. | Width100 `#check` shows independent `u_2`. | Keep. |
| 3 | `(s : Finset ι)` | structure value | Index set on both sides; final generic theorem argument | Drop cannot preserve dependent statement; compiled curry-to-`∀ s` alternative exposes equivalent abstract form. No pointwise or strict weakening applies to a data argument. | Native run-code success for fully curried proposal. | Public signature preserved. |
| 4 | `(f : ι → MvPolynomial σ ℤ)` | function value | Summands on both sides; generic theorem argument | Drop cannot preserve statement; compiled `∀ f` currying alternative. No global function-property hypothesis to localize. | Native run-code success for fully curried proposal. | Keep explicit argument. |

No proposition, typeclass, or decidability parameter was omitted from the inventory. There
is no applicable hypothesis drop, parent-class weakening, strict-to-weak, or point-localization
probe: there are no such hypotheses. The applicable independent-universe and currying probes
were compiled, rather than relying on inspection alone.

Inversion check: fires immediately — the entire proof is abstract after supplying `normOne`
and its zero/subadditivity laws. The general theorem already exists, so no extra helper/API
is justified. A compiled alternative with inferred `_` map succeeds but conceals useful
information; retained explicit `normOne`. A `by simp` zero-law argument also succeeds but is
longer and less direct than `normOne_zero.le`. No API weakening is applied.

## Literature search status

Web searches executed (top three returned hits retained for each query):

1. `finite sum triangle inequality subadditive function generalization`:
   [Geometrical criterions of generalized subadditivity](https://www.sciencedirect.com/science/article/abs/pii/S0022247X24008618),
   [generalized triangle inequality question](https://math.stackexchange.com/questions/5028610/how-can-i-define-a-generalized-triangle-inequality-for-arbitrary-binary-operat),
   [Metamath fsumabs](https://metamath.tirix.org/mpeuni/fsumabs).
2. `site.ncatlab.org subadditive function triangle inequality`:
   [triangle inequality](https://ncatlab.org/nlab/show/triangle%20inequality),
   [inequality](https://ncatlab.org/nlab/show/inequality),
   [metric space](https://ncatlab.org/nlab/show/metric%2Bspace).
3. `site.en.wikipedia.org triangle inequality finite sums norm`:
   [Triangle inequality](https://en.wikipedia.org/wiki/Triangle_inequality),
   [Normed vector space](https://en.wikipedia.org/wiki/Normed_vector_space),
   [Dual norm](https://en.wikipedia.org/wiki/Dual_norm).

These discovery results place the theorem in the usual finite triangle/subadditivity
setting. The Metamath open returned an internal error; it is not treated as verified text.
No mathematical claim depends on the StackExchange or encyclopedia snippets: the primary
pinned mathlib source and compiled theorem establish the full generality. Primary local
reference `clean.tex:450–452` states the coefficient ℓ¹ triangle inequality; arbitrary finite
families follow by induction, independently verified below. ChatGPT mathematics MCP:
n/a, no callable mathematical second-opinion tool is exposed.

Literature-driven big change: the generic subadditive-map statement applies to additive
commutative monoids and ordered additive codomain, without integer coefficients or real
values. Already supplied by mathlib; optional wrapper deletion only. No new restatement.

## Step 2.7 — line packing

Actual native run-code output with `set_option format.width 100`:

```lean
@normOne_sum_le : ∀ {σ : Type u_1} {ι : Type u_2} (s : Finset ι) (f : ι → MvPolynomial σ ℤ),
  normOne (∑ i ∈ s, f i) ≤ ∑ i ∈ s, normOne (f i)
```

| Signature line | Codepoints | Next complete syntactic token | Arithmetic | Action |
|---|---:|---|---|---|
| 85 | 78 | complete conclusion and assignment, 50 chars excluding indentation | 78 + 1 + 50 = 129 > 100 | ok |
| 86 | 54 | no next signature line; term proof follows | n/a | ok |

The conclusion is one complete relation; do not break inside it merely to move its first
identifier to the preceding colon line. Body L87 is 73 codepoints, already one line.

## Step 2.8 — inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 1 | Statement L86 | `normOne (∑ i ∈ s, f i) ≤ ∑ i ∈ s, normOne (f i)` | None: correct orientation | None |
| — | Entire signature and hypotheses | n/a — zero `≥` or `>` | None | No `_ge_` or `_gt_` |

## Step 3 — all 42 golfing rules

| Rule | Status |
|---|---|
| 1.1 by-exact wrapper | n/a: already a direct term. |
| 1.2 by-rfl | n/a: no reflexivity wrapper. |
| 1.3 rw + exact | n/a: no rewrites. |
| 1.4 simp + exact | n/a: no simplification chain. |
| 1.5 trailing rfl | n/a: no rfl. |
| 1.6 anonymous constructor | n/a: no product/constructor goal. |
| 1.7 apply + exact | n/a: already direct application. |
| 1.8 by_contra! | n/a: no contradiction proof. |
| 1.9 eta reduction | n/a: no lambda. |
| 1.10 inline have | n/a: no have. |
| 1.11 refine + fun | n/a: no apply/intro chain. |
| 1.12 redundant show | n/a: no show. |
| 1.13 obtain | n/a: no projected hypothesis. |
| 1.14 merge rw | n/a: no rw. |
| 1.15 unsqueeze terminal simp | n/a: no simp only. |
| 1.16 squeeze nonterminal simp | n/a: no simp. |
| 1.17 dot notation | Already `normOne_zero.le`; generic theorem namespace required for discoverability. |
| 1.18 reverse application | n/a: no trailing-parentheses argument in retained term. |
| 1.19 push Not | n/a: no push_neg. |
| 1.20 existential inline | n/a: no existential. |
| 2.1 whole grind | Native term replacement `by grind` tried; fails with negated inequality/False goal. |
| 2.2 delete before grind | n/a: no grind retained or preceding tactics. |
| 2.3 simpa consolidation | Compiled alternative `by simp` zero-law proof works but is longer; no simp/exact chain to consolidate. |
| 2.4 fun_prop | n/a: no continuity/differentiability/measurability goal. |
| 2.5 positivity | n/a: comparison of two arbitrary sums, not positivity goal. |
| 2.6 gcongr | Native `by gcongr` tried; no progress. |
| 2.7 lia / omega | n/a: real coefficient norms over arbitrary finite index set, not Nat/Int arithmetic. |
| 2.8 aesop | Native `by aesop` tried; no progress. |
| 2.9 norm_num / norm_cast | n/a: no numerical computation or cast goal. |
| 2.10 decide / +kernel | n/a: arbitrary noncomputable real comparison, no closed finite computation. |
| 2.11 field_simp; ring | n/a: no denominator identity. |
| 2.12 linear_combination | n/a: no ring-ending proof or algebraic hypotheses. |
| 2.13 wlog | n/a: no symmetric case branches. |
| 2.14 calc collapse | n/a: already one term, no calc. |
| 2.15 <;> | n/a: retained proof has no subgoals. |
| 3.1 erw → rw | n/a: no erw. |
| 3.2 fun_prop migration | n/a: no legacy function-property tactic. |
| 3.3 omega → lia | n/a: no omega. |
| 3.4 rcases rfl | n/a: no rcases. |
| 3.5 attributes | n/a: one inequality does not provide a simp normal form; no demonstrated repeated automation requirement. |
| 3.6 simp_all | n/a: no simp_all. |
| 3.7 maxHeartbeats | n/a: no raised limit. |

## Step 4 — reflection and actual probes

Native `lean_term_goal` at L87:3 returned the exact expected inequality and all four
parameters. Initial unwrapped tactic snippets were rejected as term identifiers; reran each
with `by`, so those first errors were not mistaken for tactic results. `by simp` makes no
progress; `by grind`, `by aesop`, and `by gcongr` fail; `by exact?` cannot close the goal.
`by apply?` offers the existing subadditivity lemma with its zero and binary laws remaining
(plus predicate/nonempty variants); it is not a complete proof and was not installed.
Temporary sorry diagnostics emitted by search experiments never entered source.

Actual native run-code successful batch: original-type assignment, independent Finset induction
reproof, `_` map inference alternative, `by simp` zero-law alternative, and fully curried
generic theorem application. The first induction trial used the wrong positional-addition
lemma (`add_le_add_left`); corrected to `add_le_add_right`, reran successfully. No source edit.
The independent proof uses only `normOne_add_le`, finite-sum rewriting, and induction,
never `normOne_sum_le` itself. Term mode is shorter and directly exposes its two premises.
There are no haves to compose, redundant tactics, or missing API. Keep current proof.

## Step 5 — gates

`/Users/ramin/.elan/bin/lake build Roth.CoeffNorm`, session 73402: exit 0,
`Build completed successfully (1658 jobs)`. Replayed six existing CoeffNorm warnings,
and dependency header warnings only. Final complete native diagnostics:
`partial=false`, `timed_out=false`, `success=true`, no errors/failed dependencies,
six unchanged warnings (header; DecidableEq in mul/prod/det/abs_coeff_det; hC).
No warnings at L85–87. No suppression added.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | ✓ pass | Actual module command above exited 0. |
| definition_protected | ✓ pass | Empty worker source diff. |
| theorem_statement_protected | ✓ pass | Entire file byte-identical; original-type assignment compiles. |
| structure_gate | ✓ pass | One-line proof, no conjunction or branch. |
| naming_gate | ✓ pass | Descriptive name; no forbidden pattern/abbreviation. |
| line_packing_gate | ✓ pass | Both signature lines measured above; no repack row. |
| inequality_orientation_gate | ✓ pass | Complete scan above, no reversed relation. |
| no_unintended_breakage | ✓ pass | No source or signature changes; module elaborates completely. |

Overall: pass. No source edits, no new axiom, sorry, suppression, import or option change.
Fresh CLI probe `/private/tmp/coeffnorm-sum-final.lean` additionally checks width100 types,
original-type assignment, independent named reproof and axiom lists (result recorded below).

Fresh CLI probe command `/Users/ramin/.elan/bin/lake env lean
/private/tmp/coeffnorm-sum-final.lean`, session 62550: exit 0. Both
`Roth.normOne_sum_le` and the independent induction theorem `independentSum` depend only on
`[propext, Classical.choice, Quot.sound]`. All alternative successful examples in the batch
also compile. Final whole-file SHA256 rechecked and equals the frozen hash above.

## Step 6 — result

Before: 3 declaration lines / 1 proof line. After: 3 / 1. Saved: 0.
Rules applied: none; existing direct term retained after applicable alternatives.
Renames queued: none. Comments preserved: existing docstring byte-identical, no proof comments.
Pending scoped public API decision: optional removal of this specialized wrapper and migration
of consumers; explicit preserve-signatures instruction prevents it here. No other refactoring.

- [✓] Step 1 — full reference documents read.
- [✓] Step 2 — all 24 audit items recorded.
- [✓] Step 2.5 — all five mathlib search methods and strict-rule decisions recorded.
- [✓] Step 2.6 — every parameter analyzed; applicable proposals compiled; literature recorded.
- [✓] Step 2.7 — width100 #check and every signature-line width recorded.
- [✓] Step 2.8 — complete inequality scan recorded.
- [✓] Step 3 — all 42 golfing rules have explicit status.
- [✓] Step 4 — reflection and alternative proof attempts completed.
- [✓] Step 5a — complete native LSP diagnostics clean of errors.
- [✓] Step 5b — actual module build and all diff gates pass.
- [✓] Step 6a — no rename required; shared sidecars untouched.
