# Phase 4 — `Roth.genWronskian_eq_zero_of_not_linearIndependent`

Current amendment: the user explicitly approved the two proposed unused public-instance
removals on2026-10-16. See [approved amendment audit](GenWronskian-api-amendment.md) for
the later source, type and verification evidence. The audit below records its historical
checkpoint; its pending-proposal statements describe that earlier state.

Scope: only this declaration, originally L36–45; now L36–44. Source snapshot:
`/private/tmp/roth-d02-before.lean`. No Git operations, shared reports, full builds,
or other declarations changed. Source ownership returned to file owner after freeze.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md in full, together with both installed
SKILL.md files, the complete worker contract, naming conventions, review stages, relevant
style sections, initial file audit and clean.tex §2.

## Full audit (before fixes, with resolutions)

1. LINT: two target warnings: unused section `[Fintype σ]`, and unused Fintype in public
   type. Preserve signature; separately compiled omission proposal below. Outside scope:
   missing authoritative copyright metadata, unused `DecidableEq` in `det_sum_rows`, and
   unused `Fintype` in existence theorem. No suppression or invented metadata.
2. HAVE SCAN: original L43 anonymous `have := congrArg (hasseDeriv (D μ)) hg`, no `by`,
   one mathematical use in final `simpa` plus preprocessing by `simp only`: inline by
   normalizing constant multiplication to scalar multiplication in final simplifier.
3. SET_OPTION: none.
4. SIMP SQUEEZE: L41 terminal `simpa` retained. Original L44 nonterminal `simp only`
   eliminated by consolidation; terminal L45 `simpa` retained unsqueezed.
5. NAMING: describes vanishing generalized Wronskian under dependence; snake separators
   preserve existing subject identifiers `genWronskian` and `LinearIndependent`, as in
   mathlib's `det_eq_zero_of_not_linearIndependent_cols`. No forbidden patterns or
   abbreviations; no rename needed.
6. LINE PACKING: measured table below, both signature lines pass unchanged.
7. BY PLACEMENT: `by` ends second signature line.
8. FORMAT: normalize two ordinary lambdas `=>` to `↦`; two-space proof indentation,
   no empty proof lines, no tactic chains, no `haveI`/`letI`.
9. COMMENTS: no inline comments; complete existing declaration docstring preserved.
10. DOCSTRING: existing statement/source documentation preserved verbatim.
11. VISIBILITY: public mathematical API, not a new implementation helper; preserved.
12. STRUCTURE: 8 proof lines → 7, no conjunction, longest branch 3 lines; no extraction.
13. MATHLIB: five searches below; existing null-vector API is the appropriate partial
    match. No generic wrapper replacement discovered.
14. JUNK DEF: n/a, theorem.
15. EXISTS LEMMA: n/a, public theorem, not a trivial witness helper.
16. SHOW vs CHANGE: neither present.
17. PUSH_NEG: none.
18. GENERALISE: every parameter audited below; public-instance proposal compiled,
    held for approval. Abstract coefficient/operator proposals closed under preserved API.
19. INEQUALITY: no reversed inequalities, table below.
20. NORMAL-FORM: vanishing equation with zero on RHS is canonical; independence
    hypothesis uses mathlib's predicate.
21. SYNTAX-GEN: explicit operator orders and implicit polynomial family are convenient
    for existing intended use; no equivalent restatement improves this scoped API.
22. IMPORT-FANOUT: n/a, no imports added.
23. CASTS: zero dropped, zero cross-type casts, zero new load-bearing ascriptions.
24. INSTANCE-NAME: n/a, no instance declaration.

Issues fixed: single-use have/preprocessing consolidation; two ordinary lambda arrows.
Refactoring deferred: public `[Fintype σ]` omission proposal only.

## Mathematics and source

Take a nonzero coefficient vector witnessing dependence. Each Hasse derivative preserves
its zero linear combination. The corresponding vector of constant polynomials is nonzero
and lies in the generalized Wronskian matrix kernel; its determinant therefore vanishes.
This matches clean.tex §2's second lemma and proof. Unlike the source's differential
formulation, this Hasse-derivative direction needs no characteristic-zero assumption and
no bounds on the operator orders.

## Mathlib search-status

All five methods were actually called. Native metadata and schemas were inspected.

| Method | Query | Result |
|---|---|---|
| A Lean-Finder | generalized Wronskian determinant vanishes linearly dependent polynomials linear maps | `Polynomial.isAlt_wronskianBilin`, `wronskian_self_eq_zero`, `wronskian_zero_right`: two-polynomial partial matches |
| B Loogle | `Matrix.det, ¬ LinearIndependent _ _` | `Matrix.det_eq_zero_of_not_linearIndependent_rows`, `_cols` |
| C LeanSearch | determinant zero if columns linearly dependent over field | `_cols`, `Matrix.exists_mulVec_eq_zero_iff_aux`, `Matrix.linearIndependent_cols_of_det_ne_zero` |
| D rg source | full target name; `linearIndependent.*det`, `det.*linearIndependent`, `exists_mulVec_eq_zero_iff` | target absent in mathlib source; determinant Basic and ToLinearEquiv APIs found |
| E local names | `det_eq_zero_of` | row, column, row-zero, column-zero and mulVec nonZeroDivisors APIs; index reported unavailable, so no absence claim based on local index |

Auxiliary variants inspected: `_rows`, `_cols`, `linearIndependent_cols_of_det_ne_zero`,
`LinearIndependent.restrict_scalars'`, `LinearIndependent.of_comp`, `map_injOn`, `map'`,
`exists_mulVec_eq_zero_iff`. Direct column dependence requires changing scalar rings and
building the Hasse evaluation linear map; it is not a simpler replacement for the already
used null-vector criterion. Common-equivalents table: no matching topology/finiteness
bucket. Concluded: partial match; keep domain-specific theorem using existing null-vector
API. The proof has genuine derivative/kernel content beyond a 1–3-call wrapper, and no
wrapper-type/cast/typeclass plumbing extraction signal. Public deletion is unauthorized.

Generic absence probes: isolated imports HasseDeriv/Wronskian and independently copied
definition (no import of GenWronskian). `exact?` fails to close; `apply?` returns only
coefficient/support partial goals and reports a sorry warning, hence is rejected. Full
logs `/private/tmp/roth-d02-auto-{exact,apply}.log`; these are failed exploratory probes,
not accepted proofs. No admitted proof is used by final verification.

## Generalisation status

| Parameter | Class | Use | Mechanical candidates and verification | Resolution |
|---|---|---|---|---|
| `{K : Type*}` | type variable | coefficients/scalars | already universe polymorphic; dropping leaves coefficient type unbound | keep |
| `[Field K]` | typeclass | public genWronskian signature; dependence/kernel APIs | DivisionRing loses commutativity required by polynomial determinant; CommRing+IsDomain version independently compiles after cloning/generalizing definition | keep: protected definition is currently Field-parametric; no public definition changes authorized |
| `{σ : Type*}` | type variable | polynomial variables and exponent vectors | already universe polymorphic; dropping leaves variables unbound | keep |
| `[Fintype σ]` | typeclass | unused | strongest drop-test: `omit [Fintype σ] in` compiles without even Finite | propose only; exact original signature preserved |
| `{l : ℕ}` | structure value | square matrix/family cardinality | dropping leaves Fin index unbound; arbitrary finite index requires public restatement | keep |
| `(D : Fin l → σ →₀ ℕ)` | structure value | Hasse operators | dropping loses designated matrix; arbitrary linear maps is abstract restatement, not a local weakening | keep |
| `{φ : Fin l → MvPolynomial σ K}` | structure value | input family | dropping loses theorem subject; arbitrary modules/operator codomains require restatement | keep |
| `(h : ¬ LinearIndependent K φ)` | proposition | nonzero dependence vector | drop is false: compiled singleton constant-one family with D=0 has nonzero Wronskian; strict→weak/point-local catalogues do not apply | keep |

Drop-h counterexample `/private/tmp/roth-d02-drop-h.lean` compiled exit0. Abstract
coefficient probe `/private/tmp/roth-d02-ring.lean` compiled exit0 with CommRing+IsDomain,
standard axioms; closed as outside protected API. Inversion check: concrete Hasse maps
are only used through linearity; an arbitrary-family-of-linear-maps theorem is a possible
future abstraction, not required to clean this existing theorem. No abstract extension
is pending in this worker.

### Literature search status

Web query: `generalized Wronskian linearly dependent polynomials generalization characteristic field`.
Top three returned hits:
1. [Diophantine approximation and the subspace theorem](https://pure.mpg.de/rest/items/item_3634762_1/component/file_3634763/content), §2.5: generalized polynomial Wronskians over characteristic-zero fields.
2. [Bostan–Dumas, Wronskians and linear independence (mirror)](https://citeseerx.ist.psu.edu/document?doi=764fc665e7ba79d9301b9508b7c49f91764623a2&repid=rep1&type=pdf): power-series/rational-function criterion and characteristic caveat for converse.
3. [Bostan–Dumas author-hosted paper](https://mathexp.eu/dumas/publications/Bostan_Dumas_2010_WLI.pdf): same primary paper, not independent evidence.

Inference from linearity and the compiled theorem: this dependence-implies-zero direction
already removes characteristic-zero and order bounds. Literature-standard broader
function spaces/operator families would change the subject API; no scoped change.
ChatGPT math MCP: unavailable (no matching tool in actual tool inventory).

### Concrete omission proposal (NOT APPLIED)

Insert `omit [Fintype σ] in` immediately **before** the preserved theorem docstring.
Separate complete theorem `/private/tmp/roth-d02-omit.lean` compiled exit0; `#check`
confirms no Fintype binder, axioms are exactly propext/Classical.choice/Quot.sound.
This removes both target warnings. Actual project callers: zero (`rg` over Roth finds
only declaration). Inferred calls remain applicable; explicit `@` callers would lose
one instance binder and may need adjustment. File owner forwarded this proposal for
scoped user decision and instructed that original signature remain unchanged.

## Signature width and inequality artifacts

`#check` with `format.width 100`:
```lean
@genWronskian_eq_zero_of_not_linearIndependent : ∀ {K : Type u_3} [inst : Field K] {σ : Type u_4} [Fintype σ] {l : ℕ}
  (D : Fin l → σ →₀ ℕ) {φ : Fin l → MvPolynomial σ K}, ¬LinearIndependent K φ → genWronskian D φ = 0
```
The printer leaves its long initial binder line intact; source signature is packed below
the 100-codepoint limit without changing the public type.

| Sig line | Chars | Next complete token | Arithmetic | Action |
|---|---:|---|---|---|
| 36 | 76 | `{φ : Fin l → MvPolynomial σ K}` (30) | 76+1+30=107 >100 | ok |
| 37 | 93 | none (proof follows) | n/a | ok |

| Occurrence | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| none | signature and hypotheses | no ≥ or > | n/a | n/a |

## Golfing rule pass (all 42 rules)

| Rule | Status |
|---|---|
| 1.1 by exact | n/a: no wrapper |
| 1.2 by rfl | n/a: none |
| 1.3 rw+exact | n/a: none |
| 1.4 simp+exact | applied: final simpa absorbs derivative normalization |
| 1.5 trailing rfl | n/a: none |
| 1.6 constructor | n/a: existential term already direct |
| 1.7 apply+exact | n/a: none |
| 1.8 by_contra | n/a: none |
| 1.9 eta lambdas | lambda C-composition retained: not eta-redex; both arrows normalized |
| 1.10 single-use have | applied: anonymous congrArg inlined |
| 1.11 apply+intro | n/a: none |
| 1.12 show | n/a: none |
| 1.13 have projections | n/a: obtain already used |
| 1.14 rw merge | n/a: no rw |
| 1.15 terminal simp only | n/a: original simp only was nonterminal |
| 1.16 nonterminal simp | n/a after consolidation; no bare nonterminal simp |
| 1.17 dot notation | already uses iff projection and linear map application |
| 1.18 <\| | n/a: no removable trailing-parenthesis application |
| 1.19 push_neg | n/a: none |
| 1.20 trivial exists | n/a: not a helper witness theorem |
| 2.1 grind | actual isolated whole-proof trial fails; diagnostic log retained |
| 2.2 before grind | n/a: no retained grind |
| 2.3 simpa consolidation | applied; forward smul_eq_C_mul first failed, reverse direction compiles |
| 2.4 fun_prop | n/a: no analytic function-property goal |
| 2.5 positivity | n/a: dependence witness nonzero comes from h; no ordered structure |
| 2.6 gcongr | n/a: no inequalities |
| 2.7 lia/omega | n/a: no arithmetic goal |
| 2.8 aesop | actual isolated whole-proof trial fails, no progress |
| 2.9 norm_num/cast | n/a: no numeric/cast identity |
| 2.10 decide | n/a: arbitrary field/family predicate, not finite computation |
| 2.11 field_simp/ring | n/a: no denominators/ring normalization goal |
| 2.12 linear_combination | n/a: no ring-ending block |
| 2.13 wlog | n/a: no symmetric case split |
| 2.14 calc | n/a: none |
| 2.15 <;> | n/a: witness nonzero and kernel identity need different arguments |
| 3.1 erw | n/a: none |
| 3.2 legacy analysis | n/a: none |
| 3.3 omega→lia | n/a: no omega/arithmetic |
| 3.4 rcases rfl | n/a: none |
| 3.5 attributes | no new attribute: broad conditional vanishing theorem, no normalization need |
| 3.6 simp_all | n/a: no simp_all only |
| 3.7 option limits | n/a: none |

Step-back reflection: whole-proof simp only unfolds determinant and leaves unsolved
goal; grind/aesop fail. Independent exact? cannot close. apply? offers partial support/
coefficient goals, not a proof. Term mode does not improve the two independent obligations.
The retained two-stage nonzero-kernel proof follows the mathematics directly.

Native multi_attempt stalled and was cancelled; separate direct MCP multi_attempt was
bounded at 65 seconds and timed out. Direct MCP goal inspection succeeded. Actual
independent CLI automation probes were then run with normal limits, no option raises.

## Verification and diff gates

Accepted independent proofs:
- `/private/tmp/roth-d02-candidate.lean`: shorter proof compiled exit0.
- `/private/tmp/roth-d02-nonself.lean`: imports only HasseDeriv/Wronskian, copied exact
  definition and shortened proof, no use/import of target; compiled exit0, standard axioms.
- `/private/tmp/roth-d02-original-type.lean`: fully quantified ORIGINAL type including
  Fintype binder assigned `@Roth.genWronskian_eq_zero_of_not_linearIndependent`, exit0.
  Target axioms exactly `[propext, Classical.choice, Quot.sound]`.

Complete LSP `/private/tmp/roth-d02-lsp.json`: success=true, partial=false,
timed_out=false, failed_dependencies=[], zero errors, all five existing warnings retained.
Module gate `/Users/ramin/.elan/bin/lake build Roth.GenWronskian`, exit0, built module
24 seconds; `/private/tmp/roth-d02-build.log`. An isolated omit probe initially raced
the module build's olean replacement; retry after build passed, as recorded above.
Diff captured using `diff -u` against start snapshot; only the target's proof changed.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | actual module command exit0 |
| definition_protected | pass | no definition/import change |
| theorem_statement_protected | pass | both signature lines byte-identical, original-type probe |
| structure_gate | pass | 7 proof lines, no conjunction, longest branch 3 |
| naming_gate | pass | mathematical subject/conclusion/hypothesis name, no forbidden pattern |
| line_packing_gate | pass | complete 76/93-codepoint signature table |
| inequality_orientation_gate | pass | zero reversed-inequality occurrences |

Overall: pass under preserved public API. Proposal remains a separately reported approval
item, not an unperformed routine proof obligation.

## Result and required checklist

Before 10 declaration lines; after 9; saved 1. Three mechanical issues fixed (two arrows
and one single-use-have/consolidation), two original warning instances retained pending
one public omission decision. No helpers, renames, comments or docstrings changed.

- [x] Step 1 — references read.
- [x] Step 2 — all 24 audit items reported.
- [x] Step 2.5 — five actual searches, variants, generic probes.
- [x] Step 2.6 — every parameter, literature, compiled omission and impact.
- [x] Step 2.7 — complete line-width table.
- [x] Step 2.8 — inequality scan table.
- [x] Step 3 — all 42 golfing rules reported.
- [x] Step 4 — independent automation and strategic reflection.
- [x] Step 5a — complete error-free LSP, original warnings listed.
- [x] Step 5b — diff gates and actual module build pass.
- [x] Step 6a — no rename needed; no rename queue mutation.

Freeze-ready full-source SHA256:
`612dec221169e15882ba06cd07f3cd99fa7fa7e1dd751f38705e5ba30b065418`.
