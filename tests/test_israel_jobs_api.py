"""Tests for Issue #3: israel-jobs skill — API-based company queries."""
import pathlib
import re

SKILL_PATH = pathlib.Path.home() / "yoad" / ".claude" / "skills" / "israel-jobs" / "SKILL.md"


class TestSkillFileStructure:
    """Verify SKILL.md has correct frontmatter and structure."""

    def setup_method(self):
        assert SKILL_PATH.exists(), "israel-jobs SKILL.md must exist"
        self.content = SKILL_PATH.read_text()

    def test_has_name_frontmatter(self):
        assert "name: israel-jobs" in self.content

    def test_has_description_frontmatter(self):
        assert "description:" in self.content

    def test_has_allowed_tools(self):
        assert "WebFetch" in self.content

    def test_has_websearch_tool(self):
        assert "WebSearch" in self.content


class TestIsraeliCompanyEndpoints:
    """Verify 35+ Israeli companies are listed with API endpoints."""

    def setup_method(self):
        self.content = SKILL_PATH.read_text()

    def test_minimum_35_companies(self):
        # Count Greenhouse API lines
        greenhouse = len(re.findall(r"boards-api\.greenhouse\.io", self.content))
        ashby = len(re.findall(r"ashbyhq\.com", self.content))
        lever = len(re.findall(r"lever\.co", self.content))
        total = greenhouse + ashby + lever
        assert total >= 35, f"Expected 35+ company endpoints, found {total}"

    def test_has_greenhouse_section(self):
        assert "Greenhouse" in self.content

    def test_has_ashby_section(self):
        assert "Ashby" in self.content

    def test_key_israeli_company_fireblocks(self):
        assert "fireblocks" in self.content.lower()

    def test_key_israeli_company_monday(self):
        assert "monday" in self.content.lower()

    def test_key_israeli_company_wix(self):
        assert "wix" in self.content.lower()

    def test_key_israeli_company_melio(self):
        assert "melio" in self.content.lower()

    def test_key_israeli_company_taboola(self):
        assert "taboola" in self.content.lower()

    def test_key_israeli_company_payoneer(self):
        assert "payoneer" in self.content.lower()

    def test_key_israeli_company_honeybook(self):
        assert "honeybook" in self.content.lower()

    def test_key_israeli_company_appsflyer(self):
        assert "appsflyer" in self.content.lower()


class TestCompanyQueryInstructions:
    """Verify company-specific query instructions."""

    def setup_method(self):
        self.content = SKILL_PATH.read_text()

    def test_company_specific_instructions(self):
        lower = self.content.lower()
        assert "company-specific" in lower or "specific" in lower

    def test_webfetch_instruction(self):
        assert "WebFetch" in self.content

    def test_apply_url_instruction(self):
        lower = self.content.lower()
        assert "apply" in lower and "url" in lower

    def test_history_append_instruction(self):
        assert "job-history.md" in self.content

    def test_arguments_variable(self):
        assert "$ARGUMENTS" in self.content
