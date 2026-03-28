"""Smoke tests: verify a sample of API endpoints are reachable."""
import requests
import pytest


TIMEOUT = 10


class TestGreenhouseEndpoints:
    """Verify sample Greenhouse API endpoints return valid JSON."""

    @pytest.mark.parametrize("company,url", [
        ("fireblocks", "https://boards-api.greenhouse.io/v1/boards/fireblocks/jobs"),
        ("taboola", "https://boards-api.greenhouse.io/v1/boards/taboola/jobs"),
        ("melio", "https://boards-api.greenhouse.io/v1/boards/melio/jobs"),
    ])
    def test_greenhouse_endpoint_reachable(self, company, url):
        resp = requests.get(url, timeout=TIMEOUT)
        assert resp.status_code == 200, f"{company} endpoint returned {resp.status_code}"
        data = resp.json()
        assert "jobs" in data, f"{company}: expected 'jobs' key in response"


class TestAshbyEndpoints:
    """Verify sample Ashby API endpoints return valid JSON."""

    @pytest.mark.parametrize("company,url", [
        ("linear", "https://api.ashbyhq.com/posting-api/job-board/linear"),
        ("supabase", "https://api.ashbyhq.com/posting-api/job-board/supabase"),
        ("deel", "https://api.ashbyhq.com/posting-api/job-board/deel"),
    ])
    def test_ashby_endpoint_reachable(self, company, url):
        resp = requests.get(url, timeout=TIMEOUT)
        assert resp.status_code == 200, f"{company} endpoint returned {resp.status_code}"
        data = resp.json()
        assert "jobs" in data, f"{company}: expected 'jobs' key in response"


class TestAshbyRemoteFieldExists:
    """Verify Ashby API responses include remote/location fields we filter on."""

    def test_ashby_jobs_have_remote_field(self):
        resp = requests.get(
            "https://api.ashbyhq.com/posting-api/job-board/linear",
            timeout=TIMEOUT
        )
        data = resp.json()
        if data["jobs"]:
            job = data["jobs"][0]
            # Ashby jobs should have location or isRemote fields
            assert "isRemote" in job or "location" in job, (
                f"Expected isRemote or location field, got keys: {list(job.keys())}"
            )
