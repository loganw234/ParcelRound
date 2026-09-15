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

## Timeline (2026-09-15, local time; commit times and file mtimes where they exist, `~` where only an agent's own stamp does)

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
| 06:30 | **P1** (indexed inputs, the long pole) and **P4** (beat-wide accumulator, disjoint files) dispatched. |
| 06:31 | The Icarus tail lands, all green; nothing changes. |
| 06:32 | **P1 escalates through `urgent/`** (two minutes after dispatch): the plan's ownership list forbids the one CSR edit its brief requires; the dispatch message had granted it; the dispatch said the document wins. P1 stops and asks instead of guessing. |
| 06:33 | Lead answers on `urgent/` (one minute after the escalation), decides once for P1 and P3, corrects the plan on main. |
| ~07:20 | P4's first two ledger entries: the brief's rate claim is an asymptote (100% adder utilisation), the target is the memory's rate; and a disclosed crossing into the module's bench wrapper. |
| ~07:25 | Lead acknowledges both in lead.md. |
| ~07:30 | **P4 finds a gate defect with its own negative control**: a single bench target exits 0 when its tests fail (only the full suite runs the results checker). Also its measurement: fp32 sum 11.3 -> 1.4 cycles a beat, every declined shape cycle-identical. |
| 07:33 | Lead puts the gate defect on `urgent/` for every parcel and verifier; the briefs' build sections corrected on main at 07:34. |

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

**§4, nobody in the round knew what time it was.** The lead's ledger
headings from mid-morning on ran up to ninety minutes ahead of the
clock, and P4's ran thirty-five minutes ahead; both were guessed, not
read. The first draft of this timeline copied the guesses. Commit
times and file mtimes told the truth when checked: P1's escalation was
two minutes after dispatch and the answer one minute after that, not
twenty-five and ten. The method's entry format should carry a
machine-written stamp - `date` in the entry, or the watcher stamping
what it sees - because a timeline is the measurement the case study
rests on, and this one had to be reconstructed.

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
- Add to §4: **stamp entries mechanically** (`date` in the entry, or the
  watcher stamping arrivals); every human-typed time in this round was
  wrong by up to ninety minutes.
- Add to §5: **a single test target's exit code is not a verdict** in
  any suite where the harness cannot set one; say in the brief which
  command *is* the verdict.
- Add to §8: when the confirming simulator is ten times slower than
  the iterating one, **dispatch on the fast one and let the slow one
  confirm in the background** - the round's owner said so, and the
  confirmation changed nothing.

**§3, a working rule stated as a prohibition was broken under pressure, and disclosed within minutes.** lead.md's environment entry said "never kill a process by image name; your own PIDs only". P4, with a hung lint container, ran `docker kill $(docker ps -q --filter ancestor=cft-sim)` twice (08:09, 08:11) and killed five containers, two of them P1's benches. It noticed within four minutes, wrote one file into `urgent/` naming the container IDs, the commands, what P1 would have seen ("a hang, a truncated log, a missing results.xml - that was me, not your RTL") and what it had changed. Two lessons for the method: (a) a rule that protects a sibling must be written as **the command to use**, not only the command to avoid - "`docker ps --no-trunc`, then kill one ID whose command line is yours" survives pressure where "never kill by name" did not; (b) the disclosure standard held - prompt, precise, actionable by the victim - and the lead judged it on that, as §3 says. Cost: P1 re-runs whatever was in flight in those two minutes; the lead spent ten minutes.

| 08:14 | **P4 discloses on `urgent/`** that a blanket `docker kill` of every sim container at 08:09/08:11 took two of P1's benches with it; names the IDs, the commands, and what P1 will have seen. |
| ~08:16 | Lead acknowledges, restates the rule as the command to use. |

**§2, the seam put a refusal where the parcel would remove it.** P0 refused every new field in one function, and told P1 to turn that function's refusals into bounds checks. P1 noticed that doing so would have let the REMOTE backend - which has no field for a table - run the dense stream and return wrong elements with clean flags, and added a refusal in the remote route itself. The method's §2 says the seam should make shared facts shared; here the seam made one refusal stand for three backends, and the parcel removing it for one backend silently removed it for the others. **A refusal at a seam belongs in every backend that cannot yet do the thing, not in the one place the first parcel will edit.**

**§3, the brief's cost model named a divisor that did not exist.** The P1 brief said a gathered element costs a round trip "divided by the reads in flight"; the sequencer issues one burst at a time, so there is no divisor. And the plan's three-instruction fold sketch accumulated into a register that is an input stream. Both corrected by the parcel from the code within its first two hours, both fixed in the plan the same hour; neither would have been caught by "every path exists".

| 08:2x-08:32 | P1 posts seven entries: the CSR diff as granted; a bench expectation now derived from both CAPS2 bits; a remote-route hole the seam left and P1 closed; the software backend publishing INDEXED; doc counts are the lead's; the read side is one burst in flight (a gathered element is a whole round trip); the plan's fold sketch used an input stream as the accumulator. |
| 08:32-08:33 | Lead decides the caps consistency on `urgent/`, corrects the plan for the last two, acknowledges the rest. |

| 08:54 | **P1 reports**: 2 h 24 min wall, 279 tool uses, ~530k tokens; eight commits; every gate quoted by the checker; three controls shown failing; five brief corrections; six disclosed crossings, all previously approved through the ledger. |
| 08:57 | **V1 dispatched** against P1's tip with a twelve-item attack list; the box runs the full suite at the same tip in parallel. Nothing merged on the report. |
| 09:04 | **The lead's seam test** (§7): a gathered program between segmented reductions on one tile, written in the lead's own worktree at P1's tip while V1 runs; 2/2 with the checker. It belongs to no parcel, which is exactly why the method says the lead writes it. |
| 09:06 | **P4 reports**: 2 h 37 min wall, 209 tool uses, ~490k tokens; three commits; 8.0x marginal on the fp32 sum with every bit unchanged; every gate by the checker; six brief corrections, among them that the brief described the tree as sharing the accumulator's issue port when it uses the other lanes of the same beat-op - the brief's own lane arithmetic contradicted its own prose. |
| 09:08 | **V4 dispatched** against P4's tip. The plan had no verifier for P4; the method's own criterion (a numerical invariant on a hot path) says there should be one, and the lead followed the method over the plan. |

**§6, the plan under-provisioned verifiers and the method corrected it.** The plan named verifiers for P1 and P3 only. P4 changes the pairing path of every reduction - a numerical invariant on a hot path, which §6 lists as exactly when a verifier is worth the agent. The lead dispatched V4 anyway. Worth stating in the method: a verifier is chosen by what the parcel touches, decided at dispatch of the verifier, not fixed in the plan.
| 09:14 | The lead fixes the gate defect on main (every bench target runs the checker), proven both ways on one bench, before wave 2's briefs are written. About a hundred minutes from P4's finding to the durable fix. |
| 09:29 | **V1's first entries**, thirty minutes into its list: a pre-existing decode rule (any operand field below three marks a stream as needed) that the gather turns from a beat read into a whole table plus a round trip per entry; the XRT path staging an indexed source at the dense size; the parcel's own device-test leg reading past its buffer and passing because the deposits do not depend on it. P1 sent back to fix all three; V1 continues. |

**§6, the verifier found within thirty minutes what the parcel's green gates could not.** Three findings, each of a shape §6 names: a false sentence in a docstring ("the fold names no stream"), measured wrong by counting bursts; a staging size unreachable from any gate on this host (no XRT build, no card), believed from the source and flagged as believed; and a test that reads past its own buffer and passes because nothing it asserts depends on the bytes it reads - the verifier put the buffer against a guard page to prove it. The parcel's report was honest and its gates were green; the defects lived where the gates could not look. The one the lead most wants in the method: **a rule inherited from an earlier revision can change cost class under a new mechanism** (a defaulted field cost a beat read dense and the whole gather indexed) - the brief should say which existing rules the mechanism makes expensive.
| 09:57 | P1 returns with the three fixes (tip b812a53) twenty-six minutes after being sent back. The decode fix changes the dense path for every program, not only gathered ones, and P1 held it to the model with a bench case that derives operand use for all 256 opcodes from the model's own steering - and fails on a table that is all-three everywhere, so the case cannot pass vacuously. V1 asked to re-check the three on the new tip; the box re-runs the suite there after its Icarus tail. |
| 10:07 | **V4 returns: no defect.** Every gate reproduced from a clean build, quarter added, eleven probes of its own, both fatal guards fired, a pair-preserving permutation shown to pass. Two findings of the second kind: the wide-path-off build is a source edit no gate builds, and the quarter-tile bench was missing from the parcel's list. P4 merged onto a staging branch; the lead makes the switch a parameter so the control becomes a gate. |
| 10:24 | **V4 finds a regression after reporting none**: the reduce-then-program probe - the diagnostic written for yesterday's shared-array hang, and NOT in the suite - fails at P4's tip with a spurious underflow flag, bits correct, with the tree built out too. P4's nine benches and V4's eleven probes all ran reductions back to back, where nothing is left in the array to leak; only a different kind of run first exposes it. P4 sent back; the merge held. |

**§6 and §7, the defect lived in the combination no parcel's gate could reach, and the probe outside the suite found it.** P4's new flag arm reads the array's lane flags on every accepted edge; the array is shared with the sequencer, and the first sixteen edges of a reduction still carry the previous program's work. Every reduction bench runs reductions after reductions, where the idle lanes hold zero, so nine benches and eleven verifier probes passed; the probe written on 2026-09-14 for the shared-array hang - which sits outside `make sim` precisely because it was "a diagnostic, not a bench" - failed at once. Three lessons: (a) the verifier's "found nothing" was honest and provisional, and it kept going into the seam the parcel did not own, which is where §7 says the lead should be looking; (b) a diagnostic that caught a defect once should be in the suite, and this one was not; (c) the shape of the bug is the first case study's canonical failure in miniature - a mechanism correct in isolation and wrong in a sequence its own gates never produce.
| 10:28 | P1 re-reports at b812a53: 3 h 57 min wall in all, 360 tool uses, ~620k tokens, nine commits; every gate green, the dense cycle table unchanged after a decode change that touches every program. The lead promotes the probe that caught P4 into the suite on main. |
