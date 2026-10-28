from pathlib import Path
import json,hashlib,re,shutil
D=Path(__file__).parent;N='Roth.pow_rootMultiplicity_le'
def rd(n):return json.loads((D/n).read_text())
def save(n,x): (D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def result(r):z=r['result']['structuredContent'];return z.get('result',z)
for p in Path('/private/tmp/roth-overview').glob('root-bound197-*'):
 if p.is_file():shutil.copy2(p,D/p.name)
ph=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
save('assessment.json',dict(declaration=N,canonical_index=197,verdict='YES-but-generalise-first',completed=True,allphases='PASS',phases=dict.fromkeys(ph,'PASS'),unresolved=[],root_acceptance='pending'))
v=dict(declaration=N,standard_axioms=['propext','Classical.choice','Quot.sound'],unresolved=[],accepted=[],rejected=[],canonical_direct_consumers=['_private.Roth.Theta.0.Roth.index_unique_le_log_div'],canonical_direct_type_consumers=[],audit=dict(source='root-bound197-original-executed.lean.txt',receipt='root-bound197-original-receipt.json',marker='ROOTBOUND197',native_region_start_line=15),composition=dict(strict_three_existing_call_term_verified=False,parent_project_helpers_counted_as_mathlib_blocks=False,no_global_absence_claim=True,exact_search_timeout_is_absence_evidence=False,experiments=['pow_rootMultiplicity_dvd wrong output','leadingCoeff_dvd applied to field factor misses integral denominator bridge','den_dvd_of_is_root order1/chosen denominator','Gauss+coefficient+Int bound requires primitive-power and map normalization']))
reqs={'original':['ROOTBOUND197_FULL_TYPE:','ROOTBOUND197_AUDIT: requested=293; unique=293','ROOTBOUND197_AUDIT_PRESENT: present=293; values=293'], 'project':["'Bound197.no_pos' depends on axioms:","'Bound197.no_nonzero_counter' depends on axioms:"], 'isolated':["'Bound197Generic.denominator_dvd' depends on axioms:","'Bound197Generic.signed_bound' depends on axioms:","'Bound197Generic.original_no_pos' depends on axioms:"], 'stronger':['[inst : Ring L]',"'Bound197Guards.coprime_necessary' depends on axioms:","'Bound197Guards.arbitrary_coefficients_fail' depends on axioms:","'Bound197Guards.zero_denominator_divisibility_fails' depends on axioms:"], 'fullcaller':['[inst : Ring L]',"'Bound197Caller.fullcaller' depends on axioms:"], 'positive':['den_dvd_of_is_root','one_le_pow_mul_abs_eval_div','Int.natAbs_le_of_dvd_ne_zero']}
for label in reqs:
 src='root-bound197-'+label+'-executed.lean.txt';rec='root-bound197-'+label+'-receipt.json';raw='code' in rd(rec)['request'];v['accepted'].append(dict(label=label,source=src,source_sha256=sha(D/src),receipt=rec,format='raw' if raw else 'disk',native_region_start_line={'original':15,'project':344,'fullcaller':344,'positive':18}.get(label,16),required_info=reqs[label]))
for p in sorted(D.glob('*rejected*-receipt.json')):
 src=p.name.replace('-receipt.json','-executed.lean.txt');z=result(rd(p.name));msgs=[x['message'] for x in z.get('diagnostics',z.get('items',[])) if x.get('severity') in ['error','warning']];v['rejected'].append(dict(source=src,source_sha256=sha(D/src),receipt=p.name,reason='; '.join(msgs),accepted_as_proof=False))
save('verification.json',v)
z=result(rd('root-bound197-stronger-receipt.json'));msgs=z['diagnostics'];save('generic-native-type.json',dict(native_messages=[x['message'] for x in msgs if x['message'].startswith('@denominator_dvd') or x['message'].startswith('@signed_bound')]))
save('overview-entry.json',dict(kind='theorem',type=rd('native-type.json')['type'],what='Reduced rational-root denominator to its multiplicity is bounded by absolute integer polynomial leading coefficient, hence by B.',how='Primitive linear-factor descent through Gauss lemma, compare nonzero integer leading coefficients and cast.',hypotheses=['R≠0','q>0 (removable numerically)','IsCoprime h ↑q (IsRelPrime equivalent over ℤ)','absolute leading coefficient≤B'],project_dependencies=['Roth.exists_eq_pow_mul_of_rootMultiplicity'],caller_summary='One explicit within-file caller: private Roth.index_unique_le_log_div at Theta:245; zero outside file; canonical1value/0type.',mathlib_api_audit='Related pow_rootMultiplicity_dvd, Gauss descent, leadingCoeff_dvd_leadingCoeff, den_dvd_of_is_root and Int.natAbs_le_of_dvd_ne_zero verified; no exact retrieved replacement.',moral_duplications='Rational root theorem with multiplicity; determinant coefficient proofs reuse integer discreteness but do not rederive this bound.',generalization='Verified signed integer denominator, no positivity, Ring L ordered target, direct abs lc bound; separate GCD-domain/fraction-field denominator-power divisibility for q≠0. IsRelPrime strictly generalizes Bézout condition only in generic coefficient domains; numerical law retains ℤ coefficients.',missing_api='Generic multiplicity integral-linear-factor descent and denominator-power leading-coefficient divisor; numeric discrete-order corollary.',junk=False,action='YES-but-generalise-first; group accepted196 factor theorem, algebraic divisor and ordered integer bound; generalise and cleanup before PR.'))
p=D/'report.md';s=p.read_text().replace('`Mathlib/RingTheory/Polynomial/RationalRoot.lean:106`','`Mathlib/RingTheory/Polynomial/RationalRoot.lean:89`').replace('`Polynomial.leadingCoeff_pow`, same module,','`Polynomial.leadingCoeff_pow`, same module:717,').replace('`Mathlib/Algebra/Polynomial/DenomsClearable.lean`:','`Mathlib/Algebra/Polynomial/DenomsClearable.lean:86`:')
s=s.replace('The two private primitivity helpers193–195','The two private primitivity helpers194–195')
s=s.replace('Weaken to `IsRelPrime h q`; only primitive-factor reducedness matters.','Use `IsRelPrime h q`; it is equivalent to `IsCoprime` over ℤ, while genuinely weaker over general GCD domains. Only primitive-factor reducedness matters.')
s=s.replace('weakens coprimality, permits signed denominators','uses relative primality (equivalent over ℤ), permits signed denominators')
s=s.replace('relative primality, no positivity','relative primality (equivalent reducedness over ℤ), no positivity')
needle='The numerical statement and original specialization are in'
code='''The independently checked numerical statement is:

```lean
theorem Polynomial.abs_pow_rootMultiplicity_le_abs_leadingCoeff
    {L : Type*} [Ring L] [LinearOrder L] [IsStrictOrderedRing L]
    {R : Polynomial ℤ} (hR : R ≠ 0) {h q : ℤ} (hcop : IsRelPrime h q) :
    |(q : L)| ^ Polynomial.rootMultiplicity ((h : ℚ) / q)
      (R.map (Int.castRingHom ℚ)) ≤ |(R.leadingCoeff : L)|
```

Removing the `B` envelope is equivalent conclusion packaging, not additional arithmetic content. Relative primality is equivalent to Bézout coprimality over ℤ; its strict weakening is in the arbitrary GCD-domain algebraic statement. Ordered target generalization changes the comparison codomain only, preserving integer coefficients.

'''
s=s.replace(needle,code+needle);p.write_text(s)
print('metadata ready')
