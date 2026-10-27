# Roth.wronskian_eq_zero_iff

**Verdict: BORDERLINE-needs-human.** This is the named n-ary polynomial Wronskian criterion, and a main public result of the module. Its short proof packages two project theorems; those are not existing mathlib building blocks. The upstream decision concerns the n-ary Wronskian foundation and its coefficient-ring interface, not proof length or computational cost.

## Phase 0 — Doctor

Canonical declaration 52 resolves at `Roth/Wronskian.lean:219`, on the assigned `ramin-cleanup` branch. [Canonical entry](../evidence/Roth.wronskian_eq_zero_iff/canonical-entry.json). The reusable successful baseline has all 17 source/pin hashes freshly matched: [baseline](../evidence/Roth.wronskian_eq_zero_iff/baseline-build.txt), [manifest](../evidence/Roth.wronskian_eq_zero_iff/input-manifest.json), [fresh check](../evidence/Roth.wronskian_eq_zero_iff/input-hash-check.json). Additionally, the root ran a fresh full `lake build` at completion of this file: exit 0, all 2467 jobs, no warnings/errors, 6.425 seconds. [Exact log](../evidence/Roth.wronskian_eq_zero_iff/file-milestone-build.txt), [receipt](../evidence/Roth.wronskian_eq_zero_iff/file-milestone-build.json). This verifies the unchanged production repository, not a migrated domain API.

Kind: theorem; no sorry. The target's native type/axioms and original proof replay succeeded completely: [exact executed source](../evidence/Roth.wronskian_eq_zero_iff/native-target-executed.lean.txt), [raw complete receipt](../evidence/Roth.wronskian_eq_zero_iff/native-target-success.json). Only `propext`, `Classical.choice`, `Quot.sound` occur. Full persistent snapshots intentionally preserve earlier declarations and their diagnostics; no partial/warming response is accepted.

The entire declaring module and the modules using the constituent criterion were read: [Wronskian](../evidence/Roth.wronskian_eq_zero_iff/Wronskian-module.lean.txt), [GenWronskian](../evidence/Roth.wronskian_eq_zero_iff/GenWronskian-module.lean.txt), [Separation](../evidence/Roth.wronskian_eq_zero_iff/Separation-module.lean.txt). Whole-project source searches supply the caller and inline inventory below.

## Phase 1 — Comprehend

For any finite family of univariate polynomials over a characteristic-zero field, the determinant of their Hasse derivatives of orders 0 through l−1 vanishes as a polynomial exactly when the original family is linearly dependent over the coefficient field. This does not assert that a nonzero Wronskian has no roots. It includes the empty family: its determinant is 1 and its family is independent.

Full native type:

```lean
∀ {K : Type u_1} [inst : Field K] {l : ℕ} [CharZero K] {φ : Fin l → K[X]},
  Roth.wronskian φ = 0 ↔ ¬ LinearIndependent K φ
```

K is the coefficient field, l the family length, and φ the arbitrary family. Field and characteristic zero are the only class hypotheses. The definition uses `det (hasseDeriv μ (φ ν))`. The proof combines the contrapositive of `Roth.wronskian_ne_zero_of_linearIndependent` with `Roth.wronskian_eq_zero_of_not_linearIndependent`. The hard theorem uses strong induction on the sum of degrees, constant column shears, cancellation of equal leading degrees, and a nonzero top coefficient computed by a binomial/Vandermonde determinant. The easy theorem applies Hasse derivatives to a constant linear relation between columns. The definition dependencies are `Roth.wronskian` and `Roth.wronskianMatrix`; both implication dependencies are project declarations.

## Phase 2 — Preliminary checks

**BIG:** explicitly listed under the module's Main results and the complete named Wronskian criterion. Its two-line packaging does not make its mathematical content small. Phase 2b one-line-definition test: n/a, theorem. It is neither a definition-only alias nor rfl glue, so no inherited verdict shortcut applies.

## Phase 3 — Exhaustive literature

Every named channel was actually attempted; at least three distinct general-web forms were searched. Exact requests, returned-response SHA256/bytes/status, and source locators are retained. Article and search-result bodies are not archived. The protocol's informal nine-channel label is not used to omit named channels or invent an extra synthesis channel.

| Channel | Evidence | Finding and limitation |
|---|---|---|
| General web: specific Hasse form | [request/metadata](../evidence/Roth.wronskian_eq_zero_iff/web-general-current.json) | Characteristic-zero polynomial criterion and Bostan–Dumas identified |
| General web: standard/named form | [request/metadata](../evidence/Roth.wronskian_eq_zero_iff/web-general-standard.json) | Wronskians and Linear Independence, Bostan–Dumas |
| General web: abstract form | [request/metadata](../evidence/Roth.wronskian_eq_zero_iff/web-general-abstract.json) | Differential fields use independence over the derivation's constants; fraction-field constants require care |
| Optional mathematical ChatGPT | n/a | `ask_chatgpt_math` unavailable in actual tool inventory; no simulated opinion |
| Local reference | [receipt](../evidence/Roth.wronskian_eq_zero_iff/local-reference.json), [excerpt](../evidence/Roth.wronskian_eq_zero_iff/local-wronskian-excerpt.tex.txt) | `clean.tex`, §Wronskians lines157–195: normalized rational-coefficient iff and degree elimination |
| nLab | [search](../evidence/Roth.wronskian_eq_zero_iff/web-nlab.json), [open metadata](../evidence/Roth.wronskian_eq_zero_iff/web-primary-nlab.json) | Wronskian entry found and search content inspected; direct open fails 400 unsupported application/xhtml+xml |
| nCatLab | [request/metadata](../evidence/Roth.wronskian_eq_zero_iff/web-ncatlab.json) | Separate site-wide differential-field search returns Wronskian/differential algebra entries; no required categorical reformulation located |
| Stacks Project | [request/metadata](../evidence/Roth.wronskian_eq_zero_iff/web-stacks.json) | Character-independence results, including tag0CKK, are different mathematics; no direct criterion located |
| MathOverflow | [request/metadata](../evidence/Roth.wronskian_eq_zero_iff/web-mathoverflow.json) | Hasse/characteristic-p and rational-function independence discussions; contextual rather than primary proof authority |
| Recent arXiv, 2021-10-27–2026-10-27 | [request/metadata](../evidence/Roth.wronskian_eq_zero_iff/web-arxiv.json), [primary abstract](../evidence/Roth.wronskian_eq_zero_iff/web-primary-recent.json) | 2024 nonzero constant polynomial/Laurent Wronskians; 2023 derivative-family and 2026 circuit applications. Search dates alone are unreliable: an old patt-sol result appeared and is excluded from the recent evidence. |

Primary sources inspected:

* [Bostan–Dumas, Wronskians and linear independence](https://mathexp.eu/dumas/publications/Bostan_Dumas_2010_WLI.pdf), Theorem2 p2, Lemmas2–3 p3, proof p4. It treats characteristic-zero formal series and rational functions, using constant echelonization and a Vandermonde leading term. Ordinary derivative rows differ from Hasse rows by invertible factorials in characteristic zero. [Access metadata](../evidence/Roth.wronskian_eq_zero_iff/web-primary-bostan.json).
* [Churchill–Kovacic, Introduction to Differential Galois Theory](https://ksda.ccny.cuny.edu/PostedPapers/intro.pdf), §3.12, Proposition3.12.2 and Corollary3.12.3 pp71–73: the differential-field criterion is over its constants; domain extensions require distinguishing constants of the fraction field from fractions of constants. [Access metadata](../evidence/Roth.wronskian_eq_zero_iff/web-primary-differential.json). The abstract-query response independently exposed this precise locator; direct open initially displayed front matter.
* [Hermoso–Alcázar, Nonzero Constant Wronskians of Polynomials and Laurent Polynomials, and Geometric Consequences](https://arxiv.org/abs/2410.18867), submitted2024-10-24, abstract: characterizes constant nonzero Wronskians and extends to Laurent polynomials. This supports continued mathematical relevance, not a replacement proof of the criterion.

Literature summary: the standard name is the Wronskian criterion/test for linear independence. The polynomial Field+CharZero statement is standard, already broader than the local rational formulation. Broader ambient representations include formal series, rational functions, and differential fields over constants. Historical ordinary derivatives and the local Hasse normalization are equivalent here. Arbitrary smooth functions and unrestricted positive-characteristic base-field independence are false widenings.

## Phase 4a–4b — Generality

| Parameter / hypothesis | Essentially used? | Literature comparison and weakening outcome |
|---|---|---|
| K : Type* | yes | Already universe polymorphic |
| Field K | current interface yes | Both named parents and Wronskian definitions currently carry Field. DivisionRing does not supply the commutative determinant interface. An expanded domain representation is genuinely broader but changes foundational signatures and the hard proof. |
| l : ℕ | yes | All lengths including 0 and1; no positivity assumption to delete. Fin rows encode consecutive derivative orders. Arbitrary finite column labels require an enumeration/reindexing interface. |
| CharZero K | yes | A compiled ZMod2 family [1,X²] is independent and has zero determinant; dropping it is false for these consecutive Hasse rows. |
| φ : Fin l → K[X] | yes | No degree/distinctness/nonzero restriction. Other ambient differential structures change representation and scalar-constants bookkeeping. |

Current form: **MAXIMALLY GENERAL within the fixed Field-bound parent interface**; zero successful mechanical same-parent hypothesis drops. A mathematically stronger expanded domain theorem was actually compiled:

```lean
{R : Type*} [CommRing R] [IsDomain R] [CharZero R] {l : ℕ} {φ : Fin l → R[X]} :
  (Matrix.of fun μ ν : Fin l ↦ Polynomial.hasseDeriv (μ : ℕ) (φ ν)).det = 0 ↔
    ¬ LinearIndependent R φ
```

[Exact executed source](../evidence/Roth.wronskian_eq_zero_iff/native-domain-executed.lean.txt), [clean complete native receipt](../evidence/Roth.wronskian_eq_zero_iff/native-domain-success.json). The hard domain direction explicitly extends to a fraction field and transports Hasse derivatives/determinants; it replays the field induction independently of the target iff. The easy domain proof uses determinant dependence of columns, restriction of scalars, and composition with the bundled jet map. The expanded iff then recovers the original Field statement. This is not a claim that `Roth.wronskian` already elaborates for an arbitrary domain, nor that its new hard helper exists in mathlib.

The reference's [exact Class5 instruction](../evidence/Roth.wronskian_eq_zero_iff/class5-excerpt.md.txt) ([source path/hash](../evidence/Roth.wronskian_eq_zero_iff/class5-source.json)) applies: changing the parent definitions and dependent API is more than a single hypothesis-weakening edit. This supports BORDERLINE with a concrete design question; it does not support YES-generalise-first by calling a new fraction-field proof a mechanical drop. Cost is not the verdict reason. A CharZero ring with zero divisors is also inadequate: the compiled ℤ×ℤ singleton C(1,0) is dependent but has nonzero determinant. [Guard source](../evidence/Roth.wronskian_eq_zero_iff/native-guards-executed.lean.txt), [receipt](../evidence/Roth.wronskian_eq_zero_iff/native-guards-success.json).

## Phase 4c — Modern idiom, all nine rows

| # | Question | Answer and downstream consequence |
|---|---|---|
| 1 | Typeclasses | Already Field/CharZero; no ad-hoc field predicate |
| 2 | Filters/nets | no: finite algebra, no limits |
| 3 | Universal property | no object construction in this iff; fraction-field universal property is useful in the domain proof |
| 4 | Bundled substructures | no closure predicate to replace; `LinearIndependent` is existing module API. A degree-echelon basis API could organize the underlying hard proof but must first be developed. |
| 5 | Field-to-module hierarchy | yes: domain determinant/LI formulation enables integral polynomial families and composes with `LinearIndependent.iff_fractionRing`, polynomial map, `hasseDeriv_map`, determinant map |
| 6 | Higher categories | no applicable categorical content |
| 7 | Concrete indices | natural derivative orders are essential; arbitrary finite column enumeration can be designed, arbitrary additive-group derivative rows would change the theorem |
| 8 | Concrete-via-abstract diagnostic | Proof-body scan finds no specific coefficient field or witness. It uses only the two criterion implications: abstractly they package an iff by `imp_not_comm`. Those are substantive project theorems, not properties automatically available for an arbitrary operator. No mathematical content is gained by inventing a generic propositional packaging lemma. |
| 9 | False-generalization guard | Expanded domain polynomials preserve the object and compile. Arbitrary smooth functions, arbitrary linear operators, dropping CharZero, and arbitrary CharZero rings are rejected. Differential-field independence must be over actual constants, not an arbitrary base field. |

Modern-idiom verdict: a domain-level n-ary polynomial interface has concrete benefit; the current theorem already uses the right independence predicate. Foundation redesign is the outstanding choice, not cosmetic categorification. Power-series/differential-field theorems are separate substantial extensions.

## Phase 4.5 — Infrastructure risk

n/a: theorem. The six concerns—typeclass diamonds, reducibility leaks, noncanonical unfolding, instance priorities, universe-instance issues, coercion ambiguity—introduce no new definitions or instances here. Parent interface risks are tracked as design dependencies rather than inherited theorem risks.

## Phase 4.6 — Proof-strategy optimality

| Row | Assessment |
|---|---|
| Topology epsilon/delta versus filters | n/a: finite algebra |
| Algebra elements versus bundled submodules | Current iff simply combines complementary implications; appropriate. Underlying degree elimination could use a new echelon-basis API. |
| Analysis sequences versus nets | n/a: no convergence |
| Category construction versus universal property | n/a for iff; localization is appropriate for the domain extension |
| Missing helper API | Both n-ary Wronskian implications and its foundation are missing upstream; propositional iff assembly needs no new general helper. |

Strategy verdict: **MATHLIB-IDIOMATIC** for assembling the criterion. Keep the substantial directions separately useful; do not prove either direction through this iff or a downstream generalized-Wronskian theorem, which would be circular.

## Phase 5 — Five actual mathlib methods on three forms

| Method | Current Hasse determinant iff | Standard polynomial Wronskian | Abstract differential-field/constants |
|---|---|---|---|
| Lean-Finder | [raw](../evidence/Roth.wronskian_eq_zero_iff/formal-finder-current.json) | [raw](../evidence/Roth.wronskian_eq_zero_iff/formal-finder-standard.json) | [raw](../evidence/Roth.wronskian_eq_zero_iff/formal-finder-abstract.json) |
| Loogle | [raw](../evidence/Roth.wronskian_eq_zero_iff/formal-loogle-current.json) | [raw](../evidence/Roth.wronskian_eq_zero_iff/formal-loogle-standard.json) | [raw](../evidence/Roth.wronskian_eq_zero_iff/formal-loogle-abstract.json) |
| LeanSearch | [raw](../evidence/Roth.wronskian_eq_zero_iff/formal-leansearch-current.json) | [raw](../evidence/Roth.wronskian_eq_zero_iff/formal-leansearch-standard.json) | [raw](../evidence/Roth.wronskian_eq_zero_iff/formal-leansearch-abstract.json) |
| Pinned source rg | [raw](../evidence/Roth.wronskian_eq_zero_iff/rg-current.json) | [raw](../evidence/Roth.wronskian_eq_zero_iff/rg-standard.json) | [raw](../evidence/Roth.wronskian_eq_zero_iff/rg-abstract.json) |
| Local name search | [raw](../evidence/Roth.wronskian_eq_zero_iff/formal-local-current.json) | [raw](../evidence/Roth.wronskian_eq_zero_iff/formal-local-standard.json) | [raw](../evidence/Roth.wronskian_eq_zero_iff/formal-local-abstract.json) |

Every result was inspected. Local search marks the index unavailable while returning source matches: neither proves absence nor a complete index. External search revisions may differ from the pin. Current Loogle is empty; standard Loogle and Finder positively find `IsCoprime.wronskian_eq_zero_iff`. The actual pinned native signature is:

```lean
∀ {R : Type u_1} [CommRing R] [NoZeroDivisors R] {a b : R[X]},
  IsCoprime a b → (a.wronskian b = 0 ↔ derivative a = 0 ∧ derivative b = 0)
```

This is a different namespace and binary coprime/derivatives-zero criterion. It is not the target for arbitrary n or a one-call specialization. `Polynomial.wronskian` is binary. `Matrix.linearIndependent_cols_of_det_ne_zero` and `Matrix.det_eq_zero_of_not_linearIndependent_cols` concern independence of jet columns over the matrix ring R[X], not independence of φ over R. The easy direction can transport through a bundled jet map, but the converse needs the missing polynomial Wronskian theorem. Discriminants/Gram matrices, Jacobian submersive presentations, Sylvester matrices, and Vandermonde injectivity criteria concern different matrices; none supplies this iff.

The pinned [Wronskian source](../evidence/Roth.wronskian_eq_zero_iff/Wronskian-mathlib.lean.txt) explicitly lists TODO: “Define Wronskian for n-tuple of polynomials, not necessarily two.” This is a specific missing-API anchor. [Pinned candidate and missing-target guards](../evidence/Roth.wronskian_eq_zero_iff/native-guards-success.json) and [mathlib-only exact? failure](../evidence/Roth.wronskian_eq_zero_iff/native-composition-rejected.json) accompany the untruncated source searches. The guessed `Polynomial.wronskian_eq_zero_iff` is unknown under the tested imports; this is not asserted to prove global absence by itself.

Search conclusion: partial matches and useful easy-direction building blocks; no exact n-ary criterion or existing ≤3-call proof identified. No parent re-aim hit: the parents have no existing general n-ary mathlib counterpart with the analogous law.

## Phase 5.5 — Statement shape

Normal forms considered: W=0 iff not LI; W≠0 iff LI; LI implies W≠0. The current negative iff puts independence content on the RHS and is a natural vanishing rewrite API. The positive iff is also useful, but no existing n-ary canonical form was located. Keep implication names for the callers supplying LI. No `simp` attribute is present; assigning one needs orientation/API review.

Syntactic generality: implicit φ and l support rewriting and projection application; no reason to add positivity or individual nonzero assumptions. The expanded-domain signature was compiled and specializes to the original spelling. An arbitrary finite column type would require consistent reindexing of this ordered determinant API.

Superfluous audit: K, l, φ all determine the object; Field is used by the fixed parents, CharZero is mathematically necessary as demonstrated by the compiled guard. There are no unused explicit assumptions. Normal form: OK. Syntactic form: OK within the parent interface; **RESTATE-BEFORE-SHIP** if the domain foundation is chosen. This is an API decision, not a hidden verified same-parent weakening.

## Phase 6.0 — Callers and inline audit

[Whole-project exact-name search](../evidence/Roth.wronskian_eq_zero_iff/callers.json), [whole-project Wronskian/independence inline inventory](../evidence/Roth.wronskian_eq_zero_iff/inline.json). Search covers all production `Roth/**/*.lean` and `Roth.lean`, including qualified and unqualified name occurrences; no aliases or dot calls found.

Internal explicit use count outside declaring file: **0**, external-to-file caller files: **0**. Same-module calls: **0**. The only exact-name source matches are the declaration and its Main results documentation.

| Actual target caller | Usage | Refactor |
|---|---|---|
| none | no named calls | no target call-site edits justified |

Inline audit distinguishes related results from rederivations of the full iff:

| Location | Actual related content | Classification |
|---|---|---|
| Roth/GenWronskian.lean:41 | dependent family gives vanishing generalized Wronskian | different multivariate easy direction, not target iff |
| Roth/GenWronskian.lean:262 | hard implication applied to an independent Kronecker-substituted family | uses the primary implication; not a full iff rederivation |
| Roth/Separation.lean:534 | hard implication supplies nonzero univariate factor in existential tuple | uses primary implication; not a full iff rederivation |

No full target iff is rederived inline elsewhere. These are explicit source references, not an opaque kernel/simp dependency closure. Zero named callers does not establish junk: this theorem is explicitly documented as the module's main public criterion, packages both useful directions, and is discoverable as a vanishing rewrite. Retain it while deciding upstream API.

## Phase 6 — Actual composition experiments

1. Original proof replay succeeds using `imp_not_comm.mp` and the two **project** implication theorems. That is valid propositional packaging, not a two-call existing-mathlib replacement. [Target source/receipt](../evidence/Roth.wronskian_eq_zero_iff/native-target-success.json).
2. A mathlib-only raw determinant iff with `exact?` fails promptly without timeout. It imports no Roth module and guards the target missing. [Exact code](../evidence/Roth.wronskian_eq_zero_iff/native-composition-executed.lean.txt), [raw rejected receipt](../evidence/Roth.wronskian_eq_zero_iff/native-composition-rejected.json). Failure alone is not proof of absence; it supplements positive-candidate analysis and the pinned n-tuple TODO.
3. The generic raw domain easy direction compiles via `Matrix.det_eq_zero_of_not_linearIndependent_cols`, `LinearIndependent.restrict_scalars'`, `LinearIndependent.of_comp`, and `LinearMap.pi`: four existing calls, with a scalar/jet bridge. It supplies only one implication. The full expanded-domain iff compiles only after adding the new fraction-field hard proof; neither that helper nor the prior project hard theorem counts as existing mathlib. [Exact code](../evidence/Roth.wronskian_eq_zero_iff/native-domain-executed.lean.txt), [receipt](../evidence/Roth.wronskian_eq_zero_iff/native-domain-success.json).
4. Binary `IsCoprime.wronskian_eq_zero_iff` cannot specialize to arbitrary l and arbitrary φ. A generic matrix dependence theorem changes the scalar-independence premise; the missing hard implication cannot be bypassed by relabelling columns. No closing simp composition was found; Phase6b would make such a finding BORDERLINE rather than automatic NO.

Conclusion: **NOT-COMPOSABLE from existing mathlib in ≤3 calls**. This does not deny the deliberately short assembly once the missing directions have been upstreamed.

## Phase 7 — Verdict and actionable next step

**BORDERLINE-needs-human**, independently assessed. Literature confirms a standard named criterion; the specific pinned TODO identifies the missing n-ary foundation. Mathlib's binary coprime iff is a false same-name match. The new domain proof is verified, but adopting it requires changing Field-bound parent definitions and dependent signatures. Class5 therefore applies. Neither zero caller count, the two-line source proof, nor implementation cost justifies deletion or a NO verdict.

Concrete upstream API questions:

1. Adopt an n-ary Hasse-Wronskian foundation over commutative rings, with this criterion over characteristic-zero integral domains, or initially expose the field API?
2. Keep the finite-column interface `Fin l`, or design arbitrary finite columns with an explicit enumeration/reindexing law in the foundational PR?
3. Ship W=0 iff not LI as the public vanishing criterion alongside the separately useful implications, and should it carry a simp attribute?

Next action: resolve those design questions when planning the upstream API, then rerun `/mathlibable Roth.wronskian_eq_zero_iff` against the adopted foundation. This read-only assessment is complete; no verification remains unresolved and no production edit is requested now. Keep the declaration in `Roth/Wronskian.lean` meanwhile.

If accepted for contribution, target `Mathlib/RingTheory/Polynomial/Wronskian.lean` or a focused n-ary companion and propose “feat(Polynomial): add the n-ary Wronskian criterion”. Group the criterion with its two directions and foundation; the directions/foundation currently have BORDERLINE assessments, not accepted YES verdicts. Already accepted related YES candidates are `Roth.det_choose_eq`, `Roth.coeff_wronskian_of_natDegree_injective`, and `Roth.wronskian_ne_zero_of_natDegree_injective`, each YES-but-generalise-first. [Actual progress-derived grouping](../evidence/Roth.wronskian_eq_zero_iff/accepted-grouping.json). Run `/generalise Roth.wronskian_eq_zero_iff`, `/cleanup Roth/Wronskian.lean Roth.wronskian_eq_zero_iff`, and choose an algebra/polynomial reviewer from relevant recent upstream commits before opening the eventual PR. No reviewer identity is guessed in this BORDERLINE assessment.

## Phase 8 — Report and evidence integrity

All phases PASS, with theorem-only n/a items explicitly justified. Root acceptance is pending independent review. [Assessment](../evidence/Roth.wronskian_eq_zero_iff/assessment.json), [verification](../evidence/Roth.wronskian_eq_zero_iff/verification.json), [overview entry](../evidence/Roth.wronskian_eq_zero_iff/overview-entry.json), [current copy manifest](../evidence/Roth.wronskian_eq_zero_iff/copy-manifest.json), [portable read-only validator](../evidence/Roth.wronskian_eq_zero_iff/validate.py).

The validator supports scratch and integrated layouts, checks the current manifest rather than historical worker manifests, requires complete native successes/standard axioms, source/pin hashes, exact archived executed sources, fresh file-milestone success, all formal/literature channels, and report links. It invokes the tracked credential guard. Rejected composition evidence is explicitly separate from accepted proofs. No production sources, pins, Git, or overview/progress files were changed by this worker.
