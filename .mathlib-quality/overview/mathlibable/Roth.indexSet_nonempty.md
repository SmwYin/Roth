# Roth.indexSet_nonempty — NO-mathlib-has-it

Canonical185, `Roth/Theta.lean:80`. This is a read-only assessment; production and pins are unchanged. The theorem is useful to its two supremum callers, but its general law already exists as `Set.Nonempty.image2`. Re-aiming the accepted parent `indexSet` at `Set.image2` makes that correspondence explicit. The coefficient-family witness remains project mathematics and is not counted as an existing mathlib call.

## Phase 0 — Baseline and native declaration

The shared successful baseline completed2467 jobs. All17 source/pin hashes were freshly recomputed and match it: [baseline](../evidence/Roth.indexSet_nonempty/baseline-build.txt), [fresh hashes](../evidence/Roth.indexSet_nonempty/source-hashes.json), [input manifest](../evidence/Roth.indexSet_nonempty/input-manifest.json). The complete985-line declaring module and both actual callers in that module were read; it develops the index supremum and Lemmas5–7 of the source. No sorry occurs in the declaration. [Complete source](../evidence/Roth.indexSet_nonempty/source-Theta.lean.txt).

Full elaborated native type:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] {B : ℝ},
  1 ≤ B → ∀ (q r : σ → ℕ), (Roth.indexSet B q r).Nonempty
```

The native kernel body constructs the index of polynomial1 at numerators constantly1, then supplies `one_mem_RSet hB r` and coordinatewise `isCoprime_one_left`. It does not compute that index. Standard axioms are `propext`, `Classical.choice`, `Quot.sound`. [Native original receipt](../evidence/Roth.indexSet_nonempty/nonempty185-original-receipt.json), [exact executed source](../evidence/Roth.indexSet_nonempty/nonempty185-original-executed.lean.txt).

## Phase 1 — Mathematical content

For a real coefficient bound B≥1, any finite family of natural denominators q and natural weights r admits an index in the family defining Θ. The constant integer polynomial1 has degree0 in every variable, has coefficients bounded by B, and is nonzero. Numerator1 is coprime to every denominator, including0, so evaluating its index yields a member of the family. No positivity of q or r is needed.

σ is the variable type; `[Fintype σ]` supports the existing weighted-index parent interface; B bounds every integer coefficient; q specifies denominators and r degree bounds/weights. The only propositional hypothesis is1≤B. `DecidableEq σ` is already omitted. Project dependencies are `Roth.indexSet`, `Roth.RSet`, `Roth.index`, and `Roth.one_mem_RSet` (direct constants versus unfolded context distinguished in native evidence).

## Phase 2 — Preliminary checks

SMALL: this is an existence helper, neither a named theorem nor a main result nor a new structure. The one-line-definition test is n/a because this is a theorem; its one substantive witness-construction line is not a definition-exemption argument. Exhaustive literature search still runs.

## Phase 3 — Exhaustive literature

Exact requests, returned-response SHA256/bytes/status, URLs and concise summaries are archived; full returned bodies are not persisted. Search results establish locators, not theorem absence. [General queries](../evidence/Roth.indexSet_nonempty/web-0.json), [nLab/nCatLab](../evidence/Roth.indexSet_nonempty/web-1.json), [Stacks/MO](../evidence/Roth.indexSet_nonempty/web-2.json), [recent arXiv](../evidence/Roth.indexSet_nonempty/web-3.json), [primary opens/access failures](../evidence/Roth.indexSet_nonempty/web-primary.json).

| Channel | Actual query / locator | Finding |
|---|---|---|
| General web, specific | Roth theorem index polynomial bounded coefficients constant polynomial supremum nonempty | Roth-index exposition; no separate standard name for this wrapper |
| General web, general | image of Cartesian product nonempty sets binary function | Elementary binary-image/nonempty-product law; Metamath xpnz locator |
| General web, alias | direct image nonempty set elementary set theory | Princeton chapter p25 direct-image definition |
| ChatGPT math MCP | n/a | `ask_chatgpt_math` unavailable; other channels completed |
| Local clean.tex | §5 lines643–701 | Direct source explicitly chooses polynomial1 and numerators1 before boundedness |
| nLab | `site:ncatlab.org/nlab image nonempty set` | Image, inhabited set and product pages; direct image page open failed400 unsupported XHTML |
| nCatLab | `site:ncatlab.org/ncatlab image nonempty set` | Actual distinct namespace query; results were principally /nlab, no exact /ncatlab hit |
| Stacks | `site:stacks.math.columbia.edu image nonempty sets` | General maps/sets/categories material; no specialized bounded-index theorem |
| MathOverflow | `site:mathoverflow.net Roth index polynomial supremum` | Roth quantitative/Diophantine context; no replacement beyond elementary image law |
| Recent arXiv | `site:arxiv.org Roth theorem polynomial index after:2021-10-27 before:2026-10-28` | Window explicitly searched; several unrelated nonlinear/progression or other polynomial hits, plus weighted-index material; no exact API found |

Primary sources: [Princeton set-theoretic preliminaries](https://assets.press.princeton.edu/chapters/s8274.pdf), p25, defines direct images; [Min Ru's Roth notes](https://www.math.uh.edu/~minru/fields/roth.pdf), pp2–4, supplies the weighted-index and coefficient-height setting. Neither is claimed to state this exact project helper. Metamath xpnz direct open failed cache miss, so only the returned search theorem snippet is used. The [local excerpt](../evidence/Roth.indexSet_nonempty/clean-section5-excerpt.tex.txt) is the exact project-specific anchor; [local search/hash](../evidence/Roth.indexSet_nonempty/local-literature.json).

Synthesis: the project form is a bounded-polynomial binary-image existence witness. The most general elementary law says that a binary image of two nonempty sets under any total function is nonempty, with no algebra/order/topology/finiteness assumptions. No source conflict was found. Numerical bounds belong to the supplied polynomial witness, not to the abstract image law.

## Phase 4a — Every parameter and constraint

| Parameter/constraint | Role in current statement | Generality result |
|---|---|---|
| `σ : Type u` | Polynomial variables | Universe polymorphic already; arbitrary types in abstract law |
| `[Fintype σ]` | `indexSet` invokes existing finite-variable `index` | Retain for this unchanged parent spelling; abstract binary-image law has no Fintype. Removing the parent is a representation change, not a claimed local weakening |
| `DecidableEq σ` | None in native type | Already omitted; replacement has none |
| `B : ℝ` | Uniform coefficient bound after integer cast | Bound cannot simply be removed; checked family/nonempty equivalence gives exact threshold1 |
| `hB : 1 ≤ B` | Ensures polynomial1 is admissible | Sharp for existence of any admissible nonzero integer polynomial, not merely for this witness; proved from a nonzero integer coefficient |
| `q : σ → ℕ` | Rational denominators, coprimality predicate | Arbitrary q already, zero permitted; no positive/nonzero restriction added |
| `r : σ → ℕ` | Degree bound and index weight | Arbitrary r already, zero permitted; constant1 works |
| Integer coefficient ring | Nonzero coefficients have absolute value≥1 | Expanded generic source family can be arbitrary, but changing this concrete ring changes the height-threshold mathematics |
| Real output/order | Existing index takes values in ℝ | Abstract law works for arbitrary output type and does not inspect order |
| Nonzero, degree, coefficient predicates | Complete `RSet` family | All retained in expanded witness and necessity proof; none silently discarded |
| Coordinatewise coprimality | Complete numerator family | All coordinates retained; explicit numerator1 works for every q |

## Phase 4b — Verified restatement

The unchanged project interface is already as weak as its parents support. Its abstract mathematical core is strictly narrower than the existing polymorphic law, and that widening was mechanically checked:

```lean
{α β γ : Type*} → (f : α → β → γ) →
  {s : Set α} → {t : Set β} →
  s.Nonempty → t.Nonempty → (Set.image2 f s t).Nonempty
```

This is existing `Set.Nonempty.image2`, not a proposed new helper. Isolated mathlib-only native checks additionally verify the full iff `image2_nonempty_iff`; project-context checks verify the exact representation bridge, expanded complete polynomial witness, both caller proofs, `RSet.Nonempty ↔1≤B`, `indexSet.Nonempty ↔1≤B`, and zero-bound emptiness. [Exact project execution](../evidence/Roth.indexSet_nonempty/nonempty185-project-executed.lean.txt), [project native receipt](../evidence/Roth.indexSet_nonempty/nonempty185-project-receipt.json), [isolated execution](../evidence/Roth.indexSet_nonempty/nonempty185-isolated-executed.lean.txt), [isolated receipt](../evidence/Roth.indexSet_nonempty/nonempty185-isolated-receipt.json). Cost CHEAP is descriptive only and does not determine the verdict.

## Phase 4c — All nine modern-idiom rows

| # | Question | Answer and concrete consequence |
|---|---|---|
|1| Explicit structures to typeclasses? | No; no ad-hoc algebraic structure hypotheses; no new instance needed |
|2| Sequences/metrics to filters? | No; pure existence, no limit |
|3| Construction to universal-property class? | No; set image already represents evaluation, no universal-property class needed |
|4| Closure predicate to bundled substructure? | No; nonzero bounded polynomial family need not be an additive/multiplicative substructure |
|5| Field/vector assumptions to weaker hierarchy? | Yes at expanded law: arbitrary sets/function, no scalar structure; unchanged index parent still needs its existing instances |
|6| Higher category? | No; elementary set-theoretic existence; categorification adds no useful API here |
|7| Concrete ℤ/ℝ/ℕ indices to abstract structures? | Yes in abstract image2 law: input/output types arbitrary; do not claim the original integer-height threshold survives arbitrary coefficient rings |
|8| Concrete-via-abstract diagnostic? | Yes: original proof-body has zero occurrences of `indexSet`/`index`, one `one_mem_RSet` call. Once two family witnesses are supplied it only packages a binary-image witness. Existing `Set.Nonempty.image2` removes redundant packaging and gives general nonempty-image API |
|9| False-generalization guard? | Pass for image2 restatement: same two source families and same evaluation map preserved. Reject dropping nonzero/degree/coefficient/coprimality predicates or hB without evidence. Checked B0 emptiness explicitly refutes unrestricted B |

Modern idiom is already supplied by mathlib. Downstream gains are `Set.image2_nonempty_iff`, source nonempty projections, and `Set.image2_subset_iff`; this target adds no missing contemporary formulation.

## Phase 4.5 — Infrastructure risk

n/a — theorem kind. Typeclass diamonds, reducibility leaks, noncanonical unfolding, instance priorities, universe-instance issues, and coercion ambiguity are all definition/instance risk rows and no new such infrastructure is introduced by a proposition proof.

## Phase 4.6 — All five proof-strategy rows

| # | Question | Result |
|---|---|---|
|1| ε–δ versus filters | No topology |
|2| Elementwise versus ideals/submodules | No closure property; use existing image2 operation instead of repackaging nested existentials |
|3| Sequences versus nets | No limiting process |
|4| Explicit object versus universal property | No categorical construction |
|5| Missing helper mathlib should have | No missing nonempty binary-image law: it exists. Unit admissibility concerns the separately assessed complete bounded-family API, not an absent image law |

REFACTOR-RECOMMENDED, CHEAP: after the independently accepted parent re-aim, use `Set.Nonempty.image2` with complete family witnesses; no upstream theorem addition. The original witness proof is mathematically direct. The expanded coefficient-family normalization is real local proof work and is not falsely counted as one existing mathlib call.

## Phase 5 — All five methods on all three forms

[All12 raw external/formal responses](../evidence/Roth.indexSet_nonempty/formal-search.json); each fulfilled, no tool error. Local symbol index was unavailable (source-name hits still returned); no empty local result is evidence of absence. External indexes may differ from this pin; native positive checks settle candidate validity here.

| Method | Current concrete form | Literature-standard binary image | Abstract nonempty image |
|---|---|---|---|
| Lean-Finder | Polynomial bounded-index query; unrelated polynomial existence hits | Exact `Set.Nonempty.image2`, `Set.image2_nonempty_iff` | Same exact hits |
| Loogle | `Set.Nonempty, MvPolynomial`; empty | `Set.image2, Set.Nonempty`; exact law/iff | `Set.Nonempty, Set.image`; unary image and equivalence candidates |
| LeanSearch | Concrete index-family query; support/Nullstellensatz near misses | Exact binary image law/iff | Exact binary image law/iff |
| rg source | `indexSet_nonempty\|RSet.*Nonempty\|index.*[Nn]onempty` | `image2_nonempty_iff\|Nonempty.image2\|image_nonempty` | `theorem Nonempty.image2\|theorem image2_nonempty_iff\|theorem Nonempty.prod\|def image2` |
| local names | `indexSet_nonempty`; project target | `image2_nonempty`; exact mathlib iff | `Nonempty.image2`; exact mathlib law |

The three complete rg receipts are [current](../evidence/Roth.indexSet_nonempty/rg-current.json), [standard](../evidence/Roth.indexSet_nonempty/rg-standard.json), [abstract](../evidence/Roth.indexSet_nonempty/rg-abstract.json). All15 method×form cells actually ran. Pinned positive declarations: `Set.Nonempty.image2` at `Mathlib/Data/Set/NAry.lean:114`, `Set.image2_nonempty_iff` at118; archived full source/hash in [mathlib inputs](../evidence/Roth.indexSet_nonempty/mathlib-inputs.json). No global absence claim is made.

## Phase 5.5 — Three statement-shape checks

Normal form: use `(Set.image2 f S T).Nonempty`; alternatives are nested existential witnesses and nonemptiness of the unary image of the product/subtype. `Set.image2_nonempty_iff` canonically simplifies to `S.Nonempty ∧ T.Nonempty` on the RHS. Current standalone nonempty proposition is convenient for `csSup_le`; the helper is not an ill-oriented iff.

Syntactic generality: checked both implication `hs.image2 ht` and full nonempty iff, then both actual supremum-call replacements. Requiring arbitrary source-family nonemptiness is mathematically more general than choosing1 internally; for these callers the admissible witness is available from hB. A direct image2 application still exhausted default200k heartbeats despite explicit f; the accepted current-form proof rewrites by the bridge and `Set.image2_nonempty_iff` first, then supplies the pair. No limits were raised. Alternative set builder spelling requires a representation bridge before applying the generic API.

Superfluous arguments: no local unused explicit argument. B/hB,q,r occur in family/interface; hB is necessary by actual iff. Fintype is fixed by the current index parent; DecidableEq already absent. No positive q/r hypotheses are needed. Overall RESTATE-BEFORE-SHIP via the already accepted parent re-aim, then reuse the existing law; no new theorem to ship.

## Phase 6.0 — Actual callers and inline audit

| Caller | Actual source usage | Refactor |
|---|---|---|
| `Roth.Θ_le_of_forall_index_le`, Theta:127 | `csSup_le (indexSet_nonempty hB q r)` | Rewrite by the checked bridge and `Set.image2_nonempty_iff`, then supply the paired `RSet` witness1 and coprime-numerator witness1 |
| `Roth.Θ_mono`, Theta:136 | `csSup_le_csSup (indexSet_bddAbove B' q) (indexSet_nonempty hB q r)` | Replace only the nonempty premise by the same verified iff rewrite and paired witnesses; bound/subset proof unchanged |

There are2 explicit body calls in one file,0 external-to-file explicit calls,0 type references. Fresh lexical and tracked Git enumerations agree: [lexical](../evidence/Roth.indexSet_nonempty/callers.json), [Git](../evidence/Roth.indexSet_nonempty/git-callers.json), [structured source excerpts](../evidence/Roth.indexSet_nonempty/callers-structured.json). The ordered293 canonical kernel audit finds exactly the same2 direct value consumers, no type consumers; that equality is an independently checked outcome, not a definition of source callers. No transitive/simp dependency-closure claim is made.

[Inline audit](../evidence/Roth.indexSet_nonempty/inline-audit.json) searched all production files without ignore-rule omissions for unit-membership/coprimality/index-nonempty and supremum patterns. No separate equivalent nonemptiness re-derivation was found. Other supremum inequalities in the module do not constitute re-proofs of this existence statement. No downstream external repository was searched or asserted absent.

## Phase 6 — Composition and parent re-aim

The exact generic law is a single existing mathlib call: `hs.image2 ht`, independently verified in mathlib-only context with the project target guarded unavailable. The original spelling requires the checked image2 representation bridge and two supplied witnesses. The bridge itself is definitionally true (`rfl` checked), although the old-form proof still needs an explicit rewrite to guide elaboration. The rejected direct image2 attempt is retained separately and is not accepted evidence. Its unit-membership premise calls `Roth.one_mem_RSet`; that project lemma is not a mathlib building block. The fully expanded witness uses coefficient/degree normalization and is recorded as local proof, not ≤3 existing calls.

Consequently the honest old-form call accounting does not establish a direct ≤3 existing-mathlib-call proof of every bounded-family premise. The parent re-aim gate nevertheless applies: accepted180 identified `indexSet` as this precise binary image, and mathlib already has the corresponding nonempty law. This independently verified analogous law yields NO-mathlib-has-it; normalization of the old spelling is not a reason to downgrade to BORDERLINE. It does not relitigate accepted184's bounded-family API judgment. Both actual caller compositions compile in the native project-context evidence. `simp [RSet,…]` is disclosed as trivial simp proof of the complete family witness, not used to derive a NO-composable verdict.

## Phase 7 — Actionable verdict

**NO-mathlib-has-it.** Existing declarations: `Set.Nonempty.image2` and `Set.image2_nonempty_iff`, `Mathlib/Data/Set/NAry.lean:114/118`. Literature identifies elementary image existence, parameter analysis preserves full families and validates the sharp integer coefficient threshold, all15 search cells ran, and native generic/current/caller probes establish the exact bridge. The theorem supplies no new mathematical content beyond the existing law after the parent re-aim. No cost-based downgrade or search-only absence claim enters this decision.

The actual checked old-form proof is:

```lean
rw [bridge, Set.image2_nonempty_iff]
exact ⟨⟨1, Roth.one_mem_RSet hB r⟩,
  ⟨fun _ ↦ 1, fun _ ↦ isCoprime_one_left⟩⟩
```

Here `bridge` is the checked exact equality from `indexSet` to the full image2 expression, proved by `rfl`. It is a project-representation proof, not an additional mathlib building block. This expanded snippet preserves honest accounting of the arithmetic premise.

One-line generic replacement is `Set.Nonempty.image2 hs ht` with f instantiated to the original index-evaluation map and hs/ht the complete admissible source sets. Refactor both listed callers using the verified old-form iff route above for their nonempty premise. The generic one-call term was checked in abstract isolated context; a fully typed source-set version of it at these current-form callers was not separately executed. Keep `one_mem_RSet` locally according to accepted184 until the generic bounded-family API design is settled. Delete this thin nonempty wrapper together with the parent representation refactor; avoid creating an upstream Roth-specific theorem. If retained for paper-navigation compatibility, its alternative home is project-local `Roth/Theta.lean`, where its two supremum consumers and source-specific notation live. All of this is a plan; production was not edited.

## Phase 8 — Verification and handoff

[Verification inventory](../evidence/Roth.indexSet_nonempty/verification.json), [assessment metadata](../evidence/Roth.indexSet_nonempty/assessment.json), [overview entry](../evidence/Roth.indexSet_nonempty/overview-entry.json), and [portable validator](../evidence/Roth.indexSet_nonempty/validate.py) record exact accepted executions and scope. Full source/pin hashes, mathlib candidate hashes, ordered canonical293 enumeration, actual native diagnostics/standard axioms, caller excerpts, all phases and current manifest bytes/hashes are checked. The initial direct image2 attempt, even with f explicit, failed at the default200k defeq heartbeat limit; rejected1 exact source/receipt are retained and excluded from accepted evidence. Rewriting by the image2 iff then supplying paired witnesses succeeded with unchanged limits. Root acceptance is pending independent review. No unresolved verification remains.
