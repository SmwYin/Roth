# Cleanup: `Roth.ncard_boxFamily` — original18

The public count now handles any variable type whose degree bounds have finite support:
`(boxFamily r B).ncard = (B + 1) ^ ∏ᶠ j, (r j + 1)`.
Finite index types recover the previous product by `finprod_eq_prod_of_fintype`;
the old `Fin m` proposition is checked through an explicit adapter and a genuine
independent project-original proof. The sole direct caller has the necessary extra
rewrite. No polynomial/family DATA changes. This is a broader API, not a speedup claim.

## Scope and source protection

Sole original18 leaf; no children, Git, shared progress, or rename writes. Publication
counts remain233/264, MainLemma17/27 until owner review/publication. Original19+ is not
credited. Entry publication supplied by owner:7a24c379a5797a7bd3e846e2ca7c3fe020b1689b.

Resumed BEFORE728lines SHA354ae06443a541463530d38c3a4fc7f48a548cbb6331ebc88839655fc93121c3
includes the independently audited helper4 and untouched old count/caller.
Final734lines SHA45dba9b58a75de21900d1100d8eb255c9449d68162739b63b58d8607258657dc.
`source-protection18.json` reverses precisely the new Finprod import, own count
doc/declaration, necessary caller rewrite, and the authorized previously-added12 doc
sentence to recover resumed BEFORE byte for byte. The sentence now reads
“Finiteness and counting below need only finitely supported bounds.”
All original §6 quotes/prose, seven signposts, unknown metadata, old3helpers, Main,
and four-entry rename queue remain exact. Main SHA5f384557dccacaec469699cc7d32bd5666c9d525267e00433b7ae401fee98d09;
queue SHA2be6064f493c70e58303375e24ea0d93fb43cf11788b046c5265d791c6200179.

Helper4 exact scoped wrapper/declaration/one final newline SHA
8e541df58adf5f5cdbaebda0098baff81e8e0286fa24e69b936e727ca4932d9f.
Its separately completed report is
`.mathlib-quality/cleanup/MainLemma-helper-boxFamily_eq_image_finsupp_aux.md`
SHA65d494ae41d5b76fd188c188b217fd707678ac3b358495522ec66970ffded3cd;
manifest `/private/tmp/roth-mainlemma-box-family-finsupp-helper/artifact-manifest.json`
SHAce51a6e90c2f9db373e088cbb3bc5851c7ee8881b14f8b83acb1d3d01a241df2.
No helper inflation in the original264 count. No earlier original pruning or17 proof
change is included here.

Before proof2lines; after6lines (four more lines for the stronger statement), declaration8.
Public module-headline≤15 and branch≤10 gates pass. Naming and visibility stay public;
renames queued:none; comments in old target proof:none; refactoring needed:none for18.

## Genuine independent semantic verification

The fresh harness retains the complete published17 entry body (SHAff29cc40cece7f7432c7a2ddc64fd9cc73ceafd995b37b6927b7f3d2897bbac7)
and eight genuine project-original declarations from704line source
SHAa3d09825fb878c5d512cfdd3feca517465e0a8215807b1261b988f664915f3a8:
family, constructor, coefficient, injectivity, range, finiteness, count, and whole caller.
The original range RHS uses genuine original family; the original finite proof uses
original range. Every old TYPE and opaqueVALUE dependency closure bans current family,
constructor/coeff/injective/range/finite/count/caller, all old3helpers, and new helper4.
Final audited helper bytes are independently cloned in the final18 import context;
its full TYPE and actual VALUE, inferred type, standard axioms, and nonself closure
are checked as well as its exact source hash.

Only six named DATA declarations (original/entry/current boxPoly and boxFamily) unfold,
with restricted application-spine beta reduction. Actual private Name objects and fresh
universe levels are used. Raw and expanded written inner binder names/order/BI/universes
are checked before both-side generated-macro-scope normalization. No changed-arity Name
migration map, proof-irrelevance shortcut, or reflexive old/new conclusion substitution.
Actual VALUE!true and TYPE are closed: no expression/universe metavariable, free variable,
loose bound variable, or sorry. Actual VALUE inferred type matches; allowed axioms are
only propext, Classical.choice, Quot.sound. DATA uses defnInfo, theorems thmInfo.
The old Finm adapter uses actual finprod specialization, not bare definitional equality.

Ten actual property proofs cover Fin0 (count B+1), B0, Bool, ULift Bool, Finsupp bounds,
infinite Nat zero degree (count B+1), merely Finiteσ, infinite Nat single support,
infinite uniform-degree family atB1, and failure of unconditional count generality.
TYPE+opaqueVALUE/inferred/std3 are checked on these theorem properties themselves.
The negative mechanical run deliberately fails on dropping finite support, removing r/B
under autoImplicitfalse, or replacing Type by Sort; it is not positive verification.
The actual imported direct TYPE+opaqueVALUE inventory is checked, not transitive/word
search: sole count consumer `Roth.exists_ne_modByMonic_eq`. Constructor-chain direct use
is retained in raw evidence for the final fresh whole-file simplification review.

## Corrections and rejected evidence

Original18 first phase is preserved by immutable partial manifest
`/private/tmp/roth-mainlemma-ncard-box-family/partial18-artifact-manifest.json`
SHA239fd80166f123816a0785a7c5d70b7e0cb078a6e4e82b166e74e3cb8043ce15
(353references,80,461,010bytes,26binary exceptions,9drained groups).
Its helperless22.948/284.523ms profile and the separate helper-only164.135/164.965ms
recovery cannot substitute for this expanded public18 matched scope. Historical
proxy-only Lake resolution is disclosed; no later hash is backdated.

The intermediate735line selected proof with redundant classical is preserved exactly,
SHA4da98ad89b304e38ec909820d6d1934cd0018e9e32ec52fffac06f1c28f2b590.
An exact full-source no-classical alternative passed48.178708s with strict closed
TYPE/VALUE/inferred/std3; only that redundant tactic was removed. All final gates follow
that last source edit. Wrong guessed Int interval source path was corrected using the
actual file inventory to `Mathlib/Data/Int/Interval.lean` before source binding/#checks.

The wrong-line old automation run is rejected. Corrected old initial-goal attempts fail
and also retain the multiline continuation parse error; no whole proof success is claimed.
New rfl/simp/grind/aesop/exact?/decide/omega attempts fail. apply? suggestions/zero-goal
states containing synthetic holes or sorry are rejected. Initial prototype errors remain
in the immutable first-phase evidence. IndependentV1 wholeexit1/103.561781s and V2
wholeexit1/245.018074s are entirely rejected, including their partial PASS output.
V1 corrected a shadowed worklist and polymorphic String.startsWith use; V2 then exposed
the reserved local binder `prefix`. V3 changes that binder to nsPrefix and preserves all
contract/inner-name/VALUE/closure/property/inventory guards. No production change arose
from harness repairs. Negative18 wholeexit1/40.736537s is an intentional failed drop test.

## Full24 audit, final resolutions

Both the outer review and inner declaration pass cover this sole original18 target.
The separately completed helper4 audit is cited separately, without original-count credit.

1. LINT: final selected source has no target warning. Existing file metadata warning
   remains user-preserved; Main's existing header/hδ/hQ/hc warnings are disclosed.
2. HAVE SCAN: no have in old or selected count proof; none to inline.
3. SET_OPTION: none in target; no limit change or committed profiling scaffold.
4. SIMP SQUEEZE: one nonterminal simp only with five used cardinality lemmas;
   final simpa is terminal and unsqueezed. The prototype's unused Int.toNat_natCast
   was omitted. No bare nonterminal simp remains.
5. NAMING: ncard_boxFamily names the standard property of named family DATA;
   no forbidden abbreviation/numeric pattern or orientation suffix. No rename queued.
6. LINE PACKING: final signature widths87/59 codepoints. First line plus complete
   next unit55 gives87+1+55=143>100; final line has no next signature unit. Both ok.
   Old widths57/58:57+1+54=112>100. Actual width100 #check retained in positive18.log.
7. BY PLACEMENT: at end of signature line.
8. FORMAT: two-space proof indent; no internal blank line, haveI/letI, chained rw,
   or excess-width line. Body widths68/82/87/9/61/97. No redundant context tactic.
9. COMMENTS: old target had none. All seven original signposts and all unrelated
   source prose preserved by exact reversible source protection.
10. DOCSTRING: own public doc describes finite-support finprod formula and names
    the finite-index specialization for callers. Exact original §6 quote preserved.
    Only the explicitly authorized previously-added12 sentence changes cross-doc.
11. VISIBILITY: public, reusable module-headline counting API; not a private witness.
12. STRUCTURE: selected public proof6 lines≤15, declaration8 lines, no branches or
    conjunction conclusion. Substantive helper4 independently audited at14 proof lines;
    exact wrapper+helper bytes preserved throughout original18.
13. MATHLIB: all five actual methods; standard card_finsupp/card_Iic/ncard_image
    and finprod specialization reused directly. No exact project-family equivalent
    established. Whole-proof exact? fails; apply? offers partial/synthetic refinements
    and is rejected. This is substantive project DATA integration, not a redundant wrapper.
14. JUNK DEF: n/a, theorem; no DATA definition added or edited.
15. EXISTS LEMMA: n/a, not a trivial private existential witness.
16. SHOW vs CHANGE: neither in selected count; no redundant annotation.
17. PUSH_NEG: none.
18. GENERALISE: arbitrary-universeσ with finite support of degree bounds and standard
    finprod replaces Finm. No public Fintype or DecEq. Actual Finm adapter and broader
    finite/infinite properties compile. Full status tables follow.
19. INEQUALITY: explicit signature/hypothesis scan has zero≥/> occurrences and no
    _ge_/_gt_ name; no orientation rewrite or rename applies.
20. NORMAL-FORM: Set.ncard with finprod over finitely supported factors is standard;
    old indexed-product formula recovered propositionally, never called bare defeq.
21. SYNTAX-GEN: function r plus inferred finite-support class accepts infinite ambient
    types and automatically supports finite index types. No extra Fintype choice or
    finite-support enumeration is exposed in the conclusion.
22. IMPORT-FANOUT: direct Finprod import names the new public normal form and actual
    proof APIs. Main/LeanEval/root full builds validate downstream import fanout.
    Actual setup/package changes are measured in the provenance section.
23. CASTS: no new explicit cast/ascription in count proof;0 dropped/0 cross-type/0
    load-bearing. Helper4's frozen integer interval ascriptions remain its audited DATA
    contract. Prototype Int.toNat_natCast was a redundant simp lemma, not a cast.
24. INSTANCE-NAME: no instance declaration or global shortcut. Actual whole-file
    no-classical alternative passes closed TYPE/VALUE/inferredTYPE/std3, and removal
    is selected. Helper4's local Classical statement wrapper remains exact.

## Outer generalisation2.6a–e

| Parameter | Class/use | Mechanical candidates and actual result |
|---|---|---|
| old m:ℕ / Finm | structure value, ambient domain/product | replace by arbitraryσ:Type* and finite-support finprod; actual prototype, final proof and exact old formula adapter compile |
| new σ:Type* | universe/type-variable | arbitrary universe accepted including ULift Bool; Sort probe fails because MvPolynomial/Finsupp require Type; dropping leaves an unbound domain |
| r:σ→ℕ | DATA, coordinate degree bounds/factors | dropping under autoImplicitfalse produces unknown r; Nat is intrinsic existing degreeOf DATA, not an unused algebra assumption; preserve function API |
| Finite(Function.support r) | proposition/typeclass, finite exponent down-set | drop fails synthesis; mathematical uniform drop refuted by r≡1,B1 infinite-family count0 versus positive RHS; Finiteσ stronger and accepted via generic boundary; no weaker parent class |
| B:ℕ | DATA, coefficient interval/cardinality | dropping under autoImplicitfalse produces unknown B; no sign premise; integer coefficient predicate and Nat bound are protected DATA |
| old implicit Fin finite/DecEq | implicit construction machinery | no such public assumptions remain; ordinary finite types synthesize support finiteness, standard finprod removes Fintype choice |
| universe formerly small | universe | arbitrary Type* actually verified; no fixed-universe restriction retained |

2.6b: actual positive/negative whole compiler runs, full independent original/entry
contracts and current expected new TYPE/VALUE checks provide verification. No partial
PASS in a failed run is accepted. The deliberate negative run exits1 and is not a
positive gate.2.6c: standing user authorization covers evidenced beneficial public
generality. No approval is required again.2.6d: three actual independent literature
queries with their top3 each below; no ChatGPT mathematics MCP available.2.6e: selected
finite-support generality kept, all failed drops absent from production. There are no
analysis/algebra parent classes, strict premises, or bundled assumptions to unbundle.

## Inner generalisation2.6a–e and abstraction

| Effective inner parameter | Use and weakening assessment |
|---|---|
| product j:σ | every coordinate contributes rj+1; domain followsσ; drop lambda loses the indexed family, no point-local premise |
| family W and degree j | degreeOf bounds all variables of every member; inherited DATA byte-exact and full VALUE AST checked, no strict-to-weak premise |
| coefficient monomial d | common polynomial coefficient assignment across all d; cannot replace whole-array condition by independent existential choices |
| implicit support proof/instance | finite down-set of ofSupportFinite r; inferred for Finiteσ; no DecEq/Fintype hidden in public TYPE; all effective binders logged/compared |
| Nat factors rj+1 | already nonnegative and positive without added premises; changing degree domain would change existing family DATA |

Inner2.6b uses the same actual theorem properties and raw TYPE/DATA-value AST checks,
including all written inner binder names/order/BI/universes.2.6c has no further beneficial
restatement.2.6d is the same public target's three literature queries, not an omitted
private exemption.2.6e keeps standard finite-support formulation. Inversion check:
the reusable finite-choice abstraction is Mathlib Finset.finsupp/Iic, already used;
no new dictionary/default wrapper or additional helper is justified.

## All42 golfing rules

1.1 n/a: no by-exact wrapper. 1.2 n/a: no by-rfl wrapper.
1.3 n/a: rw is followed by substantive cardinality normalization, not adjacent exact.
1.4 already terminal simpa using hj; no simp/exact pair to consolidate.
1.5 n/a: no trailing rfl after simp.
1.6 n/a: no constructor/exact pair; helper4 is separately audited.
1.7 n/a: no apply/exact chain.
1.8 n/a: no by_contra/push-neg.
1.9 n/a: indexed-factor and support-implication lambdas are not eta expansions.
1.10 n/a: no have.
1.11 n/a: no apply/intro.
1.12 n/a: no show.
1.13 n/a: no have/projection destructuring.
1.14 already one rw list; no consecutive rewrite calls.
1.15 terminal simpa remains unsqueezed; nonterminal simp only is intentional.
1.16 nonterminal simp only is explicit; prototype's unused argument removed.
1.17 applied: .symm and standard support/product API; dot notation already concise.
1.18 n/a: enclosing parentheses are required for .symm projection, no <| saving.
1.19 n/a: no push_neg.
1.20 n/a: public cardinality result, not a private trivial witness.
2.1 actual old/new whole-proof grind attempts fail at the initial goal.
2.2 n/a: no grind retained.
2.3 already final simpa using membership hypothesis; nonterminal normalization feeds
    congruence, with no subsequent exact of a normalized existing hypothesis.
2.4 n/a: no analytic function property.
2.5 n/a: no positivity subgoal in selected count proof.
2.6 n/a: no inequality/calc monotonicity block.
2.7 n/a: no standalone linear arithmetic goal; actual whole omega cannot relate
    uninterpreted ncard and product. Final support implication is direct simp.
2.8 actual old/new whole aesop attempts fail.
2.9 n/a: no numerical computation/cross-type cast goal.
2.10 actual decide rejects free variables; no native_decide or trust extension.
2.11 n/a: no denominator/ring-identity goal.
2.12 n/a: no ring/ring_nf ending with arithmetic hypotheses.
2.13 n/a: no symmetric branches.
2.14 n/a: no calc chain.
2.15 n/a: no repeated similar subgoals; congr1 leaves one exponent equality.
3.1 n/a: no erw.3.2 n/a: no continuity/measurability.
3.3 n/a: no omega retained or linear arithmetic subgoal needing lia.
3.4 n/a: no rcases/rfl substitution.
3.5 no new global attribute: explicit count rewriting is sufficient at actual caller;
    no evidenced need for global simp/grind automation changes.
3.6 n/a: no simp_all only.
3.7 n/a: no resource options; no limits raised or heartbeat wrappers used.

Step-back: rfl/simp/grind/aesop/exact?/decide/omega fail on both original and broader
initial goals. apply? produces partial/synthetic refinements, not an accepted proof.
The selected strategy counts standard bounded arrays through the audited representation,
then identifies the finite support product. congr1 supplies the expected exponent type;
a more explicitly parameterized congrArg term would expose the finite down-set and
obscure the short mathematical outline. No additional extraction is warranted at6 lines.
The redundant classical tactic was tested on an exact full-source alternative with
strict TYPE/VALUE/inferredTYPE/std3 guards and removed. All final gates follow that edit.

## Search, literature, and retained recommendations

All five actual searches are retained in the original18 immutable partial root:
Finder bounded-degree/coeff count, Loogle Finset.finsupp, LeanSearch finite-choice
cardinality, full pinned-source grep and standard-file inspection, and local name
lookups. Local index unavailable/warming is not an absence claim. Auxiliary variants:
card_Iic/card_Icc, ncard_image_of_injective/ncard_coe_finset, ofCoeff_injective,
finprod_eq_prod_of_mulSupport_subset(_of_finite), finprod_eq_prod_of_fintype.
All new external names are verified by actual #check in positive18's wholeexit0;
eight actual source files are copied/hash-bound in pinned-source18.json.
The common finite-cardinality lookup supplies building blocks, not project family DATA.
No exact Mathlib replacement established; actual generic exact? fails, apply? is partial.

Three independent actual queries and exact top3, in returned order:

| Query | Top3 |
|---|---|
| count polynomials bounded degree bounded integer coefficients product number monomials generalization | https://arxiv.org/abs/1803.08755 ; https://www.sciencedirect.com/science/article/pii/S0022314X05002647 ; https://arxiv.org/abs/1402.5430 |
| polynomial ring infinitely many indeterminates finite monomials finite support | https://en.wikipedia.org/wiki/Polynomial_ring ; https://en.wikipedia-on-ipfs.org.ipns.s402.de/wiki/Polynomial_ring ; https://www.cip.ifi.lmu.de/~grinberg/t/23wa/23wa.pdf |
| mathlib Finset finsupp card_finsupp finprod finite support product | https://leanprover-community.github.io/mathlib_docs/data/finset/finsupp.html ; https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Finset/Finsupp.html ; https://math.iisc.ac.in/~gadgil/PfsProgs25doc/Mathlib/Data/Finset/Finsupp.html |

Related bounded-height papers are not evidence for the exact box formula. The old
mathlib3/mirror/Wikipedia hits are leads, not pinned implementation evidence. The
mathematical inference is that finite exponent support plus finite coefficient choices
suffices even with infinitely many ambient variables; actual pinned primary source and
kernel-checked proofs establish the selected statement. No missing third query or late
literature completion is hidden: all three belonged to original18 before its final report.

Scoped holistic review: the new count and helper have different roles, and no further
target issue is found. A built-in simplify callable is unavailable, so no invented
invocation or independent full-file simplify credit is claimed. Original17 can have
a3-line finiteness proof through the audited helper: positive18 compiles that exact
candidate with closed TYPE/VALUE/inferredTYPE/std3. It remains unchanged under the
explicit narrow scope; the helper currently follows17, so applying it in production
also requires a declaration-order change. Owner was notified for final simplify. Actual constructor-chain
usage is logged independently; no earlier original is pruned here. Fresh whole-file
independent simplify/GLOBAL/public+retained-axiom/cumulative gates remain mandatory.

## Final builds, native diagnostics, and diff gates

All final gates bind canonical734line source45dba9 after the last source edit.
No limit raises, new axioms, sorry/admit, weaker conclusion, Meta profiling trick,
positive builtin max0 heartbeat run, or production scaffold. Full stdout and stderr
are separate strict UTF8 streams with actual hashes, whole exit status, immutable17pins,
non-timeout and process-group drain in each runner JSON.

| Final operation | Whole exit | Seconds |
|---|---:|---:|
| affected MainLemma | 0 | 80.346163 |
| full project | 0 | 35.196532 |
| separate LeanEval | 0 | 39.404247 |
| positive identifiers/properties/future17 probe | 0 | 48.626677 |
| fresh genuine independent V3 | 0 | 335.618427 |

Native calls are full and unfiltered, sequential, complete/nonpartial/nontimeout, with no failed dependencies.

| Native file | Errors | Existing warnings |
|---|---:|---:|
| MainLemma.lean | 0 | 1 |
| Main.lean | 0 | 4 |
| LeanEval.lean | 0 | 0 |

MainLemma preserves the existing copyright-header warning. Main preserves that header
plus existing hδ/hQ/hc warnings. LeanEval has no messages. No warning-free claim for
MainLemma/Main, and no metadata change to silence user-preserved warnings.
`final18-native-verification.json` binds actual unfiltered arguments, raw hashes, and17
source/config pins before and after each call.

| Gate | Status/evidence |
|---|---|
| lake_build_file | PASS final affected exit0 |
| lake_build | PASS final full exit0 |
| definition_protected | PASS no existing DATA definition changed; full exact values checked |
| theorem_statement_protected | PASS authorized broader count, genuine exact old Finm adapter; unchanged whole caller TYPE |
| structure_gate | PASS headline6≤15;0 branches; frozen helper4 separately audited14≤15 |
| naming_gate | PASS public mathematical property name; no rename required |
| line_packing_gate | PASS full per-line widths and next-unit143>100; no overlong line |
| inequality_orientation_gate | PASS0 occurrences, no ≥/> name/signature issue |
| cumulative_no_unintended_external_breakage | PASS affected/full/separateEval/native and old whole callers |
| no-limit-raise | PASS no new maxHeartbeats/synthInstance.maxHeartbeats/maxRecDepth option |
| no-scaffolding | PASS profiling only in reversible snapshot scaffold |
| scoped re-sweep | PASS helper/count/sole actual consumer measured, all under1000ms |

Gates: PASS for original18 scope. No target decomposition/rename deferral. The separate
final-file/global slow rows remain red until their owner completes the later full pass.

## Matched profile and honest scope

Exact CLI on each separately frozen side:
`lake env lean -j1 --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 FILE`.
Flags precede each entire doc/command, including `open scoped Classical in` outer helper
wrapper. Removing only scaffolding recovers exact side canonical source bytes.
Actual private qualified proof anchors, unique token+separator, column0 disjoint
command/async/compiler/kernel/lint roots are checked by the owner parser and verifier.
The two flat privatelemma/privatetheorem macro-expansion commands are inclusive children
of the outer wrapper, explicitly excluded. No nested/Meta/next/end double count.
Full actual parent consumer command includes its generated proof; no second count for
`_proof_1_1`. Raw/scaffold/source wrapper binding JSON is retained on each side.

| Complete scope | BEFORE ms | AFTER ms |
|---|---:|---:|
| helper | 166.314 | 159.934 |
| count | 20.499 | 55.913 |
| consumer | 280.309 | 269.328 |
| helper + count | 186.813 | 215.847 |
| whole matched scope | 467.122 | 485.175 |

All rows and both combined scopes are below750ms, so frozen repeat trigger does not
fire; all are below1000ms. No failed>1000 row, cherry-picked third run, or unmatched
numeric speedup claim. The old count does not call the helper but the complete helper
command is deliberately included on both sides because final count uses it. This is a
strictly broader public statement; count time increases and no speedup is claimed.
Wall times are not declaration times. Full BEFORE/AFTER raw hashes and exit/drain records
are in before18-profile.json/final18-profile.json, not inferred from a profiler substring.

before18-profile: wholeexit0/58.540406s; rawSHAdfc09a285f2dbd85f1adb7547d4f0512ec36aa162c8b1b383261ec2d7ef72aff; stderrSHA3fa545b2698e600ffa920e8ffe7a347fc7f0de31f33f88b5b3edb7a648978722; PGID5451 absent.

final18-profile: wholeexit0/59.313490s; rawSHA1ceb126fde3e910840c6bd6140dc415735929ef6651c1ed112a0917b1d2338ef; stderrSHAd9c4647b0bdd5fb2e6729ea6d7c01d4d252b739303fe5a67a2bed8af48447147; PGID6730 absent.

## Source, setup, executable, and compiled-artifact provenance

BEFORE API edit, the expanded baseline freshly captures exact audited helper/current
published17 source,17 source/config pins,104 actual project cache companions, setup
options, observed environment, direct --deps, actual distinct pinned Lake and Lean
binaries, both Elan proxies/PATH resolution, and both compiled-artifact catalog scopes.
Final fresh copies/observations repeat these after the last edit, with pre/post final
profile executable and core hashes. No inherited proxy-only pair is accepted.

Actual pinned Lean49968bytes SHA1b370cfcbf44e80d1b004ab1b1ab9a4c73951f9f7c242140bcff9bc577576554;
actual pinned Lake51824bytes SHAc8c24f1398162ab4004e2a869952d8469f54293651151feaad4526f2b8474c6e.
Both Elan proxies5880832bytes SHAd52c4516a6c6f0cc14cab0ecf36e5058a764f39b109d8609be7dd1279ca41e9f.
All three observations agree; actual final bytes are freshly rehashed, not just catalog
hashes. Executable binary exceptions are explicit; they are not called UTF8 source.

The MainLemma/Main dynamic setup.importArts PACKAGE/SETUP union (plus existing split
companions) is12201 artifacts: BEFORE1,803,601,640bytes, AFTER1,803,613,128bytes.
This union is NOT an exact loaded-module closure; direct --deps is not a transitive
catalog. Installed pinned lib/lean compiled-artifact SUPERSET is12592 files/
2,125,623,224bytes, including implicit Init and all .olean/.server/.private/.ir/.ir.sig
companions. This SUPERSET is NOT an exact loaded closure and does not replace executable
hashes. Both scopes are separately saved and actually rehashed after profile.
No union path is added/removed. Only project MainLemma.olean differs in the union;
12190 external package artifacts are freshly unchanged. All12592 core entries are
freshly equal across before/pre-final-profile/post-final-profile. Combined scoped
catalog entries24793 total3,929,236,352bytes (including11 project union entries).
The inherited package catalog is reused only through actual fresh byte verification;
new18 project cache copies and setup observations are independent.

Direct --deps changes9rows/8unique→10rows/9unique by exactly Finprod. Both duplicated
implicit Init rows are retained, and every direct path belongs to one of the two
separately scoped actual catalogs. The direct-import increase does not imply a new
transitive package artifact. Full setup options remain weak.linter.mathlibStandardSet
true, relaxedAutoImplicit false, pp.unicode.fun true, maxSynthPendingDepth3; no plugins
or dynlibs added. Source/config pins differ only at authorized MainLemma source.
All104 final project companions equal actual final bytes;9 expected rebuilt companions
change versus BEFORE (MainLemma olean/ilean/hash/trace/c/hash, Main/LeanEval traces), listed
in final18-verification.json. No expectation of byte-equal project artifacts is imposed
across an intentional source change.

The observed lake-env printenv captures differ only SHLVL=1→SHLVL=2 due to the shell
capture context; all other observed environment lines agree. This is disclosed rather
than asserting byte-equal environments. Exact raw captures and hashes are retained in
final18-environment-comparison.json. Compiler/scaffold CLI flags/options and pinned
paths are separately bound; no altered heartbeat/recursion option is introduced.

## Required phase checklist and remaining owner work

- [✓] Step1 reference docs fully read: lean4/mathlib-quality skills, cleanup/cleanup-all/buzz and mandatory references; verbatim854line dispatch and112line profiler-scope procedure.
- [✓] Step2 full24 audit printed before/final resolution; item1–19 and20–24 all covered.
- [✓] Step2.5 all five actual search methods and actual standard source/name checks; failures honestly recorded.
- [✓] Step2.6 outer and inner2.6a–e, all binders/assumptions/universes, three literature queries/top3 each.
- [✓] Step2.7 all signature line widths/next-unit inequality, width100 actual #check.
- [✓] Step2.8 full inequality occurrence/orientation table (zero occurrences).
- [✓] Step3 all42 golfing rules have individual statuses and actual automation evidence.
- [✓] Step4 step-back/abstraction/packing/normal-form reflection complete.
- [✓] Step5a fresh full native diagnostics clean of errors; existing warnings explicitly preserved.
- [✓] Step5b all applicable diff, semantic, build, scoped performance and preservation gates PASS.
- [✓] Step6a no rename required; existing four-entry sidecar byte-exact, no queue write.

The scoped manual holistic review and actual future17 probe do not claim built-in
/simplify invocation or a fresh independent whole-file simplify. The latter remains
mandatory later. Actual final constructor-chain inventory shows no direct TYPE/VALUE
users of current boxPoly_injective or range_boxPoly; boxPoly and coeff only serve that
private chain/generated eq. Owner may assess removal during fresh whole-file review.
The compiled3-line17 candidate also needs moving helper before17; no such edit here.

Known final GLOBAL/file failures remain historical δ11188.775ms, pigeon1000.235ms,
main4880.648ms; no scoped pass closes them. Full27, all retained rows/repairs, cumulative
all22 original public DATA and all retained axioms/import/docs/comments/static references,
final fresh whole-file simplification, all affected/full/Eval/native, rename end pass,
report/pushclean/release remain owner work. RootCI39497338608@d953155 infraSSL35 before
codecheck/rerun pending is supplied by owner; no GitHub probe or workflow/version edit.
Parent independently reviews this evidence, runs fresh FULL/separateEval/rootEvalnative,
and stages/publishes sourceA plus actual metadataB before original19.

Artifact root: `/private/tmp/roth-mainlemma-ncard-box-family-resumed`.
The final artifact-manifest.json records every actual saved artifact byte count/SHA and
strict UTF8 status or actual binary exception, freshly verifies the immutable first
phase353-reference and helper4 manifests/files, and separately references both external
catalog scopes. It excludes itself to avoid a circular hash; its final SHA is delivered
in the handoff. No saved binary is represented as textual evidence.

Final fresh verification: 17 resumed owned CLI process groups absent, all native requests complete; initial9 groups were separately drained. No compiler/native/profile operation remains. Explicit END is delivered after final report/manifest freeze; that handoff releases all original18 leases.
