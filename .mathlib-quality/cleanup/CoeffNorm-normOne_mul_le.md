# Phase 4: `Roth.normOne_mul_le`

Current amendment: the user explicitly approved the unused public-binder removals on
2026-10-16. See [approved amendment audit](CoeffNorm-api-amendment.md) for the current
source, types, warning count and verification. The original audit below records its
historical checkpoint and remains unchanged.

Scope: only the target block in `Roth/CoeffNorm.lean` (initial L89–102, final L89–97) and this report. Parent supplied branch `ramin-cleanup`, HEAD `84b944e`, full baseline build followed by separate LeanEval session 90598 exit 0, and complete baseline LSP without errors. No Git or shared-log operations performed.

Read the full mathlib-quality and lean4 SKILL.md files, `/private/tmp/roth-coeffnorm-worker-contract.md`, and required references golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, cleanup-gates.md, style-rules.md, naming-conventions.md; also mathlib-review-stages.md and local source `clean.tex` L475–498. Native Lean MCP discovered through ALL_TOOLS worked; no fallback needed.

SOURCE FROZEN: whole-file SHA256 `7e5a4e7491daccb1e05fc20d375fc5bc64f27abc581fbb79cf97595b491e589a`. Parent explicitly revoked source ownership at this hash. All source editing finished before freeze; subsequent work is report, probes, and verification only.

## Audit (all 24 items)

1. LINT: target has the known unused `[DecidableEq σ]` warning. Kept by explicit parent instruction pending a scoped user decision; verified drop candidate below. Complete final LSP has six warnings: preserved header, four unused DecidableEq hypotheses, and unused `hC`. No suppression introduced.
2. HAVE SCAN: initial L93 `have hPQ : ... := by` has proof content, used once at initial L98; the mechanical no-by inline rule does not apply. Replaced the entire expansion proof and its use with existing `MvPolynomial.mul_def`. Final proof has no have.
3. SET_OPTION: none; no heartbeat or recursion changes.
4. SIMP SQUEEZE: initial expansion's terminal `simp [monomial_mul_monomial]` disappears with the redundant expansion; final L97 terminal `simp [normOne_monomial, abs_mul]` remains unsqueezed. Native simp? confirms the exact set `normOne_monomial, Int.cast_mul, abs_mul`; no nonterminal bare simp exists.
5. NAMING: `normOne_mul_le` describes coefficient-norm submultiplicativity using the existing `normOne` identifier, with `_mul_le` orientation. No forbidden abbreviation, single-letter public name, or numerical scheme; no rename needed.
6. LINE PACKING: both signature lines measured below; complete conclusion does not fit on first line. All target lines ≤100 codepoints.
7. BY PLACEMENT: `by` stays at end of the conclusion line.
8. FORMAT: two-space tactics, four-space continuation, no internal blank lines, no haveI/letI. Normalized both ordinary lambda arrows from `=>` to `↦`.
9. COMMENTS: no inline proof comments existed. Existing public docstring and source attribution preserved byte for byte.
10. DOCSTRING: existing statement of submultiplicativity plus §3 source identifies this public API result; preserved under existing-docstring protection.
11. VISIBILITY: public main result named in module documentation and consumed by finite products; retained.
12. STRUCTURE: ten proof-body lines become five; no conjunction or case branch, below main-result ≤15-line limit.
13. MATHLIB: five-method search found a directly useful expansion API, `MvPolynomial.mul_def`; replaced manual expansion. Detailed search block below.
14. JUNK DEF: n/a: theorem, not a data definition.
15. EXISTS LEMMA: n/a: no existential statement or witness helper.
16. SHOW vs CHANGE: n/a: neither appears.
17. PUSH_NEG: n/a: no negation tactic.
18. GENERALISE: every parameter appears in the mechanical table below. Decidability drop verified independently but explicitly deferred; public type stays unchanged.
19. INEQUALITY: one ≤, zero ≥ or > in the signature and its hypotheses; table below.
20. NORMAL-FORM: already canonical submultiplicative form `f (P * Q) ≤ f P * f Q`; no equivalent-form theorem introduced.
21. SYNTAX-GEN: OK: explicit P/Q arguments support direct composition with the product induction. Removing decidability improves generality but is the pending API proposal, not silently applied.
22. IMPORT-FANOUT: n/a: no imports changed.
23. CASTS: 0 dropped / 0 kept as cross-type / 0 kept as load-bearing in the diff. The replacement contains no explicit coercion or ascription; existing definition's casts are outside this scope.
24. INSTANCE-NAME: n/a: theorem introduces no named instance.

Issues found: redundant manual product expansion and two lambda-arrow style occurrences, all fixed. Target unused decidability warning remains deliberately visible pending the parent's scoped approval flow.

## Mathlib search status

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | sum absolute values polynomial coefficients submultiplicative multiplication | `Polynomial.cauchyBound`, `Polynomial.mahlerMeasure_mul`, `Polynomial.mahlerMeasure_le_sum_norm_coeff`, `Dioph.abs_poly_dioph`; related but no direct target replacement |
| B Loogle | `MvPolynomial, _ * _ ≤ _ * _` | empty result |
| C LeanSearch | l1 norm of multivariate polynomial product is at most product of coefficient l1 norms | generic norm product bounds `Finset.norm_prod_le'`, `Finset.nnnorm_prod_le`, `Finset.nnnorm_prod_le'`, `List.norm_prod_le`; no theorem about local normOne |
| D source rg | `normOne_mul_le`, sum/abs/mul and norm/mul_le patterns in MvPolynomial, Finsupp, MonoidAlgebra, normed Lp directories; `mul_def`, `sum_mul_index` variants | `MvPolynomial.mul_def` at Basic.lean L101–102 directly supplies the manually proved expansion; no full-name occurrence of `normOne_mul_le` in Mathlib |
| E local names | `sum_mul`, `MvPolynomial.mul_def` | `Finset.sum_mul_sum`, `Finsupp.sum_mul`, and `MvPolynomial.mul_def` confirmed; index warming, so no absence conclusion based on empty index |

Auxiliary variants checked: Finsupp sum and sum-index routes, AddMonoidAlgebra.mul_def, MvPolynomial.mul_def, finite double sums, generic norm-product bounds, and WithLp Finsupp API. Initial rg used a nonexistent Group/Finsupp path; corrected with rg --files to Analysis/Normed/Lp/Finsupp.lean. A second guessed Order/BigOperators/Finsupp path also did not exist; not treated as evidence of absence. The canonical equivalents table has no discrete/finite/bounded pattern matching this result.

Conclusion: partial match, build on `MvPolynomial.mul_def`, retaining the established public coefficient-norm API. No claim that the mathematical convolution estimate is absent from all mathlib abstractions. The full-name rg was untruncated. Native exact? at the target could not close; apply? produced only generic partial order refinements, not a proof. Generic supplied norm bounds concern an installed norm structure, whereas this declaration uses a protected local `normOne` definition.

Six strict rules: (1) no wrapper added; (2) all five searches plus compiled exact?/apply? probes executed; (3) auxiliary variants examined; (4) no custom predicate introduced; (5) the exact duplicate expansion was removed in favor of the library theorem; no public declaration deletion authorized; (6) usage is documented here, while existing module docstrings remain protected.

## Generalisation status

| # | Parameter | Class | Used as | Mechanical candidates tried | Verified? | Result |
|---|---|---|---|---|---|---|
| 1 | `{σ : Type*}` | type variable | polynomial variable index | drop binder with autoImplicit=false; Type*→Sort*; inspect universe poly | yes | drop gives unknown σ; Sort* gives MvPolynomial type mismatch; already universe polymorphic, retain |
| 2 | `[DecidableEq σ]` | decidability | finite-support elaboration in proof, absent from mathematical type | drop instance, use classical locally | yes | independent full proof compiles without this parameter; NOT APPLIED per explicit parent instruction pending scoped user approval |
| 3 | `(P : MvPolynomial σ ℤ)` | structure value | product and first factor coefficient sum | drop P binder with autoImplicit=false | yes | unknown P in conclusion, retain explicit argument; no property of P to weaken |
| 4 | `(Q : MvPolynomial σ ℤ)` | structure value | product and second factor coefficient sum | drop Q binder with autoImplicit=false | yes | unknown Q in conclusion, retain explicit argument; no property of Q to weaken |

No algebra/analysis typeclass parameter other than decidability; no proposition, strict hypothesis, pointwise/global function property, or bundled hypothesis exists. Thus parent-class, point-localisation, strict→weak, and unbundling catalogue entries have no parameter to act on. DecidableEq has no weaker parent supporting an alternative signature beyond dropping it. P and Q's types follow the protected definition domain, not an optional assumption. Generalizing coefficients from ℤ to an arbitrary CommRing in an isolated probe fails at normOne Q: normOne requires integer coefficients. A normed-ring restatement would require a new generalized definition rather than a hypothesis weakening.

Candidate verification used native lean_run_code and a fresh CLI probe after native scratch imports reported stale. No candidate altered the live public signature. Verified positive result: `/private/tmp/coeffnorm-d10-final.lean` independently proves the theorem for `{σ : Type*}` without `[DecidableEq σ]`, using classical, and exits 0. Negative drop/Sort/general-coefficient candidates are preserved in `/private/tmp/coeffnorm-d10-negative.lean`; expected errors do not contaminate project source.

Fresh negative CLI `/Users/ramin/.elan/bin/lake env lean /private/tmp/coeffnorm-d10-negative.lean`, session80359, exited1 as expected: unknown σ/P/Q for corresponding binder drops, Sort-vs-Type mismatch for Sort*, and integer-coefficient domain mismatch for generalized R. This independently reproduces the native negative candidate outcomes without stale-import diagnostics.

Inversion check: after `MvPolynomial.mul_def`, the proof is the finite convolution triangle inequality plus multiplicativity of absolute value. This explains the broader normed coefficient-ring possibility, but a new abstract norm API is beyond the preserved definition contract. Existing general finite-sum lemmas already handle the abstract summation; no extra local helper is warranted.

Big-change candidate requiring action: remove target `[DecidableEq σ]` using local classical, already included in `.mathlib-quality/cleanup/CoeffNorm-api-proposal.md`. Explicitly pending parent/user decision; earlier Box approval does not cover this theorem. Broader coefficient-norm redesign is a possible future project, not a prerequisite for this cleanup.

## Public literature search

Query 1: `polynomial coefficient l1 norm submultiplicative convolution generalization`. Top three displayed results:

1. [A Generalization of the Widder–Arendt Theorem](https://citeseerx.ist.psu.edu/document?doi=567e03155d65056ba0c129ee3f88ec92aaaf3962&repid=rep1&type=pdf): weighted convolution context, not a direct polynomial hypothesis improvement.
2. [Minimal Norm Interpolation in Harmonic Analysis](https://citeseerx.ist.psu.edu/document?doi=b144bc5983cd3e2611b427471970995c551cea65&repid=rep1&type=pdf): weights and Wiener-type convolution; related general setting.
3. [Dense m-convex Fréchet Subalgebras of Operator Algebras](https://citeseerx.ist.psu.edu/document?doi=87c016ffe669c7aa1656b7326f286db65271e99b&repid=rep1&type=pdf): broader weighted algebra setting; no direct change applied.

Query 2: `"polynomial" "norm" "submultiplicative" "coefficients" l1`. Top three displayed results:

1. [Beauzamy, Products of polynomials and a priori estimates for coefficients in polynomial decompositions](https://www.sciencedirect.com/science/article/pii/S0747717110800069): weighted polynomial norm is submultiplicative; the weights distinguish it from this unweighted result.
2. [Norms on Taylor Polynomials, Appendix A](https://wrap.warwick.ac.uk/id/eprint/191810/1/WRAP-Cauchy-born-rule-microscopic-models-25.pdf): primary manuscript discusses ℓ1-type norms and submultiplicative weights.
3. [IAS/Park City Mathematics Series notes](https://abhayg11.github.io/pcmi22/harvey/pointcounting.pdf): row ℓ1 matrix norms; related but not this coefficient theorem.

Query 3: `Young convolution inequality l1 sequences Banach algebra site:edu`. Top three displayed results:

1. [Driver, Approximation Theorems and Convolutions, Theorem 22.30](https://www.math.ucsd.edu/~bdriver/240A-C-03-04/Lecture_Notes/Older-Versions/chap22.pdf): Young convolution norm inequality and L1 algebra property.
2. [Driver, Analysis notes, Theorem 42.11](https://mathweb.ucsd.edu/~bdriver/231-02-03/Lecture_Notes/PDE-Anal-Book/analpde2-2p.pdf): another primary presentation of Young's inequality.
3. [Driver, Convolution and Young's Inequalities](https://mathweb.ucsd.edu/~bdriver/240A-C-03-04/Lecture_Notes/Older-Versions/chap22.pdf): duplicate host presentation of item 1, recorded rather than counted as independent evidence.

Also returned [Heil's sequence convolution notes](https://heil.math.gatech.edu/metricnote/extra.pdf), directly discussing ℓ1(Z) submultiplicativity. Inference from these primary sources: the finite coefficient estimate is an instance of the convolution ℓ1 bound; integer coefficients and a decidability parameter are not mathematically essential. The local source clean.tex L492–498 explicitly requests this submultiplicativity for the determinant bound. No literature result authorizes changing the protected public API. ChatGPT math MCP: n/a, ALL_TOOLS exposes no such tool.

## Candidate experiments and reflection

Whole-proof native attempts: grind fails; simp [normOne] leaves the coefficient-sum inequality; aesop makes no progress; exact? cannot close; apply? yields only partial generic order refinements. Initial line replacement at a multiline have left parser remnants below it: these diagnostics are not counted as mathematical failures, while the tactic-specific unsolved-goal results remain valid. Repeated probes after the one-line expansion replacement avoid that remnant. `grind [MvPolynomial.mul_def]` still fails; gcongr at the original inequality makes no progress.

Direct library candidate: rewrite MvPolynomial.mul_def, then apply normOne_sum_le twice, distribute the product of coefficient sums, and simplify monomial norms. Native independent reproof succeeded with no errors. This removes hPQ rather than merely golfing its construction, and uses the more general CommSemiring expansion API directly.

Final monomial equality at L97 column39: simp [normOne_monomial, abs_mul] closes; grind with those hints also closes but warns abs_mul is redundant; aesop leaves the equality; simp? closes with suggestion simp only [normOne_monomial, Int.cast_mul, abs_mul]. Retain the clear terminal unsqueezed simp. An earlier line-based probe targeted the expression outside `by` and returned Unknown identifier simp/grind; reran at the exact tactic column and did not treat positioning errors as tactic failures.

Step-back reflection: one-tactic replacements do not establish this convolution bound. The newly found multiplication API eliminates the only local have and all manual monomial algebra. Remaining five lines follow the mathematical argument directly: expand convolution, bound outer and inner finite sums, then use |ab|=|a||b|. Term-mode composition of the whole nested sum proof would obscure the intermediate rewrite and would not reduce mathematical work. No case extraction, helper, or missing wrapper/coercion API is needed.

## Golfing-rule pass (42/42)

| Rule | Status |
|---|---|
| 1.1 by exact wrapper | n/a: body has required expansion and summation rewrites |
| 1.2 by rfl | n/a: no reflexivity wrapper |
| 1.3 rw + exact→rwa | n/a: rewrite prepares two different sum inequalities; final exact is not a transported unchanged hypothesis |
| 1.4 simp + exact→simpa | n/a: simp already closes the monomial equality |
| 1.5 trailing rfl | n/a: no trailing rfl |
| 1.6 anonymous constructor | n/a: no conjunction or constructor |
| 1.7 apply + exact | n/a: final exact already directly supplies the proof |
| 1.8 by_contra! | n/a: no contradiction proof |
| 1.9 eta reduction | both lambdas genuinely depend on bound a/b and ignore membership, so not eta-reducible; arrows normalized |
| 1.10 inline have | hPQ had by, but stronger library replacement removes it entirely |
| 1.11 refine + fun | n/a: no apply/intro sequence |
| 1.12 redundant show | n/a: none |
| 1.13 obtain | n/a: no paired projections |
| 1.14 merge rw | initial consecutive rw steps in hPQ disappear with library replacement; final rewrites separated by necessary inequality refinement |
| 1.15 terminal simp-only | n/a: existing terminal simp unsqueezed |
| 1.16 nonterminal simp | n/a: no nonterminal simp |
| 1.17 dot notation | already trans and trans_eq compositions |
| 1.18 use <\| | already used for final equality argument; no redundant trailing parentheses |
| 1.19 push Not | n/a: no push_neg |
| 1.20 inline existential | n/a: no existential lemma |
| 2.1 whole grind | tried, failed; also failed with mul_def hint |
| 2.2 delete before grind | whole hinted grind attempted and fails; no retained grind block |
| 2.3 simpa consolidation | n/a: no simp-followed-by-closing-tactic sequence |
| 2.4 fun_prop | n/a: no continuity/differentiability/measurability goal |
| 2.5 positivity | n/a: no standalone zero-bound or nonzero subgoal |
| 2.6 gcongr | tried at whole bound, no progress; explicit summation bounds retained |
| 2.7 lia/omega | n/a: inequality is real coefficient convolution, not Nat/Int linear arithmetic |
| 2.8 aesop | tried whole bound and final monomial equality, fails |
| 2.9 norm_num/norm_cast | n/a: no numerical computation or cross-type equality goal remains; cast_mul handled by terminal simp |
| 2.10 decide/+kernel | n/a: universally quantified polynomial and real bound, not finite computable proposition |
| 2.11 field_simp; ring | n/a: no denominator algebra |
| 2.12 linear_combination | n/a: proof ends in simp, no ring/ring_nf block with hypotheses |
| 2.13 wlog | n/a: no symmetric case branches |
| 2.14 calc→term | already trans/trans_eq rather than calc; no two-step calc remains |
| 2.15 <;> | n/a: no multiple parallel goals |
| 3.1 erw→rw | n/a: no erw |
| 3.2 fun_prop | n/a: no legacy continuity/measurability tactics |
| 3.3 omega→lia | n/a: no omega and no integer arithmetic goal |
| 3.4 rcases with rfl | n/a: no cases or substitution |
| 3.5 automation attributes | no new attribute: nonlinear norm inequality is not a simp rewrite; adding grind registration changes public automation and is unnecessary here |
| 3.6 simp_all | n/a: no simp_all only |
| 3.7 remove limits | n/a: no maxHeartbeats/maxRecDepth |

## Line packing

Fresh CLI reference with `set_option format.width 100`, `#check @Roth.normOne_mul_le`:

```lean
@normOne_mul_le : ∀ {σ : Type u_1} [DecidableEq σ] (P Q : MvPolynomial σ ℤ), normOne (P * Q) ≤ normOne P * normOne Q
```

Lean emits the theorem check on one logical output line even at width100; source widths below were measured as codepoints, independently of that rendering. Treat the complete conclusion as the semantic next signature token, as in the contract's `: conclusion :=` examples.

| Sig line | Chars | Next token | Arithmetic | Action |
|---|---:|---|---|---|
| 91 | 65 | complete conclusion `normOne (P * Q) ≤ normOne P * normOne Q := by` (45 chars) | 65+1+45=111>100 | ok |
| 92 | 49 | no next signature line; proof body follows | n/a | ok |

Final target maximum line length is70 codepoints (proof); signature max65. No hypothesis or entire conclusion can be moved intact onto the preceding line. Source signature remains byte-identical.

## Inequality scan

| # | Location | Original | Rewrite | Lemma rename? |
|---|---|---|---|---|
| 1 | L92 conclusion | normOne (P * Q) ≤ normOne P * normOne Q | none: already ≤ | none |
| 2 | full signature and hypotheses | n/a: zero ≥ and zero > | none | no _ge_/_gt_ name |

## Verification and gates

Complete native LSP before and after: success=true, partial=false, timed_out=false, failed_dependencies=[], zero errors, six known warnings. No sorry diagnostic. Target warning retained explicitly pending scoped API decision. Final module command `/Users/ramin/.elan/bin/lake build Roth.CoeffNorm`, session28226, exited0: Built Roth.CoeffNorm (18s), Build completed successfully (1658 jobs). Full project build belongs to parent; this worker did not duplicate it.

Native scratch probes later reported stale imports. Fresh independent CLI `/Users/ramin/.elan/bin/lake env lean /private/tmp/coeffnorm-d10-final.lean`, session30038, exited0, confirms exact original type application, nonself reproof without DecidableEq, and both axiom checks. Output:

```text
'Roth.normOne_mul_le' depends on axioms: [propext, Classical.choice, Quot.sound]
'_private._stdin.0.independent' depends on axioms: [propext, Classical.choice, Quot.sound]
```

The independent theorem's body never calls normOne_mul_le, so its generality check is not circular. No new axiom, sorry, native_decide, suppression, or limit increase. Frozen-source SHA rechecked after probes and unchanged.

| Gate | Result | Details |
|---|---|---|
| lake_build_file | ✓ pass | actual module build session28226 exit0 |
| definition_protected | ✓ pass | no definition, abbreviation, or value changed |
| theorem_statement_protected | ✓ pass | exact original signature and docstring unchanged; fresh compiled application |
| structure_gate | ✓ pass | body5 lines ≤15; no conjunction or branches |
| naming_gate | ✓ pass | descriptive normOne_mul_le; no forbidden pattern or abbreviation |
| line_packing_gate | ✓ pass | both signature lines measured above; no intact binder/conclusion fits preceding line |
| inequality_orientation_gate | ✓ pass | zero ≥/>; complete occurrence table above |
| scope/source freeze | ✓ pass | diff against private pre-edit snapshot contains only owned target proof; final whole-file hash supplied to parent |

Overall: pass, with the explicitly pending public decidability proposal retained as a visible warning. No renames queued; no source ownership remains.

## Result

Before:10 proof-body lines /12 declaration lines. After:5 proof-body lines /7 declaration lines. Saved:5 lines. Changes: replace redundant product expansion with MvPolynomial.mul_def; normalize two lambdas. Comments preserved: existing public docstring unchanged; no proof comments present. Rules applied: direct library replacement, have elimination by library API, lambda normalization; existing trans/trans_eq and terminal simp retained after probes.

Refactoring needed: scoped decision on removal of `[DecidableEq σ]`, already in the parent's combined CoeffNorm API proposal. Keep this public type until approval; no other required refactoring.

- [✓] Step 1 — full required reference docs read
- [✓] Step 2 — full24-item audit recorded
- [✓] Step 2.5 — all five mathlib search methods recorded
- [✓] Step 2.6 — every parameter mechanically analysed and candidate probes recorded
- [✓] Step 2.7 — full signature packing table and width100 #check recorded
- [✓] Step 2.8 — inequality occurrence scan recorded
- [✓] Step 3 — all42 golfing rules have a status
- [✓] Step 4 — independent strategy/reflection recorded
- [✓] Step 5a — complete final LSP has zero errors
- [✓] Step 5b — module build, original-type/nonself reproof, axiom and diff gates pass
- [✓] Step 6a — no rename needed; no sidecar mutation
