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

## What the method predicted, and what happened

*(Filled in at each milestone.)*
