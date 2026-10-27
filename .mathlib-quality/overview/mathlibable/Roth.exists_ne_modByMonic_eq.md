---
decl: Roth.exists_ne_modByMonic_eq
file: Roth/MainLemma.lean
line: 359
kind: theorem
visibility: public
verdict: BORDERLINE-needs-human
cost: n/a
junk: KEEP
rationale: Pigeonhole step of Lemma 9 (two distinct box polynomials with equal monic remainders of all selected diagonal Hasse derivatives); a 15-line application of Fintype.exists_ne_map_eq_of_card_lt plus ncard_boxFamily and sum_modByMonic_coeff; the Hasse/diag/box content is incidental (abstract form over any finite pigeon set compiles and implies it in 3 lines) but even the abstract form has no literature standing and mathlib precedent (SiegelsLemma, AdmissibleCardPowDegree) keeps such pigeonhole applications inline or local.
action: Keep in Roth/MainLemma.lean (single caller, private exists_mem_RSet_le_index_aux at l.557); optionally restate it as the compiled abstract corollary of exists_ne_forall_modByMonic_eq (evidence/abstract.lean) or make it private; no mathlib PR.
---

# Roth.exists_ne_modByMonic_eq

## Inventory entry

### `theorem Roth.exists_ne_modByMonic_eq`
- **Type**: `∀ {σ : Type u_1} (r : σ → ℕ) [Finite ↑(Function.support r)] (B : ℕ) {f : ℤ[X]}, f.Monic → ∀ (J : Finset (σ →₀ ℕ)) (C : ℕ), (∀ W ∈ boxFamily r B, ∀ j ∈ J, ∀ i < f.natDegree, |(diag (hasseDeriv j W) %ₘ f).coeff i| ≤ ↑C) → ↑(2 * C + 1) ^ (f.natDegree * J.card) < (↑B + 1) ^ ∏ᶠ j, (r j + 1) → ∃ W' ∈ boxFamily r B, ∃ W'' ∈ boxFamily r B, W' ≠ W'' ∧ ∀ j ∈ J, diag (hasseDeriv j W') %ₘ f = diag (hasseDeriv j W'') %ₘ f`
- **What**: If every member `W` of the box family `𝒲` (degree box `r`, coefficients in `[0, B]`) has all diagonal Hasse remainders `Δ_j W(x,…,x) mod f`, `j ∈ J`, with low coefficients bounded by `C`, and `(2C+1)^{deg f · |J|} < (B+1)^{∏(r_j+1)} = |𝒲|`, then two distinct `W', W'' ∈ 𝒲` have identical remainders for every `j ∈ J`.
- **How**: Builds a `Fintype` on `boxFamily r B` from `boxFamily_finite`, maps each `W` to its coefficient tuple `F W : J × Fin (deg f) → Icc (-C) C`, applies `Fintype.exists_ne_map_eq_of_card_lt` (the cardinality inequality from `hcount` via `Fintype.card_fun`, `Int.card_Icc`, `Set.fintypeCard_eq_ncard`, `ncard_boxFamily`), then recovers equality of remainders from equality of their low coefficients via `Polynomial.sum_modByMonic_coeff hf`.
- **Hypotheses**: `[Finite (Function.support r)]` (needed for `boxFamily_finite`/`ncard_boxFamily`); `hf : f.Monic` (needed: without it `%ₘ` is the identity and bounding coefficients below `natDegree f` does not determine the polynomial; e.g. one variable, `r = 1`, `B = 1`, `f = 2X`, `J = {0}`, `C = 1` satisfies `hC` and `3 < 4`, but the four `W` have distinct remainders); `hC`; `hcount`.
- **Uses from project**: `Roth.boxFamily`, `Roth.boxFamily_finite`, `Roth.ncard_boxFamily`, `Roth.diag`, `MvPolynomial.hasseDeriv`
- **Used by**: Roth/MainLemma.lean:557 (private `exists_mem_RSet_le_index_aux`); listed in the module docstring l.43. No other uses in `Roth/`.
- **Visibility**: public
- **Lines**: 350–378 (docstring 350–358, statement 359–364, proof 365–378, proof length 14 lines)
- **Notes**: Source clean.tex §6 l.1501–1504 and the `\lean{}` note l.1514–1520 (finite pigeonhole on the coefficient arrays). Siblings: `Roth.pigeonhole_count` (BORDERLINE), `Roth.ncard_boxFamily` (YES-but-generalise-first), `Roth.boxFamily` (NO-composable).

## Junk check (Step 8)
- **Used anywhere?** Yes, once (l.557).
- **Wrapper of 1–2 mathlib calls?** No: it combines `Fintype.exists_ne_map_eq_of_card_lt`, a cardinality computation (incl. project `ncard_boxFamily`), and remainder reconstruction from coefficients.
- **Does mathlib have it?** No. Closest: `Polynomial.exists_eq_polynomial` (Mathlib/NumberTheory/ClassNumber/AdmissibleCardPowDegree.lean:36), a pigeonhole on polynomials of degree `< deg b` over a *finite* semiring; `Int.Matrix.exists_ne_zero_int_vec_norm_le` (Siegel) does its pigeonhole inline.
- **Too specific?** Statement is Roth-specific (box family, diag, Hasse derivatives), but it isolates exactly the source's pigeonhole sentence; inlining into the caller would lengthen it. Could be `private`.
- **Well-chosen?** Mostly; the abstract version (any finite set of pigeons, any family of integer polynomials) is cleaner and compiles (evidence).
- Conclusion: `KEEP`. Action: keep; optionally restate as a corollary of the abstract form.

## Mathlibable assessment (Step 9)

Pre-filter: not private; no `_aux`; docstring not internal/auxiliary; Step 8 KEEP; `grep -rn exists_ne_modByMonic_eq .lake/packages/mathlib/Mathlib` empty. Real 14-line proof, not glue; INHERITED does not apply. Full run follows.

### Baseline (Phase 0)
- lake build:               ✓ clean (project built per brief; evidence file importing `Roth.MainLemma` compiles with no output)
- decl `Roth.exists_ne_modByMonic_eq`: ✓ resolved at Roth/MainLemma.lean:359
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Roth's main lemma (Lemma 9): auxiliary polynomial via a pigeonhole/box argument with explicit coefficient bounds.

### Statement (Phase 1)

`Roth.exists_ne_modByMonic_eq` is a theorem stating the following. Let `𝒲` be the set of integer polynomials in variables `σ` (finitely many of which have `r_j > 0`) with `deg_{x_j} W ≤ r_j` and coefficients in `[0, B]`, so `|𝒲| = (B+1)^N`, `N = ∏(r_j+1)`. Let `f ∈ ℤ[x]` be monic of degree `n`, `J` a finite set of multi-indices, and suppose for all `W ∈ 𝒲`, `j ∈ J` the remainder of `Δ_j W(x,…,x)` modulo `f` has all coefficients in `[-C, C]`. If `(2C+1)^{n|J|} < (B+1)^N`, then there are `W' ≠ W''` in `𝒲` with `Δ_j W'(x,…,x) ≡ Δ_j W''(x,…,x) (mod f)` for every `j ∈ J`.

Variables (Lean side):
- `σ`, `r : σ → ℕ` — variables and degree box; `B : ℕ` — coefficient bound.
- `f : ℤ[X]` — modulus (the minimal polynomial of `α`); `J` — selected derivative multi-indices; `C` — remainder coefficient bound.

Hypotheses (Lean side):
- `[Finite (Function.support r)]` — finiteness of the box.
- `hf : f.Monic`.
- `hC` — remainder coefficient bound below `f.natDegree`.
- `hcount` — pigeon count exceeds hole count (supplied via `pigeonhole_count`).

Conclusion (math): two distinct box polynomials share all selected diagonal Hasse remainders mod `f`.

Conclusion (Lean): `∃ W' ∈ boxFamily r B, ∃ W'' ∈ boxFamily r B, W' ≠ W'' ∧ ∀ j ∈ J, diag (hasseDeriv j W') %ₘ f = diag (hasseDeriv j W'') %ₘ f`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: the pigeonhole sentence inside the proof of Lemma 9; listed under "Main results" only as part of "the pigeonhole step", not a named theorem or structure.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 14
One-liner verdict: n/a (kind is theorem)

Conclusion: MULTI-LINE

### Literature search table

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth theorem auxiliary polynomial pigeonhole remainders modulo minimal polynomial Hasse derivatives divisible | partial | Roth expositions (arXiv 2502.00731, math.uh.edu roth.pdf, Waldschmidt arXiv 0908.4024) get the auxiliary polynomial from Siegel's lemma / box principle | none states the remainder-mod-f pigeonhole as a lemma |
| 2 | WebSearch (general form) | pigeonhole principle polynomials remainder modulo monic polynomial bounded coefficients two distinct congruent | partial | arXiv 1609.01361 Claim A.4 uses the same pattern (reduce a bounded-coefficient family mod Q, collide remainders) inline | no standalone/standard statement |
| 3 | WebSearch (aliases) | Thue-Siegel lemma Dirichlet box principle auxiliary polynomial vanishing at algebraic number difference of two polynomials | yes | Thue–Siegel lemma: box principle on integer vectors, `(2NH+1)^N` count (arXiv 2303.02037, Wikipedia "Siegel's lemma") | the collision step is a proof step, never a separate result |
| 4 | ChatGPT MCP | n/a | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for `pigeonhole` | yes | l.1501–1504 "By the pigeonhole principle, there are two distinct polynomials W', W'' ∈ 𝒲 ..."; `\lean{}` note l.1514–1520 (finite pigeonhole on coefficient arrays) | source of the statement |
| 6 | nLab | pigeonhole principle | no | generic pigeonhole only | no entry for Diophantine box arguments |
| 7 | nCatLab | n/a | n/a | — | not a categorical concept |
| 8 | Stacks Project | n/a | n/a | — | not algebraic geometry |
| 9 | MathOverflow / Math.SE | (covered by #2, #3) | no | — | routine pigeonhole bookkeeping not discussed as a result |
| 10 | recent arXiv (last 5 years) | arXiv 2502.00731 (2025), arXiv 2303.02037 (2023) | partial | each does its own inline box/collision step | no common named form |

### Literature summary (Phase 3)

Concept identified as: the Dirichlet box principle / pigeonhole collision step in the Thue–Siegel–Roth auxiliary polynomial construction ("two distinct pigeons land in the same remainder tuple, so their difference is divisible by `f`").
Sources agree on the standard form: no standalone form exists; every exposition applies pigeonhole inline.
Most general standard form: the pigeonhole principle itself (in mathlib as `Fintype.exists_ne_map_eq_of_card_lt`, `Finset.exists_ne_map_eq_of_card_lt_of_maps_to`, `Set.exists_ne_map_eq_of_ncard_lt_of_maps_to`). The intermediate abstraction "a finite family of more than `(2C+1)^{n|J|}` pigeons, each giving `|J|` integer polynomials with remainders mod a monic `f` of degree `n` bounded by `C`, has a collision" is natural but not stated in the literature.
Generality dimensions where the literature varies: pigeon set (box family vs. integer vectors), the map (linear forms vs. remainders), constants.
Disagreement with the literature: none.

### Generality analysis — `Roth.exists_ne_modByMonic_eq`

Literature-standard form (from Phase 3): none beyond pigeonhole; abstract form `exists_ne_forall_modByMonic_eq` (any finite set `s` of pigeons, any `g : ι → α → ℤ[X]`).

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|------------------------|-------------------|--------------------------|---------------------|---------------------------------|
| 1 | pigeon set `boxFamily r B` | the box family | any finite set | yes (abstraction, not weakening) | proof uses only finiteness and `ncard`; abstract form compiled (evidence) |
| 2 | map `W ↦ diag (hasseDeriv j W)` | Roth-specific | any `g : ι → α → ℤ[X]` | yes (abstraction) | proof never uses Hasse/diag structure; compiled |
| 3 | `hf : f.Monic` | monic | monic | no | needed for `sum_modByMonic_coeff`; counterexample `f = 2X` (see Inventory) |
| 4 | coefficient ring `ℤ` | ℤ | ordered ring with finite intervals | marginal | would need `LocallyFiniteOrder` + `abs`; only ℤ is used anywhere; not attempted |
| 5 | `[Finite (Function.support r)]` | finite support | finite box | no | needed for finiteness of `𝒲` |
| 6 | `hC`, `hcount` | as stated | as stated | no | the pigeonhole hypotheses themselves |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL as a hypothesis set (no hypothesis can be dropped), but concrete-via-abstract (Phase 4c Q8): the Roth-specific objects are incidental.
Number of weakening opportunities found: 0 hypothesis drops; 1 abstraction (rows 1–2), verified to compile in evidence/Roth.exists_ne_modByMonic_eq/abstract.lean, with the project lemma re-derived from it in 3 lines.
Proposed restatement: `exists_ne_forall_modByMonic_eq {α ι} {s : Set α} (hs : s.Finite) {f : ℤ[X]} (hf : f.Monic) (J : Finset ι) (g : ι → α → ℤ[X]) (C : ℕ) (hC : ∀ a ∈ s, ∀ j ∈ J, ∀ i < f.natDegree, |(g j a %ₘ f).coeff i| ≤ C) (hcount : (2*C+1)^(f.natDegree * J.card) < s.ncard) : ∃ a ∈ s, ∃ b ∈ s, a ≠ b ∧ ∀ j ∈ J, g j a %ₘ f = g j b %ₘ f`.
Cost of restatement: CHEAP (done in evidence; proof is the original proof minus `ncard_boxFamily`).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|----------|----------|------------------------|----------------------------------|
| 1 | preambles to typeclasses? | no | — | — |
| 2 | sequences to filters? | no | finite combinatorics | — |
| 3 | construction vs universal property? | no | — | — |
| 4 | bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | no | ℤ needed for interval counting | — |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | no | — | — |
| 8 | concrete-via-abstract? | yes | after the `let F ...` the proof never mentions Hasse derivatives or diag; `boxFamily` appears only through `boxFamily_finite` and `ncard_boxFamily`. Abstract form above | none in mathlib beyond the project; it is pigeonhole with a remainder map |
| 9 | false-generalisation guard | no false generalisation | the abstract form specialises back exactly (compiled `example`) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes (abstraction of the witness), but it is not a mathlib-level improvement.
- Proposed restatement: `exists_ne_forall_modByMonic_eq` (Phase 4b).
- Cost: CHEAP.
- Mathlib downstream: none identified; mathlib's own analogous steps (`Int.Matrix.exists_ne_zero_int_vec_norm_le`, `Polynomial.exists_eq_polynomial`) are stated differently (finite coefficient ring / linear maps) and would not reuse it.
- Real improvement: cleaner project lemma decoupled from Hasse/diag; useful locally, not a mathlib gap.

### Proof strategy — `Roth.exists_ne_modByMonic_eq`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|----------|----------|------------------------|----------------|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | could phrase equality of remainders via `modByMonic_eq_of_dvd_sub`, no gain | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | partly | a lemma "two polynomials of degree < n with equal coefficients below n are equal" is used via `sum_modByMonic_coeff`; `Polynomial.ext` + `coeff_eq_zero_of_natDegree_lt` would also do; alternatively `Set.exists_ne_map_eq_of_ncard_lt_of_maps_to` into `boxPoly`-style sets (`Polynomial.ncard_boxPoly`) | CHEAP, no gain |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC. Direct `Fintype.exists_ne_map_eq_of_card_lt` on coefficient tuples, as suggested by the source's `\lean{}` note.

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem

### Mathlib search-status: `Roth.exists_ne_modByMonic_eq`

- [A] Lean-Finder: "pigeonhole: two distinct elements ... same remainders modulo a monic polynomial ... bounded coefficients" → `Polynomial.exists_eq_polynomial`, `Polynomial.exists_approx_polynomial(_aux)`, `Polynomial.exists_partition_polynomial(_aux)` (all AdmissibleCardPowDegree, finite coefficient ring); not our form.
- [B] Loogle: `∃ a ∈ _, ∃ b ∈ _, a ≠ b ∧ _ %ₘ _ = _ %ₘ _` → no hits.
- [C] LeanSearch: "exists two distinct polynomials with equal modByMonic remainder pigeonhole bounded coefficients" → `Polynomial.modByMonic`, `Polynomial.exists_eq_polynomial`, `Polynomial.modByMonic_eq_of_dvd_sub`, `Polynomial.div_modByMonic_unique`; not our form.
- [D] Grep mathlib: `exists_ne_modByMonic_eq`, `exists_ne_forall_modByMonic` → none; pigeonhole family found: `Fintype.exists_ne_map_eq_of_card_lt` (Data/Fintype/Pigeonhole.lean:46), `Finset.exists_ne_map_eq_of_card_lt_of_maps_to` (Data/Finset/Card.lean:470), `Set.exists_ne_map_eq_of_ncard_lt_of_maps_to` (Data/Set/Card.lean:937), `Set.exists_ne_map_eq_of_encard_lt_of_maps_to` (l.585); `Polynomial.sum_modByMonic_coeff` (Algebra/Polynomial/Div.lean:442); `Polynomial.boxPoly`/`ncard_boxPoly` (NumberTheory/MahlerMeasure.lean:55–57). SiegelsLemma.lean:160 applies `exists_ne_map_eq_of_card_lt_of_maps_to` inline.
- [E] Name pattern: project-only.

Searched for both the current form and the abstract form. Concluded: found building blocks (`Fintype.exists_ne_map_eq_of_card_lt`, `Polynomial.sum_modByMonic_coeff`, `Int.card_Icc`, `Fintype.card_fun`); not in mathlib.

### Normal-form check — `Roth.exists_ne_modByMonic_eq`

Equivalent formalisms: (a) equal remainders `%ₘ f`; (b) `f ∣ Δ_j W' − Δ_j W''` (the source's phrasing); (c) `W' − W''` with vanishing remainders. Mathlib has no canonical form; (a) ↔ (b) is `Polynomial.modByMonic_eq_of_dvd_sub`/`dvd_sub_of_modByMonic_eq`-style. The caller consumes (a) via `eval_hasseDeriv_sub_eq_zero`.
RHS convention respected? n/a.

### Syntactic generality — `Roth.exists_ne_modByMonic_eq`

Alternative restatements attempted: abstract pigeon set/map (compiled); `hcount` in ℕ instead of ℝ.
Chosen restatement: current for the project (ℝ `hcount` matches `pigeonhole_count`'s output); abstract form is the better standalone statement.
Justification: the caller (l.557) supplies `hcount` from the real-valued `pigeonhole_count`.

### Superfluous-argument audit — `Roth.exists_ne_modByMonic_eq`

| # | Argument | Essentially used? | Notes |
|---|----------|-------------------|-------|
| 1 | `[Finite (Function.support r)]` | yes | finiteness of `𝒲` |
| 2 | `hf` | yes | counterexample `f = 2X` (Inventory) |
| 3 | `hC` | yes | defines the hole set |
| 4 | `hcount` | yes | pigeonhole inequality |

### Statement-shape verdict (Phase 5.5)

- Normal form: OK
- Syntactic generality: OK for the project (abstract form optional)
- Superfluous arguments: NONE

Overall: SHIP-AS-STATED (as a project lemma)

### Call sites — `Roth.exists_ne_modByMonic_eq`

Internal use count: 0 outside the declaring file; 1 inside it.
External-to-file callers: 0 distinct files.

| Caller file:line | Usage pattern (one-line excerpt) |
|------------------|----------------------------------|
| Roth/MainLemma.lean:557 (private `exists_mem_RSet_le_index_aux`) | `obtain ⟨W', hW', W'', hW'', hne, hWeq⟩ := exists_ne_modByMonic_eq r B hf J C hC (by simpa [finprod_eq_prod_of_fintype] using hcount)` |

Inline-derivation grep: none (the only other `exists_ne_map_eq_of_card_lt` in `Roth/` is inside this proof, l.370).

### Composition check (Phase 6)

Can `Roth.exists_ne_modByMonic_eq` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Set.exists_ne_map_eq_of_ncard_lt_of_maps_to` with `f := W ↦ (j ↦ diag (hasseDeriv j W) %ₘ f)` into `Set.pi J (fun _ ↦ boxPoly-like set)`.
- Mathlib decls used: `Set.exists_ne_map_eq_of_ncard_lt_of_maps_to`, `Polynomial.ncard_boxPoly`, a `Set.ncard_pi`-type count.
- Result: partial — needs `natDegree (g %ₘ f) < natDegree f` (`natDegree_modByMonic_lt`), the box count with `natDegree ≤ n-1` indexing, the pi-set ncard, and project `ncard_boxFamily`; a real proof.

Attempt 2: current route `Fintype.exists_ne_map_eq_of_card_lt` + card simp set + `sum_modByMonic_coeff`.
- Result: 14 lines with a heavy `simpa` cardinality computation; not a ≤3-call composition.

Conclusion: NOT-COMPOSABLE

### Verdict: `Roth.exists_ne_modByMonic_eq`

**Category:** BORDERLINE-needs-human

**Evidence:**
- Literature search (Phase 3): only as an inline pigeonhole step (clean.tex l.1501; Thue–Siegel expositions; arXiv 1609.01361 Claim A.4).
- Generality analysis (Phase 4): no droppable hypothesis; the Roth objects are incidental, abstract form compiled and implies the lemma.
- Mathlib search (Phase 5): building blocks only (pigeonhole family, `sum_modByMonic_coeff`); analogous mathlib steps are inline (SiegelsLemma l.160) or for finite coefficient rings (`Polynomial.exists_eq_polynomial`).
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

The NO buckets do not fit: mathlib has no such statement, and deriving it needs the pigeonhole lemma plus a nontrivial cardinality computation and a remainder-reconstruction step. YES-add-as-is does not fit either: as stated it is wired to Roth-specific objects (`boxFamily`, `diag`, Hasse derivatives). Its abstract core `exists_ne_forall_modByMonic_eq` (compiled) is a clean "pigeonhole on bounded monic remainders over ℤ", but it has no literature standing as a result, names no mathlib gap (no TODO, no recurring manual reformulation), and mathlib's own Siegel lemma and class-number pigeonholes are stated in their own shapes and would not reuse it. So upstreaming even the abstract form is a taste call, not something the evidence decides.

Consistent with the sibling `Roth.pigeonhole_count` (BORDERLINE, keep local). Practical recommendation: keep project-local.

Numbered questions:
1. Keep `Roth.exists_ne_modByMonic_eq` project-local and do not upstream it? (Recommended: yes.)
2. Restate it locally as the 3-line corollary of the abstract `exists_ne_forall_modByMonic_eq` (evidence/Roth.exists_ne_modByMonic_eq/abstract.lean), so the pigeonhole is decoupled from Hasse/diag? (Recommended: optional.)
3. Make it `private`, given its only caller (l.557) is private, though it is listed under "Main results" (l.43)? (Recommended: optional, decide together with `pigeonhole_count`.)

Next action: user answers the questions; default is no change.

---

### Next step

Keep `Roth.exists_ne_modByMonic_eq` in Roth/MainLemma.lean (caller l.557); optionally restate via the abstract form or make private. Do not upstream.

## Evidence
- `.mathlib-quality/overview/evidence/Roth.exists_ne_modByMonic_eq/abstract.lean` (imports `Roth.MainLemma`): `lake env lean` compiled clean with no output (43 s). Contains the abstract `exists_ne_forall_modByMonic_eq` (any finite pigeon set `s`, any `g : ι → α → ℤ[X]`) and an `example` re-deriving the exact project statement from it via `boxFamily_finite` and `ncard_boxFamily` in 3 lines.
- `hf` necessity: argued by explicit counterexample (`f = 2X`, one variable, `r = 1`, `B = C = 1`, `J = {0}`), not compiled.
- Mathlib greps: declaration names (no hits); pigeonhole family and `sum_modByMonic_coeff`, `boxPoly`, SiegelsLemma l.160 located (Phase 5 [D]).
- LeanFinder (1), LeanSearch (1), Loogle (1, no hits); WebSearch 3 queries; ChatGPT MCP n/a (not configured); local reference clean.tex l.1495–1520.
- Project grep: l.43 (docstring), l.359 (decl), l.557 (only use).
