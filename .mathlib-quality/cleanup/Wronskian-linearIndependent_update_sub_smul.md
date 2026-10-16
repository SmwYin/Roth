# `Roth.linearIndependent_update_sub_smul` — declaration 12

Baseline: `8520ced`; source snapshot `/private/tmp/roth-wronskian-decl12-before.lean`.
Original inventory lines 207–217; worker-start lines 182–192; final lines 182–187.
Before: 11 declaration lines / 8 body lines. After: 6 / 3. Saved: 5 lines.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md in full. Also read the Lean 4 and
mathlib-quality skills, naming-conventions.md, mathlib-review-stages.md, applicable
style-rules.md sections, and the full worker contract.

## Full audit

1. **LINT:** no warnings in this declaration. Complete final file diagnostics contain
   only the existing header warning and the coefficient lemma's `hφ`/`hd` warnings.
2. **HAVE SCAN:** original L186 `hinv : ... := by ...` had proof content and one use,
   so not a mandatory inline; removed because Mathlib proves span invariance directly.
   Original L188 `hspan : ... := term` had no `by` and one use at L192: mandatory inline,
   superseded by the direct span equality rewrite. The `ψ` set binding was also removed.
3. **SET_OPTION:** none in original or final declaration; no limit changes.
4. **SIMP SQUEEZE:** original terminal `simp [ψ, Function.update_of_ne h]` was already
   appropriately unsqueezed; that inverse-operation subproof is now unnecessary. Final
   proof has no simp calls. Whole-proof `simpa` and `simpa only` alternatives were tested
   and rejected because span rewriting did not fire after scalar normalization.
5. **NAMING:** `linearIndependent` follows Mathlib's predicate spelling and
   `update_sub_smul` describes the actual operation. No forbidden abbreviation,
   numeric scheme, `_auxN`, or single-letter public identifier; no rename queued.
6. **LINE PACKING:** all three unchanged signature lines measured below; every break
   is justified using the complete next binder/conclusion token.
7. **BY PLACEMENT:** `by` remains at the end of the conclusion line.
8. **FORMAT:** two-space proof indentation, four-space signature indentation, no
   internal blank lines, no tactic semicolon chain, no `haveI`/`letI`. Rewrites merged.
9. **COMMENTS:** no inline proof comments originally; none deleted. Entire existing
   docstring and all file docstrings verified byte-identical.
10. **DOCSTRING:** existing statement/source context retained exactly as requested.
    It explains the column operation and its role in the cited construction of a basis.
11. **VISIBILITY:** public API preserved under the user's current-API instruction.
    The same-file consumer is `wronskian_ne_zero_of_linearIndependent` (the
    surrounding degree-reduction argument). Privatization/removal would alter API.
12. **STRUCTURE:** final body 3 lines, no conjunction, no branches, below every threshold.
13. **MATHLIB:** five-method results below. Span-preservation Mathlib API replaces the
    manual inverse update and two private helper calls. Generic independence theorem
    also compiled, but requires a longer function-conversion proof here.
14. **JUNK DEF:** n/a: theorem, no data definition introduced.
15. **EXISTS LEMMA:** n/a: no existential lemma or witness wrapper.
16. **SHOW vs CHANGE:** no `show` or `change` in source.
17. **PUSH_NEG:** no `push_neg` or negation tactic.
18. **GENERALISE:** all binders considered below; generic module version compiled in
    scratch. No changed public contract or speculative companion API added.
19. **INEQUALITY:** table below; no ordered inequalities in signature or proof.
20. **NORMAL-FORM:** `LinearIndependent K (Function.update ...)` is the intended
    polynomial-family operation. Mathlib's scalar form translates by `smul_eq_C_mul`;
    no new equivalent predicates or normalization lemmas required.
21. **SYNTAX-GEN:** OK for callers, which already construct a polynomial update of
    this form. Generic pointwise-addition spelling is less direct at that caller.
22. **IMPORT-FANOUT:** n/a: no new import or import edit.
23. **CASTS:** 0 dropped / 0 kept as cross-type / 0 load-bearing coercion ascriptions
    in the diff. `C c` is the existing polynomial embedding, translated by an API lemma.
24. **INSTANCE-NAME:** n/a: theorem, no instance introduced or renamed.

Issues found: manual span-preservation reconstruction and its single-use term binding.
Both fixed by the same Mathlib substitution. No source audit issue remains.
Refactoring needed: parent Phase 5a should remove the now-unused private
`span_range_update_sub_le` (already tracked from declaration 11); this worker did not
edit that helper. No rename/decomposition/generalization request remains pending.

## Line packing

Actual isolated `#check @Roth.linearIndependent_update_sub_smul` with
`set_option format.width 100`:

```lean
@Roth.linearIndependent_update_sub_smul : ∀ {K : Type u_1} [inst : Field K] {l : ℕ} {φ : Fin l → K[X]} {ν ν' : Fin l},
  ν ≠ ν' → ∀ (c : K), LinearIndependent K φ → LinearIndependent K (Function.update φ ν' (φ ν' - C c * φ ν))
```

The printer's first line includes its fully qualified name and implicit section binders;
source widths below are measured independently in Unicode codepoints.

| Signature line | Chars | Next syntactic unit | Arithmetic | Action |
|---|---:|---|---|---|
| 182 | 96 | `(hφ : LinearIndependent K φ)` (28) | 96 + 1 + 28 = 125 > 100 | ok |
| 183 | 34 | `LinearIndependent K (Function.update φ ν' (φ ν' - C c * φ ν)) := by` (67) | 34 + 1 + 67 = 102 > 100 | ok |
| 184 | 71 | proof body follows | n/a | ok |

No signature repack was needed. Final proof widths are 79, 43, 56.

## Inequality scan

| Occurrence | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| none | all signature lines, hypotheses, and proof | no `≥` or `>`; no ordered inequality | n/a | no `_ge_`/`_gt_` name |

The hypothesis `ν ≠ ν'` is disequality, not an oriented inequality.

## Five-method Mathlib search

| Method | Query / evidence | Result |
|---|---|---|
| A Lean-Finder | `linear independence preserved by subtracting a scalar multiple of another vector function update` | `linearIndependent_add_smul_iff`, `LinearIndependent.pair_add_smul_left_iff`, `LinearIndependent.pair_add_smul_right_iff` |
| B Loogle | `LinearIndependent, Function.update` | `LinearIndependent.update`, a general update theorem requiring a suitable linear combination |
| C LeanSearch | same natural-language problem | unavailable: inherited known HTTP 500 service failure; no repeated failing request, no absence claim |
| D source search | untruncated `rg` for `linearIndependent_update_sub_smul`, `update_smul`, `span_range_update_sub_smul`, `linearIndependent_iff_card_eq_finrank_span`; inspect exact source | span equality in `LinearAlgebra/Span/Defs.lean:652`, finite-rank criterion in `Dimension/OrzechProperty.lean:42`, generic add-scalar theorem in `LinearIndependent/Defs.lean:751` |
| E native local search | `span_range_update_sub_smul` | exact source hit `Submodule.span_range_update_sub_smul`; index unavailable, so not interpreted as an exhaustive negative index result |

Auxiliary variants: `LinearIndependent.update`, pair left/right update results,
`span_range_update_add_smul`, and `linearIndependent_add_smul_iff`.
Common-equivalents table: no discrete/finite/separation/boundedness bucket applies.
Every new source identifier was found in local source and compiled in an isolated example.

Concluded: Mathlib supplies span preservation directly, and a generic independence
statement in pointwise-addition form. Use its span theorem in this existing public API.
The six strict replacement rules were considered: this is not a new wrapper, and the
user's explicit public-API preservation instruction controls retention of the existing
public declaration. Delete the now-unused private span wrapper in Phase 5a. No custom
predicate, duplicated definition, or unverified absence claim was introduced. Module-doc
changes are outside this worker's source ownership and existing docs remain protected.

## Generalisation status

| Binder | Kind | Mechanical candidates / drop test | Result / disposition |
|---|---|---|---|
| `{K : Type*}` | type variable | universe poly; drop | already universe-polymorphic; scalar and polynomial types require K |
| `[Field K]` | typeclass | drop; Field→DivisionRing; Field→CommRing/Ring with module restatement | fully generic Ring/module/index proof compiled cleanly, subsuming division-ring and commutative-ring cases; bare drop loses polynomial/module structure; public abstraction/signature unchanged |
| `{l : ℕ}` | index-size value | drop; arbitrary index | l occurs in Fin l; arbitrary index compiled in generic scratch theorem; source kept for current API |
| `{φ : Fin l → K[X]}` | family | drop; arbitrary module family | φ occurs in both premise and conclusion; arbitrary module family compiled in scratch |
| `{ν ν' : Fin l}` | indices | drop either; arbitrary index type | both indices occur in operation; arbitrary index compiled with DecidableEq |
| `h : ν ≠ ν'` | proposition | remove; strict→weak / point-localize | actual deletion probe fails at unknown h and leaves span goal; mathematically necessary: with equal indices and c=1 a nonzero vector is replaced by zero; no strict/global property to weaken |
| `c : K` | scalar value | drop | scalar occurs in conclusion and is unrestricted; no positivity/nonzero assumption to weaken |
| `hφ : LinearIndependent K φ` | proposition | remove; unbundle | deletion probe fails at unknown hφ; zero family disproves conclusion without independence; not bundled or a pointwise/global property |
| decidability | inherited from Fin | explicit drop / classical alternative | no explicit decidability binder in public type; generic scratch requires DecidableEq for Function.update syntax |

The two hypothesis-deletion probes returned expected `Unknown identifier h` / `hφ`
errors, not a success claim; the server additionally reported stale imported artifacts
while the module rebuild was in progress. These are negative dependency tests only.
The positive generic proof returned `success=true`, `timed_out=false`, zero diagnostics:

```lean
example {R M ι : Type*} [Ring R] [AddCommGroup M] [Module R M] [DecidableEq ι]
    {φ : ι → M} {i j : ι} (h : i ≠ j) (c : R) (hφ : LinearIndependent R φ) :
    LinearIndependent R (Function.update φ j (φ j - c • φ i)) := by
  convert (linearIndependent_add_smul_iff (v := φ)
    (c := fun k ↦ if k = j then -c else 0) (i := i) (by simp [h])).mpr hφ using 1
  ext k
  by_cases hk : k = j <;> simp [hk, sub_eq_add_neg]
```

Inversion diagnostic: fires in the sense that polynomial structure disappears after
`← smul_eq_C_mul`; the existing generic Mathlib module theorem already provides that
abstract content. No new project abstraction is necessary. Current public API is kept
per the user's instruction; no further approval question or pending extension.

## Literature search status

A. Web search ran `linear independence elementary column operations modules generalization university`.
Top three returned hits: University of Hawaii's [Linear Independence module](https://descartes.manoa.hawaii.edu/ee345/modules/module-linind/),
University of Washington's [Linear Algebra notes](https://math.washington.edu/~smith/Teaching/308/308_notes.pdf),
and a Teachmint-hosted PDF (not relied on). The university sources connect independence
with pivots and elementary transformations.

A targeted query, `elementary matrices column operations invertible site:math.washington.edu`,
returned the Washington notes (two URL variants), then [Folland's Advanced Calculus notes](https://sites.math.washington.edu/~folland/AdvCalc24.pdf);
[Burke's matrix review](https://sites.math.washington.edu/~burke/crs/408/notes/Math408_W2020/308rev408-w20.pdf)
also explains elementary operations using invertible matrices. These support the familiar
invertible-operation interpretation; the general ring/module claim here is justified by
Mathlib's checked theorem and the compiled scratch proof, not inferred from a field-only textbook.
A separate Mathlib-doc search query returned no relevant web hits; local Mathlib source
and compiler are authoritative for the actual API.

B. ChatGPT math MCP: n/a, no matching connected callable tool exposed.
Literature-driven API proposals: none; the generic theorem already exists and current
polynomial API is preserved.

## Golfing rule pass (all 42 rules)

| Rule | Status |
|---|---|
| 1.1 by exact wrapper | n/a: final proof performs a rewrite before exact |
| 1.2 by rfl | n/a: no reflexivity wrapper |
| 1.3 rw + exact → rwa | considered; final exact applies the finrank criterion to hφ, not an unchanged assumption; tested whole simpa forms fail, retain explicit application |
| 1.4 simp + exact → simpa | tested unsqueezed and squeezed whole-proof alternatives; both leave updated span, rejected |
| 1.5 trailing rfl after simp | n/a: no trailing rfl |
| 1.6 constructor pair | n/a: no constructor goals |
| 1.7 apply + exact | n/a: no apply chain; direct `.mp hφ` used |
| 1.8 by_contra + push_neg | n/a: no contradiction proof |
| 1.9 eta reduction | n/a: no source lambdas |
| 1.10 inline single-use have | applied: hspan removed in favor of direct span theorem |
| 1.11 apply + intro | n/a: no quantified proof introduction |
| 1.12 redundant show | n/a: none |
| 1.13 have + projections | n/a: no conjunction/existential projection |
| 1.14 merge consecutive rw | applied: criterion, Set.finrank, scalar conversion and span update in one rw |
| 1.15 unsqueeze terminal simp only | n/a: original terminal simp already unsqueezed, now removed with inverse proof |
| 1.16 squeeze nonterminal simp | n/a: none |
| 1.17 dot notation | used for criterion `.mp hφ`; no additional shortening |
| 1.18 `<|` over parentheses | n/a: no nested application needing it |
| 1.19 push_neg replacement | n/a: none |
| 1.20 inline trivial existential helper | n/a: no existential helper |
| 2.1 grind | actual native trial failed to prove the whole independence goal |
| 2.2 remove before grind | n/a: no retained grind |
| 2.3 simpa consolidation | actual two variants failed to rewrite updated span; rw version compiled |
| 2.4 fun_prop | n/a: linear independence is not a continuity/measurability/differentiability property |
| 2.5 positivity | n/a: no positivity or arithmetic nonzero goal |
| 2.6 gcongr | n/a: no monotone inequality goal |
| 2.7 lia/omega | n/a: independence and span dimension identity, not integer arithmetic |
| 2.8 aesop | actual trial exhausted search without closing independence goal |
| 2.9 norm_num/norm_cast | n/a: no concrete numeric computation or cast goal |
| 2.10 decide/kernel | n/a: independence of an arbitrary polynomial family is not finite decidable computation |
| 2.11 field_simp/ring | n/a: no denominator identity; inverse algebra eliminated by API |
| 2.12 linear_combination | n/a: no ring/ring_nf ending or scalar equation goal |
| 2.13 wlog | n/a: no symmetric case branches |
| 2.14 collapse calc | n/a: no calc |
| 2.15 `<;>` multiple goals | n/a: selected proof creates no parallel goals; generic scratch used this appropriately |
| 3.1 erw→rw | n/a: no erw; rw works |
| 3.2 continuity/measurability | n/a: neither tactic present |
| 3.3 omega→lia | n/a: no arithmetic tactic |
| 3.4 rcases with rfl | n/a: no case decomposition |
| 3.5 automation attributes | n/a: specialized update theorem, no new canonical simp orientation/attribute justified |
| 3.6 simp_all unsqueeze | actual simp_all trial left independence unsolved; none retained |
| 3.7 remove limits | n/a: no source heartbeat/recursion option |

## Actual experiments and step-back reflection

Native `lean_multi_attempt` tried grind, simp_all, aesop, exact?, apply?, simpa, and the
ordered rw proof at original L185. grind failed; simp_all and aesop left the target;
exact? and apply? reached the default 200000-heartbeat limit. The line-based tool also
re-elaborated the old tail: missing ψ and no-goals/continuation parsing messages from
that tail are not evidence against the standalone rw proof. It was therefore checked
in isolation and then in the actual edited file. No search tactic or limit tweak ships.

Bounded fallback `lean_run_code` verified the ordered rw proof and generic independence
proof together; both compiled. The generic trial initially had redundant `congr 1` and
`Function.update_apply`, which were removed in the final independently compiled generic
probe. Scratch-only long-line warnings were absent from the final generic probe.

The selected strategy uses the same mathematical finite-span criterion as the original,
but obtains span invariance from Mathlib in one step. It avoids both manual inverse
updates and function extensionality. A single simpa was tried, not assumed to work.
Term-mode would require packaging transport and obscure the ordered rewrites, so the
three-line tactic proof is retained. No redundant final step remains.

## Verification and gates

- Complete native `lean_diagnostic_messages` after the final patch: success=true,
  partial=false, timed_out=false, no failed dependencies, zero errors; only three
  pre-existing warnings outside the target.
- `/Users/ramin/.elan/bin/lake build Roth.Wronskian`: exit 0, 1826 jobs.
  Log: `/private/tmp/roth-wronskian-decl12-module.log`.
- Native `lean_verify`: axioms exactly propext, Classical.choice, Quot.sound;
  trust=standard, non_standard_axioms=[], warnings=[].
- Isolated exact final proof compiled before source edit; final type/axiom probe below.
- Script compared against worker-start snapshot: signature byte-identical; all docstrings
  byte-identical; declaration 11→6 lines; no forbidden syntax in target.
- `git diff --check`: exit 0. Diff: 3 inserted / 8 removed lines, only target body changed.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | actual module build exit 0, 1826 jobs |
| definition_protected | pass | no def/abbrev changes |
| theorem_statement_protected | pass | complete signature byte-identical |
| structure_gate | pass | 3 body lines; no ∧ or branches |
| naming_gate | pass | descriptive predicate/operation name, no forbidden pattern |
| line_packing_gate | pass | all three signature lines and arithmetic above |
| inequality_orientation_gate | pass | full occurrence table; zero ≥/> |
| proof trust | pass | only standard three axioms, no suspicious source matches |
| comments/docstrings | pass | existing docstrings byte-identical; no proof comments existed |

Overall: pass. Parent owns dependent full-project and LeanEval checks and publication.
Source frozen after all source audits and successful module/LSP/axiom checks; no source
edits allowed after that notification. Report-only work continued afterward.

## Required phase checklist

- [x] Step 1: full mandatory references read.
- [x] Step 2: all 24 audit items answered.
- [x] Step 2.5: five-method search status and strict-rule dispositions.
- [x] Step 2.6: every binder/generalisation, inversion and literature search considered.
- [x] Step 2.7: complete measured per-line width table.
- [x] Step 2.8: complete inequality occurrence table.
- [x] Step 3: all 42 golfing rules with concrete statuses.
- [x] Step 4: whole-proof and alternative-strategy reflection plus actual trials.
- [x] Step 5a: complete successful final LSP diagnostics.
- [x] Step 5b: actual module build, trust and diff gates passed.
- [x] Step 6a: no rename required or queued.

Renames queued: none. Comments preserved: no inline comments originally; existing
API documentation retained. Sole cross-declaration action is the already-tracked
private span helper removal; this public declaration's audit is complete.

Final post-build isolated `lean_run_code` also returned success=true, timed_out=false;
its only diagnostics were the requested `#check` and `#print axioms` information.
It checked the exact final three-line proof, printed the unchanged public type, and
again confirmed exactly propext, Classical.choice and Quot.sound.
