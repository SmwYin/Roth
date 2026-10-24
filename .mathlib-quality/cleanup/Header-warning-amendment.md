# Approved Apache-2.0 header amendment

Status: PASS, 2026-10-24. The user approved the proposed copyright year 2026,
Ramin Takloo-Bighash and Samuel Yin attribution, and Apache License 2.0.
The standard license is recorded in the new repository-root LICENSE file, copied
byte-for-byte from the pinned mathlib LICENSE.

The twelve previously warning-producing mathematical modules now begin with the approved
copyright, license and authors block. All prior source bytes are preserved after the
six-line prefix, including the separately validated Finite changes. No theorem, proof,
import, option, version or dependency changed during the header amendment. Roth.lean and
Roth/LeanEval.lean are unchanged by this amendment.

## Validation

- Full lake build: exit 0, 2,467 jobs, zero errors and zero warnings.
- Subsequent separate lake build Roth.LeanEval: exit 0, 2,466 jobs, zero errors and zero warnings.
- Independent Astra High read-only review: PASS. All twelve exact prefixes, saved source
  bytes and old/new hashes match; LICENSE exactly matches pinned mathlib's standard license.
- git diff --check: PASS. No warning suppression was introduced.
- Earlier proof, contract, axiom and performance checks remain applicable to the unchanged
  mathematical source. No new performance claim or redundant profile is introduced for comments.

The warning count is now zero. This supersedes all historical retained-header notices in
individual file reports, and the earlier inventories of 19, 14 and 12 warnings.
The Finite follow-up is also complete; its second validated checkpoint is included in the
final publication alongside these headers. Original completion remains 263/263 declarations
and 14/14 files. No required change or validation remains.

Evidence: /private/tmp/roth-header-amendment/ contains both build logs, headers.json,
and exact pre-header source copies. Prior Finite proof/profile evidence is described in
[Finite-warning-amendment.md](Finite-warning-amendment.md).
