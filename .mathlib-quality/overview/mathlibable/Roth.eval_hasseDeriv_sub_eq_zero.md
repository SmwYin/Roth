# Roth.eval_hasseDeriv_sub_eq_zero - canonical251/293

**Verdict: BORDERLINE-needs-human.** Retain the local helper while deciding the upstream API grain.
The scalar equal-remainder/evaluation mechanism is already supplied by polynomial APIs. The full
Hasse/diagonal/coefficient-change conclusion additionally requires substantive normalization and
project Hasse transport. A new generic observation proof is useful evidence of semantic generality,
not an existing mathlib replacement. This completed assessment has three future API questions;
none is a missing verification gate or a request to stop the overview.

## Phase0 - baseline and resolution

The shared baseline completed successfully with 2467 jobs, exit0 and no reported warnings/errors.
All 17 production source/pin hashes freshly match it. Reuse is therefore valid; the accepted
Theta file-end build228 also passed. No additional file-end build is due here (next266).
[Baseline](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/baseline-build.txt), [fresh inputs](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/inputs.json), [input manifest](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/input-manifest.json).
Unique public theorem at Roth/MainLemma.lean402. The entire762-line declaring module was read,
including its private caller and complete main-lemma continuation. Sources/pins and Git remain
unchanged. [Whole module](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/source-MainLemma.lean.txt), [target excerpt](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/target-excerpt.lean.txt), [production status](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/production-status.json).

## Phase1 - mathematical statement and native elaborated type

Let f be an integer polynomial and alpha a root in any commutative ring S. If the diagonal
specializations of the j-th Hasse derivatives of W' and W'' have equal remainders modulo f,
then the j-th Hasse derivative of their difference, after changing integer coefficients to S,
vanishes at the constant point with every coordinate alpha. Variables may form any type and
j is finitely supported; neither finite variables nor monicity of f is needed.

The argument first uses Hasse linearity, diagonal additivity and subtraction of remainders to
show f divides the diagonal derivative of W'-W''. The polynomial evaluation homomorphism kills
this multiple because it kills f. Hasse coefficient-change naturality and composition of
multivariate substitution with univariate evaluation identify the resulting value with the
claimed multivariate evaluation. No factorial division or characteristic-zero step occurs.

Full type, obtained with Lean.getConstInfo and pp.funBinderTypes=true (not by splitting a
#print at an internal let):

```lean
∀ {σ : Type u_1} {S : Type u_2} [inst : CommRing S] {f : Polynomial ℤ} {α : S},
  (Polynomial.aeval α) f = 0 →
    ∀ {W' W'' : MvPolynomial σ ℤ} {j : σ →₀ ℕ},
      Roth.diag ((hasseDeriv j) W') %ₘ f = Roth.diag ((hasseDeriv j) W'') %ₘ f →
        (eval fun (x : σ) ↦ α) ((hasseDeriv j) ((map (Int.castRingHom S)) (W' - W''))) = 0
```

The two universe parameters are independent. Every parameter is material: sigma chooses variables,
S the evaluation ring, f the modulus, alpha its root, W'/W'' the inputs and j the selected Hasse
order. The hypotheses are the root equation and the selected remainder equality. There are no
nonzero, degree, finiteness, domain, order, monicity or positivity conditions.
[Original exact fullmodule replay](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/original-executed.lean.txt), [raw receipt](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/original-receipt.json), [native type](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/native-type.json).
The complete original kernel body printed without elision; both original and replay use only
propext, Classical.choice and Quot.sound. Fresh replay type identity and exact canonical 293
order/uniqueness/presence/kernel-values pass. One direct canonical value consumer and zero direct
type consumers are found. [Canonical consumers](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/canonical-consumers.json), [dependencies](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/dependencies.json).

Source-body project references are diag, diag_sub, hasseDeriv and hasseDeriv_map. Direct kernel
constants include those same interfaces; the full lists, including mathematical instances and
generated transport terms, are archived. Source lexical, source statement, direct kernel type,
direct kernel body and simp/transitive scopes are distinguished. The target has no simp attribute.
No full transitive kernel or global simp dependency closure is claimed.

## Phase2 - size and definition-only check

SMALL: a conversion helper in the auxiliary-polynomial construction, not a named theorem,
new structure or main result. Definition-only one-line and its defeq/diamond/API exemptions are
N/A because this is a theorem. Short proof spelling does not prefilter the assessment.

## Phase3 - exhaustive literature

All named channels and three actual general queries ran. Each linked web record retains exact
requests, returned UTF8 response SHA256/byte count/status, clean titles/URLs/locators and an original
short summary; full external bodies are not archived. Search rank/freshness is not publication date.

| Channel | Actual query/action | Finding and limit |
|---|---|---|
| General specific | Hasse derivatives polynomial congruence equal remainders vanishing root diagonal Roth auxiliary polynomial | Hasse and auxiliary polynomial context; no exact complete bundle identified. [Evidence](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/web-general1.json). |
| General standard | polynomial remainder theorem evaluation homomorphism quotient commutative ring arbitrary root | Remainder/evaluation and quotient formulations; distinguish noncommutative skew-polynomial hits. [Evidence](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/web-general2.json). |
| General aliases | Hasse Schmidt derivatives higher derivations arbitrary commutative rings vanishing ideals | Higher derivation literature supports characteristic-free formulation; no factorial division. [Evidence](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/web-general3.json). |
| ChatGPT mathematical MCP | Unavailable: ask_chatgpt_math is not an enabled tool | Optional channel skipped honestly. |
| Local reference | clean.tex lines1491-1515, plus actual rg receipt | Section6 proof of Lemma9 explicitly takes the difference, uses divisibility by f, linearity and root evaluation for vanishing. [Excerpt](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/literature-local-excerpt.txt), [hash](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/literature-local-input.json). |
| nLab | site:ncatlab.org/nlab polynomial ring evaluation universal property | Polynomial entry uses the free commutative algebra over arbitrary commutative rings. [Evidence](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/web-nlab.json). |
| Distinct nCatLab | site:ncatlab.org/ncatlab polynomial evaluation quotient ring | Returned nLab spillover, including modular polynomial; no exact nCatLab namespace hit. [Evidence](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/web-ncatlab.json). |
| Stacks | site:stacks.math.columbia.edu polynomial evaluation quotient ring root | Root and quotient surrounding algebra; no exact Hasse remainder lemma. A guessed tag00E5 open concerns Spec(R/I), retained as background only and excluded as a replacement. [Evidence](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/web-stacks.json), [direct access](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/web-primary.json). |
| MathOverflow | site:mathoverflow.net Hasse derivatives vanishing polynomial roots | Mostly ordinary derivative/root discussions; no exact full statement verified. [Evidence](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/web-mathoverflow.json). |
| Recent arXiv | site:arxiv.org Hasse derivatives polynomial vanishing multiplicities after:2021-10-29 before:2026-10-30 | He-Pham-Xu2022 explicitly use Hasse derivatives for multiple roots; newer symbolic-power and unrelated Hesse hits are not exact replacements. [Evidence](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/web-arxiv.json). |

Primary inspected source: [He, Pham and Xu, Universality for low degree factors of random
polynomials over finite fields](https://arxiv.org/abs/2201.06156), abstract and submission history:
submitted16Jan2022, revised23Feb2022. Its use of Hasse derivatives handles multiple-root statistics;
it does not supply this theorem or prescribe its exact abstraction. [nLab polynomial](https://ncatlab.org/nlab/show/polynomial),
Definitions and meanings, supports the universal-property viewpoint. The local paper is the exact
application source. Standard concepts are polynomial congruence, root evaluation, and Hasse higher
derivatives. Inference from these sources to arbitrary bundled additive observations is our
algebraic analysis, verified below, rather than a claim that a source states that new helper.

## Phase4a-4b - all parameters and verified generality

| Parameter/hypothesis | Current boundary | Concrete analysis/verification |
|---|---|---|
| Variable type sigma | Arbitrary Type | Already arbitrary; no finite/decidable/nonempty assumption to remove. |
| Multiorder j | Finitely supported natural multiindex | Hasse definition needs nonnegative finite multiorders. Replacing by an arbitrary group index changes the operator; rejected as false generalization. |
| Integer source coefficients | Fixed integers | Verified same Hasse/diagonal theorem over arbitrary CommRing R and CommRing S with Algebra R S; exact theorem below. |
| Target S | Arbitrary CommRing | Literal MvPolynomial S and coefficient map from integers need the ring/commutative structure. No domain/CharZero/Nontrivial assumptions. A separate bundled observation theorem works with Ring S. This is a representation generality, not a claim the literal syntax supports arbitrary noncommutative MvPolynomial coefficients. |
| f | Arbitrary polynomial, possibly nonmonic/zero/one | No monicity required by either dvd_modByMonic_iff_dvd or pinned root-evaluation law. Prior collision theorem249 uses monicity to recover coefficients; that premise is not inherited here. |
| Root equation | Evaluation of f is zero | Necessary: f=1, W'=1,W''=0,j=0 over integers gives equal zero remainders but value1. Both scalar and exact Hasse guards compile. |
| Remainder equality | One chosen j | Necessary: f=X,alpha=0, constants1/0,j=0 have root but unequal remainders and value1. Scalar inequality and exact Hasse value guards compile separately. |
| W',W'' | Arbitrary polynomials | No distinctness or box membership needed. |
| Constant point | Every coordinate alpha | Diagonal specialization fixes this semantic relation. Arbitrary points require changing the observation map, not silently dropping the diagonal connection. |

**Verified coefficient generality** (complete proof in composition source):

```lean
theorem generalized {σ R S : Type*} [CommRing R] [CommRing S] [Algebra R S]
    {f : Polynomial R} {α : S} (hfα : Polynomial.aeval α f = 0)
    {W' W'' : MvPolynomial σ R} {j : σ →₀ ℕ}
    (h : aeval (fun _ ↦ Polynomial.X) (hasseDeriv j W') %ₘ f =
      aeval (fun _ ↦ Polynomial.X) (hasseDeriv j W'') %ₘ f) :
    eval (fun _ ↦ α) (hasseDeriv j (map (algebraMap R S) (W' - W''))) = 0
```

**Verified semantic abstraction** (new scratch theorem, not existing mathlib):

```lean
theorem observe [Ring R] [Ring S] [AddGroup A] (D : A →+ Polynomial R)
    (e : Polynomial R →+* S) {f : Polynomial R} (hf : e f = 0) {p q : A}
    (h : D p %ₘ f = D q %ₘ f) : e (D (p - q)) = 0
```

The latter uses a bundled additive map D into a polynomial ring and a bundled RingHom e killing f.
It proves e(a mod f)=e(a) from modByMonic_eq_sub_mul_div and homomorphism laws, then transports
remainder equality and subtraction. This works for arbitrary Ring R, Ring S and AddGroup A.
Specializing D to diagonal-after-Hasse and e to aeval recovers the exact original theorem.
[Isolated complete source](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/isolated-executed.lean.txt), [receipt](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/isolated-receipt.json), [original recovery source](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/recovery-executed.lean.txt),
[receipt](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/recovery-receipt.json), [generality/direct experiment](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/composition-executed.lean.txt), [receipt](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/composition-receipt.json).
The original recovery type is checked after fresh universe-level instantiation. A rejected raw
comparison used fixed universe parameter names from separately elaborated declarations; those
names differ after the generic declaration, while the displayed/full instantiated signatures agree.
No claim of changed binders is made from that rejected diagnostic.

Generality status: STRICTLY NARROWER in coefficients/observation interface, with actual proofs;
no unsupported literal S typeclass weakening. All proofs preserve zero-ring and positive-characteristic
cases. The broader observation is a reusable semantic parameter; integers here are a coefficient
representation, not an irreducible mathematical constant. This does not by itself prove that the
most abstract helper deserves a public name or should replace the coordinate Hasse API.

## Phase4c - all nine modern-idiom rows

| # | Diagnostic | Answer and concrete consequence |
|---|---|---|
|1| Typeclasses/instances | Existing CommRing and Algebra express scalar structure; generic extension uses them without new instances. |
|2| Filters/nets | No: finite algebraic substitution, no convergence. |
|3| Universal property | Yes: bundled aeval/eval homomorphisms organize diagonal/evaluation composition. Enables comp_aeval_apply directly. |
|4| Bundled substructure | Optional kernel/ideal inclusion captures annihilation; the caller supplies remainder equality, so bundling it first adds transport rather than removing a premise. No new ideal API claim. |
|5| Hierarchy weakening | Generic observations only require AddGroup A and Ring R/S. Literal Hasse version retains CommRing coefficients and target. |
|6| Higher categories | No: no categorical construction or coherence problem. |
|7| Concrete index | Integer coefficient ring generalizes; natural multiindex is the actual divided-derivative order and cannot be arbitrary group-valued without changing mathematics. |
|8| Concrete-via-abstract | Diagnostic fires: proof never inspects integer coefficients or binomial factors, only additive/naturality laws. diag has one body line in the divisibility expression and one unfolding line; Hasse appears structurally then disappears after normalization. Verified D/e theorem captures these exact properties and recovers original. |
|9| False-generalization guard | Retain D additivity, e multiplicativity, e(f)=0 and equal remainders. Dropping root/equality is refuted natively. Ordinary derivatives/factorial inversion would lose positive-characteristic content and are rejected. |

Modern idiom exists and is a mathematical organization improvement: reusable observations and
coefficient base change compose with AddMonoidHom.comp, RingHom and aeval. The new generic proofs
are not already existing lemmas; no cost-based verdict follows from their availability.

## Phase4.5 - six infrastructure risks

All six are N/A for this theorem: typeclass diamonds (no instance), reducibility leaks (no data
construction), noncanonical unfolding (no new definition), instance priority collision (none),
universe-polymorphism infrastructure (no new typeclass path), and coercion ambiguity (none added).
The universe comparison correction above is verification plumbing, not a mathematical assumption.

## Phase4.6 - all five proof-strategy checks

| # | Question | Finding |
|---|---|---|
|1| Epsilon-delta versus filters | N/A algebra. |
|2| Element proof versus inclusions | Divisibility/kernel annihilation is idiomatic; equal-remainder eval route avoids an intermediate divisibility witness. |
|3| Sequences versus nets | N/A. |
|4| Construction versus universal property | aeval composition is the correct universal-property interface; no object construction. |
|5| Missing helper | Possible equal-remainder evaluation companion or diagonal evaluation across coefficients; observation helper is newly proved and its upstream value remains a design question. |

Strategy verdict: MATHLIB-IDIOMATIC, with verified direct evaluation alternative. Both paths need
the same coefficient/Hasse/diagonal normalization. Generalizing the observation does not make
that normalization definitional or furnish an existing full replacement.

## Phase5 - full fifteen-cell formal search

| Method | Current form | Literature standard form | Abstract form |
|---|---|---|---|
| Finder | Equal diagonal Hasse remainders/root | Equal polynomial remainders/root evaluations | Ring hom killing divisor |
| Loogle | Polynomial.aeval, divisibility, zero | Polynomial.eval₂ plus modByMonic | RingHom plus divisibility/zero |
| LeanSearch | Current Hasse vanishing | Equal-remainder evaluation | Observation factors through quotient |
| Source rg | Full target/eval_diag/hasseDeriv_map | eval₂_modByMonic/sub_modByMonic/dvd_mod | map/eval zero from divisibility |
| Local name | eval_hasseDeriv_sub_eq_zero | modByMonic | eq_zero_of_dvd |

[Matrix](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/formal-search-matrix.json) links all 15 complete raw request/result receipts. Local index reports unavailable
or error, with fallback items; this is not absence evidence. Finder's abstract hit has an older
monicity-requiring signature. Loogle and, decisively, pinned native #check show no monicity in
this pin. No result from the external index is silently treated as pinned source.

Positive native/pinned sources: Polynomial.eval₂_modByMonic_eq_self_of_root (Div636),
Polynomial.dvd_modByMonic_iff_dvd (Div269), Polynomial.sub_modByMonic (Div724),
Polynomial.aeval_eq_zero_of_dvd_aeval_eq_zero (AlgebraMap511), and
MvPolynomial.comp_aeval_apply (MvPolynomial/Eval). Full candidate modules/hashes retained.
[Full-name grep](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/full-name-search.json) has no exact target declaration in mathlib. Isolated #check_failure
also shows neither the target nor project MvPolynomial.hasseDeriv is imported. This is a precise
import-environment boundary, not proof of global mathematical absence. Repeated broad exact?
searches after the known default200k Hasse search exhaustion were not repeated or raised.
Native generic-route proofs test the actual positive candidate mechanisms instead.

## Phase5.5 - all three statement-shape checks

1. Normal form: equal remainders, divisibility of a difference, and equality of evaluated values
are related formulations. Pinned modByMonic/eval₂ is the scalar normal form; the current conclusion
is appropriate for index vanishing. No orthogonal equivalence API proposed. The RHS is zero.
2. Syntactic generality: original root/equality hypotheses fit the caller; the generalized Hasse
form removes integer-only coefficients; observation form accepts a bundled map. All alternatives
are actually compiled. Arbitrary e is more reusable but requires supplying the bridge D/e at the
Hasse caller. Original recovery shows exactly that cost without hiding it in a new axiom.
3. Superfluous arguments: no extraneous binders detected; root and equality guards are explicit.
No monicity/finiteness/CharZero binder can be removed because none exists. Literal ring floor and
semantic observation generality are distinguished above.

## Phase6.0 - complete actual caller and inline audit

| Caller | Source invocation | Purpose and actual inlining |
|---|---|---|
| private Roth.exists_mem_RSet_le_index_aux | MainLemma567, fun d hd hw maps selected hWeq to eval_hasseDeriv_sub_eq_zero | Supply h=hWeq d(hJ d hd hw), prove f divides diagonal derivative of W'-W'', then evaluate/root-normalize. Whole original caller and the entire remainder of MainLemma are replayed, not only its final fragment. |

One actual proof use, zero uses outside the declaring file, zero direct type consumers. The command's
internal count excluding the declaring file is0; this is not the same as zero total uses. Fresh
rg --no-ignore and git grep agree with canonical kernel-value enumeration. No independent inline
rederivation of the complete theorem was found. [Callers](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/callers.json), [lexical](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/source-search.json),
[tracked](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/tracked-source-search.json), [inline audit](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/inline-search.json).

[Full inlined module source](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/inline-executed.lean.txt), [receipt](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/inline-receipt.json) retain the private caller's original
signature, verify no target constant in its kernel value and compile through main_lemma using only
standard axioms. Thus it is locally inlineable, not dead code. This is not a claim that inlining
its proof turns project Hasse lemmas into existing mathlib building blocks.

## Phase6 - actual composition experiments

Attempt1, original route: dvd_modByMonic_iff_dvd plus sub_modByMonic and additive normalization,
then aeval_eq_zero_of_dvd_aeval_eq_zero, followed by hasseDeriv_map, eval_map and comp_aeval_apply
normalization. Native full original replay succeeds, but this exceeds three existing calls and
uses project Hasse transport.

Attempt2, direct route: two calls to existing eval₂_modByMonic_eq_self_of_root, congrArg on the
remainder equality, trans/symm transport, sub_eq_zero, and the complete Hasse/coefficient/diagonal
evaluation bridge. The isolated scalar eval_eq_of_mod_eq is an explicitly new helper composed from
those calls; the project direct theorem includes that helper and the full bridge. The helper is
not counted as one existing mathlib call. Direct whole theorem closes cleanly and preserves all
assumptions, but there is no verified <=3-existing-call whole-target term.

The complete tested direct body is preserved verbatim in composition-executed.lean.txt. Its
first line calls the new eval_eq_of_mod_eq helper, whose exact tested proof is:

```lean
  exact (Polynomial.eval₂_modByMonic_eq_self_of_root (p := p) hf).symm.trans
    ((congrArg (Polynomial.eval₂ g x) h).trans
      (Polynomial.eval₂_modByMonic_eq_self_of_root (p := q) hf))
```

Instantiating p and q at the two diagonal Hasse polynomials supplies scalar evaluation equality,
then direct changes eval₂ to aeval and uses sub_eq_zero.mpr before the final bridge. Thus the
actual successful experiment is a real proof with normalization, not a bounded term whose only
issue is counting how often a symbol occurs. The original complete bounded-term aspiration
fails to account for those bridges; no existing theorem found supplies them all at once.

Attempt3, generic observe: modByMonic_eq_sub_mul_div with map_sub/map_mul and root annihilation,
then additive transport. This is a new generic proof, not an existing mathlib law. Exact original
recovery is clean. The arbitrary-coefficient Hasse version is also clean.

Composition conclusion: **NOT-COMPOSABLE under the strict <=3 existing-mathlib-call criterion**.
The scalar core is short existing-law composition, and the remaining bridge is a normalization
proof using project API. A closing simp/rewriting spelling is not automatically a NO verdict;
Phase6b leaves such convenience/API grain to judgment. Neither the usefulness of main_lemma nor
the short surface proof independently determines the bucket.

Pairwise moral-duplication comparison:

| Pair | Same statement? | Same proof? | Decision |
|---|---|---|---|
| Target vs aeval_eq_zero_of_dvd_aeval_eq_zero | No: former starts with remainder equality and returns mapped multivariate Hasse value | Same terminal annihilation leaf only | Reuse scalar theorem; preserve bridge evidence. |
| Target vs eval₂_modByMonic_eq_self_of_root | No: one polynomial remainder eval vs difference of two Hasse observations | Direct route uses law twice | Potential generic evaluation companion, not exact replacement. |
| Target vs diag_sub | No: additivity only | Reused normalization leaf; diag_sub is map_sub | No duplicate whole statement. |
| Target vs hasseDeriv_map | No: coefficient naturality only | Reused transport leaf | Existing project parent API is not mathlib replacement. |
| Target vs new observe/generalized | Exact specialization after bridge | Generic scalar proof plus explicit new normalization | Verified restatement; public grain remains judgment. |

Parent assessments were freshly read: diag NO-composable (aeval), diag_sub NO-mathlib-has-it
(map_sub), Hasse and Hasse map YES-add-as-is. None supplies an existing full analogous law for
this combined target, so the parent re-aim rule does not automatically force NO. No verdict inherited.

## Phase7 - actionable verdict and future questions

**BORDERLINE-needs-human.** The theorem combines a wholly standard polynomial remainder/root
mechanism with a reusable but specialized Hasse/diagonal transport bridge. The current integer
coefficient restriction is genuinely removable, and both broader observation and precise Hasse
coefficient statements are proved. Existing scalar APIs are enough for the core but do not alone
replace the complete old form within the strict composition gate. A local one-use convenience
lemma is defensible; the evidence does not settle whether mathlib should expose the full Hasse
corollary, a scalar equal-remainder evaluation companion, or just the diagonal-evaluation bridge.
This is an upstream audience/API-grain judgment, not uncertainty about correctness or cost.

1. Should a generic equal-remainder evaluation law be public Polynomial API, given the existing
   root-preservation law and short trans/congrArg derivation?
2. Should a coefficient-independent diagonal-evaluation bridge accompany the multivariate Hasse
   API, leaving this one-use vanishing corollary local?
3. If a Hasse-specific corollary is desired, should its public hypothesis be equal remainders or
   divisibility of the diagonal difference, with the other form derived at callers?

Concrete action now: retain Roth/MainLemma local helper, or optionally inline its verified body
at the sole private caller. For an upstream proposal, first choose the scalar versus Hasse grain;
use the verified arbitrary-R form rather than integer-only data. Candidate homes are existing
Mathlib/Algebra/Polynomial/Div.lean for the scalar companion and a future
Mathlib/Algebra/MvPolynomial/HasseDeriv.lean for a Hasse corollary after the parent API exists.
These are provisional design destinations, not a YES PR proposal. No external action is performed.

No auto-removal as junk, no cost-based downgrade, no monicity accidentally introduced. Future
questions concern optional upstream decisions only; this assessment is completed and root-reviewable.

## Phase8 - evidence, verification and freeze

[Assessment](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/assessment.json), [verification](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/verification.json), [portable validator](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/validate.py),
[current copy manifest](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/copy-manifest.json), [final validation](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/final-validation.json), [secret guard](../evidence/Roth.eval_hasseDeriv_sub_eq_zero/secret-guard.json).
Six accepted native sources/receipts include original fullmodule audit, isolated generic/guard
proofs, original recovery, whole-caller inline, exact metadata and generalized/direct composition.
No warnings/errors, partial results, recovered sorryAx, unsafe trust or resource-limit raises are
accepted. Rejected drafts are archived separately (wrong Ring-level use of CommRing APIs, raw
universe-name comparison, and namespace ambiguity), with complete sources and raw diagnostics.
An initial isolated rejected call's receipt serialization failed; the exact rejected source was
re-executed warm and its complete raw failure archived, explicitly not an accepted proof.
A preliminary diagnostic request merely observed historical250 inlined scratch; it is not evidence
for251. Final source/request receipts are target-specific and scoped to the new native region.

The portable validator checks the current manifest in scratch and simulated integrated layouts,
not the historical worker manifest. Root independently reviews before any publication. No production
Lean/pin, shared import prefix, tracked overview/progress or Git write was made by this worker.
