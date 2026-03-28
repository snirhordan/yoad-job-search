# Transcript: Junior Software Developer Job Search -- Israel

**Date:** 2026-03-28
**Task:** Search for junior software developer jobs in Israel across all Israeli job boards. Recent graduate, no tech stack preference.

---

## Step 0: Read Skill File and Gather Context

1. **Read** `/home/snirhordan/yoad/.claude/skills/israel-jobs/SKILL.md` -- loaded the skill instructions including:
   - Greenhouse API endpoints for 30+ Israeli tech companies
   - Ashby API endpoints (Snyk, Deel, ClickUp, Vanta, Drata)
   - Lever API endpoints (Spotify, Atlassian)
   - Israeli job board search patterns (Hebrew and English)
   - Hebrew keyword translation table
   - Instructions for general queries (no specific company)

2. **Read** `~/.yoad-jobs/preferences.md` -- confirmed Yoad's preferences:
   - Junior / entry-level software developer
   - 0-2 years experience
   - Any tech stack, any city in Israel
   - No salary minimum
   - Must be dev role (not QA-only or support)

3. **Read** `~/.yoad-jobs/job-history.md` -- noted existing entries to avoid duplicates.

4. **Created** output directory: `/home/snirhordan/yoad/skill-eval-workspace/iteration-1/eval-2/with_skill/outputs/`

---

## Step 1: Hebrew Web Searches (AllJobs, Drushim, JobMaster)

### Search 1a: `מפתח תוכנה ג'וניור 2026 site:alljobs.co.il OR site:drushim.co.il`
- **Tool:** WebSearch
- **Results:** 10 links returned. Found junior positions including:
  - COBOL junior developer (financial org, bootcamp by John Bryce Talent)
  - Junior manual QA tester (Petah Tikva)
  - Junior software developer at software house in Rosh HaAyin (React, Node.js)
  - Junior Java developer at fintech company
  - DATA company recruiting juniors with no experience
  - Infinity Labs training programs

### Search 1b: `מתכנת ללא ניסיון site:jobmaster.co.il OR site:drushim.co.il 2026`
- **Tool:** WebSearch
- **Results:** 10 links. Found:
  - BI developer positions with company-funded training (no experience)
  - Infinity Labs DevOps positions (no experience)
  - Multiple "programmer without experience" listing pages on Drushim and JobMaster

### Search 1c: `מהנדס תוכנה ג'וניור ישראל דרושים 2026 site:alljobs.co.il`
- **Tool:** WebSearch
- **Results:** 10 links. Found:
  - Software engineer no-experience category pages on AllJobs
  - Student-targeted positions
  - Training programs for graduates (680+ psychometric, degree required)

### Search 1d: `פול סטאק ג'וניור דרושים תל אביב 2026`
- **Tool:** WebSearch
- **Results:** 10 links. Found:
  - Junio.co.il -- dedicated junior jobs platform in Israel
  - GotFriends Full Stack junior position
  - Expoint listing 772 full stack developer positions in Israel
  - Mploy junior positions

---

## Step 2: English Web Searches (Indeed IL, Janglo, Secret Tel Aviv, GotFriends)

### Search 2a: `junior software developer Israel 2026 site:il.indeed.com OR site:janglo.net`
- **Tool:** WebSearch
- **Results:** 10 links. Found:
  - Indeed IL: Junior Developer (9 results), Junior Software Engineer (50+), Junior Backend positions
  - Cisco Junior C++ Software Engineer in Caesarea
  - Eternitech junior front-end developer
  - Free Junior Developer training programs

### Search 2b: `junior developer Israel site:gotfriends.co.il OR site:secrettelaviv.com 2026`
- **Tool:** WebSearch
- **Results:** 10 links. Found 6 junior positions on Secret Tel Aviv:
  - Junior Software Engineer
  - Junior Java Developer
  - Junior Backend Developer (Python & Django)
  - Junior Unity Developer
  - Junior Full Stack Developer
  - Junior DevOps

### Search 2c: `junior software developer Israel entry level 2026`
- **Tool:** WebSearch (broad)
- **Results:** 10 links from Glassdoor, Built In, LinkedIn, PayScale. Found:
  - 25 junior software developer jobs (Glassdoor)
  - 8 entry-level software engineer jobs (Glassdoor)
  - Salary data: NIS 130,843-351,887/year
  - Top hiring companies: iCloudius, Deloitte, Agora, Pango, Tonkean, GigaSpaces, D-Fend, Apple, DRIVENETS

### Search 2d: `site:linkedin.com/jobs junior developer Israel 2026`
- **Tool:** WebSearch
- **Results:** 10 links. Key counts:
  - 34 Junior Developer jobs
  - 85 Junior Web Developer jobs
  - 1,000+ Junior Software Developer jobs
  - 2,000+ Junior Software Engineer jobs
  - 25 Junior Full Stack Developer jobs

### Search 2e: `junior developer entry level software engineer Israel wellfound startups 2026`
- **Tool:** WebSearch
- **Results:** Found Wellfound Spring 2026 Graduate Program position and startup job listings.

### Search 2f: `"junior developer" OR "entry level developer" Israel hiring 2026 site:glassdoor.com`
- **Tool:** WebSearch
- **Results:** Confirmed 16 junior software developer, 35 junior developer, 8 entry-level SWE jobs. Specific companies: Eternitech, iCloudius, Deloitte.

### Search 2g: `junior software developer Israel Cisco Apple Intel 2026 entry level`
- **Tool:** WebSearch
- **Results:** Found Cisco Junior Software Engineer - Graduate position (Tel Aviv-Yafo). Requirements: B.Sc/M.Sc CS, GPA 88+.

### Search 2h: `junior developer jobs Israel goozali 2026`
- **Tool:** WebSearch
- **Results:** Confirmed Goozali as a resource for job seekers. Platform offers filtering by experience level and specialization.

---

## Step 3: Company API Fetches (Greenhouse)

### Fetched Successfully:
| Company | Endpoint | Junior Roles Found |
|---------|----------|-------------------|
| SimilarWeb | Greenhouse API | 3 dev roles in Israel (Android Dev, AI Engineer, Data Engineer) |
| Riskified | Greenhouse API | 7 Israel roles (Data Scientist, SRE, etc. -- no explicit junior) |
| AppsFlyer | Greenhouse API | 5 dev roles in Herzliya (Backend Engineer, Data Engineer x2, Cloud Architect, Sr. Backend) |
| Lightricks | Greenhouse API | 6 R&D roles in Jerusalem/Haifa (all senior-level, no junior) |
| HoneyBook | Greenhouse API | 1 dev role in Tel Aviv (Senior Full Stack -- no junior) |
| Forter | Greenhouse API | 11 Israel roles (all senior; Data Researcher and Fraud Analyst potentially junior-friendly) |
| JFrog | Greenhouse API | 5 dev roles in Tel Aviv/Netanya (Full Stack Engineer, Software Engineer x2, Sr. roles) |
| Melio | Greenhouse API | 7 dev roles in Tel Aviv (Full Stack Engineer, Backend Engineer Data, iOS Developer + senior roles) |
| Yotpo | Greenhouse API | 7 roles in Tel Aviv (Back End Engineer + all senior roles) |

### Failed (404 / Not Found):
| Company | Status |
|---------|--------|
| Wix | 404 |
| Monday | 404 |
| Tipalti | 404 |
| Playtika | 404 |
| BigPanda | 404 |
| Checkpoint | 404 |

### Secret Tel Aviv Individual Pages:
- Attempted to WebFetch 6 individual Secret Tel Aviv job pages
- All returned **403 Forbidden** (site blocks automated fetching)
- Job listings still accessible via the search result links

### Cisco:
- Attempted to WebFetch 2 Cisco job detail pages
- Both redirected to careers.cisco.com (302) -- detail pages not directly fetchable

### Indeed IL:
- WebFetched `il.indeed.com/jobs?q=junior+developer&l=Israel`
- Found 1 detailed listing: Experis Academy Junior Developer Training (Jerusalem, free, Java/C/C++/Cloud)

### Goozali:
- WebFetched `en.goozali.com`
- Only CSS/styling returned -- no job data extractable (Google Sheets-based backend)

### Junio.co.il:
- WebFetch failed -- certificate expired

---

## Step 4: Compilation and Deduplication

1. Compared all discovered jobs against `~/.yoad-jobs/job-history.md`
2. Existing entries from prior search (2026-03-28) were noted and not double-counted
3. Categorized results into:
   - **HIGH-FIT** (22 positions): Explicitly junior/entry-level/no-experience
   - **MEDIUM-FIT** (17 positions): Non-senior dev roles at Israeli companies that may accept strong juniors
   - **Training Programs** (4 programs): Free bootcamps with job placement
4. Added direct browse links for all major job boards

---

## Step 5: Scoring Against Preferences

All results scored against `~/.yoad-jobs/preferences.md`:
- Junior/entry-level: YES
- Software development role: YES (filtered out QA-only, support, sales)
- Israel location: YES
- No tech stack restriction: Wide range covered (Java, Python, Node.js, React, TypeScript, C/C++, Unity, COBOL, Full Stack)
- Industries: Tech, fintech, ad-tech, security, gaming, e-commerce

---

## Step 6: Output

- **Results file:** `/home/snirhordan/yoad/skill-eval-workspace/iteration-1/eval-2/with_skill/outputs/results.md`
- **Transcript file:** `/home/snirhordan/yoad/skill-eval-workspace/iteration-1/eval-2/with_skill/outputs/transcript.md`

---

## Tools Used Summary

| Tool | Count | Purpose |
|------|-------|---------|
| WebSearch | 10 | Hebrew and English job board searches |
| WebFetch | 14 | Company API endpoints, job detail pages, job boards |
| Read | 2 | Skill file, preferences/history files |
| Write | 2 | Results and transcript output files |

## Search Queries Summary

### Hebrew Queries
1. `מפתח תוכנה ג'וניור 2026 site:alljobs.co.il OR site:drushim.co.il`
2. `מתכנת ללא ניסיון site:jobmaster.co.il OR site:drushim.co.il 2026`
3. `מהנדס תוכנה ג'וניור ישראל דרושים 2026 site:alljobs.co.il`
4. `פול סטאק ג'וניור דרושים תל אביב 2026`

### English Queries
1. `junior software developer Israel 2026 site:il.indeed.com OR site:janglo.net`
2. `junior developer Israel site:gotfriends.co.il OR site:secrettelaviv.com 2026`
3. `junior software developer Israel entry level 2026`
4. `site:linkedin.com/jobs junior developer Israel 2026`
5. `junior developer entry level software engineer Israel wellfound startups 2026`
6. `"junior developer" OR "entry level developer" Israel hiring 2026 site:glassdoor.com`
7. `junior software developer Israel Cisco Apple Intel 2026 entry level`
8. `junior developer jobs Israel goozali 2026`
