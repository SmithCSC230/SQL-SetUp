#!/usr/bin/env python3
"""
Minimal MySQL connection tester for CSC230.

Usage:
  python mysql_test.py --host 127.0.0.1 --user root --database mysql
  python mysql_test.py --host db.example.edu --user alice --database school --port 3306

Password will be requested securely at runtime.
"""

from __future__ import annotations

import argparse
import getpass
import sys

import mysql.connector
from mysql.connector import Error


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Test a MySQL connection.")
    parser.add_argument("--host", required=True, help="MySQL server hostname/IP")
    parser.add_argument("--user", required=True, help="MySQL username")
    parser.add_argument("--database", required=True, help="Database name")
    parser.add_argument("--port", type=int, default=3306, help="MySQL port (default: 3306)")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    password = getpass.getpass("MySQL password: ")

    try:
        connection = mysql.connector.connect(
            host=args.host,
            port=args.port,
            user=args.user,
            password=password,
            database=args.database,
            connection_timeout=10,
        )

        if not connection.is_connected():
            print("Connection failed (not connected).")
            return 1

        cursor = connection.cursor()
        cursor.execute("SELECT VERSION()")
        (version,) = cursor.fetchone()
        print("Connected successfully.")
        print(f"MySQL version: {version}")

        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        if tables:
            print("\nTables in database:")
            for (table_name,) in tables:
                print(f" - {table_name}")
        else:
            print("\nNo tables found in this database.")

        cursor.close()
        connection.close()
        return 0

    except Error as err:
        print(f"MySQL error: {err}")
        return 2
    except KeyboardInterrupt:
        print("\nCancelled.")
        return 130


if __name__ == "__main__":
    sys.exit(main())
