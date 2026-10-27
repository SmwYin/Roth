# Roth.wronskian — full mathlibable assessment

**Verdict: BORDERLINE-needs-human.** This is the named Hasse Wronskian determinant for arbitrary finite polynomial families. Its data construction is a verified three-building-block expression, but its semantic/API role has substantial actual consumers and directly addresses mathlib's pinned n-tuple TODO. The remaining decision is the upstream API and normalization, not verification or development cost. All required phases complete; unresolved verification: []. This is a read-only assessment; future recommendations do not authorize migration.

## Phase 0 — baseline and scope

Canonical 41, public noncomputable definition at `Roth/Wronskian.lean:60`; no prefilter. [Baseline](../evidence/Roth.wronskian/baseline-build.txt) reports exit0, successful 2467-job build. [Fresh hashes](../evidence/Roth.wronskian/source-pin-hashes.json) match all 17 source/pin inputs to the shared baseline. Entire [declaring module](../evidence/Roth.wronskian/source-wronskian.lean.txt), [GenWronskian](../evidence/Roth.wronskian/caller-genwronskian.lean.txt) and [Separation](../evidence/Roth.wronskian/caller-separation.lean.txt) were read. No sorry in target. Root alone ran native Lean. Parent matrix's BORDERLINE verdict was read as context and not inherited.

## Phase 1 — comprehension

For l polynomials φν, take the determinant of the l×l polynomial matrix with entry HasseDerivμ(φν). Rows start at order 0, columns enumerate the family. The output is a polynomial, with no evaluation point, independence assumption or characteristic restriction. For l = 0 the determinant is1, for l = 1 it is φ0, and for l = 2 it agrees exactly with the existing binary polynomial Wronskian.

Full native type:
```lean
@Roth.wronskian : {K : Type u_1} → [inst : Field K] → {l : ℕ} →
  (Fin l → K[X]) → K[X]
```
K is universe polymorphic; Field supplies the coefficient structure; l determines consecutive derivative orders and square size; φ is the essential family input. The implementation is `(Roth.wronskianMatrix φ).det`. Native [focused type/body/axioms](../evidence/Roth.wronskian/native-target-focused.json), [full target receipt](../evidence/Roth.wronskian/native-target-success.json) and [executed snapshot](../evidence/Roth.wronskian/native-target-executed.lean.txt) establish the exact target and rfl bridge. This definition asserts no vanishing criterion.

## Phase 2 — preliminary checks

BIG: introduces a classical named determinant, listed among the module's main definitions. ONE-LINER WITH-EXEMPTION, body count 1.

| Exemption | Applies? | Evidence |
|---|---|---|
| Defeq abuse avoidance | no | Exact original-to-expanded bridge is rfl; consumers explicitly unfold rather than needing a special sealed barrier. |
| Typeclass diamonds | no | A polynomial value definition introduces no instance/carrier; no competing structure is selected by its name. |
| Semantic intent/API stability | yes | Six theorems in this module and three caller declarations elsewhere use the anchor; the independence criterion and separation factorization are naturally stated using a Wronskian name. |

The exemption avoids dismissing a named concept by body length. It does not negate the raw composition result.

## Phase 3 — exhaustive literature

[Full channel table/synthesis](../evidence/Roth.wronskian/literature-summary.md), exact requests and returned-response metadata: [web1](../evidence/Roth.wronskian/web1-metadata.json), [web2](../evidence/Roth.wronskian/web2-metadata.json), [web3](../evidence/Roth.wronskian/web3-metadata.json), [web4](../evidence/Roth.wronskian/web4-metadata.json). Three distinct general-web forms and every named channel ran; optional ask_chatgpt_math unavailable. nLab indexed access succeeded, direct open failed400 unsupported XHTML and is honestly recorded. No web bodies or credential-bearing URLs are archived.

Local clean.tex §2 defines exactly the factorial-normalized determinant over rational polynomials; [excerpt](../evidence/Roth.wronskian/local-literature.txt). Guruswami–Kopparty's *Explicit Subspace Designs*, §3 Definition9 and Lemma10, gives Hasse derivative rows and then their determinant, explicitly discussing ordinary/Hasse scaling. [Primary paper](https://www.math.toronto.edu/swastik/subspace-designs.pdf). Principal-parts universal properties provide broader geometric context rather than a ready-made determinant. [Stacks09CH](https://stacks.math.columbia.edu/tag/09CH). Recent n-ary polynomial Wronskian usage appears in Kiselev 2025. [Primary abstract](https://arxiv.org/abs/2510.02145).

Standard concept confirmed, with normalization variants. Ordinary derivatives multiply row μ by μ!, so they cannot silently replace Hasse derivatives. Independence theorems have characteristic/degree conditions, which must not be imported into this definition or assumed without proof.

## Phase 4a–b — parameters and generality

| Parameter | Current interface | Tested weakening/alternative | Finding |
|---|---|---|---|
| K : Type u | Universe polymorphic | Type u and explicit Type1 examples | Already general; no forced small universe. |
| Field K | Needed by unchanged matrix parent | Expanded standalone body over CommRing R | Compiles, exact Field bridge rfl. No inverses/division/nonzero/cancellation needed. **Not** a literal binder drop with unchanged Field-only `Roth.wronskianMatrix`. |
| Commutativity and subtraction | Consequences of Field | CommRing floor for present Matrix.det | Pinned det signature requires CommRing; Semiring supports Hasse entries but not this determinant interface. No Semiring/noncommutative determinant weakening claimed. |
| l : ℕ | Implicit arbitrary size | l = 0,1,2 checks | Empty family allowed, no positivity needed. |
| Fin l index | Consecutive derivative orders and square size | Arbitrary finite ι plus order : ι→ℕ | New `WOrder` constructor compiles; original is its rfl specialization using Fin.val. This is expanded representation with extra data, not simply dropping Fin. |
| φ | Explicit polynomial family | Retained; arbitrary operator/differential-ring idea examined | Essential; replacing polynomials/operators requires larger API, not a mechanical hypothesis edit. |
| noncomputable | Inherited Hasse/determinant construction | Retained | Matches pinned noncomputable infrastructure. |

Standalone verified replacement:
```lean
noncomputable def hasseWronskian {R : Type*} [CommRing R] {l : ℕ}
    (φ : Fin l → R[X]) : R[X] :=
  (Matrix.of fun i j : Fin l ↦ Polynomial.hasseDeriv i (φ j)).det
```
Exact executed name `WronskianRaw.W`; [strongest source](../evidence/Roth.wronskian/native-order-executed.lean.txt), [receipt](../evidence/Roth.wronskian/native-order-success.json). STRICTLY NARROWER coefficient interface; CommRing standalone construction verified. Replacing Field in the current body requires generalizing/inlining its matrix parent; this is not an authorized production edit or an unsupported claim that every downstream theorem weakens. Such joint interface design is a larger decision than the false-positive “drop this binder unchanged” route. Cost is CHEAP for standalone construction and not a verdict factor.

## Phase 4c — nine modern-idiom checks

| # | Check | Answer, reformulation and downstream consequence |
|---|---|---|
|1| Typeclass preambles | no: coefficient structure already uses a typeclass. No new class needed. |
|2| Filters/nets | no: finite algebraic data, no limit or topology. |
|3| Universal property | optional jet/principal-parts perspective was investigated; introduces a different interface, not a verified existing equivalent. No concrete shorter present construction established. |
|4| Bundled substructure | no set-with-closure predicate to replace. Alternating/multilinear packaging could expose generic laws, but Hasse derivatives are R-linear rather than R[X]-linear; a naive polynomial-scalar pullback is invalid. No uncompiled bundling claim. |
|5| Module/ring hierarchy | yes: CommRing expanded construction gives integer-coefficient Wronskians directly, verified by an ℤ example. Matrix parent's Field constraint must be addressed explicitly. |
|6| Higher categories | no: no categorical statement or concrete downstream benefit requiring such machinery. |
|7| Concrete indices | yes, optional: native WOrder over arbitrary finite ι with selected row orders; Fin.val bridge rfl. Enables generalized derivative row choices. Consecutive row μ still needs an order map; replacing ℕ by an arbitrary group loses meaning. |
|8| Concrete-via-abstract | definition, no theorem proof to unfold. K and φ are variables, not named witnesses; the body contains determinant once. Matrix.det is the abstract constructor already reused; this diagnostic provides composition evidence rather than a new abstract theorem. |
|9| False-generalization guard | CommRing expanded body and order-map specialization preserve the object exactly. Ordinary derivative substitution is rejected: over ℤ, the Hasse determinant of [1,X,X²] is1 and the ordinary determinant is2, both compiled. No characteristic-free identification. |

Modern gains: integer coefficient input and optional chosen-order API. These are real new inputs; neither a category slogan nor a new scratch helper counts as preexisting mathlib replacement. The l = 2 bridge is special and does not imply arbitrary-l equality with ordinary derivative normalization.

## Phase 4.5 — infrastructure risks

| Risk | Verdict | Concrete audit |
|---|---|---|
| Typeclass diamond | none | Defines a value with existing Field/Polynomial/Matrix instances. Native `#synth CommRing (Polynomial ℤ)` succeeds through existing ring structure; no new instance path. |
| Reducibility leak | low | Ordinary semireducible noncomputable def; rfl bridges succeed without reducible attribute. Unfolding exposes determinant, whose expansion should remain explicit. |
| Noncanonical unfolding | low | No simp attribute forces determinant expansion. Current coefficient/column/row proofs deliberately unfold the name; native Fin0/1/2 computations show intended behavior. |
| Instance priority collision | none | Not an instance, has no priority or instance head. |
| Universe polymorphism | none | Native Type u and Type1 constructions compile; Fin l contributes no coefficient-universe equation. |
| Coercion ambiguity | none | No CoeFun/CoeSort declaration; standard LinearMap application supplies Hasse entries and Matrix.det supplies result. Direct and order-map bridges compile. |

Overall LOW, no HIGH rows. Semantic/API exemption is not a diamond workaround.

## Phase 4.6 — five proof-strategy checks

| # | Check | Finding |
|---|---|---|
|1| ε-δ versus filters | n/a: no topology/proof. |
|2| Elements versus submodule inclusions | no element proof; direct determinant is idiomatic. Independence statements are separate declarations. |
|3| Sequences versus nets | n/a: no limits. |
|4| Construction versus universal property | Concrete polynomial-valued determinant is intentional; principal parts would organize a broader theory, not shorten this data constructor. |
|5| Missing helper lemmas | None needed for construction; normalized n-ary named API and its compatibility laws are the upstream TODO/design scope. |

MATHLIB-IDIOMATIC as a construction. No proof to golf and no cost-based downgrade.

## Phase 5 — actual five-method search on three forms

[Complete formal requests/receipts](../evidence/Roth.wronskian/formal-search-raw.json), [exact source searches](../evidence/Roth.wronskian/source-search-raw.json), [pinned excerpts](../evidence/Roth.wronskian/mathlib-source-excerpts.lean.txt) and [hashes](../evidence/Roth.wronskian/mathlib-source-hashes.json).

| Method | Current form | Literature-standard form | Abstract form | Finding |
|---|---|---|---|---|
| Finder | Hasse derivative Wronskian determinant of finite univariate family | Generalized Wronskian determinant divided derivatives over commutative ring | Alternating multilinear determinant of linear maps/Taylor jets | Binary Wronskian and bilinear form; abstract detRowAlternating/detAux candidates. |
| LeanSearch | Same natural-language current query | Same standard query | Same abstract query | Hasse derivative, binary API; alternating/multilinear API, not a named arbitrary-family Hasse determinant. |
| Loogle | `Polynomial.hasseDeriv, Matrix.det` | `"wronskian"` | `Matrix.detRowAlternating` | Current query empty; binary Wronskian; generic determinant alternating map. |
| rg | Target/full candidate names untruncated | All Wronskian/wronskian occurrences | Hasse, Taylor coefficient, determinant and alternating constructor signatures | Existing three raw building blocks, binary API and explicit n-tuple TODO. |
| local name | wronskian | hasseDeriv | detRowAlternating | Target/binary/derivative/abstract declarations; index unavailable, source-assisted results do not establish absence. |

All five methods actually ran at all three forms. External index may differ from pinned mathlib. Finder descriptions occasionally reverse the binary sign; the actual pinned body and native fin2 proof control the conclusion. Positive signatures `Matrix.det`, `Matrix.detRowAlternating`, `Polynomial.factorial_smul_hasseDeriv`, `Polynomial.wronskian` checked natively. Binary wronskian takes two polynomials, not an arbitrary finite family. The pinned module TODO expressly asks for n-tuple Wronskians. No search-only absence theorem is claimed; generic raw construction is positively compiled. detRowAlternating is generic determinant infrastructure, not an existing Hasse-family definition. LinearMap.detAux requires endomorphism/basis data, unavailable from an arbitrary polynomial family without additional construction. No circular project theorem was used to build W.

## Phase 5.5 — statement shape

Normal forms considered: determinant of Hasse matrix; ordinary derivative determinant with factorial row scaling; generalized chosen-order determinant; geometric/evaluated jets. Current direct Hasse form matches the project's normalization. RHS normal-form rule for equality/iff statements is n/a for a definition; the rfl bridge displays the expanded constructor on RHS. The binary compatibility theorem directs the Fin2 special case toward existing `Polynomial.wronskian`.

Syntactic generality: implicit l and explicit φ are convenient; new coefficient class CommRing is appropriate for a standalone API. WOrder is a verified expanded representation, optional rather than forced for existing consumers. Superfluous argument audit: Field's division/inverses/nonzero assumptions unnecessary after resolving parent interface; commutative-ring structure used by det; K/universe/l/φ essential. No characteristic/degree/positivity assumptions to drop. Overall RESTATE-BEFORE-SHIP: a distinct normalized-family name over CommRing, with explicit binary compatibility, if maintainers elect to expose it. Existing `Polynomial.wronskian` already owns the binary signature and must not silently be replaced.

## Phase 6.0 — all explicit callers and inline audit

External-to-module K=5 executable occurrences in 3 declarations across 2 files. Total13 executable occurrences in 9 caller declarations, excluding definition/comments/docstrings; source occurrences are not the kernel/simp dependency closure. Names such as `wronskian_ne_zero_of_linearIndependent` are not counted as extra references to the target identifier.

| Caller | Exact references | Future inline/refactor plan if name rejected |
|---|---|---|
| wronskian_eq_zero_of_not_linearIndependent | Wronskian:66 | Statement uses `(wronskianMatrix φ).det`; proof already enters determinant infrastructure. |
| coeff_wronskian_of_natDegree_injective | Wronskian:123,139 | Expand determinant in statement, remove `wronskian` from rw list. |
| wronskian_ne_zero_of_natDegree_injective | Wronskian:149 | Expand determinant in statement; coefficient theorem call unchanged in form after corresponding restatement. |
| wronskian_update_sub_smul | Wronskian:159 twice | Expand both determinant expressions; existing det-column update proof remains. |
| wronskian_ne_zero_of_linearIndependent | Wronskian:206 | Expand statement determinant; induction uses correspondingly restated lemmas. |
| wronskian_eq_zero_iff | Wronskian:220 | Expand statement determinant; same two implication lemmas. |
| private wronskian_kronecker_eq_sum_aux | GenWronskian:241,244 | Expand determinant in statement, remove target name from simp list. |
| det_hasseDeriv_separated | Separation:356,357 | Expand polynomial factor determinant; remove target unfolding rewrite. |
| private exists_rat_factors_det_hasseDeriv_aux | Separation:528 | Replace local hFmap factor with same determinant; existing factorization theorem specializes accordingly. |

This is a future per-caller plan, not a tested whole-project migration. If the matrix name is also rejected, use its Matrix.of expression consistently. If upstream name chosen, replace the determinant expression with that name and use its exact bridge; no ordinary-derivative substitution.

Inline audit searched Matrix.of/Hasse/determinants across Roth. genWronskian uses multivariate selected differential operators; separation uses mixed partial matrices. These are related but distinct, not bypasses of the exact consecutive univariate target. No exact inline duplicate outside its consumers found. Nonzero external uses establish active API, not dead code.

## Phase 6 — actual composition experiments

1. Exact raw data: `(Matrix.of fun i j : Fin l ↦ Polynomial.hasseDeriv i (φ j)).det`. Three existing mathlib building blocks: `Matrix.det`, `Matrix.of`, `Polynomial.hasseDeriv`; lambdas/application are syntax. Native W construction, `direct` rfl and original Field bridge all succeed. Project parent matrix is **not** counted as a mathlib building block. This is COMPOSABLE as data.
2. Existing binary candidate: `W ![a,b] = Polynomial.wronskian a b` closes by `simp [W, Matrix.det_fin_two, hasseDeriv_zero, hasseDeriv_one, Polynomial.wronskian, mul_comm]`, verified without project imports. It covers precisely l = 2, requires normalization, and is not a one-call arbitrary-arity replacement. Under Phase6b, a closing simp-only bridge is BORDERLINE evidence, not automatic NO.
3. General order representation: WOrder compiles and `W φ = WOrder Fin.val φ` is rfl. This is newly constructed scratch infrastructure, not existing mathlib replacement. Fin0/1 evaluations also compile.
4. Normalization guard: Hasse [1,X,X²] determinant=1 and ordinary determinant=2 over ℤ, compiled. Binary equality cannot be extrapolated. Characteristic-sensitive vanishing theorems remain outside this definition assessment.

Exact experiments and axiom prints are in [strongest executed source](../evidence/Roth.wronskian/native-order-executed.lean.txt) and [full success receipt](../evidence/Roth.wronskian/native-order-success.json). No exact? timeout is repeated: this is a data-construction assessment with a positive constructor term, not a theorem-absence claim.

## Phase 7 — actionable verdict

**BORDERLINE-needs-human**, independently derived. NO-mathlib-has-it is unsupported for arbitrary l: binary API is a partial match. NO-composable has positive raw-constructor evidence but competes with the Phase2 semantic exemption, many actual users and pinned named n-tuple TODO. A YES generalise-first based solely on deleting Field would misrepresent the unchanged matrix parent's constraint. The assessment therefore surfaces actual design questions, not cost or technical incompleteness:

1. Should the existing n-tuple TODO be fulfilled by a named normalized-family determinant (`Polynomial.hasseWronskian` or similar) over CommRing, with its exact Fin2 binary compatibility theorem?
2. Should that family API expose consecutive Fin rows first, or make chosen finite row orders primary and consecutive rows a specialization?
3. Should the Hasse matrix be public alongside the determinant, or inline inside it, with ordinary-derivative normalization exposed through separate scaling lemmas?

These are future upstream questions; no user input is needed to finish this read-only assessment. Default local recommendation: retain the actively used anchor in `Roth/Wronskian.lean` until the coherent API is settled; record verified standalone CommRing opportunity without changing production.

Conditional upstream destination `Mathlib/RingTheory/Polynomial/Wronskian.lean`; possible PR title “feat(Polynomial): add Hasse Wronskians of finite families”. Existing accepted YES entries in progress are multivariate Hasse API, not this determinant or its matrix. A coherent future family determinant/matrix contribution could use those compatibility results separately, but is not already an accepted YES grouping. Future checklist `/generalise Roth.wronskian` with parent interface explicitly scoped; `/cleanup Roth/Wronskian.lean Roth.wronskian`; settle naming/normalization before upstreaming. Relevant reviewer lead: Moritz Firsching's Hasse derivative map commit 334438dace, with Jineon Baek/Seewoo Lee as binary-module author context; availability unassessed and nobody contacted. See [history context](../evidence/Roth.wronskian/reviewer-history.txt).

## Phase 8 — verification and handoff

[Verification map](../evidence/Roth.wronskian/verification.json), [assessment](../evidence/Roth.wronskian/assessment.json), [current manifest](../evidence/Roth.wronskian/copy-manifest.json), [portable read-only validator](../evidence/Roth.wronskian/validate.py). Accepted target, raw, normalization and order receipts are terminal success with no errors/warnings, no partial/timeouts, standard axioms only (`propext`, `Classical.choice`, `Quot.sound`). Strongest isolated code guards `#check_failure Roth.wronskian`, imports mathlib only, and constructs the object independently. No sorry, unsafe, native_decide, new axiom or raised resource limit. No rejected native attempts. Source/pin17 hashes and explicit caller archives freshly match; current manifest hashes every supporting artifact. Root acceptance pending. No production source/pin or Git mutation by worker.
