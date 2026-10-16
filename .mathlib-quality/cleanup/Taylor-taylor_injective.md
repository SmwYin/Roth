# `MvPolynomial.taylor_injective` — fresh declaration audit

Scope: `Roth/Taylor.lean`, live lines 182–183 (original assignment 200–201).
Branch/baseline supplied by parent: `ramin-cleanup` / `59c59a0`.
Worker-start and frozen file SHA256:
`0a6ab3437c5950f4d2e800b78f03e7a53b7ce97f6cc248c3bff71fcf00a46f22`.
Only this declaration and this report were owned. No Git operations, shared-log edits,
public deletion, import changes, or full-project build were performed by this worker.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md. Also read both skill instructions,
the complete worker contract, relevant style/naming rules, and review-stage guidance.
The supplied scope overrides broad skill directions to delete public wrappers or alter docs/API.

## Result

Retained the original two-line declaration unchanged:

```lean
theorem taylor_injective (α : σ → A) : Function.Injective (taylor α : MvPolynomial σ A → _) :=
  Function.LeftInverse.injective (taylor_neg_taylor α)
```

Before: 2 lines. After: 2 lines. Saved: 0. Rules applied: none.
No target lint findings, no deferred refactoring, no renames. Existing docstring preserved.
The direct general theorem is already the shortest clear proof here. A tested dot-notation
replacement fails because the unbundled `∀ P, ...` type resolves `.injective` in namespace
`Function`, not `Function.LeftInverse`. A type annotation would erase the supposed saving.

## Full audit (24 items)

| # | Item | Concrete finding/action |
|---|---|---|
| 1 | LINT | No diagnostic in lines 182–183. Full-file native diagnostics finish with `partial=false`, `success=true`; existing line-1 copyright warning preserved. |
| 2 | HAVE SCAN | None: proof is a single application, with no `have` declarations. |
| 3 | SET_OPTION | None in target; no limit raises added. |
| 4 | SIMP SQUEEZE | No simp call in target. Bare `simp` experiment makes no progress. |
| 5 | NAMING | `taylor_injective` names the map and its property, uses snake case, matches no forbidden abbreviation/pattern; no rename needed. |
| 6 | LINE PACKING | Single signature line: 94 codepoints, including conclusion and `:=`; measured table below. |
| 7 | BY PLACEMENT | No `by` wrapper in final term proof. |
| 8 | FORMAT | Proof term has two-space indentation; no blank line, semicolon, `haveI`, `letI`, or sequential rewrite inside target. |
| 9 | COMMENTS | No inline proof comments. Existing one-sentence docstring preserved verbatim. |
| 10 | DOCSTRING | Public theorem has its existing sentence explaining the inverse relationship. Scope forbids rewriting/moving it. |
| 11 | VISIBILITY | Public named translation API retained, including use by `taylor_eq_zero_iff`; public deletion/visibility changes excluded by assignment. |
| 12 | STRUCTURE | One-line proof, no conjunction or branches; no extraction warranted. |
| 13 | MATHLIB | Five-method search finds the generic `Function.LeftInverse.injective` already used and the univariate analogue, not a drop-in multivariate translation theorem. Details below. |
| 14 | JUNK DEF | n/a: theorem, not a definition. |
| 15 | EXISTS LEMMA | n/a: public injectivity theorem, no existential witness. |
| 16 | SHOW vs CHANGE | n/a: no `show` or `change`. |
| 17 | PUSH_NEG | n/a: no negation-pushing tactic. |
| 18 | GENERALISE | All four parameters audited below; drop/parent probes fail for concrete elaboration reasons. No safe weakening found. |
| 19 | INEQUALITY | No reversed inequality in signature or hypotheses; table below. |
| 20 | NORMAL-FORM | `Function.Injective` on the underlying function is the canonical property; no equivalent-form family needed. |
| 21 | SYNTAX-GEN | OK: explicit translation vector and inferred universes/instances compose directly at the following call site. |
| 22 | IMPORT-FANOUT | n/a: no imports added. Univariate comparison was searched/read separately. |
| 23 | CASTS | Empty final source diff: 0 dropped, 0 added/kept as cross-type, 0 added/kept as load-bearing. Existing function type annotation remains under statement protection. |
| 24 | INSTANCE-NAME | n/a: target declares no instance. |

Issues to fix: none. Refactoring needed: none.

## Mathlib search-status

| Method | Actual query/evidence | Result |
|---|---|---|
| A Lean-Finder | `polynomial translation by a constant is injective left inverse`, 3 hits | `Polynomial.taylor_injective`, `Polynomial.taylor_inj`, `Polynomial.taylorEquiv_symm`; all univariate. |
| B Loogle | `Function.LeftInverse, Function.Injective`, 3 hits | `Function.LeftInverse.injective` (`Init.Data.Function`), `Function.rightInverse_of_injective_of_leftInverse`, `Function.Injective.exists_leftInverse`. |
| C LeanSearch | `a function with a left inverse is injective`, 3 hits | `Function.Injective.hasLeftInverse`, `Function.injective_iff_hasLeftInverse`, `Set.LeftInvOn.injOn`; generic supporting API. |
| D Source search | Untruncated `rg -n 'taylor_injective|LeftInverse.injective|taylorEquiv'` over `Algebra/Polynomial/Taylor.lean`, `Algebra/MvPolynomial`, `Logic/Function/Basic.lean` (regex alternation used in actual call) | Univariate theorem at `Polynomial/Taylor.lean:130`; its equivalence at 191; generic inverse applications at `Function/Basic.lean:965,968`. No multivariate hit in the searched directory. |
| E Name pattern | Native `lean_local_search` query `LeftInverse.injective`, project root supplied, limit 5 | Positive hit for exact generic theorem in Lean's `Init/Data/Function.lean`; index reported `warming`, so no absence claim is based on this index. |

Auxiliary variants inspected: `HasLeftInverse.injective`, `injective_iff_hasLeftInverse`,
`RightInverse` route, univariate `_inj` and `taylorEquiv_symm`. `#check` independently
confirmed the generic theorem, and the isolated original-type proof compiled using it.
Common-equivalents table: no discrete/finiteness/separation/bornology match.

Six-rule disposition: use the generic theorem directly (already done); search all five
methods without claiming exhaustive absence; inspect auxiliary forms; introduce no custom
predicate; do not delete protected public API; preserve protected module docs. The
univariate result concerns `Polynomial`, so replacing this declaration with it is not a
specialization. The general set-theoretic result is a partial match already used, not a
missing API to extract. No new theorem or wrapper was introduced.

Compiled generic-route probe: native `lean_multi_attempt` at live proof position L183
(after temporarily exposing the existing term with `by exact`) tried `grind`, `simp`,
`aesop`, `exact?`, and `apply?`. The first four did not close; `apply?` produced partial
routes, including `HasLeftInverse.injective` and kernel formulations, with unresolved
premises. Its synthetic incomplete-proof diagnostics belong to experiments, not the
restored live source. The temporary wrapper was reverted exactly.

## Generalisation status

Probes used native `lean_run_code`, `import Roth.Taylor`, `autoImplicit=false`, and
explicit original-type examples whose bodies called only `Function.LeftInverse.injective
(taylor_neg_taylor α)`. No probe used the audited theorem as its proof. Failed candidates
were isolated; the live public signature was never weakened.

| # | Parameter | Class | Used as | Mechanical candidates actually checked | Verified? | Result |
|---|---|---|---|---|---|---|
| 1 | `{σ : Type*}` | type variable | Index of vector and polynomial variables | Drop with autoImplicit off; universe-poly inspection | yes | Drop reports unknown `σ` at example line 5; already independently universe polymorphic. No pointwise/strict/bundled candidate applies to an index type. |
| 2 | `{A : Type*}` | type variable | Coefficient ring/vector codomain | Drop with autoImplicit off; universe-poly inspection | yes | Drop reports unknown `A` at example line 5; already independently universe polymorphic. No concrete numeric field specialization is present. |
| 3 | `[CommRing A]` | typeclass | `taylor` needs commutative semiring; inverse lemma needs negatives | Drop; `[Ring A]`; `[CommSemiring A]` | yes | Drop/Ring fail `CommSemiring A` at line 5 and `CommRing A` at line 6; CommSemiring fails `CommRing A` for inverse at line 6. Original retained. |
| 4 | `(α : σ → A)` | structure value | Translation map and its inverse witness | Drop with autoImplicit off | yes | Unknown `α` at example lines 5–6. Arbitrary vector already; point-localisation/strict→weak hypotheses absent, function domain/codomain determined by σ and A. |

No decidability, nontriviality, finiteness, order, topology, or separate proposition
hypotheses occur. No catalogue entry for those classes applies. No weakening is marked
kept. Tests establish failure of this proof/API under weaker classes; they do not claim
that every differently constructed theorem over every semiring is mathematically false.

Inversion check: the mathematical argument is abstract left-inverse injectivity; that
abstract statement already exists as `Function.LeftInverse.injective`, exactly the
current proof. Another abstract helper would duplicate it. Big-change candidates: none.

## Public literature search

Actual web searches:

1. `polynomial ring translation automorphism X plus a commutative ring generalization`
   combined with `left inverse function injective generalization` returned general inverse
   references. The displayed top three were
   [Injective function](https://en.wikipedia.org/wiki/Injective_function),
   [CMU functions notes](https://www.math.cmu.edu/~mradclif/teaching/127S19/Notes/Functions.pdf),
   [Cornell left inverse/injective notes](https://www.cs.cornell.edu/courses/cs2800/2015sp/lnotes/14_functions.pdf).
2. `polynomial ring translation automorphism "X" "a" commutative ring substitution inverse`:
   top three displayed hits were
   [Affine Automorphisms of a Univariate Polynomial Ring](https://androma.org/theorems/17392),
   [Lang polynomial ring automorphism question](https://math.stackexchange.com/questions/999478/lang-problem-about-automorphism-of-polynomial-ring),
   [Affine substitution question](https://math.stackexchange.com/questions/3757345/for-a-polynomial-ring-is-fx-mapsto-faxb-an-automorphism).
   Primary teaching sources also returned:
   [IISc substitution exercises](https://math.iisc.ac.in/~patil/current_courses/MA312-CA2020/Exercises/2020MA-MA312-ca-ex04.pdf)
   and [IIT Kanpur polynomial rings notes](https://home.iitk.ac.in/~chavan/alg3.pdf).

Finding: translation is a standard reversible substitution; left-inverse injectivity is
more general and requires no algebraic structure on its domain/codomain. That generality
is already supplied by the core theorem. The substitution result is naturally formulated
over commutative polynomial rings with arbitrary index sets; the current theorem has no
field, domain, characteristic-zero, or finite-index restriction to remove. The general
left-inverse fact is supported by the primary Cornell/CMU lecture material; the polynomial
comparison is consistent with the IISc substitution exercises. No literature-driven
public restatement proposed. ChatGPT math MCP: n/a, none discovered in `ALL_TOOLS`.

## Width and inequality artifacts

Native/CLI `#check` at `format.width=100`:

```lean
@MvPolynomial.taylor_injective : ∀ {σ : Type u_1} {A : Type u_2} [inst : CommRing A] (α : σ → A),
  Function.Injective ⇑(MvPolynomial.taylor α)
```

| Signature line | Codepoints | Next signature token | Arithmetic | Action |
|---|---|---|---|---|
| 182 | 94 | none; proof term follows | n/a; complete single-line signature | ok |

Proof-body line 183 has 54 codepoints. It is not another signature line and cannot join
the signature within 100 columns (`94 + 1 + 52 = 147`, after removing body indentation).

| Occurrence | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| none | Entire signature and inherited hypotheses | n/a: no `≥` or `>` | none | no `_ge_`/`_gt_` in name |

## Every golfing rule (42)

| Rule | Status and evidence |
|---|---|
| 1.1 by exact wrapper | Already a term; temporary testing wrapper reverted. |
| 1.2 by rfl | n/a: no reflexivity proof. |
| 1.3 rw + exact | n/a: no rewrite chain. |
| 1.4 simp + exact | n/a: no simplification chain. |
| 1.5 trailing rfl | n/a: no simp/rfl. |
| 1.6 anonymous constructor | n/a: no constructor proof. |
| 1.7 apply + exact | Already a single direct term application. |
| 1.8 by_contra! | n/a: no contradiction. |
| 1.9 eta reduction | n/a: no lambda in target proof. |
| 1.10 inline have | n/a: no have. |
| 1.11 apply + intro | n/a: no introductions. |
| 1.12 redundant show | n/a: no show. |
| 1.13 obtain | n/a: no projected conjunction/existential. |
| 1.14 merge rw | n/a: no rw. |
| 1.15 terminal simp only | n/a: no simp only. |
| 1.16 nonterminal simp | n/a: no simp. |
| 1.17 dot notation | Tried isolated `(taylor_neg_taylor α).injective`; compiler error `lean.invalidField`, environment lacks `Function.injective`; discarded. |
| 1.18 `<\|` | No saving: namespace application already needs one parenthesized inverse witness; `<\|` adds characters. |
| 1.19 push Not | n/a: no push_neg. |
| 1.20 existential inlining | n/a: no existential theorem. |
| 2.1 grind | Actual native attempt failed with negated Injective goal. |
| 2.2 delete before grind | n/a: no grind in final proof. |
| 2.3 simpa consolidation | n/a: no two-step simp/closing chain; bare simp attempt makes no progress. |
| 2.4 fun_prop | n/a: injectivity, no analytic/topological function-property goal. |
| 2.5 positivity | n/a: no order/positivity goal. |
| 2.6 gcongr | n/a: no inequality. |
| 2.7 lia/omega | n/a: no integer/natural arithmetic. |
| 2.8 aesop | Actual native attempt failed, made no progress. |
| 2.9 norm_num/norm_cast | n/a: no concrete computation/cast goal. |
| 2.10 decide | n/a: arbitrary polynomial equality/injectivity, no finite decidable computation. |
| 2.11 field_simp; ring | n/a: no denominator identity. |
| 2.12 linear_combination | n/a: no ring/ring_nf proof or equation combination. |
| 2.13 wlog | n/a: no symmetric cases. |
| 2.14 calc term | n/a: no calc. |
| 2.15 multiple goals | n/a: one direct proof, no generated subgoals. |
| 3.1 erw → rw | n/a: neither tactic. |
| 3.2 fun_prop migration | n/a: no continuity/measurability tactics. |
| 3.3 omega → lia | n/a: no arithmetic tactic. |
| 3.4 rcases rfl | n/a: no destructuring. |
| 3.5 automation attributes | Existing Injective API is directly applicable; adding simplification/grind registration changes automation API without a demonstrated need; none added. |
| 3.6 simp_all | n/a: no simp_all only. |
| 3.7 limit removal | n/a: no maxHeartbeats/maxRecDepth option. |

Step back: all generic closure/search attempts were executed. `apply?` only reformulates
the problem; the inverse witness is already available and directly discharges it. Term
mode beats adding automation or an elementwise cancellation proof. No helper or new API
is needed.

## Local verification and gates

Actual tools and results:

- `/Users/ramin/.elan/bin/lake build Roth.Taylor`: exit 0, build completed successfully
  (1439 jobs). Existing header warnings in Box/HasseDeriv/Taylor only.
- Native `lean_diagnostic_messages` on full Taylor file: `partial=false`,
  `success=true`, `timed_out=false`, no failed dependencies, only line-1 header warning.
- `/Users/ramin/.elan/bin/lake env lean /private/tmp/TaylorInjectiveIsolated.lean`:
  exit 0. This file contains the live source prefix strictly before the target docstring,
  then a theorem `taylor_injective_audit` with the exact original type/proof; target itself
  and all later declarations are excluded. It imports only the original two imports.
  `#print axioms` returns `[propext, Classical.choice, Quot.sound]`; no `sorryAx`.
- `/Users/ramin/.elan/bin/lake env lean /private/tmp/TaylorInjectiveChecks.lean`:
  exit 0; independent live-target `#check`/axiom check and `Polynomial.taylor_injective`
  comparison with its defining import explicitly added only to that scratch file.
- The earlier rejected dot-notation scratch returned exit 1 and `sorryAx` from failed
  elaboration; that candidate was discarded and the isolated file overwritten/recompiled
  successfully. No failed experiment is counted as a proof or allowed into live source.
- Start-snapshot comparison via Python `difflib`: empty source diff. SHA256 remeasured
  as above. Width measured with Python Unicode `len`, not bytes.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Actual module build exit 0 above. |
| definition_protected | pass | Empty worker source diff. |
| theorem_statement_protected | pass | Original signature and exact original proof restored. |
| structure_gate | pass | One-line body, no conjunction/branches. |
| naming_gate | pass | Descriptive property name; forbidden patterns/abbreviations absent. |
| line_packing_gate | pass | Complete single-line signature table above, 94 codepoints. |
| inequality_orientation_gate | pass | Zero reversed comparisons; occurrence table above. |
| original_type_isolated | pass | Pre-target-prefix CLI proof exit 0; target absent. |
| standard_axioms | pass | Only propext, choice, quotient soundness. |

Overall local gates: pass. Full-project build and separate LeanEval remain parent-owned,
sequential checks after freeze; they are not silently claimed as worker checks.

## Required 11-step checklist

- [x] Step 1 — mandatory references read.
- [x] Step 2 — all 24 audit items above.
- [x] Step 2.5 — five-method search and auxiliary variants above.
- [x] Step 2.6 — every parameter, actual probes, public literature, inversion check above.
- [x] Step 2.7 — every signature line measured at width 100.
- [x] Step 2.8 — complete zero-occurrence inequality scan.
- [x] Step 3 — all 42 golfing rules have individual statuses.
- [x] Step 4 — complete-proof reflection and search/automation attempts above.
- [x] Step 5a — native full diagnostics complete, no errors.
- [x] Step 5b — actual module build and protection/content gates above.
- [x] Step 6a — no rename needed, no shared sidecar touched.

Source ownership explicitly revoked to parent after local gates and SHA freeze. Parent
acknowledged the revocation and is performing full build then separate LeanEval. This
worker is report-only from that point onward.
