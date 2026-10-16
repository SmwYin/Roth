# Declaration cleanup: `Roth.wronskian_ne_zero_of_natDegree_injective`

Dedicated Phase-4 worker; baseline `edaf9aa`; declaration initially lines154–161, finally154–158.
Read lean4 and mathlib-quality skills, full golfing-rules, proof-patterns, mathlib-search,
generalisation-patterns, cleanup-gates and naming-conventions references, applicable style-rules
sections, and the full literal per-declaration contract. Existing public API/docstrings are protected.

## Mathematical reading

If the Wronskian were zero, its coefficient at the sum of degrees minus the derivative orders
would vanish. The coefficient identity and binomial determinant formula express this as a product
of nonzero leading coefficients, nonzero inverse factorials, and nonzero differences of distinct
degrees. Characteristic zero makes the casts injective. Simplification contradicts that product
being zero. The revised proof expresses this directly using the coefficient identity.

## Full audit (24 items)

1. **LINT:** no warning at this declaration. Complete final LSP has only preexisting missing
   copyright header and unused `hφ`/`hd` in the preceding coefficient theorem (lines127–128).
2. **HAVE SCAN:** initial L158 `have h1 := coeff_wronskian_of_natDegree_injective hφ hd`, no `by`;
   L159 rewrites it, L160–161 consume it. One mathematical consumer, with intermediate rewriting;
   inline into `simpa ... using ...`. No have remains.
3. **SET_OPTION:** none in source; width option only in isolated scratch code.
4. **SIMP SQUEEZE:** initial terminal `simp [...] at h1` and final terminal `simpa [...] using ...`
   remain unsqueezed. No nonterminal bare simp.
5. **NAMING:** `wronskian_ne_zero_of_natDegree_injective` states the conclusion and distinctive
   hypothesis, snake_case with the API identifier `natDegree`. No forbidden abbreviations,
   numerical labels, `_ge_`/`_gt_`, single-letter public name, or rename needed.
6. **LINE PACKING:** move `hφ` onto first signature line (exactly100 codepoints), combine `hd`
   and conclusion on second. Required before/after arithmetic below.
7. **BY PLACEMENT:** `by` remains on signature's last line.
8. **FORMAT:** two-space tactics, four-space signature continuation; `fun ν =>` becomes `fun ν ↦`;
   no empty lines, semicolon chains, haveI/letI, or trailing whitespace.
9. **COMMENTS:** no inline proof comments; complete four-line existing docstring preserved verbatim.
10. **DOCSTRING:** existing public description identifies characteristic zero and distinct degrees,
    with source reference; preserved under the user/API protection policy.
11. **VISIBILITY:** retained public: headline theorem named in module Main results and usable
    independently; local downstream caller `wronskian_ne_zero_of_linearIndependent` uses it.
12. **STRUCTURE:** headline theorem proof5→3 physical body lines, below15; no conjunction or branches.
13. **MATHLIB:** five-method search below; mathlib's two-polynomial Wronskian is only partial match.
    Keep this finite-family public theorem; use Finset product and factorial facts directly.
14. **JUNK DEF:** n/a: theorem, no new definition.
15. **EXISTS LEMMA:** n/a: neither private nor existential.
16. **SHOW vs CHANGE:** n/a: neither construct present.
17. **PUSH_NEG:** n/a: no negation-pushing tactic.
18. **GENERALISE:** all7 parameters checked below; no signature/API change adopted.
19. **INEQUALITY:** zero reversed inequalities in signature/hypotheses; table below.
20. **NORMAL-FORM:** `wronskian φ ≠ 0` and `Function.Injective` are direct standard propositions;
    no competing equivalence/normal-form API introduced.
21. **SYNTAX-GEN:** OK; pairwise-degree condition remains bundled as injectivity, directly consumed
    through `hd.eq_iff`. Switching to linear independence is the separate downstream theorem.
22. **IMPORT-FANOUT:** n/a: no new import.
23. **CASTS:** 1 redundant ascription dropped: `eq_comm (a := (0 : K))`→`eq_comm (a := 0)`.
    Complete isolated proof with this omission compiled. Zero new cross-type or load-bearing casts.
24. **INSTANCE-NAME:** n/a: no instance declaration.

Issues fixed: single-consumer have/rewrite chain, lambda syntax, signature packing, redundant
ascription. Refactoring needed: none for this declaration. The preceding coefficient theorem's
pending argument-removal proposal remains outside this worker's scope and its current call is kept.

## Mathlib search status

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | `Wronskian of nonzero polynomials with distinct degrees is nonzero` | Four hits: Polynomial.natDegree_wronskian_lt_add, degree_wronskian_lt_add, IsCoprime.wronskian_eq_zero_iff, Polynomial.wronskian_self_eq_zero; all concern two polynomials, not arbitrary finite families. |
| B Loogle | `"wronskian"` | Polynomial.wronskian and self/neg variants; no direct replacement in returned results. |
| C LeanSearch | `nonzero Wronskian polynomials pairwise distinct degrees` | HTTP500; unavailable, not evidence of absence; no repeated retry. |
| D Source | untruncated `rg` for exact target, wronskian theorem/lemma names, coeff_ne_zero/ne_zero_of_coeff in polynomial directories; prod_ne_zero source | Located `Mathlib/RingTheory/Polynomial/Wronskian.lean`, degree coefficient facts, Finset.prod_ne_zero_iff. Initial guessed Algebra/Polynomial/Wronskian path absent; corrected using rg --files. |
| E Local names | `wronskian`, limit12 | Returned project family API and mathlib binary API; index warming, so no absence inferred. |

Auxiliary variants checked: wronskian_eq_zero_iff, wronskian_self_eq_zero, wronskian_neg_left,
degree_wronskian_lt_add, natDegree_wronskian_lt_add, prod_eq_zero_iff/prod_ne_zero_iff,
leadingCoeff_ne_zero and coeff/support nonemptiness suggested by apply?. Common-equivalents table:
no disguised topology/finiteness/custom-predicate bucket.

Live predeclaration `exact?` failed to close; `apply?` supplied partial generic nonzero/support
routes but no complete proof. These checks avoid claiming absence merely from source search.
Conclusion: partial binary Wronskian match only; retain project finite-family theorem, build
on existing project coefficient/determinant results and direct mathlib product simplification.
This is not a wrapper around1–3 mathlib calls: its two principal mathematical inputs are project
finite-family results. No missing API extraction signal remains in the three-line proof.
The six replacement rules were checked: no matching declaration to delete, no new wrapper or
custom predicate, no new imports or replacement-driven module documentation changes.

## Generalisation status

All probes were isolated (no changes to repository statements). The failed probe batch returned
success=false, timed_out=false with the concrete diagnostics below.

| # | Parameter | Class/use | Candidate and evidence | Disposition |
|---|---|---|---|---|
| 1 | `{K : Type*}` | type variable; polynomial coefficient field | Already universe-polymorphic; removing K leaves coefficient type unbound. | Retain; no smaller universe restriction to remove. |
| 2 | `[Field K]` | typeclass; wronskian and det_choose_eq API | DivisionRing and CommRing+IsDomain scratch declarations each fail at `wronskian φ` with Polynomial type mismatch/required Field hierarchy. Dropping all structure would also leave polynomial operations unavailable. | No local weakening; would need coordinated definition/API refactoring, no current caller need. |
| 3 | `{l : ℕ}` | structure value; Fin index cardinality | Removing l leaves Fin l unbound; arbitrary finite indexing would restate wronskian derivative-row indexing. | Retain implicit natural cardinality. |
| 4 | `[CharZero K]` | typeclass; factorial/degrees casts and determinant evaluation | Dropped in a complete copy of current argument: simplification leaves binomial determinant=0, expected False. | Retain; not mechanically droppable. |
| 5 | `{φ : Fin l → K[X]}` | structure value; family in result | Removing φ leaves conclusion unbound; general power series require different named objects. | Retain implicit family. |
| 6 | `hφ : ∀ ν, φ ν ≠ 0` | proposition; leading coefficients nonzero | Drop and run exact?: failed to close. A singleton zero family illustrates why injectivity alone cannot suffice. Strict→weak catalogue doesn't apply to unordered field polynomial nonvanishing. | Retain. |
| 7 | `hd : Function.Injective ...natDegree` | proposition; pairwise factors nonzero | Drop and run exact?: failed to close. Repeated nonzero constant polynomials illustrate failure without distinction. LeftInverse adds data and is not a weakening. | Retain. |

No unused explicit hypothesis; both hφ and hd are also consumed by final simplification. No
point-localisation candidate: each family index/pair participates in a finite product. Inversion
check: the final algebraic contradiction is generic, but its crucial coefficient and determinant
identities are specific to Wronskians, and generic nonzero-coefficient/product APIs already exist.
No duplicate abstract lemma is warranted. Optional power-series/rational-function extensions
have no current caller need and are closed as out of this cleanup's scope, not pending work.

### Public literature

Web query `Wronskians linearly independent polynomials distinct degrees characteristic zero
Bostan Dumas` returned as its first three scholarly hits the arXiv record and two author-hosted
copies of Bostan–Dumas, *Wronskians and linear independence*:

- https://arxiv.org/abs/1301.6598
- https://specfun.inria.fr/bostan/publications/BoDu09.pdf
- https://mathexp.eu/dumas/publications/Bostan_Dumas_2010_WLI.pdf

Read the last author's PDF (Theorem2 and Lemma1). It extends the ordinary Wronskian criterion to
formal power series/rational functions over characteristic-zero fields and explains the
Vandermonde factor for monomials. Its positive-characteristic example1,x^p shows that simply
dropping characteristic zero fails. The present Hasse normalization agrees up to invertible
factorials in characteristic zero; extending to power series is a different API, not a local
proof cleanup. No concrete literature-driven change required here. Math ChatGPT MCP unavailable
in the exposed tool inventory; no result claimed from it.

## Required signature width tables

Actual `#check @Roth.wronskian_ne_zero_of_natDegree_injective` under `format.width100`:

```lean
@wronskian_ne_zero_of_natDegree_injective : ∀ {K : Type u_1} [inst : Field K] {l : ℕ} [CharZero K] {φ : Fin l → K[X]},
  (∀ (ν : Fin l), φ ν ≠ 0) → (Function.Injective fun ν ↦ (φ ν).natDegree) → wronskian φ ≠ 0
```

Before (codepoint counts, including indentation):

| Sig line | Chars | Next complete binder/conclusion | Arithmetic | Action |
|---|---:|---|---|---|
|154|80|`(hφ : ∀ ν, φ ν ≠ 0)`19|80+1+19=100≤100|repack|
|155|76|`wronskian φ ≠ 0 := by`21|76+1+21=98≤100|repack|
|156|25|none|n/a|ok|

After:

| Sig line | Chars | Next complete binder/conclusion | Arithmetic | Action |
|---|---:|---|---|---|
|154|100|`(hd : Function.Injective fun ν ↦ (φ ν).natDegree)`49|100+1+49=150>100|ok|
|155|77|none: conclusion and `:= by` included here|n/a|ok|

### Required inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
|1|signature and all hypotheses|n/a: no ≥ or > relation (initial => was a lambda token)|none|no _ge_/_gt_ in name|

## Golfing rule pass (all42)

| Rule | Status |
|---|---|
|1.1 by exact|n/a: no wrapper.|
|1.2 by rfl|n/a: no reflexivity proof.|
|1.3 rw+exact→rwa|n/a: original rewrite followed by simp at h1; consolidated using simpa instead.|
|1.4 simp+exact→simpa|Applied analogous simplification of input theorem directly in terminal simpa.|
|1.5 trailing rfl|n/a: absent.|
|1.6 constructor|n/a: no conjunction/data constructor.|
|1.7 apply+exact|n/a: absent.|
|1.8 by_contra!|n/a: direct intro of negated equality, no push_neg.|
|1.9 eta reduction|n/a: degree projection lambda is not an eta wrapper; arrow normalized.|
|1.10 single-use have|Applied: inline coefficient identity, eliminate h1 and its separate rw.|
|1.11 refine+fun|n/a: no apply/intro pair; direct intro followed by simp is clearer.|
|1.12 show|n/a: none.|
|1.13 have projections|n/a: no conjunction projections.|
|1.14 consecutive rw|n/a: one original rewrite, removed through simpa.|
|1.15 terminal simp only|n/a: none; unsqueezed terminal simpa retained.|
|1.16 nonterminal simp|n/a: none.|
|1.17 dot notation|Already `hd.eq_iff`; no new opportunity.|
|1.18 <\||n/a: no enclosing term parentheses to remove.|
|1.19 push Not|n/a: none.|
|1.20 trivial exists helper|n/a: not existential.|
|2.1 grind|Actual live attempt failed, leaving contradiction goal.|
|2.2 delete before grind|n/a: no successful grind proof.|
|2.3 simpa consolidation|Applied; isolated complete proof validates it.|
|2.4 fun_prop|n/a: no analytic function-property goal.|
|2.5 positivity|Actual live attempt: failed to prove nonzeroness.|
|2.6 gcongr|n/a: no order/monotonicity goal.|
|2.7 lia/omega|n/a: target is polynomial nonzeroness over an arbitrary field, no arithmetic inequality.|
|2.8 aesop|Actual live attempt failed exhaustive search, leaving False.|
|2.9 norm_num/norm_cast|n/a: no standalone numeric/cast goal; existing casts are simplified by standard CharZero simp facts.|
|2.10 decide|n/a: arbitrary field/family, not finite closed computation.|
|2.11 field_simp;ring|n/a: no goal of rational algebra equality; denominators occur only in the supplied nonzero product formula.|
|2.12 linear_combination|n/a: proof does not end in ring/ring_nf.|
|2.13 wlog|n/a: no symmetric branches.|
|2.14 calc|n/a: no calc.|
|2.15 <;>|n/a: one goal and no parallel branches.|
|3.1 erw|n/a: absent.|
|3.2 continuity/measurability|n/a: absent.|
|3.3 omega→lia|n/a: no arithmetic tactic.|
|3.4 rcases rfl|n/a: absent.|
|3.5 automation attributes|No attribute added: nonvanishing theorem needs substantial explicit hypotheses; no rewrite normal form.|
|3.6 simp_all|Actual live attempt left goal unresolved; no simp_all only to unsqueeze.|
|3.7 heartbeat option|n/a: absent; no limit raised.|

## Experiments and step-back review

Live multi-attempt tested grind, aesop, positivity, exact?, apply?, and the complete direct simpa
candidate at original L157. Failed tactics had concrete remaining goals; apply? returned partial
support/leadingCoeff facts only. The successful candidate closed its goal but old trailing source
reported 'No goals to be solved', so it was then checked as a complete isolated declaration and
as the actual edited file. Later simp/simp_all attempts left nonzero goal unresolved. A cast-drop
multi-attempt initially overlapped old multiline continuation and was syntactically inconclusive;
a complete isolated rerun of the whole proof without the ascription succeeded with no diagnostics.

A bounded fallback multi-attempt subprocess timed out after65seconds; native results were
obtained independently, and this timeout is not counted as verification. Native run_code for
initial proof/#checks/axioms succeeded (only long-line warnings in scratch); final isolated proof
with dropped ascription and a term checking the public theorem at its original type succeeded
without diagnostics. No external service failure is presented as theorem absence.

The coefficient/Vandermonde strategy remains the shortest verified conceptual argument. Whole
proof automation did not replace its mathematical inputs. No helper or API extraction improves
this three-line proof. Terminal simpa keeps all mathematical dependencies at the use site.

## Verification gates

| Gate | Result | Evidence |
|---|---|---|
|lake_build_file|pass|`/Users/ramin/.elan/bin/lake build Roth.Wronskian`, final log `/private/tmp/roth-wronskian09-module-final.log`; session41854 completed exit0,1826jobs.|
|complete LSP|pass|Final native lean_diagnostic_messages: success=true, partial=false, timed_out=false, failed_dependencies=[]; only baseline out-of-scope warnings.|
|isolated proof|pass|Native lean_run_code complete current proof: success=true, timed_out=false, diagnostics=[].|
|type compatibility|pass|Isolated example with original universes, field/CharZero instances, explicit hφ/hd and conclusion applies current theorem successfully.|
|axioms/source|pass|lean_verify: propext, Classical.choice, Quot.sound; trust=standard, non_standard_axioms=[], warnings=[].|
|definition_protected|pass|No definition, import, instance, or version edits.|
|theorem_statement_protected|pass|Only whitespace and =>→↦ changed in statement; original-type application compiles.|
|structure_gate|pass|Headline body3≤15; no conjunction or branches.|
|naming_gate|pass|Descriptive mathematical name; no forbidden pattern.|
|line_packing_gate|pass|Both final signature rows documented above; 100/77codepoints.|
|inequality_orientation_gate|pass|No ≥/> relation in signature/hypotheses.|
|comments/docstrings|pass|Existing docstring byte-preserved; no proof comments existed.|
|diff hygiene|pass|git diff --check passed; only this target source changed.|
|downstream closure|parent-owned|Parent performs full build+LeanEval after final source checkpoint; not claimed by this leaf.|

Overall per-declaration gates: pass. No deferred refactoring, rename, decomposition, or speculative API task.
The first SOURCE FROZEN message was premature: the subsequent mandatory cast audit removed a
redundant ascription. The parent was immediately notified; its earlier fullbuild is not counted
as final-source closure. Final module41854 and complete LSP validate the actual final source;
the parent owns the fresh fullbuild and LeanEval gates. No source edits followed cast removal.

## Result and checklist

Before8 declaration lines, after5, saved3. Proof body5→3. Audit issues4, fixed4. Applied1.4,
1.10,2.3 plus lambda/packing/cast syntax. Renames queued:none. Comments preserved: complete
existing docstring, no inline proof comments. Refactoring needed:none.

- [x] Step1: full required references read.
- [x] Step2: all24 audit items answered.
- [x] Step2.5: five-method search and auxiliary routes documented.
- [x] Step2.6: every parameter, mechanical probes, inversion and public literature documented.
- [x] Step2.7: before/after per-line codepoint tables.
- [x] Step2.8: per-occurrence inequality scan.
- [x] Step3: all42 rules have concrete status.
- [x] Step4: alternate strategies and direct term/consolidation considered.
- [x] Step5a: complete final LSP clean of errors.
- [x] Step5b: actual diff/build/type/axiom gates recorded.
- [x] Step6a: no rename needed; queue unchanged.
