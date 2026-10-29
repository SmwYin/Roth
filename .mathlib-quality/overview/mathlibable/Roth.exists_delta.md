# Roth.exists_delta — canonical276

Verdict: **BORDERLINE-needs-human**. Keep this parameter choice project-local while the upstream public API granularity is decided. The mathematical and mechanical assessment is complete with all portable gates passing; the three future questions are not a request to pause this overview. This verdict is independent of exists_delta_bound/exists_m and is not based on proof cost.

## Phase0: baseline and scope

The clean2467-job baseline is reusable: fresh checks match all17 tracked production-source/pin hashes. No production Lean/pin/Git/overview/progress changes were made. No new full literal build is due at276; next required file boundary is289. Root exclusively executed every native check and all local searches through its persistent session. Sources and raw request/results retain exact code, hashes and elapsed times.

The target is the public theorem at Main227. The declaring file and the sole actual caller were read in full, together with Main's full continuation and the LeanEval terminal module. Original proof re-elaboration is deliberately **target-only**, in a fresh namespace, with no private-helper closure needed: public project ingredients remain imported. A native theorem equality checks exact original/replay proposition type; proof irrelevance does not assert identical proof construction.

## Phase1: statement and proof

For natural degree n and fixed dimension m>16n², suppose the limiting quotient 2m/(m−4n√m) is strictly below real κ. There is a positive δ below1/m such that both η(δ,m)+2(1+3δ)n√m<m/2 and m(1+4δ)/(γ(δ,n,m)−η(δ,m))<κ. Here η=10^m δ^((1/2)^m), γ=(m−4(1+3δ)n√m)/2. **n may be zero**; **κ>2 is not an input binder**.

Full native type:

```lean
∀ {n m : ℕ},
  16 * n ^ 2 < m →
    ∀ {κ : ℝ},
      2 * ↑m / (↑m - 4 * ↑n * √↑m) < κ →
        ∃ (δ : ℝ),
          0 < δ ∧
            δ < 1 / ↑m ∧
              Roth.eta δ m + 2 * (1 + 3 * δ) * ↑n * √↑m < ↑m / 2 ∧
                ↑m * (1 + 4 * δ) / (Roth.gam δ n m - Roth.eta δ m) < κ
```

The proof first uses exists_delta_bound for the cap and first strict envelope on an interval that includes0. That interval's estimate at0 gives a positive gamma-minus-eta denominator. Continuity of the real-power quotient at0 preserves the second strict inequality; a positive point below the original interval and a metric continuity radius meets both bounds. This is a small-perturbation argument with a genuine limiting gap, not just an arbitrary witness choice.

## Phase2 and4.5: preliminary/risk checks

SMALL: a parameter-selection helper, not a main named result or new structure. One-line definition check is n/a because this is a theorem. Each of the six infrastructure risks (diamond, reducibility, unfolding, priority, universes, coercion) is n/a: the declaration introduces a proof, no instance or data representation. All six are recorded separately in the phase evidence.

## Phase3: exhaustive literature

| Channel | Actual query / outcome |
|---|---|
| web-specific | `Roth theorem proof "delta" "gamma" "eta" small parameters` — The arithmetic-specific query found the primary 2003 Princeton notes, §17.3, equations17.17–17.20: fix m, then shrink delta for positivity and the quotient bound. Most other Roth hits concern additive combinatorics and are irrelevant. |
| web-general | `continuous functions strict inequalities persist neighborhood finite simultaneous inequalities` — Broad simultaneous-inequality search was noisy; no named theorem matching all Roth envelopes emerged. Basic continuity/open-set persistence is the relevant standard principle, checked against primary sources. |
| web-alias | `continuity principle choose sufficiently small positive parameter strict inequality` — NIST DLMF §1.4(ii) gives the classical pointwise continuity framework; sufficiently small positive perturbations are an application, not a separately named Roth result. |
| nlab | `site:ncatlab.org/nlab continuity neighborhood filter open inequality` — Search returns neighborhood/filter topology resources. Direct neighborhood open failed due unsupported application/xhtml+xml; abstract neighborhood vocabulary only, no exact arithmetic theorem. |
| ncatlab | `site:ncatlab.org/ncatlab continuous functions strict inequalities neighborhoods` — The distinct /ncatlab query ran; returned results were in /nlab, outside requested namespace. No exact /ncatlab theorem was obtained; this is a search limitation, not a claim of absence. |
| stacks | `site:stacks.math.columbia.edu continuous function open inverse image topology` — Search returns general topological bases and continuity. Tag0D5Q is a quotient-from-basis construction and does not supply the strict quantitative parameter lemma. |
| mathoverflow | `site:mathoverflow.net continuity strict inequalities sufficiently small parameter` — The continuity/bootstrap question is related strategy discussion; parameterized optimization hits concern different hypotheses. No exact Roth envelope API was established. |
| arxiv | `site:arxiv.org Roth theorem formalization after:2021-10-29 before:2026-10-30` — Date-constrained recent search ran. Results include Carleson formalization and additive-combinatorial Roth criteria; these do not identify an exact simultaneous quantitative delta theorem. Returned old or irrelevant items are excluded as evidence. |
| local | clean.tex, §6 lemma m-delta and §7 equations47–49; full exact query receipt and bounded source excerpt retained. |
| ask_chatgpt_math | n/a: tool unavailable; no reduction of other channels. Historical comparison uses primary2003 notes. |

The specific-form, general-form and alias queries are three actual distinct requests. nCatLab was queried distinctly with site:ncatlab.org/ncatlab; search returned nLab pages, not a claimed nCatLab exact match. Direct nLab fetch failed for unsupported XHTML; that limitation is retained. Recent arXiv used after:2021-10-29 before:2026-10-30, with irrelevant or old returned results excluded as mathematical evidence. No failed or empty search is a proof of absence.

The primary [Princeton seminar notes](https://web.math.princeton.edu/mathlab/jr02/diophantine.pdf), §17.3 pp.151–152 equations17.17–17.20, choose m and then successively decrease δ to preserve a positive denominator and the strict quotient inequality. Their text after17.19 prints k<2 despite the section beginning k>2; this is a typo, and the native theorem uses the explicit strict h47 input. The local modern source has the corrected positive exponent and retains the simultaneous envelopes. [NIST DLMF §1.4(ii)](https://dlmf.nist.gov/1.4) supplies the classical continuity vocabulary; the abstract standard form is persistence of strict inequalities in neighborhoods, with finite intersections. No standalone traditional theorem name for this entire Roth-specific parameter package was established.

Only exact requests, returned-response SHA256/bytes/status, selected clean titles/URLs/locators and original summaries are persisted for web evidence. No article/search body is archived; truncated URLs were omitted. Search-only sources are background, not a substitute for primary mathematical evidence.

## Phases4a–4b: parameter/generality analysis

| Parameter/hypothesis | Concrete assessment |
|---|---|
| n:ℕ | Zero is allowed; native recovery explicitly verifies n=0,m=1. No n>0 premise may be introduced. |
| m:ℕ | hm implies m>0; this is needed for1/m to be a positive cap. Real division by0 is0, so deleting hm admits an impossible positive δ<0 at m=0. |
| hm:16n²<m | Supplies4n<√m, hence strict positive limiting gamma-minus-eta gap. The proof does not merely use m≠0. |
| κ:ℝ | Arbitrary real bound at the interface. No separate κ>2 binder; h47 supplies all needed limiting slack. |
| h47 | Essential strict quotient slack. A native no-zero-upper-bound test proves that positive numerator/positive gap cannot meet a zero strict threshold. This is a counterexample to naive deletion, not a claimed classification of every possible weakening. |
| Fixed constants and named functions | Generic quantitative cap/envelope selection is compiled; actual arithmetic recovery proves continuity, zero values and square-root gap, without calling the target. The concrete arithmetic spelling alone is not evidence for a NO verdict. |

There is no verified removable **original** hypothesis. Modern abstraction is available as a different reusable interface; it is not a mechanical removal of n,m or κ. Strictly positive exponent makes η(0)=0; the native zero-rpow and division conventions are checked before weakening assumptions. Adding all-real generic envelopes is a new proof rather than an existing-mathlib replacement.

## Phase4c: modern idiom, all nine rows

| Question | Answer / downstream consequence |
|---|---|
| Typeclasses | No new bundled assumption: original uses fixed real arithmetic; continuity assumptions in generic schema use existing predicates. |
| Filters | Yes: replace explicit metric radius/minimum by eventually_lt conjunctions and exists_gt; compiled generic schema and exact recovery. |
| Universal properties | No constructed algebraic object or universal mapping property. |
| Bundled structures | No substructure predicate; scalar parameter selection benefits from filters rather than a new bundle. |
| Hierarchy | ContinuousAt.div already works for topological group-with-zero targets; ordered real inequalities/rpow are substantive in arithmetic recovery. |
| Higher categories | No categorical object or morphism. |
| Concrete indices | Natural n,m enter exponent and coefficients; arbitrary continuous envelopes and arbitrary cap verified; do not replace real rpow with a semiring operation. |
| Concrete-via-abstract | Diagnostic executed; generic selection abstractable, but named eta/gam still used in analytic premises and zero values. Actual old recovery retains both quantitative envelopes. |
| False-generalization guard | Passing only an eventual predicate would remove arithmetic work. Accepted generic quantitative schema includes cap, first envelope, numerator/denominator and strict quotient; recovery proves every original premise. |

The mathlib-only generic theorem takes continuous real f,p,q, a positive cap U, bounds f(0)<B and p(0)/q(0)<K, and q(0)≠0. It returns δ>0,δ<U,f(δ)<B,p(δ)/q(δ)<K simultaneously. Its implementation composes eventual inequalities and exists_gt; a separate example verifies that **point selection alone already exists**. The old-recovery proof uses f=η+2(1+3δ)n√m, p=m(1+4δ), q=γ−η. It rebuilds each analytic/quantitative premise, so the abstraction has not discarded the actual Roth content. This replaces explicit metric-radius bookkeeping with filter composition and enables other continuous perturbations to reuse the selection step.

The quantitative abstraction was also checked independently, beyond generic point selection. In mathlib-only19 (stable18 plus root-authorized genuine Pow.Continuity), a **new** theorem allows signed amplitude A, positive real exponent e, real scale M and geometric parameter s, an independent positive cap U, and4s<M with2M/(M−4s)<K. It retains both Aδ^e+2(1+3δ)s<M/2 and M(1+4δ)/((M−4(1+3δ)s)/2−Aδ^e)<K together with0<δ<U. Neither A, M nor s is silently required positive; the limiting denominator gap follows from4s<M, while cap positivity is separate.

The same isolated source reconstructs the **full raw old statement**, with A=10^m, e=(1/2)^m, M=m, s=n√m and U=1/m, using only genuine mathlib operations and proving the square-root gap. It imports no project definitions and guards target absence. A separate native ambient bridge unfolds only eta/gam/lam and proves exact old-type agreement. This distinguishes a reusable semantic amplitude/exponent/scale/cap API from merely changing numeric literals, and avoids mistaking an eventual-predicate transport for complete arithmetic recovery. The full actual caller replacement already verified the identical original signature through the simultaneous-continuity recovery; no additional caller implementation change is asserted for the separate raw-form bridge.

## Phase4.6: proof strategy, all five rows

| Question | Assessment |
|---|---|
| Topology | REFACTOR: eventually_lt + and + exists_gt eliminates radius and exists_between. |
| Algebra | n/a: no ideals/submodules or pointwise ring-map proof. |
| Analysis sequences | No sequence; continuity at0 composes directly, with positive exponent. |
| Universal construction | n/a: no universal-property construction. |
| Missing helper | The generic simultaneous schema is new proof packaging; primitive filter API exists. Whether a quantitative arithmetic-envelope helper merits upstream API remains a design question. |

REFACTOR-RECOMMENDED: use existing filter tools for the selection stage. Whether to expose a named simultaneous helper is a public API question; no cost-based downgrade is made.

## Phase5: all15 formal search cells

| Form | Finder | Loogle | LeanSearch | source rg | local search |
|---|---|---|---|---|---|
| current | [leanfinder](../evidence/Roth.exists_delta/formal-current-leanfinder.json) | [loogle](../evidence/Roth.exists_delta/formal-current-loogle.json) | [leansearch](../evidence/Roth.exists_delta/formal-current-leansearch.json) | [rg](../evidence/Roth.exists_delta/formal-current-rg.json) | [local](../evidence/Roth.exists_delta/formal-current-local.json) |
| standard | [leanfinder](../evidence/Roth.exists_delta/formal-standard-leanfinder.json) | [loogle](../evidence/Roth.exists_delta/formal-standard-loogle.json) | [leansearch](../evidence/Roth.exists_delta/formal-standard-leansearch.json) | [rg](../evidence/Roth.exists_delta/formal-standard-rg.json) | [local](../evidence/Roth.exists_delta/formal-standard-local.json) |
| abstract | [leanfinder](../evidence/Roth.exists_delta/formal-abstract-leanfinder.json) | [loogle](../evidence/Roth.exists_delta/formal-abstract-loogle.json) | [leansearch](../evidence/Roth.exists_delta/formal-abstract-leansearch.json) | [rg](../evidence/Roth.exists_delta/formal-abstract-rg.json) | [local](../evidence/Roth.exists_delta/formal-abstract-local.json) |

Current-form searches are polluted by the unrelated additive-combinatorics Roth theorem; those are rejected as matches. Standard and abstract forms identify ContinuousAt.eventually_lt, Filter.Eventually.and/exists_gt/exists and ContinuousAt.div. Positive candidate signatures are natively checked. All three local calls returned index:error; neither their hits nor empty lists certify complete local index coverage. Remote indices can differ from the pinned mathlib; pinned source excerpts and native compilation verify the candidates actually used.

The strongest confirmed hits cover component steps, not the full eta/gamma envelope theorem in a one-line specialization. The exact isolated code is guarded by #check_failure Roth.exists_delta, and imports no project module. New generic proofs are labelled as new proofs, never cited as pre-existing building blocks.

## Phase5.5: statement shape

| Check | Assessment |
|---|---|
| Normal form | Both gamma-eta quotient and expanded denominator exist; shape02 natively verifies expanded formula. Keep project gamma-eta form for eta_lt_gam_iff downstream; no rewrite loop or new simp family. |
| Syntactic generality | Generic positive cap U and continuous real envelope functions compile; full old recovery exact-type equality compiles. Arithmetic constants are representations, not new algebraic structures. |
| Superfluous arguments | No n>0 or kappa>2 binder exists. hm gives m>0 and strict limit gap; h47 gives quotient slack. Zero-dimension contradiction and no-zero-upper-bound probe forbid naive deletion; n=0 recovery compiled. |

The expanded denominator form is the literature's2m(1+4δ)/(m−4(1+3δ)n√m−2η). The native shape proof validates it, while the project gamma-minus-eta form aligns with downstream eta_lt_gam_iff. There is no proposed new simp-normal-form cycle or unnecessary instance constraint.

## Phases6.0–6: callers, dependencies, composition

Lexical enumeration was cross-checked with git grep over tracked production sources. There is one actual source call, Main420 inside private exists_roth_parameters_aux; the module docstring and declaration line are not callers. Canonical293 loaded-kernel audit finds the same one direct value consumer and no direct type consumer. Five canonical transitive consumers are that helper, roth_of_isIntegral, roth, roth_rat and LeanEval's thueSiegelRoth. These are canonical graph edges from native type/value constants, distinct from lexical use and unrestricted generated-constant closure. Target has no simp attribute and no later source attribute registration was found.

Canonical written proof dependencies, in tracked declaration order: Roth.lam, Roth.gam, Roth.eta, Roth.exists_delta_bound, Roth.eta_lt_gam_iff. The overview contains only these public/canonical names. Generated kernel constants such as lam._proof_1 are preserved in native raw evidence, not promoted into the overview dependency list.

The complete actual private caller was re-elaborated with a local exact-signature helper containing the target's literal proof. This retains all original hypotheses and polynomial/coefficient/dimension conclusions. The replacement experiment separately replays the **entire Main410–588 continuation**, including every required private helper with private visibility removed in the scratch namespace, then roth_of_isIntegral/roth/roth_rat, replacing the actual target call with the recovered generic theorem. It retains original signatures. The LeanEval module was read and its transitive edge audited; **no new LeanEval terminal replay is claimed**.

Composition tests are scoped honestly. The isolated generic selection is several existing calls (three eventual inequalities, two conjunctions, quotient continuity and exists_gt); the complete old-form recovery additionally needs the arithmetic square-root gap, rpow continuity and zero-value normalization. This is not a verified≤3-existing-call replacement. Independent native `solve | simp` and `solve | aesop` do not close the full original goal; the literal proof then closes it. These bounded failures do not prove library absence. Inline success proves feasibility, not redundancy. No separate source-level inline derivation bypassing the theorem was found.

## Phase7: verdict and future upstream questions

BORDERLINE-needs-human, with these concrete future API questions:

1. Should a simultaneous positive-parameter theorem with an explicit cap and two strict continuous envelopes be public API, rather than applications composing the existing eventual-inequality tools?
2. If a reusable quantitative perturbation API is added, should its primary statement expose arbitrary continuous numerator/denominator functions or positive-power arithmetic envelopes?
3. Should this exact gamma/eta parameter choice remain local to a future Roth development, with the generic filter portion kept as a local composition?

Keeping the current project-local theorem is a concrete next action. It is used and not established junk. Its full arithmetic content is too narrow to recommend as-is solely from Roth's theorem being important; its reusable selection pattern already has a rich filter API, but the whole original result is not verified as a tiny existing-call composition. No public mathlib PR/home/reviewer/grouping is proposed under this BORDERLINE verdict; those YES-only artifacts are n/a rather than invented.

## Phase8: native/evidence gates and limitations

Accepted root-executed proofs use only propext, Classical.choice and Quot.sound, with default resource limits, no sorry/new axioms/unsafe/native_decide. Full raw receipts and exact executed sources include failed attempts separately. Original and scope kernel printers each elide95497 characters of the body; **neither is a full kernel-body dump**. Complete written proof, full native type/standard axioms and the ordered293/unique293/present293/value293 kernel audit remain available.

Rejected attempts remain raw: recovery01/callers01 left the zero-dimension contradiction unfinished; composition01 used fail_if_success on a progress-only simp; shape01 elaborated but produced an unnecessary-sequence-focus warning. Subsequent immutable02 sources fix each issue. The initial inline width guard occurred before a native call and is documented separately; no earlier executed source was overwritten.

Evidence: [verification](../evidence/Roth.exists_delta/verification.json), [phase checklist](../evidence/Roth.exists_delta/phase-checks.json), [literature requests/summaries](../evidence/Roth.exists_delta/literature.json), [canonical consumers](../evidence/Roth.exists_delta/canonical-consumers.json), [portable validator](../evidence/Roth.exists_delta/validate.py), [current manifest](../evidence/Roth.exists_delta/copy-manifest.json). Validation supports scratch and integrated layouts, checks current manifest hashes/bytes, exact293 order/private names, normalized written dependencies, fresh17 hashes, native outcomes/axioms/requests and all report links. Root acceptance remains pending independent review.

Final gates: [scratch validation](../evidence/Roth.exists_delta/validation-scratch.json), [integrated validation](../evidence/Roth.exists_delta/validation-integrated.json), [secret scan](../evidence/Roth.exists_delta/secret-scan.json). All passed; assessment completed with unresolved[] and root acceptance pending.
