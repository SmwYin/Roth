---
decl: Roth.exists_eq_pow_mul_of_rootMultiplicity
file: Roth/Theta.lean
line: 184
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Gauss-lemma consequence that (qX - h)^t divides R in Z[X] when h/q (coprime) is a root of multiplicity t over Q; mathlib has the pieces (IsPrimitive.dvd_of_fraction_map_dvd_fraction_map, pow_rootMultiplicity_dvd, num_den_reduced) but no such lemma, and the compiled general form over any normalized-GCD domain with fraction field (IsRelPrime, q ne 0, divisibility conclusion) is a natural multiplicity strengthening of mathlib's rational root theorem.
action: Upstream the compiled general form pow_rootMultiplicity_dvd_of_isRelPrime (plus isPrimitive_C_mul_X_sub_C and a num/den corollary) to Mathlib/RingTheory/Polynomial/GaussLemma.lean; locally keep the lemma (sole caller Roth/Theta.lean:209 pow_rootMultiplicity_le) or restate it as a one-line corollary once upstreamed.
---

# Roth.exists_eq_pow_mul_of_rootMultiplicity

## Inventory entry

### `theorem Roth.exists_eq_pow_mul_of_rootMultiplicity`
- **Type**: `∀ {R : Polynomial ℤ} {h : ℤ} {q : ℕ}, 0 < q → IsCoprime h (q : ℤ) → ∃ Q : Polynomial ℤ, R = (C (q : ℤ) * X - C h) ^ rootMultiplicity ((h : ℚ) / q) (R.map (Int.castRingHom ℚ)) * Q`
- **What**: If `h` and `q > 0` are coprime and `t` is the multiplicity of `h/q` as a root of `R` over ℚ, then `(qX − h)^t` divides `R` in ℤ[X].
- **How**: `t` is set to the multiplicity. `hmap` computes `(qX − h)` mapped to ℚ[X] as `C q * (X − C (h/q))` via `Polynomial.map_sub/map_mul/map_C/map_X`, `mul_sub`, `mul_div_cancel₀`. Then Gauss's lemma `Polynomial.IsPrimitive.Int.dvd_iff_map_cast_dvd_map_cast` with primitivity from the private `isPrimitive_pow (isPrimitive_linear hcop) t` reduces to divisibility over ℚ. Over ℚ it rewrites with `Polynomial.map_pow`, `mul_pow`, `C_pow`, `Polynomial.C_mul_dvd` (unit constant) and closes with `Polynomial.pow_rootMultiplicity_dvd`.
- **Hypotheses**: `hq : 0 < q` (only `q ≠ 0` is used); `hcop : IsCoprime h q` (only relative primality is used). `R` need not be nonzero (for `R = 0` the multiplicity is 0).
- **Uses from project**: `Roth.isPrimitive_linear` (private, Theta.lean:167), `Roth.isPrimitive_pow` (private, Theta.lean:175).
- **Used by**: Roth/Theta.lean:209 (`pow_rootMultiplicity_le`, the leading-coefficient bound of Lemma 5). `grep -rn exists_eq_pow_mul_of_rootMultiplicity Roth/` gives only the definition and this use. Transitively used by `index_unique_le_log_div` (Theta.lean:245) and the Lemma 5 chain.
- **Visibility**: public
- **Lines**: 179–200 (docstring 179–183, statement 184–187, proof 188–200), proof length 13 lines
- **Notes**: Source: clean.tex l.677–699 (§5, proof of Lemma 5, "The polynomial (q_1x_1-h_1)^t is primitive and divides R over ℚ. Gauss's lemma therefore gives ..."). The existential `∃ Q, R = _ * Q` is definitionally `_ ∣ R`; mathlib would state the `∣` form.

## Junk check (Step 8)
- **Used anywhere?** Yes, once (Theta.lean:209), essential for Lemma 5.
- **Wrapper of 1–2 mathlib calls?** No. It combines three mathlib lemmas plus two private primitivity helpers and a map computation (13 lines).
- **Does mathlib have it?** No (Phase 5 below). Mathlib has the rational root theorem (`num_dvd_of_is_root`, `den_dvd_of_is_root`) and Gauss's lemma for divisibility, but no multiplicity lift of a rational root to an integral linear factor.
- **Too specific (inline?)?** No. It is the Gauss-lemma step the source names, and isolating it keeps `pow_rootMultiplicity_le` short.
- **Well-chosen?** Yes, modulo stating it with `∣` and `q ≠ 0`, which are cosmetic locally.
- **Conclusion:** `KEEP`.

## Mathlibable assessment (Step 9)

Pre-filter: public; name does not end in `_aux`; docstring not internal/auxiliary; Step 8 said KEEP; no `namespace Roth` in `.lake/packages/mathlib/Mathlib/`. Not a glue lemma (genuine 13-line proof). Its helpers `Roth.isPrimitive_linear` and `Roth.isPrimitive_pow` were SKIP (private), so there is no parent verdict to inherit. Full run follows.

### Baseline (Phase 0)
- lake build:               clean (project built per the brief; the evidence file elaborates with no diagnostics)
- decl `Roth.exists_eq_pow_mul_of_rootMultiplicity`: resolved at Roth/Theta.lean:184
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  `Θ_m(B; q; r)`, the supremum of indices of bounded integer polynomials at rational points, and Lemmas 5–7 bounding it

### Statement (Phase 1)

`Roth.exists_eq_pow_mul_of_rootMultiplicity` is a theorem stating the following.

Let `R ∈ ℤ[X]`, and let `h ∈ ℤ`, `q ∈ ℕ` with `q > 0` and `gcd(h, q) = 1`. Let `t` be the multiplicity of `h/q` as a root of `R` viewed in ℚ[X]. Then `(qX − h)^t` divides `R` in ℤ[X], i.e. `R = (qX − h)^t Q` for some `Q ∈ ℤ[X]`.

Variables / typeclasses involved (Lean side):
- `R : ℤ[X]`: the polynomial.
- `h : ℤ`, `q : ℕ`: numerator and denominator of the rational point.

Hypotheses (Lean side):
- `hq : 0 < q`: the denominator is nonzero.
- `hcop : IsCoprime h q`: the fraction is reduced.

Conclusion (math): `(qX − h)^{mult_{h/q}(R)} ∣ R` in ℤ[X].

Conclusion (Lean): `∃ Q : ℤ[X], R = (C (q:ℤ) * X - C h) ^ rootMultiplicity ((h:ℚ)/q) (R.map (Int.castRingHom ℚ)) * Q`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a helper step (the Gauss-lemma step) inside the proof of Lemma 5, not a main result.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 13 substantive lines
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE (check skipped, theorem).

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | rational root a/b lowest terms multiplicity k integer polynomial (bx - a)^k divides Gauss lemma | partial | rational root theorem (a ∣ a_0, b ∣ a_n); "special case (single linear factor) of Gauss's lemma" (Wikipedia Rational root theorem, ProofWiki, cut-the-knot) | the k-fold version is not stated anywhere explicitly; it is the obvious iteration |
| 2 | WebSearch (general form) | Gauss lemma UFD primitive polynomial divides over fraction field then divides over ring corollary linear factor root multiplicity | yes | over a UFD/GCD domain R with fraction field F, a primitive g ∈ R[x] dividing f in F[x] divides f in R[x] (Wikipedia Gauss's lemma, TCD/UMich/LSU/Reed notes) | this is the general engine; our lemma applies it to g = (bX − a)^t |
| 3 | WebSearch (named-after / aliases) | Roth lemma proof "q_1 x_1 - h_1" primitive Gauss lemma index rational point leading coefficient bound | no | none Roth-specific; general Gauss-lemma notes | the step is standard bookkeeping in Roth's lemma (one-variable case) |
| 4 | ChatGPT MCP | n/a | n/a | n/a | the `ask_chatgpt_math` MCP is not configured in this session (absent from the tool list) |
| 5 | Local references | clean.tex l.677–699 | yes | "(q_1x_1-h_1)^t is primitive and divides R over ℚ. Gauss's lemma therefore gives ... R = (q_1x_1-h_1)^t Q" | exactly the project statement; the Lean note points to mathlib's GaussLemma file |
| 6 | nLab | Gauss's lemma / primitive polynomial | partial | nLab treats Gauss's lemma (content multiplicative) abstractly; no multiplicity corollary | general form only |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept (divisibility in a polynomial ring) |
| 8 | Stacks Project | n/a | n/a | n/a | commutative algebra of GCD domains is not where Stacks states Gauss-lemma corollaries; no relevant tag beyond normal-domain basics |
| 9 | MathOverflow / Math.SE | covered by searches 1–2 | no | n/a | too elementary for a thread; standard textbook exercise |
| 10 | recent arXiv (last 5 years) | search 3 surfaced arXiv 2503.20071 | partial | uses Gauss's lemma after normalising a leading coefficient | analogy only |

### Literature summary (Phase 3)

Concept identified as: Gauss's lemma corollary / rational root theorem with multiplicity: if `a/b` is a reduced root of multiplicity `t` of `f ∈ R[X]` (R a UFD/GCD domain), then `(bX − a)^t ∣ f` in R[X].
Sources agree on the standard form: yes (tacitly; every source proves the `t = 1` case, i.e. the rational root theorem, as a special case of Gauss's lemma).
Most general standard form: R a GCD domain (UFD in textbooks) with fraction field K; `a, b ∈ R` relatively prime, `b ≠ 0`; `(bX − a)^{mult_{a/b}(f)} ∣ f`.
Generality dimensions where the literature varies:
  - base ring: ℤ (elementary texts) to UFD / GCD domain (algebra texts); most general is GCD domain.
  - coprimality: gcd = 1 (relatively prime), which over ℤ coincides with Bézout coprimality.
Disagreement with the literature: none mathematically; the Lean form is the ℤ specialisation with Bézout `IsCoprime` and `0 < q` (q a natural number).

### Generality analysis — `Roth.exists_eq_pow_mul_of_rootMultiplicity`

Literature-standard form: over a GCD domain with fraction field, relatively prime `h, q`, `q ≠ 0`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | base ring ℤ, field ℚ | `Polynomial ℤ`, `Int.castRingHom ℚ` | GCD domain `R`, `IsFractionRing R K` | yes | proof uses only Gauss's lemma (`IsPrimitive.dvd_of_fraction_map_dvd_fraction_map`, needs `[NormalizedGCDMonoid R]` in practice) — compiled in evidence (1) |
| 2 | `q : ℕ`, `hq : 0 < q` | positive natural | `q ∈ R`, `q ≠ 0` | yes | only `q ≠ 0` is used (to cancel the unit constant) — compiled |
| 3 | `hcop : IsCoprime h q` | Bézout coprime | `IsRelPrime h q` | yes | primitivity of `C q * X - C h` needs only that common divisors are units — compiled (`isPrimitive_C_mul_X_sub_C`, any `CommRing`) |
| 4 | conclusion `∃ Q, R = _ * Q` | existential | `_ ∣ R` | yes (cosmetic) | definitionally equal; `∣` is mathlib's normal form |
| 5 | `R` | arbitrary | arbitrary | already general | no `R ≠ 0` needed |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 4 (all verified clean in the evidence file)
Proposed restatement:

```lean
theorem Polynomial.pow_rootMultiplicity_dvd_of_isRelPrime {R K : Type*} [CommRing R] [IsDomain R]
    [NormalizedGCDMonoid R] [Field K] [Algebra R K] [IsFractionRing R K] (p : R[X]) {h q : R}
    (hq : q ≠ 0) (hcop : IsRelPrime h q) :
    (C q * X - C h) ^ rootMultiplicity (algebraMap R K h / algebraMap R K q)
      (p.map (algebraMap R K)) ∣ p
```

Cost of restatement: CHEAP — the existing proof transfers verbatim (compiled, 9-line proof), and the project form is a 3-line corollary (evidence (3)).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | Typeclasses instead of preambles? | no | no preamble hypotheses | — |
| 2 | Sequences vs filters? | no | algebraic divisibility | — |
| 3 | Construction vs universal property? | no | — | — |
| 4 | Bundled substructure? | no | — | — |
| 5 | Field-specific vs typeclass-weakened? | yes | ℤ/ℚ to GCD domain / fraction field (row 1 above) | composes with `IsFractionRing` API and the rational root theorem file |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index generalised? | yes | `q : ℕ` to `q : R` | removes casts |
| 8 | Concrete-via-abstract? | yes | the proof never uses ℤ beyond Gauss's lemma: restate with `IsFractionRing.num A r`, `IsFractionRing.den A r` for any `r : K` over a UFD: `(C (den A r) * X - C (num A r)) ^ rootMultiplicity r (p.map (algebraMap A K)) ∣ p` (evidence (2)) | directly strengthens `den_dvd_of_is_root` (den^mult ∣ leadingCoeff) and `num_dvd_of_is_root` |
| 9 | False-generalisation guard | no false generalisation | the general statement specialises exactly to the ℤ/ℚ statement (evidence (3)) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: the `IsRelPrime` form above, plus the `num`/`den` corollary for UFDs.
  - Cost: CHEAP (both compiled).
  - Mathlib downstream this enables: a multiplicity version of the rational root theorem in `Mathlib/RingTheory/Polynomial/RationalRoot.lean` style; `den A r ^ rootMultiplicity r _ ∣ p.leadingCoeff` follows by comparing leading coefficients (as the project's `pow_rootMultiplicity_le` does).
  - Real mathematical improvement: removes the ℤ-specific statement and the `∃` packaging; the content is about any GCD domain.

### Proof strategy — `Roth.exists_eq_pow_mul_of_rootMultiplicity`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers? | yes | `IsPrimitive.pow` (mathlib has `IsPrimitive.mul` but no `pow`) and `isPrimitive_C_mul_X_sub_C` (primitivity of a reduced linear polynomial) | CHEAP (both compiled in evidence; ship in the same PR) |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (Gauss's lemma reduction, map computation, `pow_rootMultiplicity_dvd`).
  - Missing mathlib API: `Polynomial.IsPrimitive.pow`, `Polynomial.isPrimitive_C_mul_X_sub_C` (or `IsRelPrime.isPrimitive_C_mul_X_sub_C`).

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.exists_eq_pow_mul_of_rootMultiplicity`

[A] Lean-Finder       "power of (den * X - num) to the root multiplicity of a rational root divides the polynomial over a UFD (Gauss lemma)"   hits: `Polynomial.pow_rootMultiplicity_dvd`, `den_dvd_of_is_root`, `num_dvd_of_is_root`, `Polynomial.exists_eq_pow_rootMultiplicity_mul_and_not_dvd`, `Polynomial.pow_mul_divByMonic_rootMultiplicity_eq` (building blocks / weaker analogues; none over the base ring)
[B] Loogle            `(Polynomial.C _ * Polynomial.X - Polynomial.C _) ^ Polynomial.rootMultiplicity _ _ ∣ _`   no hits
[C] LeanSearch        "if a/b in lowest terms is a root of multiplicity t of integer polynomial p then (bX - a)^t divides p"   hits: `pow_rootMultiplicity_dvd`, `le_rootMultiplicity_iff`, `pow_rootMultiplicity_not_dvd`, `prod_multiset_X_sub_C_dvd`, `dvd_iff_isRoot` (all over the field / same ring; no lift)
[D] Grep mathlib src  `exists_eq_pow_rootMultiplicity_mul_and_not_dvd` (Algebra/Polynomial/Div.lean:551, root in the same ring), `pow_rootMultiplicity_dvd` (Div.lean:538), `IsPrimitive.dvd_of_fraction_map_dvd_fraction_map` (RingTheory/Polynomial/GaussLemma.lean:299, `[IsGCDMonoid R]` section), `IsPrimitive.Int.dvd_iff_map_cast_dvd_map_cast` (GaussLemma.lean:324), `num_dvd_of_is_root`/`den_dvd_of_is_root` (RingTheory/Polynomial/RationalRoot.lean:69, 89), `num_den_reduced` (RingTheory/Localization/NumDen.lean:56); grep for `IsPrimitive.pow`, `isPrimitive_pow`, primitive `C _ * X - C _` / `X - C`: no hits; files mentioning both `rootMultiplicity` and `IsPrimitive`/`IsFractionRing`: only FieldTheory/IsAlgClosed/Basic, RingTheory/Invariant/Basic, Algebra/Polynomial/Roots, none relevant
[E] Name pattern      `pow_rootMultiplicity_dvd*`, `IsPrimitive.pow`, `isPrimitive_C_mul_X_sub_C` via lean_local_search / grep: only the base `pow_rootMultiplicity_dvd`; the others absent

Searched for both:
  - the user's form (ℤ, ℚ): not in mathlib
  - the literature-standard form (GCD domain, fraction field; num/den form): not in mathlib

Concluded: found building blocks (`IsPrimitive.dvd_of_fraction_map_dvd_fraction_map`, `IsPrimitive.Int.dvd_iff_map_cast_dvd_map_cast`, `pow_rootMultiplicity_dvd`, `C_mul_dvd`, `IsPrimitive.mul`, `num_den_reduced`); the composition is a genuine 9-line proof plus two missing helper lemmas, not a ≤3-call composition.

### Normal-form check — `Roth.exists_eq_pow_mul_of_rootMultiplicity`

Equivalent formalisms: `∃ Q, R = g * Q` (current); `g ∣ R` (mathlib normal form); `t ≤ multiplicity`-style via `le_rootMultiplicity_iff` (only over the field).
Does mathlib already have a canonical form? yes: divisibility `_ ∣ p`, as in `pow_rootMultiplicity_dvd`.
Our statement uses the unfolded existential → REFACTOR to the `∣` form for mathlib (definitionally equal, so call sites keep `obtain ⟨Q, hQ⟩`).
RHS convention respected? n/a (not an equation/iff)

### Syntactic generality — `Roth.exists_eq_pow_mul_of_rootMultiplicity`

Alternative restatements attempted:
- explicit `h q : R` with `IsRelPrime h q`, `q ≠ 0` (evidence (1))
- `r : K` with `num A r`, `den A r` (evidence (2))
Chosen restatement: the explicit `h q` form as the main lemma, with the `num`/`den` form as a corollary.
Justification: the explicit form applies to any reduced representation (the project's call site supplies `h`, `q` directly), and the num/den form follows in one line.

### Superfluous-argument audit — `Roth.exists_eq_pow_mul_of_rootMultiplicity`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hq : 0 < q` | only `q ≠ 0` | weaken |
| 2 | `hcop : IsCoprime h q` | only `IsRelPrime h q` | weaken (equivalent over ℤ) |
| 3 | ℤ / ℚ | no | any normalized-GCD domain and its fraction field |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (state with `∣`)
Syntactic generality: RESTATE (general `IsRelPrime` form, num/den corollary)
Superfluous arguments: 2 to weaken (`0 < q` to `q ≠ 0`, `IsCoprime` to `IsRelPrime`)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.exists_eq_pow_mul_of_rootMultiplicity`

Internal use count: 0 outside the declaring file; 1 inside Roth/Theta.lean.
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Theta.lean:209 | `obtain ⟨Q, hQ⟩ := exists_eq_pow_mul_of_rootMultiplicity hq hcop` (in `pow_rootMultiplicity_le`) |

Inline-derivation grep (`grep -rn "rootMultiplicity\|IsPrimitive" Roth/`, outside Theta.lean l.160–249):
  - (none). Roth/Index.lean:236–243 uses `rootMultiplicity` only for the Taylor-index identification, not a Gauss-lemma lift.

### Composition check (Phase 6)

Can `Roth.exists_eq_pow_mul_of_rootMultiplicity` be derived from mathlib in ≤3 chained calls?

Attempt 1: `(IsPrimitive.Int.dvd_iff_map_cast_dvd_map_cast _ _ hprim).2 (by rw [...]; exact pow_rootMultiplicity_dvd _ _)`
  - Mathlib decls used: `IsPrimitive.Int.dvd_iff_map_cast_dvd_map_cast`, `pow_rootMultiplicity_dvd`, `C_mul_dvd`, `map_pow`, `mul_pow`, `C_pow`.
  - Result: partial. The primitivity `hprim` of `(qX − h)^t` is not in mathlib (needs `IsPrimitive.pow` and primitivity of a reduced linear polynomial), and the map computation `hmap` is a 3-line rewrite.
Attempt 2: via `exists_eq_pow_rootMultiplicity_mul_and_not_dvd` over ℚ and clearing denominators — fails (still needs Gauss's lemma and primitivity).

Conclusion: NOT-COMPOSABLE (13-line proof with two missing helpers).

## Verdict: `Roth.exists_eq_pow_mul_of_rootMultiplicity`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): the statement is the multiplicity form of the rational root theorem / Gauss's lemma corollary, standard over UFDs/GCD domains; the local source states exactly the ℤ case.
- Generality analysis (Phase 4): STRICTLY NARROWER; the general form over a normalized-GCD domain with fraction field, `IsRelPrime`, `q ≠ 0`, `∣` conclusion compiles (evidence (1)).
- Mathlib search (Phase 5): not in mathlib in either form; building blocks only.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

Mathlib's `RationalRoot.lean` proves that for a root `r = num/den` of `p` over a UFD, `num ∣ p.coeff 0` and `den ∣ p.leadingCoeff`, and `GaussLemma.lean` proves primitive divisors lift from `K[X]` to `R[X]`. Nothing connects these to root multiplicity: there is no lemma giving the integral factor `(den·X − num)^{mult}` of `p`, nor even `IsPrimitive.pow` or primitivity of a reduced linear polynomial. The project lemma is exactly this missing link, specialised to ℤ. The general version transfers with the same proof (compiled), and the project statement is a 3-line corollary, so the change is cheap and mechanical.

Reason for the generalisation: LITERATURE-WEAKENING (ℤ to GCD domain, `IsCoprime` to `IsRelPrime`, `0 < q` to `q ≠ 0`) and MODERN-IDIOM (`∣` conclusion, `IsFractionRing.num/den` corollary).

Proposed restatement:
```lean
theorem Polynomial.isPrimitive_C_mul_X_sub_C {R : Type*} [CommRing R] {h q : R}
    (hcop : IsRelPrime h q) : (C q * X - C h).IsPrimitive := by
  sorry  -- compiled in evidence

theorem Polynomial.IsPrimitive.pow {p : R[X]} (hp : p.IsPrimitive) (n : ℕ) : (p ^ n).IsPrimitive := by
  sorry  -- compiled inline in evidence (Nat.rec with IsPrimitive.mul)

theorem Polynomial.pow_rootMultiplicity_dvd_of_isRelPrime {R K : Type*} [CommRing R] [IsDomain R]
    [NormalizedGCDMonoid R] [Field K] [Algebra R K] [IsFractionRing R K] (p : R[X]) {h q : R}
    (hq : q ≠ 0) (hcop : IsRelPrime h q) :
    (C q * X - C h) ^ rootMultiplicity (algebraMap R K h / algebraMap R K q)
      (p.map (algebraMap R K)) ∣ p := by
  sorry  -- compiled in evidence; current proof survives verbatim
```
plus the corollary `(C (den A r : A) * X - C (num A r)) ^ rootMultiplicity r (p.map (algebraMap A K)) ∣ p` for UFDs.

Estimated cost of regeneralisation: CHEAP.

Mathlib downstream this enables:
- a multiplicity version of `den_dvd_of_is_root` (`den ^ mult ∣ leadingCoeff`) by comparing leading coefficients;
- `IsPrimitive.pow` fills an obvious gap next to `IsPrimitive.mul` in `Mathlib/RingTheory/Polynomial/Content.lean`;
- the ℤ form becomes a direct specialisation, removing the `Int.castRingHom`-specific statement.

Proposed mathlib location: `Mathlib/RingTheory/Polynomial/GaussLemma.lean` (the `GCDMonoid` section, after `IsPrimitive.dvd_iff_fraction_map_dvd_fraction_map`); `IsPrimitive.pow` and `isPrimitive_C_mul_X_sub_C` in `Mathlib/RingTheory/Polynomial/Content.lean`. One PR.

Call sites in our project (from Phase 6.0): 1 (Roth/Theta.lean:209). Locally, nothing has to change; after upstreaming, the project lemma becomes the 3-line corollary of evidence (3) (or the call site uses the mathlib lemma directly, since `obtain ⟨Q, hQ⟩` works on `∣`), and the private helpers `isPrimitive_linear` / `isPrimitive_pow` can be deleted.

Next action: run `/generalise Roth.exists_eq_pow_mul_of_rootMultiplicity` targeting the evidence-file statement, then prepare the GaussLemma/Content PR.

## Next step

Run `/generalise Roth.exists_eq_pow_mul_of_rootMultiplicity` (target: the compiled `pow_rootMultiplicity_dvd_of_isRelPrime` over a normalized-GCD domain) and open one PR adding it, `IsPrimitive.pow` and `isPrimitive_C_mul_X_sub_C` to `Mathlib/RingTheory/Polynomial/GaussLemma.lean` / `Content.lean`. Locally keep the lemma (sole caller Roth/Theta.lean:209) until upstreamed.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.exists_eq_pow_mul_of_rootMultiplicity/generalise.lean` (imports `Mathlib.RingTheory.Polynomial.GaussLemma` and `Mathlib.RingTheory.Polynomial.RationalRoot` only). Final `lean_diagnostic_messages`: success, no diagnostics. Contents:
  - `isPrimitive_C_mul_X_sub_C` over any `CommRing` from `IsRelPrime`;
  - (1) `pow_rootMultiplicity_dvd_of_isRelPrime` over a normalized-GCD domain with fraction field (`q ≠ 0`, `IsRelPrime`, `∣` conclusion);
  - (2) the UFD `num`/`den` corollary via `IsFractionRing.mk'_num_den'`, `num_den_reduced`;
  - (3) the exact project statement recovered from (1) with `IsCoprime.isRelPrime`.
  Two earlier iterations failed and were fixed: `[IsGCDMonoid R]` alone did not synthesise the `NormalizedGCDMonoid` instance needed by `dvd_of_fraction_map_dvd_fraction_map` (switched to `[NormalizedGCDMonoid R]`); `simpa` in (3) did not unfold `∣` (replaced by `simp only [algebraMap_int_eq, eq_intCast, Int.cast_natCast] at this; exact this`).
- WebSearch ×3 (queries in the table). Sources: Wikipedia "Rational root theorem" and "Gauss's lemma (polynomials)", ProofWiki, cut-the-knot, TCD/UMich/LSU/Reed course notes, arXiv 2503.20071.
- LeanSearch, Lean-Finder, Loogle queries as in Phase 5; grep of `.lake/packages/mathlib/Mathlib/` as in [D].
- Local refs: clean.tex l.672–699.
- `grep -rn exists_eq_pow_mul_of_rootMultiplicity Roth/` and `grep -rn "rootMultiplicity\|IsPrimitive" Roth` for the call-sites table.
- Sibling reports reused: Roth.isPrimitive_linear.md, Roth.isPrimitive_pow.md (both SKIP private), Roth.Θ_equiv.md (format).
- ChatGPT channel: n/a (the `ask_chatgpt_math` MCP is not configured in this session).
