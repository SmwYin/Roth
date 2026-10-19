# Phase 4 / Mode A: `Roth.gam`

Single original target: `Roth/MainLemma.lean:52`, one term line. Worker entry HEAD supplied
by owner: `7699f1850b7d25a949e5e65d13e84914299bf128`. Classic dialect. Source ownership
is restricted to this declaration; the worker makes no Git/shared-log writes or subagents.
No source change is warranted. Evidence directory: `/private/tmp/roth-mainlemma-gam/`.

## Step 1: references and immutable original

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md in full. Also read the complete cleanup.md,
installed mathlib-quality and lean4 skills, naming-conventions.md, relevant style-rules.md
sections on definitions, spacing/packing, documentation/comments, visibility, normal forms,
generality, API transparency/completeness and casts, and profiling.md. References root:
`/Users/ramin/.local/share/roth-mathlib-quality/skills/mathlib-quality/references/`.
`original.lean` preserves the owner's project-original snapshot at
`d2eb5e9a1806e12e66db25d15d8954ade4be9874`; `pre-worker.lean` preserves worker entry.
Both snapshots were made read-only before validation; gam text is identical in them.

## Step 2: full 24-item audit

1. **LINT:** none on gam. Complete native diagnostics retain the header warning at 1
   and unused `hδ0`/`hr₁` warnings at 150; these are outside this worker's target.
2. **HAVE SCAN:** n/a: no `have` or proof block exists.
3. **SET_OPTION:** none; no limit or debug option is added.
4. **SIMP SQUEEZE:** n/a: no simp call exists.
5. **NAMING:** `gam` is lowerCamelCase returning real data. It has three letters,
   matches none of the numeric schemes or forbidden abbreviations, and is identified as
   paper γ in its namespace and source-linked docstring. No rename is warranted or queued.
6. **LINE PACKING:** measured complete one-row table below, including conclusion and `:=`.
7. **BY PLACEMENT:** n/a: the definition already uses direct term mode.
8. **FORMAT:** conventional spaces, flush left, no internal blank line, tactic chains,
   `haveI` or `letI`; the whole declaration fits under 100 codepoints.
9. **COMMENTS:** no inline proof comment exists; preserve the public source docstring.
10. **DOCSTRING:** accurate one-sentence parameter description identifies §6 equation (35),
    providing context absent from its raw real-valued type. Retained verbatim.
11. **VISIBILITY:** public API: Main.lean directly unfolds gam at 323 and uses it at
    286/567; MainLemma uses it in eta_lt_gam_iff and main_lemma. Retain public.
12. **STRUCTURE:** one term line, no conjunction or branch; no extraction/decomposition needed.
13. **MATHLIB:** all five actual search methods below; no replacement found. No decidability
    instance, coset wrapper or missing-API ugly-proof signal occurs.
14. **JUNK DEF:** retain: named equation (35), multiple theorem/API uses and external callers;
    not a single-proof helper or accidental wrapper of a mathlib concept.
15. **EXISTS LEMMA:** n/a: not an existential lemma.
16. **SHOW vs CHANGE:** n/a: no show or tactic-mode goal change.
17. **PUSH_NEG:** n/a: no negation tactic.
18. **GENERALISE:** all three effective explicit binders audited below; no hidden section
    parameters, hypotheses or instances. Preserve established API/domain decisions.
19. **INEQUALITY:** no inequality in the complete signature/body; occurrence table below.
20. **NORMAL-FORM:** real subtraction followed by division by 2 is the paper's canonical
    parameter formula. Expanding lam or distributing division would obscure its role and
    provide no improved simp normal form.
21. **SYNTAX-GEN:** OK: explicit δ n m supports existing calls; bundling or lambda restatement
    offers no caller benefit.
22. **IMPORT-FANOUT:** n/a: no new import is required.
23. **CASTS:** empty diff: 0 dropped / 0 kept cross-type / 0 kept load-bearing in diff.
    Original `(m : ℝ)` is a genuine ℕ→ℝ conversion ensuring real subtraction, not Nat
    truncated subtraction. The lam result/real output also fixes that expected type;
    spelling the conversion explicitly clarifies the mathematical domain without churn.
24. **INSTANCE-NAME:** n/a: ordinary definition, not an instance.

Issues to fix: none. Refactoring needed: none. No invented API or domain change.

## Step 2.5: five-method mathlib search-status

| Method | Actual query | Actual outcome |
|---|---|---|
| A Lean-Finder | `Roth Diophantine approximation main lemma gamma parameter (m - lambda) / 2` | Three combinatorial Roth-number results, no relevant definition. |
| B Loogle | `Real.sqrt, ℝ → ℕ → ℕ → ℝ` | Empty items. |
| C LeanSearch | `Roth Diophantine approximation main lemma gamma equals m minus lambda divided by two` | Two Behrend Roth-number bounds and a rational denominator bound, no replacement. |
| D source grep | `Roth\.gam`, `def gam`, auxiliary name variants, `(m - lambda) / 2` | Untruncated search over mathlib source, zero matches, exit 1. |
| E local name | `gam` | Roth.gam plus unrelated gamma-function, congruence-subgroup, ordinal and game names; index warming, not an absence certificate. |

Full A/B/C/E responses are retained in `search-all.json`; D in `search-source.txt`.
Auxiliary variants actually searched: gam_apply, gam_def, gam_eq, gam_of_, gam_left,
gam_right. Common-equivalents lookup: no discrete/finite/separation/boundedness/typeclass
bucket matches. No new theorem is written on an absence claim. A generic `exact?` on
`ℝ → ℕ → ℕ → ℝ` could synthesize arbitrary data functions and cannot characterize this
formula; the compiled independent exact-value probe provides the relevant check.
Conclusion: no replacement found by all five methods; retain the domain-specific parameter.
No API-extraction signal appears in a direct arithmetic term.

## Step 2.6: generalisation-status

Effective telescope: δ : ℝ, n : ℕ, m : ℕ, all BinderInfo.default (explicit), in this
order, result ℝ, no universe parameters. No instances or proposition binders.

| # | Binder | Class | Used as | Mechanical candidates | Verification / result |
|---|---|---|---|---|---|
| 1 | `(δ : ℝ)` | structure value | passed to lam, affecting its real factor | drop; concrete→abstract considered | Drop rejects unresolved δ with autoImplicit=false. No typeclass-parent, strict→weak, point-local or universe weakening applies to a scalar value. |
| 2 | `(n : ℕ)` | structure value | degree count passed to lam | drop; count→abstract considered | Drop rejects unresolved n with autoImplicit=false. Changing the type changes the public count-valued API, rather than weakening an assumption. |
| 3 | `(m : ℕ)` | structure value | real cast in subtraction and argument to lam | drop; count→abstract considered | Drop rejects unresolved m with autoImplicit=false. Changing type changes both count semantics and lam's public call signature. |

No proposition can be weakened/unbundled, global function property point-localised,
decidability instance removed, or universe binder widened: none exists. The three
independent negative tests are batched in `drop-all.lean`, with autoImplicit false.
Expected negative compilation is evidence for rejected candidates, not a positive gate.
Native scratch limitations and actual fallback results are recorded with validation below.

Inversion check: n/a: this is the construction itself, with lam used in its only value
term. There is no theorem proof which unfolds a concrete witness and then stops using it.
Replacing lam by an arbitrary real parameter would define a different abstraction and
erase δ/n/m's specified meaning; it is not a hypothesis weakening of gam.

Big-change analysis: widening ℕ to ℝ or abstracting ℝ needs a replacement for lam and
its real sqrt, changes the mathematical domain/public call interface, and offers no
required caller. No warranted big-change recommendation; none deferred.

### Public literature search

Actual WebSearch queries: `"Roth" "gamma" "lambda" "main lemma" generalization` and
`"Formalizing Roth" "Takloo" Yin gamma`. Full results: `literature-web.json`.
Per-query evidence was also captured separately in literature-query-1.json and
literature-query-2.json. Query 1 top three: a
[textbook mirror](https://dokumen.pub/an-invitation-to-modern-number-theory-9780691215976.html),
an unrelated [contextual-bandits paper](https://link.springer.com/article/10.1007/s44230-022-00008-w),
and [polynomial Szemerédi proceedings](https://epubs.siam.org/doi/10.1137/25M1806259).
Query 2 returned only two leads: a Scribd SpringerNature books-title catalog and a
manuals.plus product document containing unrelated bibliography. There was no third hit.
The mirror/catalogs are not relied on as primary authority; other hits concern different objects.
The project primary source `clean.tex:1342–1345` defines γ = ½(m−λ), exactly this parameter.
No evidence warrants altering its chosen domain. ChatGPT math MCP: n/a, unavailable
and expressly authorized to skip by owner. Literature-driven big-change candidates: none.

## Step 2.7: complete line-packing table

Reference #check: n/a by definition rule; actual width-100 #check is nevertheless in
the independent log: `Roth.gam : ℝ → ℕ → ℕ → ℝ`.

| Sig line | Codepoints through `:=` | Full line | Next signature token | Arithmetic | Action |
|---|---:|---:|---|---|---|
| 52 | 46 | 72 | none, body is on same line | n/a: no next signature line/token to pack | ok |

The only signature line contains all binders, conclusion and `:=`; no artificial break
exists. Before/after identical, so the table is final as well.

## Step 2.8: complete inequality occurrence scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| — | signature and complete value term | none | n/a: zero ≥/> in code | n/a: no _ge_/_gt_ in name |

## Step 3: all 42 golfing rules

| Rule | Technique | Status and reason |
|---|---|---|
| 1.1 | by exact wrapper | n/a: direct arithmetic term has no by/exact. |
| 1.2 | by rfl | n/a: no proof wrapper. |
| 1.3 | rw + exact | n/a: no tactics. |
| 1.4 | simp + exact | n/a: no simplifier or exact. |
| 1.5 | trailing rfl | n/a: no tactic chain. |
| 1.6 | constructor pair | n/a: real-valued formula, no constructor proof. |
| 1.7 | apply + exact | n/a: no tactic application. |
| 1.8 | by_contra! | n/a: no contradiction proof. |
| 1.9 | eta reduction | n/a: no lambda in body. |
| 1.10 | inline have | n/a: no have. |
| 1.11 | apply + intro | n/a: no tactic proof. |
| 1.12 | redundant show | n/a: no show. |
| 1.13 | have projections | n/a: no have or projection. |
| 1.14 | merge rw | n/a: no rewrites. |
| 1.15 | unsqueeze terminal simp | n/a: no simp. |
| 1.16 | squeeze nonterminal simp | n/a: no simp. |
| 1.17 | dot notation | n/a: lam applied to its explicit parameters, arithmetic notation already direct. |
| 1.18 | use <\| | n/a: parentheses group subtraction before division, not trailing application. |
| 1.19 | push Not | n/a: no push_neg. |
| 1.20 | inline exists helper | n/a: no existential lemma. |
| 2.1 | grind whole proof | n/a: constructing real data, not proving a proposition. |
| 2.2 | delete before grind | n/a: no grind or tactics. |
| 2.3 | simpa consolidation | n/a: no proof chain. |
| 2.4 | fun_prop | n/a: no function-property proof. |
| 2.5 | positivity | n/a: scalar definition rather than sign goal. |
| 2.6 | gcongr | n/a: no inequality goal. |
| 2.7 | lia/omega | n/a: no Nat/Int proposition. |
| 2.8 | aesop | n/a: data construction without proof goal. |
| 2.9 | norm_num/norm_cast | n/a: symbolic scalar construction, no numeric/cast proof. |
| 2.10 | decide +kernel | n/a: not a decidable proposition. |
| 2.11 | field_simp; ring | n/a: no equality proof; denominator 2 belongs to defining value. |
| 2.12 | linear_combination | n/a: no ring proof or hypotheses. |
| 2.13 | wlog | n/a: no case branches. |
| 2.14 | collapse calc | n/a: no calc. |
| 2.15 | close multiple goals | n/a: no refinement goals. |
| 3.1 | erw→rw | n/a: no erw. |
| 3.2 | continuity→fun_prop | n/a: no property tactic. |
| 3.3 | omega→lia | n/a: no omega. |
| 3.4 | rcases with rfl | n/a: no rcases. |
| 3.5 | register automation | n/a: no theorem or property to register. |
| 3.6 | simp_all | n/a: no simplifier proof. |
| 3.7 | remove heartbeat limit | n/a: no limit setting exists. |

## Step 4: step back and think

Equation (35) is already directly expressed in term mode with no redundant step.
Introducing by/grind/exact?/apply? would add tactic-based data construction; algebraic
rearrangement would obscure the paper formula. It has no have block to compose or
duplicated proof to extract. The semireducible named definition is appropriate for its
external unfolding callers. No edit is made.

## Validation and final gates

### Anchored profiling / buzz

Actual invocation: `/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true
-Dtrace.profiler.threshold=0 /private/tmp/roth-mainlemma-gam/profile-prefix.lean`.
Exit 0, timed_out=false, 29.013s wall. Prefix consists of the exact live source through
gam at line 52, followed only by `end Roth`. Prefix SHA256:
`1bd9bd5c78cd790132adfa9cd7be75b539535c1213204476a6ba043bfdfac16a`.
Raw unfiltered UTF-8 output is `profile-1.log`; metadata `profile-1.json`;
exact target block raw lines 1499–2245 in `profile-target-raw.txt`;
root arithmetic in `profile-summary.json`. The preceding lam command, its whnf roots,
all its asynchronous declaration/lint roots, and 25.7s imports are excluded.

| Disjoint target component | ms | Accounting |
|---|---:|---|
| Outermost gam Elab.command | 7.469 | Includes nested header/value/addDecl events, not summed again. |
| Ten post-command Meta.whnf roots | 0.014 | Only roots following gam command. |
| Two addDecl Elab.async roots | 0.205 | Includes gam and generated proof kernel children. |
| Outermost gam async linter | 14.400 | Nested lint children already included. |
| Standalone compiler roots | 0 | None emitted for this noncomputable definition. |
| **Total** | **22.088** | Mutually disjoint outermost roots. |

Kernel children total 0.170ms, already inside the 0.205ms asynchronous addDecl roots;
remaining async overhead is 0.035ms. Equivalent disjoint split: 7.469 command + 0.014
whnf + 0.170 kernel + 0.035 async overhead + 14.400 lint + 0 compiler = 22.088ms.
Below 750ms repeat threshold and 1000ms budget; no repeat required, no failed samples.
Buzz outcome: FAST-BOARD. Limit raises removed 0 / added 0; deferrals/big changes none.
No profiling scaffolding touches production source.

### Independent contract and negative binder tests

Initial independently implemented original right-hand side passed compiled kernel `rfl`
and exact full type AST/universe list/binder-name/order/BinderInfo/value checks, exit 0,
45.085s, `independent.log/json`. Initial input is retained as
`independent-initial.lean`. Its construction did not refer to Roth.gam.
The stronger final verifier `independent.lean` also independently reconstructs original
lam, so neither gam nor lam is used to construct originalGam; this additionally checks
each actual/original body type against its full effective type. Final result below.
Both effective telescopes are exactly explicit δ : ℝ, n : ℕ, m : ℕ → ℝ with no
universes. The actual constant and independent original have only propext,
Classical.choice, Quot.sound axioms. `#print axioms` and checked allowlists retained.

Actual native `lean_run_code` compiled the batched three negative drop tests this time;
no external-scratch/import workaround was needed. Complete `drop-native.json` reports
success=false, timed_out=false with only expected unresolved δ at line 3, n at 4, and
m twice at 5. This rejects each drop candidate with autoImplicit=false. It is expected
negative evidence, never represented as a successful file diagnostic gate. Test input
is `drop-all.lean`; no drop was applied to source.

Actual affected-module invocation `lake build Roth.MainLemma Roth.Main` exited 0,
4.620s, replaying unchanged modules; full warnings retained in affected-build.log/json.
Actual complete source invocation `lake env lean Roth/MainLemma.lean` exited 0,
32.798s, with only existing unused hδ0/hr₁ warnings; `file-final.log/json`.

Final stronger independent verifier exited 0 in 40.912s (`independent-final.log/json`),
including independently reconstructed originalLam/originalGam, kernel rfl, exact type AST,
effective binders/names/order/BinderInfo/universes, body-type checks and defeq value.
The checked axiom lists remain exactly propext, Classical.choice, Quot.sound.

Final complete unfiltered native `lean_diagnostic_messages` on MainLemma.lean returned
success=true, partial=false, timed_out=false, failed_dependencies=[], zero errors.
Its complete warnings are exactly the initial header at 1 and unused hδ0/hr₁ at 150,
with none on gam; `native-final.json`. Final complete unfiltered native caller diagnostics
on Main.lean have the same four passing flags, zero errors, and existing warnings:
header at 1, hδ at 333, hQ at 474, hc at 475 (`native-caller-final.json`).
No linter is suppressed. No source comment/docstring, pin, theorem, instance or other
original declaration is changed. New-identifier audit: n/a, empty source diff.

### Step 5b: diff-gate status

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Actual lake build Roth.MainLemma Roth.Main, exit 0, 4.620s; full live file lean invocation exit 0, 32.798s. |
| definition_protected | pass | Empty worker source diff and immutable original gam text identical; independent kernel value equality. |
| theorem_statement_protected | pass | No theorem/lemma or other original source edited. |
| structure_gate | pass | One term line, no conjunction or branch, below all relevant bounds. |
| naming_gate | pass | Three-letter lowerCamelCase data name, no forbidden pattern/abbreviation. |
| line_packing_gate | pass | Complete one-row measured table, 46 signature / 72 full codepoints, no next line to pack. |
| inequality_orientation_gate | pass | Complete occurrence table, zero ≥/> and no reversed name. |
| actual telescope/body/type/axioms | pass | Strong independent final probe, exact type AST, BinderInfo/names/order/universes, body types and data rfl/defeq; standard axioms only. |
| caller compatibility | pass | Affected build and complete final native Main diagnostics pass. |
| performance | pass | 22.088ms disjoint outermost target total, no repeats needed. |

Overall worker gates: pass. Parent owns the separate full-build, evaluation, commit and
push checkpoint; this report does not claim that checkpoint or whole-file completion.

### Step 6: result

Before 1 line; after 1 line; saved 0. Audit issues found 0, fixed 0, deferred 0.
Rules applied: none (each rule's prerequisite is absent, as individually recorded).
Renames queued: none; Step 6a sidecar append is n/a. Comments preserved: original public
docstring verbatim, no inline proof comments present. Refactoring needed: none.
Source edits: none. Only this owned report is written in the repository.

### Eleven-step checklist

- [✓] Step 1 — full five references plus applicable style/naming/skills read.
- [✓] Step 2 — full 24-item audit printed with concrete statuses.
- [✓] Step 2.5 — all five actual search methods and auxiliary variants recorded.
- [✓] Step 2.6 — every effective binder audited, native negative drop tests,
  public literature search and inversion check recorded.
- [✓] Step 2.7 — complete measured signature codepoint/packing table printed.
- [✓] Step 2.8 — complete inequality occurrence table printed.
- [✓] Step 3 — all 42 golf rules have individual statuses and reasons.
- [✓] Step 4 — whole-definition term mode/reuse/alternative-strategy reflection done.
- [✓] Step 5a — complete unfiltered live native diagnostics pass all required flags.
- [✓] Step 5b — actual affected build, full-file compile, independent original
  contract/axiom checks and anchored profiling pass; diff-gate table printed.
- [✓] Step 6a — no rename warranted, no sidecar append needed, no source rename applied.

## Artifact manifest, source freeze and ownership release

All evidence is under `/private/tmp/roth-mainlemma-gam/`:

- Immutable original/pre-worker sources: original.lean, pre-worker.lean; hashes and
  declaration-text comparison: source-hashes.json.
- Native complete initial/final/caller evidence: native-initial.json,
  native-final.json, native-caller-final.json.
- Five actual searches: search-all.json, search-source.txt.
- Literature: literature-web.json, literature-query-1.json, literature-query-2.json.
- Independent exact original probes: independent-initial.lean, independent.lean,
  independent.log/json, independent-final.log/json.
- Negative drop tests: drop-all.lean, drop-native.json.
- Actual module and full-file compilation: affected-build.log/json, file-final.log/json.
- Exact anchored profile: profile-prefix.lean, profile-1.log/json,
  profile-target-raw.txt, profile-summary.json.
- Process runner: run.py; empty owned source delta: worker.diff;
  final hashes/sizes/command statuses and report hash: final-manifest.json.

Frozen live-source SHA256:
`0236435831af553f54e04569caadb7b985e0a556dbebf51d454e53abf3ea2abb`.
The entire live file remains byte-identical to pre-worker.lean. All owned subprocess
sessions and native calls have returned; no background compiler/profile/native work
remains. Source, compiler and native ownership are explicitly released to the parent.


## Owner measurement correction (original5 checkpoint review)

The immutable original raw profile remains retained. A fresh owner parser audit found
unindented `Meta.whnf` internal trace events included in the earlier column-zero sum.
The accepted disjoint target total is **22.074 ms**, replacing the earlier
22.088 ms figure for measurement purposes. This counts only the exact target's
column-zero `Elab.command` / `Elab.async` roots, excludes nested/internal Meta events,
and excludes the following `end Roth` command and its asynchronous lint work.
The budget conclusion is unchanged. Both sums and anchors are preserved in
`/private/tmp/roth-mainlemma-owner/prior-profile-root-reaudit.json`; no raw evidence
or original worker report text was overwritten.
