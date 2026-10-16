# Phase 4 — `kronSpan`

Owned declaration: `Roth/GenWronskian.lean:141–143`, private definition. Source ownership
was revoked after final source/module/LSP handoff; remaining work touched only this report
and isolated `/private/tmp` verification. No Git, full-project builds, LeanEval, sibling
source edits, shared logs, renames, imports, or new declarations were added.

Both installed skill files and the full 853-line worker contract were read. Required
references read: golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, cleanup-gates.md; relevant style-rules.md sections and naming
conventions were also consulted. Initial audit `.mathlib-quality/cleanup/GenWronskian.md`
was read. Native Lean tools were discovered through ALL_TOOLS and schemas read from
`/private/tmp/roth-mcp-tools.json`; native tools responded without helper fallback.

## Full audit

1. LINT: none at lines 141–143. Complete before/after LSP has five unchanged warnings:
   missing copyright metadata at L1; unused Fintype section/type parameters in
   genWronskian_eq_zero_of_not_linearIndependent at L36/L32; unused DecidableEq in
   det_sum_rows at L224; unused Fintype in exists_genWronskian_ne_zero at L242.
2. HAVE SCAN: n/a, direct data expression contains no `have`.
3. SET_OPTION: none in declaration; no options introduced.
4. SIMP SQUEEZE: n/a, no tactics or simp calls.
5. NAMING: `kronSpan` is lowerCamelCase for data, describes the span of the named
   Kronecker-Hasse operators, and contains none of the forbidden abbreviations/patterns.
6. LINE PACKING: move `Submodule (Polynomial K)` to declaration line; measured below.
7. BY PLACEMENT: n/a, term-mode definition with no `by`.
8. FORMAT: original 4-space signature continuation and 2-space body retained; no blank
   internal lines, trailing whitespace, `haveI`, `letI`, or syntax changes to the value.
9. COMMENTS: existing one-line private docstring preserved byte-for-byte under explicit
   user protection; no inline comments were present.
10. DOCSTRING: generic private-doc stripping is overridden by the explicit preservation
    instruction. Existing sentence correctly identifies generators and order bound.
11. VISIBILITY: private is correct; used only by this file's Hasse-span argument.
12. STRUCTURE: three declaration lines; one data-expression body line; no conjunction,
    branches, or proof extraction needed.
13. MATHLIB: five actual methods below; uses `Submodule.span` and Set.image directly.
14. JUNK DEF: keep. This names a domain-specific filtered submodule used in monotonicity,
    derivative stability, and Hasse-derivative membership lemmas; it has surrounding API
    and multiple users outside one proof. It passes the documented keep/API test.
15. EXISTS LEMMA: n/a, not a proposition or existential witness lemma.
16. SHOW vs CHANGE: n/a, no show/change terms.
17. PUSH_NEG: n/a, no tactics.
18. GENERALISE: every elaborated parameter assessed below; no signature/value change.
19. INEQUALITY: only degree ≤ μ appears in the value; zero reversed inequalities in
    the signature or body. Required scan table below.
20. NORMAL-FORM: already canonical `Submodule.span R (f '' s)`; no custom closure
    predicate or bespoke module construction. Independent sInf reconstruction verifies
    the universal-property interpretation.
21. SYNTAX-GEN: OK. The current result is a submodule of functions so generic span
    induction applies directly; bundled linear operators would redesign the operator
    representation and downstream API without improving this definition.
22. IMPORT-FANOUT: n/a, no new imports.
23. CASTS: zero dropped, zero cross-type, zero load-bearing casts in diff; only whitespace
    moves. `(K := K)` is an explicit named type argument in unchanged body, not a cast.
24. INSTANCE-NAME: n/a, declaration is not an instance and creates none.

Issues found: one underpacked signature; fixed one. Refactoring needed: none. Optional
bundled operator/module redesign closed as unnecessary: the existing function module
supports span induction and all downstream results directly. No compiled proposal or
parent decision is needed for a redesign that is not being proposed/applied.

## Mathlib search-status

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | `Submodule span image of Hasse derivative operators of bounded total degree under polynomial substitution` | Polynomial.degreeLT, Polynomial.hilbertPoly_linearMap, Polynomial.hasseDeriv; none duplicates the filtered operator submodule |
| B Loogle | `Submodule.span, Set.image` | Submodule.span_sInf_le, Submodule.span_sSup, Finsupp.supported_eq_span_single, Finsupp.single_mem_span_single, Finsupp.span_image_eq_map_linearCombination |
| C LeanSearch | `submodule span of the image of a set of generators` | Submodule.image_span_subset_span, Submodule.span_range_eq_iSup, LinearMap.map_span |
| D source rg | `def span`, `span_image`, `span_mono`, `span_induction` in Span/{Defs,Basic}.lean; full-name `\bkronSpan\b|\bkronHasse\b` over Mathlib | generic span definition/induction/monotonicity/image API found; full-name search had zero hits |
| E lean_local_search | `Submodule.span`, limit 6 | Submodule.span, span.ringHom, span_eq, span_le, spanRank, span_pow; `index: unavailable` is recorded, not interpreted as absence |

Auxiliary variants searched directly in source: span_image, span_image_linearEquiv,
apply_mem_span_image_of_mem_span, apply_mem_span_image_iff_mem_span, span_mono,
span_monotone, span_induction, span_induction₂. Common-equivalents lookup: no matching
bucket beyond the already-used generic submodule construction. Concluded: partial match,
KEEP the domain-specific submodule and build directly on `Submodule.span`. The searches
establish the generic APIs used here; no claim of exhaustive mathematical absence is
made. No wrapper lemma/predicate is introduced, and no replacement calls are needed.
Six strict rules checked: no wrapper lemma, all five methods executed, auxiliary variants
searched, no custom class predicate, no duplicate to delete, existing protected module
doc unchanged because this whitespace-only edit adds no dependency requiring new usage
text. `exact?`/`apply?` absence probes are n/a: there is no proposition proof or proposed
new lemma; the generic construction is already used directly.

## Generalisation status

Elaborated original parameters (width-100 #check in isolated clone):
`{K : Type u} [Field K] {σ : Type v} [Fintype σ] (k μ : ℕ)`.
Section parameter `l` is absent from the elaborated type and value.

| # | Parameter | Class | Mechanical candidates / precise dependency | Verified? / result |
|---|---|---|---|---|
| 1 | `{K : Type*}` | type variable | Drop impossible: appears in scalar Polynomial K and function domain/codomain. Universe already independent and polymorphic. Point-localise/strict→weak n/a: type parameter. | Precise dependency; retain |
| 2 | `[Field K]` | typeclass | Drop; parents CommSemiring, CommRing, DivisionRing considered. Existing body explicitly calls kronHasse→kronecker, whose fixed public signature requires Field K and returns a K-algebra hom. Generalising it requires changing public dependency, outside this private definition. Merely making span weaker leaves the generator unavailable. | Precise signature dependency; retain, not a claim field axioms are mathematically minimal |
| 3 | `{σ : Type*}` | type variable | Drop impossible: MvPolynomial σ K domain and finitely supported generator indices use σ. Universe already independent/polymorphic. Point-localise/strict→weak n/a. | Precise dependency; retain |
| 4 | `[Fintype σ]` | typeclass | Drop; parent Finite considered. Generator kronHasse→kronecker uses Fintype.equivFin σ and its public type requires Fintype. Finite does not supply this enumeration value; replacing with a chosen Fintype can change the specific substitution. No pointwise/strict form applies. | Precise value/signature dependency; retain |
| 5 | `(k : ℕ)` | structure value | Drop/abstract index considered. k occurs in the actual generator `kronHasse k` and its substitution exponents k^(e j). For the coordinate with e j=1, Δ₀(X j) maps to X^k, distinguishing k=2 from k=3 over ℚ. Abstract order would not supply exponentiation data. No hypothesis to localise/weaken. | Precise dependency and counterexample; retain |
| 6 | `(μ : ℕ)` | structure value | Drop/abstract ordered bound considered. μ occurs in the set `{d | d.degree ≤ μ}`; e.g. σ=Fin 1 has index e_j admitted at μ=1 but not μ=0. The span at μ=0 contains multiples of substitution, whereas Δ_ej at μ=1 kills 1 but sends X j to 1, so cannot be such a multiple. Natural degree already fixes bound type. No strict hypothesis to weaken. | Precise dependency/counterexample; retain |

Small-safe generalisations kept: none. Big-change candidates: none proposed; weakening
Field mathematically would require a separate public Kronecker API redesign, which is
unneeded here. Inversion check: n/a, data construction rather than theorem proof that
forgets its concrete input; generator and degree bound occur explicitly in the value.
Literature search: n/a: private declaration, literature search not required (contract
Step 2.6d). No public web/ChatGPT queries were run for this private declaration.

## Line packing

Definition reference: n/a for definition per contract; isolated clone still prints
`#check @kronSpan` under `format.width 100` to independently confirm full implicit type.
Before:

| Signature line | Chars | Next complete token group | Arithmetic | Action |
|---|---:|---|---|---|
| 141 | 46 | `Submodule (Polynomial K)` (24) | 46+1+24=71 ≤100 | repack |
| 142 | 65 | none; body next | n/a | ok |

After (all codepoint widths remeasured):

| Signature line | Chars | Next complete token group | Arithmetic | Action |
|---|---:|---|---|---|
| 141 | 71 | `(MvPolynomial σ K → Polynomial K)` (33) | 71+1+33=105 >100 | ok |
| 142 | 40 | none; body next | n/a | ok |

The parenthesised function type is the next syntactic type argument; it cannot join
line 141 without overflow. No remaining underpacked complete signature argument.

## Inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| — | signature and body | no `≥` or standalone `>`; body has `d.degree ≤ μ` | n/a | n/a |

`→` arrows are function types, not reversed inequalities. Name has no `_ge_`/`_gt_`.

## Golfing rule pass (42 rules)

- [1.1] by exact wrapper: n/a — no by/exact.
- [1.2] by rfl: n/a — no by/rfl.
- [1.3] rw + exact: n/a — no tactics.
- [1.4] simp + exact: n/a — no tactics.
- [1.5] trailing rfl: n/a — no tactics.
- [1.6] anonymous constructor: n/a — no constructor.
- [1.7] apply + exact: n/a — no tactics.
- [1.8] by_contra + push_neg: n/a — no negation proof.
- [1.9] eta-reduce: n/a — no lambda in this definition; generator already unapplied.
- [1.10] inline have: n/a — no have.
- [1.11] apply + intro: n/a — no tactics.
- [1.12] redundant show: n/a — no show.
- [1.13] have + projection: n/a — no have/projection.
- [1.14] merge rw: n/a — no rw.
- [1.15] unsqueeze terminal simp: n/a — no simp.
- [1.16] squeeze nonterminal simp: n/a — no simp.
- [1.17] dot notation: n/a — Submodule.span is constructor with scalar argument, no receiver.
- [1.18] use <|: n/a — image/set arguments already direct, no removable nested parentheses.
- [1.19] push Not: n/a — no push_neg.
- [1.20] inline existential helper: n/a — data definition with multiple users/API, not existential helper.
- [2.1] grind whole proof: n/a — data definition in direct term mode, no tactic proof.
- [2.2] delete tactics before grind: n/a — no tactics.
- [2.3] simpa consolidation: n/a — no tactics.
- [2.4] fun_prop: n/a — no analytic property goal.
- [2.5] positivity: n/a — no inequality proof goal.
- [2.6] gcongr: n/a — no inequality proof goal.
- [2.7] lia / omega: n/a — no arithmetic proof goal.
- [2.8] aesop: n/a — data construction, no logic or membership goal.
- [2.9] norm_num / norm_cast: n/a — no numeric/cast proof goal.
- [2.10] decide / decide +kernel: n/a — data construction, no decidable proposition.
- [2.11] field_simp; ring: n/a — no denominator identity.
- [2.12] linear_combination: n/a — no ring/ring_nf proof.
- [2.13] wlog: n/a — no branches.
- [2.14] collapse calc: n/a — no calc.
- [2.15] <;>: n/a — no multiple goals.
- [3.1] erw → rw: n/a — no erw.
- [3.2] legacy → fun_prop: n/a — no analytic tactics.
- [3.3] omega → lia: n/a — no omega.
- [3.4] rcases with rfl: n/a — no cases.
- [3.5] automation attributes: n/a — definition, no new proposition API or normal form to register.
- [3.6] simp_all: n/a — no simp_all.
- [3.7] remove heartbeat option: n/a — none present.

## Step back and think

The existing body is already one canonical span construction. Automation would replace
an explicit data value with proof search without improving it. Alternative range or
linear-combination/image representations have generic conversion API, but the present
image-of-order-bounded-indices form exposes exactly what downstream span induction needs.
No missing API signal, single-use intermediate, redundant proof step, or proof strategy
exists. Keep the value and pack only its signature.

## Verification and gates

Original baseline target and final target were parsed independently and compared after
whitespace normalisation: identical tokens. Only the two signature lines moved; the
entire body and docstring are unchanged. Isolated exact-source clone is
`/private/tmp/kronSpan-verify.lean`; original private type/value example, independently
expanded sInf/aeval reconstruction, and standard-axiom checks are included there.

Isolated verification completed: `/Users/ramin/.elan/bin/lake env lean
/private/tmp/kronSpan-verify.lean`, session42351 exit0. It accepted the exact original
private return type, `rfl` against the original defining value, and the independently
expanded sInf construction proved via the two directions of image membership. `#print
axioms kronSpan` reports exactly `[propext, Classical.choice, Quot.sound]`. Initial scratch
errors (noncomputable example, namespace reopening, sInf binder type) were repaired only
in the scratch file; the final scratch is error-free. Log:
`/private/tmp/kronSpan-verify.log`.

Complete final native LSP: success=true, partial=false, timed_out=false, zero errors,
failed_dependencies=[], five unchanged warnings listed in item 1. Artifact:
`/private/tmp/kronSpan-lsp.json` (full tool return, no warning filtering).

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | `/Users/ramin/.elan/bin/lake build Roth.GenWronskian`, session53968 exit0, built target in22s |
| definition_protected | pass | exact original type/value tokens unchanged; explicitly authorized routine private signature packing |
| theorem_statement_protected | pass | no theorem or lemma line changed |
| structure_gate | pass | one-line body, no conjunction/branches |
| naming_gate | pass | descriptive data lowerCamelCase, no forbidden names |
| line_packing_gate | pass | final two-row measured table,105>100 break |
| inequality_orientation_gate | pass | zero reversed inequalities |

Overall: pass; isolated verification completed successfully. Full-project and
separate LeanEval gates belong to owner; no worker claim is made for them.

## Result

Before3 lines; after3 lines; saved0 lines. Issues found1; fixed1; deferred0.
Golfing rules applied: none applicable to direct data body; packing audit item6 applied.
Renames queued: none. Comments preserved:1/1 original docstring, zero relocations.
Refactoring needed: none. No sorry, new axiom, weaker result, native_decide, version,
option raise, import, public declaration or definition value change.

Phase checklist:

- [✓] Step1 — reference docs read.
- [✓] Step2 — full24-item audit.
- [✓] Step2.5 — actual five-method search status.
- [✓] Step2.6 — every elaborated parameter/generalisation status; private literature exemption.
- [✓] Step2.7 — before/after per-line width table.
- [✓] Step2.8 — inequality scan table.
- [✓] Step3 — all42 golfing rule statuses.
- [✓] Step4 — step-back reflection.
- [✓] Step5a — complete final LSP, no errors.
- [✓] Step5b — gate status block and source-start diff inspected.
- [✓] Step6a — no renames needed.

Final source SHA256: `783c291cbae82149741146cdf964f79d1b26b84cc23c7191613fef88bb984a75`.

Exact worker diff:

```diff
--- start
+++ final
@@ -138,8 +138,8 @@
   fun P ↦ kronecker k (hasseDeriv d P)
 
 /-- The `K[X]`-span of the operators `kronHasse k d` with `|d| ≤ μ`. -/
-private noncomputable def kronSpan (k μ : ℕ) :
-    Submodule (Polynomial K) (MvPolynomial σ K → Polynomial K) :=
+private noncomputable def kronSpan (k μ : ℕ) : Submodule (Polynomial K)
+    (MvPolynomial σ K → Polynomial K) :=
   Submodule.span (Polynomial K) (kronHasse (K := K) k '' {d | d.degree ≤ μ})
 
 private lemma kronSpan_mono (k : ℕ) {μ ν : ℕ} (h : μ ≤ ν) :
```
