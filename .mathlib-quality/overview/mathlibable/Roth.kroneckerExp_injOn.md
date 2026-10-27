# Roth.kroneckerExp_injOn — full mathlibable assessment

**Verdict: YES-but-generalise-first.** The reusable contribution is bounded-digit injectivity of geometric `Finsupp.weight`, with an explicit enumeration and no lower-base hypothesis. The project spelling should not be upstreamed. This conclusion independently re-aims the parent `kroneckerExp` at `Finsupp.weight`; the parent NO verdict does not imply that a corresponding weight injectivity theorem already exists.

## Phase 0 — baseline and identity

Canonical entry108 is `Roth.kroneckerExp_injOn`, public theorem, `Roth/GenWronskian.lean:69`; the conclusion begins at70. All17 current production/pin hashes freshly equal the shared baseline manifest. The successful2467-job baseline is reusable. Production and Git are unchanged. See [inputs](../evidence/Roth.kroneckerExp_injOn/inputs.json), [baseline](../evidence/Roth.kroneckerExp_injOn/baseline-build.txt), [canonical entry](../evidence/Roth.kroneckerExp_injOn/canonical-entry.json), and [full original native receipt](../evidence/Roth.kroneckerExp_injOn/kronecker-exp-injon-original-receipt.json).

## Phase 1 — statement and comprehension

Given a finite index set with its chosen enumeration and a natural base greater than1, form the sum of the coordinates multiplied by successive powers of the base. Two exponent vectors whose coordinates are smaller than the base have equal sums only when they agree. This is uniqueness of equal-length positional expansion, applied to monomial exponents.

Full elaborated type (universe spelling normalized):

```lean
∀ {σ : Type u} [Fintype σ] {k : ℕ},
  1 < k → Set.InjOn (Roth.kroneckerExp k) {d | ∀ j : σ, d j < k}
```

There is no `K`, `Field`, characteristic, or `l` argument despite the surrounding section. `σ` is the variable index, `[Fintype σ]` supplies enumeration, `k` the positional base, and the set predicate bounds every digit. The proof identifies the weighted sum with `Nat.ofDigits k (List.ofFn ...)`, uses `Nat.ofDigits_inj_of_len_eq`, and transports list equality through `List.ofFn_injective`, surjectivity of the enumeration inverse, and `DFunLike.coe_injective`. The entire declaring module and sole explicit caller were read; [archived source](../evidence/Roth.kroneckerExp_injOn/source-0.lean.txt) includes them.

## Phase 2 — preliminary checks

SMALL: an arithmetic helper for Kronecker substitution, rather than a new structure or main Wronskian result. “Kronecker” names the substitution, not an independently named main theorem. One-line definition test and its three exemption tests are n/a: theorem, not a definition. This does not reduce the literature protocol.

## Phase 3 — exhaustive literature

Exact requests, response SHA256/byte count/status, returned locators, and original short summaries are retained; article/search bodies are not persisted.

| Channel | Actual query or inspection | Finding |
|---|---|---|
| General web: specific | Kronecker substitution injective bounded degrees positional numeral representation uniqueness | Korwar thesis §2.3.2 explicitly identifies bounded exponents with base-d expansion. [receipt](../evidence/Roth.kroneckerExp_injOn/web-0.json) |
| General web: standard | unique positional representation natural numbers base b digits less than b proof | Equal length or a leading-zero convention is necessary for a unique digit list. [receipt](../evidence/Roth.kroneckerExp_injOn/web-1.json) |
| General web: aliases/general | mixed radix representation uniqueness Kronecker substitution polynomial encoding | Mixed-radix weights are a broader encoding; they require a changed weight system. [receipt](../evidence/Roth.kroneckerExp_injOn/web-2.json) |
| ChatGPT mathematics | unavailable `ask_chatgpt_math` | n/a; no second-opinion response invented. |
| Local references | clean.tex: FACT in proof of Lemma1 | Each exponent is strictly less than k; positional representation is unique. [search](../evidence/Roth.kroneckerExp_injOn/rg-local-literature.json), [excerpt](../evidence/Roth.kroneckerExp_injOn/local-literature.txt) |
| nLab | `site:ncatlab.org/nlab positional numeral system` | Numeral/decimal-representation pages provide terminology. Direct numeral-system URL failed; no inaccessible theorem attributed. |
| nCatLab | `site:ncatlab.org/ncatlab numeral representation` | No exact categorical law found; returned nLab background is not a nCatLab hit. Finite digit encoding supplies no higher-category target. |
| Stacks | `site:stacks.math.columbia.edu Noether normalization powers distinct monomials`, direct00OW | §10.115 Lemma1 separates finite multi-index sets by sufficiently dominant weights, a broader related result. |
| MathOverflow | `site:mathoverflow.net Kronecker substitution injective` | Mostly unrelated names; no exact bounded-digit theorem identified, not proof of absence. |
| Recent arXiv | initial dated2022–26 query; refined `site:arxiv.org "Kronecker substitution" after:2021-10-27 before:2026-10-28` | Wang–Su–Wang–Zhang2024 reversible iterative substitution; Shunia2024 applications. Relevant ongoing use, not a replacement for the arithmetic law. |

Named-channel exact requests are in [web3](../evidence/Roth.kroneckerExp_injOn/web-3.json), [web4](../evidence/Roth.kroneckerExp_injOn/web-4.json), and [direct/refined access](../evidence/Roth.kroneckerExp_injOn/web-direct.json).

Primary locators: [Korwar thesis](https://www.iitgoa.ac.in/~arpita/articles/PITAndLowerBoundsForSumABPs.pdf), §2.3.2; [Stacks00OW](https://stacks.math.columbia.edu/tag/00OW), Lemma10.115.1; [2024 iterative reduction paper](https://arxiv.org/abs/2403.12716); [2024 combinatorial application paper](https://arxiv.org/abs/2404.00332). The standard concept is uniqueness of bounded positional digit expansion, historically used in Kronecker substitution and Noether normalization. Polynomial coefficient rings play no role. Mixed radix and arbitrary dominant weights go beyond a mere change of enumeration; they are not silently substituted for the project statement.

## Phase 4a–b — all parameters and verified generality

| Parameter/hypothesis | Need in current interface | Generality conclusion |
|---|---|---|
| `σ : Type u` | arbitrary universe already | Preserve arbitrary universe; no concrete type restriction. |
| `[Fintype σ]` | needed by `kroneckerExp` and chosen `equivFin` | Expanded weight theorem needs only `e : σ ≃ Fin n`; a proof-local Fintype is derived from e. A public redundant class was rejected by native warning. |
| implicit natural `k` | natural positional base | Remains natural; arbitrary rings lose order, bounded digits, and uniqueness. |
| `hk : 1 < k` | used by existing `ofDigits` theorem | **Removable**: for k≤1, all admissible digits are0 (or the set is empty), so any two are equal coordinatewise. Native no-base proof succeeds. |
| `∀ j, d j < k` and analogous second vector | essential uniqueness condition | Preserve strict bound; allowing digit k causes carries, e.g. vectors (k,0) and (0,1) in two positions. |
| chosen enumeration | fixes actual function | Abstract to explicit e, not an arbitrary weight with unjustified injectivity. |
| finitely supported natural exponents | existing domain | Preserve and use `Finsupp.weight`; no coefficient-field weakening to claim because field absent already. |

STRICTLY NARROWER THAN STANDARD API: the field-free positional content is already recognized, but arbitrary explicit enumeration and removal of hk are verified improvements. The no-hk conclusion also compiles for the **fixed original parent interface**, rather than merely an expanded representation. [raw proof](../evidence/Roth.kroneckerExp_injOn/kronecker-exp-injon-raw-executed.lean.txt), [no-base proof](../evidence/Roth.kroneckerExp_injOn/kronecker-exp-injon-no-base-executed.lean.txt), and [bridge](../evidence/Roth.kroneckerExp_injOn/kronecker-exp-injon-bridge-executed.lean.txt) preserve exact executions and receipts in verification metadata. The explicit enumeration change is mechanical; removal of hk adds a short elementary case split, not new mathematical machinery. Cost: CHEAP. No production edit is proposed during this read-only assessment.

Proposed public form (name provisional):

```lean
theorem Finsupp.weight_pow_injOn {σ : Type*} {n : ℕ}
    (e : σ ≃ Fin n) (k : ℕ) :
    Set.InjOn (Finsupp.weight (fun j ↦ k ^ (e j : ℕ)))
      {d : σ →₀ ℕ | ∀ j, d j < k}
```

A further version for an injective position map into ℕ could cover infinite index types with finite support; supplemental Finder/LeanSearch/Loogle/local-name queries tested this boundary and found digit/weight partial matches only (the final local weight_inj query reports unavailable, unlike the earlier successful index queries); that would require a support-restriction proof not established here. The checked proposal makes no maximal-generality claim for that additional direction. Mixed radix similarly remains a separate possible API, not a claimed compiled weakening.

## Phase 4c — nine modern-idiom rows

| # | Question | Answer and concrete consequence |
|---|---|---|
|1| Typeclass preambles | No new class; an explicit finite enumeration is the data, and redundant Fintype can be derived locally. |
|2| Filters/topology | No: finite arithmetic, no topology. |
|3| Universal property | No constructed universal object; additive `Finsupp.weight` already expresses the sum. |
|4| Bundled substructure | No: bounded-digit vectors are not closed under addition, hence not a submodule. `Set.InjOn` is appropriate. |
|5| Field→module hierarchy | No field in actual type. Retain natural arithmetic and existing additive weight bundle. |
|6| Higher categories | No categorical structure used or needed. |
|7| Concrete index | Abstract σ already. Explicit e decouples the law from arbitrary `Fintype.equivFin`; natural positions encode actual base powers and cannot just become arbitrary monoids. |
|8| Concrete-via-abstract diagnostic | Yes. Proof body mentions `kroneckerExp` only in hsum's statement and its unfolding normalization list; after hsum, zero lines mention it. The rest is digit uniqueness plus injective transports. Checked weighted theorem reuses that proof with arbitrary e. |
|9| False-generalisation guard | Pass: geometric weights k^(e j) recover precisely the original exponent under e=equivFin. Arbitrary positive weights are rejected: equal weights collide on singletons. The no-hk branch preserves content, since admissible digits are forced0. |

Modern idiom available: yes, `Finsupp.weight` with explicit enumeration. This enables direct reuse for `NoetherNormalization.sum_r_mul_ne`'s weighted sums and future polynomial substitutions, and composes with existing `weight_eq_sum` without exporting the project’s `kroneckerExp`. It is an actual organisation improvement, not categorical relabelling. All stronger claims are distinguished from verified statements.

## Phase 4.5 — infrastructure

n/a: theorem. All six risks (typeclass diamond, reducibility leak, noncanonical unfolding, instance-priority collision, universe constraints, coercion ambiguity) are n/a as new infrastructure: neither original nor proposed theorem installs instances, coercions, or a new data definition. The unused Fintype/style warnings in rejected raw attempts are preserved and corrected, not accepted as clean runs.

## Phase 4.6 — proof strategy

| # | Strategy question | Finding |
|---|---|---|
|1| ε–δ versus filters | n/a finite arithmetic. |
|2| Elements versus substructures | Digits require coordinate comparison; bounded set not additive. Existing bundled weight is suitable; no submodule inclusion proof replaces it. |
|3| Sequences versus nets | n/a finite lists, not convergence sequences. |
|4| Explicit construction versus universal property | n/a uniqueness arithmetic, not a universal object. |
|5| Missing helper API | Yes: public geometric-weight bounded-digit injectivity bridges existing digit lists to finitely supported monomial exponents; near-identical conversion occurs privately in NoetherNormalization90–98. |

REFACTOR-RECOMMENDED: use a public weight law with arbitrary enumeration and no hk. The core proof strategy via `ofDigits` is mathematically idiomatic. A normalized `ofDigits (List.ofFn ...) = weight ...` bridge could be factored if another caller needs it; no invented helper counts as existing mathlib. Switching is CHEAP and produces a cleaner shared boundary.

## Phase 5 — five actual mathlib methods on three forms

[All exact formal requests and raw responses](../evidence/Roth.kroneckerExp_injOn/formal-search.json) record current Kronecker exponent, standard positional digits, and abstract geometric weight queries separately.

| Method | Current | Standard | Abstract |
|---|---|---|---|
| Lean-Finder | `Finset.geomSum_injective`, a finite-set digit0/1 restriction (`Combinatorics/Colex.lean:513`) | `Nat.ofDigits_inj_of_len_eq` | digits injectivity, not bounded Finsupp weight |
| Loogle | first query rejected unknown k; valid wildcard retry returns none | `Nat.ofDigits, Set.InjOn` finds `Nat.injOn_ofDigits` | `Finsupp.weight, Set.InjOn` returns none |
| LeanSearch | power-series injectivity etc., no exact target | `Nat.ofDigits_inj_of_len_eq` | unrelated weighted-sum lemmas; no target |
| rg whole pinned mathlib | no qualified target | exact digit theorems | no corresponding weight law; private NoetherNormalization sum helper located |
| local name index | project/scratch Kronecker names, not independent mathlib replacement | ofDigits declarations | existing weight definition and unrelated names |

The local index was available; its scratch hits were excluded as replacements. External services may index another revision. Pinned sources/signatures and actual native tests are decisive. Untruncated [current](../evidence/Roth.kroneckerExp_injOn/rg-current.json), [standard](../evidence/Roth.kroneckerExp_injOn/rg-standard.json), [abstract](../evidence/Roth.kroneckerExp_injOn/rg-abstract.json) searches are archived. The fresh isolated weighted `exact?` probe failed to close without timing out, with both project target and our invented helper guarded absent; this is only failed search evidence, not a theorem of nonexistence. It is retained separately as a rejected/search attempt, never accepted proof.

Positive blocks: `Nat.ofDigits_inj_of_len_eq` in `Mathlib/Data/Nat/Digits/Defs.lean:312`; `Nat.injOn_ofDigits` in `Mathlib/Data/Nat/Digits/Lemmas.lean:361`; `Nat.bijOn_ofDigits` there378; `Nat.ofDigits_eq_sum_mapIdx` there37; `Finsupp.weight_eq_sum` in `Mathlib/Data/Finsupp/Weight.lean:100`; list and equiv transports. Full sources are archived. The [isolated Colex candidate check](../evidence/Roth.kroneckerExp_injOn/kronecker-exp-injon-colex-executed.lean.txt) and [native receipt](../evidence/Roth.kroneckerExp_injOn/kronecker-exp-injon-colex-receipt.json) pin `Finset.geomSum_injective`: it takes a Finset of natural positions, hence digits0/1, and does not cover the arbitrary bounded multiplicities of d; [Colex source](../evidence/Roth.kroneckerExp_injOn/source-11.lean.txt) is hashed. `NoetherNormalization.sum_r_mul_ne` is **private**, restricted to Fin(n+1) and base2+totalDegree f; its existing proof duplicates the positional conversion. It is a concrete reuse anchor, not a public theorem that specializes to the proposed law.

Phase5 conclusion: existing digit-list uniqueness and conversion blocks, with a missing public bounded-digit weight bridge. Parent re-aim was genuinely tested and did not find an existing analogous weight law; NO-mathlib-has-it is unsupported for this declaration.

## Phase 5.5 — statement shape

Normal-form alternatives: pairwise equality implication; `Set.InjOn` on bounded Finsupps; injectivity on subtype; `Nat.injOn_ofDigits` on equal-length lists. Use `Set.InjOn` on the existing `Finsupp.weight`, rather than introduce another exponent definition. RHS convention n/a: not an iff or a bridge between competing normal forms. The weight equality normalization in the original bridge goes toward the existing weight/sum API, not an O(n²) family of aliases.

Syntactic restatements actually checked: explicit-e weighted law with hk, the no-hk weighted law, and no-hk law at the original `kroneckerExp` interface. Choose explicit e and arbitrary k to supply exactly the enumeration the caller owns. `σ`, natural base and bounded digits remain; standalone Fintype becomes superfluous when e is supplied, and hk is superfluous even at fixed parent. No unused field/l argument is falsely counted as a weakening. Overall **RESTATE-BEFORE-SHIP**.

## Phase 6.0 — callers and inline audit

| Source caller | Pattern | Refactor implication |
|---|---|---|
| `Roth.coeff_kronecker`, GenWronskian97–98 | `hed (kroneckerExp_injOn hk ... hd h.symm)` | After new upstream law exists, normalize h to geometric weight via `weight_eq_sum` and apply `weight_pow_injOn (Fintype.equivFin σ) k`; hk no longer needed by this step. The full scratch caller replay also removes hk cleanly, discovering it is unused in this coefficient statement under hP/hd. This is not a completed assessment of declaration109 or a production edit. |

One explicit internal named caller, one occurrence excluding declaration/doc/proof;0 external-to-file callers and0 distinct external files. No re-derivation elsewhere in production project sources. [caller search](../evidence/Roth.kroneckerExp_injOn/rg-callers.json), [inline search](../evidence/Roth.kroneckerExp_injOn/rg-inline.json), [caller metadata](../evidence/Roth.kroneckerExp_injOn/callers.json). The [full sole caller replay](../evidence/Roth.kroneckerExp_injOn/kronecker-exp-injon-consumer-executed.lean.txt) and [native receipt](../evidence/Roth.kroneckerExp_injOn/kronecker-exp-injon-consumer-receipt.json) are clean. A [Noether-normalization expanded-statement replay](../evidence/Roth.kroneckerExp_injOn/kronecker-exp-injon-noether-consumer-executed.lean.txt) with [receipt](../evidence/Roth.kroneckerExp_injOn/kronecker-exp-injon-noether-consumer-receipt.json) also passes over CommSemiring coefficients, using the same up=2+totalDegree and r=up^i formula; this is potential reuse, not an actual source caller or mathlib edit. Exact canonical293 name-array order/uniqueness/presence/value audit reports sole direct proof consumer `Roth.coeff_kronecker`. This is not the full implicit simp/kernel downstream closure. Target has no simp attribute. It is used, not dead code. The single local call is a weak NO signal outweighed by the concrete mathlib private duplicate and nontrivial representation bridge.

## Phase 6 — actual composition experiments

1. In list representation, `Nat.injOn_ofDigits hk n` is one existing call; native `digits_law` passes. This does not have the Finsupp domain or weight function.
2. Weighted current-law `exact?` fails cleanly as a search experiment. Neither parent Finsupp additive homomorphism structure nor positive weights grants injectivity. The experiment did not find a typeclass-derived or auto-generated equality theorem closing the bounded-weight goal.
3. Native generalized weighted proof succeeds, but is a genuine proof: `ofDigits_eq_sum_mapIdx`, `List.mapIdx_eq_ofFn`, `Fin.sum_ofFn`, `weight_eq_sum`, scalar-to-multiplication conversion, equivalence reindexing, list evaluation/length/cast normalization, `ofDigits_inj_of_len_eq`, `List.forall_mem_ofFn_iff`, `List.ofFn_injective`, surjective composition transport and `DFunLike.coe_injective`. More than3 existing calls, including a separately proved hsum and nontrivial rewrite transport. Counting only its last line or counting the new helper as mathlib would be false.
4. Original-interface no-base theorem follows from the **new** no-base helper plus weight normalization; verified bridge establishes applicability, not existing composability. No closing `simp [defs...]` proof of original injectivity was found; the Phase6b BORDERLINE simp heuristic therefore supplies no automatic NO here.

Conclusion **NOT-COMPOSABLE** by the tested routes in ≤3 existing calls; this is an evidence-based assessment, not a formal impossibility claim about every possible mathlib term. The mathematically substantive uniqueness is known, but the Finsupp representation bridge is reusable missing API. The public list theorem does not trigger the parent re-aim gate, because the actual parent replacement is weight, not list `ofDigits`.

## Phase 7 — verdict and actionable upstream plan

**YES-but-generalise-first**, reasons MODERN-IDIOM and verified weakening. Add `Finsupp.weight_pow_injOn` in proposed new file `Mathlib/Data/Nat/Digits/Finsupp.lean`, importing digits/list conversion and Finsupp.Weight. A dedicated bridge file avoids adding list/digit imports to foundational Weight. Proposed PR title: **feat(Data/Nat/Digits): injectivity of geometric Finsupp weights on bounded digits**.

The concrete gap is a public finite-exponent geometric-weight uniqueness API: Roth manually converts Finsupp exponent vectors to lists; mathlib’s own private `NoetherNormalization.sum_r_mul_ne`90–98 independently makes essentially the same conversion. Generalizing makes that use independent of a field, a polynomial-total-degree choice, a nonempty Fin(n+1) index, and the project-specific exponent alias. Keep the checked no-hk improvement and explicit enumeration. This is a small upstream bridge contribution with two concrete consumers, not a claim that elementary numeral uniqueness is new.

PR grouping: [accepted YES snapshot](../evidence/Roth.kroneckerExp_injOn/accepted-yes.json) includes `Roth.genWronskian` and Hasse-derivative results. The weight bridge should be a separate foundational PR, referenced by the later generalized-Wronskian PR; it should not be bundled with unrelated Hasse coefficient/derivative additions. None of the already assessed Kronecker/kroneckerExp/kronecker_monomial declarations is an accepted YES contribution.

Pre-PR checklist:

- [ ] `/generalise Roth.kroneckerExp_injOn`: retain checked arbitrary-e/no-hk result; evaluate injection-to-ℕ finite-support extension separately without asserting it already compiled.
- [ ] `/cleanup Mathlib/Data/Nat/Digits/Finsupp.lean Finsupp.weight_pow_injOn`: naming, import minimization, documented digit orientation, full audit and diff gates.
- [ ] Refactor private `NoetherNormalization.sum_r_mul_ne` to use the public bridge, independently build that module, then apply the original-interface bridge in sole Roth caller.
- [ ] Request a reviewer familiar with weights/digits: Yaël Dillies (recent affected-area commits631b214f7c/d99d52c36b) or Chris Birkbeck (weighted homogeneous API e011717410), based on [actual recent history](../evidence/Roth.kroneckerExp_injOn/reviewer-history.json). This is a reviewer suggestion, no contact/message was sent.

Alternative local destination pending upstream contribution: retain the useful arithmetic helper in `Roth/GenWronskian.lean`, preferably as a private general weight lemma. No deletion/refactor has been made by this assessment. Cost does not determine the verdict. No unanswered user design question or pending verification is required for this read-only verdict; the read-only worker assessment is complete.

## Phase 8 — evidence and completion

All phases are complete with theorem-only infrastructure/one-line exceptions justified. Exact accepted Lean snippets and raw native receipts, separately labelled rejected/search attempts, expected axiom declarations, fresh native-region boundaries, hashes and original execution paths are linked in [verification](../evidence/Roth.kroneckerExp_injOn/verification.json). Accepted proofs use only standard `propext`, `Classical.choice`, `Quot.sound`; no sorry, axiom, unsafe, native_decide, or raised limits. Search failure is never accepted proof. [Portable validator](../evidence/Roth.kroneckerExp_injOn/validate.py) checks current copy-manifest, all17 current inputs, exact canonical293 order, receipts, search protocol and credential guard. Worker assessment completed; machine metadata separately tracks integration acceptance.
