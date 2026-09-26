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

## Timeline (2026-09-25 into the 26th, local time, UTC-7; commit times and file mtimes where they exist)

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
| 20:56-20:58 | **Resumed at the owner's word** ("Continue work"). Nothing had been written to the ledger in the two hours paused. The lead re-armed its watch first. Then it dispatched four checks together, from the pause entry's list: <br>- verifier-P2 and verifier-P3 re-check their parcels' fixes; <br>- verifier-P1 makes its first pass; <br>- the P0 verifier makes a fourth, over three lead commits no verifier had seen. |
| 21:12 | **The P0 verifier's fourth pass: the lead's import allowlist does not hold.** Five lint-clean modules ran an effect at import and passed the whole front door: <br>- a bare decorator; <br>- a class that fires `__init_subclass__`; <br>- `operator.call`; <br>- `itertools.starmap`; <br>- a name rebound after its last allowed use. <br>Seventeen more shapes passed the parse, `import antigravity` (which opens a web browser) among them. The verifier named four mechanisms no list of spellings closes, and proposed a check on behaviour: PEP 578's audit hook. |
| 21:18 | verifier-P3: P3's fixes hold as found, and its merge onto main is green. Five minor items. |
| 21:23 | verifier-P2: P2's seven fixes hold as found. But three routes pass both P2's rule and its replay, where PINNED.md says they cannot: <br>- libm computed outside a registered function; <br>- long-double arithmetic in the integer layers; <br>- replay marks stripped. <br>P2 resumed. |
| 21:25 | **P3 merged** (`63a831e`, integrated at `bda92eb`, pushed). 12 of 12 stages pass with `--require-all`, and all 1,995 device rolls pass main's fixer. Also `4ff989b`: every module is imported in a child process under an audit hook. The hook refuses a process, a socket, a file write or a library load, however it is spelled. Each of nine planted effects is stopped and named. |
| 21:28-21:31 | **The owner, going to bed: the watch tool needs consent**, so watch with a script. The expiring watch and the new script ran together on one snapshot's temporary files. Each moved the other's copy, and the script reported the ledger "REWRITTEN". The lead checked every file by hand: the ledger was untouched. The script now has per-run temporary files. |
| 21:32 | **verifier-P1's first pass.** P1's arithmetic holds as claimed: 600 + 60 rolls equal, and 68 planted refusals never answered. It is NOT READY on five defects: <br>- six one-ulp faults in the wrong direction pass every gate, because wide boxes hide the slack; <br>- six respellings pass the source rule; <br>- a refusal after a hand-off comes back misnamed; <br>- writable caches; <br>- a non-bytes stream. |
| 22:15, 22:25 | P1's fixes (`3c29f3a`), then P2's (`27c9b4b`: the rule reads every path into a pinned chain, and the chains run under a libm trap). |
| 22:38 | verifier-P1's re-check: the five are fixed as found. But seven new faults pass every gate, and five respellings pass P1's new allowlist. |
| 22:39 | **The lead scoped both parcels' next rounds to converge.** Five rules that read spellings had now fallen, each to a spelling it did not list. The scope: close the structural gaps, and hold what behaviour can hold (tight exact checks inside the steps; audit hooks and libm traps at the edges). State the rest as a limit. The verifiers judge READY by the standard verifier-P1 had offered: "a gate, or a stated limit". |
| 22:54 | **verifier-P2's third pass: the bits and the branch are ready; the document is not.** Two routes passed the rule and the trap, where PINNED.md, which the push publishes, says neither can: <br>- libm through `**` inside a subscript or a validator; <br>- pinned code's exact methods rebound from a module the rule does not read. <br>P2 resumed at the converge scope. |
| 23:05 | P1's third round (`6dcd5a1`): the structural gaps closed, and the spelling limit stated. |
| 23:24 | **verifier-P1's third pass: one defect left, and the shipped code correct.** The end-to-end check read what `decide` traced, not the position it returned. So a two-line fault in `decide` certified the wrong site on a tight input, while passing every gate, 300 of 300 equal rolls and the rule. It was a decision certified without its Gram factor, and traced honestly. |
| 23:25-23:35 | P1 resumed on it at 23:25. The lead wrote its answer to the ledger ten minutes later, after the message. verifier-P1, which watches the ledger, had found no answer there. |
| 23:39 | **P1 closed D10** (`b7cb207`). The check now holds the decision `decide` returns, with targets planted either side of every boundary. The honest-trace fault gives 317 problems there, and so does its respelling past the rule. |
| 23:40 | The lead wrote the ledger first this time, then resumed verifier-P1. It stamped the entry 06:44Z by estimate; the clock said 06:40Z, and a correction was appended. |
| 23:40-23:50 | **While verifier-P1 checked, the lead prepared the merge** in a worktree of its own. It made the merge, its integration commit (D6 and the docs), and the full suite: 13 of 13 stages with `--require-all`, 537 tests in one session. One figure P1 had handed over for the docs was wrong. P1's report put the binary32 "2 of 40" on a 64x64 prototype; the 2026-09-25 VALIDATION entry says 32x32. The docs took the ledger's figure. |
| 23:46 | **P2's round** (`3a79346`): <br>- D13 closed; <br>- the two rebinding plants held at run time; <br>- the count-law cache removed, so it cannot be pre-filled. <br>Six new limits are stated, each with a plant a tracer showed live, and PINNED.md now claims what each gate holds. verifier-P2 was resumed at 23:47. |
| 23:50 | **verifier-P1: READY TO MERGE.** It built a fault to evade the new check, N3m, which returns the unsound decision only where the Gram bound is below 2^-40. It passes every gate, because family G's bound is about 2^-36, and it lies inside the limit P1 had stated. |
| 23:51-23:53 | **P1 merged**: main fast-forwarded to the prepared merge (`a389653`, `04fe2fe`), plus VALIDATION.md's entry (`709055b`), and was pushed. The P0 verifier was resumed for a fifth pass, over the lead's own commits since its fourth. |
| **2026-09-26** | |
| 00:09 | **The P0 verifier's fifth pass: every fourth-pass defect closed as found, and one claim false as stated, the lead's.** VALIDATION.md gave the plain formats' worst errors "in units of u". Beside a format, u reads as its unit roundoff, and read that way binary32 would err below its own rounding. |
| 00:11 | **verifier-P2's fourth pass: the code, the bits and the branch ready, and one route no limit named.** A trace hook installed at import rewrote a chain's value in place and passed every gate. PINNED.md's limits named rebindings, and this was none. |
| 00:12-00:13 | The lead checked the label against P1's measuring script. P1's u was the uniform the target is drawn from, so the figure held as P1 meant it and was false as the docs said it. The same check found a second mislabel in the same table: absolute distances marked "(relative)". Both were corrected by an appended entry and pushed (`283330c`), and the P0 verifier was asked to confirm. P2 was resumed on a docs-only round: state the limit as a class, not by its instances. |
| 00:17 | **The P0 verifier: PASS.** It re-ran P1's script on the new code and reproduced its figures, and the correction held. Over five passes it had found 21, 4, 5, 5 and 1 defects, each closed as found. No verifier pass is owed on main. |
| 00:22 | **P2's docs-only round** (`f3aa361`). The limit is stated as a class, with the trace hook as its plant. P2 corrected every other sentence that implied the class was covered, and fixed the docstrings that still made a refuted claim. It added no gate and changed no code. verifier-P2 was resumed at 00:22. |
| 00:34 | **verifier-P2's fifth pass: the limit stated as found, and one phrase left.** PINNED.md still said two libm routes "cannot run in a pinned chain". P2 had corrected the same claim in the docstring beside it, and missed its twin in the document; the verifier had missed it on the pass before. P2 was resumed to replace the phrase with the docstring's own wording. |
| 00:35-00:38 | P2's one-line fix (`d4007b2`), then verifier-P2's confirming pass. It put log10 and np.interp into pinned code in copies of the tree; the rule refused each by name, and the trap caught each. **READY TO PUSH.** |
| 00:39 | **atlas-film's `pinned` pushed** (`d4007b2`), under the owner's word of 15:35 the day before. It went from the round's clone, never the owner's checkout. `git ls-remote` shows the new branch beside main, unchanged at `be1d674`, and no pull request was opened. **Every parcel of the round is landed and verified.** Left for the owner: METHOD.md's lessons, the ledger's archive, the clean-up, and whether `pinned` merges. |

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

    *(Written at 17:52, and half wrong by 21:12: the allowlists fell too. See 14.)*
11. **Check a new seam against the parcels' branches before they merge.** The lead's allowlist was right about Atlas and wrong about the parcels. Run against their branches before either merged, it would have refused both. METHOD's merge section should add: a seam changed mid-round is checked against every open branch at once, not at each merge.
12. **A usage pause is survivable when the ledger is the state.** Three agents stopped mid-task on a rate limit. Each resumed from its own ledger entries and its tree after a full read, and none repeated or lost work that was recorded. P1 had written its state down before the pause, unasked. METHOD should make that a rule: when a pause is announced, each agent records where it is.
13. **Verification converges slowly on the lead's own gates.** The P0 verifier's three passes found 21, then 4, then 5 defects, a third of them in fixes to the pass before. Every fix was planted and watched to fail first, but on faults the fixer chose. The lesson of observation 7 bears repeating: the verifier picks the faults.

*(Observations 14-22, from the night of the 25th to the 26th.)*

14. **Allowlists over spellings fell too; checks on behaviour held.** Observation 10 was right about lists of forbidden spellings and wrong about lists of allowed ones. Three allowlists fell overnight, each to a spelling it did not list:
    - the lead's list of what may run at import (the P0 verifier, 21:12);
    - P1's source rule (verifier-P1, 21:32 and 22:38);
    - P2's per-layer rule (verifier-P2, 21:23 and 22:54).

    What held checks behaviour instead:
    - an audit hook that sees a process, a socket or a file write however it is spelled;
    - a libm trap around the chains;
    - exact checks on tight inputs inside each step.

    METHOD §5 should say: a gate that reads source text is a stated limit, not a guarantee. Put the guarantee in a check of what the code does, and state what that check cannot see.
15. **A verifier loop over a spelling rule does not end by itself.** P1 and P2 each went three rounds, and each pass found new spellings. The lead ended the loop by scoping a round to converge: close the structural holes, state the limit, and judge READY by "a gate, or a stated limit". The verifiers had offered that standard themselves. METHOD should put the READY standard in the brief, before the first pass, not in the third round.
16. **A check on what the code says it did is not a check on what it did.** P1's end-to-end check held the trace `decide` wrote, and not the position it returned. A fault that traced honestly and returned another answer passed every gate and 300 of 300 rolls. Only a target planted inside the fault's reach showed it, which is observation 8 again: a control bites only where the fault bites.
17. **The lead's decisions go in the ledger first, then in the message.** The lead resumed P1 by message and wrote the ledger ten minutes later, and a verifier that reads only the ledger saw no answer. A watch that needs a human to approve it does not run overnight. With the owner asleep, the lead's watch became a script it relaunches at each exit. Its first run raced the expiring watch on shared temporary files, and reported a rewrite that had not happened. METHOD should say: one watch at a time, on files of its own.
18. **Under the converge standard, a stated limit is a claim a verifier can test.** It builds a fault that passes every gate, and sees whether the fault lands inside the limit or outside it. verifier-P1 built N3m to evade P1's new check. It landed inside: it certifies wrong sites only on inputs the end-to-end check never reaches, which is what P1's limit says. A fault outside a stated limit would have been NOT READY.
19. **The lead can prepare a merge while the verifier works; the verdict still gates main.** The lead's trial merge, in a worktree of its own, ran the whole suite before READY arrived, so READY became a fast-forward. Writing the integration against the ledger's entries, not the parcel's summary, also caught a figure handed over wrongly.
20. **A unit is part of a figure.** Two figures reached VALIDATION.md with the parcel's label but not its definition: "units of u", where u was the uniform and not the unit roundoff, and "(relative)" on absolute distances. Every figure traced to the ledger, so a check that traced figures passed them. METHOD should say: a figure that crosses from a parcel's report into the docs carries its definition with it, or it is re-measured.
21. **A limit stated by its instances is walked past, as a rule stated by its instances is.** P2's limits named what had been found: rebindings below the names, and a rebinding between checks. A trace hook is neither, and it passed every gate. The fix states the class: code the interpreter runs inside a chain that pinned code did not call. Observation 14 applies to limits as it does to gates. State a limit by the behaviour it concedes, not by the plants that found it.
22. **A claim in two places is corrected in one.** P2's last false sentence was one it had already fixed, in a docstring. Its twin in PINNED.md said the same and kept it. HonestFramework's "one fact in one place" applies to claims about a gate's reach as much as to parameters: a limit stated in the document and restated in a docstring drifts. The docstring should point to the document.
