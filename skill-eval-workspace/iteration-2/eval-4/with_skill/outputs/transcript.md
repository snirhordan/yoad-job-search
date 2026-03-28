# Job Search Transcript -- 2026-03-28

## Task
Broad job search across Israeli sites for Yoad, a recent CS graduate looking for any junior dev role in Israel or remote. No specific tech stack preference.

## Skill Used
`/job-search-il` -- Israeli Job Search Skill (SKILL.md)

## Step 0: Prerequisites Check
- `~/.yoad-jobs/preferences.md` -- EXISTS
- `Yoad Hordan - CV.pdf` -- EXISTS in project root
- `~/.yoad-jobs/job-history.md` -- EXISTS (empty, no previous searches)

## Step 1: Context Loaded
- **Preferences**: Junior/entry-level SWE, Tel Aviv preferred or remote, no 3+ yr experience, no defense/military, no unpaid, no relocation outside Israel
- **Search terms**: Default terms used (no $ARGUMENTS override): "junior software developer", "מפתח תוכנה ג'וניור", "entry level developer"
- **Job history**: No previous searches to deduplicate against

## Step 2: Web Search -- 9 Queries Executed (All in Parallel)

### English Searches (5):
1. `"junior software developer" Israel site:il.indeed.com`
   - Result: Multiple listing pages found. 50+ junior SWE, 25+ junior dev, 17 junior Python dev roles. Companies include Cisco, Copyleaks, Eternitech. Locations: Tel Aviv, Caesarea, Netanya, Jerusalem, Haifa.

2. `"junior developer" OR "entry level developer" Israel site:janglo.net OR site:secrettelaviv.com`
   - Result: Only 1 result -- Senior Unity Developer on Secret Tel Aviv. No junior matches on these English-language community boards.

3. `"software developer" Israel junior site:wellfound.com OR site:startup.jobs`
   - Result: Junior SWE at ZipRecruiter (Tel Aviv), Intern/Junior Frontend at Brainnest (Jerusalem). Wellfound lists various SWE roles in Israel generally.

4. `"developer" Israel junior OR entry site:goozali.com`
   - Result: Goozali homepage returned. Platform has 4,000+ open positions and 6,000 candidates. Covers SWE, AI, Data Science, ML, Frontend, Mobile, DevOps, QA.

5. `junior developer site:junio.co.il` -- **JUNIO (junior-specific board)**
   - Result: Confirmed JUNIO is Israel's first junior-only hi-tech job site (est. 2022). Found Python Developer listing (AI/ML + Big Data). Site designed to accelerate first-job search.

### Hebrew Searches (4):
6. `"מפתח תוכנה" ג'וניור site:alljobs.co.il`
   - Result: Python dev and Full Stack dev listing pages. Most results skewed senior (1-5+ years). Limited junior-specific results from search.

7. `"מתכנת" OR "מפתח תוכנה" ללא ניסיון site:drushim.co.il`
   - Result: Rich results. Multiple "no experience" listings including מתכנת ללא ניסיון, מתכנת מתחיל, מפתח תוכנה, web developer. Strongest Hebrew source.

8. `"מפתח תוכנה" ג'וניור site:jobmaster.co.il`
   - Result: "תוכנה ללא ניסיון" listings, Python jobs, web dev, hi-tech no-experience roles. Experis and John Bryce training programs featured.

9. `"junior developer" OR "מפתח" site:gotfriends.co.il`
   - Result: **Best structured results.** 5 specific junior positions with job IDs: Junior Developer (#120389), Junior Full Stack (#120707), Junior Web Developer (#99568 -- defense sector, skipped), Junior Developer (#121319), Junior Fullstack Developer (#100627).

## Step 3: Enrichment (WebFetch on Top Results)

| URL | Status | Result |
|-----|--------|--------|
| il.indeed.com/Junior-Developer-jobs | 200 | Express Academic training program (Java/C/C++, Jerusalem, GPA 85+) |
| startup.jobs/israel/junior-software-developer | **403** | Fell back to WebSearch site: filter. Found JFrog ML role + ZipRecruiter junior SWE |
| GotFriends #120389 (Junior Dev) | 200 | E-commerce startup, Tel Aviv, Node/Go, 1yr exp, 10 employees |
| GotFriends #120707 (Junior Full Stack) | 200 | Financial portal, Tel Aviv, React/Node/MongoDB, 6mo OR graduates |
| GotFriends #121319 (Junior Dev - frontend page) | 200 | Page showed only senior roles (6-7+ years) -- no junior content on this page |
| junio.co.il | **Certificate expired** | Fell back to WebSearch. Confirmed junior-only platform exists |
| Drushim no-experience page | 200 | 5 listings extracted: Infinity Labs (Haifa), Experis AI/ML (TLV), Experis Junior SWE (TLV), Ness QA (Dimona), Experis Data Sci (TLV) |
| en.goozali.com | 200 | Only CSS/structural markup returned -- dynamic content not extractable |
| JobMaster no-experience page | 200 | Experis recruitment campaign for graduates, Tel Aviv |
| startup.jobs ZipRecruiter listing | **403** | Used search snippet info instead |
| il.indeed.com junior SWE search | 200 | 0 results returned for that specific query string |

## Step 4: Scoring

### High Fit (5):
1. Junior Full Stack Developer -- Financial Portal via GotFriends (React/Node, Tel Aviv, accepts graduates)
2. Junior Software Developer -- Experis Academy via Drushim (Tel Aviv, no experience)
3. AI/ML Engineer -- Experis Academy via Drushim (Tel Aviv, no experience)
4. Junior Software Engineer -- JFrog via startup.jobs (Tel Aviv hybrid, ML focus)
5. Junior Software Engineer -- ZipRecruiter via startup.jobs (Tel Aviv)

### Medium Fit (6):
6. Junior Developer -- E-commerce Startup via GotFriends (1yr exp preferred)
7. Junior Fullstack Developer -- Ad-Tech via GotFriends (PHP/Node)
8. Software Dev Career Track -- Experis via JobMaster (training program)
9. Junior Dev Training -- Express Academic via Indeed (Jerusalem, GPA threshold)
10. Developers for Security Cos -- Infinity Labs via Drushim (Haifa)
11. Junior Data Scientist -- Experis Academy via Drushim (data, not pure SWE)

### Low Fit (1):
12. Junior Software Tester -- Ness Technologies (QA not SWE, Dimona)

### Skipped (3):
- Junior Web Developer at Security Startup (GotFriends #99568) -- Defense sector dealbreaker
- Senior Unity Developer (Secret Tel Aviv) -- Senior, not junior
- Senior roles from GotFriends frontend page -- 6-7+ years required

## Step 5: History Updated
All 12 jobs appended to `~/.yoad-jobs/job-history.md`

## Step 6: Results Saved
Full formatted results saved to `/home/snirhordan/yoad/skill-eval-workspace/iteration-2/eval-4/with_skill/outputs/results.md`

## Search Coverage Summary

| Source | Query # | Jobs Found | Fetchable |
|--------|---------|------------|-----------|
| Indeed IL | 1 | 1 enriched listing (Express Academic) | Yes |
| Janglo / Secret Tel Aviv | 2 | 0 junior matches | N/A |
| Wellfound / startup.jobs | 3 | 2 (JFrog, ZipRecruiter) | 403 -- used search fallback |
| Goozali | 4 | Platform confirmed, dynamic content | CSS only -- visit directly |
| JUNIO.co.il | 5 | Platform confirmed, Python dev listing | Cert expired -- used search fallback |
| AllJobs | 6 | Listing pages found, mostly senior | N/A |
| Drushim | 7 | 5 specific listings extracted | Yes |
| JobMaster | 8 | Experis training program | Yes |
| GotFriends | 9 | 5 junior positions (1 skipped defense) | Yes |

**Total: 9 search queries executed, 8 WebFetch enrichment attempts, 12 unique jobs identified, 5 high-fit, 6 medium-fit**
