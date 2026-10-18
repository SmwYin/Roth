# Separation — completed file cleanup

Baseline a39317e; final source SHA256 df4193795f1618f8f5cdbd71869583fc45d20a0a45c21f4b5eaf5f824133f37a.
Original 618 → final 556 lines (−62, −10.0%). All 30 originals audited by distinct fresh
Sol Medium declaration workers. 27 retained declarations: one definition, 19 public
theorems, one original private lemma and six added private proof helpers. Nine original
private wrappers removed; all eight historical helper additions received distinct fresh
independent audits (six retained,two subsequently removed). After successful final
publication: overall 181/264 original declarations and 9/14 files complete.

## Phases 0–5: scope, audits and refactoring

Baseline full build and complete native LSP passed; baseline 32 warnings reduced to 2.
Every original declaration received all 24 audit items, 42 golf rules,five actual Mathlib
search methods,effective-binder/generalisation probes,literature evidence for public
results,signature packing,inequality scan and 11 completion steps. Each declaration
checkpoint passed independent owner gates and was pushed before the next source edit.
Public-hypothesis revisits followed the same separate sequential cadence. Bounded failed
remote/index searches were recorded as unavailable rather than mathematical absence;
source search and actual compiler checks supplied fallbacks. No phase was silently skipped.

Proof changes replace support,degree,polynomial evaluation,determinant and gcd wrappers
with existing APIs. Substantive stages of basis separation,primitive factor construction
and rational determinant factorisation are private lemmas. All four module headline
proofs meet the 15-line target: exists_separated_representation: 14,
det_hasseDeriv_separated: 10,exists_int_factors: 15,exists_det_eq_mul: 11.
Every other retained proof is at most 30 physical body lines; no branch/structure flag
remains. Correlated existential outputs require shared witnesses, so splitting them into
independent existential conjuncts would lose the usable witness relationship. Fixed-factor
facts instead recombine directly; one proposed conjunction-bundle helper was removed.

Original block documentation (all 21 comments/docstrings) is byte-identical. No original
inline proof narratives existed or were removed. Every line is at most 100 codepoints.
The six final imports replace LinearCombination with Polynomial.Eval.Subring; Mathlib and
project import groups are separated. The defining value and public type of coeffNone are
unchanged. Header metadata remains unchanged by explicit user decision.

### Original declaration inventory and dedicated audits

| # | Original declaration | Final disposition |
|---|---|---|
| 1 | [mapDomain_some_none](Separation-mapDomain_some_none.md) | Deleted duplicate private wrapper |
| 2 | [eq_mapDomain_some_add_single](Separation-eq_mapDomain_some_add_single.md) | Retained; full audit complete |
| 3 | [some_mapDomain_add_single](Separation-some_mapDomain_add_single.md) | Deleted duplicate private wrapper |
| 4 | [mapDomain_add_single_none](Separation-mapDomain_add_single_none.md) | Deleted duplicate private wrapper |
| 5 | [coeff_X_none_pow_mul_rename](Separation-coeff_X_none_pow_mul_rename.md) | Retained; full audit complete |
| 6 | [coeffNone](Separation-coeffNone.md) | Retained; full audit complete |
| 7 | [coeff_coeffNone](Separation-coeff_coeffNone.md) | Retained; full audit complete |
| 8 | [eq_sum_X_none_pow_mul_coeffNone](Separation-eq_sum_X_none_pow_mul_coeffNone.md) | Retained; full audit complete |
| 9 | [degreeOf_coeffNone_le](Separation-degreeOf_coeffNone_le.md) | Retained; full audit complete |
| 10 | [coeff_rename_mul_aeval](Separation-coeff_rename_mul_aeval.md) | Retained; full audit complete |
| 11 | [aeval_X_eq_rename](Separation-aeval_X_eq_rename.md) | Retained; full audit complete |
| 12 | [degreeOf_none_rename_some](Separation-degreeOf_none_rename_some.md) | Deleted duplicate private wrapper |
| 13 | [degreeOf_aeval_X_none_of_ne](Separation-degreeOf_aeval_X_none_of_ne.md) | Deleted duplicate private wrapper |
| 14 | [rename_some_ne_zero](Separation-rename_some_ne_zero.md) | Deleted duplicate private wrapper |
| 15 | [aeval_X_none_ne_zero](Separation-aeval_X_none_ne_zero.md) | Deleted duplicate private wrapper |
| 16 | [hasseDeriv_rename_mul_aeval](Separation-hasseDeriv_rename_mul_aeval.md) | Retained; full audit complete |
| 17 | [coeff_uniqueAlgEquiv_symm](Separation-coeff_uniqueAlgEquiv_symm.md) | Retained; full audit complete |
| 18 | [degreeOf_uniqueAlgEquiv_symm](Separation-degreeOf_uniqueAlgEquiv_symm.md) | Retained; full audit complete |
| 19 | [degreeOf_rename_mul_aeval](Separation-degreeOf_rename_mul_aeval.md) | Retained; full audit complete |
| 20 | [degreeOf_none_rename_mul_aeval](Separation-degreeOf_none_rename_mul_aeval.md) | Retained; full audit complete |
| 21 | [exists_separated_representation](Separation-exists_separated_representation.md) | Retained; full audit complete |
| 22 | [det_hasseDeriv_separated](Separation-det_hasseDeriv_separated.md) | Retained; full audit complete |
| 23 | [exists_sum_mul_eq_gcd](Separation-exists_sum_mul_eq_gcd.md) | Retained; full audit complete |
| 24 | [exists_nat_smul_eq_map](Separation-exists_nat_smul_eq_map.md) | Retained; full audit complete |
| 25 | [exists_primitive_smul_eq](Separation-exists_primitive_smul_eq.md) | Retained; full audit complete |
| 26 | [exists_int_eq_of_gcd_eq_one](Separation-exists_int_eq_of_gcd_eq_one.md) | Retained; full audit complete |
| 27 | [map_aeval_X_none](Separation-map_aeval_X_none.md) | Deleted duplicate private wrapper |
| 28 | [degreeOf_map_intCast](Separation-degreeOf_map_intCast.md) | Deleted duplicate private wrapper |
| 29 | [exists_int_factors](Separation-exists_int_factors.md) | Retained; full audit complete |
| 30 | [exists_det_eq_mul](Separation-exists_det_eq_mul.md) | Retained; full audit complete |

### Added-helper independent audits

| Helper | Dedicated fresh audit | Disposition |
|---|---|---|
| linearIndependent_coordinate_polynomials_aux | [Audit](Separation-helper-linearIndependent_coordinate_polynomials_aux.md) | Retained;23 body lines |
| eq_sum_aeval_basis_coeffNone_aux | [Audit](Separation-helper-eq_sum_aeval_basis_coeffNone_aux.md) | Retained;16 body lines |
| degreeOf_mem_coeffNone_span_aux | [Audit](Separation-helper-degreeOf_mem_coeffNone_span_aux.md) | Audited then replaced with restrictSupport API |
| exists_coeffNone_basis_aux | [Audit](Separation-helper-exists_coeffNone_basis_aux.md) | Retained;21 body lines |
| rescale_separated_factor_aux | [Audit](Separation-rescale_separated_factor_aux.md) | Retained;private Field generality;final2 body lines |
| exists_int_polynomial_of_primitive_factor_aux | [Audit](Separation-exists_int_polynomial_of_primitive_factor_aux.md) | Retained;8 body lines via mem_map_range |
| int_factorization_eq_aux | [Audit](Separation-int_factorization_eq_aux.md) | Audited then inlined;headline remains15 lines |
| exists_rat_factors_det_hasseDeriv_aux | [Audit](Separation-exists_rat_factors_det_hasseDeriv_aux.md) | Retained;Finite assumption;20 body lines |

### Approved API menu and closed alternatives

The exact 12-theorem τ-instance menu was explicitly approved and fully applied: both
Fintype and DecidableEq removed from eq_mapDomain_some_add_single,coeff_coeffNone,
eq_sum_X_none_pow_mul_coeffNone,degreeOf_coeffNone_le,coeff_rename_mul_aeval,
hasseDeriv_rename_mul_aeval,degreeOf_rename_mul_aeval,degreeOf_none_rename_mul_aeval,
exists_separated_representation,det_hasseDeriv_separated and exists_int_factors;
ONLY DecidableEq removed from exists_det_eq_mul,whose Fintype is deliberately retained.
No external caller edit was needed. All other public coefficient,nonzero,degree and
witness contracts and all public names remain unchanged.

The user considered and declined deleting aeval_X_eq_rename and coeff_uniqueAlgEquiv_symm
and widening the two product-degree coefficient domains to CommSemiring/NoZeroDivisors.
Those APIs/hypotheses remain. The separate compiled optional gcd-wrapper deletion and
arbitrary-Ring integer-witness enhancement were not approved or applied; retention during
this cleanup was recommended. They are optional assessed alternatives,not required input
or unfinished proof work. The Nat codomain remains. Separation has no rename pending.
The shared project-end Index rename queue remains intentionally assigned to the parent:
index_hasseDeriv_ge → index_sub_weight_le_index_hasseDeriv; not falsely reported as applied.

## Phase 6: cumulative gates

All leaf/reviewer source ownership was revoked and requests drained before final owner
checks. The final owner mechanical scan also normalized three remaining ordinary lambda
arrows; valid conv_lhs => syntax is retained. Every affected final check below was refreshed
after that syntax-only adjustment. Earlier pre-normalisation successful logs remain
preserved and are not substituted for final-source gates.

| Gate | Successful final-source evidence |
|---|---|
| lake_build_file / lake_build | Fresh reviewer module build passed; owner sequential full lake build exit0 in38.96s, then separate lake build Roth.LeanEval exit0 in51.62s. Root excludes LeanEval. /private/tmp/roth-separation-final-current-{full,leaneval}.log and -builds.json; source hash stable. |
| independent original proofs / public contracts | Fresh compiler exit0 in98.12s; /private/tmp/roth-separation-final-current-compatibility.lean/.log/.json. Whole original30 independently re-proved including all deleted private wrappers; not certified by merely invoking replacements. All20 original public type/value recoveries compile using only the exact approved instance adapters; coeffNone value equality rfl. |
| actual standard axioms | Same probe checks ALL 27 actual retained public/private constants, suffix-locating private names. Only propext,Classical.choice,Quot.sound. No new axiom,sorry,native_decide or resource-limit change. |
| full Theta compatibility | Fresh compiler exit0 in51.15s; /private/tmp/roth-separation-final-current-theta-all-compatibility.lean/.log. Independently re-proves FULL ORIGINAL Index+Theta and checks all 29 original Theta public type/value equalities plus actual standard axioms. Theta source unchanged from a39317e. |
| complete cumulative LSP | All6 actual files complete,success=true,partial=false,timed_out=false,no failed dependencies,no errors. Final-current-lsp.json supplies Separation/Theta; final-current-lsp-repeat.json supplies four complete downstream responses. Earlier timeout/partial responses explicitly excluded. |
| documentation / structure / width / trust | Final-current-static.json: all 30 reports present,all 21 original block docs identical,all lines≤100,inline narratives0→0,no forbidden source tokens or ordinary legacy lambda arrows. Headlines14/10/15/11; other proofs≤30; no new helper lacks fresh audit. |

Complete diagnostics by actual module:

| Module | Errors | Warnings |
|---|---:|---:|
| Roth/Separation.lean | 0 | 2 |
| Roth/Theta.lean | 0 | 28 |
| Roth/MainLemma.lean | 0 | 3 |
| Roth/Main.lean | 0 | 4 |
| Roth/LeanEval.lean | 0 | 0 |
| Roth.lean | 0 | 0 |

The two Separation warnings are the explicitly preserved header metadata and retained
public Fintype. Theta's28 and MainLemma/Main3/4 are preserved earlier warnings; five Theta
warnings already exposed during Index cleanup remain assigned to the upcoming Theta audit.
No warning was suppressed. Actual direct determinant caller is Theta.index_le_lem6:530;
index_det_le:406 is a separate theorem used in earlier coefficient-product caller validation.

### Added external-reference verification

All 46 declaration references in the final identifier manifest received actual native local
search queries;45 returned positive source hits. The index reported warming/error,so empty
results were not treated as absence. Module.Basis.coord_apply is generated by the simps!
annotation on coord in LinearAlgebra/Basis/Defs.lean:664; its source and actual compiler check
resolve the remaining index miss. All 46 actual #checks compile exit0; no invented identifier.
The Eval.Subring import resolves its actual pinned source file. Namespace/projection/local
variable tokens were filtered rather than misreported as external declarations.

Artifacts: /private/tmp/roth-separation-final-identifier-native.json and -identifier-manifest.json; /private/tmp/roth-separation-final-current-identifiers.lean/.log exit0 in35.56s.

| Verified names (grouped) | Evidence |
|---|---|
| `AlgHom.map_det`, `Finset.gcd_eq_sum_mul`, `Fintype.ofFinite`, `Function.injective_of_subsingleton`, `LinearMap.smul_apply` | Actual pinned source + compiled #check/use |
| `LinearMap.sum_apply`, `LinearMap.zero_apply`, `Module.Basis.coord_apply`, `Module.Basis.repr_self`, `Multiset.mem_replicate` | Actual pinned source + compiled #check/use |
| `Nat.lt_succ_of_le`, `Ne.symm`, `Polynomial.CAlgHom`, `Polynomial.C_mul_X_pow_eq_monomial`, `Polynomial.X_pow_mul_C` | Actual pinned source + compiled #check/use |
| `Polynomial.aeval_X_left_eq_map`, `Polynomial.aeval_algHom_apply`, `Polynomial.coeff_C_mul`, `Polynomial.map_aeval_eq_aeval_map`, `Polynomial.mem_map_range` | Actual pinned source + compiled #check/use |
| `Polynomial.natDegree_le_iff_coeff_eq_zero`, `Polynomial.toMvPolynomial_eq_rename_comp`, `Polynomial.toMvPolynomial_injective`, `Submodule.coe_smul`, `Subsingleton.elim` | Actual pinned source + compiled #check/use |
| `MvPolynomial.degreeOf_def`, `MvPolynomial.degrees_map_of_injective`, `MvPolynomial.degrees_rename_of_injective`, `MvPolynomial.mem_support_coeff_optionEquivLeft`, `MvPolynomial.notMem_support_of_degreeOf_lt` | Actual pinned source + compiled #check/use |
| `MvPolynomial.optionEquivLeft_X_none`, `MvPolynomial.optionEquivLeft_coeff_coeff`, `MvPolynomial.rename_eq_zero_iff_of_injective`, `MvPolynomial.restrictSupport`, `MvPolynomial.support_nonempty` | Actual pinned source + compiled #check/use |
| `MvPolynomial.map_X`, `Roth.wronskianMatrix`, `smul_ne_zero`, `mul_mul_mul_comm`, `eq_comm` | Actual pinned source + compiled #check/use |
| `ite_true`, `mul_ite`, `mul_one`, `not_not`, `Finite` | Actual pinned source + compiled #check/use |
| `AddCommMonoid` | Actual pinned source + compiled #check/use |

## Phase 6.5: fresh independent simplify

[Independent full-file review](Separation-simplify.md): ISSUES-FOUND-AND-FIXED. Built-in
Claude simplify is unavailable here; the report documents the independent holistic
adaptation rather than pretending that tool ran. Reviewer read all 560 then-current lines
and entire baseline diff and compiled a direct AC/inverse-rewrite alternative for the
rescaling stage. Applied: 5 → 2 body lines,remove cancellation certificate and linear_combination,
delete now-unused explicit import. No declarations/public types/docs changed. Fresh module,
complete LSP,independent exact helper proof and actual downstream axioms passed. Final owner
then normalized the three lambda arrows and repeated all cumulative gates/profiles.

## Phase 6.6: actual per-declaration profiling

Two fresh uncontended actual repository-module commands after ALL other native/compiler/
build requests drained: lake env lean --profile -Dtrace.profiler=true
-Dtrace.profiler.threshold=0 Roth/Separation.lean. Both complete exit 0; source hash stable.
Budget 1000 ms; 750 ms borderline requires repeat. Named outer-command maximum plus associated
outer async-proof cost is used without nested double counting; aggregate timing or an
extracted namespace is not substituted. Every retained theorem has command/proof anchors;
coeffNone is a synchronous definition. Multiple omit/section wrappers use max,not sum.

Sample 1: /private/tmp/roth-separation-final-current-profile1.log; parser input /private/tmp/roth-separation-final-current-profile1.log; invalid UTF8 replacements 0; elapsed 140.19 s; maximum 793.891 ms.

Sample 2: /private/tmp/roth-separation-final-current-profile2.log; parser input /private/tmp/roth-separation-final-current-profile2.log; invalid UTF8 replacements 0; elapsed 133.96 s; maximum 717.493 ms.

| Retained declaration | Source line | Sample1 ms | Sample2 ms |
|---|---:|---:|---:|
| eq_mapDomain_some_add_single | 51 | 170.963 | 128.040 |
| coeff_X_none_pow_mul_rename | 58 | 232.054 | 206.126 |
| coeffNone | 74 | 11.866 | 11.093 |
| coeff_coeffNone | 79 | 97.713 | 86.028 |
| eq_sum_X_none_pow_mul_coeffNone | 92 | 107.784 | 94.044 |
| degreeOf_coeffNone_le | 108 | 33.831 | 30.358 |
| coeff_rename_mul_aeval | 117 | 178.284 | 172.148 |
| aeval_X_eq_rename | 131 | 38.878 | 32.929 |
| hasseDeriv_rename_mul_aeval | 140 | 380.101 | 361.331 |
| coeff_uniqueAlgEquiv_symm | 163 | 32.937 | 30.446 |
| degreeOf_uniqueAlgEquiv_symm | 168 | 48.892 | 45.663 |
| degreeOf_rename_mul_aeval | 191 | 136.721 | 133.262 |
| degreeOf_none_rename_mul_aeval | 207 | 152.453 | 170.958 |
| linearIndependent_coordinate_polynomials_aux | 229 | 301.921 | 280.005 |
| eq_sum_aeval_basis_coeffNone_aux | 259 | 793.891 | 717.493 |
| exists_coeffNone_basis_aux | 285 | 775.522 | 688.695 |
| exists_separated_representation | 319 | 348.648 | 361.216 |
| det_hasseDeriv_separated | 345 | 493.411 | 436.596 |
| exists_sum_mul_eq_gcd | 368 | 93.621 | 91.146 |
| exists_nat_smul_eq_map | 374 | 349.010 | 308.267 |
| exists_primitive_smul_eq | 400 | 718.102 | 617.749 |
| exists_int_eq_of_gcd_eq_one | 437 | 152.486 | 135.799 |
| rescale_separated_factor_aux | 451 | 286.300 | 260.173 |
| exists_int_polynomial_of_primitive_factor_aux | 460 | 384.003 | 282.193 |
| exists_int_factors | 479 | 642.713 | 556.379 |
| exists_rat_factors_det_hasseDeriv_aux | 504 | 566.354 | 487.023 |
| exists_det_eq_mul | 537 | 313.537 | 243.192 |

All 27 are below 1000 ms in both final sweeps; any borderline declaration receives both
actual samples. No over-budget Separation deferral,raised limit or profiler scaffolding.
No whole-project speedup is inferred from proof length or a single measurement.

### Explicit external Theta performance follow-up

Normal actual Theta builds,complete LSP and all original contracts/standard axioms pass.
The earlier actual threshold-zero Theta trace stalled and was terminated(exit130); a
bounded rerun at verified 1 ms trace threshold exited1 at default 200000-heartbeat linarith
simplex timeouts in unchanged index_le_lem6 at Theta.lean:604/617. Its failed-run diagnostic
anchors are index_det_le: 2055.175 ms and direct caller index_le_lem6: 10015.925 ms. They are NOT
accepted successful performance samples. Raw evidence is preserved in
/private/tmp/roth-separation-d30-theta-profile-1ms.log and
/private/tmp/roth-separation-d30-theta-profile-1ms-status.json. No Theta proof or
limit was changed. These concrete performance issues belong to the next dedicated Theta
file/declaration audit; this report claims Separation performance success,not whole-project
performance success. The project remains active and incomplete.

## Phase 7: publication and handoff

All 30 original reports,eight independent historical helper audits,all 12 approved public
instance removals,fresh holistic review,actual per-declaration profile table and cumulative
evidence are recorded. No required Separation API decision or proof/style obligation
remains; metadata and retained Fintype are explicit user-preserved warnings. Optional
unapplied alternatives and scheduled project-end rename/external Theta performance work
remain accurately scoped above. No source edit after the final freeze. Exact-path final
commit and successful push to ramin-cleanup,followed by clean status,are required before
file/Git/shared-progress ownership release. The parent continues with fresh Theta ownership.
