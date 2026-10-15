# Box declaration 10: `Roth.weight_single`

Worker: fresh dedicated `decl10`; baseline `d51137b`; file `Roth/Box.lean`.
Original declaration lines 95–97; final lines 96–98, with scoped `omit` at 94.
Ownership: this declaration and this report only; no Git or shared-report mutations.

## References and mathematical understanding

Read the complete declaration-worker prompt, Lean skill, mathlib-quality skill,
`golfing-rules.md`, `proof-patterns.md`, `mathlib-search.md`,
`generalisation-patterns.md`, and `cleanup-gates.md`; read applicable style sections
on formatting, documentation, visibility, declaration layout, and tactics.

A vector supported at `j` with coefficient `n` has only one potentially nonzero
summand in its weighted sum, namely `n / r j`. This remains true when `r j = 0`,
using total real division. The proof unfolds the weight and single-coordinate
function, distributes division through its conditional, and simplifies the sum.

User-approved action: remove verified unnecessary `DecidableEq` assumptions in
Box, preserving mathematical conclusions. Applied scoped `omit [DecidableEq σ] in`
before the unchanged docstring and local `classical` inside the proof. Also packed
the two-line signature into one line. No other API change.

## Full audit

1. **LINT:** original target has one `unusedDecidableInType` warning. Final complete
   LSP has no target warnings or errors; 11 warnings remain in other declarations
   and the known header. The user chose to leave the header metadata unchanged.
2. **HAVE SCAN:** no `have` declarations, hence no single-use bindings to inline.
3. **SET_OPTION:** no declaration options or resource-limit changes.
4. **SIMP SQUEEZE:** one terminal `simp [weight, Finsupp.single_apply, ite_div]`;
   preserve unsqueezed. Omitting either latter ingredient does not close the goal.
5. **NAMING:** `weight_single` describes weight evaluated on `Finsupp.single`, is
   snake_case, and matches no forbidden number/scheme/abbreviation pattern. No rename.
6. **LINE PACKING:** original signature had 51 and 49 codepoints; after removing
   continuation indentation, the entire declaration signature is 97. Repacked.
7. **BY PLACEMENT:** `by` remains at the end of the signature.
8. **FORMAT:** two-space proof indentation, no blank proof lines or semicolons;
   no `haveI`/`letI`, redundant syntax, or whitespace defects.
9. **COMMENTS:** no inline comments existed (0 → 0); none removed or relocated.
10. **DOCSTRING:** one-sentence mathematical single-coordinate interpretation;
    preserved byte-for-byte, including `n • e_j` notation.
11. **VISIBILITY:** public: actual external uses occur in `Lattice.lean:160` and
    `Theta.lean:386`. Making this private would break the API.
12. **STRUCTURE:** final proof has two lines (`classical`, terminal `simp`), no
    conjunction or branches; no helper/decomposition needed.
13. **MATHLIB:** five-method table below. The Finsupp weight API is related, but
    deleting the Roth theorem requires representation changes beyond this scope.
14. **JUNK DEF:** n/a: a theorem, no definition introduced or changed.
15. **EXISTS LEMMA:** n/a: no existential conclusion or witness helper.
16. **SHOW vs CHANGE:** n/a: neither occurs.
17. **PUSH_NEG:** n/a: no negation-pushing tactic.
18. **GENERALISE:** verified removal of DecidableEq; Fintype drop fails elaboration.
    Explicit `r`, `j`, `n` are data occurring in the conclusion; see full table below.
19. **INEQUALITY:** no inequality occurs; required scan table below.
20. **NORMAL-FORM:** evaluation of weight on a single reduces to its scalar value;
    already a natural rewrite orientation. No new equivalence network.
21. **SYNTAX-GEN:** OK: direct equality rewrites actual Lattice/Theta uses; no bundled
    hypotheses or unnecessary explicit proof arguments.
22. **IMPORT-FANOUT:** n/a: imports unchanged. Avoid importing field automation just
    to replace a successful elementary simplifier proof.
23. **CASTS:** 0 dropped / 0 kept as explicit cross-type / 0 kept as load-bearing in
    the diff. Existing implicit natural-to-real casts are necessary mathematical casts.
24. **INSTANCE-NAME:** n/a: no instance declaration; local `classical` supplies proof
    decidability without exporting an instance or adding an API parameter.

Issues found: unnecessary decidability parameter and underpacked signature; both fixed.
Refactoring needed: none within the authorized scope. No rename queue entries.

## Mathlib search status

| Method | Query/evidence | Result |
|---|---|---|
| A Lean-Finder | finite sum of a finitely supported single function divided by coordinate weights | `Finsupp.weight_apply`, affine combination and centroid sum lemmas |
| B Loogle | `Finsupp.single, Finset.sum` | `Finsupp.univ_sum_single_apply`, primed variant, `coe_univ_sum_single` |
| C LeanSearch | inherited service availability probe from this Box session | HTTP 500 unavailable; parent explicitly requested no repeated remote stalls; not evidence of absence |
| D source search | untruncated `rg` for full `Finsupp.weight_single`, theorem/lemma `weight_single`; inspect `Data/Finsupp/Weight.lean:70–105` and `Data/Finsupp/Basic.lean` | found `weight_single`, `weight_single_index`, `weight_single_one_apply`, `weight_eq_sum`; verified `single_apply` and `ite_div` types |
| E local name search | `sum_single` | Finsupp/DFinsupp sum-single APIs returned from source; symbol index reported unavailable, so no absence claim |

Auxiliary variants: `_single_index`, `_single_one_apply`, `_univ_sum_single_apply`,
primed single-apply sum, `_eq_sum`, `_apply`. Common-equivalents table: no matching
specialized bucket. General scalar-weight evaluation is present as
`Finsupp.weight_single`; it concerns `Finsupp.weight : (σ →₀ R) →+ M`, whereas this
API concerns the existing `Roth.weight : (σ → ℕ) → (σ →₀ ℕ) → ℝ`.

Conclusion: partial mathematical match. Keep the established public Roth theorem
and use existing simplification primitives. No claim that the abstract result is
absent from mathlib, no new wrapper or abstraction introduced. The user preserved
Roth definitions/conclusions and approved only the specified assumption removals.
Replacing all weights with bundled linear combinations would exceed that scope.
Live `exact?` could not close this goal; `apply?` supplied only partial equality or
division transformations requiring further proofs, not a replacement theorem.

## Generalisation status

| Parameter | Class | Role | Candidate/drop analysis | Verified result |
|---|---|---|---|---|
| `{σ : Type*}` | type variable | coordinate domain | already universe-polymorphic; dropping leaves all coordinate data untyped | retain; no universe restriction to weaken |
| `[Fintype σ]` | typeclass | index of defining sum | drop in independent snippet | fails `failed to synthesize Fintype σ` at `Roth.weight`; retain |
| `[DecidableEq σ]` | decidability | only proof conditional evaluation | drop, supply local `classical` | independent proof and actual module/LSP pass; removed |
| `(r : σ → ℕ)` | data | denominator at every coordinate and RHS | drop would remove a named argument used twice in statement; no proposition to weaken | retain; changing ℕ requires redesign of weight definition |
| `(j : σ)` | data | support coordinate, RHS denominator index | drop leaves single and `r j` unbound | retain arbitrary coordinate |
| `(n : ℕ)` | data | coefficient and RHS numerator | drop leaves coefficient unbound | retain arbitrary coefficient including zero |

There are no positivity, nonzero, strict/weak, pointwise/global, or bundled
propositional hypotheses here. A `[Finite σ]` replacement would require choosing a
Fintype in the statement, since `Roth.weight` takes Fintype; this changes how the
public definition is instantiated rather than removing an unused assumption.

Inversion check: the concrete weight unfolds once, after which the proof is the
abstract single-summand sum identity. That general result already belongs to the
Finsupp/big-operator APIs found above; no new abstract lemma is warranted. Broader
codomain generalisation would change the fixed-real Roth definition, outside the
approved removal. Big-change candidates selected for action: none.

### Public literature search

Web query: `weighted sum standard basis vector coordinate linear functional generalization`.
Top three hits recorded: [coordinate functional discussion](https://math.stackexchange.com/questions/1876953/question-about-coordinates-in-linear-functionals),
[Functions are Vectors](https://thenumb.at/Functions-are-Vectors/), and
[Schauder basis](https://en.wikipedia.org/wiki/Schauder_basis). These frame the
single-coordinate result as evaluation on basis vectors; the infinite-dimensional
Schauder extension adds convergence issues and is not needed here. The primary
textbook [Introduction to Applied Linear Algebra](https://www-leland.stanford.edu/~boyd/vmls/vmls.pdf)
was also returned, describing fixed-weight inner products as linear functions.
This supports the abstract linear-evaluation viewpoint; it supplies no missing
hypothesis requirement for this finite elementary identity. No quotation copied.
ChatGPT math MCP: unavailable (no matching callable tool). No literature-driven
change selected beyond the already verified decidability removal.

## Line-packing artifact

Baseline width reference and final `#check @Roth.weight_single` at `format.width 100`
were actually run. Final elaborated type:

```lean
@Roth.weight_single : ∀ {σ : Type u_1} [inst : Fintype σ] (r : σ → ℕ) (j : σ) (n : ℕ),
  Roth.weight r (Finsupp.single j n) = ↑n / ↑(r j)
```

| Version / signature line | Codepoints | Next signature chunk | Arithmetic | Action |
|---|---:|---|---|---|
| Before L95 | 51 | conclusion plus `:= by`, 45 after indentation | 51 + 1 + 45 = 97 ≤ 100 | repack, applied |
| Before L96 | 49 | none | n/a | final line |
| After L96 | 97 | none; proof follows | n/a | ok |

## Inequality scan artifact

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| — | full signature and all hypotheses | no ≥ or >, indeed no inequalities | n/a | none; no `_ge_`/`_gt_` name |

## All 42 golfing rules

- [1.1] n/a: no `by exact` wrapper.
- [1.2] n/a: no `by rfl`; identity needs finite-sum simplification.
- [1.3] n/a: no `rw` followed by `exact`.
- [1.4] n/a: terminal simp has no following exact/assumption.
- [1.5] n/a: no trailing `rfl`.
- [1.6] n/a: no constructor proof.
- [1.7] n/a: no apply/exact chain.
- [1.8] n/a: no contradiction proof.
- [1.9] n/a: no lambda expression.
- [1.10] n/a: no `have` binding.
- [1.11] n/a: no apply/intro sequence.
- [1.12] n/a: no show expression.
- [1.13] n/a: no projected conjunction binding.
- [1.14] n/a: no rewrite sequence.
- [1.15] already satisfied: terminal simp is unsqueezed.
- [1.16] n/a: no nonterminal simp.
- [1.17] n/a: no lemma application improved by dot notation.
- [1.18] n/a: no trailing function-argument parentheses.
- [1.19] n/a: no push_neg.
- [1.20] n/a: no private existential lemma.
- [2.1] tried live `grind`: failed; it cannot establish the weighted-single identity.
- [2.2] n/a: selected proof contains no grind.
- [2.3] n/a: no final tactic after simp to consolidate.
- [2.4] n/a: no continuity/differentiability/measurability goal.
- [2.5] n/a: equality of weighted sums, not a sign goal.
- [2.6] n/a: no monotonicity inequality.
- [2.7] n/a: this is a real finite-sum identity, not Nat/Int linear arithmetic.
- [2.8] tried live `aesop`: failed, made no progress.
- [2.9] n/a: no concrete numerical computation or isolated cast equality.
- [2.10] n/a: equality over arbitrary real-valued sums is not finite decidable computation.
- [2.11] tried live `field_simp` then ring: field_simp unavailable under existing imports;
  no new import justified because the conditional sum needs simp first anyway.
- [2.12] n/a: no ring-ending proof or algebraic hypotheses to combine.
- [2.13] n/a: no symmetric branches.
- [2.14] n/a: no calc chain.
- [2.15] n/a: no multiple generated goals in selected proof.
- [3.1] n/a: no erw.
- [3.2] n/a: no legacy continuity/measurability tactic.
- [3.3] n/a: no omega; arithmetic tactic not needed as explained in 2.7.
- [3.4] n/a: no rcases or substitution.
- [3.5] considered: this rewrite could be simp-friendly, but existing callers explicitly
  rewrite it; no automation attribute change is needed or introduced.
- [3.6] n/a: no simp_all only.
- [3.7] already satisfied: no maxHeartbeats or other limit override.

## Live experiments and reflection

Native `lean_multi_attempt` at original line97 tested eight candidates with no timeout:
`simp [weight]` failed on the single-coordinate sum; adding `Finsupp.single_apply`
left a conditional divided by the coordinate denominator; adding `ite_div` closes.
`grind`, `aesop`, and `exact?` failed. `apply?` gave only partial suggestions
(`Real.ext_cauchy` or division lemmas); any temporary sorry in that unsuccessful
probe is not in the source. `field_simp` was unavailable in current imports.

Selected proof retains the necessary terminal simp. Local classical is required
for conditional evaluation once the unused exported instance is removed. A term
proof via Finsupp.weight would add a representation bridge and import, so is not
shorter or clearer here. No repeated proof logic, redundant haves, helper needs,
or alternative one-step direct theorem found for this unchanged Roth definition.

## Verification and gates

- Actual `/Users/ramin/.elan/bin/lake build Roth.Box` process session20186 exited0;
  1154 jobs, log `/private/tmp/roth-box-d10-module.log`.
- Complete final `lean_diagnostic_messages` returned `success=true`, `partial=false`,
  `timed_out=false`, no failed dependencies, zero errors and zero target warnings.
  Eleven unrelated future-declaration/header warnings remain; none suppressed.
- Native `lean_verify Roth.weight_single` found only `propext`, `Classical.choice`,
  `Quot.sound`, with no nonstandard axioms or source scan warnings.
- Fresh independent `example` reproved the conclusion using only weight, single_apply,
  ite_div and local classical, without calling weight_single or assuming DecidableEq.
- A second independent example called the final theorem without DecidableEq and compiled.
- Final actual `#check` confirms only the approved DecidableEq removal; explicit
  arguments, order, universe polymorphism, Fintype and mathematical conclusion remain.
- `git diff --check` exited0. Focused diff changes only target omit/layout/classical;
  all docstring bytes and surrounding declarations preserved.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | actual module command exit0/1154 jobs |
| definition_protected | pass | no definition/abbreviation changes |
| theorem_statement_protected | pass | only approved instance removal; conclusion and explicit arguments unchanged; whitespace packing |
| structure_gate | pass | two proof lines, no branches/conjunction |
| naming_gate | pass | descriptive snake_case, no forbidden pattern |
| line_packing_gate | pass | sole final signature line97 codepoints; complete table above |
| inequality_orientation_gate | pass | required scan table, zero reversed inequalities |
| trust / isolation | pass | standard3 axioms, independent proof compiled |
| comments / scope | pass | docstring unchanged, 0 inline comments before/after, target-only diff |

Full-project and separate LeanEval builds, then commit/push, belong to the parent
checkpoint and are not asserted by this leaf report.

## Result and checklist

Before:3 declaration lines. After:3 declaration lines; one added scoped omit line.
Saved:0 declaration lines; signature packing offsets the local classical line.
Audit issues found:2. Fixed:2. Refactoring deferred:0. Renames queued:none.
Rules applied: formatting/line packing and approved mechanical instance weakening;
terminal simp preserved after failed shorter alternatives.

- [x] Step1 references read.
- [x] Step2 all24 audit items recorded.
- [x] Step2.5 five-method search status and auxiliary variants recorded.
- [x] Step2.6 every parameter, mechanical weakening, inversion and public literature recorded.
- [x] Step2.7 every signature line measured and final layout packed.
- [x] Step2.8 inequality scan table recorded.
- [x] Step3 all42 golfing rules have concrete statuses.
- [x] Step4 independent strategic reflection and live alternatives completed.
- [x] Step5a complete final LSP clean for the target.
- [x] Step5b actual module build, diff, type, axiom and isolation gates passed.
- [x] Step6a no rename required; no sidecar change.
- [x] Step6 report complete; source ownership released to parent.

Publication verification: full `lake build` session 41056 exited 0 (2586 jobs;
`/private/tmp/roth-box-d10-full.log`); separate `lake build Roth.LeanEval` session 58453
exited 0 (2585 jobs; `/private/tmp/roth-box-d10-leaneval.log`). All affected dependents pass.
