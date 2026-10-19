# Phase 4 / Mode A: `Roth.lam`

Target: `Roth/MainLemma.lean:49`, one original declaration only. Entry HEAD supplied by
owner: `4d7445c6dd8fe1dd0abfd6edbd5c73f3bc5ccec6`. Source starts in classic dialect.
Owner's import-group blank line is outside this worker's diff. No source edit is warranted.
All evidence lives under `/private/tmp/roth-mainlemma-lam/`; this report is the only owned
repository write. No Git or shared-log writes were made.

## Step 1: references and scope

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md in full. Also read the installed
mathlib-quality and lean4 skills, the complete Phase 4 Worker Agent Prompt in cleanup.md,
naming-conventions.md, relevant style-rules.md sections (definitions, formatting,
documentation, visibility, normal forms, transparency, casts, generality, API), and
profiling.md. References are rooted at
`/Users/ramin/.local/share/roth-mathlib-quality/skills/mathlib-quality/references/`.
The parent expressly prohibits subagents for this leaf worker; none were spawned.

Original source is preserved read-only as `original.lean` (copied from the owner's
immutable original file); `pre-worker.lean` preserves the prepared file read-only.
The owner also recovered project-original commit
`d2eb5e9a1806e12e66db25d15d8954ade4be9874`; its lam text is identical to entry.
`source-hashes.json` identifies the original, prepared, independent and profiling inputs.

## Step 2: full 24-item audit

1. **LINT:** no warning on line 49. Complete native diagnostics report the existing
   header warning at 1 and unused `hδ0`/`hr₁` warnings at 150, outside the target.
2. **HAVE SCAN:** n/a: the definition has no `have` binding or proof block.
3. **SET_OPTION:** none; no limit or debug option is introduced.
4. **SIMP SQUEEZE:** n/a: there is no simplifier call.
5. **NAMING:** `lam` returns real data and is lowerCamelCase. It is three letters,
   not a single-letter public declaration; it matches none of the forbidden abbreviation
   or numeric scheme patterns. It is explicitly tied to paper λ by the docstring and
   namespace. No rename is queued; no established API retention decision is reversed.
6. **LINE PACKING:** one fully packed line; measured codepoint table below.
7. **BY PLACEMENT:** n/a: the body is a direct arithmetic term, with no `by`.
8. **FORMAT:** flush-left declaration, conventional spaces, no blank internal lines,
   no tactic chains, no `haveI` or `letI`.
9. **COMMENTS:** no inline proof comments exist; existing source docstring preserved.
10. **DOCSTRING:** public one-sentence parameter description plus §6 equation (34)
    source locator is accurate; it identifies the paper role, adding context to the type.
11. **VISIBILITY:** keep public: `Roth/Main.lean:323` directly unfolds `lam`;
    `gam`, `eta_lt_gam_iff`, and `main_lemma` also use it. This is a named paper parameter.
12. **STRUCTURE:** one term line, no conjunction statement, branches, or extractable
    proof; passes the 60-line and headline 15-line bounds without a decompose flag.
13. **MATHLIB:** all five actual searches below; no replacement construction found.
    No noncomputable decidability instance or coset wrapper is present.
14. **JUNK DEF:** retain: names equation (34), is reused beyond a single proof and
    outside this file, and is a stable unfolding boundary. It is not a disposable wrapper.
15. **EXISTS LEMMA:** n/a: real-valued definition, no existential statement.
16. **SHOW vs CHANGE:** n/a: no `show` or tactic-mode goal conversion.
17. **PUSH_NEG:** n/a: no negation tactic or lambda syntax to modernize.
18. **GENERALISE:** each of the three effective explicit binders is audited below.
    No assumptions or instances are hidden by section-variable omission.
19. **INEQUALITY:** no inequality in signature or body; occurrence table below.
20. **NORMAL-FORM:** already a left-associated real multiplication of the paper's
    factors with canonical `Real.sqrt` and natural casts. Changing factor order has no
    mathematical or caller advantage.
21. **SYNTAX-GEN:** OK: explicit `δ n m` is convenient at all current callers;
    neither rebundling nor replacing the formula with a lambda improves application.
22. **IMPORT-FANOUT:** n/a: no import is added.
23. **CASTS:** diff has 0 dropped / 0 kept cross-type / 0 kept load-bearing casts,
    because the diff is empty. In original body, `(m : ℝ)` is a genuine ℕ→ℝ conversion
    fixing sqrt's domain; `n` also has an implicit ℕ→ℝ cast. Both are mathematically needed.
24. **INSTANCE-NAME:** n/a: this is a definition, not a typeclass instance.

Issues to fix: none. Refactoring needed: none. No new API lemma is warranted for
a formula whose consumers intentionally unfold the equation; no ugly-proof signal fires.

## Step 2.5: mathlib search-status

| Method | Actual query / terms | Outcome |
|---|---|---|
| A Lean-Finder | `Roth main lemma parameter lambda 4 (1 + 3 delta) n sqrt m`; refined to Diophantine approximation | Returned corners/regularity bounds and combinatorial Roth-number results, not equation (34). Refined raw result in `search-leanfinder.json`. |
| B Loogle | `Real.sqrt, ℕ → ℕ → ℝ` | 0 items, `search-loogle.json`. |
| C LeanSearch | `Roth Diophantine approximation main lemma parameter lambda four one plus three delta n square root m` | Three Behrend combinatorial Roth bounds; different mathematical object, `search-leansearch.json`. |
| D source grep | `Roth\.lam`, `def lam\b`, `4 \* \(1 \+ 3 \*`, `lambda.*sqrt`, auxiliary variants | Untruncated mathlib source result: 0 matches, `search-source.txt`. |
| E local name pattern | `lam` | Actual project lam plus unrelated lambda/metaprogramming/cyclotomic names; `search-name.json` records all returned items. Index reports warming; source grep independently covers the exact name/formula. |

Auxiliary variants tried in source search: `lam_apply`, `lam_def`, `lam_eq`,
`lam_of_`, `lam_left`, `lam_right`. Common-equivalents lookup: no match; this is
neither discreteness, finiteness, separation, boundedness nor a custom typeclass predicate.
The five searches establish that no replacement was found; they do not prove global
absence. A data constructor `ℝ → ℕ → ℕ → ℝ` is not uniquely characterized by its type,
so a generic `exact?` probe of that type would find arbitrary functions and would not
certify a replacement for this formula. No declaration is being newly written on an
absence claim. The independent original-value kernel probe instead verifies the actual
formula exactly. Conclusion: retain the domain-specific definition; no missing-API signal.

## Step 2.6: generalisation-status

The effective telescope, read from the actual built constant, is exactly three default
(explicit) binders `δ : ℝ`, `n : ℕ`, `m : ℕ`, in that order, result ℝ, no universes.

| # | Binder | Class | Used as | Mechanical candidates | Verification/result |
|---|---|---|---|---|---|
| 1 | `(δ : ℝ)` | structure value | `3 * δ` in the factor `1 + 3 * δ` | drop; concrete→abstract considered separately | Drop is invalid: unresolved δ with autoImplicit false. No typeclass parents, strict hypotheses, global properties, decidability or universe binder apply to a scalar value. |
| 2 | `(n : ℕ)` | structure value | multiplicative factor after coercion | drop; natural→abstract considered separately | Drop is invalid: unresolved n with autoImplicit false. This counts polynomial degree; replacing its type changes public call signature. No hypothesis weakening entry applies. |
| 3 | `(m : ℕ)` | structure value | sqrt of its real cast | drop; natural→abstract considered separately | Drop is invalid: unresolved m with autoImplicit false. This counts variables; same lack of typeclass/proposition/decidability/universe weakening entries. |

Drop-test artifacts and their actual validation status are recorded in final evidence below.
Native diagnostics initially rejected external scratch paths (no lean-toolchain ancestor),
and native lean_run_code initially reported stale imports, so neither attempt is counted
as a successful binder test; both raw failures are retained.
The repeat of native lean_run_code after the successful affected build also reported
stale imports (`drop-run-code-after-build.json`). The bounded compiler fallback
`lake env lean /private/tmp/roth-mainlemma-lam/drop-all.lean` exited 1 in 32.943s,
with exactly the expected unknown-identifier errors for δ, n, m at lines 3, 4, 5.
All three drop candidates were therefore rejected and never applied to live source.
The complete input, raw compiler errors, and process metadata are `drop-all.lean`,
`drop-all.log`, and `drop-all.json`.

Point-localisation, strict→weak, bundled-hypothesis elimination and universe polymorphism:
n/a, because no such binders occur. Inversion check: n/a, this is the explicit construction
itself and has no theorem proof that stops using a named object after an unfolding.

Big-change analysis: extending n/m to real arguments or replacing ℝ by an abstract field
with a square-root operation would change the public formula API and mathematical domain,
and provide no required new user. There is no mechanical-safe change and no warranted
big-change recommendation. Retain the paper's count-valued parameters and real square root.

### Public literature search

WebSearch was run with `"Roth" "lambda" "4" "delta" main lemma generalization`
and `"Formalizing Roth" "main lemma"`; the complete returned evidence is saved in
`literature-web.json`. The first three displayed search leads were the Isabelle
arithmetic-progression formalization (different theorem), a differential-privacy paper
(irrelevant), and an online scan of *An Invitation to Modern Number Theory* (secondary
mirror, not relied on as an authoritative source). Additional targeted author/name and
Diophantine generalization searches produced a Schmidt book listing, a distribution
paper, and the same mirrored textbook as leading results. These do not justify changing
this chosen parameter's API. No mathematical ChatGPT MCP is exposed in ALL_TOOLS;
that method is n/a. The local primary project source `clean.tex:1337–1341` defines
`λ = 4(1+3δ)nm^{1/2}` exactly. No literature-driven weakening is identified.

## Step 2.7: line packing

Reference: definition, so the required #check formatting reference is n/a by procedure;
actual `#check @Roth.lam` is nevertheless captured in `independent.log` at width 100:
`Roth.lam : ℝ → ℕ → ℕ → ℝ`.

| Sig line | Chars through `:=` | Complete line chars | Next sig token | Arithmetic | Action |
|---|---:|---:|---|---|---|
| 49 | 46 | 77 | none: term body is on the same line | n/a: no next signature line to pack | ok |

One row covers the entire signature, and the complete declaration fits under 100
codepoints. Before and after are identical, so this is also the final table.

## Step 2.8: inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| — | complete signature plus body | none | n/a: no ≥ or > | n/a: no `_ge_`/`_gt_` in name |

## Step 3: all 42 golfing rules

| Rule | Technique | Status and concrete reason |
|---|---|---|
| 1.1 | by exact wrapper | n/a: direct real term, no by/exact. |
| 1.2 | by rfl | n/a: no proof. |
| 1.3 | rw + exact | n/a: no rewrite or exact. |
| 1.4 | simp + exact | n/a: no simp/exact. |
| 1.5 | trailing rfl | n/a: no tactics. |
| 1.6 | constructor pair | n/a: real data, no structure constructor proof. |
| 1.7 | apply + exact | n/a: direct term. |
| 1.8 | by_contra! | n/a: no contradiction argument. |
| 1.9 | eta reduction | n/a: no lambda in the body. |
| 1.10 | inline have | n/a: no have. |
| 1.11 | apply + intro | n/a: no tactic block. |
| 1.12 | redundant show | n/a: no show. |
| 1.13 | have projections | n/a: no have or projections. |
| 1.14 | merge rw | n/a: no rw. |
| 1.15 | terminal simp only | n/a: no simp. |
| 1.16 | nonterminal simp squeeze | n/a: no simp. |
| 1.17 | dot notation | n/a: arithmetic notation already expresses each operation. |
| 1.18 | use <\| | n/a: no trailing function-application parentheses; `(m : ℝ)` is a cast. |
| 1.19 | push Not | n/a: no push_neg. |
| 1.20 | single-use exists | n/a: not an existential lemma. |
| 2.1 | grind whole proof | n/a: produces real data, no proposition proof to automate. |
| 2.2 | delete before grind | n/a: no grind or tactics. |
| 2.3 | simpa consolidation | n/a: no proof chain. |
| 2.4 | fun_prop | n/a: no function-property goal. |
| 2.5 | positivity | n/a: defines the scalar rather than proving a sign. |
| 2.6 | gcongr | n/a: no inequality proof. |
| 2.7 | lia/omega | n/a: no natural/integer proposition. |
| 2.8 | aesop | n/a: data formula without proof goal. |
| 2.9 | norm_num/norm_cast | n/a: symbolic scalar construction, no arithmetic goal. |
| 2.10 | decide +kernel | n/a: not a decidable proposition. |
| 2.11 | field_simp; ring | n/a: no equality proof or denominators. |
| 2.12 | linear_combination | n/a: no hypotheses or ring proof. |
| 2.13 | wlog | n/a: no branches. |
| 2.14 | collapse calc | n/a: no calc. |
| 2.15 | close multiple goals | n/a: no refinement or goals. |
| 3.1 | erw→rw | n/a: no erw. |
| 3.2 | continuity→fun_prop | n/a: no such tactic. |
| 3.3 | omega→lia | n/a: no omega. |
| 3.4 | rcases with rfl | n/a: no rcases. |
| 3.5 | automation registration | n/a: no theorem is added; attaching proof attributes to this data definition is unwarranted. |
| 3.6 | simp_all | n/a: no simplifier proof. |
| 3.7 | remove heartbeat limit | n/a: no limit setting exists. |

## Step 4: step back and think

This definition directly states equation (34), already in term mode. It has no redundant
steps or single-use bindings. Adding `by`, `exact?`, `apply?`, or proof automation would
introduce data-construction tactics and cannot improve the formula. Inlining it at all
call sites would erase the named paper parameter used by `gam` and downstream users.
The existing semireducible noncomputable definition is the appropriate API boundary.

## Final validation and gates

### Actual anchored profiling / buzz

Exact invocation: `lake env lean --profile -Dtrace.profiler=true
-Dtrace.profiler.threshold=0 /private/tmp/roth-mainlemma-lam/profile-prefix.lean`.
Exit 0, timeout false, wall 35.474s. The prefix is byte-for-byte source from its start
through line 49 (`lam`), followed only by a namespace close; prefix SHA256
`7a679e5f867f294c9c3ff91f962d7e9bc1e0fc9059653e507249669a74e05fb8`.
The raw UTF-8 trace is retained unfiltered in `profile-1.log`; command/process/source
metadata in `profile-1.json`, extracted exact anchored block in `profile-target-raw.txt`,
and root-by-root arithmetic in `profile-summary.json`. No failed profiling samples occurred.

| Disjoint target component | ms | Accounting |
|---|---:|---|
| Outermost `Elab.command` for lam | 62.568 | Includes its nested elaboration/header/value events; descendants not added. |
| Outermost post-command `Meta.whnf` roots | 0.019 | All ten roots between the target command and its async tasks. |
| Three `Elab.async` addDecl roots | 1.168 | Includes all generated proof declarations and actual lam kernel tasks. |
| Outermost target async lint task | 24.193 | Includes nested lint events, not added again. |
| Standalone compiler roots | 0 | No compiler event emitted for this noncomputable def. |
| **Disjoint outermost total** | **87.948** | Sum of these mutually disjoint roots. |

Kernel children sum to 1.138ms, contained within the 1.168ms async addDecl total;
the remaining 0.030ms is async overhead. An equivalent fully disjoint split is therefore
62.568 command + 0.019 whnf + 1.138 kernel + 0.030 async overhead + 24.193 lint +
0 compiler = 87.948ms. Nested sums and cumulative file counters are not double-counted.
The 28.8s import time is explicitly excluded from the target budget. The target is below
750ms and 1000ms; the repeat threshold is not reached. No performance patch or deferral
is needed; production source contains no profiling scaffolding or raised limits.

### Compiled independent original contract

`independent.lean` imports the actual `Roth.MainLemma` and separately implements the
immutable original right-hand side as `LamAudit.originalLam`, without using `Roth.lam`
in that construction. `example : @Roth.lam = @originalLam := rfl` passes kernel checking.
Direct `Lean.getConstInfo` checks require identical universe names/list, full type AST,
effective binder names/order/BinderInfo, and definitionally equal values. Printed actual
effective binders are δ : ℝ default, n : ℕ default, m : ℕ default; result ℝ.
Both independently collected axiom lists are exactly
`[propext, Classical.choice, Quot.sound]`; no sorryAx or nonstandard axiom is accepted.
The initial compiled probe exited 0 in 41.857s (`independent.log/json`).

The affected build `lake build Roth.MainLemma Roth.Main` exited 0 in 64.533s,
actually rebuilding MainLemma (32s) and Main (29s), including the real downstream
unfolding caller. Its complete warning output is retained in `affected-build.log`.
No source, toolchain pin, definition, theorem statement, visibility or documentation
was changed by this worker.

Scheduling note: one pure remote Lean-Finder search request was made while the affected
build process was active. It does not elaborate a Lean file; all compiler, native proof
evaluation, diagnostics and profiling gates are serialized. The parent was informed.

The post-build independent probe was repeated against the freshly built actual module:
`independent-final.log/json`, exit 0, 43.156s, identical PASS and axiom output.
The complete actual source was separately compiled by
`lake env lean Roth/MainLemma.lean`, exit 0, 33.698s (`file-final.log/json`).
This file gate reports only the pre-existing unused hδ0/hr₁ warnings.

Final unfiltered native `lean_diagnostic_messages` on `Roth/MainLemma.lean` returned
`success=true`, `partial=false`, `timed_out=false`, `failed_dependencies=[]`, and no
errors (`native-final.json`). Its entire warning set remains exactly the baseline
header warning and unused hδ0/hr₁ at line 150. No warning is attached to lam.

### Diff gates

| Gate | Result | Actual evidence |
|---|---|---|
| lake_build_file | pass | Actual `lake build Roth.MainLemma Roth.Main`, exit 0. |
| definition_protected | pass | Byte-identical original lam signature/value and no source diff against worker entry; independent kernel equality. |
| theorem_statement_protected | pass | No theorem or other original declaration edited. |
| structure_gate | pass | One term line, no conjunction or branch. |
| naming_gate | pass | `lam` lowerCamelCase, length 3, no forbidden pattern or abbreviation; no rename needed. |
| line_packing_gate | pass | Complete one-row measured table: 46 signature / 77 full codepoints, no remaining break. |
| inequality_orientation_gate | pass | Complete occurrence table: zero reversed inequalities or names. |
| actual_telescope_and_axioms | pass | Actual built constant compared by exact type AST/BinderInfo/name/order/universes and defeq value; only standard axioms. |
| performance | pass | 87.948ms disjoint outermost budget total; no repeat threshold reached. |
| cumulative caller compatibility | pass | Actual `Roth.Main` build and complete unfiltered native caller diagnostics both pass. |

### Result

Before: 1 line. After: 1 line. Saved: 0 lines.
Audit issues found: 0. Fixed: 0. Refactoring deferred: 0.
Rules applied: none, because every transformation's syntactic/proof prerequisite is absent.
Renames queued: none; Step 6a sidecar append is n/a, no rename was required.
Comments preserved: original one-line public docstring retained, no inline proof comments.
Refactoring needed: none. Source edits: none. Overall worker diff gates: pass.

### Eleven-step checklist

- [✓] Step 1 — all five full references plus applicable style/naming/skills read.
- [✓] Step 2 — all 24 audit items have concrete outcomes.
- [✓] Step 2.5 — all five search methods actually called; outcomes and limits recorded.
- [✓] Step 2.6 — every effective binder examined; drop tests rejected by actual compiler;
  public literature search and inversion check recorded; native failures retained.
- [✓] Step 2.7 — every signature line measured in codepoints; final packing table printed.
- [✓] Step 2.8 — complete inequality occurrence scan table printed.
- [✓] Step 3 — all 42 golfing rules have individual reasoned status lines.
- [✓] Step 4 — whole-definition strategy and term mode reconsidered.
- [✓] Step 5a — complete unfiltered live-file native diagnostics pass with all required flags.
- [✓] Step 5b — actual file/affected builds and all diff gates recorded; kernel/value/
  effective telescope/axioms verification and anchored profile pass.
- [✓] Step 6a — rename sidecar action n/a, no rename warranted or source renamed.

The parent retains responsibility for its separate full-build/evaluation/commit/push
checkpoint. This report certifies only the single-declaration worker's evidence.

Final caller diagnostics (`native-caller-final.json`) also return success=true,
partial=false, timed_out=false, failed_dependencies=[] with no errors. Full warnings
are the existing header warning and unused hδ at 333, hQ at 474, hc at 475.

## Freeze and ownership release

Final live-source SHA256:
`0236435831af553f54e04569caadb7b985e0a556dbebf51d454e53abf3ea2abb`.
`cmp` against `pre-worker.lean` succeeds byte-for-byte. Final artifact manifest,
including raw-log hashes and all frozen Lean inputs, is `final-manifest.json`.
All owned subprocess sessions (independent, affected build, drop tests, prefix profile,
file gate, final independent verifier) have exited; all native calls have returned.
No background compiler/native/profile work remains. The worker explicitly releases
source, compiler and native ownership to the parent. No file/checkpoint completion or
commit/push claim is made here.
