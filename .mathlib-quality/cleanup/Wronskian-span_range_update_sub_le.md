# Declaration audit: `Roth.span_range_update_sub_le`

Worker: dedicated declaration 11. Baseline HEAD `64872e6`; original lines 192–201,
current baseline lines 172–181 (10 lines). Scope: this private declaration and this report.
Read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md,
cleanup-gates.md in full, plus relevant style/naming instructions and Lean skill.

## Full audit

1. **LINT:** none in target. Existing file copyright warning and unused `hφ`/`hd` elsewhere are unchanged.
2. **HAVE SCAN:** no `have`, `let`, or local instance in the target.
3. **SET_OPTION:** none; no limits introduced.
4. **SIMP SQUEEZE:** no original simp calls. Selected proof uses explicit `rw` followed by terminal `aesop`.
5. **NAMING:** `span_range_update_sub_le` is descriptive snake_case for span inclusion after subtraction update; no forbidden abbreviation, numeric scheme, `_ge_`, `_gt_`, or single-letter name. A standard property need not gain `_aux`. No rename.
6. **LINE PACKING:** all three signature lines checked below. Signature unchanged.
7. **BY PLACEMENT:** `by` ends the conclusion line.
8. **FORMAT:** two-space tactics, no internal blanks, one tactic per line. Old lambda `=>` disappears with case split; no new `haveI`/`letI`.
9. **COMMENTS:** zero target comments, none removed.
10. **DOCSTRING:** n/a: private helper, appropriately undocumented.
11. **VISIBILITY:** private, used twice inside one public caller; appropriate until Phase 5a removal.
12. **STRUCTURE:** original seven proof lines, selected two; no conjunction in statement, no long branch, no decomposition required.
13. **MATHLIB:** five searches below locate a direct replacement for the caller's span equality. Queue helper removal and direct Mathlib use in Phase 5a. Helper's unrestricted inclusion itself is not identical to Mathlib's equality under distinct indices.
14. **JUNK DEF:** n/a: lemma, not definition.
15. **EXISTS LEMMA:** n/a: conclusion is inclusion, not an existential.
16. **SHOW vs CHANGE:** neither occurs.
17. **PUSH_NEG:** absent.
18. **GENERALISE:** full table below; Ring and abstract module variants compiled in isolation, no signature change authorized or needed given queued removal.
19. **INEQUALITY:** one `≤`, no reversed inequalities; table below.
20. **NORMAL-FORM:** standard submodule inclusion; caller equality is already provided by Mathlib's scalar-action API.
21. **SYNTAX-GEN:** current callers need no restatement; use Mathlib directly during queued refactor.
22. **IMPORT-FANOUT:** n/a: no import changes.
23. **CASTS:** 0 dropped / 0 cross-type / 0 load-bearing casts in diff. `C` is the original polynomial constructor, not a new coercion.
24. **INSTANCE-NAME:** n/a: no instance declaration.

Issues found: manual update case split and obsolete lambda spelling. Both disappear in selected proof.
Refactoring needed: Phase 5a delete this helper after replacing the sole caller's two applications
(and inverse-update equality) by `Submodule.span_range_update_sub_smul`; concrete route compiled below.
No pending broadening request.

## Mathlib search status

| Method | Query | Result |
|---|---|---|
| A Lean-Finder | span of range after replacing vector by subtraction of scalar multiple | Found `Submodule.span_range_update_sub_smul`, additive variant, span insertion APIs. |
| B Loogle | `Submodule.span, Function.update` | Found both update-add and update-sub span equalities. |
| C LeanSearch | span range update subtract scalar multiple | HTTP 500; genuinely unavailable, not evidence of absence. |
| D source | `span.*update\|update.*span`; `forall_update` | `LinearAlgebra/Span/Defs.lean:640–654`; `Logic/Function/Basic.lean:687`. Full searches, no truncating filters. |
| E local names | `span_range_update` | Found two Mathlib declarations and local helper. Symbol index unavailable, source hits verified separately by compiled `#check`. |

Auxiliary variants searched: add/sub scalar updates, `Function.forall_update_iff`, span subset/monotonicity.
Common-equivalents table: no unrelated topology/finiteness bucket applies.
Whole-goal `exact?` failed; `apply?` returned only partial reductions (span monotonicity/span_le etc.),
not a completed proof. No claim of universal absence is made.
The relevant Mathlib replacement is present, verified by `#check` and this successful isolated example:

```lean
example {K : Type*} [Field K] {l : ℕ} (φ : Fin l → K[X]) {ν ν' : Fin l}
    (h : ν ≠ ν') (c : K) :
    Submodule.span K (Set.range (Function.update φ ν' (φ ν' - C c * φ ν))) =
      Submodule.span K (Set.range φ) := by
  simpa [smul_eq_C_mul] using Submodule.span_range_update_sub_smul h φ c
```

The parent accepted this concrete Phase 5a queue. No caller was edited by this worker.
The no-wrapper/delete-not-simplify rule is satisfied by that queued deletion, not by keeping a new wrapper.
No custom predicates or global decidability instances are introduced. Module-level Mathlib usage note
belongs to the same file-level replacement pass.

## Generalisation status

| Parameter | Class/use | Mechanical check | Result |
|---|---|---|---|
| `{K : Type*}` | Scalar type and polynomial coefficients | Already universe polymorphic; dropping loses carrier of statement | Keep; no narrower universe introduced. |
| `[Field K]` | Polynomial subtraction and scalar multiplication | Isolated replacements with `DivisionRing`, `CommRing`, `Ring`; drop instance; `Semiring` | First three compile. Dropping fails `Semiring K`; Semiring fails `HSub K[X] K[X]`. Keep source signature under scope; removal queued. |
| `{l : ℕ}` | Size of index type | Used in `Fin l`; arbitrary index tested in abstract module probe | Abstract variant compiles, no production API addition. |
| `(φ : Fin l → K[X])` | Family whose span is compared | Appears on both sides; arbitrary module-valued family tested | General module probe compiles; removing family destroys statement. |
| `(ν : Fin l)` | Source of scalar multiple | Occurs in updated vector | No proposition to weaken/drop; generic index probe compiles. |
| `(ν' : Fin l)` | Updated coordinate | Occurs in update and vector | No proposition to weaken/drop; generic index probe compiles. |
| `(c : K)` | Arbitrary scalar | Appears as `C c` in statement | Already arbitrary; dropping changes statement, no positivity/nonzero restriction exists. |

Inversion check: after rewriting `← smul_eq_C_mul`, the proof is purely about module spans.
A scratch theorem for `{R M ι : Type*} [Ring R] [AddCommGroup M] [Module R M] [DecidableEq ι]`
compiled using the same span/update rewrites and closure proof, with only standard axioms.
This verifies the abstraction rather than asserting it speculatively. It need not be added: the actual
caller already has a stronger equality in Mathlib, so deletion resolves the local specialization.
Point-localization/strict-to-weak/unbundling: no such hypotheses present.
Literature: n/a, private declaration. No external literature claim made.

## Line packing (codepoints)

Reference compiled `#check` of an isolated identically typed copy at `format.width 100` is included
in verification below. Signature chunks are complete application expressions, not pieces of identifiers.

| Sig line | Chars | Next complete expression chunk | Arithmetic | Action |
|---|---:|---|---|---|
| 172 | 82 | `Submodule.span K (Set.range (Function.update φ ν' (φ ν' - C c * φ ν)))` (70) | 82 + 1 + 70 = 153 > 100 | keep |
| 173 | 76 | `Submodule.span K (Set.range φ)` (30) | 76 + 1 + 30 = 107 > 100 | keep |
| 174 | 42 | no next signature line | n/a | keep |

## Inequality scan

| Location | Original | Rewrite | Rename |
|---|---|---|---|
| Statement line 173 | updated span `≤` original span | already smaller side left | none |
| Entire signature/hypotheses | zero `≥`, zero `>` | none | no `_ge_`/`_gt_` name |

## Golfing rules (all 42)

| Rule | Status |
|---|---|
| 1.1 by-exact | n/a: original multi-step proof, no wrapper. |
| 1.2 by-rfl | n/a: no reflexivity-only proof. |
| 1.3 rw/exact to rwa | Considered both old branches; replaced entire split by update iff and closure automation. |
| 1.4 simp/exact to simpa | n/a in target; successful simpa route verified for caller equality. |
| 1.5 trailing rfl | n/a: absent. |
| 1.6 anonymous constructor | Tried explicit pair after rewriting update iff; compiles, then shortened to aesop. |
| 1.7 apply/exact | n/a: absent. |
| 1.8 by_contra! | n/a: no contradiction proof. |
| 1.9 eta | Original lambda carries a goal, not an eta redex; disappears with rewrite. |
| 1.10 inline have | n/a: no haves. |
| 1.11 refine/fun | Original already uses refine/fun; update iff is shorter. |
| 1.12 show | n/a: absent. |
| 1.13 obtain | n/a: no have projections. |
| 1.14 merge rw | Applied new single rewrite chain normalizing span and update together. |
| 1.15 terminal simp | n/a: no retained simp. |
| 1.16 squeeze simp | n/a: no retained simp. |
| 1.17 dot notation | Original `.2`/membership methods appropriate; replaced by generic iff rewrites. |
| 1.18 parens | n/a: final tactics have no avoidable lambda parentheses. |
| 1.19 push Not | n/a: no push_neg. |
| 1.20 existential helper | n/a: no existential statement. |
| 2.1 grind | Whole proof failed. After normalization and supplied submodule closure lemmas also failed. |
| 2.2 delete before grind | n/a: grind not retained. |
| 2.3 simpa consolidation | Whole simp normalization left quantified membership, no complete simp proof; explicit update-iff approach selected. |
| 2.4 fun_prop | n/a: no analytic function property. |
| 2.5 positivity | n/a: submodule inclusion, not numeric positivity. |
| 2.6 gcongr | Tried, leaves unsupported containment of updated range in original range; rejected. |
| 2.7 lia/omega | n/a: no natural/integer arithmetic proposition. |
| 2.8 aesop | Whole goal failed; after four iff/scalar rewrites plain aesop succeeds. Selected. |
| 2.9 norm_num/norm_cast | n/a: no numeric computation/coercion goal. |
| 2.10 decide | n/a: arbitrary modules/spans not a finite closed computation. |
| 2.11 field_simp/ring | n/a: no denominator or ring identity. |
| 2.12 linear_combination | n/a: no ring terminal or algebraic equality. |
| 2.13 wlog | n/a: update-self/nonself are structurally different; generic forall_update eliminates both. |
| 2.14 calc | n/a: no calc. |
| 2.15 `<;>` | No sibling goals remain after closure automation, so redundant. |
| 3.1 erw | n/a: only rw. |
| 3.2 legacy function tactics | n/a: absent. |
| 3.3 omega | n/a: absent and no arithmetic. |
| 3.4 rfl substitution | Original correct; case split entirely eliminated. |
| 3.5 attributes | Do not register a private helper queued for removal as a global automation rule. |
| 3.6 simp_all | Actual normalized-goal attempt left conjunction of span memberships; not selected. |
| 3.7 limits | None present or added. |

## Step-back reflection and experiments

The key improvement is recognizing universal membership in an updated family as
`Function.forall_update_iff`, leaving standard submodule closure facts to aesop.
Explicit pair construction also compiles but is longer (four body lines versus two).
Aesop with three registered closure rules, then one, then no added rules all compiled;
the minimal plain form was selected. No unnecessary tactic preceding grind remains.
Initial native multi-attempt accidentally targeted comment line 183 and produced parse diagnostics;
these were discarded and the actual proof start at line 175 was retried. A first multi-rule aesop
experiment used incorrect syntax, then was corrected to bracketed rule syntax and compiled.
No experiment changed production source. No failed experiment is counted as a pass.

## Verification and gates

Final source installed and ownership relinquished immediately after verification.

- Actual module command: `/Users/ramin/.elan/bin/lake build Roth.Wronskian > /private/tmp/wronskian-decl11-build.log 2>&1`, session 16539, exit **0**.
- Native `lean_diagnostic_messages` over the whole file: `success=true`, `partial=false`, `timed_out=false`, no failed dependencies, no errors. Only existing copyright warning (line 1) and unused `hφ`/`hd` (127–128).
- Native `lean_run_code`: identically typed isolated proof using final two tactics compiled, `success=true`, `timed_out=false`. The tool noted imports were out of date while the module rebuild was running; that build subsequently exited 0. No proof diagnostic failed.
- Compiled `#check @probe` at width 100:

```lean
@probe : ∀ {K : Type u_1} [inst : Field K] {l : ℕ} (φ : Fin l → K[X]) (ν ν' : Fin l) (c : K),
  Submodule.span K (Set.range (Function.update φ ν' (φ ν' - C c * φ ν))) ≤ Submodule.span K (Set.range φ)
```

- Compiled `#print axioms probe`: `[propext, Classical.choice, Quot.sound]` only.
- Exact prefix comparison through `:= by`: signature byte-identical before/after.
- Codepoint lengths of all final declaration lines: **82, 76, 42, 91, 7**.
- No `sorry`, `admit`, custom axiom, `native_decide`, `set_option`, `haveI`, `letI`, `push_neg`, `≥`, or `>` in target. No comment, docstring, definition, import, version, or caller edit.
- Source frozen SHA256: `475dfef2e50a37a99af4680772230ee8ff5ef2fce781f805c0a291f1d44f7ce2`.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | PASS | Actual `lake build Roth.Wronskian` exit 0. |
| definition_protected | PASS | No def/abbrev touched. |
| theorem_statement_protected | PASS | Exact signature comparison true. |
| structure_gate | PASS | Two-line body; no conjunction statement or branches. |
| naming_gate | PASS | Descriptive standard-property name, no forbidden patterns; no rename queue. |
| line_packing_gate | PASS | All three signature rows measured above; all lines ≤100 codepoints. |
| inequality_orientation_gate | PASS | Only correctly oriented `≤`; no reversed relation. |
| comments_preserved | PASS | None present in target; none removed elsewhere. |
| no_proof_escape | PASS | Source scan clear and compiled isolated proof has only standard axioms. |
| cumulative_no_unintended_breakage | Worker scope PASS | Current complete file LSP and module pass; parent owns full-project and separate LeanEval build before checkpoint. |
| docstring_only_changes | n/a | Proof cleanup, not prose-only mode. |

Overall: **PASS**, with concrete Phase 5a helper-removal/caller-Mathlib replacement queued.

## Result

Before **10 lines**, after **5 lines**, saved **5 lines**. Proof body **7 → 2**.
Audit issues: 2 found, both fixed. One cross-declaration refactor queued, not an unresolved
proof gate. Applied rules: 1.14, 2.8 (and removal of obsolete lambda syntax).
Renames queued: none. Comments preserved: none present. No generalisation applied.

Phase checklist:
- [x] Step 1: required reference docs read.
- [x] Step 2: all 24 audit items reported.
- [x] Step 2.5: all five search methods attempted and actual availability recorded.
- [x] Step 2.6: all parameters/mechanical candidates, inversion, and private-literature scope recorded.
- [x] Step 2.7: all signature lines measured with codepoint arithmetic.
- [x] Step 2.8: per-occurrence inequality scan completed.
- [x] Step 3: all 42 rules assigned concrete statuses.
- [x] Step 4: alternative whole-proof tactics, direct API, and term/closure strategies tested and reflected on.
- [x] Step 5a: complete final-source LSP passed, no target diagnostics.
- [x] Step 5b: module build and all diff gates passed.
- [x] Step 6a: rename queue n/a; concrete non-rename Phase 5a action delivered to parent.

No source edits after freeze. Git and shared progress logs remain exclusively with parent.

