# `Roth.exists_eq_pow_mul_of_rootMultiplicity` — YES-but-generalise-first

Declaration196, `Roth/Theta.lean:184`. Full read-only overview and mathlibable assessment. Root acceptance pending.

## Phase 0 — Doctor

All17 freshly computed source/pin hashes match the successful exit0,2467-job baseline. [Fresh hashes](../evidence/Roth.exists_eq_pow_mul_of_rootMultiplicity/source-hashes.json), [baseline](../evidence/Roth.exists_eq_pow_mul_of_rootMultiplicity/baseline-build.txt), [manifest](../evidence/Roth.exists_eq_pow_mul_of_rootMultiplicity/input-manifest.json). The complete985-line declaring module and full sole caller were read. [Module](../evidence/Roth.exists_eq_pow_mul_of_rootMultiplicity/source-Theta.lean.txt). The public theorem is not an obvious prefilter or inherited glue law. No production edits.

## Phase 1 — Comprehend

Let `R ∈ ℤ[X]`, and let `h/q` be a reduced fraction with positive natural denominator. If `t` is its root multiplicity in `R` viewed over ℚ, then `(qX-h)^t` divides `R` over ℤ. The conclusion supplies an integer polynomial quotient, with the equality oriented `R = factor * Q`.

```lean
∀ {R : Polynomial ℤ} {h : ℤ} {q : ℕ},
  0 < q →
    IsCoprime h ↑q →
      ∃ (Q : Polynomial ℤ),
        R =
          (Polynomial.C ↑q * Polynomial.X - Polynomial.C h) ^
              Polynomial.rootMultiplicity (↑h / ↑q) (Polynomial.map (Int.castRingHom ℚ) R) *
            Q
```

[Full native type](../evidence/Roth.exists_eq_pow_mul_of_rootMultiplicity/native-type.json), [original native receipt](../evidence/Roth.exists_eq_pow_mul_of_rootMultiplicity/root-factor196-original-receipt.json), [exact executed source](../evidence/Roth.exists_eq_pow_mul_of_rootMultiplicity/root-factor196-original-executed.lean.txt). `R`, `h`, `q`, positivity and coprimality are all parameters; ambient variable-type finiteness/decidable equality instances are absent from the actual type. There is **no nonzero-polynomial hypothesis**, despite the docstring's narrower prose. Zero is allowed; this is not a missing-assumption error. The formal conclusion also does not promise `Q ≠ 0`.

The proof sets `t`, maps `qX-h` to `q(X-h/q)`, obtains primitivity of its power from the two private project lemmas `Roth.isPrimitive_linear` and `Roth.isPrimitive_pow`, applies Gauss divisibility descent, cancels the nonzero rational constant factor and invokes `Polynomial.pow_rootMultiplicity_dvd`. The original proof and full type were printed without elision. Exact ordered293-name kernel audit:293 unique/present/value-bearing constants, one direct value consumer `Roth.pow_rootMultiplicity_le`, no direct type consumers. Source callers and direct kernel consumers are separate measurements.

## Phase 2 — Preliminary

SMALL: a supporting rational-root-factor lemma, not one of the module's stated main Θ results and not a new structure. One internal call is a reason to inspect abstraction quality, not a proof of redundancy. One-line definition-only test: n/a, theorem. Its13 substantive source proof lines include a genuine factor normalization/descent argument.

## Phase 3 — Exhaustive literature

Exact requests, UTF-8 returned-response SHA256/bytes/status, titles/URLs and original summaries are retained. No article/search-result bodies are archived: [general](../evidence/Roth.exists_eq_pow_mul_of_rootMultiplicity/web-0.json), [nLab/nCatLab/Stacks](../evidence/Roth.exists_eq_pow_mul_of_rootMultiplicity/web-1.json), [MO/arXiv](../evidence/Roth.exists_eq_pow_mul_of_rootMultiplicity/web-2.json), [focused retries](../evidence/Roth.exists_eq_pow_mul_of_rootMultiplicity/web-3.json), [failed primary opens](../evidence/Roth.exists_eq_pow_mul_of_rootMultiplicity/web-primary.json), [primary access](../evidence/Roth.exists_eq_pow_mul_of_rootMultiplicity/web-primary2.json).

| Channel | Actual query / locator | Finding |
|---|---|---|
| General specific | `Gauss lemma rational root multiplicity primitive polynomial (bX-a) power integer divides` | Rational root representative `bX-a` and Gauss descent. |
| General multiplicity | `rational root theorem multiplicity denominator power leading coefficient GCD domain` | Classical denominator/leading coefficient result; multiplicity requires repeated factor descent. |
| General abstract/alias | `primitive polynomial divides over fraction field GCD domain Gauss lemma` | Gauss lemma commonly taught for UFDs; GCD-domain abstraction is pertinent. |
| ChatGPT math | Tool inventory | n/a: `ask_chatgpt_math` unavailable. |
| Local reference | `clean.tex` §5, lines676–699, Lemma5 proof | Exact `(qX-h)^t` primitive/fraction-field divisor argument. [Hash/locator](../evidence/Roth.exists_eq_pow_mul_of_rootMultiplicity/local-literature.json), [excerpt](../evidence/Roth.exists_eq_pow_mul_of_rootMultiplicity/clean-lemma5-excerpt.tex.txt). |
| nLab | `site:ncatlab.org/nlab Gauss lemma primitive polynomial GCD domain` | GCD-domain, content and rational-zero-theorem results. Direct XHTML page opens failed HTTP400; search content returned. |
| nCatLab | `site:ncatlab.org/ncatlab primitive polynomial Gauss lemma fraction field` | Actual distinct namespace query returned /nlab pages outside the requested namespace, no exact nCatLab hit. |
| Stacks | `site:stacks.math.columbia.edu Gauss lemma primitive polynomial`; focused retry `site:stacks.math.columbia.edu "Gauss" "polynomial"` | Initial combined response gave no Stacks hit; retry and direct tag00EZ open succeeded. Related descent application, not the full multiplicity statement. |
| MathOverflow | `site:mathoverflow.net rational root multiplicity primitive polynomial Gauss lemma` | Primitive-polynomial/Gauss distinctions beyond gcd domains; supplementary discussion, not foundational proof. |
| Recent arXiv | `site:arxiv.org rational root theorem Gauss lemma primitive polynomial after:2021-10-27 before:2026-10-28`; focused `"Gauss lemma" "GCD"` with same dates | Returned mostly unrelated Gauss-Lucas, primitive-root and rational-approximation material. No exact relevant recent theorem located; no absence inference. |

Primary [Garrett, *Polynomials over UFDs*](https://www-users.cse.umn.edu/~garrett/m/algebra/notes_2023-24/12.pdf), §12.2 Lemma2.0.2 and Corollary2.0.3, pp183–184, gives content multiplicativity and integral factor descent. [Stacks Example10.27.2, tag00EZ](https://stacks.math.columbia.edu/tag/00EZ), lines22–25, uses Gauss lemma for ℤ[X]. Chicago lecture-note open failed404, Stanford open timed out, and nLab direct XHTML opens failed400; all failures are recorded. No full articles were saved.

Synthesis: the content is rational-root factor descent with multiplicity, a standard application of Gauss lemma. Integer coefficients, a natural positive denominator and a chosen ℚ model are unnecessary for this mechanism. A GCD domain and any fraction field suffice; a relatively prime pair means no common nonunit divisor and need not satisfy a Bézout identity. This last distinction matters outside PIDs. The generic proof below is independently verified, rather than inferred merely from literature or names.

## Phase 4a — Every parameter and hypothesis

| Parameter / hypothesis | Audit |
|---|---|
| `R : ℤ[X]` | Replace ℤ by a commutative GCD domain `A`; `R` may be zero. No degree, monicity or primitive assumption on `R` is needed. |
| `h : ℤ` | Arbitrary numerator, including zero/negative. Generic `h : A` uses only ring structure. |
| `q : ℕ` | Generic `q : A` need not have an order or positivity. Original specialization uses the existing natural cast. |
| `hq : 0 < q` | Droppable, actually proved: at `q=0`, coprimality forces `h` to be a unit, so `(-C h)^t` is a unit and divides every `R`; at `q≠0`, use ordinary rational-root factorization. |
| `hcop : IsCoprime h ↑q` | Weaken to `IsRelPrime h q`: only the common-divisor-is-unit consequence is used to prove primitivity. `IsCoprime.isRelPrime` recovers the original. Cannot remove all reducedness: `h=q=2`, `R=X-1` has multiplicity1 at1 but `2X-2` does not divide `X-1` over ℤ. Both parts of this guard were checked. |
| Rational cast/map | Replace by `[Field K] [Algebra A K] [IsFractionRing A K]` and `algebraMap A K`. Injectivity and division, not characteristic0 or rational-specific arithmetic, supply the proof. |
| Generic gcd choice | Strongest public signature needs only `[IsGCDMonoid A]`; a local chosen normalized gcd instance serves existing primitive multiplication internally. No global instance installed. |
| Ambient σ instances | Absent in full native type. No finite-variable assumptions to remove. |
| Structural floors | `CommRing` supplies subtraction/commutative polynomial arithmetic; existing Gauss descent requires `IsDomain` and `IsGCDMonoid`. No claimed arbitrary-ring, semiring, division-ring or arbitrary-localization weakening was compiled. |

## Phase 4b — Generality verdict

STRICTLY NARROWER THAN VERIFIED GENERAL FORM. Positivity drops, the primitive coefficient condition weakens from Bézout coprimality to relative primality, ℤ/ℚ become an arbitrary GCD domain/fraction field, and chosen normalized gcd becomes an existential structure internally. These are actual full-proof checks. The proposed primary statement is:

```lean
theorem Polynomial.pow_linear_dvd_of_rootMultiplicity
    {A K : Type*} [CommRing A] [IsDomain A] [IsGCDMonoid A]
    [Field K] [Algebra A K] [IsFractionRing A K]
    {R : Polynomial A} {h q : A} (hcop : IsRelPrime h q) :
    (Polynomial.C q * Polynomial.X - Polynomial.C h) ^
      Polynomial.rootMultiplicity (algebraMap A K h / algebraMap A K q)
        (R.map (algebraMap A K)) ∣ R
```

The exact original quotient form, with positivity removed, follows as the checked one-line specialization `Factor196GCD.generic (K := ℚ) hcop.isRelPrime` under the exact quotient expected type; the theorem used there is newly proved evidence, **not** an existing mathlib replacement. Proof transfer is mechanical with local map qualifications and one unit branch, with no foundational project definition change or multi-file migration needed to state it. All generic conditions and zero-denominator semantics remain explicit. [Verification](../evidence/Roth.exists_eq_pow_mul_of_rootMultiplicity/verification.json).

## Phase 4c — Modern-idiom check

| # | Question | Answer / consequence |
|---|---|---|
| 1 | Typeclasses instead of concrete preambles | Yes: `IsDomain`, `IsGCDMonoid`, `IsFractionRing` express exactly the abstract descent infrastructure. |
| 2 | Filters/nets | No topology or limits. |
| 3 | Universal-property construction | No new object needed; use the existing fraction-ring class and algebra map. |
| 4 | Bundled substructure | No ad hoc closed subset is being replaced. Divisibility already packages the quotient witness. |
| 5 | Weaker algebraic hierarchy | Yes: GCD domains rather than ℤ or UFD-only numerator/denominator machinery; arbitrary characteristic/fraction field. Enables roots of polynomials over polynomial rings and other GCD domains. |
| 6 | Higher categories | No categorical coherence question. |
| 7 | Concrete index | Multiplicity remains a natural exponent. The natural denominator is a coefficient, not an indexing restriction; generalized by row5. |
| 8 | Concrete-via-abstract diagnostic | Yes by proof transfer. Literal disappearance shortcut alone does not justify it: rational type/cast operations occur on several original body lines. The independent generic proof supplies positive evidence. [Actual counts](../evidence/Roth.exists_eq_pow_mul_of_rootMultiplicity/concrete-abstract-diagnostic.json). |
| 9 | False-generalization guard | Pass: same polynomial factor and same root multiplicity after scalar extension; original is exactly recovered. Do not conflate `IsRelPrime` with Bézout `IsCoprime` on general gcd domains. The `q=0` branch is a unit argument using total division; no assertion that zero is a valid nonzero denominator. |

Modern idiom available: yes. Concrete consequences: `dvd_trans`, polynomial divisibility/leading-coefficient APIs and Gauss descent become usable over any GCD domain without first producing ℤ/ℚ-specific data; the complete original bound caller consumes the generic result unchanged after `hcop.isRelPrime`. This is a real reusable factor-descent law, rather than a category-theoretic rebranding.

## Phase 4.5 — Infrastructure risks

All six definition/instance risks are n/a for a theorem: typeclass diamonds (no instance declared), reducibility leak (no new definition), noncanonical unfolding (no reducible alias), instance-priority collision (no priority), universe issues (generic theorem checks arbitrary `Type*` for `A,K`), coercion ambiguity (no new coercion). Local choice of a normalized gcd instance is internal proof data and absent from the strongest checked signature.

## Phase 4.6 — Proof strategy

| # | Diagnostic | Answer / alternative |
|---|---|---|
| 1 | Topology/ε–δ | No topology. |
| 2 | Element calculations vs substructures | The proof already uses polynomial divisibility and generic Gauss descent. Prefer primary `∣` output to an explicit quotient existential; they are definitionally the same quotient interface. |
| 3 | Analysis/sequences | No analytic convergence. |
| 4 | Category/universal properties | Existing fraction-field structure suffices; no new construction. |
| 5 | Missing helpers | General primitive linear-polynomial criterion and primitive-power closure are useful helper candidates near `Content`; searched source provides `IsPrimitive.mul` and `isPrimitive_one`, not a new existing theorem proved by this assessment. Their native transferred proofs are explicitly new. |

MATHLIB-IDIOMATIC mathematical strategy: primitivity, fraction-field linear factor, then Gauss descent. Refactor presentation before contribution to the generic divisibility statement, retaining the separate unit branch. This does not replace substantive normalization by an alleged one-line theorem. Cost is not the verdict criterion.

## Phase 5 — Five actual methods, three forms

[All12 raw formal-search requests/receipts](../evidence/Roth.exists_eq_pow_mul_of_rootMultiplicity/formal-search.json) plus three complete source-search receipts give all15 cells:

| Form | Finder | Loogle | LeanSearch | rg | Local name search |
|---|---|---|---|---|---|
| Current ℤ/ℚ factor | Rational-root multiplicity factor request | `Polynomial.rootMultiplicity, _ ∣ _` | Rational factor power divides integer polynomial | [Current](../evidence/Roth.exists_eq_pow_mul_of_rootMultiplicity/rg-current.json) | `rootMultiplicity` |
| Literature Gauss/lowest terms | Primitive divisor descends | `Polynomial.IsPrimitive, Polynomial.map, _ ∣ _` | Reduced rational-root factor multiplicity | [Standard](../evidence/Roth.exists_eq_pow_mul_of_rootMultiplicity/rg-standard.json) | `dvd_iff_map_cast_dvd_map_cast` |
| Abstract GCD/fraction field | Coprime linear root-factor power | `Polynomial.IsPrimitive, IsFractionRing, _ ∣ _` | Primitive divisibility in GCD domain | [Abstract](../evidence/Roth.exists_eq_pow_mul_of_rootMultiplicity/rg-abstract.json) | `dvd_of_fraction_map_dvd_fraction_map` |

Local search explicitly reports index unavailable while returning fallback hits; absence does not follow. Finder/LeanSearch returned older signatures requiring **both** polynomials primitive, whereas pinned Loogle/source/native signatures require only the divisor primitive. The pinned evidence controls this assessment.

Pinned positive building blocks, read and checked natively:

- `Polynomial.pow_rootMultiplicity_dvd`, `Mathlib/Algebra/Polynomial/Div.lean:538`: monic factor power over one coefficient ring; does not descend an integer denominator factor.
- `Polynomial.IsPrimitive.dvd_of_fraction_map_dvd_fraction_map`, `Mathlib/RingTheory/Polynomial/GaussLemma.lean:299`, and its iff at309: generic GCD-domain Gauss descent, requiring primitive divisor plus mapped divisibility.
- `Polynomial.IsPrimitive.Int.dvd_iff_map_cast_dvd_map_cast`, same file324: integer specialization of the preceding result.
- `Polynomial.C_mul_dvd`, `Mathlib/Algebra/Polynomial/FieldDivision.lean:579`: cancels a nonzero constant multiplier over a field.
- `Polynomial.IsPrimitive.mul`, `Mathlib/RingTheory/Polynomial/Content.lean:373`, and `Polynomial.isPrimitive_one`: primitive multiplication and the induction base.
- `IsCoprime.isRelPrime`, `Mathlib/RingTheory/Coprime/Basic.lean:183`, and `isRelPrime_zero_right`: reducedness specialization and unit branch.
- `num_dvd_of_is_root`, `den_dvd_of_is_root`, `Mathlib/RingTheory/Polynomial/RationalRoot.lean`: related first-order numerator/denominator coefficient bounds, not the full multiplicity factorization.

[Exact pinned source hashes/archives](../evidence/Roth.exists_eq_pow_mul_of_rootMultiplicity/mathlib-inputs.json). Mathlib-only sources guard the absent project target and never import Roth. A one-time generic `exact?` probe before any generic descent theorem hit the default200000-heartbeat `whnf` limit. A wildcard direct-root-factor probe also exhausted the default limit. These are retained rejected search attempts, **not absence evidence**, and were not repeated or limit-raised. The positive generic proof exposes the exact missing application layer; no universal absence claim is made.

Conclusion: partial matches and building blocks, no verified existing exact or ≤3-call full replacement. The proposed addition is specifically the primitive linear factor raised to the mapped root multiplicity, combining the currently separate Gauss and multiplicity APIs.

## Phase 5.5 — Statement shape

1. Normal form: `a ∣ R` is definitionally `∃ Q, R=a*Q`, with the exact source orientation. The generic divisibility form matches existing `pow_rootMultiplicity_dvd` and Gauss APIs; no equality-orientation bridge is hidden. No `A↔B` orthogonal equivalence is proposed.
2. Syntactic generality: actually checked explicit quotient specialization, generic divisibility, no-positive-denominator form and relative-prime GCD-domain form. Prefer `∣` primary output; `obtain ⟨Q,hQ⟩` still works in the sole caller.
3. Superfluous arguments: `hq` drops by the checked unit branch. Reducedness cannot drop entirely by the checked2/2 counterexample. No `R≠0` to remove or add. Generic field/algebra/fraction-ring/domain/gcd assumptions serve the existing Gauss machinery; no stronger unsupported weakening is claimed.

RESTATE-BEFORE-SHIP: generic divisibility, `IsRelPrime`, no positivity, `[IsGCDMonoid A]`, arbitrary fraction field. Fix the source docstring's nonzero-polynomial wording during a separately authorized cleanup.

## Phase 6.0 — Callers and inline audit

| Explicit caller | Location | Actual experiment / migration |
|---|---|---|
| `Roth.pow_rootMultiplicity_le` | declaration206, call209 in `Roth/Theta.lean` | Entire proof replayed with `obtain ⟨Q,hQ⟩ := Factor196ProjectGCD.original_without_hq (R := R) hcop`; this checked original-type corollary applies the strongest generic law with `hcop.isRelPrime`, then leading-coefficient equality, nonzero-quotient argument, absolute-value estimate and real bound preserved. |

Internal use count1. [Fresh ignore-safe rg](../evidence/Roth.exists_eq_pow_mul_of_rootMultiplicity/callers.json), [tracked git crosscheck](../evidence/Roth.exists_eq_pow_mul_of_rootMultiplicity/root-factor196-git-callers.json), [canonical signature/body enumeration](../evidence/Roth.exists_eq_pow_mul_of_rootMultiplicity/lexical-enumeration.json), [structured caller](../evidence/Roth.exists_eq_pow_mul_of_rootMultiplicity/callers-structured.json). [Inline audit](../evidence/Roth.exists_eq_pow_mul_of_rootMultiplicity/inline-audit.json): no second inline integral `(qX-h)^t` descent in production source; nearby root multiplicity map comparison is a different law. Kernel direct-consumer audit independently agrees on one value consumer and zero type consumers; neither count is claimed to measure opaque transitive/simp dependencies.

## Phase 6 — Actual composition experiments

Attempt1: direct `pow_rootMultiplicity_dvd` does not supply integral denominator-factor descent. The wildcard negative test reached default heartbeats and is retained as rejected, not a proof of failure. A concrete map-only `simpa only [Polynomial.map_pow, Polynomial.map_sub, Polynomial.map_mul, Polynomial.map_C, Polynomial.map_X]` test does not close the original integer quotient form; the complete proof then closes it through the **newly proved** generic law.

Attempt2: Gauss descent plus rational multiplicity divisibility is mathematically right, but needs the primitive-power proof, the scalar-factor identity `map(qX-h)=C q*(X-C(h/q))`, mapped-power rewrites and nonzero-constant cancellation. The generic native proof executes those steps and additionally handles `q=0`. These are actual mathematical bridges, not ≤3 existing calls. Project private helpers are not counted as mathlib building blocks. A generic `exact?` timeout contributes no absence inference.

Conclusion: no ≤3-existing-mathlib-call proof of the full statement was verified in this assessment. This is a bounded search/experiment conclusion, not an impossibility result. The accepted old-form specialization and full sole caller demonstrate that the proposed generic API handles the real downstream requirement. The accepted factor-normalization proof uses qualified polynomial rewrites; a redundant trailing `simp` was removed after those rewrites closed that intermediate equality. This does not close the entire divisibility target, and no closing `simp [defs...]` composition is misclassified as NO.

## Phase 7 — Actionable verdict

**YES-but-generalise-first**, reasons MODERN-IDIOM and verified hypothesis weakening. The precise gap is **primitive linear root-factor divisibility to the full fraction-field root multiplicity over a GCD domain**. Existing `pow_rootMultiplicity_dvd` handles monic factors in one ring; Gauss descent handles arbitrary primitive divisors given a mapped divisibility proof. The new theorem makes their recurring rational-root application available without rebuilding primitive powers and clearing the linear denominator. Its full generic proof, exact original specialization, zero/reducedness guards and complete real-bound caller are independently checked. This verdict does not inherit any earlier declaration's judgment, and is not based on a lemma name, length, expensive work or failed search.

Proposed upstream file: `Mathlib/RingTheory/Polynomial/RationalRoot.lean`, adding the existing `Mathlib.RingTheory.Polynomial.GaussLemma` import. Static pinned import traversal finds no path from GaussLemma to RationalRoot, so this proposed import introduces no cycle; final PR import fanout still needs normal review. [Full1881-module import graph with source hashes](../evidence/Roth.exists_eq_pow_mul_of_rootMultiplicity/root-factor196-import-layer-check.json). Proposed name `Polynomial.pow_linear_dvd_of_rootMultiplicity` is provisional; the full checked signature is in Phase4b. Proposed PR title: **feat(Polynomial): descend linear root factors with multiplicity over GCD domains**.

Group primitive coefficient/power helper additions with accepted YES `Roth.exists_primitive_smul_eq` (172) if a focused content PR benefits; coordinate the GCD fraction-field application with accepted YES `Roth.exists_int_factors` (176), keeping univariate and multivariate modules separate where layering requires. [Fresh accepted grouping](../evidence/Roth.exists_eq_pow_mul_of_rootMultiplicity/accepted-grouping.json). These are accepted records, not guesses from useful names. Suggested reviewer Junyan Xu, based on relevant normalization weakening commit `2f35248703` (2026-07-08), with Anne Baanen as an alternative contributor to these paths. [Recent path history](../evidence/Roth.exists_eq_pow_mul_of_rootMultiplicity/root-factor196-mathlib-reviewer-history.json). Candidates were not contacted.

Before contribution:

- Run `/generalise Roth.exists_eq_pow_mul_of_rootMultiplicity` using the verified relative-prime GCD-domain form; retain the no-positive-denominator result and exact quotient specialization.
- Run `/cleanup Roth/Theta.lean Roth.exists_eq_pow_mul_of_rootMultiplicity`, including docstring consistency, then `/cleanup Mathlib/RingTheory/Polynomial/RationalRoot.lean Polynomial.pow_linear_dvd_of_rootMultiplicity` on the final upstream form/name.
- Review placement/redundancy of generic primitive-linear and power helpers in `Content`; these new proofs are not existing mathlib replacements. Keep Gauss dependencies above foundational polynomial modules.
- Replay `Roth.pow_rootMultiplicity_le` with the upstream generic theorem and `hcop.isRelPrime`; this complete migration is already checked with the evidence theorem.
- Pick a reviewer from relevant recent commits, run appropriate builds/checks and `/pre-submit`.

Until an upstream API is adopted, `Roth/Theta.lean` is the appropriate local destination. No deletion is recommended merely because the original has one caller.

## Phase 8 — Overview and handoff

No junk/dead-code finding. Mathematical overlap with Gauss and root multiplicity is documented; the missing integral linear-factor multiplicity bridge is explicit. The evidence package preserves exact executed sources, full native receipts, rejected attempts separately, fresh source/pin hashes, all search methods and literature channels, exact canonical audit order and a portable read-only validator. [Verification index](../evidence/Roth.exists_eq_pow_mul_of_rootMultiplicity/verification.json), [overview entry](../evidence/Roth.exists_eq_pow_mul_of_rootMultiplicity/overview-entry.json). Rejected attempts are separately indexed: initial map-name/implicit-dividend mistakes, a redundant `simp`, counterexample cast/constant normalization, default-limit searches, inherited namespace ambiguities and direct caller cast spelling. None is accepted proof evidence. The final caller uses an explicitly typed original-form corollary before rewriting, preserving the integer/rational cast interface. Root acceptance remains pending until independent review.
