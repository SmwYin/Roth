# Cleanup: `MvPolynomial.taylor_C`

Worker baseline: `ef61039`; target `Roth/Taylor.lean`, original worker lines 49–50, final line 49. Scope: this declaration and this report only. Public statement, binders, name, visibility, simp attribute, and docstring preserved. No Git operations.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md. Also read both skills, the full supplied worker contract, applicable style sections, and review-stage normal-form/documentation sections. No naming issue required the conditional naming-conventions reference. User instruction to keep the existing public API overrides generic wrapper-deletion suggestions in the reference rules.

## Result

Before: 2 declaration lines. After: 1. Saved: 1. Body: one terminal simp tactic becomes the direct proof term `algHom_C _ _`. This removes dependence on unfolding `taylor` and states the abstract reason constants are fixed. One improvement found and fixed; no outstanding refactoring or renames.

## Full audit

| # | Item | Finding/action |
|---|---|---|
| 1 | LINT | No target diagnostics; complete final LSP has only the user-preserved copyright warning at L1:2. |
| 2 | HAVE SCAN | No `have` bindings. |
| 3 | SET_OPTION | No declaration options or limit changes. |
| 4 | SIMP SQUEEZE | Original terminal `simp [taylor]` needed no squeeze. Replaced with a generic direct lemma. |
| 5 | NAMING | `taylor_C` describes translation of the standard named constant embedding `C`; snake-case composition with the existing mathematical constant. No forbidden abbreviation, numeric scheme, `_auxN`, `_ge_`, or `_gt_`. No rename warranted. |
| 6 | LINE PACKING | Single signature line, measured below; all binders and conclusion on one line. |
| 7 | BY PLACEMENT | Original `by` at end of signature; removed in favor of a term. |
| 8 | FORMAT | Flush-left theorem, no blank internal lines, no tactic chain, no `haveI`/`letI`; final line 75 codepoints. |
| 9 | COMMENTS | No inline comments present; none removed. |
| 10 | DOCSTRING | Existing one-sentence public API docstring “`taylor α` fixes constants.” preserved byte-for-byte. This elementary result needs no proof strategy or extra application advice. |
| 11 | VISIBILITY | Public simplification API, explicitly used in `Roth/Index.lean:212` and later Taylor proof; preserve public visibility. |
| 12 | STRUCTURE | One-term body, no conjunction or branches; no decomposition needed. |
| 13 | MATHLIB | Generic `MvPolynomial.algHom_C` found and applied directly; detailed five-method status below. |
| 14 | JUNK DEF | n/a: theorem, no definition. |
| 15 | EXISTS LEMMA | n/a: no existential conclusion or witness wrapper. |
| 16 | SHOW vs CHANGE | n/a: neither syntax present. |
| 17 | PUSH_NEG | n/a: absent. |
| 18 | GENERALISE | Every parameter reviewed and drop-tested; weaker Semiring cannot type the fixed Taylor API. Abstract generality already exists as `algHom_C`. |
| 19 | INEQUALITY | No inequality occurrences; explicit scan below. |
| 20 | NORMAL-FORM | Already canonical: translate of `C a` reduces to `C a`; RHS removes the translation and introduces no variable. |
| 21 | SYNTAX-GEN | OK: equation rewrites directly at call sites and remains a simp rule. |
| 22 | IMPORT-FANOUT | n/a: no new imports; generic lemma already available. |
| 23 | CASTS | 0 dropped / 0 kept cross-type / 0 kept load-bearing; no explicit casts in diff. |
| 24 | INSTANCE-NAME | n/a: theorem, no instance declaration. |

Issues to fix: replace unfolding-based simp proof by direct generic constant-preservation term (fixed). Refactoring needed: none. Preserve existing public theorem under user API policy; no wrapper deletion proposed as an outstanding task.

## Mathlib search status

| Method | Actual query/action | Result |
|---|---|---|
| A Lean-Finder | `MvPolynomial algebra homomorphism fixes constant polynomial` | `MvPolynomial.algHom_C`, `MvPolynomial.algebraMap_eq`, `Polynomial.coe_algebraMap_eq_CC`. |
| B Loogle | Initial `MvPolynomial.C, _ (_ _) = _` rejected because placeholder used as function; corrected `MvPolynomial.C, ?f (MvPolynomial.C ?a) = _` | `constantCoeff_comp_C`, `C_eq_algebraMap`, `algebraMap_eq`, `C_1`, `C_0`. |
| C LeanSearch | No repeated request | Unavailable: established HTTP 500 in this cleanup session, as provided by parent; no absence claim. |
| D Source | Untruncated `rg` for `aeval_C`, `algHom_C`, `map_C` in MvPolynomial Basic/CommRing/Eval; read exact source | `Basic.lean:441` has `algHom_C`; `Eval.lean:590` has `aeval_C`; `map_C` is coefficient-map API rather than the generic algebra-hom map. |
| E Name pattern | Native local searches `map_C`, `algHom_C` | Found source declarations, but index reported unavailable/warming. Positive source hits checked via `#check` and compiled proof; no absence inference. |

Auxiliary variants: `aeval_C`, `map_C`, `algebraMap_eq`, `C_eq_algebraMap`, and generic homomorphism `.commutes` (implementation of `algHom_C`). Common-equivalents table: no discrete/finiteness/separation/boundedness bucket applies. Generic algebra-hom preservation is the exact abstract content. The public project-specific simp API is retained per user direction, and its proof now uses the generic lemma. No new wrapper added, no absence claim, no module-docstring mutation.

## Generalisation status

All destructive/weakening probes ran in native `lean_run_code` scratch contexts with `autoImplicit false`; none were applied to the live file. Failed probe diagnostics are deliberate negative evidence, not shipped errors.

| # | Parameter | Class | Used as | Mechanical candidates tried | Verified? | Result |
|---|---|---|---|---|---|---|
| 1 | `{σ : Type*}` | type variable | Variable index of `α` and polynomial | Drop; universe widening reviewed | yes (drop) | Unknown identifier `σ`; already universe-polymorphic, no wider universe restriction to remove. |
| 2 | `{R : Type*}` | type variable | Coefficient type | Drop; universe widening reviewed | yes (drop) | Unknown identifier `R`; already universe-polymorphic independently of `σ`. |
| 3 | `[CommSemiring R]` | typeclass | Types `taylor`, `C`, and algebra homomorphism | Drop; weaken to `[Semiring R]` | yes | Both fail synthesis of `CommSemiring R`; retained. No order/analysis parents apply. |
| 4 | `(α : σ → R)` | structure value | Translation input in conclusion | Drop | yes | Unknown identifier `α`; no logical/global hypothesis to point-localise. Arbitrary function already allowed. |
| 5 | `(a : R)` | structure value | Constant input in conclusion | Drop | yes | Unknown identifier `a`; no positivity/nonzero or strictness assumption to weaken. Arbitrary coefficient already allowed. |

No proposition or decidability parameters are present. No strict-to-weak, topology, analytic, or bundled predicate catalogue entry applies. No small-safe generalisation retained. No big-change proposal warranted.

Mandatory inversion check: the original proof unfolds `taylor` once and then proves a generic algebra-hom fact. `algHom_C` already supplies the abstract theorem for every semiring-valued `R`-algebra target. The final proof applies that fact to the existing `taylor α`; adding an abstract companion would duplicate mathlib.

## Public literature search

Query: `polynomial algebra homomorphism constants evaluation universal property generalization`.

Top three returned hits recorded: [Knapp, Basic Algebra](https://www.math.stonybrook.edu/~aknapp/download/b2-alg-inside.pdf), [UTSA, Polynomials](https://mathresearch.utsa.edu/wiki/index.php?title=Polynomials), [Wikipedia, Polynomial ring](https://en.wikipedia.org/wiki/Polynomial_ring). Also returned the primary lecture note [The universal properties of polynomial rings](https://fenix.tecnico.ulisboa.pt/downloadFile/845043405563825/ring_algebras2.pdf).

The search supports the universal-property perspective: substitution is an algebra homomorphism extending the coefficient map. The installed mathlib declaration gives the exact formal generality over commutative semirings, so no field, characteristic, finiteness, or nontriviality assumption should be added. No new generalisation API follows from this search. ChatGPT math MCP: n/a, no callable math-second-opinion tool found in available metadata.

## Line packing

Final `#check @MvPolynomial.taylor_C` rendered with `format.width 100`:

```lean
@MvPolynomial.taylor_C : ∀ {σ : Type u_1} {R : Type u_2} [inst : CommSemiring R] (α : σ → R) (a : R),
  (MvPolynomial.taylor α) (MvPolynomial.C a) = MvPolynomial.C a
```

| Signature line | Codepoints through `:=` | Whole source line | Next signature token | Arithmetic | Action |
|---|---:|---:|---|---|---|
| 49 | 62 | 75 | none; proof term on same line | n/a: no next signature line; 75 ≤ 100 | ok |

Before: single signature line ending in `by` (65 codepoints), already fully packed. After: same statement prefix (62 through `:=`), with the proof term on that same line. No omitted signature lines.

## Inequality scan

| # | Location | Original | Rewrite | Lemma rename? |
|---|---|---|---|---|
| — | Whole signature and inherited parameters | No `≥` or `>`; no inequalities at all | n/a | none; no `_ge_`/`_gt_` in name |

## Golfing rule pass

| Rule | Status |
|---|---|
| 1.1 by exact wrapper | Applied term-mode endpoint after successful `exact algHom_C (taylor α) a` probe; final `:= algHom_C _ _`. |
| 1.2 by rfl | Tried `rfl`; not definitionally equal. No such wrapper to remove. |
| 1.3 rw + exact | n/a: no rewrites. |
| 1.4 simp + exact | n/a: original simp already terminal. |
| 1.5 trailing rfl | n/a: no trailing tactic. |
| 1.6 constructor chain | n/a: equality, no constructor chain. |
| 1.7 apply + exact | n/a: no apply chain. |
| 1.8 by_contra + push_neg | n/a: no contradiction proof. |
| 1.9 eta-reduce | n/a: no lambdas in target body. |
| 1.10 inline have | n/a: no haves. |
| 1.11 apply + intro | n/a: no introductions. |
| 1.12 redundant show | n/a: none. |
| 1.13 have projections | n/a: no haves or projections. |
| 1.14 consecutive rw | n/a: none. |
| 1.15 terminal simp only | n/a: original simp unsqueezed; removed altogether. |
| 1.16 nonterminal simp | n/a: original simp terminal. |
| 1.17 dot notation | n/a: direct named `algHom_C` is the relevant two-argument API. |
| 1.18 `<|` parentheses | n/a: no parenthesized final argument in selected term. |
| 1.19 push_neg | n/a: absent. |
| 1.20 single-use exists | n/a: not existential. |
| 2.1 grind | Tried live; failed with negated equality context. |
| 2.2 pre-grind tactics | n/a: original has no grind. |
| 2.3 simpa consolidation | n/a: one terminal tactic, no follow-up to consolidate. |
| 2.4 fun_prop | n/a: no function-property proposition. |
| 2.5 positivity | n/a: no order or nonzero goal. |
| 2.6 gcongr | n/a: no monotonic inequality. |
| 2.7 lia/omega | n/a: no natural/integer arithmetic. |
| 2.8 aesop | Tried live and isolated without target in environment; succeeds. Direct mathlib term is clearer and smaller. |
| 2.9 norm_num/norm_cast | n/a: no numerals or casts. |
| 2.10 decide | n/a: arbitrary semiring equality, no finite computation/decidable equality supplied. |
| 2.11 field_simp/ring | n/a: no denominators or polynomial arithmetic normalization. |
| 2.12 linear_combination | n/a: no ring-ending proof or algebraic hypotheses. |
| 2.13 wlog | n/a: no cases. |
| 2.14 calc to term | n/a: no calc. |
| 2.15 multiple goals | n/a: one equality goal. |
| 3.1 erw | n/a: none. |
| 3.2 continuity/measurability | n/a: none. |
| 3.3 omega to lia | n/a: neither needed. |
| 3.4 rcases rfl | n/a: none. |
| 3.5 automation attributes | Existing `[simp]` retained; canonical RHS removes translation. No additional registration needed. |
| 3.6 simp_all only | n/a: none. |
| 3.7 heartbeat options | n/a: none added or present. |

## Step back and experiments

The original proof is one tactic. A direct generic lemma better exposes its content and removes explicit unfolding. Live `lean_multi_attempt` results: `exact algHom_C (taylor α) a`, `exact aeval_C _ _`, `simp`, and `aesop` succeeded; `rfl` and `grind` failed. Both `exact?` and `apply?` reached the default 200000 heartbeat limit at `whnf`; recorded once with no raised limits. No searches repeated after these timeouts.

A self-contained native `lean_run_code` imported only `Roth.Box` and `Roth.HasseDeriv`, rebuilt the preceding Taylor definition as `probeTaylor`, and proved the chosen term with no target theorem available. The direct term, `aeval_C _ _`, bare simp, and aesop all compiled. `#check @algHom_C` confirmed its general signature. The selected `algHom_C _ _` does not need to unfold the Taylor definition, unlike the specialized `aeval_C` route. Standard axioms for the isolated proof: `propext`, `Classical.choice`, `Quot.sound`.

## Verification and gates

Complete native `lean_diagnostic_messages` after the patch: `partial=false`, `success=true`, `timed_out=false`, no failed dependencies; only pre-existing header warning L1:2. No target errors, sorries, or warnings.

`/Users/ramin/.elan/bin/lake build Roth.Taylor` exited **0**, 1439 jobs, Taylor target 13 seconds. Log: `/private/tmp/roth-taylor_C-module.log`. Parent notified before dependent builds. The final fresh CLI type/axiom probe is recorded below; an earlier native import probe emitted an out-of-date-import informational message while this build ran, so it is not used alone as final artifact evidence.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | PASS | Actual module build exit 0. |
| definition_protected | PASS | No definition/abbreviation changed. |
| theorem_statement_protected | PASS | Identical declaration text through `:=`; only proof replaced. |
| structure_gate | PASS | One-term body, no conjunction or branch. |
| naming_gate | PASS | Mathematical `taylor_C`; no forbidden patterns. |
| line_packing_gate | PASS | One measured signature row; final complete line 75 codepoints. |
| inequality_orientation_gate | PASS | Explicit table; zero reversed inequalities. |
| LSP | PASS | Complete elaboration, baseline header warning only. |
| isolated proof | PASS | No Taylor import or existing target available; direct term compiled. |
| axiom check | PASS | Only propext, Classical.choice, Quot.sound. |

Overall: PASS. Full-project and LeanEval dependent builds belong to parent checkpoint, not claimed here.

Source frozen and ownership released at SHA256 `57ed0bd46f1e97a504e63e53fb570c98045df68530f25bd8f48287ed2604ff6a`. No subsequent source edits.

## Phase checklist

- [x] Step 1 — required references and applicable style sections read.
- [x] Step 2 — all 24 audit items answered concretely.
- [x] Step 2.5 — five-method search status and auxiliary variants recorded.
- [x] Step 2.6 — every parameter audited/drop-tested; literature and inversion check recorded.
- [x] Step 2.7 — complete signature width table.
- [x] Step 2.8 — inequality occurrence table.
- [x] Step 3 — all 42 golfing rules recorded.
- [x] Step 4 — whole-proof alternatives and generic API considered and tested.
- [x] Step 5a — complete final LSP elaboration clean except baseline header warning.
- [x] Step 5b — diff gates and actual module build pass.
- [x] Step 6a — no renames needed, no sidecar mutation.

Comments preserved: one existing docstring byte-for-byte; no inline comments existed. Refactoring needed: none.

Fresh post-build artifact check: `/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-taylor_C-final-check.lean` exited **0**. It printed the final type shown above, confirmed `[propext, Classical.choice, Quot.sound]`, and compiled an exact application with all original arguments. No out-of-date-import warning appeared in this fresh CLI invocation.
