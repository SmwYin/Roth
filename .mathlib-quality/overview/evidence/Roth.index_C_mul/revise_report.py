from pathlib import Path
p=Path(__file__).parent/'report.md';s=p.read_text()
s=s.replace('# Roth.index_C_mul — BORDERLINE-needs-human','# Roth.index_C_mul — NO-composable-from-mathlib')
s=s.replace('but its proof is just definitional simp; Phase6b makes whether it merits a named theorem a design question.','and a fresh explicit congruence term proves the law using existing support_smul_eq alone. This is a genuine composition, independent of the earlier simp diagnostic.')
s=s.replace('The fixed parent interface is already maximal in its explicit assumptions:','The fixed parent interface has no verified droppable assumptions:')
s=s.replace('The support-only form further weakens coefficients to an AddCommMonoid M with the same scalar module/torsion-free hypotheses, and is an exact application of existing `Finsupp.support_smul_eq`.','The support-only form further weakens coefficients to an AddCommMonoid M with the same scalar module/torsion-free hypotheses, and is an exact application of existing `Finsupp.support_smul_eq`. These are the verified library-interface assumptions, not a logical minimality claim. Scalar support invariance only needs the coefficient action at this particular c to preserve and reflect zero; injectivity suffices. A unit can act injectively even over a ring with zero divisors. Existing `Finsupp.support_mapRange_of_injective` (`Mathlib/Data/Finsupp/Defs.lean:348`) expresses the wider zero-preserving injective coefficient-map form. No uncompiled unit/regular-action theorem or mechanical weakening is claimed; that broader interface is a separate optional API design.')
a=s.index('Parent Roth.index was assessed NO-mathlib-has-it')
b=s.index('## Phase 8 —',a)
s=s[:a]+'''Parent Roth.index was assessed NO-mathlib-has-it via projected infDegree. We independently re-aimed here, rather than inheriting NO. Unlike the preceding negation theorem, no analogous named scalar degree law was identified in the pin. The first independently compiled modern proof closed by `simp only [AddMonoidAlgebra.infDegree, AddMonoidAlgebra.coeff_smul, Finsupp.support_smul_eq hc]`. In isolation that is Phase6b's BORDERLINE trivial simp diagnostic; it is not an exact named law and not automatically a NO composition.

A fresh explicit composition then compiled independently, with `fail_if_success exact?` confirming one-step tactic search did not already close the goal:

```lean
by
  classical
  exact congrArg (fun s : Finset A ↦ s.inf D)
    (Finsupp.support_smul_eq hc (g := f.coeff))
```

Here the only substantive existing mathlib theorem is support_smul_eq; core congrArg transports its equality through Finset.inf. The degree/coeff scalar identities match definitionally, with no rewriting, normalization proof, new helper premise or imported project target. This meets Phase6a's ≤3-existing-call composition bar. `exact?` failure is evidence about that search attempt, not global absence. [Exact composition source](../evidence/Roth.index_C_mul/index-c-mul-explicit-composition-executed.lean.txt), [raw receipt](../evidence/Roth.index_C_mul/index-c-mul-explicit-composition-receipt.json).

Root also checked actual original-form transport through the retained canonical133 bridge, Taylor multiplication/constant/scalar conversion, and this exact support congruence under `WithTop.untopD 0`. The bridge is a genuine previously proved normalization theorem; it is not falsely counted as a mathlib building block. [Bridge source](../evidence/Roth.index_C_mul/index-c-mul-bridge-executed.lean.txt), [receipt](../evidence/Roth.index_C_mul/index-c-mul-bridge-receipt.json). The full sole caller replay preserves its original statement and all parameters, changing only the target call to the independently proved fallback replacement. [Caller execution](../evidence/Roth.index_C_mul/index-c-mul-caller-executed.lean.txt), [receipt](../evidence/Roth.index_C_mul/index-c-mul-caller-receipt.json).

A natural weightedOrder_mul route is contextual and needs translation, natural-weight conversion and zero handling; it does not supply the arbitrary-weight, no-positivity parent law as a one-call replacement. No full migration of all index consumers to a new generic representation is claimed.

## Phase 7 — Actionable verdict

**NO-composable-from-mathlib**, evaluated on the properly re-aimed parent degree law. The substantive existing building block is `Finsupp.support_smul_eq`, at `Mathlib/Data/Finsupp/SMul.lean:137`; equality transport uses core congrArg. The fresh explicit term above makes the verdict rest on genuine ≤3-call composition, rather than on the earlier closing-simp diagnostic. No named infDegree scalar law is falsely claimed to exist; this is not NO-mathlib-has-it. The old-form Roth theorem still needs the genuine parent bridge and Taylor normalization, and is not claimed to be a ≤3-mathlib-call term.

Every explicit caller refactor plan: at the sole `Roth/Theta.lean:405` application inside `sum_max_sub_le_index_det`, retain `map_intCast` normalization and substitute the verified original-form replacement proof in local hidx if deleting the wrapper while retaining the old parent. The full caller replay proves this interface. With parent index migrated to the canonical infDegree representation, use the explicit support_smul_eq congruence under default0 projection after Taylor scalar normalization; the bridge execution demonstrates that transport. Do not simply replace the old call by support_smul_eq without these representation steps.

Alternative local destination: `Roth/Index.lean` is the appropriate compatibility-adapter home while the zero-default Taylor index remains. It may reasonably remain there during a staged parent refactor; this assessment recommends against upstreaming the concrete real/Taylor specialization. If contributors later want named generic degree scalar laws beside supDegree_neg, that is optional API convenience, not missing mathematical substance. The coefficient-action regularity / unit interface is separately worth designing and compiling before claiming a stronger upstream law. No production files or Git state were changed by this assessment.

''' + s[b:]
s=s.replace('The three design questions above remain judgment questions while verification unresolved[] is empty.','Verification unresolved[] is empty; optional future naming or regular-action design does not block this read-only assessment.')
p.write_text(s)
