# Phase 4: Roth.abs_coeff_le_normOne

Scope: only this declaration in `Roth/CoeffNorm.lean`, originally L66–71, finally L66–68.
Before: 6 declaration lines; after: 3; saved: 3. Documentation unchanged (2 lines).
The four-line support case split is replaced by one direct Mathlib term.
No public signature, definition, instance, import, option, or other declaration changed.
Source frozen and ownership returned before final verification.
Frozen whole-file SHA256: `29e747bec2da1d802c9dea2a034b17dfe1db36b793f966b7007c46c3529e93bc`.
Frozen owned-block SHA256: `b54abca37528d37ec3deb57c9ce363b96df8ace01c715c45dbc170009e505731`.

## References and baseline

Read the full mathlib-quality and lean4 SKILL.md files, the complete worker contract,
and mathlib-quality references `golfing-rules.md`, `proof-patterns.md`,
`mathlib-search.md`, `generalisation-patterns.md`, `cleanup-gates.md`,
`style-rules.md` (including the separate read of its initially truncated middle),
and `naming-conventions.md`.
I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md.

Parent supplied the green whole-project and separate LeanEval baseline, session 67751 exit 0.
Fresh native complete-file diagnostics before editing: success=true, partial=false,
timed_out=false, no failed dependencies, zero errors and six existing outside warnings.
The target has no warning. The six warnings are the preserved header, four existing
DecidableEq arguments, and `hC`; their API decisions belong to the parent scope.

## Full 24-item audit

1. LINT: zero target warnings; six outside warnings retained, no suppression added.
2. HAVE SCAN: no `have` in either proof, so no single-use block exists to inline.
3. SET_OPTION: no local options; no heartbeat or recursion limit to remove.
4. SIMP SQUEEZE: original branch's `simp [...]` closes that branch. New `(by simp)`
   closes the zero-preservation side condition; no nonterminal simp needs squeezing.
5. NAMING: `abs_coeff_le_normOne` describes the bound, uses the actual API's normOne
   spelling, and matches no forbidden pattern or abbreviation; no rename queue entry.
6. LINE PACKING: complete measured signature table below; both rows pass.
7. BY PLACEMENT: original `by` was correctly placed; final proof is term mode.
8. FORMAT: 2-space term indentation; no empty interior lines, semicolon chains,
   haveI/letI, or trailing whitespace. Mathematical lambdas use `↦`.
9. COMMENTS: no inline comments present; both existing docstring lines preserved exactly.
10. DOCSTRING: existing public mathematical statement and source retained under Rule A.
11. VISIBILITY: reusable public coefficient API retained by explicit scope instruction.
12. STRUCTURE: final proof is one term; no conjunction or long branches remain.
13. MATHLIB: direct generic `Finsupp.single_eval_le_sum` found and compile-tested below.
14. JUNK DEF: n/a, theorem with no definition body to inline.
15. EXISTS LEMMA: n/a, no existential or private witness helper.
16. SHOW vs CHANGE: neither occurs, before or after.
17. PUSH_NEG: none occurs.
18. GENERALISE: all three parameters audited and mechanically drop-tested below.
19. INEQUALITY: the only relation is already `≤`; full scan below.
20. NORMAL-FORM: bound of an absolute coefficient by its ℓ¹ sum is canonical; no
    parallel equivalence lemmas introduced.
21. SYNTAX-GEN: OK; arbitrary coefficient index is directly available to callers.
22. IMPORT-FANOUT: n/a; the generic Finsupp lemma is already available through imports.
23. CASTS: 0 redundant body ascriptions retained, 1 cross-type cast retained (`z : ℝ`
    with z : ℤ), 0 other load-bearing body casts. The old body-local redundant
    `: ℤ` ascription disappeared with the case split. Signature ascriptions preserved.
24. INSTANCE-NAME: n/a; the declaration is a theorem and creates no instance.

Issues fixed: explicit case analysis duplicating Finsupp's existing nonnegative-sum API;
old mathematical lambda arrows replaced through the direct term.
Refactoring needed: none required within this declaration's scope. The generic Mathlib
result also supports eliminating local wrappers in a future cross-file API refactor;
deletion was not applied because this task explicitly preserves all public signatures.

## Five-method Mathlib search

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | absolute value of any coefficient bounded by sum absolute values coefficients multivariate polynomial | `Polynomial.le_gaussNorm` (sup/Gauss norm, different construction), `MvPolynomial.exists_degree_lt`, `ChevalleyThm.degBound` |
| B Loogle | `Finset.sum, _ ≤ _` | broad matches `Equiv.Perm.sum_comp`, `Equiv.Perm.sum_comp'`, `Int.natAbs_sum_le`; not the direct target |
| C LeanSearch | a term is bounded by sum of nonnegative terms even if outside support zero | `single_le_finsum`, `Summable.le_tsum`, `sum_le_hasSum` |
| D source rg | full name `abs_coeff_le_normOne`; `single_le_sum`, `single_eval_le_sum`, coefficient/norm and sum variants | full-name search empty; Data/Finsupp/Order.lean L154–169 supplies exact generic building block |
| E lean_local_search | `single_le_sum` | `Finsupp.single_le_sum`; index unavailable, so no absence inferred from the index |

Auxiliary variants: `single_eval_le_sum`, `single_le_sum`, `sum_le_sum`,
`sum_le_sum_index`, `coeff.*le.*sum`, `coeff.*norm`, `norm.*coeff`, Gauss norm.
Inspected MvPolynomial/Basic, coefficient-related source families, MonoidAlgebra/Defs,
Data/Finsupp/Order, and NumberTheory/Height/MvPolynomial. One guessed file
Analysis/Normed/MvPolynomial did not exist; rg --files located actual related files.
Common-equivalents table: no discrete/finite/separation/bornology bucket applies;
the relevant abstraction is a Finsupp nonnegative mapped sum.

Conclusion: found the general building block `Finsupp.single_eval_le_sum`, now used
directly. No claim of Mathlib absence. No new wrapper, predicate, helper, or import.
The existing public API is preserved as explicitly required by the task, overriding
the generic recommendation to delete wrapper declarations. Module documentation also
stays unchanged by that same instruction.

Compiled candidate evidence (native lean_run_code):

```lean
example (P : MvPolynomial σ ℤ) (d : σ →₀ ℕ) :
    |((P.coeff d : ℤ) : ℝ)| ≤ normOne P :=
  Finsupp.single_eval_le_sum P.coeff (g := fun z ↦ |(z : ℝ)|) (by simp) (fun _ ↦ abs_nonneg _) d
```

Result success=true, timed_out=false, diagnostics=[] before applying the source edit.
Deleting `(g := ...)` failed at the zero-preservation simp (underconstrained map).
Wrapping the direct term in `simpa using` failed because simplification obscured the
definitional relation of Finsupp.sum to normOne; the expected-type-directed term works.
Guessed `P.toFinsupp` and direct coercion to Finsupp failed; source inspection shows
AddMonoidAlgebra's actual field `coeff`, and `P.coeff` works.

## Generalisation status

The declaration has no proposition hypotheses, decidability parameters, algebraic
typeclass parameters, or bundled maps. All actual parameters are recorded here.

| # | Parameter | Class | Used as | Mechanical candidates actually tried | Verified | Result |
|---|---|---|---|---|---|---|
| 1 | `{σ : Type*}` | type variable | variable index for P and exponent d | drop under autoImplicit=false; inspect universe | yes | drop fails unknown σ; already universe-polymorphic; retained |
| 2 | `(P : MvPolynomial σ ℤ)` | structure value | coeff and normOne argument | drop under autoImplicit=false | yes | fails unknown P.coeff/P; retained |
| 3 | `(d : σ →₀ ℕ)` | structure value | selected coefficient index | drop under autoImplicit=false | yes | fails unknown d; retained |

Point-localisation and strict-to-weak are n/a for each row: these are an index type
and two mathematical values, not global analytic predicates or strict assumptions.
Typeclass parent weakening is n/a: none is declared. Universe weakening is already
maximal in `{σ : Type*}`. Dropping values cannot preserve the original statement.
No public unused argument was found, and no signature change applied.

Inversion check: fires positively as a sum-of-nonnegative-terms argument. The abstract
form is already in Mathlib, so no project helper should be added. Compiled probe:

```lean
example {α M N : Type*} [Zero M] [AddCommMonoid N] [PartialOrder N]
    [IsOrderedAddMonoid N] (f : α →₀ M) {g : M → N} (hg : g 0 = 0)
    (h : ∀ m, 0 ≤ g m) (a : α) : g (f a) ≤ f.sum (fun _ m ↦ g m) :=
  Finsupp.single_eval_le_sum f hg h a
```

Native lean_run_code success=true, diagnostics=[]; no extra generalisation is needed.
Big-change candidates: none required; the more general result already exists.

## Public literature search

Actual web queries and top three returned hits per query are recorded below. Search
results were screened for coefficient-vector norms versus norms of polynomial values;
they are discovery evidence, not imported proof authority.

| Query | Top three hits | Assessment |
|---|---|---|
| polynomial coefficient l1 norm coefficient bound generalization | PMLR *Sample Complexity of Dictionary Learning*; ECCC TR26-127; Technion dictionary-learning record | mostly irrelevant learning-theory hits |
| site.mathlib.org Finsupp single_eval_le_sum | gebner Mathlib3 Finsupp/basic; Mathlib3 Finsupp/defs; Mathlib4 Data/Finsupp/Basic | source-level generic lemma resolved locally instead |
| site.encyclopediaofmath.org lp sequence space norm | Encyclopedia *Lp spaces*; KIT functional-analysis lecture notes; Wikipedia Lp space | sequence-space abstraction, not special polynomial assumptions |
| site.terrytao.wordpress.com lp norms infinity 1 | Tao *247A Notes 1*; Tao *245B Notes 3*; Tao order-theory tag | general norms background |
| sequence norm sup sum site.math.mit.edu l1 linfty | MIT Functional Analysis Chapter 1; MIT non-classical polynomials; UCR supplementary Chapter 2 | no stronger coefficient-specific assumption needed |
| polynomial coefficient 1-norm bound generalization | ECCC TR26-127; ECCC TR09-136; *On Approximate Irreducibility of Polynomials* | coefficient norms occur more generally |
| polynomial f norm coefficients infinity 1 bound | Littlewood polynomials small L4 norm; TUM thesis; stability radius | distinguish function norms from coefficient norms |
| polynomial coefficient l1 norm bound generalization (quoted terms) | CausalSmith formalization; polynomial coefficient-updating paper; Kybernetika coercive polynomials | low-relevance hits |

Useful primary research hit from the broader results:
[*Counting Real Roots in Polynomial-Time via Diophantine Approximation*](https://pmc.ncbi.nlm.nih.gov/articles/PMC9707291/)
explicitly records the coefficient infinity norm bounded by the coefficient 1-norm
in its indexed search excerpt. Opening PMC itself returned a browser/reCAPTCHA page;
therefore the excerpt was not treated as a fully inspected paper.
The mathematical generalisation inferred here is finite-support nonnegative sum
domination; it is independently established by the compiled Mathlib generic probe.
ChatGPT mathematical MCP: n/a; metadata inventory contains no mathematical second-opinion
tool (ChatGPT Space tools are content tools, not this service).

## Line packing

`#check @Roth.abs_coeff_le_normOne` at `format.width := 100`:

```lean
@Roth.abs_coeff_le_normOne : ∀ {σ : Type u_1} (P : MvPolynomial σ ℤ) (d : σ →₀ ℕ), |↑(P.coeff d)| ≤ Roth.normOne P
```

This is Lean's actual diagnostic rendering; the source uses two lines to remain ≤100.
Widths measured as Unicode codepoints, not bytes. Before first line 66, following
whole conclusion-with-`by` 41: 66+1+41=108, so that existing break was justified.

| Signature line | Chars | Next signature unit | Arithmetic | Action |
|---|---:|---|---|---|
| 66 | 66 | `|((P.coeff d : ℤ) : ℝ)| ≤ normOne P :=` (38) | 66+1+38=105 >100 | ok |
| 67 | 42 | none, term proof next | n/a, signature ends | ok |

The proof term is 96 codepoints; no new line exceeds 100.

## Inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 1 | conclusion L67 | `|((P.coeff d : ℤ) : ℝ)| ≤ normOne P` | none, already canonical | none |
| 2 | all parameter types | no relation | n/a | none |

Forbidden `≥`/`>` signature occurrences: zero, both before and after.

## All 42 golfing rules

- [1.1] Applied: direct term eliminates the tactic wrapper.
- [1.2] n/a: no `by rfl`.
- [1.3] n/a: no rw/exact chain.
- [1.4] n/a: no simp/exact chain; direct lemma eliminates the case split.
- [1.5] n/a: no trailing rfl.
- [1.6] n/a: no constructor proof.
- [1.7] n/a: no apply/exact chain.
- [1.8] n/a: no contradiction or push_neg.
- [1.9] Lambdas normalised to ↦; neither surviving lambda is an eta-redex.
- [1.10] n/a: no have declarations.
- [1.11] n/a: no apply/intro chain.
- [1.12] n/a: no show annotations.
- [1.13] n/a: no projected conjunction hypotheses.
- [1.14] n/a: no rewrites.
- [1.15] n/a: no terminal simp only; new terminal simp stays bare.
- [1.16] n/a: no nonterminal simp.
- [1.17] Applied field notation P.coeff; no further dot-notation shortening helps.
- [1.18] n/a: final arguments follow `(by simp)`, so `<|` is not a useful replacement.
- [1.19] n/a: no push_neg.
- [1.20] n/a: no existential helper.
- [2.1] Tried grind [normOne] on the whole goal: failed, cannot derive sum domination.
- [2.2] n/a: retained proof has no grind or preparatory tactics.
- [2.3] Tried simpa using direct generic lemma: failed (definitional sum context); direct term succeeds.
- [2.4] n/a: no analytic function-property goal.
- [2.5] Tried positivity: reports not a positivity goal.
- [2.6] Tried gcongr: no progress on selected coefficient versus sum.
- [2.7] n/a: this is a real finite-sum bound, no Nat/Int arithmetic subgoal.
- [2.8] Tried aesop: failed, made no progress.
- [2.9] n/a: no numeric evaluation or cast-comparison subgoal.
- [2.10] n/a: symbolic real bound, no closed finite decision problem.
- [2.11] n/a: no denominator or algebraic identity.
- [2.12] n/a: no ring/ring_nf conclusion or linear combination of equality hypotheses.
- [2.13] n/a: support membership cases are not symmetric; the general lemma removes both.
- [2.14] Applied broader term-mode strategy via generic mapped-Finsupp sum theorem; no calc remains.
- [2.15] n/a: there are no repeated subgoals in the final term.
- [3.1] n/a: no erw.
- [3.2] n/a: no continuity or measurability tactic.
- [3.3] n/a: no omega or arithmetic goal.
- [3.4] n/a: no rcases/substitution.
- [3.5] No new automation attribute: a one-way bound is not a simplifying rewrite.
- [3.6] n/a: no simp_all only.
- [3.7] n/a: no raised limit exists.

Whole-goal simp [normOne] leaves the sum inequality unresolved; exact? failed to
close the original goal. apply? suggested abs_le, abs_le', and generic order routes,
all requiring unresolved subgoals; no direct simplification. Native multi_attempt
on a multiline branch spliced a continuation line into the candidate, yielding
extraneous-application diagnostics; full isolated lean_run_code subsequently tested
the real candidates. Explicit-f Finset branch works; deleting its f annotation
fails type inference. The selected direct Finsupp term compiles without that branch.

## Step-back reflection

The statement is a finite-support sum fact; the original proof manually reimplemented
its zero-outside-support case. Generic Finsupp API is the shortest robust proof.
Automation did not improve it, no `have` can fold, no helper extraction is justified,
and the single-term proof avoids both duplicated reasoning and extra imports.

## Verification and diff gates

Final `lake build Roth.CoeffNorm`: executed via `/Users/ramin/.elan/bin/lake`,
session 71860, exit 0, target built in 20 seconds, 1658 jobs. This was a module build,
not a new whole-project build. Six existing target-module warnings persisted; no
target declaration warning. Dependencies replayed their existing header warnings.

Final complete native lean_diagnostic_messages, after the edit and again after the
module build: success=true, partial=false, timed_out=false, failed_dependencies=[],
0 errors, 6 existing outside warnings, no target diagnostic.

Independent final source probe `/private/tmp/coeff-bound-final.lean` contains:
(1) an explicitly written original polymorphic type assigned the target theorem,
(2) an independent proof of the original statement by the original support split,
without referencing abs_coeff_le_normOne, and (3) #print axioms for both proofs.
First CLI probe session 99834 exited 0. Both axiom lists are exactly
`[propext, Classical.choice, Quot.sound]`; no sorry or custom axiom.
A fresh CLI run after module-build completion is recorded in the final addendum.
Some later isolated native tactic probes reported cached imports out of date;
the fresh CLI check avoids treating those cached imports as final evidence.

| Gate | Result | Actual evidence |
|---|---|---|
| lake_build_file | pass | lake build Roth.CoeffNorm, session 71860 exit 0 |
| definition_protected | pass | worker snapshot diff has no definition/abbreviation/instance/import edits |
| theorem_statement_protected | pass | both type lines unchanged except `:= by` becomes term `:=`; original-type example compiles |
| structure_gate | pass | 1 proof term, no conjunction or branches |
| naming_gate | pass | descriptive name, no forbidden abbreviation or pattern |
| line_packing_gate | pass | all signature rows measured above, no repack row |
| inequality_orientation_gate | pass | complete scan, zero forbidden signs |
| documentation_protected | pass | two docstring lines byte-identical |
| trust | pass | independent reproof and standard-axiom printout |

Overall: pass. Renames queued: none. No new axioms, sorry, suppressed warnings,
options, or source edits after the freeze notification.

## Required phase checklist

- [✓] Step 1 — reference documents read.
- [✓] Step 2 — full 24-item audit supplied.
- [✓] Step 2.5 — all five Mathlib search methods and actual results supplied.
- [✓] Step 2.6 — every parameter mechanically audited and actual candidate probes supplied.
- [✓] Step 2.7 — complete per-line codepoint width table supplied.
- [✓] Step 2.8 — inequality occurrence scan supplied.
- [✓] Step 3 — all 42 golfing rules given individual statuses.
- [✓] Step 4 — strategy reflection completed.
- [✓] Step 5a — complete final LSP diagnostics, zero errors.
- [✓] Step 5b — actual module build and full gate table supplied.
- [✓] Step 6a — no rename required or queued.

Final addendum: fresh post-build CLI probe
`/Users/ramin/.elan/bin/lake env lean /private/tmp/coeff-bound-final.lean`, session 33658,
exited 0. Original type assignment and the independent nonself reproof both compile;
both #print axioms outputs are `[propext, Classical.choice, Quot.sound]`.
Recomputed whole-file source SHA256 still equals the frozen
`29e747bec2da1d802c9dea2a034b17dfe1db36b793f966b7007c46c3529e93bc`.
The report has exactly eleven separate required `- [✓]` checklist rows.
