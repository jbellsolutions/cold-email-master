# QC report 2: Real Experts Series v2 (after the fix loop)

Doc: scratchpad/e2e/v2.md (1928 lines). Line numbers below are v2.md line numbers as of this pass. Prior report: qc-v2-final.md (21 findings).

## 1. verify_doc.py --grades (full output, verbatim)

```
checked v2.md

EMAIL | WORDS | GRADE
F1 example | 90 | 3.5
F1 follow-up | 36 | 2.3
F2 example | 95 | 4.2
F2 follow-up | 38 | 4.9
F3 example | 89 | 2.9
F3 follow-up | 32 | 4.1
F4 example | 87 | 4.1
F4 follow-up | 40 | 1.9
F5 example | 94 | 3.9
F5 follow-up | 45 | 3.4
F6 example | 91 | 3.2
F6 follow-up | 37 | 3.0
F7 example | 92 | 4.5
F7 follow-up | 34 | 3.7
F8 example | 89 | 2.9
F8 follow-up | 43 | 4.8
F9 example | 95 | 3.4
F9 follow-up | 32 | 3.0
F10 example | 94 | 4.7
F10 follow-up | 37 | 3.3
Alt A example | 92 | 3.7
Alt A follow-up | 38 | 2.1
Alt B example | 94 | 4.1
Alt B follow-up | 32 | 4.4
Alt C example | 94 | 4.9
Alt C follow-up | 34 | 4.4
Closer 1 (step 21, new thread, subject `{{RANDOM | last note | a question | still worth asking}}`, under 50 words) | 41 | 3.3
Closer 2, Track A (step 22, reply in thread, no subject, under 100 words) | 73 | 2.5
Closer 2, Track B (step 22, reply in thread, no subject, they already share their work, under 100 words) | 78 | 2.1
Closer 2, thin research variant (step 22, reply in thread, no subject, under 100 words) | 81 | 2.8

NOTES (2, not failures):
  - sentence repeated across FRAMEWORK 2, FRAMEWORK 10, ALTERNATE A: 'no matter how good ai gets it cant replace what a veteran knows' (fine only if it is a designated signature line)
  - doc: has [NEEDS: ...] open items; resolve before launch

PASS
```

Both notes are expected: the thesis line is a designated signature line (F2, F10, Alt A, three of a lead's frameworks at most), and the [NEEDS] items are the launch-time open items. Every example is 87 to 95 words, so the worst-case "Thanks, {sender}" spin option adds one word and stays at or under 96. I also grepped the doc for em dashes, en dashes and exclamation marks outside headings: none. There are no "Saw" openers.

## 2. Status of the 21 prior findings

| # | Status | One line |
|---|---|---|
| 1 | FIXED | The 13 closes (l.557 to l.1131) now use 13 different skeletons, each logged in the 18-row bank (l.265-286) with a Roster false form; no sentence repeats. |
| 2 | FIXED | F9 follow-up (l.946) is now a reply-send line, a fresh out ("I won't take a no personally") and one craft question; "answer one here" is gone and the job table (l.343) matches. |
| 3 | FIXED | F3 (l.651): "There's no charge." is its own sentence, the share clause is gone, three signature lines (terms full, no-charge, interview), header updated. |
| 4 | FIXED | F2 now has a Roster false swap (l.609); F3 states why none is needed (l.657) and it is true (no first-person host verb). |
| 5 | FIXED | F7 follow-up (l.850) is now the practical one (45 minutes, pick your slot, link, craft question); F4 (l.708) keeps the yes-or-no job; job table l.333-347 updated. |
| 6 | FIXED | F10 (l.985) now says "Honest question, and it's fine to skip it." before the question, and l.18, l.260 and QC 9 say F10 carries an out. |
| 7 | FIXED | Alt C header (l.1101), selection logic (l.1172) and the Checks line (l.1174) all say it replaces F8 in the back half. |
| 8 | FIXED, with one new inconsistency (N1) | Research item 4 is now ten details (l.492); routing is 10+ / 5-9 / 2-4 / under 2 (l.503-507), repeated in the selection table, campaign structure, Alt B header, infra and QC 15. Alt B no longer fills several slots. |
| 9 | FIXED | Infra §5 (l.1744) now says "subject spun per the Closer 1 block", a single source; "quick one" and the stray "?" are gone. |
| 10 | FIXED | Recycle reward is the review digest in §0 (l.198), the reply section (l.1612), the weekly rhythm table (l.1841) and the Analyst read (l.1865). |
| 11 | FIXED | Header reads GO 7/10, 8/10 pending 7a (l.50); 3c is labelled NOT LIVE until 7a and 7b (l.115); Risk 1 (l.205) and Open Item 7 (l.1917) agree; the pillar maths adds up (1+2+0+2+2). |
| 12 | FIXED | §0 §2 (l.78) now says the lead framework's relevance line carries the pattern and later emails use further distinct details; QC 2 (l.1889) and Research (l.468) match. |
| 13 | FIXED | Colleague note (l.1522) now reads "Reply with a yes and the three questions I'd ask you are on their way." with a Roster false form (l.1526). |
| 14 | FIXED | Closer 1 and the three Closer 2 blocks carry spun stock opener and opt-out lines (l.1230, 1252-1253, 1276, 1299); l.377-378 narrows the follow-up and escape-hatch claim to "reworded per lead". |
| 15 | FIXED | F1 (l.553) is now hedged in one sentence: "I'd bet you knew within ninety seconds, maybe as the car pulled in, before the driver got out." |
| 16 | FIXED | F5 (l.743) folds the series sentence into the one before it ("to get that kind of know-how on the record"); the wisdom line stays in F1. |
| 17 | FIXED | Reply Money rule (l.1319) now reads "an earlier email or reply to this lead (F3 counts...)". |
| 18 | FIXED | The "no Attack Plan yet" clause is gone (l.1695); "all 18 checks" (l.1785) matches the 18-item list; §0 items are renamed A1 to A8 (l.215) so "Open Item N" means one thing. |
| 19 | FIXED | Testing plan (l.160-164) is two fixed variants (interview framing, gift framing) and says the unfixed v1 offer is never sent; Risk 1 and the Analyst read agree. |
| 20 | FIXED | The footer rule is written in (l.1754): postal address and the sequencer's unsubscribe header only, excluded from word counts and the no-link check; the NEEDS tag is gone. |
| 21 | FIXED | F7 pain is now #8, "invited with everyone else" (l.431, l.811); no adjacent fields, no "room", no implied guests; B4 and the room line are held behind Open Item 7b. |

## 3. Findings (new, real)

Fresh full read against checklist §2 (all 19 checks) and the doc's own 18-item QC list. Checks 1 to 12, 14 to 16, 18 and 19 otherwise pass. Three real failures remain, all small, none needing new research.

| # | Location | Rule | Exact text | Owner | Fix |
|---|---|---|---|---|---|
| N1 | Research routing rule l.505 against Selection logic l.1166 | Check 13 (routing) and check 19 (cross-section). "The buckets (one at a time, never two in a row from the same bucket)." | Routing example: "Example: seven details in the default order runs F1, F2, F3, F4, F5, F6, F9 (16 touches)." Buckets: "What it is: F3, F6, F9". F6 then F9 puts two "What it is" frameworks back to back. The 16-touch count at l.1188 repeats it. | Strategist, then Copy Chief | Either change the skip order so the bucket rule survives (skip F10, F8, F6, F7 and so on: seven details becomes F1, F2, F3, F4, F5, F7, F9, which alternates cleanly), or add one sentence saying the bucket rule applies to the full sequence and shortened routes only avoid back-to-back same-bucket where possible. Update the 7-detail example in l.505 and l.1188 to match. I checked 5, 6, 8 and 9 details: only the 7-detail route clashes. |
| N2 | F6 follow-up l.800 and F8 follow-up l.898 | Check 17 (near-twin follow-ups); copy-rules §1 (each follow-up adds one new reason). | F6: "Hey Dr. Lee, one thing I keep noticing. Owners often search before they call..." F8: "Hey Dr. Patel, something I keep noticing in reviews of good dentists. Patients thank the decision..." | Follow-up and closer writer | Same job ("the useful one") with the same opening skeleton, four touches apart in one lead's thread. Reopen F8 on its content, for example "Hey Dr. Patel, reviews of good dentists tend to thank the decision, not the procedure." and keep the rest. (F1 "one thing I left out" and F5 "I forgot to say one thing" are a milder pair of the same shape; reword F5 to "Hey Tom, a detail I skipped:" while you are there.) |
| N3 | F3 close l.653 against the Closer 1 opt-out l.1224 and l.1230 | Check 17: no two escape hatches or opt-outs share a skeleton; opt-outs sit in a separate bank "so they never echo an out the lead already had" (l.309). QC finding 2 set the precedent on F9. | F3: "If the timing's wrong, tell me and I'll leave it." Closer 1: "If not, just say so and I'll stop." / "If not, just say the word and I'll stop." / "If not, let me know and I'll stop." | Framework writer | Same skeleton ("if X, tell me and I'll stop or leave it"), and the bank's own escape-hatch #4 carries it. Reword #4 and F3's out so it does not ask them to tell you anything, for example "If now's a bad time, no hard feelings." (F7's "If you're slammed right now, that's fair." stays as is). |
| N4 | Ammo bank heading l.420 | Check 19 (cross-section). | "THE 10-PAIN AMMO BANK (+3 bench pains)" followed by B1, B2, B3 and B4 (l.436-439). | Strategist | The fix crew added B4 (held pain); the heading was not updated. Change to "+4 bench pains". |

## 4. Verdict

**FAIL.** The script is clean, all 21 prior findings are fixed, and touch 1 (F1) is still the best email in the doc. Four small edits remain (N1 to N4): one routing example that breaks the doc's own bucket rule, one near-twin pair of follow-up openers, one escape hatch that echoes the Closer 1 opt-out, and a stale heading count. None needs new research or a new rewrite loop. After they are applied, a spot-check of l.505, l.800/898, l.653 and l.420, plus a rerun of the script, should be enough to pass.

### Answer to the judgment call: F7 pain #8 against F3 pain #10

Not too close. Keep both. F3 attacks the terms ("it turned out to be a sales pitch"); F7 attacks the targeting ("went to every agent in town"). They are different distrust claims, F3 sits at touch 5 and F7 at touch 13, and F7's turn lands on the scarcity ("each one is picked"), which F3 never touches. F7 is also hedged ("I'd guess") and lives in its own bucket. It meets the F7/7b problem from finding 21: it implies no adjacent experts, no other guests and no room. One optional tweak is in the polish list.

## 5. Polish (non-blocking)

- F7 l.839 "This one didn't." and F3 l.651 "This isn't that." use the same "unlike those" turn. Let F7's turn come from the scarcity instead ("I only have room for a couple of ... a day, so each one is picked" can open the paragraph).
- Outs cluster on one idea (declining is fine): F1 "not for you", F2 "answer is no", F4 "aren't your thing", F5 "pass", F6 "not a fit", and the F9 follow-up "won't take a no personally". Wording differs, but a reader may hear F2 and the F9 follow-up as the same promise. Consider moving F6 to a different idea (for example "If you'd rather keep it to yourself, that's fine.").
- "the three questions I'd ask you" appears verbatim in the F1, F2 and F8 closes (and "the three questions I'd ask" in Alt C). The frames differ, so check 17 passes, but vary F8 (for example "Should I send over the three I'd ask?").
- Three lead-sequence closes or follow-ups start with "Reply" (F1 close, F9 follow-up, Closer 2 "Reply and they're yours"). The continuations differ, so this passes.
- F3 follow-up (l.662) and Alt C follow-up (l.1140) both do the "honest no-reply admission" in a default lead's sequence, and both say "you're busy". Give Alt C the "useful one" job when F3 has already run.
- Closer 2 uses the full feature line ("We share it with our list and socials, and after that it's yours to share") but the signature table (l.325) lists F6 as the only full-form home. Add Closer 2 to the feature-line home, or shorten it.
- The doc's QC list has 18 items; checklists.md §2 now has 19. Add "19. Cross-section consistency: the reward, recycle offer, subjects, open-item numbering and capacity figures say the same thing in §0, the frameworks, the closers, the reply section and the infrastructure section," and change l.1785 to "all 19 checks".
- l.1841 "[NEEDS: recycle gap from Attack Plan section 0, item 11]" is ambiguous with the new "Open Item N" convention, and the Attack Plan section 11 only points to "reply-playbook §6". Say "Attack Plan section 11".
- Capacity table l.1699-1700: "100 live inboxes" next to "102 inbox slots, about 29 sends per inbox" (and 34 against 36 slots) mix inbox counts and slots. State the per-inbox figure from the inbox count (30) or label the slots line as spare slots.
- "a question" is both an Alt B subject option and a Closer 1 subject option. A thin-route lead (Alt B, follow-up, Closer 1, Closer 2) can receive the same subject twice. Swap one.
- On a shortened route, F9 can land at position 5 or 6 of the lead's sequence. Say "back half of the lead's own sequence" in the QC 15 and the selection checks.
- F1 l.555 "I'm putting together the Real Experts Series, because it's not what you know. It's what you've seen." reads slightly like a slogan. Fine as the doc's best email, but "...because it's not what you know, it's what you've seen" in one sentence would sit easier.
