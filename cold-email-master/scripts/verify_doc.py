#!/usr/bin/env python3
"""Mechanical verifier for cold-email-master frameworks docs and per-lead copy.

Doc mode (default):
    python3 verify_doc.py "Cold Email Frameworks — X v1.md" [--grades] [--legacy]

    Checks every framework/alternate example, follow-up, subject list and spin set,
    the two closers, and the v2 section skeleton, against references/copy-rules.md.
    --grades  also prints a Flesch-Kincaid grade table (for the plain-English editor).
    --legacy  skip v2-only structure checks (spin sets, Attack Plan, infra/weekly sections)
              so pre-v2 docs can be scanned for copy problems only.

Leads mode:
    python3 verify_doc.py --leads out.json [more.json] [--packets packets.json]
                          [--canonical canonical.txt] [--threshold 0.45]

    out.json shape: {"<lead_email>": {"<fw_key>": {"subject": "...", "body": "..."}}}
    fw_key: F1..F10 / A..C (framework emails), F1_FU.. (follow-ups), C1, C2 (closers).
    packets.json: {"<lead_email>": {"company": "...", "city": "..."}} for name stripping.
    canonical.txt: one regex per line for designated lines allowed to repeat across leads.
    Runs the per-touch rules plus the cross-lead similarity check (template-swap defect),
    vendored from Hermes generated-copy-qa/cross_lead_similarity_check.py (2026-09-06).

Doc directives (optional HTML comments anywhere in the doc):
    <!-- verify-allow: ai, leads -->      words removed from the banned list for this doc
    <!-- verify-ban: podcast, exposure --> words added to the banned list for this doc

Exit 0 and "PASS" when clean; exit 1 and "FAIL" with every problem otherwise.
"""
import argparse
import itertools
import json
import re
import sys

BANNED = [
    "price", "cost", "investment", "spend", "budget", "unlock", "10x", "synergy", "leverage",
    "innovative", "cutting-edge", "solution", "game-changer", "transform", "revolutionise",
    "revolutionize", "scale your", "disrupt", "guaranteed", "guarantee", "roi", "lead generation",
    "ai", "automation", "opportunity", "passive income", "furthermore", "moreover", "delve",
    "landscape", "robust", "awesome", "amazing", "excited", "honored", "honoured", "reach out",
    "touch base", "hope this finds", "wanted to reach out", "i'd love to", "hop on", "quick call",
    "risk-free", "no cost", "act now", "limited time", "realtor", "hvac",
]
SUBJECT_BANNED = ["free", "quick question", "touching base", "re:", "fwd:"]
ALLOWED_PLACEHOLDER_LINK = re.compile(r"\{[^{}]*(link|url|page)[^{}]*\}", re.I)
URL = re.compile(r"https?://|www\.", re.I)
SPIN = re.compile(r"\{\{\s*RANDOM\s*\|([^{}]*)\}\}", re.I)
WORD = re.compile(r"[A-Za-z0-9'’$%.]+")

V2_SECTIONS = {
    "ATTACK PLAN": r"ATTACK PLAN",
    "BEST PRACTICES": r"BEST PRACTICES",
    "AMMO BANK": r"AMMO BANK",
    "RESEARCH": r"#+ *RESEARCH",
    "OFFER BLOCK": r"OFFER BLOCK",
    "SELECTION LOGIC": r"SELECTION LOGIC",
    "CAMPAIGN STRUCTURE": r"CAMPAIGN STRUCTURE",
    "CLOSERS": r"CLOSERS",
    "WHEN THEY REPLY": r"WHEN THEY REPLY",
    "INFRASTRUCTURE": r"INFRASTRUCTURE",
    "WEEKLY RHYTHM": r"WEEKLY RHYTHM",
    "QC CHECKLIST": r"QC CHECKLIST",
}


# ---------- text helpers ----------

def render_spin(text):
    """Render Instantly spintax to its first option (for counting)."""
    return SPIN.sub(lambda m: m.group(1).split("|")[0].strip(), text)


def spin_options(text):
    return [o.strip() for m in SPIN.finditer(text) for o in m.group(1).split("|")]


def unquote(block):
    return re.sub(r"^> ?", "", block, flags=re.M).strip()


def words(text):
    t = render_spin(text)
    t = re.sub(r"\{[^{}]*\}", "X", t)  # a writer placeholder counts as one word
    return [w for w in WORD.findall(t) if re.search(r"[A-Za-z0-9]", w)]


def syllables(word):
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w:
        return 1  # numbers and symbols
    if len(w) <= 3:
        return 1
    w = re.sub(r"(?:[^laeiouy]es|ed|[^laeiouy]e)$", "", w)
    w = re.sub(r"^y", "", w)
    return max(1, len(re.findall(r"[aeiouy]{1,2}", w)))


def fk_grade(text):
    t = re.sub(r"\{[^{}]*\}", "X", render_spin(text))
    # greeting and sign-off lines are not prose
    lines = [l for l in t.splitlines() if l.strip()]
    if lines and re.match(r"^(hey|hi|hello|g'day|dear)\b", lines[0].strip(), re.I) and len(lines[0].split()) <= 4:
        lines = lines[1:]
    if lines and len(lines[-1].split()) <= 3 and not lines[-1].rstrip().endswith(("?", ".")):
        lines = lines[:-1]
    prose = " ".join(lines)
    ws = [w for w in WORD.findall(prose) if re.search(r"[A-Za-z]", w)]
    if len(ws) < 8:
        return 0.0
    sentences = max(1, len(re.findall(r"[.?]+(?:\s|$)", prose)))
    syl = sum(syllables(w) for w in ws)
    return round(0.39 * (len(ws) / sentences) + 11.8 * (syl / len(ws)) - 15.59, 1)


def banned_hits(text, banned):
    t = render_spin(text)
    t = re.sub(r"\{[^{}]*\}", " ", t)
    hits = []
    for b in banned:
        suffix = r"(?:s|es|ed|d|ing|ation)?" if len(b) > 3 else ""
        if re.search(r"(?<![A-Za-z])" + re.escape(b) + suffix + r"(?![A-Za-z])", t, re.I):
            hits.append(b)
    return hits


def link_count(text):
    return len(URL.findall(text)) + len(ALLOWED_PLACEHOLDER_LINK.findall(text))


# ---------- per-email checks ----------

def check_email(label, text, kind, banned, problems, notes, grades):
    """kind: framework | followup | closer1 | closer2"""
    variants = [text]
    if SPIN.search(text):
        # every spintax option must pass the character rules on its own
        for o in spin_options(text):
            for b in banned_hits(o, banned):
                problems.append(f"{label}: spin option '{o}' has banned '{b}'")
            if re.search("[–—!]", o):
                problems.append(f"{label}: spin option '{o}' has a dash or '!'")
    for t in variants:
        n = len(words(t))
        lo, hi = {"framework": (60, 100), "followup": (30, 50), "closer1": (1, 49), "closer2": (1, 99)}[kind]
        if not lo <= n <= hi:
            problems.append(f"{label}: {n} words (want {lo}-{hi})")
        for b in banned_hits(t, banned):
            if kind == "closer2" and b == "free":
                continue
            problems.append(f"{label}: banned word '{b}'")
        if re.search("[–—]", t):
            problems.append(f"{label}: em/en dash")
        if "!" in render_spin(t):
            problems.append(f"{label}: exclamation mark")
        links = link_count(t)
        if kind == "framework" and links:
            problems.append(f"{label}: link in a framework email")
        elif links > 1:
            problems.append(f"{label}: {links} links (max 1)")
        free = len(re.findall(r"(?<![A-Za-z])free(?![A-Za-z])", re.sub(r"\{[^{}]*\}", " ", render_spin(t)), re.I))
        if kind != "closer2" and free:
            problems.append(f"{label}: 'free' outside Closer 2 (use 'at no charge' / 'yours either way')")
        elif kind == "closer2" and free > 1:
            problems.append(f"{label}: 'free' {free} times (max 1, in Closer 2)")
        if kind == "followup":
            last = [l for l in render_spin(t).splitlines() if l.strip()]
            body_end = last[-1].strip() if last else ""
            if len(last) > 1 and len(body_end.split()) <= 3 and not body_end.endswith("?"):
                body_end = last[-2].strip()  # allow a name-only sign-off line
            if not body_end.endswith("?"):
                problems.append(f"{label}: follow-up does not end on a question")
            if body_end.count("?") > 1 or render_spin(t).count("?") > 2:
                notes.append(f"{label}: several questions; the rule is one, at the end")
        if kind == "framework" and re.search(r"(as I mentioned|my last (note|email)|following up)", t, re.I):
            problems.append(f"{label}: references another email (framework emails stand alone)")
        if re.search(r"\b(\w+), (\w+),? and (\w+)\b", render_spin(t)):
            notes.append(f"{label}: possible parallel triplet, read it aloud")
        g = fk_grade(t)
        grades.append((label, n, g))
        if g > 7:
            problems.append(f"{label}: reading grade {g} (ceiling 7, target 5)")
        elif g > 5:
            notes.append(f"{label}: reading grade {g} (target 5)")


def check_subjects(label, line, problems):
    subs = re.findall(r"`([^`]+)`", line)
    if len(subs) < 3:
        problems.append(f"{label}: {len(subs)} subject options (want 3+)")
    for s in subs:
        s_r = render_spin(s)
        if s_r != s_r.lower():
            problems.append(f"{label}: subject '{s}' not lowercase")
        if not 1 <= len(s_r.split()) <= 4:
            problems.append(f"{label}: subject '{s}' is {len(s_r.split())} words (want 1-4)")
        if re.search("[–—!]", s_r):
            problems.append(f"{label}: subject '{s}' has a dash or '!'")
        for b in SUBJECT_BANNED:
            if re.search(r"(?<![A-Za-z])" + re.escape(b) + r"(?![A-Za-z])", s_r, re.I):
                problems.append(f"{label}: subject '{s}' contains '{b}'")


# ---------- doc mode ----------

def directives(doc):
    allow = set()
    ban = set()
    for m in re.finditer(r"<!--\s*verify-(allow|ban):([^>]*)-->", doc, re.I):
        items = {x.strip().lower() for x in m.group(2).split(",") if x.strip()}
        (allow if m.group(1).lower() == "allow" else ban).update(items)
    return allow, ban


def blockquote_after(body, label_regex):
    m = re.search(r"\*\*" + label_regex + r"[^\n]*\*\*[^\n]*\n+((?:>.*(?:\n|$))+)", body, re.I)
    return unquote(m.group(1)) if m else None


def verify_doc(path, show_grades=False, legacy=False):
    doc = open(path, encoding="utf-8").read()
    allow, extra = directives(doc)
    banned = [b for b in BANNED if b not in allow] + sorted(extra)
    problems, notes, grades = [], [], []

    parts = re.split(r"\n(?=# (?:FRAMEWORK \d+|ALTERNATE [A-Z])\b)", doc)
    fws = [p for p in parts if re.match(r"# (?:FRAMEWORK \d+|ALTERNATE [A-Z])\b", p)]
    # trim each framework chunk at the next top-level heading that is not a framework
    fws = [re.split(r"\n# (?!FRAMEWORK|ALTERNATE)", p)[0] for p in fws]
    n_main = sum(1 for p in fws if p.startswith("# FRAMEWORK"))
    if n_main != 10:
        problems.append(f"doc: {n_main} frameworks found (want 10, headings '# FRAMEWORK n: \"Name\"')")

    for p in fws:
        label = re.match(r"# ((?:FRAMEWORK \d+)|(?:ALTERNATE [A-Z]))", p).group(1).replace("FRAMEWORK ", "F").replace("ALTERNATE ", "Alt ")
        ex = blockquote_after(p, r"Example")
        if ex is None:
            problems.append(f"{label}: no **Example** blockquote")
        else:
            check_email(f"{label} example", ex, "framework", banned, problems, notes, grades)
        fu = blockquote_after(p, r"Follow-?up")
        if fu is None:
            problems.append(f"{label}: no **Follow-up** blockquote")
        else:
            check_email(f"{label} follow-up", fu, "followup", banned, problems, notes, grades)
        sl = re.search(r"\*\*Subject line options?:?\*\*:?([^\n]*)", p, re.I)
        if sl:
            check_subjects(label, sl.group(1), problems)
        else:
            problems.append(f"{label}: no **Subject line options:** line")
        if not legacy:
            spin = re.search(r"\*\*Spin set:?\*\*(.*)", p, re.I | re.S)
            if not spin:
                problems.append(f"{label}: no **Spin set:** (v2 requires one per framework)")
            else:
                s = spin.group(1)
                subj = re.search(r"subject:\s*(\{\{[^\n]*\}\})", s, re.I)
                if not subj or len(spin_options(subj.group(1))) < 3:
                    problems.append(f"{label}: spin set needs a subject with 3+ options")
                for o in spin_options(s):
                    for b in banned_hits(o, banned):
                        problems.append(f"{label}: spin option '{o}' has banned '{b}'")
                    if re.search("[–—!]", o):
                        problems.append(f"{label}: spin option '{o}' has a dash or '!'")

    # closers
    cl = re.search(r"\n# [^\n]*CLOSERS[^\n]*\n(.*?)(?=\n# (?!#))", doc + "\n# END", re.S)
    if not cl:
        problems.append("doc: no CLOSERS section")
    else:
        sec = cl.group(1)
        for m in re.finditer(r"\*\*(Closer [12][^*\n]*)\*\*[^\n]*\n+((?:>.*(?:\n|$))+)", sec):
            kind = "closer1" if m.group(1).startswith("Closer 1") else "closer2"
            check_email(m.group(1).strip(" :"), unquote(m.group(2)), kind, banned, problems, notes, grades)
        if not re.search(r"\*\*Closer 1", sec):
            problems.append("CLOSERS: no **Closer 1** blockquote")
        if not re.search(r"\*\*Closer 2", sec):
            problems.append("CLOSERS: no **Closer 2** blockquote")

    if not legacy:
        for name, rx in V2_SECTIONS.items():
            if not re.search(rx, doc, re.I):
                problems.append(f"doc: missing section '{name}'")
        if re.search(r"\[NEEDS:", doc):
            notes.append("doc: has [NEEDS: ...] open items; resolve before launch")

    return problems, notes, grades


# ---------- leads mode ----------

def verify_leads(paths, packets_path, canonical_path, threshold, banned):
    copy = {}
    for path in paths:
        copy.update(json.load(open(path, encoding="utf-8")))
    packets = json.load(open(packets_path, encoding="utf-8")) if packets_path else {}
    canonical = [l.strip() for l in open(canonical_path, encoding="utf-8")] if canonical_path else []
    canonical = [c for c in canonical if c and not c.startswith("#")]
    problems, notes, grades = [], [], []

    for em, fws in sorted(copy.items()):
        details_seen = {}
        for key, v in sorted(fws.items()):
            body, subj = v.get("body", ""), v.get("subject", "")
            kind = ("closer1" if key == "C1" else "closer2" if key == "C2"
                    else "followup" if key.endswith("_FU") else "framework")
            label = f"{em} {key}"
            check_email(label, body, kind, banned, problems, notes, grades)
            if re.search(r"(?<!\{)\{[^{}]+\}(?!\})", body + subj) or re.search(r"\[[^\]]+\]", body + subj):
                problems.append(f"{label}: unfilled placeholder or bracket")
            if subj:
                check_subjects_single(label, subj, problems)
            first = " ".join(body.split()[:25]).lower()
            details_seen.setdefault(first, []).append(key)
        for first, keys in details_seen.items():
            if len(keys) > 1:
                problems.append(f"{em}: touches {keys} open identically (detail reused?)")

    # cross-lead similarity per framework key (from Hermes generated-copy-qa)
    def norm(t):
        return re.findall(r"[a-z0-9'&-]+", t.lower())
    keys = sorted({k for fws in copy.values() for k in fws})
    for key in keys:
        blobs = []
        for em, fws in sorted(copy.items()):
            if key not in fws:
                continue
            b = fws[key].get("body", "")
            pk = packets.get(em, {})
            for name in (pk.get("company"), pk.get("city")):
                if name:
                    b = re.sub(re.escape(name), " ", b, flags=re.I)
            b = b.lower()
            for pat in canonical:
                b = re.sub(pat, " ", b)
            blobs.append((em, {w for w in norm(b) if len(w) > 3}))
        for (ea, wa), (eb, wb) in itertools.combinations(blobs, 2):
            if wa and wb:
                j = len(wa & wb) / len(wa | wb)
                if j > threshold:
                    problems.append(f"{key}: {ea} vs {eb} similarity {j:.2f} (> {threshold}, template swap?)")
    return problems, notes, grades, len(copy)


def check_subjects_single(label, s, problems):
    s_r = render_spin(s)
    if s_r != s_r.lower():
        problems.append(f"{label}: subject not lowercase")
    if not 1 <= len(s_r.split()) <= 4:
        problems.append(f"{label}: subject {len(s_r.split())} words")
    for b in SUBJECT_BANNED:
        if re.search(r"(?<![A-Za-z])" + re.escape(b) + r"(?![A-Za-z])", s_r, re.I):
            problems.append(f"{label}: subject contains '{b}'")


# ---------- main ----------

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("doc", nargs="?", help="frameworks doc (.md)")
    ap.add_argument("--grades", action="store_true", help="print reading grade per email")
    ap.add_argument("--legacy", action="store_true", help="skip v2-only structure checks")
    ap.add_argument("--leads", nargs="+", metavar="JSON", help="per-lead copy JSON file(s)")
    ap.add_argument("--packets", help="per-lead {company, city} JSON for name stripping")
    ap.add_argument("--canonical", help="file of regexes for lines allowed to repeat across leads")
    ap.add_argument("--threshold", type=float, default=0.45)
    ap.add_argument("--allow", default="", help="comma list removed from the banned list (leads mode)")
    ap.add_argument("--ban", default="", help="comma list added to the banned list (leads mode)")
    a = ap.parse_args()

    if a.leads:
        allow = {x.strip().lower() for x in a.allow.split(",") if x.strip()}
        banned = [b for b in BANNED if b not in allow] + [x.strip().lower() for x in a.ban.split(",") if x.strip()]
        problems, notes, grades, n = verify_leads(a.leads, a.packets, a.canonical, a.threshold, banned)
        header = f"checked {n} leads"
    elif a.doc:
        problems, notes, grades = verify_doc(a.doc, a.grades, a.legacy)
        header = f"checked {a.doc}"
    else:
        ap.error("give a doc path or --leads")

    print(header)
    if a.grades:
        print("\nEMAIL | WORDS | GRADE")
        for label, n, g in grades:
            print(f"{label} | {n} | {g}")
    if notes:
        print(f"\nNOTES ({len(notes)}, not failures):")
        for x in notes:
            print("  - " + x)
    if problems:
        print(f"\nPROBLEMS ({len(problems)}):")
        for x in problems:
            print("  - " + x)
        print(f"\nFAIL: {len(problems)} problems")
        sys.exit(1)
    print("\nPASS")


if __name__ == "__main__":
    main()
