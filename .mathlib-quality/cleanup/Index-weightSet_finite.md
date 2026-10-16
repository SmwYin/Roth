# `Roth.weightSet_finite` — single-declaration audit

Audited pre-deletion source: `Roth/Index.lean` lines 60–62, three declaration lines
plus `omit [DecidableEq σ] in`. Baseline HEAD supplied by owner: `b211d75`.
Source SHA256 at release:
`9ea21436746c9e155e485b0ae6ef6deb884e4391417044407c717cb2f6206f64`.

The worker made **no source changes**. Source authority was explicitly released to the
owner, who accepted the Phase 5a deletion and two caller replacements. This report audits
the helper before deletion; final deletion, builds, public-type recovery, project gates,
and profiling evidence belong to the owner's renewed verification. No rename is queued
for a wrapper selected for deletion.

Read: lean4 and mathlib-quality SKILL.md; full cleanup.md including the Phase 4 worker
contract; full golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, cleanup-gates.md; relevant style/naming rules. No delegation.

## Audit (24 items)

| # | Item | Concrete result/action |
|---|---|---|
| 1 | LINT | No diagnostics on target lines 59–62; complete target query returned success, no partial result, empty items. |
| 2 | HAVE SCAN | No `have` bindings in the one-term proof. |
| 3 | SET_OPTION | No declaration-scoped option. |
| 4 | SIMP SQUEEZE | No simp call. |
| 5 | NAMING | Descriptive finite-weight-set name; no forbidden abbreviation or numeric pattern. Select deletion rather than cosmetic rename; owner confirms no rename queue needed. |
| 6 | LINE PACKING | Both signature lines measured below; no repacking needed before deletion. |
| 7 | BY PLACEMENT | Term proof; no `by`. |
| 8 | FORMAT | Four-space signature continuation, two-space term indentation, no empty line inside. |
| 9 | COMMENTS | None in proof; none removed. |
| 10 | DOCSTRING | Private helper has none, correctly. No documentation changes authorized or made. |
| 11 | VISIBILITY | Correctly private; both callers in same file. |
| 12 | STRUCTURE | One term, no conjunction or branches; no extraction/decomposition warranted. |
| 13 | MATHLIB | Found finite-image API and automatic finite-set instance; recommend deleting wrapper and using Mathlib directly at two callers. |
| 14 | JUNK DEF | n/a: lemma, no data definition. |
| 15 | EXISTS LEMMA | n/a: conclusion is finiteness, not existential. |
| 16 | SHOW vs CHANGE | No `show` or `change`. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | Every binder probed below; no remaining safe weakening. Inversion identifies generic finite-image theorem already in Mathlib. |
| 19 | INEQUALITY | No inequality occurrence; table below. |
| 20 | NORMAL-FORM | `Set.Finite` of set image is the canonical form required by callers' `bddBelow` / `csInf_mem`. |
| 21 | SYNTAX-GEN | Direct finite-image term is usable at both callers without a wrapper or altered caller signatures. |
| 22 | IMPORT-FANOUT | n/a: no import added. |
| 23 | CASTS | Diff: 0 dropped / 0 cross-type / 0 load-bearing. Existing Finset-to-Set ascription expresses the image's set domain; no source change. |
| 24 | INSTANCE-NAME | n/a: not an instance declaration; no instance introduced. |

Issues found: redundant Mathlib wrapper. Worker fixes: none (cross-declaration Phase 5a
action reserved for owner). Refactoring needed: remove helper and replace both uses.

## Line packing

Actual `#check @` of the built private constant, emitted through `mkIdent` to retain
the numeric private-name component, at `format.width := 100`:

```lean
@Roth.weightSet_finite✝ : ∀ {σ : Type u_1} [inst : Fintype σ] (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ),
  (Roth.weight r '' ↑((MvPolynomial.taylor α) P).support).Finite
```

This final scratch query emitted an imports-out-of-date informational notice because the
owner had begun the accepted refactor; it is a pre-deletion artifact check, not a final
post-deletion gate. The previous constant/axiom enumeration and module build were completed
before source release.

| Sig line | Characters | Next signature unit | Arithmetic | Action |
|---|---:|---|---|---|
| 60 | 79 | Complete conclusion with `:=`, 61 characters excluding indentation | 79 + 1 + 61 = 141 > 100 | ok |
| 61 | 65 | None: proof term follows | n/a, last signature line | ok |

The conclusion is a single parenthesized image expression ending in `.Finite`; moving
only `(weight` would split that expression rather than pack a complete signature unit.

## Inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 1 | Entire signature/hypotheses | n/a — no `≥` or `>` | none | no `_ge_` or `_gt_` in name |

## Mathlib search status (five actual searches)

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | `The image of a finite set under any function is finite` (3 results) | `Set.Finite.image`, `Set.Finite.map`, finite replacement instance. |
| B Loogle | `Set.Finite, Set.image` (5 results) | `Set.Finite.image`, `Set.Finite.of_finite_image`, `Set.finite_image_iff`. |
| C LeanSearch | `the image of a finset as a set is finite` (3 results) | `Finite.Set.finite_image`, `Set.fintypeMap`, finite replacement instance. |
| D Mathlib source rg | `theorem (finite_toSet|finite_toSet_image)`, `theorem Finite.image`, `lemma Finite.image`, `theorem finite_image` in Data/Set and Data/Finset | `Data/Set/Finite/Basic.lean:363` Finset.finite_toSet, :568 Set.Finite.image, :684 finite_image_iff. Untruncated results. |
| E Local name pattern | `finite_toSet` (5 results), then `Set.toFinite` (3 results) | Both exact declarations found; index was warming, so no absence inference. |

All remote tools returned non-error results; no remote unavailability was interpreted
as absence. Auxiliary variants considered: `Finite.of_finite_image`, `finite_image_iff`,
`Finite.map`, `finite_toSet_toFinset`, and generic `Set.toFinite`. Common-equivalents
table: finite-set bucket relevant; finite-image API is the exact generic mechanism.

Compiled `exact?` and `apply?` both suggest
`Set.toFinite (weight r '' ↑((taylor α) P).support)`. `#check` verified
`Finset.finite_toSet`, `Set.Finite.image`, and `Set.toFinite` in current imports.
No absence claim is made. Conclusion: **found in Mathlib more generally; delete local
wrapper and specialize Mathlib directly at its two callers**. Module docstring remains
protected by task scope; usage is documented here.

## Generalisation status — every binder

Actual isolated `lean_run_code` probes used `import Roth.Index`; all failures below are
intentional probes and did not modify the target file.

| Binder | Class / use | Candidates actually probed | Result |
|---|---|---|---|
| `{σ : Type*}` | Type variable; polynomial/function/Finsupp domain | Drop under `autoImplicit false`; universe already polymorphic | Fails unknown `σ`; retain universe-polymorphic parameter. |
| `[Fintype σ]` | Typeclass; required to form `weight r` | Drop; replace with `[Finite σ]` | Both fail synthesis of `Fintype σ` in statement. No weaker parent supports unchanged `weight`. |
| `[DecidableEq σ]` | Ambient decidability, omitted from helper | Independent reproof with no DecidableEq binder | Compiles. Already correctly omitted; no new action. |
| `P` | Structure value; Taylor support | Drop under `autoImplicit false` | Fails unknown `P`; needed in conclusion. No proposition to point-localise/weaken. |
| `α` | Function value; Taylor center | Drop under `autoImplicit false` | Fails unknown `α`; needed in conclusion. No regularity/strictness hypothesis. |
| `r` | Function value; weight | Drop under `autoImplicit false` | Fails unknown `r`; needed in conclusion. No positivity assumption to weaken. |

Inversion check: proof never uses any Taylor- or weight-specific fact; it works for
every finite set and function, exactly `Set.Finite.image`. No new abstract helper is
needed. Private literature search: n/a, private declaration scope exemption.
Big-change candidates: none; deleting the private wrapper needs two proof-body caller
edits, with no public contract change.

## Golfing-rule pass (all 42 rules)

| Rule | Status |
|---|---|
| 1.1 by exact | n/a: already term proof. |
| 1.2 by rfl | n/a: no reflexivity wrapper. |
| 1.3 rw + exact | n/a: no rewrites. |
| 1.4 simp + exact | n/a: no simp. |
| 1.5 trailing rfl | n/a: no simp/rfl chain. |
| 1.6 constructor | n/a: no product/conjunction. |
| 1.7 apply + exact | n/a: direct term already. |
| 1.8 by_contra! | n/a: no contradiction proof. |
| 1.9 eta reduction | n/a: no lambda. |
| 1.10 single-use have | n/a: no have. |
| 1.11 refine + fun | n/a: no apply/intro. |
| 1.12 redundant show | n/a: no show. |
| 1.13 obtain | n/a: no projections from local facts. |
| 1.14 merged rw | n/a: no rw. |
| 1.15 terminal simp | n/a: no simp only. |
| 1.16 nonterminal simp | n/a: no simp. |
| 1.17 dot notation | Already `.image _`; direct caller proposal also uses `.finite_toSet.image`. |
| 1.18 `<|` | n/a: nested finite proof is receiver of dot notation, not trailing callback. |
| 1.19 push Not | n/a: no negation tactic. |
| 1.20 existential inline | n/a: not existential. |
| 2.1 grind | Actually tried whole goal; failed with negated finiteness hypothesis and False target. |
| 2.2 remove before grind | n/a: no preceding tactics or grind in source. |
| 2.3 simpa | n/a: no simp/closing chain. |
| 2.4 fun_prop | n/a: goal is finiteness, no function regularity property. |
| 2.5 positivity | n/a: no order/nonzero goal. |
| 2.6 gcongr | n/a: no inequality/congruence. |
| 2.7 lia/omega | n/a: no Nat/Int arithmetic proposition. |
| 2.8 aesop | Actually tried whole goal; failed, made no progress. |
| 2.9 norm_num/norm_cast | n/a: no numeric/cast equality. |
| 2.10 decide | n/a: symbolic Set.Finite proposition, no finite computational decision problem. |
| 2.11 field_simp/ring | n/a: no algebraic identity. |
| 2.12 linear_combination | n/a: no ring-ending proof/hypotheses. |
| 2.13 wlog | n/a: no symmetric case split. |
| 2.14 calc | n/a: no calc chain. |
| 2.15 `<;>` | n/a: single goal and term. |
| 3.1 erw | n/a: no rewrites. |
| 3.2 continuity | n/a: no regularity tactics. |
| 3.3 omega→lia | n/a: no arithmetic tactic. |
| 3.4 rcases rfl | n/a: no cases/substitution. |
| 3.5 attributes | n/a: wrapper selected for deletion; no new automation API. |
| 3.6 simp_all | n/a: no simp_all. |
| 3.7 heartbeat option | n/a: none present. |

Step-back reflection: existing proof is already one composed term. Actual `exact?` and
`apply?` close via `Set.toFinite`; grind/aesop do not. A shorter wrapper proof would
retain the duplication. The proper change is the owner’s cross-declaration deletion.

## Compiled replacement proposal

Both callers compiled successfully in one `lean_run_code` probe with their original
conclusions, using the original support/evaluation equivalence re-proved locally and
the original nonempty proof re-established locally. Neither replacement used
`weightSet_finite` or the caller theorem itself.

```lean
-- index_le_weight proof body
csInf_le ((taylor α P).support.finite_toSet.image (weight r)).bddBelow
  (Set.mem_image_of_mem _ (Finset.mem_coe.2 (mem_support_taylor_iff.2 h)))

-- exists_weight_eq_index obtain step
obtain ⟨d, hd, hdw⟩ :=
  (weightSet_nonempty hP α r).csInf_mem ((taylor α P).support.finite_toSet.image (weight r))
```

Only scratch-local memSupport unused-instance lint warnings occurred; the probe had
success=true, timed_out=false. Owner applies these edits under its source authority.

## Verification and gates — worker pre-deletion state

Independent original-type reproof:
`(taylor α P).support.finite_toSet.image _`, with `{σ : Type*} [Fintype σ]` and no
DecidableEq. Compiles without using target; its axioms are exactly
`[propext, Classical.choice, Quot.sound]`.

Actual built private constant discovered by iterating imported environment constants:
`_private.Roth.Index.0.Roth.weightSet_finite`. `Lean.collectAxioms` returned exactly
`[propext, Classical.choice, Quot.sound]`. Numeric-name spelling via quoted `«0»`
was tried and failed to resolve; environment-name enumeration and `mkIdent` avoided
that parser/name mismatch and checked the real constant rather than a surrogate.

| Gate | Status | Evidence |
|---|---|---|
| lake_build_file | pass | Actual `lake build Roth.Index`, exec session 63141, exit 0; 1501 jobs successful. Existing unrelated warnings replayed. |
| definition_protected | pass | Worker source diff empty; no definition changed. |
| theorem_statement_protected | pass | Worker source diff empty; target and every public signature unchanged by worker. |
| structure_gate | pass | One-line body; no conjunction or branches. |
| naming_gate | pass | No forbidden patterns; owner-selected deletion makes rename unnecessary. |
| line_packing_gate | pass | Both signature rows and arithmetic above. |
| inequality_orientation_gate | pass | Zero reversed inequality occurrences; table above. |
| complete LSP | pass for pre-deletion state | Whole-file diagnostic tool returned success=true, partial=false, timed_out=false, failed_dependencies=[]; 28 existing warnings outside target. Final target query returned empty items, success=true, partial=false. |
| trust | pass | Actual built private constant and independent reproof use only the standard three axioms. |

Overall worker gates: pass, with accepted Phase 5a deletion handed to owner.
Whole-project build, final cumulative source gates, separate LeanEval and final profile
are owner responsibilities; not claimed here.

## Buzz / holistic status

No skill-invocation tool for built-in simplify/buzz is exposed. Manual holistic review
identified the redundant helper and produced the compiled deletion proposal above.
Actual anchored per-declaration profiling is reserved for the owner's final full-source
`lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Index.lean`.
No FAST-BOARD or target timing verdict is claimed from an aggregate profiler. No
heartbeat increases, profiling source scaffolding, or new axioms introduced.

## Result and 11-step checklist

Before: 3 declaration lines; after worker: 3; saved by worker: 0.
Accepted owner follow-up removes wrapper plus omit line and changes two proof bodies.
Comments-preserved: none present. Renames-queued: none. Compiler processes: all finished
at source release; subsequent scratch #check also finished before report completion.

- [✓] Step 1 — references read.
- [✓] Step 2 — all 24 audit answers recorded.
- [✓] Step 2.5 — five actual search methods and results recorded.
- [✓] Step 2.6 — every binder mechanically probed; private literature exemption recorded.
- [✓] Step 2.7 — every signature line measured, with arithmetic and width-100 check.
- [✓] Step 2.8 — inequality scan table recorded.
- [✓] Step 3 — all 42 golfing rules given concrete status.
- [✓] Step 4 — reflection and actual exact?/apply? trials complete.
- [✓] Step 5a — complete pre-deletion LSP; target diagnostic-clean.
- [✓] Step 5b — diff gates and actual module build recorded.
- [✓] Step 6a — no rename needed for wrapper selected for deletion.

Source authority released; report-only worker complete. Final owner evidence must
supersede the pre-deletion build/diagnostics after applying the accepted refactor.

## Owner amendment (reported after source release)

Owner applied helper deletion and both explicit finite-image caller replacements.
New source: 272 lines, 20 retained declarations, SHA256
`6897edb8955031680fa67e41007292a74287c1f0737f9dbcd5b44ca42e471ef7`.
Owner reports actual module-build session 45739 exited 0 and complete native LSP
success=true, partial=false, zero errors,27 inherited warnings. Owner's independent
whole-original reproof, all18 public type/value equalities and all20 retained actual
constant standard-axiom checks subsequently completed in90385, exit0;
`/private/tmp/roth-index-d03-compatibility.log`. Owner sequential full then separate
LeanEval7465 both exit0(143.50s/32.05s), frozen hash stable;
logs `/private/tmp/roth-index-d03-{full,leaneval}.log`. Original block docs are identical
and all source lines remain within100 codepoints. These are owner-observed post-deletion
facts, distinct from worker's directly observed pre-deletion evidence.
