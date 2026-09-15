# A second round, recorded as it runs

The first case study ([CASE-STUDY.md](CASE-STUDY.md)) was written after
the fact, from a round that produced the method. This one is written
**during** the round it describes - one of the first applications of
the method since it was extracted - so that what the method predicted
and what happened can be set beside each other with timestamps rather
than reconstructed. It is a draft until the round ends; the final
section says what METHOD.md should say differently.

## The setting

cft-fp256: a deterministic floating-point coprocessor for an Alveo U50
- RTL, a Python golden model that is the authority, a C library with
software, XRT and remote backends, nine language bindings, and a
conformance census in the millions of cases. The invariant is bit
identity across every backend and the tile, and anything the hardware
cannot do is refused by name. The requester is a second repository, an
N-body integrator ported onto the library, whose own document ranks the
things it wants.

The round: four asks from that document deferred from an earlier
round - a device-side scatter, a gather, a per-run lane mask, a scalar
broadcast. Lead: one Claude session (the author of this record).
Parcels: Opus agents in git worktrees of the same repository. The
build box and the card belong to the lead; the parcels see neither.

## Timeline (2026-09-15, local time)

| when | what |
|---|---|
| 02:00-03:30 | The plan written (`cft-fp256/docs/ROUND2.md`, ~850 lines: the seam, five briefs, two verifiers, the ledger, the merge order), after reading both repositories rather than remembering them. |
| 03:30 | Plan delivered; Logan approves the ABI shape and dispatching every parcel, including the two the plan had flagged as optional or low-value. |
| 04:00-05:15 | P0 written and built on the host: ABI 0.14 declared and refused everywhere, five registers, VERSION 0xA00, seventeen kernel arguments, the model's signature, eleven new refusal checks. |
| 05:13-05:16 | Host gates green. A Python harness's hand-declared ctypes struct refused by the size handshake (74 disagreements at once) - the first thing P0 found. |
| 05:18-06:30 | Proofs: the runner's quick budget (22/25 ok; two skips for tools off PATH; two FAILs, neither the seam's), the box's Verilator suite, multi-pass census, Icarus confirmations, lint. |
| 05:40 | Ledger created outside every worktree; lead.md seeded with environment facts and two rules from the day before; the lead's watcher armed over the whole directory. |
| 06:0x | The plan's paths re-checked before dispatch: `bind_role` named in the wrong file in two briefs. Corrected on main and noted in the ledger. |
| 06:3x | Logan: "we may want to utilize the quick tests" - dispatch on the Verilator suite, census and lint; Icarus confirms in the background. |
| 06:40 | **P1** (indexed inputs, the long pole) and **P4** (beat-wide accumulator, disjoint files) dispatched. |
| 06:45 | The Icarus tail lands, all green; nothing changes. |
| 07:0x | **P1 escalates through `urgent/`**: the plan's ownership list forbids the one CSR edit its brief requires; the dispatch message had granted it; the dispatch said the document wins. P1 stops and asks instead of guessing. |
| 07:05 | Lead answers on `urgent/` (~10 minutes after the escalation), decides once for P1 and P3, corrects the plan on main. |
| 07:20 | P4's first two ledger entries: the brief's rate claim is an asymptote (100% adder utilisation), the target is the memory's rate; and a disclosed crossing into the module's bench wrapper. |
| 07:30 | Lead acknowledges both in lead.md. |
| 08:05 | **P4 finds a gate defect with its own negative control**: a single bench target exits 0 when its tests fail (only the full suite runs the results checker). Also its measurement: fp32 sum 11.3 -> 1.4 cycles a beat, every declined shape cycle-identical. |
| 08:15 | Lead puts the gate defect on `urgent/` for every parcel and verifier, corrects every brief's build section on main. |

## Observations against the method, so far

**§1, the lead's model is wrong - but this time before dispatch.** The
first case study's headline was that every parcel corrected its brief.
Here the plan itself, written from reading both repositories rather
than from memory, found three things the ask list had wrong before any
parcel existed: one ask had already shipped three days earlier and was
never marked done; two asks were one mechanism (the requester's
"scatter" is a table gather followed by a fixed-order fold, not a
scatter-add); the third's value had a two-percent ceiling by the
requester's own table. Reading the upstream's code, not its summary,
is where that came from. The method should say so as a step: *read the
requester's implementation, not its ask.*

**§2, P0 preserved behaviour, and the proof found three unrelated
things.** The seam - every new field refused by name, every new bit
zero - did what §2 asks, and running the whole suite on both sides of
it found (a) a harness mirroring a C input struct by hand, refused at
its old size (the size handshake working as designed, on a caller
nobody had listed); (b) a generated table stale since an earlier
commit; (c) a language leg broken for eleven days on this host,
untested since. None was the seam's. §2's "run the full suite before
and after" is what made them visible; a P0 proven only by its own
tests would have missed all three.

**§3, "verify the constraints you write down" - done, and still not
enough.** Every path in the plan was checked to exist. A function was
still named in the wrong file in two briefs; a second pass, checking
what each named function *is* rather than whether it exists, caught it
before dispatch. What that pass did not catch: an ownership list that
forbade a file the parcel's own job required (the CSR's reserved-bits
guard). The seam's own code comment said the parcels would change it;
the plan's list said they must not. **Two artefacts stated one fact and
drifted** - §1's own rule, violated by the lead in the plan.

**§4, the urgent channel, first live use in this round: it worked in
both directions within twenty-five minutes of dispatch.** P1 found the
contradiction, wrote one file into `urgent/`, and *kept working on the
narrower grant* rather than stopping cold; the lead's watcher fired,
the answer went back through the same directory ten minutes later, and
the decision was made once for the parcel that would hit the same wall
in wave 2. The rule "the document wins where the dispatch disagrees"
was written for the case where the document is the more careful of
the two; here it was the less careful, and the rule's cost was one
escalation rather than an hour on a wrong path - which is the channel
working, not failing.

**§4, the lead's watcher echoes the lead's own entries.** Every entry
the lead appends comes back as a notification. Harmless, but noise;
the watcher loop should skip the author's own file.

**§5, a parcel's negative control found a gate that could not fail.**
P4, told to break one pairing and watch the bench name the size, saw
the bench fail *and the container exit 0*: cocotb cannot set an exit
code, and only the full suite runs the checker. Every brief in the
round told parcels to run single targets. The method's §5 is exactly
about this shape, and the control it demands is what found it - on the
first parcel to run one. Propagated to every parcel in ten minutes
through `urgent/`; the durable fix (each target running the checker
itself) is the lead's, after wave 1, because the file is in every
worktree.

**§3, the brief got the mechanism's arithmetic wrong.** P4's brief said
"a beat a cycle"; the parcel measured the serial path at 1.41 cycles an
element (not 1.0) and argued that epb adds a beat against epb adders is
100% of the port with no margin. Same lesson as the first case study's
"the lead described a mechanism backwards in a way that changed what
the feature cost": the lane arithmetic was right, the rate was an
asymptote, and the parcel corrected it in its first hour and built to
the honest target.

**§3, a boundary crossing judged on disclosure.** P4 had to edit the
module's bench wrapper (a new port; the simulator treats a missing pin
as fatal). It said so in the ledger before doing it, said what the diff
would contain, and named the reviewer. Approved in the next lead entry.

**Costs, so far.** The lead's time went overwhelmingly to P0 and its
proofs (about three hours) and to the plan (ninety minutes); the two
dispatch briefs took minutes because the plan already was the brief.
The escalation and the gate defect each cost the lead about fifteen
minutes to answer and propagate. Parcel wall time: P1 and P4 both
still running at 08:30.

## What is not yet known

The merges, the verifiers, the seam tests, wave 2 (P2, P3), the image
and the card day. This section is replaced as they happen.

## What METHOD.md should say differently (draft, to be settled at the end)

- Add to §2 or §3: **read the requester's code, not its ask list**;
  the plan's largest corrections came from there, before dispatch.
- Add to §3: a brief's ownership list is a statement of the same fact
  the seam's code makes; **derive the list from the seam's own
  comments**, or at least diff the two before dispatch.
- Add to §4: the lead's watcher should **skip the lead's own file**.
- Add to §5: **a single test target's exit code is not a verdict** in
  any suite where the harness cannot set one; say in the brief which
  command *is* the verdict.
- Add to §8: when the confirming simulator is ten times slower than
  the iterating one, **dispatch on the fast one and let the slow one
  confirm in the background** - the round's owner said so, and the
  confirmation changed nothing.

**§3, a working rule stated as a prohibition was broken under pressure, and disclosed within minutes.** lead.md's environment entry said "never kill a process by image name; your own PIDs only". P4, with a hung lint container, ran `docker kill $(docker ps -q --filter ancestor=cft-sim)` twice (08:09, 08:11) and killed five containers, two of them P1's benches. It noticed within four minutes, wrote one file into `urgent/` naming the container IDs, the commands, what P1 would have seen ("a hang, a truncated log, a missing results.xml - that was me, not your RTL") and what it had changed. Two lessons for the method: (a) a rule that protects a sibling must be written as **the command to use**, not only the command to avoid - "`docker ps --no-trunc`, then kill one ID whose command line is yours" survives pressure where "never kill by name" did not; (b) the disclosure standard held - prompt, precise, actionable by the victim - and the lead judged it on that, as §3 says. Cost: P1 re-runs whatever was in flight in those two minutes; the lead spent ten minutes.

| 08:15 | **P4 discloses on `urgent/`** that a blanket `docker kill` of every sim container at 08:09/08:11 took two of P1's benches with it; names the IDs, the commands, and what P1 will have seen. |
| 08:25 | Lead acknowledges, restates the rule as the command to use. |
