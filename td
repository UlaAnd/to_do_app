#!/usr/bin/env bash

prefix=""

set -x

lint() {
  ${prefix} isort . &&
  ${prefix} black . --exclude venv &&
  ${prefix} mypy .  &&
  ${prefix} flake8 .
}

"$@"