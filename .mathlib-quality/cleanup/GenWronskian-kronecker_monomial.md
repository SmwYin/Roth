# Phase 4 — Roth.kronecker_monomial

Dedicated target: `Roth/GenWronskian.lean`, original/current signature L55–56;
original declaration L55–60, final L55–58. Only its proof body changed.
Initial audit: `.mathlib-quality/cleanup/GenWronskian.md`.
Full project and separate LeanEval baseline inherited from the file owner; no Git operations,
full builds, shared logs, LeanEval builds, other declarations, or new helpers touched by this worker.

## Step 1 — references

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md in the installed mathlib-quality skill.
Also read both installed SKILL.md files, the full worker contract, naming-conventions.md,
mathlib-review-stages.md, and relevant formatting/documentation/lambda/theorem/normal-form/
generalisation/cast sections of style-rules.md. Source clean.tex §2 L223–270 was checked.

## Step 2 — 24-item audit

| # | Item | Finding/action |
|---|---|---|
| 1 | LINT | No warning in target; complete final diagnostics contain five existing outside warnings. |
| 2 | HAVE SCAN | No `have` in original or final proof; no occurrence/use-count rows needed. |
| 3 | SET_OPTION | None in target, none introduced. |
| 4 | SIMP SQUEEZE | Original has no simp; final single terminal `simp [...]` stays unsqueezed. |
| 5 | NAMING | `kronecker_monomial` names the operation and input constructor, snake_case; no forbidden patterns or abbreviations. |
| 6 | LINE PACKING | Both signature lines measured below; no signature edit needed. |
| 7 | BY PLACEMENT | `:= by` terminates L56. |
| 8 | FORMAT | Two-space proof indent and four-space signature continuation; no empty proof lines or trailing whitespace. Two original ordinary `=>` lambdas disappear with congruence boilerplate. |
| 9 | COMMENTS | No inline proof comments; existing docstring preserved byte-for-byte. |
| 10 | DOCSTRING | Existing one-sentence public doc identifies the substituted monomial and exponent; preserved under explicit API/docs protection. |
| 11 | VISIBILITY | Existing public computation API retained as requested; useful rewrite in downstream coefficient argument. |
| 12 | STRUCTURE | Final proof is two physical lines, one tactic; no conjunction or branches. No helper needed. |
| 13 | MATHLIB | Partial general match `MvPolynomial.aeval_monomial`; full search/probes below. |
| 14 | JUNK DEF | n/a: theorem, no definitions added. |
| 15 | EXISTS LEMMA | n/a: equality, no existential witness lemma. |
| 16 | SHOW vs CHANGE | n/a: no `show` or `change`. |
| 17 | PUSH_NEG | n/a: no negation manipulation. |
| 18 | GENERALISE | Every actual parameter audited below; preceding public definition constraints block inline coefficient weakening. |
| 19 | INEQUALITY | Zero reversed inequalities in signature/hypotheses; scan below. |
| 20 | NORMAL-FORM | RHS is coefficient times one power of X, matching `Polynomial.coeff_C_mul_X_pow`; canonical computation form. |
| 21 | SYNTAX-GEN | OK: direct equality rewrites the precise `kronecker`/`monomial` expression used downstream. |
| 22 | IMPORT-FANOUT | n/a: no imports changed/added. |
| 23 | CASTS | Diff contains no coercions or type ascriptions: 0 dropped / 0 cross-type kept / 0 load-bearing kept. |
| 24 | INSTANCE-NAME | n/a: theorem, no instance declarations. |

Issues found: (1) explicit finite-product congruence can consolidate into terminal simplification;
(2) two ordinary lambda arrows occur in the resulting redundant proof code. Both fixed.
Refactoring needed: none. The existing meaningful public API is protected; no speculative
cross-definition generalisation ticket is opened.

## Step 2.5 — mathlib search status

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | “Evaluating a multivariate polynomial monomial at powers of X gives coefficient times X to a sum of exponents” | Tool invoked; read operation timed out. No absence conclusion inferred. |
| B Loogle | `MvPolynomial.aeval, MvPolynomial.monomial` | `MvPolynomial.aeval_monomial`, plus `Algebra.Generators.ofComp_toAlgHom_monomial_sumElim`. |
| C LeanSearch | “aeval monomial multivariate polynomial product powers” | `MvPolynomial.aeval_monomial`, `eval₂_mul_monomial`, `eval_monomial`. |
| D source grep | `aeval_monomial`, `prod_pow_eq_pow_sum`, `prod_fintype`, `eval₂_monomial`, `eval₂_prod` | Eval.lean L92/L240/L681; Finsupp/Basic.lean L63; Finset/Basic.lean L656. Full-name/topic `kronecker_monomial\|kroneckerExp\|kronecker` search over both polynomial directories yielded no matches, without truncation. |
| E name pattern | `lean_local_search aeval_monomial` | Source-backed hits for MvPolynomial and Polynomial variants; index reported `warming`, which is not absence evidence. |

Auxiliary variants checked: eval₂_monomial, eval₂_mul_monomial, eval_monomial,
eval₂_prod, product of powers, Finsupp product over a finite type. Relevant signatures
were compiled by `#check` in `/private/tmp/kronecker-monomial-final-check.lean`.
Common-equivalents lookup: no match (this is polynomial substitution, not topology/finiteness).

Conclusion: partial match, keep the existing public computation lemma and build directly on
`aeval_monomial`, `Finsupp.prod_fintype`, and `Finset.prod_pow_eq_pow_sum`. The latter two require
exponent normalization with `pow_mul`/`mul_comm`; this gives the requested named Kronecker API.
This is not a claim that mathlib has no generic monomial API: it has that API, and we use it.
No new wrapper/helper or custom predicate was introduced, no equivalent mathlib declaration
was found, and protected existing public content/docs are retained. Thus the six strict rules
are addressed without deleting the requested API. No module-docstring rewrite is authorized.

Generic-route attempts used a fresh scratch namespace with copied substitution/exponent
*definitions only*, importing the original dependencies rather than this theorem's module.
`fail_if_success grind` and `fail_if_success aesop` compiled successfully, establishing neither
closes the goal; the final `simp` closes it. `exact?`/`apply?` were actually attempted; see
their separate CLI logs `/private/tmp/kronecker-monomial-exact.log` and
`/private/tmp/kronecker-monomial-apply.log`: each reached the default 200000-heartbeat bound
in `whnf`, without a usable closing term. No limits were raised and no self-reproof was used
in these searches. The successful grind/aesop rejection probes each exited 0 in separate files.
Native multi-attempt stalled and was cancelled; the direct MCP fallback timed out after 65s,
so scratch CLI tests supplied the usable evidence instead.

## Step 2.6 — generalisation

| # | Parameter | Class | Use | Mechanical candidates / verification | Result |
|---|---|---|---|---|---|
| 1 | `{K : Type*}` | type variable | Coefficient and polynomial ring | Already universe polymorphic; dropping K makes coefficient types unbound. No point-local/strict weakening applies to a type. | Keep. |
| 2 | `[Field K]` | typeclass | Required by existing `kronecker` declaration | Drop/CommSemiring/CommRing/DivisionRing checked against unchanged public definitions in scratch; no Field instance can be synthesized. | Keep; theorem-only weakening cannot elaborate. |
| 3 | `{σ : Type*}` | type variable | Variables/exponent-vector domain | Already independent universe; dropping σ makes d's domain unbound. No order/point-local hypothesis. | Keep. |
| 4 | `[Fintype σ]` | typeclass/data | Chosen enumeration `Fintype.equivFin σ` inside kronecker/kroneckerExp | Drop and replacement by `Finite` checked in scratch; `Fintype σ` fails synthesis. | Keep; no unused instance in target. |
| 5 | `(k : ℕ)` | structure value | Natural base/exponent | Unrestricted value, no bound to weaken. Dropping binder leaves k unbound; abstraction of ℕ would change polynomial exponent semantics. | Keep. |
| 6 | `(d : σ →₀ ℕ)` | structure value | Monomial exponent vector | No support/degree bound to weaken; dropping leaves d unbound. Finsupp is already the finite-support exponent representation. | Keep. |
| 7 | `(a : K)` | structure value | Arbitrary coefficient | No nonzero/unit restriction; dropping leaves a unbound. Type follows K. | Keep. |

The surrounding `{l : ℕ}` is not included in the exported theorem: compiled `#check @...`
confirms exactly the seven rows above. No propositional, decidability, topology, strict,
point-local or bundled-injectivity hypotheses are present. No SMALL weakening was applied.
Coefficient-only parent tests are expected failures and leave the source unchanged.
The actual four-candidate compiler failure log is `/private/tmp/kronecker-monomial-weaken.log`;
its errors occur in statement elaboration at the protected definitions, before proof tactics.
Additional drop-Field and Finite-only checks also fail precisely at required instance synthesis
in `/private/tmp/kronecker-monomial-drops.log` (L30 and L34); both expected-negative probes exit 1.
The field structure itself is stronger than the abstract computation needs, but broadening
preceding protected definitions is outside this target and unnecessary for the current API;
that optional extension is closed, with no pending work.

Inversion check: after unfolding `kronecker`/`kroneckerExp`, the mathematical content is exactly
general evaluation of a monomial plus aggregation of powers. The general evaluation is
already `MvPolynomial.aeval_monomial`; no abstract clone is needed. The special geometric
weights are exactly the chosen Kronecker substitution's API.

### Literature status

Web query: “Kronecker substitution monomial exponent sum polynomial generalization”. Top three
returned hits (captured, with no unsupported inference of missing hypotheses):

1. [UC Berkeley dissertation](https://escholarship.org/content/qt92n4z7j2/qt92n4z7j2.pdf): monomial exponents encoded as univariate exponents.
2. [Marsh/Monagan, Kronecker substitution](https://www.cecm.sfu.ca/~monaganm/papers/MarshCASC2016.pdf): polynomial Kronecker substitution in symbolic computation.
3. [PIT and lower bounds notes, §2.3.2](https://www.iitgoa.ac.in/~arpita/articles/PITAndLowerBoundsForSumABPs.pdf): explicitly maps a monomial to y raised to the weighted exponent sum.

The third source directly supports this monomial identity. The local source clean.tex §2
L231–243 has the same substitution and exponent sum. The identity needs no lower bound on k
or exponent bound on d; those restrictions enter subsequent injectivity, not this theorem.
ChatGPT math MCP: n/a, no matching callable tool exposed in ALL_TOOLS. Literature-driven
big-change candidates: none required for the protected API.

## Steps 2.7 and 2.8 — hard-gate artifacts

`set_option format.width 100 in #check @kronecker_monomial` was run in the final scratch check:

```lean
@kronecker_monomial : ∀ {K : Type u_1} [inst : Field K] {σ : Type u_2} [inst_1 : Fintype σ] (k : ℕ) (d : σ →₀ ℕ)
  (a : K), (kronecker k) ((monomial d) a) = Polynomial.C a * Polynomial.X ^ kroneckerExp k d
```

The declaration signature itself is byte-identical. Widths below are Unicode codepoints.
The next signature unit is the complete equality conclusion (not a word fragment).

| Sig line | Chars | Next token/unit | Arithmetic | Action |
|---|---:|---|---|---|
| 55 | 57 | equality conclusion through `:= by` (83 chars) | 57 + 1 + 83 = 141 > 100 | ok |
| 56 | 87 | no next signature line | n/a, proof body next | ok |

| # | Location | Original | Rewrite | Lemma rename? |
|---|---|---|---|---|
| — | Full signature/hypotheses | No ≥ or > | n/a | No `_ge_`/`_gt_` in name |

## Step 3 — all 42 golfing rules

| Rule | Status |
|---|---|
| 1.1 by exact | n/a: no by-exact wrapper. |
| 1.2 by rfl | n/a: not reflexive by definitional reduction. |
| 1.3 rw + exact | Superseded: entire rw/congr/exact chain replaced by simp. |
| 1.4 simp + exact | n/a: original has no simp/exact chain. |
| 1.5 trailing rfl | n/a: none. |
| 1.6 constructors | n/a: equality, no constructor chain. |
| 1.7 apply + exact | n/a: none. |
| 1.8 by_contra | n/a: none. |
| 1.9 eta reduction | Two original lambdas do genuine work; direct simp eliminates both rather than eta-reducing. |
| 1.10 inline have | n/a: no have. |
| 1.11 apply + intro | n/a: none. |
| 1.12 redundant show | n/a: none. |
| 1.13 have projections | n/a: none. |
| 1.14 merge rw | n/a: original outer and inner rw have intervening congruence, not sequential calls; both eliminated. |
| 1.15 terminal simp only | n/a: no simp only; final simp unsqueezed. |
| 1.16 nonterminal simp | n/a: no nonterminal simp. |
| 1.17 dot notation | n/a: final proof has no explicit method application. |
| 1.18 `<\|` | n/a: no dollar/trailing application parentheses to remove. |
| 1.19 push Not | n/a: no push_neg. |
| 1.20 trivial exists | n/a: no exists lemma. |
| 2.1 grind | Actually tried, does not close fresh definition-only scratch goal. |
| 2.2 delete pre-grind | n/a: no retained grind. |
| 2.3 simpa consolidation | Applied more directly as a single terminal simp; explicit product congruence removed. |
| 2.4 fun_prop | n/a: polynomial equality, no analytic function property. |
| 2.5 positivity | n/a: no positivity/nonzero goal. |
| 2.6 gcongr | n/a: no inequality/monotonicity goal. |
| 2.7 lia/omega | n/a: no linear arithmetic proposition; exponent identity is power/product aggregation. |
| 2.8 aesop | Actually tried, does not close fresh definition-only scratch goal. |
| 2.9 norm_num/norm_cast | n/a: no numeric constants/cast computation to normalize. |
| 2.10 decide | n/a: equality of arbitrary polynomials over arbitrary Field, not finite computation. |
| 2.11 field_simp/ring | n/a: no denominators; variable finite product aggregation is handled by named API. |
| 2.12 linear_combination | n/a: no ring-ending proof or algebraic hypotheses. |
| 2.13 wlog | n/a: no symmetric branches. |
| 2.14 calc term mode | n/a: no calc; raw composed congruence would be longer than simp. |
| 2.15 `<;>` | n/a: single closing tactic, no repeated goals. |
| 3.1 erw | n/a: none. |
| 3.2 legacy function tactics | n/a: none. |
| 3.3 omega to lia | n/a: neither needed/present. |
| 3.4 rcases rfl | n/a: no destructuring. |
| 3.5 automation attributes | No attribute change: public API attributes protected; local simp hints suffice. |
| 3.6 simp_all | n/a: no hypotheses to simplify globally; terminal simp suffices. |
| 3.7 heartbeat option | n/a: none in source, none raised. |

## Step 4 — reflection

The whole proof is now one tactic. General monomial evaluation and product-power expansion
already provide every component; a separate helper would duplicate that API. No have blocks,
redundant goal changes, casts, or branches remain. The direct simplifier proof is clearer than
manual congruence because it states precisely the normalization rules needed.

## Step 5 — verification

- `/Users/ramin/.elan/bin/lake build Roth.GenWronskian`: exit 0, target built in 17s.
  Log `/private/tmp/kronecker-monomial-build.log`.
- Complete direct MCP `lean_diagnostic_messages`: success=true, partial=false,
  timed_out=false, failed_dependencies=[], zero errors; artifact
  `/private/tmp/kronecker-monomial-lsp.json`.
- All five file warnings are outside the target and unchanged: L1 missing metadata,
  L36 and L32 dependent-zero unused Fintype, L239 det_sum_rows unused DecidableEq,
  L257 existence unused Fintype. Dependency replay header warnings also pre-exist.
- `/private/tmp/kronecker-monomial-final-check.lean` freshly compiled, exit 0: exact original
  universally quantified type accepted via the exported theorem; independently named reproof
  uses the original rw/congruence argument and never calls kronecker_monomial.
- Both theorem and independent reproof have only `[propext, Classical.choice, Quot.sound]`.
  Log `/private/tmp/kronecker-monomial-final-check.log`.
- Initial successful scratch `KMProbe` proof used copied definitions and the new simp tactic;
  no reference to the theorem under test. Log `/private/tmp/kronecker-monomial-probe.log`.
- No source sorry/axiom/native_decide/options/version change/new helper. Source context was
  re-read immediately before applying a narrow contextual patch.
- A Python snapshot diff independently asserted all text outside the target byte-identical,
  the complete signature byte-identical, and zero reversed inequalities in its signature.
- Source ownership revoked after reporting frozen SHA256
  `8145a47137b5aec96742b4f5a429393b77e00e345799fda13fd6d658bbb704cb`; subsequent work report-only
  or scratch outside repo. File owner handles full/separate cumulative gates.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | ✓ pass | Actual module build exit 0 above. |
| definition_protected | ✓ pass | Snapshot diff changes no definition or abbreviation. |
| theorem_statement_protected | ✓ pass | Both original signature lines byte-identical; exact original type compiled. |
| structure_gate | ✓ pass | Two proof lines, no conjunction/branch. |
| naming_gate | ✓ pass | Descriptive name; forbidden-pattern/abbreviation scan negative. |
| line_packing_gate | ✓ pass | Both signature lines accounted for above; 141-character combined conclusion justifies break. |
| inequality_orientation_gate | ✓ pass | Zero reversed inequality occurrences, table above. |

Overall: pass. Renames queued: none. Comments preserved: no proof comments; one existing
docstring unchanged. Refactoring needed: none.

## Step 6 — result and phase checklist

Before: 6 lines. After: 4 lines. Saved: 2 lines. Audit issues found: 2; fixed: 2;
refactoring deferred: 0. Applied rules: 2.3, with deletion of redundant lambda/congruence code.

- [x] Step 1 — reference docs read.
- [x] Step 2 — full 24-item audit emitted.
- [x] Step 2.5 — actual five-method mathlib search status emitted, failures distinguished.
- [x] Step 2.6 — every parameter generalisation status and public literature search emitted.
- [x] Step 2.7 — per-signature-line width table emitted.
- [x] Step 2.8 — per-occurrence inequality scan table emitted.
- [x] Step 3 — all 42 rules have a concrete status/reason.
- [x] Step 4 — alternate strategy/automation/general API reflection complete.
- [x] Step 5a — complete diagnostics with all warnings and no errors.
- [x] Step 5b — all required diff gates passed.
- [x] Step 6a — no rename needed, no shared sidecar mutation.
