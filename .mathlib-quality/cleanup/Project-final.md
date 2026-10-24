# Roth project cleanup — final validation

Status: **PASS: all 263 genuine original declarations and all 14 files validated**.
Publication status is recorded in [cleanup-progress.md](../cleanup-progress.md).
The historical denominator 264 included comment prose in CoeffNorm; it is not an extra
declaration. Introduced helpers were audited separately and add no original-declaration credit.

The thirteen accepted mathematical file audits remain authoritative. This final pass completes
the zero-declaration umbrella module, applies the five queued names, and checks the resulting
project. It does not repeat accepted per-declaration work or add optional API changes.

## Approved warning follow-up (2026-10-24)

**PASS:** the subsequent user-approved four-theorem Theta amendment removes all five
previously retained binder warnings. The [amendment report](Theta-warning-amendment.md)
records sequential checkpoints, exact old-contract adapters, independent new proofs,
actual bodies/axioms, fresh independent review and both required whole-file profiles.
All 50 profile rows pass below 1 s in both samples (maxima 795.574 / 822.148 ms).

The amended project passes full `lake build` (26.202 s), followed by the separate
`lake build Roth.LeanEval` (4.045 s), with zero errors and **14 warnings**: twelve metadata
warnings and two retained public `Fintype` assumptions. Complete final affected-file/root
diagnostics also pass. Only Theta source changed; all other sources, imports and pins are
preserved. These results supersede the historical nineteen-warning inventory below and
only the five Theta binder-retention choices expressly overridden by the user. The original
263-declaration/14-file cleanup counts and all other accepted choices remain unchanged.

## File completion

Final reports: [HasseDeriv](HasseDeriv-final.md), [Box](Box-final.md),
[Wronskian](Wronskian-final.md), [Taylor](Taylor-final.md), [CoeffNorm](CoeffNorm-final.md),
[GenWronskian](GenWronskian-final.md), [Lattice](Lattice-final.md), [Index](Index-final.md),
[Separation](Separation-final.md), [Theta](Theta-final.md), [MainLemma](MainLemma-final.md),
[Main](Main-final.md), [LeanEval](LeanEval-final.md), and [Roth](Roth-final.md).
Their earlier pending global-rename/project-completion statements are superseded here.

## Phase 5a and Phase 5b

No outstanding non-rename refactoring was recommended. The five distinct queue entries had
no conflicting destinations or existing-name collisions. They were applied sequentially,
with complete declaring-file and changed-caller diagnostics before continuing.

All names below are in namespace `Roth`.

| Old name | New name | Declaring file |
|---|---|---|
| `index_hasseDeriv_ge` | `index_sub_weight_le_index_hasseDeriv` | Index |
| `B₁` | `mainCoeffBound` | MainLemma |
| `log_B₁_gt` | `mul_log_div_two_lt_log_mainCoeffBound` | MainLemma |
| `abs_coeff_modByMonic_le` | `norm_coeff_modByMonic_le` | MainLemma |
| `lem7_hyp_of_h32` | `mul_two_mul_add_one_div_lt_of_le_sq_mul` | MainLemma |

- Queue: raw 5, deduplicated 5, applied 5, skipped 0; queue now empty.
- Four mathematical files changed: Index, Theta, MainLemma and Main.
- 33 identifier occurrences updated: five declarations, 24 executable uses, three module
  documentation references and one proof comment. Longer lines were wrapped to width 100.
- No stale exact identifiers remain in live Lean source. Historical audits, tickets and
  source-reference notes retain the names used when their evidence was produced; the table
  above is their current-name map. No historical proof evidence was rewritten.
- `thueSiegelRoth` retains its explicitly accepted external benchmark name.

## Phase 6: actual final gates

| Gate | Result and actual evidence |
|---|---|
| Full project and affected modules | `/Users/ramin/.elan/bin/lake build`, exit 0, 92.751 s, 2467 jobs. |
| Separate LeanEval target | Subsequent `/Users/ramin/.elan/bin/lake build Roth.LeanEval`, exit 0, 30.822 s. |
| Actual changed contracts and bodies | Before/after `lake env lean` probes exited 0 (44.799 / 86.696 s); all five full TYPE/opaque VALUE records compared as detailed below. |
| Project trust | All 445 actual constants defined by the thirteen mathematical modules have closed types/available values and use only `propext`, `Classical.choice`, `Quot.sound`. |
| Complete diagnostics | Eight serial rename checks plus final MainLemma/Main/LeanEval/root checks: success, nonpartial, no timeout or failed dependencies, zero errors. |
| Source/definition/statement protection | All fourteen files recover their pre-rename contents modulo exactly the five names and whitespace; the root's preceding doc-only correction is independently checked. |
| Imports, references and pins | All imports unchanged; original citations/comments retained modulo names/wrapping; no new external Lean identifier. Toolchain, Lake configuration and dependency manifest unchanged since cleanup entry. |
| Static/structure/trust | All source lines ≤100 columns; no trailing whitespace, admissions, new axioms, native-decide trust shortcuts, resource raises, disabled linters, debug scaffolding or TODO/FIXME. Existing proof decomposition remains intact. |

Before/after contract comparison uses complete serialized expressions, not just hashes or
proof irrelevance. The coefficient definition and logarithm theorem match exactly after
constant renaming. The other three declarations additionally require seven explicitly
enumerated generated Name-fragment substitutions, all independently located exclusively
in `lam`/`forallE` binder-name positions. Written binder names, binder kinds, de Bruijn
indices, universes, hypotheses, conclusions and every remaining TYPE/VALUE byte agree.
All five actual opaque bodies were inferred against their actual types with default limits;
their standard-axiom checks pass. Initial literal mismatches are retained and are not
described as raw identity. Existing original-contract adapters and independent proof audits
remain accepted through this precisely bounded source/name transformation.

Scratch evidence is under `/private/tmp/roth-completion/`: `source-before.json`,
`source-final.json`, `rename-queue.jsonl`, `rename-log.jsonl`, `rename-diagnostics.json`,
`final-diagnostics.json`, `before-values.json`, `after-values.json`,
`accepted-contract-comparison.json`, `project-trust.json`, and the actual command receipts
and separate raw streams. The first baseline probe's serialized output was overwritten by
its same-named command receipt; this harness mistake was corrected and that probe alone
was recaptured before any rename. No lost output is used as evidence.

## Independent review and performance

Fresh independent Astra HIGH review accepted the root file and subsequently all five changed
source files. The reviewer independently reversed the rename map, checked all fourteen
source hashes and confirmed that proof logic, assumptions and documentation were preserved.
Outcome: **PASS-THROUGH**, no unresolved recommendation. This substitutes for unavailable
`/simplify`; no unavailable-tool invocation is claimed.

The accepted final per-file performance audits are reused with an explicit qualification:
the final pass changes names, wrapping and root documentation only, so executable proof
payloads are identical under the recorded renames. No new timing sample or post-rename
speedup is claimed. Prior valid failures remain in their original reports; accepted final
samples and required near-budget repeats are not replaced or averaged away. For example,
Main's accepted final pair covers all 23 rows with maximum 916.000 ms; MainLemma and
LeanEval retain their accepted complete sweeps. Root has zero declarations to profile.
No new proof or performance defect was found that warrants restarting those audits.

## Preserved choices and limitations

Lean remains `v4.34.0`; mathlib remains
`5ed2965256430c3649e86755f9576b54eca72435`. The original completion build reported 19 existing warnings:
twelve missing-authoritative-metadata warnings, two deliberately retained public `Fintype`
assumptions, and five then-preserved Theta binder warnings. The approved follow-up above resolves those five.
None is suppressed;
LeanEval and root diagnostics are clean. No license/year/author metadata was invented.
Previously accepted wrapper/domain/denominator/bound assumptions and declined optional
companions remain as instructed. All required cleanup work is validated; no pending rename,
mathematical correction or mandatory validation gate remains.
