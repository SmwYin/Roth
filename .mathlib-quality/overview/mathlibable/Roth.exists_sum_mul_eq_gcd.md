---
decl: Roth.exists_sum_mul_eq_gcd
file: Roth/Separation.lean
line: 374
kind: theorem
visibility: public
verdict: NO-mathlib-has-it
cost: n/a
junk: REPLACE
rationale: Restatement over ℤ (with sides and factors swapped) of mathlib's Finset.gcd_eq_sum_mul, which holds in any IsBezout NormalizedGCDMonoid commutative ring; the project proof is literally simpa using that lemma.
action: At Roth/Separation.lean:446 (exists_int_eq_of_gcd_eq_one) use `obtain ⟨z, hz⟩ := Finset.gcd_eq_sum_mul s u` and adapt the calc to the orientation `s.gcd u = ∑ i ∈ s, u i * z i` (compiled in evidence); then delete exists_sum_mul_eq_gcd; no mathlib PR.
---

# Roth.exists_sum_mul_eq_gcd

## Inventory entry

### `theorem Roth.exists_sum_mul_eq_gcd`
- **Type**: `∀ {ι : Type u_1} (s : Finset ι) (u : ι → ℤ), ∃ z : ι → ℤ, ∑ i ∈ s, z i * u i = s.gcd u` (confirmed by `#check`, evidence (0))
- **What**: Bézout's identity for a finite family of integers: the (normalized) finset gcd of `u` over `s` is an integer linear combination of the `u i`, `i ∈ s`.
- **How**: one line, `simpa [eq_comm, mul_comm] using Finset.gcd_eq_sum_mul s u` (mathlib, Mathlib/RingTheory/PrincipalIdealDomain.lean:233), only flipping the equation and the factor order.
- **Hypotheses**: none beyond the data `s`, `u`; ring fixed to `ℤ`.
- **Uses from project**: `[]`
- **Used by**: `Roth.exists_int_eq_of_gcd_eq_one` (Roth/Separation.lean:446, `obtain ⟨z, hz⟩ := exists_sum_mul_eq_gcd s u`). No other uses (`grep -rn exists_sum_mul_eq_gcd Roth/`).
- **Visibility**: public
- **Lines**: 372–376, proof length 1 line
- **Notes**: Section `Integrality` of Separation.lean; docstring cites the source's Lean implementation note ("by a Bézout relation", clean.tex:432).

## Junk check (Step 8)
- Used anywhere? Yes, once (Separation.lean:446).
- Wrapper of 1–2 mathlib calls? Yes: exactly `Finset.gcd_eq_sum_mul` plus `eq_comm`/`mul_comm` normalisation.
- Does mathlib have it? Yes, `Finset.gcd_eq_sum_mul` (any `[CommRing R] [IsBezout R] [NormalizedGCDMonoid R]`; ℤ has both instances, evidence (1),(3)), in the orientation `s.gcd f = ∑ a ∈ s, f a * g a`.
- Too specific? Yes: specialised to ℤ and stated in a non-mathlib orientation; the single call site works equally well with the mathlib orientation (evidence (2)).
- Well-chosen? No new content.
- Conclusion: `REPLACE` — call `Finset.gcd_eq_sum_mul s u` directly at :446 and delete this theorem.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring does not start with internal/auxiliary; Step 8 = REPLACE (not REMOVE); qualified name `Roth.exists_sum_mul_eq_gcd` absent from mathlib (grep for `exists_sum_mul_eq_gcd` over `.lake/packages/mathlib/Mathlib/`: no hit). Not a glue lemma about an assessed parent def (no project def involved). Full workflow below.

### Baseline (Phase 0)
- lake build:               clean (per brief; evidence file importing `Roth.Separation` compiles)
- decl `Roth.exists_sum_mul_eq_gcd`: resolved at Roth/Separation.lean:374
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Separating one variable: the determinant `F = U(x_1, …, x_{p-1}) V(x_p)` (Lemma 2 of the source), including the integrality/primitivity rescaling.

### Statement (Phase 1)

`Roth.exists_sum_mul_eq_gcd` is a theorem stating the following: for a finite index set `s` and integers `u_i` (`i ∈ s`), there are integers `z_i` with `∑_{i∈s} z_i u_i = gcd(u_i : i ∈ s)`, where the gcd is the nonnegative (normalized) one, and the empty gcd is `0`.

Variables / typeclasses involved (Lean side):
- `ι : Type*` — index type.
- `s : Finset ι` — the finite family's index set.
- `u : ι → ℤ` — the integers.

Hypotheses (Lean side):
- none.

Conclusion (math): `gcd(u_i)_{i∈s} ∈ ∑_{i∈s} ℤ u_i`, i.e. the gcd is a ℤ-linear combination of the `u_i`.

Conclusion (Lean): `∃ z : ι → ℤ, ∑ i ∈ s, z i * u i = s.gcd u`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a helper specialisation of a classical named identity (Bézout) to a finite family of integers, used once; not a main result of the project.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE (theorem; check skipped)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Bézout identity several integers gcd of finitely many integers linear combination | yes | `ax + by = gcd(a,b)`; n-integer version by induction via `gcd(x_1..x_n) = gcd(gcd(x_1..x_{n-1}), x_n)` | Brilliant, ProofWiki, Gordon NTIC; n-ary version treated as an immediate corollary |
| 2 | WebSearch (general form) | Bézout domain finitely generated ideal principal gcd linear combination of n elements | yes | in a Bézout domain (every f.g. ideal principal) / PID, gcd of `a_1..a_n` is `∑ d_i a_i` | Wikipedia "Bézout domain", ProofWiki "Bézout's Identity/Principal Ideal Domain" (n elements) |
| 3 | WebSearch (named-after / mathlib aliases) | Mathlib Finset.gcd_eq_sum_mul IsBezout Bézout lemma Finset | partial | doc snapshots show `gcd_eq_gcd_ab` (Euclidean domains, ℤ, ℕ) and Finset gcd API | snapshots predate `Finset.gcd_eq_sum_mul`; its existence confirmed by Loogle/grep in Phase 5 |
| 4 | ChatGPT MCP | n/a | n/a | — | n/a: `ask_chatgpt_math` MCP not configured in this session |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for Bézout | yes | clean.tex:428–432: "if integer coefficients u_a have gcd 1 ... each rational v_b is integral by a Bézout relation" | source uses n-ary Bézout over ℤ as a black box |
| 6 | nLab | Bézout domain / Bézout's identity | partial | nLab treats Bézout domains as integral domains where finitely generated ideals are principal (surfaced via #2 sources) | no finer statement than #2 |
| 7 | nCatLab | n/a | n/a | — | not a categorical concept; elementary ring theory |
| 8 | Stacks Project | n/a | n/a | — | Stacks does not state elementary Bézout identities; the ideal-theoretic form (f.g. ideals principal) is the definition used in #2 |
| 9 | MathOverflow / Math.SE | (covered by #1/#2: n-integer Bézout via induction) | no | — | too elementary to be discussed beyond the induction remark |
| 10 | recent arXiv | n/a | n/a | — | classical (18th c.) result; no recent formulation change; commalg.subwiki and Brown CS mathlib docs (from #2) confirm the Bézout-domain framing used by mathlib |

### Literature summary (Phase 3)

Concept identified as: Bézout's identity (Bézout's lemma) for finitely many elements.
Sources agree on the standard form: yes — the gcd of finitely many elements is a linear combination of them.
Most general standard form: in any Bézout ring (finitely generated ideals principal) with a gcd, the gcd of `a_1, …, a_n` equals `∑ d_i a_i`; equivalently `(a_1, …, a_n) = (gcd)`.
Generality dimensions where the literature varies:
  - ring: ℤ → Euclidean domain → PID → Bézout domain/ring; most general is Bézout ring.
  - arity: two elements → finite family; finite family follows by induction.
Disagreement with the literature: none; the project form is the ℤ specialisation.

### Generality analysis — `Roth.exists_sum_mul_eq_gcd`

Literature-standard form (from Phase 3): for `[CommRing R] [IsBezout R] [NormalizedGCDMonoid R]`, `∃ g, s.gcd f = ∑ a ∈ s, f a * g a`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | coefficient ring `ℤ` | concrete ℤ | any Bézout normalized-GCD comm ring | yes | the same one-line proof compiles for general `R` (evidence (1)); but this general form is exactly mathlib's `Finset.gcd_eq_sum_mul` |
| 2 | `ι : Type*`, `s : Finset ι` | arbitrary | arbitrary | no | already general |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 1 (verified: evidence (1) compiles with ℤ replaced by `[CommRing R] [IsBezout R] [NormalizedGCDMonoid R]`)
Proposed restatement (if STRICTLY NARROWER):

```lean
theorem exists_sum_mul_eq_gcd {R ι : Type*} [CommRing R] [IsBezout R] [NormalizedGCDMonoid R]
    (s : Finset ι) (u : ι → R) : ∃ z : ι → R, ∑ i ∈ s, z i * u i = s.gcd u
```

Cost of restatement: CHEAP — but the restated form is mathlib's `Finset.gcd_eq_sum_mul` up to `eq_comm`/`mul_comm`, so false-positive class 4 (general form already in mathlib) applies: route to NO-mathlib-has-it, not YES-but-generalise-first.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | Preambles to typeclasses? | no | no hypotheses | — |
| 2 | Sequences to filters? | no | no topology | — |
| 3 | Construction vs universal property? | no | an ideal-theoretic phrasing `Ideal.span (u '' s) = Ideal.span {s.gcd u}` exists in spirit (two-element `Ideal.span_gcd`), but the existential form is what the call site needs | — |
| 4 | Set-with-predicate to bundled? | no | — | — |
| 5 | Field/specific to (semi)ring? | yes | ℤ to `IsBezout` + `NormalizedGCDMonoid` | already in mathlib as `Finset.gcd_eq_sum_mul` |
| 6 | 1-categorical to higher? | no | — | — |
| 7 | Concrete index to general structure? | yes (same as row 5) | ℤ to Bézout ring | same as row 5 |
| 8 | Concrete-via-abstract? | yes | proof uses only Bézout property of ℤ via the general mathlib lemma | the abstract form is mathlib's lemma |
| 9 | False-generalisation guard | no | generalising ℤ to Bézout rings preserves meaning (normalized gcd, same identity) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no (as a contribution)
  - One-line reason: the modern/general form already exists in mathlib as `Finset.gcd_eq_sum_mul`; nothing to add.

### Proof strategy — `Roth.exists_sum_mul_eq_gcd`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | proof is a direct mathlib call | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | none | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (it is the mathlib lemma; the wrapper itself is the redundancy)

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.exists_sum_mul_eq_gcd`

[A] Lean-Finder       "Bézout identity for finset gcd: there exist coefficients z with sum z i * u i = s.gcd u"   hits: `IsBezout.gcd_eq_sum`, `exists_gcd_eq_mul_add_mul`, `Int.gcd_eq_gcd_ab` (two-element versions), `Finset.extract_gcd`; v4.28 index did not surface `Finset.gcd_eq_sum_mul`
[B] Loogle            `Finset.gcd _ _ = Finset.sum _ _`   hit: `Finset.gcd_eq_sum_mul` (Mathlib.RingTheory.PrincipalIdealDomain), sole result
[C] LeanSearch        "gcd of a finite family of integers is an integer linear combination of them"   hits: `Int.gcd_eq_gcd_ab`, `exists_gcd_eq_mul_add_mul`, `Int.gcd_least_linear`, `Finset.gcd`
[D] Grep mathlib src  `gcd_eq_sum`, `exists_sum_mul_eq_gcd`, `Finset.gcd.*∑`, `span_gcd`   `Finset.gcd_eq_sum_mul` at Mathlib/RingTheory/PrincipalIdealDomain.lean:233; `IsBezout.gcd_eq_sum` :203; `span_gcd` (two-element) :184, :466, EuclideanDomain.lean:85; no `exists_sum_mul_eq_gcd`
[E] Name pattern      `gcd_eq_sum`   n/a for `lean_local_search` (ripgrep not installed in this session); grep [D] covers the name pattern

Searched for both:
  - the user's current form (ℤ, `∑ z i * u i = s.gcd u`): no ℤ-specific finset statement; covered by the general lemma.
  - the literature-standard form (Bézout ring, finite family): present as `Finset.gcd_eq_sum_mul`.

Concluded: found in mathlib as `Finset.gcd_eq_sum_mul`; more general form (ours is the ℤ specialisation with sides and factors swapped).

### Normal-form check — `Roth.exists_sum_mul_eq_gcd`

Equivalent formalisms: (a) `∃ z, ∑ z i * u i = s.gcd u` (project); (b) `∃ g, s.gcd f = ∑ f a * g a` (mathlib); (c) ideal form `s.gcd u ∈ Ideal.span (u '' s)`.
Does mathlib already have a canonical form? yes — (b), `Finset.gcd_eq_sum_mul`.
Is our statement stated against the canonical form? NO — orientation and factor order differ; no reason to keep (a).
RHS convention respected? n/a (existential statement).

### Syntactic generality — `Roth.exists_sum_mul_eq_gcd`

Alternative restatements attempted:
- mathlib orientation (b) at the call site: works with a 2-token change to the calc (evidence (2)).
Chosen restatement: (b), i.e. use mathlib directly.
Justification: the sole call site is equally served; no extra lemma needed.

### Superfluous-argument audit — `Roth.exists_sum_mul_eq_gcd`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `s : Finset ι` | yes | data |
| 2 | `u : ι → ℤ` | yes | data; ℤ itself is over-specific (evidence (1)) |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (use mathlib's `s.gcd f = ∑ a ∈ s, f a * g a`)
Syntactic generality: RESTATE (call `Finset.gcd_eq_sum_mul` directly)
Superfluous arguments: NONE (but ring over-specialised)

Overall: RESTATE-BEFORE-SHIP (restated form is already mathlib's)

### Call sites — `Roth.exists_sum_mul_eq_gcd`

Internal use count: 0 outside the declaring file; 1 inside Roth/Separation.lean.
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Separation.lean:446 | `exists_int_eq_of_gcd_eq_one`: `obtain ⟨z, hz⟩ := exists_sum_mul_eq_gcd s u` |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `exists_sum_mul_eq_gcd`?):
  - (none) — grep for `gcd_eq_sum_mul` / `gcd_eq_gcd_ab` over `Roth/` finds only the proof of this theorem.

### Composition check (Phase 6)

Can `Roth.exists_sum_mul_eq_gcd` be derived from mathlib in ≤3 chained calls?

Attempt 1: `by simpa [eq_comm, mul_comm] using Finset.gcd_eq_sum_mul s u`
  - Mathlib decls used: `Finset.gcd_eq_sum_mul`, `eq_comm`, `mul_comm`
  - Result: succeeds (it is the project proof; also for general Bézout `R`, evidence (1))
  - Notes: orientation-only normalisation.

Attempt 2: bypass entirely at the call site with `Finset.gcd_eq_sum_mul s u`
  - Result: succeeds (evidence (2)).

Conclusion: COMPOSABLE (in fact a specialisation of a single mathlib lemma)

## Verdict: `Roth.exists_sum_mul_eq_gcd`

Verdict: NO-mathlib-has-it

**Category:** NO-mathlib-has-it

**Evidence:**
- Literature search (Phase 3): standard n-ary Bézout identity, most generally in Bézout rings.
- Generality analysis (Phase 4): STRICTLY NARROWER (ℤ vs Bézout ring), but the general form is mathlib's (false-positive class 4).
- Mathlib search (Phase 5): found as `Finset.gcd_eq_sum_mul` (Loogle sole hit; grep PrincipalIdealDomain.lean:233).
- Composition check (Phase 6): COMPOSABLE; the project proof is exactly that lemma.

**Rationale:**
`Finset.gcd_eq_sum_mul` states that for any commutative ring `R` with `[IsBezout R] [NormalizedGCDMonoid R]`, every finite family has `s.gcd f = ∑ a ∈ s, f a * g a` for some `g`. ℤ carries both instances (evidence (3)), so the project theorem is its ℤ instance with the equation reversed and the products commuted. The project proof is literally `simpa [eq_comm, mul_comm] using Finset.gcd_eq_sum_mul s u`. The mathlib lemma also already covers the generalisation (any Bézout ring), so nothing should be upstreamed.

WHY not: mathlib has the identical content, in greater generality, as `Finset.gcd_eq_sum_mul`. The project orientation brings no benefit at its single call site.
Belongs-elsewhere check: nowhere; delete it.
Existing mathlib decl:        `Finset.gcd_eq_sum_mul`
Located at:                   `Mathlib/RingTheory/PrincipalIdealDomain.lean:233`
Our form follows in ≤1 line:
```lean
example {ι : Type*} (s : Finset ι) (u : ι → ℤ) : ∃ z : ι → ℤ, ∑ i ∈ s, z i * u i = s.gcd u := by
  simpa [eq_comm, mul_comm] using Finset.gcd_eq_sum_mul s u
```
Call sites in our project (from Phase 6.0): 1
Refactor plan:
- Roth/Separation.lean:446 (`exists_int_eq_of_gcd_eq_one`): replace `obtain ⟨z, hz⟩ := exists_sum_mul_eq_gcd s u` with `obtain ⟨z, hz⟩ := Finset.gcd_eq_sum_mul s u`. Then `hz : 1 = ∑ i ∈ s, u i * z i` after `rw [hu] at hz`. Make three adjustments: use witness `∑ i ∈ s, w i * z i`, start the calc from `((∑ i ∈ s, u i * z i : ℤ) : ℚ) * v` closed by `simp [← hz]`, and finish the summand step with `rw [mul_right_comm, hw i hi]`. The whole revised proof compiles (evidence (2)).
Next action: delete `Roth.exists_sum_mul_eq_gcd` after updating the call site. No mathlib PR.

---

## Next step

No mathlib PR. Inline `Finset.gcd_eq_sum_mul s u` at Separation.lean:446 using the compiled proof in evidence (2), then delete `exists_sum_mul_eq_gcd`.

## Evidence
- Evidence file: `.mathlib-quality/overview/evidence/Roth.exists_sum_mul_eq_gcd/reaim.lean` (imports `Roth.Separation`). One `lake env lean` run (about 32 s) printed only the `#check` output, with no errors.
  - (0) `#check @Roth.exists_sum_mul_eq_gcd` gives the signature.
  - (1) The project statement for an arbitrary `[CommRing R] [IsBezout R] [NormalizedGCDMonoid R]` is proved by the same `simpa ... using Finset.gcd_eq_sum_mul s u`.
  - (2) `exists_int_eq_of_gcd_eq_one` is reproved with `Finset.gcd_eq_sum_mul` directly, in mathlib orientation.
  - (3) `IsBezout ℤ` is found by `inferInstance`.
- Searches: 3 WebSearch queries, recorded above. Loogle `Finset.gcd _ _ = Finset.sum _ _` returned `Finset.gcd_eq_sum_mul` as its only result. Lean-Finder and LeanSearch returned two-element Bézout lemmas. `lean_local_search` was unavailable because ripgrep is missing. A mathlib grep for `gcd_eq_sum`, `exists_sum_mul_eq_gcd`, `span_gcd` and finset-gcd/sum patterns found the lemma and no ℤ-specific duplicate. ChatGPT MCP was n/a (not configured).
