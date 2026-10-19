# Final independent filewide simplify review — Roth/Theta.lean

Outcome: **PASS-THROUGH**.

Issues identified in final Lean source: none. Fixes applied to Lean source: none.
Files modified by this review: this report only; refreshed review evidence is under
`/private/tmp/theta-final-review-after-hr/`. Historical first report
`Theta-final-simplify.md` remains byte-identical, SHA256
`484a772138314b48bf1793e71aa2b4013b49aa37c3b377ca8a3189746b329576`.
Its ISSUES-FOUND-NOT-FIXED outcome remains the historical findings handoff; both findings
are now resolved at separately published checkpoints.

No built-in simplify callable is exposed. I performed its independent holistic reuse,
quality and efficiency assessment directly, applying lean4/mathlib-quality, installed cleanup
Phases 5a/6/6.5/6.6, cleanup-gates, golfing-rules, proof-patterns, profiling and relevant
style/naming guidance. This review does not replace the owner's final gate sweep.

## Exact source and scope

Reviewed the ENTIRE final 991-line, 50-declaration source and ENTIRE cumulative diff against
original `2b64544bf9f77a8ff957bf1bcaf693ac72217ff6` (709 insertions,699 deletions).
Published HEAD `164e33bbab012cd4106a39d42a85be423d5f3f57`.
Theta SHA256 `ff85b7f132cf83c980323449b38558699e7e39d5a1b8bd895ac3374d78310207`.
MainLemma SHA256 `a002b02724dc9f4bcef52280bc96c736eb2fd9acbc06b5352c6eff55b94dd689`.
Original Theta SHA256 `7804edad88aa3e586df46b7722755ba89e67566c5434c58ae970d0dd2fbfa4fd`.
Cumulative diff SHA256 `52aab55a168762dc5d6062d348df8515262594c7fde38bb6b695128640ca766b`.
`source-manifest.json` and `hash-FIRST-verification.json` bind the review to all17 final
source/configuration entries and3 overlapping toolchain/Lake pins. These match the final
original20 freeze. No Git/shared-log writes or production source changes were made.

## Both earlier recommendations resolved

- Original9 `index_le_Θ.hr` was removed in source/audit checkpoint
  `34102b2ba52a952cecd11df7d030b44454697ece`, metadata
  `73e260450bf91912548fef9130a46d5b0daf422f`. Its direct supremum proof is unchanged.
  Both internal separated-product calls now omit the positivity argument; MainLemma676
  is `index_le_Θ hWX hh`. MainLemma's independently necessary `hr0` remains elsewhere.
- Original20 `Θ_unique_le.hr` was removed in source/audit checkpoint
  `367508ced3cb06f20874c08d30361a261b14a1a9`, metadata/current HEAD above. Both private
  callers now use the new arity. `theta_lt_base_aux.hrlast` still supplies the genuinely
  necessary real denominator certificate through explicit `ne_of_gt` and `exact_mod_cast`;
  that private premise is not an unused argument kept by a fictional user veto.
  `theta_scaled_unique_le_aux` retains positivity needed by monotonicity and division.

`callers.json` freshly inventories all production mentions, distinguishing the module-doc
mention from calls. There are2 internal +1 MainLemma calls of original9 and2 internal calls
of original20. Both theorem bodies remain the direct established proofs. The dedicated
checkpoint evidence checks actualRoot new telescopes/opaque values/standard axioms, exact old
adapters and genuine zero-weight applications. Public names, conclusion, retained argument
order, domains, hq, global Θ hB/hr, wrappers and header choices remain protected. No further
substantive helper/proof/API issue survived independent inspection.

## Structure, reuse, formatting and imports

`structure.json` independently refreshes every declaration. All7 module Main-results fit15
noncomment body lines: Θ_lt15, Θ_option_le5, Θ_unique_le3, Θ_le_card5, others≤3. Every ordinary
body fits30; separated-product, prefix and phi stages reach30. The phi statement's `let M :=`
is not miscounted as the body boundary. Explicit branches/local subproofs fit10: quadratic
numeric branch9, prefix ratio branch8, Θ_lt zero branch8. No split of correlated existential
witnesses is warranted: factorization and index_le_lem6 witnesses depend on one another.
RSet's conjunction defines its mathematical data predicate; there is no ordinary fixed-parameter
conjunction theorem left requiring separation.

I inspected repeated skeletons across supremum lifting, polynomial multiplicity, finite sums,
determinant estimates and the induction. Boundedness/cardinality repeat a short direct index
bound in distinct supremum arguments; extracting a forwarding helper would add no useful
mathematics. The linear/quadratic estimates, determinant map/nonzero certificate, separated
product and coefficient/exponential stages have distinct roles. Existing induction helpers
expose the base, scaled singleton, prefix, successor and large-delta arguments clearly.
No substantial duplicated proof skeleton, junk predicate/definition or additional helper is needed.
No new instance, named-instance clutter or forbidden numeric helper name exists. The authorized
Index rename remains the owner's later project-wide pass, with no new Theta rename request.

Maximum width100 codepoints. `signature-packing.json` refreshes all183 signature-line rows:
unchanged rows revalidated against actual final widths, both public changed signatures replaced
with their dedicated exact packing tables. No repacking is needed. Lambda arrows, by placement,
blank lines, inequalities and casts remain appropriate; explicit casts cross actual coefficient,
weight and logarithm domains. Documented restricted terminal simplifications retain prior
performance/recursion justifications; no broad automation churn is warranted.

Cumulative import set is unchanged, alphabetized in Mathlib/project groups. Logarithms, powers,
Gauss lemma, coefficient bounds, indices and separation are directly used. CoeffNorm's direct
import states an actual API dependency even though Separation reaches it transitively.
No new fanout or import promotion. All five public definition types/values remain intact
(two ordinary lambda spellings changed cumulatively); owner's exact kernel evidence covers
these values. Header/module reference content is unchanged by this review. No axioms, sorry,
native_decide, limit raises, suppressions, options, TODO/FIXME, code λ, dollar or push_neg
appear. `textual-gates.log` has only3 MainLemma prose λ hits.

## Refreshed comment, reference, audit and FIRST evidence

- `proof-comments.md/json`: all11 original proof signposts traced to final anchors;
  10 preserved/re-anchored, one antitone next-tactic restatement permissibly removed,
  one new small-index explanation. Capitalization of the lower/upper determinant signpost
  is the only textual change there. The explicit antitone declaration remains at907.
- `external-reference-table.md/json`, `current-newtokens.json`: cumulative lexical inventory
  freshly recomputed against original source, comments excluded.176 added identifiers;
  the earlier inventory's five omitted local epsilon binders/projections are now explicit.
  This is a reporting correction, not a source finding.97 normalized external expressions
  are unchanged; no new external name is introduced by the denominator certificate.
  Project declarations, syntax, binders and projections are classified separately.
- Fresh `/Users/ramin/.elan/bin/lake env lean /private/tmp/theta-final-review-after-hr/References.lean`
  exited0, zero errors/warnings, all97 positive checks. `positive-compiler-results.json`
  binds probe/log/pins/source hashes. Earlier per-name local/source/native verification is
  inherited honestly; fresh ne_of_gt/log_pos local lookups and pinned-source fallback are
  archived separately. The index reports unavailable; no global absence claim follows.
  Fully qualified environment checks supply positive existence beyond ambiguous source hits.
- `audit-inventory.md`, `report-inventory.json`:35 originals=29public/6private;
  current50=32 retained originals+18 retained introduced helpers. All22 introduced-helper
  histories (18 retained,4 deleted) have dedicated reports.3 removed ORIGINAL private
  declarations remain separate.80 distinct report hashes and concrete gate/FIRST pointers
  are refreshed, including both technical-hr reports and mapped-performance supplement.
  All78 previously indexed report hashes match. No repeated42-rule/historical compilation
  was manufactured for unchanged declarations.
- `hash-FIRST-verification.json`:23 combined FIRST paths and9 older supplements rehash
  exactly. Their complementary provenance is retained; a16-helper special map is not
  treated as covering all22 histories. Historical snapshots with later errors are not
  relabelled clean whole-file compiles. All143 latest artifact entries were examined:
  142 match exactly, and the original20 report differs solely by its owner publication
  appendix; its entire prior prefix recovers the exact frozen hash. No unexplained hash delta.

## Contract, migration and measurement boundaries

Latest inherited accepted cumulative scaffold:
`/private/tmp/theta-unique-technical-hr/ActualSemanticsAugmented.lean`, SHA256
`fd402edc1a05acd6530a4ed2f6498c501df1da3a3919baf53222e21365d7999c`.
Its final freeze SHA256 `93c588ef23892e24b5fdf08598bdfa8e464172d5964ab7de46727654711c2293`
and owner checked records are freshly hash-verified. Its actual compiler run exited0 with1223
markers:1055 prior checks preserved under one explicitly HISTORICAL AST marker mapping plus168
new actualRoot checks. Historical retained-hr compatibility is not actual currentRoot metadata.
The new8-binder target, exact old10-binder adapter, full affected private13/7-binder contracts,
all29 old public adapters, actual definition values and whole26-binder MainLemma proof have
separate actual/independent value/type/standard-axiom/nonself/dependency evidence. Two generated
MainLemma sharing auxiliaries differ (independent eta._proof_1/lam._proof_1); every source
proof remains checked. Identical generated-auxiliary counts are not claimed.

Four COMPLETE canonical OriginalIndex/OriginalTheta/original2bMainLemma/preceding-currentMainLemma
blocks rehash exactly at recorded raw offsets. Both inverse scripts were freshly executed:
original9 recovers all692893 preceding bytes; original20 recovers all806170 preceding bytes,
SHA256 `903f10bdf10c4be5508886910804af3ebca2f978f5eafbc5116ddef2f5ee8da7`.
Migrations occur outside the four canonical blocks; no unchanged-whole-prefix claim is made.
`index-inverse-check.json`, `inverse-check.json` and the hash inventory record these facts.

Inherited original20 scoped actual whole-file profile has50 anchored disjoint declaration rows,
all below750ms: target75.070ms, scaled519.579ms, base482.899ms. No required repeat in that
checkpoint; no new performance issue was found by structural inspection. These are inherited
accepted scoped measurements, not the owner's future final FAST-BOARD. MainLemma main_lemma
actual timing remains unavailable after the bounded60s pre-target cutoff (5/27); whole-project
performance is not certified. No whole-file profiling/full build/large semantic replay was
duplicated during this independent read-only review. Owner's already completed original20
full build78.682s THEN separate LeanEval50.523s are historical exact-source publication gates.

## Complete warning exceptions and remaining owner gates

`native-warning-inventory.json` preserves all warning messages/provenance. Latest complete
unfiltered final-source inherited native Theta result:0errors/6warnings (header1;
Θ_nonneg hB/hr101; Θ_le_card hB109; Θ_mono hr129; protected index_le_lem6 hq553).
MainLemma:0/3 (header1; hδ0/hr₁149). Unchanged Main inherited result:0/4 (header1;
hδ333, hQ474, hc475). LeanEval/root:0/0 each. All recorded requests completed with success=true,
partial=false,timed_out=false,failed_dependencies=[]. Neither removed public hr warning remains.
No diagnostic suppression. Imported-module headers and pre-existing GenWronskian Fintype241/
Separation Fintype531 warnings, historical scratch unused premises/section instances and old-arity
compatibility warnings remain in their unfiltered checkpoint logs. Original20 module builds
reported16/20 warnings; independent/cumulative scratch29/120. Expected-failure binder/automation
probes remain negative evidence, not positive gates. The sole fresh reviewer compiler has0warnings.

Owner must still align its all29 generator using the supplied minimal BOTH-hr-drops patch,
then run fresh final all29/all50 opaque-value/standard-axiom checks, complete unfiltered native5,
actual whole-file all50 profiling with required≥750 repeat, full build THEN separate LeanEval,
and publication. No future gate is claimed complete. This PASS-THROUGH is the completed
independent review; owner decides file completion. No original/file credit is added here.

## Terminal authority and drain

One reviewer compiler session15424 was observed exited0; two reviewer native local-search
requests returned complete. Both inverse checks and inventory scripts completed. No reviewer
profiler, full build or diagnostics sweep was started; no request remains in flight.
`terminal-manifest.json` contains exact report/artifact hashes and pending=[].
All source/scratch/report/compiler/native authority is revoked at this terminal handoff.
No system-wide ps success is claimed; drain evidence is completion of every reviewer-owned
session/call. Source is unchanged. The owner now holds the source/compiler/native window.
