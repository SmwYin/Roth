# Fresh introduced-helper6 audit: `Roth.abs_eval_iterated_hasseDeriv_lt_aux`

This report concerns only the introduced private helper, its necessary direct application, and this helper lifecycle. It does not complete original declaration27, MainLemma, Main, the final file budgets, or the required later fresh independent whole-file simplify review. Original progress remains242/264 declarations, MainLemma26/27,10/14 files. No Git, shared progress, original27 report, or sealed predecessor artifact was written.

Entry is the actual first ungolfed707-line source SHA256 `0e1db65fbdf99d91baea2e9371a6c5022d177f1ca84916f55af6af417aab02b6`. The final source is699 lines SHA256 `82ffa78b0eb23b880235b87902fcbb3885b22b625cd96fa077468b122488b384`. Helper25→17 declaration lines,18→12 proof physical lines. The helper accepts `(1 + |α|)^s ≤ β` instead of `< β`; the strict conclusion, binder names/order/BinderInfo/universes, other hypotheses and common evaluation point remain. The caller supplies `hTα.le`. The inner redundant Int ascription was removed. Exact inverse of those two source regions restores all entry bytes (`source-change-binding.json`, `helper-change.diff`).

## Phase0/1 and independent first-draft comprehension

Both skill files, full cleanup/cleanup-all/buzz commands, all required reference documents, full854/112/46-line owner instructions, entire source, module prose and relevant clean.tex mathematical context were read. The full predecessor25539-file/4552463870-byte manifest was independently streamed/read/rehash-checked at entry with zero mismatches. That establishes entry provenance; it does not turn pre-draft compiled outputs into post-draft outputs. Fresh selected source build was therefore run before imported metadata, native and profiles.

The first-draft proof was independently reconstructed **before golf or production edits**. For S=∑r, each Hasse derivative preserves coordinate degree and introduces a coefficient bound2^S. The second derivative has coefficient bound2^S(2^S B). Evaluation contributes(1+|α|)^S after the finite-product identity. S≤s and bases≥1 compare to the supplied power bounds; positivity of B and the strict coefficient threshold supply strictness. This is the final derivative/evaluation stage of clean.tex Lemma9, not a wrapper around the counting/common-witness/index stages.

`independent-original-v4` actually exited0/161.17972875s. It compared the entire effective original TYPE, including written binder names/order/BinderInfo/universe names, and checked distinct genuine original/current proof values, closure and inferred types, standard axioms only, and defaults200000/20000/512. Only compiler-generated binder macro scopes were normalized; all raw ASTs were retained. A recursive TYPE+actual-opaque-VALUE dependency walk denies the original/current private helper and descendants, main_lemma and descendants, and sorryAx. It checked all positive candidates and countercertificates in the same successful run, plus all61 fresh defining-module retained declarations. `independent-original-v4-acceptance.json` records the distinct actual proof-value hashes. The owner independently reviewed this run; no partial marker from a failed run is credited.

## Step2: final full24 audit

| Item | Final status |
|---|---|
| 1 LINT | Fresh full unfiltered MainLemma/Main/Eval native complete, success/nonpartial/nontimeout,0errors; inherited warnings1/4/0 only. No helper warning. |
| 2 HAVE | hdQ2 uses, heval rewrite+terminal2 uses, h2'3 uses. Single-use hcQ/hcQ2/e3 inlined through genuine estimates; redundant hT2pos/e2 staging replaced by early strict h2'. |
| 3 SET_OPTION | None in production helper. Actual default heartbeat/synthesis/depth200000/20000/512 checked in TYPE+VALUE semantic commands. Profiling-only trace scopes are separate exact recoverable fixtures. |
| 4 SIMP | No simp/simp-only sequence to squeeze; numerical proof slots use norm_num, positivity uses existing API. |
| 5 NAMING | Descriptive private unnumbered `_aux`, no forbidden abbreviation/numeric pattern. No new rename; standing five global renames remain queued. |
| 6 LINE PACKING | All five final signature rows measured in codepoints; all `ok`, no wide-hyp escape. Widths96/99/100/84/27. Full tables/reference below. |
| 7 BY | Signature and inner by positions valid; final composed exact term follows substantive bounds. |
| 8 FORMAT | No blank proof lines, haveI/letI, semicolon sequencing or deprecated syntax. Every changed source line≤100 codepoints. |
| 9 COMMENTS | No helper comment; all9 entry standalone comments byte-preserved, including5 in main and all7 genuine-original filewide comments. Exact inverse preserves all prose/unknown metadata. |
| 10 DOCSTRING | None for private helper, correct; none introduced. |
| 11 VISIBILITY | Private. Actual TYPE+opaque-VALUE scan of all457 project-origin declarations, including all5 separate Eval-origin declarations, finds only main_lemma as direct consumer. Defining module, not namespace, selects the inventory. |
| 12 STRUCTURE |12 physical proof lines, no conjunction conclusion, no branches; ordinary≤30 gate. No new helper necessary. Existing long headline main remains original27's repair task. |
| 13 MATHLIB | All five actual methods recorded below. Partial univariate/general coefficient/evaluation matches; no wholesale replacement. Full target-free compiled exact?/automation negative certificate supplements qualified name-index results. |
| 14 JUNK DEF | n/a theorem; no def/abbrev changed. All7 actual non-theorem/data TYPE/VALUE rows exactly unchanged. |
| 15 EXISTS | n/a universal estimate, no trivial existential helper. |
| 16 SHOW | No show/change. |
| 17 PUSH_NEG | None. |
| 18 GENERALISE | Full outer/inner a–e audit and verified stronger hα premise below; old contract recovered by actual current application. |
| 19 INEQUALITY | All7 signature inequalities and2 explicit inner proof bounds already ≤/<. Zero ≥ or > characters in target Lean code; table below. |
| 20 NORMAL-FORM | Preserve β*(β*B)*β, matching the three estimation factors and caller's existing ring normalization. No claim that this coarse numerical bound is optimal. |
| 21 SYNTAX-GEN | Arbitrary finite universe-polymorphic variable type, natural degree/cap including zero, arbitrary multiindices and real α already supported. One weaker power premise verified and applied. |
| 22 IMPORT-FANOUT | No import added; no new classical/typeclass plumbing. |
| 23 CASTS | Genuine Int→Real map/coercion and real base2 retained. Inner `(P.coeff d : ℤ)` removed; exact full effective stronger TYPE checked, not merely inferred from syntax. |
| 24 INSTANCE-NAME | Anonymous Fintype binder retained; no instance declared/named. |

## Step2.5: five actual search methods

[A] Lean-Finder: “absolute value evaluation iterated multivariate Hasse derivatives bounded coefficients coordinate degrees”. Five unrelated Chevalley/degree hits; no matching replacement. Full request/response/receipt saved.

[B] Loogle: `"hasseDeriv", _ ≤ _`; partial univariate `Polynomial.natDegree_hasseDeriv_le`.

[C] LeanSearch: evaluation/coefficient/iterated-Hasse bound query; partial `MvPolynomial.aeval_natDegree_le`, `Polynomial.taylor_coeff`, `Polynomial.natDegree_hasseDeriv_le`, `MvPowerSeries.order_le`, `LaurentSeries.hasseDeriv`.

[D] Actual source rg: Hasse/evaluation/coefficient/norm/ordered-product patterns, project and mathlib scopes, full stdout/stderr retained. Auxiliary variants `hasseDeriv_(le|lt)`, `abs_.*hasse`, `hasse.*abs`, bound/norm suffixes, `abs_eval_le`, product-power and multiplicative-order APIs were searched. Useful project APIs are `Roth.abs_coeff_hasseDeriv_le`, `Roth.abs_eval_le`; useful mathlib APIs preserve degree, convert product-powers, and compare positive products.

[E] Name-pattern native search: `hasseDeriv` limit80 returned actual names but also index:error. Presence is usable; **absence is not credited from this response**. The full target-free complete-command exact? probe failed to solve the goal; grind/simp/aesop/gcongr/positivity/linarith/nlinarith also failed as complete solve probes, with the genuine fallback then checked closed/std3/defaults in an actual exit0 run. Earlier native line-replacement attempts all had continuation syntax errors; apply? produced a sorry trap and is rejected, never a success certificate.

Common-equivalents lookup: no typeclass/canonical named theorem that replaces this combined stage. Concluded: partial matches; keep this genuine stage built on coefficient/evaluation/degree/order APIs. It combines substantially more than1–3 API calls, not a thin wrapper. No ugly cast/typeclass workaround remains, so no new public extraction API is warranted. Full search files and exact commands are in scratch; no indexed-search or literature absence claim is made.

## Step2.6a–e: every outer/inner binding and conclusion

For every row, drop, weaker/strict, pointwise/localized, algebra/typeclass, and conclusion effects were considered. Structural values have no independent propositional hypothesis to delete; ill-formed or caller-unhelpful API restatements are distinguished from verified candidates.

| Binding | Drop/weakening/type audit and actual decision |
|---|---|
| σ:Type* | Already arbitrary universe; Sort* is incompatible with this polynomial API. Preserve actual u_1 and all written binders; no Fin specialization. |
| Fintype σ | Used by sums/products and primitive bounds. Drop leaves the displayed sums without an enumeration instance; Finite requires a chosen-enumeration reformulation, not a silent class deletion. No such new API selected. |
| P:MvPolynomial σ ℤ | Appears in evaluation, degrees and coefficients. Cannot drop while keeping statement. General ring/complex versions need the optional broader Hasse/norm companion APIs already declined. |
| r:σ→ℕ | Appears in coordinate bounds and total cap; zeros permitted. Fractional/real degrees require a different power/comparison API, no current benefit. |
| B:ℝ | Appears in coefficient scale and conclusion; arbitrary positive size. Removing its scale loses the stated mathematical estimate. hc implies nonnegativity, but zero B invalidates strictness. |
| α:ℝ | Arbitrary real, no sign/nonzero/irrationality/algebraicity premise. Negative and zero values included. Function-valued evaluation is a broader companion API, previously declined. |
| β:ℝ | Appears in supplied thresholds and target; positivity follows from h2. No extra positivity hypothesis added. |
| s:ℕ | Arbitrary total cap, including0. Removing changes hs and both powers; no hidden positive-s assumption. |
| hP:∀j degreeOf j P≤rj | Drop countercertificate: X²,r=0,s=0,α=3,β=2,B=1 gives9 not<8 while other hypotheses hold. PASS. No support-only reformulation selected. |
| hB:0<B | Weak0≤B fails: P=0,B=0,s=0,β=2 gives0 not<0, all other hypotheses hold. PASS. Nonzero-B reformulation with hc is merely a less convenient equivalent. |
| hs:∑r≤s | Drop countercertificate X²,r=2,s=0,α=3,β=2,B=1 gives9 not<8; PASS. Already weak. |
| h2:2^s<β | Drop countercertificate double order2 derivative of X⁴ at0:6 not<27/8 forβ=3/2,s=4,r=4,B=1; PASS. Separately weaker≤ candidate genuine proof PASS, but not selected simultaneously with weak hα. |
| hα:(1+abs α)^s<β originally | Drop countercertificate X,α=100,s=1,r=1,β=3,B=1 gives100 not<27; PASS. Individually weaken to≤: genuine polymorphic proof PASS before edit and after; selected. Equality-boundary positive example X,α=2,β=3,s=1,B=1 checked. |
| hc:∀d abs(coeff P d)≤B | Drop countercertificate C100 in empty variables,B=1,s=0,β=2 gives100 not<8; PASS. Support-restricted form is equivalent under B>0 outside support and does not help this caller. |
| i:σ→₀ℕ | Arbitrary order including0; explicit in actual conclusion and both proof APIs. No restricted-support/nonzero hypothesis. |
| k:σ→₀ℕ | Same, independently arbitrary; sequential derivative order preserved. |
| Conclusion | Same strict absolute double-Hasse evaluation bound, same α and β*(β*B)*β. No weaker conclusion. Sharper multinomial/coefficient companions are an optional broader API, explicitly declined; no optimality claim. |

Inner binders: hP's j ranges over everyσ; hs's sum index uses the same Fintype; hc's d ranges over everyσ→₀ℕ; the evaluation lambda has no premise and the same α at every coordinate. hdQ's j is proved from degree monotonicity, not imported from the caller. Both power comparisons require only hs and bases≥1; positivity is proved using abs_nonneg/pow_pos/hB. All inner degree/coefficient comparisons are weak and all typeclasses actually consumed. No inner hidden nonempty/nonzero/positive-degree assumption. The zero-polynomial/empty-variable/zero-cap/negative-α positive example and separate weak-two equality-boundary example also compile and pass the same proof-value guards.

2.6b: all chosen/alternative proofs and every countercertificate have actual whole-run exit0, actual TYPE+opaque VALUE, closed/inferred/standard3/defaults and denied-dependency checks. 2.6c: larger ring/normed-space/function-valued/sharper-Hasse companion changes not selected, preserving explicit prior declines. 2.6d actual three literature queries and exact first3 ranked titles/URLs are listed below; no mathChatGPT tool exists in this tool catalog. 2.6e only the evidenced small-safe hα weakening and redundant Int annotation removal are applied. Weakening both power thresholds is false: empty variables,P=1,B=β=1,s=0 gives1 not<1 (checked countercertificate). The original effective contract is recovered by `audit_migration` using actual current helper plus hα.le; independent proof closure remains separately target-denied.

## Step2.6d: actual literature queries, Top3 each

Raw requests/responses are `literature-query-0/1/2.json`; exact selected hit blocks are `literature-top3-v2.json`. V1's third hit in query1 overincluded later hits; v2 uses title-plus-citation boundaries without changing raw text. These are search ranking observations, not exhaustive coverage or a Lean theorem certificate. Technical mathematics here comes from the checked proof and project clean.tex context; Wikipedia/nLab hits are recorded, not used as proof authority.

1. “Hasse derivative polynomial coefficient binomial bound evaluation multivariate”: [Fast Multivariate Multipoint Evaluation over All Finite Fields](https://doi.org/10.1145/3652025); [ECCC2026/032](https://eccc.weizmann.ac.il/report/2026/032/download); [Polynomial Methods for Grid Covering Problems](https://repository.tudelft.nl/file/File_84835409-4d57-41ea-853e-318cdce06d8b).
2. “Roth theorem auxiliary polynomial derivative coefficient bound”: [An elementary approach to Roth’s theorem](https://aleksa-milojevic.github.io/expository/roth.pdf); [Proof of Roth’s Theorem](https://diposit.ub.edu/bitstreams/8cfc8916-c376-44d7-8822-14f9fed3aa15/download); [Roth’s theorem](https://en.wikipedia.org/wiki/Roth%27s_theorem).
3. “multivariate Hasse Schmidt derivative composition binomial coefficients”: [Algorithmic Aspects thesis](https://www.maths.usyd.edu.au/u/PG/Theses/2012-ivey-law.pdf); [ECCC2026/032](https://eccc.weizmann.ac.il/report/2026/032/download); [Hasse-Schmidt derivative](https://ncatlab.org/nlab/show/Hasse-Schmidt%2Bderivative).

## Fresh generated source/AST binding

`generated-family-source-ast.json` matches32 actual written roots exactly to source declarations and all29 generated names to complete actual TYPE+opaque VALUE pairs. All generated names are absent as explicit source names; actual theorem/data kinds, both full AST hashes and every directed family const dependency are retained. Some simp auxiliaries are unused/inlined; graph connectivity is recorded truthfully, not asserted universally. All61 actual pairs already passed the successful independent kernel/std3/default/closure guards, with59 full rows byte-identical before/after. No fixed suffix cap is used.

Host-only final bookkeeping initially rejected a multiline-universe parsing omission and two invalid graph assumptions: a generated equation theorem can point to its data root, and generated simp auxiliaries need not be connected to the final root proof. The actual facts and rejected assumptions are preserved in `generated-family-preparse-note.txt`. No compiler/native/profile call, source change, altered semantic guard or partial family PASS was credited. The final complete source-absence/full-AST binding check passed. A report insertion assertion also stopped before writing; this final paragraph was then appended explicitly before the final manifest regenerated.

The first independent rehash attempt streamed every manifest entry but then rejected an invalid raw-order requirement on `rg --files`; no partial rehash PASS was credited. That failed walk's raw listing was not saved before rejection and is not reconstructed. `source-list-order-recheck.json/.stdout/.stderr` records a fresh actual recheck: exact same complete file universe, different traversal order. The final second pass repeats every byte read, compares the exact sorted full-path universe, and saves its complete actual raw listing in the receipt. Source, proofs, native results and all timing captures are unchanged.

## Step2.7: measured signature packing

Actual `#check @actualExactName` reference at format.width100 (`actual-check-v2`, exit0/49.800775916s; command macro expands the exact fresh private Name before elaboration):

```lean
@Roth.abs_eval_iterated_hasseDeriv_lt_aux✝ : ∀ {σ : Type u_1} [inst : Fintype σ] {P : MvPolynomial σ ℤ} {r : σ → ℕ}
  {B α β : ℝ} {s : ℕ},
  (∀ (j : σ), degreeOf j P ≤ r j) →
    0 < B →
      ∑ j, r j ≤ s →
        2 ^ s < β →
          (1 + |α|) ^ s ≤ β →
            (∀ (d : σ →₀ ℕ), |↑(P.coeff d)| ≤ B) →
              ∀ (i k : σ →₀ ℕ),
                |(eval fun x => α) ((map (Int.castRingHom ℝ)) ((hasseDeriv i) ((hasseDeriv k) P)))| < β * (β * B) * β
```

The earlier term-macro check instantiated implicit parameters and is retained only as a qualified display run, not this reference or a closed-term certificate. Full effective TYPE/BinderInfo/name/universe semantics are independently checked in the successful semantic fixtures.

### before: every signature line, codepoints

| Signature row | Width | Next complete token width | Arithmetic | Action |
|---|---:|---:|---|---|
| 1 | 73 | 22 | 73 + 1 + 22 = 96 ≤100 | repack |
| 2 | 58 | 30 | 58 + 1 + 30 = 89 ≤100 | repack |
| 3 | 67 | 22 | 67 + 1 + 22 = 90 ≤100 | repack |
| 4 | 51 | 39 | 51 + 1 + 39 = 91 ≤100 | repack |
| 5 | 60 | 100 | 60 + 1 + 100 = 161 >100 | ok |
| 6 | 82 | 21 | 82 + 1 + 21 = 104 >100 | ok |
| 7 | 27 | none | n/a, proof follows | ok |

### after: every signature line, codepoints

| Signature row | Width | Next complete token width | Arithmetic | Action |
|---|---:|---:|---|---|
| 1 | 96 | 11 | 96 + 1 + 11 = 108 >100 | ok |
| 2 | 99 | 22 | 99 + 1 + 22 = 122 >100 | ok |
| 3 | 100 | 102 | 100 + 1 + 102 = 203 >100 | ok |
| 4 | 84 | 21 | 84 + 1 + 21 = 106 >100 | ok |
| 5 | 27 | none | n/a, proof follows | ok |

The full next-token strings and every exact signature line are retained in line-packing-tables.json. The final third line has100 characters before the colon; attaching ` :` would make102, so the colon begins the full long conclusion on the next line. The conclusion and its final `:= by` participate in the arithmetic. No wide-hyp escape is claimed.

## Step2.8: every written inequality occurrence

| Location after | Actual comparison | Orientation/action |
|---|---|---|
| L505 hP, inner j | degreeOf j P ≤ r j | already ≤; keep |
| L505 hB | 0 < B | already <; keep, zero-bound countercertificate |
| L505 hs, inner sum j | ∑j,rj ≤ s | already ≤; keep |
| L506 h2 | 2^s < β | already <; keep |
| L506 hα | (1+abs α)^s ≤ β | generalized strict→weak, already preferred orientation |
| L506 hc, inner d | abs(coeff P d) ≤ B | already ≤; keep |
| L507–508 conclusion | abs(eval doubleHasse) < β*(β*B)*β | same strict conclusion |
| L509 hdQ, inner j | degreeOf j (hasseDeriv k P) ≤ rj | already ≤ |
| L515 h2' | 2^(∑r) < β | already < |

Actual source scan:0 ≥ and0 > in target Lean code; no ge/gt identifier to queue.

## Step 3: all 42 golfing rules

| Rule | Status and evidence |
|---|---|
| 1.1 by exact wrapper | n/a; no standalone wrapper. Final proof has genuine intermediate estimates. |
| 1.2 by rfl | n/a; none. |
| 1.3 rw + exact | Keep `rw ... at heval`: rewrites a hypothesis before a distinct strict comparison, not rw-goal + exact. |
| 1.4 simp + exact → simpa | n/a; no such sequence. |
| 1.5 trailing rfl after simp | n/a; none. |
| 1.6 constructor + exact | n/a; no conjunction/product goal. |
| 1.7 apply + exact | n/a; no such sequence. |
| 1.8 by_contra + push_neg | n/a; direct estimate. |
| 1.9 eta reduction | Degree lambda has a genuine j-dependent `.trans (hP j)`; evaluation lambda is constant, not eta-expanded application. |
| 1.10 inline single-use have | Applied: hcQ/hcQ2/e3 folded into coefficient/evaluation/monotonicity expressions. Keep hdQ (2 uses), heval (rewrite + terminal), h2' (3 uses). |
| 1.11 apply + intro | n/a; none. |
| 1.12 redundant show | n/a; none. |
| 1.13 have + projections → obtain | n/a; no conjunction extraction. |
| 1.14 merge rw | n/a; one rewrite of a hypothesis. |
| 1.15 terminal simp only | n/a; none. |
| 1.16 nonterminal bare simp | n/a; none. |
| 1.17 dot notation | Retained/applied `.trans`, `.trans_lt`; degree and coefficient estimates compose directly. |
| 1.18 `<|` over parentheses | Applied to `heval.trans_lt <| ...`. |
| 1.19 push_neg | n/a; none. |
| 1.20 single-use trivial exists helper | n/a; genuine universal estimate, no existential. |
| 2.1 whole-proof grind | Actual complete-command negative solve probe passed, target module absent; fallback genuine proof closed/std3/defaults. Earlier native line-replacement probe syntax failures are not credited. |
| 2.2 delete before grind | n/a; no grind retained. |
| 2.3 simpa consolidation | n/a; no adjacent simp/exact sequence. |
| 2.4 fun_prop | n/a; no continuity/measurability/differentiability proposition. |
| 2.5 positivity | Retained for three elementary nonnegative-product premises; whole-proof solve probe failed as recorded. |
| 2.6 gcongr | Actual whole-proof complete-command solve probe failed. Keep the shorter explicit product comparison; power thresholds require the two supplied monotonicity steps. |
| 2.7 lia / omega | Removed original real `linarith` base justification in favor of `le_add_of_nonneg_right (abs_nonneg α)`; no remaining Presburger goal or arithmetic tactic to replace. |
| 2.8 aesop | Actual complete-command whole-proof negative probe passed. |
| 2.9 norm_num / norm_cast | Two numerical base proofs use norm_num; redundant inner Int ascription removed and actual full TYPE equality checked. No cast-normalization round trip. |
| 2.10 decide / decide +kernel | n/a; arbitrary-polynomial real inequalities are not a closed decidable numerical proposition. |
| 2.11 field_simp; ring | n/a helper proof has no denominator algebra/normalization goal. Existing caller `ring` remains outside the rewritten helper. |
| 2.12 linear_combination | n/a; exponential/degree/coefficient estimates need multiplicative monotonicity, not a linear identity of supplied equalities. Actual whole-proof linarith/nlinarith negative probes also passed. |
| 2.13 wlog | n/a; i/k symmetric-looking derivatives need no case split and no symmetric case duplication. |
| 2.14 collapse 2-step calc | Applied structurally: original weak-then-strict calc replaced by `heval.trans_lt` and early strict threshold at total degree. |
| 2.15 `<;>` multiple goals | n/a; proof is composed term-mode estimates with individually distinct positivity slots. |
| 3.1 erw → rw | n/a; no erw. |
| 3.2 continuity/measurability → fun_prop | n/a; none. |
| 3.3 omega → lia | n/a; neither retained; see 2.7. |
| 3.4 rcases with rfl | n/a; no substitutions/destructuring. |
| 3.5 register automation lemmas | n/a; one private stage, existing monotonicity APIs suffice; no new automation attribute. |
| 3.6 simp_all over simp_all only | n/a; neither occurs. |
| 3.7 remove maxHeartbeats | n/a; none introduced/present in target; actual 200000/20000/512 verified. |

## Step 4: manual reflection, distinct from independent review

The whole proof cannot be one tested standard tactic in the full target-free context. The stage genuinely combines two coefficient bounds, two degree bounds, evaluation, finite-product conversion, two power comparisons, and strict positive multiplication. The final composed term avoids all single-use intermediate coefficient bounds and the original real-arithmetic automation. Folding hdQ, heval, or h2' would duplicate substantive expressions or obscure the rewrite/strictness step. A different proof using a sharper multinomial estimate would require a new Hasse companion API; that optional expansion remains explicitly declined. No new helper or wrapper is warranted. The weaker evaluation-power premise is actually proved and has a nontrivial equality-boundary example; the independently proved alternative weaker-two premise is not also applied, because weakening both is false.

This reflection is manual self-review. It is not the unavailable Claude-Code `Skill(skill="simplify")` invocation and is not the mandatory future fresh independent whole-file simplify review.

## Step5: actual validation and all seven diff gates

| Validation | Actual result |
|---|---|
| baseline-selected | exit0/196.847298167s, no timeout, source/input immutable, raw UTF8, env stable, drained |
| after-selected | exit0/206.548456709s, no timeout, source/input immutable, raw UTF8, env stable, drained |
| after-full-build | exit0/45.483901750s, no timeout, source/input immutable, raw UTF8, env stable, drained |
| discovery-after | exit0/145.686885792s, no timeout, source/input immutable, raw UTF8, env stable, drained |
| after-semantics-v2 | exit0/192.552061500s, no timeout, source/input immutable, raw UTF8, env stable, drained |
| actual-check-v2 | exit0/49.800775916s, no timeout, source/input immutable, raw UTF8, env stable, drained |

Whole-run seconds above follow the preserved run receipts and include post-wait bookkeeping; each -terminal.json separately retains the authoritative immediately-after-wait exit/timeout/seconds before any group probe, environment resampling or hashing. No wall-clock duration is substituted for the rooted profiler budgets.

Fresh final native requests contain only file_path: full MainLemma/Main/Eval API content and structured results agree; success/nonpartial/nontimeout, no failed dependencies,0 errors, warnings1/4/0. Current per-call source17 pre/post pins match. Request was saved before each call; actual Date.now was sampled immediately after awaited return, and response-save-observed after saving before postpins. Baseline own source pins bracket the whole native series rather than every individual baseline call; that narrower historical qualification is retained. Inherited header and Main hδ/hQ/hc warnings were not silenced or misreported as helper findings.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | PASS | fresh selected+all affected+Eval and full project exit0 |
| definition_protected | PASS | no def/abbrev source change; all7 actual data/non-theorem full TYPE+VALUE rows exact unchanged |
| theorem_statement_protected | PASS, declared item18 exception | checked small hα weakening only; cast TYPE identical; exact original contract recovered; public main full TYPE unchanged |
| structure_gate | PASS helper |12 physical proof lines≤30, no conjunction or branch; no new helper |
| naming_gate | PASS | no forbidden name/new rename; existing five global renames left to owner |
| line_packing_gate | PASS | all5 rows measured, actual explicit #check reference, every final action ok |
| inequality_orientation_gate | PASS | complete occurrence table;0 ≥/> |

Overall: **PASS for the leased helper diff gates**. This does not turn the retained foreign main/group budget failures, long main structure, pending whole-file global scan or later independent whole-file review into a pass.

## Phase6.6 buzz: matched actual rooted profiles

Actual CLI in all four captures: `/Users/ramin/.elan/bin/lake env lean -j1 --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 FILE`. Each whole canonical source is retained; exactly three standalone trace-option insertions recover it byte-for-byte. Complete actual helper and main command payloads, unique exact source markers/spans, actual proof/private Names, all kernel/generated descendants, lint/root events, strict stdout/stderr hashes, input/source17/environment/terminal/PGID receipts are bound. Only whitespace and standalone comments are ignored in payload comparison. Source-unit private Name `_private._stdin.0.Roth.abs_eval_iterated_hasseDeriv_lt_aux` is explicitly distinct from freshly discovered imported `_private.Roth.MainLemma.0.Roth.abs_eval_iterated_hasseDeriv_lt_aux`; actual trace names and complete dynamic family membership crossmatch. All61 corresponding actual opaque values/types passed current semantics. No fixed suffix cap, forced kernel count, Meta time, nested/inclusive wrapper, trailing-end or double count enters budget totals. No separate Compiler.compile event exists in these theorem spans; actual AddDecl/Kernel names are retained and checked.

| Capture | Helper ms | main_lemma ms | Disjoint combined ms | Budget status |
|---|---:|---:|---:|---|
| before-profile-a | 214.922 | 4914.254 | 5129.176 | helper PASS; main/group FAIL |
| before-profile-b | 203.157 | 4899.926 | 5103.083 | helper PASS; main/group FAIL |
| after-profile-a | 143.380 | 4718.066 | 4861.446 | helper PASS; main/group FAIL |
| after-profile-b | 176.046 | 5201.260 | 5377.306 | helper PASS; main/group FAIL |

Every main/group failure remains valid. AfterB main/group is worse than both before samples; it is not discarded, labeled noise, averaged away, or replaced by a third sample. Both helper samples remain below both before samples and below1000ms. The ≥750 consumer triggered the required same-freeze pairs. There was no unchanged third sample. All generated main proof siblings retain exact TYPE+VALUE rows; only helper and root main rows changed.

Changed contribution diagnosis uses uniquely payload-bound complete nested Elab.step source blocks, **diagnosis only**, never added to/subtracted from disjoint root totals:

| Capture | Entire final caller branch ms | Complete exact-helper+ring tactic ms |
|---|---:|---:|
| before-profile-a | 28.968 | 24.905 |
| before-profile-b | 30.018 | 25.665 |
| after-profile-a | 28.251 | 24.174 |
| after-profile-b | 30.629 | 26.391 |

The complete changed caller branch remains≤30.629ms; the main proof root remains4.397–4.875s after, versus4.462–4.580s before. Kernel/lint contributions and all actual roots remain preserved in the reanchor JSONs. Source inverse and59 exact unchanged metadata rows rule out moving work into hidden/generated helpers. The new helper and changed caller stage are within their local budgets; the large main root/group is still a failing preexisting retained consumer requiring original27 repair. External `Roth.roth_of_isIntegral` has inherited qualified before3176.809/5482.437ms; this helper lifecycle did not take an unmatched after timing or claim that external budget passed. Main public TYPE is exact unchanged and fresh Main build/native pass provide the narrow change-regression check. Full actual GLOBAL rows/stages and final file budgets remain mandatory later.

## Phase6.5 simplify and explicit remaining file obligations

Claude-Code-specific `Skill(skill="simplify")` is unavailable in this Codex tool catalog; tool-availability.json records actual names. No invocation is invented. Manual reflection above is separate from independent review. Standing authorization permits adapting that machinery; the owner retains a mandatory NEW fresh independent whole-file simplify reviewer after original27, including this helper, followed by rerunning any changed gates. That pass is **pending**, not replaced by this helper audit, the owner's evidence checks, or self-reflection. No user-input blocker was invented.

Existing owner obligations: finish original27 main decomposition/meaningful stages and budget repair; final full-file structural/global profiles; cumulative wider semantic/build/native gates; five queued global renames in their designated phase; mandatory fresh whole-file independent simplify. No new helper-scope refactoring or rename remains. Previously declined optional Hasse companions, Separation domains/wrappers, Theta optional APIs and common-Q/common-witness conclusions remain preserved.

## Preserved failed evidence and qualifications

- Original independent V1 exit1/86.793558708s and V2 exit1/141.726873083s failed concrete certificate simplifications; V3 exit1/168.429301333s left27/8≤abs(constantCoeff6). Guards rejected the admitted/open certificate. V4 fixed the certificate with standard simplification and passed. No partial semantic markers credited.
- After semantic V1 exit1/178.110599333s failed parsing the saved before-Main Expr repr at `_@`. V2 quotes that exact internal Name component in four occurrences; inverse recovers V1 bytes. It does not rename or normalize written binders. Actual whole V2 exit0 is required and achieved.
- Initial native nine line-replacement automation attempts had continuation syntax errors; apply? produced a sorry warning/empty-goal trap. All success/absence credit is rejected. Repaired full-command target-free eight negative solve probes plus genuine fallback passed exit0/69.622292333s. Candidate genuine shortened proof passed exit0/81.119125667s before edit.
- Native name index:error qualifies absence claims; full raw saved. Literature Top3 extraction V1 overincluded later query1 hits; V2 preserves raw content and exact first3 title boundaries.
- First display check exited0 but term-macro implicit instantiation made it unsuitable as the full packing reference. Correct command-macro explicit check V2 passed; full TYPE semantics were independently closed throughout.
- Initial runner argparse misuse failed before compiler launch. Reanchor V1 incorrectly included following Meta payload; repaired V2 uses actual trace boundaries, preserving failure note and all raws. Preparation-template leading-newline assertion failed before launch and was fixed without proof change.
- Initial administrative broad AGENTS rg was stopped via its exact unified session34178, exit130; its PGID was not recorded and is not reconstructed. Initial and preseal sandbox ps PermissionErrors are retained with UNKNOWN inventory status; narrow authorized read-only observations succeeded, including all57 recorded groups absent and no exact task/printenv argv rows. No automatic-approval review rejection occurred. All compiler/profile/env subprocesses in this lifecycle have actual tracked PID/PGID and terminal-first records. Unknown predecessor metadata/oldenv history remains qualified, never retroactively repaired.

## Actual input closure and release conditions

source-change-binding/input-closure-comparison and final manifest cover actual source17, before/after saved project104/root8 outputs, all14 actual setup/importArts unions including Eval, fresh package12202 and pinned core12592 availability entries, all4 actual executable paths/bytes and Lake-environment resolution, frozen and actual raw environments, exact CLI/scaffolds/commands/failed inputs/native full APIs, every scratch artifact and read instruction/reference.24782 external package/core artifact hashes and all4 executable hashes match the independently rehashed entry bytes. Availability is an explicit superset, **not an exact runtime-loaded closure**. Original pre-draft project-cache status is not reused as post-draft proof; own before and after builds/snapshots provide the actual112 outputs. All unknown historical timing/process states stay qualified.

Final `manifest.json`, `second-rehash.json`, `final-drain-owned-process-inventory.json` and `final-seal.json` are authoritative for actual complete streamed rehash counts, binary exceptions, fresh owned process absence and all seven END releases. Missing/failing seal means no release or lifecycle completion is claimed. The self-referential receipts are explicitly excluded from the manifest; the seal hashes those receipts and the report. No original27 sealed artifact was mutated.

## Step6b Result and all11 phase checks

Before25 declaration/18 proof lines; after17 declaration/12 proof lines; saved8 declaration/6 proof lines. Five audit issue classes found/fixed: underpacking, single-use bound staging, redundant Int annotation, unnecessary real-arithmetic base automation, and unnecessarily strict evaluation-power premise. No new helper or rename. Applied golfing rules1.10/1.17/1.18/2.7/2.9/2.14; other42 statuses and actual probes above. Gates: PASS helper-local seven gates; valid foreign main/group performance failures retained. Renames queued by this worker: none; owner's existing five unchanged. Comments: all9 entry/all7 genuine-original filewide preserved,5 main, no helper comments/docstring. Refactoring needed in helper scope: none. File/original27 obligations explicitly pending above.

| Required phase check | Status |
|---|---|
| Step1 full references | ✓ read full |
| Step2 full24 audit | ✓ final24 above, entry audit retained |
| Step2.5 five actual search methods | ✓ with name-index/absence qualification and compiled negative certificate |
| Step2.6 full a–e generalization | ✓ all outer/inner/conclusion bindings, candidates/countercertificates/literature |
| Step2.7 full line-packing table | ✓ all before/after rows, actual explicit reference |
| Step2.8 inequality scan | ✓ every occurrence;0 ≥/> |
| Step3 every42 golf rules | ✓ status/reason each |
| Step4 reflection | ✓ manual, distinct from independent review |
| Step5a native | ✓ fresh full unfiltered ML/Main/Eval complete, no errors; inherited warnings qualified |
| Step5b seven diff gates/Overall | ✓ helper-local PASS, foreign/file budgets not laundered |
| Step6a rename sidecar | ✓ n/a no new rename; no shared sidecar write |
