#!/bin/bash
# Maintenance Page - test suite
# Usage: bash tests/run.sh
# Needs Python 3 and Node; the dev-server checks also use PHP 7.4 ($PHP_BIN, php74, php7.4,
# %LOCALAPPDATA%\Programs\PHP\7.4\php.exe or php) and are skipped without it. No other dependencies.
set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

PY="${PYTHON:-}"
if [ -z "$PY" ]; then
    for candidate in python3 python; do
        if "$candidate" -c 'import sys; sys.exit(sys.version_info < (3, 6))' >/dev/null 2>&1; then PY="$candidate"; break; fi
    done
fi
if [ -z "$PY" ]; then
    echo "Python 3 is needed to run the tests." >&2
    exit 1
fi

exec "$PY" -m unittest discover -s "$DIR" -p 'test_*.py' "$@"
