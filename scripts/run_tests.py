#!/usr/bin/env python3
"""Simple test runner script for Poetry."""

import subprocess
import sys


def main():
    """Run pytest tests."""
    return subprocess.call([sys.executable, "-m", "pytest", "-s", "--color=yes"])


if __name__ == "__main__":
    sys.exit(main())