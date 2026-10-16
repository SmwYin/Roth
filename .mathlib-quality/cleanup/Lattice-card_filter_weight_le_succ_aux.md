# Phase 4 — `card_filter_weight_le_succ_aux`

Scope: the private successor-step helper in `Roth/Lattice.lean`, its sole headline caller's
positivity argument, and this report. No Git operations or shared progress edits.
I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md in full, both skills, the full Phase-4 worker
prompt, and relevant style/naming sections. Source frozen at SHA256
`be707274cdc77d8e31a73497e8392e8a556f8d13af1e3c190e32ad9c9496a2b3`.

## Result

The fibre induction uses positivity of only the last radius; prefix positivity is encapsulated
by `ih`. Replaced `hr : ∀ j, 0 < r j` with `hr : 0 < r (Fin.last n)` and changed the sole
caller to pass `(hr _)`. This private premise localization was explicitly authorized. Removed
an unnecessary `classical`, packed the signature, and removed two redundant parenthesis pairs
around square-root arguments. No mathematical definition, public type, docstring, header,
import, or version changed. Helper: 33 → 30 declaration lines, 25 → 24 body lines. Headline
remains 14 body lines. No rename, new helper, or public API expansion.

## Full audit (24 items)

1. LINT: final complete native diagnostics: `partial:false`, `success:true`, no target warnings;
   only inherited line-1 copyright warning, explicitly preserved by the user.
2. HAVE SCAN: sole `have hs := sum_inv_lt ...`, no `by`, used by `push_cast ... at hs` and by
   `hs.le` in the final sum bound. Keep; it is transformed then consumed, not a single-use alias.
   `set R := r (Fin.last n)` appears throughout and is retained.
3. SET_OPTION: none in target; no limits, suppression, profiling, or trace settings added.
4. SIMP SQUEEZE: nested `by simp` is terminal; final `simp [R]` terminal. Both unsqueezed.
5. NAMING: mathematical snake_case describes filtered-cardinality successor step; private,
   nonnumbered `_aux`, no forbidden abbreviation or scheme-number pattern. No rename warranted.
6. LINE PACKING: every signature line measured below; first line is 100 codepoints. Packed the
   `ih` binder and filter body; no whole next syntactic unit fits across a remaining break.
7. BY PLACEMENT: `by` always ends its expression line; no isolated `by`.
8. FORMAT: two-space proof indentation, nested calc proofs indented consistently; no empty
   proof lines, semicolon chains, `haveI`/`letI`, or trailing whitespace. Removed unused `classical`.
9. COMMENTS: none in original proof, none removed; file header and public documentation preserved.
10. DOCSTRING: private internal helper needs none; no public documentation changes.
11. VISIBILITY: private, sole in-file caller; no wider visibility appropriate.
12. STRUCTURE: 24 body lines ≤60, no conjunction statement and no case branch; substantive fibre
    decomposition, sum estimate, reciprocal bound, and cancellation remain explicit.
13. MATHLIB: all five searches below; existing `Finset.sum_le_sum`, `sum_congr`, `mul_sum`,
    `Fin.prod_univ_castSucc` already handle the generic steps. No replacement for this specialized
    weighted-box induction step established. No duplicated wrapper or missing generic API justified.
14. JUNK DEF: n/a — lemma; no definitions changed.
15. EXISTS LEMMA: n/a — conclusion is a cardinality inequality, not an existential witness.
16. SHOW vs CHANGE: sole `show 0 ≤ ... by positivity` is a typed term inside `linarith`'s list;
    it is not a tactic changing the goal, so retain.
17. PUSH_NEG: none.
18. GENERALISE: every binder tested or justified below; localized `hr` retained. Failed weak-premise
    probes show this proof needs repair under those premises, not logical necessity of hypotheses.
19. INEQUALITY: no reversed inequality in signature; table below.
20. NORMAL-FORM: real cardinality bound and normalized weight match the source theorem and caller;
    no competing normal form or equivalence API.
21. SYNTAX-GEN: localized positivity makes the private premise match its use. Existing dependent
    prefix-box `ih` remains immediately supplied by induction, with no broader restatement needed.
22. IMPORT-FANOUT: n/a — no imports changed.
23. CASTS: no coercion removed or introduced; nine genuine `ℕ → ℝ` casts and three inner Nat
    ascriptions in the signature remain. The latter fix `n + 1` before casting. Two redundant
    grouping-parenthesis pairs removed. Typed nonnegativity term fixes `linarith`'s real premise.
24. INSTANCE-NAME: n/a — no instance declarations or instance naming.

## Mathlib search-status

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | `cardinality lattice box weighted sum at most m minus lambda over two bounded by two sqrt m divided lambda product` | `cornersTheoremBound`, regularity bounds, `Behrend.sum_sq_le_of_mem_box`; different estimates |
| B Loogle | `Finset.sum_le_sum` | generic finite-sum monotonicity found and already used |
| C LeanSearch | `Cardinality of lattice points in a box with sum of normalized coordinates bounded by dimension minus lambda` | `Behrend.card_box`, three ZLattice covolume limit variants; not this induction step |
| D source rg | full `card_filter_weight_le_succ_aux`, `sum_inv_lt`, `card_filter.*sqrt`, `card_filter.*weight` in Mathlib and project | no Mathlib candidate; specialized project results and sole caller found |
| E local name-pattern | `card_filter_weight` | three project declarations; `index:unavailable`, so do not infer absence from index |

Auxiliary variants: `card_filter_le`, `card_filter_le_iff`, `sum_le_sum`, `card_box`,
`Behrend.sum_sq_le_of_mem_box`, lattice covolume variants. Common-equivalents lookup has no
matching compact/discrete/separation bucket. Native `exact?` failed at the initial proof state;
`apply?` produced partial suggestions, including the opposite parameter range, and stopped at
the default budget. `grind`, `simp`, and `aesop` did not close the full initial goal. These
searches do not prove absence. Keep the substantive helper using the existing generic API;
it is not a 1–3-call wrapper. No new public API has a current caller benefit.

## Generalisation status

All CLI probes used the real source prefix and actual proof in isolated scratch files with
`autoImplicit false`, preventing dropped binders from being silently reintroduced. Evidence:
`/private/tmp/roth-succ-probes.py`, `roth-succ-probes-results.jsonl`, and per-case `.log` files.

| Binder | Class/use | Mechanical probes | Result |
|---|---|---|---|
| `{n : ℕ}` | dimension, Fin domain, sums, sqrt | drop | rejected: unbound dimension; natural finite dimension is construction-specific, no applicable typeclass/universe weakening |
| `r : Fin (n+1) → ℕ` | radius data, boxes, product | drop | rejected: unbound `r`; arbitrary radii already allowed; abstract field/domain restatement has no current benefit |
| original `hr : ∀ j, 0 < r j` | passed only at `Fin.last n` | localize; drop; local `0 ≤ r (Fin.last n)` | localization compiles, kept; drop unbound `hr`; weak premise fails `sum_inv_lt`'s `1 ≤ R` requirement |
| `hn : 0 < n` | successor lower bound, sqrt cancellation | drop; `0 ≤ n` | drop unbound `hn`; weak premise fails `Nat.succ_le_succ` and leaves cancellation goal |
| `{lam : ℝ}` | threshold, denominators | drop | unbound threshold; `Real.sqrt` and existing real count estimates preclude a mechanical parent-type weakening |
| `hlam : 2 * √↑(n+1) < lam` | reciprocal sum estimate | drop; `≤` | drop unbound `hlam`; weak premise fails strict premise of `sum_inv_lt`; no necessity claim |
| `ih : ∀ {t : ℝ}, 0 < t → ...` | prefix estimate for shifted parameters | drop | valid repaired drop probe rejects unknown `ih` at sum estimate; full positive-parameter family used |
| nested `{t : ℝ}` | quantified induction parameter | drop | unbound `t`; moving its domain changes `ih` rather than mechanically weakening the declaration |
| nested `0 < t` | domain of `ih` | polarity inspection | changing to `0 ≤ t` or dropping this premise strengthens the supplied `ih`, so is not a theorem generalisation; no candidate applied |

The first `drop_ih` scratch had a missing colon and was rejected syntactically; it was corrected
and rerun. Only `/private/tmp/roth-succ-drop_ih-fixed.log` supports the verdict. Strict→weak
failures concern this proof; no counterexamples were asserted. The nonnegativity-only `hr`
probe also concerns this proof, not the impossibility of a different proof.

Inversion check: the concrete prefix-box count remains in the finite-sum stage; its fibre
formula and dimension-specific reciprocal estimate are essential. Abstracting arbitrary
counts would merely move current premises with no demonstrated second caller benefit.
Big-change candidates: none. Literature: n/a — private declaration, exempt by scope rule.

## Line packing

Actual `#check @card_filter_weight_le_succ_aux` at `format.width := 100` was compiled in
`/private/tmp/roth-succ-certification.lean`; output is in the corresponding `.log`:

```lean
@card_filter_weight_le_succ_aux : ∀ {n : ℕ} (r : Fin (n + 1) → ℕ),
  0 < r (Fin.last n) →
    0 < n →
      ∀ {lam : ℝ},
        2 * √↑(n + 1) < lam →
          (∀ {t : ℝ},
              0 < t →
                ↑(#({d ∈ box (r ∘ Fin.castSucc) | weight (r ∘ Fin.castSucc) d ≤ (↑n - t) / 2})) ≤
                  2 * √↑n / t * ∏ j, (↑((r ∘ Fin.castSucc) j) + 1)) →
            ↑(#({d ∈ box r | weight r d ≤ (↑(n + 1) - lam) / 2})) ≤ 2 * √↑(n + 1) / lam * ∏ j, (↑(r j) + 1)
```

Each next unit is a whole binder, filter-lambda head, or arithmetic expression through its
relation; breaks preserve those grammatical units rather than splitting applications.

| Sig line | Chars | Next unit (width) | Arithmetic | Action |
|---|---:|---|---|---|
| 160 | 100 | `(hn : 0 < n)` (12) | 100 + 1 + 12 = 113 >100 | ok |
| 161 | 89 | filter-lambda head `(((box (r ∘ Fin.castSucc)).filter fun d ↦` (41) | 89 + 1 + 41 = 131 >100 | ok |
| 162 | 77 | `((n : ℝ) - t) / 2).card : ℝ) ≤` (30) | 77 + 1 + 30 = 108 >100 | ok |
| 163 | 98 | conclusion left side through `≤` (80) | 98 + 1 + 80 = 179 >100 | ok |
| 164 | 84 | complete bound through `:= by` (57) | 84 + 1 + 57 = 142 >100 | ok |
| 165 | 63 | proof follows | n/a | ok |

## Inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 1 | entire signature, including `hr`, `hn`, `hlam`, nested `ih` | n/a — no `≥`/`>` | none | none |

## Golfing-rule pass (42 rules)

| Rule | Status |
|---|---|
| 1.1 by-exact wrapper | n/a — none |
| 1.2 by-rfl wrapper | n/a — none |
| 1.3 rw + exact → rwa | no terminal rw/exact match: sum congruence needs `rw` before constructing its proof |
| 1.4 simp + exact → simpa | n/a — no such chain |
| 1.5 trailing rfl | n/a — none |
| 1.6 constructor pair | n/a — no conjunction/structure construction |
| 1.7 apply + exact | n/a — direct term proof already used |
| 1.8 by_contra! | n/a — no contradiction proof |
| 1.9 eta reduction | sum lambdas depend on index; no reducible eta wrapper |
| 1.10 inline have | `hs` transformed then used, retained; `R` used repeatedly |
| 1.11 refine + fun | existing sum refinement already uses this form |
| 1.12 redundant show | term-valued nonnegativity premise needs its expected type |
| 1.13 obtain projections | n/a — no conjunction-valued have |
| 1.14 merge rw | no consecutive rw calls; intervening cast normalization required |
| 1.15 terminal simp unsqueeze | both existing simp calls already unsqueezed |
| 1.16 nonterminal simp squeeze | n/a — no bare nonterminal simp retained |
| 1.17 dot notation | existing `hs.le`, `.2` used naturally; no improvement |
| 1.18 `<|` | arguments have following arguments or appear in typed premise; no parentheses saving |
| 1.19 push Not | n/a — no push_neg |
| 1.20 trivial existential | n/a — no existential |
| 2.1 whole grind | tried at initial live state; failed counting goal |
| 2.2 delete before grind | no grind retained in proof; native grind after sum expansion closed that local equality but saved no line |
| 2.3 simpa consolidation | standalone sum `simp [Finset.mul_sum, div_eq_mul_inv, mul_assoc, mul_left_comm, mul_comm]` left a sum distributivity goal, rejected |
| 2.4 fun_prop | n/a — no analytic function-property goal |
| 2.5 positivity | already handles nonnegative shifted increment and multiplicative coefficient |
| 2.6 gcongr | native `by gcongr` closes multiplicative comparison, but same line count and loses explicit `hs.le`; existing term retained |
| 2.7 lia / omega | n/a — no integer arithmetic tactic block; successor bound already a direct Nat lemma |
| 2.8 aesop | initial live-state probe failed exhaustive search |
| 2.9 norm_num / norm_cast | symbolic casts feed fibre matching/cancellation; no concrete numeric computation to replace |
| 2.10 decide | n/a — unrestricted real inequalities and symbolic boxes |
| 2.11 field_simp/ring | existing field_simp retained; standalone `field_simp [R]` without final simp leaves product/composition and R-identification goal |
| 2.12 linear_combination | native and complete standalone replacement of inner ring compiled; no clarity/line benefit over ring, retained ring |
| 2.13 wlog | n/a — no symmetric case split |
| 2.14 calc collapse | four substantive links: fibre estimate, factorization, reciprocal bound, product cancellation; not a two-step chain |
| 2.15 `<;>` | n/a — no multiple sibling goals with a shared closing tactic |
| 3.1 erw→rw | n/a — no erw |
| 3.2 legacy fun_prop | n/a — no continuity/measurability |
| 3.3 omega→lia | n/a — neither occurs |
| 3.4 rcases rfl | n/a — no cases |
| 3.5 automation attributes | private single-caller induction helper is not a reusable simp normal form |
| 3.6 simp_all | n/a — no simp_all only |
| 3.7 limits | none; unnecessary `classical` removed after complete successful standalone probe |

Step-back reflection: whole-goal automation and direct lemma search did not replace the
fibre argument. The existing four-link calc follows the mathematical decomposition. Retaining
explicit sum congruence and final simp is clearer than the unsuccessful broad simp alternatives.
No further helper extraction is useful at 24 body lines.

## Verification and diff gates

Baseline supplied by owner: preceding easy-helper full build and separate LeanEval both exit 0
(`roth-lattice-helper-easy-full.log`, `roth-lattice-helper-easy-leaneval.log`, 115.31/45.69s).
This worker's initial localized-premise module build exited 0 (30s); final frozen module build
also exited 0 (26s): actual command `/Users/ramin/.elan/bin/lake build Roth.Lattice`, output
`/private/tmp/roth-succ-final-module.log`. Complete native LSP after final edits has
`partial:false`, `success:true`, `timed_out:false`; only user-preserved line-1 header warning.

* INITIAL exact type independently re-proved, without the cleaned helper in scope:
  `/private/tmp/roth-succ-original_independent.lean`, `lake env lean` exit 0, corresponding `.log`.
  Its source contains the original statement and sum/fibre proof renamed `original_independent`;
  no reference to `card_filter_weight_le_succ_aux` occurs. Earlier dependencies retain their real
  proofs. The specialization of the original global radius premise is justified independently.
* INITIAL exact type recovered from the localized helper: `original_recovered` in
  `/private/tmp/roth-succ-certification.lean`, `lake env lean` exit 0; also emits actual width-100
  `#check` above and standard axioms for the recovery theorem.
* ACTUAL built private helper and public headline checked by environment enumeration plus
  `Lean.collectAxioms`, avoiding guessed numeric private syntax:
  `/private/tmp/roth-succ-built-axioms-final.log`. Both depend only on
  `[propext, Classical.choice, Quot.sound]`. Final native `lean_verify` on the logical private
  name independently returns `trust:standard`, no nonstandard axioms, no source warnings.
* A scratch `#check Roth.card_filter_weight_le_succ_aux` from a different importing module failed
  as expected because the name is private. It was replaced by the same-source width check and
  actual-built environment check; that failure is not reported as successful verification.
* Scope comparison against the worker-start snapshot confirms identical file prefix and suffix
  except the sole caller's `hr` argument; all definition/public-type/doc/header protection holds.
  No source line exceeds 100 codepoints. Comments preserved: none present in target body.
* New identifier verification: none introduced. Existing standard API and project names all
  compile in the final module; removal of `classical` introduces no new declaration reference.
* No sorry, new axiom, limit option, suppression, profiling scaffold, TODO, or FIXME introduced.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | actual final `lake build Roth.Lattice`, exit 0, 26s |
| definition_protected | pass | no def/abbrev edits; outside owned block unchanged |
| theorem_statement_protected | pass | authorized private last-coordinate premise weakening; original exact type independently proved and recovered; public type unchanged |
| structure_gate | pass | 24 body lines, no conjunction or long case branch; headline remains 14 |
| naming_gate | pass | mathematical snake_case, private nonnumbered `_aux`, no forbidden pattern |
| line_packing_gate | pass | all six measured signature rows above justified |
| inequality_orientation_gate | pass | zero reversed inequalities in signature |
| cumulative_no_unintended_breakage | pass at worker scope | sole in-file caller compiles; no other helper caller exists |
| docstring_only_changes | n/a | not docstrings-only mode |

Overall: per-worker gates pass. Full project/separate LeanEval and cumulative final performance
sweep belong to the owner after this explicit freeze; no worker claims those gates from a module
build. Owner revoked source-edit ownership at the frozen hash; report-only work follows.

## Simplify / performance hand-off

Holistic manual simplification review found the premise localization and unnecessary classical
context; both applied and checked. No duplicate mathematical proof skeleton with another current
caller warranted extraction. Built-in `/simplify` is not exposed as a callable skill in this
runtime; this report records the actual manual review rather than inventing a tool invocation.
No optional local profiling was run: the owner's final actual all-declaration sweep is mandatory
and runs on the frozen file. No limit raises or performance-suppression changes.

## Required worker checklist

- [✓] Step 1 — all required references read.
- [✓] Step 2 — all 24 audit items reported.
- [✓] Step 2.5 — all five Mathlib search methods actually attempted and documented.
- [✓] Step 2.6 — every binder mechanically probed or inapplicable candidate justified.
- [✓] Step 2.7 — width-100 reference and six-line arithmetic packing table.
- [✓] Step 2.8 — inequality scan table.
- [✓] Step 3 — all 42 golfing rules given concrete status.
- [✓] Step 4 — whole-proof alternatives and decomposition reconsidered.
- [✓] Step 5a — complete native LSP, no target warnings/errors, preserved header warning only.
- [✓] Step 5b — diff gates and actual module build recorded.
- [✓] Step 6a — rename queue: none needed, none appended.

Refactoring needed: none. Renames queued: none. Audit findings resolved: private premise scope,
signature packing, unused classical context, redundant parentheses. No original project tally
increment is requested for this fresh private helper.

Owner checkpoint: explicit source edit revocation before sequential full/separate LeanEval session96137; both exit0(144.68s/36.29s), frozen hash stable. Logs `/private/tmp/roth-lattice-helper-succ-{full,leaneval}.log`. Original264 tally unchanged.
