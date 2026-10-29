# `LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth` — canonical293

Verdict: **YES-but-generalise-first**, reason **MODERN-IDIOM**. The contribution is the full named
Thue–Siegel–Roth theorem, not the length of this final project corollary. Present its primary
mathlib statement using `LiouvilleWith`, and recover the exact benchmark uniform bound.
No parent verdict is inherited; no cost-based downgrade or novelty-by-search-failure is used.

## Phase0 — baseline, reading and scope

Fresh17 source/pin hashes match the tracked shared manifest. The shared baseline passed2467jobs;
accepted file-end builds remain historical evidence. Root owns final literal `lake build` and
`lake build Roth.LeanEval` after all293 assessments and global gates. This package certifies this
assessment, not overall repository completion. Production Lean, pins and Git are unchanged.
The entire declaring LeanEval66 and Main588 were read, including all main endpoints and the
integer reduction, auxiliary-polynomial argument and rational approximation endpoint.

Original re-elaboration copies the exact final target into a fresh namespace; its public
project ingredients remain imported. No private-helper closure is needed and unrelated Main
re-elaboration is not claimed. Root executed every native and local-LSP request. Isolated proofs
use authorized exact19 mathlib imports; normal project diagnostics retain exact disk9. A separate
explicitly authorized PROJECT-CONTEXT run uses disk9 plus LiouvilleWith as a standalone10-import
source; this never mutates the persistent disk header and is not mathlib-only evidence.

[inputs](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/inputs.json), [baseline](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/baseline-build.txt), [Main](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/source-Main.lean.txt), [LeanEval](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/source-LeanEval.lean.txt), [prefix controls](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/prefix-controls.json).

## Phase1 — full statement and proof

```lean
∀ (x : ℝ), Irrational x → IsAlgebraic ℤ x →
  LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine x
```

The conclusion expands to:

```lean
∀ ε : ℝ, 0 < ε → ∃ C : ℝ, 0 < C ∧
  ∀ (p q : ℤ), 0 < q → C / (q : ℝ) ^ ((2 : ℝ) + ε) < |x - (p : ℝ) / (q : ℝ)|
```

For each positive epsilon there is one positive constant, depending on x and epsilon but independent
of numerator and denominator, that bounds every rational approximation error from below at exponent
2+epsilon. The strict inequality is harmless after shrinking the constant, but its positivity and
quantifier order matter. The theorem asserts every positive epsilon, not merely existence of one.

The written proof extends integer algebraicity to rational scalars using injectivity of ℤ→ℚ,
then applies project `Roth.roth`. The equivalence `isDiophantine_iff` converts exclusion of infinitely
many approximants above exponent2 into this uniform positive bound. Its reverse transport uses a
minimum of finitely many positive weighted errors and separates the remaining errors using1/2;
its forward transport absorbs a fixed constant through a strict exponent gap at large denominators.

The underlying Roth theorem is substantive: reduce to an algebraic integer, choose rapidly growing
reduced approximants and balanced degrees, construct a high-index multivariate integer polynomial
with small Hasse derivatives, bound its nonzero value below by clearing denominators, estimate it
above by Taylor expansion, and contradict the logarithmic parameter inequality. None of this is
supplied by an existing scalar-transfer theorem or a generic finite-minimum argument.

The loaded kernel full type, full printed target body, body/type constant inventories and standard
axioms are retained. This target's printer output is complete, without elision. Exact written
proof and fresh native replay are also retained. `Subsingleton.elim` checks equality of proofs of
the same full proposition; it does not assert equality of proof construction histories.

Project dependencies use exact canonical names: statement `IsDiophantine`; lexical body
`LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff` and `Roth.roth`; elaborated body
additionally mentions `Roth.approxSet` and `IsDiophantine`. The private minimum helper belongs to
the transitive equivalence dependency, not a direct dependency of the final written proof.

[original source](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/original-executed.lean.txt), [raw receipt](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/original01-receipt.json), [native type](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/native-type.json), [dependency scopes](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/project-dependencies.json).

## Phase2 — preliminary checks

**BIG**: named theorem and final exact LeanEval endpoint. A short proof invoking another project
Roth endpoint does not make the mathematical statement a trivial mathlib composition.
Definition-only one-line test: n/a, theorem. Infrastructure assessment has six explicit n/a rows
below; the theorem introduces no typeclass, instance, coercion or definitional infrastructure.

## Phase3 — exhaustive literature

| Channel | Exact query | Finding |
|---|---|---|
| General specific | Roth theorem algebraic irrational uniform constant epsilon rational approximation | Standard uniform and finite-exception forms; primary Roth1955 metadata and Roth1958 opening. |
| General wider | Roth theorem irrationality exponent algebraic numbers finite rational solutions 1955 | Irrationality exponent2 and finite rational approximations above2. |
| General aliases | Thue Siegel Roth theorem LiouvilleWith irrationality measure generalizations number fields | Liouville/Roth distinction and number-field/place extensions. |
| nLab | site:ncatlab.org/nlab Roth theorem diophantine approximation | Vojta dictionary gives higher-dimensional context, not a replacement theorem. |
| nCatLab distinct | site:ncatlab.org/ncatlab Roth theorem irrationality | No exact namespace theorem; returned nLab results are not relabelled nCatLab. Quoted Roth retry also performed. |
| Stacks | site:stacks.math.columbia.edu Roth theorem diophantine approximation | No applicable Stacks theorem returned; quoted Roth retry performed, no absence inference. |
| MathOverflow | site:mathoverflow.net Roth theorem irrationality exponent uniform constant | Historical and constant/effectivity discussions, used for discovery and caution. |
| Recent arXiv | site:arxiv.org/abs "Roth" "Diophantine" after:2021-10-29 before:2026-10-30 | Hindes2022 characteristic-p failure; Inami2026 application of Roth-type inequalities. |
| Local references | rg Roth, kappa, irrational, approximation in clean.tex | §6 theorem and integer reduction read; exact local excerpt retained. |
| Optional ask_chatgpt_math | Standard form, generality and historical evolution | Unavailable: optional tool not installed; all other named channels executed. |

Initial recent searches returned much unrelated formalization material; the targeted retry and
primary abstract opens supply the relevant2022/2026 results. Full ICM PDF opening failed400 due
its74MB size; only the returned primary search opening is used. GitHub benchmark page opening
returned cache miss, then its raw canonical URL succeeded. Stacks and nCatLab results do not
establish absence. Web artifacts retain exact requests, response SHA256/bytes/status, clean titles,
URLs/locators and original short summaries; no article or search-result bodies are persisted.

[Roth1955](https://www.cambridge.org/core/journals/mathematika/article/rational-approximations-to-algebraic-numbers/EFB89E2873019B246F004FAA06E05A7F),
Mathematika2(1),1–20, DOI10.1112/S0025579300000644, confirms publication identity and the earlier
degree-dependent Liouville background. [Roth1958 ICM](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf),
opening§1, states that infinitely many exponent-kappa approximations force kappa≤2.
[Canonical LeanEval benchmark](https://raw.githubusercontent.com/leanprover/lean-eval/main/LeanEval/NumberTheory/ThueSiegelRoth.lean),
lines10–19 and27–36, explicitly distinguishes every-epsilon Roth from finite irrationality measure;
its placeholder proof is not imported or used by this project, whose theorem has standard axioms.

[Hindes2022](https://arxiv.org/abs/2209.09182), abstract, explicitly warns that the characteristic-p
analogue fails. [Inami2026](https://arxiv.org/abs/2608.03194), abstract, uses Roth-type inequalities
for algebraic frequency ratios in Strichartz estimates, an application beyond this project.
The [MathOverflow constant question](https://mathoverflow.net/questions/387285/more-about-roths-theorem-bound-for-the-constant-and-multidimensional-case)
separates a positive constant from an effective formula. These community discussions do not replace
primary theorem evidence. Higher-dimensional, place and moving-target variants require different
height/valuation machinery; no mechanical arbitrary-field generalization is claimed.

Standard form: every irrational algebraic real has all-epsilon uniform bounds, equivalently finite
exceptions above every exponent2, equivalently exponent≤2. Classical real generality agrees with
the target. Variants in constant choice, strictness and denominator representation are equivalent
through the actually compiled bridges; arbitrary fields or a fixed epsilon0 are different claims.

[literature](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/literature.json), [web0](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/web-batch0.json), [web1](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/web-batch1.json), [web2](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/web-batch2.json), [web3](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/web-batch3.json), [web4](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/web-batch4.json), [local](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/local-source-section6.tex.txt).

## Phase4a–b — generality and verified alternatives

| Parameter or assumption | Analysis and native evidence |
|---|---|
| x : ℝ | Real rational approximation is the intended object. No arbitrary ordered-field weakening verified. |
| Irrational x | Necessary for the uniform statement: every rational r admits exact r.num/r.den, making a positive lower bound impossible. Generality02 proves this for all rationals and0. |
| IsAlgebraic ℤ x | Equivalent to IsAlgebraic ℚ x by existing IsFractionRing.isAlgebraic_iff; not a strict weakening. Generality02 proves both the equivalence and final theorem overℚ. |
| Algebraicity altogether | Liouville x implies irrationality, nonalgebraicity and failure of IsDiophantine, compiled in projectmodern01. This is a conditional Liouville-family counterexample, not a separately constructed numerical witness. |
| Every ε>0 | Essential Roth strength; replacing it by some epsilon is the weaker degree-dependent Liouville property. |
| Positive C independent of p,q | Essential uniformity. Constant depends on x,epsilon; no effective computation or global x-independent constant claimed. |
| Positive integer q | Correct domain; lifting toℕ and reducing rationals are representation bridges, not arbitrary signed-denominator removal. |
| Strict error inequality | Equivalent weak formulation compiled using half the positive constant; finite exceptions compiled from actual Roth. |
| Threshold2 | Substantive sharp Roth constant. Generic t bridge and monotonicity compile, but do not prove arbitrary algebraic cutoff t. |

Classical generality: **MAXIMALLY GENERAL** within this real uniform formulation. No original
hypothesis is casually dropped. The equivalent ℚ algebraicity spelling is a syntactic improvement.
The semantic modernisation changes the primary interface to the existing frequent exponent API:

```lean
∀ {x p : ℝ}, IsAlgebraic ℚ x → 2 < p → ¬ LiouvilleWith p x
```

This exact theorem is compiled as `Endpoint293Modern.algebraic_not_liouville`. At p>2,
`LiouvilleWith.irrational` supplies irrationality; no irrational binder is required there.
The equivalent all-exponent bound accommodates rationals precisely because LiouvilleWith excludes
exact equality. It must not be identified with uniform bounds at all real x without a conjunct:

```lean
UniformBound t x ↔ Irrational x ∧ ∀ {p : ℝ}, LiouvilleWith p x → p ≤ t
```

The full generic equivalence, all-real pair iff and rational false-generalization guard are freshly
compiled in isolated modern01. The proof is adapted from accepted292 generic transport, which
itself credits accepted290/288. It is authored proof using mathlib building blocks, not an
existing mathlib theorem. No earlier verdict is inherited. In PROJECT-CONTEXT projectmodern01,
actual `Roth.roth` yields the Liouville family, and that family recovers the entire original
uniform signature with its original irrational and integer-algebraic binders. The comment inherited
inside the bridge about no project imports describes its isolated provenance; this second execution
explicitly imports the project and is labelled accordingly.

[generality source](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/generality2-executed.lean.txt), [generality receipt](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/generality02-receipt.json), [isolated modern source](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/modern-executed.lean.txt), [isolated modern receipt](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/modern01-receipt.json), [PROJECT source](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/project-modern-executed.lean.txt), [PROJECT receipt](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/projectmodern01-receipt.json).

## Phase4c — all nine modern idioms

| Question | Result | Consequence |
|---|---|---|
| Typeclasses | No | Pointwise irrational/algebraic propositions should remain hypotheses. |
| Filters/nets | Yes | LiouvilleWith already uses frequently atTop denominators and existential C. Exponent-gap bridge connects it to the uniform theorem. |
| Universal properties | No | No object is being characterized by a universal property. |
| Bundled substructures | No | Approximation solutions are not a subring/submodule. |
| Algebraic hierarchy | No | Actual proof requires real powers, logarithms and integer arithmetic; arbitrary-field variant unverified and characteristic-p analogue fails. |
| Higher categories | No | No categorical statement or useful categorification. |
| Concrete indices | No | Integers/naturals encode rational approximation; arbitrary monoids change the object. |
| Concrete-via-abstract diagnostic | No new weakening | No fixed named x or unfolding rewrite. The body forwards both semantic hypotheses to Roth. Supplying the full Roth conclusion as a hypothesis abstracts away the hard theorem. Generic t transport is useful but does not change the algebraic threshold2. |
| False-generalization guard | PASS | Uniform↔Liouville family retains Irrational. Rational cutoff holds while uniform fails. All-real unreduced pair iff is separately proved because exact rational multiples are infinite. Liouville family defeats removing algebraicity. |

Modern verdict: **available and verified**. Existing `LiouvilleWith.mono`,
`frequently_lt_rpow_neg`, `add_rat_iff` and `mul_rat_iff` become directly usable. Fresh isolated
proofs transport uniform bounds through rational translation and nonzero rational multiplication;
these are concrete downstream uses. This change exposes the same named theorem through mathlib's
existing exponent predicate and avoids a benchmark-specific primary definition.

## Phase4.5 — infrastructure risks

| Risk | Status and reason |
|---|---|
| Typeclass diamond | n/a theorem; no instance graph introduced. |
| Reducibility leak | n/a theorem; no new definitional unfolding. |
| Noncanonical unfolding | n/a theorem; proof does not install reductions. |
| Instance priority | n/a theorem; no instance priority. |
| Universe polymorphism | n/a theorem; real-valued proposition introduces no new type constructor. |
| Coercion ambiguity | n/a theorem; no coercion instance introduced. |

## Phase4.6 — all five proof-strategy checks

| Question | Result | Strategy |
|---|---|---|
| Topology epsilon/delta | No | Endpoint is theorem transport, not neighbourhood chasing. |
| Algebra element arguments | No | Use existing scalar algebraicity bridge directly. |
| Analysis sequences versus filters | Yes | Expose frequent LiouvilleWith endpoint; loss of exponent absorbs constants. |
| Category constructions | No | No categorical object construction. |
| Missing helper API | Yes | Full uniform/finite/frequent exponent transport and Roth exclusion are missing together; author generic transport beside primary theorem. |

**REFACTOR-RECOMMENDED** for the upstream interface. The original local proof already efficiently
composes its project ingredients. The contribution includes the hard Roth theorem, not merely
shortening its final invocation. Proof improvement follows mathematical API, without cost deciding
the verdict.

## Phase5 — all fifteen formal cells and pinned candidates

| Form | Lean-Finder | Loogle | LeanSearch | rg | local LSP |
|---|---|---|---|---|---|
| Current uniform theorem | Executed | Unknown identifier retained; corrected quoted query executed, no results | Executed | Executed | index error, no absence inference |
| Standard finite/exponent theorem | Executed | Executed | Executed | Executed | index error, no absence inference |
| Abstract LiouvilleWith endpoint | Executed | Executed | Executed | Executed | warming, no absence inference |

Every cell links its full raw receipt in the matrix. External indexes may be a different mathlib
revision; pinned source/native signatures decide compatibility. Candidate hits are near-matches:

* `Liouville.exists_pos_real_of_irrational_root` gives an exponent depending on polynomial degree,
  not2+epsilon for every positive epsilon.
* `Liouville.transcendental` excludes the intersection of all high-exponent approximability
  conditions, not every individual p>2 condition. Its quantifiers are weaker than Roth's endpoint.
* `Real.infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational` is Dirichlet's complementary lower
  irrationality-exponent direction. It supplies infinitely many exponent2 approximants, not the
  algebraic upper exponent bound.
* `ae_not_liouvilleWith` is an almost-everywhere statement; an algebraic point cannot be extracted
  from a measure-one statement, since the algebraic set is countable and null.
* `LiouvilleWith.exists_pos`, `mono`, `frequently_lt_rpow_neg`, `irrational` and rational affine
  invariance supply transport, not the algebraic exclusion theorem.

The pinned module `LiouvilleWith.lean` lines24–28 expressly mentions Roth's p>2 transcendence
implication as mathematical context; its body provides no such theorem. This is a concrete API gap,
not novelty inferred solely from missing search hits. Native candidate checks retain full signatures
and standard axioms. No isolated source imports Roth or assumes its conclusion in the composition
probe. Full-name grep is untruncated and actual exact?/simp probes precede authored bridge helpers.

[15-cell matrix](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/formal-search-matrix.json), [full-name grep](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/full-name-search.json), [pinned source inputs](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/mathlib-inputs.json), [composition receipt](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/composition01-receipt.json).

## Phase5.5 — statement shape

| Check | Verdict | Reason |
|---|---|---|
| Normal form | RESTATE | Existing LiouvilleWith family is primary; recover uniform benchmark via one generic equivalence with canonical family on RHS, not pairwise O(n²) bridges. |
| Syntactic generality | RESTATE | ℚ algebraicity composes with field API; p>2 negation removes redundant irrational binder for that precise form. Actual Q/finiteness/weak/modern/recovery alternatives compile. |
| Superfluous arguments | NONE in uniform target | x is essential; irrationality necessary at rational exact approximants; algebraicity necessary on Liouville family. Underscored binder names do not make assumptions unused. |

**RESTATE-BEFORE-SHIP** as the modern endpoint above; keep exact benchmark signature downstream.
Changing `<` to `≤` in a positive uniform family is verified by shrinking C, not assumed by syntax.

## Phase6.0 — callers, inline audit and duplication

| Scope | Actual result |
|---|---|
| Explicit canonical source callers |0 |
| External-to-file project caller files |0 |
| Fresh lexical rg --no-ignore and git grep | Declaration only; module doc references are context, not proof callers. |
| Fresh exact293 direct kernel type consumers |0 |
| Fresh exact293 direct kernel body consumers |0 |
| simp registration | None on this target. |
| Inline uniform rederivations bypassing target | None in production inventory. |

All293 canonical names were generated from tracked order, checked before execution for exact
private modules/order/uniqueness, then loaded natively with present293 and value293. Values use
`ci.value? (allowOpaque := true)` with explicit missing-value failure. Zero callers does not make
a named final benchmark endpoint dead code: this is the intended externally consumable output.
The endpoint is not dead code. No invented caller or chopped unrelated proof is used for inline evidence. Caller inlining is
justified n/a because there are no actual callers; complete source reading and audits still run.

| Pair comparison | Same statement? | Same proof? | Action |
|---|---|---|---|
| Final thueSiegelRoth / Roth.roth | Equivalent uniform/exponent families with irrationality, through verified bridge | Final transports project main theorem | One substantive upstream Roth result, several derived interfaces. |
| Final thueSiegelRoth / Roth.roth_rat | Equivalent rational representation at family level; no definitional set equality claimed | Rational endpoint maps reduced num/den; final uses positive minima | Group, do not create a duplicate contribution. |
| Final thueSiegelRoth / Roth.roth_of_isIntegral | Integral case is special hypothesis; scalar denominator reduction reaches general algebraic case | Substantive integral argument versus endpoint transport | Keep internal proof hierarchy, primary general algebraic API. |
| Final thueSiegelRoth / Liouville.transcendental | No; every epsilon versus degree-dependent finite exponent | Different quantitative strength | Cannot replace Roth by Liouville. |

[callers](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/callers.json), [lexical](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/source-search.json), [tracked grep](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/source-search-git.json), [inline search](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/inline-search.json), [canonical consumers](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/canonical-consumers.json).

## Phase6 — actual composition experiments

Isolated composition01 guards project `Roth.roth` and final target absence. Before any authored
helper, exact? fails to derive the full uniform theorem from irrationality and algebraicity; a
restricted simp expansion also fails. Separate probes of finite/exponent and Liouville family
forms fail. These bounded automation failures are corroborating experiments, not universal
unprovability results. Source/mathlib candidate comparison identifies the missing substantive step.

Attempt1: integer-to-rational scalar transfer followed by a mathlib Roth theorem. Scalar transfer
exists, but the required full all-epsilon Roth theorem is project-only.
Attempt2: `Liouville.transcendental` or its degree-bound theorem. Its quantifiers/exponent do not
yield every positive epsilon; no ≤3-call composition established.
Attempt3: frequent-atTop exponent gap and finite positive minimum. These provide representation
transport only; they do not prove that algebraic x cannot be LiouvilleWith p for p>2.

**NOT-COMPOSABLE from existing mathlib** in ≤3 chained calls. The original two project calls do
compose locally, but neither the project main theorem nor the authored bridge is an existing
mathlib building block. No closing simp composition is misreported as an automatic NO.

[exact isolated experiment](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/composition-executed.lean.txt).

## Phase7 — actionable contribution plan

**YES-but-generalise-first, MODERN-IDIOM.** Why add it: this is the named sharp Roth theorem,
whose all-epsilon algebraic upper exponent bound is explicitly distinguished from Liouville's
weaker theorem by the benchmark and pinned source context. The existing LiouvilleWith API already
organizes exponent monotonicity, exponent-loss absorption, irrationality and rational affine
transport. The missing algebraic p>2 exclusion belongs on that API. The actual project proof,
verified modern transport and complete original-signature recovery establish the connection.

Proposed primary statement, actually compiled with project content:

```lean
lemma algebraic_not_liouville {x p : ℝ} (ha : IsAlgebraic ℚ x) (hp : 2 < p) :
    ¬ LiouvilleWith p x
```

Equivalently expose `IsAlgebraic ℚ x → LiouvilleWith p x → p ≤ 2`; the strict p>2 negation is the
executed candidate, not an uncompiled widening. Full recovery retains original irrationality when
forming the uniform conclusion. The generic cutoff t belongs in the transport API; the algebraic
endpoint keeps sharp2. Number fields/places are a separate development, not a prerequisite here.

Exact proposed home: **Mathlib/NumberTheory/DiophantineApproximation/Roth.lean** (new substantive
module importing existing LiouvilleWith and the upstreamed proof hierarchy). Keep the foundational
LiouvilleWith file light; expose the theorem from the new Roth module. Proposed PR title:
**feat(NumberTheory/DiophantineApproximation): prove Roth's theorem via LiouvilleWith**.

Group in the accepted **Roth exponent exclusion and Diophantine approximation endpoints** group
with `Roth.roth_of_isIntegral`, `Roth.roth` and `Roth.roth_rat`; fresh tracked progress records all
three as accepted YES-but-generalise-first. This is one theorem contribution with equivalent
interfaces, not four independent mathematical results. IsDiophantine and isDiophantine_iff have
accepted BORDERLINE verdicts, so they are not mislabelled accepted YES candidates; retain the exact
benchmark adapter in Roth/LeanEval.lean while primary mathlib API uses LiouvilleWith.

Before opening: run `/generalise LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth` and
`/cleanup Roth/LeanEval.lean LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth` against this
concrete modern statement and the main grouped proof. Estimate MODERATE integration; cost is not a
verdict factor. Select a reviewer from actual relevant history: Yaël Dillies touched rational
coercion API in commit483ba09b2edd4d422fa9e502f1c6df6b382483e8 (2026-06-16), and Andrew Hendel
corrected DiophantineApproximation namespace documentation in834e51690b251d70cee9e014e90f4a80828881ff
(2026-05-12). These are recent relevant maintenance commits, not a claim they authored Roth's proof.
Xavier Roblot's171df1ee3232b67f4cf732014af10cfd2aed80ae (2023-06-02) ported LiouvilleWith and gives
older mathematical API provenance. The raw second history search also returned arithmetic-function
Liouville, which is unrelated and is not used as reviewer evidence.

[accepted progress snapshot](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/progress-snapshot.json), [recent commits](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/reviewer-commits.json), [mathematical history](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/reviewer-mathematical-commits.json).

## Phase8 — verification, rejected attempt and delivery

Five accepted root executions: original01 (exact target replay/full kernel type/body/axioms/293
audit), generality02 (Q↔Z, finite/weak/rational guard/recovery), modern01 (isolated generic bridge),
composition01 (isolated candidates and closure probes), projectmodern01 (actual project endpoint
and full uniform recovery). Every accepted diagnostic is checked for errors, warnings, partial,
timed out, sorryAx and PANIC including info severity. All reported axioms are standard propext,
Classical.choice and Quot.sound. Complete raw receipts and immutable executed sources remain intact.

Rejected generality01 is retained separately: an unrelated unavailable Liouville #check in disk
context and a backwards .symm on the scalar iff caused errors and recovered sorryAx. It is not
accepted proof evidence. Generality02 removes the unnecessary check (candidate already tested
isolated), corrects the native-signature orientation, and passes completely. Failed current Loogle
unknown-identifier query is likewise retained with a corrected quoted retry. Root local index
errors/warming are recorded honestly.

The package includes a portable read-only validator for scratch and integrated layouts, the actual
current manifest, fresh17 hashes, exact293 source/runtime integrity, all15 search cells and named
literature channels, both actual draft-layout checks and secret guard before completed=true, then
final checks. Root independently accepts, integrates, runs final dual builds/global gates and
publishes. This worker performs no publication or production change.

[verification](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/verification.json), [rejected receipt](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/generality01-receipt.json), [phase rows](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/phase-checks.json), [validator](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/validate.py).
