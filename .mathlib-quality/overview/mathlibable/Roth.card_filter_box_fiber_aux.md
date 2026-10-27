---
decl: Roth.card_filter_box_fiber_aux
file: Roth/Lattice.lean
line: 100
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private fibre-counting bijection (box in the first m coordinates filtered by the extended predicate vs. the fibre of box r filtered by p over last coordinate i); the single substantive step of card_filter_box_last, with no Finsupp-level counterpart in mathlib (mathlib's card_snocEquiv_filter_piFinset only handles predicates depending on init).
action: Keep as private helper for its sole use in card_filter_box_last (Roth/Lattice.lean:141); revisit only if a Finsupp.snoc API is added to Mathlib/Data/Finsupp/Fin.lean, in which case the bijection could be rebuilt via Finset.filter_piFinset_eq_map_snocEquiv-style maps.
---

# Roth.card_filter_box_fiber_aux

## Inventory entry

### `theorem Roth.card_filter_box_fiber_aux`
- **Type**: `∀ {m : ℕ} (r : Fin (m + 1) → ℕ) (p : (Fin (m + 1) →₀ ℕ) → Prop) [DecidablePred p] {i : ℕ}, i ≤ r (Fin.last m) → ((box (r ∘ Fin.castSucc)).filter fun d ↦ p (d.mapDomain Fin.castSucc + Finsupp.single (Fin.last m) i)).card = (((box r).filter p).filter fun d ↦ d (Fin.last m) = i).card` (declared `private lemma`).
- **What**: For a box `box r ⊆ Fin (m+1) →₀ ℕ` and any decidable predicate `p`, the fibre of `{d ∈ box r | p d}` over last coordinate `i` (with `i ≤ r_last`) has the same cardinality as the set of `d` in the lower-dimensional box `box (r ∘ castSucc)` whose extension by `i` in the last slot satisfies `p`. Mathematically: the map `d ↦ (d, i)` is a bijection between those two sets.
- **How**: `Finset.card_bij` with the map `d ↦ d.mapDomain Fin.castSucc + Finsupp.single (Fin.last m) i`. Maps-to: `mem_box` plus `Fin.lastCases`, with the last coordinate via `extend_apply_last` and the hypothesis `hi`, the others via `extend_apply_castSucc`. Injectivity: evaluate at `j.castSucc` (`congrArg`) and `extend_apply_castSucc`. Surjectivity: preimage `Finsupp.equivFunOnFinite.symm fun j ↦ d j.castSucc`, with the reconstruction identity `hext` proved by `ext` and `Fin.lastCases` using `extend_apply_last`, `extend_apply_castSucc` and the fibre condition.
- **Hypotheses**: `hi : i ≤ r (Fin.last m)` is genuinely needed (otherwise the right side is empty while the left side need not be, e.g. `p := True`). `[DecidablePred p]` is needed for `Finset.filter`. All used.
- **Uses from project**: `Roth.box`, `Roth.mem_box` (Roth/Box.lean:47, 51), `Roth.extend_apply_castSucc` (Roth/Lattice.lean:92), `Roth.extend_apply_last` (Roth/Lattice.lean:96).
- **Used by**: Roth/Lattice.lean `Roth.card_filter_box_last` only (l.141, in the `Finset.sum_congr` step after `Finset.card_eq_sum_card_fiberwise`). `grep -rn card_filter_box_fiber_aux Roth/` returns only the definition and this use. Transitively feeds `card_filter_weight_le_succ_aux` (l.175) and the lattice-point counting of Roth/Lattice.lean.
- **Visibility**: private
- **Lines**: 100–124, proof length 20 lines (105–124)
- **Notes**: Name ends in `_aux`; would also be caught by the Step 9a pre-filter. The extension `d.mapDomain Fin.castSucc + Finsupp.single (Fin.last m) i` is a hand-rolled "Finsupp.snoc" (see the reports for `Roth.extend_apply_castSucc` / `Roth.extend_apply_last`).

## Junk check (Step 8)
- Used anywhere? Yes, once: the fibre identification in the public `Roth.card_filter_box_last` (l.141).
- Wrapper of 1–2 mathlib calls? No: a 20-line explicit bijection with three proof obligations.
- Does mathlib have it? Not in this form. The closest mathlib results are in `Mathlib/Data/Fin/Tuple/Finset.lean`: `Finset.card_snocEquiv_filter_piFinset` / `Finset.filter_piFinset_eq_map_snocEquiv` (product decomposition of `piFinset` filtered by a predicate of `init r` only) and `Fin.snoc_mem_piFinset_snoc`. These handle predicates depending only on the first `m` coordinates, not a general `p` restricted to a last-coordinate fibre, and they live on plain functions (`piFinset`), whereas `box` is a `Finset (σ →₀ ℕ)` obtained by mapping along `Finsupp.equivFunOnFinite.symm`. There is no Finsupp snoc/init API (`grep -rln "snoc" Mathlib/Data/Finsupp/`: no hits). Transporting to `piFinset` and using `Fin.snocEquiv` would be possible but would not shorten the proof meaningfully, since the general-`p` fibre statement still needs its own bijection.
- Too specific / inline? It could be inlined into `card_filter_box_last` (single use), but that would put a 20-line bijection inside a `Finset.sum_congr` lambda; as a separate lemma it keeps the public statement's proof readable. Keeping it separate is the better style.
- Well-chosen? Yes; the statement is exactly the fibre identity needed, with the minimal hypothesis `hi`.
- Conclusion: `KEEP`. Action: none; if mathlib gains `Finsupp.snoc` (natural home `Mathlib/Data/Finsupp/Fin.lean`), restate the extension through it and simplify the bijection proof.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Lattice.lean:100); additionally the name ends in `_aux`.

Side note: the upstreamable idea, if any, is the public wrapper `Roth.card_filter_box_last` (fibrewise counting of a filtered box over the last coordinate) together with a `Finsupp.snoc` API, assessed separately.

## Evidence
- `grep -rn card_filter_box_fiber_aux Roth/`: definition l.100, sole use l.141 (`card_filter_box_last`).
- `grep -rn "extend_apply_castSucc\|extend_apply_last" Roth/`: used only within this lemma (l.110, 111, 112, 115, 122).
- Read `Mathlib/Data/Fin/Tuple/Finset.lean` in full: `card_snocEquiv_filter_piFinset`, `filter_piFinset_eq_map_snocEquiv`, `snoc_mem_piFinset_snoc` exist but cover only `init`-dependent predicates on `piFinset`, not this fibre statement.
- `grep -rln "Finsupp.*snoc\|snoc.*Finsupp" Mathlib/Data/Finsupp/`: no hits.
- Read `Roth.box` / `Roth.mem_box` (Roth/Box.lean:47–52) to confirm `box` is the `equivFunOnFinite.symm` image of `Fintype.piFinset`.
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening experiments, and the project builds clean, so the lemma compiles as stated.
