# Approved instance revisit: `Roth.degreeOf_rename_mul_aeval`

Scope: only this theorem in `Roth/Separation.lean`, inherited clean HEAD `8b669ec` on
`ramin-cleanup`. User approved removing both `[Fintype τ]` and `[DecidableEq τ]`.
User declined coefficient widening; retain `[CommRing R] [IsDomain R]` exactly.
No wrapper deletion, Nat codomain change, helper, Git mutation, shared-log edit, or delegation.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md, plus both skills, Phase 4,
relevant style/naming rules and profiling reference. This is a fresh audit;
historical d19 report informs reasoning but does not substitute for fresh evidence.

## Initial audit — recorded before source edits

Source target initially lines 190–200: 11 declaration lines, 9 proof lines counting
the `:= by` line. Fresh native full-file LSP: complete, 0 errors, 18 warnings,
0 infos, partial=false, timed_out=false, success=true, failed_dependencies=[].
Raw `/private/tmp/roth-separation-r07-baseline-lsp.json`. Target has three warnings:
unused section Fintype, unused decidability in type, unused Fintype in type.

1. LINT: remove exactly the two approved instances; address the three target warnings.
2. HAVE SCAN: no `have` declarations, so no use-count/inlining candidate.
3. SET_OPTION: none in target; no limit changes planned.
4. SIMP SQUEEZE: zero branch `simp [hU]` and final `simp [...]` are terminal; retain unsqueezed.
5. NAMING: degreeOf/rename/mul/aeval identify mathlib operations; no forbidden abbreviation,
   numeric scheme, single-letter name, `_ge_` or `_gt_`; no rename necessary.
6. LINE PACKING: signature widths measured below; all breaks justified.
7. BY PLACEMENT: `:= by` ends the conclusion line.
8. FORMAT: two-space proof indent, no blank internal lines, merged rw list; add local
   `classical` only if necessary after dropping decidability; no haveI/letI.
9. COMMENTS: no inline proof comments; preserve all existing docstring bytes.
10. DOCSTRING: existing mathematical statement and motivating source citation preserved by user contract.
11. VISIBILITY: public result retained; same-module use does not authorize changing public API visibility.
12. STRUCTURE: proof under 15 lines, no conjunction, zero branch one line and nonzero branch six;
    no helper extraction needed.
13. MATHLIB: fresh five-method search launched/completed; finder and LeanSearch returned degreeOf_mul_eq,
    degreeOf_prod_eq, degreeOf_rename_of_injective and X variants; Loogle empty for the actual query;
    local index warming with source hits. Source/generic-route follow-up required below.
14. JUNK DEF: n/a, theorem rather than definition.
15. EXISTS LEMMA: n/a, no existential.
16. SHOW vs CHANGE: absent.
17. PUSH_NEG: absent.
18. GENERALISE: fresh exact arbitrary-τ proof and original-class adapter required; test every effective
    binder. Coefficient weakening is a closed declined option, never apply it.
19. INEQUALITY: equality with `V ≠ 0`; no inequalities in signature/hypotheses/proof.
20. NORMAL-FORM: canonical mathlib degreeOf equality in ℕ, preserving its zero convention.
21. SYNTAX-GEN: U and j explicit, V inferred from hV; convenient rewrite at exists_det_eq_mul.
22. IMPORT-FANOUT: n/a, no new imports needed.
23. CASTS: `X none : MvPolynomial (Option τ) R` fixes the aeval codomain; retain load-bearing annotation.
24. INSTANCE-NAME: n/a, theorem introduces no instance declaration.

| Initial signature line | Codepoints | Next token | Arithmetic | Result |
|---|---:|---|---|---|
|190|98|degreeOf (8)|98 + 1 + 8 = 107 > 100|keep|
|191|97|degreeOf (8)|97 + 1 + 8 = 106 > 100|keep|
|192|24|end|24 ≤ 100|keep|

| Region | ≤ | < | ≥ | > | Result |
|---|---:|---:|---:|---:|---|
|Effective signature and all hypotheses|0|0|0|0|n/a — no ≥/> occurrence|
|Proof|0|0|0|0|no inequality rewrite or rename|

Initial concrete action: put scoped `omit [Fintype τ] [DecidableEq τ] in` before the
original docstring and add local `classical`; retain original mathematics and coefficient
classes. No pending required user decision.

## Mathematics, searches, and literature

For U=0 both natural degrees are zero. Otherwise injective renaming and the injective
univariate embedding make both factors nonzero; product degree is additive. Renaming
preserves the first degree and the second factor contains only none, so its some-j
degree vanishes. Arbitrary τ suffices; no enumeration is involved.

|Method|Fresh actual query|Outcome|
|---|---|---|
|A Lean-Finder|degree in one variable of product of multivariate polynomials with disjoint variables|Success: degreeOf_mul_eq, degreeOf_prod_eq, degreeOf_mul_le, degreeOf_mul_X_of_ne|
|B Loogle|`MvPolynomial.degreeOf (_ * _)`|Success, empty for this particular pattern; no absence claim|
|C LeanSearch|degreeOf rename product univariate aeval disjoint variables|Success: degreeOf_rename_of_injective and product/X variants|
|D source|full name and degreeOf_mul / degreeOf_rename / degreeOf-aeval patterns, full untruncated rg|Product/rename APIs found; full target name absent in searched Mathlib directory|
|E local name|degreeOf_mul|12 hits including product, C/X/power variants; index=warming, so no index-certified absence|

Raw native outputs `/private/tmp/roth-separation-r07-{finder,loogle,search,local}.json`;
full source results `/private/tmp/roth-separation-r07-source-search.log`. Read
NoZeroDivisors.lean product/degree APIs, including degreeOf_mul_eq at line 43, and
Degrees.lean rename/X variants. No common-equivalents bucket matches this polynomial
statement. Existing direct mathlib calls retained; no new wrapper or custom predicate.

Fresh live-file generic routes and whole-proof attempts: grind failed, simp made no
progress, aesop failed exhaustive search, exact? could not close; apply? offered
generic Nat equality transformations with nontrivial remaining goals, no direct polynomial
replacement. Complete raw `/private/tmp/roth-separation-r07-attempts.json`; all timed_out=false.
The multi-attempt tool replaces one tactic line, so continuations after candidate closures
also report syntax/no-goal errors; no such candidate is counted as a successful full proof.
Search findings establish useful building blocks, not mathematical nonexistence.

Actual web query: `multivariate polynomial degree in one variable product disjoint
variables integral domain generalization`. First three results: Choe–Oxley–Sokal–Wagner
*Homogeneous Multivariate Polynomials*, Androma degree formula, and *On zeros of a
polynomial in a finite grid* (arXiv:1508.06020). Fresh primary source inspected:
[Choe–Oxley–Sokal–Wagner](https://www.math.lsu.edu/~oxley/ycjoasdw.pdf), Lemma 4.7 proof,
PDF page 22, lines 1213–1224: taking the leading coefficients in one chosen variable
over the polynomial ring in the remaining variables proves that individual product
degrees add over an integral domain. This supports the same mathematical argument;
the arbitrary-index conclusion here is compiler-verified rather than attributed to a
separate semiring result in that paper. Local motivating source reread at
`.mathlib-quality/references/clean.tex:435`, proof of Lemma 2.
ChatGPT math MCP unavailable: fresh ALL_TOOLS name/description discovery found no
mathematical second-opinion connector. No substitute or external message claimed.

The optional coefficient widening remains DECLINED; wrapper deletions remain DECLINED,
Nat codomain remains unchanged. The two approved index-instance removals are applied.

## All 42 golf rules — fresh pass

|Rule|Concrete result|
|---|---|
|1.1 by exact|n/a, no wrapper|
|1.2 by rfl|n/a, non-reflexive polynomial degree proof|
|1.3 rw + exact|n/a, rewrite followed by degree-zero simplification|
|1.4 simp + exact|n/a, both simp calls terminal|
|1.5 trailing rfl|n/a, absent|
|1.6 constructor|n/a, equality without conjunction|
|1.7 apply + exact|n/a, no apply|
|1.8 by_contra!|n/a, direct zero/nonzero split|
|1.9 eta reduction|n/a, no lambdas|
|1.10 inline have|n/a, no haves|
|1.11 refine fun|n/a, no introduction sequence|
|1.12 redundant show|n/a, absent|
|1.13 obtain projections|n/a, no destructuring haves; iff .2 directly applies its hypothesis|
|1.14 merge rw|already one list for product and rename|
|1.15 unsqueeze terminal simp|both already unsqueezed|
|1.16 squeeze nonterminal simp|n/a, both terminal|
|1.17 dot notation|already `.not.mpr` and iff `.2`; no verbose composition|
|1.18 <\||n/a, nested parentheses group arguments in rw list|
|1.19 push Not|n/a, no push_neg|
|1.20 existential inline|n/a, no existential helper|
|2.1 whole grind|fresh actual native attempt failed|
|2.2 before grind|n/a, no grind in retained proof|
|2.3 simpa consolidation|whole simp fresh attempt made no progress; no trailing exact to consolidate|
|2.4 fun_prop|n/a, no analytic property|
|2.5 positivity|n/a, equality of symbolic degrees; nonzero factors come from injectivity and hV|
|2.6 gcongr|n/a, not monotonicity or an inequality|
|2.7 lia/omega|n/a, polynomial degree relation missing; no arithmetic hypotheses to derive it|
|2.8 aesop|fresh native exhaustive search failed|
|2.9 norm_num/norm_cast|n/a, no numerical or cast calculation|
|2.10 decide/kernel|n/a, arbitrary polynomials and coefficient ring|
|2.11 field_simp/ring|n/a, degree equality is not a ring identity, no denominator|
|2.12 linear_combination|n/a, no ring/ring_nf ending or ring-valued target|
|2.13 wlog|n/a, zero and nonzero cases use different arguments|
|2.14 calc|n/a, absent|
|2.15 <;>|n/a, branches require different polynomial facts|
|3.1 erw→rw|already rw|
|3.2 continuity→fun_prop|n/a, neither tactic nor analytic goal|
|3.3 omega→lia|n/a, no arithmetic tactic|
|3.4 rcases rfl|n/a, no rcases|
|3.5 automation attributes|none needed for the approved local instance removal; specialized rule not added globally|
|3.6 simp_all|fresh final-goal native trial closes goal but leaves continuation syntax diagnostic; no accepted full-proof improvement and scans needless context|
|3.7 heartbeat limits|n/a, none present or added|

## Step-back / simplify review

Reviewed zero-case chunk, product/nonzero chunk, and rename/disjoint-variable chunk.
Each retained step changes or closes the goal; native live final goal now has τ, R,
CommRing, IsDomain, U, V, hV, j, hU and **no index instances**. It is exactly
`degreeOf j U + degreeOf (some j) (aeval (X none) V) = degreeOf j U` before terminal simp,
and no goals afterward. Term-mode chaining would repeat the same nonzero prerequisites;
induction on V would introduce unnecessary coefficient/sum bookkeeping. No >10-line
branch, duplicated haves, coercion churn, or missing-API extraction signal justifies a
new helper. Fresh whole-proof and generic-route attempts supplied no replacement.
The two-line production diff is the minimal approved instance removal with local classical.

Fresh final-goal attempts `/private/tmp/roth-separation-r07-final-attempts.json`:
grind fails to prove the second factor has degree zero; simp without
Multiset.mem_replicate leaves explicit replicate nonmembership; simp_all with all the
same lemmas closes the local goal but the one-line replacement leaves the original
continuation as a syntax error and exceeds the width limit. No candidate changed source.

## Every effective binder / fresh compiler probes

Actual persisted compiler trials use autoImplicit=false so a removed binder cannot be
silently reconstructed. Every row has a separately saved `.lean` and unfiltered `.log`
under `/private/tmp/roth-separation-r07-NAME`; run manifest
`/private/tmp/roth-separation-r07-probe-results.json`. Exit 1 means failure of the stated
mechanical test, not proof that no alternative argument could ever work.

|Binder|Class / actual use|Fresh mechanical test|Result / disposition|
|---|---|---|---|
|τ : Type*|type variable in U, j and Option τ|drop_tau|exit 1, unknown τ; independent universes u_1/u_2 already supported|
|Fintype τ|index instance, no enumeration|drop_fintype, drop_both|both exit 0; approved removal applied; Finite would be stronger than no assumption|
|DecidableEq τ|decidability used only by proof simplification|drop_decidable, drop_both with local classical|both exit 0; approved removal applied|
|R : Type*|coefficient type|drop_R|exit 1, unknown R; already universe polymorphic|
|CommRing R|commutative polynomial operations|drop_commring, ring, commsemiring|exits 1 (Semiring absent), 1 (CommSemiring absent), 0 respectively; widening DECLINED, retain CommRing|
|IsDomain R|nonzero product-degree API|drop_domain, nozerodivisors|exits 1 (NoZeroDivisors absent), 0 respectively; widening DECLINED, retain IsDomain|
|U : MvPolynomial τ R|first factor and RHS degree|drop_U|exit 1, unknown U; structure-value input required; no extra U≠0 assumption introduced|
|V : Polynomial R|second factor and hV|drop_V|exit 1, unknown V; structure-value input required|
|hV : V ≠ 0|injective evaluation gives second-factor nonzero|drop_hV|exit 1, unknown hV in proof; retain nonzero hypothesis|
|j : τ|chosen variable|drop_j|exit 1, unknown j; structure-value input required|

No point/global localization or strict→weak comparison applies: hV is a nonzero
polynomial over an unordered arbitrary ring. Inversion check NOT-APPLICABLE: all
objects are already arbitrary, typeclass-parametric polynomials; the proof genuinely
uses the concrete rename/aeval disjoint-variable structure rather than hiding a special
named mathematical object. ℕ codomain is the existing degreeOf normal form and stays fixed.

The independent file proves the exact new arbitrary-τ theorem by a non-self proof,
then checks `@Roth.degreeOf_rename_mul_aeval` against the explicit new type and supplies
an explicit original-class adapter with both Fintype and DecidableEq binders. No index
instance is available to the independent theorem. Actual built target, actual sole
caller `Roth.exists_det_eq_mul`, the independent theorem and original adapter all
print exactly `[propext, Classical.choice, Quot.sound]`. Native fresh run-code signature
and axiom confirmation also succeeds without timeout, raw
`/private/tmp/roth-separation-r07-native-exact.json`.

No external direct caller: fresh full project `.lean` search found only the declaration
and the call in `exists_det_eq_mul` (now line 577). No caller source changes required.

Actual `hV_necessity` trial exits 0: for τ=Unit, R=ℤ, U=X(), V=0, the proposed
equality without hV is false (degree zero versus degree one), certified by `simp`.
All 16 compiler trials completed and their processes drained before profiling.

## Final width, preservation, and gates

At `format.width := 100`, fresh native `#check @Roth.degreeOf_rename_mul_aeval`
prints the effective binders `{τ : Type u_1} {R : Type u_2} [CommRing R] [IsDomain R]`
followed by U, implicit V, hV and j; no index class remains. Raw native exact JSON
and command-line independent log retain the complete pretty-printed reference.

|Final signature line|Codepoints|Next token|Arithmetic|Action|
|---|---:|---|---|---|
|191|98|degreeOf (8)|98 + 1 + 8 = 107 > 100|keep|
|192|97|degreeOf (8)|97 + 1 + 8 = 106 > 100|keep|
|193|24|end|24 ≤ 100|keep|

The initial inequality table still applies literally: written signature/proof contains
no ≤/< /≥/>; omit and classical introduce none. Target source signature and docstring
were compared against `/private/tmp/roth-separation-original.lean`: both byte-identical.
Coefficient variable declaration remains exactly `variable {R : Type*} [CommRing R] [IsDomain R]`.

|Gate|Result|Fresh evidence|
|---|---|---|
|lake_build_file|PASS|`/Users/ramin/.elan/bin/lake build Roth.Separation`, exit 0, 1876 jobs; `/private/tmp/roth-separation-r07-build.log`|
|definition_protected|PASS|diff contains only scoped omit and local classical, no definition/import/pin/header changes|
|theorem_statement_protected|PASS, exact approval exception|only approved effective index-instance removal; original written signature/docs and coefficient assumptions preserved|
|structure_gate|PASS|declaration 11→12 lines, proof counting := by 9→10 lines; no conjunction or branch >10|
|naming_gate|PASS|operation-based name, no forbidden pattern or rename needed|
|line_packing_gate|PASS|all three final signature lines measured above|
|inequality_orientation_gate|PASS|all hypotheses/conclusion/body scanned, no reversed inequality|
|complete unfiltered native LSP|PASS|`...-complete-final-lsp.json`: 0 errors, 15 warnings, 0 infos, partial=false, timed_out=false, success=true, failed_dependencies=[]|
|exact new type / independent proof|PASS|`...-independent.lean/.log`, exit 0; arbitrary τ, non-self proof, explicit @new-type assignment|
|original effective-type adapter|PASS|same file, explicit original Fintype/DecidableEq binders retained, old application recovered|
|actual built target/caller axioms|PASS|same log: target, exists_det_eq_mul, independent and adapter use exactly propext, Classical.choice, Quot.sound|
|caller gate|PASS|sole caller same built and complete-LSP module; no external direct callers or caller edits|
|diff/whitespace|PASS|actual git diff --check exit 0; source numstat 2 additions/0 deletions; module 580→582 lines, declarations 25→25|

All short `...` evidence paths in the gate table have prefix `/private/tmp/roth-separation-r07`.
Unrelated warnings, including user-preserved header metadata, remain recorded unsuppressed.

Simplify pass: PASS-THROUGH. No separate built-in simplify callable was exposed;
performed the full step-back review in-thread under the no-delegation contract.
No further issue, helper, rename, source edit, or pending concrete proposal.

## Buzz / actual repository profile

All owned native MCP, module-build and 16 scratch compiler requests drained before the
final isolated actual repository command:

```
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Separation.lean
```

Exit 0. Complete raw `/private/tmp/roth-separation-r07-profile.log` (1,080,282 lines)
and parser table `/private/tmp/roth-separation-r07-profile.log.json`. Parser
`/private/tmp/roth-separation-profile-table.py` identifies two nested command anchors
(inner theorem and outer scoped omit) and one outer proof anchor. Use the **outer omit
command only**; do not add its nested theorem time again.

|Sample|Outer command|Outer async proof|Conservative total|
|---|---:|---:|---:|
|Authorized actual r06 baseline|22.671 ms|115.579 ms|138.250 ms|
|Fresh actual r07 final|17.912 ms|110.900 ms|128.812 ms|

Final outer command anchor line 200422, `[Elab.command] [0.017912] ... omit ...`,
with target theorem text at 200426. Nested theorem command at 197217 is 16.381 ms
and is **not additionally counted**. Actual outer proof anchor 200459,
`[Elab.async] [0.110900] ... elaborating proof of Roth.degreeOf_rename_mul_aeval`.
Under 750 ms repeat threshold and 1000 ms budget, so no repeat/fix needed.
Outcome FAST-BOARD for owned target. Zero limits raised, zero profiling scaffolding
in source, no over-budget deferral or big-change proposal. Timing samples alone
are not claimed as a performance improvement for the theorem or whole project.

## Eleven completion steps and freeze

1. Doctor: inherited clean pushed HEAD 8b669ec and authorized r06 actual baseline;
   fresh native complete baseline 0 errors/18 warnings, no missing dependencies.
2. Prepare: both skills, Phase 4, full five required references and relevant
   naming/style/profiling rules read; original contract and sole caller located.
3. Audit: all 24 items written before the two source additions; all signature widths
   and inequality occurrences accounted for. Initial line arithmetic remeasured exactly.
4. File-level fixes: none in scope; header metadata, imports, definitions and docs preserved.
5. Per-declaration golf: all 42 rules have concrete statuses; actual five search methods,
   native whole-proof/generic/final-goal attempts and public literature inspection recorded.
6. Refactor: exactly approved scoped omission of Fintype/DecidableEq plus local classical.
   No helper, rename, caller edit, wrapper deletion, coefficient widening or codomain change.
7. Module gate: actual lake build Roth.Separation exit 0, 1876 jobs; exact source diff
   2 additions/0 deletions, whitespace check exit 0, 580→582 lines, 25→25 declarations.
8. LSP gate: complete unfiltered fresh final native response, 0 errors/15 warnings/0 infos,
   partial=false, timed_out=false, success=true, failed_dependencies=[]; warnings unsuppressed.
9. Compatibility/independence/axioms: exact new type and non-self independent proof, explicit
   original-class adapter, actual built target and sole caller standard axioms; all 16
   compiler probes completed, including certified hV counterexample. No external direct caller.
10. Simplify/buzz: in-thread full step-back PASS-THROUGH; final isolated actual repository
    profile exit 0 with anchored conservative 128.812 ms and no scaffolding or limit changes.
11. Report/freeze: ALL owned Lean/MCP/compiler/profile requests drained, including final
    profile session 33540, probe batch 73828 and module session 83292. ALL source ownership
    revoked; report-only from this point. Parent owns cumulative original/public/all-actual
    checks, sequential full project and separate LeanEval builds, exact-path commit and
    successful push before the next declaration. No required approval or pending proposal.

Frozen source SHA256: `700e71b2e6acaec6767a0bd483fd17ee0e029340a4b3e745831542b8cc720ab5`.

Worker phase checklist: Step 1 references ✓; Step 2 full audit ✓; Step 2.5 five searches ✓;
Step 2.6 every binder ✓; Step 2.7 all signature widths ✓; Step 2.8 inequality table ✓;
Step 3 all golf rules ✓; Step 4 step-back ✓; Step 5a complete diagnostics ✓;
Step 5b all diff gates ✓; Step 6a renames ✓ (none needed, no sidecar mutation).

## Owner cumulative publication gates

Source FROZEN SHA256 `700e71b2e6acaec6767a0bd483fd17ee0e029340a4b3e745831542b8cc720ab5`; leaf ownership revoked and requests drained before owner gates. Owner probe `55892` exit0,42.65s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL25 actual retained standardaxiom checks. `/private/tmp/roth-separation-r07-compatibility.{lean,log,json}`. Owner build session `59964` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,120.36s/27.69s; source hash stable. `/private/tmp/roth-separation-r07-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.
