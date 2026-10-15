# Cleanup audit: `MvPolynomial.hasseDeriv_zero_apply`

Date: 2026-10-15 (America/Chicago). Baseline: pushed checkpoint `6ab3654`.
Target: `Roth/HasseDeriv.lean:106`. Reviewed and retained without source changes.
The existing coefficient-extensionality proof is short and clear. An isolated
attempt to replace it with direct simplification of the definition failed; the
failed experiment was never applied to the source.

## Workflow and all 24 audit items

Dedicated Phase 4 worker following the inherited mathlib-quality/lean4 workflow
and reference review. Native Lean MCP tools are absent from this leaf registry;
the orchestrator supplied actual remote-search evidence. Direct MCP 0.31.0
bridge provided local search, live goals, isolated experiments and diagnostics.

| # | Item | Disposition |
|---|---|---|
| 1 | LINT | Fresh complete diagnostics: no errors; existing header warning only. |
| 2 | HAVE SCAN | No have bindings. |
| 3 | SET_OPTION | No options present or added. |
| 4 | SIMP SQUEEZE | Terminal simp already follows recommended style; retained. |
| 5 | NAMING | zero_apply distinguishes pointwise form from following bundled zero theorem. |
| 6 | LINE PACKING | Complete signature is 79 characters; no avoidable continuation. |
| 7 | BY PLACEMENT | by is already on the signature line. |
| 8 | FORMAT | Two-space indentation; no whitespace defect. |
| 9 | COMMENTS | No proof comments to improve; source citation preserved. |
| 10 | DOCSTRING | Correct pointwise identity and related theorem link. |
| 11 | VISIBILITY | Used in Index and to construct bundled identity; retain public API. |
| 12 | STRUCTURE | Two simple proof steps; no extraction. |
| 13 | MATHLIB | Five search methods attempted; analogous representations checked. |
| 14 | JUNK DEF | Theorem, no definition introduced. |
| 15 | EXISTS LEMMA | No existential statement. |
| 16 | SHOW vs CHANGE | Neither present. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | All parameters and inversion reviewed below; no API change. |
| 19 | INEQUALITY | No inequalities in target statement or proof. |
| 20 | NORMAL-FORM | Simplifies zero-order derivative to original polynomial. |
| 21 | SYNTAX-GEN | No custom syntax or disguised predicate. |
| 22 | IMPORT-FANOUT | No imports changed or needed. |
| 23 | CASTS | No explicit target casts: 0 dropped / 0 retained / 0 added. |
| 24 | INSTANCE-NAME | Not an instance declaration. |

## Signature width and inequality tables

Measured Unicode codepoint lengths with Python len.

| Signature line | Before | After | Next unit | Arithmetic/action |
|---|---:|---:|---|---|
| 106: complete theorem, binders, conclusion and := by | 79 | 79 | First tactic ext e (5 unindented characters) | No continuation to pack; 79 + 1 + 5 = 85 would fit, but tactic bodies remain on their own indented lines; ok. |

The proof lines have lengths 7 and 37. No signature wraps, split binders,
blank lines inside the declaration or lines over 100 columns occur.

| Scope | Inequalities | Action |
|---|---|---|
| Statement | None; equality only | No orientation change. |
| Proof | None; coefficient equality | No orientation change. |

## Five-method mathlib search

| Method | Query/scope | Observed result |
|---|---|---|
| A Lean-Finder | zero order Hasse derivative is identity polynomial | Polynomial.hasseDeriv_zero', Polynomial.hasseDeriv_zero, LaurentSeries.hasseDeriv_zero. |
| B Loogle | "hasseDeriv_zero", limit 5 | Same three analogues. |
| C LeanSearch | Hasse derivative order zero equals original polynomial | HTTP 500; unavailable, not evidence of absence. |
| D Pinned source/project | hasseDeriv_zero / hasseDeriv_zero_apply | Inspected univariate and Laurent-series source, target and callers in Index. |
| E Local MCP | hasseDeriv_zero, limit 20 | Same library declarations and current project declarations; index unavailable, source matching works. |

Evidence: `/private/tmp/roth-hasseDeriv_zero_apply-native-search.json` and
`/private/tmp/roth-hasseDeriv_zero_apply-local.json`. Pinned
`Mathlib/Algebra/Polynomial/HasseDeriv.lean:82` proves the univariate pointwise
identity using the expansion formula and sum_monomial_eq; line 86 packages it
as a linear-map identity. `Mathlib/RingTheory/LaurentSeries.lean:139` uses
extensionality and simp for its different Laurent-series representation.
Neither theorem has the multivariate polynomial type needed here.

Replacement checklist: inspected actual callers in `Roth/Index.lean:107–108`
and the following `hasseDeriv_zero`; five methods attempted; both bundled and
pointwise formulations checked; no custom predicate, topology or separation
alias involved. The same-file bundled identity depends on this target, so using
it to shorten the target would be circular. Rebuilding the theorem through a
univariate encoding would add unnecessary representation conversions. The
current coefficient theorem and mathlib extensionality already supply the
appropriate abstraction. Bounded search does not establish exhaustive absence.

## Parameters, generalisation, inversion and literature

| Parameter/context | Assessment |
|---|---|
| `{σ : Type u}` | Arbitrary variables, including empty/infinite types; no finiteness or nonemptiness restriction. |
| `{R : Type v}` | Arbitrary universe; no characteristic restriction. |
| `[CommSemiring R]` | Required by the current multivariate polynomial and linear-map construction; weakening the underlying representation is outside this theorem cleanup. |
| `(P : MvPolynomial σ R)` | Arbitrary polynomial, including zero; essential argument. |

No propositional hypothesis is available to drop, weaken or localize. The result
already applies beyond the finite-variable field setting of typical literature.
The same statement with a bundled identity is the next existing declaration;
there is no missing generalization to add here. Inversion review: the underlying
principle is that a linear endomorphism fixing every coefficient is the identity.
Mathlib extensionality and the existing coefficient formula express precisely
that principle. No additional helper or structural redesign is warranted.

Local `clean.tex` §1 defines the operator through binomial coefficients and linear
extension; at zero order each factor is one and each exponent is unchanged.
A fresh public-source inspection of §2.1, Definition 2, p.6 of
[Dvir–Kopparty–Saraf–Sudan, Extensions to the Method of Multiplicities](https://eccc.weizmann.ac.il/report/2009/004/download/)
confirmed the coefficient-of-Z definition via P(X + Z). Inference from that
definition: the coefficient at Z^0 is P(X), matching this result. The paper is
not claimed to prove a Lean-specific commutative-semiring formulation. Optional
ask_chatgpt_math skipped as authorized. No new substantial proposal is queued;
the earlier hasseCoeff parameter-definition proposal remains unapplied.

## All 42 golfing rules

| Rule | Disposition |
|---|---|
| 1.1 by exact | No redundant wrapper. |
| 1.2 by rfl | Coefficient identity is proved, not a definitional equality; no by rfl wrapper. |
| 1.3 rw + exact | None. |
| 1.4 simp + exact | None. |
| 1.5 trailing rfl | None. |
| 1.6 constructor chain | None. |
| 1.7 apply + exact | None. |
| 1.8 by_contra + push_neg | None. |
| 1.9 eta reduction | No lambda. |
| 1.10 single-use have | None. |
| 1.11 apply + intro | None. |
| 1.12 redundant show | None. |
| 1.13 have projections | None. |
| 1.14 merge rw | No rw calls. |
| 1.15 terminal simp only | Terminal simp already unrestricted with the necessary explicit definitions. |
| 1.16 nonterminal simp | None. |
| 1.17 dot notation | No applicable function application. |
| 1.18 `<\|` | No nested application requiring parentheses. |
| 1.19 push Not | No push_neg. |
| 1.20 trivial existential | None. |
| 2.1 grind | Deterministic ext/simp already closes; search adds no benefit. |
| 2.2 delete before grind | No grind. |
| 2.3 simpa consolidation | No preceding equality chain to consolidate; direct simp experiment failed. |
| 2.4 fun_prop | No function-property goal. |
| 2.5 positivity | No positivity goal. |
| 2.6 gcongr | Equality, not monotonicity. |
| 2.7 lia/omega | No arithmetic reasoning beyond simplification. |
| 2.8 aesop | Extensionality plus deterministic simp already sufficient. |
| 2.9 norm_num/norm_cast | Generic symbolic identity; simp handles zero order. |
| 2.10 decide/kernel | Not a closed decidable instance. |
| 2.11 field_simp/ring | No denominator or ring-normalization goal. |
| 2.12 linear_combination | No equations to combine. |
| 2.13 wlog | No symmetric case split. |
| 2.14 calc | Two-step extensionality proof does not benefit from an equality chain. |
| 2.15 `<;>` | ext gives one coefficient goal; sequential tactics clearer. |
| 3.1 erw/rw | Neither present. |
| 3.2 fun_prop | No legacy analytic tactic. |
| 3.3 omega/lia | Neither present. |
| 3.4 rcases rfl | No destructuring. |
| 3.5 automation attributes | Following bundled zero theorem supplies simp normalization; no redundant attribute needed here. |
| 3.6 simp_all | No hypotheses to simplify. |
| 3.7 maxHeartbeats | No override present or added. |

Strategy reflection: retain the coefficient-level interface instead of unfolding
the linear-map implementation. This explains the result in two local steps and
avoids dependency on implementation details or circular use of the next theorem.

## Experiments and validation

Live lean_goal at line 107 showed the polynomial equality before ext and its
coefficient equality afterward. The isolated lean_run_code experiment copied
only the file prefix before this target (original mathlib imports and earlier
declarations), importing neither target nor downstream theorem. The proposed
`simp [hasseDeriv, hasseCoeff]` failed with a residual monomial-sum identity.
Its success=false response is recorded honestly; the compiler's recovery-only
sorryAx in that failed scratch result is not a proof certificate and was never
introduced into a project file. No failed experiment was adopted.
Evidence: `/private/tmp/roth-hasseDeriv_zero_apply-goal.json`,
`/private/tmp/roth-hasseDeriv_zero_apply-probe-input.json`, and
`/private/tmp/roth-hasseDeriv_zero_apply-probe.json`.

| Gate | Result/evidence |
|---|---|
| lake_build_file | PASS: lake build Roth.HasseDeriv, exit 0, 1430 jobs. /private/tmp/roth-hasseDeriv_zero_apply-module-build.log. |
| fresh LSP | PASS: success=true, partial=false, timed_out=false, failed_dependencies=[]; no errors, only existing header warning. /private/tmp/roth-hasseDeriv_zero_apply-postedit-diagnostics.json. |
| definition_protected | PASS: no source edits. |
| theorem_statement_protected | PASS: statement and source byte-identical. |
| structure_gate | PASS: two short proof steps; no extraction needed. |
| naming_gate | PASS: established descriptive name retained. |
| line_packing_gate | PASS: full signature already one 79-character line. |
| inequality_orientation_gate | PASS: no inequalities. |
| scoped diff | PASS: git diff for source empty; git diff --check exit 0. |
| dependent closure | PASS: orchestrator full lake build exit 0, 2586 jobs; separate lake build Roth.LeanEval exit 0, 2585 jobs. Logs /private/tmp/roth-hasseDeriv_zero_apply-build.log and /private/tmp/roth-hasseDeriv_zero_apply-leaneval.log. |

The retained target was separately inspected with lean_run_code importing the
validated module: success=true, timed_out=false; #print axioms reports exactly
[propext, Classical.choice, Quot.sound], and #check confirms the original
σ/R/CommSemiring/P parameters and conclusion. Evidence:
`/private/tmp/roth-hasseDeriv_zero_apply-axioms.json`. Together with the module
build and complete source diagnostics, this validates the retained proof itself.

No sorry, new axiom, native_decide, option, import, version, rename, structure or
source edit. Existing header warning remains deferred pending ownership/license
information. This checkpoint records a completed review without unnecessary edits.

## Phase 4 checklist

- [x] Step 1: inherited workflow/references and target context reviewed.
- [x] Step 2: all 24 target audit dispositions.
- [x] Step 2.5: five searches, with unavailable LeanSearch disclosed.
- [x] Step 2.6: all parameters, inversion and local/public literature reviewed.
- [x] Step 2.7: complete signature-width table.
- [x] Step 2.8: complete inequality scan.
- [x] Step 3: all 42 golfing rules considered.
- [x] Step 4: strategy reassessed; failed isolated alternative not adopted.
- [x] Step 5a: module build and complete fresh diagnostics passed.
- [x] Step 5b: protection, structure, naming, packing and scoped-diff gates passed.
- [x] Step 6a: no new rename or structure queue.

Parent owns dependent validation, shared progress logs, commit/push and file-wide phases.
