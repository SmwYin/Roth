# Phase 4 — `Roth.wronskian_eq_zero_iff`

Dedicated worker for the final original declaration, original lines 266–269, current lines 231–234. Baseline: `7f3fa5a`. Only this declaration and this report are owned by this worker. Source ownership was relinquished after source freeze; Git and shared logs belong to the file orchestrator.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md. Also read both Lean 4/mathlib-quality skill instructions, the complete worker contract, relevant style sections and naming conventions. Existing statements, definitions, docstrings and toolchain remain protected.

## Result

Replaced the manual implication-argument swap
`fun hw hli => wronskian_ne_zero_of_linearIndependent hli hw`
with `imp_not_comm.mp wronskian_ne_zero_of_linearIndependent`.
The converse remains the existing project theorem. The proof now names the standard logical equivalence directly. No new declarations or imports.

Before: 4 declaration lines, 2 body lines. After: 4 declaration lines, 2 body lines. Saved: 0 lines, 5 characters. One concrete issue fixed: manual logical argument swap and its legacy lambda arrow. No refactoring or rename required.

## Complete audit

| # | Item | Concrete disposition |
|---|---|---|
| 1 | LINT | No diagnostics in lines 231–234. Complete file diagnostics retain the pre-existing header warning and unused `hφ`/`hd` warnings in another declaration. |
| 2 | HAVE SCAN | No `have`/`let` declarations or hidden single-use bindings. |
| 3 | SET_OPTION | No per-declaration options, heartbeat or recursion overrides. |
| 4 | SIMP SQUEEZE | No simp calls in original or final proof. Bare simp scratch attempt made no progress. |
| 5 | NAMING | `wronskian_eq_zero_iff` describes the vanishing equivalence, is snake_case, and contains no forbidden abbreviation, numeric scheme, numbered auxiliary suffix or single-letter public name. No rename queued. |
| 6 | LINE PACKING | All signature lines measured below; complete conclusion cannot join the first line within 100 codepoints. |
| 7 | BY PLACEMENT | Term proof; no `by` placement issue. |
| 8 | FORMAT | Two-space body/four-space continuation, no internal blank line, no semicolons, no local instances. Legacy `=>` eliminated with the lambda. |
| 9 | COMMENTS | No inline proof comments; all existing module/declaration docstrings preserved byte-for-byte. |
| 10 | DOCSTRING | Existing public documentation states characteristic-zero dependence criterion and source, distinguishing this iff from the one-direction lemmas. No rewrite needed or permitted. |
| 11 | VISIBILITY | Keep public: headline criterion listed among main results, intended as the file's reusable API; not an implementation helper. |
| 12 | STRUCTURE | Main theorem body is 2 lines, below 15-line threshold. No conjunction and no long branch. The two directions already have named lemmas. |
| 13 | MATHLIB | Five-method evidence below: binary polynomial Wronskian is a related but different object. Use core `imp_not_comm` directly for logic. This public mathematical criterion combines project results, not a duplicate wrapper around a mathlib criterion. |
| 14 | JUNK DEF | n/a: theorem, not a definition. |
| 15 | EXISTS LEMMA | n/a: public iff, no existential witness/helper. |
| 16 | SHOW vs CHANGE | Neither occurs. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | Mechanical probes and literature below. Existing field-based definition prevents immediate field weakening; characteristic zero needed by hard-direction lemma. No approved/needed public API extension. |
| 19 | INEQUALITY | No order inequalities in signature or hypotheses; zero reversed occurrences, table below. |
| 20 | NORMAL-FORM | `wronskian φ = 0 ↔ ¬ LinearIndependent K φ` is the appropriate vanishing-to-dependence rewriting form. No alternate normal-form theorem added. |
| 21 | SYNTAX-GEN | OK: implicit family and inference of K/l allow direct rewriting; existing directional API already handles applications with independence/dependence evidence. |
| 22 | IMPORT-FANOUT | n/a: no new imports; core logic lemma already available. |
| 23 | CASTS | 0 dropped / 0 cross-type / 0 load-bearing ascriptions in diff. |
| 24 | INSTANCE-NAME | n/a: theorem introduces no instances. |

Issues fixed: direct implication-swap API replaces manual lambda. Refactoring needed: none.

## Line packing

Actual `#check` at `format.width := 100`:

```text
@wronskian_eq_zero_iff : ∀ {K : Type u_1} [inst : Field K] {l : ℕ} [CharZero K] {φ : Fin l → K[X]},
  wronskian φ = 0 ↔ ¬LinearIndependent K φ
```

Before and after signature identical:

| Signature line | Codepoints | Next complete signature unit | Arithmetic | Action |
|---|---:|---|---|---|
| 231 | 63 | `wronskian φ = 0 ↔ ¬ LinearIndependent K φ :=` (44) | 63 + 1 + 44 = 108 > 100 | ok |
| 232 | 48 | No next signature line; proof follows | n/a | ok |

Final proof-line widths: 58 and 47. The complete constructor cannot fit on one 100-codepoint line. All target lines ≤ 100.

## Inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 0 | Signature and all hypotheses | No `<`, `≤`, `>`, or `≥` order predicates | None | Name has no `_ge_`/`_gt_` |

## Mathlib search status

- **A — Lean-Finder:** actual query “Wronskian of polynomials vanishes if and only if linearly dependent”; returned `Polynomial.wronskian_self_eq_zero`, `wronskianBilin_apply`, `wronskian_eq_of_sum_zero`, `wronskian_zero_right`. These concern the binary polynomial Wronskian.
- **B — Loogle:** actual `"wronskian"` query returned `Polynomial.wronskian` and self/negation lemmas, again the binary construction.
- **C — LeanSearch:** unavailable due the previously established service HTTP 500 in this sequential file audit; parent explicitly instructed not to repeat the failed service probe. This is a capability limitation, not evidence of absence.
- **D — source:** untruncated `rg -n 'wronskian|imp_not_comm'` in the located Wronskian/basic logic files. `Mathlib/RingTheory/Polynomial/Wronskian.lean` has binary Wronskian and `IsCoprime.wronskian_eq_zero_iff` (both derivatives zero under coprimality), not this family criterion. Initial guessed source paths were absent; `rg --files` located the actual files and search was rerun. No absence conclusion was drawn from missing paths.
- **E — local name search:** actual searches `wronskian`, `not_imp_comm`, `imp_not_comm`; found the project family API, mathlib's binary API and core `imp_not_comm`. Local index reported warming/unavailable; positive source matches verified with compiled `#check`, not interpreted as exhaustive negative evidence.

Auxiliary variants reviewed: `wronskian_eq_zero_iff`, `wronskian_self_eq_zero`, `wronskian_eq_of_sum_zero`, the two project directional lemmas, `not_imp_comm` and `imp_not_comm`. Common-equivalents lookup: no discrete/finite/separation/custom-predicate match. `#check @imp_not_comm` verified `∀ {a b : Prop}, (a → ¬b) ↔ (b → ¬a)`.

Conclusion: related partial mathlib match, retained public family theorem while using the existing generic logic API. No categorical “mathlib lacks this” claim is made given the unavailable search endpoint. No new declaration is being justified from search absence. In imported scratch, `exact?` and `apply?` found the existing `wronskian_eq_zero_iff` itself; rejected as circular replacement evidence. No extraction signals: proof already two direct terms, no casts/plumbing or ugly unfolding.

Six strict rules: no new mathlib wrapper; capability limitation explicit; auxiliary variants searched; existing `LinearIndependent`/typeclasses used; no duplicate identified for deletion; new logic fact is core and no file-level mathematical dependency/documentation change needed.

## Generalisation status

| Parameter/hypothesis | Kind | Mechanical candidates tried/considered | Verified result |
|---|---|---|---|
| `{K : Type*}` | Type/universe | Drop type binder would merely auto-generalize K; universe already polymorphic | No mathematical weakening; existing `#check` confirms universe polymorphism |
| `[Field K]` | Typeclass | Drop; replace by `DivisionRing`; replace by `CommRing`; predicate-class `[CommRing K] [IsField K]` would require installing/reconciling field data, so is a restatement rather than a direct weakening | Actual scratch probes: drop fails `Semiring K`/`Field K`; division ring and commutative ring cannot elaborate existing field-based `wronskian φ` (polynomial instance mismatch). No source edits |
| `{l : ℕ}` | Value/index | Drop explicit binder only auto-generalizes l; arbitrary l already includes empty family | No restriction to weaken; changing Fin l to arbitrary indexing changes the definition and API |
| `[CharZero K]` | Typeclass | Drop test | Actual scratch proof fails `failed to synthesize CharZero K` at the hard-direction lemma |
| `{φ : Fin l → K[X]}` | Structure value/family | Drop binder only auto-generalizes φ; no attached nonzero/injective hypothesis to drop/localize | Arbitrary family already; power series/rational functions require a different object/API |

There are no explicit propositional assumptions, decidability parameters, strict order bounds, pointwise/global analytic assumptions, bundled equivalences, or unused proof hypotheses. No mechanical weakening survived. This is evidence about the existing API/proof, not a claim that no more general mathematical theorem exists.

Inversion check: the result assembles the two existing domain-specific directions; it performs no unfolding followed by object-independent substantive proof. The only abstract logic was the swap of two implications, supplied directly by `imp_not_comm`; adding another abstract wrapper would duplicate core logic.

## Public literature search

Actual web query: “Wronskian polynomials characteristic zero linear independence generalization Bostan Dumas”. Top three primary hits:

1. [Bostan–Dumas, Wronskians and linear independence, arXiv](https://arxiv.org/abs/1301.6598), opened successfully; analytic-function statement.
2. [Author PDF at mathexp.eu](https://mathexp.eu/dumas/publications/Bostan_Dumas_2010_WLI.pdf), search excerpt discusses the characteristic-p counterexample.
3. [Author PDF at INRIA](https://specfun.inria.fr/bostan/publications/BoDu09.pdf), search excerpt states power-series/rational-function generality. Opening this mirror timed out; no unseen full-text claim is used.

These are broader settings, requiring a different Wronskian object/API. Search excerpts also explicitly indicate that characteristic zero cannot be dropped for the ordinary criterion (1 and X^p in characteristic p). This supports keeping the current characteristic-zero criterion; the immediate Lean drop test independently fails. No current caller benefit warrants a fresh power-series/differential-field development. No new generalisation proposal or user decision is pending. ChatGPT math MCP: n/a, no such tool in exposed tool inventory.

## All 42 golfing rules

| Rule | Status |
|---|---|
| 1.1 by exact | n/a: original/final are term constructors |
| 1.2 by rfl | n/a: no reflexivity block |
| 1.3 rw + exact | n/a: no rewriting |
| 1.4 simp + exact | n/a: no simplification sequence |
| 1.5 trailing rfl | n/a: none |
| 1.6 constructor chain | Already anonymous constructor with two direct directions |
| 1.7 apply + exact | n/a: no tactic application chain |
| 1.8 by_contra + push_neg | n/a: no contradiction tactic |
| 1.9 eta reduction | Original lambda swaps arguments, so not a plain eta reduction; replaced with `imp_not_comm.mp`, eliminating both binders |
| 1.10 inline have | n/a: no bindings |
| 1.11 apply + intro | n/a: no apply/intro |
| 1.12 redundant show | n/a: none |
| 1.13 have projections | n/a: none |
| 1.14 merge rw | n/a: none |
| 1.15 terminal simp only | n/a: no simp |
| 1.16 nonterminal simp | n/a: no simp |
| 1.17 dot notation | Applied `imp_not_comm.mp`; existing project theorem names take no object argument suited to dot notation |
| 1.18 trailing parentheses | n/a: none |
| 1.19 push_neg | n/a: none |
| 1.20 trivial exists helper | n/a: iff, no witness/helper |
| 2.1 grind | Actual isolated hinted grind closes. Two explicit premises still required; kept deterministic direct constructor/logic term, which is already term-mode and avoids tactic search |
| 2.2 pre-grind deletion | n/a: no existing grind/tactic prefix |
| 2.3 simpa consolidation | Bare simp tested: no progress; no simp/exact chain to consolidate |
| 2.4 fun_prop | n/a: no analytic function-property goal |
| 2.5 positivity | n/a: target is iff, not structural positivity/nonzero arithmetic |
| 2.6 gcongr | n/a: no ordered inequality/congruence chain |
| 2.7 lia/omega | n/a: no arithmetic proposition |
| 2.8 aesop | Actual hinted aesop exhausts search with forward False goal; rejected |
| 2.9 norm_num/norm_cast | n/a: no numeric/cast calculation |
| 2.10 decide | n/a: arbitrary polynomial family/field and mathematical dependence, not a finite decidable computation |
| 2.11 field_simp/ring | n/a: no denominator identity |
| 2.12 linear_combination | n/a: no ring-ending proof or scalar equations |
| 2.13 wlog | n/a: no duplicated symmetric cases |
| 2.14 calc term | n/a: already term, no calc |
| 2.15 multiple-goal combinator | Two distinct mathematical directions; direct constructor preferred to introducing tactic subgoals |
| 3.1 erw | n/a: no rewrites |
| 3.2 continuity/measurability | n/a: none |
| 3.3 omega to lia | n/a: no arithmetic tactic |
| 3.4 rcases rfl | n/a: none |
| 3.5 automation registration | Considered: existing public rewrite theorem can be selected explicitly; no demonstrated caller benefit for adding global simp/grind attributes or changing normal forms |
| 3.6 simp_all only | n/a: none |
| 3.7 limits | n/a: no limits in source |

## Experiments and reflection

Native `lean_multi_attempt` at the term constructor was attempted; it inserted tactic snippets in term syntax and produced unknown-identifier/remaining-constructor errors. These were tool-position failures, not mathematical failures, and the source was untouched. Actual isolated `lean_run_code` experiments then tested the candidate, hinted grind, hinted aesop, bare simp, exact? and apply?. Initial aesop argument-list syntax was rejected and corrected; the corrected tactic failed logically at the forward direction. No failed code entered source.

The shorter standard logic term compiled. The first standalone theorem equality check exposed scratch binder order `[CharZero K] {l}` versus the original `{l} [CharZero K]`; corrected scratch order, then full theorem equality by `rfl` compiled. This scratch correction did not change production code. Final isolated snippet returned `success: true`, `timed_out: false`; only informational output, including an LSP import freshness notice while the independent module build had completed. Final module build and complete live diagnostics independently establish source validity.

Step-back: both directions already exist. No alternative algebraic proof is warranted. Core implication commutation is exactly the missing abstraction in the old lambda and needs no new helper. The constructor communicates the two mathematical directions directly. Retained API and public name are already appropriate; no speculative generalisation/extraction task added.

## Verification gates

- Actual command `/Users/ramin/.elan/bin/lake build Roth.Wronskian > /private/tmp/roth-wronskian-iff-module.log 2>&1`, session 17133, exited 0. 1826 jobs; Wronskian built in 18 seconds. Only the existing header and earlier unused-hypothesis warnings.
- Native `lean_diagnostic_messages` for complete `Roth/Wronskian.lean`, timeout 30: `success: true`, `partial: false`, `timed_out: false`, no failed dependencies. Same three pre-existing warnings, none in target.
- Isolated final theorem has same complete binder order/type, and `example : @Roth.wronskian_eq_zero_iff = @wronskianIffAudit := rfl` succeeds.
- `#print axioms wronskianIffAudit` and original target: only `propext`, `Classical.choice`, `Quot.sound`.
- Actual `git diff --check` exited 0. Programmatic source comparisons confirm exact target signature and all existing docstrings unchanged, target has no sorry/admit/axiom/options/instance/scaffolding tokens. Diff changes exactly one proof line.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Module command exited 0, log/session above |
| definition_protected | pass | No definition/abbreviation changes |
| theorem_statement_protected | pass | Signature byte-for-byte identical |
| structure_gate | pass | Main body 2 lines ≤15; no conjunction or long branch |
| naming_gate | pass | Descriptive mathematical snake_case name, no forbidden patterns |
| line_packing_gate | pass | Both signature rows measured above |
| inequality_orientation_gate | pass | No reversed order predicates |
| comments/docs | pass | Existing comments/docstrings preserved |
| proof integrity | pass | Isolated proof, type equality, standard axioms, no admissions |
| docstring_only_changes | n/a | Normal cleanup scope includes proof edits |
| cumulative dependent builds | parent-owned | Full `lake build` then separate `lake build Roth.LeanEval` run by file orchestrator after source freeze; results recorded in shared checkpoint |

Overall worker gates: pass. Source frozen; no later source edits allowed without renewed ownership. Renames queued: none. Refactoring needed: none. Comments preserved: no inline comments present; all docstrings unchanged.

## Phase checklist

- [x] Step 1 — required reference documents read.
- [x] Step 2 — full audit, all 24 items.
- [x] Step 2.5 — five-method search block and capability limits.
- [x] Step 2.6 — every parameter/hypothesis, mechanical probes, inversion and public literature.
- [x] Step 2.7 — complete signature width table.
- [x] Step 2.8 — inequality occurrence table.
- [x] Step 3 — all 42 rules with statuses/reasons.
- [x] Step 4 — alternative approaches and reflection.
- [x] Step 5a — complete native diagnostics clean of new errors/warnings.
- [x] Step 5b — module build and all diff/content gates passed.
- [x] Step 6a — no rename needed; no queue mutation.
