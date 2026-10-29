from pathlib import Path
import json
D=Path(__file__).resolve().parent;N='LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine'
rd=lambda n:json.loads((D/n).read_text())
def dump(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
link=lambda n:'['+n+'](../evidence/'+N+'/'+n+')'
ph=rd('phase-checks.json');lit=rd('literature.json')
r=f'''# `{N}` — canonical290

Verdict: **BORDERLINE-needs-human**, completed assessment subject to root acceptance. Keep the exact LeanEval specification in `Roth/LeanEval.lean`; decide the upstream semantic API separately. This is an API-design judgment, not a cost judgment or an inherited verdict from Roth's theorem.

## Phase0 — baseline

The shared clean build completed2467 jobs. All17 current production source/pin hashes match its manifest, freshly checked before preparation and at freeze. Root alone executed native checks. No production source, pin, nine-import disk prefix, shared eighteen-import prefix or Git state was changed by this worker. Final project/LeanEval builds belong to root's final293 gate, not this definition's file boundary.

Evidence: {link('baseline-build.txt')}, {link('inputs.json')}, {link('fresh-final-inputs.json')}, {link('prefix-controls.json')}, {link('prefix-authorization.json')}.

## Phase1 — exact meaning and dependency scopes

Full native type: `ℝ → Prop`. The full body, with explicit input `x : ℝ`, is:

```lean
∀ ε : ℝ, 0 < ε → ∃ C : ℝ, 0 < C ∧
  ∀ (p q : ℤ), 0 < q →
    C / (q : ℝ) ^ ((2 : ℝ) + ε) < |x - (p : ℝ) / (q : ℝ)|
```

For every positive epsilon, one positive constant works uniformly for every integer numerator and every positive integer denominator. Constants may depend on x and epsilon. Exact rational approximations are included; consequently every satisfying x is irrational. There is no algebraicity hypothesis in this definition. The property expresses irrationality exponent at most2 for irrational reals; it is weaker than badly approximable, which demands a constant at exponent2 itself. The broader phrase Diophantine number sometimes means a bound at some finite exponent; this fixed2, every-epsilon predicate is more specific and must not be conflated with that usage.

The entire66-line LeanEval module and588-line Main module were read. Original replay copies just this definition into a fresh namespace, with native definitional equality `rfl`. Complete kernel body printing has no printer elision; full type/value constant inventories and standard axioms are archived. The mathematical body uses no other canonical project declaration. Its generated numeral helper `IsDiophantine._proof_1` is recorded separately rather than treated as a public project dependency.

Evidence: {link('native-type.json')}, {link('original-executed.lean.txt')}, {link('original01-receipt.json')}, {link('source-LeanEval.lean.txt')}, {link('source-Main.lean.txt')}, {link('project-dependencies.json')}.

The exact ordered canonical293 names were derived from tracked declaration-order, including private names with their defining modules; the pre-execution audit and runtime all293-present/all293-values checks passed. Direct kernel type and body consumers are precisely `LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff` and `.thueSiegelRoth`. Source statement occurrences agree. This distinguishes lexical scope, direct kernel scope, generated numeral helper, and transitive/simp closure; no claim to enumerate every external future consumer is made.

## Phase2 — size and one-line definition test

BIG: this introduces a named mathematical predicate, despite only two physical body lines and one substantive quantified formula. Semantic one-line result: **ONE-LINER WITH-EXEMPTION**.

| Exemption | Applies | Evidence |
|---|---|---|
| Avoid defeq abuse | no | No sealed computation barrier; native rfl unfolds it. |
| Avoid typeclass diamonds | no | No typeclass or instance is introduced. |
| Semantic intent / stable API | yes | Both actual consumers use the named predicate; the final theorem preserves the independent LeanEval problem statement. |

The exemption justifies a stable local API anchor; it does not automatically establish that upstream should receive this fixed2 name.

## Phase3 — exhaustive literature

All named channels were attempted; unavailable optional ask_chatgpt_math is justified n/a. Searches ran three distinct general queries plus an explicit mathlib4/lean4 API web search. Exact requests, status, response SHA256 and byte counts are archived without third-party article/search-result bodies. Query URLs carrying credentials were not retained; truncated URLs were omitted without guessing. Two concise inspection queries were repeated for fingerprinted archival; web-batch6/7 identify the actual recorded repeat responses.

| Channel | Exact query | Finding |
|---|---|---|
'''
for x in lit['channels']:r+='| '+x['channel']+' | `'+x['query']+'` | '+x['summary']+' |\n'
r+='| Optional ChatGPT math | standard form, generality, historical evolution | n/a: configured tool unavailable. |\n| Local references | clean.tex: irrationality/Roth/approximation | Sections6/7 formulate infinite integer pairs; source search archived. |\n\n'
for x in lit['sources']:r+='- ['+x['title']+']('+x['url']+'), '+x['locator']+': '+x['summary']+'\n'
r+=f'''
Literature summary: irrationality exponent/measure and Roth-type approximation are established names. The standard family allows a real exponent cutoff; fixed2 is singled out by Roth's theorem. Natural-positive and signed integer denominators are normalization choices. The reduced-rational-denominator proof uses2+epsilon>0 and is not claimed for arbitrary negative cutoff. Rational-denominator height is valid here; replacing denominator height by projective max(num,den) height would require additional x-dependent comparison, and is not claimed as a verified equivalence. Number-field, p-adic, simultaneous and weighted generalizations require different arithmetic data and are not automatic weakenings.

Evidence: {link('literature.json')}, {link('literature-local.json')}, {link('local-source-section6.tex.txt')}, {link('local-source-section7.tex.txt')}, {link('web-batch0.json')}, {link('web-batch1.json')}, {link('web-batch2.json')}, {link('web-batch3.json')}, {link('web-batch4.json')}, {link('web-batch5.json')}, {link('web-batch6.json')}, {link('web-batch7.json')}.

## Phase4a/b — generality

| Input/condition | Current | Assessment |
|---|---|---|
| x | real | Real rpow and rational approximation are essential to this specified predicate; no extraneous algebraicity assumption. |
| epsilon | every positive real | Replacing forall by exists changes the meaning to a much weaker non-Liouville condition; reject. |
| numerator | integer | Arbitrary integers are required; reduced rationals provide verified alternative presentation. |
| denominator | positive integer | Natural-positive and signed-nonzero absolute denominator presentations verified; q=0 must not be added. |
| lower constant | exists C>0 for each epsilon | Fixed C across all epsilon or epsilon=0 strengthens the property; allowing C=0 reduces the bound to irrationality and admits Liouville numbers; strict/nonstrict positive bounds are equivalent after halving. |
| cutoff2 | fixed real numeral | Parameter t gives `UniformBound t x`; full original formula recovered definitionally at t=2. |

There is no external hypothesis/typeclass to weaken mechanically. Parameterization is a genuine wider API design, natively established; it is not being called a dropped-hypothesis improvement. A new scalar cutoff affects which property callers express. The benchmark's name and exact namespace remain a stable compatibility surface.

## Phase4c — nine modern-idiom checks

| Question | Result | Concrete consequence / guard |
|---|---|---|
'''
for a,b,c in ph['modern9']:r+='| '+a+' | '+b+' | '+c+' |\n'
r+=f'''
The tested modern semantic statement is:

```lean
UniformBound t x ↔ Irrational x ∧
  ∀ {{p : ℝ}}, LiouvilleWith p x → p ≤ t
```

This uses the existing filter predicate but the equivalence proof is new. It reconstructs the integer-pair predicate using genuine mathlib operations, proves finite bounded-denominator sets, converts denominator frequency to pair infinitude, takes a positive minimum over finite exceptions, and absorbs constants across a strict exponent gap. Pair/exponent helper structure is adapted with credit from accepted canonical288 scratch `modern2-executed.lean.txt`; this is reused proof syntax for a new generic proof, not an existing mathlib Roth theorem or an inherited verdict.

Concrete verified consequences are `cutoff_mono` for s≤t and rational affine invariance (`add_rat_iff`, `mul_rat_iff` with nonzero multiplier). The complete fixed2 formula is recovered, while `rational_cutoff` proves the cutoff family at every rational, `¬UniformBound 2 0` refutes the unguarded equivalence, and `liouvilleWith_one`/`mono` explicitly test p≤1. No algebraicity was smuggled into the property.

Evidence: {link('modern3-executed.lean.txt')}, {link('modern03-receipt.json')}, {link('mathlib-inputs.json')}.

## Phase4.5 — six infrastructure risks

| Risk | Level | Evidence |
|---|---|---|
'''
for a,b,c in ph['infrastructure_risks']:r+='| '+a+' | '+b+' | '+c+' |\n'
r+='\nOverall LOW, no HIGH rows. Native rfl and failed instance-synthesis probes accompany the structural analysis; universe and CoeFun/CoeeSort probes are inapplicable to the fixed Real -> Prop signature, which introduces neither classes nor coercions.\n\n## Phase4.6 — five proof-strategy checks\n\n| Question | Applies | Assessment |\n|---|---|---|\n'
for a,b,c in ph['proofstrategy5']:r+='| '+a+' | '+b+' | '+c+' |\n'
r+=f'''
The definition itself has no proof strategy. For upstream supporting API, REFACTOR-RECOMMENDED: provide the generic filter/constant bridge once, allowing rational-affine consequences from existing LiouvilleWith invariance rather than duplicate numerator arithmetic. This is a concrete new bridge, not a claim that filters alone solve finite-exception bounds.

## Phase5 — all15 formal cells

All current / literature-standard / abstract forms were searched by Lean-Finder, Loogle, LeanSearch, full source rg and root-executed local search. The malformed free-x Loogle attempt is preserved separately; a corrected fully quantified query returned clean empty results. Local index states were error/error/warming; these do not support absence. Semantic search index revisions differ from this pin; positive candidate signatures were independently checked against pinned sources and native checks.

| Form | Finder | Loogle | LeanSearch | rg | local |
|---|---|---|---|---|---|
'''
for f in ['current','standard','abstract']:r+='| '+f+' | '+' | '.join(link('formal-'+f+'-'+m+('-retry'if f=='current'and m=='loogle'else'')+'.json')for m in ['leanfinder','loogle','leansearch','rg','local'])+' |\n'
r+=f'''
Closest API is `LiouvilleWith`, especially `exists_pos`, `mono`, `frequently_lt_rpow_neg`, `irrational`, `add_rat_iff`, `mul_rat_iff`. `Liouville` only asks arbitrarily strong approximation; its negation is insufficient for cutoff2. `Dioph`/`DiophFn` concern integer-polynomial representability, an unrelated same-word collision. `ae_not_liouvilleWith` is a measure-almost-everywhere statement, not this pointwise definition or Roth's algebraic result. The generic exact? probe before introducing the new bridge does not close its equivalence. Full-name grep is untruncated. Search conclusion: partial API match, no verified exact existing definition; it is not proof of global absence.

Evidence: {link('formal-search-matrix.json')}, {link('full-name-search.json')}, {link('mathlib-source-0.lean.txt')}, {link('mathlib-source-1.lean.txt')}, {link('mathlib-source-2.lean.txt')}, {link('mathlib-source-3.lean.txt')}.

## Phase5.5 — statement shape

| Check | Result | Evidence |
|---|---|---|
'''
for a,b,c in ph['statement_shape3']:r+='| '+a+' | '+b+' | '+c+' |\n'
r+=f'''
Native exact alternatives cover natural-positive denominators; signed q≠0 with absolute denominator, including negative q; strict versus nonstrict positive bounds using C/2; and reduced rational denominator height r.den. None is an unproved name analogy. Overall RESTATE-BEFORE-SHIP concerns upstream API choice; the benchmark-compatible statement stays intact.

Evidence: {link('shape2-executed.lean.txt')}, {link('shape02-receipt.json')}.

## Phase6.0 — full actual callers and inline audit

| Caller | Source | Explicit occurrences | Current role | Refactor action |
|---|---|---|---|---|
| LeanEval...isDiophantine_iff | LeanEval:42–57 |1 statement| Uniform bound vs infinite-pair cutoff | Keep full signature; define bridge through generic t=2 only if upstream API chosen. |
| LeanEval...thueSiegelRoth | LeanEval:61–64 |1 statement| Benchmark endpoint | Keep namespace, x and both original assumptions; recover exact bound from any modern endpoint using the irrationality input. |

Both have direct kernel type and body dependencies; there are no additional production source consumers. A complete original LeanEval module replay, with namespace substitution only, verifies full original caller proof bodies including the private helper and preserves signatures modulo native rfl. Both replayed caller types/values are free of the original target. Inlining here is the mathematically identical expanded formula behind the fresh definition; it establishes compatibility, not a replacement theorem from existing mathlib.

Evidence: {link('source-search.json')}, {link('tracked-source-search.json')}, {link('inline-search.json')}, {link('callers.json')}, {link('callers-executed.lean.txt')}, {link('callers01-receipt.json')}.

## Phase6 — composition and moral duplication

The quantified arithmetic formula can be pasted at both caller statements without changing their proofs, but naming it records semantic intent and benchmark compatibility. Existing LiouvilleWith alone does not define the same property: omitting irrationality provably changes rational cases. Obtaining the exact uniform-bound equivalence requires new finite-exception and exponent-gap proofs, not≤3 existing mathlib calls. The affine consequence proofs compose only after this new bridge; they cannot be represented as existing-mathlib replacements for the definition. Composition conclusion: NOT-COMPOSABLE from verified existing semantic API in≤3 calls. Moral overlap with Roth.approxSet is a genuinely proved alternate presentation, not definitional identity. No junk/dead-code diagnosis follows from the short body; both real callers depend on the stable predicate.

## Phase7 — verdict and actionable future questions

BORDERLINE-needs-human. The predicate is mathematically standard in its benchmark context and its one-line semantic exemption is real. The verified family exposes reusable cutoff monotonicity and rational-affine invariance. Choosing whether mathlib should add a named lower-bound family, simply use an irrationality conjunct plus the existing exponent predicate, or add only their bridge is an upstream API decision. This crosses a foundational interface, so it is not asserted to be a single dropped-hypothesis edit. No verdict is inherited from the enclosing Roth theorem and no cost/time criterion is used.

1. Should upstream introduce a named parameterized predicate `UniformBound (t x : ℝ) : Prop`, or keep `Irrational x ∧ ∀ {{p}}, LiouvilleWith p x → p ≤ t` as its canonical expression?
2. If a named predicate is wanted, should it use natural-positive denominators, with integer/signed/rational formulations supplied only as equivalence lemmas?
3. Should the fixed2 `IsDiophantine` name remain solely in the LeanEval compatibility module while the generic bridge and invariance API live upstream?

These are concrete future upstream questions, not unresolved assessment work or a request to stop the project. Preserve `Roth/LeanEval.lean` as the local destination. A candidate home for the eventual bridge/family is `Mathlib/NumberTheory/Transcendental/Liouville/Diophantine.lean`, importing LiouvilleWith. Recent related-file commit evidence is retained for a future reviewer decision; no YES PR grouping is claimed. Evidence: {link('reviewer-commits.json')}.

## Phase8 — verification and handoff

Accepted exact sources and raw root-native requests/results, rejected attempts, elapsed times, standard axioms, exact293 audit, all17 hashes and portable manifest/layout/secret gates are indexed in {link('verification.json')}. Failed modern01, modern02 and shape01 are retained separately and not counted as accepted proof evidence; their recovered sorryAx is rejected. Accepted receipts must contain no PANIC even in info diagnostics. Current-manifest validation applies in scratch and integrated layouts; historical worker manifests never replace it. Production sources/pins remain unchanged. Root acceptance is pending.
'''
r='\n'.join(l.rstrip()for l in r.splitlines()).rstrip()+'\n';(D/'report.md').write_text(r)
dump('overview-entry.json',dict(type='ℝ → Prop',kind='def',what='Uniform positive strict rational-approximation lower bound at every exponent2+epsilon; includes exact approximants and therefore implies irrationality.',how='Quantified arithmetic predicate; no proof. Native generic bridge uses bounded-denominator finiteness, positive finite minimum and exponent-gap absorption.',hypotheses=['x : ℝ; no algebraicity or external irrationality assumption'],project_dependencies=[],caller_summary=rd('callers.json'),mathlib_api_audit=dict(closest='LiouvilleWith',exact_replacement=False,warning='Must retain irrationality conjunct; rational cutoff family holds while IsDiophantine fails.'),moral_duplications=['Related to Roth.approxSet infinitude cutoff through a substantive bridge, not defeq.'],generalization=dict(proposed_type='(t x : ℝ) → Prop',proposed_body='∀ ε : ℝ, 0 < ε → ∃ C : ℝ, 0 < C ∧ ∀ p q : ℤ, 0 < q → C / (q : ℝ) ^ (t + ε) < |x - (p : ℝ) / q|',modern_type='UniformBound t x ↔ Irrational x ∧ ∀ {p : ℝ}, LiouvilleWith p x → p ≤ t',verified=True,consequences=['cutoff_mono','add_rat_iff','mul_rat_iff'],recovery='UniformBound 2 is definitionally the complete original formula'),missing_api=['Uniform-bound iff irrationality-conjoined LiouvilleWith exponent cutoff; scratch proof new, not existing mathlib.'],junk='Keep stable LeanEval compatibility predicate; two actual consumers.',action='BORDERLINE: resolve3 concrete upstream API questions; keep production unchanged.'))
print('Report and exact overview keys authored')
