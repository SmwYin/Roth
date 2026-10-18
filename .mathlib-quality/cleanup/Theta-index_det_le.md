# Dedicated audit — `Roth.index_det_le` (ORIGINAL 28/35)

Scope: one original declaration, two necessary private extractions, one routine caller application. No Git/shared-ledger edits. The parent owns publication and fresh separate audits of both new helpers. Target documentation and all three Step comments preserved verbatim in their original order. No prior audited helpers changed.

## Baseline and mathematical understanding

Initial full source SHA256 `ac43e6d19ce869213d3d0f6a260ffc92ab8f419d9b2be320483539746e5434a9`, 980 lines. Inherited same-source complete native LSP: `/private/tmp/roth-theta-sum-index/final-lsp.json`, success true, partial false, timed_out false, failed_dependencies [], 0 errors, 14 warnings. Inherited owner full build 110.300s and separate LeanEval 32.749s; neither is represented as fresh worker evidence. No target profile inherited.

Fresh uncontended baseline: `lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/roth-theta-index-det/baseline.lean`, corrected complete prefix through target, exit 0. Raw UTF8 `/private/tmp/roth-theta-index-det/baseline-profile-corrected.log`, 143925827 bytes; exact anchor/node data in `baseline-timings.json`. Total target 2083.744ms: outer command 137.994ms, async proof 1739.162ms, associated top-level async addDecl/kernel and lint jobs included, no nested double counting. First diagnostic run had a missing `end Lemma6` after the target; it exited 1 and is not accepted baseline evidence. Corrected run preserves every exact preceding import/declaration/context and adds only section/namespace closure. No profile masks or raised limits.

Mathematics: bound coefficients of the determinant via the general determinant Hasse-derivative estimate and uniform degree cap. Separation makes each coefficient a unique product. A nonzero integer coefficient has absolute value at least one, giving bounds on each factor. Add indices after injective renaming; scale positive weights by l and apply the defining supremum bounds for Θ. This yields lΦ. δ, its positivity, and the upper bound on l never enter this argument. The coefficient bound on R itself implies B≥0, so the separate B≥1 premise is redundant too.

## Full 24-item substantive audit

| # | Item | Finding/action |
|---|---|---|
| 1 | LINT | Baseline target warnings: unused DecidableEq τ, hl′, hδ. Approved removal eliminates these; final native diagnostics recorded below. No warning suppression. |
| 2 | HAVE SCAN | Complete inventory below; aliases/trivial intermediates removed, real estimates extracted, rewritten coefficient inequalities retain their local h1. |
| 3 | SET_OPTION | None in target; none introduced. Scratch automation has a lower local search budget only, never production or performance limits. |
| 4 | SIMP SQUEEZE | Original final nonterminal `simp only [Function.comp_def] at *` eliminated. Two terminal simp sites are explicitly squeezed as measured performance exceptions (386ms hsum,291ms final combination before restriction). Unsqueezing uniqueAlgEquiv conversion rewrites too early; replaced those three with rw/rwa and direct exact, rather than keeping fragile simp-only blocks. |
| 5 | NAMING | `index_det_le` describes its comparison; no banned abbreviations, numeric scheme, `_ge_`/`_gt_`. Private names describe coefficient and separated-product content and end `_aux`; no rename required. |
| 6 | LINE PACKING | Every signature line measured in codepoints below, with complete next binder/application groups; no mid-ascription or MvPolynomial type break. |
| 7 | BY PLACEMENT | Each `:= by` stays on its preceding statement line. |
| 8 | FORMAT | Two-space proofs, four-space signatures, no blank proof lines, Unicode mathematical lambdas, no haveI/letI. |
| 9 | COMMENTS | 3/3 original Step signposts remain in public proof at corresponding calls/retained factor estimate. |
| 10 | DOCSTRING | Public original docstring retained byte-for-byte. New private helpers have no docstrings. |
| 11 | VISIBILITY | Public wrapper retained per user instruction. Both necessary extracted proof helpers private; no public API proliferation. Classic import dialect. |
| 12 | STRUCTURE | Original 94 proof lines decomposed into coefficient estimate and separated-product index estimate; final counts below. The only new obtain occurs inside hVc, with <10-line continuation; no long case/constructor branch. No conjunction added to public conclusion. |
| 13 | MATHLIB | Five actual search methods below; use existing pow/mul monotonicity, index APIs and integer coefficient facts directly. Neither helper is a 1–3-call convenience wrapper. |
| 14 | JUNK DEF | n/a: theorem; no definitions/abbrevs added or changed. |
| 15 | EXISTS LEMMA | n/a: public inequality, not a trivial existential wrapper. Nonzero coefficient witness remains visibly correlated with its nonzero proof inside hVc. |
| 16 | SHOW/CHANGE | No redundant show/change in target or helpers. |
| 17 | PUSH_NEG | None in target; none introduced. |
| 18 | GENERALISE | Every effective binder has compiled drop/weakening evidence below. Exact approved/removal adapter includes DecEq, δ, hB, hl′, hδ; retained wrapper/domains and full caller contract preserved. |
| 19 | INEQUALITY | All signature occurrences checked below; no reversed inequality notation. |
| 20 | NORMAL-FORM | Keep canonical real index ≤ lΦ, natural degree bounds and integer coefficient absolute values. No equivalent-form API added. |
| 21 | SYNTAX-GEN | Existing RSet/public wrapper is useful at actual caller; retain it. hB is derived immediately from its coefficient field. |
| 22 | IMPORT-FANOUT | No production import added; no downstream dependency fanout. |
| 23 | CASTS | Retained integer→real, natural→real and Fin→Nat casts are actual coefficient/degree/index bridges. Explicit base `(1 : ℝ)` in pow monotonicity fixes elaboration, not redundant. All introduced names compile. |
| 24 | INSTANCE-NAME | No named instances created; omitted anonymous DecEq may naturally renumber synthetic binders. Explicit user-written names/order/BinderInfo checked exactly. |

### Original have inventory

All original haves, with original line references; typed `by` blocks contain proof content, never classified as trivial aliases.

| Original line/name | Use/action |
|---|---|
| 423 hB0 | Derived from hR coefficient bound, no longer from removed hB. |
| 424 hl0 | Trivial alias inlined as hl. |
| 426 hprod | Real proof retained in coefficient helper; one use in pow monotonicity. |
| 431 hsum; 432 anonymous sum bound | Replaced by sum_le_sum → Nat.mul_le_mul_right and one simpa; genuine proof. |
| 437 hFcoef | Used for both factor estimates; retained via coefficient helper. |
| 441 h1; 443 h2 | Single-use power monotonicity terms inlined. |
| 445 h4 | Positivity fact replaced by immediate side condition to explicit mul_le_mul. |
| 455 hb₀ | Single-use leading coefficient nonzero fact inlined. |
| 456 hUc; 457 h1; 459 h2 | hUc retained; h1 is rewritten before use; h2 cast fact inlined. Nonlinear arithmetic replaced by le_mul_of_one_le_right.trans. |
| 463 hVc; 464 h1; 466 h2 | hVc retained; h1 is rewritten; h2 inlined. Nonlinear arithmetic replaced by le_mul_of_one_le_left.trans. |
| 471 hV′0 | Genuine nonzero conversion retained in separated-product helper. |
| 473 hUmem | Single-use constructor inlined as ⟨hU,hUd,hUc⟩. |
| 474 hVmem | Genuine degree/coefficient conversion retained in separated-product helper, branches ≤2 lines. |
| 481 hinjU | Direct standard Option.some_injective used inline. |
| 482 hinjV | Used twice; retained, proof is Subsingleton.elim. |
| 484 hmU; 486 hmV | Single-use map nonzero terms inlined into index_mul. |
| 488 hmapF | Single-use equality eliminated; direct rewrite with hF, aeval_X_eq_rename, map_mul/map_rename. |
| 491 hrU; 492 hrV | Single-use positivity functions inlined into index_le_Θ. |
| 496 hlR | Genuine cast positivity retained to apply div_le_iff₀ twice. |
| 497 hU′; 502 hV′′ | Both field_simp identities eliminated: rewrite index_mul_left_weights in Θ inequalities. |
| 508 hUΘ; 509 hVΘ | Retained and rewritten before direct add_le_add. |
| 512 anonymous mul bound; 513 anonymous mul bound | Replaced by direct div_le_iff₀ applications under add_le_add. |

## Five-method actual mathlib search

[A] Native Lean-Finder query “upper bound index of a determinant of multivariate Hasse derivatives integer polynomial coefficients”: Chevalley numerical/degree bound results, no applicable theorem.
[B] Native Loogle first `MvPolynomial.hasseDeriv, Matrix.det` returned an unknown-identifier index error; corrected query `"hasseDeriv", "det"` returned an empty items list. The first failure is not absence evidence.
[C] Native LeanSearch “coefficients determinant Hasse derivatives polynomial bound”: Polynomial.coeff_bdd_of_roots_le, natDegree_hasseDeriv_le, coeff_le_of_roots_le, Chebyshev coefficient estimate. None has the determinant/index conclusion.
[D] Full local rg of index/determinant and coefficient/determinant variants under Mathlib/Algebra/MvPolynomial and LinearAlgebra/Matrix; raw `grep-search.log` contains polynomial characteristic-determinant identities, not this weighted-index estimate. Full-name rg for new helper candidates returned no hits. No truncated full-name search used for absence.
[E] Native lean_local_search `index_det`: existing project target only. `le_mul_of_one_le` locates actual mathlib le_mul_of_one_le_left/right and variants. Index status unavailable means source-backed hits only; it does not prove absence of generated declarations.

Compiled generic-route/automation probes in the exact prefix BEFORE the target, anonymous examples only; they cannot cite the theorem under audit. See `automation.lean`/`automation.log` below. Native multi_attempt is not retried because consecutive earlier workers established its unbounded stall; bounded ordinary compilation is the permitted fallback. Common-equivalents lookup: none of the discrete/compact/coset buckets applies. Partial reusable content is already the existing project APIs `abs_coeff_det_hasseDeriv_le`, `index_mul`, `index_rename`, `index_mul_left_weights`, `index_le_Θ`; use those directly.

## Literature and inversion

Local `.mathlib-quality/references/clean.tex`, lines 735–777, gives exactly coefficient control for U,V and the separate-variable index bound (17); lines 779ff stress scaling the index weights without changing the degree bounds. Native web queries: `"Formalizing Roth" "index" determinant Φ`; `Roth theorem index polynomial product separate variables coefficient determinant lemma 6`. Checked primary texts [Princeton seminar notes](https://web.math.princeton.edu/mathlab/jr02/diophantine.pdf), [Min Ru's Roth notes](https://www.math.uh.edu/~minru/fields/roth.pdf), and [Soundararajan's transcendental number theory notes](https://math.stanford.edu/~ksound/TransNotes.pdf). These support the standard product-index/auxiliary-polynomial setting; none supplies a reason to retain δ or l's upper bound for this upper-bound stage. No connected math ChatGPT MCP is exposed, so that route is unavailable, not searched-and-empty.

Mandatory inversion check: after coefficient control, the index argument does not use the determinant, R, or D. It becomes the private separated-product estimate for arbitrary coefficient bound M and separated U,V, and the public wrapper applies it after hF. Conversely the determinant coefficient helper takes arbitrary derivative matrix E, not the special D/ν form. Both abstractions compile independently as part of the candidate. Preserve existing public wrappers/domains; no unrelated abstract public API proposed.

## Complete 42-rule golf pass

| Rule | Actual result |
|---|---|
| 1.1 | No by-exact wrapper; trivial hl0/hUmem terms inlined. |
| 1.2 | No by-rfl proof. |
| 1.3 | hV′0 conversion uses rwa. |
| 1.4 | Natural sum bound uses simpa from sum_le_sum; final index bound simpa using add_le_add. |
| 1.5 | No trailing rfl. |
| 1.6 | hU membership anonymous constructor at call; hV membership retained constructor. |
| 1.7 | Direct existing lemma applications; no apply/exact chain remains. |
| 1.8 | No contradiction or pushed negation. |
| 1.9 | Lambdas express actual transformations or finset premises; no removable eta wrapper. |
| 1.10 | All trivial single-use original aliases inlined as have inventory records; rewritten h1 and Θ bounds retained. |
| 1.11 | No apply-intro pair. |
| 1.12 | No redundant show. |
| 1.13 | Existing hR component projections remain at two semantically distinct uses; nonzero witness obtained only in its local coefficient branch. |
| 1.14 | Adjacent rewrites merged; all map/index rewrites in one call. |
| 1.15 | Terminal simp-only trials unsqueezed first; measurements then justified explicit lists for hsum and final index combination (386/291ms before). Problematic uniqueAlgEquiv conversions use rw/rwa + exact. |
| 1.16 | No nonterminal bare simp remains. |
| 1.17 | Inequality .trans and map-iff .2 notation used. |
| 1.18 | Parentheses retained for grouped theorem arguments under multiline expressions; no dollar syntax. |
| 1.19 | No push_neg. |
| 1.20 | No trivial existential helper. |
| 2.1 | Whole-proof grind tested in clean anonymous prefix; failure recorded in automation log. |
| 2.2 | No retained grind with redundant preceding tactics. |
| 2.3 | hsum and final index combination consolidated to simpa using. |
| 2.4 | No analytic function-property goal. |
| 2.5 | Actual positivity side conditions retained; no coefficient nlinarith. |
| 2.6 | Original expensive gcongr replaced by explicit pow/mul monotonicity terms. |
| 2.7 | No linear integer search required; exact_mod_cast/Nat.mul_le_mul_right handle actual natural inequalities. |
| 2.8 | Whole-proof aesop tested; fails in clean prefix. |
| 2.9 | Numeric base-two monotonicity uses norm_num; casts use exact_mod_cast. |
| 2.10 | Goal not a closed finite computation; decide cannot establish arbitrary-polynomial inequality. |
| 2.11 | Two original field_simp identities removed entirely by rewriting index_mul_left_weights in inequalities. |
| 2.12 | Original ring reorder eliminated by mul_right_comm in hsum; no polynomial-identity goal remains for linear_combination. |
| 2.13 | Two factors have different variable domains; no symmetric case split to wlog. |
| 2.14 | Final calc and linarith collapsed to explicit mul/add inequalities and .trans; nontrivial product comparison retained. |
| 2.15 | Degree and coefficient membership branches use distinct existing lemmas; no duplicated automation branch. |
| 3.1 | No erw. |
| 3.2 | No continuity/measurability tactic. |
| 3.3 | No omega introduced. |
| 3.4 | No rfl-destructuring followed by redundant substitution. |
| 3.5 | No global simp/grind attributes warranted for file-local quantitative bound. |
| 3.6 | Whole simp_all tested in clean prefix; no matching simple closing proof. |
| 3.7 | No heartbeat/recursion limit added or retained. |

Step-back review: no single-tactic exact?/apply?/grind/aesop proof found in uncontaminated prefix. The direct proof follows the source's three mathematical stages, while replacing the measured costly arithmetic rather than merely relocating it. RSet is the deliberate retained public input interface, and no new structure bundles independent estimates.
## Every effective parameter: compiled drop/weakening probes

Positive evidence is separate from expected-failure files. `candidate-compatibility-final.log` is exit0 and proves exact removal of the five original binders plus full old telescope recovery and all standard axioms. `binder-negative.lean` uses autoImplicit=false and repeats the actual candidate proof with one ordinary binder removed each time; `binder-negative-ranges.json` and `binder-negative-results.json` classify all twenty retained ordinary binders. Unknown-identifier failures establish that the *current proof* needs that input; they are not mathematical counterexamples. A few malformed data-drop recoveries also hit default 200000 heartbeats, after the corresponding primary unknown-identifier error; no budget was raised. Initial section-class omission probes fail at referenced-instance checks; a clean standalone class/type-variable probe against built imports is recorded separately below.

| Original effective parameter | Class/use | Concrete compiled candidate/result |
|---|---|---|
| τ : Type u | Variable domain, already universe polymorphic | Standalone no-autoImplicit omission ill-typed; preserve universe parameter. |
| [Fintype τ] | Class; cardinality in M and finite Θ/index domains | Drop/Finite replacement tested; retain Fintype. No meaningful parent weakening preserves current card-valued interface. |
| [DecidableEq τ] | Decidability | Actual final type omits it with local classical; positive full-old adapter passes. |
| δ : ℝ | Unused numerical parameter | Removed together with its only proof hypothesis; exact positive adapter passes. |
| r : Option τ → ℕ | Degree/index data | probe_drop_r: unknown r in dependent binders/conclusion; retain domain. |
| hr0 : ∀ j, 0 < r j | Positive index weights | Drop: unknown hr0; weaken all < to ≤: index helper application type mismatch. Retain strict positivity. |
| r₁ : ℕ | Uniform degree cap | Drop: unknown r₁ in cap and M; retain. |
| hr₁ : ∀ j, r j ≤ r₁ | Uniform degree bound | Drop: unknown hr₁ at coefficient helper; natural weak inequality already used. |
| q : Option τ → ℕ | Rational point denominators | Drop: unknown q in point and Φ; retain. No positive-denominator assumption introduced. |
| B : ℝ | Coefficient-bound parameter in RSet/M | Drop: unknown B; retain data. |
| hB : 1 ≤ B | Redundant proposition | Removed entirely, rather than weakened: hRc implies 0≤B from coefficient 0. Final candidate and exact original adapter pass; parent explicitly recommended/accepted under current user authority. |
| R : MvPolynomial (Option τ) ℤ | Polynomial data | Drop: unknown R in hR/determinant; retain. |
| hR : R ∈ RSet B r | Degree and coefficient bounds | Drop: unknown hR at coefficient helper. The helper uses only degree/coefficient fields, but the user's retained-wrapper/domain preference protects this public RSet interface. No wrapper churn. |
| h : Option τ → ℤ | Rational point numerators | Drop: unknown h; retain integer point data. |
| hh : ∀ j, IsCoprime (h j) (q j : ℤ) | Θ-admissibility | Drop: unknown hh at index helper; both some/none restrictions needed. |
| l : ℕ | Determinant size/weight scale | Drop: unknown l in dependent D/Fin and conclusion; retain. |
| hl : 1 ≤ l | Positive size | Drop: unknown hl; weaken to 0≤l: helper application type mismatch. Avoid unnecessary l=0 API case churn. |
| hl′ : l ≤ r none + 1 | Unused upper size bound | Exact positive removal passes; the caller retains its own hl′ for its other estimates. |
| D : Fin l → (τ →₀ ℕ) | Derivative data | Drop: unknown D in determinant and coefficient-helper call. Helper generalized to arbitrary derivative matrix E, public input preserved. |
| U : MvPolynomial τ ℤ | Separated first factor | Drop: unknown U; retain domain. |
| V : Polynomial ℤ | Univariate last factor | Drop: unknown V; retain domain. |
| hU : U ≠ 0 | Nonzero coefficient witness/membership | Drop: unknown hU; retain. Replacing by weak sign does not define a natural polynomial order. |
| hV : V ≠ 0 | Leading coefficient and nonzero embedding | Drop: unknown hV; retain. |
| hUd : ∀ j, degreeOf j U ≤ l*r(some j) | Θ admissible degree bound | Drop: unknown hUd; already weak/pointwise. |
| hVd : V.natDegree ≤ l*r none | Θ admissible degree bound | Drop: unknown hVd; already weak. |
| hF : det = rename U * aeval V | Exact factorization | Drop: unknown hF in coefficient separation and final rewrite; equality required by current statement/proof. |
| hδ : 0 < δ | Unused proposition | Removed with δ, positive exact adapter passes. |

Big-change assessment: retain integer coefficient, real index, Option separation, RSet wrapper, and existing public name/conclusion. A general field version would lose the integer absolute-value ≥1 fact and requires a different arithmetic coefficient lattice; no recommendation. No previous explicit Θ hB/hr or caller hq preference reopened.

## Measured signature packing and inequality scan

Widths are Unicode codepoints. Next tokens below are COMPLETE binders or the next mathematical application block, never a detached word from a binder/ascription. Every `:= by` is part of the measured signature. Reference: actual public/private type printouts at `format.width 100` in `actual-compatibility.log`.

### coeff_det_le_lem6M_aux

| Source line | Chars | Next complete binder/application group | Arithmetic | Action |
|---|---:|---|---|---|
| 405 | 94 | `{R : MvPolynomial (Option τ) ℤ}` | 94 + 1 + 31 = 126 > 100 | ok |
| 406 | 67 | `(hRc : ∀ d, |((R.coeff d : ℤ) : ℝ)| ≤ B)` | 67 + 1 + 40 = 108 > 100 | ok |
| 407 | 90 | `(d : Option τ →₀ ℕ)` | 90 + 1 + 19 = 110 > 100 | ok |
| 408 | 96 | `lem6M (Fintype.card τ + 1) r₁ B l := by` | 96 + 1 + 39 = 136 > 100 | ok |
| 409 | 45 | `` | final signature line | ok |

| Inequality occurrence | Signature + hypothesis scan | Action |
|---|---|---|
| 0 | No `≥` or standalone `>` in any Lean signature/hypothesis; all orders use `≤`/`<` | none |

### index_separated_mul_le_aux

| Source line | Chars | Next complete binder/application group | Arithmetic | Action |
|---|---:|---|---|---|
| 430 | 99 | `{h : Option τ → ℤ}` | 99 + 1 + 18 = 118 > 100 | ok |
| 431 | 89 | `{U : MvPolynomial τ ℤ}` | 89 + 1 + 22 = 112 > 100 | ok |
| 432 | 88 | `(hV : V ≠ 0)` | 88 + 1 + 12 = 101 > 100 | ok |
| 433 | 92 | `index (map (Int.castRingHom ℝ)` | 92 + 1 + 30 = 123 > 100 | ok |
| 434 | 34 | `(rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) ℤ) V)` | 34 + 1 + 73 = 108 > 100 | ok |
| 435 | 82 | `(fun j ↦ (h j : ℝ) / q j)` | 82 + 1 + 25 = 108 > 100 | ok |
| 436 | 59 | `` | final signature line | ok |

| Inequality occurrence | Signature + hypothesis scan | Action |
|---|---|---|
| 0 | No `≥` or standalone `>` in any Lean signature/hypothesis; all orders use `≤`/`<` | none |

### index_det_le

| Source line | Chars | Next complete binder/application group | Arithmetic | Action |
|---|---:|---|---|---|
| 469 | 91 | `{q : Option τ → ℕ}` | 91 + 1 + 18 = 110 > 100 | ok |
| 470 | 82 | `{h : Option τ → ℤ}` | 82 + 1 + 18 = 101 > 100 | ok |
| 471 | 81 | `{D : Fin l → (τ →₀ ℕ)}` | 81 + 1 + 22 = 104 > 100 | ok |
| 472 | 94 | `(hUd : ∀ j, degreeOf j U ≤ l * r (some j))` | 94 + 1 + 42 = 137 > 100 | ok |
| 473 | 79 | `(hF : (Matrix.of fun μ ν : Fin l ↦` | 79 + 1 + 34 = 114 > 100 | ok |
| 474 | 38 | `hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det =` | 38 + 1 + 72 = 111 > 100 | ok |
| 475 | 80 | `rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) ℤ) V) :` | 80 + 1 + 74 = 155 > 100 | ok |
| 476 | 80 | `index (map (Int.castRingHom ℝ) (Matrix.of fun μ ν : Fin l ↦` | 80 + 1 + 59 = 140 > 100 | ok |
| 477 | 63 | `hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det)` | 63 + 1 + 71 = 135 > 100 | ok |
| 478 | 79 | `(fun j ↦ (h j : ℝ) / q j)` | 79 + 1 + 25 = 105 > 100 | ok |
| 479 | 93 | `` | final signature line | ok |

| Inequality occurrence | Signature + hypothesis scan | Action |
|---|---|---|
| 0 | No `≥` or standalone `>` in any Lean signature/hypothesis; all orders use `≤`/`<` | none |
## Introduced external identifier verification

| Identifier/group | Verification | Result |
|---|---|---|
| le_mul_of_one_le_left/right | Native local search finds actual Mathlib.Algebra.Order.GroupWithZero.Basic declarations; post-build #check in actual-compatibility.log; both actual target coefficient terms compile | pass |
| div_le_iff₀ | Post-build #check, actual helper applications with positive natural cast | pass |
| Nat.add_le_add_right | Actual coefficient-helper term checked by fresh module build, exact_mod_cast of this named theorem | pass |
| Nat.mul_le_mul_right | Post-build #check and actual hsum proof application | pass |
| mul_right_comm, add_comm, mul_comm | Existing imported standard algebra names; actual fresh helper simp proofs and post-build actual proof values verify references/types | pass |
| mul_le_mul, mul_le_mul_of_nonneg_right, pow_nonneg | Actual fresh coefficient helper proof term/type and collected axioms checked | pass |
| pow_le_pow_left₀/right₀ | Post-build #check and actual monotonicity applications | pass |
| all new private names | Actual environment scan finds exactly one constant for each; actual opaque proof-value/type check and standard axioms pass | pass |

Additional third-helper exploration: while the coordinator briefly imposed a mistaken ≤15 cap, an isolated `abs_coeff_aeval_factor_le_aux` candidate compiled with full target/caller original adapters. Corrected workflow cap is30 here (the target is not a module Main result), so that extraction was not applied and no third helper was introduced. Its native LeanSearch, Loogle, Lean-Finder, local search and full grep found no matching bound (unrelated disjoint-support irreducibility/Chevalley results). This scratch exploration is not an additional audited declaration, follow-up requirement or blocker. The one attempted generated third-helper patch failed verification before any source mutation; subsequent live edits are exactly the two measured `simpa only` performance restrictions.
## Gates and exact compatibility

`/Users/ramin/.elan/bin/lake build Roth.Theta` was invoked AFTER the final packing edit and both measured terminal-simp restrictions and exited 0 (2423 jobs), `final-module-build.log`. The source SHA was `f9ff4b423b085a156e8706bd40b8a8588826394c065e812cea5b800e2313684d` throughout this build and all following final probes. All final proof and packing edits preceded the final module build; the first-introduction snapshot remains immutable. No source edits after the module gate.

Preapply `candidate-compatibility-final.log`: exit0, complete original target + complete caller independently re-proved in immutable namespace. Post-build `actual-compatibility.lean` imports the ACTUAL built Roth.Theta, not the scratch candidate. Its independent original namespace SHA256 is `72cfbff9abab811d59c4037bc09f00e3e5f326d8435ff6dd03f0e73301eb7b2f`; the entire source namespace from the prior immutable probe is preserved. Only the tail chooses exact new drop set `[DecidableEq, δ, hB, hl′, hδ]` for `index_det_le`, and `[]` for `index_le_lem6`. Every retained ordinary binder name, type, order, BinderInfo, universe count and conclusion is checked; anonymous synthetic instance names are exempt from renumbering-only name equality. Full old-telescope lambda adapters and proof equality recoveries typecheck. The independent original opaque proof values use `value! true`, and each inference matches its declared type.

Actual-built post-build probe exited 0, no `PANIC`, error or `sorryAx`; both full original target/caller PASS markers present. `Lean.collectAxioms` for original proofs, actual target/caller and recoveries returns only propext, Classical.choice, Quot.sound. Both private constant names located programmatically from the actual environment; each actual opaque value/type and standard-axiom set separately checked with its own PASS marker.

`class-negative.lean` against built imports uses autoImplicit=false: omitting τ produces Unknown identifier τ, and replacing Fintype by Finite produces failed synthesis of Fintype τ. Expected exit1, separate from all positive/axiom checks. The ordinary-binder batch has twenty distinct primary unknown-identifier failures, plus actual application type mismatches for weak hr0/hl; full range/result map retained.

Fresh COMPLETE native `lean_diagnostic_messages` call used ONLY file_path + timeout_s=120, no declaration/line/severity filter. `final-lsp.json`: success=true, partial=false, timed_out=false, failed_dependencies=[], zero errors, eleven warnings. No target/helper warning. Residual warnings: copyright/header at1; hr at93; hB/hr at101 (explicit retained Θ_nonneg API); hB at109 (retained Θ_le_card); hr at129 (retained Θ_mono); hr at252; index_le_lem6 DecEq at504 and500 (next reserved original audit); its explicitly retained hq at506; Θ_option_le DecEq at602 (later original audit). No warnings suppressed.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Exact `/Users/ramin/.elan/bin/lake build Roth.Theta`, exit0, final-module-build.log. |
| definition_protected | pass | No existing def/abbrev/import or other declaration touched; byte-exact prefix/tail verification. |
| theorem_statement_protected | pass with authorized removal | Only target exact drop set DecEq/δ/hB/hl′/hδ. Complete immutable-original adapters and actual built types check retained API. |
| caller_full_contract | pass | Whole original index_le_lem6 proof/type/binders/axioms recovered; own δ/hδ0/hB/hq/DecEq and every other binder retained. Only hupper application drops arguments. |
| structure_gate | pass | Public body19, helpers18/26, each ≤30; local obtain continuation5 lines, membership branches2; no branch>10. index_det_le is not named in the module Main results, so its applicable public cap is30, not15. |
| naming_gate | pass | No banned abbreviation/scheme/reversed inequality name; private helpers descriptive `_aux`; no rename queue edit. |
| line_packing_gate | pass | Every signature line measured below; next complete group arithmetic >100, all rows ok. |
| inequality_orientation_gate | pass | Every new/target signature inspected, no ≥ or standalone >. |
| complete_native_LSP | pass | Fresh unfiltered result, zero errors/eleven known unrelated or explicitly retained warnings. |
| actual_value/type/standard_axioms | pass | Post-build actual-compatibility.log, both full recoveries + both private helper checks, no panic/errors/sorryAx. |
| cumulative_no_unintended_breakage | pass within worker scope | Only direct target caller is index_le_lem6, full actual module rebuilt; exact old caller contract recovered. Owner project-wide gates remain pending. |
| lake_build / separate Roth.LeanEval | owner pending | Required only after fresh dedicated audits of both new helpers; inherited earlier owner checks not presented as fresh final checks. |

## Simplify and refactoring status

Full manual holistic simplify pass completed: eliminated redundant M/F aliases, unnecessary hB0 helper argument, coefficient nonlinear arithmetic, duplicated scaling identities, and one-use map/nonzero aliases. Retained the necessary two mathematical abstractions; no new structure or convenience wrapper. Built-in `/simplify` callable is not exposed in this environment; this is an explicitly manual equivalent review, not a claim to have invoked an unavailable tool. Outcome ISSUES-FOUND-AND-FIXED, exact resulting source regated above.

Phase5a: two necessary private extractions and concretely verified redundant-premise removal as authorized; no public restatement, definitions, domains, or prior audited helpers changed. Phase5b: no rename candidates/renames, no shared rename queue touched by this leaf. Owner-owned whole-file phases remain with owner.

## New helper first-introduction records

First full source snapshot `/private/tmp/roth-theta-index-det/first-introduction-snapshot.lean`, SHA256 `42d60acc1b1b3d587ffe568e246cb9ba637ee0a6449a6a2b29d6f02249354ba4`.

| Helper | Exact FIRST text file | First text SHA256 | Initial proof lines |
|---|---|---|---:|
| coeff_det_le_lem6M_aux | coeff_det_le_lem6M_aux-FIRST.lean | 975db962d42a209a6d28afb22593651b0ced9ac12b39ed27acc5854d660b6335 |18|
| index_separated_mul_le_aux | index_separated_mul_le_aux-FIRST.lean |82ea1dcd2a8ced63947dc92f7a43f06b3cf868156e85895cd843a16873a03c92|26|

Both files are in `/private/tmp/roth-theta-index-det/`; manifest `new-helper-first-introduction.json`. Subsequent single-line signature packing only joined coefficient helper's final d binder with LHS. Subsequent measured performance edits changed only `simpa` to `simpa only` in coefficient hsum and separated-product final combination. Both initial full snapshot/texts remain immutable; final proof line counts18/26 remain unchanged. Each helper still requires its own fresh dedicated audit arranged by parent, not counted as audited by this original-target report.

## Eleven-step checklist

- [x] Step1: full required skills/workflow and five mandatory reference docs, applicable style/naming/profiling references read.
- [x] Step2: substantive24-item audit, including full original have inventory.
- [x] Step2.5: five ACTUAL mathlib search methods, corrected failed query documented, clean bounded generic-route probes.
- [x] Step2.6: every effective original parameter assessed with compiled drop/weakening evidence; literature and inversion done.
- [x] Step2.7: complete measured per-line signature packing tables.
- [x] Step2.8: per-signature inequality occurrence scan.
- [x] Step3: all42 golf rules with concrete result or reasoned n/a.
- [x] Step4: alternative strategy and holistic simplify review; direct inequalities selected.
- [x] Step5a: fresh COMPLETE native diagnostics success, zero errors, retained warnings documented.
- [x] Step5b: actual module build, exact original/actual proof/type/axiom gates, structure/naming/packing/orientation and final profile evidence.
- [x] Step6a: no rename required, no shared queue edit; comments3/3 and docstring preserved, full report delivered.

Source line delta: 980→963 (−17). Original target proof94→19 (−75); new private proof bodies18+26 (44), net audited mathematical proof-body reduction31 lines. All counts retain narrative comments. Original28 remains pending owner publication; this leaf does not increment shared totals or perform Git mutations.

## Final buzz/performance gate

Outcome FIXED. Final frozen source SHA256 `f9ff4b423b085a156e8706bd40b8a8588826394c065e812cea5b800e2313684d`. All compiler/LSP requests drained before the fresh full exact-prefix command:

```text
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/roth-theta-index-det/final-prefix.lean
```

Exit0, raw UTF8 `final-profile.log` (113526904 bytes), exact per-node/root anchors `final-timings.json`; prefix/source binding in `final-profile-manifest.json`. Every preceding source import/declaration/context is retained. Scope is prefix through target and BOTH helpers, not a whole-file or project profile claim. Later index_le_lem6 default-heartbeat profiling issue remains owned by ORIGINAL29. No threshold mask, raised limits or production profiling scaffolding.

| Declaration | Before | Final disjoint total | Final outer-command raw line | Result |
|---|---:|---:|---:|---|
| coeff_det_le_lem6M_aux | 787.562ms | 373.647ms | 853673 | pass |
| index_separated_mul_le_aux | 970.052ms | 733.357ms | 897033 | pass |
| index_det_le | 2083.744ms | 430.371ms | 1014590 | pass |

The public baseline is the initial original theorem; helper before times are the valid intermediate46e49f same-source diagnostic sweep `superseded-46e49f-profile.log`, superseded only as a FINAL gate. Final public+helper combined cost 1537.375ms versus2083.744ms original (−26.2%). Public total430.371ms versus2083.744ms. Thus the improvement includes direct arithmetic and measured simplifier reductions, not just splitting the original proof into renamed wrappers.

All final totals <750ms, so the required ≥750ms same-SHA repeat rule does not trigger. All are also below1000ms budget. Intermediate coeff787.562ms/separated970.052ms triggered investigation, not acceptance: hsum broad simpa386.354ms and final combination291.457ms motivated the two narrow terminal-simp exceptions. Final exact tactic nodes:
- coeff_det_le_lem6M_aux, raw line868195: 21.705ms, `✅️ (simpa only [Finset.sum_const, Finset.card_univ,`.
- coeff_det_le_lem6M_aux, raw line868198: 21.700ms, `✅️ simpa only [Finset.sum_const, Finset.card_univ,`.
- coeff_det_le_lem6M_aux, raw line868201: 21.695ms, `✅️ simpa only [Finset.sum_const, Finset.card_univ,`.
- coeff_det_le_lem6M_aux, raw line868204: 21.677ms, `✅️ simpa only [Finset.sum_const, Finset.card_univ,`.
- index_separated_mul_le_aux, raw line994040: 109.546ms, `✅️ simpa only [lem6Φ, mul_add, Function.comp_def, mul_comm _ (l : ℝ),`.

Disjoint accounting sums only the selected outermost command and associated top-level async proof, addDecl/kernel/compiler and lint jobs. Nested definition.value, macro/omit commands, tactics and child Kernel nodes are not counted again. The raw node lists are retained, including auxiliary addDecl jobs. maxHeartbeats raises:0; maxRecDepth raises:0; no sorry/new axioms/native_decide. Both helpers still await separate fresh audits by owner.

## Terminal handoff

Final source frozen; source-edit authority revoked on this leaf at handoff. No compiler/LSP requests remain in flight. Report and scratch evidence only; no Git/shared-ledger/rename mutations. Owner publication, dedicated18/26-line helper audits, then full project build and separate Roth.LeanEval remain owner gates.


## Final owner-frozen helper batch (supersedes intermediate source above)

Both initially added private helpers received separate fresh dedicated audits. The coefficient
helper audit found `abs_coeff_det_hasseDeriv_le` with the constant degree function sufficient,
compiled its direct specialization at the exact first private contract, and deleted the
single-use wrapper. Its [fresh audit](Theta-coeff_det_le_lem6M_aux-helper.md) checks the independent
first18-line proof and replacement, actual built deletion and trace absence. The uniform
coefficient hypothesis itself supplies nonnegativity of B; no new premise is introduced.

The [remaining separated-product helper audit](Theta-index_separated_mul_le_aux-helper.md)
retains its26-line proof, removes one redundant inner integer ascription, and independently
checks the exact first introduction and actual opaque constant/type/BinderInfo/names/standard
axioms. No additional helper was introduced. The public proof now has24 physical lines,
including all3 protected Step comments (21 code lines), satisfying its ordinary≤30 cap.
Only the module Main results names have the≤15 cap; index_det_le is not one of those names.
Final file943 lines versus original28 baseline980. The initial19-line/two-helper/f9ff4b
measurements above are retained as history and superseded as final-batch evidence here.

Final frozen Theta SHA256:
`c6e59b0ff252c0cdfc0e00070bb7c0c5bea3a53e0786889767f4b1594f5e6ee3`.
Fresh final module build passes. The post-build probe
`/private/tmp/roth-theta-separated-helper/actual-compatibility.lean` and its clean exit0 log
replay the complete immutable original target AND entire original index_le_lem6 caller proofs,
exact old adapters, opaque original/actual values and actual standard axiom sets. Target drops
are exactly DecidableEqτ/δ/hB/hl′/hδ; the caller's entire original telescope has no drops.
Deleted coefficient-helper absence and actual retained-helper contract/axioms pass. Original
Index/Theta namespace blocks are unchanged; the owner block-SHA comparison also distinguishes
one harmless inter-block blank line from proof drift.

Complete unfiltered final native LSP:
`/private/tmp/roth-theta-separated-helper/final-lsp.json`, success=true, partial=false,
timed_out=false, dependencies=[],0errors11warnings. After all normal requests drained,
real global `--profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0` exact-prefix run
exited0: retained helper655.221ms, public742.222ms. Both are<750ms, so no repeat trigger.
Raw UTF8 log115495771bytes, exact disjoint accounting and source binding:
`/private/tmp/roth-theta-separated-helper/final-profile.log`, `final-timings.json`,
`final-profile-manifest.json`. Combined current target+helper1397.443ms versus accepted
original2083.744ms; scope is through public28, not whole Theta. No raised limits, masks,
new axiom, sorry or production profiling scaffolding. The later index_le_lem6 instrumented
heartbeat failure awaits original29. Full project and separate LeanEval owner gates follow.
All dedicated leaves revoked source edits and drained their requests before owner builds.


## Owner cumulative publication gates

After leaf source revocation and drained requests, owner ran full `lake build` (91.138 s),
then separate `lake build Roth.LeanEval` (30.612 s); both exit0. All 17 project/source/pin
hashes remained identical through both commands. Theta SHA256 `c6e59b0ff252c0cdfc0e00070bb7c0c5bea3a53e0786889767f4b1594f5e6ee3`.
Raw logs: `/private/tmp/roth-theta-d28-full.log`, `/private/tmp/roth-theta-d28-leaneval.log`; machine record
`/private/tmp/roth-theta-d28-builds.json`. These completed gates supersede pending owner
entries above. Exact-path staging, commit and successful push publish this checkpoint before
the next original declaration edit. After publication: Theta 28/35, overall 209/264 original
declarations, 9/14 completed files. One retained private separated-product helper26lines, separately freshly audited; the initially added coefficient helper was separately freshly audited and deleted. New helpers and revisits add no original count.
