# Checklists

Two, because the failures cluster at two moments: what you get wrong
before dispatch is structural and expensive, and what you get wrong at a
merge is procedural and recoverable. [METHOD.md](../METHOD.md) has the
reasoning behind every line.

---

## Before dispatch

**The split**

- [ ] Every file each parcel would touch is listed. Anything appearing
      in three or more columns became P0.
- [ ] P0 landed and was pushed, is behaviour-preserving, and the full
      suite is green on **both sides** of it.
- [ ] The P0 refactor was aimed at making the shared seam **disappear**,
      not at making it small. (Can the build glob a directory? Can the
      entry points be discovered rather than declared?)
- [ ] Every shared fact has exactly one owning file.
- [ ] Every count is derived from the definition, or declared once
      beside the list and checked against it — and the brief says which
      of those two it is.
- [ ] Registries walk themselves and fail **by name, in both
      directions** — a row no test names, and a test naming a row that
      is gone. Proven with a dummy entry.

**Each brief**

- [ ] Names its owned files — by function where a file is shared.
- [ ] Names its forbidden files **with the owner of each**.
- [ ] Enumerates the small edits outside its files that are expected.
- [ ] Says how to make the tree buildable, if that takes a step.
- [ ] Names the base commit **and says to verify it**.
- [ ] Carries the host build traps as verbatim commands.
- [ ] Names its **specific** negative control, not "test it properly",
      and asks for the control's output.
- [ ] Says what regression this parcel is most likely to cause.
- [ ] Asks what the brief got wrong.
- [ ] Asks for boundary crossings to be disclosed, and says they are
      expected.
- [ ] **Every path named in it exists.** (A forbidden-files list carried
      from another project is noise at best.)

**The ledger**

- [ ] Exists, outside every worktree, at a path every brief states.
- [ ] Ignored by version control.
- [ ] One file per author; the README says so.
- [ ] Read moments are stated **as moments**, not "periodically".
- [ ] Seeded with whatever the lead already knows that a parcel would
      want.

---

## At each merge

- [ ] The parcel's negative control was run, and its output reported —
      not just described.
- [ ] The diff stayed inside the ownership boundary; any crossing was
      disclosed and reasoned.
- [ ] Claims added in comments and commit messages are true. (A
      sentence in the code is something the next person relies on.)
- [ ] Conflicts were enumerated from **what the VCS says is
      conflicted**, not from what the merge output printed.
- [ ] No conflict marker survived into the commit, and nothing was
      staged that should not be — check what you staged, not what you
      expected to stage.
- [ ] A seam test exercises this parcel against an already-merged one.
- [ ] The full suite was run by the lead, on a tree **nothing was merged
      into while it ran**, and the **log was read** — not the exit code.
- [ ] A failure that is not immediately attributable got a timestamp
      check before it got a diagnosis, and was called neither a defect
      nor a false alarm until a clean re-run said which.
- [ ] Anything the merge taught the lead went **into the ledger**, for
      the parcels still running.

---

## At the end of the round

- [ ] The ledger's durable findings are folded into the project's own
      records, and the ledger is deleted.
- [ ] The files that state the project's claims — README, published
      docs, support tables — are swept for anything a parcel made stale.
      (Parcels are forbidden to touch these, so every one of them will
      have reported staleness rather than fixed it.)
- [ ] Each parcel's brief errors are written down somewhere the next
      round's briefs will be built from.
