#!/usr/bin/env python3
"""ParcelRound's gate: does the method still hold together?

    python tools/check_method.py            every check; exit 1 if any fails
    python tools/check_method.py --control  plant one fault per check in a copy
                                            of the tree; each must be caught

It reads structure and citations, never what a rule says. A gate that reads a
rule's wording is a stated limit, not a guarantee (case study 4's proposals
for section 5). Checks 7 and 9 read text, and are such limits.

The checks, by name:
  links      1. every relative link in a Markdown file names a file that exists
  citations  2. every case-study citation in METHOD.md and templates/ resolves
                to its round's record: the case study's own text (its bracketed
                citations aside), or the round's ledger archived beside it
  proposals  3. every proposal in a case study's list "What METHOD.md should
                say differently" has exactly one row in ADOPTION.md
  anchors    4. every ADOPTION.md row whose status is adopted names METHOD.md
                headings that exist
  refs       5. every section of METHOD.md a template cites exists
  readme     6. README.md links every case study and every template
  brieferr   7. templates/brief.md's report section still asks what the brief
                got wrong
  sections   8. METHOD.md's eight sections keep their numbers and titles
  quoted     9. every passage another repository quotes still matches once:
                loganw.dev's own patterns, run as it runs them, and
                HonestFramework's quotations, word for word
  privacy   10. no email address, personal path or secret-shaped token in any
                file, archive member or commit message, but those allowed

There is no cache: each run reads everything again. Standard library only.

Citation forms (check 2) in METHOD.md and the templates:
  [CASE-STUDY-n, 15:09]   a time in case study n or its archived ledger; ranges
                          (12:00-12:30) and minute wildcards (08:2x) read too
  [12:37]                 a bare time is round 2's, in METHOD.md only
  [CASE-STUDY-n, §4]      a section mark in case study n
  [CASE-STUDY-n, obs 10]  a numbered observation, where the case study numbers
                          its observations (case studies 4 and 5)
  [The setting]           a heading or a bold-marked item of the case study
                          (such as "the card day"), by its opening words
  [CASE-STUDY-n, the ledger]  the round's archived ledger itself
  An incident recorded outside the case studies is cited as a Markdown link to
  its record, e.g. [round 6's survey, B3](archive/round6-practice-survey.md),
  which check 1 resolves.

What it cannot see (stated limits, each by the behaviour it concedes):
  - citations: a time resolves if the round's record holds that minute anywhere,
    so a citation of the right minute and the wrong event passes;
  - proposals: it holds ids, not the rows' content, so a wrong status passes;
  - anchors: it holds that the headings exist, not that the rule is under them;
  - brieferr: the clause kept where nothing asks it (negated, or moved within
    the report section) passes; a respelled clause fails it;
  - quoted: it holds the passages listed in QUOTED; a passage another
    repository starts to quote is held only once it is added there, and
    HonestFramework's quotations are held as words, not as line wrapping;
  - privacy: an address spelled out for a person to reassemble, written in
    look-alike letters, or a secret of a shape not in SECRET passes; the
    archived ledgers' personal paths pass by design (they are records);
  - links: an http(s) link is not fetched.
Each of these is on every verifier's list by name.
"""
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile

# Each case study's ledger, archived beside it. Round 1 kept none.
ARCHIVES = {
    2: ["round2-ledger.zip"],
    3: ["round3-ledger.zip"],
    4: ["round4-ledger.zip", "round4-second-ledger.zip"],
    5: ["round5-ledger.zip"],
}
# Declared once and checked (METHOD.md section 1, the second grade): the case
# studies are records, so their proposal lists never change. A parse that
# finds another count means the parser or a record changed, and either is a
# finding.
EXPECTED_PROPOSALS = {2: 35, 3: 18, 4: 23, 5: 13}
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
# refuses any count but one (its site/facts.py, prose()). They are its own
# patterns, copied verbatim, so a rewrap that would break them breaks this.
LOGANW_PATTERNS = [
    ("README.md", r"^(A method for splitting one body of work across several coding agents\s+at\s+once,\s+without the pieces failing to meet)\.", "site/pages/method.py"),
    ("README.md", r"^(A method for splitting one body of work across several coding agents at\s+once, without the pieces failing to meet)\.", "site/pages/work_parcelround.py"),
    ("README.md", r"^(A method for splitting one body of work across several coding agents\s+at\s+once)", "site/pages/home.py, thread_determinism.py"),
    ("README.md", r"## (Is this for you\?)", "site/pages/work_parcelround.py"),
    ("README.md", r"\*\*Don't\*\* (for a single task, for exploratory work where the split isn't\s+obvious yet, or where the pieces can't be tested separately)\.", "site/pages/work_parcelround.py"),
    ("README.md", r"(Two agents\s+on a two-way split is usually slower than doing it yourself, because\s+the brief costs more than the work)\.", "site/pages/work_parcelround.py"),
    ("README.md", r"\*\*(twelve corrections from five parcels — every single parcel\s+corrected its brief)\*\*", "site/pages/work_parcelround.py"),
    ("README.md", r'\*"(Report anything you found that this brief got wrong)\."\*', "site/pages/work_parcelround.py"),
    ("METHOD.md", r"## 1\. (The one failure mode)", "site/pages/work_parcelround.py"),
    ("METHOD.md", r"The failure is that (\*\*the work between the parcels belongs to\s+nobody\*\*, and it is invisible because every parcel's own gate is green)\.", "site/pages/work_parcelround.py"),
    ("METHOD.md", r"\*\*(Exactly one file owns each shared fact; everyone else includes it)\.\*\*", "site/pages/method.py"),
]
# HonestFramework quotes these as verbatim through unpinned links
# (WITH-PARCELROUND.md; METHOD.md section 9), re-wrapped in its own lines.
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
# Built from parts, so that this file holds no personal path of its own to find.
_SL = "/"
USER_PATH = re.compile(
    r"[A-Za-z]:[\\/]+Users[\\/]+[^\\/\s]+"
    + "|" + _SL + "c" + _SL + "Users" + _SL + r"[^/\s]+"
    + "|" + _SL + "home" + _SL + r"[^/\s]+"
    + "|" + _SL + "Users" + _SL + r"[^/\s]+")
# Common credential shapes, built from parts for the same reason.
SECRET = re.compile("|".join([
    "gh" + r"[pousr]_[A-Za-z0-9]{20,}",
    "github" + r"_pat_[A-Za-z0-9_]{20,}",
    "s" + r"k-[A-Za-z0-9_-]{20,}",
    "AK" + r"IA[0-9A-Z]{16}",
    "xo" + r"x[abprs]-[A-Za-z0-9-]{10,}",
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

STAMP = re.compile(r"(?<![\d:])(\d{1,2}):(\d[\dx])(?![\d:])")
LINK = re.compile(r"\[[^\]\n]*\]\(([^)\s]+)\)")
CITATION = re.compile(r"\[([^\]\n]+)\](?!\()")
LEDGER_PHRASE = re.compile(r"(?:the )?(?:round's |parcels' |lead's )?ledger(?: files?)?", re.I)


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


def norm_stamp(h, m):
    return f"{int(h):02d}:{m}"


def stamp_matches(cited, known):
    if len(cited) != len(known):
        return False
    return all(a == b or a == "x" or b == "x" for a, b in zip(cited, known))


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
        with zipfile.ZipFile(path) as zf:
            for name in zf.namelist():
                if not name.endswith(".md"):
                    continue
                body = zf.read(name).decode("utf-8", "replace")
                for line in body.splitlines():
                    if line.startswith("#"):
                        stamps |= {norm_stamp(h, m) for h, m in STAMP.findall(line)}
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


def resolve_item(item, n, rec):
    """None if the item resolves in round n's record, else the reason."""
    item = item.strip().lstrip("~").strip()
    if not item:
        return "an empty citation"
    found = [norm_stamp(h, m) for h, m in STAMP.findall(item)]
    if found:
        missing = [s for s in found if not any(stamp_matches(s, k) for k in rec["stamps"])]
        return f"no {', '.join(missing)} in round {n}'s record" if missing else None
    m = re.search(r"§\s*(\d+)", item)
    if m:
        k = m.group(1)
        ok = (f"**§{k}" in rec["text"] or any(f"§{k}" in h for h in rec["headings"]))
        return None if ok else f"no §{k} in case study {n}"
    m = re.fullmatch(r"obs(?:ervation)?\.?\s*(\d+)", item, re.I)
    if m:
        k = m.group(1)
        return None if k in rec["observations"] else f"no numbered observation {k} in case study {n}"
    phrase = re.sub(r"\s+", " ", item).lower()
    if any(h.startswith(phrase) for h in rec["headings"] + rec["bold"]):
        return None
    if LEDGER_PHRASE.fullmatch(phrase) and rec["archived"]:
        return None  # a citation of the round's archived ledger itself
    return f"'{item}' opens no heading or bold-marked item of case study {n}"


# ---- the checks: each returns (failures, a line that says what ran) ----

def check_links(root):
    bad, n = [], 0
    for rel in md_files(root):
        for target in LINK.findall(read(root, rel)):
            if re.match(r"(https?:|mailto:|#)", target):
                continue
            n += 1
            path = os.path.normpath(os.path.join(root, os.path.dirname(rel), target.split("#")[0]))
            if not os.path.exists(path):
                bad.append(f"{rel}: link to {target}, which does not exist")
    return bad, f"{n} relative links read"


def citation_groups(root, rel):
    for i, line in enumerate(read(root, rel).splitlines(), 1):
        # A code span shows a citation's form rather than citing: skip it.
        for g in CITATION.findall(re.sub(r"`[^`]*`", " ", line)):
            if g.strip() in ("", "x", " "):
                continue  # a checklist box
            yield i, g


def check_citations(root):
    bad, n = [], 0
    records = {}
    files = ["METHOD.md"] + [f for f in md_files(root) if f.startswith("templates/")]
    for rel in files:
        for i, group in citation_groups(root, rel):
            parts = [p.strip() for p in group.split(";")]
            m = re.match(r"CASE-STUDY(?:-(\d))?(?:\.md)?\s*,\s*(.*)", parts[0])
            if m:
                cs = int(m.group(1) or 1)
                parts[0] = m.group(2)
            elif rel == "METHOD.md":
                cs = METHOD_DEFAULT_ROUND
            else:
                # Templates hold placeholders such as [the post-mortem]; only an
                # explicit case-study citation is checked there.
                continue
            if not os.path.exists(os.path.join(root, case_study_file(cs))):
                bad.append(f"{rel}:{i}: [{group}] cites case study {cs}, which does not exist")
                continue
            rec = records.setdefault(cs, record_of(root, cs))
            for p in parts:
                n += 1
                why = resolve_item(p, cs, rec)
                if why:
                    bad.append(f"{rel}:{i}: [{group}]: {why}")
    return bad, f"{n} cited items read"


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
    seen = {}
    for i, cells in rows:
        if re.fullmatch(r"CS(\d)#(\d+)", cells[0]):
            seen.setdefault(cells[0], []).append(i)
    for pid in derived:
        if pid not in seen:
            bad.append(f"ADOPTION.md has no row for {pid}")
        elif len(seen[pid]) > 1:
            bad.append(f"ADOPTION.md has {len(seen[pid])} rows for {pid} (lines {seen[pid]})")
    for pid, where in seen.items():
        if pid not in derived:
            bad.append(f"ADOPTION.md line {where[0]}: {pid} is no proposal in any case study")
    return bad, f"{len(derived)} proposals derived, {len(seen)} ids in ADOPTION.md"


def method_headings(root):
    return {l.lstrip("#").strip() for l in read(root, "METHOD.md").splitlines()
            if re.match(r"#{2,3} ", l)}


def check_anchors(root):
    rows = adoption_rows(root)
    if rows is None:
        return ["ADOPTION.md does not exist"], "no ADOPTION.md"
    header = next((c for _, c in rows if "status" in [x.lower() for x in c]), None)
    if header is None:
        return ["ADOPTION.md has no table with a 'status' column"], "no table"
    lower = [x.lower() for x in header]
    si, hi = lower.index("status"), lower.index("method heading")
    heads = method_headings(root)
    bad, n = [], 0
    for i, cells in rows:
        if cells is header or len(cells) <= max(si, hi):
            continue
        if cells[si].lower().startswith("adopted"):
            n += 1
            # A rule split across sections names each heading, separated by " ; ".
            for h in [x.strip() for x in cells[hi].split(" ; ")]:
                if h not in heads:
                    bad.append(f"ADOPTION.md line {i}: {cells[0]} is {cells[si]} at "
                               f"'{h}', which is no heading in METHOD.md")
    return bad, f"{n} adopted rows read"


def check_refs(root):
    sections = {m.group(1) for m in re.finditer(r"(?m)^## (\d+)\. ", read(root, "METHOD.md"))}
    bad, n = [], 0
    # The templates' own spellings, across a line break: "[METHOD.md](../METHOD.md)
    # §3", "... section 4", "METHOD §6".
    pat = re.compile(r"METHOD(?:\.md)?(?:\]\([^)]*\))?\s*(?:§\s*|section\s+)(\d+)")
    for rel in [f for f in md_files(root) if f.startswith("templates/")]:
        text = read(root, rel)
        for m in pat.finditer(text):
            n += 1
            if m.group(1) not in sections:
                line = text.count("\n", 0, m.start()) + 1
                bad.append(f"{rel}:{line}: cites METHOD §{m.group(1)}, which METHOD.md does not have")
    return bad, f"{n} section references read"


def check_readme(root):
    readme = read(root, "README.md")
    want = [f for f in md_files(root) if re.fullmatch(r"CASE-STUDY(-\d)?\.md", f)]
    want += [f for f in md_files(root) if f.startswith("templates/") and f != "templates/README.md"]
    bad = [f"README.md does not link {f}" for f in want if f"]({f})" not in readme]
    return bad, f"{len(want)} files the README must list"


def check_brieferr(root):
    text = read(root, "templates/brief.md")
    m = re.search(r"(?ms)^## Report\s*$(.*?)(?=^## |\Z)", text)
    if not m:
        return ["templates/brief.md has no '## Report' section"], "no report section"
    if "got wrong" not in m.group(1).lower():
        return ["templates/brief.md's report section no longer asks what the brief got wrong"], "read"
    return [], "the report section read"


def squash(s):
    return re.sub(r"\s+", " ", s).strip()


def check_sections(root):
    found = [l[3:].strip() for l in read(root, "METHOD.md").splitlines() if re.match(r"## \d+\. ", l)]
    if found == SECTIONS:
        return [], f"{len(found)} sections read"
    return [f"METHOD.md's numbered sections are {found}; they must stay {SECTIONS}"], "read"


def check_quoted(root):
    bad = []
    for rel, pattern, where in LOGANW_PATTERNS:
        k = len(re.findall(pattern, read(root, rel), re.M))
        if k != 1:
            bad.append(f"{rel}: loganw.dev's pattern ({where}) matches {k} times, where it "
                       f"must match once: {pattern[:60]}…")
    for rel, passage in HF_PASSAGES:
        k = squash(read(root, rel)).count(squash(passage))
        if k != 1:
            bad.append(f"{rel}: a passage HonestFramework quotes appears {k} times, where it "
                       f"must appear once: \"{passage[:60]}…\"")
    return bad, f"{len(LOGANW_PATTERNS)} loganw.dev patterns and {len(HF_PASSAGES)} HonestFramework passages read"


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


def commit_message_problems(repo):
    try:
        log = subprocess.run(["git", "-C", repo, "log", "--format=%B"], capture_output=True,
                             text=True, encoding="utf-8", check=True).stdout
    except (OSError, subprocess.CalledProcessError) as e:
        return [f"commit messages could not be read: {e}"]
    out = []
    found = disallowed(log)
    if found:
        out.append(f"commit messages: {len(found)} disallowed address(es): {masked(found)}")
    if SECRET.search(log):
        out.append("commit messages: a secret-shaped token")
    return out


def check_privacy(root):
    bad, nfiles = [], 0
    for d, dirs, files in os.walk(root):
        dirs[:] = [x for x in dirs if x != ".git"]
        for f in files:
            if f == ".git":
                continue  # a worktree's pointer to its repository, not a published file
            p = os.path.join(d, f)
            rel = os.path.relpath(p, root).replace(os.sep, "/")
            nfiles += 1
            if f.endswith(".zip"):
                counts = {}
                with zipfile.ZipFile(p) as zf:
                    for name in zf.namelist():
                        body = zf.read(name).decode("utf-8", "replace")
                        for k in disallowed(body):
                            counts[(name, k)] = counts.get((name, k), 0) + 1
                        if SECRET.search(body):
                            bad.append(f"{rel}!{name}: a secret-shaped token")
                known = KNOWN_PRIVACY.get(rel, {}).get("counts", {})
                for key, c in counts.items():
                    if c != known.get(key, 0):
                        bad.append(f"{rel}!{key[0]}: {c} disallowed address(es) at "
                                   f"{masked([key[1]])[0]}, where {known.get(key, 0)} are known")
                for key, c in known.items():
                    if key not in counts:
                        bad.append(f"{rel}: its known exception for {key[0]} no longer holds; "
                                   f"remove or update it")
                continue  # the archived ledgers' personal paths are their records'
            try:
                with open(p, encoding="utf-8") as fh:
                    text = fh.read()
            except (UnicodeDecodeError, OSError):
                continue
            found = disallowed(text)
            if found:
                bad.append(f"{rel}: {len(found)} disallowed address(es): {masked(found)}")
            if USER_PATH.search(text):
                bad.append(f"{rel}: holds an absolute personal path")
            if SECRET.search(text):
                bad.append(f"{rel}: holds a secret-shaped token")
    for rel in KNOWN_PRIVACY:
        if not os.path.exists(os.path.join(root, rel)):
            bad.append(f"{rel}: has a known exception but no longer exists; remove the exception")
    # A repository's .git is a directory; a worktree's is a file naming its repository.
    if os.path.exists(os.path.join(root, ".git")):
        bad += commit_message_problems(root)
        note = "and every commit message"
    else:
        note = "commit messages skipped by name: no .git here"
    return bad, f"{nfiles} files read, {note}"


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


def run(root, only=None, quiet=False):
    failed = 0
    for name, fn in CHECKS:
        if only and name != only:
            continue
        bad, ran = fn(root)
        failed += bool(bad)
        if not quiet:
            print(f"{name:<10} {'FAIL' if bad else 'ok':<5} {ran}")
            for b in bad:
                print(f"           {b}")
    return failed


# ---- the controls: one planted fault per check, each must be caught ----

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
    with open(os.path.join(t, rel), "a", encoding="utf-8") as f:
        f.write(s)


def plant_links(t):
    append(t, "METHOD.md", "\n[a planted link](no-such-file.md)\n")


def plant_citations(t):
    append(t, "METHOD.md", "\nA planted citation. [CASE-STUDY-3, obs 7]\n")


def plant_proposals(t):
    edit(t, "ADOPTION.md", lambda s: re.sub(r"(?m)^\| CS3#1 \|.*\n", "", s, count=1))


def plant_anchors(t):
    edit(t, "ADOPTION.md", lambda s: re.sub(
        r"(?m)^(\| CS2#1 \|(?:[^|]*\|){4})[^|]*\|", r"\1 No such heading |", s, count=1))


def plant_refs(t):
    # A wrapped reference, the way brief.md writes them.
    edit(t, "templates/brief.md", lambda s: s.replace("[METHOD.md](../METHOD.md)\n§3", "[METHOD.md](../METHOD.md)\n§9", 1))


def plant_readme(t):
    edit(t, "README.md", lambda s: re.sub(r"(?m)^.*\]\(CASE-STUDY-5\.md\).*\n", "", s, count=1))


def plant_brieferr(t):
    edit(t, "templates/brief.md", lambda s: s.replace("got wrong", "got right"))


def plant_sections(t):
    edit(t, "METHOD.md", lambda s: s.replace("## 4. The ledger", "## 4. The record", 1))


def plant_quoted(t):
    # Rewrap a passage loganw.dev reads with literal spaces: its pattern stops matching.
    edit(t, "README.md", lambda s: s.replace("Two agents\non a two-way split", "Two\nagents on a two-way split", 1))


def plant_privacy(t):
    # A personal address assembled at run time, so this file never holds one.
    planted = "someone" + "@" + "personal-domain.net"
    append(t, "README.md", f"\nContact {planted} for details.\n")


PLANTS = {
    "links": plant_links, "citations": plant_citations, "proposals": plant_proposals,
    "anchors": plant_anchors, "refs": plant_refs, "readme": plant_readme,
    "brieferr": plant_brieferr, "sections": plant_sections, "quoted": plant_quoted,
    "privacy": plant_privacy,
}


def control_commit_messages():
    """The privacy check's commit-message branch, planted in a scratch repository."""
    tmp = tempfile.mkdtemp(prefix="check_method-git-")
    try:
        env = dict(os.environ, GIT_AUTHOR_NAME="control", GIT_AUTHOR_EMAIL="control@example.com",
                   GIT_COMMITTER_NAME="control", GIT_COMMITTER_EMAIL="control@example.com")
        planted = "someone" + "@" + "personal-domain.net"
        cmds = [["git", "init", "-q", tmp],
                ["git", "-C", tmp, "commit", "-q", "--allow-empty", "-m", f"a planted message to {planted}"]]
        for c in cmds:
            subprocess.run(c, check=True, capture_output=True, env=env)
        return bool(commit_message_problems(tmp))
    except (OSError, subprocess.CalledProcessError):
        return None
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def control(root):
    if run(root, quiet=True):
        print("CONTROL REFUSED: the tree fails before any fault is planted, so a caught plant proves nothing")
        return 1
    missed = 0
    for name, plant in PLANTS.items():
        tmp = tempfile.mkdtemp(prefix="check_method-")
        try:
            shutil.copytree(root, os.path.join(tmp, "t"), ignore=shutil.ignore_patterns(".git"))
            t = os.path.join(tmp, "t")
            plant(t)
            caught = run(t, only=name, quiet=True) > 0
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
        missed += not caught
        print(f"control {name:<16} {'caught' if caught else 'NOT CAUGHT: this check cannot fail'}")
    cm = control_commit_messages()
    if cm is None:
        print("control privacy/commits SKIPPED by name: git is not available here")
    else:
        missed += not cm
        print(f"control {'privacy/commits':<16} {'caught' if cm else 'NOT CAUGHT: this check cannot fail'}")
    total = len(PLANTS) + (cm is not None)
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
