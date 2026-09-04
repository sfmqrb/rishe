#!/bin/sh
# Publish the verification state safely:
#   1. push branch `verified` (no reference library) to the PUBLIC remote `origin`
#      (the pre-push hook refuses if the tree ever contains data/verification/sources/refs/);
#   2. update the PRIVATE backup: in a separate worktree on `verified-with-sources`, merge
#      `verified`, copy the reference library in, commit, push to remote `private` only.
# Never checks out verified-with-sources in the main working tree (that deletes the library).
set -e
ROOT=$(cd "$(dirname "$0")/.." && pwd)
cd "$ROOT"
[ "$(git rev-parse --abbrev-ref HEAD)" = "verified" ] || { echo "run from branch 'verified'"; exit 1; }
[ -z "$(git status --porcelain --untracked-files=no)" ] || { echo "commit first (tracked changes pending)"; exit 1; }
if git ls-tree -r --name-only verified | grep -q '^data/verification/sources/refs/'; then
  echo "ABORT: branch verified tracks the reference library"; exit 1; fi
echo "== public: pushing verified -> origin"
git push -q origin verified
BK="$ROOT/../rishe-backup"
if [ ! -d "$BK" ]; then git worktree add -q "$BK" verified-with-sources; fi
echo "== private: updating backup worktree"
( cd "$BK" && git checkout -q verified-with-sources && git merge -q --no-edit verified \
  && rsync -a --delete --exclude 'tessdata/' --exclude '_tessdata/' --exclude '*_pages.txt.pages/' \
       --exclude 'Bailey_Studies_1930-1993_bedrosian.pdf' \
       "$ROOT/data/verification/sources/refs/" "$BK/data/verification/sources/refs/" \
  && git add -A && { git diff --cached --quiet || git commit -q -m "Backup: sync reference library $(date -u +%Y-%m-%dT%H:%MZ)"; } \
  && git push -q private verified-with-sources )
echo "== done: origin/verified = $(git rev-parse --short origin/verified), private/verified-with-sources = $(git rev-parse --short private/verified-with-sources)"
