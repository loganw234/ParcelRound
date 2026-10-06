# A seventh round, and the run around it: one lead, eight rounds, eleven days

Written during the run it describes, which has not ended. It covers one lead
session on one project, cft-fp256: a discussion on 2026-09-24, then eight
rounds of work from 2026-09-25 to 2026-10-05, each rolling into the next. The
owner, verbatim: "The prior 'round' rolled over immediately, effectively being
a continuation". Its largest round, step 6, is recorded closely, including the
two days it paused and the day it resumed with its verifiers on a smaller
model.

The sources:
- the rounds' ledgers in cft-fp256's `Data/runs/` (the lead's and every
  agent's, append-only, outside every worktree);
- git, and the project's `docs/VALIDATION.md`, whose entries are the record of
  each push;
- the lead session's transcript: the owner's prompts, and a task notification
  for every agent run;
- each agent's own transcript, beside it, for what the agents used.

The lead wrote the draft from those records, after case study 5's lesson
(twelve of that draft's claims were wrong or unsourced). A verifier then
checked it against them. It found the draft's cost method wrong, and its
account of the session's first day, among other things. The lead checked each
finding against the records again before revising. What was found, and what
changed, is in the last section.

## Where this sits among the other studies

| | file | project | when | what it is about |
|---|---|---|---|---|
| 1 | [CASE-STUDY.md](CASE-STUDY.md) | a C numerical integrator at 64-, 128- and 256-bit precision, bit for bit at 64 | before the method was extracted | the defect that lived in the seam between two parcels; "Tell me what the brief got wrong" |
| 2 | [CASE-STUDY-2.md](CASE-STUDY-2.md) | cft-fp256 | 2026-09-15 to 16 | a round recorded as it ran |
| 3 | [CASE-STUDY-3.md](CASE-STUDY-3.md) | cft-fp256 | 2026-09-24 to 25 | a documentation sweep run by workflow scripts, reconstructed; its correction loop stopped at 69, 29, 6 |
| 4 | [CASE-STUDY-4.md](CASE-STUDY-4.md) | Quantum-Film (and a second repository) | 2026-09-25 to 26 | a verifier on the lead before dispatch; a second round the lead ran alone |
| 5 | [CASE-STUDY-5.md](CASE-STUDY-5.md) | loganw.dev | 2026-09-29 to 30 | a verifier added mid-round on the lead's own commits, because the lead had broken the round's own rule |
| 6 | [CASE-STUDY-6.md](CASE-STUDY-6.md) | ParcelRound itself | 2026-10-02 to 03 | the method run on itself: METHOD.md brought to the method as practised, ADOPTION.md, the templates compiled, an integration verifier on the lead |
| 7 | this file | cft-fp256 | 2026-09-24 to 10-05, running | sustained use: eight rounds in sequence, and step 6 |

Three things tie this one to the others:
- **The same days.** This session began at 12:33 on 2026-09-24 with a
  discussion of a service built on the project, verbatim "No work is needed
  yet". Its first instruction to work came on 09-25 at 08:27. On 09-24, three
  sessions shared the project's checkout:
  - case study 3's lead, from 08:32;
  - the U50 clock sweep's session, case study 3's "second live session", which
    pushed 3b15d52 at 12:52;
  - this one.

  Case study 3 counted two of them. This session led every round below, from
  2026-09-25.
- **Other rounds ran beside it, from other sessions on the same desktop:**
  round 4 beside this run's first days, round 5 beside its revision-7 and
  audit rounds, and round 6 beside step 6's first waves.
- **METHOD.md** is cited here as main holds it at f42242e, after round 6
  brought it to the method as practised. Its eight sections kept their
  numbers and titles.

## The setting

- **The project.** cft-fp256, as case studies 2 and 3 describe it:
  - a deterministic floating-point tile for an Alveo U50;
  - a Python golden model, which is the authority;
  - a C library with software, XRT and remote backends;
  - bit identity everywhere, with anything the hardware cannot do refused by
    name.

  Since case study 3 it has gained:
  - segments and certificates;
  - a seventh revision of the tile's RTL, built and proven on the card;
  - the first half of an eighth: its seam, R21's lanes and the instruction
    fetch are on main, its sequencer items are on a branch, and no image is
    built yet;
  - an auditor in C;
  - a language for dynamical systems, with its compiler;
  - step 6 of the owner's work order.
- **The machines.** The lead and every agent run on the owner's Windows
  desktop, which the owner uses at the same time. A Linux box holds the FPGA
  card and the vendor tools. **No agent touches the box or the card.** Every
  gate budget, bitstream probe and card leg there is the lead's.
- **The rules in force, and where each is written:**
  - **Only a regression or a wrong answer sends a parcel back.** Everything
    else merges as a recorded known limit.
    - The lead proposed it on 09-27 at 19:39, and the owner agreed at 19:42,
      verbatim: "Agreed with the only regression or wrong answer being send
      backs".
    - Of the 112 briefs written from then to the writing, 94 state it. The 18
      that do not are fifteen parcels' briefs, from the certificate, audit,
      revision-7 and step-6 rounds, one verifier's and two surveys'. A brief
      that only reports an earlier verifier's "no wrong answer" is not counted
      as stating it.
    - METHOD.md section 6 has carried the rule since round 6.
  - **Agents test quickly, and hand the long runs back to the lead** (the
    owner's, 09-29). Of step 6's 44 briefs at the writing, 17 carry it in
    his full sentence, and most of the rest in other words: 36 in all by the
    third verifier's count, 28 counting explicit hand-over wording alone.
    All 44 carry the desktop rule in some wording: one run at a time, niced.
    METHOD.md section 7 has carried the hand-back rule since round 6.
  - **The lead may merge and push when ready** (the owner's, 09-28, verbatim
    "You are permitted to merge, push, etc when ready"). It is a rule for the
    lead, and no brief carries it.
  - **No agent loads the desktop on purpose** (the owner's, 09-25).
- **What is new against rounds 1 to 6:**
  - **Length.** Eight rounds in sequence, each one's push recorded as a
    VALIDATION entry. The next was dispatched within hours, sometimes before
    the last one's push.
  - **A verifier on the lead's commits before a push.** Round 5 added one
    mid-round, and round 6 ran one on its lead's integration and wrote the
    rule into METHOD.md (sections 5 and 7). Here every round had one: an
    integration verifier on the lead's merges and records.
  - **Design stops for the owner inside rounds.** Step 6's plan of record,
    certificate version 2's twelve questions and revision 8's RTL plan, with
    ten questions, each went to the owner before code.
  - **Verifiers on a smaller model while the parcels stay on the larger,**
    from 2026-10-05, at the owner's word (observation 9). Round 5 ran its
    parcels and their verifiers on the smaller model, and round 6 its parcels
    with its verifiers on the larger. This run reverses round 6's
    arrangement.
  - **Probes before builds.** Out-of-context bitstream probes on the box,
    measured before any multi-hour image.

## The run, measured

By round, from each round's directory, at the writing:

| round | dates | ledgers (verifiers') | ledger lines | briefs |
|---|---|---|---|---|
| ODE (work order steps 0 and 1) | 09-25 to 09-28 | 17 (12) | 6,556 | 7 |
| certificates (step 2) | 09-28 to 09-29 | 13 (8) | 3,298 | 14 |
| revision 7 | 09-29 to 09-30 | 13 (6) | 5,297 | 11 |
| the auditor in C (steps 4 and 7) | 09-29 to 09-30 | 9 (4) | 2,692 | 7 |
| fixes | 09-30 | 7 (4) | 1,392 | 6 |
| steps 5 and 6 | 09-30 | 13 (8) | 4,073 | 15 |
| the language (step 3) | 10-01 to 10-02 | 14 (8) | 4,867 | 14 |
| step 6 | 10-02 to now | 44 (26) | 14,273 | 44 |
| **all** | | **130 (76)** | **42,448** | **118** |

- A ledger here is a `.md` file in the round's ledger directory. Each holds
  one lead ledger beside its agents'.
- The first three rounds also hold an `urgent/` directory, with 5, 7 and 12
  notes (observation 4).

By day (local time, UTC-7):

| | 09-25 | 26 | 27 | 28 | 29 | 30 | 10-01 | 02 | 03 | 04 | 05 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| commits on main | 38 | 1 | 2 | 48 | 83 | 75 | 54 | 81 | 25 | 0 | 12 |
| agent runs that ended | 25 | 2 | 4 | 26 | 34 | 43 | 36 | 61 | 21 | 0 | 7 |

- **In all, 419 commits and 259 agent runs.**
  - A run is one stretch of one agent's work, from its launch or a resumption
    to its end.
  - The transcript's task notifications report most runs, some of them twice.
    The same task id can report again for the same run, with figures
    cumulative from its start: 22 of the 277 notifications that carry usage
    are such repeats. Some of the earlier ones say so ("the result below may
    be interim").
  - Four runs end in a notification with no usage at all: each was cut off
    by a usage limit. Their figures are read from the agents' own
    transcripts.
- **The quiet days are two breaks at the owner's word.** They ran from 09-26
  at 05:40 to 09-27 at 19:26, and from 10-03 at 05:20 to 10-05 at 01:29: about
  38 and 44 hours. Each began when the agents had wrapped up, and ended at the
  owner's next prompt.
- **There were five shorter stops too, two of them usage limits:**
  - a usage limit on 09-25, from 16:33 to 17:01, which stopped the agents
    and the lead (the owner's warning came at 16:27);
  - a pause to recap, the same evening, from the owner's word at 17:46 to
    20:56;
  - a weekly usage limit, from 09-27 at 20:55 to the owner's "Continue" at
    09-28 02:46;
  - on 09-30, a pause at the owner's word that the agents did not outlive,
    14:18 to 16:51 (observation 4);
  - the same night, a hold at the owner's word before step 3, from the
    push at 23:05 to "Yes, begin on the next step" at 10-01 04:32.
- **The send-back rule came at the end of the first break.**
  1. The owner asked for the lead's recommendations at 19:26.
  2. The lead proposed the rule at 19:39.
  3. The owner agreed at 19:42.
  4. The lead recorded it at 19:43.
- **The VALIDATION entries,** from 09-25's steps 0 and 1a to 10-05's third
  wave, number 14.

## Step 6's round: a timeline

Local time, from the headings of the lead's ledger.

- **10-02**
  - 07:36: the acceptance parcel (A1) and a three-part survey launched.
  - 08:06: the owner's three decisions for the step.
  - 09:15: the plan of record approved, "Approve as written (Recommended)", after a verifier's three checks of it.
  - 10:24: A1 merged, and the first wave of five launched.
  - 12:40: **pushed** (A1 and the plan). 15:54: **pushed** (four of the first wave). 18:11: **pushed** (revision 8, golden-first).
  - 13:16: certificate version 2's twelve questions decided, verbatim: "Regarding the 12 questions, the recommended solutions are appropriate as stated".
  - 22:27: **revision 8's RTL plan approved,** question 9 "Only if probe L finds it cheap (Recommended)", the other nine "Approve as written (Recommended)".
  - 22:48: five parcels launched from the merged tree: two for certificate version 2's C half, three for the RTL's first round.
  - 23:41 to 23:48: **an integration regression, met twice within minutes.** Gate4's programs stage on the box failed on it at 23:41. One of the new parcels (CV2CW) met it in its own run on the tree it was given, and reported it at 23:44. A corpus written at compiler version 2 had met a merge that moved the compiler to version 4. The lead recorded both at 23:48.
- **10-03**
  - 01:00: **gate4's verdict: red,** on that stage alone.
  - 01:34: **probe L measured** R21's lanes at +10,595 LUTs a tile, so by question 9's answer the quad is built without them.
  - 03:52: gate5 passed; wave 2's entry committed.
  - 05:19: wave 2's integration verifier (VI4) found one text error in three places. **The push was held, and the round paused at the owner's word:** "Once they wrap up go ahead and take a pause where we are until I resume".
- **10-05**
  - 01:30: **resumed,** and the verifiers moved to a smaller model.
  - 02:12: **wave 2 pushed** after a narrow re-check.
  - 02:26: the RTL's second round dispatched (C, the sequencer; E, the host side), with the box running the gate and the long RTL simulations.
  - 04:36: **gate6 red** (a test that fails only on Linux, below). 07:23: gate7 passed.
  - 08:19: **probe S1 measured** a timing path the plan had not expected, before any image was built.
  - 07:23 to 10:07: wave 3's integration verifier, then two narrow re-checks. **Wave 3 pushed** at 10:07.
  - 10:24: C finished the sixth and last item of the RTL's second round.

## What the method predicted, and what happened

**1. Each layer caught a class the others could not.** METHOD.md section 5
(gates) and section 6 (verifiers) predict layered defences. Each layer here
stopped something nothing else would have:

| layer | what it stopped, step 6 |
|---|---|
| a parcel's own gate | C's directed cases caught a stale-context bug in R22 that its fuzz passed (10-05, item 6). CV2CW's own run met the integration regression in the tree it was dispatched on, and reported it three minutes after the box gate's stage failed (10-02) |
| a parcel's verifier | coverage gaps a parcel's tests could not see. VE (10-05) ran an XRT mock where no card or image existed. It found that a wrong staging offset passes device-test, because every caller pattern there is uniform. VC12 (10-05) found four behaviours of the abort and the fetch held only by its own cases |
| the lead's box gate | gate4 (10-02, 23:41): its programs stage failed on the integration regression, a corpus written at compiler version 2 against a merge that moved the compiler to version 4. Each parcel had been consistent alone. gate6 (10-05): a new check wrote a private key under the umask, which the signing tool refuses on Linux. Windows has no such check, so every desktop run had passed |
| the integration verifier | VI5 (10-05): a merge resolution that lost a parcel's sentence, and a sentence true on a branch that the merge made false |
| a probe | probe S1 (10-05): the new fetch unit's take path, at +0.452 ns out of context, likely negative inside the quad. It was fixed, and probe S3 measured it at +5.458 ns |

Each was missed by every layer before the one that caught it. The integration
regression is case study 1's seam again: work that belonged to no parcel. Two
layers met it within minutes of each other: the box gate, and a parcel
dispatched on the merged tree. Gate6's is a seam between two hosts.

**2. The lead's own work was the commonest source of wrong answers at
integration, and the verifiers on it were what caught them.**
- On 10-05, six findings stopped a push. Four were in the lead's own work:
  - a merge resolution that kept one parcel's README row whole and lost the
    other's clause;
  - a decision's restatement that counted four variables where the code has
    five;
  - in the fix of those, a wrong VERSION constant, and a list member the lead
    overlooked.

  The other two came from parcels' work: a sentence a merge made false, and
  gate6's key written under the umask.
- The same day's ledger records the lead's operational slips:
  - a desktop build without its make flags;
  - a box script handed a short SHA;
  - a cross-environment script whose failed clone left its build in the main
    checkout;
  - a box script that never sourced the vendor tools;
  - a box script with an unbound variable;
  - a task chip created by mistake;
  - two slips in briefs: a make line without the `.exe` it needs on Windows
    (VE's note), and a refusal's name misstated in VI5's brief.

  Guards stopped three of these before anything was built: an assertion, an
  unset variable under `set -u`, and a missing command. The one in the main
  checkout wrote 19 untracked build files, which were removed. It had also
  checked out one tracked file and restored it, so its end state changed
  nothing tracked.
- **An earlier slip was the same kind.** On 09-26, "27 ahead of origin/main"
  was typed, not measured; it was 29.
- Case study 5 found the same thing in one round, and added the verifier
  mid-round. Eleven days on, this run's record is the stronger form of that
  finding: **the lead is the agent with the least pre-checked work, and its
  verifier is not optional.**

**3. A correction loop on text converged in three passes: 3, 2, 0.**
- Wave 3's integration verifier found three wrong answers.
- A narrow re-check of their fixes found two new ones in the fixes' own
  wording.
- A third pass found none.
- That took from 07:23 to 10:07, for text alone: 62, 42 and 43 minutes of
  verifier time, and the lead's fixes between.
- **The other studies' loops:**
  - case study 3's loop stopped at 69, 29, 6;
  - case study 6 found a verifier loop that "did not end by itself" (its
    observation 1). It ended when the owner had the gate state a threat
    model (its observation 2).
- **What converged it here** was scoping each re-check to the previous
  commit's diff. Both of the second pass's findings were restatements by the
  lead that the code contradicted: the guard's constant, and an instrument
  the lead overlooked (proposal 3).

**4. Interruptions cost nothing that was written down.**
- **What the run survived:**
  - two breaks and five shorter stops;
  - fourteen continuations of the lead's own context by the writing, each
    from a summary;
  - API failures that stopped agents mid-task: one parcel three times on
    10-05 (two dropped connections and an overload), and others on 09-29,
    09-30, 10-02 and 10-03.
- **An agent that dropped was resumed by message,** with its context and its
  uncommitted work intact (8 files, +661/-60 lines, in the parcel that
  dropped three times). After its third drop, it was asked to leave a resume
  note at each step.
- **One pause outlived the agents.** On 09-30, at the owner's word, every
  agent committed its work and wrote a resume note within nine minutes. The
  agents did not survive the pause. Each was dispatched again from its brief
  and its own ledger's resume note (VALIDATION.md, the steps 5 and 6 round).
- **On 09-29 the box briefly lost power.** A storm's risk of more cuts then
  had every agent log its work often until the owner said it had passed.
- **The lead resumed each time from the summary of its context.** After most
  continuations it also read its ledger and a memory file holding the run's
  state and resume list. Of the 15 to date (the fifteenth came after the
  writing), it read the ledger after 14 and the memory file after 7, by the
  second verifier's count.
- METHOD.md section 4 makes the ledger the channel of record for correcting a
  brief after dispatch: a message may carry a correction too, once its entry
  is written. Over a run this long, the ledger is also what a lost agent
  restarts from: the 09-30 agents were dispatched again from theirs.
- **The out-of-turn channel moved from files to messages.** The first three
  rounds kept an `urgent/` directory inside their ledger directories, with 5, 7 and 12
  notes between the lead and the agents. From the audit round on there is
  none: the lead and the agents messaged each other directly, in both
  directions, as METHOD.md section 4 has noted since round 6.

**5. The shared indices collided at almost every merge.**
- The project's document index states every document's line count and three
  totals, and a docs gate holds them true. So every one of the six merges the
  lead made on 10-05 conflicted there. Each took two or three runs of the
  gate to recount (the verifier counted 3, 3, 2, 3, 3 and 2 in the
  transcript).
- The project's verification map keeps one table row a stage, one line each, so
  two parcels touching one stage's row conflict on the whole line. The lead
  resolved such rows two ways: once by taking each row from the side that
  changed it, and once word by word, with `git merge-file` over a word split.
- Twice, taking one side of a conflicted index whole would drop a parcel's
  edits. Once it was caught. The other time (observation 2) it did drop them.
- METHOD.md section 2's rule fits: a thing three parcels touch is the lead's
  P0. The index is such a thing, and here it was nobody's (proposal 1).

**6. Decisions arrived mid-parcel, and were settled by message in minutes.**
- Three choices came back from parcels on 10-05:
  - whether new compiler targets join the built-in set now, which would move
    every committed manifest and step the compiler's output version, or
    later;
  - whether the quad's tile, without R21, gets a gated bench target;
  - whether the small open-core builds gain R21 by a new default.
- The lead answered each within minutes, and the owner confirmed the last,
  verbatim: "Agreed on keeping R21 off for open-core, parallel work is already
  being undertaken to get the dense design to close timing on NextPnr, once
  progress is seen there it will be reconsidered along with other space saving
  measures".
- The ledger keeps every such answer, and the owner's words verbatim. The
  parcel quotes them in its commit and its documents.

**7. The environment's traps recurred, though written down.**
- **Three recurred on 10-05, and a fourth earlier in the run:**
  - a Windows make that needs its compiler, OS and temp directory on the
    command line;
  - WSL commands that re-parse their argument;
  - an unquoted heredoc that runs backticks;
  - earlier, on 10-02 and before: Git for Windows' shell halving doubled
    backslashes.
- **Where they are written:**
  - the lead's memory names two of them: the make's temp-directory flags (but
    not the compiler or OS flags the make also needs), and WSL's re-parse;
  - the briefs' ground rules name the heredoc and the backslashes;
  - the project's CLAUDE.md names none of the four, though it names a
    neighbour: the two MSYS runtimes' `/tmp`.
- The make flags and the heredoc each cost the lead a retry on 10-05, and
  parcel E met WSL's re-parse the same day.
- **Two were new:**
  - a git worktree's `.git` file holds a Windows path that Linux git cannot
    follow;
  - a running box script cannot be edited safely, so a slip found in one
    waits for a second script.
- What worked was not the note but the guard: box scripts that assert the
  commit, the tree hash and the content before they build, and refuse
  otherwise (proposal 5).

**8. Measuring before the expensive build changed the plan twice.**
- **Probe L** (10-03, about half an hour) priced R21's lanes at +10,595 LUTs a
  tile. That settled the quad's contents by a rule the owner had set in
  advance.
- **Probe S** (10-05) took four runs of 34 to 44 minutes each:
  - S1 found the take path;
  - S2 measured the cascade remedy the plan asked for;
  - S3 measured the parcel's fix. Against the same run's control, streaming
    costs +114 LUTs a tile net and frees 48.5 block-RAM tiles a tile; the plan
    had estimated about 1,000 LUTs;
  - S4b, without the remedy, showed it worth keeping: the store cascades
    again, and every fetch path loses 0.24 to 0.68 ns, at the same block RAM.
- **The cost against the alternative:** probes L and S took about three hours
  of box time together, where one image takes 2.6 to 7.5 hours.
- **What METHOD.md says:** section 8 (sequencing) does not yet say that probes
  go before images. Section 7's habit of one instrument per hypothesis,
  cheapest first, is the principle.

**9. Verifiers on a smaller model, as the owner's trial.**
- The owner, 2026-10-05, verbatim: "switch to Sonnet models for verifiers,
  testing if they perform well in that role, as most "information" is passed
  to them correctly or at least complete enough to manage, the task of trying
  to verify it is simpler and not as demanding as writing the initial."
- **Six such verifiers had finished at the writing:**

| verifier | on | minutes | tool uses | what it found |
|---|---|---|---|---|
| VI4b | the lead's fix of a wave's text | 32 | 138 | none that sends back; two stale sentences the earlier, larger-model verifier had missed |
| VE | a parcel (the host side) | 100 | 296 | none that sends back; wrote an XRT mock to run code no test could; a coverage gap |
| VC12 | a parcel (the sequencer's abort and fetch) | 180 | 300 | none that sends back; four coverage gaps; a probe recipe smoke-tested |
| VI5 | wave 3's integration and its entry | 62 | 308 | three wrong answers |
| VI5b | the lead's fix of those | 42 | 158 | two wrong answers |
| VI5c | the lead's fix of those | 43 | 160 | none that sends back |

- **No false finding.** Five of the six found something an earlier check had
  missed. The sixth, the loop's third pass, found nothing that sends back,
  which is what that pass was for.
- **They kept to their briefs.** Each kept the ground rules. One departed from
  its brief once and said so: a small synthesis run the brief had said was
  impossible.
- **Per first run, they did more, not less: more tool uses and cache reads,
  in about the same time.** Medians over each verifier's first run, 6 against
  71:

  | | smaller model | larger model |
  |---|---|---|
  | tool uses | 228 | 165 |
  | cache reads | 81 M | 51 M |
  | fresh tokens | 805 k | 751 k |
  | minutes | 53 | 55 |

  Tool uses and minutes are the notifications' own figures, which match the
  agents' transcripts; tokens and cache reads are summed from the
  transcripts. First runs compare like with like, since later runs are
  mostly short re-checks.
  - Six runs are few, and they fall in two groups: three re-checks of 138 to
    160 tool uses, and three first verifications of 296 to 308. The median
    sits between them.
  - Any saving is the smaller model's price per token, not a lighter task.
- **Two more have finished since the writing:**
  - VC34, on the sequencer's flag-control items: 215 minutes. It found one
    narrow wrong answer (a test leg that could not fail) and four coverage
    gaps, with its own cases to close them.
  - VCS7, this file's verifier: 96 minutes (see the last section).
- **Still open:**
  - VC34's narrow wrong answer is the first such finding in a parcel's own
    work. Every earlier one was in an integration of the lead's.
  - VCS7's own report held a low count: briefs lacking the send-back rule,
    11 where it is 19. It is the first error the lead has found in a
    smaller-model verifier's report (the last section).

**10. The lead's ledger grew to the size of a book, and stayed usable.**
- Step 6's own lead ledger is 2,642 lines in 136 entries at the writing, out
  of the round's 14,273 ledger lines.
- The lead works from it through:
  - its own dated headings;
  - a memory file holding the run's state and resume list;
  - briefs that cite the ledger lines an agent needs.
- Most agents read the parts their briefs cite. Integration verifiers read
  more: VI4, whose brief names the whole ledger, read 851 lines of it, and
  VI5 989, each in several reads (the third verifier's count, from their
  transcripts). Early agents read it whole while it was short, 31 to 328
  lines (the second verifier's count).

**11. Throughput was the owner's attention and the box, not the agents.**
- Step 6 had five parcels building at once at its peak, and their verifiers
  beside them, with the desktop held to at most two simulator containers.
- The serial resources were:
  - **the owner's answers,** which came within minutes or hours;
  - **the box,** one heavy job at a time. Its gate budget took 125 to 153
    minutes on each of seven runs, and the RTL suites 197 minutes.
- The README's "the bottleneck is not agent count" holds at this scale, with
  the box added beside the lead's merges.

## Cost of the run (measured from the transcripts)

**The method.** Each agent run is counted once.
- The draft of this file summed the task notifications' own figures, and its
  verifier found two faults in that:
  - 22 of the 277 notifications repeat an earlier one's run, with cumulative
    figures;
  - a notification's "tokens" is the agent's context size at the run's end,
    not the tokens it used. Case study 2 had warned that the cards' tokens
    "count what each agent's turns carried".
- So the tokens below are summed from each agent's own transcript, once a
  message, as case studies 5 and 6 did. Fresh tokens are input, cache writes
  and output; cache reads are counted apart.
- **Twelve notifications carry no usage at all,** each an agent cut off by
  an API error or a usage limit.
  - Three are parcel C's, still running at the writing and outside the table.
  - Five fell mid-run, and the same agents' later notifications cover those
    stretches.
  - The other four are two verifiers' runs on 09-25 and two parcels' on
    09-27, each cut off by a usage limit. Their 3.2 hours and 377 tool uses
    are read from the agents' own transcripts.
- The lead's own session is not included, nor the three agents still running
  at the writing.
- The scripts that made these figures, and observation 9's table, are
  archived beside this file in
  [archive/round7-cost-scripts.zip](archive/round7-cost-scripts.zip), with a
  README saying what each does. They read the session's transcripts, which
  are not published, so they show the method but cannot remake the figures.

| | agents | runs | agent-hours | tool uses | fresh tokens | cache reads |
|---|---|---|---|---|---|---|
| parcels | 43 | 108 | 112.0 | 19,052 | 193.4 M | 7.77 G |
| verifiers, larger model | 71 | 136 | 119.1 | 15,519 | 183.1 M | 5.91 G |
| verifiers, smaller model (from 10-05) | 6 | 6 | 7.7 | 1,360 | 6.0 M | 0.52 G |
| surveys and others | 9 | 9 | 2.7 | 1,022 | 4.3 M | 0.23 G |
| **all, 2026-09-25 to 10-05** | **129** | **259** | **241.4** | **36,953** | **386.7 M** | **14.42 G** |
| of which step 6 (agents whose first run began from 10-02 07:33) | 43 | 85 | 62.9 | 11,975 | 83.4 M | 4.61 G |

Each figure is rounded on its own. The hours' exact sum is 241.44.

- **Verifiers and parcels took about the same.**
  - The 77 verifiers used 189.0 M fresh tokens, against the 43 parcels'
    193.4 M.
  - The verifiers took more hours, 126.8 against 112.0.
  - They made fewer tool uses (16,879 against 19,052) and fewer cache reads
    (6.4 G against 7.8 G).
  - A parcel cost about twice a verifier: 4.5 M fresh tokens against 2.5 M.
- **What the draft had said:** 168.9 M "tokens" and 277.0 agent-hours, from
  277 notifications.
  - Counted by run, the same notifications give 154.8 M (a sum of final
    context sizes, which measures nothing spent) and 238.2 hours.
  - The four runs without a usage notification add 3.2 hours.
- **Box time for step 6:**
  - seven gate-budget runs, 125 to 153 minutes each;
  - one run of the RTL suites, 197 minutes;
  - probes L and S1 to S4b, 33 to 44 minutes each;
  - the card legs.

## What METHOD.md should say differently (proposed; the owner's to settle)

1. **An index that states counts is a P0 thing (section 2).**
   - What METHOD.md already says: section 1 says to derive counts, never
     transcribe them, and section 2 says to aim for a glob, not a list.
   - What happened: the project's document index transcribes counts and holds
     them with a gate, so every merge conflicts on its numbers (observation
     5).
   - The change: generate the index, or give its gate a mode that rewrites the
     counts.
2. **A shared table's row is the unit of conflict (section 2, beside "Aim for
   a glob, not a list").** Rows that parcels edit in parallel should be short,
   or one file each.
3. **A restatement by the lead reads every constant, count and list member
   from the code at the moment of writing (section 7, Habits).**
   - What exists: section 6 asks verifiers to "derive the increment" for any
     count a report quotes. Case study 6's pending section 4 proposal has a
     value in the lead's entry read from the command that measured it.
   - The change: extend both to the lead's restatements of decisions. Both of
     the second pass's wrong answers here were such restatements (observation
     3).
4. **A narrow re-check is scoped to the previous commit's diff, may run on a
   smaller model, and has a budget (section 6).**
   - What exists: section 6 already makes the scoped re-check the default,
     and section 3 records case study 4's loop ending once the lead scoped
     the next round to converge.
   - What is new: the scope (the diff since the last pass), the model, and the
     budget. Here the loop converged at 3, 2, 0.
5. **Any script that crosses an environment, a clone or a build host asserts
   its directory, commit and content before it builds (section 5).**
   - What exists: section 3's base-commit rules, and the project's "assert the
     SHA and the content separately", are the same idea for briefs and builds.
   - Why: the guard, not the note, is what stopped the traps here (observation
     7).
6. **Probes before images (section 8).**
   - What exists: section 7's "one instrument per hypothesis, cheapest first,
     before touching the design" is the principle.
   - The change: where a build costs hours, a measured out-of-context probe of
     the new logic comes first, and the plan names what each probe must show
     (observation 8).
7. **Verifier model choice is a recorded trial (section 6).**
   - The change: record each verifier's yield per model (findings, false
     findings, misses found later), as observation 9 does, until the question
     is settled.
   - Related: case study 5's pending "Models" proposals are the same trial from
     the other side. They put parcels and their verifiers on the smaller model
     when the work is sentences, and read each agent's model from its
     transcript.
8. **When rounds roll over, each still ends on paper (section 7).**
   - What happened: here each push has its VALIDATION entry. But a verifier
     found that two earlier verifiers' notes had not been carried into any
     entry.
   - What exists: METHOD.md section 6 gives side notes a step of their own in
     every round.
   - The change: check the carried notes as part of that step, at each entry.
9. **When the owner's machine is busy, agents' runs go to the lead's build host
   as batches (section 8; from after the writing, below).** An agent that may
   not touch the host writes its runs as a list: commit, edits, target and
   expected result. The lead runs the list there and returns the results.
   - What exists: section 7's "The long runs", the owner's rule that agents
     hand large runs back to the lead. It does not say how they travel.

## The run's state at the writing (2026-10-05, about 10:40)

- **On main:** step 6's first three waves (d4cf250).
- **Building:**
  - the sequencer's six items are done, with their follow-ups and last verifier
    to come;
  - the host side is merged into the round's integration branch;
  - a verifier is on the sequencer's flag-control items;
  - the math library's first part is in its design phase.
- **Next:** the second RTL round's merge and gate, two more probes, three
  images on the box, and their card legs. Then the rest of the math library.

**Since the writing (to about 12:45):**
- **VC34 reported.** It found the narrow wrong answer and four gaps above. The
  parcel fixed the one and adopted VC34's cases for the others.
- **The cascade remedy stays,** by probe S4b's result.
- **The sequencer's parcel finished:** six items and two follow-ups.
- **From about 11:05 the owner used the desktop heavily.** A game held it at
  100%, so by his rule of 09-29 no new simulator run started there.
  - The parcel stopped its own runs, and asked.
  - The lead built a batch runner on the box. An agent writes its runs as a
    list; the lead runs each in a fresh copy of its commit, two or three at a
    time, and returns the results.
  - The runner's smoke test reproduced a parcel's desktop red exactly.
  - By 12:45, the parcel's last runs had come back as expected, and two
    verifiers' seven batches, about a hundred runs, were running.

This file will gain a section when the round ends, as case studies 2 and 4
did.

## How this file was checked

A verifier, VCS7 on the smaller model, checked the draft against the records:
the ledgers, git, the lead's transcript, each agent's own transcript, the other
studies and METHOD.md. It edited nothing. It took 96 minutes.

- **Confirmed:**
  - most figures, every timeline time and every quotation;
  - the other studies' rows, with two corrections;
  - the six findings and the slips, and the probe and gate times;
  - the smaller-model verifiers' table, as reported.
- **Wrong, and corrected here:**
  - the cost method: the repeat notifications, and "tokens" read as tokens
    used;
  - the session's first day, and gate4's finder;
  - the ledger counts (an `urgent/` directory had been counted);
  - the step-6 cost row, which held two runs of the language round's verifier;
  - smaller-model verifiers named as new;
  - "each pass found something", and "resumed from its own ledger";
  - proposal 2's subsection, and where the traps are written.
- **Misleading or unsupported, and restated:**
  - "without a stop", and "carried in every brief";
  - "at least one compaction", and "an eighth revision";
  - "every one found something real", and "caught every one";
  - the wave-3 verifier's start;
  - "two to four runs of the gate", and "restated from memory";
  - "no agent reads the whole of it".
- **Missing, and added:**
  - the shorter stops and the 09-30 pause, and the fourteen continuations;
  - the out-of-turn channel's move to messages;
  - how case study 6's loop ended;
  - three more slips;
  - the pending proposals that this file's proposals overlap.

**The first revision, and a second verifier.** The lead checked each major
finding against the records before restating it. It re-derived the cost
section with its own scripts, from the transcripts.

A second verifier, VCS7b on the smaller model, then re-checked that
revision's diff, in 106 minutes. It confirmed most of it, and found 6 wrong
claims, 9 misleading and 2 unsupported. All of them were in the revision's
changed text, as its scope was:
- the run count, which missed four runs that ended in a notification with
  no usage: 259, not 255;
- gate4. Its programs stage had failed before the parcel reported. The
  draft had credited the gate alone, and the first verifier and the
  revision the parcel first. The record shows both;
- the brief counts. The lead's search had counted three briefs that only
  report an earlier verifier's "no wrong answer". Strictly, 94 of 112 state
  the send-back rule, and the owner's full hand-back sentence is in 17
  briefs, not 19;
- two stops left out: a weekly usage limit, and the hold before step 3;
- "four recurred on 10-05", where the fourth was earlier;
- a claim that the first verifier had listed the storm as a stop. The lead
  had, in its own list, and the storm was a precaution, not a stop;
- the lead's correction of the first verifier's desktop-rule count. In some
  wording every brief carries the rule, as the first verifier had said;
- overstatements: the smaller model's comparison, how the lead resumed, and
  the ledger's longest reads.

**The second revision, and a third verifier.** The lead checked the major
findings against the records before revising. Its own measurements were
these:
- the four runs and their 3.2 hours and 377 tool uses (two scripts over the
  transcripts);
- gate4's stage, at 23:41 from its stage times, and the parcel's report at
  23:44;
- the three briefs that only report an earlier verifier's "no wrong answer";
- the two stops, from the owner's prompts;
- the first-run medians.

The other figures the revision restated are the verifiers' own counts, and
the text now says whose: the hand-back wording, the continuations after
which the ledger and memory were read, and the ledger's longest reads. The
first verifier's count of briefs lacking the send-back rule, 11 of 115, was
low: strictly it is 19.

A third verifier, VCS7c on the smaller model, re-checked the second
revision's diff, in 49 minutes. It confirmed the run count, the stops and
the send-back split. It found six claims wrong, four misleading and one
unsupported, again in the changed text:
- gate4's time, 23:43 where the stage times give 23:41, and "within a
  minute", where the parcel reported three minutes later;
- the hand-back count, 30, which it recounts at 36;
- VI4's read, 885 lines asked against 851 returned;
- the smaller model's table, which set first runs against all runs;
- the fifteenth continuation, left undated;
- "agents read the parts their briefs cite", which VI4's brief did not;
- and the claim that the lead had recounted wherever a figure was the
  verifier's own, which it had not.

The lead fixed each of these in this version. It checked gate4's stage
times and the first-run medians itself, and it attributes the other counts
above.

**The loop, and where it stopped.** This file's own correction loop ran as
observation 3's did. Each revision of the lead's drew new errors in its own
changed text: 17 at the second pass and 11 at the third, smaller each time.
A re-check scoped to the diff found them.

The third pass was the budgeted last one. Its findings were fixed without a
fourth, which is this file's known limit.

**Before the push: main had moved.** The lead wrote this file in a checkout
of ParcelRound whose main was 8767e23. Round 6 had been pushed to main on
10-03, and the checkout had not been pulled since. So this file said that
case studies 5 and 6 were on unmerged branches, and it cited METHOD.md as it
stood before round 6. The lead's briefs gave its three passes the same
premise, and none of them caught what it hid. Before pushing, the lead found
it in the checkout's own record of the remote, and `git ls-remote` confirmed
it: the repository has one branch, main, at f42242e, which holds both
studies and round 6's METHOD.md. It is a slip of observation 2's kind: a
remote's state read from a local copy, not measured.

The lead rebased this file on f42242e and linked both studies. It read each
of the file's METHOD.md citations again at f42242e, and so did the fourth
pass below. All hold there but two, both restated: proposal 8 called the
side-notes step pending, and section 6 now has it; observation 4 said
section 4 makes the ledger the only way to correct a brief, where section 4
now lets a message carry the correction once its entry is written. Other
sentences now name where METHOD.md says what round 6 adopted: the verifier
on the lead's work, messages in both directions, the send-back and hand-back
rules, and the rules beside proposals 4 and 9. The cost scripts are archived
beside this file.

A fourth verifier, VCS7d on the smaller model, checked this revision in 31
minutes. It confirmed the stale base's facts, the rebase, the archive's
bytes and its privacy, and every citation but the two above. It found two
wrong sentences, both in the archive's README: one script, firstruns.py, is
the lead's file of a program it had run inline, not the copy it ran; and
the scripts were not listed in the order of their use. It found five
misleading ones, among them observation 4's and this section's account of
how the lead found the stale base. All are fixed in this version, without a
fifth pass, which is this revision's known limit.

This file practised case study 5's pending proposal CS5#11: it was written
from the records, and read against them by verifiers other than the lead
before its push.
