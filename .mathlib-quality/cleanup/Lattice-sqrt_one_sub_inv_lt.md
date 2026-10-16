# Phase 4: `Roth.sqrt_one_sub_inv_lt`

Scope: only this declaration plus owner-authorized import-group blank line. Original public type and documentation preserved. No Git mutations, shared logs, pinned-version changes, sorry, new axioms, or resource-limit changes.

Read in full: `golfing-rules.md`, `proof-patterns.md`, `mathlib-search.md`, `generalisation-patterns.md`, `cleanup-gates.md`, both SKILL.md files, and cleanup Phase 4 worker prompt. Relevant style/naming sections read. Baseline full build/complete diagnostics supplied by owner. Header warning is inherited and expressly retained.

## Result

Original declaration: 11 lines (L22–32), 10 proof-body lines counting the `:= by` line; after: 10 declaration lines (L23–32), 9 proof-body lines under that same convention (8 tactic lines after `:= by`). Saved 1 line, removed two named local facts and an explicit typed positivity subproof. Initial dispatch's “seven haves/10 body lines” count does not match the actual source: five top-level haves were present (`hm'`, `h0`, `hsq`, `hu`, `htm`).

Changes: inline `h0` into `hsq`; use `Nat.cast_nonneg` in `Real.sq_sqrt`; inline `htm` into positivity argument of `Real.sqrt_lt'`; insert blank line between Mathlib/project imports. Keep the mathematical decomposition: square the λ hypothesis, reverse reciprocal inequality, square the target using positivity.

## Full audit (24 items)

1. LINT: complete native diagnostics reports zero target errors/warnings; only inherited L1 header warning, unchanged by user decision.
2. HAVE SCAN: original `hm'` has `by`, keep (cast fact used by positivity and reciprocal bound); `h0 := Real.sqrt_nonneg ...` no `by`, one arithmetic consumer (`hsq`), INLINE; `hsq` has `by`, keep (strict denominator comparison); `hu` has `by`, keep (feeds RHS positivity and terminal arithmetic); `htm := one_div_le_one_div_of_le ...` no `by`, one consumer (RHS positivity), INLINE. Final three haves all contain proof content.
3. SET_OPTION: none.
4. SIMP SQUEEZE: no simp calls in original or final proof.
5. NAMING: `sqrt_one_sub_inv_lt` is snake_case describing the square-root comparison; no forbidden abbreviation, scheme number, numeric aux, single-letter public name, `_ge_` or `_gt_`; no rename needed.
6. LINE PACKING: measured complete signature table below; no repack needed.
7. BY PLACEMENT: all `by` tokens end preceding lines.
8. FORMAT: two-space tactics/four-space nested tactics; one tactic per line; no empty body lines, trailing spaces, haveI/letI or mergeable consecutive rewrites.
9. COMMENTS: no proof comments present; entire declaration docstring retained byte-for-byte.
10. DOCSTRING: existing application condition and precise source preserved under explicit source/doc contract; no rewrite.
11. VISIBILITY: one in-file consumer (`sum_inv_lt`), no external use found by project-wide rg. Public status preserved as requested; making it private would be public API churn with no current benefit.
12. STRUCTURE: final body 9 lines counting `:= by`, no conjunction or branch; no extraction needed.
13. MATHLIB: five actual methods below; build on partial match `Real.sqrt_lt'`, not an established exact duplicate.
14. JUNK DEF: n/a, theorem.
15. EXISTS LEMMA: n/a, conclusion is strict real inequality.
16. SHOW/CHANGE: n/a, neither occurs.
17. PUSH_NEG: n/a, none.
18. GENERALISE: mechanical probes and public literature below; preserve original statement. Compiled `hm : 1 ≤ m` proposal separately reported to owner.
19. INEQUALITY: all code inequalities already ≤/<; table below.
20. NORMAL-FORM: real sqrt and inverse square are native mathlib operations. `inv_pow`/`one_div` converts denominator arithmetic locally; no equivalence API needed.
21. SYNTAX-GEN: existing implicit `m`/`lam` and explicit bounds align with the sole caller; no practical application advantage from restating conclusion.
22. IMPORT-FANOUT: n/a, no imports added/removed; only group whitespace.
23. CASTS: removed one load-bearing-looking but unnecessary typed subproof by using `Nat.cast_nonneg`; in changed lines `(m : ℝ)` occurrences are genuine ℕ→ℝ coercions and retained. No redundant same-type cast introduced.
24. INSTANCE-NAME: n/a, no instance declaration.

## Mathlib search-status

A. Lean-Finder actual native query `sqrt (1 - 1 / m) < 1 - 1 / lam ^ 2 when 2 * sqrt m < lam`: returned partial `Real.sqrt_one_add_le`, plus unrelated rational-root/Liouville results; no matching full bound.
B. Loogle actual query `Real.sqrt (?a - ?b) < ?c`: successful response, empty items.
C. LeanSearch actual query `square root of one minus reciprocal bounded by one minus inverse square`: returned `Real.sqrt_one_add_le`, `Real.sqrt_le_one`, `Real.sqrt_inv`, `Real.le_sqrt_of_sq_le`; these are building blocks, not the full estimate.
D. rg actual source searches for `sqrt_one_sub`, `sqrt_lt'`, `one_div_lt_one_div_of_lt`, `sqrt_lt_one`, `sqrt_one_add_le`, `sq_sqrt` in relevant Sqrt and field files: found reciprocal monotonicity in `Algebra/Order/Field/Basic.lean:72`, and `Real.sqrt_lt'` at `Analysis/Real/Sqrt.lean:235`, `sqrt_one_add_le` at :440. No untruncated full-name match for the target in the searched sqrt sources. No global absence claim made.
E. Native `lean_local_search sqrt_lt` returned 20 named variants, including `Real.sqrt_lt'`, `sqrt_lt_sqrt`, `sqrt_lt_sqrt_iff`, `sqrt_lt_self_iff`; index warming means the search is presence evidence only.

Auxiliary variants inspected: `sqrt_lt`, `sqrt_lt'`, `sqrt_lt_sqrt_iff`, `sqrt_one_add_le`, reciprocal comparison. Common-equivalents table has no matching discrete/finiteness/bornology bucket. Native `exact?` at the original goal failed to close it; `apply?` suggested `Real.sqrt_lt'` with the two expected positivity/squared-inequality subgoals. No exact replacement or 1–3-call wrapper established; retain this arithmetic estimate. No definition/typeclass predicate involved; no API-extraction signal from wrappers, coercion round-trips, or manual typeclass plumbing.

## Generalisation status

| Parameter | Class/use | Mechanical probe | Actual result |
|---|---|---|---|
| `{m : ℕ}` | value, denominator and sqrt | drop n/a: occurs in conclusion; real-valued generalization would restate API and require revised sqrt domain | concrete Nat→Real boundary retained; no abstract-only named object to invert |
| `(hm : 2 ≤ m)` | proposition, cast and reciprocal bound | drop; weaken 2→1 | independent native run_code drop failed `Unknown identifier hm`; 1≤m variant compiled success true/no diagnostics |
| `{lam : ℝ}` | value, inverse and comparison | drop n/a: occurs in conclusion and bound; general field lacks `Real.sqrt` | retain real domain |
| `(hlam : 2 * √(m : ℝ) < lam)` | proposition, squared lower bound | drop; strict→weak | drop failed at hsq (`linarith failed`); weak variant first failed terminal nlinarith, succeeds after explicit positive reciprocal hint; no source API change |

The weak-λ probe had already run when owner requested no further API variants; it is audit evidence only. The concrete proposal the owner requested is exclusively the useful/simple hm1 variant, saved with exact compiled code and caller audit in `Lattice-api-proposal.md`. No weakening applied. Failed drop/replacement probes show failure of this proof attempt, not logical necessity of the hypotheses. Owner has closed hm1 as a compiled unnecessary proposal with no current caller benefit; no pending approval or refactoring action remains. No typeclass/universe/global-point hypotheses exist. Inversion check: n/a, no special named concrete witness is unfolded; `Real.sqrt` remains essential throughout.

Public literature searches actually performed: `Takloo Bighash Yin Formalizing Roth theorem lattice count estimate lambda square root` and `square root inequality sqrt 1-x less than 1-x/2 concavity generalization`. First query's top visible hits were squaring-condition PlanetMath, an unrelated square-root MSE problem, and author's Pythagorean page: no usable canonical generalization. Second query surfaced concavity-based treatments: MIT thesis (`https://math.mit.edu/~urschel/publications/thesis.pdf`), ECCC report (`https://eccc.weizmann.ac.il/report/2011/024/download`), and Lehigh technical paper (`https://engineering.lehigh.edu/sites/engineering.lehigh.edu/files/_DEPARTMENTS/ise/pdf/tech-papers/17/17T_017.pdf`); search snippets support broad concavity context, not a claimed theorem-specific generalization. No theorem/generalization claim is inferred from those unrelated snippets. Local primary source `.mathlib-quality/references/clean.tex:1115–1117` states the exact λ bound and instructs squaring positive quantities, matching this proof. ChatGPT math MCP unavailable: metadata search returned zero matching tools. No remote search failure hidden; all five native search calls responded successfully.

## Line packing

Reference requested via native run_code twice after source changes: import-out-of-date error (disclosed, not treated as a successful #check). Shell fallback `/Users/ramin/.elan/bin/lake env lean /private/tmp/lattice_sqrt_check.lean` exited 0 and produced this exact width-100 output:

```text
@Roth.sqrt_one_sub_inv_lt : ∀ {m : ℕ}, 2 ≤ m → ∀ {lam : ℝ}, 2 * √↑m < lam → √(1 - 1 / ↑m) < 1 - lam⁻¹ ^ 2
'Roth.sqrt_one_sub_inv_lt' depends on axioms: [propext, Classical.choice, Quot.sound]
```

| Signature line | Codepoints | Next token | Arithmetic | Action |
|---|---:|---|---|---|
| 23 | 88 | complete conclusion `√(1 - 1 / (m : ℝ)) < 1 - lam⁻¹ ^ 2 := by`, 40 | 88+1+40=129 >100 | ok |
| 24 | 44 | no next signature line | n/a | ok |

## Inequality scan

| Location | ≥/> occurrences | Rewrite | Rename |
|---|---:|---|---|
| signature + all body hypotheses | 0 | n/a: already ≤/< | n/a |

The docstring's natural-language ≥/> is intentionally excluded.

## Every golfing rule (42)

1.1 n/a: no by-exact wrapper. 1.2 n/a: no by-rfl. 1.3 n/a: rw/exact rewrites the *goal* to apply reciprocal comparison, so `rwa` does not remove an exact without obscuring the direct proof. 1.4 n/a: no simp/exact. 1.5 n/a: no trailing rfl. 1.6 n/a: no constructor. 1.7 n/a: no apply/exact chain. 1.8 n/a: no contradiction chain. 1.9 n/a: no lambda. 1.10 APPLIED: inline original h0/htm at their sole consumers. 1.11 n/a: no apply/intro. 1.12 n/a: no show. 1.13 n/a: no projected conjunction. 1.14 n/a: no consecutive rw. 1.15 n/a: no terminal simp. 1.16 n/a: no nonterminal simp. 1.17 n/a: no named function application with clearer available receiver notation. 1.18 n/a: final by-proof arguments are followed by another argument or embedded inside rw/nlinarith brackets; `<|` adds no useful compression. 1.19 n/a: no push_neg. 1.20 n/a: not existential.

2.1 TRIED whole-goal grind: failed with open reciprocal/sqrt contradiction. 2.2 TRIED terminal grind at current L32: failed; keep nlinarith. 2.3 n/a: no simp/closing chain. 2.4 n/a: no function-property goal. 2.5 existing denominator positivity retained; positivity tried on hsq: `not a positivity goal`. 2.6 TRIED whole-goal gcongr: did not make progress. 2.7 TRIED lia: grind arithmetic failed; goal is real nonlinear arithmetic, no omega fallback warranted. 2.8 TRIED whole and terminal aesop: exhausted search, unresolved squared inequality. 2.9 TRIED whole norm_num: normalizes inverse expression but leaves goal; hsq norm_cast leaves real squared comparison; exact_mod_cast kept for hm'. 2.10 TRIED decide: free-variable goal rejected; decide+kernel inapplicable to parameterized real comparison. 2.11 n/a: goal strict inequality, no denominator identity. 2.12 n/a: no ring/ring_nf ending. 2.13 n/a: no symmetric branches. 2.14 n/a: no calc. 2.15 n/a: no family of similar generated subgoals.

3.1 n/a: no erw. 3.2 n/a: no continuity/measurability. 3.3 no omega; lia failure recorded at 2.7. 3.4 n/a: no rcases. 3.5 considered: no simp equality or predictable normal form; adding automation attributes to this specialized inequality has no demonstrated consumer benefit. 3.6 TRIED terminal simp_all: leaves squared inequality; no simp_all only retained. 3.7 n/a: no resource option.

## Step-back reflection

Whole-goal grind/simp/aesop/nlinarith/exact? failed; apply? selected the same appropriate sqrt API. Terminal grind/simp_all/aesop also failed while original nlinarith hint closes. Term composition would hide the two meaningful arithmetic bounds and does not shorten the proof. No redundant target-changing tactics remain. The concavity alternative `sqrt_one_add_le` is partial relevant API but not an exact consequence with the λ hypothesis; current square-and-reciprocate strategy mirrors the source and has nine body lines counting `:= by`.

## Verification and diff gates

- Independent original-type proof, importing only `Roth.Box` and mathlib sqrt (not this target), native lean_run_code: success true, timed_out false; `probe` axioms `[propext, Classical.choice, Quot.sound]`.
- Complete native `lean_diagnostic_messages` after edit and again after build: success true, partial false, timed_out false, failed_dependencies []; only inherited L1 header warning.
- `/Users/ramin/.elan/bin/lake build Roth.Lattice`: exit 0, target built in 26s; inherited header warnings for Box/Lattice only.
- Native actual-target `lean_verify`: axioms `[propext, Classical.choice, Quot.sound]`, trust standard, non_standard_axioms [], warnings [].
- Native run_code import of rebuilt module reported stale imports twice; actual live-file diagnostics and verify above succeed. This tool-specific stale scratch session is disclosed, not counted as proof failure or success.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | actual module build exit 0 |
| definition_protected | pass | no def/abbrev edit |
| theorem_statement_protected | pass | exact original two-line signature retained |
| structure_gate | pass | 9 body lines including `:= by`, no conjunction/branches |
| naming_gate | pass | descriptive snake_case; no forbidden pattern |
| line_packing_gate | pass | measured all two signature lines above |
| inequality_orientation_gate | pass | zero ≥/> in code |

Overall: pass. Parent owns cumulative/full-project gates and performance handoff; no full-project build run here. Historical proposal: hm1 only, not applied and closed by owner as unnecessary; no pending refactoring. Renames queued: none. Comments preserved: all existing documentation, no inline comments present.

Phase checklist: [✓] Step 1 full mandatory references; [✓] Step 2 all 24 audit items; [✓] Step 2.5 five actual searches; [✓] Step 2.6 hypothesis probes/public literature; [✓] Step 2.7 width arithmetic; [✓] Step 2.8 inequality table; [✓] Step 3 all 42 rules; [✓] Step 4 reflection; [✓] Step 5a complete clean diagnostics except inherited header; [✓] Step 5b gates; [✓] Step 6a no rename required.

Source SHA-256 at handoff: `9d5a4630daf715a8a7c8248c41046c74276421ccc603c004d020e129d049c53c`.

Owner checkpoint: explicit source-ownership revocation at above SHA256 before sequential full `lake build` and separate `lake build Roth.LeanEval`, session61721. Both exit0 (114.13s/37.98s), source hash stable. Logs `/private/tmp/roth-lattice-d01-{full,leaneval}.log`.
