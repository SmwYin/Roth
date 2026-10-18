# Dedicated cleanup: `Roth.degreeOf_map_intCast_real`

## Scope and result

Original private declaration #5/35, baseline `2b64544bf9f77a8ff957bf1bcaf693ac72217ff6`,
original lines 67–69; worker start HEAD `7c36b31`, lines 64–66. Only this helper and the two
necessary caller proofs (`indexSet_bddAbove`, `Θ_le_card`) were edited. No new helper.
Deleted the specialization; both callers use `MvPolynomial.degreeOf_def` and
`MvPolynomial.degrees_map_of_injective` directly on the entire degree-bound family.
The protected public signatures, instances and hypotheses remain unchanged. In particular,
all positivity/decidability assumptions remain. No public amendment was applied.

The helper had 3 declaration lines; it now has 0. Two caller proof arguments each gain 2
lines, offsetting the deleted helper and separating blank line: file 981 → 981 lines.
This removes specialized API rather than claiming a line-count win. Retaining the helper
would preserve two shorter call expressions, but the direct alternative needs only one
terminal `simpa` per caller and avoids a local theorem to maintain. The owner accepted this
bounded direct-specialization direction. No congrArg scaffolding is repeated.

Frozen source SHA256: `526ebb8e1c0616d69da8eda215feb13677a245e758521e519d0d483e379e5ae7`.
No source mutation after this freeze. No Git mutations or shared-report/queue writes.

## References, baseline and mathematical reading

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md and cleanup-gates.md, the Lean/mathlib-quality skills, cleanup
worker workflow, profiling reference and relevant declaration formatting/naming/style sections.
References used the required `/Users/ramin/.local/share/roth-mathlib-quality/` root.

The owner supplied a built checkpoint and exclusively granted this compiler/LSP window.
The baseline bounded direct unfiltered LSP returned partial=true, timed_out=true while late
Theta declarations were elaborating; it is NOT a successful complete gate. No diagnostic
on the original helper. Raw response `/private/tmp/roth-degree-baseline-lsp.json`.
The native live multi-attempt stalled and its execution was terminated after a bounded wait;
no result was invented. Independent compiled tactic probes replaced that exploration.
The fallback baseline session ended and was drained before later verification.

Mathematics: an injective coefficient map preserves the support and therefore each variable's
maximum exponent. Mathlib packages the stronger invariant as equality of `degrees` multisets.
Taking the count of a variable is exactly `degreeOf_def`; rewriting the whole family transports
the existing per-variable bounds. No Roth-specific theorem or analytical property is required.

## Full 24-item audit

| # | Item | Finding/action |
|---|---|---|
| 1 | LINT | No helper warning in baseline; full final diagnostics recorded below. Preserve unrelated warnings under scope. |
| 2 | HAVE SCAN | Original helper and replacements have no `have`. |
| 3 | SET_OPTION | None in target; no source option or limit added. |
| 4 | SIMP SQUEEZE | Original has no simp. Each new simpa is terminal and intentionally unsqueezed. |
| 5 | NAMING | Standard degreeOf/map/intCast naming, no forbidden numbered pattern or abbreviation. Deleted; no rename queue action. |
| 6 | LINE PACKING | Both original signature lines measured below; final helper has no signature. Added proof lines max 82 codepoints. |
| 7 | BY PLACEMENT | Original by ends conclusion line; nested new `(by` closes its line. No isolated standalone by command. |
| 8 | FORMAT | Two-space proof indentation; nested simpa continuation indented; no blank proof line, haveI/letI, or tactic chain added. |
| 9 | COMMENTS | All 42 comment blocks/line comments preserved byte-for-byte and in order. Helper has none. |
| 10 | DOCSTRING | Private helper correctly has none. Existing public/module docs unchanged by explicit protection. |
| 11 | VISIBILITY | Private specialization removed. No public visibility changes. |
| 12 | STRUCTURE | One original tactic, no conjunction/branch. Caller bodies remain ≤7 lines, below 15-line headline and 30-line other limits. No >10-line branch. |
| 13 | MATHLIB | General degrees-map equality supplies the invariant; use directly at both callers. Actual five-method search below. |
| 14 | JUNK DEF | n/a: lemma, no data definition. |
| 15 | EXISTS LEMMA | n/a: equality, no existential conclusion. |
| 16 | SHOW/CHANGE | Neither occurs. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | All 3 effective binders have compiled drop probes; generic semiring/injective-hom version compiles. No new public API. |
| 19 | INEQUALITY | Original is equality, no reversed inequalities; caller bounds retain ≤ and <. |
| 20 | NORMAL-FORM | Mathlib's canonical generic multiset-degree equality transported through degreeOf_def. |
| 21 | SYNTAX-GEN | Whole family rewriting avoids introducing a variable/lambda merely to transport each bound. |
| 22 | IMPORT-FANOUT | No imports added. |
| 23 | CASTS | No coercion expression introduced; ℝ in Int.castRingHom fixes the coefficient-map target and is load-bearing. |
| 24 | INSTANCE-NAME | n/a: no instance introduced or modified. |

Issue fixed: unnecessary private coefficient-cast degree specialization. No extraction/rename
or public generalisation is deferred for this declaration.

## Five actual Mathlib searches

| Method | Actual query | Observed result |
|---|---|---|
| A Lean-Finder | `degree in a variable of multivariate polynomial mapped by injective ring homomorphism` | degrees_map_of_injective plus rename variants. |
| B Loogle | `MvPolynomial.degreeOf, MvPolynomial.map` | Completed empty result; no global absence inference. |
| C LeanSearch | `The degree in each variable of a multivariate polynomial is unchanged under an injective map of coefficients` | degrees_map_of_injective; univariate degree_map_eq_of_injective and rename variant. |
| D source rg | `degreeOf_map`, `degreeOf.*map`, `map.*degreeOf`, followed by `degrees_map` and `degreeOf_def` in MvPolynomial | Degrees.lean:196 degrees_map_of_injective; :220 degreeOf_def; :177 degrees_map_le. No textual direct degreeOf_map hit. |
| E native local name search | `degreeOf_map` | Returned local specialization in Theta/MainLemma, index=unavailable; source-positive hits only, NOT absence evidence. |

Auxiliary forms checked: degrees_map_le, degrees_map_of_injective, degreeOf_def,
degreeOf_le_iff, support_map_of_injective, rename and univariate degree-map variants.
Common-equivalents table has no relevant topology/finiteness bucket.
Conclusion: Mathlib provides the more general invariant; delete local specialization and
specialize directly. No claim of global absence and no new theorem needing an absence claim.
Raw native search results: `/private/tmp/roth-degree-searches.json`. All five calls completed; missing local index is explicitly bounded evidence.
New identifiers are source-verified and independently `#check`-verified in the original probe;
the actual module build also checks their concrete uses. Strict replacement rules observed:
no replacement wrapper/custom predicate; all methods and variants tried; original deleted;
Mathlib usage documented here while protected module documentation remains untouched.

## Effective binders, compiled weakening/drop probes, inversion and literature

Independent positive probe `/private/tmp/roth-degree-original.lean` copies the exact original
statement and original support-based proof under `original`; it does not invoke either
current caller or an existing local target. `#print original` exhibits its actual proof value.
Its fully elaborated type at format.width=100 is:

```lean
∀ {σ : Type u_1} (R : MvPolynomial σ ℤ) (j : σ),
  degreeOf j ((map (Int.castRingHom ℝ)) R) = degreeOf j R
```

The fresh σ shadows the file's ambient σ: Fintype and DecidableEq are NOT effective helper
binders, as independently elaborated above. They therefore cannot silently be dropped from
any consumer in this cleanup.

| Effective binder | Classification/use | Actual compiled candidate | Result |
|---|---|---|---|
| `{σ : Type*}` | Type variable, variables of R | drop_sigma under autoImplicit=false; Sort* weakening; generic universe-polymorphic semiring proof | Drop: unknown σ; Sort*: MvPolynomial requires Type, not arbitrary Sort. Already universe-polymorphic, no finite/decidable assumption. |
| `(R : MvPolynomial σ ℤ)` | Structure value whose degrees are compared | drop_R; generic changes coefficient rings to arbitrary CommSemiring A/B and map to injective f | Drop: unknown R. Generic equality compiles; abstraction already supplied by Mathlib and not retained locally. |
| `(j : σ)` | Structure value selecting degree coordinate | drop_j; whole-family transport in actual callers; generic arbitrary j | Drop: unknown j. All-coordinate transport compiles in actual callers; no pointwise/global premise to weaken. |

Negative probes in `/private/tmp/roth-degree-negative.lean` intentionally fail; no negative
probe is used to certify axioms or proof soundness. These are dependent data parameters,
not dispensable logical hypotheses. There are no explicit class/propositional premises,
strict-to-weak inequalities, bundled equivalence or continuity/localisation conditions to try.

Generic positive proof works with arbitrary A,B,σ, CommSemiring A, CommSemiring B,
f:A→+*B and injectivity, without finiteness or decidability assumptions. Inversion check:
YES, support preservation forgets ℤ/ℝ; the generic degrees-map API already is the abstraction.
No new generalized helper or public-contract candidate is needed.
Literature: n/a, original declaration private; public-literature requirement does not apply.
Caller proof maintenance does not audit/amend their protected public hypotheses.

## Measured signature packing and inequalities

All widths are Unicode codepoints. Every original signature line included:

| Original line | Chars | Next signature token | Arithmetic | Action |
|---|---:|---|---|---|
| 64 | 84 | degreeOf (8) | 84+1+8=93≤100; complete next fragment would be 84+1+59=144 | Could start fragment earlier; entire declaration deleted instead. |
| 65 | 63 | none, boundary := by | n/a | Deleted. |

Final helper signature table: zero rows, declaration absent; no retained repack row.
Existing consumer headers preserved; exact effective public types independently compiled below.

| Occurrence | Location | Original | Rewrite/rename |
|---|---|---|---|
| none | Original signature and all 3 binders | no ≥ or > ordered inequality | n/a; no _ge_/_gt_ name |
| retained | Caller degree bounds and positivity | ≤ / < | already smaller side left |

## All 42 golfing rules

| Rule | Status/reason |
|---|---|
| 1.1 by exact | n/a, no wrapper. |
| 1.2 by rfl | n/a, no reflexivity tactic proof. |
| 1.3 rw+exact | n/a, original single rw; direct terminal simpa replaces wrapper usage. |
| 1.4 simp+exact | Applied transport as terminal simpa using existing hRd family. |
| 1.5 trailing rfl | n/a, no trailing reflexivity. |
| 1.6 constructor chain | n/a, equality helper. |
| 1.7 apply+exact | n/a, no apply. |
| 1.8 contradiction | n/a, no by_contra. |
| 1.9 eta lambdas | Removed coordinate lambda at both call sites; transport family directly. |
| 1.10 single-use have | n/a, none. |
| 1.11 apply+intro | n/a, none. |
| 1.12 show | n/a, none. |
| 1.13 projections | n/a, none in target. |
| 1.14 consecutive rw | Original already one rw list; no merger needed. |
| 1.15 terminal simp only | New terminal simpa deliberately unsqueezed. |
| 1.16 nonterminal simp | n/a, none introduced. |
| 1.17 dot notation | Original caller .trans_le replaced by family rewrite; no remaining opportunity. |
| 1.18 trailing parentheses | Parentheses group a proof argument to index_le_card before final argument, required. |
| 1.19 push_neg | n/a, none. |
| 1.20 existential lemma | n/a, no existential. |
| 2.1 grind | Independent fail_if_success grind verified failure on original goal; direct API preferred. |
| 2.2 delete-before-grind | n/a, original contains no grind chain. |
| 2.3 simpa consolidation | Applied whole degree-bound family rewrite at two uses. |
| 2.4 fun_prop | n/a, no analytic function property goal. |
| 2.5 positivity | n/a, equality of polynomial degrees; caller result is upper bound, not positivity. |
| 2.6 gcongr | Degree-map invariant needed, not arithmetic monotonicity; direct equality transport suffices. |
| 2.7 lia/omega | n/a, arbitrary polynomial degrees not related by bare linear arithmetic. |
| 2.8 aesop | Independent fail_if_success aesop verified failure on original equality. |
| 2.9 norm_num/norm_cast | Exact cast map is handled by generic injectivity; no numeric evaluation/cast equality to normalize. |
| 2.10 decide | n/a, universally quantified polynomial invariant; not finite decidable computation. |
| 2.11 field_simp/ring | n/a, no denominators or ring identity. |
| 2.12 linear_combination | n/a, no ring/ring_nf or polynomial algebra equality. |
| 2.13 wlog | n/a, no symmetric branches. |
| 2.14 calc composition | n/a, no calc. |
| 2.15 multiple goals <;> | n/a, target one equality and replacements close one family goal. |
| 3.1 erw→rw | Original rw already works; no erw introduced. |
| 3.2 legacy analysis | n/a, none. |
| 3.3 omega→lia | n/a, neither occurs. |
| 3.4 rcases rfl | Existing caller rintro rfl unchanged, no redundant substitution. |
| 3.5 attributes | Deleted helper; adding simp/grind attribute would create unnecessary local API/global behavior. |
| 3.6 simp_all | n/a, no simp_all. |
| 3.7 heartbeat options | None present or added. |

Step-back reflection: direct generic API is preferable to golfing the support proof or adding
an attribute. The shorter speculative count-monotonicity term failed definitional matching
with hRd; the explicit degreeOf_def rewrite is clear and compiled. The first scratch probe
had a misspelled pretty-printer option and an insufficiently specified hom in a simp list;
corrected, no source API change. The first module build caught nested simpa continuation
indentation; corrected before final gates. No failed exploratory attempt is counted as success.

## Verification, gates and measured performance

Actual successful commands and artifacts:

| Gate/probe | Result | Evidence |
|---|---|---|
| Module | PASS | `/Users/ramin/.elan/bin/lake build Roth.Theta`, exit 0; `/private/tmp/roth-degree-module-final.log`, “Build completed successfully (2423 jobs).” |
| Full live LSP | PASS | Native lean_diagnostic_messages, complete unfiltered file, timeout_s=180: success=true, partial=false, timed_out=false, failed_dependencies=[], 0 errors/27 warnings. `/private/tmp/roth-degree-final-lsp.json`. |
| Independent original proof/value/type | PASS | `lake env lean /private/tmp/roth-degree-original.lean`, final exit 0; `/private/tmp/roth-degree-original-final.log`; exact original support proof and generic proof, printed proof value and standard axioms. The prior `original` exit1 in probes.json refers to the failed exploratory simp tail, not this corrected final run. |
| Every effective binder | PASS | `lake env lean /private/tmp/roth-degree-negative.lean`, expected exit1; all drop failures plus Sort weakening explicitly logged. |
| Independent original consumers | PASS | `lake env lean /private/tmp/roth-degree-compatibility.lean`, exit0, 37.421s; full baseline original Theta prefix independently replayed under Roth.DegreeOriginal. Exact old application types also tested by rfl; strengthened by direct type comparison below. |
| Direct constant types | PASS | `lake env lean /private/tmp/roth-degree-strong-types.lean`, exit0; log prints Exact original type matches for both consumers. |
| Actual built axioms | PASS | compatibility.log prints actual Roth.indexSet_bddAbove, Roth.Θ_le_card, their independent originals and MvPolynomial.degrees_map_of_injective: only propext, Classical.choice, Quot.sound. |
| Deleted actual private constant | PASS | compatibility probe scans actual imported environment programmatically for `_private.Roth.Theta.*.Roth.degreeOf_map_intCast_real`, result []. |
| definition_protected | PASS | No def/abbrev/import/instance changes. |
| theorem_statement_protected | PASS | Only audited private helper deleted; all public full signatures preserved, direct type gate above. |
| structure_gate | PASS | Deleted target; caller bodies 6 lines each, no long branch or independent subproof to extract. |
| naming_gate | PASS | No forbidden pattern remains from target; no rename. |
| line_packing_gate | PASS | Original lines measured, deleted target has no retained signature; all added proof lines ≤82. |
| inequality_orientation_gate | PASS | Per-occurrence scan above; no reversed ordered inequality. |
| Comments/header | PASS | 42/42 comments and complete header before namespace byte-identical in worker start/final comparison. |
| Scoped no unintended breakage | PASS | Both necessary consumers built, independently replayed and exact types checked; no external private uses. Owner retains broader final project gate. |

Diagnostic difference against preceding complete source checkpoint
`/private/tmp/roth-theta-map-intcast/final-lsp.json`: 28→27 warnings, zero new message texts.
Exactly one disappeared: baseline line83, `automatically included section variable(s) unused
in theorem Roth.indexSet_bddAbove: [DecidableEq σ]` (unusedSectionVars). This declaration is
now at source line79, and degreeOf_def at line85 actually consumes the retained instance.
The separate unusedDecidableInType and unused hr warnings remain; no hypothesis was removed.
Machine comparison `/private/tmp/roth-degree-diagnostic-difference.json` anchors the removed
warning and empty added list. Remaining warnings concern protected header and unused premises.
No unrelated warning was suppressed or hidden by filtering.

The strong type probe directly retrieves `getConstInfo.type`, aligns the single universe
parameter, and uses Meta.isDefEq against the exact old forall type including original Fintype
and DecidableEq binders. It does not apply a theorem or permit inserted implicit lambdas.
Both expected signatures are explicitly written in `/private/tmp/roth-degree-strong-types.lean`.
Actual printed signatures in compatibility.log include both instances and every old hypothesis.

### Buzz pass — exact early source prefixes only

Outcome: FAST-BOARD for the assigned target and changed callers. All LSP, build and proof
requests had returned before these two sequential uncontended profiler runs. Actual command:

```
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/roth-degree-prefix-{before,after}.lean
```

The braces above identify two separately executed paths, not one claimed shell command.
Both exact prefixes retain all original imports, preceding source and namespace context,
ending after Θ_le_card with namespace closure. Before exit0 (35.962s), after exit0 (38.548s).
Raw UTF-8 logs `/private/tmp/roth-degree-profile-before.log` and `...-after.log`;
summary `/private/tmp/roth-degree-profile-summary.json`, command outcomes `...-profile-runs.json`.

| Declaration/source anchor | Before command+async proof+kernel ms | After command+async proof+kernel ms |
|---|---:|---:|
| degreeOf_map_intCast_real, before L64 | 5.438+23.321+2.276=31.035 | Deleted (no retained constant/cost) |
| indexSet_bddAbove, before L83 / after L79 | 3.335+53.423+3.280=60.038 | 3.938+180.499+3.756=188.193 |
| Θ_le_card, before L106 / after L104 | 6.685+44.094+3.178=53.957 | 3.696+169.869+5.069=178.634 |

Root command and associated top-level async proof/kernel nodes counted exactly once; nested
Meta/Elab/tactic times are not double-counted. These Prop declarations have no separate compiler
root in the trace. Baseline private trace anchor is `_private._stdin.0.Roth.degreeOf_map_intCast_real`,
which is the actual prefix compiler's private module name. Full built absence checked separately.
Direct terminal simp costs more than two private theorem applications, but remains <200ms;
no ≥750ms case requiring uncontended repeat, and all below1000ms. No raised limits, profiling
scaffolding or source options. No performance-driven source change or further helper warranted.
This is NOT a full-file profiler success: known late index_le_lem6 profiler failure remains
for the owner to resolve and sweep on the final frozen module.

## Simplify pass and scope of owner gates

No built-in simplify tool is exposed in this session. Manual holistic review: no new proof
skeleton, helper, repeated cast manipulation or independent branch merits extraction. Two
small terminal family rewrites are the intended direct Mathlib replacement. PASS-THROUGH,
no extra source mutation. No invented invocation is claimed.

Full-project `lake build`, separate `lake build Roth.LeanEval`, final frozen cumulative
whole-Theta profiler and downstream file gates belong to the owner; not run or claimed by
this leaf. The source-prefix profile is only interim evidence for this early declaration.
Shared reports, inventory counts, Git and rename queue remain owner-controlled.

## Required 11-step checklist

- [✓] Step 1 — required references and relevant style/naming/profiling read.
- [✓] Step 2 — all 24 substantive audit items reported.
- [✓] Step 2.5 — all five actual Mathlib search methods and variants recorded.
- [✓] Step 2.6 — all three effective binders compiled/drop-tested; generic positive probe; private literature scope and inversion recorded.
- [✓] Step 2.7 — every original signature line measured; deleted target final has zero rows.
- [✓] Step 2.8 — explicit inequality occurrence scan.
- [✓] Step 3 — all 42 golf rules have individual status/reason.
- [✓] Step 4 — whole-proof/API alternative and direct-family replacement reviewed.
- [✓] Step 5a — complete unfiltered live LSP successful; existing warnings explicitly preserved under scope except one instance-use warning resolved by proof.
- [✓] Step 5b — module, proof, exact direct type, actual axiom and diff gates recorded; prefix performance measured with bounded full-file caveat.
- [✓] Step 6a — no renames required; queue unchanged as owner-controlled.

Renames queued: none. Comments preserved: 42/42 byte-identical; helper itself had none.
Refactoring needed: none for this original helper. No source-authority retained after handoff.

Final drain: every submitted compiler/LSP/profile process returned or was explicitly terminated; no outstanding request or exec session remains. Final SHA rechecked unchanged. Source authority revoked: this leaf will make no further source edits.

## Owner frozen checkpoint gates

Leaf source authority revoked and all requests drained before owner gates. Source SHA256
`526ebb8e1c0616d69da8eda215feb13677a245e758521e519d0d483e379e5ae7` remained unchanged
through sequential `lake build` (exit0,75.907s) THEN separate `lake build Roth.LeanEval`
(exit0,22.076s). Raw `/private/tmp/roth-theta-d05-{full,leaneval}.log`; structured outcomes
and source hashes `/private/tmp/roth-theta-d05-builds.json`. Exact-path staging, commit and
successful cleanup-branch push precede the next original declaration edit. After publication:
Theta5/35 originals, overall186/264,9/14files complete. No new helper/public contract amendment.
