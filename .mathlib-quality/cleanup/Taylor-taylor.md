# `MvPolynomial.taylor` — declaration cleanup

Source: `Roth/Taylor.lean`, lines 36–37; before 2 lines, after 2 lines, saved 0.
Source frozen SHA256: `91e0b1f92db86dacca1c06b0ae8c3e87793d5a27ffafc3070db8074caa2d40ae`.
Only worker source edit: mathematical lambda `fun j =>` → `fun j ↦` on line 37.
Baseline snapshot: `/private/tmp/roth-taylor-taylor-before.lean`; earlier file-owner edits are excluded from this worker diff.

## Step 1 — references

Read lean4 and mathlib-quality skills, the complete supplied worker contract, golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, cleanup-gates.md, naming-conventions.md, and relevant style-rules.md sections (formatting, comments/docs, definitions, syntax, visibility, signatures, normal forms, API transparency/completeness). Read the complete target file immediately before the context-anchored patch. No whole-file rewrite.

## Step 2 — full audit

1. **LINT:** no declaration warnings. Final complete LSP has only the preexisting L1:2 copyright warning, explicitly accepted unchanged by the user.
2. **HAVE SCAN:** n/a: no `have` in this term definition.
3. **SET_OPTION:** none in declaration or worker diff.
4. **SIMP SQUEEZE:** n/a: no tactics or simplification calls.
5. **NAMING:** `taylor` is a descriptive lowerCamelCase data-definition name matching the univariate mathematical terminology. No forbidden abbreviation, numbered scheme, auxiliary-number, single-letter public name, or inequality suffix. No rename warranted.
6. **LINE PACKING:** single 81-codepoint signature line, including conclusion and `:=`; table below. No signature continuation can be packed.
7. **BY PLACEMENT:** n/a: term-mode data construction, no `by`.
8. **FORMAT:** body has two-space indentation; no blank internal lines or trailing spaces. Replace mathematical lambda arrow with `↦`. No `haveI`/`letI` introduced.
9. **COMMENTS:** no inline proof comments; declaration docstring preserved byte-for-byte.
10. **DOCSTRING:** existing one-sentence translation description plus source citation accurately describes the operation; preserve it.
11. **VISIBILITY:** retain public definition: it anchors the entire translation API and is directly used by `Roth/Index.lean`.
12. **STRUCTURE:** one-line term body; no conjunction or branches; no helper extraction warranted.
13. **MATHLIB:** five-method results below; already directly uses the generic `MvPolynomial.aeval` constructor. The univariate Taylor API is a partial analogue, not a replacement of this type.
14. **JUNK DEF:** keep: substantial API (`taylor_apply`, `taylor_X`, `taylor_C`, coefficient/evaluation/composition/map/rename/injectivity results) and downstream Index uses. Satisfies explicit documented exemption for definitions with API and external use.
15. **EXISTS LEMMA:** n/a: data definition, not private single-use existence lemma.
16. **SHOW vs CHANGE:** n/a: neither appears.
17. **PUSH_NEG:** n/a: none.
18. **GENERALISE:** already arbitrary universe-polymorphic index/coefficient types and commutative semiring; compiled weakening/drop probes fail for missing `CommSemiring R`, as detailed below.
19. **INEQUALITY:** zero inequality occurrences; table below.
20. **NORMAL-FORM:** canonical substitution by `X j + C (α j)`, represented as bundled algebra homomorphism. Already normal form; no bridge equivalence needed.
21. **SYNTAX-GEN:** OK: bundled map supports generic map lemmas and function coercion; no more applicable restatement identified.
22. **IMPORT-FANOUT:** n/a: no new import.
23. **CASTS:** 0 dropped / 0 kept cross-type / 0 kept load-bearing: no explicit ascription/coercion in diff; `C` is the mathematical constant-polynomial map.
24. **INSTANCE-NAME:** n/a: not an instance declaration.

Issues found: one lambda style issue. Fixed: one. Refactoring needed: none.

## Step 2.5 — mathlib search status

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | `multivariate polynomial translation substitution X plus constants` | `MvPolynomial.rename_toMvPolynomial`, `MvPolynomial.bind₁_X_right`, `Polynomial.algEquivAevalXAddC_apply`; substitution building blocks/univariate analogue |
| B Loogle | `MvPolynomial.aeval` | `MvPolynomial.aeval`, `aevalTower_id`, `aevalTower_ofId`; already uses direct constructor |
| C LeanSearch | `multivariate polynomial Taylor translation` | HTTP500; unavailable, not a no-hit conclusion; no repeated retry |
| D source rg | `def (taylor\|aeval)`, `MvPolynomial.taylor`, `translate` in MvPolynomial and Polynomial/Taylor source | generic `aeval` at Eval.lean:569; univariate `taylor`, `taylorAlgHom`, `taylorEquiv`; no replacement established |
| E native local name search | `taylor` | source hits include local `MvPolynomial.taylor` API and `Polynomial.taylor`; index unavailable, source results valid but no absence claim |

Auxiliary variants: `aevalTower`, `bind₁`, `taylorAlgHom`, `taylorEquiv`, `algEquivAevalXAddC_apply`, rename/evaluation compatibility. Common-equivalents buckets: none match this polynomial definition.
`#check @MvPolynomial.aeval` compiled and confirms the existing constructor's full type. Generic construction was compiled independently, with `rfl` confirming equality to the old body. We are preserving an established definition, not creating an absence-based replacement; no claim that a mathematical operation is absent from mathlib. No guessed identifier introduced. Rule disposition: reuse `aeval` directly; preserve meaningful definition with API and the user's signature/definition contract; no wrapper theorem or custom predicate added.

## Step 2.6 — generalisation status

| Parameter | Class | Used as | Mechanical candidates considered/tested | Verified? | Result |
|---|---|---|---|---|---|
| `{σ : Type*}` | type variable | variable domain in α and both polynomial types | drop dependency check; universe widening already present | source/type check | retain: removing the type parameter leaves σ unresolved or re-inferred as the same implicit parameter; no restriction to weaken |
| `{R : Type*}` | type variable | coefficient and base scalar type | drop dependency check; universe widening already present | source/type check | retain: required in α, C and both polynomial types; already independent universe |
| `[CommSemiring R]` | typeclass | required by polynomial/algebra-hom type and aeval | drop entirely; weaken to `[Semiring R]` | actual isolated compiler probes | both fail `failed to synthesize ... CommSemiring R` at the type; keep |
| `(α : σ → R)` | structure value | translated constant in every coordinate | drop dependency check; point-localisation/strict weakening inapplicable | source/type check | retain: supplies the translation data itself; replacing it by fixed data changes mathematical operation |

No proposition, order, finiteness, decidability, topology, or nonzero hypotheses. No larger concrete coefficient field to abstract. Inversion check: n/a to proof extraction—this is the actual substitution data definition, already parameterized by arbitrary types/semiring, with no unfolded concrete-witness proof. Big-change candidates: none warranted. Generalized codomain/substitution is already `aeval`; changing the domain-specific translation API would lose its purpose.

### Literature status

Web search performed: `multivariate polynomial Taylor translation commutative semiring generalization`. Top three returned hits were [mathlib3 Taylor documentation](https://leanprover-community.github.io/mathlib_docs/data/polynomial/taylor.html), [FormalBook mirror](https://firsching.ch/FormalBook/docs/Mathlib/Algebra/Polynomial/Taylor.html), and [FLT mirror](https://imperialcollegelondon.github.io/FLT/docs/Mathlib/Algebra/Polynomial/Taylor.html). The authoritative current [mathlib4 Taylor documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Taylor.html) was then opened: univariate translation has a linear-map version over semirings and an algebra-hom version over commutative semirings. This supports retaining the current bundled type rather than dropping commutativity. Local `clean.tex` lines501–507 state the real finite-variable expansion, and lines547–549 define `P_α(X)=P(X+α)`; current definition already abstracts beyond those restrictions. ChatGPT math MCP: n/a, no matching callable tool discovered. No literature-driven API change warranted.

## Step 2.7 — line packing

Reference: n/a for a definition under the worker contract; nevertheless `#check` verified independently at `format.width 100`:

```lean
@MvPolynomial.taylor : {σ : Type u_1} →
  {R : Type u_2} → [inst : CommSemiring R] → (σ → R) → MvPolynomial σ R →ₐ[R] MvPolynomial σ R
```

| Sig line | Chars | Next signature token | Arithmetic | Action |
|---|---:|---|---|---|
| 36 | 81 | none: body follows `:=` | n/a: no next signature line | ok |

Same table before/after: signature byte-identical. Body is29codepoints after arrow edit; merging the whole term would be81+1+27=109, exceeding100. No repack needed.

## Step 2.8 — inequality scan

| # | Location | Original | Rewrite | Lemma rename? |
|---|---|---|---|---|
| — | signature and parameters | n/a: zero ≥/> inequalities | none | none: name has no `_ge_`/`_gt_` |

Lambda syntax `=>` in the old body is not an inequality and has independently been changed to `↦`.

## Step 3 — every golfing rule

The target is a one-line term-mode data constructor, not a tactic proof. Tactic automation cannot replace its value with arbitrary inhabitance; no invented failed tactic trials are reported.

- 1.1 by-exact: n/a, no wrapper.
- 1.2 by-rfl: n/a, no proof.
- 1.3 rw+exact: n/a, no tactics.
- 1.4 simp+exact: n/a, no tactics.
- 1.5 trailing rfl: n/a, no tactics.
- 1.6 constructor chain: n/a, no conjunction/structure tactic construction.
- 1.7 apply+exact: n/a, already direct term application.
- 1.8 by_contra: n/a, no negation proof.
- 1.9 eta reduction: inspected; j occurs in both X j and α j, so not an eta-redex; retain explicit lambda and normalize arrow.
- 1.10 single-use have: n/a, none.
- 1.11 apply+intro: n/a, none.
- 1.12 redundant show: n/a, none.
- 1.13 have projections: n/a, none.
- 1.14 merge rw: n/a, none.
- 1.15 terminal simp: n/a, none.
- 1.16 nonterminal simp: n/a, none.
- 1.17 dot notation: n/a, aeval is constructor with variable assignment, no receiver improvement.
- 1.18 parentheses: already `aeval fun j ↦ ...`, no outer parentheses to remove.
- 1.19 push_neg: n/a, none.
- 1.20 existence helper: n/a, not such a lemma.
- 2.1 grind: n/a, data definition whose exact value must be preserved.
- 2.2 pre-grind tactics: n/a, none.
- 2.3 simpa: n/a, no simplification chain.
- 2.4 fun_prop: n/a, no analytic property goal.
- 2.5 positivity: n/a, no order goal.
- 2.6 gcongr: n/a, no inequality goal.
- 2.7 lia/omega: n/a, no arithmetic proposition.
- 2.8 aesop: n/a, exact data construction, no logical proof.
- 2.9 norm_num/norm_cast: n/a, no numeric/cast proof.
- 2.10 decide: n/a, result is algebra-hom data, not decidable proposition.
- 2.11 field_simp/ring: n/a, no equality proof or denominators.
- 2.12 linear_combination: n/a, no ring proof/hypotheses.
- 2.13 wlog: n/a, no branches.
- 2.14 calc: n/a, none.
- 2.15 multi-goal closure: n/a, no goals.
- 3.1 erw: n/a, none.
- 3.2 continuity/measurability: n/a, none.
- 3.3 omega→lia: n/a, none.
- 3.4 rcases rfl: n/a, none.
- 3.5 automation attributes: n/a, data definition already has surrounding simp API; unfolding globally would change normal forms.
- 3.6 simp_all: n/a, none.
- 3.7 heartbeat options: n/a, none.

## Step 4 — reflection

The single expression already constructs the desired map through mathlib's universal evaluation map. Replacing it with tactics (`exact?`, `apply?`, `grind`, etc.) would replace a transparent mathematical definition with proof-search-driven data, with no simplification benefit. No have blocks, redundant proof steps, ugly API plumbing, or alternative shorter value-preserving strategy identified. Keep the constructor and fix its arrow only.

## Step 5 — verification and gates

Actual experiments: initial native scratch imports twice reported out-of-date imports. A baseline module refresh then a second build of the final source resolved this. A scratch data example missing `noncomputable section` failed with the expected noncomputability error, and one scratch line was too long; both were corrected in scratch only. The final scratch returned success=true, timed_out=false with info-only #check/axiom output. Its `rfl` example compares the final definition with the exact old ASCII-arrow expression. Its independent noncomputable data example compiles the construction. No scratch definitions/options entered source.

Final `/Users/ramin/.elan/bin/lake build Roth.Taylor` exited0,1439jobs, target14s; log `/private/tmp/roth-taylor-taylor-module-final.log`. Final native `lean_diagnostic_messages` returned success=true, partial=false, timed_out=false, failed_dependencies=[]; only accepted copyright warning. `#print axioms MvPolynomial.taylor`: `[propext, Classical.choice, Quot.sound]`.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | final-source build exit0 as above |
| definition_protected | pass | def header/type byte-identical; sole body syntax arrow change; old-body equality by rfl succeeds |
| theorem_statement_protected | pass | no theorem changed in worker snapshot diff |
| structure_gate | pass | one-line body, no conjunction or branches |
| naming_gate | pass | descriptive data name; no forbidden patterns |
| line_packing_gate | pass | complete signature table, no repack rows |
| inequality_orientation_gate | pass | complete scan, zero reversed inequalities |
| isolated/type/axiom | pass | final native snippet clean; old value rfl; standard axioms only |
| comment preservation | pass | existing docstring unchanged; no inline comments present |
| source scope | pass | snapshot diff only line37 arrow; no sorry/admit/axiom/scaffolding added |

Overall: pass. Full project and LeanEval dependent builds are the file owner's publication gates, not run by this leaf.

## Step 6 — result and checklist

Before2lines; after2lines; saved0. Audit issues1; fixed1; deferred0. Rules applied: mathematical-lambda style (eta review1.9 concluded no reduction). Renames queued:none. Comments preserved: declaration docstring1/1; inline comments0/0. Refactoring needed:none.

- [x] Step1: mandatory references read.
- [x] Step2: all24audit items reported.
- [x] Step2.5: allfive search methods accounted for, unavailability distinguished from absence.
- [x] Step2.6: every parameter accounted for; actual typeclass probes; public literature search.
- [x] Step2.7: complete width table.
- [x] Step2.8: complete inequality scan.
- [x] Step3: all42golf rules have concrete status.
- [x] Step4: strategy reflection.
- [x] Step5a: complete clean LSP except accepted header.
- [x] Step5b: all gates pass against final exact source.
- [x] Step6a: no rename required; sidecar untouched.

No source edits after SOURCE FROZEN; only this report was written thereafter. Git and shared logs untouched by this leaf.
