# Audit: `degreeOf_none_rename_some` (original declaration 12)

Initial audit written before source edits. Start: clean HEAD `d9a5acd`, 577 source lines,
27 retained declarations. Target L132–138, seven declaration lines, five proof-body lines;
scoped omit L131 is already present. Ownership: this private helper and exact necessary
substitutions at its two callers only; parent owns Git, shared logs and public decisions.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md. Also read both skill files, Phase 4
worker instructions, naming/style references and profiling reference. Existing public
types, definitions, documentation, imports and inline narratives are protected.

## Initial 24-item audit

| # | Item | Concrete finding / action |
|---|---|---|
| 1 | LINT | Complete native initial diagnostics: 0 errors, 31 warnings; none in target range. |
| 2 | HAVE SCAN | No have declarations. |
| 3 | SET_OPTION | No local limits, traces or suppression. |
| 4 | SIMP SQUEEZE | L138 terminal simp with mapDomain lemma; no squeezing required. |
| 5 | NAMING | degreeOf, none, rename, some describe the operation and conclusion; no banned abbreviation or numeric pattern. Delete rather than rename if direct mathlib substitution passes. |
| 6 | LINE PACKING | Initial widths 64 and 43; joining conclusion without indent gives 64 + 1 + 39 = 104, so break justified. See table below. |
| 7 | BY PLACEMENT | by is at end of conclusion line. |
| 8 | FORMAT | Two-space proof indent, no empty body lines; mathematical lambda uses => initially, eliminated if deletion succeeds. |
| 9 | COMMENTS | No target proof comments; preserve both callers' existing comments and docs. |
| 10 | DOCSTRING | Private helper has none, appropriate. |
| 11 | VISIBILITY | Private, exactly two uses in same module. Removal authorized if wrapper unnecessary. |
| 12 | STRUCTURE | Five proof-body lines, no conjunction or long branch; no extraction needed. |
| 13 | MATHLIB | Five actual native/source searches below; direct terminal simp using degreeOf and degrees_rename_of_injective closes target in live test. Test deletion and direct uses. |
| 14 | JUNK DEF | Not a definition. |
| 15 | EXISTS LEMMA | Equality, not an existential. |
| 16 | SHOW vs CHANGE | No show/change in target. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | Effective binders τ, R, CommSemiring R, U; Fintype and DecidableEq already omitted. Probe every binder; private literature exemption applies. |
| 19 | INEQUALITY | Signature is equality only; no ≥ or >. |
| 20 | NORMAL-FORM | degreeOf none = 0 is canonical; underlying degree multiset contains only some variables. |
| 21 | SYNTAX-GEN | Arbitrary rename and variable outside range would generalize; existing mathlib degrees API already supplies this without a local wrapper. |
| 22 | IMPORT-FANOUT | No new imports required. |
| 23 | CASTS | No ↑ or explicit value ascriptions in target; caller annotations tested for load-bearing necessity. |
| 24 | INSTANCE-NAME | Not an instance. |

## Five actual search methods

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | MvPolynomial degreeOf a renamed polynomial at a variable outside the range is zero | degreeOf_eq_natDegree, coeff_rename_eq_zero, degrees_rename; all partial matches. |
| B Loogle | MvPolynomial.degreeOf, MvPolynomial.rename | degreeOf_rename_of_injective, degreeOf_eq_natDegree; neither directly handles none. |
| C LeanSearch | MvPolynomial degreeOf rename variable not in range equals zero | degreeOf_rename_of_injective, coeff_rename_eq_zero, degrees_rename_of_injective. |
| D Source | degreeOf.*rename, rename.*degreeOf; degreeOf.*eq_zero and notMem variants in Algebra/MvPolynomial | Degrees.lean L419; no exact none specialization found in source; source results alone do not prove absence. |
| E Native local | degreeOf_rename | Same mathlib theorem and local callers; index warming, so no indexed absence claim. |

Auxiliary variants inspected: degrees_rename_of_injective, degrees_rename, degreeOf_def,
degreeOf_eq_sup, degreeOf_le_iff, support_rename_of_injective, outside-range mapDomain.
Common-equivalents buckets do not match this algebraic claim. Compiled live exact?
failed; grind and aesop failed. Live simp with degreeOf and degrees_rename_of_injective
closes the goal; its reported 'No goals to be solved' is from the original remaining
tactic, not failure of the proposed tactic. Isolated proof and full caller compile follow.
No claim that the general mathematics is absent from mathlib.

## Signature width and inequality tables

| Initial signature line | Codepoints | Next complete expression | Arithmetic | Action |
|---|---:|---|---|---|
| 132 | 64 | degreeOf none (rename some U) = 0 := by (39) | 64 + 1 + 39 = 104 | Keep break; delete if replacement passes. |
| 133 | 43 | No next signature line | n/a | End of signature. |

| Location | Inequality | Action |
|---|---|---|
| Entire signature and hypotheses | No ≥, >, ≤ or < | No orientation rewrite or rename. |

## Intended change

Delete the redundant private wrapper and use mathlib directly at the two public callers,
subject to complete compilation, native diagnostics, independent ORIGINAL proof,
actual caller axiom checks and anchored caller profiling. No new helper is planned.
Public instance omission menu remains pending and is not applied here.

## All 42 golf rules

| Rule | Concrete status |
|---|---|
| 1.1 by exact | n/a: no by exact wrapper. |
| 1.2 by rfl | n/a: no by rfl wrapper. |
| 1.3 rw + exact | n/a: target rw is followed by obtain and simp. |
| 1.4 simp + exact | n/a: target simp is already terminal. |
| 1.5 trailing rfl | n/a: no trailing rfl. |
| 1.6 constructor pair | n/a: no conjunction construction. |
| 1.7 apply + exact | n/a: no apply. |
| 1.8 by_contra! | n/a: no contradiction proof. |
| 1.9 eta reduction | n/a: fun e he supplies an unsolved body, not eta form; deleted with helper. |
| 1.10 single-use have | n/a: none. |
| 1.11 refine + fun | Existing refine already introduces e and he with lambda; whole argument replaced. |
| 1.12 redundant show | No original show; candidate caller term show supplies the expected equality for rewrite elaboration. |
| 1.13 obtain | Already uses obtain with rfl; no have projections. |
| 1.14 merge rw | No consecutive rw in target. |
| 1.15 terminal simp only | n/a: terminal simp unsqueezed already. |
| 1.16 nonterminal simp | No nonterminal simp in target or new substitutions. |
| 1.17 dot notation | Existing degreeOf_le_iff.2; replaced by direct mathlib simp. |
| 1.18 apply <\| | n/a: no applicable trailing parenthesis; rewrite-list term grouping required. |
| 1.19 push Not | n/a: no push_neg. |
| 1.20 existential inline | n/a: equality helper has two uses, not trivial existential. |
| 2.1 grind | Live whole-proof attempt failed on degreeOf equality. |
| 2.2 delete before grind | Live attempt already used grind alone; failed. |
| 2.3 simpa consolidation | Direct simp closes target, so no source simpa needed. |
| 2.4 fun_prop | n/a: no continuity, measurability or differentiability property. |
| 2.5 positivity | n/a: equality to zero, positivity cannot give the upper bound. |
| 2.6 gcongr | n/a: no monotonicity goal. |
| 2.7 lia / omega | n/a: obstacle is degreeOf renaming, not linear arithmetic; direct simp removes arithmetic stage. |
| 2.8 aesop | Live whole-proof attempt failed without progress. |
| 2.9 norm_num / norm_cast | n/a: no numerical computation or cast problem. |
| 2.10 decide +kernel | n/a: universally quantified arbitrary polynomial equality, not finite computation. |
| 2.11 field_simp; ring | n/a: no division or ring expression identity. |
| 2.12 linear_combination | n/a: no ring/ring_nf ending or algebraic hypotheses. |
| 2.13 wlog | n/a: no symmetric case branches. |
| 2.14 calc | n/a: no calc chain. |
| 2.15 <;> | n/a: no similar generated goals in replacement. |
| 3.1 erw | n/a: no erw. |
| 3.2 legacy function tactics | n/a: no continuity/measurability tactics. |
| 3.3 omega to lia | n/a: no omega. |
| 3.4 rfl substitution | Existing obtain substitutes immediately; removed with helper. |
| 3.5 attributes | No new lemma or automation attribute is needed; direct existing API. |
| 3.6 simp_all | n/a: no simp_all only. |
| 3.7 heartbeat options | n/a: no local limit options. |

## Step-back review

The support proof reconstructs a fact already encoded by mathlib's renaming-degree
multiset theorem. Live simp closes with two existing names. Keeping that as a local
one-line lemma would be an unnecessary wrapper. Direct call substitutions remove a
declaration without requiring a new helper, broad automation or new imports. Full
candidate and original-type proof compilation must still confirm the live result.

Literature status: n/a, private declaration; no WebSearch or math MCP literature search
is required. The two affected public callers retain their original statements and docs;
they are only checked for necessary substitution, not independently generalized here.

## Mechanical generalisation probes

Each probe is saved under `/private/tmp/roth-separation-d12-probes/`; the six-probe
loop records actual exit statuses in `results.json`. The initial drop-R/drop-tau probes
compiled because Lean autoImplicit reconstructed those binders; that is not a successful
binder removal. Follow-up explicit-drop-binders disables autoImplicit and checks the
real negative tests, with all diagnostics preserved.

| Effective binder | Role and candidates | Compiler evidence / result |
|---|---|---|
| τ : Type* | Variable type used in MvPolynomial and some injection; drop; universe widening | Already universe polymorphic. AutoImplicit reconstructed attempted drop; strict negative follow-up below. |
| R : Type* | Coefficient type; drop; universe widening | Already universe polymorphic. AutoImplicit reconstructed attempted drop; strict negative follow-up below. |
| CommSemiring R | Required to form MvPolynomial/rename/degreeOf; drop; Semiring R | Both negative files exit 1, failed to synthesize CommSemiring R at statement. No weaker catalogue candidate supports current MvPolynomial API. |
| U : MvPolynomial τ R | Polynomial whose renamed degree is measured; drop | Initial drop exit 1 with stuck coefficient type; strict negative follow-up below. No proposition to weaken/localize. |
| Fintype τ | Not an effective binder, already scoped omit in original | Positive original-type and direct-simp files compile without it; no source change needed. |
| DecidableEq τ | Not an effective binder, already scoped omit in original | Same positive files compile without it; no source change needed. |

No strict hypotheses, bundled conjunctions, point/global analysis properties or concrete
coefficient fields are present. Inversion check: the concrete some/none construction
can be generalized to arbitrary renaming and an omitted variable, but mathlib's
degrees_rename_of_injective is that abstraction already. Use it directly instead of
adding a new public generalization. No new private helper was introduced.

## Verification obtained before final profile

`lake build Roth.Separation` exited 0: `Build completed successfully (1876 jobs)`.
Raw actual-module log `/private/tmp/roth-separation-d12-module.log`.
Complete unfiltered native LSP raw `/private/tmp/roth-separation-d12-final-lsp.json`:
partial false, timed_out false, success true, failed_dependencies empty; 0 errors,
31 warnings, no sorry diagnostics. Initial raw `/private/tmp/roth-separation-d12-diag.json`.
Warnings are unchanged header metadata plus existing public unused-instance warnings;
public assumptions are deliberately preserved pending the parent-owned proposal.

Independent exact ORIGINAL type proof, not referring to the removed helper, compiled
exit 0 in `probes/original.lean`. Printed at `format.width = 100`:

```lean
@original : ∀ {τ : Type u_1} {R : Type u_2} [inst : CommSemiring R] (U : MvPolynomial τ R),
  degreeOf none ((rename some) U) = 0
```

`/private/tmp/roth-separation-d12-original-axioms.log` records original independent proof
and actual freshly built `Roth.hasseDeriv_rename_mul_aeval` and
`Roth.degreeOf_none_rename_mul_aeval` all depending only on
`[propext, Classical.choice, Quot.sound]`. Actual caller checks are used because the
target was deleted. No guessed private mangled constant is used.

Actual diff `/private/tmp/roth-separation-d12.diff`: 11 removed / 4 added = net −7;
577 → 570 source lines, 27 → 26 retained declarations. Helper declaration 7 → 0 lines;
its omit and separator also removed. First caller replacement is one line for one;
second caller rewrite grows from one line to three. All public signatures, docs,
imports, definitions, comments, instance assumptions and attributes are unchanged.
The term-mode show in the second caller fixes the rewrite equality expected type;
it is not a tactic-mode show/change issue. No value casts or ↑ added (0 dropped /
0 cross-type / 0 redundant; one equality type annotation supports elaboration).

Strict drop-binder follow-up `explicit-drop-binders.lean` exited 1 as expected:
unknown R at L6, unknown U at L13, unknown τ at L18/L20, with autoImplicit false.
Consequent recovery metavariables are confined to that deliberately failing scratch
file; repository and positive proof have no sorry. Thus every effective binder is
compiler-probed, without misreporting the initial autoImplicit successes as drops.

## Gate status and eleven completion steps

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | Pass | Actual lake build Roth.Separation exit 0, module.log. |
| definition_protected | Pass | No definition or abbrev changes. |
| theorem_statement_protected | Pass | Authorized private removal; both public caller signatures byte-identical. |
| structure_gate | Pass | Target removed, no new helper, unchanged caller structure with short local simp. |
| naming_gate | Pass | Target descriptive and then eliminated; no new names or rename needed. |
| line_packing_gate | Pass | Initial two-line table above, 104-column joined conclusion; no retained target signature. |
| inequality_orientation_gate | Pass | No reverse inequalities in target or new substitutions. |
| complete native LSP | Pass | Unfiltered complete final response, 0 errors / 31 warnings, no dependencies or partial data. |
| original-type independent proof | Pass | probes/original.lean exit 0, no reference to removed constant. |
| actual changed caller axioms | Pass | Both freshly built callers print only standard three axioms. |
| diff / comments / whitespace | Pass | Focused diff and git diff --check; all Lean block docs and inline comments preserved. |
| cumulative project / LeanEval / whole-original compatibility | Parent-owned | Run sequentially after source freeze, not asserted by this worker. |

1. References read in full; scope and baseline recorded.
2. All 24 initial audit items saved before source edits.
3. Five actual searches, auxiliary routes and exact? probe recorded.
4. Every binder probed; actual negative results and private literature exemption recorded.
5. Signature codepoint arithmetic and inequality table supplied.
6. All 42 golf rules carry concrete statuses.
7. Step-back review chose direct mathlib substitutions and removal.
8. Actual module build and complete unfiltered final native diagnostics passed.
9. ORIGINAL independent proof plus actual changed caller axiom checks passed.
10. Focused diff gates passed; actual caller profile is recorded below before freeze.
11. No rename queue action; report, final hash, drain and ownership revocation below.

Pending proposal: only parent-owned public instance removals in
`.mathlib-quality/cleanup/Separation-instance-proposal.md`; none applied by this worker.
No new public/generalisation/literature proposal and no new helper requires an audit.

## Actual repository-module profiling

Command: `/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true
-Dtrace.profiler.threshold=0 Roth/Separation.lean`.
Final raw `/private/tmp/roth-separation-d12-final-profile.log`; anchored table parser
`/private/tmp/roth-separation-profile-table.py`, JSON sidecar at raw-log path plus `.json`.
No extracted namespace or aggregate category substituted for actual declaration timings.
Final sweep started only after owner optional scratch and all worker builds/probes/MCP
requests drained. Conservative sums use outer Elab.command + outer Elab.async, counting
neither nested children nor the same proof twice.

| Actual declaration | Baseline command | Baseline async | Baseline sum | Final command | Final async | Final sum (ms) |
|---|---:|---:|---:|---:|---:|---:|
| degreeOf_none_rename_some | 13.487 | 81.907 | 95.394 | Removed | Removed | 0 |
| hasseDeriv_rename_mul_aeval | 79.082 | 152.208 | 231.290 | 65.655 | 182.016 | 247.671 |
| degreeOf_none_rename_mul_aeval | 17.356 | 46.714 | 64.070 | 21.430 | 80.199 | 101.629 |

Each retained affected declaration has one actual command and one async proof anchor.
Baseline raw `/private/tmp/roth-separation-d11-final-profile.log` is the valid preceding
actual-module measurement. Both final affected callers are below the 750 ms repeat
threshold and 1000 ms budget. Caller elaboration sums rose in this sweep, while the
private declaration is removed; this is an API simplification, with no claim of a
whole-project performance improvement. No heartbeat, recursion or trace options were
added to repository source.

Actual final full-module profiler command completed exit 0. Both affected anchor totals
were re-parsed after process completion and are unchanged. Request status artifact:
`/private/tmp/roth-separation-d12-completion.json`.

## Freeze

Source SHA256: `1d7e167ce78eb18a4815866a71a286989095d26499f49534db6af2ee823d2137`.
All native Lean/MCP, compiler, build, binder-probe and profiler requests are completed
and drained. **ALL source ownership is revoked, including this target, both callers
and every other source path. I am report-only and will make no source edit after
this freeze.** Parent owns cumulative original/public compatibility, every retained
actual axiom audit, sequential full build and separate LeanEval build, exact-path Git
commit and successful push before the next declaration.

## Owner cumulative publication gates

Source FROZEN SHA256 `1d7e167ce78eb18a4815866a71a286989095d26499f49534db6af2ee823d2137`; leaf ownership revoked and requests drained before owner gates. Owner probe `83868` exit0,63.55s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL26 actual retained standardaxiom checks. `/private/tmp/roth-separation-d12-compatibility.{lean,log,json}`. Owner build session `20284` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,113.27s/25.24s; source hash stable. `/private/tmp/roth-separation-d12-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.
