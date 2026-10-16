# Declaration cleanup: `MvPolynomial.eval_taylor`

Baseline: `53f4983`; target live lines 135–137. Before: 3 declaration lines / 1 proof line. After: 3 / 1. Saved: 0 lines. Improvement: replace polynomial induction with the library's evaluation composition theorem; ordinary lambda uses `↦`. Exact mathematical type, name, argument order, visibility, attributes, imports, and docstring preserved.

SOURCE FROZEN: whole `Roth/Taylor.lean` SHA256 `fbd691573b1e1fa3dd2c4f33449095583791028ee6cbd25a8d92df2175e9ab39`. Source ownership handed to the parent after module build and complete LSP. This worker did no Git/shared-log/full-project-build operations.

## References and mathematics

Read lean4 and mathlib-quality SKILL.md, the complete worker contract, golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, cleanup-gates.md, relevant formatting/documentation/tactic/visibility sections of style-rules.md, and mathlib-review-stages.md. Naming was checked against the contract's explicit forbidden patterns; no naming issue required the optional naming reference. Existing docs are preserved under the user's stronger instruction.

Mathematics: substituting `X + α` then evaluating at `x` is substitution at `x + α`. This is associativity of polynomial substitution (`eval_assoc`), followed by evaluation of variables, constants, and sums. No induction specific to this theorem is needed.

## Full audit (24 items)

1. LINT: complete final LSP has no target diagnostics; only preserved file-line-1 copyright warning.
2. HAVE SCAN: none before/after.
3. SET_OPTION: none; no limits or suppression added.
4. SIMP SQUEEZE: original terminal `simp_all` unsqueezed; final terminal `simp [taylor, aeval_def, ← eval_assoc, Function.comp_def]` unsqueezed. No nonterminal simp.
5. NAMING: `eval_taylor` describes evaluation of translation, snake_case, no forbidden abbreviation or numbered/scheme pattern. No rename.
6. LINE PACKING: measured every signature line below; complete equation cannot join binder line within 100 characters.
7. BY PLACEMENT: `:= by` ends the conclusion line.
8. FORMAT: 2-space proof indent, 4-space statement continuation, no internal blank lines, no tactic chains, no haveI/letI; lambda `=>` changed to `↦`.
9. COMMENTS: no inline proof comments; existing docstring unchanged.
10. DOCSTRING: concise existing public documentation explains the evaluation identity; preserved byte-for-byte.
11. VISIBILITY: public translation API retained as explicitly requested. Current repository rg finds only the declaration; this does not authorize removing public API.
12. STRUCTURE: one proof line, no conjunction or case branch; no extraction needed.
13. MATHLIB: all five search methods attempted; found general composition APIs, used `eval_assoc` directly in proof. Details below.
14. JUNK DEF: n/a, theorem rather than definition.
15. EXISTS LEMMA: n/a, no existential witness.
16. SHOW vs CHANGE: none in final proof. Tested change/rw/simp route works but is longer.
17. PUSH_NEG: none.
18. GENERALISE: every implicit/explicit parameter checked below; no safe in-place weakening.
19. INEQUALITY: no reversed inequalities; table below.
20. NORMAL-FORM: translated evaluation on left reduces to evaluation at shifted point on right; matches substitution composition normal form, no equivalence proliferation.
21. SYNTAX-GEN: OK; explicit α, x, P make rewriting straightforward; no derived hypothesis demanded from users.
22. IMPORT-FANOUT: n/a, no imports added.
23. CASTS: 0 dropped / 0 cross-type / 0 load-bearing ascriptions added; only existing binder type annotations remain.
24. INSTANCE-NAME: n/a, no instance declaration.

Issues fixed: induction replaced by composition; ordinary lambda style. No deferred refactoring. The generic skill's wrapper-deletion recommendation conflicts with the explicit exact-public-API preservation instruction; the latter governs. No declaration deletion or documentation rewrite is proposed.

## Five-method mathlib search

| Method | Query | Actual result |
|---|---|---|
| A Lean-Finder | `multivariate polynomial evaluation composition substitution` | `MvPolynomial.aeval_comp_bind₁`, `eval₂_cast_comp`, `eval₂Hom_bind₁` |
| B Loogle | `MvPolynomial.aeval, _ (_ _) = _`; corrected `MvPolynomial.aeval, MvPolynomial.aeval` | First query rejected: placeholder cannot be function; corrected query returned aeval, aevalTower_id, aevalTower_ofId |
| C LeanSearch | `Multivariate polynomial evaluation composed with algebra evaluation substitution` | aeval_bind₁, aeval_comp_bind₁, eval_comp_toMvPolynomial; service worked |
| D Source | eval/aeval composition, comp_C, eval₂_id, eval_eval₂ in Algebra/MvPolynomial/Eval.lean | eval_assoc (line 303), eval_eval₂, comp_aeval, comp_aeval_apply, map_aeval |
| E Name patterns | `comp_aeval`, project root explicit | Found comp_aeval and comp_aeval_apply; index warming, presence supported by source and compilation, not absence inference |

Auxiliary variants inspected: applied/unapplied `comp_aeval`, `comp_aeval_apply`, `map_aeval`, `eval_assoc`, `eval_eval₂`, `eval₂_comp_left`, `eval₂_id`, and bind₁ APIs. Common-equivalents table: no topology/finiteness/predicate replacement applies. Conclusion: partial match/general composition theorem found; retain mandated public translation theorem and build its proof on mathlib. No claim that mathlib lacks a theorem, no new wrapper introduced.

## Experiments and step-back reflection

Live `lean_multi_attempt` at proof line 137:

- `grind`: failed; `aesop`: no progress; `exact?`: could not close.
- `apply?`: only partial hom_congr_vars/DFunLike.congr suggestions; not a completed proof, its temporary sorry diagnostic is not accepted evidence.
- `simp [taylor, ← aeval_eq_eval, comp_aeval_apply]`: fails at coefficient-map composition because map_aeval rewrites first.
- `simpa [taylor, aeval_eq_eval] using comp_aeval_apply ...`: timeout at default 200000 heartbeats; no limit raised.
- `change aeval x (aeval (fun j ↦ X j + C (α j)) P) = _; rw [comp_aeval_apply]; simp`: works, three tactic lines.
- `simp [taylor, -map_aeval, ← aeval_eq_eval, comp_aeval_apply]`: works, but disabling a simp lemma is avoidable.
- `simp [taylor, aeval_def, eval_eval₂]`: leaves coefficient-map equality.
- `simpa [Function.comp_def] using (eval_assoc ...).symm`: fails to simplify the inferred intermediate type to the target.
- `simp [taylor, aeval_def, ← eval_assoc, Function.comp_def]`: succeeds, retained. This directly expresses substitution associativity.

Two invalid guessed identifiers (`eval_comp_C`, `eval₂_eval`) were rejected in temporary attempts, never added to source. An initial multi-attempt used signature line 136 by mistake and returned syntax errors; corrected to live proof line 137 before counting any results. A `simpa -only` experiment was invalid syntax, rejected. These are failed experiments, not verification.

Step back: the entire proof is now one terminal simp call using the library composition law. A direct term would need extensional evaluation normalization; the one-tactic proof is simpler. No have blocks, duplicated branches, or further redundant steps remain.

## Generalisation status

| Parameter | Class | Use | Mechanical candidates checked | Verified? | Result |
|---|---|---|---|---|---|
| `{σ : Type*}` | type variable | domain of α/x and variables of P | Drop breaks dependent types; universe polymorphism already independent Type* | Type print/dependency inspection | Keep arbitrary variable domain |
| `{R : Type*}` | type variable | coefficient and evaluation codomain | Drop leaves dependent types unbound; already Type* | Type print/dependency inspection | Keep |
| `[CommSemiring R]` | typeclass | taylor and eval API | Drop; weaken to Semiring | Native isolated run_code, both rejected with failed synthesis CommSemiring R | Keep; parents insufficient for current API |
| `(α : σ → R)` | structure value | translation point and RHS shift | Drop leaves statement occurrence unbound; no global predicate to point-localise | Dependency inspection | Keep arbitrary function |
| `(x : σ → R)` | structure value | evaluation point and RHS shift | Drop leaves statement occurrence unbound; no point/global or strict/weak condition | Dependency inspection | Keep arbitrary function |
| `(P : MvPolynomial σ R)` | structure value | polynomial on both sides | Drop leaves statement occurrence unbound; abstract exponent/index changes polynomial object | Dependency inspection | Keep arbitrary polynomial |

No proposition, decidability, finite-domain, nonzero, order, characteristic, or topology assumption exists to weaken. No bundled hypothesis can be unbundled. Drop-testing data binders means checking dependent occurrences, not letting autoImplicit silently recreate the same parameter.

Inversion check: translation is a special case of arbitrary polynomial substitution. The abstract result already exists as eval_assoc and comp_aeval_apply; use it rather than introducing another general theorem. No novel big-change candidate; no public signature change applied.

## Public literature search

Web query: `polynomial evaluation substitution universal property commutative semiring generalization`. Top three returned hits: Logic, Semirings, and Fixed Points (RWTH), RWTH masterarbeit on semirings, Elementary equivalence versus isomorphism in semiring semantics (ResearchGate copy). The ResearchGate copy was not relied on for a technical claim.

- [RWTH primary thesis](https://publications.rwth-aachen.de/record/996756/files/996756.pdf) describes polynomial semirings through the universal property extending assignments by evaluation.
- [RWTH primary thesis](https://logic.rwth-aachen.de/pub/mrkonjic/masterarbeit.pdf) discusses freely generated commutative semirings and extension of assignments to homomorphisms.
- [Polynomial ring canonical overview](https://en.wikipedia.org/wiki/Polynomial_ring) describes the free commutative algebra formulation, arbitrary variable sets, and polynomial rigs.

Inference from these sources plus checked Lean API: no field, characteristic-zero, subtraction, or finiteness assumption is needed; the current arbitrary-type/CommSemiring statement already has that breadth. The abstract composition law is already available in mathlib. ChatGPT math MCP: n/a, no matching callable tool in inventory. Literature-driven big-change candidates: none.

## Line packing

`#check @eval_taylor` in the exact pre-target probe at format.width 100:

```text
@eval_taylor : ∀ {σ : Type u_3} {R : Type u_4} [inst : CommSemiring R] (α x : σ → R) (P : MvPolynomial σ R),
  (eval x) ((taylor α) P) = (eval fun j => x j + α j) P
```

The probe deliberately retains original lambda syntax to check the original mathematical type. Source uses equivalent `↦` syntax. Widths count Unicode codepoints; the next signature token is the complete equation, not an arbitrary identifier fragment.

| Signature line | Chars | Next signature unit | Arithmetic | Action |
|---|---:|---|---|---|
| 135 | 58 | complete equation through `:= by`, 54 chars | 58 + 1 + 54 = 113 > 100 | ok |
| 136 | 58 | none, proof follows | n/a, final signature line | ok |

Before lambda conversion the conclusion unit was 55 chars and total 114, likewise too wide. Final proof line is 59 chars.

## Inequality scan

| Occurrence | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| none | full signature and all parameters | no ≥ or > operator | none | name has neither _ge_ nor _gt_ |

## Every golfing rule

- [1.1] n/a: no by-exact wrapper.
- [1.2] n/a: no by-rfl wrapper.
- [1.3] n/a: no rw/exact sequence in original or final.
- [1.4] n/a: no simp/exact sequence; simpa candidates tested and rejected as above.
- [1.5] n/a: no trailing rfl.
- [1.6] n/a: no constructor pair.
- [1.7] n/a: no apply/exact chain.
- [1.8] n/a: no contradiction/push-neg.
- [1.9] n/a: shifted sum lambda is not eta-reducible; arrow style fixed separately.
- [1.10] n/a: no have.
- [1.11] n/a: no apply/intro.
- [1.12] n/a: no show.
- [1.13] n/a: no projected have.
- [1.14] n/a: no consecutive rw.
- [1.15] n/a: no terminal simp only.
- [1.16] n/a: no nonterminal simp.
- [1.17] n/a: simp lemma names have no receiver-style application to shorten.
- [1.18] n/a: no trailing function/proof parentheses.
- [1.19] n/a: no push_neg.
- [1.20] n/a: no existential lemma.
- [2.1] tried whole-proof grind, failed.
- [2.2] n/a: no successful grind proof or preceding tactics.
- [2.3] tried simpa composition formulations, failed; final direct simp succeeds.
- [2.4] n/a: no continuity/differentiability/measurability goal.
- [2.5] n/a: no positivity/nonzero goal.
- [2.6] n/a: no inequality or monotonicity.
- [2.7] n/a: no Nat/Int arithmetic goal.
- [2.8] tried aesop, no progress.
- [2.9] n/a: no numerical computation/cast goal.
- [2.10] n/a: symbolic arbitrary-semiring equality, no finite decidable computation.
- [2.11] n/a: no denominators or field structure.
- [2.12] n/a: no ring-ending proof/hypothesis combination.
- [2.13] n/a: no symmetric case branches.
- [2.14] n/a: no calc chain.
- [2.15] original already shared simp_all across induction goals; final composition removes all subgoals.
- [3.1] n/a: no erw.
- [3.2] n/a: no legacy analysis tactic.
- [3.3] n/a: no omega.
- [3.4] n/a: no rcases/rfl substitution.
- [3.5] considered, no attribute addition: public attributes/normal form preserved as requested.
- [3.6] original already unsqueezed simp_all; replaced by direct terminal simp.
- [3.7] n/a: no maxHeartbeats option.

## Validation and gates

Actual `/Users/ramin/.elan/bin/lake build Roth.Taylor`: exit 0, target built in 7.9 seconds, 1439 jobs. Only preserved copyright-header warnings in Taylor and replayed dependencies.

Complete native `lean_diagnostic_messages` on the live file: success=true, partial=false, timed_out=false, failed_dependencies=[]; only line-1 copyright warning. No target error/warning/sorry.

Isolated native run_code importing only Roth.Box and Roth.HasseDeriv recreated translation and verified the original theorem shape with the chosen proof; standard axioms only. Its compact scratch lines had long-line warnings, not source warnings. Stronger exact pre-target check: `/private/tmp/taylor-eval-pretarget.lean` contains the actual source prefix before this target plus the original-type theorem and new proof, with no import of Roth.Taylor or target availability. `/Users/ramin/.elan/bin/lake env lean /private/tmp/taylor-eval-pretarget.lean` exited 0, printed exact type at format.width 100, and axioms `[propext, Classical.choice, Quot.sound]`. Baseline snapshot `/private/tmp/taylor-eval-before.lean`; diff compared against it is exactly the two changed target lines.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | actual module build exit 0 |
| definition_protected | pass | no def/abbrev changes |
| theorem_statement_protected | pass | declaration line unchanged; only synonymous lambda arrow in conclusion; original type independently checked |
| structure_gate | pass | one proof line, no conjunction/branches |
| naming_gate | pass | mathematical snake_case; no forbidden pattern |
| line_packing_gate | pass | two measured rows, both ok |
| inequality_orientation_gate | pass | no reversed inequality occurrence |

Overall: pass. Parent owns subsequent full-project build, separate post-build LeanEval, commit and push. This worker does not claim those later gates.

## Required phase checklist

- [✓] Step 1 — reference docs read.
- [✓] Step 2 — all 24 audit items reported.
- [✓] Step 2.5 — all five search methods reported honestly.
- [✓] Step 2.6 — every parameter and literature/generalisation status reported.
- [✓] Step 2.7 — every signature line measured.
- [✓] Step 2.8 — inequality table emitted.
- [✓] Step 3 — all 42 rules given statuses.
- [✓] Step 4 — one-tactic/library-composition comparison completed.
- [✓] Step 5a — complete clean target LSP; preserved header warning noted.
- [✓] Step 5b — diff gates and actual module build passed.
- [✓] Step 6a — no renames required, sidecar untouched.

Rules applied: strategy-level direct composition/simp; lambda style. Comments preserved: existing docstring unchanged, no inline comments. Renames queued: none. Refactoring needed: none within authorized scope.
