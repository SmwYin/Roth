# Declaration cleanup: `MvPolynomial.taylor_apply`

Baseline: `3ed5784`, `Roth/Taylor.lean:40–41`. Scope: this declaration and this report only.
The sole source edit replaces the mathematical lambda `=>` by `↦`. The theorem remains
2 lines, with the original `rfl` proof, parameters, visibility, name, and docstring.

## Step 1 — references

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md in full, together with the full
worker contract, lean4 and mathlib-quality skills, naming-conventions.md,
mathlib-quality-principles.md, and the applicable formatting, documentation,
visibility, normal-form, API, and generalisation sections of style-rules.md.

## Full audit

1. **LINT:** no target diagnostic; complete file diagnostics contain only the
   user-preserved copyright-header warning at L1:2.
2. **HAVE SCAN:** none; the proof term is `rfl`.
3. **SET_OPTION:** none in the declaration or diff.
4. **SIMP SQUEEZE:** n/a: no simp call.
5. **NAMING:** `taylor_apply` describes the evaluation of the Taylor translation;
   snake_case theorem name, correct subject namespace, no forbidden abbreviation,
   numerical scheme, `_auxN`, `_ge_`, or `_gt_` pattern. No rename needed.
6. **LINE PACKING:** the complete conclusion does not fit after the parameters;
   measured tables below. No additional signature line needed or removable.
7. **BY PLACEMENT:** n/a: term proof `:= rfl`, no `by`.
8. **FORMAT:** replace ordinary mathematical lambda arrow with `↦`; four-space
   statement continuation, no empty lines within declaration, no haveI/letI.
9. **COMMENTS:** no inline proof comments. Existing one-line docstring preserved byte-for-byte.
10. **DOCSTRING:** present, accurately identifies the evaluation interpretation;
    this definitional lemma requires no additional application caveat.
11. **VISIBILITY:** public defining API of the retained public `taylor`; keep its
    public contract as instructed. It is an unfolding rule, not an internal proof helper.
12. **STRUCTURE:** single proof term; no conjunction, cases, branches, or extraction needed.
13. **MATHLIB:** five-method status below; generic evaluation and univariate Taylor
    are partial matches, not replacements for this project definition's API.
14. **JUNK DEF:** n/a: theorem, not a definition.
15. **EXISTS LEMMA:** n/a: no existential conclusion.
16. **SHOW vs CHANGE:** n/a: neither occurs.
17. **PUSH_NEG:** n/a: none.
18. **GENERALISE:** every parameter assessed below; all retained.
19. **INEQUALITY:** zero inequalities; explicit scan below.
20. **NORMAL-FORM:** already an applied unfolding equation, from named translation
    to standard `aeval`; no new simp normal form introduced.
21. **SYNTAX-GEN:** OK: explicit translation vector and polynomial suit pointwise
    rewriting; an unapplied companion would add API without current need.
22. **IMPORT-FANOUT:** n/a: no imports changed.
23. **CASTS:** 0 dropped / 0 kept as cross-type / 0 kept as load-bearing;
    no coercion or expression ascription in the diff.
24. **INSTANCE-NAME:** n/a: theorem, no new instance.

Issues found: one ordinary lambda arrow; fixed. Refactoring needed: none.

## Mathlib search status

| Method | Query / evidence | Result |
|---|---|---|
| A Lean-Finder | Multivariate polynomial Taylor translation by constants equals algebra evaluation at X plus constants | `Polynomial.taylor_apply`, `Polynomial.taylor_eval`, `Polynomial.taylorAlgHom_apply`; univariate analogues only |
| B Loogle | `MvPolynomial.aeval` | `MvPolynomial.aeval`, `aevalTower_id`, `aevalTower_ofId`; generic evaluation, no local translation name |
| C LeanSearch | Same translation/evaluation concept | unavailable: parent's established HTTP 500 service failure; instruction was to record once and not repeatedly retry; no absence inference |
| D Source | untruncated `taylor_apply`, `taylor.*aeval`, `aeval.*taylor`, `def aeval`, `aeval_def`, `aeval_eq_eval₂Hom` in mathlib and Roth | local theorem, univariate Taylor file, and multivariate Eval.lean definitions |
| E Local names | `taylor_apply` | positive source matches for project theorem and `Polynomial.taylor_apply`; index unavailable, so no negative inference |

Auxiliary variants: `taylorAlgHom_apply`, `taylor_eval`, `aeval_def`,
`aeval_eq_eval₂Hom`, `aevalTower_id`, `aevalTower_ofId`.
Common-equivalents table: no applicable discrete/finiteness/separation/bornology bucket.
`#check` confirms `MvPolynomial.aeval_def` and, with its own import,
`Polynomial.taylor_apply`; the latter is not imported by `Roth.Taylor` itself.
An initial scratch check without that extra import correctly failed with unknown
constant; adding `Mathlib.Algebra.Polynomial.Taylor` in scratch verified the candidate.
No project import was added.

Conclusion: partial matches, retain the local applied equation as the public API of
`taylor`. This is an intentional definitional unfolding rule, not a wrapper around
an unrelated mathlib theorem. No claim of exhaustive global absence is made.
Compiled probes in a namespace with a fresh `taylorProbe` definition and only the
original prerequisite imports avoid using the target as its own proof. `exact?` and
`apply?` both suggest `AlgHom.congr_arg (taylorProbe α) rfl`; `rfl` is more direct.

## Generalisation status

| Parameter | Class | Used as | Mechanical candidates / drop assessment | Verified? | Result |
|---|---|---|---|---|---|
| `{σ : Type*}` | type-variable | variable index in α, P, X | universe polymorphism already present; dropping leaves the index type unbound, not an assumption weakening | type checked | retain |
| `{R : Type*}` | type-variable | coefficient type in all expressions | universe polymorphism already present independently of σ; dropping leaves coefficient type unbound | type checked | retain |
| `[CommSemiring R]` | typeclass | prerequisite of MvPolynomial, taylor and aeval | drop; weaken to `[Semiring R]` | compiled scratch tests | both fail to synthesize `CommSemiring R`; retain |
| `(α : σ → R)` | structure-value | translation vector on both sides | drop under autoImplicit=false; point localisation/strict weakening do not apply to data | compiled scratch | unknown identifier α; retain |
| `(P : MvPolynomial σ R)` | structure-value | polynomial evaluated on both sides | drop under autoImplicit=false; no proposition or bundled property to weaken | compiled scratch | unknown identifier P; retain |

The invalid P-drop scratch also reached the default heartbeat limit while recovering
from its unbound identifier; no limits were raised and no failing candidate touched
live source. Algebra typeclass parent tests fail already in the statement, so further
weaker ancestors cannot supply the required CommSemiring instance. There are no
proposition, decidability, pointwise/global, or strict inequality hypotheses.

Inversion check: n/a for extraction. This is exactly the definitional application
rule of the public translation operator; its abstract content is reflexivity, not
an omitted reusable theorem. Big-change candidates: none warranted. No additional
API, parameter order change, or public contract change is proposed.

## Literature search status

A. WebSearch queries and top three hits:

- `multivariate polynomial translation generalization commutative semiring algebra evaluation`:
  [Carleson Eval docs](https://florisvandoorn.com/carleson/docs/Mathlib/Algebra/MvPolynomial/Eval.html),
  [PFR Eval docs](https://teorth.github.io/pfr/docs/Mathlib/Algebra/MvPolynomial/Eval.html),
  [Analysis Eval docs](https://teorth.github.io/analysis/docs/Mathlib/Algebra/MvPolynomial/Eval.html).
- `multivariate polynomial evaluation commutative semiring site:leanprover-community.github.io`:
  [official Eval documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/MvPolynomial/Eval.html),
  [official historical Basic documentation](https://leanprover-community.github.io/mathlib_docs/data/mv_polynomial/basic.html),
  [Mathematics in Lean](https://leanprover-community.github.io/mathematics_in_lean/mathematics_in_lean.pdf).
- `polynomial algebra universal property generalization site:stacks.math.columbia.edu`:
  [Fundamental Groups](https://stacks.math.columbia.edu/download/pione.pdf),
  [Artin's Axioms](https://stacks.math.columbia.edu/download/artin.pdf),
  [Divided Power Algebra](https://stacks.math.columbia.edu/download/dpa.pdf).

The official Eval documentation supports evaluation for arbitrary variable types over
commutative semirings, already the scope here. Stacks hits concern general universal
properties or divided powers and do not supply a weaker statement of this definitional
rule. No literature-driven contract change is warranted.
B. ChatGPT math MCP: n/a, no such tool is available in this session's tool inventory.

## Line packing

Actual `#check @taylor_apply` with `format.width 100`:

```lean
@taylor_apply : ∀ {σ : Type u_1} {R : Type u_2} [inst : CommSemiring R] (α : σ → R) (P : MvPolynomial σ R),
  (taylor α) P = (aeval fun j ↦ X j + C (α j)) P
```

The semantic next signature unit is the complete conclusion expression; splitting
inside the evaluation application would fragment the mathematical statement. Widths
are Unicode codepoints. The `:= rfl` boundary is included in physical line width.

| Stage / line | Chars | Next signature unit | Arithmetic | Action |
|---|---:|---|---|---|
| Before L40 | 57 | conclusion without `:= rfl`, 45 chars | 57 + 1 + 45 = 103 > 100 | ok |
| Before L41 | 56 | none, term proof ends this line | n/a | ok |
| After L40 | 57 | conclusion without `:= rfl`, 44 chars | 57 + 1 + 44 = 102 > 100 | ok |
| After L41 | 55 | none, term proof ends this line | n/a | ok |

Entire final declaration flattened including `:= rfl` is 109 codepoints.

## Inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| — | all signature and parameters L40–41 | n/a: no ≥ or > inequality | none | none |

The original ASCII lambda arrow is syntax, not an inequality; it was changed to ↦.

## Golfing rule pass

| Rule | Status |
|---|---|
| 1.1 by exact | n/a: no tactic wrapper |
| 1.2 by rfl | already `:= rfl` |
| 1.3 rw + exact | n/a: no rw |
| 1.4 simp + exact | n/a: no simp |
| 1.5 trailing rfl | n/a: rfl is the complete proof, not a redundant final tactic |
| 1.6 constructor | n/a: equality, no constructor sequence |
| 1.7 apply + exact | n/a: no tactics |
| 1.8 by_contra | n/a: no negation proof |
| 1.9 eta reduction | n/a: j occurs in both X j and α j; lambda is not an eta wrapper |
| 1.10 single-use have | n/a: no have |
| 1.11 apply + intro | n/a: no tactics |
| 1.12 show | n/a: absent |
| 1.13 projections | n/a: absent |
| 1.14 merge rw | n/a: absent |
| 1.15 terminal simp only | n/a: absent |
| 1.16 nonterminal simp | n/a: absent |
| 1.17 dot notation | n/a: no applied named proof lemma |
| 1.18 parens / <\| | n/a: lambda parentheses are required since aeval has a following P argument |
| 1.19 push_neg | n/a: absent |
| 1.20 existential helper | n/a: public equality API |
| 2.1 grind | tried in isolated pre-target environment; fails to prove the definitional equation without unfolding |
| 2.2 pre-grind tactics | n/a: no grind in retained proof |
| 2.3 simpa consolidation | n/a: no simp sequence; rfl is shorter than by simpa [taylor] |
| 2.4 fun_prop | n/a: no analytic function property |
| 2.5 positivity | n/a: equality, not sign goal |
| 2.6 gcongr | n/a: no inequality |
| 2.7 lia / omega | n/a: no integer arithmetic |
| 2.8 aesop | isolated probe elaborated without error; longer than rfl, not adopted |
| 2.9 norm_num / norm_cast | n/a: no numeric computation or cast |
| 2.10 decide | n/a: symbolic equality over arbitrary semiring, not finite computation |
| 2.11 field_simp; ring | n/a: no denominators or ring structure |
| 2.12 linear_combination | n/a: no ring/ring_nf proof or algebraic hypotheses |
| 2.13 wlog | n/a: no cases |
| 2.14 calc | n/a: no calculation chain |
| 2.15 multi-goal | n/a: one equality proof term |
| 3.1 erw | n/a: absent |
| 3.2 continuity | n/a: absent |
| 3.3 omega to lia | n/a: absent |
| 3.4 rcases rfl | n/a: absent |
| 3.5 attributes | retain ordinary unfolding theorem; no new simp/grind attribute warranted |
| 3.6 simp_all | n/a: absent |
| 3.7 limits | n/a: no source limits |

## Step back and verification

`rfl` is already the shortest direct proof of this definitional equality. The
fresh-definition exact?/apply? probes find a longer generic congruence expression;
there is no proof chain, have block, or hidden computational work to simplify.
The final independent proof and original-type ascription compile. No tactic
replacement or new lemma is needed.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | `lake build Roth.Taylor` exit 0, target 13s, 1439 jobs; `/private/tmp/roth-taylor-apply-build.log` |
| definition_protected | pass | no definition or abbrev changed |
| theorem_statement_protected | pass | only synonymous lambda token; original full type accepted by Lean ascription |
| structure_gate | pass | single rfl term, no conjunction/branch |
| naming_gate | pass | descriptive taylor_apply; no forbidden pattern |
| line_packing_gate | pass | complete two-line width table, conclusion does not fit preceding line |
| inequality_orientation_gate | pass | no inequalities in declaration |
| LSP | pass | complete success=true, partial=false, timed_out=false; only preserved header warning |
| isolated proof | pass | rfl rechecked separately with same parameters and conclusion |
| axiom check | pass | only propext, Classical.choice, Quot.sound |

Native final isolated check succeeded but noted stale imports after the concurrent
module build; a fresh CLI process repeats the proof/type/axiom checks against the
rebuilt module. Parent owns full-project and separate LeanEval dependent build gates.

## Result

Before 2 lines; after 2 lines; saved 0. One style issue found and fixed. No
refactoring, rename, or API change. Inline comments: none present; docstring preserved.
Applied: ordinary lambda notation rule. Proof-golf rules had no beneficial source change.

Source frozen SHA256: `b09b1665ded220e46380fb7174a024f0f5d12144caafdb60a25f107d0488f56a`.
Source ownership returned to parent; report-only work after freeze.

- [x] Step 1 references read
- [x] Step 2 full 24-item audit
- [x] Step 2.5 five-method search status
- [x] Step 2.6 generalisation and literature status
- [x] Step 2.7 per-line width table
- [x] Step 2.8 inequality table
- [x] Step 3 all 42 golfing rules
- [x] Step 4 strategic reflection
- [x] Step 5a complete LSP diagnostics
- [x] Step 5b gates
- [x] Step 6a no renames required

Fresh CLI closure: `lake env lean /private/tmp/roth-taylor-apply-verify.lean`
exited 0 with only the requested type and axiom informational output. Both the
independent `rfl` example and the original `=>` spelling ascribed to `taylor_apply`
passed. This supersedes the stale-import informational note from native scratch.
