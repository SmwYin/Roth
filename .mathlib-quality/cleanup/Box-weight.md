# Phase 4 — `Roth.weight`

Dedicated worker: `/root/cleanup_continuation/box_file/decl05`. Baseline `20d4254`.
Target: `Roth/Box.lean:66`, one declaration line (original line 65).
Outcome: retained unchanged; one-line term-mode real weighted sum already has an extensive API.

## Step 1 — References

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md in full, together with the full worker
instructions and lean4 skill. Relevant style-rules sections read: width, variable conventions,
formatting, comments, docstrings, mathlib-first, junk definitions, unused variables, syntax,
declaration formatting, visibility, hypotheses, normal forms, transparency, and definition API.
Naming-conventions extra read is n/a: no naming defect was identified.

## Step 2 — Full audit

1. **LINT:** none at the target declaration. Full-file LSP succeeds with no errors;
   known header and later-declaration warnings remain outside this worker's scope.
2. **HAVE SCAN:** none; the body is a finite sum data term.
3. **SET_OPTION:** none in the target; none added.
4. **SIMP SQUEEZE:** n/a: no simp or tactic block in this definition.
5. **NAMING:** `weight` is a descriptive mathematical lowerCamelCase noun, qualified by
   `Roth`; it contains none of the forbidden abbreviations or numeric/internal patterns.
   No rename is warranted or queued.
6. **LINE PACKING:** the sole physical declaration line is 77 codepoints; signature through
   `:=` is 56. All parameters, result type, and body fit on that line. Table below.
7. **BY PLACEMENT:** n/a: data is defined in term mode, with no `by`.
8. **FORMAT:** flush-left one-line declaration, standard spacing, no internal blank lines,
   `haveI`/`letI`, tactic sequences, or redundant syntax.
9. **COMMENTS:** no inline body comments; existing docstring preserved byte-for-byte.
10. **DOCSTRING:** existing sentence identifies the weighted multi-index and its source in
    the index construction. No proof prose or missing documentation issue.
11. **VISIBILITY:** public API is justified by direct consumers in Index, Lattice, Main,
    Theta, and MainLemma; privatizing would break these consumers.
12. **STRUCTURE:** one-line data expression, zero conjunctions and zero branches;
    no extraction or decomposition is warranted.
13. **MATHLIB:** five-method status below. `Finsupp.weight` is a related generic additive
    homomorphism, and its reciprocal-real specialization is propositionally equal to this
    sum (compiled). Retain the documented project API and its exact mathematical definition.
14. **JUNK DEF:** not junk: surrounding API includes nonnegativity, zero, additivity,
    zero characterization, single support, coordinate bounds, scaling, degree bounds,
    and reindexing; used throughout multiple external files.
15. **EXISTS LEMMA:** n/a: definition of real data, not an existential lemma.
16. **SHOW vs CHANGE:** n/a: neither occurs.
17. **PUSH_NEG:** n/a: none occurs.
18. **GENERALISE:** actual signature already excludes section `DecidableEq`; no assumption
    can be mechanically dropped while retaining this finite-universe sum. Tables below.
19. **INEQUALITY:** zero inequalities in signature/body; no `_ge_`/`_gt_` name. Table below.
20. **NORMAL-FORM:** finite sum of real quotients is the project convention used by the
    index API. The generic support-sum/scalar-multiplication form has a compiled bridge,
    but no additional equivalence API or normal-form migration is needed.
21. **SYNTAX-GEN:** OK: explicit `r` and `d` match existing call sites; no restatement proposed.
22. **IMPORT-FANOUT:** n/a: no new imports; `Finsupp.Weight` already imported.
23. **CASTS:** diff: 0 dropped / 0 kept cross-type / 0 kept load-bearing because no source
    diff. Existing `(d j : ℝ)` is genuine ℕ→ℝ coercion, as is implicit denominator cast.
    Removing the numerator cast risks selecting natural division before result inference;
    there is no redundant real-to-real cast.
24. **INSTANCE-NAME:** n/a: this is a definition, not an instance.

Issues to fix: none. Refactoring needed: none.

## Step 2.5 — Mathlib search status

| Method | Query / evidence | Result |
|---|---|---|
| A Lean-Finder | `Finsupp weight weighted sum natural exponents real weights` | `Finsupp.weight`, `weight_apply`, `degree_eq_weight_one` |
| B Loogle | `Finsupp.weight` | Generic additive homomorphism and its finiteness/degree API |
| C LeanSearch | Known service HTTP 500 from earlier serialized workers | Unavailable; not treated as absence; no redundant failing retry |
| D Source grep | Untruncated `def weight`, `theorem weight`, `lemma weight`, `weight.*sum` in Mathlib/Data/Finsupp/Weight.lean | Definition L82, apply L85, sum L100, single and zero APIs |
| E Name pattern | `lean_local_search Finsupp.weight` | Eight source hits including `weight_eq_sum`; semantic index unavailable, so no absence claim |

Auxiliary variants inspected: `weight_apply`, `weight_eq_sum`, `weight_single`,
`weight_eq_zero_iff_eq_zero`, `degree_eq_weight_one`. Common-equivalents buckets: no match;
this is weighted algebraic data, not discrete/finiteness/boundedness predicates.

Actual `#check @Finsupp.weight` and `#check @Finsupp.weight_eq_sum` succeed. The following
comparison compiled successfully in `lean_run_code`:

```lean
example {σ : Type*} [Fintype σ] (r : σ → ℕ) (d : σ →₀ ℕ) :
    Roth.weight r d = Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹) d := by
  simp [Roth.weight, Finsupp.weight_eq_sum, nsmul_eq_mul, div_eq_mul_inv]
```

Conclusion: related generic construction found; no absence claim. A replacement would
change the declared representation from division over `Finset.univ` to a support sum of
scalar multiples and remove/alter a public project definition used by many callers.
The user/dispatch explicitly preserves this mathematical definition/signature and permits
only beneficial definitionally-equal syntax cleanup. Retain it; no missing-API signal occurs.
This is a documented mathematical definition with API, not a disposable theorem wrapper.
No broader migration is proposed as necessary cleanup.

## Step 2.6 — Generalisation status

| Parameter | Class | Used as | Mechanical candidates considered/tried | Verified? | Result |
|---|---|---|---|---|---|
| `{σ : Type*}` | type variable | Domain of `r`, `d`, and sum | Already universe-polymorphic; dropping leaves dependent types without a domain | Type checked | Retain; no stricter universe constraint |
| `[Fintype σ]` | typeclass | Constructs the universe finite sum | Drop; replace by `[Finite σ]` with unchanged body | Yes, scratch diagnostics | Both fail to synthesize `Fintype σ`; retain |
| section `[DecidableEq σ]` | decidability | Unused in this def | Inspect actual type; isolate definition without it | Yes | Already absent, no edit required |
| `(r : σ → ℕ)` | structure value | Denominators `r j` | Drop with autoImplicit false | Yes, scratch diagnostics | Unknown identifier `r`; retain |
| `(d : σ →₀ ℕ)` | structure value | Numerators `d j` | Drop with autoImplicit false | Yes, scratch diagnostics | Unknown identifier `d`; retain |

No proposition/positivity/nonzero/global analytic hypotheses to weaken or point-localize.
No algebraic instance parameters with weaker parents. Replacing ℝ by another coefficient
structure or allowing infinite `σ` through a support sum changes the data/API rather than
performing a small hypothesis cleanup; not proposed in this task. Inversion diagnostic:
n/a, a data definition has no proof abstracting away from a named object.

Big-change candidates requiring action: none. Existing generic `Finsupp.weight` is available
for future clients needing a broader construction; current scope preserves this API.

### Literature search status

[A] Web search: `Roth theorem index polynomial weighted sum multi index r_i definition generalization`.
Top three returned hits were Min Ru's notes, a third-party copy of Bombieri–Gubler, and Wikipedia.
The latter two were not used as technical evidence. Primary-source follow-up inspected:

- [Min Ru, Roth's Theorem](https://www.math.uh.edu/~minru/fields/roth.pdf), Definition 1,
  uses natural multi-indices and positive integer denominator weights in the index.
- [K. F. Roth, ICM 1958 proceedings](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf),
  search excerpt describes positive parameters and weighted derivative order; direct open failed.
- [An elementary approach to Roth's theorem](https://aleksa-milojevic.github.io/expository/roth.pdf),
  opened successfully as an additional primary exposition of the index construction.

Inference: the existing finite normalized multi-index sum is the intended classical
construction. No literature evidence requires a broader API for these consumers. The definition
already allows zero denominator parameters under Lean's total real division; positivity belongs
only in subsequent theorems that need it.

[B] ChatGPT math MCP: n/a, no such callable tool in the available tool inventory.
Literature-driven big-change proposals: none.

## Step 2.7 — Line packing

Actual compiled output at `format.width := 100`:

```lean
@Roth.weight : {σ : Type u_1} → [Fintype σ] → (σ → ℕ) → (σ →₀ ℕ) → ℝ
```

| Signature line | Codepoints through `:=` | Full physical line | Next signature token | Arithmetic | Action |
|---|---:|---:|---|---|---|
| 66 | 56 | 77 | None: all signature and body already on one line | n/a, no next signature line | ok |

Measured with Python `len` on decoded Unicode; not byte counts.

## Step 2.8 — Inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| — | Entire signature and definition body | No `≥` or `>` | n/a | None; no `_ge_` or `_gt_` |

## Step 3 — All 42 golfing rules

| Rule | Status and reason |
|---|---|
| 1.1 by exact wrapper | n/a: body is already a data term |
| 1.2 by rfl | n/a: no tactic proof |
| 1.3 rw + exact | n/a: no tactics |
| 1.4 simp + exact | n/a: no tactics |
| 1.5 trailing rfl | n/a: no tactics |
| 1.6 constructor chain | n/a: no constructor proof |
| 1.7 apply + exact | n/a: no tactics |
| 1.8 by_contra + push_neg | n/a: no proposition proof |
| 1.9 eta reduction | n/a: no explicit eta-redex; sum binder performs division |
| 1.10 inline have | n/a: no have bindings |
| 1.11 apply + intro | n/a: no tactics |
| 1.12 redundant show | n/a: no show |
| 1.13 have projections | n/a: no have or conjunction |
| 1.14 merge rw | n/a: no rewrites |
| 1.15 unsqueeze terminal simp | n/a: no simp |
| 1.16 squeeze nonterminal simp | n/a: no simp |
| 1.17 dot notation | n/a: expression is notation for summation and division |
| 1.18 use `<|` | n/a: no nested trailing term arguments |
| 1.19 push Not | n/a: no negation tactic |
| 1.20 inline exists helper | n/a: not an existential lemma |
| 2.1 grind | n/a: data definition, not a proof goal; automation would not specify intended data |
| 2.2 remove pre-grind tactics | n/a: no grind |
| 2.3 simpa consolidation | n/a: no proof tactics |
| 2.4 fun_prop | n/a: no analytic proposition |
| 2.5 positivity | n/a: no positivity proof goal |
| 2.6 gcongr | n/a: no inequality proof |
| 2.7 lia / omega | n/a: no arithmetic proposition |
| 2.8 aesop | n/a: real data, not logical proof |
| 2.9 norm_num / norm_cast | n/a: no numeric or cast equality proof |
| 2.10 decide | n/a: no decidable proposition |
| 2.11 field_simp; ring | n/a: division defines data rather than an identity goal |
| 2.12 linear_combination | n/a: no ring-ending proof |
| 2.13 wlog | n/a: no cases |
| 2.14 collapse calc | n/a: no calc |
| 2.15 close multiple goals | n/a: no goals |
| 3.1 erw to rw | n/a: no erw |
| 3.2 fun_prop migration | n/a: no continuity/measurability tactics |
| 3.3 omega to lia | n/a: no omega |
| 3.4 rcases rfl | n/a: no rcases |
| 3.5 automation attributes | n/a: defining data; surrounding lemmas provide simplification API |
| 3.6 simp_all | n/a: no simp_all |
| 3.7 remove limits | n/a: no local limits/options |

## Step 4 — Reflection and experiments

The entire body is already the mathematical formula in one line of term mode. Replacing it
with tactic automation would construct arbitrary real data, not a clearer definition. Thus
`exact?`/`apply?` proof search is inapplicable to the data target. The meaningful generic
alternative was tested by the compiled equality with `Finsupp.weight` above. The existing
formula is shorter and preserves definitional reduction used by callers. No expression
composition, redundant tactic, or helper extraction remains to attempt.

## Step 5 — Verification and gates

- `lean_run_code`: actual type and generic candidate types checked; success true, no timeout.
- Definition isolation: a new scratch `isolatedWeight` using exactly the body and only
  `[Fintype σ]` compiled; `isolatedWeight r d = Roth.weight r d` proved by `rfl`.
- Original-form check: `Roth.weight r d = ∑ j, (d j : ℝ) / r j` proved by `rfl`.
- Axioms: `#print axioms Roth.weight` reports only `propext`, `Classical.choice`, `Quot.sound`.
- Negative drop experiments deliberately failed in scratch only; no source artifacts added.
- Full live-file `lean_diagnostic_messages` returned success true, partial false, timeout false,
  failed dependencies empty, zero errors. Target has zero warnings. Remaining header and later
  theorem warnings are existing work for the file owner/next dedicated workers.
- Actual `/Users/ramin/.elan/bin/lake build Roth.Box` exited 0, 1154 jobs;
  log `/private/tmp/roth-box-d05-module.log`, session 66153.
- `git diff --no-color -- Roth/Box.lean` is empty against worker baseline.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Actual Roth.Box build exited 0 |
| definition_protected | pass | Empty source diff; mathematical body/signature unchanged |
| theorem_statement_protected | pass | No theorem changed |
| structure_gate | pass | One-line data body, no branches/conjunction |
| naming_gate | pass | Descriptive mathematical noun; no forbidden patterns |
| line_packing_gate | pass | Complete measured one-line table above |
| inequality_orientation_gate | pass | Complete zero-occurrence table above |

Overall: pass. Full dependent builds belong to the parent checkpoint owner.

## Step 6 — Result and checklist

Before: 1 declaration line. After: 1. Saved: 0.
Audit issues found: 0. Fixed: 0. Refactoring deferred: 0.
Rules applied: none needed. Gates: pass. Renames queued: none.
Comments preserved: docstring 1/1 unchanged; inline comments none present.
Refactoring needed: none. Source ownership released to parent; no Git mutations performed.

- [x] Step 1 — reference documents read.
- [x] Step 2 — all 24 audit items recorded.
- [x] Step 2.5 — all five search-method statuses recorded with service limitation.
- [x] Step 2.6 — all parameters, weakening experiments, inversion, literature reviewed.
- [x] Step 2.7 — complete codepoint width table.
- [x] Step 2.8 — complete inequality table.
- [x] Step 3 — every one of 42 golfing rules has a reasoned status.
- [x] Step 4 — meaningful alternative tested; data/proof distinction respected.
- [x] Step 5a — full-file LSP completed successfully, no errors.
- [x] Step 5b — actual module build and all diff/content gates pass.
- [x] Step 6a — no rename needed, no sidecar mutation.

Parent checkpoint verification: full `lake build` session 76138 and separate
`lake build Roth.LeanEval` session 34164 both exited 0 against the unchanged source,
confirmed by the file owner before this worker released ownership.
