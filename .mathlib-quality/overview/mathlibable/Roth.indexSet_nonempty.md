---
decl: Roth.indexSet_nonempty
file: Roth/Theta.lean
line: 80
kind: theorem
visibility: public
verdict: INHERITED-NO-composable-from-mathlib
cost: n/a
junk: KEEP
rationale: One-term glue lemma (anonymous constructor with witness 1 from one_mem_RSet, h = 1, isCoprime_one_left, rfl) giving the csSup nonemptiness side condition for the project-local carrier set indexSet, which is NO-composable-from-mathlib; nothing to upstream.
action: Do not upstream; keep in Roth/Theta.lean as the Nonempty side lemma of indexSet (callers Θ_le_of_forall_index_le at Roth/Theta.lean:127 and Θ_mono at Roth/Theta.lean:136); no call-site changes.
---

# Roth.indexSet_nonempty

## Inventory entry

### `theorem Roth.indexSet_nonempty`
- **Type**: `∀ {σ : Type*} [Fintype σ] {B : ℝ}, 1 ≤ B → ∀ (q r : σ → ℕ), (Roth.indexSet B q r).Nonempty`
- **What**: If `1 ≤ B`, the set of indices `ind(R; h/q; r)` (over `R ∈ ℛ_m(B; r)` and `h` coprime to `q`) whose supremum is `Θ_m(B; q; r)` is nonempty. So the supremum is well-defined in the `csSup` sense.
- **How**: A term proof `⟨_, 1, one_mem_RSet hB r, fun _ ↦ 1, fun _ ↦ isCoprime_one_left, rfl⟩`. The witness polynomial is the constant `1` (`Roth.one_mem_RSet`), and the point is `h = 1`, coprime to every `q j` by mathlib's `isCoprime_one_left`.
- **Hypotheses**: `hB : 1 ≤ B` (needed for `1 ∈ RSet B r`). The section instance `[DecidableEq σ]` is omitted (`omit ... in`). `[Fintype σ]` is inherited from `indexSet`.
- **Uses from project**: `Roth.indexSet`, `Roth.one_mem_RSet` (and through them `Roth.RSet` and `Roth.index`)
- **Used by**: `Roth.Θ_le_of_forall_index_le` (Roth/Theta.lean:127, `csSup_le (indexSet_nonempty hB q r) ?_`), `Roth.Θ_mono` (Roth/Theta.lean:136, `csSup_le_csSup (indexSet_bddAbove B' q) (indexSet_nonempty hB q r) ?_`). No other uses in `Roth/`.
- **Visibility**: public
- **Lines**: 80–81, proof length 1 line
- **Notes**: Source: clean.tex §5 ("This supremum is well-defined"). The paper assumes `B ≥ 1` throughout. Lean makes it a hypothesis here.

## Junk check (Step 8)
- Used anywhere? Yes, twice, as the `Nonempty` side condition of the `csSup` API (`csSup_le`, `csSup_le_csSup`) in `Θ_le_of_forall_index_le` and `Θ_mono`.
- Wrapper of 1–2 mathlib calls? No. It is a one-term membership witness for the project set `indexSet`. Its only mathlib ingredient is `isCoprime_one_left`.
- Does mathlib have it? No. `indexSet` is project-local, and there is no `namespace Roth` under `.lake/packages/mathlib/Mathlib/`.
- Too specific (inline?)? It could be inlined at its two callers, but it is the standard named `Nonempty` companion of a carrier set used with `csSup`, paired with `indexSet_bddAbove`. Inlining would duplicate the witness term in two places and make the callers harder to read.
- Well-chosen? Yes. It mirrors the paper's "this supremum is well-defined".
- Conclusion: `KEEP`. Action: none.

## Mathlibable assessment (Step 9)
Inherited from: Roth.indexSet

Pre-filter: the lemma is public, its name does not end in `_aux`, its docstring is not internal or auxiliary, Step 8 said KEEP, and the qualified name is absent from mathlib (`grep -rln "namespace Roth" .lake/packages/mathlib/Mathlib/` has no hits). No SKIP.

Glue check: the proof is a single anonymous-constructor term that unfolds the existential set-builder of `indexSet` and supplies a witness (`1`, `one_mem_RSet hB r`, `h = 1`, `isCoprime_one_left`, `rfl`). It adds no mathematics beyond the definition and the sibling glue lemma `one_mem_RSet`, which is itself `INHERITED-NO-composable-from-mathlib`. The parent `Roth.indexSet` is `NO-composable-from-mathlib`, not `NO-mathlib-has-it`, so the re-aim rule does not apply. `indexSet` is a proof-internal carrier set of Ridout's/Cassels' `Θ_m`, and it is not going to mathlib. Its nonemptiness lemma has no independent upstream value. The generic facts it uses (`isCoprime_one_left`, `Set.Nonempty`) already exist in mathlib. Verdict: `INHERITED-NO-composable-from-mathlib`. Next step: none. Keep it next to `indexSet` and `indexSet_bddAbove`.

## Evidence
- `grep -rn indexSet_nonempty Roth/`: the definition at Theta.lean:80, with uses at Theta.lean:127 (`Θ_le_of_forall_index_le`) and Theta.lean:136 (`Θ_mono`).
- `grep -rln "namespace Roth" .lake/packages/mathlib/Mathlib/`: no hits.
- I reused the parent reports `.mathlib-quality/overview/mathlibable/Roth.indexSet.md` and `.mathlib-quality/overview/mathlibable/Roth.one_mem_RSet.md`. I wrote no new evidence files and ran no Lean (the project builds clean per the brief).
