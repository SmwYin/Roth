# Phase 4 — `digits_unique`

Dedicated target: original current L60–64, five lines; source snapshot
`/private/tmp/roth-d06-start.lean`. Only the private helper and its sole direct caller expression
were changed. No cleanup claim is made for `kroneckerExp_injOn`.

Read both installed SKILL.md files, the complete worker contract, golfing-rules.md,
proof-patterns.md, mathlib-search.md, generalisation-patterns.md, cleanup-gates.md, relevant
style-rules.md sections, mathlib-review-stages.md, and initial GenWronskian.md audit.

## Full 24-item audit

1. LINT: no warning at the target or replacement; complete final diagnostics below.
2. HAVE SCAN: target has no `have`. Replacement has one proof-bearing `have : ... := by`,
   retained because it carries the digit uniqueness argument and is used by `congrFun`.
3. SET_OPTION: none; no option introduced.
4. SIMP SQUEEZE: original `by simp`, two `by simpa`, and terminal `simpa [...] using h`
   all close their own goals. No nonterminal bare simp or terminal simp-only exists.
5. NAMING: `digits_unique` is descriptive snake_case, no forbidden abbreviation/pattern.
   Deletion makes a rename unnecessary; no renamed declaration introduced.
6. LINE PACKING: measured original two signature lines below; no target signature survives.
7. BY PLACEMENT: original `by` ends L61; replacement `by` ends its have line.
8. FORMAT: two-space proof indentation; no haveI/letI, semicolon chains, trailing whitespace,
   or empty lines inside the replacement. New lambdas use ↦.
9. COMMENTS: target had no comments. All caller/module documentation preserved verbatim.
10. DOCSTRING: n/a: private auxiliary lemma needs no docstring; no existing docstring edited.
11. VISIBILITY: private implementation helper; deleted instead of exposing an API wrapper.
12. STRUCTURE: original body three lines, no conjunction or branch; deletion requires no
    extraction. The caller replacement is a four-line proof-bearing have.
13. MATHLIB: found existing API; deleted wrapper and updated exactly one direct use.
14. JUNK DEF: n/a: theorem, not def/abbrev.
15. EXISTS LEMMA: n/a: function equality, no existential witness.
16. SHOW vs CHANGE: n/a: neither occurs in target/replacement.
17. PUSH_NEG: n/a: none.
18. GENERALISE: all original binders considered below; helper deletion supersedes changes.
19. INEQUALITY: all three bounds already use <; no reversed inequality occurs.
20. NORMAL-FORM: canonical list digit representation is `Nat.ofDigits`; use Mathlib directly
    and transfer equality through `List.ofFn_inj`, rather than maintaining another API.
21. SYNTAX-GEN: direct Mathlib theorem consumes list length, bounded digits and ofDigits
    equality. The caller's existing sum is converted by the existing sum/mapIdx API.
22. IMPORT-FANOUT: n/a: no import changes.
23. CASTS: 0 redundant casts dropped, 2 original Fin→Nat exponent coercions retained in
    the independent original-statement probe. No explicit cast was added in source diff.
24. INSTANCE-NAME: n/a: no instance declaration.

Issues found: one redundant private Mathlib wrapper. Fixed: deleted and specialized Mathlib
at its only call site. Refactoring needed: none. No public statements, definitions, docs,
attributes, imports, versions, or mathematical result changed.

## Mathlib search-status

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | uniqueness of base k digits of equal length; bounded retry via direct MCP helper | Both native/direct calls returned read-operation timeout; unavailable, not evidence of absence |
| B Loogle | `Nat.ofDigits, _ = _ → _ = _` | `Nat.ofDigits_inj_of_len_eq`, exact list API |
| C LeanSearch | Nat.ofDigits injectivity lists equal length digits less than base | `Nat.ofDigits_inj_of_len_eq`, `Nat.injOn_ofDigits`, `Nat.digits_inj_iff` |
| D Source rg | `ofDigits.*(inj\|sum)` and `ofFn_inj` in Digits/List | Defs L312; Lemmas L37; List/OfFn L189 |
| E Name pattern | `ofDigits_inj` via lean_local_search | exact source hit, index unavailable (no absence claim) |

Auxiliary variants searched: `_inj_of_len_eq`, `injOn_ofDigits`, `digits_inj_iff`,
`ofFn_inj`, `ofFn_injective`, `ofDigits_eq_sum_mapIdx`.
Common-equivalents table: no listed domain bucket matches; actual digit API establishes presence.
Rules 1/5: deleted wrapper, rather than simplifying it. Rule 2: all five methods actually
attempted; no absence claim. Rule 3: variants above. Rule 4: no custom predicate/typeclass
replacement applies. Rule 6: Mathlib usage documented here; existing module docstring is
user-protected, so no documentation mutation.

Compiled independent original statement confirms the composition of `List.ofFn_inj.mp`,
`Nat.ofDigits_inj_of_len_eq` and sum normalization. `exact?` cannot directly close the
sum-form goal; `apply?` suggests `List.ofFn_inj.mp` with a remaining list equality, an
incomplete search result (its generated sorry warning is not a verification pass).
No API extraction is needed because the required canonical API already exists.

## Generalisation status (every original parameter)

| Parameter | Class/use | Mechanical candidates considered/tried | Result |
|---|---|---|---|
| `{k : ℕ}` | data/base in bounds, powers, ofDigits | drop invalidates dependent type; Nat→abstract would change positional-base arithmetic | keep underlying concrete base in direct API |
| `hk : 1 < k` | proposition, passed to Mathlib | drop; strict→weak `1 ≤ k`; separately compile drop-hk proof by k≤1 zero-digit case | mathematically removable from helper; helper deleted, so no signature remains to weaken |
| `{n : ℕ}` | data/Fin index and sum | drop leaves dependent Fin n unbound; arbitrary finite index needs enumeration/positional ordering, a different presentation | keep at existing Mathlib `List.ofFn` specialization |
| `{f : Fin n → ℕ}` | structure value/digit function | drop leaves statement unbound; codomain fixed by Nat.ofDigits; no universe/typeclass parent applies | retained as caller's digit function |
| `{g : Fin n → ℕ}` | structure value/digit function | same dependent-type/codomain check as f, independently | retained as caller's second digit function |
| `hf : ∀ i, f i < k` | proposition/digit validity | drop; weaken < to ≤; point-localise would not cover all sum positions | carry counterexample at k=2: [2,0] and [0,1] have equal value, so invalid |
| `hg : ∀ i, g i < k` | proposition/digit validity | drop; weaken < to ≤; point-localise as for hf | symmetric carry counterexample invalidates each weakening |
| `h : ∑... = ∑...` | proposition/value equality | drop; weaken equality to one-sided ≤ | distinct bounded one-digit functions [0], [1] refute drop or one-sided inequality (swap for opposite direction) |

No section variable K/Field/σ/Fintype/l is included in the private helper's type.
The isolated `/private/tmp/roth-d06-drop.lean` drop-hk proof compiled exit0. The
`/private/tmp/roth-d06-generalise.lean` concrete carry/distinct-digit counterexample probe
also compiled exit0; these are mathematical necessity checks, not source API changes.
No type-variable/universe binder, decidability assumption, bundled hypothesis, or algebraic
typeclass exists to weaken. Inversion check: already a generic theorem about arbitrary
digit functions; its list-based generalization is exactly Mathlib's theorem, used directly.
Big-change candidates: none after deletion. The hk observation concerns only the removed
private wrapper; it does not authorize modifying the caller's public hk argument.

Literature search: n/a: private decl, literature search not required. WebSearch and ChatGPT
math MCP not required for this private implementation helper.

## Line packing

Reference `#check @digits_unique_original` at format.width 100 in independent scratch:

```lean
@digits_unique_original : ∀ {k : ℕ},
  1 < k →
    ∀ {n : ℕ} {f g : Fin n → ℕ},
      (∀ (i : Fin n), f i < k) → (∀ (i : Fin n), g i < k) → ∑ i, f i * k ^ ↑i = ∑ i, g i * k ^ ↑i → f = g
```

| Original sig line | Codepoints | Next complete token | Arithmetic | Action |
|---|---:|---|---|---|
| 60 | 94 | `(hg : ∀ i, g i < k)` (19) | 94 + 1 + 19 = 114 > 100 | ok |
| 61 | 91 | proof body next | n/a, last signature line | ok |

Final: no target signature remains; every added source line is ≤100 codepoints.

## Inequality scan

| Location | Occurrence | Rewrite | Rename |
|---|---|---|---|
| original hk | `1 < k` | none, already smaller-left | none |
| original hf | `f i < k` | none, already smaller-left | none |
| original hg | `g i < k` | none, already smaller-left | none |
| entire target/replacement | zero ≥ or > inequalities | n/a | no _ge_/_gt_ name |

## All 42 golfing rules

1.1 n/a: no by-exact wrapper; removed the whole redundant lemma.
1.2 n/a: no by-rfl.
1.3 n/a: no rw/exact chain in target.
1.4 existing terminal simpa already consolidates sum normalization.
1.5 n/a: no trailing rfl.
1.6 n/a: no constructor pair.
1.7 n/a: no apply/exact chain.
1.8 n/a: no contradiction/push_neg.
1.9 n/a: new digit lambdas compose with e.symm and cannot eta-reduce.
1.10 n/a: target has no have; replacement have has proof content.
1.11 n/a: no apply/intro.
1.12 n/a: no show.
1.13 n/a: no conjunction projections.
1.14 n/a: no sequential rw in target/replacement.
1.15 n/a: no terminal simp-only.
1.16 n/a: every simp/simpa closes its own goal.
1.17 already List.ofFn_inj.mp; no shorter object method needed.
1.18 considered; current parentheses delimit Nat theorem application inside List injection.
1.19 n/a: no push_neg.
1.20 n/a: no existential helper.
2.1 tried grind on entire original statement in isolated compile: failed unsolved equality.
2.2 n/a: no preceding grind tactics.
2.3 existing simpa is retained at direct use.
2.4 n/a: no analytic function-property goal.
2.5 n/a: conclusion is function equality, no positivity goal.
2.6 n/a: no monotonicity/inequality goal.
2.7 tried lia on whole original statement: failed, power-weighted sum is not linear arithmetic.
2.8 tried aesop: failed, no progress.
2.9 n/a: symbolic base/digits, no numeric or cross-type cast goal.
2.10 n/a: symbolic function equality is not finite concrete computation.
2.11 n/a: no division or ring identity goal.
2.12 n/a: no ring/ring_nf ending.
2.13 n/a: no symmetric case branches in target.
2.14 n/a: no calc.
2.15 n/a: different length/bounds/value subgoals use distinct short proof terms.
3.1 n/a: no erw.
3.2 n/a: no continuity/measurability tactics.
3.3 n/a: no omega; lia attempt documented in 2.7.
3.4 n/a: no rcases-rfl.
3.5 n/a: deleted private wrapper should not acquire automation attributes.
3.6 n/a: no simp_all-only.
3.7 n/a: no heartbeat options.

## Step-back reflection

Whole-proof grind/simp/aesop/lia/exact? do not establish symbolic digit uniqueness alone.
`apply?` identifies the injection transfer but leaves the actual list goal. The useful
change is removing the redundant API layer. Its two mathematical steps remain directly
at the unique use; no extra helper, import, or attribute is warranted.

## Verification and gates

Source freeze SHA256: `dff932bf70cdff2d9d0c8160f0f752cd1cdf13ba8dbdf932d375bffd81bc4a10`.
Source ownership revoked by owner after the successful gates; no later source mutation.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | `/Users/ramin/.elan/bin/lake build Roth.GenWronskian`, session82420 exit0, module32s |
| definition_protected | pass | no def/abbrev changes; snapshot unified diff inspected |
| theorem_statement_protected | pass | explicitly authorized private wrapper deletion; caller signature byte-identical |
| structure_gate | pass | original three-line body; removed helper, four-line inline argument |
| naming_gate | pass | no forbidden names or rename |
| line_packing_gate | pass | complete two-row measured table; all added lines ≤100 |
| inequality_orientation_gate | pass | full occurrence table, zero reversed inequalities |
| diagnostics | pass | `/private/tmp/roth-d06-lsp.json`: success=true, partial=false, timed_out=false, failed_dependencies=[] |

Full warning inventory: L1 missing protected copyright metadata; L36 unused section Fintype
in dependent-zero theorem; L32 unused Fintype in that theorem type; L236 unused DecidableEq
in det_sum_rows; L254 unused Fintype in existence theorem. All five are outside target;
none is hidden, suppressed, or newly introduced. No target/replacement warning.

Native multi_attempt stalled and was cancelled; individual isolated Lean compiles supplied
the automation evidence. LeanFinder direct bounded retry also returned timeout, accurately
recorded above. Other search tools succeeded. Full/separate project gates belong to owner.

Independent `/private/tmp/roth-d06-original.lean` re-proves the exact original private
statement without referring to its deleted name; exit0. `/private/tmp/roth-d06-caller.lean`
independently re-proves the caller's original type from the edited proof (no self-reference);
exit0. Both report only `[propext, Classical.choice, Quot.sound]` under `#print axioms`.
The source contains no added sorry, axiom, native_decide, or option raise.

## Result and 11-step checklist

Before 5 declaration lines; after 0; saved 5 target lines. Caller integration adds 3 lines;
net source saving 3 lines including separator removal. One issue found/fixed, no deferred
refactor. Renames queued: none. Comments preserved: none in target; caller docs unchanged.

- [x] Step 1 references read.
- [x] Step 2 full 24-item audit.
- [x] Step 2.5 five actual search methods/statuses.
- [x] Step 2.6 all-parameter generalisation and private literature exemption.
- [x] Step 2.7 per-signature-line width arithmetic.
- [x] Step 2.8 occurrence inequality scan.
- [x] Step 3 all 42 rules/statuses.
- [x] Step 4 independent step-back reflection and tactic attempts.
- [x] Step 5a complete clean LSP diagnostics with all warnings.
- [x] Step 5b actual module and source-diff gates.
- [x] Step 6a no renames required.
