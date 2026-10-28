from pathlib import Path
import json
D=Path(__file__).resolve().parent
N='Roth.Θ_le_of_forall_index_le'
def link(n):return f'[{n}](../evidence/{N}/{n})'
t=json.loads((D/'native-type.json').read_text())['type']
s='''# Roth.Θ_le_of_forall_index_le — full assessment190

**NO-mathlib-has-it.** The full mathematical content is the existing `csSup_le`, re-aimed at the independently checked `sSup` parent. The hypothesis already supplies every arithmetic index bound. This differs materially from proving a uniform bound on those indices.

## Phase 0 — baseline

The successful shared build (2467 jobs) is reusable: all17 source/pin SHA256 hashes freshly match the shared baseline. No production changes, pin changes, Git operations, or raised Lean limits were made. Five complete native evidence sets succeeded without errors, warnings, partial elaboration, or nonstandard axioms; isolated proof1 is axiom-free. Native source/receipt paths are retained exactly. An initial Fintype-removal preparation was corrected before execution; it is not a rejected native run.

EVIDENCE0

## Phase 1 — comprehend

Source Roth/Theta.lean:124; theorem, no simp attribute. Read the complete985-line module, both complete callers, and the local Section5 source. Full native elaborated type:

```lean
TYPE
```

`RSet B r` consists of nonzero integer multivariate polynomials with coordinate degree and absolute coefficient bounds. `indexSet` collects their real indices at coprime rational numerator choices; `Θ` is exactly its real `sSup`. Given the pointwise premise `hc`, `csSup_le` only needs nonemptiness. `1≤B` provides the constant-one polynomial with all numerators1. The remaining proof transports `hc` across existential membership witnesses. No quantitative estimate is proved here.

Dependencies (canonical names only): `Roth.Θ`, `Roth.indexSet`, `Roth.indexSet_nonempty`, `Roth.RSet`, `Roth.index`. The full proof uses `csSup_le` and the project nonempty helper, with logical witness elimination.

EVIDENCE1

## Phase 2 — size and definition-only test

SMALL: three tactic lines; pure least-upper-bound elimination once the actual bound is supplied. Definition-only one-line test: n/a, theorem. No infrastructure-stability exemption is needed. Two explicit consumers make this useful local convenience API, but do not make the supremum law novel.

## Phase 3 — exhaustive literature

| Channel | Actual request/outcome | Consequence |
|---|---|---|
| General web current | `Roth theorem polynomial index taking supremum upper bound` | No exact standalone Roth helper located; batching also returned generic completeness material. |
| General web standard | `least upper bound supremum nonempty set upper bound property` | Yale course notes Chapter4 p78 and UPenn Advanced Analysis completeness describe supremum as least upper bound. |
| General web abstract | `conditional complete lattice supremum empty set convention` | Conditional completeness and empty/unbounded junk-value distinctions surfaced. |
| ChatGPT mathematics | n/a: no callable ask_chatgpt_math tool | No synthetic external opinion invented. |
| Local clean.tex | Fresh rg on supremum/Theta and Section5 excerpt | Definition of Θ and Lemma5 proof take a supremum of already established pointwise inequalities. |
| nLab | Actual `site:ncatlab.org/nlab supremum least upper bound`; direct supremum open | Search returned nLab material; direct open cache miss honestly retained. |
| Distinct nCatLab | Actual `site:ncatlab.org/ncatlab supremum lattice`; direct namespace open | Search primarily returned out-of-namespace nLab; direct nCatLab inaccessible. No exact namespace hit claimed. |
| Stacks | Actual `site:stacks.math.columbia.edu supremum upper bound` | No exact law established. Supplementary direct tags005Y and09E1 were unrelated Jacobson/Nagata statements and rejected. |
| MathOverflow | Actual `site:mathoverflow.net supremum empty set real numbers` | Questions/comments distinguish extended-real empty supremum from real conventions; no new Roth law. |
| Recent arXiv | Actual `site:arxiv.org supremum conditionally complete lattice after:2021-10-27` | arXiv2608.20848 (21Aug2026), abstract: sup-inf completion of Dedekind complete vector lattices; adjacent general theory, not this elementary elimination law. |

Literature-standard formulation: if S is nonempty and c bounds all its members, then supS≤c. The upper-bound premise itself proves boundedness. Literature often leaves empty real suprema undefined; Lean returns0, so preserving the side condition is necessary when interpreting the theorem. No source claims a special independent theorem about the supplied-index-bound wrapper. UPenn direct access was403, retained separately; no inaccessible source body is treated as read. Web artifacts contain exact requests, response SHA256/bytes/status, sanitized locator URLs, and original concise summaries only; no full external bodies or credentials are archived.

EVIDENCE3

## Phase 4a — parameter audit

| Parameter | Role and attempted scope |
|---|---|
| universe/σ | Arbitrary Typeu already; no finite numeral index restriction. |
| Fintypeσ | Required by the fixed Θ/index signatures. An unexecuted removal draft was rejected before Lean. Abstract generic sSup law has no Fintype, but changes the interface. |
| DecidableEqσ | Already omitted in source and full native type. |
| B:ℝ | Arbitrary real with hB:1≤B; hB supplies nonempty admissible family, no upper restriction. |
| q:σ→ℕ | Arbitrary natural vector; coprimality is supplied pointwise, no positivity needed by this law. |
| r:σ→ℕ | Arbitrary natural weights including zero; no positive-weight hypothesis is used. |
| c:ℝ | Arbitrary upper bound, may be negative syntactically; hB+hc constrain valid cases. |
| hc | Full uniform index bound; essential. This theorem cannot manufacture it. |

## Phase 4b — generality

STRICTLY NARROWER THAN STANDARD as a mathematical schema: `csSup_le` works over an arbitrary conditionally complete lattice and arbitrary nonempty set. This general form already exists, so no generalise-first contribution follows. The exact old-form specialization compiled. A separate verified alternative replaces hB by0≤c using `Real.sSup_le`; this changes the explicit premise, and is not an unconditional deletion. Under hc we additionally proved `Θ B q r ≤ c ↔ 0≤c`, using project Θ_nonneg forward and Real.sSup_le backward. This sharp project-context observation is a new local proof, not an existing-call replacement claim. The generic empty set/c=-1 counterexample verifies the abstract empty-default guard. A separate accepted actual Roth counterexample proves RSet0r=∅ from a nonzero integer coefficient having absolute value at least1, then supplies hc at B=0,c=-1 vacuously while Θ0q r=0 is not≤-1. Thus deleting hB with unrestricted c is false. The family-only emptiness lemma omits Fintype legitimately; the actual Θ counterexample preserves it. Retain current local API unchanged in this read-only assessment.

## Phase 4c — all modern idiom rows

| # | Question | Answer / downstream consequence |
|---|---|---|
|1| Typeclasses | Yes: conditionally complete lattice is the right generic structure, already `csSup_le`; reusable for other value types. |
|2| Filters/nets | No convergence or metric arguments occur. |
|3| Universal property | Yes: the least-upper-bound elimination law is exactly csSup_le; no object construction needed. |
|4| Bundled substructure | No closure predicate; plain sets are correct, no submodule/ideal exists here. |
|5| Weaken hierarchy | Yes: real-specific law abstracts to ConditionallyCompleteLattice. Fixed polynomial coefficient representation remains local. |
|6| Higher categories | No categorical data or coherence statement. |
|7| Concrete indices | Yes: arbitrary target ordered lattice replaces ℝ at the schema level; generic probe compiles. |
|8| Concrete-via-abstract diagnostic | Fires: proof body contains zero Θ/index operations after csSup_le application, only nonempty witness source and hc transport. Generic csSup_le is already present. |
|9| False-generalization guard | Conditional-lattice restatement preserves the nonempty supremum law. Reject interpreting ℝ as CompleteLattice, changing empty supremum to minus infinity, or deleting hB with no replacement condition. |

Modern idiom available, already in mathlib: `csSup_le hs hc`. Concrete gain is direct use of the standard upper-bound API and Set.image2 predicate transport without Roth-specific names. No new abstraction PR warranted.

## Phase 4.5 — infrastructure risks

n/a: theorem. All six definition/instance risks—typeclass diamond, reducibility leak, noncanonical unfolding, instance priority, universe-polymorphism infrastructure, coercion ambiguity—introduce no new definition/instance/coercion paths here. Parent Θ semantics were separately inspected via a fresh rfl bridge; not inherited as a theorem-risk claim.

## Phase 4.6 — proof strategy

| # | Test | Finding |
|---|---|---|
|1| ε-δ versus filters | n/a: no topology. |
|2| Element algebra versus bundled inclusion | n/a: no algebraic closure reasoning. |
|3| Sequences versus nets | n/a: no limit. |
|4| Construction versus universal property | Already uses supremum universal-property elimination directly. |
|5| Missing helper API | None for upper bound law or image2 quantifier transport. Nonemptiness arithmetic is project-specific, not a missing generic lattice theorem. |

MATHLIB-IDIOMATIC strategy. Refactor recommendation concerns deleting a redundant local wrapper, not replacing the proof method. No cost-based verdict reasoning.

## Phase 5 — actual five-method searches

All five methods executed on current, standard, and abstract forms. Exact requests/results and one corrected Loogle retry are archived.

| Method | Current | Standard | Abstract |
|---|---|---|---|
| Finder | Roth polynomial index supremum query returned unrelated Roth-number/Chevalley bounds | Exact csSup_le, ConditionallyCompleteLattice.csSup_le | Finset binary sup laws and iSup_image2; distinct structures, not exact real parent |
| Loogle | `sSup ?s ≤ ?c` finds complete-lattice sSup_le plus directed partial-order laws | `csSup_le` exact hit | Initial `Set.image2, sSup` parser error; corrected `Set.image2, "sSup"` finds complete-lattice sSup_image2; no claim usable onℝ |
| LeanSearch | Current prose returned irrelevant polynomial degree/finite-sup facts | ConditionallyCompleteLattice.csSup_le and Real.sSup_le | Finset sup binary laws, Real.iSup_le, mem_upperBounds_image2 with different monotonicity premises |
| rg | Full target/name patterns: no mathlib Roth helper | Pinned csSup_le and Real.sSup_le declarations | forall_mem_image2 / complete-lattice image laws |
| Local names | Target search index unavailable | csSup_le family positive source hits despite unavailable global index | Set.forall_mem_image2 positive source hit |

Conclusion: found in mathlib as `csSup_le`, more general form; Mathlib/Order/ConditionallyCompleteLattice/Basic.lean:201. `Real.sSup_le` is an alternative at Mathlib/Algebra/Order/Archimedean/Real/Basic.lean:222 with0≤c (the former Data/Real/Archimedean module is only a forwarding import). External index revisions can differ; all accepted positive candidates are pinned and native checked. No global absence claim is made. Generic isolated proofs compile with no Roth import and explicit `#check_failure Roth.Θ_le_of_forall_index_le`.

EVIDENCE5

## Phase 5.5 — statement shape

Normal forms compared: sSup(indexSet)≤c; pointwise upper-bound predicate; binary image2 pointwise predicate; Real.sSup_le with0≤c. Canonical form is csSup_le on a nonempty Set. The rfl Θ bridge and image2 transport are independently checked. This is an implication, so RHS iff convention is n/a. Syntactic generality: old witness-wise hc is convenient for the two callers; abstract Set upper-bound form is canonical upstream. Every argument is audited in4a; Fintype is a fixed-parent constraint, DecidableEq already absent, and hB is replaced only in the explicitly compiled alternative. No unconditional arguments to drop. Overall RESTATE-BEFORE-SHIP as abstract csSup_le—but already present, so do not ship this wrapper upstream.

## Phase 6.0 — exhaustive caller and inline audit

Fresh `rg --no-ignore` scoped to production Roth/ and Roth.lean agrees with tracked `git grep`; canonical inventory independently checked. Three lexical lines: declaration124, applications258 and599. Two distinct callers, two occurrences, zero outside declaring file, zero statement mentions. Contract's internal-use count excluding the declaring file is0; total production applications is2. Kernel audit reports the same two direct value consumers and zero direct type consumers among exactly293 ordered canonical declarations; this is not a transitive/simp closure claim.

| Caller | Pattern | Actual full replay / refactor |
|---|---|---|
| Roth.Θ_unique_le, Theta:258 | `Θ_le_of_forall_index_le hB fun _ hR _ hh ↦ …` | Use csSup_le with indexSet_nonempty; unpack R,hR,h,hh,equality; preserve private index_unique_le_log_div proof. Full statement compiled using a permitted term elaborator referring to the original existing private constant, introducing no axiom. |
| Roth.Θ_option_le, Theta:599 | `refine Θ_le_of_forall_index_le hB fun R hR h hh ↦ ?_` | Refine csSup_le with indexSet_nonempty, rintro witnesses, retain complete index_le_lem6 / Finset.le_sup' continuation. Full exact conclusion compiled. |

Inline audit: Θ_le_card:114 uses Real.sSup_le with a substantive uniform degree/index bound, and Θ_mono:135 uses csSup_le_csSup. These are analogous supremum mechanics with different premises/conclusions, not overlooked duplicate callers. The target itself uses csSup_le:128. No further exact old helper theorem rederived inline was found in the canonical production inventory. The wrapper is not dead and has no simp attribute.

EVIDENCE6

## Phase 6 — actual composition and parent re-aim

Fresh exact bridge: `Roth.Θ B q r = sSup (Roth.indexSet B q r) := rfl`. Existing abstract proof:

```lean
example {α : Type*} [ConditionallyCompleteLattice α] {s : Set α} {c : α}
    (hs : s.Nonempty) (hc : ∀ x ∈ s, x ≤ c) : sSup s ≤ c := csSup_le hs hc
```

The whole original theorem, with its full hc premise and hB, follows by the one-line term below (compiled as named proof1):

```lean
csSup_le (Roth.indexSet_nonempty hB q r)
  (fun _ ⟨R, hR, h, hh, he⟩ ↦ he ▸ hc R hR h hh)
```

Honest call accounting: one existing mathlib call csSup_le, one project helper indexSet_nonempty, logical existential elimination/equality substitution. The project helper is not counted as a mathlib building block, and this is not claimed as a strict all-mathlib ≤3-call proof of the entire old presentation. No closing simp composition is the basis of the verdict. Under the verified image2 parent, `csSup_le hst (Set.forall_mem_image2.mpr hc)` compiles in isolation: two mathlib calls with nonemptiness supplied. Thus the mandatory parent re-aim gate hits an exact existing law. COMPOSABLE on the re-aimed standard form; the old spelling additionally requires its local nonemptiness bridge. Full caller replays verify mechanical replacement at both real consumers without using the target.

## Phase 7 — actionable verdict

**NO-mathlib-has-it**, independently justified by `csSup_le` and exact parent bridge. Mathlib already has the analogous law for the parent sSup; the theorem's supposed arithmetic content is supplied entirely by hc. Re-aim rule prevents misclassifying presentation normalization as missing upstream API. The preceding Θ_le_card assessment is not inherited: it must establish its arithmetic bound, whereas this statement assumes that bound.

Do not upstream this helper. For a separately authorized cleanup, delete it and update exactly the two sites listed above. At Θ_unique_le replace the target application by csSup_le(indexSet_nonempty hB q r), unpack indexSet witnesses and use the unchanged private estimate. At Θ_option_le insert the same csSup_le/rintro prefix and keep its existing complete continuation. Native caller proofs archive the exact refactor. Existing generic building blocks: csSup_le (ConditionallyCompleteLattice/Basic), Real.sSup_le (Algebra/Order/Archimedean/Real/Basic:222), Set.forall_mem_image2 (Data/Set/NAry); the last two explain alternatives rather than being required for the old proof. If retaining the spelling for local exposition, its alternative destination is Roth/Theta.lean next to Θ; no Archive or external downstream library is warranted for a project-specific wrapper. No production deletion is performed by this assessment.

## Phase 8 — evidence and delivery

All mandatory phases complete; unresolved[]. The portable validator checks current manifests, all17 fresh hashes, pinned sources, canonical293 exact order including private names, five clean complete native evidence sets plus separately rejected diagnostics, standard axioms, all search forms, complete caller coverage, local links and credential guard. Integration acceptance remains pending root's independent review. No YES PR grouping/reviewer selection is applicable to this NO result.

EVIDENCE8
'''
s=s.replace('TYPE',t)
for k,ns in {'0':['baseline-build.txt','source-hashes.json','input-manifest.json','preparation-not-executed.json'],'1':['Theta.lean.txt','native-type.json','theta-upper190-original-receipt.json'],'3':['web0-metadata.json','web1-metadata.json','web2-metadata.json','web3-metadata.json','web4-metadata.json','local-literature.json','clean-section5-excerpt.tex.txt'],'5':['formal-search.json','rg-current.json','rg-literature.json','rg-abstract.json','mathlib-inputs.json','theta-upper190-isolated-receipt.json'],'6':['callers.json','callers-rg.json','callers-git.json','inline-audit.json','theta-upper190-callers-sharp-receipt.json'],'8':['verification.json','assessment.json','overview-entry.json','theta-upper190-actual-guard-receipt.json','theta-upper190-actual-guard-rejected-receipt.json','validate.py','copy-manifest.json']}.items():s=s.replace('EVIDENCE'+k,'Evidence: '+', '.join(link(n)for n in ns)+'.')
(D/'report.md').write_text(s)
