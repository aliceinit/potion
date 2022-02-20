#!/usr/bin/env bash

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" &> /dev/null && pwd)
TEST_DIR="${SCRIPT_DIR}/test_app"
VENV_DIR=${SCRIPT_DIR}/venv

# Check if we are in the right virtual_env
if [[ -z "$VIRTUAL_ENV" || "${VIRTUAL_ENV}" != "${VENV_DIR}" ]]; then
    echo "No VIRTUAL_ENV set"
    ${VENV_DIR}/bin/activate
fi

# Add this script's directory to the pythonpath
export PYTHONPATH=${PYTHONPATH}:${SCRIPT_DIR}


python ${TEST_DIR}/app.py &
FLASK_PID=$!

python -m pytest ${TEST_DIR}

kill ${FLASK_PID}