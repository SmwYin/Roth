from pathlib import Path
import json
D=Path(__file__).resolve().parent;N='Roth.approxSet'
def link(n,label=None):return '['+(label or n)+'](../evidence/'+N+'/'+n+')'
rows=json.load(open(D/'callers.json'))['source_explicit']
report='''# Roth.approxSet — canonical267

**Verdict: BORDERLINE-needs-human.** Completed assessment; the remaining questions concern future upstream API design, not verification or a request to stop this overview. Keep the current project definition while choosing a primary approximation-family API. The fixed coefficient `1` and the original integer/natural pair representation carry real mathematical information. Neither an ordinary metric ball, a generic comprehension constructor, the reduced-rational Dirichlet theorem, nor `LiouvilleWith` is an exact replacement.

## Phase0 — baseline and provenance

The definition resolves at `Roth/Main.lean:55–56`. Fresh hashes of all17 production source/pin inputs agree with the shared baseline manifest; the reusable baseline was a clean `lake build` with2467jobs. The entire588-line Main module and66-line LeanEval module were read and archived, and their bodies replayed in scratch. No production source, pin, Git, overview or progress edit was made. No file-end build is due here: the accepted prior MainLemma/file-end build is historical evidence; the next scheduled boundary is289.

Evidence: INPUTS; BASELINE; SOURCES; ORIGINAL.

## Phase1 — mathematical content and full type

For arbitrary real α and real exponent κ, the definition collects **unreduced** integer/natural pairs `(h,q)` with positive q and strict approximation error `|α−h/q| < q^(−κ)`. It records the supplied denominator, rather than the denominator of the reduced rational value. Irrationality, algebraicity and positivity of κ are assumptions of later results, not prerequisites for constructing this set.

Full native Lean type:
```lean
Roth.approxSet : ℝ → ℝ → Set (ℤ × ℕ)
```
Exact written declaration:
```lean
 def approxSet (α κ : ℝ) : Set (ℤ × ℕ) :=
   {hq | 0 < hq.2 ∧ |α - (hq.1 : ℝ) / hq.2| < 1 / (hq.2 : ℝ) ^ κ}
```
Both parameters occur essentially in the family. Construction uses conjunction, absolute error, casts, division and real powers. There are no project dependencies in its type or body, and hence no transitive project dependency of the definition itself. Native `Lean.getConstInfo` with `pp.funBinderTypes` produced the full type; `pp.all` printed the full kernel body without elision. The original and replay depend only on `propext`, `Classical.choice`, `Quot.sound`.

Evidence: TYPE; DEPENDENCIES; ORIGINAL.

## Phase2 — preliminary and one-line definition test

**BIG:** this introduces the semantic approximation family in the module's main theorem, rather than an incidental arithmetic helper. The body has one substantive line.

| One-line exemption | Applies | Concrete evidence |
|---|---|---|
| Avoid defeq abuse | No | Membership unfolds definitionally; `pointwise` and `constant_one_literal` compile by reflexivity. No sealed normalization barrier is needed. |
| Avoid typeclass diamonds | No | The definition is a set-valued function, not an instance, new carrier or coercion. |
| Semantic intent / stable API | Yes | Ten explicit declaration callers use the same family; reduction preserves unreduced q, reduced approximation selection changes q, and the main finiteness/infinitude statements need a common name. |

Conclusion: **ONE-LINER WITH-EXEMPTION**. Actual full-body inlining succeeds, so the name is technically removable. That does not settle whether its reusable mathematical API should be named upstream.

## Phase3 — exhaustive literature

Every requested named channel was attempted. Search absence is reported as a bounded outcome, not a mathematical absence claim. Only requests, returned-response hashes/byte counts/status, clean titles/URLs/locators and original summaries are archived. The one returned credential-bearing thesis URL was stripped of its whole query before archival; no signed query or article/search-result body is retained.

| Channel | Exact query/request evidence | Finding |
|---|---|---|
| General web, specific form | WEBGENERAL query1: integer/natural pair approximation and Roth | Pair form and positive denominator occur in Roth formulations. |
| General web, wider form | WEBGENERAL query2: approximating function ψ, C, rational height | Arbitrary denominator-dependent errors and height functions are genuine standard families. |
| General web, alias | WEBGENERAL query3: irrationality exponent, noncoprime multiples | Reduced/coprime formulations and exclusion of exact equality matter for rational α. |
| Optional mathematical second opinion | OPTIONAL | Justified n/a: `ask_chatgpt_math` unavailable. |
| Local clean.tex | LOCAL, lines1139–1197 and1571–1610 | Eq.(1) is exactly the coefficient1 pair inequality; the reduction introduces M and absorbs it using a smaller exponent. Later prose explicitly proves reduction of pairs and finite rational-value fibers. |
| nLab | WEBCHANNELS: `site:ncatlab.org/nlab Diophantine approximation` | Broad number theory/arithmetic geometry pages; no exact family definition returned. |
| distinct nCatLab | WEBCHANNELS: `site:ncatlab.org/ncatlab Diophantine approximation rational height` | Out-of-namespace nLab results, no exact nCatLab hit. This is an actual distinct namespace query. |
| Stacks | WEBCHANNELS plus WEBAPI exact phrase query | No relevant direct result. This is an approximation/height family, not an algebraic-geometric scheme construction. |
| MathOverflow | WEBCHANNELS: reduced fractions and irrationality exponent | Discussions use positive C, coprime pairs and denominator restrictions; contextual evidence, not a formal replacement. |
| recent arXiv | WEBAPI: `after:2021-10-29 before:2026-10-30` | Primary2024 abstracts for2403.11257 and2409.03331 distinguish approximating functions, reduced fractions and restricted denominator families. Older/out-of-window hits are not represented as recent evidence. |
| Definition-specific mathlib web API, overview4a | WEBAPI query2: `mathlib4 DiophantineApproximation Basic infinite_rat_abs_sub_lt_one_div_den_sq irrational` | Official mathlib4 documentation found; this is additional to the three general queries and15formal cells. |

The primary abstract of [Frühwirth–Hauke (2024)](https://arxiv.org/abs/2403.11257) uses arbitrary ψ and distinguishes reduced fractions. [Tan–Zhou (2024)](https://arxiv.org/abs/2409.03331) gives a denominator-restricted, inhomogeneous direction; that is related research, not the same definition. The attempted PMC height-functions source open returned a CAPTCHA, honestly recorded in WEBPRIMARY. Current official [mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/DiophantineApproximation/Basic.html) uses reduced rational denominator height at exponent2. Exact pinned-source/native verification is separate from these potentially different web revisions.

**Literature synthesis:** no universal choice between an unreduced pair family, reduced rational-height family, and filter/existential-C predicate is imposed by the literature. All are useful, with distinct quantification. The arbitrary-error/C family is a real semantic extension; simply replacing arithmetic with an arbitrary predicate would discard the intended denominator-height relation.

## Phase4a–4b — parameter generality and verified semantic families

| Parameter/data | Current meaning | Alternative and actual verification |
|---|---|---|
| α:ℝ | Target real, unrestricted | Preserve it. Rational targets are legitimate inputs; all rational targets have infinitely many exact pair multiples. Irrationality must not be added to the definition. |
| κ:ℝ | Arbitrary real exponent | Preserve zero/negative exponents. Theorems about reduced images require κ≥0; finite fibers require κ>0 and irrationality. These are theorem hypotheses, not definition restrictions. |
| h:ℤ, q:ℕ | Signed numerator, supplied natural denominator | Positive-denominator subtype is equivalent packaging; pair multiplication by M in `reduction` preserves q. Replacing pairs by rationals quotients genuine information. |
| `0<q` | Explicitly excludes zero division | `no_zero` compiles for every α,κ,h. A total division convention does not justify admitting q0. |
| coefficient1 | Exact fixed radius normalization | `approxC α κ C` is verified for arbitrary real C, with exact old recovery at C1. `constants_differ` proves C1 and C2 give different sets already at q1, so C is semantic, not arithmetic decoration. |
| radius as q-function | Power-specific error | `approxWith α ψ` accepts any ψ:ℕ→ℝ. A new mathlib-only bounded-denominator finiteness proof compiles for arbitrary ψ, with no positivity/monotonicity assumption on ψ. |
| strict `<` | Endpoint exclusion | Retain it. At α0,h1,q1,C1 the error is exactly1 and the pair is excluded; C2 admits it. Weak `≤` changes membership. |

Verified proposed family:
```lean
noncomputable def approxWith (α : ℝ) (ψ : ℕ → ℝ) : Set (ℤ × ℕ) :=
  {hq | 0 < hq.2 ∧ |α - (hq.1 : ℝ) / hq.2| < ψ hq.2}
noncomputable def approxC (α κ C : ℝ) : Set (ℤ × ℕ) :=
  approxWith α (fun q ↦ C / (q : ℝ) ^ κ)
```
The old family is definitionally the C1 specialization. C≤0 gives the empty set; no positivity hypothesis is needed to define it. `constant_mono` proves monotonicity in C. `exponent_antitone` compiles using q≥1; at q1 the radius is1 for every κ, so increasing κ does not give pointwise strict shrinking.

This establishes a **strict semantic family extension**, rather than a verified drop of a typeclass hypothesis. Moving the entire primary API to a new radius/height representation is a foundational API design decision; this assessment does not label it a one-edit theorem weakening. No cost argument is used in the verdict. Evidence: PROJECT; ISOLATED; SUPPLEMENT.

### Exact representation bridges and guards

`reduced_mem_iff` proves, for every real κ and rational x, `(x.num,x.den)∈approxSet α κ` iff `|α−x|<1/x.den^κ`. `quotient_image` proves equality of the rational-value image of the pair set with that reduced-rational set for κ≥0, using `Rat.den_dvd`, `Rat.num_div_den`, real cast formulas and a new denominator-power monotonicity argument. These bridges are new scratch proofs; those existing Rat lemmas alone are not an existing named approximation-family equivalence.

`finite_fiber` proves each rational-value fiber finite under irrationality and κ>0, using the existing **project** `eventually_div_rpow_lt` and `approxSet_den_le_finite`. `infinite_iff_rat` then proves the complete infinitude equivalence under those hypotheses via `Set.Finite.of_finite_fibers`; the reverse rational→pair implication needs neither irrationality nor κ>0. This is a new bridge assembled from project results, not a mathlib-only replacement claim and not an invocation of `roth`.

`rational_pair_infinite` proves for every rational x and every κ that exact multiples `(x.num*(n+1),x.den*(n+1))` give infinitely many members. Meanwhile the pinned reduced-rational exponent2 set at α0 is finite, verified in ISOLATED. Thus unconditional replacement of pair infinitude by rational infinitude is false, including at exponent3 where exact pair multiples persist. `zero_exponent_fiber_infinite` proves a fixed rational-value0 fiber is infinite whenever |α|<1 and κ0, so irrationality alone cannot supply finite fibers. `negative_reduction_guard` proves `(0,2)` approximates α3/2 at κ−1 whereas its reduced pair `(0,1)` does not: κ≥0 in the image bridge is substantial.

The mathlib-only `infinite_iff_frequently` proves arbitrary-ψ pair infinitude equivalent to frequent positive-denominator witnesses using a new finite-slice argument. `liouvilleWith_iff` proves, for irrational α and every real κ,
```lean
LiouvilleWith κ α ↔ ∃ C : ℝ, (approxC α κ C).Infinite
```
The existential C cannot be replaced silently by fixed1 at the same exponent. `LiouvilleWith` also explicitly excludes exact equality; the irrationality premise removes that discrepancy in the proved bridge. Its `.frequently_lt_rpow_neg` permits a strictly smaller exponent, not automatic equality of the original fixed-κ pair set. No blanket irrationality equivalence at every κ is asserted.

## Phase4c — all modern-idiom rows

| # | Diagnostic | Result and concrete consequence |
|---|---|---|
|1| Typeclasses instead of preambles | No. α,κ,ψ are varying data, not structures to infer. No custom class would improve the family. |
|2| Filters/nets | Yes for infinitude endpoints. The verified arbitrary-ψ filter bridge composes with `Filter.frequently_atTop'`, `and_frequently`, and `LiouvilleWith.exists_pos`; retain pair membership for finite slices and numerator transformations. |
|3| Universal property | No object is being constructed up to universal uniqueness. Quotienting pairs is an arithmetic representation change, not such a characterization. |
|4| Bundled substructure | No. An error-defined set is not closed under addition or multiplication. A subtype can bundle witnesses but does not unlock Submodule/Subfield lattice laws. |
|5| Weaken scalar hierarchy | No claimed real-power weakening. An arbitrary-ψ construction can be written over ordered fields, but bounded integer slices require suitable Archimedean/discreteness input. Such a syntactic construction alone is not the verified real Diophantine API. |
|6| Higher categories | No categorical structure is present. |
|7| Concrete indices | q:ℕ and h:ℤ encode rational height and exact multiples. General rational/number-field heights are related but additional data are necessary; replacing ℕ by an arbitrary monoid is not supported. |
|8| Concrete-via-abstract | The def has no proof and no concrete named real witness; target body has0project identifiers. The fixed1 does admit the verified semantic C/ψ family and common finite-slice proof. That is the meaningful abstraction, not arbitrary Set syntax. |
|9| False-generalization guard | Preserve original q, positivity and strict error. The verified C1 recovery preserves the old object. Replacing pair sets unconditionally by reduced rationals or LiouvilleWith fails the rational/κ≤0/constant-quantifier guards above. |

Modern endpoint API is useful, but no single one subsumes all existing consumers. A new pair-family/rational bridge layer could connect them; a filter predicate alone loses finite pair geometry.

## Phase4.5 — six infrastructure risks

| Risk | Rating | Checked reason |
|---|---|---|
|Typeclass diamond|NONE| No new instance or carrier hierarchy; membership uses the existing Set/Prod and real structures. |
|Reducibility leak|LOW| Semireducible arithmetic comprehension; actual rfl recovery and original-signature equality checks pass without an added reducibility attribute. No computational instance is exposed. |
|Noncanonical unfolding|LOW| Explicit projections `.1/.2` of membership are used across callers. Unfolding is predictable, but a new radius-family implementation needs stable membership lemmas. Full raw inlining compiled. |
|Instance priority collision|NONE| Not an instance, so no priority or alternative synthInstance path exists. |
|Universe polymorphism|NONE| Concrete Real, Int, Nat and Set.{0}; no varying universe argument exists to test or silently constrain. Generic universe probes are inapplicable to this concrete function. |
|Coercion ambiguity|LOW| Existing Int/Nat→Real and Rat→Real routes require explicit normalization in bridges. No new CoeFun/CoeSort is declared; full signatures retain the same existing casts. |

Overall **LOW**. No `#synth approxSet` is meaningful: it is not a class. Existing Set membership/function application and rfl/cast/signature probes were executed instead. No HIGH row needs mitigation.

## Phase4.6 — five strategy rows

| Question | Applies | Conclusion |
|---|---|---|
| ε–δ topology | No | Definition has no topology proof. |
| Elements vs subobjects | No | There is no algebraic closure/subobject law to exploit. |
| Sequences vs filters | Yes at endpoint | Generic finite-slice proof plus frequent-witness bridge is verified; use it for infinitude, preserve actual pairs for reduction. |
| Construction vs universal property | No | No universal characterization is at stake. |
| Missing helper API | Yes | A named approximation family needs membership, finite slices, rational image/fiber equivalences and a filter/LiouvilleWith bridge. The last two are new proofs here, not existing mathlib replacements. |

Construction strategy is MATHLIB-IDIOMATIC; **API refactoring recommended** before upstreaming, using the verified family/bridge layer. This recommendation is mathematical organization, not a proof-cost downgrade.

## Phase5 — all15 actual formal searches

FORMAL contains raw complete requests/results for each cell below. External Finder/Search indices may not match the pin; local name search reports `index:error` while still returning source-text hits, so empty index results are never treated as absence. Positive candidates were read in pinned source and independently compiled.

| Form | LeanFinder | Loogle | LeanSearch | rg source | local name |
|---|---|---|---|---|---|
| Current positive-q pair/fixed1/arbitraryκ | LiouvilleWith/Legendre near-matches | `"approxSet"`, no hit | LiouvilleWith, Dirichlet near-matches | full approxSet/Roth.approxSet pattern; no mathlib hit | `approx`, project target plus unrelated approximations |
| Literature rational height/C/ψ | rational Dirichlet results | `"abs_sub_lt_one_div_den"`, three hits | rational squared-error infinitude and convergents | rational approximation/den_dvd signatures | `infinite_rat_abs`, two pinned file hits |
| Abstract denominator function/filter | LiouvilleWith filter family | `"LiouvilleWith"`, predicate and laws | frequent witnesses/ball descriptions | LiouvilleWith/exists_pos/frequent signatures | `Liouville`, two definition hits |

Existing pinned APIs: `Real.infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational`, its irrationality iff, `Rat.finite_rat_abs_sub_lt_one_div_den_sq`, `Rat.den_dvd`, `Rat.num_div_den`, `LiouvilleWith`, `.exists_pos`, `.frequently_lt_rpow_neg`. Paths and exact file hashes: MATHLIBINPUTS. Independent #checks and proofs appear in ISOLATED. Dirichlet's theorem supplies the κ2 endpoint, not arbitrary-κ family membership; Rat's finite theorem uses rational scalar arithmetic/reduced denominator. `LiouvilleWith` is an existential-C predicate, not a set of pairs. Search did not find an exact named arbitrary-κ pair family. This is a bounded search conclusion, not a proof that no possible derived term exists.

## Phase5.5 — three statement-shape checks

1. **Normal form:** raw pair inequality, reduced-rational height inequality and frequent witnesses are different interfaces. Keep pair membership canonical for pair statements, with a rational image equivalence and filter endpoint bridges; do not build O(n²) miscellaneous conversions. `reduced_mem_iff` places the rational predicate on the RHS. Unconditional pair/rational equivalence is rejected. Normal form is OK locally; choose the primary upstream family before shipping.
2. **Syntactic generality:** actually tried raw comprehension in every full caller; arbitraryψ/C specialization; reduced num/den rational membership; rational image; frequently denominator witnesses. Original caller signatures remain definitionally identical after raw inlining (12 equalities). Prefer a stable family name locally; use ψ or C upstream only with explicit membership and bridge API.
3. **Superfluous arguments:** α and κ are essentially used; neither is a proof assumption to remove. No explicit typeclasses, irrationality or algebraicity occur. q positivity and strict inequality are essential data; C/ψ need no positivity assumption for their definitions.

Overall **RESTATE-BEFORE-SHIP** if adding a new general family; current project spelling is coherent and not junk.

## Phase6.0 — complete callers and inline audit

There are10source-explicit declaration callers:8in Main and2in LeanEval (one external file). Native canonical audit separately finds12direct kernel-value consumers and10direct type consumers. `roth_rat` and `thueSiegelRoth` have no explicit source approxSet occurrence, but elaborated parameter terms include the constant. These counts do not assert the transitive/simp closure. There is no target simp attribute. Source enumeration uses canonical metadata plus fresh `rg --no-ignore` and tracked `git grep`, avoiding ignore-rule omissions.

CALLERTABLE

Every caller's complete source body is archived, together with both complete modules. INLINE replays all Main and LeanEval bodies with raw literal replacement of explicit target references and proves9public +3private original-signature equalities. Private constants are accessed by fresh-level term elaborators using `Lean.mkPrivateNameCore` with the correct original module. It does not insert axioms or textual malformed private identifiers. All12proof axiom audits are standard. Transitive dependence through original project lemmas is not claimed to disappear.

The inline audit also checked `roth_rat`'s reduced-rational input and `abs_eval_lt_of_le_index`'s weak coordinatewise errors: these are useful related formulations, not a second exact bypassed definition. LeanEval's uniform positive lower-bound predicate is another quantified endpoint. INLINEAUDIT retains the search and distinctions.

## Phase6 — actual composition experiments

* **Raw syntax:** `constant_one_literal` is rfl; all caller inlining succeeds. `Set.ofPred` constructs a set from a supplied arithmetic predicate. This is construction infrastructure, not an existing semantic approximation-family replacement. The compiled type-negative candidates show `Set.ofPred` and `Metric.ball` are not directly the required function; supplying the entire rational-height relation by hand is precisely the missing data.
* **Metric ball:** a ball is a fixed-radius set in one ambient type. Here the radius depends on the supplied denominator and the quotient map identifies different heights. A ball alone does not encode that relation. No blanket replacement is claimed from syntactic abs/dist equivalence.
* **Reduced rational Dirichlet endpoint:** the κ2 theorem compiles and yields a useful input set; new image/fiber proofs are necessary for the arbitraryκ pair family. The rational exact-multiple counterexample rules out unconditional interchange.
* **Filter/LiouvilleWith endpoint:** the exact existential-C bridge compiles mathlib-only, but required a new arbitraryψ finite-slice proof and frequent-witness argument. That new proof is not a ≤3-existing-call replacement. It also changes quantification from fixed1 to ∃C and, without irrationality, excludes exact equality.

Conclusion: **NOT-COMPOSABLE from an existing named semantic family in ≤3 calls.** Literal definition inlining is available; no cost-based argument turns that observation into a semantic API verdict. The diagnostic witness equality in ISOLATED proves only the supplied comprehension's equality; it is not counted as discovering an existing definition. Definitions with goal `Set _` admit arbitrary witnesses, so an unconstrained `exact?` witness search would not test the intended mathematical family.

## Phase7 — actionable verdict

**BORDERLINE-needs-human**, because the primary upstream interface and useful named API boundary remain genuine design choices. This is not inherited from a parent verdict, not based on proof difficulty, and not a dismissal of an integer/natural representation as obsolete. The real contribution would be an approximation-family API with finite-slice and pair/rational/filter bridges, rather than this isolated fixed1 name. The actual generalization and complete caller experiments establish the available choices and their limits.

Concrete future upstream questions (not current user blockers):
1. Should `Mathlib/NumberTheory/DiophantineApproximation/ApproximationSet.lean` introduce a named unreduced pair family parameterized by ψ, with the power/C family as a specialization?
2. Should reduced-rational height sets be the primary public interface, while a pair-family layer remains public for denominator-preserving transformations and finite fibers?
3. Should the generic finite-slice/frequent-witness and irrational `LiouvilleWith ↔ ∃C, Infinite` bridges ship together with that family, rather than adding a standalone fixed1 definition?

Keep `Roth.approxSet` in its current local destination until these API choices are made. If upstream chooses a family, preserve `approxSet α κ` as its C1 specialization during migration, retain original public theorem signatures as verified here, and supply the κ≥0/irrationality/κ>0 bridge hypotheses explicitly. Assess later declarations independently; this definition's verdict does not pre-decide finiteness or Roth's theorem. No YES PR grouping/reviewer selection is asserted for this BORDERLINE assessment.

## Phase8 — verification and delivery

Five accepted sources have complete successful, warning-free receipts; disk runs are explicitly nonpartial, isolated run_code diagnostics successful and not timed out. Four rejected native sources/receipts remain separately labeled (project missing denominator normalization/deprecated spelling, isolated endpoint rewrite, inline whitespace warning, supplement cast/conjunction errors). The first original cold query was warming/partial and is not accepted proof evidence. One initial inline width preparation failed before writing/executing; that preparation is not represented as native evidence.

The exact293 canonical name array is generated from tracked order, checked before execution by the independent root script, and runtime checked for293requested/unique/present/values. Native dependency info, full type/body,10source and12kernel caller distinctions,15formal cells, all literature requests, exact20import authorization, hashes and timings are retained. The portable validator checks current manifest artifacts in scratch and simulated integrated layouts, including required overview keys and full type. Final source/pin hashes and credential guard must pass before freeze. Root acceptance remains pending.

VERIFICATION; VALIDATOR; GUARD.
'''
subs={'INPUTS':link('inputs.json'),'BASELINE':link('baseline-build.txt'),'SOURCES':link('source-Main.lean.txt')+' and '+link('source-LeanEval.lean.txt'),'ORIGINAL':link('original-executed.lean.txt')+' / '+link('original-receipt.json'),'TYPE':link('native-type.json'),'DEPENDENCIES':link('dependencies.json'),'WEBGENERAL':link('web-general.json'),'WEBCHANNELS':link('web-channels.json'),'WEBAPI':link('web-recent-api.json'),'WEBPRIMARY':link('web-primary.json'),'OPTIONAL':link('optional-math-opinion.json'),'LOCAL':link('local-excerpt.tex.txt'),'PROJECT':link('project-executed.lean.txt')+' / '+link('project-receipt.json'),'ISOLATED':link('isolated-executed.lean.txt')+' / '+link('isolated-receipt.json'),'SUPPLEMENT':link('supplement-executed.lean.txt')+' / '+link('supplement-receipt.json'),'FORMAL':link('formal-search-matrix.json'),'MATHLIBINPUTS':link('mathlib-inputs.json'),'INLINEAUDIT':link('inline-audit.json'),'INLINE':link('inline-executed.lean.txt')+' / '+link('inline-receipt.json'),'VERIFICATION':link('verification.json'),'VALIDATOR':link('validate.py'),'GUARD':link('secret-guard.json')}
for a,b in sorted(subs.items(),key=lambda x:-len(x[0])):report=report.replace(a,b)
tab='| Caller | Original source line | Actual usage |\n|---|---|---|\n'
uses={'approxSet_den_le_finite':'Finite bounded denominator slice','reduction':'Infinitude under numerator scaling and smaller exponent','approxSet_num_den_mem_aux':'Reduction of num/den with κ≥0','exists_reduced_approx':'Infinite set yields reduced large denominators','exists_approximants':'Finite sequence of reduced approximation witnesses','exists_roth_approximants_aux':'Approximation family threaded into balanced degree choices','roth_of_isIntegral':'Main algebraic-integer infinitude hypothesis','roth':'Main algebraic-real infinitude hypothesis','exists_pos_div_rpow_lt_aux':'Finite pair-set yields uniform positive lower constant','isDiophantine_iff':'Exponent-infinitude endpoint equivalence'}
for x in rows:tab+='| '+link(x['archive'],'`'+x['name']+'`')+' | '+x['file']+':'+str(x['line'])+' | '+uses[x['name'].split('.')[-1]]+' |\n'
report=report.replace('CALLERTABLE',tab)
(D/'report.md').write_text(report)
print('Report',len(report.split()),'words')
