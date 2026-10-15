# Declaration audit: `Roth.card_box`

Dedicated Phase-4 worker; baseline `5bed172`; source `Roth/Box.lean:53–54`.
Result: unchanged. Two declaration lines, one proof-body line, zero lines saved.
The statement, public API, definition dependencies, and existing docstring are preserved verbatim.

## Step 1 — references

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md in full. Also read the complete
declaration-worker prompt, lean4/SKILL.md, naming-conventions.md, and applicable
style-rules.md sections on formatting, comments/documentation, inequalities,
declarations, tactics, visibility, generalisation, API, and normal forms.

## Step 2 — full audit

1. **LINT:** no diagnostics on the target. Complete file diagnostics have no errors;
   header and later-declaration warnings remain in their respective owners' scope.
2. **HAVE SCAN:** none; the entire body is `simp [box]`.
3. **SET_OPTION:** none in this declaration; no options added.
4. **SIMP SQUEEZE:** L54 is terminal `simp [box]`, already unsqueezed. Keep it.
5. **NAMING:** `card_box` describes the cardinality operation on `box`, follows
   snake_case and the `card_<object>` convention, and has no forbidden abbreviation,
   numeric scheme, single-letter name, `_ge_`, or `_gt_`. No rename required.
6. **LINE PACKING:** single 66-codepoint signature line; complete table below.
7. **BY PLACEMENT:** `by` is at the end of the signature line.
8. **FORMAT:** proof has two-space indentation, one tactic, no internal blank lines,
   semicolon chains, redundant parentheses, or `haveI`/`letI`.
9. **COMMENTS:** no inline proof comments; existing three-line docstring untouched.
10. **DOCSTRING:** existing statement description and source references make its
    counting role explicit. This elementary headline result needs no extra application
    recipe; preserved under the task's docstring protection.
11. **VISIBILITY:** public headline API. External references include Lattice.lean:182,
    Main.lean:522, and MainLemma.lean:337, plus local card_le_card_box. Keep public.
12. **STRUCTURE:** one proof line is below the 15-line headline threshold. No conjunction,
    branch, or helper extraction opportunity.
13. **MATHLIB:** the existing proof already uses the general cardinality API through
    simp. Five-method status and compiled application below.
14. **JUNK DEF:** n/a: theorem, not a definition.
15. **EXISTS LEMMA:** n/a: neither private nor existential.
16. **SHOW vs CHANGE:** n/a: neither occurs.
17. **PUSH_NEG:** n/a: no negation tactic occurs.
18. **GENERALISE:** all four elaborated parameters examined and drop-tested in isolated
    snippets; none can simply be removed from the existing statement. Details below.
19. **INEQUALITY:** no inequality in the statement/hypotheses; table below.
20. **NORMAL-FORM:** already normal: cardinality on the left, explicit product on the
    right, suitable for rewriting a box count. General mathlib Pi-cardinality normal
    form is the same orientation.
21. **SYNTAX-GEN:** OK: explicit bound vector `r` and a rewrite-ready equality serve all
    observed callers. An arbitrary family of finite sets already has mathlib API.
22. **IMPORT-FANOUT:** n/a: no import added or changed.
23. **CASTS:** 0 dropped / 0 kept as cross-type / 0 kept as load-bearing in the empty diff.
24. **INSTANCE-NAME:** n/a: this declaration is not an instance.

Issues to fix: none. Refactoring needed: none. Existing public API is explicitly protected
by the task. The generic skill's wrapper-deletion suggestion does not authorize removing
this documented, externally used `box` API. No cross-file deletion or speculative companion
declaration is proposed.

## Step 2.5 — Mathlib search status

| Method | Query / evidence | Result |
|---|---|---|
| A: Lean-Finder | `cardinality of finite Cartesian product of ranges equals product of cardinalities` | `Finset.card_pi`, `Nat.card_pi`, `Fintype.card_piFinset` |
| B: Loogle | `Fintype.piFinset, Finset.card` | `Fintype.card_piFinset`, `_const`, filtered Pi variants |
| C: LeanSearch | Cartesian-product cardinality concept | Unavailable: inherited session evidence records HTTP 500; parent explicitly instructed not to repeat stalled calls. This is not an absence result. |
| D: source search | Untruncated `rg` for `card_piFinset`, `card_range`, `theorem card_map` | BigOperators.lean:124/130; Finset/Card.lean:174/271 |
| E: local name search | `card_piFinset` | Exact and constant variant found in source; index reported `warming`, so no index-based absence claim |

Auxiliary variants checked: `card_piFinset_const`, `card_filter_piFinset_eq_of_mem`,
`card_filter_piFinset_const`, `Finset.card_pi`, `Finset.card_map`, `Finset.card_range`.
Common-equivalents table: no discrete/compact/separation bucket applies; this is finite
Cartesian-product counting.

Compiled `#check`s verified `Fintype.card_piFinset`, `Finset.card_map`, and
`Finset.card_range` with the current project imports. A compiled example using
`simpa [Roth.box] using Fintype.card_piFinset (fun j ↦ Finset.range (r j + 1))`
succeeds, but emits unnecessarySimpa and is longer. The existing `simp [box]` already
uses these lemmas directly. Live `exact?` failed; `apply?` offered incomplete generic
routes such as `Finset.card_eq_of_equiv_fin`, requiring a new equivalence. No absence
claim is made, and no independent counting proof is introduced.

Conclusion: found the general mathlib counting ingredients already used in the proof;
retain the authorized public `box` API and its minimal simplifier proof. No Phase-5 action.

## Step 2.6 — generalisation status

All probes below used native `lean_run_code`, returned complete diagnostics, and never
modified the live file. Failed variants were discarded.

| # | Parameter | Class | Use | Mechanical candidates tried | Verified? | Result |
|---|---|---|---|---|---|---|
| 1 | `{σ : Type*}` | type variable | Domain of `r`, box indices, product index | Drop with autoImplicit false; inspect universe | yes | Drop: unknown σ; already universe-polymorphic `Type u_1`, no fixed universe to weaken |
| 2 | `[Fintype σ]` | typeclass | Required by box and finite product in statement | Drop; replace with `[Finite σ]` | yes | Both fail to synthesize Fintype σ while elaborating statement; retain |
| 3 | `[DecidableEq σ]` | decidability | Instance argument of box in statement | Drop | yes | Fails to synthesize DecidableEq σ before proof; retain |
| 4 | `(r : σ → ℕ)` | value | Both sides depend on bounds | Drop with autoImplicit false | yes | Unknown r on both sides; retain; no proposition to weaken or point-localize |

No algebraic/analytic structures, strict hypotheses, global function properties, or
bundled logical hypotheses exist to weaken. Replacing the statement's construction by
a classically chosen one would be an API/definition restatement, not a dropped proof-only
instance; it is not needed for the current API.

Inversion check: `box` appears in the one unfolding simp call and the remaining content
is abstract Cartesian-product counting. The abstraction already exists as
`Fintype.card_piFinset`; it is used by the current proof. There is no missing general
theorem to add locally. Big-change candidates: none warranted.

### Literature search

[A] WebSearch query: `finite Cartesian product cardinality product rule generalization`.
Top three returned hits recorded:

1. [Androma, Cardinality of a Finite Cartesian Product](https://androma.org/theorems/15123).
2. [ProofWiki, General Result/Corollary](https://proofwiki.org/wiki/Cardinality_of_Cartesian_Product_of_Finite_Sets/General_Result/Corollary).
3. [ProofWiki, General Result](https://proofwiki.org/wiki/Cardinality_of_Cartesian_Product_of_Finite_Sets/General_Result).

Primary teaching source in the same results: [James Aspnes, Yale, HowToCount §2.5](https://www.cs.yale.edu/homes/aspnes/pinewiki/HowToCount.html)
states the finite-family product rule. This supports the canonical abstraction already
represented by mathlib's Pi-cardinality lemma. No bound positivity assumption is needed.
The current statement permits zero coordinates and the empty index type.

[B] ChatGPT math MCP: n/a: tool inventory contains no such connected tool.
Literature-driven additions: none; the general theorem is already available in mathlib.

## Step 2.7 — line packing

Actual `#check @Roth.card_box` with `format.width := 100`:

```lean
@Roth.card_box : ∀ {σ : Type u_1} [inst : Fintype σ] [inst_1 : DecidableEq σ] (r : σ → ℕ),
  (Roth.box r).card = ∏ j, (r j + 1)
```

| Signature line | Codepoints | Next signature token | Arithmetic | Action |
|---|---:|---|---|---|
| 53 | 66 | none: proof body follows | n/a; sole complete signature line, 66 ≤ 100 | ok |

Measured programmatically from the actual source, including `:= by`. There is no dangling
conclusion or signature fragment to repack. Before and after table are identical.

## Step 2.8 — inequality scan

| # | Location | Original | Rewrite | Lemma rename? |
|---|---|---|---|---|
| — | Entire signature and all elaborated parameter types | n/a: no ≥ or > | none | no `_ge_` / `_gt_` in `card_box` |

## Step 3 — all golfing rules

### Phase 1

- [1.1] by exact wrapper: n/a; body uses simp.
- [1.2] by rfl: n/a; no rfl body; live rfl probe fails definitional equality.
- [1.3] rw + exact: n/a; neither sequence occurs.
- [1.4] simp + exact: n/a; simp closes immediately.
- [1.5] trailing rfl: n/a; no trailing tactic.
- [1.6] constructor + exact: n/a; equality, no constructors.
- [1.7] apply + exact: n/a; no apply sequence.
- [1.8] by_contra + push_neg: n/a; no contradiction argument.
- [1.9] eta reduction: n/a; no lambda in proof.
- [1.10] single-use have: n/a; zero haves.
- [1.11] apply + intro: n/a; neither tactic occurs.
- [1.12] redundant show: n/a; no show.
- [1.13] have projections: n/a; no haves/projections.
- [1.14] consecutive rw: n/a; no rewrites.
- [1.15] terminal simp only: n/a; terminal simp is already unsqueezed.
- [1.16] nonterminal bare simp: n/a; existing simp is terminal.
- [1.17] dot notation: n/a; no explicit lemma application to shorten.
- [1.18] `<|`: n/a; no nested term application.
- [1.19] push_neg replacement: n/a; no push_neg.
- [1.20] existential helper: n/a; public cardinality equality, no existential helper.

### Phase 2

- [2.1] grind whole proof: live `grind` and `grind [box]` both fail; retain simp.
- [2.2] delete before grind: n/a; no grind in source or prefix tactics.
- [2.3] simpa consolidation: explicit card_piFinset candidate compiles but triggers
  unnecessarySimpa and lengthens proof; retain existing terminal simp.
- [2.4] fun_prop: n/a; no function-property goal.
- [2.5] positivity: n/a; target is a cardinality equality, not positivity/nonzeroness.
- [2.6] gcongr: n/a; no inequality or monotonicity step.
- [2.7] lia/omega: live lia and fallback omega fail; cardinality and product remain
  unrelated symbolic arithmetic atoms without counting lemmas.
- [2.8] aesop: live attempt fails with no progress.
- [2.9] norm_num/norm_cast: n/a; no concrete numeric computation or coercion.
- [2.10] decide: live attempt fails because expected type contains free σ/r/instances;
  kernel finite enumeration is not applicable to this arbitrary symbolic family.
- [2.11] field_simp; ring: n/a; no field/division expression.
- [2.12] linear_combination: n/a; no ring tail or algebraic hypotheses.
- [2.13] wlog: n/a; no symmetric branches.
- [2.14] collapse calc: n/a; no calc chain.
- [2.15] `<;>`: n/a; single goal closed by one tactic.

### Phase 3

- [3.1] erw to rw: n/a; no erw.
- [3.2] legacy function tactics: n/a; none.
- [3.3] omega to lia: both tested in 2.7 and fail; neither occurs in source.
- [3.4] rcases with rfl: n/a; no case split.
- [3.5] register automation: considered, no new attribute. Existing cardinality facts
  are already simp lemmas after explicit box unfolding; changing the public automation
  surface is unnecessary for this cleanup and observed callers use rw directly.
- [3.6] simp_all: `simp_all [box]` succeeds but is longer, and there are no hypotheses
  to simplify; original simp is clearer. No simp_all only to unsqueeze.
- [3.7] resource options: n/a; no maxHeartbeats/maxRecDepth option.

Rules applied: none; the original proof already satisfies applicable transformations.

## Step 4 — step back

The proof already consists of one tactic. Bare simp fails because box is not globally
unfolded by simp; `simp [box]` succeeds. Rfl, grind, aesop, arithmetic tactics, decide,
and exact? do not improve it. Apply? offers longer incomplete routes. Explicit
cardinality-lemma simpa succeeds but is redundant by the linter. A composed term would
expose map/product/range plumbing rather than improve this proof. Keep unchanged.

## Step 5 — verification and gates

- Native `lean_goal` at L54 reports the expected original goal before simp and no goals
  after it.
- Native `lean_diagnostic_messages` on the whole file returns `success: true`,
  `partial: false`, `timed_out: false`, and no failed dependencies or errors. Target
  range has no warnings. Preexisting header and later-declaration warnings remain.
- Actual `/Users/ramin/.elan/bin/lake build Roth.Box` exited 0 (session 82489), 1154 jobs.
  Log: `/private/tmp/roth-box-d03-module.log`.
- Native isolated compilation using only the file's eight Mathlib imports, a local
  clone of the unchanged box definition, and the target proof succeeds. It does not
  import Roth.Box or use Roth.card_box. No errors or warnings.
- Both actual and isolated theorem axiom prints report only
  `propext`, `Classical.choice`, `Quot.sound`.
- Complete type printed above; statement unchanged. A programmatic comparison against
  `git show 5bed172:Roth/Box.lean` reports entire source identical.
- Parent separately confirmed full `lake build` session 4764 and `lake build Roth.LeanEval`
  session 20469 exit 0 against this unchanged source. These dependent builds were run
  by the file owner, not claimed as this worker's invocations.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Actual Roth.Box build exited 0, log above |
| definition_protected | pass | Empty source diff; every definition unchanged |
| theorem_statement_protected | pass | Source byte-identical to worker baseline; actual complete type checked |
| structure_gate | pass | 1 body line ≤ 15 headline limit, no ∧ or branches |
| naming_gate | pass | Descriptive `card_box`; no forbidden patterns/abbreviations |
| line_packing_gate | pass | Complete one-row 66-codepoint table, no repack row |
| inequality_orientation_gate | pass | Complete scan table; no ≥/> or ge/gt name |
| isolation/type/axiom | pass | Independent import-only clone and standard-axiom checks succeed |

Overall: pass. Audit issues found: 0. Fixed: 0. Refactoring deferred: 0.
Renames queued: none. Comments preserved: no proof comments present; existing docstring
preserved verbatim. Refactoring needed: none.

## Step 6 — phase checklist

- [x] Step 1: references read.
- [x] Step 2: all 24 audit items recorded.
- [x] Step 2.5: all five search methods have evidence/status, including unavailable service.
- [x] Step 2.6: complete parameter table, actual drop tests, inversion check, public literature.
- [x] Step 2.7: every signature line measured and table emitted.
- [x] Step 2.8: inequality scan table emitted.
- [x] Step 3: all 42 rules have a concrete status.
- [x] Step 4: whole-proof alternatives actually tried and assessed.
- [x] Step 5a: complete LSP verification succeeds.
- [x] Step 5b: module, diff, structure, naming, packing, inequality, isolation/type/axiom gates pass.
- [x] Step 6a: no renames needed; sidecar untouched.
- [x] Step 6b: source ownership released unchanged; report ready for file-owner checkpoint.
