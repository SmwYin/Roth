# Cleanup: `Roth.some_mapDomain_add_single` (original d3)

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md in full, together with both skill
entrypoints and the installed Phase-4 command. Single private declaration scope;
all Git and shared progress belong to the owner. This initial audit predates source edits.

## Baseline and scope

Owner confirms published baseline e112272: actual module, full project and separate
LeanEval pass. Native unfiltered baseline diagnostics are complete, success=true,
partial=false, timed_out=false, failed_dependencies=[], with 0 errors and 32 existing
warnings. No target warning. Original target is current L57–60; two proof-body lines.
Private target already omits Fintype and DecidableEq; it has two uses, in the public
`coeff_coeffNone` and `coeff_rename_mul_aeval`. All public contracts/docstrings protected.
No public omission proposal is applied. No other declaration cleanup is authorised.

## Full 24-item initial audit

| # | Item | Concrete result/action |
|---|---|---|
| 1 | LINT | No warning in L56–60; 32 existing file warnings recorded unfiltered. |
| 2 | HAVE SCAN | n/a: no have of any kind. |
| 3 | SET_OPTION | None in target; none added. |
| 4 | SIMP SQUEEZE | Sole simp is terminal, already unsqueezed; preserve terminal convention. |
| 5 | NAMING | Mathematical operations some/mapDomain/add/single describe result; no forbidden abbreviation or number scheme. Delete wrapper if direct generic API route verifies; no rename. |
| 6 | LINE PACKING | Both signature lines measured below; deleted target needs no repacking. |
| 7 | BY PLACEMENT | by ends conclusion line. |
| 8 | FORMAT | Two-space tactic indent; no internal blank line, haveI, letI or sequential rw. |
| 9 | COMMENTS | No target inline comments; preserve all module/caller comments byte-for-byte. |
| 10 | DOCSTRING | Private helper appropriately has none; no documentation edit. |
| 11 | VISIBILITY | Already private with only two local uses; no export/API change. |
| 12 | STRUCTURE | Two-line equality proof, no conjunction/branch, no extraction needed. |
| 13 | MATHLIB | Five actual native/source searches find generic some restriction/embedding API; verify direct composition then remove redundant private wrapper. |
| 14 | JUNK DEF | n/a: lemma, no data definition. |
| 15 | EXISTS LEMMA | n/a: equality, not existential. |
| 16 | SHOW/CHANGE | n/a: neither occurs. |
| 17 | PUSH_NEG | n/a: none. |
| 18 | GENERALISE | Every binder audited below; generic AddCommMonoid coefficient version compiled. Private literature exemption applies explicitly. |
| 19 | INEQUALITY | Zero inequalities; table below. |
| 20 | NORMAL-FORM | Restriction cancels extension; RHS original d is canonical. |
| 21 | SYNTAX-GEN | Generic embDomain API applies to all Zero coefficient types; mapDomain requires AddCommMonoid. Direct specialised API avoids local wrapper. |
| 22 | IMPORT-FANOUT | n/a: no added import. |
| 23 | CASTS | No target coercion/ascription; only explicit library embeddings may be needed in candidate rewrites. |
| 24 | INSTANCE-NAME | n/a: no instance declaration. |

Issues to fix: remove this private wrapper and exactly its two uses if the direct
library rewrites compile. No separate refactoring, rename or decomposition flag.

## Generalisation: every effective binder

| Binder | Class | Candidate/drop analysis | Result |
|---|---|---|---|
| `{τ : Type*}` | type variable | Already universe-polymorphic; dropping explicit type under autoImplicit=false makes dependent domain unknown; Sort cannot serve as Finsupp index. | Keep domain. |
| `(d : τ →₀ ℕ)` | structure value | Subject of equality; drop leaves unknown d. Generalise ℕ to arbitrary AddCommMonoid M. | Generic version actually compiled independently. |
| `(ν : ℕ)` | structure value | Singleton coefficient; drop leaves unknown ν. Generalise together with d to ν : M. | Same generic compilation succeeds. |
| `[Fintype τ]`, `[DecidableEq τ]` | section instances | Already omitted before target and absent from effective type. | No extra drop required. |
| `{R}`, `[CommSemiring R]` | section variables | Do not enter effective target type at all. | No target class assumption to weaken. |

No proposition hypotheses, strict bounds, continuity/localisation or bundled assumptions.
Initial drop rows above describe syntactic necessity. Subsequent native drop-tests actually
removed τ, d and ν individually under autoImplicit=false; all three are rejected with
the respective unknown identifier (raw d03-drop-tests.json). These intentional invalid
scratch probes are not proof certificates; error-recovery `sorry` text in diagnostics is
not source. Positive generic proof uses existing mathlib API; no new abstract declaration
is added. Inversion check:
Option.some is the concrete embedding; existing generic extension API already abstracts it.
Literature search n/a: private helper, as permitted by Phase4 item18. No public restatement.

## Inequality scan

| Location | Original | Rewrite | Rename |
|---|---|---|---|
| Entire original signature and every binder | n/a: zero ≥/> occurrence | none | none |

## Five actual searches

Full tool schemas discovered in ALL_TOOLS before native calls. Raw files:
`/private/tmp/roth-separation-d03-{finder,loogle,search,local}.json`.

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | Finsupp restricting to some after mapping domain Option.some and adding singleton none gives original finitely supported function | some_embDomain_some, some_optionElim, optionElim_some, optionEquiv_symm_apply. |
| B Loogle | `"Finsupp.some", "Finsupp.mapDomain"` | No items, no error; not an absence claim. |
| C LeanSearch | Finsupp some of mapDomain some plus single none equals original | mapDomain, mapDomain_add/sum/single and sum_mapDomain_index_addMonoidHom. |
| D Source | some_add/some_map/some_single/embDomain/mapDomain in Data/Finsupp/Option; embDomain_eq_mapDomain in Basic | some_add L69, some_single_none L78, some_embDomain_some L89; Basic L422 bridge. |
| E Name pattern | some_, limit40 | Finsupp.some_add, some_zero, some_apply and target among presence hits; index unavailable, so no absence inference. |

Auxiliary variants: some_optionElim, optionElim_some, some_single_some,
embDomain_some_some; Function.Embedding.some_apply bridges the embedding coercion.
Common-equivalents table: no specialised bucket. Found composition of existing generic
mathlib APIs; action is deletion and direct specialisation at exactly two uses. No claim
that a single exact named theorem is absent. Module-doc usage note not added: existing
docstrings are protected by session scope; API names documented in this report.

## Line packing

Width-100 independent `#check @D03.original`:

```lean
@original : ∀ {τ : Type u_2} (d : τ →₀ ℕ) (ν : ℕ), (Finsupp.mapDomain some d + Finsupp.single none ν).some = d
```

Lean prints this type as one unbreakable declaration display even with format.width100;
repository source measurements below are codepoints, not UTF8 bytes.

| Original signature line | Codepoints | Next whole mathematical token | Arithmetic | Action |
|---|---:|---|---|---|
| L57 | 62 | `Finsupp.some (d.mapDomain some + Finsupp.single none ν) = d := by` (65) | 62+1+65=128 >100 | justified break |
| L58 | 69 | none: proof body next | n/a | ok |
| Final target | n/a: deleted | none | n/a | ok |

Original body widths7/91. Final changed caller lines92–94 widths91/72/66;
lines140–142 widths84/72/66. Each next rewrite lemma would exceed100, accounting
for commas and the existing open list; caller signatures unchanged. No signature
packing churn was introduced outside the owned declaration.

## All42 golfing rules

Native live multi_attempt at original L59 tried the whole replacement of `ext j`.
Bare grind failed; bare simp/aesop left the mapDomain restriction goal. The library
simp with both embedding bridge hints closed immediately (the following original
L60 simp then reported no goals). Independent run_code certifies the complete
two-hint proof and generic coefficient version without a trailing tactic.

| Rule | Concrete result |
|---|---|
| 1.1 by exact | n/a: no wrapper. |
| 1.2 by rfl | n/a: no rfl target proof. |
| 1.3 rw+exact | n/a: neither original tactic is rw/exact. |
| 1.4 simp+exact | n/a: original simp terminal. |
| 1.5 trailing rfl | n/a: none in target; existing caller rfl unchanged. |
| 1.6 constructor pairs | n/a: equality, no constructor. |
| 1.7 apply+exact | n/a: neither occurs. |
| 1.8 by_contra+push_neg | n/a: neither occurs. |
| 1.9 eta reduction | n/a: no target lambda. |
| 1.10 inline have | n/a: no have. |
| 1.11 apply+intro | n/a: no such sequence. |
| 1.12 redundant show | n/a: no show. |
| 1.13 have+projections | n/a: no have/projection. |
| 1.14 merge rw | n/a: no original rw; direct caller rewrites merged into existing lists. |
| 1.15 terminal simp only | n/a: original simp already unsqueezed. |
| 1.16 nonterminal simp | n/a: original simp closes; replacement nonterminal simp_rw is explicitly bounded. |
| 1.17 dot notation | some method spelling does not improve an equality rewrite list. No receiver application to change. |
| 1.18 trailing parentheses | n/a: no parenthesised tactic/lambda argument. |
| 1.19 push_neg migration | n/a: none. |
| 1.20 existential helper | n/a: no existential. General wrapper deletion separately applied. |
| 2.1 grind | Actually tried live; failed on restriction of mapDomain. |
| 2.2 delete before grind | n/a: no successful grind sequence. |
| 2.3 simpa consolidation | No closing tactic after original simp. Independent two-hint simp succeeds; use direct bounded rewrites in nonterminal caller context. |
| 2.4 fun_prop | n/a: no analytic function property. |
| 2.5 positivity | n/a: equality, no ordered/nonzero conclusion. |
| 2.6 gcongr | n/a: no comparison or monotonicity. |
| 2.7 lia/omega | n/a: equality needs Finsupp API, not arithmetic; no arithmetic hypotheses. |
| 2.8 aesop | Actually tried live; exhaustive search left mapDomain restriction goal. |
| 2.9 norm_num/norm_cast | n/a: symbolic Finsupp with no concrete arithmetic/casts. |
| 2.10 decide/kernel | n/a: arbitrary τ and arbitrary Finsupp, no closed finite computation. |
| 2.11 field_simp/ring | n/a: no division/ring-polynomial identity. |
| 2.12 linear_combination | n/a: no ring/ring_nf ending or ring hypotheses. |
| 2.13 wlog | n/a: no case split. |
| 2.14 collapse calc | n/a: no calc. |
| 2.15 parallel goals | n/a: one extensional equality, no repeated branch. |
| 3.1 erw→rw | n/a: no erw. |
| 3.2 analytic tactic upgrade | n/a: neither legacy tactic. |
| 3.3 omega→lia | n/a: no target arithmetic tactic; other declarations outside target remain untouched. |
| 3.4 rcases rfl | n/a: no rcases. |
| 3.5 automation attributes | Existing library some lemmas already simp; no local/global attribute needed after wrapper deletion. |
| 3.6 simp_all | n/a: no hypotheses or simp_all only. |
| 3.7 heartbeat option | n/a: none in target, none added. |

Step-back reflection: restriction distributes over addition, kills the none singleton,
and cancels extension along some. This is existing generic library API. The only
representation detail is converting Option.some to its bundled embedding, via
Function.Embedding.some_apply; merely supplying embDomain_eq_mapDomain does not
match that opaque coercion. Retaining a private two-hint simp wrapper would hide this
existing API. Two explicit caller rewrite lists keep each nonterminal proof bounded
and remove a declaration. No missing API, duplicated proof block or extraction flag.

## Applied result and scoped holistic review

Deleted target plus its scoped omit (6 source lines) and replaced exactly two uses:
`coeff_coeffNone` and `coeff_rename_mul_aeval`. All other proof text, public
statements, definitions, docs and imports are unchanged. Source 614→611 lines, delta−3.
Before/after snapshot diff: `/private/tmp/roth-separation-d03-diff.patch`.

Builtin simplify is not exposed in this worker session. Scoped holistic review was
performed directly, disclosed here rather than claiming a tool invocation: checked
reuse, caller applicability, proof duplication and imports. Outcome
ISSUES-FOUND-AND-FIXED: wrapper removed through library composition. No further
issue within scope. No separate rename, follow-up extraction or generalisation.

## Verification

Actual module build `lake build Roth.Separation` exit0 (session91161), 1876 jobs;
raw `/private/tmp/roth-separation-d03-module.log`. Final native unfiltered diagnostic
request is complete: success=true, partial=false, timed_out=false,
failed_dependencies=[], 0errors and32 existing warnings; raw
`/private/tmp/roth-separation-d03-lsp.json`. No target/caller new warning.

Independent `D03.original` reproduces exact effective ORIGINAL type and proof without
importing/referring to Roth.Separation. The same successful native request compiles
`D03.generic` over AddCommMonoid coefficients and the exact direct rw replacement.
Both named proofs have only propext, Classical.choice, Quot.sound; raw
`/private/tmp/roth-separation-d03-independent.json`.

Discarded probes are not certificates: initial multi_attempt accidentally targeted
blank L61 (unexpected identifier); corrected live test targeted L59. Initial independent
probe used unknown pp.width; corrected option is format.width. Bare embDomain
conversion fails because Function.Embedding.some_apply is required. Those failures
were confined to native scratch experiments, no source or axiom contamination.

Actual module axiom verification imports freshly built Roth.Separation, resolves names
from the environment including private numeric components, and calls Lean.collectAxioms.
All eight retained actual private declarations pass with only propext, Classical.choice,
Quot.sound: mapDomain_add_single_none, coeff_X_none_pow_mul_rename,
degreeOf_none_rename_some, degreeOf_aeval_X_none_of_ne, rename_some_ne_zero,
aeval_X_none_ne_zero, map_aeval_X_none and degreeOf_map_intCast. Both actual changed
public callers pass the same check. Raw d03-actual-axioms.json and
d03-remaining-private-axioms.json under /private/tmp/roth-separation- prefix. One long-line
warning belongs only to the scratch verification list, not repository source.

Block-comment extraction comparison against pre-worker snapshot is byte-identical;
focused difflib patch confirms only target removal and its two uses were edited.
No def/abbrev, retained signature, import, documentation or unrelated proof changed.
No new sorry, custom axiom, native_decide, heartbeat/recursion limit, haveI/letI,
attribute or profiling scaffolding. No target-name occurrence remains in source.

## Gates

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | actual lake build Roth.Separation, session91161 exit0 |
| definition_protected | pass | focused diff has no definition change |
| theorem_statement_protected | pass: authorised private removal | removed only owned private target; both public signatures byte-identical |
| structure_gate | pass | original two-line proof removed; no new helper or long branch |
| naming_gate | pass | mathematical operation name, no forbidden pattern; deletion requires no rename |
| line_packing_gate | pass | every original signature line table above; changed source max91 |
| inequality_orientation_gate | pass | zero occurrence table above |
| comments/docs | pass | all block comments byte-identical |
| trust/limits | pass | actual retained-private and changed-public axioms standard-only; no options/axioms/sorries added |
| cumulative/full project/LeanEval | owner gate | owner runs sequential independent gates after source freeze |

## Buzz pass: FAST-BOARD (target removed), budget1000ms

Actual pre-edit repository profile supplied by owner:
`/private/tmp/roth-separation-d02-actual-profile.log` and its json. Target body was
unchanged since original. Anchored outer Elab.command7.362ms + proof Elab.async20.680ms
=28.042ms, below budget and below borderline750ms. The declaration is deleted, so
there is no final target elaboration cost and no fictitious zero-valued target timing.

Final actual repository-module command, session53646 exit0:

```text
lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Separation.lean
```

Raw `/private/tmp/roth-separation-d03-final-profile.log` plus parsed `.json` contain
actual source-command/proof anchors. Changed callers are also below budget:

| Actual caller | Outer command ms | Async proof ms | Conservative sum ms |
|---|---:|---:|---:|
| coeff_coeffNone | 12.997 | 38.009 | 51.006 |
| coeff_rename_mul_aeval | 27.491 | 367.018 | 394.509 |

Nested proof/tactic times are not added twice; max outer command anchor plus outer
proof anchor is used, not file aggregate or extracted-copy timings. No source profiling
wrapper exists. No limit raise, slow target, decomposition deferral or performance
change beyond wrapper removal was needed. No claim about total project speedup.

## Frozen ownership and eleven-step checklist

Every Lean request, module build and profiler process completed before releasing source.
Frozen SHA256:
`0f24374fef7d2a0392679a8848e1ef5358fff49531082934a021ee6a50c2e622`.
ALL SOURCE OWNERSHIP explicitly revoked and returned to owner; this worker is report-only.
Owner owns original whole-file compatibility proof, sequential full build and separate
LeanEval gate, shared progress, exact-path commit and push before the next declaration.

- [x] Step1: both skills, installed command and all required references read before edit.
- [x] Step2: complete24-item initial audit written before source edit.
- [x] Step2.5: all five actual searches, auxiliary variants and common-equivalents lookup.
- [x] Step2.6: every effective binder, actual individual drop-tests, omitted section instances,
  positive generic coefficient proof, inversion check and explicit private literature exemption.
- [x] Step2.7: every original signature line measured in codepoints; width100 check output.
- [x] Step2.8: zero-occurrence inequality table.
- [x] Step3: all42 golfing rules, actual corrected live automation probes.
- [x] Step4: step-back reflection, library embedding alternative and direct caller reuse.
- [x] Step5a: complete unfiltered native diagnostics, saved raw.
- [x] Step5b: actual module build, focused diff/protection gates, exact original independent
  proof and all actual retained-private axiom checks.
- [x] Step6a: no rename required, no queue change.

Refactoring flags: none. Renames: none. Public omission proposals remain pending owner/user
approval and were not applied. Source614→611 (−3); target deleted, two uses updated.

## Owner cumulative publication gates

Owner90175exit0 (43.10s): whole ORIGINAL30 declarations independently re-proved in a separate namespace;all20 original public type/value recoveries and ALL28 actual retained standardaxiom checks pass. `/private/tmp/roth-separation-d03-compatibility.{lean,log,json}`. Owner94244 sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,124.01s/30.50s; before/after hashes equal the frozen SHA. Logs `...-full.log`, `...-leaneval.log`, `...-builds.json`. Owner original block-doc byte comparison/exact diff/whitespace pass. Exact-path commit and successful cleanup-branch push precede next declaration.
