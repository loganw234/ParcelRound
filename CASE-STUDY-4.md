# A fourth round, recorded as it runs: two repositories, and a verifier on the lead before dispatch

Written during the round it describes, like [CASE-STUDY-2.md](CASE-STUDY-2.md),
so that what the method predicted and what happened can be set beside each
other with timestamps. It is a draft until the round ends; the final section
says what METHOD.md should say differently.

## The setting

- **The project.** Quantum-Film (github.com/loganw234/Quantum-Film, MIT),
  begun the same day for Moth Quantum's hackathon: film stocks whose
  crystal layouts are drawn from quantum laws, and a "fixer" that records
  a roll as integers so that every print of it is the same bits
  everywhere. It is built under HonestFramework.
  - An exact Python authority (mpmath at 256 bits, SHA-256 counter-based
    uniforms) that refuses any draw rounding could decide.
  - Frozen vectors, and a runner whose every gate was watched to fail.
  - An append-only ledger in docs/VALIDATION.md.
- **What is new against rounds 1 to 3.**
  1. **The owner made the P0 verifier a precondition of dispatch**: "ensure
     a verifier agent was dispatched to check your work prior to
     dispatching P1-P3". METHOD §5 already says the lead's code goes
     through the same gates as a parcel's; here the whole P0 goes past an
     independent verifier before any parcel sees it.
  2. **One parcel works in a different repository.** P2 moves atlas-film
     (the film-emulation library the stocks develop through) onto
     cft-fp256's pinned arithmetic. The owner's direction: atlas-film was
     always meant to make that move, and the gaps a survey found in it are
     that step not yet taken. METHOD §3 warns that a harness which
     branches worktrees from the session's repository cannot serve such a
     parcel. The lead therefore gave P2 a fresh clone of atlas-film
     instead, never the owner's checkout, which carries the owner's
     uncommitted work.
- **The round.**
  - **P0**, the lead's: the shelf, the authority, the fixer, the Atlas
    client, the runner.
  - **P1**: a pinned binary64 sampler on libcft that must equal the
    authority by construction.
  - **P2**: atlas-film on the pinned primitive set.
  - **P3**: a hardware-shaped circuit, and device rolls from Moth's
    platform.
  - **Who:** the lead is one Claude session (Opus 5.5), and the parcels
    and verifiers are Opus 5.5 agents.
  - **Where:** the plan is Quantum-Film's docs/ROUND1.md, and the briefs
    are in the round's ledger.

## Timeline (2026-09-25, local time, UTC-7; commit times and file mtimes where they exist)

| when | what |
|---|---|
| 10:01-11:30 | A day of exploration: Moth's API probed (seeds fix circuits, not shots; an undocumented per-setting count order, decoded against known answers), three emulsions simulated, four research agents. It is recorded in Quantum-Film's docs/VALIDATION.md. |
| 11:56-11:58 | Three local commits: the exploration, the skeleton, cft-fp256 as a pinned submodule. |
| ~12:40 | The owner: create and push the repository; dispatch P1-P3 once P0 is finished, **with a verifier on P0 first**; and move atlas-film onto cft-fp256 now. |
| 12:46 | Repository created, public; main pushed, and confirmed with `git ls-remote`, not a local ref. |
| 12:47 | libcft built by the lead in the pinned submodule, because two parcels need it: 8 s, 0 warnings, 122 exports. The `cft` stage passes for the first time. Its first failure message was found to lie ("ABI 0.14, not 0.14") when a sabotaged copy was run, and was fixed. |
| 12:50-13:03 | The rest of P0, for the round's seams: the device-roll record format and its commitment; tests moved to one directory per stage, with a registry test that fails a test file no stage runs; packages discovered rather than listed. **A gap closed:** nothing had tested that the authority samples the law it claims. Now 2,000 rolls give chi^2/dof 0.943, while the uniform control gives 7.052. |
| 13:04 | P0 committed and pushed, `775b5ed`; `make verify` 9 passed, 1 skipped by name. The ledger created outside every repository, with `lead.md` seeded with the environment traps. |
| 13:05-13:06 | **The P0 verifier dispatched** against a fresh clone of the pushed commit, not the lead's tree. P2's atlas-film clone made at `be1d674`; the owner's checkout was untouched, and that was asserted. |
| 13:06 | A trap measured for P2 before dispatch: an editable install of the owner's atlas-film checkout means tests run from anywhere but the clone's root import the owner's code. It went into P2's brief as a rule with an assertion. |
| 13:08-13:10 | The three briefs written to the ledger. All 33 paths they name were checked to exist. |
| 13:15 | The owner confirmed P2's scope while the P0 verifier ran: libcft is the oracle, with no U50 programs; a binary256 evaluation is the yardstick for whether binary64 is precise enough. Written into P2's brief before dispatch, in output units: 16-bit threshold steps and float32 ulps. |
| 13:43 | The P0 verifier posted the round's first `urgent/` message: `givens.py`'s pauli-4x4 circuit had never run on Atlas. **The lead had not armed its own watch.** The message sat unread until the owner noticed the watch missing at 13:48. The lead armed it and read the whole ledger. |
| 13:49 | The P0 verifier's report. The authority held: its basis, its law over 50,000 rolls, its normalisation, its uniforms, the decode rule and the gauge. The rest did not: a run credited to the wrong law (8a); two golden gates that could not fail; five runner flaws, among them a PASSED over a failing authority; four holes in the fixer; six claims with nothing behind them. |
| 13:51 | An untracked clone was found inside the lead's tree, `qf-verify-p0/`, made at 13:34, pristine. The verifier's report did not list it. It was removed. |
| 13:53 | **P2 dispatched ahead of the fixes.** None of the findings touched its inputs: another repository, and only the lead's libcft build read. Its brief gained two measured lines first. |
| 13:55-15:25 | The lead fixed P0. Every finding became a planted fault in a scratch copy, and each was refused. The new gates found three more defects on their first runs: <br>- the runner's `git -C` fails under `MSYS_NO_PATHCONV=1`, so no tree was ever dirty and the new `--resume` guard could not fire; <br>- the Atlas client checked the host but not the scheme; <br>- an eighth script that called Atlas on import was the lead's own smoke tool. |
| 14:18 | **The lead's watch expired at the tool's 30-minute limit**, unnoticed. P2's first entry (14:52) landed while it was down, and was read at 15:25, when the watch was re-armed with its snapshot kept and reported the entry on its first pass. |
| 15:26 | `b0e9ed1` pushed; `git ls-remote` agrees. `run.sh --require-all`: 12 passed, 0 skipped, the live Atlas smoke included. |
| 15:27 | **P1 and P3 dispatched from `b0e9ed1`.** P3's brief now says its run is the first of the shelf's law on Atlas, and that the old scorer scores the wrong law. P1's brief carries the no-skip rule, the thread hazard, and P2's two findings about its replay. |
| 15:27 | **P2 reported.** atlas-film has a pinned mode, `78f35d3`, not pushed. 51 chains are bit-identical under libcft replay, and binary256 moves no output quantum. P2 also found its own brief's control 2 unable to fail for most one-ulp changes, and said so. |
| 15:29 | The P0 verifier was resumed to check the fixes, and verifier-P2 was dispatched. |
| 15:35 | The owner cleared the push of atlas-film's `pinned` branch "when ready". The lead reads "ready" as after verifier-P2. |
| 15:50 | P3's first entry: 51 rotations, not the brief's 55. And **a completed Atlas job's status response carries its whole result**. So a commitment must be committed before the first status call, and the lead's own `run_job` cannot run a device roll. P3's tool already committed first. |
| 15:59 | **The P0 verifier's re-check.** All 21 of its findings were fixed as found. Four new defects, **three of them in the gates written to answer it**. The premise gate compared the authority with itself at 512 bits, so a binary64 slip that moved every boundary 2^-51.5 passed it. The verifier also explained its stray clone: WSL's shell had expanded `$D` to nothing. |
| 16:03 | **The shelf's law ran on Atlas for the first time** (job 8586f1cc): sites 1.48 sigma, pairs 2.52 sigma, 0 forbidden layouts. Its commitment was in git before any status call. |
| 16:06 | P3 reported: 51 rotations and 102 CNOTs, 1,995 device rolls all checked, 1 Atlas job of 6. verifier-P3 was dispatched at 16:08. |
| 16:13 | A file notice showed that P1 had overwritten one of the lead's scratch files. **The harness gives every subagent the lead's session scratchpad**, which holds the Atlas key. The lead posted to `urgent/`: work only under a subdirectory named for you. |
| 16:17 | `5fe9741` pushed. The premise is now measured against code the authority does not share: exact Fractions (pauli-4x4's kernel is rational) and an independent chain rule. A source rule bans binary64 from the authority, and catches the two slips that are inert on today's shelf. |
| 16:17 | **P1: the control the lead's brief specified could not fail.** A target 1e-14 from a boundary is decided identically by plain binary64. P1 planted inside binary64's own error instead (3e-17 to 4e-16) and watched the control fail there. |
| 16:19 | The P0 verifier resumed for a third, focused pass over `5fe9741`. |
| ~16:25 | The owner: a usage limit would pause everything for about 30 minutes, so let the agents run until they stop, then resume them. The lead wrote a resume rule into the ledger: full read, check your tree, re-arm your watch, say where you stopped. P1 recorded its state before the pause (16:29). |
| 16:30 | verifier-P2 reported: P2's pinned chains are the same bits everywhere it ran them. But the replay cannot see libm on a scalar, the source rule is a list of forbidden names, NaN dials leak, supplied sheets are under-checked, and unpinned readers accept `pinned=True`. The owner's push waits on the fixes. |
| 16:30-17:08 | The limit hit (its notices arrived with the owner's next message, so its exact time is not recorded): P1, verifier-P3 and the P0 verifier stopped mid-task with HTTP 429. P2 and verifier-P2 had finished. |
| 17:08 | The owner: carry on. The watch was re-armed and the ledger read; nothing had landed during the pause. All four agents were resumed, P2 to fix its defects. |
| 17:25 | **The P0 verifier's third pass**: five new defects. One is a regression the lead had introduced: the runner compared two spellings of a path, and refused every clone under %TEMP%, where the verifiers work. The source rule and the guards gate were walked past again, by respellings. A refusal checked on one side of a boundary passed every gate. |
| 17:30-17:34 | verifier-P3 hit the same regression independently (17:30). It was fixed and pushed on its own at 17:34 (`900b9e5`) so the verifiers could proceed. |
| 17:39 | verifier-P3 reported: P3's circuit lays the shelf's law exactly, and the scores reproduce. But `--score` cannot fail, and the commitment's timing rests on the local clock and the code. And `kind`, `fixed_at` and `occurrences` are bound by nothing: an emulator roll re-sealed as a QPU roll passed. P3 was resumed to fix its part. |
| ~17:45 | The owner, while the batch was being planted: once these agents finish, start no more, pause, and document where things stand. |
| 17:49-17:52 | `1a92c62` then `73a79af` pushed. The guards gate became an allowlist. The premise got an exact reference on L = 6, a tile whose arithmetic is not accidentally exact (Niven). The refusal is now planted on both sides of a boundary. The basis checks its content before caching. The fixer says what the commitment binds: its anchor, not its recomputable value. **Checked against both parcel branches before either merged, the first allowlist would have refused their pure constructors**, so it was widened to pure modules before they arrived. |
| 17:55 | **P2's fixes** (`e5f63f8`, not pushed). Every number now enters pinned mode through a named gate. The replay treats every value past a gate as opaque, and refuses a bare number. The source rule became an allowlist per layer, and each of verifier-P2's faults, planted again, fails. One limit, in PINNED.md: `np.asarray` strips the replay's mark. |
| 18:43 | **P1's report** (`857065b`). The pinned binary64 sampler lays the authority's roll on 2,300 pauli-4x4 and 740 pauli rolls, with 0 random hand-offs. The control fails as it must. On the 16x16 stock it is faster than the authority, at 0.62x. And a finding against its own brief: **equality with the authority passed 10 of 11 planted certificate faults**, so each step is now held to exact arithmetic. |
| 18:54 | **P3's fixes** (`961b385`). `--score` fails when a check does, the coherence sign is pinned, and `kind` and `fixed_at` are held. The 0/0 convention and the platform that wrote the QASM are recorded. |
| 18:56 | **Paused at the owner's word**, with every parcel finished. main is `73a79af`; P1's and P3's branches merge onto it cleanly. Owed on resume: re-checks of P2's and P3's fixes, a first verifier for P1, a fourth pass on the lead's last three commits, then the merges and atlas-film's push. The ledger's lead.md 01:56Z entry lists everything, including what the lead missed. |

## What the method predicted, and what happened

*(Filled in at each milestone. The first observations, at 15:30.)*

1. **The verifier before dispatch paid for itself.**
   - 8a would have sent P3 to reuse a scorer written for another law, and to improve on a baseline that never existed.
   - 7e would have let P1's libcft tests skip unseen on any machine without the DLL.
   - METHOD §5 has the lead's code go through the same gates as a parcel's. This round shows why the gates themselves need a verifier: two of the lead's gates could not fail, and its runner could report PASSED over a failure.
2. **The lead forgot its own watch.** METHOD has every parcel arm its watcher before anything else. The lead dispatched a verifier without arming its own, so the round's first urgent message sat unread for five minutes. The owner caught it, not the method. METHOD should say: the lead arms its watch in the same message as its first dispatch.
3. **A watch has a lifetime.** This harness caps a watch at 30 minutes, and the lead's expired silently while it worked. Because the re-armed watch kept its snapshot, the gap cost latency and not information. METHOD should say: re-arm on expiry, and keep the snapshot across re-arms, so that a gap reports what it missed.
4. **A verifier crossed a boundary and did not report it.** Its clone inside the lead's tree was found only by the lead's `git status`. The verifier's "what I did not do" list is a claim like any other.
5. **A parcel that shares no seam need not wait for the lead's fixes.** P2 was dispatched while P0 was being fixed, and finished before P1 and P3 started. The verifier-before-dispatch gate applies per parcel, to the seams that parcel reads.
6. **The first run of a new gate is a finding.** Three of the gates written to answer the verifier found defects the verifier had not listed.
7. **A gate written to answer a verifier needs that verifier again.** Every new gate had been watched to fail, but on faults its author chose. The author of the premise gate planted only faults that scale with precision, and the gate was blind to the one kind that does not. METHOD §5's "a gate you haven't watched fail" is necessary but not sufficient when the author picks the faults. METHOD should say: the lead's fixes to verifier findings go back to the verifier, which picks its own faults.
8. **A control the lead names in a brief is a claim like any other.** The lead wrote "about 1e-14" without measuring binary64's error at a boundary; P1 measured it and found the control could not fail. METHOD should say: name a control by the property that makes it bite ("inside binary64's own error at that boundary"), or run it before the brief goes out.
9. **The scratchpad is shared.** Every agent got the lead's session scratchpad, including the directory holding the Atlas key. P3 had kept to a subdirectory of its own; P1 wrote at the root and overwrote a lead file. METHOD's brief template should name each agent's scratch directory, and the lead should keep secrets outside any directory the agents are given.
10. **A gate that names what to refuse is walked past; a gate that names what to allow is not.** Every gate the lead built as a list of forbidden spellings fell to a spelling it did not list:
    - the guards gate, twice;
    - golden's no-binary64 rule;
    - P2's source rule, found by verifier-P2 on another repository the same afternoon.

    The versions that held name what is allowed: pure modules at import; an exact reference on a tile whose arithmetic is not accidentally exact. METHOD §5 should say this outright.
11. **Check a new seam against the parcels' branches before they merge.** The lead's allowlist was right about Atlas and wrong about the parcels. Run against their branches before either merged, it would have refused both. METHOD's merge section should add: a seam changed mid-round is checked against every open branch at once, not at each merge.
12. **A usage pause is survivable when the ledger is the state.** Three agents stopped mid-task on a rate limit. Each resumed from its own ledger entries and its tree after a full read, and none repeated or lost work that was recorded. P1 had written its state down before the pause, unasked. METHOD should make that a rule: when a pause is announced, each agent records where it is.
13. **Verification converges slowly on the lead's own gates.** The P0 verifier's three passes found 21, then 4, then 5 defects, a third of them in fixes to the pass before. Every fix was planted and watched to fail first, but on faults the fixer chose. The lesson of observation 7 bears repeating: the verifier picks the faults.
