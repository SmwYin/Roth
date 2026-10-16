# Phase 4: `Roth.sum_inv_le`

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md, together with both SKILL.md files,
the complete Phase-4 worker prompt, and relevant style/naming sections.

Scope: only the private declaration, originally and finally lines 41–55. No Git,
shared-progress, docstring, header, import, definition, signature, or version edits.
Source ownership ceased on the owner's explicit freeze instruction.

Baseline: owner checkpoint `53c603b`, full build and separate LeanEval both exit 0
(session 74194, 6.14s and 2.86s); evidence
`/private/tmp/roth-lattice-d02-{full,leaneval}.log` and builds.json.
Native complete module diagnostics before and after edits: success, partial=false,
zero errors, only the existing line-1 copyright warning. The user reserved the header
decision; it was neither invented nor suppressed.

## Full audit

| Item | Finding/action |
|---|---|
| 1 Lint | No target warnings; inherited header warning outside scope. |
| 2 Have | `hr'` has a proof, keep; `h` has the pointwise proof and is reused by rewrite, push_cast, and linarith, keep; `hjr` is consumed by cast-aware gcongr and Nat.cast_sub, keep; `hx2` has a proof, keep; single-use anonymous no-by reciprocal bound inlined into `simpa ... using`. |
| 3 Options | No local resource or linter options. |
| 4 Simp | No nonterminal simp. Terminal `simpa only` unsqueeze actually tried and failed downstream: unrestricted simp rewrites reflected index `r + 1 - 1 - j` to `r - j`, preventing `sum_range_reflect` matching at L52. Keep `only` to preserve that normal form. |
| 5 Naming | `sum_inv_le` describes the inverse-sum inequality, uses snake_case, and has no forbidden abbreviation/number pattern; mathematical-property naming is appropriate. No rename queue. |
| 6 Packing | Both signature lines measured below; unchanged. |
| 7 By | All `by` tokens end their preceding statement line. |
| 8 Format | Both lambdas now use ↦; separate rw and field_simp; two-space proof indentation. |
| 9 Comments | None present in target; none removed. |
| 10 Doc | Private helper needs no docstring; existing surrounding docs untouched. |
| 11 Visibility | Already private, one in-file caller `sum_inv_lt`. |
| 12 Structure | 13 body lines, one 7-line pointwise proof, no conjunction or case branches; no extraction required. |
| 13 Mathlib | Five actual searches below; retain local pairing calculation using existing sum/reflection API. |
| 14 Junk def | n/a: lemma. |
| 15 Exists | n/a: no existential witness lemma. |
| 16 Show | Term-mode equality witness used inside simp lemma list, not a tactic-mode goal change; retain. |
| 17 Push | No deprecated push_neg. |
| 18 Generalise | Every parameter probed below; no retained change. |
| 19 Inequality | All signature/local inequalities use ≤/<; scan below. |
| 20 Normal form | Existing range sum and inverse syntax match direct caller and reflection API. Preserve the inferred `r + 1 - 1 - j` reflected index until reflection rewrite. |
| 21 Syntax generality | Current caller supplies hr/hlam directly; no restatement benefits that caller. |
| 22 Imports | n/a: no new import. |
| 23 Casts | Dropped the explicit Nat.cast_le bridge by using gcongr. Remaining Nat→Real coercions are genuine; zero ascription fixes needed. The nested Nat annotation distinguishes truncated subtraction before casting from real subtraction. |
| 24 Instances | n/a: no instance declaration or local instance. |

Concrete issues fixed: single-use temporary, manual cast arithmetic, two lambda arrows,
and chained tactics. No refactoring deferred.

## Mathlib search status

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | `sum over range reciprocal affine positive bounded using reflection j n-j` | Returned factorial/geometric/reciprocal-square bounds; no matching affine pairing bound among the five returned results. |
| B Loogle | `Finset.sum_range_reflect` | Exact existing reflection identity; retained direct use. |
| C LeanSearch | `upper bound sum reciprocal affine sequence by pairing reflection` | Returned Schlömilch and reciprocal-square estimates; inspected types do not give this finite affine estimate. |
| D Source | `sum_inv_le\|sum_range_reflect\|sum.*inv.*le` in BigOperators/Intervals and Analysis/PSeries | Reflection usage and reciprocal-square bounds; no full match in searched files. |
| E Local names | `sum_inv_le`; `sum_range_reflect` | Local declaration, reciprocal-square bounds, reflection identity. Index first unavailable then warming: these are positive hits, not evidence of absence. |

Auxiliary forms considered: reciprocal-square `_le_sub` and `_le` estimates and the
generic `sum_range_reflect`; no applicable `_of_`/left/right specialization identified.
Common-equivalents table: no discrete/finiteness/separation/bornology bucket applies.
Native services were available; no DNS failure occurred in these calls. Warming-index
limitations are explicit; no claim of global mathlib absence is made.

Compiled generic-route probes: whole-proof `exact?` failed; `apply?` returned only
partial inequality transformations (e.g. toNNReal), not a completed proof. Whole-proof
grind, simp, aesop failed. Keep this substantive finite pairing argument; it is not a
one-to-three-call wrapper. No new public API or documentation rewrite is justified.

## Generalisation status

All candidates ran through native lean_run_code on independent renamed declarations;
failed candidate snippets were discarded, with no live signature edits.

| Parameter | Class/use | Candidates actually probed | Verified result |
|---|---|---|---|
| `{r : ℕ}` | Value, range length/denominator/reflection | Drop binder with autoImplicit=false | Fails unknown `r` in dependent statement. Abstract index change is not mechanical: Nat range and truncated subtraction are essential here. |
| `(hr : 1 ≤ r)` | Proposition, positive denominator | Drop; weaken to `0 ≤ r` | Drop fails unknown hr; weak form fails exact_mod_cast because `0 ≤ r` cannot prove `0 < r`. |
| `{lam : ℝ}` | Value, summand and bound | Drop binder with autoImplicit=false | Fails unknown lam throughout statement. Ordered-field abstraction needs a matching abstract pair estimate and gives no current caller benefit; closed without API proposal. |
| `(hlam : 2 < lam)` | Proposition, pair estimate input | Drop; weaken to `2 ≤ lam` | Drop fails unknown hlam; weak form mismatches pair helper's `2 < lam` input. This rejects reuse of this proof, not the mathematical truth of a weaker theorem. |

No typeclass, decidability, global function-property or universe parameter exists to
weaken/localise. Inversion check: the summand parameters remain in the pointwise proof
and reflection step; this does not merely unfold a named concrete object and forget it.
Optional weaker λ/abstract-field APIs have no concrete current-caller benefit and are
closed, with no pending user question. Literature search: n/a, private declaration,
explicit Phase-4 private/aux literature exemption.

## Signature packing

Actual built target, #check at format.width 100:

```lean
@Roth.sum_inv_le✝ : ∀ {r : ℕ},
  1 ≤ r →
    ∀ {lam : ℝ}, 2 < lam → ∑ j ∈ Finset.range (r + 1), (lam - 1 + 2 * ↑j / ↑r)⁻¹ ≤ (↑r + 1) * (lam / (lam ^ 2 - 1))
```

| Signature line | Codepoints | Next complete conclusion token | Arithmetic | Action |
|---|---:|---|---|---|
| 41 | 74 | 90-character conclusion through `:= by`, excluding indentation | 74 + 1 + 90 = 165 > 100 | ok |
| 42 | 94 | No next signature line | n/a | ok |

Conclusion tokens are kept together rather than splitting the sum binder off its body.

## Inequality scan

| Occurrence | Location | Orientation | Rewrite/rename |
|---|---|---|---|
| 1 | hr | `1 ≤ r` | none |
| 2 | hlam | `2 < lam` | none |
| 3 | conclusion | sum `≤` bound | none |
| 4 | hr' | `0 < (r : ℝ)` | none |
| 5 | hjr | `j ≤ r` | none |
| 6 | hx2 | affine term `≤ 2` | none |
| — | complete target | zero ≥/> operators | no `_ge_`/`_gt_` name; no queue |

## All 42 golfing rules

| Rule | Status |
|---|---|
| 1.1 | n/a: exact_mod_cast has proof content, no by-exact wrapper. |
| 1.2 | n/a: no by-rfl. |
| 1.3 | Original rwa already fused; replaced single-use temporary through simpa using. |
| 1.4 | Applied simpa using direct pair estimate. |
| 1.5 | n/a: no trailing rfl. |
| 1.6 | n/a: no constructor. |
| 1.7 | n/a: no apply/exact chain. |
| 1.8 | n/a: no contradiction. |
| 1.9 | n/a: lambdas compute summand/pointwise proof, not eta expansions. |
| 1.10 | Applied to anonymous pair bound; h and hjr retained for multiple consumers. |
| 1.11 | n/a: no apply/intro. |
| 1.12 | Equality witness's term show fixes exact rewrite proposition; not redundant. |
| 1.13 | n/a: no projected conjunction. |
| 1.14 | No adjacent rw blocks to merge; field_simp separated from rw. |
| 1.15 | Unsqueeze actually attempted; fails reflection rewrite after simp changes index to r-j. Keep only. |
| 1.16 | n/a: no nonterminal bare simp. |
| 1.17 | Existing .1 membership projection appropriate; no dot-notation gain. |
| 1.18 | n/a: no dollar or avoidable outer parenthesised argument. |
| 1.19 | n/a: no push_neg. |
| 1.20 | n/a: no existential helper. |
| 2.1 | Whole-proof grind failed with unresolved inverse-sum inequality. |
| 2.2 | n/a: no retained grind. |
| 2.3 | Applied direct simpa consolidation. |
| 2.4 | n/a: no regularity predicate. |
| 2.5 | Existing positivity discharges nonnegative summand input. |
| 2.6 | Tested and retained gcongr for `2 * ↑j ≤ 2 * ↑r`. |
| 2.7 | n/a: membership bound directly uses Nat.lt_succ_iff; no arithmetic tactic needed. |
| 2.8 | Whole-proof aesop failed with unchanged inequality. |
| 2.9 | norm_cast on product inequality leaves `2*j ≤ 2*r`; gcongr closes. exact_mod_cast retained for hr'. |
| 2.10 | n/a: arbitrary real-parameter inequalities are not finite decidable computations. |
| 2.11 | Existing field_simp closes reflection identity after Nat.cast_sub; no following ring needed. |
| 2.12 | n/a: no ring/ring_nf terminal block. |
| 2.13 | n/a: no duplicated symmetric case branches. |
| 2.14 | n/a: no two-step calc. |
| 2.15 | n/a: no multiple similar subgoals. |
| 3.1 | n/a: no erw. |
| 3.2 | n/a: no continuity/measurability tactic. |
| 3.3 | n/a: no omega. |
| 3.4 | n/a: no rcases/rfl. |
| 3.5 | No new global attribute justified for a private, single-caller estimate. |
| 3.6 | n/a: no simp_all only. |
| 3.7 | n/a: no heartbeat or recursion limits. |

Step-back review: direct library reflection and summing the two-term estimate express
the mathematical argument. Failed whole-proof automation offers no shorter replacement.
The retained inferred reflected index is deliberate, not accidental cast plumbing.

## Verification and gates

`/Users/ramin/.elan/bin/lake build Roth.Lattice`: session 69913, exit 0;
Built Roth.Lattice (31s), Build completed successfully (2214 jobs). The earlier session
1126 also exited 0; the final source was independently checked by complete native LSP.
Owner alone runs final full-project and separate LeanEval builds after source freeze.

Independent exact-type, nonself proof: cloned pair bound as audit_pair_inv_add_inv_le
and target as audit_pair_sum_inv_le in lean_run_code; neither proof calls sum_inv_le.
It compiled and #print axioms returned only propext, Classical.choice, Quot.sound.
The compiled import was initially reported stale during concurrent module compilation;
the actual built target check below ran after successful module completion.

Actual built private declaration found by scanning imported environment constant names:
`_private.Roth.Lattice.0.Roth.sum_inv_le`. Its numeric name component cannot be parsed
as ordinary dotted source syntax; an initial direct #check failed parsing, then using
the actual environment Name with mkIdent in elabCommand succeeded. Its #check output
appears above; #print axioms returned exactly:

```text
'_private.Roth.Lattice.0.Roth.sum_inv_le' depends on axioms:
  [propext, Classical.choice, Quot.sound]
```

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Mandatory Roth.Lattice build session 69913 exit 0. |
| definition_protected | pass | No definition/abbreviation edit. |
| theorem_statement_protected | pass | Both signature lines byte-identical. |
| structure_gate | pass | 13 body lines, no conjunction/case branch. |
| naming_gate | pass | Mathematical snake_case property; no banned pattern. |
| line_packing_gate | pass | Both lines measured above. |
| inequality_orientation_gate | pass | Complete occurrence scan above. |
| diagnostics | pass | Complete module, partial=false, zero errors; original header warning only. |
| axioms | pass | Independent proof and actual built private target standard axioms only. |
| external breakage | owner gate | Signature private/unchanged; final whole project and separate LeanEval owned by file owner. |

New mathematical identifiers: none. `gcongr` is the only newly used tactic; its actual
successful lean_multi_attempt and module compilation verify availability. No proof
holes, new axioms, resource-limit changes or profiling scaffolding added.

## Result and all 11 worker checks

Before 15 lines; after 15 lines; net 0. Better direct proof flow and cast automation;
line savings offset by separating the chained tactics. Renames queued: none.
Comments preserved: none present. Refactoring needed: none.

- [✓] Step 1 — required references read.
- [✓] Step 2 — all 24 audit items answered.
- [✓] Step 2.5 — all five actual search attempts recorded with index limitations.
- [✓] Step 2.6 — per-parameter generalisation probes and private literature exemption.
- [✓] Step 2.7 — complete signature packing table with arithmetic and #check width 100.
- [✓] Step 2.8 — occurrence inequality table.
- [✓] Step 3 — all 42 rules assigned status.
- [✓] Step 4 — holistic proof reflection.
- [✓] Step 5a — complete native module diagnostics, zero errors/header only.
- [✓] Step 5b — mandatory module build and protection/content gates.
- [✓] Step 6a — no renames required; no shared sidecar mutation.

Final source file SHA256:
`f94e0e1dcdc5dc0fc14ca4c9940b57963f59d44c60361a4724d50604b501251d`.
Target declaration SHA256:
`335336a234333cb9f521bc29cd67fd9b603aaed331d2922bb3075a1c1cccc760`.

File-level simplify/buzz handoffs and final cumulative gates remain the owner's phase,
not claimed as completed by this Phase-4 worker.

Owner checkpoint: source ownership explicitly revoked at above freeze before sequential full/separate LeanEval session38839; both exit0 (104.70s/35.53s), hash stable. Logs `/private/tmp/roth-lattice-d03-{full,leaneval}.log`.
