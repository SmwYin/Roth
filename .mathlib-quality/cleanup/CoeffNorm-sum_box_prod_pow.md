# Phase 4: `Roth.sum_box_prod_pow` (original audit 23)

Dedicated declaration owner; original `Roth/CoeffNorm.lean` lines 208–211, four lines.
Scope includes the minimal sole-caller replacement in `abs_eval_le`, explicitly authorized.
No Git operation, shared log, other source, public statement, definition, import, or docstring
was edited. Baseline full build and separate `Roth.LeanEval` build (session 84781, exit 0)
were inherited from the file owner, as instructed; neither was repeated by this worker.

## Result

Deleted the private wrapper. At the sole caller, replaced
`rw [← Finset.mul_sum, sum_box_prod_pow]` with
`simp [← Finset.mul_sum, box, Finset.prod_univ_sum]`.
The finite distributive identity is already `Finset.prod_univ_sum`; `box` is a mapped
`Fintype.piFinset`, and simp handles `Finset.sum_map` and the function/finsupp equivalence.
Four declaration lines plus one blank separator removed; caller remains one tactic line.
Issues found: one redundant wrapper; fixed: one; deferred: zero. Renames: none.
Comments present in target: zero. All caller documentation preserved verbatim.

SOURCE FROZEN, source ownership revoked: whole-file SHA256
`15d3ac71121de58374fd6d7bce63a35c7a25e81b1bf4bae306a12a3809277a5b`.
No source edits after this hash. Report/probes/verification only thereafter.

## References read

Read both complete `mathlib-quality/SKILL.md` and `lean4/SKILL.md`, the complete worker
contract `/private/tmp/roth-coeffnorm-worker-contract.md`, and complete reference files:
`golfing-rules.md`, `proof-patterns.md`, `mathlib-search.md`,
`generalisation-patterns.md`, `cleanup-gates.md`, `style-rules.md`,
`naming-conventions.md`, `mathlib-review-stages.md`, `mathlib-quality-principles.md`,
and `pr-feedback-examples.md`. Long reads were split into contiguous ranges to prevent
truncation. The governing narrow authorization overrides generic header/doc rewrite rules.

## Full 24-item audit

| # | Item | Finding/action |
|---|---|---|
| 1 | LINT | No target warning. Six baseline warnings elsewhere preserved: header, four public DecidableEq arguments, unused hC. Final complete LSP confirms unchanged warning content. |
| 2 | HAVE SCAN | No `have` in target; no new `have` at caller. |
| 3 | SET_OPTION | No local options or resource-limit changes. |
| 4 | SIMP SQUEEZE | Original target used rw/rfl; replacement terminal simp closes the equality. Leave terminal simp unsqueezed. |
| 5 | NAMING | Descriptive snake_case, no forbidden abbreviation or numeric pattern. Declaration removed, no rename necessary. |
| 6 | LINE PACKING | Two historical signature lines and three caller signature lines measured below; no signature edited. Removed declaration has no final signature to repack. |
| 7 | BY PLACEMENT | Original and caller `by` occur at end of preceding line. |
| 8 | FORMAT | Original two-space proof indentation; existing calc indentation preserved. No empty declaration lines, semicolon chains, haveI, or letI added. |
| 9 | COMMENTS | None in removed target; no comment removed from caller. |
| 10 | DOCSTRING | n/a private helper had none; existing public caller docstring protected and unchanged. |
| 11 | VISIBILITY | Private helper, one caller, deleted. No public visibility change. |
| 12 | STRUCTURE | Original two proof lines, no conjunction or branch; caller equality is now one terminal simp. No extraction warranted. |
| 13 | MATHLIB | Five-method search below; use existing generic identity directly, delete wrapper. |
| 14 | JUNK DEF | n/a target is a proposition-valued lemma. |
| 15 | EXISTS LEMMA | n/a equality, not an existential witness wrapper. |
| 16 | SHOW vs CHANGE | Neither present in target or new proof. |
| 17 | PUSH_NEG | None present. |
| 18 | GENERALISE | Every parameter mechanically analyzed and actual drop probes run below. No new generalization retained because wrapper removed. |
| 19 | INEQUALITY | No ≥ or > in target signature; table below. |
| 20 | NORMAL-FORM | Finite product/sum distributivity is canonical `Finset.prod_univ_sum`; no new equivalent form exported. |
| 21 | SYNTAX-GEN | Direct simp at sole call eliminates wrapper instantiation; public caller surface unchanged. |
| 22 | IMPORT-FANOUT | n/a no new import. Existing imports provide all required API. |
| 23 | CASTS | 0 dropped / 0 kept as cross-type / 0 kept as load-bearing in added code. No ascription or coercion added. |
| 24 | INSTANCE-NAME | n/a no instance declaration in target or diff. |

Refactoring needed: none. Private wrapper deletion and its sole caller adjustment completed.

## Mathlib search-status

| Method | Actual query/search | Result |
|---|---|---|
| A Lean-Finder | `finite product of sums equals sum over functions of products` | `Fintype.prod_sum`, `Finset.prod_sum`, `Finset.prod_univ_sum` |
| B Loogle | `Finset.prod, Finset.sum` | Broad hits `ofAdd_sum`, `ofMul_prod`, `toAdd_prod`, `toMul_sum`; these are not the needed factorization. |
| C LeanSearch | `product of finite sums equals sum of products over piFinset` | `Finset.prod_univ_sum`, `Finset.sum_prod_piFinset`, `Fintype.prod_sum` |
| D source rg | Untruncated `prod_univ_sum`, `sum_pi`, `sum_map` in big-operator/Finsupp sources | Read Ring/Finset.lean 115–170: generic prod_sum, prod_univ_sum, constant-fiber sum_prod_piFinset. Read actual box definition. |
| E local names | `prod_univ_sum` | Positive source hit `Finset.prod_univ_sum`; index warming, so no absence claim made. |

Auxiliary variants: `prod_sum` (arbitrary finset), `prod_univ_sum` (univ),
`sum_prod_piFinset` (constant fibers), `Fintype.prod_sum` (finite types), `Finset.sum_map`.
Common-equivalents table: no listed bucket applies (finite distributivity, not topology).
Conclusion: existing generic Mathlib identity, specialized via `box` and sum-map simplification;
ACTION completed: delete private wrapper, update one call site directly.
Six strict rules: (1) no wrapper retained; (2) all five methods attempted, presence established;
(3) auxiliary variants inspected; (4) no custom predicate introduced;
(5) local copy deleted; (6) direct Mathlib dependency recorded here, since module docstring
edits are outside authorized scope. No claim that Mathlib lacks this result.

## Generalisation status (every parameter)

All drop probes used `autoImplicit false` so Lean could not silently reintroduce a missing
binder. Native `lean_run_code` compiled isolated versions importing `Roth.Box`.
Failed probes were not applied to live source; no temporary broken source was published.

| # | Parameter | Class / use | Mechanical candidates actually tested or inapplicable | Verified? | Result |
|---|---|---|---|---|---|
| 1 | `{σ : Type*}` | Type variable, index of box/products | Drop binder; universe polymorphism already present; no further universe widening available. | yes | Drop yields unknown σ. Width-100 #check confirms original arbitrary universe. |
| 2 | `[Fintype σ]` | Typeclass, constructs box/univ product | Drop; replace by `[Finite σ]`. Other algebra/topology parents n/a for this class. | yes | Both fail to synthesize `Fintype σ` in statement. No valid weakening retained. |
| 3 | `[DecidableEq σ]` | Decidability required by `box` surface | Drop. No parent class; point localization/strict weakening n/a to decidability. | yes | Statement fails `DecidableEq σ` at box. Caller already has local classical, and wrapper removed. |
| 4 | `(r : σ → ℕ)` | Structure value, defines bound and ranges | Drop; point localization n/a as no assumed property of r; strict weakening n/a as no inequality hypothesis. | yes | Unknown r under autoImplicit false. |
| 5 | `(y : σ → ℝ)` | Structure value, bases in summand and factors | Drop; point localization n/a as no assumed property of y; no strict/weak property to change. | yes | Unknown y under autoImplicit false. |

Concrete-to-abstract check: generic `Finset.prod_univ_sum` already works in a `CommSemiring R`;
removing the wrapper uses that general API instead of creating a new generalized project lemma.
Inversion check: fires after unfolding box; all remaining work is generic finite distributivity.
Resolved by direct existing API, not by another abstraction layer.
Big-change candidates: none needing a new declaration or approval after deletion.

Literature search: n/a: private decl, literature search not required.
WebSearch and ChatGPT mathematical literature search are both exempt for this private helper.

## Line packing

Native `lean_run_code`, with `set_option format.width 100`, produced:

```lean
@d23_original : ∀ {σ : Type u_2} [inst : Fintype σ] [inst_1 : DecidableEq σ] (r : σ → ℕ) (y : σ → ℝ),
  ∑ k ∈ box r, ∏ j, y j ^ k j = ∏ j, ∑ s ∈ Finset.range (r j + 1), y j ^ s
```

`d23_original` independently repeats the original mathematical type because the private
declaration is removed. `format.width`, not `pp.width`, is the valid option on this toolchain;
an initial pp.width probe failed and was corrected and recompiled successfully.

| Signature line | Codepoints | Next semantic signature token | Arithmetic | Action |
|---|---:|---|---|---|
| Original 208 | 84 | left sum `∑ k ∈ box r, ∏ j, y j ^ k j` (27) | 84 + 1 + 27 = 112, exceeds 100 | ok (historical; now removed) |
| Original 209 | 82 | no next signature line | n/a | ok (historical; now removed) |
| Final caller 211 | 97 | `{B : ℝ}` (7) | 97 + 1 + 7 = 105, exceeds 100 | ok |
| Final caller 212 | 65 | conclusion through `:= by` (71) | 65 + 1 + 71 = 137, exceeds 100 | ok |
| Final caller 213 | 75 | no next signature line | n/a | ok |

No final target signature remains. Replacement tactic at final line 235 is 58 codepoints.
All widths computed using Python `len` on Unicode strings, not UTF-8 byte counts.

## Inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 1 | Original target signature and all parameters | n/a: no ≥ or > | none | none |
| 2 | Added caller code | n/a: no inequality, only simp invocation | none | none |

Caller original conclusion uses ≤ and was not changed. Original target name has no `_ge_`/`_gt_`.

## All 42 golfing rules

| Rule | Status |
|---|---|
| 1.1 by exact | n/a no by-exact wrapper. |
| 1.2 by rfl | n/a no whole-proof by-rfl; original trailing rfl removed with helper. |
| 1.3 rw + exact | n/a no exact following rewrite. |
| 1.4 simp + exact | n/a no such chain. |
| 1.5 trailing rfl | Applied broadly: terminal simp replaces rw/rfl identity at point of use. |
| 1.6 constructor | n/a equality, no constructor pair. |
| 1.7 apply + exact | n/a absent. |
| 1.8 by_contra! | n/a no contradiction argument. |
| 1.9 eta reduction | n/a original target has no lambda. |
| 1.10 single-use have | n/a no have. |
| 1.11 refine + fun | n/a no apply/intro chain. |
| 1.12 redundant show | n/a no show. |
| 1.13 obtain | n/a no projections from have. |
| 1.14 merged rw | Original already has one merged rw; superseded by direct simp. |
| 1.15 terminal simp | New terminal simp left unsqueezed. |
| 1.16 nonterminal simp | n/a no added nonterminal simp. |
| 1.17 dot notation | n/a no applicable receiver in added simp list. |
| 1.18 <\| | n/a no trailing-parenthesized function argument. |
| 1.19 push Not | n/a no push_neg. |
| 1.20 existential | n/a equality, not witness existence. |
| 2.1 grind | Actual native multi-attempt failed: negation of identity remains, cannot prove False. |
| 2.2 before grind | n/a no original grind chain. |
| 2.3 simpa | Actual explicit prod_univ_sum.symm simpa closes identity; longer than direct simp. |
| 2.4 fun_prop | n/a no continuity/differentiability/measurability goal. |
| 2.5 positivity | n/a target is an identity, no positivity subgoal. |
| 2.6 gcongr | n/a target has no inequality/monotonicity step. |
| 2.7 lia/omega | n/a symbolic finite distributivity, no linear arithmetic subgoal. |
| 2.8 aesop | Actual native multi-attempt failed, made no progress on identity. |
| 2.9 norm_num/norm_cast | n/a no concrete numeric or cast reduction subgoal. |
| 2.10 decide | n/a arbitrary symbolic real equality, not closed finite computation. |
| 2.11 field_simp/ring | n/a no denominators or polynomial-normalization goal; distributivity indexed by variable finite sets. |
| 2.12 linear_combination | n/a no ring/ring_nf ending and no algebraic hypotheses. |
| 2.13 wlog | n/a no symmetric case split. |
| 2.14 calc to term | n/a target has no calc; only authorized caller equality leaf changed. |
| 2.15 <;> | n/a one equality goal, no parallel subgoals. |
| 3.1 erw | n/a absent. |
| 3.2 fun_prop upgrade | n/a no legacy continuity/measurability. |
| 3.3 omega to lia | n/a no arithmetic tactic in original or diff. |
| 3.4 rcases rfl | n/a no case splitting. |
| 3.5 attributes | n/a wrapper deleted; no new automation declaration to register. |
| 3.6 simp_all | n/a no simp_all only or useful propositional hypotheses. |
| 3.7 heartbeat option | n/a no maxHeartbeats or maxRecDepth setting. |

## Step-back reflection and tested alternatives

Native live multi-attempt at original line 210 tested `grind`, `aesop`, `exact?`, `apply?`,
`simp [box, Finset.prod_univ_sum]`, and an explicit `simpa ... using ... .symm`.
Grind/aesop/exact? failed; apply? offered Real.ext_cauchy plumbing, not a useful shortcut.
Simp and explicit simpa closed the first goal and then reported `No goals to be solved`
on the original following rfl: this was evidence to remove that rfl, not evidence of a
final clean file. The independent whole-statement reproof later compiled cleanly.
Live caller multi-attempt at original line 240 showed the chosen terminal simp closes
with no diagnostic. A multiline rw/rfl alternative suffered indentation in the replacement
mechanism and was rejected; it is not counted as a successful candidate.
Term mode with explicit prod_univ_sum specialization is longer; no have blocks exist to fold.
Mathematically the proof is finite distributivity under an equivalence. Direct Mathlib use
is simpler than maintaining either original or golfed wrapper. No new API gap remains.

## Actual verification and diff gates

Native final `lean_diagnostic_messages` on the complete file:
`partial=false`, `success=true`, `timed_out=false`, `failed_dependencies=[]`;
zero errors, zero sorry messages, the same six out-of-scope warnings.
Actual `/Users/ramin/.elan/bin/lake build Roth.CoeffNorm`, PTY session 79122:
exit 0, `Built Roth.CoeffNorm (17s)`, `Build completed successfully (1658 jobs)`.
No full-project or LeanEval build repeated by this worker.

Exact source diff checked against `/private/tmp/roth-d23-start.lean`:
only the four-line private lemma and separator removed, only sole caller tactic replaced.
Python verified exact authorized transformation and original caller signature byte equality.
No `sorry`, `admit`, `axiom`, `native_decide`, `haveI`, or `letI` in final source.
No dependency/toolchain/config/attribute/suppression changes.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | ✓ pass | Actual module build session 79122 exit 0. |
| definition_protected | ✓ pass | No def/abbrev edits. |
| theorem_statement_protected | ✓ pass with authorized private deletion | Target private wrapper removal explicitly allowed; sole caller original statement and docs byte-identical. |
| structure_gate | ✓ pass | Deleted two-line identity proof, replaced caller equality with one tactic. |
| naming_gate | ✓ pass | No forbidden pattern; no declaration rename. |
| line_packing_gate | ✓ pass | Full historical target and untouched caller table above; removed target has no retained underpacked signature. |
| inequality_orientation_gate | ✓ pass | Table above, no ≥/> added; target original signature has none. |
| cumulative_no_unintended_external_breakage | ✓ pass for owned scope | One private caller in same module, module built; caller original type rechecked independently. Full publication builds handled by file owner. |

Overall: pass. Renames queued: none. Refactoring needed: none.

Independent original-statement reproof imports `Roth.Box` and compiles using
`simp [box, Finset.prod_univ_sum]`; native width-100 #check shown above.
Native final imported caller original-type example also succeeds.
Both independent original identity and `Roth.abs_eval_le` report only
`[propext, Classical.choice, Quot.sound]` under `#print axioms`.
A fresh CLI probe `/private/tmp/roth-d23-final-check.lean` is additionally run after the
module build, proving the original identity and checking the caller against its original type.
Actual `/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-d23-final-check.lean`,
session 16772, exited 0. It printed the original identity type and original caller type;
`d23_original`, `abs_eval_le`, and `d23_caller_original_type` each use only
`[propext, Classical.choice, Quot.sound]`. No diagnostic warning or error in this fresh probe.

## Mandatory phase checklist

- [✓] Step 1 — complete skills/contract/reference docs read.
- [✓] Step 2 — full 24-item audit printed and recorded.
- [✓] Step 2.5 — all five Mathlib search methods and variants recorded.
- [✓] Step 2.6 — every parameter analyzed; actual drop/parent probes run.
- [✓] Step 2.7 — width-100 #check and full per-line packing table recorded.
- [✓] Step 2.8 — inequality scan table recorded.
- [✓] Step 3 — every one of 42 golfing rules has a status.
- [✓] Step 4 — alternative automation, direct API, term-mode reflection completed.
- [✓] Step 5a — complete final LSP diagnostics have no errors or sorries.
- [✓] Step 5b — actual module build and all applicable diff gates passed.
- [✓] Step 6a — no renames needed; no shared sidecar edit.
