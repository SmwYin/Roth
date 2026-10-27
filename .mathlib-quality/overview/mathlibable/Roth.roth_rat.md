---
decl: Roth.roth_rat
file: Roth/Main.lean
line: 581
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: EXPENSIVE
junk: KEEP
rationale: Den-form Roth theorem stated entirely in mathlib vocabulary (same shape as Real.infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational) and absent from mathlib, but Irrational is superfluous (compiled roth_rat' via the mathlib iff for rational x) and the mathlib-facing form is the finiteness statement for 2 < κ; proof upstreaming waits on Roth.roth and the whole development.
action: Keep in Roth/Main.lean (no project callers; listed in module docstring); drop the Irrational hypothesis now using evidence roth_rat'; upstream as IsAlgebraic.finite_rat_abs_sub_lt_one_div_den_rpow next to Real.infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational (Mathlib/NumberTheory/DiophantineApproximation/Basic.lean) or in the planned Mathlib/NumberTheory/Transcendental/Liouville/Roth.lean, as a corollary of IsAlgebraic.not_liouvilleWith once Roth.roth lands.
---

# Roth.roth_rat

## Inventory entry

### `theorem Roth.roth_rat`
- **Type**: `{α : ℝ} (hα : Irrational α) (halg : IsAlgebraic ℚ α) {κ : ℝ} (hinf : {x : ℚ | |α - x| < 1 / (x.den : ℝ) ^ κ}.Infinite) : κ ≤ 2`
- **What**: Roth's theorem in rational/denominator form: if α is an irrational real algebraic number and infinitely many rationals x satisfy `|α − x| < 1/den(x)^κ`, then `κ ≤ 2`.
- **How**: Applies `Roth.roth` after pushing the infinite rational set into `approxSet α κ` via the injective map `x ↦ (x.num, x.den)` (`Set.Infinite.image` with `Rat.ext`, then `Set.Infinite.mono`); membership uses `Rat.den_pos` and `Rat.cast_def`. 5-line proof.
- **Hypotheses**: `hα : Irrational α`, `halg : IsAlgebraic ℚ α`, `hinf` (infinitely many rational approximations of quality κ).
- **Uses from project**: `Roth.roth`, `Roth.approxSet` (implicitly, as the target of `.mono`)
- **Used by**: unused in project (only named in the Roth/Main.lean module docstring, line 21)
- **Visibility**: public
- **Lines**: 578–587 (docstring 578–579), statement 581–582, proof 583–587, proof length 5 lines
- **Notes**: User-facing variant of the main theorem; the only project statement of Roth phrased purely in mathlib vocabulary (no `approxSet`).

## Junk check (Step 8)
- Used anywhere? No project callers; it is a main-results entry of the module docstring (public API).
- Wrapper of 1–2 mathlib calls? No: a corollary of the project's `Roth.roth` plus a 4-line set-image argument.
- Does mathlib have it? No (Phase 5). Mathlib has only the κ = 2 den-form (Dirichlet: `Real.infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational`, `..._iff_irrational`, `Rat.finite_rat_abs_sub_lt_one_div_den_sq`).
- Too specific? No: this is the most common textbook phrasing of Roth.
- Well-chosen? Yes, except that `Irrational α` is superfluous (evidence (1)).

Conclusion: KEEP. Local action: drop `hα` (evidence `roth_rat'`).

## Mathlibable assessment (Step 9)

Pre-filter: public; name not `_aux`; docstring not internal/auxiliary; Step 8 KEEP; namespace-aware grep of mathlib for `roth_rat`: no hit. Not glue (real proof). Full run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Main` compiles with zero diagnostics)
- decl `Roth.roth_rat`:      resolved at Roth/Main.lean:581
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Roth's theorem for real algebraic numbers, reduced to irrational real algebraic integers and proved via the index method.

### Statement (Phase 1)

`Roth.roth_rat` is a theorem stating the following:

Let α be an irrational real algebraic number and κ ∈ ℝ. If there are infinitely many rational numbers x (in lowest terms, with denominator den(x)) such that |α − x| < den(x)^{−κ}, then κ ≤ 2. Equivalently, for every κ > 2 only finitely many rationals x satisfy |α − x| < den(x)^{−κ}.

Variables / typeclasses involved (Lean side):
- `α : ℝ`: the algebraic number.
- `κ : ℝ`: the approximation exponent.

Hypotheses (Lean side):
- `hα : Irrational α`: superfluous (evidence (1)); for rational α even the κ = 2 set is finite.
- `halg : IsAlgebraic ℚ α`: algebraicity.
- `hinf`: infinitely many rationals x with `|α - x| < 1 / x.den ^ κ`.

Conclusion (math): κ ≤ 2.
Conclusion (Lean): `κ ≤ 2`.

### Size classification (Phase 2a)

Verdict: BIG
Reason: listed under `## Main results` of Roth/Main.lean; it is Roth's (named) theorem in its textbook rational form.

### One-line check (Phase 2b)

n/a: kind is theorem (5-line proof); check skipped.

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth's theorem finitely many rationals p/q, abs(α − p/q) < 1/q^{2+ε}, reduced fractions | yes | for algebraic α and ε > 0 only finitely many rationals p/q satisfy abs(α − p/q) < q^{−2−ε} (arXiv 1210.2983, MathWorld, arXiv 2502.00731) | reduced vs unreduced irrelevant to finiteness |
| 2 | WebSearch (general form) | irrationality exponent definition, Bugeaud, algebraic numbers equal 2 | yes | μ(ξ) = sup of μ with infinitely many rational solutions; Roth: μ(α) = 2 for algebraic irrational α; rationals have μ = 1 (Becher–Bugeaud–Slaman arXiv 1410.1017; Bugeaud–Kim arXiv 2510.02059) | the rational-number formulation with exponent is the standard "irrationality exponent" form; rationals are harmless (μ = 1), so no irrationality hypothesis is needed for a ≤ 2 statement |
| 3 | WebSearch (named-after / formalisations) | Thue–Siegel–Roth theorem Lean formalization rational approximation den | yes | lean-lang.org/eval `thue_siegel_roth` (sorry; notes mathlib has Dirichlet den-form `Real.infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational` but no Roth); Encyclopedia of Math: coprime p, q, finitely many solutions | no existing formalisation in mathlib |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session |
| 5 | Local references | `.mathlib-quality/references/clean.tex` §6 Theorem (Roth) | yes | pairs (h, q) form (eq. (1)); den-form not stated separately | den-form is the project's convenience corollary |
| 6 | nLab | "Roth's theorem", "irrationality measure" | no | no entry | no Diophantine-approximation coverage |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | n/a | n/a | n/a | not algebraic geometry |
| 9 | MathOverflow / Math.SE | Roth statement with reduced fractions vs pairs | partial | standard remark: unreduced solutions yield reduced solutions with smaller denominator, so both forms are equivalent | consistent with Roth.exists_reduced_approx report |
| 10 | recent arXiv (last 5 years) | irrationality exponent, Roth | yes | arXiv 2510.02059 (Bugeaud–Kim), 2603.10561 (p-adic quantitative Roth) | all use the rational-number / exponent form |

### Literature summary (Phase 3)

Concept identified as: Roth's theorem (Thue–Siegel–Roth), irrationality exponent of algebraic numbers.
Sources agree on the standard form: yes.
Most general standard form: for every real algebraic α and every κ > 2, the set of rationals x with |α − x| < den(x)^{−κ} is finite (no irrationality needed: rational α have exponent 1).
Generality dimensions where the literature varies:
  - constant: 1 vs arbitrary C (equivalent for the exponent statement);
  - reduced vs unreduced fractions (equivalent);
  - irrationality hypothesis: present in some statements, unnecessary for the finiteness/exponent claim.
Disagreement with the literature: none; the project form adds an unneeded `Irrational α`.

### Generality analysis — `Roth.roth_rat`

Literature-standard form (from Phase 3): `IsAlgebraic ℚ α → 2 < κ → {x : ℚ | |α - x| < 1 / x.den ^ κ}.Finite`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `hα : Irrational α` | explicit | absent | yes | rational α: the κ-set is inside the 2-set (den ≥ 1, κ ≥ 2), finite by mathlib `Real.infinite_rat_abs_sub_lt_one_div_den_sq_iff_irrational`; compiled as `roth_rat'` (evidence (1)) |
| 2 | `halg : IsAlgebraic ℚ α` | over ℚ | over ℤ or ℚ | equivalent | `extendScalars` one term (evidence (3)) |
| 3 | `hinf` + conclusion `κ ≤ 2` | contrapositive form | `2 < κ → Finite` | equivalent | mathlib's sibling `Rat.finite_rat_abs_sub_lt_one_div_den_sq` uses the `.Finite` shape |
| 4 | base field ℝ | ℝ | ℝ | no | p-adic/number-field versions are separate theorems (Ridout, Lang) |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD (superfluous `Irrational α`; weakening verified by compiling `roth_rat'`, zero diagnostics).
Number of weakening opportunities found: 1 (drop `Irrational α`), plus the shape change to `.Finite`.
Proposed restatement:

```lean
theorem IsAlgebraic.finite_rat_abs_sub_lt_one_div_den_rpow {α κ : ℝ} (halg : IsAlgebraic ℚ α)
    (hκ : 2 < κ) : {x : ℚ | |α - x| < 1 / (x.den : ℝ) ^ κ}.Finite
```

Cost of restatement: CHEAP for the statement (compiled `roth_rat'` and `roth_rat_of_not_liouvilleWith`); EXPENSIVE for an upstream proof (needs Roth.roth, i.e. the whole development). Cost is sequencing only.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | single real number | — |
| 2 | sequences to filters? | partial | the filter form is `¬ LiouvilleWith p α` (parent Roth.roth report); the den-form is kept as the user-facing corollary matching mathlib's Dirichlet lemmas | pairs with `Real.infinite_rat_abs_sub_lt_one_div_den_sq_iff_irrational`, `Rat.finite_rat_abs_sub_lt_one_div_den_sq` |
| 3 | construction to universal property? | no | — | — |
| 4 | set to bundled substructure? | no | solution set, not a substructure | — |
| 5 | field-specific to weaker typeclasses? | no | ℝ intrinsic | — |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | no | ℚ with `den` is the point | — |
| 8 | concrete-via-abstract? | no | proof just transports to `approxSet` and calls `Roth.roth` | — |
| 9 | false-generalisation guard | checked, no false generalisation | dropping `Irrational` keeps the statement true and identical for irrational α (evidence (1) proves the general form from the original) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes (mild)
  - Proposed mathlib-idiomatic restatement: `IsAlgebraic.finite_rat_abs_sub_lt_one_div_den_rpow (halg : IsAlgebraic ℚ α) (hκ : 2 < κ) : {x : ℚ | |α - x| < 1 / x.den ^ κ}.Finite`, derived from `IsAlgebraic.not_liouvilleWith`.
  - Cost: CHEAP (statement), EXPENSIVE (proof upstream).
  - Mathlib downstream this enables: sits next to `Rat.finite_rat_abs_sub_lt_one_div_den_sq` and `Real.infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational`, giving the complete den-form picture (exponent 2 sharp, exponent > 2 finite for algebraic); gives the den-form API a non-trivial theorem.
  - Real mathematical improvement: removes a superfluous hypothesis and matches the shape of the existing mathlib den-form lemmas.

### Proof strategy — `Roth.roth_rat`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | yes | derive from `IsAlgebraic.not_liouvilleWith` via `Nat.frequently_atTop_iff_infinite` (compiled: `roth_rat_of_not_liouvilleWith`) | CHEAP once the LiouvilleWith form exists |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes | a bridge lemma "infinite den-set of exponent p ⇒ LiouvilleWith p" (inline in evidence; cf. Roth.exists_reduced_approx report Q1); exponent-monotonicity of the den-set (`ratSet_mono` in evidence) | CHEAP, separate small PR |

### Proof strategy verdict (Phase 4.6)

Current strategy: REFACTOR-RECOMMENDED (for the upstream version)
  - Proposed strategy: corollary of `IsAlgebraic.not_liouvilleWith` (filter form) instead of the project-local `approxSet`; handle rational α not at all (no hypothesis needed).
  - Cost: CHEAP given the LiouvilleWith form.
  - Missing mathlib API: den-set to LiouvilleWith bridge; den-set exponent monotonicity.
  - Would refactoring make the proof strictly shorter / cleaner? cleaner (removes `approxSet` dependence); similar length.

### Diamond / defeq risk

n/a: declaration kind is theorem.

### Mathlib search-status: `Roth.roth_rat`

[A] Lean-Finder       "Roth's theorem: for algebraic x and exponent greater than 2, the set of rationals q with abs(x - q) < 1/q.den^κ is finite"   hits: `Rat.finite_rat_abs_sub_lt_one_div_den_sq`, `Real.infinite_rat_abs_sub_lt_one_div_den_sq_iff_irrational`, `..._of_irrational`, `liouville_liouvilleNumber`, `LiouvilleWith`; none is Roth.
[B] Loogle            `IsAlgebraic, Rat.den, Set.Infinite`: no hits.
[C] LeanSearch        "algebraic irrational real number, only finitely many rationals q with abs(x - q) < 1 / q.den ^ k for k > 2"   hits: `setOf_liouville_eq_irrational_inter_iInter_iUnion`, `Liouville`, `Real.infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational`, `LiouvilleWith.irrational`, `ae_not_liouvilleWith`; none is Roth.
[D] Grep mathlib src  `roth_rat`, `not_liouvilleWith`, `q.den : ℝ) ^` with non-2 exponent: only `ae_not_liouvilleWith` (Measure.lean:115) and its corollary; no den-form exponent > 2 result.
[E] Name pattern      `roth_rat`, `finite_rat_abs_sub_lt_one_div_den` (grep): only the κ = 2 `Rat.finite_rat_abs_sub_lt_one_div_den_sq` (for rational ξ).

Searched for both:
  - the user's current form (Irrational + IsAlgebraic, infinite den-set ⇒ κ ≤ 2)
  - the literature-standard form (IsAlgebraic, 2 < κ ⇒ den-set finite; `¬ LiouvilleWith`)

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form). Closest: the κ = 2 Dirichlet den-form lemmas.

### Normal-form check — `Roth.roth_rat`

Equivalent formalisms: (a) infinite den-set ⇒ κ ≤ 2 (project); (b) 2 < κ ⇒ den-set finite; (c) ∀ p > 2, ¬ LiouvilleWith p α; (d) `Roth.roth` approxSet form.
Does mathlib already have a canonical form for this idea? yes for the exponent idea: `LiouvilleWith` (c); for the den-form the mathlib shape is `{q : ℚ | ...}.Finite / .Infinite` (DiophantineApproximation/Basic.lean).
Is our statement stated against the canonical form? Partially: it uses the mathlib den-form set, but in contrapositive shape and with an extra hypothesis. REFACTOR: state (b), derived from (c).
RHS convention respected? n/a (not an iff).

### Syntactic generality — `Roth.roth_rat`

Alternative restatements attempted (compiled in evidence):
- `roth_rat'`: no `Irrational` (evidence (1)).
- `roth_rat_of_not_liouvilleWith`: same, derived from the LiouvilleWith form (evidence (2)).
- `IsAlgebraic ℤ` variant (evidence (3)).

Chosen restatement: `IsAlgebraic.finite_rat_abs_sub_lt_one_div_den_rpow` (dot notation on algebraicity, `.Finite` conclusion as in `Rat.finite_rat_abs_sub_lt_one_div_den_sq`).
Justification: callers hold `IsAlgebraic` and want a finiteness fact; no irrationality proof needed.

### Superfluous-argument audit — `Roth.roth_rat`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hα : Irrational α` | no | drop; compiled `roth_rat'` (rational case via `Real.infinite_rat_abs_sub_lt_one_div_den_sq_iff_irrational`) |
| 2 | `halg : IsAlgebraic ℚ α` | yes | the content |
| 3 | `hinf` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (finiteness form, corollary of `¬ LiouvilleWith`)
Syntactic generality: RESTATE (`IsAlgebraic.finite_rat_abs_sub_lt_one_div_den_rpow`)
Superfluous arguments: 1 to drop (`Irrational α`)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.roth_rat`

Internal use count: 0 (outside the declaring file; also 0 inside it)
External-to-file callers: 0 files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Main.lean:21 (module docstring only) | `* Roth.roth_rat: the same statement for rational numbers x and their denominators x.den.` |

Inline-derivation grep (den-set to approxSet transport elsewhere): Roth/LeanEval.lean `isDiophantine_iff` works with `approxSet` directly, not via `roth_rat`; the reverse transport (approxSet ⇒ den-set) is `Roth.exists_reduced_approx` (Main.lean:164). No re-derivation of `roth_rat` itself.

### Composition check (Phase 6)

Can `Roth.roth_rat` be derived from mathlib in ≤3 chained calls?

Attempt 1 (mathlib only): `Rat.finite_rat_abs_sub_lt_one_div_den_sq` covers only rational α; `Liouville.exists_pos_real_of_irrational_root` gives only exponent deg α; `ae_not_liouvilleWith` only a.e.
  - Result: fails.
Attempt 2 (mathlib + `Roth.roth`): `Roth.roth hα halg (hinf.image ...).mono ...` (current proof).
  - Result: succeeds, but depends on the project's core theorem; with a future `IsAlgebraic.not_liouvilleWith` it is a ~15-line corollary (evidence (2)), not ≤3 calls.

Conclusion: NOT-COMPOSABLE.

### Phase 7 gate

- Literature table: 10 rows, 3 WebSearch, local refs, n/a channels justified, ChatGPT n/a recorded: yes.
- STRICTLY NARROWER verified by compiling the weakening (`roth_rat'`): yes.
- Restatement matches literature-standard and modern-idiom targets: yes.
- Downstream consequences listed: yes.
- Q9: no false generalisation.
- Mathlib search 5 methods, both forms: no hit.
- Composition: NOT-COMPOSABLE.
- Call-sites table, 4.6, 5.5 present: yes.
- Cost not used to downgrade: yes.

### Verdict: `Roth.roth_rat`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): the den/rational form with exponent is the textbook Roth statement and the "irrationality exponent = 2" formulation; rationals need no exclusion.
- Generality analysis (Phase 4): STRICTLY NARROWER (`Irrational α` superfluous; compiled `roth_rat'`).
- Mathlib search (Phase 5): not in mathlib; only the κ = 2 Dirichlet den-form lemmas exist.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

`Roth.roth_rat` is the textbook form of Roth's theorem, and unlike `Roth.roth` it is stated entirely in mathlib vocabulary: the set `{x : ℚ | |α - x| < 1 / x.den ^ κ}` has exactly the shape of mathlib's Dirichlet lemmas `Real.infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational` / `_iff_irrational` and `Rat.finite_rat_abs_sub_lt_one_div_den_sq` in Mathlib/NumberTheory/DiophantineApproximation/Basic.lean. Those lemmas settle exponent 2 (infinitely many for irrationals, finitely many for rationals). The missing piece is the exponent > 2 statement for algebraic numbers. Mathlib names that gap itself: the LiouvilleWith.lean module docstring states Thue–Siegel–Roth without a proof, and lean-eval lists it as open.

The statement is not maximally general. `Irrational α` can be dropped: for rational α and κ > 2, the κ-set sits inside the 2-set, which mathlib already proves finite. The evidence compiles `roth_rat'` without the hypothesis. It also compiles `roth_rat_of_not_liouvilleWith`, which derives the same den-form from the LiouvilleWith form proposed in the Roth.roth report, again without irrationality. So in mathlib this should be a finiteness corollary of `IsAlgebraic.not_liouvilleWith`. The proof upstream is EXPENSIVE because it needs Roth.roth and therefore the whole development, but that is sequencing, not a reason to change the bucket.

Reason for the generalisation: LITERATURE-WEAKENING (drop `Irrational`) and MODERN-IDIOM (`.Finite` shape of the sibling mathlib lemmas, derived from `¬ LiouvilleWith`).

Proposed restatement:
```lean
/-- **Roth's theorem**, rational form. -/
theorem IsAlgebraic.finite_rat_abs_sub_lt_one_div_den_rpow {α κ : ℝ} (halg : IsAlgebraic ℚ α)
    (hκ : 2 < κ) : {x : ℚ | |α - x| < 1 / (x.den : ℝ) ^ κ}.Finite := by
  sorry  -- = roth_rat_of_not_liouvilleWith (evidence (2)) in contrapositive form
```

Estimated cost of regeneralisation: CHEAP (statement, compiled); EXPENSIVE (upstream proof depends on Roth.roth). EXPENSIVE does not downgrade the verdict.

Mathlib downstream this enables:
- completes the den-form picture in DiophantineApproximation/Basic.lean: exponent 2 is sharp for irrationals (Dirichlet) and exponent > 2 is finite for algebraic numbers (Roth);
- gives users a Roth statement in the den vocabulary of `Real.infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational` without going through `LiouvilleWith`;
- with `Real.infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational` it yields "irrationality exponent of an algebraic irrational is exactly 2" in one line.

PR grouping: ship together with `IsAlgebraic.not_liouvilleWith` / `LiouvilleWith.transcendental` (Roth.roth report, step 5 of its upstreaming path) in Mathlib/NumberTheory/Transcendental/Liouville/Roth.lean; the den-set to LiouvilleWith bridge (cf. Roth.exists_reduced_approx report, BORDERLINE Q1) can go first to DiophantineApproximation/Basic.lean.

Next action: drop `hα` from `Roth.roth_rat` in Roth/Main.lean now (proof from evidence `roth_rat'`; no callers to update); at upstream time, restate as the `.Finite` form and run `/generalise Roth.roth_rat`.

### Next step

Locally: replace `Roth.roth_rat` with the `roth_rat'` signature (no `Irrational`), zero call sites affected. Upstream: `IsAlgebraic.finite_rat_abs_sub_lt_one_div_den_rpow` as a corollary of `IsAlgebraic.not_liouvilleWith`, after the Roth.roth upstreaming path lands.

## Evidence
- Evidence file: `.mathlib-quality/overview/evidence/Roth.roth_rat/weaken.lean` (imports `Roth.Main`, LiouvilleWith, DiophantineApproximation.Basic); `lake env lean` on it prints nothing (zero errors, zero warnings). Contents: `ratSet_mono` (exponent monotonicity of the den-set); (1) `roth_rat'`: `Roth.roth_rat` without `Irrational α`; `IsAlgebraic.not_liouvilleWith'` (copied from the Roth.roth evidence); (2) `roth_rat_of_not_liouvilleWith`: the den-form from the LiouvilleWith form, no irrationality; (3) `IsAlgebraic ℤ` variant.
- WebSearch ×3 (table rows 1–3); Lean-Finder ×1, LeanSearch ×1, Loogle ×1 (no hits); grep of mathlib for `roth_rat`, `not_liouvilleWith`, non-2 den exponents; grep of `Roth/` for callers (none). ChatGPT MCP unavailable in this session.
- Related reports read: Roth.roth.md (YES-but-generalise-first), Roth.exists_reduced_approx.md (BORDERLINE).
