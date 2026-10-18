# Cleanup: original declaration 28, private `Roth.degreeOf_map_intCast`

## Initial audit — recorded before source edits

Scope: only the private lemma at input lines 450–452 and its exact two callers in
`exists_int_factors` and `exists_det_eq_mul`. Input: 553 lines, 25 retained declarations,
clean source at parent-dispatched HEAD `27f4b08`. No Git mutations, shared logs, or agents.
Skills: lean4 and mathlib-quality. Read golfing-rules.md, proof-patterns.md,
mathlib-search.md, generalisation-patterns.md, cleanup-gates.md, Phase 4 of installed
cleanup.md, and relevant style, naming, profiling references. Private declaration:
literature search is explicitly exempt. Public contracts and documentation retained.

Baseline `lake build Roth.Separation` exited 0; raw
`/private/tmp/roth-d28-baseline-build.log`. Native complete unfiltered LSP:
`/private/tmp/roth-d28-lean_diagnostic_messages.json`: partial=false, timed_out=false,
success=true, 0 errors, 6 warnings, 0 infos. The header warning is user-preserved;
the five warnings concern existing public instance binders and are outside this leaf's
authorized changes. Target has no warning. Full project baseline supplied by parent.

| # | Audit item | Initial result/action |
|---|---|---|
| 1 | LINT | No target lint; baseline module warnings recorded above. |
| 2 | HAVE SCAN | No `have` in the one-line proof. |
| 3 | SET_OPTION | None. |
| 4 | SIMP SQUEEZE | No simp. |
| 5 | NAMING | Describes degree, map, integer cast; no forbidden names/patterns. |
| 6 | LINE PACKING | Two-line signature; table below. Deletion proposed. |
| 7 | BY PLACEMENT | `by` ends conclusion line. |
| 8 | FORMAT | Two-space tactic indent, no interior blank, one rw. |
| 9 | COMMENTS | No target inline comment; preserve all surrounding prose. |
| 10 | DOCSTRING | None, appropriate for private helper. |
| 11 | VISIBILITY | Private, exactly two local callers. |
| 12 | STRUCTURE | One tactic, no conjunction, no branches. |
| 13 | MATHLIB | Generic degrees preservation supplies result; remove thin private wrapper and replace exact callers. |
| 14 | JUNK DEF | n/a: lemma, not data definition. |
| 15 | EXISTS LEMMA | n/a: equality, no existential. |
| 16 | SHOW vs CHANGE | No show in original. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | Compiled generic semiring/injective-hom version; no new helper needed: use mathlib. |
| 19 | INEQUALITY | No > or ≥; table below. |
| 20 | NORMAL-FORM | `degreeOf` equality is canonical partial-degree form; obtained by counting generic degrees equality. |
| 21 | SYNTAX-GEN | Direct degrees rewrite fits first caller; count congruence fits second caller. |
| 22 | IMPORT-FANOUT | No new import. |
| 23 | CASTS | No value casts/ascriptions in target or planned diff; `Int.castRingHom ℚ` specifies coefficient hom. |
| 24 | INSTANCE-NAME | n/a: no instance. |

### Five actual search methods

| Method | Actual result |
|---|---|
| A Lean-Finder | Native success: `MvPolynomial.degrees_map_of_injective` first result. |
| B Loogle | Native success, query `MvPolynomial.degreeOf (MvPolynomial.map _ _) = _`, empty results; not an absence claim. |
| C LeanSearch | Native success: same degrees theorem first result, plus renaming/Polynomial candidates. |
| D source | Full untruncated rg for degreeOf map/injective variants and degrees source; Degrees.lean:196 gives generic theorem, :216 degreeOf definition. |
| E local names | `degrees_map` success with source hits; index=warming, so no indexed absence claim. |

Raw `/private/tmp/roth-d28-lean_{leanfinder,loogle,leansearch,local_search}.json`.
No absence claim. All six strict rules considered: use direct mathlib (1,5); actual
five methods and compiled generic proof (2); degree/degrees/rename variants (3);
generic CommSemiring/injective hom route (4); usage recorded here (6), module docstring
preserved per leaf scope. Native live `exact?` failed; generic proof compiles.

### Every effective binder / generalisation

Live `lean_goal` context contains exactly σ, U, j, no enclosing τ/Fintype/DecidableEq.
`/private/tmp/roth-d28-goal.json`.

| Binder | Drop/weakening probe | Outcome |
|---|---|---|
| `{σ : Type*}` | Universe-polymorphic already; remove σ while leaving U/j type unchanged | Syntactically necessary free variable, not claimed compiler-tested negative. |
| `(U : MvPolynomial σ ℤ)` | Remove U with unchanged conclusion | Free variable needed on both sides; not claimed compiler-tested negative. Generic coefficient R compiled. |
| `(j : σ)` | Remove j with unchanged conclusion | Free variable needed; not claimed compiler-tested negative. No Fintype/DecidableEq assumption required. |
| Concrete ℤ→ℚ map | R,S CommSemiring plus f injective | Compiled independent generic example via degrees_map_of_injective; no Field, Ring, domain, finite variable requirements. |

No propositional hypotheses/typeclass binders to weaken or point-localize, no strict
hypotheses. Inversion check fires: the proof depends only on injectivity of the map;
existing generic mathlib theorem is the abstraction. Delete wrapper rather than add
a generalized private helper. Independent exact original type proof succeeds with
`classical; exact congrArg (Multiset.count j) (degrees_map_of_injective U Int.cast_injective)`.
Raw `/private/tmp/roth-d28-independent.json` (two scratch long-line warnings only).

### Initial signature widths and inequality scan

| Input line | Codepoints | Next complete unit | Arithmetic | Action |
|---|---:|---|---|---|
| 450 | 79 | conclusion `degreeOf j (map (Int.castRingHom ℚ) U) = degreeOf j U := by` (59) | 79+1+59=139>100 | ok |
| 451 | 63 | end of signature | terminal | ok |

| Occurrence | ≥ | > | Action |
|---|---:|---:|---|
| All target signature/hypotheses | 0 | 0 | none |

### Initial planned change

Remove 3-line private wrapper and one separator; use mathlib degrees preservation in
the two authorized exact caller sites. Keep all public signatures byte-identical.
No helper added. No pending public proposal from this leaf.

## Golf pass — all 42 rules

| Rule | Concrete status |
|---|---|
| 1.1 | n/a: no by-exact wrapper. |
| 1.2 | n/a: no by-rfl wrapper. |
| 1.3 | n/a: no rw followed by exact. |
| 1.4 | n/a original; caller hdeg uses terminal simpa using hr none. |
| 1.5 | n/a: no trailing rfl. |
| 1.6 | n/a: no constructor. |
| 1.7 | n/a: no apply/exact chain. |
| 1.8 | n/a: no contradiction. |
| 1.9 | n/a: no lambda. |
| 1.10 | n/a: no original have; caller hdeg has subsequent use. |
| 1.11 | n/a: no introductions. |
| 1.12 | n/a: no show. |
| 1.13 | n/a: no projections/have. |
| 1.14 | Already one combined rw; caller replacement remains one combined rw. |
| 1.15 | Applied terminal simp policy: final caller uses unsqueezed simpa. |
| 1.16 | n/a: no nonterminal simp. |
| 1.17 | n/a: no applicable dot-notation chain in replacement. |
| 1.18 | n/a: no trailing term parentheses improved by <|. |
| 1.19 | n/a: no push_neg. |
| 1.20 | n/a: not an existential lemma. |
| 2.1 | Native live grind failed on actual original target; raw attempts log. |
| 2.2 | n/a: no preceding tactics before grind. |
| 2.3 | Native live simp failed original; final hdeg consolidation compiled. |
| 2.4 | n/a: no analytic function-property proposition. |
| 2.5 | n/a: equality of degrees, not positivity/nonzero. |
| 2.6 | n/a: no inequality chain in target; caller hdeg is equality rewrite plus given bound. |
| 2.7 | n/a: no linear arithmetic relationship to solve. |
| 2.8 | Native live aesop failed, no progress. |
| 2.9 | n/a: no concrete numeric computation/value casts; Int.castRingHom is a hom. |
| 2.10 | n/a: arbitrary polynomial over arbitrary variable type, not finite computation. |
| 2.11 | n/a: no division/ring-expression identity. |
| 2.12 | n/a: no ring/ring_nf closing proof or algebraic hypotheses. |
| 2.13 | n/a: no symmetric branches. |
| 2.14 | n/a: no calc. |
| 2.15 | n/a: single target, no parallel subgoals. |
| 3.1 | Already rw, no erw. |
| 3.2 | n/a: no legacy continuity/measurability. |
| 3.3 | n/a: no omega; arithmetic rule 2.7 inapplicable. |
| 3.4 | n/a: no rcases. |
| 3.5 | n/a: deleted private specialization; no global automation attribute warranted. |
| 3.6 | n/a: no simp_all. |
| 3.7 | n/a: no limit options. |

### Step back / simplify review

Original target is already one rw, but it recreates generic degree preservation from
support. `exact?`, grind, simp, and aesop failed live; direct counting congruence succeeds
with classical equality. A standalone proof works, but a direct counting term in the
actual Option caller exposed a DecidableEq defeq mismatch. Repair: named `degreeOf_def`
normalization under the caller's existing instance, explicit f parameter in the degrees
lemma, and terminal simpa. The first caller directly rewrites degreeOf/degrees and needs
no intermediate local helper. Native multi_attempt line replacement of first multiline
rw left a dangling original continuation (therefore not claimed a successful complete
file gate); subsequent actual module LSP/build checks establish the whole replacement.
An initial compiler run failed on the counting expression and is retained as
`/private/tmp/roth-d28-build.log`; final gates use the repaired source.

Simplify pass: PASS-THROUGH after the repair and line packing. Built-in simplify is not
available in this runtime; equivalent holistic review performed directly: no repeated
proof skeleton, no new helper, direct mathlib reuse at both exact callers. No follow-up
suggestion or public proposal. Phase 3 file-level work: none in this one-leaf scope;
header/imports/documentation preserved. Phase 5a: private mathlib-wrapper deletion,
two exact caller substitutions. Phase 5b: empty leaf rename queue, 0 names queued,
0 applied, 0 conflicts; shared queue untouched by contract.

## Final validation artifacts

Final source: 551 lines, 24 retained declarations (20 public constants: 19 theorems
and `coeffNone`; 4 private lemmas). Input 553 lines/25 declarations. Target 3 declaration
lines → 0, separator removed, caller changes add 2 lines: net -2. Git numstat: 5 added,
7 removed. No new helper. All public theorem signatures are byte-identical to input;
the existing public definition is untouched. Comments: 0 target proof comments before,
0 after; all file docstrings and narrative text preserved.

Module command `/Users/ramin/.elan/bin/lake build Roth.Separation` exited 0 after
final line packing: `/private/tmp/roth-d28-packed-build.log`. Earlier repaired module
build also exited 0: `/private/tmp/roth-d28-final-build.log`.

Independent exact ORIGINAL private type (snapshot lines 517–519) proved without the
removed helper or either caller: `/private/tmp/roth-d28-proof.lean`;
`lake env lean /private/tmp/roth-d28-proof.lean` exited 0, raw
`/private/tmp/roth-d28-proof.log`. Also proves arbitrary CommSemiring coefficients and
injective hom. `#check @independent_d28` at `format.width 100` confirms exactly σ,U,j;
actual built public callers' axioms checked with `#print axioms`. All three proofs use
only `[propext, Classical.choice, Quot.sound]`. Removed private target confirmed absent
by enumerating actual environment constants and exact suffix
`.Roth.degreeOf_map_intCast`, without guessing private name components.

Fresh binder-drop tests performed after initial audit: native log
`/private/tmp/roth-d28-binder_explicit.json`, autoImplicit=false. Dropping σ/U/j causes
the expected unknown-identifier errors in each respective unchanged statement. The
earlier autoImplicit=true probe reconstructed σ implicitly, so it was not treated as
evidence that σ is redundant. Negative scratch probes are intentional failures, never
claimed successful gates. Native scratch tool mentions stale imports; authoritative
independent type/axiom checks use the compiler after the completed final module build.

### New-identifier verification

| Identifier newly used in source diff | Verified by |
|---|---|
| `degrees_map_of_injective` | Native local search, source Degrees.lean:196, native #check, actual module build. |
| `degreeOf_def` | Source Degrees.lean:220, live caller proof and actual module build. |
| `degreeOf` | Already used throughout source; definition Degrees.lean:216. |

No value casts added (0 dropped / 0 cross-type / 0 load-bearing); no new import,
option, instance, attribute, sorry, axiom, native_decide, haveI/letI, limit raise, or
profiling scaffolding. `Int.castRingHom ℚ` is needed to select the coefficient hom.

### Final widths / inequalities

Removed private signature has no final lines. Original per-line table above remains
the audited table; retained public signatures are unchanged. Replacement body widths:

| Lines | Widths | Packing check |
|---|---|---|
| first caller rw 502–503 | 91, 95 | long lemma with explicit hom, natural comma break; ≤100. |
| hdeg 527–529 | 45, 32, 91 | by at end; next complete degrees lemma plus first simp line exceeds 100. |

| Occurrence in replacement | ≥ | > | Action |
|---|---:|---:|---|
| All added lines | 0 | 0 | none |

### Complete unfiltered final native LSP

`/private/tmp/roth-d28-packed_lsp.json`: partial=false, timed_out=false,
success=true, 0 errors, 6 warnings, 0 infos, 0 hints, failed_dependencies=[].
All six warnings are unchanged in substance from baseline: one user-preserved header,
one unused-section-vars warning and four public instance warnings. No suppression.
No target or replacement warning. Public instance removals remain pending parent/user
approval and outside this leaf's scope.

### Buzz / actual anchored profile

Outcome: FAST-BOARD for target and affected callers. Actual repository module command
`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true
-Dtrace.profiler.threshold=0 Roth/Separation.lean` exited 0 after all preceding
Lean/MCP/compiler requests completed. Raw `/private/tmp/roth-d28-final-profile.log`,
parsed `/private/tmp/roth-d28-final-profile.log.json`. No extracted namespace proxy.
Baseline supplied unchanged-target actual-module run:
`/private/tmp/roth-d27-final-profile.log` and `.log.json`.
Times use maximum outer command plus outer async proof; no nested-node double count.

| Actual declaration | Baseline command + proof = conservative ms | Final command + proof = conservative ms | Final raw command/proof anchor lines |
|---|---|---|---|
| removed private degreeOf_map_intCast | 8.614 + 28.010 = 36.624 | removed, no final elaboration cost | absent |
| Roth.exists_int_factors | 64.279 + 606.011 = 670.290 | 67.978 + 666.075 = 734.053 | 821065 / 828761 |
| Roth.exists_det_eq_mul | 108.419 + 421.044 = 529.463 | 111.276 + 434.620 = 545.896 | 961634 / 983081 |

Both affected retained declarations are below 750ms repeat threshold and 1000ms budget;
no repeat or performance repair required. No claim of speed improvement: the first
caller measured somewhat slower; deleting the redundant private declaration is the
cleanup benefit. Limit raises removed 0 / added 0; deferred over-budget declarations
none in this leaf; no performance-driven public proposal.

### Phase 4 and final gates

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | actual packed `lake build Roth.Separation`, exit 0, packed-build.log |
| definition_protected | pass | no def/abbrev change |
| theorem_statement_protected | pass | authorized private wrapper removal; every retained public signature unchanged |
| structure_gate | pass | original one-line proof; deleted target; only exact caller proof substitutions |
| naming_gate | pass | no forbidden pattern, no rename required |
| line_packing_gate | pass | initial complete signature table; no final private signature; public signatures untouched |
| inequality_orientation_gate | pass | both occurrence tables have 0 forbidden orientations |
| cumulative_no_unintended_breakage | pass for leaf | both actual callers in same built module; parent owns cumulative whole-original compatibility/full project/LeanEval |
| complete native LSP | pass | freeze_lsp.json: partial=false, timed_out=false, 0 errors, same 6 existing warnings, 0 infos/hints |
| independent original proof / actual axioms | pass | proof.log, exit 0; only standard axioms |
| simplify | PASS-THROUGH | direct holistic equivalent; unavailable built-in explicitly recorded above |
| buzz | FAST-BOARD | both changed callers below 750ms and 1000ms |

Overall: pass for this declaration leaf. Full project / cumulative compatibility /
separate LeanEval build remain parent's explicitly assigned post-freeze gates.

### Eleven-step completion checklist

- [✓] Step 1 — full golf/pattern/search/generalisation/gate references and relevant style/naming/profiling read.
- [✓] Step 2 — 24-item initial audit recorded before source edits.
- [✓] Step 2.5 — all five fresh actual search methods and six replacement rules recorded.
- [✓] Step 2.6 — every effective binder, generic compiled probe, concrete-map inversion check, private literature exemption.
- [✓] Step 2.7 — complete two-line original signature codepoint/packing arithmetic table.
- [✓] Step 2.8 — original/final inequality occurrence tables.
- [✓] Step 3 — all 42 golf-rule statuses, actual applicable live tactic trials.
- [✓] Step 4 — step-back strategy and holistic simplify review.
- [✓] Step 5a — final complete unfiltered native module LSP, unchanged warning inventory.
- [✓] Step 5b — actual module build, diff gates, independent original proof, actual axioms, anchored profile.
- [✓] Step 6a — no rename needed; shared sidecar untouched; report and freeze completed.

Applied: remove private degreeOf_map_intCast wrapper, replace its exact two local calls
with existing generic mathlib degrees preservation. Comments-preserved: none present
inside target; all surrounding narrative/docstrings unchanged. Renames queued: none.
Refactoring needed: none from this leaf. No new helper; no pending concrete proposal.

### Freeze / handoff

All native Lean/MCP requests completed; compiler/build sessions 8832, 32791 (intentional
failed attempt), 87112, 50226, 34905, 85989 finished and drained. Final post-profile
complete native LSP saved in `/private/tmp/roth-d28-freeze_lsp.json`. No outstanding
source operations. Source SHA256:
`4a1043e85ba9f8cc40be0801aa9bbc8e733f3ebc7beaf60449c884bad858e3b3`.
ALL source ownership revoked. Worker is report-only from this handoff; no source edit
after freeze. Parent owns all subsequent source/Git/build operations.

## Owner cumulative publication gates

Source FROZEN SHA256 `4a1043e85ba9f8cc40be0801aa9bbc8e733f3ebc7beaf60449c884bad858e3b3`; leaf ownership revoked and requests drained before owner gates. Owner probe `18565` exit0,40.91s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL24 actual retained standardaxiom checks. `/private/tmp/roth-separation-d28-compatibility.{lean,log,json}`. Owner build session `84237` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,124.05s/28.75s; source hash stable. `/private/tmp/roth-separation-d28-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.
