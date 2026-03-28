"""Tests for Issue #4: israel-jobs skill — Hebrew + English web board search."""
import pathlib

SKILL_PATH = pathlib.Path.home() / "yoad" / ".claude" / "skills" / "israel-jobs" / "SKILL.md"


class TestIsraeliJobBoards:
    """Verify all 10 Israeli job board sites are listed."""

    def setup_method(self):
        self.content = SKILL_PATH.read_text()

    def test_junio_listed(self):
        assert "junio.co.il" in self.content

    def test_alljobs_listed(self):
        assert "alljobs.co.il" in self.content

    def test_drushim_listed(self):
        assert "drushim.co.il" in self.content

    def test_jobmaster_listed(self):
        assert "jobmaster.co.il" in self.content

    def test_gotfriends_listed(self):
        assert "gotfriends.co.il" in self.content

    def test_indeed_il_listed(self):
        assert "il.indeed.com" in self.content

    def test_goozali_listed(self):
        assert "goozali.com" in self.content

    def test_janglo_listed(self):
        assert "janglo.net" in self.content

    def test_secret_tlv_listed(self):
        assert "secrettelaviv.com" in self.content

    def test_wellfound_listed(self):
        assert "wellfound.com" in self.content


class TestHebrewKeywords:
    """Verify Hebrew keyword translation table."""

    def setup_method(self):
        self.content = SKILL_PATH.read_text()

    def test_hebrew_software_developer(self):
        assert "מפתח" in self.content and "תוכנה" in self.content

    def test_hebrew_programmer(self):
        assert "מתכנת" in self.content

    def test_hebrew_software_engineer(self):
        assert "מהנדס" in self.content

    def test_hebrew_junior(self):
        assert "ג'וניור" in self.content

    def test_hebrew_entry_level(self):
        assert "ניסיון" in self.content or "מתחילים" in self.content

    def test_hebrew_fullstack(self):
        assert "פול סטאק" in self.content or "full stack" in self.content.lower()

    def test_hebrew_backend(self):
        assert "בקאנד" in self.content or "צד שרת" in self.content

    def test_hebrew_frontend(self):
        assert "פרונטאנד" in self.content or "צד לקוח" in self.content


class TestWebSearchPatterns:
    """Verify WebSearch patterns for Israeli sites."""

    def setup_method(self):
        self.content = SKILL_PATH.read_text()

    def test_site_filter_alljobs(self):
        assert "site:alljobs.co.il" in self.content

    def test_site_filter_drushim(self):
        assert "site:drushim.co.il" in self.content

    def test_hebrew_search_example(self):
        # Should have a Hebrew search pattern example
        assert "מפתח תוכנה" in self.content and "site:" in self.content

    def test_english_search_example(self):
        lower = self.content.lower()
        assert "junior developer" in lower and "site:" in lower

    def test_source_attribution_mentioned(self):
        lower = self.content.lower()
        assert "source" in lower

    def test_deduplication_mentioned(self):
        lower = self.content.lower()
        assert "dedup" in lower or "duplicate" in lower


class TestErrorHandling:
    """Verify 403 error handling instructions."""

    def setup_method(self):
        self.content = SKILL_PATH.read_text()

    def test_403_handling_documented(self):
        assert "403" in self.content

    def test_fallback_to_websearch(self):
        lower = self.content.lower()
        assert "fall back" in lower or "fallback" in lower
