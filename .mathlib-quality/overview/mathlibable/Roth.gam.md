# Roth.gam — canonical230

**BORDERLINE-needs-human.** The assessment is complete. The remaining questions concern the future upstream API boundary: expose the exact numerical choice publicly, or use an arbitrary admissible real cutoff and keep this formula local. They are not missing verification and do not block this read-only overview. This is an independent assessment of gamma, with no inherited verdict from lambda.

## Phase 0 — Baseline and identity

Public noncomputable definition at `Roth/MainLemma.lean:63`; one source line. The module constructs Roth's auxiliary polynomial and main lemma from box counting and Hasse derivative vanishing. No sorry, unsafe proof, new axiom, or resource-limit raise in accepted evidence. All17 production/pin hashes freshly match the shared manifest; the reusable baseline completed2467 jobs. Endpoint228's full build is already root accepted;230 is not a file endpoint, next266. No production/pin/Git/overview/progress edit made by this worker.

[inputs.json](../evidence/Roth.gam/inputs.json); [baseline-build.txt](../evidence/Roth.gam/baseline-build.txt); [canonical-entry.json](../evidence/Roth.gam/canonical-entry.json).

## Phase 1 — Mathematical content and exact kernel data

For real δ and natural degree n and dimension m, define λ = 4(1+3δ)n√m and γ = (m−λ)/2. Gamma is the high-index cutoff used before subtracting the low-index loss η in the main lemma. The definition is total and assumes no positivity: admissible-parameter theorems establish the needed gap separately.

```lean
noncomputable def Roth.gam (δ : ℝ) (n m : ℕ) : ℝ :=
  ((m : ℝ) - Roth.lam δ n m) / 2
-- native full type: ℝ → ℕ → ℕ → ℝ
-- binder form from full native print: (δ : Real) → (n m : Nat) → Real
```

δ is the real small-parameter input; n is the polynomial degree; m is the variable count. There are no instance or propositional hypotheses, and the result is a real number. The only project body dependency is `Roth.lam`; no project type dependency. The full `pp.all` native print was inspected: it explicitly contains subtraction/division/Nat.cast/Roth.lam and has **no printer-elision marker**. The tagged type comes directly from `Lean.getConstInfo` with `pp.funBinderTypes`; it was not split from a printed internal let/body. Universe parameters are empty. Native axioms are exactly propext, Classical.choice, Quot.sound.

[native-type.json](../evidence/Roth.gam/native-type.json); [original-executed.lean.txt](../evidence/Roth.gam/original-executed.lean.txt); [original-receipt.json](../evidence/Roth.gam/original-receipt.json). The original source was replayed as a complete MainLemma module in a new namespace, with only the target renamed outside the canonical audit array. A cold-loading partial receipt is retained separately and is not accepted verification.

## Phase 2 — Size and one-line definition gate

**SMALL**: a numerical parameter choice, not a new mathematical structure or the main theorem. One substantive body line: **ONE-LINER WITH-EXEMPTION**.

| Exemption | Applies? | Concrete evidence |
|---|---|---|
| Avoid defeq abuse | No demonstrated need | rfl unfolding and all eight original signature checks work after replacing the name; no sealed opacity barrier is needed. |
| Avoid typeclass diamonds | No | A real-valued function adds no instances; native Sub/Div/NatCast inference uses standard Real instances. |
| Semantic intent/API stability | Yes locally | The main lemma names the index cutoff and exists_delta names the denominator gap. Eight caller declarations include public statement users across two files. |

Local semantic value does not by itself settle whether mathlib should expose the exact constant choice.

## Phase 3 — Exhaustive literature protocol

The exact local authority is clean.tex §6 eqs34–35,38 and Lemma9; γ is the half-difference parameter associated with this proof. The primary contemporary exposition Goel–Lunia–Ray, *Diophantine approximation and the subspace theorem*, arXiv2502.00731v2, §3.3 Lemmas3.5–3.6, instead uses m(1−ε)/2 and an exponential monomial-count bound. This is evidence of useful alternative parameterizations, not evidence that changing coefficients in the present formula preserves the current proof.

| Channel | Exact request/query | Result and scope | Receipt |
|---|---|---|---|
| web-general | `Roth theorem auxiliary polynomial "gamma" "lambda" index m` | Three distinct general queries sought the exact gamma, a general polynomial-index cutoff, and the formalization name. Returned author-hosted Roth notes and Princeton lecture notes; secondary book mirror reports the exact half difference but is not used as the mathematical authority. Local clean.tex eq35 supplies the exact formula. | [web-general.json](../evidence/Roth.gam/web-general.json) |
| web-general | `Roth lemma polynomial index cutoff (m lambda) / 2 parameter` | Three distinct general queries sought the exact gamma, a general polynomial-index cutoff, and the formalization name. Returned author-hosted Roth notes and Princeton lecture notes; secondary book mirror reports the exact half difference but is not used as the mathematical authority. Local clean.tex eq35 supplies the exact formula. | [web-general.json](../evidence/Roth.gam/web-general.json) |
| web-general | `"Formalizing Roth" "gamma" main lemma` | Three distinct general queries sought the exact gamma, a general polynomial-index cutoff, and the formalization name. Returned author-hosted Roth notes and Princeton lecture notes; secondary book mirror reports the exact half difference but is not used as the mathematical authority. Local clean.tex eq35 supplies the exact formula. | [web-general.json](../evidence/Roth.gam/web-general.json) |
| nlab | `site:ncatlab.org/nlab Roth theorem Diophantine approximation auxiliary polynomial index` | Search returned operator index theory, polynomials, and Vojta background. Operator index differs from weighted polynomial index. No exact gamma parameter hit; this does not prove absence. | [nlab.json](../evidence/Roth.gam/nlab.json) |
| ncatlab | `site:ncatlab.org/ncatlab Roth theorem polynomial index cutoff` | The actual query explicitly targeted /ncatlab. All returned titles were /nlab or /nlab/files, outside the requested namespace. No distinct categorical reformulation of the scalar cutoff was supplied. | [ncatlab.json](../evidence/Roth.gam/ncatlab.json) |
| stacks | `site:stacks.math.columbia.edu Roth theorem auxiliary polynomial index` | Returned commutative algebra, relatively prime polynomials, and multiplicities. Those are different constructions; no auxiliary-index gamma parameter found. | [stacks.json](../evidence/Roth.gam/stacks.json) |
| mathoverflow | `site:mathoverflow.net Roth theorem proof auxiliary polynomial index parameters` | Returned discussions of Roth quantitative bounds and Dyson index arguments; they concern auxiliary polynomials and alternative proofs, not a canonical independent gamma definition. | [mathoverflow.json](../evidence/Roth.gam/mathoverflow.json) |
| arxiv | `site:arxiv.org Roth theorem auxiliary polynomial index after:2021-10-28 before:2026-10-29` | The required five-year date query returned mostly additive-combinatorial Roth and unrelated polynomial papers. Titles are inspected as false positives; no exact scalar definition established. | [arxiv.json](../evidence/Roth.gam/arxiv.json) |
| arxiv-targeted | `site:arxiv.org "Roth" "Diophantine approximation" "index" after:2021-10-28 before:2026-10-29` | A more targeted quoted Diophantine approximation query was attempted after the broad arXiv results. The engine returned no usable source text. Primary paper was then opened directly; this failed/empty search is not absence evidence. | [arxiv-targeted.json](../evidence/Roth.gam/arxiv-targeted.json) |
| primary | Open primary paper abstract/HTML and author-hosted Princeton PDF | Fresh primary access to Goel–Lunia–Ray arXiv2502.00731 (2025, revised2026) and its text, plus Princeton lecture notes. The paper's Section3.3 uses a relative index-loss parameter rather than the exact project gamma. | [primary.json](../evidence/Roth.gam/primary.json) |
| primary-locators | Find Lemma3.5, §3.3, gamma, irrelevant in the actually opened sources | Primary paper Section3.3, Lemmas3.5–3.6, lines728–812: cutoff m(1-epsilon)/2 with exponential monomial-count bound exp(-epsilon²m/16). This supports alternate admissible cutoffs, not arbitrary alteration of the constants in the existing main lemma. Princeton PDF find gamma/irrelevant found no matching extracted text. | [primary-locators.json](../evidence/Roth.gam/primary-locators.json) |
| web-api | `mathlib4 Roth Diophantine approximation gamma index cutoff parameter` | Specific mathlib4 web search returned official DiophantineApproximation.Basic and Siegel lemma documentation, plus unrelated Gamma-function material. The pinned source files, rather than current web documentation, determine exact available API. No exact gamma parameter was identified. Author-site gamma/lambda query did not establish an additional exact formula. | [web-api.json](../evidence/Roth.gam/web-api.json) |
| web-api | `site:web.williams.edu "gamma" "lambda" Roth Miller Takloo Bighash` | Specific mathlib4 web search returned official DiophantineApproximation.Basic and Siegel lemma documentation, plus unrelated Gamma-function material. The pinned source files, rather than current web documentation, determine exact available API. No exact gamma parameter was identified. Author-site gamma/lambda query did not establish an additional exact formula. | [web-api.json](../evidence/Roth.gam/web-api.json) |
| Local reference | `gamma`, `roth:eq35` in clean.tex | Exact half-difference choice and η<γ gap; hash and excerpt retained. | [local-literature.json](../evidence/Roth.gam/local-literature.json); [local-excerpt.tex.txt](../evidence/Roth.gam/local-excerpt.tex.txt) |
| ChatGPT math second opinion | n/a | ask_chatgpt_math unavailable in this session; optional skip only. All other named channels executed. | Tool inventory limitation |

All actual general queries were distinct; explicit nLab and nCatLab namespace queries are separate. nCatLab returned only out-of-namespace nLab material. Recent arXiv was restricted to after2021-10-28 before2026-10-29; the broad query was mostly false positives, the targeted retry returned no usable sources, and the actual 2025/2026 paper was opened directly. nLab operator index and Stacks multiplicity are different notions. Search failures or empty results are not absence evidence. No canonical independent universal gamma concept was established beyond a chosen high-index threshold. The standard exact formula here matches the local paper; the more general useful mathematical interface is an admissible cutoff, not a generic symbol called gamma.

Receipts retain exact requests, returned-response UTF8 SHA256/bytes/status, clean titles/URLs/locators and original concise summaries only. No full article or search-result bodies archived. Malformed/truncated URLs are omitted without guessing; no signed URL retained. Primary online mathematical claims are grounded in the actual arXiv text, while exact constants are grounded in the local source.

## Phase 4a — Parameters, hypotheses and literature generality

| Input | Current | Mathematical role/possible widening | Verified outcome |
|---|---|---|---|
| δ | ℝ, unrestricted | Real small parameter; no positivity assumption to weaken. | formula accepts arbitrary δ; deltaMatters witnesses genuine dependence. |
| n | ℕ | Degree; can feed its real cast to a real-valued arithmetic formula. | Real-parameter formula and rfl cast bridge compile; degreeMatters rules out dropping it. |
| m | ℕ | Dimension; an arithmetic expression can accept real m. | Real-parameter formula/bridge compile; dimensionMatters rules out dropping it. Counting and Fin m still use natural dimension. |
| Output field | ℝ | sqrt and ordered analytic estimates make ℝ meaningful. | Field expression with arbitrary s compiles, but no longer specifies the same real square root. |
| Exact numerical loss | Roth.lam δ n m | Can instead carry an independent real loss l or a supplied admissible cutoff. | halfGap and gapComparison compile; generic cutoff monotonicity compiles. These are newly written probes, not existing mathlib definitions. |
| Positivity/nonzero | None | Positivity of γ is conditional, not intrinsic. | signGuard proves formula 0 1 1<0; positiveGap proves the sufficient admissibility condition. |

[isolated-executed.lean.txt](../evidence/Roth.gam/isolated-executed.lean.txt); [isolated-receipt.json](../evidence/Roth.gam/isolated-receipt.json); [project-executed.lean.txt](../evidence/Roth.gam/project-executed.lean.txt); [project-receipt.json](../evidence/Roth.gam/project-receipt.json). The isolated exact18 prefix contains no Roth import, and both Roth.gam/Roth.lam are checked absent. No project-only operation is silently counted as mathlib.

## Phase 4b — Generality verdict

**MAXIMALLY GENERAL for the current degree/dimension semantics**, with no hypothesis to drop. The arithmetic representation admits real n,m and a polymorphic Field expression, and those widenings were actually compiled. They do not establish that the surrounding auxiliary-polynomial/counting theory works for real degrees or dimensions. No STRICTLY NARROWER THAN STANDARD claim is made for the intended numerical parameter.

```lean
noncomputable def formula (δ n m : ℝ) : ℝ :=
  (m - 4 * (1 + 3 * δ) * n * √m) / 2
def halfGap {K : Type*} [Field K] (x l : K) : K := (x - l) / 2
```

The first preserves the old formula under natural casts; the second represents the half-difference arithmetic but does not package the original choice of λ. Merely introducing either helper in scratch is not an existing-mathlib replacement. A variable admissible-cutoff main-lemma API would have real downstream value by decoupling the polynomial construction from the proof's chosen loss; this is a future API-design question, not an unverified weakening. Cost is not a verdict factor.

## Phase 4c — Nine modern-idiom checks

| # | Question | Assessment/reformulation | Concrete consequence |
|---|---|---|---|
| 1 | Typeclasses for preambles? | No structural hypotheses; retain explicit numeric inputs. | Avoid a meaningless instance for a scalar choice. |
| 2 | Filters/nets replacing sequences? | No sequence in this definition. Existing Continuous/ContinuousAt handles δ. | continuousDelta compiled with fun_prop; exists_delta can reuse it locally. |
| 3 | Universal-property class? | No canonical object selected by a universal property. | half-difference arithmetic does not need a new class. |
| 4 | Bundled substructure? | γ is a scalar, not a closed subset. | Bundling would not unlock a lattice/quotient API. |
| 5 | Weaker scalar hierarchy? | Field arithmetic with arbitrary s compiles as algebraic. | An expression evaluator is more general syntactically; actual Real.sqrt/counting semantics remains specific. |
| 6 | Higher category? | No categorical structure. Distinct nCatLab query supplied no relevant categorical content. | None justified. |
| 7 | Concrete ℕ indices? | Real n,m expression verified with rfl bridge. | Allows continuous algebraic manipulations, but cannot replace Fin m or polynomial natDegree with reals. |
| 8 | Concrete-via-abstract diagnostic? | Yes at the arithmetic boundary: body contains lam once; after unfolding it is only arithmetic/sqrt. halfGap abstracts an arbitrary loss; arbitraryCutoff transports a pointwise predicate below a smaller cutoff. | MainLemma's existing project helper le_index_of_forall_eval_eq_zero already takes arbitrary c. Future index-bound theorem can consume a supplied admissible γ; continuity still comes from ordinary scalar API. This is an API proposal, not proof of a new universal gamma concept. |
| 9 | False-generalization guard? | Reject identifying arbitrary Field/s with this real gamma, and reject unconditional positivity; signGuard proves failure even at δ=0. | Preserve counts n,m and the chosen real loss when specializing; use explicit bridge if arithmetic representation widens. |

Modern idiom available at the reusable theorem boundary, not a missing structure for this one-line def. The verified generic probes explain that boundary; they do not automatically justify a YES-but-generalise-first label.

## Phase 4.5 — Six infrastructure risks

| Risk | Verdict | Checked evidence |
|---|---|---|
| Typeclass diamond | None | No new class/instance. Native #synth Sub ℝ, Div ℝ, NatCast ℝ return the standard Real instances. |
| Reducibility leak | Low | Plain noncomputable def is semireducible; rfl unfolding succeeds without adding reducible. Body only scalar operations and lam. |
| Noncanonical unfolding | Low | Existing callers explicitly unfold gam in normalization. Full caller inlining retains all eight signatures/proofs. No recursive simp rule introduced. |
| Instance priority collision | None | No instance registration or priority change. |
| Universe issues | None | Native levelParams=[]; concrete ℝ/ℕ fix the universes. Generic Field helper is separately polymorphic. |
| Coercion ambiguity | None | Nat casts are fixed by ℝ; correctly typed negative CoeFun ℝ instance probe fails with a genuine synthesis message, not a metavariable error. |

Overall **LOW** (routine unfolding/API choice); no HIGH mitigation needed. Evidence in isolated and project native sources/receipts above.

## Phase 4.6 — Five proof-strategy checks

| # | Question | Assessment | Alternative/cost relevance |
|---|---|---|---|
| 1 | Topology ε–δ? | Definition has no proof; downstream continuity already uses ContinuousAt. | Local continuousDelta proof verified by unfolding/fun_prop. |
| 2 | Element algebra versus subobjects? | Only real arithmetic, not an ideal/submodule argument. | No subobject abstraction indicated. |
| 3 | Sequences versus nets? | No sequence argument. | No net restatement needed. |
| 4 | Construction versus universal property? | Numerical parameter selection only. | No universal property identified. |
| 5 | Helper mathlib SHOULD have? | No missing subtraction/division/sqrt infrastructure. | General index/counting theorems are separate potential contributions; do not mistake their novelty for gamma's. |

Strategy **MATHLIB-IDIOMATIC** as a local scalar definition. The question is statement/API grain, not proof optimization or implementation expense.

## Phase 5 — Fifteen formal search cells

All three forms were searched with all five actual methods. External semantic/type search revisions may differ from this pinned checkout. Exact returned candidate signatures and full raw receipts retained. Local name index reported error/error/warming; no empty local response is used to prove absence.

| Form | Method | Actual query | Result |
|---|---|---|---|
| current | leanfinder | `Roth gamma parameter (m - 4*(1+3*delta)*n*sqrt m)/2 index cutoff in Diophantine approximation` | rothNumberNat_le, rothNumberNat_def, cornersTheoremBound, Behrend.roth_lower_bound; [search-current-leanfinder.json](../evidence/Roth.gam/search-current-leanfinder.json) |
| current | loogle | `Real.sqrt, _ / 2` | Real.sqrt_two_lt_three_halves, Real.sqrt_one_add_le, Real.exp_half, Real.cos_pi_div_four; [search-current-loogle.json](../evidence/Roth.gam/search-current-loogle.json) |
| current | leansearch | `Roth auxiliary polynomial index parameter gamma m minus lambda divided by two` | Behrend.bound_aux', Behrend.bound_aux, Behrend.roth_lower_bound, Complex.GammaAux_recurrence1; [search-current-leansearch.json](../evidence/Roth.gam/search-current-leansearch.json) |
| current | rg | `Roth\.gam / def gam\b / 4 \* \(1 \+ 3 \*.*sqrt` | exit1; complete source receipt; [search-current-rg.json](../evidence/Roth.gam/search-current-rg.json) |
| current | local_search | `gam` | Roth.gam, Ordinal.gamma, ProbabilityTheory.gammaPDF, EisensteinSeries.gammaSet; index=error; [search-current-local_search.json](../evidence/Roth.gam/search-current-local_search.json) |
| standard | leanfinder | `Roth main lemma auxiliary polynomial index at least gamma minus eta parameter m lambda halves` | Behrend.roth_lower_bound, Behrend.bound_aux', cornersTheoremBound, Behrend.bound_aux; [search-standard-leanfinder.json](../evidence/Roth.gam/search-standard-leanfinder.json) |
| standard | loogle | `"index", Real.sqrt` | no results; [search-standard-loogle.json](../evidence/Roth.gam/search-standard-loogle.json) |
| standard | leansearch | `Diophantine approximation auxiliary polynomial high index centered cutoff m/2` | Rat.den_le_and_le_num_le_of_sub_lt_one_div_den_sq, Liouville.exists_pos_real_of_irrational_root, LindemannWeierstrass.exp_polynomial_approx, Dioph; [search-standard-leansearch.json](../evidence/Roth.gam/search-standard-leansearch.json) |
| standard | rg | `Roth / Diophantine / index.*polynomial / polynomial.*index` | exit0; complete source receipt; [search-standard-rg.json](../evidence/Roth.gam/search-standard-rg.json) |
| standard | local_search | `Diophantine` | no results; index=error; [search-standard-local_search.json](../evidence/Roth.gam/search-standard-local_search.json) |
| abstract | leanfinder | `half difference real numbers subtraction division by two cutoff midpoint` | ProbabilityTheory.sub_half_inf_sub_mem_Ioo, ProbabilityTheory.add_half_inf_sub_mem_Ioo, add_sub_div_two_lt, right_sub_midpoint; [search-abstract-leanfinder.json](../evidence/Roth.gam/search-abstract-leanfinder.json) |
| abstract | loogle | `_ - _ / _` | Int.sub_ediv_of_dvd, Nat.mul_sub_div_of_dvd, Nat.mul_sub_mul_div_of_dvd, Int.sub_ediv_of_dvd_sub; [search-abstract-loogle.json](../evidence/Roth.gam/search-abstract-loogle.json) |
| abstract | leansearch | `x minus y divided by two equals x divided by two minus y divided by two` | sub_div, tsub_div, div_sub_div_same, ofAdd_sub; [search-abstract-leansearch.json](../evidence/Roth.gam/search-abstract-leansearch.json) |
| abstract | rg | `theorem sub_div\b / theorem div_sub_div_same\b / sub_self_div_two / right_sub_midpoint / left_sub_midpoint` | exit0; complete source receipt; [search-abstract-rg.json](../evidence/Roth.gam/search-abstract-rg.json) |
| abstract | local_search | `sub_div` | ENNReal.sub_div, NNReal.sub_div, sub_div, sub_div'; index=warming; [search-abstract-local_search.json](../evidence/Roth.gam/search-abstract-local_search.json) |

Positive arithmetic candidate `sub_div : ∀ {K} [DivisionRing K] (a b c), (a-b)/c=a/c-b/c` was checked natively and used in project divideSub. It is a normalization identity, not the definition of Roth's cutoff. Native Real.sqrt and continuity/sub/div signatures also verified. Search hits rothNumberNat/Behrend concern arithmetic-progression-free sets, not Diophantine approximation; GammaAux concerns the gamma function. Pinned source confirms those mismatches. `left_sub_midpoint`/`right_sub_midpoint` are generic affine midpoint identities; even a midpoint spelling would need the separately chosen λ and supplies no new Roth parameter semantics. The midpoint source requires invertibility of2; arbitrary Field alone was not established as a midpoint interface, and no midpoint bridge was executed. No exact semantic replacement established; this is a search conclusion with stated limitations, not a proof of global absence. The compiled generic routes test casts, real arithmetic, inference and the missing Roth target directly.

[mathlib-inputs.json](../evidence/Roth.gam/mathlib-inputs.json) archives the exact pinned Sqrt/Field/OrderField/Midpoint/AP-Three/DiophantineApproximation source files and hashes.

## Phase 5.5 — Three statement-shape checks

**Normal form:** equivalent spellings `(m−λ)/2`, `m/2−λ/2`, and `m/2−2(1+3δ)n√m` were verified (rfl/sub_div/ring respectively). There is no established mathlib canonical semantic gamma spelling. Retain the short half-difference with its documented λ; no O(n²) equivalence API proposed. RHS orientation is n/a to a scalar def, but the probe equalities orient from gamma to explicit arithmetic.

**Syntactic generality:** realParameter formula and independent halfGap were attempted and compile. Natural degree/dimension arguments remain easiest to supply at existing callers; replacing them throughout is not justified by an expression-only widening. An admissible real γ argument for index theorems could compose better with alternative tail bounds.

**Superfluous arguments:** δ,n,m all matter; three explicit counterexamples to constancy compile in the isolated source. No typeclass/propositional assumptions to remove. Overall **SHIP-AS-STATED locally**; future upstream publication depends on the two Phase7 API questions.

## Phase 6.0 — Complete source callers and inline audit

15 lexical executable occurrences in eight declarations: five same-file declarations, three external-to-file declarations in one file (Main). Module documentation and the target definition are excluded.

| Caller | Occurrences (signature/body) | Mathematical use | Refactor if name becomes local/expanded |
|---|---|---|---|
| `Roth.exists_delta` Roth/Main.lean:227 | 4 (1/3) | Continuity and strict denominator-gap bound | Replace each gam δ n m by ((m : ℝ) - lam δ n m) / 2, using f.natDegree for n where present; remove gam from explicit unfold/simp lists. Full written caller proof replay and all original signatures verified. |
| `Roth.exists_roth_parameters_aux` Roth/Main.lean:410 | 1 (1/0) | Package compatible numerical choices | Replace each gam δ n m by ((m : ℝ) - lam δ n m) / 2, using f.natDegree for n where present; remove gam from explicit unfold/simp lists. Full written caller proof replay and all original signatures verified. |
| `Roth.one_lt_roth_eval_bound_aux` Roth/Main.lean:453 | 1 (1/0) | Taylor decay exponent in the evaluation comparison | Replace each gam δ n m by ((m : ℝ) - lam δ n m) / 2, using f.natDegree for n where present; remove gam from explicit unfold/simp lists. Full written caller proof replay and all original signatures verified. |
| `Roth.eta_lt_gam_iff` Roth/MainLemma.lean:100 | 2 (1/1) | Gap inequality equivalence | Replace each gam δ n m by ((m : ℝ) - lam δ n m) / 2, using f.natDegree for n where present; remove gam from explicit unfold/simp lists. Full written caller proof replay and all original signatures verified. |
| `Roth.exists_mem_RSet_le_index_of_log_bound_aux` Roth/MainLemma.lean:618 | 2 (1/1) | Choose the concrete index cutoff | Replace each gam δ n m by ((m : ℝ) - lam δ n m) / 2, using f.natDegree for n where present; remove gam from explicit unfold/simp lists. Full written caller proof replay and all original signatures verified. |
| `Roth.exists_auxiliary_polynomial_of_log_bound_aux` Roth/MainLemma.lean:643 | 1 (1/0) | State high index for the auxiliary polynomial | Replace each gam δ n m by ((m : ℝ) - lam δ n m) / 2, using f.natDegree for n where present; remove gam from explicit unfold/simp lists. Full written caller proof replay and all original signatures verified. |
| `Roth.exists_auxiliary_polynomial_with_index_gap_aux` Roth/MainLemma.lean:692 | 1 (1/0) | Subtract eta and compare with Theta | Replace each gam δ n m by ((m : ℝ) - lam δ n m) / 2, using f.natDegree for n where present; remove gam from explicit unfold/simp lists. Full written caller proof replay and all original signatures verified. |
| `Roth.main_lemma` Roth/MainLemma.lean:735 | 3 (1/2) | Final polynomial index statement and derivative choice | Replace each gam δ n m by ((m : ℝ) - lam δ n m) / 2, using f.natDegree for n where present; remove gam from explicit unfold/simp lists. Full written caller proof replay and all original signatures verified. |

[source-search.json](../evidence/Roth.gam/source-search.json) and [tracked-source-search.json](../evidence/Roth.gam/tracked-source-search.json) agree exactly; no-ignore inventory covers the canonical tracked production modules. Full caller bodies/signatures/hashes retained in [callers.json](../evidence/Roth.gam/callers.json).

The inline-derivation search finds the expanded cutoff `(m−4 c n√m)/2` in the rpow auxiliary lemma, the scaled counting cutoff in mul_card_filter_weight_le_aux, and the δ=0 limiting ratio in exists_m. These are real parameter-generalized/limiting calculations, not unused duplicated gamma definitions. No second exact gamma definition was identified.

| Decl A | Decl B | Same statement? | Same proof/construction? | Duplication verdict |
|---|---|---|---|---|
| gam | lam | No; cutoff versus loss | gam subtracts half of lam from half dimension | Keep distinct roles if both names retained. |
| gam | exists_mem_RSet_le_index_of_rpow_bound_aux cutoff | Specialized value only (c=1+3δ) | Same half-difference arithmetic within a substantive existence theorem | Factor the admissible-cutoff theorem boundary; no duplicate definition to delete. |
| gam | mul_card_filter_weight_le_aux cutoff | Specialized value only (a=(1+3δ)n) | Same centered threshold within a counting bound | Counting is substantive independent content; not an arithmetic alias replacement. |
| gam | halfGap scratch probe | Old form specializes after supplying chosen lambda | Same subtraction/division, but helper is newly written | Representation probe only; not existing mathlib. |


The fresh canonical293 audit separately finds eight direct kernel type consumers and eight direct value consumers. eta_lt_gam_iff has a type reference but its proof normalizes gamma away; roth_of_isIntegral has no lexical gamma yet its elaborated proof stores an inferred parameter containing gamma. These facts explain why lexical and kernel scopes differ. Full arrays are in verification.json; all293 names match tracked order, are unique/present, and have kernel values. This is not a transitive dependency/simp-closure audit.

## Phase 6 — Actual composition and full caller experiment

1. **Old arithmetic spelling:** `((m : ℝ) - Roth.lam δ n m) / 2` needs only subtraction/division after lambda is supplied. It is verified by rfl. Roth.lam is a project definition and cannot be counted as an existing mathlib building block.
2. **Mathlib-only expanded formula:** the isolated formula uses existing Real.sqrt, casts, multiplication, addition, subtraction and division. It compiles directly. Fully expanded construction exceeds three primitive arithmetic calls; no strict ≤3 existing-mathlib-call semantic replacement was established. This arithmetic is not novel theorem content either.
3. **Arithmetic normalization:** `sub_div _ _ _` gives the divideSub identity; the shorter coefficient form needs ring after unfolding. These prove equalities about the chosen formula, not a pre-existing definition of that chosen parameter. Newly written halfGap/gapComparison are not existing mathlib.
4. **Caller experiment:** full original MainLemma and Main written bodies replayed after removing gam and replacing all15 executable occurrences with the half-difference expression. Explicit gam unfold/simp-list entries removed; Main's eta_lt_gam_iff/main_lemma use the replayed local versions. All eight original signatures retained by defeq, including five private signatures checked via mkPrivateNameCore and three public rfl equality probes. All eight caller axiom prints clean. No gam identifier remains in the exact written inline source. The imported transitive project proof graph can still contain original definitions; no target-free imported closure claim is made.

Conclusion: **NOT-COMPOSABLE under the strict ≤3 existing-mathlib-call semantic test**; direct arithmetic inlining is verified. Semantic naming may still be worthwhile. The test alone does not force YES: the remaining issue is the value of publishing this exact numerical choice versus the reusable admissible-cutoff boundary.

[inline-executed.lean.txt](../evidence/Roth.gam/inline-executed.lean.txt); [inline-receipt.json](../evidence/Roth.gam/inline-receipt.json); [verification.json](../evidence/Roth.gam/verification.json).

## Phase 7 — Independent verdict and actionable boundary

**BORDERLINE-needs-human.** Gamma is a useful locally named scalar: its eight callers include public main-lemma and parameter-selection signatures. Literature confirms the exact local formula and also displays alternative high-index cutoffs. The full inlining experiment establishes no defeq/instance necessity for the named anchor. Arithmetic/sqrt API already exists; no exact semantic mathlib hit was established, and the strict ≤3 composition test cannot count project lambda as mathlib. Neither arithmetic novelty nor parent theorem usefulness is sufficient to pick a standalone upstream definition.

The following questions are concrete future upstream design choices after a completed assessment; no user response is required to finish this overview:

1. For an upstream Roth main-lemma development, should this exact gamma be a public documented parameter, or a local abbreviation expanded in theorem statements?
2. Should the reusable auxiliary-polynomial API accept an arbitrary admissible real index cutoff, with this gamma chosen only in the Roth application?

Action now: retain the project definition and record this completed assessment. For a future upstream proposal, settle those two API choices with the main-lemma statement. If expanded, apply the exact replacements in the complete caller table; if retained, document the specific cutoff choice and expose only companion lemmas consumers actually need. A local continuity lemma can simplify exists_delta (verified continuousDelta). No production refactor is requested/performed here.

A YES-only exact home/PR-title/reviewer/grouping checklist is n/a to this verdict; no unaccepted project declaration is counted as existing mathlib. Accepted-verdict snapshot retained for provenance, not inherited judgment. No cost-based downgrade or unresolved proof task is hidden in BORDERLINE.

## Phase 8 — Completed evidence and handoff

All mandatory phases PASS. Four complete clean native sets, exact18 isolated imports, nine disk imports unchanged, complete293 canonical audit, full caller inlining/signature checks, formal15 cells and all named literature channels completed. One cold-loading partial original receipt remains separately labeled, no rejected native proof attempt. Standard axioms only; no warning/error/sorry/unsafe/new axiom/native_decide/resource raise accepted. Full native print had no elision marker. Production17 hashes, local literature/mathlib source hashes, current copy manifest, local links, clean URL guard and secret scan checked by the portable validator before freeze. Root acceptance remains pending independent review; no worker publication or Git write.

[assessment.json](../evidence/Roth.gam/assessment.json); [verification.json](../evidence/Roth.gam/verification.json); [validate.py](../evidence/Roth.gam/validate.py); [copy-manifest.json](../evidence/Roth.gam/copy-manifest.json).
