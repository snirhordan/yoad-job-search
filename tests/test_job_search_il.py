"""Tests for Issue #7: job-search-il skill — multi-site aggregated search with scoring."""
import pathlib
import re

SKILL_PATH = pathlib.Path.home() / "yoad" / ".claude" / "skills" / "job-search-il" / "SKILL.md"


class TestSkillFileStructure:
    """Verify SKILL.md has correct frontmatter."""

    def setup_method(self):
        assert SKILL_PATH.exists()
        self.content = SKILL_PATH.read_text()

    def test_has_name_frontmatter(self):
        assert "name: job-search-il" in self.content

    def test_has_description(self):
        assert "description:" in self.content

    def test_has_websearch_tool(self):
        assert "WebSearch" in self.content

    def test_has_webfetch_tool(self):
        assert "WebFetch" in self.content

    def test_has_argument_hint(self):
        assert "argument-hint" in self.content


class TestParallelSearchQueries:
    """Verify 8 parallel search queries (4 English, 4 Hebrew)."""

    def setup_method(self):
        self.content = SKILL_PATH.read_text()

    def test_english_indeed_il_query(self):
        assert "il.indeed.com" in self.content

    def test_english_janglo_query(self):
        assert "janglo.net" in self.content

    def test_english_wellfound_query(self):
        assert "wellfound.com" in self.content or "startup.jobs" in self.content

    def test_english_secrettelaviv_query(self):
        assert "secrettelaviv.com" in self.content

    def test_hebrew_alljobs_query(self):
        assert "alljobs.co.il" in self.content and "מפתח" in self.content

    def test_hebrew_drushim_query(self):
        assert "drushim.co.il" in self.content

    def test_hebrew_jobmaster_query(self):
        assert "jobmaster.co.il" in self.content

    def test_hebrew_gotfriends_query(self):
        assert "gotfriends.co.il" in self.content


class TestKeywordOverride:
    """Verify custom keywords replace defaults."""

    def setup_method(self):
        self.content = SKILL_PATH.read_text()

    def test_arguments_variable(self):
        assert "$ARGUMENTS" in self.content

    def test_custom_keyword_documentation(self):
        lower = self.content.lower()
        assert "keyword" in lower or "arguments" in lower


class TestWorkflow:
    """Verify the full workflow is documented."""

    def setup_method(self):
        self.content = SKILL_PATH.read_text()
        self.lower = self.content.lower()

    def test_prerequisites_check(self):
        assert "prerequisite" in self.lower or "preferences.md" in self.content

    def test_load_context_step(self):
        assert "preferences.md" in self.content

    def test_web_search_step(self):
        assert "WebSearch" in self.content

    def test_scoring_step(self):
        assert "score" in self.lower or "fit" in self.lower

    def test_enrichment_step(self):
        assert "webfetch" in self.lower or "enrich" in self.lower

    def test_save_history_step(self):
        assert "job-history.md" in self.content

    def test_present_results_step(self):
        assert "result" in self.lower or "present" in self.lower

    def test_indeed_mcp_tip(self):
        assert "Indeed" in self.content

    def test_feedback_loop(self):
        assert "feedback" in self.lower


class TestOutputFormat:
    """Verify output format matches spec."""

    def setup_method(self):
        self.content = SKILL_PATH.read_text()

    def test_top_matches_section(self):
        assert "Top Matches" in self.content

    def test_fit_in_output(self):
        assert "Fit" in self.content

    def test_source_in_output(self):
        assert "Source" in self.content

    def test_apply_url_in_output(self):
        lower = self.content.lower()
        assert "apply" in lower and "url" in lower

    def test_summary_section(self):
        lower = self.content.lower()
        assert "summary" in lower or "found" in lower


class TestPermissions:
    """Verify permissions section."""

    def setup_method(self):
        self.content = SKILL_PATH.read_text()

    def test_permissions_section(self):
        assert "Permissions" in self.content or "permissions" in self.content.lower()

    def test_yoad_jobs_read(self):
        assert ".yoad-jobs" in self.content
