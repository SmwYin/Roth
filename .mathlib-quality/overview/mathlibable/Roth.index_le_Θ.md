# Roth.index_le_Θ — NO-mathlib-has-it

Canonical187; `Roth/Theta.lean:99` on `ramin-cleanup`. Assessment complete; root acceptance pending.
The parent Θ is exactly `SupSet.sSup`, and its analogous member-below-supremum law already exists as
`le_csSup`. This is a re-aim result after independently verifying both law and representation, not a
claim that the arithmetic boundedness theorem is already in mathlib.

## Phase 0 — Baseline

Clean baseline: 2467 jobs, reused only after fresh hashes of all17 source/pin files match shared
manifest. Declaration resolves with no sorry and only propext, Classical.choice, Quot.sound.
The complete985-line Theta module and complete actual caller bodies were read. Module develops
bounded polynomial-index suprema and source Lemmas5–7.
[Build](../evidence/Roth.index_le_Θ/baseline-build.txt); [fresh hashes](../evidence/Roth.index_le_Θ/source-hashes.json);
[original native receipt](../evidence/Roth.index_le_Θ/index-le-theta187-original-receipt.json).

## Phase 1 — Mathematical content and full type

An admissible nonzero integer polynomial has bounded degree and coefficients. Its weighted index at
any rational point represented by numerators coprime to the prescribed denominators belongs to the
family whose supremum is Θ; hence that index is at most Θ. Boundedness of the family is needed for
this real conditional-supremum operation. The theorem adds no coefficient or root estimate.

```lean
∀ {σ : Type u_1} [inst : Fintype σ] {B : ℝ} {q r : σ → ℕ} {R : MvPolynomial σ ℤ},
  R ∈ Roth.RSet B r →
    ∀ {h : σ → ℤ},
      (∀ (j : σ), IsCoprime (h j) ↑(q j)) →
        Roth.index ((map (Int.castRingHom ℝ)) R) (fun (j : σ) ↦ ↑(h j) / ↑(q j)) r ≤ Roth.Θ B q r
```

Parameters: σ indexes variables; Fintype supplies finite index infrastructure and the uniform card
bound; B bounds coefficients; q prescribes denominators; r weights degrees; R is the polynomial;
h supplies numerators. Hypotheses hR and hh supply membership. No DecidableEq, `1 ≤ B`, positive
weights or positive denominators are assumed. Full proof is
`le_csSup (indexSet_bddAbove B q) ⟨R, hR, h, hh, rfl⟩`.
[Type](../evidence/Roth.index_le_Θ/native-type.json); [full module](../evidence/Roth.index_le_Θ/source-Theta.lean.txt).

## Phase 2 — Preliminary checks

SMALL: structural helper, no new mathematical structure or named/main theorem.
One-line definition test n/a: theorem. The one-line proof is evidence of direct reuse, not the
one-line-definition prefilter; all remaining phases ran.

## Phase 3 — Exhaustive literature

Every named channel was actually queried. At least three distinct general web forms were run.
Exact requests and response hashes/byte counts are archived; full returned bodies are not.

| Channel | Exact query or locator | Finding and limitation |
|---|---|---|
| Web specific | Roth polynomial index Theta supremum individual index bounded coefficient | Older Thue–Siegel–Roth notes surfaced; no new membership-supremum principle |
| Web general | least upper bound element bounded above supremum conditionally complete lattice | Conditional completeness and upper-bound property |
| Web alias | supremum upper bound property least upper bound axiom | Standard supremum / least upper bound terminology |
| ChatGPT MCP | n/a | ask_chatgpt_math unavailable; no fabricated consultation |
| Local | clean.tex §5, supremum / Theta / Theta_m | Defines Θ as supremum; individual bound is its defining upper-bound property |
| nLab | site:ncatlab.org/nlab supremum | join / upper bound / Dedekind completion analogs; direct join open unsupported XHTML |
| nCatLab | site:ncatlab.org/ncatlab supremum order | Explicit distinct namespace queried; results mostly nLab pages, not an exact namespace hit |
| Stacks | site:stacks.math.columbia.edu supremum ordered set; tag05N1 | Ordinal supremum analog, lines20–21; not polynomial arithmetic |
| MathOverflow | site:mathoverflow.net supremum bounded above element | Bounded real family discussion, question375759; contextual analog |
| Recent arXiv | site:arxiv.org Roth theorem polynomial index after:2021-10-27 before:2026-10-28 | 2026 weighted projective lines paper and additive-combinatorial Roth homonyms; no change to generic supremum law evidenced |

Primary Penn analysis notes search result identifies least-upper-bound definition; direct open failed
HTTP403. nLab join direct open failed content-type support. Stacks open succeeded. Initial arXiv
query returned a2017 paper outside the five-year window; a distinct date-bounded retry was executed
and documented. Search results cannot establish literature absence.

Standard form: in a partially ordered setting, every member lies below a supremum when it exists;
conditional completeness obtains it for inhabited bounded sets. In Lean the given member itself
supplies inhabitance. Neither finiteness, polynomial structure, coefficients nor coprimality belongs
to the generic order law. The source specialization agrees with this form.

[General web requests](../evidence/Roth.index_le_Θ/web-0.json); [named sources](../evidence/Roth.index_le_Θ/web-1.json);
[primary opens and date retry](../evidence/Roth.index_le_Θ/web-primary.json);
[local search](../evidence/Roth.index_le_Θ/local-literature.json); [§5 excerpt](../evidence/Roth.index_le_Θ/clean-section5-excerpt.tex.txt).
Primary locators: [Penn completeness](https://www2.math.upenn.edu/~gressman/analysis/01-completeness.html),
[nLab join](https://ncatlab.org/nlab/show/join),
[Stacks05N1](https://stacks.math.columbia.edu/tag/05N1),
[MO375759](https://mathoverflow.net/questions/375759/can-we-take-a-supremum-over-all-hilbert-spaces).

## Phase 4a — Parameter-by-parameter generality

| Parameter/hypothesis | Fixed project interface | Expanded generic interface |
|---|---|---|
| σ, Fintype σ | Index and uniform card-bound infrastructure; no verified direct removal claimed | Arbitrary type/universe for ordered codomain; no Fintype |
| B : ℝ | Coefficient restriction selecting family | Arbitrary subset s |
| q : σ→ℕ | Rational-point family restriction; zero allowed | Arbitrary function arguments |
| r : σ→ℕ | Weight/degree restriction; zero allowed | Arbitrary function arguments |
| R : MvPolynomial σ ℤ | Selected polynomial | Arbitrary member x |
| hR : R∈RSet B r | Supplies first family witness; hidden R≠0 removable in verified allow_zero extension | Membership x∈s; separate zero branch needs Θ_nonneg |
| h : σ→ℤ | Selected numerator | Arbitrary argument b |
| hh : ∀j, IsCoprime ... | Supplies second admissibility witness | Membership b∈t |
| implicit boundedness | Project indexSet_bddAbove proves substantive uniform arithmetic bound | Explicit hs : BddAbove s |

## Phase 4b — Verified generality conclusion

STRICTLY NARROWER in one verified hidden-hypothesis dimension: the nonzero conjunct inside hR can
be dropped when retaining the degree/coefficient/coprimality conditions. The native allow_zero theorem
handles R=0 by zero_index and the independent Θ_nonneg, and nonzero R by the checked replacement.
This optional real-zero-default extension is distinct from the original supremum-member law.
It specifically uses the real-valued index default0 and asserts no infinity-valued index inequality
at R=0.
Expanded generic representation is mechanically verified with arbitrary universes
and `ConditionallyCompleteLattice γ` by `le_csSup hs hx`; it already exists. This is a representation
re-aim, not a claimed one-edit polynomial generalization or a new helper contribution.
[Isolated source](../evidence/Roth.index_le_Θ/index-le-theta187-isolated-executed.lean.txt);
[isolated clean receipt](../evidence/Roth.index_le_Θ/index-le-theta187-isolated-receipt.json).

## Phase 4c — Nine modern-idiom checks

| # | Check | Answer and evidence |
|---|---|---|
|1| Typeclass preambles | Yes for abstract order structure: existing ConditionallyCompleteLattice; no custom predicate class needed |
|2| Sequences/metrics to filters | No topology or convergence |
|3| Construction to universal property | Yes: supremum upper-bound law le_csSup; Θ itself stays exact sSup |
|4| Set predicates to bundled substructure | No closure substructure; admissibility is a selected set |
|5| Field to weaker algebra | Order layer independent of field operations; no claim polynomial index itself works over arbitrary lattice |
|6| Higher categories | No categorical structure |
|7| Concrete numeric index | Yes: ℝ upper-bound result is existing arbitrary conditionally complete lattice theorem |
|8| Concrete-via-abstract diagnostic | Yes: body contains Θ/index/RSet zero times; only one project boundedness call and membership witness; actual generic proof verified |
|9| False-generalization guard | Preserve BddAbove. Native real-univ counterexample disproves unrestricted member≤sSup; no unbounded/complete-lattice conflation |

Modern idiom is existing le_csSup; benefit is using common order API and avoiding duplicate laws
for every named supremum. Image2 bridge and actual `Set.mem_image2_of_mem hR hh` independently pass.

## Phase 4.5 — Infrastructure risk

n/a: theorem introduces no definitions, coercions or typeclass instances. All six definition-only
rows (diamond, reducibility leak, noncanonical unfolding, priority, universe forcing, coercion
ambiguity) are inapplicable. No definition/instance proposal is made.

## Phase 4.6 — Five proof-strategy checks

| # | Question | Finding |
|---|---|---|
|1| Topology ε–δ to filters | n/a; no topology |
|2| Element algebra to substructure inclusions | n/a; selected set membership is appropriate |
|3| Sequences to nets | n/a; no limits |
|4| Construction to universal property | Already supremum upper-bound property |
|5| Missing helpers mathlib should have | No missing generic law; substantive project boundedness kept separate |

MATHLIB-IDIOMATIC: one existing le_csSup call. No cost-based downgrade. Arithmetic bound APIs remain
a separate design question already identified at186, not hidden inside generic order claims.

## Phase 5 — All five methods on three forms

| Method | Current Roth form | Literature-standard form | Abstract form |
|---|---|---|---|
| Finder | Polynomial/Roth/Θ natural-language query | Member of bounded set below supremum | Bounded image2 value below supremum |
| Loogle | Roth.index_le_Θ request failed; broad quoted-index retry gives irrelevant Lean core hits | Initial le_csSup request rate-limited; later exact retry returned le_csSup | BddAbove/sSup requests failed unknown sSup; qualified SupSet.sSup retry first rate-limited, later succeeds with conditional-lattice isLUB constructors/laws |
| LeanSearch | Current natural-language query | Member of bounded set below supremum | Abstract bounded image2 query |
| rg | index_le_Θ/Roth.Θ/indexSet absent in pinned mathlib text | le_csSup and mem_image2_of_mem located | Generic le_sSup/conditional-lattice variants located |
| local | index_le_Θ project hit | le_csSup family hit | mem_image2_of_mem hit |

All15 actual cells ran; complete12 API responses plus3 CLI receipts archived, together with honest
Loogle retry receipts. Current-form Finder/LeanSearch primarily return additive-combinatorial Roth
homonyms and unrelated polynomial bounds, not the target; standard-form searches locate le_csSup. Local name search
reports index unavailable even while returning source-derived candidates; this is not absence
proof. External search may index a different revision. Pinned source and native #check/proofs are
authoritative. Positive result is `le_csSup`, more general law, exact pinned signature
`[ConditionallyCompleteLattice α] → BddAbove s → a∈s → a≤sSup s`.
`le_sSup` complete-lattice law is an analog, not applicable to ℝ by assuming a nonexistent instance.
[Formal raw responses](../evidence/Roth.index_le_Θ/formal-search.json);
[Loogle retries](../evidence/Roth.index_le_Θ/formal-loogle-retry.json);
[rate-limited abstract retry](../evidence/Roth.index_le_Θ/formal-loogle-abstract-retry.json);
[successful qualified abstract search](../evidence/Roth.index_le_Θ/formal-loogle-qualified.json); [pinned positives](../evidence/Roth.index_le_Θ/formal-positive.json);
[rg current](../evidence/Roth.index_le_Θ/rg-current.json); [rg standard](../evidence/Roth.index_le_Θ/rg-standard.json);
[rg abstract](../evidence/Roth.index_le_Θ/rg-abstract.json).

## Phase 5.5 — Three statement-shape checks

Normal form: both direct set membership and image2 membership are usable; canonical order form is
`a ≤ sSup s`, already le_csSup. Θ unfolds definitionally, and indexSet=image2 bridge is rfl; exact
witness packaging is verified, not assumed. RHS inequality orientation is already standard.
Syntactic generality: direct existential witness is shortest for old callers; image2 representation
composes with Set.mem_image2_of_mem. Both actual project probes pass. Superfluous arguments:
Fintype remains fixed-index infrastructure; hR and hh supply membership; no DecidableEq or positivity
appears in full native type. The hidden R≠0 conjunct is removable by the actual allow_zero proof,
which retains degree/coefficient bounds and hh and adds a zero case using Θ_nonneg. No other
unverified weakening is claimed. RESTATE-BEFORE-SHIP upstream
means use existing generic law; local project spelling is useful but duplicates that law.

## Phase 6.0 — Every explicit caller and inline audit

| File:line | Caller declaration | Usage / exact substitution plan |
|---|---|---|
| Theta443 | private index_separated_mul_le_aux | hUΘ; replace `index_le_Θ hU ...` by `le_csSup (indexSet_bddAbove M _) ⟨U,hU,...,rfl⟩` |
| Theta445 | same private declaration | hVΘ; Unit-variable V′ witness with explicit q/h |
| MainLemma760 | main_lemma | linarith bound on W; same le_csSup bound and W/hW/h/hh witness |

Three call occurrences, two declaration bodies, two files; one external-to-declaring-file occurrence
in one file. Exact inventory/no-ignore rg agrees with tracked Git cross-check. Canonical293 audit:
two direct kernel-value consumers and zero direct type consumers; this is not transitive/simp
closure. No equivalent index≤Θ inline rederivation was found; other supremum bounds have different
directions/content. This useful local helper is not dead code.

Both complete caller bodies were replayed natively after target-call substitution with the verified
replacement, retaining all mathematics. Main caller's private prerequisites are accessed by two
term elaborators returning existing mkPrivateNameCore constants; these introduce no axiom. These
are full caller replays, not merely expression checks, and all three target occurrences are covered.
[Lexical inventory](../evidence/Roth.index_le_Θ/callers.json); [Git cross-check](../evidence/Roth.index_le_Θ/index-le-theta187-git-callers.json);
[structured calls](../evidence/Roth.index_le_Θ/callers-structured.json); [inline audit](../evidence/Roth.index_le_Θ/inline-audit.json);
[exact caller execution](../evidence/Roth.index_le_Θ/index-le-theta187-callers-executed.lean.txt);
[caller receipt](../evidence/Roth.index_le_Θ/index-le-theta187-callers-receipt.json).

## Phase 6 — Actual composition experiments

1. Old form: `le_csSup (Roth.indexSet_bddAbove B q) ⟨R,hR,h,hh,rfl⟩` passes. Honest count:
   one existing mathlib call, one project theorem call, existential/pair constructors and rfl.
2. Parent re-aim: arbitrary set member `le_csSup hs hx` passes mathlib-only. It is the analogous law
   of exactly sSup. For image2, `le_csSup hs (Set.mem_image2_of_mem ha hb)` passes with two mathlib
   calls; actual polynomial/numerator image2 bridge and membership pass separately.
3. Full arithmetic side condition is not silently replaced. indexSet_bddAbove uses index_le_card,
   nonzero preservation of integer→real map and degree transfer. It remains substantive project
   arithmetic (accepted186 BORDERLINE, index_le_card150 BORDERLINE). No ≤3 mathlib-only old-form
   arithmetic proof is claimed. This does not negate a verified existing analogous parent law.
4. Verified hidden nonzero weakening: allow_zero retains degree/coefficient/coprimality restrictions,
   splits R=0, uses zero_index=0 and independent Θ_nonneg, and otherwise checked replacement. This
   is a real-default extension, not direct membership for the zero polynomial.
5. Guard: without BddAbove, take real univ and member1; real unbounded sSup=0 contradicts1≤0.
   Exact guard and both full callers pass natively with standard axioms.

No closing simp composition is used as a NO argument. No failed-search absence conclusion is made.
Re-aim rule applies because the analogous generic law itself is independently verified; merely
having component API would not suffice.
[Project probes](../evidence/Roth.index_le_Θ/index-le-theta187-project-executed.lean.txt);
[project receipt](../evidence/Roth.index_le_Θ/index-le-theta187-project-receipt.json).

## Phase 7 — Actionable verdict

**NO-mathlib-has-it**, by verified parent re-aim to `le_csSup` in
`Mathlib/Order/ConditionallyCompleteLattice/Basic.lean:197`.
Existing blocks: le_csSup; for image2 spelling Set.mem_image2_of_mem. Θ=sSup is definitional;
indexSet=image2 is definitional; exact polynomial/numerator membership is mechanically checked.
Project indexSet_bddAbove is an explicit substantial side condition, not an existing mathlib block.

Do not propose another upstream member-below-supremum theorem. Inline the concrete one-call term
at each of the three occurrences following the table, retaining the arithmetic boundedness proof;
or retain this named convenience locally in `Roth/Theta.lean`. Its local ergonomic usefulness does
not justify duplicate generic upstream API. This read-only assessment makes no production changes.
YES-only PR path/title/group/reviewer tasks are n/a. The optional verified allow_zero extension drops nonzero using the real index default at zero and
independent Θ_nonneg. It uses the real index default0, and does not assert an infinity-valued index bound at R=0.
It is not claimed to be le_csSup without membership and does not alter the
NO-has-it verdict for the original member law; it can remain a separate local convenience.
No unresolved verification or user design question remains for this duplicate law; independent
arithmetic design questions are preserved.

## Phase 8 — Completion and portable evidence

Five native sets: original/type/ordered293 audit; project old/image2 forms; isolated generic forms;
full two caller replays plus false-generalization guard; actual zero_index/allow_zero weakening. Every accepted receipt is clean and
complete, with disk partial=false or documented raw diagnostics format. No rejected native attempt,
new axiom, sorry, unsafe, native_decide or raised limit. Generic laws have no axioms; project results
use only standard propext, Classical.choice, Quot.sound. Exact executed sources and raw receipts
are preserved; current copy manifest governs current hashes, not historical worker manifests.

[Zero weakening source](../evidence/Roth.index_le_Θ/index-le-theta187-zero-executed.lean.txt);
[zero weakening receipt](../evidence/Roth.index_le_Θ/index-le-theta187-zero-receipt.json).

[Verification](../evidence/Roth.index_le_Θ/verification.json); [assessment](../evidence/Roth.index_le_Θ/assessment.json);
[portable validator](../evidence/Roth.index_le_Θ/validate.py); [current manifest](../evidence/Roth.index_le_Θ/copy-manifest.json).
