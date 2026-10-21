# Helper5 owner verification addendum

The independently frozen helper report and its 915-artifact manifest remain unchanged: report SHA `0dbb1d902ecf16a225285da2f037eb1bb49db9a77fcd97c63c57c1113cea5871`, manifest SHA `20a4a7b69678c2d946f7eaae678c342f963a11c8873565ed67df731025fa2e68`.

Owner review found that the six saved worker-native responses did not include their request arguments. After compaction the worker could not recover the exact executed arguments. The recovery attestation records unknowns explicitly; no historical arguments or observations were backdated. The source, reports and frozen evidence were not edited to conceal that gap.

The owner therefore made three fresh, sequential `lean_diagnostic_messages` requests on the selected source, with exactly `file_path` and `timeout_s: 60`. No severity, line-range or declaration filter was supplied. Every response is complete, nonpartial, nontimeout, successful, without errors or failed dependencies. All six historical diagnostic result objects are structurally identical after JSON decoding to the corresponding new explicit unfiltered result. The historical request arguments remain unknown.

| File | Actual absolute file_path | timeout_s | Result | Fresh complete raw response SHA256 |
|---|---|---:|---|---|
| ML | `/Users/ramin/LEAN/Roth/Roth/MainLemma.lean` | 60 | 1 warnings, zero errors | `b0b7c457ad06da34de1072d12cea4c5fa9c4adf45715143c01c1165356c0b6c7` |
| Main | `/Users/ramin/LEAN/Roth/Roth/Main.lean` | 60 | 4 warnings, zero errors | `dc9c6d7b7666058ba799a9e4a08bdeaddd9c689923c544b8510ec049d30434cf` |
| Eval | `/Users/ramin/LEAN/Roth/Roth/LeanEval.lean` | 60 | 0 warnings, zero errors | `918bc0c9ce187601dea6c5324c90f810d1bf950546bf1326988074f1c8933111` |

Actual request/response records: `/private/tmp/roth-mainlemma-owner/helper5-owner-native-requests.json`; source pins before and after: `helper5-owner-native-{prepins,postpins}.json`; comparison and gap repair: `helper5-owner-native-gap-repair.json`. The 17 source/configuration pins were identical before and after, selected MainLemma source SHA `3fd2eb2e69cf2e3fb112cdfe992dad74a1b2a1ded6c13e11c8b395b7070e6147`. All 104 current project-cache companions still match the final audited snapshot.

The owner independently verified all 915 actual artifacts (367069698 bytes; 65 explicit binary exceptions), 25 external text references, nine catalog references, and all 24793 current compiled inputs (3929272896 bytes). The latter scope is the actual package/setup availability union plus the installed core compiled-artifact SUPERSET, not an exact loaded closure. All 29 helper-owned process groups are freshly absent. Actual pinned Lean/Lake binaries and Elan proxies match all recorded observations.

Independent raw reanchoring confirms controlled matched **213.894 → 145.625 ms**, with the complete private-lemma command and exact proof/kernel/lint roots counted once, one inclusive private-theorem expansion excluded, identical explicit captured environments and immutable source/input hashes. The older 224.899 ms capture and raw MANPATH discrepancy remain disclosed historical evidence.

Detailed owner review: `/private/tmp/roth-mainlemma-owner/helper5-owner-evidence-review.json`; raw timing review: `helper5-owner-profile-reanchor.json`. Helper5 is accepted for the next phase of original19. This addendum grants no original-declaration count, publication, final whole-file profile or file-complete credit.
