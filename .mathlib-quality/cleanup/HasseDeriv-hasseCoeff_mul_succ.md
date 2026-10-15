# Phase 4 audit: `MvPolynomial.hasseCoeff_mul_succ`

Date: 2026-10-15. Dedicated worker; source scope only this private declaration.
Baseline source: `/private/tmp/decl17-before.lean`, declaration lines 188–212,
25 declaration lines and 22 proof-body lines. No commit or push by this worker.

## Reference-read confirmation

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md in full. Also read the full
Phase-4 worker prompt in `/Users/ramin/.local/share/roth-mathlib-quality/commands/cleanup.md`,
lean4/SKILL.md, mathlib-quality/SKILL.md, style-rules.md, naming-conventions.md,
and mathlib-review-stages.md. All reference paths are under
`/Users/ramin/.codex/skills/` unless explicitly stated otherwise. Large initial
combined reads were truncated; subsequent bounded reads covered the missing
spans. Earlier worker reports were consulted as templates, not verification.

## Full audit, before source edit

| # | Audit slot | Concrete finding and action |
|---|---|---|
| 1 | LINT | No supplied declaration warning. Preexisting file copyright warning only; final fresh diagnostics required below. |
| 2 | HAVE SCAN | L194 `hd`, no by, used twice (L196 and L198): normally retain. L195 `hds`, contains nested by at L197, used once at L199: proof content, normally retain or inline. L202 `hrest`, by proof, used once at L207: keep proof content. L209 `key`, no by, used at L210 and L211: not a trivial single-use alias. All four become unnecessary under the proved composition specialization and are removed with that argument. |
| 3 | SET_OPTION | No local options or heartbeat increases. |
| 4 | SIMP SQUEEZE | L192 `simp only [hasseCoeff]` and L208 `simp only [Finsupp.add_apply, Finsupp.single_eq_same]` are nonterminal and correctly squeezed. L197 `simp [S]` and L206 `simp [...]` are terminal and already unsqueezed. Replace whole proof by a terminal `simpa [...] using`; no terminal simp-only survives. |
| 5 | NAMING | `hasseCoeff` identifies the subject, `mul_succ` the successor factor. No forbidden abbreviation, numeric scheme, or single-letter public declaration. This is a standard binomial identity, so a descriptive property name is preferable to a generic `_aux` suffix. No rename required. |
| 6 | LINE PACKING | Three unchanged signature lines measured below; equation expressions are the natural units, and moving either next unit exceeds 100 codepoints. |
| 7 | BY PLACEMENT | `by` is at the end of L190. |
| 8 | FORMAT | Two-space proof indentation. Three old mathematical lambdas use `=>`; the replacement eliminates them entirely. No `haveI`, `letI`, blank proof lines, semicolon chains, or trailing spaces added. |
| 9 | COMMENTS | No inline proof comments or declaration docstring present; none removed. |
| 10 | DOCSTRING | n/a: private identity; no public API docstring required. |
| 11 | VISIBILITY | Already private. Sole source use is the adjacent pderiv_hasseDeriv proof. |
| 12 | STRUCTURE | Original 22-line straight-line body, no cases or conjunction. Composition specialization reduces it to two lines; no extraction or decompose flag needed. |
| 13 | MATHLIB | Five methods below; scalar choose identities are partial matches. Reuse the existing project composition identity and mathlib singleton-product simp API. |
| 14 | JUNK DEF | n/a: lemma, not def. |
| 15 | EXISTS LEMMA | n/a: equality, not existential. |
| 16 | SHOW vs CHANGE | No show or change. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | Every actual parameter audited below. No typeclass assumptions survive Lean section-variable pruning. |
| 19 | INEQUALITY | Equality conclusion; local hypotheses were support inclusions, all oriented subset. No ≥ or > relation. |
| 20 | NORMAL-FORM | Natural-number equality of binomial factors; multiplication and addition normalization suffice. No competing canonical predicate representation. |
| 21 | SYNTAX-GEN | Existing explicit j,d,e order serves the sole caller directly. No materially easier statement form identified; preserve signature. |
| 22 | IMPORT-FANOUT | n/a: no imports added or changed. |
| 23 | CASTS | Three old Finsupp type ascriptions disappear with hrest. No cross-type coercion or load-bearing ascription remains in added proof lines. |
| 24 | INSTANCE-NAME | n/a: no instance declaration. |

Issues to fix: redundant reproduction of coefficient composition; three lambda
arrows are resolved by deleting that obsolete proof. No source change outside
the target declaration is authorized or needed. Refactoring needed: none.

## Five-method mathlib search status

| Method | Exact query/scope | Result |
|---|---|---|
| A Lean-Finder | `multivariate binomial coefficients product successor index choose_succ_right_eq`, 4 results | Nat.succ_mul_binomial, Nat.binomial_succ_succ, Nat.choose_mul_add, Nat.choose_mul_succ_eq. Multinomial coefficients are not products of independent coordinatewise choose coefficients. |
| B Loogle | `Nat.choose, _ * _ = _ * _`, 6 results | Nat.choose_mul, Nat.choose_succ_right_eq, Nat.choose_mul_succ_eq, Nat.add_one_mul_choose_eq and DividedPowers API. The first four concern scalar indices; no direct hasseCoeff replacement. |
| C LeanSearch | `product binomial coefficients increment one index`, 3 requested | HTTP 500 on the single attempted request. Unavailable, not negative evidence; no repeated retries. |
| D Pinned mathlib sources | Full untruncated rg for hasseCoeff, choose_succ_right_eq, choose_mul_succ_eq, prod_single_index, prod_add_index in MvPolynomial/Finsupp/Nat Choose; inspected BigOperators/Finsupp/Basic.lean:68 and Choose/Basic.lean:210 | Existing scalar relation and singleton-product simplifier verified. No hasseCoeff identifier in the searched mathlib subtrees. |
| E Native local search | `choose_succ_right_eq`, project root, limit 5 | Nat.choose_succ_right_eq found in pinned source; index unavailable, so source match only. |

Auxiliary variants: choose_mul, choose_mul_succ_eq, add_one_mul_choose_eq,
prod_single_index, prod_add_index, and the already proved project
hasseCoeff_mul_hasseCoeff with singleton order. Common-equivalents table: no
bucket matches this binomial-product identity.

Concluded: partial mathlib matches, and an exact *project* specialization found.
Keep the private named identity and build on hasseCoeff_mul_hasseCoeff. This is
not a wrapper around one to three mathlib calls: the supporting composition
identity is project-specific, and deleting the existing helper would change a
different declaration's proof. No claim of exhaustive mathematical absence is
made while LeanSearch is unavailable.

Generic-route probes in the live declaration: `exact?` could not close it;
`apply?` returned only partial generic arithmetic/division suggestions. The
successful replacement was then compiled in a prefix-only file with neither
the original target proof nor any later declaration, excluding self-reference
and use of the subsequent pderiv theorem.

## Generalisation status

The width-100 `#check @hasseCoeff_mul_succ` confirms actual parameters are only
`{σ : Type u}`, `j`, `d`, and `e`. Section R and CommSemiring R are already absent.

| Parameter | Class | Used as | Mechanical candidates | Verification and result |
|---|---|---|---|---|
| `{σ : Type u}` | type variable/universe | Domain of Finsupp and j | Already universe polymorphic; drop cannot retain a well-typed statement | Scratch autoImplicit=false drop gives unknown σ. Type→Type* is already satisfied; Sort would not be accepted by Finsupp and changes the data interface. Retain. |
| `(j : σ)` | structure value | Distinguished coordinate and single index | Drop | Separate scratch compiler probe with autoImplicit=false reports unknown j throughout statement. No proposition/typeclass to weaken. Retain. |
| `(d : σ →₀ ℕ)` | structure value | Derivative order and successor coefficient | Drop | Separate scratch probe reports unknown d in conclusion. Coefficient type ℕ is essential to Nat.choose; abstract codomain is a different statement. Retain. |
| `(e : σ →₀ ℕ)` | structure value | Residual exponent and scalar e j+1 | Drop | Separate scratch probe reports unknown e in conclusion. No global property to point-localize or strict bound to weaken. Retain. |
| Section R, CommSemiring R | not actual theorem parameters | Unused | Inspect elaborated type | Already pruned by Lean; no assumption to remove. |

Drop probes use the compiler, not an assertion that LSP accepted a weakening;
none produced a candidate to retain or a source modification. Their errors are
at the deleted binder's free uses, before proof elaboration. The σ probe also
lacks local hasseCoeff declarations and is used only to confirm the free σ
dependency; no semantic inference rests on its other unknown-name diagnostics.
Big-change candidates: none. Inversion check: the original expanded-product
proof is subsumed by the existing composition identity, now used directly; no
new abstract API is needed. Literature: n/a, private declaration. Optional
ask_chatgpt_math skipped as instructed.

## Measured signature width table

`format.width` (not pp.width) is the supported option. Reference:

```text
@hasseCoeff_mul_succ : ∀ {σ : Type u_3} (j : σ) (d e : σ →₀ ℕ),
  hasseCoeff d (e + Finsupp.single j 1 + d) * (e j + 1) =
    (d j + 1) * hasseCoeff (d + Finsupp.single j 1) (e + Finsupp.single j 1 + d)
```

Widths count Unicode codepoints. Natural expression units, rather than splitting
function applications or parenthesized arithmetic, determine line breaks.

| Sig line | Chars before/after | Next signature unit | Arithmetic | Action |
|---|---:|---|---|---|
| 188 | 58 / 58 | LHS expression through `=`, 55 chars | 58 + 1 + 55 = 114 > 100 | ok |
| 189 | 59 / 59 | RHS expression through `:= by`, 82 chars | 59 + 1 + 82 = 142 > 100 | ok |
| 190 | 88 / 88 | None; proof begins next | n/a | ok |

## Inequality orientation table

| Occurrence | Original | Rewrite/status |
|---|---|---|
| Signature and parameters | No ≥ or > | n/a: equality only |
| Original hd, hds hypotheses | support ⊆ S | Already subset-oriented; both removed with obsolete proof |
| Final proof | No inequality hypotheses | No rewrite or name change needed |

## Golfing rule pass (all rules)

| Rule | Status |
|---|---|
| 1.1 by exact | n/a: no by-exact wrapper. |
| 1.2 by rfl | n/a: no by-rfl wrapper. |
| 1.3 rw + exact | n/a: no adjacent rw/exact chain. |
| 1.4 simp + exact | Applied conceptually: one terminal simpa using the composition theorem replaces the derivation. |
| 1.5 trailing rfl | n/a: none. |
| 1.6 anonymous constructor | n/a: equality proof, no constructor branches. |
| 1.7 apply + exact | n/a: none. |
| 1.8 by_contra! | n/a: no contradiction argument. |
| 1.9 eta reduction | Old proof lambdas are not eta expansions; entire obsolete lambdas removed. |
| 1.10 single-use have | All four haves audited above; whole-proof replacement removes them without losing proof content. |
| 1.11 refine + fun | Original prod_congr already uses refine+fun; obsolete after specialization. |
| 1.12 redundant show | n/a: no show. |
| 1.13 have projections | n/a: no conjunction projections. |
| 1.14 merge rw | No adjacent same-location rw calls: key rewrite at a hypothesis differs from goal rewrite. All removed in replacement. |
| 1.15 terminal simp only | n/a: both existing simp-only calls are nonterminal; final simpa is unsqueezed. |
| 1.16 nonterminal simp | n/a: both existing nonterminal calls already squeezed; none remains. |
| 1.17 dot notation | Existing .trans calls already dot notation; no improved dot form for composition specialization. |
| 1.18 <\| | Existing hds uses <\|; replacement has only necessary parenthesized singleton argument. |
| 1.19 push Not | n/a: no push_neg. |
| 1.20 existential inline | n/a: no existential helper. |
| 2.1 whole-proof grind | Tried live: failed on unresolved coefficient identity. |
| 2.2 before grind | Tried grind at original final ring: succeeds, but entire derivation is removed. No grind remains to precede. |
| 2.3 simpa consolidation | Applied: direct singleton specialization. Dropping add_left_comm fails normalization; dropping mul_comm also leaves reversed factors. |
| 2.4 fun_prop | n/a: no continuity, differentiability, or measurability proposition. |
| 2.5 positivity | n/a: no positive/nonnegative subgoal in original or final proof. |
| 2.6 gcongr | n/a: no order goal or monotonicity calc. |
| 2.7 lia/omega | Tried lia at original terminal ring; succeeds. No arithmetic block remains in selected proof. |
| 2.8 aesop | Tried whole proof; failed without progress. |
| 2.9 norm_num/norm_cast | n/a: symbolic natural binomial products, no numeric or cast subgoal. |
| 2.10 decide | n/a: universally symbolic j,d,e, no closed finite computation. |
| 2.11 field_simp; ring | n/a: no denominators or field. |
| 2.12 linear_combination | Tried at original ring with hypotheses; unknown tactic in current imports. No import added for an inferior replacement. |
| 2.13 wlog | n/a: no symmetric case branches. |
| 2.14 calc term | n/a: no calc. |
| 2.15 <;> | n/a: no multiple similar subgoals in selected proof. |
| 3.1 erw | n/a: absent. |
| 3.2 legacy function tactics | n/a: absent. |
| 3.3 omega→lia | Already tested in 2.7; no omega present. |
| 3.4 rcases with rfl | n/a: no rcases. |
| 3.5 automation attributes | No attribute added: private local successor identity has a specialized purpose and there is no repeated automation need. |
| 3.6 simp_all | n/a: no simp_all only, and final proof has no hypotheses for simp_all. |
| 3.7 heartbeat options | n/a: none present or introduced. |

## Step-back reflection and experiments

The old proof independently expands the same coordinatewise choose identity
already captured by hasseCoeff_mul_hasseCoeff. Specializing its first order to
a singleton yields `(e j + 1)` on the left and `(d j + 1)` on the right.
Singleton-product simp rules and commutative addition normalize the result.
This directly expresses the mathematical relationship in two proof lines.
Term mode would expose a cumbersome equality transport; terminal simpa is
clearer. No extraction, statement restatement, or new API is necessary.

Live attempts tested: grind, simp [hasseCoeff], aesop, exact?, apply?, composition
specialization with and without classical, removal of add_left_comm, and removal
of mul_comm. The specialization succeeds without classical. Removing
add_left_comm leaves different parenthesized exponent sums. Removing mul_comm
also leaves factors reversed. Original terminal ring alternatives: lia and grind
succeed; simp [mul_comm, mul_left_comm, mul_assoc] succeeds with an unused
mul_left_comm warning; linear_combination is unavailable. An initial terminal
probe accidentally targeted blank L213, was rejected as command syntax, and was
rerun at correct L212. Those blank-line errors count as no proof evidence.

Live multi_attempt reports “No goals to be solved” on the *next original tactic*
when a replacement closes early. Success is therefore confirmed independently
by the prefix-only compiler probe, not inferred from an empty goals array alone.
The first scratch metadata probe used nonexistent pp.width and failed only on
that option; the corrected format.width run exited zero.

Experiment artifacts: `/private/tmp/decl17-goal.json`, `decl17-simpa.json`,
`decl17-terminal-correct.json`, `decl17-isolation.lean`, and the four
`decl17-drop_*.lean` files. No scratch file is in the repository root.

## Final validation and gates

All validation below ran on 2026-10-15 after the selected source edit. The source
was reread immediately before the contextual apply_patch. The source diff is
exactly the target proof body; automated comparison to the worker snapshot
confirmed both surrounding file regions and the complete signature are
byte-identical. No declaration name, definition, import, version, or docstring
changed. Final proof-line widths are 72 and 54 codepoints.

- `lake build Roth.HasseDeriv`: **exit 0**, module built in **9.9s**, 1430 jobs.
  Sole warning is preexisting `Roth/HasseDeriv.lean:1:1 Copyright too short!`.
- Complete fresh `lean_diagnostic_messages`, file path absolute, timeout 45s:
  **success=true, partial=false, timed_out=false, failed_dependencies=[]**.
  Only the same L1 copyright warning; zero errors and no target diagnostics.
  Raw evidence: `/private/tmp/decl17-final-diagnostics.json`.
- Final `lean_goal` at L192: **goals_before=[], goals_after=[]**, complete tool
  result, no error. Raw evidence: `/private/tmp/decl17-final-goal.json`.
- `lake env lean /private/tmp/decl17-isolation.lean`: **exit 0** after removing
  classical. This contains only the original module prefix and the replacement
  target, followed by type/axiom probes. No original target proof or subsequent
  declaration is available to the replacement.
- `lake env lean /private/tmp/decl17-original-check.lean`: **exit 0**.
  Original and final `#check @hasseCoeff_mul_succ` types agree. Both
  `#print axioms hasseCoeff_mul_succ` return exactly
  **[propext, Classical.choice, Quot.sound]**; no sorryAx or new axiom.
- `lake env lean /private/tmp/decl17-identifiers.lean`: **exit 0**; imported
  final built module and checked all external identifiers in added proof lines.
- `git diff --check`: **exit 0**. Target scan: no sorry, admit, set_option,
  haveI, letI, push_neg, ASCII lambda arrows, ≥, or > relation.

The direct MCP helper logs an event-loop cleanup warning on process exit, after
successful complete result emission. That warning is not a Lean diagnostic;
the returned diagnostics and compiler builds above are the proof evidence.

### New-identifier verification

| Identifier in added lines | Verification | Result |
|---|---|---|
| hasseCoeff_mul_hasseCoeff | Existing preceding private declaration; prefix-only compilation uses it | pass |
| MvPolynomial.hasseCoeff, Finsupp.single | Explicit `#check` in identifiers probe | pass |
| add_comm, add_assoc, mul_comm | Explicit `#check` in identifiers probe | pass |
| add_left_comm | Local search returned specialized source matches with unavailable index; generic explicit `#check` confirms AddCommSemigroup theorem | pass |

### Gate status — hasseCoeff_mul_succ (Phase 4)

| Gate | Result | Exact evidence |
|---|---|---|
| lake_build_file | pass | `lake build Roth.HasseDeriv`, exit 0, 9.9s, header warning only |
| definition_protected | pass | No def/abbrev changed; surrounding source byte-identical |
| theorem_statement_protected | pass | Full three-line target signature byte-identical |
| structure_gate | pass | Two-line body, no conjunction, no case branch |
| naming_gate | pass | Descriptive binomial successor property; no forbidden name pattern or abbreviation |
| line_packing_gate | pass | All three measured signature rows above have justified breaks; max width 88 |
| inequality_orientation_gate | pass | Occurrence table supplied; zero ≥ or > relations remain |

Overall: **pass**. No worker-level deferred gate. Full project build and
`lake build Roth.LeanEval` are owned by the parent/file owner and are not
claimed here. File-level simplify/buzz hand-offs belong to that owner too.

### Worker result

Before: **25 declaration lines / 22 body lines**. After: **5 / 2**.
Saved: **20 lines**. Two audit issues fixed: duplicated proof structure and
ASCII lambda syntax (eliminated with the obsolete argument). Refactoring
deferred: **0**. Rules applied: **1.4, 1.10, 2.3**, together with the
Step-4 whole-proof reuse strategy. All other rule statuses are recorded above.
Renames queued: **none**. Comments preserved: **none present (0→0)**.
Refactoring needed: **none**. No substantial API proposal or approval needed.

### Phase checklist

- [✓] Step 1 — full reference reads, including recovery of truncated spans.
- [✓] Step 2 — all 24 audit slots supplied before source edit.
- [✓] Step 2.5 — all five search methods attempted/status reported.
- [✓] Step 2.6 — per-parameter generalisation and inversion checks; private literature exemption recorded.
- [✓] Step 2.7 — every signature line measured before/after.
- [✓] Step 2.8 — occurrence-level inequality table supplied.
- [✓] Step 3 — all 42 golfing rules have concrete statuses.
- [✓] Step 4 — alternative proof strategy tested and independently isolated.
- [✓] Step 5a — fresh complete LSP, zero errors; preexisting file-header warning documented.
- [✓] Step 5b — all seven worker gates pass with actual module-build citation.
- [✓] Step 6a — no rename required; sidecar untouched.

## Dependent checkpoint validation

The file owner ran `lake build` and `lake build Roth.LeanEval`, sequentially;
both exited 0 (2586 and 2585 jobs). Logs:
`/private/tmp/roth-hasseCoeff_mul_succ-build.log` and
`/private/tmp/roth-hasseCoeff_mul_succ-leaneval.log`.
Existing downstream linter warnings are retained for their later file audits.
