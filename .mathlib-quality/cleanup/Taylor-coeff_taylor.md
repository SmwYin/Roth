# Declaration cleanup: `MvPolynomial.coeff_taylor`

Worker baseline: `4239ed6`; live starting lines 98–132 (35 declaration lines, 33 proof-body lines). Final target lines 130–134: 5 declaration lines, 3 proof-body lines. The target saves 30 lines; extraction adds two private declarations, so the whole file grows by 2 lines. This is structural improvement rather than a claim of net line savings.

Source frozen and handed to the file owner at SHA256 `339ca8621ef76a233dab2c5f86002e6a1016b9116616266e78b9a5d311177b39`. No edits to existing declarations other than the target; the previously audited three helpers remain untouched. No shared-log or Git operations by this worker.

## References and mathematical decomposition

Read the worker contract in full, lean4 and mathlib-quality skills, golfing-rules, proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates, applicable style-rules sections, and mathlib-review-stages normal-form/syntactic-generality/documentation sections. Conflicting generic recommendations to rewrite existing docstrings are superseded by the explicit instruction to preserve them.

The theorem says that translation converts a Hasse derivative evaluated at the translation point into the corresponding coefficient. Linearity reduces the statement to monomials. For a monomial, induction on its finitely supported exponent vector separates one variable; a univariate binomial expansion computes that variable's coefficient. The remaining variables have exponent zero in the separated coordinate, so the coefficient factors through erasing that coordinate.

Extracted private declarations, both checked by the compiler and axiom printer:

- `coeff_taylor_monomial_single_add_aux`: extends the coefficient formula when a previously absent variable with exponent `n` is adjoined. Its proof has 14 lines, with the support argument kept as a short local proof. It uses the project's three nontrivial coefficient/product lemmas and the univariate binomial theorem; it is not a wrapper around 1–3 mathlib calls.
- `coeff_taylor_monomial_aux`: proves the formula for an arbitrary monomial by exponent induction. Its proof has 9 lines; the zero branch has 5 lines, and the single-add branch calls the preceding lemma.

The parent will dispatch fresh dedicated declaration audits for these two helpers. This report audits the original headline theorem; it does not claim that the helpers have completed their independent audits.

## Full audit (24 items)

1. **LINT:** complete live LSP diagnostics contain no target-range warning/error. The preexisting file copyright-header warning remains at line 1.
2. **HAVE SCAN:** original line 109 anonymous zero-coefficient fact: no `by`, one use in the next `simp`; inlined in the monomial helper. Original `hi'` line 112: no `by`, used in the support arithmetic and both product/coefficient rewrites (three uses), so not a single-use candidate; replaced by the explicit `hi` parameter of the extracted step helper. Original `hXC` lines 113–115: has `by`, one use in `htay`; retained as a proof-bearing local equality in the step helper. Original `hsupp` lines 116–123: has `by`, one use; retained in the step helper and shortened. Its anonymous `hasseCoeff` equality has an internal `by`; replaced by a direct proof term inside terminal `simp`. Its inner `have := hle i` was a single arithmetic input and is eliminated by `le_zero_iff.1 (hi ▸ hle i)`. Original `htay` lines 124–127: has `by`, one use; eliminated by merging its rewrites into the main coefficient calculation. Final headline contains no `have`.
3. **SET_OPTION:** none before or after; no limit raises or profiling scaffolding introduced.
4. **SIMP SQUEEZE:** original additive/base/support/hXC `simp` calls were terminal, so no squeeze required. Final headline's additive `simp [hp, hq]` is terminal. New helpers also use only terminal `simp`; terminal `simp [mul_assoc, mul_comm, mul_left_comm]` replaces `push_cast; ring`.
5. **NAMING:** `coeff_taylor` names the coefficient operation on translation, is snake_case, and contains no forbidden abbreviation, numeric scheme pattern, `_ge_`, or `_gt_`. No rename required or queued.
6. **LINE PACKING:** measured target signature table below; unchanged signature, both rows pass.
7. **BY PLACEMENT:** `:= by` is at the end of the conclusion line.
8. **FORMAT:** two-space proof indentation, no internal blank lines, no semicolon chains, no `haveI`/`letI`; ordinary lambdas in relocated mathematics use `↦`, branch arrows keep `=>`.
9. **COMMENTS:** no original inline proof comments. All existing block comments and docstrings compare byte-identically before/after; no removals or relocations.
10. **DOCSTRING:** existing public docstring explains coefficient form and its relation to the polynomial Taylor theorem and cites the source. Its existing proof-strategy phrase is preserved under the explicit documentation lock.
11. **VISIBILITY:** headline result remains public: it is the coefficient API used by degree and expansion results. New implementation lemmas are private and have descriptive `_aux` names.
12. **STRUCTURE:** the headline's 33-line body and 29-line monomial branch are replaced by a 3-line linearity argument. Final branches are one line each, no conjunction. Exponent induction and variable-separation mathematics are factored into two private helpers; no decomposition deferral.
13. **MATHLIB:** five-method search below; partial univariate match retained as building block, no multivariate replacement identified.
14. **JUNK DEF:** n/a: target is a theorem, no definitions changed.
15. **EXISTS LEMMA:** n/a: no existential statement or witness wrapper.
16. **SHOW vs CHANGE:** n/a: neither occurs in the target or extracted proof.
17. **PUSH_NEG:** none before or after.
18. **GENERALISE:** every parameter checked below; typeclass drop and Semiring weakening fail because the existing multivariate polynomial API requires CommSemiring. No public signature changes proposed.
19. **INEQUALITY:** zero reversed inequalities in the signature or hypotheses; table below.
20. **NORMAL-FORM:** coefficient-of-translation on the left and evaluated Hasse derivative on the right match the univariate `Polynomial.taylor_coeff` convention. No alternative equivalence family introduced.
21. **SYNTAX-GEN:** OK: explicit translation, exponent, and polynomial parameters are convenient for rewriting coefficients. No bundled hypothesis is being reconstructed by callers.
22. **IMPORT-FANOUT:** n/a: no new imports; both helper proofs use the existing import closure.
23. **CASTS:** no coercions/ascriptions added to the public target. One existing `: MvPolynomial σ R` ascription moves with `hXC` and fixes the coefficient ring on the otherwise underdetermined left expression. The explicit cast normalisation tactic disappears; casts remain implicit in the binomial/Hasse coefficient API. Status: 0 ascriptions dropped / 0 new cross-type casts / 1 moved load-bearing ascription.
24. **INSTANCE-NAME:** n/a: no instance declaration or local named instance.

Issues fixed: headline decomposition; redundant `generalizing d` and `classical` in the headline; single-use zero-coefficient fact; redundant translation equality; support-arithmetic scaffolding; ordinary lambda style; terminal cast/ring chain. No public API or definition edits.

## Mathlib search status

| Method | Actual query / evidence | Result |
|---|---|---|
| A Lean-Finder | `multivariate polynomial Taylor shift coefficient Hasse derivative binomial expansion` | Returned `Polynomial.taylor_coeff`, `taylor_coeff_one`, `hasseDeriv_apply`, `hasseDeriv_coeff`; univariate partial matches. |
| B Loogle | `Polynomial.coeff ((_ + Polynomial.C _) ^ _) _` | Returned `Polynomial.coeff_X_add_C_pow`, already the correct binomial building block. |
| C LeanSearch | Session-known HTTP 500 failure; parent explicitly instructed not to retry the unavailable service | Unavailable, not evidence of absence. |
| D local source | Untruncated `rg` for `coeff_taylor`, `coeff_X_add_C_pow`, `hasseDeriv`, `taylor` in MvPolynomial and Polynomial/Taylor; exact new-helper names in mathlib | Found the univariate API and no source match for the two new helper names. |
| E name pattern | Native `lean_local_search` for `coeff_taylor` | Found current project theorem and `Polynomial.coeff_taylor_natDegree`; index reported unavailable, so empty portions are not absence evidence. Source and compiled `#check` supplement this. |

Auxiliary variants examined: `taylor_coeff`, `taylor_coeff_zero`, `taylor_coeff_one`, `taylor_monomial`, `taylor_X_pow`, `hasseDeriv_apply`, `hasseDeriv_coeff`, `monomial_single_add`, and the existing three project helpers. The common-equivalents table has no matching topology/finite-set concept. No noncomputable decidability instance, custom predicate, coset equality, or redundant mathlib wrapper was introduced.

Compiled generic-route probes at the original live proof position: `exact?` could not close; `apply?` suggested `Finsupp.apply_eq_of_mem_graph`, leaving a graph-membership goal equivalent to the original problem. This is not a replacement proof. Whole-proof `grind`, `simp [taylor, hasseDeriv]`, and `aesop` also failed. Thus the evidence supports retaining this project-specific multivariate theorem built on the univariate coefficient API; it is not an absolute absence claim about all mathlib versions. Extracted helpers capture the existing nontrivial monomial argument, rather than adding public wrappers.

## Generalisation status

| Parameter | Class | Use | Mechanical candidates checked | Verified? | Result |
|---|---|---|---|---|---|
| `{σ : Type*}` | type variable | Variable domain in α, d, P | Drop would leave dependent parameter types unbound; universe generality already independent `Type*` | Type shown by `#check` | Keep; no narrower universe constraint. |
| `{R : Type*}` | type variable | Coefficient domain | Drop leaves all coefficient types unbound; already universe-polymorphic | Type shown by `#check` | Keep. |
| `[CommSemiring R]` | typeclass | MvPolynomial, taylor, eval, hasseDeriv and commuting binomial factors | Drop; weaken to `[Semiring R]` | Yes, compiled scratch errors at lines 9, 10, 14 | Both fail `failed to synthesize CommSemiring R`; reverted/not applied. |
| `(α : σ → R)` | structure value | Translation and evaluation point | Drop would remove the point occurring on both sides; no global property to point-localise | Syntactic dependency check | Keep arbitrary function; no finite-support/nonzero assumption. |
| `(d : σ →₀ ℕ)` | structure value | Extracted exponent and derivative order | Drop leaves both sides unbound; replacing ℕ by ordered abstract exponents changes polynomial/Hasse content | Syntactic dependency check | Keep arbitrary multi-index. |
| `(P : MvPolynomial σ R)` | structure value | Polynomial translated and differentiated | Drop leaves both sides unbound; no property hypothesis to weaken | Syntactic dependency check | Keep arbitrary polynomial. |

No proposition, strict inequality, decidability, topology, finiteness, or characteristic hypothesis exists to drop or weaken. No injectivity/bijectivity bundle exists to unbundle. The inversion check does not reveal a concrete witness: all variables are arbitrary, and translation/Hasse formulas are used throughout the monomial calculation. A generic Hasse-Schmidt system would require an additional abstract structure and different theorem; no current caller warrants that change. Big-change candidates: none.

The native `lean_run_code` weakening attempt reported stale imports; this was not recorded as a result. The CLI fallback `/Users/ramin/.elan/bin/lake env lean /private/tmp/taylor-coeff-weakening.lean` returned exit 1 with the three expected instance-synthesis errors, while printing checked signatures. Log: `/private/tmp/taylor-coeff-weakening.log`.

## Public literature search

Web query: `multivariate polynomial Hasse derivative Taylor expansion commutative ring generalization`. Top three returned hits were *Joints of Varieties* (research article), a Vaia textbook exercise (not used as authoritative support), and *Fast Multivariate Multipoint Evaluation over All Finite Fields* (research article). Primary-source findings used:

- [Joints of Varieties](https://link.springer.com/article/10.1007/s00039-022-00597-5) presents multivariate Hasse derivatives as coefficient extraction in Taylor expansion, avoiding factorial denominators in positive characteristic.
- [Fast Multivariate Multipoint Evaluation](https://doi.org/10.1145/3652025) formulates multivariate polynomial Hasse derivatives over a commutative coefficient ring.
- [Author-hosted algorithm paper](https://perso.ens-lyon.fr/gilles.villard/BIBLIOGRAPHIE/PDF/ieee-2015.pdf) states the Hasse Taylor expansion for a commutative ring with unity.

Inference: this theorem already avoids field, characteristic-zero, and subtraction hypotheses by working over CommSemiring, and it allows an arbitrary variable type with finitely supported exponents. These sources do not supply a concrete weakening compatible with the current API. ChatGPT math MCP: unavailable (no matching callable tool in the tool inventory). Literature-driven big-change candidate list: empty.

## Line packing

`#check @MvPolynomial.coeff_taylor` run with `format.width 100` prints the fully quantified type with independent universes and exactly the original three explicit parameters. Fully qualified names make the printer output wider than the source; the source arithmetic below uses codepoints. The indivisible next syntactic unit on line 131 is the complete equation `… := by`, not an arbitrary word fragment.

```lean
@MvPolynomial.coeff_taylor : ∀ {σ : Type u_1} {R : Type u_2} [inst : CommSemiring R] (α : σ → R) (d : σ →₀ ℕ)
  (P : MvPolynomial σ R), ((MvPolynomial.taylor α) P).coeff d = (MvPolynomial.eval α) ((MvPolynomial.hasseDeriv d) P)
```

| Signature line | Codepoints | Next signature unit | Arithmetic | Action |
|---|---:|---|---|---|
| 130 | 70 | Complete equation and `:= by`, 52 chars without indentation | 70 + 1 + 52 = 123 > 100 | ok |
| 131 | 56 | No next signature line | n/a | ok |

Before/after target signature bytes compare identically. All changed-region lines are at most 100 codepoints. The new step-helper first line was repacked to 99 codepoints; its remaining signature widths are 18, 88, 77, 71. Its independent worker will own its formal width/audit artifact.

## Inequality scan

| Occurrence | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| n/a | Entire signature and every target parameter | No `≥` or `>` | None | No `_ge_`/`_gt_` in name |

The moved proof's order premise is `hle : e ≤ k`, obtained within the negated coefficient criterion; smaller side is already on the left. No reversed inequality was introduced.

## Golfing rule pass (all 42)

| Rule | Status |
|---|---|
| 1.1 by-exact wrapper | n/a: target has a genuine induction proof, not a wrapper. |
| 1.2 by-rfl | n/a: no reflexivity wrapper. |
| 1.3 rw + exact | n/a: no adjacent rewrite/exact pair in the final target. |
| 1.4 simp + exact | n/a: all simp calls terminate their branches. |
| 1.5 trailing rfl | n/a: no rfl after simp. |
| 1.6 constructors | n/a: equation, no conjunction construction. |
| 1.7 apply + exact | n/a: no such pair. |
| 1.8 by_contra + push_neg | n/a: support contradiction has no push_neg. |
| 1.9 eta-reduce | No `fun x ↦ f x` lambda; meaningful lambdas normalised to `↦`. |
| 1.10 single-use have | Applied: original zero-case hasseCoeff fact inlined; support arithmetic inputs eliminated; htay eliminated. hi' was multiply used, not incorrectly classified as single-use. |
| 1.11 apply + intro | n/a: no such sequence. |
| 1.12 redundant show | n/a: none. |
| 1.13 have + projections | n/a: no stored conjunction/existential projected repeatedly. |
| 1.14 merge rw | Applied: the translation-factor rewrites formerly inside htay merge into the coefficient rewrite. |
| 1.15 terminal simp only | n/a: none. |
| 1.16 nonterminal bare simp | n/a: all calls terminal, including contradiction at he. |
| 1.17 dot notation | Existing `.2`, `.1`, and `.coeff` use appropriate projection notation; no shorter named application pair. |
| 1.18 avoid parentheses | Applied direct `fun hle ↦ …` argument inside coefficient criterion; no trailing lambda parentheses. |
| 1.19 push_neg | n/a: none. |
| 1.20 trivial exists helper | n/a: neither target nor extracted helpers is existential. |
| 2.1 grind whole proof | Tried at original entry; failed with the negated translation-coefficient identity. Also tested at original terminal algebra goal; succeeded. Chose terminal AC simp because it exposes the exact algebraic operation. |
| 2.2 delete before grind | No grind retained. New terminal simp absorbs both push_cast and ring; no precursor arithmetic tactic remains. |
| 2.3 simpa consolidation | Terminal simp with commutativity/associativity and casts consolidates old final two tactics. |
| 2.4 fun_prop | n/a: no continuity/differentiability/measurability property. |
| 2.5 positivity | n/a: no positivity or structural nonzero goal; support disequality is a hypothesis, not a numerical positivity obligation. |
| 2.6 gcongr | n/a: no inequality congruence goal. |
| 2.7 lia/omega | Existing lia support step removed entirely via `le_zero_iff.1 (hi ▸ hle i)`; no arithmetic automation needed afterward. |
| 2.8 aesop | Tried at original entry; failed to make progress. |
| 2.9 norm_num/norm_cast | norm_num tried at original terminal algebra goal; left the multiplicative identity unsolved. Final simp handles Nat casts while normalising products. |
| 2.10 decide | n/a: arbitrary polynomial/semiring equation is not finite executable decision data. |
| 2.11 field_simp; ring | n/a: no denominators and only a CommSemiring assumption. |
| 2.12 linear_combination | Actually tried at original ring endpoint; tactic unavailable in existing import closure (`unknown tactic`). No new import justified because AC simp closes it. |
| 2.13 wlog | n/a: addition and monomial cases are distinct mathematical constructors, not symmetric cases. |
| 2.14 collapse calc | n/a: no calc. |
| 2.15 close several goals | Considered applying common automation across induction branches; explicit three-line outline retained because additive simp and the monomial helper are different arguments. An attempted multi_attempt at a branch-header position returned `No goals to be solved`/missing-alternative errors and is not counted as a successful or failed mathematical proof. |
| 3.1 erw | n/a: none. |
| 3.2 legacy function tactics | n/a: none. |
| 3.3 omega→lia | No omega; existing lia eliminated as in 2.7. |
| 3.4 rfl substitution | Existing `obtain rfl | hd` substitutes zero directly; no redundant subsequent substitution. |
| 3.5 automation attributes | No new global attributes: the coefficient conversion remains an explicit public rewrite API; private helpers only serve its proof. |
| 3.6 simp_all | n/a: no squeezed simp_all; final additive branch uses its two hypotheses explicitly. |
| 3.7 maxHeartbeats | n/a: no option before or after. |

## Step back

Whole-proof automation does not discover the multivariate binomial calculation; `exact?` and `apply?` supply no usable replacement. The mathematical improvement is separating polynomial linearity from monomial exponent induction and the single-coordinate step. Final headline proof is already three short lines; term-mode induction would obscure its two mathematical cases. All original explanatory documentation stays attached to the public theorem. No redundant tactic, unexplained case split, or cast normalisation chain remains in the headline.

## Verification and diff gates

- Complete native `lean_diagnostic_messages` after final edit: `success: true`, `partial: false`, `timed_out: false`, no failed dependencies; only existing line-1 copyright warning.
- Actual final `/Users/ramin/.elan/bin/lake build Roth.Taylor`: session 92619, exit 0, 1439 jobs, Taylor compiled in 15 seconds. `/private/tmp/taylor-coeff-module.log`.
- Isolated file constructed from imports and declarations strictly before/through the target, excluding all later Taylor declarations: `/private/tmp/taylor-coeff-isolated.lean`, `lake env lean`, session 19413 exit 0. No import of Roth.Taylor in this file, so no self-reuse/circular proof. The subsequent final edit was whitespace-only packing of the new helper signature; final LSP and module build above cover it.
- The isolated file includes an `example` of the exact original public statement proved by the new theorem, and `#print axioms` for the headline and both helpers. All report only `propext`, `Classical.choice`, `Quot.sound`. Log `/private/tmp/taylor-coeff-isolated.log`.
- Programmatic checks: original target signature byte-identical; every original block comment/docstring byte-identical; no changed-region line >100; no sorry/admit/axiom/native_decide/set_option/haveI/letI/push_neg in changed region.
- Parent owns full-project and separately `Roth.LeanEval` dependent gates after source freeze.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Actual module build above, exit 0. |
| definition_protected | pass | No def/abbrev changed. |
| theorem_statement_protected | pass | Headline signature byte-identical; two explicitly authorized private extractions. |
| structure_gate | pass | Headline 3 lines ≤15; two one-line branches; no conjunction. |
| naming_gate | pass | Descriptive mathematical snake_case; no forbidden patterns. |
| line_packing_gate | pass | Both target signature rows measured above, no repack row. |
| inequality_orientation_gate | pass | Required scan emitted; zero reversed inequalities. |

Overall: pass for the original declaration; new helpers await their own fresh dedicated audits.

## Result and checklist

Before 35 declaration/33 body lines; after 5 declaration/3 body lines; headline savings 30. Seven concrete cleanup categories fixed. Refactoring needed: no deferred source refactor; parent must independently audit the two newly extracted private declarations listed above. Renames queued: none. Comments preserved: all existing block comments/docstrings, zero inline comments originally.

- [x] Step 1 — reference documents read.
- [x] Step 2 — full 24-item audit recorded.
- [x] Step 2.5 — all five search methods accounted for with availability distinctions.
- [x] Step 2.6 — all parameters and applicable weakenings covered; public literature search recorded.
- [x] Step 2.7 — full target signature width table.
- [x] Step 2.8 — inequality occurrence scan.
- [x] Step 3 — all 42 rules given concrete status.
- [x] Step 4 — strategy reflection and actual whole-proof alternatives.
- [x] Step 5a — complete live LSP diagnostics clean for target.
- [x] Step 5b — diff gates and actual module/isolation/type/axiom checks.
- [x] Step 6a — no rename required.
