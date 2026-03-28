"""Tests for Issue #8: Indeed MCP integration and CLAUDE.md documentation."""
import pathlib

PROJECT_DIR = pathlib.Path.home() / "yoad"


class TestClaudeMdIndeedSection:
    """Verify CLAUDE.md documents Indeed MCP as a first-class source."""

    def setup_method(self):
        self.claude_md = PROJECT_DIR / "CLAUDE.md"
        assert self.claude_md.exists(), "CLAUDE.md must exist"
        self.content = self.claude_md.read_text()

    def test_indeed_mcp_section_exists(self):
        assert "Indeed MCP" in self.content

    def test_indeed_example_queries(self):
        lower = self.content.lower()
        assert "junior software developer" in lower or "junior developer" in lower

    def test_indeed_israel_query(self):
        assert "Israel" in self.content

    def test_indeed_remote_query(self):
        lower = self.content.lower()
        assert "remote" in lower

    def test_indeed_in_job_sources_table(self):
        assert "Indeed" in self.content and ("MCP" in self.content or "indeed" in self.content.lower())

    def test_indeed_positioned_as_equal_partner(self):
        lower = self.content.lower()
        assert "equal partner" in lower, "Indeed MCP should be documented as equal partner"

    def test_indeed_setup_instructions(self):
        lower = self.content.lower()
        # Should mention how to use it (connector, settings, etc.)
        assert "connector" in lower or "enabled" in lower or "setting" in lower


class TestJobSearchIlMentionsIndeed:
    """Verify job-search-il skill references Indeed MCP as supplementary tip."""

    def setup_method(self):
        self.skill_path = PROJECT_DIR / ".claude" / "skills" / "job-search-il" / "SKILL.md"
        assert self.skill_path.exists()
        self.content = self.skill_path.read_text()

    def test_indeed_mcp_tip_in_skill(self):
        assert "Indeed" in self.content, "job-search-il should mention Indeed MCP"


class TestClaudeMdJobSourcesTable:
    """Verify CLAUDE.md has a comprehensive job sources table."""

    def setup_method(self):
        self.content = (PROJECT_DIR / "CLAUDE.md").read_text()

    def test_source_table_has_alljobs(self):
        assert "AllJobs" in self.content

    def test_source_table_has_drushim(self):
        assert "Drushim" in self.content

    def test_source_table_has_indeed_il(self):
        assert "il.indeed.com" in self.content or "Indeed Israel" in self.content

    def test_source_table_has_goozali(self):
        assert "Goozali" in self.content

    def test_source_table_has_janglo(self):
        assert "Janglo" in self.content

    def test_source_table_has_ashby(self):
        assert "Ashby" in self.content

    def test_source_table_has_greenhouse(self):
        assert "Greenhouse" in self.content
