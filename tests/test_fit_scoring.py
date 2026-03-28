"""Tests for Issue #6: Fit scoring, deduplication, and history tracking."""
import pathlib

PROJECT_DIR = pathlib.Path.home() / "yoad"
DATA_DIR = pathlib.Path.home() / ".yoad-jobs"


class TestScoringInJobSearchIl:
    """Verify job-search-il skill has fit scoring logic."""

    def setup_method(self):
        self.skill = (PROJECT_DIR / ".claude" / "skills" / "job-search-il" / "SKILL.md").read_text()

    def test_high_fit_criteria(self):
        lower = self.skill.lower()
        assert "high" in lower and "fit" in lower

    def test_medium_fit_criteria(self):
        lower = self.skill.lower()
        assert "medium" in lower and "fit" in lower

    def test_low_fit_criteria(self):
        lower = self.skill.lower()
        assert "low" in lower and "fit" in lower

    def test_skip_criteria(self):
        lower = self.skill.lower()
        assert "skip" in lower

    def test_dealbreaker_check(self):
        lower = self.skill.lower()
        assert "dealbreaker" in lower or "deal" in lower

    def test_junior_swe_high_fit(self):
        lower = self.skill.lower()
        assert "junior" in lower


class TestDeduplication:
    """Verify deduplication logic is documented."""

    def setup_method(self):
        self.skill = (PROJECT_DIR / ".claude" / "skills" / "job-search-il" / "SKILL.md").read_text()

    def test_deduplication_by_company_title(self):
        lower = self.skill.lower()
        assert "dedup" in lower or "duplicate" in lower

    def test_checks_against_history(self):
        assert "job-history.md" in self.skill


class TestHistoryAppendFormat:
    """Verify history tracking format."""

    def setup_method(self):
        self.skill = (PROJECT_DIR / ".claude" / "skills" / "job-search-il" / "SKILL.md").read_text()

    def test_date_in_history(self):
        assert "DATE" in self.skill or "date" in self.skill.lower()

    def test_table_format(self):
        assert "| Job Title" in self.skill or "| Title" in self.skill

    def test_company_in_table(self):
        assert "Company" in self.skill

    def test_source_in_table(self):
        assert "Source" in self.skill

    def test_fit_in_table(self):
        assert "Fit" in self.skill

    def test_url_in_table(self):
        assert "URL" in self.skill or "url" in self.skill


class TestPostingSave:
    """Verify high-fit postings are saved."""

    def setup_method(self):
        self.skill = (PROJECT_DIR / ".claude" / "skills" / "job-search-il" / "SKILL.md").read_text()

    def test_save_to_jobs_dir(self):
        assert "jobs/" in self.skill or ".yoad-jobs" in self.skill

    def test_posting_md_format(self):
        assert "posting.md" in self.skill


class TestScoringInIsraelJobs:
    """Verify israel-jobs skill also has scoring/history references."""

    def setup_method(self):
        self.skill = (PROJECT_DIR / ".claude" / "skills" / "israel-jobs" / "SKILL.md").read_text()

    def test_history_append(self):
        assert "job-history.md" in self.skill

    def test_high_fit_save(self):
        lower = self.skill.lower()
        assert "high" in lower and ("fit" in lower or "save" in lower)


class TestScoringInAshbyRemote:
    """Verify ashby-remote skill has history tracking."""

    def setup_method(self):
        self.skill = (PROJECT_DIR / ".claude" / "skills" / "ashby-remote" / "SKILL.md").read_text()

    def test_history_append(self):
        assert "job-history.md" in self.skill

    def test_high_fit_save(self):
        lower = self.skill.lower()
        assert "high" in lower or "save" in lower
