---
decl: Roth.sum_natDegree_update_lt
file: Roth/Wronskian.lean
line: 182
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: n/a
junk: KEEP
rationale: Project-specific induction measure (sum of natDegrees drops after one leading-term elimination); its only mathematical content is mathlib's degree_sub_lt_left (equivalently the division-free cancelLeads API) lifted through Finset.sum_lt_sum, and the hypotheses weaken (verified) to phi nu ne 0 plus nonvanishing of the updated member.
action: Do not upstream; keep locally for its sole call site Roth/Wronskian.lean:213 (wronskian_ne_zero_of_linearIndependent), optionally restating with the verified weaker hypotheses (hp, hne, any Fintype index, DivisionRing) or inlining the degree_sub_lt_left plus Finset.sum_lt_sum composition there.
---

# Roth.sum_natDegree_update_lt

## Inventory entry

### `theorem Roth.sum_natDegree_update_lt`
- **Type**: `{K : Type*} [Field K] {l : ℕ} {φ : Fin l → K[X]} (hφ : LinearIndependent K φ) {ν ν' : Fin l} (h : ν ≠ ν') (hdeg : (φ ν).natDegree = (φ ν').natDegree) : ∑ ρ, (Function.update φ ν' (φ ν' - C ((φ ν').leadingCoeff / (φ ν).leadingCoeff) * φ ν) ρ).natDegree < ∑ ρ, (φ ρ).natDegree`
- **What**: In a linearly independent family of polynomials, if two distinct members have equal degree, replacing `φ ν'` by `φ ν' - (lc φ ν' / lc φ ν) φ ν` (cancelling its leading term) strictly decreases the total degree `∑ deg φ ρ`.
- **How**: Gets `φ i ≠ 0` from `LinearIndependent.ne_zero`; nonvanishing of the updated member from the project lemma `linearIndependent_update_sub_smul`; the pointwise strict drop from mathlib's `degree_sub_lt_left` (after `degree_C_mul`, `leadingCoeff_mul`, `leadingCoeff_C`, `div_mul_cancel₀`) and `natDegree_lt_natDegree`; then `Finset.sum_lt_sum` with `Function.update_of_ne` for the other indices.
- **Hypotheses**: `[Field K]` (section variable); `hφ : LinearIndependent K φ`; `h : ν ≠ ν'`; `hdeg` equal natDegrees.
- **Uses from project**: `Roth.linearIndependent_update_sub_smul`
- **Used by**: Roth/Wronskian.lean:213 (`wronskian_ne_zero_of_linearIndependent`, decreasing measure in the strong induction). No other project use.
- **Visibility**: public
- **Lines**: 182–204, proof length 19 lines
- **Notes**: `hφ` and `h` are used only to obtain `φ ν ≠ 0` and `φ ν' - C a * φ ν ≠ 0`; both can be taken directly as hypotheses (verified in evidence file).

## Junk check (Step 8)
- Used anywhere? Yes, once (Roth/Wronskian.lean:213), as the termination measure of the strong induction in the hard direction of the Wronskian criterion.
- Wrapper of 1–2 mathlib calls? Nearly: `degree_sub_lt_left` (pointwise) plus `Finset.sum_lt_sum` (summing), with some leading-coefficient bookkeeping. Not a bare wrapper, but no new mathematics.
- Does mathlib have it? The pointwise fact yes (`Polynomial.degree_sub_lt_left`; division-free version `Polynomial.natDegree_cancelLeads_lt_of_natDegree_le_natDegree`); the summed, `Function.update` form no (and should not).
- Too specific (inline?)? It is specific to the induction, but naming it keeps `wronskian_ne_zero_of_linearIndependent` short; inlining is possible but not an improvement.
- Well-chosen? Reasonable; hypotheses are stronger than needed (see Notes).
- Conclusion: `KEEP` — action: keep as a local lemma; optionally weaken to `(hp : φ ν ≠ 0) (hne : φ ν' - C a * φ ν ≠ 0)` over any `Fintype` index.

## Mathlibable assessment (Step 9)

Pre-filter: public; name not `_aux`; docstring not internal/auxiliary; Step 8 = KEEP; `sum_natDegree_update_lt` does not occur in `.lake/packages/mathlib/Mathlib/` (grep). Not a glue lemma. Full workflow run.

### Baseline (Phase 0)
- lake build:               ✓ clean (project built per brief; evidence file importing `Roth.Wronskian` elaborates with no errors)
- decl `Roth.sum_natDegree_update_lt`: ✓ resolved at Roth/Wronskian.lean:182
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  n-ary (Hasse-derivative) Wronskian of polynomials and the criterion "Wronskian ≠ 0 iff linearly independent" in characteristic zero (§2 of the Roth source).

### Statement (Phase 1)

`Roth.sum_natDegree_update_lt` is a theorem stating the following:

Let φ_0, …, φ_{l-1} be linearly independent polynomials over a field K, and suppose deg φ_ν = deg φ_ν' for some ν ≠ ν'. Replace φ_ν' by φ_ν' − (lc φ_ν' / lc φ_ν)·φ_ν. Then the total degree Σ_ρ deg φ_ρ strictly decreases.

Variables / typeclasses involved (Lean side):
- `K` field (scalars); `l` family size; `φ : Fin l → K[X]` the family; `ν ν'` indices.

Hypotheses (Lean side):
- `hφ` linear independence (used only to get nonzeroness of φ ν and of the updated member); `h : ν ≠ ν'`; `hdeg` equal natDegrees.

Conclusion (math): one leading-term elimination lowers Σ deg.

Conclusion (Lean): `∑ ρ, (Function.update φ ν' (φ ν' - C (lc φ ν' / lc φ ν) * φ ν) ρ).natDegree < ∑ ρ, (φ ρ).natDegree`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: helper lemma providing the decreasing measure for one induction; not a main result, not a structure, not named.

### One-line check (Phase 2b)

Body line count: 19 substantive lines
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Wronskian linearly independent polynomials basis distinct degrees Gaussian elimination leading coefficients | yes | reduce to distinct degrees by subtracting multiples of same-degree members (Wronskian unchanged) | arXiv 0707.0434, 2602.20832, Bostan–Dumas 1301.6598 (Lemma: change of basis to distinct orders) |
| 2 | WebSearch (general form) | finite-dimensional space of polynomials has a basis with pairwise distinct degrees lemma | partial | distinct-degree nonzero polynomials are independent; echelon basis of a span | textbook level (LibreTexts Nicholson 6.5); the degree-drop step is never stated as a lemma |
| 3 | WebSearch (aliases) | "leading term" cancellation "degree drops" polynomial subtract multiple same degree echelon basis | yes | "cancel leading terms" lowers degree | led to mathlib's `Polynomial.cancelLeads` docs |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for "eliminat" | yes | "Such a basis is obtained by eliminating equal leading degrees" (clean.tex:177) | the lemma formalises exactly one elimination step plus the termination measure |
| 6 | nLab | ncatlab Wronskian / leading coefficient polynomial degree | no | — | no nLab page; elementary polynomial algebra, not covered |
| 7 | nCatLab | — | n/a | — | not a categorical concept (checked together with #6) |
| 8 | Stacks Project | — | n/a | — | not an algebraic-geometry concept; elementary degree bookkeeping |
| 9 | MathOverflow / MSE | mathoverflow Wronskian polynomials linearly independent iff nonzero proof distinct degrees reduction | partial | same reduction-to-distinct-degrees argument; no MO thread isolating the degree-drop step | Bostan–Dumas cited as the standard proof |
| 10 | recent arXiv | covered by #1/#9 (2410.18867, 2602.20832) | yes | the reduction is stated in prose as a routine step | never isolated as a lemma |

### Literature summary (Phase 3)

Concept identified as: leading-term cancellation (one step of Gaussian elimination by degree / "cancel leads"), used as the termination measure for reducing a family of polynomials to distinct degrees.
Sources agree on the standard form: yes — "if deg p = deg q then deg(q − (lc q/lc p) p) < deg q (or the difference is 0)"; in division-free form, deg(lc p·q − lc q·p) < deg q.
Most general standard form: over any ring, for p, q of equal degree with equal (or cross-multiplied) leading coefficients, the difference has strictly smaller degree.
Generality dimensions where the literature varies:
  - scalars: field (divide) vs commutative ring (cross-multiply, `cancelLeads`).
  - summed form: never stated; the literature states only the pointwise step and says "repeat".
Disagreement with the literature: none; the summed `Function.update` measure is a formalisation artefact.

### Generality analysis — `Roth.sum_natDegree_update_lt`

Literature-standard form (from Phase 3): pointwise degree drop under leading-term cancellation (mathlib: `degree_sub_lt_left`, `cancelLeads`).

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason |
|---|------|------|------|------|------|
| 1 | `[Field K]` | field | division ring / comm ring (cancelLeads) | yes | verified over `[DivisionRing K]` (evidence (A),(B)) |
| 2 | `Fin l` index | Fin l | any finite index | yes | verified over `[Fintype ι] [DecidableEq ι]` (evidence (B)) |
| 3 | `hφ : LinearIndependent K φ` | lin. indep. | `φ ν ≠ 0` and updated member ≠ 0 | yes | verified: only these two facts are used (evidence (B)) |
| 4 | `h : ν ≠ ν'` | distinct indices | not needed | yes | follows from `hne` (if ν = ν' the difference is 0); dropped in evidence (B) |
| 5 | `hdeg` | equal natDegree | equal degree | NO | essential for the cancellation |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD (as a local lemma)
Number of weakening opportunities found: 4 (all verified clean in the evidence file)
Proposed restatement (local only — see verdict):

```lean
theorem sum_natDegree_update_lt' {K ι : Type*} [DivisionRing K] [Fintype ι] [DecidableEq ι]
    {φ : ι → K[X]} {ν ν' : ι} (hp : φ ν ≠ 0)
    (hne : φ ν' - C ((φ ν').leadingCoeff / (φ ν).leadingCoeff) * φ ν ≠ 0)
    (hdeg : (φ ν).natDegree = (φ ν').natDegree) :
    ∑ ρ, (Function.update φ ν' (φ ν' - C ((φ ν').leadingCoeff / (φ ν).leadingCoeff) * φ ν) ρ).natDegree
      < ∑ ρ, (φ ρ).natDegree
```

Cost of restatement: CHEAP — mechanical; the original is a 2-line corollary (evidence (C)). The weakening does not change the mathlib verdict: even weakened, the content is mathlib's `degree_sub_lt_left` summed.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Downstream |
|---|---|---|---|---|
| 1 | typeclasses instead of bundled hypotheses | no | — | no structure preamble |
| 2 | filters instead of sequences | no | finite combinatorial/degree statement | — |
| 3 | universal property | no | no construction | — |
| 4 | bundled substructure | partly | the natural invariant statement is about the span (degree filtration quotients of a submodule have dim ≤ 1), not a family | would be a different, larger lemma ("a finite-dim subspace of K[X] has a basis of distinct degrees"); not this declaration |
| 5 | field → ring/module | yes | division-free `cancelLeads` over `[CommRing R]` already in mathlib | mathlib already has it |
| 6 | higher-categorical | no | — | — |
| 7 | concrete index → general | yes | `Fin l` → `Fintype ι` | verified; local benefit only |
| 8 | concrete-via-abstract | no | statement mentions no concrete named object; proof uses the abstract degree-drop fact directly | — |
| 9 | false-generalisation guard | no false generalisation | the weakened statement is the same measure inequality | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
- One-line reason: the idiomatic mathlib form of the content already exists (`degree_sub_lt_left`, `cancelLeads` lemmas); the only "new" part is a summed measure that mathlib would not want as API.

### Proof strategy — `Roth.sum_natDegree_update_lt`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ topology | no | — | — |
| 2 | element-wise algebra vs ideals | no | — | — |
| 3 | sequences vs filters | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | marginal | a `natDegree` form of `degree_sub_lt_left` (`natDegree_sub_lt_left` with `p - q ≠ 0`) would shorten the pointwise step by one call | CHEAP; too small for its own PR, `natDegree_lt_natDegree` bridges it |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (pointwise mathlib lemma + `Finset.sum_lt_sum`). Taking `hne`/`hp` as hypotheses would remove the dependence on `linearIndependent_update_sub_smul` (move that to the call site).

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.sum_natDegree_update_lt`

[A] Lean-Finder  "natDegree (q - C (leadingCoeff q / leadingCoeff p) * p) < natDegree q when natDegree p = natDegree q"  hits: `Polynomial.natDegree_cancelLeads_lt_of_natDegree_le_natDegree`, `..._of_comm`, `Polynomial.degree_sub_lt`, `Polynomial.div_wf_lemma`
[B] Loogle       `Polynomial.natDegree (_ - _) < Polynomial.natDegree _`  no hits (no natDegree-form of the sub lemma)
[C] LeanSearch   "subtracting a scalar multiple of p cancelling the leading coefficient of q lowers the degree of q when deg p = deg q"  hits: same `cancelLeads` lemmas, `degree_sub_lt`, `degree_eraseLead_lt`
[D] Grep mathlib `theorem degree_sub_lt`, `natDegree_sub_lt`, `sum_natDegree`, `div_wf_lemma`, `cancelLeads`  hits: `Polynomial.degree_sub_lt_left`/`_right` (Mathlib/Algebra/Polynomial/Degree/Defs.lean:543/562; `degree_sub_lt` deprecated alias), `Polynomial.cancelLeads` (Mathlib/Algebra/Polynomial/CancelLeads.lean:41,81), `div_wf_lemma` (Div.lean:106); no `sum_natDegree*` or summed form
[E] Name pattern `sum_natDegree_update_lt`, `natDegree_sub_lt`  no hits

Searched for both the user's form (summed, updated family) and the literature-standard form (pointwise cancellation).

Concluded: found building blocks (`Polynomial.degree_sub_lt_left`, `Polynomial.natDegree_lt_natDegree`, `Polynomial.cancelLeads` + `natDegree_cancelLeads_lt_of_natDegree_le_natDegree`, `Finset.sum_lt_sum`); composition yields our form. Evidence (D) verifies `q - C (lc q / lc p) * p = C (lc p)⁻¹ * p.cancelLeads q` when degrees agree.

### Normal-form check — `Roth.sum_natDegree_update_lt`

Equivalent formalisms: divided form `q - C (lc q / lc p) * p`; division-free `p.cancelLeads q`; `degree` vs `natDegree`.
Does mathlib already have a canonical form? yes: `cancelLeads` (division-free) and `degree_sub_lt_left` (equal leading coefficients).
Our statement is a summed consequence, not an equivalence; the pointwise part is not stated against `cancelLeads` but is equivalent up to a unit (evidence (D)).
RHS convention respected? n/a (inequality).

### Syntactic generality — `Roth.sum_natDegree_update_lt`

Alternative restatements attempted:
- weakened hypotheses `hp`, `hne` over `Fintype ι`, `[DivisionRing K]` (evidence (B), compiles);
- pointwise lemma alone (evidence (A), compiles).

Chosen restatement: (B) for local use — the call site already has `hφ`, so it supplies `hφ.ne_zero ν` and the `linearIndependent_update_sub_smul` fact (evidence (C) shows the call-site cost is one term).
Justification: decouples the measure lemma from linear independence; easier to reuse.

### Superfluous-argument audit — `Roth.sum_natDegree_update_lt`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Field K]` | no (DivisionRing suffices) | verified |
| 2 | `hφ` | no | only nonzeroness consequences used |
| 3 | `h : ν ≠ ν'` | no | implied by `hne` |
| 4 | `hdeg` | yes | essential |
| 5 | `Fin l` | no | any `Fintype` |

### Statement-shape verdict (Phase 5.5)

Normal form: OK (inequality; pointwise content is mathlib's canonical lemma)
Syntactic generality: RESTATE (locally, to the hypotheses of evidence (B))
Superfluous arguments: 4 to drop (`[Field K]`→`[DivisionRing K]`, `hφ`, `h`, `Fin l`→`Fintype ι`)

Overall: RESTATE-BEFORE-SHIP (local cleanup only; not shipping to mathlib)

### Call sites — `Roth.sum_natDegree_update_lt`

Internal use count: 1 (in the declaring file; 0 outside it)
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Wronskian.lean:213 | `exact ih _ (hN ▸ sum_natDegree_update_lt h hne hdeg)` in `wronskian_ne_zero_of_linearIndependent` |

Inline-derivation grep: (none) — `grep -rn "degree_sub_lt\|sum_lt_sum" Roth/` shows the composition only inside this lemma.

K = 1 internal use: leans toward NO-composable (single-use helper).

### Composition check (Phase 6)

Can `Roth.sum_natDegree_update_lt` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Finset.sum_lt_sum (fun i _ ↦ …) ⟨ν', mem_univ _, natDegree_lt_natDegree hne (degree_sub_lt_left hd hq hlc)⟩`
  - Mathlib decls used: `Finset.sum_lt_sum`, `Polynomial.natDegree_lt_natDegree`, `Polynomial.degree_sub_lt_left` (+ `degree_C_mul`, `leadingCoeff_mul`, `leadingCoeff_C`, `div_mul_cancel₀` for the side conditions, `Function.update_of_ne` for the other indices)
  - Result: succeeds (evidence (A)+(B))
  - Notes: the three main calls carry all the content; the side conditions are routine leading-coefficient bookkeeping.

Attempt 2: via `cancelLeads`: rewrite the update with evidence (D) and use `natDegree_cancelLeads_lt_of_natDegree_le_natDegree` (needs `0 < natDegree`, otherwise `hne` fails) — also works but adds the unit rewrite.

Conclusion: COMPOSABLE (three core mathlib calls; side goals are bookkeeping, recorded as "trivial simp-level composition")

## Verdict: `Roth.sum_natDegree_update_lt`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): the literature states only the pointwise step ("eliminate equal leading degrees", clean.tex:177; Bostan–Dumas) and never the summed measure.
- Generality analysis (Phase 4): STRICTLY NARROWER as a local lemma (4 verified weakenings), but the weakened form is still just the mathlib pointwise lemma summed.
- Mathlib search (Phase 5): building blocks `Polynomial.degree_sub_lt_left`, `Polynomial.cancelLeads` + `natDegree_cancelLeads_lt_of_natDegree_le_natDegree`, `Finset.sum_lt_sum`.
- Composition check (Phase 6): COMPOSABLE.

**Rationale:**

The mathematical content is "cancelling the leading term of one of two equal-degree polynomials lowers its degree". Mathlib already has this in two canonical forms: `Polynomial.degree_sub_lt_left` (equal leading coefficients) and the division-free `Polynomial.cancelLeads` with `natDegree_cancelLeads_lt_of_natDegree_le_natDegree` over any commutative ring. The project lemma adds only the summation over a `Function.update`d family, the termination measure of one specific induction. Mathlib would not want that as API: it is never stated in the literature, it fixes one choice of measure, and `Finset.sum_lt_sum` produces it from the pointwise lemma in a few lines. The weakenings found (`[DivisionRing K]`, any `Fintype` index, `hφ` and `h` replaced by `φ ν ≠ 0` and nonvanishing of the updated member) all compile, but they help only local reuse.

If this direction is ever upstreamed, it goes in with the n-ary Wronskian criterion (`wronskian_ne_zero_of_linearIndependent`, see the sibling reports). There the natural statement is "a finite-dimensional subspace of K[X] has a basis with distinct degrees" (Bostan–Dumas style). That is a different and larger lemma for which this measure is only proof-internal.

WHY not: mathlib has the building blocks. Pointwise drop: `Polynomial.degree_sub_lt_left` (Mathlib/Algebra/Polynomial/Degree/Defs.lean:543) via `Polynomial.natDegree_lt_natDegree`. Division-free alternative: `Polynomial.natDegree_cancelLeads_lt_of_natDegree_le_natDegree` (Mathlib/Algebra/Polynomial/CancelLeads.lean:81). Summation: `Finset.sum_lt_sum`.
Belongs-elsewhere check: keep it project-local in Roth/Wronskian.lean as a named step of the induction. It is not a mathlib lemma, but naming it keeps `wronskian_ne_zero_of_linearIndependent` readable.
Mathlib building blocks: `Polynomial.degree_sub_lt_left`, `Polynomial.natDegree_lt_natDegree`, `Finset.sum_lt_sum`, `Function.update_of_ne` (alternatively `Polynomial.cancelLeads`, `Polynomial.natDegree_cancelLeads_lt_of_natDegree_le_natDegree`).
Composition sketch (≤3 lines):
```lean
example : <our statement> :=
  Finset.sum_lt_sum (fun i _ ↦ by by_cases hi : i = ν' <;> simp [hi, hlt.le, Function.update_of_ne])
    ⟨ν', Finset.mem_univ _, by simpa using
      natDegree_lt_natDegree hne (degree_sub_lt_left hd (h0 ν') hlc)⟩
```
Call sites in our project (from Phase 6.0): 1
Refactor plan: at the single call site Roth/Wronskian.lean:213 either (a) keep the call and restate the lemma locally with the verified weaker hypotheses: `sum_natDegree_update_lt' (h.ne_zero ν) (by simpa using (linearIndependent_update_sub_smul hne _ h).ne_zero ν') hdeg` (evidence (C)); or (b) inline the composition above. Recommended: (a), because it decouples the measure from linear independence. Inlining would lengthen the induction proof for no gain.
Next action: do not upstream. Locally keep (or weaken per (a)) the lemma for its one call site at Roth/Wronskian.lean:213.

## Next step

Do not upstream. Keep the lemma locally for Roth/Wronskian.lean:213, optionally restated with the verified weaker hypotheses (`[DivisionRing K]`, `Fintype ι`, `hp : φ ν ≠ 0`, `hne`). Inlining the `degree_sub_lt_left` + `Finset.sum_lt_sum` composition at that site is the alternative.

## Evidence
- Evidence file: `.mathlib-quality/overview/evidence/Roth.sum_natDegree_update_lt/experiments.lean` (imports `Roth.Wronskian`, `Mathlib.Algebra.Polynomial.CancelLeads`). Checked with `lean_diagnostic_messages`: no errors, no warnings. Contents: (A) pointwise `natDegree_sub_C_div_mul_lt` over `[DivisionRing K]` from `degree_sub_lt_left`; (B) weakened sum lemma (`Fintype ι`, `DivisionRing`, `hp`, `hne`, no `hφ`, no `ν ≠ ν'`); (C) the original project statement recovered from (B); (D) `q - C (lc q / lc p) * p = C (lc p)⁻¹ * p.cancelLeads q` when degrees agree. The first attempt at (B) used `Finset.sum_update_of_mem` and failed (the summand is composed with `natDegree`), and (D) needed the `CancelLeads` import. Both were fixed and the final file is clean.
- Searches: Loogle (natDegree sub pattern: no hits), LeanSearch, Lean-Finder (cancelLeads, degree_sub_lt), grep of mathlib (degree_sub_lt_left/right, cancelLeads, div_wf_lemma; no `sum_natDegree*`), lean name search. Six WebSearch queries (Wronskian reduction, distinct-degree basis, leading-term cancellation, MathOverflow, nLab). ChatGPT MCP n/a (not configured in this session).
