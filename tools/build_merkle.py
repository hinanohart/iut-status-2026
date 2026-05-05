#!/usr/bin/env python3
"""Build a Merkle root for the IUT claim graph.

Produces a single SHA-256 hex string that uniquely identifies the
content of every JSON-LD record (entities, claims, evidence,
timeline). Two graphs with bit-identical content produce identical
roots; a single-byte change anywhere produces a different root.

This is the **physical-layer drift-resistance** complement to the
IRI-level drift-resistance provided by the JSON-LD design. When this
root is committed in `data/merkle_root.txt` and embedded in a git
commit, anyone can verify (with `tools/verify_merkle.py`) that the
graph state at that commit has not been tampered with.

When LANA produces formal `theorem` bodies in 2026-Q3+, the Merkle
root at the moment of formalization can be embedded in the Lean
artefact, giving a cryptographic anchor between the unformalized
JSON-LD and the formalized Lean.

Algorithm
---------
1. For each of the four data files (entities, claims, evidence,
   timeline), serialize the `@graph` array to canonical JSON
   (`sort_keys=True`, `separators=(",", ":")`, `ensure_ascii=False`,
   UTF-8 encoded).
2. Per-record SHA-256 over the canonical bytes — these are the
   Merkle leaves. Sorted by IRI (`id` field) for deterministic order.
3. Pair-wise Merkle hash up the tree. If a level has an odd number
   of nodes, duplicate the last node (Bitcoin-style) before pairing.
4. The root is the topmost hash in hex.

Invariants
----------
- Order of files in input does not matter (all four are concatenated
  in fixed order: entities, claims, evidence, timeline).
- Whitespace, key ordering, and Unicode normalization within each
  record do not affect the hash.
- Removing or adding any record changes the root.
- Reordering records does not change the root (leaves are sorted
  by IRI before hashing).

Stdlib only. No external dependencies.

Usage::

    python tools/build_merkle.py
    # writes data/merkle_root.txt and prints root to stdout
"""
from __future__ import annotations

import hashlib
import json
import logging
import sys
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
ROOT_FILE = DATA_DIR / "merkle_root.txt"

DATA_FILES = ("entities.json", "claims.json", "evidence.json", "timeline.json")


def canonical_bytes(record: dict[str, Any]) -> bytes:
    """Serialize a JSON record canonically: sorted keys, minimal separators, UTF-8."""
    return json.dumps(
        record,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")


def leaf_hash(record: dict[str, Any]) -> bytes:
    """SHA-256 of the canonical encoding of a single record."""
    return hashlib.sha256(canonical_bytes(record)).digest()


def parent_hash(left: bytes, right: bytes) -> bytes:
    """SHA-256 of the concatenation of two child hashes."""
    return hashlib.sha256(left + right).digest()


def merkle_root(leaves: list[bytes]) -> bytes:
    """Compute a Merkle root from a list of leaf hashes.

    Empty input returns the SHA-256 of the empty byte string (32 bytes).
    Single-leaf input returns that leaf.
    For odd-length levels, the last hash is duplicated before pairing.
    """
    if not leaves:
        return hashlib.sha256(b"").digest()

    level = list(leaves)
    while len(level) > 1:
        if len(level) % 2 == 1:
            level = level + [level[-1]]
        next_level: list[bytes] = []
        for i in range(0, len(level), 2):
            next_level.append(parent_hash(level[i], level[i + 1]))
        level = next_level
    return level[0]


def collect_leaves(data_dir: Path) -> list[bytes]:
    """Read all four data files, sort each `@graph` by `id`, return leaf hashes."""
    all_leaves: list[bytes] = []
    for filename in DATA_FILES:
        path = data_dir / filename
        if not path.exists():
            raise FileNotFoundError(f"required data file missing: {path}")
        with path.open("r", encoding="utf-8") as fh:
            doc = json.load(fh)
        graph = doc.get("@graph")
        if not isinstance(graph, list):
            raise ValueError(f"{path} missing @graph array")
        sorted_records = sorted(graph, key=lambda r: r.get("id", ""))
        for record in sorted_records:
            all_leaves.append(leaf_hash(record))
    return all_leaves


def build_root(data_dir: Path = DATA_DIR) -> str:
    """Compute the canonical Merkle root in hex."""
    leaves = collect_leaves(data_dir)
    root = merkle_root(leaves)
    return root.hex()


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    root_hex = build_root()
    ROOT_FILE.write_text(root_hex + "\n", encoding="utf-8")
    logger.info("Merkle root written to %s", ROOT_FILE.relative_to(REPO_ROOT))
    print(root_hex)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
