# Roth.indexSet_bddAbove — full mathlibable assessment

**Verdict: BORDERLINE-needs-human.** The full theorem combines a substantive uniform polynomial-index bound with elementary bounded-image packaging. The latter is a one-call composition from existing `Set.forall_mem_image2`; it does not supply the former. No exact existing full boundedness law was established. Retain this useful local lemma while choosing the upstream Taylor/degree-envelope API. All verification is complete; the remaining questions concern API design, not an unfinished proof.

## Phase 0 — Doctor

Canonical declaration186 is the public theorem at `Roth/Theta.lean:87`; line86 belongs to its docstring. [Canonical entry](../evidence/Roth.indexSet_bddAbove/canonical-target.json). The shared [baseline](../evidence/Roth.indexSet_bddAbove/baseline-build.txt) completed2467jobs successfully. All17 production/pin hashes freshly match [the baseline inputs](../evidence/Roth.indexSet_bddAbove/input-manifest.json), as recorded in [fresh hashes](../evidence/Roth.indexSet_bddAbove/source-hashes.json). No production source, pin, Git state or overview record was changed.

The entire985-line [Theta module](../evidence/Roth.indexSet_bddAbove/source-Theta.lean.txt) and both complete actual callers were read. Theta defines the family of bounded integral polynomials and suprema of their weighted indices, then proves the three estimates used for Roth's theorem. Native original resolution, complete kernel body, standard axioms and exact canonical293 audit all pass: [original source](../evidence/Roth.indexSet_bddAbove/bddabove186-original-executed.lean.txt), [raw receipt](../evidence/Roth.indexSet_bddAbove/bddabove186-original-receipt.json). No printer elision occurred.

## Phase 1 — Comprehend

For any real coefficient bound B and any natural denominator and degree vectors q,r, the real indices of all permitted nonzero integer polynomials, at all permitted coprime rational numerator choices, are bounded above. The explicit common bound is the number of variables. Nonzero Taylor coefficients have coordinate degrees within the prescribed box, which bounds their normalized weights and therefore the minimum defining the index.

Full native elaborated type:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] (B : ℝ) (q : σ → ℕ) {r : σ → ℕ},
  BddAbove (Roth.indexSet B q r)
```

σ is the finite variable type; B bounds coefficients; q supplies denominators; r bounds coordinate degrees and normalizes derivative orders. There are no positivity, `1 ≤ B`, nonempty-type, or DecidableEq hypotheses. The proof unpacks a polynomial R≠0 and its degree bounds; coefficient bounds and numerator coprimality are discarded. Injectivity of integer-to-real coefficient mapping transfers nonvanishing and coordinate degrees. The actual uniform estimate is **project** `Roth.index_le_card`, not a mathlib declaration.

Documentation finding: the docstring starts “If every `r j` is positive”, but the native theorem needs no such premise. It already covers zero coordinates under total real division. This is a documentation mismatch only; source remains unchanged.

## Phase 2 — Preliminary checks

SMALL: a boundedness helper supporting supremum estimates, with no new structure or named main theorem. The one-line-definition test is n/a because this is a theorem. Its short proof is not itself a reason for rejection.

## Phase 3 — Exhaustive literature

All named channels were actually checked. Web artifacts retain exact requests, returned-response SHA256/bytes/status, sanitized URLs/titles/locators and concise original summaries; full returned bodies are not archived. [General queries](../evidence/Roth.indexSet_bddAbove/web-0.json), [nLab/nCatLab](../evidence/Roth.indexSet_bddAbove/web-1.json), [Stacks/MO](../evidence/Roth.indexSet_bddAbove/web-2.json), [recent arXiv](../evidence/Roth.indexSet_bddAbove/web-3.json), [primary access and exact recent window](../evidence/Roth.indexSet_bddAbove/web-primary.json).

| Channel | Actual query / locator | Finding |
|---|---|---|
| General specific | `Roth theorem polynomial index theta supremum bounded above number variables` | Princeton lecture notes and original Roth ICM lecture supply weighted derivative-index context. |
| General abstract | `bounded above binary image uniform bound function set order theory` | Upper bound means a common majorant for every image value; does not prove the polynomial majorant. |
| General aliases | `Roth lemma index polynomial Taylor expansion index at most number variables` | Index/normalized derivative minimum terminology; source's Taylor degree-box argument is the exact local content. |
| ChatGPT math MCP | Standard form, generality and historical evolution | n/a: ask_chatgpt_math unavailable. Other channels were not reduced. |
| Local source | clean.tex §5, lines643–703 | Defines Θ as supremum of this family and explains a nonzero Taylor derivative with ij≤rj, weight≤m. [Exact excerpt](../evidence/Roth.indexSet_bddAbove/clean-section5-excerpt.tex.txt), [source hash](../evidence/Roth.indexSet_bddAbove/local-literature.json). |
| nLab | `site:ncatlab.org/nlab upper bound image ordered set` | Indexed [upper bound](https://ncatlab.org/nlab/show/upper%2Bbound) defines upper bounds in a preorder; image page gives generic image context. Direct XHTML open failed400. |
| nCatLab | `site:ncatlab.org/ncatlab upper bound binary image order` | Actual distinct namespace searched; returned related nLab material, no exact in-namespace result established. |
| Stacks | `site:stacks.math.columbia.edu polynomial index Roth degree bound` | Adjacent polynomial/geometric material, no exact normalized weighted-family boundedness law established. |
| MathOverflow | `site:mathoverflow.net Roth polynomial index bound` | Related Roth/Diophantine discussions; no exact full-law replacement established. |
| Recent arXiv | `site:arxiv.org Roth polynomial index Diophantine 2022 2023 2024 2025 2026`, then strict after2021-10-27/before2026-10-28 query | Initial hits included irrelevant Roth-name material and older Diophantine work. Exact recent query empty; no recent standard reformulation verified. |

Primary locators: [Princeton Chapter17](https://web.math.princeton.edu/mathlab/jr02/diophantine.pdf), Definition17.1.1, describes normalized derivative index; [Roth's ICM1958 lecture](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf), p206, describes minimal weighted derivative order and arithmetic index bounds. Direct opens respectively timed out and exceeded the content-size limit; only their indexed extracts were available. These are contextual evidence, while the local manuscript gives the exact family/boundedness statement.

Synthesis: the standard arithmetic content is a uniform bound on weighted Taylor order from a coordinate-degree box. Generic bounded-image packaging works over an arbitrary relation LE; the arithmetic bound still requires its degree/witness argument. The manuscript assumes m≥1, B≥1 and positive q,r; Lean admits empty σ, small/negative B and zero coordinates using its totalized real index. This extension must not be confused with the manuscript's infinity-valued zero-polynomial convention.

## Phase 4a — Every parameter and hypothesis

| Parameter | Role / generality | Evidence and limit |
|---|---|---|
| σ : Type u | variable universe | Native target is universe-polymorphic; no explicit inhabitance assumption. |
| Fintype σ | finite coordinate sum and card | Required by current `index`/card interface. Generic image law has arbitrary independent source universes and needs no finiteness. Removing Fintype from the old spelling is not claimed mechanically verified. |
| B : ℝ | coefficient bound defining RSet | Arbitrary real already; no lower bound. Coefficient control is unused by the pointwise degree bound, but B remains an input to the exact family. |
| q : σ→ℕ | denominator vector | All q including zero; coprimality restricts numerators but is unused in the degree estimate. Arbitrary centers could be used after changing the family definition; no old-interface parameter deletion is claimed. |
| r : σ→ℕ | degree box and normalization | Zero permitted; no positivity to drop. Dropping all degree control would destroy the cardinality estimate. |
| ℤ coefficients / ℝ index | inherited exact family inputs | Generic image law accepts any types/codomain with LE. This abstracts packaging only; it is not a proof of a semiring-valued Roth bound. |
| DecidableEq σ | absent | `omit` removes it; classical reasoning is local in the proof. |

## Phase 4b — Generality verdict

MAXIMALLY GENERAL relative to the fixed parent interfaces: no removable native hypothesis was found. The isolated generic image-bound and exact boundedness equivalence both compile under **LE γ**, weaker than Preorder; this is an expanded structural restatement, not a mechanically weakened arithmetic theorem. No YES-but-generalise-first claim follows from merely changing the map to arbitrary f and supplying its desired bound as a new premise.

Compiled structural form:

```lean
{α : Type u} → {β : Type v} → {γ : Type w} → [LE γ] →
{f : α → β → γ} → {s : Set α} → {t : Set β} → {c : γ} →
(∀ x ∈ s, ∀ y ∈ t, f x y ≤ c) → BddAbove (Set.image2 f s t)
```

[Exact isolated source](../evidence/Roth.indexSet_bddAbove/bddabove186-isolated-executed.lean.txt), [clean raw receipt](../evidence/Roth.indexSet_bddAbove/bddabove186-isolated-receipt.json). Its hypothesis is the substantial arithmetic obligation in the original application.

## Phase 4c — Nine modern-idiom rows

| # | Question | Assessment / concrete downstream consequence |
|---|---|---|
| 1 | Preambles as typeclasses | Existing Fintype and LE structures suffice; no new class for a particular bound. |
| 2 | Sequences versus filters | No convergence/topology appears. |
| 3 | Construction versus universal property | No new object constructed beyond an upper-bound witness. |
| 4 | Sets versus bundled substructures | The family excludes zero and imposes arithmetic restrictions; it is not a submodule. |
| 5 | Field-specific hierarchy | Generic packaging verified at LE, with no scalar field. Arithmetic remains in the real polynomial parent. |
| 6 | Higher categories | No categorical structure in this finite degree bound. |
| 7 | Concrete numeric indices | Image-bound theorem accepts arbitrary LE codomain; retaining numeric card requires arithmetic structure and finite variables. |
| 8 | Concrete-via-abstract diagnostic | Fires for outer packaging: body has zero indexSet occurrences after membership unpacking. RSet's coefficient and coprimality conditions disappear; `Set.forall_mem_image2` transports any pointwise bound. The index_le_card computation remains genuinely polynomial-dependent. |
| 9 | False-generalization guard | An arbitrary image is not automatically bounded. The generic law retains a supplied uniform c; discarding that premise changes the claim. Likewise, dropping degree control or silently identifying WithTop∞ with real0 changes arithmetic meaning. |

Modern idiom available: yes, existing image2 quantifier API gives an honest short structural proof, directly usable by `le_csSup` and `csSup_le_csSup`. Parent index's earlier infDegree/Finsupp.weight re-aim does not imply mathlib already proves this full coordinate/Taylor/card bound. The new generic helper is not advertised as an existing named mathlib theorem.

## Phase 4.5 — Infrastructure risk

n/a: theorem. Typeclass diamonds, reducibility leaks, noncanonical unfolding, instance-priority collisions, universe restrictions and coercion ambiguity are all definition/instance concerns; this proposition proof introduces none. Its choice of parent representation is an API design matter, not a new coercion or instance.

## Phase 4.6 — Five proof-strategy rows

| # | Question | Assessment |
|---|---|---|
| 1 | ε–δ to filters | n/a; finite polynomial/order argument. |
| 2 | Elements to point-free algebra | Separate pointwise bound from image2 quantifier transport; no ideal/submodule inclusion needed. |
| 3 | Sequences to nets | n/a; no limits. |
| 4 | Construction to universal property | n/a; existential majorant is the appropriate witness. |
| 5 | Missing helpers mathlib should have | Generic packaging is already a one-call composition. The possible upstream gap is the reusable Taylor-coordinate-degree/weighted-support envelope, discussed independently at index_le_card. |

REFACTOR-RECOMMENDED for future upstream organization: reuse image2 and keep the uniform polynomial estimate as its own theorem. The original proof is sound and compact; extracting a project pointwise lemma would be a new proof interface, not a preexisting mathlib replacement. Cost is not used to select the verdict.

## Phase 5 — All five actual mathlib methods

[Complete formal requests and raw receipts](../evidence/Roth.indexSet_bddAbove/formal-search.json) cover Finder, Loogle, LeanSearch and local name search on current, literature-standard and abstract forms. Three fresh source searches complete all15cells: [current](../evidence/Roth.indexSet_bddAbove/rg-current.json), [standard](../evidence/Roth.indexSet_bddAbove/rg-standard.json), [abstract](../evidence/Roth.indexSet_bddAbove/rg-abstract.json). [Positive refinements](../evidence/Roth.indexSet_bddAbove/formal-positive.json) independently locate the relevant quantifier theorem through all three remote methods.

| Method | Current arithmetic form | Literature-standard form | Abstract image form |
|---|---|---|---|
| Finder | Chevalley degree bounds, rejected as different | BddAbove.image2, related but wrong premises | forall_mem_image2 after precise refinement |
| Loogle | BddAbove/MvPolynomial no hit | BddAbove/image2 monotonicity family | Exact forall_mem_image2 positive refinement |
| LeanSearch | Mahler measure finiteness / Schwartz–Zippel, rejected | BddAbove.image2 and partial image bounds | Exact forall_mem_image2 positive refinement |
| rg | No exact project target in mathlib pin | BddAbove.image2 / bddAbove_def | forall_mem_image2 / image2_subset_iff |
| local | Actual project theorem | BddAbove and image2 laws | forall_mem_image2 source hit |

All local receipts report index unavailable, so these hits verify names through source lookup; empty results never establish absence. External services may index a different mathlib revision.

Pinned and isolated-native-checked candidates: `Set.forall_mem_image2`, `Mathlib/Data/Set/NAry.lean:54`, transports predicates over binary images; `bddAbove_def`, `Mathlib/Order/Bounds/Basic.lean:42`, supplies existential pointwise formulation but requires Preorder in this pin. `BddAbove.image2`, `Mathlib/Order/Bounds/Image.lean:209`, assumes both source preorders, monotonicity in each argument and boundedness of both source sets. Those assumptions are not supplied by the Roth family; it is rejected as a full replacement. [Pinned source archives and hashes](../evidence/Roth.indexSet_bddAbove/mathlib-inputs.json).

Conclusion: existing generic transport plus boundedness witness constructor give the structural component. No exact full arithmetic law was established. This is not a global proof of absence.

## Phase 5.5 — Three statement-shape checks

Normal forms: `BddAbove indexSet`; an existential common c for all polynomial/numerator choices; image2 contained in `Set.Iic c`. The exact image2 bridge is rfl, and the isolated boundedness equivalence compiles. BddAbove is appropriate for the actual conditional-supremum callers; an explicit card bound is stronger useful arithmetic data. No orthogonal chain of representation equivalences is needed.

Syntactic generality: tested pointwise bound, then BddAbove image2, then complete original caller signatures. Keep the local named boundedness fact for its two callers; if upstreaming generic structure, use existing forall_mem_image2 rather than a parallel specialized definition. RHS normalization is respected by the displayed iff with pointwise formula on the right.

Superfluous arguments: no unused native assumptions to delete. Fintype is fixed by index/card; B,q,r determine the exact family even when particular RSet conditions are unused in the proof. DecidableEq and positivity are already absent. Overall: SHIP-AS-STATED locally, RESTATE-BEFORE-SHIP upstream until the polynomial parent/envelope interface is chosen. Docstring positivity should be corrected in later source cleanup.

## Phase 6.0 — Complete callers and inline audit

[rg --no-ignore](../evidence/Roth.indexSet_bddAbove/callers.json) cross-checks [git grep](../evidence/Roth.indexSet_bddAbove/git-callers.json), the canonical source inventory and [structured caller table](../evidence/Roth.indexSet_bddAbove/callers-structured.json). There are exactly two explicit proof applications, both in the declaring file; external-to-file uses0. An initial git grep with a \b ERE pattern returned no hits on this host; the root's actual `git grep -w` retry agrees exactly with rg. The command's count excluding the declaring file is therefore0, while total project application count is2. Native canonical293 enumeration independently finds exactly these2 direct value consumers and0 type consumers. Source occurrences and direct kernel consumers are separate audits.

| Caller | Actual use | Tested prospective treatment |
|---|---|---|
| Roth.index_le_Θ, Theta102 | le_csSup (indexSet_bddAbove B q) | caller_index_le replays full proof with independently derived replacement bound; membership witness unchanged. |
| Roth.Θ_mono, Theta136 | csSup_le_csSup (indexSet_bddAbove B' q) | caller_mono replays full proof, retaining nonempty source and coefficient-bound inclusion. |

[Inline audit](../evidence/Roth.indexSet_bddAbove/inline-audit.json): Θ_le_card at118–124 repeats the mapped polynomial degree/index estimate inside Real.sSup_le. It is a stronger numeric supremum estimate, not another direct BddAbove theorem. The target is useful local API, not dead code. No claim about opaque/transitive/simp closure follows from lexical counts.

## Phase 6 — Actual composition experiments

The generic structural term is:

```lean
example [LE γ] {f : α → β → γ} {s : Set α} {t : Set β} {c : γ}
    (h : ∀ x ∈ s, ∀ y ∈ t, f x y ≤ c) : BddAbove (Set.image2 f s t) :=
  ⟨c, Set.forall_mem_image2.mpr h⟩
```

This is one existing theorem call plus constructor packaging: **COMPOSABLE structural component**. The bound-iff experiment normalizes the definition then uses `simp only [Set.forall_mem_image2]`; that is a trivial simp composition, explicitly subject to Phase6b's BORDERLINE caution. It is not a named existing boundedness law.

The actual project experiment proves exact image2 identification by rfl, independently proves the full pointwise card bound by retaining map nonvanishing/degree transport and project `index_le_card`, builds BddAbove from it, and replays both complete callers. [Exact project source](../evidence/Roth.indexSet_bddAbove/bddabove186-project-executed.lean.txt), [clean receipt](../evidence/Roth.indexSet_bddAbove/bddabove186-project-receipt.json). It never calls indexSet_bddAbove to prove its replacement.

**Full original: NOT-COMPOSABLE by a verified ≤3-existing-mathlib-call term.** A project `pointwise` helper is a new arithmetic proof; counting its name as one mathlib building block would conceal the substantive premise. Generic image boundedness does not prove a uniform bound on Roth's index. The parent's more-general image2 constructor was independently checked, but its predicate-transport law is not the full analogous arithmetic boundedness law, so ModeB re-aim does not force NO-mathlib-has-it. Earlier infDegree/Finsupp.weight representations similarly settle a support-minimum component without establishing the full Taylor/degree/card bound. No full expanded bridge call-count claim is made.

Boundary scope is exact: all accepted project statements quantify over arbitrary B,q,r and finite σ, including q=0, r=0 and empty σ. The theorem requires no nonempty family; boundedness of an empty image is legitimate. No claim that arbitrary map values are bounded without the explicit uniform premise is made.

One isolated attempt failed after root weakened Preorder to LE: `bddAbove_def` cannot rewrite at this weaker structure, so simp made no progress and the failed proof printer recovered sorryAx. [Rejected exact source](../evidence/Roth.indexSet_bddAbove/bddabove186-isolated-rejected1-executed.lean.txt), [rejected receipt](../evidence/Roth.indexSet_bddAbove/bddabove186-isolated-rejected1-receipt.json). The accepted source unfolds only the boundedness proposition with `change`, then applies the quantifier theorem; no raised limits or new axiom. Rejected sorryAx evidence is excluded from accepted proofs.

## Phase 7 — Actionable verdict

**BORDERLINE-needs-human.** Keep `Roth.indexSet_bddAbove` in `Roth/Theta.lean`: it supplies the exact side condition for both conditional-supremum consumers. There is no evidence for adding this arithmetic-family wrapper to foundational set/order mathlib. The generic packaging is already composable; the full mathematical dependence is the polynomial index bound, whose upstream shape was itself left as an API-design question in accepted declaration150, `Roth.index_le_card`. This assessment independently checks the current dependence rather than inheriting that verdict.

Concrete future upstream API questions:

1. Should the full uniform bound over coordinate-degree-bounded polynomials be exposed upstream, or should this arithmetic-family boundedness lemma remain local after a generic weighted Taylor-degree theorem is added?
2. Should the upstream theorem target canonical WithTop infDegree with a nonzero premise, or a real-valued default0 projection matching this project's totalized boundary cases?
3. Should a future contribution expose an arbitrary coordinate-envelope weighted bound, with cardσ obtained locally, rather than a named Θ-family bound?

These are ≤3 concrete design decisions; they do not require an answer to finish this read-only assessment. If upstreaming is chosen, a prospective Taylor/degree file under `Mathlib/Algebra/MvPolynomial/` should own the reusable mathematical theorem; `Mathlib/Data/Set/NAry.lean` already owns the generic transport. This is a conditional location, not a YES proposal or accepted PR grouping. No cost consideration changes the verdict.

Local refactor plan, if the wrapper is later removed: at index_le_Θ102 preserve `le_csSup` and supply the independently derived image2 bound; at Θ_mono136 preserve `csSup_le_csSup`, nonempty witness and set inclusion, replacing only its upper-bound argument. The tested replacement still depends on the project pointwise degree proof. Keeping the wrapper is clearer until that arithmetic API is settled. Correct its stale positivity docstring during cleanup; no edit is made here.

## Phase 8 — Completion and evidence

All mandatory phases PASS, with theorem-only checks justified n/a; unresolved[] is empty. Three native accepted receipts verify original, project replay and isolated structural law with standard axioms only. The rejected isolated proof is retained separately. [Assessment](../evidence/Roth.indexSet_bddAbove/assessment.json), [verification](../evidence/Roth.indexSet_bddAbove/verification.json), [overview entry](../evidence/Roth.indexSet_bddAbove/overview-entry.json), [current manifest](../evidence/Roth.indexSet_bddAbove/copy-manifest.json), [portable validator](../evidence/Roth.indexSet_bddAbove/validate.py). The validator checks current artifact hashes/bytes, fresh17 inputs, exact ordered293 names including private names, clean native diagnostics, all15 formal-search cells, caller agreement and report links. Root acceptance remains pending independent review.
