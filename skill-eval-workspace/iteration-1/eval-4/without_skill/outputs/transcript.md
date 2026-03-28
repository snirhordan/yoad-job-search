# Job Search Transcript
**Date:** March 28, 2026
**Task:** Broad job search across Israeli sites for Yoad, a recent CS graduate looking for junior dev roles in Israel or remote.

---

## Step 1: Environment Setup
- Created output directory at `/home/snirhordan/yoad/skill-eval-workspace/iteration-1/eval-4/without_skill/outputs/`
- Verified `curl` and `wget` available
- Discovered `WebSearch` and `WebFetch` tools were available, fetched their schemas

## Step 2: Initial Broad Web Searches (4 parallel searches)

### Search 2a: "junior software developer jobs Israel 2026"
- **Results:** Found Glassdoor listings (25 junior software developer, 860 software developer, 62 junior software engineer jobs in Israel), Built In, Secret Tel Aviv Jobs, Workable, Expoint
- **Key companies surfaced:** IronCircle, Gini Apps, Eternitech, BiltOn, SAP, DRIVENETS, Mend, Razor Labs, riverside.fm, Shift4
- **Key cities:** Tel Aviv-Yafo, Herzliya, Haifa, Ramat Gan, Petah Tikva, Raanana, Jerusalem

### Search 2b: "junior developer entry level programmer jobs Israel remote 2026"
- **Results:** Found Indeed remote listings, Arc remote jobs, Remote Rocketship, LinkedIn (34 junior developer jobs)
- **Key platforms:** Glassdoor, Indeed, Arc, Remote Rocketship, LinkedIn, Secret Tel Aviv

### Search 2c: "site:linkedin.com junior software developer Israel 2026"
- **Results:** Found 1,000+ junior software developer jobs, 2,000+ junior software engineer jobs, 2,000+ graduate software engineer jobs, 37 junior Java developer jobs on LinkedIn Israel

### Search 2d: Hebrew search "משרות מפתח ג'וניור ישראל 2026"
- **Results:** Found Hebrew job boards: Drushim.co.il, CareerJet Israel, GotFriends, Jobify360, JobSwipe, JUNIO (junior-only board), Poenta, AllJobs
- **Key insight:** Globes article reported only 88 out of 5,641 open positions available for candidates without experience -- competitive market

## Step 3: Deep Fetches of Specific Job Board Pages (4 parallel fetches)

### Fetch 3a: Glassdoor Israel junior software developer page
- **Result:** 403 Forbidden (blocked by Glassdoor)

### Fetch 3b: LinkedIn Israel junior software developer jobs
- **Result:** Successfully extracted 13 specific job listings including Rayzone Group, Meta, inManage, HPE, Apple, Deliveright, VAST Data, DRS RADA, Arcos LLC, Insait, Deloitte, abra

### Fetch 3c: Secret Tel Aviv Jobs programmer page
- **Result:** 403 Forbidden (blocked)

### Fetch 3d: JUNIO.co.il
- **Result:** Certificate expired error

## Step 4: Additional Targeted Searches (4 parallel searches)

### Search 4a: "site:alljobs.co.il junior developer software 2026"
- **Results:** Found AllJobs categories (Full Stack, Frontend, DevOps, QA, etc.)
- **Specific find:** Junior Backend Developer at a cybersecurity company (Java/Go), OMC Group, CodeValue, Junior QA at e-commerce company

### Search 4b: "junior backend developer Israel hiring 2026 entry level"
- **Results:** 403 backend developer jobs, 8 entry-level software engineer jobs on Glassdoor
- **Key companies:** Same top employers + new mentions (Mize, CodeValue, Invaya, Ravin AI, Consist Group, ART Medical, Pango, Anchor Fintech, Planck, My Mobile)

### Search 4c: "junior fullstack developer Israel Tel Aviv 2026 hiring"
- **Results:** 261 full stack developer jobs in Tel Aviv, 131 full stack web developer jobs in Israel
- **Salary data:** Junior full stack in Tel Aviv: NIS 15,000-25,000/month; average full stack Israel: NIS 264,947/year

### Search 4d: "junior frontend developer React Israel jobs March 2026"
- **Results:** 104 front-end developer jobs, 67 junior front-end web developer jobs, 399 web developer jobs in Israel
- **Key companies:** Ideo digital, Eternitech, Toonimo, YKM, LS Technologies, Sweep, GlassesUSA, Datarails, Apple, Code Oasis

## Step 5: More Platform Fetches and Searches (4 parallel)

### Fetch 5a: LinkedIn junior developer jobs page (full listing)
- **Result:** Successfully extracted 60 job listings with company, title, location, and posting date. This was the richest single source of specific jobs.

### Fetch 5b: startup.jobs Israel full-stack engineer
- **Result:** 403 Forbidden

### Search 5c: "remote junior developer jobs hiring Israel-based candidates 2026"
- **Results:** Found Arc, Indeed (20 remote jobs), Remote Rocketship, Dynamite Jobs, Glassdoor (451 remote jobs in Israel), Jobicy, Remotive
- **Salary data:** Remote jobs in Israel: $2.9k-$8.3k/month average, some up to $18.6k

### Search 5d: "junior Python developer Israel jobs 2026"
- **Results:** 153 junior Python jobs, 725 Python developer jobs on LinkedIn Israel
- **Key companies:** Eternitech, Abra, Varonis, VAST Data, Millennium Management, Sapiens

## Step 6: Remote and Startup Platform Fetches (3 parallel)

### Fetch 6a: Arc remote jobs for Israel
- **Result:** Successfully extracted 9 visible listings including freelance React/Next.js, QA Tester, Senior Engineer, Fullstack Go, Full Stack AI, plus full-time roles at Cornerstone OnDemand, Allied Benefit Systems, Toloka

### Fetch 6b: Expoint junior software engineer Israel
- **Result:** Certificate expired

### Fetch 6c: Built In Israel software engineer jobs
- **Result:** Successfully extracted listings including DraftKings (Junior Unity), CrowdStrike, monday.com (2 positions), plus senior roles at Navan, Silverfort, Datadog, ServiceNow, Snap Inc.

## Step 7: Company-Specific and Niche Searches (4 parallel)

### Search 7a: "Comeet jobs Israel junior developer 2026"
- **Specific finds:** PTC Junior Software Engineer in Herzliya (Creo 3D MCAD tool), inManage Junior Backend Developer (PHP)

### Search 7b: "new grad" OR "entry level" software engineer Israel 2026
- **Results:** 8 entry-level software engineer jobs, 2,000+ graduate software engineer on LinkedIn
- **Key find:** Junior Fullstack Engineer role requiring TypeScript, Node.js, ReactJS; requires recently completed CS degree with 90+ average

### Search 7c: "junior C# .NET developer Israel jobs 2026"
- **Results:** 118 C#/.NET developer jobs in Israel
- **Key companies:** YouAppi, Eternitech, Gini Apps, IronCircle, SAP, Earnix, BiltOn, MateHR, Mend, DRIVENETS, MPrest Defense

### Search 7d: "junior DevOps QA automation engineer Israel 2026 entry level"
- **Results:** 595 QA jobs in Israel, junior DevOps positions available
- **Salary data:** Entry-level QA: NIS 146,504/year; DevOps: NIS 225,100/year

## Step 8: Hebrew Board and Indeed Fetches + Big Company Search (3 parallel)

### Fetch 8a: Drushim.co.il junior jobs page
- **Result:** Successfully extracted listings including Kishrim Plus (Junior Software Developer, Petah Tikva, no experience), John Bryce (Junior Cloud Data Manager training), Yael Group (Junior System Admin), Harel Connect (Junior AI/Automation)

### Fetch 8b: Indeed Israel junior developer jobs
- **Result:** Found Express Academic free Junior Developer training program in Jerusalem (6-month bootcamp, Java/C/C++, requires degree with 85+ GPA)

### Search 8c: "Wix Fiverr monday.com Check Point junior graduate software engineer Israel 2026"
- **Key discovery:** Wix KickstartX 2026 program -- 7-month immersive program for junior developers (0-3 years), starts June 14, 2026. Registration opened March 25.

## Step 9: Graduate Programs and Large Company Searches (2 parallel)

### Search 9a: "Israel graduate programs tech companies 2026 hiring bootcamp junior engineers IDF graduates"
- **Results:** Found Israel Innovation Authority government program for juniors, Israel Tech Challenge bootcamp, MAMRAM pipeline info, geographic hub data

### Search 9b: "Comverse Amdocs SAP Labs Israel junior software developer positions 2026"
- **Results:** 12 Amdocs open positions in Israel, historical Amdocs junior hiring in Nazareth

## Step 10: Wix Program Details and Final Searches (3 parallel)

### Search 10a: "Wix KickstartX 2026 program junior developers Israel application details"
- **Key details extracted:** Full-time 7 months; on-site Tel Aviv (Glilot) 5 days/week; 2 months training + 5 months embedded in teams; registration opened March 25, 48-hour window; technical exam April 17; starts June 14, 2026

### Search 10b: "Israel tech companies hiring junior developers graduates 2026 Taboola CyberArk Playtika"
- **Results:** Playtika hiring Unity/Java developers, opening academies; Taboola ~30 positions in Israel; 18,000-25,000 estimated unfilled tech positions in Israel

### Fetch 10c: Wellfound Israel startup jobs
- **Result:** 403 Forbidden

## Step 11: Compiled Results
- Organized all findings into comprehensive results document at `results.md`
- Categorized by: explicit junior listings (17), accessible non-senior positions (42), Hebrew board listings (4), graduate programs (7), hiring companies, remote opportunities, salary benchmarks, job boards, and strategic tips
- Total specific job listings documented: 63+

## Summary of Sources Consulted

### Successfully Scraped (with specific job data)
1. LinkedIn Israel - junior developer jobs (60 listings)
2. LinkedIn Israel - junior software developer jobs (13 listings)
3. Built In Israel - software engineer jobs (5+ listings)
4. Arc.dev - remote jobs for Israel (9 listings)
5. Drushim.co.il - junior jobs (8+ listings)
6. Indeed Israel - junior developer (1 training program)

### Search Results Analyzed (aggregated data)
7. Glassdoor Israel (multiple category searches)
8. AllJobs.co.il
9. Comeet job platform
10. Wellfound/AngelList
11. Remote Rocketship
12. Dynamite Jobs
13. Jobicy
14. Remotive
15. Startup.jobs
16. Top Startups.io
17. Secret Tel Aviv Jobs
18. CareerJet Israel
19. GotFriends
20. Jobify360
21. JobSwipe
22. JUNIO
23. Poenta
24. DevJobs Israel

### Blocked (403/error)
- Glassdoor direct page fetch
- Secret Tel Aviv direct fetch
- JUNIO direct fetch (certificate expired)
- Expoint direct fetch (certificate expired)
- Startup.jobs direct fetch
- Wellfound direct fetch

## Tools and Approach
- Used `WebSearch` for broad queries across multiple search engines
- Used `WebFetch` to scrape specific job board pages for detailed listings
- Searched in both English and Hebrew to cover Israeli-specific boards
- Searched by role type (frontend, backend, fullstack, DevOps, QA), by technology (React, Python, Java, C#/.NET, Node.js), and by company
- Checked both traditional job boards and startup-specific platforms
- Investigated graduate/training programs as pipeline opportunities
- Collected salary benchmarks from multiple sources
