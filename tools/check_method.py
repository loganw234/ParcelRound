#!/usr/bin/env python3
"""ParcelRound's gate: does the method still hold together?

    python tools/check_method.py            every check; exit 1 if any fails
    python tools/check_method.py --control  plant faults, each in a copy of the
                                            tree or in a scratch repository, at
                                            least one per check; each must be
                                            caught

It reads structure and citations, never what a rule says. A gate that reads a
rule's wording is a stated limit, not a guarantee (case study 4's proposals
for section 5). Checks 7 and 9 read text, and are such limits.

Threat model (the owner's decision, 2026-10-02). The gate guards against two
things:
  - drift by honest, fallible authors:
    - a reference that goes stale as files change (a line number, a link, an
      anchor, a section number);
    - a citation of something the record does not hold;
    - a passage another repository reads, changed or duplicated;
    - the adoption record drifting from the case studies;
    - a section renamed, or an archived record edited;
  - accidental publication: a personal address, a home-directory path or a
    secret-shaped token written into a file, an archive, the index, history
    or a commit message, the way pasted output or a careless note carries one.
It does not guard against deliberate evasion: text built to pass it, such as
an address encoded, split or spelled out, or a citation or link in a syntax
its patterns don't read. Catching that is the verifiers' and the owner's job.
Nor does it judge content: whether a rule says what its incident supports is
a verifier's question, not this gate's. A fault built against the gate is
judged against this paragraph. Inside the threat model, the gate must catch it
or a limit below must state it. Outside the model, it is out of scope.

The checks, by name:
  links      1. every relative link target in a Markdown file names a file
                inside the repository, spelled exactly as it is (GitHub's paths
                are case-sensitive), and in a repository one in the index; an
                #anchor into a Markdown file names one of its headings
  citations  2. every case-study citation in METHOD.md and templates/ resolves
                to its round's record: the case study's own text (its bracketed
                citations aside), or the Markdown of the round's ledger archived
                beside it. Every item a citation holds must resolve, so one that
                names its case study any other way fails. The archived ledgers'
                bytes are pinned.
  proposals  3. every proposal in a case study's list "What METHOD.md should
                say differently" has exactly one row in ADOPTION.md, and so
                does every id in OTHER_IDS (the B, R and S rows); a row with
                any other id fails
  anchors    4. every ADOPTION.md row whose status is adopted names METHOD.md
                headings that exist; every file:line in ADOPTION.md, METHOD.md,
                README.md and templates/ (outside code, but anywhere in
                ADOPTION.md) has a commit, in backticks, in its cell or line;
                in a repository, every commit ADOPTION.md writes in backticks,
                and every commit beside a line number in those files, is in
                HEAD's history, unless FOREIGN_COMMITS declares it another
                repository's pin; and each pin declared there is still named,
                in ADOPTION.md or beside a line number in those files. The case
                studies and the archive are records that do not change, so
                their line numbers are not read.
  refs       5. every section number written with a section sign or the word
                "section", alone or in a list, in METHOD.md, README.md,
                ADOPTION.md and templates/, is one of METHOD.md's sections. A
                section mark inside a citation that check 2 reads is check 2's.
  readme     6. README.md links every case study and every template
  brieferr   7. templates/brief.md's report section still asks what the brief
                got wrong
  sections   8. METHOD.md's eight sections keep their numbers and titles
  quoted     9. each passage loganw.dev reads through facts.prose() (the
                patterns its page modules and its relations.json run on this
                repository, read at loganw.dev LOGANW_REV) and each passage
                HonestFramework quotes (read at HF_REV) matches exactly once,
                with and without its fenced code and HTML comments
  privacy   10. no email address, personal path or secret-shaped token, but
                those allowed, in: the working tree's files a commit would
                publish, and their names; in a repository, the index's staged
                contents, every blob in HEAD's history and every commit
                message; every archive member, its name and its comment,
                nested archives opened, and a gzip header's name and comment.
                The text is decoded first: percent-escapes, HTML entities,
                Unicode compatibility forms, and invisible format characters
                removed. A file it cannot read fails.

How Markdown is read. Checks 7, 8 and 9, and check 4 for METHOD.md's headings,
remove fenced code blocks and HTML comments first. Check 6 also removes code
spans, since a link in code is not a link. Checks 1, 2 and 5 remove code spans
and fenced code blocks, since code shows a form rather than using it, and read
HTML comments. Check 4 reads ADOPTION.md's line numbers and commits in all of
its text, and line numbers in METHOD.md, README.md and the templates outside
their code. A check that crashes fails, by name. No failure line prints a path, address or token the
gate refuses: its output is pasted into ledgers that will be published. There
is no cache: each run reads everything again. Standard library only, and git
for what checks 1, 4 and 10 read from a repository.

Citation forms (check 2) in METHOD.md and the templates:
  [CASE-STUDY-n, 15:09]   a time in case study n, or in its archived ledger;
                          ranges (12:00-12:30) and minute wildcards (08:2x)
                          read too
  [12:37]                 a bare time is round 2's, in METHOD.md only; in a
                          template, a citation names its case study
  [CASE-STUDY-n, §4]      a section mark in case study n
  [CASE-STUDY-n, obs 10]  a numbered observation, where the case study numbers
                          its observations (case studies 4 and 5)
  [The setting]           a heading or a bold-marked item of the case study
                          (such as "the card day"), by its opening words
  [CASE-STUDY-n, the ledger]  the round's archived ledger itself
  Items are separated by ";" or ",". Square brackets in METHOD.md hold
  citations: every bracketed text is read as one, but a link's text, a label
  that a link definition in the same file defines, and code. An incident
  recorded outside the case studies is cited as a Markdown link to its record,
  e.g. [round 6's survey, B3](archive/round6-practice-survey.md), which check 1
  resolves.

What it cannot see. Each limit is stated by the behaviour it concedes, so that
a new spelling of a stated class falls inside it:
  - links: links are found by patterns, not by a CommonMark parser. They read
    inline links (wrapped, with one level of brackets in their text, and with
    a plain or an angle-bracket target) and link definitions (with the target
    on the same line or the next). A link in any other syntax is not read:
    HTML, an autolink, or brackets nested deeper. A link definition is a
    label, a target and an optional title alone on their line; a line with
    more on it renders as text, and is read as text. A link with a scheme
    (https:, mailto:) is not fetched. A link's text and its target are not
    compared: text that names one file, line or commit, beside a URL that
    names another, passes. An anchor into a file that is not
    Markdown is not checked. Anchors are computed by GitHub's rule for "#"
    headings of plain text, so a setext heading, or one holding HTML, may
    differ. Outside a repository, a target need only exist on disk.
  - citations: citations are found by a pattern over square brackets, not by
    a parser. A citation in any other shape is not read: in parentheses, as a
    link's text, as an image's alt text, or in code. Nor is one outside
    METHOD.md and templates/. A footnote's text is read, and so is a line
    that only looks like a link definition.
    - An item resolves by existing, not by being the one the sentence means.
      An item that names something real but wrong passes, whatever its form:
      a minute, a phrase, an observation number or a section mark.
    - A time resolves if the round's record holds that minute anywhere in the
      case study's text or the archived ledger's Markdown, whatever it was: an
      entry's stamp, a time an entry records, a ratio such as 1:24, an
      example.
    - A named phrase resolves if it opens any heading or bold-marked item at
      a word boundary, so a phrase that opens many (such as "the") passes.
    - In a template, a bracketed phrase with no time, section mark or
      observation number is a placeholder.
  - proposals: it holds ids, not the rows' content, so a wrong status passes.
  - anchors: it holds that an adopted row's headings exist, not that the rule
    is under them. It holds that every file:line in the files check 4 names
    has a commit beside it, and in a repository that each commit is in HEAD's
    history; not that the line is right at it, nor that the commit beside it
    is the one it was counted at. A line named any other way ("line 66 of
    METHOD.md") is not read, nor is a line number in a case study or the
    archive, nor a commit written other than in backticks. Outside a
    repository, a commit is not looked up.
  - refs: a section number is read after the section sign or the word
    "section", in any case, alone or in a list joined by commas, "and", "or",
    "to", "through", "&" or dashes. A section named any other way is not
    read: in words, by its title, or by an abbreviation such as "Sect.".
  - brieferr: it reads templates/brief.md's report section only. The clause
    kept where nothing asks it (negated, or moved within the report section)
    passes, and so does METHOD.md's own statement of the rule, changed in any
    way. A respelled clause fails it.
  - quoted: it holds the passages in LOGANW_PATTERNS and HF_PASSAGES.
    - A passage another repository starts to quote, or that loganw.dev reads
      other than through facts.prose() from its page modules and
      relations.json, is held only once it is added there.
    - HonestFramework's quotations are held with whitespace and emphasis set
      aside. A copy that differs from a passage in anything else (letter
      case, punctuation, quotation marks, a word) is not counted as a copy,
      and passes.
    - loganw.dev's other reads of this repository (file counts, existence,
      last change, commits by SHA) are not held.
  - privacy: it reads text after the decoding check 10 names.
    - An address, path or token written any other way that a reader could
      reassemble passes: spelled out, split by a line break or by markup, in
      another script's look-alike letters, encoded in base64,
      quoted-printable or another scheme, or inside an image.
    - A path is personal when it names a home directory in one of USER_PATH's
      shapes, behind any prefix. A forward-slash shape inside a URL with a
      host (a token beginning scheme://host, or a dotted host name) is
      excused, so a home written as a URL's path passes. A home reached any
      other way passes: through an environment variable, a symbolic link, a
      mapped drive, or a share of another name.
    - A secret of a shape not in SECRET passes.
    - The personal paths in the archived ledgers KNOWN_PATHS names pass by
      design: they are records published before this gate, and their bytes
      are pinned.
    - Author and committer fields are not read. Every commit's carry the
      owner's own address, public in each commit.
    - Only the working tree, the index and HEAD's history are read. Other
      branches, stashes and tags are not: only main is pushed, and a branch
      push carries no tags.
    - A binary file whose zero bytes fall like UTF-16's is read as that text.
  - everywhere: an indented code block is read as text.
Each of these is on every verifier's list by name.
"""
import contextlib
import gzip
import hashlib
import html
import io
import os
import posixpath
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import unicodedata
import zipfile
from urllib.parse import unquote

# Each case study's ledger, archived beside it. Round 1 kept none.
ARCHIVES = {
    2: ["round2-ledger.zip"],
    3: ["round3-ledger.zip"],
    4: ["round4-ledger.zip", "round4-second-ledger.zip"],
    5: ["round5-ledger.zip"],
}
# The archived ledgers are records, so their bytes never change: a citation
# resolves against a record nobody can edit unseen, and the paths an archive
# may hold (check 10) stay the ones it was published with.
ARCHIVE_SHA256 = {
    "archive/round2-ledger.zip": "d5eed511e455ebc87fef777a6e38df81fb070b6dd87a070d0de044e87929cd3e",
    "archive/round3-ledger.zip": "3a8a191e4e32607d03bf100c919e321e0a56c6d1cb8a52533490fd0d6bbca150",
    "archive/round4-ledger.zip": "6166f93f725f604282a244cec3ea8cd3850918a113b1db86fbba08ec5a99f2f7",
    "archive/round4-second-ledger.zip": "71c1b4f29978c16809a2d66f8a799c307d5c8815682e523972cf32c2c239c28e",
    "archive/round5-ledger.zip": "0f44d183b570bf5c5f49aa68dfd7da9ed7ceee2cbbc645c1bffb520417213e1e",
}
# Declared once and checked (METHOD.md section 1, the second grade): the case
# studies are records, so their proposal lists never change. A parse that
# finds another count means the parser or a record changed, and either is a
# finding.
EXPECTED_PROPOSALS = {2: 35, 3: 18, 4: 23, 5: 13}
# ADOPTION.md's other rows, declared once: practices nobody proposed (B),
# safeguards restored (R) and adaptations allowed (S), from round 6's survey.
OTHER_IDS = ["B1", "B3", "B4", "B8", "B9", "B10", "B11", "B12", "B13", "B14", "B15", "B16", "B17",
             "R1", "R2", "R3", "R4", "R5",
             "S1", "S2", "S3", "S4", "S5", "S6"]
# METHOD.md's preamble: bare times are round 2's.
METHOD_DEFAULT_ROUND = 2
# The headings under which case studies number their observations.
OBSERVATION_SECTIONS = ("what the method predicted, and what happened",
                        "observations from the second round")

# Other repositories cite METHOD.md by section number (HonestFramework cites
# "ParcelRound's section 5"), so the eight sections keep their numbers and titles.
SECTIONS = [
    "1. The one failure mode",
    "2. P0: make the shared thing shared, before you split",
    "3. The brief",
    "4. The ledger",
    "5. Gates and negative controls",
    "6. The verifier",
    "7. What the lead keeps",
    "8. Sequencing",
]

# loganw.dev reads these at its pin with re.finditer(pattern, text, re.M) and
# refuses any count but one (its site/facts.py, prose()). They are the patterns
# it hands facts.prose() for this repository at LOGANW_REV, copied verbatim:
# one per call in its page modules (found by reading their calls), and one per
# edge of its site/data/relations.json (mapgen.py, all_edges). A rewrap that
# would break one breaks this.
LOGANW_REV = "43c36a2"
LOGANW_PATTERNS = [
    ("CASE-STUDY-2.md", 'produced (four send-backs, none for a wrong bit)', "site/pages/method.py:102"),
    ("CASE-STUDY-2.md", 'puts the human-active time at (1 h 38 min against\\s+23 h 40 min of API time across every agent)', "site/pages/method.py:33"),
    ("CASE-STUDY-2.md", '(every guess was AHEAD of the clock \\(by 3 to 90 minutes\\))', "site/pages/work_parcelround.py:54"),
    ("CASE-STUDY-2.md", '(The fix that finally held for the lead was mechanical: write the entry with a placeholder and let the append command substitute `date`)\\.', "site/pages/work_parcelround.py:57"),
    ("CASE-STUDY-2.md", '(stamps are substituted, not typed)\\.', "site/pages/work_parcelround.py:60"),
    ("CASE-STUDY-2.md", '(which is how a wrong number propagates - it was in the ledger for fifteen minutes and got used once)', "site/pages/work_parcelround.py:63"),
    ("CASE-STUDY-2.md", '(a correction should EDIT nothing but should be linked from the entry it corrects)', "site/pages/work_parcelround.py:66"),
    ("CASE-STUDY-2.md", '(\\"see 11:52\\" appended below the old entry is an append, not an edit)', "site/pages/work_parcelround.py:68"),
    ("CASE-STUDY-2.md", '(a number a sibling might reuse should be stated in the entry that supersedes it in the form the sibling would search for)\\.', "site/pages/work_parcelround.py:70"),
    ("CASE-STUDY-3.md", '^(Six send-backs and eleven defects)\\.', "site/pages/method.py:105"),
    ("CASE-STUDY-3.md", 'the gate: (32 planted controls, 29 of 29 mutations killed)', "site/pages/method.py:107"),
    ("CASE-STUDY-4.md", "\\*\\*atlas-film's `pinned`\\*\\* at `([0-9a-f]{7})`", "site/pages/home.py:134"),
    ("CASE-STUDY-4.md", "(Whether atlas-film's `pinned` merges into its main)", "site/pages/home.py:135"),
    ("CASE-STUDY-4.md", '(Every print re-developed to the same bits) \\(`--check`\\)', "site/pages/home.py:214"),
    ("CASE-STUDY-4.md", '\\*\\*(equality with the authority passed 10 of 11 planted certificate faults)\\*\\*', "site/pages/method.py:110"),
    ("CASE-STUDY-4.md", '(P2 moves atlas-film)', "site/data/relations.json, edges[10]"),
    ("LICENSE", '^(MIT) License', "site/pages/propose.py:92"),
    ("METHOD.md", '\\*\\*(Exactly one file owns each shared fact; everyone else includes it)\\.\\*\\*', "site/pages/method.py:63"),
    ("METHOD.md", '## 1\\. (The one failure mode)', "site/pages/work_parcelround.py:36"),
    ("METHOD.md", "The failure is that (\\*\\*the work between the parcels belongs to\\s+nobody\\*\\*, and it is invisible because every parcel's own gate is green)\\.", "site/pages/work_parcelround.py:37"),
    ("README.md", '^(A method for splitting one body of work across several coding agents\\s+at\\s+once)', "site/pages/home.py:106"),
    ("README.md", '^(A method for splitting one body of work across several coding agents\\s+at\\s+once,\\s+without the pieces failing to meet)\\.', "site/pages/method.py:60"),
    ("README.md", '^(A method for splitting one body of work across several coding agents\\s+at\\s+once)', "site/pages/thread_determinism.py:39"),
    ("README.md", '^(A method for splitting one body of work across several coding agents at\\s+once, without the pieces failing to meet)\\.', "site/pages/work_parcelround.py:22"),
    ("README.md", '## (Is this for you\\?)', "site/pages/work_parcelround.py:27"),
    ("README.md", "\\*\\*Don't\\*\\* (for a single task, for exploratory work where the split isn't\\s+obvious yet, or where the pieces can't be tested separately)\\.", "site/pages/work_parcelround.py:28"),
    ("README.md", '(Two agents\\s+on a two-way split is usually slower than doing it yourself, because\\s+the brief costs more than the work)\\.', "site/pages/work_parcelround.py:31"),
    ("README.md", '\\*\\*(twelve corrections from five parcels — every single parcel\\s+corrected its brief)\\*\\*', "site/pages/work_parcelround.py:46"),
    ("README.md", '\\*"(Report anything you found that this brief got wrong)\\."\\*', "site/pages/work_parcelround.py:50"),
]
# HonestFramework quotes these through unpinned links (its WITH-PARCELROUND.md
# and METHOD.md, read at HF_REV), re-wrapped in its own lines, one marked "word
# for word" and others with a word's case changed or split in two. This holds
# ParcelRound's own words, so what HonestFramework quotes stays here to find.
HF_REV = "65447fd"
HF_PASSAGES = [
    ("README.md", "**Merge serially, run the full suite after each one, and read the log rather than the exit code.**"),
    ("METHOD.md", "**A gate that cannot fail is not a gate**"),
    ("METHOD.md", "A control described but not run is worth nothing, so ask for its output."),
    ("METHOD.md", "**re-run the gate itself**, from a clean build, rather than trust pasted output"),
    ("METHOD.md", "**It must NOT fix anything.** A verifier that edits is a second author with none of the first one's context, and you lose the independence you paid for."),
    ("METHOD.md", "Require it to state what it actually ran, command by command, and make **\"found nothing\" an acceptable, unpenalised answer**. A verifier under pressure to produce findings invents them, which is worse than none."),
]

EMAIL = re.compile(r"([A-Za-z0-9._%+-]+)@([A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,})")
# Allowed: the co-author trailer's address, the public contact, and the
# domains reserved for examples (RFC 2606 and RFC 6761).
ALLOWED_ADDRESSES = {"noreply@anthropic.com", "logan@loganw.dev"}
RESERVED = re.compile(r"(^|\.)(example\.(com|net|org)|example|invalid|test|localhost)$", re.I)
# A home directory, in any case, in each shape it takes:
#   - a Windows profile under its drive: C:\Users\<name>, c:/users/<name>, and
#     the older Documents and Settings;
#   - the drive mounted as a directory, behind any prefix: /c/Users/<name> (MSYS),
#     /mnt/c/... (WSL), /cygdrive/c/..., /host_mnt/c/... (containers);
#   - backslashed with no drive, or over a share: \Users\<name>, and a WSL home
#     reached as \\wsl$\<distro>\home\<name>;
#   - a POSIX home, /home/<name> or /Users/<name>, behind any prefix: file:///,
#     a PATH list, /var, /usr, /export, a mounted disk.
# The two forward-slash shapes are excused only inside a URL with a host,
# since github.com/users/... is a URL; see personal_paths().
# Built from parts, so that this file holds no personal path of its own to find.
_SL, _BS = "/", "\\"
_PROFILES = "(?:" + "us" + "ers|documents and settings)"
_NAME = r"[^\\/\s'\"`<>|*?:]+"
USER_PATH = re.compile(
    r"(?i)(?<![\w])[a-z]:[\\/]+" + _PROFILES + r"[\\/]+" + _NAME
    + "|" + _BS + _BS + "(?:" + "us" + "ers|documents and settings|ho" + "me)" + _BS + _BS + "+" + _NAME
    + "|(?P<slash>" + _SL + "(?:[a-z]" + _SL + _PROFILES + "|" + "us" + "ers|ho" + "me)" + _SL + _NAME + ")")
# A token that is a URL with a host: scheme://host..., or a dotted host name
# such as github.com, with an optional port, then a path.
_URL_TOKEN = re.compile(r"(?i)(?:[a-z][a-z0-9+.-]*://[^\s/]+|[\w-]+(?:\.[\w-]+)*\.[a-z]{2,}(?::\d+)?)(?:/|$)")
# Invisible format characters (Unicode category Cf: zero-width spaces and
# joiners, the soft hyphen, the byte-order mark), which can sit inside an
# address or a path without showing.
_FORMAT_CHARS = re.compile("[" + "".join(re.escape(chr(c)) for c in range(sys.maxunicode + 1)
                                         if unicodedata.category(chr(c)) == "Cf") + "]")
# Common credential shapes, built from parts for the same reason.
SECRET = re.compile("|".join([
    "gh" + r"[pousr]_[A-Za-z0-9]{20,}",
    "github" + r"_pat_[A-Za-z0-9_]{20,}",
    "s" + r"k-[A-Za-z0-9_-]{20,}",
    "[sr]" + r"k_live_[A-Za-z0-9]{16,}",
    "AK" + r"IA[0-9A-Z]{16}",
    "AI" + r"za[0-9A-Za-z_-]{35}",
    "gl" + r"pat-[A-Za-z0-9_-]{20,}",
    "np" + r"m_[A-Za-z0-9]{36}",
    "xo" + r"x[abprs]-[A-Za-z0-9-]{10,}",
    "hooks" + r"\.slack\.com/services/[A-Za-z0-9/]{20,}",
    "-----BEGIN " + r"(?:RSA |OPENSSH |EC |DSA |PGP )?PRIVATE KEY-----",
]))
# Addresses published before this gate existed, held per archive member and
# per domain, with their counts. A personal domain is held by its SHA-256 only,
# since naming it here would publish it again. Any address beyond these fails,
# and an entry whose count no longer holds fails as stale, so this list can't
# outlive its reason.
KNOWN_PRIVACY = {
    "archive/round4-ledger.zip": {
        "why": "published at b1e5956 (2026-09-26); removing these needs a history "
               "rewrite, which is the owner's decision",
        "counts": {
            ("quantum-film-round1-ledger/verifier-P0.md", "amazon.com"): 1,  # a third party's public contact
            ("quantum-film-round1-ledger/verifier-P0.md", "sha256:0c6e258fbe0837f27541c44a2744d0a0a2a8d2047a281c04fcc056c4aeb7f3cc"): 1,
            ("quantum-film-round1-ledger/verifier-P2.md", "sha256:0c6e258fbe0837f27541c44a2744d0a0a2a8d2047a281c04fcc056c4aeb7f3cc"): 3,
        },
    },
}
_PUBLIC_KNOWN_DOMAINS = {"amazon.com"}
# The archived ledgers whose members hold the personal paths of the machines
# their rounds ran on. They are records, published before this gate, so their
# paths pass, but only while their bytes are the pinned ones; an archive
# listed here that holds no path fails as stale. A new archive is not listed:
# it is held to no paths.
KNOWN_PATHS = [
    "archive/round2-ledger.zip",
    "archive/round3-ledger.zip",
    "archive/round4-ledger.zip",
    "archive/round4-second-ledger.zip",
    "archive/round5-ledger.zip",
]

STAMP = re.compile(r"(?<![\d:])(\d{1,2}):(\d[\dx])(?![\d:])")
# Square brackets around text, wrapped or not but never across a blank line.
BRACKET = re.compile(r"\[((?:[^\[\]\n]|\n(?![ \t]*\n))*)\]")
# A case study's own citations, stripped from its text before its times are
# read: bracketed text that is not a link's text.
CITATION = re.compile(r"(?<!\])\[((?:[^\[\]\n]|\n(?![ \t]*\n))+)\](?![(\[])")
# What makes a bracketed phrase in a template a citation rather than a placeholder.
CITES = re.compile(r"(?<![\d:])\d{1,2}:\d[\dx](?![\d:])|§\s*\d|\bobs(?:ervation)?\.?\s*\d", re.I)
# An inline link's target: plain, or in angle brackets (which may hold spaces),
# with an optional title.
_TARGET = r"\(\s*(?:<([^>\n]+)>|([^\s()<>]+))(?:\s+(?:\"[^\"]*\"|'[^']*'|\([^)]*\)))?\s*\)"
_LINK_TEXT = r"(?:[^\[\]\n]|\n(?![ \t]*\n))*"
LINK = re.compile(r"\[" + _LINK_TEXT + r"\]" + _TARGET)
# A link whose text holds one level of brackets, such as a badge: [![alt](image)](target).
LINK_NESTED = re.compile(r"\[(?:[^\[\]\n]|\[" + _LINK_TEXT + r"\](?:\([^)\n]*\))?|\n(?![ \t]*\n))*\]" + _TARGET)
# A link definition: a label (not a footnote's), its target on the same line
# or the next, an optional title, and nothing else on the line. A line with
# more on it is no definition, and renders as text.
LINK_DEFINITION = re.compile(r"(?m)^ {0,3}\[(?!\^)([^\]\n]+)\]:[ \t]*\n?[ \t]*(?:<([^>\n]+)>|([^\s<]\S*))"
                             r"(?:[ \t]+(?:\"[^\"\n]*\"|'[^'\n]*'|\([^)\n]*\)))?[ \t]*$")
# A footnote's definition, "[^9]:"; the footnote's text after it is read.
FOOTNOTE_LABEL = re.compile(r"(?m)^ {0,3}\[\^[^\]\n]+\]:")
LEDGER_PHRASE = re.compile(r"(?:the )?(?:round's |parcels' |lead's )?ledger(?: files?)?", re.I)
FENCE = re.compile(r"(?ms)^ {0,3}(`{3,}|~{3,})[^\n]*\n.*?(?:^ {0,3}\1[ \t]*$|\Z)")
COMMENT = re.compile(r"(?s)<!--.*?(?:-->|\Z)")
CODE_SPAN = re.compile(r"`(?:[^`\n]|\n(?![ \t]*\n))*`")
# A section number, after the section sign or the word "section", in any case,
# alone or in a list: "§4", "§§4-6", "§§4 and 9", "§4-§6", "Section 4",
# "sections 4, 5 and 6", "sections 4 through 9", "sections 4 & 9".
_SECTION_JOIN = r"(?:\s*(?:,|;|&|-|\u2013|\u2014|\band\b|\bor\b|\bto\b|\bthrough\b)\s*)"
SECTION_REF = re.compile(r"§§?\s*(\d+)((?:" + _SECTION_JOIN + r"§?\s*\d+)*)"
                         r"|\bsections?\s+(\d+)((?:" + _SECTION_JOIN + r"\d+)*)", re.I)
# A line number ADOPTION.md gives, such as METHOD.md:66 or CS2:358, and a
# commit as ADOPTION.md writes one, in backticks: `49a9266`.
LINE_REF = re.compile(r"(?<![\w/.])[A-Za-z][\w./-]*:\d+(?:-\d+)?\b")
COMMIT_REF = re.compile(r"`([0-9a-f]{7,40})`")
# Another repository's commits that ADOPTION.md names, declared once: each is
# that repository's pin, not one of this repository's, and each must still be
# named, so this list can't outlive its reason.
FOREIGN_COMMITS = {
    "4190a47": "cft-fp256, the commit at which its public docs/VALIDATION.md and docs/ROADMAP.md are read",
}


def read(root, rel):
    with open(os.path.join(root, rel), encoding="utf-8") as f:
        return f.read()


def md_files(root):
    out = []
    for d, dirs, files in os.walk(root):
        dirs[:] = [x for x in dirs if x != ".git"]
        for f in files:
            if f.endswith(".md"):
                out.append(os.path.relpath(os.path.join(d, f), root).replace(os.sep, "/"))
    return sorted(out)


def _blank(m):
    """The match's text as spaces, its line breaks kept, so line numbers hold."""
    return re.sub(r"[^\n]", " ", m.group(0))


def _lines_only(m):
    return "\n" * m.group(0).count("\n")


def rendered(text):
    """Markdown as a reader sees it: fenced code blocks and HTML comments gone."""
    return COMMENT.sub(_lines_only, FENCE.sub(_lines_only, text))


def uncoded(text):
    """Markdown with its code (fenced blocks and spans) blanked: code shows a
    form rather than using it."""
    return CODE_SPAN.sub(_blank, FENCE.sub(_lines_only, text))


def line_of(text, pos):
    return text.count("\n", 0, pos) + 1


def norm_stamp(h, m):
    return f"{int(h):02d}:{m}"


def stamp_matches(cited, known):
    if len(cited) != len(known):
        return False
    return all(a == b or a == "x" or b == "x" for a, b in zip(cited, known))


def git(root, *args, data=None):
    """A read-only git command in root, as bytes, taking no optional lock that
    another session working in the same repository would notice."""
    env = dict(os.environ, GIT_OPTIONAL_LOCKS="0")
    return subprocess.run(["git", "-C", root, *args], input=data, capture_output=True,
                          check=True, env=env).stdout


def is_repository(root):
    # A repository's .git is a directory; a worktree's is a file naming its repository.
    return os.path.exists(os.path.join(root, ".git"))


# ---- the round's record: what a citation may resolve against ----

def case_study_file(n):
    return "CASE-STUDY.md" if n == 1 else f"CASE-STUDY-{n}.md"


def record_of(root, n):
    """The times, section marks, headings and numbered observations of round n's record."""
    text = read(root, case_study_file(n))
    lines = text.splitlines()
    # A case study's own bracketed citations are not evidence for a citation of
    # it: strip them before reading its times.
    own = CITATION.sub(" ", text)
    stamps = {norm_stamp(h, m) for h, m in STAMP.findall(own)}
    archived = False
    for z in ARCHIVES.get(n, []):
        path = os.path.join(root, "archive", z)
        if not os.path.exists(path):
            continue
        archived = True
        # Every time in the ledger's Markdown, its entries' stamps and the times
        # their bodies record: round 2's suite "started 11:47" in the body of the
        # 11:48 entry, and METHOD.md cites the start.
        with zipfile.ZipFile(path) as zf:
            for name in zf.namelist():
                if name.endswith(".md"):
                    body = zf.read(name).decode("utf-8", "replace")
                    stamps |= {norm_stamp(h, m) for h, m in STAMP.findall(body)}
    headings = [l.lstrip("#").strip().lower() for l in lines if l.startswith("#")]
    # Bold-marked items, such as a timeline's "**The card day begins**".
    bold = [re.sub(r"\s+", " ", b).strip().lower() for b in re.findall(r"\*\*([^*]+)\*\*", text)]
    observations, in_obs = set(), False
    for l in lines:
        if l.startswith("#"):
            in_obs = any(l.lstrip("#").strip().lower().startswith(s) for s in OBSERVATION_SECTIONS)
        elif in_obs:
            m = re.match(r"^\s*(\d+)\.\s+\*\*", l)
            if m:
                observations.add(m.group(1))
    return {"text": text.lower(), "stamps": stamps, "headings": headings, "bold": bold,
            "observations": observations, "archived": archived}


def opens(phrase, items):
    """True if the phrase opens one of the items and ends at a word boundary
    there: "the card day" opens "the card day begins", and "w" opens nothing."""
    for h in items:
        if h.startswith(phrase) and (len(h) == len(phrase) or not (h[len(phrase)].isalnum()
                                                                  or h[len(phrase)] == "_")):
            return True
    return False


def resolve_phrase(phrase, n, rec):
    p = re.sub(r"\s+", " ", phrase).strip().lower()
    if opens(p, rec["headings"] + rec["bold"]):
        return None
    if LEDGER_PHRASE.fullmatch(p) and rec["archived"]:
        return None  # a citation of the round's archived ledger itself
    return f"'{phrase}' opens no heading or bold-marked item of case study {n}"


def resolve_item(item, n, rec):
    """None if the item resolves in round n's record, else the reason. What an
    item holds beside its time must resolve too, so "CS3 02:00" is no time of
    round 2's: "CS3" opens nothing there."""
    item = re.sub(r"\s+", " ", item).strip().lstrip("~").strip()
    if not item:
        return "an empty item"
    found = [norm_stamp(h, m) for h, m in STAMP.findall(item)]
    if found:
        missing = [s for s in found if not any(stamp_matches(s, k) for k in rec["stamps"])]
        if missing:
            return f"no {', '.join(missing)} in round {n}'s record"
        # What is left once the times are gone, but a range's dash or brackets.
        rest = re.sub(r"(?:^|(?<=\s))[~()\-\u2013\u2014]+(?=\s|$)", " ", STAMP.sub(" ", item)).strip()
        return resolve_phrase(rest, n, rec) if rest else None
    m = re.search(r"§\s*(\d+)", item)
    if m:
        k = m.group(1)
        if not (f"**§{k}" in rec["text"] or any(f"§{k}" in h for h in rec["headings"])):
            return f"no §{k} in case study {n}"
        rest = (item[:m.start()] + item[m.end():]).strip().lower()
        if rest in ("", "of the case study"):
            return None
        return f"'{rest}' beside §{k} is no part of a citation's forms"
    m = re.fullmatch(r"obs(?:ervation)?\.?\s*(\d+)", item, re.I)
    if m:
        k = m.group(1)
        return None if k in rec["observations"] else f"no numbered observation {k} in case study {n}"
    return resolve_phrase(item, n, rec)


# ---- the checks: each returns (failures, a line that says what ran) ----

def resolve_path(root, base, target):
    """(the repository path a link names, None), or (None, why not). Each part
    must exist spelled exactly so: GitHub's paths are case-sensitive, and a
    trailing dot that Windows forgives is a different name there."""
    joined = target.lstrip("/") if target.startswith("/") else posixpath.join(base, target)
    norm = posixpath.normpath(joined)
    if norm == ".":
        return "", None
    if norm == ".." or norm.startswith("../"):
        return None, "it points outside the repository"
    cur = root
    for part in norm.split("/"):
        try:
            names = os.listdir(cur)
        except (NotADirectoryError, FileNotFoundError):
            return None, "which does not exist"
        if part not in names:
            near = [x for x in names if x.lower() == part.lower().rstrip(". ")]
            if near:
                return None, f"which does not exist as spelled; GitHub would not find '{part}' (the file is '{near[0]}')"
            return None, "which does not exist"
        cur = os.path.join(cur, part)
    return norm, None


def heading_anchors(text):
    """The anchors GitHub gives a Markdown file's "#" headings."""
    out, seen = set(), {}
    for line in rendered(text).splitlines():
        m = re.match(r" {0,3}#{1,6}[ \t]+(.*?)(?:[ \t]+#+)?[ \t]*$", line)
        if not m:
            continue
        h = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", m.group(1))
        s = re.sub(r"[^\w\- ]", "", h.strip().lower()).replace(" ", "-")
        k = seen.get(s, 0)
        seen[s] = k + 1
        out.add(s if k == 0 else f"{s}-{k}")
    return out


def tracked_files(root):
    """In a repository, the paths in its index: what a commit here would hold."""
    out = git(root, "ls-files", "-z", "--cached")
    return {p for p in out.decode("utf-8", "replace").split("\0") if p}


def link_targets(text):
    """(position, target) for every inline link, badge link and link definition."""
    seen, out = set(), []
    # Each pattern's target is in an angle-bracket group or a plain one.
    for rx, angle, plain in ((LINK, 1, 2), (LINK_NESTED, 1, 2), (LINK_DEFINITION, 2, 3)):
        for m in rx.finditer(text):
            target = m.group(angle) or m.group(plain)
            if (m.start(), target) not in seen:
                seen.add((m.start(), target))
                out.append((m.start(), target))
    return sorted(out)


def check_links(root):
    bad, n = [], 0
    anchors = {}
    tracked = tracked_files(root) if is_repository(root) else None
    for rel in md_files(root):
        text = uncoded(read(root, rel))
        for pos, target in link_targets(text):
            if re.match(r"[A-Za-z][A-Za-z0-9+.-]*:", target):
                continue  # a scheme: https:, mailto:
            n += 1
            where = f"{rel}:{line_of(text, pos)}"
            path, _, frag = target.partition("#")
            if path:
                dest, why = resolve_path(root, posixpath.dirname(rel), unquote(path))
                if not why and tracked is not None and dest and not (
                        dest in tracked or any(t.startswith(dest + "/") for t in tracked)):
                    why = "which is not in the index: git add it, or the link dangles in the commit"
                if why:
                    bad.append(f"{where}: link to {target}, {why}")
                    continue
            else:
                dest = rel
            if frag and dest.endswith(".md"):
                if dest not in anchors:
                    anchors[dest] = heading_anchors(read(root, dest))
                if unquote(frag) not in anchors[dest]:
                    bad.append(f"{where}: link to {target}: {dest} has no heading whose anchor is "
                               f"#{frag} (GitHub's anchors are lower case)")
    return bad, f"{n} relative links read"


def _label(s):
    return re.sub(r"\s+", " ", s).strip().lower()


def citation_matches(raw):
    """(match, group) for every bracketed citation in a Markdown text, wrapped
    or not, its code blanked. Bracketed text is a citation unless it is a
    link's text, a label a link definition in the same text defines (a
    reference link), a checklist box or a footnote; an escaped bracket
    renders as a bracket, so it is read too."""
    defined = {_label(m.group(1)) for m in LINK_DEFINITION.finditer(raw)}
    text = uncoded(raw)
    # A link definition ("[label]: target") is a link, not a citation, and so
    # is a footnote's label. The text after a footnote's label, and any line
    # that only looks like a definition, are read.
    text = FOOTNOTE_LABEL.sub(_blank, LINK_DEFINITION.sub(_blank, text))
    for m in BRACKET.finditer(text):
        if text[m.end():m.end() + 1] == "(":
            continue  # a link's text; its target is check 1's
        label = _label(m.group(1))
        if label in defined:
            continue  # a reference link's text or label
        if text[m.end():m.end() + 1] == "[":
            nxt = BRACKET.match(text, m.end())
            if nxt and (_label(nxt.group(1)) in defined or (not nxt.group(1).strip() and label in defined)):
                continue  # a reference link's text, its label defined here
        g = re.sub(r"\s+", " ", m.group(1)).strip()
        if g in ("", "x", "X") or g.startswith("^"):
            continue  # a checklist box, or a footnote
        yield m, g, text


def citation_groups(root, rel):
    """(line, group) for every bracketed citation in a file."""
    for m, g, text in citation_matches(read(root, rel)):
        yield line_of(text, m.start()), g


def archive_pins(root):
    bad = []
    for rel, want in ARCHIVE_SHA256.items():
        p = os.path.join(root, rel)
        if not os.path.exists(p):
            bad.append(f"{rel}: a pinned record is gone")
            continue
        with open(p, "rb") as f:
            got = hashlib.sha256(f.read()).hexdigest()
        if got != want:
            bad.append(f"{rel}: its bytes are not the record's (sha256 {got[:12]}…, pinned "
                       f"{want[:12]}…); an archived ledger never changes")
    for n, zs in ARCHIVES.items():
        for z in zs:
            if f"archive/{z}" not in ARCHIVE_SHA256:
                bad.append(f"archive/{z}: round {n}'s ledger, read by citations, has no pin")
    return bad


def check_citations(root):
    bad, n = archive_pins(root), 0
    records = {}
    files = ["METHOD.md"] + [f for f in md_files(root) if f.startswith("templates/")]
    for rel in files:
        for i, group in citation_groups(root, rel):
            items = [p.strip() for p in re.split(r"[;,]", group)]
            m = re.fullmatch(r"CASE-STUDY(?:-(\d+))?(?:\.md)?", items[0])
            if m:
                cs, items = int(m.group(1) or 1), items[1:]
            elif rel == "METHOD.md":
                cs = METHOD_DEFAULT_ROUND
            elif CITES.search(group):
                bad.append(f"{rel}:{i}: [{group}] names no case study; a citation in a template "
                           f"starts with CASE-STUDY-n")
                continue
            else:
                continue  # a template's placeholder
            if not items:
                bad.append(f"{rel}:{i}: [{group}] names a case study and nothing in it")
                continue
            if not os.path.exists(os.path.join(root, case_study_file(cs))):
                bad.append(f"{rel}:{i}: [{group}] cites case study {cs}, which does not exist")
                continue
            rec = records.setdefault(cs, record_of(root, cs))
            for p in items:
                n += 1
                why = resolve_item(p, cs, rec)
                if why:
                    bad.append(f"{rel}:{i}: [{group}]: {why}")
    return bad, f"{n} cited items read, {len(ARCHIVE_SHA256)} archived ledgers' pins checked"


def proposals(root, n):
    lines = read(root, case_study_file(n)).splitlines()
    start = next((i for i, l in enumerate(lines)
                  if l.startswith("## What METHOD.md should say differently")), None)
    if start is None:
        return None
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
    out = []
    for i in range(start + 1, end):
        line, prev = lines[i], lines[i - 1]
        if re.match(r"- \*\*", line):
            out.append(i + 1)
        elif (line.startswith("**") and prev.strip() == ""
              and not re.fullmatch(r"\*\*[^*]+\*\*\s*", line)):
            out.append(i + 1)  # a proposal written as a bold paragraph (case study 3's last)
    return out


def adoption_rows(root):
    path = os.path.join(root, "ADOPTION.md")
    if not os.path.exists(path):
        return None
    rows = []
    for i, line in enumerate(read(root, "ADOPTION.md").splitlines(), 1):
        if line.startswith("|") and not re.match(r"^\|\s*-", line):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            rows.append((i, cells))
    return rows


def check_proposals(root):
    bad = []
    derived = []
    for n, want in EXPECTED_PROPOSALS.items():
        found = proposals(root, n)
        if found is None:
            bad.append(f"case study {n} has no list 'What METHOD.md should say differently'")
            continue
        if len(found) != want:
            bad.append(f"case study {n}'s list parses to {len(found)} proposals; {want} are declared")
        derived += [f"CS{n}#{k}" for k in range(1, len(found) + 1)]
    rows = adoption_rows(root)
    if rows is None:
        return bad + ["ADOPTION.md does not exist"], "no ADOPTION.md"
    declared = derived + OTHER_IDS
    seen = {}
    for i, cells in rows:
        if re.fullmatch(r"CS\d+#\d+|[A-Z]\d+", cells[0]):
            seen.setdefault(cells[0], []).append(i)
    for pid in declared:
        if pid not in seen:
            bad.append(f"ADOPTION.md has no row for {pid}")
        elif len(seen[pid]) > 1:
            bad.append(f"ADOPTION.md has {len(seen[pid])} rows for {pid} (lines {seen[pid]})")
    for pid, where in seen.items():
        if pid not in declared:
            bad.append(f"ADOPTION.md line {where[0]}: {pid} is no proposal in any case study, "
                       f"and no id OTHER_IDS declares")
    return bad, f"{len(derived)} proposals derived and {len(OTHER_IDS)} other ids declared, {len(seen)} ids in ADOPTION.md"


def method_headings(root):
    return {l.lstrip("#").strip() for l in rendered(read(root, "METHOD.md")).splitlines()
            if re.match(r"#{2,3} ", l)}


def check_anchors(root):
    return anchors(root, foreign=True)


def anchors(root, foreign):
    """Check 4. foreign=False skips only the check that each FOREIGN_COMMITS
    entry is still named, for the controls' scratch repositories, which name
    none of them."""
    rows = adoption_rows(root)
    if rows is None:
        return ["ADOPTION.md does not exist"], "no ADOPTION.md"
    header = next((c for _, c in rows if "status" in [x.lower() for x in c]), None)
    if header is None:
        return ["ADOPTION.md has no table with a 'status' column"], "no table"
    lower = [x.lower() for x in header]
    if "method heading" not in lower or "evidence" not in lower:
        return ["ADOPTION.md's table has no 'METHOD heading' or no 'evidence' column"], "no table"
    si, hi, ei = lower.index("status"), lower.index("method heading"), lower.index("evidence")
    heads = method_headings(root)
    bad, n, refs = [], 0, 0
    for i, cells in rows:
        if cells is header or len(cells) <= max(si, hi, ei):
            continue
        if cells[si].lower().startswith("adopted"):
            n += 1
            # A rule split across sections names each heading, separated by " ; ".
            for h in [x.strip() for x in cells[hi].split(" ; ")]:
                if h not in heads:
                    bad.append(f"ADOPTION.md line {i}: {cells[0]} is {cells[si]} at "
                               f"'{h}', which is no heading in METHOD.md")
    # Lines move, so a line number is only true at a commit, and names one: in
    # every cell of every row, and every line of prose, of ADOPTION.md, and of
    # the files that change round to round, METHOD.md, README.md and the
    # templates (outside their code, which shows forms). The case studies and
    # the archive are records that do not change, so theirs cannot go stale.
    text = read(root, "ADOPTION.md")
    refs, beside = 0, set()
    named_in = {sha: "ADOPTION.md" for sha in COMMIT_REF.findall(text)}
    files = ["ADOPTION.md", "METHOD.md", "README.md"] + [f for f in md_files(root) if f.startswith("templates/")]
    for rel in files:
        if not os.path.exists(os.path.join(root, rel)):
            continue
        raw = read(root, rel)
        seen = raw.splitlines() if rel == "ADOPTION.md" else uncoded(raw).splitlines()
        for i, (line, shown) in enumerate(zip(raw.splitlines(), seen), 1):
            cells = (zip(line.strip().strip("|").split("|"), shown.strip().strip("|").split("|"))
                     if line.startswith("|") and shown.count("|") == line.count("|") else [(line, shown)])
            for part, shown_part in cells:
                found = LINE_REF.findall(shown_part)
                refs += len(found)
                if found:
                    shas = COMMIT_REF.findall(part)
                    beside |= set(shas)
                    for sha in shas:
                        named_in.setdefault(sha, rel)
                    if not shas:
                        bad.append(f"{rel} line {i}: {found[0]} without the commit it is counted at")
    # Every commit ADOPTION.md writes, whatever word precedes it, and every
    # commit beside a line number elsewhere, is this repository's own, in what
    # main will carry, or another repository's pin that FOREIGN_COMMITS declares.
    commits = set(COMMIT_REF.findall(text)) | beside
    if foreign:
        for sha in sorted(set(FOREIGN_COMMITS) - commits):
            bad.append(f"FOREIGN_COMMITS declares {sha}, which nothing check 4 reads names any longer; "
                       f"remove it")
    own = sorted(commits - set(FOREIGN_COMMITS))
    if is_repository(root):
        for sha in own:
            r = subprocess.run(["git", "-C", root, "merge-base", "--is-ancestor", sha, "HEAD"],
                               capture_output=True, env=dict(os.environ, GIT_OPTIONAL_LOCKS="0"))
            if r.returncode != 0:
                bad.append(f"{named_in.get(sha, 'ADOPTION.md')} names commit {sha}, which is not in HEAD's history")
        note = f"{len(own)} commits looked up in HEAD's history"
    else:
        note = "commits not looked up: no .git here"
    return bad, f"{n} adopted rows and {refs} line numbers read; {note}"


def check_refs(root):
    sections = {int(m.group(1)) for m in re.finditer(r"(?m)^## (\d+)\. ", read(root, "METHOD.md"))}
    bad, n = [], 0
    files = ["METHOD.md", "README.md", "ADOPTION.md"] + [f for f in md_files(root) if f.startswith("templates/")]
    for rel in files:
        if not os.path.exists(os.path.join(root, rel)):
            continue
        raw = read(root, rel)
        text = uncoded(raw)
        # A section mark in a citation that check 2 reads is the case study's,
        # and check 2's. Check 2 reads METHOD.md and the templates only.
        if rel == "METHOD.md" or rel.startswith("templates/"):
            chars = list(text)
            for m, _, _ in citation_matches(raw):
                for k in range(m.start(), m.end()):
                    if chars[k] != "\n":
                        chars[k] = " "
            text = "".join(chars)
        for m in SECTION_REF.finditer(text):
            if m.group(1):
                nums = [m.group(1)] + re.findall(r"\d+", m.group(2) or "")
            else:
                nums = [m.group(3)] + re.findall(r"\d+", m.group(4) or "")
            for k in nums:
                n += 1
                if int(k) not in sections:
                    bad.append(f"{rel}:{line_of(text, m.start())}: '{squash(m.group(0))}' names "
                               f"section {k}, which METHOD.md does not have; another document's "
                               f"section is cited as check 2 reads it, [CASE-STUDY-n, §k]")
    return bad, f"{n} section numbers read"


def check_readme(root):
    # A link in code is not a link.
    readme = uncoded(rendered(read(root, "README.md")))
    want = [f for f in md_files(root) if re.fullmatch(r"CASE-STUDY(-\d+)?\.md", f)]
    want += [f for f in md_files(root) if f.startswith("templates/") and f != "templates/README.md"]
    bad = [f"README.md does not link {f}" for f in want if f"]({f})" not in readme]
    return bad, f"{len(want)} files the README must list"


def check_brieferr(root):
    text = rendered(read(root, "templates/brief.md"))
    m = re.search(r"(?ms)^## Report\s*$(.*?)(?=^## |\Z)", text)
    if not m:
        return ["templates/brief.md has no '## Report' section"], "no report section"
    if "got wrong" not in m.group(1).lower():
        return ["templates/brief.md's report section no longer asks what the brief got wrong"], "read"
    return [], "the report section read"


def squash(s):
    return re.sub(r"\s+", " ", s).strip()


def plain(s):
    """Words as a reader takes them: whitespace squashed and emphasis markers gone."""
    return squash(re.sub(r"[*_]", "", s))


def check_sections(root):
    found = [l[3:].strip() for l in rendered(read(root, "METHOD.md")).splitlines()
             if re.match(r"## \d+\. ", l)]
    if found == SECTIONS:
        return [], f"{len(found)} sections read"
    return [f"METHOD.md's numbered sections are {found}; they must stay {SECTIONS}"], "read"


def check_quoted(root):
    bad, texts = [], {}

    def both(rel):
        if rel not in texts:
            raw = read(root, rel)
            texts[rel] = (raw, rendered(raw))
        return texts[rel]

    for rel, pattern, where in LOGANW_PATTERNS:
        raw, shown = both(rel)
        k, s = len(re.findall(pattern, raw, re.M)), len(re.findall(pattern, shown, re.M))
        if (k, s) != (1, 1):
            bad.append(f"{rel}: loganw.dev's pattern ({where}) matches {k} times as written and "
                       f"{s} as rendered, where it must match once in each: {pattern[:60]}…")
    for rel, passage in HF_PASSAGES:
        raw, shown = both(rel)
        k, s = squash(raw).count(squash(passage)), squash(shown).count(squash(passage))
        w = plain(shown).count(plain(passage))
        if (k, s, w) != (1, 1, 1):
            bad.append(f"{rel}: a passage HonestFramework quotes appears {k} times as written, "
                       f"{s} as rendered and {w} as words, where it must appear once in each: "
                       f"\"{passage[:60]}…\"")
    return bad, f"{len(LOGANW_PATTERNS)} loganw.dev patterns and {len(HF_PASSAGES)} HonestFramework passages read"


# ---- privacy ----

def address_ok(local, domain):
    return f"{local}@{domain}".lower() in ALLOWED_ADDRESSES or RESERVED.search(domain) is not None


def domain_key(domain):
    d = domain.lower()
    return d if d in _PUBLIC_KNOWN_DOMAINS else "sha256:" + hashlib.sha256(d.encode()).hexdigest()


def disallowed(text):
    """The disallowed addresses in a text, as domain keys: no address is ever printed."""
    return [domain_key(d) for l, d in EMAIL.findall(text) if not address_ok(l, d)]


def masked(keys):
    return sorted({k if not k.startswith("sha256:") else "a personal domain (" + k[7:19] + "…)"
                   for k in keys})


def decoded(text):
    """A text as a reader would see it: percent-escapes and HTML entities
    decoded, full-width and other compatibility forms folded (NFKC), and
    invisible format characters removed."""
    return _FORMAT_CHARS.sub("", unicodedata.normalize("NFKC", html.unescape(unquote(text))))


def personal_paths(text):
    """The spans of the personal paths in a text. A forward-slash shape is
    excused only where its token, the text since the last space or quote,
    begins as a URL with a host: https://github.com/users/<name> is a URL;
    file:///home/<name>, /var/home/<name> and PATH=/usr/bin:/home/<name> are
    paths."""
    out = []
    for m in USER_PATH.finditer(text):
        if m.group("slash") is not None:
            start = max(text.rfind(c, 0, m.start()) for c in " \t\n\"'<>()[]{}`") + 1
            if _URL_TOKEN.match(text, start) and start < m.start():
                continue
        out.append(m.span())
    return out


def findings(text):
    """(disallowed address keys, holds a personal path, holds a secret) for a text."""
    t = decoded(text)
    return disallowed(t), bool(personal_paths(t)), bool(SECRET.search(t))


def described(keys, path, secret):
    out = [f"{len(keys)} disallowed address(es): {masked(keys)}"] if keys else []
    out += ["an absolute personal path"] if path else []
    out += ["a secret-shaped token"] if secret else []
    return "; ".join(out)


def decode_text(data):
    """A file's text: UTF-8, or UTF-16 with or without its byte-order mark.
    None for anything else, which the check then fails by name."""
    if data[:2] in (b"\xff\xfe", b"\xfe\xff"):
        encodings = ["utf-16"]
    elif b"\x00" in data:
        # UTF-16 with no mark, in a Latin script: at least two in five of the
        # bytes on one side of each pair are zero, and almost none on the
        # other. Anything else with a zero byte is binary, and unreadable.
        half = max(1, len(data) // 2)
        odd, even = data[1::2].count(0), data[0::2].count(0)
        if max(odd, even) >= 0.4 * half and min(odd, even) <= 0.05 * half:
            encodings = ["utf-16-le" if odd > even else "utf-16-be"]
        else:
            encodings = []
    else:
        encodings = ["utf-8-sig"]
    for enc in encodings:
        try:
            text = data.decode(enc)
        except UnicodeDecodeError:
            continue
        if "\x00" not in text:
            return text
    return None


def gzip_header_texts(data):
    """The name and comment a gzip header may carry (RFC 1952, FNAME and FCOMMENT)."""
    out = []
    if len(data) < 10:
        return out
    flags, pos = data[3], 10
    if flags & 4 and len(data) >= pos + 2:  # FEXTRA comes first
        pos += 2 + int.from_bytes(data[pos:pos + 2], "little")
    for bit, label in ((8, "gzip name"), (16, "gzip comment")):
        if flags & bit:
            end = data.find(b"\0", pos)
            if end < 0:
                break
            out.append((label, data[pos:end].decode("latin-1")))
            pos = end + 1
    return out


def texts_in(name, data, depth=0):
    """(name, text) for every text in data, archives opened: a zip's members,
    its comment and each member's, and a gzip's content and its header's name
    and comment, to a depth of four. Text that cannot be read comes back as
    None."""
    if depth > 4:
        yield name, None
        return
    if data[:4] in (b"PK\x03\x04", b"PK\x05\x06"):
        try:
            with zipfile.ZipFile(io.BytesIO(data)) as zf:
                comment = zf.comment
                members = [(i.filename, i.comment, zf.read(i)) for i in zf.infolist() if not i.is_dir()]
        except (zipfile.BadZipFile, NotImplementedError, RuntimeError, OSError, EOFError):
            yield name, None  # broken, or encrypted
            return
        if comment:
            yield f"{name}!(archive comment)", comment.decode("utf-8", "replace")
        for member, member_comment, body in members:
            if member_comment:
                yield f"{name}!{member}!(comment)", member_comment.decode("utf-8", "replace")
            yield from texts_in(f"{name}!{member}", body, depth + 1)
        return
    if data[:2] == b"\x1f\x8b":
        for label, text in gzip_header_texts(data):
            yield f"{name}!({label})", text
        try:
            inner = gzip.decompress(data)
        except (OSError, EOFError):
            yield name, None
            return
        yield from texts_in(name + "!(gunzipped)", inner, depth + 1)
        return
    yield name, decode_text(data)


def object_problems(label, rel, data):
    """Everything wrong with one file or blob: its name, its text, and each
    archive member's name and text. rel is the path its known exceptions name."""
    bad = []
    keys, path, secret = findings(rel)
    if keys or path or secret:
        bad.append(f"{label}: its name holds {described(keys, path, secret)}")
    conceded = rel in KNOWN_PATHS and hashlib.sha256(data).hexdigest() == ARCHIVE_SHA256.get(rel)
    counts, with_paths = {}, 0
    for name, text in texts_in(rel, data):
        member = name.split("!", 1)[1] if "!" in name else None
        where = f"{label}!{member}" if member else label
        if member:
            k, p, s = findings(member)
            if k or p or s:
                bad.append(f"{where}: its name holds {described(k, p, s)}")
        if text is None:
            bad.append(f"{where}: cannot be read as text or as an archive")
            continue
        keys, path, secret = findings(text)
        if member:
            for k in keys:
                counts[(member, k)] = counts.get((member, k), 0) + 1
        elif keys:
            bad.append(f"{where}: {len(keys)} disallowed address(es): {masked(keys)}")
        if path:
            if conceded:
                with_paths += 1
            else:
                bad.append(f"{where}: holds an absolute personal path")
        if secret:
            bad.append(f"{where}: holds a secret-shaped token")
    known = KNOWN_PRIVACY.get(rel, {}).get("counts", {})
    for key, c in counts.items():
        if c != known.get(key, 0):
            bad.append(f"{label}!{key[0]}: {c} disallowed address(es) at "
                       f"{masked([key[1]])[0]}, where {known.get(key, 0)} are known")
    for key in known:
        if key not in counts:
            bad.append(f"{label}: its known exception for {key[0]} no longer holds; remove or update it")
    if conceded and not with_paths:
        bad.append(f"{label}: no member holds a personal path, so its place in KNOWN_PATHS no "
                   f"longer holds; remove it")
    return bad


def published_files(root):
    """The files a commit here would publish: in a repository, git's own list
    (tracked, and untracked but not ignored); elsewhere, every file."""
    if is_repository(root):
        out = git(root, "ls-files", "-z", "--cached", "--others", "--exclude-standard")
        return sorted({p for p in out.decode("utf-8", "replace").split("\0") if p})
    out = []
    for d, dirs, files in os.walk(root):
        dirs[:] = [x for x in dirs if x != ".git"]
        for f in files:
            if f != ".git":  # a worktree's pointer to its repository, not a published file
                out.append(os.path.relpath(os.path.join(d, f), root).replace(os.sep, "/"))
    return sorted(out)


def git_blob_id(data):
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def stored_blobs(root, skip):
    """(path, where, id, bytes) for every blob the index stages or HEAD's
    history holds, whose id is not in skip, each under the first path git
    names it by: what a commit or a push from here could publish."""
    named = {}
    # The index first: what is staged is what the next commit holds, whatever
    # the working tree now says.
    for rec in git(root, "ls-files", "-s", "-z").decode("utf-8", "replace").split("\0"):
        meta, _, path = rec.partition("\t")
        if path and len(meta.split()) == 3:
            named.setdefault(meta.split()[1], (path, "in the index"))
    for line in git(root, "rev-list", "--objects", "HEAD").decode("utf-8", "replace").splitlines():
        oid, _, path = line.partition(" ")
        if path:
            named.setdefault(oid, (path, "in history"))
    if not named:
        return []
    kinds = git(root, "cat-file", "--batch-check", data=("\n".join(named) + "\n").encode()).decode()
    blobs = [l.split()[0] for l in kinds.splitlines()
             if len(l.split()) >= 2 and l.split()[1] == "blob" and l.split()[0] not in skip]
    if not blobs:
        return []
    out = git(root, "cat-file", "--batch", data=("\n".join(blobs) + "\n").encode())
    res, pos = [], 0
    for oid in blobs:
        nl = out.index(b"\n", pos)
        size = int(out[pos:nl].split()[2])
        path, where = named[oid]
        res.append((path, where, oid, out[nl + 1:nl + 1 + size]))
        pos = nl + 1 + size + 1
    return res


def check_privacy(root):
    return privacy(root, exceptions=True)


def privacy(root, exceptions):
    """Check 10. exceptions=False skips only the check that each known
    exception's file still exists, for the controls' scratch repositories,
    which hold none of them."""
    bad, nfiles, seen = [], 0, set()
    repo = is_repository(root)
    for rel in published_files(root):
        try:
            with open(os.path.join(root, rel), "rb") as f:
                data = f.read()
        except FileNotFoundError:
            continue  # tracked but deleted here: its committed bytes are read with the history
        nfiles += 1
        seen.add(git_blob_id(data))
        bad += object_problems(rel, rel, data)
    for rel in sorted(set(KNOWN_PRIVACY) | set(KNOWN_PATHS)) if exceptions else []:
        if not os.path.exists(os.path.join(root, rel)):
            bad.append(f"{rel}: has a known exception but no longer exists; remove the exception")
    if not repo:
        return bad, f"{nfiles} files read; history and commit messages skipped by name: no .git here"
    try:
        blobs = stored_blobs(root, seen)
        log = git(root, "log", "--format=%B%x00", "HEAD").decode("utf-8", "replace")
    except (OSError, subprocess.CalledProcessError, ValueError, IndexError) as e:
        return bad + [f"the index or history could not be read: {e}"], f"{nfiles} files read"
    for path, where, oid, data in blobs:
        bad += object_problems(f"{path} ({where}, blob {oid[:7]})", path, data)
    keys, path, secret = findings(log)
    if keys or path or secret:
        bad.append(f"commit messages: {described(keys, path, secret)}")
    nmsg = log.count("\x00")
    return bad, (f"{nfiles} files, {len(blobs)} more blobs in the index and HEAD's history, and "
                 f"{nmsg} commit messages read")


CHECKS = [
    ("links", check_links),
    ("citations", check_citations),
    ("proposals", check_proposals),
    ("anchors", check_anchors),
    ("refs", check_refs),
    ("readme", check_readme),
    ("brieferr", check_brieferr),
    ("sections", check_sections),
    ("quoted", check_quoted),
    ("privacy", check_privacy),
]


def scrub(line):
    """A line of output with every personal path, disallowed address and
    secret-shaped token masked: what the gate refuses, it never prints, since
    its output is pasted into ledgers that will be published."""
    line = decoded(line)
    for a, b in reversed(personal_paths(line)):
        line = line[:a] + "<a personal path>" + line[b:]
    line = SECRET.sub("<a secret-shaped token>", line)
    return EMAIL.sub(lambda m: m.group(0) if address_ok(m.group(1), m.group(2)) else "<an address>", line)


def run(root, only=None, quiet=False):
    failed = 0
    for name, fn in CHECKS:
        if only and name != only:
            continue
        try:
            bad, ran = fn(root)
        except Exception as e:  # a check that crashes fails, by name
            bad, ran = [f"the check could not run: {type(e).__name__}: {e}"], "crashed"
        failed += bool(bad)
        if not quiet:
            print(f"{name:<10} {'FAIL' if bad else 'ok':<5} {ran}")
            for b in bad:
                print(f"           {scrub(b)}")
    return failed


# ---- the controls: planted faults, at least one per check, each must be caught ----

def edit(t, rel, fn):
    p = os.path.join(t, rel)
    with open(p, encoding="utf-8") as f:
        s = f.read()
    s2 = fn(s)
    if s2 == s:
        raise SystemExit(f"control could not plant its fault in {rel}")
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(s2)


def append(t, rel, s):
    with open(os.path.join(t, rel), "a", encoding="utf-8", newline="") as f:
        f.write(s)


def write_bytes(t, rel, b):
    with open(os.path.join(t, rel), "wb") as f:
        f.write(b)


def zipped(members):
    b = io.BytesIO()
    with zipfile.ZipFile(b, "w", zipfile.ZIP_DEFLATED) as z:
        for name, body in members:
            z.writestr(name, body)
    return b.getvalue()


# Built at run time, so this file holds none of them.
PLANTED_ADDRESS = "someone" + "@" + "personal-domain.net"
PLANTED_PATH = "C:" + _BS + "Us" + "ers" + _BS + "someone" + _BS + "work"
PLANTED_MOUNT_PATH = _SL + "mnt" + _SL + "c" + _SL + "Us" + "ers" + _SL + "someone" + _SL + "work"
PLANTED_DEEP_HOME = _SL + "var" + _SL + "ho" + "me" + _SL + "someone" + _SL + "work"
PLANTED_HIDDEN_ADDRESS = "some" + "​" + "one" + "@" + "personal-domain.net"


def plant_archive_member(t):
    # A record edited: one member added to an archived ledger, the zip still valid.
    with zipfile.ZipFile(os.path.join(t, "archive/round2-ledger.zip"), "a") as z:
        z.writestr("planted.md", "# 09:59 a planted entry\n")


def plant_archive_comment(t):
    b = io.BytesIO()
    with zipfile.ZipFile(b, "w") as z:
        z.writestr("notes.md", "# notes\n")
        z.comment = f"packed for {PLANTED_ADDRESS}".encode()
    write_bytes(t, "archive/planted.zip", b.getvalue())


PLANTS = [
    # (the check that must catch it, what is planted, how)
    ("links", "a link to no file", lambda t: append(t, "METHOD.md", "\n[a planted link](no-such-file.md)\n")),
    ("links", "a link whose case differs from the file's", lambda t: append(t, "METHOD.md", "\n[a planted link](adoption.md)\n")),
    ("links", "a link to an anchor no heading has", lambda t: append(t, "METHOD.md", "\n[a planted link](#no-such-heading)\n")),
    ("links", "a badge link whose outer target is missing", lambda t: append(t, "README.md", "\n[![badge](LICENSE)](no-such-file.md)\n")),
    ("links", "an angle-bracket target that is missing", lambda t: append(t, "METHOD.md", "\n[a planted link](<no such file.md>)\n")),
    ("links", "a definition, its target on the next line", lambda t: append(t, "README.md", "\n[planted]:\n  no-such-file.md\n")),
    ("citations", "an observation case study 3 does not number", lambda t: append(t, "METHOD.md", "\nA planted citation. [CASE-STUDY-3, obs 7]\n")),
    ("citations", "a wrapped citation of no case study", lambda t: append(t, "METHOD.md", "\nA planted citation. [CASE-STUDY-9, 10:00;\n11:00]\n")),
    ("citations", "a case study named another way", lambda t: append(t, "METHOD.md", "\nA planted citation. [CS3, 12:37]\n")),
    ("citations", "an escaped citation of no case study", lambda t: append(t, "METHOD.md", "\nA planted citation. \\[CASE-STUDY-9, 10:00]\n")),
    ("citations", "a citation after a bracket, no label defined", lambda t: append(t, "METHOD.md", "\nA planted citation. [see][CASE-STUDY-9, 10:00]\n")),
    ("citations", "a citation in a footnote's text", lambda t: append(t, "METHOD.md", "\n[^9]: A planted note. [CASE-STUDY-9, 10:00]\n")),
    ("citations", "a citation on a line shaped like a definition", lambda t: append(t, "METHOD.md", "\n[aside]: https://example.com [CASE-STUDY-9, 10:00]\n")),
    ("citations", "an archived ledger edited", plant_archive_member),
    ("proposals", "a case study's row removed", lambda t: edit(t, "ADOPTION.md", lambda s: re.sub(r"(?m)^\| CS3#1 \|.*\n", "", s, count=1))),
    ("proposals", "a B row removed", lambda t: edit(t, "ADOPTION.md", lambda s: re.sub(r"(?m)^\| B9 \|.*\n", "", s, count=1))),
    ("anchors", "an adopted row under no heading", lambda t: edit(t, "ADOPTION.md", lambda s: re.sub(
        r"(?m)^(\| CS2#1 \|(?:[^|]*\|){4})[^|]*\|", r"\1 No such heading |", s, count=1))),
    ("anchors", "a line number with no commit", lambda t: edit(t, "ADOPTION.md", lambda s: s.replace("; both at `49a9266`", "", 1))),
    ("anchors", "a line number in prose with no commit", lambda t: append(t, "ADOPTION.md", "\nThe planted rule is at METHOD.md:66.\n")),
    # A pin declared that nothing names: declared in-process, so the control stays
    # live wherever the real pins are cited, and undone after.
    ("anchors", "a declared pin nothing names", lambda t: FOREIGN_COMMITS.update({"fffffff": "planted"}),
     lambda: FOREIGN_COMMITS.pop("fffffff", None)),
    ("anchors", "a line number in a template with no commit", lambda t: append(t, "templates/brief.md", "\nThe planted rule is at METHOD.md:241.\n")),
    ("refs", "a wrapped section reference", lambda t: edit(t, "templates/brief.md", lambda s: s.replace("[METHOD.md](../METHOD.md)\n§3", "[METHOD.md](../METHOD.md)\n§9", 1))),
    ("refs", "a bare section sign", lambda t: append(t, "templates/verifier.md", "\nThe planted rule (§9) applies here.\n")),
    ("refs", "section signs in a list joined by 'and'", lambda t: append(t, "templates/verifier.md", "\nSee §§4 and 9.\n")),
    ("refs", "a bracketed section mark in README", lambda t: append(t, "README.md", "\nSee [§9].\n")),
    ("readme", "a case study's row removed", lambda t: edit(t, "README.md", lambda s: re.sub(r"(?m)^.*\]\(CASE-STUDY-5\.md\).*\n", "", s, count=1))),
    ("readme", "a case study's link inside a code span", lambda t: edit(t, "README.md", lambda s: re.sub(
        r"(\[[^\]\n]*\]\(CASE-STUDY-5\.md\))", r"`\1`", s, count=1))),
    ("brieferr", "the clause respelled", lambda t: edit(t, "templates/brief.md", lambda s: s.replace("got wrong", "got right"))),
    ("sections", "a section renamed", lambda t: edit(t, "METHOD.md", lambda s: s.replace("## 4. The ledger", "## 4. The record", 1))),
    # Rewrap a passage loganw.dev reads with literal spaces: its pattern stops matching.
    ("quoted", "a passage HonestFramework quotes, copied without its bold", lambda t: edit(t, "METHOD.md", lambda s: s + "\nA gate that cannot fail is not a gate.\n")),
    ("quoted", "a passage rewrapped", lambda t: edit(t, "README.md", lambda s: s.replace("Two agents\non a two-way split", "Two\nagents on a two-way split", 1))),
    ("quoted", "a passage kept only in an HTML comment", lambda t: edit(t, "METHOD.md", lambda s: s.replace(
        "**Exactly one file owns each shared fact; everyone else includes it.**",
        "<!-- **Exactly one file owns each shared fact; everyone else includes it.** -->", 1))),
    ("quoted", "loganw.dev's relations.json passage changed", lambda t: edit(t, "CASE-STUDY-4.md", lambda s: s.replace(
        "P2 moves atlas-film", "P2 moved atlas-film", 1))),
    ("privacy", "an address in a file", lambda t: append(t, "README.md", f"\nContact {PLANTED_ADDRESS} for details.\n")),
    ("privacy", "a percent-encoded address", lambda t: append(t, "README.md", "\n[Write](mailto:" + PLANTED_ADDRESS.replace("@", "%40") + ").\n")),
    ("privacy", "an address split by an invisible character", lambda t: append(t, "README.md", f"\nContact {PLANTED_HIDDEN_ADDRESS}.\n")),
    ("privacy", "a personal path behind a mount prefix", lambda t: append(t, "ADOPTION.md", f"\nRead at {PLANTED_MOUNT_PATH}.\n")),
    ("privacy", "a home after another path segment", lambda t: append(t, "ADOPTION.md", f"\nRead at {PLANTED_DEEP_HOME}.\n")),
    ("privacy", "an address in a nested archive", lambda t: write_bytes(t, "archive/planted.zip", zipped(
        [("inner.zip", zipped([("lead.md", f"# lead\n\nwrite to {PLANTED_ADDRESS}\n")]))]))),
    ("privacy", "an address in an archive's comment", plant_archive_comment),
    ("privacy", "a file that is not UTF-8", lambda t: write_bytes(t, "planted.txt", "Planted \u2013 notes\n".encode("cp1252"))),
]


def _rmtree(path):
    def retry(func, p, *_):
        os.chmod(p, stat.S_IWRITE)  # git's objects are read-only on Windows
        func(p)
    if sys.version_info >= (3, 12):
        shutil.rmtree(path, onexc=retry)
    else:
        shutil.rmtree(path, onerror=retry)


def git_plant_message_address(g, repo):
    g("commit", "-q", "--allow-empty", "-m", f"A planted message to {PLANTED_ADDRESS}")


def git_plant_message_path(g, repo):
    g("commit", "-q", "--allow-empty", "-m", f"A planted message: built in {PLANTED_PATH}")


def git_plant_history_blob(g, repo):
    # Committed, then removed: only the history holds it.
    with open(os.path.join(repo, "notes.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write(f"# notes\n\nwrite to {PLANTED_ADDRESS}\n")
    g("add", "notes.md")
    g("commit", "-q", "-m", "Notes")
    g("rm", "-q", "notes.md")
    g("commit", "-q", "-m", "Notes removed")


def git_plant_index_only(g, repo):
    # Staged, then cleaned in the working tree only: the next commit holds it.
    path = os.path.join(repo, "notes.md")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(f"# notes\n\nwrite to {PLANTED_ADDRESS}\n")
    g("add", "notes.md")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("# notes\n")


def git_plant_link_untracked(g, repo):
    # The target exists here, but nothing staged it: in the commit, the link dangles.
    with open(os.path.join(repo, "notes.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("# notes\n")
    with open(os.path.join(repo, "README.md"), "a", encoding="utf-8", newline="\n") as f:
        f.write("\n[the notes](notes.md)\n")


def git_setup_adoption(g, repo):
    # A METHOD.md and an ADOPTION.md whose one line number names a commit of this repository.
    with open(os.path.join(repo, "METHOD.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("# The method\n\n## 1. A section\n\nA rule.\n")
    g("add", "METHOD.md")
    g("commit", "-q", "-m", "A method")
    sha = subprocess.run(["git", "-C", repo, "rev-parse", "--short", "HEAD"], capture_output=True,
                         text=True, check=True).stdout.strip()
    with open(os.path.join(repo, "ADOPTION.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("| id | proposal | type | status | evidence | METHOD heading | template | parcel |\n"
                "|---|---|---|---|---|---|---|---|\n"
                f"| X1 | a rule | t | pending | METHOD.md:5 at `{sha}` | — | — | — |\n")
    g("add", "ADOPTION.md")
    g("commit", "-q", "-m", "An adoption record")


def git_plant_foreign_commit(g, repo):
    # A line number counted at a commit that no history here holds.
    with open(os.path.join(repo, "ADOPTION.md"), "a", encoding="utf-8", newline="\n") as f:
        f.write("| X2 | a rule | t | pending | METHOD.md:5 at `0000000` | — | — | — |\n")


def git_plant_commit_spelled_otherwise(g, repo):
    # A status that names a commit with no "at" before it.
    with open(os.path.join(repo, "ADOPTION.md"), "a", encoding="utf-8", newline="\n") as f:
        f.write("| X3 | a rule | t | adopted in `0000000` | — | — | — | — |\n")


GIT_PLANTS = [
    # (the check, what is planted, how, any setup the clean baseline needs)
    ("privacy", "an address in a commit message", git_plant_message_address, None),
    ("privacy", "a personal path in a commit message", git_plant_message_path, None),
    ("privacy", "an address only history holds", git_plant_history_blob, None),
    ("privacy", "an address only the index holds", git_plant_index_only, None),
    ("links", "a link to a file not in the index", git_plant_link_untracked, None),
    ("anchors", "a commit not in HEAD's history", git_plant_foreign_commit, git_setup_adoption),
    ("anchors", "a commit written without 'at'", git_plant_commit_spelled_otherwise, git_setup_adoption),
]


def control_in_repository(plant, check="privacy", setup=None):
    """A check in a scratch repository with a clean commit, before and after
    the plant: 'caught', 'missed', 'refused', 'crash', or None without git.
    Check 10 runs without its known exceptions, which the scratch repository
    does not hold."""
    tmp = tempfile.mkdtemp(prefix="check_method-git-")
    env = dict(os.environ, GIT_AUTHOR_NAME="control", GIT_AUTHOR_EMAIL="control@example.com",
               GIT_COMMITTER_NAME="control", GIT_COMMITTER_EMAIL="control@example.com",
               GIT_CONFIG_NOSYSTEM="1", GIT_OPTIONAL_LOCKS="0")
    which = {"privacy": "privacy-in-repository", "anchors": "anchors-in-repository"}.get(check, check)

    def g(*a):
        subprocess.run(["git", "-C", tmp, *a], check=True, capture_output=True, env=env)
    try:
        subprocess.run(["git", "init", "-q", tmp], check=True, capture_output=True, env=env)
        with open(os.path.join(tmp, "README.md"), "w", encoding="utf-8", newline="\n") as f:
            f.write("# A scratch repository for the gate's controls\n")
        g("add", "README.md")
        g("commit", "-q", "-m", "A clean first commit")
        if setup:
            setup(g, tmp)
        if outcome(tmp, which) != "pass":
            return "refused"
        plant(g, tmp)
        return {"fail": "caught", "pass": "missed", "crash": "crash"}[outcome(tmp, which)]
    except (OSError, subprocess.CalledProcessError):
        return None
    finally:
        _rmtree(tmp)


def outcome(t, check):
    """'pass', 'fail' or 'crash': a control counts only a failure the check
    reports, never a crash, which proves nothing about the plant."""
    fn = {"privacy-in-repository": lambda r: privacy(r, exceptions=False),
          "anchors-in-repository": lambda r: anchors(r, foreign=False)}.get(check) or dict(CHECKS)[check]
    try:
        bad, _ = fn(t)
    except Exception:
        return "crash"
    return "fail" if bad else "pass"


def control(root):
    if run(root, quiet=True):
        print("CONTROL REFUSED: the tree fails before any fault is planted, so a caught plant proves nothing")
        return 1
    missed, total = 0, 0
    for check, what, plant, *undo in PLANTS:
        tmp = tempfile.mkdtemp(prefix="check_method-")
        try:
            t = os.path.join(tmp, "t")
            shutil.copytree(root, t, ignore=shutil.ignore_patterns(".git", "__pycache__"))
            before = outcome(t, check)
            if before != "pass":
                verdict = f"REFUSED: the copy's check gives '{before}' before the plant"
            else:
                plant(t)
                after = outcome(t, check)
                verdict = {"fail": "caught", "pass": "NOT CAUGHT: this check cannot fail this way",
                           "crash": "CRASHED: the plant broke the check rather than being caught"}[after]
        finally:
            for u in undo:  # a plant made in-process, not in the copy
                u()
            _rmtree(tmp)
        total += 1
        missed += verdict != "caught"
        print(f"control {check:<10} {what:<46} {verdict}")
    tmp = tempfile.mkdtemp(prefix="check_method-")
    try:
        t = os.path.join(tmp, "t")
        shutil.copytree(root, t, ignore=shutil.ignore_patterns(".git", "__pycache__"))
        # An address in a file's name, and a personal path in a link's target,
        # which check 1 would print as it refuses the link.
        write_bytes(t, f"archive/{PLANTED_ADDRESS}.md", b"# notes\n")
        append(t, "README.md", f"\n[a planted link]({PLANTED_MOUNT_PATH}.md)\n")
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            failed = run(t)
        shown = out.getvalue()
        masked_out = (failed and PLANTED_ADDRESS not in shown and PLANTED_MOUNT_PATH not in shown
                      and "<an address>" in shown and "<a personal path>" in shown)
    finally:
        _rmtree(tmp)
    total += 1
    missed += not masked_out
    print(f"control {'privacy':<10} {'its output, which masks what it refuses':<46} "
          f"{'caught, and masked' if masked_out else 'NOT MASKED: the output prints what it refuses'}")
    for check, what, plant, setup in GIT_PLANTS:
        r = control_in_repository(plant, check, setup)
        if r is None:
            print(f"control {check:<10} {what:<46} SKIPPED by name: git is not available here")
            continue
        total += 1
        missed += r != "caught"
        verdict = {"caught": "caught", "missed": "NOT CAUGHT: this check cannot fail this way",
                   "refused": "REFUSED: the scratch repository fails before the plant",
                   "crash": "CRASHED: the plant broke the check rather than being caught"}[r]
        print(f"control {check:<10} {what:<46} {verdict}")
    print(f"controls: {total - missed} of {total} caught")
    return 1 if missed else 0


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if "--control" in sys.argv[1:]:
        sys.exit(control(root))
    failed = run(root)
    print(f"{'FAIL' if failed else 'PASS'}: {len(CHECKS) - failed} of {len(CHECKS)} checks hold")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
