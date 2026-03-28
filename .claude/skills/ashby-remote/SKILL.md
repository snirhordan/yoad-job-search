---
name: ashby-remote
description: Scan all Ashby-hosted companies worldwide for remote software development positions. Use when user wants remote jobs, worldwide remote positions, or asks about Ashby job listings.
allowed-tools: WebFetch
---

# Ashby Remote Job Scanner

Scan Ashby-powered companies for remote software development positions worldwide.

By default, scan the **Top 15** companies most likely to have junior-friendly remote roles. If the user asks for a broader scan, use the extended list. If they say "all", scan everything — but warn it may take a while.

## Top 15 Companies (Default Scan)

These companies are known for remote-friendly hiring and developer roles:

| Company | Endpoint |
|---------|----------|
| linear | https://api.ashbyhq.com/posting-api/job-board/linear |
| supabase | https://api.ashbyhq.com/posting-api/job-board/supabase |
| deel | https://api.ashbyhq.com/posting-api/job-board/deel |
| cursor | https://api.ashbyhq.com/posting-api/job-board/cursor |
| posthog | https://api.ashbyhq.com/posting-api/job-board/posthog |
| snyk | https://api.ashbyhq.com/posting-api/job-board/snyk |
| clickup | https://api.ashbyhq.com/posting-api/job-board/clickup |
| notion | https://api.ashbyhq.com/posting-api/job-board/notion |
| render | https://api.ashbyhq.com/posting-api/job-board/render |
| retool | https://api.ashbyhq.com/posting-api/job-board/retool |
| railway | https://api.ashbyhq.com/posting-api/job-board/railway |
| clerk | https://api.ashbyhq.com/posting-api/job-board/clerk |
| neon | https://api.ashbyhq.com/posting-api/job-board/neon |
| vanta | https://api.ashbyhq.com/posting-api/job-board/vanta |
| workos | https://api.ashbyhq.com/posting-api/job-board/workos |

## Extended List (use when user asks for "more" or "all")

| Company | Endpoint |
|---------|----------|
| openai | https://api.ashbyhq.com/posting-api/job-board/openai |
| cohere | https://api.ashbyhq.com/posting-api/job-board/cohere |
| ramp | https://api.ashbyhq.com/posting-api/job-board/ramp |
| ashby | https://api.ashbyhq.com/posting-api/job-board/ashby |
| replit | https://api.ashbyhq.com/posting-api/job-board/replit |
| drata | https://api.ashbyhq.com/posting-api/job-board/drata |
| motion | https://api.ashbyhq.com/posting-api/job-board/motion |
| fullstory | https://api.ashbyhq.com/posting-api/job-board/fullstory |
| deepgram | https://api.ashbyhq.com/posting-api/job-board/deepgram |
| hightouch | https://api.ashbyhq.com/posting-api/job-board/hightouch |
| benchling | https://api.ashbyhq.com/posting-api/job-board/benchling |
| pinecone | https://api.ashbyhq.com/posting-api/job-board/pinecone |
| runway | https://api.ashbyhq.com/posting-api/job-board/runway |
| perplexity | https://api.ashbyhq.com/posting-api/job-board/perplexity |
| scaleai | https://api.ashbyhq.com/posting-api/job-board/scaleai |
| revenuecat | https://api.ashbyhq.com/posting-api/job-board/revenuecat |
| braintrust | https://api.ashbyhq.com/posting-api/job-board/braintrust |
| greptile | https://api.ashbyhq.com/posting-api/job-board/greptile |
| podium | https://api.ashbyhq.com/posting-api/job-board/podium |
| primer | https://api.ashbyhq.com/posting-api/job-board/primer |
| reka | https://api.ashbyhq.com/posting-api/job-board/reka |
| stedi | https://api.ashbyhq.com/posting-api/job-board/stedi |
| golinks | https://api.ashbyhq.com/posting-api/job-board/golinks |
| paragon | https://api.ashbyhq.com/posting-api/job-board/paragon |
| creditgenie | https://api.ashbyhq.com/posting-api/job-board/creditgenie |
| anyscale | https://api.ashbyhq.com/posting-api/job-board/anyscale |
| helion | https://api.ashbyhq.com/posting-api/job-board/helion |
| freshpaint | https://api.ashbyhq.com/posting-api/job-board/freshpaint |
| juicebox | https://api.ashbyhq.com/posting-api/job-board/juicebox |
| kustomer | https://api.ashbyhq.com/posting-api/job-board/kustomer |
| sprig | https://api.ashbyhq.com/posting-api/job-board/sprig |
| svix | https://api.ashbyhq.com/posting-api/job-board/svix |
| tldraw | https://api.ashbyhq.com/posting-api/job-board/tldraw |
| sieve | https://api.ashbyhq.com/posting-api/job-board/sieve |
| oso | https://api.ashbyhq.com/posting-api/job-board/oso |

## Instructions

User query: $ARGUMENTS

### Scanning Process

1. **Default**: Fetch the **Top 15** companies. Only use the extended list if the user explicitly asks for more.
2. Fetch all companies in a **single batch** — do NOT split into multiple sequential batches (this causes timeouts). WebFetch them all in one pass.
3. For each company, WebFetch the endpoint with this prompt:
   ```
   List all job postings. For each job, return: title, location, isRemote (true/false),
   workplaceType (Remote/Hybrid/OnSite), department, employmentType, and the jobUrl.
   Only include jobs where isRemote is true OR workplaceType is "Remote".
   ```
3. **Filter results**:
   - `isRemote === true` OR `workplaceType === "Remote"`
   - Title contains any of: developer, engineer, software, junior, entry, intern, graduate, full stack, backend, frontend, SWE, SDE
   - Exclude: senior (5+ years), staff, principal, director, VP, lead (unless specifically asked)
4. **Present results** sorted by company

### Output Format

```markdown
## Remote Jobs — Ashby Scan [DATE]

### [Company Name]
| Title | Type | Apply |
|-------|------|-------|
| Junior Software Engineer | Remote | [Apply](url) |

### [Company Name]
...
```

### After scanning:
1. Append all remote results to `~/.yoad-jobs/job-history.md`
2. Save high-fit postings to `~/.yoad-jobs/jobs/[company]-[date]/posting.md`
3. Report total: X remote dev jobs found across Y companies

### Filtering by keywords:
If `$ARGUMENTS` is provided, additionally filter by those keywords in the job title or description.
