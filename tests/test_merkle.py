"""Tests for the Merkle provenance chain.

The Merkle root must be:
1. Computable from the data files alone.
2. Deterministic (same input always produces same output).
3. Sensitive to any single-byte change in any record.
4. Insensitive to record reordering within a file.
5. Match what is committed in `data/merkle_root.txt`.

Run with::

    python -m unittest tests.test_merkle -v
"""
from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.build_merkle import (  # noqa: E402
    DATA_FILES,
    ROOT_FILE,
    build_root,
    canonical_bytes,
    leaf_hash,
    merkle_root,
)

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"


class CanonicalEncodingTests(unittest.TestCase):
    """Canonical JSON encoding must be order-independent and whitespace-free."""

    def test_keys_sorted(self) -> None:
        a = {"b": 1, "a": 2}
        b = {"a": 2, "b": 1}
        self.assertEqual(canonical_bytes(a), canonical_bytes(b))

    def test_no_whitespace(self) -> None:
        out = canonical_bytes({"a": 1, "b": [2, 3]})
        self.assertNotIn(b" ", out)
        self.assertNotIn(b"\n", out)

    def test_utf8_preserved(self) -> None:
        out = canonical_bytes({"label": "望月新一"})
        self.assertIn("望月新一".encode("utf-8"), out)


class MerkleRootTests(unittest.TestCase):
    """The Merkle root must satisfy structural cryptographic properties."""

    def test_empty(self) -> None:
        import hashlib
        self.assertEqual(merkle_root([]).hex(), hashlib.sha256(b"").hexdigest())

    def test_single_leaf(self) -> None:
        leaf = leaf_hash({"id": "x"})
        self.assertEqual(merkle_root([leaf]), leaf)

    def test_deterministic(self) -> None:
        leaves = [leaf_hash({"id": f"r{i}"}) for i in range(5)]
        r1 = merkle_root(leaves)
        r2 = merkle_root(leaves)
        self.assertEqual(r1, r2)

    def test_odd_length_duplication(self) -> None:
        leaves = [leaf_hash({"id": f"r{i}"}) for i in range(3)]
        # Should not raise; odd-length levels duplicate the last leaf.
        r = merkle_root(leaves)
        self.assertEqual(len(r), 32)


class GraphRootTests(unittest.TestCase):
    """The published Merkle root must match the recomputed root."""

    def test_committed_root_matches_recomputed(self) -> None:
        if not ROOT_FILE.exists():
            self.skipTest(
                "data/merkle_root.txt not present; run build_merkle.py first."
            )
        committed = ROOT_FILE.read_text(encoding="utf-8").strip()
        recomputed = build_root()
        self.assertEqual(committed, recomputed,
                         "Merkle root mismatch: rebuild with tools/build_merkle.py")


class TamperDetectionTests(unittest.TestCase):
    """A single-byte change in any data file must change the root."""

    def setUp(self) -> None:
        self.original_root = build_root()

    def test_modified_record_changes_root(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_dir = Path(tmp)
            for filename in DATA_FILES:
                src = DATA_DIR / filename
                dst = tmp_dir / filename
                doc = json.loads(src.read_text(encoding="utf-8"))
                if filename == "claims.json":
                    doc = copy.deepcopy(doc)
                    if doc["@graph"]:
                        doc["@graph"][0]["label"] = doc["@graph"][0]["label"] + " [TAMPERED]"
                dst.write_text(json.dumps(doc, ensure_ascii=False), encoding="utf-8")

            tampered_root = build_root(tmp_dir)
            self.assertNotEqual(self.original_root, tampered_root,
                                "tamper-detection failed: modifying a claim "
                                "label did not change the root")

    def test_record_reorder_does_not_change_root(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_dir = Path(tmp)
            for filename in DATA_FILES:
                src = DATA_DIR / filename
                dst = tmp_dir / filename
                doc = json.loads(src.read_text(encoding="utf-8"))
                if filename == "claims.json":
                    doc = copy.deepcopy(doc)
                    doc["@graph"] = list(reversed(doc["@graph"]))
                dst.write_text(json.dumps(doc, ensure_ascii=False), encoding="utf-8")

            reordered_root = build_root(tmp_dir)
            self.assertEqual(self.original_root, reordered_root,
                             "reorder-stability failed: reversing claim order "
                             "changed the root (leaves should be sorted by id)")


if __name__ == "__main__":
    unittest.main()
