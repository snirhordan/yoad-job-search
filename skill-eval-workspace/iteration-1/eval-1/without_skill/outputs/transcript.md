# Transcript: Fireblocks Job Search for Yoad

## Task
Find open developer positions at Fireblocks for a new CS graduate based in Israel.

## Approach
Used direct HTTP requests to Fireblocks' careers page and their Greenhouse job board to scrape current openings. No special skills or external APIs were used -- just curl and Python parsing.

## Steps Taken

### Step 1: Fetch Fireblocks Careers Page
- **Command:** `curl -s -L "https://www.fireblocks.com/careers/"`
- **Result:** Got the main careers page HTML (308 KB). Confirmed Fireblocks uses Greenhouse as their ATS.

### Step 2: Fetch Greenhouse Job Board
- **Command:** `curl -s -L "https://boards.greenhouse.io/fireblocks"`
- **Result:** Got the Greenhouse job board HTML (62 KB) containing embedded JSON data with all open positions.

### Step 3: Extract Job Data from HTML
- Used `grep` to extract title, location, and URL fields from the embedded JSON.
- **Result:** Identified 50 total open positions across all departments and locations.

### Step 4: Parse Full JSON Data
- Used Python to locate and parse the embedded JSON array in the Greenhouse HTML.
- Successfully extracted all 50 job objects with full metadata (id, title, location, department, absolute_url, published_at).

### Step 5: Filter for Israel-Based Positions
- Filtered by location containing "Israel" or "Tel Aviv".
- **Result:** Found 9 Israel-based positions (8 in R&D, 1 in Legal & Compliance).

### Step 6: Check for Junior/Entry-Level Roles
- Searched all 50 positions for keywords: junior, entry, associate, graduate, intern, jr.
- **Result:** No junior/entry-level developer positions found. The word "Associate" appeared only in Legal/Compliance roles.

### Step 7: Analyze All R&D Positions
- Listed all 25 R&D positions globally to understand hiring patterns.
- Found that 8 of 25 R&D positions are in Israel (Tel Aviv).
- All Israel R&D roles are "Senior" level except "Technical Integration Engineer."

## Key Findings
- **50 total positions** at Fireblocks globally.
- **9 positions in Israel** (Tel Aviv), of which **8 are R&D/dev roles**.
- **No junior/entry-level dev roles** are currently listed.
- **Best match for a new grad:** Technical Integration Engineer (no "Senior" prefix, recently posted).
- Fireblocks is a blockchain/digital-asset infrastructure company headquartered in New York with a large R&D center in Tel Aviv.

## Data Sources
- Primary: https://job-boards.greenhouse.io/fireblocks (Greenhouse job board, scraped 2026-03-28)
- Secondary: https://www.fireblocks.com/careers/ (company careers page)

## Tools Used
- `curl` for HTTP requests
- Python 3 with `re` and `json` modules for HTML/JSON parsing
- No external APIs, browser automation, or special skills were used
