# Roth.linearIndependent_kronecker — full mathlibable assessment

**BORDERLINE-needs-human.** The useful new content is the support-restricted injectivity of monomial evaluation and its degree-bound specialization. The final transport of independence is already `LinearIndependent.map_injOn`. A verified generalization works over any commutative semiring, arbitrary family index, and arbitrary natural base; deciding whether to expose its polynomial-specific corollary depends on the upstream API chosen for the preceding coefficient/injectivity bridge. This assessment is complete; the three API questions below are design choices, not unresolved verification.

## Phase 0 — Doctor

Canonical declaration **111/293**, public theorem, `Roth/GenWronskian.lean:117`. The entire declaring module and its actual sole consumer were read. Its subject is the reduction of generalized Wronskians to ordinary Wronskians through Kronecker substitution. No production source, pin, Git state, or progress record was changed.

The shared `lake build` completed successfully (2467 jobs, exit0). All **17** production-source/pin hashes freshly match the baseline manifest; this permits reuse of that build. Native `#check`, `#print`, and axiom inspection resolve the actual theorem without placeholders. Evidence: [baseline](../evidence/Roth.linearIndependent_kronecker/baseline-build.txt), [fresh hashes](../evidence/Roth.linearIndependent_kronecker/inputs.json), [full source](../evidence/Roth.linearIndependent_kronecker/GenWronskian-source.lean.txt), [native original](../evidence/Roth.linearIndependent_kronecker/original-receipt.json), [canonical entry](../evidence/Roth.linearIndependent_kronecker/canonical-entry.json).

## Phase 1 — Comprehend

Let a finite family of multivariate polynomials over a field be linearly independent, and suppose every polynomial has degree less than `k` in each variable. Substituting powers `t, t^k, t^(k²), …` for an enumeration of the variables preserves that linear independence. The proof applies a putative scalar relation to the substitution, bounds each partial degree of its preimage scalar sum, uses restricted zero detection, and then invokes the original independence.

The exact native type is:

```lean
∀ {K : Type u_1} [inst : Field K] {σ : Type u_2} [inst_1 : Fintype σ] {l k : ℕ},
  1 < k → ∀ {φ : Fin l → MvPolynomial σ K},
    (∀ (ν : Fin l) (j : σ), MvPolynomial.degreeOf j (φ ν) < k) →
      LinearIndependent K φ →
        LinearIndependent K fun ν ↦ (Roth.kronecker k) (φ ν)
```

`K` supplies coefficients/scalars; `σ` indexes variables and `Fintype` supplies the chosen enumeration; `l` indexes the finite family; `k` is the positional base; `hk` is positivity used by the current degree-of-sum proof; `hφ` bounds the family; `h` is its independence. The conclusion concerns formal univariate polynomials, not polynomial functions. Project proof dependencies are `Roth.kronecker` and `Roth.kronecker_eq_zero_iff`; the coefficient/separation chain is transitive.

## Phase 2 — Preliminary checks

**SMALL:** helper transport statement inside the proof of the named generalized-Wronskian result; “Kronecker” identifies its substitution, not a separate principal theorem. The exhaustive literature protocol remains unchanged. One-line definition-only check: **n/a — theorem**, with a substantive multiline proof. No definition barrier or instance-diamond exemption is claimed.

## Phase 3 — Exhaustive literature

Exact requests, response SHA256/bytes/status, primary locators and concise original summaries are in [web evidence](../evidence/Roth.linearIndependent_kronecker/web-evidence.json) and [five-year window/retry](../evidence/Roth.linearIndependent_kronecker/web-window.json). Full web bodies were not persisted. The table below lists every attempted search form; direct opens are recorded separately in the same metadata.

| Channel | Actual query/form | Finding |
|---|---|---|
| General web, specific | `"Kronecker substitution" "linear independence"` | MPG *Diophantine approximation and the subspace theorem*, Lemma2.24, explicitly transports independence after separating bounded monomials. |
| General web, general | `"monomial substitution" injective "linear" polynomials` | Ring-valued exponent packing and injective monomial maps; no field division inherent in encoding. |
| General web, alias | `"Kronecker map" polynomial encoding bounded degree substitution` | Classical Kronecker-map terminology and base-digit separation. |
| Optional ChatGPT mathematics | Standard form/generality/history consultation unavailable | `n/a: ask_chatgpt_math unavailable`; [availability record](../evidence/Roth.linearIndependent_kronecker/optional-channel.json). |
| Local references | `Kronecker|linearly independent|subspace|individual exponent` | `clean.tex:224–271`, source Lemma1 and its coefficient argument. [Excerpt](../evidence/Roth.linearIndependent_kronecker/local-literature-excerpt.txt). |
| nLab via nCatLab host | `site:ncatlab.org "Kronecker substitution"` | No exact result surfaced. |
| nCatLab host, abstract form | `site:ncatlab.org linear independence injective linear map span` | nLab module/subspace and independence pages; this is not a separate exact Kronecker theorem. |
| Stacks | `site:stacks.math.columbia.edu linear independence injective linear map` | Tag05GR uses independent images to establish injectivity on finite free restrictions; related module principle, not this substitution lemma. |
| MathOverflow | `site:mathoverflow.net "Kronecker substitution"` | No exact target surfaced. |
| arXiv | `site:arxiv.org "Kronecker substitution" "2022"` | Supplementary recent encoding literature. |
| arXiv | `site:arxiv.org "Kronecker substitution" "2024"` | 2403.12716, reversible multivariate-to-univariate reduction. |
| arXiv | `site:arxiv.org "Kronecker substitution" "linear independence"` | No stronger exact independence law located. |
| nLab | `site:ncatlab.org/nlab "linear independence" "semiring"` | Abstract free-module monomorphism viewpoint over a rig. |
| MathOverflow retry | `site:mathoverflow.net "Kronecker substitution"` | No exact target surfaced. |
| nCatLab separate channel | `site:ncatlab.org/ncatlab "linear independence"` | No separate categorical improvement located; ordinary modules and submodules suffice. |
| arXiv explicit window | `site:arxiv.org "Kronecker substitution" after:2021-10-27 before:2026-10-28` | 2024 reduction paper and quotient-ring applications; all primary relevant recent locators lie inside five years. |
| MathOverflow broader retry | `site:mathoverflow.net "Kronecker" "substitution" polynomial independence` | Unrelated Kronecker coefficients/umbral substitution; no support for a stronger target. |

Direct opens: [arXiv2403.12716](https://arxiv.org/abs/2403.12716) succeeded; MPG PDF returned403; nLab direct page returned unsupported XHTML400 although indexed material was available; [Stacks05GR](https://stacks.math.columbia.edu/tag/05GR) succeeded, lines22–28. The [MPG primary locator](https://pure.mpg.de/rest/items/item_3634762_1/component/file_3634763/content) was available as an indexed excerpt only. The indexed excerpt uses a degree-bound convention not adopted here; full text was unavailable and no error in the paper is claimed. This report relies on the local strict `< k` digit bound and the independent native proofs.

Concept: **Kronecker substitution / monomial encoding**, followed by **injective linear maps preserve independence**. The local rational-coefficient formulation is sufficient for Roth's theorem. Modern encoding works at the coefficient-module level: weights need only separate the exponent set supporting the family. Fieldness, finite family index, and a global base≥2 restriction are not mathematically essential. The semiring generalization is independently compiled, rather than attributed solely to the web literature. No higher-categorical formulation is needed. Historical development from positional encoding to weighted/reversible computer-algebra encodings is compatible with the abstract support formulation; no exact “most general published theorem” is asserted.

## Phase 4a–b — Parameters and verified generality

| Parameter/hypothesis | Current form | Verified weakening / limit |
|---|---|---|
| Coefficients/scalars | `[Field K]` | `[CommSemiring R]` works after stating the substitution with existing `aeval`; fixed project `Roth.kronecker` itself still requires Field. No claim of a literal edit through that fixed parent interface. |
| Variables | `[Fintype σ]` | Arbitrary `σ` for arbitrary weights `w`; explicit `e : σ ≃ Fin n` for positional exponents. A finite enumeration is genuine data for positional encoding. |
| Family | `φ : Fin l → …` | Arbitrary index type `ι`; no Fintype/Finite assumption. Relations have finite support intrinsically. |
| `l` | Natural family length | Eliminated with arbitrary `ι`. |
| Base `k` | Natural positional base | Any natural `k`; no inequality hypothesis in verified positional theorem. |
| `hk` | `1 < k` | Dropped. For k0/k1 use support sets, not the false assertion that strict degree-bound sets are always submodules. |
| `hφ` | Every partial degree `< k` | Support containment in any `S` on which weighted exponents are injective. The original degree bound implies this support condition by `monomial_le_degreeOf`. |
| `h` | Original linear independence | Essential: no claim that substitution creates independence. Existing `LinearIndependent.of_comp` supplies the reverse direction without injectivity. |
| Universes | Independent coefficient/variable universes | Generic probe has independent arbitrary `Type*` indices; no universe collapse introduced. |

**STRICTLY NARROWER THAN VERIFIED GENERAL FORM.** [Abstract executed source](../evidence/Roth.linearIndependent_kronecker/abstract-executed.lean.txt) and [receipt](../evidence/Roth.linearIndependent_kronecker/abstract-receipt.json) prove all proposed weakenings with standard axioms. The support formulation uses existing `AddMonoidAlgebra.supported`, not a new ad-hoc bundle. Proposed public shape (names provisional):

```lean
theorem linearIndependent_aeval_X_pow {R σ ι : Type*} [CommSemiring R]
    (w : σ → ℕ) (S : Set (σ →₀ ℕ))
    (hi : Set.InjOn (Finsupp.weight (R := ℕ) w) S)
    {φ : ι → MvPolynomial σ R}
    (hφ : ∀ i, (↑(φ i).coeff.support : Set (σ →₀ ℕ)) ⊆ S)
    (h : LinearIndependent R φ) :
    LinearIndependent R fun i ↦
      MvPolynomial.aeval (fun j ↦ (Polynomial.X : Polynomial R) ^ w j) (φ i)
```

A second verified shape replaces `w` by `k^(e j)` for `e : σ ≃ Fin n`, `hφ` by the original pointwise degree bounds, and omits `hk`. This is a real expanded representation, using newly proved bridge/injectivity prerequisites. It is not a ≤3-call existing-mathlib replacement.

## Phase 4c — Modern-idiom check

| # | Question | Answer and consequence |
|---|---|---|
| 1 | Typeclass preambles? | Already uses instances; weaken Field to CommSemiring after re-aiming at `aeval`. |
| 2 | Sequences/metrics to filters? | No topology or convergence. |
| 3 | Construction to universal property? | Existing `MvPolynomial.aeval` already packages the free commutative-algebra universal property; no new substitution definition needed. |
| 4 | Closure predicate to substructure? | Yes: `AddMonoidAlgebra.supported R R S` contains the family span by `Submodule.span_le`. Enables lattice/submodule inclusion and existing map-on-span API. |
| 5 | Field result to module hierarchy? | Yes: semiring module linear independence and `LinearIndependent.map_injOn`, avoiding subtraction/field division. |
| 6 | Higher categories? | No: ordinary modules and linear maps capture the theorem. |
| 7 | Concrete indices? | Yes: Fin l→arbitraryι; arbitraryσ in weighted form. ℕ exponents remain the actual polynomial monoid; replacing them would change the codomain and is not claimed here. |
| 8 | Concrete-via-abstract? | Yes. Body lines120–128 have one occurrence of `kronecker_eq_zero_iff` and no bare `kronecker` call; the rest uses linearity, degree closure, and independence. The concrete substitution is only used through restricted zero detection. Replace the final relation argument by existing `map_injOn` once span injectivity is proved. |
| 9 | False-generalization guard? | No false generalization in accepted proposals: each specializes to the exact original type. Reject global injectivity: X₁ and X₀^k collide. Reject treating `{P | ∀j, degreeOf j P<0}` as a submodule when σ is inhabited: it omits zero. The support submodule handles k0 and empty cases correctly. |

Modern idiom available: **yes**, substantive: arbitrary families and semirings become available through support submodules and linear-map transport. Missing mathematics is the specialized injectivity premise; the abstract transport is already in mathlib. This distinction controls Phase7.

## Phase 4.5 — Infrastructure risk

**n/a — theorem.** No new definitions, classes, instances or coercions are proposed as assessment changes. All six definition-risk dimensions (diamond, reducibility leak, noncanonical unfolding, instance priority, universe restriction, coercion ambiguity) are outside this declaration-kind gate. Existing supported submodules and `aeval` avoid inventing new infrastructure.

## Phase 4.6 — Proof-strategy audit

| # | Question | Result |
|---|---|---|
| 1 | ε–δ vs filters? | n/a: algebraic finite-support argument. |
| 2 | Element reasoning vs submodule inclusion? | Yes: prove span(rangeφ)≤supportedS, restrict the substitution's injectivity there, then apply `LinearIndependent.map_injOn`. |
| 3 | Sequences vs nets? | n/a: no limits. |
| 4 | Explicit categorical construction vs universal property? | Existing `aeval` already supplies the construction; no separate categorical proof. |
| 5 | Helpers mathlib should have? | The evaluation/coefficient `mapDomain` representation bridge, support-restricted monomial-evaluation injectivity and positional weight separation are new proofs from assessments108–110. Their API organization remains open; no new generic independence-transport lemma is missing. |

**REFACTOR-RECOMMENDED:** use the support-submodule strategy. It removes the finite-sum degree/positivity bottleneck and is strictly cleaner in its available hypotheses. Cost: moderate proof/API rearrangement; cost does not decide the verdict. The first attempted `.mono` premise left an implicit polynomial argument ambiguous; its rejected receipt is preserved separately, followed by the accepted explicit-lambda proof. The first edge probe also used an unavailable empty-family spelling and an underconstrained `aeval`; these were repaired to `linearIndependent_empty_type` and explicit `R := ℚ`. Rejected elaborations with recovered `sorryAx` are not accepted proof evidence.

## Phase 5 — Five-method search, all three forms

[Complete formal requests/raw responses](../evidence/Roth.linearIndependent_kronecker/formal-search-raw.json), [corrected abstract Loogle request](../evidence/Roth.linearIndependent_kronecker/loogle-abstract-final.json), and the complete untruncated [current](../evidence/Roth.linearIndependent_kronecker/rg-current.json), [literature-standard](../evidence/Roth.linearIndependent_kronecker/rg-standard.json), [abstract](../evidence/Roth.linearIndependent_kronecker/rg-abstract.json) source searches retain exact evidence.

| Method | Current form | Literature-standard form | Abstract form |
|---|---|---|---|
| Lean-Finder | Kronecker bounded-degree independence; variables/finite-field evaluation near matches | Injective monomial substitution on supported exponents; no exact target | `LinearIndependent.map_injOn` and equivalent iff. |
| Loogle | `MvPolynomial, LinearIndependent`; variables/submersive near matches | `LinearIndependent, Set.InjOn`; exact generic transport | First query malformed (`LinearIndependent (_ ∘ _)` omitted scalar argument), first corrected retry rate-limited; final `LinearIndependent _, Function.comp` succeeded and found map_injOn/iff. All failures archived honestly. |
| LeanSearch | Kronecker bounded degrees; algebraic-independence near matches | Injective linear map on span; map_injOn/iff | Same final transport plus map′. |
| `rg` pinned source | Kronecker/aeval/independence | map_injOn, mapDomain_injOn/support | supported submodules, coefficient equivalence, span closure. |
| Local name patterns | `linearIndependent_kronecker` finds project/scratch only | `map_injOn` | `linearIndependent_iff_of_injOn`; positive pinned source hit. Index reports unavailable, so no absence inference. |

Pinned positive candidates, natively checked:

* `LinearIndependent.map_injOn`, `Mathlib/LinearAlgebra/LinearIndependent/Basic.lean:136`: a semiring-linear map injective on the span of the family preserves its independence.
* `LinearMap.linearIndependent_iff_of_injOn`, `…/Defs.lean:330`: same premise, equivalence of independence.
* `LinearIndependent.map′`, `…/Basic.lean`: requires globally trivial kernel over a ring; unsuitable for unreduced multivariate-to-univariate substitution.
* `AddMonoidAlgebra.supported` and `mem_supported`, `Mathlib/Algebra/MonoidAlgebra/Module.lean:142`: existing support submodule; `Submodule.span_le` proves closure of the family span.
* `Finsupp.mapDomain_injOn` and its coefficient representation route are the restricted-injectivity foundation, not already a theorem phrased as bounded-degree evaluation independence.

Conclusion: **partial exact abstract match**, not an exact bounded-degree `aeval` law. Native source/axiom evidence verifies the generic hit at the current pin. External indexes can differ from the pinned revision. Neither failed searches nor local-index unavailability prove absence. A mathlib-only `exact?` probe of the bounded positional goal hit the default200000-heartbeat limit at `isDefEq`: tool-level timed_out=false does not make that a clean no-hit. It is archived as [rejected absence evidence](../evidence/Roth.linearIndependent_kronecker/absence-receipt.json), was not rerun with raised limits, and supports no absence claim. The verdict rests on the positive verified proof/API distinction.

## Phase 5.5 — Statement shape

Normal forms considered: (1) concrete Kronecker family preservation, (2) `LinearIndependent R (f ∘ φ)` under `Set.InjOn f (span R (range φ))`, (3) supported monomial-evaluation corollary, (4) corresponding independence iff. Mathlib's canonical transport is (2), already present; `aeval` is the canonical substitution representation. The current theorem is not an incorrectly oriented iff; RHS convention is inapplicable to this implication. The existing iff puts the unmapped independence on the RHS.

Syntactic generality attempts: arbitrary family `ι`, arbitrary support/weight, explicit finite equivalence for positional exponents, and a recovery term with the exact original interface. Keep degree bounds as a convenient caller-facing hypothesis only if the positional corollary is chosen; expose support injection for weights. This makes alternative sparse monomial separators usable without forcing uniform partial degrees.

Superfluous-argument audit: Field is stronger than necessary after parent re-aim; Fintypeσ is necessary only for the chosen-enumeration spelling; Finl is unnecessary; hk is unnecessary in the accepted proof; hφ remains essential in the positional form and becomes support containment plus weight separation; h remains essential; k and e determine the actual map and cannot be erased. **RESTATE-BEFORE-SHIP**, subject to the API questions.

## Phase 6.0 — Actual callers and inline audit

[Explicit source receipts](../evidence/Roth.linearIndependent_kronecker/rg-callers.json), [inline scan](../evidence/Roth.linearIndependent_kronecker/rg-inline.json), [caller metadata](../evidence/Roth.linearIndependent_kronecker/callers.json), [canonical293 audit](../evidence/Roth.linearIndependent_kronecker/audit-receipt.json).

| Caller | Usage | Refactor route |
|---|---|---|
| `Roth.exists_genWronskian_ne_zero`, `Roth/GenWronskian.lean:263` | Applies target to k=2+sum of all partial degrees, bounded family, and its independence | Replace this one invocation by the verified positional recovery, or obtain span injectivity from the support API and call `h.map_injOn`. The original caller's chosen k and bound proof remain usable. |

Named explicit callers: **1**, all in declaring file. Internal use count excluding declaring file: **0**. External-to-file callers: **0**. No independent inline re-derivation found in production. Canonical audit inspects all293 exact ordered unique source declarations and identifies the same sole direct consumer; it is not a claim about full opaque kernel/simp dependency closure. This theorem is used and is not junk.

## Phase 6 — Composition experiments and parent re-aim

1. **Exact final transport succeeds:** with `hf : Set.InjOn f (span R (range φ))`, the complete proof is `h.map_injOn f hf`. This is one existing mathlib call. It assumes the specialized injectivity work has already been performed.
2. **Generic support/evaluation proof succeeds:** prove `span(rangeφ)≤AddMonoidAlgebra.supported R R S` by `Submodule.span_le`, use the newly verified support-restricted evaluation injection, then the existing transport. The accepted source contains the actual normalization and inclusion proof. It is not a new generic linear-algebra theorem.
3. **Positional no-hk specialization succeeds:** use newly proved base-digit/weight injectivity and `monomial_le_degreeOf` to supply the support premise. The exact old interface and actual consumer are replayed in [consumer source](../evidence/Roth.linearIndependent_kronecker/consumer-executed.lean.txt) and [receipt](../evidence/Roth.linearIndependent_kronecker/consumer-receipt.json). That accepted source also checks k0 with empty variables, k1, and empty families, plus the noninjective global map. A fresh [mathlib-only source](../evidence/Roth.linearIndependent_kronecker/isolated-executed.lean.txt) and [receipt](../evidence/Roth.linearIndependent_kronecker/isolated-receipt.json) physically include all new prerequisites and the target proof while guarding that the project theorem is absent.
4. **Global map′ route rejected mathematically:** the substitution is not globally injective in two variables; the compiled counterexample makes the premise failure concrete. Passing a global kernel-zero hypothesis would change the original theorem's mathematical content.

**NOT-COMPOSABLE in ≤3 existing calls from the original hypotheses.** New positional separation, coefficient/mapDomain bridge, and restricted evaluation injection are proof prerequisites, not available mathlib calls. Their final independence transport does have an existing exact law. No `simp [defs…]` closure is miscounted as a ≤3-call proof.

**Automatic NO parent gate:** parent `Roth.kronecker` was assessed NO in favor of `MvPolynomial.aeval`. Re-aiming is performed explicitly. Mathlib does have an analogous final law for *arbitrary linear maps with span-injectivity already assumed*; however the actual `aeval` law with the degree/support sufficient condition still needs the nontrivial new injection proof. That premise is not a representational identity. Thus the rule does not automatically resolve this bounded-degree law as NO. Prior109/110 verdicts are not inherited; their executed proofs are verification prerequisites.

## Phase 7 — Verdict and actionable design questions

**BORDERLINE-needs-human.** The mathematical generalization is verified, and the transport endpoint already exists. The unresolved issue is the grain of the upstream polynomial API: whether restricted injectivity plus existing transport should be the public interface, or whether a discoverable support/positional linear-independence corollary merits its own name. This is an API choice independent of proof cost. Do not submit the current Field/Finl/hk spelling unchanged or delete it claiming that `map_injOn` directly discharges degree bounds.

1. Should the upstream contribution stop at support-restricted `aeval(X^w)` injectivity and use existing `LinearIndependent.map_injOn` at callers, or also expose the compiled support-family independence corollary?
2. Should a positional corollary with explicit `e : σ ≃ Fin n`, arbitrary family index and no `hk` be public, or remain a project-local bridge for the Wronskian proof?
3. Should the span-to-supported inclusion be left as a local `Submodule.span_le` argument, or packaged alongside the chosen restricted-evaluation API for repeated use?

Next action: choose the API boundary, then rerun `/mathlibable Roth.linearIndependent_kronecker` if that changes what is being proposed upstream. No user response is required to finish this read-only overview. Until then, keep the present theorem local to `Roth/GenWronskian.lean` or place the generalized bridge in a project-local Kronecker module.

If a public theorem is selected, a plausible new leaf home is `Mathlib/Algebra/MvPolynomial/MonomialEval.lean`, consistent with the provisional generic monomial-evaluation bridge home in110. The distinct positional-separation law108 retains its accepted proposed home `Mathlib/Data/Nat/Digits/Finsupp.lean`; it is a prerequisite, not silently relocated into a Kronecker hierarchy. The coefficient/evaluation bridge requires polynomial algebra/toFinsupp, weight, and domain-map imports, so foundational `MvPolynomial/Eval.lean` is only a provisional home pending import-layer review. Proposed future PR: `feat(Algebra/MvPolynomial): support-restricted monomial substitutions`. [Accepted YES snapshot](../evidence/Roth.linearIndependent_kronecker/accepted-yes.json) confirms `Roth.kroneckerExp_injOn` is YES-but-generalise-first;109 and110 are BORDERLINE and are not relabeled accepted YES. A future YES contribution requires `/generalise`, full `/cleanup`, and reviewer selection from recent relevant commits; no PR/reviewer assignment is performed for this BORDERLINE assessment.

## Phase 8 — Completion and evidence integrity

All required phases have PASS or theorem-kind n/a status. The [verification manifest](../evidence/Roth.linearIndependent_kronecker/verification.json) links exact accepted sources and raw native receipts, distinguishes rejected attempts, and records original execution requests and fresh native regions. The [portable validator](../evidence/Roth.linearIndependent_kronecker/validate.py) validates the current copy manifest in scratch or integrated layout, checks all17 source/pin hashes, exact293-name order, fresh target markers, raw native completion, standard axioms only, source/receipt agreement, evidence links and the credential guard. Root independently reviews this complete package before integration. No verification debt is hidden by the design questions.
