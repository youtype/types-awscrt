#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $0))
cd $ROOT_PATH

poetry run npx pyright awscrt-stubs
poetry run flake8 awscrt-stubs
poetry run black awscrt-stubs
poetry run isort awscrt-stubs
poetry run mypy awscrt-stubs
poetry run istub -u
