# Phase 4 — Roth.index

Scope: `Roth/Index.lean`, original lines 50–51, baseline `e557886`, branch
`ramin-cleanup`. Only this declaration and this report are owned by this worker.
Result: **retain unchanged**. Before 2 code lines; after 2; saved 0. No helpers,
renames, import changes, comments removed, signature edits, or definition edits.

## Step 1 — References

Read lean4/SKILL.md and mathlib-quality/SKILL.md; the Phase-4 worker contract in
`/Users/ramin/.local/share/roth-mathlib-quality/commands/cleanup.md`; and the full
golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md,
cleanup-gates.md. Consulted relevant style-rules.md and naming-conventions.md;
also buzz.md and profiling.md for the performance pass. No delegation by this worker.

## Step 2 — Audit (all 24 items)

| # | Item | Finding/action |
|---|---|---|
| 1 | LINT | Complete native LSP: success=true, partial=false, timed_out=false, failed_dependencies=[]. No warnings in target lines 47–51. Whole file has 27 pre-existing warnings (header, other public DecidableEq binders, index_le_card.hr), outside this worker's ownership. |
| 2 | HAVE SCAN | n/a: zero `have` expressions in this term definition. |
| 3 | SET_OPTION | n/a: target has no scoped or global option override. |
| 4 | SIMP SQUEEZE | n/a: target has no simp call. |
| 5 | NAMING | PASS: `index` names the mathematical index, is lowerCamelCase for real data, is not a single-letter identifier, and matches none of the forbidden abbreviations or numbering patterns. No rename needed. |
| 6 | LINE PACKING | PASS: one signature line, 77 codepoints, entire conclusion and `:=` on that line; required table below. |
| 7 | BY PLACEMENT | n/a: pure term mode, no `by`. |
| 8 | FORMAT | PASS: definition flush left; two-space body indentation; no empty internal line, tactic chains, haveI, or letI. |
| 9 | COMMENTS | Existing three-line docstring preserved byte-for-byte; no inline proof comments. |
| 10 | DOCSTRING | Public def has mathematical description and source attribution; preserve under lean4 Rule A and explicit owner constraint. |
| 11 | VISIBILITY | Public mathematical API: used throughout Index and by Main, MainLemma, Theta, and Separation. Keep public. Classic dialect. |
| 12 | STRUCTURE | One term body line, no conjunction, case branch, or large proof. No extraction needed. |
| 13 | MATHLIB | All five actual methods tried; weightedOrder is a partial conceptual match with different codomain/weights/zero convention. Search block below. |
| 14 | JUNK DEF | Keep: names a nontrivial mathematical object, substantial API in this file, and multiple external users; not a single-use wrapper. |
| 15 | EXISTS LEMMA | n/a: a real-valued definition, not a private existential lemma. |
| 16 | SHOW vs CHANGE | n/a: no show/change. |
| 17 | PUSH_NEG | n/a: no push_neg. |
| 18 | GENERALISE | All elaborated binders mechanically drop-tested in isolated snippets; table below. No live public API change. Optional semiring proposal compiled separately. |
| 19 | INEQUALITY | PASS: no inequalities anywhere in target Lean code; required table below. |
| 20 | NORMAL-FORM | Already direct `sInf` of the image of the Taylor support. Substituting weightedOrder requires natural rescaling, nonzero/positive-weight conditions, and toNat, handled by existing index_eq_weightedOrder_div. No unconditional canonical replacement established. |
| 21 | SYNTAX-GEN | Existing `index P α r` is the useful applied form. Changing to a power-series weightedOrder expression makes callers construct conversions and rescalings. Keep. |
| 22 | IMPORT-FANOUT | n/a: no new import. |
| 23 | CASTS | Diff casts: 0 dropped / 0 kept cross-type / 0 kept load-bearing, because source diff is empty. Existing Finset-to-Set annotation was experimentally removable; retaining it avoids protected definition churn. |
| 24 | INSTANCE-NAME | n/a: target is not an instance; introduces none. |

Issues requiring source repair: 0. Optional generalization: one, reported for owner
review only. No mathematical or trust-basis changes.

## Step 2.5 — Mathlib search status

Actual native calls (bounded results) and source searches:

| Method | Query | Observed result |
|---|---|---|
| A Lean-Finder | `index of multivariate polynomial at a point minimum weighted degree of nonzero Taylor coefficients` (3 results) | MonomialOrder.degree; MvPolynomial.weightedTotalDegree; MvPowerSeries.weightedOrder. |
| B Loogle | `MvPowerSeries.weightedOrder` (3 results) | weightedOrder, weightedOrder_zero, weightedOrder_one, including types. |
| C LeanSearch | `The index of a multivariate polynomial at a point is the infimum of weighted degrees of nonzero Taylor coefficients` (3 results) | MvPowerSeries.order, weightedOrder, le_weightedOrder. |
| D source rg | `MvPolynomial\.index\|def index.*MvPolynomial\|def.*weightedOrder` in mathlib MvPolynomial and MvPowerSeries.Order; also inspected Order lines 130–175 and WeightedHomogeneous | Finds weightedOrder and order; weightedOrder has natural weights, ℕ∞ codomain and zero value ⊤. weightedTotalDegree is a supremum, not the required infimum. |
| E local name search | `weightedOrder`, `weightedOrder_of`, `weightedOrder_eq_top_iff` | Positive source-backed hits for weightedOrder, _le, _mul, _zero, _prod, _eq_nat, _monomial_of_ne_zero, _add_of_weightedOrder_ne, _eq_top_iff. Symbol-index status initially error, then warming; these are positive hits, and empty results would not prove absence. |

Auxiliary variants examined: `_zero`, `_eq_top_iff`, `_le`, `_of`, `_left`,
`_right`; source search also inspected multiplication and weighted total degree.
Common-equivalents lookup: no matching discrete/finite/separation/bounded bucket.
Conclusion: **partial match** `MvPowerSeries.weightedOrder`; keep domain-specific
index, which already uses mathlib `sInf`, Taylor, and support directly. The existing
`index_eq_weightedOrder_div` supplies the relation under its required hypotheses.
No assertion of exhaustive mathematical absence, and no new declaration is being
introduced. Therefore an absence claim/probe is not used as justification.

## Step 2.6 — Generalisation status

The elaborated API is:

```lean
@Roth.index.{u} : {σ : Type u} → [Fintype σ] →
  MvPolynomial σ ℝ → (σ → ℝ) → (σ → ℕ) → ℝ
```

`DecidableEq σ` in the surrounding section is **already omitted** by elaboration.
It is included below to account for all lexical context as well as actual binders.
Tests used native lean_run_code isolated snippets, avoiding unauthorized mutations
of the protected public definition. Expected failing drop snippets returned
success=false, timed_out=false and the stated errors; successful snippets returned
success=true, timed_out=false. They did not introduce source sorries.

| # | Binder | Class/use | Actual mechanical tests | Verified result |
|---|---|---|---|---|
| 1 | `{σ : Type*}` | type-variable: variable and exponent index | Remove σ, autoImplicit=false | Fails: unknown σ at snippet lines 6–7. Universe already arbitrary; no universe widening needed. |
| 2 | `[Fintype σ]` | typeclass: Roth.weight's sum | Remove; then replace with `[Finite σ]` | Both fail: cannot synthesize Fintype σ (drop snippet L11; Finite snippet L6). No weaker parent directly supplies required computational enumeration. |
| 3 | `[DecidableEq σ]` lexical only | decidability, not elaborated API | Reconstruct body without it; compare full functions | Compiles and rfl equality to Roth.index succeeds. Already absent, no source change needed. |
| 4 | `(P : MvPolynomial σ ℝ)` | structure value: Taylor polynomial and support | Remove P, autoImplicit=false | Fails: unknown P at snippet L15. No proposition, strictness, pointwise, or class-parent weakening applies to a data value. Coefficient generalization below. |
| 5 | `(α : σ → ℝ)` | structure value: Taylor translation point | Remove α, autoImplicit=false | Fails: unknown α at snippet L18. No global property hypothesis to localize; follows coefficient domain in proposal below. |
| 6 | `(r : σ → ℕ)` | structure value: denominators in weight | Remove r, autoImplicit=false | Fails: unknown r at snippet L21. No positivity/nonzero hypothesis exists to weaken. Replacing denominator domain would also change Roth.weight and is outside the target. |

No binder has an untested applicable proposition or typeclass parent weakening.
Inversion check: n/a — this is a defining term, not a proof that unfolds a concrete
witness then reasons abstractly. The term uses P, α and r directly.

### Public literature search

WebSearch query: `Roth theorem index polynomial weighted index multiplicity generalization`.
Top three returned hits: (1) Min Ru, Roth's Theorem, university-hosted notes;
(2) Bombieri–Gubler, Heights in Diophantine Geometry, a Scribd copy;
(3) Baker–Wüstholz, Logarithmic Forms and Diophantine Geometry, a third-party PDF.
Only inspected primary/university sources are used for conclusions here.

* [Min Ru's notes](https://www.math.uh.edu/~minru/fields/roth.pdf), p. 3,
  explicitly define the minimum of normalized derivative multi-indices for complex
  points and positive integer weights. Thus real coefficient/point data are not
  an intrinsic limitation of the mathematical idea.
* [Milojević's exposition](https://aleksa-milojevic.github.io/expository/roth.pdf)
  was also successfully opened as a supplementary source.
* [AMS preview](https://www.ams.org/bookstore/pspdf/mbk-48-prev.pdf) appeared in
  search with the single-variable multiplicity interpretation; opening failed
  with Internal Error, so no stronger conclusion is based on it.
* ChatGPT math MCP: n/a, no callable math consultation tool exposed in this session.

### Optional big-change proposal — not applied

The following concrete scratch proposal compiled, including the specialization
equality. Sent to the owner before any possible application:

```lean
import Roth.Index
namespace IndexGeneralizationProposal
open MvPolynomial
variable {σ R : Type*} [Fintype σ] [CommSemiring R]
noncomputable def generalIndex (P : MvPolynomial σ R) (α : σ → R) (r : σ → ℕ) : ℝ :=
  sInf (Roth.weight r '' ((taylor α P).support : Set (σ →₀ ℕ)))
example (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) :
    generalIndex P α r = Roth.index P α r := rfl
end IndexGeneralizationProposal
```

Potential future `/generalise`: broaden polynomial coefficients and translation
point to a commutative semiring while keeping real-valued weights. This changes
public type parameters and needs review of the surrounding API. It is not required
for cleanup; **retain present public API**. No live generalization kept.

## Step 2.7 — Line packing

`#check @Roth.index` verified above; definition pretty-print reference formally n/a.
Widths measured by Python `len` on Unicode source strings, not bytes.

| Signature line | Chars | Next signature token | Arithmetic | Action |
|---|---:|---|---|---|
| 50 | 77 | none: body begins next line after `:=` | n/a — no further signature line | ok |

All three explicit arguments, the real conclusion, and `:=` share that line.
The single expression body L51 has 58 codepoints; it is not a signature line.
Appending the full body to L50 would be 77 + 1 + 56 = 134 > 100.

## Step 2.8 — Inequality scan

| # | Location | Original | Rewrite | Rename? |
|---|---|---|---|---|
| — | L50 signature and all binders | n/a — no ≥/> in signature | none | none |

Body also has no inequality; the arrow `→` is a Unicode type constructor, not `>`.

## Step 3 — All 42 golfing slots

| Rule | Status |
|---|---|
| 1.1 by exact wrapper | n/a: direct term, no by exact. |
| 1.2 by rfl | n/a: no proof wrapper. |
| 1.3 rw + exact | n/a: no tactics. |
| 1.4 simp + exact | n/a: no simplifier or closing exact. |
| 1.5 simp; rfl | n/a: no simp or rfl in source. |
| 1.6 anonymous constructor | n/a: result is real data, no constructor proof. |
| 1.7 apply + exact | n/a: no apply. |
| 1.8 by_contra! | n/a: no contradiction argument. |
| 1.9 eta reduction | n/a: no source lambda. |
| 1.10 inline have | n/a: no have. |
| 1.11 apply/intro | n/a: no apply or intro. |
| 1.12 redundant show | n/a: no show. |
| 1.13 have projections | n/a: no have or projections of hypotheses. |
| 1.14 merge rw | n/a: no rw. |
| 1.15 terminal simp only | n/a: no simp. |
| 1.16 nonterminal simp | n/a: no simp. |
| 1.17 dot notation | Already uses `.support`; sInf and weight have no useful receiver replacement. |
| 1.18 use <\| | Not applied: sInf's parentheses delimit an image expression; <\| substitutes punctuation without improving structure or width. Minimum-value filter and protected definition favor retention. |
| 1.19 push_neg | n/a: none present. |
| 1.20 existential helper | n/a: no existential declaration. |
| 2.1 grind whole proof | n/a: defining real data directly, no proposition proof or multiline tactic block; automation would replace the specified value. |
| 2.2 delete pre-grind tactics | n/a: no grind/tactics. |
| 2.3 simpa consolidation | n/a: no simplifier chain. |
| 2.4 fun_prop | n/a: no function-property proposition. |
| 2.5 positivity | n/a: result is a real value, not a positivity goal. |
| 2.6 gcongr | n/a: no comparison goal or calc. |
| 2.7 lia/omega | n/a: no Nat/Int proposition. |
| 2.8 aesop | n/a: no logical proof or membership goal. |
| 2.9 norm_num/norm_cast | n/a: no concrete arithmetic proposition. |
| 2.10 decide/+kernel | n/a: arbitrary real data, not a decidable proposition. |
| 2.11 field_simp/ring | n/a: no identity proof. |
| 2.12 linear_combination | n/a: no ring-ending proof with hypotheses. |
| 2.13 wlog | n/a: no symmetric cases. |
| 2.14 collapse calc | n/a: no calc. |
| 2.15 close goals with <;> | n/a: no proof subgoals. |
| 3.1 erw/rw | n/a: neither occurs. |
| 3.2 continuity/measurability | n/a: neither occurs. |
| 3.3 omega/lia | n/a: no omega. |
| 3.4 rcases rfl | n/a: no rcases. |
| 3.5 automation attributes | n/a: data def, not a new theorem; its established API provides the relevant facts. |
| 3.6 simp_all | n/a: no simp_all. |
| 3.7 remove limits | n/a: no limit override. |

## Step 4 — Reflection

The mathematics is to translate P by α, take its finite set of nonzero exponents,
map each exponent to its normalized weight, and take the real infimum. This is
already a single mathematical expression in term mode. Tactic-mode data synthesis
would obscure the defining value and not shorten it. No redundant have, show,
rewrite, branch, coercion round-trip, or missing-API signal is present. Existing
support API and order API already do the work. `exact?`/`apply?` are n/a to finding
a unique real defining value: their type alone cannot characterize this index.
An isolated inferred-Set version compiled and was rfl-equal, but that cosmetic
change is intentionally not made to a protected definition.

## Step 5a — Actual checks

* `lake build Roth.Index`: exit 0, `Build completed successfully (1501 jobs)`;
  existing warnings replayed, none target-specific. No full-project build run.
* Native full-file lean_diagnostic_messages: success=true, partial=false,
  timed_out=false, failed_dependencies=[], 27 pre-existing warnings.
* Native target-range check L47–51: success=true, partial=false,
  timed_out=false, items=[], failed_dependencies=[].
* Independent original value check: reconstructed e557886 body as
  `IndexAcceptedTests.originalIndex` in an isolated namespace; compiled
  `example : @Roth.index σ = @originalIndex σ := rfl` and pointwise equality
  to the raw sInf expression. This is not self-comparison.
* Independent type check: noncomputable snippet assigns `@Roth.index σ _` to
  `MvPolynomial σ ℝ → (σ → ℝ) → (σ → ℕ) → ℝ`; success=true.
* Actual `#print axioms Roth.index`: exactly
  `[propext, Classical.choice, Quot.sound]`. No new axioms or sorry introduced.
* Initial type-check scratch lacked `noncomputable` on a data-valued example;
  it failed with the expected compiler error. Repeated with `noncomputable
  section`, all examples passed. Expected failing binder tests were isolated.

## Step 5b — Gates

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | PASS | Actual `lake build Roth.Index`, exit 0. |
| definition_protected | PASS | Source diff empty; target identical to e557886. |
| theorem_statement_protected | PASS | No theorem edits. |
| structure_gate | PASS | One term body line; no conjunction or branch. |
| naming_gate | PASS | Mathematical lowerCamelCase `index`, zero forbidden patterns. |
| line_packing_gate | PASS | Complete one-row signature table; 77 codepoints. |
| inequality_orientation_gate | PASS | Required zero-occurrence table, no reversed inequalities. |
| docstring preservation | PASS | Existing docstring unchanged. |
| standard axioms | PASS | Actual target axiom print, three permitted axioms only. |
| cumulative_no_unintended_external_breakage | PASS for worker diff | Empty source diff; owner runs cumulative full-project gates. |

Overall: **PASS**, optional public generalization unimplemented pending separate
review, not a gate deferral. Helpers: none. Renames queued: none.

## Buzz status (1000 ms budget)

Native lean_profile_proof at line 50 returned `No theorem/lemma/def at line 50`
(parser did not recognize this noncomputable def). Fallback actual command:

```text
lake env lean -Dprofiler=true -Dprofiler.threshold=0 Roth/Index.lean
```

Exit 0; log `/private/tmp/roth-index-index-profile.log`. In the first definition's
block (immediately after section-variable elaboration and before first private
lemma), elaboration is 6.51 ms; process pre-definitions 1.03 ms, type checking
1.7 ms. FAST, no fix or limit raise. Equivalent isolated term profiler confirms
small inference/pre-definition costs (pre-definitions 3.36 ms, kernel 2.44 ms).
No profiling scaffolding touched live source. Two scratch profiling attempts used
the documentation's `count_heartbeats in` spelling; Lean requires the leading `#`,
so those were syntax failures. Final successful measurement omitted that wrapper;
no heartbeat speedup is claimed and no performance fix was made.

## Step 6 — Result and checklist

Before: 2 lines. After: 2. Saved: 0. Source issues: 0. Fixed: 0.
Rules applied: no source transformation justified. Comments preserved: all 3
existing docstring lines; no proof comments existed. Refactoring needed: no
mandatory work; optional future coefficient-semiring generalization above.

- [x] Step 1 — mandatory references read.
- [x] Step 2 — all 24 audit items answered.
- [x] Step 2.5 — actual five-method search and limitations recorded.
- [x] Step 2.6 — every binder, mechanical tests, public literature, optional proposal.
- [x] Step 2.7 — every signature line measured.
- [x] Step 2.8 — inequality occurrence table.
- [x] Step 3 — all 42 rule slots.
- [x] Step 4 — alternative/whole-term reflection.
- [x] Step 5a — complete native LSP, module build, independent value/type, axioms.
- [x] Step 5b — all diff and content gates.
- [x] Step 6a — no rename needed, no sidecar queue mutation.

Freeze: no more source edits by this worker. Source SHA256 at release:
`001fece6d8853df7923088ed8fbe68bb37545c1d24d8365139148c1e3414dd42`.
Target two-line code SHA256 (excluding trailing newline):
`453e3e250016fa121c036ac73caae41b7f7262fa758bed228e9ef600b7c5e60a`.
All compiler processes launched by this worker finished (build session 70711 and
profile session 6189 both exit 0); native snippet calls completed.
