# `Roth.eta_lt_gam_iff` — canonical235

**BORDERLINE-needs-human.** The exact named bridge has two real consumers and records the paper's equation (38). Its mathematical core is existing additive-order API; the precise 2/4 coefficient spelling also needs arithmetic normalization. All assessment phases and native verification are complete; the three future upstream-design questions below do not block this read-only assessment. Production Lean, pins, nine disk imports, shared18 and Git were not changed.

## Phase 0 — baseline

The fresh [17-input comparison](../evidence/Roth.eta_lt_gam_iff/inputs.json) matches the tracked [baseline manifest](../evidence/Roth.eta_lt_gam_iff/input-manifest.json) exactly. The reusable [baseline build](../evidence/Roth.eta_lt_gam_iff/baseline-build.txt) completed all 2467 jobs without warnings/errors. Target resolves at MainLemma:100–102, theorem, no sorry. The whole MainLemma develops Roth's Lemma 9 via a polynomial pigeonhole construction and derivative extraction; this target only translates its parameter condition. The original complete module was replayed under `Gap235Original`, target alone renamed `replay`.

[Exact original execution](../evidence/Roth.eta_lt_gam_iff/original-executed.lean.txt), [complete native receipt](../evidence/Roth.eta_lt_gam_iff/original-receipt.json), [canonical order](../evidence/Roth.eta_lt_gam_iff/canonical-snapshot.json), [preparation checks](../evidence/Roth.eta_lt_gam_iff/preparation-checks.json). No file-end build is due at235 (last accepted boundary228, next266).

## Phase 1 — comprehend

For any real δ and naturals n,m, let λ=4(1+3δ)n√m, γ=(m−λ)/2 and η=10^m δ^((1/2)^m). Then η+2(1+3δ)n√m<m/2 exactly when η<γ. Dividing λ by two gives the error term; translation of a strict inequality supplies the equivalence. No property of the real-power expression defining η is used.

Full native kernel type (obtained with `Lean.getConstInfo` and `pp.funBinderTypes`, not by splitting a printer message at `:=`):

```lean
∀ (δ : ℝ) (n m : ℕ),
  Roth.eta δ m + 2 * (1 + 3 * δ) * ↑n * √↑m < ↑m / 2 ↔ Roth.eta δ m < Roth.gam δ n m
```

Parameters: δ is a scalar perturbation; n a polynomial-degree parameter; m a dimension. No hypotheses besides their types. Source proof uses `gam` and `lam`; `eta` is in the statement. Direct kernel body uses the generated `Roth.eta_lt_gam_iff._proof_1_3`; this differs from source lexical dependencies. The [full target printer](../evidence/Roth.eta_lt_gam_iff/original-receipt.json) has no printer-elision marker and prints that wrapper, not expanded generated `grind` internals. The separate [project body-edge traversal](../evidence/Roth.eta_lt_gam_iff/project-receipt.json) follows Roth-prefixed body edges and shows eta/gam/lam and their generated helpers. It is not a traversal of all imported mathlib constants.

## Phase 2 — preliminary checks

SMALL: a parameter-conversion helper, neither a named theorem nor a module main result nor a new structure. Phase2b definition-only one-line test: n/a, theorem. A one-line tactic proof is not itself a NO criterion. Semantic naming is nevertheless concretely useful: exists_delta uses the bridge to prove a denominator nonzero for continuity, and roth_of_isIntegral uses it to clear the positive denominator in the final contradiction. This supports a project-local API name, not by itself a general upstream API.

## Phase 3 — exhaustive literature

Every named channel was actually checked; exact requests, response SHA256/byte counts/status, clean titles and URLs, and original summaries are preserved. Full web bodies are not archived. The original local paper is the exact source; supplementary web sources only establish context/abstraction.

| Channel | Exact query / locator | Finding |
|---|---|---|
| General specific | `Roth theorem "Inequality" "eta" "gamma" main lemma parameters` | Broad Roth and unrelated eta/gamma results; no exact equivalence. |
| General abstract | `ordered field addition subtraction division strict inequality equivalence` | Ordered-field arithmetic; primary university course notes give translation and positive scaling. |
| General alias/source | `Roth lemma 9 lambda gamma eta parameter inequality 30 38` | No exact named independent scalar theorem. |
| Local reference | clean.tex §6, eqs.(30),(34)–(36),(38), lines1334–1359 | Exact parameter definitions and equivalence; [local excerpt](../evidence/Roth.eta_lt_gam_iff/local-excerpt.tex.txt). |
| ChatGPT math | unavailable | Optional `ask_chatgpt_math` tool absent. |
| nLab | `site:ncatlab.org/nlab ordered field addition inequality` | [Ordered field](https://ncatlab.org/nlab/show/ordered%2Bfield), Definition; compatible strict order is the abstract setting. |
| nCatLab distinct | `site:ncatlab.org/ncatlab ordered field order translation` | Returned /nlab pages, no in-namespace result; no categorical upgrade established. |
| Stacks | `site:stacks.math.columbia.edu ordered field inequality` | Field/valuation material, e.g. [Examples of fields,09FF](https://stacks.math.columbia.edu/tag/09FF); no Roth scalar bridge. |
| MathOverflow | `site:mathoverflow.net Roth theorem parameters main lemma` | [Optimal Roth-type result](https://mathoverflow.net/questions/332190/optimal-roth-type-result-in-diophantine-approximation), effectiveness discussion; no competing scalar law. |
| Recent arXiv | `site:arxiv.org Roth theorem formalizing after:2021-10-28 before:2026-10-29` | [2207.07499](https://arxiv.org/abs/2207.07499) concerns the different arithmetic-progression Roth theorem. |
| Refined recent arXiv and primary access | `site:arxiv.org "Roth" "Diophantine" "formalization" after:2021-10-28 before:2026-10-29` | No results; opening [Penn notes](https://www2.math.upenn.edu/~gressman/analysis/01-orderedfields.html) returned403; only initial indexed excerpts available. |

Receipts: [general](../evidence/Roth.eta_lt_gam_iff/web-general.json), [nLab](../evidence/Roth.eta_lt_gam_iff/nlab.json), [nCatLab](../evidence/Roth.eta_lt_gam_iff/ncatlab.json), [Stacks](../evidence/Roth.eta_lt_gam_iff/stacks.json), [MO](../evidence/Roth.eta_lt_gam_iff/mathoverflow.json), [arXiv](../evidence/Roth.eta_lt_gam_iff/arxiv.json), [refinement/access failure](../evidence/Roth.eta_lt_gam_iff/primary.json), [local search](../evidence/Roth.eta_lt_gam_iff/local-literature.json). No malformed site query was used. Query noise and access failure do not establish absence. The exact local formulation is a paper-specific parameter bridge; the standard general mathematics is translation invariance of strict order in an additive group and distributivity of division over subtraction. No historical evolution of this elementary law was established by the search.

## Phase 4a — generality dimensions

| Parameter / feature | Current | Verified broader form / constraint |
|---|---|---|
| δ | arbitrary ℝ, no sign condition | η can be independent e; no δ-positivity needed. |
| n | ℕ degree parameter | Abstract scalar error b in the field law. Dropping n from the unchanged concrete signature is meaningless: it occurs in γ/error. |
| m | ℕ dimension | Arbitrary scalar c in the field law; no m>0 required for original equivalence. |
| eta formula | fixed real power, constants10 and1/2 | `arbitrary_eta` replaces it by any e:ℝ; its constants play no role. |
| sqrt and natural coercions | fixed concrete representation | Treat `(1+3δ)n√m` as b; no analytic theorem or completeness needed. |
| constants2,4 | linked by division by2 | Cannot vary independently; certified `false_coefficient` counterexample. |
| ℝ | concrete scalar field | `Field K`, `LinearOrder K`, `IsStrictOrderedRing K` generic proof compiles. |
| order hypotheses | none explicit | Underlying translation requires only `AddGroup G`, `LT G`, `AddRightStrictMono G`. |
| strict conclusion | both sides strict | Weak analogue independently verified, but replacing only one side loses equivalence; keep strict original semantics. |
| universes / unused binders | concrete types | Abstract G/K universe-polymorphic; no unused explicit arguments/classes in original. |

## Phase 4b — verified generality

The scalar mathematical relation is STRICTLY NARROWER than its abstract form. This is not a claim that `gam` or real `sqrt` can be kept unchanged over an arbitrary field: those concrete definitions fix the original interface. The genuinely verified generic statement is:

```lean
theorem generic {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    (a b c : K) : a + 2 * b < c / 2 ↔ a < (c - 4 * b) / 2
```

[Exact isolated source](../evidence/Roth.eta_lt_gam_iff/isolated-executed.lean.txt) and [clean receipt](../evidence/Roth.eta_lt_gam_iff/isolated-receipt.json) verify it, the fully expanded original, the weak analogue and a coefficient counterexample with no project imports. `#check_failure` guards eta/gam/lam/target. [Project probes](../evidence/Roth.eta_lt_gam_iff/project-executed.lean.txt) verify arbitrary eta and the concrete normalization bridge. These are **new proofs**, not existing mathlib building blocks and not new axioms. Restating at this level is mechanically verified; cost is not a verdict reason. Existing additive API already provides the broader mathematical law after normalization.

## Phase 4c — modern idiom

| # | Check | Applies / concrete consequence |
|---|---|---|
| 1 | Typeclasses | Yes for abstract scalar law; field/order hierarchy removes concrete ℝ dependence and permits ℚ or any ordered field. Original parameter definitions stay real. |
| 2 | Filters/nets | No; no limit statement in this equivalence. Caller's continuity argument does not turn this algebra law into a filter theorem. |
| 3 | Universal property | No construction or universal object. |
| 4 | Bundled substructure | No closed-set predicate or subobject. |
| 5 | Weaker hierarchy | Yes; translated inequality is already `lt_sub_iff_add_lt` at AddGroup/LT/right-strict-monotone level. Division law uses existing division-ring API. |
| 6 | Higher category | No categorical content. |
| 7 | Concrete indices | Yes as scalar abstraction: n/m/sqrt's values can become arbitrary b/c; not a claim about arbitrary dimensions' square roots. |
| 8 | Concrete-via-abstract | Fires: source body `grind [gam, lam]` mentions eta zero times, gam/lam once each. Arbitrary e and general-field probes certify abstraction; [diagnostic](../evidence/Roth.eta_lt_gam_iff/concrete-diagnostic.json). |
| 9 | False-generalization guard | Preserve linked coefficients and ordinary subtraction. Do not replace Roth eta/gamma by modular/Dirichlet functions or Diophantine Roth by arithmetic-progression Roth. Counterexample rejects independent coefficients. |

Modern organization is available: use existing additive order API after scalar normalization. It enables direct composition with `sub_pos` and ordered-field arithmetic without real analysis. It does not establish a missing mathlib theorem warranting a new general wrapper.

## Phase 4.5 — infrastructure risk

All six rows are justified n/a for this theorem; it introduces no data definition or instance.

| Risk | Assessment |
|---|---|
| Typeclass diamond | n/a: no instance or structure is introduced. |
| Reducibility | n/a: theorem equality is proof-irrelevant; no data reduction contract. |
| Noncanonical unfolding | n/a for theorem; normalization of its parent definitions is separately tested. |
| Instance priority | n/a: no priority declaration. |
| Universe | n/a infrastructure risk: original concrete ℝ/ℕ, abstract probes use Type*. |
| Coercion | n/a: no coercion is installed; Nat→Real casts already existing. |

## Phase 4.6 — proof strategy

| # | Check | Result |
|---|---|---|
| 1 | Topology / epsilon-delta | No topology in target. |
| 2 | Algebra / subobjects | Scalar arithmetic, no ideal/submodule abstraction to gain. |
| 3 | Analysis / sequence vs filter | No analytic argument after treating eta/error as scalar values. |
| 4 | Category / universal characterization | No constructed categorical object. |
| 5 | Missing helper mathlib should have | None established: existing translation and field API suffice after normalization. New generic arithmetic proof is a possible wrapper, not evidence of absent substantive mathematics. |

MATHLIB-IDIOMATIC locally: unfold two parameter definitions and normalize scalar arithmetic. An explicit alternative is the verified `bridge` equality followed by `lt_sub_iff_add_lt.symm`; the bridge is a new `ring` proof, so that route cannot be labelled a strict existing-call replacement for the original. The current named form exposes source semantics to its callers.

## Phase 5 — all fifteen formal search cells

Each cell has the complete original tool request/result and elapsed_ms, or exact rg command/stdout/stderr/exit. External indexes are not assumed to match the pin. All local-search indexes reported warming: positive results are useful, empty results would not show absence.

| Form | Method | Result / receipt |
|---|---|---|
| current | leanfinder | `rothNumberNat_le`, `Behrend.roth_lower_bound`, `Behrend.roth_lower_bound_explicit`, `Behrend.bound_aux'` [receipt](../evidence/Roth.eta_lt_gam_iff/search-current-leanfinder.json) |
| current | loogle | No results, not proof of absence. [receipt](../evidence/Roth.eta_lt_gam_iff/search-current-loogle.json) |
| current | leansearch | `ModularForm.eta`, `Nat.le_div_two_iff_mul_two_le`, `ModularForm.eta_ne_zero`, `Nat.ceil_lt_two_mul` [receipt](../evidence/Roth.eta_lt_gam_iff/search-current-leansearch.json) |
| current | rg | Pinned source enumeration; exact command and returned lines archived. [receipt](../evidence/Roth.eta_lt_gam_iff/search-current-rg.json) |
| current | local_search | `Roth.eta_lt_gam_iff` [receipt](../evidence/Roth.eta_lt_gam_iff/search-current-local_search.json) |
| standard | leanfinder | `add_lt_of_lt_sub_right`, `add_lt_of_lt_sub_left`, `lt_sub_iff_add_lt'`, `lt_tsub_iff_left` [receipt](../evidence/Roth.eta_lt_gam_iff/search-standard-leanfinder.json) |
| standard | loogle | `Nat.add_lt_iff_lt_sub_right` [receipt](../evidence/Roth.eta_lt_gam_iff/search-standard-loogle.json) |
| standard | leansearch | `sub_neg`, `lt_of_sub_pos`, `sub_pos`, `sub_lt_zero` [receipt](../evidence/Roth.eta_lt_gam_iff/search-standard-leansearch.json) |
| standard | rg | Pinned source enumeration; exact command and returned lines archived. [receipt](../evidence/Roth.eta_lt_gam_iff/search-standard-rg.json) |
| standard | local_search | `Nat.lt_sub_iff_add_lt`, `EReal.lt_sub_iff_add_lt`, `lt_sub_iff_add_lt`, `Nat.lt_sub_iff_add_lt'` [receipt](../evidence/Roth.eta_lt_gam_iff/search-standard-local_search.json) |
| abstract | leanfinder | `Mathlib.Tactic.LinearCombination.div_lt_const`, `div_lt_div_iff₀`, `Rat.div_lt_div_iff_mul_lt_mul`, `div_lt_div₀` [receipt](../evidence/Roth.eta_lt_gam_iff/search-abstract-leanfinder.json) |
| abstract | loogle | `div_sub_div_same`, `div_sub_div`, `Commute.div_sub_div`, `EuclideanDomain.div_sub_div_of_dvd` [receipt](../evidence/Roth.eta_lt_gam_iff/search-abstract-loogle.json) |
| abstract | leansearch | `sub_div`, `EuclideanDomain.sub_mul_div_right`, `tsub_div`, `ENNReal.sub_div` [receipt](../evidence/Roth.eta_lt_gam_iff/search-abstract-leansearch.json) |
| abstract | rg | Pinned source enumeration; exact command and returned lines archived. [receipt](../evidence/Roth.eta_lt_gam_iff/search-abstract-rg.json) |
| abstract | local_search | `ENNReal.sub_div`, `NNReal.sub_div`, `sub_div`, `sub_div'` [receipt](../evidence/Roth.eta_lt_gam_iff/search-abstract-local_search.json) |

Current-form searches returned unrelated Roth-number and Dedekind-eta declarations; those are rejected conceptually. Standard/abstract searches find the real building blocks. Pinned native #checks verify `lt_sub_iff_add_lt`, `sub_div`, `div_sub_div_same`, `mul_div_cancel_left₀`, `lt_div_iff₀`. Pinned homes: `Mathlib/Algebra/Order/Group/Unbundled/Basic.lean` (lt_sub_iff_add_lt via to_additive near619), `Mathlib/Algebra/Field/Basic.lean:97,112` (division/subtraction), `Mathlib/Algebra/GroupWithZero/Defs.lean:204` (cancellation). [Pinned files and hashes](../evidence/Roth.eta_lt_gam_iff/mathlib-inputs.json). No exact named old-form API is established; absence is not inferred solely from searches.

## Phase 5.5 — statement shape

1. **Normal form:** compare η+error<m/2, η<m/2−error, η<γ, and 0<γ−η. The canonical additive translation is already `lt_sub_iff_add_lt`; local RHS η<γ is the paper's semantic normal form and both callers then use `sub_pos`. It is not tagged simp, so no new global normalization policy is introduced.
2. **Syntactic generality:** verified `arbitrary_eta`, general-field `generic`, explicit subtraction `explicit_existing_translation`, and `original_normalized`. The named form is easiest for source-aligned local consumers; abstract upstream arithmetic should use the existing additive form. Both `.mp` and `.mpr` exist; actual callers only use `.mp`.
3. **Superfluous parameters/classes:** no explicit hypotheses or typeclasses to drop; δ/n/m occur in the concrete type. Eta's defining formula is superfluous to the arithmetic proof and can become e in a broader statement. This does not permit deleting these parameters from the unchanged `gam` signature.

Statement-shape verdict: acceptable locally; RESTATE-BEFORE-SHIP for any upstream scalar law, at the existing canonical abstract API. No public signature changed.

## Phase 6.0 — full caller and inline audit

Fresh no-ignore rg agrees with git grep over tracked production; inventory includes all canonical source files. [Lexical search](../evidence/Roth.eta_lt_gam_iff/source-search.json), [tracked crosscheck](../evidence/Roth.eta_lt_gam_iff/tracked-source-search.json), [inventory](../evidence/Roth.eta_lt_gam_iff/source-inventory.json), [full callers](../evidence/Roth.eta_lt_gam_iff/callers.json), [related expression audit](../evidence/Roth.eta_lt_gam_iff/inline-audit.json).

| Caller | Occurrences / use | Verified inline action |
|---|---|---|
| Roth.exists_delta, Main:227–249 (use241) | 1 body; no signature occurrence | In denominator nonzero proof, retain h=(hδ₀' 0 le_rfl hδ₀.le).2, unfold gam/lam, derive eta0<gam0 arithmetically. |
| Roth.roth_of_isIntegral, Main:547–563 (use560) | 1 body; no signature occurrence | Retain h30, unfold gam/lam and derive eta<gam before `sub_pos` and `div_lt_iff₀'`. |

External-to-file: one file, two declarations/two occurrences. None in declaring file. Both whole actual proofs replayed inside the complete original Main module under `Gap235Inline`, with only target calls replaced by explicit arithmetic derivations; both original signatures validated by `rfl` equality. [Exact full replay](../evidence/Roth.eta_lt_gam_iff/inline-executed.lean.txt), [clean result](../evidence/Roth.eta_lt_gam_iff/inline-receipt.json). This is more than a toy caller. No exact equivalent re-derivation elsewhere was established; related gamma−eta bounds are substantive estimates, not duplicates of the iff.

The canonical293 kernel audit independently finds exactly these two direct body consumers, zero direct type consumers, all293 names unique/present/with values and exact tracked order/private modules. Source lexical refs, source type refs, direct kernel body/type edges, generated-helper closure, simp and transitive import closure are distinct scopes: [scope audit](../evidence/Roth.eta_lt_gam_iff/scope-audit.json). No unmeasured transitive target-freedom claim is made for the replay.

## Phase 6 — composition experiments

A strict **three-existing-theorem term** compiles for normalized arbitrary scalars:

```lean
theorem three_term (a b c d : ℝ) (hd : d ≠ 0) :
    a + b < c / d ↔ a < (c - d * b) / d :=
  Eq.ndrec (motive := fun z ↦ a + b < c / d ↔ a < z)
    (Eq.ndrec (motive := fun z ↦ a + b < c / d ↔ a < c / d - z)
      (show a + b < c / d ↔ a < c / d - b from lt_sub_iff_add_lt.symm)
      (mul_div_cancel_left₀ b hd).symm) (div_sub_div_same c (d * b) d)
```

This uses exactly three mathematical lemmas plus equality transport and Iff symmetry; the equivalent three-rewrite proof is also verified. Only d≠0 is required, not d>0; negative_d verifies that detail. It is **not** an existing named mathlib theorem and not a strict three-call proof of the exact original spelling. Directly supplying it at d=2 to the expanded original fails (certified `fail_if_success`) because d*b is not definitionally the left-associated 4(1+3δ)n√m expression. Direct `lt_sub_iff_add_lt.symm` also fails until the gamma normalization bridge is supplied.

The fully expanded original closes by arithmetic automation; generic and arbitrary-eta forms likewise compile. The concrete bridge γ=m/2−error needs new ring normalization. Therefore **NOT-COMPOSABLE under the strict original-form ≤3-existing-call test as verified here**; this is not a universal impossibility theorem about all possible terms. The normalized form is COMPOSABLE. New generic proofs/project eta/gam/lam must not be counted as existing mathlib calls. Short `grind`/`ring` or a closing `simp [defs]` proof does not meet that strict composition criterion; this semantic-versus-normalization choice is precisely why the verdict remains BORDERLINE rather than an unsupported NO.

## Phase 7 — verdict and actionable alternatives

**BORDERLINE-needs-human**, independently assessed. The scalar content is already represented by mathlib's additive order and field identities, while the local name tells both actual callers that the paper's inequality gives a positive γ−η gap. Searches establish no substantive missing theorem; verified abstraction removes eta's formula, sqrt and natural indices entirely. The exact old spelling still needs arithmetic normalization, and the clean inline replay does not erase the value of a source-aligned local name. Neither the short original proof nor a parent parameter's verdict determines this result; no cost-based downgrade is used.

Future upstream design questions (not blockers for completion):
1. When a Roth parameter API is proposed upstream, should this named equivalence stay beside eta/gam as a stable semantic bridge to the source equation (38)?
2. Should an upstream parameter API expose gamma as m/2 minus the error term, making this law a direct lt_sub_iff_add_lt specialization?
3. Does the general scalar law a + b < c/d ↔ a < (c-d*b)/d merit a separate upstream name despite its verified three-existing-lemma term?

Concrete local action: retain this lemma in `Roth/MainLemma.lean` while the named parameter API is local. If that API is removed or normalized, inline the two exact replacements already validated in `inline-executed.lean.txt`; no caller signatures need change. If a standalone upstream scalar wrapper is proposed, first decide question3 against the already verified three-call composition. No PR home/title/reviewer/grouping is promised for a BORDERLINE declaration. Prior accepted YES declarations were not inferred from names or reused as a verdict rationale.

Pairwise duplication audit:

| A | B | Same statement? | Same argument? | Action |
|---|---|---|---|---|
| eta_lt_gam_iff | lt_sub_iff_add_lt | After non-definitional gamma normalization | Yes, translated strict inequality | Use canonical additive API for abstract arithmetic; retain local semantic bridge if desired. |
| eta_lt_gam_iff | div_sub_div_same / mul_div_cancel_left₀ composition | Normalized scalar form only | Same arithmetic core | Verified strict-three term; coefficient/association bridge is separate. |
| eta_lt_gam_iff | exists_delta_bound | No: existence of small δ with the inequality versus equivalence | No: continuity/gap versus arithmetic | Do not unify; latter supplies the substantive hypothesis. |
| eta_lt_gam_iff | the two actual caller denominator arguments | Same local conversion substep | Yes | Full inlining possible; no other exact redeclaration located. |

## Phase 8 — evidence and completion

Four accepted clean native sets: original full-module replay/type/body/axioms/exact293 audit; exact18 isolated mathlib-only arithmetic; full Main caller inline replay; project generic/normalization and outgoing Roth body-edge probes. All are successful, nonpartial/non-timeout where the tool exposes those fields, error/warning/sorry-free, standard axioms only. Initial original warming response is not accepted success. The first isolated rejected attempt has recovered sorryAx; the second has tactic-linter warnings. Both exact sources and raw receipts are preserved separately and excluded from accepted verification. No limits raised, unsafe code, native_decide or new axiom. `#check_failure` unknown-identifier messages are intended info diagnostics, not errors.

[Verification index](../evidence/Roth.eta_lt_gam_iff/verification.json), [assessment](../evidence/Roth.eta_lt_gam_iff/assessment.json), [portable validator](../evidence/Roth.eta_lt_gam_iff/validate.py), [current manifest](../evidence/Roth.eta_lt_gam_iff/copy-manifest.json), [final validation](../evidence/Roth.eta_lt_gam_iff/final-validation.json). Supporting Lean sources are exact `.lean.txt` evidence, not new project modules. Root independent acceptance is pending. Freeze/native release only after manifest, portable validator and credential guard PASS.
