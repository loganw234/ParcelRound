# Ledger template

Drop this in as the ledger directory's own `README.md`, with the two
`<...>` filled. It is the text that ran, not a rewrite of it -
[METHOD.md](../METHOD.md) section 4 says why the ledger exists.

---

# The round ledger

Scaffolding for a parcel round, not history. Ignored by version
control; the lead folds anything durable into `<the project's own
records>` at the end of the round and deletes this directory.

It exists because **a brief is written once, at dispatch, and cannot be
updated.** Anything learned while the parcels are running otherwise
reaches them never — it arrives in a final report, after the sibling who
needed it has finished.

## How to use it

This directory is **outside every worktree**. Agents work in separate
checkouts and cannot see each other's files, so reach this by its
absolute path:

    <absolute path to the ledger directory>

**One file per author, append only.** Yours is `<your-name>.md` —
`P1.md`, `verifier-P2.md`, `lead.md`. Read every file in the directory;
write only to your own. Never edit anyone else's, and never edit an
entry you already wrote: append a correction underneath instead.

**Read at three moments**, not "periodically":

1. once before starting anything;
2. again before designing anything that touches a file your brief
   called shared or forbidden;
3. again before writing your final report.

**Write when this clears the bar:** *would it have changed another
parcel's work, or the lead's?* Three things do.

1. **Environment and setup** — what the tree needs before it builds,
   what your base commit actually turned out to be, a tool that is not
   where it looks.
2. **A brief that turned out wrong** — the moment you find it, not in
   your report. A sibling may be acting on the same wrong premise right
   now.
3. **A finding about shared code** — behaviour in a function another
   parcel owns, an upstream defect, a constraint that will bind someone
   else.

**Do not write** progress, plans, or anything only your own parcel cares
about. A ledger full of status is one nobody reads.

**Mark what you measured.** Every entry says which claims were
*measured* and which are *believed*, to the same standard as your
report. Other agents build on these, and an unverified claim propagates
faster than a verified one.

## Entry format

    ## <date time> — <one-line headline>

    Measured: ...
    Believed: ...
    For: <who this is likely to matter to, or "anyone">
