# exists_separated_representation — original21 initial audit

Before editing: HEAD 499b6fa; source 551 lines. Baseline supplied actual repository profile `/private/tmp/roth-separation-d18-direct-final-profile.log`: 35.370 ms command + 1202.250 ms async = 1237.620 ms. Complete native LSP obtained, 0 errors / 31 warnings. Exact public statement, assumptions, conclusion and docstring protected.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md.

1. LINT: unused inherited Fintype/DecidableEq warnings are pending public API decisions, preserved.
2. HAVE SCAN: finite-dimensional instance retained; hmem repeated basis inputs; hP' reconstruction retained; hψexp coordinate reconstruction retained; hl1 positivity retained; nested witness/nonzero proofs retained; hln dimension bound retained; hVW degree span inclusion extracted; hcoeff/h1/hf independence extracted. Every one has mathematical content; no trivial single-use term wrapper.
3. SET_OPTION: none.
4. SIMP: terminal simp in contradiction; terminal simpa in coordinate reconstruction; nonterminal simp only in coefficient identity; terminal simpa in linear-map restriction. Preserve semantics, extract at mathematical boundaries.
5. NAMING: exists_separated_representation describes existential independent separation; no forbidden abbreviations/patterns, no rename.
6. LINE PACKING: original exact public type is protected; measured table to follow, proof-only edits.
7. BY: already attached.
8. FORMAT: two spaces; change new lambdas to ↦; no haveI/letI.
9. COMMENTS: no original proof inline comments; preserve full source docstring.
10. DOCSTRING: detailed source attribution, protected.
11. VISIBILITY: headline public theorem; helpers will be private.
12. STRUCTURE: 64-line proof (actual count; dispatch estimated ~67) over budget; extract independence of coordinate polynomials, degree-bounded coefficient span, and basis reconstruction; target every proof ≤30, main as short as practical.
13. MATHLIB: actual LeanFinder, Loogle, LeanSearch, local name searches run; results give monomial basis and generic nondegenerate sums, not direct separation. Source search and compiled generic-route probe follow before extraction.
14. JUNK DEF: n/a theorem.
15. EXISTS LEMMA: n/a public substantive theorem.
16. SHOW: none.
17. PUSH_NEG: none.
18. GENERALISE: all effective binders τ/Fintype/DecidableEq/K/Field/P/hP/n/hn will be probed; no public weakening applied without authorization.
19. INEQUALITY: ≤ already canonical throughout statement; positive dimension uses 0 < l; per-occurrence table follows.
20. NORMAL-FORM: finite sum of separated factors with independent families is intended canonical tensor-rank representation; preserve.
21. SYNTAX-GEN: Fin l supports determinant consumers; no restatement proposed.
22. IMPORT-FANOUT: no imports added.
23. CASTS: b-coercions subtype→polynomial and Fin→Nat are genuine; expected-type annotations remain where needed.
24. INSTANCE-NAME: n/a theorem; anonymous finite-dimensional local evidence retained.

Literature: actual web search found coefficient-space formulation in https://www.cse.iitk.ac.in/users/manindra/Students/thesis_arpita.pdf and https://image.informatik.htw-aalen.de/~thierauf/Papers/sumROABP.pdf ; consistent with choosing a basis of partial coefficient span. No public alternative required. Private helper audits exempt from literature search.

Initial actions: extract substantive private mathematical lemmas and measure actual module; preserve all public API pending decisions. All new helpers require fresh independent owner audits before final checkpoint.

## Five-method mathlib search and generic-route probe

| Method | Actual query/action | Result |
|---|---|---|
| A LeanFinder | `Polynomial finite sum coordinate polynomials linearly independent spanning family basis` | Monomial bases and degreeLT basis; no direct separation specialization returned. Raw `/private/tmp/roth-d21-search1.json`. |
| B Loogle | `LinearIndependent _ (fun _ => ∑ _, _)` | `LinearIndependent.sum_smul_of_nondegenerate`, partial matrix route requiring nondegeneracy; raw search2. |
| C LeanSearch | `polynomial separated representation linearly independent coefficient span basis` | `Polynomial.Sequence.linearIndependent`, basisMonomials, representation API; raw search3. |
| D source | `linearIndependent.*(coeff|sum)`, `coeff.*linearIndependent` in LinearAlgebra/Basis, LinearIndependent, Algebra/Polynomial | Generic sum independence, no immediate direct theorem. Actual source read confirms basis.sum_repr, repr_self, coord_apply. |
| E local names | `linearIndependent` | Existing basis and monomial API, index warming (not proof of absence); raw search0. |

Compiled/live generic route: `exact?` at the actual public theorem goal fails; `grind` fails and `aesop` does not close. `/private/tmp/roth-d21-attempts.json`. Therefore keep substantive local theorem using mathlib basis/span APIs; do not claim global theorem absence. Auxiliary variants checked: basisMonomials, sum_smul_of_nondegenerate, repr, repr_self_apply, coord_apply, span_span_coe_preimage. Common-equivalents buckets do not match algebraic separation. No new public API/import/automation attributes. ChatGPT math MCP unavailable in exposed tool inventory. Actual literature search records coefficient-space basis formulation; top three relevant primary hits are thesis_arpita.pdf, PITAndLowerBoundsForSumABPs.pdf, and sumROABP.pdf linked above.

## All 42 golf rules

| Rule | Concrete status |
|---|---|
| 1.1 | n/a: no by-exact wrapper. |
| 1.2 | n/a: no by-rfl declaration. |
| 1.3 | Existing reconstruction rw+exact remains two mathematical steps (rewrite finite index, then apply expansion); no repeated closing rewrite. |
| 1.4 | Applied coordinate coercion via simpa; narrowed terminal simplification for measured performance. |
| 1.5 | n/a: no trailing rfl. |
| 1.6 | Applied/retained anonymous constructors for all existential/conjunction witnesses. |
| 1.7 | n/a: no adjacent apply+exact of same lemma. |
| 1.8 | Retained by_contra! in coefficient nonzero witness. |
| 1.9 | Removed obsolete hmem/a lambdas from public proof; remaining indexed lambdas construct data. |
| 1.10 | Inlined hln; removed unused public hmem and hψexp by extracting actual mathematical content. |
| 1.11 | Retained refine+fun for summand equalities. |
| 1.12 | n/a: no show. |
| 1.13 | Retained obtain for nonzero coefficient and span generator; no have projections. |
| 1.14 | All adjacent rewrites already merged where they act on one goal; sum_congr steps separate distinct sums. |
| 1.15 | Performance exception: preserve newly squeezed terminal simp only lists after traces showed failed univ_eq_empty discharge dominating broad simp. |
| 1.16 | Nonterminal coefficient simp only and simp_rw are explicit; no nonterminal bare simp. |
| 1.17 | Retained .trans/.trans_eq/.map'/.linearIndependent dot notation. |
| 1.18 | n/a: no helpful parenthesis-only change; constructor boundaries are load-bearing. |
| 1.19 | n/a: no push_neg. |
| 1.20 | n/a: all helpers prove substantial universal linear algebra/degree/reconstruction content, no trivial existential helper. |
| 2.1 | Actual whole-goal grind fails; saved attempts. |
| 2.2 | n/a: no grind kept. |
| 2.3 | Applied precise simpa only to subtype scalar coercion. |
| 2.4 | n/a: no analytic function-property goals. |
| 2.5 | n/a after direct finrank positivity application; no positivity arithmetic tactic needed. |
| 2.6 | Degree bounds use degreeOf_add_le/max_le and natDegree_sum_le APIs directly; no scalar monotonicity calc block to replace. |
| 2.7 | Removed obsolete omega: the finrank positive lemma already has definitionally the desired 1 ≤ l type. |
| 2.8 | Actual whole-goal aesop fails; saved attempts. |
| 2.9 | n/a: no concrete numeral computation or numeric cast equality. |
| 2.10 | n/a: existential field-polynomial construction is not finite decidable computation. |
| 2.11 | n/a: no divisions/denominators. |
| 2.12 | Actual live linear_combination closes final commutative identity, as does ring; retain ring for direct normalisation without irrelevant hypothesis search. |
| 2.13 | n/a: no symmetric branches. |
| 2.14 | n/a: no calc. |
| 2.15 | n/a: remaining obligations use different mathematical lemmas; no duplicate terminal goals. |
| 3.1 | n/a: no erw. |
| 3.2 | n/a: no continuity/measurability. |
| 3.3 | Applied by eliminating redundant omega (see 2.7). |
| 3.4 | Retained obtain rfl for span-subtype representative. |
| 3.5 | n/a: one proof's private steps should not become global automation rules. |
| 3.6 | n/a: no simp_all. |
| 3.7 | n/a: no limit setters; none added. |

## Step-back review / simplify

The public proof contains the two remaining mathematical choices: coefficient span basis and nonzero span. Its three helpers prove independence of coordinate polynomials, closure of partial-degree bounds under spans, and reconstruction in a new basis. Generic automation cannot choose that basis, confirmed by live exact?/grind/aesop attempts. Reconstruction now consumes the coefficient expansion also used for positivity instead of recomputing it, and its temporary local `a` prevents rewriting coefficients inside b.repr. A different tensor-product or matrix-rank proof adds transport and imports without simplifying these degree bounds. Local have blocks retain reused statements or deliberate expected-type boundaries. No source comments/docstrings removed, no redundant arithmetic tactic remains. Simplify outcome: ISSUES-FOUND-AND-FIXED by this manual equivalent review; no separate built-in simplify tool is exposed.

## Generalisation and every effective binder

Compiler probes are generated by `/private/tmp/roth-d21-probes.py`, summary `/private/tmp/roth-d21-probe-results.json`; each file/log uses matching `/private/tmp/roth-d21-NAME.{lean,log}`. These are actual independent original proofs with autoImplicit disabled. Deleting τ/K/P/n tests dependent parameters and produces compiler errors; it is not a theorem that these binders can vanish. Deleting hP/hn tests actual proof dependence. Field→DivisionRing fails commutative coefficient requirements; Field→CommRing fails vector-space finite-dimensional construction. Dropping DecidableEq succeeds; Fintype→Finite succeeds with a local Fintype.ofFinite; dropping Fintype alone or both instances fails existing dependency signatures. These public changes remain pending under the coordinator's existing instance menu, none applied. Strict→weak: hn is already weak ≤, and the essential hP ≠ 0 supports l ≥ 1; no further valid scalar weakening. Pointwise/global: no global regularity hypothesis. Universe: Type* already polymorphic. Inversion: no distinguished concrete object, only arbitrary P/K/τ. Every τ-instance was removed from new helpers; they use mathlib support transport directly and a supplied expansion.

## Final signature packing (codepoints)

Each next fragment is a complete binder or displayed expression fragment, not a byte count. Exact public mathematical type stays unchanged. Types are printed by the actual axiom/type probe at format.width 100.

### linearIndependent_coordinate_polynomials_aux

| Source line | Width | Next displayed fragment width | Arithmetic | Action |
|---|---:|---:|---|---|
| 218 | 85 | 62 | 85+1+62=148 | ok |
| 219 | 66 | 63 | 66+1+63=130 | ok |
| 220 | 67 | 47 | 67+1+47=115 | ok |
| 221 | 51 | 93 | 51+1+93=145 | ok |
| 222 | 99 | none | n/a | ok |
### degreeOf_mem_coeffNone_span_aux

| Source line | Width | Next displayed fragment width | Arithmetic | Action |
|---|---:|---:|---|---|
| 248 | 74 | 62 | 74+1+62=137 | ok |
| 249 | 66 | 79 | 66+1+79=146 | ok |
| 250 | 83 | 45 | 83+1+45=129 | ok |
| 251 | 49 | none | n/a | ok |
### eq_sum_aeval_basis_coeffNone_aux

| Source line | Width | Next displayed fragment width | Arithmetic | Action |
|---|---:|---:|---|---|
| 265 | 75 | 41 | 75+1+41=117 | ok |
| 266 | 45 | 76 | 45+1+76=122 | ok |
| 267 | 80 | 27 | 80+1+27=108 | ok |
| 268 | 31 | 71 | 31+1+71=103 | ok |
| 269 | 77 | 82 | 77+1+82=160 | ok |
| 270 | 86 | 73 | 86+1+73=160 | ok |
| 271 | 81 | 68 | 81+1+68=150 | ok |
| 272 | 78 | none | n/a | ok |
### exists_separated_representation

| Source line | Width | Next displayed fragment width | Arithmetic | Action |
|---|---:|---:|---|---|
| 298 | 92 | 28 | 92+1+28=121 | ok |
| 299 | 32 | 85 | 32+1+85=118 | ok |
| 300 | 89 | 76 | 89+1+76=166 | ok |
| 301 | 82 | 49 | 82+1+49=132 | ok |
| 302 | 55 | 94 | 55+1+94=150 | ok |
| 303 | 100 | none | n/a | ok |

## Inequality orientation scan

| Declaration | Occurrences | Rewrite | Rename |
|---|---|---|---|
| linearIndependent_coordinate_polynomials_aux | no ≥ or > in signature | n/a | n/a |
| degreeOf_mem_coeffNone_span_aux | no ≥ or > in signature | n/a | n/a |
| eq_sum_aeval_basis_coeffNone_aux | no ≥ or > in signature | n/a | n/a |
| exists_separated_representation | no ≥ or > in signature | n/a | n/a |

Public positive/degree bounds already use `1 ≤ l`, `l ≤ n + 1`, `natDegree ≤ n`, and `degreeOf ≤ degreeOf`. Helpers use `degreeOf ≤ degreeOf`; finite-index `<` is supplied by Fin, never reversed.

## Private-helper initial audits and ownership handoff inventory

All three are substantial private mathematical lemmas, not 1–3-call wrappers or single-use existential witness packaging. Each needs the coordinator's fresh independent owner audit after this worker freezes; this section is the implementation audit, not a claim that those later independent audits have happened.

| Exact source name | Frozen source span | Proof-body lines | Mathematical content | Instances |
|---|---:|---:|---|---|
| `linearIndependent_coordinate_polynomials_aux` | 218–245 | 23 | Coordinate polynomials of a spanning family in any finite basis are linearly independent | CommRing R, AddCommMonoid M, Module R M; no τ assumptions |
| `degreeOf_mem_coeffNone_span_aux` | 248–262 | 11 | All elements of the coefficient span satisfy the original partial-degree bounds | CommSemiring R; arbitrary τ |
| `eq_sum_aeval_basis_coeffNone_aux` | 265–290 | 18 | A finite coefficient expansion becomes a separated sum along any basis of its coefficient span | CommSemiring R; arbitrary τ |

Exact source snapshots are `/private/tmp/roth-d21-NAME.lean.txt` for each name in the table, with inventory `/private/tmp/roth-d21-source-spans.json` and entire frozen source `/private/tmp/roth-d21-final-source.lean`. Actual environment types (including universes/implicit arguments) and suffix-resolved private names appear in `/private/tmp/roth-d21-axioms-final.log`. No guessed private numeric-name lookup was used. They are all necessary to split original21 into mathematically separate elaboration units; no helper only packages existential data or renames an imported theorem.

Initial helper audit covering the same 24 items: no local warnings; hcoeff/hf and hexp/h are reused semantic equalities or coordinate-restriction proofs; no limit/suppression setters; terminal simpa only is the measured performance exception described above; names describe the content with auxiliary suffix; every signature ≤100 codepoints and table above; by attached, two-space proof structure, no inline comments/docstrings to delete, private visibility, ≤30 proof lines, mathlib basis/span/support APIs used directly, not defs or trivial ∃ lemmas, no show/push_neg, scalar/binder weakening actually compiled as recorded next, inequalities canonical, no new normal forms or automation attributes, no new imports, genuine Fin→Nat/subtype coercions retained, no instance declarations. The upcoming fresh independent audits must perform their own full binder/search/golf verification of final frozen helper types.

Private mechanical results: `/private/tmp/roth-d21-helper0-commRing.lean` compiles independence with CommRing + AddCommMonoid; CommSemiring fails the Ring-based Fintype.linearIndependent_iff rewrite, as recorded in helper0_semiring/helper0_addMonoid logs. helper1_semiring/helper2_semiring compile over CommSemiring. Applied all these private weakenings. Final reconstruction improves further on the tested previous transport proof by consuming the expansion, so it no longer needs to prove a degree-bound expansion internally. All final helper types and proofs are confirmed by actual module build7 and actual final suffix-resolved axiom/type checks. Public Field/Fintype/DecidableEq contracts stay byte-identical.

## Identifier and cast checks

| New direct API reference | Verification |
|---|---|
| `LinearMap.sum_apply`, `LinearMap.smul_apply`, `LinearMap.zero_apply` | Successful live only-list test, then actual module build |
| `Module.Basis.coord_apply`, `Module.Basis.repr_self` | Basis/Defs source search, live simp? output, actual module build |
| `Submodule.coe_smul` | Live narrowed coordinate reconstruction, actual module build |
| `mem_support_coeff_optionEquivLeft` | MvPolynomial polynomial source and successful generic degree-span compile/module build |
| `Finset.sum_ite_eq` | Live simp? output and actual module build |

New helper names are declared locally, not imported guesses. Cast audit: Fin→Nat exponent coercions and basis-subtype→MvPolynomial coercions are genuine bridges. `(p : Polynomial R)` in congrArg fixes the elaboration source, and the `Submodule.span R _ ≤ W` annotation fixes the constructed degree-bounded submodule. No redundant output cast or instance ascription was added.

## Concrete validation gates

| Gate | Result / actual evidence |
|---|---|
| `lake_build_file` | `/Users/ramin/.elan/bin/lake build Roth.Separation` → exit 0; `/private/tmp/roth-d21-build7.log` ends `Build completed successfully (1876 jobs).` |
| Complete native LSP | `/private/tmp/roth-d21-final-lsp2.json`: partial=false, timed_out=false, success=true, 0 errors / 31 warnings. Baseline 31 retained warnings; none added. |
| Original isolated type/non-self proof | `/private/tmp/roth-d21-independent.lean` uses the original 64-line proof, not the public theorem or new helpers; equality of original/public constants by rfl checks exact original public type. Final compile exit 0, `/private/tmp/roth-d21-independent-final.log`. |
| Actual target/helper axioms | `/private/tmp/roth-d21-axioms.lean` enumerates exact suffixes from the built environment; final compile exit 0, `/private/tmp/roth-d21-axioms-final.log`. Only propext, Classical.choice, Quot.sound for all four actual constants. |
| definition protected | No existing def/abbrev change. |
| statement protected | Original public statement bytes, effective assumptions, conclusion and full docstring unchanged; surrounding source byte-identical outside target+three helpers. |
| structure | Original actual proof-body count 64 (dispatch approximation ~67); final 25, helpers 23/11/18. No >30 proof or >10 case branch. Main contains necessary basis/nonzero construction; fourth helper solely to force 15 lines would add another audit unit. |
| naming | All names mathematical snake_case; no forbidden abbreviation/pattern. No rename proposed. |
| width / inequalities | Full tables above; no reverse inequalities. |
| cumulative project / LeanEval | Coordinator owns sequential full project and separate LeanEval gates after required fresh helper audits and freeze; this worker does not claim those have run. |

Line arithmetic against the dedicated pre-edit snapshot: 551 → 587 source lines, +36; diff +95/−59. Public proof 64 → 25 (39 fewer body lines), with 52 proof-body lines in substantive private lemmas. Comments-preserved: no original inline proof comments; full original public documentation preserved. No profile scaffolding, limit raises, sorry, custom axioms, native_decide, haveI/letI or warning suppression introduced.

## Eleven-step completion checklist

- [x] Step 1: required references read.
- [x] Step 2: all 24 audit items recorded before edits.
- [x] Step 2.5: all five actual mathlib search methods and generic-route proof attempt.
- [x] Step 2.6: every effective public binder probed, private scalar/binder minimization compiled, public literature searched, pending approvals respected.
- [x] Step 2.7: full per-signature codepoint width tables.
- [x] Step 2.8: inequality scan tables.
- [x] Step 3: all 42 golf rules have concrete status.
- [x] Step 4: mathematical step-back / equivalent simplify review performed.
- [x] Step 5a: complete unfiltered native LSP passed, baseline warnings preserved.
- [x] Step 5b: actual module, exact original proof/type, actual axioms and protected-diff gates passed; isolated final profiles recorded below.
- [x] Step 6a: no rename needed; no shared rename/progress/Git mutation.

## Buzz: measured diagnosis, fixes, and isolated final actual-module sweep

Outcome: **FIXED**, no deferral and no limit raise. All measurements use actual `Roth/Separation.lean` repository declarations, with the conservative outer-command + outer-async-proof convention. Nested trace nodes are not added twice.

Baseline unchanged public proof: `/private/tmp/roth-separation-d18-direct-final-profile.log`, command 35.370 + async 1202.250 = **1237.620 ms**. Initial decomposition alone was insufficient: profile1 gave independence 1188.912, reconstruction 1309.477 and main 1045.116 ms. Subsequent profile2 gave independence 717.451, reconstruction 1070.072 and main 683.608 ms; profile3 after narrower independence, but before all final fixes, gave independence 451.018, reconstruction 1525.743, main 893.457. Those over-budget and ≥750 samples prompted the final changes rather than a deferral or concurrency exemption.

Trace root cause: broad independence `simpa [f,a]` and `simpa [f,Finsupp.single_apply]` triggered repeated failing `Finset.univ_eq_empty` discharges (approximately 97+140+200 ms in profile1). Actual live simp? / only-list tests produced explicit linear-map evaluation, coordinate and finite-single-sum rewrites, eliminating those dischargers. Reconstruction's broad subtype-coordinate `simpa` cost about 228 ms, including a 121 ms failing univ discharger; `simpa only [Submodule.coe_smul]` replaces it. Reconstruction also recomputed the polynomial expansion (~413 ms); its final form consumes the expansion already shared with the main positivity proof. Reduced private scalar assumptions further avoid field/irrelevant-index-instance searches.

Before the final sweep, **all** module builds, independent proofs, binder probes, axiom/type probes and native LSP/tactic requests completed and drained. The only running compiler was:

```
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Separation.lean
```

It exited **0**. Complete raw log: `/private/tmp/roth-d21-final-profile1.log`; parser output `/private/tmp/roth-d21-final-profile1.log.json`; exact root-anchor inventory `/private/tmp/roth-d21-final-profile-anchors.json`.

| Actual declaration | Outer command ms (raw line) | Outer async ms (raw line) | Conservative total ms |
|---|---:|---:|---:|
| `linearIndependent_coordinate_polynomials_aux` | 52.298 (256943) | 229.849 (257085) | **282.147** |
| `degreeOf_mem_coeffNone_span_aux` | 18.768 (297310) | 78.750 (297364) | **97.518** |
| `eq_sum_aeval_basis_coeffNone_aux` | 115.476 (330269) | 515.932 (330508) | **631.408** |
| `Roth.exists_separated_representation` | 36.069 (410600) | 662.645 (420124) | **698.714** |

Every final declaration is below 750 ms and below the 1000 ms budget. No final ≥750 sample needs another sweep. This demonstrates a faster public declaration and bounded separately cached helper costs; no aggregate whole-project performance improvement is claimed. `maxHeartbeats` raises added: 0; profiler scaffolding in source: none; deferred over-budget declarations: none.

## Freeze and coordinator follow-through

**ALL source ownership is revoked.** This worker is report-only from this freeze onward and will make no further source edits. **ALL Lean/MCP/compiler/profile requests are drained**; final native requests completed, final module/probe sessions exited, and the isolated final profiler exited 0.

Frozen source SHA256:

```
d4b98fed52d6f22e3a3c34e2509abf03a5f30ac2342161ab819afe6b8d70c32f
```

Required coordinator sequence before original21 checkpoint: fresh independent audit of **each of the three new private helpers** listed above; rerun every affected module/native-LSP/original/public/actual-axiom/profile/full-project/LeanEval gate after any owner changes; then exact-path commit and successful push. Public instance menu/wrapper/domain-class proposals remain pending and **none** was applied by this worker. No Git or shared progress log was mutated.


## Fresh independent helper audits and final batch reconciliation

The preceding worker freeze and timing table describe the first decomposition, before required fresh helper reviews. The following final batch supersedes its source counts and retained-helper inventory. Fresh dedicated workers independently audited all three additions with the complete 24/42/five-search/effective-binder/width/inequality/11-step workflow:

- [Independence helper](Separation-helper-linearIndependent_coordinate_polynomials_aux.md): retained explicit narrow simplifications; rejected a shorter broad-simp candidate after actual profiling. Final independent audit includes original helper type and a separate coefficient proof.
- [Degree helper](Separation-helper-degreeOf_mem_coeffNone_span_aux.md): removed the new helper by using the imported `MvPolynomial.restrictSupport` submodule directly in the main proof. Final main proof has 30 physical body lines; the typed local inclusion avoids a bespoke duplicate submodule construction.
- [Reconstruction helper](Separation-helper-eq_sum_aeval_basis_coeffNone_aux.md): removed unnecessary `classical`, combined subtype transport using a narrow `simpa only`, and replaced `ring` with `ac_rfl`. Final helper declaration24/proof16 lines.

Final source551→573 lines (+22), with25 retained declarations, including only two added private helpers. The original public statement and all original block documentation remain unchanged. The degree helper's removal does not increase the original declaration inventory. All leaf source ownership was explicitly revoked and all requests drained before owner validation. Final frozen SHA256 `36a381873357317a18cc528ac03d6d55739d5487e00c3daa8fbf568d9dcdbc17`.

User approval arrived during the helper reviews for the exact twelve-theorem instance menu in `Separation-instance-proposal.md`. To preserve frozen validation, no public instance removal is applied in this original21 batch. The nine already-audited affected declarations will receive separate fresh, dependency/source-ordered revisit checkpoints after this publication; the three upcoming originals will apply their approved removals during their ordinary audit. Public-wrapper deletions and coefficient-class weakening remain unapproved and unapplied.


Final owner isolated actual repository sweep `/private/tmp/roth-separation-d21-owner-profile.log` exited0 after all leaf jobs drained; parsed full retained table `.log.json`. Independence helper46.225+266.324=312.549ms; reconstruction helper108.531+609.741=718.272ms; main39.115+856.039=895.154ms. Main remains below1000ms after the two preceding same-source isolated helper3 sweeps844.929/853.337ms; its required≥750 repeat is satisfied. No source or option change, no performance deferral. The original over-budget1237.620ms proof was structurally decomposed and narrowed. The final main proof is30lines; all new retained helper bodies are≤30. Full file performance certification, including upcoming original29's806.987ms sample, remains the final-file buzz pass after remaining declarations.

Owner complete unfiltered native diagnostics `/private/tmp/roth-separation-d21-owner-lsp.json`: success=true, partial=false, timed_out=false, no failed dependencies, zero errors/31 existing warnings. Exact frozen source and all original block docs rechecked; git diff --check passes.

## Owner cumulative publication gates

Source FROZEN SHA256 `36a381873357317a18cc528ac03d6d55739d5487e00c3daa8fbf568d9dcdbc17`; leaf ownership revoked and requests drained before owner gates. Owner probe `88657` exit0,37.80s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL25 actual retained standardaxiom checks. `/private/tmp/roth-separation-d21-compatibility.{lean,log,json}`. Owner build session `56384` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,115.49s/28.60s; source hash stable. `/private/tmp/roth-separation-d21-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.
