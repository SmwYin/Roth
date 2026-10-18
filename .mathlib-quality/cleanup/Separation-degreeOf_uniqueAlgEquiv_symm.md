# Roth.degreeOf_uniqueAlgEquiv_symm — original declaration 18

Initial audit, written before source edits (line arithmetic corrected at completion): source lines 161–174, 12-line proof. The theorem identifies the only-variable degree with ordinary natural degree. The upper bound transports nonzero coefficients; the lower bound uses the leading coefficient. Public type and docstring are protected. No header, import, declaration deletion, instance removal, or public API change is authorized here. Baseline actual target cost is 15.506 + 56.513 = 72.019 ms from `/private/tmp/roth-separation-d16-final-profile-fixed.log`; baseline full LSP is 0 errors / 31 warnings per dispatch.

Initial punch list: test replacing the zero/nonzero lower-bound split by the coefficient-vanishing criterion; inspect the single `have h`; no options or proof comments occur; terminal `simp [hf]` and `simpa using h` are already unsqueezed. The 2-line signature fits the 100-column limit. No inequality occurs in the public statement. Public name follows mathlib's `degreeOf_..._symm` operation naming. Public visibility and existing documentation must remain unchanged. Full search and binder probes will be recorded below.

## Full 24-item audit

| Item | Concrete result |
| --- | --- |
| 1 LINT | Final native complete unfiltered LSP: 0 errors, 31 existing warnings, no target warning; partial=false, timed_out=false. |
| 2 HAVE SCAN | Original `have h := monomial_le_degreeOf ...` used once by `simpa`; removed with entire leading-coefficient branch. No have remains. |
| 3 SET_OPTION | No target options, limits, or profiler scaffolding. |
| 4 SIMP SQUEEZE | Original terminal simp/simpa removed. Final explicit terminal simpa only protects the equivalence abstraction: unrestricted simp unfolds `uniqueAlgEquiv_symm_apply` before coefficient transport and fails; tested concretely. Inner simpa only identifies the singleton exponent without unfolding the polynomial. |
| 5 NAMING | Degree-of / inverse-unique-equivalence name mirrors mathlib operation names; no forbidden abbreviation, numeric scheme or single-letter name. No rename needed. |
| 6 LINE PACKING | Complete signature width table below. |
| 7 BY PLACEMENT | by ends conclusion line. |
| 8 FORMAT | Two-space indentation, no internal blank lines, ordinary lambda uses ↦, no haveI/letI. |
| 9 COMMENTS | No inline comments existed; zero removed. |
| 10 DOCSTRING | Existing one-line interpretation preserved byte-for-byte. |
| 11 VISIBILITY | Public theorem retained under original contract. |
| 12 STRUCTURE | Original proof 12 lines; final 10, two short inequality branches; no conjunction or >10-line branch, no extraction needed. |
| 13 MATHLIB | Five actual searches below; coefficient vanishing API replaces bespoke nonzero leading-coefficient argument. |
| 14 JUNK DEF | n/a: theorem, no data definition. |
| 15 EXISTS LEMMA | n/a: equality theorem, no private existential witness. |
| 16 SHOW/CHANGE | n/a: no show. |
| 17 PUSH_NEG | n/a: no push_neg. |
| 18 GENERALISE | Every effective binder and parent weakening tested below; no public changes applied. |
| 19 INEQUALITY | Public type has zero comparisons; proof's derived bounds are ≤ and < only. |
| 20 NORMAL-FORM | Equality of variable degree and ordinary natural degree is canonical; coefficient characterization is mathlib's normal interface. |
| 21 SYNTAX-GEN | Explicit polynomial convenient for rewriting. General all-variable coefficient degree formulation already exists as degreeOf_eq_natDegree; no new restatement needed. |
| 22 IMPORT-FANOUT | n/a: no imports changed. |
| 23 CASTS | No casts. Original `(default : σ)` removed; final p annotation fixes polynomial context and i follows by inference. No redundant ascriptions in diff. |
| 24 INSTANCE-NAME | n/a: no instance declaration. |

## Five actual search methods

All native outputs saved unfiltered as `/private/tmp/roth-separation-d18-search0.json` through `search4.json` (search4 is live goal inspection).

| Method | Query and actual result |
| --- | --- |
| Local index | `degreeOf_unique`, positive project theorem plus unrelated hits; index warming, so no absence inference. |
| Loogle | `MvPolynomial.degreeOf, MvPolynomial.uniqueAlgEquiv`, completed empty list; only this exact query was empty. |
| LeanSearch | `degree of univariate polynomial as multivariate polynomial one variable uniqueAlgEquiv`, returned degreeOf_eq_natDegree, degree_finSuccEquiv and equivalence definitions. |
| Lean Finder | `degreeOf of uniqueAlgEquiv inverse equals polynomial natDegree`, returned natDegree_finSuccEquiv and degree_finSuccEquiv, plus composition equivalences. |
| Direct source | Actual rg of Equiv.lean/Degrees.lean and Polynomial/Degree files; checked uniqueAlgEquiv coefficient formulas at Equiv.lean:115, natDegree_optionEquivLeft:578, degreeOf_eq_natDegree:827, degreeOf_le_iff:235, notMem_support_of_degreeOf_lt:288, Polynomial.natDegree_le_iff_coeff_eq_zero in Degree/Lemmas.lean:78. |

Search strict rules: directly reuse mathlib primitives; no new wrapper or private helper. Five methods actually run, and positive source signatures verified by compiled candidate. Standard files, inverse direction, support and coefficient alternatives inspected. No custom condition duplicates a typeclass; no common-equivalents issue. General equivalences need extra transport and do not directly close this precise unique-equivalence goal. No claim of global mathlib absence. No module documentation change authorized or required.

## Literature and every-binder generalisation

Actual web searches: `site.encyclopediaofmath.org polynomial ring degree variable polynomial ring one indeterminate` and `site.stacks.math.columbia.edu polynomial ring variables degree coefficients`. Opened primary author-hosted [Y. Vorobets, MATH 433 Lecture 33](https://people.tamu.edu/~yvorobets/MATH433-2023A/Lect3-08web.pdf), pages 2 and 4: formal polynomials are finite coefficient sequences, and degree is the largest exponent with nonzero coefficient. This supports the coefficient-transport proof interpretation. The source treats rings, a stronger setting than this commutative-semiring theorem; no weaker algebra assumption inferred. Encyclopedia opening returned 502 and is not evidence. No ChatGPT mathematics connector was exposed. The public theorem already has universe-polymorphic coefficient and variable types.

Actual compiler-negative probes, with autoImplicit=false: `/private/tmp/roth-separation-d18-binder-probes.lean`, native output `/private/tmp/roth-separation-d18-binder-probes.json`. Native completed, timed_out=false; expected errors at each candidate signature, with an out-of-date-import informational diagnostic during the concurrent build. These are actual elaboration failures, never applied to repository source.

| Effective binder | Candidate | Actual result and decision |
| --- | --- | --- |
| `{R : Type*}` | Drop R | Unknown identifier R at instance/polynomial/equivalence. Retain universe-polymorphic type. |
| `[CommSemiring R]` | Drop; weaken to Semiring | Drop fails Semiring and CommSemiring; Semiring fails CommSemiring at uniqueAlgEquiv. Retain. |
| `{σ : Type*}` | Drop σ | Unknown identifier σ at Unique and equivalence. Retain. |
| `[Unique σ]` | Drop; Inhabited; Inhabited + Subsingleton | All fail Unique synthesis at exact existing equivalence expression. Unbundling requires building an equivalent Unique witness, not mathematically weaker content. Retain. |
| `(f : Polynomial R)` | Drop f | Unknown f and f.natDegree. Retain essential data. |

Section τ/Fintype τ/DecidableEq τ are absent from this theorem's effective type; #check confirms. No pointwise/global, strict/weak, nonzero/domain/field hypothesis exists to weaken. Inversion check: after coefficient identification both sides use general support-degree criteria already in mathlib; extracting another abstract helper would duplicate that API. No public proposal added. All three existing public options remain pending and unapplied.

## Width and inequality gates

Actual source codepoint widths:

| Signature line | Width | Next expression unit | Packing arithmetic / decision |
| --- | --- | --- | --- |
| 161 | 80 | `degreeOf default ((uniqueAlgEquiv R σ).symm f)` (46) | 80 + 1 + 46 = 127 > 100; keep break. |
| 162 | 70 | Proof body follows | n/a: last signature line. |

`format.width 100` #check is in the isolated final probe log. No signature edits.

| Occurrence | Original/final orientation | Action |
| --- | --- | --- |
| Public type and effective hypotheses | No inequality operators | None. |
| First branch goal from le_antisymm | degreeOf ≤ natDegree | Already smaller-side-left. |
| Lower branch goal | natDegree ≤ degreeOf | Already smaller-side-left. |
| hn generated by natDegree criterion | degreeOf < n | Already smaller-side-left. |
| Explicit source comparisons / theorem name | None; no _ge_/_gt_ | No rename or rewrite. |

## All 42 golf rules

| Rule | Concrete status |
| --- | --- |
| 1.1 by exact | n/a: no wrapper. |
| 1.2 by rfl | n/a: requires coefficient transport. |
| 1.3 rwa | Upper branch rw changes a hypothesis, then degree bound uses it; no matching terminal rw/exact compression. |
| 1.4 simpa using | Applied to direct mathlib support nonmembership. |
| 1.5 trailing rfl | n/a: none. |
| 1.6 constructor | n/a: no conjunction. |
| 1.7 exact application | Direct notMem_support theorem used under simpa. |
| 1.8 by_contra! | n/a: no contradiction. |
| 1.9 eta reduce | n/a: lambda binds n and hn used separately. |
| 1.10 inline have | Original single-use h removed with lower-branch strategy. |
| 1.11 refine fun | Applied coefficient criterion with `refine ... fun n hn ↦ ?_`. |
| 1.12 show | n/a: none. |
| 1.13 obtain | n/a: no projections. |
| 1.14 merge rw | No consecutive same-location rw; hypothesis transport already two lemmas in one rw. |
| 1.15 terminal simp | Unrestricted simplification tested and failed by unfolding unique equivalence too early; explicit only protects abstraction, not cosmetic squeeze. |
| 1.16 nonterminal simp | n/a: all simplifications close their subgoals. |
| 1.17 dot notation | Existing `.2` coefficient criterion and direct API are suitable; no longer namespace application to shorten. |
| 1.18 <| | Parenthesized using expression spans lines and fixes theorem application; no useful trailing-parenthesis simplification. |
| 1.19 push Not | n/a: none. |
| 1.20 existential inline | n/a: no existential helper. |
| 2.1 grind | Actual live attempt `grind [MvPolynomial.coeff_uniqueAlgEquiv_symm]` failed. |
| 2.2 before grind | n/a: retained proof has no grind. |
| 2.3 simpa consolidate | Applied direct coefficient transport; no trailing exact remains. |
| 2.4 fun_prop | n/a: algebraic degree, no analytic property. |
| 2.5 positivity | n/a: no positivity goal. |
| 2.6 gcongr | n/a: bounds depend on coefficient support, not monotonic expression congruence. |
| 2.7 lia/omega | n/a: symbolic degrees require support API, no arithmetic relation supplies missing degree identification. |
| 2.8 aesop | Actual live attempt failed to prove equality. |
| 2.9 norm_num/cast | n/a: no concrete computation or cast. |
| 2.10 decide | n/a: arbitrary coefficient semiring and arbitrary polynomial, no closed finite computation. |
| 2.11 field_simp/ring | n/a: no denominators or ring expression equality. |
| 2.12 linear_combination | n/a: no ring/ring_nf goal or algebraic hypothesis. |
| 2.13 wlog | n/a: no symmetric branches; original zero split eliminated. |
| 2.14 calc | n/a: no calc. |
| 2.15 <;> | Bounds use distinct arguments; sharing automation unhelpful. |
| 3.1 erw | n/a: no erw. |
| 3.2 continuity | n/a: none. |
| 3.3 omega→lia | n/a: none. |
| 3.4 rcases rfl | n/a: none. |
| 3.5 automation attrs | No global attribute needed for compatibility theorem; no API change. |
| 3.6 simp_all | n/a: no simp_all. |
| 3.7 limits | n/a: none. |

## Step-back, simplify, and evidence

Live goal at line 163 confirmed only R, CommSemiring R, σ, Unique σ, f. Actual whole-proof simp, grind, aesop, exact? all failed (`/private/tmp/roth-separation-d18-attempts.json`). The successful alternate proof removes the exceptional zero case by using coefficient vanishing above a bound. Direct inverse coefficient rewriting initially failed because `single default n default` is not definitionally n. Unrestricted terminal simpa unfolded the equivalence early; the explicit p argument and only-list compiled. A still-shorter candidate using the retained Roth coefficient wrapper compiled, then was superseded by direct mathlib reuse after owner review. Its earlier profile is explicitly not final evidence. Final simplification avoids that new wrapper dependency and adds no helper.

Diff gates: public signature/docstring byte-identical; definitions/imports/pins untouched; no new axiom, sorry, native_decide, options, warning suppression, local instance tactic or helper. Final actual diff is 5 additions / 7 deletions: file 553 → 551 lines, proof 12 → 10 lines; 23 retained declarations unchanged. Public instance-removal and two public-deletion proposals remain pending and unapplied. Full-project/LeanEval/Git/push belong to parent after freeze.

## Final gates, eleven completion steps, and freeze

1. Doctor: inherited clean pushed HEAD febb5ad and valid actual baseline; fresh baseline native LSP saved at `/private/tmp/roth-separation-d18-baseline-lsp.json`, complete 0 errors/31 warnings.
2. Prepare: read skills, full golf/proof-pattern references, cleanup Phase 4 and relevant search/generalisation/style/naming/gates/profiling material; located original declaration and effective context.
3. Initial audit: written above before source edits; all 24 items and concrete punch list completed.
4. File-level fixes: none within scope; header warning and public instance options deliberately preserved by explicit contract.
5. Per-declaration golf: all 42 rules above, actual live attempts and independently compiled candidate; proof-only replacement applied.
6. Refactor: zero new helpers, zero renames, zero public changes; pending options remain unapplied. Direct mathlib variant superseded wrapper-dependent candidate.
7. Module gate: `/Users/ramin/.elan/bin/lake build Roth.Separation` exited 0, `/private/tmp/roth-separation-d18-build-final.log`, successfully built 1876 jobs. `git diff --check` passed.
8. LSP gate: complete unfiltered native `/private/tmp/roth-separation-d18-direct-final-lsp.json`, partial=false, timed_out=false, success=true, 0 errors/31 warnings/0 infos. Baseline warnings unchanged.
9. Independent/contract/axioms: `/private/tmp/roth-separation-d18-direct-independent.lean` checks the explicit ORIGINAL effective type and proves it independently without calling the target theorem. Actual built target and independent theorem both report exactly propext, Classical.choice, Quot.sound. Shell retry exited 0 with full log `/private/tmp/roth-separation-d18-direct-independent-retry.log`. First attempt raced the module rebuild and reported missing olean; retried after successful build, not counted as pass. No affected private helper exists.
10. Simplify/buzz: step-back alternative removes zero split. Actual final repository-module profiler exited 0: `/private/tmp/roth-separation-d18-direct-final-profile.log`, parsed `.json` sidecar. Target command 12.344 ms + outer async proof 23.659 ms = 36.003 ms, one actual anchor of each kind, no nested double counting. Baseline 72.019 ms; below 750 ms repeat threshold and 1000 ms budget. This is only target timing, no project-wide speedup claim. Earlier non-direct profile superseded.
11. Report/freeze: corrected measured line arithmetic from git HEAD and current source; 553→551 file lines, 14→12 declaration lines, 12→10 proof lines. ALL source ownership revoked; report-only from this point. ALL Lean/MCP/compiler/profile requests drained; final build, shell independent probe, and both profile processes completed. Parent owns sequential whole-project/LeanEval, complete-original/all-retained compatibility and axiom checks, exact-path commit and push.

Frozen source SHA256: `1c58b8b35fe3c01d326d802b94c54dbc8ed0349e1ca388f87e9b34aa2a0278d4`.

## Owner cumulative publication gates

Source FROZEN SHA256 `1c58b8b35fe3c01d326d802b94c54dbc8ed0349e1ca388f87e9b34aa2a0278d4`; leaf ownership revoked and requests drained before owner gates. Owner probe `59024` exit0,45.72s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL23 actual retained standardaxiom checks. `/private/tmp/roth-separation-d18-compatibility.{lean,log,json}`. Owner build session `2299` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,128.62s/29.26s; source hash stable. `/private/tmp/roth-separation-d18-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.
