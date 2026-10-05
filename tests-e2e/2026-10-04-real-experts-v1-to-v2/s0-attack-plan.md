## §0 ATTACK PLAN — HOW WE ATTACK

**Verdict header**
- `OFFER: FIX FIRST (score 5/10)`
- `MODE: Standard 22-touch. No Sprint. Spearhead tier off until the referral-partner priority list exists.`
- `FREE THING: three interview questions written only for them, from research, sent the same day they reply`

**What this means, in one paragraph.** The v1 copy is strong, and copy cannot rescue an offer. From the prospect's side, the v1 offer is a respectful invitation with no proof behind it and a reply reward ("more info") that is not worth anything on its own. Two fixes, both inside the doc's own bans, take it to 8/10 (see 3c): make the three questions the default reply reward, and filter the list on the review pattern before research starts. A third fix needs one fact confirmed first: name the edited interview and clips as an asset they keep. Proof stays at 0 until real interviews exist. We do not invent it. The real business goal, referral partnerships, sits behind the curtain. So the number that matters is not interviews recorded but referral conversations started, and the plan below measures it.

---

### 1. Target

- **Who:** the named expert in a US business, meaning the person customers ask for by name. In a firm, that is the partner or principal who is the expert, not the marketing person. In a family business, it is whoever the reviews name. There are 12 segments, per the swap table: auto and repair, home and trades, personal care, health and wellness, family/pets/learning, food and hospitality, real estate and property, professional services, marketing and creative, technology, product founders, coaching and consulting.
- **Hard filters (at list build, before research):**
  1. A person is named in the reviews or on the site as the practitioner. Faceless brands and franchise locations with no named expert are out.
  2. The review-pattern signal is present (see 2).
  3. A personal or named-person email address can be found and verified. If the only address is a generic inbox, the lead goes to a lower-priority pool and is not dropped.
  4. Not already a contact, a past guest or a referral partner. The do-not-contact list is checked.
- **Filters that stay per lead (already in the doc):** at least 2 Gold or Silver details or the lead is skipped (the routing rule), the Track A/B check, and the regulated-field check.
- **Segment priority at launch:** `[NEEDS: which segments the referral-partnership business most wants as partners]`. The interview is the front door to that business, so the list should lean toward the segments the back end serves. Until Justin answers, weight toward segments where reviews name a person and a judgment skill (auto and repair, home and trades, personal care, family and pets). Those have the densest Gold details and the lowest regulatory exposure. Track B segments (marketing, technology, coaching) run on Alt A.
- **TAM:** no count yet. `[NEEDS: TAM count]`. Method:
  1. Pull Google Maps listings by segment category and by metro through `lead-warehouse` and `apify-enrich`.
  2. Hand-check a random sample per segment against hard filters 1 to 3, and record the pass rate.
  3. TAM per segment = listings pulled × measured pass rate. Report it by segment, with the sample size beside it.

  Professional services and regulated fields can also be pulled from license boards and association directories.

### 2. Signals

- **The signal: the review pattern.** Customers have written down the expert's ninety seconds themselves. Several reviews name the same judgment skill: found what others missed, knew right away, talked me out of the thing I didn't need, the one other pros call. This is what makes the invitation feel earned rather than mass-sent, and it is the list-level version of the doc's Gold detail.
- **Why it matters for the offer:** "every field, US" is a population, not a list. A list filtered on the review pattern puts the reason we're writing in the first line of every email, and turns a broadcast into "they actually looked."
- **Secondary signals (route the sequence, not the list):** teaching, mentoring or hiring juniors (F10 moves forward), a family business or origin story (F5 leads), a visible FAQ or repeated customer question (F6 leads), Track B channels (Alt A leads), and no camera signals (Alt C).
- **Timeliness:** the thesis is timeless on purpose, and we do not manufacture a "why now." A milestone the expert posted themself (an anniversary year in business, an award, a new location) is a valid Silver detail when research finds one.
- **How List & Signals gets it in-house (no paid enrichment SaaS):**
  - Scrape Maps reviews with `apify-enrich` / Apify.
  - Score the review text against a phrase set for judgment skills, using an in-house AI pass. List & Signals writes the phrase set per segment and keeps the pass rate. We don't invent thresholds here.
  - Pull sites and about pages with `firecrawl` / browser-use.
  - Run the Track B check by searching YouTube and podcasts with browser-use.
  - Find emails by guessing the common patterns, then verify every address with `verify-emails` / `verify-leads` (self-hosted Reacher). Catch-all domains get catch-all verification.
  - Store everything in `lead-warehouse`.

### 3. Offer score: the 5 cold-traffic pillars, from the prospect's side

**3a. The offer as v1 states it:** a 20 to 30 minute recorded interview about what you've learned. We send it to our list and socials, and it's yours to share. No charge, no pitch, nothing hidden. Reply and I'll send more info.

| # | Pillar | Score | Evidence (one line) |
|---|---|---|---|
| 1 | Makes them money, reframed as being found by people who need them | **1** | The only allowed line is "if somebody watching needs what you do, they'll know where to find you." We can't state the list size, views or clients, so the visibility is real but unsized. "Theirs to share" is the one tangible asset. |
| 2 | Signal paired with the list | **1** | The list is "experts in every field, US." Per-lead research skips weak leads, but that filters after the pull. It is not a signal the list is built on. |
| 3 | Look-alike proof | **0** | No episodes, no guests, and the doc rightly bans "our last guest." F8's credibility line (300 agency owners, an AI summit) is proof about the sender, not look-alike proof. |
| 4 | Easy yes | **1** | The ask is tiny (a reply). But in 8 of 10 frameworks the reward is "more info," the page, which is not worth anything on its own. The reward that is (the three questions) appears in only 2 of 22 touches, F9 and Closer 2. Behind the reply sits a 45-minute on-camera call with a stranger. |
| 5 | Not Google-able | **2** | Nobody can search their way into being interviewed about their own judgment. One caveat: the three questions alone could be machine-written, so they are worth something only if they are built from a Gold detail. |
| | **Total** | **5/10** | Under 6, so **FIX FIRST**. No 0 on pillar 1 or 4. |

**3b. The fixes (each inside the doc's bans: no money talk, no "free" hook, no clients, no list size, no views):**

- **Pillar 4, from 1 to 2: make the reward valuable on its own.** The default reply reward in every framework becomes "the three questions I'd ask you, plus how it works." The three questions are already logged at research time (research item 10), so they go out the same day. F9 and Closer 2 keep their framing. Every other framework's close shifts from "reply for more" to "reply and I'll send the questions I'd ask you." The variation bank gets reworded to match, and the closes still never repeat within a lead. The reply templates already have the three-questions message. It becomes the default reply, with the page link under it.
- **Pillar 2, from 1 to 2: filter the list on the review pattern** (section 2) before research. Every lead then arrives with the reason we're writing already in hand.
- **Pillar 1, from 1 to 2 (conditional): name the asset, and name who will see it.**
  - First, the asset. The offer block and the feature line say they keep the edited interview and the short clips. Those clips can go on their site and profile, and to every customer who asks the question they answer fifty times (F6). The clips are what they'd otherwise hire a videographer and editor to make. We say the asset, never a price. `[NEEDS: confirm the full interview and clips are delivered as files they own, not only a link]`. If they only get a link, this pillar stays at 1.
  - Second, who sees it. Add the honest version of the room line: the experts in the fields next to theirs see it too. These are the people who serve their customers before and after them. It promises no clients, and it is the true shape of what the series does.
- **Pillar 3 stays 0, and we say so.** It is fixed by a milestone, not by copy:
  1. Record the first interviews from Justin's warm network before the cold launch, or in parallel with it.
  2. Once guests approve and their interview is published, add a true look-alike line by segment, such as "I just recorded one with a {segment} in {state}." Name the guest only with their consent.

  Until then, the doc does what the playbook prescribes when there is no proof: lead with the terms and the free thing.

**3c. The rewritten offer (the version that passes):**
> A 20 to 30 minute recorded interview about what you've learned. Our team edits it and cuts short clips. You see it first, and once you approve it, the interview and the clips are yours to use anywhere. We share it with our list, our socials, and the experts in the fields around yours. No charge, no pitch, nothing hidden. Reply and I'll send you the three questions I'd ask you, and how it works.

The rewrite scores 2 + 2 + 0 + 2 + 2 = **8/10, GO**, once the file-delivery fact is confirmed. Without it, the score is 7/10, which is still GO.

**3d. What this means for the business behind the curtain.** The prospect scores what they see: the interview. The business scores what comes after: a referral-partnership conversation that the prospect starts. Those are two different funnels joined by one call. The offer can score well and still produce nothing for the business, if interviews never turn into partnership conversations. That is why the testing plan (section 8) tracks the whole chain, and why the segment mix (section 1) needs Justin's answer on which partners the back end wants.

### 4. The free thing

- **What it is:** three interview questions written only for this expert. They come from their Gold and Silver details, their ninety seconds and their story hooks (research items 4 to 6). They are theirs whether they do the interview or not.
- **Why it qualifies (honestly):** it is in the house idea bank for interview offers ("Interviews, three questions written just for them"). Its value is that it proves somebody read their reviews and understood the work. It is weaker against the "give away what others charge for" rule, because people rarely pay for interview questions. So the questions must be specific enough that no other expert in the category could receive them. QC fails any question that passes the swap test (could it be sent to another business in their category?).
- **Same-day fulfilment:** the questions are written and logged at research time, before touch 1 goes out, so the reply goes back within minutes with no new research. The setter pastes them from the research log.
- **Held in reserve for the recycle:** a one-page "what your customers say you do that nobody else does" digest. It is built from the 20 or more reviews we already read, and it is worth having on its own. Marketers sell this kind of customer-voice summary. It needs no new data. For health and wellness, it quotes no outcomes or results.

### 5. Proof on file

- **True today, sender proof only:** Justin taught referral partnerships to 300 agency owners and was asked to speak at an AI summit. This line appears in F8 only, in the first person only when the sender is Justin.
- **Look-alike proof:** none. That stays true until real interviews are recorded, approved and published.
- **May NOT be claimed:** list size, audience size, views, reach, past guests, past episodes, "our last guest," any named guest, clients or new business for them, "we'll pay you" (parked, open item 1), any statistic about AI or the internet, and "a couple a day" until the recording schedule is confirmed (open item 2).

### 6. Campaign mode

- **Standard 22-touch (the default), as the doc's policy section states.** It is relationship-led, the ask is personal (their judgment, on the record), and the back-end goal is a partnership. All of these reward patience and many angles over speed.
- **No Sprint.** Sprint needs a strong offer and a fast-close motion. This offer is not strong until the fixes land, and a booking cadence pushing hard toward a call would contradict "no pitch, nothing hidden."
- **Spearhead tier: off at launch.** It turns on when two things exist: (a) Justin's list of the businesses he most wants as referral partners, and (b) at least one published interview to point to. The special thing for that tier is a printed card with their three questions, mailed before touch 1, followed by an email that names it.

### 7. Capacity math `[NEEDS: capacity]`

House constants: about 30 cold sends per inbox per day, 3 inboxes per domain (90 a day per domain, under the 100 cap), and +50% insurance inboxes warming on the side. Standard load is 22 touches per lead, so new leads a day = sends a day ÷ 22.

| Daily cold sends | Live inboxes | Live domains | Insurance inboxes | Insurance domains | Total inboxes / domains | New leads a day |
|---|---|---|---|---|---|---|
| 1,000 | 34 (1,000 ÷ 30, rounded up) | 12 | 17 | 6 | 51 / 18 | about 45 |
| 3,000 | 100 | 34 | 50 | 17 | 150 / 51 | about 136 |

- **Steady state only:** sends = new leads × 22 holds only once every step of the sequence has cohorts in flight. Before that, the same new-lead rate sends less. The inbox count is the ceiling, not the starting volume.
- **Research load:** every new lead needs the full research checklist, plus the three questions, before touch 1. That means about 45 or about 136 fully researched leads a day, and research throughput is a constraint in its own right.
- **The likely binding constraint is the host's calendar, not the inboxes.** Open item 2 says Justin records about two interviews a day, and F7's scarcity line depends on that. Size the send volume from the recording ceiling:
  > sends a day needed = interviews a day ÷ (positive reply rate × book rate × show rate)

  All three rates are `[NEEDS: measured]`. We don't guess them. Once the first 1,000-send verdict produces real rates, solve this formula. If it calls for fewer sends than the inbox capacity, the extra inboxes go to the always-warm inventory instead of to more volume. If more people book than the host can record, either the roster adds a host (`hosts_the_interviews`), or F7's line changes and the volume comes down.

### 8. Testing plan

- **What counts as a positive for this offer:** a reply that asks for the questions, the info or the page, says yes or sure, answers the follow-up's question with real engagement, or asks the catch question in good faith. These do not count: not now, not interested, unsubscribe, auto-replies, and "is this a podcast" with no further interest.
- **First test (one variable):** the reply reward, because it is the pillar 4 fix and it does not depend on the selection logic. The lead framework changes per lead, so it can't be the test variable.
  - **Variant A:** v1 as written, "reply and I'll send more info."
  - **Variant B:** the fixed offer, "reply and I'll send the three questions I'd ask you."

  Both variants use the same list (the review-pattern filtered list), the same frameworks and the same inboxes.
- **Verdict thresholds:** no verdict before 1,000 sends per variant.
  - 1,000 sends and 0 positives: kill the variant, and change the offer or the list, not the subject.
  - 1,000 sends and 1 positive: scale to 3,000 before judging.
  - Count every touch, and attribute each positive to the step that produced it.
- **The full chain, tracked per lead:** positive, then booked, showed, recorded, approved, published, and finally a referral-partnership conversation that the guest starts (they asked how we make money, or asked about the work). The last link is the business metric. If interviews are recorded but no partnership conversations start, the series is working and the business is not. Fix that on the page and in the post-interview flow, never in the cold email.
- **Read by segment:** positives, bookings and partnership conversations by segment. The list moves toward the segments that do well on both the prospect side and the business side.
- **Next tests, in order and one at a time:** Track B (Alt A) as the lead framework against F1 for loud-segment leads, the subject set, and naming mode (branded against unbranded).
- **Who reads the results:** the Analyst, on the weekly rhythm. Results go into the campaign's results note in the Obsidian vault (booked, showed, recorded, partnership conversation), together with the next test chosen.

### 9. Reply plan

- **Who answers:** the reply-setter agent drafts, and Justin approves sends unless an auto-send policy is set for this campaign. Any reply pauses the sequence.
- **Speed:** within minutes, not hours. The three questions and the page are pre-built per lead, so there is nothing to research at reply time.
- **What goes back:** the three questions, then the page link with the lead's ref (`experts.truerevenuepartnerships.com/?ref={lead_ref}`), using the doc's reply templates.
- **Calendar:** the Expert Series event, about 45 minutes (15 to get acquainted, then the 20 to 30 minute interview, then the review booking). `[NEEDS: switch cal.com from the 30-minute discovery event to the Expert Series event]` (open item 3). Offer as many slots as the host's recording ceiling allows. The ceiling sets the slots, and the slots set the volume (section 7).
- **Caller hand-off:** none by default. A phone push contradicts the terms. Exception: a lead who replied positively and has a number but didn't book can get one warm call or text from the host. Then stop, and set the recycle trigger.
- **The catch question:** answer it with the doc's "how do you make money" reply, word for word in spirit. The referral-partnership work is said plainly and is never pitched on the call.

### 10. Trust readiness

- **Sender profile:** prospects will check who is asking. Justin's LinkedIn should show the series (a featured link to the page, and posts about what experts teach him once interviews exist). Every sending inbox needs a real first name, a Google profile photo and roster flags filled in (open item 5).
- **The page:**
  - Rename it to "Real Experts Series" (open item 6).
  - Replace "video coming soon" before the reply templates go live (open item 4).
  - Add one plain line saying who runs the series and what else they do. This makes "nothing hidden" literally true when someone checks.
- **Domains:** sending domains are lookalikes of the brand that owns the page, lead to a real site, and pass the pre-launch infrastructure gate. No inbox goes live until warmup health reads 99 to 100%.
- **Links:** none in framework emails, and one in follow-ups (the page with the ref). Turn off open tracking, or use a custom tracking domain.

### 11. Recycle plan

- **Trigger:** step 22 sent, no reply, plus the house recycle gap (reply-playbook §6). We never recycle a no, an unsubscribe or a rude reply.
- **What changes:** a new angle and a new free thing.
  - **New angle:** proof-led, once real published interviews exist in their segment ("I just recorded one with a {segment} in {state}").
  - **New free thing:** the review digest (section 4).
  - If no published interview exists in their segment when the trigger fires, the lead waits for one rather than recycling with the same angle.

### 12. Risks and open items

**Risks**

1. **The offer is FIX FIRST as v1 states it (5/10).** Apply the 3b fixes before the first send. They change the reward line, the offer block and the list filter, not the frameworks' structure.
2. **No look-alike proof.** Reply rates may be lower until real interviews exist. Mitigation: record warm-network interviews first, and lead with the terms and the questions.
3. **"Nothing hidden" against the business goal.** The terms line stays true only if three things hold: the interview call never pivots to a pitch, the referral-partnership talk happens only when the guest asks, and the page says plainly who runs it. If the setter or host ever pitches on the call, every email in this doc becomes the "pitch in a costume" it warns about (pain #10).
4. **Vanity-metric risk.** Interviews recorded are not the goal. If partnership conversations don't follow, fix the post-interview flow, not the cold email.
5. **Recording capacity.** If bookings outrun the host's calendar, the experience breaks and F7's scarcity line goes stale. Size volume to the calendar (section 7).
6. **The niche is broad.** Twelve segments in one campaign will hide which ones work. Read every number by segment.
7. **Regulated fields** (health, legal, finance, insurance, real estate licensing): no outcomes and no advice language, in email or in the interview edit.
8. **Generic inboxes.** Local businesses often show only info@ addresses. Writing to a named expert through a shared inbox weakens the relevance line. Those leads go in a lower-priority pool.
9. **The three questions read as generic.** If they could be sent to anyone in the category, the free thing is worthless and contradicts the thesis. QC enforces the swap test.

**Open items (must be true before launch)**

1. `[NEEDS: capacity]`: real daily send capacity, which picks a row in section 7.
2. `[NEEDS: TAM count]`: run the section 1 method by segment.
3. `[NEEDS: which segments the referral-partnership business most wants as partners]`: sets segment priority and the Spearhead list.
4. `[NEEDS: confirm the full interview and clips are delivered as files they own]`: decides pillar 1.
5. `[NEEDS: measured]`: positive, book and show rates, taken from the first 1,000-send verdict to size volume against the recording ceiling.
6. **Carried from v1:**
   - The pay line stays parked.
   - Confirm "a couple a day" for F7.
   - Switch the cal.com event.
   - The page video.
   - Fill in the sender roster flags.
   - Rename the page.
7. Write the review-pattern phrase set per segment, and record its measured pass rate (List & Signals).
8. Reword the close variation bank for the three-questions reward (Copy Chief). Then rerun QC on all 22 touches.
