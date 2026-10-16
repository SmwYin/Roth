# Phase 4: Roth.normOne_eq_sum_of_support_subset

Scope: `Roth/CoeffNorm.lean:49–51`, one declaration only. Parent baseline: full project and separate LeanEval build exited 0 (18176 jobs); responsive complete LSP. No Git, shared sidecars, other source blocks, definitions, imports, signatures or docstrings changed. Source frozen at SHA256 `d6d990fb089ca49ae94d876a531e7b2237d84b3fb83400f815effd77571ef538`; source ownership revoked on handoff.

## Step 1: References read

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md in full. Also read both `/Users/ramin/.codex/skills/{lean4,mathlib-quality}/SKILL.md`, full `/private/tmp/roth-coeffnorm-worker-contract.md`, all style-rules.md and mathlib-review-stages.md. Naming reference is unnecessary for C3: descriptive name matches no forbidden pattern.

## Step 2: Full audit

The mathematical argument: extend the sum over the support to `s`. Every added exponent has zero coefficient, so its absolute real coefficient contributes zero. This is precisely `Finset.sum_subset` with the polynomial support criterion.

| Item | Finding and action |
|---|---|
| 1 LINT | No target warning. Baseline and final complete LSP have six existing warnings elsewhere: header; four DecidableEq arguments; hC. Preserve all under parent API restrictions. |
| 2 HAVE SCAN | None: the single expression contains no `have`. |
| 3 SET_OPTION | None in target. No limit changes or suppressions. |
| 4 SIMP SQUEEZE | One terminal `simp [notMem_support_iff.1 hd]`; closes the zero-summand obligation. Leave unsqueezed. |
| 5 NAMING | `normOne_eq_sum_of_support_subset` describes the conclusion and support-containment hypothesis; no forbidden abbreviation or pattern. No rename. |
| 6 LINE PACKING | Both signature lines checked below: 85 and 74 codepoints, justified break. |
| 7 BY PLACEMENT | Inner `by` stays on the lambda line. Whole proof is already a direct term. |
| 8 FORMAT | Correct 2-space proof indentation and 4-space signature continuation; no blank proof lines. Change mathematical lambda `=>` to `↦`. |
| 9 COMMENTS | No inline comments; existing one-sentence docstring preserved verbatim. |
| 10 DOCSTRING | Existing public docstring explains the freedom to choose any finite superset of the support. Preserve it. |
| 11 VISIBILITY | Public named API for normOne. Parent explicitly requires preserving public surface; no visibility change. |
| 12 STRUCTURE | Three declaration lines, one proof expression, no conjunction and no branches. No extraction indicated. |
| 13 MATHLIB | All five searches below. Keep existing public normOne API and its direct Finset.sum_subset implementation. |
| 14 JUNK DEF | n/a: theorem, not a definition. |
| 15 EXISTS LEMMA | n/a: equality, not a private existential helper. |
| 16 SHOW vs CHANGE | n/a: neither occurs. |
| 17 PUSH_NEG | n/a: none. |
| 18 GENERALISE | Every parameter audited and drop-probed below; hs is mathematically necessary. No public signature edits. |
| 19 INEQUALITY | Zero reversed inequalities, table below. |
| 20 NORMAL-FORM | Existing norm equality expands to a finite sum. No competing equivalence family. RHS depends on freely chosen s, so do not register as simp. |
| 21 SYNTAX-GEN | OK: implicit P and s inferred from hs, with explicit `(s := ...)` available at union-support call sites. |
| 22 IMPORT-FANOUT | n/a: no imports added. |
| 23 CASTS | Diff: 0 dropped, 0 kept cross-type, 0 kept load-bearing; it changes only a lambda arrow. Original signature ascriptions preserved. |
| 24 INSTANCE-NAME | n/a: no instance declaration. |

Issues found: one mathematical-lambda style issue, fixed. C3 direct proof retained after meaningful alternative probes.
Refactoring needed: none for this declaration. Existing module-wide API-warning decisions remain with the parent.

## Step 2.5: Mathlib search status

| Method | Query and actual result |
|---|---|
| A Lean-Finder | `sum over finite superset equals sum over support if terms vanish outside support`: finsum_eq_sum_of_support_subset; finsum_eq_sum_of_support_toFinset_subset; old-named finsum variant. These concern generic finsum, not Roth.normOne. |
| B Loogle | `Finset.sum_subset`: exact generic finite-sum extension lemma and its type. |
| C LeanSearch | `finite sum unchanged when adding zero terms outside support`: Finset.sum_extend_by_zero, finsum_mem_insert_of_eq_zero_if_notMem, finsum_mem_insert_zero. |
| D Source rg | Untruncated `sum_subset|sum_of_support_subset` search in BigOperators/Group/Finset/Basic, Algebra/MvPolynomial, and Data/Finsupp/Basic; hits in MvPolynomial/Coeff and Expand. Read actual Finsupp.prod_of_support_subset source and its to_additive-generated sum counterpart via #check. |
| E Local search | `sum_of_support_subset`: Finsupp.sum_of_support_subset, DFinsupp analogue and finsum variants. `Finset.sum_subset`: confirmed generic lemma, sum_subset_zero_on_sdiff, sum_eq_of_subset, support_sum_subset, sum_indicator_subset. Index warming, so no absence claim inferred from search. |

Auxiliary variants checked: sum_subset_zero_on_sdiff, sum_eq_of_subset, Finsupp.sum_of_support_subset, finsum_eq_sum_of_support_subset, extend_by_zero. Common-equivalents lookup: no listed bucket matches this finite polynomial-coefficient sum.

Concluded: partial generic match `Finset.sum_subset`; already used directly. The existing public theorem exposes the custom normOne definition. Retain under the explicit public-signature constraint. A direct Finsupp.sum_of_support_subset application was actually tested and rejected: MvPolynomial is not accepted as an α →₀ M argument. No claim of mathlib absence and no new wrapper added. Removing the existing API would require cross-declaration permission and is outside C3's requested proof cleanup.

## Step 2.6: Generalisation status

| # | Parameter | Class | Used as | Mechanical candidates tried | Verified? | Result |
|---|---|---|---|---|---|---|
| 1 | `{σ : Type*}` | type variable/universe | Domain of P and exponent type | Drop binder with autoImplicit false; universe polymorphism | yes | Drop makes the type-domain identifier unknown. Already universe-polymorphic; no stronger class or fixed universe to weaken. |
| 2 | `{P : MvPolynomial σ ℤ}` | structure value | Defines support, coefficients, norm | Drop binder with autoImplicit false; abstract Finsupp/zero-preserving-weight restatement | yes | Drop yields unknown P.support. Generic weighted Finsupp version succeeds via existing mathlib API, but replacing this named norm API changes the mathematical surface and is not applied. |
| 3 | `{s : Finset (σ →₀ ℕ)}` | structure value | Finite summation domain and containment | Drop binder with autoImplicit false | yes | Drop yields unknown s. No typeclass-parent, point-localisation or strict-to-weak candidate: this is data specifying the RHS sum. |
| 4 | `(hs : P.support ⊆ s)` | proposition | First argument of sum_subset | Drop hs, then concrete counterexample; pointwise variant is just expansion of ⊆ | yes | Drop proof fails with unknown hs. Independently verified P = 1 over Unit and s = ∅ gives unequal sums, so no unconditional weakening. No strict inequality or bundled continuity hypothesis to weaken. |

Actual native lean_run_code probes: all three dependent-binder removals fail with the cited unknown-identifier diagnostics; no source mutation. Separate hs-drop probe failed. A successful no-error probe proves the counterexample by `simp [normOne]` and a general weighted Finsupp result using `[Zero M] [AddCommMonoid N]` and `hg : ∀ a, g a 0 = 0` by `Finsupp.sum_of_support_subset`.

Inversion check: yes, normOne unfolds to generic support extension; the abstract theorem already exists as Finset.sum_subset (and the weighted Finsupp API). No new general helper is needed. Existing source stays the one-line specialization.

Big-change candidates: no pending proposal. Generic zero-preserving weighted finite sums are already supplied by mathlib; no reason to restate the preserved public normOne theorem. No typeclass arguments occur in this signature.

### Literature search status

Queries and top three returned hits, recorded without asserting irrelevant results support the theorem:

1. `finite support sum zero outside support generalization additive commutative monoid`:
   [Finite products in commutative monoids](https://arxiv.org/abs/2605.08089);
   [finite sums in a commutative monoid](https://alphabetamath.cc/item/def-finite-sum-in-a-commutative-monoid);
   [Finsupp definitions](https://teorth.github.io/equational_theories/docs/Mathlib/Data/Finsupp/Defs.html).
2. `finite support sum generalization site:ncatlab.org/nlab`:
   [sum](https://ncatlab.org/nlab/show/sum);
   [support of a set](https://ncatlab.org/nlab/show/support%20of%20a%20set);
   [finite object](https://ncatlab.org/nlab/show/finite%2Bobject).
   Only the sum discussion bears on additive algebra; the other two are unrelated notions, not evidence of a further weakening.
3. `site:leanprover-community.github.io/mathlib4_docs Finset.sum_subset`:
   [find Finset.insert (404)](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Finset.insert);
   [Finsupp.Multiset](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Finsupp/Multiset.html);
   [Mathematics in Lean](https://leanprover-community.github.io/mathematics_in_lean/mathematics_in_lean.pdf).
   These search hits do not establish the exact theorem; the pinned local source and elaborator do.

Findings: generic finite sums over additive commutative monoids are the relevant abstraction; compiled mathlib #check and the successful generic probe establish the precise needed generality. No literature-driven change to this public statement. ChatGPT math MCP: n/a, no matching tool available in tool inventory.

## Step 2.7: Line packing

Width reference, actual final `#check` with `set_option format.width 100`:

```lean
@Roth.normOne_eq_sum_of_support_subset : ∀ {σ : Type u_1} {P : MvPolynomial σ ℤ} {s : Finset (σ →₀ ℕ)},
  P.support ⊆ s → Roth.normOne P = ∑ d ∈ s, |↑(P.coeff d)|
```

| Signature line | Codepoints | Next signature token | Arithmetic | Action |
|---|---:|---|---|---|
| 49 | 85 | `(hs : P.support ⊆ s)` (20) | 85 + 1 + 20 = 106 > 100 | ok |
| 50 | 74 | none: `:=` ends signature; proof expression next | n/a | ok |

All signature lines covered; width measured with Python len on Unicode text. The proof line is 69 codepoints. No repack row remains.

## Step 2.8: Inequality scan

| # | Location | Original | Rewrite | Rename? |
|---|---|---|---|---|
| — | Complete signature and hypotheses | n/a: no ≥ or > | none | none: name has no _ge_/_gt_ |

## Step 3: Every golfing rule

| Rule | Status |
|---|---|
| 1.1 by exact wrapper | n/a: direct term already. |
| 1.2 by rfl | n/a: none. |
| 1.3 rw + exact | n/a: no rw. |
| 1.4 simp + exact | n/a: sole simp is terminal. |
| 1.5 trailing rfl | n/a: none. |
| 1.6 constructor + exact | n/a: equality proved by generic sum lemma. |
| 1.7 apply + exact | n/a: direct application already. |
| 1.8 by_contra + push_neg | n/a: no contradiction proof. |
| 1.9 eta reduction | n/a: lambda constructs a zero-summand proof from hd and is not eta-expanded. Arrow syntax corrected. |
| 1.10 single-use have | n/a: none. |
| 1.11 apply + intro | n/a: direct lambda already. |
| 1.12 redundant show | n/a: none. |
| 1.13 have + projections | n/a: none. |
| 1.14 merge rw | n/a: none. |
| 1.15 terminal simp only | n/a: already unsqueezed. |
| 1.16 nonterminal simp | n/a: none. |
| 1.17 dot notation | n/a: sum_subset is a namespace operation with hs as explicit argument, already direct. |
| 1.18 use <\| | n/a: no wrapping parenthesis. |
| 1.19 push Not | n/a: no push_neg. |
| 1.20 trivial existential | n/a: no existential. |
| 2.1 grind whole proof | Tested in isolated original-import context without target theorem: fails. Inner `grind [notMem_support_iff]` also fails. |
| 2.2 remove before grind | n/a: no grind in source. |
| 2.3 simpa consolidation | n/a: no following closing tactic. Whole `simp [normOne]` tested and leaves sum equality. |
| 2.4 fun_prop | n/a: equality of finite sums, no function property. |
| 2.5 positivity | n/a: no positivity/nonzero target. |
| 2.6 gcongr | n/a: no inequality. |
| 2.7 lia/omega | n/a: support extension, not arithmetic constraints. |
| 2.8 aesop | Whole proof tested and fails; inner zero-summand goal succeeds. Retain explicit simp because it names the support-to-zero step clearly, same line count. |
| 2.9 norm_num/norm_cast | n/a: no numeric target or unresolved cast equality; zero coefficient simp already handles cast zero. |
| 2.10 decide/+kernel | n/a: arbitrary polynomial coefficients over arbitrary type, not closed finite computation. |
| 2.11 field_simp; ring | n/a: no denominators or polynomial identity. |
| 2.12 linear_combination | n/a: no ring/ring_nf proof. |
| 2.13 wlog | n/a: no symmetric cases. |
| 2.14 calc to term | n/a: no calc, already term mode. |
| 2.15 <;> | n/a: no repeated goals. |
| 3.1 erw to rw | n/a: neither. |
| 3.2 continuity to fun_prop | n/a: no analysis automation. |
| 3.3 omega to lia | n/a: no omega. |
| 3.4 rcases rfl | n/a: none. |
| 3.5 automation registration | Not added: s is introduced on RHS and uncontrolled expansion would be a poor simp normal form. |
| 3.6 simp_all | n/a: no simp_all only. |
| 3.7 remove maxHeartbeats | n/a: none. |

Probe caveat: first live multi_attempt column joined `by` to tactic text, producing `bysimp` etc.; corrected by preserving whitespace and reran all. Only corrected results count. Whole-proof `exact?` failed; `apply?` suggested unrelated real extensionality subgoals and did not close. Inner `exact?` failed; inner `apply?` suggested abs_eq_zero.mpr but left a cast-zero subgoal. No source or final axiom result relies on these incomplete scratch attempts.

## Step 4: Reflection

The support-to-superset argument is already one direct generic lemma application, and the inner zero coefficient is one terminal simp. Whole-proof automation failed; Finsupp substitution would require exposing polynomial representation. Retaining direct Finset.sum_subset preserves a readable mathematical reason with minimum syntax. No have blocks, redundant transitions, branches, or missing-API signals remain.

## Step 5: Verification and gates

Final module build: `/Users/ramin/.elan/bin/lake build Roth.CoeffNorm`, exit 0; `Built Roth.CoeffNorm (15s)`, 1658 jobs. Six unchanged source warnings, plus dependency header warnings. Final native complete `lean_diagnostic_messages` returned `success: true`, `partial: false`, `timed_out: false`, `failed_dependencies: []`, zero errors and six known warnings, none in target. Goal query shows source with ↦ and no goals.

Final independent CLI verification: `/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-coeffnorm-d03-final.lean`, exit 0. It imports the final built module, assigns the exact original type to the actual declaration, independently reproves the original statement with Finset.sum_subset, and prints axioms for both. Both actual declaration and independent reproof depend only on `[propext, Classical.choice, Quot.sound]`. A separate successful native probe also reproved the original statement using the original imports and norm definition without importing the target theorem, excluding accidental self-use.

Owned diff:

```diff
-  Finset.sum_subset hs fun d _ hd => by simp [notMem_support_iff.1 hd]
+  Finset.sum_subset hs fun d _ hd ↦ by simp [notMem_support_iff.1 hd]
```

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | ✓ pass | Actual module build exit 0, 1658 jobs. |
| definition_protected | ✓ pass | No def/abbrev changed. |
| theorem_statement_protected | ✓ pass | Both original signature lines and all implicit parameters unchanged. |
| structure_gate | ✓ pass | One proof expression; declaration 3 lines; no conjunction/branches. |
| naming_gate | ✓ pass | Descriptive norm support-extension name, no forbidden pattern. |
| line_packing_gate | ✓ pass | Complete two-row measured table, no repack rows. |
| inequality_orientation_gate | ✓ pass | Complete scan table; zero ≥/>. |

Overall: pass.

## Step 6: Result

Before: 3 lines. After: 3 lines. Saved: 0 lines. Audit issues found: 1; fixed: 1. Rules applied: mathematical lambda style. Existing direct sum-subset proof retained after alternatives. Renames queued: none. Comments preserved: no inline comments present; original docstring preserved. Refactoring needed: none in scope. Pending warnings: six existing file warnings remain subject to the parent's explicit preservation/API restrictions.

- [✓] Step 1 — required references read.
- [✓] Step 2 — all 24 audit items reported.
- [✓] Step 2.5 — five-method mathlib search reported.
- [✓] Step 2.6 — every parameter, actual probes and literature search reported.
- [✓] Step 2.7 — complete per-line width table reported.
- [✓] Step 2.8 — inequality scan table reported.
- [✓] Step 3 — all 42 golfing rules have status lines.
- [✓] Step 4 — step-back reflection completed.
- [✓] Step 5a — final complete LSP clean of errors; target warning-free.
- [✓] Step 5b — all seven diff/build gates pass.
- [✓] Step 6a — no renames required; no shared sidecar touched.
