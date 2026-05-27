#!/usr/bin/env sh
set -eu

PYTHON="${PYTHON:-python3}"
"$PYTHON" scripts/verify_templates.py

