---
decl: Roth.abs_eval_lt_of_le_index
file: Roth/Main.lean
line: 380
kind: theorem
visibility: public
verdict: BORDERLINE-needs-human
cost: MODERATE
junk: KEEP
rationale: Roth §7 upper bound for Q(h/q) from the Taylor expansion at (α,…,α) once the index is at least c; a named step of the Roth proof, not a standalone mathlib lemma; built on project-only API (index, eval_eq_sum_box, hasseDeriv) with all seven hypotheses load-bearing, so it only goes upstream if the whole Roth development (and Roth.index, itself BORDERLINE) does.
action: Keep in Roth/Main.lean for its single caller one_lt_roth_eval_bound_aux (Roth/Main.lean:477); revisit only if the Roth proof is upstreamed (Mathlib/NumberTheory/DiophantineApproximation/Roth or Archive), together with Roth.index and the MvPolynomial Taylor PR.
---

# Roth.abs_eval_lt_of_le_index

## Inventory entry

### `theorem Roth.abs_eval_lt_of_le_index`
- **Type**: `{m : ℕ} [NeZero m] {Q : MvPolynomial (Fin m) ℝ} {r : Fin m → ℕ} (hd : ∀ j, degreeOf j Q ≤ r j) {α c : ℝ} (hidx : c ≤ index Q (fun _ ↦ α) r) {h : Fin m → ℤ} {q : Fin m → ℕ} (hq : ∀ j, 0 < q j) {κ : ℝ} (hκ : 0 ≤ κ) (happ : ∀ j, |α - (h j : ℝ) / q j| ≤ 1 / (q j : ℝ) ^ κ) (hqr : ∀ j, (q 0 : ℝ) ^ ((r 0 : ℝ) / r j) ≤ q j) {C : ℝ} (hC : ∀ i : Fin m →₀ ℕ, |eval (fun _ ↦ α) (hasseDeriv i Q)| < C) : |eval (fun j ↦ (h j : ℝ) / q j) Q| < (∏ j, ((r j : ℝ) + 1)) * C * (q 0 : ℝ) ^ (-(r 0 : ℝ) * c * κ)`
- **What**: If `Q` has partial degrees at most `r_j`, index at least `c` at `(α, …, α)`, all Hasse derivatives at that point bounded by `C`, and each `h_j/q_j` approximates `α` to order `κ` with `q_j ≥ q_0^{r_0/r_j}`, then `|Q(h/q)| < ∏(r_j+1) · C · q_0^{-r_0 c κ}`.
- **How**: Rewrites `Q(h/q)` by the Taylor formula `MvPolynomial.eval_eq_sum_box`; bounds each term: terms with vanishing Hasse coefficient trivially, others via `hC` and the private `abs_prod_pow_le_rpow_of_le_weight` fed by `Roth.index_le_weight` (`hidx.trans (index_le_weight h0)`), combined by `mul_lt_mul_of_lt_of_le_of_nonneg_of_pos`; sums with `Finset.abs_sum_le_sum_abs`, `Finset.sum_lt_sum_of_nonempty`, `Finset.sum_const`, `Roth.card_box`.
- **Hypotheses**: `hd` (partial degree bounds), `hidx` (index lower bound), `hq` (positive denominators), `hκ` (nonnegative exponent), `happ` (approximation quality), `hqr` (denominator growth eq. (52)), `hC` (Hasse-derivative bound, Lemma 9 (3)).
- **Uses from project**: `MvPolynomial.eval_eq_sum_box`, `MvPolynomial.hasseDeriv`, `Roth.index`, `Roth.index_le_weight`, `Roth.box`, `Roth.mem_box`, `Roth.card_box`, `Roth.abs_prod_pow_le_rpow_of_le_weight` (private)
- **Used by**: Roth/Main.lean:477 (`one_lt_roth_eval_bound_aux`, the final contradiction); mentioned in the module docstring Roth/Main.lean:39.
- **Visibility**: public
- **Lines**: 372–407 (docstring 372–379, statement 380–387), proof length 20 lines
- **Notes**: Source: clean.tex §7 l.1656–1672.

## Junk check (Step 8)
- Used anywhere? Yes, once (Roth/Main.lean:477).
- Wrapper of 1–2 mathlib calls? No: 20-line proof combining the project Taylor formula, index bound and a private monomial estimate.
- Does mathlib have it? No (Loogle `|MvPolynomial.eval _ _| < _`: no hits; LeanSearch/Lean-Finder: only univariate `Polynomial.taylor_coeff`, Liouville lemmas; mathlib's "Roth" files are the combinatorial 3-AP Roth theorem).
- Too specific / inline? It is a named paragraph of the paper; inlining would lengthen the already long final argument. Keep separate.
- Well-chosen? Yes for the project.
- Conclusion: `KEEP`. Action: none locally.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring not internal/auxiliary; Step 8 KEEP; qualified name absent from mathlib (grep `abs_eval_lt_of_le_index` over `.lake/packages/mathlib/Mathlib/`: no hits). Not a glue lemma (20-line proof). Full workflow below.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; the LSP elaborated Roth/Main.lean without errors during the minimal-hypotheses run)
- decl `Roth.abs_eval_lt_of_le_index`:  resolved at Roth/Main.lean:380
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Proof of Roth's theorem from the main lemma (Lemma 9): choice of approximations, degrees, and the final contradiction.

### Statement (Phase 1)

`Roth.abs_eval_lt_of_le_index` is a theorem stating the following: let `Q ∈ ℝ[x_1, …, x_m]` with `deg_{x_j} Q ≤ r_j`, whose index at `(α, …, α)` with respect to `r` is at least `c` (i.e. every Hasse derivative `Δ_d Q(α,…,α)` with `∑ d_j/r_j < c` vanishes), and with `|Δ_d Q(α,…,α)| < C` for all `d`. If `|α − h_j/q_j| ≤ q_j^{-κ}` and `q_j ≥ q_1^{r_1/r_j}` for all `j`, then `|Q(h_1/q_1, …, h_m/q_m)| < (r_1+1)⋯(r_m+1) · C · q_1^{-r_1 c κ}`.

Variables / typeclasses involved (Lean side):
- `m : ℕ`, `[NeZero m]` (so the distinguished index `0 : Fin m` exists), variables `Fin m`.
- `Q : MvPolynomial (Fin m) ℝ`; `r : Fin m → ℕ` degree bounds/weights; `α c κ C : ℝ`; `h : Fin m → ℤ`, `q : Fin m → ℕ`.

Hypotheses (Lean side):
- `hd`, `hidx`, `hq`, `hκ`, `happ`, `hqr`, `hC` as in the inventory.

Conclusion (math): `|Q(h/q)| < ∏(r_j+1) · C · q_1^{-r_1 c κ}`.

Conclusion (Lean): `|eval (fun j ↦ (h j : ℝ) / q j) Q| < (∏ j, ((r j : ℝ) + 1)) * C * (q 0 : ℝ) ^ (-(r 0 : ℝ) * c * κ)`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: one estimate inside the proof of Roth's theorem (§7), not a main result, not named.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 20 (theorem)
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE (check skipped for theorems)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth's theorem proof upper bound auxiliary polynomial at rational point Taylor expansion index Hasse derivatives q_1^{-r_1 gamma kappa} | partial | proof outlines (Wikipedia Roth's theorem; arXiv 2502.00731; Nickel arXiv 2005.06531): construct P, lower-bound its index at the approximations, upper-bound via Roth's lemma | the Taylor upper bound is an unnamed routine step |
| 2 | WebSearch (general form) | polynomial vanishing to high weighted order at a point small value near the point Taylor expansion bound Diophantine approximation index | partial | general auxiliary-polynomial method (arXiv 1601.02243, 1001.1534 weighted order of vanishing, Roy–Waldschmidt math/0207102 small values with derivatives) | no standalone lemma in this form |
| 3 | WebSearch (named-after / aliases) | Thue-Siegel-Roth "index" polynomial upper bound product of approximations Schmidt Diophantine Approximation lecture notes | partial | Schmidt LNM 785 Ch. II/IV; Evertse notes dio19-6; Klazar NDMI045 notes; Mignotte notes | estimate appears inline in each proof, with proof-specific constants |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` l.1656–1672 | yes | "terms with ∑ i_j/r_j < γ−η vanish ... `|Q(h/q)| < (r_1+1)⋯(r_m+1) B_1^{1+3δ} q_1^{-r_1(γ−η)κ}`" | exactly the project statement with c = γ−η, C = B_1^{1+3δ} |
| 6 | nLab | index of a polynomial / Roth theorem | no | — | no Diophantine-approximation estimates on nLab |
| 7 | nCatLab | — | n/a | — | not a categorical statement (real-analytic estimate) |
| 8 | Stacks Project | — | n/a | — | no archimedean Diophantine estimates in Stacks |
| 9 | MathOverflow / Math.SE | (results of #1–#3) | no | — | no dedicated discussion of this step found |
| 10 | recent arXiv (last 5 years) | (results of #1, #3) | partial | arXiv 2502.00731 (2025) Roth/subspace exposition | same inline step |

### Literature summary (Phase 3)

Concept identified as: the "upper bound" half of the Thue–Siegel–Roth method: a polynomial of large index at `(α,…,α)` takes a small value at a point of good simultaneous approximations (Taylor expansion plus termwise estimate).
Sources agree on the standard form: yes in substance, but every source states it inline with its own normalisations (which `q_j` is distinguished, how the Hasse coefficients are bounded, strict vs non-strict).
Most general standard form: for a polynomial `Q` with index `≥ c` at `α`, `|Q(x)| ≤ ∑_{d ∈ box r, wt(d) ≥ c} |Δ_d Q(α)| ∏ |x_j − α_j|^{d_j}`, then specialised to approximations. No source isolates it as a named lemma.
Generality dimensions where the literature varies:
  - point `(α,…,α)` vs general `α ∈ ℝ^m` (the proof does not need equal coordinates, but `index` is applied at the diagonal point in the project).
  - archimedean `|·|` vs arbitrary absolute value (Bombieri–Gubler work with places).
  - normalisation of the decay (here via the distinguished `q_0` and `hqr`).
Disagreement with the literature: none (matches clean.tex with `c = γ − η`).

### Generality analysis — `Roth.abs_eval_lt_of_le_index`

Literature-standard form (from Phase 3): no isolated standard form; the paper's inline estimate, which the project matches.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `hd` | `degreeOf j Q ≤ r j` | same | no | load-bearing (needed by `eval_eq_sum_box`); confirmed by `lean_minimal_hypotheses` |
| 2 | `hidx` | `c ≤ index Q α r` | same | no | load-bearing |
| 3 | `hq` | `0 < q j` | same | no | load-bearing |
| 4 | `hκ` | `0 ≤ κ` | same | no | load-bearing (used by the monomial estimate) |
| 5 | `happ` | `|α − h_j/q_j| ≤ q_j^{-κ}` | same (paper: strict) | no | load-bearing; already the weaker non-strict form |
| 6 | `hqr` | `q_0^{r_0/r_j} ≤ q_j` | same (eq. (52)) | no | load-bearing |
| 7 | `hC` | `∀ i, |Δ_i Q(α)| < C` | `∀ i ∈ box r` would suffice | marginal | only terms in `box r` are used, but derivatives outside the box vanish by `hd`, so the two forms are equivalent; not a real weakening |
| 8 | `h : Fin m → ℤ`, `q : ℕ` | integer/natural approximants | real points `x_j` with `|x_j − α| ≤ q_j^{-κ}` | yes in principle | integrality is not used in this proof; restating over real `x` changes the statement shape for no current consumer; not pursued (no weakening claimed) |
| 9 | target `ℝ` | `ℝ` | `ℝ` | no | `Real.rpow` exponents essential |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (for the project's purposes; every explicit hypothesis is load-bearing per `lean_minimal_hypotheses`; no weakening claimed or compiled)
Number of weakening opportunities found: 0 verified (row 8 noted as a possible restatement, not claimed)
Proposed restatement: none.
Cost of restatement: n/a

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | hypotheses are numerical data conditions |
| 2 | sequences to filters? | no | — | a single finite inequality |
| 3 | construction vs universal property? | no | — | — |
| 4 | bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | no | — | needs ordered field with `rpow`: `ℝ` |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | marginal | `Fin m` with distinguished `0` to `[Fintype σ]` with a chosen `i₀` | none: purely cosmetic for a single caller |
| 8 | concrete-via-abstract? | no | the statement names no concrete object; the abstract content is "Taylor + index ⇒ smallness" which already lives in `eval_eq_sum_box` and `index_le_weight` | — |
| 9 | false-generalisation guard | no false generalisation | no generalisation proposed | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - Reason: a concrete numerical estimate in the Roth argument; the reusable abstractions (`MvPolynomial.taylor`/`hasseDeriv`, `eval_eq_sum_box`, a weighted order) are assessed separately.

### Proof strategy — `Roth.abs_eval_lt_of_le_index`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes | `MvPolynomial` Taylor formula (`eval_eq_sum_box`, YES-but-generalise-first) and a weighted order at a point (Roth.index, BORDERLINE) | MODERATE (separate PRs) |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (Taylor expansion, termwise bound, `Finset.sum_lt_sum_of_nonempty`).
  - Missing mathlib API: the MvPolynomial Taylor PR and an index/weighted order; once present, the proof is unchanged.

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.abs_eval_lt_of_le_index`

[A] Lean-Finder       "polynomial with high index (weighted order of vanishing) at (α,…,α) takes small value at a good rational approximation point, Roth's theorem"   hits: `Liouville.exists_pos_real_of_irrational_root`, `one_le_pow_mul_abs_eval_div` (univariate Liouville; not this)
[B] Loogle            `|MvPolynomial.eval _ _| < _`   no hits
[C] LeanSearch        "absolute value of multivariate polynomial at point near alpha bounded using Taylor expansion and Hasse derivatives"   hits: `Polynomial.taylor_coeff` (univariate), analytic power-series big-O lemmas (unrelated)
[D] Grep mathlib src  `abs_eval_lt_of_le_index`, `Roth's theorem`, `hasseDeriv`, `abs_eval_lt`   hits: only `Algebra/Polynomial/HasseDeriv.lean`, `Algebra/Polynomial/Taylor.lean` (univariate), and `Combinatorics/Additive/.../Roth.lean` (combinatorial 3-AP Roth, unrelated)
[E] Name pattern      `index_le_weight`, `eval_eq_sum_box`, `card_box` (lean_local_search / project)   hits: project-only

Searched for both the user's form and the literature form (Taylor-plus-index smallness bound).

Concluded: not in mathlib (all 5 methods exhausted); mathlib lacks even the prerequisites (`MvPolynomial.hasseDeriv`, `taylor`, an index).

### Normal-form check — `Roth.abs_eval_lt_of_le_index`

Equivalent formalisms: (a) strict bound with `∏(r_j+1) · C · q_0^{-r_0 c κ}` (project, paper); (b) non-strict bound `≤ ∑_{d} |Δ_d Q(α)| ∏|x_j−α|^{d_j}` followed by a separate numerical estimate.
Does mathlib already have a canonical form for this idea? no.
Canonical form we'd propose: (b)-style general Taylor remainder bound plus (a) as the Roth corollary, if ever upstreamed.
RHS convention respected? yes.

### Syntactic generality — `Roth.abs_eval_lt_of_le_index`

Alternative restatements attempted:
- (a) current statement.
- real points `x` with `|x_j − α| ≤ q_j^{-κ}` instead of `h_j/q_j` (not compiled; not claimed).
Chosen restatement: current form.
Justification: matches the single caller verbatim (`happ` and `hq0` from the approximant choice are passed directly).

### Superfluous-argument audit — `Roth.abs_eval_lt_of_le_index`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[NeZero m]` | yes | distinguished index `0` |
| 2 | `hd` | yes | `lean_minimal_hypotheses`: load-bearing |
| 3 | `hidx` | yes | load-bearing |
| 4 | `hq` | yes | load-bearing |
| 5 | `hκ` | yes | load-bearing |
| 6 | `happ` | yes | load-bearing |
| 7 | `hqr` | yes | load-bearing |
| 8 | `hC` | yes | load-bearing |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (as a project lemma)

### Call sites — `Roth.abs_eval_lt_of_le_index`

Internal use count: 0 outside the declaring file (1 in the declaring file)
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Main.lean:477 (`one_lt_roth_eval_bound_aux`) | `(mul_lt_mul_of_pos_left (abs_eval_lt_of_le_index hdmap hidx_strict.le hq0 hκ0 happ hqr hC) ...)` |
| Roth/Main.lean:39 | module docstring mention only |

Inline-derivation grep (`eval_eq_sum_box`, `index_le_weight` over `Roth/`):
  - (none) — `eval_eq_sum_box` is used only here (Main.lean:390); `index_le_weight` elsewhere only within Roth/Index.lean for index API.

### Composition check (Phase 6)

Can the statement be derived from mathlib in ≤3 chained calls?

Attempt 1: mathlib primitives only
  - Mathlib decls used: none applicable (no `MvPolynomial` Taylor formula, no Hasse derivatives for `MvPolynomial`, no index)
  - Result: fails.
Attempt 2: project API
  - Decls used: `eval_eq_sum_box`, `index_le_weight`, `abs_prod_pow_le_rpow_of_le_weight`, `card_box`, plus `Finset.abs_sum_le_sum_abs`, `Finset.sum_lt_sum_of_nonempty`
  - Result: succeeds only as the existing 20-line proof (case split on vanishing coefficients, termwise strict bound, summation).
Conclusion: NOT-COMPOSABLE

### Verdict: `Roth.abs_eval_lt_of_le_index`

**Category:** BORDERLINE-needs-human

**Evidence:**
- Literature search (Phase 3): the step is standard but always inline in Roth/Thue–Siegel proofs (clean.tex §7; Schmidt LNM 785; Bombieri–Gubler); never a named general lemma.
- Generality analysis (Phase 4): MAXIMALLY GENERAL for its use; all seven explicit hypotheses load-bearing.
- Mathlib search (Phase 5): not in mathlib; prerequisites (`MvPolynomial.taylor`/`hasseDeriv`, an index) also absent.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

This is the §7 upper-bound estimate of Roth's proof: combine the multivariate Taylor formula at `(α,…,α)` with the index lower bound to show that `Q` is small at the approximation point. Mathematically it is correct, maximally general for its role and not derivable from mathlib, so the NO buckets do not apply. But it is not a free-standing mathlib lemma either: its hypotheses (`hqr`, the distinguished `q_0`, the shape of `hC`) are tuned to Roth's argument, it has a single caller, and it depends on project definitions (`Roth.index`, verdict BORDERLINE-needs-human; `MvPolynomial.eval_eq_sum_box`, YES-but-generalise-first, still unshipped). Whether it goes upstream is a project-policy decision about Roth's theorem as a whole, not about this lemma.

The reusable content (Taylor formula, weighted order at a point, multivariate Liouville bound `one_le_prod_pow_mul_abs_eval`) is already covered by those separate assessments. If Roth's theorem goes to mathlib, this lemma would ship unchanged as part of that file.

Numbered questions:
1. Should the full proof of Roth's theorem be upstreamed (e.g. to Mathlib/NumberTheory/DiophantineApproximation/Roth.lean)? If yes, this lemma ships unchanged with it; if no, it stays project-local.
2. If upstreamed, should this be stated with the general Taylor remainder bound `|Q(x)| ≤ ∑_{d ∈ box r, c ≤ wt d} |Δ_d Q(α)| ∏ |x_j − α_j|^{d_j}` split out as a separate lemma (real points `x`, any `α : σ → ℝ`), with the current form as the corollary?
3. Should it wait on the decision for `Roth.index` (real-valued sInf vs `MvPowerSeries.weightedOrder` of `taylor`), since `hidx` is stated through it?

Next action: user answers the questions; meanwhile keep the lemma in Roth/Main.lean for its single caller (line 477).

---

### Next step

Keep locally; revisit only if the user decides to upstream Roth's theorem, together with `Roth.index` and the MvPolynomial Taylor PR.

## Evidence
- `lean_minimal_hypotheses` on Roth/Main.lean `abs_eval_lt_of_le_index` (LSP scratch variants, project file not edited): all seven explicit hypotheses (`hd`, `hidx`, `hq`, `hκ`, `happ`, `hqr`, `hC`) load-bearing.
- No evidence Lean file written: no weakening is claimed.
- Loogle (1), LeanSearch (1), Lean-Finder (1) queries and mathlib greps as recorded in the search-status block.
- WebSearch: 3 queries (literature table). ChatGPT MCP: n/a (not configured). Local refs: clean.tex l.1656–1672.
- Project greps: `grep -rn abs_eval_lt_of_le_index Roth/` (Main.lean:39 docstring, :380 decl, :477 call).
