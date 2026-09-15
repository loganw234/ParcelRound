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
| 10:38 | V1 confirms P1's three fixes at the new tip by its own reading of the model, re-runs every gate there, and finds the old stream-loading rule still stated in the RTL declaration and in the document - a false sentence in two places a reader goes first. Fixed by the lead on the staging branch; the branch runs on the box. |
| 10:41 | **V4's final report**: 1 h 32 min, 190 tool uses, ~420k tokens. One defect, ten confirmations, two gate gaps, one latent coupling handed to the next parcel. Its own earlier "found nothing" entry stands in the ledger with the correction appended beneath it, as the ledger asks. Its gate-quality verdict is the sentence the method wants: strong for a pairing break (five of nine cases fail, two of them pre-existing), absent for a flags break (no bench sequences a different run before a reduction). |

**§6, the verifier distinguished the shipped code from the gate, as asked - and the second answer was the useful one.** V4's report closes with two sentences: the gate is strong for a pairing break and absent for a flags break. The first says P4's tests are good; the second says where the next defect will live. The lead acted on the second (the probe into the suite, a regression case into the reduction bench) before the first parcel's fix arrived.
| 10:49 | **V1's final report**: 1 h 52 min, 325 tool uses, ~555k tokens. Everything confirmed at P1's fixed tip, by its own cases as much as by re-running P1's; four "gate would not catch it" items and three false sentences named, two of them the lead's own. P1 resumed for the two real gaps; the lead fixes its own paragraph. |

**§6, the verifier's list was a floor, not a ceiling, and the lead's own artefacts were on the findings list.** V1 built the cases P1 did not (all four tables at once; a dense preload followed by an indexed stream; a whole block of sentinels; a burst-length corner where a misaligned table base would issue a 256-beat read), then checked the parcel's sentences and the LEAD's - the seam paragraph in the public header, written that morning, was out of step on three counts by the time the parcel landed. A brief cannot ask for that; the instruction "tell me what I did not think to ask" got it.

**§6 and §8, the verifier loop under start/stop - measured on two parcels.** P1 went back twice (V1's three findings at 09:27, fixed by 09:55; V1's final report at 10:49 named two gaps, back again), P4 once (V4's regression at 10:25, fixed by 10:54). Each cycle: the parcel's fix took 25-30 minutes because the harness RESUMES the agent with its whole context (a send-back costs no re-brief - the method assumed a brief is written once and that the parcel cannot be re-entered; here it can); the verifier's re-check 20-30 minutes; the box's suite at the new tip an hour, which is the real cost and the one §8 predicts. Not one send-back was a style disagreement: every one was a defect the parcel's own gates could not see (a cost class, a staging size, a test reading past its buffer, a flag arm reading the array in cycles that were not its run's). The alternative - no verifier - would have merged both parcels with those in them, and two of the four would have reached the card. One near-miss worth stating: V4 posted "no defect" before running the one target outside its list, and the lead had P4 merged onto a staging branch within minutes of that entry; the regression note arrived twenty minutes later. "Never merge on a report" held only because staging is not pushing. The method should say: a verifier's report is due when its LIST is exhausted, not when its first pass is, and a merge is a push. And a practice that paid for itself: a second checkout on the build box, so two suites run at once and a send-back does not queue behind a sibling's hour.
| 11:27 | **P4 reports its fix** (tip 778dabf): 4 h 54 min wall in all, 252 tool uses, ~550k tokens; the flag arm now contributes only on its own levels' return strobes, closed by construction; both regression shapes fail with the fix reverted; redprog green under both simulators; the cycle table byte-identical. V1 closes out clean. |
| 11:37 | **P1 is on main** (5c0c655, a fast-forward of the staging branch). The verdict: the box's suite at 1c6b63a (24 benches, the suite-level line present this time, census, lint), the one commit after it shown comment-only by diff, and the host-side gates re-run on the desktop at the tip in six minutes (build, api-test, 66 model tests, the 200-program corpus with its three sub-corpora, device-test both legs, docs index, five generators, the Arduino copy). 5 h 07 min after P1 was dispatched (06:30, this timeline). |
| 11:41 | **The wave-2 briefs amended before dispatch** (d4e4529, e0f211f): twenty minutes of the lead's time converting what the ledger and the verifiers produced into the two sections P2 and P3 read - the opcode read rule, P1's remote route and its three lines, P1's CSR items quoted for P3's mirror, V4's parameter fact, P4's flag fact with the two cases it implies, the one-burst read side, and the regions of P1's in-flight follow-up. A V2 list added: the method's criterion said yes for P2 as it had for P4. |
| 11:43 | **Wave 2 dispatched**: P2 (the composed `cft_run_ex`) and P3 (the lane mask), Opus, isolated worktrees from main at e0f211f. Four agents share the desktop (P1's follow-up and V4 still running). |

**§2, a brief is written once - so the lead's job between waves is to write the next one from the ledger.** The method says the ledger exists because a brief cannot be updated. What it does not say is the corollary the lead met at 11:20: a wave boundary is the one moment a brief CAN be updated, and everything the ledger accumulated (seven urgent files, four author files, two verifier lists) has to be folded into the next wave's sections there and then, or the next wave starts from the plan as it was written the night before, learns the same facts from the ledger in its own time, and the ledger's latency becomes the brief's. Two things made it tractable: the ledger's "For:" lines said which entries were for P2 and which for P3 without re-reading everything, and the lead had been keeping a list of "for the next brief" items in its own notes since the first send-back. The twenty minutes it took is the cheapest twenty minutes in the round. One wording lesson from doing it: a brief that names its base commit exactly is wrong the moment the brief itself is committed on top of that base - name the base "at or after", and put the exact tip in the dispatch message, where it can be right.
| 11:44 | **P1's follow-up reports** (991603f; 5 h 15 min and 425 tool uses for the parcel in all): MODE[22] without a scratch block refused at the header check from the header's own bits; the `-b` leg gates the tables' binding path with a resident-versus-staged assertion no gate had; the stale probe comment fixed. Its rule for P3, in the ledger with a `For:` line: a MODE bit whose selected object does not exist is refused at the header check, never skipped in the state machine. Staged as round2/merged-p1b (29809cb), the box's suite in the first checkout, V1 resumed for a scoped check. |
| 11:50 | **The lead's own gate had a hole.** The `-b` device-test count did not move across a commit that adds a leg - because `make all` does not build the test executables, and the lead's script had been running a device-test binary from 05:13, P0's, on two merge gates. The number that refused to change was the tell; the verdicts stood on the verifier's and the parcel's own builds and on the box, not on the lead's binary. Corrected in the ledger as a correction entry (the 11:37 and 11:48 entries left standing), the script fixed to build every test executable by name and to print their build times. |

**§5, the lead is a participant, not an auditor - and its own artefacts need the same controls it demands.** The lead had written "verify the fact, not its neighbour: a stale binary" into P1's brief that morning and then ran one on two merges. What caught it was not a rule but a number: a check count that stayed exactly equal across a commit whose report said "+20". Two things follow. The lead's gate script should print the build time of every binary it runs - a line that costs nothing and would have said "05:13" at 11:36. And a merge verdict should name what it rests on: this one rested on V1's build, P1's build and the box, and the lead's numbers were decoration - which is why the correction cost a ledger entry and not a revert. The method's §5 says the verifier disconfirms the parcel; nobody disconfirms the lead except the lead's own habit of asking why a number did not move.
| 12:05 | **V4 confirms P4's fix** (2 h 54 min in all, 266 tool uses, ~504k tokens): the defect gone under both simulators; the two new bench cases fail with only the narrowing reverted; an instrumented copy measured the guard doing real work (8,690 flag collections, the earliest at edge 21; the unqualified OR non-zero at edges 0..15 on 127 occasions) rather than being vacuously true; the tap pinned both ways (one stage early fails nine of eleven cases, losing a real flag and gaining a spurious one); nothing outside the tree and the decode changed, by section hashes; the cycle table identical in all 21 rows. Two of V4's "still open" items were already closed on main (redprog in the suite, EN_WIDE through the kernel) - a verifier at the parcel's tip cannot see the lead's branch, and says so. |
| 12:03 | P4 merged into main locally (27c424d, not pushed); the seam test runs on the desktop on the combined P1+P4 tree, which no suite has run; the push waits for the box's suite at P4's staging commit; then the box runs the merged main. Six stated bench counts become twenty-five. |
| 12:18 | **The seam test on the combined P1+P4 tree** (the lead's local merge, 16 minutes on the loaded desktop): redprog 2/2 - a segmented reduction, an indexed fold through the scratch pool, a gathered fold across a block, a reduction again, on one tile - reduce 11/11, reducenowide 11/11, krnlseq 1/1. The two parcels had never run together; the shared-array hand-off where the previous day's hang lived is the thing this test exists for, and it held first time. |
| 12:22 | **The box on P4's staging commit**: 25 benches, the suite-level line present, the census, lint - 58 minutes from launch, three suites sharing the box. |
| 12:24 | **P4 is on main** (a061d3f): the second parcel merged, 5 h 54 min after its dispatch (06:30), one send-back in between. The merge itself was the cheap part: two clean auto-merges, one seam test, one box run. |
| 12:34 | **P3's first findings**, 50 minutes in: four environment facts for its siblings (the remote target's Python default, the unused variable at HEAD, the WSL route to the XRT 2.14 compile check through PowerShell, the XRT file warning-free on 2.14); the two P0 controls it had to flip, disclosed; and a rule question - MODE[23] on an elementwise run is accepted and ignored, the shape MODE[18:16] already has on a program run - asked rather than answered by inventing a refusal. P3 stamped all three entries 13:07, then read the clock, and appended a correction addressed "For: the case study": the guess was 33 minutes ahead. |
| 12:36 | The lead's answer in the ledger within the hour: the rule is one rule already (the build's, not the run's), stated once in the sequencer doc on main; the flipped controls are the expected shape; the merge of the bench file where three neighbours now meet is the lead's by hand. |

**§4 again, the clock.** Every author in this round - the lead three times, P1, P4, V4, P3 - has written a guessed time into a stamped entry at least once, and every guess was AHEAD of the clock (by 3 to 90 minutes), which suggests the guess is "when I expect to finish writing this" rather than "now". The fix that finally held for the lead was mechanical: write the entry with a placeholder and let the append command substitute `date`. P3's self-correction is the other half: an author who reads the clock after writing and corrects in the open. The method should say: stamps are substituted, not typed.
| 12:37 | **P3 measures the value statement's premise wrong**: the lane mask saves no compute on this tile - the sequencer issues per beat, and the active bit decides what is written, not what is computed - so half-masked and all-masked cost the same, dense plus one beat read a block (four cycles), and the early exit sees the mask. The plan had priced ask 5 at up to two percent of a step on "compute and bytes"; the bytes half stands, the compute half was never there. P3 stopped at the brief's line ("if the RTL wants to grow past the block setup and the drains, stop and report") and reported, with the two mechanisms that would buy the compute named and placed outside its ownership. |
| 12:38 | The lead's answer within the hour: the mask ships as built; the beat-skipping is a revision-7 item for the roadmap with P3's numbers as the before-side; the plan's value statement corrected on main the same hour, dated; V3's list gains "the dense column unchanged, re-measured". |

**§2 and §7, the parcel that measures the plan.** The brief's last sentence for P3 was a stop line, written because the parcel was priced small. It fired for a reason the lead had not imagined: not the RTL growing, but the VALUE not being there. P3 did the thing the method asks of a parcel that finds its brief wrong - measured it, named the mechanism, named what would fix it and whose it is, and did not build it - and the plan is corrected on main with the parcel's table in it. Two lessons for the method. A value statement that names a mechanism ("removes compute and bytes") should also name the measurement that would falsify it, so the parcel knows it is a claim and not a fact; and a stop line in a brief should say what to measure before stopping, because the measurement is what made this report decidable in one reading rather than a debate.
| 12:49 | **P2's first findings**, an hour in: a program run requires stream a, so the naive operand-to-stream mapping over-reads a one-element scalar buffer beside an indexed operand - the trap the brief named, met and solved by packing the streams by what the opcode reads and expanding a scalar into a constant with its k bit (measured in the RTL parser, not assumed); the remote route gathers on the client and the handle publishes the bit again (419 checks); two rules decided and written down (a table on an unread operand refused by name; d aliases nothing when a table is present); two environment traps for the next brief (Python text-mode writes flip a file to CRLF; a heredoc eats a backslash and an assert on the match count cannot see it); the two integrator gates red at its tip, named, and left to the lead. Then a self-correction: its first probe had read a lazy `cwrap` as proof an export existed. |

**§3, a brief that names the trap gets the trap solved; a brief that names the wrong file gets a correction in ten minutes.** P2's brief carried a sentence beginning "That is the trap" about a scalar beside an indexed operand, and the parcel's first substantive entry is the measured shape of that trap and the design that avoids it. The same brief named two functions that did not exist, and the parcel's first entry of all, at ten minutes, was that fact with a grep beside it. Both are the brief working: one by being right about what is hard, the other by being falsifiable about what is there. The parcels in this round correct their own entries in the open (P2 on the module's state, P3 on its stamps, V4 on "no defect"), which the ledger's append-only rule makes cheap and the "measured / believed" line makes natural - a correction is just a later measurement.
| 12:56 | **P1 is whole on main** (01729e4): the follow-up merged on its box verdict with the lead's three merge-time edits (V1's two notes and the warning), krnlseq and the fresh-binary host gates green on the merged tree, the box's suite launched on the pushed tip in a fourth checkout. Main now carries P0, P1 both parts, P4, and every wave-1 gate fix; 6 h 25 min after the first dispatch. |
| 13:11 | **P2 reports** (1 h 27 min, 336 tool uses, ~547k tokens): the composed route measured by a one-line control that makes the software backend compose instead of gather, with the whole device-test agreeing (8,754 checks); three new rules refused by name; the remote route rebuilt as a client-side gather with no frame sent on a refusal; the stream-a constraint solved by packing; four things the brief got wrong named with their evidence; one thing it chose not to do (the C export without its JavaScript half) explained rather than done. V2 dispatched within ten minutes with the plan's list plus four items the lead added from the report. |
| 13:16 | **P3 reports** (1 h 31 min, 658 tool uses, ~716k tokens): eighteen files; every gate green on both the RTL and the host side; four controls; the value statement's correction as the headline; six brief errors named with evidence - among them that a program run is not split across tiles today (the repack's slice offset is always zero) and that the brief's own remote sketch would have leaked a masked lane's flag, which compaction fixes. It kept its bench cases in a new test as the lead asked at 12:13, and the merge preview shows every code file auto-merging. V3 dispatched within minutes with five items added from the report. Both wave-2 parcels landed within four minutes of each other, 1 h 31 min after dispatch. |
| 13:34 | **V2 finds a regression in P2** twenty minutes into its list: the new per-index bound loop runs before the elementwise path's own n-sanity check, so an absurd n that the dense call refuses without touching a byte now walks the caller's table - a segfault, reproduced at n = 2^61 with an eight-entry table. One hoisted check. V2 also corrected the report's "+4,720 checks" to 4,676 by rebuilding both tips: the parcel had subtracted the lead's retracted stale-binary number, which is how a wrong number propagates - it was in the ledger for fifteen minutes and got used once. And four sentences in the public header go false at the merge (the lead's file, the lead's job). |
| 13:38 | P2 sent back within three minutes (the hoisted check with its case; the refusal order on a device without the scalar capability, which V2 read rather than ran - there is no card); the header sentences prepared as a two-half patch so main never states a falsehood between the two wave-2 merges. |

**§6, the verifier catches the parcel's use of the lead's wrong number.** The lead retracted a stale-binary count at 11:52; P2, reading the ledger for the base's count, took the 11:37 figure rather than the 12:00 replacement and reported an increment 44 too high. The correction entry was in the file, in order, with a "CORRECTION" headline - and it still lost to the earlier number, because a reader looking for "the count at 5c0c655" finds the first entry that has one. Two things follow for the method: a correction should EDIT nothing but should be linked from the entry it corrects ("see 11:52" appended below the old entry is an append, not an edit), and a number a sibling might reuse should be stated in the entry that supersedes it in the form the sibling would search for. V2 found it because its list said "derive the increment", which is the lead's own rule applied to the lead's own arithmetic.
| 13:41 | **V2's full report** (29 minutes, 137 tool uses, ~305k tokens - a third of a parcel): every item on the list confirmed by its own drivers (six scalar/indexed pairs at every format; a one-byte overlap; flags reachable only through the gather; the wire frame byte-identical; three controls rebuilt from copies, the off-by-one caught cleanly by api-test alone), plus the defect, the wrong number, a gate gap (scalar b and c beside a table are right but unheld), a pre-existing sticky error string, and the card-day gap no host can hold (bus_out on the composed route). The cheapest agent of the round found the round's only host-side regression. |
| 13:50 | **P2's fix** (13:45-13:50; 2 h 07 min for the parcel in all, 407 tool uses): the memory-touching rules moved BEHIND every check the dense path makes rather than beside two of them - so a check added later is inherited - with a poisoned-pointer case that segfaults when the check is neutered; the capability refusal moved to where exactly the runs that use the thing it names reach it, proved both ways; the gate gap closed with a derived pair count. P2 also stated the general rule in the ledger for P3 (a rule that dereferences a caller's buffer belongs behind every rule that does not), and the lead forwarded it to V3 as an item, because the lane mask and P1's tables have the same shape. V2 resumed for the re-check. |
| 13:56 | **Wave 1 verified on the box at its pushed tip**: the full merged main (P0, both parts of P1, P4, every gate fix) - 25 benches, the census, lint, nothing failing. Seven box runs today across four checkouts, every one green; the only launch that failed was the lead's grep mark in the wrong file. Wave 2 merges onto this line. |
| 13:59 | **V2's re-check** (11 minutes): all three fixes hold; the read-before-check property proved with a poisoned pointer in eighteen shapes (a read would have killed the process); the new gate shown live by neutering the check (a segfault is the only faithful witness of "no read happened"); the pair sweep's count derived by hand (28 pairs a format, 10 checks a pair, 800 added, 9,554 total); the dense stages' increments identical. P2 merged within a minute of the entry, the header's seam sentences made true in the same push, the host gates re-run with fresh binaries before it. |
