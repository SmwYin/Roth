# exists_norm_coeff_reduction_aux — fresh helper3 audit

Status: complete helper audit, pending owner review and publication. No original264 theorem credit is claimed. The SAME original11 worker must resume its remaining gates after this helper release. Source/compiler/native/profile/report/helper leases are released only by the final release record.

Final source SHA256: `05967520b94e30cefb4984a9f29cbe418e17c71db1e4c93c647f23a27e737382`, 707 lines. Entry SHA256: `8f88bdc8ffc4808ef41146886a6ffe0c84090c6368680a815b3d1f49297fea5c`, 711 lines. Only the private helper changed. Its public caller retains 15 body lines and longest induction branch10. The helper now has 5 signature lines, 27 body lines, degree branch4 and coefficient branch8. Other16 source/config pins, all foreign MainLemma bytes, public headline/body/docstring, existing four-entry rename queue and Main source remain byte-identical.

Implemented: pack every signature line maximally within100 codepoints; pack the final remainder field into its tuple; replace a single-use anonymous degree inequality plus lia with `Nat.le_sub_one_of_lt` and transitivity; use the equally short direct contradiction `fun h ↦ hself (by simp [h])`. The intermediate aesop candidate is retained and explicitly superseded because its bounded heartbeat count increased. No new production helper, import, option override, rename, axiom, admission, limit raise or weakened conclusion was introduced.

## Final24-check closure

|Check|Final disposition|
|---|---|
|1 lint|Affected build and both full native files complete with0errors; existing warnings preserved below; no helper-local warning|
|2 have scan|Derived anonymous Nontrivial/hf/hP0/hdeg/hmod/Q are shared or essential; inline the single-use anonymous degree have. hP0 uses direct lambda; hdeg is used three times|
|3 set_option|No production overrides; effective bounded limits200000/20000/depth512|
|4 simp squeeze|All selected simp/simpa calls terminal in their branch; no nonterminal broad simp|
|5 naming|Private mathematical exists_norm_coeff_reduction_aux retained; no rename needed|
|6 packing|All five signature lines quantified below; each next indivisible unit exceeds100|
|7 by placement|All by tokens on preceding statement line|
|8 formatting|Two-space proof/four-space signature, no blank proof lines, no haveI/letI; tuple packed|
|9 comments|No internal helper comments existed or were removed; foreign comments protected|
|10 docs|Private helper had no docstring; unchanged|
|11 visibility|Private helper, sole narrow direct caller preserved|
|12 structure|27 body/8 longest branch; public15/10; substantive algebraic extraction|
|13 mathlib|All five actual methods and partial matches recorded below; whole automation attempts preserved|
|14 junk definitions|Theorem; no production definition introduced|
|15 exists|Witness has genuine degree, norm and remainder obligations; not a trivial tuple wrapper|
|16 show|No redundant show|
|17 push_neg|No applicable negation chain|
|18 generalization|Every effective outer/inner binder audited; actual drop tests and independent countercertificates below|
|19 inequality|Helper statement contains six ≤ and one <, all smaller-left; zero ≥ or > comparisons|
|20 normal form|natDegree, modByMonic and real norm match pinned API; natural subtraction handles s0|
|21 syntax generalization|Existential witness abstracts the elimination expression; current type identical to entry|
|22 imports|No added imports; complete actual setup/import catalog recorded|
|23 casts|No redundant numeric casts; explicit synthesis annotations retained|
|24 instances|Anonymous Nontrivial derived from hself; no named instance introduced|

## Final correctness, independence and provenance

The genuine saved firstdraft and full context remain immutable. `firstdraft-exact` compiled the extracted proof with only fresh declaration name/namespace, exit0 without repairs, preserving unused-hf1/unnecessarySimpa warnings. A separate exact firstdraft actual opaque VALUE guard also exited0. This does not claim its enclosing historical file compiled. Its NormedCommRing+Nontrivial domain and smaller existential conclusion differ from the current SeminormedRing contract with additional positive-degree/cap outputs.

`independent-final-direct` freshly elaborates the genuine firstdraft, an independently written expected-current proof, a public-consumer proof using that independent proof, and a projection of the actual helper onto the exact old contract. All three type pairs pass full AST/binder names/order/BinderInfo/universe comparison (raw retained; only generated macro scopes normalized), definitional equality, and exact universe parameter checks. Both TYPE and actual opaque VALUE are closed, contain no expression/universe metavariable, loose bound/free variable or sorryAx, and VALUE's inferred type equals the declared type. Allowed axioms are exactly the standard propext/Classical.choice/Quot.sound set. Dependency closure checks ban current helper/public from the independent proofs. Actual private imported name is `_private.Roth.MainLemma.0.Roth.exists_norm_coeff_reduction_aux`; constants generated using mkConstWithFreshMVarLevels end fully instantiated. Scratch countercertificates and automation fallback proofs receive the same actual-VALUE guard. Every rejected universe/API/automation scratch run remains evidence, never an accepted partial PASS.

`lake build Roth.MainLemma Roth.Main` (`final-direct-affected-build`) exited0 in67.922s. Final imported helper/public semantics and transitive Main theorem semantics separately exited0. Native diagnostics used full file paths with no line/declaration/severity filter: both complete, success true, partial false, timed_out false, failed_dependencies empty,0errors. MainLemma retains one copyright-header warning; Main retains that header and three unused-variable warnings. Native output JSON is retained in full. No claim of zero warnings.

All17 current pins and104 actual project cache artifacts/companions are physically preserved before/final. Exact frozen setup JSON bytes, importArts, options, package/module metadata, plugins and dynlibs agree. Complete actual setup resolves12,201 union artifacts totaling1,803,543,032 bytes. All current artifacts were freshly hashed:12,190 external artifacts match the accepted immutable prior catalog;11 project artifacts map to the actual entry/final saved binaries. The reconstructed BEFORE explicitly reuses that accepted external baseline; it is not labeled a new prospective pre-edit full hash. The full MainLemma profile import set has12,185 artifacts, with all hashes equal before/final. Only Main's imported MainLemma.olean changes in the union. Direct68/99-file catalogs are supplementary direct dependency scope, never described as full transitive closure. Each full import binary actually failed strict UTF8 decoding and has an explicit binary exception. Setup/catalog paths and hashes are retained; no extra compiler probe was used for cataloging.

## Performance and complete profile roots

Both AFTER samples use final frozen source and rebuilt imports, identical CLI/options/environment/import identity to BEFORE. Commands are `lake env lean -j1 --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 <before/after-scoped.lean>`. Scoped source recovers the complete canonical file after removing only the matching trace toggles. Raw stdout/stderr are separate strict UTF8 files. Complete unique declaration spans use only column0 Elab.command/Elab.async roots including proof/kernel/lint, excluding nested Meta/children, next commands and trailing end double counts. Exact standalone qualified private proof name is `_private._stdin.0.Roth.exists_norm_coeff_reduction_aux`. The unmodified owner parser and exact-name completeness verifier accept every row. No omitted failed profile or third unchanged cherry-pick. The first BEFORE combined755.540ms mandated repeats of both sides even though the second BEFORE was smaller.

|Sample|Helper ms|Public consumer ms|Combined ms|
|---|---:|---:|---:|
|before|319.452|436.088|755.540|
|before-repeat|312.552|416.949|729.501|
|after|236.507|439.363|675.870|
|after-repeat|228.563|429.472|658.035|

Both final combined rows are below the meaningful1000ms ceiling. Optional bounded custom heartbeat wrapper preserves positive defaults and temporarily disables async only in the scratch measurement. Entry helper2782/public5374 user heartbeats; rejected intermediate aesop3485/5391; selected final direct2085/5386. The public count increased slightly; no public-only speedup claim. No built-in max0 figure is accepted.

## ModeB phases and final11 checklist

0 inventory: frozen entry, original worker partial handoff, immutable actual firstdraft/context and all17 pins saved. 1 initial per-declaration24 audit recorded before edits. 2 all42 golf rules, five actual search methods, automation and counterexample checks recorded below. 3 file-level header/import work is foreign protected scope; no hidden file cleanup. 4 final affected build/imported semantics/native complete. 5 statement/binders/generalization/packing/inequality/source protection complete. 5b no helper rename, existing queue bytes preserved. 6 fresh matched scoped BEFORE/AFTER repeats complete; full-file/global all-row profiling remains original11/owner scope. 7 report, complete artifact manifest, frozen hashes and actual process-group drain/release provided.

Final11: (1) full instruction/skill/source/context reading recorded; (2) all24 checks closed; (3) all42 statuses recorded; (4) five actual searches plus generic automation probes; (5) independent genuine firstdraft/current expected proof/old projection exact full AST+actual VALUE guards; (6) all binders/hypotheses and generalization/counterexamples; (7)100-column maximal packing and smaller-left orientation; (8) foreign bytes/public15/source/config protections; (9) fresh affected build, full native and imported semantics; (10) complete anchored profile pairs, positive bounded heartbeat figures, matching setup/imports; (11) full raw artifact manifest, source freeze and all owned jobs drained before explicit lease release. No Git or shared progress mutation and no credit publication by this worker.

## Final signature packing

|Signature line|Codepoints|Next indivisible signature unit|Arithmetic|Action|
|---|---:|---|---|---|
|201|97|`{A C : ℝ}`|97+1+9=107>100|ok|
|202|78|`(hs : P.natDegree ≤ s)`|78+1+22=101>100|ok|
|203|99|`∃ Q : Polynomial R,`|99+1+19=119>100|ok|
|204|80|`P %ₘ f = Q %ₘ f := by`|80+1+21=102>100|ok|
|205|25|none|n/a|ok|


# Helper3 detailed audit and golf record

## Mathematical content and contract boundaries

One step of division by a monic polynomial cancels the dividend's leading term. Its new
polynomial has lower degree, the same remainder, and coefficient norm at most
`C + A*C = (1+A)*C`. The remainder implementation in pinned `Div.lean` uses
`P - f*(C P.leadingCoeff * X^(P.natDegree-f.natDegree))`; respecting that multiplication
order is essential over noncommutative rings. This is substantial algebraic extraction,
not a wrapper for one to three mathlib calls or a trivial existential tuple.

The genuine firstdraft has NormedCommRing+Nontrivial assumptions and only the existential
output. It independently compiles unchanged apart from a fresh declaration name and namespace,
then passes the closed TYPE/actual opaque VALUE/inferredtype/standard-axiom guard. Its weaker
output explains the unused hf1 warning. Current positive-degree output makes hf1 necessary.
Neither exactfirstdraft run required repairs. Every firstdraft byte/hash is retained.

## Five-method search status

A. Lean-Finder: actual query `Polynomial remainder by monic one leading term subtraction norm
coefficient bound`; results include Polynomial.div_wf_lemma, sum_modByMonic_coeff,
coeff_divModByMonicAux_mem_span_pow_mul_span, modByMonic, natDegree_modByMonic_le.
B. Loogle: actual pattern `Polynomial.modByMonic, Polynomial.coeff`; results include
sum_modByMonic_coeff and coeff_modByMonic_mem_pow_natDegree_mul.
C. LeanSearch: actual `Polynomial remainder by monic coefficient norm bound after leading
coefficient reduction`; results include divModByMonicAux/modByMonic/field-division building blocks.
D. Full untruncated pinned source search: saved source-search.txt for exact proposed helper,
norm/modByMonic combinations, coeff_modByMonic, degree/remainder/coefficient APIs.
E. Actual local name search `modByMonic` returned22matching names; index reports unavailable,
so its empty-result absence guarantee is not asserted. It returned genuine textual matches.
Auxiliary variants searched: _of_dvd_sub, _eq_of_not_monic, _eq_self_iff, divModByMonicAux,
coeff_mul_C, coeff_mul_X_pow'. Common-equivalents table: no applicable disguised concept.
Conclusion: partial mathlib matches used DIRECTLY. No ready-made quantitative reduction theorem
was found. Compiled generic exact? fails; apply? produces an apparent partial success whose term is
explicitly rejected as open/sorry-containing. This is a statement about searches/probes, not a claim of exhaustive
mathematical absence from all possible mathlib formulations.

## Literature and inversion check

Although private-helper literature is normally out of scope, explicit dispatch requires it.
Three actual single-query responses and their first3returned blocks are preserved separately:
monic division coefficient bounds/generalization; monic division over noncommutative rings;
Roth coefficient-bound growth. The third query mostly returned unrelated results; no support
is inferred from those results. Initial combined query additionally found the primary paper
*General remainder theorem and factor theorem for polynomials over non-commutative coefficient
rings* at https://uvadoc.uva.es/handle/10324/78208 and author material for ring division.
These motivate checking noncommutative multiplication order; acceptance rests on actual Lean
certificates. No math-second-opinion MCP is exposed. No unverified maximal-generality claim.
Inversion check: n/a, already abstract/typeclass-parametric with arbitrary f,P,A,C,s; no
concrete named object disappears after unfolding.

## Generalisation 2.6a–e: every outer and inner effective signature binder

|Binder|Class/use|Drop/weakening candidates and verification|Disposition|
|---|---|---|---|
|universe u_1|type level|already Type*; dropping would specialize, not generalize|keep polymorphic|
|{R : Type*}|type variable|used by polynomial and seminormed-ring data; deletion makes dependent signature ill-formed|keep|
|[SeminormedRing R]|typeclass|already drops NormedCommRing's commutativity and separation; NonUnital parent lacks1/monicity; Ring parent lacks norm estimate; SeminormedAddCommGroup lacks ring/division/submultiplicativity|keep natural weakest bundled class supporting written API|
|{f : Polynomial R}|structure value|divisor appears in hself and all degree/remainder outputs; deletion loses mathematical object|keep arbitrary|
|{P : Polynomial R}|structure value|dividend in hP,hs,hself,remainder equation; deletion loses input|keep arbitrary|
|{A : ℝ}|bound value|arbitrary real, not restricted positive; hfA at0 implies0≤A; abstract ordered codomain would require changing norm's real codomain|keep|
|{C : ℝ}|bound value|arbitrary real, hP at0 implies0≤C; no independent sign premise|keep|
|hfA|proposition|drop tested; coefficient estimate consumes it; A=-1,C=1 countercertificate makes output bound0 impossible|keep|
|inner i:ℕ in hfA|index|all coefficient indices needed for requested uniform estimate; restriction to ≤natDegree is equivalent using zero coefficients+A≥0, no mathematical gain|keep uniform quantifier|
|hP|proposition|drop tested; P=X+1, f=X, C=0 countercertificate makes output impossible|keep|
|inner i:ℕ in hP|index|every dividend coefficient and leading coefficient can enter one elimination; localization to finite support is equivalent with derived nonnegativity|keep|
|{s : ℕ}|degree cap|arbitrary natural; deletion would restate output/consumer recurrence, not drop an unused parameter|keep|
|hs:P.natDegree≤s|proposition|drop tested; X/X withs0 violates returned f-degree cap; weakening to succ cap insufficient for s−1 conclusion|keep|
|hf1:f≠1|proposition|drop tested; 1%1≠1 while natDegree1=0 disproves positive-degree output; unused only in smaller old contract|keep current|
|hself:P%f≠P|proposition|drop tested; f=0,P=0 violates positive-degree output; also supplies monicity and nontriviality|keep|
|existential Q|witness|chosen elimination expression; replacing with fixed/public Q would change abstraction and make caller construct it|keep existential|
|inner i:ℕ in Q coefficient conclusion|index|uniform requested bound; weakening conclusion is forbidden, index type is polynomial exponent ℕ|keep|

2.6b verification uses compiled drop probes plus independently kernelchecked boundary
countercertificates; failed scratch APIs and universe errors are retained as negatives.
2.6c no verified beneficial big-change restatement remains. Bounds only on nonleading divisor
coefficients might support a different sharper theorem, but that is not asserted/proved by this
contract and is not claimed as an implemented generalization. No name/order/conclusion changes.
2.6d actual literature recorded above. 2.6e no production hypothesis was removed; current broad
SeminormedRing domain retained and independently re-proved.

Proof-local binders are also accounted for: anonymous Nontrivial derived from hself; hf is
monicity derived by contradiction; hP0 derived by the selected direct zero-contradiction lambda; hdeg from not-smaller-degree; Q shared
local polynomial; hmod recursive equation; hn in Nat.pos_of_ne_zero excluded by hf1; h in degree
contradiction excluded by hself; hQ0 zero/nonzero split is exhaustive; i in coefficient branch is
arbitrary. No hidden section variables or external decidability/nonzero/sign assumptions.

## All42golfing statuses

|Rule|Status|
|---|---|
|1.1 by exact wrapper|n/a, no whole-proof by-exact wrapper|
|1.2 by rfl|n/a, no reflexivity wrapper|
|1.3 rw+exact→rwa|n/a, final rewritten coefficient goal needs a composed inequality rather than a closing fact already in context|
|1.4 simp+exact→simpa|terminal coefficient branch already uses simpa using mul_nonneg|
|1.5 trailing rfl|n/a, no trailing reflexivity|
|1.6 anonymous constructor|already tuple-built cohesive degree/existential certificate; packed hmod into same tuple line|
|1.7 apply+exact|already direct norm/degree lemma applications|
|1.8 by_contra!|n/a, no push_neg chain; monicity contradiction uses exact negation directly|
|1.9 eta reduction|degree contradiction lambda uses h substantively; hn used by monic degree0 lemma; no eta lambda|
|1.10 inline single-use have|APPLIED: anonymous natDegree inequality replaced by Nat.le_sub_one_of_lt composed with hs; retained hdeg because three times used; class evidence used throughout implicitly|
|1.11 apply+intro|n/a, arbitrary coefficient i introduced for its own estimate; no immediately applied forall theorem|
|1.12 redundant show|n/a, none|
|1.13 obtain projections|already no have-projection pair; consumer destructures certificate once|
|1.14 merge rw|already merged coefficient rewrite list, no consecutive independent rw calls|
|1.15 unsqueeze terminal simp|terminal simp [hQ0] unsqueezed; finalsimpa unsqueezed; no terminal simp only|
|1.16 squeeze nonterminal simp|n/a, none nonterminal|
|1.17 dot notation|already .trans,.trans_le, .2 and direct norm API|
|1.18 <\| over parentheses|n/a, remaining parentheses delimit arguments to multiargument inequalities rather than a final lambda/by block|
|1.19 push_neg|n/a, none|
|1.20 trivial existential|n/a, substantive degree/norm/remainder algorithm, not reflexivity tuple|
|2.1 whole grind|actual repaired plain grind probe fails; first invalid maxSteps config retained, not counted as search success|
|2.2 delete before grind|n/a, selected source contains no grind|
|2.3 simpa consolidation|selected coefficient0 branch already consolidated|
|2.4 fun_prop|n/a, no continuity/differentiability/measurability goal|
|2.5 positivity|actual coefficient subgoal probe fails: not a positivity goal; signs derived explicitly via norm_nonneg.trans|
|2.6 gcongr|actual coefficient subgoal gcongr probe fails to make progress; selected direct add_le_add/mul_le_mul supplies the required norm and sign facts|
|2.7 lia/omega|whole omega and coefficient lia probes failed; original local lia removed entirely via direct Nat.le_sub_one_of_lt|
|2.8 aesop|whole probe leaves goals; local aesop contradiction compiled but increased bounded counts; equally short direct fun h ↦ hself (by simp [h]) selected after closed-value+bounded verification|
|2.9 norm_num/norm_cast|n/a generic bound, no concrete numerals/casts beyond identities; concrete boundary certificates use norm_num|
|2.10 decide|n/a, arbitrary polynomial norm estimates are not finite decisions; no native_decide|
|2.11 field_simp;ring|n/a no denominators; selected noncommutative polynomial identity uses actual recursion rather than commutative ring normalization|
|2.12 linear_combination|n/a, no ring/ring_nf-ending block with algebraic hypotheses|
|2.13 wlog|n/a, zero/nonzero and coefficient shifted/unshifted branches are not symmetric|
|2.14 collapse calc|already composed norm_sub_le.trans and norm_mul_le.trans; no two-step calc|
|2.15 <;> multiple goals|n/a, degree/norm/remainder obligations use mathematically distinct arguments|
|3.1 erw→rw|n/a, no erw|
|3.2 fun_prop legacy replacement|n/a, no continuity/measurability|
|3.3 omega→lia|helper's only arithmetic tactic removed by direct Nat lemma; no omega/lia remains|
|3.4 rfl substitution|n/a, final selected direct lambda internalizes zero contradiction; no subsequent manual redundant simp|
|3.5 automation attributes|private quantified existential certificate not a simp rewrite/normal form; adding global search attributes would broaden unrelated proof search|
|3.6 simp_all|whole simp probe no progress; coefficient simp_all leaves goals; no selected simp_all only to unsqueeze|
|3.7 limits|no limit raises before/after; optionalcustom HB wrapper independently preserves positive defaults|

## Step back / simplify review

Whole rfl/simp/ring/linarith/nlinarith/omega/exact?/apply?/grind/aesop were actually attempted
in a scratch theorem that contains no current helper/target. State is restored after each probe.
No admitted search term is accepted. Current certificate combines three distinct mathematical
facts, so term-only source would obscure the recursive remainder equation and coefficient split.
Its remaining shared hdeg/Q/hmod prevent duplication. A full imported independent proof and
old-contract projection test the abstraction rather than a self-reference. No duplicated new
project API or redundant cast was introduced. Built-in simplify tool is unavailable; this explicit
holistic reuse/quality/efficiency review is the recorded equivalent, not a fabricated invocation.


## Retained negative evidence and final artifact index

Failed `boundaries` v1–v3 API/universe/projection fixtures were repaired independently to v4; failed sharp-extra v1–v2 repaired to v3; drop-probes v1 invalid API and v2 wrong hygienic names are not accepted drop evidence, v3 is accepted; first automation grind maxSteps configuration failure repaired with plain grind in v2. All raw attempts remain. Apparent apply? closure is rejected by the combined open/sorry-containing-term guard, without asserting which disjunct fired. Candidate aesop successful compilation is retained as rejected cost evidence. No false claim that failed scaffolds compile.

Artifact directory: `/private/tmp/roth-mainlemma-norm-reduction`. `artifact-manifest.json` lists every local audit artifact with actual bytes/SHA256 and strict UTF8 result or explicit binary exception, plus this report. `source-freeze.json`, `source-protection-final.json`, `final-source.patch`, `complete-import-catalog-summary.json`, full before/final import catalogs, `profile-comparison.json`, `native-binding.json` and `release.json` are the final review entry points. Historical `initial-audit.md` is retained as prospective evidence; its pending items are resolved by this final report. Intermediate-v3 freeze/cache/source are explicitly superseded, never final AFTER profile inputs.
