# Fresh declaration 24/30: `Roth.exists_nat_smul_eq_map`

## Initial audit (written before source edits)

Scope: only this declaration (input lines 374–395, 22 declaration lines, 20 body lines)
and this report. Public type, documentation, and meaning preserved. No new helper planned.
Read lean4/SKILL.md, mathlib-quality/SKILL.md, cleanup Phase 4, full golfing-rules.md and
proof-patterns.md, mathlib-search.md, generalisation-patterns.md, cleanup-gates.md,
style-rules.md, naming-conventions.md, and profiling.md. Parent supplies baseline project checks.

1. LINT: complete initial native LSP: zero errors, six warnings in whole module; none in target.
   Header warning and five reserved instance warnings outside ownership remain untouched.
   Raw: `/private/tmp/roth-d24-initial-lsp.json`.
2. HAVE SCAN: `hN0` (L378) no `by`, one use L389 → inline `Finset.prod_pos`.
   `hint` (L379–387) has `by`, used once by `choose` → retain mathematical content.
3. SET_OPTION: no per-declaration options or limits.
4. SIMP SQUEEZE: L387 terminal `simp [notMem_support_iff.1 hd]`, retain;
   L392 nonterminal `simp only [coeff_monomial, Finset.sum_ite_eq']`, already squeezed;
   L394 terminal `simp`, retain; L395 terminal `simpa`, retain.
5. NAMING: `exists_nat_smul_eq_map` describes existential natural scalar and map equality,
   snake_case, no forbidden abbreviations/numeric schemes. No rename warranted.
6. LINE PACKING: signature table below; multiline existential binder is one syntactic group.
7. BY PLACEMENT: final signature line ends `:= by`.
8. FORMAT: two proof lambdas use `=>` → `↦`; 2-space indentation otherwise correct;
   no empty internal lines, adjacent rewrites cannot merge across `push_cast`.
9. COMMENTS: zero proof comments; preserve all existing docstring/source narrative.
10. DOCSTRING: existing two-line public statement/source docstring preserved byte-for-byte.
11. VISIBILITY: public reusable denominator-clearing contract; one direct caller here.
    Making private would change public API and is not authorized or warranted.
12. STRUCTURE: 20 body lines; longest case branch 5 lines; conjunction packages witness
    positivity with its defining equation, so retain cohesive existential contract.
    No >30-line body or helper extraction needed.
13. MATHLIB: five searches below. Generic localization partial match does not directly give
    positive natural scalar in this module's current imports. Keep public API, test simplification.
14. JUNK DEF: n/a, theorem.
15. EXISTS LEMMA: public nontrivial denominator construction, not a trivial private witness.
16. SHOW vs CHANGE: no `show`.
17. PUSH_NEG: absent.
18. GENERALISE: effective binders precisely universe, σ, G; no inherited section instances.
    Binder table below; concrete rational/integer coefficients essential to requested contract.
19. INEQUALITY: positivity already `0 < N`; no reversed inequalities; table below.
20. NORMAL-FORM: map equation is canonical coefficientwise equality; positivity natural
    witness useful directly to caller. Localization abstraction is available in mathlib.
21. SYNTAX-GEN: current existential order supports direct `obtain ⟨N,U,hN,hU⟩` at caller.
22. IMPORT-FANOUT: n/a, no import planned.
23. CASTS: `(N : ℚ)` and denominator natural-to-rational cast are genuine; `z : ℤ`
    casts into ℚ by expected type. No new diff casts planned.
24. INSTANCE-NAME: n/a, theorem declares no instance.

### Signature widths and inequalities

| Signature line | Codepoints | Next syntactic group | Arithmetic | Action |
|---|---:|---|---|---|
| 374 | 67 | `∃ (N : ℕ) (U : MvPolynomial σ ℤ),` (33) | 67+1+33=101 | justified break |
| 375 | 91 | none | n/a | fits |

The quantified binder group is syntactically indivisible as a complete proposition prefix;
its measured 33 characters justify the break. Native `#check` at `format.width 100` gives:
`@Roth.exists_nat_smul_eq_map : ∀ {σ : Type u_1} (G : MvPolynomial σ ℚ),`
then `∃ N U, 0 < N ∧ (MvPolynomial.map (Int.castRingHom ℚ)) U = ↑N • G`.

| Occurrence | Location | Expression | Action |
|---|---|---|---|
| 1 | conclusion | `0 < N` | correct orientation |
| 2 | local `hN0` | `0 < N` | correct; inline planned |
| — | all signature/hypotheses | zero `≥`/`>` | no rewrite/name change |

### Five actual search methods

| Method | Actual query | Result |
|---|---|---|
| Lean-Finder | clearing denominators multivariate rational polynomial integer multiple | success: `IsLocalization.integerNormalization_spec` (univariate), DenomsClearable evaluation API |
| Loogle | `MvPolynomial, "integer"` | successful empty result for that query |
| LeanSearch | A multivariate polynomial over rational numbers has an integer multiple with integer coefficients | integral-coefficient criterion, no direct clearing theorem |
| Source | exists/smul/multiple/denom in MvPolynomial, polynomial, localization; full-name search | `IsLocalization.exists_integer_multiple`, `exist_integer_multiples`, MvPolynomial localization instance; `/private/tmp/roth-d24-integer-search.txt` |
| Name pattern | native local `exists_nat` | returned target and unrelated facts; index warming, not evidence of absence |

Auxiliary variants: `exists_integer_multiple'`, `exist_integer_multiples_of_finite`,
`integerNormalization_spec`, `MvPolynomial.isLocalization`; common-equivalents lookup
has no matching category. Native `exact?`, `grind`, `aesop` at target entry all failed.
No claim that the result is absent from all of mathlib.

### Generalisation and public literature

| Effective binder | Role/use | Mechanical candidates | Verification/result |
|---|---|---|---|
| universe parameter | arbitrary variable universe | already `Type*`; no narrower universe | #check/exact-original test planned |
| `{σ : Type*}` | polynomial variable type | dropping named σ without replacement is ill-formed; already arbitrary, no finiteness/decidability assumptions | no proposed weakening; dependency is syntactic, not claimed compiler-negative |
| `(G : MvPolynomial σ ℚ)` | arbitrary input polynomial, used throughout | dropping G leaves conclusion unbound; no propositional assumption to weaken | no valid drop candidate; not claimed compiler-negative |

No effective typeclass/proposition hypotheses, strict input inequalities, or pointwise
conditions; no hypothesis weakening applies. Inversion check: rational numerators and
denominators remain throughout proof, so it is not accidentally proving an abstract fact
after a concrete-object unfolding. Localization is a known broader formulation, already
implemented in mathlib; no public restatement proposed.

Actual WebSearch query: `clearing denominators multivariate polynomial rational integer
coefficients localization generalization Stacks`. Top relevant hits: [MIT Algebra II notes]
(https://live.ocw.mit.edu/courses/res-18-012-algebra-ii-student-notes-spring-2022/mit18_702s22_full_lec.pdf),
[Sage localization documentation](https://doc.sagemath.org/html/en/reference/rings/sage/rings/localization.html),
[mathlib DenomsClearable](https://leanprover.github.io/hex/docs/Mathlib/Algebra/Polynomial/DenomsClearable.html).
These describe scaling rational polynomials and general localization; inference: generic
localization is broader, while positive natural scaling is the appropriate original API.
ChatGPT math MCP unavailable in ALL_TOOLS; no pretend consultation.

Issues to fix: inline hN0; mathematical lambda arrows. Signature already packed.
Refactoring needed: none; retain public declaration and witness conjunction.

## Full 42-rule golf pass

| Rule | Status and concrete reason/result |
|---|---|
| 1.1 | n/a: no `by exact` wrapper |
| 1.2 | n/a: no `by rfl` |
| 1.3 | n/a: no adjacent rewrite and exact pair |
| 1.4 | existing final `simpa ... using hc e` already consolidated |
| 1.5 | n/a: no trailing rfl |
| 1.6 | existing existential anonymous constructor retained; no constructor/exact chain |
| 1.7 | n/a: no apply/exact chain |
| 1.8 | n/a: no contradiction proof |
| 1.9 | lambda in `dvd_prod_of_mem` needs argument projection; cannot eta-reduce; arrow corrected |
| 1.10 | APPLIED: hN0 expression inlined into witness constructor, one body line removed |
| 1.11 | n/a: no apply/intro pair |
| 1.12 | n/a: no show |
| 1.13 | already `obtain ⟨k,hk⟩`; no have/projection chain |
| 1.14 | two rewrite calls separated by `push_cast`, cannot merge across cast normalization |
| 1.15 | n/a: sole `simp only` is nonterminal before split_ifs |
| 1.16 | all bare simp calls terminal; nonterminal simp already explicit |
| 1.17 | no suitable dot-notation improvement; `Rat.den_pos` is an argument-free inference |
| 1.18 | no trailing argument parentheses removable without damaging lambda grouping |
| 1.19 | n/a: no push_neg |
| 1.20 | n/a: public nontrivial existential, no disposable private lemma |
| 2.1 | native whole-proof grind FAILED with unresolved existence |
| 2.2 | n/a: no retained grind preprocessing chain |
| 2.3 | existing final simpa retained; no further simp/exact chain |
| 2.4 | n/a: no continuity, smoothness, measurability goal |
| 2.5 | native positivity at witness constructor succeeded, but explicit prod_pos is clearer and already available |
| 2.6 | n/a: no monotone inequality chain; positivity is finite-product positivity |
| 2.7 | n/a: no linear integer arithmetic gap; divisibility uses explicit product factor |
| 2.8 | native whole-proof aesop FAILED to construct clearing denominator |
| 2.9 | no concrete numerical computation; genuine casts normalized once by existing push_cast |
| 2.10 | n/a: arbitrary polynomial existence is not a finite decidable computation |
| 2.11 | n/a: no fraction-field division equality after known denominator identity rewrite |
| 2.12 | n/a: no proof ends in ring/ring_nf |
| 2.13 | n/a: support membership branches are asymmetric mathematics |
| 2.14 | n/a: no calc chain |
| 2.15 | membership/nonmembership branches need different hypotheses, retain focused bullets |
| 3.1 | n/a: no erw |
| 3.2 | n/a: no legacy continuity/measurability tactics |
| 3.3 | n/a: no omega |
| 3.4 | n/a: no rcases-with-rfl followed by redundant simp |
| 3.5 | no attribute added: existential construction is unsuitable for simp/rewrite automation |
| 3.6 | n/a: no simp_all only |
| 3.7 | n/a: no limit option |

Step-back review: native exact? failed at actual declaration entry; native grind/aesop
failed there too. Generic localization requires denominator-submonoid and sign conversion
plus coefficient reconstruction, so the elementary product proof stays easier to follow
without new imports or hypotheses. Its single-use positivity fact composes directly;
the main `hint` contains real denominator reasoning and remains local. No new helper.

## Final change and direct callers

Applied: inline `Finset.prod_pos fun _ _ ↦ Rat.den_pos _` at its sole use and use ↦ for
the remaining mathematical lambda. No new mathematical identifiers: `Finset.prod_pos`
and `Rat.den_pos` already occurred in removed code, and were checked by native symbol
search/source and compilation. Exploratory `MvPolynomial.map_smul` was rejected by
`#check` as nonexistent and was never added to source.

`rg -n exists_nat_smul_eq_map Roth --glob '*.lean'` finds only the declaration and one
direct caller `Roth.exists_primitive_smul_eq` in this same module. No external direct
caller module or call-site edit. No def, import, statement, visibility, universe, or
documentation change. No new helper/instance/attribute/limit/scaffolding.

Final signature widths remain 67 and 91 (67+1+33=101 justifies the sole break); maximum
target line width 92. Input 22 declaration /20 body lines → final 21/19, delta −1.
Module input 571 → final 570 lines. Git diff exactly 2 insertions /3 deletions.

Comments-preserved: all docstring text unchanged, zero proof comments before/after.

### Actual mechanical probes

Native `lean_run_code` `/private/tmp/roth-d24-binders-native.json` attempted each dependency:
with autoImplicit false, dropping σ gives unknown identifier σ; dropping G gives unknown
identifier G. Widening σ from Type* to Sort* is rejected because MvPolynomial requires
a Type argument. These tests are real compiled negative probes, not mathematical
counterexamples. Their native response also noted rebuilding imports while the module
build was pending; final fresh compilation and exact original proof resolve that timing.
The original universe-polymorphic binder shape is verified by #check and independent proof.
Fresh rerun after the module build: `/private/tmp/roth-d24-binders-final-native.json`,
the same three expected negative errors, no stale-import info or timeout.

### Simplify pass

Outcome: ISSUES-FOUND-AND-FIXED (manual equivalent; built-in simplify tool not exposed).
One single-use proof fact inlined; no duplicate skeleton or useful helper identified.
Further automation attempts at the final support case failed or left the other branch;
focused existing simp/simpa branches retained. No source change after this review.

## Final verification and gates

Actual `/Users/ramin/.elan/bin/lake build Roth.Separation` exited **0** (1876 jobs),
raw `/private/tmp/roth-d24-build.log`. Complete unfiltered final native LSP after build
and profile: `/private/tmp/roth-d24-final-complete-lsp.json`, success=true, partial=false,
timed_out=false, failed_dependencies=[], **0 errors /6 warnings /0 info /0 hints**.
All six warnings are unchanged: preserved header; reserved d29/d30 instance warnings.
Target has no diagnostics.

Actual `/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-d24-independent.lean`
exited **0**, successful evidence exclusively `/private/tmp/roth-d24-independent-final.log`.
The harness contains the exact ORIGINAL declaration type (extracted from immutable snapshot),
a separately named independent non-self proof using the final elementary construction,
and an original-signature example applying the actual built target.
It prints both signatures at format.width 100, and actual built axioms for target and
direct caller `Roth.exists_primitive_smul_eq`, plus independent proof. All three report
only `[propext, Classical.choice, Quot.sound]`. Native verify independently reports standard
trust and no suspicious patterns: `/private/tmp/roth-d24-verify-native.json`.
The earlier scratch harness run had an incorrectly unapplied function in its appended
compatibility example; that failed log is **not** successful gate evidence. Corrected rerun
above passes. No repository fix or declaration change was needed.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | PASS | actual lake build Roth.Separation exit0, log above |
| definition_protected | PASS | no def/abbrev/import edits |
| theorem_statement_protected | PASS | exact signature byte equality against original; compiled original example |
| naming_gate | PASS | descriptive snake_case, no forbidden scheme or abbreviation |
| line_packing_gate | PASS | every signature line measured: 67,91; 67+1+33=101 |
| structure_gate | PASS | 19 body lines; case branch ≤5; cohesive witness conjunction retained by scope instruction |
| inequality_orientation_gate | PASS | all positivity expressions already smaller-left; zero ≥/> |
| cumulative_no_unintended_breakage | PASS at worker scope | sole direct caller is same built/LSP-checked module; actual caller axioms standard |
| comments/documentation | PASS | byte-preserved documentation, 0→0 inline proof comments |
| diff hygiene | PASS | actual git diff --check exit0; scoped 2 additions/3 deletions |

No public deletion/generalisation proposal, new helper, unresolved source issue, or external
direct caller. Parent retains responsibility for cumulative original30/public20 compatibility,
whole-project and separate LeanEval builds, shared reports, exact-path commit and push.

### Buzz pass — target

Outcome: **FAST-BOARD**. Baseline actual module log supplied by parent:
`/private/tmp/roth-s23-final-profile.log` and `.json`: command25.247 ms + proof355.005 ms
= **380.252 ms**. Final actual repository command:

```
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Separation.lean
```

Exited **0**; raw `/private/tmp/roth-d24-final-profile.log`, parsed
`/private/tmp/roth-d24-final-profile.log.json` using
`/private/tmp/roth-separation-profile-table.py`. Target has one outer command anchor
**16.223 ms** and one outer async proof anchor **292.695 ms**, conservative sum
**308.918 ms**, with no nested-node double counting. Final async proof anchor occurs
at raw log line714901. Isolated sweep ran with all other compiler/MCP requests drained
and parent idle; successful harness rerun/final LSP happened only after sweep exit.
Repository source did not change. Under750 ms: no repeat needed. Under1000 ms: no
diagnosis/fix needed. No claim of whole-project speedup from a single wall-clock sample.
Limits removed0, added0; profiling scaffolding added0; deferrals0.

## Eleven completion phases

| Phase | Completion |
|---|---|
| 0 Doctor | parent baseline supplied; initial full native LSP captured |
| 1 Prepare | original/current target, context/direct caller, skills/full golf references read |
| 2 Audit | all24 items written before first source edit |
| 3 File fixes | none authorized/needed; existing preserved header and pending instance issues untouched |
| 4 Deep golf | all42 rules with statuses, five searches, binder probes, width/inequality tables |
| 5a Non-rename refactoring | inlined one local proof fact; no API deletion/generalisation |
| 5b Rename | clean mathematical name; no rename or shared queue mutation |
| 6 Final verification | actual module build, exact-original independent proof, built target/caller axioms, full native LSP |
| 6.5 Simplify | manual equivalent completed; built-in tool unavailable; no further useful change |
| 6.6 Buzz | actual isolated repository sweep308.918 ms, under threshold |
| 7 Report | this dedicated report and drained freeze handoff; parent owns cumulative Git/build gates |

## Freeze

All compiler, MCP, and profiler requests have completed; no pending request/session.
ALL source ownership is revoked: **report-only**, no further source edit.
Frozen `Roth/Separation.lean` SHA256:
`39e0e38b16b6b9b3b1feabe00fd135a8746c5f4cf60622c0b8fb46b9cf9f79ca`.

## Owner cumulative publication gates

Source FROZEN SHA256 `39e0e38b16b6b9b3b1feabe00fd135a8746c5f4cf60622c0b8fb46b9cf9f79ca`; leaf ownership revoked and requests drained before owner gates. Owner probe `16927` exit0,40.74s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL26 actual retained standardaxiom checks. `/private/tmp/roth-separation-d24-compatibility.{lean,log,json}`. Owner build session `70044` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,126.18s/28.72s; source hash stable. `/private/tmp/roth-separation-d24-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.
