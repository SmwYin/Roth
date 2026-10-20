# Original17: `Roth.boxFamily_finite`

Leaf review result: PASS on scoped final gates, awaiting owner review and publication.
This report does not advance the published232/264 or MainLemma16/27 counters.
No original18+ audit, whole-file completion, or GLOBAL performance credit is claimed.
Artifact root: `/private/tmp/roth-mainlemma-box-family-finite` (all short filenames below are relative to it).

## Result and exact scope

The public theorem now accepts arbitrary-universe `σ` and only
`[Finite (Function.support r)]`. This includes infinite ambient indices with finitely
supported degree bounds. Finite index types synthesize this instance, so all old
`boxFamily_finite r B` calls retain their explicit argument order and compile unchanged.
The conclusion and integer coefficient predicate are unchanged.

The proof enumerates allowed exponent vectors using `Finset.finsupp`, then enumerates
coefficient arrays on those vectors, and takes the image under `AddMonoidAlgebra.ofCoeff`.
Coordinate degree bounds force every exponent outside `Function.support r` to zero.
This uses existing standard APIs and introduces no helper, definition, axiom, or wrapper.

Only four authorized edits occur: necessary direct `Mathlib.Data.Finset.Finsupp` import;
original17 theorem; its own accurate docstring; only the previously ADDED original12
sentence about finiteness/counting. All original §6 quotations/prose and seven signposts
are preserved. `source-protection17.json` reverses exactly these four edits and recovers
the entire entry source byte-for-byte. Main, all three retained helpers, all other source
and configuration pins, and the exact four-entry rename queue remain unchanged.
Original source694 lines → final708; declaration3→15; proof2→13 (ordinary≤30, branches0≤10).
There are still27 original declarations and3 retained helpers, with no helper inflation.

Entry source SHA256: `6808b77320c176564d9d60b450f59ddff6b7b319cc9a03da01dbf2a159a111eb`.
Final source SHA256: `ff29cc40cece7f7432c7a2ddc64fd9cc73ceafd995b37b6927b7f3d2897bbac7`.
Main SHA256: `5f384557dccacaec469699cc7d32bd5666c9d525267e00433b7ae401fee98d09`.
Protected helper hashes are recorded individually in `source-protection17.json`.
No Git operation or shared-progress/queue mutation was performed by this leaf.

## Final generalisation status: outer AND inner2.6a–e

The full before-edit table is reproduced later as a historical record. This final table
covers every old and new parameter, including effective instances and universe binders.
Both outer and inner passes inspect the same sole target; no unexamined new helper exists.

| Parameter | Class and use | Mechanical candidates, actual verification | Result |
|---|---|---|---|
| old `{m : ℕ}` / index `Fin m` | structure value; fixes ambient variables | arbitrary `σ : Type*` with merelyFiniteσ actually compiled; strictly weaker finite support actually compiled and property-tested | kept finite-support API |
| new `{σ : Type*}` | type-variable; polynomial/Finsupp domain | arbitrary universe verified, including lifted Bool; `Sort*` attempted and rejected by domain requirements; dropping leaves unboundσ | retain Type*; no finite ambient assumption |
| `(r : σ → ℕ)` | structure value; coordinate bounds and support | drop with autoImplicitfalse fails; ℕ intrinsic to existing degreeOf/predicate, no ordered-ring parent applies; finite-support bound is exact natural weakening | retain explicit r; no new representation |
| `[Finite (Function.support r)]` | typeclass/proposition; finite exponent support | drop fails missing finiteness; Finiteσ route succeeds but is stronger; no DecidableEq/Fintype needed in public statement; Set.Finite support is definitionally same proposition | kept weakest verified premise; infiniteNat zero/single-support cases compile |
| `(B : ℕ)` | structure value; coefficient upper bound | drop fails unknown B; fixed integer-polynomial DATA semantics retained; no strict premise or algebra hierarchy to weaken | retain explicit B |
| old implicit Fin m finite/DecEq machinery | decidability/typeclass | generic support proof requires only local classical; no global instance/statement DecEq/Fintype | dropped concrete ambient restriction |
| universe formerly small | universe | arbitrary universe accepted; actual lifted-index boundary check | kept universe polymorphism |

2.6b: actual bounded CLI candidates and whole final native diagnostics supply verification;
failed probes are retained, never credited. MerelyFiniteσ proof uses local
`Fintype.ofFinite` with the genuine generic range representation and compiled. The stronger
support proof is independently compiled, not inferred from a proposed statement.
Removing all finiteness is false: `probe17-alternatives-v2.lean` actually proves infinitely
many bounded polynomials for σ=ℕ,r≡1,B=1 using distinct variables.
2.6c: this public structural generalisation is covered by the standing user instruction
to implement evidenced beneficial recommendations; no new permission is needed.
All original call sites compile under resolution; no postponed candidate remains.
2.6d: literature and all five actual searches below. 2.6e: selected support premise kept;
all drop failures reverted. No bundled hypotheses to unbundle, no strict→weak candidate,
no analysis/algebra class hierarchy, or point-localisation candidate is omitted.
Inversion/abstraction: the reusable enumeration abstraction is already `Finset.finsupp`;
no new abstraction or proof wrapper is justified.

## Search and literature evidence

A: actual Lean-Finder bounded-degree/coeff query returned partial module-finite
restrictDegree/restrictTotalDegree and Finsupp.finite_of_degree_le results.
B: actual Loogle Set.Finite/MvPolynomial query returned0.
C: actual LeanSearch returned Finset.finsupp, mem_finsupp_iff, onFinset.
D: full actual pinned-source search and explicit Finset.Finsupp source inspection retained
in `search17-source.txt` and `new-identifiers17-pinned-source.txt`.
E: actual local name lookups encountered index warming/errors, so no absence claim is
made from them; all16 newly used identifiers were subsequently compiled with actual
`#check`, including final theorem at format.width100 (`new-identifiers17-v2.log`, exit0).
The imported actual TYPE+opaqueVALUE inventory and corrected LSP references agree:
sole complete direct-consumer command `Roth.exists_ne_modByMonic_eq`, with generated
`._proof_1_1` a member of the same parent group. Three LSP positions are declaration plus
two calls. An initial wrong-line lookup returning0 is retained and superseded.
No exact standard boxFamily theorem exists among these results; this family is project DATA.
No ChatGPT mathematics MCP tool was available in the actual tool inventory.

Two primary-literature queries and their exact top3 results are frozen in
`literature17-top3.json` (all raw results retained):

| Query | Actual top3, in order |
|---|---|
| Stacks polynomial ring/infinite variables/finite monomials | [Stacks algebra PDF](https://stacks.math.columbia.edu/download/algebra.pdf); [Stacks054A](https://stacks.math.columbia.edu/tag/054A); [Wikipedia polynomial ring](https://en.wikipedia.org/wiki/Polynomial_ring) |
| Mathlib4 Finset.finsupp/mem_finsupp_iff finite | [Mathlib4 Finset.Finsupp](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Finset/Finsupp.html); [Mathlib4 Finsupp.Defs](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Finsupp/Defs.html); [mathlib3 Finset.Finsupp](https://leanprover-community.github.io/mathlib_docs/data/finset/finsupp.html) |

Only pinned Mathlib4 source/compiled APIs establish the chosen implementation. Wikipedia,
the older mathlib3 hit, and general flatness result are search results, not proof evidence.
The mathematical inference is that finite allowed exponent support and finite coefficient
choices suffice even when the ambient variable type is infinite; the compiled proof and
boundary checks establish this for the actual project predicate.

## Structure, packing, orientation, and casts

Naming gate PASS: public `boxFamily_finite` correctly names the family property; no rename.
Structure gate PASS:13 proof lines,0 branches, no haves/options/simp blocks, no useful
helper extraction. Existing three helpers were not edited or credited again.
Original one-line signature width87. Final two signature lines have widths88 and32.
Appending the whole next conclusion `(boxFamily r B).Finite := by` (28 including its
proper separator accounting) to the first line requires117>100, so the break is necessary.
Actual width100 `#check` also breaks after the binders. A provisional width field excluded
`:= by`; final `source-protection17.json` measures the complete signature lines.

| Final declaration line | Unicode codepoints |
|---|---:|
| 1 | 88 |
| 2 | 32 |
| 3 | 11 |
| 4 | 88 |
| 5 | 69 |
| 6 | 39 |
| 7 | 12 |
| 8 | 27 |
| 9 | 45 |
| 10 | 61 |
| 11 | 29 |
| 12 | 97 |
| 13 | 30 |
| 14 | 46 |
| 15 | 77 |

All body lines≤97. The coefficient image/refinement and final expression continue across
lines at expression boundaries; no isolated binder/quantifier fits by joining its whole
next syntactic unit within100. One extra proof line was removed by packing the inner pair
refinement; every final gate was rerun after that source edit.

| Inequality scan | Occurrences | Decision |
|---|---:|---|
| old/new declaration signature `≥` or `>` |0| no orientation rewrite applicable |
| added public documentation |0| prose states positive degree bounds |
| retained proof inequalities | no ≥/> notation | bound.trans and Nat.eq_zero_of_le_zero use canonical ≤ direction |

No casts were present in the old proof. `(0 : ℤ)` in the new coefficient interval is
load-bearing: dropping it in a standalone whole-file probe exits1 with coefficient-array
Nat/Int mismatch and strict closedness rejection. It remains. No resource limit increase,
new global instance, or global simp/grind attribute was introduced.

## Final builds, diagnostics, and independent semantics

All commands were serialized and fully drained. Exact executable/argv/environment,
source17pins before/after, input hashes, PIDs/PGIDs, stdout/stderr hashes, UTF8 validation,
elapsed, timeout and exit are stored per run in corresponding `.json` records.
CLI uses `/Users/ramin/.elan/bin/lake`; compiler invocations use `env lean -j1`.

| Run | Whole exit | Wall seconds | Role |
|---|---:|---:|---|
| `before17-affected-build` | 0 | 3.066760458 | entry baseline |
| `before17-full-build` | 0 | 6.830726250 | entry baseline |
| `final17-affected-build` | 0 | 79.967684833 | historical intermediate only |
| `final17-packed-affected-build` | 0 | 77.131935209 | final packed source |
| `final17-independent-v2` | 0 | 208.323614209 | final packed source |
| `final17-full-build` | 0 | 39.980263708 | final packed source |
| `final17-eval-build` | 0 | 39.688400416 | final packed source |

`final17-affected-build` used709-line intermediate source SHA
`bce0fb555349b2ba06638f17053ee0b63eb30336786b5ce40949c1102ad085c7`.
The exact bytes are preserved in `intermediate17-unpacked-source/Roth/MainLemma.lean`,
reconstructed by reversing only the recorded packing edit; hash equals that run's actual
before/after source pins. `intermediate17-source-binding.json` and reversible
`intermediate17-to-final-packing.diff` bind it. This successful historical run is never
substituted for the final packed gates.

Fresh full unfiltered final native diagnostics: MainLemma, Main, LeanEval all success,
nonpartial, nontimeout, no failed dependency, zero errors. Existing warning counts1/4/0:
MainLemma preserved metadata header; Main preserved header and unused hδ/hQ/hc warnings.
Baseline full ML/Main diagnostics similarly zero errors with1/4 old warnings. Warnings
are disclosed, not suppressed or called warning-free.

Independent V2 whole run exits0. Harness SHA
`4c958f75b7bf3d79da4ab8bf18a5272a8fbef986f4c6ac2dbf3c9d085d6e1ae3`;
raw stdout SHA `c2e4d1f6888268ab728ced937a5956372c0e14bc0516b607da3cad50eb9d110b`.
It clones the entire byte-exact entry MainLemma and eight genuine project-original
declarations including original family DATA, ctor, coefficient/range/injective proofs,
original17 finite theorem, cardinality support, and actual original consumer.
The project-original source SHA is
`a3d09825fb878c5d512cfdd3feca517465e0a8215807b1261b988f664915f3a8`.
No original range RHS accidentally resolves the current family.

V2 checks14 complete contracts (old/current/expected generic types and separate genuine
Fin m adapter), exact written binder names/order/BI/universes and all effective inner
binders, raw TYPE AST and actual isDefEq. Actual DATA values also checked. Only six named
DATA definitions unfold, with restricted application-spine beta reduction; only generated
macro scopes normalize on both sides. No arity/name-map repair or proof-irrelevance
shortcut replaces the actual comparison. Forty-two actual TYPE and opaque value!true
closedness/inferred-type/axiom guard occurrences reject expr/universe metavariables,
fvars, loose binders, sorry, or inferred-type mismatch. Four inherited unchanged-arity
paper-name maps are unused by compared contracts; no changed-arity map is present.
Fourteen old transitive TYPE+opaqueVALUE project closures ban current target, callers,
family/constructor/coefficient/range and all three retained helpers. The actual original
finite proof is required to use the genuine original range. Standard axioms only:
`propext`, `Classical.choice`, `Quot.sound`.

Eight actual theorem property-boundary checks: Fin0 empty indices, coefficient bound0
with finite indices, generic merelyFiniteσ, Bool, lifted-universe Bool, generic Finsupp
bounds, infiniteNat all-zero bounds, and infiniteNat single-supported bounds.
These are actual family membership/finiteness checks, not just DATA applications.
No builtin heartbeat count is claimed; bounded harness options are recorded and not raised.

## Profiling and complete provenance

Exact CLI: `lake env lean -j1 --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 FILE`.
Both frozen scopes preserve the complete target and sole direct-consumer command bodies,
types and order; standalone trace options are inserted before attached docs, not inside
a declaration. `scope17.py`, `scope17.json`, and provenance records bind the scaffolds.
Actual imported TYPE+opaqueVALUE inventory selects the consumer. Parser scripts verify
exact declaration token+separator, qualified proof, disjoint column0 command/proof/kernel/
linter roots, no nested Meta events, no next-command leakage or end doublecount.

The historical first BEFORE sample (`before17-first`,51.428s) has16.149ms target and
314.735ms consumer, with package-only catalog evidence. It is retained separately and is
not the accepted matched numeric comparison. A later exact frozen BEFORE-source replay
under freshly observed full core-superset provenance closes this gap without rollback,
importing unchanged Lattice/Theta/mathlib rather than current MainLemma.

| Accepted matched scope | Recovered BEFORE ms | Final AFTER ms |
|---|---:|---:|
| `Roth.boxFamily_finite` |17.129|38.964|
| complete `Roth.exists_ne_modByMonic_eq` command |320.078|260.369|

Every target/consumer/group row is<750ms, so mandatory repeat was not triggered.
No aggregate speedup, cherry-picked repeat, heartbeat, or GLOBAL claim is made. The
stronger theorem modestly increases target cost. Recovered BEFORE wall53.6130955s,
AFTER54.743104709s; whole logs exit0 and are drained. Four exact target roots each.
Raw matched BEFORE SHA `696cf28f63b5d288565c99c747bdd119d1c0fdf226517e14710a651083ffdaf7`;
AFTER SHA `01855820e38fc45eef7d21ba995c7e4ce8e96755e2af2a1b7f127b32bcc2e058`.

Before API edits,17 fresh source/config copies and104 cache companions were frozen and
the predecessor package/project setup.importArts union freshly rehashed:12201 artifacts,
1803538672bytes. Final package/project union:12201 artifacts,1803563080bytes, no added or
removed paths, one changed artifact MainLemma.olean. The source has an added direct
import, but it was already transitive: actual ML/Main setup bytes, options, importArts
sets and actual environment bytes compare equal. This is observed, not assumed.
The final17 source/cache copies and actual full artifact catalogs retain all individual
paths, byte counts and hashes. Physical project-source pins for replay and AFTER match;
the replay's separate exact frozen old input is expressly recorded, not confused with
current production source.

CORRECTION: setup.importArts package union is NOT an exact full loaded closure: implicit
Init and other pinned core modules may be omitted. A later `--deps` recovery on the exact
frozen BEFORE bytes discovered this omission; this is explicitly a later provenance
command, not a historical timing command. Its explicit dependencies were verified against
the frozen BEFORE package artifacts. Implicit Init is bound only to the newly observed
core catalog; no historical core-beforeAPI hash claim is made. Failed initial strict
assertion is retained as rejected evidence. See `catalog17-terminology-erratum.md`,
`direct-deps17-verified.json`, and both actual deps streams.

The newly observed full installed pinned-toolchain compiled-artifact SUPERSET contains
12592 files,2125623224bytes. It is a SUPERSET, not the exact loaded closure. Pre/post
recovered matched-pair catalogs actually hash equal, with equal actual raw environment
SHA `8210989d6ba2454e80d0c1b90d71c5ddb0cde44c80fbcfa469b72a11e5a41041`.
Lean/lake executable/path resolution is separately recorded. This supports the new
replayed comparison only, without retroactive repair of the initial historical sample.
Mutable owner state is historical context, not an immutable evidence input.

## Rejected evidence and honest failures

- Initial support probe wrongly assumed the new AddMonoidAlgebra structure was defeq to
  Finsupp: whole exit1/sorryAx, rejected. V2 standard constructor-image proof exits0.
- Initial alternatives run had a good marker but unresolved infinite-counterfixture:
  whole exit1, rejected; corrected V2 whole exit0 proves both alternatives.
- Negative removal/Sort* probe whole exit1 is expected falsification, not a positive gate.
- Old and new whole-proof grind/simp/aesop probes fail. Old exact? fails. apply? may
  report zero goals alongside synthetic admission/partial suggestions; rejected. A simpa
  experiment followed by a now-extra tactic reports no goals and is not credited.
- Independent V1 wrongly compared generic Entry range with concrete Fin m adapter:
  entire exit1 after192.672s is rejected despite partial PASS markers. Attempt to signal
  only its owned group was denied; denial preserved; bounded process finished naturally
  and drained before V2. No broader process action or concurrent V2 occurred.
- Initial direct-deps catalog assertion failed on implicit Init; terminology/provenance
  corrected as above, failed script retained. Initial same-basename skill-copy metadata
  was invalid and is marked so; corrected distinct skill snapshots/provenance retained.
- Removing the Int ascription whole exit1 confirms it is necessary; final source unchanged.
- Local index errors and wrong-line references are retained; compiled name checks and
  corrected references provide positive evidence, not empty search results.

## Final diff gates and eleven-phase checklist

Gates: PASS for this leaf's packed source: no new target diagnostic, unchanged standard
axioms, full contract/closure compatibility, ordinary structure, naming, line packing,
inequality orientation, comments/source preservation, matched scoped profile, affected/
full/separateEval builds, and complete final native diagnostics. No defer of a failed
leaf gate. Rules applied1.6,1.11,1.17; all42 rule statuses reproduced below.
Renames-queued: none. Refactoring needed: none. Comments-preserved: no target proof
comments existed; original public source prose and seven signposts preserved. Own doc
updated and only the authorized added original12 sentence corrected.

- [✓] Step1: all mandatory reference docs read, exact corrected input provenance retained.
- [✓] Step2: full24 audit reproduced with final resolutions above.
- [✓] Step2.5: all five actual mathlib searches, errors and positive fallback disclosed.
- [✓] Step2.6: complete outer/inner hypothesis, candidate, literature and application pass.
- [✓] Step2.7: per-line codepoint table and actual width100 reference printed.
- [✓] Step2.8: inequality orientation scan table printed.
- [✓] Step3: every one of42 golfing rules has a status below.
- [✓] Step4: actual step-back reflection below; no helper/decomposition needed.
- [✓] Step5a: full final ML/Main/Eval native diagnostics complete, zero errors, old warnings disclosed.
- [✓] Step5b: full final diff gate block above and raw source-protection record retained.
- [✓] Step6a: no rename required; sidecar exact and untouched.

Owner still must review, run own full/separateEval/root native, stage/hash/publish clean
before18. Fresh independent whole-file simplify, cumulative original-public DATA/axiom/
import/docs/source checks and GLOBAL remain mandatory after27. Known old GLOBAL failures
(delta11188.775ms,pigeon1000.235ms,main4880.648ms) are not resolved or credited here.
Artifact manifest excludes itself to avoid a hash cycle, includes this report and every
actual evidence-root file plus referenced immutable parser scripts. Catalogs separately
bind all external package and core-superset artifacts. Final drain record binds every
owned PGID and checks current17source/config pins and104 cache companions before release.

## Historical before-edit audit and complete golfing-rule record

The following preserves prospective/pending language as a BEFORE record. Its claims about
12201 'all imports' are superseded by the explicit package/core terminology correction
above; final resolved results and accurate provenance are the preceding sections.

# Original17 before-edit audit: Roth.boxFamily_finite

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md. Lean4/mathlib-quality skills,
cleanup/cleanup-all/buzz, 854-line verbatim prompt (1–300/301–600/601–854),
112-line scope instructions, style/naming/profiling/review/principles references read.

## Phase0/1/2/3

Affected build exit0,3.066760s; full build exit0,6.830726s. Full native ML success,
complete/nonpartial/nontimeout0errors1existingheaderwarning; Main same0errors4oldwarnings.
Classic dialect. Original17 is ordinary, not a module headline. No file-level fixes
are licensed by this leaf; existing author metadata and imports preserved until a
necessary import is justified. Scope:17only, its doc, one added12docsentence, necessary
narrowcalls, report. Main and three retainedhelpers/renamequeue protected.
Fresh17source/config17pins and104cachecompanions frozen. All12201actualimports
1803538672bytes freshly hashed; prior16external catalog only after actual verification.
Source/LSP references (3positions) and actual imported TYPE+opaqueVALUE inventory agree:
exists_ne_modByMonic_eq plus its generated _proof_1_1; the latter belongs to the same
complete parent command and is not counted twice. Their full types/bodies/order are
preserved by the scoped source. BEFORE complete command/proof/kernel/lint roots:
target16.149ms, directconsumer314.735ms; both<750, no repeat required before editing.

## Full24 audit

1. LINT: no target warning; existing headerwarning preserved by user decision.
2. HAVE: none in old proof. No inline candidates.
3. SET_OPTION: none, no limit changes.
4. SIMP: none in old proof; no squeeze candidate.
5. NAMING: boxFamily_finite names family plus standard finite suffix; no forbidden
   pattern or abbreviation. No rename needed; queue remains exact4.
6. LINE PACKING: original one-line signature87codepoints (machine table follows).
   New signature will pack every binder/conclusion with measured arithmetic.
7. BY: attached to declaration line.
8. FORMAT: two proof lines/two-space indent; no empty internal line or haveI/letI.
9. COMMENTS: none in target proof; all seven file signposts protected.
10. DOC: public one-sentence finite-family statement; update for actual selected
    finite-support hypothesis and indicate infinite ambient indices are allowed.
11. VISIBILITY: retain public reusable finiteness API; automatic finite-index instances
    and explicit finite-support bounds are valid applications beyond this local caller.
12. STRUCTURE: old2prooflines, no conjunction in conclusion/branches. No helper needed.
13. MATHLIB: five actual methods executed; partial match Finset.finsupp and
    mem_finsupp_iff enumerate functions on finite supports. No exact boxFamily lemma;
    predicate is project-defined. Build directly on this standard API if support route
    succeeds; no new wrapper/helper declaration.
14. JUNK DEF: n/a, theorem.
15. EXISTS: n/a, not an existential/private witness declaration.
16. SHOW: none.
17. PUSH_NEG: none.
18. GENERALISE: test arbitrary-universe finiteσ without Fintype/DecEq; additionally
    test natural strictly weaker Finite(Function.support r). Preserve integer
    coefficient predicate and all oldFinm contracts. Details below.
19. INEQUALITY: no ≥ or > in original signature; final signature likewise has none.
20. NORMAL-FORM: Set.Finite on existing family is canonical, no equivalence layer.
21. SYNTAX-GEN: finite-support subtype class is standard Set.Finite (definitionally),
    automatically synthesized for Finiteσ, and admits infinite ambientσ. Compare its
    application interface with simpler Finiteσ rather than inventing default wrappers.
22. IMPORT-FANOUT: support route uses Mathlib.Data.Finset.Finsupp, already present in
    the actual import closure; add direct import if selected. No extra closure fanout.
23. CASTS: old proof no explicit casts. New `(0 : ℤ)` determines coefficient interval;
    retain only if elaboration needs it, no redundant old casts.
24. INSTANCE-NAME: no global instances introduced; local classical only.

## Generalisation2.6a–e (outer and inner target pass)

| Parameter | Role/use | Candidates / verification |
|---|---|---|
| m:ℕ | ambient Fin m size | replace with arbitrary-universeσ; finiteσ proof pending |
| r:Fin m→ℕ | coordinate degree bounds in family | domainσ; retain ℕ as intrinsic degrees; drop-test pending |
| B:ℕ | natural coefficient bound in integer family | fixedDATAsemantics; drop-test pending |
| finite ambient indexing | implicit concrete Fin instances | try no finiteness, then finite support r, then merelyFiniteσ; no DecEq/Fintype in statement |
| universe | Fin m is small | σ:Type*, Sort* rejected only after actual test |

No strict premise, analysis/algebra class, pointwise hypothesis or bundled conjunction
exists to weaken/unbundle. Inversion check: after range rewrite old proof is the
mathlib fact finite_range, but the new content is precisely showing this concrete
family has finite monomial/coeff support. The abstraction is Finset.finsupp, already
in mathlib, so no new abstract wrapper.

Finite-support prospect uses Finset.finsupp twice (finite exponent vectors, then finite
coefficient arrays), with AddMonoidAlgebra.ofCoeff transferring arrays to polynomials.
First failed candidate incorrectly treated the new monoid-algebra structure as defeq to
Finsupp; retained exit1/sorryAx evidence is rejected. V2 image-ofCoeff candidate exits0
with only propext/Classical.choice/Quot.sound. This gives real new applications:
σ=ℕ with r zero except at finitely many indices, requiring no enumeration of ambientσ.
This is not dismissed on cost and needs no helper. Existing r/B explicit order remains.

Literature queries/top results preserved in literature17*.json. General polynomial
formulation is finite sums of monomials, including infinitely many ambient variables;
finite allowed exponent support and finite coefficient choices ensure finiteness.
Mathlib's actual Finset.finsupp implementation supports that formulation. ChatGPT math
MCP unavailable in tool inventory. Primary actual source consulted, remote search
version hits treated only as leads, never as proof of pinned APIs.

## Five-method search

A Lean-Finder actual query bounded coordinate degree/finite coefficients: module-finite
restrictDegree/restrictTotalDegree and Finsupp.finite_of_degree_le are partial matches.
B Loogle actual Set.Finite,MvPolynomial:0hits.
C LeanSearch actual finite support/finite values:Finset.finsupp,mem_finsupp_iff,onFinset.
D pinned source:untruncated search17-source.txt plus explicit Finset.Finsupp source.
E actual local finite/name lookup:index warming, therefore no absence claim from index;
pinned source and compiled uses supply positive verification.
Auxiliary variants inspected:finite_range,finite_subset,finite preimage/image,
finite intervals,Finsupp finite_of_degree_le, Finset.mem_finsupp_iff.
Common-equivalents finite-subset bucket applies to enumerated arrays.
Issues: select evidenced general API, update own doc/one authorized added12sentence,
verify old callers/contracts and all matched final gates. No renames/decomposition.

## Golfing-rule pass (all42)

1.1 n/a:no by-exact wrapper. 1.2 n/a:no by-rfl.
1.3 n/a:rw changes membership forms before refining, no following exact using that rewrite.
1.4 n/a:no simp+exact. 1.5 n/a:no trailing rfl after simp.
1.6 applied:anonymous pairs/witness instead of constructor branches.
1.7 n/a:no apply+exact chain. 1.8 n/a:no contradiction+pushneg.
1.9 n/a:lambdas bind membership proofs, not eta expansions.
1.10 n/a:no have; local s is used to construct the coefficient support enumeration.
1.11 applied:function proofs introduced directly by refine lambdas.
1.12 n/a:no show. 1.13 n/a:no paired have projections.
1.14 n/a:membership rewrites are separated by refinements changing the goal.
1.15 n/a:no simp only. 1.16 n/a:no nonterminal simp.
1.17 applied:finite_toSet.image/subset, bound.trans, standard dot notation.
1.18 n/a:no removable terminal parentheses requiring <|.
1.19 n/a:no push_neg. 1.20 n/a:not a trivial private existential.
2.1 actual old and new generalized whole-proof grind probes failed.
2.2 n/a:no grind in retained proof.
2.3 n/a:no simp followed by closing tactic.
2.4 n/a:no analytic function property.
2.5 n/a:no positivity goal; coefficient interval membership directly consumes hW.2.
2.6 n/a:no monotonicity/calc goal requiring gcongr.
2.7 n/a:no stand-alone arithmetic goal; explicit Nat.eq_zero_of_le_zero consumes bound.
2.8 actual old and new generalized whole-proof aesop probes failed.
2.9 n/a:no concrete numeric calculation/cast-equality goal.
2.10 n/a:arbitrary polynomial-set finiteness has no computational decidability proof.
2.11 n/a:no field denominators or ring equality.
2.12 n/a:no ring/ring_nf with hypotheses.
2.13 n/a:no symmetric cases.
2.14 n/a:no calc chain.
2.15 n/a:refined obligations have distinct mathematical roles, no identical tactic.
3.1 n/a:no erw. 3.2 n/a:no legacy continuity/measurability.
3.3 n/a:no omega/lia in retained proof.
3.4 n/a:no rcases-rfl. 3.5 not added:finite-family result is not a rewrite normal form;
no new simp/grind global registrations needed for the direct caller.
3.6 n/a:no simp_all only. 3.7 n/a:no resource options.

## Step back

The original short parametrization proof only works when all ambient variables form a
finite type. The direct standard finite-support enumeration proves the stronger theorem
without a new helper or a new family definition. One finite enumeration controls exponent
vectors, another controls coefficients; image of the standard coefficient constructor and
subset close the result. No repeated proof skeleton needs extraction. No hand-built
monomial array API or typeclass wrapper is introduced. The shorter original finiteσ
route was actually compiled; stronger support generality is the reason for the longer
proof, with exact old contracts checked separately. Old exact? failed; apply? yielded
partial suggestions/zero-goal diagnostics and is explicitly rejected as proof evidence.
No global /simplify or whole-file final performance completion is claimed by this leaf;
those mandatory fresh final-file gates remain with the owner after original27.
