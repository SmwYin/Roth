# Roth.Θ_nonneg — full mathlibable assessment

**Verdict: NO-mathlib-has-it.** Re-aiming the accepted parent `Roth.Θ` at its exact existing counterpart `SupSet.sSup` finds `Real.sSup_nonneg`. Its premise is independently proved by expanding the pointwise index into a real infimum of sums of nonnegative natural ratios. Neither boundedness nor nonemptiness nor `1 ≤ B` is needed. This is an independently checked parent-law hit, not an inherited verdict from the project lemma `index_nonneg`.

## Phase 0 — Doctor

Canonical188 is the public theorem at `Roth/Theta.lean:107`; [canonical entry](../evidence/Roth.Θ_nonneg/canonical-target.json), [entire Theta module](../evidence/Roth.Θ_nonneg/Theta.lean.txt), [Index](../evidence/Roth.Θ_nonneg/Index.lean.txt), [Box](../evidence/Roth.Θ_nonneg/Box.lean.txt). Theta defines the bounded polynomial family, its index image and supremum, then proves Lemmas5–7. The complete declaring module and the sole actual consuming declaration `index_le_lem6` were read, including its determinant and numeric helper context.

The shared [baseline build](../evidence/Roth.Θ_nonneg/baseline-build.txt) exited0 after2467 jobs without warnings. Fresh verification matches all17 production source/pin SHA256s in the [baseline manifest](../evidence/Roth.Θ_nonneg/input-manifest.json): [fresh hashes](../evidence/Roth.Θ_nonneg/source-hashes.json). Production sources, pins and Git are unchanged.

Fresh [original exact source](../evidence/Roth.Θ_nonneg/theta-nonneg188-original-executed.lean.txt) and [complete native receipt](../evidence/Roth.Θ_nonneg/theta-nonneg188-original-receipt.json) show the complete type/body, standard axioms, no elision and no errors/warnings. [Standalone audit source](../evidence/Roth.Θ_nonneg/theta-nonneg188-audit-executed.lean.txt) enumerates the canonical293 names in exact order, including private names. Runtime requested/unique/present/value counts are all293; one direct kernel-value consumer and zero direct type consumers. Required target information is scoped to the original native region15; subsequent project/caller info is scoped to343/359. Historical diagnostics do not substitute for new proof information.

## Phase 1 — Comprehend

Full native type:

```lean
Roth.Θ_nonneg.{u_1} : ∀ {σ : Type u_1} [inst : Fintype σ]
  {B : ℝ} (q : σ → ℕ) {r : σ → ℕ}, 0 ≤ Roth.Θ B q r
```

The supremum of the weighted indices of admissible integer polynomials at the specified rational points is nonnegative. Each weighted Taylor-support index is nonnegative because it is the real infimum of finite sums of natural-number ratios. Real infimum at empty support is0; real supremum at empty or unbounded index family is also0. Thus the statement holds for every real coefficient bound, every natural denominator and weight vector, and an empty variable type.

σ is an arbitrary-universe variable type; Fintype supplies the global finite sum in the unchanged index definition. B bounds integer coefficients, q specifies rational denominators, r supplies reciprocal weights. There are no explicit proof hypotheses, no DecidableEq premise, no positive denominator/weight premise and no nonempty family premise. The project dependencies are Θ, indexSet, index and weight; the original body additionally invokes project `index_nonneg`. The substantive arithmetic premise and the outer supremum law must be assessed separately.

## Phase 2 — Preliminary checks

**BIG** under the command's explicit main-result criterion: listed jointly with the upper bound in the module's main-results overview. Its mathematical content is elementary; the exhaustive protocol still runs in full. Phase2b is **n/a — theorem**, not a one-line definition or exemption case. The original proof has three substantive tactic lines.

## Phase 3 — Exhaustive literature

[Exact general/nLab requests and response digests](../evidence/Roth.Θ_nonneg/web0-metadata.json), [nCatLab/Stacks/MO/arXiv requests and digests](../evidence/Roth.Θ_nonneg/web4-metadata.json), [direct primary access](../evidence/Roth.Θ_nonneg/web-direct-metadata.json). Only exact requests, response SHA256/bytes/status, locators and original concise summaries are archived; no full web article or search-result bodies are persisted. [Local manuscript search](../evidence/Roth.Θ_nonneg/local-literature.json), [input hash](../evidence/Roth.Θ_nonneg/local-literature-input.json), [excerpt](../evidence/Roth.Θ_nonneg/clean-excerpt.tex.txt).

| Named channel | Actual query / locator | Finding and limits |
|---|---|---|
| General specific | `Roth theta supremum index polynomials nonnegative` | No exact independent theorem isolated by this spelling; local source supplies the exact Θ notation. No absence inference. |
| General standard | `supremum set nonnegative real numbers least upper bound` | [Hunter, An Introduction to Real Analysis](https://www.math.ucdavis.edu/~hunter/m125a/intro_analysis.pdf), Definition1.3 and Theorem1.7, pp1–2, gives the real least-upper-bound convention for nonempty bounded sets. Nonnegativity is an elementary consequence of the upper-bound property. |
| General aliases | `least upper bound nonnegative subset empty supremum convention` | Distinguishes ordinary real sup existence from extended-real empty sup=−∞. The current empty/unbounded real default0 is mathlib's totalization, not a universal literature convention. |
| ChatGPT mathematical MCP | Standard form, generality, historical evolution | n/a: ask_chatgpt_math unavailable. No fabricated consultation. |
| Local clean.tex | `Theta|Θ|0.*\\Theta|supremum|well-defined|nonnegative` | §5 lines645–668 defines Θ with positive natural r,q and B≥1, and states0≤Θ≤m. Source uses constant1 for nonemptiness and Taylor bounds for boundedness. The Lean lower bound alone needs neither. |
| nLab | `site:ncatlab.org/nlab supremum least upper bound` | [Join](https://ncatlab.org/nlab/show/join), Definition, gives the poset least-upper-bound universal property. Search-index content inspected; direct fetch failed unsupported application/xhtml+xml. |
| nCatLab explicit namespace | `site:ncatlab.org/ncatlab supremum least upper bound` | Returned nLab material, including order/one-sided-real context, rather than an exact /ncatlab namespace result. No higher categorical replacement inferred. |
| Stacks | `site:stacks.math.columbia.edu supremum ordered set` | [Tag05N1, §3.4 Ordinals](https://stacks.math.columbia.edu/tag/05N1) defines ordinal supremum as union; directly inspected. Adjacent order theory, not this real nonnegativity theorem. |
| MathOverflow | `site:mathoverflow.net supremum empty set real numbers` | [Supremum over all Hilbert spaces](https://mathoverflow.net/questions/375759/can-we-take-a-supremum-over-all-hilbert-spaces) discusses nonempty bounded real supremum existence; [vacuous entities](https://mathoverflow.net/questions/45951/interesting-examples-of-vacuous-void-entities/45967) discusses empty sup as initial object. Indexed results inspected; no project-specific bound claimed. |
| Recent arXiv | `site:arxiv.org after:2021-10-27 supremum nonnegative real numbers lattice` | Five-year window2021-10-27 through current2026-10-27. [Kleinbock–Rao2210.09299](https://arxiv.org/abs/2210.09299), submitted2022-10-17/revised2023-08-31, concerns supremum norms and Diophantine approximation, not the target. Abstract directly inspected. Returned2105/2108 hits precede the window;2609 Ehrhart positivity is a different object. No recent novelty inference. |
| Direct primary access | Hunter PDF; nLab join; Stacks05N1; arXiv2210.09299 | Hunter, Stacks and arXiv opened; nLab XHTML access limitation preserved. |

The concept is **nonnegativity of the supremum of a nonnegative real family**, abstractly a lower-bound consequence of supremum membership domination. The manuscript's polynomial realization is specialized; the standard real theorem assumes nonempty bounded inputs for an actual least upper bound. Mathlib's totalization extends the nonnegative conclusion to empty/unbounded inputs. Replacing this by an arbitrary complete lattice law while retaining the literal number0 would require an appropriate zero/bottom relationship; it is not an unqualified scalar generalization.

## Phase 4a — Parameter and hypothesis analysis

| Parameter / premise | Original role | Expanded order form and verified scope |
|---|---|---|
| σ : Type u | variables | Generic law accepts any set of reals; family law accepts independent A:Type u and H:Type v. No variable type at all is needed for the set law. |
| Fintype σ | global sum in unchanged index parent | Required by the current parent interface. No unverified removal from that exact parent signature is claimed. Generic real-set/family laws have no finiteness typeclass. |
| B : ℝ | coefficient bound | Only selects a subset. No `1 ≤ B`, nonnegative B or admissible member witness needed. All B are retained by the actual replacement. |
| q : σ→ℕ | rational denominator | Only selects the points. Zero denominator is permitted by total real division; no q>0 is added. Generic f is arbitrary. |
| r : σ→ℕ | nonnegative reciprocal weights | Naturality ensures every ratio nonnegative, including r=0. Expanded law needs only the pointwise nonnegative real value premise. The pointwise nonnegative-support proof need not hold for signed weights; no signed-weight Θ redefinition is assessed. |
| ℝ result and0 | conditional real supremum with default0 | Generic law covers any real set. Empty/unbounded cases use actual mathlib fallback0, not an invented CompleteLattice ℝ instance. |
| Further hypotheses | none | No boundedness, nonemptiness, positive weights, R≠0 or coprimality is needed by the outer nonnegative law. Those predicates only define the selected family. |

## Phase 4b — Generality verdict

For the unchanged parent, **MAXIMALLY GENERAL**: no proof hypothesis remains to remove and no mechanical deletion of Fintype is asserted. In expanded representation, the independently compiled `law` and `family` widen from polynomial indices to arbitrary real sets/families with pointwise nonnegative values. This general form already exists as `Real.sSup_nonneg`; it is not a new YES-generalise-first opportunity. The alternative witness form `Real.sSup_nonneg'` needs one nonnegative member, but requires a witness and does not cover an empty family by itself. The universal and existential premises are incomparable on arbitrary sets: the universal premise holds vacuously for the empty set, while a set containing both negative and nonnegative values satisfies only the existential premise. Choosing the universal-premise form preserves the no-`1 ≤ B` target uniformly.

[Isolated exact source](../evidence/Roth.Θ_nonneg/theta-nonneg188-isolated-executed.lean.txt) and [raw clean success](../evidence/Roth.Θ_nonneg/theta-nonneg188-isolated-receipt.json) actually compile arbitrary universes/families, both premise shapes, empty/unbounded default0 and the negative-singleton false-generalization guard. No weakening is justified merely by visual inspection.

## Phase 4c — Nine modern-idiom checks

| # | Question | Answer / concrete consequence |
|---|---|---|
|1| Preambles to typeclasses | No new bundled preamble. Existing SupSet/conditional-order infrastructure already expresses the parent; no custom NonnegativeTheta class is warranted. |
|2| Sequences/metrics to filters | No topology or convergence in this scalar order proof. |
|3| Construction to universal property | Yes: upper-bound membership gives nonnegativity on the actual-sup branch. Existing Real.sSup_nonneg handles the default branches; no new universal-property class is needed. |
|4| Closure set to bundled substructure | No closure property is used. Arbitrary Set ℝ is the appropriate input; forcing a subsemiring would add irrelevant assumptions. |
|5| Field/vector-space weakening | The outer argument does not use polynomial coefficients or field arithmetic. Generic set/family law removes those inputs, already in mathlib. Ratios and support weights remain separate arithmetic normalization. |
|6| Higher category | No useful higher-category content. Poset-colimit language does not supply the real fallback convention. |
|7| Concrete index to ordered structure | Only real value-order is used; generic variables/families compile. A law over arbitrary conditional complete orders needs an explicit fallback/lower-bound condition and is not asserted here. |
|8| Concrete-via-abstract diagnostic | Fires: original proof body has zero occurrences of Θ after its statement, and zero occurrences of indexSet or weight. It applies Real.sSup_nonneg, unpacks membership, and uses pointwise nonnegativity. The abstract law is exactly the found mathlib law. |
|9| False-generalization guard | Keep nonnegative member values, empty/unbounded fallback0, and all natural zero denominators. `sSup {-1}=-1` disproves unconditional nonnegativity; named signed_guard compiles. Sup∅=−∞ in EReal would change the target. Arbitrary SupSet alone supplies no order law. |

Modern idiom available: **yes, already implemented**. Use the real-set law with membership transport or the compiled image2 family form. This separates the only arithmetic obligation from the supremum operation and allows arbitrary admissibility predicates without adding new upstream API. Cost is cheap at the outer law, moderate only if migrating all parent representations; cost does not determine the verdict.

## Phase 4.5 — Infrastructure risks

All six rows are **n/a — theorem**: typeclass diamonds, reducibility leaks, noncanonical unfolding, instance priorities, universe infrastructure and coercion ambiguity. The declaration proves Prop and installs no data/instances/coercions. Parent-definition risks are distinct from this theorem; no new Real complete-lattice instance is proposed.

## Phase 4.6 — Five proof-strategy checks

| # | Check | Assessment |
|---|---|---|
|1| ε–δ versus filters | n/a: no topology. |
|2| Elements versus algebraic inclusions | No ideal/submodule/subring argument. Pointwise family nonnegativity is exactly the existing law's premise. |
|3| Sequences versus nets | n/a: no limiting family. |
|4| Explicit construction versus universal property | Existing nonnegativity supremum law packages the conditional universal-property argument and totalized cases. |
|5| Missing helper API | None for the outer supremum. Real.sInf_nonneg, Finset.sum_nonneg, div_nonneg and Nat.cast_nonneg independently discharge the pointwise premise; no new polynomial theorem is needed. |

Current strategy: **MATHLIB-IDIOMATIC**. The original body already uses the correct outer law. Expanding pointwise arithmetic in the verification is for independence, not a recommended repeated golfing change. No missing API ticket is established.

## Phase 5 — Five actual methods × three forms

[Complete exact formal requests/receipts](../evidence/Roth.Θ_nonneg/formal-search.json) record12 calls: Finder, Loogle, LeanSearch and local for each of current, literature and abstract form. The fifth method consists of pinned [current rg](../evidence/Roth.Θ_nonneg/rg-current.json), [literature rg](../evidence/Roth.Θ_nonneg/rg-literature.json), [abstract rg](../evidence/Roth.Θ_nonneg/rg-abstract.json). [Pinned source hashes](../evidence/Roth.Θ_nonneg/mathlib-inputs.json) and [real order source](../evidence/Roth.Θ_nonneg/mathlib-Basic.lean.txt) anchor candidates.

| Method | Current polynomial Θ | Literature real nonnegative sup | Abstract pointwise family |
|---|---|---|---|
| Finder | Roth additive-combinatorics hits; rejected as different theorem | Real.sSup_nonneg, Real.sSup_nonneg', empty law | Real.iSup_nonneg, Real.sSup_nonneg, NNReal coercion neighbors |
| Loogle | Both exact nonnegative supremum laws | Exact universal-premise Real.sSup_nonneg | Exact Real.sSup_nonneg |
| LeanSearch | Real.sSup_nonneg and indexed variants | Both premise shapes and sSup_def | Witness and universal laws |
| rg | Target/index_nonneg and existing real law | Nonnegative/default0 laws at pinned source | Set.forall_mem_image2 and conditional bound transport |
| local | Both exact sSup_nonneg names | Real.sSup variants | Witness law |

All12 calls returned isError=false. Local index is unavailable, but source-backed positive names returned; no absence inference is made. Remote revisions show old module paths `Mathlib.Data.Real.Archimedean`; the pinned path is `Mathlib/Algebra/Order/Archimedean/Real/Basic.lean`.

Positive signatures/proofs independently checked in the isolated native source:

- `Real.sSup_nonneg` (Basic:288): `(∀x∈s,0≤x) → 0≤sSup s`. This is the exact re-aimed law.
- `Real.sSup_nonneg'` (Basic:267): `(∃x∈s,0≤x) → 0≤sSup s`. Weaker value premise but explicit witness, unsuitable alone for all empty families.
- `Real.sSup_empty`, `Real.sSup_of_not_bddAbove`: fallback0; both compiled as equality statements.
- `Set.forall_mem_image2.mpr`: transports a two-argument family premise; the checked family proof is two existing calls.
- `Real.sInf_nonneg`: independent pointwise support-infimum engine. Finset.sum_nonneg/div_nonneg/Nat.cast_nonneg supply the nonnegative ratios.

Conclusion: **found in mathlib as Real.sSup_nonneg on the exact existing sSup parent**, with the project arithmetic premise separately verified. No global nonexistence claim is involved.

## Phase 5.5 — Three statement-shape checks

Normal forms: original `0≤Θ B q r`; `0≤sSup s` under a membership premise; image2-family form under a two-argument premise; existential nonnegative-member form. The canonical reusable outer statement is existing `Real.sSup_nonneg`. Parent unfolding sends Θ directly to `SupSet.sSup (indexSet...)`; no nondefinitional bridge is hidden for this outer constructor. RHS orientation for iff rewriting is n/a: this is an inequality. Parent equality would put existing sSup on the RHS.

Syntactic generality: both universal and existential premise shapes actually compile. Choose universal membership nonnegativity for this target because no member exists when B<1, and no extra B premise should be added. The image2 variant supplies pointwise data before quantifier transport and is useful after parent-family normalization.

Superfluous-argument audit: σ/Fintype/B/q/r all occur through the unchanged parent interface. No declaration hypothesis can be dropped; DecidableEq is already omitted. The expanded abstract law removes polynomial parameters by changing the subject, not by silently weakening an unchanged Θ signature. No R≠0 or coprimality premise enters the independent pointwise proof. Overall: original convenience statement is well shaped locally; upstream **RESTATE to the already existing real-set law**.

## Phase 6.0 — Complete caller and inline audit

Fresh lexical [rg](../evidence/Roth.Θ_nonneg/callers-rg.json) and tracked [git grep](../evidence/Roth.Θ_nonneg/callers-git.json) agree: docstring33, declaration107, and a single source application line583 containing **two occurrences**, both in `Roth.index_le_lem6`. [Structured plan](../evidence/Roth.Θ_nonneg/callers.json), [root git receipt](../evidence/Roth.Θ_nonneg/theta-nonneg188-git-callers.json). Searches cover Roth/ and Roth.lean with --no-ignore, cross-checked against the canonical source inventory. Distinct actual source caller count1; external-to-module count0. This is not dead code and is not tagged simp. Kernel-value audit independently finds only `Roth.index_le_lem6`; no direct type consumer. Source/direct-consumer counts are not an opaque or transitive dependency closure.

The caller supplies `(add_nonneg (Θ_nonneg _) (Θ_nonneg _)) hδ1 hrp` to the private numeric estimate, proving both summands of Φ nonnegative. Refactor both sites to Real.sSup_nonneg with the independent pointwise premise; preserve the determinant lower/upper bounds, the positive-l witness and the numeric inequality. No other explicit caller needs refactoring. The docstring overview should name the underlying direct real law if the local wrapper is removed.

[Inline audit](../evidence/Roth.Θ_nonneg/inline.json) finds the target and its two calls, plus the separate upper-bound statement and explicit real supremum invocation; it does not reveal an independent duplicate proof of Θ nonnegativity elsewhere. This is a source search observation, not a global hidden dependency claim.

## Phase 6 — Actual composition experiments and re-aim

Attempt1, original proof: `Real.sSup_nonneg` plus membership elimination plus **project** `index_nonneg`. It is correct local code, but project index_nonneg is not a mathlib building block. Its accepted138 report was read: it independently re-aimed at infDegree/Finset.le_inf_iff with an all-P/all-r projection bridge. That accepted verdict alone does not settle this supremum property.

Attempt2, freshly independent premise: [project exact source](../evidence/Roth.Θ_nonneg/theta-nonneg188-project-executed.lean.txt), [complete native success](../evidence/Roth.Θ_nonneg/theta-nonneg188-project-receipt.json). `ThetaNonneg188.pointwise` unfolds real support infimum, destructures its image membership, and proves the weight sum nonnegative using Finset.sum_nonneg, div_nonneg and Nat.cast_nonneg. It invokes neither index_nonneg nor Θ_nonneg nor any downstream law. It handles every P, α and r, including zero polynomial/zero weights. `replacement` then applies Real.sSup_nonneg and destructures indexSet membership. The fresh region contains no reference to either target nonnegativity theorem. The outer Θ-to-sSup bridge is definitional, witnessed by the successful application without rewriting and the separate explicit exact_sup rfl check. Expanded arithmetic and image elimination are explicit normalization work; **no strict ≤3-existing-call old-form term is claimed**.

Attempt3, isolated re-aim: `law hs := Real.sSup_nonneg hs` is one existing mathlib call on arbitrary Set ℝ; `family` uses two calls with Set.forall_mem_image2.mpr. No Roth imports are present and #check_failure guards the absent target. Both laws plus witness/empty/unbounded/negative guards compile with standard axioms. This is the deciding existing parent-law hit under ModeB's explicit re-aim rule. It is not merely a closing simp[defs] composition, which would need Phase6b's BORDERLINE treatment.

Attempt4, complete actual caller: [exact replay](../evidence/Roth.Θ_nonneg/theta-nonneg188-callers-executed.lean.txt), [complete native success](../evidence/Roth.Θ_nonneg/theta-nonneg188-callers-receipt.json). The full original `index_le_lem6` is renamed `Roth.caller`, its two target calls use the independently proved replacement, and three private helpers are accessed through term elaborators `mapped188`, `weight188`, `numeric188` using Lean.mkPrivateNameCore Roth.Theta. Those elaborators return the already existing constants with fresh universe metavariables and introduce no axiom; every other mathematical proof step is retained. The replay uses no direct Θ_nonneg application. Both replacement and full caller print only standard axioms. Imported helper proofs retain their original dependencies; this is a direct-call refactor experiment, not an opaque-kernel closure rewrite.

All five accepted native sets are complete successes, disk partial=false where applicable; no errors, warnings, sorryAx, unsafe/native_decide or raised limits. **No rejected native attempts.** Preparation-only files are distinguished from exact executed archives; the isolated anonymous false guard was given the name signed_guard for its axiom print. The scratch187 zero-member extension is not used to prove the present target, avoiding circularity.

## Phase 7 — Verdict and actionable plan

**NO-mathlib-has-it**, citing `Real.sSup_nonneg` on the already existing exact parent `SupSet.sSup`. The compiled one-call generic specialization is:

```lean
example {s : Set ℝ} (hs : ∀ x ∈ s, 0 ≤ x) : 0 ≤ sSup s := Real.sSup_nonneg hs
```

Its application to the actual project family is independently native-verified, including the expanded pointwise arithmetic. A fresh explicit parent [rfl bridge source](../evidence/Roth.Θ_nonneg/theta-nonneg188-bridge-executed.lean.txt) and [clean receipt](../evidence/Roth.Θ_nonneg/theta-nonneg188-bridge-receipt.json) separately verify `Θ B q r = SupSet.sSup (indexSet B q r)`; this adds the fifth accepted native set. This satisfies the explicit parent re-aim gate; no automatic inheritance, misleading project-call count, or cost-based downgrade is used.

If eliminating wrapper API, inline this existing law at **both occurrences in the one caller** `index_le_lem6` (Theta:583), with the nonnegative support-inf premise supplied by the independently checked direct proof or by a shared project representation bridge. Keep the caller's surrounding arithmetic unchanged. A shared local pointwise nonnegative index convenience theorem may remain during parent migration, but it is project API, not a new mathlib theorem. Do not add boundedness or `1≤B`; fallback0 already handles all exceptional families. Do not replace real sSup with EReal empty-sup conventions.

Alternative local destination: **Roth/Theta.lean manuscript convenience API**. It records source notation and keeps the Φ application short; no Archive or satellite library is needed. Missing upstream API: none established for this law. YES-only path/title/PR grouping/reviewer selection and /generalise,/cleanup proposal are n/a because no new upstream declaration is proposed. Neighboring upper-bound and substantive arithmetic theorems need separate assessments.

## Phase 8 — Handoff

All required phases complete; unresolved=[]; root acceptance pending. [Assessment](../evidence/Roth.Θ_nonneg/assessment.json), [verification](../evidence/Roth.Θ_nonneg/verification.json), [overview entry](../evidence/Roth.Θ_nonneg/overview-entry.json), [current manifest](../evidence/Roth.Θ_nonneg/copy-manifest.json), [portable read-only validator](../evidence/Roth.Θ_nonneg/validate.py). The validator checks fresh17 inputs, exact canonical293 order including private names, target-scoped native success/axioms,12formal+3rg cells, named literature requests, complete caller substitutions, current manifest hashes/bytes and portable links, and credential hygiene. It uses current copy-manifest.json; a later historical worker-copy-manifest is not authoritative for integration hashes.
