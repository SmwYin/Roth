# Fresh helper audit: exists_int_polynomial_of_primitive_factor_aux

Initial audit written before any source edit. Scope: helper and a routine polynomial-range import only; no public contract change. Baseline is 561 lines, helper lines 463–482 (20 declaration lines, 15 body lines after := by). Mathematical content: extract each separated coefficient, use the primitive coefficients' Bezout relation to show the rational univariate coefficient is integral, then lift all coefficients to an integer polynomial.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, cleanup-gates.md, relevant style/naming/profiling references, and cleanup Phase 4. Contract: /private/tmp/roth-separation-worker-contract.md. Source snapshots: /private/tmp/roth-integral-start.lean (current), /private/tmp/roth-separation-d29-first-freeze.lean (exact initial helper).

## Initial audit (24 items)
1. LINT: complete native unfiltered LSP success, 0 errors and 3 existing warnings (header and caller30's Fintype/DecidableEq); zero in helper.
2. HAVE SCAN: hint carries coefficient integrality and feeds choose; h extracts one coefficient of hF and feeds simp. Both substantive. Proposed eliminate hint through direct mem_map_range application, retain coefficient equality h or fold into simpa.
3. SET_OPTION: none.
4. SIMP SQUEEZE: nonterminal simp only [coeff_rename_mul_aeval, coeff_map] is explicit; simp only on finite reconstruction is nonterminal, final simp is terminal. Proposed remove reconstruction entirely.
5. NAMING: name states existence of integral polynomial from primitive factor, snake_case, private _aux, no forbidden pattern or abbreviation. No rename justified.
6. LINE PACKING: measured table below; inspect final packing after candidate.
7. BY PLACEMENT: := by at end of conclusion line.
8. FORMAT: two-space proof indent, no blank body line, no haveI/letI, no tactic semicolons.
9. COMMENTS: zero helper proof comments; preserve all surrounding documentation.
10. DOCSTRING: private helper has none, appropriate.
11. VISIBILITY: private internal lemma, exactly one call in exists_int_factors.
12. STRUCTURE: 15 proof-body lines, no conjunction conclusion; coefficient extraction 6 lines and finite reconstruction 7 lines. Remove reconstruction using library API; no new helper.
13. MATHLIB: all five actual searches below find range characterization, not this full primitive-factor result. It replaces a subargument; retains nontrivial coefficient/primitivity reasoning.
14. JUNK DEF: n/a lemma.
15. EXISTS LEMMA: not a reflexive witness wrapper; requires Bezout/integrality argument.
16. SHOW vs CHANGE: no show.
17. PUSH_NEG: none.
18. GENERALISE: effective binders τ,U,V',F,hgcd,hF, no Fintype/DecidableEq. Every-binder probes will be compiled separately; initial pending evidence, no untested compiler claim. Concrete ℤ/ℚ bridge is the content; no generic ring substitution preserves the cast/integrality lemma without extra structure.
19. INEQUALITY: zero order inequalities in type/hypotheses/body; arrows →+* and ↦ are not inequalities.
20. NORMAL-FORM: polynomial map equality is canonical witness target, matches call site. Coefficient-wise range is canonical intermediate provided by mem_map_range.
21. SYNTAX-GEN: keep existential map equality, directly consumed by the equality helper; no restatement needed.
22. IMPORT-FANOUT: candidate adds Mathlib.Algebra.Polynomial.Eval.Subring, small canonical polynomial API; parent authorized. Check actual module and downstream import/use search before acceptance.
23. CASTS: existing (X none : MvPolynomial (Option τ) ℚ) disambiguates coefficient algebra; (fun P ↦ P.coeff ...) inferred. Integer/rational coercion is essential content. Reaudit final diff.
24. INSTANCE-NAME: n/a no instance declaration.

## Five actual search methods
A Lean-Finder: query polynomial with integer coefficients belongs to range integer polynomial map; returned Polynomial.mem_map_range, mem_map_rangeS, lifts_iff_set_range.
B Loogle: Polynomial.mem_map_range; exact ring range coefficient characterization found (actual native tool success).
C LeanSearch: polynomial coefficients in range ring homomorphism polynomial map range; found mem_map_range, liftsRing, MvPolynomial variants.
D Source rg: exact mem_map_range in .lake/packages/mathlib/Mathlib/Algebra/Polynomial/Eval/Subring.lean lines 33–51; inspected complete file, including constructive finite sum proof.
E lean_local_search Polynomial.mem_map_range: returned both declarations from source, index unavailable (presence confirmed; no absence inference).
Library helper replaces reconstruction only. Full helper search/automation probes remain to be compiled. No claim of global mathlib absence.

## Initial line packing (codepoints)
| Signature row | Chars | Next semantic token | Width arithmetic | Action |
|---|---:|---|---|---|
| 463 | 82 | `{V' : Polynomial ℚ} {F : MvPolynomial (Option τ) ℤ} (hgcd : U.support.gcd U.coeff = 1)` | 82 + 1 + 86 = 169 | recheck final packing |
| 464 | 90 | `(hF : map (Int.castRingHom ℚ) F = rename some (map (Int.castRingHom ℚ) U) *` | 90 + 1 + 75 = 166 | recheck final packing |
| 465 | 79 | `Polynomial.aeval (X none : MvPolynomial (Option τ) ℚ) V') :` | 79 + 1 + 59 = 139 | recheck final packing |
| 466 | 65 | `∃ V : Polynomial ℤ, V.map (Int.castRingHom ℚ) = V' := by` | 65 + 1 + 56 = 122 | recheck final packing |
| 467 | 60 | `` | body next | ok |

## Inequality occurrence table
| Scope | Occurrences | Action |
|---|---:|---|
| Signature + all hypotheses + full body | 0 `<`, `≤`, `>`, `≥` order comparisons | none |

## Literature exemption
n/a: private decl, literature search not required. Mechanical binder audit still required.

## Initial action
Compile the exact initial type with an independent proof using Polynomial.mem_map_range under its defining import. If successful and performant, apply only import + helper proof simplification; preserve all types and calls. No new helper or pending public proposal.

## Final generalisation status: every effective binder
The exact INITIAL type compiled as integralIndependent without Fintype/DecidableEq or any replacement instance, and without classical. This is the positive simultaneous omitted-instance probe. Binder deletions used autoImplicit false in scratch only; source stays unchanged. Negative deletion tests show dependency of this proof/type, not a general impossibility theorem.

| Binder | Candidate / compiled test | Result | Resolution |
|---|---|---|---|
| τ : Type* | delete binder | unknown τ in polynomial types (retry fixes scratch variable syntax) | retain universe-polymorphic index |
| U : MvPolynomial τ ℤ | delete binder | unknown U in hgcd/hF after completed retry | retain primitive factor |
| V' : Polynomial ℚ | delete binder | unknown V' in hF/conclusion | retain target polynomial |
| F : MvPolynomial (Option τ) ℤ | delete binder | unknown F in hF/coefficient extraction | retain integral source |
| hgcd : U.support.gcd U.coeff = 1 | delete hypothesis | unknown hgcd in Bezout integrality step | retain primitivity assumption |
| hF : separated factorization | delete hypothesis | unknown hF / coefficient equality remains unsolved | retain factorization |
| ambient Fintype τ | omitted from effective type; exact type compiles | positive pass | already absent |
| ambient DecidableEq τ | omitted from effective type; exact type compiles | positive pass | already absent |

Raw probes: /private/tmp/roth-integral-drop-*.lean and .log, /private/tmp/roth-integral-binders.json (records first U import failure, superseded by -U-retry.log). No order, topology, injectivity, strict/weak, pointwise or bundled-structure hypotheses to weaken. ℤ/ℚ carry the mathematical integrality content; replacing ℚ by Field K would require replacing the rational integrality interface with a different general theorem (not a tested mechanical weakening), outside this helper's intended role. Inversion: no named special construction vanishes after unfolding; U,V',F stay used for the coefficient calculation. No public proposal or new helper.

## Full 42-rule golf pass
| Rule | Concrete status |
|---|---|
|1.1|n/a: no by exact wrapper.|
|1.2|n/a: no by rfl.|
|1.3|n/a: no adjacent rw/exact in final proof.|
|1.4|Already uses terminal simpa using h.symm.|
|1.5|n/a: no trailing rfl.|
|1.6|Already uses anonymous coefficient witness ⟨..., proof⟩.|
|1.7|n/a: apply range equivalence generates coefficient goal; not an apply/exact pair.|
|1.8|n/a: no contradiction/negation block.|
|1.9|n/a: coefficient extraction lambda is not an eta expansion.|
|1.10|Eliminated hint; h is retained to expose its coefficient equality to simplification.|
|1.11|Considered refine ... fun b; current apply/intro separates library reduction and coefficient step clearly; no need to churn one line.|
|1.12|n/a: no show.|
|1.13|Applied obtain ⟨z,hz⟩ to integrality witness.|
|1.14|n/a: no rw chain after range replacement.|
|1.15|Removed finite-sum terminal branch, no terminal simp only remains.|
|1.16|Remaining nonterminal simp only [coeff_rename_mul_aeval, coeff_map] is squeezed.|
|1.17|Uses .2 and hz.symm / h.symm.|
|1.18|No avoidable parenthesized by term; tuple requires comma/body grouping.|
|1.19|n/a: no push_neg.|
|1.20|Not a trivial reflexive existential; arithmetic coefficient argument retained.|
|2.1|Actual native lean_multi_attempt grind failed with existential nonimage contradiction unresolved.|
|2.2|n/a: no grind retained.|
|2.3|Coefficient equality already consolidated with simpa using.|
|2.4|n/a: no analytic function property.|
|2.5|n/a: no positivity/nonzero goal.|
|2.6|n/a: no ordered congruence goal.|
|2.7|n/a: no linear Nat/Int arithmetic goal; gcd integrality is structural.|
|2.8|Actual native aesop failed, no progress on whole helper.|
|2.9|n/a: no concrete arithmetic; casts are normalized by coefficient-map simp.|
|2.10|n/a: unbounded polynomial existence not a finite decision problem.|
|2.11|n/a: no denominator identity.|
|2.12|n/a: no ring/ring_nf ending or linear identity with additive hypotheses.|
|2.13|n/a: no symmetric cases.|
|2.14|n/a: no calc chain.|
|2.15|n/a: final proof has a single coefficient equality subgoal.|
|3.1|n/a: no erw.|
|3.2|n/a: no continuity/measurability.|
|3.3|n/a: no omega/lia.|
|3.4|n/a: no rfl case-substitution.|
|3.5|n/a: private single-use integrality step; automation attribute would broaden search without demonstrated use.|
|3.6|n/a: no simp_all only.|
|3.7|n/a: no heartbeat/recursion option.|

## Step-back review
Actual native whole-goal grind/simp/aesop/exact? failed (all completed, no timeout); exact? reported it could not close this goal before the helper body. Library mem_map_range changes the strategy productively: no manual support sum, choice function or support cases. The retained helper still combines extraction of a bivariate coefficient with Bezout integrality; it is not a direct one-to-three-library-call wrapper. Keeping the mathematical integrality boundary gives main29 an 11-line assembly proof. No further extraction justified and no helper was added.

## Final line packing
Reference: exact initial-type @integralIndependent rendered by set_option format.width 100; raw /private/tmp/roth-integral-independent.log. All five signature lines unchanged.

| Sig line | Chars | Next semantic token | Arithmetic | Action |
|---|---:|---|---|---|
|464|82|`{V' : Polynomial ℚ}` (19)|82+1+19=102 >100|ok|
|465|90|next factorization hypothesis prefix (75)|90+1+75=166 >100|ok|
|466|79|`Polynomial.aeval ... V') :` (59)|79+1+59=139 >100|ok|
|467|65|full existential conclusion (56)|65+1+56=122 >100|ok|
|468|60|body next|n/a|ok|

The splits inside hF occur at the product boundary and after its binder; joining the whole next application/conclusion exceeds 100. No long-line issue in helper. Inequality scan unchanged: no order inequalities in full helper. Lambda ↦ and ring-hom arrow are excluded. Naming matches no forbidden pattern; no renames queued. Comments-preserved: none in helper, surrounding module and theorem documentation byte-preserved.

## New identifier verification / casts / imports
Polynomial.mem_map_range verified by native local search, actual Loogle/LeanSearch/Lean-Finder, complete source inspection at defining import, and successful exact-type compilation. All remaining proof names already present in initial helper or source. Import Mathlib.Algebra.Polynomial.Eval.Subring is a canonical, small coefficient-range API and passed actual lake build. Direct downstream module found by rg: Roth.Theta. No public signatures or new instances introduced; parent runs its cumulative full-project/LeanEval gates. Cast audit: no new explicit cast ascription; ℤ→ℚ bridge and (X none : MvPolynomial (Option τ) ℚ) retained as essential/load-bearing.

## Verification evidence
- Exact INITIAL helper type and independent NONSELF proof: /private/tmp/roth-integral-independent.lean, exit 0, /private/tmp/roth-integral-independent.log. Proof references only public Roth.exists_int_eq_of_gcd_eq_one and Roth.coeff_rename_mul_aeval plus mathlib, never target helper.
- Actual module /Users/ramin/.elan/bin/lake build Roth.Separation: exit 0, built target in 19s; /private/tmp/roth-integral-build.log. Includes full main29 and caller30 checking.
- Complete unfiltered native LSP: /private/tmp/roth-integral-final-lsp.json, partial false, success true, timed_out false, 0 errors, 3 warnings, no infos, no failed dependencies; exactly baseline warnings (user-preserved header; caller30's Fintype/DecidableEq pending parent approval scope).
- Actual built target suffix found in environment: _private.Roth.Separation.0.Roth.exists_int_polynomial_of_primitive_factor_aux. /private/tmp/roth-integral-axioms.lean and .log, exit 0. Target plus actual Roth.exists_int_factors and Roth.exists_det_eq_mul all depend only on [propext, Classical.choice, Quot.sound]. Independent proof same three standard axioms.
- Focused diff /private/tmp/roth-integral-diff.patch: exactly one import and helper proof; signatures/call sites/other proofs unchanged. 561→555 module lines (-6); helper 20→13 declaration lines (-7), 15→8 body lines (-7); main29 remains 11 proof lines; retained declaration count remains 27.

## Gate status (scoped worker)
| Gate | Result | Evidence |
|---|---|---|
|lake_build_file|pass|actual lake build Roth.Separation exit 0 log above|
|definition_protected|pass|no definition or abbreviation edit|
|theorem_statement_protected|pass|exact signature bytes preserved|
|structure_gate|pass|8-line body, no conjunction or large branch; main29 unchanged 11|
|naming_gate|pass|descriptive mathematical snake_case private _aux, no forbidden token|
|line_packing_gate|pass|five measured rows and width-100 reference above|
|inequality_orientation_gate|pass|zero order comparisons in helper|
|target/caller local compatibility|pass|module build plus actual axioms|
|whole-project / LeanEval cumulative|parent responsibility|explicit dispatch, not claimed locally|

## Simplify pass (scoped manual equivalent)
No built-in simplify callable is exposed. Performed substantive holistic review: reuse range API, no manual finite reconstruction, no duplicate coefficient route, retained nontrivial mathematical helper, no new helper. Outcome ISSUES-FOUND-AND-FIXED: range reconstruction removed; module and native LSP rechecked.

## Eleven completion-step checklist
- [x] Step 1: reference documents read.
- [x] Step 2: initial full 24-item audit written before edits.
- [x] Step 2.5: five actual search-method statuses recorded.
- [x] Step 2.6: every effective binder audited with actual probes and explicit private literature exemption.
- [x] Step 2.7: per-signature-line width table and format.width reference.
- [x] Step 2.8: inequality occurrence table.
- [x] Step 3: all 42 golf-rule statuses.
- [x] Step 4: actual automation attempts and step-back strategy review.
- [x] Step 5a: complete unfiltered native diagnostics.
- [x] Step 5b: diff/build/independent type/actual axiom gates; final profile evidence appended below.
- [x] Step 6a: no rename warranted, sidecar untouched per ownership scope.

Additional scoped audit notes: the first U deletion attempt encountered a transient missing Separation.olean during the authorized module rebuild; the completed retry is the valid dependency probe. τ scratch syntax was corrected and rerun; its completed retry gives only unknown-τ dependency errors. Both retries exited 1, as expected for binder deletions. No mathematical impossibility is inferred from these syntactic dependency probes. Full strict-weak and pointwise catalogue: hgcd is an equality in ℤ, with no ordered or point-local property to weaken; hF is the global equality needed to extract all b and supported a coefficients. A coefficientwise premise could encode precisely the consumed consequence but would move extraction back into main29 and restate the helper's interface; no such new public/private API is applied or claimed compiler-tested. The retained global equation is canonical and directly available at the only caller.

## Buzz pass — actual repository module, all other owned requests drained first
Outcome: FAST-BOARD for target and affected actual callers; no over-budget declaration in full sweep. No limits raised, no profiler scaffolding, no deferred target issue. Exact invocation exited 0:
`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Separation.lean`

Raw final log /private/tmp/roth-integral-drained-profile.log; anchored parsed table /private/tmp/roth-integral-drained-profile.log.json. Parser /private/tmp/roth-separation-profile-table.py selects actual named declaration outer command and outer async proof; uses maximum overlapping command wrapper (not sum of nested nodes), plus outer proof conservatively. Baseline accepted uncontended actual-module /private/tmp/roth-rescale-drained-profile.log(.json) on unchanged starting source.

| Actual declaration | Baseline ms | Final command ms | Final async proof ms | Conservative final ms |
|---|---:|---:|---:|---:|
|exists_int_polynomial_of_primitive_factor_aux|410.504|44.308|283.557|327.865|
|exists_int_factors|484.287|101.770|448.785|550.555|
|exists_det_eq_mul|583.871|113.589|453.340|566.929|

All target/affected values below750, so no repeat trigger in owned scope. Full table also reports unchanged earlier exists_coeffNone_basis_aux at767.672ms (accepted baseline764.058ms), eq_sum_aeval_basis_coeffNone_aux at749.659ms (baseline765.952ms). These unrelated helpers are unedited and already have baseline/final sweeps; parent will apply cumulative profiling gates after next fresh equality-helper audit. No claim of global performance improvement. No source changes after this measurement.

## Final result and freeze
Audit issue resolved: manual finite coefficient reconstruction replaced by standard Polynomial.mem_map_range with its defining import. Helper body15→8; declaration20→13; module561→555; retained27. Main29 unchanged11 proof lines. No new helper, public proposal, rename, pins/docstring/header change, Git mutation or shared log write.

All native Lean requests, all scratch compilers (including failed deletion retries), independent proof, module build, actual axioms compiler, and final profile process completed and drained. This worker revokes ALL source ownership, including the helper/import/call sites, and is now REPORT-ONLY. Parent may continue with fresh equality-helper audit and cumulative gates; this is not a whole-batch completion claim.

Frozen source: /private/tmp/roth-separation-d29-integral-freeze.lean.
SHA256: `a61cb09884b63b8383da431a329a15dd937b10680f08fb5398530371c50aba72`.
