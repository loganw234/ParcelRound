# Parcel rounds

A method for splitting one body of work across several coding agents at
once, without the pieces failing to meet.

It exists because the obvious approach fails in a specific, repeatable
way. Give four agents four well-scoped parcels of one feature and you
can get four green gates and a feature that does not work — because the
work *between* the parcels belonged to nobody, and nothing was looking
there. That happened, on a real codebase, and most of what follows is a
defence against it.

## What's here

| | |
|---|---|
| [METHOD.md](METHOD.md) | The method. Start here. |
| [CASE-STUDY.md](CASE-STUDY.md) | One round, measured: what it caught, what it cost, what went wrong. |
| [templates/brief.md](templates/brief.md) | A parcel brief. Every section earns its place. |
| [templates/verifier.md](templates/verifier.md) | A verifier brief — the agent whose job is to disconfirm. |
| [templates/ledger.md](templates/ledger.md) | Drop-in README for the cross-agent ledger. |
| [templates/checklists.md](templates/checklists.md) | Dispatch and per-merge checklists. |

## Is this for you?

**Use it when** there are three or more pieces of work that are each
session-sized, mostly independent, and all land in one codebase, and
the codebase has a test suite you actually trust.

**Don't** for a single task, for exploratory work where the split isn't
obvious yet, or where the pieces can't be tested separately. Two agents
on a two-way split is usually slower than doing it yourself, because
the brief costs more than the work.

**The bottleneck is not agent count.** It's the lead's capacity to merge
and verify, and in practice it's the suite run after each merge. Four
parcels is comfortable. Eight is a queue.

## The five-minute version

1. **List every file each parcel would touch.** Anything appearing in
   three or more columns isn't a conflict to manage — it's the first
   parcel, and it's yours. Do that refactor *first*, prove it changed
   no behaviour, and land it before anyone else starts.
2. **Write briefs that say what each parcel owns, what it must not
   touch and who owns that instead, and which small edits outside its
   files are expected.** Name the specific negative control it has to
   run. End with *"tell me anything you found that this brief got
   wrong."*
3. **Stand up a ledger** — append-only, one file per author, outside
   every worktree — and say when to read it. It's the only way to
   correct a brief after dispatch.
4. **Merge serially, run the full suite after each one, and read the
   log rather than the exit code.** Never merge while a suite is
   running.
5. **For anything hard to check by reading, put a verifier between the
   parcel and the merge.** Its job is to disconfirm, it must not fix
   anything, and "found nothing" has to be an acceptable answer.

## The clearest single argument for it

A bit-identity defect that **five parcels, two verifiers, a follow-up
parcel and 211 assertions all passed over** — because it lived in a
combination two parcels' gates each excluded by construction. One
parcel's file pinned the setting; the other's registered no force;
neither brief mentioned the other. A hundred-line seam test, written by
the lead because it belonged to no parcel, found it in seconds:
21 of 21 values differing at ~1e-4, a trajectory divergence rather than
a last bit. The fix was three lines.

Splitting work creates a gap exactly where the split is, and the gap is
invisible to everyone working inside it. [CASE-STUDY.md](CASE-STUDY.md)
traces that one end to end.

## The one line that pays for the whole thing

> *"Report anything you found that this brief got wrong."*

Nine words. In the round measured in [CASE-STUDY.md](CASE-STUDY.md) it
returned **twelve corrections from five parcels — every single parcel
corrected its brief**, including one where the lead had described a
mechanism backwards in a way that changed what the feature cost.

The lesson generalises past agents: the parcels were fine. What the
system surfaced, fast, was that *the lead's model of the code was
wrong*, over and over. That is worth knowing in hours rather than at
integration.

## Licence

MIT ([LICENSE](LICENSE)) — chosen so this can be copied into anything
without thought. One file to change if you'd rather it were something
else.
