# Cleanup: private `Roth.roth_product_bound_aux`

Local necessary helper of original declaration15; no independent count/publication credit.
Only this helper changed. Immediate ordinary comment and B/product proof signpost both
preserved; all preceding accepted helpers/comments/reports and the parent remain untouched.
Main outside the helper is byte-exact to entry. The same parent author must resume and
consume this API, finish its own audit/gates, and publish parent plus helpers jointly.

Before34 declaration /27 body lines; after22 /16; saved12 declaration lines.
The product bound now uses `Finset.prod_le_pow_card`, avoiding the intermediate sum bound.
Removed hm2, weakened δ and A to nonnegative and h32 to nonstrict. Conclusion unchanged;
exact original-contract recovery compiled and its actual opaque VALUE was checked.

## Provenance and doctor

Genuine FIRSTUNGOLFED was saved and SHA-verified before any helper Lean/golf:
149fa30cd6c49145b15e002993e3e30d33bbde9f5be6c5f62a36b1b0e47a0592.
Entry Main a85711f8426dae432b940c4eac896cd63e6bba5c615e111256114e4b95d9df91
included uncompiled parent adaptation; it was not falsely called a green full baseline.
Historical accepted 9ea17c… full/Eval/native/LSP evidence is reused as historical only.
First-draft exact-prefix compile/profile passed before changes. Actual changed-source FULL
and separate Eval builds plus fresh native checks and complete LSP passed below.
No unchanged baseline build was run solely for a label. No cache/linter executable added.

# Product-scale helper audit (before production changes)

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md, plus installed skills, full cleanup
and cleanup-all commands, style/naming/review/profiling references and buzz command.
Scope is this private helper; three preceding accepted helpers are frozen.
Genuine first ungolfed declaration: 34 lines, 27 body; exact saved SHA149fa30….
First draft actual scoped profile: 594.096ms; no repeat required.

1. LINT: first-prefix compile has no target warnings; complete final LSP required later.
2. HAVE SCAN (all original bindings): hlogA/hlogα each have nested by-linarith, single use in h32'; replace log-bound subproofs by le_add_of_nonneg_right and inline;
   hm1 by-block single use keep or replace via NeZero; hmR' by-block used twice,
   replace Nat.cast_nonneg directly. h32' by-block keep; two anonymous nonneg products
   used once each by linarith, keep as tactic inputs (proof content). hX has nested by-linarith, one use,
   inline in sqrt_lt_floor. hBpos no-by one use inline in final tuple. hsumr has nested by-simp,
   one use, eliminate through direct prod_le_pow_card. hN by-block one use, replace
   final component proof; h1 by-block needed as cast source or replace direct product
   API; h2 by exact_mod_cast one use keep bridge; h3 has nested by-norm_num, one use inline/eliminate.
3. SET_OPTION: none.
4. SIMP: only terminal simp in sum constant cardinality; no squeezing needed; direct
   product API will use terminal simpa. No nonterminal simp.
5. NAMING: roth_product_bound_aux descriptive snake_case private auxiliary, no forbidden
   abbreviations/patterns. No rename.
6. PACKING: original line 2 can absorb hr0max; final repack and per-line arithmetic due.
7. BY: end of preceding line throughout.
8. FORMAT: replace lambda => with ↦; two-space proof/four-space signature; no blank lines.
9. COMMENTS: preserve both immediate ordinary comment and B/product signpost, reanchor.
10. DOCSTRING: private helper has none; retain none.
11. VISIBILITY: private auxiliary needed only by parent.
12. STRUCTURE: one coherent common-scale stage, three jointly consumed bounds share the
    same B and logarithmic inequality. Body27≤30, no branch >10. Splitting the conjunction
    duplicates premises and shared floor setup; explicit scoped exception preserving
    meaningful mathematical stage, no extra single-use wrappers.
13. MATHLIB: five methods performed. LeanFinder query finite product(n+1) vs powers,
    returned rising factorial partials only. Loogle prod_le_pow_card gave generic
    Finset.prod_le_pow_card. LeanSearch bounded finite product confirmed same and
    Multiset variant. Source search verified exact theorem; local-name search found
    Finset and Multiset variants (index unavailable, positive source hits). Supporting
    Nat.lt_two_pow_self and prod_pow_eq_pow_sum considered. Generic product bound
    replaces sum/power/product manual chain. Roth-specific B₁/four_lt_rpow and
    three_small_factors are upstream project API, not a mathlib duplicate claim.
14. JUNK DEF: n/a lemma, local B alias removable.
15. EXISTS: n/a no existential witness wrapper.
16. SHOW: original term-mode show cast lower bound is load-bearing, not tactic show;
    remove by direct hm1 proof annotation.
17. PUSH_NEG: none.
18. GENERALISE: supported tests remove hm2 (NeZero already supplies1≤m), weaken
    hδ0 to0≤δ (only .le used), hA1 to0≤A (only log nonneg and three_small_factors).
    Every other binder: m essential to Fin m, B exponents and coefficient; NeZero
    essential to index0 and1≤m (cannot simply delete well-formedness instance);
    α essential to h32 only, fixed real abs/log API prevents abstract field substitution;
    A essential to h32, log nonneg and upstream factors; δ essential to B/rpow/h32,
    fixed real-power API; q essential B and log; r essential B/product and monotone
    maximum; hr0 essential four_lt_rpow and small factors (strictness used upstream);
    hr0max essential product bound (weaker conclusion-side global bound would restate
    intended input); h32 essential positive floor and strict small-factor bound, try
    weak version separately if supported. No universe variables to generalise. No
    concrete-object inversion: B₁ floor-specific setup used directly, abstract replacement
    would merely restate sqrt/floor and upstream small-factor API. Private literature n/a.
19. INEQUALITY: zero reversed inequality occurrences: no ≥/> in signature.
20. NORMAL FORM: standard ordered real bounds and Finset product, no competing predicate.
21. SYNTAX: jointly destructured scale bounds suit caller, weaker premises improve use.
22. IMPORT FANOUT: n/a no imports added.
23. CASTS: natural→real casts bridge product/floor/rpow; retained until checked. Redundant
    local B ascriptions disappear with alias. All literals target Nat/Real as required.
24. INSTANCE NAME: n/a no declared instance; anonymous NeZero binder retained.

Preliminary reflection: a single general tactic cannot synthesize Roth-specific analytic
floor and power estimates unaided. Existing named upstream estimates plus direct finite
product order API is the short mathematical path. No optional helpers/generalisation.
Simplify skill unavailable; manual substantive scope review performed, not invocation.


## Per-binder mechanical review

|Original binder|Class/use|Bounded candidate and result|
|---|---|---|
|m : ℕ|Dimension and numerical coefficient|Keep; Nat/Fin/cardinality are integral to this stage.|
|[NeZero m]|Instance for index0 and1≤m|Keep; deleting loses index0 well-formedness and positivity.|
|hm2 : 2≤m|Used only to infer1≤m|Remove: Nat.one_le_iff_ne_zero from existing instance; compiled.|
|α : ℝ|Absolute/log term in h32|Keep; real analytic API, not an abstract field theorem.|
|A : ℝ|Log term and nonnegative coefficient scale|Keep; numeric parameter, type follows log API.|
|δ : ℝ|B₁ and real powers|Keep; concrete real power/floor API.|
|hδ0 :0<δ|Only passed as .le|Weaken to0≤δ; compiled.|
|hA1 :1≤A|Log nonnegative and small factors|Weaken to0≤A, rename local binder hA; compiled.|
|q :Fin m→ℕ|q0 supplies denominator scale|Keep; scalar restatement changes application interface unnecessarily.|
|r :Fin m→ℕ|Degree product and maximum|Keep; Fintype/cardinality restatement outside supported mechanical scope.|
|hr0 :0<r0|Strict power and small factors|Keep; r0=0 forces all rj=0 and would demand1<1.|
|hr0max|Every product factor bounded by maximum|Keep; dropping permits arbitrarily large other factors.|
|h32 :strict log bound|Only weak numerical bound required|Weaken < to≤; compiled.|

No type-variable/universe binder to generalise. No additional companions/extractions.
Private literature search n/a. Three premise weakenings and hm2 removal were tested
in the scoped candidate; changing only h32 from < to≤ also passed the corrected
whole-goal automation-negative trial. The final FULL build verifies them together.

## Line packing

Every width below is codepoints. Syntactic units are complete binders or complete
inequality-side expressions, not individual lexical symbols. All signature lines included.

Before:
|Signature line|Codepoints|Next syntactic unit|Arithmetic|Action|
|---|---:|---|---|---|
|1|81|`(hδ0 : 0 < δ)`|81+1+13=95 ≤100|repack|
|2|65|`(hr0max : ∀ j, r j ≤ r 0)`|65+1+25=91 ≤100|repack|
|3|29|`(h32 : 2 * m + 1 + 2 * m * Real.log (1 + A) + 2 * m * Real.log (1 + |α|) < δ ^ 2 * Real.log (q 0))`|29+1+98=128 >100|ok|
|4|78|`δ ^ 2 * Real.log (q 0))`|78+1+23=102 >100|ok|
|5|60|`(B₁ δ (q 0) (r 0) : ℝ) ≤ (q 0 : ℝ) ^ (δ * r 0) ∧`|60+1+48=109 >100|ok|
|6|54|`(∏ j, ((r j : ℝ) + 1)) < (B₁ δ (q 0) (r 0) : ℝ) ^ δ := by`|54+1+57=112 >100|ok|
|7|63|``|end of signature|ok|

After:
|Signature line|Codepoints|Next syntactic unit|Arithmetic|Action|
|---|---:|---|---|---|
|1|94|`{q r : Fin m → ℕ}`|94+1+17=112 >100|ok|
|2|63|`(h32 : 2 * m + 1 + 2 * m * Real.log (1 + A) + 2 * m * Real.log (1 + |α|) ≤ δ ^ 2 * Real.log (q 0))`|63+1+98=162 >100|ok|
|3|78|`δ ^ 2 * Real.log (q 0))`|78+1+23=102 >100|ok|
|4|60|`(B₁ δ (q 0) (r 0) : ℝ) ≤ (q 0 : ℝ) ^ (δ * r 0) ∧`|60+1+48=109 >100|ok|
|5|54|`(∏ j, ((r j : ℝ) + 1)) < (B₁ δ (q 0) (r 0) : ℝ) ^ δ := by`|54+1+57=112 >100|ok|
|6|63|``|end of signature|ok|


Actual `#check @Roth.roth_product_bound_aux` with format.width100 from regular final capture:

```lean
@Roth.roth_product_bound_aux : ∀ {m : ℕ} [inst : NeZero m] {α A δ : ℝ},
  0 ≤ δ →
    0 ≤ A →
      ∀ {q r : Fin m → ℕ},
        0 < r 0 →
          (∀ (j : Fin m), r j ≤ r 0) →
            2 * ↑m + 1 + 2 * ↑m * Real.log (1 + A) + 2 * ↑m * Real.log (1 + |α|) ≤ δ ^ 2 * Real.log ↑(q 0) →
              0 < ↑(Roth.B₁ δ (q 0) (r 0)) ∧
                ↑(Roth.B₁ δ (q 0) (r 0)) ≤ ↑(q 0) ^ (δ * ↑(r 0)) ∧ ∏ j, (↑(r j) + 1) < ↑(Roth.B₁ δ (q 0) (r 0)) ^ δ
```

|Inequality scan occurrence|Disposition|
|---|---|
|All signature/hypothesis occurrences|0 reversed ≥/> occurrences; smaller-left orientation.|

## All golfing rules and step-back review

# All 42 golfing rules

| Rule | Actual disposition |
|---|---|
|1.1|No by-exact wrapper at declaration end; cast by-block has tactic content.|
|1.2|No by-rfl proof.|
|1.3|No consecutive rw/exact equivalent after product API change.|
|1.4|Terminal simpa uses product/card identities; no following exact to consolidate.|
|1.5|No simp then rfl.|
|1.6|Original final triple becomes refine triple with analytic third goal.|
|1.7|No apply/exact chain.|
|1.8|No contradiction/negation block.|
|1.9|Lambdas genuinely depend on j, no eta lambda.|
|1.10|hlogA,hlogα,hmR',hX,hBpos,hsumr,h3,hN aliases removed/inlined. Final hm1,h32',hprod,hprodR each contain substantive proof and kept. Anonymous have products are linarith input certificates.|
|1.11|No apply/intro chain.|
|1.12|Removed old term-show lower-bound bridge via direct Nat.one_le_iff_ne_zero API.|
|1.13|Destructure sqrt bound directly; use small-factors .1 once, avoiding named tuple.|
|1.14|No adjacent rw calls.|
|1.15|No terminal simp-only left.|
|1.16|No nonterminal bare simp.|
|1.17|Use .trans, .trans_lt, .trans_le directly.|
|1.18|No single terminal parenthesized by proof benefits; arguments are nested chain terms with necessary parentheses.|
|1.19|No push_neg.|
|1.20|Not existential witness helper.|
|2.1|Actual isolated fail_if_success grind verified whole-goal failure before real proof.|
|2.2|No grind retained.|
|2.3|Terminal simpa using prod_le_pow_card supplies cardinality normalisation directly.|
|2.4|No function-property goal.|
|2.5|Original positivity m cast replaced direct Nat.cast_nonneg. Square-root nonneg is API theorem; strict B positivity uses hsqB, so blind positivity lacks premise.|
|2.6|Direct Nat.pow_le_pow_right discharges monotonicity; gcongr would be a wrapper around the same theorem, no long inequality block left.|
|2.7|Nat linear bound uses Nat.one_le_iff_ne_zero.2 directly; no arithmetic tactic remains.|
|2.8|Actual solve-aesop failed whole-goal closure; no search left in production.|
|2.9|norm_num supplies 2≤4 and base2≥1; exact_mod_cast proves degree product bridge.|
|2.10|No finite decidable arithmetic proposition except literal comparisons already norm_num. No native_decide.|
|2.11|No denominator ring identity.|
|2.12|No ring/ring_nf goal or polynomial identity.|
|2.13|No symmetric cases.|
|2.14|No calc chain left; direct transitivity.|
|2.15|Triple fields have different proof roles; close two directly and leave third.|
|3.1|No erw.|
|3.2|No continuity/measurability.|
|3.3|Removed original omega via direct Nat.one_le_iff_ne_zero; no lia required.|
|3.4|No rfl cases.|
|3.5|Private one-use scale result, no global automation attribute warranted.|
|3.6|No simp_all-only.|
|3.7|No resource-option raises.|

Step-back: the product is bounded pointwise by2^(r0), so cardinality gives the desired
2^(m*r0) in one existing API call. This removes the sum-bound argument, three aliases,
and the unnecessary local B alias. The floor and small-factor estimates are precisely
the existing upstream analytic interface. Whole-goal exact? also failed in the same
compiled probe. No API extraction, branch extraction, renames, or imports needed.

Truthful failed probes: first candidate used unqualified `univ` and failed; fixed to
Finset.univ and passed. First automation-negative probe used fail_if_success aesop,
which counts non-closing success and was rejected; corrected to solve|aesop and passed.
No failed trial was ever installed in production. No sorries/axioms/limit raises.

Final HAVE scan: hm1 by exact_mod_cast, used by linarith; h32' by-block used in
four_lt_rpow; two anonymous product-sign facts used by linarith; hprod by-block used
as cast source; hprodR by-block used in final transitivity. All substantive by-blocks,
no single-use no-by aliases left. sqrt pair destructuring feeds two result fields.


## Gates and validation

|Gate|Actual result|
|---|---|
|FULL|`lake build`, exit0,50.116s; final-full-build-terminal.json.|
|Separate Eval|`lake build Roth.LeanEval`, exit0,25.799s.|
|Fresh native Main/Eval/root|`lake env lean Roth/Main.lean`,36.180s; `Roth/LeanEval.lean`,27.127s; `Roth.lean`,26.391s; all exit0.|
|Complete LSP Main/Eval/root|Unfiltered, partial=false, timed_out=false, success=true;0errors. Main only pre-existing line1 copyright warning; Eval/root empty.|
|definition_protected|No def/abbrev or import changed.|
|theorem_statement_protected|Only audit-declared supported private weakenings; exact conclusion retained, original-contract recovery passed.|
|structure_gate|16body lines, no >10line branch. Coherent common B-scale conjunction deliberately retained per scoped instruction; shared floor/log bounds make splitting duplicate the stage.|
|naming_gate|Descriptive private snake_case _aux, no forbidden patterns; no rename.|
|line_packing_gate|All6 final signature rows arithmetic-ok above.|
|inequality_orientation_gate|0 reversed inequalities in code; table above.|
|scope/comments|Outside target byte-exact; both comments preserved.|
|new identifiers|Finset.prod_le_pow_card verified by Loogle/LeanSearch/local-name/source; Nat.one_le_iff_ne_zero and Nat.pow_le_pow_right resolved in actual compiled proof; no unresolved identifier.|
|casts|No redundant same-type ascriptions introduced; Nat→Real bridges for q,r,B retained; `(1:ℝ)` and `(2:ℝ)` pin real target arithmetic. Local B alias/ascriptions removed.|
|limits/trust|No limit raises, sorry, axioms, native_decide, or profiling scaffolding in production.|
|caller impact|No current helper call sites (definition only); full dependent build/native/LSP passed. Parent consumption and parent audit remain later author work.|

## Independent/contract/semantics

Independent proof imports only Roth.MainLemma and uses the original sum-of-degrees/product
power strategy, distinct from the new uniform-product bound. Independent build exit0,
32.682s. Recovery preserves the exact genuine old contract and applies the weakened helper;
recovery fixed build exit0,65.049s (expected scratch unused-hm2 warning).

Complete actual families/universes were enumerated before per-row guards:
production root[] plus `_simp_1_1`[`u_2`]; independent root[]; recovery root[].
All4 actual opaque theorem VALUES were inferred in memory, closed/no admits, standard
axioms only propext/Classical.choice/Quot.sound, with defaults200000/20000/512. Every actual
external origin is strictly upstream of Main; the fresh local graph is acyclic. No self,
production→independent/recovery or independent→production/recovery edges. No broad imported
DAG replay or unchanged-helper clone/reproof was used. Full raw VALUES not dumped; small
hash/length receipts only; no VALUE identity claim.

Strict complete root TYPE comparison uses recursive Name/Level/BinderInfo/metadata/literal/
projection/Expr checks with no ExprBEq shortcut. Initial concrete raw TYPE mismatches were
exactly anonymous second-forall instance-name hygiene. Two actual literal Name pairs:
old `_stdin2371898401/hyg5`→recovery `RecoverProductBound386675664/hyg5`, and independent
`IndependentProductBound4062995913/hyg5`→current `Roth.Main2371898401/hyg5`.
All names have macro scopes and erase to inst, at actual path forall.body.forall.name,
BinderInfo.instImplicit. Original raw TYPES remain unequal; all remaining complete raw
TYPE bytes and recursive fields equal. TYPE-only finite supplement exit0,38.340s.
Exact original-contract recovery VALUE provides the old→new API implication.

The regular final profile supplied actual target and generated TYPES/universes. Generated
simp TYPE is full raw/recursive exact; root differs only by actual current/profile second
binder Main↔_stdin2371898401/hyg5. TYPE-only complete-family binding exit0,42.781s;
no VALUE reinference. Old genuine family2 VALUES were checked in first-draft capture.

Truthful failed checks: first candidate unqualified univ fixed before production; negative
aesop harness changed to require closure; first recovery direct dotted numeric private Name
failed and was replaced by exact actual private-name resolution; first semantic aggregate
exit1 due to pasted unquoted Name._@ in scratch old TYPE, with4 successful VALUE rows
preserved; quoting-only TYPE supplement exposed expected strict raw mismatch; final finite
TYPE supplement passed. No failed aggregate is presented as an unqualified whole-pass.

## Simplify and performance

Built-in simplify unavailable, so no invocation claimed. Manual substantive review covered
reuse, coherent scale-stage structure, aliases, all binders, casts, comments, trust, and
current caller needs. No further supported changes remain in this scope; fresh whole-file
simplify/audit/capture remains a later parent/file obligation.

Genuine first draft594.096ms; final739.036ms. Final is slower but below1000ms and below
750ms repeat trigger; no extra unchanged capture or speedup claim. Exact imports/preceding
commands and target prefix bind each measurement to its actual source. Full canonical
payload, actual families, separate stdout/stderr, disjoint outer/proof/kernel-parent/lint
roots captured; nested nodes not double-counted; no compiler or lazy prior DATA roots here.

|Final disjoint root|ms|
|---|---:|
|Source outer command|88.352|
|Async proof|621.141|
|Generated kernel parent|0.199|
|Root kernel parent|8.584|
|Lint|20.760|
|Total|739.036|

Actual expanded private-theorem payload was bound by an indexed narrow2MB read before the
outer root. Accepted expandLemma/Lean recursive elabCommand trace evidence was reused with
both source-file hashes checked exact: inner final88.101ms is included in outer88.352ms,
not added again. Genuine first inner62.654ms similarly inside outer62.713ms.

Both profile phases followed HOLD→ACK before prep, safe environment bytes in memory only,
actual driver/child-group drain terminal0/absent and defaults/freeze PASS while RAWUNPARSED,
then explicit OWNERRELEASE before parsing. First driver23672/groups23675,23699,23724,23783,
23807; final driver25083/groups25086,25110,25136,25232,25256 all absent. No full environment
or unrelated arguments persisted. No repeat required for either accepted timing.

## Phase checklist and handoff

|Phase|Status|
|---|---|
|Prepare/reference reads|Complete; installed skills/full commands/mandatory references.|
|24item audit/HAVE/per-binder/search|Complete above.|
|42 golfing rules/reflection|Complete, all applicable bounded actions resolved.|
|Packing/inequality/naming/structure|Complete above; no rename queue entries.|
|Refactoring5a/5b|Supported private premise weakening applied; no other refactoring or renames.|
|Build/native/LSP/diff gates|Pass with documented pre-existing header warning.|
|Strict semantics/independent/recovery|Pass with explicitly finite actual hygiene exceptions and prior failed-probe qualifications.|
|Simplify|Manual substantive substitute; unavailable built-in not invoked.|
|Buzz|739.036ms<1000; no >=750 repeat trigger, no deferral/scaffolding.|
|Report|Complete; final actual drain/END receipt accompanies handoff.|

Final Main SHA: fa572ddfd97ea163a48745735d7720e3bb99e8142ad96078ee63e1733bc7ea57.
Final helper SHA (newline included): 4a6e57cc38881802d118e92d87461beb606220cfce781f458bf16f60fafa6f74.

Caller API for same parent author:
`roth_product_bound_aux hδ0.le (zero_le_one.trans hA1) (hr0 0) hr0max h32.le`.
No Git/shared progress changes, no parent audit credit, no standalone publication.
