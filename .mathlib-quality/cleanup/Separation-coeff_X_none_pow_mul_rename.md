# Cleanup: `coeff_X_none_pow_mul_rename` (original d05)

Initial audit written before source edits. Scope: this private lemma only. Starting HEAD
`9a27b9e`, starting module 610 lines. Parent supplies green full/module/separate LeanEval
baseline and actual-module target profile 63.474 + 185.236 = 248.710 ms in
`/private/tmp/roth-separation-d04-final-profile.log{,.json}`. Native complete initial LSP
confirmed 0 errors, 32 warnings, including two unused-in-type instance warnings on target.
Both Lean and mathlib-quality skills, full Phase 4, golfing-rules.md, proof-patterns.md,
mathlib-search.md, generalisation-patterns.md, cleanup-gates.md and relevant
style/naming/profiling references read. No subdelegation, Git/shared-log mutations.

## Initial 24-item audit

| # | Item | Finding/action before editing |
|---|---|---|
| 1 | LINT | Remove private Fintype/DecidableEq requirements if independently verified. |
| 2 | HAVE SCAN | hν bounds ν; anonymous exponent reconstruction; anonymous evaluation of hu. Existing reconstruction calls public theorem with pending assumptions: replace proof strategy rather than touch public API. |
| 3 | SET_OPTION | None on target. |
| 4 | SIMP SQUEEZE | hν simpa closes; simp only at this is nonterminal and correctly squeezed. |
| 5 | NAMING | Describes coefficient of distinguished variable power times renamed polynomial. X/map operation casing follows actual library names; no forbidden abbreviation/pattern. No rename needed. |
| 6 | LINE PACKING | Signature 2 lines; concrete width table to follow. |
| 7 | BY PLACEMENT | by at end of conclusion line. |
| 8 | FORMAT | Standard two-space tactics, no empty body lines; omega should disappear with alternate proof. |
| 9 | COMMENTS | No inline comments in target; preserve surrounding documentation. |
| 10 | DOCSTRING | Private technical helper needs none; do not create public prose. |
| 11 | VISIBILITY | Private helper used by two coefficient calculations. Retain private. |
| 12 | STRUCTURE | 21 body lines with nested order/equality cases; try polynomial equivalence to avoid subtraction casework. |
| 13 | MATHLIB | Actual five searches find optionEquivLeft coefficient correspondence and renamed coefficient API. Exact? fails; no absence claim. Test composed proof. |
| 14 | JUNK DEF | n/a: proposition lemma. |
| 15 | EXISTS LEMMA | n/a: equality, no existential. |
| 16 | SHOW/CHANGE | No original show; any new change must express the composed map's application. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | Test both unused private instances; test CommSemiring→Semiring and binder dependence separately. |
| 19 | INEQUALITY | No inequality in signature. Body has single none ν ≤ e and ν ≤ e none; orientation already ≤. |
| 20 | NORMAL-FORM | Coefficient equality with if e none = ν is application-ready for simp_rw. |
| 21 | SYNTAX-GEN | Keep equality/if form: both actual callers use simp_rw. |
| 22 | IMPORT-FANOUT | No import required: equivalence/coefficient API already imported. |
| 23 | CASTS | No original coercions/ascriptions beyond binder types; audit new map ascriptions for necessity. |
| 24 | INSTANCE-NAME | n/a: no instance declaration. |

Issues: unused private assumptions; nested subtraction proof; omega arithmetic. Proposed
safe action is one retained private helper over arbitrary τ, with equivalence-based proof.
No public contract change authorized/applied. No new helper planned. Literature exempt:
private declaration. Public instance proposal remains pending with parent.

## Applied result and final audit refinements

Only the target changed. `optionEquivLeft` turns the polynomial into
`Polynomial.X ^ ν * Polynomial.C Q`, after verifying equality of the two algebra maps
on generators. The monomial coefficient formula then leaves two equality cases.
Both private instance parameters are omitted; its written conclusion and both call sites
are unchanged. No new helper, declaration, import, attribute, rename, public type change,
comment change or wrapper substitution outside the target.

Corrected exact counts: original declaration 22 lines, comprising 2 signature and 20 body
lines. Final declaration 13 lines, comprising 2 signature and 11 body lines, plus one new
`omit` line. Net module 610 → 602 lines (-8); Git numstat 11 additions / 19 deletions.
The initial rough STRUCTURE estimate of 21 body lines is superseded by these measured counts.

Final HAVE scan: `h` at L60 has a three-line tactic proof and is used once to evaluate the
map equality; keep proof content. `hQ` at L63 is used once without `by`; an actual attempt
to inline it with its full type ascription **fails** because `rw` re-infers the composed
AlgHom application as the rewrite pattern, which does not occur syntactically. Keeping the
typed local equality provides the folded rewrite pattern. Failure is captured in
`/private/tmp/roth-separation-d05-inline-failure.json`; this is a verified load-bearing
bridge, not an untested exemption. Original hν/reconstruction/evaluation haves disappear.
All three final simp calls close their local goal, so no nonterminal simp needs squeezing.
No casts introduced; h's map type and hQ's equality type are load-bearing elaboration types.
No inequality remains in the target. Name remains descriptive and free of forbidden patterns.

## Five actual mathlib searches

Raw native results: `/private/tmp/roth-separation-d05-{finder,loogle,leansearch,names}.json`.
Full source search: `/private/tmp/roth-separation-d05-source-search.log`.

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | coefficient of X none power times rename some multivariate polynomial | Found optionEquivLeft_coeff_some_coeff_none, coeff_rename_eq_zero, coeff_rename_embDomain, coeff_rename_mapDomain. |
| B Loogle | MvPolynomial.coeff (MvPolynomial.rename _ _) _; then Polynomial.coeff, Polynomial.monomial | First query failed with unknown constant in remote index, not absence. Second returned coeff_monomial, coeff_monomial_same, coeff_monomial_of_ne and related results. |
| C LeanSearch | coefficient of a power of the distinguished variable times a renamed multivariate polynomial | Found coeff_X_pow and rename coefficient API. |
| D Source | full target name; coeff_X_pow.*rename; optionEquivLeft.*rename/coeff; X_pow_mul_C; C_mul_X_pow_eq_monomial; aeval_rename | Located coefficient correspondence, generator images, monomial coefficient and multiplication APIs. Two local caller references found. |
| E Name pattern | optionEquivLeft, limit30 | Found all required equivalence lemmas; index warming, so no absence claim from index. Source and #check independently verify names. |

Auxiliary variants checked: coeff_monomial_same/of_ne, coeff_rename_eq_zero/mapDomain/embDomain,
optionEquivLeft_X_none/X_some, aeval_rename, Polynomial.CAlgHom and X_pow_mul_C.
Common-equivalents lookup: none of topology/finiteness/bornology buckets match this
polynomial coefficient statement. Conclusion: partial library matches permit a much
shorter direct proof. This retained helper is not a 1–3-call wrapper: generator-map
extensionality, application congruence, coefficient transport, map multiplication/power,
commutation/monomial normalization and equality cases are all required. It remains useful
to both `simp_rw` callers. No exact duplicate claimed absent from all mathlib.

`exact?`, `grind`, bare `simp` and `aesop` actually failed at the original full goal.
Fresh final full-goal tests at L59 again fail; raw
`/private/tmp/roth-separation-d05-whole-automation.json`. The aesop test's additional
unknown-ν/unused-simp errors come from running the residual original tail after its
context-changing tactic; these tail artifacts are not treated as independent failures.
An additional L68 branch probe hit the positive branch without its focus dot and hence
left the negative branch untouched; `/private/tmp/roth-separation-d05-final-automation.json`
is explicitly invalid as a whole-proof replacement or a negative-branch test.

## Generalisation status: every effective original binder

| Binder | Class | Use / mechanical candidates | Actual verification and result |
|---|---|---|---|
| `{τ : Type*}` | type variable | Domain of Option and MvPolynomial; universe already polymorphic. | Drop under autoImplicit=false fails unknown τ. Independent u/v candidate passes. Keep. |
| `[Fintype τ]` | typeclass | Only original public reconstruction call required it; drop is weaker than Finite replacement. | Candidate without both index instances succeeds; actual file with omit and complete LSP succeeds. Drop kept. |
| `[DecidableEq τ]` | decidability | Statement independent; proof can use local classical. | Candidate without both index instances succeeds; actual file/complete LSP succeeds. Drop kept. |
| `{R : Type*}` | type variable | Coefficient type in both sides; universe independent from τ. | Drop fails unknown R. Independent u/v candidate passes. Keep. |
| `[CommSemiring R]` | algebra class | rename, optionEquivLeft and polynomial multiplication use this API. | Class drop fails synthesize CommSemiring. Semiring weakening separately fails same requirement in statement; retain. |
| `(ν : ℕ)` | value | Power and equality test on the distinguished exponent. | Drop fails unknown ν. Arbitrary exponent structure would restate the MvPolynomial exponent API, not a mechanical weakening. Keep. |
| `(Q : MvPolynomial τ R)` | value | Polynomial factor and coefficient. | Drop fails unknown Q.coeff. General object changes meaning; keep. |
| `(e : Option τ →₀ ℕ)` | value | Coefficient index and restriction. | Drop fails unknown e. Replacing with arbitrary functions loses finite-support type; keep. |

Native raw drop probes `/private/tmp/roth-separation-d05-binder-probes.json`; parent-class
probe `/private/tmp/roth-separation-d05-semiring-probe.json`. Successful strongest omission
candidate `/private/tmp/roth-separation-d05-candidate.json` has success=true, timed_out=false,
empty diagnostics. This verifies complete omission, so adding Finite/Fintype.ofFinite would
be unnecessary. Strict→weak, point localisation, conjunction unbundling do not apply: no
propositional/function-property assumption exists. Universe test separates u/v already.
Inversion check: option syntax is the canonical distinguished-variable presentation; no
fixed named witness is unfolded whose property could be abstracted. Arbitrary injection
with a distinguished complement would require a conclusion restatement, not a routine
binder weakening. No new concrete public proposal from this private declaration.

Literature: n/a, private declaration; explicit skill exemption applies. The existing public
12-theorem instance-removal menu remains PENDING in `Separation-instance-proposal.md`.

## Signature width and inequality tables

Width-100 original `#check @D05.original` in independent log:

```lean
@original : ∀ {τ : Type u_3} [Fintype τ] [DecidableEq τ] {R : Type u_4} [inst : CommSemiring R] (ν : ℕ)
  (Q : MvPolynomial τ R) (e : Option τ →₀ ℕ),
  (X none ^ ν * (rename some) Q).coeff e = if e none = ν then Q.coeff e.some else 0
```

| Signature line | Codepoints | Next unit | Arithmetic | Action |
|---|---:|---|---|---|
| L57 | 94 | complete conclusion, 95 without indentation | 94 + 1 + 95 = 190 > 100 | ok |
| L58 | 99 | none: proof follows | n/a | ok |

The scoped `omit` at L56 is 35 characters; it is an enclosing command, not a signature
binder line. It cannot absorb the 94-character declaration (35 + 1 + 94 = 130 > 100).
Signature written syntax is byte-identical; only scoped effective private instances change.

| Location | Original inequality | Rewrite | Rename |
|---|---|---|---|
| Signature and all parameter types | none; no ≥ or > | none | none |
| Original body | single none ν ≤ e; ν ≤ e none | casework removed | none |

## All 42 golfing rules

| Rule | Concrete status |
|---|---|
| 1.1 by exact | n/a: no no-op by-exact wrapper in source. |
| 1.2 by rfl | n/a: neither proof is by-rfl. |
| 1.3 rw + exact | Original negative-order exact chain removed with old strategy; final rw is followed by case split, not exact. |
| 1.4 simp + exact | Original hν simpa removed; final simp already closes its goal. |
| 1.5 trailing rfl | n/a: none. |
| 1.6 constructor pairs | n/a: no conjunction or constructor pair. |
| 1.7 apply + exact | n/a: no such chain. |
| 1.8 contradiction + push_neg | n/a: no by_contra or push_neg. |
| 1.9 eta reduction | Original evaluation lambda disappears; no reducible lambda remains. |
| 1.10 inline single-use have | Original three haves disappear. Final h has tactic proof; hQ inline with ascription tested and fails rw matching. Retained for verified type bridge. |
| 1.11 apply + intro | n/a: no such pair. |
| 1.12 redundant show | n/a: none in source; no term-mode show needed. |
| 1.13 have + projections | n/a: neither proof destructures conjunction projections. |
| 1.14 merge rw | Applied: a single final rw transports and normalizes the coefficient. |
| 1.15 terminal simp only | Original nonterminal squeeze removed with subtraction proof; final terminal simp unsqueezed. |
| 1.16 nonterminal bare simp | n/a: three final simp calls each close their local goal. |
| 1.17 dot notation | `toAlgHom.comp` already uses dot; hQ uses named AlgHom.congr_fun to specify its exact operation. |
| 1.18 use <\| | n/a: no terminal parenthesized proof/lambda argument in final. |
| 1.19 push_neg | n/a: none. |
| 1.20 trivial ∃ wrapper | n/a: equality with two actual consumers, not an existential. |
| 2.1 whole grind | Actually tested before and after; fails the coefficient identity. |
| 2.2 delete before grind | n/a: final proof contains no grind. |
| 2.3 simpa consolidation | No simp-plus-closing-tail remains; native whole simp fails, so transport is required. |
| 2.4 fun_prop | n/a: no continuity/differentiability/measurability claim. |
| 2.5 positivity | n/a: final goal is coefficient equality, no positivity subgoal. |
| 2.6 gcongr | n/a: no inequality or monotonicity goal in final. |
| 2.7 lia/omega | Original arithmetic need eliminated by equivalence proof; no arithmetic terminal goal remains to run lia on. |
| 2.8 aesop | Whole-goal test actually fails; keep explicit API proof. |
| 2.9 norm_num/cast | n/a: no concrete numerical computation or coercion target. |
| 2.10 decide/kernel | n/a: equality depends on arbitrary polynomial, so not finite computation. |
| 2.11 field_simp; ring | n/a: CommSemiring statement, no inverses/denominators. |
| 2.12 linear_combination | n/a: no ring/ring_nf ending or coefficient ring hypotheses. |
| 2.13 wlog | n/a: equality vs disequality cases have distinct zero/nonzero coefficient conclusions. |
| 2.14 collapse calc | n/a: no calc. |
| 2.15 shared <;> | Original arithmetic branches replaced; final case simp arguments differ and each is explicit. Shared unconditional ext/cases simp in surrounding theorem untouched. |
| 3.1 erw→rw | n/a: no erw. |
| 3.2 legacy function tactic | n/a: none. |
| 3.3 omega→lia | Applied stronger strategy: omega disappears entirely; no surviving arithmetic to translate. |
| 3.4 rcases rfl | n/a: no rcases. |
| 3.5 automation attributes | Private rewrite helper is explicitly supplied to two simp_rw calls; no global registration needed. |
| 3.6 simp_all | Final branch experiment at L68 only closes positive goal and leaves negative goal untouched; not accepted as replacement. Explicit terminal simp retained. |
| 3.7 limits | n/a: no target maxHeartbeats/maxRecDepth; none added. |

## Step back / simplify review

The alternative strategy removes subtraction and inequality reasoning entirely. Whole
automation does not know the coefficient transform without hints. Exact? does not close
the statement. A shorter direct term would still need the generator-map proof, the typed
application bridge, coefficient normalization and the two cases. No duplicate skeleton
justifies a new helper. Tested hQ inlining fails, so its explicit type earns its line.
`ext i : 1` was also tested in an isolated candidate and succeeds; changing a single tactic
for no measured benefit is below the minimum-value threshold, so existing `ext i` retained.
No source edits were made for discarded probes. Built-in simplify callable absent; the
equivalent holistic inspection was performed directly. Outcome: PASS-THROUGH after the
main rewrite; no additional fixes, suggestions or extraction flags.

## Verification and diff gates

Actual `/Users/ramin/.elan/bin/lake build Roth.Separation` exited 0 (1876 jobs), raw
`/private/tmp/roth-separation-d05-build.log`. Complete unfiltered native LSP:
`/private/tmp/roth-separation-d05-final-lsp.json`, success=true, partial=false,
timed_out=false, no failed dependencies, **0 errors / 31 warnings**. Two target warnings
are gone, and an existing pending public caller, coeff_rename_mul_aeval, newly exposes
its own unusedSectionVars pair: 32 - 2 + 1 = 31. No warning suppressed. Header warning is
explicitly user-preserved. Parent notified of this newly visible caller warning.

Independent exact ORIGINAL effective type and non-self proof:
`/private/tmp/roth-separation-d05-independent.lean` and `.log`, actual
`lake env lean ...` exit 0. This restores both original instance arguments and proves
the original conclusion by the old coefficient/subtraction route, with the previously
removed mapDomain wrapper substituted by its exact direct library lemma. It never calls
the target. Width-100 type and axioms [propext, Classical.choice, Quot.sound] printed.

Actual **built** target and affected public axioms checked via exact suffix lookup in the
imported environment, not guessed private indices:
`/private/tmp/roth-separation-d05-axioms.lean` and `.log`, `lake env lean ...` exit 0.
Actual target is `_private.Roth.Separation.0.Roth.coeff_X_none_pow_mul_rename`; printed
effective type confirms no Fintype/DecidableEq. Also checked eq_sum_X_none_pow_mul_coeffNone,
coeff_rename_mul_aeval, exists_separated_representation, exists_int_factors,
exists_det_eq_mul. Every one has only propext, Classical.choice, Quot.sound.

| Introduced identifier | Verification | Result |
|---|---|---|
| optionEquivLeft_coeff_some_coeff_none; optionEquivLeft_X_none | source, native name search, #check | pass |
| Polynomial.CAlgHom; X_pow_mul_C; C_mul_X_pow_eq_monomial; coeff_monomial | source, Loogle for coefficient API, compiled #check | pass |
| AlgHom.congr_fun; Ne.symm | compiled #check | pass |

Identifier raw log `/private/tmp/roth-separation-d05-identifiers.json` succeeds. No new
unverified lemma name. Git diff --check exits 0. Only one source hunk, exactly target.
Original previous-wrapper substitutions in every other declaration remain byte-identical.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | actual module build exit0 above |
| definition_protected | pass | no def/abbrev changed |
| theorem_statement_protected | pass | written target statement unchanged; private omit authorized and compiler-verified; public contracts unchanged |
| structure_gate | pass | body11, no conjunction, branches1 line each |
| naming_gate | pass | descriptive coefficient name, no forbidden pattern/abbreviation |
| line_packing_gate | pass | complete two-line table above, both ok |
| inequality_orientation_gate | pass | zero ≥/> in all effective binders and statement |
| comment_preservation | pass | no proof comments existed; all surrounding docs untouched |
| cumulative caller module | pass | actual same-module callers compile unchanged |
| full project / separate LeanEval / cumulative original compatibility | parent gate | parent explicitly owns sequential post-freeze checks; not falsely claimed run here |

## Buzz: actual repository-module anchored profile

Exact command `/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true
-Dtrace.profiler.threshold=0 Roth/Separation.lean` exited 0. Raw 110MB
`/private/tmp/roth-separation-d05-final-profile.log`; compact exact source/line anchors
`/private/tmp/roth-separation-d05-profile-anchors.json`. Baseline supplied actual module
log `/private/tmp/roth-separation-d04-final-profile.log`, unchanged target at dispatch.
No namespace-copy surrogate or aggregate-only performance evidence used.

| Actual declaration | Before command + outer async (ms) | Final command + outer async (ms) |
|---|---:|---:|
| target | 63.474 + 185.236 = 248.710 | 60.400 + 209.913 = 270.313 |
| eq_sum_X_none_pow_mul_coeffNone | 29.284 + 110.113 = 139.397 | 25.109 + 132.748 = 157.857 |
| coeff_rename_mul_aeval | 45.540 + 479.209 = 524.749 | 34.074 + 394.429 = 428.503 |

Target final outer omit command anchor line25561 and outer async proof line25586.
The generated inner private-theorem command57.510 and private-lemma command58.094
are nested elaboration and not added again. Baseline command line25421/async25456.
Caller command/proof anchors final73968/76730 and87170/91660; baseline69065/71832 and
82384/86879. All conservative totals below750ms, hence no threshold-triggered second
sweep. Budget1000ms. Outcome FAST-BOARD; no raised limits, profiler scaffolding or
deferrals. These noisy wall-clock observations do not establish a target or whole-project
speedup; the benefit is less casework and strictly weaker private assumptions.

## Eleven completion steps

- [✓] Step1: both skills and full required references read.
- [✓] Step2: all24 audit entries written before source edits, refined above.
- [✓] Step2.5: five actual search methods, failure/partial-index caveats recorded.
- [✓] Step2.6: every effective binder, actual drop/weakening probes, private literature exemption.
- [✓] Step2.7: complete signature width arithmetic and width100 type.
- [✓] Step2.8: complete inequality scan, no reverse inequalities.
- [✓] Step3: all42 golfing rules have concrete statuses.
- [✓] Step4: alternate strategy, automation, typed bridge and holistic simplify review.
- [✓] Step5a: complete unfiltered LSP 0 errors/31 warnings; no target warnings.
- [✓] Step5b: real module/independent/actual axioms/anchored profile and focused diff gates.
- [✓] Step6a: no rename needed; no shared queue mutated.

No new helper requires another audit. Renames queued: none. Comments preserved: none in
target, all existing surrounding documentation unchanged. Refactoring needed: no new item;
public instance-removal menu remains pending with parent.

## Freeze

All own native MCP calls and module/independent/axiom/profile processes completed and
drained. No source edits after the final build/profile/LSP. Source ownership is revoked
for **all** of Roth/Separation.lean; this worker is report-only. Frozen SHA256:
`c6488cc1c5738d1f9e69b7267a0ad182c823f7bacd02c347e644d710ff559c3f`.
Parent owns cumulative compatibility, full-project/separate LeanEval builds, exact-path
Git commit and successful push before proceeding to the next declaration.

## Owner cumulative publication gates

Source FROZEN SHA256 `c6488cc1c5738d1f9e69b7267a0ad182c823f7bacd02c347e644d710ff559c3f`; leaf ownership revoked and requests drained before owner gates. Owner probe `16920` exit0,48.70s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL27 actual retained standardaxiom checks. `/private/tmp/roth-separation-d05-compatibility.{lean,log,json}`. Owner build session `8141` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,139.72s/32.94s; source hash stable. `/private/tmp/roth-separation-d05-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.
