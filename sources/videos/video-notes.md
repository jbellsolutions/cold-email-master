# Video notes (extracted 2026-10-04)

Condensed extractions from the four cleaned transcripts in this folder. The transcripts are YouTube auto-captions (`en-orig` track, fetched with yt-dlp, cleaned with `clean_vtt.py`), so tool names are sometimes garbled; likely corrections are marked "(sic)". These notes feed `cold-email-master/references/*`. Vendor names appear here for the record only. Justin's no-paid-enrichment rule means the skill keeps the methods, not the vendors.

---

## 1. Lead Gen Jay: "Everything I Taught You About Cold Email Setup Is Wrong Now"
32:46 · 2026-10-01 · TG7ZAHD5_ck · infrastructure only · sponsored by his own Inbox Insiders and community.

- **Three pillars:** infrastructure, copy, list. One wrong DNS record sends everything to spam.
- **Trust is the first hurdle:** a real founder name, a real LinkedIn, sending domains that look like the brand.
- **Domains:** never the main ("sacred") domain. Lookalikes (`otterpublicrelations.com`, `get___`, `my___`). Use `.com`/`.co`; avoid `.net`, `.xyz`, long names, pricey `.io`/`.ai`. Flat-renewal registrars with APIs (Dynadot, Spaceship, about $10 to $11). Buy in bulk early, because age builds reputation. Aged domains: no good cheap source, about $50, unproven, only if Microsoft placement is a struggle.
- **Name servers:** stop putting all domains on Cloudflare. A shared NS pair got flagged by SURBL. Use registrar NS, or isolated Route 53 at scale. Blacklists: Spamhaus, SORBS, SURBL.
- **DNS:** SPF, DKIM (generated in Google Admin), DMARC, MX. Check with a DNS and blacklist checker until all green.
- **Masking proxy over redirect:** a redirect from a cold domain is now a red flag. A proxy serves the real site's content. Redirects are still OK at small scale.
- **Mailboxes:**
  - Google Workspace is strongest now ($3.50 reseller vs $8.40 direct, same product).
  - Private SMTP is hardest; avoid anything under $1 a mailbox or "unlimited".
  - Microsoft has a cheap tenant loophole of unknown lifespan.
  - Diversify providers.
  - Don't buy mailboxes from the sequencer: lock-in, and someone else's name.
  - Legacy G Suite panels are risky; he uses them for testing.
- **Volume:** under 100 a day per domain, 3 to 4 mailboxes per domain.
- **Warmup:** at least 2 weeks, really 4. Pool quality matters (Instantly premium, Email Bison, SmartLead). Avoid free-unlimited-warmup tools. Use slow ramp, warmup volume equal to cold volume, and a high warmup reply rate (about 25).
- **Google profile photo** on every inbox.
- **AI:** Claude Code plus registrar APIs can run the entire setup (he manages 12,502 domains this way).
- **Rules change yearly.** Stay in a community.

## 2. Eric Nowoslawski: "I speedran cold email from 0 to $50k in 30 days"
8:09 · 2026-09-10 · -LjvwKOIH9Y · case study, copy withheld.

- **Results:** 106k emails in under 30 days. 373 positive replies (1 per about 286 sends). 62% booked, so 231 meetings. Paid per attended call, about $50k.
- **Core:** "Cold email absolutely still works. You just need an offer that can really rip." Weaker offers need more signal-based targeting.
- **Targeting:** US CEOs, 25+ employees, 5+ years in business, more than 80% of the team in the US. Pure volume. A 3-sentence email, about 20 spintax subject variants, an unsubscribe line.
- **Always-warm inventory** of generic inboxes, so a blitz can start immediately (also insurance). Aged closeout `.com` domains at about $5 went live after 3 to 4 days of warmup. The trade-off is brand control.
- **Lists:** layered several data vendors (benchmarked against a 10k Sales Nav scrape) plus catch-all verification (80 of 500 positives would have been lost without it). Clay qualification. *Vendors excluded from the skill; methods kept.*
- **Reply cadence (credits Oren Klaff), run by an AI reply bot tied to the calendar API:**
  1. Answer the question, then offer 2 specific times plus "or book on my calendar link".
  2. +1 day: "Hey, I lost both of those times. Do you want to book with my calendar link, or I'm available at this time and this time?"
  3. AI researches the company and writes a one-line, company-specific reason the call is worth it.
  4. Lost-times again with new times.
  5. A commissioned warm caller.
- **Tools:** Claude Code plus a CLI built the campaign; SmartLead sent.

## 3. Eric Nowoslawski: "Give Me 25 Minutes and I'll Give You 7 Years of Cold Email Advice"
25:44 · 2026-08-30 · H-dot6onaIw.

- **Diagnose in order:** infrastructure → list → offer and copy. Infrastructure and list are "hard science"; spend the creative effort on offer and framing. "Campaigns work quickly or they don't."
- **Cold-traffic offer, five pillars:**
  1. Make money (or a categorical 80 to 90% saving, never 10%).
  2. Relevant signals paired with the list (restaurants with bad parking lots on Maps).
  3. Look-alike case studies.
  4. An easy-yes next step (a dental free sample cost $40 a lead cold vs $300 on Facebook).
  5. Not Google- or ChatGPT-able (bookkeeping reframed: "the IRS sent one return to 20 firms, got 19 strategies back").
- **Verdicts:** none before 1,000 sends. 0 positives means kill it; 1 positive means scale to 3,000. 300 sends is no data.
- **Testing:** always test. Images: plain text got 70 seen and 0 replies; an image got 40 seen and 2 replies, so send the image. Email 1 normally gets about 99% of positives. Use an AI thought partner with results and sales calls each week.
- **Personalisation:** what you'd conclude after about 10 minutes of manual research. No "loved your website", no "CEO for 2 years".
- **Lists:**
  - Work backwards from where the buyer shows up (LinkedIn, Google Maps, hard niches).
  - Build seed-list lookalikes from the do-not-contact list.
  - Score homepages against the ICP with a cheap model ("no excuse for a bad company list").
  - Benchmark vendors against a live Sales Nav scrape; pay under about 2 cents a contact.
  - Email permutations plus validation find 60 to 70%; pay for a finder only on the rest.
  - Don't guess 28 permutations.
- **Five-level inbox health:**
  1. Warmup score (distrust under 99 to 100%, pull at about 92%).
  2. Seed test (directional only).
  3. Weekly reply rate per inbox and domain (≥100 sends and under 1% means pull it).
  4. Auto-responder seed list of about 10k OOO and "no longer monitored" addresses (expect 80% back, under 60% means kill it).
  5. An always-on "likely positive" campaign for engagement and as a baseline.
- **Automation schedule:** spam tests daily, reply rate Friday, auto-responder Saturday. Alert on sudden drops (spam trap first, fingerprinting second).
- **Capacity:** 30 a day per inbox (3,000 a day = 100 inboxes) plus 50% insurance warming. Free warmup in beta at Hypertide (sic); new inboxes live in 24 to 48 hours.
- **Spintax:** 0.3% to 1.2% reply rate the day it was added. Spin greeting, body, signature and unsubscribe at **word level**.
- **Forwarding:** some third-party lists are flagging the forward pattern. ClickUp forwards with zero issues. Microsites are an option. Google says it ignores third-party lists like SORBS.
- **Never send from the main domain.**
- "Claude Fable" is named for list building. That is the real model name, not a caption error.

## 4. Instantly: "Alex Hormozi's Cold Email Strategy for 2026"
27:31 · 2026-07-17 · j5uPj9A7zlE · a compilation; [H] marks Hormozi, [N] marks the narrator.

- **Why outbound** [H]: the beginner's play. One channel, no audience needed. Gym Launch got about half its sales from outbound.
- **Profiles are the new website** [H]: post 2 to 3 times a week on the outreach channel and link socials in the signature.
- **The list is king** [H]: a great email to the wrong list is worthless. [N]: define the buyer, build the list, then write. Smaller, specific lists get more replies. Segment (e.g. realtors at Compass). Signals: job posts, recent posts, traffic surges, expansion; mention them.
- **Lead magnet** [H]: the biggest response lift is an insane lead magnet, operationalised (1% to 3% triples throughput). [N]: give away what others charge for, not a Loom, PDF or call. Idea bank by agency type (in `strategy-playbook.md` §3). Put the offer at the end.
- **Copy constraints** [H]:
  1. Third-grade reading level (+50% response).
  2. Short; cold emails rarely more than half a page. [N]: about 80 words.
  3. Exact numbers, not ranges ("17.3 members in the first 30 days").
  4. Never look mass-sent. [N]: read it aloud.
- **Example** [N] (reconstructed from captions): "Hi John, Saw XYZ company is running ads right now. That gets pricey fast and it stops the second you stop paying. We help SaaS teams book demos with outbound, no ad budget needed. One client swapped $8,000 a month in ads for outbound. They booked 22 demos in 30 days." Structure: signal → problem → solution → named exact-number proof → offer last.
- **Competitor play** [H voicemail, N email adaptation]: the subject is the prospect's nearest competitor (an AI column), and the body says "Companies like {competitor} are booking demos with cold email instead of burning budget on ads. We just did 22 demos in 30 days for one of them. Want the exact setup?" Untested; it is a flagged test in the skill.
- **Follow-up levers** [H]: availability (15-minute slots, 5-minute gaps), speed to contact (minutes), volume (10x), reply on their channel. Contact multiple times, multiple ways, quickly. Recycle non-repliers in 3 to 6 months with a new angle; a 2,000-person list doesn't need replacing.
- **Technical** [N]: never the main domain, multiple domains, about 30 a day per inbox, warmup at 100% before sending. Instantly's reply agent handles fast responses.
