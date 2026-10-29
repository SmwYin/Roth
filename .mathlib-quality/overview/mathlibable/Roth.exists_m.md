# Roth.exists_m — full assessment

**BORDERLINE-needs-human.** The numerical existence theorem is valid and useful in Roth's proof. A stronger theorem with arbitrary real size coefficient and numerator coefficient has been proved from mathlib in isolation, with exact old recovery and the complete actual caller checked. The remaining question is whether this precise combination deserves public upstream API. This is a completed assessment, not a user blocker; no production change is proposed here.

## 0. Baseline and scope

Canonical275, public theorem at `Roth/Main.lean:196–218`. All of Main (588 lines) and LeanEval (66 lines), including the full actual caller, were read. The original replay scope is exactly the target, renamed `Dimension275Original.replay` in a fresh namespace; no helper closure is needed. Existing public project imports remain available. The equality check with `Subsingleton.elim` certifies exact original/replay proposition agreement, not proof-construction identity.

The reusable baseline completed2467jobs cleanly. All17source/pin hashes were freshly matched against the tracked shared manifest and checked again before freeze. No file-boundary build is due at275; the next is289. Root exclusively executed every native and local-LSP request; the worker prepared sources, inspected returned evidence, and ran portable checks. No production/pin/Git/overview/progress change or native limit raise was made.

Evidence: [baseline-build.txt](../evidence/Roth.exists_m/baseline-build.txt), [inputs.json](../evidence/Roth.exists_m/inputs.json), [input-manifest.json](../evidence/Roth.exists_m/input-manifest.json), [source-Main.lean.txt](../evidence/Roth.exists_m/source-Main.lean.txt), [source-LeanEval.lean.txt](../evidence/Roth.exists_m/source-LeanEval.lean.txt), [original-executed.lean.txt](../evidence/Roth.exists_m/original-executed.lean.txt), [original-receipt.json](../evidence/Roth.exists_m/original-receipt.json).

## 1. Statement and proof

For every natural n, including0, and every real κ>2, there exists a natural m strictly exceeding16n². It simultaneously satisfies4n√m<m and2m/(m−4n√m)<κ. Thus m is positive and the quotient denominator is positive. The theorem makes no assumption that n is a polynomial degree or n≥2.

Full loaded kernel type (captured with Lean.getConstInfo and pp.funBinderTypes, not by splitting a printer output at an internal let):

```lean
∀ {n : ℕ} {κ : ℝ},
  2 < κ → ∃ (m : ℕ), 16 * n ^ 2 < m ∧ 4 * ↑n * √↑m < ↑m ∧ 2 * ↑m / (↑m - 4 * ↑n * √↑m) < κ
```

The original chooses s=ceil_nat(4κn/(κ−2))+4n+1 and m=s². The additive slack gives s>4n and s>0; ceiling control gives4κn<s(κ−2). Multiplication by s then proves all three bounds after √(s²)=s and positive-denominator division. The source proof has no project-declaration dependency. Kernel lists include generated `Roth.exists_m._proof_*` constants, which are internal proof fragments, not separate canonical project declarations.

The full written source and full kernel type, constant lists, value availability and standard axioms were inspected. The `pp.all` body explicitly elides80194characters; it is **not** a full kernel-body dump. Both the loaded original and focused replay depend only on propext, Classical.choice and Quot.sound.

## 2. Preliminary checks

SMALL: a numerical parameter-selection helper, not a new mathematical structure, named theorem, or main result listed in the module's main-results list. The one-line definition test is n/a because this is a theorem. Proof length does not determine the contribution verdict.

## 3. Exhaustive literature

All named channels were actually attempted. Optional ask_chatgpt_math is unavailable. Search receipts preserve exact requests, returned-response SHA256/byte count/status, clean titles/URLs and concise original summaries; no full third-party article/search body is stored. Some batched results are out of the requested namespace; this is recorded rather than treated as absence.

| Channel | Actual query / locator | Finding |
|---|---|---|
| General web | `Roth theorem proof "m" "4n" "kappa" parameters square root` | Roth proof/background and Archimedean bound selection; no named combined selector. [web1-receipt.json](../evidence/Roth.exists_m/web1-receipt.json) |
| General web | `Archimedean property choose sufficiently large integer rational function square root limit` | Roth proof/background and Archimedean bound selection; no named combined selector. [web1-receipt.json](../evidence/Roth.exists_m/web1-receipt.json) |
| General web | `Roth rational approximations algebraic numbers 1955 proof choice m parameter` | Roth proof/background and Archimedean bound selection; no named combined selector. [web1-receipt.json](../evidence/Roth.exists_m/web1-receipt.json) |
| ask_chatgpt_math | n/a | Optional tool unavailable; no second-opinion response invented |
| local | [literature-local.json](../evidence/Roth.exists_m/literature-local.json) | Choose sufficiently large positive integer dimension with positive denominator and ratio<κ; formal theorem adds explicit16n² bound. |
| nLab | [web2-receipt.json](../evidence/Roth.exists_m/web2-receipt.json) | Archimedean ordered field/property background; does not package these three bounds. |
| nCatLab | [web5-receipt.json](../evidence/Roth.exists_m/web5-receipt.json) | Actual distinct site:ncatlab.org/ncatlab query returned /nlab results; no in-namespace exact statement. Not categorical; no absence claim. |
| Stacks | [web5-receipt.json](../evidence/Roth.exists_m/web5-receipt.json) | Actual Stacks-targeted query; returned batch shows no relevant Stacks theorem. Scalar real inequalities, not an algebraic geometry interface. |
| MathOverflow | [web3-receipt.json](../evidence/Roth.exists_m/web3-receipt.json) | Number-theory Roth quantitative bounds questions appear; additive Roth hits are different. No named simultaneous scalar choice theorem identified. |
| recent arXiv | [web6-receipt.json](../evidence/Roth.exists_m/web6-receipt.json) | Actual date window after:2021-10-29 before:2026-10-30. Hindes2209.09182 concerns characteristic p where Roth fails, not these real scalar inequalities; other recent applications/generalizations do not identify this helper as named standalone theorem. |

The closest exact source is the local reference, §7 eq(47), lines1588–1594: choose a positive integer m with m>4n√m and quotient<κ, using κ>2. The formal theorem additionally exposes16n²<m. This is a standard step in the proof of Roth, not an independently named theorem found by the search. The publisher page confirms Roth's1955 article (June1955, pp1–20; online2010 is distinct), but the visible extract does not display internal eq(47). The IMU1958 search extract discusses many variables; root's direct PDF open failed400 for74705952bytes, so no claim of a full read is made. Root independently checked the actual local formula and publisher metadata.

Sources: [Roth1955 publisher page](https://www.cambridge.org/core/journals/mathematika/article/rational-approximations-to-algebraic-numbers/EFB89E2873019B246F004FAA06E05A7F), [IMU1958 outline](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf), [nLab Archimedean property](https://ncatlab.org/nlab/show/Archimedean%2Bproperty). Recent-arXiv query used after:2021-10-29 before:2026-10-30; [Hindes2209.09182](https://arxiv.org/abs/2209.09182) treats characteristic p and different approximation methods, not this scalar selection lemma. Additive Roth search hits are unrelated.

Evidence: [literature.json](../evidence/Roth.exists_m/literature.json), [literature-source.json](../evidence/Roth.exists_m/literature-source.json), [literature-local.json](../evidence/Roth.exists_m/literature-local.json), [root-primary-crosscheck.json](../evidence/Roth.exists_m/root-primary-crosscheck.json), [web4-receipt.json](../evidence/Roth.exists_m/web4-receipt.json), [web6-receipt.json](../evidence/Roth.exists_m/web6-receipt.json).

## 4. Generality

| Parameter | Current | Verified analysis |
|---|---|---|
| n | arbitrary ℕ | No n>0 required. Replace4n by arbitrary real a, even signed, and16n² by a². |
| κ | real | Retain reals for Real.sqrt; full arbitrary-field sqrt transport is not claimed. |
| hκ | 2<κ | Cannot weaken uniformly to2≤κ: n=0,κ=2 admits no witness, compiled counterexample. |
| coefficient4 | fixed multiplier of n | Independent real c and real size t are allowed via a=c*t; positive c/nonnegative t included. |
| numerator2 | fixed | Arbitrary signed b with sufficient b<κ works; not asserted necessary for every fixed signed a,b. |
| m | natural witness | Kept natural to supply finite variable counts; replacing it by a real would not recover the project interface. |

First a≥0 was verified. The stronger signed variant chooses natural s>max(|a|,κa/(κ−b)) and m=s². Since s>|a| and s>0, a²<m and a√m<m. The cross-multiplied quotient follows from κa<s(κ−b). All arithmetic positivity obligations are proved, and n=0 is tested explicitly. No argument supplies the desired conclusion as a premise.

Verified stronger signature:

```lean
∀ {a b κ : ℝ}, b < κ → ∃ m : ℕ, a ^ 2 < (m : ℝ) ∧ a * √(m : ℝ) < m ∧ b * m / (m - a * √(m : ℝ)) < κ
```

This is **our new generic proof**, not a theorem already in mathlib. Exact old recovery specializes a=4n,b=2 and transports the first inequality back to ℕ using arithmetic and exact_mod_cast. The full original caller also compiles using this recovery with its original signature intact. A meaningful scalar parameter has replaced project constants; nevertheless, searches did not establish that this exact conjunction is the customary standalone upstream API. Generality is mathematically established; upstream interface choice remains a Phase7 question. Cost is not part of the verdict.

A full Tendsto-to-b alternative was considered and searched. Pinned Real.tendsto_sqrt_atTop and tendsto_bdd_div_atTop_nhds_zero are verified building blocks. No full normalized quotient limit, eventual denominator bound, or simultaneous eventual witness theorem has been claimed or counted as an existing replacement. The explicit generic proof already certifies the required quantitative existence.

Evidence: [generic-executed.lean.txt](../evidence/Roth.exists_m/generic-executed.lean.txt), [generic-receipt.json](../evidence/Roth.exists_m/generic-receipt.json), [signed-executed.lean.txt](../evidence/Roth.exists_m/signed-executed.lean.txt), [signed-receipt.json](../evidence/Roth.exists_m/signed-receipt.json), [generality.json](../evidence/Roth.exists_m/generality.json), [replacement-caller-executed.lean.txt](../evidence/Roth.exists_m/replacement-caller-executed.lean.txt), [replacement-caller-receipt.json](../evidence/Roth.exists_m/replacement-caller-receipt.json).

### Modern idiom — all nine rows

| # | Question | Verdict | Concrete analysis |
|---|---|---|---|
| 1 | Typeclasses | no | No structured hypotheses to rebundle; a strict scalar gap is a proposition. |
| 2 | Filters/nets | possible alternative | Search identifies Tendsto.sqrt and Real.tendsto_sqrt_atTop; full simultaneous conclusion is instead proved constructively. No unverified limit replacement counted. |
| 3 | Universal property | no | Selecting a numerical witness has no uniqueness/universal mapping characterization. |
| 4 | Bundled substructures | no | No closure predicate or algebraic subobject. |
| 5 | Weaker hierarchy | partially | Archimedean bound selection works for ordered semirings; Real.sqrt part remains real. Shape probe certifies abstract bound selection only. |
| 6 | Higher categories | no | Numerical real inequalities do not gain categorical content. |
| 7 | Concrete indices | yes | n natural magnitude replaced by arbitrary real a; coefficient b replaces2. The witness m remains natural, essential to finite variable counts downstream. |
| 8 | Concrete-via-abstract | diagnostic recorded | No named project mathematical object appears in statement or body; constants4,16,2 occur repeatedly. New generic proof independently verifies magnitude/asymptote abstraction, without using vanish-after-unfold heuristic as proof. |
| 9 | False-generalisation guard | PASS | All three quantitative bounds retained, m natural, n=0 retained, κ=2 uniformly refuted, exact old signature recovered. Signed-a result is true; not an unrelated finite-dimensional algebra statement. |

The signed-size version lets unrelated real error coefficients and arbitrary leading ratio coefficients use the same proof without manufacturing natural dimensions in advance. No categorical, finite-dimensional-algebra or abstract-square-root theorem is substituted for the scalar statement. The natural witness remains compatible with the actual finite-variable caller.

### 4.5. Infrastructure risk

All six rows are n/a for a theorem: typeclass diamond, reducibility leak, noncanonical unfolding, instance priority collision, universe-polymorphism data, and coercion ambiguity. No definition/instance/coercion is introduced. The explicit six-row record is in [phase-checks.json](../evidence/Roth.exists_m/phase-checks.json).

### 4.6. Proof strategy — all five rows

| # | Question | Verdict | Analysis |
|---|---|---|---|
| 1 | Topology epsilon-delta | n/a | No local continuity proof. |
| 2 | Algebra elements/subobjects | n/a | Scalar inequalities; no ideal/submodule alternative. |
| 3 | Analysis sequence/filter | considered | Filter route would require quotient normalization and positivity bookkeeping; explicit square witness proves the actual simultaneous quantitative statement. |
| 4 | Category universal property | n/a | No category or universal object. |
| 5 | Missing helpful API | possible | A generic simultaneous square-root denominator witness lemma is now proved in scratch; whether sufficiently reusable upstream is a taste/API question, not existing mathlib. |

MATHLIB-IDIOMATIC: direct Archimedean square witness avoids proving only a limiting slogan. A proposed upstream generic API would be the scratch theorem itself, not a pre-existing helper silently assumed available.

## 5. Five methods × three forms

| Form | Finder | Loogle | LeanSearch | rg | Local |
|---|---|---|---|---|---|
| current | [finder](../evidence/Roth.exists_m/formal-current-finder.json) | [loogle](../evidence/Roth.exists_m/formal-current-loogle-retry.json) | [search](../evidence/Roth.exists_m/formal-current-search.json) | [rg](../evidence/Roth.exists_m/formal-current-rg.json) | [local](../evidence/Roth.exists_m/formal-current-local.json) |
| standard | [finder](../evidence/Roth.exists_m/formal-standard-finder.json) | [loogle](../evidence/Roth.exists_m/formal-standard-loogle-retry.json) | [search](../evidence/Roth.exists_m/formal-standard-search.json) | [rg](../evidence/Roth.exists_m/formal-standard-rg.json) | [local](../evidence/Roth.exists_m/formal-standard-local.json) |
| abstract | [finder](../evidence/Roth.exists_m/formal-abstract-finder.json) | [loogle](../evidence/Roth.exists_m/formal-abstract-loogle-retry.json) | [search](../evidence/Roth.exists_m/formal-abstract-search.json) | [rg](../evidence/Roth.exists_m/formal-abstract-rg.json) | [local](../evidence/Roth.exists_m/formal-abstract-local.json) |

Current-form semantic hits concerned additive Roth numbers, integer square roots and unrelated bounds; they do not prove the statement. Standard-form queries found square-root/filter growth building blocks. Abstract queries found the existing exists_nat_gt and Archimedean API. Positive candidate signatures were pinned natively and source files archived with hashes. External indexes can describe different revisions: the pin locates exists_nat_gt at Algebra/Order/Archimedean/Defs.lean:76 and Real.sqrt_sq at Analysis/Real/Sqrt.lean:181.

All three local requests returned `index=error`, despite positive candidate lists. These do not provide negative presence evidence. Initial Loogle attempts were rate-limited; successful later retries are separate receipts. An initial remote batch could not serialize its receipts; all nine queries were repeated with complete subsequent raw archives. The untruncated current-name rg returned exit1; it is not by itself an absence proof. Compiled `fail_if_success exact?` on the full current goal and full signed-generic goal also did not close. These checks support “no replacement identified”, not a logical theorem of library absence.

Evidence: [formal-search-matrix.json](../evidence/Roth.exists_m/formal-search-matrix.json), [mathlib-inputs.json](../evidence/Roth.exists_m/mathlib-inputs.json), [shape-receipt.json](../evidence/Roth.exists_m/shape-receipt.json), [composition2-receipt.json](../evidence/Roth.exists_m/composition2-receipt.json).

## 5.5. Statement shape

| Check | Verdict | Analysis |
|---|---|---|
| Normal form | RESTATE if upstream | Exists natural square witness versus eventual inequality; current caller needs existential. Middle inequality follows from first, certified by shape proof; retain it for old recovery. |
| Syntactic generality | RESTATED IN SCRATCH | Use real a,b and b<κ; recover old n:ℕ form exactly, full actual caller replacement compiled. |
| Superfluous arguments | NONE in current statement | n,κ occur in conclusion; κ>2 cannot be removed uniformly. No typeclasses. Positivity assumptions on signed a,b are unnecessary in generalized theorem and were actually dropped. |

The existential conjunction is directly convenient for the caller. The middle inequality follows from16n²<m, verified independently with Real.lt_sqrt and multiplication by positive√m. Thus an upstream minimal interface could separate this bridge, while exact original recovery must retain all three requirements. The alternative abstract simultaneous-bound lemma is checked over an Archimedean ordered semiring; it does not pretend Real.sqrt generalizes through that hierarchy. RHS normalization conventions are not relevant to an existential theorem with no equivalence rewrite.

Evidence: [shape-executed.lean.txt](../evidence/Roth.exists_m/shape-executed.lean.txt), [shape-receipt.json](../evidence/Roth.exists_m/shape-receipt.json).

## 6.0. Complete callers and inlining

| Caller | Site / calls | Full original use | Experiments |
|---|---|---|---|
| Roth.exists_roth_parameters_aux (private) | Main:419 /1 | n=f.natDegree; consumes hm and quotient bound in exists_delta, discards middle bound, uses degree≥2 to derive m≥2 | Full original caller signature/body checked with literal target proof in local helper, and separately with signed-generic recovery. |

Fresh `rg --no-ignore` and `git grep` across all tracked production modules agree: one explicit proof caller, no cross-file explicit caller. Two documentation mentions occur at29 and220; target declaration at196 is not a caller. Native exact293 audit finds that same one direct kernel-value consumer and zero direct type consumers. Five canonical type/value transitive consumers are the private parameter selector, Roth.roth_of_isIntegral, Roth.roth, Roth.roth_rat, and LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth. Target's canonical dependency closure is only itself. This is an explicit canonical-project graph, not a traversal of every imported mathlib/generated constant. No simp attribute exists on the target; lexical references and opaque kernel/transitive dependencies are distinct scopes.

Every actual affected direct caller is fully checked. All transitive consumers' full modules were read; they do not contain another target call to inline. Raw canonical names preserve correct private modules and exact293order, generated directly from tracked declaration-order; Python preflight and native requested/unique/present/value counts all pass.

Evidence: [source-search.json](../evidence/Roth.exists_m/source-search.json), [git-source-search.json](../evidence/Roth.exists_m/git-source-search.json), [inline-search.json](../evidence/Roth.exists_m/inline-search.json), [callers.json](../evidence/Roth.exists_m/callers.json), [caller-excerpt.lean.txt](../evidence/Roth.exists_m/caller-excerpt.lean.txt), [callers-executed.lean.txt](../evidence/Roth.exists_m/callers-executed.lean.txt), [callers-receipt.json](../evidence/Roth.exists_m/callers-receipt.json), [canonical-consumers.json](../evidence/Roth.exists_m/canonical-consumers.json), [consumer-scope2-executed.lean.txt](../evidence/Roth.exists_m/consumer-scope2-executed.lean.txt), [consumers2-receipt.json](../evidence/Roth.exists_m/consumers2-receipt.json).

## 6. Composition

NOT-COMPOSABLE by the identified existing API in≤3calls. exists_nat_gt or Nat.le_ceil selects a large scalar; it does not establish all square, sqrt and quotient bounds. Real.sqrt_sq and division order lemmas normalize once a suitable witness and positivity inequalities have been supplied. The actual original proof and new generic proof both contain substantive arithmetic bridging. The full current goal resisted exact?, simp and aesop in an accepted isolated test before the original proof closed it. This is evidence about those concrete routes, not an exhaustive impossibility theorem. The new generic theorem makes recovery short only after a new proof; it cannot count as an existing mathlib building block.

The literal full proof can be inlined at the one caller and passes, but that is a refactoring experiment, not a≤3-call composition. No NO-composable/delete recommendation follows merely from having one caller.

## 7. Verdict, overview findings and next action

**BORDERLINE-needs-human**, independently assessed; no parent verdict is inherited. The statement is a genuine useful numerical lemma, with a stronger verified form and no exact existing match identified. It is also an ad hoc conjunction associated with one stage of Roth's proof; the literature does not establish a named general public interface, and no second independent consumer was identified. The upstream API/publicness question remains after the proof work, not because generalization would cost time.

1. Should a generic natural-dimension selection theorem for a²<m and b*m/(m-a*sqrt m)<κ be public mathlib API, or stay local to a Roth proof until a second independent consumer exists?
2. If upstream, should the primary interface retain the explicitly derived middle inequality, or expose only the square bound and quotient bound with a separate square-root bridge?
3. Should such a reusable theorem live near real square-root inequalities or in a Roth/Diophantine approximation development, given the absence of an established standalone name?

These are future upstream design questions, not unresolved verification or a request blocking the project overview. Keep the current theorem in Roth/Main.lean pending that decision. If proposed upstream, use the signed generic result and decide whether to split the redundant middle inequality; tentative homes are a real square-root inequality module or a dedicated Roth proof module. No YES PR title/reviewer/grouping claim is made for this BORDERLINE package.

Moral duplication: exists_delta/exists_delta_bound choose real small parameters near0, while this theorem chooses a natural dimension at infinity; their conclusions and interfaces differ. No duplicate or junk classification follows from their common parameter-choice role. Missing API is at most a reusable generic quantitative selector, whose scratch proof is now available. The existing theorem is used, substantive, and safe to retain. There are no project proof dependencies to replace.

## 8. Verification and evidence

- Accepted original: [original-executed.lean.txt](../evidence/Roth.exists_m/original-executed.lean.txt), [original-receipt.json](../evidence/Roth.exists_m/original-receipt.json); root elapsed3453ms.
- Accepted callers: [callers-executed.lean.txt](../evidence/Roth.exists_m/callers-executed.lean.txt), [callers-receipt.json](../evidence/Roth.exists_m/callers-receipt.json); root elapsed2653ms.
- Accepted consumers: [consumer-scope2-executed.lean.txt](../evidence/Roth.exists_m/consumer-scope2-executed.lean.txt), [consumers2-receipt.json](../evidence/Roth.exists_m/consumers2-receipt.json); root elapsed2771ms.
- Accepted generic: [generic-executed.lean.txt](../evidence/Roth.exists_m/generic-executed.lean.txt), [generic-receipt.json](../evidence/Roth.exists_m/generic-receipt.json); root elapsed101182ms.
- Accepted signed: [signed-executed.lean.txt](../evidence/Roth.exists_m/signed-executed.lean.txt), [signed-receipt.json](../evidence/Roth.exists_m/signed-receipt.json); root elapsed2570ms.
- Accepted composition: [composition2-executed.lean.txt](../evidence/Roth.exists_m/composition2-executed.lean.txt), [composition2-receipt.json](../evidence/Roth.exists_m/composition2-receipt.json); root elapsed3503ms.
- Accepted shape: [shape-executed.lean.txt](../evidence/Roth.exists_m/shape-executed.lean.txt), [shape-receipt.json](../evidence/Roth.exists_m/shape-receipt.json); root elapsed797ms.
- Accepted replacementcaller: [replacement-caller-executed.lean.txt](../evidence/Roth.exists_m/replacement-caller-executed.lean.txt), [replacement-caller-receipt.json](../evidence/Roth.exists_m/replacement-caller-receipt.json); root elapsed1759ms.

Eight accepted native executions are clean, complete, and use standard axioms only. Two earlier executions are preserved and rejected: composition01 had erroneous indentation and recovered sorryAx; consumers01 used unavailable Array.union. Corrected immutable attempts passed. Rejected output is never counted as proof. All exact requests, executed sources, receipt hashes, full raw native/formal results, input hashes, current recursive manifest and read-only portable validator are included. Printer body elision and local index-error limitations are explicit. The checker validates both scratch and integrated layouts, every current-manifest artifact, canonical dependency membership/normalization, exact293array order/private modules, accepted-source identity, roots/prefixes, links, and final inputs.

Evidence: [assessment.json](../evidence/Roth.exists_m/assessment.json), [overview-entry.json](../evidence/Roth.exists_m/overview-entry.json), [verification.json](../evidence/Roth.exists_m/verification.json), [preparation-notes.json](../evidence/Roth.exists_m/preparation-notes.json), [composition-receipt.json](../evidence/Roth.exists_m/composition-receipt.json), [consumers-receipt.json](../evidence/Roth.exists_m/consumers-receipt.json), [validate.py](../evidence/Roth.exists_m/validate.py), [copy-manifest.json](../evidence/Roth.exists_m/copy-manifest.json), [validation-scratch.json](../evidence/Roth.exists_m/validation-scratch.json), [validation-integrated.json](../evidence/Roth.exists_m/validation-integrated.json), [secret-scan.json](../evidence/Roth.exists_m/secret-scan.json).
