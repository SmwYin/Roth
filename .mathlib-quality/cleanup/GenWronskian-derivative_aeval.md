# Phase 4 — Roth.derivative_aeval

Result: complete. Declaration L125–138 (14 lines) → L125–134 (10 lines); proof 11→7 lines, saved 4. Source frozen SHA256 `2d8077043642a40c4a55a8d438157c5234fa7c35c04d38567839fe1028249f32`. Three issues fixed: redundant manual multiplication branch, ordinary lambda arrow, semicolon tactic chain (the latter two disappear with the replaced branch). Public type, existing docstring, all comments and definition values preserved. No helpers, renames, imports, new axioms or options. Refactoring needed: none.

## Step 1 — references

Read both installed SKILL.md files, full `/private/tmp/roth-genwronskian-worker-contract.md`, initial `.mathlib-quality/cleanup/GenWronskian.md`, and mandatory references: golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, cleanup-gates.md, naming-conventions.md and relevant style-rules.md sections. I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md.

## Step 2 — full audit

1. LINT: no warnings/errors in target. Complete file diagnostics retain exactly five outside warnings: header metadata, two unused-Fintype warnings for the dependent-zero theorem, unused DecidableEq in det_sum_rows, unused Fintype in existence theorem. These are outside ownership and preserved.
2. HAVE SCAN: zero `have` declarations, so no single-use bindings to inline.
3. SET_OPTION: none in target; no raised heartbeat/recursion limits.
4. SIMP SQUEEZE: C and add cases terminal simp already appropriate. Original nonterminal simp only was explicitly squeezed; replacement makes the entire mul_X branch terminal simp, avoiding a maintenance-heavy squeezed list. Trial lists had unused arguments; final list has no unusedSimpArgs warnings.
5. NAMING: derivative_aeval describes differentiation after algebra evaluation; snake_case; no forbidden abbreviations/numeric patterns/single-letter name. No rename.
6. LINE PACKING: all three signature lines checked in table below; preserved verbatim.
7. BY PLACEMENT: by remains at end of final signature line.
8. FORMAT: two-space proof indentation, no blank lines in declaration, each proof branch compact, no haveI/letI. Original inner rw;ring chain removed.
9. COMMENTS: zero proof comments; existing four-line source docstring preserved byte-for-byte.
10. DOCSTRING: existing statement/source documentation adequate and protected; no edits.
11. VISIBILITY: public algebraic chain-rule API, protected as requested; no visibility change.
12. STRUCTURE: proof 7 lines, longest branch 2 tactic lines; no conjunction in statement, no helper needed.
13. MATHLIB: five actual search methods and generic search probes below; no exact replacement found.
14. JUNK DEF: n/a, theorem rather than definition.
15. EXISTS LEMMA: n/a, equality theorem rather than existential witness helper.
16. SHOW vs CHANGE: neither occurs.
17. PUSH_NEG: none occurs.
18. GENERALISE: every actual parameter assessed below, including successful CommSemiring scratch and failed structural drop tests. Public API preserved; optional widening closed without speculative follow-up.
19. INEQUALITY: no order predicates; zero ≥ or > tokens in signature.
20. NORMAL-FORM: standard algebraic chain rule, derivative on LHS and sum of evaluated partials on RHS; no alternate canonical equivalence needed.
21. SYNTAX-GEN: explicit substitution and polynomial are convenient for rewriting; bundled derivations would require extra scalar-action setup at this call site. Keep applied equality.
22. IMPORT-FANOUT: n/a, no import added.
23. CASTS: zero explicit casts/ascriptions in diff, so 0 dropped/0 cross-type/0 load-bearing.
24. INSTANCE-NAME: n/a, theorem introduces no named instance.

Issues to fix: replace manual mul_X expansion/congruence/ring by terminal simplification; resulting replacement also removes an ordinary => lambda and semicolon. All fixed. Refactoring needed: none.

## Step 2.5 — Mathlib search-status

[A] Lean-Finder: actual query `multivariate polynomial chain rule derivative evaluation sum partial derivatives`, 4 results: MvPolynomial.aeval_sumElim_pderiv_inl; MvPolynomial.mkDerivationₗ; Polynomial.derivative_eval₂_C; pderiv_sumToIter (old name, not used). Partial matches only.
[B] Loogle: actual `MvPolynomial.aeval, MvPolynomial.pderiv`, results include aeval_sumElim_pderiv_inl and Algebra.Generators cotangent representation lemmas. These commute special substitutions/describe cotangent coordinates, not this chain rule.
[C] LeanSearch: actual natural-language derivative-of-evaluation/sum-partials query, hits MvPolynomial.mkDerivation and related derivation APIs. No direct applied chain-rule replacement.
[D] Grep mathlib: inspected full relevant aeval/pderiv/chain matches in Algebra/MvPolynomial/PDeriv.lean, Algebra/MvPolynomial/Derivation.lean and RingTheory/Derivation/*.lean; examined derivation_ext, mkDerivation, pderiv_mul, Derivation.map_aeval, apply_aeval_eq. No exact full-name derivative_aeval match outside this project target was identified; univariate map_aeval and derivative_eval₂_C have different domains.
[E] Name pattern: actual native lean_local_search `derivative_aeval` returned only Roth.derivative_aeval, index=warming (not evidence of absence); `pderiv_mul` returned MvPolynomial.pderiv_mul/pderiv_C_mul and project Hasse variants, index=warming. Source verification and compiled probes supplement this incomplete index.
Auxiliary variants examined: pderiv_mul, pderiv_C_mul, derivation_ext, derivation_eq_of_forall_mem_vars, mkDerivationEquiv, aeval_sumElim_pderiv_inl, map_aeval, apply_aeval_eq, derivative_eval₂_C. Common-equivalents lookup: no discrete/finite/topology disguise; target already uses standard MvPolynomial/aeval/Derivation concepts.

Native lean_multi_attempt tried whole-goal simp/grind/aesop/exact?/apply?: simp made no progress, grind and aesop failed; exact? could not close; apply? suggested coefficient/extensionality detours only. The line replacement tool additionally reports trailing old induction branches, so those extra parser diagnostics are trial-artifact noise, not a source failure. The actual goal-level failure messages establish no automatic direct proof found. No claim of global mathematical absence is made. Generic derivation comparison requires constructing a pullback scalar action and two derivations; existing polynomial induction is shorter and needs no new imports/helpers. Final local proof builds directly on the existing derivative/partial-derivative and finite-sum simp API. No ugly wrapper/coercion/instance-plumbing extraction signal remains.

## Step 2.6 — generalisation status

| Parameter | Class | Dependency / candidates | Verification and outcome |
|---|---|---|---|
| `{K : Type*}` | type/universe | Coefficient type of γ, P, derivative, aeval; drop cannot state these typed terms. Already independent universe-polymorphic Type*. | Original-type compile confirms polymorphism; no concrete-type weakening applies. |
| `[Field K]` | typeclass | Drop; DivisionRing; CommRing; CommSemiring. No division/negation used. | Dropping structure fails at polynomial Semiring and MvPolynomial CommSemiring formation. DivisionRing fails CommSemiring K/Polynomial K. Strongest successful weakening: full independent proof compiles over CommSemiring K, hence also covers CommRing. Keep original Field API per authorization; optional widening has no present consumer and is closed. |
| `{σ : Type*}` | type/universe | Variable type occurs in γ, P and sum; dropping loses these typed binders; already Type*, no universe coupling. | Exact original-type compile; no concrete index restriction present. |
| `[Fintype σ]` | typeclass/data | Drop; Finite with locally chosen Fintype; finite-set support reformulation. | Actual drop test fails `Fintype σ` in statement at ∑; this is a statement-formation dependency, not a failed-proof necessity claim. Finite would require supplying a chosen enumeration before the statement's sum elaborates; support sum changes public statement. No change needed. |
| `(γ : σ → Polynomial K)` | structure value | Drop; point-localise; weaken differentiability. | Exact γ is substituted on LHS and appears with its derivative and aeval on RHS. No regularity hypotheses exist to localise. With σ=Unit, K=ℚ and P=X (), γ=X versus γ=0 gives derivative 1 versus 0, so there is real substitution data. Removing γ cannot preserve these terms. |
| `(P : MvPolynomial σ K)` | structure value | Drop; restrict support/degree. | P appears in evaluated polynomial and every partial; restriction would strengthen the theorem. With γ()=X, P=X () versus P=0 gives derivative 1 versus 0. Removing P loses the arbitrary-polynomial assertion. |

There is no `l` parameter in the actual public type; no order/strictness, decidability, topology, propositional or bundled hypotheses to weaken. Inversion check: polynomial-specific derivative evaluation is essential in every induction case; arbitrary derivations are a broader optional reformulation, but require an algebra/module substitution setup and do not improve this preserved applied API. No new generic helper is required.

Scratch evidence (outside repository): `/private/tmp/roth-d11-probe.lean` proves entire chain rule over CommSemiring, exit0 session10191, only standard axioms. `/private/tmp/roth-d11-drop_fintype.lean` session90049 exit1; drop_coefficient_structure session80956 exit1; divisionring session10113 exit1. Failed drop results are described only as the exact elaboration dependencies they demonstrate. No changes to public signature applied.

### Literature search status

Actual web queries included `algebraic chain rule multivariate polynomial derivation commutative ring generalization`, `site.stacks.math.columbia.edu derivation polynomial ring partial derivatives`, `site.ncatlab.org derivation polynomial chain rule`, and a targeted Stacks/generalization query. Top three relevant returned hits from the nLab query: [chain rule](https://ncatlab.org/nlab/show/chain+rule), [total derivative](https://ncatlab.org/nlab/show/total+derivative), [derivation](https://ncatlab.org/nlab/show/derivation). The Stacks query returned [Differentials 10.131](https://stacks.math.columbia.edu/tag/00RM), [Differentials 111.50](https://stacks.math.columbia.edu/tag/02AT), and the algebra PDF/index among its top relevant hits. Final targeted query top three returned results: Stacks index, a mirror of Regularity and derivations, and Columbia Optimization notes; these were search observations, not relied upon as algebraic authority. Other returned references: [Elkies, Derivatives and Derivations](https://people.math.harvard.edu/~elkies/M250.04/deriv.html) and [higher derivation chain rule paper](https://arxiv.org/abs/1611.01940).

The canonical algebraic perspective is a derivation determined by its values on polynomial generators; no field division is intrinsic. Strongest concrete evidence for semiring generality is the kernel-checked scratch proof, rather than extrapolating an analytic chain-rule statement. Native tool inventory has no ChatGPT math MCP, so that query is unavailable. No literature-driven action remains pending under preserved-API scope.

## Step 2.7 — line packing

`#check @Roth.derivative_aeval` with format.width100:

```lean
@Roth.derivative_aeval : ∀ {K : Type u_3} [inst : Field K] {σ : Type u_4} [inst_1 : Fintype σ] (γ : σ → Polynomial K)
  (P : MvPolynomial σ K),
  Polynomial.derivative ((aeval γ) P) = ∑ j, Polynomial.derivative (γ j) * (aeval γ) ((pderiv j) P)
```

Lean prints an indivisible binder group over 100 despite format.width100; source signature is ≤100 on every line.

| Signature line | Codepoints | Next semantic token/group | Arithmetic | Action |
|---|---:|---|---|---|
|125|72|`Polynomial.derivative (aeval γ P)` (33)|72+1+33=106 >100|ok|
|126|39|`∑ j, Polynomial.derivative (γ j) * aeval γ (pderiv j P) := by` (61)|39+1+61=101 >100|ok|
|127|67|none; proof starts|n/a|ok|

The sum binder/group stays intact; joining it to the preceding equation line exceeds 100 by one codepoint. All source signature lines unchanged.

## Step 2.8 — inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
|—|signature/hypotheses|n/a, no ≥ or > in Lean code|none|none|

## Step 3 — all 42 golfing rules

| Rule | Status |
|---|---|
|1.1 by-exact wrapper|n/a, no declaration-level by exact.|
|1.2 by-rfl|n/a, no by rfl.|
|1.3 rw+exact→rwa|n/a, no such sequential pair.|
|1.4 simp+exact→simpa|Original expansion/congruence/closing exact replaced with terminal simp.|
|1.5 trailing rfl|n/a, no trailing rfl.|
|1.6 anonymous constructor|n/a, equality proof has no constructor pair.|
|1.7 apply+exact|n/a, none.|
|1.8 by_contra!|n/a, no contradiction.|
|1.9 eta lambda|Original lambda proves a sum-congruence equality and is not eta-reducible; removed completely by simplification.|
|1.10 single-use have|n/a, zero have.|
|1.11 refine+fun|n/a, no apply/intro sequence.|
|1.12 redundant show|n/a, none.|
|1.13 obtain projections|n/a, no conjunction/projections.|
|1.14 merge rw|n/a, original rw calls live in separate nested goals; now removed.|
|1.15 terminal simp unsqueeze|Final mul_X terminal simp uses contextual lemmas; original simp only was nonterminal, so not blindly unsqueezed.|
|1.16 nonterminal simp squeeze|n/a after replacement: all three simp calls terminal.|
|1.17 dot notation|n/a, no surviving suitable explicit namespace application.|
|1.18 use <\||n/a, no trailing parenthesized proof term.|
|1.19 push Not|n/a, no push_neg.|
|1.20 existential inline|n/a, no private existential helper.|
|2.1 grind whole proof|Actual native trial failed on derivative chain-rule goal.|
|2.2 remove pre-grind|n/a, no retained grind.|
|2.3 simpa consolidation|Terminal simp closes multiplication case directly; no using-term needed.|
|2.4 fun_prop|n/a, formal polynomial derivative equality rather than analytic function property.|
|2.5 positivity|n/a, no positivity/nonzero goal.|
|2.6 gcongr|n/a, no ordered monotonicity goal.|
|2.7 lia/omega|n/a, no Nat/Int arithmetic goal.|
|2.8 aesop|Actual native whole-goal trial failed.|
|2.9 norm_num/norm_cast|n/a, no concrete numeric/cast goal.|
|2.10 decide|n/a, arbitrary polynomials over generic field, no closed decidable computation.|
|2.11 field_simp;ring|n/a, no denominator.|
|2.12 linear_combination|Original ring tail solved a pure product rearrangement after hp had already rewritten derivative; final proof eliminates this goal using simp associativity/commutativity, so no ring/hypothesis stage remains.|
|2.13 wlog|n/a, three distinct inductive constructors rather than symmetric cases.|
|2.14 calc term|n/a, no calc.|
|2.15 <;> goals|n/a, each constructor uses different facts; no identical branch tactic.|
|3.1 erw→rw|n/a, no erw.|
|3.2 legacy function tactic|n/a, no continuity/measurability.|
|3.3 omega→lia|n/a, no arithmetic tactic.|
|3.4 rcases rfl|n/a, no rcases.|
|3.5 register automation|No attribute added: chain-rule RHS duplicates γ/P across a finite sum; ordinary applied theorem is the intended rewrite API.|
|3.6 simp_all|n/a, no simp_all only; existing hp-based simp closes branch directly.|
|3.7 option removal|n/a, none present.|

## Step 4 — reflection

One-tactic simp/grind/aesop and direct exact?/apply? trials did not prove the whole theorem. Induction on C/add/mul_X is the natural free-algebra argument. The final mul_X proof uses existing simplification rules plus finite-sum linearity and commutative multiplication; it removes six manual lines in favour of two. Constructing generic derivations would introduce scalar-action plumbing absent here and is not a shorter proof. No extra abstraction, definition, helper, or deferred task is needed.

## Step 5 — verification and gates

Complete native `lean_diagnostic_messages` immediately after final edit: success=true, partial=false, timed_out=false, failed_dependencies=[], zero errors, zero target warnings; all five outside warnings listed above. Actual `/Users/ramin/.elan/bin/lake build Roth.GenWronskian` session75879 exit0, target built in17s; warning set unchanged.

Independent `/private/tmp/roth-d11-independent.lean`, session98233 exit0: imports built current module only after module build finished; checks exact original public type against @Roth.derivative_aeval and re-proves original baseline theorem independently using original induction proof, without citing target. `#print axioms` for both target and independent theorem returns precisely propext, Classical.choice, Quot.sound. Generic semiring proof independently compiles with the same axiom set. No sorry/new axiom/native_decide/limit raise introduced.

Worker snapshot `/private/tmp/roth-d11-start.lean`; direct diff shows exactly the mul_X branch replacement and nothing outside target. Source ownership revoked after freeze; all later work isolated/report-only.

| Gate | Result | Evidence |
|---|---|---|
|lake_build_file|pass|session75879 exit0, Roth.GenWronskian|
|definition_protected|pass|no definition/abbrev change|
|theorem_statement_protected|pass|all original signature lines byte-identical; independent original-type compile|
|structure_gate|pass|7 proof lines, no conjunction, 2-line largest branch|
|naming_gate|pass|descriptive derivative_aeval, no forbidden pattern|
|line_packing_gate|pass|three measured rows, no repack rows|
|inequality_orientation_gate|pass|zero reversed order tokens|

Overall: pass. Broader full build and separate LeanEval belong to file owner and were not run by worker.

## Step 6 — result and checklist

Before14 / after10 declaration lines, saved4; proof11→7. Issues3/fixed3/deferred0. Applied proof consolidation (1.4/2.3) and removal of redundant manual branch; no renames queued. Comments preserved: existing docstring preserved, no proof comments present. Refactoring needed: none.

- [✓] Step 1 — references read.
- [✓] Step 2 — all24 audit items recorded.
- [✓] Step 2.5 — five actual search methods recorded.
- [✓] Step 2.6 — every actual parameter, mechanical tests, public literature recorded.
- [✓] Step 2.7 — per-line codepoint width table.
- [✓] Step 2.8 — inequality scan.
- [✓] Step 3 — all42 rules have status.
- [✓] Step 4 — holistic proof reflection.
- [✓] Step 5a — complete successful LSP, unchanged outside warnings.
- [✓] Step 5b — actual module build, protected diff, independent type/reproof/axioms.
- [✓] Step 6a — renames none; no shared sidecar writes.

### Search audit supplement

Untruncated full-name `rg -n 'derivative_aeval' .lake/packages/mathlib/Mathlib` returned no source hits; companion sum/pderiv search returned precisely the special sum-elimination/renaming API noted above. This source-text observation is supplemented by the failed native exact? probe and does not treat the warming local index as absence.

Repeated broad literature query's first three returned hits, captured in order: [Generalizations of the derivative](https://en.wikipedia.org/wiki/Generalizations_of_the_derivative), [P-adic Expansions and Approximations](https://www.csd.uwo.ca/~mmorenom/AM583/Lectures/Newton2Hensel.html/node17.html), [Algebraic proof of the chain rule?](https://math.stackexchange.com/questions/2104068/algebraic-proof-of-the-chain-rule). These are search records only; the generality conclusion is certified by the semiring scratch and supported by the primary mathematical notes/Stacks references above. Combined domain-query first three returned hits were nLab chain rule, total derivative, derivation, as listed above. The final targeted query first three were the Stacks index, the regularity/derivations mirror, and [Pinkham, Analysis, Convexity, and Optimization](https://www.math.columbia.edu/department/pinkham/Optimizationbook.pdf); none supplies a closer API replacement.
