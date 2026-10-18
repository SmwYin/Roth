# Fresh audit: Roth.degreeOf_rename_mul_aeval (original 19)

Initial audit written before any source edits. Dedicated worker d19; baseline HEAD 82146b3; actual module 551 lines / 23 retained declarations. Scope: lines 180–193 (doc plus declaration), theorem 183–193, 11 lines, proof 9 lines including `:= by`. No source edits yet.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md, plus both skills, Phase 4, style/naming/profiling references. User-preserved metadata and ORIGINAL public type/docs control over generic skill rewrite suggestions.

## Initial 24-item audit

1. LINT: complete native unfiltered LSP succeeded: 0 errors, 31 warnings. Target has unused Fintype section variable at 183, unused DecidableEq/Fintype in type at 180. Preserve pending public instances. Full raw `/private/tmp/roth-separation-d19-tool0.json`.
2. HAVE SCAN: zero `have` statements; no inline opportunity.
3. SET_OPTION: none.
4. SIMP SQUEEZE: L187 `simp [hU]` and L192–193 final `simp [...]` are terminal; preserve unsqueezed.
5. NAMING: descriptive composition of mathlib identifiers `degreeOf`, `rename`, `mul`, `aeval`; no forbidden abbreviations or numeric schemes; mathematical subject clear. No rename required.
6. LINE PACKING: required width table below; all lines satisfy width and no next token fits.
7. BY PLACEMENT: `by` ends line 185.
8. FORMAT: two-space tactic indentation, no blank body lines, one tactic per line, no haveI/letI.
9. COMMENTS: no inline comments in this proof; existing source narrative in docstring must remain intact.
10. DOCSTRING: public descriptive statement and source citation present; preserve exact ORIGINAL doc.
11. VISIBILITY: public contract, used by exists_det_eq_mul; public deletion/visibility changes unauthorized.
12. STRUCTURE: 9 proof lines including `:= by`; first branch one line, remaining branch six lines; no conjunction. No extraction needed.
13. MATHLIB: five actual search methods performed; building blocks degreeOf_mul_eq and degreeOf_rename_of_injective already direct. Detailed evidence below.
14. JUNK DEF: n/a, theorem.
15. EXISTS LEMMA: n/a, public equality, no existential.
16. SHOW vs CHANGE: no show/change.
17. PUSH_NEG: absent.
18. GENERALISE: test every effective binder in isolated probes; public type frozen. Existing 12-theorem instance proposal remains pending, and any additional compiled weakening will be flagged.
19. INEQUALITY: no ordered comparisons in code; table below.
20. NORMAL-FORM: coordinate degree equality is standard mathlib degreeOf normal form; natural degree zero for zero U handled explicitly.
21. SYNTAX-GEN: U explicit, V inferred via hV, j explicit support the call at line 546 directly; no restatement proposed.
22. IMPORT-FANOUT: no import change needed.
23. CASTS: the single explicit `X none : MvPolynomial (Option τ) R` fixes codomain; no coercion syntax. No cast diff expected.
24. INSTANCE-NAME: n/a, theorem defines no instances.

## Signature widths (Unicode codepoints)

| Line | Width | Next token | Arithmetic | Action |
|---|---:|---|---|---|
|183|98|degreeOf (8)|98 + 1 + 8 = 107|ok|
|184|97|degreeOf (8)|97 + 1 + 8 = 106|ok|
|185|24|end of signature|24 ≤ 100; no next token|ok|

## Inequality occurrence scan

| Region | ≤ | < | ≥ | > | Result |
|---|---:|---:|---:|---:|---|
|Full effective signature and hypotheses|0|0|0|0|equality and hV ≠ 0 only|
|Proof body|0|0|0|0|hU equality only|

Initial actions: test automation/generic routes, binders and alternate degree-zero APIs; retain current proof if no improvement survives clarity/performance filter. No new helper planned. Public instance removal, aeval_X_eq_rename deletion, coeff_uniqueAlgEquiv_symm deletion remain PENDING/unapplied.

## Mathematics and all five actual searches

If U is zero both degrees are zero. Otherwise injective renaming and univariate embedding preserve nonzeroness. Mathlib degreeOf_mul_eq adds the degrees, degreeOf_rename_of_injective identifies the first summand, and the second summand is zero since some j differs from none. This proof genuinely combines the disjoint-variable structure with product degree; no new wrapper/helper is justified.

| Method | Actual query and status | Evidence / finding |
|---|---|---|
|A Lean-Finder|`degree of product multivariate polynomial in disjoint variables` succeeded|tool2.json: degreeOf_mul_eq, degreeOf_prod_eq, degrees_mul_eq; building blocks already used directly|
|B Loogle|`MvPolynomial.degreeOf (_ * _)` succeeded, empty result|tool3.json: empty applies only to this query; no absence claim|
|C LeanSearch|`degreeOf product rename evaluation polynomial disjoint variables` succeeded|tool4.json: degreeOf_mul_X_of_ne, degreeOf_mul_eq, degreeOf_prod_eq; no direct arbitrary-V replacement found|
|D Full source/name search|untruncated rg for full name and degreeOf rename/eval/product patterns in Mathlib/Algebra/MvPolynomial; read Degrees.lean product/rename APIs|`/private/tmp/roth-separation-d19-source-search.log`: generic product and rename APIs found; no full candidate name|
|E local name search|`degreeOf_mul` executed|tool5.json: index unavailable; source fallback returned eight product-degree names. Not an index-certified absence result|

Raw files tool2–5 are `/private/tmp/roth-separation-d19-toolN.json`. Exact generic routes were tested live at target entry: `exact?` failed to close; `apply?` gave generic Nat equalities/inequality subgoals, no direct theorem replacement. Full unfiltered `/private/tmp/roth-separation-d19-attempts.json` preserves all suggestions. No mathematical nonexistence claim is made from these searches.

Strict replacement rules: no new wrapper; existing direct mathlib use retained; auxiliary product/rename/X-power variants inspected; no custom predicate introduced; no equivalent found requiring deletion; module documentation preserved under explicit user contract.

## Public literature search

Actual web query: `multivariate polynomial degree product disjoint variables polynomial integral domain degree variable`. Top three hits were Androma Degree Formula, Choe–Oxley–Sokal–Wagner, and Wikipedia Degree of a polynomial. The primary source inspected was [Choe–Oxley–Sokal–Wagner, Homogeneous Multivariate Polynomials with the Half-Plane Property](https://www.math.lsu.edu/~oxley/ycjoasdw.pdf), Lemma 4.7 proof, printed page 23 (PDF page 22), which uses nonzero leading coefficients in the other-variable polynomial ring to add individual degrees. This supports the existing argument over domains and arbitrary variable sets. [Magma's multivariate element documentation](https://docs.magma-maths.org/BasicRings/MultivariatePolynomialRings/operation-element.html) also treats degree in one chosen variable. Inference from the formal product-degree API: subtraction and finite variable enumeration are unnecessary; isolated compiler probes test this below. No claim that this paper states the semiring generalization.

ChatGPT math MCP: unavailable (tool metadata search found no mathematical second-opinion connector); no outbound messaging or substitute claimed. Existing local source `.mathlib-quality/references/clean.tex` §2, Lemma 2 remains the preserved motivating citation.

## All 42 golf rules

|Rule|Concrete status|
|---|---|
|1.1 by exact|n/a: no wrapper|
|1.2 by rfl|n/a: no reflexivity proof|
|1.3 rw + exact|n/a: product rewrite followed by terminal simp, not exact|
|1.4 simp + exact|n/a: both simp calls close their goals|
|1.5 trailing rfl|n/a: absent|
|1.6 constructor|n/a: equality, no conjunction|
|1.7 apply + exact|n/a: no apply|
|1.8 by_contra!|n/a: direct nonzero split, no contradiction chain|
|1.9 eta reduce|n/a: proof contains no lambdas|
|1.10 inline have|n/a: zero haves|
|1.11 refine fun|n/a: no introductions|
|1.12 redundant show|n/a: none|
|1.13 obtain projections|n/a: no conjunction/existential projection chain; map iff .2 is a direct application|
|1.14 merge rw|product and rename already combined in one rw; no consecutive rw|
|1.15 unsqueeze terminal simp only|n/a: no simp only; both terminal simp retained|
|1.16 squeeze nonterminal simp|n/a: neither simp is nonterminal|
|1.17 dot notation|existing `.not.mpr` and `.2` are direct dot/projection forms; no verbose theorem application to reduce|
|1.18 <||n/a: nested parentheses group rw list arguments, not trailing by/fun blocks|
|1.19 push Not|n/a: no push_neg|
|1.20 existential helper|n/a: no existential helper|
|2.1 whole grind|actually tried live; failed to establish degree identity|
|2.2 before grind|n/a: retained proof has no grind|
|2.3 simpa consolidation|whole simp failed; final shorter simp excluding Multiset.mem_replicate left explicit replicate nonmembership goal; keep targeted current proof|
|2.4 fun_prop|n/a: no continuity/differentiability/measurability goal|
|2.5 positivity|n/a: no positivity goal|
|2.6 gcongr|n/a: equality requires degree API, no monotonic inequality|
|2.7 lia/omega|n/a: no arithmetic hypotheses relate symbolic degree terms; missing polynomial fact cannot follow from arithmetic|
|2.8 aesop|actually tried live, exhaustive search failed|
|2.9 norm_num/norm_cast|n/a: symbolic polynomial, no numerical/cast problem|
|2.10 decide/kernel|n/a: arbitrary coefficient ring and symbolic polynomials, no closed finite computation|
|2.11 field_simp/ring|n/a: degree is not a ring expression, no division|
|2.12 linear_combination|n/a: no ring ending or ring identity target|
|2.13 wlog|n/a: zero and nonzero branches are not symmetric|
|2.14 calc|n/a: no calc|
|2.15 <;>|n/a: two branches require different mathematics; no uniform terminal tactic succeeds|
|3.1 erw→rw|n/a: rw already used|
|3.2 continuity→fun_prop|n/a: no analytic property|
|3.3 omega→lia|n/a: no arithmetic tactic|
|3.4 rcases rfl|n/a: no rcases|
|3.5 automation attrs|none added: this specialized public rule need not be globally registered; API changes remain pending|
|3.6 simp_all|actually tried on final goal with same lemmas: goal closed but original continuation produced a residual syntax diagnostic in the line-replacement tool; no accepted whole-proof improvement, and simp_all scans unnecessary context|
|3.7 heartbeat limits|n/a: no set_option or limit to remove|

## Step-back and simplify review

Reviewed chunks 186–190 (zero case plus nonzero product) and 191–193 (renaming plus disjoint variable). Each step changes the goal or closes a branch. Whole grind/simp/aesop and generic exact?/apply? were actual native attempts; none supplied a complete replacement. Final degree-zero grind also failed. Dropping Multiset.mem_replicate left `some j ∉ Multiset.replicate ... none`, confirming why the final lemma is present. Final attempt tool replaces one source line and left continuation line 193 as a syntax error; these are explicitly not claimed as successful candidate builds. Raw `/private/tmp/roth-separation-d19-final-attempts.json`.

Term-mode rewrite chaining would obscure the same nonzero prerequisites. Induction on V would add coefficient and sum bookkeeping. No duplicated internal haves or long branch motivates a helper; adding one would recreate a wrapper previously removed. Current nine-line proof is retained by the minimum-value filter, with no source mutation and no new helper.

## Every effective binder / generalisation probes

Each trial is an isolated actual compiler invocation, with autoImplicit=false, so dropping a referenced variable cannot silently reintroduce it. Complete machine-readable results: `/private/tmp/roth-separation-d19-probe-results.json`; source/log for each row uses `/private/tmp/roth-separation-d19-NAME.{lean,log}`. Exit 0 is a compiler-verified candidate, exit 1 is a failure of the stated mechanical test, not a theorem of impossibility. No candidate was applied to repository source.

|Binder|Use / mechanical candidate|Actual result|Disposition|
|---|---|---|---|
|τ : Type*|variable index in U, j, Option τ; drop τ|drop_tau exit 1, unknown τ|required dependent type binder; already independent universe u_1, no extra universe restriction|
|Fintype τ|no enumeration in proof; drop; weaker Finite subsumed by complete removal|drop_fintype exit 0; drop_both exit 0|existing public-instance proposal PENDING|
|DecidableEq τ|degree counting simplification; drop and use classical|drop_decidable exit 0; drop_both exit 0|existing public-instance proposal PENDING|
|R : Type*|coefficient type; drop R|drop_R exit 1, unknown R|required dependent type binder; universe u_2 independent of u_1|
|CommRing R|drop; Ring; CommSemiring|drop_commring exit 1 missing Semiring; ring exit 1 missing CommSemiring; commsemiring exit 0|new coefficient weakening proposal, PENDING|
|IsDomain R|nonzero product-degree API; drop; NoZeroDivisors|drop_domain exit 1 missing NoZeroDivisors; nozerodivisors exit 0|new coefficient weakening proposal, PENDING|
|U : MvPolynomial τ R|operand of product and RHS degree; drop U|drop_U exit 1 unknown U|structure-value binder, no parent type substitution that preserves statement; no nonzero-U hypothesis needed|
|V : Polynomial R|operand of aeval and hV; drop V|drop_V exit 1 unknown V|structure-value binder, required input|
|hV : V ≠ 0|injective evaluation nonzero for product degree; drop hV|drop_hV exit 1 unknown hV; separate V=0/U=X ℤ counterexample compiled exit 0|preserve exact nonzero hypothesis; no ordered strict-to-weak variant over arbitrary ring|
|j : τ|chosen variable; drop j|drop_j exit 1 unknown j|required structure-value binder, no pointwise/global weakening|

Combined weakest tested d19 candidate: no Fintype/DecidableEq, `[CommSemiring R] [NoZeroDivisors R]`, same U/V/hV/j; `weakest` exit 0 using `classical`. This does not automatically authorize a public API change. Inversion check: no concrete named mathematical object is being abstracted away; theorem is already polynomial-parametric and its specific rename/evaluation structure supplies disjoint variables. No useful new abstract theorem proposed.

## Concrete grouped public coefficient proposal (not applied)

At owner request, compiled a full-module scratch candidate rather than only a local extracted proof: `/private/tmp/roth-separation-d19-domain-proposal.lean`, compiler log `/private/tmp/roth-separation-d19-domain-proposal.log`, exit 0. Only production-like edit is the Domain section variable line:

```lean
variable {R : Type*} [CommSemiring R] [NoZeroDivisors R]
```

This affects exactly `Roth.degreeOf_rename_mul_aeval` and `Roth.degreeOf_none_rename_mul_aeval`. Both existing proof bodies and every other module declaration are unchanged. Fintype/DecidableEq remain as in current public signatures, so this coefficient option can be considered independently from the existing twelve-theorem instance option. Appended scratch-only #checks confirm both effective signatures; #print axioms for both returns only propext, Classical.choice, Quot.sound. No private helper is involved. Owner notified with concrete source/log paths before any possible application; this worker does not apply it.

The three earlier options remain PENDING/unapplied: twelve-theorem instance removal, aeval_X_eq_rename deletion, coeff_uniqueAlgEquiv_symm deletion. The newly verified grouped coefficient option is likewise PENDING/unapplied. The ORIGINAL public type, including hV, and original docs remain exact.

## Gates

|Gate|Result|Actual evidence|
|---|---|---|
|lake_build_file|pass|`/Users/ramin/.elan/bin/lake build Roth.Separation`, exit 0, 1876 jobs; `/private/tmp/roth-separation-d19-build.log`|
|definition_protected|pass|no source diff; no def/abbrev/import/pin/header changes|
|theorem_statement_protected|pass|original doc+source signature byte-for-byte comparison true; independent explicit ORIGINAL effective type assignment compiles|
|structure_gate|pass|11 declaration lines, 9 proof lines including := by, branches 1 and 6 lines; no conjunction|
|naming_gate|pass|mathematical identifier composed from mathlib identifiers, no forbidden naming pattern|
|line_packing_gate|pass|all three source signature rows measured above; 98/97/24 codepoints|
|inequality_orientation_gate|pass|required full-signature/hypothesis/body scan table above; zero reversed comparison|
|LSP|pass|complete unfiltered native baseline and final: 0 errors, 31 warnings, 0 infos; partial=false, timed_out=false, success=true, failed_dependencies=[]|
|independent proof|pass|`/private/tmp/roth-separation-d19-independent.lean/.log`, exit 0; explicit ORIGINAL type example uses actual target, separate theorem body proves it without calling target|
|actual target axioms|pass|actual built Roth.degreeOf_rename_mul_aeval and independent_original both exactly propext, Classical.choice, Quot.sound, no sorryAx|
|profile target|pass|authorized unchanged actual-module baseline reused: 13.297 ms command + 118.049 ms outer async proof = 131.346 ms, below 750 repeat threshold and 1000 budget|
|diff/whitespace|pass|`git diff --check` exit 0; source diff empty; wc -l 551|

Full native final diagnostics: `/private/tmp/roth-separation-d19-final-lsp.json`; all 31 warnings preserved raw, including unrelated module warnings and user-preserved metadata. Warnings were not suppressed. No affected private helper, new helper, definition or axiom exists.

Actual profile evidence is `/private/tmp/roth-separation-d18-direct-final-profile.log`, authorized by dispatch for this unchanged target. Command anchor line 193639 (`[Elab.command] [0.013297]` with theorem at 193642), outer async proof anchor line 196841 (`[Elab.async] [0.118049] ... Roth.degreeOf_rename_mul_aeval`). Actual parser `/private/tmp/roth-separation-profile-table.py` reconfirmed exactly one command/proof anchor and conservative total 131.346 ms; no nested child times added. No final reprofile is required because target/source are unchanged. No file-wide speedup or all-declaration budget claim is made; unrelated timings remain owner scope.

A preliminary scratch generator accidentally put by_cases on the := by line and produced malformed indentation; that batch was interrupted and all probes were regenerated correctly. Only the corrected completed batch and its overwritten final logs above count as validation. Failed binder probes are retained as negative test evidence, never treated as acceptable proof artifacts.

## Eleven completion steps and freeze

1. Doctor: inherited clean pushed HEAD 82146b3 and actual target baseline; fresh native module LSP complete 0 errors/31 warnings, raw tool0.json.
2. Prepare: both skills, Phase 4, full golfing/proof-pattern docs, relevant search/generalisation/style/naming/gates/profiling references read; target and ORIGINAL contract located.
3. Initial audit: all 24 numbered items written before source edits; in fact no source edits were needed.
4. File-level fixes: none authorized within target; preserved header metadata and pending instance options.
5. Per-declaration golf: all 42 statuses recorded, actual native entry and final-step attempts; retained already direct short proof.
6. Refactor: no new helper, no rename, no source change; existing three public proposals and new concrete grouped coefficient proposal remain pending.
7. Module gate: actual lake build Roth.Separation exit 0; diff/whitespace check exit 0.
8. LSP gate: fresh complete unfiltered final native response saved, 0 errors/31 warnings/0 infos, no pending ranges or dependencies.
9. Contract/independence/axioms: explicit ORIGINAL effective signature compiles; non-self independent proof compiles; actual built target and independent theorem use exactly the three permitted standard axioms. All binders mechanically probed; hV necessity additionally certified by compiled counterexample. Parent whole-original/all-retained probe not duplicated.
10. Simplify/buzz: whole-proof replacement and alternate strategies reviewed; no improvement survived. Unchanged actual repository target has anchored conservative 131.346 ms, no profiler scaffolding or limit added. Full-module grouped proposal compiled separately without modifying repository.
11. Report/freeze: source 551→551 lines, declaration 11→11 lines, proof 9→9 lines, retained declarations 23→23, 0 source additions/deletions. ALL source ownership revoked; report-only. ALL Lean/MCP/compiler/profile requests drained, including completed proposal session and corrected probe batch. Parent owns sequential full project and separate LeanEval, complete original/all-retained probes, exact-path report commit and push.

Frozen source SHA256: `1c58b8b35fe3c01d326d802b94c54dbc8ed0349e1ca388f87e9b34aa2a0278d4`.

## Owner cumulative publication gates

Source FROZEN SHA256 `1c58b8b35fe3c01d326d802b94c54dbc8ed0349e1ca388f87e9b34aa2a0278d4`; leaf ownership revoked and requests drained before owner gates. Owner probe `75014` exit0,34.54s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL23 actual retained standardaxiom checks. `/private/tmp/roth-separation-d19-compatibility.{lean,log,json}`. Owner build session `45446` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,5.75s/2.65s; source hash stable. `/private/tmp/roth-separation-d19-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.
