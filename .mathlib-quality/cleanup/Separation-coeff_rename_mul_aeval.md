# Fresh audit: Roth.coeff_rename_mul_aeval (original 10)

Initial audit recorded before source changes. Baseline HEAD cadba56d802c6d7c1a9fb8969b6399e1b2a44465; source 597 lines, 27 retained declarations. Ownership is this declaration only. Public instance omission remains pending; original contract and documentation stay unchanged.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md, plus relevant style, naming, profiling and Lean skill instructions.

## Initial 24-item audit

1. Lint: three warnings for this target: unused section Fintype/DecidableEq and two unused-in-type warnings. Pending public omission proposal covers these; no warning suppression.
2. Have scan: hA has a substantive by proof (support expansion), used once; retain unless the alternate polynomial equivalence route succeeds. No other have.
3. Set option: none.
4. Simp squeeze: simp_rw is targeted; the inner simp is terminal. No bare nonterminal simp.
5. Naming: coeff_rename_mul_aeval names the actual coefficient, renaming, product, evaluation operations, snake case; no forbidden patterns or abbreviations.
6. Line packing: signature widths and arithmetic will be measured below; retain the public type.
7. By placement: by ends preceding line.
8. Format: two-space tactics, no empty proof lines, no instance local declarations. Existing proof has 18 physical proof lines.
9. Comments: no inline comments; docstring and source attribution must remain exact.
10. Docstring: states coefficient factorisation and disjoint-variable source context.
11. Visibility: public contract retained; actual local use is in exists_int_factors and external scope is controlled by parent.
12. Structure: no conjunction, no long case branch; 18-line body below limit. Investigate optionEquivLeft to remove support expansion.
13. Mathlib: actual Lean Finder, Loogle, LeanSearch and local symbol calls performed; source rg found optionEquivLeft_coeff_coeff and aeval_algHom. No exact equivalent established. Probe exact?/apply? and alternate route.
14. Junk def: n/a theorem.
15. Exists lemma: n/a no existential conclusion.
16. Show/change: term-mode show establishes exponent evaluation; not tactic show. Seek elimination by normal coefficient API.
17. Push_neg: none.
18. Generalise: probe every effective binder below. Fintype/DecidableEq removal proposal remains pending. CommSemiring already supports zero divisors; investigate noncommutative weakening for well-formedness. τ/R universes arbitrary. No concrete object to abstract.
19. Inequality: no inequalities in signature or hypotheses; table below.
20. Normal form: equality of coefficients is canonical; Option τ represents disjoint variable extension. No custom predicate.
21. Syntax generality: explicit U,V,a,b directly apply to the existing coefficient caller; tensor restatement would add construction overhead.
22. Import fanout: no new imports planned.
23. Casts: X none ascription fixes ambient variables and coefficient ring. Inner exponent-vector ascription supports term show; possible removal with new proof.
24. Instance name: n/a theorem.

Issues: simplify proof via polynomial equivalence if it compiles and measures well. Refactoring: only already-pending public instance omission; no new helper authorized or needed yet.

## Search status

[A] Lean Finder: native `lean_leanfinder`, query “coefficient product disjoint variables multivariate polynomial”: returned coeff_X_mul', coeff_mul_X', coeff_monomial_mul', coeff_mul, coeff_monomial_mul. These are partial matches, with convolution or monomial multiplication, not the separated evaluation formula.
[B] Loogle: native `lean_loogle`, query `MvPolynomial.optionEquivLeft`: returned optionEquivLeft and degree/support/X_none lemmas.
[C] LeanSearch: native `lean_leansearch`, query “coefficient product multivariate polynomials disjoint variables”: returned coeff_mul and X multiplication lemmas.
[D] Source rg: untruncated searches for optionEquivLeft, coeff_C_mul, coeff_map, aeval_algHom, aeval_X_left_eq_map across polynomial and multivariate polynomial sources located the exact compositional API used in the final proof. Full-name source lookup located no mathlib coeff_rename_mul_aeval; absence is not inferred from this alone.
[E] Native local symbol query optionEquivLeft returned 26 source-backed items; index warming, so no negative index claim. The useful coefficient bridge is optionEquivLeft_coeff_coeff.

Raw complete native results: `/private/tmp/roth-separation-d10-search0.json` through `search4.json` (4 is initial complete LSP). Auxiliary variants: `_coeff_coeff`, `_coeff_some_coeff_none`, `_C`, `_X_none`, aeval_algHom/apply, aeval_X_left/eq_map. Common-equivalents lookup: no discrete/finite/order bucket applies. Conclusion: partial match; retain a substantive public disjoint-variable coefficient theorem using the polynomial equivalence. This is not an exact equivalent or a one-to-three-call wrapper. No custom predicates introduced. No public deletion or documentation changes applied.

A standalone native `lean_run_code` imported only mathlib and tried `exact?` on the whole separated coefficient goal: complete response, success false, `exact? could not close the goal`, no timeout. Live `lean_multi_attempt` tried grind/simp/aesop/exact?/apply? before edits: no closing result; apply? offered only generic equality rearrangements. Its line replacement also produced an unrelated unexpected-sum parse diagnostic because it replaced the first line of a multiline have; these are trial diagnostics, not module diagnostics. The independent compiler proof below is the reliable success gate.

## Literature status

Web search performed for “polynomial disjoint variables coefficients product polynomial ring tensor product”. Top relevant primary source hit: Mel Hochster, MATH 614 Fall 2013 lecture notes, https://dept.math.lsa.umich.edu/~hochster/615W12/614F13/614.pdf (indexed description: polynomial ring in variables indexed by disjoint union). The PDF open returned inaccessible, so no unverified contents claimed. Other top hits: Cambridge “On the tensor product of polynomials over a ring” (a different root-product operation, rejected as irrelevant); CWI “Polynomial and tensor invariants” (basis/tensor interpretation, no stronger hypothesis conclusion inferred).

Local primary project reference `.mathlib-quality/references/clean.tex:421–424` explicitly says that u_a v_b is a coefficient of F because the two factors have disjoint variables. This matches the present coefficient formula. The generality supported by the formal API is arbitrary commutative semiring and arbitrary variable type; no field, characteristic, nonzero, or domain conditions are needed. The tensor-product formulation is a canonical conceptual generalisation, but would add bundled construction at this use site without improving application. Math ChatGPT MCP: unavailable (no tool in current metadata). No literature-driven public restatement proposed.

## Signature width and inequality gates

`#check @Roth.coeff_rename_mul_aeval` with `set_option format.width 100` is recorded in the independent compile log. The declaration signature remains byte-identical to the original snapshot.

| Signature line | Codepoints | Next complete syntactic unit | Arithmetic | Result |
|---|---:|---|---|---|
| 112 | 95 | `(rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) R) V).coeff` (79) | 95 + 1 + 79 = 175 | break required |
| 113 | 83 | `(a.mapDomain some + Finsupp.single none b)` (42) | 83 + 1 + 42 = 126 | break required |
| 114 | 80 | no next signature unit | n/a | packed, by on same line |

| Occurrence | Location | Inequality | Action |
|---|---|---|---|
| none | full effective signature and all hypotheses | no ≥, >, ≤ or < | n/a; no orientation or rename needed |

## Golf rules: all 42

| Rule | Concrete status |
|---|---|
| 1.1 | No by-exact wrapper in source output; inline term show carries needed hom-application type. |
| 1.2 | No by-rfl. |
| 1.3 | No rw followed by exact; final rw closes. |
| 1.4 | No simp/exact chain. |
| 1.5 | No trailing rfl after simp. |
| 1.6 | No constructor goal. |
| 1.7 | No apply/exact chain. |
| 1.8 | No by_contra. |
| 1.9 | No eta lambda. |
| 1.10 | Candidate single-use hU without by was actually inlined into typed show; final h has substantive ext/simp proof. |
| 1.11 | No apply/intro chain. |
| 1.12 | Removed old term show for exponent evaluation by different proof; final term show is needed to fold AlgHom.comp_apply for rewriting (untyped congr_fun rewrite failed in candidate log). |
| 1.13 | No projection have. |
| 1.14 | Final coefficient operations merged into one rw. |
| 1.15 | Only simp is terminal in hom extensionality. |
| 1.16 | No nonterminal bare simp; targeted rw handles main goal. |
| 1.17 | .toAlgHom.comp uses dot notation; no eligible remaining projection rewrite. |
| 1.18 | No trailing proof/lambda parentheses eligible for <|; term show is rw-list element. |
| 1.19 | No push_neg. |
| 1.20 | No existential helper. |
| 2.1 | Actual native grind trial failed on whole coefficient goal. |
| 2.2 | No grind output or preceding grind steps. |
| 2.3 | Direct coefficient rw consolidates old support/case proof; no simp-followed-closing chain remains. |
| 2.4 | No function regularity goal. |
| 2.5 | No positivity or nonzero goal. |
| 2.6 | No inequalities/monotonicity. |
| 2.7 | No Nat/Int arithmetic proposition; exponents merely index coefficients. |
| 2.8 | Actual native aesop trial failed, made no progress. |
| 2.9 | No concrete numeric computation or cross-type cast. |
| 2.10 | Arbitrary semiring coefficient equality has no computable DecidableEq; decide is inapplicable. |
| 2.11 | No denominators or field structure. |
| 2.12 | Old ring normalised a commutative expression with no equation hypotheses to combine; replaced entire block by coefficient API. Final proof has no ring/ring_nf. |
| 2.13 | No symmetric case branches; old support split removed. |
| 2.14 | No calc. |
| 2.15 | Hom ext creates a uniform variable goal closed by terminal simp; no replicated goals requiring <;>. |
| 3.1 | No erw. |
| 3.2 | No continuity/measurability. |
| 3.3 | No omega/lia present or applicable. |
| 3.4 | No rcases. |
| 3.5 | Considered simp/grind registration: unchanged public API, specialised existing coefficient caller explicitly rewrites with this theorem; no attribute needed. |
| 3.6 | No simp_all only. |
| 3.7 | No local limits or profiler scaffolding. |

## Step-back and simplify review

The whole-goal automation and mathlib exact search did not close. A different strategy did: use the coefficient-polynomial view, prove the renaming is the constant-polynomial algebra hom, transport evaluation, then apply two constant multiplication coefficient formulas. This removes the support sum, exponent normalisation, case split, ring tactic and local classical command. The remaining have is a reusable hom equality inside this proof, not an unnecessary single-use term. A single term would need the same explicit folding type and would obscure the coefficient rewrite chain. No new source helper, imports, definition, public attribute, or caller edits.

Final casts audit: zero cross-type coercions introduced; original X-none ambient type ascription retained; the new term show provides a load-bearing equality type because rewriting the raw `AlgHom.congr_fun h U` failed to match the unfolded hom application. No redundant explicit type cast in the diff.

## Verification evidence already complete

- Baseline: parent supplied clean pushed HEAD and sequential cumulative project/LeanEval gates. Optional cache and runLinter are not rerun for this single-declaration worker. Fresh actual baseline sweep completed exit 0; target 40.222 ms outer command + 450.409 ms outer async proof = 490.631 ms. This repeats the inherited borderline 842.772 ms timing, as required; raw `/private/tmp/roth-separation-d10-baseline-profile.log` (full trace) and its `.json` table.
- Actual `/Users/ramin/.elan/bin/lake build Roth.Separation` exited 0, built target in 21 seconds; `/private/tmp/roth-separation-d10-build.log` contains complete output.
- Complete unfiltered native module diagnostics: `/private/tmp/roth-separation-d10-final-lsp.json`, success true, partial false, timed_out false, failed_dependencies empty, 0 errors / 31 warnings. Baseline was 0 errors / 32 warnings. The target's unused-section warning disappears because the new proof calls coeff_coeffNone, whose retained public signature includes the original instances; two unused-in-type warnings remain. No suppression or instance omission was applied.
- `/private/tmp/roth-separation-d10-independent.lean` compiled exit 0; corresponding `.log` prints the width-100 signature, compiles an exact ORIGINAL-type assignment to the actual theorem, and independently proves the target without referring to itself. It uses the earlier public coeff_coeffNone bridge plus mathlib; no renamed self-proof or source-copy namespace trick.
- Actual built axioms printed for Roth.coeff_rename_mul_aeval, Roth.coeff_coeffNone, Roth.exists_int_factors, and independent D10.independent: exactly propext, Classical.choice, Quot.sound for each. No actual private constant changed or added, so no affected private axiom target. The source independent-proof file and log are isolated under /private/tmp.
- Source search evidence `/private/tmp/roth-separation-d10-source-search.log` is untruncated. Trial candidate logs retain the failed raw-hom rewrite and invalid guessed coeff_mul_C route; final candidate-inline compiled exit 0.
- `git diff --check` exited 0. The only source hunk is this theorem's proof: 7 inserted / 18 removed lines. File 597 → 586 lines, 27 → 27 retained declarations. Three signature lines and docstring match the original exactly; bytes outside this proof match the starting source exactly. Public effective original instances remain present, and their possible omission is still pending in Separation-instance-proposal.md.

## Actual-module performance

Final command `/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Separation.lean` exited 0. Full raw log: `/private/tmp/roth-separation-d10-final-profile.log`; parser table: same path plus `.json`. Actual named repository anchors are outer Elab.command 52.568 ms and outer Elab.async `elaborating proof of Roth.coeff_rename_mul_aeval` 215.845 ms, summed conservatively to 268.413 ms. Nested trace nodes are not double-counted. This is comfortably below 750 ms and the 1000 ms budget; another final sweep is not required. Fresh unchanged baseline was 490.631 ms; measured saving in this sweep is 222.218 ms, without a whole-project improvement claim. The trace diagnosis is removal of support-sum expansion, general ring normalisation and repeated Finsupp exponent rewrites in favor of hom transport and coefficient rewrites.

Unchanged future declaration exists_separated_representation measured 1342.091 ms in the complete sweep. Parent was notified and explicitly confirmed it is tracked for its own fresh dedicated audit (original 21), already over budget in earlier baselines, outside this worker's source ownership. It stays untouched; this report does not represent all module declarations as under budget.

## Binder/generalisation probes

Actual compiler probes live at `/private/tmp/roth-separation-d10-probe-CASE.lean`, complete diagnostics at the matching `.log`, suite exit statuses at `/private/tmp/roth-separation-d10-probes-summary.log`. For positive generalisations the isolated probe uses a locally proved coeffBridge with no finite/decidable assumptions, so it can test the mathematics independently of the earlier public bridge's pending class omissions. This is a probe-only theorem outside the repository, not a new source helper. Direct class omission of the final proof is tested separately and reported below.

| Effective binder | Role and candidates | Compiler evidence / outcome |
|---|---|---|
| τ : Type* | arbitrary index type, already universe polymorphic; drop | drop-tau tests unknown τ with autoImplicit false; type cannot be dropped. No stronger universe restriction. |
| Fintype τ | no mathematical finiteness needed; drop; Finite intermediate unnecessary if no finiteness works | drop-fintype exit 0, independent bridge. Pending public proposal only; retained in actual source. |
| DecidableEq τ | no mathematical decidability needed; drop | drop-decidable exit 0, independent bridge. drop-both exit 0. Pending public proposal only; retained in actual source. |
| R : Type* | arbitrary coefficient type, already universe polymorphic; drop | drop-R exit 1, unknown R with autoImplicit false. |
| CommSemiring R | supports rename, MvPolynomial multiplication, algebra evaluation; drop, Semiring, NonUnitalCommSemiring | all are tested in the actual suite; diagnostic details appended after completion. No subtraction, field, domain or nonzero assumptions present to weaken. |
| U : MvPolynomial τ R | arbitrary structure value on both sides, type follows variables/coefficients; drop | drop-U exit 1, unknown U; no proposition, pointwise weakening or strict→weak hypothesis. |
| V : Polynomial R | arbitrary structure value on both sides; drop | drop-V exit 1, unknown V; no degree/nonzero assumption. |
| a : τ →₀ ℕ | arbitrary monomial exponent, built into MvPolynomial coefficient API; drop | drop-a exit 1, unknown a; generalising exponents would change the underlying polynomial object. |
| b : ℕ | arbitrary polynomial coefficient exponent, built into Polynomial API; drop | drop-b exit 1, unknown b; same object-level obstruction to a different index type. |

No bundled propositions, global regularity assumptions, or strict inequalities exist. Inversion check: purely parametric polynomials and exponents throughout; no distinguished concrete mathematical object to abstract. Point-localisation is n/a, since the conclusion is already a coefficient at the explicitly given a,b. No additional public type/structure change proposed beyond the existing pending instance proposal.

Direct deletion of both source instances was actually compiled separately in `/private/tmp/roth-separation-d10-direct-drop-both.lean`: exit 1, missing Fintype τ and DecidableEq τ at the call to the still-original public coeff_coeffNone. Thus the positive semantic generalisation is compiler-verified using the isolated bridge, while a literal omission of only this final declaration does not yet compile. If the pending public menu is approved for both the earlier coefficient bridge and this target, the new proof supports the same generality; approving this target alone would require a different bridge proof. No type-level omission is silently applied.

## Diff gates and completion checklist

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | actual lake build Roth.Separation exit 0, full build log |
| definition_protected | pass | no definition/abbreviation changed |
| theorem_statement_protected | pass | original three-line signature byte-identical; exact ORIGINAL type assignment compiles |
| naming_gate | pass | descriptive coefficient/rename/mul/aeval name; no forbidden pattern, no rename |
| structure_gate | pass | 7 physical body lines; no conjunction or case branches |
| line_packing_gate | pass | all three width rows above, required breaks exceed 100 |
| inequality_orientation_gate | pass | zero inequality occurrences in effective signature |
| source_scaffolding | pass | no options, sorry, axioms, native_decide, haveI/letI or profiler material introduced |
| actual built axioms | pass | actual target, dependent caller and independent proof standard three only |
| native module LSP | pass | complete unfiltered 0 errors/31 warnings |
| scoped performance | pass | actual target 268.413 ms, baseline repeat 490.631 ms |
| cumulative whole project + separate LeanEval | parent-owned final gate | parent runs sequentially after this freeze, along with whole-original compatibility and Git commit/push |

All eleven substantive completion steps:

- [x] Step 1: read required references and relevant style/naming/performance references.
- [x] Step 2: initial 24-item audit recorded before editing.
- [x] Step 2.5: five actual search methods, variants, compiled exact-search probe, replacement assessment.
- [x] Step 2.6: every effective binder considered, actual drop/weakening probes and literature search.
- [x] Step 2.7: every signature-line width and next-unit arithmetic.
- [x] Step 2.8: complete inequality scan, empty-table row.
- [x] Step 3: concrete status for all 42 golf rules.
- [x] Step 4: different proof strategy tested and adopted; holistic simplify review recorded.
- [x] Step 5a: complete native module diagnostics and actual build.
- [x] Step 5b: diff gates, original type, independent proof, built axioms and actual profiling.
- [x] Step 6a: no renames needed; no sidecar write.

Result: 21 → 10 declaration lines (3 signature + 18 → 7 body), saving 11 lines. Rules 1.10, 1.12 and 1.14 applied along with whole-strategy API simplification. One proof restructuring issue fixed; two pending public instance omissions remain under the existing proposal. No new source helper, no private declaration changed, no deletion or call-site substitution. Comments: none in original body; all docstring and inline narratives outside the body preserved exactly. Source-only diff 7 additions/18 deletions. Report-only finalisation follows the completed probe drain.

Final probe drain: all 12 suite cases completed; runner exited 0 after recording each compiler's independent exit code. Three positive cases drop-fintype, drop-decidable, drop-both exited 0. All dependent-value/type drops, CommSemiring drop, Semiring weakening and NonUnitalCommSemiring weakening exited 1 with expected diagnostics. Semiring fails to synthesise CommSemiring R for rename/evaluation; nonunital and omitted ring structure fail to synthesise CommSemiring R and Semiring R. These are actual compiler-verified failures, not predictions. The direct final-proof drop-both compiler also completed exit 1 as described above.

Freeze: SHA256 of Roth/Separation.lean is `721b7cde6fe0430a6e37e3fd92be12f272ad38ed8409de2acfdb81567ca7dacb`. ALL source ownership is revoked. All native Lean/MCP requests, compiler sessions, probe runner and both actual profiling sweeps are complete and drained. This worker is report-only and will make no further source edits. Parent owns cumulative compatibility, sequential full project and separate LeanEval builds, exact-path commit and push.

## Owner cumulative publication gates

Source FROZEN SHA256 `721b7cde6fe0430a6e37e3fd92be12f272ad38ed8409de2acfdb81567ca7dacb`; leaf ownership revoked and requests drained before owner gates. Owner probe `87314` exit0,40.79s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL27 actual retained standardaxiom checks. `/private/tmp/roth-separation-d10-compatibility.{lean,log,json}`. Owner build session `51365` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,123.85s/29.72s; source hash stable. `/private/tmp/roth-separation-d10-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.
