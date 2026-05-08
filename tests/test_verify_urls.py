"""Tests for tools/verify_urls.py.

Network-bearing tests are skipped by default; the offline path
(syntax + collection) is fully exercised.

Run with::

    python -m unittest tests.test_verify_urls -v
"""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.verify_urls import (  # noqa: E402
    UrlOutcome,
    _check_host_ssrf,
    collect_urls,
    main,
    render_summary,
    verify_one,
    verify_syntax,
)

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"


class SyntaxTests(unittest.TestCase):
    def test_https_url_ok(self) -> None:
        ok, _ = verify_syntax("https://arxiv.org/abs/2505.10568")
        self.assertTrue(ok)

    def test_http_url_ok(self) -> None:
        ok, _ = verify_syntax("http://arxiv.org/")
        self.assertTrue(ok)

    def test_ftp_rejected(self) -> None:
        ok, detail = verify_syntax("ftp://arxiv.org/")
        self.assertFalse(ok)
        self.assertIn("non-http scheme", detail)

    def test_no_netloc_rejected(self) -> None:
        ok, detail = verify_syntax("https://")
        self.assertFalse(ok)
        self.assertIn("empty netloc", detail)

    def test_unknown_host_rejected(self) -> None:
        ok, detail = verify_syntax("https://attacker.example.com/")
        self.assertFalse(ok)
        self.assertIn("not in allowlist", detail)


class SSRFGuardTests(unittest.TestCase):
    """Unit tests for _check_host_ssrf SSRF mitigations (CWE-918)."""

    def test_ip_literal_ipv4_rejected(self) -> None:
        ok, detail = _check_host_ssrf("127.0.0.1")
        self.assertFalse(ok)
        self.assertIn("IP literal", detail)

    def test_ip_literal_private_rejected(self) -> None:
        ok, detail = _check_host_ssrf("10.0.0.1")
        self.assertFalse(ok)
        self.assertIn("IP literal", detail)

    def test_ip_literal_metadata_endpoint(self) -> None:
        ok, detail = _check_host_ssrf("169.254.169.254")
        self.assertFalse(ok)
        self.assertIn("IP literal", detail)

    def test_ip_literal_ipv6_loopback_rejected(self) -> None:
        # urlparse delivers netloc as "[::1]" with brackets for IPv6
        ok, detail = _check_host_ssrf("[::1]")
        self.assertFalse(ok)
        self.assertIn("IP literal", detail)

    def test_unknown_host_rejected(self) -> None:
        ok, detail = _check_host_ssrf("attacker.example.com")
        self.assertFalse(ok)
        self.assertIn("not in allowlist", detail)

    def test_allowlisted_host_accepted(self) -> None:
        ok, _ = _check_host_ssrf("arxiv.org")
        self.assertTrue(ok)

    def test_allowlisted_doi_host_accepted(self) -> None:
        ok, _ = _check_host_ssrf("doi.org")
        self.assertTrue(ok)


class CollectTests(unittest.TestCase):
    def test_collect_from_real_data(self) -> None:
        triples = collect_urls(DATA_DIR)
        self.assertGreater(len(triples), 0)
        kinds = {kind for _, _, kind in triples}
        self.assertEqual(kinds, {"evidence", "timeline"})
        for rid, url, _ in triples:
            self.assertTrue(rid.startswith("evidence:") or rid.startswith("event:"))
            self.assertTrue(url.startswith("http"))


class OfflineVerifyTests(unittest.TestCase):
    def test_offline_returns_unchecked(self) -> None:
        outcome = verify_one(
            "evidence:test", "https://arxiv.org/abs/0001", "evidence", network=False
        )
        self.assertEqual(outcome.status, "unchecked")

    def test_offline_invalid_syntax_returns_dead(self) -> None:
        outcome = verify_one(
            "evidence:bad", "ftp://example.org/", "evidence", network=False
        )
        self.assertEqual(outcome.status, "dead")
        self.assertIn("non-http scheme", outcome.detail)


class RenderTests(unittest.TestCase):
    def test_render_includes_status_buckets(self) -> None:
        outcomes = [
            UrlOutcome("evidence:a", "https://a/", "evidence", "alive", 200, "ok"),
            UrlOutcome("evidence:b", "https://b/", "evidence", "dead", 404, "x"),
        ]
        text = render_summary(outcomes)
        self.assertIn("alive: 1", text)
        self.assertIn("dead: 1", text)


class CLIOfflineTests(unittest.TestCase):
    def test_main_offline_returns_zero_when_all_unchecked(self) -> None:
        with TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            ev_payload = {
                "@graph": [
                    {
                        "id": "evidence:x",
                        "type": "Paper",
                        "label": "x",
                        "url": "https://arxiv.org/abs/test",
                    }
                ]
            }
            tl_payload = {"@graph": []}
            (tmp_path / "evidence.json").write_text(
                json.dumps(ev_payload), encoding="utf-8"
            )
            (tmp_path / "timeline.json").write_text(
                json.dumps(tl_payload), encoding="utf-8"
            )
            exit_code = main(["--data", str(tmp_path)])
            self.assertEqual(exit_code, 0)


if __name__ == "__main__":
    unittest.main()
