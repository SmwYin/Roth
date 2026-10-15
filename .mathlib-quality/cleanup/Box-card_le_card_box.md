# Phase 4 — `Roth.card_le_card_box`

Baseline: `9e3462f`. Scope: `Roth/Box.lean:59–61` and this report only.
Source before: 3 declaration lines / 1 proof-body line. Final: 4 declaration lines /
2 proof-body lines, plus one scoped `omit` command; net source growth 2 lines.
The source change replaces the lambda arrow with `↦` and composes the cardinality bound
with the equality using `.trans_eq (card_box r)`, removing the intermediate `.le`.
After explicit user approval relayed by the orchestrator, the unused `[DecidableEq σ]`
parameter is omitted and `classical` is local to the proof. The mathematical conclusion,
explicit parameters, and existing docstring are unchanged. No other declaration changed.

## Step 1 — references

Read `golfing-rules.md`, `proof-patterns.md`, `mathlib-search.md`,
`generalisation-patterns.md`, and `cleanup-gates.md` in full; read the declaration's
applicable formatting, documentation, inequalities, visibility, and syntax sections of
`style-rules.md`, plus the lean4 and mathlib-quality skill instructions. The full worker
contract was read, including its middle section through a separate untruncated read.
Naming does not trigger a rename: the name explicitly describes the cardinality bound
against the box, uses snake_case, and contains no forbidden abbreviations or patterns.

## Step 2 — full audit

| # | Item | Finding and action |
|---|---|---|
| 1 | LINT | Initial `unusedDecidableInType` warning for `[DecidableEq σ]` removed after explicit user approval. Scratch and final source compile with local `classical`; no target warnings, errors, or sorry diagnostics. |
| 2 | HAVE SCAN | No `have` expressions in the original or final proof. |
| 3 | SET_OPTION | No declaration-local option or resource-limit override. |
| 4 | SIMP SQUEEZE | No simp calls in the retained proof. |
| 5 | NAMING | `card_le_card_box` is a descriptive snake_case cardinality-bound name; no scheme numbers, forbidden abbreviations, single-letter public name, `_ge_`, or `_gt_`. No rename warranted. |
| 6 | LINE PACKING | Both signature lines measured below; final conclusion with `by` would require 121 codepoints. No repack. |
| 7 | BY PLACEMENT | Final `by` is at the end of the conclusion line, followed by `classical` and the exact term. |
| 8 | FORMAT | Two-space body indentation, four-space signature continuation, no blank line within declaration, no sequential tactics, no `haveI`/`letI`. Replace the ordinary lambda's `=>` with `↦`. |
| 9 | COMMENTS | No inline proof comments. Existing three-line docstring preserved verbatim. |
| 10 | DOCSTRING | Existing documentation describes the bound, containment interpretation, and source/application context. Preserve it under the signature/docstring fence. |
| 11 | VISIBILITY | Public API used in `Roth/CoeffNorm.lean:307` and `Roth/MainLemma.lean:618`; keep public. This is not a module-system file. |
| 12 | STRUCTURE | Final two-line proof, no conjunction in statement, no branches; no extraction/decomposition needed. |
| 13 | MATHLIB | Five-method block below. Existing `Finset.card_le_card` supplies the generic bound; `mem_box` and `card_box` supply project construction facts. Retain the documented public API under the user's preservation instruction. |
| 14 | JUNK DEF | n/a: theorem, not a definition. |
| 15 | EXISTS LEMMA | n/a: public cardinality inequality, no existential wrapper. |
| 16 | SHOW vs CHANGE | No `show` or `change`. |
| 17 | PUSH_NEG | No negation-pushing tactic. |
| 18 | GENERALISE | Every parameter considered below; only unused decidability has a verified drop candidate. No speculative additional API. |
| 19 | INEQUALITY | Both inequalities use `≤`; zero `≥`/`>` in signature/hypotheses. Table below. |
| 20 | NORMAL-FORM | Natural cardinality upper bound against the product is already the useful normal form for coefficient counts. |
| 21 | SYNTAX-GEN | OK: coordinatewise boundedness matches both external call sites directly. No alternative bundling improves those uses. |
| 22 | IMPORT-FANOUT | n/a: no new import. |
| 23 | CASTS | 0 dropped / 0 kept as cross-type / 0 kept as load-bearing; no casts/ascriptions in the proof diff. |
| 24 | INSTANCE-NAME | n/a: theorem, no instance declaration. |

Issues fixed: ordinary lambda syntax; redundant conversion of an equality into a second
inequality before transitivity; unused decidability instance. The instance omission was
initially reported, then applied only after the orchestrator relayed explicit user approval
for verified unused positivity and DecidableEq assumptions. The prior full build finished
before the approved edit started.

## Step 2.5 — mathlib search status

| Method | Query/evidence | Outcome |
|---|---|---|
| A — Lean-Finder | `finite set of functions bounded coordinatewise has cardinality at most product of coordinate bounds` | Returned `Fintype.card_filter_piFinset_const`, `Fintype.card_filter_piFinset_const_eq_of_mem`, and an unrelated pair-reduction bound. Product-cardinality infrastructure exists; no direct project theorem replacement found. |
| B — Loogle | `Finset.card _ ≤ Finset.card _` | Returned `Finset.card_erase_le`, `card_filter_le`, `card_image_le`; the generic subset bound was confirmed separately. |
| C — LeanSearch | Unavailable in this cleanup session: established HTTP 500, per dispatch instructions do not repeat a failed service call | Unavailability is not a claim of absence. |
| D — mathlib source | Untruncated search for `card_le_card_box`; variants `card_le_card`, `card_pi`, `card_map` in finset cardinality and finite-product files | No project-name copy; `Finset.card_le_card` at `Mathlib/Data/Finset/Card.lean:66`, and injection/surjection variants at 430–455. |
| E — local name search | `Finset.card_le_card` | Source-backed hits include `Finset.card_le_card` and `Finset.card_le_card_of_injOn`. Index reported `unavailable`; no absence conclusion drawn from index. |

Auxiliary variants checked: `_of_injOn`, `_of_injective`, `_of_surjOn`,
`_of_surjective`, `card_map`, finite-product cardinality. Common-equivalents table:
finite-subset/cardinality reasoning is the applicable generic concept.

Compiled `#check` verified `Finset.card_le_card`, `Fintype.card_piFinset`, and
`LE.le.trans_eq`. Live `exact?` failed to close the target without the current theorem;
`apply?` produced only incomplete generic inequality reductions, including
`Nat.le_of_lt_succ`, not a proof. We do not infer a global absence theorem from these
searches. Conclusion: partial generic match; the retained proof already builds on
mathlib and the local box API. Deleting a documented public theorem used by two files
would contradict the user's current API-preservation instruction; no deletion applied.

## Step 2.6 — generalisation status

| # | Parameter | Class | Use | Mechanical candidates | Verification/result |
|---|---|---|---|---|---|
| 1 | `{σ : Type*}` | type variable/universe | Domain of `r`, finsupps, finite product | Already universe-polymorphic; deleting the domain binder does not preserve a well-scoped signature | Retain; no universe weakening available. |
| 2 | `[Fintype σ]` | typeclass | `∏ j` and the box APIs | Drop; replacing by `Finite` alone also cannot supply the finite product's required `Fintype` | Drop scratch failed to synthesize `Fintype σ` at conclusion and box/card calls. A replacement using chosen finite structure changes the signature/construction and is not warranted. |
| 3 | `[DecidableEq σ]` | decidability | Only implementation/API instances of the proof | Drop and use local `classical` | Compiled scratch success; explicitly approved by user and applied as `omit [DecidableEq σ] in` before the unchanged docstring, with local `classical`. Final complete diagnostics and type check pass. |
| 4 | `{r : σ → ℕ}` | structure value | Coordinate bounds and cardinality product | No typeclass parent applies; removing binder leaves the named data unbound | Retain; its values are essential to the theorem, not an assumption to weaken. |
| 5 | `{s : Finset (σ →₀ ℕ)}` | structure value | Membership hypothesis and `s.card` | No weakening without restating the object/count | Retain; needed in both hypothesis and conclusion. |
| 6 | `hs : ∀ d ∈ s, ∀ j, d j ≤ r j` | proposition | Gives inclusion in the box | Drop; point-localisation already restricted to `d ∈ s`; strict-to-weak already weak `≤` | Drop scratch failed at unknown `hs`. The assertion without it is false, e.g. two distinct one-coordinate indices with bound zero. Retain. |

Inversion check: the result is precisely the generic finite-subset cardinality bound
specialized through `mem_box` and `card_box`. That abstract theorem already exists as
`Finset.card_le_card`; creating another abstract companion would duplicate mathlib.

Verified and user-approved generalisation: omit the unused `[DecidableEq σ]`, introducing
`classical` in its proof. The following scratch proof compiled before applying it:

```lean
example {σ : Type*} [Fintype σ] {r : σ → ℕ} {s : Finset (σ →₀ ℕ)}
    (hs : ∀ d ∈ s, ∀ j, d j ≤ r j) : s.card ≤ ∏ j, (r j + 1) := by
  classical
  exact (Finset.card_le_card fun d hd ↦ Roth.mem_box.2 (hs d hd)).trans_eq (Roth.card_box r)
```

### Literature search

Web query: `finite set bounded multi indices cardinality product coordinate bounds generalization`.
Top three returned hits were:

1. [On multiple sum and product sets of finite sets of integers](https://comptes-rendus.academie-sciences.fr/mathematique/articles/10.1016/j.crma.2003.08.010/) — additive-combinatorics topic; no relevant weakening established.
2. [Bonn preprint, bounds on cardinality of index sets](https://ins.uni-bonn.de/media/public/publication-media/INSPreprint1805.pdf?pk=1287) — concerns more specialized index regions; no change to this coordinate-box bound established.
3. [Cardinality of a finite Cartesian product](https://androma.org/theorems/15123) — elementary product formula; contextual secondary hit, not relied on for the Lean proof.

The canonical general construction is already present in mathlib's checked
`Fintype.card_piFinset` and `Finset.card_le_card`. Search did not establish a further
useful project-specific weakening. ChatGPT math MCP: n/a, no callable tool is installed
(discovery returned no such tool). No literature-driven new API proposed.

## Step 2.7 — line packing

Final actual `#check @Roth.card_le_card_box` with `format.width 100`:

```text
@Roth.card_le_card_box : ∀ {σ : Type u_1} [inst : Fintype σ] {r : σ → ℕ} {s : Finset (σ →₀ ℕ)},
  (∀ d ∈ s, ∀ (j : σ), d j ≤ r j) → s.card ≤ ∏ j, (r j + 1)
```

Measured original signature (before the approved omission/local classical proof):

| Signature line | Codepoints | Next complete signature unit | Arithmetic | Action |
|---|---:|---|---|---|
| 59 | 91 | `s.card ≤ ∏ j, (r j + 1) :=` (26) | 91 + 1 + 26 = 118 > 100 | ok |
| 60 | 30 | None; proof body follows | n/a: final signature line | ok |

Final signature after approval (the scoped `omit` precedes the docstring):

| Signature line | Codepoints | Next complete signature unit | Arithmetic | Action |
|---|---:|---|---|---|
| 60 | 91 | `s.card ≤ ∏ j, (r j + 1) := by` (29) | 91 + 1 + 29 = 121 > 100 | ok |
| 61 | 33 | None; proof body follows | n/a: final signature line | ok |

## Step 2.8 — inequality scan

| # | Location | Original | Rewrite | Rename? |
|---|---|---|---|---|
| 1 | `hs`, final line 60 | `d j ≤ r j` | None: correct orientation | No |
| 2 | conclusion, final line 61 | `s.card ≤ ∏ j, (r j + 1)` | None: correct orientation | No |
| 3 | entire signature/hypotheses | n/a: zero `≥`/`>` | None | No `_ge_`/`_gt_` in name |

## Step 3 — all 42 golfing rules

| Rule | Status |
|---|---|
| 1.1 by exact wrapper | Initial term proof has none; final `by` is needed for the local `classical` command, so not a redundant wrapper. |
| 1.2 by rfl | n/a: no reflexivity wrapper. |
| 1.3 rw + exact | n/a: no rewrite before the final exact. |
| 1.4 simp + exact | n/a: no simplification chain. |
| 1.5 trailing rfl | n/a: no rfl. |
| 1.6 constructor + exact | n/a: no conjunction/constructor. |
| 1.7 apply + exact | n/a: exact supplies the direct composed term; no apply prefix. |
| 1.8 by_contra + push_neg | n/a: no contradiction proof. |
| 1.9 eta reduction | Lambda is not eta-reducible: it composes `mem_box.2` with `hs d hd`. Changed arrow to `↦` as syntax cleanup. |
| 1.10 single-use have | n/a: no have. |
| 1.11 apply + intro | n/a: term lambda already supplies inclusion. |
| 1.12 redundant show | n/a: no show. |
| 1.13 have + projections | n/a: no have/projection pair. |
| 1.14 consecutive rw | n/a: no rw. |
| 1.15 terminal simp only | n/a: no simp only. |
| 1.16 nonterminal bare simp | n/a: no retained simp. |
| 1.17 dot notation | Already used; direct `.trans_eq` replaces `.trans ... .le`. |
| 1.18 avoid trailing parentheses | Parentheses around the cardinality proof are necessary for its dot receiver; parentheses around `card_box r` delimit the equality argument. No `<|` improvement. |
| 1.19 push_neg | n/a: absent. |
| 1.20 trivial single-use exists | n/a: no existential lemma. |
| 2.1 grind | Live `by grind` failed at the assumed reverse cardinality inequality; no containment-to-count bridge discovered. |
| 2.2 delete before grind | n/a: no retained grind. |
| 2.3 simpa consolidation | n/a: no simp followed by closing tactic to consolidate. |
| 2.4 fun_prop | n/a: no analytic/function-property goal. |
| 2.5 positivity | n/a: target is an arbitrary cardinality comparison, not nonnegativity/positivity/nonzero. |
| 2.6 gcongr | Live `by gcongr` made no progress. |
| 2.7 lia/omega | Live `by lia` failed; the missing link is finite-set inclusion, not linear arithmetic. No omega substitution retained. |
| 2.8 aesop | Live `by aesop` failed, made no progress. |
| 2.9 norm_num/norm_cast | n/a: no concrete arithmetic or casts. |
| 2.10 decide | n/a: universally parameterized data cannot be closed by finite reduction. |
| 2.11 field_simp; ring | n/a: no denominators or ring equality. |
| 2.12 linear_combination | n/a: no ring/ring_nf ending or polynomial identity. |
| 2.13 wlog | n/a: no symmetric case branches. |
| 2.14 collapse calc | Already one composed term; improved mixed inequality/equality composition with trans_eq. |
| 2.15 multiple goals | n/a: one term goal, no duplicated branches. |
| 3.1 erw → rw | n/a: no erw. |
| 3.2 legacy analytic tactics | n/a: absent. |
| 3.3 omega → lia | n/a: no omega; lia trial recorded in 2.7. |
| 3.4 rcases rfl | n/a: no destructuring. |
| 3.5 automation attributes | No new attribute: this dependent bound has two explicit project callers, and no concrete repeated automation failure warrants a global rule. |
| 3.6 simp_all | n/a: no simp_all only. |
| 3.7 remove resource options | n/a: none present. |

## Step 4 — reflection and experiments

The mathematics is containment followed by finite-cardinality monotonicity and the box
cardinality formula. The composed term expresses precisely this; the final proof adds local classical decidability after the approved instance omission. The equality
step now uses `LE.le.trans_eq`, avoiding a gratuitous weakening to another inequality.
Bare `simp` made no progress. `grind`, `aesop`, `gcongr`, and `lia` failed as reported;
`exact?` failed and `apply?` only suggested incomplete generic steps. The tested trans_eq
term had no diagnostics and no remaining goals. No single-tactic replacement succeeded.

The first multi-attempt batch at the term position omitted `by`, so Lean interpreted
names such as `grind` as terms and rejected them as unknown identifiers. That batch is
not evidence about the tactics. The corrected live batch used `by grind`, `by simp`,
etc., obtaining the actual failures above without modifying the source.

## Step 5 — verification and gates

- Complete live `lean_diagnostic_messages` on `Roth/Box.lean`: `success=true`,
  `partial=false`, `timed_out=false`, no errors and no sorry diagnostics. Existing
  header and later-declaration warnings remain; the target unused-decidability warning
  is gone after the approved change.
- Isolated `lean_run_code` example with the exact proposed retained term: success.
  Initial original theorem type checked; final full generalized theorem type assigned
  to `@Roth.card_le_card_box` without DecidableEq: success.
- Final `#check` and live hover confirm exactly the approved DecidableEq omission. Native `lean_verify`
  on the final source returns `trust=standard`, axioms `propext`, `Classical.choice`,
  `Quot.sound`, no nonstandard axioms and no suspicious source warnings. Some isolated
  import checks reported an informational import-refresh message; the final native
  verify and actual module build provide the authoritative source verification.
- `/Users/ramin/.elan/bin/lake build Roth.Box`: actual exit 0, 1154 jobs,
  `/private/tmp/roth-box-d04-module.log` initially, then independently
  `/private/tmp/roth-box-d04-module-approved.log` after the approved change.
- Diff inspected: only the scoped omission and target proof changed. No definition,
  docstring, import, visibility, or other declaration changes. Conclusion unchanged.
- Full project and `Roth.LeanEval` builds belong to the file orchestrator, notified
  immediately when this module gate passed.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | `lake build Roth.Box` exit 0, 1154 jobs; log above. |
| definition_protected | pass | No definition/abbrev changed. |
| theorem_statement_protected | pass | Approved unused-instance omission only; full generalized type compiles and conclusion is unchanged. |
| structure_gate | pass | Body 2 lines, no conjunction, no branch. |
| naming_gate | pass | Descriptive cardinality-bound name; no forbidden pattern or abbreviation. |
| line_packing_gate | pass | Full final two-row width table; 121 exceeds 100 at the only break. |
| inequality_orientation_gate | pass | Two ≤ occurrences; zero reversed inequalities. |

Overall: pass for the proof cleanup and explicitly approved unused-instance removal.
Target warning fixed; unrelated existing file warnings remain.

## Step 6 — result

Before: 3 declaration lines / 1 body line. After: 4 / 2, plus the scoped `omit`
command. Net source growth: 2 lines. All three identified issues fixed, including the
verified signature change after explicit user approval.
Rules applied: 1.17 / mixed transitivity refinement, ordinary lambda syntax; existing
composed proof retained inside the local classical block. Renames queued: none. Inline comments:
none present. Existing docstring: preserved verbatim.

Refactoring needed: none for this declaration. User approved the previously reported
unused-instance omission, and it is implemented and verified. No deletion, new theorem,
abstract companion, or further API restatement requested by this worker.

Phase checklist:

- [x] Step 1 — reference docs read.
- [x] Step 2 — all 24 audit items recorded.
- [x] Step 2.5 — all five search methods addressed, unavailable service explicit.
- [x] Step 2.6 — parameter table, verified candidate, inversion and literature search.
- [x] Step 2.7 — every signature line measured.
- [x] Step 2.8 — inequality occurrences scanned.
- [x] Step 3 — all 42 rules have concrete statuses.
- [x] Step 4 — whole-proof alternatives tested and reflection recorded.
- [x] Step 5a — complete LSP diagnostics, no errors/sorries.
- [x] Step 5b — diff, module, type, and axiom gates passed.
- [x] Step 6a — no rename required; queue untouched.

Source ownership released to the file orchestrator on delivery of this report.

Additional approved-change experiment: a scratch term-local `open scoped Classical in`
did not synthesize `DecidableEq σ` for these box API applications in this environment.
The final tactic-local `classical` form compiled, and live `lean_goal` on the final
`exact` line returned an empty `goals_after` array. The final no-DecidableEq full type
check completed without import-refresh diagnostics.

Final approved-source publication verification: full `lake build` session 11996 exited 0
(2586 jobs; `/private/tmp/roth-box-d04-full-approved.log`), separate
`lake build Roth.LeanEval` session 35385 exited 0 (2585 jobs;
`/private/tmp/roth-box-d04-leaneval-approved.log`). These runs supersede the earlier
proof-only full build 90150 and verify the selected generalized signature plus all callers.
