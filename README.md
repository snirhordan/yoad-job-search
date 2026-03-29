# Yoad Job Search

Israel-focused job discovery platform for junior software developers, powered by Claude Code skills.

Searches 10+ Israeli job boards (Hebrew + English), 35+ Israeli tech company APIs, 50+ Ashby companies for remote roles, and Indeed via MCP — all from the terminal.

---

## Getting Started (from zero)

### Step 1: Install Claude Code

Open a terminal and run:

```bash
npm install -g @anthropic-ai/claude-code
```

If you don't have npm, install Node.js first from https://nodejs.org (download the LTS version, install it, then retry the command above).

After installation, run `claude` once to log in with your Anthropic account. Follow the prompts to authenticate.

### Step 2: Clone this repo

```bash
git clone https://github.com/snirhordan/yoad-job-search.git ~/yoad-job-search
```

### Step 3: Create the data directory

```bash
mkdir -p ~/.yoad-jobs
cp ~/yoad-job-search/preferences.md ~/.yoad-jobs/preferences.md
touch ~/.yoad-jobs/job-history.md
```

### Step 4: Start searching for jobs

```bash
cd ~/yoad-job-search
claude
```

Claude will open. Type any of these commands:

```
/job-search-il                    # Search all Israeli job boards
/israel-jobs wix                  # Check jobs at a specific company
/ashby-remote                     # Find remote jobs worldwide
```

That's it!

---

## הוראות בעברית

### שלב 1: התקנת Claude Code

פתח טרמינל והרץ:
```bash
npm install -g @anthropic-ai/claude-code
```

אם אין לך npm, תתקין קודם Node.js מ-https://nodejs.org (תוריד את גרסת LTS, תתקין, ואז תנסה שוב).

אחרי ההתקנה, תרשום `claude` פעם אחת כדי להתחבר עם החשבון שלך באנתרופיק.

### שלב 2: שכפול הפרויקט

```bash
git clone https://github.com/snirhordan/yoad-job-search.git ~/yoad-job-search
```

### שלב 3: יצירת תיקיית הנתונים

```bash
mkdir -p ~/.yoad-jobs
cp ~/yoad-job-search/preferences.md ~/.yoad-jobs/preferences.md
touch ~/.yoad-jobs/job-history.md
```

### שלב 4: חיפוש משרות

```bash
cd ~/yoad-job-search
claude
```

קלוד ייפתח. תרשום אחת מהפקודות:

| פקודה | מה עושה |
|-------|---------|
| `/job-search-il` | חיפוש בכל האתרים הישראליים (עברית + אנגלית) |
| `/job-search-il Python` | חיפוש עם מילת מפתח ספציפית |
| `/israel-jobs wix` | בדיקת משרות בחברה מסוימת |
| `/israel-jobs` | חיפוש בכל חברות ההייטק הישראליות |
| `/ashby-remote` | משרות Remote בחברות בינלאומיות |

---

## Prerequisites (detailed)

1. **Node.js** (v18+) — https://nodejs.org
2. **Claude Code** — `npm install -g @anthropic-ai/claude-code`
3. **Git** — comes pre-installed on Mac/Linux; on Windows install from https://git-scm.com
4. **GitHub CLI** (`gh`) — optional, only needed for contributing
5. **Indeed MCP connector** — optional, enable in Claude settings for Indeed searches

## Quick Start (for experienced users)

```bash
git clone https://github.com/snirhordan/yoad-job-search.git ~/yoad-job-search
mkdir -p ~/.yoad-jobs && cp ~/yoad-job-search/preferences.md ~/.yoad-jobs/
cd ~/yoad-job-search && claude
```

Then:
```
/job-search-il                          # Broad search across all Israeli sites
/job-search-il Python developer         # Search with specific keywords
/job-search-il מפתח תוכנה              # Search in Hebrew
/israel-jobs wix                        # Check a specific company
/israel-jobs                            # Search all Israeli boards + company APIs
/ashby-remote                           # Scan 15 top companies for remote roles
/ashby-remote all                       # Scan all 50+ Ashby companies
```

## Skills

### `/job-search-il` — Multi-Site Aggregated Search

The main search skill. Runs 9 parallel queries across Israeli job boards in both Hebrew and English.

**What it does:**
1. Loads your preferences from `~/.yoad-jobs/preferences.md`
2. Checks job history to avoid showing duplicates
3. Searches 10+ sites: AllJobs, Drushim, Indeed IL, JUNIO, GotFriends, Janglo, Secret Tel Aviv, Wellfound, startup.jobs, Goozali, JobMaster
4. Scores each result as High / Medium / Low / Skip based on your preferences
5. Enriches top matches with full job descriptions
6. Saves results to job history
7. Presents ranked results with apply links

**Sites searched:**

| Site | Language | Type |
|------|----------|------|
| AllJobs.co.il | Hebrew | Israel's largest job board |
| Drushim.co.il | Hebrew | 378+ no-experience listings |
| JUNIO.co.il | Hebrew/English | Israel's only junior-specific board |
| GotFriends.co.il | Hebrew/English | Top hi-tech recruiter |
| JobMaster.co.il | Hebrew | Generalist board |
| il.indeed.com | English/Hebrew | Indeed Israel |
| Janglo.net | English | English-speaker community |
| SecretTelAviv.com | English | English-speaker community |
| Wellfound.com | English | Startup jobs |
| startup.jobs | English | Startup jobs |
| Goozali.com | English | Google Sheets-based hi-tech board |

### `/israel-jobs` — Company-Specific & Board Search

Query specific Israeli tech companies via their Greenhouse/Ashby/Lever APIs, or search all boards at once.

**Company-specific:**
```
/israel-jobs fireblocks       # Fetch Fireblocks jobs from Greenhouse API
/israel-jobs melio            # Fetch Melio jobs
/israel-jobs wix              # Fetch Wix jobs
```

**General search:**
```
/israel-jobs                  # Search all Israeli boards + APIs
/israel-jobs backend          # Search with keyword filter
```

**35+ Israeli companies with API endpoints:** Fireblocks, HoneyBook, Melio, Taboola, Yotpo, Cybereason, Papaya Global, Payoneer, Wix, Check Point, JFrog, Lightricks, Playtika, SimilarWeb, WalkMe, AppsFlyer, Riskified, Tipalti, and more.

### `/ashby-remote` — Worldwide Remote Job Scanner

Scans Ashby-powered companies for remote developer positions worldwide.

**Default (Top 15 companies):**
```
/ashby-remote                           # Scan top 15 companies
/ashby-remote frontend                  # Filter by keyword
```

**Extended scan:**
```
/ashby-remote all                       # Scan all 50+ companies (slower)
```

**Companies scanned:** Linear, Supabase, Deel, Cursor, PostHog, Snyk, ClickUp, Notion, Render, Retool, Railway, Clerk, Neon, Vanta, WorkOS, and 35+ more in the extended list.

**Filters applied automatically:**
- Only remote positions (`isRemote: true`)
- Only dev roles (developer, engineer, software, junior, etc.)
- Excludes senior/staff/principal/director/VP

### Indeed MCP (Cloud Connector)

Use natural language to search Indeed directly:

```
Search Indeed for junior software developer jobs in Israel
Find entry level developer positions in Tel Aviv on Indeed
Search Indeed for remote software developer jobs
```

## Data Files

| File | Location | Purpose |
|------|----------|---------|
| `preferences.md` | `~/.yoad-jobs/` and repo | Role preferences, dealbreakers |
| `job-history.md` | `~/.yoad-jobs/` and repo | Running log of all discovered jobs |
| `application-tracker.md` | repo | Track application status |
| `Yoad Hordan - CV.pdf` | repo | CV for reference |

### Updating Preferences

Edit `~/.yoad-jobs/preferences.md` to change:
- Target roles and experience level
- Location preferences
- Tech stack preferences
- Dealbreakers (e.g., "no defense sector", "minimum NIS 20k/month")

Or just tell the skill after a search: "no startups" or "prefer Tel Aviv" — it will update preferences automatically.

## Application Tracking

After finding jobs, track applications in `application-tracker.md`:

1. Move a job from "To Apply" to "Applied" with the date
2. Update to "Interview" when you hear back
3. Track offers and rejections

## Project Structure

```
yoad/
├── README.md                              # This file
├── CLAUDE.md                              # Project config for Claude Code
├── Yoad Hordan - CV.pdf                   # CV
├── preferences.md                         # Job preferences (also at ~/.yoad-jobs/)
├── job-history.md                         # Search history (also at ~/.yoad-jobs/)
├── application-tracker.md                 # Application status tracker
├── .claude/skills/
│   ├── israel-jobs/SKILL.md               # Israeli company + board search
│   ├── ashby-remote/SKILL.md              # Worldwide remote scanner
│   └── job-search-il/SKILL.md             # Multi-site aggregated search
├── .agents/skills/
│   ├── grill-me/                          # Interview/planning skill
│   ├── write-a-prd/                       # PRD creation skill
│   ├── prd-to-issues/                     # PRD to GitHub issues
│   ├── tdd/                               # Test-driven development
│   └── improve-codebase-architecture/     # Architecture improvement
├── tests/                                 # 169 tests (pytest)
└── skill-eval-workspace/                  # Skill evaluation benchmarks
```

## Running Tests

```bash
python3 -m pytest tests/ -v
```

169 tests covering skill structure, API endpoint reachability, content validation, and fit scoring logic.

## Benchmark Results

Skills were evaluated using Anthropic's [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) methodology:

| Metric | With Skill | Without Skill |
|--------|-----------|---------------|
| Pass Rate | **100%** | 49% |
| Hebrew search | Always | Sometimes |
| Fit scoring | Always | Never |
| Data persistence | Always | Never |

## Hebrew Search Keywords

The skills search in Hebrew using these terms:

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
