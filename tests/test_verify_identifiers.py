"""Tests for tools/verify_identifiers.py — DOI + ISBN structural / network checks.

Network paths are exercised via mock; the CI offline path runs the
``--no-network`` default against real evidence data and must exit 0
because the v0.7.0 graph carries no broken DOI / ISBN values.
"""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import mock
from urllib.error import HTTPError

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from tools import verify_identifiers as vi  # noqa: E402


SAMPLE_EVIDENCE = {
    "@context": "./context.jsonld",
    "@graph": [
        {
            "id": "evidence:doi_valid",
            "type": "Paper",
            "label": "Valid DOI sample",
            "doi": "10.4171/PRIMS/57-1-1",
        },
        {
            "id": "evidence:isbn13_valid",
            "type": "Book",
            "label": "Valid ISBN-13 sample (Kato 2019)",
            "isbn": "978-4-04-400417-0",
        },
        {
            "id": "evidence:isbn10_valid",
            "type": "Book",
            "label": "Valid ISBN-10 sample (well-known fixture: Practical Common Lisp)",
            "isbn": "1-59059-239-5",
        },
        {
            "id": "evidence:doi_invalid",
            "type": "Paper",
            "label": "Invalid DOI sample (no slash)",
            "doi": "not-a-doi",
        },
        {
            "id": "evidence:isbn_invalid_checksum",
            "type": "Book",
            "label": "Invalid ISBN-13 sample (last digit wrong)",
            "isbn": "978-4-04-400417-9",
        },
    ],
}


def _write_sample(data_dir: Path) -> None:
    (data_dir / "evidence.json").write_text(
        json.dumps(SAMPLE_EVIDENCE, indent=2) + "\n", encoding="utf-8"
    )


class IsbnChecksumTests(unittest.TestCase):
    def test_isbn13_valid(self) -> None:
        ok, detail = vi.validate_isbn("978-4-04-400417-0")
        self.assertTrue(ok, detail)
        self.assertIn("isbn-13", detail)

    def test_isbn13_round7_kato_correct(self) -> None:
        # Round 7 audit replaced the fabricated 978-4-04-110262-7 with this.
        ok, _ = vi.validate_isbn("978-4-04-400417-0")
        self.assertTrue(ok)

    def test_isbn13_round7_fabricated_fails_checksum(self) -> None:
        # Happy finding: the v0.6.1 Round-7 audit caught this fabrication
        # via cross-source verification (KADOKAWA / hanmoto / Kinokuniya),
        # but ISBN-13 checksum **alone** would have caught it too. This
        # test pins that fact down so a future maintainer can rely on
        # ``verify_identifiers.py`` as a *structural* defence against
        # this class of fabrication, in addition to the cross-source
        # check that remains the gold standard.
        ok, detail = vi.validate_isbn("978-4-04-110262-7")
        self.assertFalse(ok)
        self.assertIn("checksum", detail)

    def test_isbn13_bad_checksum(self) -> None:
        ok, detail = vi.validate_isbn("978-4-04-400417-9")
        self.assertFalse(ok)
        self.assertIn("checksum", detail)

    def test_isbn13_bad_prefix(self) -> None:
        ok, detail = vi.validate_isbn("123-4-04-400417-0")
        self.assertFalse(ok)
        self.assertIn("prefix", detail)

    def test_isbn10_valid(self) -> None:
        # "Practical Common Lisp" — well-known stable test fixture
        ok, _ = vi.validate_isbn("1-59059-239-5")
        self.assertTrue(ok)

    def test_isbn10_x_check_digit(self) -> None:
        # ISBN-10 "0-7864-0700-X" — the X represents check value 10 per
        # ISO 2108 modulo-11 rule. Sum of digit*weight = 0+63+64+42+24+
        # 0+28+0+0+10 = 231; 231 mod 11 = 0 ⇒ valid.
        ok, _ = vi.validate_isbn("0-7864-0700-X")
        self.assertTrue(ok)

    def test_isbn_wrong_length(self) -> None:
        ok, detail = vi.validate_isbn("123456")
        self.assertFalse(ok)
        self.assertIn("length", detail)

    def test_unicode_dash_isbn_strip(self) -> None:
        # Round 9 audit (v0.7.8): regression test for v0.7.7 Unicode-dash
        # NFKC + Pd category strip. en-dash (U+2013) and em-dash (U+2014)
        # in a JP-pasted ISBN must reduce to the same valid digits.
        # 978-4-04-400417-0 (Kato 2019) variants:
        en_dash_isbn = "978–4–04–400417–0"
        em_dash_isbn = "978—4—04—400417—0"
        nbsp_isbn = "978 4 04 400417 0"
        for variant in (en_dash_isbn, em_dash_isbn, nbsp_isbn):
            ok, _ = vi.validate_isbn(variant)
            self.assertTrue(ok, f"variant {variant!r} should be valid")


class DoiPatternTests(unittest.TestCase):
    def test_prims_doi(self) -> None:
        ok, _ = vi.validate_doi("10.4171/PRIMS/57-1-1")
        self.assertTrue(ok)

    def test_arxiv_style_rejected(self) -> None:
        ok, _ = vi.validate_doi("arXiv:2505.10568")
        self.assertFalse(ok)

    def test_no_slash_rejected(self) -> None:
        ok, _ = vi.validate_doi("not-a-doi")
        self.assertFalse(ok)

    def test_short_registrant(self) -> None:
        # ANSI/NISO Z39.84 requires at least 4-digit registrant prefix
        ok, _ = vi.validate_doi("10.123/foo")
        self.assertFalse(ok)


class CollectIdentifiersTests(unittest.TestCase):
    def test_returns_doi_and_isbn(self) -> None:
        with TemporaryDirectory() as td:
            data = Path(td)
            _write_sample(data)
            triples = vi.collect_identifiers(data)
        kinds = sorted({t[1] for t in triples})
        self.assertEqual(kinds, ["doi", "isbn"])
        self.assertEqual(len(triples), 5)


class VerifyOneOfflineTests(unittest.TestCase):
    def test_valid_doi_offline(self) -> None:
        out = vi.verify_one(
            "evidence:x", "doi", "10.4171/PRIMS/57-1-1",
            check_doi=False, check_isbn=False,
        )
        self.assertEqual(out.status, "valid_offline")

    def test_invalid_doi_offline(self) -> None:
        out = vi.verify_one(
            "evidence:y", "doi", "not-a-doi",
            check_doi=False, check_isbn=False,
        )
        self.assertEqual(out.status, "invalid")

    def test_valid_isbn_offline(self) -> None:
        out = vi.verify_one(
            "evidence:z", "isbn", "978-4-04-400417-0",
            check_doi=False, check_isbn=False,
        )
        self.assertEqual(out.status, "valid_offline")

    def test_invalid_isbn_offline(self) -> None:
        out = vi.verify_one(
            "evidence:w", "isbn", "978-4-04-400417-9",
            check_doi=False, check_isbn=False,
        )
        self.assertEqual(out.status, "invalid")


class VerifyDoiNetworkTests(unittest.TestCase):
    def test_alive_status(self) -> None:
        with mock.patch.object(vi, "_http_head", return_value=(302, "head ok")):
            status, detail = vi.verify_doi_network("10.4171/PRIMS/57-1-1")
        self.assertEqual(status, "alive")
        self.assertIn("302", detail)

    def test_invalid_status(self) -> None:
        with mock.patch.object(vi, "_http_head", return_value=(404, "http error")):
            status, _ = vi.verify_doi_network("10.4171/PRIMS/57-1-1")
        self.assertEqual(status, "invalid")

    def test_unresolved_status(self) -> None:
        with mock.patch.object(vi, "_http_head", return_value=(None, "timeout")):
            status, _ = vi.verify_doi_network("10.4171/PRIMS/57-1-1")
        self.assertEqual(status, "unresolved")


class _MockResponse:
    """Minimal urlopen() context-manager stand-in."""

    def __init__(self, status: int, body: bytes = b"") -> None:
        self.status = status
        self._body = body

    def read(self) -> bytes:
        return self._body

    def __enter__(self):  # noqa: D401
        return self

    def __exit__(self, *exc) -> bool:
        return False


def _fake_404(url: str) -> HTTPError:
    return HTTPError(url=url, code=404, msg="Not Found", hdrs=None, fp=None)


def _ndl_body(total_results: int) -> bytes:
    return (
        f'<?xml version="1.0"?>'
        f'<rss xmlns:openSearch="http://a9.com/-/spec/opensearch/1.1/">'
        f"<openSearch:totalResults>{total_results}</openSearch:totalResults>"
        f"</rss>"
    ).encode("utf-8")


class VerifyIsbnNetworkTests(unittest.TestCase):
    def test_non_jp_open_library_404_is_unresolved_no_ndl_call(self) -> None:
        """Non-Japanese ISBN with Open Library 404 stays at unresolved
        without consulting NDL (NDL is the Japanese national library)."""
        en_isbn = "0-7864-0700-X"  # ISBN-10, group 0 = English
        with mock.patch.object(
            vi, "urlopen", side_effect=_fake_404("https://openlibrary.org/...")
        ) as mock_open:
            status, detail = vi.verify_isbn_network(en_isbn)
        self.assertEqual(status, "unresolved")
        self.assertIn("en coverage", detail)
        self.assertEqual(mock_open.call_count, 1, "NDL must not be queried for non-jp ISBN")

    def test_jp_open_library_404_ndl_zero_hits_is_invalid(self) -> None:
        """R7-class fabrication signal: structurally valid Japanese ISBN
        that is in *neither* Open Library nor the National Diet Library
        is highly likely to be fabricated."""
        jp_isbn = "978-4-04-400417-0"

        def side_effect(request, timeout=None):
            url = request.full_url if hasattr(request, "full_url") else str(request)
            if "openlibrary.org" in url:
                raise _fake_404(url)
            if "ndl.go.jp" in url:
                return _MockResponse(200, _ndl_body(0))
            raise AssertionError(f"unexpected url: {url}")

        with mock.patch.object(vi, "urlopen", side_effect=side_effect):
            status, detail = vi.verify_isbn_network(jp_isbn)
        self.assertEqual(status, "invalid")
        self.assertIn("total_results=0", detail)

    def test_jp_open_library_404_ndl_hit_is_alive(self) -> None:
        jp_isbn = "978-4-04-400417-0"

        def side_effect(request, timeout=None):
            url = request.full_url if hasattr(request, "full_url") else str(request)
            if "openlibrary.org" in url:
                raise _fake_404(url)
            return _MockResponse(200, _ndl_body(1))

        with mock.patch.object(vi, "urlopen", side_effect=side_effect):
            status, detail = vi.verify_isbn_network(jp_isbn)
        self.assertEqual(status, "alive")
        self.assertIn("ndl total_results=1", detail)

    def test_jp_open_library_404_ndl_transport_error_is_unresolved(self) -> None:
        """Don't fail CI on NDL network flake — keep at unresolved."""
        jp_isbn = "978-4-04-400417-0"

        def side_effect(request, timeout=None):
            url = request.full_url if hasattr(request, "full_url") else str(request)
            if "openlibrary.org" in url:
                raise _fake_404(url)
            from urllib.error import URLError
            raise URLError("temporary network failure")

        with mock.patch.object(vi, "urlopen", side_effect=side_effect):
            status, detail = vi.verify_isbn_network(jp_isbn)
        self.assertEqual(status, "unresolved")
        self.assertIn("ndl url error", detail)

    def test_open_library_2xx_is_alive_no_ndl_call(self) -> None:
        jp_isbn = "978-4-04-400417-0"
        with mock.patch.object(
            vi, "urlopen", return_value=_MockResponse(200, b"{}")
        ) as mock_open:
            status, detail = vi.verify_isbn_network(jp_isbn)
        self.assertEqual(status, "alive")
        self.assertIn("open-library", detail)
        self.assertEqual(mock_open.call_count, 1, "NDL fallback must not run on OL hit")


class JapaneseIsbnDetectionTests(unittest.TestCase):
    def test_isbn13_978_4_is_japanese(self) -> None:
        self.assertTrue(vi._is_japanese_isbn("9784044004170"))

    def test_isbn13_978_0_is_not_japanese(self) -> None:
        self.assertFalse(vi._is_japanese_isbn("9780786407002"))

    def test_isbn10_starting_4_is_japanese(self) -> None:
        self.assertTrue(vi._is_japanese_isbn("4044004176"))

    def test_isbn10_starting_0_is_not_japanese(self) -> None:
        self.assertFalse(vi._is_japanese_isbn("0786407008"))

    def test_invalid_length_is_not_japanese(self) -> None:
        self.assertFalse(vi._is_japanese_isbn("123"))


class CLIOfflineTests(unittest.TestCase):
    def test_invalid_id_returns_one(self) -> None:
        with TemporaryDirectory() as td:
            data = Path(td)
            _write_sample(data)
            rc = vi.main(["--data", str(data)])
        self.assertEqual(rc, 1)

    def test_real_data_offline_returns_zero(self) -> None:
        # Real repo data should have all valid DOI/ISBN values after v0.6.1
        rc = vi.main(["--data", str(REPO_ROOT / "data")])
        self.assertEqual(rc, 0)


if __name__ == "__main__":
    unittest.main()
