# MvPolynomial.taylor_taylor — full mathlibable assessment

Verdict: **BORDERLINE-needs-human**, independently assessed. Canonical declaration 65, `Roth/Taylor.lean:146`. This is the Phase 6b “trivial simp composition; user decides if worth a lemma” case. It is neither an inherited verdict nor a cost-based downgrade. The theorem is live through the negative-translation inverse. All requested verification is complete; the remaining questions concern upstream API design.

## Phase 0 — Baseline and scope

The shared clean `lake build` completed successfully (2467 jobs, exit 0). All 17 production-source and pin hashes were freshly checked against that build's input manifest and match. The complete declaring module and the relevant downstream `Roth/Index.lean` module were read. No production, pin, Git, progress or overview files were changed by this assessment.

Evidence: [baseline](../evidence/MvPolynomial.taylor_taylor/baseline-build.txt), [input manifest](../evidence/MvPolynomial.taylor_taylor/inputs.json), [fresh check](../evidence/MvPolynomial.taylor_taylor/input-hash-check.json), [Taylor module](../evidence/MvPolynomial.taylor_taylor/Taylor-module.lean.txt), [Index module](../evidence/MvPolynomial.taylor_taylor/Index-module.lean.txt). The original theorem and independent replay are completely elaborated with standard axioms `[propext, Classical.choice, Quot.sound]`: [native target receipt](../evidence/MvPolynomial.taylor_taylor/native-target-success.json), [exact executed source](../evidence/MvPolynomial.taylor_taylor/native-target-executed.lean.txt). No sorry, unsafe proof, raised limits, partial success or pending diagnostics are accepted.

## Phase 1 — Mathematical content and full type

For a polynomial in any set of variables over a commutative semiring, translating its variables by β and then translating by α gives the same formal polynomial as translating once by α+β. Translation fixes coefficients and sends each variable Xⱼ to Xⱼ+C(αⱼ). This is algebraic substitution, without analytic convergence, degree bounds or characteristic restrictions.

```lean
∀ {σ : Type u_1} {R : Type u_2} [CommSemiring R]
  (α β : σ → R) (P : MvPolynomial σ R),
  taylor α (taylor β P) = taylor (fun j ↦ α j + β j) P
```

The native full type is in the target receipt. `σ` indexes variables, `R` supplies coefficients, α and β are translation vectors, and P is arbitrary input. The proof unfolds `taylor`, composes evaluation homomorphisms, and computes the image of each translated generator. Its generic substitution step is followed by genuine equality normalization, not definitional reduction alone.

## Phase 2 — Preliminary checks

SMALL: an elementary compatibility law, not a definition, named main theorem or new structure. The one-line-definition test is **n/a, theorem**. Its one-line `simp` proof remains relevant in Phase 6b; it is not a definition-only rejection and is not a literal rfl glue lemma.

## Phase 3 — Exhaustive literature

All named channels were actually attempted. The command calls this a nine-channel protocol while its table enumerates three general web forms plus named specialist sources; no invented channel was added to fix that count. Receipts retain exact requests, response SHA256/bytes/status, original summaries and sanitized URL locators, never full search-result or article bodies.

| Channel | Actual request / result | Assessment |
|---|---|---|
| General web, current form | `multivariate polynomial translation composition P(X+a+b) Taylor shift` | Taylor shift terminology and substitution composition. |
| General web, general form | `polynomial substitution homomorphism composition universal property arbitrary variables` | Substitution principle and free-algebra description. |
| General web, alias/structural form | `Taylor shift additive group action polynomial ring` | Translation action formulation; group assumptions belong to inverses, not the semiring composition law. |
| AskChatGPT | n/a: `ask_chatgpt_math` unavailable | Optional channel unavailable; other channels retained. |
| Local clean.tex | §§4 Taylor expansion, lines 503–527; implementation note 547–554; translated terms 600–607 | Defines Pα(X)=P(X+α), with real coefficients and finite p for Roth's application. Composition is implicit substitution, not a separately stated theorem. |
| nLab | `site:ncatlab.org/nlab polynomial ring universal property additive group action` | Polynomial page gives free commutative algebra on an arbitrary set; composition follows by uniqueness (our inference). |
| nCatLab | `site:ncatlab.org/ncatlab polynomial substitution action`, then exact polynomial/substitution retry | Returned nLab substitution material, not a separate nCatLab law. Syntactic substitution does not generally commute for variable-dependent substitutions. |
| Stacks | `site:stacks.math.columbia.edu additive group action affine space polynomials translation` | Tag 088V uses affine-line translation group action; quotient geometry is beyond this elementary identity. |
| MathOverflow | `site:mathoverflow.net polynomial translation additive group action` | Question 464098 discusses conjugacy of general additive actions to translations, a different stronger problem. |
| arXiv, last five years | Initial 2022–2026 multivariate Taylor-shift query was noisy; exact `shift equivalence` + `polynomials` + 2022 retry | Chen–Du–Fang arXiv:2204.06968 (2022; latest 2025v3), and Bläser et al. arXiv:2610.27168 (October 2026), use constant multivariate shifts and shift-equivalence groups. |
| Primary source opens | FLINT composition docs; arXiv2204.06968; nLab polynomial | FLINT defines Taylor shifts f(x+c); arXiv latest title is *Symbolic Summation of Multivariate Rational Functions*. nLab direct open failed unsupported `application/xhtml+xml`; cached search content was available. |

Evidence: [general web](../evidence/MvPolynomial.taylor_taylor/web-0.json), [nLab](../evidence/MvPolynomial.taylor_taylor/web-N.json), [nCatLab](../evidence/MvPolynomial.taylor_taylor/web-C.json), [Stacks](../evidence/MvPolynomial.taylor_taylor/web-S.json), [MathOverflow](../evidence/MvPolynomial.taylor_taylor/web-O.json), [initial arXiv](../evidence/MvPolynomial.taylor_taylor/web-A.json), [exact retries](../evidence/MvPolynomial.taylor_taylor/web-retry.json), [primary opens and access failure](../evidence/MvPolynomial.taylor_taylor/web-P.json), [local literature](../evidence/MvPolynomial.taylor_taylor/local-literature.json).

Primary locators: [Chen–Du–Fang](https://arxiv.org/abs/2204.06968), [Bläser et al.](https://arxiv.org/abs/2610.27168), [Stacks 088V](https://stacks.math.columbia.edu/tag/088V), [nLab polynomial](https://ncatlab.org/nlab/show/polynomial). Root directly verified the 2026 paper's submission date as **19 October 2026**, inside the required window: [primary date check](../evidence/MvPolynomial.taylor_taylor/web-root-arxiv-date.json). FLINT's current docs disclose that some sections were LLM generated; their terminology is only supplementary, independently corroborated by the papers and Lean source. MathOverflow supplies a research-context observation, not a theorem relied on in the proof.

Literature summary: this is additive composition of Taylor shifts / constant translations. Abstractly, polynomial substitution is functorial for maps out of a free commutative algebra. Computational sources often restrict to finite variables, fields or characteristic zero for their algorithms; those restrictions are not required by this identity. Arbitrary-variable commutative-semiring generality already covers the relevant algebraic law. The shift parameter is constant in the polynomial variables; replacing it by arbitrary polynomial-valued substitutions changes the additive law.

## Phase 4 — Parameters and generality

| Parameter / hypothesis | Role and comparison | Result |
|---|---|---|
| `σ : Type u_1` | Arbitrary variable set; no finite or decidability assumption | Already maximally general for current representation. |
| `R : Type u_2` | Independent coefficient universe | No universe collapse in native type. |
| `[CommSemiring R]` | Needed by fixed `taylor`, `aeval`, commutative multivariate polynomial algebra interface | `[Semiring T]` alone fails to synthesize `CommSemiring T`, verified under `#check_failure`; no weakening claimed. |
| `α : σ → R` | Outer translation, essential generator image | Cannot drop arbitrary α. |
| `β : σ → R` | Inner translation, essential generator image | Cannot drop arbitrary β. |
| `P : MvPolynomial σ R` | Arbitrary input | Can remove the explicit P by bundling composition, verified below. |
| Additional mathematical assumptions | No field, domain, nonzero, finite, degree, characteristic or subtraction assumptions occur | None to remove. |

Fixed-interface verdict: MAXIMALLY GENERAL. A noncommutative coefficient construction or polynomial-valued shifts with invariance/commutation hypotheses would require a different representation or hypotheses, not a mechanical weakening. No unverified generalisation is offered as an accepted restatement. The semiring failure and bundled form are in [extra native source](../evidence/MvPolynomial.taylor_taylor/native-extra-executed.lean.txt) and [receipt](../evidence/MvPolynomial.taylor_taylor/native-extra-success.json).

## Phase 4c — All nine modern-idiom checks

| # | Question | Applies / consequence |
|---|---|---|
| 1 | Typeclass instead of bundled assumptions? | No; commutative semiring already uses the typeclass hierarchy. |
| 2 | Filters/nets instead of sequences/metrics? | No topology or limits. |
| 3 | Universal property instead of explicit construction? | Yes as proof organization: `comp_aeval` is the existing universal-property engine. No new categorical machinery is needed. |
| 4 | Bundled substructures / morphisms? | Yes: `(taylor α).comp (taylor β) = taylor (fun j ↦ α j + β j)` is natively verified and composes directly as AlgHom equality. These are morphisms, not a new subobject lattice problem. |
| 5 | Modules / semirings instead of field-specific form? | Already generalized beyond the real/field application to CommSemiring. No further fixed-interface weakening. |
| 6 | Higher category formulation? | No concrete downstream gain; ordinary algebra homomorphisms suffice. |
| 7 | Concrete index to abstract monoid/group? | σ already arbitrary. The parameter space σ→R is an additive commutative monoid; expressing shifts as an action is structural packaging, not dropping a concrete index assumption. |
| 8 | Concrete-via-abstract diagnostic? | Yes: the proof's only `taylor` occurrence is the unfolding entry in `simp [taylor, ...]`; zero occurrences remain after unfolding. Abstract composition is exactly `comp_aeval_apply`. Generator normalization still uses the actual translation images, so the abstract theorem alone is not a defeq replacement. |
| 9 | False-generalization guard? | Generic algebra evaluation composition preserves the identity as a specialization after normalization. Arbitrary polynomial substitutions do not obey additive translation composition; action structure must be constructed and its laws proved. Polynomial functions cannot replace formal polynomials over finite rings. No false proposal is accepted. |

Modern idiom available: a bundled AlgHom composition law is verified. It enables rewriting a composition in homomorphism diagrams without first introducing P. Additive action packaging could make this an action axiom; over rings an AlgEquiv with inverse shift −α could supply injectivity directly. Those structures are prospective **new constructions** and require laws; no existing translation action or equivalence on arbitrary `MvPolynomial σ R` was found and claimed as a replacement. Native negative/injective caller checks show the concrete benefit while retaining honest dependency on the newly replayed law. This is an API-design option, not an automatic YES-generalise verdict.

## Phase 4.5 — Infrastructure risk

n/a: theorem, no definition, instance, coercion or definitional equality introduced. The six definition-specific risks (diamond, reducibility leak, noncanonical unfolding, priority collision, universe-polymorphism and coercion ambiguity) do not apply to this theorem assessment. A future action instance would need a separate infrastructure assessment; none is introduced here.

## Phase 4.6 — All five proof-strategy checks

| # | Strategy check | Answer |
|---|---|---|
| 1 | Explicit neighborhoods versus filters | No topology. |
| 2 | Element reasoning versus substructures | No ideal/submodule inclusion. AlgHom equality is a useful alternative, compiled by generator extensionality. |
| 3 | Sequences versus nets | No analysis. |
| 4 | Construction versus universal property | Existing `comp_aeval_apply` already uses the polynomial universal property. Bundled generator extensionality is also checked. |
| 5 | Missing helpers mathlib should have | No missing generic composition engine. Translation-specific surface/API remains a design question. |

Verdict: MATHLIB-IDIOMATIC. The direct simplifier proof computes generators after composition. An action-oriented API could reorganize downstream inverse/injectivity results; that benefit does not turn a new action wrapper into existing mathlib infrastructure.

## Phase 5 — Actual five methods on all three forms

All fifteen method/form cells were executed freshly. External index revisions may differ from the pinned checkout. Positive candidates were read in pinned source and the operative composition/univariate signatures checked natively. Local search returned textual hits but `index: unavailable`; empty index results are never used to prove absence.

| Actual method | Current form | Literature form | Abstract form |
|---|---|---|---|
| Lean-Finder | Multivariate Taylor translation composition → univariate `Polynomial.taylor_taylor` | Taylor shift action → univariate Taylor API | Algebra evaluation composition → `comp_aeval`, `comp_aeval_apply` |
| Loogle | `MvPolynomial.aeval, MvPolynomial.aeval` → evaluation API, not normalized additive law | `Polynomial.taylor, Polynomial.taylor` → univariate API | `MvPolynomial.comp_aeval` → generic bundled law |
| LeanSearch | Taylor translation composition → univariate theorem, `translate_translate` | Taylor shift action → univariate Taylor/AlgEquiv API | Evaluation homomorphism composition → `comp_aeval`, `comp_aeval_apply`, eval₂ composition |
| rg source | Multivariate taylor composition search → no native named law | Univariate Taylor source → exact univariate analogue at157 | MvPolynomial evaluation/ext/action search → generic composition, no established translation action |
| lean_local_search | `taylor_taylor` → project theorem + univariate theorem | `taylor` → project API and univariate API | `comp_aeval` → generic composition candidates; index unavailable |

Exact requests and all responses: [formal search index](../evidence/MvPolynomial.taylor_taylor/formal-search.json), [Finder current](../evidence/MvPolynomial.taylor_taylor/search-lean_leanfinder-current.json), [Finder literature](../evidence/MvPolynomial.taylor_taylor/search-lean_leanfinder-literature.json), [Finder abstract](../evidence/MvPolynomial.taylor_taylor/search-lean_leanfinder-abstract.json), [Loogle current](../evidence/MvPolynomial.taylor_taylor/search-lean_loogle-current.json), [Loogle literature](../evidence/MvPolynomial.taylor_taylor/search-lean_loogle-literature.json), [Loogle abstract](../evidence/MvPolynomial.taylor_taylor/search-lean_loogle-abstract.json), [LeanSearch current](../evidence/MvPolynomial.taylor_taylor/search-lean_leansearch-current.json), [LeanSearch literature](../evidence/MvPolynomial.taylor_taylor/search-lean_leansearch-literature.json), [LeanSearch abstract](../evidence/MvPolynomial.taylor_taylor/search-lean_leansearch-abstract.json), [local current](../evidence/MvPolynomial.taylor_taylor/search-lean_local_search-current.json), [local literature](../evidence/MvPolynomial.taylor_taylor/search-lean_local_search-literature.json), [local abstract](../evidence/MvPolynomial.taylor_taylor/search-lean_local_search-abstract.json), [rg current](../evidence/MvPolynomial.taylor_taylor/rg-current.json), [rg literature](../evidence/MvPolynomial.taylor_taylor/rg-literature.json), [rg abstract](../evidence/MvPolynomial.taylor_taylor/rg-abstract.json), [untruncated full-name grep](../evidence/MvPolynomial.taylor_taylor/rg-full-name.json).

Candidate discrimination: `Polynomial.taylor_taylor` (`Mathlib/Algebra/Polynomial/Taylor.lean:157`) requires a single univariate polynomial and scalar shifts. It cannot simply specialize to arbitrary σ. `translate_translate` (`Mathlib/Algebra/Group/Translate.lean:49`) acts on arbitrary functions by x−a over an additive commutative group; it does not prove equality of formal polynomials, whose evaluation map can fail injectivity over finite rings. The univariate `algEquivAevalXAddC` similarly does not supply the arbitrary-variable semiring law. `MvPolynomial.comp_aeval` and `comp_aeval_apply` (`Mathlib/Algebra/MvPolynomial/Eval.lean:607,612`) are actual generic building blocks; their specialization leaves the generator normalization below. No exact normalized arbitrary-variable existing law or ≤3 existing-call replacement was verified. This is not a search-only assertion of absolute absence.

## Phase 5.5 — All three statement-shape checks

Normal forms compared: nested application equality, bundled AlgHom composition, function equality, and a hypothetical additive-action law. Nested shifts normalize to one shift on the RHS, so the existing pointwise theorem has an appropriate rewrite orientation. The generic canonical engine is `aeval` composition; a named translation surface is optional API rather than a rival polynomial representation.

Syntactic generality: the pointwise and bundled equalities both compile. The existing pointwise statement is easiest for the actual `simp` caller at Taylor184; the bundled statement is easiest for morphism diagrams. Neither justifies requiring a group or finite variables. No argument is superfluous: σ,R and the class support the fixed types; α,β specify the shifts; P is needed in the pointwise surface and intentionally omitted only in the bundled alternative. Overall SHIP-AS-STATED if a named convenience law is accepted; bundling/action packaging is an upstream design option.

## Phase 6 — Callers, inline audit and actual compositions

Internal use count by the command's external-to-declaring-file convention: **0**. Same-file direct source callers: **1**, no external file. The sole direct named call is:

| Caller | Actual source | Dependency and possible refactor |
|---|---|---|
| `Roth/Taylor.lean:184`, `MvPolynomial.taylor_neg_taylor` | `simp [taylor_taylor]` | Set outer α=−α and inner β=α, then zero translation. A future omission of the convenience law could inline `simp [taylor, comp_aeval_apply, add_assoc]` in this caller. |

The law is live: `taylor_neg_taylor` supplies the left inverse used by `taylor_injective` at188, then `taylor_eq_zero_iff` at193 and the inverse step of `eq_sum_box_hasseDeriv` at208. Index uses the translated-polynomial nonzero API. These are transitive callers, not additional named uses of this target. No independent exact inline duplicate was found. The generic composition in `taylor_rename` is a different generator calculation. Source named occurrences are distinct from kernel/simplifier dependency closure. [Fresh native references](../evidence/MvPolynomial.taylor_taylor/native-references.json) returned six locations: the definition, Taylor184, and four scratch inspection locations (including one overlapping qualified identifier).

Evidence: [caller table](../evidence/MvPolynomial.taylor_taylor/callers.json), [exact caller rg](../evidence/MvPolynomial.taylor_taylor/rg-callers.json), [inline audit](../evidence/MvPolynomial.taylor_taylor/rg-inline.json), [native negative caller and derived injectivity](../evidence/MvPolynomial.taylor_taylor/native-extra-success.json). The fresh negative replay uses `TaylorTaylorAssessment.replay`, not the original target.

Actual experiments (root ran serial native Lean; all complete and clean):

1. **Old form, independent native replay**, same original proof:
   ```lean
   simp [taylor, comp_aeval_apply, add_assoc]
   ```
   Successful. Full printed proof uses six distinct mathematical fact families: `comp_aeval_apply`, `map_add`, `aeval_X`, `algHom_C`, `add_assoc`, `C_add`, plus equality/function congruence. Repeated uses and coercion bookkeeping are not hidden as “one call.” It is a closing simp proof, exactly Phase6b BORDERLINE.
2. **Isolated mathlib-only old representation**, locally defined `shift α := aeval (fun j ↦ X j + C (α j))`, with `#check_failure MvPolynomial.taylor_taylor`. Same simp normalization succeeds, proving no project theorem or downstream simp law was necessary. Local `shift` is a new test definition, not existing library replacement.
3. **Bundled translation composition**, both native and isolated: `apply MvPolynomial.algHom_ext; intro j; simp [shift, add_assoc]` (native uses taylor). Successful generator proof; extensionality alone leaves actual normalization. This new proof is not counted as an existing named theorem.
4. **Abstract composition**, arbitrary f and algebra hom φ:
   ```lean
   comp_aeval_apply (f := f) φ P
   ```
   Successful one-existing-call exact proof. This already belongs to mathlib. It is the abstract engine, not yet the normalized α+β law.
5. **Exact old-form first step**, isolated:
   ```lean
   shift α (shift β P) = aeval (fun j ↦ shift α (X j + C (β j))) P
   ```
   closes by `comp_aeval_apply (f := fun j ↦ X j + C (β j)) (shift α) P`. The desired RHS instead has `X j + C (α j + β j)`; computing that image needs the remaining facts. Thus the apparent one-call replacement is not definitionally the old target.
6. **Actual caller**: `simp [TaylorTaylorAssessment.replay]` proves the full negative inverse, and `Function.LeftInverse.injective (negative α)` proves injectivity. Both are standard-axiom, complete native checks. They demonstrate use and structural motivation, not a library replacement for the composition law.

Evidence: [isolated source](../evidence/MvPolynomial.taylor_taylor/native-raw-executed.lean.txt), [isolated native receipt](../evidence/MvPolynomial.taylor_taylor/native-raw-success.json), [extra exact source](../evidence/MvPolynomial.taylor_taylor/native-extra-executed.lean.txt), [verification index](../evidence/MvPolynomial.taylor_taylor/verification.json). No rejected native attempts occurred for this declaration. No exact?/timeout from earlier assessments is inherited as negative evidence.

Conclusion: no verified ≤3-call existing normalized replacement; verified closing-simp composition triggers Phase6b. The one-call abstract law and univariate analogue are acknowledged without overclaiming their specialization.

## Phase 7 — Actionable verdict and gate

**BORDERLINE-needs-human.** Generic evaluation composition already exists, yet a named additive translation law offers a useful surface for the actual inverse caller. The proof is a trivial closing simp composition in the command's explicit borderline category. All parameter, literature, search, strategy, shape and caller checks were run independently; parent `taylor`, sibling `eval_taylor` and accepted `coeff_taylor` verdicts are not inherited. No costs or missing optional tools drive the verdict.

Concrete upstream design questions, not unresolved verification:

1. Should an upstream translation API retain this additive-composition convenience theorem despite its closing simp proof?
2. Prefer the pointwise rewriting law, bundled AlgHom composition law, or both?
3. Should translations be exposed as an additive monoid action, with a ring AlgEquiv upgrade, instead of isolated convenience laws?

Next action: retain the theorem in project-local `Roth/Taylor.lean` while settling that API design. If the named theorem is omitted from a future upstream translation API, inline the verified generator normalization at the sole direct caller Taylor184; preserve the inverse, injectivity and expansion behavior. No production deletion is authorized by this read-only assessment. If upstreaming is selected, the natural destination is a translation/Taylor module under `Mathlib/Algebra/MvPolynomial/`, with `/generalise MvPolynomial.taylor_taylor` and `/cleanup Roth/Taylor.lean MvPolynomial.taylor_taylor` before contribution. This is not an accepted YES PR proposal or reviewer assignment.

Already accepted YES declarations were read from current progress, not inferred from names: [accepted grouping evidence](../evidence/MvPolynomial.taylor_taylor/accepted-grouping.json). In particular `coeff_taylor` is accepted YES, but that does not decide this short compatibility law. No unaccepted sibling is included as a YES grouping commitment.

## Phase 8 — Completion and portability

[Assessment](../evidence/MvPolynomial.taylor_taylor/assessment.json) marks all phases PASS except the justified theorem-only infrastructure n/a, `completed=true`, `unresolved=[]`, `root_acceptance=pending`. [Overview entry](../evidence/MvPolynomial.taylor_taylor/overview-entry.json) retains the full Lean type. [Verification index](../evidence/MvPolynomial.taylor_taylor/verification.json) names exact accepted executed sources, raw complete native receipts and standard-axiom allowlist. [Read-only validator](../evidence/MvPolynomial.taylor_taylor/validate.py) checks the current copy manifest, all evidence hashes/bytes, native completion and axiom checks, fresh production/pin hashes, all five-by-three actual searches, literature requests and portable links in scratch and integrated layouts. Historical worker manifests never substitute for current artifact validation. Root independently reviews and integrates.
