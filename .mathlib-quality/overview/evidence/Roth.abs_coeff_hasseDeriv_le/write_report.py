from pathlib import Path
import json,hashlib,re
D=Path(__file__).parent;N='Roth.abs_coeff_hasseDeriv_le'
def out(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def link(n):return f'[{n}](../evidence/{N}/{n})'
modern=[
 ('Typeclasses / bundled hypotheses','yes','Use existing AddGroupSeminorm R, with CommRing R; no custom size predicate.','Existing map_add_le_add/apply_nonneg; any coefficient seminorm.'),
 ('Sequences / filters','no','Finite algebraic estimate has no convergence.','n/a'),
 ('Construction / universal property','no','A coefficient inequality does not construct an object.','n/a'),
 ('Set / bundled substructure','no','No substructure appears.','n/a'),
 ('Field-specific / hierarchy','yes','Replace integer coefficients by arbitrary CommRing R and additive seminorm.','Works in positive characteristic and without multiplicative norm assumptions.'),
 ('Higher categories','no','No categorical structure enters.','n/a'),
 ('Concrete index','no','σ is already arbitrary finite; ℕ exponent is intrinsic polynomial degree.','Do not substitute another degree monoid without redesigning Hasse derivatives.'),
 ('Concrete-via-abstract diagnostic','yes','After coeff_hasseDeriv the operator occurs zero times in the proof; absolute-value scalar arithmetic uses only additive seminorm laws.','Generic bound and exact integer specialization compile.'),
 ('False-generalisation guard','PASS','Same Hasse operator and same coefficient positions and 2^sum r constant. AddGroupSeminorm changes only coefficient size.','No divided-power algebra replacement; exact intSize bridge compiled.')]
strategy=[
 ('Topology / filters','no','No topology; finite-support coefficient arithmetic.'),
 ('Elements / subobjects','no','Pointwise coefficient inequalities are the appropriate interface, not ideal inclusions.'),
 ('Sequences / nets','no','No limiting process.'),
 ('Construction / universal property','no','No categorical construction.'),
 ('Missing helper API','yes','Multivariate coeff_hasseDeriv plus a quantitative bound; additive-seminorm natural scalar bound may be a small supporting lemma. Normed-group norm_nsmul_le is existing, but is not silently counted as a supplied arbitrary bundled-seminorm theorem.')]
risks=[('Typeclass diamond','n/a: theorem; adds no instance'),('Reducibility leak','n/a: theorem; no computational definition'),('Non-canonical unfolding','n/a: theorem; inequality is not a new unfolding equation'),('Instance priority collision','n/a: theorem; no instance priority'),('Universe polymorphism','n/a: theorem; arbitrary σ and R remain universe-polymorphic'),('Coercion ambiguity','n/a: theorem; existing AddGroupSeminorm coercion reused')]
out('generality.json',dict(modern_rows=modern,strategy_rows=strategy,infrastructure_rows=risks,expanded_forms=[dict(name='CommRing coefficients and AddGroupSeminorm',verified=True,status='PASS',source='native-generic-executed.lean.txt',receipt='native-generic-success.json'),dict(name='exact integer absolute-value specialization',verified=True,status='PASS',source='native-generic-executed.lean.txt',receipt='native-generic-success.json')],not_claimed=['dropping Fintype σ without changing RHS','arbitrary degree monoid','semiring AddGroupSeminorm without additive inverses'],false_generalization_guard='Same coefficient operator and constant; exact specialization compiled.'))
phases={k:'PASS' for k in ['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']};phases['4.5']='n/a: theorem; six risk rows justified'
out('assessment.json',dict(declaration=N,canonical_index=89,verdict='YES-but-generalise-first',reason='MODERN-IDIOM',completed=True,allphases='PASS',phases=phases,unresolved=[],root_acceptance='pending',production_unchanged=True))
type_='∀ {σ : Type u_1} [Fintype σ] (d : σ →₀ ℕ) (P : MvPolynomial σ ℤ) {r : σ → ℕ}, (∀ j, MvPolynomial.degreeOf j P ≤ r j) → ∀ {B : ℝ}, (∀ e, |((P.coeff e : ℤ) : ℝ)| ≤ B) → ∀ e, |(((MvPolynomial.hasseDeriv d P).coeff e : ℤ) : ℝ)| ≤ 2 ^ (∑ j, r j) * B'
out('overview-entry.json',dict(declaration=N,kind='theorem',type=type_,what='Every coefficient of a multivariate Hasse derivative is bounded by 2^(sum coordinate degree bounds) times an input coefficient bound.',how='Coefficient extraction has one preimage e+d; split membership in input support, bound binomial product, multiply coefficient bound, handle zero coefficients.',hypotheses='Arbitrary finite variable type; integer polynomial; coordinate degree bounds r; real coefficient bound B; no B≥0 assumption because hB implies it.',project_dependencies=['MvPolynomial.coeff_hasseDeriv','MvPolynomial.hasseCoeff_le_two_pow'],caller_summary='Three explicit applications in two private MainLemma declarations at lines468 and509; full replay and exact canonical293 unique proof-value audit.',mathlib_api_audit='Polynomial.hasseDeriv_coeff and norm_nsmul_le cover separate ingredients; no searched multivariate Hasse coefficient-size bound. Isolated raw binomial bound and actual generic operator bound compiled.',moral_duplications='Same finite binomial factor appears in normOne_hasseDeriv_le; that is an L1 estimate and cannot retain the coefficient B without an unwanted support-cardinality factor.',generalization='Verified arbitrary CommRing R with AddGroupSeminorm R, followed by exact integer absolute-value specialization.',missing_api='Quantitative coefficient bounds for multivariate Hasse derivatives, atop the proposed multivariate Hasse algebraic API.',junk='Not junk: three explicit uses support main Lemma9, including iterated derivatives and diagonal remainder bounds.',action='YES-but-generalise-first MODERN-IDIOM: add additive-seminorm version in proposed Mathlib/Analysis/Polynomial/MvHasseDeriv.lean, after upstream algebraic Hasse API; preserve local integer corollary.'))
out('callers.json',dict(named_count=2,explicit_occurrences=3,files=1,callers=[dict(name='Roth.abs_eval_iterated_hasseDeriv_lt_aux',file='Roth/MainLemma.lean',line=468,occurrences=2,plan='Replace each integer bound call by generic bound intSize; nested application retains identical constants.'),dict(name='Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux',file='Roth/MainLemma.lean',line=509,occurrences=1,plan='Replace coefficient bound by generic bound intSize before abs_coeff_diag_le; subsequent support-cardinality and monic-remainder proof unchanged.')],inline='normOne_hasseDeriv_le reuses factor argument for a different L1 conclusion; no bypass derivation of this exact coefficient B bound found.',native_audit=dict(status='PASS',requested=293,unique=293,present=293,values=293,source='native-consumers-executed.lean.txt',receipt='native-consumers-success.json'),scope='Explicit source references plus direct constants in canonical proof values; not an opaque kernel/simp transitive dependency closure.'))
group=json.loads((D/'accepted-yes-grouping.json').read_text())
accepted={x['declaration'] for x in group['accepted_yes']}
grouping=[n for n in ['MvPolynomial.hasseDeriv','MvPolynomial.coeff_hasseDeriv','MvPolynomial.hasseDeriv_map','MvPolynomial.hasseDeriv_rename','MvPolynomial.degreeOf_hasseDeriv_le'] if n in accepted]
rows=lambda xs:'\n'.join('| '+ ' | '.join(map(str,x))+' |' for x in xs)
report=f'''# {N} — YES-but-generalise-first

Canonical declaration **89/293**, Roth/CoeffNorm.lean:134–145. Reason: **MODERN-IDIOM**.
The useful upstream result is a coefficient bound for an arbitrary additive seminorm on
any commutative coefficient ring. The exact integer absolute-value theorem is its verified
specialization. This assessment changes no production source or pin.

## Phase 0 — Baseline and declaration resolution

The shared `lake build` succeeded (2467 jobs). All 17 current production/pin hashes freshly
match its baseline manifest: {link('inputs.json')}, {link('input-hash-check.json')},
{link('baseline-build.txt')}. Canonical metadata: {link('canonical-order.json')} and
{link('canonical-entry.json')}. The full declaring module, Hasse module and MainLemma caller
module were read fresh; archived as {link('source-module.lean.txt')},
{link('HasseDeriv-module.lean.txt')}, {link('MainLemma-module.lean.txt')}.
The original theorem and same-proof replay resolve, elaborate, and use only
`propext`, `Classical.choice`, `Quot.sound`: {link('native-original-success.json')}.

## Phase 1 — Mathematical statement and proof

If every coordinate degree of P is at most r_j and every coefficient has absolute value
at most B, then every coefficient of any fixed Hasse derivative Δ_d P has absolute value
at most 2^(Σ r_j) B. There is no support-cardinality factor: the output coefficient at e
receives exactly the input coefficient at e+d times a product of binomial coefficients.

Full Lean type (explicit spelling of the native elaborated statement):

```lean
{type_}
```

The native `#check @...` and `#print` record the complete universes and binders in
{link('native-original-success.json')}; exact executed source is
{link('native-original-executed.lean.txt')}. σ is an arbitrary finite type, d/e are arbitrary
finitely supported natural multi-indices, P has integer coefficients, r gives natural
coordinate bounds, and B is a real bound. Both explicit hypotheses are essential to a
uniform estimate of this shape. No nonzero-polynomial or nonzero-derivative hypothesis is
needed. hB itself implies 0≤B, by looking at any coefficient.

Proof: rewrite `coeff_hasseDeriv`, cast the natural multiplier and use absolute-value
multiplicativity. If e+d belongs to the input support, `monomial_le_degreeOf` and hP bound
its coordinate exponents, then `hasseCoeff_le_two_pow` bounds the multiplier. Apply
`mul_le_mul`. Outside support the coefficient is zero; nonnegativity of B gives the result.
This support split is meaningful proof content, not a projection of an existing norm law.

## Phase 2 — Preliminary checks

**SMALL**: a reusable quantitative helper, neither a new structure nor a named main theorem.
The one-line-definition filter is **n/a: theorem**. The existing proof contains substantive
support and inequality reasoning. Its three explicit applications are useful API evidence,
but use count does not itself decide the verdict.

## Phase 3 — Exhaustive literature search

The exact requests, returned-response SHA256/byte counts/status, credential-safe URLs and
original concise summaries are in {', '.join(link('web-'+str(i)+'.json') for i in range(15))}.
Full returned web/search bodies were not archived. Each listed web channel was actually
queried; there are at least three distinct general-web forms and at least three queries
for each named external search channel. The final arXiv request explicitly covers
2021-10-27 through 2026-10-27. Query noise is recorded, not counted as a positive hit.

| Channel | Queries / access | Finding |
|---|---|---|
| General web specific | multivariate Hasse derivative coefficient bound height 2 degree | Primary Hasse-operator papers/notes; exact bound in local paper. |
| General web general | polynomial seminorm coefficient binomial bounds arbitrary ring | Commutative-ring operator is standard; abstract seminorm inequality is our verified inference. |
| General web alias | divided derivatives polynomial height estimates Roth theorem | Height/divided-derivative terminology; divided differences excluded. |
| ChatGPT math | n/a: ask_chatgpt_math unavailable | No independent ChatGPT opinion claimed. |
| Local references | fresh rg of clean.tex plus §§1,3,6 | Exact coefficient estimate and no-collision mechanism. |
| nLab | Hasse derivative; Hasse-Schmidt derivation; divided powers | Indexed page gives binomial monomial law over a commutative rig. Direct open failed: unsupported XHTML content type. |
| nCatLab | Hasse-Schmidt/divided powers; differential operator; higher derivation, plus /ncatlab queries | Related categorical discussions; no exact quantitative law identified. |
| Stacks | divided power/Hasse; Hasse-Schmidt; divided-power polynomial structure | Tags 07H4 and 09PG concern related but different multiplication, not this inequality. |
| MathOverflow | Hasse coefficient norm; Hasse bound; divided-derivative height | No exact hit; divided-difference results do not replace Hasse coefficient extraction. |
| Recent arXiv | initial height query; 2024 query; 2022 multivariate query; explicit five-year window | arXiv:2201.06156 confirms use for multiplicities; no exact seminorm coefficient bound there. |

Local exact locators and source hash: {link('local-literature-source.json')},
{link('local-literature.txt')}, {link('rg-local-literature.json')}. clean.tex lines457–461 bound
the binomial-scaled monomial coefficient by B2^S; lines496–498 explain that each output
coefficient has at most one input; lines1445 and1537–1544 use this estimate successively.
The literature calls the operator the Hasse or divided derivative, defined by coefficients
of P(X+Z). The algebraic operator works over commutative semirings; quantitative real size
requires additional additive-size structure. The proposed AddGroupSeminorm formulation is
a proved modern abstraction, not an assertion that every source states that exact signature.

Primary references checked: [Kopparty–Saraf–Yekhanin, multiplicity codes](https://people.csail.mit.edu/dmoshkov/courses/codes/Multiplicity.pdf),
[He–Pham–Xu, January2022](https://arxiv.org/abs/2201.06156),
[Stacks 07H4](https://stacks.math.columbia.edu/tag/07H4).
The [nLab indexed formulation](https://ncatlab.org/nlab/show/Hasse-Schmidt+derivative)
is useful terminology, with the direct-access limitation stated above.

## Phase 4a — Parameter and hypothesis generality

| Parameter / hypothesis | Present role | Verdict and verification |
|---|---|---|
| σ : Type* | Variables arbitrary | Already universe-polymorphic; no fixed Fin m. |
| Fintype σ | Finite sum Σr_j and product estimate | Retained. Dropping it changes the written RHS; no unverified weakening claimed. |
| d : σ→₀ℕ | Hasse order | Arbitrary; zero, large and overlapping orders allowed. |
| P : MvPolynomial σ ℤ | Coefficient ring fixed to integers | Verified arbitrary CommRing R with AddGroupSeminorm R. |
| r : σ→ℕ | Coordinate degree bounds | Arbitrary including zeros. Finite derivative-support alternatives change representation and are not needed here. |
| hP : ∀j, degreeOf j P≤r j | Bound relevant input exponents | Essential for a uniform 2^Σr bound; e.g. linear derivative of X^n has coefficient n. |
| B : ℝ | Coefficient size bound | Arbitrary real; hB implies nonnegativity. No extra hB0 introduced. |
| hB : ∀e, abs coefficient≤B | Uniform input size | Retained as ∀e, p(coeff e)≤B; handles zero P uniformly. |
| e : σ→₀ℕ | Output coefficient | Arbitrary; pointwise conclusion supports nested calls directly. |

## Phase 4b — Verified generalisation

**STRICTLY NARROWER than the verified modern formulation.** Replace the integer absolute
value by an arbitrary `p : AddGroupSeminorm R` for `[CommRing R]`. No multiplication law,
normalization at 1, norm topology, characteristic assumption, field, or normed-ring
structure is required. The proposed signature is:

```lean
theorem seminorm_coeff_hasseDeriv_le {{σ R : Type*}} [CommRing R] [Fintype σ]
    (p : AddGroupSeminorm R) (d : σ →₀ ℕ) (P : MvPolynomial σ R)
    {{r : σ → ℕ}} (hP : ∀ j, MvPolynomial.degreeOf j P ≤ r j) {{B : ℝ}}
    (hB : ∀ e, p (P.coeff e) ≤ B) (e : σ →₀ ℕ) :
    p ((MvPolynomial.hasseDeriv d P).coeff e) ≤ 2 ^ (∑ j, r j) * B
```

Actual complete proof and integer specialization compile:
{link('native-generic-executed.lean.txt')}, {link('native-generic-success.json')}.
Cost is MODERATE (one scalar-bound helper plus support split), not a verdict factor.
This is a generalisation of the original integer theorem, not a claim to weaken the
algebraic parent from commutative semirings to all rings: AddGroupSeminorm needs additive
inverses, while HasseDeriv itself continues to be a commutative-semiring construction.

## Phase 4c — Nine modern-idiom rows

| Question | Applies? | Reformulation / reason | Enabled downstream |
|---|---|---|---|
{rows(modern)}

The concrete-via-abstract diagnostic is explicit: after the first coefficient rewrite,
the proof has **zero** further occurrences of hasseDeriv. Integer casts and abs_mul expose
only natural scalar multiplication, additive size, and ordered real arithmetic. The
abstract theorem uses the *same* operator and its exact integer specialization is one
application of `bound intSize d P hP hB e`. It therefore enables coefficients equipped
with several seminorms, positive-characteristic coefficients, and sizes that need not be
submultiplicative. {link('generality.json')} records these checks.

## Phase 4.5 — Six infrastructure risk rows

**n/a: theorem**, with all six rows explicitly accounted for:

| Risk | Assessment |
|---|---|
{rows(risks)}

The test-only intSize definition is a specialization witness, not a proposed new global
instance or a replacement coefficient norm definition.

## Phase 4.6 — Five proof-strategy rows

| Question | Applies? | Assessment |
|---|---|---|
{rows(strategy)}

Current support/coefficient strategy is mathematically appropriate. **REFACTOR-RECOMMENDED**
for the scalar-size interface: use an additive seminorm, and expose a natural-scalar
inequality if not otherwise available in its API. The compiled helper is genuinely new
proof evidence, not counted as an already-existing mathlib replacement. The finite
binomial estimate may be proved inline from Nat.choose_le_two_pow and finite products;
its previous project assessment is not used as a decision premise here.

## Phase 5 — All five actual mathlib search methods

All current, literature-standard and abstract forms were searched:
{link('formal-search.json')}. Four callable methods produced twelve actual receipts;
the source-rg method produced independent full, untruncated receipts.

| Method | Current | Literature standard | Abstract |
|---|---|---|---|
| Lean-Finder | coefficient Hasse height estimate; broad unrelated hits | divided derivatives/binomial coefficients; broad hits | norm_nsmul_le and variants |
| Loogle | hasseDeriv | choose_le_two_pow | norm of natural scalar multiplication |
| LeanSearch | Polynomial/LaurentSeries Hasse API | Polynomial.hasseDeriv_coeff, pderiv | norm_nsmul_le, norm_smul_le |
| rg pinned source | coeff/Hasse/target names | Hasse operator source families | choose bounds, group seminorm, additive bounds |
| lean_local_search | hasseDeriv | choose_le_two_pow | nsmul_le |

Local index reported **unavailable**, so its text hits are discovery aids and empty results
would not prove absence. Some local-search hits are historical overview evidence, explicitly
excluded from upstream candidate claims. Remote search indexes may differ from the pin;
positive ingredients were checked natively against this project's pin.
Receipts: {link('rg-current.json')}, {link('rg-literature.json')},
{link('rg-abstract.json')}, {link('rg-full-name.json')},
{', '.join(link(m+'-'+f+'.json') for m in ['lean_leanfinder','lean_loogle','lean_leansearch','lean_local_search'] for f in ['current','standard','abstract'])}.

Pinned positives: `Polynomial.hasseDeriv_coeff`, `Nat.choose_le_two_pow`,
`Finset.prod_le_prod`, `MvPolynomial.monomial_le_degreeOf`, `norm_nsmul_le`.
They cover the univariate coefficient formula, binomial estimate, support-degree bridge,
and scalar inequality separately. They do not give the multivariate coefficient estimate
as an existing application. Archived pinned sources and hashes:
{link('mathlib-inputs.json')}. The isolated mathlib-only compilation verifies the finite
binomial-scaled coefficient estimate for an arbitrary additive seminorm; it guards that
the project target and MvPolynomial.hasseDeriv are absent:
{link('native-raw-executed.lean.txt')}, {link('native-raw-success.json')}.
This is constructive proof of the proposed abstraction, not a proof of universal API
absence. No failed search or warming response is interpreted as absence.

## Phase 5.5 — Three statement-shape checks

**Normal form:** pointwise coefficient bound with conclusion `p(coeff ...) ≤ constant*B`.
Equivalent integer spellings include abs after Int→ℝ and Int norm with cast normalization;
a bundled supremum coefficient norm is another possible presentation. A maximum-based
height requires extra finite-support plumbing and is unnecessary for these call sites.
The scalar action `n • a` and natural-cast multiplication are the same action; the
compiled scalar helper keeps their representation explicit. Inequality orientation is ≤.

**Syntactic generality:** retain implicit r/B and pointwise ∀e bounds, so nested derivatives
can feed directly into the next estimate. Both full caller replays use this interface.
`p` should be an explicit existing bundle rather than an arbitrary custom size predicate.

**Superfluous arguments:** σ, d, P, r, B and e each enter the formula; hP bounds exponents,
hB bounds coefficients, and Fintype supplies the finite sum. ℤ/absolute-value specialization
is unnecessary; it is replaced by the verified coefficient ring plus size bundle. No
other deletion is claimed. Overall: **RESTATE-BEFORE-SHIP**, with the verified signature
in Phase4b. No new characteristic or nonzero assumption is introduced.

## Phase 6.0 — Explicit callers, inline audit, canonical proof audit

| Caller | Source use | Refactor |
|---|---|---|
| Roth.abs_eval_iterated_hasseDeriv_lt_aux | MainLemma468, two nested calls | Specialize p=intSize twice; exact same 2^Σr factors. |
| Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux | MainLemma509, one call | Specialize p=intSize before diagonal bound; support-cardinality factor stays in the separate diagonal estimate. |

Thus **3 explicit applications, 2 named callers, 1 caller file**. The raw source rg includes
the declaration itself and uses a short-name word boundary, not only a qualified-name
grep: {link('rg-callers.json')}, {link('callers.json')}.
Inline audit {link('rg-inline.json')} finds `normOne_hasseDeriv_le` using the same binomial
mechanism for an L1 sum; this proves a different conclusion, not a bypass of the B-bound.
No exact unreferenced inline derivation was found. The theorem is not marked simp; no
claim of complete transitive kernel/simp dependency closure is made.

The full two original consumer statements and proofs were replayed with only the bound
calls redirected to the verified generic specialization:
{link('native-consumers-executed.lean.txt')}, {link('native-consumers-success.json')}.
The runtime array has **293 entries and 293 unique names**, all present with proof values.
It was generated directly from the tracked order, preserving private names through
`Lean.mkPrivateNameCore`. The portable validator compares exact order, not just counts:
{link('canonical-audit-array.lean.txt')}. The audit reports the two private MainLemma
consumers. Generated source does not globally replace target strings in this array.

## Phase 6 — Actual composition experiments

1. **Univariate existing Hasse coefficient law:** pinned `Polynomial.hasseDeriv_coeff`
   gives a natural binomial multiplier, but its polynomial type is univariate. A
   multivariate-to-univariate encoding is not a definitional identification and does
   not supply the uniform multivariate degree/height estimate in ≤3 existing calls.
2. **Finite binomial product + scalar inequality:** the isolated raw theorem compiles
   from `Nat.choose_le_two_pow`, `Nat.pow_le_pow_right`, finite product comparison,
   and the newly proved additive-seminorm scalar helper. The code includes a real
   proof of the product estimate; these are not ≤3 calls supplying the whole theorem.
3. **Actual multivariate operator:** the generic proof uses project `coeff_hasseDeriv`
   and `hasseCoeff_le_two_pow`, then explicitly splits support membership and proves
   the zero case. Those project lemmas are proposed upstream content and cannot be
   counted as already-existing mathlib building blocks.
4. **L1 alternative:** `abs_coeff_le_normOne` plus `normOne_hasseDeriv_le` gives a bound
   involving normOne P; hB bounds this by #support*B. The unwanted cardinality factor
   prevents recovering the actual statement by that route.

Conclusion: **NOT-COMPOSABLE from existing mathlib in ≤3 calls** on the evidence checked.
No closing `simp [defs...]` is offered as a disguised NO verdict; no failed exact-search
is offered as a proof of absence. Existing norm_nsmul_le is a checked candidate ingredient,
not a complete estimate. Current proof and both consumers use only standard axioms.

## Phase 7 — Actionable verdict

**YES-but-generalise-first, MODERN-IDIOM.** Upstream the additive-seminorm coefficient bound,
after the algebraic multivariate Hasse API. The new mathematical interface is the uniform
size estimate for a coefficient-extracting differential operator, with no coefficient
collisions and no extra support factor. Existing univariate Hasse and norm scalar API
do not offer this law. The arbitrary additive seminorm is materially more useful than
the integer absolute value: it avoids multiplicativity/unit/topology assumptions and
can be applied separately to each coefficient seminorm.

Proposed exact upstream file: **Mathlib/Analysis/Polynomial/MvHasseDeriv.lean** (new leaf
importing the proposed Mathlib/Algebra/MvPolynomial/HasseDeriv.lean and seminorm API).
Proposed declaration: `MvPolynomial.seminorm_coeff_hasseDeriv_le`.
Proposed PR title: **feat(Analysis/Polynomial): bound coefficients of multivariate Hasse derivatives**.
Group with or follow the already accepted YES declarations {', '.join('`'+x+'`' for x in grouping)}.
Their acceptance is read from the fresh progress snapshot {link('accepted-yes-grouping.json')};
no useful lemma name is assumed to be YES. Keep purely algebraic Hasse API independent of
analysis imports. `Roth.abs_coeff_hasseDeriv_le` can remain a downstream exact integer
specialization while callers migrate; its spelling is not the recommended upstream API.

Before opening that PR:

- [ ] `/generalise Roth.abs_coeff_hasseDeriv_le` using the compiled additive-seminorm target;
  consider an additive-monoid size interface only with an equally useful existing bundle
  and fresh proof, without claiming an unverified weakening.
- [ ] `/cleanup Roth/CoeffNorm.lean Roth.abs_coeff_hasseDeriv_le`, then cleanup the new
  upstream analysis leaf, normalize natural-scalar spelling and check import fanout.
- [ ] Coordinate the algebraic Hasse dependency and finite binomial-product helper design;
  retain the actual proved coefficient bound rather than replacing it by an L1 bound.
- [ ] Select a reviewer from relevant recent commits; Moritz Firsching for the Hasse API,
  Moritz Doll or Eric Wieser for seminorm interface. Exact commit evidence is in
  {link('reviewer-git.json')}.

No human design question blocks completing this read-only assessment, and no cost-based
downgrade is applied. This verdict is independent of the prior binomial-factor assessment.

## Phase 8 — Verification and handoff

{link('verification.json')} lists exact accepted sources, requests, raw native receipts,
axiom declarations and separately rejected attempts. The initial generic attempt had an
incorrect add_le_add_right term order and recovered sorryAx; it is rejected. The corrected
`add_le_add ih le_rfl` proof and successful receipts are the only accepted generic evidence.
Raw import warming responses are not treated as completed proof checks.

Current hashes/bytes and integration destinations: {link('copy-manifest.json')}.
Portable read-only checker: {link('validate.py')}, invoked with the repository root as its
optional argument. It checks the current manifest (never substitutes the historical
worker manifest), all phases/search channels, standard axioms, raw no-Roth isolation,
exact canonical order/private-name mapping, source/pin identity, local links and secrets.
Root independently reviews and owns integration, acceptance, commits and pushes.
'''
(D/'report.md').write_text(report)
print('Report and structured phase artifacts written')
