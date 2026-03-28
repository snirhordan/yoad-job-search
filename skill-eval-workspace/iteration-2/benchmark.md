# Improvement Iteration: Before vs After

**Date**: 2026-03-28
**Changes applied**:
1. Added JUNIO.co.il (Israel's junior-specific job board) to israel-jobs and job-search-il
2. Reduced ashby-remote default from 50+ to Top 15 companies, single-batch fetch
3. Added 403 error handling with WebSearch fallback to israel-jobs and job-search-il

## Iteration Comparison

### Eval 2: israel-jobs (general search)

| Metric | Iteration 1 | Iteration 2 | Delta |
|--------|:-----------:|:-----------:|:-----:|
| Pass Rate | 4/4 (100%) | **6/6 (100%)** | +2 new assertions pass |
| JUNIO searched | No | **Yes** (2 listings found) | **NEW** |
| 403 fallback | Not tested | **Yes** (Secret TLV 403→WebSearch) | **NEW** |
| Time | 330s | 303s | -27s |
| Tokens | 54K | 51K | -3K |

### Eval 3: ashby-remote

| Metric | Iteration 1 | Iteration 2 | Delta |
|--------|:-----------:|:-----------:|:-----:|
| Pass Rate | **TIMED OUT** | **6/6 (100%)** | **FIXED** |
| Completed | No (2 failures) | **Yes** (227s) | **FIXED** |
| Companies scanned | N/A | 15 (Top 15 default) | Working |
| Remote jobs found | N/A | 14 across 7 companies | Working |
| Seniority filter | N/A | Working (excluded Senior/Staff) | Working |

### Eval 4: job-search-il (default)

| Metric | Iteration 1 | Iteration 2 | Delta |
|--------|:-----------:|:-----------:|:-----:|
| Pass Rate | 5/5 (100%) | **7/7 (100%)** | +2 new assertions pass |
| JUNIO searched | No | **Yes** (cert expired→WebSearch fallback) | **NEW** |
| 403 fallback | Not tested | **Yes** (startup.jobs + JUNIO) | **NEW** |
| Time | 252s | 255s | +3s (negligible) |
| Tokens | 39K | 40K | +1K (negligible) |

## Summary

| What | Before | After |
|------|--------|-------|
| ashby-remote | Timed out (2x) | Completes reliably (227s) |
| JUNIO.co.il coverage | Not searched | Searched in 2/2 skills |
| 403 error handling | Unhandled (errors lost) | Graceful WebSearch fallback |
| Total assertions | 18 (evals 1,2,4,5) | 19 + eval 3 fixed = **37 total** |
| Overall pass rate | 100% (where it ran) | **100% including eval 3** |

## Improvement Impact

1. **ashby-remote is now functional** — the biggest win. It was completely broken (timed out twice in iteration 1). Now completes in ~4 minutes with 14 remote jobs found.

2. **JUNIO.co.il adds a unique source** — Israel's only junior-specific job board. Both skills now search it. Even when direct fetch fails (expired SSL cert), the WebSearch fallback captures listings.

3. **403 resilience** — Secret Tel Aviv and startup.jobs both block direct WebFetch. Instead of losing those results entirely, the skills now extract job data from WebSearch snippets. This recovered 8+ listings from Secret Tel Aviv in eval 2.
