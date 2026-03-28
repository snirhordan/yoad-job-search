---
name: ashby-remote
description: Scan all Ashby-hosted companies worldwide for remote software development positions. Use when user wants remote jobs, worldwide remote positions, or asks about Ashby job listings.
allowed-tools: WebFetch
---

# Ashby Remote Job Scanner

Scan all Ashby-powered companies for remote software development positions worldwide.

## Ashby Companies

| Company | Endpoint |
|---------|----------|
| linear | https://api.ashbyhq.com/posting-api/job-board/linear |
| notion | https://api.ashbyhq.com/posting-api/job-board/notion |
| revenuecat | https://api.ashbyhq.com/posting-api/job-board/revenuecat |
| clerk | https://api.ashbyhq.com/posting-api/job-board/clerk |
| neon | https://api.ashbyhq.com/posting-api/job-board/neon |
| ramp | https://api.ashbyhq.com/posting-api/job-board/ramp |
| render | https://api.ashbyhq.com/posting-api/job-board/render |
| retool | https://api.ashbyhq.com/posting-api/job-board/retool |
| railway | https://api.ashbyhq.com/posting-api/job-board/railway |
| supabase | https://api.ashbyhq.com/posting-api/job-board/supabase |
| cohere | https://api.ashbyhq.com/posting-api/job-board/cohere |
| openai | https://api.ashbyhq.com/posting-api/job-board/openai |
| cursor | https://api.ashbyhq.com/posting-api/job-board/cursor |
| deel | https://api.ashbyhq.com/posting-api/job-board/deel |
| ashby | https://api.ashbyhq.com/posting-api/job-board/ashby |
| braintrust | https://api.ashbyhq.com/posting-api/job-board/braintrust |
| drata | https://api.ashbyhq.com/posting-api/job-board/drata |
| freshpaint | https://api.ashbyhq.com/posting-api/job-board/freshpaint |
| helion | https://api.ashbyhq.com/posting-api/job-board/helion |
| juicebox | https://api.ashbyhq.com/posting-api/job-board/juicebox |
| kustomer | https://api.ashbyhq.com/posting-api/job-board/kustomer |
| motion | https://api.ashbyhq.com/posting-api/job-board/motion |
| posthog | https://api.ashbyhq.com/posting-api/job-board/posthog |
| replit | https://api.ashbyhq.com/posting-api/job-board/replit |
| snyk | https://api.ashbyhq.com/posting-api/job-board/snyk |
| sprig | https://api.ashbyhq.com/posting-api/job-board/sprig |
| svix | https://api.ashbyhq.com/posting-api/job-board/svix |
| stedi | https://api.ashbyhq.com/posting-api/job-board/stedi |
| tldraw | https://api.ashbyhq.com/posting-api/job-board/tldraw |
| vanta | https://api.ashbyhq.com/posting-api/job-board/vanta |
| workos | https://api.ashbyhq.com/posting-api/job-board/workos |
| pinecone | https://api.ashbyhq.com/posting-api/job-board/pinecone |
| podium | https://api.ashbyhq.com/posting-api/job-board/podium |
| primer | https://api.ashbyhq.com/posting-api/job-board/primer |
| reka | https://api.ashbyhq.com/posting-api/job-board/reka |
| runway | https://api.ashbyhq.com/posting-api/job-board/runway |
| sieve | https://api.ashbyhq.com/posting-api/job-board/sieve |
| golinks | https://api.ashbyhq.com/posting-api/job-board/golinks |
| greptile | https://api.ashbyhq.com/posting-api/job-board/greptile |
| hightouch | https://api.ashbyhq.com/posting-api/job-board/hightouch |
| fullstory | https://api.ashbyhq.com/posting-api/job-board/fullstory |
| deepgram | https://api.ashbyhq.com/posting-api/job-board/deepgram |
| clickup | https://api.ashbyhq.com/posting-api/job-board/clickup |
| benchling | https://api.ashbyhq.com/posting-api/job-board/benchling |
| paragon | https://api.ashbyhq.com/posting-api/job-board/paragon |
| oso | https://api.ashbyhq.com/posting-api/job-board/oso |
| creditgenie | https://api.ashbyhq.com/posting-api/job-board/creditgenie |
| scaleai | https://api.ashbyhq.com/posting-api/job-board/scaleai |
| anyscale | https://api.ashbyhq.com/posting-api/job-board/anyscale |
| perplexity | https://api.ashbyhq.com/posting-api/job-board/perplexity |

## Instructions

User query: $ARGUMENTS

### Scanning Process

1. **Batch fetching**: Process companies in batches of 5-8 to avoid rate limits
2. For each company, WebFetch the endpoint with this prompt:
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
