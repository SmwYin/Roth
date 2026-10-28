# `Roth.pow_rootMultiplicity_le` — YES-but-generalise-first

Canonical declaration197 at `Roth/Theta.lean:206`; full overview/mathlibable assessment, production unchanged. Root acceptance pending.

## Phase 0 — Doctor

All17 freshly computed source/pin hashes match the successful exit0 baseline (2467 jobs). [Fresh hashes](../evidence/Roth.pow_rootMultiplicity_le/source-hashes.json), [baseline](../evidence/Roth.pow_rootMultiplicity_le/baseline-build.txt), [manifest](../evidence/Roth.pow_rootMultiplicity_le/input-manifest.json). Full985-line module and complete sole caller read; [source](../evidence/Roth.pow_rootMultiplicity_le/source-Theta.lean.txt). The public theorem is a substantive arithmetic bound and passes no prefilter. It resolves without recovered placeholders.

## Phase 1 — Comprehend

For a nonzero integer polynomial, write a rational point as a reduced fraction `h/q` with positive natural denominator. If its multiplicity is `t`, the absolute leading coefficient is at least `q^t`. Consequently any real bound `B` on that absolute leading coefficient also bounds `q^t`. The formal theorem allows `t=0`, so the point need not be a root.

```lean
∀ {R : Polynomial ℤ},
  R ≠ 0 →
    ∀ {h : ℤ} {q : ℕ},
      0 < q →
        IsCoprime h ↑q →
          ∀ {B : ℝ},
            |↑R.leadingCoeff| ≤ B →
              ↑q ^ Polynomial.rootMultiplicity (↑h / ↑q)
                (Polynomial.map (Int.castRingHom ℚ) R) ≤ B
```

[Native full type](../evidence/Roth.pow_rootMultiplicity_le/native-type.json), [original receipt](../evidence/Roth.pow_rootMultiplicity_le/root-bound197-original-receipt.json), [exact source and ordered canonical audit](../evidence/Roth.pow_rootMultiplicity_le/root-bound197-original-executed.lean.txt). No ambient `σ`, finiteness or decidable-equality instance occurs in the full type. Standard axioms only. The complete kernel proof is printed in the original receipt.

The proof gets `R=(qX-h)^t Q` from project declaration196, computes leading coefficients as `q^t lc(Q)`, deduces `lc(Q)≠0` from `R≠0`, and uses the discreteness of ℤ to obtain `1≤|lc(Q)|`. Casting and absolute-value multiplication finish the inequality. The theorem genuinely uses only a leading-coefficient bound; the docstring's all-coefficients wording is sufficient but stronger than its formal assumption.

## Phase 2 — Preliminary

SMALL: helper for Lemma5, no new structure and not itself a named main module result. Its multiline proof includes integer discreteness and factor normalization. One-line definition-only check: n/a, theorem. A single explicit caller prompts the composition check below; it does not establish redundancy.

## Phase 3 — Exhaustive literature

Exact requests, returned-response UTF-8 SHA256/bytes/status, returned URLs/titles and original concise summaries are archived, without article or search-result bodies: [general web](../evidence/Roth.pow_rootMultiplicity_le/web-0.json), [nLab/nCatLab/Stacks](../evidence/Roth.pow_rootMultiplicity_le/web-1.json), [MO/arXiv](../evidence/Roth.pow_rootMultiplicity_le/web-2.json), [primary access](../evidence/Roth.pow_rootMultiplicity_le/web-primary.json).

| Channel | Exact query / locator | Finding |
|---|---|---|
| General specific | `rational root multiplicity denominator power leading coefficient integer polynomial` | Rational-root and repeated-factor coefficient comparison. |
| General abstract | `Gauss lemma rational root theorem multiplicities GCD domain fraction field` | Gauss descent over fraction fields; GCD-domain generalization relevant. |
| General alias | `rational zeros theorem repeated roots denominator divides leading coefficient power` | Rational-zero / rational-root names, integral linear factors. |
| ChatGPT math | Tool inventory | n/a: `ask_chatgpt_math` unavailable. |
| Local | `clean.tex` §5, lines676–699 | Exact factor descent followed by leading-coefficient bound. [Hash/locator](../evidence/Roth.pow_rootMultiplicity_le/local-literature.json), [excerpt](../evidence/Roth.pow_rootMultiplicity_le/clean-lemma5-excerpt.tex.txt). |
| nLab | `site:ncatlab.org/nlab rational root theorem Gauss lemma` | Rational-zero theorem and roots pages returned; direct Gauss-lemma page failed to fetch. |
| nCatLab | `site:ncatlab.org/ncatlab rational roots polynomial multiplicity` | Explicit distinct namespace queried; returned results outside namespace, no exact nCatLab theorem located. |
| Stacks | `site:stacks.math.columbia.edu Gauss lemma primitive polynomial`; direct tag00EZ | Direct Example10.27.2 succeeds, using Gauss descent; not the exact bound. |
| MathOverflow | `site:mathoverflow.net rational root multiplicity denominator polynomial leading coefficient` | Root multiplicities, coefficient-height and rational-root discussions; related rather than exact. |
| Recent arXiv | `site:arxiv.org rational root theorem multiplicity denominator after:2021-10-27 before:2026-10-28` | Mostly unrelated recent root/denominator papers. Some older identifiers returned despite filters; no completeness or absence inference. |

Primary [Garrett, *Polynomials over UFDs*](https://www-users.cse.umn.edu/~garrett/m/algebra/notes_2023-24/12.pdf), §12.2 Lemma2.0.2 and Corollary2.0.3, printed pp183–184, proves content multiplicativity and fraction-field factor descent. [Stacks Example10.27.2, tag00EZ](https://stacks.math.columbia.edu/tag/00EZ), lines22–25, applies Gauss lemma over ℤ. The specific multiplicity denominator-power divisibility is an inference from repeated integral factor descent, independently formalized here; neither source is represented as stating the exact numeric theorem. nLab access failure is retained honestly.

Synthesis: rational-root theorem with multiplicity. Algebraically, a reduced denominator raised to the root multiplicity divides the leading coefficient over a GCD domain. Numerically, integer coefficient discreteness turns divisibility into an absolute-value lower bound in an ordered target. The proof does not require real completeness or analytic structure. Do not transfer the numerical bound to arbitrary coefficient domains without a discrete lower bound on nonzero coefficients.

## Phase 4a — Parameters and hypotheses

| Parameter / hypothesis | Audit |
|---|---|
| `R : ℤ[X]` | Arbitrary polynomial, no degree, monic, primitive or coefficient-height assumption. Integer discreteness matters for numerical comparison. The algebraic divisibility layer generalizes independently to any GCD domain. |
| `hR : R≠0` | Essential to the numerical statement: zero polynomial has multiplicity0 and leading coefficient0, so `2^0≤0` fails. Checked native counterexample. Generic divisibility layer allows `R=0`. |
| `h : ℤ` | Numerator arbitrary, including negative/zero; general divisor theorem has `h:A`. |
| `q : ℕ` | Can become a signed integer denominator with `|q|` on the left in the numeric law; algebraic layer uses arbitrary `q:A`. |
| `hq : 0<q` | Removable from numerical law. At `q=0`, `0^t≤1≤|lc(R)|` for every natural `t`; no positivity/multiplicity inference is needed. Existing-context and independent mathlib-only proofs check this. |
| `hcop : IsCoprime h ↑q` | Use `IsRelPrime h q`; it is equivalent to `IsCoprime` over ℤ, while genuinely weaker over general GCD domains. Only primitive-factor reducedness matters. Cannot delete reducedness: `h=q=2,R=X−1` gives multiplicity1 and false `2≤1`. |
| `B : ℝ`, `hB` | Remove the arbitrary bound parameter from the core theorem and conclude directly against `|lc(R)|`; transitivity recovers any `B`. No separate `B≥0` is necessary. |
| ℚ/map | Algebraic law works in any fraction field via `algebraMap`; its proof checks arbitrary characteristic and GCD domain. Numeric specialization keeps ℤ/ℚ and replaces only the ordered comparison codomain. |
| Real target | General ordered ring target verified in the stronger probe; no topology, completeness, norm or Archimedean hypothesis. |
| Algebraic floors | CommRing/IsDomain/IsGCDMonoid and fraction-field assumptions supply primitive factor descent. No arbitrary-semiring, zero-divisor, or arbitrary-localization weakening claimed. |
| Ambient variable instances | Absent from native type; none to drop. |

## Phase 4b — Verified generality

STRICTLY NARROWER. Independently checked numeric generalization permits signed denominators, relative primality (equivalent reducedness over ℤ), no positivity, a general ordered comparison ring, and no extraneous bound parameter. The arithmetic proof is mechanically transferred to the divisor API rather than rebuilding a project definition. The complementary algebraic theorem is:

```lean
theorem Polynomial.pow_denominator_dvd_leadingCoeff
    {A K : Type*} [CommRing A] [IsDomain A] [IsGCDMonoid A]
    [Field K] [Algebra A K] [IsFractionRing A K]
    {R : Polynomial A} {h q : A} (hq : q ≠ 0) (hcop : IsRelPrime h q) :
    q ^ Polynomial.rootMultiplicity (algebraMap A K h / algebraMap A K q)
      (R.map (algebraMap A K)) ∣ R.leadingCoeff
```

The independently checked numerical statement is:

```lean
theorem Polynomial.abs_pow_rootMultiplicity_le_abs_leadingCoeff
    {L : Type*} [Ring L] [LinearOrder L] [IsStrictOrderedRing L]
    {R : Polynomial ℤ} (hR : R ≠ 0) {h q : ℤ} (hcop : IsRelPrime h q) :
    |(q : L)| ^ Polynomial.rootMultiplicity ((h : ℚ) / q)
      (R.map (Int.castRingHom ℚ)) ≤ |(R.leadingCoeff : L)|
```

Removing the `B` envelope is equivalent conclusion packaging, not additional arithmetic content. Relative primality is equivalent to Bézout coprimality over ℤ; its strict weakening is in the arbitrary GCD-domain algebraic statement. Ordered target generalization changes the comparison codomain only, preserving integer coefficients.

The numerical statement and original specialization are in [accepted exact proof evidence](../evidence/Roth.pow_rootMultiplicity_le/verification.json). Its copied196 factor theorem and the new denominator-divisibility theorem are **new proofs**, never existing mathlib replacements. The separate algebraic law retains `q≠0`: at `q=0,h=1,R=X`, multiplicity at total division `1/0=0` is1, making `0∣1` false. Removing positivity from the numerical law does not remove nonzero denominator from this algebraic law.

## Phase 4c — Modern idiom

| # | Diagnostic | Answer and downstream consequence |
|---|---|---|
| 1 | Typeclasses | Yes: generic ordered target plus GCD-domain/fraction-field algebraic layer. Real analysis is absent from the bound. |
| 2 | Filters/nets | No limit or topology. |
| 3 | Universal properties | Existing `IsFractionRing` and algebra maps suffice; no construction to replace. |
| 4 | Bundled structures | Divisibility packages the quotient witness and composes with existing `leadingCoeff_dvd_leadingCoeff`; no custom subset. |
| 5 | Weaker hierarchy | Yes: no Real-specific structure; GCD-domain algebraic theorem avoids UFD-only chosen num/den representation. |
| 6 | Higher categories | No categorical coherence. |
| 7 | Concrete indices | Multiplicity is a natural exponent, intrinsic here; not a finite indexing constraint. |
| 8 | Concrete-via-abstract | Yes after factor descent for the algebraic part; numerical comparison still uses genuine ℤ discreteness. [Body/count diagnostic](../evidence/Roth.pow_rootMultiplicity_le/concrete-abstract-diagnostic.json). Full generic proof, rather than disappearance counts alone, supplies evidence. |
| 9 | False-generalization guard | Pass for proposed signature: exact original recovered; q0 handled numerically; signed q uses absolute value. Checked guards refute arbitrary rational-coefficient numerical comparison and q0 algebraic divisibility. |

Modern formulation yields `q^t∣lc(R)` usable with `dvd_trans`, coefficient divisibility and monicity/unit APIs over general GCD domains. Integer absolute-value comparison then works in ordered rings without importing real analysis. Full actual caller accepts the generalized numeric statement. This is a substantive organization improvement; it does not assert that every ring has nonzero coefficients of absolute value at least1.

## Phase 4.5 — Infrastructure risk

All six risks are n/a for this theorem: no global typeclass instance/diamond; no reducible definition; no unfolding alias; no instance priority; no new universe-bearing data; no coercion declaration. Generic `Type*` parameters actually elaborate. Internal classical choice of normalized gcd is proof data and absent from the strongest algebraic theorem's signature.

## Phase 4.6 — Proof strategy

| # | Diagnostic | Answer / proposed strategy |
|---|---|---|
| 1 | Topological ε–δ | n/a. |
| 2 | Algebra elements vs structure | Prefer leading-coefficient divisibility to choosing an explicit quotient and calculating its nonzero leading coefficient. The normalization of the linear leading coefficient remains real proof. |
| 3 | Sequences/nets | n/a. |
| 4 | Universal property | Existing fraction-field structure suffices. |
| 5 | Missing helpers | Generic multiplicity linear-factor descent from196 and resulting denominator-power leading-coefficient divisor are useful upstream API; new helpers checked independently. |

REFACTOR-RECOMMENDED: factor descent → leading-coefficient divisibility → integer natural-absolute-value comparison → ordered cast. Mechanical proof transfer is moderate; cost does not determine the verdict. The original proof is mathematically sound and idiomatic, but the separated algebraic law enables additional coefficient domains without a false numeric generalization.

## Phase 5 — All five mathlib methods on three forms

[12 exact formal requests and raw complete responses](../evidence/Roth.pow_rootMultiplicity_le/formal-search.json) and three full CLI receipts supply15 cells:

| Form | Finder | Loogle | LeanSearch | rg | Local |
|---|---|---|---|---|---|
| Current | Denominator power ≤ absolute leading coefficient | `Polynomial.rootMultiplicity, _ ≤ _` | Integer rational-root multiplicity bound | [Current](../evidence/Roth.pow_rootMultiplicity_le/rg-current.json) | `rootMultiplicity` |
| Literature | Multiplicity rational-root divisor | `Polynomial.rootMultiplicity, _ ∣ _` | Reduced denominator power divides leading coefficient | [Standard](../evidence/Roth.pow_rootMultiplicity_le/rg-standard.json) | `den_dvd_of_is_root` |
| Abstract | GCD/fraction-field multiplicity divisor | `Polynomial.leadingCoeff, _ ∣ _` | Primitive linear-power coefficient divisibility | [Abstract](../evidence/Roth.pow_rootMultiplicity_le/rg-abstract.json) | `leadingCoeff_dvd` |

Local returns `index:unavailable` with fallback hits, not an absence certificate. Some external search signatures are older: generic Gauss descent in pinned source/native check requires only the divisor primitive, whereas Finder/LeanSearch reported both polynomials primitive. Pinned source/native evidence controls.

Pinned positives, [source archives/hashes](../evidence/Roth.pow_rootMultiplicity_le/mathlib-inputs.json), checked in [native verification](../evidence/Roth.pow_rootMultiplicity_le/verification.json):

- `Polynomial.pow_rootMultiplicity_dvd`, `Mathlib/Algebra/Polynomial/Div.lean:538`: monic field-factor power; no integer denominator descent.
- `Polynomial.leadingCoeff_dvd_leadingCoeff`, `Mathlib/Algebra/Polynomial/Degree/Operations.lean:720`: divisor-to-leading-coefficient transport; requires the actual integral polynomial divisor first.
- `Polynomial.leadingCoeff_pow`, same module:717, and `Polynomial.leadingCoeff_linear`, `Mathlib/Algebra/Polynomial/Degree/SmallDegree.lean:84`: normalize divisor leading coefficient, the latter requires nonzero linear coefficient.
- `Polynomial.IsPrimitive.dvd_of_fraction_map_dvd_fraction_map`, `Mathlib/RingTheory/Polynomial/GaussLemma.lean:299`: Gauss descent, needs primitivity and mapped divisibility.
- `den_dvd_of_is_root`, `Mathlib/RingTheory/Polynomial/RationalRoot.lean:89`: UFD reduced chosen denominator divides leading coefficient at a root. Covers a single denominator factor, not its full multiplicity power, and uses the chosen `IsFractionRing.den` representation.
- `Int.natAbs_le_of_dvd_ne_zero`, `Mathlib/Data/Int/Basic.lean:85`, and `Int.le_abs_of_dvd`, `Mathlib/Algebra/Order/Ring/Abs.lean:282`: integer divisor inequalities once correct divisibility is established.
- `one_le_pow_mul_abs_eval_div`, `Mathlib/Algebra/Polynomial/DenomsClearable.lean:86`: lower bound for **nonzero evaluation** after clearing denominators; a rational root has zero evaluation, so it does not supply the multiplicity leading-coefficient bound.

Bounded conclusion: related rational-root, Gauss, coefficient and integer-order building blocks located; none of the retrieved statements is an exact numerical or multiplicity-power replacement. Native mismatch experiments verify the identified bridges, without asserting global theorem absence.

## Phase 5.5 — Statement shape

Normal forms compared: arbitrary real `B` bound, direct leading-coefficient inequality, and denominator-power divisibility. Prefer direct numeric inequality as the arithmetic core and the separate generic divisor law as algebraic foundation. This is not a pairwise equivalence proliferation; no iff normal-form RHS issue arises.

Syntactic generality actually attempted: remove `hq`; remove `B` from core; signed denominator/relative-prime form; ordered target; generic GCD-domain divisor. The old exact caller proof checks against the new direct bound plus `.trans hB`. Superfluous-argument audit is the complete Phase4a table: numeric positivity removed, `B` is conclusion transitivity, nonzero and reducedness retained with guards, ambient σ classes absent. Overall RESTATE-BEFORE-SHIP, preserving ℤ coefficient discreteness for numerical comparison.

## Phase 6.0 — Callers and inline audit

| Caller | Explicit use |
|---|---|
| `Roth/Theta.lean:245`, private `Roth.index_unique_le_log_div` | Supplies nonzero univariate polynomial, positive denominator from `q>1`, coprimality and leading-coefficient bound; takes logarithms of the result. |

One explicit within-file use; zero callers outside declaring module. Complete canonical inventory plus fresh lexical enumeration, `rg --no-ignore` and tracked `git grep` agree: [callers](../evidence/Roth.pow_rootMultiplicity_le/callers.json), [git](../evidence/Roth.pow_rootMultiplicity_le/git-callers.json), [lexical](../evidence/Roth.pow_rootMultiplicity_le/lexical-enumeration.json). Ordered293 kernel-value audit independently gives one direct consumer `_private.Roth.Theta.0.Roth.index_unique_le_log_div`, no direct type consumers. These counts are distinct from all opaque/simp dependency closure.

[Inline audit](../evidence/Roth.pow_rootMultiplicity_le/inline-audit.json): integer nonzero-coefficient lower bounds recur in determinant-factor coefficient control (`index_det_le`) and coefficient-norm infrastructure; these do not reconstruct the rational-root multiplicity bound. No other explicit equivalent inline derivation located in the complete production inventory.

The complete sole caller, including univariate-map and rootMultiplicity transport to ℝ and logarithm/division steps, was rebuilt with the newly generalized bound: [exact executed source](../evidence/Roth.pow_rootMultiplicity_le/root-bound197-fullcaller-executed.lean.txt), [clean receipt](../evidence/Roth.pow_rootMultiplicity_le/root-bound197-fullcaller-receipt.json). This is a real fullcaller experiment, not only an application-shaped example.

## Phase 6 — Composition

Attempt1, `Polynomial.pow_rootMultiplicity_dvd`: native negative check confirms wrong output (field polynomial divisibility, not a numeric bound). Attempt2, `Polynomial.leadingCoeff_dvd_leadingCoeff (Polynomial.pow_rootMultiplicity_dvd ...)`: native negative check confirms missing integral denominator-factor bridge. Both then close with the newly proved generalized bound; new helpers are explicitly excluded from mathlib call counting.

Attempt3, classical `den_dvd_of_is_root` plus integer absolute-value comparison: retrieved theorem supplies only exponent1 and a chosen denominator, requires an actual root rather than allowing multiplicity0, and does not directly identify the input pair `h,q`. Multiplicity iteration and representation transport are extra mathematical work. Attempt4, generic Gauss descent + coefficient divisor + integer comparison: primitivity of the power and field-factor normalization are necessary premises. The checked independent proof performs these explicitly; no ≤3-existing-mathlib-call term was verified. This is bounded evidence about actual candidates, not an impossible-proof or global absence claim.

The project196 factor theorem plus leading-coefficient arithmetic makes the original bound short, but project helpers and their newly transferred generalizations are not existing mathlib blocks. No closing `simp [defs...]` composition was found; if one were found, Phase6b would require BORDERLINE treatment. No ≤3-existing-mathlib-call proof verified on the tested existing API; the gap is the generic multiplicity integral-factor/divisor bridge, and the useful numeric corollary retains substantive integer discrete-order content.

## Phase 7 — Verdict and concrete upstream plan

**YES-but-generalise-first**, reasons LITERATURE-WEAKENING and MODERN-IDIOM. The independently compiled proof removes positivity, uses relative primality (equivalent over ℤ), permits signed denominators and general ordered comparison rings. The primary algebraic layer exposes full denominator-power divisibility over a GCD domain. No three-existing-call derivation of that multiplicity bridge from the retrieved first-order rational-root, field root-factor and leading-coefficient APIs was verified.

Propose numeric theorem `Polynomial.abs_pow_rootMultiplicity_le_abs_leadingCoeff` with signed `h q:ℤ`, `IsRelPrime h q`, `R≠0`, and a generic ordered ring target, concluding directly against `|lc(R)|`; exact checked signature is in verification. Keep its `B`-bounded spelling as project transitivity. Companion `Polynomial.pow_denominator_dvd_leadingCoeff` is stated above. Generic algebraic home: `Mathlib/RingTheory/Polynomial/RationalRoot.lean`, after the accepted196 proposed general factor law and with its planned GaussLemma import; numerical corollary home: new `Mathlib/NumberTheory/Polynomial/RationalRootBound.lean`, importing RationalRoot and the ordered integer/absolute-value API. This keeps Real analysis outside the algebraic core. The numeric new-file path is a concrete proposal, subject to upstream import-layer review. Keeping the algebraic corollary after its proposed factor-law parent avoids a reverse GaussLemma-to-RationalRoot dependency or cycle.

Proposed PR title: **feat(Polynomial): rational root multiplicity denominator divisibility and bounds**. Group with already accepted YES declaration196 `Roth.exists_eq_pow_mul_of_rootMultiplicity` (confirmed progress PASS); [accepted grouping](../evidence/Roth.pow_rootMultiplicity_le/accepted-grouping.json). The two private primitivity helpers194–195 are not relabelled YES merely because their proofs are useful. The group should expose the general factor law, its leading-coefficient divisor, then the discrete integer numeric corollary.

Before PR: `/generalise Roth.pow_rootMultiplicity_le`; `/cleanup Roth/Theta.lean Roth.pow_rootMultiplicity_le`; review file layering/naming; choose reviewer from relevant pinned history. [History](../evidence/Roth.pow_rootMultiplicity_le/reviewer-history.json) includes Junyan Xu's normalization weakening (`2f35248703`,2026-07-08) and Justus Springer's primitive-polynomial `mem_lifts` addition (`e4c37418a1`,2026-03-05); Justus Springer is a well-matched potential reviewer, with Junyan Xu relevant for hierarchy review. No reviewer contact or PR creation performed.

The sole caller migration is concrete: replace `pow_rootMultiplicity_le hR (Nat.zero_lt_of_lt hq) hh hRB` by the checked generalized bound specialized to ℝ and `q:ℤ`, normalize the natural cast absolute value, then `.trans hRB`; all surrounding logarithm work stays as verified. No production edit is part of this assessment.

## Phase 8 — Verification and delivery

[Verification ledger](../evidence/Roth.pow_rootMultiplicity_le/verification.json) links exact executed source bytes and complete native receipts, scoped to each target-specific native region. Rejected attempts are retained separately and never counted as proof. No sorry/admit/new axioms/unsafe/native_decide/limit raises; standard axioms only in accepted proofs. Fresh17 source/pin hashes, ordered293 canonical audit, all15 search cells, literal evidence links, current artifact hashes/bytes, required overview keys, and credential scan are enforced by the [portable validator](../evidence/Roth.pow_rootMultiplicity_le/validate.py). Assessment complete with no verification unresolved items; root independent acceptance pending.
