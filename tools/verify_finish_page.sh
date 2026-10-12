#!/bin/sh
# Post-process one finished verification agent (no commit):
#   export its process log, archive the URLs it cites, run the coverage check.
# usage: sh tools/verify_finish_page.sh N /path/to/subagents/agent-<id>.jsonl
# The page passes only if the last line shows "nodes verified: k/k" and no PROBLEM lines.
set -e
N="$1"; T="$2"
[ -n "$N" ] && [ -f "$T" ] || { echo "usage: $0 N agent-transcript.jsonl"; exit 1; }
cd "$(dirname "$0")/.."
python3 tools/verify_export_process.py "$T" "verify-page-$N" | tail -1
python3 tools/verify_archive_sources.py "$N" | tail -1
python3 tools/verify_check.py "$N" | grep -E 'nodes verified|PROBLEM' || true
