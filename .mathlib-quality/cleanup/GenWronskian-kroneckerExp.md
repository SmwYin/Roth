# Phase 4 — `Roth.kroneckerExp`

Target: `Roth/GenWronskian.lean:52`, one declaration line. Fresh dedicated worker;
source unchanged. Before 1 line, after 1 line, saved 0. Issues 0, fixed 0,
refactoring deferred 0, helpers 0, renames 0. Source ownership released after gates.

## References and scope

Read both installed `mathlib-quality/SKILL.md` and `lean4/SKILL.md`, the full
`/private/tmp/roth-genwronskian-worker-contract.md`, initial file audit, and mandatory
`golfing-rules.md`, `proof-patterns.md`, `mathlib-search.md`,
`generalisation-patterns.md`, `cleanup-gates.md`, relevant `style-rules.md`, and
`naming-conventions.md`. No Git, shared-log, other-declaration, full-build, or LeanEval work.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md.

The definition is the base-`k` positional exponent of a monomial under Kronecker
substitution. Source `clean.tex` §2 lines 243–254 writes
`s_1 + k s_2 + ... + k^{p-1} s_p`; its bounded-digit uniqueness is used by the
neighboring injectivity API. The definition itself accepts all natural digits and bases.

## Full audit

1. LINT: no target warning. Complete diagnostics give exactly the five known warnings
   outside the target, listed below.
2. HAVE SCAN: none; the body is a direct finite sum.
3. SET_OPTION: none.
4. SIMP SQUEEZE: no simp calls.
5. NAMING: `kroneckerExp` is meaningful lowerCamelCase for a data-valued Kronecker
   exponent. No forbidden abbreviation or numeric pattern; no rename needed.
6. LINE PACKING: exactly 100 codepoints for the entire definition; table below.
7. BY PLACEMENT: n/a, term-mode data definition.
8. FORMAT: one flush-left declaration, normal spacing, no empty internal lines,
   trailing whitespace, lambda arrows, or local-instance syntax.
9. COMMENTS: no inline comments; existing docstring preserved byte-for-byte.
10. DOCSTRING: one sentence describes the image-monomial exponent and its formula.
11. VISIBILITY: retain public API, used throughout monomial, injectivity and coefficient
    statements; its mathematical meaning supports discovery and reuse.
12. STRUCTURE: one-line term, no conjunction, proof block, or case branch.
13. MATHLIB: all five methods attempted; related `Nat.ofDigits` API found, see below.
14. JUNK DEF: keep. This names a mathematical exponent and has established
    `kronecker_monomial`, `kroneckerExp_injOn`, `coeff_kronecker` consumers/API.
15. EXISTS LEMMA: n/a, a natural-valued definition.
16. SHOW vs CHANGE: neither appears.
17. PUSH_NEG: absent.
18. GENERALISE: all actual parameters audited below; no safe weakening identified.
19. INEQUALITY: zero reversed inequalities, table below.
20. NORMAL-FORM: finite sum of digit times base power is the source's positional
    exponent form; list `Nat.ofDigits` requires an enumeration/reindexing adapter.
21. SYNTAX-GEN: OK. Accepting a finitely supported monomial exponent directly matches
    the polynomial API; a list representation would require extra conversions at calls.
22. IMPORT-FANOUT: n/a, no imports added.
23. CASTS: 0 dropped, 1 retained cross-type and load-bearing bridge `Fin → ℕ`.
    Removing `: ℕ` fails synthesis of `HPow ℕ (Fin (Fintype.card σ)) ...` in an isolated
    native LSP probe. The parentheses fix the exponent type, not cosmetic annotation.
24. INSTANCE-NAME: n/a, no instance declaration.

Issues to fix: none. Refactoring needed: none.

## Line packing

`#check @Roth.kroneckerExp` at `set_option format.width 100`:

```lean
@Roth.kroneckerExp : {σ : Type u_1} → [Fintype σ] → ℕ → (σ →₀ ℕ) → ℕ
```

| Sig line | Chars (complete declaration) | Next signature token | current + 1 + next | Action |
|---|---:|---|---|---|
| 52 | 100 | none; signature and term already on one line | n/a, no next line | ok |

The signature through `:=` occupies 58 codepoints; its term continues on the same
line. No broken signature token or conclusion remains to pack.

## Inequality scan

| # | Location | Original | Rewrite | Lemma rename? |
|---|---|---|---|---|
| 1 | signature and body | no `≥` or `>` | n/a | n/a, no `_ge_`/`_gt_` name |

## Mathlib search-status

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | `Kronecker substitution encode multivariate monomial exponent finite sum d j times k power enumeration`; direct bounded fallback `Kronecker substitution exponent encoding` | Both service requests returned read-operation timeout. Attempted, unavailable; no absence inference. |
| B Loogle | `Nat.ofDigits` | `Nat.ofDigits`, `Nat.ofDigits_digits`, `Nat.ofDigits_nil`; list digit evaluation is related. |
| C LeanSearch | `Kronecker substitution exponent sum base powers finite variables` | `Poly.map`, `MvPowerSeries.subst_monomial`, `MvPowerSeries.subst_pow`; no exact replacement among these hits. |
| D mathlib source | `kroneckerExp`, `[Kk]ronecker`, `ofDigits.*sum`, `sum.*ofDigits` in digit, multivariate-polynomial and Finsupp sources | `Nat.ofDigits_eq_sum_mapIdx`, related digit sums; no target-name hit. Search untruncated. |
| E local name pattern | `kronecker` | Project exponent/monomial API and unrelated matrix Kronecker products. `index: unavailable`; source hits establish presence only. |

Auxiliary variants inspected: `ofDigits_eq_sum_mapIdx`, its `_aux`,
`ofDigits_digits`, `sum_le_ofDigits`; source confirms their different list-based inputs.
Common-equivalents lookup: no discrete/finite/topological/bornological bucket applies.
Conclusion: partial match `Nat.ofDigits`; keep the established monomial-indexed definition.
It already uses mathlib finite sums and `Fintype.equivFin`. No claim of exhaustive absence
is made, and no new declaration is introduced. No ugly-proof API-extraction signal exists.
The six replacement rules were checked: no duplicate wrapper lemma/custom predicate is
being created, no exact match was found to migrate, auxiliary APIs were searched, and
no import or module-doc rewrite is needed for unchanged direct mathlib use.

## Generalisation status

The compiled full type has exactly `{σ}`, `[Fintype σ]`, `k`, `d`. Section variables
`K`, `[Field K]`, and `l` are absent; coefficient-ring extensions do not concern this type.

| # | Parameter | Class | Used as | Mechanical candidates considered/tried | Verified? | Result |
|---|---|---|---|---|---|---|
| 1 | `{σ : Type*}` | type-variable | domain of `d`, finite enumeration and sum | Drop would leave `d` and enumeration untyped; universe generalisation already present. No pointwise/strict/typeclass weakening applies to a type binder. | type checked | Keep universe-polymorphic domain. |
| 2 | `[Fintype σ]` | typeclass | chosen finite enumeration and finite sum | Drop tested in scratch with `autoImplicit false`; `[Finite σ]` cannot preserve the chosen enumeration value without selecting new `Fintype` data. No algebraic parents, pointwise or strict weakening applies. | yes, drop rejected | Fails `Fintype σ` synthesis at both sum and `equivFin`; keep. |
| 3 | `(k : ℕ)` | structure-value | radix in `k ^ ...` | Drop would remove the radix referenced by the body, not weaken a hypothesis. Abstracting ℕ is not an assumption weakening of a monomial exponent; pointwise/strict/universe changes inapplicable. | dependency inspection | Keep; already permits 0 and 1 without positivity hypotheses. |
| 4 | `(d : σ →₀ ℕ)` | structure-value | monomial digit vector | Drop would remove body input. An arbitrary function or altered digit type restates the monomial-indexed public API; no unused assumptions or bundled predicates exist. | dependency inspection | Keep finitely supported natural exponents. |

Inversion check: n/a, direct data definition, no proof that unfolds a concrete witness
and then works independently of it. Big-change candidates: none. Small-safe changes: none.

### Literature search

Web query: `Kronecker substitution exponent encoding generalization polynomial mixed radix`.
Top three returned hits (all the same primary thesis, in three published locations):

1. [Roche, Efficient Computation with Sparse and Dense Polynomials, Waterloo repository](https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/2517263a-23da-4ba0-b399-362229779bd3/content).
2. [Roche, thesis introduction](https://cs.uwaterloo.ca/~droche/phd/ch1-intro.pdf).
3. [Roche, full thesis](https://cs.uwaterloo.ca/~droche/phd/roche-v11.pdf).

Search excerpts describe the variable-radix extension of Kronecker exponent encoding.
This confirms the positional interpretation. Variable radix is a different construction,
not a removable assumption of this fixed-base exponent; no speculative pending
generalisation is created. Existing `clean.tex` §2 specifically uses one common base.
ChatGPT math MCP: n/a, no such tool is exposed in `ALL_TOOLS`.

## Golfing rule pass

- [1.1] n/a: no `by exact`.
- [1.2] n/a: no `by rfl`.
- [1.3] n/a: no rewrite/exact chain.
- [1.4] n/a: no simp/exact chain.
- [1.5] n/a: no simp or rfl.
- [1.6] n/a: no constructor proof.
- [1.7] n/a: no apply/exact chain.
- [1.8] n/a: no contradiction proof.
- [1.9] n/a: finite-sum binder is not an eta-expanded function application.
- [1.10] n/a: no have.
- [1.11] n/a: no apply/intro chain.
- [1.12] n/a: no show.
- [1.13] n/a: no projected have.
- [1.14] n/a: no rw.
- [1.15] n/a: no terminal simp only.
- [1.16] n/a: no nonterminal simp.
- [1.17] n/a: no eligible namespace application improves the expression.
- [1.18] n/a: necessary exponent ascription parentheses, no trailing application parentheses.
- [1.19] n/a: no push_neg.
- [1.20] n/a: not an existential helper.
- [2.1] n/a: direct data term, not a tactic proof for grind.
- [2.2] n/a: no grind prefix.
- [2.3] n/a: no simpa chain.
- [2.4] n/a: no analytic function-property goal.
- [2.5] n/a: no positivity goal.
- [2.6] n/a: no inequality goal.
- [2.7] n/a: no arithmetic proposition proof.
- [2.8] n/a: no proposition proof for aesop.
- [2.9] n/a: no numeric/cast proof; the sole coercion was independently tested.
- [2.10] n/a: no decidable proposition.
- [2.11] n/a: no denominators or ring identity proof.
- [2.12] n/a: no ring-ending proof with hypotheses.
- [2.13] n/a: no symmetric proof branches.
- [2.14] n/a: no calc.
- [2.15] n/a: no generated subgoals.
- [3.1] n/a: no erw.
- [3.2] n/a: no continuity/measurability tactic.
- [3.3] n/a: no omega.
- [3.4] n/a: no rcases.
- [3.5] n/a: no new lemma to register; definition remains an explicit API head.
- [3.6] n/a: no simp_all.
- [3.7] n/a: no heartbeat/recursion option.

Step-back reflection: the complete mathematical construction is already a single term
at exactly the line-width limit. Replacing it with proof search, a list adapter, or an
extra helper would obscure the finite-sum formula. Retain it without forced churn.

## Verification and gates

Native `lean_run_code` successful final probe included `format.width 100`, exact full
type display, full unapplied equality to the original function by `rfl`, independent
reconstruction as `∑ i : Fin (card σ), d (e.symm i) * k ^ (i : ℕ)` using
`e.symm.sum_comp`, and `#print axioms Roth.kroneckerExp`.
Result `success=true`, `timed_out=false`, no errors/warnings; axioms exactly
`propext`, `Classical.choice`, `Quot.sound`.

An exploratory `Nat.ofDigits (List.ofFn ...)` reconstruction encountered a dependent
Fin-index transport mismatch in scratch. It was replaced by the successful independent
Fin-sum reconstruction; neither probe touched project source. Intentional negative probes
confirmed Fintype necessity and the exponent coercion requirement.

Complete native `lean_diagnostic_messages` on the whole source:
`success=true`, `partial=false`, `timed_out=false`, failed dependencies `[]`, no errors.
Warnings: missing header metadata L1; unused Fintype section variable L36 and type
parameter L32 in the dependent-zero theorem; unused DecidableEq L241 in `det_sum_rows`;
unused Fintype L259 in existence theorem. No target warning. These are the supplied
five outside warnings; all source docs/comments and metadata were preserved.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | `/Users/ramin/.elan/bin/lake build Roth.GenWronskian`, session 45882, exit 0; 1838 jobs. |
| definition_protected | pass | Exact source byte equality to worker snapshot; full original function equality `rfl`. |
| theorem_statement_protected | pass | No theorem changes or new declarations. |
| structure_gate | pass | One-line data definition, no conjunction or branch. |
| naming_gate | pass | Meaningful lowerCamelCase, no prohibited pattern. |
| line_packing_gate | pass | Complete one-line definition is 100 codepoints, table above. |
| inequality_orientation_gate | pass | No reversed inequalities; scan above. |

Overall: pass. Source diff against `/private/tmp/roth-d04-kroneckerExp-before.lean` empty.
Final frozen source SHA256:
`0def23fb49d7e7ceab911c7637391c7e343b5f71307b503855950a1757d14fe2`.

Rules applied: none required. Renames queued: none. Comments preserved: existing
docstring unchanged; no inline comments. Refactoring needed: none.

## Required phase checklist

- [✓] Step 1 — mandatory references read.
- [✓] Step 2 — all 24 audit items reported.
- [✓] Step 2.5 — five actual search methods and limitations reported.
- [✓] Step 2.6 — every actual parameter and public literature search reported.
- [✓] Step 2.7 — complete signature-width table emitted.
- [✓] Step 2.8 — inequality scan emitted.
- [✓] Step 3 — all 42 golfing rules individually classified.
- [✓] Step 4 — independent reflection done; no forced churn.
- [✓] Step 5a — complete successful LSP diagnostics, outside warnings explicit.
- [✓] Step 5b — module and all source diff gates pass.
- [✓] Step 6a — no rename needed; report complete.
