# Phase 4 — `Roth.linearIndependent_kronecker`

Scope: only target declaration, fresh worker; baseline target lines 109–121, 13 declaration
lines / 10 proof-body lines. Final lines 109–119, 11 declaration lines / 8 proof-body lines.
Source frozen at SHA256 `66842fe6298588547e6abd33d06e4354e763637f48490d0410d75c0d1294f1de`.
Source ownership revoked by file owner after successful module/LSP gates; remaining work report-only.

Read both installed SKILL.md files, entire worker contract, initial GenWronskian audit,
golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md,
cleanup-gates.md, style-rules.md, and relevant review-stages material. I have read
golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and
cleanup-gates.md. Installed lean4/mathlib-quality skills applied. No agents spawned.

## Full 24-item audit

1. LINT: no target diagnostics; five pre-existing outside warnings listed below.
2. HAVE SCAN: original `hdeg` L115 has a lambda whose body is `by`, used once at L120.
   Although proof-content permits keeping it, successfully inline the bound proof directly
   into `kronecker_eq_zero_iff`; final target has no `have`.
3. SET_OPTION: none in target; no option added or raised.
4. SIMP SQUEEZE: original terminal `simpa [map_smul] using hg` stays unsqueezed;
   fold preceding `map_sum` rewrite into its simp list. New degree comparison terminal
   `simpa [smul_eq_C_mul]` closes its branch; no nonterminal bare simp.
5. NAMING: descriptive predicate `linearIndependent` plus map identifier `kronecker`,
   matching Mathlib's subject naming; no forbidden pattern or abbreviation, no rename.
6. LINE PACKING: all three signature lines measured in the table below, no repack needed.
7. BY PLACEMENT: `:= by` ends conclusion line; no standalone `by`.
8. FORMAT: two-space tactic indent; no empty proof lines or chained tactics; ordinary
   lambdas use `↦`. No `haveI`/`letI`.
9. COMMENTS: no proof comments originally; existing four-line public docstring preserved exactly.
10. DOCSTRING: public docstring already explains bounded partial degrees and cites source
    §2. Preserved under API/docstring instruction; no missing-doc issue.
11. VISIBILITY: public reusable preservation theorem; preserve public API.
12. STRUCTURE: final 8-line body, maximum branch 3 lines, no conjunction in signature;
    no extraction needed.
13. MATHLIB: five actual search methods below; generic preservation API is only a partial
    match because injectivity must be proved on the bounded-degree family span. Keep
    specialized theorem using existing degree/sum APIs and local zero criterion.
14. JUNK DEF: n/a, theorem rather than definition.
15. EXISTS LEMMA: n/a, public implication, no existential helper.
16. SHOW vs CHANGE: n/a, no `show`.
17. PUSH_NEG: n/a, no `push_neg`.
18. GENERALISE: every explicit/inferred parameter examined below. No public type change.
19. INEQUALITY: table below; no reversed inequality occurrence.
20. NORMAL-FORM: `LinearIndependent K φ` is the canonical Mathlib predicate. Internal
    `Fintype.linearIndependent_iff` is its standard finite linear-combination criterion.
21. SYNTAX-GEN: current degree hypothesis is directly applicable to families used later;
    an abstract map-injectivity statement already exists as `LinearIndependent.map_injOn`.
22. IMPORT-FANOUT: n/a, no new imports.
23. CASTS: 0 dropped, 0 cross-type, 0 load-bearing ascriptions in target diff.
24. INSTANCE-NAME: n/a, theorem creates no instance.

Issues fixed: (1) ordinary lambda arrows; (2) single-use named degree bound; (3) map-sum
rewrite followed by terminal simplification. Three issues fixed, no deferred refactoring.

## Five-method Mathlib search

A. Lean-Finder actual query: “linear independence preserved under Kronecker substitution
for polynomials of bounded degree”; returned Bernstein polynomial, Nobeling good-products,
and polynomial sequence independence results, no specialized match.

B. Loogle actual query `LinearIndependent, LinearMap`; returned
`LinearIndependent.of_comp`, `LinearIndependent.fintypeLinearCombination_injective`,
`linearIndependent_iff_injective_fintypeLinearCombination`, `LinearIndependent.repr`.

C. LeanSearch actual query “linear independence preserved by a linear map injective on a
submodule”; returned `LinearMap.iSupIndep_map`, `LinearMap.linearIndependent_iff`,
`LinearIndependent.map'`, `LinearIndependent.map_of_injective_injectiveₛ`.

D. Untruncated local source `rg`: `linearIndependent.*map|map.*linearIndependent|linearIndependent.*comp`
in LinearIndependent directory, then `degreeOf_(sum|smul|C_mul)|linearIndependent_kronecker`
through Mathlib. Found `MvPolynomial.degreeOf_sum_le`, `degreeOf_C_mul_le`, and
`degreeOf_C_mul`; no full-name specialized match. Additional variants `map_injOn`,
`LinearIndependent.map`, `map'`, `linearIndependent_iff` inspected in Basic.lean.

E. Actual local-search queries `LinearIndependent.map`, `linearIndependent`, `map_injOn`.
First response index unavailable; later responses warming, with positive source hits for
`LinearIndependent.map_injOn` and `LinearIndepOn.map_injOn`. No empty warming/unavailable
result is treated as absence. Source signatures independently inspected.

Auxiliary variants: `map`, `map'`, `map_injOn`, `of_comp`, degree sum / C-multiplication
bounds. Common-equivalents lookup: no listed disguise bucket applies. Six strict rules
checked: no new wrapper/predicate; searches + nonself exact?/apply? probes performed;
auxiliary variants inspected; direct Mathlib APIs used; no equivalent specialized theorem
identified for deletion; module documentation preserved under current scope.

Conclusion: partial generic matches, keep local specialized bounded-degree theorem.
Its 8-line body is ordinary degree control plus the existing Kronecker zero criterion;
no casts, wrapper round trips, typeclass plumbing, or API extraction signal remains.

## Generalisation — every parameter

| Parameter | Class | Dependency / candidates examined | Verification / result |
|---|---|---|---|
| `K : Type*` | type variable | `MvPolynomial σ K`, scalar field, output Polynomial; drop leaves signature unbound | already universe polymorphic; retain |
| `[Field K]` | typeclass | drop; DivisionRing; CommRing/CommSemiring | preserved `Roth.kronecker` and `kronecker_eq_zero_iff` APIs require Field; DivisionRing lacks required CommSemiring for these exact objects. A weaker coefficient construction requires changing other declarations, outside target; no claim Field is mathematically necessary |
| `σ : Type*` | type variable | polynomial indeterminates; drop leaves type unbound | already universe polymorphic; retain |
| `[Fintype σ]` | typeclass | drop / Finite | `kronecker` chooses `Fintype.equivFin σ` and its value depends on that enumeration; Finite alone does not provide that instance. Replacing it changes the preserved map value/type rather than simply dropping an unused assumption |
| `l : ℕ` | structure value | `Fin l` family length; drop unbinds signature; arbitrary finite index is a restatement | existing finite dimension fits uses; arbitrary index optional, closed under preserved API with no current need |
| `k : ℕ` | structure value | radix of map and degree bound; drop unbinds signature; abstract ordered type cannot supply Nat exponentiation | retain exact radix API |
| `hk : 1 < k` | proposition | drop, `1 ≤ k`, `0 < k`; strict-to-weak scratch below | existing zero criterion requires `1 < k`; weaker proof compatibility fails. This is an API dependency, not semantic necessity: for `k=1` the bound forces constants, so removing hk would need separate degenerate-case handling; optional change closed under preserved API, no pending work |
| `φ : Fin l → MvPolynomial σ K` | structure value | family appears in both hypotheses and conclusion; drop unbinds signature | arbitrary polynomial family, retain |
| `hφ : ∀ ν j, degreeOf j (φ ν) < k` | proposition | drop; point-localise; strict→weak `≤ k` | bound used at every family/variable degree. Without it (and also with weak bound) `σ=Fin 2`, `k=2`, family `X₀², X₁` is independent but both images are `t²`. This is a precise counterexample; cannot point-localise without omitting needed family degrees |
| `h : LinearIndependent K φ` | proposition | drop | zero one-element family (`l=1`, `k=2`) satisfies degree bound and has zero image, not linearly independent. No bundled halves to remove |

No separate DecidableEq parameter exists. No pointwise analysis hypotheses, scalar tower,
or concrete real/complex carrier exist. Inversion check: the final step uses the concrete
`kronecker_eq_zero_iff` and bounded-degree control; the abstract preservation statement
is already `LinearIndependent.map_injOn`, whose span injectivity proof adds rather than
removes work. Optional coefficient/index/radix generalisations are closed under the
explicit preserved-API scope; no speculative pending task or refactoring request.

## Public literature search

Actual web query: “Kronecker substitution preserves linear independence bounded partial
degree generalization”. Top three primary relevant hits captured:

1. *Sparse polynomial interpolation and testing*, §2.3: distinct partial degree bounds
   admit a mixed-radix substitution, rather than a uniform bound.
   https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/b213e882-3fe9-4ae4-8df3-2d889c18a18d/content
2. *PIT and Lower Bounds for Sum ABPs*, §2.3.2: bounded individual degrees give unique
   base-d monomial exponents; modular Kronecker maps may separate specified pairs.
   https://www.iitgoa.ac.in/~arpita/articles/PITAndLowerBoundsForSumABPs.pdf
3. *Kronecker Substitution* (Marsh/Monagan): reversible substitution uses a radix above
   the relevant variable degree.
   https://www.cecm.sfu.ca/~monaganm/papers/MarshCASC2016.pdf

These support the same bounded-support injectivity mechanism. Mixed radix and restricted
support separation are optional mathematical extensions requiring a changed map, so closed
under preserved API with no current need. Math ChatGPT MCP unavailable: discovery of
ALL_TOOLS found no chatgpt-math capability. Source `clean.tex` §2 lines 233–255 directly
states the linear-independence claim and uses uniqueness of bounded base-k digits.

## Line packing

`#check @Roth.linearIndependent_kronecker` was compiled with `format.width 100` in
`/private/tmp/roth-d10-verify.lean`:

```lean
@linearIndependent_kronecker : ∀ {K : Type u_3} [inst : Field K] {σ : Type u_4} [inst_1 : Fintype σ] {l k : ℕ},
  1 < k →
    ∀ {φ : Fin l → MvPolynomial σ K},
      (∀ (ν : Fin l) (j : σ), degreeOf j (φ ν) < k) →
        LinearIndependent K φ → LinearIndependent K fun ν => (kronecker k) (φ ν)
```

| Signature line | Characters | Next complete signature token | Arithmetic | Action |
|---|---:|---|---|---|
| 109 | 87 | `(hφ : ∀ ν j, degreeOf j (φ ν) < k)` (34) | 87 + 1 + 34 = 122 > 100 | ok |
| 110 | 68 | conclusion `LinearIndependent K fun ν ↦ kronecker k (φ ν) := by` (51) | 68 + 1 + 51 = 120 > 100 | ok |
| 111 | 55 | none, proof follows | n/a | ok |

The pretty-printed type unfolds binders and may expose generated binder text; the source
signature itself is at most 87 codepoints per line. Only the lambda notation changed,
which elaborates to exactly the same original public type.

## Inequality scan

| Occurrence | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| none | signature and hypotheses | no `≥` or reversed `>` | n/a; existing `1 < k`, degree `< k` correctly oriented | none |

Arrow `→` and original lambda `=>` are not inequality operators. Post-edit signature has
zero reversed inequality operators.

## All 42 golfing rules

| Rule | Status |
|---|---|
| 1.1 by exact | n/a, no wrapper |
| 1.2 by rfl | n/a, no reflexivity proof |
| 1.3 rw + exact | replaced original C-mul rewrite/exact by terminal simpa |
| 1.4 simp + exact | terminal simpa already present; map simplification consolidated |
| 1.5 trailing rfl | n/a, none |
| 1.6 constructor | n/a, no conjunction construction |
| 1.7 apply + exact | n/a, `apply h g` is followed by genuine degree/map proof |
| 1.8 by_contra! | n/a, no contradiction proof |
| 1.9 eta lambdas | no eta-redex: kronecker applied to `φ ν` is composition; normalized all ordinary arrows |
| 1.10 single-use have | applied to hdeg with proof content by direct refinement |
| 1.11 apply + intro | n/a, h application asks a polynomial equation, not binder |
| 1.12 show | n/a, none |
| 1.13 have projections | n/a, no tuple projections |
| 1.14 merge rw | no consecutive rewrites; final map_sum merged into terminal simpa |
| 1.15 terminal simp only | n/a, none |
| 1.16 nonterminal bare simp | n/a, none |
| 1.17 dot notation | applied degreeOf_sum_le `.trans_lt`, retained degreeOf_C_mul_le `.trans_lt` |
| 1.18 `<|` | applied between degree sum comparison and sup bound |
| 1.19 push_neg | n/a, none |
| 1.20 existential helper | n/a, none |
| 2.1 whole grind | attempted native multi_attempt, canceled stalled call; direct fallback timed out65; independent prefix scratch fails with unsolved goal |
| 2.2 before grind | n/a, no grind retained |
| 2.3 simpa consolidation | applied map_sum/map_smul and C-mul comparison |
| 2.4 fun_prop | n/a, no analytic function property |
| 2.5 positivity | n/a, no standalone arithmetic positivity goal; `Nat.zero_lt_of_lt hk` is a direct one-term bound |
| 2.6 gcongr | n/a, degree bound needs degreeOf_sum_le rather than order congruence |
| 2.7 lia / omega | n/a, no arithmetic tactic in original/final proof; explicit lemma application retained |
| 2.8 aesop | independent prefix scratch failed, made no progress; details below |
| 2.9 norm_num / norm_cast | n/a, no numeric calculation or casts |
| 2.10 decide | n/a, abstract field/poly family proposition, no finite closed computation |
| 2.11 field_simp; ring | n/a, no fractions or ring-normalization goal |
| 2.12 linear_combination | n/a, no ring/ring_nf ending or scalar identity |
| 2.13 wlog | n/a, no symmetric cases |
| 2.14 calc | n/a, no calc; trans_lt already composed |
| 2.15 `<;>` | degree and mapped-zero branches require different mathematics; no identical closure |
| 3.1 erw | n/a, none |
| 3.2 legacy analysis tactics | n/a, none |
| 3.3 omega→lia | n/a, no omega introduced; parent explicitly corrected initial punch-list |
| 3.4 rcases rfl | n/a, no rcases |
| 3.5 attributes | no new automation lemma needed; specialization is not a rewrite normal form |
| 3.6 simp_all | tried independent prefix scratch; fails “simp_all made no progress” |
| 3.7 option removal | n/a, no options |

## Step-back reflection

A linear-combination proof directly expresses why bounded monomials preserve independence.
The generic map_injOn route requires proving span membership bounds and injectivity for two
span elements, so it does not shorten this proof. Single-use hdeg is folded into the exact
point where its degree control is needed. No new helper, change of public statement,
term-mode wrapper, or extraction improves the resulting eight-line body. Full automation
and nonself exact?/apply? were actually tested as documented below.

## Verification and gates

- `/Users/ramin/.elan/bin/lake build Roth.GenWronskian`, session95684: exit0, 1838 jobs;
  target module compiled in 26s. No full project build or LeanEval run by this worker.
- Native `lean_diagnostic_messages` full file after edit: success=true, partial=false,
  timed_out=false, failed_dependencies=[], zero errors. Five known outside warnings:
  missing header metadata (L1); unused section Fintype (L36); same Fintype unused in
  dependent-zero theorem type (L32); DecidableEq det_sum_rows (L228); Fintype existence
  theorem (L246). No target warning. No warning suppressed or outside declaration edited.
- `/private/tmp/roth-d10-verify.lean`: compiled exit0 after module build. It contains an
  example with the exact ORIGINAL public type proved by the final theorem, plus a
  separate original proof renamed `RothD10.independent_reproof` that never references
  the target. Both axiom checks report only `[propext, Classical.choice, Quot.sound]`.
- Snapshot-based diff gate: every byte outside the target block is unchanged relative
  to `/private/tmp/roth-d10-start.lean`. No Git used. Public definition values, comments,
  docs, theorem name and elaborated type preserved. No sorry, axiom, option raise,
  native_decide, imports, or version changes.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | actual module invocation above, exit0 |
| definition_protected | pass | no def/abbrev diff |
| theorem_statement_protected | pass | original public type example compiled; only arrow notation changes |
| structure_gate | pass | 8 body lines, branches ≤3, no conjunction |
| naming_gate | pass | mathematical descriptive name, no forbidden patterns |
| line_packing_gate | pass | all 3 measured rows above |
| inequality_orientation_gate | pass | occurrence table, no reversed operators |

Overall: pass. Refactoring needed: none. Renames queued: none.

## Phase checklist

- [✓] Step 1 — references read.
- [✓] Step 2 — all 24 audit items printed.
- [✓] Step 2.5 — actual five-method search and generic-route probes.
- [✓] Step 2.6 — every parameter, mechanical candidates, dependencies/counterexamples, literature.
- [✓] Step 2.7 — every signature line measured with arithmetic.
- [✓] Step 2.8 — inequality occurrence table.
- [✓] Step 3 — all 42 rules have a concrete status.
- [✓] Step 4 — alternate strategy / automation reflection.
- [✓] Step 5a — complete clean LSP with all outside warnings recorded.
- [✓] Step 5b — every diff gate passed and module build cited.
- [✓] Step 6a — no renames required; no sidecar mutation.

Result: 13→11 declaration lines, 10→8 body lines, 2 saved. Three issues fixed;
no refactoring deferred. Existing docstring preserved, no inline comments originally.

## Isolated automation and weakening results

All following scratch files live outside the repository and use default heartbeats.
For automation probes, source was the worker snapshot prefix ending BEFORE the target,
so neither exact? nor apply? could reference the theorem under cleanup. Each probe was
compiled via `/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-d10-<name>.lean`.

| Probe | Exit | Actual result |
|---|---:|---|
| grind | 1 | unsolved LinearIndependent goal / contradiction goal remains |
| simp_all | 1 | `simp_all made no progress` |
| aesop | 1 | `aesop` failed, made no progress |
| exactq (`exact?`) | 1 | default 200000 heartbeat limit reached in whnf |
| applyq (`apply?`) | 1 | default 200000 heartbeat limit reached in whnf |
| hkweak (`1 ≤ k`) | 1 | `kronecker_eq_zero_iff` expects `1 < k`, gets `1 ≤ k` |
| hphweak (`degreeOf … ≤ k`) | 1 | `.trans_lt` expects strict bound, gets weak bound |

Logs: `/private/tmp/roth-d10-{grind,simp_all,aesop,exactq,applyq,hkweak,hphweak}.log`.
These failures establish failed proof/automation compatibility only, not mathematical
absence or necessity. No exhaustive absence claim is made from timeout. The five
searches positively identified generic building blocks; no specialized replacement was
identified. The exact original-type and independent reproof verification exited 0 and
used only standard axioms, independently of these intentionally failing experiments.
