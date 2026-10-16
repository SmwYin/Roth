# Phase 4 — `Roth.kronecker_eq_zero_iff`

Scope: only this declaration in `Roth/GenWronskian.lean`, current L98–103. Source frozen at
SHA256 `a17695405eb4047be5fa1470a670fd6b55a9a242b2b82357f5c37a0fc56ef5df`; ownership revoked
by parent after module/LSP gates. Original declaration: 8 lines; final: 6; saved: 2.
Public type, definitions, docstring, source reference, comments and attributes preserved.
No helper introduced. Baseline: parent full/separate gates and initial audit
`.mathlib-quality/cleanup/GenWronskian.md`; independent pre-edit module build exit 0.

## Step 1 — references

Read both installed `mathlib-quality/SKILL.md` and `lean4/SKILL.md`, full worker contract,
`golfing-rules.md`, `proof-patterns.md`, `mathlib-search.md`, `generalisation-patterns.md`,
`cleanup-gates.md`, relevant `style-rules.md`, `naming-conventions.md`, and
`mathlib-review-stages.md`. Existing documentation/signature preservation overrides generic
rewrite suggestions. No Git, shared log, full-project build, LeanEval, or other source edits.

## Full 24-item audit

1. **LINT:** no target warning. Complete final LSP has only the five previously identified
   outside warnings, listed in verification below.
2. **HAVE SCAN:** zero `have` bindings before/after; no single-use term to inline.
3. **SET_OPTION:** none in declaration; no limit changes.
4. **SIMP SQUEEZE:** both original `simpa` calls were terminal. Final single `simpa [h] using`
   is terminal and remains unsqueezed. No nonterminal bare `simp`.
5. **NAMING:** `kronecker_eq_zero_iff` describes the zero equivalence; snake_case, no forbidden
   abbreviation, numeric scheme, `_ge_`, or `_gt_`; no rename needed.
6. **LINE PACKING:** every signature line measured below, both pass.
7. **BY PLACEMENT:** `:= by` stays at end of conclusion line.
8. **FORMAT:** ordinary lambdas normalized to `↦`; two-space proof indentation; no empty
   lines inside declaration, no semicolon chain, no `haveI`/`letI`.
9. **COMMENTS:** zero proof comments present; entire existing docstring/source citation preserved.
10. **DOCSTRING:** present, states bounded-degree zero detection and cites source §2.
11. **VISIBILITY:** public API retained as requested; no helper added.
12. **STRUCTURE:** 4 proof lines, no conjunction statement, no >10-line branch. Replaced
    extensionality/exponent case split with support emptiness and coefficient contradiction.
13. **MATHLIB:** five actual search methods below; generic supporting APIs reused directly.
14. **JUNK DEF:** n/a: theorem, no data definition.
15. **EXISTS LEMMA:** n/a: public equivalence, no trivial existential helper.
16. **SHOW/CHANGE:** n/a: no `show` before/after.
17. **PUSH_NEG:** n/a: no `push_neg` before/after.
18. **GENERALISE:** every explicit/inherited parameter audited below; public type retained.
19. **INEQUALITY:** only `1 < k` and `degreeOf j P < k`; no reverse inequalities.
20. **NORMAL-FORM:** substituted zero iff original zero, with canonical zero RHS. Under a
    degree bound the substitution need not be globally injective; generic global-injectivity
    `map_eq_zero_iff` does not replace this restricted statement.
21. **SYNTAX-GEN:** OK: implicit polynomial/base and explicit degree-bound proof are convenient
    for downstream `rw [← kronecker_eq_zero_iff hk hdeg]`.
22. **IMPORT-FANOUT:** n/a: zero new imports.
23. **CASTS:** 0 dropped / 0 cross-type / 0 load-bearing added; no cast in changed proof.
24. **INSTANCE-NAME:** n/a: theorem, no instance introduced or renamed.

Issues fixed: (1) ordinary lambda arrows; (2) unnecessary exponent case split, consolidated
through generic support API. Refactoring needed: none. Renames queued: none.

## Mathlib search status

[A] **Lean-Finder:** actual `lean_leanfinder` query “multivariate polynomial equals zero if
coefficients on support vanish Kronecker substitution bounded degrees”; returned
`MvPolynomial.totalDegree_eq_zero_iff`, `aeval_eq_zero`, `sum_eval_eq_zero`,
`coeff_toPolynomialAdjoinImageCompl_ne_zero`, `eval₂Hom_eq_zero`; supporting facts only.
[B] **Loogle:** initial `MvPolynomial.coeff, _ = 0` rejected identifier; corrected actual
`"MvPolynomial.coeff", _ = 0` returned `coeff_zero_X`, `coeff_zero`, `coeffs_C`,
`coeff_C_of_ne_zero`, `coeff_add_single_C`, `coeff_single_X_pow`, `coeff_rename_eq_zero`,
`coeff_eq_zero_of_totalDegree_lt`. None supplies bounded substitution zero reflection.
[C] **LeanSearch:** actual query “A multivariate polynomial is zero if every coefficient in
its support is zero”; returned `Polynomial.ofFinsupp_eq_zero`, `toFinsupp_eq_zero`,
`card_support_eq_zero`, `MvPolynomial.ne_zero_iff`, `support_zero`.
[D] **Source rg:** untruncated searches in MvPolynomial, MonoidAlgebra and Finsupp for
`eq_zero_iff`, `ext.*support`, `eq_zero.*support`, `support.*eq_zero`, `coeff.*degreeOf`,
`kronecker_eq_zero_iff`, `kronecker.*injective`, `coeff.*support`. Found
`MvPolynomial.support_eq_empty`, `eq_zero_iff`, `ne_zero_iff`, `Finsupp.ext_iff'` and
`monomial_le_degreeOf`; no custom-name replacement hit in mathlib source.
[E] **Name search:** actual `lean_local_search` for `MvPolynomial.ext`, `MvPolynomial`,
`kronecker`, `MvPolynomial.support_eq_empty`; verified positive names in source. Index
reported unavailable/error/warming, so an empty indexed result would NOT prove absence.
`kronecker` hits besides Roth concern matrix products.

Auxiliary variants: support/coeff zero criteria, `_eq_zero_iff`, `_of_degreeOf`, `_injective`,
`aeval_eq_zero`; generic `map_eq_zero_iff` requires global injectivity, false for ≥2 variables.
Common-equivalents table: no topology/finiteness/separation bucket applies.
Conclusion: partial matches provide support/coeff infrastructure; keep the bounded custom
Kronecker result and use those APIs directly. No assertion of exhaustive semantic absence.
Actual live `exact?` failed on whole goal; `apply?` suggested global injectivity of the
substitution, which the degree-bound theorem intentionally avoids. No new API-gap helper.

## Generalisation status

| Parameter | Class | Use / candidates | Evidence and result |
|---|---|---|---|
| `{K : Type*}` | type variable | coefficient ring; drop/universe | Already arbitrary universe; removing K leaves polynomial coefficient type unbound. |
| `[Field K]` | typeclass | `kronecker`, `coeff_kronecker`; drop, DivisionRing, CommRing/CommSemiring | Preserved definitions themselves explicitly require Field. Isolated DivisionRing/CommRing probes test this interface dependency; this does not assert field axioms are mathematically necessary. Generalizing the underlying API has no current need and is closed under the preservation scope. |
| `{σ : Type*}` | type variable | variable domain; drop/universe | Already arbitrary universe; `MvPolynomial σ K` and degree quantifier require it. |
| `[Fintype σ]` | typeclass | chosen enumeration in `kronecker`; drop/Finite | `kronecker` type requires a concrete Fintype, whose `equivFin` fixes exponents. Finite-only probe tests this interface; replacing the chosen enumeration requires definition/API changes outside scope. |
| `{k : ℕ}` | structure value | radix/degree bound; drop/concrete→abstract | k occurs in both substitution and hP; no removable unused argument. Natural powers/digits are the construction, not merely an abstract ordered index. |
| `(hk : 1 < k)` | proposition | coefficient preservation; drop/strict→weak `1 ≤ k` | Isolated drop/weak probes fail at `coeff_kronecker` input. This establishes dependency of the chosen proof only, NOT necessity of hk. In fact k≤1 forces supported exponents zero (or an empty variable type when k=0); the theorem can extend to these constant cases. No present consumer needs them; optional extension closed with public API preserved, no pending task. |
| `{P : MvPolynomial σ K}` | structure value | substituted polynomial; drop | Statement depends on P; general polynomial already arbitrary. |
| `(hP : ∀ j, degreeOf j P < k)` | proposition | bounds every supported exponent; drop/point-local/strict→weak `≤ k` | Actual weak-bound probe rejects `coeff_kronecker` input. Independently, with two variables a,b and chosen enumeration e(a)=0,e(b)=1, P=X_b−X_a^k is nonzero but maps to t^k−t^k=0; its degrees are ≤k, so both dropping and replacing `<k` by `≤k` are false for k≥2. Every variable matters. Support-local bounds are equivalent via `monomial_le_degreeOf` and finite sup, not a material weakening. |

No decidability parameter. No point-local analytic predicates. No unbundling candidate.
Inversion check: proof uses the special coefficient-preservation lemma and the degree bound;
abstract zero-reflection from injectivity is already generic mathlib API, but global injectivity
is false. No useful new abstract declaration required.
Big-change candidates: none retained; optional ring/radix broadening is explicitly closed under
preserved-API scope, without speculative follow-up or claim of semantic necessity.

## Literature search

Actual web query: `Kronecker substitution injectivity bounded individual degree generalization`.
Top three returned relevant hits captured:
1. Arpita Korwar, §2.3.2 Kronecker substitution,
   https://www.iitgoa.ac.in/~arpita/articles/PITAndLowerBoundsForSumABPs.pdf — bounded individual
   degrees prevent exponent collisions; modular variants separate prescribed monomial pairs.
2. https://image.informatik.htw-aalen.de/~thierauf/Papers/SOS.pdf — linear extension and inverse
   of bounded-degree Kronecker encoding; degree bound from radix representation.
3. https://www.cecm.sfu.ca/~monaganm/papers/MarshCASC2016.pdf — polynomial multiplication via
   Kronecker substitution; coefficient/reconstruction setting broader than fields.
These support the finite radix encoding perspective, not a need to change this public theorem.
Local `clean.tex` L246,266–268 explicitly gives radix uniqueness and restriction to individual
exponents <k. ChatGPT mathematical MCP: n/a, no such tool exposed among ALL_TOOLS. No literature
candidate needed for present callers; public API preserved.

## Signature width / inequality artifacts

Actual `#check @Roth.kronecker_eq_zero_iff` with `format.width 100`:
```lean
@kronecker_eq_zero_iff : ∀ {K : Type u_1} [inst : Field K] {σ : Type u_2} [inst_1 : Fintype σ] {k : ℕ},
  1 < k → ∀ {P : MvPolynomial σ K}, (∀ (j : σ), degreeOf j P < k) → ((kronecker k) P = 0 ↔ P = 0)
```

| Sig line | Codepoints | Next complete syntactic token | Arithmetic | Action |
|---|---:|---|---|---|
| 98 | 73 | `(hP : ∀ j, degreeOf j P < k)` (28) | 73+1+28=102 >100 | ok |
| 99 | 66 | no next signature line | n/a, proof follows | ok |

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| — | full signature/hypotheses | no `≥` or `>` | none | none |

Both positive inequalities already orient smaller side left. Final proof longest line 98 chars.

## All 42 golfing rules

1.1 n/a: no by-exact wrapper.
1.2 n/a: no by-rfl wrapper.
1.3 n/a: no rw followed by exact; reverse implication closes directly with rw.
1.4 n/a: existing simpa already terminal.
1.5 n/a: no trailing rfl.
1.6 already anonymous iff constructor; preserved and composed with support criterion.
1.7 applied: support emptiness and finite-set criterion composed directly in refine.
1.8 n/a: no by_contra/push_neg.
1.9 n/a: lambdas bind semantically used variables, not eta wrappers; arrows normalized.
1.10 n/a: zero have bindings.
1.11 applied: introduce supported monomial directly as `fun d hd ↦` in refine.
1.12 n/a: no show.
1.13 n/a: no have projections.
1.14 n/a: only rw already has `[h, map_zero]`.
1.15 n/a: no terminal simp only.
1.16 n/a: no nonterminal bare simp.
1.17 preserved: `.trans_lt`, `.symm`, `.1` standard dot/projection use.
1.18 applied: `<|` composes support-zero criterion without trailing parenthesis.
1.19 n/a: no push_neg.
1.20 n/a: no trivial existential helper.
2.1 tried whole-goal grind; failed on zero reflection. Hint-heavy first attempt timed out,
    bounded/cancelled. No limit increase.
2.2 n/a: final proof contains no grind prefix.
2.3 applied: one terminal simpa consolidates coefficient zero with contradiction.
2.4 n/a: no analytic/function-property goal.
2.5 n/a: no positivity goal.
2.6 n/a: no monotonic inequality goal; existing trans_lt is direct bound composition.
2.7 n/a: no pure Nat/Int arithmetic goal; polynomial equality needs coefficient preservation.
2.8 tried aesop; exhaustive search left forward implication unsolved.
2.9 n/a: no numeral/cast normalization goal.
2.10 n/a: polynomial over arbitrary field, not finite decidable computation.
2.11 n/a: no denominator identity.
2.12 n/a: no ring/ring_nf terminal algebra identity.
2.13 n/a: old branches were inside/outside exponent bounds, not symmetric; removed both.
2.14 n/a: no calc chain.
2.15 n/a: iff directions are different, no shared closing tactic.
3.1 n/a: no erw.
3.2 n/a: no continuity/measurability.
3.3 n/a: no omega.
3.4 n/a: no rcases-with-rfl; original obtain eliminated entirely.
3.5 n/a: attributes/public normal forms preserved; no new reusable rewrite rule.
3.6 n/a: no simp_all only.
3.7 n/a: no heartbeat override.

Step-back reflection: the proof now argues directly on support; no bespoke helper or arbitrary
exponent cases. Whole-goal simp made no progress, grind failed, aesop left forward direction,
exact? failed; apply? suggested insufficient global injectivity. Native multi_attempt on a
multiline tactic left synthetic continuation parse diagnostics at L101; these are probe-only,
not source diagnostics. Independent complete scratch proof and module/LSP certify final result.

## Verification / gates

- `lake build Roth.GenWronskian`, session43456, exit0; log `/private/tmp/d09-module.log`.
- Full native `lean_diagnostic_messages`: success=true, partial=false, timed_out=false,
  failed_dependencies=[], no errors, no sorries, no target warnings.
- Complete warnings: L1 copyright/header too short; L36 unused section Fintype on dependent
  zero theorem; L32 unused Fintype in that theorem type; L230 unused DecidableEq in
  `det_sum_rows`; L248 unused Fintype in existence theorem. All five outside owned range.
- Independent non-self proof `/private/tmp/d09-proof.lean` compiled exit0 before source edit.
  It uses support/coeff lemmas, not `kronecker_eq_zero_iff`. Exact original public type test
  and final axiom check are included in the same isolated verification file.
- Axioms: `[propext, Classical.choice, Quot.sound]` only.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | module session43456 exit0 |
| definition_protected | pass | no definition touched |
| theorem_statement_protected | pass | signature byte-identical; exact original-type probe |
| structure_gate | pass | 4 proof lines, no conjunction, no long branch |
| naming_gate | pass | descriptive snake_case; no forbidden pattern |
| line_packing_gate | pass | both signature lines measured above |
| inequality_orientation_gate | pass | scan has zero reverse inequalities |

Overall: pass. Refactoring needed: none. Renames queued: none. Comments: none in proof;
existing docstring and source reference fully preserved. Audit issues 2, fixed2, deferred0.

## Eleven-step checklist

- [x] Step1 reference docs read.
- [x] Step2 full24-item audit.
- [x] Step2.5 five actual search methods, positive API verification, no empty-index absence claim.
- [x] Step2.6 every inherited/explicit parameter, mechanical candidates, semantic evidence, literature.
- [x] Step2.7 every signature line measured with codepoint arithmetic.
- [x] Step2.8 inequality occurrence scan.
- [x] Step3 all42 rules explicitly considered.
- [x] Step4 holistic proof and generic automation alternatives tried.
- [x] Step5a complete LSP success, all outside warnings identified.
- [x] Step5b all seven gates with actual module exit0.
- [x] Step6a no rename required; no sidecar mutation.

Isolated verification completion: exact-type + independent proof + axiom file session63028
exited0, `/private/tmp/d09-proof.log`. Expected-failure assumption probes all exited1:
`drop_hk` session91277 (`hk` unknown), `weak_hk` session39228 (`1 ≤ k` versus `1 < k`),
`division` session13821 (CommSemiring unavailable), `ring` session9063 (Field-dependent
polynomial type mismatch), `finite` session90414 (Fintype unavailable), `weak_hP` session13179
(≤ bound versus < bound). Sources/logs `/private/tmp/d09-<label>.lean`/`.log`.
These probes concern the preserved construction/proof dependencies; the table separately gives
semantic evidence and explicitly avoids inferring necessity from unchanged-proof failure.
Direct target-only comparison against original baseline: signature byte-equal=true; only six
old proof lines replaced by four new proof lines, zero other declarations in worker diff.
