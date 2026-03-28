# Transcript: Scanning Ashby Job Boards for Remote Developer Positions

**Task:** Find remote software developer positions on Ashby-hosted job boards for Yoad, a fresh CS grad looking to work remotely from Israel.
**Date:** March 28, 2026

---

## Approach

I used a multi-pronged strategy:

1. **Web searches** on Google for `site:jobs.ashbyhq.com` with various keyword combinations (remote, junior, new grad, entry level, Israel, EMEA, Europe, worldwide, etc.)
2. **Direct page fetching** of individual job postings via WebFetch to extract detailed descriptions, location requirements, and Israel eligibility
3. **Ashby Public API** (`api.ashbyhq.com/posting-api/job-board/{company}`) to programmatically scan dozens of company job boards for matching positions
4. **Third-party job aggregators** (Himalayas, CareerVault) for additional context when Ashby pages required JavaScript rendering

---

## Step-by-Step Actions

### Phase 1: Initial Web Searches
- Searched "Ashby job board remote software developer entry level 2026"
- Searched "site:jobs.ashbyhq.com remote software engineer junior 2026"
- Searched "ashbyhq.com remote software developer Israel entry level"
- Found initial leads: Quora (new grad, remote), Checkly (junior, remote), BRM (entry level), Handshake, TENEX.AI, Zapier, Lottie

### Phase 2: Fetching Job Details
- Fetched Quora SE New Grad (Data Infra) -- remote but Israel NOT eligible
- Fetched Quora AI Engineer New Grad (Poe) -- remote but Israel NOT eligible
- Verified Quora's eligible countries at careers.quora.com/eligible-countries -- **Israel is NOT listed**
- Fetched BRM Entry Level SE -- San Francisco on-site only, not remote
- Fetched Checkly Junior Software Developer -- page needed JS, used web search for details. Found it targets Americas timezone
- Fetched Replit New Grad -- hybrid Foster City CA, USA only
- Fetched Fieldguide All Levels -- remote but USA only
- Fetched Foundry for Good -- Philippines only
- Fetched Meshy New Grad -- USA only
- Fetched Eventual New Grad -- SF on-site, 4 days/week
- Fetched Continue New Grad -- SF on-site
- Fetched Profound New Grad -- NYC or SF on-site
- Fetched Keragon Fullstack -- Greece only
- Fetched Whatnot New Grad -- must be near SF/LA/Seattle hub
- Fetched Decagon New Grad -- SF or NYC, in-person 5 days/week
- Fetched Abridge All Levels -- SF or NYC hybrid, USA only
- Fetched Mechanize Junior SE -- SF on-site, $300K salary

### Phase 3: Broadening the Search
- Searched for EMEA/Europe/Israel-specific positions
- Searched for UTC+2/UTC+3 timezone positions
- Found Checkly hires in UTC-3 to UTC+3 (covers Israel) but only senior roles currently
- Found WunderGraph has EMEA remote positions (senior)
- Found EverAI has Europe/EMEA remote positions
- Found Camunda has EMEA remote positions (senior)

### Phase 4: Ashby Public API Scanning
Systematically queried the Ashby posting API for 70+ companies:

**Companies with relevant remote/EMEA positions found:**
- **Ashby** -- Design Engineer EU (Remote Europe, EUR 141K-226K), Engineering Manager EU
- **Deel** -- Full Stack Engineer EMEA (multiple variants), Senior Full Stack Engineer EMEA
- **Quora** -- 3 new grad roles (but Israel not eligible)
- **Zip** -- Senior Technical Support Engineer in Tel Aviv, Israel (5-6yr exp needed)
- **Supabase** -- Multiple remote roles including EMEA support engineers, SDK engineers, platform engineers
- **G2i** -- Multiple remote positions, AI Engineer (Europe), FullStack Developer (Remote)
- **PostHog** -- Multiple remote engineering roles (but found to be US-only when checked)
- **Resend** -- Design Engineer (Europe/Remote)
- **Linear** -- Senior/Staff Fullstack Engineer (Europe)
- **WunderGraph** -- Senior Design Engineer (EMEA), Senior Full Stack Engineer (EMEA)
- **LangChain** -- Customer Engineer (Europe)
- **Cursor** -- Technical Support Engineer (Remote, no location specified)
- **Firecrawl** -- Multiple remote roles (Americas timezone)
- **Weaviate** -- Developer Advocate Intern (Europe)

**Companies checked with no matching positions:**
Suno, Zapier (API returned no data), n8n (senior only), Notion (SF only for new grads), Sentry (API returned no current new grad listings), Harvey (no data), Sierra (on-site only), Cloudflare, GitLab, Stripe, Snyk, Wiz, Figma, Vercel, PlanetScale, Neon, Turso, Deno, Bun, Val Town, Retool, Appsmith, ToolJet, Metabase, Cal.com, Highlight, Axiom, Tinybird, Knock, Novu, Courier, Plain, Unkey, Hoppscotch, Gitpod, Coder, Depot, FlightControl, Coolify, Windmill, Temporal, Modal, Baseten, Replicate, Together AI, Mistral, Cohere, Hugging Face, Pinecone (US remote only), Qdrant, Chroma, Zilliz

### Phase 5: Deep-Diving Key Positions
- Fetched Deel Full Stack Engineer (EMEA) -- 4+ years required, Israel explicitly excluded from one variant but EMEA listed for another
- Fetched Deel Full Stack Engineer (React, Node.js) EMEA -- EMEA location, Israel potentially eligible since Middle East is in EMEA
- Fetched Supabase Support Engineer (EMEA) -- 3+ years, European time zones required
- Fetched Supabase Database Support Engineer (EMEA) -- 6+ years, senior role
- Fetched PostHog Product Engineer -- USA only
- Fetched G2i AI Engineer (Europe) -- EUR 80K-120K + equity, 2-5+ years, founding role
- Checked Ashby's own EU engineering positions -- senior IC level
- Fetched Zip Israel position -- Senior Technical Support, 5-6 years exp, Tel Aviv

---

## Key Findings

1. **Israel eligibility is the main blocker.** Most remote positions on Ashby are either US-only or limited to specific country lists that don't include Israel.

2. **EMEA is the best keyword.** Companies that say "EMEA" (Europe, Middle East, Africa) technically include Israel. Deel and Supabase are the strongest leads.

3. **Junior/new grad + remote + Israel is an extremely narrow intersection.** No positions found that simultaneously satisfy all three criteria.

4. **Most new grad roles are on-site.** Replit, Benchling, Whatnot, Decagon, Continue, Eventual, Profound, Mechanize -- all require US presence.

5. **Quora is the biggest "close but no" -- they have perfect new grad remote roles but explicitly exclude Israel from their eligible countries.**

6. **Zip has an Israel office (Tel Aviv)** but only a senior support role currently.

7. **The best realistic strategy** is to target EMEA remote roles at companies like Deel, Supabase, G2i, WunderGraph, and Ashby itself, even if current openings are above entry level -- these companies have the legal infrastructure to hire in Israel-adjacent timezones.

---

## Tools Used
- WebSearch: 15+ queries with various keyword combinations
- WebFetch: 25+ individual job page fetches
- Ashby Public API: Programmatic scan of 70+ company job boards
- Bash: API data processing with Python for structured extraction

## Limitations
- Many Ashby job pages are single-page applications requiring JavaScript, making direct content extraction impossible for some listings
- Some companies' Ashby API endpoints returned no data (may use different board names)
- Job listings change rapidly; positions may have opened or closed during the scan
- Could not verify Israel eligibility for every position -- some require direct inquiry to the company
