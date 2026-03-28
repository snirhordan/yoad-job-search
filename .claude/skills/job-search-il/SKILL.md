---
name: job-search-il
description: Search for junior software development jobs across Israeli job boards using WebSearch aggregation. Searches in both Hebrew and English across AllJobs, Drushim, Indeed IL, Goozali, Janglo, and more.
allowed-tools: WebSearch, WebFetch
argument-hint: "keyword to search"
---

# Israeli Job Search Skill

Automated job search across Israeli job boards using web search aggregation.

## Quick Start

- `/job-search-il` — Run search with default junior SWE keywords
- `/job-search-il Python developer` — Search with specific keywords
- `/job-search-il מפתח תוכנה` — Search in Hebrew

## Data Directory

`~/.yoad-jobs/`

---

## Workflow

### Step 0: Check Prerequisites

Verify these files exist:
- `~/.yoad-jobs/preferences.md` (job preferences)
- `Yoad Hordan - CV.pdf` (in project root)

If `preferences.md` doesn't exist, create a default one based on the CLAUDE.md candidate profile.

### Step 1: Load Context

Read these files:
- `~/.yoad-jobs/preferences.md` (preferences & dealbreakers)
- `~/.yoad-jobs/job-history.md` (to avoid duplicates)

Extract search terms from:
1. `$ARGUMENTS` if provided
2. Default terms: "junior software developer", "מפתח תוכנה ג'וניור", "entry level developer"

### Step 2: Web Search — Multi-Site Aggregation

Run parallel WebSearch queries across Israeli job boards:

**English searches:**
1. `"junior software developer" Israel site:il.indeed.com`
2. `"junior developer" OR "entry level developer" Israel site:janglo.net OR site:secrettelaviv.com`
3. `"software developer" Israel junior site:wellfound.com OR site:startup.jobs`
4. `"developer" Israel junior OR entry site:goozali.com`
5. `junior developer site:junio.co.il` — JUNIO is Israel's only junior-specific hi-tech job board, always check it

**Hebrew searches:**
6. `"מפתח תוכנה" ג'וניור site:alljobs.co.il`
7. `"מתכנת" OR "מפתח תוכנה" ללא ניסיון site:drushim.co.il`
8. `"מפתח תוכנה" ג'וניור site:jobmaster.co.il`
9. `"junior developer" OR "מפתח" site:gotfriends.co.il`

If `$ARGUMENTS` is provided, replace default keywords but keep the site filters.

### Step 3: Extract & Deduplicate

From WebSearch results:
1. Extract: job title, company, location, URL, brief description
2. Deduplicate by company + title combination
3. Remove jobs already in `~/.yoad-jobs/job-history.md`

### Step 4: Score Jobs

For each new job, evaluate fit:

**High fit** — Junior/entry-level SWE role, Israel-based or remote, no dealbreakers
**Medium fit** — SWE-adjacent role (QA, DevOps, data) OR slightly above junior level
**Low fit** — Wrong field, requires 3+ years, or has dealbreakers
**Skip** — Not a tech role, or matches a dealbreaker

### Step 5: Enrich Top Results

For High-fit and Medium-fit jobs:
1. WebFetch the job posting URL to get full description
2. Extract: requirements, tech stack, salary (if listed), company info
3. Note anything relevant to Yoad's profile

**Handling 403 errors**: Some Israeli sites (Secret Tel Aviv, AllJobs direct pages) block WebFetch with 403 errors. When this happens:
- Do NOT retry the same URL
- Fall back to WebSearch with `site:` filter to find the listing
- Extract details from the WebSearch snippet instead
- Note in results that direct fetch was blocked

### Step 6: Save History

Append ALL jobs to `~/.yoad-jobs/job-history.md`:

```markdown
## [DATE] — Search: "[terms]"

| Job Title | Company | Location | Source | Fit | URL |
|-----------|---------|----------|--------|-----|-----|
| Junior Dev | Monday.com | Tel Aviv | AllJobs | High | [link] |
```

Save High-fit postings to `~/.yoad-jobs/jobs/[company-slug]-[date]/posting.md`

### Step 7: Present Results

Show only NEW High/Medium fits:

```markdown
## Top Matches — [DATE]

### 1. [Title] at [Company]
- **Fit**: High
- **Location**: Tel Aviv / Remote
- **Source**: AllJobs / Indeed IL / etc.
- **Tech Stack**: Python, React, PostgreSQL
- **Why**: Junior SWE role, matches CS graduate profile
- **Apply**: [direct URL]
```

### Step 8: Indeed MCP Supplement

After web search results, remind the user:
```
Tip: For additional results, ask me to search Indeed using the Indeed connector:
"Search Indeed for junior software developer jobs in Israel"
```

### Step 9: Learn from Feedback

If user provides feedback, update `~/.yoad-jobs/preferences.md`:
- "No startups" → add to dealbreakers
- "Prefer Tel Aviv" → add to location preferences
- "Only Python" → add to must-haves

---

## Response Format

1. **Top Matches** — table of High/Medium fits with company, role, source, fit rating, and URL
2. **Summary** — X new jobs found across Y sites, Z high-fit matches
3. **Next Steps** — suggest specific companies to check via `/israel-jobs [company]`

---

## Permissions Required

```json
{
  "permissions": {
    "allow": [
      "Read(~/.yoad-jobs/**)",
      "Write(~/.yoad-jobs/**)",
      "Edit(~/.yoad-jobs/**)",
      "WebSearch(*)",
      "WebFetch(*)"
    ]
  }
}
```
