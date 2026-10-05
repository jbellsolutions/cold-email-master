# Checklists

Four checklists, run at four moments. The QC Auditor owns 1 and 2, the Deliverability Engineer owns 3, the Analyst owns 4. The Executive Director confirms all four before calling anything launch-ready.

---

## 1. Per email: DO and DON'T (every touch, every lead)

**DO, every email**
- [ ] Exactly one research detail, in the first two lines, passing the specificity test, logged with a source, not reused in this lead's 22 touches.
- [ ] Exactly one pain (framework emails).
- [ ] The doc's declared close, worded fresh, with an easy way out.
- [ ] Words: framework 60 to 100 (aim 80 to 95), follow-up 30 to 50 ending on one question, Closer 1 under 50, Closer 2 under 100.
- [ ] Reading grade 5 or lower (7 is the ceiling).
- [ ] Exact numbers only for real past results; "built to add" for anything forward-looking.
- [ ] Locale spelling and terms.
- [ ] Reads like one person wrote it to one person, out loud, as a voicemail.
- [ ] Every spintax option passes on its own.

**DON'T, ever**
- [ ] No em dash, no en dash, no exclamation mark (subjects included).
- [ ] No banned word (base list + this doc's list).
- [ ] No price, no fee, no "no cost", no "guarantee".
- [ ] No "free" in a subject or touch 1.
- [ ] No link in a framework email; at most one in a follow-up or closer.
- [ ] No "as I mentioned" or "my last note" in a framework email.
- [ ] No unfilled `{placeholder}` or `[bracket]` in anything that ships.
- [ ] No invented stat, client, result, guest or local detail.
- [ ] No fake urgency; scarcity only if structurally true and in the back half.
- [ ] No parallel three-item list. No "hope this finds you well", "I wanted to reach out", "I'd love to", "hop on a call".
- [ ] No jokes, no humour formulas, no images (unless a declared test).
- [ ] No named competitor in the body.
- [ ] No "silence means no".

## 2. Per doc: the QC second-agent pass (base set; each doc adds its own)

A second agent, never the writer, runs `scripts/verify_doc.py` and then reads. Any failure goes back to the writer. Zero flags to pass.

1. **Script clean:** `verify_doc.py` reports zero problems.
2. **Attack Plan present** and consistent with the frameworks (the signal in §0 shows up in the relevance lines; the free thing in §0 is the one in the free-thing framework and Closer 2).
3. **Naming rule** per the header (branded: once per framework email, in the offer sentence, never in a subject; unbranded: no names anywhere).
4. **Dashes and exclamation marks:** zero.
5. **AI footprint:** no parallel triplets, no filler openers, sentence length varies, read-aloud passes.
6. **Lengths and grade:** every example and follow-up in range.
7. **One detail, one pain:** every framework email.
8. **Links:** none in framework emails; one max in follow-ups and closers, carrying the lead's ref.
9. **Standalone:** no framework email references another; each follow-up references only its own framework.
10. **Claims and facts:** facts-section bans honoured; no promised outcomes; regulated-field rules followed.
11. **Money:** no prices; "free" only in Closer 2; signature money lines only in their homes.
12. **Signature lines:** each used only in its designated homes and within its limits; never more than three per email.
13. **Routing:** selection logic covers every research outcome; scarcity and free-thing in the back half; tracks and thin research route correctly.
14. **Spin sets:** every framework has one; subjects have 3+ options; every option passes the rules.
15. **Opt-out:** Closer 1 and Closer 2 carry a plain opt-out line; nothing says "silence means no".
16. **Touch 1 read twice:** the lead framework's example is the best email in the doc. If it isn't, fix it first.

## 3. Pre-launch gate (nothing sends until every box is ticked)

**Copy**
- [ ] QC pass (checklist 2) on the doc: zero flags.
- [ ] Per-lead QC: a second agent ran checklist 1 on all 22 touches for every lead in the first batch, and `scripts/verify_doc.py --leads` (similarity check) is clean.
- [ ] Open items in the doc are closed, or none touch the copy.
- [ ] Reply templates loaded where the setter or reply agent can use them; reply reward ready to send the same day.

**Infrastructure** (detail in `deliverability.md` §11)
- [ ] Domains, DNS, warmup, capacity, insurance, sequencer settings all pass the Deliverability Engineer's gate.
- [ ] List verified; expected bounce under 2%.
- [ ] Unsubscribe on every step; postal address present for US recipients.

**People and calendar**
- [ ] Sender profiles real and active (LinkedIn posting 2 to 3 times a week where possible).
- [ ] Calendar has plenty of slots (15-minute slots, 5-minute gaps); the booking page matches what the emails promise.
- [ ] Someone (or an approved reply agent) answers within minutes during send hours; caller ready if Sprint mode.

**Approval**
- [ ] Justin has approved the launch. Nothing is uploaded, scheduled or sent without it.

## 4. Weekly rhythm (after launch)

| When | Check | Owner |
|---|---|---|
| Daily | Warmup scores (pull under 99%; out at about 92%), seed placement, bounce rate (pause above 3%) | Deliverability Engineer |
| Daily | Replies answered within minutes; booking cadence running | Reply Setter |
| Friday | Reply rate per inbox and domain, this week vs two weeks ago; ≥100 sends and under 1% → pull | Deliverability Engineer |
| Saturday | Auto-responder seed test; under 60% return → kill inbox/domain; harvest new auto-responders | Deliverability Engineer |
| Weekly | Verdicts: any variant past 1,000 sends (0 positives kill; 1 positive scale to 3,000); booked, showed, qualified, closed | Analyst |
| Weekly | Next test chosen from results + sales-call notes; learnings written to the Obsidian vault | Analyst |
| On a sudden drop | Spam trap first (pull domains now), fingerprinting second (more spintax) | Deliverability Engineer |
| At sequence end + 3 months | Recycle non-repliers with a new angle and free thing | Strategist + Analyst |
