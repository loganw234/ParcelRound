# The method

Every rule here is here because something broke without it. Where a
rule cites an incident, that is evidence rather than colour; the
incidents are written up in [CASE-STUDY.md](CASE-STUDY.md).

**This file is the canonical copy.** It was extracted from a working
copy that still lives in the project it was developed on, as that
round's own documentation. Two copies of one document is precisely
what section 1 tells you not to have; the honest position is that the
duplication is known, this one wins, and the other is scheduled to
become a pointer once this repository has somewhere to point at.

Vocabulary: the **lead** is you, the session that plans, briefs, merges
and verifies. A **parcel** is one agent with one brief. A **verifier**
is an agent whose only job is to disconfirm a parcel's work. A **round**
is one pass of all of it.

---

## 1. The one failure mode

Not "an agent does bad work". Agents mostly do the work in front of
them. The failure is that **the work between the parcels belongs to
nobody**, and it is invisible because every parcel's own gate is green.

The canonical instance: four parcels built one feature, every gate
passed, and the feature did not work. The tests for one half drove a
stand-in for the other half — a stub whose own header said to re-point
the tests once the real thing landed. It landed. Nobody did. So the
whole path had never once been executed, and the load routine happily
reported "restored exactly" for a restore that had not happened, because
it validated the *file* rather than what reached memory.

Nobody was wrong. The seam belonged to no parcel.

### Two rules that prevent most of it

**Exactly one file owns each shared fact; everyone else includes it.**
When the same fact is stated twice, the copies drift — not might, do. In
the instance above a single count was written by hand in four places and
a name list in a fifth; growing the list broke all six in different
ways, including a gate that passed while printing "only 50 of 48".

**Derive counts and name lists; never transcribe them.** There are two
grades of this and it is worth being precise, because a brief that
conflates them is wrong about the thing it is protecting.

- **Derived**: the consumer reads the definition, so there is one value
  and no way to disagree — a test that greps the header for a `#define`.
- **Declared once and checked**: the count is still a literal, but it
  sits beside the list it counts and a selftest asserts it against the
  list, so a disagreement surfaces on the next run.

Ask for the first where it is possible and the second where it is not,
and do not call the second the first.

The payoff is immediate and visible. When a constant moved from one
header to another, the test that *reads* it stopped with `no #define
CFT_MAX_BODIES in src/ias15_cft.c`, naming the file it could not find it
in. A transcribed copy would have gone on silently testing a stale
number. **A test that breaks when you move a definition is working.**

---

## 2. P0: make the shared thing shared, before you split

Before dispatching anything, list every file each parcel would touch.
**Anything appearing in three or more columns is not a conflict to
manage — it is the first parcel, and it is the lead's.**

The diagnostic is mechanical. In the measured round, five parcels each
removed one entry from a list that was stated in four places: two
functions, a test, and a table in the README. Five agents editing four
files each is twenty edits and a guaranteed drift. P0 turned the list
into one table that both callers walk, and **unlocking a capability
became deleting one row.**

**Aim for a glob, not a list.** Even after that P0, every parcel still
had to add its file to a build variable, a declaration to a header, and
a call to a `main()` — four one-line edits in shared files, so every
merge conflicted in the same four places. Trivial is a P0 win over what
it would otherwise have been, but *zero* was available: had the build
globbed a directory and the entry points been discovered rather than
declared, the parcels would have shared no file at all. When you design
the refactor, ask what would make the seam **disappear**, not what would
make it small.

Two conditions:

- **It must preserve behaviour**, proven by running the full suite
  before and after. A P0 that also fixes things is a P0 whose green
  suite means nothing.
- **It must land and be pushed before any parcel starts**, so every
  worktree branches from it. A P0 landing mid-round is worse than none.

### Make the registry self-enforcing

When P0 turns scattered statements into a table, make the test **walk
that table and fail by name, in both directions**:

- a row no test exercised → fail, naming the row;
- a test naming a row that no longer exists → fail, naming the test.

The first stops a capability being added untested. The second catches a
test left behind when a capability is *removed*, which is the one a
round of deletions will actually hit.

This earned its place on the first run: four rows had never been
exercised by anything. The table did not create that gap, it revealed
it.

Then prove the check can fail — add a dummy row, confirm the failure
names it, remove the row.

---

## 3. The brief

Sections, each here because leaving it out cost something. The
template is [templates/brief.md](templates/brief.md).

**Start here** — what to read, in what order, with paths. An agent that
has read the post-mortem does not repeat it.

**Your job** — one paragraph. If it needs three, the parcel is two
parcels.

**Files you own** — by path, and by *function* where a file is shared.
"`choose_timestep()` in `src/engine.c`, and nothing else in that file"
is a workable boundary; "the step control" is not.

**Files you must NOT touch, and who owns each.** Naming the owner
matters: a boundary with a reason behind it gets respected, an arbitrary
one gets litigated in the report.

**The small edits outside your files that ARE expected**, enumerated.
Without this an agent either avoids a necessary edit and delivers
something that does not build, or reads the absence of a rule as
permission and sprawls. Say "one declaration here, one line in the build
file, one call in `main()`" and that is what you get.

**How to make the tree buildable**, if that takes a step. Three parcels
in one round each discovered independently that a directory their brief
told them to read did not exist in a fresh worktree, and each solved it
from scratch. One line in the brief.

**The base commit, and an instruction to verify it.** A worktree does
not necessarily branch from where you think: one parcel found itself a
merge behind the SHA its brief named, noticed, and reset. Say the SHA
and say "check you are on it".

**Host build traps, as verbatim commands.** Not "build it" — the exact
invocation, including whatever is non-obvious on this machine. An agent
will rediscover these in forty minutes; you can spend three lines.

**Working rules learned the hard way** — the two or three
environment-specific traps that have actually cost hours. Keep the list
short and true; a long one gets skimmed.

**The negative control, named specifically.** See §5.

**Do not** — push, merge, rebase, or commit to the main branch; weaken
an assertion to make something pass; fix anything outside scope.

**Report format**, always including *"anything you found that the brief
got wrong."* This is the highest-yield sentence in the whole system.

### Verify the constraints you write down

A forbidden-files list carried from another project is noise at best.
Four of the six files named "never edit" in one round's briefs **did not
exist in that repository** — they belonged to a sibling repo and the
list came across unchecked. Harmless as a prohibition; the same
carelessness in an *owned*-files list sends an agent to edit the wrong
thing.

Check that every path in a brief exists before you send it.

### Expect boundary violations, and judge them on disclosure

A seam drawn by function is a hypothesis like any other, and one round
falsified three of five. A parcel told to own the step control found
that the setting it was implementing also changes a *different*
function; another needed one call in a function its brief never
mentioned; a third put its plumbing in an existing file rather than the
new one the brief named, because a new object would have meant a larger
edit to the build than the code was to the file.

All three were right, and all three said so unprompted. That is the
standard: **judge a crossing on whether it was disclosed and reasoned,
not on whether it happened.** A parcel that silently stays inside a
wrong boundary ships something half-implemented; a parcel that crosses
one quietly is the thing the ownership list exists to prevent. Ask for
the disclosure explicitly and you get it.

---

## 4. The ledger

A brief is written once, at dispatch, and cannot be updated. Everything
learned while the parcels are running otherwise reaches them **never** —
it arrives in a final report, after the sibling who needed it has
finished.

Three things from one round:

- three parcels independently hit the same setup problem and each solved
  it from scratch;
- one parcel ended its report with a paragraph headed "for P3" — which
  reached P3 hours after P3 had made the same discovery itself;
- the lead learned at the second merge that a refusal was refusing
  something correct, with three agents still running and no channel to
  tell them.

So: **an append-only ledger the agents read and write while they work.**
Drop-in text at [templates/ledger.md](templates/ledger.md).

**Where it lives matters.** Agents in worktrees cannot see each other's
files — that is what a worktree is. The ledger sits outside every
worktree, at a fixed absolute path each brief states, and is **ignored
by version control** so it never conflicts and never lands in history.

**One file per author, append only.** Not one shared file: concurrent
appends lose writes, and per-author files make locking unnecessary by
construction. Everyone reads the directory; everyone writes only their
own, and corrects an earlier entry by appending beneath it.

**Read at three moments**, stated as moments because "periodically"
means never: before starting; before designing anything that touches a
file the brief called shared or forbidden; before writing the report.
These are the floor, not the mechanism — see the push channel below.

**Write when it clears the bar** — *would this have changed another
parcel's work, or the lead's?* Three things do: environment and setup
facts; a brief that turned out wrong (the moment you find it, not in
your report); a finding about shared code. Progress and plans do not. A
ledger full of status is one nobody reads.

**Mark what you measured.** Every entry says which claims were measured
and which believed. Agents build on each other's entries and an
unverified claim propagates faster than a verified one.

**The lead writes to it too**, and this is half the value: it is the
only channel for correcting a brief after dispatch.

### Reading it is a polling schedule; add a push channel

Three read moments are a schedule, and a schedule's latency is its
interval. An agent that reads at the start, designs for an hour, then
reads again before touching a shared file will sit on a correction
posted ten minutes in for the other fifty. That is the difference
between a note that saves an hour and a note that arrives after the hour
is spent.

So **watch the ledger as well as reading it**, with a file watcher that
turns a new entry into a notification. Where the agent runtime offers a
monitor primitive — a background command whose every stdout line becomes
a notification — one poll loop over a directory is all it takes.

Three things make this work rather than backfire.

**1. Push PLUS pull, never instead.** A watcher that has died — timed
out, been killed, been auto-stopped for volume — looks exactly like a
ledger with nothing new in it. Silence is not success. The three read
moments stay as the floor and the watcher is latency reduction on top;
if an agent notices its watch is gone, it re-arms *and* does a full
read.

**2. Split the channel by urgency, not by author.** Most entries matter
to one parcel in four. Watching everything means every agent pays a
notification for every entry, most of them irrelevant — and a runtime
that throttles or stops a noisy watch will turn the push channel off
without saying so. So:

- `ledger/urgent/` — **watched.** One file per message, and the bar is
  "stop what you are doing and read this". Mostly the lead: a brief that
  turned out wrong, a merge that invalidated an assumption, a parcel
  told to delete something that turned out to be load bearing.
- `ledger/<author>.md` — **polled** at the three moments. Everything
  else.

This is what turns the ledger from a noticeboard into a channel the lead
can actually *send* on, which is the half a brief has never had.

**3. Emit the routing line, not the entry.** The watcher should print
the headline and the `For:` line, nothing more, so an agent decides in
one glance whether to go and read. A notification that dumps a paragraph
costs the same attention as the interruption it was meant to save.

**One file per urgent message, written atomically** — compose it
elsewhere and rename it into place. A new file is an unambiguous event,
and rename-into-place means a watcher can never catch a half-written
one. Appending to a shared `urgent.md` reintroduces both problems.

A shape that works, polling every twenty seconds and emitting one line
per new message:

```bash
U=<ledger>/urgent; mkdir -p "$U"
seen=$(ls "$U" 2>/dev/null | sort)
while true; do
  cur=$(ls "$U" 2>/dev/null | sort)
  comm -13 <(echo "$seen") <(echo "$cur") | while read -r f; do
    head -1 "$U/$f"; grep -m1 '^For:' "$U/$f" 2>/dev/null || true
  done
  seen=$cur; sleep 20
done
```

**Verifiers watch the lead's channel only.** A verifier is paid for
independence, and a stream of "the parcel says this is fine" is exactly
the input that erodes it. Environment facts and lead corrections should
reach it; parcel self-reports should not, until it has formed its own
view.

At the end of the round, fold anything durable into the repository's own
records and throw the ledger away. It is scaffolding, not history.

---

## 5. Gates and negative controls

**A gate that cannot fail is not a gate**, and the ways one dies are
specific enough to check for. All four of these were found in a single
round, and each was found by the parcel that wrote the code the gate was
meant to hold down:

- **Passing against itself.** A mode the implementation silently ignored
  would have left every case comparing the default against the default.
- **Proving nothing.** A case exercising a re-read triggered on step 1,
  when the thing being re-read was still all zeros. Re-read zeros, got
  zeros, passed.
- **Vacuous through the observable.** A control was checked through a
  rounded *view* of a wider state; the underlying difference existed and
  re-converged below the view's last bit, so the control matched and
  could not fail. Fixed by hashing the wide bytes.
- **Inert by construction.** A configuration where the physics made the
  difference *exactly zero* — so the obvious test would have passed with
  nothing implemented at all.

And one more, found by a verifier rather than a parcel: a **bit
comparison** that could be swapped for a **value comparison** and still
pass the entire suite, while silently breaking signed zero.

So: **name each parcel's negative control in its brief.** Not "test it
properly" — the specific control. "A do-nothing routine must leave the
run bit-identical to no routine at all, *and* the active case must
differ from the inactive one." Require the parcel to build it, run it,
confirm it fails, delete the artifact, and **report both results**. A
control described but not run is worth nothing, so ask for its output.

---

## 6. The verifier

For anything hard to check by reading, put a second agent between the
parcel and the merge whose job is to *disconfirm*. Template at
[templates/verifier.md](templates/verifier.md).

**Inputs:** the brief, the diff, and the parcel's claimed results.

**It must:**

- **re-run the gate itself**, from a clean build, rather than trust
  pasted output;
- **re-run the negative control**, or build one if the parcel did not;
- **diff the changes against the ownership list** — anything outside is
  a finding, even if it looks correct;
- look for the specific cheat shapes: an assertion loosened, a tolerance
  where exactness was required, a skipped case, a constant transcribed,
  a `TODO` where work was claimed;
- **verify the "nothing else regressed" claim by running the rest**, not
  by reading it.

**It must NOT fix anything.** A verifier that edits is a second author
with none of the first one's context, and you lose the independence you
paid for. It reports; the parcel or the lead acts.

**When it is worth the extra agent:** the gate is slow, so there is a
real chance it was not run; the change touches a numerical invariant, a
hot path, or anything where "looks right" and "is right" come apart; the
report claims green without pasting output; or the parcel is the long
pole, where a late problem is most expensive.

**Its own failure mode is rubber-stamping.** Require it to state what it
actually ran, command by command, and make **"found nothing" an
acceptable, unpenalised answer**. A verifier under pressure to produce
findings invents them, which is worse than none.

### What verifiers actually returned

**Give it a numbered list to attack, and expect its best work to be
outside the list.** One run confirmed all eight items it was handed and
found two genuine divergences nobody had thought to ask about. Eight
confirmations were worth the run; the two findings were worth more. Name
what you suspect, then ask explicitly what *else* is there.

**Distinguish "the shipped code is right" from "the gate would catch it
if it weren't."** Four of one run's findings were the second kind.
Those are worth as much as defects, because they are the defects of the
next change, and a verifier is the only role positioned to notice them.

**A false claim in a comment is a finding.** One verifier disproved a
statement in the code — "this file is byte for byte what we wrote
before" — by writing the file at both commits and comparing. The
behaviour was fine; the sentence was not, and a sentence in the code is
something the next person will rely on.

**One technique worth copying.** To prove a change did not touch a build
it was not supposed to, diff the **preprocessed translation unit** at
both commits, not the source. In one case the same file compiled two
ways and only one was in scope; the preprocessed output was 3610 lines
each and differed by one line. That settles the question in a way
reading a diff cannot. Comparing the compiled object's hash is the same
idea, cheaper.

---

## 7. What the lead keeps

- **P0.**
- **The seam tests.** They belong to no parcel, which is exactly why
  they get skipped. Each merge should get a test exercising *two*
  parcels together. The test that would have caught the canonical
  failure is nine lines and runs in under a second.
- **Files that are the lead's alone** — the README, published docs, CI
  config. Not because agents cannot write prose, but because those files
  state the project's claims and the claims must be one voice.
- **Every merge, and the full suite after each one.**
- **The ledger's own file**, and folding it into the record at the end.

### Habits

**Never merge on the strength of a report.** Run the suite yourself.
Agents report in good faith and are sometimes wrong about what their own
change did.

**Resolve conflicts from what the VCS says is conflicted**, never from
what the merge output happened to print, and assert that no marker
survives before you stage. One lead resolved the two files the merge
message named, staged everything, and committed a third file still
holding its conflict — along with eight agent worktrees as embedded
repositories.

**Never merge while a suite is running.** This looks safe — the suite
built its binaries at the start, so a source edit cannot reach it — and
it is wrong for any part of the suite that is *interpreted*. One lead
merged mid-run on exactly that reasoning; the run reached a scripted
checker, read the merged parcel's **new** script off disk, and drove it
against the **old** compiled binary, producing three failures that were
entirely self-inflicted. A suite is only as prebuilt as its
least-compiled component, and scripts are never prebuilt.

**Read the log, not the exit code.** A background wrapper once reported
exit 0 for a run whose log said `Error 1`, because a trailing `echo`
succeeded. And when a failure is not immediately attributable, check
timestamps before diagnosing — comparing a binary's build time against a
script's mtime settled the case above in one command. Never call such a
failure a defect *or* a false alarm until a clean re-run says which.

---

## 8. Sequencing

- **Dispatch the long pole first.** It sets the merge order and it is
  where a late problem hurts most.
- **Hold any parcel that shares a file intimately with another** until
  the first lands. A VCS will merge two disjoint functions in one file
  without complaint; what it cannot merge is one parcel reshaping the
  thing another is hooking into.
- **Parcels finishing early is fine.** Merging is serial, and the
  constraint is not the merge but the **suite run after it**. Budget it
  explicitly: at twenty-five minutes a run, five parcels is two hours of
  waiting nobody plans for. Where two parcels share no file, merging
  both and running one suite is a defensible trade *if you say you made
  it* — a failure then costs a bisection over two candidates, cheap when
  each arrived green on its own.
- **Re-brief from what comes back.** The first report usually corrects
  the plan. Fold it into the remaining briefs, and into the ledger for
  the ones already running.
