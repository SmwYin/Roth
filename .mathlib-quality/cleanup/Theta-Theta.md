# Dedicated audit: `Roth.Θ`

Scope: original `Roth/Theta.lean` L62, published baseline HEAD
`2f5160ba344b3d5f023497a97ffdca773dd2cfbd`. The declaration is retained unchanged:
`noncomputable def Θ (B : ℝ) (q r : σ → ℕ) : ℝ := sSup (indexSet B q r)`.
One line before/after; source delta zero. No helper, caller, public signature, value,
name, visibility, import, header or shared-sidecar change. The whole-file public-contract
menu remains unapplied; this audit does not infer approval for any proposal in it.

References read: Lean and mathlib-quality skills; full cleanup worker workflow;
full golfing-rules, proof-patterns, mathlib-search, generalisation-patterns,
cleanup-gates and profiling references in the required installed reference root;
relevant style sections on definitions, names, packing, documentation, transparency,
normal forms and performance; naming conventions; review stages 5/6. Substantive
truncated combined reads were followed by separate range reads.

## Baseline and mathematical meaning

Owner supplied clean pushed checkpoint and complete baseline live LSP
`/private/tmp/ThetaIndexSetFinalLsp.json`: 0 errors / 28 warnings, no Θ warning.
Unchanged whole-project baseline gates belong to owner. The local source
`.mathlib-quality/references/clean.tex` L656–668 defines Θ as the supremum of
indices over the bounded integer polynomial family at coprime rational points.
The body applies mathlib's canonical `sSup` directly to exactly that family.
This is a named mathematical object with the nonnegative/cardinality/monotonicity/
renaming/Lemmas 5–7 API, not a disposable local shorthand. Arbitrary B, q and r
are intentionally allowed by the definition; later theorems supply hypotheses
needed to use the conditional supremum. No positivity assumption is added.

## Full 24-item audit

| # | Item | Concrete finding/action |
|---|---|---|
| 1 | LINT | No target warning in supplied complete baseline; final check below. |
| 2 | HAVE SCAN | No have; direct data term. |
| 3 | SET_OPTION | None on declaration. |
| 4 | SIMP SQUEEZE | No simp call. |
| 5 | NAMING | Θ is the source's mathematical symbol, explicitly retained by dispatch. A descriptive spelling such as `indexSup` is a cosmetic public-API proposal only, assessed and unapplied; no sidecar entry or rename. No numbered scheme or forbidden abbreviation. |
| 6 | LINE PACKING | Single signature 48 codepoints through :=; whole line 70; measured table below. |
| 7 | BY PLACEMENT | No by; direct term already. |
| 8 | FORMAT | One line, standard spacing, no tactic, blank/trailing-space line, haveI or letI. |
| 9 | COMMENTS | No inline comments; existing two-line source docstring retained byte-for-byte. |
| 10 | DOCSTRING | Explains precise index family and source §5; existing protected documentation sufficient. |
| 11 | VISIBILITY | Retain public principal definition; public Θ API depends on its name. |
| 12 | STRUCTURE | One-line defining body; no branches or conjunction in signature. No extraction warranted. |
| 13 | MATHLIB | Already directly uses canonical sSup; five actual methods below. No equivalent source-specific Θ construction established. |
| 14 | JUNK DEF | Keep: named source object with extensive nonneg/card/mono/equiv/bound API, reused across many independent results. |
| 15 | EXISTS LEMMA | n/a: data definition, no private existential wrapper. |
| 16 | SHOW/CHANGE | Neither occurs. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | All explicit and ambient parameters considered and compiled scratch probes below; public contract retained. |
| 19 | INEQUALITY | Zero reversed inequality occurrences, table below. |
| 20 | NORMAL-FORM | Already sSup of the set; generic SupSet operation is canonical. iSup over witnesses would change representation and demand default/conditional-supremum care. |
| 21 | SYNTAX-GEN | Current B/q/r argument order directly matches source and consumers; no easier equivalent call shape identified. |
| 22 | IMPORT-FANOUT | n/a: no new import. |
| 23 | CASTS | 0 dropped / 0 cross-type / 0 load-bearing explicit casts in target or diff. ℝ and ℕ in binders are types, not redundant casts. |
| 24 | INSTANCE-NAME | n/a: not an instance, none introduced. |

## Measured signature and inequality tables

Definition packing reference: n/a; actual imported #check is captured in verification log.

| Signature line | Codepoints through := | Next signature token | Arithmetic | Action |
|---|---:|---|---|---|
| 62 | 48 | none: body follows on same line | n/a; complete declaration is 70 ≤ 100 | ok |

| Location | Reversed inequality | Rewrite / rename |
|---|---|---|
| L62 complete signature and body | none: no ≥ or > | n/a |

## Five actual mathlib searches

Native Lean MCP schemas were inspected before calls.

| Method | Actual query | Observed result |
|---|---|---|
| A Lean-Finder | `supremum indices nonzero integer multivariate polynomials bounded degree coefficients rational points Roth theta` | Three ChevalleyThm.MvPolynomialC numerical/degree bounds, unrelated to Θ. |
| B Loogle | `sSup`, then `SupSet.sSup` | First failed unknown identifier; qualified retry returned SupSet.sSup, OrderSupSet.mk and isLUB_sSup_of_isLUB. Canonical operation already used directly. |
| C LeanSearch | `supremum polynomial indices bounded integer coefficients Roth theorem theta` | Polynomial.coeff_bdd_of_roots_le, Behrend.roth_lower_bound and Polynomial.supDegree_eq_natDegree; none defines this family supremum. |
| D source rg | `def (Θ|theta|indexSet)|Roth\.Θ|SupSet\.sSup` in NumberTheory, conditional complete lattice and real sources | Only unrelated Chebyshev theta definition. Standard Order.Bounds.Defs read; no replacement established. |
| E local name search | `sSup`, limit 5 | Positive category/subobject/linear map/ordinal sSup results; index unavailable, therefore no empty-result absence inference. |

Full untruncated follow-up `rg -n 'def (Θ|indexSet)|Roth\.Θ'` over all Mathlib
returned no textual hit. That is bounded textual evidence, not proof of absence.
Auxiliary/generic variants inspected: SupSet, OrderSupSet and IsLUB; conditional
supremum API; polynomial-degree and number-theory folders. Common-equivalents table
does not match a discrete/compact/finite/bornology condition. Conclusion is presence
of the generic operation already used, not a claim that exhaustive textual absence
proves no possible library expression. No new lemma is being written, so there is
no speculative absence claim requiring an exact?-generated replacement. Six strict
replacement rules respected: no proof wrapper/custom predicate/bridge introduced;
the generic operation is used directly. Named mathematical Θ is retained by scope.

## Generalisation, literature and inversion

| Parameter/context | Role | Actual mechanical candidate | Outcome |
|---|---|---|---|
| {σ : Type*} | Variable index type, already universe polymorphic | Drop its binding / replace with fresh τ without Fintype | Compiled scratch probe recorded below; arbitrary universe already supported. |
| [Fintype σ] | Required by indexSet | Drop; replace with [Finite σ] | Compiled scratch probes below. |
| [DecidableEq σ] | Ambient instance | Drop | Compiled scratch probe below; #check determines whether it is already absent from exported type. |
| B : ℝ | Coefficient bound passed to indexSet | Drop | Compiled scratch probe below. General field replacement would require redesigning dependent family/index, not weaken this direct expression. |
| q : σ → ℕ | Denominator vector passed to indexSet | Drop | Compiled scratch probe below; changing denominator type changes dependent construction. |
| r : σ → ℕ | Degree/weight vector passed to indexSet | Drop | Compiled scratch probe below; no positivity premise to weaken. |

No proposition, global continuity/monotonicity premise, strict bound or bundled
equivalence is available to weaken. No public candidate applied. Inversion check:
n/a as a theorem generalisation: this is a data definition with no proof forgetting
its concrete argument. Abstracting `indexSet` to an arbitrary set gives sSup itself,
already used; it would discard the named source object rather than strengthen a theorem.

Actual public web searches: (1) `Takloo Bighash Yin Formalizing Roth theorem index theta
supremum polynomials`; top hits author research page, author Pythagorean book page,
and a secondary Vojta copy, no new Θ formulation. (2) `Roth theorem proof theta supremum
index polynomial generalization Dyson lemma`; top relevant primary hits Gao's
[Diophantine Geometry notes](https://ziyangjeremygao.github.io/LectureNotes/DiophantineGeometry.pdf),
[Maculan's Roth book](https://webusers.imj-prg.fr/~marco.maculan/files/papers/roth_book),
and [Min Ru's Roth notes](https://www.math.uh.edu/~minru/fields/roth.pdf).
(3) `site.math.uic.edu Roth theorem supremum index polynomial` returned no separate
direct source formulation. Search excerpts concern alternate Dyson/index proofs;
they do not establish a stronger interchangeable definition. Local clean.tex §5
is the directly inspected decisive source. ChatGPT math MCP absent from available
tool inventory; no second-opinion result fabricated. Literature-driven replacement:
none established. Number fields/geometric index variants would be a separate design.

## All 42 golfing rules

| Rule | Status/reason |
|---|---|
| 1.1 by exact | n/a: no tactic wrapper |
| 1.2 by rfl | n/a: direct data term |
| 1.3 rw+exact | n/a: no rw/exact |
| 1.4 simp+exact | n/a: no simp/exact |
| 1.5 trailing rfl | n/a: no simp/rfl |
| 1.6 constructor | n/a: no constructor |
| 1.7 apply+exact | n/a: no tactics |
| 1.8 by_contra | n/a: no contradiction proof |
| 1.9 eta | n/a: no lambda |
| 1.10 have | n/a: no have |
| 1.11 apply+intro | n/a: no tactics |
| 1.12 show | n/a: none |
| 1.13 projections | n/a: no have/projection |
| 1.14 merge rw | n/a: no rw |
| 1.15 terminal simp | n/a: none |
| 1.16 nonterminal simp | n/a: none |
| 1.17 dot notation | n/a: sSup already direct canonical application |
| 1.18 <\| | n/a: parentheses delimit indexSet argument; replacing with <\| gives no clarity/performance gain |
| 1.19 push Not | n/a: none |
| 1.20 existential wrapper | n/a: no lemma/witness |
| 2.1 grind | n/a: no propositional proof; direct real-valued definition |
| 2.2 delete before grind | n/a: no grind |
| 2.3 simpa | n/a: no tactic proof |
| 2.4 fun_prop | n/a: no function-property goal |
| 2.5 positivity | n/a: no positivity goal |
| 2.6 gcongr | n/a: no inequality goal |
| 2.7 lia/omega | n/a: no arithmetic proof |
| 2.8 aesop | n/a: data term, no proof search |
| 2.9 norm_num/cast | n/a: no numeric computation/cast proof |
| 2.10 decide | n/a: noncomputable supremum, no decidable proposition |
| 2.11 field_simp/ring | n/a: no algebraic identity |
| 2.12 linear_combination | n/a: no ring-ending proof |
| 2.13 wlog | n/a: no cases |
| 2.14 calc | n/a: no calc |
| 2.15 <;> | n/a: no tactic goals |
| 3.1 erw | n/a: none |
| 3.2 continuity | n/a: none |
| 3.3 omega→lia | n/a: no arithmetic tactic |
| 3.4 rcases rfl | n/a: none |
| 3.5 attributes | n/a: no new lemma; unfolding this named supremum globally offers no benefit |
| 3.6 simp_all | n/a: none |
| 3.7 limits | n/a: no limit option |

Step-back/simplify: direct term is minimal and exposes the standard order API.
No composed proof, redundant step, repeated skeleton or independent branch exists.
Built-in simplify skill/tool is unavailable; manual holistic review is PASS-THROUGH.
No source change or new helper is justified by any applicable rule.

## Validation and frozen handoff

Owner explicitly reserved an exclusive compiler/LSP/profile window after its previous
scratch candidate compiler drained. Module invocation
`/Users/ramin/.elan/bin/lake build Roth.Theta` exited 0; raw UTF-8
`/private/tmp/ThetaDefBuild.log` ends `Build completed successfully (2423 jobs)`.

Imported verification invocation
`/Users/ramin/.elan/bin/lake env lean /private/tmp/ThetaDefVerify.lean` exited 0;
raw UTF-8 `/private/tmp/ThetaDefVerify.log`. It imports the actual built Roth.Theta,
defines `ThetaDefAudit.original` independently using the original defining body
`sSup (Roth.indexSet B q r)` (never calls Θ inside that definition), then proves both
whole-function type/value equality `@Roth.Θ = @original` and pointwise equality by rfl.
It also independently checks the unfolding equality to sSup by rfl and prints the
actual built constant, rather than certifying a prefix-local lookalike. Actual type:
`{σ : Type u} → [Fintype σ] → ℝ → (σ → ℕ) → (σ → ℕ) → ℝ`.
The surrounding DecidableEq is already absent. Actual built `#print axioms Roth.Θ`
reports exactly `[propext, Classical.choice, Quot.sound]`.

Seven drop/weakening variants compiled sequentially with
`/Users/ramin/.elan/bin/lake env lean /private/tmp/ThetaDef-<variant>.lean`;
each corresponding raw `.log` is retained. Exit codes in order:
dropFintype 1, weakenFinite 1, dropDecidableEq 0, dropB 1, dropq 1, dropr 1,
dropσ 1. The first two fail synthesis of Fintype σ at the indexSet application;
the final one similarly fails Fintype τ after replacing the index type binding.
B/q/r drops fail with the respective unknown identifier in the defining body.
Dropping DecidableEq succeeds and confirms what the actual exported type already
shows. These are scratch probes only; no live API edits or assumption drops.

Fresh complete unfiltered native `lean_diagnostic_messages` on actual final source
completed with `success=true`, `partial=false`, `timed_out=false`, empty failed
dependencies, 0 errors / 28 warnings. Full raw response retained in
`/private/tmp/ThetaDefFinalLsp.json`; console rendering truncation did not affect
the stored response. No warning at L62. Warning lines, unfiltered:
1,87,135,74,79,72,72,87,84,94,102,110,109,117,127,154,135,188,372,228,372,369,
414,419,407,621,524,518. They concern header/other declarations and match baseline;
no warning suppression added. Header metadata and other public contracts are owner
scope. All compiler sessions and the LSP request completed before profiling began.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Actual lake build Roth.Theta exit 0, log above. |
| definition_protected | pass | Entire target declaration byte-identical; independent imported type/value rfl passed. |
| theorem_statement_protected | pass | No theorem touched. |
| structure_gate | pass | One-line body, no branch or statement conjunction. |
| naming_gate | pass under explicit scope | Source symbol Θ retained as instructed; cosmetic indexSup suggestion unapplied and unqueued. |
| line_packing_gate | pass | Complete one-line measured width table. |
| inequality_orientation_gate | pass | Complete zero-occurrence scan table. |
| live diagnostics | pass for target | Complete actual-file response, 0 errors/no target warning. |
| original type/value and standard axioms | pass | Actual imported built constant, independent original and whole-function rfl. |
| cumulative external breakage | owner final gate | Source unchanged; direct Θ source users found in Theta only. |
| full project / LeanEval | pending owner | Owner must run sequential lake build then separate lake build Roth.LeanEval. Not claimed here. |

## Required 11-step checklist

- [✓] Step 1: reference documents read, including full five required references.
- [✓] Step 2: full 24-item audit recorded.
- [✓] Step 2.5: all five actual searches, positive results and limitations recorded.
- [✓] Step 2.6: each parameter/ambient instance probed; public literature/inversion checks.
- [✓] Step 2.7: complete signature codepoint table.
- [✓] Step 2.8: complete inequality scan.
- [✓] Step 3: all 42 golf rules with concrete statuses.
- [✓] Step 4: holistic simplify/step-back review, PASS-THROUGH.
- [✓] Step 5a: actual complete unfiltered final live LSP response.
- [✓] Step 5b: diff/content/module/type/value/axiom gates, owner gates explicit.
- [✓] Step 6a: no rename applied or queued; sidecar untouched per dispatch.

Comments-preserved: existing two-line docstring unchanged, no inline comments present.
Refactoring needed: none recommended. Cosmetic descriptive renaming assessed only;
not an approval request or a blocker. No new identifier, helper, sorry, axiom,
native_decide, limit raise, profiling scaffold or code edit introduced.

## Buzz pass and final freeze

Outcome: FAST-BOARD for Θ; no fix or repeat required. Actual uncontended command
`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/ThetaDefPrefix.lean`
exited 0. Raw UTF-8 `/private/tmp/ThetaDefProfile.log` retained. Prefix preserves
all exact actual source lines 1–62, including imports, namespace, variables,
preceding definitions and Θ; only `end Roth` is appended. Exact prefix equality
was checked after the run. This is prefix-only, not a whole-Theta profile pass:
known later index_le_lem6 linarith failures under whole-file profiling remain
owner scope; final actual whole-module sweep remains mandatory after that cleanup.

Actual target anchor at raw log L5066–5069 is the docstring and `noncomputable def Θ`.
Outer `Elab.command` 3.905 ms + associated async addDecl/kernel wrapper 0.057 ms
+ associated async linters 2.516 ms = **6.478 ms**, conservatively including linting.
Kernel child 0.033 ms is nested and not added again. No separate compiler/proof
node for this noncomputable data definition. Imports (23.4 s) and other declarations
are excluded. Total is well below 750 ms repeat threshold and 1000 ms budget.
No profiling scaffolding was inserted into live source; no limit raise.

Final source freeze SHA256:
`4966bfa4274976d8e46102aa89c8fead84392ecf1351f7b337ad8ecfac63ecd9`.
All leaf compiler sessions, parameter probes, native LSP and profile requests have
completed. Leaf source-edit authority revoked; no source edits made or planned.
Only this dedicated report was written. Owner final full build, separate LeanEval
build, cumulative/profile sweep and commit/push remain owner gates, not claimed done.


## Owner checkpoint gates

Fresh leaf source/report authority revoked and all requests drained. Owner inspected the actual
original whole-function/value/axiom compiler,complete unfilteredLSP and exact-source-prefix
profile evidence. Source unchanged,so no caller/proof/doc/name change is hidden. Frozen owner
sequential full `lake build`:exit0 in4.975s,then separate `lake build Roth.LeanEval`:exit0
in2.850s. Source SHA stable; `/private/tmp/roth-theta-d03-builds.json` and full/leaneval logs.
An earlier RSet width-table action label was normalized from keep to ok; measured content and
source unchanged. Exact-path commit/push are the final declaration publication gates.
