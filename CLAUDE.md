# Yoad Job Search — Israel-focused Job Discovery

## Candidate Profile

- **Name**: Yoad Hordan
- **Status**: Recent CS graduate
- **Target roles**: Junior/entry-level software developer
- **Tech stack**: Any/all languages (wide net)
- **Locations**: Israel (primary) + remote worldwide
- **CV**: `Yoad Hordan - CV.pdf` (project root)

## Installed Skills

### Job Discovery
- **`/israel-jobs`** — Search Israeli company job boards via Greenhouse/Ashby/Lever APIs + Israeli native sites
- **`/ashby-remote`** — Scan all Ashby companies worldwide for remote-only positions
- **`/job-search-il`** — WebSearch-based aggregation across Israeli job boards (Hebrew + English)

### Indeed MCP
The Indeed MCP connector is enabled as a Claude connector. Use it as an equal partner alongside the custom skills:
- `"junior software developer Israel"` — Israel-based roles
- `"entry level developer Tel Aviv"` — Tel Aviv roles
- `"remote software developer"` — Remote positions

## Search Strategy

### Hebrew Keywords
For Israeli-native job boards (AllJobs, Drushim, Jobmaster):
- מפתח/ת תוכנה (Software developer)
- מתכנת/ת (Programmer)
- מהנדס/ת תוכנה (Software engineer)
- ג'וניור (Junior)
- פיתוח (Development)
- מתחילים / ללא ניסיון (Entry-level / No experience)

### English Keywords
- Junior software developer
- Entry level developer
- Graduate developer
- Software engineer (junior/entry)
- Full stack developer (junior)
- Backend developer (junior)
- Frontend developer (junior)

## Job Sources

| Source | Type | Language | Access Method |
|--------|------|----------|---------------|
| Indeed MCP | Global + Israel | EN/HE | Claude MCP connector |
| JUNIO.co.il | Junior-specific IL | HE/EN | WebSearch — Israel's only junior hi-tech board |
| AllJobs.co.il | Israeli native | HE | WebSearch/WebFetch |
| Drushim.co.il | Israeli native | HE | WebSearch/WebFetch |
| Jobmaster.co.il | Israeli native | HE | WebSearch/WebFetch |
| GotFriends.co.il | Israeli recruiter | HE/EN | WebSearch/WebFetch |
| Indeed Israel (il.indeed.com) | Global (Israel) | EN/HE | WebSearch/WebFetch |
| Goozali | Israeli hi-tech | EN | WebFetch (Google Sheets) |
| Janglo | English community IL | EN | WebSearch/WebFetch |
| Secret Tel Aviv | English community IL | EN | WebSearch/WebFetch |
| Wellfound | Startups | EN | WebSearch/WebFetch |
| Greenhouse API | Tech companies | EN | WebFetch (JSON API) |
| Ashby API | Tech companies | EN | WebFetch (JSON API) |
| Lever API | Tech companies | EN | WebFetch (JSON API) |

## Israeli Tech Companies (with API endpoints)

Companies with Israel offices or founded in Israel that use Greenhouse/Ashby/Lever:
- Fireblocks, HoneyBook, Melio, Taboola, Yotpo, Cybereason, Papaya Global
- Payoneer, Monday.com, Wix, Check Point, CyberArk, ironSource
- JFrog, Lightricks, Via, Lemonade, Hibob, Gong, Snyk

## Data Directory

`~/.yoad-jobs/` — separate from other users' data
```
~/.yoad-jobs/
├── resume/          # Yoad's CV
├── preferences.md   # Job preferences
├── job-history.md   # Running log of discovered jobs
└── jobs/            # Saved job postings
    └── [company-date]/
        └── posting.md
```

## Workflow

1. **Discover**: `/israel-jobs`, `/ashby-remote`, `/job-search-il`, or Indeed MCP
2. **Filter**: Score against preferences (junior SWE, Israel/remote, any tech stack)
3. **Track**: All results saved to `~/.yoad-jobs/job-history.md`
4. **Apply**: Manual for now (discovery-only scope)
