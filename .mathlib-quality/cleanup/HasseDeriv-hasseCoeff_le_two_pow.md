# Phase 4 — `MvPolynomial.hasseCoeff_le_two_pow`

Scope: only `Roth/HasseDeriv.lean:273–277`; baseline `9052f39`, first 24 declarations already complete. Worker changes only the target proof and this report. No Git operations, shared logs, other declarations, statements, definitions, imports, versions, or public documentation were changed.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md in full, together with the installed Lean 4 and mathlib-quality skills, Phase 4 procedure, relevant style rules, and naming conventions.

## Full audit

| # | Item | Finding and action |
|---|---|---|
| 1 | LINT | No target warning. Full final LSP and module build retain only the pre-existing copyright-header warning at line 1. |
| 2 | HAVE SCAN | No `have` declarations. |
| 3 | SET_OPTION | No declaration-local options or resource-limit overrides. |
| 4 | SIMP SQUEEZE | No simp invocation in retained proof. Terminal `simpa` alternative was tested successfully but needs more explicit arguments. |
| 5 | NAMING | `hasseCoeff_le_two_pow` identifies its subject, relation, and bound; the subject token matches `hasseCoeff`. No forbidden abbreviation or numerical scheme pattern, no `_ge_`/`_gt_`, no rename needed. |
| 6 | LINE PACKING | Measured signature widths 92 and 41 codepoints; next token would produce 103. Full table below. |
| 7 | BY PLACEMENT | `:= by` at the end of the conclusion line. |
| 8 | FORMAT | Fixed mathematical lambda `=>` to `↦`; two-space proof indentation, no internal blank line, one tactic per line, no `haveI`/`letI`. |
| 9 | COMMENTS | No proof-body comments; existing public docstring and source citation preserved verbatim. |
| 10 | DOCSTRING | Existing description identifies the bound on the coordinate box and cites source §3, Lemma 3. Preserved under the task's documentation constraint. |
| 11 | VISIBILITY | Public API used twice in `Roth/CoeffNorm.lean`, at lines 150 and 173. Public visibility justified. |
| 12 | STRUCTURE | Three proof-body lines; no conjunction or case branches; no extraction required. |
| 13 | MATHLIB | Partial match: `Nat.choose_le_two_pow`; retained proof already uses it with product monotonicity and power monotonicity. Search details below. |
| 14 | JUNK DEF | n/a: theorem, not a definition. |
| 15 | EXISTS LEMMA | n/a: no existential assertion or private witness helper. |
| 16 | SHOW vs CHANGE | n/a: neither construct occurs. |
| 17 | PUSH_NEG | n/a: no negation-normalization tactic. |
| 18 | GENERALISE | Every parameter examined below. Summed-bound companion compiled and presented; user explicitly chose to keep the current API. Existing statement unchanged. |
| 19 | INEQUALITY | Both occurrences are `≤`; no reversed inequality or reversed name. Full table below. |
| 20 | NORMAL-FORM | Canonical natural-number inequality with coefficient on the left and power of the total box bound on the right. |
| 21 | SYNTAX-GEN | Current pointwise hypothesis fits both existing coefficient-norm callers. `k ≤ r` after coercion would merely repackage it. Optional total-sum bound has mathematical extra scope, not just syntactic compression. |
| 22 | IMPORT-FANOUT | n/a: no new imports. |
| 23 | CASTS | 0 dropped, 0 kept cross-type, 0 kept load-bearing: no casts or ascriptions in the diff. |
| 24 | INSTANCE-NAME | n/a: theorem, no instance declaration. |

Issues fixed: one mathematical-lambda style issue. No proof compression improves the current three-line argument. No cross-declaration edits required for routine cleanup.

## Mathlib search status

| Method | Query / action | Result |
|---|---|---|
| A — Lean-Finder | `product binomial coefficients bounded by two to sum of upper indices` | Native tool returned read timeout. Recorded unavailable; no absence claim inferred and no repeated request. |
| B — Loogle | `Nat.choose _ _ ≤ 2 ^ _` | Found `Nat.choose_le_two_pow` and `Nat.choose_succ_le_two_pow`. |
| C — LeanSearch | `binomial coefficient bounded above by two to the power of upper index` | One native request returned HTTP 500; no retry. |
| D — source search | `choose_le_two_pow`, `prod_pow_eq_pow_sum`, `prod_le_prod`, and adjacent bounds | Located and read `Data/Nat/Choose/Bounds.lean`, `Algebra/BigOperators/Group/Finset/Basic.lean`, and the order/product API. |
| E — local name pattern | `choose_le_two_pow` | Found `Nat.choose_le_two_pow` and `Nat.choose_succ_le_two_pow`; index was warming, positive hits confirmed by source and `#check`. |

Auxiliary variants checked: `Nat.choose_lt_two_pow`, `Nat.choose_succ_le_two_pow`, `Nat.pow_le_pow_right`, and general `Finset.prod_le_prod`. Common-equivalents table: no discrete/finite/topological substitute matches this combinatorial coefficient estimate.

Conclusion: partial mathlib match, already used directly. This is an API fact about the project's `hasseCoeff`, requiring its product formula, product monotonicity, the scalar binomial bound, exponent monotonicity, and the product/power identity. It is not an exact duplicate found in mathlib or a 1–3-call wrapper. `exact?` failed on the live original goal; `apply?` generated generic order reductions, not a closing theorem. No global absence claim or new declaration is made.

## Generalisation status

| Parameter | Class | Use | Candidate / evidence | Result |
|---|---|---|---|---|
| `{σ : Type*}` | type / universe | Domain of all functions and finite sum | Already universe polymorphic (`Type u_1` confirmed by `#check @...`); deletion leaves domains undefined. | Retain; no universe restriction to weaken. |
| `[Fintype σ]` | typeclass | `∑ j, r j` and `∏ j` | Isolated substitution `[Finite σ]` fails to synthesize `Fintype σ` in statement and proof. Dropping even the `Finite` assumption cannot supply the missing enumeration. Finite-support formulation would restate the bound. | Retain for current formula; no safe drop. |
| `{d : σ →₀ ℕ}` | structure value | Lower binomial indices, coefficient subject | Deletion leaves `hasseCoeff d k` unbound. Ordinary-function domain requires redefining the coefficient API; that earlier proposal is outside this worker. | Retain. |
| `{k : σ →₀ ℕ}` | structure value | Upper indices and comparison hypothesis | Deletion leaves coefficient and hypothesis unbound. Natural-number codomain is essential to `Nat.choose`; an abstract-ring replacement would be a different construction. | Retain. |
| `{r : σ → ℕ}` | structure value | Box and power exponent | Deletion leaves hypothesis and conclusion unbound. Already an unrestricted function, not needlessly finite-support. | Retain. |
| `(hk : ∀ j, k j ≤ r j)` | proposition | Each exponent comparison | Drop is false: compiled counterexample on `Unit`, `d=single () 1`, `k=single () 2`, `r=0` has coefficient 2 and bound 1. Already weak inequality, no strict-to-weak change. Summed hypothesis `∑ j, k j ≤ ∑ j, r j` verified in isolated Lean; this changes the public call signature. | Existing hypothesis retained; optional companion presented and declined by user. |
| Ambient `{R}` / `[CommSemiring R]` | excluded section variables | None | Fully explicit `#check` shows neither is included in this theorem. | Already omitted by Lean; no source change needed. |

Global-to-pointwise catalogue: the sole proposition already supplies coordinatewise inequalities. A support-restricted hypothesis would be another API variant requiring a different proof and would add no convenience to current callers, which provide full degree boxes. No continuity, integrability, injectivity, strict-positivity, or bundled algebraic assumptions apply.

Inversion check: after the first product rewrite, `hasseCoeff` disappears. The remaining abstraction is exactly existing product monotonicity plus `Nat.choose_le_two_pow`; extracting a new abstract helper would duplicate that API. The substantive summed-bound observation is recorded separately below.

### Literature search

Query: `binomial coefficient bound 2^n binomial theorem generalization DLMF`.
Top three hits: [DLMF §1.2](https://dlmf.nist.gov/1.2), [DLMF §17.2](https://dlmf.nist.gov/17.2), and [DLMF §26.3](https://dlmf.nist.gov/26.3).
Opened §1.2 and §26.3. [DLMF (1.2.3)](https://dlmf.nist.gov/1.2.E3) gives the sum of all binomial coefficients as `2^n`. The single-coefficient bound, followed by multiplication over coordinates, is an inference from this identity. §17.2 concerns q-binomial coefficients and does not justify changing this theorem's natural-number coefficient construction.

Read local source `.mathlib-quality/references/clean.tex:446–465`: Lemma 3 uses the product of scalar binomial bounds on the coordinate box. Thus the existing API matches the source's actual application.

ChatGPT math MCP: skipped as explicitly allowed by the parent dispatch.

### Concrete proposal — declined by user

An optional companion `hasseCoeff_le_two_pow_of_sum_le` could require only
`∑ j, k j ≤ ∑ j, r j`. This accepts exponent vectors such as `k=(2,0)`, `r=(1,1)` that do not satisfy the coordinatewise assumption. The following isolated example compiled successfully:

```lean
example {σ : Type*} [Fintype σ] {d k : σ →₀ ℕ} {r : σ → ℕ}
    (hk : ∑ j, k j ≤ ∑ j, r j) : MvPolynomial.hasseCoeff d k ≤ 2 ^ (∑ j, r j) := by
  exact (MvPolynomial.hasseCoeff_le_two_pow (d := d) (fun _ ↦ le_rfl)).trans
    (Nat.pow_le_pow_right two_pos hk)
```

Sent promptly to parent; root presented the optional companions as a bundled user choice and recommended retaining the current API. The user answered: “Keep the current API as you recommend.” The candidate was considered and compiled in scratch, then explicitly declined. Neither this new theorem nor a statement change was implemented; no decision or refactoring remains pending.

## Line packing

`#check @MvPolynomial.hasseCoeff_le_two_pow` with `format.width 100`:

```text
@MvPolynomial.hasseCoeff_le_two_pow : ∀ {σ : Type u_1} [inst : Fintype σ] {d k : σ →₀ ℕ} {r : σ → ℕ},
  (∀ (j : σ), k j ≤ r j) → MvPolynomial.hasseCoeff d k ≤ 2 ^ ∑ j, r j
```

| Signature line | Codepoints | Next token | Arithmetic | Action |
|---|---:|---|---|---|
| 273 | 92 | `hasseCoeff` (10) | 92 + 1 + 10 = 103 > 100 | ok |
| 274 | 41 | none; proof follows | n/a | ok |

Measured before and after; signature byte-identical. Proof widths after edit: 55, 37, 75 codepoints. No line exceeds 100.

## Inequality scan

| Occurrence | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 1 | `hk`, line 273 | `k j ≤ r j` | none; forward orientation | none |
| 2 | conclusion, line 274 | `hasseCoeff d k ≤ 2 ^ (∑ j, r j)` | none; forward orientation | none |
| reversed scan | full signature | no `≥` or `>` | n/a | no `_ge_` / `_gt_` |

## Golfing rule pass — all 42 rules

| Rule | Status |
|---|---|
| 1.1 | n/a: no `by exact` wrapper. |
| 1.2 | n/a: no `by rfl`. |
| 1.3 | Tried rewrite/closing-proof consolidation via `simpa`; successful but needs explicit indices and univ, so retain direct proof. |
| 1.4 | n/a: retained proof has no simp/exact chain. |
| 1.5 | n/a: no simp followed by rfl. |
| 1.6 | n/a: no constructor. |
| 1.7 | Already direct `exact Finset.prod_le_prod ...`; no apply/exact pair. |
| 1.8 | n/a: no contradiction proof. |
| 1.9 | Lambda body composes two bounds and depends on `j`; no eta-redex. Lambda arrow corrected. |
| 1.10 | n/a: no have. |
| 1.11 | n/a: no apply/intro chain. |
| 1.12 | n/a: no show. |
| 1.13 | n/a: no projections from a named conjunction. |
| 1.14 | Already one combined rewrite invocation. |
| 1.15 | n/a: no simp only. |
| 1.16 | n/a: no nonterminal simp retained. |
| 1.17 | Already `.trans` composition. |
| 1.18 | n/a: no trailing parenthesized function argument needing `<|`; `.trans` argument is short. |
| 1.19 | n/a: no push_neg. |
| 1.20 | n/a: no existential helper. |
| 2.1 | Tried live `grind`; failed to derive the coefficient inequality. |
| 2.2 | n/a: no grind in retained proof. |
| 2.3 | Tried terminal `simpa [hasseCoeff_eq_prod, Finset.prod_pow_eq_pow_sum] using ...`; passes, same line count, more explicit parameters. |
| 2.4 | n/a: no function-property goal. |
| 2.5 | n/a: no positivity goal; `two_pos` directly supplies the scalar premise. |
| 2.6 | Tried `rw [...]`, `gcongr with j`, scalar bound; passes, same line count and more tactics than original. |
| 2.7 | Tried live `lia`; fails because abstract binomial/products are not linear arithmetic. |
| 2.8 | Tried live `aesop`; no progress. |
| 2.9 | n/a: no numerical evaluation or cast normalization goal. |
| 2.10 | n/a: symbolic arbitrary `σ`, `d`, `k`, `r`; no closed finite computation. |
| 2.11 | n/a: no denominator or field equality. |
| 2.12 | n/a: no ring-ending proof or polynomial equality. |
| 2.13 | n/a: no symmetric case branches. |
| 2.14 | Already uses `.trans` for the two scalar inequalities; no calc remains. |
| 2.15 | n/a: no repeated parallel goals. |
| 3.1 | Already rw; no erw. |
| 3.2 | n/a: no continuity/measurability tactic. |
| 3.3 | Already tested lia under 2.7; no omega introduced. |
| 3.4 | n/a: no rcases/substitution. |
| 3.5 | No attribute added: free upper-bound parameter makes this an application theorem, not a canonical simp normalization; no demonstrated automation need. |
| 3.6 | n/a: no simp_all only. |
| 3.7 | n/a: no resource-limit option. |

## Actual alternatives and step-back review

Native `lean_goal` at line 275 confirmed the complete local context and the rewrite to a product-versus-product inequality. Native `lean_multi_attempt` tested all following alternatives in that live context:

| Attempt | Result |
|---|---|
| `grind` | Failed. |
| `aesop` | Failed, no progress. |
| `simp [hasseCoeff_eq_prod]` | Leaves product bound; does not close. |
| `exact?` | No closing proof found. |
| `apply?` | Only partial generic order suggestions; no replacement accepted. |
| `lia` | Failed. |
| rewrite + `gcongr with j` + scalar `.trans` | Passed, three lines. |
| direct terminal `simpa` from explicit `Finset.prod_le_prod` | Passed, three lines, more arguments. |
| retained rewrite + direct product term with `↦` | Passed. |

The proof is already a direct statement of the mathematics: express the coefficient as a product, compare every binomial factor with a power of two, then combine the powers. Term-mode transport would obscure the two structural rewrites. No useful extraction, redundant have, or alternate one-tactic proof was found. Retained the simplest successful proof with the lambda style corrected.

## Verification and gates

Native full-file `lean_diagnostic_messages` after the edit: `success=true`, `partial=false`, no failed dependencies, no errors, only the inherited header warning at line 1. No target warnings.

Isolated `lean_run_code` redeclared the selected proof, checked `@checked = @MvPolynomial.hasseCoeff_le_two_pow` by `rfl`, and printed axioms: both have only `propext`, `Classical.choice`, `Quot.sound`. The temporary snippet had a leading-space style warning, unrelated to source, and an imports-out-of-date information message while the module build was running. Its proof/type verification succeeded. The subsequent module build completed successfully.

An initial pretty-printer probe used unsupported `pp.width`; this scratch-only error was corrected to `format.width 100`, and the corrected probe succeeded. No failed experiment was left in project source.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Actual `lake build Roth.HasseDeriv`; exec session 57111, final chunk `91c652`, exit 0, 1430 jobs; target built in 22s. |
| definition_protected | pass | Worker diff touches no definition or abbreviation. |
| theorem_statement_protected | pass | Parsed before/after text through `:= by` compared byte-identical. |
| structure_gate | pass | Three body lines, no conjunction or branches. |
| naming_gate | pass | Descriptive name, no forbidden pattern or abbreviation. |
| line_packing_gate | pass | Both signature rows measured, next token would exceed 100. |
| inequality_orientation_gate | pass | Both inequalities forward; zero reversed inequalities. |
| comments_preserved | pass | Entire docstring/source reference unchanged; no proof comments existed. |
| identifiers | pass | No new identifiers introduced. Existing scalar/product names independently found and checked. |

Overall: pass for existing-declaration cleanup. Parent owns cumulative full-project build, performance review, and publication.

## Result

Before: 5 declaration lines (3 proof lines). After: 5 declaration lines (3 proof lines). Saved: 0 lines. One `=>` replaced by `↦`; no mathematical change.

Audit issues found: 1. Fixed: 1. Refactoring needed: none. Optional companion: considered, compiled in scratch, and declined by user; not automatically deferred. Renames queued: none. Comments preserved: public documentation/source citation unchanged; no proof comments present.

Phase checklist:

- [x] Step 1 — required references read.
- [x] Step 2 — all 24 audit slots recorded.
- [x] Step 2.5 — all five search methods recorded, including explicit service failures.
- [x] Step 2.6 — every parameter audited; literature and compiled candidate recorded.
- [x] Step 2.7 — measured signature-width table.
- [x] Step 2.8 — inequality scan table.
- [x] Step 3 — all 42 golfing rules have a status.
- [x] Step 4 — alternate strategies tested and reviewed.
- [x] Step 5a — complete native LSP diagnostics, inherited header warning only.
- [x] Step 5b — gates and actual successful module-build evidence.
- [x] Step 6a — no renames required; no shared sidecar edited.

## Dependent checkpoint validation

The file owner ran `lake build` (2586 jobs) and `lake build Roth.LeanEval`
(2585 jobs), sequentially; both exited 0. Logs:
`/private/tmp/roth-hasseCoeff_le_two_pow-build.log` and
`/private/tmp/roth-hasseCoeff_le_two_pow-leaneval.log`.
