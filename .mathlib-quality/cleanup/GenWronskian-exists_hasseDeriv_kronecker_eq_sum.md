# `exists_hasseDeriv_kronecker_eq_sum` — Phase 4

Result: **10 → 8 declaration lines**, proof body **6 → 5**. Public statement tokens,
documentation, uniform witnesses, degree certificate, and all surrounding source are unchanged.
Only signature whitespace and the proof changed. Start snapshot:
`/private/tmp/roth-d17-before.lean`; frozen source SHA256:
`c99367130f26ea52ba6f1a375afba046a79d3231c4f66722875209be3fbf0a8c`.
Source ownership was explicitly revoked after the verified freeze; subsequent work is report-only.

## Step 1 — references and context

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md. Both installed SKILL.md files, the full worker
contract, relevant style-rules sections, naming-conventions, mathlib-review-stages, the initial
GenWronskian audit, source context, and clean.tex §2's uniform-expansion argument were read.
Native LSP was available; no fallback server was required. Tool metadata was discovered through
ALL_TOOLS. No mathematical ChatGPT MCP appears in that inventory.

## Step 2 — full audit (original lines 206–215)

1. **LINT:** no warning in this declaration. Complete final diagnostics have five inherited
   warnings elsewhere: header; two Fintype warnings on the dependent-Wronskian theorem;
   DecidableEq on det_sum_rows; Fintype on the final existence theorem.
2. **HAVE SCAN:** no have declarations. The obtain destructuring is used to retain the coefficient
   function, support certificate, and function equality.
3. **SET_OPTION:** none; no limit increases introduced.
4. **SIMP SQUEEZE:** original proof had no simp. Final simpa is terminal, explicitly unfolds only
   linearCombination_apply, Finsupp.sum, and kronHasse; no nonterminal bare simp remains.
5. **NAMING:** existential conclusion, subject hasseDeriv/kronecker, operation eq_sum; no forbidden
   abbreviation, numbered scheme, single-letter public name, _ge_, or _gt_ pattern. No rename.
6. **LINE PACKING:** repacked all four original signature lines into three; measured table below.
7. **BY PLACEMENT:** by ends final signature line.
8. **FORMAT:** two-space proof indentation, no blank body lines, one tactic per line, lambda ↦;
   no haveI/letI. Removed redundant lambda around hc.
9. **COMMENTS:** no inline proof comments existed; complete adjacent docstring preserved.
10. **DOCSTRING:** existing detailed public docstring gives source and factorial-normalization
    context. Preserved under the explicit documentation-preservation instruction.
11. **VISIBILITY:** retained public domain API; used by exists_genWronskian_ne_zero at L251.
12. **STRUCTURE:** five body lines, no branches. The conjunction certifies the *same* existential
    support used by a polynomial-independent coefficient family. Splitting or moving ∀P before
    the witnesses changes the useful packaging; explicit task instruction requires this exact
    conjunction. No helper extraction is useful for a five-line proof. This explicit scope
    exception takes precedence over the generic no-conjunction heuristic.
13. **MATHLIB:** five actual methods below found the existing generic finite-linear-combination
    API. Kept this public application theorem and used that API directly.
14. **JUNK DEF:** n/a, theorem rather than definition.
15. **EXISTS LEMMA:** not a trivial private witness wrapper: it exports a uniform differential
    operator expansion whose mathematical input is the preceding span-membership theorem.
16. **SHOW vs CHANGE:** neither present.
17. **PUSH_NEG:** none.
18. **GENERALISE:** every elaborated parameter examined below; no API changes applied.
19. **INEQUALITY:** degree certificate uses ≤; no reverse inequality occurrence, table below.
20. **NORMAL-FORM:** span membership is the generic intermediate form; finite support plus a
    global coefficient function is the required downstream existential form. Existing mathlib
    conversion is canonical; no new equivalence layer introduced.
21. **SYNTAX-GEN:** OK: ∃s,c precedes ∀P. Subtype coefficients from the alternative span API would
    require extension to all exponent vectors; keeping Finsupp supplies the global function
    immediately and preserves direct choose usage downstream.
22. **IMPORT-FANOUT:** n/a, no imports changed.
23. **CASTS:** zero dropped / zero cross-type / zero added load-bearing casts. Existing inferred
    coercion from c : exponent →₀ Polynomial K to a function remains essential to the witness.
24. **INSTANCE-NAME:** n/a, no instance declaration.

Issues fixed: underpacked signature; eta-expanded certificate/lambda arrow; manual rewrite/rfl
conversion replaced by terminal simpa. No refactoring or rename action remains.

## Step 2.5 — five-method mathlib search

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | membership in span of image iff finite sum coefficients supported in generating set | Finsupp.mem_span_image_iff_linearCombination; Submodule.mem_span_image_iff_exists_fun; Module.Basis.mem_span_image |
| B Loogle | Finsupp.linearCombination | linearCombination; range_linearCombination; linearCombination_range |
| C LeanSearch | membership in span image exists finite linear combination | mem_span_range_iff_exists_finsupp; mem_span_image_iff_linearCombination; Submodule.mem_span_image_iff_exists_fun |
| D source rg | mem_span_image_iff / linearCombination_apply / sum_apply | LinearCombination.lean L57,60,201,395–421; Supported.lean and LSum.lean matches |
| E native local name search | mem_span_image | both image-finset variants, Submodule image variant, Finsupp linearCombination variant, Basis and span variants |

Auxiliary variants inspected: linearCombination_apply_of_mem_supported;
Submodule.mem_span_image_iff_exists_fun; mem_span_image_finset_iff_exists_fun and its primed form;
mem_span_iff_exists_finset_subset. The first already uses the support; the subtype variants require
transport/extension of coefficients and do not shorten this public API conversion.
Common-equivalents table: no discrete/compact/bornology analogue applies.
Conclusion: **partial match found and used directly**, not a claim of mathlib absence.
The specialized differential span membership comes from the preceding audited private lemma.
No new wrapper, custom predicate, or helper was introduced. Public API preservation governs keeping
the existing named corollary; the proof uses the generic mathlib lemma at its actual call site.
Untruncated source search also checked the full public theorem name and Hasse composition/aeval
variants. No exact-name mathlib result was found; this alone is not treated as an absence proof.
Live exact? failed; apply? suggested only existential reshufflings, not a differential identity.

## Step 2.6 — parameter generalisation and inversion

| Parameter | Role/use | Mechanical candidates and outcome |
|---|---|---|
| {K : Type*} | coefficient type throughout both polynomial rings | Already universe-polymorphic; dropping changes the mathematical input or makes it autoimplicit; retained. |
| [Field K] | kronecker/hasseDeriv_kronecker_mem dependencies | DivisionRing loses CommSemiring required by MvPolynomial/aeval; CommRing loses field-dependent preceding API. IsField rebundling would restate the API. Prefix substitution probes reject the first two; no changes retained. |
| {σ : Type*} | variable/exponent index | Already universe-polymorphic, occurs in input and witnesses. Dropping or replacing changes type; no point-local or order weakening applies. |
| [Fintype σ] | enumeration in kronecker and preceding span theorem | Drop / Finite replacement tested in isolated prefix probes; the chosen equivFin construction needs a Fintype. Finite plus locally chosen enumeration changes the instance-dependent public expression, so not applied. |
| [CharZero K] | preceding hasseDeriv_kronecker_mem | Target-only drop probe fails at L212 with failed synthesis CharZero K. Mathematical characteristic-free coefficient-extraction proof is possible in the literature but requires different preceding API; explicitly closed as no-current-need by task scope. |
| (k : ℕ) | exponents of the named substitution | Appears in input and each summand. Dropping would change explicitness; abstracting the substitution is a public restatement. No strict bound is assumed, so k=0 and k=1 remain covered. |
| (μ : ℕ) | derivative order and support bound | Both occurrences essential. Not an arbitrary ordered index: Hasse derivatives are naturally indexed by ℕ. No strict→weak hypothesis exists. |

The unused section parameter l is absent from the elaborated theorem type (#check confirms).
There are no explicit proposition hypotheses to point-localise and no decidability assumptions to
drop; classical is local to the proof. Negative prefix probes are *dependency* tests, not claims
that the abstract mathematical results are false. Only the CharZero drop was additionally tested
with the full preceding source unchanged. Compiler-generated sorry placeholders in failing
scratch diagnostics are not source admissions and never entered the repository.

Inversion check: after hasseDeriv_kronecker_mem, the proof is generic span-to-finite-support
conversion. That abstract content already exists as Finsupp.mem_span_image_iff_linearCombination,
which is used directly. Extracting another generic helper would duplicate it. The original public
corollary is retained under API preservation; no new theorem/helper or API proposal is needed.

### Public literature search (three actual queries, top three returned results each)

1. Query: `Hasse derivative composition multivariate chain rule arbitrary characteristic generalization`.
   - [Ivey-Law thesis](https://www.maths.usyd.edu.au/u/PG/Theses/2012-ivey-law.pdf): multivariate
     Hasse derivatives and arbitrary-characteristic Taylor expansions; broader coefficient context.
   - [Hasse derivative overview](https://en.wikipedia.org/wiki/Hasse_derivative): search discovery
     result only; not relied on as primary technical evidence.
   - [Joints of Varieties](https://par.nsf.gov/servlets/purl/10337079): coefficient extraction over
     arbitrary fields; supports the distinction from factorial-dependent ordinary derivatives.
2. Query: `Kronecker substitution differential operators Wronskian Roth theorem`.
   - [Diophantine Approximation and the Subspace Theorem](https://pure.mpg.de/pubman/item/item_3634762_1/component/file_3634763/2502.00731.pdf):
     directly relevant Kronecker substitution/generalized Wronskian setting.
   - [Math 249A notes](https://www.ucl.ac.uk/~ucahpet/TransNotes.pdf): Roth/generalized Wronskian
     differential operators with bounded order; matches the downstream motivation.
   - [Rational approximations to solutions of linear differential equations](https://pmc.ncbi.nlm.nih.gov/articles/PMC384210/?page=1):
     Wronskian methods in differential approximation; adjacent, not the same uniform polynomial API.
3. Query: `Hasse Schmidt derivation chain rule higher derivatives polynomial substitution`.
   - [Hazewinkel](https://arxiv.org/abs/1110.6108): higher derivation algebra, more abstract than
     this fixed substitution; does not replace the local support witness conversion.
   - [Ivey-Law thesis](https://www.maths.usyd.edu.au/u/PG/Theses/2012-ivey-law.pdf): multivariate
     polynomial higher-derivation setting, consistent with the characteristic-free candidate.
   - [Algebraic independence over finite fields](https://citeseerx.ist.psu.edu/document?doi=2cc8db4c436d9e5f06085d50e5b3df38c5efe642&repid=rep1&type=pdf):
     higher-derivation product rules over finite fields; adjacent motivation, not this exact API.

Primary references additionally opened and compared:
[Maurischat](https://arxiv.org/abs/1611.01940) gives higher-derivation chain rules in arbitrary
characteristic; [Narváez-Macarro](https://arxiv.org/abs/1810.08075) studies substitution maps on
multivariate Hasse–Schmidt derivations over commutative algebras; [Vojta](https://math.berkeley.edu/~vojta/jets.pdf)
provides the general higher-derivation framework. These support a broader *mathematical* formulation,
but do not justify changing an instance-dependent public expression in this cleanup. Characteristic
and arbitrary-γ widening remain closed/no-current-need, not an unfulfilled refactoring task.
Math MCP: unavailable in discovered metadata, so no second-opinion result is claimed.

## Steps 2.7–2.8 — packing and inequalities

Original widths: 67,84,71,57. Final codepoint measurements include := by on the last line.
`set_option format.width 100` (not pp.width) was used for the compiled #check reference in
`/private/tmp/roth-d17-api.lean`; its exact output is in `/private/tmp/roth-d17-api.log`.

| Final signature line | Codepoints | Next complete syntactic token | Arithmetic | Action |
|---|---:|---|---|---|
| 206 | 91 | `(c : (σ →₀ ℕ) → Polynomial K),` (30) | 91+1+30=122 >100 | ok |
| 207 | 84 | `Polynomial.hasseDeriv μ (kronecker k P) =` (41) | 84+1+41=126 >100 | ok |
| 208 | 97 | no next signature line | n/a | ok |

| Occurrence | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| none | complete signature and hypotheses | zero ≥ / > | none; d.degree ≤ μ already oriented | none |

## Step 3 — all 42 golfing rules

| Rule | Concrete result |
|---|---|
| 1.1 by exact | n/a: obtain and witness construction require tactic context. |
| 1.2 by rfl | n/a: theorem is not reflexive. |
| 1.3 rw+exact | n/a: original closing step was rw+rfl; replaced by terminal simpa under 2.3. |
| 1.4 simp+exact | n/a: no original simp+exact pair. |
| 1.5 simp+rfl | n/a: original had rw+rfl, not simp+rfl. |
| 1.6 constructor | already anonymous existential/conjunction construction; retained. |
| 1.7 apply+exact | n/a: neither appears. |
| 1.8 contradiction | n/a: no contradiction argument. |
| 1.9 eta reduction | applied: fun d hd => hc hd replaced by hc; remaining P lambda is substantive. |
| 1.10 single-use have | n/a: no have. |
| 1.11 apply+intro | n/a: no such pair. |
| 1.12 show | n/a: no show. |
| 1.13 have projections | already obtain destructuring; no have projections. |
| 1.14 merge rw | n/a: single original rw list; no sequential rw pair. |
| 1.15 terminal simp only | n/a: none. |
| 1.16 nonterminal simp | n/a: none. |
| 1.17 dot notation | applied at use of hsum.symm rather than separate symmetry rewrite. |
| 1.18 <| | n/a: parenthesized .1 membership conversion needs its proof argument; no shorter trailing-parenthesis lambda. |
| 1.19 push Not | n/a: no push_neg. |
| 1.20 inline existential | n/a: protected public mathematical corollary, not trivial private witness packaging. |
| 2.1 grind | actually tried at whole-goal L209 and post-obtain L213; failed to construct the uniform support/function expansion. |
| 2.2 delete before grind | n/a: no grind retained. |
| 2.3 simpa | applied: evaluates congrFun hsum.symm P with linearCombination_apply, sum, kronHasse; removes manual rw/rfl. |
| 2.4 fun_prop | n/a: no analytic function-property goal. |
| 2.5 positivity | n/a: certificate is hc, no isolated positivity/nonzero goal. |
| 2.6 gcongr | n/a: no monotonicity calculation. |
| 2.7 lia/omega | n/a: no arithmetic subgoal; degree bounds copied directly from support membership. |
| 2.8 aesop | actually tried whole goal/post-obtain; exhaustive search left existential finite-support goals. |
| 2.9 norm_num/cast | n/a: no numeric or cast goal. |
| 2.10 decide | n/a: quantified polynomial identity is not finite computation. |
| 2.11 field_simp/ring | n/a: no denominator/ring normalization goal. |
| 2.12 linear_combination | n/a: no ring/ring_nf endpoint; this is module support conversion. |
| 2.13 wlog | n/a: no symmetric cases. |
| 2.14 calc | n/a: no calc. |
| 2.15 <;> | n/a: support certificate discharged directly; one substantive residual equality. |
| 3.1 erw | n/a: absent. |
| 3.2 legacy analytic tactics | n/a: absent. |
| 3.3 omega→lia | n/a: neither present, no arithmetic goal. |
| 3.4 rcases rfl | n/a: no substituting pattern. |
| 3.5 automation attributes | no attribute added: existential witness theorem is not a simp normal form. |
| 3.6 simp_all | n/a: no simp_all only; a direct equality is available. |
| 3.7 options | n/a: no limits/options in the declaration. |

## Step 4 — strategy reflection and actual attempts

Whole-goal grind, aesop, simp, and exact? were tried live; none supplies the specialized membership
input. Post-obtain exact? also fails; apply? only reshuffles existential binders. A term-mode
anonymous constructor succeeded in the multi-attempt test, but would require a longer nested by
and wrapping; the five-line proof exposes the mathematical steps more clearly. Two reduced simp
sets were actually tested: omitting kronHasse failed to match the applied operator; bare simpa
left the linearCombination term. The chosen three-lemma terminal simpa compiled. Multi-attempt
reports “No goals to be solved” in unchanged following tactics when the replacement already closes
the goal; final actual-source LSP and module compilation independently confirm success.

## Steps 5a–5b — verification and gates

`/Users/ramin/.elan/bin/lake build Roth.GenWronskian` exited **0**, session88422,
`/private/tmp/roth-d17-module.log`: Build completed successfully (1838 jobs).
Complete native lean_diagnostic_messages: **success=true, partial=false, timed_out=false,
errors=0, failed_dependencies=[]**; five inherited warnings outside the target, listed above.
Artifact: `/private/tmp/roth-d17-final-lsp.json`.
Owner additionally verified the frozen source with full build (152.96s) and separate LeanEval
(26.19s), both exit0 and hash-stable, as reported in the owner handoff.

Independent checks:

- `/private/tmp/roth-d17-api.lean` imports the actual built target and assigns it to the *original*
  full type, not a reflexive equality. Its compiled #print axioms returns exactly
  `[propext, Classical.choice, Quot.sound]`.
- `/private/tmp/roth-d17-independent.lean` contains the preceding snapshot and original proof under
  d17IndependentOriginalProof, without importing or using the target theorem. It compiles; its
  axioms are also exactly the standard three. Session51945 exited 0.
- Programmatic comparison confirms token-identical complete signature, identical prefix/suffix
  outside the target, declaration 10→8, no reverse inequality or admission/limit patterns.
- `git diff --check` exits 0. No commits, shared log edits, full builds, or helper edits by worker.
- All five dependency-weakening scratch probes completed with exit1 (session51528), as expected;
  target-only CharZero drop separately completed exit1 (session98612). Logs use the
  `/private/tmp/roth-d17-{dropchar,division,commring,finite,dropfinite}.log` names and
  `/private/tmp/roth-d17-dropchar-target.log`.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | actual module build exit0, log above |
| definition_protected | pass | no def/abbrev edits; entire out-of-target prefix/suffix identical |
| theorem_statement_protected | pass | full signature tokens identical; original-type assignment compiles |
| structure_gate | pass, explicit scope exception | 5-line body/no branches; degree conjunction required by task instruction |
| naming_gate | pass | descriptive name, no forbidden abbreviation/pattern |
| line_packing_gate | pass | complete final 3-row codepoint table, no repack rows |
| inequality_orientation_gate | pass | complete scan: zero ≥/>; existing ≤ retained |

Overall: **pass** under the explicit uniform-witness/conjunction preservation instruction.
Renames queued: none. Comments preserved: complete docstring, no inline comments originally.
Refactoring needed: **none**. Parent owns cumulative full-build/LeanEval gates after source freeze.

## Step 6 — completion checklist

- [✓] Step 1 — reference docs and complete contract read.
- [✓] Step 2 — all 24 audit items answered.
- [✓] Step 2.5 — five actual mathlib search methods and alternatives recorded.
- [✓] Step 2.6 — every parameter, inversion, public literature, unavailable math MCP recorded.
- [✓] Step 2.7 — every final signature line measured with arithmetic.
- [✓] Step 2.8 — complete inequality scan recorded.
- [✓] Step 3 — all 42 concrete rules answered.
- [✓] Step 4 — actual automation/API/alternative strategy attempts recorded.
- [✓] Step 5a — complete native LSP clean of errors, inherited warnings disclosed.
- [✓] Step 5b — actual module build and diff gates pass.
- [✓] Step 6a — naming clean, no rename entry needed.
