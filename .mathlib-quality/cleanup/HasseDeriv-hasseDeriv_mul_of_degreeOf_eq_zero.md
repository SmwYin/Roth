# Phase 4 — `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero`

Date: 2026-10-15. Worker: decl22. Baseline supplied by orchestrator: `044439e`,
first 21 declarations complete. Scope: only target declaration in `Roth/HasseDeriv.lean`
and this report. No Git operations, shared logs, other declarations, imports, definitions,
toolchain, or existing documentation changed. Before L240–245; after L240–244.

## Step 1 — required references

Read installed `lean4/SKILL.md`, `mathlib-quality/SKILL.md`, the Phase-4 worker
prompt in `/Users/ramin/.local/share/roth-mathlib-quality/commands/cleanup.md`, and
the installed mathlib-quality references `golfing-rules.md`, `proof-patterns.md`,
`mathlib-search.md`, `generalisation-patterns.md`, `cleanup-gates.md`, relevant
`style-rules.md` sections, and `naming-conventions.md`. All five mandatory full
reference documents were read; the generalisation reference was read again separately
after the combined output truncated its middle. Current worker instructions and
direct task constraints take precedence over conflicting older examples.

## Step 2 — complete 24-slot audit

| # | Audit | Finding and resolution |
|---|---|---|
| 1 | LINT | No declaration-local warning. Complete final LSP returned only existing file copyright-header warning. |
| 2 | HAVE SCAN | Old L242 `ha : ∀ a ∈ f.support, ∀ j ∈ d.support, a j = 0`: term proof, no `by`, one use at old L245. Inline its body at that use, eliminating the intermediate quantification over monomials. No other `have`. |
| 3 | SET_OPTION | None; no limits introduced. |
| 4 | SIMP SQUEEZE | n/a: target proof contains no simp call. |
| 5 | NAMING | `hasseDeriv_mul_of_degreeOf_eq_zero` names the multiplication identity and degree-zero premise, with the operator names retaining their camelCase components. No forbidden abbreviation, scheme number, `_ge_`, or `_gt_`. No rename required. |
| 6 | LINE PACKING | Both signature lines measured: 80/94 codepoints; adding next binder would give 121. Full table below. |
| 7 | BY PLACEMENT | `:= by` remains at end of conclusion line. |
| 8 | FORMAT | Two-space proof indentation; four-space expression continuation; both ordinary lambdas use `↦`; no interior blank line, trailing whitespace, `haveI`, or `letI`. |
| 9 | COMMENTS | No inline proof comments; none deleted. |
| 10 | DOCSTRING | Existing public docstring explains independence of the factor and cites §2, proof of Lemma 2; preserved byte-for-byte. |
| 11 | VISIBILITY | Public API used twice by `Roth.hasseDeriv_rename_mul_aeval` in `Roth/Separation.lean`; keep public. |
| 12 | STRUCTURE | Body 4 → 3 lines; no conjunction or branches; no extraction warranted. |
| 13 | MATHLIB | All five methods attempted. Univariate product rule is a partial analogue; generic degree and finite-sum APIs already used. No exact replacement found; search limitation recorded below. |
| 14 | JUNK DEF | n/a: a theorem, not a definition. |
| 15 | EXISTS LEMMA | n/a: conclusion is equality, not a trivial existential. |
| 16 | SHOW vs CHANGE | n/a: no `show` or `change`. |
| 17 | PUSH_NEG | n/a: no negation tactic. |
| 18 | GENERALISE | All parameters audited below; coefficient class cannot weaken under existing definitions, and dropping independence is disproved by compiled counterexample. |
| 19 | INEQUALITY | No inequality relations in signature or local hypotheses. Table below. |
| 20 | NORMAL-FORM | Applied derivative of product rewrites to the independent factor times derivative of the other factor. The support-local `degreeOf = 0` premise expresses the intended polynomial independence. |
| 21 | SYNTAX-GEN | OK: callers already discharge the degree premise directly using degree lemmas. A disjoint-variable-set restatement is equivalent but has no demonstrated call-site advantage. |
| 22 | IMPORT-FANOUT | n/a: no new imports. |
| 23 | CASTS | 0 dropped / 0 kept as cross-type / 0 kept as load-bearing: no explicit casts in changed proof. |
| 24 | INSTANCE-NAME | n/a: no instance declaration. |

Issues fixed: single-use `ha` and two ordinary lambda arrows. Refactoring needed:
none warranted. No signature or documentation proposal is needed for this cleanup.

## Step 2.5 — five-method mathlib search

| Method | Actual query/evidence | Result |
|---|---|---|
| A Lean-Finder | `Multivariate polynomial Hasse derivative product factor independent of variables degreeOf zero` | `Polynomial.hasseDeriv_mul`, `hasseDeriv_apply`, `hasseDeriv_natDegree_eq_C`, `hasseDeriv_coeff`; all univariate analogues. |
| B Loogle | `"hasseDeriv", _ * _` | Univariate coefficient/application/monomial/product rules, no exact multivariate identity. |
| C LeanSearch | `Hasse derivative product polynomial factor independent variables` | HTTP 500. One bounded attempt, no repeated retry or false no-hit claim. |
| D Source | Untruncated `rg` for target full name, `hasseDeriv_mul`, `degreeOf_eq_zero`, `monomial_le_degreeOf`, `degreeOf_eq` in mathlib Polynomial/HasseDeriv and MvPolynomial sources | Univariate product rule and degree/support API. Full target name has no hit in these sources. Read `Degrees.lean` L260–274 and downstream uses in `Separation.lean`. |
| E Name pattern | `lean_local_search("hasseDeriv_mul")` | Univariate product rule, project target and private monomial lemma, downstream rename/multiplication theorem. Index `warming`, so source hits are usable but an empty result would not prove absence. |

Auxiliary variants: monomial multiplication, coefficient formula, degree-of-zero,
support-degree bounds, and degree-of-sup. Common-equivalents table: no applicable
discrete/finite/bounded predicate. `#check @MvPolynomial.monomial_le_degreeOf`
and `#check @Polynomial.hasseDeriv_mul` compiled successfully in an isolated snippet.

Conclusion: partial univariate match only; retain the local multivariate theorem,
using `MvPolynomial.monomial_le_degreeOf`, `Finset.sum_congr`, `Finset.sum_mul`,
and `map_sum`. Live `exact?` did not close the initial goal; `apply?` stopped at its
existing time budget with unusable partial cancellation suggestions. This is bounded
search evidence, not a global absence certificate. No new declaration is introduced.

Six strict replacement rules considered: target is not merely a 1–3-call mathlib
wrapper because the essential monomial identity is project-local; five methods
attempted; auxiliary variants checked; no custom predicate duplicating a typeclass;
no exact equivalent found to delete; no new mathlib dependency requiring module-doc
changes. The final three-line proof has no cast plumbing, definitional-equality
bridge, repeated wrapper round-trip, or other API-extraction signal.

## Step 2.6 — generalisation status

| Parameter | Class | Use | Mechanical candidates and verification | Result |
|---|---|---|---|---|
| `{σ : Type*}` | Type variable | Polynomial variables and multi-index domain | Already independently universe-polymorphic; drop would leave dependent types unbound. No finite/decidable assumption to weaken. | Retain. |
| `{R : Type*}` | Type variable | Coefficient type | Already universe-polymorphic; drop would leave polynomial type and coefficient class unbound. | Retain. |
| `[CommSemiring R]` | Typeclass | `MvPolynomial`, `hasseDeriv`, product and finite sums | Isolated substitutions `[Semiring R]` and no class both fail `failed to synthesize CommSemiring R`. | Retain; changing underlying definitions is outside scope. |
| `{d : σ →₀ ℕ}` | Structure value | Arbitrary derivative multi-index and support | Already arbitrary; removing it loses the derivative order. Natural exponents belong to existing polynomial API. | Retain. |
| `{f : MvPolynomial σ R}` | Structure value | Independent factor and support expansion | Already arbitrary subject to `hf`; removal would lose a factor in the conclusion. | Retain. |
| `{g : MvPolynomial σ R}` | Structure value | Arbitrary differentiated factor | No hypothesis on `g`; removing it would lose the input in the conclusion. | Retain. |
| `(hf : ∀ j ∈ d.support, degreeOf j f = 0)` | Proposition | Bounds every supported monomial coordinate by zero | Drop refuted by compiled concrete counterexample: `σ = Unit`, `R = ℕ`, `d = single () 1`, `f = monomial d 1`, `g = monomial 0 1`. Identity gives a nonzero constant on left, zero on right. Already local to relevant coordinates; no strict inequality. Replacing natural equality-to-zero by `≤ 0` is equivalent, not a genuine weakening. | Essential for the uniform statement. |

The tests were isolated `lean_run_code` snippets, not changes to the protected source.
The counterexample proves the dropped statement false rather than merely showing
the current proof fails. Data parameter removal is not a meaningful weakening of
this contract. Inversion check: not applicable; the theorem is already parametric
and the proof specifically uses Hasse monomial multiplication and polynomial degrees.

### Public literature search

Web query: `Hasse derivative product rule independent variables Hasse Schmidt derivation`.
First three returned hits were the Hasse derivative encyclopedia entry, the research
paper *Algebraic independence over finite fields: Higher derivation based…*, and
the nLab Hasse-Schmidt derivative entry. Also inspected the primary-source abstract
of [Hazewinkel, *Hasse-Schmidt derivations and the Hopf algebra of noncommutative
symmetric functions*](https://arxiv.org/abs/1110.6108), which gives the general
Hasse-Schmidt product sum. nLab open returned unsupported XHTML content; search
snippet alone was not treated as a verified full reference.

Inference from the primary-source product rule: the factor-passing law holds when
the positive-order derivatives contributing from the factor vanish. A general
abstract Hasse-Schmidt product framework could express that observation. It is a
different API project; no concrete required abstraction or downstream improvement
is established for this short polynomial theorem, whose existing degree premise
is precisely what both callers know. No substantive change is proposed or silently
applied. Local source `clean.tex` §1 explicitly allows commutative semirings; §2,
Lemma 2 uses independent variable groups. The current theorem already removes the
source's finite-variable/integer-coefficient restrictions.

Optional ChatGPT math tool: skipped as instructed. Big-change candidates warranted
for this declaration: none. Small-safe generalisations applied: none. The separate
degree-subtraction proposal pending with the user belongs to another declaration.

## Step 2.7 — measured line packing

Isolated check at `format.width = 100`:

```lean
@hasseDeriv_mul_of_degreeOf_eq_zero : ∀ {σ : Type u_3} {R : Type u_4} [inst : CommSemiring R] {d : σ →₀ ℕ}
  {f g : MvPolynomial σ R}, (∀ j ∈ d.support, degreeOf j f = 0) → (hasseDeriv d) (f * g) = f * (hasseDeriv d) g
```

| Signature line | Codepoints | Next signature token | Arithmetic | Action |
|---|---:|---|---|---|
| 240 | 80 | `(hf : ∀ j ∈ d.support, degreeOf j f = 0)` (40) | 80 + 1 + 40 = 121 > 100 | ok |
| 241 | 94 | No next signature line; conclusion and `:= by` included | n/a | ok |

Measured before and after: 80/94 unchanged. Final proof lines: 56/64/82 codepoints.
Maximum target declaration line width: 94.

## Step 2.8 — inequality orientation

| Location | Original | Rewrite | Rename |
|---|---|---|---|
| Complete signature and hypotheses | n/a: zero `≥`, `>`, `≤`, or `<` relations | None | No `_ge_`/`_gt_` name |

Original local `ha` also had only equality and membership. `monomial_le_degreeOf`
uses the canonical smaller-left inequality; no reverse inequality added.

## Step 3 — all 42 golfing rules

| Rule | Status |
|---|---|
| 1.1 | n/a: no `by exact` wrapper. |
| 1.2 | n/a: no `by rfl`. |
| 1.3 | No rw/assumption consolidation: after rewriting, the closing equality must be constructed by sum congruence and the monomial lemma; rewrites alone do not supply it. |
| 1.4 | n/a: no simp/exact pair. |
| 1.5 | n/a: no trailing rfl after simp. |
| 1.6 | n/a: no constructor tactic. |
| 1.7 | n/a: no apply/exact pair. |
| 1.8 | n/a: no contradiction/push-negation pair. |
| 1.9 | Both retained lambdas use their arguments inside nested theorem applications; not eta-redexes. Changed syntax to `↦`. |
| 1.10 | Applied: inline the single-use term-valued `ha`. |
| 1.11 | n/a: no apply/intro pair. |
| 1.12 | n/a: no show. |
| 1.13 | n/a: no projections from have. |
| 1.14 | Already one combined rewrite list, no adjacent rw steps. |
| 1.15 | n/a: no terminal simp only. |
| 1.16 | n/a: no nonterminal simp. |
| 1.17 | Existing `f.as_sum` uses dot notation; no additional useful conversion. |
| 1.18 | Inner lambda is a non-final argument before `_ _`; its parentheses delimit the argument and cannot simply become `<|`. Outer lambda already omits parentheses. |
| 1.19 | n/a: no push_neg. |
| 1.20 | n/a: not an existential helper. |
| 2.1 | Whole-proof grind actually tried; failed on the product-derivative equality. |
| 2.2 | n/a: no grind retained, no preceding grind scaffolding. |
| 2.3 | n/a: no simp followed by another closing tactic. Whole-proof simp actually tried and made no progress. |
| 2.4 | n/a: no analytic function property. |
| 2.5 | n/a: equality-to-zero is inferred from an upper bound, not positivity/nonnegativity. |
| 2.6 | n/a: no monotonicity goal or inequality calc. |
| 2.7 | Actual isolated arithmetic analogue `a ≤ n → n = 0 → a = 0` closed with `lia`. Retained shorter direct `Nat.eq_zero_of_le_zero` proof term. |
| 2.8 | Whole-proof aesop actually tried; exhaustive search failed after normalizing support membership. |
| 2.9 | n/a: no concrete numeric or cast computation in target. |
| 2.10 | n/a: equality over arbitrary semiring polynomial parameters is not closed finite computation. |
| 2.11 | n/a: no denominators. |
| 2.12 | n/a: proof has no ring/ring_nf terminal algebraic identity. |
| 2.13 | n/a: no case branches or symmetric-case duplication. |
| 2.14 | n/a: no calc block. |
| 2.15 | n/a: no multiple tactic goals requiring repeated closure. |
| 3.1 | n/a: no erw. |
| 3.2 | n/a: no continuity/measurability tactic. |
| 3.3 | Satisfied by 2.7: lia tested; no omega present or introduced. |
| 3.4 | n/a: no rcases/rfl substitution. |
| 3.5 | No automation attribute added: conditional support premise requires supplied mathematical independence; current explicit rewrite uses are appropriate. |
| 3.6 | n/a: no simp_all only. |
| 3.7 | n/a: no local heartbeat option; none introduced. |

## Step 4 — experiments and reflection

Live `lean_goal` at L242 confirmed the expected context, including `hf`, before
the original `ha`. Live `lean_multi_attempt` tried grind, simp, aesop, exact?,
apply?, and the complete three-line inlined candidate. Single-line replacement
left the old multiline `have` continuation in some attempts, causing additional
`unexpected identifier` diagnostics; the first-tactic failures themselves are
reported above. The inlined candidate closed all goals and then reported `No goals
to be solved` for the remaining original proof. Neither artifact is counted as
a successful final compilation.

To verify the candidate independently, `lean_run_code` received the complete source
prefix through the preceding private helper plus the exact candidate declaration.
It returned `success: true`, `timed_out: false`, and only the requested `#check`
and `#print axioms` information. This avoids accidentally testing a term against a
different statement or assuming the original continuation is harmless.

The proof retains its mathematical two-step structure: expand the independent
factor as its sum of monomials, then apply the monomial multiplication law to
each supported exponent. The local degree-to-exponent implication now occurs
exactly where consumed. A one-tactic proof was not found. Term-mode equality
transport would obscure the four rewrites; no different proof strategy provides
a demonstrated improvement. No new lemma names were introduced.

## Step 5 — final verification and gates

Fresh target read immediately preceded a contextual `apply_patch` with at least
three surrounding lines. No whole-file write. Before/after target signature
string comparison returned `true`; declaration line count 6 → 5, body 4 → 3.

Final complete native `lean_diagnostic_messages` returned `success: true`,
`partial: false`, `timed_out: false`, `failed_dependencies: []`; only the existing
copyright-header warning at L1. Exact candidate's isolated `#print axioms`:
`[propext, Classical.choice, Quot.sound]`. No sorry or nonstandard axiom introduced.

Actual command `lake build Roth.HasseDeriv`, session 80261, exited 0:
`Built Roth.HasseDeriv (11s)`; `Build completed successfully (1430 jobs)`.
Only the same copyright warning. Source-finalized and module-complete notifications
sent to orchestrator before its dependent builds; no subsequent source edits.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | ✓ pass | Actual `lake build Roth.HasseDeriv`, session 80261, exit 0. |
| definition_protected | ✓ pass | No def/abbrev or other declaration changed. |
| theorem_statement_protected | ✓ pass | Exact before/after signature string comparison true. |
| structure_gate | ✓ pass | Body 3 lines, no conjunction or branches. |
| naming_gate | ✓ pass | Mathematical operation/premise name; no forbidden pattern. |
| line_packing_gate | ✓ pass | All signature lines measured, 80/94; binder append would be 121. |
| inequality_orientation_gate | ✓ pass | Complete scan, zero reversed inequalities or names. |
| proof/type/axioms | ✓ pass | Isolated exact candidate compiles; expected type and standard three axioms. |
| LSP | ✓ pass | Complete file diagnostics; only baseline header warning. |

Overall: pass. Full-project and dependent LeanEval gates are assigned to orchestrator.

## Step 6 — result and phase checklist

Before 6 declaration lines; after 5; saved 1. Two punch-list categories fixed:
single-use `ha` and ordinary lambda arrows. Rules applied: 1.10 plus lambda style.
Refactoring deferred: 0. Renames queued: none. Inline comments: none present.
Existing docstring and source citation preserved. Refactoring needed: none.

- [✓] Step 1 — required references read.
- [✓] Step 2 — all 24 audit slots recorded.
- [✓] Step 2.5 — five searches attempted with explicit outcomes/limitations.
- [✓] Step 2.6 — all parameters, mechanical probes, inversion and public literature recorded.
- [✓] Step 2.7 — complete measured signature-width table.
- [✓] Step 2.8 — complete inequality scan.
- [✓] Step 3 — all 42 golfing rules have statuses.
- [✓] Step 4 — actual whole-proof/targeted experiments and reflection recorded.
- [✓] Step 5a — complete final LSP, no new warning/error.
- [✓] Step 5b — actual module build and all diff gates pass.
- [✓] Step 6a — no rename needed; no shared rename sidecar modified.

## Dependent checkpoint validation

The file owner ran `lake build` (2586 jobs) and `lake build Roth.LeanEval`
(2585 jobs), sequentially; both exited 0. Logs:
`/private/tmp/roth-hasseDeriv_mul_of_degreeOf_eq_zero-build.log` and
`/private/tmp/roth-hasseDeriv_mul_of_degreeOf_eq_zero-leaneval.log`.
