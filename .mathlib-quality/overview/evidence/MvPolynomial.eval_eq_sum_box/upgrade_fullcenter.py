from pathlib import Path
import json,hashlib,shutil
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth');N=D.name
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def load(n):return json.loads((D/n).read_text())
def out(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
for suffix in ['success.json','executed.lean.txt']:shutil.copy(Path('/private/tmp/roth-overview')/f'taylor-evaluated-fullcenter-{suffix}',D/f'native-fullcenter-{suffix}')
v=load('verification.json');s=D/'native-fullcenter-executed.lean.txt';v['accepted'].append(dict(label='fullcenter',source=s.name,source_sha256=sha(s),receipt='native-fullcenter-success.json'));v['scope']+=' Strongest verified form: coefficient CommSemiring A, CommRing A-algebra B, both center/point B-valued; degree map transport, hasseDeriv_map and evaluation-map compatibility; original arbitrary equality instance recovery plus full Main estimate third time.';out('verification.json',v)
g=load('generality.json');g['verified']='[CommSemiring A] [CommRing B] [Algebra A B] [Fintype σ], α x : σ → B; scoped Classical box';g['widened']='Both center and evaluation point in arbitrary independent-universe CommRing A-algebra B; coefficient A weakens from CommRing to CommSemiring';g['full_center_validated']=True;g['coefficient_semiring_validated']=True;g['full_center_recovery_caller_validated']=True;g['ring']='Difference form requires CommRing in target B; coefficient A only CommSemiring. Same-ring A=B original remains CommRing. No unsupported unrestricted noncommutative generalisation.';g['proof']='Map P along algebraMap A B; support_map_subset transports degree bound; same-ring fresh evaluation over B plus hasseDeriv_map and eval₂_eq_eval_map yield aeval formula.';g['intermediate']='Earlier verified center-in-A algebra target remains useful intermediate, not claimed maximal.';out('generality.json',g)
a=load('assessment.json');a['reason']='MODERN-IDIOM/LITERATURE-WEAKENING: exact multivariate Hasse evaluation gap; verified coefficient CommSemiring A, arbitrary CommRing A-algebra B with BOTH center/point B-valued, no explicit DecidableEq. Original recovered propositionally and full Main estimate checked.';out('assessment.json',a)
e=load('overview-entry.json');e['caller_summary']='1 explicit external-to-file caller Roth.abs_eval_lt_of_le_index at Main390; full estimate/private product-weight helper checked against fresh scalar recovery, intermediate algebra-target recovery and strongest B-valued center/point recovery (three full estimate replays).';e['generalization']='Strongest verified: coefficient CommSemiring A, arbitrary independent-universe CommRing A-algebra B, BOTH α/x : σ→B, aeval α derivative values. No explicit DecidableEq via scoped Classical; original CommRing A=A/arbitrary instance recovered propositionally by Subsingleton.elim/cases. Degree bound after coefficient map proved by support_map_subset; uses hasseDeriv_map and eval₂_eq_eval_map. Fintype, natural exponents and degree bound retained. Earlier center-in-A algebra law is intermediate.';e['action']='YES-but-generalise-first: propose Mathlib/Algebra/MvPolynomial/Taylor.lean with coefficient-CommSemiring/arbitrary-ring-algebra-target B-valued center/point/no-explicit-DecidableEq theorem and original recovery; group with accepted finite expansion/coefficient/Hasse foundations. Sources unchanged; full Taylor milestone build clean2467 jobs.';e['how']+=' Strongest scalar-extension form additionally transports degree via support_map_subset and Hasse evaluation via hasseDeriv_map/eval₂_eq_eval_map.';out('overview-entry.json',e)
s=(D/'report.md').read_text()
s=s.replace('four successful native sets','five successful native sets')
s=s.replace('No field/domain/CharZero needed; subtraction/inverse transport means unqualified CommSemiring replacement changes this displayed form.','No field/domain/CharZero needed. Same-ring difference form stays CommRing; in the verified scalar-extension form coefficient A only needs CommSemiring, while target B remains CommRing.')
s=s.replace('Verified widen to x : σ→B for arbitrary CommRing B with Algebra A B; evaluate with aeval, map derivative values/center through algebraMap. Original recovered at B=A.','Verified widen BOTH α/x to σ→B for arbitrary CommRing A-algebra B; coefficients A may be CommSemiring. Evaluate P and its Hasse derivatives with aeval. Original recovered at B=A.')
s=s.replace('Arbitrary, including zero; do not require nonzero or distinct coordinates.','Arbitrary, including zero; strongest verified form allows α : σ→B, including centers outside the image of A. No nonzero or distinct-coordinate requirement.')
start=s.index('**STRICTLY NARROWER THAN STANDARD / MODERN IDIOM:')
end=s.index('## Phase 4c',start)
s=s[:start]+'''**STRICTLY NARROWER THAN STANDARD / MODERN IDIOM.** The strongest verified restatement removes explicit DecidableEq, weakens coefficients from CommRing A to **CommSemiring A**, and allows **both center and evaluation point in an arbitrary commutative ring A-algebra B**. Original CommRing A=B and arbitrary supplied equality decision recover **propositionally, not definitionally** via Subsingleton.elim/cases. The full original Main estimate passes from this recovery as well as the two earlier recovery routes. Cost MODERATE but mechanical: coefficient-map degree transport plus Hasse-map/evaluation compatibility, with no new mathematical foundation.

Recommended signature (complete accepted proof is archived):

```lean
open Classical in
theorem target {σ A B : Type*} [CommSemiring A] [CommRing B] [Algebra A B] [Fintype σ]
    (α x : σ → B) (r : σ → ℕ) (P : MvPolynomial σ A)
    (hP : ∀ j, degreeOf j P ≤ r j) :
    aeval x P = ∑ d ∈ Roth.box r, aeval α (hasseDeriv d P) *
      ∏ j, (x j - α j) ^ d j
```

The proof maps P along algebraMap A B. Its degree bound follows from support_map_subset, degreeOf_le_iff and monomial_le_degreeOf; apply the already verified same-ring evaluated formula over B, then hasseDeriv_map and eval₂_eq_eval_map identify each evaluated derivative. No injectivity of algebraMap is assumed: coefficient maps can only remove support, which suffices for the bound. Independent universes are retained. The earlier verified center-in-A/algebraMap-valued formula is an **intermediate**, not falsely declared maximal. [Structured generality](../evidence/MvPolynomial.eval_eq_sum_box/generality.json).

'''+s[end:]
s=s.replace('Original already CommRing, broader than real/field literature. No verified subtraction-free same-conclusion form. Target algebra widening is separate from weakening CommRing.','Original already CommRing, broader than real/field literature. Strongest verified scalar-extension form weakens coefficient A to CommSemiring while preserving CommRing in target B for differences. This is an actual checked weakening, not an unsupported subtraction-free same-ring claim.')
s=s.replace('Proposed arbitrary A-algebra evaluation uses the existing `aeval` and avoids first mapping P into its evaluation target.','Recommended arbitrary ring A-algebra evaluation allows BOTH center and point in B and uses existing `aeval`; its proof maps coefficients once and transports degrees/Hasse derivatives. Users need not manually map P to state or invoke the formula.')
s=s.replace('The current theorem is the self-algebra specialization.','Both center and point may range over B, and coefficients A need only be CommSemiring. The current theorem is the self-algebra CommRing specialization.')
s=s.replace('Generalise the target and suppress extraneous equality-decision input before upstream submission;','Generalise both center/point and the coefficient ring hierarchy, and suppress extraneous equality-decision input before upstream submission;')
s=s.replace('Cost CHEAP for the verified same-form binder change and algebra-target transport.','Cost CHEAP for same-form binder removal, MODERATE for strongest coefficient-map degree/Hasse transport; no cost-based omission of the broader verified form.')
s=s.replace('An arbitrary-algebra theorem should use aeval with coefficient values mapped by algebraMap;','The strongest arbitrary-algebra theorem uses aeval at both B-valued center and point with coefficient A only CommSemiring;')
s=s.replace('CommRing needed for this difference-form interface, Fintype for box/full product','CommRing needed in the target for differences; coefficient CommSemiring is verified sufficient in the widened form. Fintype is needed for box/full product')
s=s.replace('**Four accepted native sets**','**Five accepted native sets**')
needle='One algebra preparation contained only a long rewritten-line style warning'
pos=s.index(needle)
s=s[:pos]+'''- [Strongest full-center exact fragment](../evidence/MvPolynomial.eval_eq_sum_box/native-fullcenter-executed.lean.txt), [receipt](../evidence/MvPolynomial.eval_eq_sum_box/native-fullcenter-success.json): coefficient CommSemiring A, arbitrary independent-universe CommRing A-algebra B, BOTH α/x B-valued, no explicit DecidableEq. Full proof transports coordinate-degree bounds by support_map_subset and uses hasseDeriv_map/eval₂_eq_eval_map. Original arbitrary-equality-instance statement recovered, and **full Main estimate replayed a third time** using this strongest recovery. Complete clean success first try, standard axioms; no new rejected preparation.

'''+s[pos:]
s=s.replace('**YES-but-generalise-first: remove the explicit equality-decision requirement and expose arbitrary commutative algebra evaluation.**','**YES-but-generalise-first: remove explicit equality-decision input, weaken coefficients to CommSemiring A, and allow both center and point in any CommRing A-algebra B.**')
s=s.replace('Expose the stronger aeval theorem; recover scalar evaluation at B=A,','Expose the strongest B-valued center/point aeval theorem with coefficient CommSemiring; recover original scalar evaluation at CommRing A=B=A,')
s=s.replace('**verified** arbitrary-algebra/no-explicit-DecidableEq signature','**verified strongest** coefficient-CommSemiring/B-valued-center-and-point/no-explicit-DecidableEq signature')
s=s.replace('and CommRing assumptions in this form.','and CommRing assumption in target B; coefficient A only needs CommSemiring.')
(D/'report.md').write_text(s)
# Refresh all source/pin hashes before the new freeze.
m=load('inputs.json')
for x in m:assert sha(R/x['path'])==x['sha256']==x['baseline_sha256']
