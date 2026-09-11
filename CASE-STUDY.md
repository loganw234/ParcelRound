# One round, measured

The numbers behind [METHOD.md](METHOD.md). A method doc that cannot say
what it caught is an opinion.

## The setting

A ~15,000-line C project: a numerical integrator re-implemented so that
every floating-point operation goes through a software library, letting
the same code run at 64-, 128- and 256-bit precision. At 64-bit it must
reproduce the original **bit for bit** — every gate asserts that, and
"close enough" is never an acceptable answer anywhere in the suite.

That exactness matters to the case study in one direction only: it makes
failures unambiguous. It does not make the method precision-specific.
Any project with a suite you trust gets the same shape of result.

An earlier round on the same codebase had produced the canonical
failure — four parcels, four green gates, a feature that did not work,
because the seam between two of them belonged to nobody. This round was
designed against that.

## The shape of the round

One **P0** by the lead, then five **parcels** in parallel worktrees, two
**verifiers**, and one follow-up parcel spawned from a verifier's
findings. The lead merged serially and ran the full suite after each
merge.

P0 was two refactors: a capability list that was stated in four places
became one table both callers walk, and a 718-line single-`main()` test
file became a file per topic plus a header saying how to add one. After
it, unlocking a capability was deleting one row, and a parcel's only
shared-file edits were four one-line additions.

## What the system caught

**Twelve brief errors, from all five parcels.** Every single parcel
corrected its brief. The most consequential: the lead had described a
callback mechanism as an *addition* of an exactly-representable value,
so the total would be "wide arithmetic plus an exact addend, correctly
rounded". It is a **replacement** — the callback returns only the
narrow total and there is no addend to recover. The parcel worked that
out, proved the alternative was not bit-exact with a two-line
counterexample, and shipped replacement narrowed by a bit comparison.
The feature's cost at wide precision is materially different from what
the brief said, and nothing else would have surfaced that.

Others included: a setting the lead thought reached one function
reaching two; a flag the lead thought was live being overwritten by the
caller on every step, so refusing it had been refusing something
*correct*; and a piece of state the lead had catalogued as dead turning
out to be read before it was written.

**Four gates that could not fail** — each found by the parcel that wrote
the code the gate was meant to hold down, unprompted:

1. A control that disabled a newly written branch left **every case
   passing**. The parcel swept for a configuration that discriminates,
   found one, added it, and the control then failed on exactly the
   affected mode.
2. A case exercising a re-read of stale data triggered on **step 1**,
   when the data being re-read was still all zeros.
3. A control was observed through a *rounded view* of a wider state. The
   underlying difference was real but re-converged below the view's last
   bit, so the control matched at two of three precisions and **could
   not fail**. Fixed by hashing the wide bytes into every dump.
4. With massless particles, the feature under test was **bit-inert** —
   every removed term contributed exactly zero and ordering was
   preserved, so the obvious test case would have passed with **nothing
   implemented**. Every divergence control was moved onto massive
   particles.

**A fifth, found by a verifier:** a `memcmp` that decides whether a
value keeps its wide precision can be swapped for `!=` and **pass the
entire suite** while silently breaking signed zero.

**Two verifiers, both productive.** Each confirmed every item on the
list it was given, and each found things that were not on it:

- the first found that a callback writing any field other than the one
  the port read back was **silently discarded** where the original would
  have used it — through three separate channels, 15 of 21 values
  differing in each — plus four places where correct code had nothing
  holding it down;
- the second disproved a claim written in the code (*"byte for byte what
  we wrote before"*: measured 10,590 → 10,783 bytes), confirmed an
  upstream defect in the dependency and found a **new consequence** of
  it — that mixing builds across one commit inside one archive produces
  an unloadable file in one direction — and caught a hash seed
  mislabelled as a standard one **and hand-copied into a second file,
  three hours after the project wrote down its rule against
  transcribed constants**.

**Two previously unrecorded defects**, one of them upstream in a
third-party dependency, reproduced minimally rather than inferred.

## What the lead got wrong

Worth recording, because three of the doc's rules came from these.

1. **Committed a merge with an unresolved conflict in it**, plus eight
   agent worktrees as embedded repositories — by resolving the two files
   the merge message named, then staging everything without checking
   what the VCS still considered conflicted.
2. **Merged while a suite was running**, reasoning that the suite's
   binaries were already built so source edits could not reach it. True
   of the compiled gates, false of the scripted ones: the run read a
   newly merged script off disk and drove it against the old binary,
   producing three failures that were entirely self-inflicted. Diagnosed
   by comparing the binary's build time against the script's mtime.
3. **Carried a forbidden-files list across from a sibling repository**
   without checking. Four of the six files named "never edit" did not
   exist in the repository being worked on.

## What it cost

- **Every merge conflicted**, in the same four places every time, and
  every one was trivial — a P0 outcome, not luck.
- **Suite time dominated.** ~25 minutes per run, serial. Four merges is
  most of a working day of waiting, and it is the thing nobody budgets.
- **Three parcels independently solved the same setup problem**, because
  there was no channel between them. That is what the ledger is for, and
  it was added at the end of this round rather than the start.

## What the numbers say

The parcels were fine. Agents given a clear boundary and a named control
did careful work, found their own vacuous gates, and disclosed every
boundary crossing unprompted.

What the system surfaced, repeatedly and fast, is that **the lead's
model of the code was wrong** — twelve times, and in three of five
places where the lead drew a seam by function. That is the return on the
method: not that it makes agents trustworthy, but that it makes the
plan's wrongness visible in hours instead of at integration.

The single cheapest line in the whole system asks for exactly that.
