# `exists_genWronskian_ne_zero`: original declaration cleanup

Final source SHA256 `cbd1564dda27d17e67feacd0712e035fdfd0feeeefe920d6f7603cee970bade8`.
Earlier d2ae601… checkpoint was superseded by mandatory have inlining.
Original declaration lines 236–261: 26 lines, 23 proof lines. Final lines 252–267:
16 lines, 13 proof lines. Saved 10 headline lines. Added one meaningful private helper,
`wronskian_kronecker_eq_sum_aux`, lines 230–244: 15 lines, 9 proof lines.
Total source therefore grows by 6 lines; this is honest mathematical decomposition,
not a total-file line-saving claim. This report credits exactly one ORIGINAL declaration.
The helper requires a separate fresh audit and receives no original-declaration credit.

Only the owned original theorem body and the approved helper were changed. The original
public signature and docstring are byte-identical. No other source declaration, import,
header, global structure, setting, axiom, or instance was edited. Parent explicitly
revoked all source ownership after the checkpoint; subsequent work here is report-only
or isolated `/private/tmp` checks. No commits, pushes, full builds, or child agents.

## References and mathematical context

Read `mathlib-quality/SKILL.md`, `lean4/SKILL.md`, the worker contract, and the full
`golfing-rules.md`, `proof-patterns.md`, `mathlib-search.md`,
`generalisation-patterns.md`, `cleanup-gates.md`; relevant `style-rules.md` sections
and `mathlib-review-stages.md` were also read. Native Lean tools were discovered from
ALL_TOOLS metadata and actually used; no fallback MCP script was needed.

A Kronecker substitution with base larger than every partial degree preserves linear
independence. Its univariate Wronskian is nonzero. The uniform Hasse derivative
expansions and determinant multilinearity express it as a sum of substituted generalized
Wronskians. If every bounded-order generalized Wronskian were zero, that sum would be zero.
The helper isolates precisely the determinant expansion. It assumes arbitrary supplied
expansion coefficients, without CharZero, degree bounds, or linear independence.

Initial complete-file LSP: success=true, partial=false, timed_out=false, errors=0,
failed_dependencies=[]. The target warning is `unusedFintypeInType`; the file also has
pre-existing header, dependent-result Fintype, and det_sum_rows DecidableEq warnings.
These were not suppressed. Baseline supplied by parent:
`/private/tmp/roth-genwronskian-baseline.lean`.

## Full initial audit and resolutions (24 items)

1. **Lint.** Original target has only the Fintype-in-type warning. Instance is protected;
   retained, with the finite-variable rationale and caller review below. No new warnings.
2. **Have scan.** Original `hk`: by-proof, used once, replaced by direct Nat.lt_add_right.
   `hdeg`: originally by-proof, once at independence step; initially converted to
   a term-proof have, then correctly identified by owner as a mandatory inline and fully
   inlined into the linearIndependent_kronecker call. Nested `h1`, `h2`: no by, once each, both inlined via `.trans`.
   `hW`: no by, once, inlined into the contradiction step. `hexp`: by-proof, once,
   extracted as the approved meaningful helper. Nested `hM`: by-proof, once, retained
   inside the helper for matrix extensionality. Corrected headline has no have;
   no duplicate estimates, projections, or single-use no-by alias remains.
3. **Set option.** n/a: none in the owned declaration or added helper; no limits raised.
4. **Simp squeeze.** Original two `(by simp)` side proofs close their whole nonnegativity
   goals; terminal, retained unsqueezed. Final two such side proofs remain terminal.
5. **Naming.** `exists_genWronskian_ne_zero` describes an existential nonvanishing result;
   no forbidden abbreviation/pattern/single-letter name. New helper private and `_aux`.
   No rename required or queued.
6. **Line packing.** Every original/final signature line measured below; no underpacked
   complete parameter/conclusion token can be moved. No source line exceeds 100 codepoints.
7. **By placement.** `:= by` remains at the end of the conclusion line.
8. **Format.** Two-space tactics, four-space signature continuation, no blank proof lines,
   no haveI/letI, no semicolon chains. Ordinary lambdas now use ↦ throughout owned code.
9. **Comments.** No inline proof comments existed. None removed. Docstring preserved.
10. **Docstring.** Existing source-citing public documentation retained byte-for-byte,
    per protected-documentation instruction. It describes the tight operator bounds.
11. **Visibility.** Public headline used by Roth.Separation; preserve public visibility.
    The determinant-expansion helper is private; no private docstring introduced.
12. **Structure.** Honest extraction attempted and completed: 23→13 proof lines;
    helper 9 proof lines. No >10-line case branch remains. The existential packages
    bounds and nonvanishing for the SAME witness D: preserving this exact public bundle
    is an explicit task requirement, overriding mechanical conjunction splitting.
13. **Mathlib.** All five actual methods below; no replacement found. The helper uses
    the existing determinant multilinearity API, not a new determinant definition.
14. **Junk def.** n/a: theorem, not data. All three original public definitions untouched.
15. **Exists lemma.** Not a trivial private witness wrapper: this is the public main
    nonvanishing theorem with a substantive substitution/independence argument.
16. **Show/change.** n/a: no show, change, or definitional-equation plumbing.
17. **Push neg.** Already uses by_contra!; no deprecated push_neg introduced.
18. **Generalise.** Every parameter reviewed below; public API retained. CharZero and
    independence are essential for the stated tight bound. No pending routine proposal.
19. **Inequality.** Scan below; no ≥ or > in signature/hypotheses. Degree bound uses ≤.
20. **Normal form.** Existential bounded multi-indices and nonzero determinant already
    express the source result directly. No equivalent mathlib normal form found.
21. **Syntax generality.** OK: Separation immediately obtains D, hD, hG from this bundle.
    Splitting the existential facts would lose the shared-witness application pattern.
22. **Import fanout.** n/a: no import added or removed.
23. **Casts.** 0 dropped / 0 explicit cross-type casts added / 0 explicit load-bearing
    coercions added. Existing Fin l indices coerce to Nat for derivative order and bound;
    the helper explicitly annotates μ : Fin l because its derivative occurrence alone
    would otherwise infer Nat. This is a necessary binder annotation, not a value cast.
24. **Instance name.** n/a: no instance declaration added or changed; classical is local.

Issues fixed: headline decomposition; both omega calls replaced with direct arithmetic;
single-use h1/h2/hW/hk eliminated; all owned lambda arrows normalized.
Routine refactoring needed: none. Added helper awaits the mandated separate fresh audit.

## Mathlib search status (five actual methods)

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | linearly independent multivariate polynomials generalized Wronskian nonzero Hasse derivatives | SubmersivePresentation.linearIndependent_aeval_val_pderiv_relation; Polynomial.Sequence.linearIndependent; Matrix.det_mvPolynomialX_ne_zero. Different conclusions, no replacement. |
| B Loogle | `LinearIndependent, MvPolynomial, Exists` | Empty item list; successful query, not an absence proof. |
| C LeanSearch | linearly independent polynomials have a nonzero generalized Wronskian | Polynomial.wronskian; Polynomial.wronskianBilin; IsCoprime.wronskian_eq_zero_iff. These concern the two-polynomial univariate Wronskian, not this result. |
| D source rg | full names exists_genWronskian_ne_zero, wronskian_kronecker_eq_sum, genWronskian and phrase generalized Wronskian over all Mathlib source | Untruncated query produced no matches; no claim of mathematical absence follows. |
| E lean_local_search | wronskian, limit 20 | Roth local criterion and Mathlib two-polynomial API; index reported warming, so coverage is explicitly limited. |

Auxiliary variants considered: wronskian_eq_zero_iff, wronskian_ne_zero_of_linearIndependent,
wronskianBilin, determinant nonvanishing, linearIndependent_aeval, row multilinearity.
Common-equivalents table: no discrete/finite/separation/metric bucket matches this theorem.
`exact?` and `apply?` were actually attempted at the original pre-theorem proof state;
no completed proof was obtained. `apply?` offered only generic existential/filter
reformulations with remaining goals. The later snippet experiment on a term proof line
was syntactically invalid and is NOT counted as a tactic failure or absence evidence.
The valid whole-headline attempts with `classical; grind`, `classical; aesop`, and
`classical; simp` leave the existential goal or fail the contradiction.

Conclusion: retain the substantive local theorem, with no claim that searching establishes
absolute absence. Six strict rules checked: no 1–3-call wrapper replacement identified;
no custom predicate substituting for a typeclass; no equivalent found to delete;
auxiliary forms inspected; actual absence probes reported honestly; no module-docstring
change is authorized or needed because no new mathlib replacement was introduced.

## Generalisation status: every parameter

| Parameter | Class | Use / all applicable candidates | Verification and result |
|---|---|---|---|
| K : Type* | type variable | Coefficient field. Drop makes Field K and φ ill-scoped; Type* already universe polymorphic; no narrower universe remains. | Retain; syntactic dependency. |
| Field K | typeclass | Scalar field for independence and existing substitution/univariate criterion. Drop, DivisionRing, CommRing, CommRing+IsField considered. | DivisionRing probe fails CommSemiring R for MvPolynomial. CommRing probe of linearIndependent_kronecker fails Field R. Dropping Field loses coefficient structure. IsField presentation merely rebundles the same mathematical field and needs local field conversion, so not a weakening useful to the sole caller. No source mutation. |
| σ : Type* | type variable | Variable index. Drop makes polynomial/multi-index types ill-scoped; already universe polymorphic. | Retain. |
| Fintype σ | typeclass | Enumerates variables for Kronecker exponents and finite sum degree majorant. Drop and Finite+Fintype.ofFinite reviewed. | Explicitly protected source instance. No all-finiteness removal attempted: would require finite-support reduction, a substantial different proof. Finite is a plausible rebundling, but current Separation caller already supplies Fintype τ, so no actual caller benefit; closed no-current-need, no public proposal pending. |
| l : ℕ | structure value/index | Cardinality of family and precise operator-order bound. Drop is ill-scoped. Arbitrary finite family would need reindexing and replacement of μ's order, hence a public restatement. | Retain; no justified current caller change. |
| CharZero K | typeclass | Needed by uniform derivative expansion and univariate nonvanishing. Drop is the applicable mechanical test; no parent class of CharZero weakens meaning here. | Isolated same-proof drop exits 1 at exists_hasseDeriv_kronecker_eq_sum: cannot synthesize CharZero K. Retain. |
| φ : Fin l → MvPolynomial σ K | structure value | Family being differentiated. Drop leaves h/conclusion ill-scoped; alternate polynomial/formal-series object changes API and proof. | Retain; arbitrary φ already. |
| h : LinearIndependent K φ | proposition | Supplies nonvanishing univariate Wronskian after substitution. Drop; point-local restriction; unbundling considered. | Corrected target-only isolated drop exits 1 at use of h. The all-zero one-element family also mathematically refutes dropping h. No pointwise/unbundled catalogue weakening applies: independence concerns the entire family. Retain. |

No explicit decidability hypothesis; local classical scope remains necessary for the
choice and finite function sets. No positivity/strict hypothesis appears in the public
signature to weaken. Internally k's strict degree separation is necessary for injectivity.
No nonzero hypothesis was artificially weakened to nonnegativity.

Inversion check: no merely concrete witness is being unfolded and forgotten.
The statement uses the problem-specific genWronskian; its determinant unfolds in the
extracted expansion identity, but the proof still crucially uses Hasse-derivative
substitution and a bounded-order support condition. Replacing it by arbitrary linear
operators would require substantial additional hypotheses, not the same proof for free.
The meaningful abstraction actually extracted is the expansion with arbitrary c and s.

## Public literature search (three distinct actual web queries)

1. `generalized Wronskian linearly independent multivariate polynomials order at most i characteristic zero`.
   Top three returned: [Stanford lecture notes](https://math.stanford.edu/~ksound/TransNotes.pdf),
   [Bostan–Dumas paper mirror](https://citeseerx.ist.psu.edu/document?doi=764fc665e7ba79d9301b9508b7c49f91764623a2&repid=rep1&type=pdf),
   [Diophantine approximation and the subspace theorem](https://www.researchgate.net/publication/388657718_Diophantine_approximation_and_the_subspace_theorem).
2. `generalized Wronskians Roth theorem multivariate polynomials lemma`.
   Top three returned: [Walker paper mirror](https://doczz.net/doc/7963902/linear-dependence-of-quotients-of-analytic-functions-of-s...),
   [UCL notes](https://www.ucl.ac.uk/~ucahpet/TransNotes.pdf),
   [Chen's Roth obituary PDF](https://www.williamchen-mathematics.info/researchfolder/op05.pdf).
3. `Wronskian criterion several variables generalized derivatives characteristic p`.
   Top three returned: Wronskian overview (wikipedia mirror),
   [Diophantine approximation and the subspace theorem](https://www.researchgate.net/publication/388657718_Diophantine_approximation_and_the_subspace_theorem),
   [Wronskian testwiki](https://en.wiki.beta.math.wmflabs.org/wiki/Wronskian).
   These noisy secondary hits were recorded as search results, not used as authority.

Primary sources opened and read: [Bostan–Dumas](https://mathexp.eu/dumas/publications/Bostan_Dumas_2010_WLI.pdf)
and [Stanford notes](https://math.stanford.edu/~ksound/TransNotes.pdf).
The former extends the characteristic-zero result to formal power series and discusses
the failure in characteristic p; the latter gives the bounded-order multivariate
polynomial criterion and Kronecker reduction. These support retaining the present
characteristic-zero bounded-order result. Larger function spaces are mathematically
interesting but require a different public API and no current caller needs them.
For this exact tight bound, 1 and X^p in characteristic p are independent but derivatives
of order ≤1 cannot distinguish them, so simply dropping CharZero is not sound.

ChatGPT math MCP: unavailable; ALL_TOOLS discovery found no chatgpt-math tool.
No second-opinion claim is made. Literature-driven pending public proposals: none.

## Per-line signature packing

Actual `#check @Roth.exists_genWronskian_ne_zero`, `set_option format.width 100`:

```lean
@Roth.exists_genWronskian_ne_zero : ∀ {K : Type u_1} [inst : Field K] {σ : Type u_2} [Fintype σ] {l : ℕ} [CharZero K]
  {φ : Fin l → MvPolynomial σ K},
  LinearIndependent K φ → ∃ D, (∀ (μ : Fin l), Finsupp.degree (D μ) ≤ ↑μ) ∧ Roth.genWronskian D φ ≠ 0
```

Widths measured with Python len on Unicode source (codepoints). Signature unchanged,
so initial and final tables coincide except line offsets:

| Original/final line | Chars | Next complete signature token | Arithmetic | Action |
|---|---:|---|---|---|
| 236 / 252 | 79 | `(h : LinearIndependent K φ)` = 27 | 79+1+27=107 >100 | ok |
| 237 / 253 | 33 | existential conclusion including `:= by` = 76 | 33+1+76=110 >100 | ok |
| 238 / 254 | 80 | none; proof body next | n/a | ok |

The existential conclusion is one binder/conclusion token, consistent with the contract's
`: ∃ H₀ : ℝ, ...` token example. No wide-hyp escape invoked. No line repack needed.

## Inequality occurrence scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 1 | entire signature/hypotheses | no ≥ or > occurrence | n/a | no _ge_/_gt_ name |
| 2 | witness bound | `(D μ).degree ≤ μ` | already oriented | n/a |

Final owned proof uses only < and ≤ as well; arrow ↦ is not an inequality.

## Every golfing rule (42 statuses)

- [1.1] by-exact wrapper: n/a, absent.
- [1.2] by-rfl: n/a, absent in headline.
- [1.3] rw+exact→rwa: n/a, no such consecutive pair.
- [1.4] simp+exact→simpa: n/a, terminal side-goal simp has no successor.
- [1.5] trailing rfl after simp: n/a, absent.
- [1.6] constructor chain→tuple: n/a, contradiction proof builds no tuple explicitly.
- [1.7] apply+exact: n/a, apply sets a nontrivial zero-Wronskian goal, not a matching exact.
- [1.8] by_contra+push_neg: already by_contra!, retained.
- [1.9] eta reduction: no reducible lambda remains; dependent lambdas keep necessary arguments.
- [1.10] single-use haves: h1,h2,hW,hk eliminated; hdeg also fully inlined into the independence call.
- [1.11] apply+intro: n/a, no consecutive matching pattern.
- [1.12] redundant show: n/a, absent.
- [1.13] have+projections: n/a, no local paired projections; choose already names components.
- [1.14] merge rw: n/a, rewrite steps separated by essential finite-sum refinement.
- [1.15] terminal simp only: n/a, no squeezed terminal simp in owned headline.
- [1.16] nonterminal bare simp: n/a, all two `by simp` side proofs terminal.
- [1.17] dot notation: nested bounds use `.trans`; no longer named h1/h2.
- [1.18] <|: no nested closing-parenthesis wrapper whose replacement clarifies remaining proof.
- [1.19] push_neg→push Not: n/a, absent.
- [1.20] trivial ∃ helper: n/a, substantive public existence result.
- [2.1] whole grind: actually tried at headline, failed to derive False from independence.
- [2.2] delete before grind: n/a, no retained grind call.
- [2.3] simpa consolidation: n/a, no simp-then-closer chain.
- [2.4] fun_prop: n/a, no analytic/measurable property goal.
- [2.5] positivity: final degree strictness follows supplied upper-bound chain; no standalone
  positivity goal needing tactic search. The initial term-line positivity snippet was
  syntactically invalid and supplies no evidence; direct Nat proof used instead.
- [2.6] gcongr: n/a, finite-sum membership estimates need single_le_sum, not pointwise monotonicity.
- [2.7] lia/omega: direct Nat.lt_add_right and Nat.lt_add_of_pos_left replace both omegas;
  isolated arithmetic schema `a≤b → b≤c → a<2+c` was also checked with lia.
- [2.8] aesop: actually tried whole headline; exhausted search without proving the existential.
- [2.9] norm_num/norm_cast: n/a, no cast computation or nontrivial numeral normalization.
- [2.10] decide: retained for the closed proposition 1<2; no native_decide or new axiom.
- [2.11] field_simp/ring: n/a, no denominator or ring-identity subgoal.
- [2.12] linear_combination: n/a, no ring/ring_nf-ending proof with hypotheses.
- [2.13] wlog: n/a, no symmetric case branches.
- [2.14] calc→term: bound chain now uses `.trans` and lt_of_le_of_lt directly.
- [2.15] close multiple goals with <;>: n/a, remaining branches have different roles.
- [3.1] erw→rw: n/a, no erw.
- [3.2] continuity/measurability→fun_prop: n/a, absent.
- [3.3] omega→lia: both removed by direct arithmetic, as [2.7].
- [3.4] rcases rfl substitution: n/a, no such destructuring.
- [3.5] automation attribute registration: no new global attribute; existential theorem
  with new witnesses is not a terminating simp normal form.
- [3.6] simp_all over simp_all only: n/a, no simp_all call.
- [3.7] maxHeartbeats removal: n/a, no existing or added limit setting.

## Step back / simplify reflection

The actual mathematical phases are degree separation, univariate nonvanishing, and
multilinear expansion plus contradiction. The latter identity has independent content
and now has a private name with arbitrary coefficient expansions. A generic one-tactic
proof was tried and did not succeed. Term-mode conversion of the entire witness proof
would obscure choice and contradiction; retaining the 13-line outline is clearer.
No source changes were made after the frozen checkpoint.

## Gates and verification

| Gate | Result | Concrete evidence |
|---|---|---|
| lake_build_file | pass | `/Users/ramin/.elan/bin/lake build Roth.GenWronskian`, exit 0; corrected target built 23s, 1838 jobs complete; owner session81592, `/private/tmp/roth-d19-inline-module.log` |
| definition_protected | pass | captured git diff changes no original def/abbrev; all three public data definitions preserved |
| theorem_statement_protected | pass | original signature/docstring byte-identical, script comparison True |
| structure_gate | pass | headline 13 proof lines; helper 9; exact same-witness conjunction explicitly protected by task |
| naming_gate | pass | no forbidden name; no rename queue needed |
| line_packing_gate | pass | all three signature rows above; max source line ≤100 |
| inequality_orientation_gate | pass | zero ≥/> occurrences in signature; bounds ≤ |
| diagnostics | pass | corrected native full-file success=true partial=false timed_out=false errors=0 failed_dependencies=[]; owner cell213, `/private/tmp/roth-d19-inline-lsp.json` |

Warnings retained: original header and protected instance warnings only. No suppression.
Parent owns the full-project build, separate LeanEval, final simplification/performance
workflow and downstream gates; no shared build was run by this worker after source freeze.
No profiling result is claimed for an unmeasured declaration; module time is not a
per-declaration timing.

Independent original proof: `/private/tmp/roth-d19-independent.lean` reproduces the ORIGINAL
26-line theorem under a distinct declaration name in source context, with no call to
Roth.exists_genWronskian_ne_zero. `lake env lean` exited 0. Its axioms are exactly
`[propext, Classical.choice, Quot.sound]`.

Exact original-type application: `/private/tmp/roth-d19-type.lean`, `lake env lean` exit 0;
explicit original quantified type specializes to the built current theorem, and
`#print axioms Roth.exists_genWronskian_ne_zero` reports exactly
`[propext, Classical.choice, Quot.sound]`. An initial private-name #print failed because
private constants require mangled kernel names; it was removed from this type check and
checked separately, rather than counting the failed invocation as a pass.

## Required 11-step checklist

- [x] Step 1 references read; native tools discovered.
- [x] Step 2 all 24 audit items recorded.
- [x] Step 2.5 five actual search methods recorded, including coverage/failure caveats.
- [x] Step 2.6 every parameter and inversion reviewed; public literature search recorded.
- [x] Step 2.7 all signature widths and arithmetic recorded.
- [x] Step 2.8 inequality scan table recorded.
- [x] Step 3 all 42 golfing rules given concrete status.
- [x] Step 4 strategy and simplification reflection completed.
- [x] Step 5a complete clean LSP, no error/dependency/timeout laundering.
- [x] Step 5b module build and all worker diff gates recorded.
- [x] Step 6a no rename required; no rename sidecar mutation.

Remaining public proposals: none. Fintype warning is deliberately retained under protected
API and no-current-caller-need conclusion. Mandatory NEW-helper fresh audit remains for
parent dispatch, separate from this original declaration's count.

Owner subsequently reported full-project build exit 0 (115.03s) and separate LeanEval
exit 0 (25.76s), with frozen source hash stable. These are owner-reported checks, not
additional worker invocations. Source revocation remains in force.

Built private helper axiom gate completed: `/private/tmp/roth-d19-helper-axioms.lean`,
`lake env lean`, exit 0. To avoid numeric private-name parsing ambiguity, this enumerates
built environment constants, selects the exact suffix, and calls Lean.collectAxioms on
the actual Name (with its numeric component intact). Output:

```text
_private.Roth.GenWronskian.0.Roth.wronskian_kronecker_eq_sum_aux:
  [propext, Classical.choice, Quot.sound]
```

Corrected candidate result: 26→16 declaration lines / 23→13 proof lines; one new private helper
15 declaration / 9 proof lines. Gates pass within the explicit protected-API task scope.
No public proposal. Corrected owner module/LSP and renewed built axiom checks pass. Separate fresh helper audit still belongs
to parent workflow and is not counted as an audited original declaration here.


## Mandatory HAVE SCAN correction and final current evidence

Owner correctly rejected the initial term-proof `have hdeg` as a no-by single-use alias.
A readability exception does not exist in the contract. Fully inlined replacement is
`/private/tmp/roth-d19-inline-block.txt`, with full source snapshot
`/private/tmp/roth-d19-inline.lean`. It has 13 proof lines, maximum width 97 codepoints,
zero headline have declarations, and no artificial by-exact wrapper.
`/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-d19-inline.lean` exited 0.
Owner applied the exact body; this worker made no repository source write after revocation.

Final SHA256: `cbd1564dda27d17e67feacd0712e035fdfd0feeeefe920d6f7603cee970bade8`.
Final headline 26→16 declaration lines / 23→13 proof lines; helper unchanged at 15/9;
source net +6 lines. Signature, docstring, bounds, nonzero conclusion, and all three
public data definitions preserved.

Corrected source gates:

- Owner module session81592 exited 0, built target 23s, 1838 jobs complete;
  `/private/tmp/roth-d19-inline-module.log`.
- Owner complete native LSP cell213: success=true, partial=false, timed_out=false,
  errors=0, failed_dependencies=[], only the same five prior warnings;
  `/private/tmp/roth-d19-inline-lsp.json`.
- Worker renewed actual built original-type/headline-axiom probe session71534 exited 0.
  Built headline depends exactly on [propext, Classical.choice, Quot.sound].
- Worker renewed actual built private-helper-axiom probe session91985 exited 0.
  Exact Name selected from built environment; helper depends exactly on
  [propext, Classical.choice, Quot.sound].
- Independent original proof remains exit0/std3; unchanged public API makes its original
  type evidence still applicable. Its proof never invokes the target theorem.

Worker scope complete: all 24/42/5/11 audit items above, no pending routine correction,
no public proposal, no source ownership, no commits/pushes. Parent full build and separate
LeanEval for this corrected source run in session22282; parent owns recording their final
outcome and the mandatory separate fresh helper audit after publication. Earlier full/eval
results above refer only to the historical superseded d2ae601… source and are not silently
reused for this final hash.
