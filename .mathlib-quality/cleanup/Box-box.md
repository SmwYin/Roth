# Phase 4 declaration report: `Roth.box`

Scope: only `Roth/Box.lean` original lines 43–45, now 43–44. The file worker owns shared reports, dependent builds, and Git. This worker changed only this declaration and this report.

## Step 1 — references

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md. Also read the full dedicated worker prompt, applicable style-rules.md sections, naming-conventions.md, and the lean4 skill. References are under `/Users/ramin/.codex/skills/mathlib-quality/references/`; the full prompt is `/private/tmp/roth-box-declaration-worker.md`.

## Step 2 — full audit

1. **LINT:** none in the target declaration. Complete diagnostics contain the preexisting missing copyright warning and unused hypotheses/section-variable warnings in later declarations; those are outside this worker's ownership.
2. **HAVE SCAN:** none; body is a data term.
3. **SET_OPTION:** none in declaration or source diff.
4. **SIMP SQUEEZE:** n/a: no simplifier calls in this definition.
5. **NAMING:** `box` is descriptive lowerCamelCase for the coordinatewise bounded multi-index box in namespace `Roth`; no numbered scheme, forbidden abbreviation, single-letter public name, or reversed inequality name. No rename warranted or queued.
6. **LINE PACKING:** signature is a single 54-codepoint line; required table below. Body was two lines; joined into one 97-codepoint line.
7. **BY PLACEMENT:** n/a: term definition has no `by`.
8. **FORMAT:** changed mathematical lambda `=>` to `↦`; retained two-space body indentation; no empty lines inside declaration, tactic chains, `haveI`, or `letI`.
9. **COMMENTS:** no inline comments; existing two-line docstring preserved byte-for-byte.
10. **DOCSTRING:** present; describes the coordinatewise box and cites its source. Retained verbatim per ownership instructions.
11. **VISIBILITY:** public mathematical object with external users in Lattice, Main, Taylor, CoeffNorm, and MainLemma; retain public.
12. **STRUCTURE:** data body two lines before, one after; no conjunction statement, tactic branches, or helper-extraction need. Below both 15/60-line thresholds.
13. **MATHLIB:** five-method search below; already built on `Fintype.piFinset`, transported to multi-indices by `Finsupp.equivFunOnFinite`. Generic interval API is a related construction, not a verified drop-in replacement under the current imports. No absence claim.
14. **JUNK DEF:** retain: established documented domain-specific object, membership and cardinality API, and numerous external call sites. This is not an undocumented single-use alias.
15. **EXISTS LEMMA:** n/a: not an existential theorem.
16. **SHOW vs CHANGE:** n/a: no `show` or `change`.
17. **PUSH_NEG:** none.
18. **GENERALISE:** all four elaborated parameters audited below; no signature changes. Literal drop-tests of both instance arguments fail; `Fintype` to `Finite` also fails for the current construction. No warranted generalisation proposal.
19. **INEQUALITY:** required scan table below; no inequalities in code signature or body. Bounds in docstring are prose.
20. **NORMAL-FORM:** finite product of coordinate ranges, transported through the canonical function/Finsupp equivalence. The existing membership theorem exposes the coordinatewise normal form; no restatement proposed.
21. **SYNTAX-GEN:** OK: explicit bound function `r : σ → ℕ` matches external clients; changing to a finitely supported bound would require callers to construct that value and is not an improvement demonstrated here.
22. **IMPORT-FANOUT:** n/a: no imports added or changed.
23. **CASTS:** 0 dropped / 0 cross-type / 0 load-bearing explicit expression casts in diff. Parameter/result type declarations are unchanged.
24. **INSTANCE-NAME:** n/a: this declaration is a definition, not an instance.

Issues found: (1) mathematical lambda arrow; (2) two body lines fit on one line. Both fixed. Refactoring needed: none.

## Step 2.5 — mathlib search status

| Method | Query / evidence | Outcome |
|---|---|---|
| A Lean-Finder | `finite set of finitely supported natural number functions bounded above coordinatewise, interval Iic` | Returned `DFinsupp.rangeIcc`, `DFinsupp.instLocallyFiniteOrder`, `Finsupp.instLocallyFiniteOrder`; related interval construction. |
| B Loogle | `Fintype.piFinset` | Returned `Fintype.piFinset` and nonemptiness API with full types; confirms existing generic finite-product building block. |
| C LeanSearch | `finite set natural multi indices bounded coordinatewise interval` | HTTP 500; unavailable, not evidence of absence. |
| D source search | Untruncated `rg` for `def piFinset`, `mem_piFinset`, `Iic`, `locallyFiniteOrder`, `equivFunOnFinite` in Finsupp/Interval and Fintype/Pi, followed by source reads | `Fintype.piFinset`, `Fintype.mem_piFinset`, `Finsupp.card_Iic`, interval instance found. |
| E name pattern | `Finsupp.Iic`, then `piFinset` via native local search | First index unavailable; second index warming but returned source hits including `Fintype.piFinset`, `piFinset_mul`, `piFinset_inv`, `piFinset_div`. No empty-index absence inference. |

Auxiliary variants inspected: `Fintype.mem_piFinset`, `piFinset_subset`, `piFinset_nonempty`, `piFinset_singleton`, `Finsupp.Icc_eq`, `card_Icc`, `card_Iic`, `Finset.mem_Iic`. `#check` verified `Fintype.piFinset`, `Finsupp.equivFunOnFinite`, `Finset.mem_Iic`, and `Finsupp.card_Iic` in compiled code.

Common-equivalents table: no matching discrete/compact/boundedness predicate bucket. The finite-product construction itself is already reused.

Conclusion: **partial match, keep the domain-specific definition built on existing mathlib**, with its established API and caller contract. An isolated interval comparison under existing imports failed to synthesize `LocallyFiniteOrderBot (σ →₀ ℕ)`; the Nat interval instance lives in `Mathlib.Order.Interval.Finset.Nat`. No extra import, interval rewrite, bridge lemma, or deletion was introduced. This is not a claim that a general interval formulation is impossible or absent. The parent requested bounded investigation rather than speculative construction work.

Six replacement rules considered: no wrapper theorem is being added; no absence claim; auxiliary variants searched; no custom typeclass predicate; no verified identical replacement justifies deleting an established API; existing module documentation describes the construction and its API (unchanged).

## Step 2.6 — generalisation status

Actual width-100 elaborated type:

```lean
@Roth.box : {σ : Type u_1} → [Fintype σ] → [DecidableEq σ] → (σ → ℕ) → Finset (σ →₀ ℕ)
```

| Parameter | Class | Used as | Mechanical candidates | Verified? | Result |
|---|---|---|---|---|---|
| `{σ : Type*}` | type variable | domain of bound and resulting multi-indices | Already universe-polymorphic; dropping would leave the domain undefined, not weaken a hypothesis | n/a: structural parameter | Retain |
| `[Fintype σ]` | typeclass | enumerates the product in `piFinset`; supplies finiteness for equivalence | Drop; replace with `[Finite σ]` | Yes, actual isolated native `lean_run_code` elaboration | Both fail to synthesize `Fintype σ` at `Fintype.piFinset` |
| `[DecidableEq σ]` | decidability | required by `piFinset` | Drop | Yes, actual isolated native `lean_run_code` elaboration | Fails to synthesize `DecidableEq σ` at `Fintype.piFinset` |
| `(r : σ → ℕ)` | structure value | each coordinate bound determines its range | Dropping makes `r j` undefined and destroys the box parameter; pointwise/strict weakenings do not apply to data | n/a: essential construction input | Retain |

These tests used isolated snippets to keep the public API untouched, as instructed. The failed candidates never entered project source. There are no proposition hypotheses to localize/unbundle or strict bounds to weaken. Replacing the construction with one using classical enumeration could remove computational arguments, but no downstream need or benefit warrants that API change. Inversion check: n/a, this is a direct data construction, not a proof that unfolds a concrete named object and proceeds abstractly.

Big-change candidates: none warranted. No additions or parameter changes requested.

### Public literature search

A. WebSearch query: `multi index box natural numbers product intervals generalization`.

Top three returned hits recorded:

1. [Teutsch, Index sets and universal numberings](https://people.cs.uchicago.edu/~teutsch/papers/numberings.pdf): unrelated computability result; not used as evidence.
2. [Stanford analysis notes, generalization to higher dimensions](https://math.stanford.edu/~ryzhik/STANFORD/STANF205-16/notes-205-16.pdf): defines a box as the Cartesian product of coordinate intervals. This supports the product interpretation, not an instruction to change the discrete multi-index API.
3. [IntervalBoxes.jl](https://github.com/JuliaIntervals/IntervalBoxes.jl): interval box library; corroborates product terminology but not a replacement for this natural-number/Finsupp construction.

The query also returned [Penn analysis notes on boxes](https://www2.math.upenn.edu/~gressman/analysis/13-partitions1.html), describing coordinate products. No literature-driven change to the current domain-specific definition is warranted by these findings.

B. ChatGPT math MCP: n/a, no callable matching tool in the session's tool inventory.

## Step 2.7 — line packing

Reference: definition, so no theorem-printing requirement; actual elaborated `#check` shown above. All signature lines are included.

| Stage | Sig line | Codepoints | Next signature token | Arithmetic | Action |
|---|---:|---:|---|---|---|
| Before | 43 | 54 | none; body starts after `:=` | n/a: signature complete | ok |
| After | 43 | 54 | none; body starts after `:=` | n/a: signature complete | ok |

Body line widths before: 56 and 45. After lambda arrow normalization, joining with one space and removing continuation indentation gives `55 + 1 + 41 = 97 ≤ 100`; applied. Final body width measured as 97 codepoints. Definition keyword/signature line is byte-identical.

## Step 2.8 — inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| — | Entire code signature and body | n/a: no `≥`/`>` inequality | none | none; `box` has no `_ge_`/`_gt_` |

The original `=>` is a lambda arrow, not a greater-than inequality; it is now `↦`. Docstring inequalities remain unchanged.

## Step 3 — all 42 golfing rules

| Rule | Status |
|---|---|
| 1.1 by exact wrapper | n/a: direct data term, no wrapper |
| 1.2 by rfl | n/a: no tactic proof |
| 1.3 rw + exact | n/a: no rewrites |
| 1.4 simp + exact | n/a: no simplifier |
| 1.5 trailing rfl | n/a: no tactic sequence |
| 1.6 anonymous constructor | n/a: no constructor proof |
| 1.7 apply + exact | n/a: no tactic applications |
| 1.8 by_contra! | n/a: no contradiction proof |
| 1.9 eta-reduce lambda | n/a: `j` occurs inside `r j + 1`, not as the final argument of a bare application; composition would add machinery |
| 1.10 inline have | n/a: no `have` |
| 1.11 apply + intro | n/a: no tactic proof |
| 1.12 redundant show | n/a: no `show` |
| 1.13 have projections | n/a: no `have` |
| 1.14 merge rw | n/a: no rewrites |
| 1.15 terminal simp only | n/a: no simplifier |
| 1.16 nonterminal simp | n/a: no simplifier |
| 1.17 dot notation | already used for `.map`, `.symm`, `.toEmbedding` |
| 1.18 remove trailing parentheses | n/a: parentheses delimit the receiver of `.map` and the arithmetic argument |
| 1.19 push_neg | n/a: none |
| 1.20 existential helper | n/a: data definition, not a helper lemma |
| 2.1 whole-proof grind | n/a: data construction whose value must be preserved, no proposition proof |
| 2.2 tactics before grind | n/a: no grind |
| 2.3 simpa consolidation | n/a: no simplifier sequence |
| 2.4 fun_prop | n/a: no function-property proposition |
| 2.5 positivity | n/a: no sign goal |
| 2.6 gcongr | n/a: no inequality goal |
| 2.7 lia/omega | n/a: no arithmetic proposition to prove |
| 2.8 aesop | n/a: data value must remain definitionally equal; not a logic/membership proof |
| 2.9 norm_num/norm_cast | n/a: no cast or numeric proof |
| 2.10 decide | n/a: result is a Finset value, not a decidable proposition |
| 2.11 field_simp/ring | n/a: no division identity |
| 2.12 linear_combination | n/a: no ring proof or hypotheses |
| 2.13 wlog | n/a: no branches |
| 2.14 calc term mode | n/a: already direct term, no calc |
| 2.15 multi-goal <;> | n/a: no goals |
| 3.1 erw → rw | n/a: neither present |
| 3.2 fun_prop migration | n/a: no continuity/measurability proof |
| 3.3 omega → lia | n/a: neither present |
| 3.4 rcases rfl | n/a: no destructuring |
| 3.5 automation attributes | n/a: public data definition, not a theorem; automatically unfolding the construction is not a demonstrated improvement over its membership API |
| 3.6 simp_all | n/a: absent |
| 3.7 maxHeartbeats | n/a: no option/limit overrides |

Additional style rules applied: mathematical lambda `↦`; body packed within 100 codepoints. No tactic-rule transformation was applicable.

## Step 4 — reflection and actual experiments

The definition is already a direct expression of its mathematics: finite product of coordinate ranges, then transport to multi-indices. A tactic-generated Finset would obscure the chosen data and potentially change the definition. `exact?`/`apply?` for an arbitrary Finset goal can return the empty set and do not test equivalence; consequently no tactic automation was applied to the data definition.

Actual native experiments:

- An equality between `Roth.box r` and the old `=>` expression closes by `rfl`.
- An independently named candidate using the edited expression is definitionally equal to `Roth.box r` by `rfl`.
- A genuinely isolated snippet importing only the existing mathlib construction modules defines the edited expression and proves equality to the original expression by `rfl`; success=true, timed_out=false, no errors/warnings.
- Drop `DecidableEq`, drop `Fintype`, and weaken `Fintype` to `Finite`: each emits its expected instance-synthesis error; no source changes from these tests.
- The interval comparison fails under the current imports as recorded above. It was not applied, and is not a claim of mathematical inequivalence.

No new lemma, helper, import, attribute, or public API was introduced.

## Step 5 — verification and gates

Complete native `lean_diagnostic_messages` after the edit: success=true, partial=false, timed_out=false, failed_dependencies=[], zero errors, zero sorry diagnostics. Existing warnings are solely the header and later declarations; no target warning. No LSP-unavailable shortcut was used.

Actual `/Users/ramin/.elan/bin/lake build Roth.Box` exited 0, 1154 jobs. The original module log path was subsequently reused by the file owner for the full build; the module exit-0 tool result remains the evidence. The file worker will separately run the full/dependent build before publication.

Axiom check: both `#print axioms Roth.box` and the independently compiled isolated candidate report exactly `[propext, Classical.choice, Quot.sound]`. Native imported-code check emitted an informational out-of-date-import notice after rebuild; the fresh isolated construction check had no such notice and succeeded independently. The complete live-file diagnostics and Lake build are authoritative source gates.

Snapshot `/private/tmp/roth-box-box-before.lean` compared with final source: everything before/after target declaration unchanged; signature byte-identical; docstring therefore unchanged; forbidden-token scan in target found no sorry/admit/axiom/native_decide/set_option.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | `lake build Roth.Box`, actual exit 0 |
| definition_protected | pass | keyword/signature unchanged; body syntax-only edit; compiled `rfl` equality with original body |
| theorem_statement_protected | pass | no theorem edited |
| structure_gate | pass | one-line data body; no conjunction statement or branches |
| naming_gate | pass | descriptive lowerCamelCase; no prohibited pattern/abbreviation |
| line_packing_gate | pass | complete 54-codepoint signature; body measured 97 |
| inequality_orientation_gate | pass | no reversed inequality in code |
| declaration isolation | pass | source prefix/suffix byte-identical around target |
| type preservation | pass | same elaborated type, signature byte-identical |
| axiom gate | pass | standard axioms only |
| cumulative dependents | delegated | file worker runs before checkpoint; not represented as tested here |

Overall per-declaration gates: pass.

## Step 6 — result

Before: 3 declaration lines / 2 body lines. After: 2 declaration lines / 1 body line. Saved: 1 line.

Audit issues found: 2. Fixed: 2. Refactoring deferred: 0. Rules applied: lambda syntax and body line packing; rule 1.17 already satisfied. Renames queued: none. Comments: no inline comments; existing docstring preserved. Refactoring needed: none.

- [x] Step 1: required reference documents read.
- [x] Step 2: full 24-item audit printed above.
- [x] Step 2.5: all five mathlib methods recorded with honest availability.
- [x] Step 2.6: every parameter audited, actual drop-tests, public literature search.
- [x] Step 2.7: complete per-signature-line width table.
- [x] Step 2.8: per-occurrence inequality scan table.
- [x] Step 3: all 42 rules have concrete status.
- [x] Step 4: step-back reflection and compiled experiments.
- [x] Step 5a: complete successful LSP diagnostics.
- [x] Step 5b: all applicable diff gates pass, actual module build.
- [x] Step 6a: no rename warranted; sidecar untouched.

Publication verification for `Roth.box`: actual full `lake build` session 17861 exited 0
(2586 jobs; `/private/tmp/roth-box-box-build.log`); separate `lake build Roth.LeanEval`
session 96802 exited 0 (2585 jobs; `/private/tmp/roth-box-d01-leaneval.log`).
All dependent modules pass; remaining warnings are baseline warnings tracked for their own cleanup.
