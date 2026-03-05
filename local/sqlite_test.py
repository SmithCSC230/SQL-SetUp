#!/usr/bin/env python3
"""
Minimal SQLite connection tester for CSC230.

Usage:
  python sqlite_test.py
  python sqlite_test.py --db class_demo.db

SQLite ships with Python, so no external database server is required.
"""

from __future__ import annotations

import argparse
import sqlite3
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Test a SQLite database connection.")
    parser.add_argument(
        "--db",
        default="classroom.db",
        help="SQLite database file path (default: classroom.db)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    db_path = Path(args.db)

    try:
        db_path.parent.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(db_path)
        conn.execute("PRAGMA foreign_keys = ON")

        version = conn.execute("SELECT sqlite_version()") .fetchone()[0]
        print(f"Connected successfully to: {db_path.resolve()}")
        print(f"SQLite version: {version}")

        rows = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
        ).fetchall()

        if rows:
            print("\nTables in database:")
            for (name,) in rows:
                print(f" - {name}")
        else:
            print("\nNo tables found yet.")
            print("You can create some in the notebook activity.")

        conn.close()
        return 0
    except sqlite3.Error as err:
        print(f"SQLite error: {err}")
        return 2
    except KeyboardInterrupt:
        print("\nCancelled.")
        return 130


if __name__ == "__main__":
    sys.exit(main())
