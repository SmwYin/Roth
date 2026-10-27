### Class 5 — Real but not a single mechanical edit

The generalisation IS real (a more general form would be valuable; the
literature has it; the proof could in principle adapt) — but it's not a
single hypothesis-weakening edit. It involves restating a foundational
definition threaded through the entire development, or touching multiple
files, or rebuilding API around a different abstract structure.

`YES-but-generalise-first` is the verdict for one-edit weakenings the
downstream `/generalise` skill can mechanically apply. Multi-file
refactors are a different size of work — route to
`BORDERLINE-needs-human` with a dev-ticket-style numbered question
("This would be more general as X over `[CompositeStructure]`, but the
change threads through 7 files and changes 3 public signatures. Worth a
dev project, or ship as-is?").

