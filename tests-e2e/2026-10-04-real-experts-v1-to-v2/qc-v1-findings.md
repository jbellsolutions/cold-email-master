# QC findings: Real Experts Series v1 (Mode 5 audit, read-only)

Doc: `/private/tmp/claude-501/-Users-home-Cold-Email-skills/6a7bb7b5-e4e6-4ecb-9377-02f9a55ec684/scratchpad/e2e/v1.md`

## verify_doc.py output (--grades)

```
EMAIL | WORDS | GRADE
F1 example | 85 | 3.1      F1 follow-up | 43 | 3.7
F2 example | 90 | 4.4      F2 follow-up | 38 | 2.4
F3 example | 89 | 4.0      F3 follow-up | 38 | 2.7
F4 example | 87 | 3.9      F4 follow-up | 36 | 3.0
F5 example | 93 | 3.6      F5 follow-up | 39 | 1.5
F6 example | 89 | 5.0      F6 follow-up | 37 | 3.2
F7 example | 87 | 5.1      F7 follow-up | 39 | 4.2
F8 example | 87 | 3.2      F8 follow-up | 40 | 2.4
F9 example | 86 | 4.4      F9 follow-up | 39 | 2.3
F10 example | 87 | 3.9     F10 follow-up | 36 | 2.7
Alt A example | 90 | 4.1   Alt A follow-up | 33 | 2.4
Alt B example | 87 | 5.7   Alt B follow-up | 35 | 3.0
Alt C example | 86 | 5.7   Alt C follow-up | 33 | 3.1
Closer 1 | 41 | 5.8
Closer 2, Track A | 62 | 3.1
Closer 2, Track B | 63 | 3.1
Closer 2, thin research variant | 59 | 3.7

NOTES (5, not failures): F7 5.1, Alt B 5.7, Alt C 5.7, Closer 1 5.8 (all under the 7 ceiling);
Closer 2 thin variant: possible parallel triplet (confirmed, row D6).

PROBLEMS (20): 'ai' in F2/F8/F10/Alt A (allowed by the doc's claims section, ignored);
no Spin set x13, missing ATTACK PLAN / INFRASTRUCTURE / WEEKLY RHYTHM (by design, ignored).
FAIL: 20 problems  ->  0 real script problems after the ignores.
```

Script-clean after the agreed ignores. Every finding below is a read-only judgement the script can't make. Lengths and grades all pass. No dashes, no exclamation marks, no links in framework emails, naming rule honoured (once per framework email, never in a subject), "AI" only in its homes.

## Verdict on touch 1

**F1 is NOT the best email in the doc (checklist §2 item 16 fails).** F9 (Three Questions) and F8 and F6 have more specific relevance lines and F9 names a concrete reward. F1's relevance line is the vaguest in the doc and is weaker than the doc's own Gold example ("found the leak two other plumbers missed"). F1 also states unsourced facts as true, has a wisdom line that doesn't flow aloud, and names no reward. Fix F1 first (rows A1 to A3), then the rest. Overall verdict: **FAIL**, 27 findings.

## Findings table

Owner key: W = framework writer, FC = follow-up/closer writer, BE = Buchan editor, PE = plain-English editor, CC = Copy Chief.

| ID | Location | Rule | Exact offending text | Owner | Suggested fix |
|---|---|---|---|---|---|
| A1 | F1 example, relevance | Specificity test; copy-rules §6 (Gold = the named skill) | `Saw a few of your reviews say you found what two other shops missed.` | W | Name what was found, as the doc's own Gold does: `Saw three reviews say you found the intermittent stall two other shops missed.` (use the real thing from the reviews, with the review source logged). |
| A2 | F1 example, pain paragraph | No invented detail; checklist §1 DON'T; one detail only | `You hear a car pull into the lot and you already know it's the timing belt. Took you twenty years to get that, and nobody's ever asked you how.` and `That's the thing I keep thinking about.` | W | The ninety seconds is a model from the swap table stated as fact about Ray, "twenty years" is a second unsourced detail, and "nobody's ever asked you how" is unprovable. Hedge it as the doc does elsewhere: `I'd bet you can hear a car pull in and know it's the belt before the driver gets out.` Drop "twenty years" unless it is the logged detail. Cut "I keep thinking about" (borrowed feeling, not Buchan-honest). |
| A3 | F1 example, offer + close | Read-aloud; copy-rules §5 (reward named) | `It's not what you know. It's what you've seen.` and `Reply and I'll send you more.` | PE | The wisdom line has no referent ("It's not what you know" follows "I'm putting together the Real Experts Series"), so it reads as a stray slogan. Fold it in: `I'm putting together the Real Experts Series, because it's not what you know, it's what you've seen.` Name the reward: `Reply and I'll send you the page with how it runs.` |
| B1 | F1 to F9, Alt A to C, all closes (F10's question is its own soft close, not flagged) | copy-rules §5 / checklist §1: easy out on every close | `Reply and I'll send you more.` (F1, F6) / `Curious? Reply and I'll send the details.` (F2) / `Reply and I'll send you everything.` (F3) / `Want to see what it looks like? Just reply.` (F4) / `Reply if you're curious and I'll send it over.` (F5) / `Reply and I'll send the details.` (F7, Alt A, Alt C) / `Reply and I'll send more.` (F8) / `Just reply and I'll send all three over today.` (F9) / `Reply and I'll send you more about it.` (Alt B). None carries a way out. "No pitch, nothing hidden" is a terms line, not an out. | BE | Add a rotating Buchan escape hatch to each close and put an out bank in the doc: `If it's not for you, no problem.` / `Totally fine if the answer is no.` / `If the timing's wrong, say so and I'll leave it.` / `Yours either way.` Never repeat one within a lead. |
| B2 | F1 vs F6; F7 vs Alt A vs Alt C; F8 | copy-rules §5: no two emails to one lead close with the same sentence | F1 and F6: `Reply and I'll send you more.` F7, Alt A, Alt C: `Reply and I'll send the details.` F8: `Reply and I'll send more.` (one word off) | W | These sit in the same 22-touch sequence, so the agent copying the examples breaks the doc's own "worded fresh" rule. Rewrite each example close from the doc's variation bank so no two example closes match, and add a one-line reminder under the bank. |
| B3 | All 13 framework examples, first line after greeting | copy-rules §7 never look mass-sent; checklist §2 item 5 (filler openers) | Every relevance line starts `Saw ...`: `Saw a few of your reviews`, `Saw you only work`, `Saw you still climb`, `Saw you've had`, `Saw your dad`, `Saw your clinic's FAQ`, `Saw you've sold`, `Saw a patient wrote`, `Saw you rebuilt`, `Saw you still teach`, `Saw your episode`, `Saw you only take`, `Saw the other contractors` | W | Ten consecutive emails to one lead opening the same way is a fingerprint and reads like surveillance. Vary the entry: `Your clinic's FAQ explains why...`, `A patient wrote that...`, `Twenty-two years of climbing every roof first...`. Add "do not open two emails to one lead with the same verb" to the best-practices block. |
| B4 | F2 example, relevance | Exactly one detail (checklist §1; §2 item 7) | `Saw you only work with restaurants, and that you started on the floor as a server.` | W | Two facts, two research slots. Keep one: `Saw you started on the floor as a server before you ever touched a P&L.` |
| B5 | F4 example, relevance | Exactly one detail | `Saw you've had the same chair on Atlantic for nineteen years, and clients drive in from Jersey.` | W | Tenure plus draw radius. Keep one (the Jersey drive is the stronger Gold). |
| B6 | F3 example and F5 example, relevance | Exactly one detail (same-story pairs, lower severity) | F3: `Saw you still climb every roof yourself before you give a number, twenty-two years in.` F5: `Saw your dad started the shop in 1978, and you were pulling wire with him by fourteen.` | W | Each adds a second fact (tenure; age at start). Drop `twenty-two years in` and `by fourteen`, or confirm the pair is logged as one detail. |
| B7 | F2 example, pain | Doc spine: "confident answer", not a perfect one | `gets a perfect answer from something that has never sat with a restaurant owner at midnight` | W | "Perfect" undercuts the point (if it were perfect they would not need the veteran) and conflicts with pain #3. Use `a confident answer`. |
| B8 | F10 example, pain | Claims section: never "coming for their job", no predictions, never scare | `A lot of the people in that room are probably wondering if the job they're training for will exist in five years.` | W | Puts the job-loss fear straight beside the AI thesis line. Reframe on what stays true: `A lot of the people in that room are probably wondering what's still worth learning when everything is changing.` |
| B9 | F3 example, pain | Checklist §1: no price, no fee | `Then it turns out to be a fee, or a list to buy.` | W | The word "fee" is in the email. Say: `Then it turns out to be a sales pitch.` (also fix ammo-bank pain #10 and the pain-pairing text the same way). |
| B10 | Alt A example, pain | Claims section: no counts or "most" about online content; allowed is "a lot" | `Most of what people read in your field now comes from something that's never run a campaign.` | W | "Most" is a quantity claim. Use the allowed phrasing: `A lot of what people read in your field now comes from something that's never run a campaign.` |
| B11 | Alt A, subject options | Subject must be complete, 1 to 4 words, no stub | `your post on` | W | An unfinished subject that would ship as a fragment. Replace with `your post` or a field-neutral option such as `your last post`. |
| B12 | F7 example, F9 example, Closer 2 A/B, Alt C follow-up | Sender roster: "I'd interview you" only when `hosts_the_interviews` is true | F7: `I only record a couple of Real Experts Series interviews a day`. F9 and Closer 2: `I wrote three questions I'd ask you`. Alt C follow-up: `Just me asking about the strangest systems you've seen.` | W | Examples hard-code a host-in-first-person claim with no roster-false variant. Add a one-line note per framework (or a swap line in the roster table) for the `hosts_the_interviews: false` case: `Justin, who hosts it, would ask you...`. |
| C1 | F3 example, Closer 2 Track A | copy-rules §11 no parallel three-item lists (v2 wins over the doc's terms line) | `No charge, no pitch, nothing sneaky, nothing hidden.` | CC | The doc's full terms line is a parallel list. Rewrite the signature line: `It isn't a pitch, and nothing is hidden. We just want to connect with real experts.` Keep the two-item short form `No pitch, nothing hidden.` |
| C2 | F6 example (feature line full) | No parallel three-item lists | `We send it to our email list, feature it on our socials, and it's yours to share with every client who asks.` | PE | Three parallel verbs. Rewrite: `We send it to our email list and feature it on our socials. After that it's yours to share with every client who asks.` Update the full feature line in the signature table the same way. |
| C3 | F6 example, pain | No parallel three-item lists | `Every new client, same question, same careful answer.` | PE | Three parallel fragments. Cut to: `Every new client asks the same thing, and you give the same careful answer.` |
| C4 | Doc structure: every follow-up vs every framework close | Reply is the trigger; reward must be real and not already spent (checklist §1 close; copy-rules §5) | All 13 follow-ups hand over `{page link}`; F2 onward still closes `Curious? Reply and I'll send the details.` / `Reply and I'll send you everything.` / `Reply and I'll send the details.` | CC | The header says the page comes out in follow-ups, so the "reply for more" reward is already spent at step 2 and every later close asks them to reply for something they have. Decide: link only in the first follow-up and F9's, with other follow-ups carrying a new reason instead; or have F2 onward close on a different named reward (the three questions are F9/Closer 2 only; a one-line answer to their field question is available). |
| C5 | F8 example and credibility line vs Offer Block | Doc consistency; "Don't hint at what we sell"; v2 "Agency only as what you are not" | F8: `I taught referral partnerships to 300 agency owners`. Offer block: `Behind the curtain (never in email, follow-ups or closers): the referral partnerships work and the paid programs.` | CC | The credibility line puts the behind-the-curtain topic into the email and names "agency owners". Either change the credibility line (`I've coached 300 business owners on working with other businesses, and I was asked to speak at an AI summit`) or amend the offer block to allow it. As is, the doc contradicts itself. |
| D1 | All 13 follow-ups, opener | copy-rules §11 / Buchan §10: each follow-up has its own distinct job; never a nag; read-aloud | `Hey Ray, following up on the timing belt note.` / `Hey Dana, following up on the P&L note.` / `...following up on the not-a-pitch note.` / `...following up on the ring light note.` / `...following up on the note about your dad's shop.` / `...following up on the dental cleaning note.` / `...following up on the East Nashville note.` / `...following up on the crown note.` / `...following up on the three questions.` / `...following up on the tax course note.` / `...following up on the firing-clients note.` / `...following up on the reactive dogs note.` / `...following up on the boiler note.` | FC | Every follow-up opens with the same five words and refers to the email by a label nobody would say aloud ("the not-a-pitch note", "the ring light note"). Same shape every time: label, reassurance about format, link, craft question. Give each a distinct Buchan job and a different opener: F1 forgot-to-mention (a new true detail), F2 the useful one, F3 honest no-reply admission (`No reply usually means busy, not no.`), F4 yes-or-no both welcome, F5 forgot-to-mention, F6 useful one, F7 yes-or-no, F8 useful one, F9 three-options-style (answer here, or reply "send"), F10 pure question. Add the job label under each follow-up. |
| D2 | F10 follow-up, Alt A follow-up | Follow-up adds a new reason to answer; never nag; F10 is the lowest-pressure email | F10: `Your answer to that question would make a great interview, and you'd see the edit first. Here's how it works: {page link}. Would you be open to it?` Alt A: `Worth twenty minutes?` | FC | F10 switches from a soft question to a closed ask and adds only mild flattery ("would make a great interview"). Keep it soft: restate the question differently, or add one new true reason, and end on a question about their craft, not on `Would you be open to it?`. Same for Alt A: end on a question about the client they should have fired. |
| D3 | F9 follow-up | Don't invent terms outside the Offer Block | `If you'd rather just answer them by email, that works too.` | FC | The Offer Block has no email-answer option and it would not give the lead anything on the record. Cut it, or confirm with Justin and add it to the Offer Block first. |
| D4 | Closer 2 Track A, Track B, thin variant | Checklist §2 item 15 / copy-rules §13: Closer 2 carries a plain opt-out line | A: `Last one from me, no hard feelings either way.` ... `Fair enough?` B: same. Thin: `If you'd rather just see how it works, reply and I'll send it. Fair enough?` | FC | "Last one from me" announces the end but offers no opt-out. Add one rotating line: `If this isn't for you, just say so and I'll stop.` / `Not your thing? One word back and you won't hear from me again.` Also let the opt-out do the closing and drop one of the two "either way" phrasings in Track A. |
| D5 | Closer 2 Track A vs F3 | Doc's own rule: `"No charge" is allowed once per lead, in F3 or Closer 2`; QC item 11 | F3: `No charge, no pitch, nothing sneaky, nothing hidden.` Closer 2 A: `No charge, no pitch, nothing sneaky, nothing hidden.` | FC | F3 is in every default sequence, so "no charge" lands twice. Drop `No charge` from Closer 2 (terms with the C1 rewrite: `It isn't a pitch, and nothing is hidden.`) and keep it only in F3. |
| D6 | Closer 2 thin research variant | copy-rules §11 triplets; placeholders | `No pitch, nothing hidden, and it's yours to share.` and `Hey {first_name},` | FC | Script flagged it and it is a real three-item run. Rewrite as two items: `No pitch, nothing hidden. It's yours to share.` Mark `{first_name}` as an agent fill in the same way the other examples mark `{sender}`, or use a named example like the others. |
| D7 | Closer 1 subject (step 21) | copy-rules §3: banned in subjects "quick question"; subjects vague, not selling | `quick one` | FC | One word off a banned subject and a pattern spam filters learn. Use `last note` or `a question`, and give it 3 spin options for v2. |
| D8 | Closer 1 (note, passes narrowly) | Checklist §2 item 15 | `Is a 20 minute interview something you'd ever do, or should I stop cluttering your inbox?` | FC | Passes as a plain opt-out question, so not counted as a finding. Optional: use `20 to 30 minute` to match the doc and trim to grade 5 (scored 5.8). |

## Counts by owner

(D8 is a pass-with-note and is not counted.)

| Owner | Findings | Rows |
|---|---|---|
| W (framework writer) | 13 | A1, A2, B2, B3, B4, B5, B6, B7, B8, B9, B10, B11, B12 |
| BE (Buchan editor) | 1 | B1 |
| PE (plain-English editor) | 3 | A3, C2, C3 |
| CC (Copy Chief) | 3 | C1, C4, C5 |
| FC (follow-up/closer writer) | 7 | D1, D2, D3, D4, D5, D6, D7 |
| **Total** | **27** | |

## What passed (no action)

Lengths and reading grade on all 30 pieces; zero dashes and exclamation marks; naming rule; "AI" confined to F2, F8 (summit line), F10, Alt A; no "free", "no cost", "guarantee", price or stat anywhere in copy; no links in framework emails; follow-ups one link max and end on one question; follow-ups stand on their own framework only; no "silence means no"; scarcity (F7) and free thing (F9) in the back half; each framework has 3 subject options; signature lines within their homes and never more than three per email.
