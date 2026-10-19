# Phase 4 worker — `Roth.B₁`

Scope: single original declaration, Roth/MainLemma.lean:58 (one line).
Parent owns other source, shared progress, Git and checkpoint work. This worker
owns this report and `/private/tmp/roth-mainlemma-b1/`. Source edits are unnecessary;
only the warranted future rename is appended to the shared rename queue.

## Step 1: reads, context and immutable original

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md in full. Installed mathlib-quality
and lean4 skills, exact complete Phase-4 worker prompt from cleanup.md, applicable
formatting/docstring/visibility/definition/transparency/cast/generality/API sections
of style-rules.md and naming-conventions.md were read. Initially truncated combined
outputs were reread in bounded chunks. Skills applied: mathlib-quality and lean4.
The target file was read in full across bounded source reads. No source edit occurred.

Immutable `original.lean` comes from the parent's project-original snapshot at
d2eb5e9a1806e12e66db25d15d8954ade4be9874. Entry `pre-worker.lean` is independently
copied before mutations. B₁'s original/entry/current formula agrees exactly;
source-hashes.json records complete file hashes. Parent supplied green project
build and evaluation baseline. Fresh native full-file diagnostics passed complete
flags: success=true, partial=false, timed_out=false, failed_dependencies=[], zero errors.

Complete file warning list: header at 1:2 (`Copyright too short!`), unused `hδ0`
at 150:28, unused `hr₁` at 150:69. None is on B₁. These other owners' warnings
are retained without suppression and reproduced in final native evidence.

## Step 2: full 24-item audit

1. **LINT:** none on line 58. Complete file warnings are listed above.
2. **HAVE SCAN:** n/a: no have, proof block, binding or projection exists.
3. **SET_OPTION:** n/a: no option, debug trace or resource-limit override exists.
4. **SIMP SQUEEZE:** n/a: the direct data term has no simp/simp only/simp_all.
5. **NAMING:** actionable. B₁ returns Nat data, but its uppercase single mathematical
   letter with subscript does not provide a discoverable lowerCamelCase name.
   Queue `Roth.B₁ → Roth.mainCoeffBound`, describing the coefficient bound in
   Roth's main lemma. The proposed exact identifier is absent in project and
   mathlib source; existing `coeff` API vocabulary makes its meaning clear.
   No in-place or caller rename is made. Retain the paper notation in the docstring.
6. **LINE PACKING:** one signature line; complete measured table below. All explicit
   arguments, result and body fit within 70 codepoints. No underpacked break exists.
7. **BY PLACEMENT:** n/a: term-mode data construction already has no by.
8. **FORMAT:** flush-left declaration, conventional colon/operator spacing, no
   internal blank/trailing whitespace, tactic chains, haveI or letI.
9. **COMMENTS:** no inline proof comments exist; existing public source docstring
   is preserved verbatim with its source equation reference.
10. **DOCSTRING:** one sentence explains B₁'s coefficient-bound role and §6 (37),
    beyond the uninformative raw real-to-natural-to-natural function type. Retain.
11. **VISIBILITY:** retain public. Main.lean:571 calls B₁; MainLemma's log bound,
    three_small_factors and main_lemma use it repeatedly. Classic-import dialect;
    no module/public-section exception is involved.
12. **STRUCTURE:** one direct term line, no conjunction, proof branch or extraction
    candidate. Under all length thresholds; no decomposition flag is needed.
13. **MATHLIB:** five actual search methods below found no equivalent named
    coefficient-bound construction. No noncomputable DecidableEq, coset wrapper
    or ugly-proof API-extraction signal exists.
14. **JUNK DEF:** keep. Names a paper parameter with repeated theorem uses and an
    external caller, including coefficient/log/derivative bound API. It is not a
    one-use alias and no matching mathlib concept was found.
15. **EXISTS LEMMA:** n/a: this is a data definition, not an existential lemma.
16. **SHOW vs CHANGE:** n/a: no show or tactic goal adjustment exists.
17. **PUSH_NEG:** n/a: no negation tactic exists.
18. **GENERALISE:** all three effective explicit binders audited and drop-tested
    below. No section variables, proposition binders, instances or universes hide.
19. **INEQUALITY:** zero inequality occurrences, full scan table below; no reversed
    comparison-name fragment in B₁ or the proposed replacement.
20. **NORMAL-FORM:** paper formula in the canonical Nat.floor of a real rpow form.
    Replacing natural floor by integer floor plus toNat adds a wrapper; replacing
    rpow by exp/log introduces domain reasoning without caller benefit.
21. **SYNTAX-GEN:** OK: explicit δ q₁ r₁ applies directly at every caller; bundling
    denominators/degrees or an arbitrary power operation makes application harder.
22. **IMPORT-FANOUT:** n/a: no new import or dependency is needed.
23. **CASTS:** source diff empty: 0 dropped / 0 kept cross-type / 0 kept load-bearing
    in diff. Existing `(q₁ : ℝ)` is a genuine Nat→Real conversion fixing the rpow
    base; the implicit r₁ conversion is inferred from δ multiplication. Retain.
24. **INSTANCE-NAME:** n/a: ordinary data definition, not an instance.

Issues to fix: 1, descriptive data naming. Resolution: append the rename entry.
Refactoring needed: **Phase 5b rename `Roth.B₁ → Roth.mainCoeffBound`**, including
all cross-file uses and module documentation. Keep formula, parameters, public
visibility, semireducibility, noncomputability and source docstring intact.

## Step 2.5: five-method mathlib search-status

| Method | Actual query | Outcome |
|---|---|---|
| A Lean-Finder | Roth Diophantine approximation coefficient bound natural floor q to delta times r | rothNumberNat_le, Behrend.roth_lower_bound and Behrend.bound_aux concern arithmetic progressions, not this construction. |
| B Loogle | `Nat.floor, Real.rpow` | Empty items. |
| C LeanSearch | Roth theorem auxiliary polynomial coefficient bound floor q power delta r | Polynomial.coeff_le_of_roots_le and coeff_bdd_of_roots_le bound coefficients from roots; Behrend.bound_aux is combinatorial Roth; none defines this parameter. |
| D source grep | Roth.B₁, def B₁, mainCoeffBound, coeffBound, B₁_apply, B₁_def, B₁_eq, B₁_of_, B₁_left, B₁_right, floor/rpow formula | One unrelated local matroid variable B₁; no named replacement. Untruncated output retained. |
| E local names | coeffBound | Unrelated boundary/boundedness declarations and Height.mulHeight_constantCoeff_le_mulHeightBound. Index warming, so not an absence certificate. |

Complete A–C responses are in search-remote.json, E in search-local.json,
D in search-source.txt. Auxiliary variants actually searched: B₁_apply, B₁_def,
B₁_eq, B₁_of_, B₁_left, B₁_right. Common-equivalents lookup: no discrete,
finite, separation or bounded-space bucket matches the fixed numerical parameter.
Conclusion: no matching replacement found by all five methods; keep the
domain-specific construction. No declaration is newly written based on an absence
claim. Generic exact?/apply? at type ℝ → ℕ → ℕ → ℕ could return arbitrary data
and cannot establish this specified formula. The independent kernel value equality
below is the relevant compile check; no missing mathematical API is concealed.

## Step 2.6: full generalisation status

Effective type: `(δ : ℝ) (q₁ r₁ : ℕ) : ℕ`, exactly that order, all explicit
BinderInfo.default, no universe parameters. Exact type AST, names/order/BinderInfo,
body types, value defeq and independent original-formula rfl are compiled below.

| # | Binder | Class | Used as | Mechanical candidates tried | Verified? | Result |
|---|---|---|---|---|---|---|
| 1 | δ : ℝ | structure value | real multiplier in rpow exponent | drop; concrete-to-abstract considered | yes: native batch | Drop rejected: unknown δ at 3:61. No class parent, global/point-local, strict/weak or universe candidate exists for a scalar value. |
| 2 | q₁ : ℕ | structure value | denominator, coerced real base | drop; widening to real considered | yes: native batch | Drop rejected: unknown q₁ at 4:55. Natural denominator domain is intentional; a real base would alter public API and arithmetic meaning. No class/proposition/universe weakening applies. |
| 3 | r₁ : ℕ | structure value | degree, coerced real exponent multiplier | drop; widening to real considered | yes: native batch | Drop rejected: unknown r₁ at 5:71. Natural polynomial-degree domain is intentional; no induction-only structure weakening, class/proposition or universe candidate applies. |

Negative tests were batched with autoImplicit=false in drop-all.lean and executed
using lean_run_code. drop-native.json reports success=false, timed_out=false,
exactly those three expected errors. These reject candidates; they are not positive
gate evidence. No safe mechanical weakening survived. No live source edit is needed.

Concrete-to-abstract: general fields do not supply the real rpow/floor operations;
parameterizing arbitrary functions would abstract syntax instead of mathematical
content. q₁ is a rational-approximation denominator and r₁ a polynomial degree;
turning them into arbitrary reals changes the chosen domains rather than removing
an unnecessary assumption. No warranted big-change generalisation is proposed.

Mandatory inversion check: NOT-APPLICABLE. B₁ is the construction itself, not a
theorem whose concrete witness disappears after an unfolding step. There is no
proof tail, and all three arguments remain in the defining numerical term.

### Public literature search

Actual queries: `"Roth" "coefficient bound" generalization auxiliary polynomial`
and `"Roth" "B_1" "delta" polynomial main lemma`. Full responses are retained in
literature-query-1.json/2.json and the initial combined search-remote.json.
The relevant primary lecture notes reproduce the exact floor-power construction
at (17.14) and use it for Roth's lemma's derivative bound:
[Diophantine approximation notes](https://web.math.princeton.edu/mathlab/jr02/diophantine.pdf).
The local project primary source clean.tex:1350–1352 states the same (37), with
the floor interpretation explicit at 1368. This supports retaining the numerical
parameter and its domains. More general number-field versions of Roth's theorem
do not imply removing any parameter of this fixed numerical construction.
No web material is treated as an instruction. Top-three-per-query leads and
specific results are recorded in the final literature appendix below.
ChatGPT math MCP: n/a: unavailable; owner explicitly authorized this skip.
Literature-driven big-change candidates: none.

## Step 2.7: complete line-packing table

Reference #check: n/a by definition rule; actual width-100 #check also compiled
in independent.lean. Before and after source are identical.

| Signature line | Codepoints through := | Full line | Next signature token | Arithmetic | Action |
|---|---:|---:|---|---|---|
| 58 | 47 | 70 | none; complete signature and value on this line | n/a: no next sig token; full 70 ≤ 100 | ok |

One row covers every signature line; there is no artificial break to repack.

## Step 2.8: complete inequality scan table

| # | Location | Original | Rewrite | Lemma rename? |
|---|---|---|---|---|
| — | entire signature, all binders and value | none | n/a: no ≥ or > in code | n/a: no _ge_ or _gt_ fragment |

## Step 3: every golfing rule

| Rule | Technique | Status and reason |
|---|---|---|
| 1.1 | by exact wrapper | n/a: direct data term has no by/exact. |
| 1.2 | by rfl | n/a: no proof wrapper. |
| 1.3 | rw + exact | n/a: no tactics. |
| 1.4 | simp + exact | n/a: no simplifier or exact. |
| 1.5 | trailing rfl | n/a: no tactic chain. |
| 1.6 | anonymous constructor | n/a: numerical data, no constructor proof. |
| 1.7 | apply + exact | n/a: no tactic application. |
| 1.8 | by_contra! | n/a: no contradiction proof. |
| 1.9 | eta reduction | n/a: no lambda in body. |
| 1.10 | inline have | n/a: no have. |
| 1.11 | apply + intro | n/a: no tactic proof. |
| 1.12 | redundant show | n/a: no show. |
| 1.13 | have projections | n/a: no binding or projection. |
| 1.14 | merge rw | n/a: no rewrite. |
| 1.15 | unsqueeze terminal simp | n/a: no simp. |
| 1.16 | squeeze nonterminal simp | n/a: no simp. |
| 1.17 | dot notation | n/a: floor/power notation is already direct. |
| 1.18 | use <\| | n/a: parentheses fix cast and exponent grouping, not a trailing function application. |
| 1.19 | push Not | n/a: no negation tactic. |
| 1.20 | inline exists helper | n/a: not an existential lemma. |
| 2.1 | grind whole proof | n/a: specified data construction, no proposition proof. |
| 2.2 | delete before grind | n/a: no grind/tactic chain. |
| 2.3 | simpa consolidation | n/a: no proof chain. |
| 2.4 | fun_prop | n/a: no function-property goal. |
| 2.5 | positivity | n/a: numerical construction, no sign proposition. |
| 2.6 | gcongr | n/a: no inequality proof. |
| 2.7 | lia/omega | n/a: no Nat/Int proposition. |
| 2.8 | aesop | n/a: specified data, no logical proof. |
| 2.9 | norm_num/norm_cast | n/a: symbolic numerical definition, no computation/cast proof. |
| 2.10 | decide +kernel | n/a: not a decidable proposition. |
| 2.11 | field_simp; ring | n/a: no equality goal or denominator manipulation. |
| 2.12 | linear_combination | n/a: no ring proof or equation hypotheses. |
| 2.13 | wlog | n/a: no case branches. |
| 2.14 | collapse calc | n/a: no calc. |
| 2.15 | multiple goals <;> | n/a: no refinement subgoals. |
| 3.1 | erw to rw | n/a: no erw. |
| 3.2 | continuity to fun_prop | n/a: no legacy property tactic. |
| 3.3 | omega to lia | n/a: no omega. |
| 3.4 | rcases with rfl | n/a: no rcases. |
| 3.5 | register automation | n/a: data definition itself states no property to register. |
| 3.6 | simp_all | n/a: no simplifier proof. |
| 3.7 | remove heartbeat limit | n/a: no limit setting. |

## Step 4: step back and think

The complete definition is already a single term expressing the source formula.
Replacing it by tactic-based data synthesis would obscure the exact chosen value.
There is no have block, redundant proof step or multi-line strategy to compose
or extract. Five-method search found no matching named construction. Existing
theorem API and an external caller justify the public semireducible definition.
Preserve its numerical formula; improve discoverability through the queued rename.

## Literature appendix: top three leads per query

Query 1 returned, in order: [Roth's theorem overview](https://en.wikipedia.org/wiki/Roth%27s_theorem),
[Undergraduate Texts scan](https://ru.djvu.online/file/8rSvFN0De5p7v), and
[combinatorial Roth overview](https://en.wikipedia.org/wiki/Roth%27s_theorem_on_arithmetic_progressions).
These provide either general context or a different Roth theorem, no specific
parameter weakening. They are recorded as search leads, not mathematical evidence.

Query 2 returned, in order: [Roth's original paper](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/EFB89E2873019B246F004FAA06E05A7F/S0025579300000644a.pdf/rational_approximations_to_algebraic_numbers.pdf),
[Diophantine approximation notes](https://web.math.princeton.edu/mathlab/jr02/diophantine.pdf), and
[machine-learning security paper](https://mlsec.tu-berlin.de/docs/2024-warnecke.pdf).
The first two concern the same coefficient/derivative construction; the third
uses Roth as an author name and is irrelevant. The primary notes were opened
directly (193-page PDF, authors Takloo-Bighash/Miller/Helfgott/Spinu, 2003);
literature-primary.json retains that response. The exact floor-power formula is
supported by the search excerpt and local clean.tex (37), independently of broad
search leads. No proposed generalisation follows from these results.

## Independent original-contract and axiom verification

independent.lean independently reimplements the original formula as originalBound,
without mentioning the current target in that definition. Kernel `rfl` proves
`@Roth.B₁ = @originalBound`. A metaprogram compares exact universe lists, effective
type AST, binder names/order/BinderInfo, verifies both bodies have their declared
types and checks data-value defeq. Both have exactly the three expected explicit
binders δ, q₁, r₁ and result Nat; no hidden parameters or universes.
The actual value and original value use only propext, Classical.choice and
Quot.sound; the allowlist check and #print axioms both confirm this.

Actual invocation `/Users/ramin/.elan/bin/lake env lean
/private/tmp/roth-mainlemma-b1/independent.lean` exited 0 in 45.714s,
timed_out=false. Full source/log/metadata: independent.lean/log/json.
No sorry, axiom, native_decide or limit raise is introduced.

## Anchored profiling / buzz

Actual invocation: `/Users/ramin/.elan/bin/lake env lean --profile
-Dtrace.profiler=true -Dtrace.profiler.threshold=0
/private/tmp/roth-mainlemma-b1/profile-prefix.lean`, exit 0 in 31.680s,
timed_out=false. Prefix is exact live source through B₁ (line 58), followed only
by `end Roth`. Prefix SHA256:
`f000788dc971c19a6dbe29b767cef5270de1dfba87cdc8b9d606d997d276c2a1`.
Raw UTF-8 profile-1.log and command metadata profile-1.json are retained fully;
terminal preview truncation does not truncate the file. Target block is raw
lines 3385–4784, copied to profile-target-raw.txt. Every included outermost root
and its original raw line is retained in profile-summary.json.

| Disjoint outermost target component | ms | Accounting |
|---|---:|---|
| B₁ Elab.command | 23.830 | Includes nested header, value and addDecl events. |
| Fourteen following Meta.whnf roots | 0.018 | Roots after the B₁ command only. |
| B₁ addDecl Elab.async root | 0.849 | Includes its 0.815ms kernel child. |
| B₁ asynchronous linter root | 4.720 | Includes all nested lint events. |
| Standalone compiler roots | 0 | None for this noncomputable definition. |
| **Total** | **29.417** | Mutually disjoint outermost roots. |

Equivalent disjoint split: 23.830 command + 0.018 whnf + 0.815 kernel + 0.034
async overhead + 4.720 lint + 0 compiler = 29.417ms. Kernel children are never
added on top of their parent root. All preceding lam/gam/eta commands, their
async roots, imports, namespace/open/module doc and following end/empty commands
are excluded. Below 750ms repeat trigger and 1000ms budget; no repeat required.
No failed profiling samples. Outcome: **FAST-BOARD**. Limit raises removed 0,
added 0; deferrals none; flagged big changes none. No production scaffolding.

## Step 5a: complete live native file/caller diagnostics

Final MainLemma.lean and Main.lean lean_diagnostic_messages calls were unfiltered
and complete. Both returned success=true, partial=false, timed_out=false,
failed_dependencies=[], zero errors. Full native-final.json and
native-caller-final.json retain every warning and field.

MainLemma's complete warnings: header 1:2, hδ0 150:28, hr₁ 150:69.
Main's complete warnings: header 1:2, unused hδ 333:67, hQ 474:82, hc 475:89.
No target warning, filtering or suppression. All calls returned; no native
fallback, failure or timeout was necessary for either live file.

## Step 5b: actual full-file/module validation and diff gates

Actual `/Users/ramin/.elan/bin/lake env lean Roth/MainLemma.lean` exited 0
in 38.556s, timed_out=false. Full file-final.log/json records the existing
unused hδ0/hr₁ warnings. Actual `/Users/ramin/.elan/bin/lake build
Roth.MainLemma Roth.Main` exited 0 in 5.161s, timed_out=false (unchanged modules
replayed successfully). Full affected-build.log/json retains all file and
dependency warnings without filtering. Parent independently owns the next full
project build and separate evaluation; neither is claimed by this worker.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Actual affected-module build exit 0 in 5.161s; full-file compile exit 0 in 38.556s. |
| definition_protected | pass | Source delta empty; original formula identical; kernel rfl/data defeq checked. |
| theorem_statement_protected | pass | No theorem or lemma line changed. |
| structure_gate | pass | One term line; no conjunction or case branch. |
| naming_gate | pass with queued action | Exactly one B₁ → mainCoeffBound JSONL entry appended; prior Index entry preserved; no in-place rename. |
| line_packing_gate | pass | Complete one-row final width table: signature 47/full 70 codepoints, no break. |
| inequality_orientation_gate | pass | Complete occurrence table; no ≥/> or reversed name fragments. |
| exact telescope/body/type/axioms | pass | Independent original formula, exact universes/type AST/binder names/order/BinderInfo/body types; value rfl; standard-axiom allowlist. |
| cumulative_no_unintended_breakage | pass | Main module build and complete unfiltered native Main diagnostics, all flags passing. |
| performance | pass | 29.417ms exact anchored target total, below 1000ms; preceding declarations excluded. |

Overall worker gates: **pass**, with explicit future rename. All current mathematical
and public API contracts are preserved. No imported identifier is introduced into
source, so new-identifier checking is n/a for the empty source delta. All comments,
docstrings, metadata, imports and pins are unchanged. No source mutation used a
whole-file overwrite; none was needed. No Git or shared progress-log write occurred.

## Step 6: result and complete eleven-step checklist

Before 1 line; after 1 line; saved 0 lines. Audit issues found 1 (naming), resolved
by queued action 1; applied source renames 0. Other golf changes warranted 0.
Renames-queued: **Roth.B₁ → Roth.mainCoeffBound**. Refactoring needed: apply that
rename globally in the final Phase 5b pass, including callers and module docs.
Comments-preserved: one existing public docstring verbatim; no inline comments.

- [✓] Step 1 — complete five-reference reads, installed skills, cleanup prompt, applicable style/naming.
- [✓] Step 2 — full 24-item audit with concrete actions/reasons printed.
- [✓] Step 2.5 — all five actual mathlib methods, auxiliary variants and common-equivalents analysis.
- [✓] Step 2.6 — all three effective binders, actual negative drop batch, inversion check, public literature.
- [✓] Step 2.7 — complete measured signature line-packing table.
- [✓] Step 2.8 — complete inequality occurrence table.
- [✓] Step 3 — all 42 golfing rules individually reported.
- [✓] Step 4 — whole-definition reuse/term-mode/strategy reflection.
- [✓] Step 5a — complete unfiltered live file and caller diagnostics passed.
- [✓] Step 5b — actual file/module builds, exact independent original contract, axioms, anchored profiling and gate table passed.
- [✓] Step 6a — exactly one warranted rename appended; existing queue entry preserved; no global rename applied.

## Final manifest, source freeze and ownership release

Evidence root: `/private/tmp/roth-mainlemma-b1/`.

- Original/entry source: original.lean, pre-worker.lean, source-hashes.json;
  empty source delta worker.diff.
- Actual searches: search-remote.json, search-local.json, search-source.txt.
- Literature: literature-query-1.json, literature-query-2.json, literature-primary.json.
- Negative candidates: drop-all.lean, drop-native.json.
- Independent contract: independent.lean/log/json.
- Complete native diagnostics: native-final.json, native-caller-final.json.
- Compiler checks: file-final.log/json, affected-build.log/json.
- Anchored timings: profile-prefix.lean, profile-1.log/json,
  profile-summary.json, profile-target-raw.txt.
- Serialized bounded process runner run.py; final-manifest.json records every
  evidence file size/SHA256, command exit statuses, native flags and report hash.

Frozen live MainLemma.lean SHA256:
`0236435831af553f54e04569caadb7b985e0a556dbebf51d454e53abf3ea2abb`.
Live source is byte-identical to entry; B₁'s declaration is also identical to
project-original. All owned subprocess sessions and native calls returned; no
owned compiler/profile/native work remains. Source, compiler and native ownership
are explicitly released to the parent. This is a worker result, not a claim of
whole-file completion or the parent's build/evaluation/commit/push checkpoint.
