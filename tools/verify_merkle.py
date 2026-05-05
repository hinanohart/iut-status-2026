#!/usr/bin/env python3
"""Verify the IUT claim graph against the committed Merkle root.

Recomputes the Merkle root from `data/*.json` and compares against
the value stored in `data/merkle_root.txt`. Exit 0 = match (graph
unmodified since the root was committed); exit 1 = mismatch (graph
or root file changed without coordination).

CI runs this on every PR. A mismatch means either (a) the data was
changed and the maintainer forgot to rebuild the root with
`tools/build_merkle.py`, or (b) the root was tampered with.

Usage::

    python tools/verify_merkle.py
    # exit 0 = OK, exit 1 = MISMATCH

For external auditors (independent verifiers): clone the repo at any
commit, run this script. The git commit hash anchors the root in
git's own Merkle DAG; the JSON Merkle root anchors the JSON-LD
graph. Together they give cryptographic provenance for any reported
status snapshot.
"""
from __future__ import annotations

import logging
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from tools.build_merkle import ROOT_FILE, build_root  # noqa: E402

logger = logging.getLogger(__name__)


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    if not ROOT_FILE.exists():
        print(
            f"ERROR: {ROOT_FILE.relative_to(REPO_ROOT)} not found; "
            f"run `python tools/build_merkle.py` first.",
            file=sys.stderr,
        )
        return 1

    committed = ROOT_FILE.read_text(encoding="utf-8").strip()
    recomputed = build_root()

    if committed == recomputed:
        print(f"merkle: OK ({recomputed})")
        return 0

    print(
        f"ERROR: Merkle root mismatch.\n"
        f"  committed:  {committed}\n"
        f"  recomputed: {recomputed}\n"
        f"  data has changed since root was built; "
        f"run `python tools/build_merkle.py` if intentional.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
