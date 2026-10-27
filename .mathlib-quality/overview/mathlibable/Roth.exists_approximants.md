---
decl: Roth.exists_approximants
file: Roth/Main.lean
line: 256
kind: theorem
visibility: public
verdict: BORDERLINE-needs-human
cost: n/a
junk: KEEP
rationale: Eq. (50) selection step of Roth's proof (m reduced approximants in approxSet with log q_1 > L and log q_(j+1) > (2/delta) log q_j), stated over the project-local approxSet (NO-composable) and consumed once; its generic core (dependent choice of a sequence with prescribed growth from an unbounded function) is already essentially mathlib's exists_seq_of_forall_finset_exists (compiled), and the remaining content is log/ceil arithmetic, so there is nothing natural to upstream; recommended resolution keep project-local.
action: Keep in Roth/Main.lean (single caller private Roth.exists_roth_parameters_aux at Roth/Main.lean:438); do not upstream; optionally note in the docstring that delta needs no hypothesis (compiled with delta = -1 in evidence/Roth.exists_approximants/generic_selection.lean).
---

# Roth.exists_approximants

## Inventory entry

### `theorem Roth.exists_approximants`
- **Type**: `{α : ℝ} (hα : Irrational α) {κ : ℝ} (hκ : 0 < κ) (hinf : (approxSet α κ).Infinite) (m : ℕ) [NeZero m] {δ : ℝ} (L : ℝ) : ∃ (h : Fin m → ℤ) (q : Fin m → ℕ), (∀ j, (h j, q j) ∈ approxSet α κ) ∧ (∀ j, IsCoprime (h j) (q j : ℤ)) ∧ (∀ j, 1 < q j) ∧ L < Real.log (q 0) ∧ ∀ i j : Fin m, i.val + 1 = j.val → 2 / δ * Real.log (q i) < Real.log (q j)`
- **What**: For irrational α with infinitely many approximations of quality κ > 0, one can choose m reduced approximations h_j/q_j (j = 0, ..., m-1) of quality κ with q_j > 1, log q_0 > L, and log q_(j+1) > (2/δ) log q_j (paper eq. (32) for q_1 and eq. (50)).
- **How**: `choose g ... using fun Q₀ ↦ exists_reduced_approx hα hκ hinf Q₀` gives a reduced approximant with denominator above any bound; a sequence `s : ℕ → ℤ × ℕ` is built by `Nat.rec`, starting at `g (max ⌈exp L⌉₊ 1)` and stepping with `g (max ⌈q^(2/δ)⌉₊ 1)`. Membership/coprimality/`1 < q` come from `hgmem`, `hgcop`, `le_max_right`; `L < log q_0` from `Nat.le_ceil` and `Real.lt_log_iff_exp_lt`; the growth bound from `Real.lt_log_of_rpow_lt` and `Nat.le_ceil`.
- **Hypotheses**: `hα` irrational and `hκ : 0 < κ` (passed to `exists_reduced_approx`, needed there); `hinf` infinite approximation set; `m` with `[NeZero m]` (so `q 0` makes sense); `δ` and `L` arbitrary reals (no hypothesis on δ is needed; for δ ≤ 0 the growth condition is automatic).
- **Uses from project**: `Roth.approxSet`, `Roth.exists_reduced_approx`
- **Used by**: Roth/Main.lean:438 `Roth.exists_roth_parameters_aux` (private); also named in the module docstring (Main.lean:32). `grep -rn exists_approximants Roth/ Roth.lean`: no other hits.
- **Visibility**: public
- **Lines**: 256–277, proof length 18 lines
- **Notes**: Source: clean.tex §7 l.1608–1613 (eq. (50)) and the `\lean` note l.1639 ("Start from unbounded reduced denominators and choose the finite sequence of approximants satisfying (50)").

## Junk check (Step 8)
- Used anywhere? Yes, once: `exists_roth_parameters_aux` (Main.lean:438), which immediately feeds the result into `exists_degrees`.
- Wrapper of 1–2 mathlib calls? No: `exists_reduced_approx` (project) plus a `Nat.rec` selection plus ceil/exp/log arithmetic (18 lines).
- Does mathlib have it? No. The generic selection principle exists (`exists_seq_of_forall_finset_exists`, `Filter.extraction_forall_of_frequently`, `Nat.exists_strictMono_subsequence`), but nothing about Diophantine approximants.
- Too specific (inline?)? Single caller, but it corresponds to a self-contained step of the paper (eq. (50)) and inlining 18 lines into the already long private parameter lemma would hurt readability.
- Well-chosen? Yes; shape matches exactly what `exists_degrees` consumes (only `.le` of the growth bound is used there).

Conclusion: KEEP. No action.

## Mathlibable assessment (Step 9)

Pre-filter: public; name does not end in `_aux`; docstring not internal/auxiliary; Step 8 KEEP; mathlib has no `Roth` namespace and `grep -rn exists_approximants .lake/packages/mathlib/Mathlib/` returns nothing. Not a glue lemma (18-line proof; parent `approxSet` is NO-composable, so inheritance would not apply anyway). Full run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Main` elaborates with no diagnostics)
- decl `Roth.exists_approximants`: resolved at Roth/Main.lean:256
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Roth's theorem for irrational real algebraic numbers, via reduction to algebraic integers, parameter choice, approximants, the main lemma and a final contradiction.

### Statement (Phase 1)

`Roth.exists_approximants` is a theorem stating the following:

Let α be irrational and κ > 0, and suppose |α − h/q| < q^(−κ) has infinitely many solutions (h, q) ∈ ℤ × ℕ, q > 0. Then for every m ≥ 1, every δ and every L there are reduced solutions h_1/q_1, ..., h_m/q_m (gcd(h_j, q_j) = 1, q_j > 1) such that log q_1 > L and log q_(j+1) > (2/δ) log q_j for all j < m.

Variables / typeclasses involved (Lean side):
- `α : ℝ`: the number approximated; `κ : ℝ`: the exponent.
- `m : ℕ` with `[NeZero m]`: number of approximants (indices `Fin m`).
- `δ : ℝ`: growth parameter; `L : ℝ`: lower bound for log q_1 (eq. (32)).

Hypotheses (Lean side):
- `hα : Irrational α`, `hκ : 0 < κ`, `hinf : (approxSet α κ).Infinite`: give reduced solutions with arbitrarily large denominators (via `exists_reduced_approx`).

Conclusion (math): a finite lacunary (log-growth 2/δ) sequence of reduced approximants starting above e^L.

Conclusion (Lean): `∃ (h : Fin m → ℤ) (q : Fin m → ℕ), (∀ j, (h j, q j) ∈ approxSet α κ) ∧ (∀ j, IsCoprime (h j) (q j : ℤ)) ∧ (∀ j, 1 < q j) ∧ L < Real.log (q 0) ∧ ∀ i j : Fin m, i.val + 1 = j.val → 2 / δ * Real.log (q i) < Real.log (q j)`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a technical selection step of §7 of Roth's proof, used once; not a main result.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

n/a: kind is theorem. MULTI-LINE (18-line proof); check skipped.

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth theorem proof choose approximations h_j/q_j log q_(j+1) > (2/δ) log q_j rapidly increasing denominators | partial | Roth-type arguments need q_(j+1) large relative to q_j; the selection is a one-line step in every proof | Wikipedia "Roth's theorem", Lean eval problem page "Thue–Siegel–Roth", arXiv 1010.3475, 1007.2050 (denominator-growth bounds of Davenport–Roth type, the opposite direction); no source isolates the selection as a lemma |
| 2 | WebSearch (general form) | infinitely many solutions unbounded denominators choose subsequence q_(j+1) q_j growth condition Diophantine approximation lemma | partial | general principle: from unbounded denominators extract a subsequence with any prescribed growth (dependent choice) | arXiv 2109.09040 (unbounded denominators, unrelated sense), Kim PAMS 2009 (increasing denominators of good approximations); folklore |
| 3 | WebSearch (named / aliases) | Thue-Siegel-Roth proof "sufficiently rapidly increasing" approximants selection step Schmidt Diophantine Approximation | partial | Thue/Siegel/Roth all choose the next approximant depending on the previous ones ("q_(j+1) sufficiently large compared with q_j") | Encyclopedia of Math "Thue–Siegel–Roth theorem", "Thue method"; arXiv 0908.4024 (Waldschmidt, auxiliary functions); textbooks (Schmidt LNM 785, Bombieri–Gubler) state it in passing |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for "approximants", "(50)", "reduced solution" | yes | l.1608–1613: pick a reduced h_1/q_1 with q_1 satisfying (32), then h_2/q_2, ..., h_m/q_m reduced with log q_j / log q_(j-1) > 2/δ; l.1639 `\lean` note: "Start from unbounded reduced denominators and choose the finite sequence of approximants satisfying (50)" | matches the Lean statement and proof exactly |
| 6 | nLab | "Diophantine approximation", "Roth's theorem" | no | no page with this step | nLab has no proof-level Diophantine approximation content |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | n/a | n/a | n/a | not an algebraic-geometry concept |
| 9 | MathOverflow / Math.SE | (results of #2, #3) choosing rapidly growing subsequence of approximations | yes (folklore) | "pick each next approximation with denominator large enough"; treated as obvious | exercise level |
| 10 | recent arXiv | (results of #1, #2) Roth proof approximant selection | partial | arXiv 2111.12409 (generalisations of Roth), 0908.4024: selection step stated informally | no lemma-level statement |

### Literature summary (Phase 3)

Concept identified as: the "choice of approximants" step in Thue–Siegel–Roth proofs; generically, dependent choice of a sequence with prescribed growth from a set on which a size function is unbounded.
Sources agree on the standard form: yes (always informal, "choose q_(j+1) sufficiently large compared to q_j").
Most general standard form: if f is unbounded on S then for any g there is a sequence s in S with f(s_(k+1)) > g(f(s_k)) (and f(s_0) > B).
Generality dimensions where the literature varies:
  - growth law: log q_(j+1) > c log q_j (Roth), q_(j+1) > q_j^c, or "sufficiently large"; any monotone g works.
  - indexing: finite m (Roth) vs infinite sequence.
Disagreement with the literature: none; the Lean form is the paper's eq. (50) verbatim.

### Generality analysis — `Roth.exists_approximants`

Literature-standard form: generic dependent choice "f unbounded on S ⇒ sequence in S with f(s_(k+1)) > g(f(s_k))", specialised here to reduced approximants and g(q) = ⌈q^(2/δ)⌉.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason |
|---|---|---|---|---|---|
| 1 | `hα : Irrational α` | irrational | irrational | NO | required by `exists_reduced_approx` (rational α with κ > 1 has no large reduced solutions) |
| 2 | `hκ : 0 < κ` | positive | κ > 0 | not mechanically | required by `exists_reduced_approx`'s proof; caller has κ > 2 |
| 3 | `hinf` | infinite set | infinite set | NO | without it no large reduced solutions |
| 4 | `δ` | arbitrary real, no hypothesis | δ > 0 in the paper | already weaker | compiled: the theorem applies with δ = −1 (evidence `example`) |
| 5 | `[NeZero m]` | m ≥ 1 | m ≥ 1 | NO | the statement mentions `q 0` |
| 6 | approxSet / log specifics | Roth-specific | generic `exists_seq_growth` | n/a (class 5: different statement) | generic core compiled as `exists_seq_growth` / `exists_seq_growth'` |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL for the project statement (no hypothesis droppable; δ is already unconstrained).
Number of weakening opportunities found: 0 mechanical. The generic content is a different lemma (compiled, `exists_seq_growth` in the evidence file); it is not a weakening but a separate statement, and mathlib's `exists_seq_of_forall_finset_exists` already gives it in a 5-line composition (`exists_seq_growth'`, compiled).
Cost of restatement: n/a.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | hypotheses are propositions about one real number | — |
| 2 | sequences to filters? | partial | "∀ Q₀ ∃ q > Q₀" is `∃ᶠ` / `Tendsto ... atTop`; mathlib's `Filter.extraction_forall_of_frequently` handles fixed-index predicates but not growth relative to the previous term | none gained for a single caller |
| 3 | construction vs universal property? | no | — | — |
| 4 | bundled substructure? | no | — | — |
| 5 | field-specific to weaker typeclasses? | no | real logarithms intended | — |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes (mild) | `Fin m` could be `ℕ` (infinite sequence) and the growth relation an arbitrary g; compiled as `exists_seq_growth` | `exists_seq_of_forall_finset_exists` already covers it |
| 8 | concrete-via-abstract? | yes | after `exists_reduced_approx`, the proof never uses approximation properties: it is generic dependent choice plus ceil/log arithmetic | the abstract part is mathlib's `exists_seq_of_forall_finset_exists` |
| 9 | false-generalisation guard | no false generalisation | `exists_seq_growth` specialised to S = reduced approximants, f = denominator, g = ⌈·^(2/δ)⌉ gives back the statement | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no (as an upstreaming target).
  - One-line reason: the abstract content (Q7/Q8) is already in mathlib as `exists_seq_of_forall_finset_exists` (compiled specialisation `exists_seq_growth'`), so the abstraction yields nothing new to add; what remains is Roth-specific.

### Proof strategy — `Roth.exists_approximants`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | partial | could use `exists_seq_of_forall_finset_exists` instead of `Nat.rec`; the `Nat.rec` is 2 lines and needs only consecutive terms, so no gain | CHEAP, no gain |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | the arithmetic uses `Real.lt_log_iff_exp_lt`, `Real.lt_log_of_rpow_lt`, `Nat.le_ceil`, all in mathlib | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (`choose` + `Nat.rec` dependent choice is the standard pattern; the arithmetic uses existing mathlib lemmas).
  - Would refactoring make the proof strictly shorter / cleaner? no.

### Diamond / defeq risk

n/a: declaration kind is theorem.

### Mathlib search-status: `Roth.exists_approximants`

[A] Lean-Finder       "if for every bound there is an element of a set with f x larger than the bound, then there is a sequence in the set with f (s (n+1)) > g (f (s n))"   hits: `Nat.exists_strictMono_subsequence`, `Filter.extraction_forall_of_frequently`, `Filter.strictMono_subseq_of_tendsto_atTop`, `Filter.extraction_forall_of_eventually'`, `Filter.high_scores`; none relates consecutive terms by an arbitrary growth law
[B] Loogle            `Filter.extraction_forall_of_frequently` (signature check)   hit: `(∀ n, ∃ᶠ k in atTop, P n k) → ∃ φ, StrictMono φ ∧ ∀ n, P n (φ n)`; fixed-index predicate only
[C] LeanSearch        "frequently atTop gives a strictly monotone extraction satisfying a property at every index"   hits: `Filter.extraction_forall_of_frequently`, `Filter.extraction_forall_of_eventually'`, `Filter.extraction_of_frequently_atTop`, `Filter.tendsto_atTop_of_monotone_of_filter`
[D] Grep mathlib src  `exists_approximants`, `theorem exists_seq_of_forall`, `exists_seq_strictMono`   hits: no `exists_approximants`; `exists_seq_of_forall_finset_exists` (Mathlib/Data/Fintype/Basic.lean:259), `..._exists'` (:293), `exists_seq_strictMono_tendsto*` (Topology/Order/IsLUB.lean, unrelated)
[E] Name pattern      `exists_approximants`, `exists_reduced_approx` (grep in place of `lean_local_search`): only the project declarations

Searched for both:
  - the user's current form (Roth approximants with eq. (50) growth)
  - the literature-standard generic form (dependent choice with growth)

Concluded: found building blocks (`exists_seq_of_forall_finset_exists` for the generic selection; `Real.lt_log_iff_exp_lt`, `Real.lt_log_of_rpow_lt`, `Nat.le_ceil` for the arithmetic); the Roth-specific form is not in mathlib and depends on project `exists_reduced_approx`.

### Normal-form check — `Roth.exists_approximants`

Equivalent formalisms: (a) finite `Fin m` family with consecutive growth (current); (b) infinite `ℕ`-sequence with growth for all m < n (`exists_seq_of_forall_finset_exists` shape); (c) growth stated as q_(j+1) > q_j^(2/δ) instead of logarithms.
Does mathlib already have a canonical form for this idea? For the generic selection, yes: `exists_seq_of_forall_finset_exists`. For the Roth-specific statement, no.
RHS convention respected? n/a (not an iff).

### Syntactic generality — `Roth.exists_approximants`

Alternative restatements attempted:
- current `Fin m` form with logarithms
- generic `exists_seq_growth` (compiled) and its mathlib-derived variant `exists_seq_growth'` (compiled)
- (c) power form q_(j+1) > q_j^(2/δ) (not compiled; the caller `exists_degrees` consumes the log form)
Chosen restatement: the current one.
Justification: `exists_degrees` takes exactly `1 < q j` and the log growth on `Fin m`, so the caller applies it without conversion.

### Superfluous-argument audit — `Roth.exists_approximants`

| # | Argument | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hα` | yes | via `exists_reduced_approx`; necessary |
| 2 | `hκ` | yes | via `exists_reduced_approx` |
| 3 | `hinf` | yes | via `exists_reduced_approx` |
| 4 | `[NeZero m]` | yes | to name `q 0` |
| 5 | `δ`, `L` | yes (as parameters) | δ has no hypothesis (compiled with δ = −1) |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (project-local)

### Call sites — `Roth.exists_approximants`

Internal use count: 0 outside the declaring file; 1 in Main.lean
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Main.lean:438 (`exists_roth_parameters_aux`, private) | `obtain ⟨h, q, happ, hcop, hq1, hL, h50⟩ := exists_approximants hα hκ hinf m (...)` |

Inline-derivation grep: (none).

### Composition check (Phase 6)

Can `Roth.exists_approximants` be derived from mathlib in ≤3 chained calls?

Attempt 1: `exists_seq_of_forall_finset_exists` with S = reduced approximants, r x y := ⌈q_x^(2/δ)⌉ < q_y.
  - Mathlib decls used: `exists_seq_of_forall_finset_exists`, `Finset.le_sup`
  - Result: partial; the generic selection compiles (`exists_seq_growth'`), but the hypothesis needs the project lemma `exists_reduced_approx`, and the log/exp/ceil conversions (`Real.lt_log_iff_exp_lt`, `Real.lt_log_of_rpow_lt`, `Nat.le_ceil`) plus restriction to `Fin m` add several steps.
Attempt 2: `Filter.extraction_forall_of_frequently`.
  - Result: fails; the predicate cannot depend on the previously chosen term.

Conclusion: NOT-COMPOSABLE (needs project lemma `exists_reduced_approx` plus ~10 lines of arithmetic)

### Verdict: `Roth.exists_approximants`

**Category:** BORDERLINE-needs-human

**Evidence:**
- Literature search (Phase 3): the step is eq. (50) of the paper (clean.tex l.1608–1613, l.1639) and an informal "choose q_(j+1) large enough" in every Thue–Siegel–Roth proof; never an isolated lemma.
- Generality analysis (Phase 4): MAXIMALLY GENERAL as a project statement (δ already unconstrained); the generic core is a different statement already covered by mathlib.
- Mathlib search (Phase 5): building blocks only (`exists_seq_of_forall_finset_exists` and real log/ceil lemmas).
- Composition check (Phase 6): NOT-COMPOSABLE (project lemma plus arithmetic).

**Rationale:**

The theorem is the approximant-selection step of Roth's proof, phrased with the project-local `approxSet` (NO-composable-from-mathlib in its own report) and depending on the project lemma `exists_reduced_approx` (BORDERLINE). Once a reduced approximant above every bound is available, what remains is generic dependent choice, which mathlib already has as `exists_seq_of_forall_finset_exists` (Mathlib/Data/Fintype/Basic.lean:259); the compiled `exists_seq_growth'` shows the specialisation is a 5-line composition. The rest is arithmetic converting `q > ⌈e^L⌉` and `q_(j+1) > ⌈q_j^(2/δ)⌉` into logarithmic bounds with existing mathlib lemmas. So no new mathematical content is left to contribute: the statement cannot go upstream as is, and its abstraction is already in mathlib.

Strictly it is not NO-composable (the composition is longer than 3 calls and needs a project lemma), and NO-mathlib-has-it does not fit either, so the verdict is BORDERLINE with a recommended resolution: keep project-local. It would only matter upstream as part of a full Thue–Siegel–Roth upstreaming, which is a project-level decision.

Numbered questions:
1. Should this stay a project-local step of Roth's proof in Roth/Main.lean (recommended: yes)?
2. If Roth's theorem is ever upstreamed, should this step be folded into the (private) parameter lemma `exists_roth_parameters_aux` rather than kept as a public theorem? Default: keep public, it mirrors eq. (50).
3. Should the docstring note that no hypothesis on δ is needed (compiled with δ = −1)? Default: optional.

Belongs-elsewhere check: stays in Roth/Main.lean as the paper's eq. (50) selection.
Call sites in our project (from Phase 6.0): 1 (Main.lean:438). No change needed in any outcome.
Next action: user answers Q1–Q3; default is KEEP as is.

---

## Next step

Keep `Roth.exists_approximants` in Roth/Main.lean; do not upstream. No refactor needed at the single call site (Main.lean:438).

## Evidence
- `.mathlib-quality/overview/evidence/Roth.exists_approximants/generic_selection.lean` (imports `Roth.Main`): `exists_seq_growth` (generic dependent choice with growth, `Nat.rec` proof), `exists_seq_growth'` (same content derived from mathlib's `exists_seq_of_forall_finset_exists`), and an `example` applying `exists_approximants` with δ = −1, m = 3, L = 0 (δ needs no hypothesis). Checked with `lean_diagnostic_messages`: no diagnostics.
- Searches: 3 WebSearch queries, Lean-Finder, LeanSearch, Loogle, grep over mathlib (`exists_approximants`, `exists_seq_of_forall`, `exists_seq_strictMono`), project grep for call sites, grep of clean.tex (l.1608–1613, l.1639). ChatGPT MCP was unavailable in this session.
