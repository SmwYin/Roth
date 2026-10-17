# Cleanup: `Roth.index_eq_weightedOrder_div`

Single-original-declaration checkpoint, originally e557886; worker started from published d90ac85. Scope: this theorem and this report only. No Git operations, import changes, definition changes, helper additions, or rename applications. Whole-project builds, LeanEval, publication, final independent simplify and file sweeps belong to the file owner.

## Mathematics and changes

The rational minimum over nonzero Taylor coefficients agrees with the natural weighted order after clearing the denominators by `D = ∏ i, r i`. The forward inequality uses a coefficient attaining the power-series order. The reverse inequality supplies a lower bound for every nonzero Taylor coefficient through `le_index_iff`; there is no need to choose a second coefficient attaining the polynomial index.

The approved public-type change is precisely `omit [DecidableEq σ] in`, placed before the unchanged docstring. `hP`, `hr`, the coefficient field, data arguments, conclusion, and documentation remain. Lambda arrows are normalized to `↦`, and the short `index P α r =` joins the parameter line. The public mathematical assertion is otherwise preserved; the omission does change the elaborated public type, as the built signature confirms.

## References read

Read the lean4 and mathlib-quality SKILL.md files, cleanup.md in full (including the fresh single-declaration worker contract), the relevant cleanup-all.md orchestrator/worker and checklist contract, and the full golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, cleanup-gates.md, style-rules.md, naming-conventions.md, profiling.md, buzz.md, and mathlib-review-stages.md. Read lean4/references/proof-simplification.md for the scoped strategy review. Output truncation was resolved by range reads. The session's `/private/tmp/roth-index-leaf-contract.txt` governs the narrower API, comment-preservation, build, and release boundaries.

## Complete 24-item audit

| # | Item | Concrete finding/action |
|---|---|---|
| 1 | LINT | Input diagnostics included unused σ-DecidableEq section/type warnings on this theorem. Approved omission removes both. Complete final unfiltered native diagnostics are recorded below; target has zero warnings/errors. |
| 2 | HAVE SCAN | Final proof has no `have` declarations. Original `hF` has proof content and one use; original `hfin` is used in the attained-coefficient argument and in rewriting `h1`; original `h1` is rewritten and then cast. The initial simplification removed `hF`/`hFdef`, retaining the two-use finite-order certificate. The alternative below also removes finite-certificate and comparison `have` plumbing using `ENat.toNat_le_toNat`; no arbitrary helper split. |
| 3 | SET_OPTION | No per-declaration limits, diagnostics, profiler or trace options exist in the source. No limit raised. |
| 4 | SIMP SQUEEZE | All new `simpa` calls are terminal coefficient/nonzero conversions. No nonterminal bare simp and no squeezed terminal simp introduced. |
| 5 | NAMING | `index_eq_weightedOrder_div` describes an equality and preserves the existing `weightedOrder` API component. No forbidden abbreviation, scheme number, numeric auxiliary suffix, `_ge_`/`_gt_`, or single-letter public name. No rename queued; the existing derivative-name queue remains untouched. |
| 6 | LINE PACKING | Every signature line has a codepoint arithmetic row below; built `#check` uses `format.width 100`. The short left side was repacked into the last binder line. |
| 7 | BY PLACEMENT | `by` remains at the end of the signature; nested tactic proofs begin on their introducing line. |
| 8 | FORMAT | Two-space body, four-space signature continuation, no blank body lines, no semicolon tactic chains, no `haveI`/`letI`; all source lines at most 100 codepoints. |
| 9 | COMMENTS | No proof-body comments existed. All four docstring lines are byte-identical to the start snapshot; no comments removed or relocated. |
| 10 | DOCSTRING | Existing public explanation distinguishes the power-series interpretation and scaling by `D`; preserved exactly under user scope. |
| 11 | VISIBILITY | Public bridge is listed among module main results and used by product additivity. Its intended API is public. Classic import dialect; no module-system rewrite applies. |
| 12 | STRUCTURE | Two mathematical inequalities; each branch below ten lines. Final proof has 12 body lines (148–159), below the headline bound, without helpers. The initial 15-line candidate and the final monotonicity alternative were both compiled and profiled. No conjunction in the statement; no decomposition flag needed. |
| 13 | MATHLIB | All five actual search methods attempted, with remote DNS failures disclosed below. Build on the existing weighted-order minimum API; no replacement of the project-specific rational index was established. |
| 14 | JUNK DEF | n/a: target is a theorem; existing `index` definition is outside the owned target and unchanged. |
| 15 | EXISTS LEMMA | n/a: theorem asserts an equality, not a trivial private existential wrapper. |
| 16 | SHOW vs CHANGE | The initial candidate used term-level `show F ≠ 0 by ...` to pin an expected proposition. The final proof instead pins `(f := F)` on the witness theorem and has no show/change command. |
| 17 | PUSH_NEG | No `push_neg` or negation-normalization tactic. |
| 18 | GENERALISE | Every elaborated top-level binder is classified and probed below. Only the approved decidability omission is applied. No other API weakening is inferred from a failed proof probe. |
| 19 | INEQUALITY | Explicit occurrence table below: positive weights use `0 < r j`; neither `≥` nor `>` occurs in the signature. |
| 20 | NORMAL-FORM | RHS is mathlib `MvPowerSeries.weightedOrder`, finite `toNat`, cast to ℝ, divided by `D`. This is the intended canonical bridge for `index_mul`; no competing pairwise-equivalence API added. |
| 21 | SYNTAX-GEN | Positivity is already a directly applicable function hypothesis; `α` is explicit and `P`, `r` inferred. No easier equivalent public restatement justified. |
| 22 | IMPORT-FANOUT | n/a: no imports added; this theorem continues to use already imported power-series order API. |
| 23 | CASTS | No redundant casts introduced. Polynomial→power-series coercion fixes the relevant order object; natural order→ℝ and product→ℝ are genuine cross-type conversions. The local `F : MvPowerSeries σ ℝ` annotation is load-bearing. |
| 24 | INSTANCE-NAME | n/a: no instance declarations or local instance values introduced. |

## Five-method mathlib search

| Method | Actual query/action | Outcome |
|---|---|---|
| A Lean-Finder | `index of polynomial equals weighted order of Taylor formal power series divided by product weights`, num_results 3 | Actual bounded helper call returned DNS failure (`nodename nor servname provided, or not known`); unavailable, not no-hits. |
| B Loogle | `MvPowerSeries.weightedOrder`, num_results 3 | Actual bounded helper call returned DNS failure; unavailable, not no-hits. |
| C LeanSearch | `weighted order of multivariate polynomial Taylor expansion minimum weights nonzero coefficients`, num_results 3 | Actual bounded helper call returned DNS failure; unavailable, not no-hits. |
| D Source | Untruncated `rg` for `index_eq_weightedOrder_div`, weighted-order/coercion/sInf patterns and all weighted-order theorem declarations in MvPolynomial and MvPowerSeries/Order.lean; read Order.lean 140–222 | Located finite-order equivalence, attained-coefficient witness, lower-bound lemma, and `weightedOrder_eq_nat`. No textual copy of this project bridge found in the searched topic files. |
| E Name patterns | Native `lean_local_search "weightedOrder"`, limit 10; later `ENat.toNat_le_toNat`, limit 3 | Positive source hits include `weightedOrder_le`, `weightedOrder_eq_nat`, `weightedOrder_mul`; native symbol index was unavailable/error, so empty/index-based absence is not claimed. ENat conversion found in Data/ENat/Basic.lean:298. |

Auxiliary variants inspected: `_le`, `_eq_nat`, `_eq_top_iff`, `ne_zero_iff_weightedOrder_finite`, `exists_coeff_ne_zero_and_weightedOrder`, `_monomial`, `_toSubring`, `_mul`, and ENat monotonic conversion. Common-equivalents table: no topology, finiteness, separation or bornology bucket matches this domain-specific index bridge.

Compiled absence probe `/private/tmp/roth-index-weighted-absence.lean` imports only the original lower-level dependencies, defines the original index formula in `IndependentWeighted`, and tries `exact?` on the original public formula. It exits 1 with “exact? could not close the goal.” This is evidence against a one-step generic replacement in that environment, not a universal claim of mathlib absence. Native baseline attempts also left the goal open with `grind`, `simp`, `aesop`, `exact?`; `apply?` suggested generic real/division extensionality obligations, not a replacement theorem. That native multi-attempt replaced the second setup line, and suffix diagnostics mentioned the removed local `F`/`hFdef`; those suffix errors are disclosed and are not counted as target verification.

Six replacement rules: no wrapper/helper added; all five methods attempted; auxiliary variants searched; no custom predicate introduced; no established mathlib equivalent was retained as a duplicate; mathlib dependencies documented here while preserving the user-locked module docstring.

## Public literature and generality

Query: **“Roth theorem polynomial index weighted order Taylor expansion generalization”**. The first three displayed leads, in order (one query, no requery):

| Rank | Displayed lead | Treatment |
|---|---|---|
| 1 | [Journal de théorie des nombres de Bordeaux, 10.5802/jtnb.260](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.260.pdf) | Primary journal lead; ranking recorded, no uninspected mathematical claim attributed to it. |
| 2 | [Aleksa Milojevic, An elementary approach to Roth’s theorem](https://aleksa-milojevic.github.io/expository/roth.pdf) | Opened and inspected §3, Claim 3.1 and Taylor-expansion discussion. |
| 3 | [Min Ru, Roth’s Theorem](https://www.math.uh.edu/~minru/fields/roth.pdf) | Opened as an author's university-hosted exposition; corroborating lead. |

Milojevic's §3 defines index by a minimum of normalized multi-index degrees and explains the Taylor-polynomial viewpoint. This supports the present mathematical identification; it does not require a chosen decidable equality. Local primary project source `.mathlib-quality/references/clean.tex:531–556` explicitly permits positive real weights for a direct finite-support minimum, and prescribes positive integral weights, `D = ∏ r_j`, and `w_j = D/r_j` for this natural weighted-order encoding. Thus arbitrary real weights cannot be substituted into this exact RHS without restatement. The source's zero-polynomial infinity convention is intentionally different from the current ℝ-valued zero convention; no convention change is made here. Mathematical ChatGPT MCP is unavailable: no matching tool was exposed in ALL_TOOLS.

Literature-driven public restatement candidates: a direct finite-support minimum with arbitrary positive real weights is a larger coordinated definition/API change, not applied. The proof still names Taylor coefficients, the natural weighted-order API, and the rational weight conversion throughout: no purely abstract one-line corollary has been established by the inversion check.

## Mechanical generalisation table

Each scratch drop uses `set_option autoImplicit false`. Negative proof probes diagnose the current formulation/proof; they do not prove the hypothesis mathematically indispensable. Failed candidates never changed live source.

| Binder | Classification and role | Mechanical candidates/probe | Result |
|---|---|---|---|
| `{σ : Type*}` | Type variable, arbitrary universe; domain of polynomials, weights, point | Erase binder under autoImplicit=false; universe already polymorphic | Fails on unknown σ; no stronger universe constraint exists to relax. |
| `[Fintype σ]` | Data-bearing finiteness instance, used by products, real weight/index | Drop; replace by parent `[Finite σ]` | Signature cannot synthesize Fintype for finite products/index. Replacing all sums/products with chosen enumerations would be an API restatement, not an automatic weakening. |
| `[DecidableEq σ]` | Unused decidability inherited from section | Approved omit before docstring | Positive: candidate, actual module, native final diagnostics and built signature confirm omitted. |
| `{P : MvPolynomial σ ℝ}` | Structure value, translated polynomial and nonzero source | Erase data binder, autoImplicit=false | Fails on unknown P. Coefficient-field abstraction would change the fixed ℝ-valued `index` API; not a parent-class weakening. |
| `(hP : P ≠ 0)` | Proposition supplying finite order / nonempty minimum | Drop | Current proof cannot supply the nonzero/finiteness and lower-bound facts. Preserved. A proof failure is not a counterexample to a possible zero-case extension. |
| `{r : σ → ℕ}` | Structure value determining integral denominator clearing | Erase data binder, autoImplicit=false | Fails on unknown r. Positive real weights require a different formulation, per the source. |
| `(hr : ∀ j, 0 < r j)` | Proposition, global positivity for denominator clearing | Drop; strict→weak `∀ j, 0 ≤ r j`; point-local `∀ j ∈ (taylor α P).vars, 0 < r j` (scratch places α before the dependent hypothesis) | Drop cannot supply weight-conversion positivity; weak and point-local forms do not match required global positivity. No change applied. |
| `(α : σ → ℝ)` | Structure value, Taylor expansion center | Erase data binder, autoImplicit=false | Fails on unknown α. No continuity/monotonicity/regularity hypothesis to point-localize. |

Nested `j` in the positivity function and bound `i`,`j` in products/lambdas are bound variables of the displayed functions, not removable independent theorem parameters; erasing them would leave ill-formed dependent expressions. No algebraic/analytic class-parent candidates apply to the concrete ℝ type. No bundled injectivity/bijectivity hypotheses occur.

## Signature line packing

Before: signature lines 143–147 had widths 82, 37, 17, 94, 22. The separated `index P α r =` (13 codepoints without indentation) fit on the binder line, `37 + 1 + 13 = 51`, so it was repacked. No mathematical token was changed beyond the ordinary lambda spelling.

Final source, every signature line (widths include leading indentation; next syntactic group excludes indentation):

| Line | Codepoints | Next signature group | Arithmetic | Action |
|---|---:|---|---|---|
| 144 | 82 | `(hr : ∀ j, 0 < r j)` (19) | 82 + 1 + 19 = 102 > 100 | ok |
| 145 | 51 | Complete parenthesized weighted-order numerator followed by `/` (87) | 51 + 1 + 87 = 139 > 100 | ok |
| 146 | 93 | `∏ i, r i := by` (14) | 93 + 1 + 14 = 108 > 100 | ok |
| 147 | 22 | no next signature line | n/a; proof follows | ok |

The 87-codepoint numerator is a single parenthesized term; pulling the initial `(` token alone onto the previous line would neither pack a binder nor improve the syntax. `by` remains on the product line. No wide-hyp escape used. Built `#check @Roth.index_eq_weightedOrder_div` at `format.width 100` is included with the verification evidence below; pretty-printing may itself leave a large application segment unbroken.

## Inequality occurrence scan

| # | Location | Source | Rewrite | Rename |
|---|---|---|---|---|
| 1 | Positivity hypothesis `hr`, L145 | `0 < r j` | Already smaller side left; unchanged | none |
| 2 | Remaining signature and hypotheses | zero `≥` and zero `>` occurrences | n/a | no `_ge_`/`_gt_` in name |

All proof-side inequalities are generated by `le_antisymm`, `le_index_iff`, division monotonicity and the standard ENat order comparison; no reverse inequality notation added.

## All 42 golfing rules

| Rule | Status and concrete evidence |
|---|---|
| 1.1 by-exact wrapper | n/a: no theorem body of the form `by exact term`. |
| 1.2 by-rfl wrapper | n/a: no reflexivity proof. |
| 1.3 rw + exact → rwa | The old hF rewrite/nonzero proof is eliminated; no surviving rewrite immediately turns a goal into the following exact term without coefficient/weight conversion. |
| 1.4 simp + exact → simpa | Applied: direct terminal `simpa` converts power-series coefficients to evaluated Hasse coefficients and proves Taylor nonvanishing. |
| 1.5 trailing rfl after simp | n/a: none. |
| 1.6 constructor/exact pair | n/a: equality uses two inequalities, not a conjunction constructor. |
| 1.7 apply + exact composition | The two order directions are genuinely different subgoals; `le_antisymm` is retained. Division monotonicity leaves a real numerator comparison. |
| 1.8 by_contra/push_neg | n/a: no contradiction argument. |
| 1.9 eta reduction | Weight function computes product/division, so not eta-reducible; arrows normalized to `↦`. |
| 1.10 single-use have | Final proof removes all `have` declarations: finite-order certificate is supplied directly to the attained-coefficient API; the ENat comparison is supplied directly to `toNat_le_toNat`. |
| 1.11 apply + intro → refine/fun | Applied structurally: reverse inequality is `(le_index_iff hP).2 fun e he ↦ ...`. |
| 1.12 redundant show | Initial 15-line candidate needed `show F ≠ 0` to pin the nonzero term; final proof instead pins `(f := F)` at the witness API, eliminating that annotation. |
| 1.13 have + projections → obtain | Attained minimum is destructured directly with `obtain ⟨d, hd, hdw⟩`; no projection plumbing. |
| 1.14 merge consecutive rw | No sequential rewrite calls on the same goal remain. The forward weight conversion is one `rw` list. |
| 1.15 terminal simp only | n/a: no terminal `simp only`. |
| 1.16 nonterminal bare simp | n/a: no nonterminal `simp`. |
| 1.17 dot notation | `(le_index_iff hP).2` and finite-order equivalence `.1` used directly; qualified power-series names fix subject/API unambiguously. |
| 1.18 `<|` over parentheses | Retained parentheses in nested proof/cast arguments because following arguments and `(f := F)` require clear grouping; no trailing unnecessary `f (fun ...)` wrapper. |
| 1.19 push_neg → push Not | n/a: none. |
| 1.20 trivial existential helper | n/a: no helper declaration introduced; the attained-minimum result is substantive existing mathlib API. |
| 2.1 whole grind | Actual native attempt left an unsolved polynomial-index/weighted-order equality; not selected. |
| 2.2 delete before grind | n/a: final proof contains no grind to subsume preceding steps. |
| 2.3 simpa consolidation | Terminal coefficient conversions consolidated directly; no separate support-membership round trip. |
| 2.4 fun_prop | n/a: no continuity/differentiability/measurability goal. |
| 2.5 positivity | Compiled local probe proves `(0 : ℝ) ≤ n` by positivity. Kept explicit `Nat.cast_nonneg _` at the division API for clarity and stable small proof. |
| 2.6 gcongr | Compiled local probe proves the division comparison from `h : m ≤ n`, natural denominator, by `gcongr`. Retained the explicit monotonicity API, which states exactly the needed denominator fact. |
| 2.7 lia/omega | n/a: numerator comparison is an abstract weighted-order inequality, not arithmetic derivable from linear Nat/Int hypotheses. |
| 2.8 aesop | Actual native attempt reported exhaustive-search failure on the bridge; no automation replacement selected. |
| 2.9 norm_num/norm_cast | Actual local cast probe with `exact_mod_cast` compiles. Final proof crosses ℕ∞→ℕ with the dedicated ENat lemma, then ℕ→ℝ with exact_mod_cast; no concrete numeral computation to normalize. |
| 2.10 decide/kernel | n/a: universal equality of a real index and a noncomputable minimum is not finite computation. |
| 2.11 field_simp; ring | n/a: goal is a minimum comparison; clearing denominators alone cannot identify either minimum. Dedicated weight conversion is reused. |
| 2.12 linear_combination | n/a: no proof ends in ring/ring_nf and no polynomial algebra certificate closes the order-minimum step. |
| 2.13 wlog | n/a: inequality branches are different minimum principles, not symmetric cases. |
| 2.14 two-step calc | n/a: no calc block. |
| 2.15 `<;>` common goals | n/a: antisymmetry goals use different APIs; no identical branch closer. |
| 3.1 erw → rw | n/a: no erw. |
| 3.2 continuity/measurability | n/a: no analytic regularity tactics. |
| 3.3 omega → lia | n/a: no omega or linear integer-arithmetic goal. |
| 3.4 rcases rfl substitution | n/a: witness equality concerns order/weight, not a substitutable data-variable constructor equation. |
| 3.5 automation attributes | No global simp/grind attribute justified for this project bridge; existing explicit call sites rewrite it with nonzero/positivity arguments. |
| 3.6 simp_all | n/a: no context-wide simp_all proof; only local terminal conversions. |
| 3.7 remove maxHeartbeats | n/a: none existed; no limit or profiler scaffolding added. |

## Step-back and scoped simplify

The final mathematical improvement is eliminating the reverse attained-minimum witness and expressing its direction as the lower-bound characterization of `index`. The further selected simplification converts `weightedOrder_le` through `ENat.toNat_le_toNat`; it avoids rewriting a separate finite-order certificate merely to compare naturals. Only one attained-coefficient witness is needed. The 12-line body is an outline of the two minimum comparisons, with no helper extraction, arbitrary splitting, or tactic packing.

Whole-goal `exact?` in the independent environment failed. Native `apply?` gave partial generic division/real-extensionality candidates, which do not shorten the mathematical argument. Term-mode assembly would hide rather than remove the two different bound arguments. `weightedOrder_eq_nat` was inspected, but would require proving vanishing of all smaller weights and introduce an extra strict-inequality argument. The direct minimum inequalities are preferable.

Scoped simplify outcome: ISSUES-FOUND-AND-FIXED (redundant second witness and finite-order rewrite layer removed). No built-in Skill tool for `/simplify` is exposed here; this was an in-thread scoped review following proof-simplification.md, not a claim that the owner-level independent whole-file hand-off happened. Owner retains that gate.

## Actual compiler and native verification

All commands below ran from `/Users/ramin/LEAN/Roth` with the actual Lake executable `/Users/ramin/.elan/bin/lake`. Every listed process finished before source release.

| Gate/evidence | Actual invocation/result |
|---|---|
| Initial module build | `lake build Roth.Index > /private/tmp/roth-index-weighted-build.log 2>&1`, exit 0, 1501 jobs. |
| Final module build | `lake build Roth.Index > /private/tmp/roth-index-weighted-final-build.log 2>&1`, exit 0, “Build completed successfully (1501 jobs).” |
| Complete native baseline | Direct bounded MCP helper `lean_diagnostic_messages` with only `file_path` and timeout 45; `/private/tmp/roth-index-weighted-baseline-lsp.json`. Success true, partial false, timed_out false; target unused-decidability warnings present. |
| Complete native final | Direct bounded MCP helper `lean_diagnostic_messages` with only `file_path` and timeout 45; `/private/tmp/roth-index-weighted-final2-lsp.json`. Success true, partial false, timed_out false, failed_dependencies empty; 0 errors, 17 warnings, zero target diagnostics. No severity, line, or declaration filtering. |
| Independent original type + fresh proof | `lake env lean /private/tmp/roth-index-weighted-independent.lean`, exit 0; `/private/tmp/roth-index-weighted-independent.log`. Imports original lower-level mathlib modules, `Roth.Box`, `Roth.Taylor`; does not import `Roth.Index`, the target, its support helper, or any other theorem from that file. |
| Exact original public-type recovery | Script extracts this theorem's signature from `/private/tmp/roth-index-original.lean` (e557886), renames only the scratch theorem, and instantiates the actual built theorem. `lake env lean /private/tmp/roth-index-weighted-recovery.lean`, final exit 0; `/private/tmp/roth-index-weighted-final-recovery.log`. Original `[DecidableEq σ]` is present in the scratch section and its unused-section warning is expected. |
| Actual built signature | Same final recovery file imports `Roth.Index` and runs `set_option format.width 100` plus `#check @index_eq_weightedOrder_div`. σ-DecidableEq absent; Fintype, P, hP, r, hr, α present. |
| Actual axioms | Same final recovery runs `#print axioms index_eq_weightedOrder_div`: exactly `[propext, Classical.choice, Quot.sound]`. Original-type recovery has the same three standard axioms. Independent proof prints those same three axioms independently. |
| Scoped integrity | Compared target-adjacent prefix/suffix to `/private/tmp/roth-index-weighted-start.lean`: all bytes outside the target and its approved omit are identical. Docstring bytes identical. Target has no over-100-codepoint line, sorry, native_decide, semicolon chain, or set_option. |

The independent proof defines the *original literal sInf formula* under a fresh namespace, independently proves the denominator-clearing identity from the Finsupp weight sum, obtains a nonzero coefficient attaining power-series weighted order, and compares the real sInf directly with all support weights by `csInf_le`/`le_csInf`. It does not invoke `le_index_iff`, `index_le_weight`, `exists_weight_eq_index`, `weight_eq_finsuppWeight_div`, `mem_support_taylor_iff`, or the target. The copied definition is the original definition whose public type is under review, not an invented surrogate index. Its expected unused-DecidableEq warning preserves the original theorem binder.

Built signature, verbatim width-100 output:

```lean
@index_eq_weightedOrder_div : ∀ {σ : Type u_2} [inst : Fintype σ] {P : MvPolynomial σ ℝ},
  P ≠ 0 →
    ∀ {r : σ → ℕ},
      (∀ (j : σ), 0 < r j) →
        ∀ (α : σ → ℝ),
          index P α r = ↑(MvPowerSeries.weightedOrder (fun j => (∏ i, r i) / r j) ↑((taylor α) P)).toNat / ↑(∏ i, r i)
```

The final printed line exceeds 100 because the pretty-printer keeps that expression segment together; source packing is measured separately in codepoints above. The pretty-printer's `=>` rendering is not a source-lambda regression.

### Complete final unfiltered diagnostic inventory

Raw complete response, including full messages: `/private/tmp/roth-index-weighted-final2-lsp.json`. Every returned item is listed here; no warning was hidden or suppressed.

| Location | Warning |
|---|---|
| L1 | Header copyright too short (user-preserved metadata). |
| L200 | `index_C_mul`: automatically included unused section `[DecidableEq σ]`. |
| L163 | `index_mul`: automatically included unused section `[DecidableEq σ]`. |
| L217 | `index_rename`: automatically included unused section `[DecidableEq σ]`. |
| L195 | `index_neg`: automatically included unused section `[DecidableEq σ]`. |
| L228 | `index_le_card`: automatically included unused section `[DecidableEq σ]`. |
| L205 | `index_mul_left_weights`: automatically included unused section `[DecidableEq σ]`. |
| L194 | `index_neg`: unused DecidableEq in theorem type. |
| L199 | `index_C_mul`: unused DecidableEq in theorem type. |
| L228 | `index_le_card`: `hr` not explicitly referenced. |
| L225 | `index_le_card`: unused DecidableEq in theorem type. |
| L214 | `index_rename`: unused σ-DecidableEq and τ-DecidableEq in theorem type. |
| L204 | `index_mul_left_weights`: unused DecidableEq in theorem type. |
| L177 | `index_prod`: unused DecidableEq in theorem type. |
| L161 | `index_mul`: unused DecidableEq in theorem type. |
| L238 | `index_unique`: automatically included unused section `[DecidableEq σ]`. |
| L235 | `index_unique`: unused DecidableEq in theorem type. |

These belong to later declaration checkpoints or the explicitly preserved header. The leaf does not claim whole-file warning cleanliness.

### New identifier verification

| Identifier newly used in this target | Discovery/verification | Result |
|---|---|---|
| `ENat.toNat_le_toNat` | Native local search returned its source declaration despite index status `error`; direct source inspection at `Mathlib/Data/ENat/Basic.lean:298` establishes `(h : m ≤ n) (hn : n ≠ ⊤) : toNat m ≤ toNat n`. The final actual module compiles its application, including the finite RHS cast side condition `(by simp)`. | Verified actual use. |
| `MvPolynomial.coeff_taylor` (unqualified `coeff_taylor`) | Existing imported Taylor API; inspected coefficient identity; actual final recovery includes compiled `#check @MvPolynomial.coeff_taylor`. Final module compiles both conversions. | Verified. |
| `le_index_iff` newly used in reverse branch | Existing audited theorem in the same module; actual module build typechecks its lower-bound use. | Verified; not used in independent-original proof. |

No other external identifier was introduced: remaining APIs and tactics already occurred in the old theorem or the file. No new declaration identifier or helper name exists.

### Negative experiments and recovery

- Remote search errors were actual DNS failures, not empty successful searches; remote absence is not claimed.
- Early attempts to parse the before-profile log happened before its producer had finished: one missing-anchor assertion and one incomplete-UTF-8 read. After the process exited 0, parsing succeeded with all 19 declaration anchors. These early reads are not timing evidence.
- Initial automation multi-attempts were made at the second setup line: `simp`/`aesop` removed the local declaration and their unchanged suffix then complained about `F`/`hFdef`. Their open goals and search failure are recorded, but those suffix diagnostics are not treated as compilation of a proposed replacement.
- The 12-line scratch alternative initially left the power-series metavariable unconstrained while supplying nonvanishing. Adding the explicit existing `(f := F)` witness argument fixed it. The repaired scratch alternative compiled and was profiled before selection; no failed proof entered the live source.
- Initial σ/Fintype drops were generated against a whole-file prefix and affected earlier declarations; those confounded failures were discarded. `/private/tmp/roth-index-weighted-corrected-probes.py` reran those three cases in an isolated imported-module declaration. Corrected results, exit 1 with unknown σ or unsynthesized Fintype, are in `/private/tmp/roth-index-weighted-corrected-probes.json` and their individual `.lean.log` files.
- Other drop/strict/point-local probes changed only the owned scratch signature/proof; their expected exit-1 compiler output is in `/private/tmp/roth-index-weighted-probes.json`. Erased P, r, α, hP, hr are not silently reintroduced because autoImplicit=false. Weak hr and point-local hr produce concrete argument-type mismatches at the weight-conversion applications.
- The direct independent proof and exact original recovery both compile. Their unused-DecidableEq warnings are deliberate because those gates preserve the original public type.
- The bounded MCP helper emitted teardown event-loop warnings after some completed baseline requests. Their complete structured result was success=true/partial=false/timed_out=false; the final request cleanly ended. No outstanding worker request or compiler remained at release.

## Actual anchored buzz pass

Command for each actual source sweep:

```sh
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Index.lean > /private/tmp/roth-index-LABEL-profile-trace.log
python3 /private/tmp/roth-index-profile-parse.py LABEL
```

All producer processes exited 0 before accepted parsing. The parser asserts complete coverage of all 19 current source declarations, maps command/proof trace roots to declaration names, and writes the corresponding `-profile-table.json`. Aggregate category totals/import times are not used as target timings.

| Version | Label/log prefix | Target anchored total |
|---|---|---:|
| Original worker-start proof, 16 body lines | `weighted-before` | 282.32 ms |
| Initial compiled structural simplification, 15 body lines | `weighted-after` | 522.77 ms |
| Compiled scratch monotonicity alternative, 12 body lines | `weighted-alternative` | 331.16 ms |
| Final actual source, 12 body lines, L144 | `weighted-final` | **241.789 ms** |

The scratch alternative uses the same trace format and a separate parser whose source is that scratch file; it is a measured trial, not the final actual-module result. The final actual-source row has command 12.68 ms and proof 222.48 ms (total includes other attributed asynchronous work). Its largest observed tactic step was the direct forward `exact` coefficient-bound conversion, 69.64 ms. Machine load/import/cache and simultaneous diagnostic/probe work varied between runs; these numbers establish that the selected proof is comfortably within budget, not a stable speedup ratio.

Outcome: **FAST-BOARD for this target**, final 241.789 < 750 ms borderline threshold and < 1000 ms budget. No raises removed or added, no profiler scaffolding in source, no deferred declaration, no global attribute/instance changes. No heavyweight optimization campaign or heartbeat-limit increase is justified. Full-file independent final sweeps remain owner gates.

## Diff gates and 11-step checklist

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Final actual `lake build Roth.Index`, exit 0, log cited above. |
| definition_protected | pass | No def/abbrev/instance declaration or body changes. |
| theorem_statement_protected | pass with explicitly approved omission | Only public-type change is unused σ-DecidableEq omission; hP/hr/data/conclusion preserved. Original built-type recovery and independent original proof compile. |
| structure_gate | pass | 12 body lines; two distinct branches, each <10 lines; no statement conjunction, helper, or decomposition deferral. |
| naming_gate | pass | Descriptive existing API name, no forbidden pattern; no rename applied or queued. |
| line_packing_gate | pass | All four final signature rows contain measured arithmetic; no repack/wide-hyp escape remains. |
| inequality_orientation_gate | pass | Explicit occurrence table; no reversed inequality symbol/name. |
| standard_axioms | pass | Actual target, independent proof and exact original recovery have only propext/Classical.choice/Quot.sound. |
| comments/scope | pass | Four docstring lines byte-identical; no proof comment existed; outside-target bytes match snapshot. |

- [x] Step 1 — required references read.
- [x] Step 2 — complete 24-item audit recorded.
- [x] Step 2.5 — all five search methods actually attempted, with failures disclosed.
- [x] Step 2.6 — every top-level binder classified/probed; public literature and first-three displayed leads recorded.
- [x] Step 2.7 — every signature line measured in codepoints and packed.
- [x] Step 2.8 — explicit per-occurrence inequality table recorded.
- [x] Step 3 — all 42 golf rules have a concrete status.
- [x] Step 4 — mathematical step-back/scoped simplify and measured alternatives recorded.
- [x] Step 5a — complete unfiltered native final result success=true, partial=false, timed_out=false; target clean, all other diagnostics disclosed.
- [x] Step 5b — actual module build, diff protection, structure, naming, packing, inequality, independent original proof, original built-type recovery, actual signature/axioms, and anchored performance gates pass.
- [x] Step 6a — no new rename warranted; existing rename queue unchanged.

## Release and result

Source authority was released and revoked before report completion. Frozen source SHA256:

`5f04282b1750289a3a79d03b8a282620d4af9a4f14c3845bde6100ee3f43f770`

At release: `Roth/Index.lean` is 265 lines (worker start 269, net −4); theorem keyword through proof is 16 lines (start 21, −5), proof body 12 (start 16, −4). The extra approved omit line accounts for the different file/declaration delta. Retained originals remain 19; no helper exists or requires an audit. Only the target and this canonical report were changed by this worker. All worker Lean/MCP/compiler processes completed before release; after release, report writing only. Owner performs full-project/LeanEval/whole-file independent gates and publication under this source freeze.

Refactoring needed: none for this declaration; no decomposition or rename deferral. Broader real-weight restatement is literature context only, not an applied or purportedly approved API change. No full-project build claim is made by this leaf.


## Owner checkpoint d13

Frozen SHA256 `5f04282b1750289a3a79d03b8a282620d4af9a4f14c3845bde6100ee3f43f770`. Fresh whole ORIGINAL nonself reproof, all18 original public
type/value recoveries and all19 actual retained standard-axiom checks: compiler
session48345 exit0, `/private/tmp/roth-index-d13-compatibility.log`.
Approved no-DecEq types are additionally checked by Expr.find?; actual signatures printed.
Sequential owner full then separate LeanEval45205 both exit0(170.63s/39.73s),
Index+Theta hashes stable; `/private/tmp/roth-index-d13-{full,leaneval}.log`.
Worker COMPLETE unfiltered native Index diagnostics success=true partial=false timed_out=false, no faileddependencies, 0target diagnostics/17other warnings; /private/tmp/roth-index-weighted-final2-lsp.json. Owner rg finds onlyinternal index_mul uses; all accepted by module/full builds, no external caller to query.
All original block docs byte-identical, source widths≤100, diff checked before staging.
Exact-path publication precedes the next edit.
