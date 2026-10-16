# MvPolynomial.taylor_map — Phase 4

Target: `Roth/Taylor.lean:151–153` (original task baseline 169–171). Before/after: 3/3 lines, zero lines saved. Replaced polynomial induction with the evaluation-map naturality law; changed the mathematical lambda arrow to `↦`. API, visibility, docstring, imports and header preserved. Frozen source SHA256: `d4a821b4ee428a5e8b052cb7a6cd0a62a9830b3fdb5a3d78557b86bd29d2dd74`. Source ownership returned to parent immediately after verification.

Read lean4 and mathlib-quality skills, full worker contract, golfing-rules, proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates, and applicable style-rules sections. No naming defect requiring the optional naming reference.

## Audit (24 items)

1. LINT: complete LSP reports no target warning/error; existing file-header warning preserved.
2. HAVE SCAN: none.
3. SET_OPTION: none in target; no limits added.
4. SIMP SQUEEZE: original terminal simp_all replaced by terminal unsqueezed simp.
5. NAMING: taylor_map is descriptive snake_case; no forbidden abbreviation/pattern.
6. LINE PACKING: measured table below, both lines pass.
7. BY PLACEMENT: end of conclusion line.
8. FORMAT: correct indentation; lambda ↦ applied; no blank line inside declaration.
9. COMMENTS: no body comments; existing two-line docstring preserved verbatim.
10. DOCSTRING: existing sentence states coefficient-ring compatibility and cites source.
11. VISIBILITY: preserve public API under task contract.
12. STRUCTURE: one-line proof, no conjunction or long branches.
13. MATHLIB: map_eval₂ directly proves naturality; five-method results below.
14. JUNK DEF: n/a, theorem.
15. EXISTS LEMMA: n/a, equality theorem.
16. SHOW vs CHANGE: neither present.
17. PUSH_NEG: none.
18. GENERALISE: per-parameter analysis below; no signature change.
19. INEQUALITY: zero occurrences, table below.
20. NORMAL-FORM: translation of mapped polynomial rewritten to map of translation; coherent naturality form.
21. SYNTAX-GEN: current bundled ring hom f is appropriate; arbitrary substitution version already map_eval₂.
22. IMPORT-FANOUT: no new import.
23. CASTS: 0 dropped / 0 cross-type / 0 load-bearing casts in diff.
24. INSTANCE-NAME: n/a, theorem, no instance declarations.

Issues found/fixed: induction unnecessarily reproves naturality; lambda style. Both fixed. No substantive change applied.

## Mathlib search-status

| Method | Query | Evidence |
|---|---|---|
| A Lean-Finder | MvPolynomial evaluation commutes with mapping coefficients | map_eval₂; eval_map; eval₂_eq_eval_map |
| B Loogle | MvPolynomial.eval₂, MvPolynomial.map | eval₂_map; eval_map; eval₂_eq_eval_map |
| C LeanSearch | MvPolynomial evaluation commutes with coefficient ring homomorphism map eval2 | eval₂Hom_map_hom; map_eval₂; eval₂_map_comp_C |
| D source search | eval₂.*map / map.*eval₂ / eval₂_map | Eval.lean:365 map_eval₂ and neighboring composition laws; inspected definitions |
| E local name | map_eval₂ | index unavailable; fallback result map_eval; direct source and compiled specialization verify map_eval₂ |

Auxiliary variants: map_eval₂Hom, hom_eval₂, eval₂_comp_left/right, eval₂_map_comp_C. Common-equivalents table: no matching topology/finiteness bucket. Found a more general substitution naturality theorem; use it in the existing translation API. Compiled exact-original-statement specialization validates the match. No claim of mathlib absence. `exact?` and `apply?` each reached default 200000 heartbeats; no limits raised.

Six strict rules: generic mathlib law used directly; all five search routes attempted; auxiliary variants checked; no custom predicates; API deletion is outside authorized scope; documentation preserved rather than editing the module docstring. Potential wrapper deletion is deferred to parent/user review under the explicit API-preservation contract; the generic substitution law does not mention the project-specific taylor definition.

## Generalisation status

| Parameter | Class | Used as | Mechanical candidates / result |
|---|---|---|---|
| σ : Type* | type variable | variable index | Drop would leave polynomial and α indices unbound; already universe-polymorphic. |
| R : Type* | type variable | source coefficients | Drop would leave f, α, P unbound; already universe-polymorphic. |
| CommSemiring R | typeclass | source taylor and map API | Drop / Semiring parent blocked by taylor requiring CommSemiring; no local weakening of this theorem's type. |
| S : Type* | type variable | target coefficients | Drop would leave f target unbound; already universe-polymorphic. |
| CommSemiring S | typeclass | target taylor | Drop / Semiring parent blocked by taylor requiring CommSemiring; no local weakening of this theorem's type. |
| f : R →+* S | structure value | coefficient homomorphism on both sides | Drop leaves f unbound. Unbundling to a function changes the public API and loses required map laws. |
| α : σ → R | structure value | arbitrary translation | Drop leaves α unbound; no point-local/strict hypothesis to weaken. |
| P : MvPolynomial σ R | structure value | arbitrary polynomial | Drop leaves P unbound; no narrower concrete coefficient/index restriction. |

No proposition or decidability hypotheses. Mechanical drop checks here are dependency checks, not claimed successful compiled weakenings. An isolated attempted Semiring probe via lean_run_code encountered stale-import rejection, so no experimental weakening is claimed verified; the definition signature itself establishes the obstruction. No live signature changed. Inversion check: translation is a specialization of arbitrary substitution; that abstraction already exists as map_eval₂. No new abstraction needed.

## Public literature search

Queries: `polynomial evaluation coefficient homomorphism naturality generalization commutative semiring`; `site.stacks.math.columbia.edu polynomial ring universal property`; `site.ncatlab.org polynomial ring semiring universal property`.

Relevant retrieved hits recorded: [nLab universal construction](https://ncatlab.org/nlab/show/universal%2Bconstruction), [nLab polynomial](https://ncatlab.org/nlab/show/polynomial), [Stacks conormal modules](https://stacks.math.columbia.edu/tag/04EA); further results [nLab semiring](https://ncatlab.org/nlab/show/semiring), [nLab rig](https://ncatlab.org/nlab/show/rig), [polynomial ring](https://en.wikipedia.org/wiki/Polynomial_ring). These describe polynomial algebras by the universal property and support the arbitrary-substitution interpretation. The Stacks hit is contextual, not a stronger Taylor statement. Search also returned ProofWiki evaluation homomorphism, Algebraic Requirements, and semiring-semantics material; no extra mathematical conclusion was taken from those hits. ChatGPT math MCP: unavailable in tool inventory. No literature-driven stronger local hypothesis weakening identified; semirings and arbitrary index universes are already supported.

## Line packing

Compiled `#check @taylor_map` at format.width 100:

```lean
@taylor_map : ∀ {σ : Type u_3} {R : Type u_4} [inst : CommSemiring R] {S : Type u_5} [inst_1 : CommSemiring S]
  (f : R →+* S) (α : σ → R) (P : MvPolynomial σ R), (taylor fun j => f (α j)) ((map f) P) = (map f) ((taylor α) P)
```

| Signature line | Codepoints | Next token | Arithmetic | Action |
|---|---:|---|---|---|
| 151 | 98 | taylor (6) | 98 + 1 + 6 = 105 > 100 | ok |
| 152 | 65 | none: proof follows | n/a | ok |

## Inequality scan

| Location | Original | Rewrite | Rename |
|---|---|---|---|
| Entire signature and inherited hypotheses | no ≥ or > inequality | n/a | no _ge_ or _gt_ name |

## Golfing rule pass

- 1.1 n/a: no by-exact wrapper.
- 1.2 n/a: no by-rfl.
- 1.3 n/a: no rw/exact chain.
- 1.4 n/a: no simp/exact chain.
- 1.5 n/a: no trailing rfl.
- 1.6 n/a: no constructor.
- 1.7 n/a: no apply/exact.
- 1.8 n/a: no contradiction.
- 1.9 no eta reduction: lambda applies f to α j, not just j; ↦ style applied.
- 1.10 n/a: no have.
- 1.11 n/a: no apply/intro.
- 1.12 n/a: no show.
- 1.13 n/a: no projections/have.
- 1.14 n/a: no rw.
- 1.15 n/a: no terminal simp only.
- 1.16 n/a: simp is terminal.
- 1.17 n/a: no eligible composed term.
- 1.18 n/a: no trailing tactic argument parentheses.
- 1.19 n/a: no push_neg.
- 1.20 n/a: not existential helper.
- 2.1 tried grind: failed.
- 2.2 n/a: no retained grind.
- 2.3 direct terminal simp using map_eval₂ succeeds; removes induction.
- 2.4 n/a: no analytic function property.
- 2.5 n/a: no positivity goal.
- 2.6 n/a: no inequality.
- 2.7 n/a: no Nat/Int arithmetic goal.
- 2.8 tried aesop: failed, no progress.
- 2.9 n/a: no numeric/cast goal.
- 2.10 n/a: arbitrary semiring polynomial equality is not finite computation.
- 2.11 n/a: no denominator.
- 2.12 n/a: no ring-ending proof/hypothesis combination.
- 2.13 n/a: no symmetric cases.
- 2.14 n/a: no calc.
- 2.15 original induction <;> simp_all replaced wholesale by simp; no remaining branches.
- 3.1 n/a: no erw.
- 3.2 n/a: no continuity/measurability.
- 3.3 n/a: no omega.
- 3.4 n/a: no rcases.
- 3.5 no attributes added: normal-form/API change requires separate review.
- 3.6 original simp_all already unsqueezed; replaced with direct simp.
- 3.7 n/a: no limit override.

Step-back reflection: translation is evaluation at X + C α, so coefficient-map compatibility is exactly evaluation naturality. Direct terminal simp is clearer than rediscovering that law by induction; no helper or term-mode plumbing is needed.

## Verification and gates

- Native multi_attempt: proposed simp closed with no goals/diagnostics.
- Native complete-file diagnostics after edit: success=true, partial=false, timed_out=false; only pre-existing header warning at L1.
- `/Users/ramin/.elan/bin/lake build Roth.Taylor`: exit 0, 1439 jobs, Taylor built (17s). Existing Box/HasseDeriv/Taylor header warnings retained.
- Exact-prefix isolated test `/private/tmp/Taylor-decl13-probe.lean`: includes every original line before target, original target statement (including original arrow), new proof; `lake env lean` exit 0. Axioms exactly propext, Classical.choice, Quot.sound.
- `lean_run_code` importing Taylor returned stale-import failure, not counted as validation. The exact-prefix compiler test and complete live LSP supplied independent validation.
- Diff against `/private/tmp/Taylor-decl13-before.lean`: exactly the lambda and proof lines; no collateral edits.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | actual Roth.Taylor exit 0 |
| definition_protected | pass | no def/abbrev edited |
| theorem_statement_protected | pass | only syntax-equivalent lambda arrow; original type compiled |
| structure_gate | pass | 1 proof line, no conjunction/branches |
| naming_gate | pass | descriptive snake_case |
| line_packing_gate | pass | measured rows above |
| inequality_orientation_gate | pass | zero inequalities needing reversal |

Overall: pass. Full-project build and separate LeanEval are parent-owned; both subsequently exited 0 (sessions53057 and18619). No Git operations. No new sorry/axiom/native_decide. Renames queued: none. Comments preserved: original docstring; no body comments present.

Refactoring needed: parent/user may consider whether to retain the named translation API or delete this specialization in favor of map_eval₂; no deletion authorized/applied. No source change required for the present proof cleanup.

## Phase checklist

- [x] Step 1: references read.
- [x] Step 2: all 24 audit items recorded.
- [x] Step 2.5: five-method search block.
- [x] Step 2.6: per-parameter generalisation and public literature block, limitations explicit.
- [x] Step 2.7: every signature-line width measured.
- [x] Step 2.8: inequality table.
- [x] Step 3: all 42 rule statuses.
- [x] Step 4: strategy reflection.
- [x] Step 5a: complete live diagnostics, only preserved header warning.
- [x] Step 5b: diff and build gates.
- [x] Step 6a: no rename required.

Parent resolution: retain the named public translation API under the explicit user contract. The speculative wrapper-deletion suggestion is closed without implementation; it is not a pending proposal or required Phase5 refactor.
