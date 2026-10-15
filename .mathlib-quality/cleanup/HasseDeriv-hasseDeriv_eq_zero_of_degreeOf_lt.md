# Phase 4 — `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`

Dedicated declaration-20 worker, 2026-10-15. Baseline `ccd8f49`; source lines 216–221
before, 216–220 after. Owned only this declaration and this report. No signature,
definition, import, attribute, visibility, docstring, source citation, or other declaration changed.

## Step 1 — References

Read `lean4/SKILL.md`, `mathlib-quality/SKILL.md`, the complete Phase-4 worker
prompt in `/Users/ramin/.local/share/roth-mathlib-quality/commands/cleanup.md`,
and the full `golfing-rules.md`, `proof-patterns.md`, `mathlib-search.md`,
`generalisation-patterns.md`, and `cleanup-gates.md`. Read the relevant
`style-rules.md` sections and `naming-conventions.md`, plus review-stages normal
forms, syntactic generality, and documentation guidance. Read `clean.tex`
§1 (lines 116–151) and the §6 degree-box vanishing passage (1497–1513).

## Step 2 — Full audit (24 slots)

| # | Item | Finding and action |
|---|---|---|
| 1 | LINT | No target warning; whole-file baseline copyright warning at line 1 only. |
| 2 | HAVE SCAN | L219 `have hP : e + d ∉ P.support := fun hP => …`: no `by`, one use at L221. Inline; replace manual contradiction with mathlib's degree/support lemma. The lambda's inner `hP` is a separate binder. |
| 3 | SET_OPTION | None; no limits added. |
| 4 | SIMP SQUEEZE | Inner `by simp` and final `simp […]` are terminal. Keep unsqueezed. |
| 5 | NAMING | `hasseDeriv_eq_zero_of_degreeOf_lt` describes conclusion and hypothesis; snake-case composition retains actual lowerCamelCase API identifiers. No forbidden pattern, abbreviation, `_ge_`, or `_gt_`; no rename. |
| 6 | LINE PACKING | Both signature lines measured below; already maximally packed by binder. |
| 7 | BY PLACEMENT | `by` ends signature line; retained. |
| 8 | FORMAT | Two-space body, no blanks or chained tactics. Nonstandard lambda arrow disappears with eliminated hypothesis. |
| 9 | COMMENTS | No inline proof comments; existing docstring and source citation byte-preserved. |
| 10 | DOCSTRING | Existing public documentation explains vanishing in any one variable and identifies §6 source; retained. |
| 11 | VISIBILITY | Public API used in `Roth/Taylor.lean` (185,221) and `Roth/MainLemma.lean` (485); retain public. |
| 12 | STRUCTURE | Body 4→3 lines; no conjunction, cases, or long branch; no extraction needed. |
| 13 | MATHLIB | Partial exact building block `MvPolynomial.notMem_support_of_degreeOf_lt` replaces hand proof; five methods below. |
| 14 | JUNK DEF | n/a: theorem. |
| 15 | EXISTS LEMMA | n/a: not an existential helper. |
| 16 | SHOW vs CHANGE | n/a: neither present. |
| 17 | PUSH_NEG | n/a: absent. |
| 18 | GENERALISE | Seven parameter rows below. Strictness necessary; semiring weakening fails current polynomial API. |
| 19 | INEQUALITY | Hypothesis uses `<`; zero `≥`/`>` occurrences. |
| 20 | NORMAL-FORM | Canonical derivative vanishing as equality to zero, strict degree bound on left. No alternative normal form required. |
| 21 | SYNTAX-GEN | Existing implicit variable/order/polynomial and explicit degree-bound proof match downstream uses. An existential variable witness merely repackages this usable pointwise theorem. |
| 22 | IMPORT-FANOUT | n/a: no import changes. |
| 23 | CASTS | 0 dropped / 0 cross-type / 0 load-bearing casts. `(s := e + d)` is an implicit argument specification needed to infer the support index. |
| 24 | INSTANCE-NAME | n/a: no instance declaration. |

Issues found: 2 (single-use `hP`, lambda arrow); both fixed by eliminating the
manual support proof. Refactoring needed: none. No substantial API proposal
was warranted by these findings. The separately pending declaration-19 proposal
was not applied or assumed.

## Step 2.5 — Five-method mathlib search

| Method | Actual query / evidence | Result |
|---|---|---|
| A Lean-Finder | `multivariate polynomial Hasse derivative zero when degree in one variable less than derivative order` | `Polynomial.hasseDeriv_eq_zero_of_lt_natDegree`, `Polynomial.natDegree_hasseDeriv_le`, `Polynomial.natDegree_hasseDeriv`. Univariate analogues, not replacements. |
| B Loogle | `MvPolynomial.degreeOf, _ < _` | `MvPolynomial.notMem_support_of_degreeOf_lt` and `degreeOf_lt_iff`; first adopted. |
| C LeanSearch | `Hasse derivative zero if order exceeds polynomial degree` | Attempted once; HTTP 500. Recorded service failure, not evidence of absence; no retry loop. |
| D Source | Untruncated `rg` for exact target, univariate analogue, and `notMem_support_of_degreeOf_lt` over Mathlib; inspected `MvPolynomial/Degrees.lean:270–303` and `Polynomial/HasseDeriv.lean:65–100`. | No exact multivariate duplicate; support lemma at Degrees:288 and univariate analogue at HasseDeriv:89. |
| E Name patterns | Native `lean_local_search` for `coeff_eq_zero_of_degreeOf_lt`, `notMem_support_of_degreeOf_lt`, `hasseDeriv_eq_zero`. | Positive source hits verify support lemma and univariate analogue; target appears only in Roth. Index reports unavailable, so empty coefficient-name result is not an absence claim. |

Auxiliary variants considered: `le_degreeOf_of_mem_support`,
`monomial_le_degreeOf`, `notMem_support_of_degreeOf_lt`, `degreeOf_lt_iff`,
`notMem_support_iff`, univariate `_of_lt_natDegree` and degree-subtraction bounds.
Common-equivalents table: no matching disguised topology/finiteness predicate.
At the live declaration entry, `exact?` failed to close the goal; `apply?`
offered coefficient/support extensionality only and reached its search budget.
No timeout/heartbeat settings were raised. Thus the actual conclusion is a
partial match: keep this local multivariate API and use mathlib's support lemma.
This is not a wrapper solely around mathlib: `coeff_hasseDeriv` is the project's
essential coefficient theorem for its multivariate derivative definition.

## Step 2.6 — Generalisation

| # | Parameter | Class | Use / candidates assessed | Verified / result |
|---|---|---|---|---|
| 1 | `{σ : Type*}` | type-variable | Arbitrary variable type; used in `j`, multi-index, and polynomial. Drop leaves dependent types unbound; already universe-polymorphic. | Dependency scan; retain, no finiteness/decidability assumptions. |
| 2 | `{R : Type*}` | type-variable | Arbitrary coefficient type used by polynomial and typeclass. Drop leaves their type unbound; already independent universe. | Dependency scan; retain. |
| 3 | `[CommSemiring R]` | typeclass | Try parent `[Semiring R]`; dropping entirely is still weaker. `MvPolynomial σ R` and derivative API require commutative semiring. | Actual isolated elaboration with `[Semiring R]` fails `failed to synthesize CommSemiring R` at polynomial binder. Retain; removing class likewise cannot form current statement. |
| 4 | `{j : σ}` | structure-value | Used in strict hypothesis and degree/support lemma. Drop leaves hypothesis unbound. Existential choice is already expressible by applying this theorem after obtaining witness. | Dependency scan; retain pointwise form. |
| 5 | `{d : σ →₀ ℕ}` | structure-value | Used in hypothesis/conclusion and shifted coefficient. Drop leaves conclusion unbound. Natural exponents are intrinsic to this polynomial API. | Dependency scan; retain, no concrete index or bounded-support assumption. |
| 6 | `{P : MvPolynomial σ R}` | structure-value | Used in hypothesis/conclusion and coefficients. Drop leaves statement unbound; already arbitrary polynomial. | Dependency scan; retain. |
| 7 | `h : degreeOf j P < d j` | proposition | Drop; weaken `<` to `≤`. Already point-local at arbitrary `j`; no bundled conjunction. | Counterexample checked by Lean: `P=1`, `d=0`, `σ=Unit`, `R=ℕ` has degree ≤ order but derivative nonzero. Both proposed weakenings false. |

Counterexample certificate:

```lean
example : degreeOf () (1 : MvPolynomial Unit ℕ) ≤ (0 : Unit →₀ ℕ) () ∧
    hasseDeriv 0 (1 : MvPolynomial Unit ℕ) ≠ 0 := by simp
```

Inversion check: already typeclass-parametric, with arbitrary polynomial and
multi-index. The derivative's coefficient identity is essential, not a named
concrete witness that disappears after unfolding. No abstract-object proposal.
No mechanical weakening survives; statement preserved.

### Public literature search

Web query: `Hasse derivative multivariate degree vanishes order polynomial generalization`.
Three relevant distinct primary-source hits inspected in search output:

1. [Tao, EMS Surveys in Mathematical Sciences 1 (2014), pp. 1–46](https://ems.press/content/serial-article-files/36979): gives coordinatewise binomial formula for multivariate Hasse derivatives, including vanishing binomial factors. This supports the existing vanishing mechanism.
2. [ECCC Report 32 (2026)](https://eccc.weizmann.ac.il/report/2026/032/download): defines multivariate Hasse derivatives as coefficients of `f(X+Z)` over fields. No weaker strictness requirement is suggested.
3. [Joints of Varieties](https://link.springer.com/article/10.1007/s00039-022-00597-5): discusses coefficient extraction without factorial division and Taylor expansion over general fields. No stronger coefficient assumption is needed here.

The local source explicitly permits any commutative semiring (§1), and §6
states vanishing for multi-indices outside the degree box. The present
`CommSemiring`/arbitrary-variable formulation already covers this; the
field-based literature does not warrant an API restatement. The support
criterion is a possible alternative description of the same proof mechanism,
but no concrete downstream need or missing difficult API was found. It is not
a blocking proposal. ChatGPT math MCP: skipped as explicitly directed.

## Step 2.7 — Measured line packing

Actual `#check @hasseDeriv_eq_zero_of_degreeOf_lt` at `format.width 100`:

```text
@hasseDeriv_eq_zero_of_degreeOf_lt : ∀ {σ : Type u_1} {R : Type u_2} [inst : CommSemiring R] {j : σ} {d : σ →₀ ℕ}
  {P : MvPolynomial σ R}, degreeOf j P < d j → (hasseDeriv d) P = 0
```

| Signature line | Codepoints | Next whole binder | Arithmetic | Action |
|---|---:|---|---|---|
| 216 | 85 | `(h : degreeOf j P < d j)` = 24 | 85 + 1 + 24 = 110 > 100 | ok |
| 217 | 55 | No next signature line; conclusion and `:= by` already included | n/a | ok |

Before/after signature identical; final table remeasured with Python `len`.
Final body widths: L218=7, L219=46, L220=74 codepoints.

## Step 2.8 — Inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 1 | L217 hypothesis | `degreeOf j P < d j` | None; smaller side already left | None |
| 2 | Entire signature | No `≥` or `>` occurrence | n/a | Name has `_lt`, no `_ge_`/`_gt_` |

## Step 3 — All 42 golfing rules

| Rule | Status |
|---|---|
| 1.1 by-exact | n/a: no wrapper. |
| 1.2 by-rfl | n/a: absent. |
| 1.3 rw+exact | n/a: absent. |
| 1.4 simp+exact | n/a: terminal simp already closes. |
| 1.5 trailing rfl | n/a: absent. |
| 1.6 constructor terms | n/a: no product goal. |
| 1.7 apply+exact | n/a: absent. |
| 1.8 by_contra! | n/a: no contradiction tactic block. |
| 1.9 eta reduction | n/a: removed lambda was not an eta wrapper. |
| 1.10 inline have | Applied: eliminate single-use hP and replace its content with mathlib support API. |
| 1.11 refine+fun | n/a: no apply-intro sequence. |
| 1.12 redundant show | n/a: absent. |
| 1.13 obtain projections | n/a: no conjunction projections. |
| 1.14 merge rw | n/a: no rw sequence. |
| 1.15 unsqueeze terminal simp | Already satisfied; both simp calls terminal and unsqueezed. |
| 1.16 squeeze nonterminal simp | n/a: no nonterminal simp. |
| 1.17 dot notation | Already uses h.trans_le and iff projection. |
| 1.18 trailing parentheses | Parentheses needed inside simp list; replacing final subargument by `<|` does not remove its enclosing parentheses. |
| 1.19 push Not | n/a: no push_neg. |
| 1.20 inline existential | n/a: no existential helper. |
| 2.1 grind | Actual live whole-proof test failed, leaving derivative vanishing unproved. |
| 2.2 remove before grind | n/a: no retained grind. |
| 2.3 simpa | Whole `simp [coeff_hasseDeriv]` made no progress; no follow-up exact to consolidate. |
| 2.4 fun_prop | n/a: algebraic equality, no function regularity predicate. |
| 2.5 positivity | n/a: no positivity goal in final proof; nonnegative addend bound is already one terminal simp. |
| 2.6 gcongr | Actual arithmetic subgoal test `d ≤ e+d` made no progress. |
| 2.7 lia/omega | Actual isolated natural-number addend-bound test with lia succeeds; keep existing `simp`, which also handles Finsupp evaluation. No omega needed. |
| 2.8 aesop | Actual live whole-proof test failed, made no progress. |
| 2.9 norm_num/norm_cast | n/a: no concrete numeric computation or cast normalization. |
| 2.10 decide | n/a: arbitrary polynomial and abstract coefficient type, not a closed decidable computation. |
| 2.11 field_simp/ring | n/a: no denominators or ring-normalization goal. |
| 2.12 linear_combination | n/a: no ring/ring_nf finish or usable ring equalities. |
| 2.13 wlog | n/a: no symmetric branches. |
| 2.14 calc term | n/a: no calc; transitivity already a term. |
| 2.15 shared closer | n/a: one coefficient goal, no parallel branches. |
| 3.1 erw→rw | n/a: absent. |
| 3.2 function-property tactics | n/a: absent. |
| 3.3 omega→lia | Already satisfied by 2.7; no omega in source. |
| 3.4 rcases rfl | n/a: no cases. |
| 3.5 automation attribute | Not added: conditional vanishing rule needs externally supplied variable j; no demonstrated simplifier/automation need and attributes are public API. |
| 3.6 simp_all | n/a: no simp_all only. |
| 3.7 heartbeat option | n/a: none existed or added. |

## Step 4 — Reflection and actual alternatives

Coefficient extensionality is the mathematical core. Whole-proof `grind`,
`simp [coeff_hasseDeriv]`, `aesop`, and `exact?` did not solve it. `apply?`
suggested `eq_zero_iff.mpr`/support/extensionality, leaving the same coefficient
obligation. Term mode would merely replace `ext e` with an explicit extensionality
lambda. The adopted three-line body is clear and uses the existing API.

An initial inlining attempt omitted `(s := e + d)` and failed because Lean did
not infer the support exponent before solving the arithmetic side condition.
Both an inlined manual contradiction and an inlined support-lemma attempt were
actually tested. The support-lemma version with this explicit implicit argument
compiled in isolation. Multi-attempt replacement also exposed leftover-line
diagnostics; those were not mistaken for accepted proof results. The successful
isolated proof, live diagnostics, and module build are authoritative.

## Steps 5–6 — Verification and gates

Actual command: `/Users/ramin/.elan/bin/lake build Roth.HasseDeriv`.
Execution session `42523`, final exit **0**; target built in **6.4s**,
1430 jobs, only baseline copyright warning at line 1.

Direct MCP client invoked with the corrected elan PATH through
`/private/tmp/roth_mcp_probe.py` (session `78281`):

- `lean_diagnostic_messages` on the full file, timeout 45s:
  `success=true`, `partial=false`, `timed_out=false`, `failed_dependencies=[]`;
  only baseline copyright warning, no errors or target warnings.
- `lean_goal` at L220 C70: `status=complete`, `goals=[]`.
- `lean_verify` on the fully qualified theorem: `trust=standard`,
  axioms `[propext, Classical.choice, Quot.sound]`, no nonstandard axioms,
  no source-scan warnings.
- `lean_run_code` checked a renamed theorem containing the exact replacement,
  `#print axioms`, and `example : @decl20Candidate =
  @hasseDeriv_eq_zero_of_degreeOf_lt := rfl`: success. Early scratch-only
  formatting warnings were corrected in the final isolated probe.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | PASS | Actual module command above, exit 0. |
| isolated proof/type | PASS | Replacement elaborated; proof equality `rfl` checks unchanged type. |
| axiom/source scan | PASS | lean_verify standard three axioms; no source warnings. |
| full LSP diagnostics | PASS | Complete result, no errors/dependency failures; documented pre-existing header warning. |
| definition_protected | PASS | Focused before/after diff has no definition or abbreviation change. |
| theorem_statement_protected | PASS | Python string comparison before `:= by`: byte-identical. |
| structure_gate | PASS | Three body lines, no conjunction or case branch. |
| naming_gate | PASS | Descriptive name, no forbidden patterns; no rename needed. |
| line_packing_gate | PASS | Both signature rows measured above; no remaining repack. |
| inequality_orientation_gate | PASS | No reversed inequality or forbidden name fragment. |
| comment/source preservation | PASS | Full-file equality after replacing only target block; all surrounding bytes unchanged. |

Overall: **PASS**. Project-wide build, separate LeanEval, cumulative gates,
and commit/push are the parent agent's responsibility, not claimed here.

New identifier verification: `MvPolynomial.notMem_support_of_degreeOf_lt`
confirmed by native local search, untruncated source search at Degrees:288,
Loogle type, isolated compilation, module build, and live LSP.

Before: 6 declaration lines / 4 body lines. After: 5 / 3. Saved: 1 line.
Rules applied: 1.10 and mathlib API reuse; obsolete lambda eliminated.
Renames queued: none. Comments preserved: no inline comments existed;
docstring and source reference preserved exactly. Refactoring needed: none.

## Required phase checklist

- [✓] Step 1 — reference documents read.
- [✓] Step 2 — complete 24-item audit recorded.
- [✓] Step 2.5 — all five search methods attempted, service/index limitations explicit.
- [✓] Step 2.6 — every parameter assessed, actual weakening/counterexample probes, public literature search.
- [✓] Step 2.7 — every signature line measured with arithmetic.
- [✓] Step 2.8 — inequality scan table recorded.
- [✓] Step 3 — all 42 rule statuses recorded with actual applicable attempts.
- [✓] Step 4 — alternative proof/reflection completed.
- [✓] Step 5a — complete live diagnostics, baseline warning only.
- [✓] Step 5b — proof/type/axiom/module/diff gates pass.
- [✓] Step 6a — no rename necessary; shared queue untouched.

## Dependent checkpoint validation

The file owner ran `lake build` (2586 jobs) and `lake build Roth.LeanEval`
(2585 jobs), sequentially; both exited 0. Logs:
`/private/tmp/roth-hasseDeriv_eq_zero_of_degreeOf_lt-build.log` and
`/private/tmp/roth-hasseDeriv_eq_zero_of_degreeOf_lt-leaneval.log`.
