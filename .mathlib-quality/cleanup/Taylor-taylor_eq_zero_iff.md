# `MvPolynomial.taylor_eq_zero_iff` — fresh audit

Scope: original lines 205–206, live lines 187–188, `Roth/Taylor.lean`.
Parent supplied branch `ramin-cleanup`, baseline `8585448`.
Start/frozen source SHA256: `0a6ab3437c5950f4d2e800b78f03e7a53b7ce97f6cc248c3bff71fcf00a46f22`.
Source unchanged, including signature, docstring, `[simp]`, imports and header warning.
No Git operation or full-project build performed by worker.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md; both skills, full worker contract,
and relevant style/naming sections also read. Parent scope takes priority over broad
public-wrapper deletion, docstring and API-change advice.

Result: retain the existing direct term `(taylor_injective α).eq_iff' (map_zero _)`.
Before 2 lines; after 2; saved 0. Audit issues 0; fixes 0; deferred refactoring 0;
renames none; inline comments none; existing docstring preserved verbatim.

## Full audit

| # | Item | Finding/action |
|---|---|---|
| 1 | LINT | Native complete diagnostics: success=true, partial=false, timed_out=false; no target warning. Existing line-1 copyright warning preserved. |
| 2 | HAVE SCAN | No have in the one-line term proof. |
| 3 | SET_OPTION | No target options; no resource limits added. |
| 4 | SIMP SQUEEZE | No simp in final proof. Isolated bare simp makes no progress. |
| 5 | NAMING | Descriptive snake case, canonical eq_zero_iff suffix; no forbidden abbreviation/pattern. |
| 6 | LINE PACKING | All parameters and conclusion fit on the single 89-codepoint signature line; measured table below. |
| 7 | BY PLACEMENT | Term proof has no by wrapper. |
| 8 | FORMAT | Two-space proof indentation; no blank lines, haveI/letI, semicolon or rewrite chain. |
| 9 | COMMENTS | No inline proof comments to relocate/delete. |
| 10 | DOCSTRING | Existing public one-sentence description preserved exactly. |
| 11 | VISIBILITY | Public simp API retained as required by assignment. |
| 12 | STRUCTURE | One-line proof; no conjunction or branches, well below 60-line bound. |
| 13 | MATHLIB | Generic Injective.eq_iff' already used; map_eq_zero_iff is another verified generic route. Five methods below. |
| 14 | JUNK DEF | n/a: theorem. |
| 15 | EXISTS LEMMA | n/a: no existential witness. |
| 16 | SHOW vs CHANGE | n/a: neither construct. |
| 17 | PUSH_NEG | n/a: no negation pushing. |
| 18 | GENERALISE | Five parameters audited, drop/parent probes below; no successful safe weakening. |
| 19 | INEQUALITY | No ≥/> occurrence; scan below. |
| 20 | NORMAL-FORM | Good simp orientation removes taylor from the zero predicate, introducing no RHS variable. |
| 21 | SYNTAX-GEN | OK: explicit vector and polynomial make rewrite use direct; generic map route already available. |
| 22 | IMPORT-FANOUT | n/a: no imports added. |
| 23 | CASTS | Empty diff: 0 dropped, 0 kept cross-type, 0 kept load-bearing casts. |
| 24 | INSTANCE-NAME | n/a: no instance declaration. |

Issues to fix: none. Refactoring needed: none.

## Mathlib search-status

| Method | Actual query | Evidence |
|---|---|---|
| A Lean-Finder | injective zero preserving map f x = 0 iff x = 0 | map_eq_zero_iff, EmbeddingLike.map_eq_zero_iff, map_ne_zero_iff. |
| B Loogle | Function.Injective, _ = _ ↔ _ = _ | Function.Injective.eq_iff, Function.Injective.eq_iff', iterate_add_eq_iterate, comp_eq_const_iff. |
| C LeanSearch | An injective function preserving zero maps an element to zero if and only if the element is zero | AddEquivClass.map_eq_zero_iff, map_eq_zero_iff, EmbeddingLike.map_eq_zero_iff, injective_iff_map_eq_zero'. |
| D Source | Untruncated rg taylor_eq_zero_iff over Mathlib; map_eq_zero_iff/map_eq_one_iff in Group/Hom/Defs; eq_iff' in Lean Init/Data/Function | No exact taylor name hit. map_eq_one_iff at Hom/Defs:248 generates additive map_eq_zero_iff via to_additive; generic Injective.eq_iff' at Init/Data/Function:121. |
| E Name pattern | Injective.eq_iff, limit 5 | Positive exact eq_iff and eq_iff' hits in Init/Data/Function; index warming, so no absence conclusion from index. |

Auxiliary variants: eq_iff, eq_iff', map_eq_zero_iff, map_ne_zero_iff,
EmbeddingLike.map_eq_zero_iff, injective_iff_map_eq_zero'. Common-equivalents table:
no discrete/finiteness/separation/bornology bucket match.
Conclusion: partial generic match already directly used. No new API or absence claim.
Six strict rules: generic API used; all five searches attempted; variants inspected;
no custom predicate introduced; protected public API not deleted; protected module docs
unchanged. Deletion of this established public simp API is outside the assigned scope.

## Generalisation status

| # | Parameter | Class/use | Mechanical candidates and actual result | Verified? |
|---|---|---|---|---|
| 1 | σ : Type* | type variable; domain of α and polynomial variables | Drop with autoImplicit=false: unknown σ. Already independent universe polymorphic; no stronger universe restriction to weaken. | Native isolated drop errors; original #check confirms universe. |
| 2 | A : Type* | type variable; coefficient type | Drop with autoImplicit=false: unknown A. Already independent universe polymorphic. | Native isolated drop errors; original #check confirms universe. |
| 3 | CommRing A | typeclass; taylor definition and taylor_injective | Drop: cannot synthesize CommSemiring A. Ring: cannot synthesize CommSemiring A. CommSemiring: proof cannot synthesize CommRing A for taylor_injective. | Actual prefix CLI probes exit 1; never applied to live source. |
| 4 | α : σ → A | structure value; translation vector | Drop with autoImplicit=false: unknown α in statement and proof. No point-localisation/strict-weak property applies to a data argument. | Native isolated errors. |
| 5 | P : MvPolynomial σ A | structure value; polynomial | Drop with autoImplicit=false: unknown P in statement. No point-localisation/strict-weak property applies to a data argument. | Native isolated errors. |

No proposition/decidability parameters are omitted from the table. No weakenings kept.
The CommSemiring failure establishes a dependency of this proof, not impossibility of
a different semiring theorem. No unproved mathematical impossibility is claimed.
Inversion check: generic abstract content is exactly Injective.eq_iff' (or map_eq_zero_iff),
already in the library and already applied; no missing abstract theorem to add.
Big-change candidates: none supported by a compiled replacement proof.

## Public literature search

Query 1: `polynomial translation automorphism arbitrary commutative ring generalization zero polynomial Stacks`.
First three returned hits: [On zeros of a polynomial in a finite grid](https://arxiv.org/abs/1508.06020),
[Algebra and Discrete Mathematics](https://www.mathnet.ru/links/f4f2b75b7073d83a51b344cdc69178fe/adm3.pdf),
[ring automorphism question](https://math.stackexchange.com/questions/5058339/let-r-be-a-commutative-ring-with-1-do-every-ring-automorphism-of-the-polynomial).
These are tangential; no weakening inferred from them.

Queries 2–3: `site.stacks.math.columbia.edu polynomial ring universal property` and
`site.ncatlab.org polynomial ring universal property` (batched search).
First three returned hits: [universal construction](https://ncatlab.org/nlab/show/universal+construction),
[polynomial](https://ncatlab.org/nlab/show/polynomial),
[constant polynomial](https://ncatlab.org/nlab/show/constant+polynomial).
The polynomial entry describes the free commutative algebra formulation. From that
formulation, inverse substitutions X+α and X−α explain the present ring hypothesis;
this is an inference, not a quote or proof of maximal generality. No field, domain,
finite-variable or characteristic assumption is needed in the present declaration.
ChatGPT math MCP: n/a, no such callable tool in ALL_TOOLS. Literature-driven changes: none.

## Width and inequality artifacts

Width-100 compiled reference (`/private/tmp/decl18-original.lean`, target omitted from prefix):

```lean
@audit_original : ∀ {σ : Type u_3} {A : Type u_4} [inst : CommRing A] (α : σ → A) (P : MvPolynomial σ A),
  (taylor α) P = 0 ↔ P = 0
```

| Sig line | Chars | Next signature token | Arithmetic | Action |
|---|---|---|---|---|
| 187 | 89 | none; proof body follows := | n/a: no next signature line | ok |

| # | Location | Original | Rewrite | Rename? |
|---|---|---|---|---|
| — | Entire signature and all inherited parameters | n/a: no ≥/> in Lean code | none | no _ge_/_gt_ in name |

## All 42 golfing rules

| Rule | Status |
|---|---|
| 1.1 by exact | Already direct term. |
| 1.2 by rfl | n/a: no reflexivity wrapper. |
| 1.3 rw + exact | n/a: no rw. |
| 1.4 simp + exact | n/a: no simp chain. |
| 1.5 trailing rfl | n/a: no simp/rfl. |
| 1.6 constructor | n/a: no constructor block. |
| 1.7 apply + exact | Already single direct application. |
| 1.8 by_contra! | n/a: no contradiction proof. |
| 1.9 eta reduction | n/a: no proof lambda. |
| 1.10 inline have | n/a: no have. |
| 1.11 apply + intro | n/a: no introductions. |
| 1.12 redundant show | n/a: no show. |
| 1.13 obtain | n/a: no projections. |
| 1.14 merge rw | n/a: no rewrite. |
| 1.15 terminal simp only | n/a: no simp only. |
| 1.16 nonterminal simp | n/a: no simp. |
| 1.17 dot notation | Already `(taylor_injective α).eq_iff'`. |
| 1.18 use <\| | Parentheses contain receiver or one short argument; removing them via <\| does not shorten/read better. |
| 1.19 push Not | n/a: no push_neg. |
| 1.20 existential inlining | n/a: public iff, no witness. |
| 2.1 grind | Prefix original-type CLI experiment failed with P ≠ 0 and taylor α P = 0. |
| 2.2 delete before grind | n/a: no grind in final term. |
| 2.3 simpa | `by simpa using (taylor_injective α).eq_iff (a := P) (b := 0)` compiled, longer than original; discarded. |
| 2.4 fun_prop | n/a: no analytic/topological goal. |
| 2.5 positivity | n/a: iff of equalities, no order goal. |
| 2.6 gcongr | n/a: no inequality. |
| 2.7 lia/omega | n/a: no integer/natural arithmetic. |
| 2.8 aesop | Prefix experiment failed: exhaustive search leaves taylor α P = 0 ⊢ P = 0. |
| 2.9 norm_num/norm_cast | n/a: no numeric/cast computation. |
| 2.10 decide | n/a: universally quantified arbitrary ring equality, no finite decision problem. |
| 2.11 field_simp; ring | n/a: no denominator identity. |
| 2.12 linear_combination | n/a: no ring/ring_nf proof or linear combination goal. |
| 2.13 wlog | n/a: no symmetric cases. |
| 2.14 collapse calc | n/a: no calc. |
| 2.15 multiple goals | n/a: final proof generates no tactic subgoals. |
| 3.1 erw to rw | n/a: neither tactic. |
| 3.2 fun_prop migration | n/a: neither continuity nor measurability. |
| 3.3 omega to lia | n/a: no arithmetic tactic. |
| 3.4 rcases rfl | n/a: no destructuring. |
| 3.5 automation attributes | Existing simp attribute has correct decreasing normal form; preserved. |
| 3.6 simp_all | n/a: no simp_all only. |
| 3.7 remove maxHeartbeats | n/a: no limit override. |

Step-back reflection: bare grind/simp/aesop/exact? all failed in the target-free prefix.
apply? generated only partial suggestions with unresolved premises (its experimental
output includes a synthetic incomplete-proof warning; not accepted as a proof).
No sorry exists in live target or accepted original proof. The alternative
`map_eq_zero_iff (taylor α) (taylor_injective α)` also compiled, but is longer than
the existing direct term. No replacement improves the existing proof.

## Verification gates

Actual `/Users/ramin/.elan/bin/lake build Roth.Taylor` exited 0, 1439 jobs, with existing
header warnings only. Native full-file diagnostics were complete and clean except the
preserved header warning. Isolated ORIGINALTYPE proof compiled from pretarget prefix,
excluding target and all following declarations: `/private/tmp/decl18-original.lean`.
Both its printed axioms and native lean_verify of the live target report only
`propext`, `Classical.choice`, `Quot.sound`; native trust=standard, no suspicious patterns.
Snapshot comparison reports the entire worker source diff empty.

| Gate | Result | Actual evidence |
|---|---|---|
| lake_build_file | pass | Actual module build exit 0. |
| definition_protected | pass | Empty source diff; all definitions unchanged. |
| theorem_statement_protected | pass | Empty source diff; full original-type proof compiled. |
| structure_gate | pass | One-line body, no conjunction/branches. |
| naming_gate | pass | Descriptive name; no forbidden pattern or abbreviation. |
| line_packing_gate | pass | Single signature row measured at 89 codepoints. |
| inequality_orientation_gate | pass | Zero reversed inequalities; scan table emitted. |

Overall local gates: pass. Parent full build and subsequent separate LeanEval remain
pending until parent authorizes the post-build gate. Source ownership relinquished
at freeze; report-only changes from that point onward.

## Required phase checklist

- [x] Step 1 — references read.
- [x] Step 2 — all 24 audit items recorded.
- [x] Step 2.5 — five search methods and strict rules recorded.
- [x] Step 2.6 — every parameter audited, probes and literature recorded.
- [x] Step 2.7 — complete per-line width artifact.
- [x] Step 2.8 — per-occurrence inequality artifact.
- [x] Step 3 — all 42 rules recorded.
- [x] Step 4 — alternatives tested and reflection recorded.
- [x] Step 5a — native complete diagnostics, partial=false.
- [x] Step 5b — actual build, trust, original-type and protection gates passed.
- [x] Step 6a — no rename required; sidecar untouched.
