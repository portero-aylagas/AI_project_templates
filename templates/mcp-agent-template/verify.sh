#!/usr/bin/env sh
set -eu

PYTHON="${PYTHON:-python3}"
"$PYTHON" -m compileall -q src tests
"$PYTHON" -m ruff check .
"$PYTHON" -m pytest -q

