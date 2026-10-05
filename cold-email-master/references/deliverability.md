# Deliverability: infrastructure, warmup and inbox health

**Verified 2026-10.** These rules change every year. Jay said most of his 2025 seven-hour setup talk is "scratch" now. Re-verify anything here older than six months before relying on it, and log what changed to the Obsidian vault.

Sources: [JAY] Lead Gen Jay, "Everything I Taught You About Cold Email Setup Is Wrong Now" (2026-10-01). It is sponsored by his own Inbox Insiders and community, so vendor picks are self-interested. [ERIC] Eric Nowoslawski, two videos (2026-08-30, 2026-09-10). [INSTANTLY] Instantly's Hormozi video (2026-07-17).

**House tooling (use it, don't rewrite it):**
- Mailboxes into Instantly, tags, warmup, credentials: the `winnr-instantly` skill and its repo CLI at `/Users/home/Desktop/cold email infrastructure`. Never ad-hoc curl. Always `--dry-run` first.
- DNS checks: `~/.hermes/profiles/ai-guy-go-to-market/skills/sales/email-deliverability-audit/scripts/dns_check.py`.
- Instantly health audits: Hermes `instantly-deliverability-audit` and `cold-email-weekly-rhythm`.
- Address verification: `verify-emails` (self-hosted Reacher) and `verify-leads`.
- **Never buy domains or mailboxes, or change DNS on a live domain, without Justin's explicit go-ahead.** The Deliverability Engineer specs and audits; purchases are Justin's call.

---

## 1. Domains

- **Never send cold email from the main domain.** Losing the main domain's email is the worst case in cold email. [JAY] [ERIC] [INSTANTLY]
- **Lookalike secondary domains** that read as the brand: `otterpr.com` → `otterpublicrelations.com`, `getotter.com`, `tryotter.co`. Searching the domain should lead to a real-looking site. [JAY]
- **`.com` first, `.co` second.** Avoid `.net`, `.xyz`, long multi-word domains, and expensive `.io`/`.ai`. Ugly domains scare prospects before they read a word. [JAY]
- **Registrar:** one with flat renewal pricing and a good API (Jay names Dynadot and Spaceship, about $10 to $11 a `.com` a year at renewal too). Avoid registrars with first-year bait pricing. [JAY]
- **Buy early.** Domain age builds reputation, and it matters more now. [JAY] [ERIC]
- **Aged domains: the sources disagree.**
  - Jay: no good cheap source, about $50 each, unproven, and they break brand continuity. Only worth trying if you struggle to land in Microsoft inboxes.
  - Eric: bought closeout `.com` aged domains at about $5 each; "age matters 100%"; with 3 to 4 days of warmup they can go full tilt.
  - **House rule:** brand-sensitive campaigns (anything under Justin's or a client's name) use lookalike domains bought early. Brand-light sprint campaigns may use aged domains. The Deliverability Engineer states which and why.

## 2. Name servers and blacklists

- **Don't park many cold domains behind one Cloudflare account.** Every Cloudflare account shares a name-server pair; when SURBL sees many cold-email domains behind one pair, it flags them. Keep domains on the registrar's own name servers. At agency scale, isolated custom name servers (e.g. Route 53). [JAY]
- Blacklists that matter: Spamhaus, SURBL, SORBS among hundreds, not equally weighted. Check regularly. [JAY]
- Note: Google said publicly (per Eric, late Aug 2026) that it does not use third-party lists like SORBS and relies on its own spam policies. Third-party lists still affect other receivers. [ERIC]

## 3. DNS records (every sending domain)

- SPF, DKIM, DMARC and correct MX. Generate DKIM in the mailbox provider's admin (Google Admin for Workspace). [JAY]
- Verify with `dns_check.py` (house) and a blacklist and DNS checker. Aim for all green.
- DMARC starts at `p=none` with reporting, then tighten once clean.

## 4. Forwarding the sending domain: the sources disagree

- **Redirect / forward** (`getbrand.com` → `brand.com`): the old standard.
  - Jay: following a redirect from a cold domain is now a red flag to receivers; a **domain masking proxy** (serves the real site's content on the cold domain) is the level-up. Redirects are still "pretty much okay" at small scale.
  - Eric: some third-party blacklists are starting to flag the forwarding pattern, but ClickUp forwards every sending domain with zero issues. Optional fix: a simple microsite per domain (Claude Code plus Railway).
- **House rule:** forwarding is acceptable under about 20 domains. Above that, or if placement drops, move to a masking proxy or microsites. Record the choice in the doc.

## 5. Mailboxes

- **Diversify providers.** Every year one provider has a wave of bans. Start with Google, add SMTP and Microsoft. [JAY]
- **Google Workspace:** strongest deliverability right now. Resellers at about $3.50 a user a month are the same product as Google's $8.40 list price. [JAY]
- **Private SMTP:** hardest to inbox. Avoid "unlimited mailboxes" flat-rate offers and anything under $1 a mailbox a month (bad IPs). [JAY]
- **Microsoft:** a cheap tenant loophole exists (about $30 to $50 per 50 mailboxes); nobody knows how long it lasts. Send fewer per mailbox and watch warmup closely. Traditional Microsoft mailboxes follow Google-like rules. [JAY]
- **Don't buy mailboxes from your sequencer.** They lock you in, and pre-warmed ones come with someone else's name and domain. [JAY]
- **Real person on every inbox:** a real first name, Google profile photo where possible, a LinkedIn that exists. [JAY]
- Google legacy panels (old free G Suite): risky, can be off-boarded on 30 days' notice. Jay uses them for testing and real company mail, not cold sending. Not house practice.

## 6. Volume per inbox and domain

| Rule | Number | Source |
|---|---|---|
| Cold sends per inbox per day | about 30 | [ERIC] [INSTANTLY] |
| Inboxes per domain | 3 (up to 4) | [JAY] |
| Sends per domain per day | under 100 | [JAY] |
| Insurance capacity warming on the side | +50% | [ERIC] |
| Example | 3,000/day = 100 inboxes on 34 domains + 50 insurance inboxes | [ERIC] |

## 7. Warmup

- A new mailbox sends to spam without warmup. [JAY]
- **Lookalike domains:** at least 2 weeks, really 4 weeks, of high-quality warmup before cold sends. [JAY] (Aged domains: 3 to 4 days, per Eric.)
- **Slow ramp on.** Never 0 to 50 on day one. Ramp warmup daily until warmup volume equals the planned cold volume, then keep warmup running. [JAY]
- **Warmup reply rate:** as high as the tool allows (Jay suggests up to about 25%). [JAY]
- **Pool quality matters most.** Warmup is a shared pool; cheap "free unlimited warmup" tools poison it. Use Instantly's premium pool or an established sequencer's pool. [JAY]
- Warmup health must read 99 to 100% before an inbox goes live. [INSTANTLY] [ERIC]
- **Always-warm inventory:** keep spare inboxes warming at all times so a burned inbox is swapped the same day. [ERIC]

## 8. The five-level inbox health process [ERIC]

Most people stop at levels 1 and 2. The house runs all five, automated.

| Level | Check | Rule | Cadence |
|---|---|---|---|
| 1 | Warmup reputation score | Distrust anything under 99 to 100%. Pull an inbox at about 92% out of campaigns. | Daily |
| 2 | Seed inbox placement test | Directional only (seeds never mark spam). | Daily |
| 3 | Real reply rate per inbox and domain | This week and two weeks ago. **≥100 sends and under 1% reply rate: pull it.** | Weekly (Friday) |
| 4 | Auto-responder seed list | Keep a list of addresses that auto-reply (OOO and "no longer monitored" bounces harvested from all campaigns; Eric keeps about 10,000). Send to it: expect about 80% to auto-reply. **Under 60%: kill the inbox or domain.** Use Claude to read the replies and harvest new auto-responders. | Weekly (Saturday) |
| 5 | Always-on "likely positive" campaign | Run each inbox on something that reliably gets positive replies (candidate sourcing, partnership or podcast-guest outreach). It adds real engagement and is the baseline: if its reply rate drops on one inbox, that inbox is sick. | Always on |

**Drop alerts:** a sudden fall (e.g. 1.5% reply rate to 0.2%) means suspect a spam trap first and pull the affected domains now; content fingerprinting second (fix with spintax). [ERIC]

When an inbox fails: cancel it from campaigns, cancel its subscription, swap in an insurance inbox. No downtime. [ERIC]

## 9. Lists and bounces

- Verify every address before upload. Bounce rate target under 2%; pause the campaign above 3%. (House kits and the quickstart use these gates.)
- Catch-all domains need catch-all verification, not a guess. [ERIC]
- Spam traps sit inside B2B databases. Clean lists, send only to real prospects. [JAY]

## 10. Sending settings (Instantly)

- Plain text, open tracking **off**, click tracking off (no links in framework emails anyway).
- Unsubscribe header/link on for every step. Postal address in footer for US recipients (see `copy-rules.md` §13).
- 22 steps for Standard mode: odd steps new emails with their own subject, even steps replies in thread. Any reply stops the sequence.
- Stop-on-reply on. Stop for the whole company domain on reply where the sequencer allows.
- Spintax rendered by Instantly (`{{RANDOM | ... }}`); confirm in the preview that no single-brace `{placeholder}` survives.
- Send windows in the lead's time zone, business days.

## 11. Pre-launch infrastructure gate (the Deliverability Engineer signs this)

- [ ] Sending domains are lookalikes (or declared aged), not the main domain, `.com`/`.co`.
- [ ] Domains on registrar name servers, not one shared Cloudflare pair.
- [ ] SPF, DKIM, DMARC, MX pass on every domain (`dns_check.py` output attached).
- [ ] Forwarding vs masking proxy vs microsite decided and recorded.
- [ ] 3 inboxes per domain, real names, photos where possible.
- [ ] Warmup 99 to 100% on every live inbox; lookalikes warmed 2 to 4+ weeks.
- [ ] Capacity math matches the Attack Plan; 50% insurance inboxes warming.
- [ ] List verified; expected bounce under 2%.
- [ ] Unsubscribe on, postal address in place for US, open and click tracking off.
- [ ] Seed placement test run; auto-responder seed list ready for the first weekly check.
- [ ] Likely-positive baseline campaign live on every inbox, or a reason it isn't.
- [ ] Weekly rhythm scheduled (daily score and seed, Friday reply-rate pull, Saturday auto-responder test).
