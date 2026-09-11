# Parcel brief template

Copy, fill the `<...>`, delete the parenthesised notes. Every section is
here because leaving it out cost something — [METHOD.md](../METHOD.md)
§3 says what.

Keep it dense. A brief that reads like a contract gets skimmed; one that
reads like a colleague handing over gets followed.

---

You are parcel **<P2>** in `<repo>` (a git worktree of `<absolute path>`,
branched from `<branch>` at commit `<sha>`). **Check you are on that
commit** — `git log --oneline -1` — and if you are not, say so in the
ledger and reset.

<One paragraph on what the project is and what its central invariant is.
The thing that, if broken, makes everything else pointless. Say it in
the terms the tests use.>

## Start here

1. `<the plan / the round's brief document>`, all of it, then its
   **<P2>** section.
2. `<the method or post-mortem doc>` — <what it will save them>.
3. `<the header or registry P0 produced>` — <how a capability is
   unlocked now>.
4. `<the two or three source locations they will actually be editing,
   and the upstream they are reproducing>`.

## The ledger

`<absolute path outside every worktree>`. Read **every** file there
before you start, again before you design anything touching a file this
brief calls shared or forbidden, and again before you write your report.
Append to `<your-name>.md` only. Its README says what clears the bar.

## Your job

<One paragraph. If it needs three, this is two parcels.>

## What reading <the upstream> already turned up — verify it, do not trust it

<Anything you found while writing the brief. Hand over the facts and the
line numbers; it saves an hour each time. Then say explicitly:>

**A finding you should confirm before relying on it.** <the claim.> If
that holds, <what follows>. Check it against the source; if I am wrong,
say so in your report and design from what is actually there.

**The trap that would be a silent wrong answer.** <the thing that
becomes live the moment their change lands, and that nothing currently
handles. There is usually one. Finding it is most of the value of
writing the brief.>

## Files you own

- `<path>`, **only** `<function>` — <and why the boundary is there>.
- A new `<path>`.

## Files you must NOT touch

- `<path or function>` — **<who> is editing it right now.**
- `<path>` — <owner>.
- **Integrator-only:** `<the files that state the project's claims>`. If
  one needs a change, say so in your report.
- Anything outside this worktree — in particular `<other live repos>`.

Expected small edits outside your files, and **only** these: `<registry
row>`, `<one declaration>`, `<one line in the build file>`, `<one call
in main()>`.

## Building and testing on this host

<The tree may need a step before it builds — say it. Then the exact
invocation, not "build it":>

```bash
<verbatim, including every non-obvious variable>
```

<Which gate to run, how long it takes, and "background long runs rather
than polling". Then: "Build only inside your own worktree.">

## Working rules this repository learned the hard way

- <the two or three environment traps that have actually cost hours.
  Keep it short and true; a long list gets skimmed.>
- **A gate that cannot fail is not a gate.** <Then the specific control,
  named — not "test it properly". For example: "a do-nothing routine
  must leave the run bit-identical to no routine at all, *and* the
  active case must differ from the inactive one."> Build it, run it,
  confirm it fails, delete the artifact, and **report both results**.

## Do not

- push, merge, rebase, or commit to `<main>`. Commit inside your
  worktree only; the integrator merges.
- <the specific regression this parcel is most likely to cause>.
- "fix" anything outside your scope — report it instead.

## Report

What you changed file by file, the gate output (**actual lines**), the
controls with their measured numbers, and **anything you found that this
brief got wrong**. If you hit something that makes the approach
unworkable, stop and report that rather than inventing a different
design. If you had to cross a boundary this brief drew, say so and say
why — that is expected and fine; doing it silently is not.
