# Roth.abs_coeff_le_normOne — full mathlibable assessment

Verdict: **NO-mathlib-has-it**. The exact current statement is a direct specialization of `Finsupp.single_eval_le_sum`, not a new sum estimate. Fresh isolated, project-target, complete-caller and expanded-generality native checks all pass. This is declaration **81/293**, independently assessed; no inherited verdict is used.

## Phase 0 — Baseline and identity

`Roth/CoeffNorm.lean:71–73` is a public theorem without `sorry` or a simp attribute. The entire declaring module was read: it builds integer multivariate coefficient ℓ1 estimates, Hasse derivative/determinant bounds and diagonal/evaluation bounds. The reusable baseline `lake build` exited0 with2467 jobs; **all17** source/pin hashes freshly match its shared manifest. This reuse is justified by those hashes, not by the old commit label alone. Mathlib candidate files are separately hashed. No production source, pins, Git or progress records were edited.

Evidence: [baseline](../evidence/Roth.abs_coeff_le_normOne/baseline-build.txt), [fresh input checks](../evidence/Roth.abs_coeff_le_normOne/inputs.json), [input result](../evidence/Roth.abs_coeff_le_normOne/input-hash-check.json), [complete module](../evidence/Roth.abs_coeff_le_normOne/source-module.lean.txt), [canonical row](../evidence/Roth.abs_coeff_le_normOne/canonical-entry.json), [mathlib hashes](../evidence/Roth.abs_coeff_le_normOne/mathlib-inputs.json).

## Phase 1 — Statement and proof

For an integer polynomial in an arbitrary type of variables, the absolute real value of any one coefficient is bounded by the sum of absolute real values of all coefficients. Only finitely many coefficients are nonzero. The proof says a nonnegative summand is bounded by the whole finite sum; an exponent outside support has zero coefficient.

Full native type:

```lean
∀ {σ : Type u_2} (P : MvPolynomial σ ℤ) (d : σ →₀ ℕ),
  |↑(P.coeff d)| ≤ Roth.normOne P
```

`σ` is an arbitrary universe-polymorphic variable index; `P` is arbitrary; `d` is an arbitrary finitely supported exponent vector. There are **no explicit hypotheses or typeclasses** on `σ`. The coefficient domain and output are fixed to integers and reals by `normOne`. `Roth.normOne` is a statement dependency; the proof itself applies mathlib directly, using its transparent coefficient-sum representation. The parent assessment is historical context, not a substitute for this proof check.

Fresh [target source](../evidence/Roth.abs_coeff_le_normOne/native-target-executed.lean.txt) and [full native receipt](../evidence/Roth.abs_coeff_le_normOne/native-target-success.json) capture type, proof, axioms and direct replacement. Root owns the persistent native session; these receipts can include earlier declarations, but the archived exact appended source identifies the fresh81 segment. Declaration75 had previously proved a coefficient bound; it is **historical prerequisite only**, not fresh81 execution.

## Phase 2 — Size and one-line check

**SMALL**: an elementary coordinate bound serving the determinant theorem, not a new structure, named theorem or project main result. The definition-only one-line/exemption check is **n/a: theorem**. Its actual body is already one generic application; that fact is investigated independently below. Exhaustive literature/search phases still run.

## Phase 3 — Exhaustive literature

Each actual query is retained verbatim in the linked metadata receipts. Response SHA256/UTF8 byte counts, URLs, original summaries and access limitations are retained; full search/article bodies are not archived. Returned URL query components were removed from metadata, with the redaction documented.

| Channel | Actual query or locator | Result and relevance |
|---|---|---|
| General web: specific | `polynomial coefficient absolute value bounded sum absolute coefficients l1 norm` | Coefficient ℓ1 norm terminology; MathWorld/MSE are supplementary terminology only. |
| General web: common norm alias | `finite sequence maximum norm less than one norm inequality` | Finite vector norm comparisons, including UCSD matrix norm notes. Coordinate dominance is the elementary finite-family form. |
| General web: abstract | `finitely supported function nonnegative summand bounded by sum ordered monoid` | IsarMathLib finitely supported monoid-valued functions supplies primary formal context; not claimed to state the exact Lean target. |
| ChatGPT math | `ask_chatgpt_math` | **n/a: unavailable** in callable tools. No historical-formulation answer invented. |
| Local clean.tex | Lines438–499, Lemma3 proof and Lean note | Defines coefficient maximum and coefficient sum; proof bounds `abc(F)` by ℓ1 sum; Lean note specifically requests this elementary inequality. |
| nLab | `site:ncatlab.org/nlab l1 norm sequence` | p-norm/sequence-space pages identified. Direct p-norm fetch failed unsupported XHTML; no claim to have read inaccessible body. |
| nCatLab | `site:ncatlab.org/ncatlab normed vector space sum` | Mostly nLab-related results; direct nCatLab URL inaccessible. No relevant higher-categorical formulation established. |
| Stacks | `site:stacks.math.columbia.edu norm polynomial coefficient sum` | Opened tag0BIH, Lemma9.20.3 lines23–29: field norm/trace of algebraic elements, a different meaning of norm, not this coefficient bound. |
| MathOverflow | `site:mathoverflow.net polynomial l1 norm coefficients` | Opened question465899, lines32–35: explicitly uses sum of absolute ordinary monomial coefficients on ℤ[x]; its multiple-minimization problem is distinct. |
| Recent arXiv | `site:arxiv.org polynomial coefficient l1 norm after:2021-10-27 before:2026-10-28` | Opened Feng–Zhang arXiv2506.06880 (submitted7June2025), abstract lines16–19: sparse polynomial ℓ1 minimization/approximation. Context, not a stronger elementary coordinate bound. Off-topic/older hits excluded. |

Evidence: [three general queries](../evidence/Roth.abs_coeff_le_normOne/web-0.json), [nLab/nCatLab](../evidence/Roth.abs_coeff_le_normOne/web-1.json), [Stacks/MO](../evidence/Roth.abs_coeff_le_normOne/web-2.json), [recent arXiv](../evidence/Roth.abs_coeff_le_normOne/web-3.json), [primary opens and limitations](../evidence/Roth.abs_coeff_le_normOne/web-4.json), [local excerpt](../evidence/Roth.abs_coeff_le_normOne/local-literature.txt), [local hash/locator](../evidence/Roth.abs_coeff_le_normOne/local-literature-source.json), [exact local search](../evidence/Roth.abs_coeff_le_normOne/rg-local-literature.json).

The standard mathematical content is coordinate domination by the coefficient ℓ1 norm, equivalently the finite-family ℓ∞≤ℓ1 estimate. Polynomial texts vary between one and several variables and real/complex/integer coefficients, while the elementary proof only needs nonnegative summands. The most abstract order-sum form here is grounded in the pinned mathlib law itself. No source disagreement about the coefficient-sum meaning was found; analytic L1 norms of functions and field-extension norms are explicitly different concepts. Primary mathematical context: [IsarMathLib finitely supported functions](https://isarmathlib.org/FinSupp_ZF.html), [UCSD matrix norm notes, chapter9](https://mathweb.ucsd.edu/~njw/Teaching/Su24_170A/Borgers_Book/Borgers_Chap09.pdf), [Feng–Zhang abstract](https://arxiv.org/abs/2506.06880). The local source directly supplies the project's exact use.

## Phase 4a — Parameter and generality audit

| Parameter/hypothesis | Current form | General form and evidence |
|---|---|---|
| Variable index | `σ : Type*`, no finiteness | Already arbitrary; replacing polynomial exponent index by arbitrary `α` is an expanded representation, verified `generic`. |
| Polynomial | `P : MvPolynomial σ ℤ` | Only `P.coeff : (σ →₀ ℕ) →₀ ℤ` is used. Arbitrary `f : α →₀ M` with `[Zero M]` verified. No multiplication, degree or ring operation used. |
| Exponent | `d : σ →₀ ℕ` | Any coordinate `a : α` in the expanded family; no support membership needed. |
| Coefficient size | `|(z : ℝ)|` for `z : ℤ` | Arbitrary zero-preserving, globally nonnegative `g : M → N` in existing mathlib. Cast order/linearity is not used by the generic proof. |
| Sum output/order | ℝ | Existing law requires `[AddCommMonoid N] [PartialOrder N] [IsOrderedAddMonoid N]`; not falsely reported as only a preorder. |
| Absolute value variant | Integer-real cast | Fresh `orderedAbs` works over `[AddCommGroup G] [Lattice G] [IsOrderedAddMonoid G]`; linear order and field are unnecessary for that expanded variant. |
| Explicit assumptions | None | Nothing to drop in the original type. Fixed `normOne` interface still fixes integers/reals. |

Existing exact general law, pinned source `Mathlib/Data/Finsupp/Order.lean:165–170`:

```lean
∀ {α M N : Type*} [Zero M] [AddCommMonoid N] [PartialOrder N]
  [IsOrderedAddMonoid N] (f : α →₀ M) {g : M → N},
  g 0 = 0 → (∀ m, 0 ≤ g m) → ∀ a,
  g (f a) ≤ f.sum (fun _ m ↦ g m)
```

## Phase 4b — Verified generality verdict

**MAXIMALLY GENERAL within the fixed parent `normOne` signature**; there is no hypothesis to weaken in place. **STRICTLY NARROWER in expanded representation** than the existing arbitrary finitely supported family law, with all stated expansions actually compiled. This does not require a new project helper: existing `Finsupp.single_eval_le_sum` already supplies the full original theorem.

We also tested beyond the existing law rather than assuming its hypotheses minimal. The fresh raw set proves a new `preorderGeneric` using `[Preorder N] [IsOrderedAddMonoid N]`. The final isolated general set proves the stronger **new helper**:

```lean
theorem supportLocal {α M N : Type*} [Zero M] [AddCommMonoid N] [Preorder N]
    [AddLeftMono N] (f : α →₀ M) {g : M → N} (hg : g 0 = 0)
    (h : ∀ i ∈ f.support, 0 ≤ g (f i)) (a : α) :
    g (f a) ≤ f.sum (fun _ m ↦ g m)
```

It splits on support membership and applies `Finset.single_le_sum` or rewrites an off-support coefficient to zero before `Finset.sum_nonneg`. Thus antisymmetry, full ordered-add-monoid structure and global nonnegativity are not needed for this expanded support-local version. **This is a new proof witness, not an existing mathlib replacement or a claim of absolutely weakest assumptions.** It does not turn this exact original mathlib hit into a YES/BORDERLINE result. A separate proposed generalization of the existing upstream law would need its own scope and assessment; no novelty/absence claim is made for it here. These expansions cost a short proof; cost does not decide the verdict.

Dropping zero-preservation entirely fails for the empty support with a positive value at zero. Dropping all nonnegativity fails for a two-term family whose second transformed coefficient is negative. Those semantic guards are elementary counterexamples, not claims of new Lean-executed counterexample theorems.

Evidence: [guarded mathlib-only raw source](../evidence/Roth.abs_coeff_le_normOne/native-raw-executed.lean.txt), [raw receipt](../evidence/Roth.abs_coeff_le_normOne/native-raw-success.json), [support-local source](../evidence/Roth.abs_coeff_le_normOne/native-general-executed.lean.txt), [general receipt](../evidence/Roth.abs_coeff_le_normOne/native-general-success.json).

## Phase 4c — Nine modern-idiom checks

| # | Question | Finding and concrete consequence |
|---|---|---|
| 1 | Typeclasses instead of preambles | No unbundled structure assumptions in original. Expanded target uses canonical Zero/additive/order classes already in existing law. |
| 2 | Filters instead of sequences | No limits or convergence; finite support, not sequential approximation. |
| 3 | Universal property | No object construction to characterize; coordinate bound already generic. |
| 4 | Bundled substructures | Already bundled MvPolynomial/Finsupp; no set-with-closure predicate. |
| 5 | Weaker algebraic hierarchy | Yes in expanded representation: multiplication/rings are unused. Arbitrary Zero M and ordered additive N compile and serve non-polynomial finite families. |
| 6 | Higher categorical form | No categorical structure in inequality; nCatLab search supplies no concrete downstream benefit. |
| 7 | Concrete index/ordered structures | σ already arbitrary; coefficients/output ℤ/ℝ can expand to M/N. Lattice-ordered additive-group absolute values compile without field/linear-order assumptions. |
| 8 | Concrete-via-abstract diagnostic | **Yes**: in the one-line body `normOne` and `MvPolynomial` occur zero times; only coefficient-family projection remains. Compiled `generic` is the abstract restatement, and `raw` is its existing-law specialization. Enables finite families beyond polynomials and arbitrary zero-preserving nonnegative sizes. |
| 9 | False-generalization guard | **No false generalization in accepted expansions**: specialize α=(σ→₀ℕ), M=ℤ, N=ℝ, f=P.coeff, g=cast absolute value to recover exact original. No claim that analytic integral L1 or field norm is the same object. |

Modern-idiom verdict: **existing abstraction already available**, with direct downstream applications: `Main.lean:424` uses its univariate version; mathlib height bounds at `NumberTheory/Height/MvPolynomial.lean:277` use the same law for absolute values. Replacing the generic finite sum with a new categorical formulation would add no evidenced capability. WithLp/lp coordinate bounds are related analytical interfaces but unnecessary for this purely finite ordered-sum proof; no unverified norm-instance bridge is asserted.

## Phase 4.5 — Infrastructure risk

**n/a: theorem introduces no definitions, classes or instances.** Each infrastructure risk is explicitly accounted for: (1) no new instance diamond; (2) no new reducible definition; (3) no unfolding/simp declaration is installed; (4) no instance-priority choice; (5) `σ` stays universe-polymorphic, and isolated generic α/M/N are independently polymorphic; (6) no coercion is declared, only the existing integer-real cast used. The transparent parent `normOne` bridge is checked in native target/raw proofs rather than assumed from typography.

## Phase 4.6 — Five proof-strategy checks

| # | Strategy question | Result |
|---|---|---|
| 1 | ε–δ versus filters | n/a: no topology proof. |
| 2 | Elements versus ideals/submodules | No improvement: coefficient coordinate/order sum is appropriate; no closure assertion. |
| 3 | Sequences versus nets | n/a: finite support sum only. |
| 4 | Constructed object versus universal property | n/a: no constructed categorical object. |
| 5 | Missing helper mathlib should have | None for original. It directly applies existing exact law. Optional broader support-local law has a new proof, not a prerequisite. |

Verdict: **MATHLIB-IDIOMATIC current proof**; local theorem itself is a redundant specialization. Caller inlining is CHEAP; this cost observation is not the reason for the verdict.

## Phase 5 — Five actual mathlib methods × three forms

Current form: integer multivariate coefficient absolute value ≤ coefficient absolute sum. Literature-standard form: finite-family coordinate norm ≤ ℓ1 norm. Abstract form: zero-preserving nonnegative `g(f a)` ≤ `Finsupp.sum g`.

| Method | Current | Standard | Abstract |
|---|---|---|---|
| Lean-Finder | Chevalley/Dioph/CauchyBound noise | `PiLp.norm_apply_le`, `lp.norm_apply_le_norm` | `Finsupp.sum_le_sum`, `Finsupp.sum_nonneg` |
| Loogle | Initial unknown identifier; rate-limited retry; corrected quoted-name query succeeds with nearby coefficient lemmas | Finsupp support-related results | `Finsupp.sum_of_support_subset` and related results |
| LeanSearch | Mahler measure coefficient-sum bound, coefficients | PiLp/lp coordinate bounds | Finsupp.sum and support-subset sum |
| rg pinned source | Polynomial coefficient/norm candidates | Finds exact `single_eval_le_sum` | Finds exact law plus `single_le_sum`; existing height use |
| Local name search | Own abs_coeff family | **Finsupp.single_eval_le_sum** | **Finsupp.single_le_sum** |

All12 initial formal calls, failed Loogle attempts, and corrected successful query are retained; external indexes can differ from the pin. Local method reports **index unavailable**, with source fallback returning the listed hits; this is presence evidence, never an absence proof. Source rg ran untruncated full-qualified-name check, current, standard and abstract searches. The named project theorem is absent from mathlib under its Roth-qualified spelling, but the generic theorem is demonstrably present, so that name search is not mistaken for mathematical novelty.

Evidence: [formal request inventory](../evidence/Roth.abs_coeff_le_normOne/formal-search.json), [local exact hit](../evidence/Roth.abs_coeff_le_normOne/lean_local_search-standard.json), [corrected Loogle receipt](../evidence/Roth.abs_coeff_le_normOne/lean_loogle-current-corrected.json), [current rg](../evidence/Roth.abs_coeff_le_normOne/rg-current.json), [standard rg](../evidence/Roth.abs_coeff_le_normOne/rg-literature.json), [abstract rg](../evidence/Roth.abs_coeff_le_normOne/rg-abstract.json), [full name rg](../evidence/Roth.abs_coeff_le_normOne/rg-full-name.json), [pinned exact theorem and proof](../evidence/Roth.abs_coeff_le_normOne/mathlib-finsupp-order.lean.txt), [existing height application](../evidence/Roth.abs_coeff_le_normOne/mathlib-height-excerpt.lean.txt).

Positive candidate checked natively: **Finsupp.single_eval_le_sum** (`Mathlib/Data/Finsupp/Order.lean:165`). Its proof uses `sum_single_index` and `single_le_sum`. The latter is a related more index-dependent sum bound, not needed in our exact replacement. `Finset.single_le_sum` and `Finset.sum_nonneg` are the primitives used only in the new exploratory stronger proof, not silently counted as an existing one-call generalized law. Search conclusion: **found in mathlib as Finsupp.single_eval_le_sum**.

## Phase 5.5 — All three statement-shape checks

**Normal form:** equivalent presentations are support Finset sum, Finsupp.sum of coefficient-size function, and coefficient ℓ∞≤ℓ1 coordinate estimate. The canonical reusable order-sum form is existing `Finsupp.single_eval_le_sum`. Original RHS `normOne P` unfolds definitionally to that sum. No new cross-representation equivalence or normalization premise is required; the exact term elaborates without `rw` or a closing simp composition. RHS convention is respected for this inequality.

**Syntactic generality:** attempted direct old-form application, fully arbitrary Finsupp law, lattice absolute-value form, preorder version and support-local/AddLeftMono version; all compiled. Choose direct existing law at the sole caller, with an explicit `g` lambda to guide coercion inference. Do not change the polynomial caller to a normed-space interface merely for presentation.

**Superfluous arguments:** σ determines exponent type and polynomial and is already implicit; P supplies coefficients/support; d selects the coordinate; all three are essential and no explicit hypothesis/class is removable. ℤ/ℝ are fixed by the parent, not accidental extra typeclasses. Generic nonnegativity can be localized and order classes weakened only in the separately tested expanded statement.

Overall: **SHIP-AS-STATED mathematically; use existing generic API instead of upstreaming this wrapper**. No orthogonal equivalence, redundant explicit argument or shape defect needs repair first.

## Phase 6.0 — Complete explicit callers and inline audit

Named source caller count **1**, all within declaring file; internal-use count **excluding declaring file0**, external-to-file refs0. These counts exclude the declaration itself and distinguish source references from opaque kernel/simp dependency closure. The theorem is not tagged simp, but no dead-code conclusion is drawn from that fact.

| Caller | Usage | Exact refactor |
|---|---|---|
| `Roth.abs_coeff_det_hasseDeriv_le`, `Roth/CoeffNorm.lean:266` | First coefficient-to-norm step `abs_coeff_le_normOne _ _` | Replace with `Finsupp.single_eval_le_sum _ (g := fun z : ℤ ↦ |(z : ℝ)|) (by simp) (fun _ ↦ abs_nonneg _) _`. Expected coefficient family and exponent are inferred from the calc target. |

Inline-derivation grep finds `Roth/Main.lean:424`: the private Roth-parameter construction bounds univariate polynomial coefficients using `Finsupp.single_eval_le_sum f.toFinsupp.coeff ...` and transitivity. It is an **analogous separate application**, not a call to this theorem; no modification is needed. The surrounding proof was read to identify its exact role. Mathlib's own height application is independent corroboration of the generic abstraction.

Evidence: [caller table](../evidence/Roth.abs_coeff_le_normOne/callers.json), [exact refs](../evidence/Roth.abs_coeff_le_normOne/rg-callers.json), [inline search](../evidence/Roth.abs_coeff_le_normOne/rg-inline.json), [Main context](../evidence/Roth.abs_coeff_le_normOne/inline-main.lean.txt).

## Phase 6 — Actual composition and caller experiment

**COMPOSABLE, stronger exact-hit result:** one invocation of the existing generic law, with zero-preservation and nonnegativity supplied by existing abs facts:

```lean
example {σ : Type*} (P : MvPolynomial σ ℤ) (d : σ →₀ ℕ) :
    |((P.coeff d : ℤ) : ℝ)| ≤ Roth.normOne P :=
  Finsupp.single_eval_le_sum P.coeff (g := fun z ↦ |(z : ℝ)|) (by simp) (fun _ ↦ abs_nonneg _) d
```

The `by simp` here only discharges `g 0 = 0`, not the target inequality. The whole goal is not solved by `simp [defs...]`; Phase6b's borderline heuristic for a closing simp composition does not apply. The representation bridge is **definitional and verified**, in contrast to a merely proposed normalization proof. Parent project lemmas are not counted as mathlib building blocks.

The guarded raw proof independently clones the coefficient sum with no Roth imports and `#check_failure Roth.abs_coeff_le_normOne`. Target proof checks exact existing definition. The **entire sole determinant consumer proof body** was freshly replayed with only the coefficient edge changed to the direct generic law; its surrounding degree/support/determinant/Hasse estimates remain the source proof frontier. It does not call the assessed theorem. The changed edge itself is additionally isolated in raw proof, avoiding circular reliance through the loaded imported target. Fresh support-local generality is separately isolated and guarded.

Evidence: [full caller source](../evidence/Roth.abs_coeff_le_normOne/native-consumers-executed.lean.txt), [full caller native receipt](../evidence/Roth.abs_coeff_le_normOne/native-consumers-success.json), [four accepted native sets](../evidence/Roth.abs_coeff_le_normOne/verification.json). Every set completes successfully without errors/warnings, partial elaboration, timeout, sorry, extra axioms or raised limits. Only standard `propext`, `Classical.choice`, `Quot.sound` are observed. No rejected native81 attempts exist. Search identifier/rate failures are search receipts, not native proof rejections.

## Phase 7 — Verdict, rationale and action

**NO-mathlib-has-it**: pinned `Finsupp.single_eval_le_sum` already states the abstract coordinate bound and specializes to the current theorem exactly. Fresh isolated and target checks verify that specialization; full fresh sole-caller replay verifies practical inlining. The verdict follows actual positive evidence, not the parent's NO-composable verdict, literature absence, local-index availability, cost, or an unsupported claim that the strongest tested helper is already upstream.

During an authorized source cleanup, delete `Roth.abs_coeff_le_normOne` and replace **the one** named call at `Roth/CoeffNorm.lean:266` with the displayed exact generic call. Document direct reliance on `Finsupp.single_eval_le_sum` in that module's mathlib-usage notes if updating its documentation. There are no other explicit callers to refactor; the independent Main application already uses mathlib. Alternative destination if a teaching-oriented named convenience is retained: **project-local `Roth/CoeffNorm.lean`**, because its spelling organizes the source proof but contributes no missing generic theorem. No production deletion/refactor is performed by this assessment.

The optional `supportLocal` strengthening is an independently verified potential improvement to an existing generic theorem, not the theorem assigned here. It does not warrant reclassifying this already-present original result. YES-only PR-title/path/grouping/reviewer requirements are n/a; no upstream submission is proposed for the wrapper. No human design question blocks this NO verdict.

## Phase 8 — Completion and validation

All mandatory phases are PASS, with the justified theorem-only infrastructure/definition exemptions recorded. Four fresh accepted exact native sets, full formal-search receipts, literature metadata, source/caller/pin hashes and portable links are packaged. [Assessment](../evidence/Roth.abs_coeff_le_normOne/assessment.json), [overview entry with full type](../evidence/Roth.abs_coeff_le_normOne/overview-entry.json), [read-only portable validator](../evidence/Roth.abs_coeff_le_normOne/validate.py), [current copy manifest](../evidence/Roth.abs_coeff_le_normOne/copy-manifest.json). Root acceptance is pending independent review. The validator checks current manifests in scratch/integrated layouts and permits root's integration-only acceptance record without skipping hashes of existing evidence.
