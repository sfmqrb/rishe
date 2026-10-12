#!/bin/sh
# Validate, build, commit everything, publish (public + private), and deploy the site.
# usage: sh tools/verify_commit_deploy.sh /path/to/commit-message.txt
# The message file must already carry the Co-Authored-By / Claude-Session trailers.
# Stops before committing if validation fails, the JS does not parse, or any file under
# data/verification/sources/refs/ (copyrighted reference library) is staged.
cd "$(dirname "$0")/.." || exit 1
[ "$(git rev-parse --abbrev-ref HEAD)" = "verified" ] || { echo "run on branch verified"; exit 1; }
[ -f "$1" ] || { echo "usage: $0 message-file"; exit 1; }
V=$(python3 tools/validate.py data/extracted/batch | tail -1); echo "$V"
case "$V" in *" 0 errors"*) ;; *) echo "VALIDATE FAILED - nothing committed"; exit 1;; esac
python3 tools/build_site.py data/extracted/batch -o site/risheh.html | tail -1 || exit 1
node tools/jscheck.js | tail -1 || exit 1
git add -A
if git diff --cached --name-only | grep -q 'sources/refs/'; then
  echo "REFERENCE LIBRARY STAGED - aborting"; git reset -q; exit 1; fi
git diff --cached --quiet && { echo "nothing to commit"; exit 0; }
git commit -q -F "$1" && git log --oneline -1
sh tools/verify_publish.sh 2>&1 | tail -1
git push -q origin verified && git push -q private verified
git merge-base --is-ancestor main verified && git push -q origin verified:main \
  && git push -q private verified:main && git branch -f main verified \
  && echo "deployed main=$(git rev-parse --short main)"
