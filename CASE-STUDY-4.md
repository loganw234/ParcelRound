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
