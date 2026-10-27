# Roth.index_C_mul — NO-composable-from-mathlib

## Phase 0 — Doctor

The baseline `lake build` succeeded (2467 jobs, exit0). Fresh comparison of all17 source/pin hashes with the shared input manifest passes; this is reused build evidence, not a newly run build. The theorem resolves at `Roth/Index.lean:195` on the assigned branch. The original theorem, complete printed kernel body with no elision, standard axioms and fresh exact293 canonical audit were independently checked by root. There are no new axioms, proof holes, unsafe tactics, or raised limits in accepted evidence. [Baseline](../evidence/Roth.index_C_mul/baseline-build.txt), [fresh hashes](../evidence/Roth.index_C_mul/inputs.json), [original native receipt](../evidence/Roth.index_C_mul/index-c-mul-original-audit-receipt.json).

## Phase 1 — Comprehend

Multiplying a multivariate real polynomial by a nonzero real constant preserves its weighted order of vanishing at any point. The index is the infimum of the weights of exponents in the translated polynomial's support, with index0=0. Translation preserves constant multiplication; nonzero scalar multiplication preserves support, so the two infima are equal. This includes P=0 and zero entries in the natural weight vector.

Full native type:

```lean
Roth.index_C_mul.{u_1} {σ : Type u_1} [Fintype σ] {c : ℝ} (hc : c ≠ 0)
    (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) :
    Roth.index (MvPolynomial.C c * P) α r = Roth.index P α r
```

σ indexes variables; Fintype supplies the parent weight sum; c is the scalar with essential uniform hypothesis hc; P is arbitrary; α is the center; r is arbitrary natural weights. The proof uses `Roth.index`, `MvPolynomial.taylor`, its multiplication and constant laws, `MvPolynomial.smul_eq_C_mul`, and `MvPolynomial.support_smul_eq`. Only index, weight, and Taylor are project-level interfaces; the support invariant itself is mathlib. [Complete declaring module](../evidence/Roth.index_C_mul/Roth-Index.lean.txt).

## Phase 2 — Preliminary checks

SMALL: an elementary support invariance helper, not a main named theorem or new structure. One-line definition check is n/a: the declaration is a theorem; its one rewrite line does not trigger definition exemptions. No prefilter or inherited verdict was used.

## Phase 3 — Exhaustive literature

Every named channel was executed; the protocol's informal nine-channel label includes three distinct general web forms. Raw web bodies were not archived: evidence retains exact requests, response SHA256/bytes, locators and concise original summaries. No returned credential-bearing URL is retained.

| Channel | Exact query / action | Finding |
|---|---|---|
| General specific | `Roth polynomial index invariant nonzero constant multiplication` | Roth index and modern exposition; exact local source stronger than snippets. |
| General abstract | `weighted order of vanishing scalar multiplication nonzero polynomial` | Orders and weighted polynomial APIs; no exact theorem inferred from snippets. |
| General alias | `multiplicity polynomial root constant nonzero scalar invariant order vanishing` | Root multiplicity terminology, univariate analogue. |
| ChatGPT math | n/a: ask_chatgpt_math unavailable | Optional external opinion unavailable; other channels completed. |
| Local references | fresh rg for index, sign, and constant scaling in clean.tex | §4 gives ind(cP)=ind(P) for nonzero c; §5 determinant signs use it. |
| nLab | `site:ncatlab.org/nlab order of vanishing valuation unit`; open valuation page | Valuation/unit context; direct open failed400 unsupported XHTML. |
| nCatLab | `site:ncatlab.org/ncatlab weighted order vanishing scalar polynomial` | Returned nLab pages outside queried namespace; no exact nCatLab hit. |
| Stacks | `site:stacks.math.columbia.edu order vanishing unit valuation` | §10.121/tag02MB defines orders of vanishing in local algebra; contextual, not this rational-weight support theorem. |
| MathOverflow | `site:mathoverflow.net weighted order polynomial multiplicity nonzero scalar` | Weighted monomial order / polynomial vanishing discussions; no exact generality claim. |
| Recent arXiv | `site:arxiv.org weighted order vanishing polynomial 2022 2023 2024 2025 2026` | 2023–24 vanishing-polynomial and weighted approximation papers have different meanings of weight/vanishing. |
| Supplementary primary | `Roth theorem index polynomial definition weighted derivatives scaling constant` | Roth ICM1958 p206 and modern exposition define index using nonvanishing derivatives. |

[General request](../evidence/Roth.index_C_mul/web-general.json), [abstract web](../evidence/Roth.index_C_mul/web-specific.json), [alias](../evidence/Roth.index_C_mul/web-alias.json), [nLab](../evidence/Roth.index_C_mul/web-nlab.json), [nCatLab](../evidence/Roth.index_C_mul/web-ncatlab.json), [Stacks](../evidence/Roth.index_C_mul/web-stacks.json), [MO](../evidence/Roth.index_C_mul/web-mathoverflow.json), [arXiv](../evidence/Roth.index_C_mul/web-arxiv.json), [primary](../evidence/Roth.index_C_mul/web-primary.json), [local search](../evidence/Roth.index_C_mul/local-literature-search.json), [source excerpt](../evidence/Roth.index_C_mul/clean-index-excerpt.tex.txt).

The standard concept is weighted order of vanishing, also called Roth's index in this Diophantine setting. [Roth's ICM account](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf) p206 uses nonzero derivatives to define it; [Stacks orders of vanishing](https://stacks.math.columbia.edu/tag/02MB) provides broader local-algebra context. The scalar identity follows from coefficient support, rather than any order/positivity or differential analytic property. The local source's positive real weights and +∞ zero convention differ from natural weights and index0=0; the present invariance survives both conventions. General module hypotheses below are verified algebraic consequences, not a claim that the external literature states the exact Lean hierarchy.

## Phase 4a — Parameters and hypotheses

| Parameter | Current form | Audit / general target |
|---|---|---|
| σ | arbitrary universe, Fintype | Parent weight definition needs Fintype; expanded exponent type A can be arbitrary, with no finiteness instance. |
| coefficients | ℝ | Expanded degree law verified with any Semiring R, separately acted on by scalar semiring S. |
| scalar | c:ℝ | Expanded law takes c:S, Semiring S, IsDomain S, Module S R, Module.IsTorsionFree S R. No coefficient-domain assumption is required. |
| hc | c≠0 | Cannot drop uniformly: c=0, P=X, α=0, r=1 has unequal indices. IsUnit is an alternative over rings; no uncompiled weakening via regular actions is claimed. |
| P | any polynomial | No nonzero hypothesis needed; separate P=0 native guard passes for all c, including zero. |
| α | arbitrary center | Used only through Taylor algebra homomorphism and constants; no restriction needed. |
| r | arbitrary natural vector | No positivity assumption to remove; generic degree map D may be completely arbitrary. |
| degree target | ℝ with sInf and default0 | Modern law uses any SemilatticeInf T with OrderTop T; WithTop ℝ then default0 recovers the intended zero convention after the separately proved parent bridge. |

## Phase 4b — Verified generality

The fixed parent interface has no verified droppable assumptions: hc cannot be dropped, P may vanish, and r may have zero entries. There is no claim that simply omitting Fintype compiles against unchanged `Roth.index`. The expanded representation admits verified generalization to arbitrary exponent sets, degree maps, coefficient semirings, and torsion-free scalar modules. This is a restatement of the parent representation, not a single mechanical hypothesis deletion on this theorem.

The accepted isolated signature and proof are archived exactly in [mathlib-only execution](../evidence/Roth.index_C_mul/index-c-mul-mathlib-executed.lean.txt). Its `modern` theorem is new scratch proof, not an existing mathlib theorem:

```lean
[Semiring R] [Semiring S] [IsDomain S] [Module S R] [Module.IsTorsionFree S R]
[SemilatticeInf T] [OrderTop T] (D : A → T) {c : S} (hc : c ≠ 0)
(f : AddMonoidAlgebra R A) :
AddMonoidAlgebra.infDegree D (c • f) = AddMonoidAlgebra.infDegree D f
```

The support-only form further weakens coefficients to an AddCommMonoid M with the same scalar module/torsion-free hypotheses, and is an exact application of existing `Finsupp.support_smul_eq`. These are the verified library-interface assumptions, not a logical minimality claim. Scalar support invariance only needs the coefficient action at this particular c to preserve and reflect zero; injectivity suffices. A unit can act injectively even over a ring with zero divisors. Existing `Finsupp.support_mapRange_of_injective` (`Mathlib/Data/Finsupp/Defs.lean:348`) expresses the wider zero-preserving injective coefficient-map form. No uncompiled unit/regular-action theorem or mechanical weakening is claimed; that broader interface is a separate optional API design. All signatures and standard axioms compile. [Receipt](../evidence/Roth.index_C_mul/index-c-mul-mathlib-receipt.json).

## Phase 4c — Nine modern-idiom checks

| # | Diagnostic | Result / consequence |
|---|---|---|
| 1 | Hypotheses to typeclasses | Yes in expanded representation: Module and Module.IsTorsionFree express reusable scalar injectivity; hc remains a scalar-specific premise. |
| 2 | Sequences to filters | No topology or convergence. |
| 3 | Universal property | No object constructed; existing Taylor hom structure already handles multiplication. |
| 4 | Bundled substructure | No closure subset; no Submodule replacement needed. |
| 5 | Field to module hierarchy | Yes: arbitrary coefficient Semiring R and torsion-free S-module; supports scalar restriction and finitely supported module APIs. |
| 6 | Higher categories | No categorical content. |
| 7 | Concrete ordered index | Yes: arbitrary A→T with SemilatticeInf/OrderTop; works with nonnumerical gradings and OrderDual supDegree too. |
| 8 | Concrete-via-abstract | Fires: after index unfolds, the one proof line contains no ℝ, σ, α or r identifier. Content is scalar support invariance; Taylor and weight only transport it. |
| 9 | False generalization guard | Pass for scalar support/degree law. Reject dropping nonzero/regularity, reject omitting default0 in old-form zero cases; do not identify arbitrary-weight infDegree with natural weightedOrder without a bridge. |

Modern idiom available: yes; a scalar invariance law adjacent to degree negation could simplify every degree consumer of coefficient support invariance. This has concrete algebraic reach beyond Roth, and a fresh explicit congruence term proves the law using existing support_smul_eq alone. This is a genuine composition, independent of the earlier simp diagnostic.

## Phase 4.5 — Infrastructure risk

n/a — theorem, not def/class/instance. It creates no instance path, definitional alias, coercion, universe data structure, priority collision, or reducibility rule. The six infrastructure risks are theorem n/a; no new definition is proposed here.

## Phase 4.6 — Proof strategy

| # | Question | Result |
|---|---|---|
| 1 | Topology via filters | No topology. |
| 2 | Element algebra to bundled inclusions | Already support-level equality; no element chase. |
| 3 | Analysis sequences to nets | No analysis. |
| 4 | Construction to universal property | No construction. |
| 5 | Helper mathlib should have | Optional named `infDegree_smul` / dual `supDegree_smul`; exact named analogue not identified, but support_smul_eq already handles substance. |

MATHLIB-IDIOMATIC for current local adapter. Re-aiming to generic degree would remove Taylor/real/natural-weight baggage in a prospective upstream statement. No cost-based verdict downgrade is used.

## Phase 5 — Five actual mathlib methods

All five methods ran on current, literature-standard, and abstract forms. [All formal requests and complete raw receipts](../evidence/Roth.index_C_mul/formal-search.json); source rg receipts [current](../evidence/Roth.index_C_mul/rg-current.json), [literature](../evidence/Roth.index_C_mul/rg-literature.json), [abstract](../evidence/Roth.index_C_mul/rg-abstract.json).

| Form | Finder | Loogle | LeanSearch | rg | Local name index |
|---|---|---|---|---|---|
| Current Taylor/index C_mul | Taylor multiplication/context, no index law | support_smul_eq hit | smul_eval/root scalar laws | support_smul_eq hit | Roth target plus old scratch; index unavailable |
| Weighted order/nonzero unit | le_weightedOrder_smul, weightedOrder_mul | inequality only | inequality and homogeneous C_mul | no exact weightedOrder_smul equality | empty, index unavailable |
| Abstract degree/scalar | infDegree and support_single_mul | Finsupp.support_smul_eq | Finsupp and MvPolynomial support_smul_eq | no degree_smul name; generic support law | empty, index unavailable |

Pinned positives were read and compiled independently: `Finsupp.support_smul_eq` at `Mathlib/Data/Finsupp/SMul.lean:137`, `MvPolynomial.support_smul_eq` at `Mathlib/Algebra/MvPolynomial/Basic.lean:700`, and `AddMonoidAlgebra.coeff_smul` in `Mathlib/Algebra/MonoidAlgebra/Defs.lean`. The infDegree definition is at `Mathlib/Algebra/MonoidAlgebra/Degree.lean:624`. External search indexes may differ from this pin. Local index unavailable and name-negative checks do not prove global absence. The independently compiled generic scratch law demonstrates the support route, not that a named analogous degree law already exists. No absence claim is based solely on search failure.

## Phase 5.5 — Statement shape

Normal form: constant multiplication is appropriate for the sole determinant sign caller; scalar action is canonical for the abstract law. Both normalize toward the original polynomial on the RHS. A support equality is the existing canonical primitive, and infDegree is the appropriate parent re-aim. Syntactic generality: compare `C c * P`, `c • P`, and generic `c • f`; existing `smul_eq_C_mul` handles the first two, and `modern` compiles the third. No extra P≠0, positivity of r, or center restriction is appropriate. Fintype remains fixed by parent, not an unused hypothesis freely deletable here. hc is essential by the compiled X guard. Overall: SHIP-AS-STATED as local adapter; RESTATE-BEFORE-SHIP for any upstream degree/scalar API.

## Phase 6.0 — Complete caller and inline audit

Internal uses:1; external-to-declaring-file modules:1; statement uses:0; body applications:1. Fresh canonical inventory enumeration, no-ignore rg and tracked git grep agree.

| Caller | Usage | Concrete refactor / fallback |
|---|---|---|
| Roth.sum_max_sub_le_index_det, Roth/Theta.lean:405 | remove permutation sign from each determinant summand's index, using nonzero sign cast | Keep local adapter while parent index remains. If inlining chosen, replace this call at local hidx with the exact support-normalization proof, preserving map_intCast coercion normalization. Full original caller replay using the independent replacement was prepared and checked. |

The fresh exact293 ordered kernel audit finds this same sole direct consumer. That count concerns direct kernel values only, not transitive/simp dependency closure. The broader inline scan finds index_neg as a related special case and this sign passage; no additional independent scalar-index rederivation was identified. This theorem is genuinely used, not dead. [Caller table](../evidence/Roth.index_C_mul/callers.json), [enumeration](../evidence/Roth.index_C_mul/lexical-enumeration.json), [complete searches](../evidence/Roth.index_C_mul/complete-caller-search.json), [inline scan](../evidence/Roth.index_C_mul/rg-inline.json), [caller preparation](../evidence/Roth.index_C_mul/caller-probe-prep.lean.txt).

## Phase 6 — Composition experiments and parent re-aim

Original-form independent replacement compiles:

```lean
by
  rw [index, index, map_mul, taylor_C, ← smul_eq_C_mul, support_smul_eq hc]
```

This has a project definition, generic multiplication rewrite, project Taylor constant law, scalar conversion, and existing support law. It is not falsely counted as a three-existing-call term, and it is not an exact existing mathlib declaration for index. The zero-polynomial case holds even for c=0. Dropping hc uniformly fails, as native zeroScalarGuard proves with P=X over Unit, center0 and unit weights. The initial guard omitted `support_X`; that rejected diagnostic is retained separately and never counted as success. [Accepted target execution](../evidence/Roth.index_C_mul/index-c-mul-target-clean-executed.lean.txt), [accepted target receipt](../evidence/Roth.index_C_mul/index-c-mul-target-clean-receipt.json).

Parent Roth.index was assessed NO-mathlib-has-it via projected infDegree. We independently re-aimed here, rather than inheriting NO. Unlike the preceding negation theorem, no analogous named scalar degree law was identified in the pin. The first independently compiled modern proof closed by `simp only [AddMonoidAlgebra.infDegree, AddMonoidAlgebra.coeff_smul, Finsupp.support_smul_eq hc]`. In isolation that is Phase6b's BORDERLINE trivial simp diagnostic; it is not an exact named law and not automatically a NO composition.

A fresh explicit composition then compiled independently, with `fail_if_success exact?` confirming one-step tactic search did not already close the goal:

```lean
by
  classical
  exact congrArg (fun s : Finset A ↦ s.inf D)
    (Finsupp.support_smul_eq hc (g := f.coeff))
```

Here the only substantive existing mathlib theorem is support_smul_eq; core congrArg transports its equality through Finset.inf. The degree/coeff scalar identities match definitionally, with no rewriting, normalization proof, new helper premise or imported project target. This meets Phase6a's ≤3-existing-call composition bar. `exact?` failure is evidence about that search attempt, not global absence. [Exact composition source](../evidence/Roth.index_C_mul/index-c-mul-explicit-composition-executed.lean.txt), [raw receipt](../evidence/Roth.index_C_mul/index-c-mul-explicit-composition-receipt.json).

Root also checked actual original-form transport through the retained canonical133 bridge, Taylor multiplication/constant/scalar conversion, and this exact support congruence under `WithTop.untopD 0`. The bridge is a genuine previously proved normalization theorem; it is not falsely counted as a mathlib building block. [Bridge source](../evidence/Roth.index_C_mul/index-c-mul-bridge-executed.lean.txt), [receipt](../evidence/Roth.index_C_mul/index-c-mul-bridge-receipt.json). The full sole caller replay preserves its original statement and all parameters, changing only the target call to the independently proved fallback replacement. [Caller execution](../evidence/Roth.index_C_mul/index-c-mul-caller-executed.lean.txt), [receipt](../evidence/Roth.index_C_mul/index-c-mul-caller-receipt.json).

A natural weightedOrder_mul route is contextual and needs translation, natural-weight conversion and zero handling; it does not supply the arbitrary-weight, no-positivity parent law as a one-call replacement. No full migration of all index consumers to a new generic representation is claimed.

## Phase 7 — Actionable verdict

**NO-composable-from-mathlib**, evaluated on the properly re-aimed parent degree law. The substantive existing building block is `Finsupp.support_smul_eq`, at `Mathlib/Data/Finsupp/SMul.lean:137`; equality transport uses core congrArg. The fresh explicit term above makes the verdict rest on genuine ≤3-call composition, rather than on the earlier closing-simp diagnostic. No named infDegree scalar law is falsely claimed to exist; this is not NO-mathlib-has-it. The old-form Roth theorem still needs the genuine parent bridge and Taylor normalization, and is not claimed to be a ≤3-mathlib-call term.

Every explicit caller refactor plan: at the sole `Roth/Theta.lean:405` application inside `sum_max_sub_le_index_det`, retain `map_intCast` normalization and substitute the verified original-form replacement proof in local hidx if deleting the wrapper while retaining the old parent. The full caller replay proves this interface. With parent index migrated to the canonical infDegree representation, use the explicit support_smul_eq congruence under default0 projection after Taylor scalar normalization; the bridge execution demonstrates that transport. Do not simply replace the old call by support_smul_eq without these representation steps.

Alternative local destination: `Roth/Index.lean` is the appropriate compatibility-adapter home while the zero-default Taylor index remains. It may reasonably remain there during a staged parent refactor; this assessment recommends against upstreaming the concrete real/Taylor specialization. If contributors later want named generic degree scalar laws beside supDegree_neg, that is optional API convenience, not missing mathematical substance. The coefficient-action regularity / unit interface is separately worth designing and compiling before claiming a stronger upstream law. No production files or Git state were changed by this assessment.

## Phase 8 — Evidence and completion

The package includes exact unchanged executed source, raw native receipts, source/pin hashes, all search channels, caller replay, full canonical ordered audit and portable validation. Accepted proofs use only propext, Classical.choice and Quot.sound. Partial responses and rejected attempts are not successes. Verification unresolved[] is empty; optional future naming or regular-action design does not block this read-only assessment. [Verification index](../evidence/Roth.index_C_mul/verification.json), [portable validator](../evidence/Roth.index_C_mul/validate.py).
