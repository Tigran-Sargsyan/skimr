#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

uv sync
uv run python -m pipeline.main

cd site
npm ci || npm install
npm run dev
