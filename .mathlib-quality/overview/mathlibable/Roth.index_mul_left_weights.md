# Roth.index_mul_left_weights

**Verdict: NO-mathlib-has-it**, by the parent re-aim rule: the analogous law for the more general support minimum `AddMonoidAlgebra.infDegree` is the existing `map_finset_inf`. The real-valued, denominator-weight statement requires a verified representation bridge; that bridge is not definitional and is not counted as an existing mathlib theorem.

## Phase 0 — Baseline

The [baseline](../evidence/Roth.index_mul_left_weights/baseline-build.txt) is a successful `lake build` (2467 jobs, exit0, no warnings/errors). All17 production/pin hashes were freshly compared with the shared input manifest and match; see [fresh inputs](../evidence/Roth.index_mul_left_weights/inputs.json). The public theorem resolves at Roth/Index.lean:200; no sorry. The entire declaring module and full explicit caller were read. Index.lean defines the weighted minimum of Taylor support and proves its basic arithmetic/transport properties. This is read-only assessment; production sources and Git are unchanged.

## Phase 1 — Mathematical content and native type

For any polynomial P, point α, natural denominator vector r and natural l, replacing every r_j with l r_j divides the index by l. The result includes P=0, entries r_j=0 and l=0. In the last case every direct reciprocal weight is zero and both sides are zero under Lean's division-by-zero and the project's index0 convention.

```lean
Roth.index_mul_left_weights.{u_1} {σ : Type u_1} [Fintype σ] {l : ℕ}
    (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) :
    (Roth.index P α fun j ↦ l * r j) = Roth.index P α r / ↑l
```

σ is the variable index type; Fintype supports the current global-sum weight interface. P and α supply the translated polynomial, r supplies denominators, and l is the common factor. There is no positivity/nonvanishing hypothesis. The proof first shows the weighted support image is multiplied by (l:ℝ)⁻¹ using project `weight_mul_left`, then invokes existing `Real.sInf_smul_of_nonneg` and normalizes division. [Native original source](../evidence/Roth.index_mul_left_weights/index-scale-original-executed.lean.txt) and [complete receipt](../evidence/Roth.index_mul_left_weights/index-scale-original-audit-receipt.json) retain the full type, full kernel print with no elision, standard axioms and canonical audit.

## Phase 2 — Preliminary classification

**SMALL:** a transport law, not a new structure or a named main theorem. This does not reduce literature width. One-line definition test: n/a, declaration is a theorem. The existing proof is a genuine image/infimum normalization, not `rfl`; the independently checked negative rfl probe confirms the old expression is not definitionally equal to its quotient form.

## Phase 3 — Exhaustive literature

Every named channel and at least three distinct general queries were executed. Exact requests, response digest/bytes/status, titles, URLs and concise original summaries are archived; no article/search bodies are persisted. Returned URL query parameters were removed, including a credential-bearing guest-access parameter; hashes refer to the exact original responses.

| Channel / exact query | Outcome / locator |
|---|---|
| Specific web: `Roth theorem polynomial index scaling weights index l r divided l` | Min Ru, Roth's Theorem, p3 defines the minimum of ∑i_j/d_j. [Request metadata](../evidence/Roth.index_mul_left_weights/web-general.json). |
| General web: `weighted order vanishing polynomial scaling weights minimum support` | Weighted-order/minimal-support form; excludes weighted total-degree maxima and analytic weighted approximation. Same metadata. |
| Alias web: `monomial valuation weighted order rescaling weight vector` | Monomial weights and valuations; positive common scaling preserves order. Same metadata. |
| ChatGPT mathematical second opinion | n/a: ask_chatgpt_math unavailable; no fabricated query or response. |
| Local manuscript | [Actual search](../evidence/Roth.index_mul_left_weights/local-literature-search.json), [§4 excerpt](../evidence/Roth.index_mul_left_weights/clean-index-excerpt.tex.txt). Explicit ind(P;α;lr)=(1/l)ind(P;α;r), l>0. |
| nLab: `site:ncatlab.org/nlab weighted valuation order vanishing scaling` | Valuation page gives ordered-group/infinity convention. Search succeeded; direct open failed400 unsupported XHTML. [Search](../evidence/Roth.index_mul_left_weights/web-nlab.json), [open](../evidence/Roth.index_mul_left_weights/web-primary.json). |
| nCatLab: `site:ncatlab.org/ncatlab finite infimum monotone map valuation` | Actual distinct namespace checked. Service returned nLab results outside that namespace; no exact hit. [Receipt](../evidence/Roth.index_mul_left_weights/web-ncatlab.json). |
| Stacks: `site:stacks.math.columbia.edu monomial valuation order vanishing weight` | Divisors chapter/valuation orders adjacent; no exact weight-scaling identity identified. [Receipt](../evidence/Roth.index_mul_left_weights/web-stacks.json). |
| MathOverflow: `site:mathoverflow.net weighted order vanishing scaling weight vector valuation` | Mostly adjacent/unrelated analytic weighted approximation. General search also returned monomial-orders question476147. No replacement theorem inferred. [Receipt](../evidence/Roth.index_mul_left_weights/web-mathoverflow.json). |
| Recent arXiv: `site:arxiv.org weighted valuation scaling weight polynomial 2022 2023 2024 2025 2026` | Noisy initial search; preserved honestly. [Receipt](../evidence/Roth.index_mul_left_weights/web-arxiv.json). |
| Recent arXiv refinement: `site:arxiv.org "monomial valuations" "weights" "2024"`; `site:arxiv.org "weighted order" "polynomial" "2023"` | 2023 higher Jacobian weighted-homogeneous polynomial paper adjacent, not exact law. [Receipt](../evidence/Roth.index_mul_left_weights/web-arxiv-refined.json). |
| Primary recent arXiv: Salami, 2610.17589 (13Oct2026), §8 | Fixed-P weighted index is min∑q_i i_i/d_i. Its counterexample concerns auxiliary-polynomial existence after anisotropic floored degree bounds, not this scalar identity. [Opened paper](../evidence/Roth.index_mul_left_weights/web-arxiv-paper.json), [§8 locator](../evidence/Roth.index_mul_left_weights/web-arxiv-section8.json). |

Primary supporting sources: [Min Ru notes, p3](https://www.math.uh.edu/~minru/fields/roth.pdf), [Salami2026 §8](https://arxiv.org/html/2610.17589v1#S8). The identified concept is homogeneous scaling of a weighted order of vanishing, abstractly monotone transport of a finite support minimum. Classical positive real denominators and infinity at P=0 differ from the project's natural denominators, total zero division and index0=0. This difference is preserved explicitly, not erased by a literature analogy. See [literature summary](../evidence/Roth.index_mul_left_weights/literature-summary.json).

## Phase 4a — Parameters and generality

| Parameter | Current interface | Checked expanded representation / limitation |
|---|---|---|
| σ : Type u | arbitrary universe, Fintype | Generic infDegree transport has arbitrary A : Type u without finiteness: finite support suffices. |
| Fintype σ | required to form unchanged Roth.weight/index | Not a mechanically droppable instance in this fixed signature. Supported degree maps remove it only after restating the parent interface. |
| P : MvPolynomial σ ℝ | real polynomial | Generic law compiled for AddMonoidAlgebra R A with Semiring R, no field/domain/commutativity assumption. Translation is input data, not used by minimum transport. |
| α : σ→ℝ | center | Genuine mathematical input; retained when returning to actual index, abstract law accepts an arbitrary finite-support algebra element. |
| r : σ→ℕ | denominators can be zero | Generic D : A→K is arbitrary; reciprocal natural weights specialize it. No denominator-clearing product and no positivity assumptions inserted. |
| l : ℕ | includes zero | Direct scaling c≥0 is verified, c=(l:ℝ)⁻¹; arbitrary monotone zero-preserving φ is verified too. Negative c changes minimum to maximum; guard checked. |
| ℝ output | sInf∅=0 | Generic WithTop degree retains top internally, then untopD0 gives exact original convention. Generalized target orders and zero-preserving transport compile. |

## Phase 4b — Generality verdict

Within the fixed Roth.index/weight interface this statement is **MAXIMALLY GENERAL**: no positivity, nonzero or other removable premises occur. The parent interface is fixed to real coefficients/results and Fintype global-sum weights, so simply deleting Fintype or substituting a typeclass binder for ℝ is not a verified weakening. The expanded representation is strictly broader and **actually compiled**, rather than being proposed based on appearance: arbitrary semiring coefficients, arbitrary support degree map, arbitrary universes, and InfTopHom between semilattices with top. Monotone φ between arbitrary linear orders with zeros transports the projected minimum when φ0=0. The ordered-semiring scalar specialization is recorded in the [exact guard source](../evidence/Roth.index_mul_left_weights/index-scale-guards-executed.lean.txt) and [clean native receipt](../evidence/Roth.index_mul_left_weights/index-scale-guards-receipt.json). These are representation changes, not a claim of a single mechanical edit or of logically minimal algebraic typeclasses.

The generic core already exists in mathlib. No YES-but-generalise-first verdict is inferred merely from a narrower parent signature.

## Phase 4c — All nine modern-idiom rows

| # | Check | Applies? / reformulation and consequence |
|---|---|---|
| 1 | Typeclass preambles | No explicit preamble hypothesis to bundle; existing Semiring/lattice classes already express generic assumptions. |
| 2 | Sequences to filters | No: finite support arithmetic, no convergence. |
| 3 | Construction to universal property | No new universal-property construction; finite inf is already canonical. |
| 4 | Closed subset to bundled substructure | Yes: package the degree transport as InfTopHom. map_finset_inf then applies directly and composes with other lattice maps. |
| 5 | Vector-space/field hierarchy | Yes in expanded representation: polynomial coefficients need only Semiring for degree transport, no real field argument. Broader AddMonoidAlgebra clients share the law. |
| 6 | Higher categories | No categorical coherence issue appears. |
| 7 | Concrete numeric index | Yes: degree target arbitrary semilattice with top, and arbitrary ordered K,L for projected monotone transport; finite support permits rational/real/non-numeric targets. |
| 8 | Concrete-via-abstract diagnostic | Fires. P and α occur only inside the same Taylor support; index appears only in the final unfolding. After image normalization the content is sInf(a•S)=a•sInfS, existing Real law. Parent re-aim is map_finset_inf, not a new polynomial fact. |
| 9 | False-generalization guard | Zero-preserving φ is essential after untopD0: translation x↦x+1 fails at empty support/top. Negative scalar fails for min1,2. WithTop.map(0*·) preserves top; raw zero multiplication in other extended semirings can collapse top, so no universal smul0-top assertion is made. Salami's anisotropic floor-box existence theorem is a different statement. |

Modern idiom available: **yes, already existing**. The concrete downstream advantage is shared finite-inf transport through InfTopHom and composition, with an explicit zero-default projection only at the project boundary. [Exact isolated mathlib-only proofs](../evidence/Roth.index_mul_left_weights/index-scale-mathlib-clean-executed.lean.txt) and [clean receipt](../evidence/Roth.index_mul_left_weights/index-scale-mathlib-clean-receipt.json) verify the proposal without importing Roth.

## Phase 4.5 — Infrastructure risk

n/a: this declaration is a theorem. It introduces no typeclass path, reducible definition, instance priority, coercion or universe computation. Thus the six definition-only risk rows (diamond, reducibility leak, noncanonical unfolding, priority collision, universes, coercions) are all n/a for this target. Scratch liftMonotone is explanatory evidence, not a proposed new global instance.

## Phase 4.6 — All five proof-strategy rows

| # | Strategy check | Finding |
|---|---|---|
| 1 | ε–δ versus filters | n/a: no topology. |
| 2 | Element algebra versus point-free maps | Re-aim recommends bundled InfTopHom on finite inf instead of rebuilding weighted-image transport for each polynomial. Actual current image proof is valid and library-based. |
| 3 | Sequences versus nets | n/a: no infinite limiting argument. |
| 4 | Explicit object versus universal property | n/a: no new categorical object. |
| 5 | Helpers mathlib should supply | Existing map_finset_inf and Real.sInf_smul_of_nonneg supply core laws. Project zero-projection and reciprocal-weight normalization remain genuine adapter proofs; their being new proofs does not make them existing mathlib calls. InfHom.withTop is also present as a source/remote-index candidate, but the accepted proof directly builds the lift; no unexecuted replacement is claimed. |

Strategy verdict: **MATHLIB-IDIOMATIC locally; REFACTOR-RECOMMENDED with the parent infDegree migration.** Use the same bundled finite-inf transport across degree targets. No cost-based downgrade and no categorical decoration rationale.

## Phase 5 — All five methods, three forms

[Raw formal requests/responses](../evidence/Roth.index_mul_left_weights/formal-search.json) cover current polynomial/denominator form, literature weighted-order form and abstract finite-inf hom form. [Successful Loogle refinement](../evidence/Roth.index_mul_left_weights/search-literature-loogle-success.json) fixes an initial unknown-sInf parser error and an intervening rate limit, both retained separately.

| Method | Current form | Literature form | Abstract form |
|---|---|---|---|
| Finder | Irrelevant Roth-number/spectral-weight hits, no exact replacement | weightedOrder, nearby scalar-polynomial laws | finite inf transport and infDegree_withTop_some_comp |
| Loogle | MvPolynomial quotient-pattern results, not exact identity | Initial unknown `sInf`; quoted-name retry found exact Real.sInf_smul_of_nonneg | Finset.inf+InfTopHom query returned no items |
| LeanSearch | scaleRoots changes polynomial, not denominator weights | weightedOrder and nearby weighted-homogeneous APIs | exact map_finset_inf, InfHom.withTop, finite indexed inf APIs |
| rg | [Current](../evidence/Roth.index_mul_left_weights/rg-current.json): Real.sInf_smul_of_nonneg and Set.image_smul | [Literature](../evidence/Roth.index_mul_left_weights/rg-literature.json): weight/scalar families | [Abstract](../evidence/Roth.index_mul_left_weights/rg-abstract.json): generic infDegree, finite-inf maps |
| Local name index | Project target | Real.sInf_smul_of_nonneg and nonpos law | No generated exact hit; index unavailable |

Local unavailable index does not prove absence. Remote indexes may differ from pin (including deprecated names and support/coeff.support changes); pinned successful proofs determine usable signatures. **Found in mathlib as `map_finset_inf`, more general form after the independently verified infDegree representation bridge.** It is generated by to_dual from map_finset_sup at Mathlib/Data/Finset/Lattice/Fold.lean:93; also Finset.apply_inf'_eq_inf'_comp generated near617. Parent object AddMonoidAlgebra.infDegree is Degree.lean:624. Real.sInf_smul_of_nonneg is Basic/Real/Pointwise.lean:41 and already allows a general ordered scalar field acting on ℝ. Searches identify presence, not a proof of absence of every named scaling spelling.

## Phase 5.5 — All three statement-shape checks

**Normal form:** finite infimum of the degree map on coefficient support; WithTop preserves the empty minimum before untopD0. Equivalent real forms are image-sInf, nonempty Finset.inf', and projected infDegree. Existing map_finset_inf is the canonical transport theorem. Old index(lr)=index(r)/l is convenient local quotient normalization but not the generic statement. Direction of local equality normalizes scaled denominators on the RHS.

**Syntactic generality:** attempted generic InfTopHom, zero-preserving monotone φ, and c≥0 direct multiplication; all accepted native proofs have precise hypotheses. Generic transport's direction h(inf)=inf(h∘D) follows mathlib; bridge uses its reverse after projection. Direct reciprocal quotient syntax is retained for the actual caller's subsequent div_le_iff.

**Superfluous arguments:** σ/universes general; Fintype needed by unchanged parent; P, α, r and l each determine the expression. There is no explicit hypothesis to drop. α cannot be erased without changing the centered index; abstract law accepts its Taylor polynomial as data. Overall **RESTATE-BEFORE-SHIP toward existing generic API**, no proposed new upstream target theorem.

## Phase 6.0 — Complete callers and inline audit

[Ignore-safe rg and git grep](../evidence/Roth.index_mul_left_weights/complete-caller-search.json) were cross-checked against [fresh canonical-file lexical enumeration](../evidence/Roth.index_mul_left_weights/lexical-enumeration.json). One external-to-file caller, one source reference line, **two proof applications**, zero statement references. The exact293/293-unique/present/value canonical ordered audit found the same sole direct kernel-value consumer; source applications and kernel consumers are separately measured.

| Caller | Source | Usage / refactor |
|---|---|---|
| private Roth.index_separated_mul_le_aux | Roth/Theta.lean:447 | `rw [index_mul_left_weights] at hUΘ hVΘ`: applies to U over τ and V' over Unit. Full copied caller changes only its name and replaces the target with IndexScale148.replacement. Under parent migration, use the independently verified IndexScaleBridge148.replacement in the same positions. Its type is identical. |

[Caller plan](../evidence/Roth.index_mul_left_weights/callers.json) and [full executed replay](../evidence/Roth.index_mul_left_weights/index-scale-target-callers-clean-executed.lean.txt) / [receipt](../evidence/Roth.index_mul_left_weights/index-scale-target-callers-clean-receipt.json) retain all parameters and the entire proof. The caller's l>0 is needed later to clear division inequalities, not by the target scaling identity. [Inline audit](../evidence/Roth.index_mul_left_weights/rg-inline.json) finds the declaration, supporting weight_mul_left and the explicit caller; no independent inline re-derivation. This useful API is not junk or dead code; external use is not established by local search.

## Phase 6 — Actual composition experiments

The re-aimed mathematical law compiles with **one existing mathlib call**, all parameters explicit:

```lean
example [Semiring R] [SemilatticeInf T] [OrderTop T]
    [SemilatticeInf U] [OrderTop U] (h : InfTopHom T U) (D : A → T)
    (f : AddMonoidAlgebra R A) :
    h (AddMonoidAlgebra.infDegree D f) = AddMonoidAlgebra.infDegree (h ∘ D) f :=
  map_finset_inf h f.coeff.support D
```

That proof is accepted in the isolated mathlib-only receipt and actual project context. To recover the original form, the checked bridge uses `IndexConsumers133.targetBridge` twice, rewrites the degree function with weight_mul_left and div_eq_inv_mul, and applies the freshly proved projected scaling law to TaylorαP. The parent bridge, lift and projection are **new normalization proofs**, not preexisting mathlib building blocks. Full actual bridge source [here](../evidence/Roth.index_mul_left_weights/index-scale-bridge-clean-executed.lean.txt), [receipt](../evidence/Roth.index_mul_left_weights/index-scale-bridge-clean-receipt.json).

The old expression is **NOT-COMPOSABLE in ≤3 existing mathlib calls as demonstrated**: the existing proof uses Set.image_smul, Set.image_image, Set.image_congr, the project weight_mul_left, Real.sInf_smul_of_nonneg, and arithmetic normalization. No original project theorem is smuggled into the count. A closing `simp [defs...]` would be BORDERLINE under Phase6b, not automatic NO. We do not use such a simp closure to decide the verdict. The generic core is **COMPOSABLE, one call**, and the ModeB parent re-aim gate requires NO-mathlib-has-it once this analogous law and the actual representation bridge verify.

Zero cases are explicit: target zeroScale and zeroPolynomial compile; arbitrary projectedTransport handles empty support using φ0=0. The lift is WithTop.map(c*·), which fixes top even for c0 and therefore permits finite-inf transport uniformly. Subsequent untopD0 recovers zero. The accepted guard proof also rejects omitting zero preservation or allowing negative scaling in the same minimum law. No recovered sorryAx is accepted.

## Phase 7 — Actionable verdict

**NO-mathlib-has-it** in the more general parent representation, independently checked. Existing `map_finset_inf` is exactly functoriality of a finite support minimum under an InfTopHom. This is the appropriate re-aim of the scaling law after Roth.index's parent replacement by projected infDegree. Existing `Real.sInf_smul_of_nonneg` independently confirms the original proof's order-theoretic core. Neither a failed search nor cost establishes the verdict.

The follow-from term for the re-aimed law is the displayed one-line `map_finset_inf h f.coeff.support D`; the original quotient statement follows only after the actual bridge. This distinction is essential: no claim that the original quotient equality is itself a one-call specialization or definitionally equal is made. The required re-aim gate prevents downgrading to BORDERLINE merely because the old spelling needs normalization.

Action: during parent migration use the generic finite-inf law and the checked zero-preserving projection/reciprocal-weight adapter. At the two uses in the sole caller Roth/Theta.lean:447, the identical-type bridge replacement rewrites hUΘ and hVΘ, after which the existing positive-l inequality steps continue. If retaining the old project index name, retain the useful local law in **Roth/Index.lean**, the appropriate alternative destination, or inline its exact verified normalization proof into that caller. Deleting it in isolation and replacing `rw [index_mul_left_weights]` by raw `map_finset_inf` would not typecheck and is not the recommended plan. No new upstream PR is proposed for this redundant core law; local wrappers/adapters and broader missing APIs require their own assessments.

## Phase 8 — Evidence completion

[Assessment metadata](../evidence/Roth.index_mul_left_weights/assessment.json), [verification ledger](../evidence/Roth.index_mul_left_weights/verification.json), [portable validator](../evidence/Roth.index_mul_left_weights/validate.py) and [copy manifest](../evidence/Roth.index_mul_left_weights/copy-manifest.json) cover accepted exact sources, complete nonpartial native receipts, standard axioms only, fresh17 source/pin hashes, exact canonical293 ordered audit, all callers, all search methods and literature channels. Rejected initial probes remain separately labelled: wrong generated inf/min syntax, missing Pointwise scope and unintended WithTop arithmetic; recovered sorryAx in those attempts is excluded from accepted proof evidence. Native source preparation alone is not counted as verification. Root independently accepts and integrates the package; unresolved verification items are empty.

Root also archived a diagnostic-only persistent-session trim: [change record](../evidence/Roth.index_mul_left_weights/warm-session-trim-after-index148.json), [before](../evidence/Roth.index_mul_left_weights/warm-session-through-index148-before-trim.lean.txt), [after](../evidence/Roth.index_mul_left_weights/warm-session-index148-trimmed-executed.lean.txt), [complete post-trim native success](../evidence/Roth.index_mul_left_weights/warm-session-index148-trim-native-receipt.json). Only obsolete audit namespaces140–147 were removed; every mathematical proof and the current148 audit were retained. This is scratch maintenance, not a production change or measured speed improvement. The historical148 receipts retain their original line positions; the validator scopes assertions against those archived sources.
