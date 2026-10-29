# Roth.roth_rat — canonical289

**Verdict: YES-but-generalise-first — LITERATURE-WEAKENING.** Keep the named rational-value endpoint with the Roth theorem contribution package, and remove its unnecessary `Irrational α` binder. This is an independently assessed mathematical endpoint, although its current proof is a short representation transfer. No production source or pin changed.

## Phase0 — Baseline and scope

The public theorem resolves at `Roth/Main.lean:581–586`. All588lines of Main and all66lines of LeanEval were read. There are no actual proof/type callers of this endpoint. The focused original replay copies the exact target only, renaming it into `Roth289Original.replay`, opening the original namespaces; no private helpers are needed. Unrelated Main declarations are imported, not redundantly re-elaborated.

Fresh17 source/pin hashes agree with the shared clean2467-job baseline. At this Main file boundary root additionally executed literal `lake build`: exit0,6833.895ms,0warnings,2026-10-29 21:14:57–21:15:04UTC. Its log hash is `b7f96a04d807f93a54c01314b6f59b969256b6222dffa7ae4b62832d3a174e65`. Final293 dualbuild gates belong to root separately.

Evidence: [inputs.json](../evidence/Roth.roth_rat/inputs.json), [baseline-build.txt](../evidence/Roth.roth_rat/baseline-build.txt), [file-end-build.json](../evidence/Roth.roth_rat/file-end-build.json), [file-end-lake-build.log](../evidence/Roth.roth_rat/file-end-lake-build.log), [source-Main.lean.txt](../evidence/Roth.roth_rat/source-Main.lean.txt), [source-LeanEval.lean.txt](../evidence/Roth.roth_rat/source-LeanEval.lean.txt).

## Phase1 — Comprehension

For a fixed irrational algebraic real α, if infinitely many distinct rational numbers x satisfy |α−x|<den(x)^(−κ), then κ≤2. The exponent is an arbitrary real, and `x.den` is the positive denominator of the canonical reduced fraction. Distinct rational values, rather than arbitrary integer/natural representations, are being counted.

The map x↦(x.num,x.den) is injective by `Rat.ext`. Its image of the infinite good rational set is therefore infinite. `Rat.den_pos` and `Rat.cast_def` put every image pair in `Roth.approxSet`; the actual `Roth.roth` then bounds κ. Those set/cast operations supply representation transport; they do not supply the algebraic exponent-two theorem.

Full fresh kernel type, obtained through `Lean.getConstInfo` and tagged `pp.funBinderTypes`:

```lean
∀ {α : ℝ},
  Irrational α → IsAlgebraic ℚ α → ∀ {κ : ℝ}, {x : ℚ | |α - ↑x| < 1 / ↑x.den ^ κ}.Infinite → κ ≤ 2
```

The loaded kernel body directly mentions `Roth.roth` and `Roth.approxSet`; only `Roth.roth` is lexically explicit in the written target. No project constant occurs in the type. Transitive parent proof dependencies are not conflated with direct references. The original kernel printer elides18826characters; this is **not** a complete body dump. The exact complete written proof, full kernel type, complete used-constant lists, standard axioms and complete canonical value audit remain available. The proof equality check confirms exact original/replay type agreement by proof irrelevance, not construction identity.

Evidence: [original-executed.lean.txt](../evidence/Roth.roth_rat/original-executed.lean.txt), [original-receipt.json](../evidence/Roth.roth_rat/original-receipt.json), [native-type.json](../evidence/Roth.roth_rat/native-type.json), [project-dependencies.json](../evidence/Roth.roth_rat/project-dependencies.json), [canonical-consumers.json](../evidence/Roth.roth_rat/canonical-consumers.json).

## Phase2 — Preliminary checks

**BIG:** a named Roth theorem and explicitly listed Main result. Its five proof lines do not make the endpoint mathematically small. One-line definition test: n/a, this is a theorem. Definition barrier/diamond/API exemptions: n/a. No prefilter or parent verdict was inherited.

## Phase3 — Exhaustive literature

All named channels were actually checked, including three distinct general queries and a separate nCatLab namespace query. Optional `ask_chatgpt_math` is unavailable. Local `clean.tex` §6 states the unreduced-pair theorem with irrationality; §7 proves it. The all-algebraic rational-value formulation appears directly in Fukshansky, *Geometric Number Theory*, Theorem4.5.1, printed p67 / physical PDF page71 (zero-based70), lines5063–5095: only finitely many reduced rationals at exponent2+δ. This is the relevant standard generality.

| Channel | Actual query | Finding |
|---|---|---|
| web-specific | Roth theorem finitely many rational approximations algebraic real exponent 2 epsilon reduced denominator | Standard finite reduced-rational Roth theorem; Fukshansky Theorem4.5.1 includes every real algebraic target; number-field/Subspace extensions do not imply a mechanical widening. |
| web-general | Roth theorem rational algebraic numbers irrationality hypothesis finite rational set | Standard finite reduced-rational Roth theorem; Fukshansky Theorem4.5.1 includes every real algebraic target; number-field/Subspace extensions do not imply a mechanical widening. |
| web-alias | Thue Siegel Roth irrationality exponent number fields Schmidt subspace theorem | Standard finite reduced-rational Roth theorem; Fukshansky Theorem4.5.1 includes every real algebraic target; number-field/Subspace extensions do not imply a mechanical widening. |
| nlab | site:ncatlab.org/nlab Roth theorem Diophantine approximation | Vojta conjecture and number theory connections returned. Opening relevant Vojta page failed400 unsupported XHTML; no exact endpoint proof claimed. |
| ncatlab | site:ncatlab.org/ncatlab "Roth" "approximation" | Distinct namespace checked; dedicated query returned empty. Earlier batch returned out-of-namespace nLab hits. No categorical Roth restatement located; not absence proof. |
| stacks | site:stacks.math.columbia.edu Roth Diophantine approximation algebraic number | Dedicated query empty; Stacks targets algebraic geometry infrastructure, not a verified source of this real rational approximation theorem. |
| mathoverflow | site:mathoverflow.net Roth theorem rational approximation irrationality exponent | Questions on approximation exponents, counts, continued fractions and uniform lower bounds distinguish ineffective finiteness from effective computation. |
| arxiv | site:arxiv.org Roth theorem rational approximation after:2021-10-29 before:2026-10-30 | 2022 Hindes paper explicitly warns characteristic-p Roth fails; 2026 weighted projective line paper studies height-dependent exponents and a conjectural strengthening, not a safe generic widening. |
| Local references | clean.tex §6/§7 | Read original manuscript reduction and proof, archived excerpts. |
| Optional ChatGPT | standard form/generality/history query unavailable | ask_chatgpt_math tool absent; documented skip. |

The nLab open failed with400 unsupported XHTML; the dedicated Stacks/nCatLab queries returned empty. These are access/search outcomes, not proof of absence. The publisher request for Roth1955 redirected from PDF to HTML; no complete original-paper proof was accessed there. The primary lecture theorem and local manuscript supply the statement evidence. Recent arXiv results were inspected at their dated abstracts: Hindes(19Sep2022) explicitly cautions that characteristic-p Roth fails; Salami(13Oct2026) studies weighted heights and distinguishes a proved pullback exponent from a conjectural coprime refinement. Neither licenses blindly changing this real/rational theorem's field or denominator.

Primary citations: [Fukshansky, Theorem4.5.1](https://www1.cmc.edu/pages/faculty/lenny/classes/spring_2019/m195/GNT_lecture-notes.pdf), [Roth1955 publisher record](https://www.cambridge.org/core/journals/mathematika/article/abs/rational-approximations-to-algebraic-numbers/9B22B10EFDE4FFC405FCAAFB12C67D3C), [Hindes2022 abstract](https://arxiv.org/abs/2209.09182), [Salami2026 abstract](https://arxiv.org/abs/2610.17589).

Evidence: [literature.json](../evidence/Roth.roth_rat/literature.json), [literature-local.json](../evidence/Roth.roth_rat/literature-local.json), [web-batch0.json](../evidence/Roth.roth_rat/web-batch0.json), [web-batch1.json](../evidence/Roth.roth_rat/web-batch1.json), [web-batch2.json](../evidence/Roth.roth_rat/web-batch2.json), [web-batch3.json](../evidence/Roth.roth_rat/web-batch3.json), [web-batch4.json](../evidence/Roth.roth_rat/web-batch4.json). Exact web requests, returned SHA256/byte lengths/status and clean title/URL metadata are archived; no third-party article/search-result bodies are persisted. Out-of-scope/truncated returned URLs were omitted, query strings stripped. Search-engine crawl dates were not treated as publication dates.

## Phase4a–b — Generality

| Parameter | Disposition | Evidence |
|---|---|---|
| α : ℝ | Retain | A real target with real absolute value/rpow; literature number-field/place variants are not a mechanical class edit. |
| Irrational α | DROP verified | general02 infers it from infinite good rational values when κ≥2 using the existing pinned exponent2 iff; κ≤2 is otherwise immediate. This permits rational algebraic targets. |
| IsAlgebraic ℚ α | Retain semantic hypothesis | It supplies the actual Roth theorem, not the set conversion. Liouville reals show no corresponding assertion for all real numbers; no drop claimed. |
| κ : ℝ | Retain arbitrary real exponent | No positivity binder needs adding. Contradiction assumes κ>2. |
| Infinite rational values | Retain or finite/cofinite equivalent | Canonical rational values avoid infinite repeated representations of one fraction. Exact equivalences compiled in shape02/modern01. |
| Reduced denominator x.den | Retain meaning | Rat.den_pos and num/den injectivity supply the pair map. Denominator zero is impossible and does not need an extra argument. |
| Coefficient 1 | Concrete scope assessed | edges01 verifies extension to any real C≤1. For C>1 an exponent-gap argument and finite bounded-denominator rational set bridge would be needed; not claimed compiled and not the proposed generalization. LiouvilleWith offers a separately assessed existential-C formulation. |
| Threshold 2 | Retain sharp semantic constant | edges01.sharp verifies infinite exponent2 approximants for irrational reals via Dirichlet. Making the threshold an arbitrary parameter would replace Roth mathematics by an assumed bound. |

**STRICTLY NARROWER THAN STANDARD: one verified hypothesis drop.** The proposed endpoint is:

```lean
theorem roth_rat {α : ℝ} (halg : IsAlgebraic ℚ α) {κ : ℝ}
    (hinf : {x : ℚ | |α - x| < 1 / (x.den : ℝ) ^ κ}.Infinite) : κ ≤ 2
```

For κ>2, denominator≥1 and real-exponent monotonicity enlarge the good set into the exponent2 good set. The pinned `Real.infinite_rat_abs_sub_lt_one_div_den_sq_iff_irrational` then infers irrationality of α, permitting the exact original Roth endpoint to finish. This uses existing rational-center finiteness through that iff; it does not re-prove integer separation. At κ≤2 the conclusion is immediate. Rational algebraic targets are thus admitted without changing approximation semantics.

The mathlib-only `generalize` proof is explicitly conditional on `hR`, whose type is exactly the original all-target endpoint schema. The actual original hR is re-elaborated and type-agreed separately in the project context. This is a compiled implication from the verified original theorem, not a claim that isolated mathlib already proves Roth. `recover` restores the original signature. The rational-center edge additionally proves finiteness for every κ≥2. No proposed field/typeclass widening or C>1 strengthening is claimed verified.

Evidence: [general2-executed.lean.txt](../evidence/Roth.roth_rat/general2-executed.lean.txt), [general02-receipt.json](../evidence/Roth.roth_rat/general02-receipt.json), [edges-executed.lean.txt](../evidence/Roth.roth_rat/edges-executed.lean.txt), [edges01-receipt.json](../evidence/Roth.roth_rat/edges01-receipt.json).

## Phase4c — Modern mathlib idiom

| Question | Applies | Concrete result |
|---|---|---|
| Typeclasses | No | Irrational/algebraic are point properties. No missing algebraic-structure instance is being simulated. |
| Filters | Yes | Cofinite on rational values is exactly the finite-exception lower bound. exponent_iff_cofinite and recovery compile; Eventually.and combines exponent bounds. No uniform strict C claim. |
| Universal properties | No | The conclusion is an exponent inequality, with no object constructed to characterize. |
| Bundled substructures | No | Good approximants are not closed under addition or multiplication. A Subring/Submodule would change meaning. |
| Hierarchy weakening | No verified widening | Rational canonical denominators and the real absolute value/rpow are part of the statement. Ordered-field abstraction would require rebuilding parent arithmetic, not dropping an unused class. |
| Higher categories | No | There is no categorical construction or categorical hypothesis. |
| Concrete indices | No | Rationals and reduced positive natural denominators represent actual approximants. Arbitrary monoids/groups would lose the number-theoretic content. Number-field heights are a different theorem. |
| Concrete-via-abstract diagnostic | No new semantic abstraction | No fixed named target occurs: α is already arbitrary. Body uses roth once and num/den throughout; no first unfolding leaves a particular witness behind. The generic rational_to_pairs proof compiles without algebraicity, but supplying the full pair Roth theorem is the substantive premise. Replacing 2 by a bound parameter only abstracts bookkeeping. |
| False-generalization guard | PASS | Dropping hα for rational values is verified, using irrationality inferred at κ≥2. It is false for unreduced pairs: zero_pairs_infinite verifies the counterexample. Cofinite non-strict bound is not LeanEval strict uniform positive-C; LiouvilleWith excludes equality and is not asserted equivalent here. |

The finite bad-set endpoint is the natural arithmetic statement. Its exact cofinite reformulation supplies a non-strict lower bound outside finitely many **rational values**. The compiled `cofinite_consequence` combines two such exponent bounds by `Filter.Eventually.and`; recovery produces the original exponent implication. These are useful equivalent interfaces, not a stronger asymptotic result. The two-line `simp only [eventually_cofinite, not_le]` proves only the logical bridge, and would be a trivial simp composition if assessed on its own.

The current `LiouvilleWith` source was also read and searched: its existential constant, frequently-atTop denominators, exclusion of equality, exponent monotonicity, positive-witness normalization, exponent-gap and rational affine invariance are relevant to a larger coherent package. No new LiouvilleWith import was authorized or executed here, and no rational-value/LiouvilleWith equivalence is claimed. The existing Liouville polynomial-degree lower bound is weaker than Roth's universal exponent2 bound. LeanEval's strict uniform positive-C lower bound additionally requires irrationality and is not the cofinite statement.

Evidence: [modern-executed.lean.txt](../evidence/Roth.roth_rat/modern-executed.lean.txt), [modern01-receipt.json](../evidence/Roth.roth_rat/modern01-receipt.json), [mathlib-source-0.lean.txt](../evidence/Roth.roth_rat/mathlib-source-0.lean.txt).

## Phase4.5 — Infrastructure risks

| Risk | Status | Reason |
|---|---|---|
| diamond | n/a | Theorem introduces no definitional equality, instance, coercion or typeclass search path; no infrastructure probe is applicable. |
| reducibility | n/a | Theorem introduces no definitional equality, instance, coercion or typeclass search path; no infrastructure probe is applicable. |
| unfolding | n/a | Theorem introduces no definitional equality, instance, coercion or typeclass search path; no infrastructure probe is applicable. |
| priority | n/a | Theorem introduces no definitional equality, instance, coercion or typeclass search path; no infrastructure probe is applicable. |
| universe | n/a | Theorem introduces no definitional equality, instance, coercion or typeclass search path; no infrastructure probe is applicable. |
| coercion | n/a | Theorem introduces no definitional equality, instance, coercion or typeclass search path; no infrastructure probe is applicable. |

Overall n/a: theorem, no definition/class/instance. No new coercion or instance was proposed.

## Phase4.6 — Proof strategy

| Question | Applies | Alternative |
|---|---|---|
| Topology εδ | No | No neighborhood argument occurs in the endpoint proof. |
| Algebra elements/subobjects | No | Injecting canonical rational representations is the relevant operation; no ideal/submodule inclusion replaces it. |
| Sequences/filters | Yes for API | Use cofinite rational lower bounds for composition; the existing finite-exception proof is already set-theoretic, not an inefficient sequence argument. |
| Category universal property | No | No categorical object is constructed. |
| Missing helpers | Yes substantive endpoint | Mathlib has Rat.ext/Rat.cast_def/Infinite.image/mono, rational-center finite bounds, and cofinite conversion. It lacks the algebraic irrational exponent-two theorem. Upstream it coherently with its proof dependencies, not as a project theorem disguised as an existing mathlib call. |

**REFACTOR-RECOMMENDED for the public statement:** retain the canonical rational injection, infer irrationality only in the κ>2 branch, and offer finite/cofinite interfaces. No new abstraction should hide the actual Roth theorem behind a supplied desired conclusion. The original proof is mathematically sound; the issue is its unnecessary binder, not its shortness.

## Phase5 — Fifteen formal search cells

Current = original rational Infinite implication; standard = finite rational values for all algebraic targets; abstract = cofinite rational lower bound. All five methods were executed on each form. Remote snapshots can differ from the pin; every positive candidate used in proofs was checked against pinned source and natively checked.

| Form | Finder | Loogle | LeanSearch | rg | local |
|---|---|---|---|---|---|
| current | [formal-current-leanfinder.json](../evidence/Roth.roth_rat/formal-current-leanfinder.json) | [formal-current-loogle.json](../evidence/Roth.roth_rat/formal-current-loogle.json) | [formal-current-leansearch.json](../evidence/Roth.roth_rat/formal-current-leansearch.json) | [formal-current-rg.json](../evidence/Roth.roth_rat/formal-current-rg.json) | [formal-current-local.json](../evidence/Roth.roth_rat/formal-current-local.json) |
| standard | [formal-standard-leanfinder.json](../evidence/Roth.roth_rat/formal-standard-leanfinder.json) | [formal-standard-loogle.json](../evidence/Roth.roth_rat/formal-standard-loogle.json) | [formal-standard-leansearch.json](../evidence/Roth.roth_rat/formal-standard-leansearch.json) | [formal-standard-rg.json](../evidence/Roth.roth_rat/formal-standard-rg.json) | [formal-standard-local.json](../evidence/Roth.roth_rat/formal-standard-local.json) |
| abstract | [formal-abstract-leanfinder.json](../evidence/Roth.roth_rat/formal-abstract-leanfinder.json) | [formal-abstract-loogle.json](../evidence/Roth.roth_rat/formal-abstract-loogle.json) | [formal-abstract-leansearch.json](../evidence/Roth.roth_rat/formal-abstract-leansearch.json) | [formal-abstract-rg.json](../evidence/Roth.roth_rat/formal-abstract-rg.json) | [formal-abstract-local.json](../evidence/Roth.roth_rat/formal-abstract-local.json) |

The current and standard local queries returned one result each with `index=error`; cofinite returned seven with `index=error`. The earlier Liouville local query returned forty with `index=warming` and is retained as supplementary evidence. None supports a negative index inference. Finder/Search found Dirichlet, rational-center finite bounds, Liouville APIs and metric results, not a verified algebraic Roth bound. Loogle current and supplementary Liouville patterns were empty; standard found the rational-center theorem, abstract found cofinite generic bridges. Full-name source search was untruncated across all Mathlib; thematic rg covered NumberTheory plus the filter form.

Pinned relevant candidates:

- `Rat.finite_rat_abs_sub_lt_one_div_den_sq`, DiophantineApproximation/Basic:253: rational target, exponent2, inequality in ℚ. It is not Roth for algebraic irrational reals.
- `Real.infinite_rat_abs_sub_lt_one_div_den_sq_iff_irrational`, same:277: real-target characterization, used to infer irrationality above exponent2 by set inclusion.
- `Real.infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational`, same:197: Dirichlet sharpness at exponent2, opposite direction to finiteness above2.
- `Filter.eventually_cofinite`, Order/Filter/Cofinite:49: finite-exception transport, no arithmetic lower bound.
- `Liouville.exists_pos_real_of_irrational_root`, Transcendental/Liouville/Basic: polynomial-degree lower bound, not exponent2 independent of degree.

Evidence: [formal-search-matrix.json](../evidence/Roth.roth_rat/formal-search-matrix.json), [full-name-search.json](../evidence/Roth.roth_rat/full-name-search.json), [mathlib-inputs.json](../evidence/Roth.roth_rat/mathlib-inputs.json).

## Phase5.5 — Statement shape

| Check | Verdict | Evidence |
|---|---|---|
| Normal form | RESTATE-BEFORE-SHIP | All-algebraic finite rational bad-set for κ>2 is literature standard. Cofinite ≥ lower bound is an exact equivalent RHS normal form via Filter.eventually_cofinite; not a new fundamental approximation predicate. |
| Syntactic generality | Verified alternatives | Infinite-implies-bound, finite-above2 and cofinite-lower-bound tested both directions; original signature recovered. Prefer finite endpoint for library use and cofinite consequences using Eventually.and. |
| Superfluous arguments | One to drop | hα is used by the original proof but semantically unnecessary for distinct rational values. halg remains needed; α,κ and hinf specify the theorem. No hidden typeclass/universe binders. |

The main arithmetic assertion must still be supplied; generic finite/infinite/cofinite equivalences are not replacements for it. The finite/cofinite RHS convention agrees with the existing filter API. Original type agreement and original-signature recovery are executed, not inferred from textual similarity.

## Phase6.0 — All callers and inline audit

| Scope | Count | Evidence and disposition |
|---|---|---|
| Explicit proof callers, same/other files |0| Fresh no-ignore rg plus tracked git grep; only declaration and module-doc mention occur. |
| Explicit type callers |0| Full source inventory/canonical metadata cross-check. |
| Direct canonical kernel value/type consumers |0/0| Fresh exact ordered293 names,293unique,293present,293values; no consumer marker emitted. |
| Inline re-derivations bypassing this endpoint |0| Main pair/integral theorems and LeanEval bound have distinct domains/statements; full Main/LeanEval read. |

No actual caller exists to inline; caller-body verification is therefore justified n/a. A separate fresh `inline_endpoint` reconstructs the original endpoint from the exact canonical-map proof and actual `Roth.roth`, retains the original full signature and passes type equality; its loaded opaque value is target-free. This is a construction audit, not an invented downstream caller. There is no claim about arbitrary external consumers, simp closure or full transitive dependency traversal.

Zero internal uses do **not** establish deadness: `roth_rat` is expressly documented as a user-facing Main result, giving downstream users native rational values and canonical reduced denominators. Keep that endpoint in the coherent contribution package.

Evidence: [callers.json](../evidence/Roth.roth_rat/callers.json), [source-search.json](../evidence/Roth.roth_rat/source-search.json), [tracked-source-search.json](../evidence/Roth.roth_rat/tracked-source-search.json), [inline-search.json](../evidence/Roth.roth_rat/inline-search.json), [shape2-executed.lean.txt](../evidence/Roth.roth_rat/shape2-executed.lean.txt), [shape02-receipt.json](../evidence/Roth.roth_rat/shape02-receipt.json).

## Phase6 — Composition and duplication

Attempt1 uses `Set.Infinite.image`, injectivity from `Rat.ext`, `Set.Infinite.mono`, positivity and `Rat.cast_def`. This transports the premise to pairs, but cannot prove κ≤2 without `Roth.roth`. The latter is a project theorem, not an existing mathlib building block. Thus the five-line source proof is not a ≤3-existing-mathlib-call proof of the endpoint.

Attempt2 uses the pinned rational-center finite theorem/real iff: it infers irrationality, but still cannot bound algebraic irrational approximation exponents. Attempt3 uses existing Liouville lower-bound API: its degree-dependent exponent cannot specialize to universal2. In the isolated accepted general02 source, both `exact?` and `aesop` were required to fail on the actual original arithmetic goal; no resource limits were raised. These unsuccessful routes do not prove universal library absence, but prevent treating the located generic candidates as a verified replacement.

**NOT-COMPOSABLE from current mathlib.** The cofinite logical bridge itself composes by simp; that fact does not downgrade the missing Roth endpoint.

| Decl A | Decl B | Same statement? | Same proof? | Action |
|---|---|---|---|---|
| roth_rat | Roth.roth |No: rational values vs unreduced pairs|Canonical injection plus actual parent theorem|Group as theorem and rational-value corollary; pair hα remains.|
| roth_rat | Roth.roth_of_isIntegral |No: algebraic target vs integral/pairs|Additional reduction plus representation transport|Keep related endpoint corollaries in one staged package.|
| roth_rat | LeanEval.thueSiegelRoth |No: exponent implication vs strict uniform positive-C lower bound|Finite minimum/exponent-gap bridge needed|Do not conflate cofinite rational bound with uniform pair bound.|
| rational-center finite | Rat finite exponent2 |Yes up to casts/exponent monotonicity|Existing mathlib supplies it|Reuse pinned iff; no independent new separation theorem needed.|

## Phase7 — Actionable verdict

**YES-but-generalise-first**, reason **LITERATURE-WEAKENING**: drop `Irrational α`, retaining an original-signature corollary. This is a real compiled binder weakening, not a wholesale foundation change or cost-based choice. Modern finite/cofinite spellings improve application but are not the justification for claiming new arithmetic content.

**Why add this endpoint:** mathlib's DiophantineApproximation/Basic already exposes good rational approximation sets and Dirichlet exponent2 infinitude; its rational-center finite theorem closes the easy branch. Its LiouvilleWith module explicitly describes exponent>2 algebraic exclusion as the Thue–Siegel–Roth theorem. The concrete missing bridge is the algebraic irrational exponent-two bound, proved by this project's parent theorem. Users working with `ℚ` should be able to obtain finiteness at exponent>2 without manually constructing integer pairs or unnecessarily proving irrationality. The named rational endpoint belongs with that mathematical contribution, not in an isolated PR selling its cast conversion as new mathematics.

Proposed exact home: `Mathlib/NumberTheory/DiophantineApproximation/Roth.lean`, as a new leaf above the existing Basic and staged Roth proof modules. Proposed PR title: **feat(NumberTheory/DiophantineApproximation): Roth bounds for algebraic real rational approximations**. Namespace/naming can follow the surrounding `Real` endpoint conventions.

Grouping was checked against the current accepted progress snapshot: `Roth.roth` and `Roth.roth_of_isIntegral` are accepted YES-but-generalise-first, and `Roth.main_lemma` accepted YES-add-as-is. Their underlying proof/API work should be staged coherently; this endpoint is a corollary in the culminating theorem PR. `Roth.reduction` is accepted BORDERLINE, so it is not falsely advertised as an independently accepted YES companion. No earlier verdict was inherited here.

Pre-PR actions: `/generalise Roth.roth_rat` to remove hα using the verified branch; `/cleanup Roth/Main.lean Roth.roth_rat` before migration; preserve original recovery and finite/cofinite interfaces. For recent relevant reviewer evidence, pinned git history records Yaël Dillies' rational coercion change483ba09b(16Jun2026), Andrew Hendel's DiophantineApproximation reference correction834e5169(12May2026), and Marcelo Lynch's direct-file cleanupf01aa345(11Aug2026). Ask a number-theory reviewer such as original DiophantineApproximation author Michael Stoll for mathematical placement, with Yaël Dillies suitable for the rational-cast/API review; authorship and recent commit evidence are distinguished, not treated as proof of availability.

No production deletion/refactor was performed. The endpoint stays locally in Main until its parent theorem contribution is migrated. No user checkpoint or future upstream taste question is needed to complete this read-only assessment.

## Phase8 — Evidence integrity and completion gate

Root owns every native/LSP/build execution; the worker prepared immutable source/hash/request files and inspected raw returned receipts. Disk9 and fixed18 prefixes are byte-preserved; the only authorized extra isolated import is genuine pinned DiophantineApproximation.Basic, giving19imports and hash`9b1bd511ef007f620a7163c38b76aaf650486373cce45b2a4b108b5c1d83583e`.

| Accepted source | Raw receipt | ms | Scope |
|---|---|---|---|
| [original-executed.lean.txt](../evidence/Roth.roth_rat/original-executed.lean.txt) | [original-receipt.json](../evidence/Roth.roth_rat/original-receipt.json) | 2649 | original |
| [general2-executed.lean.txt](../evidence/Roth.roth_rat/general2-executed.lean.txt) | [general02-receipt.json](../evidence/Roth.roth_rat/general02-receipt.json) | 2808 | generality |
| [shape2-executed.lean.txt](../evidence/Roth.roth_rat/shape2-executed.lean.txt) | [shape02-receipt.json](../evidence/Roth.roth_rat/shape02-receipt.json) | 1333 | shape-inline |
| [modern-executed.lean.txt](../evidence/Roth.roth_rat/modern-executed.lean.txt) | [modern01-receipt.json](../evidence/Roth.roth_rat/modern01-receipt.json) | 301 | modern |
| [edges-executed.lean.txt](../evidence/Roth.roth_rat/edges-executed.lean.txt) | [edges01-receipt.json](../evidence/Roth.roth_rat/edges01-receipt.json) | 1930 | edges |

General01 is rejected for a set-membership elaboration error and recovered sorryAx. Shape01 is rejected despite success=true: an informational PANIC from `ConstantInfo.value!` invalidated its target-free audit. Shape02 explicitly uses `value? (allowOpaque := true)` with a missing-value failure and succeeds without PANIC. Rejected exact source/raw receipts remain immutable. Standard axioms only: propext, Classical.choice, Quot.sound. No sorry, new axiom, unsafe/native_decide, partial accepted result or raised resource limit.

Syntax credit: accepted287 shape2's finite/infinite duality proof and zero-pair construction were adapted with fresh rational-domain mathematics and fresh execution; rejected old archives were not templates. General02 supplies the genuinely new compiled hypothesis-drop implication; existing pinned rational-center/Dirichlet/filter APIs remain separately identified.

Current copy-manifest validates every artifact hash/byte size in scratch and simulated integrated layouts, including report links and exact293 source order/private modules. The completion gate holds completed=false/phase8pending until actual draft validators and secret guard PASS; completion is then set true and final current-manifest/layout checks run again. Historical worker manifests never replace the current manifest. Root acceptance stays pending until independent review. Exact executed sources, raw receipts, copied prefixes and copied source excerpts are preserved; only authored preparation/report text is normalized.

Evidence: [verification.json](../evidence/Roth.roth_rat/verification.json), [phase-checks.json](../evidence/Roth.roth_rat/phase-checks.json), [prefix-controls.json](../evidence/Roth.roth_rat/prefix-controls.json), [prefix-authorization.json](../evidence/Roth.roth_rat/prefix-authorization.json), [reviewer-specific-commits.json](../evidence/Roth.roth_rat/reviewer-specific-commits.json), [progress-snapshot.json](../evidence/Roth.roth_rat/progress-snapshot.json), [validate.py](../evidence/Roth.roth_rat/validate.py).
