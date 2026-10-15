# Phase 4 — `MvPolynomial.hasseDeriv_monomial_mul`

Date: 2026-10-15. Worker: decl21. Scope: only this private declaration in
`Roth/HasseDeriv.lean`, lines 222–236 before, 222–234 after. Baseline supplied by
orchestrator: `9860b48`, first 20 declarations complete. No Git actions or shared
logs modified. Statement, definitions, imports, and toolchain unchanged.

## Step 1 — references

Read installed Lean 4 and mathlib-quality skills, the complete Phase-4 worker
prompt in `/Users/ramin/.local/share/roth-mathlib-quality/commands/cleanup.md`,
and `golfing-rules.md`, `proof-patterns.md`, `mathlib-search.md`,
`generalisation-patterns.md`, `cleanup-gates.md`, relevant `style-rules.md`
sections, and `naming-conventions.md` from the installed mathlib-quality skill.
Conflicting older examples defer to the current worker prompt and direct task
constraints. No substantial signature/definition/structure proposal is warranted.

## Step 2 — complete 24-slot audit

| # | Audit | Finding and resolution |
|---|---|---|
| 1 | LINT | No declaration-local warning. Complete final LSP reports only the existing file copyright-header warning. |
| 2 | HAVE SCAN | `hc` at old L227: typed term proof, used once at L234; inline in `rw` with its expected equality type. `hs` at old L229: tactic proof, used once; retain the mathematical subtraction step and simplify its cases. |
| 3 | SET_OPTION | None in this declaration; no limits introduced. |
| 4 | SIMP SQUEEZE | Coefficient, support-case, and add-case `simp` calls are terminal. Original nonterminal `simp only` plus `ring_nf` replaced by explicit rewrites followed by terminal `simp`. No unsqueezed nonterminal `simp` remains. |
| 5 | NAMING | `hasseDeriv_monomial_mul` describes the derivative of multiplication by a monomial, preserves the existing operator's camelCase component, and contains no forbidden abbreviation or numeric scheme. No rename required. |
| 6 | LINE PACKING | Both signature lines measured below: 92 and 98 codepoints. The next binder would make line 1 length 115. |
| 7 | BY PLACEMENT | All tactic `by` tokens stay at the end of their preceding line. |
| 8 | FORMAT | Two-space proof indentation, normal case arrows, lambda uses `↦`, no blank lines inside declaration, no `haveI`/`letI`. |
| 9 | COMMENTS | None present in this proof; none deleted. |
| 10 | DOCSTRING | Private helper, no docstring required or added. |
| 11 | VISIBILITY | Already private, retained. |
| 12 | STRUCTURE | 13 declaration lines, 11 proof-body lines after cleanup; monomial branch body 7 lines, add branch 1 line, support branches each close with the same terminal tactic. No conjunction or oversized branch. |
| 13 | MATHLIB | Five methods executed; only univariate Hasse analogues and existing generic product congruence API found. Bounded exact/apply search timed out, so no exhaustive mathematical absence claim is made. |
| 14 | JUNK DEF | n/a: declaration is a lemma. |
| 15 | EXISTS LEMMA | n/a: conclusion is equality, not an existential witness wrapper. |
| 16 | SHOW vs CHANGE | New `show ... from Finset.prod_congr ...` is term mode within `rw`, fixing the equality type of the inlined proof; not a tactic-mode goal change. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | Every parameter considered below. Dropping `ha` is refuted by a compiled concrete example; dropping/weakening `CommSemiring` fails the existing definition's class requirement. |
| 19 | INEQUALITY | No inequality relations in signature or hypotheses; scan table below. |
| 20 | NORMAL-FORM | Applied derivative of a product rewrites to multiplication by the independent factor. Canonical equation direction already suitable. |
| 21 | SYNTAX-GEN | OK: support-local hypothesis directly matches the coefficient computation and the following theorem's monomial induction. A disjoint-support restatement is equivalent and offers no necessary application improvement here. |
| 22 | IMPORT-FANOUT | n/a: no imports added. |
| 23 | CASTS | 0 dropped / 0 added cross-type / 0 added load-bearing casts. The inlined equality's `show` supplies an expected proposition, not a numeric cast. |
| 24 | INSTANCE-NAME | n/a: no instance declarations. |

Issues fixed: lambda arrow, single-use `hc`, support-case duplication, and the
terminal normalization sequence. Refactoring needed: none. No automatic deferrals.

## Step 2.5 — five-method search status

| Method | Actual query/evidence | Outcome |
|---|---|---|
| A Lean-Finder | `Multivariate polynomial Hasse derivative multiplication by a monomial with disjoint support` | Returned `Polynomial.hasseDeriv_mul`, `Polynomial.hasseDeriv_monomial`, `Polynomial.hasseDeriv_apply`, `MvPolynomial.X_mul_pderiv_monomial`, and `Polynomial.hasseDeriv_coeff`; none is this multivariate identity. |
| B Loogle | `"hasseDeriv", _ * _` | Univariate coefficient, application, monomial, and product rules. |
| C LeanSearch | `Hasse derivative multiplication by monomial independent variables` | HTTP 500; bounded attempt recorded, no retry loop. |
| D Source search | Untruncated `rg -n 'hasseDeriv_monomial_mul|hasseDeriv_mul|prod_congr|add_tsub.*disjoint'` over Polynomial/HasseDeriv, MvPolynomial sources, Finsupp/Order | Univariate product rule and generic `Finset.prod_congr`/`Finsupp.prod_congr` uses; no full-name match for target in those mathlib sources. |
| E Name pattern | `lean_local_search("hasseDeriv_monomial")` | Local target, local monomial formula, and `Polynomial.hasseDeriv_monomial`; index unavailable, so not evidence of absence. |

Auxiliary variants: monomial, product, product congruence, and disjoint subtraction.
Common-equivalents table: no match (none of the discrete/finite/bounded predicates
occurs). Conclusion: partial univariate analogues only; retain the local proof on
the existing multivariate API plus `Finset.prod_congr`. No replacement was found.
Whole-goal `exact?` and `apply?` were actually tried in the live context and reached
the default 200000-heartbeat bound. This bounds the search evidence; it does not
certify global absence. No new API declaration is introduced or claimed absent.

Six replacement rules checked: not a 1–3-call wrapper; all five methods attempted;
auxiliary variants searched; no custom predicate replacing a typeclass; no exact
equivalent found to delete; no new mathlib dependency needing module documentation.

## Step 2.6 — per-parameter generalisation

| Parameter | Class | Use | Mechanical candidates and verification | Result |
|---|---|---|---|---|
| `{σ : Type*}` | Type | Variables and finitely supported exponents | Drop impossible while retaining dependent types; already universe-polymorphic. No finite/decidable restriction to weaken. | Retain. |
| `{R : Type*}` | Type | Coefficients and polynomial codomain | Drop impossible while retaining `c` and `g` types; already universe-polymorphic. | Retain. |
| `[CommSemiring R]` | Typeclass | Existing `hasseDeriv` signature and multiplication | Isolated elaboration with `[Semiring R]`, and separately with no class, both fail `failed to synthesize CommSemiring R`. No stronger ring/field hypotheses are present. | Retain; no definition redesign requested. |
| `{d : σ →₀ ℕ}` | Structure value | Derivative order and support | Drop would remove the mathematical order from the conclusion. Natural exponents are intrinsic to the existing polynomial API. | Retain. |
| `{a : σ →₀ ℕ}` | Structure value | Monomial exponent and independence hypothesis | Drop would remove the factor's exponent from the conclusion. No concrete specialization to weaken. | Retain. |
| `(ha : ∀ j ∈ d.support, a j = 0)` | Proposition | Coefficient invariance and subtraction identity | Drop tested semantically: a compiled counterexample with `σ = Unit`, `R = ℕ`, `a = d = single () 1`, `c = 1`, `g = monomial 0 1` proves the equality false. Already localized to the support; no strict order to weaken. | Essential. |
| `(c : R)` | Structure value | Arbitrary scalar coefficient of factor | Drop loses the arbitrary coefficient in the conclusion; type follows `R`, no assumptions on `c`. | Retain. |
| `(g : MvPolynomial σ R)` | Structure value | Arbitrary polynomial being differentiated | Drop loses the polynomial in the conclusion; already arbitrary. | Retain. |

The two class probes were isolated `lean_run_code` elaborations; they were never
applied to the protected source. The drop-`ha` test is a certified counterexample,
stronger than observing the old proof fail. Data-parameter removal would be a
different, ill-formed contract rather than a hypothesis weakening.

Inversion check: not applicable. This is already a generic theorem over arbitrary
variables, coefficients, and exponents. Its proof uses the specific Hasse
coefficient and truncated-exponent formula throughout the monomial case.
Big-change candidates: none warranted. Literature: n/a — private declaration;
public literature search not required. Optional ChatGPT math tool skipped as instructed.

## Step 2.7 — signature width

Isolated `#check @hasseDeriv_monomial_mul` with `format.width = 100`:

```lean
@hasseDeriv_monomial_mul : ∀ {σ : Type u_3} {R : Type u_4} [inst : CommSemiring R] {d a : σ →₀ ℕ},
  (∀ j ∈ d.support, a j = 0) →
    ∀ (c : R) (g : MvPolynomial σ R), (hasseDeriv d) ((monomial a) c * g) = (monomial a) c * (hasseDeriv d) g
```

| Signature line | Codepoints | Next token | Arithmetic | Action |
|---|---:|---|---|---|
| 222 | 92 | `(g : MvPolynomial σ R)` (22) | 92 + 1 + 22 = 115 > 100 | ok |
| 223 | 98 | no next signature line | n/a; includes complete conclusion and `:= by` | ok |

Measured before and after: 92/98, unchanged. Maximum declaration line width: 98.

## Step 2.8 — inequality scan

| Location | Original | Rewrite | Rename |
|---|---|---|---|
| Complete signature and hypotheses, including local `hs` | n/a: no `≥`, `>`, `≤`, or `<` relation | none | no `_ge_`/`_gt_` in name |

Pattern-match `=>` and tactic `<;>` are syntax, not inequality occurrences.

## Step 3 — all 42 golfing rules

| Rule | Status |
|---|---|
| 1.1 | n/a: no `by exact` wrapper. |
| 1.2 | n/a: no `by rfl`. |
| 1.3 | n/a: no `rw` followed by `exact`. |
| 1.4 | n/a: no `simp` followed by `exact`/assumption. |
| 1.5 | n/a: no trailing `rfl`. |
| 1.6 | n/a: no constructor proof. |
| 1.7 | n/a: no apply/exact pair. |
| 1.8 | n/a: no contradiction/push-negation pair. |
| 1.9 | n/a: coefficient lambda uses both bound variables in a proof, not eta-reducible. |
| 1.10 | Applied: inline single-use typed term `hc` into the rewrite list. |
| 1.11 | n/a: no apply/intro pair. |
| 1.12 | New `show` is necessary term-mode expected-type annotation for product congruence; no tactic-mode redundant `show`. |
| 1.13 | n/a: no projections from a conjunction/existential `have`. |
| 1.14 | Applied in result: three monomial rewrites and coefficient proof in one `rw`. |
| 1.15 | Applied in resulting terminal step: final `simp` is unsqueezed after removing `ring_nf`. |
| 1.16 | n/a after cleanup: no nonterminal bare `simp`. |
| 1.17 | n/a: no useful dot-notation substitution; `Finset.prod_congr` is a constructor of the equality. |
| 1.18 | n/a: no avoidable trailing lambda/tactic parentheses or `$`. |
| 1.19 | n/a: no `push_neg`. |
| 1.20 | n/a: not an existential helper. |
| 2.1 | Whole `grind` tried live; failed. Targeted grind with explicit local `hc` was rejected as redundant local parameter; no benefit over successful simp. |
| 2.2 | n/a: no grind retained and no preliminary grind scaffolding. |
| 2.3 | Tested terminal simplification consolidation: `simp [monomial_mul_monomial, hc, hs, mul_left_comm]` closes the old algebra goal, making subsequent `ring_nf` redundant. Final proof uses that same terminal simp after inlining `hc`. |
| 2.4 | n/a: no analytic function-property goal. |
| 2.5 | n/a: no positivity goal. |
| 2.6 | n/a: no inequality monotonicity goal. |
| 2.7 | Isolated pointwise arithmetic analogue `a = 0 ∨ d = 0 → a + b - d = a + (b - d)` closes with `lia`; support case split plus simp_all is shorter in the actual finsupp context. |
| 2.8 | Whole `aesop` tried live; exhaustive search failed, normalized support premise only. |
| 2.9 | n/a: no concrete numerical/cast normalization in target proof. |
| 2.10 | n/a: equality over arbitrary polynomial/semiring data is not closed finite computation. |
| 2.11 | n/a: no denominators. |
| 2.12 | Tried `linear_combination` after the original simp; tactic unavailable under the current imports. Successful `mul_left_comm` simplification removes the ring goal without an extra import. |
| 2.13 | n/a: support-membership cases are zero-coordinate alternatives, not symmetry-related cases admitting wlog. |
| 2.14 | n/a: no calc block. |
| 2.15 | Applied: both support cases close with `<;> simp_all`. |
| 3.1 | n/a: no `erw`. |
| 3.2 | n/a: no legacy continuity/measurability tactic. |
| 3.3 | Satisfied by 2.7: tried `lia`, no `omega` introduced. |
| 3.4 | n/a: no rcases/rfl pattern. |
| 3.5 | No attribute added: private helper with conditional support hypothesis serves one following proof; global automation registration not warranted. |
| 3.6 | Applied: terminal support-case simplification uses unsqueezed `simp_all`. |
| 3.7 | n/a: no heartbeat limit in target; none added. |

## Step 4 — proof experiments and reflection

The full statement needs polynomial induction: whole-proof grind, simp, and aesop
did not close it. Exact/apply search hit the default heartbeat bound. Retaining
induction keeps the proof aligned with the defining monomial formula. Its two
substantive facts are coefficient invariance and subtraction on disjoint
coordinates. Inlining the first and simplifying the second yields a short branch
without introducing a separate helper or changing the mathematical API.

Actual experiments:

- Initial direct-helper `lean_multi_attempt` at a term line was incorrectly positioned
  and reported unknown identifiers; it was not counted as a tactic test. Corrected
  native live-file calls at L224 and L234 supplied the results recorded above.
- Bounded helper calls at valid positions timed out once; corrected native calls
  completed. No repeated timeout loops or increased limits.
- Candidate initially compiled its proof and standard axiom check but had an unused
  simp argument and an invalid diagnostic option `pp.width`. Removed the unused
  `Finsupp.notMem_support_iff` argument and used `format.width`; final isolated
  `lean_run_code` returned `success: true`, `timed_out: false` with only requested
  information messages.
- The first concrete drop-hypothesis test over-simplified the constant monomial;
  correcting the test to rewrite the monomial derivative formulas first produced
  a certified counterexample. Its scratch-only long-line warning is not in source.
- Final isolated source prefix plus the exact candidate returned the unchanged
  theorem type and `[propext, Classical.choice, Quot.sound]` from `#print axioms`.

New-identifier check: `mul_left_comm` verified via compiled `#check`; all other
identifiers are existing source dependencies. `rw`, `simp_all`, and lambda syntax
were elaborated in the isolated and final module checks.

## Step 5 — verification and gates

Complete native `lean_diagnostic_messages` on the final file:
`success: true`, `partial: false`, `timed_out: false`, `failed_dependencies: []`.
Only diagnostic is the pre-existing copyright-header warning at line 1.

Actual module build: `lake build Roth.HasseDeriv`, session 94305, exited 0;
`Built Roth.HasseDeriv (18s)`, `Build completed successfully (1430 jobs)`.
Only the same copyright warning. Parent handles full dependent/project builds.

Contextual patch had fresh source read and at least three surrounding context
lines. Comparison against `/private/tmp/decl21-before.lean` confirms signature
byte equality and scope containment; no whole-file overwrite.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | ✓ pass | Actual `lake build Roth.HasseDeriv`, session 94305, exit 0. |
| definition_protected | ✓ pass | No definition or abbreviation changed. |
| theorem_statement_protected | ✓ pass | Before/after signature string comparison true. |
| structure_gate | ✓ pass | 11 body lines, longest branch 7, no statement conjunction. |
| naming_gate | ✓ pass | Descriptive operator/monomial/product name, no forbidden patterns. |
| line_packing_gate | ✓ pass | Complete 92/98-codepoint table; 115-codepoint proposed binder append rejected. |
| inequality_orientation_gate | ✓ pass | No reverse inequality occurrences; table complete. |
| proof/type/axiom check | ✓ pass | Exact candidate isolated-compiled; expected signature, standard axioms only. |
| local downstream compatibility | ✓ pass | Whole declaring module, including its private helper's consumer, builds. |

Overall: pass. Full project and cumulative checks remain the orchestrator's assigned
work, not a missing worker check.

## Step 6 — result and checklist

Before: 15 declaration lines. After: 13. Saved: 2 lines.
Proof body: 13 → 11 lines. Four punch-list issues fixed. Refactoring deferred: 0.
Rules applied: 1.10, 1.14, 1.15, 2.3, 2.15, 3.6 plus lambda-arrow style.
Renames queued: none. Comments preserved: none present. Refactoring needed: none.

- [✓] Step 1 — required references read.
- [✓] Step 2 — all 24 audit items recorded.
- [✓] Step 2.5 — all five search methods attempted with outcomes and limitations.
- [✓] Step 2.6 — every parameter, weakening, and private-literature scope recorded.
- [✓] Step 2.7 — all signature lines measured in codepoints.
- [✓] Step 2.8 — complete inequality scan table.
- [✓] Step 3 — every one of 42 golfing rules has a status.
- [✓] Step 4 — whole-proof and targeted experiments, reflection recorded.
- [✓] Step 5a — complete LSP verification, only pre-existing header warning.
- [✓] Step 5b — actual module build and all worker gates pass.
- [✓] Step 6a — no rename action needed; no shared sidecar modified.

## Dependent checkpoint validation

The file owner ran `lake build` (2586 jobs) and `lake build Roth.LeanEval`
(2585 jobs), sequentially; both exited 0. Logs:
`/private/tmp/roth-hasseDeriv_monomial_mul-build.log` and
`/private/tmp/roth-hasseDeriv_monomial_mul-leaneval.log`.
