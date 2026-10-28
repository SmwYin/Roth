from pathlib import Path
import json
D=Path(__file__).resolve().parent;N='Roth.lem7_Φ_bound'
def load(n):return json.loads((D/n).read_text())
def link(n,label=None):return '['+(label or n)+'](../evidence/'+N+'/'+n+')'
typ=load('native-type.json')['type'];row=load('target-metadata.json')
s='''# Roth.lem7_Φ_bound — completed assessment218

**BORDERLINE-needs-human.** This is a useful strict numerical estimate inside the Roth induction, with one verified source consumer. Its exact base10/dimension/dyadic constants have a clear local purpose, but evidence does not establish a public numerical API audience. A genuine generic real-power envelope and a wider `δ ≤ 2` version compile. Neither is an existing mathlib replacement, and no ≤3-existing-call proof of the original was established. The remaining questions concern future upstream scope and presentation; this read-only assessment has no unresolved verification and needs no user response.

## Phase0 — baseline and integrity

The unchanged successful baseline reports2467 jobs. Freshly recomputed all17 production-source/pin hashes agree with that baseline. The canonical index is218; source is `Roth/Theta.lean:678–702`, kind theorem, no source placeholder. The module develops the supremum of polynomial indices and the three Roth index bounds. Entire declaring module and full caller bodies were read. The complete module was replayed in a fresh scratch namespace, with target renamed, standard axioms printed for every public replay declaration, and downstream theorem `Θ_lt` checked.

'''+link('inputs.json','Fresh17 input checks')+'; '+link('input-manifest.json','shared baseline manifest')+'; '+link('baseline-build.txt')+'; '+link('target-metadata.json')+'; '+link('source-module.lean.txt')+'; '+link('canonical-entry.json')+'''. Production Lean, pins, Git and overview/progress records were not edited by this worker.

The exact private-aware canonical293 ordered name array passed an independent pre-execution source comparison and runtime293 requested/unique/present/value checks. The sole direct kernel-value consumer is `_private.Roth.Theta.0.Roth.theta_phi_lt_aux`. This is a direct-constant audit, not an opaque transitive/simp dependency closure. '''+link('canonical-preflight.json')+'; '+link('canonical-snapshot.json')+'; '+link('canonical-consumers.json')+'''.

## Phase1 — mathematical comprehension

For an integer dimension `p ≥ 2` and `0 < δ ≤ 1`, put `e = 2^{-(p-1)}` and `δ₁ = δ(1+1/p)`. Then `δ₁ + 10^{p-1} δ₁^e < 3·10^{p-1} δ^e`. This converts the one-variable plus lower-dimensional estimates in the induction into a uniform envelope for Φ. The statement itself contains neither Θ nor Φ; it is a standalone numerical inequality.

The complete fresh elaborated type is:

```lean
'''+typ+'''
```

There are two data parameters (`p : ℕ`, `δ : ℝ`) and exactly three propositional premises: `hp`, `hδ0`, `hδ1`. There are no inherited `Fintype`, `DecidableEq`, universe, polynomial or other project parameters in the elaborated type. Source and kernel audit record no direct project dependencies for the target.

Proof: `e≤1`; `1≤c=1+1/p≤3/2`; hence `δ≤δ^e` and `(δc)^e=δ^e c^e≤(3/2)δ^e`. With `A=10^{p-1}≥10`, the left side is at most `(3/2)(1+A)δ^e`, leaving a strictly positive margin below `3Aδ^e`. The source finishes by a verified linear combination of these bounds.

'''+link('native-type.json')+'; '+link('original-executed.lean.txt','exact executed entire replay')+'; '+link('original-receipt.json','full native receipt')+'''. The printer explicitly elides72887 characters of the kernel pretty-print body; the full type, exact complete written source, axiom information and canonical value audit are intact. No full kernel-body dump is claimed.

## Phase2 — preliminary checks

**SMALL:** a numerical helper, not a named mathematical theorem or one of the module's main results. Literature search still runs exhaustively. One-line-definition check: **n/a**, kind theorem; source proof has23 substantive lines. No definition, reducibility barrier, typeclass diamond exemption or stable-definition-name exemption is being asserted.

## Phase3 — exhaustive literature

Every named channel was executed; the skill's informal nine-channel count does not replace its separately listed queries. Only exact requests, response hashes/bytes/status, returned locators and original concise summaries are stored for web results; no complete web bodies or signed URLs are archived.

| Channel | Actual query / locator | Finding and limit |
|---|---|---|
| General specific | `Roth theorem index polynomials Phi delta 10 induction lemma 7` | Roth ICM1958 extract and Stanford/Princeton index proofs; no independently standardized exact numerical lemma. |
| General broader | `real power inequality 0 x 1 exponent less than one scaling c sublinear bound` | General real-power context; no exact weighted envelope established. |
| General aliases | `Thue Siegel Roth index lemma dyadic exponent delta proof` | Diophantine polynomial-index induction; distinguish additive Roth. |
| Optional mathematical ChatGPT | Standard form, generality and historical-evolution request | n/a: `ask_chatgpt_math` unavailable; no substitute response invented. |
| Local reference | `clean.tex:969–1033`, especially1008–1020 | Exact δ₁/Φ absorption in proof of Lemma7; source writes strictδ<1, current Lean permitsδ=1. |
| nLab | `site:ncatlab.org/nlab real exponent power inequality Roth index` | General inequality and real nth-root pages, no exact index-envelope law. |
| distinct nCatLab | `site:ncatlab.org/ncatlab Roth index real power inequality` | Returned nLab/out-of-namespace noise honestly retained; no categorical analogue established. |
| Stacks | `site:stacks.math.columbia.edu Roth polynomial index real power inequality` | Polynomial/geometric results, no exact numeric inequality; substantive algebraic geometry is not involved in this theorem. |
| MathOverflow | `site:mathoverflow.net Roth lemma index polynomial induction constants` | Index/Dyson/shortest-proof discussions supply context; no exact 3/10 estimate. |
| Recent arXiv | `site:arxiv.org Roth theorem formalizing index polynomials after:2021-10-28 before:2026-10-29` | Recent additive/ergodic polynomial Roth hits; opened2607.05124,2207.07499,2307.00271 and rejected them as different subjects. |
| Recent arXiv refinement | `site:arxiv.org "Formalizing Roth" after:2021-10-28 before:2026-10-29`; `site:arxiv.org "Roth" "index" "Diophantine" after:2021-10-28 before:2026-10-29` | Returned unrelated Phillip H. Roth communication-history paper; no exact numerical law identified. |
| Primary openings, supplementary | Roth ICM1958 PDF; Soundararajan/Petrow notes §17; MO Dyson-index question | ICM full opening failed400 due74705952-byte fetch length; search extract only. Stanford opened, pp61–62 gives index induction with different constants. MO is contextual. |

'''
for n in ['web-general','literature-source','nlab','ncatlab','stacks','mathoverflow','arxiv','arxiv-refined','primary','primary-locators','recent-primary']:
 s+=link(n+'.json')+'; '
s+=link('clean-excerpt.tex.txt')+'''.

The literature concept is **Roth's polynomial-index induction and its numerical real-power absorption**. The exact local source agrees with the present formula, while other references choose different parameters/constants. There is no evidence for a separately named universally standard 3/10/dyadic inequality. Historical index methods belong to the surrounding Roth theorem; this helper makes no independent historical innovation claim. Generic positive real-power scaling is the natural broader analytic form, verified independently below; its precise packaged envelope is a proposed organization, not a literature theorem newly discovered by search.

## Phase4a–b — parameters and verified generality

| Parameter/premise | Source role | Weakening / necessity evidence |
|---|---|---|
| `p : ℕ` | Dimension and natural powers; truncated `p-1` | Natural dimension reflects the induction. Reparameterization `p=k+2` compiles. Abstract exponent/multiplier/coefficient can be separated without changing the real-power operations. |
| `hp : 2≤p` | Bounds c by3/2 and A below by10 | Atp1 and anyδ>0, formula becomes4δ<3δ and fails. Dropping all lower-dimensional control is invalid. Atp0 the totalized formula holds, but that is not a useful zero-dimensional induction interface. |
| `δ : ℝ` | Real coefficient error parameter and real powers | `Real.rpow` is concrete real analysis; arbitrary ordered-field substitution is not justified by these interfaces. NNReal/ENNReal variants exist for ingredients but require a separately verified representation bridge, not mere typeclass weakening. |
| `hδ0 : 0<δ` | Strict positivity ofδ^e supplies strict gap | Replacing by0≤δ is false atδ0, withp≥2 andδ≤1 intact. Clean native guard proves the failure. |
| `hδ1 : δ≤1` | δ≤δ^e | Stronger than needed. **Successfully compiled** replacementδ≤2, byδ≤2δ^e; old theorem is a verified wrapper and all downstream original statements compile unchanged. No optimal endpoint claim. Removing all upper control fails atp2,δ400, whilep≥2 andδ>0 hold. |
| Instances/universes | None in full target type | No unused ambient typeclass to remove. |

Generality verdict: **STRICTLY NARROWER for the verified numericalδ-range**, while the exact constants/dimension coupling remain a public-API scope question. The proposed reachable restatement is the exact original statement with `(hδ2 : δ ≤ 2)` replacing `(hδ1 : δ ≤ 1)`. This is a proved weakening, not an assertion based on source appearance. Full proof and old-signature wrapper occur in '''+link('broader-executed.lean.txt')+'; '+link('broader-receipt.json')+'''. The mathematical proof change uses a case split at1 and reduces the final strict slack from27/2 to12. It does not alter the caller contract.

The independently compiled abstract envelope is:

```lean
theorem envelope {x c A e : ℝ} (hx : 0 < x) (hx1 : x ≤ 1) (hc : 1 ≤ c)
    (hA : 1 < A) (he : e ≤ 1) :
    x * c + A * (x * c) ^ e < 2 * c * A * x ^ e
```

It has no lower bound on `e`: both exponent-monotonicity facts still hold for all `e≤1` on these strictly positive bases. It is a true extension of the same power comparison. The original follows by a checked specialization using `c≤3/2` and `A≥10`. It is **new scratch proof**, not an existing mathlib call and not evidence of a missing theorem's global absence. '''+link('isolated-executed.lean.txt')+'; '+link('isolated-receipt.json')+'''.

## Phase4c — all modern-idiom rows

| # | Question | Answer / concrete consequence |
|---|---|---|
| 1 | Typeclass preambles | No: scalar inequalities are values, not a mathematical structure suitable for new instances. |
| 2 | Filters rather than sequences | No: finite numerical estimate has no convergence quantifiers. |
| 3 | Universal-property characterization | No object is constructed. |
| 4 | Bundled substructure rather than predicate | No closure predicate or substructure. Bundlingδ∈Ioc0 1 would add projection work at the actual caller. |
| 5 | Weaken hierarchy | No mechanical general-real-power interface over arbitrary ordered fields is proved. Existing NNReal/ENNReal ingredient forms are not a checked replacement for this exact inequality. |
| 6 | Higher categories | No categorical content. |
| 7 | Concrete indices | Yes in the analytic organization: independently choose real exponente, scalingc and coefficientA instead of tying them all to naturalp. This lets generic `Real.mul_rpow` and exponent bounds handle other scaling constants/exponents. |
| 8 | Concrete-via-abstract diagnostic | The literal named-object test is n/a: no Θ/lem6Φ occurs in the target type or proof. The constants diagnostic is positive: after settinge, the proof uses onlye≤1,c∈[1,3/2],A≥10,δ^e>0. The compiled generic envelope separates those properties and its concrete wrapper compiles. |
| 9 | False-generalization guard | Same real multiplication, order andrpow, so the envelope preserves the mathematical content on the original positive domain. Interpretingp0 as a new Roth dimension or replacingδ>0 by nonnegativity is rejected; endpoint guards explicitly expose the difference. |

Modern idiom available: **yes, generic numerical envelope**, with real downstream consequences for arbitrary scalingc, coefficientA and exponente via the existing product and exponent-monotonicity APIs. A new generic helper may shorten concrete applications, but there is no verified independent library consumer besides this specialization. This is an API-audience judgment, not a reason based on implementation cost.

## Phase4.5 — infrastructure risks

**n/a: theorem.** Typeclass diamonds, reducibility leaks, noncanonical unfolding, instance-priority collisions, universe-polymorphism defects and coercion ambiguity are each n/a for this addition: it creates no definition, class, instance or coercion. No unverified implementation of the proposed generic helper is treated as new infrastructure.

## Phase4.6 — all proof-strategy rows

| # | Strategy question | Finding |
|---|---|---|
| 1 | Topologyε–δ to filters | n/a: no topology. |
| 2 | Element algebra to ideals/submodules | n/a: ordered scalar arithmetic, no algebraic substructure. |
| 3 | Sequences to nets/filter limits | n/a: no limiting argument. |
| 4 | Explicit object to universal property | n/a: inequality proof constructs no mathematical object. |
| 5 | Missing helper that mathlib should have | Conditional: a generic weighted power envelope could factor the proof. Product/exponent comparisons and weighted order transport already exist; the independent envelope is new proof whose public utility is undecided. |

Strategy verdict: **MATHLIB-IDIOMATIC** for a local helper: expose power monotonicity then use ordered arithmetic. Optional refactor if a public generic envelope is adopted: replace the fixed-constant proof by the checked generic specialization. It removes repeated analytic comparisons, but does not make the original a≤3-existing-call composition. No claim that a longer proof is justified merely because it is already written.

## Phase5 — exhaustive actual mathlib search

All fifteen cells were executed freshly. Remote indexes may differ from this pin. Local name search reports `index: warming`; positive source hits are useful, but missing hits do not prove absence.

| Form | Method | Query / selected returned candidates | Receipt |
|---|---|---|---|
'''
for form in ['current','standard','abstract']:
 for method in ['leanfinder','loogle','leansearch','rg','local_search']:
  x=load('search-'+form+'-'+method+'.json')
  if method=='rg':q=x['command'][2];hit='source matches' if x['exit_code']==0 else 'no lexical hit'
  else:
   q=x['request']['query'];z=x['result'].get('structuredContent',{});names=[i.get('name',i.get('formal_name',''))for i in z.get('items',[])];hit=', '.join('`'+n+'`'for n in names[:3])or 'no hit'
  s+='| '+form+' | '+method+' | `'+q.replace('|','\\|').replace('`','')+'`; '+hit+' | '+link('search-'+form+'-'+method+'.json','raw receipt')+' |\n'
s+='''
Pinned positive signatures and actual proofs use `Real.mul_rpow` (`Pow/Real.lean:477`), `Real.rpow_le_rpow_of_exponent_le` (617), `Real.rpow_le_rpow_of_exponent_ge` (643), `Real.rpow_pos_of_pos`, and generic `le_self_pow₀` (`Algebra/Order/GroupWithZero/Basic.lean:505`). Their complete native types and applications are in the isolated receipt; the absence guard `#check_failure Roth.lem7_Φ_bound` confirms no project import supplies the target. The exact18-import prefix is archived unchanged. No extra import was required.

Near-misses: arithmetic-progression `Behrend`/`rothNumberNat` facts are a different Roth theorem. Power-mean inequalities apply to a weighted sum raised to an exponent and need extra convexity/weight premises; they are not this affine sum of powers. Source `rpow_one_add_le_one_add_mul_self` at `Analysis/Convex/SpecificFunctions/Basic.lean:168` offers a Bernoulli-type ingredient for `c^e`, not the whole numerical absorption. It was source-inspected, not falsely presented as a compiled exact replacement. No candidate establishes NO-mathlib-has-it.

Search conclusion: existing product/exponent/ordered-arithmetic ingredients identified; **no exact replacement established**, not a proof of global absence. '''+link('mathlib-inputs.json','pinned candidate source hashes')+'''.

## Phase5.5 — statement shape

Normal form: real `rpow` is already the canonical positive-base representation. Alternatives are an expanded product `δ^e*c^e`, a normalized ratio after dividing byδ^e, and exponent reindexingp=k+2. The product form was actually tried as a closure probe and does not close the theorem alone. A ratio formulation would require positivity side conditions already available but adds division/rewriting at the only caller; it is not selected.

Syntactic generality: checked `successor(k)` removes truncated subtraction and thehp argument withp=k+2. It remains a specialization of the exact target and compiles; the actual caller already hasp=n+2 andhp, so the existing statement is convenient. No public syntactic rewrite is required. '''+link('shape-executed.lean.txt')+'; '+link('shape-receipt.json')+'''.

Superfluous-argument audit: `p` and `δ` occur in the conclusion;hp controls the reciprocal and natural power;hδ0 supplies the strict gap;hδ1 is used but can be weakened toδ≤2. No inherited typeclasses are present. All three hypothesis changes have either a compiled positive weakening or explicit compiled boundary counterexample, so the assessment does not infer necessity solely from proof references.

Statement-shape verdict: **OK for the project; considerδ-range/abstract-envelope restatement before any upstream shipment.** No off-normal-form equivalence lemma is proposed. The normalized numeric envelope on the RHS is consistent with the original use.

## Phase6.0 — complete source callers and inline audit

Fresh ignore-independent `rg --no-ignore` over all production `Roth/` and `Roth.lean` agrees with tracked `git grep -w`. The source inventory and full caller hashes cross-check the results. There are exactly two lexical occurrences: declaration678 and call876. No target occurrence in another production module or statement. Internal use count1; external-to-file0; inline-derivation audit finds no second complete rederivation bypassing this theorem.

| Caller | Full body | Use / checked refactor option |
|---|---|---|
| `Roth.theta_phi_lt_aux` | `Roth/Theta.lean:840–889` | At876 instantiatep=n+2,hp,hδ0,hδ1.le; normalize successor subtraction/casts inhb, then chain the index estimates and calllem7_numeric. Full module replay with the entire numeric proof inserted as a local `have numeric` compiles throughΘ_lt. |

'''+link('source-search.json')+'; '+link('tracked-source-search.json')+'; '+link('inline-audit.json')+'; '+link('callers.json')+'; '+link('inline-executed.lean.txt')+'; '+link('inline-receipt.json')+'''. One explicit caller and one direct canonical kernel-value consumer coincide here; they are separately measured quantities. The theorem is used, so a dead-code conclusion is unsupported.

## Phase6 — actual composition experiments

1. The isolated original-form proof executes `fail_if_success exact?` and a product-only simplification closure test. Both negative tests pass in the final clean source. This bounds the tested routes and does not prove all mathlib proof searches impossible.
2. A positive generic ordered transport compiles as `(add_le_add hu (mul_le_mul_of_nonneg_left hx hA)).trans_lt hgap`. It transports supplied numerical premises; deriving the target'sδ/c/e/A bounds is additional substantive work.
3. The original is independently proved from the **new** envelope plusc≤3/2,A≥10,e≤1 and arithmetic. This is a real proof, not≤3existing calls, because the helper itself is new.
4. Complete actual caller local inlining compiles. That shows the theorem can be local; it does not show its mathematics already exists as a short composition.
5. Theδ≤2 proof with an old-contract wrapper compiles through every downstream declaration in the complete module.

Composition verdict: **NOT-COMPOSABLE under the verified≤3-existing-call criterion.** No closing `simp [defs]` composition was found. There are no project definitions to unfold in this target, so the parent re-aim gate is n/a. Existing real-power ingredients account for the mechanism; the specific simultaneous numerical absorption remains proved reasoning.

## Phase7 — verdict and actionable scope

**BORDERLINE-needs-human.** The local source gives the exact estimate; the current formula is mathematically sound, used once, and can be broadened or abstracted by verified proofs. No exact mathlib hit or qualifying short composition justifies either NO bucket. Conversely, the library-wide audience for a named fixed-constant envelope is not established merely because the elementary proof uses several comparisons. The choice concerns public numerical API scope and grouping with a future Roth-index development. Cost and proof length are not verdict factors. This is not YES-but-generalise-first solely becauseδ≤2 compiles: the upstream desirability of the numerical package must first be chosen.

Concrete future upstream questions (not verification blockers):

1. Should a generic weighted real-power absorption theorem be public API in `Mathlib/Analysis/SpecialFunctions/Pow/Real.lean`, with this fixed-constant estimate kept local to a future Roth-index module?
2. If the fixed-constant estimate is exposed within an upstream Roth development, should its contract use the verifiedδ≤2 range or theδ≤1 range used by the induction?
3. Should the unique caller keep a named local numerical helper or inline it, given that the complete caller and downstream theorem compile either way?

Alternative destination now: **`Roth/Theta.lean`**, next to the induction it serves. No production refactor is requested in this read-only overview. If later choosing local inlining, replace the sole call at876 with the checked local numeric proof from the archived entire-caller experiment; no other explicit source caller needs modification. If later choosing an upstream generic envelope, first run `/generalise Roth.lem7_Φ_bound`, then `/cleanup Roth/Theta.lean Roth.lem7_Φ_bound` and the candidate destination's cleanup. Proposed PR title, accepted-YES grouping and recent-commit reviewer selection are n/a for this BORDERLINE verdict, not silently omitted YES requirements.

## Phase8 — verification and freeze

Five accepted exact native executions: original entire replay/audit, isolated generic/current/guards,δ≤2 entire replay/wrapper, entire caller local inline, and shape/transport/zero-dimension guard. All final batches are successful, nonpartial where the tool format suppliespartial, warning/error-free, with standard axioms only. Raw run-code format hasdiagnostics/success rather than a diskpartial field; the validator handles it explicitly. Full-file error/warning/axiom checks apply, while required new messages are scoped to the new namespace region.

Four rejected attempt pairs remain separate: initial isolated elaboration/linter/witness failures; accidental execution of missing-file error text after a failed width preparation; initial wider elaboration/type failures; shape header warning. RecoveredsorryAx occurs only in rejected receipts. These are never used as accepted evidence. Every later preparation was separately executed and its successful exit inspected before native invocation. No new axioms, `sorry`, `unsafe`, `native_decide`, raised limits or repeated exhausting automation were introduced.

'''+link('verification.json')+'; '+link('preparation-notes.json')+'; '+link('assessment.json')+'; '+link('phase-ledger.json')+'; '+link('overview-entry.json')+'; '+link('validate.py','portable current-manifest validator')+'''. Root owns independent acceptance, integration, commits and push. The current copy manifest, not the historical worker manifest, is authoritative after integration.
'''
# Fix a construction-only quotation seam.
s=s.replace(". '' ",'. ')
(D/'report.md').write_text(s)
print('Report written',len(s.encode()),'bytes')
