# Scoped Mode B cleanup: abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux

Scoped helper audit. Production source734 is `fd03dd6324e75b3ab07865dff1258a352d30403e893716f6e813c738dbd647c2`. Mathematical, structural, build, native and helper performance gates pass. Final artifact-closure/two-rehash/process-drain/seven-lease release and independent owner acceptance are separately bound by the named final receipts; this document does not predate or fabricate those outcomes.

The private coefficient-floor helper now covers every integer divisor, including constants: the unnecessary positive-degree premise `hn` is removed. A monic constant is one and has zero remainder; a nonmonic divisor leaves the dividend unchanged. A shared local estimate handles that boundary case at divisor zero and the positive-degree case. The direct `main_lemma` application drops only its `hdeg` argument. The floor conclusion and public main contract are preserved.

This report owns only helper9 and the necessary narrow caller application. Original27/file/project completion is **not** claimed. Counts remain242/264, MainLemma26/27,10/14 files. Main proof111 still fails its headline15-line target, and its measured timings remain over1000ms. The accepted eight prior helpers, Main689, existing report530, all public docs, all9 standalone comments/all7 historical literal comments (including5main signposts), and paper quotes are protected. No Git, central progress, rename queue, CI, dependency or toolchain write occurred.

## Scope, entry and workflow

Entry MainLemma733 SHA`f6be490cdeb83fd40b3c08b58f15e1c15b166f878cc5002c35fbf7a40cdee230`; Main689 SHA`6668ff83a7e7b156f6f29b8f2d0163e699da002b70338d5ee0715065ade9b25f`; original27 report530 SHA`5e03ca866f6ab2bff0d0cd4b26c4fe8e139de3f52015bcfdbee81d1c98916dd6`. Scratch `P=/private/tmp/roth-mainlemma-helper9-rem-floor`; owner evidence `O=/private/tmp/roth-mainlemma-owner`; accepted predecessor `R3=/private/tmp/roth-mainlemma-main-lemma-resume3`.

The full dispatch, installed lean4 and mathlib-quality skills, full cleanup/cleanup-all/buzz commands, mandatory golfing/proof/search/generalisation/gate/style/naming/profiling/quality/review/linter references, lean4 mathlib-guide/proof-golfing/proof-simplification, complete source733/report530 and relevant clean.tex1450–1575 were read. No applicable AGENTS file was found in the checked ancestor/source directories. This fresh dedicated worker has no children; all compiler/native/profile work was serial. Literal Claude Skill invocation is unavailable: the authorized host adaptation was used, with actual independent owner whole-helper reflection, not a claimed built-in invocation.

Before any Lean or edit, `entry-recovery-v1.json` streamed all48090 accepted current R3 rows/15,745,839,808B/25934 exact binary-provenance rows and inspected complete accepted seal/manifest/rehash/drain/owner-review structures. Original immutable first-ungolfed26-line proof and its entry context were retained among the durable recovery essentials. Prospective source17/cache104/root8/all14 actual setup/package12202/core12592/four proxy+pinned binary observations and frozen parent/raw Lake environments were recorded before runs. These availability catalogs are supersets, not asserted exact loaded closures.

## Full24 audit

|#|Item|Disposition|
|---|---|---|
|1|LINT|No helper-local production diagnostic. Final complete file diagnostics retain only documented inherited warnings; no suppression or limit raise.|
|2|HAVE|Old9: hB0,hA0,hβ0,hNle,hNR,e1,e2,hreal,hcNatAbs. Removed the redundant A/nonneg and Nat-abs intermediates; composed exponent caps. Current7: hB0,hβ1,hβ0,h2',hNR,bound,hreal. hB0 supports multiplication; hβ1 derives β≥1 and the zero-divisor cap; hβ0 supports products/powers; h2' supplies Hasse growth; hNR supplies monomial count; bound is shared by two divisor cases; hreal supplies the floor bridge. Automation may consume facts implicitly; lexical counts are not necessity proofs. hNR,bound,hreal retain nontrivial proof blocks.|
|3|SET_OPTION|No production target option or limit change. Actual default200000/20000/512 checked. Profiler toggles exist only in immutable scratch scaffolds.|
|4|SIMP|All new simp/simpa uses are terminal and were actually compiled unsqueezed, including monic/nonmonic cases, zero-divisor argument and final floor. No terminal simp-only restriction introduced. The protected main simpa-only call is outside helper cleanup and remains byte-exact except removed proof argument.|
|5|NAMING|Descriptive snake_case private `_aux`; no forbidden abbreviation/number/ge/gt/single-letter public name. No rename warranted.|
|6|PACKING|Seven old signature lines become five; complete codepoint/next-complete-unit table below and actual Lean width100 reference retained.|
|7|BY|At end of the conclusion line; local bound and hreal follow the same form.|
|8|FORMAT|Two-space proof indentation, four-space signature continuation, no empty target proof lines, haveI/letI, deprecated lambda/push_neg/$ syntax or added semicolon tactic chain.|
|9|COMMENTS|Target has no standalone proof comment to delete. All9 file standalone comments and every protected old comment/doc/paper quote survive exact inverse. No deletion justification needed.|
|10|DOCSTRING|Private auxiliary: no added docstring. Public main/module documentation byte-exact.|
|11|VISIBILITY|Private retained. Runtime/reference inventory finds only self-family and direct main consumer.|
|12|STRUCTURE|Final29 proof lines≤30 ordinary-helper target; no conjunction conclusion and no>10-line case branch. Main111/headline15 failure remains explicit parent queue.|
|13|MATHLIB|All five methods actually attempted; results and limitations below. Existing generic helper plus numerical/product/floor proof is substantive, not a trivial alias.|
|14|JUNK DEF|n/a: theorem, no new def/abbrev/data API. Shared local bound avoids a new global declaration.|
|15|EXISTS|n/a: universal scalar coefficient estimate, no single-use existential witness wrapper.|
|16|SHOW/CHANGE|Retained one term-mode `show` inside exact_mod_cast to select the natural product inequality. It is not tactic-mode change.|
|17|PUSH_NEG|n/a: none in target.|
|18|GENERALISE|Positive-degree premise removed with closed boundary-case proofs and exact old-contract recovery; all outer/inner classifications below.|
|19|INEQUALITY|All signature/hypothesis/body comparisons use≤; no≥/> name or notation. Full per-occurrence artifact below.|
|20|NORMAL FORM|Canonical degreeOf, hasseDeriv, diag, modByMonic, absolute integer/real coefficients and Nat floor. No competing custom predicate.|
|21|SYNTAX-GEN|Arbitrary universe/finite variable set and natural budget preserved; no monic/root/dimension/δ/q/nonzero restriction. Derive nonnegativity internally.|
|22|IMPORT-FANOUT|No new import or attribute. Existing all8 accepted helpers and importer files protected.|
|23|CASTS|Integer-to-real coefficients and natural product-to-real bridge are genuine. Removed redundant `(2:ℝ)` in h2 and explicit `(1:ℝ)≤2` norm_num witness from successful candidate. Retained `(2:ℝ)` for h2' power domain, inner product`:ℕ` and outer`:ℝ`, coefficient`:ℝ`, and conclusion floor`:ℤ` because they select different mathematical domains.|
|24|INSTANCE-NAME|n/a: no instance declaration. Existing unnamed implicit Fintype parameter preserved.|

## Generalisation2.6a–e

|Outer parameter|Classification|Drop/localise/strict→weak result|
|---|---|---|
|σ and universe u_1|Arbitrary type/universe|Occurs in P,r,j and finite operations; removal ill-typed, no universe restriction introduced.|
|[Fintype σ]|Typeclass|Needed by written finite sums/products and accepted helper8. Drop probe fails; this is not a proof of mathematical minimality. Finite-only reformulation would require a chosen Fintype in this written interface, with no evidenced application benefit.|
|f:Polynomialℤ|Structure value|Divisor in conclusion; cannot omit. Already arbitrary, no monic premise.|
|P:MvPolynomialσℤ|Structure value|Target dividend and degree/coefficient bounds; cannot omit. Zero allowed.|
|r:σ→ℕ|Structure value|Coordinate bound and sum/product; cannot omit. No positivity premise.|
|A:ℝ|Scalar value|Coefficient/power budget; cannot omit. Nonnegativity follows a coefficient bound where used. Abstract ordered-ring restatement changes the fixed integer/real-floor API and has no evidenced caller benefit.|
|B:ℝ|Scalar value|Coefficient/final budget; cannot omit. Derive B≥0 from hc0, no added premise.|
|β:ℝ|Scalar value|Three growth caps/final budget; cannot omit. β≥1 follows h2.|
|s:ℕ|Budget value|Already independent weak degree cap; replacing it by exact sum specialises rather than weakens.|
|hA|Universal proposition|Original-proof drop probe fails. A support/degree-local formulation needs outside-support zero bounds and handling negative A; no simple pointwise substitute proved beneficial for all dividend coefficients. Retained, no minimality claim.|
|hn:1≤natDegree f|Weak proposition|REMOVED. Monic degree-zero divisor=1 gives0 remainder; nonmonic remainder identity reduces to generic bound at zero; positive degree bounds the exponent using hs. No conclusion weakening.|
|hd|Universal proposition|Original-proof drop probe fails. Bounding only derivative j or one variable cannot directly bound every merged diagonal term; support-local rephrasing changes the interface with no established benefit. Retained.|
|hc|Universal proposition|Original-proof drop probe fails. Restricting to nonzero support loses the automatic B≥0 witness for zero P unless additional boundary work/premise is supplied; no established simpler equivalent interface. Retained.|
|hs|Weak sum cap|Original-proof drop probe fails. Exact equality/strict bound would strengthen hypotheses; current≤ is already weak.|
|h2|Weak power cap|Original-proof drop probe fails. Controls β≥1 and Hasse/cardinality factors, including the constant case; no further weakening established.|
|hpow|Weak power cap|Original-proof drop probe fails. Exact-remainder-exponent budget alone does not supply constant nonmonic case in the same simple interface; no beneficial restatement established.|
|j:σ→₀ℕ|Structure value|Arbitrary derivative in conclusion; no support-box restriction introduced. Cannot omit.|
|i:ℕ|Structure value|Arbitrary coefficient in conclusion; cannot omit. No i<degree restriction introduced.|

Inner binders explicitly audited: hA.i:ℕ, hd.k:σ, hc.d:σ→₀ℕ, sum/product.k:σ and product lambda k all retain their natural domains and have no hidden strict/typeclass premise. New local bound parameters g:Polynomialℤ and C:ℝ vary between f/A and0/0; local hC is the generic universal coefficient hypothesis and he the exact exponent cap needed by accepted helper8. Both are substantive inputs; weakening them without changing the estimate was not established. Local coefficient i in hC and sum k are universal indices. New case hypotheses hn:natDegree f=0 and hf:Monic f are exhaustive case splits, not outer restrictions; their negations discharge the other cases. No local instance assumption or existential witness is hidden.

2.6b: actual independent first-ungolfed original, selected-current and old-contract recovery were compiled with full opaque VALUE checks. Exact helper TYPE comparison preserves universes, written binder names/order and BinderInfo, except explicitly removed hn. Only BOTH compiler-generated binder macro-scopes may compare after erasing their scopes; raw names remain saved. Owner constructor audit visits891 nodes in hn's body, finds exactly one outer/default hn binder and ZERO binder-depth-adjusted occurrences. Thus instantiate1(True.intro) inserts no proof and only adjusts de Bruijn indices. No ill-typed dependent substitution is accepted.

2.6c/e: standing human authorization covers this evidenced beneficial weakening and necessary one-argument caller repair. The proof needs three more lines than the original26 but stays≤30, and covers genuinely more divisors. The explicit multiplication replaces measured expensive gcongr. No further big API or import/domain change is recommended. 2.6d literature: n/a for this private helper; the primary clean.tex main-lemma section was read for mathematical purpose. No public literature-generalisation certification claimed.

## Five-method Mathlib search and proof attempts

|Method|Actual result and disposition|
|---|---|
|leanfinder|Combined diagonal/Hasse/remainder coefficient query returned unrelated Chevalley/root-bound candidates; none replaces this numerical floor stage.|
|Loogle|modByMonic coefficient query found sum_modByMonic_coeff and coeff_modByMonic_mem_pow_natDegree_mul. Ideal-membership information is not this numerical bound.|
|LeanSearch|Natural-language floor/remainder coefficient query returned root/Chebyshev/division/ideal estimates; no drop-in exact result. Bounded actual result retained, no indefinite retry.|
|lean_local_search|Actual division API hits; index reported error/warming, so empty/missing entries are not absence evidence. Positive hits checked against source/compiled proof.|
|rg source/name|Historical full stdout/stderr were saved then; only selected critical recovery artifacts survive reboot. Fresh generic Mathlib source universe is included in the final closure. Located constant-monic=one, nonmonic remainder identity, floor bridge and natural-power APIs. Common-equivalents/reuse check selected existing helper8 and canonical floor/division APIs.|

Whole rfl/grind/simp_all/aesop attempts fail. Mixed exact?/apply? searches were contaminated by a failed earlier theorem carrying sorryAx and were rejected. Separate independent exact? and apply? whole runs fail closed-pair checks; apply? leaves sorryAx. These are not accepted proofs. Local lia/positivity/gcongr/linear_combination/floor simpa experiments were tried; mixed-fixture partial success receives no standalone gate credit. Selected independent proofs, not search suggestions, establish correctness. CandidateV1 failed an underconstrained product intermediate (β² versus β³B); corrected explicit intermediate succeeds. Historical failures remain explicitly recorded; their available saved raw streams are immutable. Unselected old raw files lost at reboot are not claimed present.

## All42 golfing rules

|Rule|Disposition|
|---|---|
|1.1 by exact|No wrapper in final target; simple transitive bounds are direct terms.|
|1.2 by rfl|n/a: no such wrapper.|
|1.3 rw+exact→rwa|Old terminal Nat-abs rewrite/identity removed in favour of the canonical floor simpa; no remaining consecutive rw+exact candidate.|
|1.4 simp+exact→simpa|Applied to floor bridge and constant-divisor cases; whole closed proofs compiled.|
|1.5 trailing rfl|n/a: no trailing rfl after simp.|
|1.6 anonymous constructor|n/a: no conjunction constructor proof.|
|1.7 apply+exact|n/a: no such two-tactic pattern remains.|
|1.8 by_contra!|n/a: final proof uses exhaustive by_cases, no by_contra/push_neg.|
|1.9 eta-reduce|Product lambda k needs its bound proof/index; no removable fun x↦f x wrapper.|
|1.10 single-use have|Removed hA0,hNle,e1,e2,hcNatAbs staging; retained nontrivial hNR and reused local bound for clarity/reuse. No lexical-use minimality claim.|
|1.11 refine+fun|n/a: no apply/introduction sequence.|
|1.12 redundant show|Only necessary term-mode natural-product show retained inside exact_mod_cast.|
|1.13 obtain pair|n/a: no have immediately destructured by projections.|
|1.14 merge rw|n/a: one product identity rewrite, no consecutive rewrites.|
|1.15 terminal simp unsqueeze|No terminal simp only in final helper; bare terminal simp/simpa actually tried and retained.|
|1.16 squeeze nonterminal simp|n/a: all new simp invocations terminate their local goal; no nonterminal bare simplifier.|
|1.17 dot notation|Applied to .trans and coefficient hypotheses where natural; explicit multiplication arguments expose nonnegativity.|
|1.18 <| parentheses|Nested mathematical theorem applications retained; replacing delimiters here does not reduce a meaningful proof block. Exact calc RHS parentheses align source with printer.|
|1.19 push Not|n/a: no push_neg.|
|1.20 existential inlining|n/a: no existential helper.|
|2.1 whole grind|Tried; fails, no accepted partial proof.|
|2.2 delete before grind|n/a: no grind in selected proof; whole grind already fails.|
|2.3 simpa consolidation|Applied to floor and division boundary cases.|
|2.4 fun_prop|n/a: no continuity/measurability/differentiability goal.|
|2.5 positivity|Actual successful local/candidate tests; final explicit multiplication uses terminal positivity to certify nonnegative factors.|
|2.6 gcongr|Actually tried and initially selected; actual156.049/209.292ms nested cost diagnosed; replaced by measured explicit multiplication.|
|2.7 lia/omega|lia closes the positive-degree natural exponent inequality; no final omega.|
|2.8 aesop|Whole attempt fails; not retained.|
|2.9 norm_num/norm_cast|norm_num supplies power-base facts. exact_mod_cast keeps real/Nat bridge; failed Nat-abs norm_cast probe retained. Removed two redundant proof ascriptions after actual compilation.|
|2.10 decide/+kernel|n/a: variable real/polynomial inequality is not a closed decidable computation; no native_decide.|
|2.11 field_simp;ring|No field division denominator to clear; ring closes only scalar polynomial identity Bβ³.|
|2.12 linear_combination|Local scalar identity tried successfully in mixed fixture; final ring is shorter/direct and independently verified.|
|2.13 wlog|n/a: no symmetric pair of variable cases; monic/nonmonic and degree cases are substantively distinct.|
|2.14 collapse calc|Three-step generic bound→three caps→Bβ³ retained to expose types and avoid underconstrained intermediate that actually failed.|
|2.15 <;>|n/a: no repeated identical closing tactic across independent goals.|
|3.1 erw→rw|n/a: no erw.|
|3.2 fun_prop replacement|n/a: no continuity/measurability tactic.|
|3.3 omega→lia|Final arithmetic uses lia directly, verified; no omega left in helper.|
|3.4 rcases with rfl|n/a: no such pattern.|
|3.5 automation registration|n/a: private purpose-specific numerical estimate, no justified global simp/automation attribute.|
|3.6 simp_all|Whole simp_all tried and failed; no final simp_all only.|
|3.7 maxHeartbeats|No limit option to remove in target; defaults verified, no raise.|

## Reflection and simplify adaptation

The estimate has three growth factors: remainder exponent, monomial count and Hasse factor. β bounds each; Bβ³ therefore bounds every real coefficient before the integer-floor bridge. The constant cases explain why positive degree was unnecessary. Shared local bound avoids duplicate composition or a new global helper. Existing APIs and coercions express each mathematical stage directly. An actual independent owner second reading of the entire29-line candidate—not merely parsing semantic receipts—found no new implementation recommendation: `O/original27-helper9-owner-v5-holistic-reflection-v1.json`, SHAf0cafa20a9af2ed1448314cf9161409b6de4cb4a0134a447bc55b23b87c984ce. This is helper reflection only; a new independent whole-file simplify review remains a later file gate.

## Historical failures and qualifications

Preserved: initial runner argument parsing failure before any child; before-pair serializer/parser limitation for an unused generated typeCode mdata (full raw TYPE/VALUE remained actual); source-family fixtureV1 late import and V2 invalid local moduleIdx/Options.setNat; corrected V3 whole actual metadata; all unsuccessful automation/drop/candidate attempts; mixed exact/apply contamination; independent exact/apply rejection; after-generator early parsing and target-repr-key mistakes; strict retained parser caught approved main generated-name consequence; after-profile V1 wrong copied `<750` label corrected only in V2; V4 appended CoreM harness failure corrected in fresh fixtureV2; V4 strict printer-parenthesis binding rejection and dependent validator failure, followed by independently approved exact uniquely pinned one-pair allowance. Available original strict failures and selected full raw streams remain immutable; reboot availability is qualified below. No failed whole run receives partial acceptance.

The original administrative exception remains explicit: owner accidentally overwrote the old P8/R2 partial END receipt771B/SHA9533ba7212592c8f39d3f8aaa0093dec4c5b04218760a33ac33dbb5c373cd167 (see authoritative erratum for exact digest); current final715B/SHAed9f4ec26d76527ceea83aab9e7e620040efe064ee4e7bdbf1932175228de271 has a unique retained receipt. Exact lost bytes/internal timestamp/old delivery transport remain UNKNOWN and are never reconstructed. Authoritative erratum SHA9eee5f67923f027ba21dbfe4442c77f15aacd5dd4ff70c32253b282796091c2c records old digest9533ba7212592c8f39d3f8aaa0093dec4c5b04218760a33ac33dbb5c373cd167; the historical authoritative erratum carries its exact original fields and the fresh closure includes the available durable copy. Only46631/46632 unaffected old P8 rows were corroborated; no complete old P8 rehash claim. All48090 actual CURRENT R3 rows were independently rehashed at this worker's entry. No source/proof/timing/native/environment gate is waived. Older unknown environment PGIDs, failed-metadata terminal observation and original baseline-native return chronology remain UNKNOWN.

Native V1 pin files saved actual pre/post read_bytes source payloads and SHA but lacked a separate byte-count field; `native-source17-retained-byte-payloads.json` derives sizes from those exact retained payloads at its actual later time, without backdating. Later native-pins-v2 records SHA+bytes prospectively. No native output text/structured mismatch, partial result or missing dependency is silently accepted.


## Actual production validation and restart provenance

V5 production FULL project build exited0/drained176.573s, then the separate `lake build Roth.LeanEval` exited0/drained48.833s. Their actual commands, source17, terminal records and raw logs are restored at `Q/restored/production-v5-{full,eval}.{json,log}`; raw hashes are `83e6fe578bf4130c0212da49a4f9ea58525fcbf417064748c995c483ccb7a5a1` and `6d9a26a2b14781be5f022a005dbc3cfde1e9005685293bbf17c3904a5bbc1dac`. Owner independently reviewed exact immutable source734, chronology and environments in `O/original27-helper9-owner-v5-production-build-review-v1.json`. These are actual completed pre-reboot gates, not newly rerun builds or replaced by native diagnostics.

The user explicitly stopped for reboot after the source-family run. No helper9 dedup mutation occurred. Owner storage-event recovery established every recorded call returned: failed ENOSPC native preparation returned exit1; the first ML native attempt was aborted before execution by approval-infrastructure initialization failure; this was not an unsafe-action rejection; its batch stopped and Main/Eval were not called. The post-family parser had not run. The suspected Box snapshot was actually intact6100B/SHAa5d0da3d2d4ecfcb705d0c446294e393fcff048576e0bd23f67b70c06dadc827. These failed events receive no native credit. Owner receipts `original27-helper9-storage-actual-tool-events-v1.json` and `original27-helper9-storage-source-integrity-v1.json` preserve the distinction. New orchestration requires every pre/save/post preparation exec to exit0 before proceeding; tool-return success alone is insufficient.

After explicit user resume, old temporary roots were gone. The durable `.mathlib-quality/restart/mainlemma-2026-10-22` bundle has692 original-path records/645 content blobs; its manifest SHA is `f42a4edf5444adeafbedd187d8da3ab3a467e167dacbabc282520fa24214e2d8`. Owner/root verified the bundle; this worker independently restored exactly247 helper9 records/519359797 decoded bytes to `Q=/private/tmp/roth-mainlemma-helper9-reboot1/restored` using byte-verified immutable content blobs and a complete relocation map. Owner independently restored200 owner records at O. No absent original path is pretended restored, no owner rows were overwritten, and no old absolute script was blindly executed. The saved subset deliberately excludes multigigabyte old cache/catalogs and secret parent environments. Therefore the historical current48090-row entry rehash remains a historical observed gate; it is **not** a new complete old-manifest rehash after reboot. Unavailable old source/cache/environment/PGID provenance stays unavailable; no fabricated recovery or blanket binary exception is used.

Fresh current observations use source17/cache104/root8/all14 actual setup fields/package12202/core12592/four binaries, reusing immutable saved content only after actual full-byte/hash/length verification. Availability is a superset, not an exact loaded runtime closure. Fresh parent SHA`029e5b5d48db43bdca821871dfd0aef4c34a34e8693c02d5dc3e12c60abd6286` and raw Lake environment SHA`1684855f56249db71eefe30cba68e3d552be815652bab0909dd1d4c8d1a51dbc` are new, with no asserted equality to lost historical parent67a/raw5859. Frozen parent secret values are private scratch evidence, not printed in this report.

Fresh inventory460project/5Eval/64ML and all64 full TYPE+opaqueVALUE/std3/default200000/20000/512/closed/inferred guards pass. The entire fresh V5 imported raw metadata is byte-exact durable V5 raw58b03c0f. Historical owner V5 review established all63 other raw pairs exact V3; the fresh raw equality transports that relationship without falsely rehashing missing V3 raw. Fresh local original6/current7 actual TYPE+opaqueVALUE families pass, including generated source-absence checks. Local-source moduleIdx-none is explicitly distinguished from imported Roth.MainLemma origin. `Q/semantic-preparation-acceptance-v1.json` binds these facts and full raw hashes.

Literal OLD and CURRENT direct `main_lemma` command proof payloads are independently preserved in the canonical command files and strictly matched by fresh complete profile payloads; both local full TYPE+opaqueVALUE closures pass. The exact inverse restores the sole `hdeg` argument and genuine entry helper, recovering all733 original bytes. Public main TYPE/doc remains exact; Main689 remains exact. This is actual caller proof/TYPE recovery for the necessary API repair, not generic foreign-metadata prose. Original→selected generated `Roth.main_lemma._proof_1_3` has the approved one-character hygienic counter5683→5682 consequence in TYPE/typeCode(forallE) and VALUE(lam); every other field/byte is exact. Raw pairs are retained and unequal. V3→V5 all63 other pairs, including all main generated values, are entirely exact. Owner receipts `original27-helper9-owner-main-generated-hygiene-consequence-v1.json`, `original27-helper9-owner-after-retained-review-v1.json`, `original27-helper9-owner-v5-retained-review-v1.json` provide the precise separate comparisons.

Fresh full unfiltered file_path-only MainLemma/Main/LeanEval native calls pass:0 errors, no failed dependencies, complete/nonpartial/nontimeout, warnings1/4/0 inherited. Actual source17 SHA+bytes chronology is pre→request→immediate-return→complete rawtext+structured save→post, all17 exact. Every nine preparation/save/post exec returned0 with no pending session. `Q/native-acceptance-v1.json`, `native-orchestration-exec-results-v1.json`, and owner `original27-helper9-owner-reboot1-final-native-review-v1.json` bind actual response hashes/lengths and chronology. Fresh native references identify only the declaration562 and directmain call680; no extra importer or public API change.

## Fresh matched performance, all samples

After the explicit owner ACK saved at `Q/reboot-four-owner-ACK-v1.txt`, four captures ran serially original733-shadow A+B then productionV5 A+B, with pair-postfreeze checks. Owner and worker suspended all other host work/parsing through ALL4+postfreeze. All4 exited0/drained, groups absent, with external420s timeout only; no Lean limit raise. Driver9183 ended before any raw parsing. Before canonical f6be733 is a shadow only: live source17 and cache/runtime stage remained V5fd03/734 throughout. Exact same new parent/raw environment/options/runtime/setup/cache stage makes these four comparable to each other. Historical timings are not substituted or numerically matched to this environment.

|Scope|A helper ms|B helper ms|A main ms|B main ms|A combined ms|B combined ms|
|---|---:|---:|---:|---:|---:|---:|
|Original733 shadow|276.436|258.824|1953.407 FAIL|1857.366 FAIL|2229.843 FAIL|2116.190 FAIL|
|ProductionV5|467.133 PASS|436.020 PASS|1941.839 FAIL|1818.621 FAIL|2408.972 FAIL|2254.641 FAIL|

Both production helper samples are below750ms and1000ms. The stronger no-hn helper costs more than the original restricted helper; this tradeoff is retained, not discounted. Main and combined are VALIDFAIL over1000 and remain original27's repair queue. No unchanged third sample, contamination/noise excuse, nested-time subtraction or main/combined certification occurs.

Strict complete canonical payload equality (whitespace/standalone comments only), actual disjoint column0 command/asyncproof/kernel/compiler/linter roots, excluded Meta, fresh actual6/7 kernel/compiler family binding, all seven ready/Apre/Bpre/post full tuples17/104/8/14/12202/12592/4 and actual prospective chronology pass in `Q/four-profile-acceptance-v1.json`. V5 uses **no** historical printer-parenthesis allowance. Actual four raw hashes are34c6273b795181f6fee829326c1a04ccc51ba4b4c0c1b9daaaf8200af3dcb832,8c87dc2023d95af832543bdd2961d0544d8bb35fe598b072a55e35cb88144f50,81ee471c581a0257b609ec891ea83d2f2c4bcc3c9bfb993121ed28b30de81eb5,93989a6f05997350dac8f28ebc91358b0616250c61a009343a79e56276c0fe50. Owner independent four-raw reanchor V2 passes; V1 guessed a wrong fixture basename and failed before timing, preserved without Lean rerun or matcher broadening.

Anchored full-payload diagnosis matches all48 top-level main tactic regions: all unchanged whole region payloads exact modulo whitespace, and hC differs only authorized hdeg removal. Actual helpercall3.801/5.416→3.915/3.794ms; hC64.275/79.901→63.762/64.893ms. Main full totals decrease in both samples but remain FAIL. Helper shared generic bound58.099/58.175ms; constant/positive-case hreal246.108/225.113ms, versus original hreal81.111/76.440ms. New floorbridge43.513/41.440ms versus original final15.073/17.000ms plus NatAbs17.624/18.524ms. These nested regions diagnose the additional boundary-case work; they are not additive budget roots or causal/noise evidence. No avoidable gcongr remains; the measured explicit multiplication and substantive stronger contract are retained. Full anchors/trace lines/payloads are in `Q/profile-region-diagnosis-v1.json`.

Historical complete samples remain qualified: own original helper278.221/274.981, main1975.483/1840.926; V3 helper589.252/781.291, main1933.148/2692.069; pilotV4 helper473.682/449.237, main1940.480/1889.445. V3 corrected parser preserves the erroneous V1 `<750` label before correcting B. V4 scratch pilot is not V5 production credit. Its exact one-pair printer allowance was approved only for its two complete payloads: normalized1457→1459, '(' before canonical870 and ')' at965 around the unique complete mul_le_mul RHS. Receipt SHAabe442dbb4ed187158dc3be3c4b3fa288597cdd964316a7406c091d8475cae17; original strict rejection stays recorded. No general AST/name/parenthesis normalization follows.

## Full signature packing and inequality artifacts

Lean actual `format.width 100` reference is printed by the fresh current source-family fixture under that option (`WIDTH100_TYPE=` in `reboot-family-after-v1.log`). The handwritten signature packs whole binders while retaining declared grouping; the table measures actual Unicode codepoints, not byte counts.

|Line|Width|Next complete unit|Next width|Current+1+next|Action|
|---|---:|---|---:|---:|---|
|562|87|`{f : Polynomial ℤ}`|18|106|ok|
|563|77|`(hA : ∀ i, |(f.coeff i : ℝ)| ≤ A)`|33|111|ok|
|564|68|`(hc : ∀ d, |(P.coeff d : ℝ)| ≤ B)`|33|102|ok|
|565|99|`(j : σ →₀ ℕ)`|12|112|ok|
|566|92|`(end)`|—|—|ok|

Every inequality occurrence in the whole declaration, including inner hypotheses/body, is listed. All19 use≤; zero≥/> comparisons and no name requiring orientation rename.

|Line|Column|Token|Action|
|---|---:|---|---|
|564|34|≤|ok|
|564|63|≤|ok|
|565|34|≤|ok|
|565|54|≤|ok|
|565|71|≤|ok|
|565|96|≤|ok|
|566|67|≤|ok|
|567|16|≤|ok|
|568|16|≤|ok|
|569|16|≤|ok|
|570|35|≤|ok|
|572|41|≤|ok|
|574|47|≤|ok|
|577|70|≤|ok|
|578|54|≤|ok|
|579|52|≤|ok|
|580|12|≤|ok|
|581|9|≤|ok|
|585|61|≤|ok|

## New external identifiers

Historical local search was attempted but reported warming/error. Fresh exact source declaration search and actual full compiled constructor VALUE/inference checks verify introduced names; no negative index result is treated as absence.

|Identifier|Verification|OK|
|---|---|---|
|`one_le_pow₀`|Fresh exact source declaration hit + actual independent compiled VALUE|yes|
|`zero_le_one`|Fresh exact source declaration hit + actual independent compiled VALUE|yes|
|`le_trans`|Fresh exact source declaration hit + actual independent compiled VALUE|yes|
|`mul_le_mul`|Fresh exact source declaration hit + actual independent compiled VALUE|yes|
|`mul_le_mul_of_nonneg_right`|Fresh exact source declaration hit + actual independent compiled VALUE|yes|
|`eq_one_of_monic_natDegree_zero`|Fresh exact source declaration hit + actual independent compiled VALUE|yes|
|`modByMonic_eq_of_not_monic`|Fresh exact source declaration hit + actual independent compiled VALUE|yes|
|`le_add_of_nonneg_right`|Actual full constructor VALUE constant + valueDeps + independently inferred compiled proof; declaration-regex no-hit preserved|yes|
|`natCast_floor_eq_floor`|Fresh exact source declaration hit + actual independent compiled VALUE|yes|
|`le_floor`|Fresh exact source declaration hit + actual independent compiled VALUE|yes|
|`cast_abs`|Fresh exact source declaration hit + actual independent compiled VALUE|yes|


## Seven scoped diff gates

|Gate|Result|Evidence|
|---|---|---|
|lake_build_file|PASS|Actual FULL `lake build`0 includes Roth.MainLemma; separate `lake build Roth.LeanEval`0, source734 unchanged; commands/raw/terminal cited above.|
|definition_protected|PASS|No def/abbrev/import/attribute change; exact inverse recovers entire original source.|
|theorem_statement_protected|PASS with authorized weakening|Audit18 removes only unused hn, exact original/current dependent TYPE and old-contract recovery; main publicTYPE exact, one necessary caller argument removed.|
|structure_gate|PASS helper only|29≤30 proof lines, no conjunction, no>10-line case branch; main111/headline15 remains FAIL outside scoped helper acceptance.|
|naming_gate|PASS|Private descriptive `_aux`, no forbidden pattern; no rename or sidecar change.|
|line_packing_gate|PASS|All5 actual measured signature rows above are ok; actual Lean width100 reference saved.|
|inequality_orientation_gate|PASS|All19 occurrences listed; no≥/>; name uses le.|

Scoped overall: helper gates pass; final local closure/release and owner acceptance are separate receipts. File/global performance and structure are not certified.

## Eleven-step verification checklist

|Step|Result|
|---|---|
|1 references|✓ Full required installed skills/commands/references read; reboot recovery rereads recorded.|
|2 audit|✓ All24 items above, including casts/normalforms/reuse/comments.|
|2.5 search|✓ All5 methods attempted; failures/index limitations explicit.|
|2.6 generalisation|✓ Every original18 outer parameter plus universe and inner binders classified; a–e/unused-hn constructor audit/nonself/old recovery provided.|
|2.7 packing|✓ All5 codepoint/next-whole-unit rows and actual width100 reference.|
|2.8 inequalities|✓ Every19 occurrence shown, all≤.|
|3 golfing|✓ Every42 rule disposition and actual relevant attempts/failures above.|
|4 reflection|✓ Whole-proof attempts and independent owner whole-helper mathematical rereading, no unperformed literal Skill claim.|
|5a diagnostics|✓ Fresh full unfiltered ML/Main/Eval native0 errors, inherited1/4/0 warnings; actual successful FULL→separateEval builds.|
|5b diff gates|✓ All7 scoped gates above; exact inverse/retained family/caller evidence.|
|6a renames|✓ None warranted or queued by this helper; no central sidecar write.|

Before26 proof+7 signature; after29 proof+5 signature: proof grows3 lines to cover additional constant-divisor cases, signature shrinks2. Audit issues fixed: assumption generality, signature packing, redundant cast staging, composed terminal floor conversion and measured multiplication. Renames-queued:none. Comments-preserved: all9 file standalone/all7 original literal comments including5main signposts exact; none in target. Refactoring needed within this helper:none. Main111→headline15 and main/combined<1000 remain explicit SAME-original27 work; global exists_delta_bound12408.373/11188.775 and pigeonhole_count1018.335/1000.235 remain outstanding historical failures. Later genuinely independent whole-file simplify/cumulative22-public/all-retained/import-doc/comment/global/build/native/publication gates remain owner/file work; this independent whole-helper reflection is not their substitute.

## Final evidence and lease boundary

`Q/final-artifact-manifest-v1.json`, `Q/final-second-rehash-v1.json`, `Q/final-process-drain-v1.json` and `Q/final-local-seal-v1.json` are the authoritative final closure/release artifacts once actually produced. The manifest must include this report, every current own file except those exact self-exclusions, available owner evidence, the entire durable692-record/645-blob bundle with exact codec provenance, current source17 and full observed binary/source/reference universes. It must explicitly distinguish unavailable historical references from newly hashed bytes. Two independent complete streaming passes and a later fresh process/source freeze must actually succeed before local acceptance; this prose asserts no future outcome. Every current binary exception must bind an actual observed path/SHA/byte tuple or exact durable encoded blob provenance, never a blanket suffix exemption. Old parent secrets, unselected cache/raw history and unknown historical launch groups remain qualified. Reboot PID reuse forbids claiming historical process absence from current numeric PID inspection.

Final seal must explicitly end helper_source/narrow_main_application/new_report/new_artifacts/compiler/native/profile leases, with0 active calls/children and fresh manifest-bound current launch-group/task/printenv drain. No mutation after seal until explicit owner resume. Owner independent review is required before SAME original27 resumes. Counts remain242/264,ML26/27,10/14; no original27/file/project/publication completion credit.
