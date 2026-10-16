# Phase 4 — Roth.normOne_det_le

Current amendment: the user explicitly approved the unused public-binder removals on
2026-10-16. See [approved amendment audit](CoeffNorm-api-amendment.md) for the current
source, types, warning count and verification. The original audit below records its
historical checkpoint and remains unchanged.

Scope: one declaration in `Roth/CoeffNorm.lean`, original L114–124, final L114–123.
Before 11 declaration lines / 8 body lines; after 10 / 7; saved one line.
Public signature and original docstring are byte-identical. The only source changes are
inside this proof. No other source, callers, Git state, shared logs, instances, or definition
values were changed by this worker.

SOURCE FROZEN: `539842bb50df433db0d3ee8d8f366892b352427103407526700baa23ae5cd33f`.
Ownership revoked after this hash; all subsequent operations were reports/probes/builds.
The same whole-file hash was checked again after final verification.

## Step 1 — references and baseline

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md. Also read full mathlib-quality and lean4
skills, the full worker contract, style-rules.md, naming-conventions.md, and
mathlib-review-stages.md. Resolved single-declaration substitutions are this file, name,
and range. Baseline inherited from the owner: full build green, separate LeanEval session
61558 exit 0, complete file LSP without errors. A fresh native baseline diagnostic call
was complete (`partial=false`, `success=true`, no failed dependencies): six warnings,
zero errors. Final diagnostic calls preserve exactly those six warning categories.

The proof expands the determinant, uses the triangle inequality, removes each sign by
its two possible integer-unit values, applies submultiplicativity and the entry bounds,
and counts permutations. The local source `.mathlib-quality/references/clean.tex`
L470–496 supplies precisely this argument; it says “The signs have absolute value $1$”.
Its displayed product equality is stronger than submultiplicativity warrants; the Lean
proof correctly uses an inequality at that step.

## Step 2 — full audit (all 24 items)

1. LINT: target has unused `hC` and unused-in-type `[DecidableEq σ]`. Both remain named
   and unsuppressed because their proposed removal awaits scoped approval. File header
   and the three other DecidableEq warnings are unchanged.
2. HAVE SCAN: no `have` in the original or final proof; none to inline.
3. SET_OPTION: no declaration option or raised elaboration limit.
4. SIMP SQUEEZE: original `simp [Fintype.card_perm]`, sign-case `simp [h, normOne_neg]`,
   and `(by simp)` are terminal. Final terminal `simpa [h, normOne_neg]` absorbs the
   sign rewrite. No nonterminal bare simp and no squeezed terminal simp remain.
5. NAMING: `normOne_det_le` names the bound for the existing `normOne` definition;
   contains no forbidden abbreviation, numeric scheme, auxiliary suffix, or reversed
   inequality name. No rename is needed or queued.
6. LINE PACKING: measured every signature line below. All breaks exceed 100 when the
   next complete binder/conclusion is joined; body maximum is 95 characters.
7. BY PLACEMENT: `:= by` ends the statement line; nested `(by simp)` is term syntax.
8. FORMAT: ordinary lambdas changed from `=>` to `↦`; two-space proof indentation,
   natural calc continuations, no internal blank lines, no trailing whitespace,
   no `haveI`/`letI`, no tactic-semicolon chain. `<;>` deliberately shares sign cases.
9. COMMENTS: no proof comments were present; none deleted. Original docstring preserved.
10. DOCSTRING: existing public result describes the determinant estimate and cites §3;
    preserved under the explicit API/docstring lock.
11. VISIBILITY: main public result used for determinant coefficient bounds; kept public.
12. STRUCTURE: seven body lines, below the headline limit 15; no conjunction;
    each sign branch is the same two-line terminal proof. No helper extraction needed.
13. MATHLIB: all five searches below; `Matrix.det_le` is a partial match requiring
    multiplicativity, so the explicit submultiplicative argument is retained.
14. JUNK DEF: n/a — theorem, no definition introduced or changed.
15. EXISTS LEMMA: n/a — no existential helper or witness wrapper.
16. SHOW vs CHANGE: removed the intermediate `rw [show ...]` entirely. Direct sign
    elimination followed by `simpa` proves the inequality itself; no `change` needed.
17. PUSH_NEG: n/a — no negative proposition normalization tactic.
18. GENERALISE: every parameter audited and drop-probed below; two verified candidates
    deferred to the existing pending proposal; no public API change applied.
19. INEQUALITY: complete occurrence table below; no `≥`/`>` notation or `_ge_`/`_gt_` name.
20. NORMAL-FORM: standard determinant on `Matrix`, finite products/sums, and `≤` bound;
    already in the useful normal form for this project's norm. No new equivalence API.
21. SYNTAX-GEN: removing `hC` would simplify application, but is the pending API proposal.
    Quantifying hM over all entries naturally covers every permutation product.
22. IMPORT-FANOUT: n/a — no import added, removed, or changed.
23. CASTS: 0 dropped / 0 explicit cross-type casts / 0 load-bearing ascriptions in diff.
    Existing implicit integer-sign and factorial coercions remain inferred.
24. INSTANCE-NAME: n/a — no instance declaration or instance-name edit.

Issues fixed: redundant intermediate equality rewrite, ordinary-lambda syntax, one proof line.
Refactoring needed: only the existing pending decisions on `hC` and `[DecidableEq σ]`;
no extra rename, helper, generalized norm framework, or cross-declaration redesign proposed.

## Step 2.5 — mathlib search-status

| Method | Actual query / search | Findings |
|---|---|---|
| A Lean-Finder | determinant absolute value bound factorial power entry bound | Matrix.det_le, Matrix.det_sum_smul_le, Matrix.det_sum_le |
| B Loogle | `Matrix.det, _ ≤ _` | degree/charpoly and algebraic determinant results; no applicable normOne estimate |
| C LeanSearch | determinant bounded by factorial times entry bound power | Matrix.det_le plus sum variants |
| D source | `det.*(le\|norm)`, `norm.*det`, `abs.*det`, `det.*abs` in Matrix and Analysis/Matrix | AbsoluteValue.lean L42–50; direct source inspected |
| E local names | `det_le` | Matrix.det_le and project normOne_det_le; positive hits valid despite index warming |

Auxiliary variants inspected: det_sum_le, det_sum_smul_le, det_apply, det_apply',
absolute-value map_prod/map_units_int_smul, finite sum/product inequality APIs.
Common-equivalents table: no relevant discrete/finite/bornology replacement; this is a
submultiplicative polynomial coefficient norm estimate.

Concluded: partial match `Matrix.det_le`; retain local proof built on Matrix.det_apply',
Finset.sum_le_sum, Finset.prod_le_prod₀, and Fintype.card_perm. `AbsoluteValue` requires
exact multiplicativity, whereas this norm only has `normOne_mul_le`; constructing that
structure would require an unjustified stronger property. This is not a thin 1–3-call
wrapper. No API-extraction signals remain: no wrapper round-trip, manual typeclass
plumbing, repeated casts, or definitional-equality rewrite.

Six-rule disposition: (1) no wrapper introduced; (2) all searches performed and actual
nonself automation probes attempted below, without claiming exhaustive mathematical
absence; (3) auxiliary variants searched; (4) no custom predicate replacing a class;
(5) no exact equivalent found to delete; (6) mathlib dependencies documented here,
while the original module documentation is preserved by the explicit owner lock.

## Literature status and optional redesign closure

Web query 1: `determinant bound factorial n C^n Leibniz generalization normed ring`.
Top three returned hits:

1. [Determinant](https://en.wikipedia.org/wiki/Determinant): standard Leibniz formula and
   determinants over commutative rings.
2. [Oliver Knill, complex.pdf](https://legacy-www.math.harvard.edu/~knill/graphgeometry/papers/complex.pdf):
   discusses extensions of Leibniz expressions and loss of determinant identities.
3. [Leibniz formula](https://en.wikipedia.org/wiki/Leibniz_formula_for_determinants):
   permutation expansion underlying the estimate.

Web query 2: `"determinant" "n!" "bound" site:edu Leibniz norm`.
Top three returned hits:

1. [Knill, Fundamental Theorems](https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf):
   Leibniz expression over more general rings.
2. [Conway–Sloane lattice bound](https://citeseerx.ist.psu.edu/document?doi=1682d2469abaf090dbb5a4d5d95943bc5ac65167&repid=rep1&type=pdf):
   irrelevant lattice minimum result, excluded.
3. [Knill, updated copy](https://abel.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf):
   duplicate general-determinant discussion.

These search hits do not establish a new theorem for normOne. The actual proof source
is the project's clean.tex §3; the generalization inference is that any submultiplicative
seminorm with negation invariance permits the same finite expansion argument. General
finite index types and abstract seminormed commutative rings are possible redesigns,
but no concrete downstream application needs that API in this task; closed without
extra abstraction. ChatGPT math MCP: n/a — no such callable tool available in metadata.
The literature does not justify noncommutative Matrix.det, nor multiplicative normOne.

## Step 2.6 — every parameter, mechanical weakening and probes

All scratch files are under `/private/tmp/d13-*`; production signature untouched.
Actual fresh CLI command: `/Users/ramin/.elan/bin/lake env lean <probe-file>`.
Drop variants insert `classical` and set `autoImplicit false` to avoid accidental
replacement of removed binders by auto-implicit ones. Each variant independently
reproves the result rather than invoking normOne_det_le.

| Parameter | Class / use | Mechanical candidates examined and actual verification | Result |
|---|---|---|---|
| `{σ : Type*}` inherited | type-variable; coefficient-polynomial type | drop σ: d13-drop_sigma exit1, unknown σ; universe polymorphism already in signature and final exact-type assignment | retained; no parent structure, point or strictness weakening applies to a type parameter |
| `[DecidableEq σ]` | decidability; supplies existing product theorem | drop plus classical: d13-drop_decidable exit0; also drop_both exit0 | verified candidate, retained pending approval; DecidableEq has no weaker parent relevant here |
| `{l : ℕ}` | index-size value in Fin l, factorial, exponent | drop: d13-drop_l exit1, unknown l and l.factorial | retained; replacing Fin l by arbitrary Fintype is a public restatement, optional redesign closed |
| `(M : Matrix ...)` | structure-value; entries and determinant | drop: d13-drop_M exit1, unknown M/M.det | retained; no hypothesis weakening or point-localization applies to the matrix value |
| `{C : ℝ}` | bound value in entry hypothesis and conclusion | drop: d13-drop_C exit1; C resolves to MvPolynomial.C, producing LE/OfNat failures and ℝ type mismatch | retained; abstract ordered codomain would require changing normOne itself, outside this declaration |
| `(hC : 0 ≤ C)` | proposition; unused | drop: d13-drop_hC exit0; drop_both exit0 | verified candidate, retained pending approval; already weak rather than strict; no parent/point weakening |
| `(hM : ∀ μ ν, normOne (M μ ν) ≤ C)` | proposition; every entry in arbitrary permutation product | drop: d13-drop_hM exit1 at hM; strict→weak inapplicable, already ≤; fixed-point localization cannot bound every matrix entry in every permutation | retained; no bundled conjunction, function regularity, or class-parent weakening applies |

Big-change candidates: drop explicit hC (existing pending proposal); removing DecidableEq
is also explicitly held pending by the owner. No new API proposal or caller edit.
Inversion check: after det_apply', M and C remain throughout the product estimates;
the proof does not unfold a single special witness and then forget its properties.
Abstract seminorm generality is mathematically available but adds a separate interface
without demonstrated caller benefit here; no additional redesign carried forward.

## Step 2.7 — full line-packing table

Actual width-100 command in d13-final.lean: `set_option format.width 100 in #check @Roth.normOne_det_le`.
Output (Lean prints the full explicit type; the diagnostic renderer retains its own wrapping):

```lean
@normOne_det_le : ∀ {σ : Type u_2} [DecidableEq σ] {l : ℕ} (M : Matrix (Fin l) (Fin l) (MvPolynomial σ ℤ)) {C : ℝ},
  0 ≤ C → (∀ (μ ν : Fin l), normOne (M μ ν) ≤ C) → normOne M.det ≤ ↑l.factorial * C ^ l
```

Widths measured as Python Unicode codepoints, including source indentation and `:= by`.
Next-token means complete next binder or complete conclusion, not an isolated punctuation mark.

| Signature line | Characters | Next complete signature token | Arithmetic | Action |
|---|---:|---|---|---|
| 114 | 94 | `{C : ℝ}` (7) | 94 + 1 + 7 = 102 >100 | ok |
| 115 | 60 | `normOne M.det ≤ l.factorial * C ^ l := by` (41) | 60 + 1 + 41 = 102 >100 | ok |
| 116 | 45 | no next signature line | n/a, proof next | ok |

No signature repack required. Final proof lines measure 24, 87, 74, 58, 63, 86, 95.

## Step 2.8 — inequality scan

| Occurrence | Location | Original | Rewrite / rename |
|---|---|---|---|
| 1 | hC, L115 | `0 ≤ C` | already forward; none |
| 2 | hM, L115 | `normOne (M μ ν) ≤ C` | already forward; none |
| 3 | conclusion, L116 | `normOne M.det ≤ l.factorial * C ^ l` | already forward; none |
| prohibited notation | complete signature | no `≥` or `>` | none; name has no `_ge_`/`_gt_` |

## Step 3 — every golfing rule (42 statuses)

| Rule | Status |
|---|---|
| 1.1 by exact | n/a: no by-exact wrapper |
| 1.2 by rfl | n/a: no by-rfl wrapper |
| 1.3 rw + exact | replaced intermediate rw/show plus exact by direct sign-case simpa |
| 1.4 simp + exact | final simpa combines sign normalization with product-bound term |
| 1.5 trailing rfl | n/a: none |
| 1.6 anonymous constructor | n/a: no constructor goal |
| 1.7 apply + exact | n/a: no such chain |
| 1.8 by_contra! | n/a: no contradiction proof |
| 1.9 eta lambdas | existing membership-discarding lambdas are not eta wrappers; converted arrows to ↦ |
| 1.10 single-use have | n/a: no have |
| 1.11 refine + fun | n/a: sum monotonicity already takes lambda directly |
| 1.12 redundant show | removed show equality and its rewrite |
| 1.13 obtain | n/a: no projected pair |
| 1.14 merge rw | n/a: only initial det_apply' rewrite remains |
| 1.15 unsqueeze terminal simp | all terminal simps already unsqueezed |
| 1.16 squeeze nonterminal simp | n/a: none |
| 1.17 dot notation | .trans and .trans_eq already used; retained |
| 1.18 <\| | original <\| became terminal simpa using; final parentheses group trans argument, so removing them changes parsing |
| 1.19 push Not | n/a: no push_neg |
| 1.20 inline existential | n/a: no existential helper |
| 2.1 grind | whole-goal nonself scratch probe at 20000 heartbeats did not close; original proof then compiled |
| 2.2 delete before grind | n/a: no retained grind |
| 2.3 simpa consolidation | applied to both sign cases with same product-bound term |
| 2.4 fun_prop | n/a: no regularity proposition |
| 2.5 positivity | n/a: no free positivity subgoal; product nonnegativity supplied by normOne_nonneg |
| 2.6 gcongr | whole-goal nonself scratch probe did not close; original proof then compiled |
| 2.7 lia / omega | no Nat/Int inequality subgoal; whole-goal omega was actually tried and failed to close |
| 2.8 aesop | nonself scratch attempt exhausted reduced 20000-heartbeat budget; no replacement |
| 2.9 norm_num / norm_cast | n/a: symbolic determinant bound, no concrete computation/cast obligation |
| 2.10 decide | n/a: arbitrary symbolic real inequality, not finite decidable computation |
| 2.11 field_simp; ring | n/a: no denominators; whole-goal ring failed to close |
| 2.12 linear_combination | n/a: final result is inequality; no proof ending ring/ring_nf |
| 2.13 wlog | sign branches have identical normalization, already shared using <;>; no symmetry hypothesis needed |
| 2.14 term calc | three mathematical steps, not two; final bound already uses trans/trans_eq terms |
| 2.15 <;> | applied to the two sign cases |
| 3.1 erw → rw | n/a: no erw |
| 3.2 fun_prop migration | n/a: no continuity/measurability tactic |
| 3.3 omega → lia | n/a: no retained omega; symbolic real norm estimate needs neither |
| 3.4 rcases rfl | sign equation lives in integer-unit cast; named h passed to simp handles both signs directly |
| 3.5 automation attributes | n/a: no reusable normal-form lemma added; public attributes locked |
| 3.6 simp_all | n/a: no simp_all only; terminal simp/simpa sufficient |
| 3.7 remove heartbeat option | n/a: no production option; exploratory lower budget only in /tmp |

Automation evidence: d13-automation.lean uses `fail_if_success solve | tactic` for
rfl, simp, ring, linarith, nlinarith, omega: none closes. Its exact? attempt then reaches
the default 200000-heartbeat limit. d13-auto-extra.lean isolates apply?, grind, aesop,
gcongr into separate declarations; apply? and aesop reach a deliberately *lowered*
20000-heartbeat limit, while grind and gcongr fail to close and the supplied explicit
proofs finish. No timeout-limit increase or scaffolding entered production. Native
multi_attempt was first attempted, bounded/cancelled on stall; a fresh fallback session
returned splice-context errors and was terminated. The successful isolated run_code
probe established the shorter sign proof; its first unrelated error was using the wrong
option pp.width, corrected to format.width in the successful fresh final CLI probe.
Exploratory failed X/support simplification probes were discarded and never edited source.

## Step 4 — reflection

The entire proof is not discharged by the tested general automation. exact?/apply?
were tried without importing the target itself into the search context, so there is no
self-proof contamination; timeout is recorded rather than a false absence claim.
Matrix.det_le cannot apply to a merely submultiplicative norm. A bundled RingSeminorm
interface could support a reusable generic theorem, but would broaden this single-proof
cleanup without a concrete user. Term mode for the full finite expansion obscures the
three inequalities; calc plus direct sign normalization is concise and faithful.
No have block, extra equality, or coercion remains to consolidate. No decomposition flag.

## Step 5a/5b — verification and actual gates

- `/Users/ramin/.elan/bin/lake build Roth.CoeffNorm`, session 95270: exit 0,
  1658 jobs, affected module built in 11s. No full project build run by this worker.
- Final native `lean_diagnostic_messages` on whole file: `partial=false`,
  `success=true`, `timed_out=false`, `failed_dependencies=[]`, zero errors,
  exactly six preserved warnings (header; four DecidableEq; hC).
- Native live goal query on final L123: goals_before=[] and goals_after=[].
- `/Users/ramin/.elan/bin/lake env lean /private/tmp/d13-final.lean`: exit 0.
  Contains exact original-type assignment `:= @Roth.normOne_det_le` and a separate
  theorem re-proving the same statement using the final body, never invoking the target.
  Both print axioms `[propext, Classical.choice, Quot.sound]` only.
- Actual diff against start snapshot: signature byte equality true; source outside target
  equality true; no definition/abbrev changes; no prohibited inequalities; no new sorry,
  axiom, suppression, imports, or options. Source SHA256 remains the frozen value above.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | ✓ pass | actual session 95270 exit0 |
| definition_protected | ✓ pass | no def/abbrev source changes |
| theorem_statement_protected | ✓ pass | signature byte-identical; exact-type assignment compiled |
| structure_gate | ✓ pass | 7 body lines ≤15; no conjunction, sign branches ≤2 lines |
| naming_gate | ✓ pass | no forbidden name component or pattern |
| line_packing_gate | ✓ pass | all three signature rows measured; no repack row |
| inequality_orientation_gate | ✓ pass | full scan; zero prohibited notations |
| comments/docs protected | ✓ pass | no inline comments existed; full original docstring unchanged |
| scope protection | ✓ pass | actual start-snapshot comparison: outside-target text unchanged |

Overall: pass, with the two explicitly pending API candidates preserved.
Renames queued: none. Comments preserved: no inline proof comments present; docstring unchanged.

## Step 6 — required checklist

- [✓] Step 1 — full references read
- [✓] Step 2 — all 24 audit items reported
- [✓] Step 2.5 — five-method search and strict-rule disposition recorded
- [✓] Step 2.6 — every parameter examined, actual drop probes, literature recorded
- [✓] Step 2.7 — every signature line has a measured packing row
- [✓] Step 2.8 — full inequality occurrence scan recorded
- [✓] Step 3 — every one of the 42 golfing rules has a status
- [✓] Step 4 — alternate-strategy and whole-proof reflection recorded
- [✓] Step 5a — complete live-file LSP without errors on frozen source
- [✓] Step 5b — actual module build, original-type assignment, independent reproof, axioms and diff gates
- [✓] Step 6a — rename audit complete; no rename needed or queued
