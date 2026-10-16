# Phase 4 — `Roth.weightSet_nonempty`

Scope: the single private declaration at `Roth/Index.lean:60–63` at dispatch
(`1a5750b`). Only its proof was edited. No other declaration, definition, documentation,
import, option, version, or public API was changed. The original snapshot is
`/private/tmp/roth-index-original.lean`. This report is the canonical worker artifact.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md in full. Also read both skills,
the full cleanup command including its verbatim Phase 4 contract, and the relevant
style/naming sections. Native Lean LSP tools were discovered through ALL_TOOLS and used.

Mathematics: translation preserves nonzeroness; a nonzero polynomial has nonempty
support, whose image under the weight function is nonempty. All these reductions are
already simp lemmas, so the final proof is `simpa using hP`.

## Full audit (24 items)

| # | Item | Concrete result |
|---|---|---|
| 1 | LINT | No warnings/errors in lines 59–63. Full initial/final LSP requests completed; 27 pre-existing warnings elsewhere remain with the file owner. |
| 2 | HAVE SCAN | n/a: no `have` in the original or final proof. |
| 3 | SET_OPTION | n/a: no local option. No limit raises introduced. |
| 4 | SIMP SQUEEZE | Original has no simp call. New terminal `simpa using hP` stays unsqueezed. |
| 5 | NAMING | `weightSet_nonempty` describes nonemptiness of the weight set, uses the mathematical stem `weightSet`, and contains no forbidden abbreviation or numbered pattern. Standard property used by two results, so `_aux` is not needed. No rename queued. |
| 6 | LINE PACKING | Two signature lines measured below; unchanged and both pass. |
| 7 | BY PLACEMENT | `by` ends conclusion line 61. |
| 8 | FORMAT | Two-space tactic indent; no blank line inside, semicolon, `haveI`, or `letI`. |
| 9 | COMMENTS | None present in the target; none removed or relocated. |
| 10 | DOCSTRING | Private helper has no docstring; none added. All existing docs preserved. |
| 11 | VISIBILITY | Already private and used only at two callers in Index. Classic dialect. |
| 12 | STRUCTURE | Four declaration lines become three; body is one tactic; no conjunction or branch. No decomposition needed. |
| 13 | MATHLIB | Five actual methods below found `MvPolynomial.support_nonempty`; compiled direct composition and caller-deletion proposal. |
| 14 | JUNK DEF | n/a: lemma, not a definition. |
| 15 | EXISTS LEMMA | n/a: a set nonemptiness proposition, not a single-use witness/rfl lemma; two callers. Wrapper deletion is assessed separately. |
| 16 | SHOW vs CHANGE | n/a: no `show` in this target. |
| 17 | PUSH_NEG | n/a: no `push_neg`. |
| 18 | GENERALISE | Every elaborated binder audited/probed below; no signature change retained. |
| 19 | INEQUALITY | No inequality in the target signature; table below. |
| 20 | NORMAL-FORM | Canonical `Set.Nonempty`; simp reduces it to `P ≠ 0`. |
| 21 | SYNTAX-GEN | Existing explicit `hP`, `α`, `r` and implicit `P` work at both callers. Deletion proposed instead of an alternate wrapper API. |
| 22 | IMPORT-FANOUT | n/a: no imports introduced. |
| 23 | CASTS | Diff: 0 dropped / 0 cross-type kept / 0 load-bearing kept. Existing signature's Finset-to-Set ascription is untouched. |
| 24 | INSTANCE-NAME | n/a: theorem declares no instance. |

Issues fixed: replace the six-rewrite proof with a terminal simplification of `hP`.
Refactoring needed: owner should delete this thin private wrapper and use the compiled
direct proofs at both callers, after this worker releases source editing. No public API
change is needed. Do not add a replacement generalized wrapper.

## Line packing — before and after

Actual `#check @decl` rendered at `format.width := 100`, using a metaprogram to quote
the built private constant (its numeric private-name component cannot be typed as an
ordinary dotted identifier):

```lean
@Roth.weightSet_nonempty✝ : ∀ {σ : Type u_1} [inst : Fintype σ] {P : MvPolynomial σ ℝ},
  P ≠ 0 → ∀ (α : σ → ℝ) (r : σ → ℕ), (weight r '' ↑((taylor α) P).support).Nonempty
```

| Signature line | Codepoints | Next signature chunk | Arithmetic | Action |
|---|---:|---|---|---|
| 60 | 94 | full conclusion plus `:= by`, 66 codepoints | 94 + 1 + 66 = 161 > 100; even first token `(weight` gives 94 + 1 + 7 = 102 > 100 | ok |
| 61 | 70 | none; proof body follows | n/a, final signature line | ok |

Widths measured using Python `len` on the exact source lines (Unicode codepoints).
The unchanged final signature was re-read and remeasured after editing.

## Inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 1 | Entire signature and hypotheses | n/a: no `≥`/`>` or other inequality | n/a | n/a |

## Mathlib search-status

All five methods were actually called; no remote search failure is being interpreted as
absence. The remote services returned successful results in this worker session.

| Method | Actual bounded query | Result |
|---|---|---|
| A Lean-Finder | `image of support of a nonzero multivariate polynomial is nonempty`, 3 results | `MvPolynomial.support_nonempty`; two finSuccEquiv support variants. |
| B Loogle | `MvPolynomial.support, Finset.Nonempty`, 4 results | `MvPolynomial.support_nonempty`. |
| C LeanSearch | `The support of a nonzero multivariate polynomial is nonempty`, 3 results | `MvPolynomial.support_nonempty`, polynomial counterpart, and support definition. |
| D Mathlib source | `support_nonempty`, `support_nonempty_iff`, `image_nonempty`, `taylor_eq_zero_iff` in MvPolynomial and Set/Image sources | `support_nonempty` Basic.lean:770; Set.image_nonempty Image.lean:396. Taylor equivalence is project API, Roth/Taylor.lean:186. |
| E Native local-name search | `support_nonempty`, `taylor_eq_zero_iff`, `Set.Nonempty.image`, `Finset.coe_nonempty` | Positive declarations located. Index reported `warming`; positive source hits were corroborated by actual `#check`/compiled terms. No absence claim. |

Auxiliary variants checked: `support_nonempty_iff` (Finsupp), `support_eq_empty`,
`nonempty_iff_ne_empty`, `Set.Nonempty.image`, and Finset coefficient support coercion.
Common-equivalents lookup: no special discrete/compact/metric bucket applies; this is
the generic support/image API. There is no global classical equality instance.

Conclusion: composable directly from mathlib support/image simp lemmas and existing
project Taylor equivalence. ACTION: owner deletes helper and updates two callers.
No claim that the abstract fact is absent, no new API lemma needed, no docstring edit.

## Generalisation status

Each drop below was an actual independent Lean probe with `autoImplicit := false`.
These tests did not modify the source. Expected failures are recorded as failures.
Native scratch imports temporarily reported the edited Index import as out of date;
the final fresh Lake compile below verifies against the newly built artifact.

| # | Binder | Class/use | Candidates actually tried | Verified result |
|---|---|---|---|---|
| 1 | `{σ : Type*}` | Type variable for variables and supports | Drop; universe catalogue reviewed | Drop rejects unknown σ. Already universe polymorphic; no restriction to weaken. |
| 2 | `[Fintype σ]` | Typeclass required by `weight`'s finite sum | Drop; replace with `[Finite σ]` | Both reject missing `Fintype σ` in statement. Keep. |
| 3 | `{P : MvPolynomial σ ℝ}` | Structure value in support and hP | Drop | Unknown P. Keep; changing coefficient ring would require changing weight's target/general API. |
| 4 | `(hP : P ≠ 0)` | Proposition closes simplified goal | Drop with unchanged proof; drop plus `simp` | Unknown hP first; meaningful proof retry leaves `⊢ ¬P = 0`. Keep. No ordered-polynomial strict-to-weak candidate. |
| 5 | `(α : σ → ℝ)` | Translation point | Drop | Unknown α. Keep; no global pointwise hypothesis to localize. |
| 6 | `(r : σ → ℕ)` | Weight denominator function | Drop | Unknown r. Keep; no positivity assumption to weaken. |
| 7 | `[DecidableEq σ]` | Ambient instance explicitly omitted | Both no-instance original-type proof and an added-instance specialization compiled | Already omitted, so not a binder of this declaration. Keep omission. |

Inversion check: this is a concrete image/support nonemptiness corollary; the abstract
version is exactly existing mathlib support/image API. Delete at callers instead of
generalizing the wrapper. Big-change candidates: none to implement here.
Literature: n/a: private declaration, literature search not required.

## Golfing rule pass (42/42)

| Rule | Status |
|---|---|
| 1.1 by exact wrapper | n/a: no such wrapper. |
| 1.2 by rfl | n/a: no reflexivity proof. |
| 1.3 rw + exact | Already `rwa`; replaced by direct `simpa using hP`. |
| 1.4 simp + exact → simpa | Applied as simplification of hP instead of manually rewriting goal. |
| 1.5 trailing rfl | n/a: no trailing rfl. |
| 1.6 constructor tuple | n/a: no constructor branches. |
| 1.7 apply + exact | n/a: no apply chain. |
| 1.8 by_contra! | n/a: no contradiction block. |
| 1.9 eta reduction | n/a: no lambda. |
| 1.10 single-use have | n/a: no have. |
| 1.11 apply + intro | n/a: no apply/intro. |
| 1.12 redundant show | n/a: no show. |
| 1.13 projections → obtain | n/a: no have/projections. |
| 1.14 merge rewrites | Original is already one rewrite call; entire chain removed. |
| 1.15 terminal simp only | n/a: final simpa remains unsqueezed. |
| 1.16 nonterminal simp squeeze | n/a: no nonterminal simp. |
| 1.17 dot notation | Direct term alternative `.image _` compiled; longer than final tactic. |
| 1.18 use <\| | n/a: final proof has no parenthesized argument to simplify. |
| 1.19 push Not | n/a: no push_neg. |
| 1.20 trivial existential lemma | n/a: not a single-use explicit witness lemma. |
| 2.1 grind | Actual live-file attempt failed to derive image nonemptiness. |
| 2.2 remove tactics before grind | n/a: no retained grind. |
| 2.3 simpa consolidation | Applied: `simpa using hP`, independently and live-file verified. |
| 2.4 fun_prop | n/a: no function-property goal. |
| 2.5 positivity | n/a: goal is set nonemptiness, not positivity/order. |
| 2.6 gcongr | n/a: no inequality or monotonicity goal. |
| 2.7 lia / omega | n/a: no Nat/Int arithmetic goal. |
| 2.8 aesop | Actual live-file attempt succeeds; retain explicit simpa to show use of hP. |
| 2.9 norm_num / norm_cast | n/a: no numeric calculation/cast goal. |
| 2.10 decide / decide +kernel | n/a: arbitrary real polynomial and function parameters, no closed finite computation. |
| 2.11 field_simp; ring | n/a: no rational identity. |
| 2.12 linear_combination | n/a: no ring/ring_nf ending or polynomial equality goal. |
| 2.13 wlog | n/a: no symmetric branches. |
| 2.14 calc → term | n/a: no calc. |
| 2.15 <;> | n/a: only one goal/tactic. |
| 3.1 erw → rw | n/a: no erw. |
| 3.2 continuity/measurability | n/a: neither occurs. |
| 3.3 omega → lia | n/a: no arithmetic tactic. |
| 3.4 rcases with rfl | n/a: no rcases. |
| 3.5 automation attributes | n/a: wrapper deletion is preferred; supporting facts already have simp attributes. |
| 3.6 simp_all | Actual live-file `simp_all` succeeds; explicit `simpa using hP` retained for directness. |
| 3.7 remove maxHeartbeats | n/a: no option present or introduced. |

Step-back reflection: whole-proof `grind` failed; `aesop`, `simp_all`, and
`simpa using hP` all succeed. Bare `simp` leaves `P ≠ 0`; `exact?` fails;
`apply?` supplies partial image/nonempty routes. A composed term with
`Finset.coe_nonempty`, `support_nonempty`, Taylor injectivity, and `.image _`
compiled independently but is longer. Keep the one-tactic explicit simplification.
Initial multi-attempts on the old wrapped `rwa` left a dangling continuation line;
all automation results used here were rerun successfully on the final one-line proof.

## Verification and gates

`lake build Roth.Index > /private/tmp/index-nonempty-build.log 2>&1` exited 0
(session 99920; `Build completed successfully (1501 jobs)`). This is the required
module build, not a full-project build. The owner retains full-project verification.

`lake env lean /private/tmp/IndexNonemptyCallers.lean` exited 0 (session 6633).
This independent copy deletes the helper and substitutes direct proofs at both
callers; it is a proposal only, not an edit to another owned declaration.

Final full native `lean_diagnostic_messages` returned success=true, partial=false,
timed_out=false, no errors and no target warnings. The 27 pre-existing warnings on
other declarations/header remain with the file owner.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Actual `lake build Roth.Index`, exit 0. |
| definition_protected | pass | No definition/abbreviation or import changed. |
| theorem_statement_protected | pass | Exact target signature/omit directive unchanged; proof-only diff. |
| structure_gate | pass | One tactic; no conjunction/branch. |
| naming_gate | pass | Descriptive mathematical stem; no forbidden pattern/abbreviation; no in-place rename. |
| line_packing_gate | pass | Both measured signature rows pass unchanged. |
| inequality_orientation_gate | pass | Zero reversed inequalities; table above. |
| comments/documentation | pass | None in target; all existing file docs untouched. |
| identifier verification | pass | New proof only uses existing hP and the simpa tactic. Supporting API verified by local search, source and `#check`/compiled terms. |

Independent original-type recovery and built-private axiom check: final fresh
`/private/tmp/WeightSetNonemptyVerification.lean` imports the built Index, dynamically
quotes the actual private declaration for `#check`/`#print axioms`, and independently
proves the exact original no-DecidableEq signature without referencing this helper.
It also verifies the DecidableEq specialization. Fresh compiler session 18097 exited 0.
The actual built constant `_private.Roth.Index.0.Roth.weightSet_nonempty` depends on
exactly `[propext, Classical.choice, Quot.sound]`. The original-type independent proof
also compiled with no DecidableEq binder, matching the original snapshot exactly.

## Result and checklist

Before: 4 declaration lines. After: 3. Saved: 1. Rules applied: 1.4, 2.3.
Audit issues fixed: 1 proof simplification. Refactoring deferred to owner: 1 wrapper
deletion at two callers. Renames-queued: none. Comments-preserved: none present.
No sorry/new axiom/limit raise. Overall Phase 4 gates: pass. Full build and final anchored per-declaration
profile are owner's work; aggregate timing is not claimed as target timing.

- [✓] Step 1 — required reference docs read.
- [✓] Step 2 — all 24 audit items concretely recorded.
- [✓] Step 2.5 — actual five-method search-status block.
- [✓] Step 2.6 — every binder and applicable weakening probed.
- [✓] Step 2.7 — width-100 #check and all signature-line arithmetic.
- [✓] Step 2.8 — inequality scan table.
- [✓] Step 3 — all 42 golfing rules recorded.
- [✓] Step 4 — strategy/term-mode/automation reflection.
- [✓] Step 5a — complete LSP, target clean and no errors.
- [✓] Step 5b — diff gates and actual module build.
- [✓] Step 6a — no renames needed or applied.

Buzz: owner will run final hash-anchored source profile. No actual per-declaration
timing has been inferred from aggregate build or tactic-check times.

Source freeze: SHA256 `f1cb21686cecb906d503fc2a7ff919fcca73dfc9c5a879eaa54750b4494cdbe5`.
Source editing explicitly released to the owner after every compiler process finished.
`git diff --check` passed. No Git staging/commit/push was performed by this worker.

## Owner Phase5a amendment

After explicitly revoking worker source editing, owner accepted the compiled deletion
proposal and removed the helper/omit command. Its two callers now use direct terminal
`simpa using hP`; the attained-minimum call supplies the set's nonempty type explicitly
in term mode so elaboration can infer the `csInf_mem` receiver. No public type, data
definition, documentation or other hypothesis changed. Current source267lines,
19retained declarations. Frozen SHA256
`531003ff42de90398daad179eb7b7006cc520efea475de29274078cad567bf9a`.

Actual owner module2756 exit0; complete native LSP success=true,partial=false,
zero errors27 inherited warnings. Fresh whole ORIGINAL independent source reproof,
all18 public type/value equalities and all19 actual retained constant standard-axiom
checks58412 exit0, `/private/tmp/roth-index-d04-compatibility.log`.
Owner sequential full then separate LeanEval47084 both exited0(137.39s/33.18s),
Index and Theta source hashes stable; `/private/tmp/roth-index-d04-{full,leaneval}.log`.
Block docs remain byte-identical and all source lines≤100 codepoints.

Coefficient-domain clarification: generalizing P and α would coordinate their two
types and the relevant Taylor equivalence; it does not require changing Roth.weight's
real target. This potential wrapper restatement is unnecessary because the wrapper
is deleted in favor of existing generic support/image API, rather than generalized.
