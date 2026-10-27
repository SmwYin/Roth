---
decl: Roth.roth
file: Roth/Main.lean
line: 573
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: EXPENSIVE
junk: KEEP
rationale: Roth's theorem is a genuine named mathlib gap (the LiouvilleWith module docstring states Thue-Siegel-Roth without proof; lean-eval lists it as an open target) but the project statement uses the project-local approxSet and a superfluous Irrational hypothesis; the mathlib form IsAlgebraic.not_liouvilleWith (no irrationality hypothesis, plus the corollary LiouvilleWith.transcendental) is compiled from Roth.roth in the evidence file, while upstreaming the proof means landing the whole ~4.8k-line development bottom-up.
action: Keep Roth.roth in Roth/Main.lean (callers Roth.roth_rat at Main.lean:583 and LeanEval thueSiegelRoth at LeanEval.lean:64); add the compiled IsAlgebraic.not_liouvilleWith / LiouvilleWith.transcendental wrappers to the project now; upstream target Mathlib/NumberTheory/Transcendental/Liouville/Roth.lean (new file next to LiouvilleWith.lean) only after the MvPolynomial Hasse-derivative/Taylor API, index and main-lemma layers land.
---

# Roth.roth

## Inventory entry

### `theorem Roth.roth`
- **Type**: `{α : ℝ} (hα : Irrational α) (halg : IsAlgebraic ℚ α) {κ : ℝ} (hinf : (approxSet α κ).Infinite) : κ ≤ 2`
- **What**: Roth's theorem: if α is an irrational real algebraic number and `|α − h/q| < 1/q^κ` has infinitely many solutions `(h, q) ∈ ℤ × ℕ` with `q > 0`, then `κ ≤ 2`.
- **How**: By contradiction from `2 < κ`: `Roth.reduction` (scale α by a positive integer `M` from `exists_nat_mul_isIntegral` to get an irrational algebraic integer α' and an exponent κ' > 2 with `approxSet α' κ'` infinite), then `Roth.roth_of_isIntegral` gives `κ' ≤ 2`, contradiction via `not_gt`. 3-line proof.
- **Hypotheses**: `hα : Irrational α`, `halg : IsAlgebraic ℚ α`, `hinf : (approxSet α κ).Infinite`.
- **Uses from project**: `Roth.approxSet`, `Roth.reduction`, `Roth.roth_of_isIntegral`
- **Used by**: Roth/Main.lean: `Roth.roth_rat` (line 583). Roth/LeanEval.lean: `LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth` (line 64; also named in docstrings at lines 8, 41). Listed in the Main.lean module docstring (line 20). Transitively the whole project feeds it.
- **Visibility**: public
- **Lines**: 565–576 (docstring 565–572), proof 575–576 (statement 573–574), proof length 3 lines
- **Notes**: Headline theorem of the project. Source: clean.tex §6, Theorem (Roth), l.1140 ("Let α be an irrational real algebraic number and let κ ∈ ℝ. Suppose there are infinitely many pairs of integers h, q with q > 0 such that ..."). The Lean statement matches the source verbatim.

## Junk check (Step 8)
- Used anywhere? Yes: `Roth.roth_rat` and the LeanEval `thueSiegelRoth` (the project's deliverable for the lean-eval problem).
- Wrapper of 1–2 mathlib calls? No; a 2-step composition of project results (reduction + integral case), and it is the main theorem.
- Does mathlib have it? No (Phase 5 below): mathlib has only Liouville's bound (`Liouville.exists_pos_real_of_irrational_root`), the a.e. statement `ae_not_liouvilleWith`, and a docstring mention of Thue–Siegel–Roth in LiouvilleWith.lean l.26–28.
- Too specific (inline?)? No: it is the headline result.
- Well-chosen? Yes for the project (mirrors the source). For mathlib, the statement shape should change (see Phase 4c/5.5).

Conclusion: KEEP. Local action: optionally add the LiouvilleWith-form corollaries from the evidence file next to it (they are the mathlib-facing API).

## Mathlibable assessment (Step 9)

Pre-filter: public; name does not end in `_aux`; docstring not internal/auxiliary; Step 8 KEEP; namespace-aware grep of `.lake/packages/mathlib/Mathlib/` for `Roth.roth`, `theorem roth`, `not_liouvilleWith`, `Thue`: no Diophantine Roth declaration (only the LiouvilleWith docstring, `ae_not_liouvilleWith`, and the unrelated combinatorial `Mathlib/Combinatorics/Additive/Corner/Roth.lean`). Not glue. Full run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; the evidence file importing `Roth.Main` elaborates with zero diagnostics)
- decl `Roth.roth`:          resolved at Roth/Main.lean:573
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Roth's theorem for real algebraic numbers, reduced (§6) to irrational real algebraic integers and proved (§7) via the auxiliary-polynomial / index method.

### Statement (Phase 1)

`Roth.roth` is a theorem stating the following:

Let α be an irrational real algebraic number and κ ∈ ℝ. If there are infinitely many pairs (h, q) of integers with q > 0 such that |α − h/q| < q^{−κ}, then κ ≤ 2. Equivalently, every irrational real algebraic number has irrationality exponent (measure) exactly 2 (≥ 2 being Dirichlet), i.e. for every ε > 0 the inequality |α − h/q| < q^{−2−ε} has only finitely many solutions.

Variables / typeclasses involved (Lean side):
- `α : ℝ`: the algebraic number being approximated.
- `κ : ℝ`: the approximation exponent.

Hypotheses (Lean side):
- `hα : Irrational α`: excludes trivial exact approximations (necessary in this form, evidence (4)).
- `halg : IsAlgebraic ℚ α`: α algebraic over ℚ.
- `hinf : (approxSet α κ).Infinite`: infinitely many pairs `(h, q) : ℤ × ℕ`, `0 < q`, `|α − h/q| < 1/q^κ` (pairs need not be reduced).

Conclusion (math): κ ≤ 2.
Conclusion (Lean): `κ ≤ 2`.

### Size classification (Phase 2a)

Verdict: BIG
Reason: the main result of the project (first item of `## Main results` in Roth/Main.lean) and a theorem named after a person (Roth; Thue–Siegel–Roth), Fields-medal-level mathematics.

### One-line check (Phase 2b)

n/a: kind is theorem (3-line proof). MULTI-LINE in substance; check skipped.

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth's theorem irrational algebraic number "irrationality exponent" equals 2 statement | yes | "every irrational algebraic number has irrationality exponent 2"; equivalently finitely many solutions of |α − p/q| < q^{−2−ε} (Wikipedia "Roth's theorem"; arXiv 2206.12579) | Dirichlet makes 2 sharp; Liouville gives only exponent deg α |
| 2 | WebSearch (general form) | Schmidt subspace theorem generalization of Roth's theorem Ridout p-adic number field version | yes | Ridout (p-adic, finite set of places), Lang (number fields), Schmidt subspace theorem (m = 2 recovers Roth), Schlickewei (p-adic subspace) | Waldschmidt notes (imj-prg.fr), SMF Astérisque 317, arXiv 0907.2098; all far beyond mathlib's current Diophantine API |
| 3 | WebSearch (named-after / formalisations) | Thue-Siegel-Roth theorem formalized Lean 4 mathlib formalization 2025 | yes | lean-lang.org/eval problem `thue_siegel_roth` (statement only, `sorry`; says mathlib lacks Roth's lemma, auxiliary-polynomial machinery and an `IsDiophantine` predicate) | no existing mathlib formalisation; the project's Roth/LeanEval.lean proves exactly that problem statement |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` §6 Theorem (Roth), l.1140 | yes | "Let α be an irrational real algebraic number and let κ ∈ ℝ. Suppose there are infinitely many pairs of integers h, q with q > 0 such that |α − h/q| < 1/q^κ. Then κ ≤ 2" | Lean statement matches verbatim |
| 6 | nLab | "Roth's theorem", "irrationality measure" | no | no Diophantine-approximation entry | nLab has no number-theoretic approximation pages for this |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept (checked: Diophantine approximation has no categorical formulation in the literature) |
| 8 | Stacks Project | n/a | n/a | n/a | not algebraic geometry; Stacks has no Diophantine approximation chapter |
| 9 | MathOverflow / Math.SE | Roth theorem statement variants / reduction to algebraic integers | partial | standard remarks: constant C can be absorbed (any C vs C = 1 gives the same exponent), integrality is a WLOG scaling step | consistent with Roth.reduction and Roth.approxSet reports |
| 10 | recent arXiv (last 5 years) | Roth theorem formalisation; Roth for varieties | partial | Takloo-Bighash–Yin (the project's source paper); McKinnon–Roth (arXiv 1306.2976) Roth for varieties / Seshadri constants; GIT approach (arXiv 1305.0926) | generalisations out of mathlib scope; ℝ statement unchanged |

### Literature summary (Phase 3)

Concept identified as: Roth's theorem (Thue–Siegel–Roth theorem); irrationality exponent of algebraic numbers.
Sources agree on the standard form: yes.
Most general standard form: for every algebraic irrational α ∈ ℝ and every ε > 0, |α − p/q| < q^{−2−ε} has finitely many solutions; equivalently (with any constant C) α is not "approximable to order p" for any p > 2. In mathlib's vocabulary: for algebraic α and p > 2, ¬ LiouvilleWith p α, equivalently LiouvilleWith p α with p > 2 forces Transcendental ℤ α (exactly the sentence in mathlib's LiouvilleWith docstring).
Generality dimensions where the literature varies:
  - constant: literature uses an arbitrary constant C (or ε-form); project uses C = 1; equivalent for the exponent statement (evidence (1),(3)).
  - irrationality: literature includes it; in the LiouvilleWith form it is automatic (`LiouvilleWith.irrational`), so it disappears from the hypotheses (evidence (1)).
  - places / fields: Ridout (p-adic), Lang (number fields), Schmidt (subspace); out of scope for a first mathlib version.
Disagreement with the literature: none mathematically; the Lean phrasing via `approxSet` is the source's eq. (1), not mathlib's canonical predicate.

### Generality analysis — `Roth.roth`

Literature-standard form (from Phase 3): `IsAlgebraic ℚ α → 2 < p → ¬ LiouvilleWith p α` (equivalently `LiouvilleWith p α → 2 < p → Transcendental ℤ α`).

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `hα : Irrational α` | explicit hypothesis | absent in the LiouvilleWith form | yes (in LiouvilleWith form) | `LiouvilleWith.irrational` (p > 1) supplies it; compiled as `IsAlgebraic.not_liouvilleWith'` with no irrationality hypothesis (evidence (1)). In the approxSet form it is necessary (evidence (4)). |
| 2 | `halg : IsAlgebraic ℚ α` | over ℚ | over ℤ or ℚ | equivalent | `IsAlgebraic.extendScalars (FaithfulSMul.algebraMap_injective ℤ ℚ)` in one term (evidence (1'),(5)); ℚ is fine, mathlib's transcendence statements use `Transcendental ℤ`. |
| 3 | `hinf : (approxSet α κ).Infinite` | project set, constant 1 | `LiouvilleWith p α` (arbitrary constant, filter) | equivalent | bridge both ways compiled (evidence (1),(3)); approxSet is NO-composable per its own report |
| 4 | base field ℝ | ℝ | ℝ (p-adic/number-field versions are distinct theorems) | no | Ridout/Lang/Schmidt need new machinery, not a hypothesis drop |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD (in hypothesis count: `Irrational α` is superfluous once the statement is phrased with mathlib's `LiouvilleWith`; verified compiled, evidence (1)).
Number of weakening opportunities found: 1 hypothesis drop (Irrational) plus the vocabulary change approxSet to LiouvilleWith.
Proposed restatement (compiled in `.mathlib-quality/overview/evidence/Roth.roth/mathlib_form.lean`):

```lean
theorem IsAlgebraic.not_liouvilleWith {α p : ℝ} (halg : IsAlgebraic ℚ α) (hp : 2 < p) :
    ¬ LiouvilleWith p α

theorem LiouvilleWith.transcendental {α p : ℝ} (h : LiouvilleWith p α) (hp : 2 < p) :
    Transcendental ℤ α
```

Cost of restatement: CHEAP for the statement (a 6-line wrapper over `Roth.roth`, compiled). The upstreaming of the proof is EXPENSIVE (see 4.6), which is a sequencing matter, not a verdict factor.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | single real number, no structure | — |
| 2 | sequences to filters? | yes | `(approxSet α κ).Infinite` to `LiouvilleWith p α` (an `∃ᶠ n in atTop` predicate) | full LiouvilleWith API: `frequently_lt_rpow_neg`, `mul_rat`, `nat_mul`, `add_rat` (exponent invariance under rational affine maps), `ae_not_liouvilleWith`, `forall_liouvilleWith_iff` |
| 3 | construction to universal property? | no | — | — |
| 4 | set to bundled substructure? | no | the approxSet is a solution set, not a substructure | — |
| 5 | field-specific to weaker typeclasses? | no | ℝ is intrinsic; p-adic is Ridout's separate theorem | — |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | no | ℤ × ℕ pairs are absorbed into LiouvilleWith | — |
| 8 | concrete-via-abstract? | no | the proof body (via `roth_of_isIntegral`) genuinely uses the algebraicity of α (minimal polynomial, auxiliary polynomial with large index at (α,…,α)); no abstract witness | — |
| 9 | false-generalisation guard | checked, no false generalisation | `LiouvilleWith p α` for p > 2 is exactly "infinitely many approximations of order > 2 with some constant", same mathematical content (bridge iff compiled, evidence (1)+(3)); dropping `Irrational` is sound since rationals are never LiouvilleWith p, p > 1 | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `IsAlgebraic.not_liouvilleWith (halg : IsAlgebraic ℚ α) (hp : 2 < p) : ¬ LiouvilleWith p α`, with corollary `LiouvilleWith.transcendental (h : LiouvilleWith p α) (hp : 2 < p) : Transcendental ℤ α`.
  - Cost: CHEAP (statement wrapper, compiled); EXPENSIVE (proof upstreaming).
  - Mathlib downstream this enables: closes the gap stated in the LiouvilleWith.lean module docstring (l.26–28); `LiouvilleWith.transcendental` strictly strengthens the existing `Liouville.transcendental` (Liouville/Basic.lean:179), which needs all exponents, to any single exponent p > 2; combined with `LiouvilleWith.mul_rat`/`add_rat`/`nat_mul` it makes the project's `reduction` step free; gives an `irrationalityExponent`-style API a non-trivial theorem to anchor on; makes the lean-eval `thue_siegel_roth` statement a corollary.
  - Real mathematical improvement: removes a superfluous hypothesis and the project-local solution set, so the theorem plugs into mathlib's existing Diophantine-approximation predicate rather than a parallel one.

### Proof strategy — `Roth.roth`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | yes | the reduction step `Roth.reduction` becomes `LiouvilleWith.nat_mul` + `exists_nat_mul_isIntegral` (see Roth.reduction report, NO-composable); `roth_of_isIntegral` should consume `LiouvilleWith.frequently_lt_rpow_neg` | MODERATE |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | partial | approximant extraction from an infinite set vs from a `∃ᶠ` filter statement (same as row 1) | MODERATE |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes | Hasse derivatives and Taylor shifts on MvPolynomial (`MvPolynomial.hasseDeriv`, `MvPolynomial.taylor`, several YES reports), weighted index of a polynomial at a point, generalised Wronskians, Siegel's lemma variant / lattice point bounds, Roth's lemma (Θ bound), main lemma (BORDERLINE) | EXPENSIVE (separate PRs) |

### Proof strategy verdict (Phase 4.6)

Current strategy: REFACTOR-RECOMMENDED (only for an upstream version)
  - Proposed strategy: state and prove `IsAlgebraic.not_liouvilleWith`; reduce to integral α via `LiouvilleWith.nat_mul` (mathlib) and `exists_nat_mul_isIntegral`; feed the integral case from `LiouvilleWith.frequently_lt_rpow_neg`.
  - Cost: EXPENSIVE overall (the integral case depends on the full ~4.8k-line project).
  - Missing mathlib API: MvPolynomial Hasse derivatives / Taylor expansion, index of multivariate polynomials, generalised Wronskian criterion, Roth's lemma, main lemma.
  - Would refactoring make the proof strictly shorter / cleaner? yes for the wrapper (reduction becomes two mathlib calls); no change to the core argument.

### Diamond / defeq risk

n/a: declaration kind is theorem.

### Mathlib search-status: `Roth.roth`

[A] Lean-Finder       "Roth's theorem: an algebraic irrational real number is not LiouvilleWith p for any p > 2"   hits: `ae_not_liouvilleWith`, `LiouvilleWith.irrational`, `forall_liouvilleWith_iff`, `transcendental_liouvilleNumber`, `Liouville.liouvilleWith`, `liouville_liouvilleNumber`; none is Roth.
[B] Loogle            `LiouvilleWith, Transcendental`: no hits (no theorem links LiouvilleWith to transcendence).
[C] LeanSearch        "every irrational algebraic number has irrationality measure 2, finitely many rational approximations with exponent greater than 2"   hits: `setOf_liouville_eq_irrational_inter_iInter_iUnion`, `ae_not_liouvilleWith`, `Liouville.exists_pos_real_of_irrational_root` (Liouville, exponent = degree), `setOf_liouvilleWith_subset_aux`, `LiouvilleWith.frequently_lt_rpow_neg`, `Liouville`; none is Roth.
[D] Grep mathlib src  `Thue`, `theorem roth`, `Roth.roth`, `irrationalityExponent`, `IsDiophantine`, `IsAlgebraic.*LiouvilleWith`, `not_liouvilleWith`: only LiouvilleWith.lean l.27 (docstring: Thue–Siegel–Roth "states that such numbers must be transcendental") and `ae_not_liouvilleWith` (Measure.lean:115); "Roth" elsewhere is the combinatorial Roth (Combinatorics/Additive/Corner/Roth.lean, ETransform, SimpleGraph/Triangle) or the author Rothgang.
[E] Name pattern      `not_liouvilleWith`, `LiouvilleWith.transcendental`, `roth`: only `ae_not_liouvilleWith`; `Liouville.transcendental` (Basic.lean:179) exists for full Liouville numbers only.

Searched for both:
  - the user's current form (approxSet, Irrational + IsAlgebraic ⇒ κ ≤ 2)
  - the literature-standard form (`¬ LiouvilleWith p α` for algebraic α, p > 2; transcendence of LiouvilleWith p, p > 2)

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form). Closest: Liouville's theorem (exponent deg α), `Liouville.transcendental`, `ae_not_liouvilleWith`. Genuine gap, explicitly flagged in mathlib's own docstring.

### Normal-form check — `Roth.roth`

Equivalent formalisms: (a) `approxSet α κ` infinite ⇒ κ ≤ 2 (project); (b) ∀ p > 2, ¬ LiouvilleWith p α (mathlib predicate); (c) LiouvilleWith p α, p > 2 ⇒ Transcendental ℤ α (mathlib docstring phrasing); (d) lean-eval `IsDiophantine` (∀ ε > 0, ∃ C > 0, C/q^{2+ε} < |α − p/q|).
Does mathlib already have a canonical form for this idea? yes: `LiouvilleWith` (Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleWith.lean).
Is our statement stated against the canonical form? NO: it uses (a). REFACTOR target: (b) as the main theorem, (c) as a corollary; (a) and (d) become `↔ LiouvilleWith`-side bridge lemmas if kept at all (project already has `isDiophantine_iff` against (a); it should be re-aimed at (b)).
RHS convention respected? n/a (not an iff); bridge lemmas should have `LiouvilleWith` on the RHS.

### Syntactic generality — `Roth.roth`

Alternative restatements attempted (all compiled, evidence file):
- current approxSet form with `Irrational`, `IsAlgebraic ℚ`.
- `IsAlgebraic ℤ` variant (evidence (5)).
- `IsAlgebraic.not_liouvilleWith'` with no `Irrational` (evidence (1), (1') over ℤ).
- `LiouvilleWith.transcendental'` (evidence (2)).
- `Roth.roth` recovered from (1) (evidence (3)), confirming no content loss.

Chosen restatement: `IsAlgebraic.not_liouvilleWith` (dot notation on the algebraicity hypothesis, fewest hypotheses) with `LiouvilleWith.transcendental` as the user-facing corollary.
Justification: callers typically hold `IsAlgebraic`/`IsIntegral` facts or a `LiouvilleWith` fact; neither form needs an irrationality proof, and both compose with the existing LiouvilleWith API.

### Superfluous-argument audit — `Roth.roth`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hα : Irrational α` | yes in approxSet form; no in LiouvilleWith form | approxSet form: necessary (evidence (4): `approxSet 0 3` infinite, 0 algebraic). LiouvilleWith form: drop (evidence (1)). |
| 2 | `halg : IsAlgebraic ℚ α` | yes | the whole content; ℤ/ℚ interchangeable |
| 3 | `hinf` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (target `¬ LiouvilleWith p α`, corollary `Transcendental ℤ α`)
Syntactic generality: RESTATE (`IsAlgebraic.not_liouvilleWith`)
Superfluous arguments: 1 to drop in the restated form (`Irrational α`)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.roth`

Internal use count: 1 outside the declaring file (plus 1 in it)
External-to-file callers: 1 file (Roth/LeanEval.lean)

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Main.lean:583 (`Roth.roth_rat`) | `refine roth hα halg ((hinf.image (f := fun x : ℚ ↦ (x.num, x.den))) ...).mono ?_)` |
| Roth/LeanEval.lean:64 (`thueSiegelRoth`) | `(Roth.roth _h_irr (_h_alg.extendScalars (FaithfulSMul.algebraMap_injective ℤ ℚ)))` |

Inline-derivation grep (`reduction` + `roth_of_isIntegral` combined elsewhere in `Roth/`): none; `roth_of_isIntegral` is used only in `Roth.roth`.
Note: `Roth.roth_rat` is another approxSet-flavoured restatement; in the LiouvilleWith version it would be subsumed (the `x.den` form is exactly what `LiouvilleWith` quantifies over).

### Composition check (Phase 6)

Can `Roth.roth` be derived from mathlib in ≤3 chained calls?

Attempt 1 (mathlib only): `Liouville.exists_pos_real_of_irrational_root` gives exponent ≤ deg α; `ae_not_liouvilleWith` gives exponent ≤ 2 only almost everywhere, with no information on algebraic numbers (a null set).
  - Result: fails for every algebraic α of degree ≥ 3.
Attempt 2 (mathlib + project reduction): `LiouvilleWith.nat_mul` + `exists_nat_mul_isIntegral` reduce to the integral case, which still needs `Roth.roth_of_isIntegral` (the whole project).
  - Result: partial; the reduction is composable (Roth.reduction report), the core is not.

Conclusion: NOT-COMPOSABLE.

### Phase 7 gate

- Literature table: 10 rows, 3 WebSearch at different generality levels, local refs, n/a channels justified, ChatGPT MCP recorded n/a (unavailable): yes.
- STRICTLY NARROWER claim verified by compiling the weakened statement: yes (evidence (1), zero diagnostics).
- Proposed restatement matches the literature-standard and modern-idiom target: yes.
- MODERN-IDIOM downstream consequences listed concretely: yes (Phase 4c).
- Q9 false-generalisation: no false generalisation (bridge iff compiled).
- Mathlib search (5 methods, both forms): yes, no hit.
- Composition: NOT-COMPOSABLE.
- Call-sites table, 4.6 and 5.5 verdicts present: yes.
- Cost not used as a downgrade reason: the EXPENSIVE proof upstreaming is recorded as sequencing.

### Verdict: `Roth.roth`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): standard Thue–Siegel–Roth theorem (irrationality exponent 2 for algebraic irrationals); the project's statement is the source's §6 Theorem verbatim.
- Generality analysis (Phase 4): STRICTLY NARROWER (superfluous `Irrational` once phrased with `LiouvilleWith`), compiled; modern idiom `LiouvilleWith` available.
- Mathlib search (Phase 5): not in mathlib; mathlib's LiouvilleWith docstring names the theorem as missing content.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

This is the clearest mathlib gap in the project. Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleWith.lean states in its module docstring that for p > 2 the Thue–Siegel–Roth theorem says LiouvilleWith numbers must be transcendental, yet nothing proves it; mathlib only has Liouville's degree bound, `Liouville.transcendental` (all exponents), and the measure-theoretic `ae_not_liouvilleWith`. The lean-eval benchmark lists the theorem as an open target and explicitly notes the missing Roth machinery. The project's `Roth.roth` proves it, sorry-free.

The declaration is not shippable as stated, though. It is phrased via the project-local `approxSet` (itself NO-composable: it is a parallel encoding of `LiouvilleWith`), and in mathlib's vocabulary the `Irrational α` hypothesis is superfluous because `LiouvilleWith.irrational` supplies it. The evidence file compiles `IsAlgebraic.not_liouvilleWith'` (no irrationality hypothesis) and `LiouvilleWith.transcendental'` from `Roth.roth`, and recovers `Roth.roth` from them, so the restatement keeps all the content. Upstreaming the proof means landing the whole development bottom-up. Several leaves are YES on their own (MvPolynomial Hasse derivatives and Taylor shifts), while the index/Θ/main-lemma layers are BORDERLINE because of source-specific constants. That makes the cost EXPENSIVE, which affects sequencing but not the bucket. It also leaves a scope question for the authors (questions below).

Reason for the generalisation: MODERN-IDIOM (Bourbaki 2.0: `approxSet` to mathlib's `LiouvilleWith`) and LITERATURE-WEAKENING (drop `Irrational`, which the literature's "algebraic number with exponent > 2 approximations" form never needs once rationals are excluded by the predicate).

Proposed restatement:
```lean
/-- **Thue–Siegel–Roth theorem.** -/
theorem IsAlgebraic.not_liouvilleWith {α p : ℝ} (halg : IsAlgebraic ℚ α) (hp : 2 < p) :
    ¬ LiouvilleWith p α := by
  sorry  -- current proof survives: Roth.roth + LiouvilleWith.irrational + bridge (compiled)

theorem LiouvilleWith.transcendental {α p : ℝ} (h : LiouvilleWith p α) (hp : 2 < p) :
    Transcendental ℤ α :=
  fun halg ↦ (halg.extendScalars (FaithfulSMul.algebraMap_injective ℤ ℚ)).not_liouvilleWith hp h
```

Estimated cost of regeneralisation: CHEAP for the statement (done in evidence); EXPENSIVE for an upstream proof (all dependencies). EXPENSIVE does not downgrade the verdict.

Mathlib downstream this enables:
- discharges the LiouvilleWith.lean docstring claim with an actual theorem, and strengthens `Liouville.transcendental` from "all exponents" to "any single exponent p > 2";
- composes with `LiouvilleWith.mul_rat`, `add_rat`, `nat_mul`, `frequently_lt_rpow_neg`, `ae_not_liouvilleWith`, so the project's `reduction` and `roth_rat` become trivial or unnecessary;
- the lean-eval `thue_siegel_roth` statement follows from it in a few lines (the project's `isDiophantine_iff` re-aimed at LiouvilleWith).

Upstreaming path (bottom-up, each a separate PR series):
1. MvPolynomial Hasse derivatives and Taylor shift (`Roth/HasseDeriv.lean`, `Roth/Taylor.lean`; the YES-verdict reports in this overview) into Mathlib/RingTheory/MvPolynomial/ or Mathlib/Algebra/MvPolynomial/.
2. Box / coefficient-norm / Siegel-lemma lattice bounds (`Roth/Box.lean`, `Roth/Lattice.lean`, `Roth/CoeffNorm.lean`) against existing mathlib Siegel's lemma (`Mathlib/NumberTheory/SiegelsLemma.lean`) where possible.
3. Generalised Wronskians (`Roth/Wronskian.lean`, `Roth/GenWronskian.lean`).
4. Index, Θ bounds, separation, main lemma (`Roth/Index.lean`, `Roth/Theta.lean`, `Roth/Separation.lean`, `Roth/MainLemma.lean`), restated without source equation numbers.
5. New file Mathlib/NumberTheory/Transcendental/Liouville/Roth.lean (imports LiouvilleWith.lean) with `IsAlgebraic.not_liouvilleWith` and `LiouvilleWith.transcendental`; the integral case and the `_aux` assembly steps become private.

Open questions for the authors (scope, not bucket):
1. Pursue upstreaming the full development to mathlib (vs keeping a standalone mathlib-dependent repository and upstreaming only steps 1–3)? Recommended: upstream steps 1–3 first, decide on 4–5 with mathlib reviewers on Zulip.
2. Add the LiouvilleWith-form wrappers (`IsAlgebraic.not_liouvilleWith`, `LiouvilleWith.transcendental`) to Roth/Main.lean now? Recommended: yes.

Pre-PR checklist before opening (for step 5):
- [ ] `/generalise Roth.roth` re-run against the LiouvilleWith target
- [ ] `/cleanup Roth/Main.lean` with the restated theorem
- [ ] Reviewer from Mathlib/NumberTheory/Transcendental/ history (LiouvilleWith authors)

Next action: add the compiled LiouvilleWith wrappers to Roth/Main.lean and re-aim `isDiophantine_iff` at them; start the upstream series at the MvPolynomial Hasse-derivative/Taylor API.

### Next step

Add `IsAlgebraic.not_liouvilleWith` / `LiouvilleWith.transcendental` (from evidence) next to `Roth.roth`; keep `Roth.roth` (callers Main.lean:583, LeanEval.lean:64). Upstream bottom-up, ending in Mathlib/NumberTheory/Transcendental/Liouville/Roth.lean.

## Evidence
- Evidence file: `.mathlib-quality/overview/evidence/Roth.roth/mathlib_form.lean` (imports `Roth.Main`, LiouvilleWith), `lean_diagnostic_messages`: no errors, no warnings. Contents: (1) `IsAlgebraic.not_liouvilleWith'` (no `Irrational` hypothesis) from `Roth.roth` + `LiouvilleWith.irrational` + bridge; (1') ℤ-coefficient version; (2) `LiouvilleWith.transcendental'`; (3) `Roth.roth` recovered from (1) (no content loss); (4) `approxSet 0 3` infinite with 0 algebraic (Irrational necessary in approxSet form); (5) `IsAlgebraic ℤ` version in one term.
- WebSearch ×3 (table rows 1–3); Lean-Finder ×1, LeanSearch ×1, Loogle ×1 (`LiouvilleWith, Transcendental`: no hits); grep of mathlib for `Thue`, `Roth`, `not_liouvilleWith`, `IsDiophantine`, `irrationalityExponent`, `transcendental`; grep of clean.tex (l.1140). ChatGPT MCP unavailable in this session.
- Related reports read: Roth.roth_of_isIntegral.md (BORDERLINE), Roth.approxSet.md (NO-composable), Roth.reduction.md (NO-composable), Roth.main_lemma.md (BORDERLINE).
