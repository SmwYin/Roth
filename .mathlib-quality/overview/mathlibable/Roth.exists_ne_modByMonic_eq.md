# `Roth.exists_ne_modByMonic_eq` — canonical249

Verdict: **BORDERLINE-needs-human**, revised after substantive root review. **The finite-support premise on r is removable from the unchanged statement.** Two independent strengthenings and exact original/caller recovery compile. The complete selected-Hasse-remainder theorem still needs a polynomial encoding proof. The abstract finite-map collision already exists; calling that outer theorem once does not make the original theorem a one-call replacement. This completed read-only assessment leaves only future upstream design questions, with verification unresolved[] and root acceptance pending.

## Phase0 — Baseline and source

Fresh hashes of all17 sources/pins match the tracked shared manifest; the reusable baseline succeeds with2467 jobs. See [inputs.json](../evidence/Roth.exists_ne_modByMonic_eq/inputs.json), [input-manifest.json](../evidence/Roth.exists_ne_modByMonic_eq/input-manifest.json) and [baseline-build.txt](../evidence/Roth.exists_ne_modByMonic_eq/baseline-build.txt). Canonical tracked order resolves the public theorem at `Roth/MainLemma.lean:359` (prompt's358 was approximate). Full MainLemma and its sole actual caller were read; complete module evidence is [source-MainLemma.lean.txt](../evidence/Roth.exists_ne_modByMonic_eq/source-MainLemma.lean.txt). No production, pin, Git, overview or progress edits. No file-end build required at249; last accepted file-end build is Theta228, next MainLemma266.

Original full module replay succeeds, preserving the full target signature: [original-executed.lean.txt](../evidence/Roth.exists_ne_modByMonic_eq/original-executed.lean.txt) and [original-final-receipt.json](../evidence/Roth.exists_ne_modByMonic_eq/original-final-receipt.json). A first cold request was partial and is retained as warming only. Full #print type/body is unelided; independent `Lean.getConstInfo` with `pp.funBinderTypes` gives the full statement below. Original and replay use only propext, Classical.choice, Quot.sound.

## Phase1 — Mathematical statement and proof

For integer multivariate polynomials whose coordinate degrees are bounded by a finitely supported natural function r and whose coefficients lie in [0,B], consider any finite list J of Hasse derivatives. Substitute the same variable in every coordinate and reduce each resulting univariate polynomial modulo a fixed monic integer polynomial f. If every remainder coefficient below degree f has absolute value at most C and `(2C+1)^(degree f × |J|)` is smaller than the number `(B+1)^(finprod (r+1))` of inputs, two distinct inputs have identical complete remainder tuples.

Each parameter has a separate role: σ is arbitrary (not required finite); r controls the monomial box; its finite-support instance ensures the original finite count but is unnecessary for the theorem itself; B bounds source coefficients; f is the common integer divisor and hf makes the first natDegree coefficients determine its remainder; J selects observations; C bounds the target alphabet; hC provides membership in that finite alphabet; hcount is the strict pigeonhole budget.

```lean
∀ {σ : Type u_1} (r : σ → ℕ) [Finite ↑(Function.support r)] (B : ℕ) {f : Polynomial ℤ},
  f.Monic →
    ∀ (J : Finset (σ →₀ ℕ)) (C : ℕ),
      (∀ W ∈ Roth.boxFamily r B, ∀ j ∈ J, ∀ i < f.natDegree, |(Roth.diag ((hasseDeriv j) W) %ₘ f).coeff i| ≤ ↑C) →
        ↑(2 * C + 1) ^ (f.natDegree * J.card) < (↑B + 1) ^ ∏ᶠ (j : σ), (r j + 1) →
          ∃ W' ∈ Roth.boxFamily r B,
            ∃ W'' ∈ Roth.boxFamily r B,
              W' ≠ W'' ∧ ∀ j ∈ J, Roth.diag ((hasseDeriv j) W') %ₘ f = Roth.diag ((hasseDeriv j) W'') %ₘ f
```

Proof: give the box family a finite type using `boxFamily_finite`; encode W by coefficients indexed by `J × Fin f.natDegree` in `Set.Icc (-C) C`. Compute the codomain cardinality using function/product/Fin/interval cardinalities and the source cardinality using `ncard_boxFamily`, transfer the real inequality back to naturals, and apply `Fintype.exists_ne_map_eq_of_card_lt`. Sum coefficient monomials and use `Polynomial.sum_modByMonic_coeff` to recover the full remainder equalities. Distinct subtypes give distinct polynomials.

Direct canonical **type dependencies**: MvPolynomial.hasseDeriv, Roth.diag, Roth.boxFamily. Direct canonical **body dependencies**: MvPolynomial.hasseDeriv, Roth.diag, Roth.boxFamily, Roth.boxFamily_finite, Roth.ncard_boxFamily. Complete used-constant lists, including the generated internal arithmetic proof helper, are in [dependencies.json](../evidence/Roth.exists_ne_modByMonic_eq/dependencies.json); lexical/body/type/kernel scopes are kept separate. The theorem has no simp attribute; the audit does not claim transitive or simp closure.

## Phase2 — Preliminary checks

**BIG**: the module's main-results list explicitly names this pigeonhole step. This is a substantive finite encoding theorem despite its short final collision call. One-line definition test: **n/a**, theorem. No inherited verdict from246 or248 and no verdict based on proof cost.

## Phase3 — Exhaustive literature

| # | Channel | Exact request | Outcome / own summary | Evidence |
|---|---|---|---|---|
| 1 | general1 | `{'search_query': [{'q': 'Roth theorem auxiliary polynomial pigeonhole Hasse derivatives remainders monic polynomial'}], 'response_length': 'short'}` | The specific search located expositions of Roth's auxiliary polynomial construction: multivariable normalized derivatives and remainders supply a finite observation map. No independent named theorem for the exact Lean wrapper emerged. | [web-general1.json](../evidence/Roth.exists_ne_modByMonic_eq/web-general1.json) |
| 2 | general2 | `{'search_query': [{'q': 'finite family polynomial bounded coefficients pigeonhole equal remainders'}], 'response_length': 'short'}` | The polynomial family query located the Princeton Diophantine Analysis seminar notes, whose Roth construction counts coefficient arrays of remainders and applies pigeonhole. Proof complexity results concern another use of polynomial encodings. | [web-general2.json](../evidence/Roth.exists_ne_modByMonic_eq/web-general2.json) |
| 3 | general3 | `{'search_query': [{'q': 'Siegel lemma pigeonhole principle finite observation maps collision cardinality'}], 'response_length': 'short'}` | The abstract form is ordinary finite-map collision; Siegel's lemma is a related linear-algebra application, not the exact selected-remainder statement. | [web-general3.json](../evidence/Roth.exists_ne_modByMonic_eq/web-general3.json) |
| 4 | nlab | `{'search_query': [{'q': 'site:ncatlab.org/nlab pigeonhole principle finite set'}], 'response_length': 'short'}` | Finite sets and FinSet supply the abstract finite-domain viewpoint. No selected Hasse remainder collision theorem was returned. | [web-nlab.json](../evidence/Roth.exists_ne_modByMonic_eq/web-nlab.json) |
| 5 | ncatlab | `{'search_query': [{'q': 'site:ncatlab.org/ncatlab pigeonhole principle finite cardinality'}], 'response_length': 'short'}` | The explicit /ncatlab query returned /nlab material and a de Boor PDF rather than a result in the requested namespace. This is an honest out-of-namespace outcome. | [web-ncatlab.json](../evidence/Roth.exists_ne_modByMonic_eq/web-ncatlab.json) |
| 6 | stacks | `{'search_query': [{'q': 'site:stacks.math.columbia.edu polynomial monic remainder finite coefficients'}], 'response_length': 'short'}` | Search located monic polynomial division and finite free quotient algebra material. These address remainder algebra, not integer coefficient counting for selected Hasse observations. | [web-stacks.json](../evidence/Roth.exists_ne_modByMonic_eq/web-stacks.json) |
| 7 | mathoverflow | `{'search_query': [{'q': 'site:mathoverflow.net Roth theorem auxiliary polynomial pigeonhole principle'}], 'response_length': 'short'}` | A discussion identifies pigeonhole as crucial to Roth's 1955 Lemma 9 and distinguishes this Diophantine use from additive-combinatorial Roth theorems. It does not supply a broader replacement statement. | [web-mathoverflow.json](../evidence/Roth.exists_ne_modByMonic_eq/web-mathoverflow.json) |
| 8 | arxiv | `{'search_query': [{'q': 'site:arxiv.org Roth theorem auxiliary polynomial Hasse derivatives pigeonhole after:2021-10-29 before:2026-10-30'}], 'response_length': 'short'}` | The required date-window query mostly returned additive-combinatorial Roth theorems and unrelated Hasse-principle papers. These are name collisions, not alternative formulations of the present lemma. | [web-arxiv.json](../evidence/Roth.exists_ne_modByMonic_eq/web-arxiv.json) |
| 9 | arxiv-refined | `{'search_query': [{'q': 'site:arxiv.org "Diophantine approximation" "auxiliary polynomial" after:2021-10-29 before:2026-10-30'}], 'response_length': 'short'}` | The refined query for Diophantine approximation and auxiliary polynomials in the same five-year interval returned no results. This does not establish absence. | [web-arxiv-refined.json](../evidence/Roth.exists_ne_modByMonic_eq/web-arxiv-refined.json) |
| 10 | primary | `{'open': [{'ref_id': 'https://web.math.princeton.edu/mathlab/jr02/diophantine.pdf'}, {'ref_id': 'https://aleksa-milojevic.github.io/expository/roth.pdf'}], 'response_length': 'short'}` | Opened the authors' Princeton seminar notes (193 PDF pages, 2003) and Aleksa Milojevic's 2022 exposition (13 pages). Both present auxiliary polynomial constructions; exact coefficient-remainder text is checked separately. | [web-primary.json](../evidence/Roth.exists_ne_modByMonic_eq/web-primary.json) |
| 11 | primary-detail | `{'find': [{'ref_id': 'turn2060view0', 'pattern': 'Pidgeon'}, {'ref_id': 'turn2060view1', 'pattern': 'Pigeonhole'}, {'ref_id': 'turn2060view0', 'pattern': 'Tj1'}], 'response_length': 'short'}` | Princeton notes explicitly encode selected diagonal derivatives by remainders, count all coefficient tuples, and find two distinct inputs with matching tuples. Milojevic instead organizes the construction through a linear system and subtracts two vectors with equal images. These support the distinction between polynomial observation recovery and generic finite collision. | [web-primary-detail.json](../evidence/Roth.exists_ne_modByMonic_eq/web-primary-detail.json) |
| 12 | Local clean.tex | `rg` pigeonhole / remainder counts | §6 proof of Lemma9, equations43–45 and padded nD coefficient arrays | [literature-local.json](../evidence/Roth.exists_ne_modByMonic_eq/literature-local.json), [literature-local-excerpt.txt](../evidence/Roth.exists_ne_modByMonic_eq/literature-local-excerpt.txt) |
| 13 | ask_chatgpt_math | n/a | Optional tool unavailable; not substituted by invented channel | this row |

The ordinary finite-map principle is standard in arbitrary finite sets. The specific application is classical Roth auxiliary-polynomial construction, also reorganized through Siegel-type linear systems. The Princeton authors' [seminar notes](https://web.math.princeton.edu/mathlab/jr02/diophantine.pdf), PDF pages158–159, equations18.15–18.20, directly count selected remainder coefficient arrays. [Milojevic's exposition](https://aleksa-milojevic.github.io/expository/roth.pdf), Section4, instead constructs a bounded kernel vector by subtracting two equal-image inputs. These formulations agree on the collision mechanism and differ in packaging. Neither source requires that observations themselves be Hasse derivatives once the degree/remainder coefficient bounds have been supplied. The local source already separates the quantitative budget into248 and source counting into246.

nLab supplies FinSet/finite sets, not this specialized wrapper. Distinct nCatLab namespace was actually queried and returned out-of-namespace material, not a claimed exact hit. Stacks' returned commutative-algebra locators concern monic division/integral algebras, not this counting application. MathOverflow is supplementary corroboration, not proof authority. The recent arXiv query used **after:2021-10-29 before:2026-10-30**; additive-combinatorial Roth and Hasse-principle results are not this theorem; refined Diophantine query was empty. Search failure is not absence evidence. Only exact requests, response SHA/bytes/status, clean titles/URLs/locators and concise own summaries are persisted; no web article/search bodies.

## Phase4a–b — Generality

| Parameter/hypothesis | Assessment and verified alternative |
|---|---|
| σ / finite support r | **Superfluous premise, actually removed.** σ remains arbitrary. Finite support makes the original domain count finite; the same conclusion without that premise compiles. Infinite support can be handled either by an infinite Xi source or by the constant subfamily because finprod defaults to1. |
| r and boxFamily | Source cardinality is the only property used after encoding. Zero bounds are allowed; tested Unit all-zero bounds have B+1 constant polynomials. General source-family α removes all degree constraints. |
| B : ℕ | A convenient source alphabet parameter, not a collision invariant. Generic finite α removes B. For arbitrary r, including infinite support, B=0 makes the displayed right budget1 and the target count≥1, so strict hcount is impossible. The boxFamily is a singleton then, but no finite-source cardinal interpretation is assumed for B>0/infinite support. |
| f : Polynomial ℤ | Low-degree remainder reconstruction is ring-general (verified over `[Ring R]`), but counting a bounded symmetric interval uses ℤ and its locally finite order. Replacing ℤ by arbitrary ring without a finite coefficient alphabet loses the finite target bound. |
| hf : f.Monic | Essential for unchanged low-degree observation recovery. Full-family counterexample f=C2, r=0 on Unit, B1, J={0}, C0 compiles: bounds vacuous and count1<2, but no distinct pair has equal full remainders. |
| J : Finset (σ→₀ℕ) | Verified replacement by arbitrary finite observation type ι, independent of σ and derivative shape. Empty J is allowed; a concrete collision with f=1 and B1 compiles. |
| C : ℕ | Includes0. A general finite coefficient alphabet / coordinate-dependent codomains is natural; verified abstract finiteObservations takes dependent finite β i. Uniform integer bounds are retained in the substantive polynomial helper, not claimed to be generic ring norms. |
| hC | Needed to land in the finite target. Only coefficients i<natDegree are used; no unnecessary global coefficient bound. |
| hcount | Equivalent natural strict cardinal inequality verified in original recovery. Non-strict inequality cannot guarantee a collision: Fin1 has no distinct pair. |

**Generality verdict: STRICTLY NARROWER THAN STANDARD.** The fixed-interface premise `[Finite (Function.support r)]` is removable: the full theorem with exactly that premise deleted compiles, and exact original recovery/caller replay compile. This is a genuine mechanical weakening, not only a wider representation. Monicity remains essential by the full-family C2 guard. Separately, verified finite α/ι polynomial observations are an API design alternative; an infinite-source version now also compiles without a count hypothesis. The finite and infinite outer map-collision principles already exist in mathlib; the polynomial helpers are **own new proofs**, not found existing replacements.

```lean
theorem finiteObservations {α ι : Type*} [Fintype α] [Fintype ι]
    {β : ι → Type*} [∀ i, Fintype (β i)] (F : α → ∀ i, β i)
    (h : (∏ i, Fintype.card (β i)) < Fintype.card α) :
    ∃ x y, x ≠ y ∧ ∀ i, F x i = F y i := by
  classical
  obtain ⟨x, y, hne, he⟩ := Fintype.exists_ne_map_eq_of_card_lt F (by
    simpa only [Fintype.card_pi] using h)
  exact ⟨x, y, hne, fun i ↦ congrFun he i⟩

theorem polynomialObservations {α ι : Type*} [Fintype α] [Fintype ι]
    (Q : α → ι → Polynomial ℤ) {f : Polynomial ℤ} (hf : f.Monic) (C : ℕ)
    (hC : ∀ x j i, i < f.natDegree → |(Q x j %ₘ f).coeff i| ≤ C)
    (hcount : (2 * C + 1) ^ (f.natDegree * Fintype.card ι) < Fintype.card α) :
    ∃ x y, x ≠ y ∧ ∀ j, Q x j %ₘ f = Q y j %ₘ f := by
  classical
  let F (x : α) (p : ι × Fin f.natDegree) : Set.Icc (-(C : ℤ)) C :=
    ⟨(Q x p.1 %ₘ f).coeff p.2, abs_le.1 (hC x p.1 p.2 p.2.2)⟩
  obtain ⟨x, y, hne, he⟩ := Fintype.exists_ne_map_eq_of_card_lt F (by
    simpa only [Fintype.card_fun, Fintype.card_ofFinset, Int.card_Icc, sub_neg_eq_add,
      Fintype.card_prod, Fintype.card_fin, mul_comm,
      show ((C : ℤ) + 1 + C).toNat = 2 * C + 1 by omega] using hcount)
  refine ⟨x, y, hne, fun j ↦ ?_⟩
  simpa [F, Polynomial.sum_modByMonic_coeff hf Polynomial.degree_le_natDegree] using
    congrArg (fun g ↦ ∑ i : Fin f.natDegree, Polynomial.monomial (i : ℕ)
      (g (j, i) : ℤ)) he

theorem remainderRecover {R : Type*} [Ring R] {f P Q : Polynomial R} (hf : f.Monic)
    (h : ∀ i < f.natDegree, (P %ₘ f).coeff i = (Q %ₘ f).coeff i) : P %ₘ f = Q %ₘ f := by
  rw [← Polynomial.sum_modByMonic_coeff hf Polynomial.degree_le_natDegree (p := P),
    ← Polynomial.sum_modByMonic_coeff hf Polynomial.degree_le_natDegree (p := Q)]
  exact Finset.sum_congr rfl fun i _ ↦ congrArg (Polynomial.monomial (i : ℕ)) (h i i.2)
```

Sources and receipts: [isolated-executed.lean.txt](../evidence/Roth.exists_ne_modByMonic_eq/isolated-executed.lean.txt), [isolated-final-receipt.json](../evidence/Roth.exists_ne_modByMonic_eq/isolated-final-receipt.json), [recovery-executed.lean.txt](../evidence/Roth.exists_ne_modByMonic_eq/recovery-executed.lean.txt), [recovery-receipt.json](../evidence/Roth.exists_ne_modByMonic_eq/recovery-receipt.json). Independent mathlib-only18 has `#check_failure Roth.exists_ne_modByMonic_eq`, no Roth import, no project-only taylor/diag/Hasse definitions. Actual-context recovery supplies the project observation map and existing project cardinality theorem explicitly. No new isolated import was needed; disk9/shared18 stayed stable.

## Completed correction — finite support is removable

The initial published assessment (`c6c9342d`) missed a genuine unchanged-interface weakening. Root review identified the infinite-support branch, and this complete revision supersedes that generality/statement-shape conclusion. Prior accepted sources and receipts are preserved unchanged; historical report/metadata are archived for audit, not used as current claims.

Full native type after deleting **only** the finite-support premise ([generalized-type.json](../evidence/Roth.exists_ne_modByMonic_eq/generalized-type.json)):

```lean
∀ {σ : Type u_1} (r : σ → ℕ) (B : ℕ) {f : Polynomial ℤ},
  f.Monic →
    ∀ (J : Finset (σ →₀ ℕ)) (C : ℕ),
      (∀ W ∈ Roth.boxFamily r B, ∀ j ∈ J, ∀ i < f.natDegree, |(Roth.diag ((hasseDeriv j) W) %ₘ f).coeff i| ≤ ↑C) →
        ↑(2 * C + 1) ^ (f.natDegree * J.card) < (↑B + 1) ^ ∏ᶠ (j : σ), (r j + 1) →
          ∃ W' ∈ Roth.boxFamily r B,
            ∃ W'' ∈ Roth.boxFamily r B,
              W' ≠ W'' ∧ ∀ j ∈ J, Roth.diag ((hasseDeriv j) W') %ₘ f = Roth.diag ((hasseDeriv j) W'') %ₘ f
```

For this noFinite-support form, **finprod(r j + 1) is only a sufficient numerical budget, not the exact cardinality of an infinite boxFamily**. The Phase1 exact source-count explanation above is explicitly about the captured original finite-support theorem. Infinite support forces finprod=1, and the constant subfamily has B+1 choices. No infinite-cardinality formula is asserted.

Two independently accepted proofs establish this exact strengthening:

* **Infinite Xi source:** when support r is infinite, the strict budget forces B>0. For each positive coordinate j, Xj lies in boxFamily r B, and X is injective. The bounded remainder coefficient array has a finite codomain, so existing `Finite.exists_ne_map_eq_of_infinite` gives two different Xi with equal arrays; monic reconstruction gives equal full remainders. No source-count identity is used for the infinite family. Once B>0/infinite support supplies an infinite admissible family and hC supplies a finite observation target, this route dispenses with hcount entirely; the displayed theorem uses hcount only to derive B>0 in that branch. [nofinite-executed.lean.txt](../evidence/Roth.exists_ne_modByMonic_eq/nofinite-executed.lean.txt), [nofinite-receipt.json](../evidence/Roth.exists_ne_modByMonic_eq/nofinite-receipt.json).
* **Preferred constants route:** infinite support of r equals infinite multiplicative support of r+1, so `finprod_of_infinite_mulSupport` gives finprod(r+1)=1. The stated budget therefore only needs B+1 source objects. Use the original finite proof on the zero-degree subfamily, whose finprod is also1, and lift membership to the original family. This uses the default finite-product semantics honestly and avoids an infinitary source construction. [constants-executed.lean.txt](../evidence/Roth.exists_ne_modByMonic_eq/constants-executed.lean.txt), [constants-receipt.json](../evidence/Roth.exists_ne_modByMonic_eq/constants-receipt.json).

The full original MainLemma is replayed with its collision theorem replaced by the preferred strengthening, not by a call to the imported original. Its one actual caller retains its full original signature and no original-target reference. An explicit one-line corollary recovers the exact original theorem type; both that equality and the caller equality are checked natively, and downstream main_lemma keeps standard axioms. [revision-caller-executed.lean.txt](../evidence/Roth.exists_ne_modByMonic_eq/revision-caller-executed.lean.txt), [revision-caller-receipt.json](../evidence/Roth.exists_ne_modByMonic_eq/revision-caller-receipt.json).

Independent mathlib-only18 checks verify the infinite-source generic collision, a newly proved infinite-source polynomial observation helper with only `[Finite ι]`, finprod=1 under infinite support, an actual infinite support example r:ℕ→ℕ all1, and B0 budget impossibility for **arbitrary r without finiteness**. [infinite-isolated-executed.lean.txt](../evidence/Roth.exists_ne_modByMonic_eq/infinite-isolated-executed.lean.txt), [infinite-isolated-receipt.json](../evidence/Roth.exists_ne_modByMonic_eq/infinite-isolated-receipt.json). No import was added. A concrete application with r:ℕ→ℕ all1, B1, f=1 and empty J also compiles through the strengthened theorem, so the infinite-support extension is not vacuous.

Supplemental formal search (all five methods, raw receipts):

| Form | Finder | Loogle | LeanSearch | rg pinned source | Local names |
|---|---|---|---|---|---|
| Infinite source, finite target | [search-infinite-leanfinder.json](../evidence/Roth.exists_ne_modByMonic_eq/search-infinite-leanfinder.json) | [search-infinite-loogle.json](../evidence/Roth.exists_ne_modByMonic_eq/search-infinite-loogle.json) | [search-infinite-leansearch.json](../evidence/Roth.exists_ne_modByMonic_eq/search-infinite-leansearch.json) | [search-infinite-rg.json](../evidence/Roth.exists_ne_modByMonic_eq/search-infinite-rg.json) | [search-infinite-local_search.json](../evidence/Roth.exists_ne_modByMonic_eq/search-infinite-local_search.json) |

The existing generic infinite pigeonhole API is an exact hit, not missing API. The local index still reports error, so no absence claim rests on it. The [official pigeonhole documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Pigeonhole.html) also describes possibly infinite sources; the actual query returned older/mathlib4 snapshots as well, recorded honestly in [web-infinite-supplement.json](../evidence/Roth.exists_ne_modByMonic_eq/web-infinite-supplement.json). Exact pinned Finprod source is archived and included in current mathematical input hashes. Original canonical target type/body/dependencies/consumer counts remain unchanged; strengthening-only direct constants are separate in [revision-dependencies.json](../evidence/Roth.exists_ne_modByMonic_eq/revision-dependencies.json).

Correction preparation failures are not verification: the first full-caller recipe failed its width assertion and one subsequent diagnostics query read the preceding constants source. That stale query is explicitly rejected preparation evidence. The corrected recipe then completed exit0 in a separate tool call before the clean, actual full-caller execution. [revision-preparation.json](../evidence/Roth.exists_ne_modByMonic_eq/revision-preparation.json) records this incident and preserves the exact source/receipt distinctions.

## Phase4c — All nine modern-idiom rows

| # | Question | Answer / reformulation / downstream consequence |
|---|---|---|
| 1 | Typeclasses | Remove Finite support from the original theorem. The proof locally obtains it only in the finite branch. Generic infinite polynomial observations need only `[Infinite α] [Finite ι]`; construct local Fintype ι for coefficient arrays. Both map-collision APIs already exist. |
| 2 | Filters/topology | No: finite combinatorics, no convergence. |
| 3 | Universal property | No new universal-property object is needed; a finite observation function and its collision suffice. |
| 4 | Bundled substructure | boxFamily is not closed under addition and does not become a submodule. A subtype is the right source domain; it can be finite or infinite, while the coefficient-observation codomain is finite. |
| 5 | Hierarchy | Recovery ring-general; finite integer alphabet counting is separate. Arbitrary rings need supplied finite alphabets, not an unjustified ordered-ring weakening. |
| 6 | Higher categories | No higher-categorical content. |
| 7 | Concrete indices | Yes: arbitrary finite observation type ι with finite or infinite source α, both verified. Dropping finite support of r also preserves the original derivative-index form verbatim. |
| 8 | Concrete-via-abstract | Explicit body diagnostic: boxFamily appears twice in executable lines, diag/hasseDeriv in one encoding line, and neither is used by the final coefficient reconstruction. In the original finite-support proof, after setting F only finite cardinalities, bounded coefficients and monic recovery matter; the verified infinite-source variant instead uses infinitude of the source and finiteness of the target. Verified abstraction separates this structure rather than only renaming it. |
| 9 | False-generalization guard | Exact original type and full caller recovered from the noFinite-support theorem. For infinite support, finprod(r+1)=1 is a default, not the cardinality of the infinite polynomial family; never claim the original source-count formula there. Both valid proof routes respect this. Nonmonic C2 still rejects removing hf. |

Modern idiom available: **yes, remove the unnecessary source-finiteness premise and separate finite-target observations from polynomial recovery**. It removes derivative-specific coupling and composes with Fintype Pi cardinality. Existing mathlib already has the generic map theorem; deciding whether the polynomial observation bridge deserves a named API remains the concrete upstream issue.

## Phase4.5 — Infrastructure risks

| Exact risk label | Assessment |
|---|---|
| Typeclass diamond | n/a: theorem adds no instance path. |
| Reducibility leak | n/a: theorem proves Prop, not a new reducible data object. |
| Non-canonical unfolding | n/a: no new definition or simp rewrite. |
| Instance priority collision | n/a: no instance declaration. |
| Universe-polymorphism issues | n/a for definitional infrastructure; original signature and polymorphic replay verified. A rejected locally polymorphic inline attempt was corrected by using the caller's existing σ. |
| Coercion ambiguity | n/a: theorem registers no coercion; subtype coefficient coercions are explicit proof data. |

Overall risk: **n/a — theorem**. Definitions-only `#synth`/reducibility probes do not apply.

## Phase4.6 — Proof strategy

| # | Check | Answer |
|---|---|---|
| 1 | ε–δ vs filters | No topology. |
| 2 | Elements vs substructures | Finite observation encoding is appropriate; forcing an ideal/submodule loses bounded input coefficients. Equality of remainders can be expressed by divisibility, but does not perform the finite counting. |
| 3 | Sequences vs nets | No analytic limits. |
| 4 | Construction vs universal property | No categorical construction; finite Pi target already canonical. |
| 5 | Missing helper API | Potential polynomial-observation collision / finite coefficient alphabet helper. Low-degree reconstruction is already sum_modByMonic_coeff; do not re-propose it as missing. |

Verdict: **REFACTOR-RECOMMENDED**: remove finite support and use the finite-case proof plus the constant subfamily in the infinite-support branch. The infinite Xi proof is an independently verified alternative. Optional polynomial helper extraction separates the reusable finite-target layer. This is a mathematical strengthening and interface choice, not a cost-based downgrade.

## Phase5 — Fifteen actual formal searches

| Form | Finder | Loogle | LeanSearch | rg pinned source | Local names |
|---|---|---|---|---|---|
| current | [search-current-leanfinder.json](../evidence/Roth.exists_ne_modByMonic_eq/search-current-leanfinder.json) | [search-current-loogle.json](../evidence/Roth.exists_ne_modByMonic_eq/search-current-loogle.json) | [search-current-leansearch.json](../evidence/Roth.exists_ne_modByMonic_eq/search-current-leansearch.json) | [search-current-rg.json](../evidence/Roth.exists_ne_modByMonic_eq/search-current-rg.json) | [search-current-local_search.json](../evidence/Roth.exists_ne_modByMonic_eq/search-current-local_search.json) |
| standard | [search-standard-leanfinder.json](../evidence/Roth.exists_ne_modByMonic_eq/search-standard-leanfinder.json) | [search-standard-loogle.json](../evidence/Roth.exists_ne_modByMonic_eq/search-standard-loogle.json) | [search-standard-leansearch.json](../evidence/Roth.exists_ne_modByMonic_eq/search-standard-leansearch.json) | [search-standard-rg.json](../evidence/Roth.exists_ne_modByMonic_eq/search-standard-rg.json) | [search-standard-local_search.json](../evidence/Roth.exists_ne_modByMonic_eq/search-standard-local_search.json) |
| abstract | [search-abstract-leanfinder.json](../evidence/Roth.exists_ne_modByMonic_eq/search-abstract-leanfinder.json) | [search-abstract-loogle.json](../evidence/Roth.exists_ne_modByMonic_eq/search-abstract-loogle.json) | [search-abstract-leansearch.json](../evidence/Roth.exists_ne_modByMonic_eq/search-abstract-leansearch.json) | [search-abstract-rg.json](../evidence/Roth.exists_ne_modByMonic_eq/search-abstract-rg.json) | [search-abstract-local_search.json](../evidence/Roth.exists_ne_modByMonic_eq/search-abstract-local_search.json) |

[formal-search-matrix.json](../evidence/Roth.exists_ne_modByMonic_eq/formal-search-matrix.json) records all15 cells. Exact name search was untruncated: [full-name-search.json](../evidence/Roth.exists_ne_modByMonic_eq/full-name-search.json). All three local searches returned useful source matches with **index:error**; they are not complete index consultations and prove no absence. External indices can differ from the pin. Positive candidate signatures and uses were checked natively in isolated18.

Pinned building blocks: `Fintype.exists_ne_map_eq_of_card_lt` (`Mathlib/Data/Fintype/Pigeonhole.lean:44`), `Polynomial.sum_modByMonic_coeff` (`Mathlib/Algebra/Polynomial/Div.lean:442`), `Fintype.card_fun`, `Fintype.card_pi`, product/Fin/interval cardinalities, and `Int.card_Icc`. Related `Polynomial.exists_eq_polynomial` in `NumberTheory/ClassNumber/AdmissibleCardPowDegree.lean:36` works over a **finite semiring coefficient type** and one finite-indexed polynomial family. ℤ is infinite, and Set.Icc(-C,C) is not a semiring closed under the needed polynomial operations. Thus it does not replace this theorem by setting Fq to an integer interval. `NumberTheory/SiegelsLemma` concerns a bounded linear kernel vector and needs a separate linearization bridge. Source snapshots and pin hashes: [mathlib-inputs.json](../evidence/Roth.exists_ne_modByMonic_eq/mathlib-inputs.json).

The corrected infinite-source abstract form also has a mathlib hit, `Finite.exists_ne_map_eq_of_infinite` at `Data/Fintype/Pigeonhole.lean:74`. Five additional actual queries cover that form; the original finite-only searches are not used as evidence about infinite-source API. The pin and isolated compilation establish the hit independently of external snapshots. No exact entire polynomial application was located. That is a bounded search conclusion, not a universal absence claim. The compiled direct-pigeonhole attempt in recovery is rejected by `fail_if_success`: the whole polynomial codomain has no finite instance/cardinality budget supplied. Encoding and reconstruction must be supplied. No broad timed-out exact? search is counted as success or absence.

## Phase5.5 — Statement shape

**Normal form:** collision `∃ x y, x≠y ∧ F x=F y` is canonical Fintype API; pointwise equality of selected remainders is appropriate for the caller. Equivalent divisibility `f∣diag(Δj(W'−W''))` is useful after subtraction but packages additional additive work. There is no noncanonical iff orientation here; RHS normal-form convention n/a.

**Syntactic generality:** attempted natural budget, arbitrary finite α/ι polynomial observations, dependent finite β i, and full original recovery all compile. Natural card inequality avoids real casts for standalone counting; the original real inequality is convenient for248's analytic budget. Do not change that caller-facing type just for surface brevity.

**Superfluous arguments:** all nine rows in Phase4a cover σ,r/support,B,f/hf,J,C,hC,hcount. **One premise to remove: Finite (Function.support r)**. It is used by the original proof but not required by the conclusion; two actual proofs verify the deletion. B>0, natDegree>0, J nonempty and positive coordinate bounds are deliberately absent; the budget or degenerate observations handle those cases. The explicit full-family C2 guard proves hf cannot be discarded. Overall: **RESTATE-BEFORE-SHIP** at least by deleting finite support; consider the generic polynomial helper separately. This concrete strengthening is recommended independently of the future upstream decision.

## Phase6.0 — Complete callers and inlining

| Caller | Use | Refactor experiment |
|---|---|---|
| private `Roth.exists_mem_RSet_le_index_aux`, MainLemma550, call557 | Select a common pair, subtract into RSet, derive root vanishing, then lower-bound index | Full original module replay removes the named theorem, inserts its entire proof as local collision (using existing caller σ), and leaves caller signature unchanged. |

Proof uses within declaring file:1. External-to-file uses/internal-use count excluding declaring file:0. One docstring reference is not a proof caller. Fresh no-ignore rg and tracked git grep agree; [source-search.json](../evidence/Roth.exists_ne_modByMonic_eq/source-search.json), [tracked-source-search.json](../evidence/Roth.exists_ne_modByMonic_eq/tracked-source-search.json), [callers.json](../evidence/Roth.exists_ne_modByMonic_eq/callers.json). Inline-derivation audit found no separate equivalent proof bypassing this theorem: [inline-search.json](../evidence/Roth.exists_ne_modByMonic_eq/inline-search.json). Canonical kernel-value direct consumer count1; type consumers0. Canonical array derives directly from tracked order, preserving correct private modules, with293 requested/unique/present/values and exact ordered source pre-gate: [canonical-consumers.json](../evidence/Roth.exists_ne_modByMonic_eq/canonical-consumers.json), [canonical-snapshot.json](../evidence/Roth.exists_ne_modByMonic_eq/canonical-snapshot.json).

Original full caller inlining, original signature equality and absence of the original target constant in the new caller value compile cleanly: [inline-executed.lean.txt](../evidence/Roth.exists_ne_modByMonic_eq/inline-executed.lean.txt), [inline-receipt.json](../evidence/Roth.exists_ne_modByMonic_eq/inline-receipt.json). All downstream MainLemma bodies are replayed through main_lemma with standard axioms. This is a readability/API signal, not evidence of <=3 mathlib-call composition. The first inline attempt's fresh local universe was rejected and preserved separately; accepted proof specializes the local helper to the caller's variable type.

## Phase6 — Actual composition experiments

1. Direct existing `Fintype.exists_ne_map_eq_of_card_lt` on the full remainder tuple: compile-guarded failure, because the complete polynomial range is not the bounded finite target and hcount counts coefficient arrays, not all polynomials.
2. Encode bounded coefficients and reconstruct: succeeds in standalone mathlib-only polynomialObservations; this requires constructing a subtype function, normalizing cardinalities, obtaining a collision and reconstructing remainders. This is a new helper proof, not <=3 existing mathlib calls.
3. Specialize that own generic helper with `boxFamily_finite`/`ncard_boxFamily`: exact original recovery succeeds, but both the helper and the source-size bridge are not existing mathlib replacements. Low-degree reconstruction itself already exists.
4. Full original caller inlining succeeds, with the full encoding argument retained.
5. The noFinite-support statement succeeds by both infinite Xi collision and finprod=1/constant-subfamily proofs. The preferred constants proof retains the full original encoding as a local finiteCase, then lifts the zero-degree subfamily. This is a new proof, not <=3 existing mathlib calls. Full-module replay using this stronger theorem and exact-original recovery both succeed.

Conclusion: **NOT-COMPOSABLE** under the <=3 existing-mathlib-call criterion for the **entire original theorem**. Abstract finite-map collision is already mathlib; one must not transfer that NO verdict to the polynomial recovery application without accounting for the bridge.

Edge verification is [guards-executed.lean.txt](../evidence/Roth.exists_ne_modByMonic_eq/guards-executed.lean.txt), [guards-receipt.json](../evidence/Roth.exists_ne_modByMonic_eq/guards-receipt.json), and the isolated/recovery snippets. Empty J and f=1 genuinely admit a collision with zero degree bounds/B1; B0 yields a singleton and impossible strict budget; zero bounds leave B+1 constants. f=C2 has degree0, so its low-coefficient tests are vacuous, yet nonmonic modByMonic leaves inputs unchanged and full-family collision fails. The guard proves all admissible W are constants, not merely that one chosen pair fails. These are accepted kernel proofs, not informal counterexamples.

## Phase7 — Verdict and actionable future decisions

**BORDERLINE-needs-human**, fully reassessed. The finite-support premise should be dropped: this is proved, not a question left to the user. The original is strictly narrower than the verified same-interface theorem. Nevertheless the upstream verdict still concerns whether a Hasse/diagonal theorem over the project boxFamily belongs publicly, or whether a separate finite-alphabet polynomial-observation helper is the right API. Both abstract map collision principles are already mathlib; neither alone supplies polynomial encoding/reconstruction. A verified weakening is necessary for a YES-generalise-first verdict but does not settle mathematical audience/API grain. The retained BORDERLINE verdict is based on that concrete interface choice, not cost or uncertainty about the strengthening.

1. For an upstream API, should the mechanically strengthened noFinite-support Hasse/diagonal statement remain project-local while the reusable polynomial-observation helper is public?
2. Should a public polynomial-observation API use an explicit finite coefficient alphabet and finite-or-infinite source condition rather than the finprod budget, whose value defaults to1 for infinite support?
3. Should the polynomial collision bridge be grouped with bounded-polynomial counting, while both finite-source and infinite-source map collision continue to use existing mathlib pigeonhole theorems?

Next action: remove `[Finite (Function.support r)]` from `Roth.exists_ne_modByMonic_eq` using the compiled constants-route proof, retaining the strengthened Hasse application in MainLemma while designing any standalone polynomial observation helper; keep the existing Fintype pigeonhole theorem as the abstract core. If a generic helper is adopted, derive this specialization using the verified recovery and keep `exists_mem_RSet_le_index_aux`'s real-budget interface. No deletion is justified merely by one use. A provisional upstream home would be `Mathlib/Algebra/Polynomial/Div.lean` only if its import layering can support finite counting; a separate `Mathlib/Algebra/Polynomial/Card.lean` may be cleaner. No YES PR/reviewer/grouping recommendation is asserted before that choice. This is independent of earlier246/248 BORDERLINE verdicts.

## Phase8 — Verification and handoff

Accepted original, isolated, recovery, inline and guards remain unchanged evidence of the original statement. Four additional accepted sources—noFinite Xi, noFinite constants, full revised caller/recovery, and infinite-source isolated mathlib—are complete, clean and use standard axioms only. Partial warm-up, original rejected proofs, correction rejected proofs/warnings and a stale preparation query are retained separately; rejected elaboration sorryAx is not accepted evidence. No limit raises/new axioms/sorry/unsafe/native_decide. Full exact executed sources are `.lean.txt` with original requests/raw receipts/timings. Fresh17 and exact293 order/unique/present/value checks, current copy-manifest, report links, all15 formal cells, all named literature requests, secret guard and actual scratch plus simulated integrated validation are required by [validate.py](../evidence/Roth.exists_ne_modByMonic_eq/validate.py) and [test_layouts.py](../evidence/Roth.exists_ne_modByMonic_eq/test_layouts.py). See [verification.json](../evidence/Roth.exists_ne_modByMonic_eq/verification.json), [validation-result.json](../evidence/Roth.exists_ne_modByMonic_eq/validation-result.json), [secret-guard.json](../evidence/Roth.exists_ne_modByMonic_eq/secret-guard.json). Root independently reviews before any production-document integration/publication; acceptance remains pending.
