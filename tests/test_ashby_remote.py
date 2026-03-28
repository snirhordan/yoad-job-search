"""Tests for Issue #5: ashby-remote skill — worldwide remote job scanner."""
import pathlib
import re

SKILL_PATH = pathlib.Path.home() / "yoad" / ".claude" / "skills" / "ashby-remote" / "SKILL.md"


class TestSkillFileStructure:
    """Verify SKILL.md has correct frontmatter."""

    def setup_method(self):
        assert SKILL_PATH.exists(), "ashby-remote SKILL.md must exist"
        self.content = SKILL_PATH.read_text()

    def test_has_name_frontmatter(self):
        assert "name: ashby-remote" in self.content

    def test_has_description_frontmatter(self):
        assert "description:" in self.content

    def test_has_webfetch_tool(self):
        assert "WebFetch" in self.content


class TestAshbyCompanyList:
    """Verify 50+ Ashby companies are listed."""

    def setup_method(self):
        self.content = SKILL_PATH.read_text()

    def test_has_top_15_and_extended(self):
        endpoints = len(re.findall(r"ashbyhq\.com/posting-api/job-board/", self.content))
        assert endpoints >= 40, f"Expected 40+ Ashby endpoints (top 15 + extended), found {endpoints}"

    def test_top_15_section_exists(self):
        assert "Top 15" in self.content

    def test_extended_list_section_exists(self):
        assert "Extended" in self.content

    def test_default_scan_is_top_15(self):
        lower = self.content.lower()
        assert "default" in lower and "15" in lower

    def test_has_openai(self):
        assert "openai" in self.content.lower()

    def test_has_cursor(self):
        assert "cursor" in self.content.lower()

    def test_has_linear(self):
        assert "linear" in self.content.lower()

    def test_has_notion(self):
        assert "notion" in self.content.lower()

    def test_has_supabase(self):
        assert "supabase" in self.content.lower()

    def test_has_deel(self):
        assert "deel" in self.content.lower()

    def test_has_snyk(self):
        assert "snyk" in self.content.lower()


class TestRemoteFiltering:
    """Verify remote filtering instructions."""

    def setup_method(self):
        self.content = SKILL_PATH.read_text()

    def test_isremote_filter(self):
        assert "isRemote" in self.content

    def test_workplace_type_filter(self):
        assert "workplaceType" in self.content or "Remote" in self.content

    def test_remote_keyword(self):
        assert "Remote" in self.content


class TestSeniorityFilter:
    """Verify seniority exclusion for junior-appropriate results."""

    def setup_method(self):
        self.content = SKILL_PATH.read_text()
        self.lower = self.content.lower()

    def test_title_filter_developer(self):
        assert "developer" in self.lower

    def test_title_filter_engineer(self):
        assert "engineer" in self.lower

    def test_title_filter_junior(self):
        assert "junior" in self.lower

    def test_exclude_senior(self):
        assert "senior" in self.lower

    def test_exclude_staff(self):
        assert "staff" in self.lower

    def test_exclude_principal(self):
        assert "principal" in self.lower

    def test_exclude_director(self):
        assert "director" in self.lower


class TestBatchProcessing:
    """Verify batch processing to avoid rate limits."""

    def setup_method(self):
        self.content = SKILL_PATH.read_text()
        self.lower = self.content.lower()

    def test_single_batch_instruction(self):
        lower = self.content.lower()
        assert "single batch" in lower or "do not split" in lower, "Should instruct single-batch fetching to avoid timeouts"


class TestOutputFormat:
    """Verify output format and history tracking."""

    def setup_method(self):
        self.content = SKILL_PATH.read_text()

    def test_history_append(self):
        assert "job-history.md" in self.content

    def test_apply_url_in_output(self):
        lower = self.content.lower()
        assert "apply" in lower and "url" in lower

    def test_summary_total(self):
        lower = self.content.lower()
        assert "total" in lower or "summary" in lower

    def test_arguments_support(self):
        assert "$ARGUMENTS" in self.content
