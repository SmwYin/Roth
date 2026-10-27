---
decl: Roth.approxSet_den_le_finite
file: Roth/Main.lean
line: 73
kind: theorem
visibility: public
verdict: BORDERLINE-needs-human
cost: CHEAP
junk: KEEP
rationale: The stated form is about the project-local approxSet (itself NO-composable) and cannot go upstream as is; its real content, that only finitely many fractions h/q with q at most N lie in a bounded set, is missing from mathlib (mathlib re-derives it inline in Rat.finite_rat_abs_sub_lt_one_div_den_sq), so whether to upstream that generic lemma is a judgment call.
action: Keep in Roth/Main.lean (callers reduction, exists_reduced_approx, LeanEval.isDiophantine_iff); optionally shorten the proof to the compiled Int.tendsto_coe_cofinite plus Finite.biUnion route in evidence/Roth.approxSet_den_le_finite/alt_proof.lean; if the human approves, upstream the generic finite_int_abs_sub_div_lt-style lemma to Mathlib/NumberTheory/DiophantineApproximation/Basic.lean.
---

# Roth.approxSet_den_le_finite

## Inventory entry

### `theorem Roth.approxSet_den_le_finite`
- **Type**: `(α κ : ℝ) (Q₀ : ℕ) : {hq ∈ approxSet α κ | hq.2 ≤ Q₀}.Finite`
- **What**: Only finitely many approximations `(h, q)` of `α` of quality `κ` have denominator `q ≤ Q₀`.
- **How**: Sets `S = ∑_{q=1}^{Q₀} q^{-κ}` and `K = ⌈Q₀ (|α| + S)⌉`, then shows the set lies inside the finset `Icc (-K) K ×ˢ Icc 1 Q₀`. The bound on `|h/q|` uses `abs_sub_abs_le_abs_sub` and `Finset.single_le_sum` (through `linarith`). It then multiplies by `q ≤ Q₀` (`div_le_iff₀`, `mul_le_mul_of_nonneg_left`) and casts back through `Int.le_ceil` and `Int.cast_abs`.
- **Hypotheses**: none.
- **Uses from project**: `Roth.approxSet`
- **Used by**: Roth/Main.lean: `Roth.reduction` (line 124), `Roth.exists_reduced_approx` (lines 170, 182); Roth/LeanEval.lean: `isDiophantine_iff` (line 49).
- **Visibility**: public
- **Lines**: 73–96, proof length 23 lines
- **Notes**: Source: clean.tex §6 l.1175 ("For a fixed upper bound on q, there are only finitely many possible integers h satisfying the approximation inequality"). The exponent `κ` plays no role: the proof works for any bound on the right-hand side.

## Junk check (Step 8)
- Used anywhere? Yes, at 4 sites in 2 files: `reduction`, `exists_reduced_approx` (twice) and `LeanEval.isDiophantine_iff`. All of them use it to throw away the finitely many bounded-denominator approximations.
- Wrapper of 1–2 mathlib calls? No. Mathlib has no lemma stating finiteness of bounded-denominator fractions in a bounded set. The shortest proof found (evidence) uses `Int.tendsto_coe_cofinite`, `IsCompact.compl_mem_cocompact`, `Filter.mem_cofinite`, `Set.Finite.biUnion` and `Set.Finite.prod`, plus an `abs` computation. That is a short proof, not a wrapper.
- Does mathlib have it? No (searches below). The closest is `Rat.finite_rat_abs_sub_lt_one_div_den_sq`, whose proof re-derives the same "finite union over denominators of integer intervals" argument inline. `Irrational.eventually_forall_le_dist_cast_div_of_denom_le` is the topological cousin.
- Too specific (inline?)? No. It has 4 call sites in 2 files, and inlining a 10–20 line argument four times would be worse.
- Well-chosen? Yes for the project. It matches the paper's sentence, and the `sdiff`/`image` call sites use it directly.

Conclusion: KEEP. Optional local improvement: replace the 23-line proof with the compiled shorter route from the evidence file (a generic per-`q` lemma plus a 4-line union).

## Mathlibable assessment (Step 9)

Pre-filter: the theorem is public. Its name does not end in `_aux`, and its docstring is not internal or auxiliary. Step 8 said KEEP. Mathlib has no `Roth` namespace. It is not a glue lemma, since the proof is 23 lines. Full run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Main` elaborates with no diagnostics)
- decl `Roth.approxSet_den_le_finite`: resolved at Roth/Main.lean:73
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Roth's theorem for real algebraic numbers, stated with `Roth.approxSet` and reduced via §6 to algebraic integers.

### Statement (Phase 1)

`Roth.approxSet_den_le_finite` is a theorem stating the following:

Let α, κ ∈ ℝ and Q₀ ∈ ℕ. Only finitely many integer pairs (h, q) with 0 < q ≤ Q₀ satisfy |α − h/q| < q^{−κ}.

Variables / typeclasses involved (Lean side):
- `α : ℝ`: the number being approximated.
- `κ : ℝ`: the approximation exponent.
- `Q₀ : ℕ`: the denominator bound.

Hypotheses (Lean side):
- none.

Conclusion (math): the bounded-denominator part of the approximation set is finite.

Conclusion (Lean): `{hq ∈ approxSet α κ | hq.2 ≤ Q₀}.Finite`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: an elementary helper used in the §6 reduction and the LeanEval bridge. It is not a main result.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

n/a: kind is theorem. MULTI-LINE (23-line proof); check skipped.

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | finitely many rationals p/q with bounded denominator in a bounded interval approximation inequality finite | partial | an interval of length U contains at most about qU + 2 fractions with denominator q | arXiv 2608.26818 (counting remark), AoPS "Rational approximation", Mathlib DiophantineApproximation docs. Treated as folklore, never as a named lemma |
| 2 | WebSearch (general form) | rationals with bounded denominator form a discrete set locally finite 1/q Z lattice | yes | for fixed N, `⋃_{q≤N} (1/q)ℤ` is locally finite (a finite union of lattices); each level `(1/q)ℤ` is 1/q-separated | Physics Forums thread "Finite rationals with denominator less than n₀"; Shparlinski slides; mathlib docs for Topology/Instances/Irrational (bounded-denominator neighbourhood lemma) |
| 3 | WebSearch (named / aliases) | Roth theorem proof "only finitely many" h for each q approximation reduction large denominator | partial | the statement of Roth's theorem (Wikipedia, Roth 1955) | the step is used implicitly in every proof and is never stated as a lemma |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for "fixed upper bound" | yes | l.1175: "For a fixed upper bound on q, there are only finitely many possible integers h satisfying the approximation inequality" | matches the Lean statement exactly |
| 6 | nLab | "discrete subgroup", "lattice" | partial (concept) | discrete subgroups of ℝ are cyclic, hence `(1/q)ℤ` is discrete | no page for the bounded-denominator statement |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | n/a | n/a | n/a | not an algebraic-geometry concept |
| 9 | MathOverflow / Math.SE | (results of #2) bounded denominator rationals in an interval finite | yes (folklore) | finite union over q of finite sets of integers p with p/q in the interval | elementary exercise level |
| 10 | recent arXiv | (results of #1, #2) | partial | arXiv 2608.26818, 2208.13356 use the per-denominator count qU + 2 inside counting arguments | no generalisation beyond "finite union of lattice points in a bounded set" |

### Literature summary (Phase 3)

Concept identified as: local finiteness of fractions with bounded denominator. Equivalently, `⋃_{q ≤ N} (1/q)ℤ` is a finite union of discrete lattices in ℝ, so it meets every bounded set in finitely many points.
Sources agree on the standard form: yes (folklore; nobody names it).
Most general standard form: for any N and any bounded B ⊆ ℝ, the set {(h, q) ∈ ℤ × ℕ : 0 < q ≤ N, h/q ∈ B} is finite. More generally, a lattice meets a bounded set in finitely many points.
Generality dimensions where the literature varies:
  - the right-hand side: `q^{−κ}` (here), `C/q^p`, `1/q²`, any bound r(q). The most general version is any bounded target set.
  - indexing: pairs (here) vs `ℚ` with `den ≤ N`.
Disagreement with the literature: none. The user's form is a special case: the bounded set is a ball around α whose radius depends on q.

### Generality analysis — `Roth.approxSet_den_le_finite`

Literature-standard form: fractions h/q with 0 < q ≤ N in a bounded set are finitely many.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason |
|---|---|---|---|---|---|
| 1 | bound `1 / q^κ` | specific exponent bound | any bound r(q), or any bounded set | yes (compiled) | the evidence lemma `finite_int_abs_sub_div_lt` works for any `r : ℝ` at each fixed `q`, and the union over `q ∈ [1, Q₀]` handles any r(q) |
| 2 | `κ : ℝ` | any real | n/a | already general | no hypothesis on κ (κ ≤ 0 also works) |
| 3 | `α : ℝ` | real | point of ℝ / bounded set | yes | a ball around α is one bounded set among many |
| 4 | statement about `approxSet` | project def | generic set | n/a | `approxSet` is NO-composable (parent report). An upstreamed statement would have to drop it |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD, but only because it is stated against the project-local `approxSet`. The generic per-denominator lemma and the full statement are both compiled in the evidence file. The project form has no hypotheses to drop. Per false-positive class 5, the generalisation is a different statement (one that drops `approxSet`), not a mechanical edit of this one.
Number of weakening opportunities found: 1 (the bound `1/q^κ` becomes any `r`), compiled as `finite_int_abs_sub_div_lt`.
Proposed restatement (generic, for mathlib):
```lean
theorem finite_int_abs_sub_div_lt (α r : ℝ) {q : ℕ} (hq : 0 < q) :
    {h : ℤ | |α - (h : ℝ) / q| < r}.Finite
```
(and/or the pair version `{p : ℤ × ℕ | 0 < p.2 ∧ p.2 ≤ N ∧ |α - p.1 / p.2| < r p.2}.Finite`)
Cost of restatement: CHEAP (compiled, about 12 lines).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | no hypotheses | — |
| 2 | sequences to filters? | partial | equivalent to `Tendsto (fun p : ℤ × ℕ => (p.1 : ℝ) / p.2) (cofinite ⊓ 𝓟 {p | 0 < p.2 ∧ p.2 ≤ N}) (cocompact ℝ)`; the proof uses `Int.tendsto_coe_cofinite` | composes with `Int.tendsto_coe_cofinite`, cocompact API |
| 3 | construction vs universal property? | no | — | — |
| 4 | bundled substructure? | partial | `(1/q)ℤ` is `AddSubgroup.zmultiples (1/q)`; finiteness of a discrete subgroup meeting a bounded set is `Metric.finite_isBounded_inter_isClosed` | discrete-subgroup / ZLattice API (heavier than needed) |
| 5 | field-specific to weaker typeclasses? | no | the real setting is intended | — |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | no | ℤ × ℕ pairs are the standard indexing | — |
| 8 | concrete-via-abstract? | yes | the proof never uses the exponent form `q^κ` except to bound it by a constant `S`. The abstract content is "bounded set ⇒ finitely many bounded-denominator fractions" (`approxSet` occurs only in the statement and the `rintro`) | generic lemma (Phase 4b restatement) |
| 9 | false-generalisation guard | no false generalisation | the generic lemma implies the project statement in 4 lines (compiled) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes, but it is a different (generic) lemma.
  - Proposed mathlib-idiomatic restatement: `finite_int_abs_sub_div_lt` (above), proved from `Int.tendsto_coe_cofinite`.
  - Cost: CHEAP
  - Mathlib downstream this enables: it would shorten `Rat.finite_rat_abs_sub_lt_one_div_den_sq` (Mathlib/NumberTheory/DiophantineApproximation/Basic.lean:253), which re-derives this finite union over denominators by hand with explicit `Icc (⌈ξ y⌉ - 1) (⌊ξ y⌋ + 1)` boxes.
  - Real mathematical improvement: it names the local finiteness of bounded-denominator fractions, which mathlib proves by hand in one place and the project in another. The improvement is small.

### Proof strategy — `Roth.approxSet_den_le_finite`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | yes | replace the explicit `K = ⌈Q₀(|α| + S)⌉` box with `Int.tendsto_coe_cofinite` and `isCompact_closedBall`, one `q` at a time | CHEAP (compiled) |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes | a per-denominator finiteness lemma such as `finite_int_abs_sub_div_lt` | follow-up PR, if approved |

### Proof strategy verdict (Phase 4.6)

Current strategy: REFACTOR-RECOMMENDED
  - Proposed strategy: a generic per-`q` finiteness lemma (cofinite/cocompact), then `(finite_Icc 1 Q₀).biUnion (... .prod (finite_singleton q))`.
  - Cost: CHEAP
  - Missing mathlib API: the per-denominator lemma itself.
  - Would refactoring make the proof strictly shorter / cleaner? yes. The main statement drops to 4 lines, and the global sum `S` and the ceiling bound disappear.

### Diamond / defeq risk

n/a: declaration kind is theorem.

### Mathlib search-status: `Roth.approxSet_den_le_finite`

[A] Lean-Finder       "only finitely many integers h with |x - h/q| < r for fixed q; finitely many fractions with bounded denominator in a bounded interval"   hits: `Rat.finite_rat_abs_sub_lt_one_div_den_sq`, `LiouvilleWith`, `Liouville`, `setOf_liouvilleWith_subset_aux`, `Real.exists_rat_abs_sub_le_and_den_le`, `UnitAddCircle.mem_addWellApproximable_iff`. None is the bounded-denominator finiteness statement
[B] Loogle            `Set.Finite, |_ - _ / _|, Int.cast`   no hits
[C] LeanSearch        "set of rationals with bounded denominator in a bounded set is finite"   hits: `Rat.finite_rat_abs_sub_lt_one_div_den_sq`, `ZSpan.setFinite_inter`, `Metric.finite_isBounded_inter_isClosed`, `NumberField...integerLattice.inter_ball_finite` (building blocks for lattices, none for fractions)
[D] Grep mathlib src  `den_le`, `finite_rat`, `Finite.*den`, `finite_isBounded`, `tendsto_coe_cofinite`, `preimage_closedBall`   hits: `Int.tendsto_coe_cofinite` (Topology/Instances/ZMultiples.lean:50), `Metric.finite_isBounded_inter_isClosed` (Topology/MetricSpace/Bounded.lean:627), `Int.preimage_closedBall` (Topology/Instances/Int.lean:55), `Rat.finite_rat_abs_sub_lt_one_div_den_sq` (NumberTheory/DiophantineApproximation/Basic.lean:253, whose proof re-derives the union over denominators inline), `Irrational.eventually_forall_le_dist_cast_div_of_denom_le` (Topology/Instances/Irrational.lean)
[E] Name pattern      `finite_int_abs_sub`, `finite_*_den_le`, `approxSet`: no hits (grep, in place of `lean_local_search`)

Searched for both:
  - the user's current form (approxSet with bounded denominator)
  - the literature-standard form (bounded-denominator fractions in a bounded set)

Concluded: found building blocks (`Int.tendsto_coe_cofinite`, `IsCompact.compl_mem_cocompact`, `Filter.mem_cofinite`, `Set.Finite.biUnion`, `Set.Finite.prod`); a short proof yields our form. The generic statement is not in mathlib.

### Normal-form check — `Roth.approxSet_den_le_finite`

Equivalent formalisms: (a) `{hq ∈ approxSet α κ | hq.2 ≤ Q₀}.Finite` (current); (b) a finite union over `q ≤ Q₀` of finite integer sets; (c) `{x : ℚ | x.den ≤ N ∧ |α - x| < r}.Finite`.
Does mathlib already have a canonical form for this idea? no.
If upstreamed, propose (b)'s per-`q` statement (`finite_int_abs_sub_div_lt`) as the primitive, with (a)/(c) as corollaries.
RHS convention respected? n/a (not an iff).

### Syntactic generality — `Roth.approxSet_den_le_finite`

Alternative restatements attempted:
- current `sep` set over `approxSet`
- generic per-`q` integer set (evidence)
- `ℚ`-indexed `den ≤ N` set
Chosen restatement: the current one for the project, since the call sites take `hinf.sdiff (approxSet_den_le_finite ...)` directly. The per-`q` form is the right primitive for mathlib.
Justification: easiest to apply at the `sdiff`/`image` call sites.

### Superfluous-argument audit — `Roth.approxSet_den_le_finite`

| # | Argument | Essentially used? | Notes |
|---|---|---|---|
| 1 | `α` | yes | centre |
| 2 | `κ` | no (essentially) | any bound works; it appears only through `approxSet` |
| 3 | `Q₀` | yes | denominator bound; without it the set may be infinite |

### Statement-shape verdict (Phase 5.5)

Normal form: OK for the project (no canonical mathlib form exists)
Syntactic generality: OK for the project. RESTATE (generic per-`q` lemma) for mathlib
Superfluous arguments: NONE to drop locally (κ is inherent to `approxSet`)

Overall: SHIP-AS-STATED (project); RESTATE-BEFORE-SHIP if anything goes upstream

### Call sites — `Roth.approxSet_den_le_finite`

Internal use count: 1 outside the declaring file (LeanEval.lean), plus 3 in Main.lean
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Main.lean:124 (`reduction`) | `refine ((hinf.sdiff (approxSet_den_le_finite α κ Q₀)).image` |
| Roth/Main.lean:170 (`exists_reduced_approx`) | `refine ((approxSet_den_le_finite α κ Q₀).image ρ).subset ?_` |
| Roth/Main.lean:182 (`exists_reduced_approx`) | `refine (approxSet_den_le_finite α κ N).subset ?_` |
| Roth/LeanEval.lean:49 (`isDiophantine_iff`) | `(hinf.sdiff (Roth.approxSet_den_le_finite x κ Q)).nonempty` |

Inline-derivation grep: (none in the project). In mathlib, `Rat.finite_rat_abs_sub_lt_one_div_den_sq` re-derives the same argument inline, which suggests a missing generic lemma.

### Composition check (Phase 6)

Can `Roth.approxSet_den_le_finite` be derived from mathlib in ≤3 chained calls?

Attempt 1: `(finite_Icc 1 Q₀).biUnion fun q hq => (finite_int_abs_sub_div_lt α _ hq.1).prod (finite_singleton q)`, then `.subset` with a 2-line membership proof.
  - Mathlib decls used: `Set.finite_Icc`, `Set.Finite.biUnion`, `Set.Finite.prod`, `Set.finite_singleton`, `Set.mem_biUnion`
  - Result: partial. It compiles, but it needs the per-`q` lemma, which is not in mathlib.
Attempt 2: the per-`q` lemma from `Filter.mem_cofinite.1 (Int.tendsto_coe_cofinite (isCompact_closedBall (q*α) (q*r)).compl_mem_cocompact)` plus `.subset` with an `abs` rewrite (`abs_mul`, `mul_sub`, `mul_div_cancel₀`).
  - Mathlib decls used: `Int.tendsto_coe_cofinite`, `isCompact_closedBall`, `IsCompact.compl_mem_cocompact`, `Filter.mem_cofinite`
  - Result: succeeds (compiled), but as a roughly 8-line proof with a nontrivial `abs` computation, not a ≤3-call composition.

Conclusion: NOT-COMPOSABLE (the chain needs a genuine short proof; total about 12 lines compiled)

### Verdict: `Roth.approxSet_den_le_finite`

**Category:** BORDERLINE-needs-human

**Evidence:**
- Literature search (Phase 3): a folklore fact (bounded-denominator fractions are locally finite), never named. Source l.1175 matches the statement.
- Generality analysis (Phase 4): the project form is a special case, only through the project def `approxSet`. The generic per-`q` lemma is compiled.
- Mathlib search (Phase 5): building blocks only (`Int.tendsto_coe_cofinite` and friends). Mathlib proves the same fact inline inside `Rat.finite_rat_abs_sub_lt_one_div_den_sq`.
- Composition check (Phase 6): NOT-COMPOSABLE in ≤3 calls (about 12 compiled lines).

**Rationale:**

As stated, the lemma cannot go to mathlib: it is phrased with `Roth.approxSet`, which the parent report classed NO-composable-from-mathlib (mathlib's notion is `LiouvilleWith`). Its content is the folklore fact that, for fixed N, only finitely many fractions h/q with 0 < q ≤ N lie in a bounded set. That fact is absent from mathlib as a lemma. The evidence of a gap is that `Rat.finite_rat_abs_sub_lt_one_div_den_sq` (DiophantineApproximation/Basic.lean:253) re-proves it inline with explicit floor/ceil boxes and a `biUnion` over denominators. The generic statement `finite_int_abs_sub_div_lt` compiles in about 8 lines from `Int.tendsto_coe_cofinite`, and the project statement follows from it in 4.

Whether that generic lemma clears mathlib's bar is a judgment call. It is elementary and has one in-mathlib consumer. It also overlaps with the general "lattice ∩ bounded set is finite" machinery (`Metric.finite_isBounded_inter_isClosed`, `ZSpan.setFinite_inter`), which a reviewer might prefer to see used directly. Locally, the lemma is good API (4 call sites in 2 files) and should stay; its proof can optionally be shortened to the compiled route.

Numbered questions:
1. Should the generic lemma `finite_int_abs_sub_div_lt (α r : ℝ) (hq : 0 < q) : {h : ℤ | |α - h / q| < r}.Finite` (or its pair version with `q ≤ N`) be proposed for Mathlib/NumberTheory/DiophantineApproximation/Basic.lean, refactoring `Rat.finite_rat_abs_sub_lt_one_div_den_sq` to use it?
2. If yes, should it be stated over `ℚ` (`{x : ℚ | x.den ≤ N ∧ |α - x| < r}.Finite`) rather than over integer pairs?
3. Should the project replace the current 23-line proof with the shorter cofinite/biUnion proof from the evidence file (independently of upstreaming)?

Belongs-elsewhere check: the stated `approxSet` form stays project-local in Roth/Main.lean (paper §6, l.1175).
Call sites in our project (from Phase 6.0): 4 (Main.lean:124, 170, 182; LeanEval.lean:49). No change is needed at any of them in either outcome, since the statement is unchanged.
Next action: the user answers Q1–Q3. The default is KEEP as is.

---

## Next step

Keep `Roth.approxSet_den_le_finite` in Roth/Main.lean. Decide Q1–Q3. If Q3 is yes, swap in the proof from `.mathlib-quality/overview/evidence/Roth.approxSet_den_le_finite/alt_proof.lean`. If Q1 is yes, open a mathlib PR adding the generic per-denominator lemma next to `Rat.finite_rat_abs_sub_lt_one_div_den_sq`.

## Evidence
- `.mathlib-quality/overview/evidence/Roth.approxSet_den_le_finite/alt_proof.lean` (imports `Roth.Main`): (1) the generic `finite_int_abs_sub_div_lt` from `Int.tendsto_coe_cofinite`; (2) the project statement re-proved from (1) in 4 lines; (3) a reference use of the project lemma. Checked with `lean_diagnostic_messages`. The first check gave one deprecation warning (`Set.mem_setOf_eq`), which was fixed to `mem_ofPred_eq`. The re-check reported no diagnostics.
- Searches: 3 WebSearch queries, Lean-Finder, LeanSearch and Loogle (no hits), grep over mathlib (`den_le`, `finite_rat`, `finite_isBounded`, `tendsto_coe_cofinite`, `preimage_closedBall`, `eventually_forall_le_dist_cast_div`), project grep for call sites, and grep of clean.tex (l.1175). ChatGPT MCP was unavailable in this session.
