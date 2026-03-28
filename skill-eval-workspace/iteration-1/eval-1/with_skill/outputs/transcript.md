# Transcript -- Fireblocks Job Search for Yoad Hordan

**Date**: 2026-03-28
**Task**: Search for open positions at Fireblocks for a new CS graduate based in Israel

## Steps Taken

### Step 1: Read the skill file
- **Tool**: Read
- **File**: `/home/snirhordan/yoad/.claude/skills/israel-jobs/SKILL.md`
- **Result**: Found the skill instructions including the company lookup table. Located Fireblocks in the Greenhouse API table with endpoint `https://boards-api.greenhouse.io/v1/boards/fireblocks/jobs`.

### Step 2: Fetch the Greenhouse API endpoint
- **Tool**: WebFetch
- **URL**: `https://boards-api.greenhouse.io/v1/boards/fireblocks/jobs`
- **Prompt**: Requested all jobs with title, location, department, salary, and apply URL (absolute_url field). Asked to highlight junior/entry-level and Israel-based positions.
- **Result**: Retrieved 65 total open positions. Jobs grouped by department. No salary data disclosed. No explicitly junior/entry-level roles found.

### Step 3: Check Yoad's preferences and job history
- **Tool**: Read
- **Files**: `~/.yoad-jobs/preferences.md` and `~/.yoad-jobs/job-history.md`
- **Result**: Preferences confirm Yoad is looking for junior/entry-level dev roles in Israel, open to any tech stack. Job history was empty (first search).

### Step 4: Filter and analyze results
- Filtered 17 Israel-based positions (all in Tel Aviv)
- Identified 10 engineering roles in Israel
- Found 0 explicitly junior/entry-level positions
- Identified 3 roles without "Senior" prefix that might accept a strong new grad:
  1. Application Security Engineer
  2. Information Security Engineer
  3. Technical Integration Engineer

### Step 5: Save results
- **Tool**: Write
- **File**: `/home/snirhordan/yoad/skill-eval-workspace/iteration-1/eval-1/with_skill/outputs/results.md`
- Full structured output with tables, groupings, and recommendations

### Step 6: Update job history
- **Tool**: Edit
- **File**: `~/.yoad-jobs/job-history.md`
- Appended all 17 Israel-based Fireblocks positions for deduplication in future searches

## Key Findings

1. **65 total positions** at Fireblocks across all locations
2. **17 positions in Israel** (all Tel Aviv), of which 10 are engineering/technical
3. **0 junior/entry-level positions** -- all engineering roles are Senior, Staff, Lead, or Director level
4. **No salary information** disclosed in any listing
5. **Recommendation**: Fireblocks is not currently a good fit for a new CS graduate. Suggested monitoring their careers page and looking at companies with known junior hiring programs (Wix, Monday, Check Point, Playtika).

## Tools Used
- Read (3 calls)
- ToolSearch (1 call -- to load WebFetch schema)
- WebFetch (1 call)
- Bash (2 calls -- directory creation and checking yoad-jobs dir)
- Edit (1 call -- update job history)
- Write (2 calls -- results.md and transcript.md)
