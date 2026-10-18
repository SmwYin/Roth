# exists_int_factors — initial audit (before source edits)
Scope: original29, HEAD 31b9e2c; only target and necessary private stages. Approved: omit both Fintype τ and DecidableEq τ. Original docstring and mathematical conclusion preserved.

Proof understanding: normalize the multivariate factor to primitive integer coefficients; absorb the reciprocal scalar into the univariate factor. The mixed coefficient identity and Bézout show every univariate coefficient is integral. Reconstruct the integer polynomial, descend the factorization through injective coefficient casting, and preserve degrees under nonzero rescaling.

1. LINT: baseline module was parent-verified; fresh native diagnostics requested below.
2. HAVE SCAN: hF′ (proof content), anonymous C cancellation (proof content), hint (coefficient integrality proof content), h1 (congrArg once → inline), hVmap (proof content), hV′′ne (one-use term → inline), hUne and hVne (proof content). Extract coherent normalization, coefficient-descent, and degree-preserving assembly stages.
3. SET_OPTION: none.
4. SIMP SQUEEZE: mixed coefficient simp only is nonterminal; coeff_monomial sum simplification nonterminal; terminal simpa and simp retained.
5. NAMING: exists_int_factors describes integer factor existence; snake_case, no forbidden patterns. New stages receive mathematical names and private _aux suffixes.
6. LINE PACKING: preserve public type; measure every signature after decomposition, repair breaks without type changes.
7. BY: already attached.
8. FORMAT: remove fun => in touched code; no local instance declarations, limits or suppression.
9. COMMENTS: zero inline narrative comments in target; preserve original four-line docstring.
10. DOCSTRING: existing source-backed public documentation preserved exactly.
11. VISIBILITY: public contract retained; added stages private.
12. STRUCTURE: original body 46 lines requires genuine decomposition; headline target ≤15, helpers ≤30, branches ≤10. Existential conjunctions share witnesses and cannot be independently split.
13. MATHLIB: searches actually attempted: LeanFinder Gauss separated-variable factors yielded universal-factorization and integral-product lemmas, not a direct match; LeanSearch coefficient-descent yielded toSubring/int; Loogle malformed query failed, corrected query pending; source rg found Polynomial.mem_map_range, unavailable under existing imports (compiled #check). local name search unavailable index. No absence claim. Prefer existing coefficient/Bézout machinery; no new import needed.
14. JUNK DEF: n/a theorem.
15. EXISTS LEMMA: target public with nontrivial construction; not trivial witness lemma.
16. SHOW: none.
17. PUSH_NEG: none.
18. GENERALISE: effective binders τ, Fintype τ, DecidableEq τ, U′, V′, hU, hV, F, hF. τ already universe-polymorphic; both index instances approved for removal. Polynomial variables are dependent data; dropping them invalidates statement. hU/hV establish nonzero factors; dropping either is false (zero input factor, F=0). hF supplies necessary relation; without it choose F=0 and both rational factors 1, incompatible with nonzero integer factors. These negative cases are mathematical analyses, not compiler-verified drop tests; actual probes follow. ℤ/ℚ essential to integer integrality; abstract GCD/fraction field reformulation is a substantial API change outside authorization. No point-local or strict/weak hypothesis applicable. Inversion check: not an accidental concrete witness theorem; casting integers and rational denominators are used throughout.
19. INEQUALITY: no ≥/> or order relation in signature; only ≠ and equalities.
20. NORMAL-FORM: factorization via rename and aeval matches surrounding canonical polynomial API.
21. SYNTAX-GEN: current existential package is what determinant caller consumes; no restatement proposed.
22. IMPORT-FANOUT: no new imports planned.
23. CASTS: ℤ→ℚ genuine cross-type; polynomial X target ascriptions disambiguate aeval.
24. INSTANCE-NAME: n/a no instance declaration.

Literature: local clean.tex §2 lines420–429 explicitly normalizes G to integral primitive U and uses finite integral linear combination of coefficients. Web search Gauss primitive rational integer factors found Stanford lecture notes https://web.stanford.edu/~lindrew/18.702.pdf and Gauss lemma notes https://crypto.stanford.edu/pbc/notes/numberfield/gausslemma.html. Standard generalization is GCD domain/fraction field, requiring a different API; retain approved ℤ/ℚ statement. Private stages exempt from separate literature search.

Initial actions: scoped omit before original docstring, extract rescaling / integral reconstruction / degree-preserving descent, verify exact-original independent proof plus arbitrary-index statement, build, complete native diagnostics, actual axioms and anchored module profiling. Each new helper requires fresh independent leaf audit after freeze, owned by parent dispatch.

## Applied design and step-back review
Three single-statement private stages: scalar cancellation, integer univariate reconstruction by primitivity, and descent of a factorization through injective coefficient casting. The fixed-witness conjunction helper was eliminated after review; main proves each nonzero/degree component directly. This avoids incorrectly treating a plain conjunction as a correlated existential. No pointless component wrappers were added. Main11 lines; helper bodies5/15/4. The four-line descent helper is a ring-map commuting-square proof using injectivity, map_mul, map_rename, aeval naturality, and map_X; not a one-lemma convenience alias. It is generalized to arbitrary rational V′. Each new helper still requires a separate fresh independent audit.

## All 42 golf rules
| Rule | Concrete status |
|---|---|
| 1.1 | n/a no by-exact wrapper |
| 1.2 | n/a no by-rfl wrapper |
| 1.3 | retained degree rewrites close goals directly; no rw/exact pair |
| 1.4 | coefficient congruence simpa retained; direct simpa-only failed and original staged simplification restored |
| 1.5 | reconstruction branch replaced rw; rfl by exact coefficient equality |
| 1.6 | anonymous existential and conjunction constructor used |
| 1.7 | main uses explicit term application to helper |
| 1.8 | n/a no contradiction-negation conversion |
| 1.9 | n/a lambdas carry real coefficient/degree arguments |
| 1.10 | hF′ used twice; hUmap/Vmap multiple uses; h1 congrArg staged proof needed after direct simpa failure |
| 1.11 | n/a no apply/intro pattern except injective descent with rewrite proof |
| 1.12 | n/a no show |
| 1.13 | obtain decomposes primitive and integral polynomial witnesses |
| 1.14 | n/a no consecutive rewrites |
| 1.15 | terminal simpa/simp unsqueezed; nonterminal simp only kept |
| 1.16 | nonterminal coefficient simplifications already only-lists |
| 1.17 | hF′ and coefficient equation symmetry dot notation used |
| 1.18 | function lambdas passed without trailing parentheses where feasible |
| 1.19 | n/a no push_neg |
| 1.20 | nontrivial integer-polynomial existence, not trivial witness wrapper |
| 2.1 | actual native main grind failed; retained constructive witnesses |
| 2.2 | n/a no pre-grind chain retained |
| 2.3 | main simpa [h] handles zero-map contradictions; coefficient direct simpa-only failed so staged simplification retained |
| 2.4 | n/a no function regularity predicates |
| 2.5 | explicit nonzero product terms avoid unsupported positivity search; no ordered target |
| 2.6 | n/a no inequalities/monotonicity |
| 2.7 | n/a no Nat/Int arithmetic goals |
| 2.8 | actual native main aesop failed and left witness construction goal |
| 2.9 | casts necessary for integral coefficients; terminal simpa removes cast hom notation |
| 2.10 | n/a proposition requires unbounded data, not finite computation |
| 2.11 | no fraction-field identity goal after map normalization; existing scalar inverse cancellation is exact |
| 2.12 | normalization retains linear_combination using C g*C g⁻¹=1 |
| 2.13 | n/a no symmetric cases |
| 2.14 | n/a no calc block |
| 2.15 | two nonzero and two degree goals need distinct lemmas; no repeated closing tactic |
| 3.1 | n/a no erw |
| 3.2 | n/a no continuity/measurability tactic |
| 3.3 | n/a no omega or linear arithmetic |
| 3.4 | n/a no redundant rfl-substitution simp |
| 3.5 | no simp/grind attributes: existential rescaling is not a stable simplifier rewrite |
| 3.6 | actual native main simp_all failed to construct polynomial witnesses |
| 3.7 | no limits or profiler scaffolding in source |

## Every effective binder
| Binder | Role and probe/result |
|---|---|
| τ : Type* | arbitrary universe already; compiled arbitrary_index_independent with no Fintype/DecidableEq |
| Fintype τ | scoped omitted as approved; arbitrary-index independent construction compiles |
| DecidableEq τ | scoped omitted as approved; classical local to coefficient reconstruction |
| U′ | multivariate rational data determining nonzero/degree conclusion; cannot erase dependent data binder |
| V′ | rational polynomial data determining factorization and final degree; cannot erase dependent data binder |
| hU | nonzero primitive normalization; actual original-proof drop test log /private/tmp/roth-d29-drop-hU.log |
| hV | nonzero univariate factor; actual original-proof drop test log /private/tmp/roth-d29-drop-hV.log |
| F | integer polynomial being factored; cannot erase dependent data binder |
| hF | essential coefficient comparison; actual original-proof drop test log /private/tmp/roth-d29-drop-hF.log |

Drop-test failures show proof dependency, not a proof that no alternative theorem exists. Mathematical counterexamples to dropping hU/hV/hF were given in initial audit. No eligible point-local, strict→weak, or algebra-class-parent variants occur. ℤ/ℚ are concrete coefficient rings essential to arithmetic integrality, not unused structure. Abstract UFD/GCD-domain generalization is substantial and unapplied.

## Width table — rescale_separated_factor_aux
Widths are Unicode codepoints. Next atom is the next complete binder or expression at a natural syntactic boundary; splitting a binder merely to fill a line was tested and rejected as poor readability. Reference actual `#check @Roth.exists_int_factors` at format.width100 is in independent.log.

| Line | Width | Next syntactic atom | Arithmetic | Status |
|---|---:|---|---|---|
| 451 | 86 | `{U : MvPolynomial τ ℤ}` (22) | 86+1+22=109 | ok |
| 452 | 79 | `(hUmap : map (Int.castRingHom ℚ) U = g • U')` (44) | 79+1+44=124 | ok |
| 453 | 82 | `rename some U' * Polynomial.aeval (X none : MvPolynomial (Option τ) ℚ) V') :` (76) | 82+1+76=159 | ok |
| 454 | 82 | `map (Int.castRingHom ℚ) F = rename some (map (Int.castRingHom ℚ) U) *` (69) | 82+1+69=152 | ok |
| 455 | 73 | `Polynomial.aeval (X none : MvPolynomial (Option τ) ℚ) (Polynomial.C g⁻¹ * V') := by` (83) | 73+1+83=157 | ok |
| 456 | 89 | proof follows | n/a | ok |

Inequality scan: | location | occurrence | action |
|---|---|---|
| whole signature | no ≥/> order relations | n/a |

## Width table — exists_int_polynomial_of_primitive_factor_aux
Widths are Unicode codepoints. Next atom is the next complete binder or expression at a natural syntactic boundary; splitting a binder merely to fill a line was tested and rejected as poor readability. Reference actual `#check @Roth.exists_int_factors` at format.width100 is in independent.log.

| Line | Width | Next syntactic atom | Arithmetic | Status |
|---|---:|---|---|---|
| 464 | 82 | `{V' : Polynomial ℚ}` (19) | 82+1+19=102 | ok |
| 465 | 90 | `(hF : map (Int.castRingHom ℚ) F = rename some (map (Int.castRingHom ℚ) U) *` (75) | 90+1+75=166 | ok |
| 466 | 79 | `Polynomial.aeval (X none : MvPolynomial (Option τ) ℚ) V') :` (59) | 79+1+59=139 | ok |
| 467 | 65 | `∃ V : Polynomial ℤ, V.map (Int.castRingHom ℚ) = V' := by` (56) | 65+1+56=122 | ok |
| 468 | 60 | proof follows | n/a | ok |

Inequality scan: | location | occurrence | action |
|---|---|---|
| whole signature | no ≥/> order relations | n/a |

## Width table — int_factorization_eq_aux
Widths are Unicode codepoints. Next atom is the next complete binder or expression at a natural syntactic boundary; splitting a binder merely to fill a line was tested and rejected as poor readability. Reference actual `#check @Roth.exists_int_factors` at format.width100 is in independent.log.

| Line | Width | Next syntactic atom | Arithmetic | Status |
|---|---:|---|---|---|
| 486 | 100 | `{F : MvPolynomial (Option τ) ℤ}` (31) | 100+1+31=132 | ok |
| 487 | 76 | `(hF : map (Int.castRingHom ℚ) F = rename some (map (Int.castRingHom ℚ) U) *` (75) | 76+1+75=152 | ok |
| 488 | 79 | `Polynomial.aeval (X none : MvPolynomial (Option τ) ℚ) V') :` (59) | 79+1+59=139 | ok |
| 489 | 65 | `F = rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) ℤ) V := by` (81) | 65+1+81=147 | ok |
| 490 | 85 | proof follows | n/a | ok |

Inequality scan: | location | occurrence | action |
|---|---|---|
| whole signature | no ≥/> order relations | n/a |

## Width table — exists_int_factors
Widths are Unicode codepoints. Next atom is the next complete binder or expression at a natural syntactic boundary; splitting a binder merely to fill a line was tested and rejected as poor readability. Reference actual `#check @Roth.exists_int_factors` at format.width100 is in independent.log.

| Line | Width | Next syntactic atom | Arithmetic | Status |
|---|---:|---|---|---|
| 501 | 98 | `{F : MvPolynomial (Option τ) ℤ}` (31) | 98+1+31=130 | ok |
| 502 | 69 | `rename some U' * Polynomial.aeval (X none : MvPolynomial (Option τ) ℚ) V') :` (76) | 69+1+76=146 | ok |
| 503 | 82 | `∃ (U : MvPolynomial τ ℤ) (V : Polynomial ℤ), U ≠ 0 ∧ V ≠ 0 ∧` (60) | 82+1+60=143 | ok |
| 504 | 64 | `F = rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) ℤ) V ∧` (77) | 64+1+77=142 | ok |
| 505 | 83 | `(∀ j, degreeOf j U = degreeOf j U')` (35) | 83+1+35=119 | ok |
| 506 | 76 | proof follows | n/a | ok |

Inequality scan: | location | occurrence | action |
|---|---|---|
| whole signature | no ≥/> order relations | n/a |

## Identifier and preservation checks
The only new external identifier in touched proof code is `smul_ne_zero`, verified by actual module build. Other called mathlib/project identifiers already occur in original target, and all resolved in build and independent proof. No definitions/imports/documentation/header changed. Inline narrative comments0→0. Public signature unchanged except approved removal of both index classes and whitespace packing. Exact original type/order is independently reconstructed in original_type_independent and original_type_api; neither independent theorem calls the target. original_type_api alone calls the target to check backward applicability.

## Five-method search status (completed)
[A] Native LeanFinder: “Gauss lemma polynomial integral rational separated variables factors” yielded universal factorization-ring and integral-coeff-product results; none directly specialize to this separated-variable rescaling statement.
[B] Native Loogle: initial malformed query failed; corrected `Polynomial.map, _ = _` returned map_X, eval_map, eval₂_eq_eval_map.
[C] Native LeanSearch: “polynomial coefficients in subring exists polynomial map integer rational” returned toSubring, ofSubring, int.
[D] Actual source rg in MvPolynomial, Polynomial/Eval and GaussLemma found `Polynomial.mem_map_range`, Gauss primitive divisibility/irreducibility; compiled #check confirmed mem_map_range is unavailable under original imports. Kept explicit finite reconstruction rather than add import for this scoped refactor.
[E] Native local name search Polynomial.map: index unavailable, not absence. Source plus compiled identifiers are fallback.
Auxiliary variants: map range/rangeS, toSubring/ofSubring/int, map injectivity, primitive fraction-map divisibility. Common-equivalents table: no corresponding bucket.
Conclusion: partial library matches support individual stages; retain arithmetic theorem and direct map/degree APIs. No exhaustive absence claim. Actual native `exact?` failed to close target; `apply?` supplied only logical existential rearrangements, not integer factor construction. Raw /private/tmp/roth-d29-final-main-attempts.json.

## Literature search status (completed)
Web queries: “Gauss lemma primitive polynomial rational factors integer coefficients separated variables”; “Gauss lemma GCD domain fraction field primitive polynomial generalization Stacks project”; “Gauss lemma primitive multivariate polynomial separated variables integer coefficients”. Primary sources: Stanford course notes https://web.stanford.edu/~lindrew/18.702.pdf, Stanford Gauss-lemma exposition https://crypto.stanford.edu/pbc/notes/numberfield/gausslemma.html, UChicago algebra notes https://math.uchicago.edu/~linus/6310fa18.pdf. UFD/fraction-field formulation is standard; current arithmetic statement is its specialized, degree-tracked separated-variable form. Local clean.tex explicitly matches Bézout coefficient argument. ChatGPT math MCP unavailable in ALL_TOOLS. Abstract GCD-domain reformulation noted, no API proposal beyond approved index-class omission applied. Private helper literature exemption applies.

## Simplify pass
Built-in simplify tool/skill unavailable; performed its reuse/quality/efficiency review locally. Outcome ISSUES-FOUND-AND-FIXED: removed bundled fixed-witness conjunction stage, replaced with equality descent stage and short direct main proofs. Witness construction retained; map/aeval descent generalized to arbitrary rational polynomial. No shared source outside scope touched.

## Updated automation findings
Raw native nonzero probe /private/tmp/roth-d29-nonzero-attempts.json: positivity failed; aesop closed U nonzero but had a multi-goal warning from replacing a bullet and provides no line saving over the existing direct one-line proof, so retained explicit deterministic term. simp_all altered unrelated hypotheses and did not close the target. Final main exact?/apply?/grind probes preserved in final-main-attempts.json. Original-proof hU/hV/hF drops all actually failed with the corresponding unknown identifier; initial import-cache failures during a build were retried after build completion and are not counted as dependency evidence.

## Gate status — target leaf
| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | `/Users/ramin/.elan/bin/lake build Roth.Separation`, exit0; /private/tmp/roth-d29-build-final.log |
| definition_protected | pass | snapshot diff /private/tmp/roth-d29-source.diff has no def/abbrev/import changes |
| theorem_statement_protected | pass with approved amendment | only Fintype/DecidableEq removal through scoped omit; exact original binder order proof/API harness compiles |
| structure_gate | pass | headline11, helper5/15/4; all branches ≤3; public existential fields correlate shared witnesses; plain conjunction helper removed |
| naming_gate | pass | all three helper names describe mathematical stages, private _aux; no numeric/forbidden schemes |
| line_packing_gate | pass | full per-signature-line Unicode width tables above, max100 |
| inequality_orientation_gate | pass | no ≥/> order relation in any affected signature |
| actual built axioms | pass | target + all three exact private constants + determinant caller standard3 only; independent.log |
| native module LSP | pass with scoped warnings | complete unfiltered, partial=false, timed_out=false, errors0 warnings3 infos0: header preserved and d30 instance redundancy exposed |
| whole project / LeanEval / cumulative original | parent-owned | required sequentially after new helper audits; not claimed complete by leaf |

## Eleven completion steps
1. Reference documentation read: skills, full golfing/proof patterns/search/generalization/gates and relevant naming/style/profiling; installed cleanup Phase4 contract.
2. Initial audit24 items written before any source edit.
3. Five actual search methods A–E recorded, including unavailable index and initial corrected query failure.
4. Every effective binder and applicable generalization candidates recorded, compiled arbitrary-index success and actual hU/hV/hF proof-drop failures.
5. Every affected signature line measured in width tables.
6. Inequality scan tables provided; no reversed relation.
7. All42 golfing rules have concrete statuses; native whole-proof and nonzero attempts retained.
8. Step-back review done; fixed-witness conjunction removed and clear three-stage argument retained.
9. Complete native diagnostics obtained and raw response saved /private/tmp/roth-d29-lsp-final.json.
10. Actual module build, snapshot diff gates, exact-original independent/API proof and arbitrary-index independent proof, actual target/helpers/caller standard axiom checks pass.
11. No renames required/queued; shared logs/Git untouched. Final profile/drain/freeze below.

## Result arithmetic and remaining parent work
Physical proof body target46→11 (−35). Three new helper bodies5+15+4=24 lines. Actual whole file551→562 (+11) due explicit stage signatures. Retained declarations24→27 (three private stages); public names unchanged. Comments-preserved: none inline; original target docstring byte-identical. No public widening except exact two-instance removal authorized in dispatch. No pending API proposal required from this leaf.

New helpers requiring NEW independent leaf audits AFTER this freeze and BEFORE publication:
- Roth.rescale_separated_factor_aux
- Roth.exists_int_polynomial_of_primitive_factor_aux
- Roth.int_factorization_eq_aux
These audits are NOT yet complete; parent dispatches them. This leaf does not claim whole-batch completion.

## Buzz pass — first isolated actual sweep
Actual command `/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Separation.lean` exited0 after all Lean/MCP/build/probe sessions had drained. Raw119749585-byte log /private/tmp/roth-d29-final-profile.log; exact anchoring parser /private/tmp/roth-separation-profile-table.py; all27 rows /private/tmp/roth-d29-final-profile.log.json. Metric=max outer command+outer async proof, no nested double counting.
| Actual declaration | Before ms | After ms |
|---|---:|---:|
| exists_int_factors |734.053|498.457|
| rescale_separated_factor_aux |new|499.121|
| exists_int_polynomial_of_primitive_factor_aux |new|407.378|
| int_factorization_eq_aux |new|398.583|
| exists_det_eq_mul |545.896|511.974|
Baseline /private/tmp/roth-d28-final-profile.log(.json). All affected declarations well below750 repeat threshold and1000 budget. One untouched declaration eq_sum_aeval_basis_coeffNone_aux measured753.447ms, so full repeated isolated actual sweep requested before freeze. No source edits or limit changes. No project-wide performance claim: decomposition distributes proof work across cached stages and reduces headline cost.

## Repeated actual sweep and freeze
Repeat actual module command identical to first, exit0; /private/tmp/roth-d29-repeat-profile.log(.json), table log /private/tmp/roth-d29-repeat-profile-table.log. All Lean/MCP/compiler requests had drained before both profile sweeps; repeat itself has now exited and no requests remain.

| Actual declaration | Repeat command+proof ms |
|---|---:|
| eq_sum_aeval_basis_coeffNone_aux | 819.619 |
| rescale_separated_factor_aux | 513.159 |
| exists_int_polynomial_of_primitive_factor_aux | 443.695 |
| int_factorization_eq_aux | 363.743 |
| exists_int_factors | 486.618 |
| exists_det_eq_mul | 536.891 |

Repeat max: 819.619ms. All27 declarations under1000ms; affected target/helpers/caller all under750ms. Outcome FAST-BOARD; no performance fixes/limits required. Unchanged threshold-crossing earlier helper received the required second actual measurement; no source change warranted.

Freeze source SHA256 `c55b2bf327ea8b42cda84beb9d360a70784c64d4d806a055f3af0e2dc9781bc3`. ALL source ownership explicitly revoked: this worker is now REPORT-ONLY and will make no further source edits. Parent may dispatch all three required fresh helper audits now, followed by sequential project/LeanEval/whole-original checks and publication. This is a target-leaf completion, not a claim that fresh helper audits or whole batch publication have completed.

## Fresh-helper audit resolution — authoritative final batch source

All three additions received distinct fresh independent full declaration audits.
[Rescaling stage](Separation-rescale_separated_factor_aux.md): generalized private packaging
to an arbitrary field and direct polynomials; unchanged public call.
[Integral coefficient stage](Separation-exists_int_polynomial_of_primitive_factor_aux.md):
added the defining Polynomial.Eval.Subring import and used Polynomial.mem_map_range;
proof15→8 lines, exact helper contract retained.
[Equality descent stage](Separation-int_factorization_eq_aux.md): independently audited,
then removed the single-use private wrapper and inlined its4-line proof.

This supersedes the earlier11-line/three-retained-helper leaf snapshot above: the actual
final main proof is15 physical lines, all branches≤10 (inserted branch4), with only TWO
new retained helpers. Source551→548 lines, retained24→26; the public theorem's sole API
change remains the explicitly approved removal of BOTH τ instances. Original public
documentation and coefficient/nonzero/degree contracts remain unchanged. No conjunction
decomposition obligation remains: fixed-factor facts recombine directly in the main proof;
public existential outputs require the same correlated witnesses.

All three leaf owners revoked source access and drained requests. Authoritative batch
source SHA256625a4b282d0e0e7ecb78a2e9f4eb3aec52ac14cc3cafae9eb1d21285d50977fc.
Final complete native LSP:0errors/3inheritedwarnings,
/private/tmp/roth-equality-final-lsp.json. Final fresh-helper leaf module, independent
initial-type proof, actual caller29/30 axioms and removed-suffix absence all pass;
/private/tmp/roth-equality-{build,independent,built-axioms}.log. Its uncontended changed
caller profile is564.732ms/main29 and560.751ms/caller30; owner cumulative fresh sweeps
and full-build/compatibility evidence follow below before publication.

## Authoritative post-helper owner cumulative profiles
Two isolated final-source sweeps /private/tmp/roth-separation-d29-owner-profile{1,2}.log(.json) each exit0; profiles.json records frozen SHA. All26 actual retained command/proof anchors present, raw UTF8 valid. Max741.362/699.251ms; main584.170/574.304, rescale479.379/472.941, coefficient327.013/318.693, downstream518.777/538.195ms. All26 under750/1000 in both sweeps; no outstanding performance follow-up. No other compiler/native requests overlapped.

## Owner cumulative publication gates

Source FROZEN SHA256 `625a4b282d0e0e7ecb78a2e9f4eb3aec52ac14cc3cafae9eb1d21285d50977fc`; leaf ownership revoked and requests drained before owner gates. Owner probe `13106` exit0,51.21s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL26 actual retained standardaxiom checks. `/private/tmp/roth-separation-d29-compatibility.{lean,log,json}`. Owner build session `15497` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,116.89s/44.45s; source hash stable. `/private/tmp/roth-separation-d29-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.
