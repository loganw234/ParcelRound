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

**Read at three moments** — the floor, not the mechanism; `urgent/`
below is the rest of it:

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

## `urgent/` — the push channel

The three moments above are a **polling schedule**, and its latency is
its interval. A correction posted ten minutes after you start sits
unread until your next read moment. `urgent/` is the way past that.

**Arm a watcher on it before you start anything**, persistently, so a
new message becomes a notification rather than something you find later:

```bash
U=<ledger path>/urgent; mkdir -p "$U"
seen=$(ls "$U" 2>/dev/null | sort)
while true; do
  cur=$(ls "$U" 2>/dev/null | sort)
  comm -13 <(echo "$seen") <(echo "$cur") | while read -r f; do
    head -1 "$U/$f"; grep -m1 '^For:' "$U/$f" 2>/dev/null || true
  done
  seen=$cur; sleep 20
done
```

**The watch is not the mechanism, it is latency reduction.** A watcher
that has died — timed out, killed, stopped for volume — looks exactly
like a directory with nothing new in it. If you notice yours is gone,
re-arm it **and do a full read**, because you cannot tell how long it
was dead.

**The bar for writing here is "stop what you are doing and read this",**
and it is mostly the lead's: a brief that turned out wrong, a merge that
invalidated an assumption, a thing you were told to delete that turns
out to be load bearing. Everything else goes in your own file. A channel
that fires for things that could have waited is one people learn to
ignore.

**One file per message, renamed into place.** Compose it somewhere else
and `mv` it in, so a watcher can never catch a half-written file, and so
a new message is an unambiguous event:

    <who>-<short-slug>.md

First line is the headline. Include a `For:` line — the watcher prints
those two and nothing else, so they are what someone decides on.

**Verifiers watch the lead's file only.** A verifier is paid for
independence, and a stream of "the parcel says this is fine" is exactly
what erodes it.

## Entry format

    ## <date time> — <one-line headline>

    Measured: ...
    Believed: ...
    For: <who this is likely to matter to, or "anyone">
