# Roth.lam — canonical 229

**Verdict: BORDERLINE-needs-human.** The completed assessment supports retaining this as a documented project parameter while the eventual upstream Roth API is designed. It does not support a standalone parameter-only PR. The two questions in Phase 7 concern future upstream organization; they are not unresolved verification or a blocker for the overview.

## Phase 0 — Baseline and scope

The declaration is the public noncomputable definition at `Roth/MainLemma.lean:60`. All seventeen production-source/pin hashes freshly match the shared manifest; the clean baseline is `lake build`, exit 0, 2467 jobs. This declaration is not a file endpoint; the accepted preceding Theta endpoint build is additional context, and no new whole-project build is required here. No production source, pin, Git, overview, or progress file was changed. Scratch work used only this evidence package and the authorized persistent native document, preserving its nine imports.

The whole declaring module, the whole Main caller module, Lattice's differently bound `lam` variables, all four actual caller bodies, local reference passages, and relevant pinned sqrt source were read. Original MainLemma replay, full MainLemma/Main inlining, isolated mathlib proofs, and actual-context bridges are clean. [Inputs](../evidence/Roth.lam/inputs.json), [baseline](../evidence/Roth.lam/baseline-build.txt), [source MainLemma](../evidence/Roth.lam/source-MainLemma.lean.txt), [source Main](../evidence/Roth.lam/source-Main.lean.txt), [verification](../evidence/Roth.lam/verification.json).

## Phase 1 — Mathematical content and full native type

For a real number δ and natural numbers n and m, define λ(δ,n,m)=4(1+3δ)n√m. In the application, n is an integer polynomial degree, m is the number of variables, and 1+3δ accounts for the coefficient scale used in the auxiliary-polynomial pigeonhole argument. The real cutoff λ makes the generic lattice-count factor 2√m/λ compatible with the budget `(1+3δ)nD ≤ N/2`. This is a chosen quantitative parameter, not a theorem asserting a bound by itself.

Full elaborated kernel type from `Lean.getConstInfo`, with `pp.funBinderTypes=true`:

```lean
Roth.lam : ℝ → ℕ → ℕ → ℝ
```

Source signature/body:

```lean
noncomputable def lam (δ : ℝ) (n m : ℕ) : ℝ := 4 * (1 + 3 * δ) * n * √(m : ℝ)
```

Every parameter is explicit. There are no hypotheses, universe parameters, user typeclasses, or project dependencies in the body. The noncomputability is inherited from the real square root. A `pp.all` print of the actual kernel definition is complete in the receipt: **no printer-elision marker occurs**. It contains four real multiplications, a real addition, two natural casts and `Real.sqrt`, together with numeral/instance elaboration. [Native type/body](../evidence/Roth.lam/native-type.json), [complete original receipt](../evidence/Roth.lam/original-receipt.json), [exact original replay](../evidence/Roth.lam/original-executed.lean.txt).

## Phase 2 — Preliminary checks

**SMALL.** It is a proof parameter rather than a new structure or the main theorem. Being a parameter of Roth's proof does not turn it into a named theorem or transfer the parent theorem's upstream merit.

**One substantive body line: ONE-LINER WITH EXEMPTION (local API semantics).**

| Exemption | Applies? | Concrete evidence |
|---|---|---|
| Avoid defeq abuse | No established need | `Lam229Project.unfolding` is `rfl`; all four callers tolerate full inlining. No opaque barrier is needed for the verified consumers. |
| Avoid typeclass diamonds | No | It returns an ordinary real and registers no class, instance or coercion. The only selected operations are existing real operations and casts. |
| Mark semantic intent/API stability | Yes, within this project | `gam` names `(m−λ)/2`, the eta/gamma comparison unfolds the choice, and `exists_delta` normalizes it at δ=0. The docstring connects the choice to eq.(34). This is evidence for a local stable name, not automatic justification for a public standalone mathlib definition. |

Inlining is verified, not inferred from the short spelling. [Project unfolding/bridges](../evidence/Roth.lam/project-executed.lean.txt), [full caller inlining](../evidence/Roth.lam/inline-executed.lean.txt).

## Phase 3 — Exhaustive literature protocol

Every named channel was attempted. Exact requests, returned-response SHA256/byte count/status, clean titles/URLs/locators and original concise summaries are archived; full article or search-result bodies are not. Failed search coverage or an irrelevant result is not proof of absence. The distinct nCatLab query actually targets `/ncatlab`, not merely the shared host.

| Channel | Actual query or locator | Outcome and relevance |
|---|---|---|
| General web, specific | `Roth theorem auxiliary polynomial lambda "1+3" "4" sqrt m` | Exact-constant framing; search also returns unrelated Roth/lattice material. Local eq.(34), rather than a false positive, establishes this formula. |
| General web, general | `Roth theorem main lemma lattice point count lambda square root dimension` | Auxiliary-polynomial/counting context, alongside additive-combinatorics Roth false positives. |
| General web, aliases/history | `Thue Siegel Roth auxiliary polynomial construction parameters lambda gamma delta` | The arithmetic theorem and historical auxiliary-polynomial method are identifiable; it does not establish a universally named independent lambda function. |
| Optional ChatGPT math | `ask_chatgpt_math` unavailable | Justified unavailable channel; other channels were not reduced. |
| Local clean.tex | §6, eqs.(34),(35),(44),(45) and coefficient/pigeonhole proof, lines1337–1344 and1423–1500 | Exact parameter and its role: after the count bound, `(1+3δ)nD ≤ 2(1+3δ)n√m λ⁻¹N = N/2`. The definition is tied to this proof's coefficient losses and chosen count estimate. |
| nLab | `site:ncatlab.org/nlab Roth theorem auxiliary polynomial Diophantine approximation` | Diophantine equation, number theory and Vojta pages; surrounding concepts, no exact cutoff in returned results. |
| nCatLab, distinct namespace | `site:ncatlab.org/ncatlab Roth theorem auxiliary polynomial lambda` | Search returned out-of-namespace `/nlab` lambda calculus/rings and other unrelated pages. No exact in-namespace hit was returned. |
| Stacks | `site:stacks.math.columbia.edu Roth Diophantine approximation auxiliary polynomial` | Commutative algebra, minimal-polynomial tag09GL, approximation and divided powers; no returned source for this cutoff. Its arithmetic choice is not a categorical or scheme-theoretic construction. |
| MathOverflow | `site:mathoverflow.net Roth theorem auxiliary polynomial lambda square root dimension` | Quantitative Roth bounds, applications and multidimensional questions; contextual rather than an exact definition source. |
| Recent arXiv, full five-year window | `site:arxiv.org Roth theorem auxiliary polynomial parameters Diophantine approximation after:2021-10-28 before:2026-10-29` | Goel–Lunia–Ray2502.00731 (2025; v2 July2026) is relevant. Several other hits concern different dynamical/additive/analytic problems and are not treated as replacements. |
| Supplementary official mathlib/book query | `mathlib4 Roth Diophantine lambda auxiliary polynomial parameter sqrt`; book-author query | Official Dioph documentation concerns integer polynomial equations, a different meaning of “Diophantine.” Publisher/JSTOR book metadata confirms context, not this formula. |

Evidence: [general requests](../evidence/Roth.lam/web-general.json), [local search](../evidence/Roth.lam/local-literature.json), [local passage](../evidence/Roth.lam/local-excerpt.tex.txt), [nLab](../evidence/Roth.lam/nlab.json), [nCatLab](../evidence/Roth.lam/ncatlab.json), [Stacks](../evidence/Roth.lam/stacks.json), [MathOverflow](../evidence/Roth.lam/mathoverflow.json), [recent arXiv](../evidence/Roth.lam/arxiv.json), [primary access](../evidence/Roth.lam/primary.json), [primary locators](../evidence/Roth.lam/primary-locators.json), [supplementary API/book](../evidence/Roth.lam/web-api-book.json).

The relevant recent primary exposition uses a relative index loss ε, a cutoff `m(1−ε)/2`, and an exponential monomial-count bound in §3.3, Lemma3.5. It provides a real alternative proof parameterization, rather than a semantic requirement for the particular expression `4(1+3δ)n√m`. The local formula agrees exactly with its local source. Neither variation of proof parameters nor the different number-field setting proves that changing constants in this existing proof preserves its conclusions. [Goel–Lunia–Ray, §3.3](https://arxiv.org/html/2502.00731v2).

**Literature summary:** the standard concept is an auxiliary-polynomial index cutoff/error budget in a Roth proof. This exact lambda is a documented choice for one quantitative implementation. Sources establish the broader method and distinct parameterizations; they do not establish a uniquely standard independent lambda API.

## Phase 4a — Every parameter and generality dimension

| Parameter/dimension | Current form | Concrete assessment |
|---|---|---|
| δ | Arbitrary real | No positivity premise to weaken. `signGuard` shows δ=−1 can give a negative value, so a global nonnegative-valued replacement would change the total definition. |
| n | Natural degree, cast to real | A real-scalar extension compiles and specializes definitionally. In actual consumers it is a polynomial degree. Widening the raw expression does not generalize the theorem's degree interface. `degreeMatters` rules out simply dropping it. |
| m | Natural dimension, cast under square root | A real-scalar extension compiles; actual consumers use finite `Fin m`, cardinals and dimension-dependent counts. Negative “dimensions” belong to an arithmetic extension, not that finite-variable meaning. `dimensionMatters` rules out dropping it. |
| Output ℝ / square root | Real total square root | Needed for the intended real inequalities and square-root dimension. The expression can be interpreted in a semiring with a supplied function, but an arbitrary function is not a square root and does not preserve the intended parameter meaning. |
| Constants 4,3,1 | Fixed quantitative choices | Three δ losses are tracked in the local derivative/diagonal/remainder coefficient estimate. Four combines the count numerator2 with the target half-budget. A generic scale `a` is meaningful; arbitrary replacement of each constant does not automatically preserve this Roth argument. |
| Signs/zero cases | No side conditions | n=0 or m=0 is allowed; the value is0. No new `[NeZero]`, degree≥2 or m>0 premise should be added merely because the application has one. |
| Universes/instances | None | Native universe parameters `[]`; only existing real instances appear in `pp.all` body. |

Positive mechanical experiments are genuinely compiled: `formula (δ n m : ℝ)` extends the two natural inputs, `algebraic [Semiring R] (s : R → R)` interprets the syntax, `abstractBridge` absorbs `(1+3δ)n` into a single real scale, and `scaleCount` proves the corresponding generic cancellation under positive scale/dimension. [Isolated exact source](../evidence/Roth.lam/isolated-executed.lean.txt), [isolated receipt](../evidence/Roth.lam/isolated-receipt.json), [actual-context bridges](../evidence/Roth.lam/project-receipt.json).

## Phase 4b — Generality verdict

**MAXIMALLY GENERAL for the fixed degree/dimension interface, with no hypotheses to drop.** A larger raw scalar domain is verified, but has not been identified as a literature-standard semantic replacement. Thus this is not a `YES-but-generalise-first` claim. The genuine potential upstream design choice is whether to expose an arbitrary admissible real cutoff/coefficient scale, specializing to `a=(1+3δ)n` only in the application. That design includes the count and auxiliary-polynomial statements, not just an edit to this definition's casts.

No weakening is claimed on the basis of appearance. New scratch `formula`, `scaled`, `algebraic`, the reassociation bridge and `scaleCount` are newly written experiments, **not existing mathlib counterparts**.

## Phase 4c — Modern-idiom check, all nine rows

| # | Diagnostic | Result / proposed form | Actual downstream consequence |
|---|---|---|---|
| 1 | Typeclasses instead of bundled hypotheses | No: there are no structural hypotheses to bundle or infer. | Creating a class for one selected real constant provides no new inference. |
| 2 | Filters/nets instead of metric/sequences | No: the definition is a scalar expression. | `exists_delta` concerns continuity, but its full proof survives inlining; this is not itself a limit statement. |
| 3 | Universal-property characterization | No established need. A chosen quantitative cutoff is not constructed by a uniqueness/universal property. | No universal-property API has been shown to improve consumers. |
| 4 | Bundled substructure instead of closure predicate | No: returns a real, not a subset with closure. | No lattice/quotient/submodule benefit exists here. |
| 5 | Weaken field/module hierarchy | No semantic class weakening established. Semiring-plus-function syntax compiles, but has no square-root laws. | That syntactic experiment does not supply real inequality/count API. |
| 6 | Higher-categorical generalization | No: no category or categorical law occurs. | None. |
| 7 | Concrete index to abstract structure | Real n/m extension compiles, but degree and number of variables remain natural in actual callers. | Useful only as an arithmetic representation; no new finite-variable theorem follows. |
| 8 | Concrete-via-abstract adversarial body test | The defining body mentions `Real.sqrt` once and has no proof-after-unfolding segment. In caller proofs the selected formula disappears after normalization. The more general existing project helper already takes real scale `c`; scratch `scaled a x` and `scaleCount` make this explicit. | An admissible cutoff or scale could separate the lattice bound from the later polynomial coefficient choice. This is a concrete API boundary to consider with the parent theorem, not a verified already-existing mathlib definition. |
| 9 | False-generalization guard | Reject arbitrary `s : R→R` as a semantic square-root generalization and reject negative real “dimensions” as the same finite-variable object. Keep real degree/dimension extension and scale absorption labeled representations. | Preserves the actual arithmetic theorem; `signGuard` prevents silently forcing nonnegative output for all δ. |

**Modern-idiom verdict:** no established standalone modernization of `lam` worth claiming as a new general definition. A useful parent API may quantify over an admissible cutoff or scale, with the current formula as one choice. The broad arithmetic normalization is verified; the boundary choice is recorded in Phase7. This conclusion is based on mathematical meaning and the concrete consumer interface, not implementation cost.

## Phase 4.5 — Definition infrastructure risk, all six rows

| Risk | Level | Evidence |
|---|---|---|
| Typeclass diamond | NONE | `lam` is a real-valued function; it adds no typeclass or instance. `#synth Mul ℝ`, `Add ℝ`, `NatCast ℝ` select the existing real instances. |
| Reducibility leak | LOW | Ordinary definition with no `@[reducible]` attribute. `unfolding` and the real-formula bridge are `rfl`; short arithmetic can be unfolded deliberately. The definition is not a protective opaque barrier. |
| Noncanonical unfolding | LOW | Three source consumers explicitly normalize the selected formula. Expanded `(4+12δ)n√m` is equivalent by `ring`, but should not create a competing global simp normal form. Full inlining works. |
| Instance priority collision | NONE | This declaration is not an instance and sets no priority. No new search path is installed. |
| Universe polymorphism | NONE | Native `levelParams=[]`; all inputs/outputs are concrete real/natural types. The separately tested semiring expression is universe-polymorphic and is not this original definition. |
| Coercion ambiguity | NONE | No `CoeFun`/`CoeSort` registered; Nat→Real casts are explicit in the elaborated body. A correctly typed negative `CoeFun ℝ` probe confirms ordinary real values do not gain an unexpected function coercion. |

**Overall LOW**, no HIGH row. Initial isolated code compiled, but its negative coercion test failed for metavariable reasons in `inferInstanceAs`; it is archived and excluded as risk evidence. The revised typed `inferInstance` test fails for the intended missing CoeFun instance, with clean whole-snippet success. [Rejected source](../evidence/Roth.lam/isolated-probe-rejected-executed.lean.txt), [rejected receipt](../evidence/Roth.lam/isolated-probe-rejected-receipt.json), [accepted isolated receipt](../evidence/Roth.lam/isolated-receipt.json).

## Phase 4.6 — Proof strategy, all five rows

This is a definition; the relevant strategy is its construction and how the consumers use it.

| # | Strategy question | Applies? / evidence |
|---|---|---|
| 1 | ε–δ versus filters | No defining proof. Main.exists_delta already uses `ContinuousAt.eventually_lt`; full caller replay preserves it. |
| 2 | Elementwise algebra versus bundled inclusions | No subobject argument. Real arithmetic and existing casts are the direct construction. |
| 3 | Sequences versus nets | No sequence in the definition; no limit statement needs restating. |
| 4 | Explicit categorical construction versus universal property | No category involved. |
| 5 | Helpers mathlib should have | No missing sqrt, arithmetic or continuity helper was exposed. `continuousDelta` follows by unfolding and `fun_prop`. The positive-scale cancellation branch of count-to-half-budget normalization is a newly proved experiment, not a prerequisite missing basic API. Its upstream value should be assessed with the count theorem. |

**MATHLIB-IDIOMATIC construction.** Do not extract extra arithmetic wrappers just to express this formula. The optional refactor is to choose the local/public cutoff boundary, rather than change its mathematical construction.

## Phase 5 — Full fifteen-cell mathlib search

Each of the three forms was searched by all five actual methods. Raw complete formal tool requests/results and exact untruncated source-search commands/results are linked below. Search service indexes may use different mathlib revisions. Positive relevant operations were checked against this pin in the isolated snippet; none of the unrelated search results is promoted to an equivalent definition.

| Form | Lean-Finder | Loogle | LeanSearch | rg pinned source | Local search |
|---|---|---|---|---|---|
| Current `ℝ→ℕ→ℕ→ℝ`, exact formula | [request/result](../evidence/Roth.lam/search-current-leanfinder.json): unrelated additive Roth/Chevalley bounds | [request/result](../evidence/Roth.lam/search-current-loogle.json): Akra–Bazzi/upcrossing/Hurwitz functions have similar type only | [request/result](../evidence/Roth.lam/search-current-leansearch.json): additive Roth and Besicovitch | [exact search](../evidence/Roth.lam/search-current-rg.json): no full-name/fixed-formula hit | [request/result](../evidence/Roth.lam/search-current-local_search.json): original project target plus irrelevant matches; index warming |
| Literature-standard auxiliary-polynomial/index cutoff | [request/result](../evidence/Roth.lam/search-standard-leanfinder.json): additive Roth false positives | [request/result](../evidence/Roth.lam/search-standard-loogle.json): no matches to exact sqrt/arithmetic pattern | [request/result](../evidence/Roth.lam/search-standard-leansearch.json): additive Roth, unrelated polynomial constructor | [exact search](../evidence/Roth.lam/search-standard-rg.json): surrounding Diophantine approximation and additive Roth, no verified cutoff | [request/result](../evidence/Roth.lam/search-standard-local_search.json): project Roth theorem and additive Roth APIs; index warming |
| Abstract scaled square root/affine real factor | [request/result](../evidence/Roth.lam/search-abstract-leanfinder.json): `Real.sqrt`, CFC sqrt, derivative facts | [request/result](../evidence/Roth.lam/search-abstract-loogle.json): `Real.sqrt_mul`, `Real.mul_self_sqrt`, Cauchy–Schwarz | [request/result](../evidence/Roth.lam/search-abstract-leansearch.json): real/NNReal square root, RCLike/CFC and polynomial scalar multiplication | [exact search](../evidence/Roth.lam/search-abstract-rg.json): current `Analysis/Real/Sqrt.lean` definition/properties | [request/result](../evidence/Roth.lam/search-abstract-local_search.json): sqrt multiplication facts; index warming |

**Conclusion:** genuine existing building blocks are `Real.sqrt`, real multiplication/addition and natural casts. `Real.sqrt_mul` is an equality about a product's square root, not a definition of `4(1+3δ)n√m`. `rothNumberNat` counts progression-free sets, `Dioph` represents polynomial equations, and CFC square roots concern functional calculus; they are not this arithmetic cutoff. No existing equivalent named parameter or strict ≤3-existing-call replacement has been verified. This is a bounded statement of actual findings, not a proof that no such definition can exist.

A compiled arbitrary term of type `ℝ→ℕ→ℕ→ℝ` would not test equivalence: many unrelated functions have that type. Instead, the native isolated experiment constructs the exact expression and verifies its specialization, reassociation, sign/dependence behavior and relevant generic normalization. It does not use project `Roth.lam` (guarded by `#check_failure`), and no new lemma is misrepresented as a library hit. [Pinned mathlib source hashes](../evidence/Roth.lam/mathlib-inputs.json).

## Phase 5.5 — Statement shape, all three checks

1. **Normal form:** current `4*(1+3δ)*n*√m`, expanded `(4+12δ)*n*√m`, and scale form `4*((1+3δ)*n)*√m` are equivalent. The two nontrivial reassociations/expansions are compiled with `ring`. The current grouping exposes the coefficient exponent factor used by the main lemma; preserve it locally. For a definition there is no ↔-orientation issue. No competing global simp expansion is proposed.
2. **Syntactic generality:** real degree/dimension expression and single-scale expression were actually tried. They are arithmetically useful but would hide the natural degree/dimension interface or its provenance if presented as the primary standalone object. Keep explicit δ,n,m arguments or use a local choice in the parent proof; do not force consumers to construct a new bundle.
3. **Superfluous arguments:** no hypotheses or typeclasses exist. Each input changes the function: isolated `deltaMatters`, `degreeMatters`, `dimensionMatters` give concrete counterexamples to deleting an argument. Zero cases do not make an input globally superfluous.

**SHIP-AS-STATED locally; public upstream grain pending.** There is no statement-shape-driven generalise-first conclusion.

## Phase 6.0 — Complete callers and inline audit

Both `rg --no-ignore` over production inventory and `git grep` over tracked sources were executed. They agree as sets. [Fresh lexical search](../evidence/Roth.lam/source-search.json), [tracked cross-check](../evidence/Roth.lam/tracked-source-search.json), [inventory](../evidence/Roth.lam/source-inventory.json), [full caller bodies/plans](../evidence/Roth.lam/callers.json).

| Actual caller | Executable reference | Verified inlining |
|---|---|---|
| `Roth.gam`, MainLemma63 | `lam δ n m` in `(m−λ)/2` | Expand to the exact arithmetic expression; `Roth.gam = Lam229Inline.gam` is `rfl`. |
| `Roth.eta_lt_gam_iff`, MainLemma100–102 | `grind [gam, lam]` | With gamma expanded, `grind [gam]` replays the full proof. Equality of the original/replayed theorem terms typechecks by definitional equality and proof irrelevance. |
| Private `Roth.exists_mem_RSet_le_index_of_log_bound_aux`, MainLemma618–641 | `simpa only [gam, lam]` at638 | `simpa only [gam]` replays the full auxiliary-polynomial proof with gamma expanded. Native `isDefEq` verifies its complete original private signature, resolving the old private name with its actual module. |
| `Roth.exists_delta`, Main227–250 | `simpa [gam, lam, eta, …]` at244 | Remove lam after expanding gamma; full Main replay succeeds and the original/replayed theorem terms have definitionally equal signatures. |

**Counts:** four executable occurrences in four declarations; three in the declaring file and one in one other file. Outside-declaring-file use count=1; no external project consumer is established. The module-docstring mention and own definition are not call sites. The many Lattice occurrences are local variable bindings, not this definition; the corrected metadata's historical broad `used_by_other_files` field is not used as the caller list.

Fresh exact canonical293 kernel audit finds only two direct **value** consumers, `Roth.gam` and `Roth.exists_delta`, and zero direct **type** consumers. Elaboration/normalization can erase explicit names, explaining why four source callers need not equal two kernel consumers. The declaration has no source simp attribute; explicit tactic lists use it as an unfolding instruction. Neither source text, direct kernel constants nor this simp observation is a full imported transitive dependency closure. Public MainLemma results use gamma transitively; no claim is made that imported proofs are target-free.

Inline re-derivation search found the more general private auxiliary helper's cutoff `(m−4*c*f.natDegree*√m)/2` around MainLemma585 and the generic scale/count normalization around560–575. This is a related shape with free c/a, not a literal bypass of a call to `lam`. All expanded-form matches are retained in the [inline audit](../evidence/Roth.lam/inline-audit.json).

The complete MainLemma and Main replay contains **no written `lam` reference**, while retaining the arithmetic spelling in gamma and verifying all four original signatures. This is an inlining experiment, not an assertion that the original imported proof dependency graph has no lam. [Exact full replay](../evidence/Roth.lam/inline-executed.lean.txt), [clean receipt](../evidence/Roth.lam/inline-receipt.json).

### Pairwise moral-duplication audit

| A | B | Same statement/object? | Same construction/proof? | Action |
|---|---|---|---|---|
| lam | private rpow-bound helper cutoff near585 | Selected scale versus arbitrary c, not identical declaration | λ is the special arithmetic scale of the general cutoff | Keep specialization local; consider admissible-cutoff boundary with the parent theorem. |
| lam | gam | No: λ versus `(m−λ)/2` | Gamma uses lambda; it does not duplicate it | No theorem/definition merger claim; inlining gamma's chosen lambda is verified. |
| lam | eta | No: linear-in-δ scaled √m versus fractional real power of δ | Distinct losses in the proof | Do not unify merely because both are named proof parameters. |
| lam | Lattice's bound variable lam | No: selected function versus free real input | Generic lattice estimate accepts many cutoffs | Preserve distinction; expose arbitrary cutoff if designing reusable counting API. |
| lam | `Real.sqrt` | No: one primitive versus the whole selected expression | Existing mathlib primitive is reused correctly | No duplicate sqrt implementation or missing basic sqrt API. |

## Phase 6 — Actual composition experiments

* **Existing operations:** exact mathlib-only construction compiles as `4*(1+3δ)*n*√m`, with existing `HMul.hMul`, `HAdd.hAdd`, `Nat.cast` and `Real.sqrt`. This is an ordinary expression, not a newly proved arithmetic theorem. Literal operation count is four multiplications + one addition + sqrt + two natural casts; counting only outer multiplications would hide the affine factor and square-root/cast work. No literal ≤3-existing-call term equivalent to the full definition was established.
* **Exact bridge to the scalar extension:** `Lam229Project.bridge` is `rfl`, but `realFormula` is a new scratch definition, not a mathlib counterpart. The single-scale bridge and expanded normal form require normalization (`ring`), so they must not be sold as an existing-call replacement.
* **Semantic scale experiment:** isolated `scaleCount` proves `a*D ≤ N/2` from the generic lattice-shaped inequality with denominator `4*a*√x`, assuming a>0 and x>0. It verifies only the positive-a cancellation branch, not the full lattice count; the existing project helper also handles a≤0 separately. It uses inequality scaling and denominator normalization; it is a new generic proof, not an existing named mathlib law. No N/D positivity premise is needed. The actual project has a generic real-a count helper already; that project helper is not a mathlib building block.
* **Actual callers:** all four and both complete modules replay with this definition inlined and original signatures retained. This shows local removability if desired; it does not establish a reusable independent upstream semantic object or the strict ≤3-existing-call condition.

**Composition verdict: NOT-COMPOSABLE in the required verified ≤3-existing-call sense; direct primitive expression and complete local inlining are verified.** No universal impossibility/absence assertion follows. There is no hidden parent `NO-mathlib-has-it` re-aim: lam has no project parent definition and no verified existing D′ whose laws would decide its status. Nothing here is an automatically accepted `simp [defs]` verdict.

## Phase 7 — Actionable verdict and future upstream questions

**BORDERLINE-needs-human.** The mathematical formula is real and exactly sourced; its constants serve the chosen coefficient/count budget, and four executable consumers supply a local semantic-name exemption. A full scalar extension and the generic cancellation relation compile. At the same time, exact literature sourcing and usefulness inside a Roth proof do not establish a reusable standalone mathlib concept; the relevant recent exposition uses a different cutoff and count method. Generic arithmetic primitives are already available, while neither an equivalent existing named cutoff nor a strict ≤3-existing-call replacement was verified. These facts support a question about the upstream API boundary, not a cost-based downgrade or a guess of generalise-first.

1. For an eventual upstream Roth main-lemma development, should this exact lambda remain a public documented parameter, or become a private/local abbreviation with gamma expanded?
2. Should the reusable upstream boundary expose an arbitrary admissible real cutoff (or coefficient scale a), with this exact lambda chosen only in the Roth application?

**Concrete next action:** retain the documented project definition during the read-only overview; do not open a standalone parameter-only PR. If choosing local/private inlining later, update gamma's body, drop lam from the two MainLemma normalization lists and the Main.exists_delta list exactly as in the verified full replay. No hypothesis or caller signature need change. If choosing a public cutoff API, design it together with the lattice count and auxiliary-polynomial theorem and keep the exact current choice as its application. An appropriate alternative destination is project-local `Roth/MainLemma.lean`; an upstream number-theory Roth module may keep it locally if the parent theorem is contributed. A separate global general scalar or semiring wrapper is not justified by these experiments.

No YES category is claimed, so exact upstream file/PR title/reviewer/recent-commit/grouping requirements are not applicable. No unrelated accepted YES declaration is treated as a reason to ship this parameter. All investigation is complete; the questions are future design decisions, not missing evidence.

## Phase 8 — Verification, reproducibility and completion

Four accepted native evidence sets are complete and clean: original MainLemma replay plus full type/body/axioms/canonical audit; isolated mathlib-only representation/count/guard experiments under the stable exact18 imports; complete inlined MainLemma/Main modules with all four original signatures verified; and actual-context bridges/normalization/continuity/universe probes. All successful accepted receipts have zero errors/warnings, no resource raises, no new axioms or admissions, and only `propext`, `Classical.choice`, `Quot.sound`. Raw isolated diagnostics do not have a disk `partial` field; every accepted disk result explicitly has `partial=false`, no timeout or failed dependencies. The initial cold original query was partial and is excluded; the malformed negative coercion experiment was compiler-successful but semantically rejected and is retained separately.

The canonical name array is derived directly from tracked declaration order, with the correct private modules. Its pre-execution source gate passed; source exact order, runtime293 unique names, presence and kernel values are all independently checked by the portable validator. The worker manifest covers exact executed `.lean.txt` sources, original tool requests/raw results/timings, searches, source snapshots, hashes, report and metadata. Current manifest validation remains authoritative after integration; root-only acceptance/review records and historical worker manifests are excluded from recursive coverage.

[Portable read-only validator](../evidence/Roth.lam/validate.py), [current manifest](../evidence/Roth.lam/copy-manifest.json), [assessment](../evidence/Roth.lam/assessment.json), [verification](../evidence/Roth.lam/verification.json), [preparation gates](../evidence/Roth.lam/preparation-checks.json). `completed=true`, all phases PASS, `unresolved=[]`, root acceptance pending.
