# exists_sum_mul_eq_gcd — fresh declaration 23 audit

Initial audit recorded before repository source edits. Scope: original declaration 23/30,
current lines 368–387 (20 declaration lines; 18 proof-body lines). Skills read:
`golfing-rules.md`, `proof-patterns.md`, `mathlib-search.md`,
`generalisation-patterns.md`, `cleanup-gates.md`, style/naming/profiling references,
Lean skill and installed cleanup Phase 4. Header metadata/public contract preserved.

## Initial 24-item audit

1. LINT: complete native unfiltered LSP: 0 errors, 6 warnings (header and later public
   instance warnings), no warning in this declaration.
2. HAVE: L377 `hs : ... := by ...`, used once at L386; proof content, not trivial term.
   Original induction replaces this whole block using existing mathlib.
3. SET_OPTION: none.
4. SIMP: L372 terminal `simp`, unsqueezed correctly; no nonterminal simp.
5. NAMING: `exists_sum_mul_eq_gcd` describes existential sum/multiplication/gcd equality;
   snake_case, no forbidden abbreviations or number patterns; no rename required.
6. LINE PACKING: table below; whole existential conclusion cannot fit after binders.
7. BY: on signature end.
8. FORMAT: 2-space tactics; no blank proof lines; original consecutive rewrites are
   separated by meaningful operations. No haveI/letI.
9. COMMENTS: no inline comments; docstring preserved verbatim.
10. DOCSTRING: public finite Bézout identity with source/application motivation retained.
11. VISIBILITY: public API retained; sole in-project call is in this file. Deletion is a
    substantive public decision, compiled proposal sent separately before application.
12. STRUCTURE: 18 body lines; insert branch >10 lines. Existing library proof eliminates
    that branch and avoids any helper. No conjunction in statement.
13. MATHLIB: five actual methods below find imported `Finset.gcd_eq_sum_mul`.
14. JUNK DEF: n/a theorem.
15. EXISTS LEMMA: public nontrivial theorem, not private reflexive witness.
16. SHOW/CHANGE: none.
17. PUSH_NEG: none.
18. GENERALISE: every effective binder below. No section instances in elaborated type.
19. INEQUALITY: none, table below.
20. NORMAL-FORM: finite gcd equals a linear combination is canonical library form;
    current product/equality orientation differs by commutativity/symmetry only.
21. SYNTAX-GEN: explicit finite support/family is convenient for gcd-one application.
22. IMPORT-FANOUT: no new imports needed; library lemma already available.
23. CASTS: no explicit casts in source; integer gcd already has integer codomain.
24. INSTANCE-NAME: n/a theorem, not an instance.

| Signature line | Codepoints | Next unit | Arithmetic | Action |
|---|---:|---|---|---|
| 368 | 70 | full existential conclusion (47) | 70+1+47=118 >100 | keep break |
| 369 | 51 | no next signature unit | n/a | keep |

The existential conclusion is one syntactic unit; its bound variable and body remain
on the same continuation line. Native `format.width 100; #check @...` confirms:
`∀ {ι : Type u_1} (s : Finset ι) (u : ι → ℤ), ∃ z, ∑ i ∈ s, z i * u i = s.gcd u`.

| Inequality occurrence | Location | Rewrite |
|---|---|---|
| none | complete signature/hypotheses | n/a, no ≥ or > |

## Actual mathlib searches

A. Native Lean-Finder: "finite family integers greatest common divisor integer linear
   combination Bezout": Int.gcd_eq_gcd_ab, Int.gcd_dvd_iff, gcd_least_linear.
B. Native Loogle `Finset.gcd, ∃ _, _`: **Finset.gcd_eq_sum_mul** exact general equivalent,
   plus extract_gcd/extract_gcd'.
C. Native LeanSearch "greatest common divisor of finite integers is an integer linear
   combination": binary Int.gcd_eq_gcd_ab and gcd_least_linear.
D. Actual untruncated `rg` in Mathlib/Roth: declaration at
   Mathlib/RingTheory/PrincipalIdealDomain.lean:233, existing callers in ZPowers/Lemmas
   and NumberTheory/Height/NumberField; exactly one project direct caller.
E. Native local name search `gcd_eq`: hits binary gcd results, index warming. This is
   positive source evidence only, not a claim of indexed absence. Candidate checked by
   actual native compilation, including typeclass inference of integer IsBezout.
Raw native results: `/private/tmp/roth-s23-{finder,loogle,leansearch,local,lsp}.json`.
Auxiliary variants: gcd_dvd_iff, gcd_eq_gcd_ab, extract_gcd, extract_gcd'.
Common equivalents table has no Bézout bucket. All six strict rules considered:
existing lemma found, general typeclasses used, no new predicates/API, exact compiled
specialization, wrapper deletion proposed for authorized parent decision; no absence claim.

## Generalisation: every effective binder

| Binder | Kind | Role | Candidate | Verification/result |
|---|---|---|---|---|
| `{ι : Type*}` | universe/type | arbitrary finite index type | universe polymorphism already present | native #check confirms Type u; dropping is ill-scoped, not tested negative |
| `(s : Finset ι)` | structure value | finite support of gcd/sum | no parent-class, strict/pointwise hypothesis; arbitrary finite set already | no weakening applicable; dropping changes statement |
| `(u : ι → ℤ)` | structure value | integer family | replace ℤ by CommRing + IsBezout + NormalizedGCDMonoid | compiled library theorem already has precisely these assumptions; substantive alternative, not applied |

Ambient τ/Fintype/DecidableEq do not occur in elaborated type; no public omission
proposed or applied. No proposition, order, topology, decidability hypothesis to weaken.
Integer codomain preserved.

Public literature: actual web search finite integer Bézout identity found
[Gordon NTIC](https://math.gordon.edu/ntic/ntic2020/section-bezout-id.html),
[William Aitken handout](https://public.csusm.edu/aitken_html/m422/Handout1.pdf), and
[Bézout identity](https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity).
Canonical gcd/linear-combination formulation agrees. Bézout domains provide abstract
extension, already in mathlib rather than a new local public generalization.
ChatGPT math MCP: unavailable (no tool in ALL_TOOLS).

Initial action: compile public-deletion scratch proposal; preserve API while replacing
18-line induction by direct library specialization (routine proof-only authorization).

## All 42 golfing rules

| Rule | Concrete disposition |
|---|---|
| 1.1 | n/a no `by exact` wrapper |
| 1.2 | n/a no `by rfl` |
| 1.3 | n/a no rw/exact ending |
| 1.4 | Applied stronger whole-proof simpa specialization |
| 1.5 | n/a no trailing rfl |
| 1.6 | Original witnesses already anonymous; library replaces all |
| 1.7 | n/a no apply/exact chain |
| 1.8 | n/a no contradiction/push_neg |
| 1.9 | n/a original conditional lambda is not eta; gone in final |
| 1.10 | hs has proof content; entire block eliminated by library |
| 1.11 | n/a no apply/intro |
| 1.12 | n/a no show |
| 1.13 | Original obtain already idiomatic; no projection pattern |
| 1.14 | Original rw separated by beta_reduce; all gone in final |
| 1.15 | Final terminal simpa unsqueezed |
| 1.16 | n/a no nonterminal simp |
| 1.17 | `Finset.gcd_eq_sum_mul s u` names key API clearly; dot notation not shorter here |
| 1.18 | n/a no trailing parenthesis/closure |
| 1.19 | n/a no push_neg |
| 1.20 | n/a public nontrivial existential; optional public deletion separately proposed |
| 2.1 | Actual native multi_attempt grind failed existential witness construction |
| 2.2 | n/a no grind retained |
| 2.3 | Applied one-line `simpa [eq_comm, mul_comm] using ...`; native isolated compile succeeded |
| 2.4 | n/a no function regularity goal |
| 2.5 | n/a no positivity goal |
| 2.6 | n/a no inequalities |
| 2.7 | Actual native lia failed existential; library solves |
| 2.8 | Actual native aesop failed to progress |
| 2.9 | n/a no numeric/cast goal after library replacement |
| 2.10 | n/a infinite family existential not finite decidable computation |
| 2.11 | n/a no denominators |
| 2.12 | Original ring identities eliminated before retaining any ring endpoint; no surviving target for linear_combination |
| 2.13 | n/a no symmetric branches; insertion induction replaced |
| 2.14 | n/a no calc |
| 2.15 | n/a one goal in final proof |
| 3.1 | n/a no erw |
| 3.2 | n/a no continuity/measurability |
| 3.3 | lia tried in 2.7; no omega |
| 3.4 | n/a no rcases/rfl |
| 3.5 | No attribute: existential theorem should not rewrite or globally spawn witnesses |
| 3.6 | n/a no simp_all only |
| 3.7 | n/a no limits |

Native multi_attempt was actually run at original line 370: grind/simp/aesop/lia
failed the initial goal; exact? did not close it; apply? offered only partial routes.
Its multi-line replacement attempt additionally encountered leftover original branches,
so that attempt is **not** counted as a successful complete proof. Separate native
`lean_run_code` compiled both two-line specialization and final one-line simpa with
success=true/timed_out=false (final variant zero diagnostics). These are the successful
whole-proof validations.

Step-back: the induction is redundant. A two-line witness extraction works, but the
one-line simpa is shorter, reads directly as the library specialization, and removes
all classical setup, auxiliary sum algebra and branch structure. Term-mode would need
an explicit existential map and obscure the simple orientation change. No new helper.

Inversion check: concrete ℤ was used to construct binary gcd coefficients in the old
proof; final proof exposes the abstract IsBezout theorem already in mathlib. No new
abstract local declaration is appropriate.

## Eleven-step completion ledger

1. Read reference workflow, full golfing and proof-pattern checklists.
2. Recorded full 24-item initial audit before edit, with search/generalisation tables.
3. Considered all 42 rules and actually tested applicable automation/library tactics.
4. Step-back chose whole-proof existing-library specialization.
5. Actual module build and full native LSP, plus diff/structure/type gates below.
6. Refactoring: public wrapper deletion concrete compiled scratch proposal sent; no
   unapproved public deletion/generalization, no renames/new helpers.
7. Cumulative concerns handed to parent (original30/public20 compatibility ledger).
8. Simplification pass: direct single simpa now minimal; no adjacent proof duplication.
9. Performance pass: actual repository profile required after all other jobs drain.
10. Report and verify line arithmetic, actual built target/direct caller axioms.
11. Freeze SHA/revoke source ownership and parent final sequential project/LeanEval,
    compatibility, exact-path commit/push before declaration 24.

## Final verification gates

| Gate | Result | Actual evidence |
|---|---|---|
| lake_build_file | PASS | `/Users/ramin/.elan/bin/lake build Roth.Separation`, exit 0, 1876 jobs; `/private/tmp/roth-s23-build.log` |
| definition_protected | PASS | no def/abbrev changes |
| theorem_statement_protected | PASS | original signature and docs byte-identical; exact ORIGINAL independent induction compiles and theorem equality closes by proof irrelevance `rfl` |
| structure_gate | PASS | final body one tactic, declaration 3 lines; no branches/conjunction/helper |
| naming_gate | PASS | mathematical snake_case, no forbidden patterns |
| line_packing_gate | PASS | signature remains 70/51 codepoints as table; proof 59 codepoints |
| inequality_orientation_gate | PASS | zero ≥/> in signature/hypotheses |

Complete unfiltered native final LSP is saved raw at
`/private/tmp/roth-s23-final-lsp.json`: partial=false, timed_out=false,
success=true, failed_dependencies=[], **0 errors, 6 warnings, 0 infos/suggestions**.
All warnings are preserved header metadata or later original public instance proposals;
none comes from this theorem. No suppressions.

Original exact-type + independent nonself proof: `/private/tmp/roth-s23-original-nonself.lean`
contains the ORIGINAL induction copied from the immutable snapshot under a fresh namespace;
its proof never calls the target theorem. Compiler exit 0, log
`/private/tmp/roth-s23-original-nonself.log`. The probe also checks equality of the actual
built target with the independently proved theorem by `rfl` (proof irrelevance).
`#print axioms` for actual built target, sole direct caller
`Roth.exists_int_eq_of_gcd_eq_one`, and independent original proof all return only
`propext`, `Classical.choice`, `Quot.sound`. No external direct caller: fresh full-project
Lean-source rg in `/private/tmp/roth-s23-direct-references.log` contains only declaration
and one same-file caller. The caller proof was not edited.

Optional deletion proposal: `/private/tmp/roth-s23-deletion-candidate.lean` is a full-file
scratch candidate; compiled exit 0, `/private/tmp/roth-s23-deletion-candidate.log`;
exact diff `/private/tmp/roth-s23-deletion-candidate.diff`. It deletes this public API and
substitutes `Finset.gcd_eq_sum_mul` in the sole caller with local orientation correction.
Sent to parent BEFORE any application; **not authorized or applied**. Parent recommends
retaining the one-line public orientation wrapper. Preserved public contract takes
precedence over skill's default delete-wrapper preference.

Arithmetic: file 588→571 lines (−17); target 20→3 declaration lines; proof body 18→1.
Git source diff is 1 insertion, 18 deletions. No helper/declaration added or removed.

## Actual performance and freeze

After **all** native MCP, standalone compiler, candidate compiler, and module-build
requests drained, the sole final profiler ran to exit 0:

```
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Separation.lean
```

Actual anchored logs: baseline `/private/tmp/roth-s22-final-profile.log` and final
`/private/tmp/roth-s23-final-profile.log`; parsed JSON next to each log. Parser:
`/private/tmp/roth-separation-profile-table.py`. Repository declaration anchors,
outer command + outer async proof, no nested double-counting:

| Target | Command ms | Async proof ms | Conservative total ms |
|---|---:|---:|---:|
| baseline original proof | 10.047 | 112.298 | 122.345 |
| final retained wrapper | 9.730 | 87.199 | 96.929 |

Exactly one command anchor and one proof anchor each. Final <750 ms: no repeat
threshold triggered; <1000 ms budget. Ordinary wall-clock variation prevents a broad
project performance claim. Main improvement is replacing manual induction by library API.

Final source SHA256:
`f03aa9bb53b186f2d5a5de7d7397589894aacf28f8c2cea2bbd3f0d1d2529f20`.
`git diff --check` passes. All owned MCP/compiler/build/profile requests have completed;
no background requests remain. **ALL source ownership revoked; worker is report-only.**
No source edits after this freeze. Parent owns the sequential cumulative full-project
and separate LeanEval builds, original30/public20 compatibility, exact-path commit and
successful push before original declaration 24. No Git mutation performed by worker.


## Owner scope decision on optional deletion

The full-file deletion candidate and sole-caller repair compile, but no deletion is approved or applied. The retained wrapper now has a one-line proof and preserves the public orientation API. Retention is recommended: removing the public name gives little code benefit and moves orientation handling into its caller. This optional alternative is concrete and reviewable; it is not required input or a completion blocker.

## Owner cumulative publication gates

Source FROZEN SHA256 `f03aa9bb53b186f2d5a5de7d7397589894aacf28f8c2cea2bbd3f0d1d2529f20`; leaf ownership revoked and requests drained before owner gates. Owner probe `30041` exit0,52.04s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL26 actual retained standardaxiom checks. `/private/tmp/roth-separation-d23-compatibility.{lean,log,json}`. Owner build session `55314` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,124.36s/30.76s; source hash stable. `/private/tmp/roth-separation-d23-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.
