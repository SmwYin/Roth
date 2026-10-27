# Full mathlibable assessment: `MvPolynomial.taylor_map`

Canonical declaration **67/293**, `Roth/Taylor.lean:157–159`. Verdict **BORDERLINE-needs-human**: the standard coefficient-change convenience law for a prospective named translation API. This completes the read-only assessment; the future upstream API questions below are not unfinished verification or a request to change production code.

## Phase 0: baseline and scope

The unchanged baseline commit `99f19fda4b3cbee38fc0d31af76075834f5cc265` built successfully: 2467 jobs, exit 0, no warnings/errors. All 17 production source/version-pin hashes were freshly compared and match that baseline ([build](../evidence/MvPolynomial.taylor_map/baseline-build.txt), [inputs](../evidence/MvPolynomial.taylor_map/inputs.json), [hash check](../evidence/MvPolynomial.taylor_map/input-hash-check.json)). Target resolves and native replay succeeds with standard axioms only. No `sorry`, new axiom or production edit is introduced. Taylor's module develops polynomial translation, its Hasse-coefficient identity, and bounded Taylor expansion.

## Phase 1: mathematical comprehension

For a homomorphism `f : R →+* S`, change all coefficients of a polynomial and all coordinates of its translation vector by `f`. Translating the changed polynomial is the same polynomial as first translating and then changing coefficients. No injectivity or surjectivity of `f`, inverses, characteristic, nonzero or finiteness hypotheses are needed: this is naturality of polynomial substitution.

Full statement, with section binders and independent universes exposed (native original type/print in [target receipt](../evidence/MvPolynomial.taylor_map/native-target-success.json)):

```lean
∀ {σ : Type u} {R : Type v} [CommSemiring R]
  {S : Type w} [CommSemiring S] (f : R →+* S)
  (α : σ → R) (P : MvPolynomial σ R),
  MvPolynomial.taylor (fun j ↦ f (α j)) (MvPolynomial.map f P) =
    MvPolynomial.map f (MvPolynomial.taylor α P)
```

`σ` indexes arbitrary variables; `R,S` are coefficient semirings; `f` is a bundled unital semiring homomorphism; `α` is a translation vector; `P` arbitrary polynomial. Only project dependency is `MvPolynomial.taylor`. The original proof unfolds translation and algebra evaluation, uses substitution/coefficient-map compatibility and normalizes the translated generators. Root replay does not call the target theorem; its direct proof constants were inspected with `allowOpaque := true` ([executed target](../evidence/MvPolynomial.taylor_map/native-target-executed.lean.txt)).

## Phase 2: preliminary checks

**SMALL**: a structural compatibility lemma, not a new structure or one of the module's named main Taylor-expansion results. Exhaustive literature width still applies. Phase 2b is **n/a**, because the target is a theorem, not a one-line data definition. Parent `taylor` was independently assessed BORDERLINE; that verdict is not inherited here: this is not a definitional glue lemma.

## Phase 3: exhaustive literature protocol

Each actual request, returned-response hash and byte count, source locator and concise summary is preserved; full returned search/article bodies are deliberately not archived. Returned URL queries/fragments are removed from locators, so no signed download credentials are stored. See [web0](../evidence/MvPolynomial.taylor_map/web0-metadata.json), [web4](../evidence/MvPolynomial.taylor_map/web4-metadata.json), [follow-up](../evidence/MvPolynomial.taylor_map/webfollow-metadata.json), [primary sources](../evidence/MvPolynomial.taylor_map/webprimary-metadata.json), and [local search](../evidence/MvPolynomial.taylor_map/rg-local-literature.json).

| Channel | Actual query/check | Finding and limitation |
|---|---|---|
| General web, specific | `multivariate polynomial translation commutes coefficient ring homomorphism` | Polynomial-map and translation material; Magma's primary handbook states that a multivariate polynomial homomorphism is specified by the coefficient map and variable images. |
| General web, general | `polynomial algebra base change substitution naturality universal property` | Universal polynomial-algebra/base-change formulation; Stacks 05G3 explicitly describes polynomial presentations after change of coefficients. |
| General web, alias | `Hasse Schmidt Taylor homomorphism functoriality ring maps` | Hasse–Schmidt/Taylor homomorphism context; no stronger characteristic-zero requirement for this compatibility identity. |
| Optional ChatGPT mathematics | `ask_chatgpt_math` | Unavailable/optional; not invoked, no substituted claim of expert verification. |
| Local references | `clean.tex` coefficient-map and Taylor searches | §1 implementation note lines154–155 explicitly requests coefficient-map compatibility; §4 explains `Pα(X)=P(X+α)`. [Excerpt](../evidence/MvPolynomial.taylor_map/clean-excerpts.tex.txt), [source hash](../evidence/MvPolynomial.taylor_map/local-literature.json). |
| nLab | `site:ncatlab.org/nlab polynomial algebra base change`; follow-up polynomial base-change universal property | Polynomial as free commutative algebra; universal-construction extension by variable images. Direct `polynomial` page open fails unsupported XHTML; do not represent that as full direct page access. |
| nCatLab/categorical | `site:ncatlab.org/nlab polynomial ring functor natural transformation` | Naturality and polynomial free-algebra substitution context. Polynomial endofunctors/containers and enriched-topos base change hits are distinct objects, not a proof of this law. |
| Stacks | `site:stacks.math.columbia.edu polynomial ring base change universal property`; directly open tag05G3 | [Definition10.14.1 and following polynomial-presentation remark](https://stacks.math.columbia.edu/tag/05G3) explain mapped polynomial coefficients over an arbitrary collection of variables. Not cited as an exact statement of this translation lemma. |
| MathOverflow | `site:mathoverflow.net polynomial substitution base change translation`; follow-up `site:mathoverflow.net polynomial ring universal property ring homomorphism` | Queries completed; no direct MO primary locator was returned/retained and no exact translation-specific statement was established. |
| Recent arXiv | `site:arxiv.org polynomial shift equivalence Hasse derivative 2022 2026` | [Chen–Du–Fang2204.06968](https://arxiv.org/abs/2204.06968), first submitted14April2022 and revised17March2025, is within five years. Current v3 title is *Symbolic Summation of Multivariate Rational Functions*, unlike the older search-index title; polynomial shifts are context, not source for coefficient-map naturality. 2026 sparse-shift and2024 GL-algebra hits are supplementary context, not generality proofs. |

Primary [Magma multivariate homomorphism documentation](https://docs.magma-maths.org/BasicRings/MultivariatePolynomialRings/operation.html#homomorphisms) supports the coefficient-map plus generator-image interpretation. Literature agrees on substitution naturality; familiar finite-variable field treatments are applications. Most general standard form is compatibility of arbitrary polynomial substitution and coefficient homomorphisms, already represented by mathlib's generic evaluation/map laws. No literature result proves removal of the current parent definition's commutativity interface.

## Phases 4a–4b: every parameter and verified generality

| Parameter/hypothesis | Role | Generality assessment |
|---|---|---|
| `σ : Type u` | Variables | Arbitrary, possibly infinite/empty; no `Fintype`, `DecidableEq` or inhabitation. Native raw substitution additionally permits independent target variable type `τ`. |
| `R : Type v`, `[CommSemiring R]` | Source coefficients | Includes positive characteristic, zero divisors and trivial semiring. No subtraction/division used. A native Semiring-only attempt cannot form the current `taylor` parent interface. |
| `S : Type w`, `[CommSemiring S]` | Target coefficients | Independent universe, same interface floor; target Semiring-only attempt also rejected by guarded native elaboration. |
| `f : R →+* S` | Coefficient change | Arbitrary bundled homomorphism, not an embedding, algebra isomorphism or characteristic-preserving extra assumption. |
| `α : σ → R` | Shift vector | Arbitrary, mapped coordinatewise; its mapping must not be omitted. |
| `P : MvPolynomial σ R` | Polynomial | Arbitrary; no degree/support/nonzero restrictions. |

**MAXIMALLY GENERAL within the fixed parent translation interface; zero verified mechanical hypothesis weakenings.** The probes establish interface constraints, not mathematical impossibility of a separately constructed noncommutative theory. Arbitrary substitution `g : σ → MvPolynomial τ R` works and is already `map_eval₂`; this is an existing abstract theorem, not a novel generalise-first contribution. A bundled RingHom commutative square follows from the fresh replay without extra assumptions; a change of presentation, not stronger mathematics. [Extra source and receipt](../evidence/MvPolynomial.taylor_map/native-extra-executed.lean.txt), [receipt](../evidence/MvPolynomial.taylor_map/native-extra-success.json).

## Phase 4c: nine modern-idiom checks

| # | Check | Answer, reformulation and downstream effect |
|---|---|---|
| 1 | Typeclasses versus bundled hypotheses | No improvement: coefficient classes and bundled `RingHom` already used. |
| 2 | Sequences/metrics versus filters | No: finite algebraic expressions, no topology. |
| 3 | Universal-property characterization | Yes, interpret as naturality of free commutative algebra; existing `map_eval₂`/`map_aeval` supply that abstraction. No new universal-property class needed. |
| 4 | Closure predicates versus bundled substructures | No: no closure predicate. Optional equality of bundled RingHom compositions is verified, useful for diagram rewriting. |
| 5 | Fields/vector spaces versus modules/semirings | No unused field/ring structure here; already commutative semirings. `Polynomial.map_taylor` is weaker Semiring only for a different univariate representation, not direct weakening. |
| 6 | Higher-categorical formulation | No verified benefit; natural transformation vocabulary alone does not justify new category infrastructure. |
| 7 | Concrete index generalization | No: arbitrary `σ`, not fixed natural variables. Generic substitution permits target `τ`, already in mathlib. |
| 8 | Concrete-via-abstract proof diagnostic | Yes: after unfolding `taylor`, its identifier disappears; proof is generic substitution compatibility plus generator normalization. [Diagnostic](../evidence/MvPolynomial.taylor_map/proof-body-diagnostic.json). Re-aim at existing `map_eval₂`; no missing abstract theorem. |
| 9 | False-generalization guard | No false generalization is accepted. Dropping the mapping of `α` changes the commutative square; coefficient-map injectivity is not introduced. Generic substitution and bundled square preserve the original as a specialization; neither is claimed definitionally identical to its translated-generator spelling. |

Modern idiom is **already available** generically. No novel modern restatement requiring YES-but-generalise-first. The prospective benefit of the named convenience law is convenient shift/base-change rewrites, not mathematical abstraction missing from mathlib.

## Phase 4.5: infrastructure risks

**n/a for theorem**: definitional equality, instance diamonds, coercion diamonds, reducibility, universe-instance ambiguity and representation/elaboration infrastructure are all inapplicable as new-definition risk rows. The theorem creates no definitions or instances. Actual coercion/independent-universe RingHom square elaborates successfully.

## Phase 4.6: all proof-strategy rows

| # | Question | Assessment |
|---|---|---|
| 1 | Epsilon/neighborhood versus filters | n/a, no topology. |
| 2 | Element arguments versus substructure inclusions | Generic substitution-map law is appropriate; optional bundled RingHom equality verified by extensionality, no substructure argument to replace. |
| 3 | Sequences versus nets | n/a, no analysis. |
| 4 | Object construction versus universal property | Existing free-algebra substitution naturality is the idiom; avoid independent monomial induction. |
| 5 | Missing helper that should exist | None needed: `map_eval₂`, `map_aeval` and generator-map laws already exist. |

Strategy **MATHLIB-IDIOMATIC**, with a more explicit narrow-normalization replay available. No missing-helper ticket, cost-based verdict or circular reuse of the assessed theorem.

## Phase 5: five actual mathlib methods on three forms

Complete raw API receipts: [formal searches](../evidence/MvPolynomial.taylor_map/formal-search.json). Every method was actually invoked, including local search; source searches are untruncated.

| Method | Current form | Literature-standard form | Abstract form |
|---|---|---|---|
| Lean Finder | translation/coefficient ring homomorphism; `Polynomial.map_taylor` hit | shift/base-change/naturality; related Weierstrass specializations | arbitrary substitution naturality; `eval₂_map`, `map_eval₂`, `map_eval₂Hom` hits |
| Loogle | equality between `aeval` and `map`; no exact hit | `"map_taylor"` gives univariate law and degreeLT variants | `"map_eval₂"` gives generic substitution and related matrix specializations |
| LeanSearch | multivariate Taylor coefficient map; map_eval₂ plus univariate hit | base-change shift naturality; polynomial shift equivalences and power-series substitution | evaluation/map compatibility; `map_bind₁`, `eval₂_map`, `map_eval₂` |
| `rg` | [current](../evidence/MvPolynomial.taylor_map/rg-current.json) | [literature](../evidence/MvPolynomial.taylor_map/rg-literature.json) | [abstract](../evidence/MvPolynomial.taylor_map/rg-abstract.json) |
| local symbol search | `taylor_map` resolves project target | `map_taylor` resolves Polynomial candidate | `map_eval₂` prefix route returns broad map_eval results; actual pinned source/native resolve exact candidates |

Local search reports **index unavailable**, so no empty local result is evidence of absence. External indexes may lag the pinned revision. Full qualified-name source search has no `MvPolynomial.taylor_map` hit in mathlib ([receipt](../evidence/MvPolynomial.taylor_map/rg-full-name.json)); this alone is not an absence proof.

Pinned candidates, inspected independently:

* `MvPolynomial.map_eval₂`, `Mathlib/Algebra/MvPolynomial/Eval.lean:365`: arbitrary source/target variable types and arbitrary substitution assignment. Native raw `substitution` is an **exact one-call** specialization. Target native print elides a long portion of its underlying proof; [full pinned module](../evidence/MvPolynomial.taylor_map/MvPolynomial-Eval-module.lean.txt) preserves the complete induction proof.
* `MvPolynomial.map_aeval`, same file:618: arbitrary RingHom after algebra evaluation. Actual native signature and proof inspected; a broad compatibility law, not normalized shift statement.
* `MvPolynomial.eval₂_map`, same file:441: evaluation after coefficient mapping; original replay uses it twice along with `map_eval₂` and generator-map facts.
* `Polynomial.map_taylor`, `Mathlib/Algebra/Polynomial/Taylor.lean:120`: both coefficient structures `[Semiring]`, same commutation law with the **opposite displayed orientation**, univariate representation only. Full native signature inspected, not a drop-in `MvPolynomial` theorem. [Pinned module](../evidence/MvPolynomial.taylor_map/Polynomial-Taylor-module.lean.txt).
* `MvPolynomial.map_bind₁`/`hom_bind₁`, `Mathlib/Algebra/MvPolynomial/Monad.lean:241/237`: source-inspected supplementary generic substitution variants. **Not imported/native-verified in the accepted current session**; not counted as an accepted direct replacement. [Pinned source](../evidence/MvPolynomial.taylor_map/MvPolynomial-Monad-module.lean.txt).

## Phase 5.5: statement shape

1. **Normal form:** law is an equality, with changed-coefficient translation on left and map-after-translation on right. `Polynomial.map_taylor` uses reverse orientation/name; upstream naming/orientation should be considered, not changed silently.
2. **Syntactic generality:** arbitrary substitution and arbitrary target variable type are already existing `map_eval₂`; bundled RingHom square is native verified. The translated-generator normalization remains propositional.
3. **Superfluous arguments:** no unused binders or assumptions; no finiteness/decidability/characteristic assumptions to remove. Explicit α and P are appropriate; f is arbitrary RingHom.

Verdict **ACCEPTABLE CURRENT SHAPE**, conditional on choosing a named translation API. No unverified restatement required for correctness.

## Phases 6.0 and 6: complete callers, inline audit and composition

| Source caller | Count | Refactor plan |
|---|---:|---|
| Production named callers | **0** | No caller edits required by deleting just this theorem; declaration itself is the only `taylor_map` occurrence. |

[Caller search](../evidence/MvPolynomial.taylor_map/rg-callers.json), [inline search](../evidence/MvPolynomial.taylor_map/rg-inline.json), [caller record](../evidence/MvPolynomial.taylor_map/callers.json). No independent inline rederivation found: the generic `map_eval₂` occurrence is the declaration's own proof. This is a source audit, not exhaustive opaque kernel or implicit-dependency closure. Unlike adjacent `taylor_zero`, this target is not tagged simp. Zero named callers is a limited API-usage signal, not proof of junk.

An isolated **mathlib-only** experiment defines `shift` using `aeval`, guards the missing project theorem, and verifies both the generic one-call law and the exact original-shaped shift law ([source](../evidence/MvPolynomial.taylor_map/native-raw-executed.lean.txt), [clean receipt](../evidence/MvPolynomial.taylor_map/native-raw-success.json)):

```lean
-- Generic substitution is exactly existing mathlib:
map f (aeval g P) = aeval (map f ∘ g) (map f P) := map_eval₂ f g P

-- Original shift law needs generator normalization:
change eval₂ C (fun j ↦ X j + C (f (α j))) (map f P) =
  map f (eval₂ C (fun j ↦ X j + C (α j)) P)
rw [map_eval₂]
congr 1
funext j
simp only [Function.comp_apply, map_add, map_X, map_C]
```

The accepted old-form route uses **four distinct mathematical facts** (`map_eval₂`, `map_add`, `map_X`, `map_C`), plus structural congruence/function extensionality. The generic law is not definitionally the normalized old statement. The original tactic proof uses five distinct mathematical facts, including two `eval₂_map` applications. No ≤3-fact exact old-form term has been established. A closing `simp [definitions,…]` is explicitly a **Phase6b BORDERLINE** case; its brevity is not a NO-composable certificate. The longer raw proof is also not evidence of mathematical difficulty: all content is generic naturality plus generator normalization.

Root also verified equality of RingHom compositions with all independent universes using the **fresh independent replay**, avoiding original target reuse. With no actual source callers, this is a representative bundled consumer experiment, not a claim that a production caller was migrated.

One initial raw preparation was rejected: omitted `noncomputable` and a loose unfolding/simp attempt hit the default 200000-heartbeat limit, yielding rejected unproved diagnostics. [Rejected source](../evidence/MvPolynomial.taylor_map/native-raw-rejected.lean.txt), [receipt](../evidence/MvPolynomial.taylor_map/native-raw-rejected.json). Corrected explicit `change` and narrow normalization pass without raised limits. Every accepted receipt is complete, success true, partial false, no errors/warnings/unproved declarations, axioms within `propext`, `Classical.choice`, `Quot.sound`. Rejection is not evidence of absence or accepted verification.

## Phases 7–8: verdict, gates and next action

**BORDERLINE-needs-human**. The exact arithmetic compatibility is standard and generic substitution naturality already exists. A named coefficient-change theorem can still be a reasonable law of an accepted translation API, but no nontrivial new theorem or missing abstract construction has been established. Generic exact hits do not erase the propositional translated-generator bridge. No mechanical weakening verifies, and no cost or inherited parent verdict drives this conclusion.

Future upstream design questions (not required input for this completed assessment):

1. If mathlib adopts named multivariate translation, should coefficient-map compatibility be an explicit convenience theorem alongside it?
2. Should its name/orientation match `Polynomial.map_taylor`, or prefer the current translation-after-map normal form?
3. Should the primary interface expose the bundled RingHom commutative square, with the pointwise theorem as a corollary, or keep generic `map_eval₂` as the main API?

**Next action:** retain the result in project-local `Roth/Taylor.lean` during this read-only overview; resolve upstream translation-API policy before proposing it. No production changes, new definitions, version changes or external PRs. If later declining the wrapper, there are zero explicit caller edits; generic substitution `map_eval₂` plus the displayed generator normalization is the concrete replacement route. This alternative local destination preserves readability while the parent API decision remains open.

All required phase evidence and supporting source/native receipts are tracked through [verification](../evidence/MvPolynomial.taylor_map/verification.json) and the [portable validator](../evidence/MvPolynomial.taylor_map/validate.py). `unresolved=[]` records completed assessment/verification, not a fictional upstream design decision. Root independently accepts before publication; progress may advance only after this package passes.
