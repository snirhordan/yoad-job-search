# Skill Benchmark: yoad-job-search

**Model**: claude-opus-4-6
**Date**: 2026-03-28
**Evals**: 4 (eval 3 ashby-remote excluded — agent timed out)
**Runs per config**: 1

## Summary

| Metric | With Skill | Without Skill | Delta |
|--------|-----------|---------------|-------|
| **Pass Rate** | **100%** ± 0% | 49% ± 35% | **+51%** |
| Time | 224.6s ± 79.3s | 170.1s ± 131.6s | +54.5s |
| Tokens | 38,238 ± 11,240 | 25,597 ± 17,570 | +12,641 |

## Per-Eval Results

| Eval | With Skill | Without Skill | Delta |
|------|-----------|---------------|-------|
| 1. israel-jobs (Fireblocks) | 100% (5/5) | 80% (4/5) | +20% |
| 2. israel-jobs (general) | 100% (4/4) | 0% (0/4) | +100% |
| 4. job-search-il (default) | 100% (5/5) | 40% (2/5) | +60% |
| 5. job-search-il (Python) | 100% (4/4) | 75% (3/4) | +25% |

## Discriminating Assertions

| Assertion | With Skill | Without Skill |
|-----------|:---------:|:------------:|
| Greenhouse JSON API used | PASS | FAIL |
| Hebrew search queries | PASS | Mixed |
| Fit scoring (High/Med/Low) | PASS | FAIL |
| ~/.yoad-jobs/ data dir | PASS | FAIL |
| Source attribution per listing | PASS | FAIL |
| Job titles in output | PASS | PASS |
| Apply URLs included | PASS | PASS |

## Analyst Notes

- With-skill achieves 100% pass rate (18/18) vs 49% without (9/18)
- Eval 2 is the strongest discriminator — baseline produced zero output
- Without-skill consistently fails on skill-specific behaviors: fit scoring, data directory, source attribution
- With-skill costs ~50% more tokens but delivers structured, reproducible results
- Eval 4 without-skill found JUNIO.co.il — junior-specific board to add to skill
- Ashby remote scanning needs optimization — agents timed out on batch API fetching
