# Roth.lem7_numeric — completed assessment 219

**BORDERLINE-needs-human.** This numerical step of Roth's index induction has one verified caller and a substantial real square-root/power proof. No exact mathlib replacement or qualifying composition from at most three existing calls was established. A genuinely weaker coefficient cap (`4` replacing `3`, with `δ ≤ 1` unchanged) and a free-parameter square-root envelope compile independently using only mathlib. The outstanding judgment is whether either package has a public library audience, or belongs inside a future Roth-index development. The questions below concern future upstream design, not incomplete verification or a need for user input.

## Phase 0 — baseline and integrity

Fresh hashes of all 17 production source/pin inputs match the successful shared baseline (2467 jobs). Canonical order identifies declaration 219, `Roth/Theta.lean:709–740`; the metadata's exact source range is authoritative. All of `Roth/Theta.lean`, the full actual caller at 840–889 and its downstream induction through `Θ_lt` were read and replayed. The module defines polynomial-index suprema, proves the one-variable and determinant bounds, then uses this helper in the induction step. Production Lean, pins, Git, and overview/progress records remain unchanged by the worker.

[inputs.json](../evidence/Roth.lem7_numeric/inputs.json); [input-manifest.json](../evidence/Roth.lem7_numeric/input-manifest.json); [baseline-build.txt](../evidence/Roth.lem7_numeric/baseline-build.txt); [canonical-entry.json](../evidence/Roth.lem7_numeric/canonical-entry.json); [target-metadata.json](../evidence/Roth.lem7_numeric/target-metadata.json); [source-module.lean.txt](../evidence/Roth.lem7_numeric/source-module.lean.txt).

The original full-module scratch replay renames precisely the target to `Numeric219.replay` and prints standard axioms for every public replay definition/theorem. The exact private-aware canonical array was compared against tracked order before execution, then runtime checked 293 requested, 293 unique, 293 present and 293 kernel values. Its sole direct target consumer is `_private.Roth.Theta.0.Roth.theta_phi_lt_aux`. This direct-constant scan is not a transitive opaque/simp dependency closure.

[canonical-preflight.json](../evidence/Roth.lem7_numeric/canonical-preflight.json); [canonical-snapshot.json](../evidence/Roth.lem7_numeric/canonical-snapshot.json); [canonical-consumers.json](../evidence/Roth.lem7_numeric/canonical-consumers.json); [original-executed.lean.txt](../evidence/Roth.lem7_numeric/original-executed.lean.txt); [original-receipt.json](../evidence/Roth.lem7_numeric/original-receipt.json).

## Phase 1 — exact meaning and proof

For natural `p ≥ 2`, real `0 < δ ≤ 1`, and **any real Φ** satisfying `Φ ≤ 3·10^(p−1)·δ^(2^(-(p−1)))`, prove `2(Φ + √Φ + √δ) < 10^p·δ^(2^(-p))`. There is no nonnegativity premise on Φ. Lean's total `Real.sqrt` is zero on nonpositive inputs; changing to an unsigned representation without a bridge would lose allowed inputs. Equality is permitted in both upper hypotheses, including `δ = 1`.

Complete freshly printed native type:

```lean
∀ {p : ℕ},
  2 ≤ p →
    ∀ {δ : ℝ},
      0 < δ →
        δ ≤ 1 →
          ∀ {Φ : ℝ}, Φ ≤ 3 * 10 ^ (p - 1) * δ ^ (1 / 2) ^ (p - 1) → 2 * (Φ + √Φ + √δ) < 10 ^ p * δ ^ (1 / 2) ^ p
```

There are three data arguments `p : ℕ`, `δ : ℝ`, `Φ : ℝ` and exactly four propositional premises `hp,hδ0,hδ1,hΦ`. No ambient `Fintype`, `DecidableEq`, universe, polynomial or project parameter survives in the elaborated type. Source metadata records no direct project references, and the independent mathlib-only derivation demonstrates a project-free proof.

Set `p=k+1`, `a=δ^(2^(-(k+1)))` and `T=10^k`. Then `0<a≤1`, `a²=δ^(2^(-k))`, `√δ≤a`, and `T≥10`. The cap becomes `Φ≤3Ta²`. Since `3T<T²`, the existing positive-target square-root criterion yields `√Φ<Ta` even if Φ is negative. Also `a²≤a`; combining these inequalities leaves a strict margin below `10Ta`. The source makes the final comparison by `linear_combination`.

[native-type.json](../evidence/Roth.lem7_numeric/native-type.json). The native printer explicitly elides 72222 characters of the **kernel body**, not the type. Complete exact written sources, complete diagnostics, axiom output and kernel-value audit are retained; this is not a claim of a complete kernel pretty-print dump.

## Phase 2 — size and one-line check

**SMALL:** an auxiliary numerical estimate inside a named theorem's induction, not a separately named general theorem in the searched literature. Exhaustive search still runs. The source inventory counts 30 proof lines. One-line-definition test and its three exemptions are **n/a: theorem**, not a definition, abbreviation, structure or instance.

## Phase 3 — exhaustive literature protocol

Every named channel was actually queried. Web artifacts retain exact requests, returned-response SHA256/bytes/status, clean returned locators and original concise summaries only. No full web body is archived. Returned URL query strings are removed; trailing prose punctuation is stripped; visibly truncated locators are omitted without guessing. Primary-source openings supplement the protocol rather than being invented as an additional required channel.

| Channel | Actual query / source | Finding and limit |
|---|---|---|
| General specific | `Roth theorem lemma 7 Phi square root delta 10 numerical inequality` | Quantitative Roth references and Princeton lecture notes; no exact standalone named helper established. |
| General broader | `square root quadratic upper bound absorption real variable negative square root inequality` | General quadratic/root comparisons; classical domain conventions do not directly model totalized negative-input `Real.sqrt`. |
| General aliases | `Thue Siegel Roth index induction iterated square roots constants` | Polynomial-index proof context; distinguish additive Roth and unrelated root problems. |
| Optional ChatGPT mathematics | Standard form, generality and historical evolution | n/a: `ask_chatgpt_math` unavailable. No mathematical response invented. |
| Local references | `clean.tex:960–1036`, especially 1020 onward | Exact substitution `a=δ^(2^-p)` and square-root absorption in proof of Lemma 7; fixed constants serve that induction. |
| nLab | `site:ncatlab.org/nlab Roth polynomial index square root inequality` | Square-root/inequality/index pages; no exact weighted scalar absorption. |
| Distinct nCatLab | `site:ncatlab.org/ncatlab Roth polynomial index square root inequality` | Returned out-of-namespace nLab topics retained honestly; no applicable categorical reformulation. |
| Stacks | `site:stacks.math.columbia.edu Roth index numerical square root estimate` | Index/algebraic geometry search noise, no exact real numerical law. No geometric structure occurs in the target. |
| MathOverflow | `site:mathoverflow.net Roth index lemma induction constants square root` | Dyson-index smallness and quantitative Roth discussions; no exact 3/10 formula established. |
| Recent arXiv | `site:arxiv.org "Roth" "index" "Diophantine" after:2021-10-28 before:2026-10-29` | Empty results, explicitly not a proof of absence. |
| Recent refinement | `site:arxiv.org "Roth theorem" "formalization" after:2021-10-28 before:2026-10-29`; `site:arxiv.org "Roth" "Diophantine approximation" after:2021-10-28 before:2026-10-29` | 2022 characteristic-p dynamics and 2025 L-function/variety context; no exact helper identified. |
| Supplementary primary openings | Princeton notes, pp149–151, Def17.1.1/Lemma17.2.1; Bombieri–van der Poorten 1988 pp233–237 | Polynomial-index/Roth and Dyson formulations, with different constants; no independent canonical packaging of this scalar estimate. OCR limits precise exponent extraction in the latter. |
| Supplementary recent openings | arXiv2209.09182,2507.06609 | Primary abstracts dated19 Sep2022 and9 Jul2025; characteristic-p dynamics and applications of p-adic Roth, respectively. Neither establishes this helper. |

[web-general.json](../evidence/Roth.lem7_numeric/web-general.json); [nlab.json](../evidence/Roth.lem7_numeric/nlab.json); [ncatlab.json](../evidence/Roth.lem7_numeric/ncatlab.json); [stacks.json](../evidence/Roth.lem7_numeric/stacks.json); [mathoverflow.json](../evidence/Roth.lem7_numeric/mathoverflow.json); [arxiv.json](../evidence/Roth.lem7_numeric/arxiv.json); [arxiv-refined.json](../evidence/Roth.lem7_numeric/arxiv-refined.json); [primary.json](../evidence/Roth.lem7_numeric/primary.json); [primary-locators.json](../evidence/Roth.lem7_numeric/primary-locators.json); [recent-primary.json](../evidence/Roth.lem7_numeric/recent-primary.json); [literature-source.json](../evidence/Roth.lem7_numeric/literature-source.json); [clean-excerpt.tex.txt](../evidence/Roth.lem7_numeric/clean-excerpt.tex.txt).

Concept identified: **numerical square-root absorption in Roth's polynomial-index induction**. Local source gives the exact formula; other primary references supply surrounding index methods with different arrangements. Sources do not establish a single separately named standard 3/10 inequality. The natural broader analytic form separates a positive scale, a quadratic cap, a root cap and a coefficient budget; the precise envelope below is independently proved organization, not a theorem attributed to a web source. Historical alternatives via Dyson's lemma concern the surrounding proof, not a verified replacement for this numeric statement.

## Phase 4a–b — every parameter and generality

| Argument | Role | Verified weakening / necessity boundary |
|---|---|---|
| `p : ℕ` | Dimension, dyadic exponent, natural power and truncated subtraction | `p=k+2` reindexing compiles. Abstract envelope replaces linked constants by scalar bounds, without interpreting arbitrary real numbers as polynomial dimensions. |
| `hp : 2≤p` | Supplies `T≥10`, ensures successor decomposition | Dropping the lower bound is false at `p=1,δ=1,Φ=3`; both δ premises and Φ cap hold. `dimensionOne` certifies the cap and failed conclusion. No optimal lower-dimension classification claimed. |
| `δ : ℝ` | Real power and square root | Fixed real APIs; no mechanical ordered-field weakening established. NNReal loses negative Φ if applied to all variables and needs a representation bridge even for δ. |
| `hδ0 : 0<δ` | Positive scale and strict gap | Replacing by `0≤δ` fails at `δ=0,Φ=0` for any `p≥2`; original upper hypotheses then hold. `zeroDelta` certifies the failed conclusion for all p. |
| `hδ1 : δ≤1` | Bounds `a≤1` and `√δ≤a` | Cannot remove all δ upper control: at `p=2,δ=100,Φ=300`, Φ cap holds and conclusion fails, certified together by `largeDelta`. No specific larger δ range or maximal endpoint is claimed. |
| `Φ : ℝ` | Summand and square-root input | Already arbitrary real, including negative values. `negativePhi` verifies the entire nonpositive subcase under the existing p/δ hypotheses. No extra Φ positivity is introduced. |
| `hΦ` | Quadratic cap on Φ | **Successfully weakened** coefficient `3` to `4`, retaining `δ≤1` and arbitrary real Φ; entire module and original caller statements replay clean. Dropping all cap control fails at `p=2,δ=1,Φ=1000`, checked by `noPhiCap`. |
| Instances / universes | None | No ambient class or universe parameter to discard. |

Generality status: **STRICTLY NARROWER in the proved coefficient-cap dimension**. This is a verified mathematical widening, not a claim that a literature-standard public API uses 4. The exact proposed reachable statement replaces only `(hΦ : Φ ≤ 3 * …)` by `(hΦ : Φ ≤ 4 * …)`, leaving the conclusion and other hypotheses identical. All downstream original statements remain unchanged with a wrapper from cap3 to cap4. No conclusion about `δ≤2` follows from the adjacent helper's separate assessment; in particular no simultaneous cap4/range2 weakening is asserted.

[broader-executed.lean.txt](../evidence/Roth.lem7_numeric/broader-executed.lean.txt); [broader-receipt.json](../evidence/Roth.lem7_numeric/broader-receipt.json); [isolated-executed.lean.txt](../evidence/Roth.lem7_numeric/isolated-executed.lean.txt); [isolated-receipt.json](../evidence/Roth.lem7_numeric/isolated-receipt.json).

The independently compiled scalar envelope is:

```lean
theorem envelope {a c b d L x s : ℝ} (ha : 0 < a) (ha1 : a ≤ 1) (hc : 0 ≤ c)
    (hb : 0 < b) (hcb : c < b ^ 2) (hx : x ≤ c * a ^ 2) (hs : s ≤ d * a)
    (hbudget : 2 * (c + b + d) ≤ L) : 2 * (x + √x + s) < L * a
```

It allows free real `x,s` without nonnegativity, and free coefficients subject to actual sufficient inequalities. Its proof derives `a²≤a`, `x≤ca`, `√x<ba` via `Real.sqrt_lt'`, then uses the budget after multiplication by a. For cap4 choose `c=4T,b=3T/4,d=1,L=10T`; `T≥10` gives `c<b²` and the required budget. This preserves real square-root semantics and is a genuine abstraction of the original comparison. It is **new scratch proof**, not an existing mathlib building block. The fixed-dimension rpow normalization remains additional proof, not a one-call definitional specialization.

## Phase 4c — nine modern-idiom checks

| # | Question | Finding / concrete consequence |
|---|---|---|
| 1 | Typeclass preambles | No: scalar bounds are ordinary hypotheses, not new structures appropriate for instances. |
| 2 | Filters rather than sequences | No sequence or convergence predicate. |
| 3 | Universal properties | No mathematical object is constructed. |
| 4 | Bundled substructures | No closure predicate or subobject; bundling δ in an interval adds projections without simplifying the caller. |
| 5 | Hierarchy weakening | No verified arbitrary ordered-field replacement for concrete `Real.sqrt/rpow`. The scalar inequality alone may admit other root interfaces, but none is claimed to compile here. |
| 6 | Higher categories | No categorical content. |
| 7 | Concrete indices | Yes for numerical organization: free scalar a,c,b,d,L decouple base10 and natural dimension. Existing `Real.sqrt_lt'` and generic ordered multiplication compose with any supplied quadratic cap and budget. |
| 8 | Concrete-via-abstract diagnostic | Literal named-object test is n/a: neither Θ nor lem6Φ occurs in the target's type/body. After setting a,T, the proof only uses a>0,a²≤a,√δ≤a,T≥10 and the quadratic Φ cap. The compiled envelope isolates those properties. This is a constants-abstraction diagnostic, not a vanished named-object proof. |
| 9 | False-generalization guard | Same real order, multiplication, square root and rpow on original inputs. Replacing Φ by an unsigned scalar would exclude allowed cases; interpreting arbitrary coefficients as dimensions would change meaning. Both are rejected. Coefficient4 is proved withδ≤1 only. |

Modern idiom available: **yes, a free-parameter numerical envelope**, of moderate proof-refactoring cost, enabling general quadratic/root-cap comparisons with arbitrary positive scales and coefficient budgets through the existing root/order APIs. Its concrete benefit is eliminating repeated root/linear absorption arguments; a separate mathlib consumer beyond this specialization has not been demonstrated. Public audience therefore remains the upstream design question; abstraction alone does not settle inclusion.

## Phase 4.5 — infrastructure risk

**n/a: theorem.** Each of the six rows (typeclass diamonds, reducibility leaks, noncanonical unfolding, instance-priority collisions, universe constraints, coercion ambiguity) is n/a: the target introduces no definition, class, instance or coercion. No definitional replacement is proposed. The scratch scalar envelope is a theorem too.

## Phase 4.6 — five proof-strategy checks

| # | Question | Finding |
|---|---|---|
| 1 | Topology via ε–δ versus filters | n/a: no topology. |
| 2 | Element algebra versus ideals/submodules | n/a: inequalities of real scalars, no substructure argument. |
| 3 | Sequences versus nets/filters | n/a: no limiting argument. |
| 4 | Construction versus universal property | n/a: no object construction. |
| 5 | Missing helpers mathlib should have | Possible weighted quadratic/root absorption envelope; its proof and specialization compile, but an independent public API audience is undecided. Root comparison and rpow normalization themselves already exist. |

Strategy verdict: **MATHLIB-IDIOMATIC for the local estimate**, with an optional generic-envelope refactor if adopted. Normalize dyadic powers, compare a square root to a positive scalar via its square, and finish ordered arithmetic. No arbitrary category/filter reformulation helps. A potential helper is a separate API design question, not an excuse to omit search or a cost-based downgrade.

## Phase 5 — all fifteen actual search cells

All five methods were invoked on the current form, literature-standard square-root/index form and abstract budget form. External indices can differ from the pin. Local name search returned `index:warming`; positive source hits were confirmed natively, while missing hits do not establish absence.

| Form | Method | Exact query / selected result | Evidence |
|---|---|---|---|
| current | leanfinder | `If p ≥ 2, 0 < δ ≤ 1 and Φ ≤ 3 * 10^(p-1) * δ^((1/2)^(p-1)), then 2*(Φ+sqrt Φ+sqrt δ) < 10^p * δ^((1/2)^p)`; SzemerediRegularity.hundred_lt_pow_initialBound_mul, LiouvilleNumber.aux_calc, Behrend.bound | [raw receipt](../evidence/Roth.lem7_numeric/search-current-leanfinder.json) |
| current | loogle | `Real.sqrt, Real.rpow, _ < _`; no hit | [raw receipt](../evidence/Roth.lem7_numeric/search-current-loogle.json) |
| current | leansearch | `upper estimate sum x plus square root x plus square root delta bounded by iterated half power delta`; Finset.le_sum_schlomilch, Nat.sqrt_le_add, Real.sqrtTwoAddSeries_lt_two | [raw receipt](../evidence/Roth.lem7_numeric/search-current-leansearch.json) |
| current | rg | `lem7_numeric\|Phi.*sqrt\|Φ.*√`; no lexical hit | [raw receipt](../evidence/Roth.lem7_numeric/search-current-rg.json) |
| current | local_search | `lem7_numeric`; Roth.lem7_numeric | [raw receipt](../evidence/Roth.lem7_numeric/search-current-local_search.json) |
| standard | leanfinder | `Roth lemma 7 numerical induction square root bound exponential constant 10 power delta iterated square roots`; Behrend.roth_lower_bound, Behrend.roth_lower_bound_explicit, rothNumberNat_le | [raw receipt](../evidence/Roth.lem7_numeric/search-standard-leanfinder.json) |
| standard | loogle | `Real.sqrt, _ ≤ _ → _ < _`; Real.sqrt_lt_sqrt, Real.cos_lt_one_div_sqrt_sq_add_one, Behrend.roth_lower_bound_explicit | [raw receipt](../evidence/Roth.lem7_numeric/search-standard-loogle.json) |
| standard | leansearch | `square root upper bound from quadratic upper bound including negative real argument`; Real.neg_sqrt_lt_of_sq_lt, Real.sqrt_one_add_le, Real.le_sqrt_of_sq_le | [raw receipt](../evidence/Roth.lem7_numeric/search-standard-leansearch.json) |
| standard | rg | `theorem sqrt_lt\|theorem sqrt_le\|sqrt_add_le\|sqrt_one_add_le`; source hits | [raw receipt](../evidence/Roth.lem7_numeric/search-standard-rg.json) |
| standard | local_search | `Real.sqrt_lt`; Real.sqrt_lt, Real.sqrt_lt', Real.sqrt_lt_sqrt | [raw receipt](../evidence/Roth.lem7_numeric/search-standard-local_search.json) |
| abstract | leanfinder | `If a is positive at most one T at least ten and x at most 4 T a squared, then 2 (x + sqrt x + d) < 10 T a when d at most a`; Real.sqrtTwoAddSeries_step_down, Real.sqrtTwoAddSeries_step_up, two_mul_le_add_of_sq_eq_mul | [raw receipt](../evidence/Roth.lem7_numeric/search-abstract-leanfinder.json) |
| abstract | loogle | `Real.sqrt_lt'`; Real.sqrt_lt' | [raw receipt](../evidence/Roth.lem7_numeric/search-abstract-loogle.json) |
| abstract | leansearch | `bound square root of x by a positive number using strict upper bound x less than square`; Real.sqrt_lt', Real.lt_sqrt_of_sq_lt, Real.sqrt_pos_of_pos | [raw receipt](../evidence/Roth.lem7_numeric/search-abstract-leansearch.json) |
| abstract | rg | `sqrt_lt'\|rpow_mul_natCast\|rpow_le_one\|rpow_le_rpow_of_exponent_ge`; source hits | [raw receipt](../evidence/Roth.lem7_numeric/search-abstract-rg.json) |
| abstract | local_search | `Real.sqrt_lt'`; Real.sqrt_lt', Real.sqrt_le_sqrt_iff' | [raw receipt](../evidence/Roth.lem7_numeric/search-abstract-local_search.json) |

Pinned positive native signatures include `Real.sqrt_lt'`, `Real.sqrt_le_iff`, `Real.sqrt_eq_rpow`, `Real.rpow_le_one`, `Real.rpow_le_rpow_of_exponent_ge`, `Real.rpow_mul_natCast`, and `le_self_pow₀`. The isolated batch actually uses the necessary root, exponent and multiplication comparisons; its `#check_failure Roth.lem7_numeric` confirms the target is unavailable without project imports. The exact active 18-import mathlib-only prefix is unchanged, with no added import. Candidate source hashes are retained.

[mathlib-inputs.json](../evidence/Roth.lem7_numeric/mathlib-inputs.json); [pinned-candidate-locators.json](../evidence/Roth.lem7_numeric/pinned-candidate-locators.json); [isolated-prefix.lean.txt](../evidence/Roth.lem7_numeric/isolated-prefix.lean.txt); [isolated-receipt.json](../evidence/Roth.lem7_numeric/isolated-receipt.json).

Candidate triage: `Real.sqrt_lt'` is an exact arbitrary-real **ingredient**, not the combined numerical absorption; it still needs proof of its squared premise. `Real.sqrt_le_iff`, `Real.sq_sqrt'` and `Real.sqrt_one_add_le` offer related comparisons, but supplying a nonnegative target/quadratic upper bound and budget is substantive reasoning. `sqrtTwoAddSeries` concerns a different iterated expression. `Behrend` and `rothNumberNat` results concern additive arithmetic progressions rather than Diophantine polynomial indices. None is an identified replacement for the complete theorem. Search conclusion: **ingredients found; no exact replacement established**, not a proof of global absence.

## Phase 5.5 — normal form, syntax and argument audit

Normal form: `Real.sqrt` and `Real.rpow` express precisely the current real statement; `Real.sqrt_eq_rpow` supplies the existing equivalence, so a new pairwise equivalence API is unnecessary. The actual raw-form simplification probe tried replacing roots by rpow and did not close the inequality. The abstract scalar envelope separates the normalization from arithmetic. No orthogonal equivalence lemma violating RHS normal-form orientation is proposed.

Syntactic alternatives actually compiled: `successor` uses `p=k+2`, eliminating truncated subtraction/hp; `divided` states `Φ+√Φ+√δ < target/2`, matching the sole caller's immediate goal. The original form remains convenient at that caller with one `lt_div_iff₀'` transport, which already occurs in source. Both alternatives are shape changes, not existing-mathlib replacement proofs. `negativePhi` checks the allowed nonpositive branch, and `equalityUpper` checks both upper premises at equality simultaneously.

[shape-executed.lean.txt](../evidence/Roth.lem7_numeric/shape-executed.lean.txt); [shape-receipt.json](../evidence/Roth.lem7_numeric/shape-receipt.json).

Every argument is audited above: p,δ,Φ occur in the type;hp supplies scale bounds;hδ0 supplies strictness;hδ1 controls the scale;hΦ supplies the cap and admits the verified coefficient weakening. No unused ambient instance survives elaboration. Boundary counterexamples qualify necessity claims exactly: no claim thatδ≤1 or coefficient3 is optimal. Statement-shape verdict: **OK locally; consider generic-envelope/cap4 scope before upstream shipment**.

## Phase 6.0 — complete callers and inline audit

Fresh `rg --no-ignore` over the production inventory `Roth/` and `Roth.lean` agrees with tracked `git grep`: exactly declaration709 and call879, both in `Roth/Theta.lean`. No target reference in another production statement/file. Internal use1, external-to-file0. The complete canonical source inventory independently records the same sole caller. Inline-pattern enumeration reveals related square-root arithmetic in `index_numeric_bound_aux`, but that theorem derives an index bound from a minimum estimate; it is not a rederivation of this Φ-to-next-dyadic bound. No complete bypass derivation was identified.

| Actual caller | Full body | Use and verified refactor option |
|---|---|---|
| `Roth.theta_phi_lt_aux` | `Roth/Theta.lean:840–889` | Converts the divided goal with `lt_div_iff₀'`, applies `lem7_numeric hp hδ0 hδ1.le`, then proves the Φ cap from one-variable/prefix estimates and `lem7_Φ_bound`. Entire caller accepts the proof as local `have numeric`; downstream statements throughΘ_lt compile unchanged. |

[source-search.json](../evidence/Roth.lem7_numeric/source-search.json); [tracked-source-search.json](../evidence/Roth.lem7_numeric/tracked-source-search.json); [inline-audit.json](../evidence/Roth.lem7_numeric/inline-audit.json); [callers.json](../evidence/Roth.lem7_numeric/callers.json); [inline-executed.lean.txt](../evidence/Roth.lem7_numeric/inline-executed.lean.txt); [inline-receipt.json](../evidence/Roth.lem7_numeric/inline-receipt.json). The sole direct canonical kernel-value consumer agrees, but lexical use and direct kernel use remain separately measured quantities. Used once does not imply dead code, and no transitive downstream closure is inferred from this count.

## Phase 6 — actual composition experiments

The independent original-form theorem executes `fail_if_success exact?` and a second `solve | simp only [Real.sqrt_eq_rpow]` probe. Both negative tests pass cleanly. These are concrete unsuccessful candidate routes, not exhaustive proofs that no term exists. The full successful original derivation still requires dyadic normalization, positivity, square comparisons and ordered arithmetic.

The positive free-parameter envelope uses existing `Real.sqrt_lt'` and multiplication/order comparisons **with newly proved premises**, then a linear combination. The cap4 theorem additionally proves a² identity,scale bounds,rootδ comparison and coefficient budget. Its source wrapper recovers cap3 and all original downstream statements. These are new proofs, not at most three existing mathlib calls. The complete actual-caller inline experiment demonstrates a valid local destination for the argument, without converting it into an existing-call composition.

Composition verdict: **NOT-COMPOSABLE under the verified ≤3-existing-call criterion**. No closing `simp [defs]` composition was found. Parent re-aim gate: n/a, no project definition appears in the independent numerical target. The adjacent project's cap lemma is not counted as a mathlib building block.

## Phase 7 — actionable verdict and future scope

**BORDERLINE-needs-human.** Mathematical validity, successful broadening, all mandatory searches and actual caller adaptation are established. Neither NO bucket is supported: no exact existing theorem or qualifying short composition was verified. A positive verdict also needs a public API audience for the numerical packaging, beyond its usefulness to this one induction. The distinct scalar envelope is a plausible general analytic API, but the searched sources standardize the surrounding index machinery, not this coefficient budget. This audience/design decision, rather than proof cost or uncertainty about verification, motivates BORDERLINE.

Concrete future upstream questions, not user blockers:

1. Should the free-parameter quadratic/root absorption envelope be public API in `Mathlib/Analysis/Real/Sqrt.lean`, with the dyadic normalization kept inside a future Roth-index module?
2. If a named numerical helper belongs in an upstream Roth development, should its Φ cap use the independently verified coefficient4 or the source-aligned coefficient3?
3. Should the single caller use a private numerical lemma or the verified local `have numeric` proof, given both preserve downstream statements?

Alternative destination now: **`Roth/Theta.lean`**, alongside the induction. If localizing, use the exact archived inline proof in the whole caller at840–889 and replace the single call at879; there are no other explicit source callers to refactor. If generalizing, use the verified envelope and cap4 wrapper, keepδ≤1 and negativeΦ semantics, and rerun `/generalise Roth.lem7_numeric` then `/cleanup Roth/Theta.lean Roth.lem7_numeric` before any future PR. Proposed PR title, accepted-YES grouping and recent-commit reviewer selection are **n/a for this BORDERLINE verdict**; no PR is authorized or produced by this read-only assessment. No general rule against numerical lemmas is inferred from this result or from declaration218.

## Phase 8 — exact verification and freeze

Five accepted batches: complete original replay/canonical audit, mathlib-only envelope/cap4/current proof and guards, cap4 whole-module wrapper, full actual-caller local inline/downstream replay, and shape/negativeΦ/equality/cap guard batch. All final runs are successful, warning/error-free, standard axioms only. Disk responses have `partial:false`; raw run-code uses complete `diagnostics/success` and `timed_out:false`, with no partial field by design. Full-file diagnostic and axiom checks are enforced; required target-specific information is scoped to the new namespace region.

Two rejected native attempts remain separate: initial arithmetic/API failures (recoveredsorryAx excluded), and an orphaned-docstring emptyLine warning in the first inline source. A clean initial contextual replay with an unintended adjacent-helper rename is retained as supplementary only; the corrected target-renamed audit is the accepted original source. No stale/error-text native execution followed a failed preparation. Every accepted source preparation exited0, was read, and retained the exact required import prefix before native execution. No new axiom,sorry,unsafe,native_decide,resource-limit increase or repeated exhausting broad automation was used.

[verification.json](../evidence/Roth.lem7_numeric/verification.json); [preparation-notes.json](../evidence/Roth.lem7_numeric/preparation-notes.json); [assessment.json](../evidence/Roth.lem7_numeric/assessment.json); [phase-ledger.json](../evidence/Roth.lem7_numeric/phase-ledger.json); [overview-entry.json](../evidence/Roth.lem7_numeric/overview-entry.json); [portable current-manifest validator](../evidence/Roth.lem7_numeric/validate.py). All verification unresolved lists are empty. Root owns independent review, acceptance, integration, commit and push. The portable validator always checks the current copy manifest, with integration-only root records explicitly exempt from worker coverage.
