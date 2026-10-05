# Strategy Playbook: how to attack a market with cold email

The Strategist reads this before writing the Attack Plan (master-template §0). Copy cannot fix a bad offer or a bad list. Source tags as in `copy-rules.md`.

---

## 1. The three levers, and the order you fix them in

Every cold email result comes from three things: **how you send (infrastructure), who you send to (list), what you say (offer and copy).** [ERIC] [JAY]

When a campaign underperforms, diagnose in this order, and do not touch copy until the first two are clean: [ERIC]

1. **Infrastructure.** Warmup health 99 to 100%, seed test good, reply rate over 1% on the inbox, auto-responder return over 80%, the "likely positive" baseline campaign still replying. (Detail in `deliverability.md`.)
2. **List.** Pull 20 random rows and check them by hand: right title, right company type, right size, real signal present. Bad company lists have no excuse: score homepages against the ICP.
3. **Offer, then framing, then copy.** Infrastructure and list are hard science. Put all creative effort here.

"Campaigns work quickly or they don't." If infrastructure and list are right and it still fails, change the offer radically, not the subject line. [ERIC]

## 2. The cold-traffic offer (score every offer before copy)

A warm-traffic offer (people come to you) is not automatically a cold-traffic offer (you go to them). [ERIC] Score the offer 0 to 2 on each pillar. **Under 6 of 10, or any 0 on pillar 1 or 4: stop and fix the offer before writing frameworks.** The Strategist writes the fix.

| # | Pillar | 2 = strong | Fix if weak |
|---|---|---|---|
| 1 | **Makes them money** | A clear make-money frame, or a categorical saving (about 80 to 90%) | Reframe save-time and save-money as make-money. Nobody moves for a 10% discount. |
| 2 | **Signal paired with the list** | The list is filtered on a signal that makes the offer relevant now | Filter the list (restaurants with visibly bad parking lots, not all restaurants). This turns a warm offer into a cold one. |
| 3 | **Look-alike proof** | A real result for a company that looks like them | Use the closest true proof type; if none exists, lead with terms and the free thing, never invent. |
| 4 | **Easy yes** | The next step is tiny and valuable on its own (a sample, an audit, a map) | Shrink the ask. A dental supplier's free sample cost $40 a lead by cold email vs $300 on Facebook. [ERIC] |
| 5 | **Not Google-able** | They cannot get this from ChatGPT or a search | Reframe commodity services with a surprising true angle (the bookkeeping firm: the IRS sent one return to 20 firms and got 19 answers back; we'll look at yours). |

Also true for every offer:
- **Humour and copy amplify; they cannot rescue.** "Without the right offer, all of the other stuff won't matter." [BUCHAN]
- **Hormozi's priority:** the biggest response lift comes from "an insane lead magnet, then operationalising it." Going from 1% to 3% triples throughput. [HORMOZI]

## 3. The free thing (lead magnet)

Every doc names one free thing. Rules:
- **Give away what other people charge for**, not "something so good you could charge for it". They already have a price anchor, so saying no feels foolish. [INSTANTLY, from HORMOZI]
- Real, specific to them, cheap for us to produce from research, worth having even if they never buy. [HOUSE]
- Not a Loom, a PDF case study, or "a call". [INSTANTLY]
- Pick one thing from the early delivery process and make it efficient to fulfil, so it can go out the same day as the reply. [HORMOZI]
- Lives in the free-thing framework (back half) and Closer 2.

Idea bank by business type [INSTANTLY]: SEO, a Google Business Profile tune-up. Web, a ready landing page. Ads, the 5 best creatives in their niche. Video, one short-form edit. Lead gen, 500 verified prospects. Content, 30 days of post ideas with 5 written. Email, a welcome or abandoned-cart flow. CRO, a checkout teardown with the 3 biggest fixes. PPC, a wasted-spend audit with the keywords burning budget. Referral partnerships, a map of their likely partners in town. Interviews, three questions written just for them.

## 4. The list is king [HORMOZI] [ERIC]

- **Define the buyer first, then build the list, then write to the list.** Never pull a big list and then work out what to say.
- A great email to the wrong list is worthless. A smaller, more specific list gets more replies.
- **Segment so the email can be specific** (realtors at one brokerage, gyms with one location, CEOs at 25+ employee firms with 80%+ of staff in the US).
- **Work backwards:** where does this buyer show up? LinkedIn (SaaS, finance, professional services). Google Maps (local businesses). Association directories, license boards, review sites (trades, regulated fields).
- **Signals worth filtering on:** hiring (job posts), new location or expansion, running ads, a review pattern, a recent post or launch, a job change in the last 90 days, website traffic surge, funding. Mention the signal in the email; it is the reason you're writing. [HORMOZI] [BUCHAN]
- **Seed-list lookalikes:** start from existing customers (the do-not-contact list), pull their industries, keywords, headcount, and find more like them. [ERIC]
- **Score company lists with AI:** scrape each homepage, check it against ICP keywords, cut the misses. [ERIC]
- **Email finding:** guess the common patterns (first@, first.last@, flast@, last@) and verify each before paying for anything. Guessing plus verifying finds about 60 to 70%. Do not guess 28 permutations. Catch-all domains need catch-all verification. [ERIC]
- **Verify every address.** Spam traps are seeded in B2B databases; one can blacklist a domain. [JAY]

**House rule (Justin, absolute): no paid enrichment SaaS** (Clay, Apollo, Hunter, Ocean, ZoomInfo and the like). The videos name many vendors; we keep their methods and execute in-house: `lead-warehouse`, `revyops-lead-sourcing`, `apify-enrich`, browser-use, Orgo, Composio, and `verify-emails` / `verify-leads` (self-hosted Reacher) for verification. The List & Signals agent owns this.

## 5. Campaign modes

| Mode | When | Shape |
|---|---|---|
| **Standard (default)** | Any offer with a doc behind it | 22 touches per lead: 10 frameworks, a follow-up each, 2 closers. Framework every 6 days. About two months. [HOUSE, Sept 3 2026 policy] |
| **Sprint** | A short window, a strong offer, a wide TAM, brand-light | Touch 1 (the lead framework, spun hard) plus its follow-up, then the reply cadence does the work: fast reply, 2 times plus link, "lost those times", a company-specific reason, then a caller. Eric ran this to 106k sends, 373 positives, 231 meetings in under 30 days. [ERIC] |
| **Spearhead** | The top-ranked accounts (one per town, dream clients) | Standard sequence plus something made just for them (Buchan's "do something special": a direct-mail letter, a custom map or sketch), then an email naming it. [BUCHAN] |

Sprint still needs a frameworks doc (it uses the lead framework and the reply playbook); it skips frameworks 2 to 10.

## 6. Volume and capacity math

- **Volume is the lever most people under-use.** "10x what feels viable." 100 contacts won't change your life. [HORMOZI]
- **Per inbox:** about 30 cold sends a day. **Per domain:** 3 inboxes, under 100 sends a day. [ERIC] [JAY] [INSTANTLY]
- **Inboxes needed** = daily send target / 30. Domains = inboxes / 3.
- **Insurance:** keep 50% extra capacity warming on the side, so a burned inbox is swapped, not mourned. [ERIC]
- **Always-warm inventory:** a fraction of spend keeps generic inboxes warming at all times, so a sudden offer can launch the same week. [ERIC]
- Example: 3,000 sends a day = 100 inboxes on 34 domains, plus 50 insurance inboxes on 17 more domains.
- Standard mode load: each lead gets 22 touches over about 60 days, so daily send volume = new leads per day x roughly 22 spread across the window. Work out new leads per day from capacity, not the other way round.

## 7. Testing and verdicts [ERIC]

- **No verdict before 1,000 sends** on a campaign or variant. 300 sends is no data.
- **1,000 sends, 0 positive replies:** kill it. Change the offer or the list, not the subject.
- **1,000 sends, 1 positive:** scale to 3,000 before judging.
- **Always be testing.** No rule here is gospel, including these. Test one variable at a time: offer framing, lead framework, subject set, close type, image vs none, competitor subject.
- Feed results, sales-call notes and company context to an AI thought partner each week for the next test. The Analyst does this and logs it to the Obsidian vault.
- Positive reply is not the finish line: track booked, showed, qualified, closed. A great reply rate with no shows is a sales-process problem.

## 8. After the sequence

- **Recycle non-responders after 3 to 6 months** with a new angle and, ideally, a new free thing. A 2,000-person list does not need replacing. [HORMOZI] Buchan says a month or two; house default is 3 months. [BUCHAN]
- "Not now, try me in September": set the date, keep it.
- Never re-mail anyone who said no or unsubscribed.

## 9. Trust before the first send

- **Profiles are the new website.** Prospects check the sender. Real founder or real person, real LinkedIn, posting 2 to 3 times a week on the channel you do outreach on. Link socials in the signature where the naming mode allows. [HORMOZI] [JAY]
- Sending domains look like the brand (lookalike, `.com` or `.co`) and lead to a real-looking site. [JAY]
- Google profile photo on Google inboxes. [JAY]

## 10. Speed and availability (the reply side is strategy too) [HORMOZI] [ERIC]

- **Speed to contact:** answer replies within minutes. The reply-setter agent and the house reply templates exist for this.
- **Availability is the biggest throughput driver:** lots of slots (15-minute slots with 5-minute gaps).
- **Reply on their channel.** If they text, text. If they call, call.
- **Multi-channel:** contact multiple times, multiple ways, quickly. Find the LinkedIn and phone for the positives.
- Full cadence in `reply-playbook.md`.

## 11. What the Attack Plan must answer (the Strategist's output)

1. Who exactly (ICP and hard filters), and how many exist (TAM estimate with the method).
2. Which signals we filter on, and how the List & Signals agent gets them in-house.
3. Offer score on the 5 pillars, with fixes. Go or fix-first.
4. The free thing, and how it is fulfilled the same day.
5. Proof on file (exact numbers, true today) and what may not be claimed.
6. Campaign mode (Standard, Sprint, Spearhead tier) and why.
7. Capacity math: sends per day, inboxes, domains, insurance, new leads per day.
8. Testing plan: what is tested first, the verdict thresholds, who reads results.
9. Reply plan: who answers, how fast, the calendar, the caller if any.
10. Trust readiness: sender profile, LinkedIn, domains, photo.
11. Recycle plan and the date it triggers.
12. Risks and open items (what must be true before launch).
