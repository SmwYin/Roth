# Phase 4 — `Roth.normOne_monomial`

Owner scope: only `Roth/CoeffNorm.lean` L53–57 (docstring and declaration) and this report.
No Git operations, shared logs, imports, public signatures, definition values, or docs changed.
Baseline supplied by file owner: full and separate `LeanEval` build 89274 exited 0;
complete baseline LSP had no errors. Six outside warnings were explicitly preserved.
The full worker contract, both SKILL.md files, and mandatory references were read in full:
`golfing-rules.md`, `proof-patterns.md`, `mathlib-search.md`,
`generalisation-patterns.md`, `cleanup-gates.md`, `style-rules.md`,
`naming-conventions.md`, and `mathlib-review-stages.md`.

## Result

Before: 5 lines including docstring. After: 5. Saved: 0 lines, 33 characters.
One redundant proof ascription removed; public statement and docstring byte-identical.

```diff
-  rw [normOne_eq_sum_of_support_subset (support_monomial_subset : (monomial e c).support ⊆ {e})]
+  rw [normOne_eq_sum_of_support_subset support_monomial_subset]
```

Final proof:

```lean
theorem normOne_monomial (e : σ →₀ ℕ) (c : ℤ) : normOne (monomial e c) = |(c : ℝ)| := by
  classical
  rw [normOne_eq_sum_of_support_subset support_monomial_subset]
  simp
```

C4 resolved: descriptive public monomial norm API retained; terminal simp remains unsqueezed;
direct library alternatives and meaningful automation actually tested below.
Source frozen and ownership released at SHA256
`62cc00913634a7662c2313a3c36a98f0891f663db3577869a49ff676bbd4e1e5`.
After release only report/probes/build/LSP work was performed.

## Full 24-item audit

| # | Audit | Finding/action |
|---|---|---|
| 1 | LINT | No warning or error in L53–57; complete final LSP clean of errors. |
| 2 | HAVE SCAN | None: proof has no `have` bindings. |
| 3 | SET_OPTION | None in declaration; no limit raises or suppressions added. |
| 4 | SIMP SQUEEZE | L57 bare terminal `simp` closes goal; keep unsqueezed. |
| 5 | NAMING | `normOne_monomial` describes the value of the named norm on monomials; correct existing identifier fragment `normOne`; no forbidden abbreviations, numeric patterns, or single-letter API name. No rename needed. |
| 6 | LINE PACKING | One 88-codepoint signature line; complete table below. |
| 7 | BY PLACEMENT | `:= by` ends signature line. |
| 8 | FORMAT | Two-space proof indentation, one tactic per line, no internal blank lines/trailing whitespace, no `haveI`/`letI`. |
| 9 | COMMENTS | No inline comments present; none removed or relocated. |
| 10 | DOCSTRING | Existing one-sentence public docstring preserved verbatim; correctly distinguishes the monomial computation from general bounds. |
| 11 | VISIBILITY | Public reusable norm API; used by multiplication and product proofs; preserve visibility. |
| 12 | STRUCTURE | Three proof lines, no conjunction or branches; below every decomposition threshold. |
| 13 | MATHLIB | Five methods completed; partial matches are `sum_monomial_eq`, `support_monomial_subset`; local `normOne` API is not a duplicate library declaration. Search/probes below. |
| 14 | JUNK DEF | n/a: theorem, not a definition. |
| 15 | EXISTS LEMMA | n/a: not an existential/private witness lemma. |
| 16 | SHOW vs CHANGE | n/a: neither present. |
| 17 | PUSH_NEG | n/a: no negation tactic. |
| 18 | GENERALISE | All three parameters checked, actual drop probes below; no removable assumption. |
| 19 | INEQUALITY | Zero reversed inequalities; scan table below. |
| 20 | NORMAL-FORM | Already value-computation form `normOne (monomial e c) = abs c`; coefficient absolute value on RHS is the natural result. |
| 21 | SYNTAX-GEN | OK: explicit exponent/coefficient are easy to apply and rewrite; no bundled evidence required. |
| 22 | IMPORT-FANOUT | n/a: no import change. |
| 23 | CASTS | One redundant proof ascription dropped; statement's `c : ℝ` is a genuine ℤ→ℝ conversion and preserved. No coercion churn. |
| 24 | INSTANCE-NAME | n/a: target is not an instance and introduces no instances. |

Issues found: one redundant proof type ascription; fixed one.
Refactoring needed: none for this declaration. File-level API warnings remain with file owner.

## Mathlib search-status

[A] Lean-Finder query: `sum absolute coefficients monomial l1 norm equals absolute coefficient`.
Returned `PadicInt.norm_mahlerTerm`, `FormalMultilinearSeries.ofScalars_norm`,
`Polynomial.mahlerMeasure_const`; different norms, no replacement.

[B] Loogle query: `MvPolynomial.monomial, Finset.sum`.
Returned `MvPolynomial.as_sum`, `support_sum_monomial_coeff`, `monomial_sum_prod`,
`monomial_sum_one`, `monomial_sum_index`; none computes this project norm.

[C] LeanSearch query: `sum over support of monomial equals function of its coefficient`.
Returned `MvPolynomial.sum_def`, `MvPolynomial.eval_eq'`, `Polynomial.sum_monomial_eq`.
`sum_def`/sum-monomial route tested directly below.

[D] Untruncated `rg` over mathlib MvPolynomial and Analysis/Normed for
`sum_monomial|support_monomial|norm.*monomial`: relevant matches
`MvPolynomial.sum_monomial_eq` (Basic L276), `support_monomial` (L468),
`support_monomial_subset` (L477). Further untruncated full-name search
`rg -n 'normOne_monomial' .lake/packages/mathlib/Mathlib` exited 1, no matches.
Read Basic L262–286 and support/coefficient representation matches.

[E] Native `lean_local_search` query `sum_monomial` returned source-backed
`MvPolynomial.sum_monomial_eq`, `Polynomial.sum_monomial_index`, etc.
Index was `warming`, so empty-index absence was never inferred.

Auxiliary variants inspected: `support_monomial`, `support_monomial_subset`,
`sum_monomial_eq`, `sum_def`, `finsupp_support_eq_support`, polynomial norm variants.
Common-equivalents lookup: no matching discrete/finiteness/separation/bornology bucket.
Generic compiled absence check: live `exact?` fails; `apply?` offers only partial Real
extensionality/absolute-value goals, not a theorem closing the norm computation.
Concluded: partial mathlib matches; retain local API and use `support_monomial_subset`
through the project's finite-support sum lemma. No new wrapper or predicate introduced.
Deleting the public project-norm API would contradict the explicit signature-preservation
scope and does not replace it with a directly applicable library theorem.

## Actual tactic/candidate evidence

Native Lean MCP was discovered through `ALL_TOOLS` metadata. `lean_goal` at L55 showed:
`σ : Type u_1; e : σ →₀ ℕ; c : ℤ ⊢ normOne ((monomial e) c) = |↑c|`.
No native stalls required the direct fallback.

`lean_multi_attempt` at L56 and L55 tested these actual snippets. Its replacement mechanism
can leave following source tactics in place: a `No goals to be solved` from the old trailing
`simp` means the candidate already closed the goal, not that it is a clean whole-file patch.

| Candidate | Actual result | Decision |
|---|---|---|
| `simp [normOne]` | Leaves sum over monomial support with an `if e = x`; trailing simp no progress. | Reject. |
| `simp [normOne, support_monomial]` | Leaves sum over `if c = 0 then ∅ else {e}`. | Reject. |
| `grind [normOne]` | `grind failed`; negated equality survives with an absolute-value order case. | Reject. |
| `aesop` | Failed, made no progress. | Reject. |
| `exact?` | Could not close goal. | Reject. |
| `apply?` | Partial Real cauchy extensionality goals; no closing library result. | Reject. |
| `simpa only [normOne, ← MvPolynomial.sum_def] using (MvPolynomial.sum_monomial_eq (u := e) (r := c) (b := fun _ a ↦ |(a : ℝ)|) (by simp))` | Type mismatch: sum over `.coeff` representation versus project support. | Reject. |
| `simpa [normOne, Finsupp.sum] using (sum_monomial_eq (u := e) (r := c) (b := fun _ a ↦ |(a : ℝ)|) (by simp))` | Type mismatch: `.coeff.support` versus polynomial support. | Reject. |
| `classical; split_ifs <;> simp_all [normOne, support_monomial]` | `split_ifs` has no condition before unfolding. | Reject. |
| `classical; by_cases hc : c = 0 <;> simp [normOne, support_monomial, hc]` | Candidate closes; old trailing simp reports no goals. | Do not keep: adds case split and unfolds norm/support, less direct than supplied support API. |
| `classical; simp [normOne, support_monomial, apply_ite]` | Leaves membership implication implying absolute coefficient zero. | Reject. |
| `classical; simp [normOne, support_monomial, Finset.sum_ite]` | Unsolved sum; unused simp argument warning. | Reject. |
| `classical; rw [normOne_eq_sum_of_support_subset support_monomial_subset]; simp` | No goals and no diagnostics. | Keep; removes redundant proof ascription. |
| Same support proof without `classical` (isolated `lean_run_code`) | Leaves `|↑(((monomial e) c).coeff e)| = |↑c|`; no closing simp equality. | Keep local classical. |

Notation `;` in this evidence table separates the tested multiline snippets for readability;
final source has one tactic per line.

## Generalisation status

All candidates were isolated scratch probes; public signatures were never edited.
Actual drop tests ran with `set_option autoImplicit false` so missing binders cannot be
silently recreated by Lean. Diagnostics returned the unknown identifiers below; elaborator
error placeholders in those intentionally failing probes are not source sorries.

| # | Parameter | Class | Used as | Mechanical candidates tried | Verified? | Result |
|---|---|---|---|---|---|---|
| 1 | `{σ : Type*}` | type-variable/universe | Domain of exponent and polynomial | Drop σ; universe catalogue checked (`Type*` already polymorphic). No typeclass parents, local/global proposition, or strict inequality exists to weaken. | Yes, drop probe L5 | Unknown identifier `σ`; retain. Arbitrary universe shown by width-100 #check. |
| 2 | `(e : σ →₀ ℕ)` | structure-value | Monomial exponent in conclusion/support subset | Drop e. Point localisation, strict→weak, class-parent and unbundling catalogue entries do not apply to an arbitrary exponent value. | Yes, drop probe L10 | Unknown identifier `e`; retain. Changing explicitness is an API restatement, not weaker mathematics. |
| 3 | `(c : ℤ)` | structure-value | Coefficient in monomial and RHS cast | Drop c. No positivity/nonzero/bundled or class assumptions exist; concrete→abstract coefficient ring requires changing `normOne` itself. | Yes, drop probe L15 | Unknown identifier `c` at both occurrences; retain. |

There are no proposition, typeclass or decidability parameters to omit. The local
`classical` tactic is proof implementation, not a public assumption; its removal was
actually tested and failed as above.
Inversion check: after the support rewrite the proof computes a singleton sum, precisely
the abstraction already supplied by `normOne_eq_sum_of_support_subset`; no new extracted
lemma is needed. A generic finitely-supported sum with any zero-preserving coefficient
weight is the underlying library `sum_monomial_eq`, already searched/probed.
Big-change candidates: extending the definition of the coefficient norm to arbitrary
seminormed coefficients is mathematically possible but changes the definition/API and
is outside this declaration cleanup. No such change is applied or requested here.

## Public literature search

Web search was performed (not inferred from local grep). Search hit snapshots are
reported as evidence, not endorsements or claims that all hits prove a generalization.

Query `polynomial coefficient l1 norm monomial generalization`; first three returned hits:
1. [ICLR 2021 paper](https://openreview.net/pdf?id=uz5uw6gM0m): polynomial learning; no direct theorem replacement.
2. [Norms on polynomial vector spaces](https://math.stackexchange.com/questions/1805891/norms-on-mathcalp-n-vector-space-of-polynomials-up-to-order-n): discussion of coefficient norms, secondary source only.
3. [Coefficient norm development](https://causalsmith.org/library/Mathlib/Analysis/BernsteinSzegoTrig/): external generated library, not pinned mathlib; not used as theorem evidence.

Query `"polynomial" "l1" "norm" "monomial" generalization coefficient norm`; three hits retained:
1. [Rings library source](https://github.com/PoslavskySV/rings/blob/develop/rings/src/main/java/cc/redberry/rings/poly/univar/UnivariatePolynomial.java): coefficient one-norm convention.
2. [Polynomial norm discussion](https://math.stackexchange.com/questions/1805891/norms-on-mathcalp-n-vector-space-of-polynomials-up-to-order-n): secondary background.
3. [Best ℓ1 approximation paper](https://hal.science/hal-00546660v1/document): primary mathematical source using the coefficient-vector ℓ1 norm for multivariate real polynomials.

Query `site.en.wikipedia.org polynomial "sum of the absolute" coefficients norm`; first three relevant returned hits:
1. [Landau–Mignotte bound](https://en.wikipedia.org/wiki/Landau-Mignotte_bound).
2. [Per Enflo](https://en.wikipedia.org/wiki/Per_Enflo).
3. [Norm](https://en.wikipedia.org/wiki/Norm_%28mathematics%29).
These are secondary context; no result from them is used to justify a source change.
Primary source and local library mathematics support the familiar coefficient-norm
formulation; the inference that a singleton support gives the coefficient norm is elementary.
The coefficient-domain broadening would require a different norm API, not dropping a
hypothesis from this statement. Literature-driven applied changes: none.
ChatGPT math MCP: n/a; `ALL_TOOLS` contains no tool matching `chatgpt.*math`.

## Line packing

Native width reference (`set_option format.width 100`, corrected after an initial scratch
`pp.width` typo):

```text
@normOne_monomial : ∀ {σ : Type u_1} (e : σ →₀ ℕ) (c : ℤ), normOne ((monomial e) c) = |↑c|
```

| Sig line | Codepoints | Next signature token | Arithmetic | Action |
|---|---|---|---|---|
| 54 | 88 | None, proof body next | n/a: no next signature line; all binders/conclusion/`:= by` already packed | ok |

Proof lines measured too: L55 11, L56 63, L57 6 codepoints. The old L56 was 96;
new L56 removes 33 characters without artificially chaining tactics.

## Inequality scan

| # | Location | Original | Rewrite | Lemma rename? |
|---|---|---|---|---|
| — | L54 entire signature, all parameters | n/a — zero `≥` or `>` occurrences | None | No `_ge_`/`_gt_` fragment |

## All 42 golfing rules

| Rule | Status |
|---|---|
| 1.1 by exact | n/a: no exact wrapper. |
| 1.2 by rfl | n/a: not a reflexivity proof. |
| 1.3 rw + exact | n/a: rw is followed by simp, not exact. |
| 1.4 simp + exact | n/a: simp is terminal. |
| 1.5 trailing rfl | n/a: none. |
| 1.6 anonymous constructor | n/a: equality, no constructor branches. |
| 1.7 apply + exact | n/a: no apply chain. |
| 1.8 by_contra! | n/a: no contradiction proof. |
| 1.9 eta reduction | n/a: no lambda in final proof. |
| 1.10 inline have | n/a: no have. |
| 1.11 refine + fun | n/a: no apply/intro. |
| 1.12 redundant show | n/a: no show. |
| 1.13 obtain | n/a: no projections or have. |
| 1.14 merge rw | n/a: one rw. |
| 1.15 unsqueeze terminal simp only | n/a: already bare terminal simp. |
| 1.16 squeeze nonterminal simp | n/a: no nonterminal simp. |
| 1.17 dot notation | n/a: support lemma arguments inferred, no eligible receiver. |
| 1.18 use `<|` | n/a: removed whole redundant ascription rather than introducing function parentheses. |
| 1.19 push Not | n/a: no negation pushing. |
| 1.20 inline existential | n/a: no existential helper. |
| 2.1 grind | Actually tested `grind [normOne]`; failed. |
| 2.2 delete before grind | n/a: no grind in retained proof. |
| 2.3 simpa consolidation | Actually tested two generic sum variants; type mismatches. No simp+closing-step chain in retained proof. |
| 2.4 fun_prop | n/a: no continuity/differentiability/measurability goal. |
| 2.5 positivity | n/a: equality computing a finite sum, no sign side-goal. |
| 2.6 gcongr | n/a: no inequality/monotonicity goal. |
| 2.7 lia / omega | n/a: not a Nat/Int linear arithmetic proposition. |
| 2.8 aesop | Actually tested; made no progress. |
| 2.9 norm_num / norm_cast | n/a: variable coefficient, not numeric computation or cast equality; retained cast bridges ℤ→ℝ. |
| 2.10 decide / kernel | n/a: arbitrary coefficient and type; no closed finite decision computation. |
| 2.11 field_simp; ring | n/a: no denominators or ring-normal-form identity. |
| 2.12 linear_combination | n/a: no ring ending or algebraic equality hypotheses. |
| 2.13 wlog | n/a: no symmetric branches; tested zero split offered no improvement. |
| 2.14 collapse calc | n/a: no calc block. |
| 2.15 `<;>` | Case-split candidate tested; no multiple similar goals in retained proof. |
| 3.1 erw→rw | n/a: already rw. |
| 3.2 fun_prop migration | n/a: no legacy continuity/measurability tactic. |
| 3.3 omega→lia | n/a: neither arithmetic tactic present or appropriate. |
| 3.4 rcases rfl | n/a: no rcases. |
| 3.5 automation attributes | No new attribute: public signature/normal-form surface preserved; target already readily used explicitly in simp lists. |
| 3.6 simp_all | Tested split_ifs/simp_all route failed before unfolding; no hypotheses to simplify in retained proof. |
| 3.7 remove options | n/a: no heartbeat/recursion options. |

## Step-back reflection

The theorem is singleton-support evaluation. Whole-proof automation and direct library
sum alternatives were actually tried. Term mode would still need a classical singleton
coefficient simplification and would be longer; it would add no reusable mathematics.
The support-subset rewrite avoids a zero/nonzero split and uses the API deliberately
provided immediately above. Removing its explicit type annotation is a clear local
improvement; retain the remaining three tactics. No helper extraction or rename warranted.

## Verification and gates

Final native `lean_diagnostic_messages` over the complete file after module build:
`success=true`, `partial=false`, `timed_out=false`, no failed dependencies, zero errors,
zero target warnings. Six preserved outside warnings: header L1; unused DecidableEq at
L92, L107, L125, L297; unused `hC` at L128. These await the existing user API decision
and were not suppressed, renamed, or removed by this worker.

Actual `/Users/ramin/.elan/bin/lake build Roth.CoeffNorm`: exit 0,
`Built Roth.CoeffNorm (24s)`, `Build completed successfully (1658 jobs)`.
No full project build run by this worker.
Native isolated original-type/reproof/axiom probe succeeded, but reported stale import info;
therefore a fresh CLI probe was additionally required (recorded below).

Fresh CLI final gate:
`/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-normOne-monomial-final.lean`,
exec session 91378, exit 0. No cached-import notice, warning, or error.
The file imports the newly built module, checks the exact original type by assigning
`Roth.normOne_monomial` to the original universally quantified statement, independently
reproves that statement without referring to the target theorem, and prints both axioms:

```text
@normOne_monomial : ∀ {σ : Type u_1} (e : σ →₀ ℕ) (c : ℤ), normOne ((monomial e) c) = |↑c|
'Roth.normOne_monomial' depends on axioms: [propext, Classical.choice, Quot.sound]
'independently_reproved' depends on axioms: [propext, Classical.choice, Quot.sound]
```

| Gate | Result | Actual evidence |
|---|---|---|
| lake_build_file | ✓ pass | `lake build Roth.CoeffNorm`, session 84288, exit 0, built in 24s. |
| definition_protected | ✓ pass | Focused diff changes one proof rewrite only; no definition/abbrev line changed. |
| theorem_statement_protected | ✓ pass | Entire original statement/docstring unchanged; fresh original-type assignment compiles. |
| structure_gate | ✓ pass | Three proof lines; no ∧ or branches. |
| naming_gate | ✓ pass | Descriptive norm/monomial name; no forbidden patterns/abbreviations; no rename required. |
| line_packing_gate | ✓ pass | All signature lines measured (one 88-codepoint line), no repack row. |
| inequality_orientation_gate | ✓ pass | Complete occurrence scan gives zero reversed inequalities or ge/gt name fragments. |
| standard_axioms | ✓ pass | Fresh CLI target and independent reproof use only propext, Classical.choice, Quot.sound. |
| source_integrity | ✓ pass | Sole source edit removes proof ascription; no sorry, new axiom, suppression, limit option or scaffolding introduced. |

Overall: pass. Renames queued: none. Inline comments preserved: none present.
Refactoring needed: none for this declaration.
Pending outside scope: six existing file warnings, including the header explicitly
preserved by the user and public-argument warnings pending the file owner's API decision.

## Required phase checklist

- [✓] Step 1 — mandatory references read in full.
- [✓] Step 2 — all 24 audit items reported with concrete findings.
- [✓] Step 2.5 — five-method search status, variants and generic compiled probe reported.
- [✓] Step 2.6 — every parameter mechanically checked; actual candidate/drop probes and public literature search reported.
- [✓] Step 2.7 — complete per-signature-line codepoint table and width-100 #check emitted.
- [✓] Step 2.8 — complete inequality occurrence scan table emitted.
- [✓] Step 3 — all 42 rules have individual statuses and applicable probes.
- [✓] Step 4 — independent strategy/term-mode/API reflection completed.
- [✓] Step 5a — complete final LSP has no errors or target warnings.
- [✓] Step 5b — actual module build, fresh independent Lean proof/type/axiom gates and focused diff checks pass.
- [✓] Step 6a — no rename needed; sidecar unchanged.
