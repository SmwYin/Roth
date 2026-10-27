---
decl: Roth.pow_rootMultiplicity_le
file: Roth/Theta.lean
line: 206
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Multiplicity form of the rational root theorem part 2 (den^mult divides the leading coefficient) packaged as a real bound; mathlib has only den_dvd_of_is_root (mult 1), and the compiled divisibility form over any normalized-GCD domain (q^mult divides leadingCoeff, IsRelPrime, q ne 0, no p ne 0) gives the Roth bound in 4 lines.
action: Upstream pow_rootMultiplicity_dvd_leadingCoeff (and its den/num UFD corollary) in the same PR as the parent pow_rootMultiplicity_dvd_of_isRelPrime to Mathlib/RingTheory/Polynomial/RationalRoot.lean or GaussLemma.lean; locally keep the real bound (sole caller Roth/Theta.lean:245 index_unique_le_log_div), re-proved as a corollary once upstreamed.
---

# Roth.pow_rootMultiplicity_le

## Inventory entry

### `theorem Roth.pow_rootMultiplicity_le`
- **Type**: `∀ {R : Polynomial ℤ}, R ≠ 0 → ∀ {h : ℤ} {q : ℕ}, 0 < q → IsCoprime h (q : ℤ) → ∀ {B : ℝ}, |(R.leadingCoeff : ℝ)| ≤ B → (q : ℝ) ^ rootMultiplicity ((h : ℚ) / q) (R.map (Int.castRingHom ℚ)) ≤ B`
- **What**: If `R ∈ ℤ[X]` is nonzero with `|lc(R)| ≤ B`, and `h/q` (coprime, `q > 0`) is a root of `R` of multiplicity `t` over ℚ, then `q^t ≤ B`.
- **How**: Obtains `R = (qX − h)^t Q` from `Roth.exists_eq_pow_mul_of_rootMultiplicity`; computes `lc R = q^t · lc Q` with `Polynomial.leadingCoeff_mul`, `Polynomial.leadingCoeff_pow`, `Polynomial.leadingCoeff_linear`; `1 ≤ |lc Q|` from `Int.one_le_abs` and `Polynomial.leadingCoeff_ne_zero` (Q ≠ 0 via `right_ne_zero_of_mul`); then casts to ℝ (`push_cast`, `abs_mul`, `abs_pow`, `Nat.abs_cast`) and closes with `le_mul_of_one_le_right`.
- **Hypotheses**: `hR : R ≠ 0` (needed: for `R = 0`, `t = 0` and `1 ≤ B` fails at `B = 0`); `hq : 0 < q` (only `q ≠ 0` used); `hcop : IsCoprime h q` (only relative primality used); `hB` the leading-coefficient bound.
- **Uses from project**: `Roth.exists_eq_pow_mul_of_rootMultiplicity` (Theta.lean:184).
- **Used by**: Roth/Theta.lean:245 (`index_unique_le_log_div`, private; the one-variable case of Lemma 5). `grep -rn pow_rootMultiplicity_le Roth/` gives only the definition and this use.
- **Visibility**: public
- **Lines**: 201–220 (docstring 201–205, statement 206–208, proof 209–220), proof length 12 lines
- **Notes**: Source: clean.tex l.686–690 (§5, proof of Lemma 5, "Comparing nonzero leading coefficients yields B ≥ |lc(R)| = q_1^t |lc(Q)| ≥ q_1^t"). The integer content is `q^t ∣ lc R`; the real-valued `B` bound is project packaging.

## Junk check (Step 8)
- **Used anywhere?** Yes, once (Theta.lean:245), on the Lemma 5 path.
- **Wrapper of 1–2 mathlib calls?** No: it uses the project Gauss-lemma step plus a 10-line leading-coefficient and casting argument.
- **Does mathlib have it?** No (Phase 5). Mathlib has `den_dvd_of_is_root` (multiplicity 1 only).
- **Too specific (inline?)?** Not worth inlining: it isolates the "compare leading coefficients" step the source names, keeping `index_unique_le_log_div` readable.
- **Well-chosen?** Yes locally; for mathlib the divisibility form `q ^ t ∣ R.leadingCoeff` is the right statement.
- **Conclusion:** `KEEP`.

## Mathlibable assessment (Step 9)

Pre-filter: public; name does not end in `_aux`; docstring not internal/auxiliary; Step 8 said KEEP; no `namespace Roth` in `.lake/packages/mathlib/Mathlib/`. Not a glue lemma (12-line proof), so no inheritance from the parent `Roth.exists_eq_pow_mul_of_rootMultiplicity` (YES-but-generalise-first). Full run follows.

### Baseline (Phase 0)
- lake build:               clean (project built per the brief; evidence file elaborates with no diagnostics)
- decl `Roth.pow_rootMultiplicity_le`: resolved at Roth/Theta.lean:206
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  `Θ_m(B; q; r)`, the supremum of indices of bounded integer polynomials at rational points, and Lemmas 5–7 bounding it

### Statement (Phase 1)

`Roth.pow_rootMultiplicity_le` is a theorem stating the following.

Let `R ∈ ℤ[X]` be nonzero with `|lc(R)| ≤ B` for a real `B`. Let `h ∈ ℤ`, `q ∈ ℕ`, `q > 0`, `gcd(h, q) = 1`, and let `t` be the multiplicity of `h/q` as a root of `R` in ℚ[X]. Then `q^t ≤ B`.

Variables / typeclasses involved (Lean side):
- `R : ℤ[X]`, `h : ℤ`, `q : ℕ`, `B : ℝ`.

Hypotheses (Lean side):
- `hR : R ≠ 0`; `hq : 0 < q`; `hcop : IsCoprime h q`; `hB : |(lc R : ℝ)| ≤ B`.

Conclusion (math): `q^{mult_{h/q}(R)} ≤ B` (equivalently, it follows from `q^{mult} ∣ lc(R)`).

Conclusion (Lean): `(q : ℝ) ^ rootMultiplicity ((h:ℚ)/q) (R.map (Int.castRingHom ℚ)) ≤ B`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a helper step (leading-coefficient comparison) inside the proof of Lemma 5.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 12 substantive lines
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE (check skipped, theorem).

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | rational root a/b multiplicity k then b^k divides leading coefficient integer polynomial | partial | rational root theorem (den ∣ lc), stated for UFDs in mathlib docs (Britannica, mathlib RationalRoot docs) | multiplicity version not stated explicitly; it is the iterate via Gauss's lemma |
| 2 | WebSearch (general form) | Gauss lemma GCD domain root of multiplicity m denominator power divides leading coefficient | partial | Gauss's lemma over UFD/GCD domains (CUHK, Toronto, Miami notes, Floris van Doorn's mathlib course docs) | general engine; `b^m ∣ lc` is the standard consequence via `(bX − a)^m ∣ f` |
| 3 | WebSearch (named-after / aliases) | Roth's lemma one variable index rational point bounded by log B / (r log q) leading coefficient | partial | one-variable case of Roth's lemma (arXiv 1806.10737, 2502.00731, Evertse notes) | step appears as bookkeeping in proofs of Roth's lemma; no standalone name |
| 4 | ChatGPT MCP | n/a | n/a | n/a | the `ask_chatgpt_math` MCP is not configured in this session (absent from the tool list) |
| 5 | Local references | clean.tex l.680–700 | yes | "Comparing nonzero leading coefficients yields B ≥ lc(R) = q_1^t lc(Q) ≥ q_1^t" | exactly the project statement; the Lean note says compare leading coefficients in ℤ first, then cast |
| 6 | nLab | rational root theorem / Gauss's lemma | no | nLab has Gauss's lemma abstractly, no rational root multiplicity corollary | general form only |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | n/a | n/a | n/a | elementary commutative algebra of polynomial divisibility; Stacks has no rational-root-theorem tag |
| 9 | MathOverflow / Math.SE | covered by searches 1–2 | no | n/a | textbook exercise level |
| 10 | recent arXiv (last 5 years) | search 3 surfaced arXiv 2502.00731 | partial | uses the step inside Roth's lemma | analogy only |

### Literature summary (Phase 3)

Concept identified as: rational root theorem with multiplicity (part 2): if `a/b` is a reduced root of multiplicity `t` of `f ∈ A[X]`, `A` a UFD/GCD domain, then `b^t ∣ lc(f)`.
Sources agree on the standard form: yes (the `t = 1` case is the classical theorem; the multiplicity case follows by Gauss's lemma and is used tacitly).
Most general standard form: `A` a GCD domain with fraction field `K`, `a, b ∈ A` relatively prime, `b ≠ 0`; `b^{mult_{a/b}(f)} ∣ lc(f)`, no `f ≠ 0` needed.
Generality dimensions where the literature varies:
  - base ring: ℤ to UFD / GCD domain; most general is GCD domain.
  - conclusion: divisibility (algebraic) vs absolute-value bound (Diophantine use); divisibility is the primary statement.
Disagreement with the literature: the Lean form is the ℤ case packaged as a real inequality via an auxiliary bound `B`, which is project-specific.

### Generality analysis — `Roth.pow_rootMultiplicity_le`

Literature-standard form: `q ^ mult ∣ lc p` over a normalized-GCD domain.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | base ring ℤ, field ℚ | `Polynomial ℤ`, `Int.castRingHom ℚ` | GCD domain `R`, `IsFractionRing R K` | yes | compiled (evidence (1)) via the parent's general lemma |
| 2 | conclusion `q^t ≤ B` in ℝ with `hB` | real bound | `q ^ t ∣ lc p` | yes | the real bound is a 4-line corollary (`Int.le_of_dvd`), evidence (3) |
| 3 | `hR : R ≠ 0` | nonzero | none | yes (for the divisibility form) | divisibility holds for `p = 0`; `hR` only needed for the inequality |
| 4 | `hq : 0 < q` | positive natural | `q ≠ 0` | yes | compiled |
| 5 | `hcop : IsCoprime` | Bézout | `IsRelPrime` | yes | compiled |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 5 (all verified clean in the evidence file)
Proposed restatement:

```lean
theorem Polynomial.pow_rootMultiplicity_dvd_leadingCoeff {R K : Type*} [CommRing R] [IsDomain R]
    [NormalizedGCDMonoid R] [Field K] [Algebra R K] [IsFractionRing R K] (p : R[X]) {h q : R}
    (hq : q ≠ 0) (hcop : IsRelPrime h q) :
    q ^ rootMultiplicity (algebraMap R K h / algebraMap R K q) (p.map (algebraMap R K)) ∣
      p.leadingCoeff
```

Cost of restatement: CHEAP (4-line proof from the parent's general lemma; project statement recovered in 6 lines).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | Typeclasses instead of preambles? | no | no preambles | — |
| 2 | Sequences vs filters? | no | algebraic statement | — |
| 3 | Construction vs universal property? | no | — | — |
| 4 | Bundled substructure? | no | — | — |
| 5 | Field-specific vs typeclass-weakened? | yes | ℤ to normalized-GCD domain (row 1) | sits next to `den_dvd_of_is_root` |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index generalised? | yes | `q : ℕ` to `q : R`; real bound to divisibility | removes ℝ casts |
| 8 | Concrete-via-abstract? | yes | proof uses only `lc` multiplicativity after the parent factorisation; UFD form `den A r ^ rootMultiplicity r (p.map _) ∣ p.leadingCoeff` (evidence (2)) | strengthens `den_dvd_of_is_root` |
| 9 | False-generalisation guard | no false generalisation | the divisibility form specialises back to the exact project statement (evidence (3)) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: the divisibility form above, plus the UFD `den` form.
  - Cost: CHEAP (both compiled).
  - Mathlib downstream this enables: a multiplicity version of `den_dvd_of_is_root` in `Mathlib/RingTheory/Polynomial/RationalRoot.lean`; any height/size bound `q^t ≤ |lc|` over ℤ via `Int.le_of_dvd`.
  - Real mathematical improvement: replaces a real-valued inequality with the algebraic fact behind it, valid over any GCD domain and for `p = 0`.

### Proof strategy — `Roth.pow_rootMultiplicity_le`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers? | yes | the divisibility lemma itself (and the parent factorisation lemma); then `Int.le_of_dvd` replaces the `1 ≤ abs (lc Q)` argument | CHEAP |

### Proof strategy verdict (Phase 4.6)

Current strategy: REFACTOR-RECOMMENDED
  - Proposed strategy: prove `q ^ t ∣ lc R` in ℤ, then `Int.le_of_dvd` and cast (evidence (3)).
  - Cost: CHEAP
  - Missing mathlib API: `pow_rootMultiplicity_dvd_leadingCoeff` (this proposal), `pow_rootMultiplicity_dvd_of_isRelPrime` (parent proposal).
  - Would refactoring make the proof strictly shorter / cleaner? yes (no `Q ≠ 0` / `1 ≤ abs` detour).

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.pow_rootMultiplicity_le`

[A] Lean-Finder       "if h/q in lowest terms is a root of multiplicity t of integer polynomial R then q^t divides the leading coefficient of R"   hits: `den_dvd_of_is_root`, `num_dvd_of_is_root`, `Polynomial.pow_rootMultiplicity_dvd`, `exists_integer_of_is_root_of_monic`, `Polynomial.IsRoot.dvd_coeff_zero` (multiplicity-1 or same-ring analogues only)
[B] Loogle            `_ ^ Polynomial.rootMultiplicity _ _ ∣ Polynomial.leadingCoeff _`   no hits
[C] LeanSearch        "denominator of rational root raised to root multiplicity divides leading coefficient"   hits: `den_dvd_of_is_root`, `num_dvd_of_is_root`, `pow_rootMultiplicity_dvd`, `exists_integer_of_is_root_of_monic`, `aroots_pow` (none with multiplicity)
[D] Grep mathlib src  `grep -rn rootMultiplicity Mathlib | grep -i "leadingCoeff\|den "`: no hits; files in `RingTheory/Polynomial/` mentioning `rootMultiplicity`: only HilbertPoly.lean, ScaleRoots.lean (unrelated); RationalRoot.lean (l.69–100) has only the multiplicity-1 `num_dvd_of_is_root` / `den_dvd_of_is_root`
[E] Name pattern      `pow_rootMultiplicity_dvd_leadingCoeff`, `den_pow_rootMultiplicity_dvd`: absent

Searched for both:
  - the user's form (ℤ, real bound): not in mathlib
  - the literature-standard form (GCD domain, divisibility; UFD den form): not in mathlib

Concluded: found building blocks (`den_dvd_of_is_root` for multiplicity 1, `leadingCoeff_mul`, `leadingCoeff_pow`, `leadingCoeff_linear`, `Int.le_of_dvd`); the multiplicity statement itself is not in mathlib and needs the parent's (also missing) Gauss-lemma factorisation.

### Normal-form check — `Roth.pow_rootMultiplicity_le`

Equivalent formalisms: `q^t ≤ B` given `|lc| ≤ B` (current); `(q:ℤ)^t ≤ |lc R|`; `q^t ∣ lc R` (algebraic).
Does mathlib already have a canonical form? yes: the rational root theorem is stated as divisibility of `leadingCoeff` (`den_dvd_of_is_root`).
Our statement is a derived inequality → REFACTOR for mathlib to the divisibility form; the inequality stays a project corollary.
RHS convention respected? n/a (not an equation/iff)

### Syntactic generality — `Roth.pow_rootMultiplicity_le`

Alternative restatements attempted:
- explicit `h q : R`, `IsRelPrime`, `q ≠ 0`, divisibility (evidence (1))
- `r : K` with `IsFractionRing.den A r` over a UFD (evidence (2))
Chosen restatement: explicit `h q` main lemma, `den` corollary.
Justification: matches the parent lemma and the project call site, which has explicit `h`, `q`.

### Superfluous-argument audit — `Roth.pow_rootMultiplicity_le`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hR : R ≠ 0` | only for the inequality | not needed for divisibility |
| 2 | `hq : 0 < q` | only `q ≠ 0` | weaken |
| 3 | `hcop : IsCoprime` | only `IsRelPrime` | weaken |
| 4 | `B`, `hB` | packaging | drop in mathlib form |
| 5 | ℤ / ℚ / ℝ | no | normalized-GCD domain and its fraction field |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (divisibility of `leadingCoeff`)
Syntactic generality: RESTATE (general divisibility form, UFD `den` corollary)
Superfluous arguments: 4 to drop/weaken in the mathlib form (`hR`, `B`/`hB`, `0 < q` to `q ≠ 0`, `IsCoprime` to `IsRelPrime`)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.pow_rootMultiplicity_le`

Internal use count: 0 outside the declaring file; 1 inside Roth/Theta.lean.
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Theta.lean:245 | `(pow_rootMultiplicity_le ((map_ne_zero_iff _ (uniqueAlgEquiv ℤ σ).injective).2 hR) (Nat.zero_lt_of_lt hq) hh hRB)` inside `Real.log_le_log` (in `index_unique_le_log_div`) |

Inline-derivation grep (`grep -rn "leadingCoeff" Roth/` near `rootMultiplicity`): (none); the comparison is done only here.

### Composition check (Phase 6)

Can `Roth.pow_rootMultiplicity_le` be derived from mathlib in ≤3 chained calls?

Attempt 1: `den_dvd_of_is_root` then `Int.le_of_dvd` — gives only `q ≤ |lc|` (multiplicity 1); fails for `t > 1`.
Attempt 2: parent factorisation + `leadingCoeff_mul`/`leadingCoeff_pow`/`leadingCoeff_linear` + `Int.le_of_dvd` — works but the factorisation is not in mathlib (parent verdict YES-but-generalise-first) and the rest is a multi-step proof.

Conclusion: NOT-COMPOSABLE.

## Verdict: `Roth.pow_rootMultiplicity_le`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): multiplicity form of the rational root theorem part 2, standard over UFD/GCD domains; local source states the ℤ case with a bound `B`.
- Generality analysis (Phase 4): STRICTLY NARROWER; the divisibility form over a normalized-GCD domain compiles (evidence (1)) and recovers the project statement (evidence (3)).
- Mathlib search (Phase 5): not in mathlib; only the multiplicity-1 `den_dvd_of_is_root`.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

Mathlib's `den_dvd_of_is_root` (RationalRoot.lean:89) gives `den r ∣ p.leadingCoeff` for a root `r`, ignoring multiplicity. The project lemma's real content is the multiplicity strengthening `q ^ mult ∣ p.leadingCoeff`, which is the missing companion of the parent `pow_rootMultiplicity_dvd_of_isRelPrime`. The real-valued bound with `B` and `R ≠ 0` is Diophantine packaging and should stay in the project as a short corollary via `Int.le_of_dvd`. The generalised lemma has a 4-line proof from the parent and holds for `p = 0`.

Reason for the generalisation: LITERATURE-WEAKENING (ℤ to GCD domain, `IsCoprime` to `IsRelPrime`, `0 < q` to `q ≠ 0`, drop `R ≠ 0`) and MODERN-IDIOM (divisibility of `leadingCoeff` instead of a real inequality; `IsFractionRing.den` corollary).

Proposed restatement:
```lean
theorem Polynomial.pow_rootMultiplicity_dvd_leadingCoeff {R K : Type*} [CommRing R] [IsDomain R]
    [NormalizedGCDMonoid R] [Field K] [Algebra R K] [IsFractionRing R K] (p : R[X]) {h q : R}
    (hq : q ≠ 0) (hcop : IsRelPrime h q) :
    q ^ rootMultiplicity (algebraMap R K h / algebraMap R K q) (p.map (algebraMap R K)) ∣
      p.leadingCoeff := by
  sorry  -- compiled in evidence (4 lines from pow_rootMultiplicity_dvd_of_isRelPrime)

theorem den_pow_rootMultiplicity_dvd_leadingCoeff {A K : Type*} [CommRing A] [IsDomain A]
    [UniqueFactorizationMonoid A] [NormalizedGCDMonoid A] [Field K] [Algebra A K]
    [IsFractionRing A K] (p : A[X]) (r : K) :
    (IsFractionRing.den A r : A) ^ rootMultiplicity r (p.map (algebraMap A K)) ∣
      p.leadingCoeff := by
  sorry  -- compiled in evidence
```

Estimated cost of regeneralisation: CHEAP.

Mathlib downstream this enables:
- multiplicity version of `den_dvd_of_is_root`, next to it in `Mathlib/RingTheory/Polynomial/RationalRoot.lean`;
- size bounds `q^t ≤ |lc p|` over ℤ (Liouville/Roth-type arguments) by one `Int.le_of_dvd`;
- the ℤ/ℝ Roth form becomes a direct corollary.

PR grouping: ship with the parent `pow_rootMultiplicity_dvd_of_isRelPrime`, `IsPrimitive.pow` and `isPrimitive_C_mul_X_sub_C` (from the `Roth.exists_eq_pow_mul_of_rootMultiplicity` assessment) as one PR.

Call sites in our project: 1 (Roth/Theta.lean:245). After upstreaming, re-prove the project lemma as evidence (3) (or inline it into `index_unique_le_log_div`).

Next action: run `/generalise Roth.pow_rootMultiplicity_le` targeting the divisibility form, then add it to the parent's PR.

## Next step

Run `/generalise Roth.pow_rootMultiplicity_le` (target: compiled `pow_rootMultiplicity_dvd_leadingCoeff` over a normalized-GCD domain) and bundle it, with its UFD `den` corollary, into the PR proposed for `Roth.exists_eq_pow_mul_of_rootMultiplicity` (`Mathlib/RingTheory/Polynomial/RationalRoot.lean` / `GaussLemma.lean`). Locally keep the real bound (sole caller Roth/Theta.lean:245) until upstreamed.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.pow_rootMultiplicity_le/generalise.lean` (imports `Mathlib.RingTheory.Polynomial.GaussLemma`, `Mathlib.RingTheory.Polynomial.RationalRoot`, `Mathlib.Basic.Real.Basic`, `Mathlib.Tactic.Positivity`). Final `lean_diagnostic_messages`: success, no diagnostics. Contents: parent lemma copy; (1) `pow_rootMultiplicity_dvd_leadingCoeff` over a normalized-GCD domain; (2) UFD `den` form; (3) exact project statement from (1) via `Int.le_of_dvd`. One earlier iteration failed (`rw [hQ]` also rewrote inside the multiplicity; fixed with `generalize`), and the deprecated `Mathlib.Data.Real.Basic` import was replaced.
- WebSearch ×3 (queries in the table).
- LeanSearch, Lean-Finder, Loogle and grep as in Phase 5.
- Local refs: clean.tex l.680–700.
- `grep -rn pow_rootMultiplicity_le Roth/` for call sites.
- Sibling report reused: Roth.exists_eq_pow_mul_of_rootMultiplicity.md.
- ChatGPT channel: n/a (the `ask_chatgpt_math` MCP is not configured in this session).
