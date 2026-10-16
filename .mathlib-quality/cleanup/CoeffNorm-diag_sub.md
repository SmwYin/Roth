# Phase 4: `Roth.diag_sub`

Dedicated single-declaration audit of `Roth/CoeffNorm.lean:194–195` on the supplied
`ramin-cleanup` baseline HEAD `4b26300`. C21: diagonal substitution respects subtraction.
Result: retain the existing two-line direct `map_sub` term without source churn.
Before: 2 declaration lines; after: 2; saved: 0. Audit defects: 0; fixed: 0;
refactoring deferred: 0. Public signature, visibility, attributes, docstring and definitions
are unchanged. The public API preservation instruction overrides the skill's generic
wrapper deletion guidance; the existing call in `Roth/MainLemma.lean:463` uses `diag_sub`
in a rewrite list. Deletion would break that API and has no required concrete benefit.

## References and baseline

Read both complete skills `mathlib-quality/SKILL.md` and `lean4/SKILL.md`, the complete
853-line `/private/tmp/roth-coeffnorm-worker-contract.md`, and the full required references
`golfing-rules.md`, `proof-patterns.md`, `mathlib-search.md`, `generalisation-patterns.md`,
`cleanup-gates.md`, `style-rules.md`, and `naming-conventions.md`. Also read
`mathlib-review-stages.md` for normal forms and syntactic generality.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md.

The parent supplied successful baseline `lake build`, followed by the separate
`lake build Roth.LeanEval`, session 32277, exit 0. Those baseline builds were not repeated
by this worker. Native complete diagnostics were actually obtained at entry and at exit:
`partial=false`, `success=true`, `timed_out=false`, no failed dependencies and no errors.
Six existing warnings are outside this declaration: header at line 1; unused
`DecidableEq` in `normOne_mul_le`, `normOne_prod_le`, `normOne_det_le`, and
`abs_coeff_det_hasseDeriv_le`; unused `hC` in `normOne_det_le`. No suppression was added.
There are no target warnings. Existing header and public arguments remain as instructed.

## Full audit (all 24 items)

| # | Item | Concrete finding/action |
|---|---|---|
| 1 | LINT | Complete native diagnostics: no errors or warnings at 194–195. |
| 2 | HAVE SCAN | Zero `have` occurrences; nothing to inline or count. |
| 3 | SET_OPTION | No per-declaration option, heartbeat or recursion override. |
| 4 | SIMP SQUEEZE | No simp in retained proof; tested terminal `simp [diag]`, which compiles. |
| 5 | NAMING | `diag_sub` describes diagonal substitution of subtraction; snake case, no forbidden abbreviation or pattern. |
| 6 | LINE PACKING | Single signature line is 77 codepoints; entire signature and conclusion already fit. Table below. |
| 7 | BY PLACEMENT | Term proof has no `by`; no detached `by` to repair. |
| 8 | FORMAT | Two-space term continuation, no internal blank line or trailing space; no tactics or instance plumbing. |
| 9 | COMMENTS | No inline proof comments; existing one-line docstring preserved byte for byte. |
| 10 | DOCSTRING | Existing `/-- `diag` is additive. -/` retained under explicit preservation instruction. |
| 11 | VISIBILITY | Public compatibility lemma used by MainLemma; preserve its exported name and type. |
| 12 | STRUCTURE | One proof line; no conjunction, branch or decomposition candidate. |
| 13 | MATHLIB | Generic `map_sub` already used directly; five actual search methods recorded below. |
| 14 | JUNK DEF | n/a: target is a theorem, not a definition. |
| 15 | EXISTS LEMMA | n/a: no existential and no private witness helper. |
| 16 | SHOW vs CHANGE | No `show`; no goal transport in retained term. |
| 17 | PUSH_NEG | No `push_neg` or negation tactic. |
| 18 | GENERALISE | Every actual parameter audited and drop-probed below; no safe source change. |
| 19 | INEQUALITY | Zero reversed inequalities, zero inequality operators at all; table below. |
| 20 | NORMAL-FORM | Standard homomorphism normal form: image of subtraction equals subtraction of images. |
| 21 | SYNTAX-GEN | OK: explicit P Q and rewrite-compatible equality serve the actual rewrite call site. |
| 22 | IMPORT-FANOUT | n/a: no new or modified import. |
| 23 | CASTS | 0 dropped / 0 cross-type / 0 load-bearing in source diff; source diff is empty. |
| 24 | INSTANCE-NAME | n/a: theorem declares no instance. |

Issues to fix: none. Refactoring needed: none. Renames queued: none.

## Five-method mathlib search status

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | `ring homomorphism preserves subtraction map_sub` | `RingHom.map_sub`, `MulSemiringActionHom.map_sub`, `RingEquiv.map_sub`. |
| B Loogle | `"map_sub"`; `_ (_ - _) = _ - _`; `?f (?x - ?y) = ?f ?x - ?f ?y` | First returns substring noise (`List.map_subset` etc.); second rejected placeholder-function pattern; third returns Nat subtraction noise. Method tried; no absence claim. |
| C LeanSearch | `A ring homomorphism preserves subtraction` | `RingEquiv.map_sub`, `Polynomial.map_sub`, `RingHom.map_sub`. |
| D source rg | `theorem map_sub|lemma map_sub|eval₂_sub|aeval_sub` in Group/Hom, Ring/Hom and MvPolynomial | `RingHom.map_sub` at Hom/Defs:502; MvPolynomial `eval₂_sub` at CommRing:160, `eval_sub` nearby. |
| E local search | `map_sub`, then `RingHom.map_sub` | Positive source hits include `RingHom.map_sub`; index was warming, so no negative conclusion inferred. |

Auxiliary variants inspected: `MvPolynomial.eval₂_sub`, `MvPolynomial.eval_sub`,
`RingHom.map_sub`, `RingEquiv.map_sub`, and explicitly instantiated `aeval` passed to
generic `map_sub`. Common-equivalents table: no topology/finiteness/separation bucket;
this is ordinary bundled homomorphism compatibility.

Conclusion: the abstract fact is already `map_sub`, with strictly weaker algebraic
requirements than polynomial evaluation. Keep this existing public compatibility name
under the explicit API preservation instruction, and continue using `map_sub` directly
as its body. No missing API and no wrapper deletion pending.

Six strict rules: (1) no new wrapper created; existing API retained by task override;
(2) all five searches actually attempted and no absence claimed; (3) auxiliary variants
checked; (4) no custom predicate; (5) existing public deletion expressly closed by scope;
(6) no module-doc change authorized or required; mathlib usage recorded here.

## Generalisation status (every parameter)

`#check @Roth.diag_sub` confirms the complete parameter list is only `{σ}`, `P`, `Q`.
There are no typeclass, proposition, decidability or hidden section-instance parameters.

| # | Parameter | Class | Used as | Mechanical candidates and actual probe | Verified? | Result |
|---|---|---|---|---|---|---|
| 1 | `{σ : Type u_1}` | type variable | variable index of P,Q and diag | Drop σ with `autoImplicit=false`; existing universe-polymorphic `Type u` also independently checked | yes, scratch diagnostics | Drop fails `Unknown identifier σ`; Type* already maximal ordinary universe polymorphism. No change. |
| 2 | `(P : MvPolynomial σ ℤ)` | structure value | minuend and first output image | Drop P with autoImplicit=false; coefficient ring abstraction independently compiled with arbitrary `[CommRing R]` | yes, scratch diagnostics | Drop fails `Unknown identifier P`; abstract coefficients require changing diag's definition/API, closed by explicit preservation. No change. |
| 3 | `(Q : MvPolynomial σ ℤ)` | structure value | subtrahend and second output image | Drop Q with autoImplicit=false; same arbitrary-coefficient probe covers both arguments | yes, scratch diagnostics | Drop fails `Unknown identifier Q`; both arguments required. No change. |

The drop probes were isolated `lean_run_code` experiments with the substitutions
actually applied; they intentionally produced errors and never modified the live file.
They additionally showed elaboration timeouts downstream of the unknown P/Q errors;
these are failed candidates, not successful diagnostics. No candidate is marked kept.
For each row, typeclass-parent, point-localisation, strict-to-weak, and unbundling
catalogue entries are inapplicable: σ is a type and P,Q are polynomial values, with no
such hypotheses to weaken. The implicit universe was independently instantiated as
arbitrary `u`; no monomorphic universe restriction exists.

Inversion check: the retained body is already exactly the abstract `map_sub` theorem;
no proof after an unfolding rewrite exists to extract. The general statement is present
in mathlib, rather than a new theorem needed in this project.

Big-change candidates: none actionable. Arbitrary coefficients and arbitrary additive
homomorphisms are mathematically valid, but the former changes the definition/API and
the latter is already supplied by `map_sub`. Neither establishes a required concrete
benefit for redesigning this established compatibility API, so both are closed, not pending.

## Public literature search

Actual web query: `ring homomorphism subtraction preservation generalization polynomial evaluation`.
Top three returned primary teaching sources:

1. [Steffen Müller, Algebraic Structures, III.2 Evaluation homomorphisms](https://www.rug.nl/staff/steffen.muller/lecture_notes_algebraic_structures.pdf).
2. [Paul Garrett, The Mathematics of Coding](https://www-users.cse.umn.edu/~garrett/coding/CodingNotes.pdf).
3. [Evan Dummit, Algebra 1, Rings part 2](https://dummit.cos.northeastern.edu/teaching_fa20_5111/5111_lecture_03_rings_part2.pdf).

The search excerpts describe polynomial evaluation as a ring homomorphism. This supports
the canonical homomorphism formulation; subtraction preservation is its additive-group
consequence. Inference: no special finiteness, decidable equality or order assumption
is needed here. The actual pinned-environment `#check @map_sub` gives the sharper
formal generality: AddGroup domain, SubtractionMonoid codomain, and AddMonoidHomClass.
ChatGPT math MCP: n/a, no such tool is exposed in ALL_TOOLS (searched actual metadata).
Literature-driven big-change candidates: none beyond the already-closed abstraction.

## Width-100 reference and packing

Actual native `lean_run_code`, `set_option format.width 100`, output:

```lean
@diag_sub : ∀ {σ : Type u_1} (P Q : MvPolynomial σ ℤ), diag (P - Q) = diag P - diag Q
```

| Signature line | Codepoints | Next signature token | Arithmetic | Action |
|---|---:|---|---|---|
| 194 | 77 | none; next line is proof term | n/a, complete signature and `:=` already on one line | ok |

Proof line 195 is 15 codepoints with two-space indentation. The complete declaration
could be visually placed on one line in 91 codepoints, but moving term-mode proof onto
the signature does not shorten the proof or improve clarity/performance; the instruction
to preserve the existing best direct term without needless churn applies. There is no
underpacked signature continuation: its one signature line contains all binders and conclusion.

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 1 | full signature and parameters | n/a: no `≥` or `>` | none | no `_ge_` or `_gt_` name |

## All 42 golfing rules

- [1.1] n/a: already a direct term, no `by exact`.
- [1.2] n/a: no `by rfl`; scratch `rfl` actually fails.
- [1.3] n/a: no rw/exact chain.
- [1.4] n/a: no simp/exact chain.
- [1.5] n/a: no trailing rfl.
- [1.6] n/a: no constructor or conjunction.
- [1.7] n/a: no apply/exact chain.
- [1.8] n/a: no contradiction proof.
- [1.9] n/a: no lambda in retained proof.
- [1.10] n/a: no have.
- [1.11] n/a: no apply/intro chain.
- [1.12] n/a: no show.
- [1.13] n/a: no projections or have.
- [1.14] n/a: no rw.
- [1.15] n/a: retained proof has no terminal simp only; candidate simp only [diag,map_sub] compiled but not adopted.
- [1.16] n/a: no nonterminal simp.
- [1.17] Tested aeval-dot-map_sub: untyped dot variant failed inference at default heartbeat limit; explicit generic map_sub(aeval...) compiled and is longer than retained term.
- [1.18] n/a: retained term has no parentheses to replace.
- [1.19] n/a: no push_neg.
- [1.20] n/a: no existential helper.
- [2.1] Actual `fail_if_success grind` passed in successful scratch example, certifying bare grind fails; retain map_sub.
- [2.2] n/a: no tactics before grind.
- [2.3] `simp [diag]` compiles; no consolidation chain exists; direct term stays shorter and names the exact fact.
- [2.4] n/a: algebraic equality, no analytic function property.
- [2.5] n/a: not a positivity/nonzero goal.
- [2.6] n/a: no ordered congruence.
- [2.7] n/a: no Nat/Int arithmetic proposition; equality is between polynomials.
- [2.8] Actual `fail_if_success aesop` passed in successful scratch example, certifying bare aesop fails.
- [2.9] n/a: no numerical computation or casts.
- [2.10] n/a: arbitrary polynomials, no closed finite decision problem.
- [2.11] n/a: no denominators or field expression.
- [2.12] n/a: proof does not end in ring/ring_nf and has no algebraic hypotheses to combine.
- [2.13] n/a: no symmetric case branches.
- [2.14] n/a: no calc.
- [2.15] n/a: no multiple subgoals.
- [3.1] n/a: no erw.
- [3.2] n/a: no continuity/measurability.
- [3.3] n/a: no omega or arithmetic proof.
- [3.4] n/a: no rcases.
- [3.5] No attribute added: existing API attributes preserved; generic homomorphism simplification already handles the unfolded form.
- [3.6] n/a: no simp_all only.
- [3.7] n/a: no heartbeat option.

## Actual experiments and reflection

Native `lean_goal` at 195 showed the term line and no tactic goals, as expected for a term
proof. `lean_run_code` is the appropriate isolated experiment route in that situation.
Successful clean runs checked direct `map_sub _ _ _`, `by simp [diag]`, terminal
`simp only [diag, map_sub]`, explicit `map_sub (aeval ...) P Q`, and arbitrary coefficient
CommRing R with explicit universe u,v. Bare rfl, simp, grind and aesop were each
certified failures with `fail_if_success` in a scratch theorem completed by simp [diag].
Initial exploratory untyped dot notation timed out, and exact?/apply? after a broad
`change` timed out at default heartbeats; none was installed or assigned a raised limit.
Plain exact?/apply? on the original theorem succeeded by suggesting `diag_sub P Q`;
that is self-reference for this audit and was rejected. The independent reproof below
uses only simp [diag], not this theorem.

Step back: the whole proof is already one named theorem application. A single simp tactic
also works, but requires explicitly unfolding diag. No have, redundant step, case split,
or alternative mathematical strategy can usefully collapse further. The generic theorem
already provides the abstract formulation. Retain the direct term and public API.

## Verification and actual diff gates

Source frozen before final verification, whole-file SHA256:
`815a7a525d0a6ec34149da5b5d141cf978321d242abbefb9eb50bbcad4fe2cd8`.
The parent acknowledged source ownership revoked at that hash. No later source edit.
Worker declaration snapshot `/private/tmp/diag-sub-start.txt` equals the final block;
the worker diff is empty. Source never needed an apply_patch; only this report was added.

Actual final module command: `/Users/ramin/.elan/bin/lake build Roth.CoeffNorm`,
session 57811, exit 0, `Build completed successfully (1658 jobs)`; existing warnings replayed.
Actual final complete native diagnostics: `partial=false`, `success=true`,
`timed_out=false`, `failed_dependencies=[]`, zero errors and the six outside warnings above.

Actual independent original-type assignment and nonself reproof compiled successfully:

```lean
import Roth.CoeffNorm
set_option autoImplicit false
open Roth MvPolynomial
universe u
example : ∀ {σ : Type u} (P Q : MvPolynomial σ ℤ),
    diag (P - Q) = diag P - diag Q := @Roth.diag_sub
example {σ : Type u} (P Q : MvPolynomial σ ℤ) :
    diag (P - Q) = diag P - diag Q := by simp [diag]
#print axioms Roth.diag_sub
```

Actual axiom output: `[propext, Classical.choice, Quot.sound]`; no sorry or custom axiom.

| Gate | Result | Actual evidence |
|---|---|---|
| lake_build_file | ✓ pass | session 57811 exit 0, module command above |
| definition_protected | ✓ pass | worker source diff empty; no definition lines changed |
| theorem_statement_protected | ✓ pass | original exact-type assignment succeeds, signature untouched |
| structure_gate | ✓ pass | one proof line, no conjunction/branch |
| naming_gate | ✓ pass | descriptive diag_sub, no forbidden patterns |
| line_packing_gate | ✓ pass | measured single complete 77-codepoint signature row above |
| inequality_orientation_gate | ✓ pass | actual signature scan has 0 ≥ and 0 > |
| docstrings/comments/API | ✓ pass | empty worker source diff |

Overall: pass. Comments preserved: existing docstring; no inline comments present.
Rules applied: none necessary. Renames queued: none. Refactoring needed: none.

- [✓] Step 1 — full reference docs read.
- [✓] Step 2 — all 24 audit items reported.
- [✓] Step 2.5 — five-method search and six strict rules recorded.
- [✓] Step 2.6 — every parameter mechanically analysed and actually probed; literature search recorded.
- [✓] Step 2.7 — width-100 #check and complete signature packing table emitted.
- [✓] Step 2.8 — full inequality scan table emitted.
- [✓] Step 3 — all 42 golfing rules given individual statuses.
- [✓] Step 4 — independent alternatives tested and reflection recorded.
- [✓] Step 5a — complete final native diagnostics success, zero errors/target warnings.
- [✓] Step 5b — actual module build and all diff gates pass.
- [✓] Step 6a — rename review complete; no rename needed or sidecar mutation.
