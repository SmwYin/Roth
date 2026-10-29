# Roth.norm_coeff_modByMonic_le — canonical243

Verdict: **BORDERLINE-needs-human**, on the public API boundary for a quantitative polynomial
remainder estimate. This is a completed read-only assessment; the three questions below are
future upstream design questions, not unresolved verification or a request to stop the overview.
No verdict is inherited from the short outer induction or the usefulness of Roth's main lemma.

## Phase 0 — baseline and integrity

Public theorem at `Roth/MainLemma.lean:252`. All17 fresh source/pin hashes match the shared
manifest, so the successful2467-job baseline applies. The file-end build at228 is previously
accepted supplementary evidence; the next prescribed file-end build is266. No production,
Git, pin, overview or progress write was made. All scratch sources preserve the existing nine
disk imports or exact18 isolated imports. No extra import was authorized or added.

The full declaring module and the actual caller proof were read. Original MainLemma was
replayed in a fresh namespace, renaming only the target outside the canonical array. The
array was generated directly from tracked declaration-order, checked before execution with
`check_audit_source.py`, and verified at runtime:293 requested,293 unique,293 present,293 values.
The fresh canonical audit identifies one direct body consumer and zero direct type consumers.

[inputs.json](../evidence/Roth.norm_coeff_modByMonic_le/inputs.json),
[input-manifest.json](../evidence/Roth.norm_coeff_modByMonic_le/input-manifest.json),
[baseline-build.txt](../evidence/Roth.norm_coeff_modByMonic_le/baseline-build.txt),
[preparation-checks.json](../evidence/Roth.norm_coeff_modByMonic_le/preparation-checks.json),
[canonical-snapshot.json](../evidence/Roth.norm_coeff_modByMonic_le/canonical-snapshot.json).

## Phase 1 — mathematical content

Let f and P be polynomials over any seminormed ring. Suppose every coefficient of f has
norm at most A, every coefficient of P has norm at most C, and natDegree(P)≤s. Every
coefficient of P%ₘf then has norm at most (1+A)^(s+1−natDegree(f))C. The subtraction is in ℕ:
when natDegree(f)>s, the exponent is zero, not negative. Neither monicity nor sign hypotheses
are premises. The bounds at coefficient0 imply A,C≥0. For a nonmonic divisor this operation
returns P, and the estimate remains valid. The theorem also covers zero polynomials, f=1,
and the trivial coefficient ring.

Full native type, extracted with `Lean.getConstInfo` and `pp.funBinderTypes`:

```lean
∀ {R : Type u_1} [inst : SeminormedRing R] {f : Polynomial R} {A : ℝ},
  (∀ (i : ℕ), ‖f.coeff i‖ ≤ A) →
    ∀ (P : Polynomial R) {C : ℝ},
      (∀ (i : ℕ), ‖P.coeff i‖ ≤ C) →
        ∀ {s : ℕ}, P.natDegree ≤ s → ∀ (i : ℕ), ‖(P %ₘ f).coeff i‖ ≤ (1 + A) ^ (s + 1 - f.natDegree) * C
```

The private `exists_norm_coeff_reduction_aux` proves the substantive step. A nontrivial
reduction forces the divisor to be monic, P≠0 and deg(f)≤deg(P). Subtracting
f*(C(P.leadingCoeff)*X^(natDegree(P)−natDegree(f))) cancels the leading term.
`Polynomial.div_wf_lemma` lowers the degree. The coefficient formula, subtraction triangle
inequality and submultiplicativity give the new bound (1+A)C. The outer theorem handles f=1
and an unchanged remainder, then uses strong induction on s and saturated-subtraction
arithmetic to count the remaining eliminations. This private project helper is **not** an
existing mathlib building block.

Original and replay have only propext, Classical.choice and Quot.sound. The kernel printer
explicitly elided82687characters; this is **not a full kernel-body dump**. The complete
executed written module, full native type, axioms, constant lists and canonical value audit
are archived. Source-level project dependency is exactly the private reduction helper;
the full kernel body additionally mentions generated arithmetic proof constants.

[target-excerpt.lean.txt](../evidence/Roth.norm_coeff_modByMonic_le/target-excerpt.lean.txt),
[source-MainLemma.lean.txt](../evidence/Roth.norm_coeff_modByMonic_le/source-MainLemma.lean.txt),
[native-type.json](../evidence/Roth.norm_coeff_modByMonic_le/native-type.json),
[original-executed.lean.txt](../evidence/Roth.norm_coeff_modByMonic_le/original-executed.lean.txt),
[original-receipt.json](../evidence/Roth.norm_coeff_modByMonic_le/original-receipt.json).

## Phase 2 — preliminary checks

**BIG**: the module explicitly lists this estimate among its main results. It introduces no
new structure and is not a named classical theorem; BIG controls narrative, not search width.
The one-line-definition test and its three exemptions are n/a because this is a theorem.
The outer proof has19 substantive lines; the nontrivial reduction helper adds its own proof.
A short outer proof does not make this a composition from existing mathlib.

## Phase 3 — exhaustive literature

| Channel | Actual request / inspection | Result and limit |
|---|---|---|
| General web: specific | polynomial division monic remainder coefficient bound (1+A) height | Monic division and height literature; no exact external theorem hit. |
| General web: general | polynomial remainder bound submultiplicative seminorm ring coefficient growth | Algebraic division background; no arbitrary-seminorm remainder bound identified. |
| General web: aliases | Mignotte polynomial division remainder height bound monic | Factor-height bounds surfaced; factors and remainders are distinct. |
| Optional ask_chatgpt_math | unavailable | justified n/a; no second-opinion result invented. |
| Local source | clean.tex lines1431–1482, §6 proof of Lemma9 | Exact elimination argument and exponent max(0,s−n+1). |
| nLab | site:ncatlab.org/nlab polynomial division seminorm | Norm and polynomial background; no quantitative remainder theorem. |
| nCatLab, distinct namespace | site:ncatlab.org/ncatlab polynomial division norm | Returned nLab results outside requested namespace; no in-namespace exact hit. |
| Stacks | site:stacks.math.columbia.edu monic polynomial division remainder | Tag052Z uses monic long division; no quantitative norm control. |
| MathOverflow | site:mathoverflow.net polynomial remainder coefficient bound monic | Factor-bound discussion, not the target. |
| Recent arXiv | site:arxiv.org polynomial division remainder coefficient bounds after:2021-10-28 before:2026-10-29 | 2308.03885 exact quotient bounds and2602.12772 formal Gröbner division; not exact target. |
| Primary follow-up | Cambridge Nahshon–Shpilka2026 article, Lemma1.3 and Theorem1.8 discussion | Separates exact quotient bounds from exponential inexact remainder growth. |

The local source states the exact bound for integer coefficient heights in Roth's proof.
The broader literature supports the importance of height growth during division, but does
not establish a unique named theorem or a preferred arbitrary-seminorm interface. The
seminorm extension is justified by the independently compiled proof, not attributed to the
external sources.

[Division with Remainder, Theorem2.2.1 and Remark2.2.2](https://www.math.uni-sb.de/ag/schreyer/images/PDFs/teaching/ws1617ag/book.pdf)
explains degree-lowering leading-term cancellation and division by monic polynomials over rings.
[Stacks052Z](https://stacks.math.columbia.edu/tag/052Z) uses the algebraic division step.
[nLab norm](https://ncatlab.org/nlab/show/norm) provides seminorm background.
The [MathOverflow factor-bound discussion](https://mathoverflow.net/questions/108726/getting-a-bound-on-the-coefficients-of-the-factor-polynomial)
concerns factors, so is not a replacement. The primary
[Cambridge article](https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/new-bound-on-cofactors-of-sparse-polynomials/2CADDB77D2E5CBFB7B803CCCAC49D2FD),
published2026-03-31, discusses induction on long division for exact quotients and exhibits
exponential remainder growth in the inexact case. The related
[2023 arXiv paper](https://arxiv.org/abs/2308.03885) bounds exact quotients; its hypotheses and
conclusion differ. These external sources do not prove the present arbitrary-ring estimate.

Web archives retain exact requests, response SHA256/byte counts/status, clean titles, URLs,
locators and original concise summaries only. No full article/search bodies are persisted.

[web-general.json](../evidence/Roth.norm_coeff_modByMonic_le/web-general.json),
[web-channels.json](../evidence/Roth.norm_coeff_modByMonic_le/web-channels.json),
[web-recent.json](../evidence/Roth.norm_coeff_modByMonic_le/web-recent.json),
[web-primary.json](../evidence/Roth.norm_coeff_modByMonic_le/web-primary.json),
[local-excerpt.tex.txt](../evidence/Roth.norm_coeff_modByMonic_le/local-excerpt.tex.txt),
[literature-source.json](../evidence/Roth.norm_coeff_modByMonic_le/literature-source.json).

## Phase 4a — parameter and hypothesis analysis

| Parameter / premise | Role and weakening outcome |
|---|---|
| R : Type u | Arbitrary universe and coefficient ring; no specific arithmetic ring used. |
| SeminormedRing R | Associative unital ring supports modByMonic. Only nonnegative size, zero, subtraction triangle and submultiplicativity enter the estimate; verified unbundled restatement below. No commutativity or separation is needed. |
| f | Arbitrary divisor, including0,1 and nonmonic cases. Adding Monic would restrict coverage. |
| A | Semantic uniform divisor coefficient bound; hfA0 implies nonnegative. It cannot be dropped as a number without replacing it by an intrinsic size of f. |
| hfA | Controls each eliminated coefficient product; a degree bound alone does not control size. |
| P | Arbitrary dividend, including0. |
| C | Semantic uniform dividend coefficient bound; hP0 implies nonnegative. |
| hP | Necessary size input; constants of degree0 already have arbitrarily large coefficient size. |
| s, hs | User-supplied natural degree ceiling controls the number of eliminations. Can specialize s=P.natDegree, retaining the supplied-bound version for callers. |
| i | Arbitrary coefficient index; the pointwise result can equivalently be universally quantified. |
| s+1−natDegree(f) | Saturated elimination count. The final +1 is mathematically needed; X modulo X−2 refutes simply removing the final step. |

## Phase 4b — verified generality

The original is already mathematically broad: no field, commutativity, monicity, positivity,
nontriviality, completeness or separatedness premise can be removed because none is present.
A meaningful **representation generalization** was actually compiled in isolated mathlib:

```lean
theorem size_remainder {R : Type*} [Ring R] (v : R → ℝ)
    (v0 : v 0 = 0) (vn : ∀ x, 0 ≤ v x)
    (vsub : ∀ x y, v (x - y) ≤ v x + v y)
    (vmul : ∀ x y, v (x * y) ≤ v x * v y) {f : Polynomial R} {A : ℝ}
    (hfA : ∀ i, v (f.coeff i) ≤ A) (P : Polynomial R) {C : ℝ} (hP : ∀ i, v (P.coeff i) ≤ C) {s : ℕ}
    (hs : P.natDegree ≤ s) (i : ℕ) :
    v ((P %ₘ f).coeff i) ≤ (1 + A) ^ (s + 1 - f.natDegree) * C
```

The proof contains a freshly proved generic reduction and induction. It is a new theorem,
not an existing mathlib result found by search. The full original statement is recovered by
specializing v=norm with norm_zero, norm_nonneg, norm_sub_le and norm_mul_le. This enables
using an explicit size function without selecting ambient metric/topology data. The exact
same polynomial operation and saturated exponent remain; this does not assume commutativity.

Pinned `RingSeminorm.toSeminormedRing` was source-inspected as a natural bundled bridge.
Its meaningful theorem specialization was **not** compiled here: RingSeminorm is absent
from the fixed disk environment, and no extra-import authorization was received. No bundled
alternative is claimed verified. The unbundled alternative above supplies the mandatory
actual generalization test. This is why the remaining issue is which public interface to
expose, rather than an unsupported claim that the existing theorem is a mathlib duplicate.

[isolated-executed.lean.txt](../evidence/Roth.norm_coeff_modByMonic_le/isolated-executed.lean.txt),
[isolated-receipt.json](../evidence/Roth.norm_coeff_modByMonic_le/isolated-receipt.json),
[edge-executed.lean.txt](../evidence/Roth.norm_coeff_modByMonic_le/edge-executed.lean.txt),
[edge-receipt.json](../evidence/Roth.norm_coeff_modByMonic_le/edge-receipt.json),
[availability-receipt.json](../evidence/Roth.norm_coeff_modByMonic_le/availability-receipt.json).

## Phase 4c — modern idiom, all nine rows

| # | Question | Result and downstream consequence |
|---|---|---|
| 1 | Typeclasses instead of bundled hypotheses? | Original ring/norm laws are already class-driven. Explicit sizes allow multiple choices; bundled RingSeminorm is a future API choice, not a verified replacement. |
| 2 | Sequences to filters? | No; finite degree induction has no convergence premise. |
| 3 | Construction to universal property? | No; a quantitative inequality needs estimates, not just the quotient/remainder universal property. |
| 4 | Sets to bundled substructures? | CoeffMem is relevant algebraic API, but bounded norm balls are not additive submodules; no direct quantitative replacement. |
| 5 | Weaker hierarchy? | Explicit Ring plus size laws was verified; no commutativity introduced. Semiring lacks subtraction used by modByMonic in this pin. |
| 6 | Higher categories? | No; no categorical content or downstream gain. |
| 7 | Concrete indices? | ℕ indexes polynomial coefficients and the exact degree recursion. Arbitrary indices would change the polynomial representation/algorithm. |
| 8 | Concrete-via-abstract? | No special witness. Diagnostic examines1 and s+1−n: these are structural inflation/elimination constants. A,C are already semantic parameters; final_step_needed verifies the +1 matters. |
| 9 | False-generalization guard | Passed for explicit-size theorem: same Ring polynomial/modByMonic and saturated exponent. Reject adding commutativity, silently requiring Monic, using signed exponents or assuming norm balls are submodules. |

Modern representation available: verified explicit sizes. It has the concrete gain of
separating coefficient size from an ambient normed structure. This does not automatically
settle the upstream public interface, since mathlib already bundles ring seminorms and
provides intrinsic Polynomial.supNorm. No categorical reformulation is proposed.

[concrete-diagnostic.json](../evidence/Roth.norm_coeff_modByMonic_le/concrete-diagnostic.json).

## Phase 4.5 — six infrastructure rows

| Risk | Verdict and reason |
|---|---|
| Typeclass diamond | n/a: theorem introduces no instance or data structure. |
| Reducibility leak | n/a: proof equality does not create a new mathematical data definition. |
| Noncanonical unfolding | n/a: theorem, no new reducible data alias. |
| Instance priority | n/a: no instance declaration. |
| Universe | n/a infrastructure risk; theorem is already universe-polymorphic. |
| Coercion | n/a: theorem adds no coercion path. |

## Phase 4.6 — proof strategy, all five rows

| # | Question | Result |
|---|---|---|
| 1 | ε–δ versus filters | n/a: no topology argument. |
| 2 | Elements versus subobjects | CoeffMem abstracts algebraic coefficient generation, but cannot control arbitrary sums by a fixed bound. Coefficient estimates and degree descent are appropriate. |
| 3 | Sequences versus nets | n/a: finite well-founded reduction. |
| 4 | Construction versus universal property | Division recursion is needed to count size inflation. Uniqueness alone gives no inequality. |
| 5 | Missing helper API | Yes: a quantitative one-step coefficient estimate and its iteration. Current private reduction is newly proved project infrastructure. |

Strategy: MATHLIB-IDIOMATIC degree induction; REFACTOR-RECOMMENDED only for choosing a primary
quantitative interface and helper visibility before upstream. There is no strategy-based
cost downgrade. A richer existing API could shorten this proof, but the missing estimate
would itself be the contribution.

## Phase 5 — all15 formal search cells

| Form | Method | Actual query / outcome |
|---|---|---|
| current | Finder | Remainder coefficients bounded by (1+A)^(s+1−natDegree); CoeffMem and division hits, no norm iteration. |
| current | Loogle | Polynomial.modByMonic, norm, LE.le was malformed (unknown norm); corrected Polynomial.modByMonic, Norm.norm, LE.le returned empty. |
| current | LeanSearch | Same quantitative remainder query; division and algebraic CoeffMem, no numeric estimate. |
| current | rg | Full untruncated norm_coeff_modByMonic_le / norm–modByMonic patterns; no mathlib exact hit. |
| current | local | norm_coeff_modByMonic: project target only; index error means no absence inference. |
| standard | Finder | Coefficient height growth under monic long division; div_wf_lemma and CoeffMem. |
| standard | Loogle | Polynomial.modByMonic, Polynomial.coeff; reconstruction and algebraic membership. |
| standard | LeanSearch | Height/long-division query; division degree laws and CoeffMem. |
| standard | rg | coeff_modByMonic / div_wf_lemma / modByMonic_eq_self_iff; genuine building blocks. |
| standard | local | modByMonic: operation, reconstruction, degree and linearity APIs; index warming. |
| abstract | Finder | Ring seminorm/submultiplicative size remainder query; Gauss norm and spectral/root estimates. |
| abstract | Loogle | RingSeminorm, Polynomial; empty. |
| abstract | LeanSearch | RingSeminorm laws and norm_mul_le, no remainder theorem. |
| abstract | rg | gaussNorm–modByMonic / toSeminormedRing / supNorm; representation API, no remainder iteration. |
| abstract | local | gaussNorm names and algebraic norm laws; index warming. |

All exact requests and full raw formal-search responses are archived as search-{form}-{method}.json.
The malformed current Loogle receipt remains separate from its corrected retry. External index
snapshots can differ from the pin; names/signatures were checked against pinned source, and
actual positive division building blocks were checked in Lean. Local warming/error is not
absence evidence. No broad numerical exact? search was run or resource limit raised.

`Polynomial.coeff_modByMonic_mem_pow_natDegree_mul` in CoeffMem describes membership in a
power/product of coefficient-generated submodules. It forgets the number and sizes of
summands; replacing the submodules with a bounded norm ball fails closure under addition.
`Polynomial.natDegree_modByMonic_le` only bounds degree, and `sum_modByMonic_coeff` only
reconstructs the remainder. `Polynomial.gaussNorm` / `supNorm` package coefficient sizes but
supply no iterated division-loss estimate in the inspected pin. `Polynomial.div_wf_lemma`
is the real degree-descent building block; the numeric coefficient inflation is missing.

[search-current-loogle-retry.json](../evidence/Roth.norm_coeff_modByMonic_le/search-current-loogle-retry.json),
[mathlib-inputs.json](../evidence/Roth.norm_coeff_modByMonic_le/mathlib-inputs.json),
[search-current-rg.json](../evidence/Roth.norm_coeff_modByMonic_le/search-current-rg.json),
[search-standard-rg.json](../evidence/Roth.norm_coeff_modByMonic_le/search-standard-rg.json),
[search-abstract-rg.json](../evidence/Roth.norm_coeff_modByMonic_le/search-abstract-rg.json).

## Phase 5.5 — statement shape

**Normal form:** explicit pointwise coefficient bound versus intrinsic supNorm/gaussNorm bound.
The polynomial operation is already mathlib's canonical modByMonic. Preserve the saturated
natural exponent. No equivalence lemma is being oriented against another canonical predicate;
the usual RHS-normal-form issue is n/a. A supNorm statement would be an API design choice,
not an already verified existing replacement.

**Syntactic generality:** tried explicit-size parameters and compiled original norm recovery.
Also considered s=P.natDegree and a universally quantified conclusion. The supplied s version
is easiest for the actual caller, whose diagonal degree is bounded by a sum of coordinate
degrees. All coefficient indices and supplied bounds remain freely usable.

**Superfluous arguments:** every R/f/P/A/C/s/i binder and both coefficient-bound hypotheses
has a role listed in Phase4a. SeminormedRing's topological data is unused by the quantitative
argument, which the generic-size experiment verifies. There is no redundant sign, monicity,
commutativity, nonzero or positivity argument to delete. Statement-shape verdict: preserve the
current signature locally; choose direct norm versus bundled/intrinsic size before upstream.

## Phase 6.0 — full callers and inline audit

| Caller file:line | Use | Actual experiment |
|---|---|---|
| Roth/MainLemma.lean:512, private abs_coeff_diag_hasseDeriv_modByMonic_le_aux | Bounds the diagonal Hasse polynomial, then invokes target with s=∑r. | Complete module replay reroutes this caller to new generic size theorem; original signature equality compiles. |

One executable occurrence, one caller declaration, zero external-to-file callers. The other
lexical occurrences are the declaration and module documentation. Fresh scoped rg --no-ignore
and tracked git grep agree. Full source inventory was cross-checked. The exact canonical
kernel audit agrees on the single private direct body consumer and zero type consumers.

The inline-derivation search inspected coefficient/remainder/division patterns throughout
production sources. No independent inline rederivation of this exact general remainder
bound was found. The diagonal bound uses this theorem; the floor bound consumes the diagonal
bound and separately handles degree0/nonmonic branches. They are downstream estimates, not
bypasses of the general theorem.

The actual caller full-body inlining experiment removed the target theorem and nested its
proof as a local have in the original caller. It reached Lean's default200k whnf limit.
That exact source and raw failed receipt are rejected evidence; no claimed inline success,
no limit raise. A separate complete module replay replaces the call with the freshly proved
explicit-size theorem specialized to norm. It compiles with the original caller signature
retained by proof-irrelevant definitional equality and standard axioms; downstream main_lemma
also compiles. This shows representation compatibility, not existing-mathlib composability.

Lexical/body/type/kernel/simp/transitive scopes remain distinct. The target is not a simp
lemma. Imported original Roth is still transitively available, so no global transitive
independence claim is made. The new caller body is checked to have no direct target constant.

[source-search.json](../evidence/Roth.norm_coeff_modByMonic_le/source-search.json),
[tracked-source-search.json](../evidence/Roth.norm_coeff_modByMonic_le/tracked-source-search.json),
[inline-audit.json](../evidence/Roth.norm_coeff_modByMonic_le/inline-audit.json),
[callers.json](../evidence/Roth.norm_coeff_modByMonic_le/callers.json),
[canonical-consumers.json](../evidence/Roth.norm_coeff_modByMonic_le/canonical-consumers.json),
[scope-audit.json](../evidence/Roth.norm_coeff_modByMonic_le/scope-audit.json),
[project-executed.lean.txt](../evidence/Roth.norm_coeff_modByMonic_le/project-executed.lean.txt),
[project-receipt.json](../evidence/Roth.norm_coeff_modByMonic_le/project-receipt.json),
[inline-rejected-receipt.json](../evidence/Roth.norm_coeff_modByMonic_le/inline-rejected-receipt.json).

Pairwise duplication audit:

| Decl A | Decl B | Same statement? | Same proof? | Verdict |
|---|---|---|---|---|
| target | private exists_norm_coeff_reduction_aux | No: iteration versus one step | Shared reduction content | Keep helper distinction; private is not mathlib. |
| target | diagonal Hasse remainder caller | No: arbitrary ring/dividend versus integer diagonal derivatives | Caller composes target with project bounds | Genuine specialization, retain abstraction. |
| target | Polynomial.coeff_modByMonic_mem_pow_natDegree_mul | No: quantitative size versus submodule membership | Both descend degree | Related algebraic infrastructure, not replacement. |
| target | Polynomial.natDegree_modByMonic_le | No: coefficient norm versus degree | Algorithm-related only | A degree bound cannot imply a size bound. |
| target | Mignotte/factor-height estimates | No: remainders versus exact factors | Different quantitative arguments | Do not identify them. |

## Phase 6 — composition and adversarial native checks

Attempt1: derive from `Polynomial.natDegree_modByMonic_le`. A bounded exact-term attempt
fails in compiled scratch, and degree_not_size refutes degree-only coefficient bounds with
constant2. Attempt2: rewrite with modByMonic_eq_sub_mul_div and use triangle/multiplication
bounds. The rewrite alone does not close the compiled goal: quotient coefficient growth
would itself need a quantitative proof. Attempt3: CoeffMem membership or Gauss norm packaging
does not control the missing number/size of summands or iterate the elimination estimate.

Conclusion: **NOT-COMPOSABLE** from the verified existing mathlib calls. This is a bounded
experimental conclusion plus the pinned API audit, not a proof of global library absence.
A call to the newly proved size_remainder is not an existing-mathlib replacement. The private
reduction helper cannot be counted as a library call to turn the outer induction into a
≤3-call composition. No closing simp composition was found.

Native edge checks passed for nonmonic f, f=1, P=0, f=0, inferred nonnegativity of A,C,
saturation at zero, recovery of the exact original signature, and necessity of the final
elimination. The first edge probe incorrectly treated successful simp progress as closure;
its full rejected source/receipt are preserved. Replacing it by a solve wrapper tests actual
closure and the entire edge batch reran cleanly. No recovered error or axiom from a rejected
run is counted as accepted proof evidence.

## Phase 7 — verdict and action

**BORDERLINE-needs-human.** The mathematical gap is concrete: quantitative coefficient-size
inflation under monic reduction and its saturated degree-counted iteration. Existing pinned
mathlib supplies the division recurrence, degree descent, size laws and coefficient-size
representations, but the full bound was not found or verified as an existing composition.
The exact integer argument appears in the local source, and external polynomial-height
literature makes division growth relevant beyond Roth. One local caller is not evidence
that the new generic estimate is merely an existing-call wrapper.

The design question is the primary public size interface and helper boundary. The explicit
size theorem is actually proved and its norm specialization works at the real caller. A
RingSeminorm statement is a natural source-supported alternative, while Polynomial.supNorm
may be the preferred intrinsic formulation; neither alternative is presented as a compiled
replacement here. This verdict is about mathematical organization, not proof cost, failed
inlining, or lack of effort to verify generality.

1. Should the quantitative coefficient estimate be public in the direct SeminormedRing form,
   or should a RingSeminorm-parametric statement be the primary API?
2. Should the primary statement bound Polynomial.supNorm and derive coefficient estimates,
   or retain supplied coefficient bounds A and C?
3. Should the one-step reduction estimate be public reusable API alongside the iterated
   bound, or remain a private helper?

Retain the theorem and its actual caller locally. For an upstream proposal, resolve these
three choices, compile the selected bundled/intrinsic formulation, then run
`/generalise Roth.norm_coeff_modByMonic_le` and
`/cleanup Roth/MainLemma.lean Roth.norm_coeff_modByMonic_le`.
A plausible new leaf module is `Mathlib/Analysis/Polynomial/Division.lean`, importing norm
size API and algebraic division rather than putting analysis imports into foundational Div.
This is a proposed home, not an approved import-layer change. No YES PR grouping is claimed.
Pinned recent history records Juan C.'s monic-division linearity work8fc07d3bcd and Snir Broshi's
noncommutative generalization bfe34f170d; these are relevant future reviewer leads, not claims
of consent. [reviewer-history.json](../evidence/Roth.norm_coeff_modByMonic_le/reviewer-history.json).

## Phase 8 — completion and verification

All mandatory phases are complete; optional ask_chatgpt_math and definition-only checks have
justified n/a. Accepted native receipts are full and clean, with standard axioms. The original
warming response and two rejected experiments are explicitly separated. No production source
or pin changed, no resource limits were raised, and no new axiom/sorry/unsafe/native_decide
is accepted. Both scratch and simulated integrated layouts are validated with the current
manifest; links target the integrated evidence prefix. The secret guard must pass before
freeze and native release.

[assessment.json](../evidence/Roth.norm_coeff_modByMonic_le/assessment.json),
[verification.json](../evidence/Roth.norm_coeff_modByMonic_le/verification.json),
[validate.py](../evidence/Roth.norm_coeff_modByMonic_le/validate.py),
[copy-manifest.json](../evidence/Roth.norm_coeff_modByMonic_le/copy-manifest.json),
[final-validation.json](../evidence/Roth.norm_coeff_modByMonic_le/final-validation.json).
