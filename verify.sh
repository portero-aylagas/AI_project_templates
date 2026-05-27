#!/usr/bin/env sh
set -eu

PYTHON="${PYTHON:-python3}"
MAKE="${MAKE:-make}"

"$MAKE" verify PYTHON="$PYTHON"
