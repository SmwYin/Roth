# Approved instance revisit: eq_sum_X_none_pow_mul_coeffNone

Fresh r03 audit on `ramin-cleanup`, baseline `ea92721`, written before the source edit.
I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md, together with both SKILL.md files,
cleanup Phase 4, naming/style/profiling references. No subdelegation or Git mutation.

Scope: user explicitly approved omitting BOTH `[Fintype τ]` and `[DecidableEq τ]`
from this public theorem. Add a scoped `omit` before its original docstring;
retain its original proposition, argument order, documentation and proof unless
a minimal local classical adjustment is needed. Existing `classical` should suffice.
Both optional wrapper deletions and Domain widening were considered and DECLINED;
neither is reopened here. Nat exponent codomain remains unchanged.

## Initial 24-item audit (before source edit)

Target L91–102: 12 physical declaration lines, 3 signature and 9 proof lines.

| # | Item | Concrete assessment/action |
|---|---|---|
| 1 | Lint | Fresh complete native module diagnostics saved unfiltered; target has unusedSectionVars, unusedFintypeInType and unusedDecidableInType. Apply exact approved omission; preserve other warnings. Exact module counts are tabulated with final gates below. |
| 2 | Have scan | No `have` in this target, named or anonymous. |
| 3 | set_option | None scoped to target; no limits to remove or raise. |
| 4 | Simp squeeze | One `simp_rw [coeff_X_none_pow_mul_rename]` transports coefficients throughout a sum; no bare nonterminal simp or terminal simp-only. |
| 5 | Naming | `eq_sum_X_none_pow_mul_coeffNone` describes the equality to a sum of X-none powers times coefficient polynomials; snake_case theorem with intentional existing API token `coeffNone`, no forbidden abbreviation or numbered scheme. No rename. |
| 6 | Line packing | Signature widths 79/32/82 codepoints; table below covers every line. No next complete component fits. |
| 7 | By placement | `:= by` ends conclusion line. |
| 8 | Format | Two-space tactics, focused branches, one tactic per line, no blank proof lines; no haveI/letI. |
| 9 | Comments | No proof comments; preserve full four-line original docstring and all file narrative. |
| 10 | Docstring | Existing expansion interpretation plus source reference adds mathematical context; preserve byte-for-byte. |
| 11 | Visibility | Public expansion API used by exists_separated_representation; preserve public contract except exact approved instance removal. |
| 12 | Structure | 9 proof lines; equality, no conjunction; branches have 1 and 2 lines. No helper extraction. |
| 13 | Mathlib | Fresh five actual searches detailed below; univariate range expansion is a partial match transported through optionEquivLeft. Retain the public API under explicit scope. |
| 14 | Junk def | n/a: theorem, not a definition. |
| 15 | Exists lemma | n/a: public equality, not a private existential witness. |
| 16 | Show/change | No show occurrence. |
| 17 | Push_neg | No deprecated push_neg. |
| 18 | Generalise | Fresh effective-binder probes to run independently below; exact approved joint omission only. Universes already independent, CommSemiring needed for unchanged polynomial API, hn controls vanishing. |
| 19 | Inequality | Sole statement inequality `degreeOf none P ≤ n` already forward weak orientation; `<` arises only through Nat.lt_succ_of_le. Table below. |
| 20 | Normal form | Canonical finite polynomial expansion with natural exponent and range bound; coeffNone packages optionEquivLeft coefficients. No equivalence web needed. |
| 21 | Syntax generality | Bound hn supports direct existing call with P/hn; both instance omissions make this available for arbitrary index types without changing proposition. |
| 22 | Import fanout | n/a: no new imports. |
| 23 | Casts | No cast/ascription in intended diff: 0 dropped, 0 cross-type, 0 load-bearing. |
| 24 | Instance names | n/a: no instance declaration or generated named instance in intended diff. |

Issue/action: insert precisely one scoped omit before the original docstring.
No new helper, pending approval, shared log, rename, import, definition or attribute change.

## Fresh search and mathematical review

Raw initial search `/private/tmp/roth-separation-r03-search.json`, native audit and
automation `/private/tmp/roth-separation-r03-initial-native.json`.

| Method | Actual query | Evidence / conclusion |
|---|---|---|
| A LeanFinder | multivariate polynomial expand one distinguished variable Option coefficients | Returned `MvPolynomial.expand` and variants, which substitute powers rather than collect coefficients; no direct matching expansion identified. |
| B Loogle | `Polynomial.sum_range`; corrected `"as_sum_range_C_mul_X_pow"` | First query unknown identifier; corrected query successfully returns `Polynomial.as_sum_range_C_mul_X_pow'` and unprimed variant. |
| C LeanSearch | polynomial is sum of coefficients times powers X up to degree | Successful hits `Polynomial.as_sum_range_C_mul_X_pow'`, unprimed, as_sum_range, sum_C_mul_X_pow_eq. |
| D Source rg | as_sum_range_C_mul_X_pow, natDegree_optionEquivLeft, optionEquivLeft/sum | Pinned Polynomial/Degree/Support.lean L93/L97 confirms range-expansion APIs; independent transport probe will compile the partial match. |
| E Native local name index | sum_range, as_sum_range_C_mul_X_pow | Returned actual matching names but index=warming; no absence inference. Source/#check establish presence. |

Auxiliary variants: primed arbitrary bound, unprimed exact degree, monomial form
`as_sum_range`, coefficient `sum_C_mul_X_pow_eq`, optionEquivLeft and inverse transport.
Common-equivalents table's topology/finiteness/separation/bornology buckets do not
apply to polynomial coefficient collection. No custom predicate or instance added.
Conclusion: partial mathlib match exists. Independent equivalence transport uses it;
the retained proof remains the established 9-line coefficient proof. No theorem absence
claim or unauthorized public deletion. Header/doc additions are excluded by user preservation.

Actual public literature query: “multivariate polynomial ring iterated polynomial ring
R X Y isomorphic R X Y coefficients”. Primary lecture notes
[McKernan, Polynomial rings](https://mathweb.ucsd.edu/~jmckerna/Teaching/15-16/Spring/103B/l_15.pdf)
describe iterated coefficient collection, and
[Grinberg, Lecture 29](https://www.cip.ifi.lmu.de/~grinberg/t/23wa/lec29.pdf)
discuss variable reordering and viewing one variable over a polynomial coefficient ring.
These support the interpretation; arbitrary-index and commutative-semiring generality
are established by the fresh Lean probes, not inferred from the ring-only literature.

Native whole-goal attempts on initial actual target: grind fails, simp makes no
progress, aesop fails, exact? and apply? hit default 200000 heartbeats. None timed
out at tool level; no limits raised. Initial empty goal lookup was on blank L110;
the actual automation position L94 supplies the full target context.

## Signature width and inequality tables (initial; unchanged syntax planned)

| Signature line | Width | Next complete component | Combined width | Action |
|---|---:|---|---:|---|
| theorem name, P, n | 79 | `(hn : degreeOf none P ≤ n) :` (28) | 108 | Keep line break. |
| hn hypothesis plus colon | 32 | full equality conclusion (72) | 105 | Keep line break. |
| equality plus := by | 82 | proof starts next line | n/a | Keep. |

| Occurrence | Form | Orientation / action |
|---|---|---|
| hn in statement | degreeOf none P ≤ n | forward weak ≤, unchanged |
| branch bound argument | Nat.lt_succ_of_le ((monomial_le_degreeOf none h).trans hn) | constructs e none < n+1 in forward orientation, unchanged |
| name | eq_sum_X_none_pow_mul_coeffNone | no _ge_/_gt_ token |

This is the initial audit artifact. Fresh compiler probes, final gates, all 42 rule
statuses and freeze evidence will be appended after the exact authorized edit.

## Complete 42-rule fresh golfing review

No further proof rewrite is warranted in this approved instance-only revisit.

| Rule | Concrete fresh status |
|---|---|
| 1.1 | n/a: no `by exact` wrapper. |
| 1.2 | n/a: no `by rfl` wrapper. |
| 1.3 | n/a: branch rw closes directly, no following exact to merge. |
| 1.4 | n/a: no simp-plus-exact sequence. |
| 1.5 | n/a: no trailing rfl. |
| 1.6 | n/a: equality proof, no constructor sequence. |
| 1.7 | n/a: no apply-plus-exact. |
| 1.8 | n/a: no contradiction/negation normalization. |
| 1.9 | Existing `fun h ↦ he (...)` is not an eta expansion: body constructs range membership from h; retain. |
| 1.10 | n/a: no have to inline. |
| 1.11 | n/a: no apply/intro sequence; ext introduces the coefficient index. |
| 1.12 | n/a: no redundant show. |
| 1.13 | n/a: no conjunction projections. |
| 1.14 | rw blocks separated by simp_rw/split_ifs, branch-only rw is already one block. |
| 1.15 | n/a: no terminal simp only. |
| 1.16 | simp_rw deliberately rewrites inside the finite sum; no nonterminal bare simp. |
| 1.17 | Existing `notMem_support_iff.1` and `.trans hn` use dot notation; other lemma arguments cannot be shortened meaningfully by dot notation. |
| 1.18 | No trailing by-proof parentheses; existing Finset.mem_range.2 (...) argument has necessary parentheses. |
| 1.19 | n/a: no push_neg. |
| 1.20 | n/a: no private single-use existential witness declaration. |
| 2.1 | Actual fresh native whole-goal grind failed with negated expansion goal; retained coefficient proof. |
| 2.2 | n/a: no grind retained or preliminary grind pipeline. |
| 2.3 | Actual fresh independent proof transports as_sum_range_C_mul_X_pow' and closes with explicit simpa only; this requires local hom transport facts and is not shorter than retained proof. |
| 2.4 | n/a: no analytic function-property proposition. |
| 2.5 | n/a: no positivity or structure-derived nonzero goal. |
| 2.6 | n/a: coefficient equality, no monotonicity inequality subgoal. |
| 2.7 | Direct `Nat.lt_succ_of_le` and transitivity already discharge the arithmetic; no Nat/Int arithmetic tactic block to replace. |
| 2.8 | Actual fresh native aesop failed without progress. |
| 2.9 | n/a: no concrete numeric/cast computation. |
| 2.10 | n/a: arbitrary polynomial/semiring equality cannot be decided by finite computation. |
| 2.11 | n/a: no field denominator. |
| 2.12 | n/a: no ring-ending tactic or polynomial linear-combination identity. |
| 2.13 | Membership/nonmembership branches prove different facts; no symmetric duplicated cases. |
| 2.14 | n/a: no calc to compose. |
| 2.15 | Branches require reconstruction versus vanishing; no repeated closing tactic for common goals. |
| 3.1 | n/a: rw already used, no erw. |
| 3.2 | n/a: no continuity/measurability tactic. |
| 3.3 | No omega present; arithmetic already direct in 2.7. |
| 3.4 | n/a: no rcases/rfl or redundant substitution. |
| 3.5 | Preserve attributes: expanding arbitrary P into a bound-dependent sum is not a universal simplification normal form. |
| 3.6 | No simp_all only to unsqueeze; current proof has no redundant context simplification. |
| 3.7 | No maxHeartbeats scaffold existed or was added. |

Step-back review: the established proof directly splits the coefficient range into
reconstruction and vanishing. The fresh independent transport proof confirms the
same mathematics without invoking this theorem. Whole-goal automation does not
close it. One scoped omission suffices; adding helpers or changing proof strategy
would exceed the useful change for this approved instance revisit. Holistic simplify
review finds no new duplication, cast bridge, manual instance plumbing or awkward
API round trip in the source diff. No built-in simplify command is available, so
this review is performed directly. No rename/decomposition/refactoring follow-up.

## Applied change, independent compatibility and actual axioms

Applied exactly one source line: `omit [Fintype τ] [DecidableEq τ] in`, immediately
before the original expansion docstring. No proof adjustment was needed: the
pre-existing local `classical` suffices. Source 575 → 576 physical lines, diff +1/-0;
target remains 12 declaration lines / 9 physical proof lines. All 25 retained module
declarations, imports, attributes, definitions, documentation and all other public
contracts remain unchanged. Source gate `/private/tmp/roth-separation-r03-source-gates.json`
checks byte-exact equality to HEAD plus this sole insertion and identical block comments.

Fresh native isolated arbitrary-τ proof: `/private/tmp/roth-separation-r03-independent-native.json`
reports success=true, timed_out=false, zero diagnostics. It invokes no project target:
it maps through optionEquivLeft and applies the primed univariate range expansion.

Fresh compiled `/private/tmp/roth-separation-r03-independent.lean` additionally contains:

- `independentNew`, no Fintype/DecidableEq assumptions on τ; proof-irrelevance equality
  `@independentNew = @Roth.eq_sum_X_none_pow_mul_coeffNone` establishes exact NEW quantified type.
- A locally copied ORIGINAL coeffNone definition and `independentOriginal` with exact
  ORIGINAL binder order including both index classes and a separate non-self transport proof.
- `originalAdapter` explicitly retains both ORIGINAL class arguments and applies
  `@Roth.eq_sum_X_none_pow_mul_coeffNone τ R s P n hn`; equality with independentOriginal
  verifies exact original-type recovery. It does not pretend the shortened raw @type is unchanged.
- An actual infinite-index application at τ=ℕ and a compiled X-none/n=0 counterexample
  showing that dropping hn fails mathematically.
- Width-100 #check plus axioms for both independent proofs, adapter, built target,
  direct public caller exists_separated_representation and transitive exists_det_eq_mul.

Final compiler exits 0; `/private/tmp/roth-separation-r03-independent.log` lists only
`propext`, `Classical.choice`, `Quot.sound` for all six printed constants. The initial
scratch-file generation accidentally truncated a nested `:= by` and failed; its full
failure log is preserved as `...-independent-incomplete-generation.log`. The scratch
generator was corrected, no source changed, and the final run is completely successful.

Actual environment-based axiom probe `/private/tmp/roth-separation-r03-actual-axioms.lean`
finds exactly one constant per exact Roth suffix, including private names without
guessing numeric components. Nine actual built constants pass: eq_mapDomain_some_add_single,
coeff_X_none_pow_mul_rename, coeffNone, coeff_coeffNone, target,
linearIndependent_coordinate_polynomials_aux, eq_sum_aeval_basis_coeffNone_aux,
exists_separated_representation, exists_det_eq_mul. Final compiler exits 0 and log
`/private/tmp/roth-separation-r03-actual-axioms.log` lists standard axioms only.
The first scratch axiom command used reserved identifier `matches`; its failed log is
preserved as `...-actual-axioms-reserved-identifier.log`; corrected to `found` and rerun.

Fresh unfiltered native module diagnostics, `/private/tmp/roth-separation-r03-final-lsp.json`:
partial=false, timed_out=false, success=true, failed_dependencies=[], **0 errors,
25 warnings, 0 infos, 0 hints**. Initial complete native diagnostics had 27 warnings.
All three target warnings disappeared; one newly exposed unusedSectionVars warning
reports Fintype τ in the unchanged exists_separated_representation, which no longer
uses that class via this target. It is recorded rather than suppressed or silently
expanding this worker's approved scope. Header metadata is user-preserved.

Actual `/Users/ramin/.elan/bin/lake build Roth.Separation` exited 0 with 1876 jobs;
raw `/private/tmp/roth-separation-r03-module.log`. The direct caller appears only in
Roth/Separation.lean, confirmed by unfiltered project rg; no call-site edit needed.

Final signature syntax has the same 79/32/82-codepoint widths as the initial table.
The scoped omit is a separate preceding command. Width-100 actual compiled reference:

```lean
@Roth.eq_sum_X_none_pow_mul_coeffNone : ∀ {τ : Type u_1} {R : Type u_2} [inst : CommSemiring R]
  (P : MvPolynomial (Option τ) R) {n : ℕ},
  degreeOf none P ≤ n → P = ∑ ν ∈ Finset.range (n + 1), X none ^ ν * (rename some) (Roth.coeffNone P ν)
```

The effective binder change is precisely the two approved omissions; type universes
remain independent, natural exponents and all inequality occurrences remain unchanged.

## Fresh effective-binder/generalisation probes

All 11 fresh compiler probes plus the corrective retry completed and were drained
before final profiling started. Sources `/private/tmp/roth-separation-r03-probe-*.lean`,
runner `/private/tmp/roth-separation-r03-probes.py`, complete outputs and exits
`/private/tmp/roth-separation-r03-probes.json`, concise progress `...-probes.log`.
Each uses `autoImplicit false`, independent universes u/v, unchanged proposition and
the independent non-self mathlib transport proof. No untested negative is claimed.

| Effective binder | Kind/use | Fresh actual candidate(s) | Verified result / action |
|---|---|---|---|
| `{τ : Type*}` | type variable; polynomial index | Drop τ; independently instantiate Type u | Drop fails unknown τ; independent universe compiles. Retain universe-polymorphic τ. |
| `[Fintype τ]` | inherited finite-index instance | Individual drop; replacement Finite; joint drop | All three compile; user-approved full omission applied. No weaker Finite requirement retained. |
| `[DecidableEq τ]` | inherited decidability | Individual drop; joint drop | Both compile; user-approved omission applied, existing local classical remains. |
| `{R : Type*}` | coefficient type | Drop R; independent Type v | Drop fails unknown R; independent universe compiles. Retain arbitrary coefficient type. |
| `[CommSemiring R]` | structure required by unchanged MvPolynomial APIs | Drop; weaken to Semiring | Both fail to synthesize CommSemiring R in the unchanged statement/API; retain. |
| `(P : MvPolynomial (Option τ) R)` | polynomial to reconstruct | Drop P | Fails unknown P in dependent proposition; retain. |
| `{n : ℕ}` | natural exponent range/degree bound | Drop n | Fails unknown n; retain ℕ. Abstract exponent codomain would change polynomial mathematics and is outside approved scope. |
| `(hn : degreeOf none P ≤ n)` | degree bound for zero coefficients outside range | Drop hn | Independent proof fails unknown hn; separate compiled X-none/n=0 counterexample disproves unconditional conclusion. Retain. |

The first drop-τ invocation raced the module's .olean replacement and failed on a
missing object, which is not binder evidence. After the module build completed,
`...-probe-drop-0-retry.log` records the actual unknown-τ failure (and consequent
default-heartbeat failure). Both outputs are preserved in the JSON. No limits raised.

No strict→weak candidate exists: hn is already ≤. No analytic global hypothesis,
bundled conjunction, injectivity, domain, topology or completeness assumption is in
this theorem. Pointwise-localization catalogue does not apply. CommSemiring →
Semiring is the only relevant weaker structure with multiplication and natural
polynomial powers; it already fails in the unchanged statement, so still weaker
nonassociative/nonunital structures cannot support that API without restatement.
Inversion review: the abstract reconstruction fact is already mathlib's univariate
range expansion, and optionEquivLeft supplies the exact coefficient packaging;
no new abstract helper is needed. No unresolved big-change candidate remains.

## Final measured signature and inequality scan

Measured from the final source using Python codepoint lengths (not byte widths).
The declaration syntax is byte-identical to baseline; only the preceding omit differs.

| Final line | Codepoints | Next complete signature component | Arithmetic | Action |
|---|---:|---|---|---|
| 92 | 79 | hn binder plus colon, 28 | 79 + 1 + 28 = 108 > 100 | ok |
| 93 | 32 | equality conclusion, 72 | 32 + 1 + 72 = 105 > 100 | ok |
| 94 | 82 | no next signature line | n/a | ok |

| Final occurrence | Form | Rewrite / rename |
|---|---|---|
| L93 hn | `degreeOf none P ≤ n` | already forward weak inequality, unchanged |
| Signature reversed symbols | no ≥ or > | n/a, zero occurrences |
| Theorem name | no _ge_/_gt_ | no rename |

All signature lines remain ≤100; adding any complete next component would exceed 100.

## Performance: actual repository anchors

After every native/compiler/module/probe request had completed and been drained,
ran the actual repository command (not an extracted namespace):

```text
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Separation.lean
```

First sweep exited 0, raw `/private/tmp/roth-separation-r03-profile.log`, parsed by
`/private/tmp/roth-separation-profile-table.py` to the adjacent `.log.json`.
Target outer-command maximum 26.659 ms (2 anchors from scoped omit/theorem) plus
outer async proof 66.044 ms (1 anchor) = **92.703 ms**. Nested nodes are never added
again. Baseline r02 actual-module total was 85.813 ms; no speed improvement claimed.

Direct caller exists_separated_representation = 847.714 ms, transitive caller
exists_det_eq_mul = 495.352 ms, untouched private basis-expansion helper = 795.787 ms.
No declaration exceeded 1000 ms. Because the direct caller and helper exceeded
750 ms, a second complete isolated actual-module sweep was launched only after the
first exited and was drained. Source unchanged throughout; repeat evidence follows.

## Final gate status

| Gate | Result | Concrete evidence |
|---|---|---|
| lake_build_file | pass | Actual lake build Roth.Separation, exit 0, 1876 jobs; r03-module.log. |
| Native LSP | pass | Complete unfiltered r03-final-lsp.json, partial=false, timed_out=false, failed_dependencies=[], 0 errors/25 warnings/0 infos/0 hints. |
| definition_protected | pass | No definition, abbrev, instance, import or attribute changed. |
| theorem_statement_protected | pass with exact user authorization | Sole scoped omission is precisely the two approved classes; original proposition/docs/proof unchanged. Exact NEW type and explicit ORIGINAL adapter independently compiled. |
| structure_gate | pass | 9 physical proof lines, equality not conjunction, branches 1/2 lines. |
| naming_gate | pass | Expansion name describes mathematics, no forbidden pattern or abbreviation. No rename. |
| line_packing_gate | pass | Initial and final three-row measured tables 79/32/82 plus actual format.width=100 #check. |
| inequality_orientation_gate | pass | Complete per-occurrence table; no ≥/> in signature or hypotheses, no _ge_/_gt_ in name. |
| Independent correctness and compatibility | pass | Native arbitrary-τ non-self proof and compiler new type/original type/adapter/counterexample checks all successful. |
| Actual axioms | pass | Nine exact-suffix actual built constants and six print checks have only propext/Classical.choice/Quot.sound. |
| Source hygiene / arithmetic | pass | Exact +1/-0 line edit, 575→576 source lines, 25 retained declarations, no proof line saved; diff --check exits 0. |
| Whole-original/all-retained compatibility, full project, separate LeanEval, commit/push | parent-owned | Parent performs after explicit worker freeze and before any next source edit; no duplicate parent-wide compiler sweep performed here. |

No helper, sorry, axiom, native_decide, haveI/letI, suppression, limit raise,
profiler scaffold, rename or extra source mutation. All original documentation
preserved. Optional wrapper deletions and Domain widening remain explicitly declined.
No concrete proposal or user decision is pending for this target.

All eleven completion steps:

- [x] Step 1: required references read.
- [x] Step 2: all 24 audit items written before source edit.
- [x] Step 2.5: all five actual searches plus auxiliary variants/common-equivalents review.
- [x] Step 2.6: every effective binder, independent universe proof and public literature check.
- [x] Step 2.7: measured initial/final width table and format.width 100 reference.
- [x] Step 2.8: per-occurrence inequality tables with zero reversed occurrences.
- [x] Step 3: all 42 rule statuses with actual applicable automation attempts.
- [x] Step 4: step-back/holistic simplify review and independent transport proof.
- [x] Step 5a: complete unfiltered successful native LSP.
- [x] Step 5b: actual module, independent compatibility, actual axioms and diff gate block.
- [x] Step 6a: no rename required; dedicated report, no shared log or queue mutation.

Second ACTUAL isolated sweep exited 0 and was drained. Raw
`/private/tmp/roth-separation-r03-profile-repeat.log`, full anchor table adjacent
`.log.json`: target 26.532 + 69.697 = **96.229 ms** (2 command / 1 proof anchors),
direct caller 43.868 + 723.651 = **767.519 ms** (1/1), transitive caller
88.348 + 356.334 = **444.682 ms** (1/1), untouched private basis-expansion helper
119.707 + 589.632 = **709.339 ms** (3/1). Both sweeps contain all 25 declaration
rows with no missing command anchors; coeffNone is the sole definition with no
async proof, as expected. Neither sweep has a declaration ≥1000 ms. Required
≥750 ms repeat was completed; no further source optimization or limit change needed.
Conservative target worst sweep 96.229 ms versus baseline 85.813 ms; no performance
improvement claim, and no whole-project performance inference.

The repeat raw trace contains three invalid UTF-8 byte sequences from interleaved
Unicode trace output. The standard strict reader failed; preserved raw bytes and
used `/private/tmp/roth-separation-r03-profile-table.py`, identical parser logic with
only `log.open(errors='replace')` changed. Numeric/name ASCII command and proof
anchors are intact; no trace line is dropped and no nested timing is added twice.

Performance gate: **pass / FAST-BOARD** for this target, both actual sweeps below budget.
All non-rename/refactoring and simplify follow-ups: none. No pending decision.

**Freeze:** every native Lean/MCP, module/compiler, independent/axiom/binder and both
actual-module profile requests has completed and been drained. Final source SHA256
`695da96521c7eb9a07f5f8271868cd37360e9db65a0c5ca0398aa609ee62e507`.
I explicitly revoke **ALL source ownership**, including Roth/Separation.lean and all
other source files. I am now **report-only** and will make no source edit. Parent
owns fresh whole-original/all-public/all-actual compatibility, sequential full project
and separate LeanEval builds, exact-path commit and successful push before next edit.

## Owner cumulative publication gates

Source FROZEN SHA256 `695da96521c7eb9a07f5f8271868cd37360e9db65a0c5ca0398aa609ee62e507`; leaf ownership revoked and requests drained before owner gates. Owner probe `75432` exit0,47.70s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL25 actual retained standardaxiom checks. `/private/tmp/roth-separation-r03-compatibility.{lean,log,json}`. Owner build session `20590` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,122.33s/31.92s; source hash stable. `/private/tmp/roth-separation-r03-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.
