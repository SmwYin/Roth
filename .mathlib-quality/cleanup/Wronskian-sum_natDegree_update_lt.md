# Declaration audit: `Roth.sum_natDegree_update_lt`

Dedicated Phase-4 worker C13, baseline `0182ccd`. Original inventory lines224–246;
worker baseline lines194–216; final lines194–212. Declaration23→19 lines, proof18→15.
The proof cancels equal leading terms, uses independence to exclude a zero result,
and makes one summand strictly smaller while leaving every other summand unchanged.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md. The declaration contract, applicable
style/naming rules, and Lean4 statement/docstring protection rules were consulted.
Existing public statement, argument order, docstring, imports and toolchain are preserved.

## Full audit

1. **LINT:** no warning in this declaration. Complete-file diagnostics retain only the
   previously recorded missing copyright header and coefficient theorem's unused hφ/hd.
2. **HAVE SCAN:** baseline `a` is a `set`, not a have; retained because the quotient is
   used throughout the argument. `h0 := hφ.ne_zero`, no by, used at ν and ν' in five
   places, retained. `hlc := leadingCoeff_ne_zero.2 (h0 ν)`, no by, used in quotient
   nonzeroness and cancellation, retained. `ha := div_ne_zero ...`, no by, used once
   in degree_C_mul, inlined. `hne := fun h' ↦ ... by ...` contains a substantive span
   proof, used once; replaced by a two-line proof using independence of the updated
   family, retained as a proof-bearing have. `hdeg' := by rw ...`, used once, retained
   as the degree comparison proof. `hlt := natDegree_lt_natDegree ...`, no outer by
   but has a nested leading-coefficient proof, used twice (strict witness and weak
   pointwise bound); retained. No single-use proof-free have remains.
3. **SET_OPTION:** none in source; no heartbeat/recursion/instance limits introduced.
4. **SIMP SQUEEZE:** baseline had no simp. All final simpa/simp calls close their goals:
   hne, strict witness, positive update branch and negative update branch. No nonterminal
   bare simp or squeezed terminal simp remains.
5. **NAMING:** sum_natDegree_update_lt names the total-degree decrease of an updated
   family, retaining the API token natDegree. No forbidden numbered pattern, abbreviation,
   single-letter public name, or reverse-order relation suffix. No rename queued.
6. **LINE PACKING:** hypothesis/conclusion start combined; measured tables below.
7. **BY PLACEMENT:** every by is attached to the preceding expression.
8. **FORMAT:** two-space proof indentation, four-space signature continuation plus
   expression nesting, no internal empty lines or semicolon chains. Lambda => changed
   to ↦; no haveI/letI. Adjacent rewrites already merged.
9. **COMMENTS:** all five existing docstring lines byte-identical; no proof comments
   existed, none deleted. Mathematical explanation retained.
10. **DOCSTRING:** existing public documentation explains leading-term cancellation,
    the descent role, and why the difference is nonzero; preserved as requested.
11. **VISIBILITY:** public API preserved under the user's contract; used in the next
    Wronskian theorem and named in implementation notes. No visibility change proposed.
12. **STRUCTURE:** final15-line body, not one of the three named Main results, no
    conjunction conclusion, two one-line branches. No decomposition needed.
13. **MATHLIB:** five-method evidence below. Existing degree_sub_lt_left is the right
    cancellation lemma; reuse the already-cleaned updated-independence theorem for hne.
    No custom predicate or new wrapper added.
14. **JUNK DEF:** n/a: theorem; local scalar abbreviation is multiply used.
15. **EXISTS LEMMA:** n/a: no private existential wrapper.
16. **SHOW/CHANGE:** neither appears.
17. **PUSH_NEG:** none.
18. **GENERALISE:** hypothesis-by-hypothesis audit and actual compiler probes below;
    no signature change or companion API added.
19. **INEQUALITY:** per-occurrence scan below; all inequalities use < or ≤.
20. **NORMAL FORM:** Function.update plus a finite sum of natDegree is the direct
    descent measure used by strong induction. Scalar polynomial is canonically C a * p;
    no alternate equivalence API needed.
21. **SYNTAX-GEN:** current family/indices/equal-degree hypotheses match the only call
    site. A two-polynomial helper or arbitrary finite index restatement adds abstraction
    without a demonstrated caller benefit; no proposal to change this API.
22. **IMPORT-FANOUT:** n/a: no import changes.
23. **CASTS:** 0 dropped,0 cross-type coercions added,0 new load-bearing ascriptions.
    Existing K[X] and Fin l parameter types are unchanged.
24. **INSTANCE-NAME:** n/a: theorem introduces no instance.

Issues fixed: (1) one-use ha binding, (2) manual span contradiction duplicating available
updated-independence consequence, (3) statement underpacking, (4) lambda syntax and
verbose pointwise comparison. No unresolved declaration-local issue or refactoring flag.

## Line packing

The first syntactic unit of the next line is treated as a binder or complete expression
operand (not a detached punctuation character). Widths are Unicode codepoints.

Baseline:

| Line | Width | Next signature unit | Arithmetic | Action |
|---|---:|---|---|---|
|194|94|`(h : ν ≠ ν')` (12)|94+1+12=107|ok|
|195|62|`∑ ρ, (Function.update φ ν'` (26)|62+1+26=89|repack|
|196|30|polynomial update argument/application (72)|30+1+72=103|ok|
|197|80|`< ∑ ρ, (φ ρ).natDegree := by` (28)|80+1+28=109|ok|
|198|34|none|n/a|ok|

Final:

| Line | Width | Next signature unit | Arithmetic | Action |
|---|---:|---|---|---|
|194|94|`(h : ν ≠ ν')` (12)|94+1+12=107|ok|
|195|89|polynomial update argument/application (72)|89+1+72=162|ok|
|196|78|`< ∑ ρ, (φ ρ).natDegree := by` (28)|78+1+28=107|ok|
|197|34|none|n/a|ok|

Actual `#check @Roth.sum_natDegree_update_lt`, `format.width := 100`:

```lean
@Roth.sum_natDegree_update_lt : ∀ {K : Type u_1} [inst : Field K] {l : ℕ} {φ : Fin l → Polynomial K},
  LinearIndependent K φ →
    ∀ {ν ν' : Fin l},
      ν ≠ ν' →
        (φ ν).natDegree = (φ ν').natDegree →
          ∑ ρ,
              (Function.update φ ν' (φ ν' - Polynomial.C ((φ ν').leadingCoeff / (φ ν).leadingCoeff) * φ ν)
                  ρ).natDegree <
            ∑ ρ, (φ ρ).natDegree
```

## Inequality scan

| Occurrence | Relation | Disposition |
|---|---|---|
|Final L197, conclusion|updated degree sum < original sum|canonical smaller-left|
|Final L206, hlt type|difference natDegree < original natDegree|canonical smaller-left|
|Final L211, inferred hlt.le target|difference natDegree ≤ original natDegree|canonical smaller-left|
|Final L212, inferred unchanged-entry target|same natDegree ≤ itself|canonical smaller-left|
|Theorem name|`_lt`|canonical; no rename|

No ≥ or > remains anywhere in the target code; the != conditions use ≠, not order.

## Five-method search status

- **A Lean-Finder:** query “Polynomial same degree leading coefficient cancel subtraction
  smaller degree”; returned Polynomial.degree_sub_lt (older index alias), cancelLeads,
  natDegree_cancelLeads_lt_of_natDegree_le_natDegree. Local current source verifies
  degree_sub_lt_left; cancelLeads changes the expression and needs additional API.
- **B Loogle:** `Polynomial.degree (_ - _) < _`; returned degree_sub_lt_left/right,
  deprecated degree_sub_lt, div_wf_lemma, Matrix.charpoly_sub_diagonal_degree_lt.
- **C LeanSearch:** unavailable: parent/file workers established persistent HTTP500;
  not retried or counted as evidence of absence.
- **D Source:** untruncated rg over Algebra/Polynomial for degree/natDegree subtraction
  and the exact target name; found Degree/Defs.lean:543 degree_sub_lt_left and
  Operations.lean natDegree_sub_eq_left/right_of_natDegree_lt. Target name occurs only
  in project. Searched sum_update/update_comp in BigOperators and Function files;
  no direct replacement was established.
- **E Local name search:** natDegree_sub produced10 relevant source hits, including
  natDegree_sub_le and IsMonicOfDegree.natDegree_sub_lt; semantic index unavailable,
  so no absence inference. Actual #check confirms degree_sub_lt_left and
  Roth.linearIndependent_update_sub_smul, and isolated compilation confirms use.

Whole-goal exact? did not close; apply? emitted only partial suggestions, not a verified
replacement. No claim that the theorem is absent from all of mathlib. This preserves the
existing API, adding no potentially duplicate lemma.

## Generalisation status

| Hypothesis/parameter | Mechanical candidates considered/tested | Result |
|---|---|---|
|K : Type*|drop/universe generalisation|already universe-polymorphic; needed by polynomial/scalar type|
|Field K|DivisionRing; remove division or ring structure|actual DivisionRing candidate fails synthesizing Field K at updated-independence reuse; current proof kept. CommRing alone does not supply the division expression; semiring lacks subtraction. No claim Field is mathematically minimal|
|l : ℕ|drop/arbitrary finite index|l occurs in Fin l; arbitrary Fintype restates public API, no current caller benefit|
|φ : Fin l → K[X]|drop/structure value|needed in every term, no extra concrete named object to abstract|
|hφ : LinearIndependent K φ|drop; localise to relevant pair|compiled drop fails unknown hφ.ne_zero/hφ; used for original and updated nonzeroness. Pair-local hypothesis would change call signature; no needed companion|
|ν,ν' : Fin l|drop|both determine updated entry and cancelling column; statement becomes unbound|
|h : ν ≠ ν'|drop; strict→weak|compiled drop fails at updated-independence call; removing distinction permits self-cancellation, which need not strictly decrease natDegree of a constant|
|hdeg : equal natDegrees|drop; equality→one inequality|compiled drop fails at degree comparison rewrite. One-sided degree comparison does not ensure leading terms cancel: unequal degrees can leave the old degree unchanged|

Drop probes: `/private/tmp/wronskian-c13-drops.lean`, exit1 with the expected unknown
hypothesis errors. DivisionRing probe exit1, Field-instance error. None applied to source.
No analysis, topology, monotonicity, bijectivity, decidability or positive-bound hypotheses
are present. No class/drop weakening verified clean. Inversion check: no concrete named
construction disappears after unfolding; the argument uses polynomial degree and leading
coefficients throughout. General finite-sum monotonicity is already Finset.sum_lt_sum.
Big-change candidates: none warranted for the current callers.

## Literature search

Web query: “Wronskian polynomials distinct degrees elementary column operations leading
coefficients generalized field”. Top3 results:

1. [Comment. Math. Helv.86(2011),609–657](https://ems.press/content/serial-article-files/43265):
   equal degrees eliminated by elementary column operations.
2. [On linear equations with general polynomial solutions](https://www.sciencedirect.com/science/article/pii/S0022039618300044):
   generalized Wronskians and polynomial degree bounds.
3. [Bostan–Dumas, Wronskians and Linear Independence](https://mathexp.eu/dumas/publications/Bostan_Dumas_2010_WLI.pdf):
   column-echelon elimination for linearly independent families over a field, with a
   distinct-order power-series analogue.

The search supports the elimination interpretation; the power-series analogue concerns
order instead of this descending natural-degree measure and is not a drop-in weakening.
No literature-driven public API change needed. ChatGPT math MCP: not available among tools.

## Golfing rule pass

### Phase1

- [1.1] n/a: no by-exact wrapper.
- [1.2] n/a: no by-rfl block.
- [1.3] applied via simpa [hi] using hlt.le instead of rw then exact in pointwise branch.
- [1.4] n/a: no simp followed by exact; new simpa expressions directly close goals.
- [1.5] n/a: no trailing rfl.
- [1.6] n/a: no constructor/exact pair.
- [1.7] n/a: no apply/exact pair.
- [1.8] n/a: no contradiction/push_neg pair after reusing independence.
- [1.9] n/a: remaining lambda supplies a proof hole, not eta-reducible; syntax changed to ↦.
- [1.10] applied: one-use ha inlined; every retained proof-free have has multiple uses.
- [1.11] n/a: no apply/intro.
- [1.12] n/a: no show.
- [1.13] n/a: no projected conjunction have.
- [1.14] n/a: no consecutive separate rw calls.
- [1.15] n/a: no terminal simp only; new terminal simp stays unsqueezed.
- [1.16] n/a: all simp/simpa terminal.
- [1.17] applied: `(linearIndependent_update_sub_smul h a hφ).ne_zero ν'`; hlt.le retained.
- [1.18] n/a: no added removable function-argument parentheses; rw expressions require their grouping.
- [1.19] n/a: no push_neg.
- [1.20] n/a: no existential helper.

### Phase2

- [2.1] whole-proof grind actually tried, failed to derive polynomial degree descent.
- [2.2] n/a: no retained grind.
- [2.3] applied: hne from updated-family independence, strict witness by simpa, pointwise bound by simpa.
- [2.4] n/a: no analytic function-property goal.
- [2.5] positivity local attempt recorded below; structural positivity does not supply degree cancellation.
- [2.6] gcongr local attempt recorded below; explicit hlt.le is already direct.
- [2.7] local simp-only then lia attempt recorded below; no omega retained.
- [2.8] whole-proof aesop actually tried; exhaustive search failed to prove descent.
- [2.9] n/a: no concrete numeral or cross-type cast arithmetic.
- [2.10] n/a: arbitrary field/family is not a finite computable decision.
- [2.11] n/a: cancellation identity is exactly div_mul_cancel₀; no residual rational polynomial identity.
- [2.12] n/a: no ring/ring_nf ending with hypotheses.
- [2.13] n/a: update-self and update-other branches are not symmetric mathematical cases.
- [2.14] n/a: no calc chain.
- [2.15] tried by_cases <;> simp_all in isolated candidate; fails on the strict-to-weak
  natDegree inequality, so kept two distinct direct closing proofs.

### Phase3

- [3.1] n/a: no erw.
- [3.2] n/a: no continuity/measurability tactics.
- [3.3] n/a: no omega; lia considered under2.7.
- [3.4] original rfl substitution needed no later substitution; replaced split with by_cases
  to use terminal simpa [hi] directly.
- [3.5] n/a: specific descent theorem needs explicit family/equal-degree assumptions;
  no automation attribute needed by the existing caller.
- [3.6] simp_all tried as a closing tactic, failed to infer the needed weak inequality.
- [3.7] n/a: no maxHeartbeats option.

## Step-back reflection and experiments

Native whole-proof multi-attempt stalled and was terminated; bounded direct MCP fallback
returned complete results. grind, simp_all, aesop, exact? do not establish the descent;
apply? supplies partial unrelated order reductions, not a successful complete proof.
One isolated alternative `<;> simp_all` failed on hlt.le; the explicit branch candidate
compiled (exit0). The chosen strategy reuses linear independence, proves degree cancellation
with canonical polynomial API, and directly applies finite-sum strict comparison. Further
term inlining of hdeg'/hne would hide the mathematical stages without removing work.

Scratch experiments were outside the repository. No sorry, admit, new axiom, native_decide,
new import, source instrumentation, option, placeholder or altered definition remains.

## Verification and gates

- `/Users/ramin/.elan/bin/lake build Roth.Wronskian`: exit0,1826jobs, target9.6s;
  `/private/tmp/wronskian-c13-module.log`.
- Complete-file lean_diagnostic_messages via bounded direct MCP:
  success=true, partial=false, timed_out=false, no errors or failed dependencies;
  `/private/tmp/wronskian-c13-lsp.json`. Only the three previously recorded warnings.
- `/Users/ramin/.elan/bin/lake env lean /private/tmp/wronskian-c13-check.lean`: exit0.
  Contains independent copied proof, #check of target and new reused theorem, and axiom
  checks. Both target and isolatedProof depend only on propext, Classical.choice, Quot.sound.
- Scripted comparison: theorem signature identical after whitespace removal; all existing
  docstrings byte-identical; all source lines ≤100codepoints; changes only within target.
- Full project build and separate Roth.LeanEval build belong to the parent checkpoint and
  are intentionally not claimed before the parent reports them.

| Gate | Result | Evidence |
|---|---|---|
|lake_build_file|pass|actual module command exit0|
|definition_protected|pass|no def/abbrev or other declaration changed|
|theorem_statement_protected|pass|identical tokens, whitespace-only repack|
|structure_gate|pass|15-line body, no ∧, both branches one line|
|naming_gate|pass|descriptive mathematical name, no forbidden pattern|
|line_packing_gate|pass|all4final signature lines measured, no remaining repack|
|inequality_orientation_gate|pass|scan table; zero ≥/>|

Overall: pass. Renames queued: none. Refactoring needed: none.

## Phase checklist

- [x] Step1 references read.
- [x] Step2 all24audit items answered.
- [x] Step2.5 five-method search status and compiled lemma verification.
- [x] Step2.6 generalisation/drop tests/literature/inversion status.
- [x] Step2.7 per-signature-line width tables.
- [x] Step2.8 per-occurrence inequality scan.
- [x] Step3 all42golfing rules addressed.
- [x] Step4 alternate strategies and real bounded experiments.
- [x] Step5a complete LSP diagnostics, no errors.
- [x] Step5b diff gates, module, isolated proof/type/axioms.
- [x] Step6a no rename needed.

Source ownership frozen after module/LSP gates; remaining work is report-only.

Local automation result (`/private/tmp/wronskian-c13-local.json`, complete tool response):
`simp only [hi, Function.update_self]; lia` discharged the positive branch but left the
negative branch open in the multi-attempt snapshot; it is longer than the retained one-line
`simpa [hi] using hlt.le`. `gcongr` made no progress; `positivity` reported “not a positivity
goal”. Thus no further source edit is warranted. The direct MCP process emitted an async
transport cleanup warning after delivering complete results; this is not a Lean proof error.
