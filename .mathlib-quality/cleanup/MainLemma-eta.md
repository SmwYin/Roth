# Phase 4 worker — `Roth.eta`

Scope: the single original declaration at Roth/MainLemma.lean:55 (one line).
Parent owns all other declarations, shared logs, Git and checkpoint validation.
This worker owns this report and `/private/tmp/roth-mainlemma-eta/` evidence.
The source remains unchanged: the fresh audit found no warranted recommendation.
Preserve prior explicit API/domain decisions; no rename, abstraction or extra API is invented.

## Step 1: complete reads and immutable baseline

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md in full. Also read the installed
mathlib-quality/lean4 skills, complete cleanup command including the exact Phase-4
worker prompt, applicable formatting/docstring/definition/transparency/cast/generality
style sections, naming conventions, and target source context. Initial oversized
combined output was truncated; reference and command sections were re-read in bounded
chunks. No source edit preceded reading. Skills applied: mathlib-quality and lean4.

Project-original immutable snapshot: `original.lean`, copied from parent's
project-original.lean (project commit d2eb5e9a1806e12e66db25d15d8954ade4be9874).
Entry snapshot: `pre-worker.lean`. The eta declaration is identical in original,
entry and live files; assertions and full-source hashes are in source-hashes.json.
The parent supplied green project build/evaluation and native baseline evidence;
this worker independently ran full unfiltered native diagnostics, which returned
success=true, partial=false, timed_out=false, failed_dependencies=[], zero errors.

Complete initial warning list, retained verbatim in native-initial.json:

| Line | Column | Warning |
|---|---:|---|
| 1 | 2 | Copyright too short (header). |
| 150 | 28 | Variable hδ0 is not explicitly referenced. |
| 150 | 69 | Variable hr₁ is not explicitly referenced. |

No warning is on eta. Other declarations' warnings remain with their owners.

## Step 2: full 24-item audit

1. **LINT:** none on line 55; complete file warnings above, no suppression introduced.
2. **HAVE SCAN:** n/a: the direct arithmetic value has no have, hence no single-use
   binding, proof block or projection to inline.
3. **SET_OPTION:** n/a: no per-declaration option or limit setting exists.
4. **SIMP SQUEEZE:** n/a: no simp, simp only, simp_all or tactic call exists.
5. **NAMING:** eta is the three-letter transliteration of the named mathematical
   parameter η. LowerCamelCase data name, no forbidden abbreviation, scheme number,
   numeric auxiliary suffix or single-letter public name; naming gate passes.
6. **LINE PACKING:** all explicit parameters, result and body fit on one line;
   exact per-signature-line measurement appears in Step 2.7.
7. **BY PLACEMENT:** n/a: the data definition already uses term mode without by.
8. **FORMAT:** flush-left declaration, conventional operator/colon spaces,
   no internal blank line, tactic chain, trailing whitespace, haveI or letI.
9. **COMMENTS:** no inline proof comments exist; public source docstring preserved.
10. **DOCSTRING:** its one sentence identifies η and §6 equation (36), supplying
    the mathematical role absent from a raw real-valued function type. Retain verbatim.
11. **VISIBILITY:** retain public: Main.lean uses eta at 268, 273, 285–286, 321,
    567; MainLemma uses it in exists_delta_bound, eta_lt_gam_iff and main_lemma.
    This classic-import file has no module/public-section visibility exception.
12. **STRUCTURE:** one direct term line, no conjunction or case branch; extraction
    and decomposition are inapplicable under every proof-length threshold.
13. **MATHLIB:** five actual search methods and auxiliary variants below found no
    matching parameter construction. No noncomputable decidability instance, coset
    wrapper or ugly-proof missing-API signal exists.
14. **JUNK DEF:** retain: a named paper parameter, module main definition, with
    multiple theorem/caller uses outside a local proof and an external unfolding
    caller. It is not an accidental one-use wrapper of an existing mathlib concept.
15. **EXISTS LEMMA:** n/a: not an existential lemma.
16. **SHOW vs CHANGE:** n/a: no show or goal-changing tactic occurs.
17. **PUSH_NEG:** n/a: no negation tactic occurs.
18. **GENERALISE:** both effective explicit binders audited and drop-tested below;
    no implicit section parameters, propositions, instances or universes are hidden.
19. **INEQUALITY:** zero inequalities in signature or body; full occurrence table below.
20. **NORMAL-FORM:** already the defining paper formula, using natural powers for
    the count m and real rpow for the fractional exponent. Replacing by iterated
    roots introduces domains/cases; it does not improve a simp normal form.
21. **SYNTAX-GEN:** OK: explicit δ m is directly applicable at every existing call.
    Bundling or changing domains provides no demonstrated caller benefit.
22. **IMPORT-FANOUT:** n/a: no import is added or required.
23. **CASTS:** empty source diff: 0 dropped / 0 kept cross-type / 0 kept load-bearing
    in the diff. Original `(1 / 2 : ℝ)` fixes fractional real division and the real
    exponent, preventing a natural-number exponent/division interpretation; retain it.
24. **INSTANCE-NAME:** n/a: this is an ordinary data definition, not an instance.

Issues to fix: none. Refactoring needed: none. No source mutation is warranted.

## Step 2.5: five-method mathlib search-status

| Method | Actual query | Outcome |
|---|---|---|
| A Lean-Finder | Roth Diophantine approximation main lemma eta parameter 10^m delta^((1/2)^m) | Three combinatorial Roth-number results, no matching construction. |
| B Loogle | `Real.rpow, ℝ → ℕ → ℝ` | Empty items, no replacement. |
| C LeanSearch | Roth theorem main lemma parameter eta ten power m times delta to one half power m | Three Behrend combinatorial Roth-number bounds, no matching construction. |
| D source grep | `Roth\.eta`, `def eta`, eta_apply, eta_def, eta_eq, eta_of_, eta_left, eta_right, formula prefix | Eight unrelated eta definitions; full untruncated output retained. |
| E local name | eta | Roth.eta plus unrelated eta constructors, projections and Dedekind eta; index warming, not an absence certificate. |

A/B/C full responses: search-remote.json; E: search-local.json; D: search-source.txt.
Auxiliary variants actually searched: eta_apply, eta_def, eta_eq, eta_of_, eta_left,
eta_right. Common-equivalents lookup: no discrete/finite/separation/bounded bucket
matches. No new declaration is written on an absence claim. An arbitrary exact?
on ℝ → ℕ → ℝ cannot identify the specified data formula; the independent compiled
original-value equality is the relevant check. Conclusion: no matching replacement
found by the five methods; keep the domain-specific paper parameter. No public API
extraction is needed for this single direct term.

## Step 2.6: generalisation-status

Effective type: explicit `(δ : ℝ) (m : ℕ) : ℝ`, in that order, both
BinderInfo.default, no universe parameters. Independent exact type-AST, body-type,
full telescope and value checks are in independent.lean and independent.log.

| # | Binder | Class | Used as | Mechanical candidates tried | Verified? | Result |
|---|---|---|---|---|---|---|
| 1 | `(δ : ℝ)` | structure value | base of real rpow | drop; concrete-to-abstract considered | yes: native batch | Drop rejected, unresolved δ at 3:53 with autoImplicit=false. No typeclass parent, point-local property, strict/weak or universe candidate exists for this scalar value. |
| 2 | `(m : ℕ)` | structure value | natural exponent in both 10^m and (1/2)^m | drop; count-to-abstract considered | yes: native batch | Drop rejected, unresolved m at 4:45 and 4:68 with autoImplicit=false. It is a count, with two actual exponent uses; no induction-only abstract-order weakening applies. |

Both negative tests are batched in drop-all.lean; complete native output is
drop-native.json (success=false, timed_out=false, exactly the three expected unknown
identifier errors). These are rejected weakening candidates, not positive gate evidence.
No file edit was required to establish the negative tests. No proposition can be
weakened or unbundled, global property localized, decidability removed, or universe
generalized: there is no such binder. No tested safe weakening survives.

Concrete-to-abstract analysis: replacing ℝ by a general field loses the real rpow
operation; replacing m by a real exponent changes the specified variable-count
domain. A generic power-operation argument would merely parameterize construction
syntax with no demonstrated mathematical/caller gain. It would alter this public
API and prior domain decisions; no warranted big-change recommendation arises.

Mandatory inversion check: not applicable. This is the construction itself, not
a theorem with a concrete witness that disappears after unfolding. Its complete
body computes from δ and m; there is no proof tail that outruns the statement.

### Public literature search

Actual queries: `"Roth" "main lemma" "eta" generalization` and
`"Formalizing Roth" "Takloo" "Yin"`; complete results retained in
literature-web.json and separately in literature-query-1.json/2.json. The search
results are leads only; no untrusted search-result instructions were followed.
Query 1 top three leads: [Tao's transference lecture notes](https://terrytao.wordpress.com/2010/06/05/254b-lecture-notes-7-the-transference-principle-and-linear-equations-in-primes/),
[NSF private-matrix analysis paper](https://par.nsf.gov/servlets/purl/10312886),
[Cambridge arithmetic-Ramsey paper](https://doi.org/10.1017/prm.2024.96).
These concern different η/Roth objects. Query 2 returned only one lead, the
[SpringerNature title catalog](https://www.scribd.com/document/590434754/SpringerNature-Books-Title-List-20200505-082846);
there were no second/third hits and no primary mathematical replacement.
The local primary project source clean.tex:1347–1350
states equation (36), η = 10^m δ^((1/2)^m), matching the Lean construction exactly.
No literature evidence warrants changing this parameter's chosen domain.
ChatGPT math MCP: n/a: unavailable and expressly authorized to skip by owner.
Literature-driven big-change candidates: none.

## Step 2.7: complete line-packing arithmetic table

Reference #check: n/a by definition rule; actual width-100 #check was additionally
compiled and prints `Roth.eta : ℝ → ℕ → ℝ` (independent.log).

| Sig line | Codepoints through `:=` | Full line | Next signature token | Arithmetic | Action |
|---|---:|---:|---|---|---|
| 55 | 44 | 75 | none; all signature tokens and body already on this line | n/a: no next signature line/token to pack; 75 ≤ 100 | ok |

This covers the only signature line. Before/after are identical, so this is also
the final measured table. No underpacked break exists.

## Step 2.8: complete inequality occurrence table

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| — | complete signature and value | none | n/a: no ≥ or > in Lean code | n/a: no _ge_ or _gt_ in name |

## Step 3: all 42 golfing rules

| Rule | Technique | Status and reason |
|---|---|---|
| 1.1 | by exact wrapper | n/a: direct data term has no by/exact. |
| 1.2 | by rfl | n/a: no proof wrapper. |
| 1.3 | rw + exact | n/a: no tactics. |
| 1.4 | simp + exact | n/a: no simplifier or exact. |
| 1.5 | trailing rfl | n/a: no tactic chain. |
| 1.6 | constructor pair | n/a: scalar data, no constructor proof. |
| 1.7 | apply + exact | n/a: no tactic application. |
| 1.8 | by_contra! | n/a: no contradiction proof. |
| 1.9 | eta reduction | n/a: no lambda in body; eta is a parameter name. |
| 1.10 | inline have | n/a: no have binding. |
| 1.11 | apply + intro | n/a: no tactic proof. |
| 1.12 | redundant show | n/a: no show. |
| 1.13 | have projections | n/a: no have or projection. |
| 1.14 | merge rw | n/a: no rewrites. |
| 1.15 | unsqueeze terminal simp | n/a: no simp. |
| 1.16 | squeeze nonterminal simp | n/a: no simp. |
| 1.17 | dot notation | n/a: arithmetic notation already direct; no eligible named application. |
| 1.18 | use <\| | n/a: parentheses group a fractional exponent, not trailing function application. |
| 1.19 | push Not | n/a: no negation tactic. |
| 1.20 | inline exists helper | n/a: no existential lemma. |
| 2.1 | grind whole proof | n/a: constructs specified real data, no proposition proof. |
| 2.2 | delete before grind | n/a: no grind/tactic chain. |
| 2.3 | simpa consolidation | n/a: no proof chain. |
| 2.4 | fun_prop | n/a: no function-property goal. |
| 2.5 | positivity | n/a: scalar construction, no sign proposition. |
| 2.6 | gcongr | n/a: no inequality proof. |
| 2.7 | lia/omega | n/a: no Nat/Int proposition. |
| 2.8 | aesop | n/a: specified data term, no logical proof goal. |
| 2.9 | norm_num/norm_cast | n/a: symbolic value definition, no numeric/cast proof. |
| 2.10 | decide +kernel | n/a: not a decidable proposition. |
| 2.11 | field_simp; ring | n/a: no equality goal; fractional exponent is defining data. |
| 2.12 | linear_combination | n/a: no ring proof or equation hypotheses. |
| 2.13 | wlog | n/a: no case branches. |
| 2.14 | collapse calc | n/a: no calc. |
| 2.15 | close multiple goals | n/a: no refinement subgoals. |
| 3.1 | erw to rw | n/a: no erw. |
| 3.2 | continuity to fun_prop | n/a: no property tactic. |
| 3.3 | omega to lia | n/a: no omega. |
| 3.4 | rcases with rfl | n/a: no rcases. |
| 3.5 | register automation | n/a: definition alone provides no property theorem to register. |
| 3.6 | simp_all | n/a: no simplifier proof. |
| 3.7 | remove heartbeat limit | n/a: no limit setting exists. |

## Step 4: step back and think

The complete declaration already expresses equation (36) in direct term mode.
A by/grind/simp/aesop proof would add tactic-based data construction without
improving the specified formula. There is no have block, redundant proof step or
duplicated proof strategy to compose or extract. Five-method search found no
matching named construction; generic exact?/apply? on a data function would
not establish this formula's meaning. The semireducible named definition supports
the external unfolding callers. Retain its source, name, docstring and public API.

## Step 5a: complete live native validation

Complete unfiltered final native lean_diagnostic_messages on MainLemma.lean:
success=true, partial=false, timed_out=false, failed_dependencies=[], zero errors;
full response native-final.json. Complete warnings: header at 1:2, unused hδ0 at
150:28 and unused hr₁ at 150:69; no warning on eta. Complete unfiltered native
caller Main.lean response native-caller-final.json also has all four required
passing flags and zero errors. Full caller warnings: header at 1:2, unused hδ at
333:67, hQ at 474:82 and hc at 475:89. None is hidden, filtered or suppressed.
All native calls returned completely; no fallback or timeout was necessary.

## Independent original-contract and axiom verification

The immutable original declaration is reimplemented independently as originalEta
with the original complete formula, never by referring to Roth.eta. The compiler
checked kernel `rfl` for equality with the actual target. A metaprogram compares
the exact effective type AST, universe lists, binder names/order/BinderInfo and
the original/actual value's types, then checks definitional equality of the data
values. Telescope output is exactly explicit δ : ℝ, m : ℕ, result ℝ, no universe
parameters. The allowlist check and #print axioms report only propext,
Classical.choice and Quot.sound for both original and actual definitions.

Actual command: `lake env lean /private/tmp/roth-mainlemma-eta/independent.lean`,
exit 0 in 49.716s, timed_out=false; full input/output/metadata independent.lean,
independent.log and independent.json. No self-reference is used in the original
construction. No sorry, new axiom, native_decide or limit raise is introduced.

## Anchored profiling / buzz

Actual invocation: `/Users/ramin/.elan/bin/lake env lean --profile
-Dtrace.profiler=true -Dtrace.profiler.threshold=0
/private/tmp/roth-mainlemma-eta/profile-prefix.lean`, exit 0 in 35.220s,
timed_out=false. Prefix is exact live source through eta (line 55), followed
only by `end Roth`. SHA256:
`8909fb2ff93e542f7385de53071c5c8d371b26f89470f1668ac9bb8a4a2ad5d1`.
Full raw UTF-8 log profile-1.log, command metadata profile-1.json. Exact target
block is raw lines 2250–3382, retained in profile-target-raw.txt; root arithmetic
and each root's raw line are in profile-summary.json.

| Disjoint outermost target component | ms | Accounting |
|---|---:|---|
| eta Elab.command | 9.104 | Includes all nested header, value and addDecl events. |
| Twelve following Meta.whnf roots | 0.019 | Only roots after eta command. |
| Two addDecl Elab.async roots | 0.285 | Includes their nested kernel checks. |
| eta asynchronous linter root | 5.502 | Includes all nested lint work. |
| Standalone compiler roots | 0 | None emitted for this noncomputable definition. |
| **Total** | **14.910** | Mutually disjoint outermost roots. |

Nested kernel children total 0.246ms, already inside addDecl async totals;
async overhead is 0.039ms. Equivalent disjoint split: 9.104 command + 0.019
whnf + 0.246 kernel + 0.039 async overhead + 5.502 lint + 0 compiler = 14.910ms.
The preceding lam/gam command roots, all their asynchronous roots and all 29.5s
of imports are excluded. end Roth/empty-command roots are also excluded.
Below 750ms repeat trigger and 1000ms budget: no repeat needed. No failed samples.
Buzz outcome: FAST-BOARD. Limit raises removed 0 / added 0; deferrals none;
flagged big changes none; no profiling scaffolding enters production source.

## Step 5b: actual module/full-file builds and diff gates

Actual invocation `/Users/ramin/.elan/bin/lake build Roth.MainLemma Roth.Main`
exited 0 in 5.007s (replayed unchanged modules), timed_out=false. Full warning
list, including dependency warnings, is in affected-build.log/json. Actual live
full-file invocation `/Users/ramin/.elan/bin/lake env lean Roth/MainLemma.lean`
exited 0 in 31.801s, timed_out=false; file-final.log/json retains both existing
unused-variable warnings. These are actual compiler checks, not inferred from LSP.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Actual affected build exit 0, 5.007s; actual full-file compile exit 0, 31.801s. |
| definition_protected | pass | Empty source delta; exact original eta text identical; independent kernel data equality. |
| theorem_statement_protected | pass | No theorem/lemma or any other declaration edited. |
| structure_gate | pass | One direct term line, no conjunction or case branch. |
| naming_gate | pass | LowerCamelCase data parameter eta; no forbidden name pattern or abbreviation. |
| line_packing_gate | pass | Complete final one-row table, 44 signature / 75 full codepoints, no artificial break. |
| inequality_orientation_gate | pass | Complete occurrence table: no ≥/> code and no reversed name. |
| exact telescope/body/type/axioms | pass | independent.lean compiled original formula, rfl, exact AST/binders/universes/body types and standard-axiom allowlist. |
| cumulative_no_unintended_breakage | pass | Affected Main build plus complete unfiltered Main native diagnostics, all flags pass. |
| performance | pass | 14.910ms disjoint target total, frozen exact live prefix. |

Overall worker gates: pass. The parent's separate full project build, evaluation,
commit and push checkpoint remains the parent's work. This report does not claim
that checkpoint or whole-file completion. New-identifier verification: n/a, empty
source diff. No source comment, docstring, import, metadata or pin changed.

## Step 6: result and eleven-step checklist

Before 1 line; after 1 line; saved 0. Audit issues found 0; fixed 0; deferred 0.
Rules applied: none; all 42 prerequisites are individually checked above.
Renames queued: none; Step 6a sidecar append n/a. Comments preserved: original
public docstring verbatim; no inline proof comment exists. Refactoring needed: none.
Only this owned report is written inside the repository. No Git/shared-log writes.

- [✓] Step 1 — complete five-reference reads, installed skills and applicable style/naming.
- [✓] Step 2 — all 24 audit items printed with concrete decisions.
- [✓] Step 2.5 — all five actual search methods and auxiliary variants recorded.
- [✓] Step 2.6 — both effective binders/drop tests, inversion check and public literature.
- [✓] Step 2.7 — complete measured signature line-packing arithmetic table printed.
- [✓] Step 2.8 — complete inequality occurrence table printed.
- [✓] Step 3 — all 42 golfing rules individually reported.
- [✓] Step 4 — complete-definition term-mode, reuse and strategy reflection.
- [✓] Step 5a — complete unfiltered live file/caller native diagnostics passed all flags.
- [✓] Step 5b — actual module/full-file builds, independent original contract/axioms,
  anchored profiling and complete diff-gate table passed.
- [✓] Step 6a — no rename warranted, no append required, no in-place rename.

## Artifact manifest, source freeze and ownership release

Evidence root: `/private/tmp/roth-mainlemma-eta/`.

- Immutable source snapshots: original.lean, pre-worker.lean; comparisons and hashes
  in source-hashes.json; empty owned source delta in worker.diff.
- Complete native evidence: native-initial.json, native-final.json,
  native-caller-final.json; negative batch drop-all.lean and drop-native.json.
- Actual searches: search-remote.json, search-local.json, search-source.txt.
- Literature: literature-web.json, literature-query-1.json, literature-query-2.json.
- Independent contract: independent.lean, independent.log/json.
- Actual builds: affected-build.log/json, file-final.log/json.
- Anchored profile: profile-prefix.lean, profile-1.log/json, profile-target-raw.txt,
  profile-summary.json; auxiliary index profile-index.txt.
- Process runner: run.py; complete final sizes/SHA256/command statuses and report
  hash in final-manifest.json.

Frozen live MainLemma.lean SHA256:
`0236435831af553f54e04569caadb7b985e0a556dbebf51d454e53abf3ea2abb`.
Live source is byte-identical to pre-worker.lean; eta is also byte-identical to
project-original.lean. All owned subprocess sessions and native calls have returned;
no owned compiler/profile/native work remains. Source, compiler and native ownership
are explicitly released to the parent.
