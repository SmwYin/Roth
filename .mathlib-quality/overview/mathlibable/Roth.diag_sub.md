# Roth.diag_sub — declaration 95/293

**Verdict: NO-mathlib-has-it.** Existing `map_sub` is exactly the more general theorem. This conclusion is independent of the parent `Roth.diag` assessment (NO-composable-from-mathlib), and requires no new upstream lemma.

## Phase 0 — baseline

Reusable clean build: [baseline receipt](../evidence/Roth.diag_sub/baseline-build.txt); all **17** source/pin hashes freshly match shared baseline ([input check](../evidence/Roth.diag_sub/input-hash-check.json), [full inputs](../evidence/Roth.diag_sub/inputs.json)). Declaration resolves at `Roth/CoeffNorm.lean:199`, a theorem with no sorry. The whole declaring module and whole sole caller module were read and archived: [CoeffNorm](../evidence/Roth.diag_sub/source-module.lean.txt), [MainLemma](../evidence/Roth.diag_sub/source-caller.lean.txt). Module concerns integer coefficient norms, diagonal substitution, and evaluation estimates.

## Phase 1 — mathematical content and native statement

Sending every variable of an integer multivariate polynomial to one indeterminate respects differences: `(P-Q)(x,…,x)=P(x,…,x)-Q(x,…,x)`. The variable type is arbitrary, with no finiteness assumptions. Both polynomial inputs are arbitrary; there are no propositional hypotheses. The docstring calls this “additive”; the literal statement is subtraction preservation.

```lean
∀ {σ : Type u_1} (P Q : MvPolynomial σ ℤ), Roth.diag (P - Q) = Roth.diag P - Roth.diag Q
```

[Original native receipt](../evidence/Roth.diag_sub/native-original-success.json) prints the complete type and proof, with only standard axioms. The elaborated proof is `fun {σ} P Q ↦ map_sub (MvPolynomial.aeval fun x ↦ Polynomial.X) P Q`. Only project dependency is the definition `Roth.diag`; no project theorem is used.

## Phase 2 — preliminary classification

SMALL: elementary homomorphism helper, neither named theorem nor main result nor new structure. Definition-only one-line test and all three definition exemptions are n/a because this is a theorem. The full exhaustive protocol still ran.

## Phase 3 — literature, every required channel

Exact requests, response SHA256/bytes/status and source locators are archived without full web bodies in [general](../evidence/Roth.diag_sub/web-0.json), [specialist sites](../evidence/Roth.diag_sub/web-1.json), [MO/arXiv](../evidence/Roth.diag_sub/web-2.json), [direct accesses](../evidence/Roth.diag_sub/web-3.json), [Stacks correction](../evidence/Roth.diag_sub/web-4.json).

| Channel | Actual query / outcome |
|---|---|
| General specific | `polynomial diagonal substitution ring homomorphism subtraction`: evaluation/substitution homomorphisms found. |
| General abstract | `universal property polynomial algebra evaluation homomorphism additive`: free-algebra universal property. |
| General aliases | `multivariate polynomial substitution preserves subtraction`: substitution principle, evaluation homomorphism. |
| ChatGPT MCP | n/a: ask_chatgpt_math unavailable; no simulated response. |
| Local clean.tex | Actual rg plus [source metadata](../evidence/Roth.diag_sub/local-literature-source.json) and [excerpt](../evidence/Roth.diag_sub/local-literature-excerpt.txt). Lemma9 takes differences of W and compares diagonal Hasse remainders; preservation is implicit. |
| nLab | Proper site query found polynomial page. Direct fetch failed unsupported XHTML content type; search summaries only. |
| nCatLab | Proper `/ncatlab` site query produced mainly nLab spillover; direct polynomial page inaccessible. No independent source claim. |
| Stacks | Site query found uses of the universal property. Initial direct guessed tag00E1 proved unrelated and is rejected. Corrected search identifies Lemma98.10.1 tag07XB, contextual use of lifting an algebra map. |
| MathOverflow | Proper site query found polynomial substitution discussion; contextual algebra-map viewpoint, no new subtraction theorem claim. |
| Recent arXiv | Actual date-bounded query after2021-10-27 before2026-10-28; specialised substitution/homomorphism papers found, no relevant strengthening of basic map law. |

The standard concept is the evaluation/substitution algebra homomorphism. [Leinster lecture notes §3.1.7](https://www.math.mcgill.ca/darmon/courses/24-25/algebra4/leinster.pdf) formulate evaluation and substitution through the universal property. [Armstrong §18.1](https://www.math.miami.edu/~armstrong/562sp24/562sp24textbook.pdf) states the polynomial universal property. [Stacks Lemma98.10.1](https://stacks.math.columbia.edu/tag/07XB) uses that property to lift an algebra map. These support arbitrary rings/algebras, with subtraction inherited from the additive group map. The inference to diagonal substitution is ours: choose every variable image equal to X. There is no historical-formulation claim beyond the sources actually checked.

## Phase 4a — parameters and Phase 4b — generality

| Parameter | Assessment |
|---|---|
| σ : Type* | Already arbitrary; retain universe polymorphism, no Fintype/DecidableEq. |
| P,Q | Essential arbitrary inputs; cannot remove either without changing the law. |
| ℤ | Fixed by parent `diag` interface, not a removable typeclass hypothesis. Expanded aeval form works over arbitrary CommRing R. |
| Codomain | Polynomial R can be replaced by any commutative R-algebra A and any variable assignment. |
| Multiplicative structure | Unneeded by the preservation theorem itself: an additive homomorphism suffices. |

Expanded forms are genuinely checked, not claimed mechanical edits of fixed `Roth.diag`: [raw source](../evidence/Roth.diag_sub/native-raw-executed.lean.txt) and [successful receipt](../evidence/Roth.diag_sub/native-raw-success.json) verify arbitrary CommRing diagonal, arbitrary substitution, and AddGroupHom abstraction. No semiring truncated-subtraction claim is made. Generic `map_sub` is even weaker on the codomain (`SubtractionMonoid`) than our AddGroupHom probe. Generality: strictly narrower than standard, and the broader law already exists.

## Phase 4c — all nine modern idiom checks

| Question | Answer | Proposed form / consequence |
|---|---|---|
| Typeclasses | yes | Use existing AddMonoidHomClass with FunLike, AddGroup domain and SubtractionMonoid codomain; no explicit closure hypotheses. Every additive bundled map uses map_sub. |
| Filters | no | No topology or convergence. n/a |
| Universal properties | yes | aeval already supplies the universal algebra homomorphism; use its generic law. Arbitrary substitutions inherit subtraction automatically. |
| Bundled substructures | no | No subset or closure predicate; aeval is already bundled. n/a |
| Hierarchy weakening | yes | Replace integer coefficients by CommRing R in expanded representation. Arbitrary polynomial coefficient rings. |
| Higher categories | no | Elementary homomorphism law has no additional higher coherence requirement. n/a |
| Concrete index | no | σ is already arbitrary; ℤ is the coefficient object, treated in row5. n/a |
| Concrete via abstract | yes | Body map_sub _ _ _ contains zero occurrences of diag: it uses only additive homomorphism structure. Specialise existing map_sub to AddGroupHom or aeval. |
| False generalisation guard | PASS | Expanded CommRing diagonal specialises back at R=ℤ. Abstract map_sub forgets multiplicative structure but retains the identical subtraction law. Do not claim CommSemiring truncated subtraction preserves it. Original content preserved. |

Concrete diagnostic: the one proof-body line `map_sub _ _ _` contains zero occurrences of `diag`; abstraction fires decisively. The real organisational improvement is using the existing homomorphism class law, which also serves all other additive maps. No new modernisation theorem is missing.

## Phase 4.5 — infrastructure risk

n/a: theorem. Each of six rows (typeclass diamond, reducibility leak, noncanonical unfolding, priority collision, universe issues, coercion ambiguity) is n/a: the proof creates no instance, definition, reducibility rule, or coercion. The parent's representation is separately assessed. [All structured rows](../evidence/Roth.diag_sub/generality.json).

## Phase 4.6 — all five proof-strategy checks

| Row | Answer / rationale |
|---|---|
| Topology | no: No neighbourhood arguments. |
| Point-free algebra | no: Already a direct generic homomorphism-law application; ideal inclusions add no value. |
| Analysis | no: No sequence or limit. |
| Universal property | no: Construction supplied by aeval; no new construction proof. |
| Missing helpers | no: map_sub already supplies the whole law. |

Current strategy MATHLIB-IDIOMATIC: a direct existing law. Missing helper API: none; cost plays no role.

## Phase 5 — actual five-method search on all three forms

[All twelve exact formal requests and raw complete responses](../evidence/Roth.diag_sub/formal-search.json) cover current diagonal subtraction, standard algebra substitution, and abstract additive-homomorphism subtraction.

| Method | Results |
|---|---|
| Finder | Current: MvPolynomial.eval₂_sub; standard: Polynomial.aeval_sub; abstract: map_sub. |
| Loogle | `MvPolynomial.aeval, _ - _`; `RingHom, _ - _`; `map_sub`. Generic query finds map_sub, ring query RingHom.map_sub. |
| LeanSearch | All three natural-language queries executed; standard finds Polynomial.aeval_sub, abstract additive-homomorphism infrastructure. |
| rg | [current](../evidence/Roth.diag_sub/rg-current.json), [standard](../evidence/Roth.diag_sub/rg-literature.json), [abstract](../evidence/Roth.diag_sub/rg-abstract.json), [full names](../evidence/Roth.diag_sub/rg-full-name.json). |
| Local names | diag_sub, aeval, map_sub queries executed; all three returned index unavailable (source-backed hits still returned), so no absence claim follows from the index. |

Pinned source: `Mathlib/Algebra/Group/Hom/Defs.lean:460–462` generates additive `map_sub` from `map_div` via `to_additive`; textual absence of `theorem map_sub` is therefore immaterial. `Mathlib/Algebra/MvPolynomial/Eval.lean:569` bundles aeval as an algebra homomorphism. [Pinned source hashes and archives](../evidence/Roth.diag_sub/mathlib-inputs.json). External search snapshots are discovery evidence; native pinned verification establishes applicability.

## Phase 5.5 — statement shape, all three checks

Normal form: `f (P-Q)=f P-f Q`, with separate images on RHS, is standard `map_sub`. Equivalent forms tried: expanded diagonal aeval, arbitrary variable assignment, and arbitrary additive homomorphism. Syntactic generality: use the generic bundled-map theorem; no manual coefficient proof or bespoke additive predicate. Superfluous arguments: none within the original fixed interface; integer coefficients are fixed representation, not a droppable hypothesis. Locally the subtraction name is appropriate; docstring could say “preserves subtraction” if retained. Overall: reuse existing normal form.

## Phase 6.0 — complete explicit source and canonical proof callers

[Source grep](../evidence/Roth.diag_sub/rg-callers.json) finds the declaration and exactly one explicit caller: `Roth/MainLemma.lean:408`, `Roth.eval_hasseDeriv_sub_eq_zero`, whose simp list contains diag_sub alongside map_sub. [Inline search](../evidence/Roth.diag_sub/rg-inline.json) finds no separate re-derivation of this exact law. [Caller inventory](../evidence/Roth.diag_sub/callers.json). The fresh canonical array was generated directly from tracked JSON, preserving private names; the accepted execution verifies **293 entries, 293 unique, 293 present, 293 values**, in exact canonical order. It finds exactly one direct proof consumer, the same theorem. This is direct dependency evidence, not opaque transitive/simp closure.

## Phase 6 — actual composition and caller replacement

The theorem itself is one existing-call specialisation (accepted verbatim):

```lean
  map_sub (MvPolynomial.aeval fun _ ↦ Polynomial.X) P Q
```

[Accepted full caller replay and audit](../evidence/Roth.diag_sub/native-consumers-executed.lean.txt) and [native receipt](../evidence/Roth.diag_sub/native-consumers-success.json) avoid diag_sub entirely. Replace the sole caller's inner proof by introducing the syntactically expanded hypothesis before simplification:

```lean
    have hdiag :
        (aeval (fun _ ↦ (Polynomial.X : Polynomial ℤ)) (hasseDeriv j W')) %ₘ f =
          (aeval (fun _ ↦ (Polynomial.X : Polynomial ℤ)) (hasseDeriv j W'')) %ₘ f := h
    simp [map_sub, diag, Polynomial.sub_modByMonic, hdiag]
```

The original attempt simply replaced diag_sub by diag; it failed because h no longer matched the unfolded remainder. [Rejected receipt](../evidence/Roth.diag_sub/rejected-consumers-receipt.json) is preserved separately, including unsolved goal/unused simp argument/recovered sorryAx; it is never accepted evidence. The typed hdiag fixes the representation mismatch and full replay closes with standard axioms. This caller simplification is a trivial simp composition, which alone would be Phase6b BORDERLINE; the verdict instead rests on the independently checked exact one-call theorem `map_sub`, not on the caller's simp proof.

## Phase 7 — actionable verdict

**NO-mathlib-has-it**, existing declaration `map_sub`, source `Mathlib/Algebra/Group/Hom/Defs.lean:460–462` (generated additive law). It applies to any FunLike additive homomorphism class from an AddGroup to a SubtractionMonoid, strictly beyond this polynomial instance. The direct term above proves the literal project statement; no bridge theorem or new helper is required. Parent diag's NO-composable verdict does not force this law into the same bucket.

Future cleanup: update the sole MainLemma408 caller using the accepted typed-hdiag replay, then delete diag_sub. No other named or canonical direct proof caller needs changes. Leave diag unchanged during this read-only assessment; its independent assessment is already recorded at canonical76. This package changes no production code. Alternative local destination if a semantic alias is deliberately retained: `Roth/CoeffNorm.lean` beside diag, as project convenience only; Archive and upstream duplication have no justification. [Accepted YES grouping snapshot](../evidence/Roth.diag_sub/accepted-yes-grouping.json) was freshly read; no PR or grouping is proposed for this NO result.

## Phase 8 — delivery and verification

[Assessment](../evidence/Roth.diag_sub/assessment.json), [overview entry](../evidence/Roth.diag_sub/overview-entry.json), [exact verification ledger](../evidence/Roth.diag_sub/verification.json), [portable validator](../evidence/Roth.diag_sub/validate.py) and [current manifest](../evidence/Roth.diag_sub/copy-manifest.json). Three accepted native sets, one rejected set, standard axioms only, no partial or warming results treated as success. Root acceptance remains pending independent review. All phases complete; unresolved verification is empty. Production, pins, Git and progress unchanged by worker.
