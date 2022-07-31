#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $0))
cd $ROOT_PATH

npx pyright awscrt-stubs
flake8 awscrt-stubs
black awscrt-stubs
isort awscrt-stubs
mypy awscrt-stubs
python -m istub -u
