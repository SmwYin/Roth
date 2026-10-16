# Phase 4: `kronSpan_mono`

Scope: only original private lemma at fresh lines 145–147 (3 lines), plus its sole direct caller expression in `derivative_mem_kronSpan`. No caller audit credit. Baseline frozen full/separate builds supplied by owner; fresh complete native LSP before editing succeeds with exactly the five known outside warnings. Worker snapshot `/private/tmp/roth-kronSpan_mono-start.lean`.

Read both installed skills, full worker contract, golfing-rules, proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates, applicable style sections, naming guide. Existing docstrings/comments protected by owner instruction.

## Initial 24-item audit

1. LINT: no diagnostic in target; five outside warnings remain (header metadata, two Fintype warnings on dependent zero theorem, DecidableEq on det_sum_rows, Fintype on existence theorem).
2. HAVE SCAN: none in this term proof.
3. SET_OPTION: none.
4. SIMP SQUEEZE: no simp calls.
5. NAMING: describes monotonicity of existing subject `kronSpan`; no forbidden abbreviation/pattern. Proposed deletion makes rename unnecessary.
6. LINE PACKING: original width table below; target is removed rather than cosmetically repacked.
7. BY PLACEMENT: term proof, no by.
8. FORMAT: original lambda arrow `=>` disappears with wrapper; replacement uses `↦`. No instance declarations, semicolons, empty proof lines, or haveI/letI.
9. COMMENTS: target contains none; every surrounding comment/docstring remains untouched.
10. DOCSTRING: n/a private lemma with none.
11. VISIBILITY: private; only one same-file caller.
12. STRUCTURE: one term proof line, no conjunction or branches; deletion needs no helper.
13. MATHLIB: exact span/image monotonicity composition already in Mathlib, five searches below; remove wrapper and specialize APIs at caller.
14. JUNK DEF: n/a theorem, no definition changed.
15. EXISTS LEMMA: n/a conclusion is a submodule inequality.
16. SHOW vs CHANGE: none.
17. PUSH_NEG: none.
18. GENERALISE: complete parameter table below. Generic span result already has Semiring/module generality; no new abstraction needed.
19. INEQUALITY: table below; no reversed inequality.
20. NORMAL-FORM: canonical submodule inclusion `≤` induced by generating-set inclusion `⊆`.
21. SYNTAX-GEN: direct Mathlib APIs apply to caller's membership hypothesis without extra project API.
22. IMPORT-FANOUT: n/a no import additions.
23. CASTS: zero casts/coercions added; deleted `(K := K)`/`(σ := σ)` are named arguments, not casts.
24. INSTANCE-NAME: n/a no instance declaration.

Issues: one redundant private span/image wrapper; action delete and replace its one caller expression using Submodule.span_mono and Set.image_mono. No public changes, no new helper. Refactoring needed after local authorized deletion: none.

## Five-method Mathlib search

A. Lean-Finder: “Submodule.span is monotone with respect to inclusion of generating sets” → Submodule.span_mono, Submodule.span_monotone.
B. Loogle: `Submodule.span, _ ⊆ _ → _ ≤ _` → complete empty result; no absence claim made.
C. LeanSearch: “span of image of smaller set is contained in span of image of larger set” → Submodule.span_monotone, Submodule.image_span_subset_span.
D. Source rg: span_mono/image_mono and predicate-set inclusion variants → Span/Defs.lean:83, Data/Set/Image.lean:221; checked actual source and signatures.
E. lean_local_search `span_mono` → Submodule.span_mono/ span_monotone; index reports unavailable, but returned exact source hits, not treated as evidence of absence.

Auxiliary variants: span_monotone, span_le, subset_span, image_mono, ofPred_subset_ofPred_of_imp. Common-equivalents lookup: no special discrete/finite bucket; generic order/module monotonicity suffices. Six rules: (1,5) remove wrapper rather than simplify; (2) all five actual queries performed, no absence claim; (3) auxiliary variants checked; (4) no custom predicate replacing a typeclass; (6) record direct API usage here, respecting explicit module-docstring preservation instruction.

## Generalisation: every parameter

| Parameter | Class / use | Mechanical candidates / evidence | Result |
|---|---|---|---|
| `{K : Type*}` | coefficient type, both kronSpan instances | Drop invalid: Polynomial K and MvPolynomial σ K require the type; universes already polymorphic | retain type in independent statement; wrapper deleted |
| `[Field K]` | supplies structure required by named project definitions | Drop prevents kronecker/kronSpan from elaborating; DivisionRing does not supply CommSemiring required for MvPolynomial. CommSemiring clone probe separately compiled (below); predicate IsField reformulation adds unnecessary data | generic Mathlib span API already Semiring; no surviving wrapper to weaken |
| `{σ : Type*}` | monomial exponent domain, function domain | Drop invalid because σ occurs in MvPolynomial and σ →₀ ℕ; universe already arbitrary | retain type dependency |
| `[Fintype σ]` | chosen enumeration inside kronecker | Drop / Finite alone cannot supply chosen Fintype.equivFin σ used by unchanged kronecker; switching enumeration changes private/public definitions outside this target | preserve dependent definitions |
| `(k : ℕ)` | fixes kronecker substitution on both sides | Drop invalid: k is free in both spans; abstract scalar/map replacement already exactly Mathlib span_mono, so delete wrapper | direct specialization |
| `{μ : ℕ}` | smaller degree cutoff | Drop invalid: μ free in hypothesis and conclusion; abstract order generality already supplied by Mathlib | direct specialization |
| `{ν : ℕ}` | larger degree cutoff | Drop invalid: ν free in hypothesis and conclusion; no point-local predicate in statement | direct specialization |
| `(h : μ ≤ ν)` | transports each generator degree bound | No weaker strict-to-weak candidate: already weak. Drop mathematically false: K=ℚ, σ singleton, k=2, μ=1, ν=0; order-one Hasse operator kills 1 and sends X to 1, so cannot be polynomial scalar times order-zero identity (evaluation on 1 forces scalar zero) | keep ordering dependency in independent reproof |
| `{l : ℕ}` ambient | unused section variable | Not in elaborated target type; independent #check confirms automatically omitted | no change |

No bundled/analytic/global-function assumptions to unbundle or point-localise; no decidability assumption. Inversion check fires: the proof uses only generic set inclusion and span monotonicity, confirming deletion rather than a new abstract helper. Big-change candidates: none needed, since existing Mathlib API already has full algebraic/order generality.

Literature: n/a: private decl, literature search not required (both WebSearch and ChatGPT math MCP exempt).

## Signature widths and inequalities

Original signature at fresh L145 has 59 codepoints; next complete conclusion `kronSpan (K := K) (σ := σ) k μ ≤ kronSpan k ν :=` has 48. Thus 59+1+48=108 >100, ok. L146 has 52 codepoints including indentation, final signature line: no next signature token, ok. Final source has no surviving target signature, so final width table has zero rows (declaration deleted); original statement reference at format.width 100 is recorded in independent verification output.

| Occurrence | Original | Rewrite | Final |
|---|---|---|---|
| L145 h | μ ≤ ν | none, smaller side left | original statement independently reproved |
| L146 conclusion | kronSpan k μ ≤ kronSpan k ν | none | wrapper deleted |

Zero ≥ or > tokens in target signature; no _ge_/_gt_ name.

## Rule pass (all 42)

- 1.1 n/a original already term proof.
- 1.2 n/a no by rfl.
- 1.3 n/a no rw/exact pair.
- 1.4 n/a no simp/exact pair.
- 1.5 n/a no trailing rfl.
- 1.6 n/a no constructor.
- 1.7 n/a no apply/exact pair.
- 1.8 n/a no contradiction.
- 1.9 n/a lambda genuinely transforms bound, not eta form.
- 1.10 n/a no have.
- 1.11 n/a no apply/intro pair.
- 1.12 n/a no show.
- 1.13 n/a no projected have.
- 1.14 n/a no rw.
- 1.15 n/a no simp only.
- 1.16 n/a no simp.
- 1.17 n/a span/image calls already appropriate; Nat.le_trans/hd.trans considered in independent probe.
- 1.18 n/a inner application requires grouping in caller argument; no gratuitous final parentheses.
- 1.19 n/a no push_neg.
- 1.20 n/a not existential.
- 2.1 grind: actual scratch automation probe recorded below.
- 2.2 n/a no existing grind chain.
- 2.3 n/a no simplification chain.
- 2.4 n/a no analytic function-property goal.
- 2.5 n/a no numeric positivity goal.
- 2.6 gcongr: actual scratch automation probe recorded below.
- 2.7 n/a target is submodule inclusion rather than Nat/Int arithmetic goal; bound transport is direct transitivity.
- 2.8 aesop: actual scratch automation probe recorded below.
- 2.9 n/a no numerical/cast equality.
- 2.10 n/a arbitrary submodule inclusion is not finite decidable computation.
- 2.11 n/a no denominator identity.
- 2.12 n/a no ring/ring_nf ending.
- 2.13 n/a no symmetric branches.
- 2.14 n/a no calc.
- 2.15 n/a no multiple generated goals.
- 3.1 n/a no erw.
- 3.2 n/a no continuity/measurability.
- 3.3 n/a no omega in owned target.
- 3.4 n/a no rcases.
- 3.5 n/a deleted private wrapper needs no automation registration.
- 3.6 n/a no simp_all.
- 3.7 n/a no heartbeat option.

## Step back

The original proof is already a one-line term, but retaining it duplicates two generic Mathlib APIs. Removing it reduces declaration count and uses existing interfaces directly. exact?/apply? and automation experiments are verification-only; no discovery tactics remain in source. No representation redesign is useful.

## Verification

Actual native `lean_multi_attempt` on the external scratch path was rejected because /private/tmp has no lean-toolchain ancestor. Used direct `lake env lean` isolated source clones instead, with default options. Actual outcomes: grind failed with unsolved False; aesop failed with no progress; gcongr made no progress; exact? and apply? each reached the standard 200000-heartbeat limit. No options raised; successful explicit term is short and deterministic. The independent source clone reproof below succeeds without referencing the deleted wrapper.

| Original signature line | Codepoints | Next complete token | Arithmetic | Action |
|---|---:|---|---|---|
| 145 | 59 | full conclusion and := (48) | 59+1+48=108 >100 | ok |
| 146 | 52 | none, proof body follows | n/a | ok |

Final target signature: deleted, zero surviving signature lines; the table above covers every original line. Changed caller expression lines are all below 100 codepoints.

Original-statement independent source-clone probe `/private/tmp/roth-kronSpan_mono-probe.lean`, session97232, exit0:

```lean
@originalStatement : ∀ {K : Type u_3} [inst : Field K] {σ : Type u_4} [inst_1 : Fintype σ] (k : ℕ) {μ ν : ℕ},
  μ ≤ ν → kronSpan k μ ≤ kronSpan k ν
```

Proof is `Submodule.span_mono (Set.image_mono fun _ hd ↦ (Set.mem_ofPred_eq ▸ hd).trans h)` against exact cloned private definitions, with no self-reference. Axioms: `[propext, Classical.choice, Quot.sound]`. Separate minimal clone `/private/tmp/roth-kronSpan_mono-generalise.lean` verifies the underlying construction and span proof with CommSemiring K, session21742 exit0, same standard axioms. This broadens cloned definitions only; no definition change in project.

Final module `/Users/ramin/.elan/bin/lake build Roth.GenWronskian`, session64120, exit0, module built in26s. Complete native LSP after edit: success=true, partial=false, timed_out=false; zero errors, failed_dependencies=[]; all warnings retained: header at1, unused section Fintype at36, unused type Fintype at32, unused DecidableEq at221, unused Fintype on existence theorem at239.

Worker diff against source snapshot: deletes target plus following separator, replaces only one direct caller expression, caller gains one line. All definitions/public signatures/docs/comments byte-preserved. Net source −3 lines; declaration count −1. No new axiom/sorry/native_decide/option/import.

Source final SHA256 `cb4e0d6efa8a7e2b8a270914c87db5d1882b31bc5f7d205c97853a2826d56847` sent to owner after module+LSP success. Owner acknowledged freeze and revoked source ownership; subsequent work restricted to report and isolated checks.

### Gate status

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | module session64120 exit0 |
| definition_protected | pass | no definition lines changed |
| theorem_statement_protected | pass, authorized private deletion | owner explicitly permitted routine single-use wrapper deletion; every remaining signature byte-identical |
| structure_gate | pass | target deleted; no new helper/conjunction/branch |
| naming_gate | pass | no forbidden pattern; no surviving target or rename |
| line_packing_gate | pass | two original lines measured above; zero final target lines; caller expression ≤100 |
| inequality_orientation_gate | pass | per-occurrence table; zero ≥/> in owned statement |
| caller preservation | pass | isolated before session81073 / after session64659 both exit0, identical printed type and standard axioms |

Overall: source/module/LSP gates pass. Full project and separate LeanEval gates are owner-only; worker did not run them.

### Result

Before3 declaration lines, after0: saved3 declaration lines; net file −3 after caller adjustment and separator deletion. Audit issues found1, fixed1, deferred0. Rules applied: Mathlib replacement rules1/5 (delete wrapper), lambda syntax normalization in necessary caller expression; all42 golfing rules assessed. Renames queued:none. Comments preserved:none in target; every outside comment and existing private docstring untouched. Refactoring needed:none.

### Phase checklist

- [✓] Step1 reference docs read.
- [✓] Step2 full24-item audit recorded.
- [✓] Step2.5 actual five-method Mathlib search recorded.
- [✓] Step2.6 every parameter audited; private literature exemption explicit.
- [✓] Step2.7 every original signature line measured; target deleted.
- [✓] Step2.8 inequality occurrence table recorded.
- [✓] Step3 all42 rules have status.
- [✓] Step4 step-back reflection recorded.
- [✓] Step5a complete native diagnostics succeeds with known outside warnings.
- [✓] Step5b diff gates recorded and module build passes.
- [✓] Step6a no rename needed; sidecar untouched.


### Caller original-type and axiom verification

Exact source clones `/private/tmp/roth-kronSpan_mono-caller-before.lean` and `...-after.lean` independently compiled with `lake env lean`, sessions81073 and64659, both exit0. Before and after printed the identical original caller type at format.width100:

```lean
@Roth.derivative_mem_kronSpan : ∀ {K : Type u_1} [inst : Field K] {σ : Type u_2} [inst_1 : Fintype σ] (k μ : ℕ)
  {F : MvPolynomial σ K → Polynomial K},
  F ∈ Roth.kronSpan k μ → (fun P => Polynomial.derivative (F P)) ∈ Roth.kronSpan k (μ + 1)
```

Both printed precisely `[propext, Classical.choice, Quot.sound]` for the caller axioms. Full source cloning is necessary because the caller and kronSpan are private; no use of unsafe private aliases, self-reproof, sorry, axioms, or options. No caller cleanup audit credit claimed. All worker checks complete.
