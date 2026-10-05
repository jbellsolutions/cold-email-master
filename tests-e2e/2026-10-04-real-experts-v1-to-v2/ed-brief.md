# ED brief: Real Experts Series v1 → v2 (Mode 5)

Source doc: `v1.md` (same folder). QC findings: `qc-v1-findings.md`. Attack Plan: `s0-attack-plan.md` (offer verdict FIX FIRST 5/10, so its pillar-4 fix is adopted here).

## ED decisions (binding on every writer)

1. **Reward fix (Strategist pillar 4).** The default reply reward in framework closes becomes the three interview questions written only for them ("Reply and I'll send the three questions I'd ask you"), worded fresh every time. F9 stays the framework *built around* the three questions. Closer 2 keeps offering them. The questions are already logged at research (item 10), so they go out the same day.
2. **Easy out on every close** (QC B1). Each framework close pairs the ask with a rotating plain escape hatch from `buchan-techniques.md` §5 ("If it's not for you, no problem." / "Totally fine if the answer is no." / "If the timing's wrong, say so and I'll leave it." / "Yours either way."). Never repeat a close sentence or an out within a lead (QC B2).
3. **Vary openers** (QC B3). At most 3 of the 13 relevance lines may start with "Saw", and no two frameworks in a row may open with the same verb. Alternatives: "Your clinic's FAQ explains...", "A patient wrote that...", "Three reviews say...", "Twenty-two years of...".
4. **Exactly one research detail per email** (QC B4 to B6).
5. **Terms line rewrite** (QC C1): full form "It isn't a pitch, and nothing is hidden. We just want to connect with real experts." Short form "No pitch, nothing hidden." **"No charge" appears only in F3**, once (QC D5).
6. **F8 credibility line** (QC C5): "I've taught 300 agency owners, and I was asked to speak at an AI summit." Never mention referral partnerships.
7. **Roster** (QC B12): any first-person host line ("I'd interview you", "I wrote three questions I'd ask you", "I only record...") gets a one-line `Roster false:` swap under the example ("Justin, who hosts it, would ask you...").
8. **Follow-up page link** (QC C4): the page link appears ONLY in the follow-ups of F1, F4, F7 and F10. Every other follow-up carries no link and ends on a question about their craft.
9. **Follow-up jobs** (QC D1). Never open with "following up on". Each follow-up gets a `*Job:*` label line above its blockquote:

| Framework | Follow-up job |
|---|---|
| F1 | forgot to mention (one new true detail about the series, plus the page link) |
| F2 | the useful one (one true observation about their field) |
| F3 | honest no-reply admission ("No reply usually means busy, not no.") |
| F4 | yes or no both welcome (plus the page link) |
| F5 | forgot to mention |
| F6 | the useful one |
| F7 | yes or no both welcome (plus the page link) |
| F8 | the useful one |
| F9 | three options, plain ("Ignore this and I'll get the hint. Reply 'send' and the questions are yours. Or answer one right here.") Do NOT invent an "answer by email" offer (QC D3). |
| F10 | pure question, soft (plus the page link). No "would you be open to it" (QC D2). |
| Alt A | the useful one; end on a question about their craft (QC D2) |
| Alt B | yes or no both welcome |
| Alt C | honest no-reply admission |

10. **Claims fixes:** F2 "perfect answer" becomes "a confident answer" (B7). F10 drops the job-loss line (B8). F3 drops "fee" (B9; use "a sales pitch"). Alt A uses "A lot of", never "Most" (B10). Alt A subject stub `your post on` becomes `your post` (B11).
11. **Spin set per framework** (v2): the subject with 3+ options (lowercase, 1 to 4 words, never the series name, no "free"), the greeting `{{RANDOM | Hey | Hi}} {Name},`, and the sign-off `{{RANDOM | {sender} | Thanks, {sender} | Cheers, {sender}}}`.
12. **Keep everything else that works:** the four variables, the angle, the pain pairing, the signature-line homes, locale-real names and towns, the AI-word rules from the claims section, 85 to 100 words for framework examples (house doc target), 30 to 50 words for follow-ups ending on one question, reading grade 5 or lower.
13. **Pillar 1 and 3 claims are NOT in copy.** "The clips are yours to own" and "experts in nearby fields see it" stay out until Justin confirms them (Open Items).

## Output shape (exact)

The whole framework block in v1's shape plus the v2 additions, for each assigned framework:

```
# FRAMEWORK n: "Name"
**Angle:** ...
**Pain pairing:** ...
**Signature lines used:** ...
**Subject line options:** `a` | `b` | `c`
**Structure:**
> ...
**Example (segment, town):**

> Hey Name,
>
> ...
>
> {sender}

*Roster false:* ... (only if the example has a first-person host line)

**Follow-up (reply in thread, 3 days later):**
*Job:* ...

> Hey Name, ... ?

**Spin set:**
    subject: {{RANDOM | a | b | c}}
    greeting: {{RANDOM | Hey | Hi}} Name,
    sign-off: {{RANDOM | {sender} | Thanks, {sender} | Cheers, {sender}}}

---
```

Self-check with the verifier before returning. Put your block in a scratch file with a dummy header and run:
`python3 /Users/home/.claude/skills/cold-email-master/scripts/verify_doc.py <file> --legacy --grades`
It will complain that 10 frameworks are not present and that the closers are missing. Ignore only those. Prepend `<!-- verify-allow: ai -->` because the doc's claims section allows AI in its homes.
