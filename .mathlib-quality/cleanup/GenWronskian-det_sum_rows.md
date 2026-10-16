# `det_sum_rows` — Phase 4

Result: **12 → 9 declaration lines**, proof body **8 → 5**. Replaced the separately proved
matrix identity and summand congruence with `MultilinearMap.map_sum_finset`, scalar extraction,
and the existing unapplied function-sum API `Finset.sum_fn`. Mathematical statement, instance
parameters, name, documentation, finite choice set, and surrounding declarations are preserved.
Ordinary lambda arrows were normalized to `↦`.

Frozen source SHA256: `9de4ad38403b6b44012fb4619cc58aeed78981be6ca1d7b434c98d49224fff06`.
The owner explicitly revoked source ownership after accepting that freeze. Subsequent work
was report-only and isolated checks. No commits, full builds, shared-log writes, or new helpers.

## Step 1 — references and context

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md. Both installed SKILL.md files, the full
853-line worker contract, applicable style-rules sections, naming-conventions,
mathlib-review-stages, the initial GenWronskian audit, and surrounding source were read.
The source passage clean.tex §2, lines 320–346, chooses one row term in each coordinate and
multiplies the coefficients; the finite choice set and products in this theorem match it.
ALL_TOOLS metadata was inspected. Native Lean MCP was available throughout; fallback unused.
No mathematical ChatGPT MCP appeared in the inventory.

## Step 2 — full audit (original lines 220–231)

1. **LINT:** inherited unused `[DecidableEq ι]` warning on this declaration. Retained in source
   under the public-API instruction; separately compiled removal proposal below. The complete
   file has five inherited warnings: header, two on the dependent-Wronskian theorem, this one,
   and the final theorem's Fintype warning. No suppression introduced.
2. **HAVE SCAN:** original `hM` has a `by` proof and one use; eligible to keep but eliminated
   through `Finset.sum_fn`. Final `h` has no `by`; used at the scalar-rewrite location, at
   simultaneous normalization, and at `exact h`. These transformations justify retaining it.
3. **SET_OPTION:** no per-declaration option, heartbeat raise, or recursion raise.
4. **SIMP SQUEEZE:** original `simp [Finset.sum_apply]` closes the extensionality goal.
   Final nonterminal normalization is explicit `simp only`; `simp_rw` specifies its rules.
   Terminal `simpa` consolidation was actually attempted in both bare and `only` variants,
   and failed; details below.
5. **NAMING:** `det_sum_rows` names the determinant, sum, and row operation; snake_case,
   no forbidden abbreviation/number pattern, single-letter name, `_ge_`, or `_gt_`. No rename.
6. **LINE PACKING:** all four signature lines measured in codepoints; table below. Their
   natural expression boundaries justify every break. Body maximum width 92.
7. **BY PLACEMENT:** `:= by` remains at the end of the last signature line.
8. **FORMAT:** two-space tactic indentation, four-space signature continuation, no internal
   empty lines, no semicolon chains, no `haveI`/`letI`, lambda arrows normalized.
9. **COMMENTS:** no inline comments existed; no comments were removed.
10. **DOCSTRING:** existing public docstring and source citation preserved verbatim. It
    explains row multilinearity and the source's use. Public documentation is protected.
11. **VISIBILITY:** public algebraic formula retained under its existing contract. Its actual
    caller is the same-file final existence theorem; no other project Lean caller was found.
12. **STRUCTURE:** final body five lines, no conjunction in statement, no branching or long
    branch. No extraction is required.
13. **MATHLIB:** all five actual search routes were used, with partial generic matches below.
    The final proof directly uses the generic API rather than introducing another helper.
14. **JUNK DEF:** n/a: theorem, not a definition.
15. **EXISTS LEMMA:** n/a: not a private existential witness theorem.
16. **SHOW vs CHANGE:** neither is present in the final proof.
17. **PUSH_NEG:** none.
18. **GENERALISE:** every parameter examined; compiled decidability removal proposal and
    rejected Ring/CommSemiring candidates recorded below. No public change applied.
19. **INEQUALITY:** no order relation in the signature; per-occurrence scan below.
20. **NORMAL-FORM:** RHS is a finite sum over the product choice set, with scalar products
    outside each determinant. This matches the generic multilinear expansion. No alternate
    competing canonical form or equivalence lemma introduced.
21. **SYNTAX-GEN:** current entrywise formula matches the actual `rw` caller. A bundled
    multilinear-map formulation already exists in mathlib and is used in the proof.
22. **IMPORT-FANOUT:** n/a: no import added or changed.
23. **CASTS:** zero explicit coercions introduced or dropped; two named type/size arguments
    `(R := A)` and `(n := Fin l)` select the determinant map and are elaboration-bearing.
24. **INSTANCE-NAME:** n/a: no instance declaration introduced or modified.

Issues fixed: redundant local matrix conversion, manual sum congruence/scalar extraction,
and ordinary lambda syntax. Refactoring needed: only the separately submitted public
DecidableEq proposal; no pending routine cleanup or helper extraction.

## Step 2.5 — mathlib search-status

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | `determinant matrix rows finite sums multilinear map map_sum_finset` | `Matrix.detRowAlternating`, `Matrix.sum_cramer`, `Matrix.sum_cramer_apply`; the latter two concern one Cramer argument, not simultaneous row choices. |
| B Loogle | `MultilinearMap, Finset.sum` | `map_sum_finset`, `map_sum`, `map_update_sum`, `map_add_univ`, and the auxiliary finite-sum theorem. |
| C LeanSearch | `determinant rows sum scalar multiples multilinear expansion finite sums` | row-update determinant lemmas, including `det_updateRow_add_smul_self` and `det_updateRow_sum_aux`; partial rather than this simultaneous expansion. |
| D source rg | `det_sum_rows`, `map_sum_finset`, `theorem map_sum`, `theorem map_smul_univ` in Alternating/Multilinear/Matrix sources | general sum/scalar APIs; inspected Multilinear.Basic lines 612–632 and Alternating.Basic lines 620–640. Follow-up sum-application source search found `Finset.sum_fn` in Algebra.BigOperators.Pi lines 49–53. |
| E local name | `map_sum_finset`, `map_smul_univ`, `det_sum` | multilinear/continuous variants, `AlternatingMap.map_smul_univ`; `Matrix.det_sum_le` and `det_sum_smul_le` are inequalities, not this identity. The local theorem appears in the project index and was not treated as a mathlib match. |

Auxiliary variants: `map_update_sum`, `map_sum`, `map_add_univ`, `map_smul_univ`,
`sum_cramer`, row-update sums, and unapplied `sum_fn` were examined. The common-equivalents
table's topology/finite-set buckets do not match this multilinear formula. Conclusion:
**partial match already in mathlib**; retain the protected determinant-facing formula and
build directly on generic multilinear sum/scalar and function-sum APIs. This is a presence
claim, not a claim that five failed searches proved absence. Live `exact?` did not close the
goal; `apply?` exhausted its normal budget and supplied generic partial suggestions only.

## Step 2.6 — generalisation

| Parameter | Class | Use / applicable catalogue candidates | Verification and result |
|---|---|---|---|
| `{l : ℕ}` | implicit size | both matrix dimensions and Fin row index; removal merely reintroduces inferred `l`, while changing to arbitrary Fintype is a public restatement | retain exact finite-row API; generic index form already available in MultilinearMap. |
| `{A : Type*}` | universe/type | arbitrary coefficient ring; already universe-polymorphic; drop would leave the operations and c/N types without their coefficient type | no stricter universe constraint to weaken; retain. |
| `[CommRing A]` | typeclass | Matrix.det and detRowAlternating; candidates Ring, CommSemiring, drop | both parent-class candidates were actually tried through isolated Lean MCP compilation: failed to synthesize CommRing at the determinant and map. Ring also lacks the product's CommMonoid. Dropping gives the same unsupported determinant interface. Retain. |
| `{ι : Type*}` | universe/type | arbitrary row-term index; already universe-polymorphic; drop would leave s/c/N without an index type | no universe restriction; retain. |
| `[DecidableEq ι]` | decidability | unused in type and proof; candidate drop | **compiled** without it and without local classical; standard axioms only. Separate public proposal; source retains it. |
| `s : Fin l → Finset ι` | data | finite row supports and RHS product choice set; drop removes the summation domains | no proposition/strict/point-local hypothesis to weaken; Finset→Set would change the finite formula. Retain. |
| `c : Fin l → ι → A` | data | arbitrary coefficients and RHS products; drop removes coefficients | no hypothesis to weaken; arbitrary already. Retain. |
| `N : Fin l → ι → Fin l → A` | data | arbitrary candidate rows and both determinants; drop removes row data | no hypothesis to weaken; arbitrary already. Retain. |

No strict inequality, global analytic hypothesis, bundled proposition, or field assumption is
present, so the point-local/strict-to-weak/unbundling catalogue entries have no target.
The rejected isolated class trials returned real instance errors; their automatic error recovery
terms were not accepted as proofs. Their ancillary stale-import notice is not a green gate.

**Mandatory inversion check:** determinant-specific content is discharged by selecting
`Matrix.detRowAlternating`; the remaining argument is a generic multilinear identity.
The abstract result already exists as `MultilinearMap.map_sum_finset` together with
`map_smul_univ`, and the proof now uses it. No fresh abstract API or speculative determinant
over semirings is proposed. The ordinary determinant interface requires CommRing.

### Concrete public proposal (submitted to owner before application)

Remove only `[DecidableEq ι]`. Independently proved candidate:
`/private/tmp/roth-d18-candidate.lean`; actual `lake env lean` session 95815 **exit 0**;
log `/private/tmp/roth-d18-candidate.log`. It does not call `Roth.det_sum_rows`; no `classical`
is needed. Its exact resulting width-100 check is:

```lean
@candidate : ∀ {l : ℕ} {A : Type u_1} [inst : CommRing A] {ι : Type u_2} (s : Fin l → Finset ι) (c : Fin l → ι → A)
  (N : Fin l → ι → Fin l → A),
  (Matrix.of fun μ ν ↦ ∑ i ∈ s μ, c μ i * N μ i ν).det =
    ∑ f ∈ Fintype.piFinset s, (∏ μ, c μ (f μ)) * (Matrix.of fun μ ν ↦ N μ (f μ) ν).det
```

The log gives axioms exactly `[propext, Classical.choice, Quot.sound]`.
Project-wide `rg det_sum_rows --glob '*.lean'` found only its declaration and the same-file
`rw [wronskian, hM, det_sum_rows]` caller, now L255; no explicit `@` application. That caller
would continue supplying only s/c/N through ordinary rewriting. Owner appended the separate
API proposal; this worker did not edit the shared proposal file. Source still has DecidableEq.

### Literature search status

Three actual public-literature queries, with top-three comparisons:

1. `determinant multilinear rows finite sums commutative ring generalization`
   - [Alphabeta, determinants over commutative rings](https://alphabetamath.cc/linear-algebra/determinants-of-matrices-over-a-commutative-ring): search result matches the commutative-ring scope; secondary, not relied on for proof.
   - [Mandal, Determinants](https://mandal.ku.edu/math790/determinants.pdf): search result states commutative-ring determinant multilinearity; direct fetch redirected to maintenance, so that limitation is explicit.
   - [Math StackExchange, generalized determinant](https://math.stackexchange.com/questions/1830122/is-there-a-commutative-ring-with-a-generalized-determinant): discusses alternative forms over rings; different object, not a valid reason to weaken ordinary determinant assumptions.
2. `multilinear map finite sums expansion tensor product determinant`
   - [Wikipedia, Multilinear map](https://en.wikipedia.org/wiki/Multilinear_map): search result identifies determinant as a multilinear example; secondary orientation only.
   - [Zintl, Multilinear Maps](https://www.math.uni-tuebingen.de/~zintl/MLA_Wi1819/MLA_Skript_%C2%A75.pdf): primary notes opened successfully; defines module multilinearity over commutative rings, then gives determinant over fields as an example. The abstract route is already implemented by mathlib.
   - [ScienceDirect, Multilinear map overview](https://www.sciencedirect.com/topics/mathematics/multilinear-map): broad tensor/multilinear context; does not improve the exact row formula, and not used as technical evidence.
3. `determinant multilinearity row linear combinations expansion product coefficients`
   - [Boyd, Matrix Algebra](https://faculty.fiu.edu/~boydj/mathecon/math08.pdf): primary notes opened successfully; Theorem 9.16.1 gives row/column multilinearity over reals. Our CommRing statement already exceeds that scalar generality.
   - [Rojas, On Multilinearity](https://people.tamu.edu/~rojas/ml.pdf): primary one-page notes opened successfully; the coordinatewise formulation explains expansion, with no requirement for a decidability hypothesis.
   - [Androma, Leibniz formula](https://androma.org/theorems/7882): search result's choice-function and product-coefficient expansion is closely analogous, but uses standard basis vectors; secondary and not relied on.

The implementation source clean.tex also explicitly uses the same finite row-choice formula.
Literature does not support a change to the requested formula; ordinary determinant over a
commutative ring is appropriate. The unused Lean decidability parameter is a separate formal
interface issue, established by compilation rather than a literature claim.
ChatGPT math MCP: **n/a, no such tool available in ALL_TOOLS**; no external opinion claimed.

## Steps 2.7–2.8 — signature packing and inequality scan

Actual built `#check @det_sum_rows`, rendered at `format.width 100`, is recorded verbatim in
`/private/tmp/roth-d18-built-check.log`. All widths below are measured codepoints.
Natural atomic next expressions are complete binders or complete sides of the equality.

| Sig line | Chars | Next token/expression width | Arithmetic | Action |
|---|---:|---|---|---|
| 220 | 96 | `(c : Fin l → ι → A)` = 19 | 96 + 1 + 19 = 116 > 100 | ok |
| 221 | 53 | complete LHS through `=` = 54 | 53 + 1 + 54 = 108 > 100 | ok |
| 222 | 58 | RHS finite sum through `:= by` = 88 | 58 + 1 + 88 = 147 > 100 | ok |
| 223 | 94 | no next signature line | n/a, body follows | ok |

| Occurrence | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| none | all signature/hypothesis lines | no `≥` or `>` order operator | n/a | none |

The arrows are Unicode `→`/`↦`; no `=>` syntax remains in this declaration. No `_ge_`/`_gt_`.

## Step 3 — all 42 golfing rules

| Rule | Status |
|---|---|
| 1.1 by exact wrapper | n/a: original is multiline proof, final exact depends on previous transformations. |
| 1.2 by rfl | n/a: no entire by-rfl proof. |
| 1.3 rw + exact | n/a: final exact follows simp normalization, not rw. |
| 1.4 simp + exact → simpa | tried, failed with normalized type mismatch; retained verified two steps. |
| 1.5 trailing rfl after simp | original trailing rfl eliminated with the sum-congruence block. |
| 1.6 constructor tuple | n/a: no conjunction/constructor. |
| 1.7 apply + exact | n/a: no apply. |
| 1.8 by_contra! | n/a: no contradiction proof. |
| 1.9 eta reduction | row functions in summands already eta-reduced to `N μ i`; no extra eta wrapper retained. |
| 1.10 single-use have | original proved hM removed via existing API; final h is transformed at two locations and then consumed. |
| 1.11 apply + intro | n/a: none. |
| 1.12 redundant show | n/a: none in final proof. |
| 1.13 obtain tuple | n/a: no projected conjunction. |
| 1.14 merge rw | replaced separated expansion/congruence/scalar rewrite by h plus one simp_rw. |
| 1.15 terminal simp only | n/a: final simp only is nonterminal; exact is required. |
| 1.16 nonterminal simp squeeze | final normalization explicitly squeezed. Original terminal simp removed with hM. |
| 1.17 dot notation | map_sum_finset invoked on determinant's multilinear map. |
| 1.18 `<|` | n/a: no dispensable trailing application parentheses. |
| 1.19 push Not | n/a: no push_neg. |
| 1.20 trivial existential helper | n/a: no existential helper. |
| 2.1 grind | actually tried at original goal; failed to establish expansion. |
| 2.2 delete before grind | n/a: no retained grind. |
| 2.3 simpa consolidation | actual bare/only simpa trials failed; direct simp-at-h-and-goal then exact succeeds. |
| 2.4 fun_prop | n/a: no continuity/differentiability/measurability goal. |
| 2.5 positivity | n/a: no order/sign goal. |
| 2.6 gcongr | n/a: no inequality. |
| 2.7 lia/omega | n/a: no Nat/Int arithmetic goal. |
| 2.8 aesop | actually tried; made no progress on row expansion. |
| 2.9 norm_num/norm_cast | n/a: no numeric evaluation/cast goal. |
| 2.10 decide/kernel | n/a: arbitrary ring identity and unbounded dimension, no closed finite computation. |
| 2.11 field_simp/ring | n/a: no denominator identity; theorem concerns determinant multilinearity. |
| 2.12 linear_combination | n/a: no ring/ring_nf conclusion or polynomial hypotheses. |
| 2.13 wlog | n/a: no symmetric branches. |
| 2.14 calc collapse | n/a: no calc. |
| 2.15 `<;>` | n/a: no repeated branches after the replacement. |
| 3.1 erw→rw | n/a: no erw. |
| 3.2 fun_prop migration | n/a: no legacy analysis tactic. |
| 3.3 omega→lia | n/a: no arithmetic tactic. |
| 3.4 rcases rfl | n/a: no substitution cases. |
| 3.5 automation attributes | no attribute added: expanding arbitrary row combinations should be explicit, not global simp. |
| 3.6 simp_all | n/a: no simp_all only. |
| 3.7 remove heartbeat option | n/a: none existed. |

## Step 4 — step back / simplify / performance

The mathematical proof is expansion by multilinearity, then taking the product of scalar
coefficients outside. The final code follows those two mathematical operations and uses
`sum_fn` to normalize the matrix entries. No new helper API is necessary.

Actual whole-goal trials `grind`, `aesop`, `simp`, `exact?`, `apply?` were made through native
multi_attempt. Some diagnostics also reflect that tool's one-line replacement leaving the
original have's continuation; only the actual leading failures are used as evidence, never
those parser artifacts as a proof result. Isolated run_code verified the successful proof.
The one-shot `simpa using map_sum_finset` alternatives failed on row sums or scalar extraction.
The combined `simp_rw` alternative succeeded only after a final rfl and was longer. Replacing
the final `simp only ... at h ⊢; exact h` by bare/only `simpa ... using h` failed on the
Matrix.of/alternating-map normalized type; unfolding Matrix.of and Equiv.refl did not fix it.
The verified five-line proof was retained; failed candidates did not enter source.

Native `lean_profile_proof` was actually attempted with line 220/top_n5/timeout45; its extracted
standalone snippet failed with unexpected end of input. Therefore no timing or performance
pass is claimed from that tool. No limit raise or profiling scaffolding entered source.
The parent owns the file-wide final simplify/performance workflow and final project gates.

## Step 5 — actual gates and independent checks

| Gate | Result | Actual evidence |
|---|---|---|
| lake_build_file | pass | `/Users/ramin/.elan/bin/lake build Roth.GenWronskian`, session 60607 exit 0; `/private/tmp/roth-d18-module.log`, Build completed successfully (1838 jobs). |
| complete LSP | pass | `/private/tmp/roth-d18-final-lsp.json`: success=true, partial=false, timed_out=false, errors=0, failed_dependencies=[], five inherited warnings. |
| definition_protected | pass | worker diff touches only det_sum_rows; no def/abbrev. |
| theorem_statement_protected | pass | exact original type and instance arguments retained; lambda syntax normalized. Built original-type example compiles. |
| structure_gate | pass | five proof lines, no conjunction or branch. |
| naming_gate | pass | descriptive snake_case, no forbidden patterns; no rename. |
| line_packing_gate | pass | all four signature rows measured above; no repack row. |
| inequality_orientation_gate | pass | per-occurrence scan contains no reversed order notation. |
| comments/docs | pass | docstring byte-preserved; no proof comments existed. |
| original-type application | pass | `/private/tmp/roth-d18-built-check.lean`, lake env lean session 60951 exit 0, original fully quantified formula applied to built Roth.det_sum_rows. |
| independent nonself proof | pass | `/private/tmp/roth-d18-candidate.lean`, session 95815 exit 0; proves stronger no-DecidableEq formula without calling the declaration. |
| actual built axiom gate | pass | `/private/tmp/roth-d18-built-check.log`: Roth.det_sum_rows depends exactly on propext, Classical.choice, Quot.sound. |

Overall: **pass**, with the inherited unused public-instance warning explicitly preserved
pending review of the concrete proposal. Source snapshots: `/private/tmp/roth-d18-original.lean`
and `/private/tmp/roth-d18-final-declaration.lean`. Full project build and separate LeanEval
are owned by the parent after freeze, not duplicated or claimed here.

## Step 6 — result and required checklist

Before 12 lines, after 9, saved 3. Renames queued: none. Comments preserved: none present;
existing docstring preserved. No source change remains pending. The public DecidableEq
proposal was delivered and recorded separately by the owner.

- [x] Step 1 — references/context read.
- [x] Step 2 — all 24 audit items answered.
- [x] Step 2.5 — five actual mathlib search methods and auxiliary variants.
- [x] Step 2.6 — every parameter, class weakening, inversion, public literature and proposal.
- [x] Step 2.7 — all signature lines measured with next-expression arithmetic.
- [x] Step 2.8 — per-occurrence inequality scan.
- [x] Step 3 — all 42 rules have status/reason.
- [x] Step 4 — strategy reflection and actual alternatives; profiler failure disclosed.
- [x] Step 5a — complete LSP success with no errors/failed dependencies.
- [x] Step 5b — actual module build, protection/structure/naming/packing/inequality gates,
  original-type application, independent nonself proof, actual built standard-axiom check.
- [x] Step 6a — no rename required; report completed within sole owned report path.
