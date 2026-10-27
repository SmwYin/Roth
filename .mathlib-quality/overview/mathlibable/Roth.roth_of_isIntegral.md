---
decl: Roth.roth_of_isIntegral
file: Roth/Main.lean
line: 547
kind: theorem
visibility: public
verdict: BORDERLINE-needs-human
cost: EXPENSIVE
junk: KEEP
rationale: Roth's theorem for irrational real algebraic integers is the genuine core of a result mathlib lacks (LiouvilleWith's module docstring names Thue-Siegel-Roth but nothing proves it), yet the declaration is a strictly narrower one-term special case of Roth.roth (compiled), is stated over the project-local approxSet, and rests on the whole project machinery (main_lemma is itself BORDERLINE), so upstreaming it is a human decision about upstreaming the entire Roth development in LiouvilleWith form, not about this lemma.
action: Keep in Roth/Main.lean as the paper's section 7 theorem (single caller Roth.roth at Roth/Main.lean:577); do not upstream on its own; if Roth is upstreamed, the mathlib statement is the general not_liouvilleWith form next to Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleWith.lean and this lemma becomes an internal step (see evidence/Roth.roth_of_isIntegral/liouvilleWith_form.lean).
---

# Roth.roth_of_isIntegral

## Inventory entry

### `theorem Roth.roth_of_isIntegral`
- **Type**: `{α : ℝ} (hα : Irrational α) (hint : IsIntegral ℤ α) {κ : ℝ} (hinf : (approxSet α κ).Infinite) : κ ≤ 2`
- **What**: Roth's theorem for irrational real algebraic integers: if `|α − h/q| < 1/q^κ` has infinitely many solutions `(h, q) ∈ ℤ × ℕ`, `q > 0`, then `κ ≤ 2`.
- **How**: By contradiction from `2 < κ`. `exists_roth_parameters_aux` supplies the monic minimal-type polynomial `f`, the height bound `A`, the number of variables `m ≥ 2` and `δ < 1/m` with the numerical constraints (30) and (49) (via `exists_m`, `exists_delta`). `exists_roth_approximants_aux` picks reduced approximants `h_j/q_j` with rapidly growing denominators and degrees `r_j` (via `exists_approximants`, `exists_degrees`). `roth_product_bound_aux` bounds `B = mainCoeffBound` and `∏ (r_j+1)`. `one_lt_roth_eval_bound_aux` (which invokes `main_lemma`, `one_le_prod_pow_mul_abs_eval`, `abs_eval_lt_of_le_index`) gives the lower/upper comparison of `Q(h/q)`; `roth_log_bound_aux` takes logarithms to get `γκ < m(1+4δ)`, contradicting (49) via `div_lt_iff₀'` and `eta_lt_gam_iff`.
- **Hypotheses**: `hα : Irrational α`, `hint : IsIntegral ℤ α`, `hinf : (approxSet α κ).Infinite`.
- **Uses from project**: `Roth.approxSet`, `Roth.exists_roth_parameters_aux`, `Roth.exists_roth_approximants_aux`, `Roth.roth_product_bound_aux`, `Roth.roth_log_bound_aux`, `Roth.one_lt_roth_eval_bound_aux`, `Roth.eta_lt_gam_iff`
- **Used by**: Roth/Main.lean: `Roth.roth` (line 577). No other use in `Roth/` (also listed in the Main.lean module docstring, line 22).
- **Visibility**: public
- **Lines**: 543–563 (docstring 543–546), proof 549–563, proof length 15 lines
- **Notes**: Source: clean.tex §7 (l.1195 "Let α be an irrational real algebraic integer such that ... Our goal is to prove that κ ≤ 2"; docstring cites "This contradicts (49) and finishes the proof of the theorem"). It is step 2–5 of the module's proof outline; the private `_aux` helpers were extracted from it in this cleanup.

## Junk check (Step 8)
- Used anywhere? Yes: `Roth.roth` (Main.lean:577) composes it with `Roth.reduction`.
- Wrapper of 1–2 mathlib calls? No. It is the assembly of the paper's §7 argument from five project helpers.
- Does mathlib have it? No. Lean-Finder / LeanSearch / Loogle (`LiouvilleWith, IsAlgebraic`: no hits) find only `ae_not_liouvilleWith` (the measure-theoretic a.e. statement), `LiouvilleWith.irrational`, and Liouville's theorem `Liouville.exists_pos_real_of_irrational_root`. Grep of mathlib for `Thue`/`Roth` finds only the LiouvilleWith docstring mention and the unrelated combinatorial Roth (corners / 3-AP) files.
- Too specific (inline?)? It is a strict special case of `Roth.roth` (evidence (2)) with one caller, so it could be inlined; but it is the named theorem of the paper's §7 and keeps `Roth.roth` a 3-line proof that mirrors the source (reduction + integer case). Inlining would hurt readability.
- Well-chosen? Yes for the project.

Conclusion: KEEP. No action.

## Mathlibable assessment (Step 9)

Pre-filter: public; name does not end in `_aux`; docstring not internal/auxiliary; Step 8 KEEP; namespace-aware grep of `.lake/packages/mathlib/Mathlib/` for `roth_of_isIntegral` and any Diophantine Roth development: none. Not glue (15-line proof assembling the main argument). Full run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Main` elaborates with no diagnostics)
- decl `Roth.roth_of_isIntegral`: resolved at Roth/Main.lean:547
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Roth's theorem for real algebraic numbers, reduced (§6) to irrational real algebraic integers and proved (§7) via the auxiliary-polynomial / index method.

### Statement (Phase 1)

`Roth.roth_of_isIntegral` is a theorem stating the following:

Let α be an irrational real algebraic integer and κ ∈ ℝ. If there are infinitely many pairs (h, q) of integers with q > 0 and |α − h/q| < q^{−κ}, then κ ≤ 2. Equivalently: an irrational real algebraic integer has irrationality exponent at most 2.

Variables / typeclasses involved (Lean side):
- `α : ℝ`: the algebraic integer.
- `κ : ℝ`: the approximation exponent.

Hypotheses (Lean side):
- `hα : Irrational α`.
- `hint : IsIntegral ℤ α`: α is a root of a monic integer polynomial.
- `hinf : (approxSet α κ).Infinite`.

Conclusion (math): κ ≤ 2.
Conclusion (Lean): `κ ≤ 2`.

### Size classification (Phase 2a)

Verdict: BIG
Reason: it is Roth's theorem (the integral case carries the entire Fields-medal argument; the general case is a 2-line reduction on top). Listed under "Main results" of Roth/Main.lean.

### One-line check (Phase 2b)

n/a: kind is theorem with a 15-line proof. MULTI-LINE; check skipped.

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth's theorem algebraic integer case "algebraic integer" rational approximation exponent 2 proof | partial | Wikipedia, Leiden/Utrecht course notes (Evertse dio19-6, dio6): the theorem is stated for all irrational algebraic α; the integer case appears only as an internal WLOG step | no source states the integer case as a separate theorem except as a proof step |
| 2 | WebSearch (general form) | Roth theorem irrationality exponent algebraic numbers equals 2 statement Schmidt Diophantine approximation | yes | "every irrational algebraic number has irrationality exponent 2" (Wikipedia; Waldschmidt notes); generalisations: Schmidt subspace theorem, approximation by algebraic numbers of bounded degree, Ridout's p-adic version | the integer case is a special case of the standard form and of the subspace theorem |
| 3 | WebSearch (named / aliases / formalisations) | Thue-Siegel-Roth theorem formalization Lean mathlib | yes | lean-lang.org/eval problem `thue_siegel_roth` (statement only, `sorry`; notes mathlib lacks Roth machinery); Encyclopedia of Mathematics "Thue-Siegel-Roth theorem" | no prior formalisation in mathlib; the project's Roth/LeanEval.lean targets that eval problem |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` §7 | yes | l.1195: "Let α be an irrational real algebraic integer such that |α − h/q| < 1/q^κ for infinitely many pairs ... Our goal is to prove that κ ≤ 2" | Lean statement matches the source exactly |
| 6 | nLab | "Roth's theorem", "irrationality measure" | no | no Diophantine-approximation entry | — |
| 7 | nCatLab | n/a | n/a | n/a | not categorical |
| 8 | Stacks Project | n/a | n/a | n/a | not algebraic geometry |
| 9 | MathOverflow / Math.SE | Roth theorem "algebraic integer" WLOG | partial | standard remark that one may assume α integral by scaling (exponent invariant under rational scaling) | consistent with Roth.reduction report |
| 10 | recent arXiv | Roth formalisation literature (Takloo-Bighash–Yin, the project paper); arXiv 1306.2976 (Roth for arbitrary varieties, McKinnon–Roth) | partial | generalisations to varieties / Seshadri constants | far beyond mathlib scope; no change to the ℝ statement |

### Literature summary (Phase 3)

Concept identified as: Roth's theorem (Thue–Siegel–Roth), restricted to algebraic integers. Standard form: every irrational real algebraic number α has irrationality exponent 2, i.e. for every ε > 0, |α − p/q| < q^{−2−ε} has only finitely many solutions.
Sources agree on the standard form: yes.
Most general standard form at mathlib's level: for irrational algebraic α and p > 2, ¬ LiouvilleWith p α (mathlib's predicate absorbs the constant C, matching "irrationality exponent ≤ 2"). Further generalisations (Ridout/p-adic, Schmidt subspace, number fields) are out of scope.
Generality dimensions where the literature varies:
  - algebraic integer vs algebraic number: literature states it for algebraic numbers; integrality is a WLOG proof step (§6 Lemma, `Roth.reduction`).
  - constant 1 (project `approxSet`) vs arbitrary constant C (literature, `LiouvilleWith`): equivalent for the exponent statement (bridges compiled in the Roth.approxSet evidence).
Disagreement with the literature: none; the project statement is a faithful but narrower special case.

### Generality analysis — `Roth.roth_of_isIntegral`

Literature-standard form: `Irrational α → IsAlgebraic ℚ α → 2 < p → ¬ LiouvilleWith p α`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason |
|---|---|---|---|---|---|
| 1 | `hint : IsIntegral ℤ α` | integral over ℤ | `IsAlgebraic ℚ α` | yes | that is exactly `Roth.roth`; evidence (2) derives the present lemma from `Roth.roth` in one term (`hint.isAlgebraic.extendScalars ...`) |
| 2 | `hα : Irrational α` | hypothesis | hypothesis (or absorbed by `LiouvilleWith`'s `x ≠ m/n`) | no in approxSet form | evidence (3): `approxSet 0 3` is infinite and `0` is integral, so irrationality is necessary as stated. In the `LiouvilleWith` form it is still needed for the conclusion only via `LiouvilleWith.irrational` (automatic for p > 1). |
| 3 | `approxSet` infinite | constant 1 | `LiouvilleWith p α` | equivalent | evidence (1) compiles `not_liouvilleWith_of_isIntegral` from the lemma plus the `approxSet` bridge |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD. Weakening `IsIntegral ℤ α` to `IsAlgebraic ℚ α` gives `Roth.roth`, already in the project (compiled, evidence (2)). This is false-positive class 4 for the generalisation itself (the general form already exists one declaration below in the same file), but it means the integral case would never be the upstreamed statement: in mathlib it would be an internal step of the proof of the general theorem.
Number of weakening opportunities found: 1 (IsIntegral to IsAlgebraic, = Roth.roth), plus the vocabulary change approxSet to LiouvilleWith (evidence (1)).
Proposed mathlib-facing restatement (of the general theorem, not of this lemma):

```lean
theorem not_liouvilleWith_of_isAlgebraic {α : ℝ} (hα : Irrational α) (halg : IsAlgebraic ℚ α)
    {p : ℝ} (hp : 2 < p) : ¬ LiouvilleWith p α
```

(compiled as `roth_not_liouvilleWith` in evidence/Roth.approxSet/liouvilleWith_bridge.lean; the integral analogue `not_liouvilleWith_of_isIntegral` is compiled in this declaration's evidence).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | — |
| 2 | sequences to filters? | yes | `approxSet α κ` infinite to `LiouvilleWith p α` (an `∃ᶠ n in atTop` predicate) | LiouvilleWith API, `ae_not_liouvilleWith`, `Liouville` |
| 3 | construction to universal property? | no | — | — |
| 4 | set to bundled substructure? | no | — | — |
| 5 | field-specific to weaker typeclasses? | no | ℝ-specific (p-adic analogue is Ridout, separate) | — |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | partial | `IsIntegral ℤ` to `IsAlgebraic ℚ` (= Roth.roth) | — |
| 8 | concrete-via-abstract? | no | the proof is genuinely the auxiliary-polynomial argument; no abstract shortcut exists | — |
| 9 | false-generalisation guard | checked | `hα` cannot be dropped (evidence (3)); `p > 2` cannot be lowered (Dirichlet) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes, `LiouvilleWith` (mathlib's canonical predicate, whose module docstring names Thue–Siegel–Roth for p > 2). Note honestly: mathlib's docstring mentions Roth's theorem as a known fact; it is not literally a `TODO` item, but it marks the gap.

### Proof strategy — `Roth.roth_of_isIntegral`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | partial | the approximant extraction (`exists_roth_approximants_aux`) could consume `LiouvilleWith.frequently_lt_rpow_neg` instead of `approxSet` infinitude | MODERATE |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes | the whole Roth machinery (index, Θ, generalised Wronskians, Hasse derivatives on MvPolynomial, main lemma) is absent from mathlib; see the per-declaration reports (main_lemma BORDERLINE, hasseDeriv/taylor reports) | EXPENSIVE |

### Proof strategy verdict (Phase 4.6)

Current strategy: KEEP (the standard Roth argument, faithfully following the source with constants (30), (49)).
  - Proposed strategy: none for the assembly; a mathlib version would phrase input via `LiouvilleWith`.
  - Cost: EXPENSIVE for any upstream (all dependencies).
  - Missing mathlib API: Hasse derivatives / Taylor shifts for MvPolynomial, index of a polynomial at a point with weights, Roth's lemma / main lemma, generalised Wronskians.
  - Would refactoring make the proof strictly shorter / cleaner? no.

### Diamond / defeq risk

n/a: declaration kind is theorem.

### Mathlib search-status: `Roth.roth_of_isIntegral`

[A] Lean-Finder       "an irrational algebraic real number is not LiouvilleWith p for p greater than 2 (Roth's theorem)"   hits: `ae_not_liouvilleWith`, `forall_liouvilleWith_iff`, `LiouvilleWith.irrational`, `transcendental_liouvilleNumber`, `LiouvilleWith`; none is Roth.
[B] Loogle            `LiouvilleWith, IsAlgebraic`: no hits.
[C] LeanSearch        "algebraic irrational number has irrationality exponent at most 2"   hits: `setOf_liouville_eq_irrational_inter_iInter_iUnion`, `LiouvilleWith`, `Liouville.exists_pos_real_of_irrational_root` (Liouville's theorem, exponent = degree), `ae_not_liouvilleWith`, `LiouvilleWith.irrational`; none is Roth.
[D] Grep mathlib src  `Thue`, `Roth`, `roth_of_isIntegral` over `.lake/packages/mathlib/Mathlib`: only the docstring of Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleWith.lean (l.26–28, Thue–Siegel–Roth "states that such numbers must be transcendental") and unrelated combinatorial Roth files (Combinatorics/Additive/Corner/Roth.lean, AP/Three/*).
[E] Name pattern      grep `roth`, `not_liouvilleWith` in mathlib: only `ae_not_liouvilleWith`.

Searched for both the user's form (integral case with approxSet) and the literature-standard form (¬ LiouvilleWith p α for algebraic α, p > 2).

Concluded: not in mathlib. Closest: Liouville's theorem (`Liouville.exists_pos_real_of_irrational_root`, exponent deg α) and the a.e. statement `ae_not_liouvilleWith`. Genuine gap.

### Normal-form check — `Roth.roth_of_isIntegral`

Equivalent formalisms: (a) `approxSet α κ` infinite ⇒ κ ≤ 2 (project); (b) ∀ p > 2, ¬ LiouvilleWith p α (mathlib); (c) irrationality exponent ≤ 2 (no mathlib predicate).
Canonical mathlib form: (b). Our statement uses (a): REFACTOR target (b) if upstreamed (evidence (1)).
RHS convention respected? n/a.

### Syntactic generality — `Roth.roth_of_isIntegral`

Alternative restatements attempted:
- current approxSet / IsIntegral form.
- `not_liouvilleWith_of_isIntegral` (evidence (1), compiled).
- general `Roth.roth` (IsAlgebraic), from which the current lemma follows in one term (evidence (2)).
Chosen restatement: current form for the project (matches the paper §7 and `Roth.reduction`'s output).

### Superfluous-argument audit — `Roth.roth_of_isIntegral`

| # | Argument | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hα` | yes | necessary (evidence (3)); used for reduced approximants (`exists_roth_approximants_aux`) |
| 2 | `hint` | yes | monic integer polynomial `f` (`exists_roth_parameters_aux`); weakenable only by adding the reduction, i.e. to `Roth.roth` |
| 3 | `hinf` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (only if upstreamed: LiouvilleWith)
Syntactic generality: OK for the project (general form exists as `Roth.roth`)
Superfluous arguments: NONE

Overall: SHIP-AS-STATED for the project; for mathlib the statement to ship is the general LiouvilleWith form, with this lemma internal.

### Call sites — `Roth.roth_of_isIntegral`

Internal use count: 1 (in the declaring file)
External-to-file callers: 0 files

| Caller file:line | Usage pattern |
|---|---|
| Roth/Main.lean:577 (`Roth.roth`) | `exact (roth_of_isIntegral hα' hint' hinf').not_gt hκ'` after `reduction` |

Inline-derivation grep (`exists_roth_parameters_aux`, `one_lt_roth_eval_bound_aux` across `Roth/`): only inside `roth_of_isIntegral`.

### Composition check (Phase 6)

Can `Roth.roth_of_isIntegral` be derived from mathlib in ≤3 chained calls?

Attempt 1 (mathlib only): Liouville's theorem gives exponent ≤ deg α only; `ae_not_liouvilleWith` gives the bound only almost everywhere and says nothing about algebraic numbers.
  - Result: fails. No mathlib combination yields exponent 2 for algebraic integers of degree ≥ 3.
Attempt 2 (project): `Roth.roth hα (hint.isAlgebraic.extendScalars (FaithfulSMul.algebraMap_injective ℤ ℚ)) hinf`.
  - Result: succeeds (evidence (2)), but circular for the project (`Roth.roth` is proved from this lemma) and uses project API only.

Conclusion: NOT COMPOSABLE from mathlib.

### Phase 7 gate

- Literature search done (≥3 WebSearch, local refs, n/a channels justified): yes.
- Generality claims compiled: yes (evidence (1)–(3)).
- Mathlib five-method search done: yes.
- Composition check done: yes (not composable).
- Bucket evidence present: BORDERLINE requires a stated reason a human must decide: yes (below).

### Verdict: `Roth.roth_of_isIntegral`

**Category:** BORDERLINE-needs-human

**Evidence:**
- Literature (Phase 3): standard Roth's theorem restricted to algebraic integers; the literature states the general algebraic case, integrality being a WLOG step.
- Generality (Phase 4): strictly narrower than `Roth.roth` (one-term derivation compiled) and than the standard form; restated in mathlib vocabulary as `¬ LiouvilleWith p α` (compiled).
- Mathlib search (Phase 5): absent; mathlib's LiouvilleWith docstring names Thue–Siegel–Roth without proving it.
- Composition (Phase 6): not composable from mathlib.

**Rationale:**

The mathematics is a genuine and important mathlib gap: Thue–Siegel–Roth is explicitly mentioned in Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleWith.lean (l.26–28) and nothing proves it; mathlib has only Liouville's exponent-deg bound and the a.e. result. So this is not a NO. But it is also not a YES for this declaration: (i) as stated it is a strict special case of `Roth.roth` in the same file, so mathlib would want the general `IsAlgebraic` statement and would demote the integral case to an internal step; (ii) it is stated over the project-local `approxSet` (NO-composable; the canonical mathlib form is `LiouvilleWith`, bridge compiled); (iii) its proof depends on the entire project (main_lemma is BORDERLINE-needs-human, plus the index/Θ/Wronskian/Hasse-derivative machinery), with source-specific constants. Upstreaming it therefore means upstreaming the whole Roth development, redesigned in `LiouvilleWith` form and split across MvPolynomial/Hasse-derivative and Diophantine-approximation files. That is a scope and maintenance decision for the authors and mathlib reviewers.

Questions for the human:

1. Should the Roth development be proposed to mathlib as `not_liouvilleWith_of_isAlgebraic` in Mathlib/NumberTheory/Transcendental/Liouville/ (recommended: only after the MvPolynomial Hasse-derivative/Taylor API is upstreamed), or stay a standalone project depending on mathlib?
2. If upstreamed, should the integral case remain a named public lemma, or become a private step of the general theorem (recommended: private step)?
3. Keep `Roth.roth_of_isIntegral` project-local in Roth/Main.lean as is (recommended: yes)?
Belongs-elsewhere check: keep in Roth/Main.lean as the §7 theorem.
Call sites in our project: 1 (Roth/Main.lean:577).
Refactor plan: none locally.
Next action: keep as is; escalate the upstream-Roth question to the authors.

### Next step

Keep project-local. If Roth is upstreamed, ship the general `LiouvilleWith` statement (evidence (1) shows the integral case in that form; evidence/Roth.approxSet/liouvilleWith_bridge.lean shows the general one), prepared bottom-up starting with the MvPolynomial Hasse-derivative/Taylor API.

## Evidence
- Evidence file: `.mathlib-quality/overview/evidence/Roth.roth_of_isIntegral/liouvilleWith_form.lean` (imports `Roth.Main`, LiouvilleWith): (1) `not_liouvilleWith_of_isIntegral`, the LiouvilleWith form derived from `Roth.roth_of_isIntegral` via the `approxSet_infinite_of_liouvilleWith` bridge; (2) the lemma re-derived from `Roth.roth` in one term (strictly narrower); (3) `approxSet 0 3` infinite with `0` integral, showing `Irrational α` is necessary. `lean_diagnostic_messages`: no errors, no warnings.
- WebSearch ×3 (table rows 1–3), Lean-Finder ×1, LeanSearch ×1, Loogle ×1 (no hits), grep of mathlib for `Thue`/`Roth`, grep of clean.tex §7. ChatGPT MCP unavailable in this session.
- Related reports read: Roth.approxSet.md, Roth.reduction.md, Roth.main_lemma.md.
