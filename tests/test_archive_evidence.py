"""Tests for tools/archive_evidence.py — Wayback Machine bootstrap.

Network-touching code paths (lookup, submit) are not exercised here;
they are exercised manually via ``--network`` CLI runs and via
``cold_start_evidence.md`` follow-up reports. These tests cover the
offline contract: collect_records, render_summary, apply_to_data,
CLI argument validation, and the ``ArchiveOutcome`` dataclass shape.
"""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from tools import archive_evidence as ae  # noqa: E402


SAMPLE_EVIDENCE = {
    "@context": "./context.jsonld",
    "@graph": [
        {
            "id": "evidence:Sample_with_url",
            "type": "Paper",
            "label": "Sample paper with URL but no archive_url",
            "url": "https://example.com/paper.pdf",
        },
        {
            "id": "evidence:Sample_with_archive",
            "type": "Paper",
            "label": "Sample paper already archived",
            "url": "https://example.com/already.pdf",
            "archive_url": (
                "https://web.archive.org/web/20240101000000/"
                "https://example.com/already.pdf"
            ),
        },
        {
            "id": "evidence:Sample_no_url",
            "type": "Paper",
            "label": "Sample paper without URL field",
        },
    ],
}

SAMPLE_TIMELINE = {
    "@context": "./context.jsonld",
    "@graph": [
        {
            "id": "event:sample_with_url",
            "type": "event",
            "label": "Sample event with URL",
            "date": "2024-01-01",
            "url": "https://example.com/event",
        },
    ],
}


def _write_sample(data_dir: Path) -> None:
    (data_dir / "evidence.json").write_text(
        json.dumps(SAMPLE_EVIDENCE, indent=2) + "\n", encoding="utf-8"
    )
    (data_dir / "timeline.json").write_text(
        json.dumps(SAMPLE_TIMELINE, indent=2) + "\n", encoding="utf-8"
    )


class CollectRecordsTests(unittest.TestCase):
    def test_classifies_records_correctly(self) -> None:
        with TemporaryDirectory() as td:
            data = Path(td)
            _write_sample(data)
            outcomes = ae.collect_records(data)
        actions = {o.record_id: o.action for o in outcomes}
        self.assertEqual(actions["evidence:Sample_with_url"], "missing")
        self.assertEqual(actions["evidence:Sample_with_archive"], "present")
        self.assertEqual(actions["evidence:Sample_no_url"], "skipped")
        self.assertEqual(actions["event:sample_with_url"], "missing")
        self.assertEqual(len(outcomes), 4)


class ApplyToDataTests(unittest.TestCase):
    def test_apply_populates_archive_url_field(self) -> None:
        with TemporaryDirectory() as td:
            data = Path(td)
            _write_sample(data)
            archive_url = (
                "https://web.archive.org/web/20260101000000/"
                "https://example.com/paper.pdf"
            )
            outcomes = [
                ae.ArchiveOutcome(
                    record_id="evidence:Sample_with_url",
                    kind="evidence",
                    url="https://example.com/paper.pdf",
                    archive_url=archive_url,
                    action="found",
                    detail="snapshot 20260101000000",
                ),
            ]
            written = ae.apply_to_data(outcomes, data)
            self.assertEqual(written, 1)
            with (data / "evidence.json").open(encoding="utf-8") as fh:
                doc = json.load(fh)
            target = next(
                r for r in doc["@graph"]
                if r["id"] == "evidence:Sample_with_url"
            )
            self.assertEqual(target["archive_url"], archive_url)

    def test_apply_handles_duplicate_url_records_correctly(self) -> None:
        # Round 9 audit (v0.7.8): regression test for run_submit's
        # outcomes.index(o) bug where frozen dataclass eq=True could
        # let two records sharing all fields collapse on .index() and
        # shift the remaining slice. apply_to_data uses record_id as
        # primary key, so duplicate records (synthetic test) must
        # update independently if they have different IDs.
        with TemporaryDirectory() as td:
            data = Path(td)
            sample = {
                "@context": "./context.jsonld",
                "@graph": [
                    {
                        "id": "evidence:Dup_A",
                        "type": "Paper",
                        "label": "duplicate URL test record A",
                        "url": "https://example.com/dup.pdf",
                    },
                    {
                        "id": "evidence:Dup_B",
                        "type": "Paper",
                        "label": "duplicate URL test record B",
                        "url": "https://example.com/dup.pdf",
                    },
                ],
            }
            (data / "evidence.json").write_text(
                json.dumps(sample, indent=2) + "\n", encoding="utf-8"
            )
            (data / "timeline.json").write_text(
                json.dumps({"@graph": []}, indent=2) + "\n", encoding="utf-8"
            )
            outcomes = [
                ae.ArchiveOutcome(
                    record_id="evidence:Dup_A",
                    kind="evidence",
                    url="https://example.com/dup.pdf",
                    archive_url="https://web.archive.org/web/2024A/x",
                    action="found",
                    detail="A",
                ),
                ae.ArchiveOutcome(
                    record_id="evidence:Dup_B",
                    kind="evidence",
                    url="https://example.com/dup.pdf",
                    archive_url="https://web.archive.org/web/2024B/x",
                    action="found",
                    detail="B",
                ),
            ]
            written = ae.apply_to_data(outcomes, data)
            self.assertEqual(written, 2)
            doc = json.loads((data / "evidence.json").read_text(encoding="utf-8"))
            urls = {r["id"]: r.get("archive_url") for r in doc["@graph"]}
            self.assertEqual(urls["evidence:Dup_A"], "https://web.archive.org/web/2024A/x")
            self.assertEqual(urls["evidence:Dup_B"], "https://web.archive.org/web/2024B/x")

    def test_apply_does_not_overwrite_existing(self) -> None:
        with TemporaryDirectory() as td:
            data = Path(td)
            _write_sample(data)
            outcomes = [
                ae.ArchiveOutcome(
                    record_id="evidence:Sample_with_archive",
                    kind="evidence",
                    url="https://example.com/already.pdf",
                    archive_url="https://web.archive.org/web/9999/",
                    action="found",
                    detail="should not overwrite",
                ),
            ]
            written = ae.apply_to_data(outcomes, data)
            self.assertEqual(written, 0)
            with (data / "evidence.json").open(encoding="utf-8") as fh:
                doc = json.load(fh)
            target = next(
                r for r in doc["@graph"]
                if r["id"] == "evidence:Sample_with_archive"
            )
            self.assertNotEqual(
                target["archive_url"], "https://web.archive.org/web/9999/"
            )


class RenderSummaryTests(unittest.TestCase):
    def test_render_includes_action_groups(self) -> None:
        outcomes = [
            ae.ArchiveOutcome(
                record_id="evidence:A", kind="evidence",
                url="https://x.test/a", archive_url=None,
                action="missing", detail="needs lookup",
            ),
            ae.ArchiveOutcome(
                record_id="evidence:B", kind="evidence",
                url="https://x.test/b", archive_url="https://web.archive.org/web/2024/x",
                action="present", detail="already populated",
            ),
        ]
        summary = ae.render_summary(outcomes)
        self.assertIn("missing: 1", summary)
        self.assertIn("present: 1", summary)
        self.assertIn("evidence:A", summary)
        self.assertIn("evidence:B", summary)


class LookupOneTests(unittest.TestCase):
    def test_lookup_parses_availability_response(self) -> None:
        api_payload = {
            "url": "https://example.com/paper.pdf",
            "archived_snapshots": {
                "closest": {
                    "available": True,
                    "url": (
                        "https://web.archive.org/web/20240101000000/"
                        "https://example.com/paper.pdf"
                    ),
                    "timestamp": "20240101000000",
                    "status": "200",
                }
            },
        }
        with mock.patch.object(
            ae, "_http_get_json", return_value=api_payload
        ):
            archive_url, detail = ae.lookup_one("https://example.com/paper.pdf")
        self.assertEqual(
            archive_url,
            "https://web.archive.org/web/20240101000000/"
            "https://example.com/paper.pdf",
        )
        self.assertIn("20240101000000", detail)

    def test_lookup_returns_none_when_no_snapshot(self) -> None:
        with mock.patch.object(
            ae, "_http_get_json", return_value={"archived_snapshots": {}}
        ):
            archive_url, detail = ae.lookup_one("https://example.com/none.pdf")
        self.assertIsNone(archive_url)
        self.assertIn("no snapshot", detail.lower())

    def test_lookup_rejects_non_http_scheme(self) -> None:
        archive_url, detail = ae.lookup_one("ftp://example.com/paper.pdf")
        self.assertIsNone(archive_url)
        self.assertIn("non-http scheme", detail)


class CLIOfflineTests(unittest.TestCase):
    def test_lookup_without_network_exits_2(self) -> None:
        with TemporaryDirectory() as td:
            data = Path(td)
            _write_sample(data)
            rc = ae.main(["--data", str(data), "--lookup"])
        self.assertEqual(rc, 2)

    def test_apply_without_action_exits_2(self) -> None:
        with TemporaryDirectory() as td:
            data = Path(td)
            _write_sample(data)
            rc = ae.main(["--data", str(data), "--apply"])
        self.assertEqual(rc, 2)

    def test_offline_default_returns_zero(self) -> None:
        with TemporaryDirectory() as td:
            data = Path(td)
            _write_sample(data)
            rc = ae.main(["--data", str(data)])
        self.assertEqual(rc, 0)


if __name__ == "__main__":
    unittest.main()
