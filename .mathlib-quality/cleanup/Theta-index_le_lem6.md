# Dedicated audit — `Roth.index_le_lem6` (original 29)

Only the assigned original, its three necessary private extractions, the strict-ratio specialization in its sole routine caller, and this report are in scope. No Git, shared report/rename queue, definition, import, or header metadata changes. New helpers require the owner's **separate fresh audits** after this frozen handoff; this leaf does not count those audits as done.

## Baseline and mathematical understanding

Inherited source SHA256 `c6e59b0ff252c0cdfc0e00070bb7c0c5bea3a53e0786889767f4b1594f5e6ee3`, 943 lines. Same-SHA complete unfiltered native baseline diagnostics `/private/tmp/roth-theta-separated-helper/final-lsp.json`: success true, partial false, timed_out false, no failed dependencies, 0 errors/11 warnings. No duplicate baseline LSP request. The inherited 655.221ms helper/742.222ms public28 trace is **not original 29 performance evidence**. Owner supplied the known real full-trace default-200000-heartbeat failure in old29's broad arithmetic; fresh baseline/final evidence is reported below.

References read: both Lean/mathlib-quality SKILL.md sources; cleanup worker workflow; full golfing-rules, proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates; relevant style/naming/profiling rules. Earlier explicit user preferences remain binding, particularly retaining `hq`. Standing authority implements recommended supported changes without a new user approval flow.

Mathematics: separation supplies one shared l,D,U,V and all of their correlated properties. Nonzero factors and injective maps give a nonzero real determinant. A derivative of total degree ≤l−1≤r_p has weight ≤δ, by multiplying the weak coordinate ratio and summing. Combine the determinant index lower bound with its lΦ upper bound and the unconditional `min_le_sum_max`. The resulting min inequality gives either θ≤2(Φ+δ), or θ²≤4(Φ+δ) since l≤r_p+1 and r_p>10. The inequalities δ≤√δ, the two square-root squares, and nonnegativity finish. All nonlinear arithmetic now has an explicit small hypothesis list; the weighted-degree argument uses direct monotonicity.

Changes: remove approved DecidableEq τ; weaken the coordinate ratio from `<` to `≤` after a full compiled candidate and independent old-theorem/caller recovery; retain every other public binder. Owner explicitly accepted the equality boundary on concrete evidence. The sole caller retains its **entire original strict-ratio type** and specializes by `fun j ↦ (hratio j).le`.

The original small-index signpost cannot describe a removed branch. Its mathematical comparison δ≤√δ is truthfully reanchored in the numeric helper as controlling the linear bound. The `1≤M,0≤Φ` and two-index-bounds signposts remain at their corresponding stages. Public docstring is unchanged. The unconditional min theorem makes the small θr_p≤10 branch unnecessary, rather than hiding that case behind an extra premise.

## Full 24-item audit

| # | Item | Finding/action |
|---|---|---|
| 1 | LINT | Baseline unused hq is explicitly retained by user preference, never artificially used or warning-masked. DecEq removal eliminates its unused class warning. Complete final diagnostics below. |
| 2 | HAVE SCAN | Full original inventory below; single-use aliases removed, genuine mathematical estimates extracted; final hM1 has two uses and lower/upper bounds are normalized before use. |
| 3 | SET_OPTION | No production limit/option; scratch automation uses a smaller local 10000-heartbeat budget. Real traces use the default, no raises/masks. |
| 4 | SIMP SQUEEZE | Final nonterminal bound normalization uses explicit small `simp only` lists; terminal determinant-entry simp remains unsqueezed. The old Φ/α rewrite bookkeeping is eliminated. |
| 5 | NAMING | Existing index_le_lem6 preserves public source terminology and matches no forbidden numeric pattern/abbreviation. New private names describe weight, mapped determinant nonzero, and numerical index bound; all `_aux`. No rename required. |
| 6 | LINE PACKING | Every target signature line, including the correlated existential conclusion, measured below in Unicode codepoints. No dangling conclusion or split binder. |
| 7 | BY PLACEMENT | `:= by` ends the declaration's final signature line. |
| 8 | FORMAT | Two-space proof indentation, four-space signature continuations, no blank proof lines, no semicolon chain/haveI/letI. Exactly one blank between declarations. |
| 9 | COMMENTS | Original positivity and determinant-bound signposts retained/reanchored; removed small-case narrative replaced with its still-used δ≤√δ mathematics, as explained above. |
| 10 | DOCSTRING | Public original description preserved; no docstrings on private helpers. |
| 11 | VISIBILITY | Public wrapper retained per prior preference. Three substantive file-local helpers private; classic import dialect. |
| 12 | STRUCTURE | Ordinary target cap ≤30 (not a module headline); final counts below. Numeric alternative branches ≤10. Existential l and its bounds remain shared, not split into uncorrelated witnesses. |
| 13 | MATHLIB | Five actual search methods plus uncontaminated anonymous compiled automation below. Existing map/rename/square-root/order APIs used directly. No short convenience wrapper introduced. |
| 14 | JUNK DEF | n/a: theorem, no new def/abbrev. α and Φ are local abbreviations, not public definitions. |
| 15 | EXISTS LEMMA | n/a: substantive public bound, not private trivial witness wrapper; keep shared separation witness. |
| 16 | SHOW/CHANGE | Only typed `(show 0<l from hl)` expresses the Nat positivity cast bridge; no redundant tactic-mode show. |
| 17 | PUSH_NEG | Old pushed negation and by_contra small case removed; no deprecated push_neg introduced. |
| 18 | GENERALISE | Every effective old binder has compiled drop/weakening evidence; approved DecEq omission and supported ratio weakening checked with explicit complete old-telescope adapter, names/order/BinderInfo and unchanged result. |
| 19 | INEQUALITY | All comparisons have the smaller side on the left; per-occurrence scan below, no ≥/>. |
| 20 | NORMAL-FORM | Keep RSet membership, natural degrees, real index/Θ and canonical ≤ bound. Weak ratio is exactly the monotonicity premise actually used, with strict original recovered by .le. |
| 21 | SYNTAX-GEN | Retain existing public argument order, hq and shared existential l; no extra bundled structure or equivalence API makes the sole caller simpler. |
| 22 | IMPORT-FANOUT | n/a: no production imports added. |
| 23 | CASTS | Keep genuine ℤ→ℝ and ℕ→ℝ point/degree/index casts, and Fin→ℕ derivative order. α's function ascription fixes the point codomain; l's real type pins a numerical helper metavariable. Redundant old Nat-to-real auxiliary aliases removed. |
| 24 | INSTANCE-NAME | No named instance declaration; anonymous synthetic instance renumbering after DecEq removal is allowed, user-written names and retained class types checked exactly. |

### Every original `have`

The baseline snapshot supplies exact line anchors; the table inventories nested haves as well as outer ones.

| Original name / stage | Decision |
|---|---|
| hrp0 | Positive r_p cast now internal to arbitrary weight helper. |
| hl0, hlR | Redundant hl0 removed; real positivity supplied at numerical call, no named alias. |
| hθ0 | Unneeded after unconditional min bound and square comparison; removed. |
| hδrp | Removed; numeric helper obtains r_p>10 directly from δ≤1 and hrp. |
| hM1 | Kept; used for both Θ nonnegativity terms. |
| hΦ0 | Single-use typed term inlined at numeric call after compiling candidate. |
| hsδ, hsΦ | Moved into numerical stage, retaining δ≤√δ explanation. |
| anonymous θ<δ / small case | Entire unnecessary case removed; unconditional min covers it. |
| hupper | Retained and normalized with map_det, then used terminally (two references). |
| hmapdet | Large duplicate identity eliminated from public proof by direct forward bound normalization; helper's necessary nonzero conversion remains. |
| hFne | Substantive mapped determinant nonzero proof extracted and inlined at lower-bound call. |
| hδ′ | Substantive weight bound extracted; no nested nlinarith remains. |
| hdeg | Degree comparison fed directly by `lia`, cast only at mul monotonicity. |
| hj | Denominator positivity supplied directly by exact_mod_cast. |
| anonymous ratio, hdj | Inlined into mul_le_mul_of_nonneg_left; Nat.cast_nonneg supplied directly. |
| hlower | Retained, normalized by hasseDeriv_map, then used terminally. |
| hmin | Single-use term inlined into final linarith-only certificate. |
| hkey, anonymous copy of hupper | Removed bookkeeping; final scoped certificate directly combines min/lower/upper. |
| anonymous linear θ bound | Moved to numeric helper; small explicit nlinarith-only list. |
| hl′R | Inlined cast at numeric helper call. |
| hrp10 | Numeric helper obtains via div monotonicity, no large polynomial context. |
| hθsq, h1 | Scoped square bound retained in numeric helper, with multiplied l≤r_p+1 certificate. |
| hs0, hs2, hθs | Removed auxiliary sqrt(Φ+δ) and its comparison. |
| hsle, h1, h2, h3 | Replaced by direct square-root-square/nonnegative-product certificate, avoiding a separate sqrt-add lemma. |

## Five actual search methods and automation

Raw native responses and web results: `/private/tmp/roth-theta-lem6/search-results.json`.

| Method | Actual query / result |
|---|---|
| A Lean-Finder | Roth polynomial index bound determinant Lemma 6 weighted degree square root → unrelated Chevalley degree/number bounds, no matching weighted rational-index theorem. |
| B Loogle | `Real.sqrt (_ + _) ≤ Real.sqrt _ + Real.sqrt _` → empty items. This bounded search does not establish absence. |
| C LeanSearch | Roth lemma 6 polynomial index determinant bound → Matrix.det_le, degree_det_X_add_C, coefficient/root bounds; partial determinant estimates, no target conclusion. |
| D local source rg | Full new helper names untruncated (no hits); index/determinant, sqrt/add, le_sqrt, map_det and hasseDeriv_map variants. Existing RingHom.map_det, Real.le_sqrt_self_iff, Real.sq_sqrt and direct order multiplication APIs used. One initial guessed Roth/Weight.lean path was absent; corrected existing-source search logged separately. |
| E local name | sqrt_add_le → empty items with index unavailable, explicitly **not absence evidence**. Existing sqrt-square direct APIs verified by ordinary compiler. |

Auxiliary variants: map_det/map_apply, hasseDeriv_map, rename_injective, map_ne_zero_iff, sqrt square/sqrt-self, degree_eq_sum, div_le_div_iff₀ and mul monotonicity. No compact/discrete/coset/common-equivalent bucket applies. No direct replacement found within these searches. The three helpers carry substantive multi-step content; no 1–3-call wrapper retained. No exhaustive mathematical nonexistence claim.

`automation.lean` uses **exact source prefix BEFORE original 29**, imports no current Theta, and includes only anonymous examples. grind failed; aesop hit the deliberately smaller budget in nested simp; simp_all made no progress; exact? could not close; apply? hit its smaller transform budget without a complete proof. The expected-exit1 log cannot certify axioms or absence. Consecutive prior native multi_attempt stalls were respected; no repeat of that unbounded request. Successful independent proof/value/axiom checks are separate exit0 runs.

Simplification trials are recorded honestly: reverse hasseDeriv_map made no progress; forward hasseDeriv_map plus reverse map_det normalized entries but could not recognize the mapped Matrix.of shape, and the final arithmetic failed. The selected strategy explicitly normalizes RingHom.mapMatrix_apply and Matrix.map/Matrix.of_apply in the upper bound as well, and uses forward hasseDeriv_map in the lower bound, avoiding a fourth helper. Actual compiler results below. Positive positivity and gcongr subgoal probes are included with the corrected independent hq-drop probe.

## Mechanical generalisation, literature, and inversion

All 19 retained effective parameters, plus omitted DecEq, are accounted for. `binder-map.json` records exact scratch ranges; `binder-results.json` classifies errors. Data-drop unknown-name failures are signature-formation/current-proof evidence, **not mathematical counterexamples**. The first large negative batch reached Lean's default maxErrors at the final coefficient-only RSet trial; that exact unvisited tail was rerun independently in `binder-tail.lean`. No error limit was raised. The first standalone hq-positive file missed its τ/Fintype context; corrected positive evidence is separate and is the only accepted positive hq-drop result.

| Binder | Class/use | Compiled candidates and decision |
|---|---|---|
| τ : Type* | variable domain | Drop fails unknown τ with autoImplicit=false; already universe polymorphic. |
| [Fintype τ] | finite structure/card τ in M | Drop and Finite replacement fail required Fintype/card synthesis; retain. |
| [DecidableEq τ] | unused decidability | Full selected theorem without it compiles; approved omission, complete old adapter verifies. |
| δ | real error tolerance | Drop leaves dependent hypotheses/result unknown; retain ℝ because square roots/Θ are real. |
| hδ0 | positive δ | Drop and nonnegative weakening fail present reciprocal/weight/numeric stage; retain. No semantic impossibility inferred. |
| hδ1 | δ<1 | Drop and ≤1 unchanged-proof trial fail current numeric application; retain scoped original premise. |
| r | degree/index weight data | Drop ill-scopes dependent statement; retain Option τ→ℕ. |
| hr0 | all weights positive | Drop/nonnegative weakening fail needed positivity. Some/none partition covers all coordinates; no proper point restriction supports arbitrary derivatives. |
| hrp | lower reciprocal bound | Drop/≤ unchanged-proof trial fail numerical helper; retain. |
| hratio | coordinate ratio | Drop fails; actual independently compiled ≤ candidate succeeds after direct forwarding, approved and applied. Original strict hypothesis recovered by .le, same result. |
| r₁ | uniform degree cap | Drop leaves hr₁/M undefined; retain natural domain. |
| hr₁ | all degree caps | Drop fails index_det_le input; every variable may occur in arbitrary R, no proper coordinate localization. |
| q | denominator data | Drop ill-scopes hq,hh,point,Φ; retain natural domain. |
| hq | positive denominators | Drop compiles in corrected independent positive proof; **retained by explicit user preference**, not artificially used. |
| B | coefficient bound | Drop leaves RSet/M undefined; arbitrary real input already. |
| hB | B≥1 | Drop/0≤B unchanged-proof trial fail one_le_lem6M; preserve scoped public premise. No speculative RSet-derived new API amendment. |
| R | integer polynomial | Drop ill-scopes hR/result; preserve integer-coefficient domain central to separation/index_det_le. |
| hR | RSet membership | Drop and nonzero-only/degree-only/coefficient-only weakenings fail required projections/separation/upper bound. Retain useful bundled API. |
| h | integer rational-point numerators | Drop ill-scopes hh/point; arbitrary point data already. |
| hh | all-coordinate coprimality | Drop fails upper determinant estimate; all coordinates can occur, retain global form. |

Preapply positive weak-ratio evidence: `weak-ratio.log` exit0 (26.464s). `ratio-preapply-compatibility.log` exit0 (40.574s), with exact immutable independent original 29 proof, exact strict→weak entire old-telescope adapter, entire original 30 caller type and full independent caller proof, and proof values via value! true plus standard axioms for all four constants. Owner accepted the supported boundary case before live application. No other public amendment recommended.

Literature: local `.mathlib-quality/references/clean.tex` lines 705–885 states Lemma6 with positive q, strict degree ratios, the shared l bound, separated product upper bound, weighted derivative lower bound and old small-index split. Primary web queries “Roth theorem lemma 6 index polynomial determinant bound delta generalization” and “Roth 1955 rational approximations algebraic numbers lemma 6 index polynomial” found [Roth's original paper](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/EFB89E2873019B246F004FAA06E05A7F/S0025579300000644a.pdf/div-class-title-rational-approximations-to-algebraic-numbers-div.pdf), its [journal record](https://www.cambridge.org/core/journals/mathematika/article/rational-approximations-to-algebraic-numbers/EFB89E2873019B246F004FAA06E05A7F), and [Roth's ICM account](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf). These corroborate the determinant/index setting; no claim of an unrelated literature generalization. The ≤ boundary is supported by our exact compiled derivative-weight proof. No connected math ChatGPT tool is exposed, recorded unavailable rather than searched-and-empty.

Inversion performed: the arithmetic after the min inequality no longer uses R,D,U,V,Θ or M, so the numeric helper is precisely the abstract real inequality. The weighted-degree subproof likewise takes arbitrary d and a weak ratio, independent of l. Nonzero mapping takes arbitrary nonzero separated factors. The public theorem still uses RSet/separation and Θ; further abstracting those away would merely make the caller supply the same domain-specific bounds. No arbitrary public restatement or extra helper recommended.

## Complete 42-rule golf pass

| Rule | Status |
|---|---|
| 1.1 | No by-exact wrapper. |
| 1.2 | No by-rfl proof. |
| 1.3 | Final nonzero equivalence conversion uses rwa. |
| 1.4 | Degree/weight cast and determinant normalization use existing direct APIs; no simp+exact pair retained. |
| 1.5 | No simp followed by redundant rfl. |
| 1.6 | One shared existential constructor ⟨l,hl,hl′,…⟩; no unnecessary constructor chain. |
| 1.7 | Direct lemma applications where closed; apply numeric helper intentionally leaves its min obligation. |
| 1.8 | Old by_contra/pushed-negation small case removed entirely. |
| 1.9 | Weak ratio passed directly, not eta-wrapped; point/function lambdas actually transform inputs. |
| 1.10 | Single-use Φ nonnegative and min aliases inlined; hM1 used twice; normalized bounds retained. |
| 1.11 | No apply-intro chain. |
| 1.12 | No redundant show; positive Nat cast bridge is load-bearing. |
| 1.13 | Shared separation data obtained once, keeping all correlated outputs. |
| 1.14 | Nonzero conversion rewrites grouped where adjacent. |
| 1.15 | Terminal determinant-entry simp remains unsqueezed; no new terminal simp-only. |
| 1.16 | All nonterminal simplification uses explicit forward normalization lists. |
| 1.17 | .le and .trans_lt notation for original strict and reciprocal comparisons. |
| 1.18 | No dollar syntax; grouped multiline theorem arguments retained. |
| 1.19 | No push_neg; old push Not becomes unnecessary. |
| 1.20 | No trivial private existential helper; theorem's witness remains shared. |
| 2.1 | Actual clean whole-goal grind failure recorded. |
| 2.2 | No selected grind with redundant preprocessing. |
| 2.3 | Duplicate mapped identity removed by direct normalization, with failed alternatives retained in scratch logs. |
| 2.4 | n/a: no function-property goal. |
| 2.5 | Actual standalone positivity trial for l's real positivity; explicit cast kept for transparent Nat/ℝ bridge. |
| 2.6 | Actual standalone gcongr multiplication trial; direct mul_le_mul_of_nonneg_left retained to show the exact ratio premise. |
| 2.7 | lia proves degree≤r_p from degree≤l−1 and l≤r_p+1. |
| 2.8 | Actual whole-goal aesop trial hits smaller budget; no claimed success. |
| 2.9 | Concrete reciprocal numerator positivity norm_num; casts via exact_mod_cast. |
| 2.10 | n/a: arbitrary polynomial/theta result is not a closed finite decision problem. |
| 2.11 | n/a: no polynomial denominator identity remains; div order lemmas replace nonlinear arithmetic. |
| 2.12 | n/a: no ring/ring_nf goal remains. |
| 2.13 | n/a: linear versus quadratic alternatives are not symmetric cases. |
| 2.14 | Weight calculation genuinely has termwise bound, sum identity and final comparison; no artificial two-step calc. |
| 2.15 | n/a: branches prove distinct linear/quadratic facts, no duplicate tactic branches. |
| 3.1 | No erw. |
| 3.2 | No legacy continuity/measurability. |
| 3.3 | lia used directly; no new omega. |
| 3.4 | No rfl case followed by redundant substitution. |
| 3.5 | No global simp/grind attribute appropriate for this private quantitative bound. |
| 3.6 | Actual simp_all whole-goal probe makes no progress. |
| 3.7 | No production heartbeat/recursion option; default-heartbeat performance fixed, never masked. |

Step-back/simplify outcome: substantive extraction makes the public theorem an assembly of separation, positivity, two index bounds and one numerical inequality. Direct forward normalization removes repeated mapped-determinant identity without adding a fourth helper. The weak ratio captures the actual mathematical boundary. Existing public wrappers, hq and domains remain protected. No further style/API recommendation pending.

## Eleven-step checklist and scoped handoffs

| Required step | Result |
|---|---|
| 1 references | ✓ read both skills, cleanup workflow and required references |
| 2 full audit | ✓ all 24 concrete items and every original have above |
| 2.5 five-method search | ✓ actual searches, limits/failures reported |
| 2.6 generalisation | ✓ all effective parameters, compiled negative/positive/localization probes, literature/inversion |
| 2.7 packing | ✓ every public signature line measured below |
| 2.8 inequalities | ✓ per-occurrence table below, no reversed notation |
| 3 golf | ✓ all 42 rules carry concrete status |
| 4 step back | ✓ nonlinear context isolated and duplicate public determinant equality removed |
| 5a native LSP | ✓ complete unfiltered final response, 0 errors/10 warnings |
| 5b gates | ✓ concrete module/type/value/axiom/scope gates; real profile evidence below |
| 6a renames | ✓ none required; no shared queue writes |

File-wide header/import/rename-queue changes are outside this leaf. No rename or decomposition deferral. The simplify pass is completed in-thread for the assigned declaration; its concrete map-normalization findings were implemented and compiled. The performance/buzz pass is recorded with real traces below. Owner full `lake build` then **separate** `lake build Roth.LeanEval` remain pending and are not represented as this leaf's executions. Three new helpers still need their separately assigned fresh audits, each from the exact first compiled text already saved.

## Final ordinary verification and baseline trace

On final SHA `08a24ad6a1f91295e80a640d19f67bcff901c1ef5c03a8c185c6ca9c9643a894`:

* `/Users/ramin/.elan/bin/lake build Roth.Theta` — exit0, 38.715792708s, `final-module-build.log`.
* Exact independent original 29 plus **entire original Θ_option_le caller** proof/type/value/BinderInfo and actual standard axioms — exit0, 58.091921333s, `actual-compatibility-final.log`. The immediate preceding verifier's whole immutable original namespace remains byte-identical. The new tail permits only DecEq removal and exact strict→weak hratio forwarding for index_le_lem6. It also verifies the actual proof values of every old/current/recovery constant with value! true, actual three new private helpers and prior separated helper, standard 3 axioms, and no PANIC/error/sorryAx.
* Complete **unfiltered native** live Theta diagnostics — `final-lsp.json`, success true, partial false, timed_out false, failed_dependencies [], **0 errors,10 warnings**. No ordinary request remained when tracing started.

The ten final warnings are: protected header metadata at1; retained hr at93; retained hB/hr at101; retained hB at109; retained hr at129 and252; unused retained hq at546; and the two pending original 30 DecEq warnings at573/576. None was suppressed, renamed to hide, or artificially used. The original 30 removal belongs to its later dedicated leaf; this routine caller's entire old public contract is deliberately retained here.

A fresh exact baseline-prefix trace was actually attempted with `/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/roth-theta-lem6/baseline-prefix.lean`. Raw UTF8 `baseline-profile.log` emits **default 200000-heartbeat** failures at579:6 (`isDefEq`) and566:2 (`tactic execution`). It then stalled during trace finalization; the owning exec session was interrupted/drained with exit130. `baseline-profile-interrupted.json` records this incomplete failed measurement, the exact full baseline/prefix hashes and raw byte count. No successful baseline timing, complete trace, or finite old-target budget pass is claimed. No limits were raised. The selected final trace runs only after that failed process is drained.


## Measured signature packing, inequalities, scope and helper provenance

The complete effective type is printed at `format.width 100` in final successful actual compatibility output; the following covers every physical public target signature line. Next groups keep whole binders or dependent applications, never split a type ascription.

| Signature line | Codepoints | Next group (width) | Arithmetic | Action |
|---|---:|---|---|---|
| 544 | 97 | `(hrp : 10 / δ < r none)` (23) | 97+1+23=121>100 | ok |
| 545 | 82 | `(hr₁ : ∀ j, r j ≤ r₁)` (21) | 82+1+21=104>100 | ok |
| 546 | 85 | `{R : MvPolynomial (Option τ) ℤ}` (31) | 85+1+31=117>100 | ok |
| 547 | 74 | `(hh : ∀ j, IsCoprime (h j) (q j : ℤ))` (37) | 74+1+37=112>100 | ok |
| 548 | 73 | `index (map (Int.castRingHom ℝ) R) (fun j => (h j : ℝ) / q j) r ≤` (64) | 73+1+64=138>100 | ok |
| 549 | 70 | `2 * (lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l +` (54) | 70+1+54=125>100 | ok |
| 550 | 62 | `√(lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l) + √δ) := by` (62) | 62+1+62=125>100 | ok |
| 551 | 72 | proof next | n/a | ok |

| Inequality occurrence | Form | Action |
|---|---|---|
| 544:40 | `<` smaller side left | keep |
| 544:54 | `<` smaller side left | keep |
| 544:92 | `<` smaller side left | keep |
| 545:19 | `<` smaller side left | keep |
| 545:57 | `≤` smaller side left | keep |
| 546:21 | `≤` smaller side left | keep |
| 546:59 | `<` smaller side left | keep |
| 546:82 | `≤` smaller side left | keep |
| 548:52 | `≤` smaller side left | keep |
| 548:60 | `≤` smaller side left | keep |
| 549:70 | `≤` smaller side left | keep |
| Reversed occurrences | No ≥/> in signature/hypotheses (ASCII function arrows excluded) | no rewrite/rename |

| Declaration | Final proof lines | Structural check |
|---|---:|---|
| weight_le_delta_aux | 11 | ≤30; numeric alternative branches ≤9, no long case branch elsewhere |
| mapped_det_ne_zero_aux | 14 | ≤30; numeric alternative branches ≤9, no long case branch elsewhere |
| index_numeric_bound_aux | 15 | ≤30; numeric alternative branches ≤9, no long case branch elsewhere |
| index_le_lem6 | 20 | ≤30; numeric alternative branches ≤9, no long case branch elsewhere |

Original target proof 88→20 lines; entire module 943→934 (-9). The three new helpers total 40 proof lines and remain pending separate fresh audits.

Scope checks (`scope-gates.json`): exact entire prefix before new helpers unchanged; entire suffix byte-identical except the sole caller `.le` application; public docstring byte-identical; no definitions/imports/options or unrelated public types changed. Every scoped Lean line is ≤100 codepoints. All introduced identifiers are confirmed by the successful full module compiler; mapMatrix_apply, Matrix.map and Matrix.of_apply were located in their actual mathlib source before selection.

First compiled helper provenance is immutable and saved before later formatting/comments. `first-manifest.json` supplies full-source hashes, clean numeric compilation and per-declaration successful compilation in the first two-helper source despite a later unrelated numeric error.

| Helper | Exact first text including omission context | SHA256 | Full first snapshot / log |
|---|---|---|---|
| weight_le_delta_aux | `weight_le_delta_aux-FIRST-with-context.lean` | `42fd0fa1a1cc283888bc2ab2302cbd2e3d447305add544f8a2118446a7c44340` | `FIRST-compiled-weight-mapped-full.lean` / `helper-candidate.log` |
| mapped_det_ne_zero_aux | `mapped_det_ne_zero_aux-FIRST-with-context.lean` | `52d001067f8c51f34e14f870145f76fef796676f8957788a239ca36c00cb6104` | `FIRST-compiled-weight-mapped-full.lean` / `helper-candidate.log` |
| index_numeric_bound_aux | `index_numeric_bound_aux-FIRST.lean` | `b0d66a4601abec08b6e80f022298157d65da0dda19a6bc178f83d3a7898569ed` | `FIRST-compiled-numeric-full.lean` / `helper-candidate2.log` |


## Accepted uncontended real profiles / buzz outcome

Both fresh runs use `lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 FILE`, with exact **entire production source prefixes through original 29**, preserving all preceding imports/declarations/context and closing `end Lemma6` then `end Roth`. No import-current-Theta shortcut, declaration mask, raised option or profiling scaffolding in production. Every ordinary/compiler/LSP request and the failed baseline session was drained first; both runs were sequential. These are prefix-only performance results, **not a whole-file/whole-project performance claim**.

Times below sum the outer source command and associated **disjoint top-level async proof/kernel/addDecl/linter jobs**; nested tactic/Meta nodes are not added again. Exact categories, values and raw UTF8 line anchors are in final-timings.json / repeat-timings.json.

| Declaration | First final ms | Repeat ms | First outer/proof anchors | Repeat outer/proof anchors | Budget |
|---|---:|---:|---|---|---|
| index_le_lem6 | **700.891** | **675.629** | 1347627 / 1347706 | 1349189 / 1349268 | both <1000ms |
| weight_le_delta_aux | **194.730** | **217.380** | 1086763 / 1086792 | 1089381 / 1089410 | both <1000ms |
| mapped_det_ne_zero_aux | **668.049** | **733.404** | 1116431 / 1116534 | 1119152 / 1119255 | both <1000ms |
| index_numeric_bound_aux | **941.711** | **972.100** | 1219027 / 1219070 | 1221828 / 1221871 | both <1000ms |

`final-profile.log`: exit0, 157.275365542s wall, 151711548 UTF8 bytes, exact prefix SHA `72580d391fa9d0a13732869ff90dfc9765d44fd2311b23620142d1980adbaa4e`.

`repeat-profile.log`: exit0, 161.538931041s wall, 151661451 UTF8 bytes, exact prefix SHA `72580d391fa9d0a13732869ff90dfc9765d44fd2311b23620142d1980adbaa4e`.

The numeric helper's first 941.711 ms triggered the required >=750ms repeat; repeat 972.100 ms also passes 1000 ms but leaves a narrow margin. The owner will perform that helper's **separate fresh audit first**, before the other two helper audits. Public original 29 itself measured 700.891/675.629 ms. No successful old finite timing is invented from the interrupted baseline; the demonstrated improvement is from default-heartbeat failure to two complete successful real traces.

Buzz outcome for the assigned original: **FIXED**. Default-heartbeat broad arithmetic failure replaced by scoped certificates and substantive helpers; public proof 88→20 lines; no raised limits/masks, no remaining performance failure. Helpers are introduced and measured here, but their independently required fresh audits remain pending owner dispatch.

## Final gate status

| Gate | Result | Actual evidence |
|---|---|---|
| lake_build_file | PASS | final `lake build Roth.Theta` exit 0, 38.715792708 s |
| definition_protected | PASS | exact prefix/suffix scope checks, no def/abbrev/import/header change |
| theorem_statement_protected | PASS for exact approved changes | only public29 DecEq omission and approved hratio <→≤; complete old adapter, names/order/BinderInfo/result checked; old30 entire contract retained |
| structure_gate | PASS | ordinary target20≤30; helpers11/14/15≤30; numeric branches≤9; correlated l remains shared |
| naming_gate | PASS | no forbidden pattern/abbreviation; no rename queued/applied |
| line_packing_gate | PASS | all 8 public signature rows measured, each break >100 for next complete group |
| inequality_orientation_gate | PASS | complete per-occurrence scan, zero reversed inequalities |
| no_unintended_breakage | PASS within leaf | sole direct caller specialization compiled; entire independent original 30 proof/type/value retained; whole Theta module compiled |
| original_and_actual_values_axioms | PASS | immutable independent original 29 and original 30; actual compiled constants and all new private helpers; only propext/Classical.choice/Quot.sound; value! true, no PANIC/error/sorryAx |
| final_live_LSP | PASS | complete unfiltered success, no partial/timeout/dependency failure,0 errors, 10 warnings |
| final_real_profile | PASS | exact entire29 prefix twice exit0, all four targets <1000ms, >=750ms repeat honored |
| owner full build / separate LeanEval | pending owner | deliberately not run or claimed by this leaf |
| three separate fresh helper audits | pending owner | immutable first texts/full sources/hashes saved; numeric helper first |

Overall **original 29 leaf PASS**, with explicitly required downstream owner/helper gates pending. No unapplied public recommendation, rename or decompose flag. Final module 934 lines versus 943 baseline, net−9lines. Source edits are revoked and every compiler/LSP/profile request is drained. Final frozen source SHA256 **`08a24ad6a1f91295e80a640d19f67bcff901c1ef5c03a8c185c6ca9c9643a894`**.


## Final owner-frozen helper batch

The initial original29 leaf state above is superseded by the separately fresh numeric, weight
and mapped-helper audits. Final source SHA256
`47369dc4b524f54d2981a0c23e67786b442f061e86c1ec2f6141d6c46fb62c69`,937lines.
Public29 proof is22physical lines; numeric16 (alternative branches3/10), weight12 (zero2/positive8),
mapped14 (local proof3). No additional helper was introduced. Public API remains exactly
the current approved DecidableEq omission and supported weak coordinate ratio; hq is retained.
The public δ bounds and reciprocal-degree premise remain strict until the separate queued K
revisit; do not infer that private numeric generalisation has already changed them.

Each added private helper received its own fresh dedicated full audit:

- [Numeric bound](Theta-index_numeric_bound_aux-helper.md): removes private δ positivity,
  weakens its upper bound to δ≤1 and degree lower bound to3≤rp; direct order cancellation
  and scoped quadratic estimates. Public29 reconstructs3≤rp from its old premises.
- [Weight bound](Theta-weight_le_delta_aux-helper.md): removes every private weight positivity
  premise, treating rnone=0 separately and deriving positive denominators otherwise.
- [Mapped determinant](Theta-mapped_det_ne_zero_aux-helper.md): same effective signature,
  two measured binder repacks. A compiled two-line-shorter simp variant was rejected after
  an overbudget first sweep, despite a passing repeat. The original explicit14-line transport
  certificate was restored; both fresh final-source sweeps pass. Rejected evidence remains raw
  history under `/private/tmp/roth-mapped-helper/rejected-simp-04171753/`.

Fresh final module build exit0 (41.228s), complete independent compatibility exit0 (57.774s),
and complete unfiltered native LSP success=true/partial=false/timed_out=false/deps=[] with
0errors/10warnings all apply to this exact final SHA. Compatibility SOURCE is
`/private/tmp/roth-mapped-helper/actual-compatibility-final.lean`; the entire accepted weight
compatibility source is its unchanged prefix, including immutable originalIndex+Theta proofs,
exact original29 adapter and ENTIREoriginal30 independent proof/type/adapter. The mapped
FIRST proof/full old λadapter, all actual retained helper/public proof values via value!true,
standard axiom sets, retained names/types/BinderInfo/common positional universes/conclusions
and deleted coefficient-wrapper absence pass. Negative binder/automation probes are not positive
certificates. The weight audit final-chat capacity error occurred only after all report/gate/freeze
artifacts were saved; owner reviewed the complete artifacts, without changing the user model.

REAL exact entire-prefix through29, all ordinary requests drained, same final SHA/prefix
`eee4cecc7c2da79b21374267e46ddda0a774fbe412dcb6b8fa20125adb2879ac`:

|Declaration|First ms|Required repeat ms|
|---|---:|---:|
|index_le_lem6|895.050|854.163|
|weight_le_delta_aux|408.013|361.605|
|mapped_det_ne_zero_aux|707.126|651.477|
|index_numeric_bound_aux|939.576|873.525|

Both runs exit0 and every target is below1000ms; ≥750ms triggers the same-source repeat.
Raw UTF8 logs, disjoint-node timing anchors, manifests, complete LSP and freeze/drain record
are under `/private/tmp/roth-mapped-helper/`. Totals include outer command and disjoint async
proof/kernel/compiler/linter work without nested doublecount. The old baseline's default
200000-heartbeat failures and interrupted trace finalization exit130 remain failure history;
there is no finite successful old timing. No limit raises/masking or whole-file performance claim.

All helper workers are terminal and source edit authority revoked; frozen owner full build
then separate LeanEval and exact-path publication gates follow below. New helpers add zero
original counts; successful checkpoint29 publication reaches210/264,Theta29/35,9/14files.


## Owner cumulative publication gates

After leaf source revocation and drained requests, owner ran full `lake build` (92.063 s),
then separate `lake build Roth.LeanEval` (29.415 s); both exit0. All 17 project/source/pin
hashes remained identical through both commands. Theta SHA256 `47369dc4b524f54d2981a0c23e67786b442f061e86c1ec2f6141d6c46fb62c69`.
Raw logs: `/private/tmp/roth-theta-d29-full.log`, `/private/tmp/roth-theta-d29-leaneval.log`; machine record
`/private/tmp/roth-theta-d29-builds.json`. These completed gates supersede pending owner
entries above. Exact-path staging, commit and successful push publish this checkpoint before
the next original declaration edit. After publication: Theta 29/35, overall 210/264 original
declarations, 9/14 completed files. Three substantive retained private helpers separately freshly audited: numeric16lines (δ≤1,rp≥3, noδ positivity premise), weight12lines (no weight-positivity premise), mapped determinant14lines (same signature). No new public domain or conclusion change.
