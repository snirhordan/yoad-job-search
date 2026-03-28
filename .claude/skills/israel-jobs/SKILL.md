---
name: israel-jobs
description: Find job openings at Israeli tech companies and companies with Israel offices. Use when user asks about jobs in Israel, Israeli tech companies, or Hebrew job searches.
allowed-tools: WebFetch, WebSearch
---

# Israel Job Search

## Israeli Tech Companies (API Endpoints)

### Greenhouse API
| Company | Endpoint |
|---------|----------|
| fireblocks | https://boards-api.greenhouse.io/v1/boards/fireblocks/jobs |
| honeybook | https://boards-api.greenhouse.io/v1/boards/honeybook/jobs |
| melio | https://boards-api.greenhouse.io/v1/boards/melio/jobs |
| taboola | https://boards-api.greenhouse.io/v1/boards/taboola/jobs |
| yotpo | https://boards-api.greenhouse.io/v1/boards/yotpo/jobs |
| cybereason | https://boards-api.greenhouse.io/v1/boards/cybereason/jobs |
| papaya | https://boards-api.greenhouse.io/v1/boards/papaya/jobs |
| payoneer | https://boards-api.greenhouse.io/v1/boards/payoneer/jobs |
| monday | https://monday.com/careers (WebSearch: `site:monday.com/careers developer`) |
| wix | https://boards-api.greenhouse.io/v1/boards/wix/jobs |
| checkpoint | https://boards-api.greenhouse.io/v1/boards/checkpoint/jobs |
| jfrog | https://boards-api.greenhouse.io/v1/boards/jfrog/jobs |
| lemonade | https://boards-api.greenhouse.io/v1/boards/lemonade/jobs |
| gong | https://boards-api.greenhouse.io/v1/boards/gaborone/jobs |
| hibob | https://boards-api.greenhouse.io/v1/boards/hibob/jobs |
| via | https://boards-api.greenhouse.io/v1/boards/via/jobs |
| ironsource | https://boards-api.greenhouse.io/v1/boards/ironsource/jobs |
| lightricks | https://boards-api.greenhouse.io/v1/boards/lightricks/jobs |
| playtika | https://boards-api.greenhouse.io/v1/boards/playtika/jobs |
| similarweb | https://boards-api.greenhouse.io/v1/boards/similarweb/jobs |
| walkme | https://boards-api.greenhouse.io/v1/boards/walkme/jobs |
| appsflyer | https://boards-api.greenhouse.io/v1/boards/appsflyer/jobs |
| riskified | https://boards-api.greenhouse.io/v1/boards/riskified/jobs |
| tipalti | https://boards-api.greenhouse.io/v1/boards/tipalti/jobs |
| orca | https://boards-api.greenhouse.io/v1/boards/orca/jobs |
| guardicore | https://boards-api.greenhouse.io/v1/boards/guardicore/jobs |
| fundbox | https://boards-api.greenhouse.io/v1/boards/fundbox/jobs |
| nextinsurance | https://boards-api.greenhouse.io/v1/boards/nextinsurance/jobs |
| rapyd | https://boards-api.greenhouse.io/v1/boards/rapyd/jobs |
| forter | https://boards-api.greenhouse.io/v1/boards/forter/jobs |
| finastra | https://boards-api.greenhouse.io/v1/boards/finastra/jobs |
| bigpanda | https://boards-api.greenhouse.io/v1/boards/bigpanda/jobs |
| aquasecurity | https://boards-api.greenhouse.io/v1/boards/aquasecurity/jobs |
| cato | https://boards-api.greenhouse.io/v1/boards/catonetworks/jobs |
| perion | https://boards-api.greenhouse.io/v1/boards/perion/jobs |
| nayax | https://boards-api.greenhouse.io/v1/boards/nayax/jobs |
| solaredge | https://boards-api.greenhouse.io/v1/boards/solaredge/jobs |

### Ashby API
| Company | Endpoint |
|---------|----------|
| snyk | https://api.ashbyhq.com/posting-api/job-board/snyk |
| deel | https://api.ashbyhq.com/posting-api/job-board/deel |
| clickup | https://api.ashbyhq.com/posting-api/job-board/clickup |
| vanta | https://api.ashbyhq.com/posting-api/job-board/vanta |
| drata | https://api.ashbyhq.com/posting-api/job-board/drata |

### Lever API
| Company | Endpoint |
|---------|----------|
| spotify | https://api.lever.co/v0/postings/spotify |
| atlassian | https://api.lever.co/v0/postings/atlassian |

## Israeli Job Boards (Web Search/Fetch)

| Site | URL | Language | Search Pattern |
|------|-----|----------|---------------|
| AllJobs | https://www.alljobs.co.il | Hebrew | WebSearch: `site:alljobs.co.il מפתח תוכנה ג'וניור` |
| Drushim | https://www.drushim.co.il | Hebrew | WebSearch: `site:drushim.co.il מפתח תוכנה` |
| Jobmaster | https://www.jobmaster.co.il | Hebrew | WebSearch: `site:jobmaster.co.il מתכנת` |
| GotFriends | https://www.gotfriends.co.il | HE/EN | WebSearch: `site:gotfriends.co.il junior developer` |
| Indeed IL | https://il.indeed.com | EN/HE | WebFetch: `https://il.indeed.com/jobs?q=junior+developer&l=Israel` |
| Goozali | https://en.goozali.com | English | WebFetch: Google Sheets-based, filterable |
| Janglo | https://www.janglo.net/jobs | English | WebSearch: `site:janglo.net developer jobs` |
| Secret TLV | https://jobs.secrettelaviv.com | English | WebSearch: `site:secrettelaviv.com developer` |
| Wellfound | https://wellfound.com/location/israel | English | WebFetch: Israel startup jobs |

## Hebrew Search Keywords

| English | Hebrew |
|---------|--------|
| Software developer | מפתח/ת תוכנה |
| Programmer | מתכנת/ת |
| Software engineer | מהנדס/ת תוכנה |
| Junior | ג'וניור |
| Entry level | ללא ניסיון / מתחילים |
| Full stack | פול סטאק |
| Backend | בקאנד / צד שרת |
| Frontend | פרונטאנד / צד לקוח |

## Instructions

User query: $ARGUMENTS

### For company-specific queries:
1. Find company in the tables above (case-insensitive)
2. If it's a Greenhouse/Ashby/Lever company: WebFetch the endpoint
3. Prompt for WebFetch: "List all jobs with: Title, Location, Department, Salary (if available), and Apply URL (use absolute_url field). Filter for junior/entry-level positions or software development roles where possible."
4. Display results grouped by department
5. Filter for Israel-located or remote positions
6. Always include an [Apply](url) hyperlink

### For general queries (no specific company):
1. Search across multiple Israeli job boards using WebSearch
2. Run Hebrew searches: `"מפתח תוכנה ג'וניור" site:alljobs.co.il OR site:drushim.co.il`
3. Run English searches: `"junior developer Israel" site:il.indeed.com OR site:janglo.net`
4. WebFetch 3-5 Israeli tech company API endpoints
5. Compile results, prioritize junior/entry-level SWE roles
6. Score against preferences from `~/.yoad-jobs/preferences.md`

### For Hebrew queries:
1. Use Hebrew keywords from the table above
2. Search Hebrew sites: AllJobs, Drushim, Jobmaster
3. WebSearch with Hebrew terms, extract results

### After displaying results:
1. Deduplicate results by company + title against `~/.yoad-jobs/job-history.md`
2. Append new jobs to `~/.yoad-jobs/job-history.md`
3. Save high-fit postings to `~/.yoad-jobs/jobs/[company]-[date]/posting.md`
