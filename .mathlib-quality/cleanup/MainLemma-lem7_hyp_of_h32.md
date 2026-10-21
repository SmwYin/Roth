# FULL Mode B cleanup — `Roth.lem7_hyp_of_h32`

Scope is original24, its docstring and the sole necessary call in `Roth.main_lemma`. The owner controls publication and shared queues. This is not a claim that MainLemma or original27 is complete.

## References and baseline

All required skills, commands, references, 854/112/46-line instruction files, original24 dispatch, genuine original704, entire entry696 and paper §6 were read. `reference-inputs24.json` records full saved bytes and hashes of 24 reference inputs. Actual source/config baseline has 17 pins; project compiled cache has 104 companions. Before API edits, actual direct `lean --deps`, affected/full builds, separate Eval build, complete native ML/Main/Eval, imported actual TYPE+opaque VALUE direct-consumer inventory and exact scoped profile repeat all completed. The before inventory's 1.3 GB raw proof AST is retained. Subsequent inventories keep the actual complete-term validation while printing full TYPE/universes, VALUE hash and used-constant inventory, as explicitly authorized by the owner; DATA VALUE AST checks are unchanged.

Fresh before target profiles: 719.805 and 720.953 ms, 4 disjoint roots each. Complete sole caller: 4964.514 and 5094.045 ms, 9 roots each. These are entire-command scopes with actual complete printed payloads bound to canonical source. All Meta roots, nested events, inclusive wrappers and adjacent/end commands are excluded. No global-versus-local comparison, forced root count or invented sibling cap is used. The foreign caller already exceeds 1000 ms and remains an explicit original27/global obligation.

## Full 24-item audit

| # | Item | Resolution |
|---|---|---|
|1|LINT|Full unfiltered native baseline retained; target has no error. Existing header warnings and Main unused-variable warnings are reported without filtering. Final native gate recorded below.|
|2|HAVE SCAN|Removed the two log certificates, Nat case split, product conversion, h2m/hL and h1/h2/h3 intermediates from the public theorem. One meaningful δ≠0 certificate remains. Whole-property old-contract proof still explicitly derives both nonnegative log contributions.|
|3|SET_OPTION|No production option changes; default 200000/20000/512 asserted in compiled guards.|
|4|SIMP SQUEEZE|Original nonterminal `simp [h] at hδm` disappears. The sole remaining public `simpa` closes its goal and remains unsqueezed.|
|5|NAMING|Current name encodes paper numbering. Concrete content name `mul_two_mul_add_one_div_lt_of_le_sq_mul` recommended and accepted by owner for the single project-end queue. No early rename.|
|6|LINE PACKING|Every selected signature line and next indivisible binder is measured in the generated source audit; no aesthetic-only width claim.|
|7|BY PLACEMENT|`:= by` remains on the conclusion line.|
|8|FORMAT|Two-space proof indentation, no proof blank lines, no `$`, lambda boilerplate or haveI/letI.|
|9|COMMENTS|The exact two-line Source quotation, equation references and punctuation are preserved. No inline target comments existed. All seven caller signposts stay byte exact.|
|10|DOCSTRING|Revised public mathematical summary describes the arithmetic statement and its `L = log q₁` application; no proof-strategy narration.|
|11|VISIBILITY|Public, used by main_lemma; no attributes or visibility changes.|
|12|STRUCTURE|Ordinary theorem, not a module headline; eight proof lines, no branches or conjunction. No new helper or duplicated public wrapper.|
|13|MATHLIB|Five actual search methods plus guarded automation and source fallback are documented below; partial hits are reused for multiplication, square positivity and denominator algebra. No keyword-search absence claim.|
|14|JUNK DEF|n/a: theorem, no definition introduced.|
|15|EXISTS LEMMA|n/a: result is a strict inequality, not an existential proposition.|
|16|SHOW/CHANGE|No show/change in selected production theorem. Scratch counterexample's explicit change fixes a Nat-to-Real cast.|
|17|PUSH_NEG|No push_neg/negation normalization needed.|
|18|GENERALISE|Every old/new outer parameter and all field-class candidates are audited in 2.6a–e. No mathematical inner binders exist in this signature. Actual elaborated every-inner binders are checked by the independent full TYPE AST/BI/name/order gate.|
|19|INEQUALITY|Zero `≥` or `>` in Lean target code/signature. Paper quotation is preserved literally and excluded from code-orientation rewriting.|
|20|NORMAL FORM|Same strict division conclusion and same `2*m+1` expression. Scalar L removes unnecessary log/domain syntax. No independent arbitrary-P abstraction or conclusion weakening.|
|21|SYNTAX GENERALITY|ℝ, Nat m and Nat q₁ specificity removed from arithmetic core; universe-polymorphic ordered semifields include ordered fields and NNReal. Parent classes tested mechanically, with failed proof attempts retained rather than called impossibility proofs.|
|22|IMPORT FANOUT|No production import added; NNReal and exponential-bound imports occur only in scratch verification fixtures.|
|23|CASTS|No casts in generalized target. Sole caller uses only Nat.cast_add/Nat.cast_one at the actual Θ_lt boundary, explicit K=ℝ, and direct certificates from existing hmR/h32prime. Broad exact_mod_cast and positivity overhead were diagnosed and removed; no unrelated cast churn.|
|24|INSTANCE NAME|n/a: no instance declaration. Anonymous class binders retain standard syntax.|

## Mathlib search status (actual methods A–E)

| Method | Actual query/result | Evidence |
|---|---|---|
|A — Lean finder|Full scalar implication; five returned suggestions are partial square/real inequality facts, not the complete theorem.|search24-finder request/response and native pin/time captures|
|B — Loogle|`?a * ?b < 1`, eight hits: inverse and ordered multiplication APIs.|search24-loogle captures|
|C — LeanSearch|Product below one plus quadratic bound to division; partial division/multiplication results.|search24-leansearch captures|
|D — local source rg|Untruncated scoped and global full-name/pattern searches across Mathlib/Roth. Square positivity and positive-multiplier cancellation used directly.|search24-source and search24-global-names actual commands/raw/metadata|
|E — local indexed tool|`mul_lt_one`, limit30, project root: two items but index:error. This does not establish absence; D is the honest source fallback.|search24-local captures|

Standalone `automation24-negative-v2` actually checks that whole-goal grind/aesop/exact?/gcongr/positivity fail, then compiles the explicit proof and validates its actual closed TYPE+opaque VALUE/inferred TYPE/std3. First probe's apply? reported success but the whole file and actual VALUE guard failed; all output is retained and no suggested/admitted term is accepted. Available search methods support a useful local arithmetic specialization; no claim of mathematical absence or a most-general-known theorem is made.

## Generalisation status — 2.6a

Old outer binders (all nine):

| Binder | Class/use | Candidates assessed | Verified result |
|---|---|---|---|
|δ : ℝ|Structure value, division/square|Drop positivity; arbitrary ordered scalar; δ≤0 and δ=0|Generalized to K. δ negative passes; δ=0 contradicts retained quadratic/cutoff premises.|
|hδ0 : 0<δ|Proposition, old positive-divisor conversion|Drop, combine with scalar m and multiplication premise|Dropped from selected API; exact old contract retains it to derive old product hypothesis.|
|m : ℕ|Structure value, coefficient/count|Real/universe scalar; m=0; negative m down to −1/2|Generalized to K with cutoff `0<2*m+1`; examples m=0 and −1/4 pass. Cutoff equality m=−1/2 fails desired strict result.|
|hδm : δ<1/m|Proposition, small product|Product normal form; strict→weak; drop|`δ*m<1` selected. Under old hypotheses converted using actual m>0. Weak/drop fail with full remaining new premises. Old stricter h32 can support different tradeoffs; strictness is claimed necessary for the selected combined nonstrict h32 form only.|
|q₁ : ℕ|Structure value, only log q₁|Real q₁; abstract scalar L|Replaced by L : K. Exact old q₁/Nat log contract recovered. No inference that log's input must be positive.|
|A : ℝ|Structure value, extra log contribution|hA≥0 vs≥1; eliminate from arithmetic core|Eliminated in favor of h32'. The old-contract fixture explicitly derives 0≤log(1+A) from hA≥1.|
|α : ℝ|Structure value, absolute-value log contribution|Eliminate via nonnegative log; arbitrary scalar L|Eliminated from core; old-contract proof uses abs_nonneg and the actual old log term.|
|hA : 1≤A|Proposition, log sign|Weaken≥0; drop|No separate premise in scalar core. Full original-form counter with Nat q=64, δ=1/2,m=1,α=0,A=exp(−1)−1 satisfies all other old premises and fails conclusion, so original sign cannot simply be ignored.|
|h32|Proposition, dominates 2m+1|Remove extra nonnegative terms; strict→weak; drop|Selected `2*m+1≤δ²*L`; equality boundary passes. Dropping it fails with all other new hypotheses.|

New outer binders (all eleven, including the type and four classes):

| Binder | Class/use | Candidates assessed | Result |
|---|---|---|---|
|K : Type*|Type-variable|Type→Type*, concrete ℝ→abstract K|Universe-polymorphic generic proof, with actual level metadata and exact contract checks. No universe bound specialization.|
|Semifield K|Typeclass: division, commutative semiring normalization|Field, Semifield; DivisionRing/DivisionSemiring; CommRing without division|Semifield selected; NNReal actual application certifies utility beyond fields. Mechanical noncommutative/division-free proofs are rejected; not mathematical impossibility claims.|
|LinearOrder K|Typeclass, square/order reflection|PartialOrder/drop|Mechanical weaker proof fails missing order/reflection structure. No arbitrary order refactor selected.|
|IsStrictOrderedRing K|Typeclass, strict multiplier cancellation|IsOrderedRing; drop|Field+IsOrderedRing works through Field instances; Semifield+IsOrderedRing fails strict multiplication instances. Strict class retained in uniform Semifield API. Pinned Defs112–115 derives it from IsOrderedRing with Ring/NoZeroDivisors/Nontrivial, while Semifield lacks Ring; Def79 also carries ordered additive cancellation. This is an actual elaboration/structure gap, not universal impossibility.|
|ExistsAddOfLE K|Typeclass, standard square positivity API|Drop|Mechanical square-proof drop result recorded in class-drop fixture. Retained to use standard sq_pos_of_ne_zero rather than invent an order hierarchy.|
|δ : K|Structure value|δ arbitrary, δ≤0, δ=0|Arbitrary; no explicit sign/nonnull premise. Quadratic bound and cutoff imply nonzero.|
|m : K|Structure value|m=0, m<0, lower-bound weakening|Arbitrary with cutoff hm; two signs of δ tested at m=−1/4.|
|L : K|Structure value|Any scalar; L≤0|Arbitrary, with h32; nonpositive L contradicts retained premises in ordered field fixtures. Actual NNReal application also compiled.|
|hm : 0<2*m+1|Proposition, positive strict multiplier|Weak≤0/drop|Countercertificates at m=−1/2,L=0 and m=−1,L=−3 reject these changes.|
|hδm : δ*m<1|Proposition, strict contraction|Weak≤/drop|Full-premise counterexamples at (m,δ,L)=(1,1,3) and (1,2,1) reject them.|
|h32 : 2*m+1≤δ²*L|Proposition, final bound|Strict version/equality/drop|Nonstrict chosen and equality tested. Removal fails at (1,1/2,1).|

There are no inner forall/exists/let/class binders in the written target signature. No pointwise/finite-index localization applies: each proposition already concerns one scalar tuple. Changing explicit arguments to instances is inappropriate for local inequality evidence. The original nine explicit/implicit binder names/order/types are preserved in the separately compiled exact old-contract fixture; the generalized contract is compared separately rather than falsely claimed unchanged.

## 2.6b — Verification and failure history

Candidate/property v8 whole0, then final term-golf v9 whole0 (51.513 s), validate 17 actual declarations, each with closed TYPE and actual opaque VALUE, inferred TYPE agreement and only propext/Classical.choice/Quot.sound; δ≤0, δ=0, m=0, negative m, quadratic equality, all retained scalar-premise counterexamples and the exact complete original contract are included. First Field proof's redundant ring produced a no-goals error; it was not accepted. V3 Semifield+IsOrderedRing fails missing classes. V4/v5 coefficient counter cast normalization failures are retained. V6/v7 unopened scoped NNReal notation errors are retained; v8 uses the explicit NNReal type name; final v10 uses the canonical Basic.NNReal.Basic import. All launched source variants are saved by SHA, not just their hashes. Final production native diagnostics and the fresh independent old/entry/selected entire-body gate are additional gates, not replaced by these candidate checks.

## 2.6c/e — Applied generalization and authority

The public structure/argument change is larger than the command's default small-safe category. Standing user authorization explicitly requires implementation of all evidenced recommended beneficial changes; the owner expressly authorized this scalar arithmetic normalization and old-contract recovery. This session authority supersedes a redundant approval stop. Applied: scalar ordered-semifield API, cutoff m>−1/2, no δ positivity premise, nonstrict quadratic bound and necessary sole caller adaptation using its already-existing h32'. The conclusion's formula and strictness stay intact. No optional stronger companion, independent arbitrary positive P, indexing refactor or new helper is introduced. The concrete rename is queued through the owner rather than changed early.

## 2.6d — Literature search

Three separate actual queries and their top three returned hits are saved verbatim in literature24-query{1,2,3}.json and literature24-top-three.json:

1. `"Rational approximations to algebraic numbers" "log q" "Lemma 7"`: unrelated ResearchGate hits on uniform divisor distribution, Hurwitz moments and Ramanujan formulae; no mathematical support inferred.
2. `"Formalizing Roth's theorem" Takloo Bighash Yin`: MaRDI's arithmetic-progression Roth formalization, a LinkedIn result and a csauthors page; wrong subject/irrelevant, no support inferred.
3. `Roth theorem auxiliary polynomial main lemma delta logarithm denominators generalization`: AMS Rational Approximation preview, Marco Maculan's Roth book and SMF Introduction PDF; related rational-approximation background, no scalar optimality claim inferred.

The combined initial query also returned the primary Roth 1955 paper. The local paper §6 is the direct source of the retained quotation and formula. The ordered-semifield generalization is supported by the actual Lean proof and explicit tests, not attributed to those search results. Optional ChatGPT-math MCP is unavailable in the actual enabled tool inventory; no question or answer is fabricated.

## All 42 golf rules

| Rule | Resolution |
|---|---|
|1.1|No by-exact wrapper in target; caller by-simpa reconciles the actual cast-successor boundary. Explicit scalar type prevents delayed class inference.|
|1.2|No by-rfl block.|
|1.3|Old rw/rwa product conversion eliminated by product-normal-form hypothesis; no rw+exact remains.|
|1.4|Terminal simpa using closes the nonzero contradiction; multiplication and final commutation use direct terms.|
|1.5|No trailing rfl after simp.|
|1.6|No conjunction constructor in target.|
|1.7|The apply step intentionally transforms the goal by positive δ²; no following sole exact could replace the calc.|
|1.8|No by_contra/push_neg chain.|
|1.9|No lambda in target.|
|1.10|Single remaining have has a meaningful three-line proof; no term-valued trivial intermediate.|
|1.11|No apply+intro.|
|1.12|No redundant show.|
|1.13|No pair projection intermediate.|
|1.14|No consecutive rw.|
|1.15|Target terminal simpa is unsqueezed. Sole caller retains the two-cast-only exception after actual same-argument bare simpa was harmful: explicit-K-only proof74.622 vs39.236 ms; full explicit arguments88.107 vs40.138 ms. All variants passed full actual VALUE/std3 guards in bounded fixture v4; no guessed normalization exception.|
|1.16|Original nonterminal simp removed; none remains.|
|1.17|hm.trans_le, h32.trans_eq and positive-multiplier iff projection use standard notation; no artificial dot rewrite.|
|1.18|No unnecessary trailing parenthesized tactic argument.|
|1.19|No push_neg.|
|1.20|No helper or existential lemma.|
|2.1|Actual whole grind fails; negative probe guard verifies the explicit fallback proof.|
|2.2|No final grind preceded by deletable tactics.|
|2.3|Nonzero contradiction closes with simpa; two former terminal simp blocks were replaced by direct terms.|
|2.4|n/a: no continuity/differentiability/measurability goal.|
|2.5|Whole positivity actually fails; nonzero requires relational hypotheses rather than syntactic positivity.|
|2.6|Whole gcongr actually fails; explicit strict multiplication lemma is one terminal step.|
|2.7|n/a: target is abstract scalar arithmetic, no Nat/Int goal.|
|2.8|Whole aesop actually fails.|
|2.9|n/a in target: no concrete numeric computation or cast goal; norm_num used in actual rational boundaries and cast counterfixture.|
|2.10|n/a: target variables are abstract, not finite decidable computation.|
|2.11|field_simp closes the denominator identity directly. The earlier redundant ring failure is retained and removed.|
|2.12|No selected goal ends in ring/ring_nf; linear_combination not applicable to the division identity after field_simp closes it.|
|2.13|No selected symmetric case branches; sign split removed by multiplication by δ².|
|2.14|Three-step calc deliberately displays denominator identity, strict contraction and weak final bound; replacing it by nested trans terms does not reduce mathematical steps or clarify them.|
|2.15|No repeated sibling goal blocks.|
|3.1|No erw.|
|3.2|No continuity/measurability tactic.|
|3.3|No omega/lia in target; unrelated caller arithmetic remains byte exact.|
|3.4|rintro rfl substitutes δ directly; no following simp[h] rewrite.|
|3.5|No automation attribute added: specialization is not a simplifier normal form and no demonstrated repeated automation need.|
|3.6|No simp_all only chain.|
|3.7|No heartbeat or other resource-limit option added.|

## Step back / simplify / buzz

The denominator-sign argument was replaced by positive δ² scaling. This makes the mathematical dependence explicit, preserves the exact division conclusion and removes all sign branches, logarithm facts and Nat bookkeeping from the public core. No new helper cost is hidden. The same eight-line public proof applies to fields and NNReal. A manual full simplify-rule review is used because this exclusive sole leaf cannot delegate or call an unavailable built-in simplify skill; it is not labeled an independent agent review. The fresh performance captures below are actual buzz verification, not a numerical reuse of previous declarations.

Historical interruption: the c204 provisional independent replay started before the final two direct-term suggestions arrived. It was explicitly stopped to resolve those suggestions before final freeze. Sandbox stop/query failed with PermissionError; authorized SIGTERM succeeded and authorized fresh signal0 confirmed PGID36952 absent. The runner aborted in its post-wait sandbox query before emitting child exit/time; those fields are honestly null, owning tool exit1 and full raw/input history retained. No proof acceptance credit is assigned. The outer process timeout was 600 s; no Lean resource option was increased.

### Actual top-three literature results per query

| Query | Position | Actual returned title/link |
|---|---|---|
|1|1|[(PDF) Uniform distribution on divisors and Behrend sequences](https://www.researchgate.net/publication/266013276_Uniform_distribution_on_divisors_and_Behrend_sequences)|
|1|2|[(PDF) The fourth moment of the Hurwitz zeta function](https://www.researchgate.net/publication/380719679_The_fourth_moment_of_the_Hurwitz_zeta_function)|
|1|3|[(PDF) Ramanujan-type formulae and irrationality measures of some multiples of](https://www.researchgate.net/publication/230934199_Ramanujan-type_formulae_and_irrationality_measures_of_some_multiples_of)|
|2|1|[Formalising Szemerédi's Regularity Lemma and Roth's Theorem on Arithmetic Progressions in Isabelle/HOL - MaRDI portal](https://portal.mardi4nfdi.de/wiki/Formalising_Szemer%C3%A9di%27s_Regularity_Lemma_and_Roth%27s_Theorem_on_Arithmetic_Progressions_in_Isabelle/HOL)|
|2|2|[Chelsea Edmonds, PhD - The University of Western Australia \| LinkedIn](https://au.linkedin.com/in/chelsea-edmonds94)|
|2|3|[Angeliki Koutsoukou-Argyraki](https://www.csauthors.net/angeliki-koutsoukou-argyraki/)|
|3|1|[Chapter 4Rational](https://www.ams.org/bookstore/pspdf/mbk-48-prev.pdf)|
|3|2|[Marco Maculan](https://webusers.imj-prg.fr/~marco.maculan/files/papers/roth_book)|
|3|3|[INTRODUCTION](https://smf.emath.fr/system/files/2017-08/smf_mem-ns_152.pdf)|

Pinned class hierarchy evidence: Mathlib/Algebra/Order/Ring/Defs.lean112–115 derives IsStrictOrderedRing from IsOrderedRing under Ring, NoZeroDivisors and Nontrivial. Semifield alone does not supply Ring. The strict class includes ordered additive cancellation, explaining the mechanical Semifield+IsOrderedRing gap without asserting universal impossibility. The actual NNReal application establishes concrete added utility.

Property-specific input erratum: historical v4–v9 scratch test imports included ExpBounds and, in v8/v9, deprecated Data.NNReal.Basic outside the MainLemma/Main profile availability catalog. Their actual whole0/closed/std3 results are correctness evidence only; complete property-specific input coverage was not captured then. No extra-artifact hash is backdated. Final v10 uses canonical Basic.NNReal.Basic, with fresh actual parser-reported recursive --deps extra-module closure and compiled companions before/after. This supplements the production profile availability catalog, rather than calling either an exact runtime-loaded closure. NNReal failures in v6/v7 were unopened scoped notation, not a missing type or a counterexample.

Final verification repair: the first combined retained+consumer fixture whole1 at465.431045625s exhausted the unchanged200000 heartbeat budget after inventory/discovery, before any retained validation PASS. Its raw/source/metadata remain; no partial acceptance. The corrected source-specific fixture dynamically crosschecks all actual exact Lean.Name descendants against the fresh independent inventory, then runs each declaration validation as its own ordinary Lean command at actual200000/20000/512 defaults, with no internal reset or resource option. On historical4bd, all60 declarations (32written,28generated) passed. Final caller-source acceptance uses a fresh independently derived exact-name set and a new complete retained replay; no inherited count is an acceptance assumption. The separate full consumer inventory also passes and returns only Roth.main_lemma. Seven new target _simp children are included; no inherited before4-root or prior53-total assumption is used.

Final canonical-property evidence: ordinary v10 whole0 and explicit-frozen v10 whole0 have byte-identical raw output and all17 property markers. Frozen direct--deps output exactly matches the actual first recursive parser result; before/after raw Lake environment matches baseline. Fresh after hashing confirms all790 extra compiled artifacts and159 parser source headers unchanged. Parser subprocess environments were inherited and not individually snapshotted; the separately frozen replay closes final environment coverage without inventing per-parser observations.

Orchestration-only failure: queue24-semantic-v1 indexed cmd[4] after its short Python after-check command, producing an IndexError only after frozen--deps/property/after checks actually succeeded. Exact queue stderr, original script and child outcomes are retained; no overall Python queue success is claimed. The corrected retained/inventory queue completed successfully. New wrapper launch receipts are saved prospectively after the interruption lesson; they are not fabricated for older runs.

Actual profile formatting exception: strict v3 binding rejected the first after payload because pinned Lean encloses exactly the terminal calc term `mul_lt_of_lt_one_left hm hδm` in parentheses. Complete actual/canonical mismatch payloads and hashes are retained. v4 permits only this uniquely observed unchanged term at its recorded actual proof line; every other non-layout token must match. No arbitrary parentheses stripping, semantic TYPE/VALUE/proof/binder normalization, or source modification occurs. The actual full target kernel set (base plus all7simp children) and main kernel set (base plus all5proof children) are cross-matched to the freshly validated exact retained inventory.


## Narrow caller repair and actual failed samples

The initial selected4bd exact final pair passed the theorem budget (200.366/199.594 ms versus719.805/720.953), while the complete foreign main pair was5103.153/5199.000 versus4964.514/5094.045 ms. All105 same-indent event strings and9 root anchors matched. Actual changed hΘ was199.810/197.771 versus118.893/117.320; its broad exact_mod_cast was94.435/93.459 versus16.185/15.626, including two new inclusive positivity costs29.899/29.272 and20.753/20.539. These nested values are not added to root totals. The4bd pair and all comparisons/diagnostics are retained as failed-consumer evidence, not silently replaced.

A direct-certificate/cast-only d1 intermediate whole profile0/234.780860667s42358 yielded target196.194/11roots and main5197.455/9roots, actual hΘ157.809. Its remaining simpa55.098 included a cutoff33.400 with unresolved generic scalar metavariables. This valid provisional sample is retained without a final-pair acceptance claim. The final narrow repair adds explicit (K := ℝ) before the same direct certificates; target and all other production source bytes are exact.

Actual bounded fixture v4 whole0/67.634065542s42804 validates the target and9 caller variants with10 closed TYPE+actual opaque VALUE/inferred TYPE/std3 markers at unchanged200000/20000/512 defaults. It compares generic exact_mod_cast103.964ms proof, cast-only generic53.029, all-explicit cast-only40.138, same bare88.107, K-only bare74.622, selected simple K-only cast-only39.236, linarith-cutoff151.317, Nat-successor exact-cast bare83.921 and Nat-successor cast-only38.563. The last adds automation without meaningful evidence of advantage over the simpler direct-certificate variant; no optimality claim is made. These are fixture inclusive proof observations, not main root totals. Final full-source paired main costs and residual changes are reported separately.

Historical failed bounded fixtures v2/v3 had missing generated declaration separators (.letheorem/.leend); actual parser errors and the actual VALUE guard rejected them (whole1,57.981823666s42635 and63.508792041s42724). All exact code, raw streams and failures remain. The first native multi-attempt was also rejected because single-line replacement left the original following argument line. Its full parser-error response and actual arguments remain, including the separate shell-quoting failure of before-call bookkeeping and subsequent missing request failure. No per-call before timestamp was captured for that rejected native query, no zero-goals acceptance is inferred, and no timestamps/pins are fabricated. Later standalone whole0 and final full-source guards supply actual accepted evidence.

Fresh final native requests distinguish immediately observed actual tool return and saved response observations from later post-pin bookkeeping completion. Historical4bd completed_unix is explicitly post-pin bookkeeping; actual complete response file writes preceded those pin observations. No call-end timestamp is invented.

The unchanged canonical property fixture and actual recursive159-header/790-artifact graph are reused only after a fresh observation of every actual source/artifact hash and a byte-exact entire-production-target declaration comparison against4bd, then a new explicit-frozen root --deps/replay at final source pins. The original159 parser subprocess environment limitation remains historical and disclosed. Fresh v4 observations name the final current17 pins separately from the original parser capture; no old17 pins are relabeled final.

## Final source and line packing

Selected source SHA256: `cb59bb4129cbf7e353b272f05615b0cfd2193c67177b82100590c3fa84afd056`. MainLemma has 692 lines. Proof17→8, saved9; branches0; new meaningful helpers0. Thirty-two written declarations remain, and 28 actual generated descendants were discovered by exact Lean.Name ancestry (no fixed expected generated count). All five existing helper bodies and all other source/context bytes remain exact after reversing the target/doc/sole-call change.

| Signature line | Actual width | Next indivisible binder | Would-be width |
|---|---:|---|---:|
|`theorem lem7_hyp_of_h32 {K : Type*} [Semifield K] [LinearOrder K] [IsStrictOrderedRing K]`|89|`[ExistsAddOfLE K]`|107|
|`[ExistsAddOfLE K] {δ m L : K} (hm : 0 < 2 * m + 1) (hδm : δ * m < 1)`|72|`(h32 : 2 * m + 1 ≤ δ ^ 2 * L)`|102|
|`(h32 : 2 * m + 1 ≤ δ ^ 2 * L) : m * (2 * m + 1) / δ < L := by`|65|last line|n/a|

Inequality scan: target signature and proof contain 0 forbidden ≥/> occurrences. No occurrence requires flipping or a new reverse lemma; the literal paper quotation remains unchanged.

## Source-dependent verification

| Actual run | Exit | Seconds | PGID |
|---|---:|---:|---:|
|final24-affected-v3|0|98.318875|42928|
|final24-full-v3|0|42.617910|43053|
|final24-Eval-build-v3|0|42.986823|43139|
|final24-independent-v3|0|286.581900|43213|
|final24-retained-v4|0|112.555242|43397|
|final24-inventory-v4|0|131.694890|43657|
|candidate24-v10-final-properties-frozen-v3|0|65.394047|43845|
|end24-deps|0|4.554654|44576|

The independent fixture reconstructs entire genuine original, entry and selected namespace bodies and complete caller proofs, checks six nonself TYPE+actual opaque VALUE closures, standard axioms, inferred VALUE types, exact universe levels and every written/generated binder name/order/BinderInfo/type. Actual DATA VALUE AST equality and isDefEq are checked with only named DATA expansion, originating-DATA-spine β and prevalidated actual literal-pair TYPE+opaque VALUE/universe/all-binder equality. Both-generated hygiene is the only binder normalization. No proof irrelevance, NameMap or arbitrary proof unfolding. The deny set covers all actual full public/private Lean.Name roots and descendants; narrowly prevalidated immutable Entry literal sharing is the only allowed old-to-Entry exception. Original and entry callers must use their own targets, and genuine original caller its own old DATA; selected caller must use its own target and selected H5.

The final per-declaration retained fixture and separate actual direct TYPE+opaque VALUE consumer inventory validate the complete retained set and every actual direct consumer at unchanged per-command defaults. Discovery is a fresh exact-Name fold checked against the independently observed source-specific set; there is no internal budget reset or option raise. Full TYPE/universes, actual VALUE hashes and TYPE/VALUE used-constant inventories are printed for current target and caller. The failed combined inventory/retained command hit the unchanged aggregate200000 heartbeat budget before its first retained PASS marker and is rejected; it is retained as failure history. The final two inputs preserve all actual opaque VALUE closure/inferred TYPE/std3 checks as ordinary independent Lean commands. Actual generated qualified names, kinds, levels, full TYPE/opaque VALUE metadata and source absence are printed. Default limits200000/synth20000/rec512 are asserted.

## Final unfiltered native diagnostics

| File | Success | Partial | Timed out | Errors | Warnings |
|---|---|---|---|---:|---:|
|ML|true|false|false|0|1|
|Main|true|false|false|0|4|
|Eval|true|false|false|0|0|

Every actual tool name/argument/start, immediately observed returned/saved response time and later post-pin bookkeeping completion, complete raw response, launch source bytes and pre/post17 pins are saved. Separate response observations precede post-pin captures; historical completed_unix is not misrepresented as call end. No declaration, range or severity filter is used. Existing header/unused-variable warnings remain visible; no copyright metadata was invented. LeanEval has no diagnostics.

## Final matched performance

| Scope | Before1 ms | Before2 ms | After1 ms | After2 ms | Mean Δ ms | Mean Δ% |
|---|---:|---:|---:|---:|---:|---:|
|target|719.805|720.953|204.320|204.755|-515.841|-71.60696|
|consumer|4964.514|5094.045|5381.177|5157.626|240.122|4.77448|

All four actual raw captures and eight raw before/after Lake environments match the frozen observed parent environment and exact CLI/scope/options, with source-specific complete printed-command payload bindings and dynamically discovered qualified kernel siblings. Sums include only complete disjoint column-zero roots once. No Meta roots, nested timings, inclusive wrappers, next/end command roots, global substitutions or cherry-picked third sample.

The complete caller remains an explicit foreign original27/global over1000 failure, not a file pass. main-stages24-diagnostics.json retains ALL same-indent event strings/order and actual root sequences for paired control/change diagnosis. Nested inclusive values are never added to outer sums; no causal or noise dismissal is made. The changed hΘ application and all other events are reported separately.

Actual changed hΘ diagnostic: `[{"index": 96, "event": "✅️ have hΘ :=", "samples_ms": [118.893, 117.32, 149.449, 142.984], "paired_delta_ms": [30.55600000000001, 25.664000000000016], "mean_delta_ms": 28.11, "raw_lines": [1245098, 1245370, 1090952, 1091371]}]`.

## Input closure and evidence

Final property v10 has its own fresh before/after extra-module/compiled-companion capture; all additional artifacts and actual parser source headers remain unchanged. Earlier scratch scope gaps are preserved in the erratum above, with no backdating.

Fresh before/end17 pins compare: only MainLemma changed; Main, all other Lean sources and all3 project/config pins stay exact. Actual direct --deps raw output is byte equal. The package/setup availability union plus pinned core compiled SUPERSET is freshly hashed; exact project-cache intersection is excluded from strict external comparison. All 24782 strict external inputs (3918200888 bytes) remain equal; this is not claimed to be an exact loaded-module closure. Four actual resolved/pinned Lean/Lake/Elan binaries, actual setup/options/importArts/cache companions and frozen raw Lake environment are recorded. End cache has 104 companions. Source and every launched variant remain available as bytes by SHA, including failed and interrupted histories.

All artifacts, required external references, final report, source/config pins, binaries and strict external compiled-input availability are covered by manifest24.json. manifest24-second-rehash.json is the separate fresh verification record; those two manifest files are explicitly excluded from self-reference. final24-fresh-drain.json records every actual owned group, including the interrupted group with null child exit/time, and every completed native request. Final acceptance requires those manifest/drain records before all seven leases are released.

## Gate status — original24

| Gate | Result | Details |
|---|---|---|
|lake_build_file|pass|Fresh selected-v3 affected/full and separate Eval actual exit0. Entire old/entry/selected proof replay, retained inventory and native checks pass. |
|definition_protected|pass|No production def/abbrev changed; DATA actual values independently compared. |
|theorem_statement_protected|pass|Declared, standing-user-authorized generalized API; exact old contract recovered and compared separately, expected new TYPE checked exactly. No accidental statement drift or weaker conclusion. |
|structure_gate|pass|8≤30 proof lines, no branch, conjunction or new helper. |
|naming_gate|pass|Concrete content rename accepted and handed to sole owner for project-end queue, not silently deferred. |
|line_packing_gate|pass|Actual widths89/72/65; next whole binders make107/102>100. |
|inequality_orientation_gate|pass|0 forbidden orientations in code; source quotation exact. |

Overall: pass for original24 scope. MainLemma/global performance remains pending original27; no whole-file completion claim.

## 6b — Result summary

Before17 proof lines; after8; saved9. Fixed proof/domain/log/Nat boilerplate, public summary, signature packing and two terminal simp blocks. Rules applied1.4/1.10/1.16/1.17/2.3/2.11/2.13/3.4/3.7 where applicable; all42 statuses above. Gates: pass. Renames-queued: `Roth.lem7_hyp_of_h32 → Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul`, accepted by owner for the single project-end central sidecar. Comments-preserved: exact target Source quotation and all seven caller signposts; no target inline comments removed. No further refactoring recommendation remains beyond the concrete rename and existing original27/global queue.

| Required phase | Result | Evidence |
|---|---|---|
|Step1 references|pass|Full required files read and immutable24-reference bundle. |
|Step2 full audit|pass|All24 rows above. |
|Step2.5 search|pass|Five actual methods, honest error/fallback, guarded exact?/apply? observations. |
|Step2.6 generalization|pass|Every old/new outer binder and actual inner-binder check; a–e, 3 actual literature queries/top3 each; complete old contract/boundaries/counters. |
|Step2.7 packing|pass|Exact per-line arithmetic table. |
|Step2.8 inequality|pass|Explicit zero-occurrence scan, quote preserved. |
|Step3 golf|pass|All42 rules, actual automation and final direct-term property run. |
|Step4 reflection|pass|Positive square scaling removes sign split and all public log/Nat work; manual simplify review explicitly scoped. |
|Step5a diagnostics|pass|Complete unfiltered native ML/Main/Eval success, nonpartial, nontimeout, zero errors. |
|Step5b diff gates|pass|Seven named gates above; exact reversal restores all unchanged context. |
|Step6a rename sidecar handoff|pass|Concrete pair delivered to owner, who exclusively controls shared queue edits. |

Manual simplify/buzz phases are disclosed above; no independent simplify-agent claim or unavailable skill invocation is fabricated. No Git publication performed by this leaf.

Actual dynamically derived drain inventory: 57 wrapped execution contexts (including the dedicated outer recursive-parser driver and interrupted child with unknown exit/time), 159 actual nested dependency-parser commands, 57 distinct owned groups, and 16 completed tool queries. Of the tool queries, 15 have regular complete pin brackets; the single rejected multi-attempt has the disclosed failed before-bookkeeping recovery record and is not acceptance evidence. No historical fixed run count is assumed. The second fresh manifest rehash also performs a new actual group-absence check after all rehashes and records it inside the explicitly self-excluded verification record.
