#!/bin/bash
# TODO make this cleaner / platform-independent
set -e

# enter venv if needed
if [[ -z "$VIRTUAL_ENV" ]]; then
    activate_script='tests_venv/bin/activate'
    [[ -f "$activate_script" ]] || ./setup_tests.sh
    source "$activate_script"
elif [[ ! -f "$VIRTUAL_ENV/.genanki-tests-marker" ]]; then
    ./setup_tests.sh
else
    echo 'Tests are set up!' 1>&2
fi

exec python -m pytest tests/
